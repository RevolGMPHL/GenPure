import random
from typing import Tuple, Union

import numpy as np
import scipy.signal as signal
from music21 import instrument, note, stream
from tqdm import tqdm

from GenerData.ABAC_model import ABAC_model, ABAC_model_simple
from GenerData.MusicDetailManager import MusicDetailManager
from GenerData.SettingManager import SettingsManager
from GenerData.note_name_and_num import note_num_2_name
from GenerData.read_midi import Midi
from GenerData.bassclass import bass_class

def get_chord_note(sm: SettingsManager,
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


def get_median(dataraw):
    clean_data = [i for i in dataraw if i < 100]
    return np.median(clean_data)


def mj(midi, sm, md):
    k = 0
    zhangjie = 0
    zhangjie_num = md.multi_root_charpter[k]
    multi_root_charpter = md.multi_root_charpter
    multi_root = md.multi_root
    bassclass = bass_class

    root1 = sm.root
    root2 = sm.root2
    root3 = sm.root3
    midi2 = midi.copy()

    for xiaojie in range(0, len(midi)):
        for yin in range(0, 8):
            # 计算当前这个音在那个章节里
            if xiaojie * 8 + yin >= zhangjie_num:
                zhangjie_num += multi_root_charpter[k]
                k += 1
                zhangjie += 1
                midi4copy = []
                midi4copy2 = []
                midi4copy3 = []
                if zhangjie < len(multi_root) - 1:
                    root = multi_root[zhangjie]

                    if root == root1 and len(midi4copy) == 0:
                        midi4copy.append(midi[xiaojie + 1])
                        midi4copy.append(midi[xiaojie + 2])
                    if root == root2 and len(midi4copy2) == 0:
                        midi4copy2.append(midi[xiaojie + 1])
                        midi4copy2.append(midi[xiaojie + 2])
                    if root == root3 and len(midi4copy3) == 0:
                        midi4copy3.append(midi[xiaojie + 1])
                        midi4copy3.append(midi[xiaojie + 2])
                    for i in range(len(bassclass[root]) - 1):
                        if root == root1:
                            midi2[xiaojie + i * 2] = midi4copy[0]
                            midi2[xiaojie + 1 + i * 2] = midi4copy[1]
                        elif root == root2:
                            midi2[xiaojie + i * 2] = midi4copy2[0]
                            midi2[xiaojie + 1 + i * 2] = midi4copy2[1]
                        elif root == root3:
                            midi2[xiaojie + i * 2] = midi4copy3[0]
                            midi2[xiaojie + 1 + i * 2] = midi4copy3[1]
    return midi2


def write_midi(revised_melody, filename):
    note_list = []
    for i in range(0, len(revised_melody.names)):
        new_noteNote = note.Note(revised_melody.names[i])
        new_noteNote.offset = revised_melody.offsets[i]
        new_noteNote.storedInstrument = instrument.Piano()

        note_list.append(new_noteNote)

    mini_stream = stream.Stream(note_list)
    mini_stream.write('midi', fp=filename)
    # return filename


def revise_two_melody4sing(midi1: Union[list, int],
                           midi2: Union[list, int],
                           sm: SettingsManager, md: MusicDetailManager,
                           sing: int = 0) -> Tuple[Union[list, int], list]:
    hexie_list = [
        [0, 4, 7], [], [0, 3, 7], [], [0, 3, 7], [0, 4, 7], [],
        [0, 4, 7], [], [0, 3, 7], [], [0, 3, 7], [0, 4, 7]
    ]
    out_tonality = [1, 3, 6, 8, 10]

    out_tonality_find_dict = {
        '01': -1, '03': 1, '06': 1, '08': -1, '010': -1,

        '21': 1, '23': -1, '26': -1, '28': 1, '210': -1,

        '41': -1, '43': 1, '46': 1, '48': -1, '410': 1,

        '51': 1, '53': -1, '56': -1, '58': 1, '510': -1,

        '71': -1, '73': 1, '76': 1, '78': -1, '710': 1,

        '91': 1, '93': 1, '96': -1, '98': 1, '910': -1,

        '111': 1, '113': -1, '116': 1, '118': -1, '1110': 1,

    }

    # 先处理一遍离调音
    for i in range(0, len(midi2)):
        for j in range(0, len(midi2[i])):
            if midi2[i][j] < 100:
                rnote = int((midi2[i][j] - sm.tonality) % 12)
                rbass = int((midi1[i][j] - sm.tonality) % 12)
                if rnote in out_tonality:
                    midi2[i][j] += out_tonality_find_dict[str(rbass) + str(rnote)]


def revise_two_melody(midi1: Union[list, int],
                      midi2: Union[list, int],
                      sm: SettingsManager, md: MusicDetailManager,
                      sing: int = 0) -> Tuple[Union[list, int], list]:


    hexie_list = [
        [0, 4, 7], [], [0, 3, 7], [], [0, 3, 7], [0, 4, 7], [],
        [0, 4, 7], [], [0, 3, 7], [], [0, 3, 7], [0, 4, 7]
    ]
    out_tonality = [1, 3, 6, 8, 10]

    # 先处理一遍离调音
    for i in range(0, len(midi2)):
        for j in range(0, len(midi2[i])):
            if midi2[i][j] < 100:
                rnote = int((midi2[i][j] - sm.tonality) % 12)
                while rnote in out_tonality:
                    midi2[i][j] += 1
                    rnote = int((midi2[i][j] - sm.tonality) % 12)

    for i in (range(0, len(midi2))):

        for j in range(0, len(midi2[i])):
            if midi1[i][j] < 100 and midi2[i][j] < 100:
                rbass = int((midi1[i][j] - sm.tonality) % 12)
                rnote = int((midi2[i][j] - sm.tonality) % 12)

                while rnote in out_tonality or abs(midi2[i][j] % 12 - midi1[i][j] % 12) not in hexie_list[rbass]:
                    if rnote in out_tonality:
                        midi2[i][j] += 1
                        rnote = int((midi2[i][j] - sm.tonality) % 12)
                        if midi2[i][j] > 130:
                            break
                    else:
                        midi2[i][j] += 1
                        rnote = int((midi2[i][j] - sm.tonality) % 12)
                        if midi2[i][j] > 130:
                            break

                while abs(midi2[i][j] % 12 - midi1[i][j] % 12) not in hexie_list[rbass]:
                    midi2[i][j] += 1
                    if midi2[i][j] > 130:
                        midi2[i][j] = 130
                        break

                if midi2[i][j] == midi1[i][j]:
                    midi2[i][j] += 7 + random.randint(0, 1) * 5
    if sing == 1:
        for i in tqdm(range(0, len(midi2)), desc="revise_two_melody 3"):
            for j in range(0, len(midi2[i])):
                while midi2[i][j] > 74:
                    midi2[i][j] -= 12
                while midi2[i][j] < 60:
                    midi2[i][j] += 12

    return midi1, midi2


def deal_F_note(answer_logits: list, sm: SettingsManager, md: MusicDetailManager):
    for xiaojie in range(0, len(answer_logits) - 1):
        for yin in range(0, 8):
            if answer_logits[xiaojie][0] < 100:
                yin = (answer_logits[0][0] - sm.tonality) % 12
            pass


def add_start_melody(answer_logits: list,
                     sm: SettingsManager, md: MusicDetailManager, xianjierandom: int) -> list:
    startlist = [130, 130, 130, 130, 130, 130, 130, 130]
    jiangelist = [0, 2, 4, 5, 7, 9, 11]
    if answer_logits[0][0] < 100:
        yin = (answer_logits[0][0] - sm.tonality) % 12
        yin_num = jiangelist.index(yin)
        baseyin = jiangelist[yin_num]
        juli1 = jiangelist[yin_num] - jiangelist[yin_num - 1]
        juli2 = jiangelist[yin_num] - jiangelist[yin_num - 2]
        juli3 = jiangelist[yin_num] - jiangelist[yin_num - 3]
        juli4 = jiangelist[yin_num] - jiangelist[yin_num - 4]
        while juli1 < 0:
            juli1 += 12
        while juli2 < 0:
            juli2 += 12
        while juli3 < 0:
            juli3 += 12
        while juli4 < 0:
            juli4 += 12

    if answer_logits[0][0] < 100:
        if xianjierandom == 0:
            startlist[-1] = 130
            startlist[-2] = answer_logits[0][0] - juli1
            startlist[-3] = 130
            startlist[-4] = answer_logits[0][0] - juli2

        elif xianjierandom == 1:
            startlist[-1] = 130
            startlist[-2] = answer_logits[0][0] - 5
            startlist[-3] = 130
            startlist[-4] = answer_logits[0][0] - 12
            startlist[-5] = 130
            startlist[-6] = 130
            startlist[-7] = 130
            startlist[-8] = answer_logits[0][0] - 17

        elif xianjierandom == 2:
            startlist[-1] = 130
            startlist[-2] = answer_logits[0][0] - 5
            startlist[-3] = 130
            startlist[-4] = answer_logits[0][0] - 12
            startlist[-5] = 130
            startlist[-6] = answer_logits[0][0] - 17

        elif xianjierandom == 3:
            startlist[-1] = 130
            startlist[-2] = answer_logits[0][0] - juli1
            startlist[-3] = 130
            startlist[-4] = answer_logits[0][0] - juli2
            startlist[-5] = 130
            startlist[-6] = answer_logits[0][0] - juli3
            startlist[-7] = 130
            startlist[-8] = answer_logits[0][0] - juli4

        elif xianjierandom == 4:
            startlist[-1] = 130
            startlist[-2] = answer_logits[0][0] - juli1
            startlist[-3] = 130
            startlist[-4] = answer_logits[0][0] - juli2
            startlist[-5] = 130
            startlist[-6] = answer_logits[0][0] - juli3
            startlist[-7] = 130
            startlist[-8] = 130

        elif xianjierandom == 5:
            startlist[-1] = 130
            startlist[-2] = answer_logits[0][0] - juli1
            startlist[-3] = 130
            startlist[-4] = answer_logits[0][0] - juli2
            startlist[-5] = 130
            startlist[-6] = 130
            startlist[-7] = 130
            startlist[-8] = answer_logits[0][0] - juli3

        elif xianjierandom == 6:
            startlist[-1] = 130
            startlist[-2] = answer_logits[0][0] - juli1
            startlist[-3] = 130
            startlist[-4] = answer_logits[0][0] - juli2
            startlist[-5] = 130
            startlist[-6] = 130
            startlist[-7] = 130
            startlist[-8] = answer_logits[0][0] - juli4

        elif xianjierandom == 7:
            startlist[-1] = 130
            startlist[-2] = answer_logits[0][0] - juli1
            startlist[-3] = 130
            startlist[-4] = 130
            startlist[-5] = 130
            startlist[-6] = answer_logits[0][0] - juli2
            startlist[-7] = 130
            startlist[-8] = answer_logits[0][0] - juli3
    answer_logits.insert(0, startlist)


def re_high_low_melody(answer_logits: list,
                       sm: SettingsManager,
                       md: MusicDetailManager) -> list:
    for xiaojie in range(0, len(answer_logits)):
        for yin in range(0, 8):
            if 48 < answer_logits[xiaojie][yin] < 100:
                answer_logits[xiaojie][yin] -= 12


def end_sing_melody(answer_logits: list,
                    sm: SettingsManager,
                    md: MusicDetailManager) -> list:
    out_tonality = [1, 3, 6, 8, 10]

    zhangjie = 0
    k = 0
    zhangjie_num = md.multi_root_charpter[k]

    for i in range(0, 8):
        if answer_logits[-1][-i] < 110:
            endnote2 = (answer_logits[-1][-i] - sm.tonality) % 12
            answer_logits[-1][-i] -= endnote2

    highlowend = np.random.randint(1, 2)
    for xiaojie in range(0, len(answer_logits)):
        if xiaojie * 8 >= zhangjie_num:
            zhangjie_num += md.multi_root_charpter[k]
            k += 1
            zhangjie += 1

        for nege_yin in range(0, 8):
            if answer_logits[xiaojie][-nege_yin] < 100 and (answer_logits[xiaojie][-nege_yin] - sm.tonality) % 12 == 11:
                if highlowend == 1:
                    answer_logits[xiaojie][-nege_yin] += 1
                else:
                    answer_logits[xiaojie][-nege_yin] -= 11
                break
            if answer_logits[xiaojie][-nege_yin] < 100 and (answer_logits[xiaojie][-nege_yin] - sm.tonality) % 12 == 5:
                if highlowend == 1:
                    answer_logits[xiaojie][-nege_yin] += 4
                else:
                    answer_logits[xiaojie][-nege_yin] -= 8
                break


def end_melody(answer_logits: list,
               sm: SettingsManager,
               md: MusicDetailManager) -> list:
    out_tonality = [1, 3, 6, 8, 10]

    zhangjie = 0
    k = 0
    zhangjie_num = md.multi_root_charpter[k]

    for i in range(0, 8):
        if answer_logits[-1][-i] < 110:
            endnote2 = (answer_logits[-1][-i] - sm.tonality) % 12
            answer_logits[-1][-i] -= endnote2

    for xiaojie in range(0, len(answer_logits)):
        for nege_yin in range(0, 8):
            if answer_logits[xiaojie][-nege_yin] < 100 and (answer_logits[xiaojie][-nege_yin] - sm.tonality) % 12 == 11:
                answer_logits[xiaojie][-nege_yin] += 1
                break
            if answer_logits[xiaojie][-nege_yin] < 100 and (answer_logits[xiaojie][-nege_yin] - sm.tonality) % 12 == 5:
                answer_logits[xiaojie][-nege_yin] += 2
                break
        for yin in range(0, 8):

            if xiaojie * 8 + yin >= zhangjie_num:
                zhangjie_num += md.multi_root_charpter[k]
                k += 1
                zhangjie += 1
                for i in range(0, 8):
                    if answer_logits[xiaojie - 2][-i] < 110:
                        endnote2 = (answer_logits[xiaojie - 2][-i] - sm.tonality) % 12
                        randomend = np.random.choice([0, 1], p=[0.95, 0.05, ])
                        if zhangjie == len(md.multi_root_charpter) - 1:
                            randomend = 0

                        if randomend == 0:
                            answer_logits[xiaojie - 2][-i] -= endnote2
                        else:
                            answer_logits[xiaojie - 2][-i] -= (endnote2 + 5)

                for i in range(0, 8):
                    if answer_logits[xiaojie - 1][-i] < 110 and zhangjie != len(md.multi_root_charpter) - 1:
                        endnote = (answer_logits[xiaojie - 1][-i] - sm.tonality) % 12
                        randomend = np.random.choice([0, 1, ],
                                                     p=[0.8, 0.2, ])

                        if randomend == 0:
                            answer_logits[xiaojie - 1][-i] -= endnote
                        else:
                            answer_logits[xiaojie - 1][-i] -= endnote + 7

                        xianjierandom = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8],
                                                         p=[0.15, 0.15, 0.1, 0.1, 0.1, 0.15, 0.15, 0.05, 0.05, ])
                        if answer_logits[xiaojie][0] < 100:
                            if xianjierandom == 0:
                                jiangelist = [0, 2, 4, 5, 7, 9, 11]

                                yin = (answer_logits[xiaojie][0] - sm.tonality) % 12
                                yin_num = jiangelist.index(yin)
                                baseyin = jiangelist[yin_num]
                                juli1 = jiangelist[yin_num] - jiangelist[yin_num - 1]
                                juli2 = jiangelist[yin_num] - jiangelist[yin_num - 2]
                                juli3 = jiangelist[yin_num] - jiangelist[yin_num - 3]
                                juli4 = jiangelist[yin_num] - jiangelist[yin_num - 4]
                                while juli1 < 0:
                                    juli1 += 12
                                while juli2 < 0:
                                    juli2 += 12
                                while juli3 < 0:
                                    juli3 += 12
                                while juli4 < 0:
                                    juli4 += 12

                                answer_logits[xiaojie - 1][-1] = 130
                                answer_logits[xiaojie - 1][-2] = answer_logits[xiaojie][0] - juli1
                                answer_logits[xiaojie - 1][-3] = 130
                                answer_logits[xiaojie - 1][-4] = answer_logits[xiaojie][0] - juli2
                                answer_logits[xiaojie - 1][-5] = 130
                                answer_logits[xiaojie - 1][-6] = answer_logits[xiaojie][0] - juli3
                                answer_logits[xiaojie - 1][-7] = 130
                                answer_logits[xiaojie - 1][-8] = answer_logits[xiaojie][0] - juli4

                            elif xianjierandom == 1:
                                jiangelist = [0, 2, 4, 5, 7, 9, 11]

                                yin = (answer_logits[xiaojie][0] - sm.tonality) % 12
                                yin_num = jiangelist.index(yin)
                                baseyin = jiangelist[yin_num]
                                juli1 = jiangelist[yin_num] - jiangelist[yin_num - 1]
                                juli2 = jiangelist[yin_num] - jiangelist[yin_num - 2]
                                juli3 = jiangelist[yin_num] - jiangelist[yin_num - 3]
                                juli4 = jiangelist[yin_num] - jiangelist[yin_num - 4]
                                while juli1 < 0:
                                    juli1 += 12
                                while juli2 < 0:
                                    juli2 += 12
                                while juli3 < 0:
                                    juli3 += 12
                                while juli4 < 0:
                                    juli4 += 12

                                answer_logits[xiaojie - 1][-1] = 130
                                answer_logits[xiaojie - 1][-2] = answer_logits[xiaojie][0] - juli1
                                answer_logits[xiaojie - 1][-3] = 130
                                answer_logits[xiaojie - 1][-4] = answer_logits[xiaojie][0] - juli2

                            elif xianjierandom == 2:
                                answer_logits[xiaojie - 1][-1] = 130
                                answer_logits[xiaojie - 1][-2] = answer_logits[xiaojie][0] - 5
                                answer_logits[xiaojie - 1][-3] = 130
                                answer_logits[xiaojie - 1][-4] = answer_logits[xiaojie][0] - 12

                            elif xianjierandom == 3:
                                answer_logits[xiaojie - 1][-1] = 130
                                answer_logits[xiaojie - 1][-2] = answer_logits[xiaojie][0] - 5
                                answer_logits[xiaojie - 1][-3] = 130
                                answer_logits[xiaojie - 1][-4] = answer_logits[xiaojie][0] - 12
                                answer_logits[xiaojie - 1][-5] = 130
                                answer_logits[xiaojie - 1][-6] = 130
                                answer_logits[xiaojie - 1][-7] = 130
                                answer_logits[xiaojie - 1][-8] = answer_logits[xiaojie][0] - 17

                            elif xianjierandom == 4:
                                answer_logits[xiaojie - 1][-1] = 130
                                answer_logits[xiaojie - 1][-2] = answer_logits[xiaojie][0] - 5
                                answer_logits[xiaojie - 1][-3] = 130
                                answer_logits[xiaojie - 1][-4] = answer_logits[xiaojie][0] - 12
                                answer_logits[xiaojie - 1][-5] = 130
                                answer_logits[xiaojie - 1][-6] = answer_logits[xiaojie][0] - 17

                            elif xianjierandom == 5:
                                answer_logits[xiaojie - 1][-1] = answer_logits[xiaojie][0] + 7
                                answer_logits[xiaojie - 1][-2] = answer_logits[xiaojie][0] + 12

                            elif xianjierandom == 6:
                                answer_logits[xiaojie - 1][-1] = answer_logits[xiaojie][0] + 7
                                answer_logits[xiaojie - 1][-2] = answer_logits[xiaojie][0] + 12
                                answer_logits[xiaojie - 1][-3] = answer_logits[xiaojie][0] + 19

                            elif xianjierandom == 7:
                                answer_logits[xiaojie - 1][-1] = 130
                                answer_logits[xiaojie - 1][-2] = answer_logits[xiaojie][0] + 7
                                answer_logits[xiaojie - 1][-3] = 130
                                answer_logits[xiaojie - 1][-4] = answer_logits[xiaojie][0] + 12

                            elif xianjierandom == 8:
                                answer_logits[xiaojie - 1][-1] = 130
                                answer_logits[xiaojie - 1][-2] = answer_logits[xiaojie][0] + 7
                                answer_logits[xiaojie - 1][-3] = 130
                                answer_logits[xiaojie - 1][-4] = answer_logits[xiaojie][0] + 12
                                answer_logits[xiaojie - 1][-5] = 130
                                answer_logits[xiaojie - 1][-6] = answer_logits[xiaojie][0] + 19

                        # 这个是调换16分音符和8分音符的位置的
                        if answer_logits[xiaojie - 1][-1] < 100 and answer_logits[xiaojie - 1][-2] > 100:
                            answer_logits[xiaojie - 1][-1], answer_logits[xiaojie - 1][-2] = answer_logits[xiaojie - 1][
                                                                                                 -2], \
                                                                                             answer_logits[xiaojie - 1][
                                                                                                 -1]
                        break
    return answer_logits


