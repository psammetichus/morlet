import edfreader
import h5py
import scipy.signal as sgnn

class HDFEEG (object):
    h5file = None
    
    def __init__(self, filename):
        self.h5file = h5py.File(filename)
    def __getitem__(self, label):
        return self.h5file["data"][label].value
    def get_NS(self):
        return len(self.h5file["data"])
    def get_labels(self):
        return self.h5file["data"].keys()
    def get_NRec(self):
        dddd = self.h5file["data"]
        return max([len(i) for i in dddd.values()])


def saveEEGtoHDF(eegdata, filename):
    h5file = h5py.File(filename)
    g = h5file.create_group("data")
    for k,v in eegdata.items():
        g.create_dataset(k, data=v, compression='gzip')
    h5file.close()


def filterEEG(eegdata, lpcutoff=0.7, hpcutoff=0.01):
    b,a = sgnn.butter(2, [hpcutoff, lpcutoff], btype='bandpass')
    return sgnn.filtfilt(eegdata, b, a)


def convertGDFtoDatetime (t):
    unixday = t >> 32 - 719529
    daypart = t & 0x00000000ffffffff
    seconds = daypart*86400.0/(2**32)
    return datetime.datetime(1970,1,1) + datetime.timedelta(unixday, seconds)


    
    
