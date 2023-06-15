import numpy as np
from tqdm import tqdm

from . import wav_create_V1_2 as wc
# 返回下个音的距离是多少个Unittime
from . import wav_create_note_V1_2 as wc_note


# 相同的乐器就不要加两遍了
def same_instrument_filter(bass_or_note, instrument_list, zhangjie, frist_list, same_list):
    note_same_instrument_list = [same_list, [5, 7, 9, 11], [16, 19],
                                 frist_list]
    bass_same_instrument_list = [[0, 1, 2, 13, 14]]
    instrument_list_output = instrument_list.copy()
    if bass_or_note == 'bass':
        same_instrument_list = bass_same_instrument_list
        for i in range(len(same_instrument_list)):
            k = 0
            for j in range(len(instrument_list)):
                if instrument_list[j] in same_instrument_list[i]:
                    if k == 0:
                        k = 1
                    elif k == 1 and instrument_list[j] in instrument_list_output:
                        instrument_list_output.remove(instrument_list[j])
    elif bass_or_note == 'note':
        same_instrument_list = note_same_instrument_list

        for i in range(len(same_instrument_list)):
            k = 0
            for j in range(len(instrument_list)):
                if instrument_list[j] in same_instrument_list[i]:
                    if k == 0:
                        k = 1
                    elif k == 1 and instrument_list[j] in instrument_list_output:
                        instrument_list_output.remove(instrument_list[j])
        if zhangjie == 0:
            for j in range(len(instrument_list)):
                if instrument_list[j] in same_instrument_list[-1] and instrument_list[j] in instrument_list_output:
                    instrument_list_output.remove(instrument_list[j])

    return instrument_list_output


# 删减一些音
def notelist4longinstrument(answer, sm):
    answer4long = []
    for xiaojie in range(len(answer)):
        answer4long.append([])
        for yin in range(len(answer[xiaojie])):
            next_note_distance = wc.get_next_note_distance(answer, xiaojie, yin)
            if next_note_distance == None:
                next_note_distance = 6

            # TODO:这里得修改，第二长音旋律，也就是复调，现在的问题是，要么音太短，要么音太长，要么得按节奏选音长。这里以后得弄第二个神经网络
            if sm.bpm > 90:
                longnotelength = 3
            else:
                longnotelength = 2
            if answer[xiaojie][yin] < 100:
                # 这里来让长度太短的长音消失
                if next_note_distance >= longnotelength:
                    answer4long[xiaojie].append(
                        answer[xiaojie][yin] + 12)  # + np.random.choice([0, 7, 12], p=[ 0.5, 0.4, 0.1])
                else:
                    answer4long[xiaojie].append(120)
            else:
                answer4long[xiaojie].append(answer[xiaojie][yin])

    return answer4long


