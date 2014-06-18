import biosig



def edfreadin(filename):
    hdr = biosig.sopen(filename, 'r', None)
    n = 21
    eegs = {}
    v = biosig.sread(0, hdr.NRec*hdr.SPR, hdr)
    for i in range(n):
        k = hdr.CHANNEL[i].Label.split('\x00')[0]
        eegs[k] = v[i]
    return eegs


