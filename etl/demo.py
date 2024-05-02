
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

test = spark.read.format('csv').load("s3://test/amgen", header = True)
    
test.write.format('csv').mode('overwrite').save('s3://test/amgen', header = True)
print("Code Executed Successfully")
    