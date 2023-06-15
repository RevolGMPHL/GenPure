import numpy as np


def ABAC_model(midi, batch, sm, md):  # answer_logits: list, sm: SettingsManager,

    # 获取每个xiaojie对应的章节，章节来判断当前是什么root，然后根据root来决定重复长度，root之内的2 3 4个小节重复
    midi4copy = []
    midi4copy2 = []
    midi4copy3 = []

    k = 0
    zhangjie = 0
    zhangjie_num = md.multi_root_charpter[k]
    multi_root_charpter = md.multi_root_charpter
    multi_root = md.multi_root
    root1 = sm.root
    root2 = sm.root2
    root3 = sm.root3

    midi2 = midi.copy()
    repeat = np.random.choice([2, 3, 4, 8], p=[0.1, 0.2, 0.3, 0.4])

    # repeat = np.random.choice([2, 3, 4, 8], p=[0.0, 0.0, 0.0, 1])

    for xiaojie in range(0, len(midi)):
        for yin in range(0, 8):
            # 计算当前这个音在那个章节里
            if xiaojie * 8 + yin >= zhangjie_num:
                zhangjie_num += multi_root_charpter[k]
                k += 1
                zhangjie += 1

                if zhangjie < len(multi_root):
                    root = multi_root[zhangjie]

                # 相同root的章节里前4个小节的都一样
                if root == root1 and len(midi4copy) == 0:
                    midi4copy.append(midi[xiaojie])
                    midi4copy.append(midi[xiaojie + 1])
                    if repeat == 3:
                        midi4copy.append(midi[xiaojie + 2])
                    if repeat == 4:
                        midi4copy.append(midi[xiaojie + 2])
                        midi4copy.append(midi[xiaojie + 3])
                    if repeat == 8:
                        midi4copy.append(midi[xiaojie + 2])
                        midi4copy.append(midi[xiaojie + 3])
                        try:
                            midi4copy.append(midi[xiaojie + 4])
                            midi4copy.append(midi[xiaojie + 5])
                            midi4copy.append(midi[xiaojie + 6])
                            midi4copy.append(midi[xiaojie + 7])
                        except:
                            pass

                elif root == root2 and len(midi4copy2) == 0:
                    midi4copy2.append(midi[xiaojie])
                    midi4copy2.append(midi[xiaojie + 1])
                    if repeat == 3:
                        midi4copy2.append(midi[xiaojie + 2])
                    if repeat == 4:
                        midi4copy2.append(midi[xiaojie + 2])
                        midi4copy2.append(midi[xiaojie + 3])
                    if repeat == 8:
                        midi4copy2.append(midi[xiaojie + 2])
                        midi4copy2.append(midi[xiaojie + 3])
                        try:
                            midi4copy.append(midi[xiaojie + 4])
                            midi4copy.append(midi[xiaojie + 5])
                            midi4copy.append(midi[xiaojie + 6])
                            midi4copy.append(midi[xiaojie + 7])
                        except:
                            pass

                elif root == root3 and len(midi4copy3) == 0:
                    midi4copy3.append(midi[xiaojie])
                    midi4copy3.append(midi[xiaojie + 1])
                    if repeat == 3:
                        midi4copy3.append(midi[xiaojie + 2])
                    if repeat == 4:
                        midi4copy3.append(midi[xiaojie + 2])
                        midi4copy3.append(midi[xiaojie + 3])
                    if repeat == 8:
                        midi4copy3.append(midi[xiaojie + 2])
                        midi4copy3.append(midi[xiaojie + 3])
                        try:
                            midi4copy.append(midi[xiaojie + 4])
                            midi4copy.append(midi[xiaojie + 5])
                            midi4copy.append(midi[xiaojie + 6])
                            midi4copy.append(midi[xiaojie + 7])
                        except:
                            pass

                if root == root1:
                    midi2[xiaojie] = midi4copy[0]
                    try:
                        midi2[xiaojie + 1] = midi4copy[1]
                    except:
                        pass
                    if repeat == 3:
                        try:
                            midi2[xiaojie + 2] = midi4copy[2]
                        except:
                            pass
                    if repeat == 4:
                        try:
                            midi2[xiaojie + 2] = midi4copy[2]
                            midi2[xiaojie + 3] = midi4copy[3]
                        except:
                            pass
                    if repeat == 8:
                        midi2[xiaojie + 2] = midi4copy[2]
                        midi2[xiaojie + 3] = midi4copy[3]
                        try:
                            midi4copy.append(midi[xiaojie + 4])
                            midi4copy.append(midi[xiaojie + 5])
                            midi4copy.append(midi[xiaojie + 6])
                            midi4copy.append(midi[xiaojie + 7])
                        except:
                            pass

                elif root == root2:
                    midi2[xiaojie] = midi4copy2[0]
                    midi2[xiaojie + 1] = midi4copy2[1]
                    if repeat == 3:
                        midi2[xiaojie + 2] = midi4copy2[2]
                    if repeat == 4:
                        midi2[xiaojie + 2] = midi4copy2[2]
                        midi2[xiaojie + 3] = midi4copy2[3]
                    if repeat == 8:
                        midi2[xiaojie + 2] = midi4copy2[2]
                        midi2[xiaojie + 3] = midi4copy2[3]
                        try:
                            midi4copy.append(midi[xiaojie + 4])
                            midi4copy.append(midi[xiaojie + 5])
                            midi4copy.append(midi[xiaojie + 6])
                            midi4copy.append(midi[xiaojie + 7])
                        except:
                            pass

                elif root == root3:
                    midi2[xiaojie] = midi4copy3[0]
                    midi2[xiaojie + 1] = midi4copy3[1]
                    if repeat == 3:
                        midi2[xiaojie + 2] = midi4copy3[2]
                    if repeat == 4:
                        midi2[xiaojie + 2] = midi4copy3[2]
                        midi2[xiaojie + 3] = midi4copy3[3]
                    if repeat == 8:
                        midi2[xiaojie + 2] = midi4copy3[2]
                        midi2[xiaojie + 3] = midi4copy3[3]
                        try:
                            midi4copy.append(midi[xiaojie + 4])
                            midi4copy.append(midi[xiaojie + 5])
                            midi4copy.append(midi[xiaojie + 6])
                            midi4copy.append(midi[xiaojie + 7])
                        except:
                            pass

    for i in range(0, len(midi2)):
        for j in range(0, 8):
            if midi2[i][j] < 100:
                while midi2[i][j] <= 60:
                    midi2[i][j] += 12
                while midi2[i][j] >= 86:
                    midi2[i][j] -= 12

    return midi2


