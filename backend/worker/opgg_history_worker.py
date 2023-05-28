import functools
import pprint
import requests
import sys
import json
from datetime import datetime


def parse_data(data):
    games_array = []
    for game in data['data']:
        temp = {}
        stats = game['myData']['stats']
        temp['id'] = game['id']
        temp['created_at'] = game['created_at']
        temp['is_remake'] = game['is_remake']
        temp['team'] = game['myData']['team_key']
        temp['champion'] = game['myData']['champion_id']
        temp['result'] = stats['result']
        temp['kda'] = {'k': stats['kill'], 'd': stats['death'], 'a': stats['assist']}
        temp['rank'] = stats['op_score_rank']
        temp['team_mvp'] = stats['is_opscore_max_in_team']
        temp['game_mvp'] = True if stats['op_score_rank'] == '1' else False
        temp['stats'] = stats
        games_array.append(temp)
    return games_array


def only_games_after_id(data, id):
    filtered_games = []
    for game in data:
        if game['id'] != id:
            filtered_games.append(game)
        else:
            break
    return filtered_games


def filter_games_by_date(data, start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S%z")
    end = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S%z")
    filtered_games = []
    for game in data:
        time = datetime.strptime(game['created_at'], "%Y-%m-%dT%H:%M:%S%z")
        if start < time < end:
            filtered_games.append(game)
        else:
            break
    return filtered_games


def run(summoner_id, start_at, end_at, last_registered_game=None):
    headers = {
        'User-Agent': 'Chrome v22.2 Linux Ubuntu',
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'X-Requested-With': 'XMLHttpRequest'
    }
    page = f'https://op.gg/api/v1.0/internal/bypass/games/euw/summoners/{summoner_id}?&limit=20&hl=en_US&game_type' \
           f'=soloranked'
    res = requests.Session().get(url=page, headers=headers)
    res.raise_for_status()
    res_json = res.json()

    games = parse_data(res_json)

    if last_registered_game is not None:
        games = only_games_after_id(games, last_registered_game)
    games = filter_games_by_date(games, start_at, end_at)

    return games


if __name__ == '__main__':
    if sys.argv[3:]:
        if sys.argv[4:]:
            run(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
        else:
            run(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Invalid arguments passed")