def spilt2midi(answer_logits: list,
               midi: Midi,
               sm: SettingsManager,
               ) -> list:
    out_tonality = [1, 3, 6, 8, 10]

    midi_list = [[], [], []]

    savenum = 0
    for xiaojie in range(0, len(answer_logits) - 1):
        for mm in range(0, 8):
            half = get_median(answer_logits[xiaojie])
            if random.randint(0, 100) < 101 - savenum and answer_logits[xiaojie][mm] <= 100:
                if half - 8 <= answer_logits[xiaojie][mm] <= half + 8 and (
                        answer_logits[xiaojie][mm] % 12 - sm.tonality) not in out_tonality:
                    midi_list[0].append(note_num_2_name(answer_logits[xiaojie][mm]))
                    midi_list[1].append(answer_logits[xiaojie][mm])
                    midi_list[2].append(xiaojie * 2 + 0.25 * mm)
                elif half + 8 <= answer_logits[xiaojie][mm] <= half + 16 and (
                        answer_logits[xiaojie][mm] % 12 - sm.tonality) not in out_tonality:
                    midi_list[0].append(note_num_2_name(answer_logits[xiaojie][mm] - 7))
                    midi_list[1].append(answer_logits[xiaojie][mm] - 7)
                    midi_list[2].append(xiaojie * 2 + 0.25 * mm)
                else:
                    midi_list[0].append(note_num_2_name(answer_logits[xiaojie][mm]))
                    midi_list[1].append(answer_logits[xiaojie][mm])
                    midi_list[2].append(xiaojie * 2 + 0.25 * mm)

    midi.names = midi_list[0]
    midi.nums = midi_list[1]
    midi.offsets = midi_list[2]
    return midi_list


