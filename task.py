#! coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
from pyspark import SparkConf
from pyspark import SparkContext
import h5py
import os

def init(path):
    fileList = list()
    for parent,dirnames,filenames in os.walk(path):
        for filename in filenames:
            fileList.append(filename)

    SparkInitParallelize(fileList,path)

def SparkInitParallelize(fileList,path):
    sc = SparkContext(appName="millonSongDataset_analysis_year")
    files = sc.parallelize(fileList)
    results = files.map(lambda x:(loadHdf5(path+"/"+x),1)).reduceByKey(lambda a,d:a+d)

    ress = results.collect()

    for res in ress:
        print res

    sc.stop()

# year songs count
def SparkInit():

    sc = SparkContext(appName="millonSongDataset_analysis_year")

    files = sc.textFile("hdfs://localhost:9000/user/zuston/millonSongDataset/TRAAAAW128F429D538.h5")

    results = files.map(loadHdf5(files))
    print results.count()
    sc.stop()

def loadHdf5(filepath):
    f = h5py.File(filepath,"r")

    if len(f.keys())<=0:
        return 0
    # year
    yearDataset = f.keys()[-1]
    yearDset = f[yearDataset]
    yearValue = yearDset[yearDset.keys()[-1]].value[0][1]

    # artist name
    nameDataset = f.keys()[-2]
    nameDset = f[nameDataset]
    nameValue = nameDset["songs"].value[0][9]

    return yearValue


if __name__ == "__main__":
    startTime = time.time()
    init("/Users/zuston/pp")
    endTime = time.time()

    durationTime = endTime-startTime
    print ""
    print "the task is the songs year count"
    print "the duration time is : "+ str(durationTime)

