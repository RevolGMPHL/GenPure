from tqdm import tqdm

from . import wav_create_V1_2 as wc
from . import wav_create_note_V1_2 as wc_note


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


def add_longnoteins_2_wav(blank_wav, midi, sm, md, bassornoteamp):
    # instruments are melody
    Unittime = int((sm.fm.piano_source.length * (130 / sm.bpm)) / 16)
    kongbaistart = 0  # sm.fm.piano_source.length
    zhangjie = 0
    k = 0
    zhangjie_num = md.multi_root_charpter[k]
    multi_root_charpter = md.multi_root_charpter
    strength_less = 0.99
    fd_instrument_note_list = md.fd_instrument_note_list

    for xiaojie in tqdm(range(0, len(midi)), desc="复调note进度: "):
        for yin in range(0, 8):
            start = int((xiaojie * 8 + yin) * Unittime) + kongbaistart
            next_note_distance = wc.get_next_note_distance(midi, xiaojie, yin)

            if next_note_distance == None:
                next_note_distance = 8

            # 计算当前这个音在那个章节里
            if xiaojie * 8 + yin > zhangjie_num:
                zhangjie_num += multi_root_charpter[k]
                k += 1
                zhangjie += 1

                if zhangjie < len(fd_instrument_note_list):
                    fdinstrumentnum = fd_instrument_note_list[zhangjie]  # 0<=x<=3
            if zhangjie == 0 and sm.addmelodyornot == 1:
                fdinstrumentnum = -1
            elif zhangjie == 0:
                fdinstrumentnum = md.fd_instrument_bass_list[0]

            # print('fdinstrumentnum', fdinstrumentnum)
            if fdinstrumentnum in [0]:
                Woodwinds_Albion_Hi_Long_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Woodwinds_Albion_Hi_Long_N_17_source,
                                      start, Woodwinds_Albion_Hi_Long_note_num, Unittime, next_note_distance,
                                      bassornoteamp, instrument_Amp=1.0, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=1000, NoteYanyin=Unittime * 2,
                                      BlankTiqianyin=0, )
                # Flutesbansuri_note_num = int(midi[xiaojie][yin])
                # wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Flutesbansuri_B_8_source,
                #                       start, Flutesbansuri_note_num, Unittime, next_note_distance,
                #                       bassornoteamp, instrument_Amp=2.8, strength_less=strength_less,
                #                       addDecayType='decay_long_melody', add712note2bass='no',
                #                       NoteTiqianyin=0, NoteYanyin=Unittime,
                #                       BlankTiqianyin=0, )

            if fdinstrumentnum in [1]:
                ViolinLong_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.ViolinLong_N_10_source,
                                      start, ViolinLong_note_num, Unittime, next_note_distance,
                                      bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [2]:
                Woodwinds_Albion_Hi_Long_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Woodwinds_Albion_Hi_Long_N_17_source,
                                      start, Woodwinds_Albion_Hi_Long_note_num, Unittime, next_note_distance,
                                      bassornoteamp, instrument_Amp=1.0, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=1000, NoteYanyin=Unittime * 2,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [3]:
                Z_0_AhhsomeChoir_note_num = int(midi[xiaojie][yin])
                if sm.bpm < 90:
                    wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Z_0_AhhsomeChoir_source,
                                          start, Z_0_AhhsomeChoir_note_num, Unittime, next_note_distance,
                                          bassornoteamp, instrument_Amp=1, strength_less=strength_less,
                                          addDecayType='decay_long_melody', add712note2bass='no',
                                          NoteTiqianyin=4000, NoteYanyin=Unittime * 2,
                                          BlankTiqianyin=0, )

            if fdinstrumentnum in [4]:
                Z_1_Dizi_Leg_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Z_1_Dizi_Leg_source,
                                      start, Z_1_Dizi_Leg_note_num, Unittime, next_note_distance,
                                      bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=1000, NoteYanyin=Unittime * 2,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [5]:
                Z_2_Dizi_Penz_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Z_2_Dizi_Penz_source,
                                      start, Z_2_Dizi_Penz_note_num, Unittime, next_note_distance,
                                      bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=1000, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [6]:
                Z_3_Dizi_Xiao_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Z_3_Dizi_Xiao_source,
                                      start, Z_3_Dizi_Xiao_note_num, Unittime, next_note_distance,
                                      bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=1000, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [7]:
                Z_5_NanXiao_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Z_5_NanXiao_source,
                                      start, Z_5_NanXiao_note_num, Unittime, next_note_distance,
                                      bassornoteamp, instrument_Amp=0.7, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [8]:
                Z_6_Piccolo_note_num = int(midi[xiaojie][yin])

                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Z_6_Piccolo_source,
                                      start, Z_6_Piccolo_note_num, Unittime, next_note_distance,
                                      bassornoteamp, instrument_Amp=1, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=1000, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [9]:
                A_10_Joshua_JoshuaContourVioLong_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_10_Joshua_JoshuaContourVioLong_source,
                                      start, A_10_Joshua_JoshuaContourVioLong_source_note_num, Unittime,
                                      next_note_distance,
                                      bassornoteamp, instrument_Amp=2.2, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=5000, NoteYanyin=Unittime * 2,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [10]:
                A_10_Joshua_JoshuaContourVioShort_source_note_num = int(midi[xiaojie][yin])
                # print('Unittime: ', Unittime) # bpm = 94 7000
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_10_Joshua_JoshuaContourVioShort_source,
                                      start, A_10_Joshua_JoshuaContourVioShort_source_note_num, Unittime,
                                      next_note_distance,
                                      bassornoteamp, instrument_Amp=1.6, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=2000, NoteYanyin=Unittime * 2,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [12]:
                A_10_Joshua_JoshuaLongVio_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_10_Joshua_JoshuaLongVio_source,
                                      start, A_10_Joshua_JoshuaLongVio_source_note_num, Unittime, next_note_distance,
                                      bassornoteamp, instrument_Amp=0.5, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=2000, NoteYanyin=int(Unittime * 1.5),
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [-13]:
                A_11_Nucleus_16_VioViaChord_Spiccato_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_16_VioViaChord_Spiccato_source,
                                      start, A_11_Nucleus_16_VioViaChord_Spiccato_source_note_num, Unittime,
                                      Unittime * 8,
                                      bassornoteamp, instrument_Amp=0.7, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=int(Unittime * 1.5),
                                      BlankTiqianyin=int(81415 / 8), )

            if fdinstrumentnum in [14]:
                A_11_Nucleus_17_VioViaChord_Sustained_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_17_VioViaChord_Sustained_source,
                                      start, A_11_Nucleus_17_VioViaChord_Sustained_source_note_num, Unittime,
                                      next_note_distance,
                                      bassornoteamp, instrument_Amp=0.6, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=int(81415 / 16), NoteYanyin=int(Unittime * 1.5),
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [15]:
                A_11_Nucleus_6_Brass_Full_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_6_Brass_Full_source,
                                      start, A_11_Nucleus_6_Brass_Full_source_note_num, Unittime, next_note_distance,
                                      bassornoteamp, instrument_Amp=0.7, strength_less=strength_less,
                                      addDecayType='decay_hanning', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=int(Unittime * 2),
                                      BlankTiqianyin=int(81415 / 12), )

            if fdinstrumentnum in [16]:
                A_11_Nucleus_7_Brass_Full_Staccatissimo_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_7_Brass_Full_Staccatissimo_source,
                                      start, A_11_Nucleus_7_Brass_Full_Staccatissimo_source_note_num, Unittime,
                                      next_note_distance,
                                      bassornoteamp, instrument_Amp=0.7, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=int(Unittime * 1.5),
                                      BlankTiqianyin=int(81415 / 8), )

            if fdinstrumentnum in [17]:
                A_11_Nucleus_11_Choir_Sopranos_Staccato_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_11_Choir_Sopranos_Staccato_source,
                                      start, A_11_Nucleus_11_Choir_Sopranos_Staccato_source_note_num, Unittime, 8,
                                      bassornoteamp, instrument_Amp=2.0, strength_less=1,
                                      addDecayType='decay_hanning', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=int(Unittime * 1.5),
                                      BlankTiqianyin=int(81415 / 16), )

            if fdinstrumentnum in [18]:
                A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                      sm.fm.A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source,
                                      start, A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source_note_num, Unittime,
                                      next_note_distance,
                                      bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=int(Unittime * 1.5),
                                      BlankTiqianyin=int(81415 / 16), )

            if fdinstrumentnum in [19]:
                A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                      sm.fm.A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source,
                                      start, A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source_note_num, Unittime,
                                      next_note_distance,
                                      bassornoteamp, instrument_Amp=0.5, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=int(Unittime * 1.5),
                                      BlankTiqianyin=int(81415 / 16), )


