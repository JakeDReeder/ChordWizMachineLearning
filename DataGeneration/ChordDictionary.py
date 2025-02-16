# this is file for storing dictionaries of chords for generating

MAJOR_CHORDS = {
    'A_Major': [['A0', 'C#1', 'E1'], ['C#1', 'E1', 'A1'], ['E1', 'A1', 'C#2'], ['A1', 'C#2', 'E2'], ['C#2', 'E2', 'A2'], ['E2', 'A2', 'C#3'], ['A2', 'C#3', 'E3'], ['C#3', 'E3', 'A3'], ['E3', 'A3', 'C#4'], ['A3', 'C#4', 'E4'], ['C#4', 'E4', 'A4'], ['E4', 'A4', 'C#5'], ['A4', 'C#5', 'E5'], ['C#5', 'E5', 'A5'], ['E5', 'A5', 'C#6'], ['A5', 'C#6', 'E6'], ['C#6', 'E6', 'A6'], ['E6', 'A6', 'C#7'], ['A6', 'C#7', 'E7'], ['C#7', 'E7', 'A7']],
    'Bb_Major': [['A#0', 'D1', 'F1'], ['D1', 'F1', 'A#1'], ['F1', 'A#1', 'D2'], ['A#1', 'D2', 'F2'], ['D2', 'F2', 'A#2'], ['F2', 'A#2', 'D3'], ['A#2', 'D3', 'F3'], ['D3', 'F3', 'A#3'], ['F3', 'A#3', 'D4'], ['A#3', 'D4', 'F4'], ['D4', 'F4', 'A#4'], ['F4', 'A#4', 'D5'], ['A#4', 'D5', 'F5'], ['D5', 'F5', 'A#5'], ['F5', 'A#5', 'D6'], ['A#5', 'D6', 'F6'], ['D6', 'F6', 'A#6'], ['F6', 'A#6', 'D7'], ['A#6', 'D7', 'F7'], ['D7', 'F7', 'A#7']],
    'B_Major': [['B0', 'D#1', 'F#1'], ['D#1', 'F#1', 'B1'], ['F#1', 'B1', 'D#2'], ['B1', 'D#2', 'F#2'], ['D#2', 'F#2', 'B2'], ['F#2', 'B2', 'D#3'], ['B2', 'D#3', 'F#3'], ['D#3', 'F#3', 'B3'], ['F#3', 'B3', 'D#4'], ['B3', 'D#4', 'F#4'], ['D#4', 'F#4', 'B4'], ['F#4', 'B4', 'D#5'], ['B4', 'D#5', 'F#5'], ['D#5', 'F#5', 'B5'], ['F#5', 'B5', 'D#6'], ['B5', 'D#6', 'F#6'], ['D#6', 'F#6', 'B6'], ['F#6', 'B6', 'D#7'], ['B6', 'D#7', 'F#7'], ['D#7', 'F#7', 'B7']],
    'C#_Major': [['C#1', 'F1', 'G#1'], ['F1', 'G#1', 'C#2'], ['G#1', 'C#2', 'F2'], ['C#2', 'F2', 'G#2'], ['F2', 'G#2', 'C#3'], ['G#2', 'C#3', 'F3'], ['C#3', 'F3', 'G#3'], ['F3', 'G#3', 'C#4'], ['G#3', 'C#4', 'F4'], ['C#4', 'F4', 'G#4'], ['F4', 'G#4', 'C#5'], ['G#4', 'C#5', 'F5'], ['C#5', 'F5', 'G#5'], ['F5', 'G#5', 'C#6'], ['G#5', 'C#6', 'F6'], ['C#6', 'F6', 'G#6'], ['F6', 'G#6', 'C#7'], ['G#6', 'C#7', 'F7'], ['C#7', 'F7', 'G#7']],
    'C_Major': [['C1', 'E1', 'G1'], ['E1', 'G1', 'C2'], ['G1', 'C2', 'E2'], ['C2', 'E2', 'G2'], ['E2', 'G2', 'C3'], ['G2', 'C3', 'E3'], ['C3', 'E3', 'G3'], ['E3', 'G3', 'C4'], ['G3', 'C4', 'E4'], ['C4', 'E4', 'G4'], ['E4', 'G4', 'C5'], ['G4', 'C5', 'E5'], ['C5', 'E5', 'G5'], ['E5', 'G5', 'C6'], ['G5', 'C6', 'E6'], ['C6', 'E6', 'G6'], ['E6', 'G6', 'C7'], ['G6', 'C7', 'E7'], ['C7', 'E7', 'G7'], ['E7', 'G7', 'C8']],
    'D_Major': [['D1', 'F#1', 'A2'], ['F#1', 'A2', 'D2'], ['A2', 'D2', 'F#2'], ['D2', 'F#2', 'A3'], ['F#2', 'A3', 'D3'], ['A3', 'D3', 'F#3'], ['D3', 'F#3', 'A4'], ['F#3', 'A4', 'D4'], ['A4', 'D4', 'F#4'], ['D4', 'F#4', 'A5'], ['F#4', 'A5', 'D5'], ['A5', 'D5', 'F#5'], ['D5', 'F#5', 'A6'], ['F#5', 'A6', 'D6'], ['A6', 'D6', 'F#6'], ['D6', 'F#6', 'A7'], ['F#6', 'A7', 'D7'], ['A7', 'D7', 'F#7'], ['D7', 'F#7', 'A8']],
    'Eb_Major': [['D#1', 'G1', 'A#2'], ['G1', 'A#2', 'D#2'], ['A#2', 'D#2', 'G2'], ['D#2', 'G2', 'A#3'], ['G2', 'A#3', 'D#3'], ['A#3', 'D#3', 'G3'], ['D#3', 'G3', 'A#4'], ['G3', 'A#4', 'D#4'], ['A#4', 'D#4', 'G4'], ['D#4', 'G4', 'A#5'], ['G4', 'A#5', 'D#5'], ['A#5', 'D#5', 'G5'], ['D#5', 'G5', 'A#6'], ['G5', 'A#6', 'D#6'], ['A#6', 'D#6', 'G6'], ['D#6', 'G6', 'A#7'], ['G6', 'A#7', 'D#7'], ['A#7', 'D#7', 'G7'], ['D#7', 'G7', 'A#8']],
    'E_Major': [['E1', 'G#1', 'B2'], ['G#1', 'B2', 'E2'], ['B2', 'E2', 'G#2'], ['E2', 'G#2', 'B3'], ['G#2', 'B3', 'E3'], ['B3', 'E3', 'G#3'], ['E3', 'G#3', 'B4'], ['G#3', 'B4', 'E4'], ['B4', 'E4', 'G#4'], ['E4', 'G#4', 'B5'], ['G#4', 'B5', 'E5'], ['B5', 'E5', 'G#5'], ['E5', 'G#5', 'B6'], ['G#5', 'B6', 'E6'], ['B6', 'E6', 'G#6'], ['E6', 'G#6', 'B7'], ['G#6', 'B7', 'E7'], ['B7', 'E7', 'G#7'], ['E7', 'G#7', 'B8']],
    'F#_Major': [['F#1', 'A#2', 'C#2'], ['A#2', 'C#2', 'F#2'], ['C#2', 'F#2', 'A#3'], ['F#2', 'A#3', 'C#3'], ['A#3', 'C#3', 'F#3'], ['C#3', 'F#3', 'A#4'], ['F#3', 'A#4', 'C#4'], ['A#4', 'C#4', 'F#4'], ['C#4', 'F#4', 'A#5'], ['F#4', 'A#5', 'C#5'], ['A#5', 'C#5', 'F#5'], ['C#5', 'F#5', 'A#6'], ['F#5', 'A#6', 'C#6'], ['A#6', 'C#6', 'F#6'], ['C#6', 'F#6', 'A#7'], ['F#6', 'A#7', 'C#7'], ['A#7', 'C#7', 'F#7'], ['C#7', 'F#7', 'A#8']],
    'F_Major': [['F1', 'A2', 'C2'], ['A2', 'C2', 'F2'], ['C2', 'F2', 'A3'], ['F2', 'A3', 'C3'], ['A3', 'C3', 'F3'], ['C3', 'F3', 'A4'], ['F3', 'A4', 'C4'], ['A4', 'C4', 'F4'], ['C4', 'F4', 'A5'], ['F4', 'A5', 'C5'], ['A5', 'C5', 'F5'], ['C5', 'F5', 'A6'], ['F5', 'A6', 'C6'], ['A6', 'C6', 'F6'], ['C6', 'F6', 'A7'], ['F6', 'A7', 'C7'], ['A7', 'C7', 'F7'], ['C7', 'F7', 'A8'], ['F7', 'A8', 'C8']],
    'G#_Major': [['G#1', 'C2', 'D#2'], ['C2', 'D#2', 'G#2'], ['D#2', 'G#2', 'C3'], ['G#2', 'C3', 'D#3'], ['C3', 'D#3', 'G#3'], ['D#3', 'G#3', 'C4'], ['G#3', 'C4', 'D#4'], ['C4', 'D#4', 'G#4'], ['D#4', 'G#4', 'C5'], ['G#4', 'C5', 'D#5'], ['C5', 'D#5', 'G#5'], ['D#5', 'G#5', 'C6'], ['G#5', 'C6', 'D#6'], ['C6', 'D#6', 'G#6'], ['D#6', 'G#6', 'C7'], ['G#6', 'C7', 'D#7'], ['C7', 'D#7', 'G#7'], ['D#7', 'G#7', 'C8']],
    'G_Major': [['G1', 'B2', 'D2'], ['B2', 'D2', 'G2'], ['D2', 'G2', 'B3'], ['G2', 'B3', 'D3'], ['B3', 'D3', 'G3'], ['D3', 'G3', 'B4'], ['G3', 'B4', 'D4'], ['B4', 'D4', 'G4'], ['D4', 'G4', 'B5'], ['G4', 'B5', 'D5'], ['B5', 'D5', 'G5'], ['D5', 'G5', 'B6'], ['G5', 'B6', 'D6'], ['B6', 'D6', 'G6'], ['D6', 'G6', 'B7'], ['G6', 'B7', 'D7'], ['B7', 'D7', 'G7'], ['D7', 'G7', 'B8']]
}

