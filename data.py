
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
df_taskname=spark.read\
    .format("com.databricks.spark.redshift")\
    .option("tempdir", "temp")    .option("url", "jdbc")\
    .option("user", DBUtils(spark).secrets.get(scope="credina", key="username"))\
    .option("password", DBUtils(spark).secrets.get(scope="credina", key="password"))\
    .option("dbtable", "tablename")\
    .option("forward_spark_s3_credentials", True)\
    .load()


if condition is not None:
    df_taskname = df_taskname.filter(condition)
    
df_taskname.show()
    

# Write the DataFrame to the database table
df_taskname.write\
    .format("com.databricks.spark.redshift")\
    .option("tempdir", "temp")\
    .option("url", "jdbc")\
    .option('dbtable', 'tablename')\
    .option("user", DBUtils(spark).secrets.get(scope="credi", key="username"))\
    .option("password", DBUtils(spark).secrets.get(scope="credi", key="passsword"))\
    .option("dbtable", "tablename")\
    .option("forward_spark_s3_credentials", True)\
    .save()
    