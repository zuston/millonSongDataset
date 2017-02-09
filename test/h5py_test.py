import os
import sys
import h5py


def loadFile(filepath):
    f = h5py.File(filepath,"r")
    for dataset in f.keys():
        dset = f[dataset]

        for groupValue in dset.keys():
            print groupValue
            print dset[groupValue].value

    # year
    yearDataset = f.keys()[-1]
    yearDset = f[yearDataset]
    yearValue = yearDset[yearDset.keys()[-1]].value[0][1]
    print yearValue

    nameDataset = f.keys()[-2]
    nameDset = f[nameDataset]
    nameValue = nameDset["songs"].value[0][9]
    print nameValue

    if len(f.keys())>=2:
        artistDataset = f.keys()[1]
        artistDset = f[artistDataset]
        artistValue = artistDset["similar_artists"].value

if __name__ == "__main__":
    loadFile("/Users/zuston/pp/TRAXLZU12903D05F94.h5")
