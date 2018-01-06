import pymongo
import requests


def requestDataFromURL(configData):
    # get it from a config file
    # Try catch Condition
    data = requests.get(configData["API-URL"]+configData["API-KEY"]+'&limit='+str(configData["Datalimit"])).json()['records']
    return data


def cleanData(data):
    # Google key to be added in config file
    cleanedData=[]
    for hosp in data:
        hosp["ID"] = 'ID_'+ '%04d'%data.index(hosp)

        for col in ['services_','specializations']:
            hosp[col]=[val.strip() for val in hosp[col].split(',')]


        hospName = hosp['hospital_private']
        print(hosp['ID'],hospName)
        address = hosp['contact_details'].split(',')
        address=[val.strip() for val in address ]
        if(hosp['city'] in address):
            contactDetails = address[address.index(hosp['city']) - 1]
            address = hospName + ' ' + contactDetails
            hosploc = requests.get(
            'https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=AIzaSyAUcvVet8YpEOZhlLmDzYBXPM2LD6jXRFU' % address).json()[
            "results"]
            if len(hosploc)>0:
                hosp["location"] =  hosploc[0]['geometry']['location']
        cleanedData.append(hosp)
    return cleanedData
def insertData(data,db,collection):
    for info in data:
        db[collection].update({"_id": info["ID"]}, {'$set': info}, upsert=True)

def importData():
    import json

    # Read the configfile
    #Try catch for a file
    try:
        with open('../config.json') as f:
            configData = json.load(f)

    except IOError:
        print("Could not read configuration file:", 'config.json')
        exit()



    # Connect to the db
    try:
        conn = pymongo.MongoClient()
        print("Connected successfully!!!")
    except pymongo.errors.ConnectionFailure as e:
            print("Could not connect to MongoDB: %s" % e)

    db = conn[configData['MONGO_DBNAME']]
    collection = configData['MONGO_COLNAME']


    # Get the url for the site to pick the gov data along with the access token
    data=requestDataFromURL(configData)

    #Get the data and do some cleaning of the data
    data= cleanData(data)

    #push into database
    insertData(data,db,collection)

    print(" Successfully inserted Data")
if __name__=='__main__':
    importData()