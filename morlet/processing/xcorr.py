from scipy.signal import correlate

def xcorr(sig1, sig2):
    return Signal(sig1.fs, correlate(sig1.data, sig2.data))

