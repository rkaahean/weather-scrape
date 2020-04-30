import requests
from datetime import date
import logging
import configparser
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



