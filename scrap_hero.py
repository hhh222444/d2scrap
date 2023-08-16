import requests
import json
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

# ua = UserAgent()
# headers = {'User-Agent': ua.chrome}
hero_list_json_file = "hero_list.json"

def fetch_hero_list():
    hero_list_url = "https://www.dota2.com/datafeed/herolist?language=english"
    hero_list_response = requests.get(hero_list_url).json()
    hero_list = hero_list_response['result']['data']['heroes']
    with open(hero_list_json_file, 'w') as f:
        json.dump(hero_list, f)


def fetch_hero(id):
    hero_url = "https://www.dota2.com/datafeed/herodata?language=english&hero_id=" + str(id)
    print("fetching hero " + str(id) + " from " + hero_url)
    hero_response = requests.get(hero_url).json()
    hero_list = hero_response['result']['data']['heroes'][0]
    with open('heroes\hero_' + str(id) + '.json', 'w') as f:
        json.dump(hero_list, f)


def fetch_heroes():
    with open(hero_list_json_file, 'r') as f:
        hero_list = json.load(f)
    for hero in hero_list:
        fetch_hero(hero['id'])

fetch_hero_list()
fetch_heroes()

