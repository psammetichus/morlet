import scipy.signal as sn


class Signal(object):
    def __init__(self, samplingRate, data):
        self.sampR = samplingRate
        self.data = data
        self.hpass = self.nfreq(70.0)
        self.lpass = self.nfreq(1.0)
        self.fcoeffs = sn.iirfilter(2, [self.lpass, self.hpass])
        self.cache = None
            
    def nfreq(self, freq):
        """returns the frequency normalized to 1 = Nyquist"""
        return freq/(0.5*self.sampR)
            
    def getRawData(self):
        return self.data
    
    def getFiltData(self):
        if self.cache is None:
            self.cache = sn.filtfilt(self.fcoeffs[0], self.fcoeffs[1], self.getRawData())
        return self.cache


