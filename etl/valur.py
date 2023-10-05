
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

CommitCheck = spark.read.format('json').load("CommitCheck", header = True)
    
CommitCheck.write.format('csv').mode('overwrite').save('kjhg', header = True)
display(CommitCheck)
    