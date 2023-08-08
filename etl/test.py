
import os
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.functions import *
from pyspark.sql.types import *
import boto3
import json


spark = SparkSession.builder\
            .appName('Python Spark')\
            .config("spark.sql.execution.arrow.enabled", "true")\
            .getOrCreate()

extract_from_source = spark.read.format('parquet').load("pharcomm360_test", header = True)
    
        
add_new_column = extract_from_source.withColumn("additional_column",extract_from_source.new_column+50)

        