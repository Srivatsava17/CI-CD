
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

condition = None
df_dsfdsafd = spark.read\
    .format("jdbc")\
    .option("url", "fdsfads")\
    .option("user", DBUtils(spark).secrets.get(scope="dsfsdfdsfdsf", key="dsfdsf"))\
    .option("password", DBUtils(spark).secrets.get(scope="dsfsdfdsfdsf", key="dsfsdf"))\
    .option("dbtable", "dsfsdf")\
    .option("driver", "fdsfdsf")\
    .load()

if condition is not None:
    df_dsfdsafd = df_dsfdsafd.filter(condition)
    
df_dsfdsafd.show()
    
        
taskname = dsfdsafd.withColumn("targetname",dsfdsafd.None+234)

        

# Write the DataFrame to the database table
df_taskname.write.format('jdbc')\
    .option('url', 'databricks')\
    .option('dbtable', 'tablename')\
    .option("user", DBUtils(spark).secrets.get(scope="credential", key="vign@gmail.com"))\
    .option("password", DBUtils(spark).secrets.get(scope="credential", key="sdfasd"))\
    .option('driver', 'drivername')\
    .mode('append')\
    .save()
    