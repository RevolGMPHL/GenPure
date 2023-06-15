from music21 import note, chord, converter

from GenerData.note_name_and_num import note_name_2_num


# 输入时已经是归一化完的，note = (noteraw - sm.tonality)%12
def chordtype(sm, note):
    chord = 0
    # print('sm.hexiantype, note: ', sm.hexiantype, note)
    if sm.hexiantype == 0:  # 普通类
        if note in [2, 4, 9]:
            chord = 1
        elif note in [0, 5, 7]:
            chord = 0
        elif note in [11]:
            chord = 2
    elif sm.hexiantype == 1:  # 寒蝉类
        if note in [0, 5]:
            chord = 3
        elif note in [7]:
            chord = 4
        elif note in [2, 4, 9]:
            chord = 5
        elif note in [11]:
            chord = 6
    # print('chord: ', chord)
    return chord


def tonality2C(numlist, tonality):
    Ctonality = [[numlist[i][k] - tonality for k in range(0, len(numlist[i]))] for i in range(0, len(numlist))]
    out_tonality = [1, 3, 6, 8, 10]
    Ctonality_out = [[k if k % 12 not in out_tonality else k + 1 for k in i] for i in Ctonality]

    return Ctonality_out


def tonality2raw(numlist, tonality):
    # 1, 3, 6810
    rawtonality = [[numlist[i][k] + tonality for k in range(0, len(numlist[i]))] for i in range(0, len(numlist))]
    return rawtonality


