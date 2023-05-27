import time
from requests import HTTPError
import opgg_worker
import schedule
import os
import requests
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file\
api_url = str(os.getenv('API_URL'))


def fetch_summoners():
    print("fetching summoners")
    try:
        res = requests.Session().get(url=api_url + "/summoner-names")
        res.raise_for_status()
        json = res.json()
        return json
    except HTTPError:
        print("Error fetching summoners")
        return []


def update_summoner(id, data):
    try:
        response = requests.Session().post(url=api_url + f"/update/{id}", json=data)
    except HTTPError:
        print("Error posting new data to api")
    if not response.ok:
        print("Failed to update summoner")


def op_gg_renew(summoner_id):
    try:
        requests.Session().post(url="https://www.op.gg/api/v1.0/internal/bypass/summoners/euw/"
                                    f"{summoner_id}/renewal")
    except HTTPError:
        print("Error while sending renewal request")


def update_all_summoners():
    # fetch all summoners
    players = fetch_summoners()
    # renew all players data
    for player in players:
        # renew the op.gg data
        op_gg_renew(player['summoner_id'])

    # wait for op.gg servers to renew the data
    time.sleep(5)

    for player in players:
        data = opgg_worker.run(player['summoner'])
        # update the data in the db
        update_summoner(player['id'], data)


# Update all summoners every 30mins
schedule.every(30).minutes.do(update_all_summoners)

# Loop so that the scheduling task
# keeps on running all time.
while True:
    # Checks whether a scheduled task
    # is pending to run or not
    schedule.run_pending()
    time.sleep(5)
