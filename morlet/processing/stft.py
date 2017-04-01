# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 18:19:23 2015
times
@author: Tyson
"""

#short-term fourier transform

import scipy.signal as sgn
import utilities

def std_stft(data, fs):
    """calculates STFT for a real array with default step size fs/2 and overlap
    fs/4."""
    return sgn.stft(data, nperseg=fs//2)


