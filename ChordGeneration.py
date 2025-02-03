# This Programatically generates MIDI files of chord sounds
# then the MIDI files will be turned into WAV files for better processing by the model

import librosa
import os
import mido
from mido import Message, Midifile, MidiTrack
import subprocess

# List of arrays for chords 
CHORDS = {
    "C_Major": [["C4", "E4", "G4"], ["G3", "C4", "E4"], ["E4", "G4", "C5"]]
}

INSTRUMENTS = {"piano": 0 }

# Method for making MIDI file
def Make_MIDI_file(chord_name, notes, instrument, filename):
    midi = Midifile()
    track = MidiTrack()
    midi.tracks.append(track)

    # set the intrument type
    track.append(Message('program_change', program=INSTRUMENTS[instrument], time=0))

    # start midi input based on music note
    for note in librosa.note_to_midi(notes):
        track.append(Message('note_on', note=int(note), velocity=64, time=0))

    # sustain the note for 5 seconds
    track.append(Message('note_off', note=int(librosa.note_to_midi(notes)[0]), velocity=64, time=5000))

    #stop midi input
    for note in librosa.note_to_midi(notes[1:]):
        track.append(Message('note_off', note=int(note), velocity=64, time=0))

    # save the midifile
    midi_path = f"dataset/midi/{filenname}.mid"
    midi.save(midi_path)
    return midi_path


print(Make_MIDI_Object(chords))
