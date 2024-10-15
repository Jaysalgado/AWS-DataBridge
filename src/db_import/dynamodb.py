import boto3
import pandas as pd

dynamodb = boto3.resource('dynamodb') #authenticates with iam role

def import_to_dynamodb(file, table_name, primary_key):
    #create table
    try: 
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': primary_key,
                    'KeyType': 'HASH'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': primary_key,
                    'AttributeType': 'S'
                }
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 1,
                'WriteCapacityUnits': 1
            }
        )
        table.wait_until_exists()
        print(f"Table {table_name} created successfully")
    except Exception as e:
        print(f"Error creating table: {e}")
        return None
    
    #import rows into table 
    data = pd.read_csv(file)
    for _, row in data.iterrows():
        try:
            table.put_item(Item=row.to_dict())
        except Exception as e:
            print(f"Error importing data: {e}")
            return None
        
    print('Data has been imported to DynamoDB')



