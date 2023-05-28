import functools
from requests_html import HTMLSession
from bs4 import *
import sys
import json


def run(arg):
    player = arg

    session = HTMLSession()

    page = f'https://euw.op.gg/summoner/userName={player}'
    html = session.get(page)
    soup = BeautifulSoup(html.content, 'html.parser')

    output = {'status': 'NOT_FOUND', 'summoner': player}
    try:
        data_raw = soup.find("script", {"id": "__NEXT_DATA__"}).text
        json_raw = json.loads(data_raw)

        data = json_raw['props']['pageProps']['data']

        output = {
            'summoner': data['name'],
            'icon_url': data['profile_image_url'],
            'level': data['level'],
            'summoner_id': data['summoner_id'],
        }

        for queue in data['league_stats']:
            if queue['queue_info']['game_type'] == 'SOLORANKED':
                output['tier'] = queue['tier_info']['tier']
                output['division'] = queue['tier_info']['division']
                output['lp'] = queue['tier_info']['lp']
                output['tier_image_url'] = queue['tier_info']['tier_image_url']
                output['border_image_url'] = queue['tier_info']['border_image_url']
                output['win'] = queue['win']
                output['lose'] = queue['lose']
                output['games'] = output['win'] or 0 + output['lose'] or 0
                output['is_hot_streak'] = queue['is_hot_streak']
                output['series'] = queue['series']
                output['last_updated_at'] = queue['updated_at']
                output['status'] = 'OK'
    except Exception as e:
        print(f"{e}: Error! url='{page}'")
        output['status'] = 'NOT_FOUND'
    return output


if __name__ == '__main__':
    run(sys.argv[1])
