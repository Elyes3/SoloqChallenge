import time
import opgg_stats_worker
import opgg_history_worker
import schedule
import os
import requests
from requests import HTTPError
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file\
api_url = str(os.getenv('API_URL'))
summoner_update_interval = int(os.getenv('UPDATE_SUMMONERS_EVERY'))
summoner_renew_wait = int(os.getenv('SUMMONER_RENEW_WAIT'))


def fetch_challenge_details():
    print("fetching challenge details")
    try:
        res = requests.Session().get(url=api_url + "/challenge")
        res.raise_for_status()
        json = res.json()
        return json
    except HTTPError as e:
        print("Error fetching /challenge")
        print(e)
        return {}


def fetch_summoners():
    print("fetching summoners")
    try:
        res = requests.Session().get(url=api_url + "/summoner-names")
        res.raise_for_status()
        json = res.json()
        return json
    except HTTPError as e:
        print("Error fetching summoners")
        print(e)
        return []


def update_summoner(sid, data):
    try:
        response = requests.Session().post(url=api_url + f"/update/{sid}", json=data)
    except HTTPError:
        print("Error posting new data to api")
    if not response.ok:
        print("Failed to update summoner")


def update_match_history(sid, data):
    try:
        response = requests.Session().post(url=api_url + f"/matches/{sid}", json=data)
    except HTTPError:
        print("Error posting new data to api")
    if not response.ok:
        print("Failed to update match history")


def op_gg_renew(summoner_id):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/56.0.2924.76 Safari/537.36',
            "Upgrade-Insecure-Requests": "1", "DNT": "1",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate"}
        requests.Session().post(url="https://www.op.gg/api/v1.0/internal/bypass/summoners/euw/"
                                    f"{summoner_id}/renewal", headers=headers)
    except HTTPError:
        print("Error while sending renewal request")


def update_all_summoners():
    print("Summoner profile update started")

    details = fetch_challenge_details()

    # fetch all summoners
    players = fetch_summoners()
    print(f"{len(players)} profiles fetched")

    # renew all players data
    for player in players:
        # renew the op.gg data
        op_gg_renew(player['summoner_id'])
    print(f"called  op.gg renew, grace period set to {summoner_renew_wait} minutes")

    # wait for op.gg servers to renew the data
    time.sleep(60*summoner_renew_wait)

    print("grace period ended, fetching op.gg profile data")
    for player in players:
        data = opgg_stats_worker.run(player['summoner'])
        # update the data in the db
        update_summoner(player['id'], data)
        last_fetched_game_id = player.get('last_fetched_game', None)
        if last_fetched_game_id:
            games = opgg_history_worker.run(player['summoner_id'], details['start_date'], details['end_date'], last_fetched_game_id)
        else:
            games = opgg_history_worker.run(player['summoner_id'], details['start_date'], details['end_date'])

        print(f"{len(games)} games found for player {player['summoner']}")
        update_match_history(player['id'], games)
    print("Job ended successfully!")


schedule.every(summoner_update_interval).minutes.do(update_all_summoners)
print(f"Update summoners scheduled to run every {summoner_update_interval} minutes")
# Loop so that the scheduling task
# keeps on running all time.
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(5)
