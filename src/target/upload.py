from src.log.log import log
from pyspark.sql import SparkSession

##todo
## here should be a function to upload it to hdfs
## but as of right now it isn't working
def write_data(data,type):
    log("Write into spark")
    sparkSession = SparkSession.builder.appName("example-pyspark-read-and-write").getOrCreate()
    df = sparkSession.createDataFrame(data)
    #print(df)
    log("Write into hdfs")
    df.write.csv("hdfs://localhost:9000/example.csv")
    return None