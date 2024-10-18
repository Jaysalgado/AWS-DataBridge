import csv
import pandas as pd
import json

def text_to_csv(filepath):
    
    #test
    # test_text = """name age city
    # Jay 25 New_York
    # Abahn 30 Vegas
    # Matt 22 connecticut
    # name 28 Houston
    # """
    # with open("test_data.txt", "w") as file:
    #     file.write(test_text)
    #     filepath = "test_data.txt"

    with open(filepath, 'r') as file:
        lines = file.readlines()

    a_names = lines[0].split() #attribute names
    rows = [line.split() for line in lines[1:]] #tuple values

    with open(filepath.replace('txt', 'csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(a_names)
        writer.writerows(rows)

def json_to_csv(filepath):
    #test
    # test_json = [
    #     {"name": "Jay", "age": 25, "city": "New York"},
    #     {"name": "Abahn", "age": 30, "city": "Vegas"},
    #     {"name": "Matt", "age": 22, "city": "connecticut"},
    #     {"name": "name", "age": 28, "city": "Houston"}
    # ]
    # with open("test_data.json", "w") as file:
    #     json.dump(test_json, file, indent=4)
    #     filepath = "test_data.json"

    data = pd.read_json(filepath)
    data.to_csv(filepath.replace('json', 'csv'), index=False)

def xml_to_csv(filepath):

    # test 
    # test_xml = """<?xml version="1.0"?>
    # <data>
    #     <person>
    #         <name>Jay</name>
    #         <age>25</age>
    #         <city>New York</city>
    #     </person>
    #     <person>
    #         <name>Abahn</name>
    #         <age>30</age>
    #         <city>Vegas</city>
    #     </person>
    #     <person>
    #         <name>Matt</name>
    #         <age>22</age>
    #         <city>connecticut</city>
    #     </person>
    #     <person>
    #         <name>name</name>
    #         <age>28</age>
    #         <city>Houston</city>
    #     </person>
    # </data>"""

    # # Write the XML to a file
    # with open("test_data.xml", "w") as file:
    #     file.write(test_xml)
    #     filepath = "test_data.xml"

    data = pd.read_xml(filepath)
    data.to_csv(filepath.replace('xml', 'csv'), index=False)




