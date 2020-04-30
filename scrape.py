import requests
from datetime import date
import logging
from constants import API_KEY

sc_log = logging.getLogger(__name__)
sc_log.setLevel(logging.DEBUG)

day = date.today()
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

handler = logging.FileHandler('logs/' + str(day))

print(requests.__version__)
