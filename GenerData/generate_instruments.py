import random
from typing import Tuple

import numpy as np
from tqdm import tqdm


def get_instrument_list(chapters_num, melody_instruments_set, base_instruments_set,
                        drumclasslist) -> Tuple[list, list, list]:
    multi_instrument_melody_new = []
    multi_instrument_bass_new = []

    sing_melody_new = []
    hunman_instrument = np.random.choice([22, 26, 27, 28, 32, 33, 36, 40, 43, 57])  # 32好听 29,

    ins_num_melody = 1
    ins_num_bass = 2

    chapters_num = chapters_num

    # 在这里选择每个章节乐器有多少
    for i in range(0, chapters_num):

        if drumclasslist[i] < 0:
            ins_num_melody = np.random.choice([1, 2, 3, 4, 5], 1, p=[0.4, 0.45, 0.05, 0.05, 0.05])
            ins_num_bass = np.random.choice([1, 2, 3, 4, 5], 1, p=[0.4, 0.45, 0.05, 0.05, 0.05])
        elif drumclasslist[i] >= 0:
            ins_num_melody = np.random.choice([2, 3, 4, 5, 6], 1, p=[0.0, 0.1, 0.3, 0.3, 0.3])
            ins_num_bass = np.random.choice([2, 3, 4, 5, 6], 1, p=[0.0, 0.1, 0.3, 0.3, 0.3])

        random_note = np.unique(
            np.random.choice(melody_instruments_set, ins_num_melody)).tolist()  # choice 是3 的话，就是在前面的set里随机顺序抽随机个

        while len(random_note) <= 5:
            random_note.append(-2)

        random_bass = np.unique(np.random.choice(base_instruments_set, random.randint(1, ins_num_bass))).tolist()
        while len(random_bass) <= 6:
            random_bass.append(-2)

        # 下面这句话打开就可以固定的选择bass部分的乐器
        # random_bass = list(np.unique(np.array([12])))# 19是Violas_note_num

        # print('random_note: ', random_note)
        # 每个章节用到的乐器
        sing_melody_new.append([hunman_instrument, -2, -2, -2, -2, -2, -2])
        multi_instrument_melody_new.append(random_note)
        multi_instrument_bass_new.append(random_bass)

    # 第一个小节不能是stahighvio
    # print('\nmulti_instrument_bass_new   ', len(multi_instrument_bass_new), '\n', multi_instrument_bass_new)
    # print('multi_instrument_melody_new  ', len(multi_instrument_melody_new), '\n', multi_instrument_melody_new, '\n')

    return multi_instrument_bass_new, multi_instrument_melody_new, sing_melody_new


def get_input_instrument(chapters_num: int):
    multi_instrument_melody_new = []
    for i in range(chapters_num):
        print('请输入第%d章节乐器：' % (i + 1))
        x = input()
        xlist = list(map(int, x.split(",")))
        while len(xlist) < 10:
            xlist.append(-2)
        print(xlist)
        multi_instrument_melody_new.append(xlist)
    # print('multi_instrument_melody_new\n', multi_instrument_melody_new)
    return multi_instrument_melody_new
