# Databricks notebook source
class helper():
        @staticmethod
        def get_external_location_url(location_name):
                return spark.sql(f"DESCRIBE EXTERNAL LOCATION `{location_name}`") \
                .select("url") \
                .collect()[0][0]
