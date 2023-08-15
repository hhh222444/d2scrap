import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
headers = {'User-Agent': ua.chrome}

hero_url = "https://www.dota2.com/datafeed/herolist?language=english"
hero_response = requests.get(hero_url, headers=headers)

