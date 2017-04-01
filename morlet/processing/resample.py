from scipy.signal import resample

def resample_by_freq(sig, fsprime):
    """resamples signal to new fs, fsprime"""
    ratio = fsprime/sig.fs
    return Signal(fsprime, resample(sig.data, (1./ratio)*np.size(sig.data,0)))

def resample_by_len(sig, newlen):
    """resamples signal to new length newlen"""
    ratio = newlen/np.size(sig.data,0)
    return Signal( (1./ratio)*sig.fs, resample(sig.data, newlen))