# bass_splited_num_notes = [[35, 132, 42, 130, 47, 132, 49, 130], [50, 130, 130, 130, 132, 130, 132, 130], [31, 132, 38, 130, 43, 130, 45, 130], [47, 130, 132, 132, 50, 132, 132, 132], [33, 130, 40, 130, 45, 130, 47, 130], [49, 132, 130, 130, 47, 130, 132, 130], [38, 132, 45, 132, 50, 132, 52, 130], [54, 130, 132, 132, 52, 130, 50, 132], [35, 132, 42, 130, 47, 132, 49, 132], [50, 132, 130, 130, 132, 132, 132, 130], [31, 132, 38, 132, 43, 132, 45, 130], [47, 132, 130, 130, 35, 132, 132, 130], [33, 130, 40, 130, 45, 132, 47, 132], [49, 130, 130, 130, 47, 132, 130, 132], [38, 132, 45, 132, 50, 132, 52, 130], [50, 130, 130, 130, 49, 130, 50, 132], [35, 130, 42, 130, 47, 130, 49, 130], [50, 130, 132, 132, 132, 130, 132, 130], [31, 130, 38, 132, 43, 130, 45, 132], [47, 130, 132, 130, 45, 130, 43, 130], [33, 130, 40, 132, 45, 132, 47, 132], [49, 132, 132, 130, 47, 130, 130, 132], [38, 130, 45, 132, 50, 130, 52, 130], [54, 130, 132, 130, 52, 132, 50, 130], [35, 130, 42, 130, 47, 132, 49, 130], [50, 130, 132, 132, 130, 132, 132, 130], [31, 132, 38, 132, 43, 130, 45, 132], [47, 130, 130, 132, 45, 132, 43, 130], [33, 130, 40, 132, 45, 130, 47, 132], [49, 132, 132, 132, 47, 132, 130, 132], [38, 130, 45, 130, 50, 130, 52, 132], [54, 130, 130, 130, 50, 130, 130, 130], [35, 132, 42, 130, 47, 130, 49, 130], [50, 132, 132, 130, 132, 132, 132, 132], [31, 130, 38, 132, 43, 132, 45, 130], [47, 130, 132, 132, 43, 130, 45, 132], [33, 130, 40, 130, 45, 130, 47, 132], [49, 130, 132, 132, 47, 130, 132, 132], [38, 130, 45, 132, 50, 130, 52, 130], [54, 132, 132, 130, 52, 130, 50, 130], [35, 132, 42, 130, 47, 130, 49, 132], [50, 132, 132, 132, 130, 130, 132, 132], [31, 132, 38, 132, 43, 130, 45, 132], [47, 132, 130, 130, 50, 130, 132, 132], [33, 130, 40, 132, 45, 130, 47, 132], [49, 132, 132, 130, 132, 130, 132, 132], [38, 132, 45, 132, 50, 130, 52, 130], [54, 130, 130, 130, 52, 130, 50, 130], [35, 130, 42, 130, 47, 130, 49, 130], [50, 132, 132, 130, 132, 132, 132, 132], [31, 130, 38, 130, 43, 130, 45, 130], [47, 130, 130, 130, 50, 132, 130, 132], [33, 132, 40, 132, 45, 130, 47, 132], [49, 130, 132, 132, 47, 132, 132, 132], [38, 132, 45, 130, 50, 130, 52, 130], [54, 132, 132, 130, 130, 132, 132, 130], [35, 132, 42, 132, 47, 132, 49, 130], [50, 130, 130, 132, 130, 130, 130, 132], [31, 132, 38, 130, 43, 130, 45, 132], [47, 130, 130, 130, 50, 130, 132, 130], [33, 130, 40, 130, 45, 132, 47, 132], [49, 132, 130, 132, 47, 130, 132, 130], [38, 132, 45, 130, 50, 130, 52, 130], [54, 130, 132, 130, 52, 132, 50, 130], [35, 130, 42, 132, 47, 132, 49, 132], [50, 132, 132, 132, 130, 132, 132, 132], [31, 132, 38, 130, 43, 132, 45, 132], [47, 130, 132, 132, 50, 132, 130, 132], [33, 130, 40, 132, 45, 132, 47, 132], [49, 130, 132, 132, 47, 132, 130, 132], [38, 132, 45, 132, 50, 130, 52, 130], [54, 130, 130, 130, 52, 132, 50, 130], [35, 132, 42, 132, 47, 130, 49, 132], [50, 130, 130, 130, 132, 132, 130, 130], [31, 132, 38, 132, 43, 130, 45, 130], [47, 132, 132, 132, 50, 130, 132, 132], [33, 132, 40, 130, 45, 130, 47, 132], [49, 132, 132, 132, 47, 130, 130, 130], [38, 130, 45, 132, 50, 132, 52, 132], [54, 132, 130, 130, 52, 132, 50, 130], [35, 130, 42, 130, 47, 132, 49, 130], [50, 132, 130, 130, 132, 130, 130, 132], [31, 132, 38, 130, 43, 130, 45, 130], [47, 132, 132, 132, 50, 132, 132, 132], [33, 130, 40, 132, 45, 132, 47, 130], [49, 130, 130, 130, 47, 130, 132, 130], [38, 130, 45, 132, 50, 130, 52, 130], [54, 132, 130, 130, 52, 132, 50, 130], [35, 130, 42, 130, 47, 132, 49, 130], [50, 130, 132, 132, 132, 132, 132, 132], [31, 130, 38, 130, 43, 132, 45, 130], [47, 132, 132, 132, 50, 130, 130, 130], [33, 132, 40, 132, 45, 130, 47, 130], [49, 130, 132, 132, 47, 132, 132, 130], [38, 130, 45, 132, 50, 130, 52, 130], [54, 132, 130, 132, 52, 130, 50, 132], [35, 132, 42, 132, 47, 132, 49, 130], [50, 130, 130, 132, 132, 132, 130, 132], [31, 130, 38, 130, 43, 132, 45, 132], [47, 132, 132, 132, 43, 132, 45, 130], [33, 130, 40, 130, 45, 130, 47, 130], [49, 132, 130, 130, 47, 130, 132, 130], [38, 132, 45, 130, 50, 132, 52, 130], [54, 132, 130, 132, 50, 130, 132, 132], [35, 130, 42, 130, 47, 130, 49, 130], [50, 132, 132, 132, 130, 132, 132, 132], [31, 130, 38, 130, 43, 130, 45, 132], [50, 132, 130, 132, 43, 132, 45, 130], [33, 132, 40, 132, 45, 130, 47, 130], [49, 130, 132, 132, 47, 132, 130, 132], [38, 130, 45, 132, 50, 130, 52, 130], [54, 132, 130, 130, 50, 130, 132, 130], [35, 130, 42, 132, 47, 132, 49, 130], [50, 130, 132, 130, 132, 132, 132, 132], [31, 130, 38, 130, 43, 130, 45, 132], [47, 132, 130, 132, 43, 132, 45, 132], [33, 132, 40, 132, 45, 130, 47, 132], [49, 132, 132, 130, 47, 132, 130, 130], [38, 132, 45, 132, 50, 132, 52, 130], [54, 130, 130, 130, 50, 132, 132, 130], [35, 130, 42, 130, 47, 130, 49, 130], [50, 130, 130, 130, 132, 130, 132, 132], [31, 132, 38, 130, 43, 130, 45, 130], [47, 132, 132, 130, 43, 130, 45, 130], [33, 130, 40, 132, 45, 130, 47, 132], [49, 132, 132, 132, 47, 130, 130, 130], [38, 130, 45, 130, 50, 130, 52, 132], [54, 130, 130, 132, 50, 130, 130, 132], [35, 130, 42, 132, 47, 132, 49, 130], [50, 132, 130, 132, 130, 132, 132, 132], [31, 130, 38, 130, 43, 130, 45, 130], [47, 130, 132, 132, 43, 132, 38, 132], [33, 130, 40, 130, 45, 132, 47, 132], [49, 130, 132, 132, 47, 132, 132, 132], [38, 132, 45, 130, 50, 130, 52, 132], [54, 130, 132, 132, 52, 130, 50, 132], [35, 132, 42, 132, 47, 130, 49, 132], [50, 132, 130, 132, 132, 130, 132, 130], [31, 130, 38, 132, 43, 132, 45, 132], [47, 132, 130, 132, 43, 132, 38, 132], [33, 130, 40, 132, 45, 132, 47, 130], [49, 132, 132, 130, 47, 132, 132, 38], [50, 130, 132, 130, 130, 132, 130, 28], [37, 132, 130, 132, 130, 132, 132, 35], [47, 130, 130, 132, 130, 130, 132, 130], [130, 130, 130, 132, 132, 130, 132, 31], [43, 132, 132, 130, 130, 130, 130, 132], [132, 132, 132, 130, 132, 130, 132, 33], [45, 130, 130, 132, 132, 132, 130, 130], [132, 132, 130, 132, 132, 132, 132, 38], [50, 132, 132, 132, 132, 130, 130, 130], [130, 132, 132, 132, 132, 132, 130, 35], [47, 132, 132, 132, 132, 132, 132, 132], [132, 130, 132, 130, 130, 132, 132, 31], [43, 130, 130, 130, 132, 132, 132, 130], [130, 132, 132, 132, 130, 132, 130, 33], [45, 130, 132, 132, 132, 132, 132, 132], [130, 130, 132, 132, 132, 132, 130, 38], [50, 130, 130, 130, 130, 132, 130, 132], [132, 130, 130, 132, 132, 132, 132, 130], [47, 130, 54, 130, 59, 132, 61, 130], [62, 130, 132, 130, 130, 130, 132, 130], [43, 130, 50, 132, 55, 130, 57, 132], [59, 130, 130, 130, 62, 130, 132, 132], [45, 130, 52, 130, 57, 132, 59, 130], [61, 130, 130, 130, 59, 130, 132, 130], [50, 132, 57, 132, 62, 132, 64, 130], [66, 132, 132, 130, 130, 132, 132, 130], [47, 130, 54, 132, 59, 132, 61, 130], [62, 132, 132, 132, 130, 132, 130, 132], [43, 130, 50, 130, 55, 132, 57, 132], [59, 132, 130, 132, 62, 130, 132, 132], [45, 130, 52, 132, 57, 130, 59, 130], [61, 132, 130, 132, 59, 132, 132, 130], [50, 132, 57, 132, 62, 130, 64, 132], [66, 130, 132, 132, 64, 130, 62, 132], [47, 132, 54, 130, 59, 132, 61, 130], [62, 130, 132, 132, 130, 130, 132, 132], [43, 130, 50, 132, 55, 132, 57, 130], [59, 130, 132, 130, 62, 132, 130, 130], [45, 130, 52, 132, 57, 132, 59, 132], [61, 130, 130, 130, 59, 132, 130, 130], [50, 132, 57, 130, 62, 132, 64, 132], [66, 132, 130, 132, 64, 132, 62, 132], [47, 132, 54, 130, 59, 132, 61, 130], [62, 130, 130, 130, 130, 132, 130, 130], [43, 130, 50, 132, 55, 132, 57, 130], [59, 130, 130, 132, 62, 130, 130, 130], [45, 130, 52, 130, 57, 132, 59, 130], [61, 130, 132, 132, 59, 130, 132, 130], [26, 30, 33, 38, 42, 45, 50, 54], [57, 50, 54, 57, 62, 57, 54, 50], [23, 26, 30, 35, 38, 42, 47, 50], [54, 47, 50, 54, 59, 54, 50, 47], [19, 23, 26, 31, 35, 38, 43, 47], [50, 43, 47, 50, 55, 50, 47, 43], [21, 25, 28, 33, 37, 40, 45, 49], [52, 45, 49, 52, 57, 52, 49, 45], [26, 30, 33, 38, 42, 45, 50, 54], [57, 50, 54, 57, 62, 57, 54, 50], [23, 26, 30, 35, 38, 42, 47, 50], [54, 47, 50, 54, 59, 54, 50, 47], [19, 23, 26, 31, 35, 38, 43, 47], [50, 43, 47, 50, 55, 50, 47, 43], [21, 25, 28, 33, 37, 40, 45, 49], [52, 45, 49, 52, 57, 52, 49, 45], [38, 132, 45, 132, 50, 130, 52, 132], [54, 130, 45, 130, 50, 130, 52, 130], [35, 130, 42, 130, 47, 130, 49, 130], [50, 132, 130, 132, 130, 130, 132, 132], [31, 132, 38, 130, 43, 130, 45, 130], [47, 132, 132, 130, 50, 132, 132, 130], [33, 130, 40, 130, 45, 130, 47, 132], [49, 130, 132, 130, 47, 130, 130, 132], [38, 130, 45, 130, 50, 132, 52, 132], [50, 132, 130, 130, 132, 132, 132, 132], [35, 132, 42, 132, 47, 130, 49, 130], [50, 130, 132, 132, 132, 130, 132, 132], [31, 132, 38, 130, 43, 130, 45, 132], [47, 130, 132, 132, 50, 130, 130, 132], [33, 130, 40, 132, 45, 132, 47, 132], [49, 132, 130, 132, 47, 132, 132, 132], [38, 130, 45, 132, 50, 130, 52, 130], [54, 130, 130, 132, 130, 130, 132, 35]]
# tonality = 2


