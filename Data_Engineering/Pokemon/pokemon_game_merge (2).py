import time
import requests
import os
import json
import random
import math
import pandas as pd

pokemon_endpoint = 'https://pokeapi.co/api/v2/pokemon/'
type_relations = pd.read_csv('chart.csv')
type_relations.set_index('Attacking', inplace=True)
type_relations.columns = type_relations.columns.str.lower()
type_relations.index = type_relations.index.str.lower()
req = requests.get(pokemon_endpoint + '1')


def get_multiplier(attacking_types, defending_types):
    base = 1
    for t1 in attacking_types:
        for t2 in defending_types:
            base *= get_type_multiplier(t1, t2)

    return base


def get_type_multiplier(attacking, defending):
    return type_relations.loc[attacking, defending]


def get_hp_color_code(pct):
    digit = 1
    if (pct >= 0.66):
        digit = 2
    elif (pct >= 0.33):
        digit = 3

    return '\033[1;3' + str(digit) + 'm'


def title_case(s):
    return s[0].upper() + s[1:]


def get_pokemon_data(id):
    req = requests.get(pokemon_endpoint + str(id))
    data = req.json()
    dict = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    dict['name'] = title_case(data['name'])
    dict['types'] = [type['type']['name'] for type in data['types']]
    return dict


def get_hp_ticks(current, max):
    return int(20 * (round(current / max, 2)) + 0.9)


def do_battle(pokemon1, pokemon2):
    print('Your {} is fighting a {}'.format(pokemon1['name'], pokemon2['name']))
    print('-' * 42)
    print('{:20s}vs{:>20s}'.format(pokemon1['name'], pokemon2['name']))

    hp_counter_1 = pokemon1['hp']
    hp_counter_2 = pokemon2['hp']

    mult_1 = get_multiplier(pokemon1['types'], pokemon2['types'])
    mult_2 = get_multiplier(pokemon2['types'], pokemon1['types'])

    while hp_counter_2 > 0 and hp_counter_1 > 0:

        hp_color_1 = get_hp_color_code(hp_counter_1 / pokemon1['hp'])
        hp_color_2 = get_hp_color_code(hp_counter_2 / pokemon2['hp'])

        hp_counter_1 = hp_counter_1 - (5 * pokemon2['attack'] / pokemon1['defense']) * mult_1
        hp_counter_2 = hp_counter_2 - (5 * pokemon1['attack'] / pokemon2['defense']) * mult_2
        print('\r{:<31s}<>{:>31s}'.format(hp_color_1 + '|' * get_hp_ticks(hp_counter_1, pokemon1['hp']) + '\033[0m',
                                          hp_color_2 + '|' * get_hp_ticks(hp_counter_2, pokemon2['hp']) + '\033[0m')
              , end='', flush=True)
        time.sleep(1)
        if hp_counter_1 <= 0 and hp_counter_2 <= 0:
            print('\n{:^42s}'.format('It\'s a draw!'))
        elif hp_counter_1 <= 0:
            print('\n{:^42s}'.format('{} wins'.format('          \033[1;17m' + pokemon2['name'] + '\033[0m')))
        elif hp_counter_2 <= 0:
            print('\n{:^42s}'.format('{} wins'.format('          \033[1;17m' + pokemon1['name'] + '\033[0m')))

    print('-' * 42)


def main():
    f = open('title.txt', 'r')
    file_contents = f.read()
    print(file_contents)
    mode = input('1 or 2-player ?').lower()
    while (mode not in ['1', 'one', '2', 'two']):
        mode = input('Please enter a valid mode: 1 or 2-player ?').lower()

    run = True;
    while run:
        while True:
            try:
                player_pokemon = input('Trainer! Pick your pokemon. You can use its name or number!')
                pokemon1 = get_pokemon_data(player_pokemon)
                break
            except:
                print('\rThat\'s not a valid pokemon! Try again', end='\r')
                time.sleep(1)
                pass
        time.sleep(0.5)
        print('You picked {}'.format(title_case(pokemon1['name'])))
        pokemon2 = {}
        if (mode in ['1', 'one']):
            for i in range(1, 6):
                time.sleep(0.3)
                print('\rYour opponent is picking' + '.' * i, end='')
            pokemon2 = get_pokemon_data(random.randint(1, 1008))
        else:
            while True:
                try:
                    player2_pokemon = input('Trainer 2! Pick your pokemon. You can use its name or number!')
                    pokemon2 = get_pokemon_data(player2_pokemon)
                    break
                except:
                    print('\rThat\'s not a valid pokemon! Try again', end='\r')
                    time.sleep(1)
                    pass
        time.sleep(0.5)
        print('\nHe picked {}'.format(title_case(pokemon2['name'])))
        time.sleep(1)
        do_battle(pokemon1, pokemon2)
        run = (input("Do you want to play again? (Y/N)").lower() in ['y', ''])
        #os.system('cls')


if __name__ == "__main__":
    main()
