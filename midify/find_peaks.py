import scipy
import numpy as np

def find_peaks(data, height=0.2, threshold=0.001, min_distance=600):
    peaks = scipy.signal.find_peaks(data, height=height, threshold=threshold)[0]
    filtered_peaks = []

    q = 0
    for p in peaks:
        if len(filtered_peaks) == 0:
            filtered_peaks.append(p)
        else:
            if p - q > min_distance:
                filtered_peaks.append(p)
        q = p

    return np.array(filtered_peaks)

def find_first_peak(f, height=10, threshold=0.1):
    return scipy.signal.find_peaks(f, height=height, threshold=threshold)[0][0]
