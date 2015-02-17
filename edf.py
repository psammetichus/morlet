#Python native reading of EDF files
import io
import datetime as dt
import numpy as np
import logging


sor = ["Fz",
       "Fp1",
       "Fp2",
       "F3",
       "F4",
       "Cz",
       "C3",
       "C4",
       "P3",
       "P4",
       "Pz",
       "O1",
       "O2",
       "F7",
       "F8",
       "T3",
       "T4",
       "T5",
       "T6",
       "A1",
       "A2"]

def read_edf_header_preamble(stream):
    version = stream.read(8)
    patientID = stream.read(80)
    recordInfo = stream.read(80)
    startdate = stream.read(8)
    starttime = stream.read(8)
    hdrbytes = stream.read(8)
    reserved = stream.read(44)
    NR = stream.read(8)
    rec_dur = stream.read(8)
    NS = stream.read(4)

    hdr = dict()
    demo = dict()
    #our converted files may not actually follow this
#    (mrn, sex, dob, names) = patientID.split(" ")
    name = patientID.rstrip() #.split("_")
 #   demo["mrn"] = mrn
  #  demo["sex"] = sex
    demo["name"] = name
#    demo["name"] = gname
 #   (dobMo, dobD, dobY) = map(int, dob.split("."))
    # demo["dob"] = dt.date(dobY+1900 if dobY < 85 else dobY+2000,
    #                       dobMo,
    #                       dobD)
    hdr["demo"] = demo
    hdr["hdrlen"] = int(hdrbytes)
    hdr["NR"] = int(NR)
    hdr["rec_dur"] = float(rec_dur)
    hdr["NS"] = int(NS)
    
    return hdr

def getsignalinfo(stream, hdr):
    ns = hdr["NS"]
    channels = dict()
    labels = dict()
    for i in range(ns):
        lbl = stream.read(16).rstrip()
        labels[i] = lbl
        channels[lbl] = dict()
    for field, nbytes, f in [ ("tducer", 80, str), ("physDim", 8, lambda(n): n.rstrip()),
                              ("physMin", 8, float), ("physMax", 8, float),
                              ("digMin", 8, int), ("digMax", 8, int),
                              ("prefilt", 80, str), ("nsamps", 8, int) ]:
        for i in range(ns):
            channels[labels[i]][field] = f(stream.read(nbytes))
    
    #throw away
    stream.read(32*ns)
    hdr["chans"] = channels
    hdr["lbls"] = labels
    return hdr

def getsignals(stream, hdr):
    ch = hdr["chans"]
    for i in ch.keys():
        ch[i]["data"] = np.zeros(ch[i]["nsamps"]*hdr["NR"])
    for i in range(hdr["NR"]):
        for j in range(hdr["NS"]):
            c = ch[hdr["lbls"][j]]
            rawdata = np.frombuffer(stream.read(c["nsamps"]*2), np.int16)
            scaleF = 1.0/(c["digMax"]-c["digMin"])*(c["physMax"]-c["physMin"])
            c["data"][i*c["nsamps"]:(i+1)*c["nsamps"]] = scaleF * rawdata
    return hdr

class Signal(object):
    def __init__(self, samplingRate, data):
        self.sampR = samplingRate
        self.data = data

def readFile(fname):
    fio = io.FileIO(fname, 'r')
    stream = io.BufferedReader(fio)
    log = logging.getLogger('edf')
    log.info("starting to read preamble")
    hdr = read_edf_header_preamble(stream)
    log.info("read preamble; starting to read signal info")
    hdr = getsignalinfo(stream, hdr)
    log.info("read sig info; starting to read signals")
    hdr = getsignals(stream, hdr)
    stream.close()
    for lbl in hdr["chans"].keys():
        if lbl not in sor:
            del hdr["chans"][lbl]

    return {lbl : Signal(othData["nsamps"]/hdr["rec_dur"], othData["data"]) for lbl, othData in hdr["chans"].items()}





            
                              
