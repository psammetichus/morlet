#reads in EDF files using biosig

import biosig


channels = [ 	'Fp1', 'Fp2', 'F7', 
				'F8', 'F3', 'F4', 'T1', 'T2', 
				'T3', 'T4', 'T5', 'T6', 'O1',
				'O2', 'C3', 'C4', 'P3', 'P4', 
				'Fz', 'Cz', 'Pz']

def edfreadin(filename):
    hdr = biosig.sopen(filename, 'r', None)
    n = hdr.NS 
    eegs = {}
    v = biosig.sread(0, hdr.NRec*hdr.SPR, hdr)
    for i in range(n):
        k = hdr.CHANNEL[i].Label.split('\x00')[0]
        if k in channels:
            eegs[k] = v[i].astype('float32')
    return eegs


