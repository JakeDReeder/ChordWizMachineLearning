# This Programatically generates MIDI files of chord sounds
# then the MIDI files will be turned into WAV files for better processing by the model

import os
import librosa
import fluidsynth
import time

# Example dictionary of chords with inversions
CHORDS = {
    "C_Major": [["C4", "E4", "G4"], ["G3", "C4", "E4"], ["E4", "G4", "C5"]],
    "D_Minor": [["D4", "F4", "A4"], ["A3", "D4", "F4"], ["F4", "A4", "D5"]],
}

# Path to your SoundFont file
SOUNDFONT_PATH = "Soundfonts/UprightPianoKW-SF2-20220221/UprightPianoKW-20220221.sf2"

# Output directories for WAV files
OUTPUT_DIR = "dataset"

def note_to_midi(note):
    """Convert a musical note ('C4') to its corresponding MIDI number."""
    return librosa.note_to_midi(note)

def generate_chord_wav(chord_name, inversion, output_path, fs):
    """Generate a WAV file for a given chord and its inversion."""
    # Convert notes to MIDI
    midi_notes = [note_to_midi(note) for note in inversion]

    # Start playing the notes
    for note in midi_notes:
        fs.noteon(0, note, 100)  # Channel 0, velocity 100

    # Play for 4 seconds (enough time for sustained notes)
    time.sleep(4)

    # Stop playing the notes
    for note in midi_notes:
        fs.noteoff(0, note)

    print(f"Generated: {output_path}")

def generate_dataset(chords, soundfont_path, output_dir):
    """Generate WAV files for all chords in the dictionary."""
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Initialize FluidSynth
    fs = fluidsynth.Synth()
    fs.start(driver="file")  # Set audio output to WAV file
    fs.sfload(soundfont_path)

    # Process each chord and its inversions
    for chord_name, inversions in chords.items():
        for i, inversion in enumerate(inversions):
            # Create a unique filename for each inversion
            filename = f"{chord_name}_inversion_{i + 1}.wav"
            output_path = os.path.join(output_dir, filename)

            # Set the output file for FluidSynth
            os.environ["AUDIOFILE"] = output_path

            # Generate the WAV file
            generate_chord_wav(chord_name, inversion, output_path, fs)

    # Clean up FluidSynth
    fs.delete()

# Call the function to generate the dataset
generate_dataset(CHORDS, SOUNDFONT_PATH, OUTPUT_DIR)