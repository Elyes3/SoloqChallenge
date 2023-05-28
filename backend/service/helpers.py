def recalculate_stats(db, summoner_id):
    collection = db['matches']
    matches = collection.find({'summoner_id': summoner_id})

    stats = {
        'games_red_side': 0,
        'games_blue_side': 0,
        'win': 0,
        'lose': 0,
        'remake': 0,
        'games': 0,
        'kill': 0,
        'avg_kill': 0,
        'death': 0,
        'avg_death': 0,
        'assist': 0,
        'avg_assist': 0,
        'avg_kda': 0,
        'cs': 0,
        'avg_cs': 0,
        'wards_placed': 0,
        'avg_wards_placed': 0,
        'wards_destroyed': 0,
        'avg_wards_destroyed': 0,
        'vision_score': 0,
        'avg_vision_score': 0,
        'control_wards': 0,
        'avg_control_wards': 0,
        'damage_to_towers': 0,
        'avg_damage_to_towers': 0,
        'damage_to_champions': 0,
        'avg_damage_to_champions': 0,
        'gold': 0,
        'avg_gold': 0,
        'mvp': 0,
        'ace': 0,
        'avg_game_rank': 0,
        'total_game_rank': 0,
    }

    for match in matches:
        # COUNTED EVEN IN REMAKES
        if match['team'] == 'RED':
            stats['games_red_side'] = stats['games_red_side'] + 1
        else:
            stats['games_blue_side'] = stats['games_blue_side'] + 1
        # COUNTED EVEN IN REMAKES

        if match['is_remake'] == 'true':
            stats['remake'] = stats['remake'] + 1
            continue

        # NOT COUNTED EVEN IN REMAKES!
        stats['games'] = stats['games'] + 1
        if match['result'] == 'LOSE':
            stats['lose'] = stats['lose'] + 1
        else:
            stats['win'] = stats['win'] + 1

        # kills
        stats['kill'] = stats['kill'] + match['kda']['k']
        stats['avg_kill'] = stats['kill'] / stats['games']
        # deaths
        stats['death'] = stats['death'] + match['kda']['d']
        stats['avg_death'] = stats['death'] / stats['games']
        # assists
        stats['assist'] = stats['assist'] + match['kda']['a']
        stats['avg_assist'] = stats['assist'] / stats['games']
        # kda
        stats['avg_kda'] = (stats['kill'] + stats['assist']) / stats['death']
        # creep score
        stats['cs'] = stats['cs'] + match['stats']['minion_kill']
        stats['avg_cs'] = stats['cs'] / stats['games']
        # vision scores
        stats['wards_placed'] = stats['wards_placed'] + match['stats']['ward_place']
        stats['wards_placed'] = stats['wards_placed'] / stats['games']
        stats['wards_destroyed'] = stats['wards_destroyed'] + match['stats']['ward_kill']
        stats['wards_destroyed'] = stats['wards_destroyed'] / stats['games']
        stats['vision_score'] = stats['vision_score'] + match['stats']['vision_score']
        stats['vision_score'] = stats['vision_score'] / stats['games']
        stats['control_wards'] = stats['control_wards'] + match['stats']['vision_wards_bought_in_game']
        stats['control_wards'] = stats['control_wards'] / stats['games']
        # damage
        stats['damage_to_towers'] = stats['damage_to_towers'] + match['stats']['damage_dealt_to_turrets']
        stats['avg_damage_to_towers'] = stats['avg_damage_to_towers'] / stats['games']
        stats['damage_to_champions'] = stats['damage_to_champions'] + match['stats']['total_damage_dealt_to_champions']
        stats['avg_damage_to_champions'] = stats['avg_damage_to_champions'] / stats['games']
        # gold
        stats['gold'] = stats['gold'] + match['stats']['gold_earned']
        stats['gold'] = stats['gold'] / stats['games']
        # performance
        stats['total_game_rank'] = stats['total_game_rank'] + match['rank']
        stats['avg_game_rank'] = stats['total_game_rank'] / stats['games']
        if match['game_mvp'] == 'true':
            stats['mvp'] = stats['mvp'] + 1
        if match['team_mvp'] == 'true':
            stats['ace'] = stats['ace'] + 1
        # NOT COUNTED EVEN IN REMAKES!
    return stats

