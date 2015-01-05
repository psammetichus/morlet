###hdf2webeeg.py



import h5eeg
import struct
from numpy import hstack

def convert(h5file):
    eegdata = h5eeg.HDFEEG(h5file)
    NS = eegdata.get_NS()
    NREC = eegdata.get_NRec()
    labels = eegdata.get_labels()
    hdrsize = 4 + 4 + 4 + 4 + (NS*4)
    hdrsize += hdrsize % 8 #packed to 8-byte boundary
    hdr = struct.pack("4i%ds" % (NS*4), NS, 200, hdrsize,
                      NREC, 
                      "".join([str(l.ljust(4)) for l in labels]))
    data = struct.pack("%dd" % (NS*NREC), 
                       *hstack(
            eegdata.h5file["data"].values()))
    return hdr+data

    
        
