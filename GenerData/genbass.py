import random
import numpy as np
from tqdm import tqdm

import GenerData.tonality_judgment as tj
from GenerData.MusicDetailManager import MusicDetailManager
from GenerData.SettingManager import SettingsManager
from GenerData.bassclass import bass_class

def genbass(sm: SettingsManager,
            md: MusicDetailManager) -> list:
    music_bass = []

    bassclass = bass_class
    chapters_num = len(md.multi_root)
    multi_root = md.multi_root
    rythmlist = md.rythmlist
    # print('rythmlist: ', rythmlist)
    # 根音和谐音列表
    chordclass = sm.chordclass

    # 一共有多少个章节
    # print('len(bassclass[root]) ', len(bassclass[multi_root[0]]))
    # print('bassclass[root] ', bassclass[multi_root[0]])
    for i in range(chapters_num):
        root = multi_root[i]
        # print('bassclass[root]: ', bassclass[root])
        # 一个章节里面根音有多少个
        for j in range(0, len(bassclass[root])):
            # 一个根音带动16个0.25的音
            for k in range(0, 16):
                music_bass.append(130)

    # print('len(music_bass): ', len(music_bass))
    xiaojie2chapterlist = []  # 用来保存每个小节对应的章节的序号
    num = 0
    # 根音的高低
    if sm.heavyorlight == 0:
        # highlow = np.random.choice([0, 1], p=[0.3, 0.7])
        highlow = 0
    else:
        highlow = 1
    dianyinornot = sm.dianyinornot
    if dianyinornot:
        dianyinornot = np.random.choice([0, 1], p=[0.5, 0.5])
    # print('dianornot', dianyinornot)

    # 一共的章节数
    for i in range(chapters_num):
        # 和弦有两个点，一个节奏型，一个和弦走向
        # TODO: 这里节奏型和和弦走向都得重新设计。一个是随机生成，一个是找固定的
        # 一个章节选择一个节奏型
        rythm = rythmlist[i]
        # print('rythm: ', rythm)
        # 一个新的章节，重新定义和弦走向
        hexianzouxiang = []
        hexianzouxiang_type2 = []
        root = multi_root[i]
        # print(root, bassclass[root])

        # 用来解决 结构化bass
        risebefore = 0
        risebefore_type2 = 0
        hexianzouxiang.append(risebefore)
        hexianzouxiang_type2.append(risebefore_type2)

        # 有两种选项，一种是挑正常的和弦走向，就现成的，一种就随机走向
        # 这里一个m是那个节奏上有音，补走向
        for m in range(0, len(rythm)):

            # 这里要修改成概率
            # rise = random.randint(0, len(chordclass[0]) - 1)
            # # 让两个bass的音比较连贯一些，两个相邻的bass的音不能差太远
            # while abs(rise - risebefore) > 2:
            #     rise = random.randint(0, len(chordclass[0]) - 1)  # 走向的序号
            #
            # rise_range = [i for i in range(0, len(chordclass[0])) if abs(rise - i) < 3]
            # rise = random.choice(rise_range, 1)
            # # rise = random.choice([-1, 0, 1], p=[0.3, 0.2, 0.5]) +  risebefore # 走向的序号
            # risebefore = rise  # 备份上次的走向
            # hexianzouxiang.append(rise)

            rise_range = [i for i in range(0, len(chordclass[0])) if abs(risebefore - i) < 3]
            # print('rise_range', rise_range)
            if dianyinornot:
                rise = random.choice(rise_range)
            else:
                rise = 0

            risebefore = rise
            hexianzouxiang.append(rise)
            # print('hexianzouxiang', hexianzouxiang)
            rise_range_type2 = [i for i in range(0, len(chordclass[0])) if abs(risebefore_type2 - i) < 3]
            rise_type2 = random.choice(rise_range_type2)
            risebefore_type2 = rise_type2
            hexianzouxiang_type2.append(rise_type2)

        # print('rythm: ', rythm)
        # print('和弦走向: ', hexianzouxiang, '\nhexianzouxiang_type2: ', hexianzouxiang_type2)
        hiloran = np.random.randint(0, 2)
        if hiloran == 0:
            gaodizhangjie = 0 + highlow
        elif hiloran == 1:
            gaodizhangjie = 1 + highlow
        # print('len(bassclass[root]: ', len(bassclass[root]))

        # 一个章节里有几个根音
        for j in range(0, len(bassclass[root])):
            # print('j', j)
            # print('bassclass[root]', bassclass[root])
            chord = tj.chordtype(sm, bassclass[root][j])

            # 一个根音后面有几个衍生音
            for k in range(0, len(rythm)):
                # rootjiange每个音和根音的间隔 ，changenum是每个要改变的音的位置
                # print('k', k)
                if j < len(bassclass[root]) - 1:
                    rootjiange = chordclass[chord][hexianzouxiang[k]]
                else:
                    rootjiange = chordclass[chord][hexianzouxiang_type2[k]]

                # 保证第一个是根音，其实这个不是很必要# 2020814还是加上了
                if k == 0:
                    rootjiange = 0

                changenum = int(num + j * 16 + rythm[k] * 4)
                music_bass[changenum] = bassclass[root][j] + 12  + rootjiange + 12 * gaodizhangjie
        num += len(bassclass[root]) * 16

    # for i in range(16):
    #     music_bass.append(150)
    tonality = sm.tonality

    music_bass2rawtonality = [music_bass[i] + tonality for i in range(0, len(music_bass))]
    # print('len music bass: ', len(music_bass2rawtonality))
    splitbass = []
    eightbatchnum = int(len(music_bass2rawtonality)/8)

    for i in range(0, eightbatchnum):
        splitbass.append([])
        for j in range(0, 24):
            try:
                splitbass[i].append(int(music_bass2rawtonality[i*8+j]))
            except:
                splitbass[i].append(130)
    # print('splitbass: ', splitbass)

    return np.array(music_bass2rawtonality), splitbass


