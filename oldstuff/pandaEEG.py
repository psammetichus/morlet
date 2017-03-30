#uses Pandas to save simple dict of arrays  as an hdf file
import pandas as pd

def convertArraysToFrame(dictOfArrays):
	return pd.DataFrame(dictOfArrays)

def saveIt(datFr, fname):
	datFr.save(fname)



