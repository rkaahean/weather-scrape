import boto3
import configparser
import logging
from datetime import datetime
from botocore.exceptions import NoCredentialsError
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.constants import FILE_NAME

"""
Setting up logging.
"""
sc_log = logging.getLogger(__name__)
sc_log.setLevel(logging.DEBUG)

day = datetime.now()
formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

handler = logging.FileHandler('logs/transfer/' + str(day) + '.log')
sc_log.addHandler(handler)

"""
Loading in the KEYS
"""
config = configparser.ConfigParser()
config.read('config.ini')

ACCESS_KEY = config['AWS']['ACCESS_KEY']
SECRET_KEY = config['AWS']['SECRET_KEY']

"""
File related constants
"""
current_year = day.year
current_month = day.month
current_hour = day.hour

S3_FILE_KEY = str(day.year) + '/' + str(day.month) + '/' + str(day.hour)

s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

try:
    s3.upload_file(FILE_NAME, 'weather-scrape-bucket', S3_FILE_KEY)
    sc_log.log(logging.DEBUG, "Completed S3 upload.")
except FileNotFoundError:
    sc_log.exception("The file was not found.")
except NoCredentialsError:
    sc_log.exception("There is an issue with the credentials.")