def choice_note_bass_blance(answer_logits: list,
                            base_list: list,
                            sm: SettingsManager,
                            md: MusicDetailManager) -> list:
    answersing = []
    for i, content in enumerate(answer_logits):

        basexuhao = np.where(np.array(base_list[i]) < 110)
        basexuhao8 = np.where(basexuhao[0] < 8)[0]

        if 2 < len(basexuhao8) <= 4 or i % 4 == 0:
            rate = [0.0, 0.10, 0.5, 0.3, 0.05, 0.05, 0, 0]
        elif len(basexuhao8) <= 2:
            rate = [0.0, 0.50, 0.3, 0.2, 0.00, 0.00, 0, 0]
        else:
            rate = [0.00, 0.0, 0.35, 0.35, 0.25, 0.025, 0.025, 0.0]
        out = choice_4_sing_perlist(np.array(content), rate)
        answersing.append(out)
    return answersing


def choice_4_rest(sm, md, answer):
    answerrest = []
    zhangjie = 0
    k = 0
    zhangjie_num = md.multi_root_charpter[k]
    for xiaojie in range(0, len(answer)):
        for yin in range(0, 8):
            if xiaojie * 8 + yin > zhangjie_num:
                zhangjie_num += md.multi_root_charpter[k]
                k += 1
                zhangjie += 1
        if zhangjie < len(md.drumclasslist) and md.drumclasslist[zhangjie] > 0:
            out = answer[xiaojie]
        else:
            rate = [0.0, 0.1, 0.4, 0.4, 0.1, 0.00, 0, 0]
            out = choice_4_sing_perlist(np.array(answer[xiaojie]), rate)
        answerrest.append(out)
    return answerrest


