import h5eeg
import pyedflib as edf
import h5py

OKlbls = [  "Fp1", "F3", "C3", "P3", "O1",
            "Fp2", "F4", "C4", "P4", "O2",
            "F7", "T3", "T5", "F8", "T4", "T6",
            "Fz", "Cz", "Pz", "A1", "A2"]

def saveEEGtoHDF(edf_file, filename):

    rr = edf.EdfReader(edf_file)
    samps = rr.getNSamples()[2]
    chanlabels = enumerate(rr.getSignalLabels())
    eegdata = dict()
    

    for i,l in chanlabels:
        if rr.getLabel(i) in OKlbls:
            eegdata[l] = rr.readSignal(i)

    h5file = h5eeg.HDFEEG(filename)
    h5file.store_dataset(eegdata.keys(), h5eeg.np.vstack(eegdata.values()),
            rr.getSampleFrequency(2), [])

    h5file.close()