def xiaojie_tonality(bass_num, melody_num, tonality):
    tonality_list = []
    out_tonality = [1, 3, 6, 8, 10]
    all_out_tonality_note_num = [0 for i in range(0, len(bass_num))]
    change_tonality_list = []

    # 用来计数，每个小节离调音有多少，用来判断是不是曲子在这里变调了
    for i in range(0, len(bass_num)):
        for j in range(0, 24):
            if bass_num[i][j] < 100 and ((bass_num[i][j] - tonality) % 12) in out_tonality:
                all_out_tonality_note_num[i] += 1
                # if bass_num[i][j]  not in change_tonality_list:
                #     change_tonality_list.append(bass_num[i][j])
    for i in range(0, len(melody_num)):
        for j in range(0, 24):
            if melody_num[i][j] < 100 and ((melody_num[i][j] - tonality) % 12) in out_tonality:
                all_out_tonality_note_num[i] += 1
                # if melody_num[i][j] not in change_tonality_list:
                #     change_tonality_list.append(melody_num[i][j])

    # 把换调的那个小节的音用来备用，到达换调的那个小节的时候，就补上这些变调后的音
    change_tonality_batch_list = []
    for i in range(0, len(all_out_tonality_note_num)):
        if all_out_tonality_note_num[i] > 12:
            change_tonality_batch_list.append(i * 2)
            for j in range(0, len(melody_num[i])):
                if melody_num[i][j] not in change_tonality_list and melody_num[i][j] < 100:
                    change_tonality_list.append(melody_num[i][j])
    print('变调的可以变化的音: ', change_tonality_list)
    # print('变调的每个小节的其实offset是: ', change_tonality_batch_list)

    # 前者是按着这个list变调，后者是哪几个小节是变调小节
    return change_tonality_list, change_tonality_batch_list


