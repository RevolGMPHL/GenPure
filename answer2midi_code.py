import numpy as np
from pretty_readmidi import PrettyMidi


chordclass = [[0, 4, 7, 12], [], [0, 3, 7, 12], [], [0, 3, 7, 12],
              [0, 4, 7, 12], [], [0, 4, 7, 12], [], [0, 3, 7, 12], [],
              [0, 3, 6, 12]]  # D, E, A # D=2 E=4 A=9
def yinlist2mid(yinlist, b_or_n):
    nums = []
    onsets = []
    offsets = []
    volums = []
    for xiaojie_i, xiaojie in enumerate(yinlist):
        for yin_i, yin in enumerate(xiaojie):
            if yin < 100 and yin >0:
                nums.append(int(yin)+12*np.random.randint(1, 2))
                onsets.append( (xiaojie_i*8+yin_i)/4 )
                if b_or_n == 'n':
                    volums.append(np.random.randint(50, 70))
                else:
                    volums.append(np.random.randint(30, 50))
    for onset_i, onset in enumerate(onsets):
        if onset_i <= len(onsets)-2:
            offsets.append(onsets[onset_i+1])
            # offsets.append(onsets[onset_i]+1)
        else:
            offsets.append(onsets[-1] + 2)
    return nums, onsets, offsets, volums

def appendchord(tonality, yin, onset, offset, nums, onsets, offsets, volums, b_or_n):
    appendnum = np.random.choice([0, 1, 2, 3, 4], p=[0.7, 0.3, 0.00, 0.00, 0.0])
    yinchord = []
    while len(yinchord) < appendnum and len(chordclass[(int(yin)-int(tonality))%12])!=0:
        num = chordclass[(int(yin)-int(tonality))%12][np.random.randint(0, 3)]
        if num not in yinchord:
            yinchord.append(num)

    for yinc in yinchord:
        nums.append(yinc + yin)
        onsets.append(onset)
        offsets.append(offset)
        if b_or_n=='n':
            volums.append(np.random.randint(60, 80))
        else:
            volums.append(np.random.randint(30, 50))

def answer2midi(tonality, answers, music_bass, sm):

    chord_nums = []
    chord_onsets = []
    chord_offsets = []
    chord_volums = []



    chord_bass_nums = []
    chord_bass_onsets = []
    chord_bass_offsets = []
    chord_bass_volums = []

    pret = PrettyMidi()
    nums, onsets, offsets, volums = yinlist2mid(answers, 'n')

    # print('nums1: ', np.array(nums).shape)
    # b, a = signal.butter(6, 0.4, 'low')
    # nums = list(np.round(signal.filtfilt(b, a, nums)))
    mean = np.mean(nums)
    print('mean: ', mean)
    for id, x in enumerate(nums):
        if x < mean-16:
            nums[id] = x+12
        elif x > mean+12:
            nums[id] = x - 12
    nums = [int(x) for x in nums]


    for id, (num, onset, offset) in enumerate(zip(nums, onsets, offsets)):
        appendchord(tonality, num, onset, offset, chord_nums, chord_onsets, chord_offsets, chord_volums, 'n')

    # append chord
    bass_nums, bass_onsets, bass_offsets, bass_volums = yinlist2mid(np.array(music_bass)[:,:8], 'b')

    # append chord
    # for id, (num, onset, offset) in enumerate(zip(bass_nums, bass_onsets, bass_offsets)):
    #     appendchord(tonality, num, onset, offset, chord_bass_nums, chord_bass_onsets, chord_bass_offsets, chord_bass_volums, 'b')


    nums += chord_nums
    onsets += chord_onsets
    offsets += chord_offsets
    volums += chord_volums
    melomidi_name =  sm.fm.wav_music_output_name['1'][:-6] + '_melo.mid'
    pret.write_created_midi(nums, volums, onsets, offsets, melomidi_name)

    bass_nums +=  chord_bass_nums
    bass_volums +=  chord_bass_volums
    bass_onsets +=  chord_bass_onsets
    bass_offsets +=  chord_bass_offsets

    bassmidi_name =  sm.fm.wav_music_output_name['1'][:-6] + '_bass.mid'
    pret.write_created_midi(bass_nums, bass_volums, bass_onsets, bass_offsets, bassmidi_name)