import os 
import sys 
import json 

from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")
print(MONGO_DB_URL)

import certifi
ca = certifi.where()

import pandas as pd 
import numpy as np 
import pymongo 
from networksecurity.logging.logger import logging
from networksecurity.exception.exception import NetworkSecurityException 


class NetworkDataExtrack(): 
    def __init__(self):
        try: 
            pass 
        except Exception as e: 
            raise NetworkSecurityException(e)
        
    def csv_to_json_convertor(self,file_path): 
        try: 
            data = pd.read_csv(file_path)
            data.reset_index(drop=True, inplace=True)
            records = list(json.loads(data.T.to_json()).values())
            return records
        except Exception as e: 
            raise NetworkSecurityException(e)
        
    def insert_data_mongodb(self,records,database,collection): 
        try: 
            self.database = database 
            self.collection = collection 
            self.records = records 
            self.mogo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mogo_client[self.database]
            self.collection=self.database[self.collection]
            self.collection.insert_many(self.records)
            return(len(self.records))
        except Exception as e: 
            raise NetworkSecurityException(e)
        
if __name__ == "__main__": 
    FILE_PATH = "/Users/udit/Desktop/NetworkSecurity/Network_Data/phisingData.csv"
    DATABASE = "UDITAI"
    COLLECTION = "NetworkData"
    network_obj=NetworkDataExtrack()
    records = network_obj.csv_to_json_convertor(file_path=FILE_PATH)
    no_of_records = network_obj.insert_data_mongodb(records,DATABASE,COLLECTION)
    print(no_of_records)
