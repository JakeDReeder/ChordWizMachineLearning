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
        self.fs = fluidsynth.Synth()
        self.fs.start()

        # Load soundfont
        sound_font = self.fs.sfload(soundfont_path)
        self.fs.program_select(0, sound_font, 0, 0)

    def generate_chord(self, notes, duration=4.0, velocity=100):
        """Generate audio data for a chord."""
        midi_notes = [librosa.note_to_midi(note) for note in notes]
        
        samples = int(self.sample_rate * duration)

        for note in midi_notes:
            self.fs.noteon(0, note, velocity)

        audio_data = self.fs.get_samples(samples)

        for note in midi_notes:
            self.fs.noteoff(0, note)

        # Convert from stereo to mono
        audio_data = np.mean(np.reshape(audio_data, (-1, 2)), axis=1)

        time.sleep(0.1)  # Let sound decay
        
        return np.array(audio_data)

    def apply_micro_tuning(self, audio_data):
        """Apply small pitch shifts (time-stretching) to simulate tuning variations."""
        factor = np.random.uniform(0.99, 1.01)        
        audio_data = audio_data.astype(np.float32)        
        return librosa.effects.time_stretch(audio_data, rate=factor)


    def apply_envelope(self, audio_data):
        """Apply volume variations over time."""
        env = np.linspace(np.random.uniform(0.4, 0.8), 1, len(audio_data))
        return audio_data * env

    def add_noise(self, audio_data):
        """Add slight background noise."""
        noise = np.random.normal(0, np.random.uniform(0.002, 0.008), audio_data.shape)
        return audio_data + noise

    def save_wav(self, audio_data, filename):
        """Save audio data to a WAV file."""
        audio_data = np.array(audio_data).astype(np.float32)
        audio_data = audio_data / np.max(np.abs(audio_data))
        audio_data = (audio_data * 32767).astype(np.int16)
        wavfile.write(filename, self.sample_rate, audio_data)

    def generate_chord_files(self, notes, output_dir, chord_name):
        """Generate multiple variations of a chord and save them as WAV files."""
        os.makedirs(output_dir, exist_ok=True)
        base_audio = self.generate_chord(notes)

        for i in range(5):  # Generate 5 variations
            modified_audio = base_audio.copy()

            if np.random.rand() < 0.7:
                modified_audio = self.apply_micro_tuning(modified_audio)
            if np.random.rand() < 0.7:
                modified_audio = self.apply_envelope(modified_audio)
            if np.random.rand() < 0.7:
                modified_audio = self.add_noise(modified_audio)

            filename = f"{chord_name}_{i}.wav"
            self.save_wav(modified_audio, os.path.join(output_dir, filename))
            print(f"Generated: {os.path.join(output_dir, filename)}")

    def __del__(self):
        self.fs.delete()


# Import chord dictionaries
from ChordDictionary import MAJOR_CHORDS, MINOR_CHORDS, DIMINISHED_CHORDS, AUGMENTED_CHORDS, SUS2_CHORDS, SUS4_CHORDS, FLAT5_CHORDS

if __name__ == "__main__":
    SOUNDFONT_PATH = "Soundfonts/UprightPianoKW-SF2-20220221/UprightPianoKW-20220221.sf2"
    MAJOR_OUTPUT_DIR = "../data/major"
    MINOR_OUTPUT_DIR = "../data/minor"
    DIMINISHED_OUTPUT_DIR = "../data/diminished"
    AUGMENTED_OUTPUT_DIR = "../data/augmented"
    SUS2_OUTPUT_DIR = "../data/suspended2nd"
    SUS4_OUTPUT_DIR = "../data/suspended4th"
    FLAT5_OUTPUT_DIR = "../data/flat5"

    generator = ChordGenerator(SOUNDFONT_PATH)

    # # Generate Major chords
    # for chord_name, inversions in MAJOR_CHORDS.items():
    #     for i, inversion in enumerate(inversions):
    #         generator.generate_chord_files(inversion, MAJOR_OUTPUT_DIR, f"{chord_name}_v{i + 1}")

    # # Generate Minor chords
    # for chord_name, inversions in MINOR_CHORDS.items():
    #     for i, inversion in enumerate(inversions):
    #         generator.generate_chord_files(inversion, MINOR_OUTPUT_DIR, f"{chord_name}_v{i + 1}")

    # # Generate Diminished chords
    # for chord_name, inversions in DIMINISHED_CHORDS.items():
    #     for i, inversion in enumerate(inversions):
    #         generator.generate_chord_files(inversion, DIMINISHED_OUTPUT_DIR, f"{chord_name}_v{i + 1}")

    # # Generate Augmented chords
    # for chord_name, inversions in AUGMENTED_CHORDS.items():
    #     for i, inversion in enumerate(inversions):
    #         generator.generate_chord_files(inversion, AUGMENTED_OUTPUT_DIR, f"{chord_name}_v{i + 1}")

    # # Generate Suspended2nd chords
    # for chord_name, inversions in SUS2_CHORDS.items():
    #     for i, inversion in enumerate(inversions):
    #         generator.generate_chord_files(inversion, SUS2_OUTPUT_DIR, f"{chord_name}_v{i + 1}")

    # # Generate Suspended4th chords
    # for chord_name, inversions in SUS4_CHORDS.items():
    #     for i, inversion in enumerate(inversions):
    #         generator.generate_chord_files(inversion, SUS4_OUTPUT_DIR, f"{chord_name}_v{i + 1}")

    # Generate Flat5 chords
    for chord_name, inversions in FLAT5_CHORDS.items():
        for i, inversion in enumerate(inversions):
            generator.generate_chord_files(inversion, FLAT5_OUTPUT_DIR, f"{chord_name}_v{i + 1}")
