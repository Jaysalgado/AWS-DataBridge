import csv

def convert_to_csv(filepath):
    
    #test
    # sample_text = """name age city
    # Alice 25 New_York
    # Bob 30 Los_Angeles
    # Charlie 22 Chicago
    # Diana 28 Houston
    # """
    # with open("sample_data.txt", "w") as file:
    #     file.write(sample_text)
    #     filepath = "sample_data.txt"

    with open(filepath, 'r') as file:
        lines = file.readlines()

    a_names = lines[0].split() #attribute names
    rows = [line.split() for line in lines[1:]] #tuple values

    with open(filepath.replace('txt', 'csv'), 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(a_names)
        writer.writerows(rows)


