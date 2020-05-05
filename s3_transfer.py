import boto3
import configparser
import logging

from datetime import date
from botocore.exceptions import NoCredentialsError
from constants import FILE_NAME


"""
Setting up logging.
"""
sc_log = logging.getLogger(__name__)
sc_log.setLevel(logging.DEBUG)

day = date.today()
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

s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

try:
    s3.upload_file(FILE_NAME, 'weather-scrape-bucket', FILE_NAME)
    sc_log.log(logging.DEBUG, "Completed S3 upload.")
except FileNotFoundError:
    sc_log.exception("The file was not found.")
except NoCredentialsError:
    sc_log.exception("There is an issue with the credentials.")