MINOR_CHORDS = {
    'A_Minor': [['A0', 'C1', 'E1'], ['C1', 'E1', 'A1'], ['E1', 'A1', 'C2'], ['A1', 'C2', 'E2'], ['C2', 'E2', 'A2'], ['E2', 'A2', 'C3'], ['A2', 'C3', 'E3'], ['C3', 'E3', 'A3'], ['E3', 'A3', 'C4'], ['A3', 'C4', 'E4'], ['C4', 'E4', 'A4'], ['E4', 'A4', 'C5'], ['A4', 'C5', 'E5'], ['C5', 'E5', 'A5'], ['E5', 'A5', 'C6'], ['A5', 'C6', 'E6'], ['C6', 'E6', 'A6'], ['E6', 'A6', 'C7'], ['A6', 'C7', 'E7'], ['C7', 'E7', 'A7'], ['E7', 'A7', 'C8']],
    'Bb_Minor': [['A#0', 'C#1', 'F1'], ['C#1', 'F1', 'A#1'], ['F1', 'A#1', 'C#2'], ['A#1', 'C#2', 'F2'], ['C#2', 'F2', 'A#2'], ['F2', 'A#2', 'C#3'], ['A#2', 'C#3', 'F3'], ['C#3', 'F3', 'A#3'], ['F3', 'A#3', 'C#4'], ['A#3', 'C#4', 'F4'], ['C#4', 'F4', 'A#4'], ['F4', 'A#4', 'C#5'], ['A#4', 'C#5', 'F5'], ['C#5', 'F5', 'A#5'], ['F5', 'A#5', 'C#6'], ['A#5', 'C#6', 'F6'], ['C#6', 'F6', 'A#6'], ['F6', 'A#6', 'C#7'], ['A#6', 'C#7', 'F7'], ['C#7', 'F7', 'A#7']],
    'B_Minor': [['B0', 'D1', 'F#1'], ['D1', 'F#1', 'B1'], ['F#1', 'B1', 'D2'], ['B1', 'D2', 'F#2'], ['D2', 'F#2', 'B2'], ['F#2', 'B2', 'D3'], ['B2', 'D3', 'F#3'], ['D3', 'F#3', 'B3'], ['F#3', 'B3', 'D4'], ['B3', 'D4', 'F#4'], ['D4', 'F#4', 'B4'], ['F#4', 'B4', 'D5'], ['B4', 'D5', 'F#5'], ['D5', 'F#5', 'B5'], ['F#5', 'B5', 'D6'], ['B5', 'D6', 'F#6'], ['D6', 'F#6', 'B6'], ['F#6', 'B6', 'D7'], ['B6', 'D7', 'F#7'], ['D7', 'F#7', 'B7']],
    'C#_Minor': [['C#1', 'E1', 'G#1'], ['E1', 'G#1', 'C#2'], ['G#1', 'C#2', 'E2'], ['C#2', 'E2', 'G#2'], ['E2', 'G#2', 'C#3'], ['G#2', 'C#3', 'E3'], ['C#3', 'E3', 'G#3'], ['E3', 'G#3', 'C#4'], ['G#3', 'C#4', 'E4'], ['C#4', 'E4', 'G#4'], ['E4', 'G#4', 'C#5'], ['G#4', 'C#5', 'E5'], ['C#5', 'E5', 'G#5'], ['E5', 'G#5', 'C#6'], ['G#5', 'C#6', 'E6'], ['C#6', 'E6', 'G#6'], ['E6', 'G#6', 'C#7'], ['G#6', 'C#7', 'E7'], ['C#7', 'E7', 'G#7']],
    'C_Minor': [['C1', 'D#1', 'G1'], ['D#1', 'G1', 'C2'], ['G1', 'C2', 'D#2'], ['C2', 'D#2', 'G2'], ['D#2', 'G2', 'C3'], ['G2', 'C3', 'D#3'], ['C3', 'D#3', 'G3'], ['D#3', 'G3', 'C4'], ['G3', 'C4', 'D#4'], ['C4', 'D#4', 'G4'], ['D#4', 'G4', 'C5'], ['G4', 'C5', 'D#5'], ['C5', 'D#5', 'G5'], ['D#5', 'G5', 'C6'], ['G5', 'C6', 'D#6'], ['C6', 'D#6', 'G6'], ['D#6', 'G6', 'C7'], ['G6', 'C7', 'D#7'], ['C7', 'D#7', 'G7'], ['D#7', 'G7', 'C8']],
    'D_Minor': [['D1', 'F1', 'A2'], ['F1', 'A2', 'D2'], ['A2', 'D2', 'F2'], ['D2', 'F2', 'A3'], ['F2', 'A3', 'D3'], ['A3', 'D3', 'F3'], ['D3', 'F3', 'A4'], ['F3', 'A4', 'D4'], ['A4', 'D4', 'F4'], ['D4', 'F4', 'A5'], ['F4', 'A5', 'D5'], ['A5', 'D5', 'F5'], ['D5', 'F5', 'A6'], ['F5', 'A6', 'D6'], ['A6', 'D6', 'F6'], ['D6', 'F6', 'A7'], ['F6', 'A7', 'D7'], ['A7', 'D7', 'F7'], ['D7', 'F7', 'A8']],
    'Eb_Minor': [['D#1', 'F#1', 'A#2'], ['F#1', 'A#2', 'D#2'], ['A#2', 'D#2', 'F#2'], ['D#2', 'F#2', 'A#3'], ['F#2', 'A#3', 'D#3'], ['A#3', 'D#3', 'F#3'], ['D#3', 'F#3', 'A#4'], ['F#3', 'A#4', 'D#4'], ['A#4', 'D#4', 'F#4'], ['D#4', 'F#4', 'A#5'], ['F#4', 'A#5', 'D#5'], ['A#5', 'D#5', 'F#5'], ['D#5', 'F#5', 'A#6'], ['F#5', 'A#6', 'D#6'], ['A#6', 'D#6', 'F#6'], ['D#6', 'F#6', 'A#7'], ['F#6', 'A#7', 'D#7'], ['A#7', 'D#7', 'F#7'], ['D#7', 'F#7', 'A#8']],
    'E_Minor': [['E1', 'G1', 'B2'], ['G1', 'B2', 'E2'], ['B2', 'E2', 'G2'], ['E2', 'G2', 'B3'], ['G2', 'B3', 'E3'], ['B3', 'E3', 'G3'], ['E3', 'G3', 'B4'], ['G3', 'B4', 'E4'], ['B4', 'E4', 'G4'], ['E4', 'G4', 'B5'], ['G4', 'B5', 'E5'], ['B5', 'E5', 'G5'], ['E5', 'G5', 'B6'], ['G5', 'B6', 'E6'], ['B6', 'E6', 'G6'], ['E6', 'G6', 'B7'], ['G6', 'B7', 'E7'], ['B7', 'E7', 'G7'], ['E7', 'G7', 'B8']],
    'F#_Minor': [['F#1', 'A2', 'C#2'], ['A2', 'C#2', 'F#2'], ['C#2', 'F#2', 'A3'], ['F#2', 'A3', 'C#3'], ['A3', 'C#3', 'F#3'], ['C#3', 'F#3', 'A4'], ['F#3', 'A4', 'C#4'], ['A4', 'C#4', 'F#4'], ['C#4', 'F#4', 'A5'], ['F#4', 'A5', 'C#5'], ['A5', 'C#5', 'F#5'], ['C#5', 'F#5', 'A6'], ['F#5', 'A6', 'C#6'], ['A6', 'C#6', 'F#6'], ['C#6', 'F#6', 'A7'], ['F#6', 'A7', 'C#7'], ['A7', 'C#7', 'F#7'], ['C#7', 'F#7', 'A8']],
    'F_Minor': [['F1', 'G#1', 'C2'], ['G#1', 'C2', 'F2'], ['C2', 'F2', 'G#2'], ['F2', 'G#2', 'C3'], ['G#2', 'C3', 'F3'], ['C3', 'F3', 'G#3'], ['F3', 'G#3', 'C4'], ['G#3', 'C4', 'F4'], ['C4', 'F4', 'G#4'], ['F4', 'G#4', 'C5'], ['G#4', 'C5', 'F5'], ['C5', 'F5', 'G#5'], ['F5', 'G#5', 'C6'], ['G#5', 'C6', 'F6'], ['C6', 'F6', 'G#6'], ['F6', 'G#6', 'C7'], ['G#6', 'C7', 'F7'], ['C7', 'F7', 'G#7'], ['F7', 'G#7', 'C8']],
    'G#_Minor': [['G#1', 'B2', 'D#2'], ['B2', 'D#2', 'G#2'], ['D#2', 'G#2', 'B3'], ['G#2', 'B3', 'D#3'], ['B3', 'D#3', 'G#3'], ['D#3', 'G#3', 'B4'], ['G#3', 'B4', 'D#4'], ['B4', 'D#4', 'G#4'], ['D#4', 'G#4', 'B5'], ['G#4', 'B5', 'D#5'], ['B5', 'D#5', 'G#5'], ['D#5', 'G#5', 'B6'], ['G#5', 'B6', 'D#6'], ['B6', 'D#6', 'G#6'], ['D#6', 'G#6', 'B7'], ['G#6', 'B7', 'D#7'], ['B7', 'D#7', 'G#7'], ['D#7', 'G#7', 'B8']],
    'G_Minor': [['G1', 'A#2', 'D2'], ['A#2', 'D2', 'G2'], ['D2', 'G2', 'A#3'], ['G2', 'A#3', 'D3'], ['A#3', 'D3', 'G3'], ['D3', 'G3', 'A#4'], ['G3', 'A#4', 'D4'], ['A#4', 'D4', 'G4'], ['D4', 'G4', 'A#5'], ['G4', 'A#5', 'D5'], ['A#5', 'D5', 'G5'], ['D5', 'G5', 'A#6'], ['G5', 'A#6', 'D6'], ['A#6', 'D6', 'G6'], ['D6', 'G6', 'A#7'], ['G6', 'A#7', 'D7'], ['A#7', 'D7', 'G7'], ['D7', 'G7', 'A#8']]
}

