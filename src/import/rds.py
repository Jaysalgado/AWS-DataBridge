import csv 
import os 
import pymysql

#rds credentials stored in ec2
RDS_HOST = os.getenv("RDS_HOST")
RDS_USER = os.getenv("RDS_USER")
RDS_PASSWORD = os.getenv("RDS_PASSWORD")
RDS_DB = os.getenv("RDS_DB")
RDS_PORT = int(os.getenv("RDS_PORT", 3306))

def import_to_rds(filepath, table_name):
    #connect to rds 
    try:
        conn = pymysql.connect(
            host=RDS_HOST,
            user=RDS_USER,
            password=RDS_PASSWORD,
            db=RDS_DB,
            port=RDS_PORT
        )
    except pymysql.MySQLError as e:
        print(f"Error connecting to RDS: {e}")
        return None 
    
    #read data from file
    with open(filepath, 'r') as file:
        csv = csv.DictReader(file)
        a_names = csv.fieldnames
        rows = [list(row.values()) for row in csv]


    #database object (cursor) to interact with the database
    with conn.cursor() as cur:
        cur.execute(f"CREATE TABLE {table_name} ({a_names[0]} VARCHAR(255), {a_names[1]} INT, {a_names[2]} VARCHAR(255))")
        cur.executemany(f"INSERT INTO {table_name} VALUES (%s, %s, %s)", rows)
        conn.commit()
        conn.close()

    print('Data has been imported to RDS')