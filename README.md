# weather-scrape
An ETL Pipeline to query data from a Weather API and process.

## EC2 Setup.

No setup required, docker takes care of everything.
Built on ubuntu 18.04 image. Python 3.6.

## Setup & configuration

1. Clone repository.
2. Placed config.ini file in the top level directory.
3. Copy the Openweather API KEY.
4. Copy the AWS Access Key and Secret Access Key.
5. ```docker-compose up.```

## Things to do

- Ensure python3 is being used. ```alias python=python3```
- Create an environment for everything to be present (docker?). 
- All of the packages installation should be in the docker config.
- Build on a Spark Framework.
- Deploy on ECS
- Connect to a some sort of Load Balancer.
- Try Apache Kafka / Airflow.
- Built a front end with Flask.
- Amazon ECS.

## Running the python files.

- ```python src\scrape.py```