def choice_4_fd(answer, bassornote):
    answersing = []
    for i, content in enumerate(answer):
        if bassornote == 'bass':
            rate = [0.00, 0.35, 0.45, 0.2, 0.0, 0.0, 0, 0]
        elif bassornote == 'note':
            rate = [0.0, 0.00, 0.1, 0.2, 0.35, 0.25, 0.1, 0]
        out = choice_4_sing_perlist(np.array(content), rate)
        answersing.append(out)
    return answersing


def choice_4_sing_perlist(Ldatanum, rate):  # Ldatanum = np.array([10, 20, 30, 400, 50, 60, 10, 20])
    notexuhao = np.where(Ldatanum < 110)
    out = [130, 130, 130, 130, 130, 130, 130, 130, ]
    if len(notexuhao[0]) > 0:
        xiaojie_yin_num = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, ], p=rate)
        saveforsing_note_num = np.random.choice(notexuhao[0], 0 + xiaojie_yin_num)
        for i in range(len(saveforsing_note_num)):
            out[saveforsing_note_num[i]] = Ldatanum[i]
    else:
        out = Ldatanum
    return out


def choice_4_singlist(answer, saveyinlist):
    for xiaojie in range(len(answer)):
        if xiaojie < len(saveyinlist):
            for yin in range(len(answer[0])):
                if saveyinlist[xiaojie][yin] == 0:
                    answer[xiaojie][yin] = 130
                if saveyinlist[xiaojie][yin] == 1 and answer[xiaojie][yin] > 100:
                    answer[xiaojie][yin] = random.randint(54, 70)

    return answer