if __name__ == '__main__':
    singsong = 0
    chapters_num = 4
    # rootlist = []
    bassclasslist = []
    musicbasslist = []
    musicbasslen_list = []
    musicbass_rythmlist = []
    musicbasslen_rythmlist = []
    rootlist = []

    for i in range(1):
        # 这是生成一系列通用的参数
        sm = SettingsManager(
            root=None, root2=0, root3=0,
            drumclass=None, singsong=singsong, chapters_num=chapters_num,
            heavyorlight=None,
            bpm=100, tonality=0
        )

        # 这是生成一系列音乐详细的参数
        md = MusicDetailManager(sm)

        music_bass, splitbass = genbass(sm, md) # 24个音一个小batch
        # print('bass_class', bass_class[md.multi_root[0]])
        # print('md.rythmlist: ', md.rythmlist)
        # print('music_bass: ', music_bass)
        # rootlist.append(np.array(md.multi_root[0]))
        # print('music_bass: ', music_bass)

        short_music_bass = []
        short_music_bass_rythm = []
        for j, yin in enumerate(music_bass):
            if yin < 100:
                short_music_bass.append(yin)
                short_music_bass_rythm.append(j)

        while len(bass_class[md.multi_root[0]])<8:
            bass_class[md.multi_root[0]].append(np.random.randint(100, 130))

        # while len(short_music_bass) < 128:
        #     short_music_bass.append(130)
            # bbb = [np.array(), np.array(pad)]
        bassclasslist.append((bass_class[md.multi_root[0]]))
        musicbasslist.append((short_music_bass))
        musicbasslen_list.append(len(short_music_bass))

        musicbass_rythmlist.append((short_music_bass_rythm))
        musicbasslen_rythmlist.append(len(short_music_bass_rythm))
        rootlist.append([sm.root])



    music_bass_maxlenth = max(musicbasslen_list)
    for i, short_music_bass in enumerate(musicbasslist):
        while len(musicbasslist[i]) < music_bass_maxlenth:
            musicbasslist[i].append(130)

    music_bass_rythmmaxlenth = max(musicbasslen_rythmlist)
    for i, short_music_bass in enumerate(musicbass_rythmlist):
        while len(musicbass_rythmlist[i]) < music_bass_maxlenth:
            musicbass_rythmlist[i].append(130)

    for i, short_bassclass in enumerate(bassclasslist):
        while len(bassclasslist[i]) < music_bass_maxlenth:
            bassclasslist[i].append(np.random.randint(100, 130))

    for i, short_bassclass in enumerate(rootlist):
        while len(rootlist[i]) < music_bass_maxlenth:
            rootlist[i].append(np.random.randint(100, 130))

    np.save('data/root', np.array(rootlist))
    np.save('data/bassclass_short', np.array(bassclasslist))
    np.save('data/musicbass_short', np.array(musicbasslist))
    np.save('data/musicbass_rythmlist', np.array(musicbass_rythmlist))


    # aaaa = np.load('data/bassclass_short.npy')
    # print('load bassclass_short:', aaaa)
    # print('load bassclass_short:', aaaa.shape)
    # bbbb = np.load('data/musicbass_short.npy', allow_pickle=True)
    # print('load musicbass_short:', bbbb)
    # print('load musicbass_short:', bbbb.shape)
