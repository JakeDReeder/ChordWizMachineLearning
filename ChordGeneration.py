# This Programatically generates MIDI files of chord sounds
# then the MIDI files will be turned into WAV files for better processing by the model

import librosa
import os
import mido
from mido import Message, MidiFile, MidiTrack
import subprocess

# List of arrays for chords 
CHORDS = {
    "C_Major": [["C4", "E4", "G4"], ["G3", "C4", "E4"], ["E4", "G4", "C5"]]
}

INSTRUMENTS = {"piano": 0 }

# Method for making MIDI file
def make_midi_file(chord_name, notes, instrument, filename):
    midi = MidiFile()
    track = MidiTrack()
    midi.tracks.append(track)

    # set the intrument type
    track.append(Message('program_change', program=INSTRUMENTS[instrument], time=0))

    # start midi input based on music note
    for note in librosa.note_to_midi(notes):
        track.append(Message('note_on', note=int(note), velocity=64, time=0))

    # sustain the note for 4 seconds
    track.append(Message('note_off', note=int(librosa.note_to_midi(notes)[0]), velocity=64, time=4000))

    #stop midi input
    for note in librosa.note_to_midi(notes[1:]):
        track.append(Message('note_off', note=int(note), velocity=64, time=0))

    # save the midifile
    midi_path = f"dataset/midi/{filename}.mid"
    midi.save(midi_path)
    return midi_path

def convert_midi_to_wav(midi_path, wav_path, soundfont="soundfont.sf2"):
    command = ["fluidsynth", "-ni", soundfont, midi_path, "-F", wav_path, "-r", "44100"] # fluidsynth command to convert to wav 
    subprocess.run(command, check=True)

def generate_chord_dataset():
    for chord_name, inversions in CHORDS.items():
        for inversion in inversions:
            for instrument in INSTRUMENTS.keys():
                filename = f"{chord_name}_{'_'.join(inversion)}_{instrument}"
                midi_path = make_midi_file(chord_name, inversion, instrument, filename)
                wav_path = f"dataset/wav/{filename}.wav"

                convert_midi_to_wav(midi_path, wav_path)
                print(f"Generated: {wav_path}")


generate_chord_dataset();