import scipy.signal as sn


class Signal(object):
    def __init__(self, samplingRate, data):
        self.fs = samplingRate
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

class EEGDataInhomo(object):
    def __init__(self, signals, annots, demo):
        self.sigs = signals
        self.annots = annots
        self.demo = demo

class EEGData(object):
    def __init__(self, signals, annots, demo):
        if all( [i.fs is signals[0].fs for i in signals] ):
            self.data = np.hstack( [i.data for i in signals] )
            self.fs = signals[0].fs
            self.hpass = self.nfreq(70.0)
            self.lpass = self.nfreq(1.0)
            self.fcoeffs = sn.iirfilter(2, [self.lpass, self.hpass])
            self.cache = None
            self.annots = annots
            self.demo = demo
        else:
            raise Exception("inhomogenous fs")
    

class Demographics(Object):
    def __init__(self, identifier, age, sex):
        self.id = identifier
        self.age = age
        self.sex = sex



