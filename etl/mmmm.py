
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

extract1 = spark.read.format('csv').load("s3://pharcomm360/etl_lcnc/export (8).csv", header = True)
    
extract2 = spark.read.format('csv').load("s3://pharcomm360/etl_lcnc/export (7).csv", header = True)
    

 

join = extract1.join(extract2, extract1.Emp_NO == extract2.Emp_NO,"inner").drop(extract1.Emp_NO)



filtercol = join.filter(col("Salary") > 25000)



filtercol2 = filtercol.filter(col("Emp_Add") == "GNoida")



result_df = filtercol2.filter(col("Dept_No").isNotNull() & (trim(col("Dept_No")) != '') & (~col("Dept_No").rlike(r'^-?[0-9]+$')))

# Add a 'IntegerCheck' column with 'Passed' initially to the existing DataFrame 'df1'
intcheck = filtercol2.withColumn("IntegerCheck", F.lit("Passed"))

# Apply the primary key comparison and update the 'IntegerCheck' column accordingly
comparison_result = result_df.select('Emp_No')
primary_key_value = [row[0] for row in comparison_result.collect()]
intcheck = intcheck.withColumn("IntegerCheck", F.when(F.col('Emp_No').isin(*primary_key_value), "Failed").otherwise("Passed"))

rule_failed_records = intcheck.filter(F.col("IntegerCheck") == "Failed").drop('IntegerCheck')


# Optionally filter only the passed records if filter_passed is True

intcheck = intcheck.filter(col('IntegerCheck') == "Passed").drop('IntegerCheck')



if not rule_failed_records.isEmpty():
    rule_failed_records.write.options(header=True).mode('overwrite').csv("s3://pharcomm360/etl_lcnc/failedrecords/")


intcheck.write.format('csv').mode('overwrite').save('s3://pharcomm360/etl_lcnc/output/', header = True)
display(intcheck)
    