def choice_4_perlist(Ldatanum, rate):  # Ldatanum = np.array([10, 20, 30, 400, 50, 60, 10, 20])
    notexuhao = np.where(Ldatanum < 110)
    out = [130, 130, 130, 130, 130, 130, 130, 130, ]
    if len(notexuhao[0]) > 0:
        xiaojie_yin_num = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7, ], p=rate)
        saveforsing_note_num = np.random.choice(notexuhao[0], 0 + xiaojie_yin_num)
        for i in range(len(saveforsing_note_num)):
            out[saveforsing_note_num[i]] = Ldatanum[i]
    else:
        out = Ldatanum
    outlist = np.where(np.array(out) < 110)
    return out


def singcount16notenum(answer_logits: list,
                       sm: SettingsManager,
                       md: MusicDetailManager
                       ) -> list:
    for xiaojie in range(0, len(answer_logits)):
        for mm in range(0, 8):
            if (mm + 1) % 2 == 0:
                if answer_logits[xiaojie][mm - 1] > 110 and answer_logits[xiaojie][mm] < 100:
                    answer_logits[xiaojie][mm], answer_logits[xiaojie][mm - 1] = answer_logits[xiaojie][mm - 1], \
                                                                                 answer_logits[xiaojie][mm]


def count16notenum(answer_logits: list,
                   sm: SettingsManager,
                   md: MusicDetailManager
                   ) -> list:
    for xiaojie in range(0, len(answer_logits)):
        for mm in range(0, 8):
            if (mm + 1) % 2 == 0:

                if answer_logits[xiaojie][mm - 1] > 110 and answer_logits[xiaojie][mm] < 100:
                    answer_logits[xiaojie][mm], answer_logits[xiaojie][mm - 1] = answer_logits[xiaojie][mm - 1], \
                                                                                 answer_logits[xiaojie][mm]
    if_del_16_note = np.random.choice([0, 1], p=[0.8, 0.2])
    if sm.bpm >= 100:
        if_del_16_note = 1

    if if_del_16_note == 1:
        for xiaojie in range(0, len(answer_logits)):
            for mm in range(0, 8):
                if (mm + 1) % 2 == 0:
                    answer_logits[xiaojie][mm] = 130
    elif if_del_16_note == 0:
        for xiaojie in range(0, len(answer_logits)):
            if_xiaojie_del_16_note = np.random.choice([0, 1], p=[0.4, 0.6])
            for mm in range(0, 8):
                if (mm + 1) % 2 == 0 and if_xiaojie_del_16_note == 1:
                    answer_logits[xiaojie][mm] = 130
    return answer_logits