def add_note_2_wav(blank_wav, midi, instruments, sm, md, bassornoteamp, bass_or_note):
    k = 0
    zhangjie = 0
    strength_less = 0.999
    strength_press = 1
    # 第一个章节不要出现的乐器
    # frist_list = [12, 19, 22, 24, 27, 28, 29, 30, 31, 32, 33, 35, 38, 39, 40, 41, 42, 43,
    #               44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
    frist_list = []

    same_list = [0, 2, 3, 4, 9, 11, 13, 18, 46, 47]

    zhangjie_num = md.multi_root_charpter[k]
    kongbaistart = 0  # sm.fm.piano_source.length
    Unittime = int((sm.fm.piano_source.length * (130 / sm.bpm)) / 16)

    for xiaojie in tqdm(range(0, len(midi)), desc="wav拼接进度: "):
        for yin in range(0, 8):
            start = int((xiaojie * 8 + yin) * Unittime) + kongbaistart
            zhangjiechange = 0

            next_note_distance = wc.get_next_note_distance(midi, xiaojie, yin)
            if next_note_distance == None:
                next_note_distance = 8
            # print('next_note_distance: ', xiaojie, yin, next_note_distance)
            # 计算当前这个音在那个章节里
            if xiaojie * 8 + yin > zhangjie_num:
                zhangjie_num += md.multi_root_charpter[k]
                k += 1
                zhangjie += 1
                zhangjiechange = 1
            # multi_root_charpter
            if yin == 0:
                bassornoteamp += 0.15
            elif yin == 1:
                bassornoteamp -= 0.15

            if bass_or_note == 'note' and zhangjie < len(instruments):
                if xiaojie * 8 + 12 > zhangjie_num and zhangjie < len(instruments) - 1:
                    instruments[zhangjie] = instruments[zhangjie + 1]

                instrumentslist = same_instrument_filter(bass_or_note, instruments[zhangjie], zhangjie, frist_list,
                                                         same_list)

                # print('after', instrumentslist)
                for ins in range(0, len(instrumentslist)):

                    if instruments[zhangjie][ins] in same_list or (
                            instruments[zhangjie][ins] in frist_list and zhangjie == 0):
                        piano_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.piano_source,
                                               start, piano_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.7,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='yes',
                                               addRythmornot='no')

                    if instruments[zhangjie][ins] == 1:
                        Guita2_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Guita2_N_1_source,
                                               start, Guita2_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.9,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='yes',
                                               addRythmornot='no')

                    if instruments[zhangjie][ins] == 2:
                        A_12_PianoGrandeursoft_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_12_PianoGrandeursoft_source,
                                               start, A_12_PianoGrandeursoft_source_note_num, Unittime, yin,
                                               zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=2.0,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no',
                                               addRythmornot='no')

                    if instruments[zhangjie][ins] in [3]:
                        Kora_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Kora_N_3_source,
                                               start, Kora_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] == 4 and zhangjie > 0:
                        StaHighVio_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.StaHighVio_N_4_source,
                                               start, StaHighVio_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1.5,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] == 5:
                        Nyatiti_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Nyatiti_N_5_source,
                                               start, Nyatiti_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1.0,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] == 6:
                        Oud_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Oud_N_6_source,
                                               start, Oud_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.8,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] == -1:
                        MuteGuita_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.MuteGuita_N_7_source,
                                               start, MuteGuita_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1.2,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [8]:  # or instruments[zhangjie][ins] == 7:
                        MuteGuita2_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.MuteGuita2_N_8_source,
                                               start, MuteGuita2_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    #################################################################################type-ALLinstrument list##########################################################################################
                    if instruments[zhangjie][ins] in [7, 9, 11]:
                        EleGuita_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.EleGuita_source,
                                               start, EleGuita_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.6,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [-10]:
                        Guita_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Guita_source,
                                               start, Guita_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=6,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='yes',
                                               addRythmornot='no')

                    if instruments[zhangjie][ins] in [-11]:  # 11
                        Pianoshort_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Pianoshort_source,
                                               start, Pianoshort_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.6,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [-12]:  # 12
                        DeepMode_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.DeepMode_source,
                                              start, DeepMode_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=3.5, strength_less=strength_less,
                                              addDecayType='decay_melody', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=3000,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [-13]:  #
                        FluteandStrings_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.FluteandStrings_source,
                                              start, FluteandStrings_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=3.5, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=1000,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [14]:  # == 14
                        PianoGrand_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.PianoGrand_source,
                                               start, PianoGrand_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.6,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [15]:  # 15
                        PianoPopKey_note_num = int(midi[xiaojie][yin]) + 12  # 感觉这个音特别空灵，适合那种超高音
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.PianoPopKey_source,
                                               start, PianoPopKey_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=2.0,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='yes',
                                               addRythmornot='no')

                    if instruments[zhangjie][ins] in [16, 19]:
                        GenPiano_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.GenPiano_source,
                                               start, GenPiano_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=2.8,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='yes',
                                               addRythmornot='no')

                    if instruments[zhangjie][ins] in [17]:
                        Flutesbansuri_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Flutesbansuri_B_8_source,
                                              start, Flutesbansuri_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=2.8, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=6000,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [-18]:
                        FlutePersianNey_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.FlutePersianNey_B_7_source,
                                              start, FlutePersianNey_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=1, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=6000,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [19] and zhangjie > 0:  # 19:
                        ViolinLong_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.ViolinLong_N_10_source,
                                              start, ViolinLong_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=8000,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [20]:  # == 20
                        Marimba_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Marimba_N_11_source,
                                               start, Marimba_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1.0,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [21]:  # == 21
                        Xylophone_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Xylophone_N_12_source,
                                               start, Xylophone_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1.4,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [22] and zhangjie > 0:  # == 22
                        Sax_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Sax_N_13_source,
                                              start, Sax_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=2.5, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=6000,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [23] and zhangjie > 0:  # == 23
                        Ele_Heavy_Rocker_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Ele_Heavy_Rocker_N_14_source,
                                              start, Ele_Heavy_Rocker_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=0.4, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=6000,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [24] and zhangjie > 0:  # == 24
                        Ele_Higain_Breather_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Ele_Higain_Breather_N_15_source,
                                              start, Ele_Higain_Breather_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=0.4, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=6000,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [25] and zhangjie > 0:  # == 25
                        Ele_Right_in_Middle_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Ele_Right_in_Middle_N_16_source,
                                              start, Ele_Right_in_Middle_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=0.4, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=6000,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [26]:  # == 26
                        Woodwinds_Albion_Hi_Long_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Woodwinds_Albion_Hi_Long_N_17_source,
                                              start, Woodwinds_Albion_Hi_Long_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=1.2, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=1000, NoteYanyin=Unittime * 2,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [27] and zhangjie > 0:  # == 27
                        Woodwinds_Albion_Hi_Short_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Woodwinds_Albion_Hi_Short_N_18_source,
                                               start, Woodwinds_Albion_Hi_Short_note_num, Unittime, yin, zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1.6,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='no', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [-28] and zhangjie > 0:  # == 28
                        Brass_Albion_Hi_Long_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Brass_Albion_Hi_Long_N_19_source,
                                              start, Brass_Albion_Hi_Long_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=1000, NoteYanyin=Unittime,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [29] and zhangjie > 0:
                        Brass_Albion_Hi_Short_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Brass_Albion_Hi_Short_N_20_source,
                                               start, Brass_Albion_Hi_Short_note_num, Unittime, yin, zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.8,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='no', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [30] and zhangjie > 0:  # == 30
                        Z_0_AhhsomeChoir_note_num = int(midi[xiaojie][yin])
                        if sm.bpm < 90:
                            wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Z_0_AhhsomeChoir_source,
                                                  start, Z_0_AhhsomeChoir_note_num, Unittime, next_note_distance,
                                                  bassornoteamp, instrument_Amp=1, strength_less=strength_less,
                                                  addDecayType='decay_long_melody', add712note2bass='no',
                                                  NoteTiqianyin=1000, NoteYanyin=Unittime,
                                                  BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [31] and zhangjie > 0:  # == 31
                        Z_1_Dizi_Leg_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Z_1_Dizi_Leg_source,
                                              start, Z_1_Dizi_Leg_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=1000, NoteYanyin=Unittime,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [32] and zhangjie > 0:  # == 32
                        Z_2_Dizi_Penz_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Z_2_Dizi_Penz_source,
                                              start, Z_2_Dizi_Penz_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=1000, NoteYanyin=Unittime,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [33] and zhangjie > 0:  # == 33
                        Z_3_Dizi_Xiao_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Z_3_Dizi_Xiao_source,
                                              start, Z_3_Dizi_Xiao_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=1.8, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=1000, NoteYanyin=Unittime,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [34]:  # == 34
                        Z_4_Guzheng_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Z_4_Guzheng_source,
                                               start, Z_4_Guzheng_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.5,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='yes',
                                               addRythmornot='no')

                    if instruments[zhangjie][ins] in [35] and zhangjie > 0:  # == 35
                        Z_5_NanXiao_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Z_5_NanXiao_source,
                                              start, Z_5_NanXiao_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=1, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=1000, NoteYanyin=Unittime,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [-36]:  # == 36# 有个别音有问题
                        Z_6_Piccolo_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Z_6_Piccolo_source,
                                              start, Z_6_Piccolo_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=1, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=1000, NoteYanyin=Unittime,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [37]:  # == 37
                        Z_7_Zheng_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Z_7_Zheng_source,
                                               start, Z_7_Zheng_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.6,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no',
                                               addRythmornot='no')

                    if instruments[zhangjie][ins] in [38] and zhangjie > 0:  # == 38
                        N_21_ELE_DETALLED_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.N_21_ELE_DETALLED_source,
                                              start, N_21_ELE_DETALLED_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=0.4, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=4000, NoteYanyin=Unittime,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [39] and zhangjie > 0:  # == 39
                        N_22_ELE_EPICROCK_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.N_22_ELE_EPICROCK_source,
                                              start, N_22_ELE_EPICROCK_source_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=0.4, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=3000, NoteYanyin=Unittime,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [40] and zhangjie > 0:  # == 40
                        A_10_Joshua_JoshuaContourVioLong_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_10_Joshua_JoshuaContourVioLong_source,
                                              start, A_10_Joshua_JoshuaContourVioLong_source_note_num, Unittime,
                                              next_note_distance,
                                              bassornoteamp, instrument_Amp=2.2, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=5000, NoteYanyin=Unittime * 2,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [41] and zhangjie > 0:  # == 41
                        A_10_Joshua_JoshuaContourVioShort_source_note_num = int(midi[xiaojie][yin])
                        # print('Unittime: ', Unittime) # bpm = 94 7000
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_10_Joshua_JoshuaContourVioShort_source,
                                              start, A_10_Joshua_JoshuaContourVioShort_source_note_num, Unittime,
                                              next_note_distance,
                                              bassornoteamp, instrument_Amp=1.6, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=6000, NoteYanyin=Unittime * 2,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [42] and zhangjie > 0:  # == 42太尖了，刺耳
                        A_10_Joshua_JoshuaHarmonicVio_source_note_num = int(midi[xiaojie][yin]) - 12
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_10_Joshua_JoshuaHarmonicVio_source,
                                              start, A_10_Joshua_JoshuaHarmonicVio_source_note_num, Unittime,
                                              next_note_distance,
                                              bassornoteamp, instrument_Amp=0.7, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=4000, NoteYanyin=Unittime * 2,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [43] and zhangjie > 0:  # == 43
                        A_10_Joshua_JoshuaLongVio_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_10_Joshua_JoshuaLongVio_source,
                                              start, A_10_Joshua_JoshuaLongVio_source_note_num, Unittime,
                                              next_note_distance,
                                              bassornoteamp, instrument_Amp=0.7, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=2000, NoteYanyin=int(Unittime * 1.5),
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [44] and zhangjie > 0:  # == 44
                        A_10_Joshua_JoshuaSpiccato_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_10_Joshua_JoshuaSpiccato_source,
                                               start, A_10_Joshua_JoshuaSpiccato_source_note_num, Unittime, yin,
                                               zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.6,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [45] and zhangjie > 0:  # == 45
                        A_10_Joshua_JoshuaStaVio_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_10_Joshua_JoshuaStaVio_source,
                                               start, A_10_Joshua_JoshuaStaVio_source_note_num, Unittime, yin, zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.6,
                                               strength_less=strength_less,
                                               NoteTiqianyin=1000,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [46] and zhangjie > 0:  # == 46
                        A_11_Nucleus_15_VioViaChord_Pizzicato_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_15_VioViaChord_Pizzicato_source,
                                              start, A_11_Nucleus_15_VioViaChord_Pizzicato_source_note_num, Unittime,
                                              Unittime * 8,
                                              bassornoteamp, instrument_Amp=1.7, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=int(Unittime * 1.5),
                                              BlankTiqianyin=int(81415 / 8), )

                    if instruments[zhangjie][ins] in [47] and zhangjie > 0:  # == 47
                        A_11_Nucleus_16_VioViaChord_Spiccato_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_16_VioViaChord_Spiccato_source,
                                              start, A_11_Nucleus_16_VioViaChord_Spiccato_source_note_num, Unittime,
                                              Unittime * 8,
                                              bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=int(Unittime), NoteYanyin=int(Unittime * 1.5),
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [48] and zhangjie > 0:  # == 48
                        A_11_Nucleus_17_VioViaChord_Sustained_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_17_VioViaChord_Sustained_source,
                                              start, A_11_Nucleus_17_VioViaChord_Sustained_source_note_num, Unittime,
                                              next_note_distance,
                                              bassornoteamp, instrument_Amp=0.9, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=int(81415 / 12), NoteYanyin=int(Unittime * 2),
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [49] and zhangjie > 0:  # == 49
                        A_11_Nucleus_6_Brass_Full_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_6_Brass_Full_source,
                                              start, A_11_Nucleus_6_Brass_Full_source_note_num, Unittime,
                                              next_note_distance,
                                              bassornoteamp, instrument_Amp=0.7, strength_less=strength_less,
                                              addDecayType='decay_hanning', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=int(Unittime * 1.5),
                                              BlankTiqianyin=int(81415 / 8), )

                    if instruments[zhangjie][ins] in [50] and zhangjie > 0:  # == 50
                        A_11_Nucleus_7_Brass_Full_Staccatissimo_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_7_Brass_Full_Staccatissimo_source,
                                              start, A_11_Nucleus_7_Brass_Full_Staccatissimo_source_note_num, Unittime,
                                              next_note_distance,
                                              bassornoteamp, instrument_Amp=0.7, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=int(81415 / 16), NoteYanyin=int(Unittime * 1.5),
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [51] and zhangjie > 0:  # == 51
                        A_11_Nucleus_11_Choir_Sopranos_Staccato_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_11_Choir_Sopranos_Staccato_source,
                                              start, A_11_Nucleus_11_Choir_Sopranos_Staccato_source_note_num, Unittime,
                                              next_note_distance,
                                              bassornoteamp, instrument_Amp=1.0, strength_less=strength_less,
                                              addDecayType='decay_hanning', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=int(Unittime * 1.5),
                                              BlankTiqianyin=int(81415 / 16), )

                    if instruments[zhangjie][ins] in [52] and zhangjie > 0:  # == 52
                        A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source,
                                              start, A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source_note_num,
                                              Unittime,
                                              next_note_distance,
                                              bassornoteamp, instrument_Amp=1.5, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=int(Unittime * 1.5),
                                              BlankTiqianyin=int(81415 / 16), )

                    if instruments[zhangjie][ins] in [53] and zhangjie > 0:  # == 53
                        A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source,
                                              start, A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source_note_num,
                                              Unittime,
                                              next_note_distance,
                                              bassornoteamp, instrument_Amp=0.7, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=int(81415 / 16), NoteYanyin=int(Unittime * 1.5),
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [54]:  # == 54
                        A_12_PianoGrandeursoft_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_12_PianoGrandeursoft_source,
                                               start, A_12_PianoGrandeursoft_source_note_num, Unittime, yin, zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=2.0,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [55]:  # == 55
                        A_13_PianoGrandeurSoft2_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_13_PianoGrandeurSoft2_source,
                                               start, A_13_PianoGrandeurSoft2_source_note_num, Unittime, yin, zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=2.0,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [56]:  # == 56
                        A_14_PianoMaverickSoft_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_14_PianoMaverickSoft_source,
                                               start, A_14_PianoMaverickSoft_source_note_num, Unittime, yin, zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=2.0,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')
                    if instruments[zhangjie][ins] in [57]:  # == 52

                        Z_5_NanXiao_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Z_5_NanXiao_source,
                                              start, Z_5_NanXiao_note_num, Unittime, next_note_distance,
                                              bassornoteamp, instrument_Amp=1, strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=1000, NoteYanyin=Unittime,
                                              BlankTiqianyin=0, )

            if bass_or_note == 'bass' and zhangjie < len(instruments):
                # print('instruments[zhangjie]', instruments[zhangjie])
                instrumentslist = same_instrument_filter(bass_or_note, instruments[zhangjie], zhangjie, frist_list,
                                                         same_list)
                # print('instrumentslist', instrumentslist)
                for ins in range(0, len(instrumentslist)):
                    if instruments[zhangjie][ins] in [0, 2, 13, 14, 20]:
                        PianoLarge_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.PianoLarge_B_3_source,

                                               start, PianoLarge_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.18,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='yes', add34ornot='no',
                                               addRythmornot='no')

                    if instruments[zhangjie][ins] in [1]:
                        if np.random.choice([0, 1], p=[0.7, 0.3]):
                            PianoGrandeursoft_add34ornot = 'yes'
                        else:
                            PianoGrandeursoft_add34ornot = 'no'
                        A_12_PianoGrandeursoft_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_12_PianoGrandeursoft_source,
                                               start, A_12_PianoGrandeursoft_source_note_num, Unittime, yin,
                                               zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=2.0,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='yes',
                                               add34ornot=PianoGrandeursoft_add34ornot,
                                               addRythmornot='no')

                    if instruments[zhangjie][ins] != -1:
                        Bass_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Bass_B_1_source,
                                              start, Bass_note_num, Unittime, next_note_distance=12,
                                              bassornoteamp=bassornoteamp, instrument_Amp=0.03,
                                              strength_less=strength_less,
                                              addDecayType='decay', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=0,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [3]:
                        A_13_PianoGrandeurSoft2_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_13_PianoGrandeurSoft2_source,
                                               start, A_13_PianoGrandeurSoft2_source_note_num, Unittime, yin, zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=2.0,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [4]:
                        PianoLarge_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.PianoLarge_B_3_source,
                                               start, PianoLarge_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.1,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [5]:
                        StaBassVio_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.StaBassVio_B_4_source,

                                               start, StaBassVio_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1.8,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='yes', add34ornot='yes',
                                               addRythmornot='yes')

                    if instruments[zhangjie][ins] in [6]:
                        DeltaBass_note_num = int(midi[xiaojie][yin]) + 12
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.DeltaBass_B_5_source,

                                               start, DeltaBass_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.8,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='yes', add34ornot='yes',
                                               addRythmornot='yes')

                    if instruments[zhangjie][ins] in [7] and yin < 1:
                        Choir_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Choir_B_6_source,

                                              start, Choir_note_num, Unittime, next_note_distance=12,
                                              bassornoteamp=bassornoteamp, instrument_Amp=1.5,
                                              strength_less=strength_less,
                                              addDecayType='decay', add712note2bass='no',
                                              NoteTiqianyin=1000, NoteYanyin=0,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [8]:  # and xiaojie % 2 == 0:  # 结尾有问题
                        A_14_PianoMaverickSoft_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_14_PianoMaverickSoft_source,
                                               start, A_14_PianoMaverickSoft_source_note_num, Unittime, yin, zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=2.0,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [9] and (yin == 0 or yin == 4):  # and xiaojie % 2 == 0:
                        Flutesbansuri_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Flutesbansuri_B_8_source,

                                              start, Flutesbansuri_note_num, Unittime, next_note_distance=12,
                                              bassornoteamp=bassornoteamp, instrument_Amp=1,
                                              strength_less=strength_less,
                                              addDecayType='decay', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=0,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [10] and yin == 0:
                        Choir1_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Choir1_B_9_source,

                                              start, Choir1_note_num, Unittime, next_note_distance=12,
                                              bassornoteamp=bassornoteamp, instrument_Amp=2,
                                              strength_less=strength_less,
                                              addDecayType='decay', add712note2bass='yes',
                                              NoteTiqianyin=0, NoteYanyin=0,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [11] and (yin == 0 or yin == 4):
                        EpicPadAdnromeda_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.EpicPadAdnromeda_B_10_source,

                                              start, EpicPadAdnromeda_note_num, Unittime, next_note_distance=12,
                                              bassornoteamp=bassornoteamp, instrument_Amp=1.8,
                                              strength_less=strength_less,
                                              addDecayType='decay', add712note2bass='yes',
                                              NoteTiqianyin=0, NoteYanyin=0,
                                              BlankTiqianyin=0, )

                    #################################################################################type-ALLinstrument list##########################################################################################
                    if instruments[zhangjie][ins] in [12]:
                        EleGuita_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.EleGuita_source,

                                              start, EleGuita_note_num, Unittime, next_note_distance=12,
                                              bassornoteamp=bassornoteamp, instrument_Amp=0.6,
                                              strength_less=strength_less,
                                              addDecayType='decay', add712note2bass='yes',
                                              NoteTiqianyin=0, NoteYanyin=0,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [13]:
                        Guita_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Guita_source,

                                              start, Guita_note_num, Unittime, next_note_distance=12,
                                              bassornoteamp=bassornoteamp, instrument_Amp=3,
                                              strength_less=strength_less,
                                              addDecayType='decay', add712note2bass='yes',
                                              NoteTiqianyin=0, NoteYanyin=0,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [-14]:
                        Pianoshort_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Pianoshort_source,

                                               start, Pianoshort_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.6,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='yes', add34ornot='no',
                                               addRythmornot='yes')

                    if instruments[zhangjie][ins] in [15] and (yin == 0 or yin == 4):
                        DeepMode_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.DeepMode_source,

                                              start, DeepMode_note_num, Unittime, next_note_distance=12,
                                              bassornoteamp=bassornoteamp, instrument_Amp=2,
                                              strength_less=strength_less,
                                              addDecayType='decay', add712note2bass='yes',
                                              NoteTiqianyin=0, NoteYanyin=0,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [16] and (yin == 0 or yin == 4):
                        FluteandStrings_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.FluteandStrings_source,

                                              start, FluteandStrings_note_num, Unittime, next_note_distance=12,
                                              bassornoteamp=bassornoteamp, instrument_Amp=0.8,
                                              strength_less=strength_less,
                                              addDecayType='decay', add712note2bass='yes',
                                              NoteTiqianyin=0, NoteYanyin=0,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [17]:
                        PianoGrand_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.PianoGrand_source,

                                              start, PianoGrand_note_num, Unittime, next_note_distance=12,
                                              bassornoteamp=bassornoteamp, instrument_Amp=0.5,
                                              strength_less=strength_less,
                                              addDecayType='decay', add712note2bass='yes',
                                              NoteTiqianyin=0, NoteYanyin=0,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [18]:
                        PianoPopKey_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.PianoPopKey_source,

                                              start, PianoPopKey_note_num, Unittime, next_note_distance=12,
                                              bassornoteamp=bassornoteamp, instrument_Amp=0.3,
                                              strength_less=strength_less,
                                              addDecayType='decay', add712note2bass='yes',
                                              NoteTiqianyin=0, NoteYanyin=0,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [19]:
                        GenPiano_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.GenPiano_source,

                                               start, GenPiano_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.4,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='yes', add34ornot='yes',
                                               addRythmornot='yes')

                    if instruments[zhangjie][ins] in [-20] and (yin == 0 or yin == 4):
                        Violas_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Violas_source,

                                              start, Violas_note_num, Unittime, next_note_distance == 4,
                                              bassornoteamp=bassornoteamp, instrument_Amp=1.5,
                                              strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='yes',
                                              NoteTiqianyin=1000, NoteYanyin=4000,
                                              BlankTiqianyin=0, )

                        # if Violas_note_num < 100:  # 去掉空白音
                        #     while Violas_note_num < sm.fm.Violas_source.minimum - 12:
                        #         Violas_note_num += 12
                        #     while Violas_note_num > sm.fm.Violas_source.maximum - 24:
                        #         Violas_note_num -= 12
                        #     Violas_note2 = sm.fm.Violas_source.get(Violas_note_num + 12) * random.uniform(
                        #         strength_less, 1) * 1.5 * bassornoteamp
                        #     Violas_note_short2 = decay.decay_melody(Violas_note2)
                        #     blank_wav[start: (start + len(Violas_note_short2))] += Violas_note_short2

                    # 这个适合bass
                    if instruments[zhangjie][ins] in [21] and (yin == 0 or yin == 4):
                        Woodwinds_Albion_Lo_Long_note_num = int(midi[xiaojie][yin])
                        next = 4
                        if next_note_distance > 4:
                            next = next_note_distance
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Woodwinds_Albion_Lo_Long_B_16_source,
                                              start, Woodwinds_Albion_Lo_Long_note_num, Unittime,
                                              next_note_distance=next,
                                              bassornoteamp=bassornoteamp, instrument_Amp=0.5,
                                              strength_less=strength_less,
                                              addDecayType='decay_hanning', add712note2bass='no',
                                              NoteTiqianyin=2000, NoteYanyin=18000,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [22]:
                        Woodwinds_Albion_Lo_Short_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Woodwinds_Albion_Lo_Short_B_17_source,
                                               start, Woodwinds_Albion_Lo_Short_note_num, Unittime, yin, zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='yes', add712ornot='yes', add34ornot='no',
                                               addRythmornot='yes')

                    if instruments[zhangjie][ins] in [23] and zhangjie > 0:
                        Bass_Dirty_Rock_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note_cut2rythm_wav(sm, md, blank_wav, sm.fm.Bass_Dirty_Rock_B_11_source,
                                                        start, Bass_Dirty_Rock_note_num, Unittime, yin, zhangjie,
                                                        zhangjiechange,
                                                        bassornoteamp=bassornoteamp, instrument_Amp=0.1,
                                                        strength_less=strength_less,
                                                        add_EQornot='yes', add712ornot='no', addRythmornot='yes')

                    if instruments[zhangjie][ins] in [24] and zhangjie > 0:
                        Bass_Scooped_Plec_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note_cut2rythm_wav(sm, md, blank_wav, sm.fm.Bass_Scooped_Plec_B_12_source,
                                                        start, Bass_Scooped_Plec_note_num, Unittime, yin, zhangjie,
                                                        zhangjiechange,
                                                        bassornoteamp=bassornoteamp, instrument_Amp=0.1,
                                                        strength_less=strength_less,
                                                        add_EQornot='yes', add712ornot='no', addRythmornot='yes')

                    if instruments[zhangjie][ins] in [25] and zhangjie > 0:
                        Bass_Song_Three_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note_cut2rythm_wav(sm, md, blank_wav, sm.fm.Bass_Song_Three_B_13_source,
                                                        start, Bass_Song_Three_note_num, Unittime, yin, zhangjie,
                                                        zhangjiechange,
                                                        bassornoteamp=bassornoteamp, instrument_Amp=0.1,
                                                        strength_less=strength_less,
                                                        add_EQornot='yes', add712ornot='no', addRythmornot='yes')

                    if instruments[zhangjie][ins] in [26] and zhangjie > 0:
                        Bass_Vintage_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note_cut2rythm_wav(sm, md, blank_wav, sm.fm.Bass_Vintage_B_14_source,
                                                        start, Bass_Vintage_note_num, Unittime, yin, zhangjie,
                                                        zhangjiechange,
                                                        bassornoteamp=bassornoteamp, instrument_Amp=0.1,
                                                        strength_less=strength_less,
                                                        add_EQornot='yes', add712ornot='no', addRythmornot='yes')

                    if instruments[zhangjie][ins] in [27] and zhangjie > 0:
                        Bass_Wilde_Stereo_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note_cut2rythm_wav(sm, md, blank_wav, sm.fm.Bass_Wilde_Stereo_B_15_source,
                                                        start, Bass_Wilde_Stereo_note_num, Unittime, yin, zhangjie,
                                                        zhangjiechange,
                                                        bassornoteamp=bassornoteamp, instrument_Amp=0.15,
                                                        strength_less=strength_less,
                                                        add_EQornot='yes', add712ornot='no', addRythmornot='yes')

                    if instruments[zhangjie][ins] in [28] and (yin == 0) and zhangjie > 0:
                        Brass_Albion_Lo_Long_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Brass_Albion_Lo_Long_B_18_source,
                                              start, Brass_Albion_Lo_Long_note_num, Unittime, next_note_distance=8,
                                              bassornoteamp=bassornoteamp, instrument_Amp=0.7,
                                              strength_less=strength_less,
                                              addDecayType='decay_hanning', add712note2bass='no',
                                              NoteTiqianyin=2000, NoteYanyin=Unittime * 3,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [29]:
                        Brass_Albion_Lo_Short_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Brass_Albion_Lo_Short_B_19_source,
                                               start, Brass_Albion_Lo_Short_note_num, Unittime, yin, zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.5,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='no', add712ornot='no', add34ornot='no', addRythmornot='no')

                    if instruments[zhangjie][ins] in [30] and (yin == 0) and zhangjie > 0:
                        Brass_Albion_Mid_Long_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Brass_Albion_Mid_Long_B_20_source,
                                              start, Brass_Albion_Mid_Long_note_num, Unittime, next_note_distance=8,
                                              bassornoteamp=bassornoteamp, instrument_Amp=0.7,
                                              strength_less=strength_less,
                                              addDecayType='decay_hanning', add712note2bass='no',
                                              NoteTiqianyin=4500, NoteYanyin=Unittime * 3,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [31] and zhangjie > 0:
                        Brass_Albion_Mid_Short_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Brass_Albion_Mid_Short_B_21_source,
                                               start, Brass_Albion_Mid_Short_note_num, Unittime, yin, zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.5,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='no', add712ornot='no', add34ornot='no', addRythmornot='yes')

                    if instruments[zhangjie][ins] in [32] and (yin == 0) and zhangjie > 0:
                        A_11_Nucleus_1_4Trmb2Tb8Va_Sustained_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_1_4Trmb2Tb8Va_Sustained_source,
                                              start, A_11_Nucleus_1_4Trmb2Tb8Va_Sustained_source_note_num, Unittime,
                                              next_note_distance=8,
                                              bassornoteamp=bassornoteamp, instrument_Amp=1.0,
                                              strength_less=strength_less,
                                              addDecayType='decay_hanning', add712note2bass='no',
                                              NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 2,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [33] and zhangjie > 0:
                        A_11_Nucleus_2_6Cello_4Bass_Spiccato_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_11_Nucleus_2_6Cello_4Bass_Spiccato_source,
                                               start, A_11_Nucleus_2_6Cello_4Bass_Spiccato_source_note_num, Unittime,
                                               yin,
                                               zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1.0,
                                               strength_less=strength_less,
                                               NoteTiqianyin=int(81415 / 16),
                                               add_EQornot='no', add712ornot='no', add34ornot='no', addRythmornot='yes')

                    if instruments[zhangjie][ins] in [34] and (yin == 0) and zhangjie > 0:
                        A_11_Nucleus_3_6Cello_4Bass_Sustained_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_3_6Cello_4Bass_Sustained_source,
                                              start, A_11_Nucleus_3_6Cello_4Bass_Sustained_source_note_num, Unittime,
                                              next_note_distance=8,
                                              bassornoteamp=bassornoteamp, instrument_Amp=0.7,
                                              strength_less=strength_less,
                                              addDecayType='decay_hanning', add712note2bass='no',
                                              NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 3,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [35] and zhangjie > 0:
                        A_11_Nucleus_4_Bass_Spiccato_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_11_Nucleus_4_Bass_Spiccato_source,
                                               start, A_11_Nucleus_4_Bass_Spiccato_source_note_num, Unittime, yin,
                                               zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1.7,
                                               strength_less=strength_less,
                                               NoteTiqianyin=int(81415 / 16),
                                               add_EQornot='no', add712ornot='no', add34ornot='yes',
                                               addRythmornot='yes')

                    if instruments[zhangjie][ins] in [36] and (yin == 0) and zhangjie > 0:
                        A_11_Nucleus_5_Bass_Sustained_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_5_Bass_Sustained_source,
                                              start, A_11_Nucleus_5_Bass_Sustained_source_note_num, Unittime,
                                              next_note_distance=8,
                                              bassornoteamp=bassornoteamp, instrument_Amp=1.2,
                                              strength_less=strength_less,
                                              addDecayType='decay_hanning', add712note2bass='no',
                                              NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 3,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [37] and (yin == 0) and zhangjie > 0:
                        A_11_Nucleus_6_Brass_Full_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_6_Brass_Full_source,
                                              start, A_11_Nucleus_6_Brass_Full_source_note_num, Unittime,
                                              next_note_distance=8,
                                              bassornoteamp=bassornoteamp, instrument_Amp=0.7,
                                              strength_less=strength_less,
                                              addDecayType='decay_hanning', add712note2bass='no',
                                              NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 3,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [38] and zhangjie > 0:
                        A_11_Nucleus_7_Brass_Full_Staccatissimo_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_11_Nucleus_7_Brass_Full_Staccatissimo_source,
                                               start, A_11_Nucleus_7_Brass_Full_Staccatissimo_source_note_num, Unittime,
                                               yin,
                                               zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.5,
                                               strength_less=strength_less,
                                               NoteTiqianyin=int(81415 / 8),
                                               add_EQornot='no', add712ornot='no', add34ornot='no', addRythmornot='yes')

                    if instruments[zhangjie][ins] in [39] and (yin == 0) and zhangjie > 0:
                        A_11_Nucleus_8_Cellos_Legato_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_8_Cellos_Legato_source,
                                              start, A_11_Nucleus_8_Cellos_Legato_source_note_num, Unittime,
                                              next_note_distance=8,
                                              bassornoteamp=bassornoteamp, instrument_Amp=0.7,
                                              strength_less=strength_less,
                                              addDecayType='decay_hanning', add712note2bass='no',
                                              NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 3,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [40] and zhangjie > 0:
                        A_11_Nucleus_9_Cellos_Pizzicato_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_11_Nucleus_9_Cellos_Pizzicato_source,
                                               start, A_11_Nucleus_9_Cellos_Pizzicato_source_note_num, Unittime, yin,
                                               zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1.2,
                                               strength_less=strength_less,
                                               NoteTiqianyin=int(81415 / 16),
                                               add_EQornot='no', add712ornot='no', add34ornot='yes',
                                               addRythmornot='yes')

                    if instruments[zhangjie][ins] in [41] and zhangjie > 0:
                        A_11_Nucleus_10_Cellos_Spiccato_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_11_Nucleus_10_Cellos_Spiccato_source,
                                               start, A_11_Nucleus_10_Cellos_Spiccato_source_note_num, Unittime, yin,
                                               zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1.0,
                                               strength_less=strength_less,
                                               NoteTiqianyin=int(81415 / 16),
                                               add_EQornot='no', add712ornot='no', add34ornot='yes',
                                               addRythmornot='yes')

                    if instruments[zhangjie][ins] in [42] and zhangjie > 0:
                        A_11_Nucleus_11_Choir_Sopranos_Staccato_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.A_11_Nucleus_11_Choir_Sopranos_Staccato_source,
                                               start, A_11_Nucleus_11_Choir_Sopranos_Staccato_source_note_num, Unittime,
                                               yin,
                                               zhangjie, zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=1.3,
                                               strength_less=strength_less,
                                               NoteTiqianyin=int(81415 / 16),
                                               add_EQornot='no', add712ornot='no', add34ornot='no', addRythmornot='yes')

                    if instruments[zhangjie][ins] in [43] and (yin == 0) and zhangjie > 0:
                        A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source,
                                              start, A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source_note_num,
                                              Unittime,
                                              next_note_distance=8,
                                              bassornoteamp=bassornoteamp, instrument_Amp=0.7,
                                              strength_less=strength_less,
                                              addDecayType='decay_hanning', add712note2bass='no',
                                              NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 3,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [44] and (yin == 0) and zhangjie > 0:
                        A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source,
                                              start, A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source_note_num,
                                              Unittime,
                                              next_note_distance=8,
                                              bassornoteamp=bassornoteamp, instrument_Amp=5,
                                              strength_less=strength_less,
                                              addDecayType='decay_hanning', add712note2bass='no',
                                              NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 3,
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [45] and (yin == 0) and zhangjie > 0:
                        A_11_Nucleus_14_Low_Brass_Sustained_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_14_Low_Brass_Sustained_source,
                                              start, A_11_Nucleus_14_Low_Brass_Sustained_source_note_num, Unittime,
                                              next_note_distance=8,
                                              bassornoteamp=bassornoteamp, instrument_Amp=0.5,
                                              strength_less=strength_less,
                                              addDecayType='decay_hanning', add712note2bass='no',
                                              NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 3,
                                              BlankTiqianyin=0, )
                    if instruments[zhangjie][ins] in [46] and zhangjie > 0:  # == 35
                        A_11_Nucleus_11_Choir_Sopranos_Staccato_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_11_Choir_Sopranos_Staccato_source,
                                              start, A_11_Nucleus_11_Choir_Sopranos_Staccato_source_note_num, Unittime,
                                              next_note_distance,
                                              bassornoteamp, instrument_Amp=3.0, strength_less=strength_less,
                                              addDecayType='decay_hanning', add712note2bass='no',
                                              NoteTiqianyin=0, NoteYanyin=int(Unittime * 1.5),
                                              BlankTiqianyin=int(81415 / 8), )
                    if instruments[zhangjie][ins] in [47] and (yin == 0) and zhangjie > 0:  # == 35
                        A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source,
                                              start, A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source_note_num,
                                              Unittime,
                                              next_note_distance=8,
                                              bassornoteamp=bassornoteamp, instrument_Amp=1.0,
                                              strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=int(81415 / 8), NoteYanyin=int(Unittime * 1.5),
                                              BlankTiqianyin=0, )
                    if instruments[zhangjie][ins] in [48] and (yin == 0) and zhangjie > 0:  # == 35
                        A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source_note_num = int(midi[xiaojie][yin])
                        wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                              sm.fm.A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source,
                                              start, A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source_note_num,
                                              Unittime,
                                              next_note_distance=8,
                                              bassornoteamp=bassornoteamp, instrument_Amp=5,
                                              strength_less=strength_less,
                                              addDecayType='decay_long_melody', add712note2bass='no',
                                              NoteTiqianyin=int(81415 / 8), NoteYanyin=int(Unittime * 1.5),
                                              BlankTiqianyin=0, )

                    if instruments[zhangjie][ins] in [49]:
                        Guita2_N_1_source_note_num = int(midi[xiaojie][yin])
                        wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Guita2_N_1_source,

                                               start, Guita2_N_1_source_note_num, Unittime, yin,
                                               zhangjie,
                                               zhangjiechange,
                                               bassornoteamp=bassornoteamp, instrument_Amp=0.8,
                                               strength_less=strength_less,
                                               NoteTiqianyin=0,
                                               add_EQornot='no', add712ornot='no', add34ornot='no',
                                               addRythmornot='no')
