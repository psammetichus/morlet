# an HDFEEG class for dealing with HDF EEG files
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
    def close(self):
        self.h5file.close()
     

def filterEEG(eegdata, lpcutoff=0.7, hpcutoff=0.01):
    b,a = sgnn.butter(2, [hpcutoff, lpcutoff], btype='bandpass')
    return sgnn.filtfilt(eegdata, b, a)


def convertGDFtoDatetime (t):
    unixday = t >> 32 - 719529
    daypart = t & 0x00000000ffffffff
    seconds = daypart*86400.0/(2**32)
    return datetime.datetime(1970,1,1) + datetime.timedelta(unixday, seconds)


    
    
