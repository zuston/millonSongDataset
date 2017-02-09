from __future__ import print_function
import sys
import time
from pyspark import SparkConf
from pyspark import SparkContext

sc = SparkContext(appName="pyspark_hdfs_test")

lines = sc.textFile("hdfs://localhost:9000/user/zuston/millonSongDataset")

words = lines.flatMap(lambda line:line.split("\t"))

pairs = words.map(lambda word:(word,1))

counts = pairs.reduceByKey(lambda a,b:a+b)

results = counts.collect()

for res in results:
    print(res)

sc.stop()
