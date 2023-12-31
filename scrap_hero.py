import requests
import json
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent

# ua = UserAgent()
# headers = {'User-Agent': ua.chrome}
hero_list_json_file = "hero_list.json"
image_base_url = "https://cdn.cloudflare.steamstatic.com/apps/dota2/images/dota_react/heroes/"

def addingImageUrl(hero_list):
    for hero in hero_list:
        hero_name = hero['name'][len("npc_dota_hero_"):]
        hero['image_url'] = image_base_url + hero_name + ".png"

def fetch_hero_list():
    hero_list_url = "https://www.dota2.com/datafeed/herolist?language=english"
    hero_list_response = requests.get(hero_list_url).json()
    hero_list = hero_list_response['result']['data']['heroes']
    addingImageUrl(hero_list)
    with open(hero_list_json_file, 'w') as f:
        json.dump(hero_list, f)


def fetch_hero(id):
    # if (id > 3):
        # return
    hero_url = "https://www.dota2.com/datafeed/herodata?language=english&hero_id=" + str(id)
    print("fetching hero " + str(id) + " from " + hero_url)
    hero_response = requests.get(hero_url).json()
    hero_data = hero_response['result']['data']['heroes'][0]
    with open('heroes/hero_' + str(id) + '.json', 'w') as f:
        json.dump(hero_data, f)


def fetch_heroes():
    with open(hero_list_json_file, 'r') as f:
        hero_list = json.load(f)
    for hero in hero_list:
        fetch_hero(hero['id'])

fetch_hero_list()
fetch_heroes()


# def test_fetching(id):
#     hero_url = "https://www.dota2.com/datafeed/herodata?language=english&hero_id=" + str(id)
#     print("fetching hero " + str(id) + " from " + hero_url)
#     hero_response = requests.get(hero_url).json()
#     hero_data = hero_response['result']['data']['heroes'][0]
#     print(hero_data)

# test_fetching(80)

