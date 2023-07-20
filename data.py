
import os
from pyspark.sql import SparkSession
from pyspark.dbutils import DBUtils
import boto3
import json
import request

spark = SparkSession.builder\
            .appName('Python Spark')\
            .config("spark.sql.execution.arrow.enabled", "true")\
            .getOrCreate()

df_fdsfds = spark.read.format('json').load("dsfa")
    
df_fdsfds.write.format('json').save('fsdfsd', header = True)
    