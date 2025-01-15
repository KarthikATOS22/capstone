# Databricks notebook source
# MAGIC %run ./00-helper

# COMMAND ----------

class Config():    
    def __init__(self):      
        self.base_dir = helper.get_external_location_url("leo-unmanaged-dev")        
        self.db_name = "sbit_db"
        self.maxFilesPerTrigger = 1000