def read_judgment_tonality(note_name, bass_name):
    stream1 = converter.parse(note_name)
    # 这个用来判断调性
    # 只存放存在的音的数字
    melody_tonality_note = []
    for i in range(0, 12):
        melody_tonality_note.append(0)

    # 读取整个midi乐谱
    for element in stream1.flat.getElementsByClass(["Note", "Chord"]):

        # 这个是判断是不是柱式和弦
        # 如果是单音
        num_notes_buffer = []
        if isinstance(element, note.Note):
            melody_tonality_note[note_name_2_num(str(element.pitch)) % 12] += 1
        # 如果是柱式和弦
        elif isinstance(element, chord.Chord):
            # 柱式和弦分两种，一种是旋律的柱式和弦，一种是和弦的柱式和弦
            chord_nums = [note_name_2_num(str(n.pitch)) for n in element]
            extreme_chord_num = min(chord_nums)
            melody_tonality_note[extreme_chord_num % 12] += 1

    stream2 = converter.parse(bass_name)
    # 读取整个midi乐谱
    for element in stream2.flat.getElementsByClass(["Note", "Chord"]):

        if isinstance(element, note.Note):
            melody_tonality_note[note_name_2_num(str(element.pitch)) % 12] += 1
        # 如果是柱式和弦
        elif isinstance(element, chord.Chord):
            # 柱式和弦分两种，一种是旋律的柱式和弦，一种是和弦的柱式和弦
            chord_nums = [note_name_2_num(str(n.pitch)) for n in element]
            extreme_chord_num = max(chord_nums)
            melody_tonality_note[extreme_chord_num % 12] += 1

    # 因为sort是指针操作，新创建一个用来比较
    raw_tonality_note = []
    for i in melody_tonality_note:
        raw_tonality_note.append(i)

    # 整理排序，挑出前7个数量最多的音
    melody_tonality_note.sort(reverse=1)
    # print(melody_tonality_note)
    this_song_tonality_note = []
    for k in range(0, 7):
        for j in range(0, len(raw_tonality_note)):
            if melody_tonality_note[k] == raw_tonality_note[j] and j not in this_song_tonality_note:
                this_song_tonality_note.append(j)
    this_song_tonality_note.sort()

    Tonalitydict = [
        [0, 2, 4, 5, 7, 9, 11], [0, 1, 3, 5, 6, 8, 9],
        [1, 2, 4, 6, 7, 9, 11], [0, 2, 3, 5, 7, 8, 10],
        [1, 3, 4, 6, 8, 9, 11],
        [0, 2, 4, 5, 7, 9, 10], [1, 3, 5, 6, 8, 10, 11],
        [0, 2, 4, 6, 7, 9, 11], [0, 1, 3, 5, 7, 8, 10],
        [1, 2, 4, 6, 8, 9, 11], [0, 2, 3, 5, 7, 9, 10],
        [1, 3, 4, 6, 8, 10, 11]
    ]

    tonality = 0
    print('this_song_tonality_note: ', this_song_tonality_note)
    if this_song_tonality_note in Tonalitydict:
        for i in range(0, len(Tonalitydict)):
            if this_song_tonality_note == Tonalitydict[i]:
                tonality = i
                print('该曲子调性是：', tonality)

    else:

        melody_tonality_note.sort(reverse=0)
        dif_out_tonality = []
        same_out_tonality = []
        for i in range(0, 12):
            if melody_tonality_note[0] == raw_tonality_note[i] and i not in dif_out_tonality:
                dif_out_tonality.append(i)
            if melody_tonality_note[1] == raw_tonality_note[i] and i not in dif_out_tonality:
                dif_out_tonality.append(i)
            if melody_tonality_note[2] == raw_tonality_note[i] and i not in dif_out_tonality:
                dif_out_tonality.append(i)
            if melody_tonality_note[3] == raw_tonality_note[i] and i not in dif_out_tonality:
                dif_out_tonality.append(i)

        for k in range(1, 5):
            for i in range(0, 12):
                if melody_tonality_note[-k] == raw_tonality_note[i]:
                    same_out_tonality.append(i)
        # print(raw_tonality_note, melody_tonality_note)
        # print(dif_out_tonality, same_out_tonality)

        for t in range(0, len(Tonalitydict)):
            # print(same_out_tonality[0])
            if same_out_tonality[0] in Tonalitydict[t] \
                    and same_out_tonality[1] in Tonalitydict[t] \
                    and same_out_tonality[2] in Tonalitydict[t] \
                    and same_out_tonality[3] in Tonalitydict[t] \
                    and dif_out_tonality[0] not in Tonalitydict[t] \
                    and dif_out_tonality[1] not in Tonalitydict[t] \
                    and dif_out_tonality[2] not in Tonalitydict[t] \
                    and dif_out_tonality[3] not in Tonalitydict[t]:
                print('有大量离调音，该曲子调性是：', t)
                tonality = t

    return tonality