def get_highernote(answer_logits: list,
                   sm: SettingsManager,
                   md: MusicDetailManager) -> list:
    zhangjie = 0
    k = 0
    zhangjie_num = md.multi_root_charpter[k]
    zhangjiechange = 0
    for xiaojie in range(0, len(answer_logits)):
        for yin in range(0, 8):

            if xiaojie * 8 + yin >= zhangjie_num:
                zhangjie_num += md.multi_root_charpter[k]
                k += 1
                zhangjie += 1
                zhangjiechange = np.random.choice([-1, 0, 1], p=[0.45, 0.5, 0.05])
            if zhangjiechange == 1 and 48 < answer_logits[xiaojie][yin] < 100:
                answer_logits[xiaojie][yin] += 12
            elif zhangjiechange == -1 and 48 < answer_logits[xiaojie][yin] < 100:
                answer_logits[xiaojie][yin] -= 12


# 还不能用，缺个衔接
def changetonality(answer_logits: list,
                   sm: SettingsManager,
                   md: MusicDetailManager) -> list:
    zhangjie = 0
    k = 0
    zhangjie_num = md.multi_root_charpter[k]
    zhangjiechange = 0
    for xiaojie in range(0, len(answer_logits)):
        for yin in range(0, 8):

            if xiaojie * 8 + yin >= zhangjie_num:
                zhangjie_num += md.multi_root_charpter[k]
                k += 1
                zhangjie += 1
            if zhangjie == len(md.multi_root_charpter) - 1 and 20 < answer_logits[xiaojie][yin] < 100:
                answer_logits[xiaojie][yin] += 3


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


