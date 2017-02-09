import os
import sys
from pyspark import SparkContext
import time
import h5py as h

def cost(func):
    def wrapper(*arf,**kwargs):
        stime = time.time()
        func(*arf,**kwargs)
        etime = time.time()
        durationTime = etime-stime
        print "the %s cost time : %f"%(func.__name__,durationTime)

    return wrapper

@cost
def init(path):
    fileList = list()
    for parent,dirnames,filenames in os.walk(path):
        for filename in filenames:
            fileList.append(filename)

    SparkDeal(fileList,path)

def SparkInit(fileList):
    sc = SparkContext(appName="similar_artist_count")
    files = sc.parallelize(fileList)
    return files

def SparkDeal(fileList,path):
    fileNameRdd = SparkInit(fileList)
    results = fileNameRdd.flatMap(lambda x:loadData(path+"/"+x)).map(lambda x:(x,1)).reduceByKey(lambda a,b:a+b)
    resultsCollect = results.collect()
    for res in resultsCollect:
        print res

def loadData(x):
    f = h.File(x,"r")
    artistValue = []
    if len(f.keys()) >= 3:
        artistDataset = f.keys()[1]
        artistDset = f[artistDataset]
        artistValue = artistDset["similar_artists"].value

    return artistValue


if __name__ == "__main__":
    init("/Users/zuston/pp")
