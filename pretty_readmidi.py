import pretty_midi
import  numpy as np
class PrettyMidi:
    def __init__(self):
        self.names = []
        self.nums = []

        self.onsets = []
        self.offsets = []

        self.times = []
        self.durations = []
        self.volumlist = []

    def get_notes(self, midi_file_name):
        # Load MIDI file into PrettyMIDI object
        midi_data = pretty_midi.PrettyMIDI(midi_file_name)
        self.bpm = midi_data.estimate_tempo()
        # print('bpm: ', self.bpm)

        # total_velocity = sum(sum(midi_data.get_chroma()))
        # print([sum(semitone) / total_velocity for semitone in midi_data.get_chroma()])
        unit025 = 60 / (120*4)# self.bpm
        # print('0.25 = ', 60 / (130*4))
        for instrument in midi_data.instruments:
            for note in instrument.notes:
                # print('note read: ', note)
                self.nums.append(note.pitch)
                self.volumlist.append(note.velocity)
                self.onsets.append(np.round(note.start/unit025)/4)
                self.offsets.append(np.round(note.end/unit025)/4)
                self.durations.append(np.round(note.end/unit025)/4 - np.round(note.start/unit025)/4)

        # print('nums: ', self.nums)
        # print('onsets: ', self.onsets)
        # print('durations: ', self.durations)

    def write_this_midi(self, midi_file_name):
        unit025 = 60 / (120 * 4)
        cello_c_chord = pretty_midi.PrettyMIDI()
        cello_program = pretty_midi.instrument_name_to_program('Cello')
        cello = pretty_midi.Instrument(program=cello_program)
        for notenum, volum, onset, offset in zip(self.nums, self.volumlist, self.onsets, self.offsets):
            note = pretty_midi.Note(velocity=volum, pitch=notenum, start=onset*4*unit025, end=offset*4*unit025)
            # print('note: ', note)
            cello.notes.append(note)
        cello_c_chord.instruments.append(cello)
        cello_c_chord.write(midi_file_name)

    def write_created_midi(self, nums, volumlist, onsets, offsets, midi_file_name):
        unit025 = 60 / (120 * 4)
        cello_c_chord = pretty_midi.PrettyMIDI()
        cello_program = pretty_midi.instrument_name_to_program('Cello')
        cello = pretty_midi.Instrument(program=cello_program)
        for notenum, volum, onset, offset in zip(nums, volumlist, onsets, offsets):
            note = pretty_midi.Note(velocity=volum, pitch=notenum, start=onset*4*unit025, end=offset*4*unit025)
            # print('note: ', note)
            cello.notes.append(note)
        cello_c_chord.instruments.append(cello)
        cello_c_chord.write(midi_file_name)

    def list2midi(self, melolist, durations=None, midi_file_name = 'test_bass.mid'):

        nums, volumlist, onsets, offsets=[], [], [], []
        for idyin, yin in enumerate(melolist):
            if yin<100:
                if yin < 60+7:
                    nums.append(int(yin) + 24)
                else:
                    nums.append(int(yin) + 12)
                volumlist.append(np.random.randint(50, 80))
                onsets.append(idyin*0.25)
                offsets.append(idyin*0.25+1)
        # print('nums: ', nums)
        # print('onsets: ', onsets)
        # print('offsets: ', offsets)
        # print('durations: ', durations)

        self.write_created_midi(nums, volumlist, onsets, offsets, midi_file_name)
if __name__ == '__main__':
    pret = PrettyMidi()
    pret.get_notes(r'E:\project\GenPure_network\GenerData\DrumMidi\Nian/Nian01.mid')
    print('nums: ', pret.nums)
    print('onsets: ', pret.onsets)
    # print('offsets: ', pret.offsets)
    # print('durations: ', pret.durations)
    # pret.write_this_midi('test0.mid')



    # testmelo = [24, 130, 130, 130, 130, 130, 130, 130,  24, 130, 130, 130,  28, 130,
    #     130, 130,  24, 130, 130, 130, 130, 130, 130, 130,  24, 130, 130, 130,
    #      28, 130, 130, 130,  31, 130, 130, 130, 130, 130, 130, 130,  31, 130,
    #     130, 130,  35, 130, 130, 130,  31, 130, 130, 130, 130, 130, 130, 130,
    #      31, 130, 130, 130,  31, 130, 130, 130,  12, 130, 130, 130, 130, 130,
    #     130, 130,  16, 130, 130, 130,  19, 130, 130, 130,  12, 130, 130, 130,
    #     130, 130, 130, 130,  16, 130, 130, 130,  19, 130, 130, 130,  19, 130,
    #     130, 130, 130, 130, 130, 130,  23, 130, 130, 130,  26, 130, 130, 130,
    #      19, 130, 130, 130, 130, 130, 130, 130,  23, 130, 130, 130,  23, 130,
    #     130, 130,  12, 130, 130, 130, 130, 130,  19, 130, 130, 130,  28, 130,
    #      36, 130, 130, 130,  12, 130, 130, 130, 130, 130,  19, 130, 130, 130,
    #      28, 130,  36, 130, 130, 130,  19, 130, 130, 130, 130, 130,  26, 130,
    #     130, 130,  35, 130,  43, 130, 130, 130,  19, 130, 130, 130, 130, 130,
    #      26, 130, 130, 130,  19, 130,  23, 130, 130, 130,  12, 130, 130, 130,
    #     130, 130,  19, 130, 130, 130,  24, 130,  31, 130, 130, 130,  12, 130,
    #     130, 130, 130, 130,  19, 130, 130, 130,  24, 130,  31, 130, 130, 130,
    #      19, 130, 130, 130, 130, 130,  26, 130, 130, 130,  31, 130,  38, 130,
    #     130, 130,  19, 130, 130, 130, 130, 130,  23, 130, 130, 130,  26, 130,
    #      26, 130, 130, 130]
    #
    # pret.list2midi(testmelo)





