import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'd588e7f6366814e6d0f97ac2817fc952'
HEADER = {'Content-Type' : 'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 4289

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

    #def test_part_of_responce():
        #responce_get = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
        #assert responce_get.json()['name'] == 'пикачу'

##def test_parametrize(key, value):
   # responce_parametrize = requests.get(url = f'{URL}/pokemons', params = {'trainer_id' : TRAINER_ID})
    #assert responce_parametrize.json()['data'][0][key] == value

def test_name_trainer():
    responce_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert responce_get.json()['data'][0]['trainer_name'] == 'Kirito'
 