def answer23part(answerlogit,
                 music_bass: list,
                 sm: SettingsManager,
                 md: MusicDetailManager) -> dict:
    answer1 = []
    answer2 = []
    answer3 = []

    lowlist = [random.randint(0, len(answerlogit) // 2), random.randint(0, len(answerlogit) // 2)]
    lowlist.append(lowlist[0] + len(answerlogit) // 2)
    lowlist.append(lowlist[1] + len(answerlogit) // 2)
    for i in range(len(answerlogit)):
        answer1.append([])
        answer2.append([])
        answer3.append([])
        for j in range(len(answerlogit[i])):

            if j % 2 == 1 and sm.bpm > 110:  # and random.randint(0, 10) <= 0.7:
                answerlogit[i][j] += 100

            if j % 2 == 1 and j in lowlist:
                answerlogit[i][j] += 100

            if j < 8:
                answer1[i].append(answerlogit[i][j])
            elif 8 <= j < 16:
                answer2[i].append(answerlogit[i][j])
            elif 16 <= j < 24:
                answer3[i].append(answerlogit[i][j])

    music_bass = np.array(music_bass).tolist()

    answer11 = np.array(answer1).tolist()
    answer21 = np.array(answer2).tolist()
    answer31 = np.array(answer3).tolist()

    choice_note_bass_blance(answer11, music_bass, sm, md)
    choice_note_bass_blance(answer21, music_bass, sm, md)
    choice_note_bass_blance(answer31, music_bass, sm, md)


    answer11 = choice_4_rest(sm, md, answer11)
    answer21 = choice_4_fd(answer2, 'note')

    count16notenum(answer11, sm, md)
    count16notenum(answer21, sm, md)
    count16notenum(answer31, sm, md)

    get_highernote(answer11, sm, md)
    get_highernote(answer21, sm, md)
    get_highernote(answer31, sm, md)

    answer21 = ABAC_model(answer21, batch=0, sm=sm, md=md)
    answer31 = ABAC_model(answer31, batch=0, sm=sm, md=md)

    answer31 = mj(answer31, sm, md)

    music_bass, answer11 = revise_two_melody(music_bass, answer11, sm, md)
    music_bass, answer21 = revise_two_melody(music_bass, answer21, sm, md)
    music_bass, answer31 = revise_two_melody(music_bass, answer31, sm, md)

    addstart_random = 0#np.random.choice([0, 1], p=[0.4, 0.6])
    if addstart_random == 1:
        xianjierandom = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7],
                                         p=[0.2, 0.2, 0.05, 0.15, 0.1, 0.1, 0.1, 0.1])  # [0.4, 0.3, 0.3, ]
        add_start_melody(answer11, sm, md, xianjierandom)
        add_start_melody(answer21, sm, md, xianjierandom)
        add_start_melody(answer31, sm, md, xianjierandom)

    end_melody(answer11, sm, md)
    end_melody(answer21, sm, md)
    end_melody(answer31, sm, md)

    if sm.heavyorlight==1:
        re_high_low_melody(answer11, sm, md)
        re_high_low_melody(answer21, sm, md)
        re_high_low_melody(answer31, sm, md)



    answer11 = np.array(answer11).tolist()
    answer21 = np.array(answer21).tolist()
    answer31 = np.array(answer31).tolist()

    melody1 = Midi()
    melody2 = Midi()
    melody3 = Midi()

    midi_list1 = spilt2midi(answer11, melody1, sm)
    midi_list2 = spilt2midi(answer21, melody2, sm)
    midi_list3 = spilt2midi(answer31, melody3, sm)

    answer11series = []
    bass11series = []
    for xiaojie in range(len(answer11)):
        for yin in range(8):
            answer11series.append(answer11[xiaojie][yin])
    for xiaojie in range(len(music_bass)):
        for yin in range(8):
            bass11series.append(music_bass[xiaojie][yin])
    return {'1': np.array(answer11).tolist(),
            '2': np.array(answer21).tolist(),
            '3': np.array(answer31).tolist(), }, answer11series, bass11series



def lowpass_sing_melody(sing_midi_answer):
    listzuobiao = []
    listdata = []
    for xiaojie in range(len(sing_midi_answer)):
        for yin in range(8):
            if sing_midi_answer[xiaojie][yin] < 130:
                listzuobiao.append([xiaojie, yin])
                listdata.append(sing_midi_answer[xiaojie][yin])
    # N阶，临界频率，Wn与fs相同
    b, a = signal.butter(18, 0.4, 'lowpass')
    filtedData = signal.filtfilt(b, a, listdata)  # data为要过滤的信号
    print('lowpass_sing_melody: ', len(filtedData), np.array(filtedData).astype(int))

    for i in range(len(filtedData)):
        xiaojie = listzuobiao[i][0]
        yin = listzuobiao[i][1]
        sing_midi_answer[xiaojie][yin] = round(filtedData[i])
    return sing_midi_answer


def get_sing_list(sm: SettingsManager,
                  md: MusicDetailManager,
                  music_bass: list,
                  saveyinlist: list):
    # 修改歌词音的范围
    sing_midi_answer = [random_int_list(54, 66, 8) for i in range(len(music_bass))]
    # print('sing_midi_answer', sing_midi_answer)
    sing_midi_answer = np.array(sing_midi_answer).tolist()

    # sing_midi_answer = ABAC_model_simple(sing_midi_answer, batch=0, sm=sm, md=md)
    # print('sing_midi_answer', sing_midi_answer)

    # music_bass, sing_midi_answer = revise_two_melody(music_bass, sing_midi_answer, sm, md, sing=1)
    # end_melody(sing_midi_answer, sm, md)
    # print('sing_midi_answer', sing_midi_answer)

    sing_midi_answer = lowpass_sing_melody(sing_midi_answer)

    sing_midi_answer2 = choice_4_singlist(np.copy(sing_midi_answer), saveyinlist)
    # print('choice_4_singlist sing_midi_answer2', sing_midi_answer2)

    end_sing_melody(sing_midi_answer2, sm, md)
    # print('end_melody22 sing_midi_answer', sing_midi_answer)

    music_bass, sing_midi_answer2 = revise_two_melody(music_bass, sing_midi_answer2, sm, md)
    revise_two_melody4sing(music_bass, sing_midi_answer2, sm, md)
    # print('sing_midi_answer revise_two_melody', sing_midi_answer2)
    # singcount16notenum(sing_midi_answer2, sm, md)
    sing_midi_answer2 = np.array(sing_midi_answer2).tolist()
    # print('sing_midi_answer2', sing_midi_answer2)
    # melodysing = Midi()
    # midi_listsing2 = spilt2midi(sing_midi_answer2, melodysing, sm)
    # write_midi(melodysing, sm.fm.midi_sing_output_name)

    return sing_midi_answer2
