import requests
from datetime import date
import logging
import configparser

from constants import API_CITY_FORECAST

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
request_url = "http://" + API_CITY_FORECAST.format("Mumbai", API_KEY)
response = requests.get(request_url)
print(response)

