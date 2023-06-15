# 这个是把note都加到wav上的方法
import random

from Midi2WavV1_2 import wav_create_rythmbass_V1_2 as wc_rb
from effect import decay

def get_chord_note(sm,
                   note: int):
    tonality = sm.tonality
    Cnote = (note - tonality) % 12
    if Cnote == 0:
        chordlist = [0, 4, 7, 12]
    elif Cnote == 2:
        chordlist = [0, 3, 7, 12]
    elif Cnote == 4:
        chordlist = [0, 3, 7, 12]
    elif Cnote == 5:
        chordlist = [0, 4, 7, 12]
    elif Cnote == 7:
        chordlist = [0, 4, 7, 12]
    elif Cnote == 9:
        chordlist = [0, 3, 7, 12]
    elif Cnote == 11:
        chordlist = [0, 3, 7, 12]
    else:
        chordlist = [0, 4, 7, 12]
    return chordlist
# 这个给那种长音，但是切开来能用做rythmbass的乐器
# same as short note2wav
def long_note_cut2rythm_wav(sm, md, blank_wav, source,
                            start, note_num, Unittime, yin, zhangjie, zhangjiechange,
                            bassornoteamp, instrument_Amp, strength_less,
                            add_EQornot, add712ornot, addRythmornot):
    if note_num < 100:  # 去掉空白音
        while note_num < source.minimum - 12 or note_num < 48:
            note_num += 12
        while note_num > source.maximum - 12:
            note_num -= 12

        note = source.get(note_num) * instrument_Amp * bassornoteamp * random.uniform(strength_less, 1)
        if (2 * Unittime) < len(note):
            note_short = note[:(2 * Unittime)]
        else:
            note_short = note

        # if add_EQornot:
        note_short = wc_rb.add_EQforpress(sm, note_short, Q=0.8, gain=10)
        note_short = decay.decay(note_short)
        # else:
        #     note_short = decay.decay(note_short)

        blank_wav[start: (start + len(note_short))] += note_short

        if yin == 0 and zhangjie > 0 and addRythmornot == 'yes':

            note2 = decay.decay(note[:Unittime * 2])
            if zhangjiechange == 1 or zhangjie == 1:
                bassGentype = random.randint(0, 9)
            else:
                bassGentype = 100

            if sm.bpm < 95:
                if add712ornot == 'no':
                    blank_wav = wc_rb.add_rythmbass_select(blank_wav, start, Unittime,
                                                           len(note2), note2,
                                                           note2, note2,
                                                           basstype=bassGentype,
                                                           add712=0)
                elif add712ornot == 'yes':
                    while note_num + 7 > source.maximum - 12 or note_num > source.maximum - 24:
                        note_num -= 12
                    try:
                        note7 = source.get(note_num + 7) * instrument_Amp * bassornoteamp * random.uniform(
                            strength_less,
                            1) * 0.8
                        note12 = source.get(note_num + 12) * instrument_Amp * bassornoteamp * random.uniform(
                            strength_less,
                            1) * 0.8
                        note7 = wc_rb.add_EQforpress(sm, note7, Q=0.8, gain=10)
                        note12 = wc_rb.add_EQforpress(sm, note12, Q=0.8, gain=10)
                        note7 = decay.decay(note7)
                        note12 = decay.decay(note12)
                        blank_wav = wc_rb.add_rythmbass_select(blank_wav, start, Unittime,
                                                               len(note2), note2,
                                                               note7, note12,
                                                               basstype=bassGentype,
                                                               add712=1)
                    except:
                        print('note_num', note_num)
                        print('source.maximum', source.maximum)


