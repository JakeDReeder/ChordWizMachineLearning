# This file programmatically generates musical chord data
# Made a class so that we can generate more when needed.

import os
import numpy as np
from scipy.io import wavfile
import fluidsynth
import librosa
import time

class ChordGenerator:
    def __init__(self, soundfont_path, sample_rate=44100):
        """Initialize the chord generator with a soundfont and sample rate."""
        self.sample_rate = sample_rate
        self.fs = fluidsynth.Synth() # object that is used for generating wav files
        self.fs.start()
        
        # Load soundfont (piano sound, guitar sound, etc.)
        sound_font = self.fs.sfload(soundfont_path)
        self.fs.program_select(0, sound_font, 0, 0)

    def generate_chord(self, notes, duration=4.0, velocity=100):
        """Generate audio data for a chord."""
        # Convert music notes to MIDI numbers using librosa
        midi_notes = [librosa.note_to_midi(note) for note in notes]
        
        # Calculate number of samples
        samples = int(self.sample_rate * duration)
        
        # Play notes
        for note in midi_notes:
            self.fs.noteon(0, note, velocity)
            
        # Generate audio data
        audio_data = self.fs.get_samples(samples)
        
        # Stop notes
        for note in midi_notes:
            self.fs.noteoff(0, note)
            
        # Wait a bit to let the sound decay
        time.sleep(0.1)
        
        return np.array(audio_data)

    def save_wav(self, audio_data, filename):
        """Save audio data to a WAV file."""
        # Ensure the audio data is in the correct format
        audio_data = np.array(audio_data).astype(np.float32)
        
        # Normalize the audio
        audio_data = audio_data / np.max(np.abs(audio_data))
        
        # Convert to 16-bit
        audio_data = (audio_data * 32767).astype(np.int16)
        
        # Save the file
        wavfile.write(filename, self.sample_rate, audio_data)

    def generate_chord_file(self, notes, output_path, duration=4.0, velocity=100):
        """Generate a WAV file for a chord."""
        os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)
        
        # Generate and save the chord
        audio_data = self.generate_chord(notes, duration, velocity)
        self.save_wav(audio_data, output_path)

    def __del__(self):
        """Cleanup when the object is destroyed."""
        self.fs.delete()


from ChordDictionary import MAJOR_CHORDS, MINOR_CHORDS

if __name__ == "__main__":
    
    
    SOUNDFONT_PATH = "Soundfonts/UprightPianoKW-SF2-20220221/UprightPianoKW-20220221.sf2"
    MAJOR_OUTPUT_DIR = "../data/major"
    MINOR_OUTPUT_DIR = "../data/minor"

    generator = ChordGenerator(SOUNDFONT_PATH)
    
    # Generate Major chords
    for chord_name, inversions in MAJOR_CHORDS.items():
        for i, inversion in enumerate(inversions):
            filename = f"{chord_name}_inversion_{i + 1}.wav"
            output_path = os.path.join(MAJOR_OUTPUT_DIR, filename)
            generator.generate_chord_file(inversion, output_path)
            print(f"Generated: {output_path}")

    # Generate Minor chords
    for chord_name, inversions in MINOR_CHORDS.items():
        for i, inversion in enumerate(inversions):
            filename = f"{chord_name}_inversion_{i + 1}.wav"
            output_path = os.path.join(MINOR_OUTPUT_DIR, filename)
            generator.generate_chord_file(inversion, output_path)
            print(f"Generated: {output_path}")