from aws_databridge.utils.convert_to import text_to_csv, json_to_csv, xml_to_csv
from aws_databridge.db_import.rds import import_to_rds
from aws_databridge.db_import.dynamodb import import_to_dynamodb
import os

def main():
    file = input('Enter the full name of the file (e.g. animals.txt , include folder path if applicable-> folder/animals.txt):')
    file = os.path.join('/home/ec2-user/', file)
    file_type = file.split('.')[1]

    db_choice = input('What database would you like to import this data to? (rds = 1, dynamo = 2, neptune = 3, documentDB = 4): ')
    table_name = input('Enter the name of the table you would like to import this data to: ')

    #convert supported non csv types to csv
    if file_type == 'txt':
        print('Converting data to csv...')
        text_to_csv(file)
        print('Data has been converted to csv')
    elif file_type == 'json':
            print('Converting data to csv...')
            json_to_csv(file)
            print('Data has been converted to csv')
    elif file_type == 'xml':
            print('Converting data to csv...')
            xml_to_csv(file)
            print('Data has been converted to csv')

    # import data to the selected database, allowing for multiple imports if neccessary 
    stop = 0;
    while stop == 0:
        if db_choice == '1':
            import_to_rds(file, table_name)
        elif db_choice == '2':
            primary_key = input('Enter the primary key for the table: ')
            import_to_dynamodb(file, table_name, primary_key)
        elif db_choice == '3':
            print('Data has been imported to Neptune')
        elif db_choice == '4':
            print('Data has been imported to DocumentDB')
        stop = int(input('Would you like to import this file to another database? (yes = 0, no = 1): '))
        if stop == 0:
            db_choice = input('What database would you like to import this data to? (rds = 1, dynamo = 2, neptune = 3, documentDB = 4): ')
            table_name = input('Enter the name of the table you would like to import this data to: ')


if __name__ == '__main__':
    main()