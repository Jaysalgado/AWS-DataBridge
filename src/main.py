from utils.convert_to import convert_to_csv
from db_import.rds import import_to_rds
from db_import.dynamodb import import_to_dynamodb
import os

file = input('Enter the full name of the file (e.g. animals.txt):')
file = os.path.join('/home/ec2-user/', file)
file_type = file.split('.')[1]

#sanitize data 

db_choice = input('What database would you like to import this data to? (rds = 1, dynamo = 2, neptune = 3, documentDB = 4): ')
table_name = input('Enter the name of the table you would like to import this data to: ')

if file_type == 'txt':
     print('Converting data to csv...')
     convert_to_csv(file)
     print('Data has been converted to csv')

if db_choice == '1':
     import_to_rds(file, table_name)
elif db_choice == '2':
    primary_key = input('Enter the primary key for the table: ')
    import_to_dynamodb(file, table_name, primary_key)
elif db_choice == '3':
    print('Data has been imported to Neptune')
elif db_choice == '4':
    print('Data has been imported to DocumentDB')

    