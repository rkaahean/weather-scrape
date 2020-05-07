# weather-scrape
An ETL Pipeline to query data from a Weather API and process.

## EC2 Setup.

No setup required, docker takes care of everything.
Built on ubuntu 18.04 image. Python 3.6.

## Things to do

- Ensure python3 is being used. ```alias python=python3```
- Create an environment for everything to be present (docker?). 
- All of the packages installation should be in the docker config.
- Build on a Spark Framework.
- Deploy on ECS
- Connect to a some sort of Load Balancer.
- Try Apache Kafka.
- Built a front end with Flask.

## Running the python files.

- ```python src\scrape.py```

## Issues

- Need to fix import structure. ```scrape.py``` does not run from the folder.
- Need to create a logging structure in the setup. For now, committing the log folders.
- Need to automatically create a config.ini file. :