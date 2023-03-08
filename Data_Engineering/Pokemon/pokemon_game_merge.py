import time
import requests
import json
import random
import math

pokemon_endpoint = 'https://pokeapi.co/api/v2/pokemon/'

req = requests.get(pokemon_endpoint + '1')

def title_case(s):
    return s[0].upper() + s[1:]


def get_pokemon_data(id):
    req = requests.get(pokemon_endpoint + str(id))
    data = req.json()
    dict = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    dict['name'] = title_case(data['name'])
    return dict

def get_hp_ticks(current,max):
    return int(20*(round(current/max,2)))

def do_battle(pokemon1,pokemon2):
    print('Your {} is fighting a {}'.format(pokemon1['name'],pokemon2['name']))
    print('-' * 42)
    print('{:20s}vs{:>20s}'.format(pokemon1['name'], pokemon2['name']))

    hp_counter_1 = pokemon1['hp']
    hp_counter_2 = pokemon2['hp']

    while hp_counter_2 > 0 and hp_counter_1 > 0:

        hp_counter_1 = hp_counter_1 - (pokemon2['attack'] * 0.1)
        hp_counter_2 = hp_counter_2 - (pokemon1['attack'] * 0.1)
        print('\r{:20s}<>{:>20s}'.format('|' * get_hp_ticks(hp_counter_1,pokemon1['hp']),
                                         '|' * get_hp_ticks(hp_counter_2,pokemon2['hp']), )
                                         , end='', flush=True)
        time.sleep(0.3)
        if hp_counter_1 <= 0:
            print('{:^42s}'.format('{} wins'.format(pokemon1['name'])))
        elif hp_counter_2 <= 0:
            print('{:^42s}'.format('{} wins'.format(pokemon2['name'])))

    # if(pokemon1['attack'] > pokemon2['attack']):
    #     # print('{} wins'.format(pokemon1['name']))
    #     print('\r{:^42s}'.format('{} wins'.format(pokemon1['name'])))
    # elif (pokemon1['attack'] < pokemon2['attack']):
    #     # print('{} wins'.format(pokemon2['name']))
    #     print('\r{:^42s}'.format('{} wins'.format(pokemon2['name'])))
    # else:
    #     print('It was a tie!')
    print('-' * 42)
def main():
    run = True;
    while run:
        player_pokemon = input('Pick your pokemon. You can use its name or number!')
        pokemon1 = get_pokemon_data(player_pokemon)
        time.sleep(0.5)
        print('You picked {}'.format(title_case(pokemon1['name'])))
        for i in range(1,6):
            time.sleep(0.3)
            print('\rYour opponent is picking'+'.'*i,end='')
        pokemon2 = get_pokemon_data(random.randint(1,1000))
        time.sleep(0.5)
        print('He picked {}'.format(title_case(pokemon2['name'])))
        time.sleep(1)
        do_battle(pokemon1,pokemon2)


if __name__ == "__main__":
    main()
