# neptune uses Gremlin (property graphs) or SPARQL (RDF data and semantic applications)
# relational != graph 
# need to transform relational data into graph data
# need to decide which columns represent nodes (entities) and which are edges (relationships)

# property graphs good fit for health-data because they model complex data

# ask if primary key exist, and which column that is, if none exist, then create
# arbritrary primary key for each row
# provide choice to name it

# each entity indicated by the primary key is a node, the rest of the tuples
# indicate the "edges" or relationships 

# 1) ask if one csv or two csv (node/edge)
# 2) ask for primary key column, if none programmatically add one, make that node
# 3) push to db

import csv
import pandas as pd
import boto3

data = "./data/diabetes_data.csv"

d_frame = pd.read_csv(data)

node_id = input("Which column would you like to use as a unique identifier for the nodes: ")
property_id = input("What are the column names you would like to use as properties for your nodes: ")
relationship_id = input("Enter the column names that represent relationships, no name is fine: ")

vertex_export = "/mnt/data/vertex.csv" # Temporary placeholder for csv files generated
edges_export = "/mnt/data/edges.csv" # Temporary placeholder for csv files generated

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

print('Vertices and edges CSV files have been generated.')

# The CSV's for Neptune have been generated. Now upload to DB with Boto3.
# We need to use Amazon Neptune's Bulk Loader which will only accept files from Amazon S3

client_container = boto3.client('s3')
import_bucket = 'import-bucket'

client_container.upload_file(vertex_export, import_bucket, 'vertex.csv')
client_container.upload_file(edges_export, import_bucket, 'edges.csv')

neptune = boto3.client('neptune-db')

def neptune_bulk_loader_call(s3_uri):
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

response_vertices = neptune_bulk_loader_call(vertex_s3_uri)
print("Neptune Load for Vertex:", response_vertices)

response_edges = neptune_bulk_loader_call(edges_s3_uri)
print("Neptune Load for Edges:", response_edges)