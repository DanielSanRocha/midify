import scipy


def resample(data, old_rate, new_rate=6000):
    return scipy.signal.resample(data, len(data) * new_rate // old_rate)
