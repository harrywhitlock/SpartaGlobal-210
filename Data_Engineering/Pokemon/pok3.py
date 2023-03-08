import requests
import random
import time

import pandas as pd
pokemon_endpoint = 'https://pokeapi.co/api/v2/pokemon/'

req = requests.get(pokemon_endpoint + 'pikachu')

data = req.json()

df = pd.read_csv('chart.csv')
df2 = df.reset_index(drop=True)
#df = df.drop(df.columns[0], axis=1)


print(df)
multiplier = df2.iloc[1, 1]
print(multiplier)

def get_pokemon_data(id):
    req = requests.get(pokemon_endpoint + str(id))
    data = req.json()
    #print(data)
    dict = {stat['stat']['name']: stat['base_stat'] for stat in data['stats']}
    type = data['types'][0]['type']['name']#['type']#['name']
    print(type)

    #dict['types'] = data['type']

    return dict



print(get_pokemon_data(1))
