import numpy as np
import util

class Montage(object):
    def __init__(self, chanMatrix, colors, filts, polarities):
        self.chanMatrix = chanMatrix
        self.colors = colors
        self.filts = filts
        self.pols = np.transpose(polarities)
        self.nchans = np.shape(chanMatrix)[0]

    def chan_data(self, eeg, chan):
        """returns data for channel @chan from the signal matrix @eeg which is
        arranged as an (electrode x time sample) ndarray, parameterized by the
        polarities"""
        return util.filter (self.pols @ self.chanMatrix @ eeg)


    
