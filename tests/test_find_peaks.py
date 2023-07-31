import numpy as np

from midify.find_peaks import find_peaks, find_first_peak

def test_find_peaks_simple_data():
    data = np.array([0.0,0.0,1.0,0.0])
    peaks = find_peaks(data, height=0.2, threshold=0.1, min_distance=1)

    assert len(peaks) == 1
    assert peaks[0] == 2

def test_find_peaks_two_peaks():
    data = np.array([0.0,0.0,1.0,0.0,1.0,0.0,0.0])
    peaks = find_peaks(data, height=0.7, threshold=0.5, min_distance=1)

    assert len(peaks) == 2
    assert peaks[0] == 2
    assert peaks[1] == 4

def test_find_peaks_too_close_peaks():
    data = np.array([0.0,0.0,1.0,0.0,1.0,0.0,0.0])
    peaks = find_peaks(data, height=0.7, threshold=0.5, min_distance=5)

    assert len(peaks) == 1
    assert peaks[0] == 2

def test_find_first_peak_simple_case():
    data = np.array([0.2,0.1,1.0,0.2])
    peak = find_first_peak(data, height=0.2, threshold=0.3)

    assert peak == 2

def test_find_first_peak_no_peak():
    data = np.array([0.7,0.8,1.0,0.9])
    peak = find_first_peak(data, height=0.5, threshold=0.4)

    assert peak == 2