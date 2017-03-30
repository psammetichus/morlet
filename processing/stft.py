# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 18:19:23 2015
times
@author: Tyson
"""

#short-term fourier transform

import numpy as np
import scipy
import utilities

def stft(n, step, overlap):
    """calculates short-time fourier transform for an array (assumed real)
    given the @step in samples, and the @overlap in samples."""
    eStep = step - overlap
    times = len(n) / (step-(overlap/2))
    winfun = scipy.hamming(step)
    coeffs = utilities.sigprocHalf(step)
    output = np.zeros((times+1, 2, coeffs))
    for i in xrange(times+1):
        o = scipy.fft(winfun*n[i*eStep:i*eStep+step], n=step)
        output[i] = np.vstack( (np.abs(o[:coeffs]), np.angle(o[:coeffs])) )
    return output

def std_stft(data, fs):
    """calculates STFT for a real array with default step size fs/2 and overlap
    fs/4."""
    return stft(data, fs/2., fs/4.)


