# AWS-DataBridge
AWS-DataBridge is a CLI application designed for AWS EC2 instances that allows users to import data from various file formats (XML, TXT, JSON, CSV) into multiple AWS databases including RDS, DynamoDB, Neptune, and DocumentDB. This tool automates the process of data conversion (converts all types to csv) and storage, ensuring flexibility and ease of use for different database needs.

## Features
- Converts and imports XML, TXT, JSON, and CSV files into AWS databases.
- Supports AWS RDS, DynamoDB, Neptune, and DocumentDB.
- Provides flexibility for users to import data into multiple databases from a single file.
- Automatically creates tables and databases if they do not already exist.

## Installation

To install AWS DataBridge using pip3 (reccomended): 
In your Ec2 instance run the following command
```bash
pip3 install -i https://test.pypi.org/simple/ aws-databridge==0.1.4 --extra-index-url https://pypi.org/simple
```
## Usage 
After the install you can run the following command to run the program 
```bash
aws-databridge
```
## Neccessary Enviroment Setup
There are some neccessary set up requirements in order to use the application without errors for each database 
### IAM Role
Make sure your EC2 has the required IAM Role permissions attached to your EC2 instance for each of the databases you are attempting to import to
### RDS env variables 
To interact with your RDS instance you need to have the following credentials stored on your EC2 
```bash
export RDS_HOST="your-rds-endpoint.rds.amazonaws.com"
export RDS_USER="your-username"
export RDS_PASSWORD="your-password"
export RDS_DB="your-database-name"
export RDS_PORT="3306"
```
### Data Location 
Currently only Data located on the EC2 instance is supported, to transfer data from your machine to the EC2 run: 
```bash
rsync -avz --exclude '.venv' -e "ssh -i ~/.ssh/<your pem name>.pem" <path to your code> ec2-user@<ec2 ip>:/home/ec2-user/
```



