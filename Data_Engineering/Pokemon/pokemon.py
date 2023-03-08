import requests
import random
import time
import pandas as pd

df = pd.read_csv('chart.csv')

pokemon_endpoint = 'https://pokeapi.co/api/v2/pokemon/'

req = requests.get(pokemon_endpoint + 'pikachu')

data = req.json()



def get_pokemon_data(id):
    req = requests.get(pokemon_endpoint + str(id))
    data = req.json()
    dict = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    dict['name'] = data['name']
    type = data['types'][0]['type']['name']
    return dict

def get_pokemon_type(id):
    req = requests.get(pokemon_endpoint + str(id))
    data = req.json()
   # dict = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
   # dict['name'] = data['name']
    type = data['types'][0]['type']['name']
    return type


def do_battle(id1,id2):
    pokemon1 = get_pokemon_data(id1)
    pokemon2 = get_pokemon_data(id2)
    print('Your {} is fighting a {}'.format(pokemon1['name'],pokemon2['name']))
    if(pokemon1['attack'] > pokemon2['attack']):
        print('{} wins'.format(pokemon1['name']))
    elif (pokemon1['attack'] < pokemon2['attack']):
        print('{} wins'.format(pokemon2['name']))
    else:
        print('It was a tie!')


def do_battle2(id1, id2):

    pokemon1 = get_pokemon_data(id1)
    pokemon2 = get_pokemon_data(id2)

    pokemon1_type = get_pokemon_type(id1)
    pokemon2_type = get_pokemon_type(id2)

    print(pokemon1_type.capitalize())
    print(pokemon2_type.capitalize())

    multiplier1 = df.loc[pokemon1_type.capitalize(), pokemon2_type.capitalize()]
    print(multiplier1)

    print('Your {} is fighting a {}'.format(pokemon1['name'], pokemon2['name']))

    pok1_hp_counter = pokemon1['hp']
    pok2_hp_counter = pokemon2['hp']

    while pok2_hp_counter > 0 and pok1_hp_counter > 0:

        pok1_hp_counter = pok1_hp_counter - (pokemon2['attack'] * 0.1)
        print(pokemon1['name'] + ' hp is:' + str(pok1_hp_counter))
        time.sleep(0.5)
        pok2_hp_counter = pok2_hp_counter - (pokemon1['attack'] * 0.1)
        print(pokemon1['name'] + ' hp is:' + str(pok2_hp_counter))
        time.sleep(0.5)

        if pok1_hp_counter <= 0:
            print('{} wins'.format(pokemon1['name']))

        elif pok2_hp_counter <= 0:
            print('{} wins'.format(pokemon2['name']))




def main():

    mode = input('One Player or two?: ')

    if int(mode) == 1:
        opponent = random.randint(1, 1118)
        pokemon1_name = input('Enter Pokemon 1')
        do_battle2(pokemon1_name, opponent)

    if int(mode) == 2:
        pokemon1_name = input('Enter Pokemon 1')
        pokemon2_name = input('Enter Pokemon 2')
        do_battle2(pokemon1_name, pokemon2_name)


if __name__ == '__main__':
    main()

