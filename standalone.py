from pyspark.sql import SparkSession
import time

spark = SparkSession \
    .builder \
    .appName('standalone') \
    .getOrCreate()


schema = 'id INT, country STRING, hit LONG'
df = spark.createDataFrame(data=[(1,'kr',100),(2,'Kora',120),(3,'USA',80),(4,'Japan',40)], schema=schema)
print(df.count())

# sleep 10 minute
time.sleep(600)