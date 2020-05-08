import boto3
import configparser
import logging
from datetime import datetime
from botocore.exceptions import NoCredentialsError
import os
import sys
from pathlib import Path


sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.constants import FILE_NAME


"""
Setting up s3 destination structure.
"""
day = datetime.now()
S3_FILE_KEY = str(day.year) + '/' + str(day.month) + '/' + str(day.hour) + '.csv'

"""
Setting up logging.
"""
sc_log = logging.getLogger(__name__)
sc_log.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

DIRECTORY = 'logs/transfer/' + str(day.year) + '/' + str(day.month) + '/'
Path(DIRECTORY).mkdir(parents=True, exist_ok=True)

handler = logging.FileHandler(DIRECTORY + str(day.hour) + '.log')
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
s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

try:
    s3.upload_file(FILE_NAME, 'weather-scrape-bucket', S3_FILE_KEY)
    sc_log.log(logging.DEBUG, "Completed S3 upload.")
except FileNotFoundError:
    sc_log.exception("The file was not found.")
except NoCredentialsError:
    sc_log.exception("There is an issue with the credentials.")