def ABAC_model_simple(midi, batch, sm, md):  # answer_logits: list, sm: SettingsManager,

    # 获取每个xiaojie对应的章节，章节来判断当前是什么root，然后根据root来决定重复长度，root之内的2 3 4个小节重复
    midi4copy = []
    midi4copy2 = []
    midi4copy3 = []

    k = 0
    zhangjie = 0
    zhangjie_num = md.multi_root_charpter[k]
    multi_root_charpter = md.multi_root_charpter
    multi_root = md.multi_root
    root1 = sm.root
    root2 = sm.root2
    root3 = sm.root3

    midi2 = midi.copy()
    repeat = np.random.choice([2, 3, 4, 8], p=[0.1, 0.3, 0.4, 0.2])

    # repeat = np.random.choice([2, 3, 4, 8], p=[0.0, 0.0, 0.0, 1])

    for xiaojie in range(0, len(midi)):
        for yin in range(0, 8):
            # 计算当前这个音在那个章节里
            if xiaojie * 8 + yin >= zhangjie_num:
                zhangjie_num += multi_root_charpter[k]
                k += 1
                zhangjie += 1

                if zhangjie < len(multi_root):
                    root = multi_root[zhangjie]

                # 相同root的章节里前4个小节的都一样

                midi4copy.append(midi[xiaojie])
                midi4copy.append(midi[xiaojie + 1])
                if repeat == 3:
                    midi4copy.append(midi[xiaojie + 2])
                if repeat == 4:
                    try:
                        midi4copy.append(midi[xiaojie + 2])
                        midi4copy.append(midi[xiaojie + 3])
                    except:
                        pass
                if repeat == 8:
                    try:
                        midi4copy.append(midi[xiaojie + 2])
                        midi4copy.append(midi[xiaojie + 3])
                        midi4copy.append(midi[xiaojie + 4])
                        midi4copy.append(midi[xiaojie + 5])
                        midi4copy.append(midi[xiaojie + 6])
                        midi4copy.append(midi[xiaojie + 7])
                    except:
                        pass
                midi2[xiaojie] = midi4copy[0]
                midi2[xiaojie + 1] = midi4copy[1]
                if repeat == 3:
                    midi2[xiaojie + 2] = midi4copy[2]
                if repeat == 4:
                    midi2[xiaojie + 2] = midi4copy[2]
                    midi2[xiaojie + 3] = midi4copy[3]
                if repeat == 8:
                    midi2[xiaojie + 4] = midi4copy[4]
                    midi2[xiaojie + 5] = midi4copy[5]
                    midi2[xiaojie + 6] = midi4copy[6]
                    midi2[xiaojie + 7] = midi4copy[7]

    for i in range(0, len(midi2)):
        for j in range(0, 8):
            if midi2[i][j] < 100:
                while midi2[i][j] <= 60:
                    midi2[i][j] += 12
                while midi2[i][j] >= 86:
                    midi2[i][j] -= 12

    return midi2
