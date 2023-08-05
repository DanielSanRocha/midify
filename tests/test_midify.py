import librosa
import scipy

from midify.midify import midify


def test_riff1_wav_mono():
    filename = "samples/riff1.wav"
    rate, data = scipy.io.wavfile.read(filename)

    midi = midify(data=data,rate=rate)

    assert len(midi.instruments) == 1

    piano = midi.instruments[0]
    notes = piano.notes

    assert len(notes) == 11

    assert notes[0].pitch == 43
    assert notes[1].pitch == 50
    assert notes[2].pitch == 46
    assert notes[3].pitch == 45
    assert notes[4].pitch == 43
    assert notes[5].pitch == 46
    assert notes[6].pitch == 45
    assert notes[7].pitch == 43
    assert notes[8].pitch == 42
    assert notes[9].pitch == 45
    assert notes[10].pitch == 38

def test_riff1_wav_stereo():
    filename = "samples/riff1_stereo.wav"
    rate, data = scipy.io.wavfile.read(filename)

    midi = midify(data=data,rate=rate)

    assert len(midi.instruments) == 1

    piano = midi.instruments[0]
    notes = piano.notes

    assert len(notes) == 11

    assert notes[0].pitch == 43
    assert notes[1].pitch == 50
    assert notes[2].pitch == 46
    assert notes[3].pitch == 45
    assert notes[4].pitch == 43
    assert notes[5].pitch == 46
    assert notes[6].pitch == 45
    assert notes[7].pitch == 43
    assert notes[8].pitch == 42
    assert notes[9].pitch == 45
    assert notes[10].pitch == 38

def test_riff1_mp3_mono():
    filename = "samples/riff1.mp3"
    data, rate = librosa.load(filename)

    midi = midify(data=data,rate=rate)

    assert len(midi.instruments) == 1

    piano = midi.instruments[0]
    notes = piano.notes

    assert len(notes) == 11

    assert notes[0].pitch == 43
    assert notes[1].pitch == 50
    assert notes[2].pitch == 46
    assert notes[3].pitch == 45
    assert notes[4].pitch == 43
    assert notes[5].pitch == 46
    assert notes[6].pitch == 45
    assert notes[7].pitch == 43
    assert notes[8].pitch == 42
    assert notes[9].pitch == 45
    assert notes[10].pitch == 38

def test_riff1_mp3_stereo():
    filename = "samples/riff1_stereo.mp3"
    data, rate = librosa.load(filename)

    midi = midify(data=data,rate=rate)

    assert len(midi.instruments) == 1

    piano = midi.instruments[0]
    notes = piano.notes

    assert len(notes) == 11

    assert notes[0].pitch == 43
    assert notes[1].pitch == 50
    assert notes[2].pitch == 46
    assert notes[3].pitch == 45
    assert notes[4].pitch == 43
    assert notes[5].pitch == 46
    assert notes[6].pitch == 45
    assert notes[7].pitch == 43
    assert notes[8].pitch == 42
    assert notes[9].pitch == 45
    assert notes[10].pitch == 38

def test_riff2_wav_mono():
    filename = "samples/riff2.wav"
    rate,data = scipy.io.wavfile.read(filename)

    midi = midify(data=data,rate=rate)

    assert len(midi.instruments) == 1

    piano = midi.instruments[0]
    notes = piano.notes

    assert len(notes) == 12

    assert notes[0].pitch == 28
    assert notes[1].pitch == 31
    assert notes[2].pitch == 33
    assert notes[3].pitch == 28
    assert notes[4].pitch == 31
    assert notes[5].pitch == 34
    assert notes[6].pitch == 33
    assert notes[7].pitch == 28
    assert notes[8].pitch == 31
    assert notes[9].pitch == 33
    assert notes[10].pitch == 31
    assert notes[11].pitch == 28