def add_longbassins_2_wav(blank_wav, midi, sm, md, bassornoteamp):
    # instruments are melody
    Unittime = int((sm.fm.piano_source.length * (130 / sm.bpm)) / 16)
    kongbaistart = 0  # sm.fm.piano_source.length
    zhangjie = 0
    k = 0
    zhangjie_num = sm.multi_root_charpter[k]
    zhangjielong = 0
    strength_less = 0.99
    for xiaojie in tqdm(range(0, len(midi)), desc="复调bass进度: "):
        for yin in range(0, 8):
            start = int((xiaojie * 8 + yin) * Unittime) + kongbaistart
            next_note_distance = wc.get_next_note_distance(midi, xiaojie, yin)

            if next_note_distance == None:
                next_note_distance = 8

            # print('next_note_distance: ', xiaojie, yin, next_note_distance)
            # 计算当前这个音在那个章节里
            if xiaojie * 8 + yin > zhangjie_num:
                zhangjie_num += sm.multi_root_charpter[k]
                k += 1
                zhangjie += 1
                zhangjielong = 1
                if zhangjie < len(sm.fd_instrument_bass_list):
                    fdinstrumentnum = sm.fd_instrument_bass_list[zhangjie]  # 0<=x<=3

            if zhangjie == 0 and sm.addmelodyornot == 1:
                fdinstrumentnum = -1
            elif zhangjie == 0:
                fdinstrumentnum = sm.fd_instrument_bass_list[0]

            if fdinstrumentnum in [0]:
                EpicPadAdnromeda_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.EpicPadAdnromeda_B_10_source,
                                      start, EpicPadAdnromeda_note_num, Unittime, next_note_distance=next_note_distance,
                                      bassornoteamp=bassornoteamp, instrument_Amp=1.8, strength_less=strength_less,
                                      addDecayType='decay', add712note2bass='yes',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [1]:
                Woodwinds_Albion_Lo_Long_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Woodwinds_Albion_Lo_Long_B_16_source,
                                      start, Woodwinds_Albion_Lo_Long_note_num, Unittime,
                                      next_note_distance=next_note_distance,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.5, strength_less=strength_less,
                                      addDecayType='decay_hanning', add712note2bass='no',
                                      NoteTiqianyin=2000, NoteYanyin=Unittime * 2,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [2]:
                Brass_Albion_Mid_Long_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.Brass_Albion_Mid_Long_B_20_source,
                                      start, Brass_Albion_Mid_Long_note_num, Unittime,
                                      next_note_distance=next_note_distance,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.7, strength_less=strength_less,
                                      addDecayType='decay_hanning', add712note2bass='no',
                                      NoteTiqianyin=4500, NoteYanyin=Unittime * 3,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [3]:
                A_11_Nucleus_1_4Trmb2Tb8Va_Sustained_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_1_4Trmb2Tb8Va_Sustained_source,
                                      start, A_11_Nucleus_1_4Trmb2Tb8Va_Sustained_source_note_num, Unittime,
                                      next_note_distance=next_note_distance,
                                      bassornoteamp=bassornoteamp, instrument_Amp=1.0, strength_less=strength_less,
                                      addDecayType='decay_hanning', add712note2bass='no',
                                      NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 2,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [4]:
                A_11_Nucleus_3_6Cello_4Bass_Sustained_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_3_6Cello_4Bass_Sustained_source,
                                      start, A_11_Nucleus_3_6Cello_4Bass_Sustained_source_note_num, Unittime,
                                      next_note_distance=next_note_distance,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.7, strength_less=strength_less,
                                      addDecayType='decay_hanning', add712note2bass='no',
                                      NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 3,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [5]:
                A_11_Nucleus_5_Bass_Sustained_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_5_Bass_Sustained_source,
                                      start, A_11_Nucleus_5_Bass_Sustained_source_note_num, Unittime,
                                      next_note_distance=next_note_distance,
                                      bassornoteamp=bassornoteamp, instrument_Amp=1.2, strength_less=strength_less,
                                      addDecayType='decay_hanning', add712note2bass='no',
                                      NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 3,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [6]:
                A_11_Nucleus_6_Brass_Full_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_6_Brass_Full_source,
                                      start, A_11_Nucleus_6_Brass_Full_source_note_num, Unittime,
                                      next_note_distance=next_note_distance,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.7, strength_less=strength_less,
                                      addDecayType='decay_hanning', add712note2bass='no',
                                      NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 3,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [7]:
                A_11_Nucleus_8_Cellos_Legato_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_8_Cellos_Legato_source,
                                      start, A_11_Nucleus_8_Cellos_Legato_source_note_num, Unittime,
                                      next_note_distance=next_note_distance,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.7, strength_less=strength_less,
                                      addDecayType='decay_hanning', add712note2bass='no',
                                      NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 3,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [8]:
                A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                      sm.fm.A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source,
                                      start, A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source_note_num, Unittime,
                                      next_note_distance=next_note_distance,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.7, strength_less=strength_less,
                                      addDecayType='decay_hanning', add712note2bass='no',
                                      NoteTiqianyin=int(81415 / 16), NoteYanyin=Unittime * 6,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [9]:
                A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                      sm.fm.A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source,
                                      start, A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source_note_num, Unittime,
                                      next_note_distance=next_note_distance,
                                      bassornoteamp=bassornoteamp, instrument_Amp=5, strength_less=strength_less,
                                      addDecayType='decay_hanning', add712note2bass='no',
                                      NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 3,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [10]:
                A_11_Nucleus_14_Low_Brass_Sustained_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_14_Low_Brass_Sustained_source,
                                      start, A_11_Nucleus_14_Low_Brass_Sustained_source_note_num, Unittime,
                                      next_note_distance=next_note_distance,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.5, strength_less=strength_less,
                                      addDecayType='decay_hanning', add712note2bass='no',
                                      NoteTiqianyin=int(81415 / 8), NoteYanyin=Unittime * 3,
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [11]:
                A_11_Nucleus_11_Choir_Sopranos_Staccato_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.A_11_Nucleus_11_Choir_Sopranos_Staccato_source,
                                      start, A_11_Nucleus_11_Choir_Sopranos_Staccato_source_note_num, Unittime,
                                      next_note_distance,
                                      bassornoteamp, instrument_Amp=3.0, strength_less=strength_less,
                                      addDecayType='decay_hanning', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=int(Unittime * 1.5),
                                      BlankTiqianyin=int(81415 / 8), )

            if fdinstrumentnum in [12]:
                A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                      sm.fm.A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source,
                                      start, A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source_note_num, Unittime,
                                      next_note_distance=next_note_distance,
                                      bassornoteamp=bassornoteamp, instrument_Amp=1.0, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=int(81415 / 8), NoteYanyin=int(Unittime * 1.5),
                                      BlankTiqianyin=0, )

            if fdinstrumentnum in [13]:
                A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source_note_num = int(midi[xiaojie][yin]) - 12
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie,
                                      sm.fm.A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source,
                                      start, A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source_note_num, Unittime,
                                      next_note_distance=next_note_distance,
                                      bassornoteamp=bassornoteamp, instrument_Amp=5, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=int(Unittime * 2),
                                      BlankTiqianyin=0, )
