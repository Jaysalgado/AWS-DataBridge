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
##Usage 
After the install you can run the following command to run the program 
```bash
aws-databridge
```
