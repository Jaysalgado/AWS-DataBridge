# noSQL DB
# compatible with mongoDB
# stores data in JSON'ss
# store information without pre-defined schema's

import pymongo as pym
import json

try:
    client = pym.MongoClient('mongodb://<sample-user>:<password>@sample-cluster.node.us-east-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false') 

    db = client['database']
    collection = db['collection']
except pym.errors.ConnectionError as err:
    print('Unable to connect to MongoDB: {err}')
    exit(1)

with open('data.json', 'r') as data:
    imported_data = json.load(data)

if isinstance(data, list):
    try:
        collection.insert_many(imported_data)
        print('Successfully inserted multiple collections.')
    except Exception as ex:
        print(f'Unable to insert documents: {ex}')
else:
    try:
        collection.insert_one(imported_data)
        print('Successfully inserted singular collection.')
    except Exception as ex:
        print(f'Unable to insert document: {ex}')

client.close()