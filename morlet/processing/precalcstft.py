from scipy.signal import stft
from numpy import shape

def precalc(eeg):
    return np.stack(
            stft(eeg.data[i], 
                nperseg=eeg.fs) for i in shape(eeg.data)[0], axis=0
            )



