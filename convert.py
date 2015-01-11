import edfreader as er
from sys import argv
import h5eeg

def main():
	if argv[1] is None:
		print "convert edf files to hdf files"
	eegs = er.edfreadin(argv[1])
	h5eeg.saveEEGtoHDF(eegs, argv[1][:-4]+'.eegh5')

if __name__ == '__main__':
	main()