def judgment_tonality(midi):
    # 所有的note放进一个统计用的list
    melody_tonality_note = []
    for i in range(0, 12):
        melody_tonality_note.append(0)

    # 读取所有的音符，然后%12，相当于归一化到一个12长度的list里
    for section in midi.base_splited_num_notes and midi.melody_splited_num_notes:
        for section_num in section:
            # print(sention_num)
            if section_num < 140:
                melody_tonality_note[section_num % 12] += 1
    # print(melody_tonality_note)

    # 因为sort是指针操作，新创建一个用来比较
    raw_tonality_note = []
    for i in melody_tonality_note:
        raw_tonality_note.append(i)

    # 整理排序，挑出前7个数量最多的音
    melody_tonality_note.sort(reverse=1)
    # print(melody_tonality_note)
    this_song_tonality_note = []
    for k in range(0, 7):
        for j in range(0, len(raw_tonality_note)):
            if melody_tonality_note[k] == raw_tonality_note[j] and j not in this_song_tonality_note:
                this_song_tonality_note.append(j)
    this_song_tonality_note.sort()

    Tonalitydict = [
        [0, 2, 4, 5, 7, 9, 11], [0, 1, 3, 5, 6, 8, 9],
        [1, 2, 4, 6, 7, 9, 11], [0, 2, 3, 5, 7, 8, 10],
        [1, 3, 4, 6, 8, 9, 11],
        [0, 2, 4, 5, 7, 9, 10], [1, 3, 5, 6, 8, 10, 11],
        [0, 2, 4, 6, 7, 9, 11], [0, 1, 3, 5, 7, 8, 10],
        [1, 2, 4, 6, 8, 9, 11], [0, 2, 3, 5, 7, 9, 10],
        [1, 3, 4, 6, 8, 10, 11]
    ]

    tonality = 0
    if this_song_tonality_note in Tonalitydict:
        for i in range(0, len(Tonalitydict)):
            if this_song_tonality_note == Tonalitydict[i]:
                tonality = i
                print('该曲子调性是：', tonality)

    else:

        melody_tonality_note.sort(reverse=0)
        dif_out_tonality = []
        same_out_tonality = []
        for i in range(0, 12):
            if melody_tonality_note[0] == raw_tonality_note[i] and i not in dif_out_tonality:
                dif_out_tonality.append(i)
            if melody_tonality_note[1] == raw_tonality_note[i] and i not in dif_out_tonality:
                dif_out_tonality.append(i)
            if melody_tonality_note[2] == raw_tonality_note[i] and i not in dif_out_tonality:
                dif_out_tonality.append(i)
            if melody_tonality_note[3] == raw_tonality_note[i] and i not in dif_out_tonality:
                dif_out_tonality.append(i)

        for k in range(1, 5):
            for i in range(0, 12):
                if melody_tonality_note[-k] == raw_tonality_note[i]:
                    same_out_tonality.append(i)
        # print(raw_tonality_note, melody_tonality_note)
        # print(dif_out_tonality, same_out_tonality)

        for t in range(0, len(Tonalitydict)):
            # print(same_out_tonality[0])
            if same_out_tonality[0] in Tonalitydict[t] \
                    and same_out_tonality[1] in Tonalitydict[t] \
                    and same_out_tonality[2] in Tonalitydict[t] \
                    and same_out_tonality[3] in Tonalitydict[t] \
                    and dif_out_tonality[0] not in Tonalitydict[t] \
                    and dif_out_tonality[1] not in Tonalitydict[t] \
                    and dif_out_tonality[2] not in Tonalitydict[t] \
                    and dif_out_tonality[3] not in Tonalitydict[t]:
                print('有大量离调音，该曲子调性是：', t)
                tonality = t
    return tonality

###################################################### 下面是测试用代码 ###########################################################

# MidiName = 'LiuXingDeYun_2'
#
# #这里修改要生成的谱子
# base_name = './chordlist/' + MidiName +'_base.mid'
# note_name = './chordlist/' + MidiName +'_note.mid'
#
#
# deltime = 0.25  # 一个小节按这个间隔时间分， 一个小节有几个音。一个小节是2， 2/0.25 = 8就是这个小节有8个音
#
# # Readmidi 这个类，传入三个参数，一个旋律的位置，一个和弦的位置，间隔时间多少（每小节多少音）。输入midi都是单音的，和弦和旋律分开成两个midi
# # 返回一个类，里面的数据就在下面print了
#
# midi = Readmidi(chord_file_name = base_name, melody_file_name = note_name, delta_time = deltime)
#
# tonality = judgment_tonality(midi)
#
# print('tonality : ', tonality)
