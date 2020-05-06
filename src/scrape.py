import configparser
import json
import logging
import os
import sys
from datetime import date
import pandas as pd
import requests

from src.constants import API_CITY_FORECAST, CITY_LIST, FILE_NAME
from src.utils import format_url

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

"""
Setting up logging.
"""
sc_log = logging.getLogger(__name__)
sc_log.setLevel(logging.DEBUG)

day = date.today()
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

handler = logging.FileHandler('logs/scrape/' + str(day) + '.log')
sc_log.addHandler(handler)

"""
Loading in the Key.
"""
sc_log.log(logging.DEBUG, "Getting API-KEY")
config = configparser.ConfigParser()
config.read('config.ini')

try:
    API_KEY = config['KEY']['API-KEY']
except KeyError:
    sc_log.exception("Please define the key in the 'KEY' section, with 'API-KEY' key.")

"""
Hitting the api.
"""

weather_data = []
for city in CITY_LIST:
    url = format_url(API_CITY_FORECAST, city, API_KEY)
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException:
        sc_log.exception("Something went wrong in querying the API.")

    json_data = json.loads(response.content)
    data_point = json_data['list']

    for item in data_point:
        item_data_dict = {
            'time': None,
            'city': city,
            'temp': None,
            'pressure': None,
            'humidity': None,
            'desc': None,
        }
        main_item = item['main']
        weather_item = item['weather'][0]

        item_data_dict['time'] = item['dt']
        item_data_dict['temp'] = main_item['temp']
        item_data_dict['pressure'] = main_item['pressure']
        item_data_dict['humidity'] = main_item['humidity']
        item_data_dict['desc'] = weather_item['description']

        weather_data.append(item_data_dict)

weather_data = pd.DataFrame(weather_data)
weather_data.to_csv(FILE_NAME)
