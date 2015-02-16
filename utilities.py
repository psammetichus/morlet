# -*- coding: utf-8 -*-
"""
Created on Sun Feb 15 18:29:33 2015

@author: Tyson
"""

import numpy as np

def sampsToSec(sampR, nsamps):
    return nsamps/sampR


def secToSamps(sampR, nsecs):
    return nsecs*sampR

def cycsPerSec(sampR):
    return 1.0/(2*sampR)

def sigprocHalf(n):
    return n // 2 if n % 2 == 0 else n // 2 + 1

def freqs(n, sampR):
    return np.asarray([float(i)/(0.5*n) * 0.5*sampR for i in xrange(sigprocHalf(n))])
