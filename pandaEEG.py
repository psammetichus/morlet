import pandas as pd

def convertArraysToFrame(dictOfArrays):
	return pd.DataFrame(dictOfArrays)

def saveIt(datFr, fname):
	datFr.save(fname)



