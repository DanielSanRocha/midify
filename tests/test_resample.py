import numpy as np

from midify.resample import resample

def test_resample_simple():
    data = np.array([0.0,1.0,0.0,1.0])
    resampled = resample(data, old_rate=2, new_rate=1)

    new_length = (len(data) * 1) // 2

    assert len(resampled) == new_length
    assert resampled[0] == 0.5
    assert resampled[1] == 0.5

def test_resample_oversample_length():
    data = np.random.uniform(-1,1,size=300)
    resampled = resample(data, old_rate = 50, new_rate = 150)

    new_length = (len(data) * 150) // 50

    assert len(resampled) == new_length


def test_resample_undersample_length():
    data = np.random.uniform(-1,1,size=500)
    resampled = resample(data, old_rate = 150, new_rate = 33)

    new_length = (len(data) * 33) // 150

    assert len(resampled) == new_length
