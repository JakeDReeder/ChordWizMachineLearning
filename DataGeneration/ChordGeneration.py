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
        self.fs.start(driver="dsound")
        
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
        
        # convert from stereo to mono
        audio_data = np.mean(np.reshape(audio_data, (-1, 2)), axis=1)
            
        # Wait a bit to let the sound decay
        time.sleep(0.1)
        
        return np.array(audio_data)

    def apply_micro_tuning(self, audio_data):
        factor = np.random.uniform(0.99, 1.01)
        return librosa.effects.time_stretch(audio_data, factor)
    
    def apply_envelope(self, audio_data):
        env = np.linspace(0.5, 1, len(audio_data))
        return audio_data * env

    def add_noise(self, audio_data):
        noise = np.random.normal(0, 0.005, audio_data.shape)
        return audio_data + noise
    
    def save_wav(self, audio_data, filename):
        audio_data = np.array(audio_data).astype(np.float32)
        audio_data = audio_data / np.max(np.abs(audio_data))
        audio_data = (audio_data * 32767).astype(np.int16)
        wavfile.write(filename, self.sample_rate, audio_data)
    
    def generate_chord_files(self, notes, output_dir, chord_name):
        os.makedirs(output_dir, exist_ok=True)
        base_audio = self.generate_chord(notes)
        
        variants = {
            "micro_tuning": self.apply_micro_tuning(base_audio),
            "envelope_mod": self.apply_envelope(base_audio),
            "noise_addition": self.add_noise(base_audio),
            "combined": self.apply_envelope(self.add_noise(self.apply_micro_tuning(base_audio)))
        }
        
        for variant_name, audio in variants.items():
            filename = f"{chord_name}_{variant_name}.wav"
            self.save_wav(audio, os.path.join(output_dir, filename))
    
    def __del__(self):
        self.fs.delete()

from ChordDictionary import MAJOR_CHORDS, MINOR_CHORDS

if __name__ == "__main__":
    SOUNDFONT_PATH = "Soundfonts/UprightPianoKW-SF2-20220221/UprightPianoKW-20220221.sf2"
    MAJOR_OUTPUT_DIR = "../data/major"
    MINOR_OUTPUT_DIR = "../data/minor"

    generator = ChordGenerator(SOUNDFONT_PATH)
    
    for chord_name, notes in MAJOR_CHORDS.items():
        generator.generate_chord_files(notes, MAJOR_OUTPUT_DIR, chord_name)
    
    for chord_name, notes in MINOR_CHORDS.items():
        generator.generate_chord_files(notes, MINOR_OUTPUT_DIR, chord_name)