class ChordGenerator:
    def __init__(self):
        # Define the basic chromatic scale (12 notes)
        self.CHROMATIC_SCALE = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
        
        # Create a list of all notes on a piano (A0 to C8)
        self.ALL_PIANO_NOTES = []
        for octave in range(0, 9):
            for note in self.CHROMATIC_SCALE:
                piano_note = f"{note}{octave}"
                if ((note == 'A' or note == 'A#' or note == 'B') and octave >= 0) or \
                    (octave > 0 and octave < 8) or \
                    (note <= 'C' and octave == 8):
                    self.ALL_PIANO_NOTES.append(piano_note)

    def get_next_octave_note(self, note):
        """
        Find the next occurrence of the same note in the next octave.
        Example: 'A0' -> 'A1', 'C#4' -> 'C#5'
        """
        note_name = note.rstrip('0123456789')  # Get the note without octave
        current_octave = int(note[-1])  # Get the current octave
        next_note = f"{note_name}{current_octave + 1}"
        
        if next_note in self.ALL_PIANO_NOTES:
            return next_note
        return None

    def get_chord_notes(self, root, intervals):
        """
        Get the notes of a chord based on root note and intervals.
        Example: root='A', intervals=[4, 7] -> ['A', 'C#', 'E']
        """
        root_idx = self.CHROMATIC_SCALE.index(root)
        chord_notes = [root]
        
        for interval in intervals:
            note_idx = (root_idx + interval) % 12
            chord_notes.append(self.CHROMATIC_SCALE[note_idx])
            
        return chord_notes

    def generate_chord_inversions(self, root_note, intervals):
        """
        Generate all possible inversions of a chord starting from a given root note.
        """
        # Get the basic chord notes (without octaves)
        root = root_note.rstrip('0123456789')
        chord_notes = self.get_chord_notes(root, intervals)
        
        # Find the first occurrence of each chord note on piano
        current_chord = []
        current_idx = self.ALL_PIANO_NOTES.index(root_note)
        
        # Build the first position of the chord
        for note in chord_notes:
            # Find the first available occurrence of this note
            while current_idx < len(self.ALL_PIANO_NOTES):
                current_piano_note = self.ALL_PIANO_NOTES[current_idx]
                current_note = current_piano_note.rstrip('0123456789')
                if current_note == note:
                    current_chord.append(current_piano_note)
                    break
                current_idx += 1
        
        if len(current_chord) != len(chord_notes):
            return []  # Couldn't build the complete chord
            
        # Store all inversions
        all_inversions = [current_chord]
        
        while True:
            # Create next inversion:
            # 1. Take the first note and find its next octave
            # 2. Use the rest of the notes from previous inversion
            first_note = current_chord[0]
            next_note = self.get_next_octave_note(first_note)
            
            if not next_note:  # No more octaves available for this note
                break
                
            # Create new inversion
            new_chord = current_chord[1:] + [next_note]
            
            # Check if all notes are valid
            if all(note in self.ALL_PIANO_NOTES for note in new_chord):
                all_inversions.append(new_chord)
                current_chord = new_chord
            else:
                break
                
        return all_inversions

    def create_chord_dictionary(self, chord_name, intervals):
        """
        Create a dictionary of all possible chord inversions for each root note.
        """
        chord_dict = {}
        
        for root in self.CHROMATIC_SCALE:
            chord_key = f"{root}_{chord_name}"
            
            # Find the lowest occurrence of this root note
            start_note = None
            for note in self.ALL_PIANO_NOTES:
                if note.rstrip('0123456789') == root:
                    start_note = note
                    break
            
            if start_note:
                inversions = self.generate_chord_inversions(start_note, intervals)
                if inversions:
                    chord_dict[chord_key] = inversions
                    
        return chord_dict

def print_formatted_dictionary(chord_dict, dict_name):
    """
    Print the dictionary in a format that can be copied directly into code.
    """
    print(f"{dict_name} = {{")
    
    # Get sorted keys to ensure consistent order
    sorted_keys = sorted(chord_dict.keys())
    
    # Print each chord's inversions
    for i, key in enumerate(sorted_keys):
        inversions = chord_dict[key]
        
        # Format the line
        line = f"    '{key}': {inversions}"
        
        # Add comma if not the last item
        if i < len(sorted_keys) - 1:
            line += ","
            
        print(line)
    
    print("}")

# Example usage
def main():
    generator = ChordGenerator()
    
    # Generate major chord dictionary (intervals: major third [4] and perfect fifth [7])
    major_chords = generator.create_chord_dictionary("Major", [4, 7])
    minor_chords = generator.create_chord_dictionary("Minor", [3, 7])
    
    # Print the dictionary in the requested format
    print_formatted_dictionary(major_chords, "MAJOR_CHORDS")
    print_formatted_dictionary(minor_chords, "MINOR_CHORDS")

if __name__ == "__main__":
    main()