import requests
import logging

def get_pokemon_attack_multiplier(attack_type, pokemon_types):
    response = requests.get(f'https://pokeapi.co/api/v2/type/{attack_type}', verify=False)
    if response.status_code != 200:
        logging.error(f'Failed to retrieve data from api, status code: {response.status_code}.')
        return False

    damage_relations = response.json()['damage_relations']
    try:
        if any(x['name'] in pokemon_types for x in damage_relations['no_damage_to']):
            return '0x'

        result = 1

        for x in damage_relations['double_damage_to']:
            if x['name'] in pokemon_types:
                result = result * 2
        for x in damage_relations['half_damage_to']:
            if x['name'] in pokemon_types:
                result = result * 0.5

    except Exception as e:
        logging.error(f'Incorrect data: {e}')
        return False

    if result - int(result) == 0:
        result = int(result)
        
    result = str(result) + 'x'
    return result