import os
import sys
from pyspark import SparkContext
import time
from pyspark.mllib.classification import NaiveBayes, NaiveBayesModel
from pyspark.mllib.util import MLUtils

def init():
    sc = SparkContext(appName="yearPrediction")
    data = MLUtils.loadLibSVMFile(sc,"/Users/zuston/dev/machineLearning/training/yearPrediction/yearSvmFile.txt")
    traning , test = data.randomSplit([0.8,0.2])

    model = NaiveBayes.train(traning,1.0)

    predictionLabel = test.map(lambda x:(model.predict(x.features)))

    accuracy = 1.0 * predictionLabel.filter(lambda (x,v):x==v).count()/test.count()

    print accuracy

if __name__ == "__main__":
    init()