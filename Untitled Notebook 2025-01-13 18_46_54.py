# Databricks notebook source
# MAGIC %run ./00-helper

# COMMAND ----------

base_dir = helper.get_external_location_url("leo-unmanaged-dev")

landing_zone = base_dir + "/data_zone"
checkpoint_base = base_dir + "/checkpoint_zone"    
test_data_dir = base_dir_data + "/test_data"

print(landing_zone + " " + checkpoint_base + " " + test_data_dir )
