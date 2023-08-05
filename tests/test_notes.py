import numpy as np
import pretty_midi

from midify import identify, resample


def test_identify_c4_piano():
    note = 60
    rate = 44100
    program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

    mf = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=program)
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=0, end=1.0))
    mf.instruments.append(piano)

    data = mf.fluidsynth()
    data = data/np.linalg.norm(data)

    assert identify(data[30:1058], rate) == note


def test_identify_csharp4_piano():
    note = 61
    rate = 44100
    program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

    mf = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=program)
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=0, end=1.0))
    mf.instruments.append(piano)

    data = mf.fluidsynth()
    data = data/np.linalg.norm(data)

    assert identify(data[0:2048], rate) == note

def test_identify_d4_piano():
    note = 62
    rate = 44100
    program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

    mf = pretty_midi.PrettyMIDI()
    piano = pretty_midi.Instrument(program=program)
    piano.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=0, end=1.0))
    mf.instruments.append(piano)

    data = mf.fluidsynth()
    data = data/np.linalg.norm(data)

    assert identify(data[0:1058], rate) == note


def test_identify_e4_piano():
    note = 64
    rate = 6000
    program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')

    mf = pretty_midi.PrettyMIDI()
    instrument = pretty_midi.Instrument(program=program)

    instrument.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=0, end=1.0))
    mf.instruments.append(instrument)

    data = mf.fluidsynth()
    data = data/np.linalg.norm(data)
    resampled = resample(data, 44100, rate)

    assert identify(resampled[0:512], rate) == note
