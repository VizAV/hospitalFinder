# Hospital Finder
This is a fun project which aims at getting a list of hospitals which satisfy a set of filters. 
The source of the data is from [here](https://data.gov.in/catalog/hospital-directory-national-health-portal).
Currently there is not front end design available for this project and the usage should be done through HTTP clients like ['Postman'](https://www.getpostman.com/).
## How to run
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

There are two modes of working on this:

**Method 1: Importing the data from the URL manually**
1. From the main folder location run:

***
`python ../database/__init__.py`
***
Use the config.json file to give the database values accordingly
2. Edit the config.py file for all the filters and run:


***
`python run.py`
***
3. Open postman and type the following details
  * Address as _localhost:8080/filterData_
  * In body type the filters given in config.py file

click  **Send**  to get a response json having a list of all the filtered Hospitals
 
**Method 2: Downloading the database directly**
1. Download the [database files](https://github.com/VizAV/hospitalFinder/tree/master/database/hospitalDB) in the BSON format and import to your local machine using
***

`mongorestore -d db_name -c collection_name path/file.bson`

***
2. Follow from step 3 in ..Method 1..
## Prerequisite 
1. Database: [mongodb](https://www.mongodb.com/)
2. Micro-Framework: [python-flask](http://flask.pocoo.org/)
3. [API-Key](https://data.gov.in/resources/hospital-directory-july-2015/api) from data.gov.in (optional)
4. Google API key for getting the latitude  and longitude

## Future Plan
This project is maintained in trello. 
Please watch the **hospitalFinder** list in  [this](https://trello.com/b/aoHBdMcM) board for the future work planned 

## License
This project is licensed under the MIT License - see the LICENSE.md file for details

