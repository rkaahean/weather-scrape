# weather-scrape
An ETL Pipeline to query data from a Weather API and process.

## EC2 Setup.

These are commands that are being run on a Ubuntu 20.04 LTS.
Things that need to be present: 

Upgrading everything first:
```sudo apt-get update && sudo apt-get upgrade```

- git: ```sudo apt-get install git```
- python3 : ```sudo apt install python3```
- pip : ```sudo apt install python3-pip```

Use python3 and pip3 always by default.
```
alias pip=pip3
alias python=python3
```

- wheel : ```pip install wheel```
- aws-cli : ```pip install awscli --upgrade --user```

The command to run all these:
```pip install --upgrade --ignore-installed -r requirements.txt```

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