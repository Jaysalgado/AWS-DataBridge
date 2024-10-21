import csv
import pandas as pd
import boto3

data = "./data/diabetes_data.csv"

try:
    d_frame = pd.read_csv(data)
    print(f"Data loaded from {data}")
except FileNotFoundError:
    print("File not found.")
    exit(1)
except pd.errors.EmptyDataError:
    print("The provided file is empty. Please load appropriate file.")

node_id = input("Which column would you like to use as the unique identifier for the nodes? ")
if node_id not in d_frame.columns:
    print(f"{node_id} not found in data.")
    exit(1)

if d_frame[node_id].isnull().any():
    print("The column you identified contains null values. Please rectify.")
    exit(1)

property_id = input("What are the column names you would like to use as the properties for your nodes?  ")
if property_id not in d_frame.columns:
    print(f"{property_id} not found in data.")
    exit(1)

relationship_id = input("Enter the column names that represent relationships, no name is fine: ")

vertex_export = "/mnt/data/vertex.csv"
edges_export = "/mnt/data/edges.csv"

with open(vertex_export, 'w', newline='') as v, open(edges_export, 'w', newline='') as e:
    vertex_mod = csv.writer(v)
    edge_mod = csv.writer(e)

    edge_id = 1

    vertex_mod.writerow(['~id', '~label'] + relationship_id)
    edge_mod.writerow(['~id', '~from', '~to', '~label'])

    for index, row in d_frame.iterrows():
        node_id_trace = f'{row[node_id]}'
        node_properties = [row[col.strip()] for col in property_id]
        vertex_mod.writerow([node_id, 'Node'] + node_properties)

        for rel_col in relationship_id:
            if rel_col.strip() and pd.notna(row[rel_col.strip()]):
                related_node_id = f'{row[rel_col.strip()]}'
                edge_mod.writerow([f'e{edge_id}', node_id, related_node_id, f'relatedTo_{rel_col.strip()}'])
                edge_id += 1

print('Vertices and edges CSV files have been written.')

# The CSV's for Neptune have been generated. Now upload to DB with Boto3.
# We need to use Amazon Neptune's Bulk Loader which will only accept files from Amazon S3

client_container = boto3.client('s3') 
import_bucket = 'import-bucket'

try: 
    client_container.upload_file(vertex_export, import_bucket, 'vertex.csv')
    print(f"{vertex_export} uploaded to S3 bucket: {import_bucket}")
    client_container.upload_file(edges_export, import_bucket, 'edges.csv')
    print(f"{edges_export} uploaded to S3 bucket: {import_bucket}")
except boto3.exceptions.S3UploadFailedError as aws_err:
    print(f"Upload error: {aws_err}")
except boto3.exceptions.NoCredentialsError as auth_err:
    print(f"Credentials error: {auth_err}")

neptune = boto3.client('neptune-db')

def nep_load(s3_uri):
    response = neptune.start_loader_job(
        source = s3_uri,
        format = 'csv',
        iamRoleArn = 'arn:aws:iam::your-account-id:role/YourRoleName',
        region = 'my-region',
        failOnError = True
    )
    return response

vertex_s3_uri = f's3://{import_bucket}/vertex.csv'
edges_s3_uri = f's3://{import_bucket}/edges.csv'

response_vertices = nep_load(vertex_s3_uri)
print("Neptune Load for Vertex:", response_vertices)

response_edges = nep_load(edges_s3_uri)
print("Neptune Load for Edges:", response_edges)