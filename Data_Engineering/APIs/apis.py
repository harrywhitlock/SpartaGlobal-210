import requests
import json
import random
post_codes_req = requests.get('https://api.postcodes.io/postcodes/cf54ry')

print(post_codes_req)

#print(post_codes_req.content)

print(type(post_codes_req.json()))

json_body = json.dumps({'postcodes': ['PR3 0SG', 'M45 6GN', 'EX165BL']})
headers ={'Content-Type':'application/json'}

post_multi_req = requests.post("https://api.postcodes.io/postcodes", headers=headers, data=json_body)

print(post_multi_req.json())


pokemon_req = requests.get('https://pokeapi.co/api/vs/pokemon/pikachu')

print(pokemon_req.status_code)

response = requests.get('https://pokeapi.co/api/v2/pokemon?limit=1118')
data = response.json()
print(data)

random_pokemon = random.choice(data['results'])

print(random_pokemon)

response = requests.get('https://pokeapi.co/api/v2/pokemon/33/')

#response = requests.get(random_pokemon['url'])
data = response.json()
name = data['name']

print(name)

pokemon_endpoint = 'https://pokeapi.co/api/v2/'

req = requests.get(pokemon_endpoint + '1')

data = req.json()
print(data)