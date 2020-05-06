# weather-scrape
An ETL Pipeline to query data from a Weather API and process.

## EC2 Setup.

Things that need to be present
- python3 : ```sudo yum install python3```
- pip : ```sudo easy_install pip```
- wheel : ```pip install wheel```
- aws-cli : ```pip3 install awscli --upgrade --user```

The command to run all these:
```pip install --upgrade --ignore-installed -r requirements.txt```
## Things to do

- Ensure python3 is being used. ```alias python=python3```
- Create an environment for everything to be present (docker?). 
- All of the packages installation should be in the docker config.
