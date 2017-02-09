#!coding:utf-8
import os
import os.path
import shutil

def loopRead(readPath,moveToPath):

    for parent, dirnames, filenames in os.walk(readPath):
        for dirname in dirnames:
            loopRead(dirname,moveToPath)

        for filename in filenames:
            print "PATH : "+parent+"/"+filename
            shutil.move(parent+"/"+filename,moveToPath)

if __name__ == "__main__":
    loopRead("/Users/zuston/Downloads/MillionSongSubset/data","/Users/zuston/pp")
