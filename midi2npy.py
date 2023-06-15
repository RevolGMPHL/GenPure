import pretty_midi
import  numpy as np
import mido
def getbpm(midiname):
    mid = mido.MidiFile(midiname)
    tempo = mid.tracks[0][0].tempo
    bpm = 6e7 / tempo
    return bpm
def get_unit025(bpm):
    unit025 = 60 / (bpm*4)
    return unit025


def midi2note(midiname, unit025):
    mididict = {'nums':[],'onsets':[],'offsets':[],'durations':[],'volumlist':[],}
    midi_data = pretty_midi.PrettyMIDI(midiname)
    for instrument in midi_data.instruments:
        for note in instrument.notes:
            mididict['nums'].append(note.pitch)
            mididict['volumlist'].append(note.velocity)
            mididict['onsets'].append(np.round(note.start / unit025) / 4)
            mididict['offsets'].append(np.round(note.end / unit025) / 4)
            mididict['durations'].append(np.round(note.end / unit025) / 4 - np.round(note.start / unit025) / 4)

    midinpystruct = [130 for i in range(256)]

    for numid, num in enumerate(mididict['nums']):
        yinid = mididict['onsets'][numid]//0.25
        midinpystruct[int(yinid)] = num
    return midinpystruct



if __name__ == '__main__':

    midiname = r'E:\project\GenPure_network\GenerData\DrumMidi\Nian/Nian01.mid'
    # midiname = r'E:\project\GenPure_network\GenerData\DrumMidi\bios/bios01.mid'

    bpm = getbpm(midiname)
    unit025 = get_unit025(bpm)
    midinpystruct = midi2note(midiname, unit025)
    multi_struct = np.array([midinpystruct, midinpystruct, midinpystruct])
    print('multi_struct: ', multi_struct)

    np.save(r'./GenerData/data/NLPdata/input_bass_test.npy', multi_struct)