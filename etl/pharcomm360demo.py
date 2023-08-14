
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

extract = spark.read.format('parquet').load("s3://gen-insights/laad_source", header = True)
    
        
filtercol = extract.filter(col("Final Claim Status") == "APPROVED")

        
filtercol.write.format('parquet').mode('overwrite').save('s3://gen-insights/laad_test', header = True)
display(filtercol)
    