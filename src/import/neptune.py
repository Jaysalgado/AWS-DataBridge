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

data = "./data/diabetes_data.csv"

d_frame = pd.read_csv(data)

