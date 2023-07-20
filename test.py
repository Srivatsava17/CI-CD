
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

df_dataset2222 = spark.read.format('avro').load("path")
    
df_dataset2222.write.format('json').save('path', header = True)
    