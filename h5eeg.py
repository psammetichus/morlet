# an HDFEEG class for dealing with HDF EEG files
import pyedflib as edf
import h5py
import scipy.signal as sgnn
import numpy as np
import uuid

class HDFEEG (object):
    h5file = None
    
    def __init__(self, filename):
        self.h5file = h5py.File(filename)
        self.datagrp = h5file.create_group("data")
    def __getitem__(self, label):
        return self.h5file["data"][label].value
    def get_recs(self):
        return self.h5file.get("/data")
    def store_dataset(self, labels, data, fs, annots, offset=0. ):
        g = self.datagrp.create_group(uuid.uuid1().hex)
        g.create_dataset("data", data=data)
        g.create_dataset("labels", data=labels)
        g.attrs['fs']=fs
        g.attrs['offset'] = offset
        g.create_dataset("annots", shape=(len(annots),), dtype=[('offset',
            '<u8'), ('text', 'S64')], data=annots)
        return g
     

OKlbls = [  "Fp1", "F3", "C3", "P3", "O1",
            "Fp2", "F4", "C4", "P4", "O2",
            "F7", "T3", "T5", "F8", "T4", "T6",
            "Fz", "Cz", "Pz", "A1", "A2"]

def saveEEGtoHDF(edf_file, filename):

    rr = edf.EdfReader(edf_file)
    samps = rr.getNSamples()[2]
    chanlabels = enumerate(rr.getSignalLabels())
    eegdata = dict()
    

    for i,l in chanlabels:
        if rr.getLabel(i) in OKlbls:
            eegdata[l] = rr.readSignal(i)

    h5file = HDFEEG(filename)
    for k, v in eegdata.items():
        h5file.store_dataset(k, data=v)


def filterEEG(eegdata, lpcutoff=0.7, hpcutoff=0.01):
    b,a = sgnn.butter(2, [hpcutoff, lpcutoff], btype='bandpass')
    return sgnn.filtfilt(eegdata, b, a)


def convertGDFtoDatetime (t):
    unixday = t >> 32 - 719529
    daypart = t & 0x00000000ffffffff
    seconds = daypart*86400.0/(2**32)
    return datetime.datetime(1970,1,1) + datetime.timedelta(unixday, seconds)


    
    
