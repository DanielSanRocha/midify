#!/usr/bin/env python

import scipy
import click
import numpy as np
import pretty_midi

from midify.resample import resample
from midify.find_peaks import find_peaks, find_first_peak
from midify.notes import identify

def midify(data, rate, normalize_input=True, sample_rate=6000, peak_min_height=0.002, peak_threshold=0.00001, peak_min_distance=600, note_sample_size=1024, note_attack_shift=20, note_frequency_peak_min_height=0.20, note_frequency_threshold=0.01, midi_note_duration=0.5, verbose=False):
    """This function transforms an input audio data to the MIDI format identifying notes positions and frequencies."""

    data = np.array(data)
    if verbose:
        click.echo(f"File sample rate {rate}")

    if verbose:
        click.echo(f"Data Shape: {data.shape}")

    if len(data.shape) == 2:
        if verbose:
            click.echo(f"Converting data to mono channel...")
        data = np.sum(data, axis=1)/data.shape[1]
        if verbose:
            click.echo(f"New Data Shape: {data.shape}")

    if normalize_input:
        if verbose:
            click.echo("Normalizing input...")
        data = data/np.linalg.norm(data)

    if verbose:
        click.echo(f"Resampling data to rate {sample_rate}")
    resampled = resample(data, old_rate=rate, new_rate=sample_rate)

    peaks = find_peaks(resampled, height=peak_min_height, threshold=peak_threshold, min_distance=peak_min_distance)
    if verbose:
        click.echo(f"Found {len(peaks)} peaks")

    notes_samples = np.array([resampled[p + note_attack_shift: p + note_attack_shift + note_sample_size ] for p in peaks])

    if verbose:
        click.echo("Inferring notes...")
    notes = np.array([identify(x,rate=sample_rate, height=note_frequency_peak_min_height, threshold=note_frequency_threshold, verbose=verbose) for x in notes_samples])

    if verbose:
        click.echo("Generating MIDI file...")
    mf = pretty_midi.PrettyMIDI()
    piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
    piano = pretty_midi.Instrument(program=piano_program)

    for note_number, peak in zip(notes, peaks):
        start = peak/sample_rate
        note = pretty_midi.Note(velocity=100, pitch=note_number, start=start, end=start + midi_note_duration)
        piano.notes.append(note)

    mf.instruments.append(piano)

    return mf
