import os
import sys

def changeToSvmFile(oldPath,newPath):
    readPoint = open(oldPath,"r")
    writePoint = open(newPath,"w")

    for oldString in readPoint.readlines():
        # oldString = line.readline()
        label = oldString.split(",")[0]
        changeValue = list()
        index = 0
        for ss in oldString.split(",")[1:]:
            changeValue.append(str(index)+":"+ss)
            index += 1

        newString = label
        for s in changeValue:
            newString += " "+s
        print newString

        writePoint.write(newString)


    readPoint.close()
    writePoint.close()

if __name__ == "__main__":
    changeToSvmFile("/Users/zuston/dev/machineLearning/training/yearPrediction/YearPredictionMSD.txt"
                    ,"/Users/zuston/dev/machineLearning/training/yearPrediction/yearSvmFile.txt")



