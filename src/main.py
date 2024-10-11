from utils.convert_to import convert_to_csv

file = input('Enter the full name of the file (e.g. animals.txt):')
file_type = file.split('.')[1]

#sanitize data 

db_choice = input('What database would you like to import this data to? (rds = 1, dynamo = 2, neptune = 3, documentDB = 4): ')
table_name = input('Enter the name of the table you would like to import this data to: ')

if db_choice == '1':
    if file_type == 'txt':
        print('Converting data to csv...')
        convert_to_csv(file)
    print('Data has been converted to csv')
    print('Data has been imported to RDS')
elif db_choice == '2':
    print('Data has been imported to DynamoDB') 
elif db_choice == '3':
    print('Data has been imported to Neptune')
elif db_choice == '4':
    print('Data has been imported to DocumentDB')

    