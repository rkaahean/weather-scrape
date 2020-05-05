import requests
from datetime import date
import logging
import configparser
import pandas as pd
import json

from constants import API_CITY_FORECAST, CITY_LIST
from utils import format_url

"""
Setting up logging.
"""
sc_log = logging.getLogger(__name__)
sc_log.setLevel(logging.DEBUG)

day = date.today()
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

handler = logging.FileHandler('logs/' + str(day) + '.log')
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

for city in CITY_LIST:
    url = format_url(API_CITY_FORECAST, city, API_KEY)
    response = requests.get(url)
    json_data = json.loads(response.content)
    data_point = json_data['list']

    for item in data_point:
        item_data_dict = {
            'time': None,
            'city': city,
            'temp': None,
            'pressure': None,
        }
        main_item = item['main']

        item_data_dict['time'] = item['dt']
        item_data_dict['temp'] = main_item['temp']
        item_data_dict['pressure'] = main_item['pressure']
        print(item_data_dict)

print(format_url(API_CITY_FORECAST, city, API_KEY))
