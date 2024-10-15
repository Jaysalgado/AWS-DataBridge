# noSQL DB
# compatible with mongoDB
# stores data in JSON'ss
# store information without pre-defined schema's
# convert from CSV > JSON

import pandas as pd 

data = "./data/diabetes_data.json" # Path to data file

d_frame = pd.read_csv(data) # Setting data frame variable

