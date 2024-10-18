import pymongo as pym
import json

altina = '/home/ec2-user/aws-databridge/global-bundle.pem'


def import_to_documentdb(file):
    try:
        client = pym.MongoClient(f'mongodb://marduk111:mirabel3@docdb-2024-10-18-14-40-50.cluster-cfsssmgsia9l.us-east-1.docdb.amazonaws.com:27017/?tls=true&tlsCAFile={altina}&retryWrites=false&directConnection=true') 

        db = client['database']
        collection = db['collection']
    except Exception as err:
        print(f'Unable to connect to MongoDB: {err}')
        return None

    with open(file, 'r') as data:
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

    print('Data has been imported to DocumentDB.')
    client.close()