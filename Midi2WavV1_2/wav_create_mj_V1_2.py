from tqdm import tqdm

from Midi2WavV1_2 import wav_create_note_V1_2 as wc_note


def add_mj_ins_2_wav(blank_wav, midi, sm, md, bassornoteamp):
    # instruments are melody
    Unittime = int((sm.fm.piano_source.length * (130 / sm.bpm)) / 16)
    kongbaistart = 0  # sm.fm.piano_source.length
    zhangjie = 0
    k = 0
    zhangjie_num = md.multi_root_charpter[k]
    multi_root_charpter = md.multi_root_charpter
    strength_less = 0.99

    for xiaojie in tqdm(range(0, len(midi)), desc="模进进度: "):
        for yin in range(0, 8):
            start = int((xiaojie * 8 + yin) * Unittime) + kongbaistart
            # next_note_distance = wc.get_next_note_distance(midi, xiaojie, yin)
            # print('long next_note_distance: ', next_note_distance)
            zhangjiechange = 0
            # if next_note_distance == None:
            #    next_note_distance = 8
            # print('next_note_distance: ', xiaojie, yin, next_note_distance)

            # 计算当前这个音在那个章节里
            if xiaojie * 8 + yin > zhangjie_num:
                zhangjie_num += multi_root_charpter[k]
                k += 1
                zhangjie += 1
                zhangjiechange = 1
                if zhangjie < len(md.mj_instrument_note_list):
                    mjinstrumentnum = md.mj_instrument_note_list[zhangjie]  # 0<=x<=3
            if zhangjie == 0 and sm.addmelodyornot == 1:
                mjinstrumentnum = -1
            elif zhangjie == 0:
                mjinstrumentnum = md.mj_instrument_note_list[0]

            if mjinstrumentnum in [0] and zhangjie < len(multi_root_charpter) - 1:
                piano_note_num = int(midi[xiaojie][yin])
                wc_note.short_note2wav(sm, md, blank_wav, sm.fm.piano_source,
                                       start, piano_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                       bassornoteamp=bassornoteamp, instrument_Amp=0.7,
                                       strength_less=strength_less,
                                       NoteTiqianyin=0,
                                       add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

            if mjinstrumentnum in [1]:
                Guita2_note_num = int(midi[xiaojie][yin])
                wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Guita2_N_1_source,
                                       start, Guita2_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                       bassornoteamp=bassornoteamp, instrument_Amp=0.9, strength_less=strength_less,
                                       NoteTiqianyin=0,
                                       add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

            if mjinstrumentnum in [2]:
                StaHighVio_note_num = int(midi[xiaojie][yin])
                wc_note.short_note2wav(sm, md, blank_wav, sm.fm.StaHighVio_N_4_source,
                                       start, StaHighVio_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                       bassornoteamp=bassornoteamp, instrument_Amp=1.5, strength_less=strength_less,
                                       NoteTiqianyin=0,
                                       add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

            if mjinstrumentnum in [3]:
                EleGuita_note_num = int(midi[xiaojie][yin])
                wc_note.short_note2wav(sm, md, blank_wav, sm.fm.EleGuita_source,
                                       start, EleGuita_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                       bassornoteamp=bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                       NoteTiqianyin=0,
                                       add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

            if mjinstrumentnum in [4]:
                Guita_note_num = int(midi[xiaojie][yin])
                wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Guita_source,
                                       start, Guita_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                       bassornoteamp=bassornoteamp, instrument_Amp=6, strength_less=strength_less,
                                       NoteTiqianyin=0,
                                       add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

            if mjinstrumentnum in [5]:
                GenPiano_note_num = int(midi[xiaojie][yin])
                wc_note.short_note2wav(sm, md, blank_wav, sm.fm.GenPiano_source,
                                       start, GenPiano_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                       bassornoteamp=bassornoteamp, instrument_Amp=2.8, strength_less=strength_less,
                                       NoteTiqianyin=0,
                                       add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

            if mjinstrumentnum in [6]:
                Marimba_note_num = int(midi[xiaojie][yin])
                wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Marimba_N_11_source,
                                       start, Marimba_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                       bassornoteamp=bassornoteamp, instrument_Amp=1.0, strength_less=strength_less,
                                       NoteTiqianyin=0,
                                       add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

            if mjinstrumentnum in [7]:
                Xylophone_note_num = int(midi[xiaojie][yin])
                wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Xylophone_N_12_source,
                                       start, Xylophone_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                       bassornoteamp=bassornoteamp, instrument_Amp=1.4, strength_less=strength_less,
                                       NoteTiqianyin=0,
                                       add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

            if mjinstrumentnum in [8]:
                Woodwinds_Albion_Hi_Short_note_num = int(midi[xiaojie][yin])
                wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Woodwinds_Albion_Hi_Short_N_18_source,
                                       start, Woodwinds_Albion_Hi_Short_note_num, Unittime, yin, zhangjie,
                                       zhangjiechange,
                                       bassornoteamp=bassornoteamp, instrument_Amp=1.6, strength_less=strength_less,
                                       NoteTiqianyin=0,
                                       add_EQornot='no', add712ornot='no', add34ornot='no', addRythmornot='no')

            if mjinstrumentnum in [9]:  # 没问题
                Z_4_Guzheng_note_num = int(midi[xiaojie][yin])
                wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Z_4_Guzheng_source,
                                       start, Z_4_Guzheng_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                       bassornoteamp=bassornoteamp, instrument_Amp=0.5, strength_less=strength_less,
                                       NoteTiqianyin=0,
                                       add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')

            if mjinstrumentnum in [10]:
                Z_7_Zheng_note_num = int(midi[xiaojie][yin])
                wc_note.short_note2wav(sm, md, blank_wav, sm.fm.Z_7_Zheng_source,
                                       start, Z_7_Zheng_note_num, Unittime, yin, zhangjie, zhangjiechange,
                                       bassornoteamp=bassornoteamp, instrument_Amp=0.6, strength_less=strength_less,
                                       NoteTiqianyin=0,
                                       add_EQornot='yes', add712ornot='no', add34ornot='no', addRythmornot='no')
