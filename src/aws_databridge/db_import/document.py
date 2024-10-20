import pymongo as pym
import json

#add a possible check for dictionaries

def import_to_documentdb(file):
    try:
        client = pym.MongoClient('mongodb://marduk111:mirabel3@docdb-2024-10-18-14-40-50.cfsssmgsia9l.us-east-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile=global-bundle.pem&retryWrites=false') 

        db = client['database']
        collection = db['collection']
    except pym.errors.ConnectionFailure as err:
        print(f'Unable to connect to MongoDB: {err}')
        return None

    with open(file, 'r') as data:
        imported_data = json.load(data)

    if isinstance(imported_data, list):
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

    print('Now printing document to the terminal.')

    try:
        doc_doc = collection.find()
        for doc in doc_doc:
            print(doc)
    except Exception as err:
        print(f'Cannot fetch documents: {err}')

    print('Data has been imported to DocumentDB.')
    client.close()