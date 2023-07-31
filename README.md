# Midify

Midify is a command line tool for converting audio data in MIDI data identifying notes positions and frequencies.

## Installation

Inside a virtualenv run

```bash
pip install midify
```

## Usage

The simplest usage from the cli:

```bash
midify input.wav --output output.mid
```

You can also use it programatically from python or a jupyter notebook:

```python
import scipy
from midify import midify

rate,data = scipy.io.wavfile.read("input.wav")
mf = midify(data=data,rate=rate)

waveform = mf.fluidsynth(fs=44100)
IPython.display.Audio(waveform, rate=44100)
```

## Algorithm

The algorithm consists of two steps; first we use `scipy.signal.find_peaks` to find the beggining of each note; after that the program uses scipy FFT to find the first peak in the frequency spectrum which we assume is the root harmonic (the played note).

## Acknowledgments

Made with Love by Daniel Santana