# 这个给短音，比如钢琴吉他
def short_note2wav(sm, md, blank_wav, source,
                   start, note_num, Unittime, yin, zhangjie, zhangjiechange,
                   bassornoteamp, instrument_Amp, strength_less, NoteTiqianyin,
                   add_EQornot, add712ornot, add34ornot, addRythmornot):
    if note_num < 100:  # 去掉空白音
        while note_num < source.minimum - 12:
            note_num += 12
        while note_num > source.maximum - 12:
            note_num -= 12

        note = source.get(note_num) * instrument_Amp * bassornoteamp * random.uniform(strength_less, 1)

        note_short = note[NoteTiqianyin:]

        # if add_EQornot:
        note_short = wc_rb.add_EQforpress(sm, note_short, Q=0.8, gain=10)
        note_short = decay.decay(note_short)
        # else:
        #     note_short = decay.decay(note_short)

        blank_wav[start: (start + len(note_short))] += note_short

        #############################################################
        #####################加上34的note###############################
        #############################################################
        if zhangjie < len(md.drumclasslist):
            if md.drumclasslist[
                zhangjie] > 0 and note_num - 12 > source.minimum - 12 and note_num + 5 < source.maximum - 12 and add34ornot == 'yes':
                notelist = get_chord_note(sm, note_num)
                notemin12 = source.get(note_num - 12) * instrument_Amp * bassornoteamp * random.uniform(strength_less,
                                                                                                        1) * 0.7
                notemin34 = source.get(note_num + notelist[1]) * instrument_Amp * bassornoteamp * random.uniform(
                    strength_less, 1) * 0.7
                notemin12_short = notemin12[NoteTiqianyin:]
                notemin34_short = notemin34[NoteTiqianyin:]
                # if add_EQornot:
                notemin12_short = wc_rb.add_EQforpress(sm, notemin12_short, Q=0.8, gain=10)
                notemin34_short = wc_rb.add_EQforpress(sm, notemin34_short, Q=0.8, gain=10)
                notemin12_short = decay.decay(notemin12_short)
                notemin34_short = decay.decay(notemin34_short)
                # else:
                #     notemin12_short = decay.decay(notemin12_short)
                #     notemin34_short = decay.decay(notemin34_short)

                blank_wav[start: (start + len(notemin12_short))] += notemin12_short
                blank_wav[start: (start + len(notemin34_short))] += notemin34_short

            if yin == 0 and zhangjie > 0 and addRythmornot == 'yes':

                note2 = decay.decay(note_short[:Unittime * 2])
                if zhangjiechange == 1 or zhangjie == 1:
                    bassGentype = random.randint(0, 9)
                else:
                    bassGentype = 100

                if sm.bpm < 95:
                    if add712ornot == 'no':
                        blank_wav = wc_rb.add_rythmbass_select(blank_wav, start, Unittime,
                                                               len(note2), note2,
                                                               note2, note2,
                                                               basstype=bassGentype,
                                                               add712=0)
                    elif add712ornot == 'yes':
                        while note_num + 24 >= source.maximum:
                            note_num -= 12
                        # print('bug ', note_num+12, source.maximum)
                        note7 = source.get(note_num + 7) * instrument_Amp * bassornoteamp * random.uniform(
                            strength_less,
                            1) * 0.8
                        note12 = source.get(note_num + 12) * instrument_Amp * bassornoteamp * random.uniform(
                            strength_less,
                            1) * 0.8
                        note7 = wc_rb.add_EQforpress(sm, note7[NoteTiqianyin:], Q=0.8, gain=10)
                        note12 = wc_rb.add_EQforpress(sm, note12[NoteTiqianyin:], Q=0.8, gain=10)
                        note7 = decay.decay(note7)
                        note12 = decay.decay(note12)
                        blank_wav = wc_rb.add_rythmbass_select(blank_wav, start, Unittime,
                                                               len(note2), note2,
                                                               note7, note12,
                                                               basstype=bassGentype,
                                                               add712=1)


# 这个给长音，比如大提琴，然后如果要一个小节，那这个next note distance就写8，或者12，有加超长度限制，超长度就不截取，整个音接上去就行
def long_note2wav(sm, md, blank_wav, zhangjie, source,
                  start, note_num, Unittime, next_note_distance,
                  bassornoteamp, instrument_Amp, strength_less,
                  addDecayType, add712note2bass,
                  NoteTiqianyin, NoteYanyin,
                  BlankTiqianyin, ):
    if note_num < 100:  # 去掉空白音
        while note_num < source.minimum - 12:
            note_num += 12
        while note_num > source.maximum - 12:
            note_num -= 12

        note = source.get(note_num) * instrument_Amp * bassornoteamp * random.uniform(strength_less, 1)
        if (next_note_distance * Unittime) + NoteYanyin < len(note):
            note_short = note[NoteTiqianyin:(next_note_distance * Unittime) + NoteYanyin]
        else:
            note_short = note
        if addDecayType == 'decay_long_melody':
            note_short = decay.decay_long_melody(note_short)
        elif addDecayType == 'decay_hanning':
            note_short = decay.decay_hanning(note_short)
        elif addDecayType == 'decay_melody':
            note_short = decay.decay_melody(note_short)
        elif addDecayType == 'decay':
            note_short = decay.decay(note_short)

        start += BlankTiqianyin
        # print('blank_wav: ', blank_wav.shape)
        blank_wav[start: (start + len(note_short))] += note_short

        if add712note2bass == 'yes':
            blank_wav = wc_rb.add712note_2bass(sm, md, blank_wav, start, note_num,
                                               source,
                                               source.maximum, zhangjie,
                                               bassornoteamp,
                                               amp712=instrument_Amp * 0.8)
