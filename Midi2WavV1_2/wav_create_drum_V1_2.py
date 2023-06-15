import random

import numpy as np
from scipy.io import wavfile
from tqdm import tqdm

import GenerData.MusicDetailManager as MD
import GenerData.SettingManager as SM
import drum as drum
import GenerData.genbass as Genbass


# 16个0.25 = 一个81415，那么一个【】是8个0.25
def add_drum_2_wav(blank_wav, midi, sm, md):
    # instruments are bass
    Unittime = int((sm.fm.piano_source.length * (130 / sm.bpm)) / 16)
    zhangjie = 0
    kongbaistart = 0  # sm.fm.piano_source.length
    k = 0
    zhangjie_num = md.multi_root_charpter[k]

    for xiaojie in tqdm(range(0, len(midi)), desc='drum wav: '):
        for yin in range(0, 8):
            start = int((xiaojie * 8 + yin) * Unittime) + kongbaistart
            zhangjiechange = 0
            # 计算当前这个音在那个章节里
            # zhangjie 会比 charpternum多一个，比如charpter是16，len(root)=16,但是章节是0-16
            if xiaojie * 8 + yin >= zhangjie_num:
                zhangjie_num += md.multi_root_charpter[k]
                k += 1
                zhangjie += 1
                zhangjiechange = 1

            # drumlist_num[1][0], 第一个数字决定哪种鼓，第二个决定鼓的节奏
            # drumclass = sm.drumclass
            if zhangjie < len(md.multi_root_charpter) - 1:
                drumclass = md.drumclasslist[zhangjie]
            else:
                drumclass = -2
            if zhangjiechange == 1 and drumclass > 0:
                drumrythmtype = random.randint(0, len(drum.drumlist_num[drumclass]) - 1)
                # 这套鼓有多少个音
                drumlen = len(drum.drumlist[drum.drumlist_num[drumclass][drumrythmtype]])

                # 一个章节里面，有几套鼓
                zhangjiedrumnum = int(
                    md.multi_root_charpter[zhangjie] / len(drum.drumlist[drum.drumlist_num[drumclass][drumrythmtype]]))
                for j in range(0, zhangjiedrumnum):
                    for i in range(0, drumlen):
                        # 一个音有多少个鼓
                        for k in range(0, len(drum.drumlist[drum.drumlist_num[drumclass][drumrythmtype]][i])):
                            drum_note_num = drum.drumlist[drum.drumlist_num[drumclass][drumrythmtype]][i][k]

                            try:

                                if drum_note_num < 90 and drumclass == 0:
                                    FireflyDrum_note = sm.fm.FireflyDrum_D_0_source.get(
                                        drum_note_num) * random.uniform(0.999, 1) * 0.4
                                    blank_wav[(start + Unittime * len(
                                        drum.drumlist[
                                            drum.drumlist_num[drumclass][drumrythmtype]]) * j + Unittime * i + 300): (
                                                      start + Unittime * len(
                                                  drum.drumlist[drum.drumlist_num[drumclass][drumrythmtype]]) * j + len(
                                                  FireflyDrum_note) + Unittime * i + 300)] += FireflyDrum_note

                                elif drum_note_num < 90 and drumclass == 1:
                                    RefrainDrum_note = sm.fm.RefrainDrum_D_1_source.get(drum_note_num) * random.uniform(
                                        0.999,
                                        1) * 1.2
                                    blank_wav[(start + Unittime * len(
                                        drum.drumlist[
                                            drum.drumlist_num[drumclass][drumrythmtype]]) * j + Unittime * i): (
                                                      start + Unittime * len(
                                                  drum.drumlist[drum.drumlist_num[drumclass][drumrythmtype]]) * j + len(
                                                  RefrainDrum_note) + Unittime * i)] += RefrainDrum_note


                                elif drum_note_num < 90 and drumclass == 2:
                                    ContinueVoyageDrum_note = sm.fm.ContinueVoyageDrum_D_2_source.get(
                                        drum_note_num) * random.uniform(0.999, 1) * 0.4
                                    blank_wav[(start + Unittime * len(
                                        drum.drumlist[
                                            drum.drumlist_num[drumclass][drumrythmtype]]) * j + Unittime * i): (
                                                      start + Unittime * len(
                                                  drum.drumlist[drum.drumlist_num[drumclass][drumrythmtype]]) * j + len(
                                                  ContinueVoyageDrum_note) + Unittime * i)] += ContinueVoyageDrum_note

                                elif drum_note_num < 90 and drumclass == 3:
                                    CANDrum_note = sm.fm.CANDrum_D_3_source.get(drum_note_num) * random.uniform(0.999,
                                                                                                                1) * 0.45
                                    blank_wav[(start + Unittime * len(
                                        drum.drumlist[
                                            drum.drumlist_num[drumclass][drumrythmtype]]) * j + Unittime * i): (
                                                      start + Unittime * len(
                                                  drum.drumlist[drum.drumlist_num[drumclass][drumrythmtype]]) * j + len(
                                                  CANDrum_note) + Unittime * i)] += CANDrum_note

                                elif drum_note_num < 90 and drumclass == 4:
                                    BingDrum_note = sm.fm.BingDrum_D_4_source.get(drum_note_num) * random.uniform(0.999,
                                                                                                                  1) * 0.45
                                    blank_wav[(start + Unittime * len(
                                        drum.drumlist[
                                            drum.drumlist_num[drumclass][drumrythmtype]]) * j + Unittime * i): (
                                                      start + Unittime * len(
                                                  drum.drumlist[drum.drumlist_num[drumclass][drumrythmtype]]) * j + len(
                                                  BingDrum_note) + Unittime * i)] += BingDrum_note
                                elif drum_note_num < 90 and drumclass == 5:
                                    NianDrum_note = sm.fm.NianDrum_D_5_source.get(drum_note_num) * random.uniform(0.999,
                                                                                                                  1) * 0.8
                                    blank_wav[(start + Unittime * len(
                                        drum.drumlist[
                                            drum.drumlist_num[drumclass][drumrythmtype]]) * j + Unittime * i): (
                                                      start + Unittime * len(
                                                  drum.drumlist[drum.drumlist_num[drumclass][drumrythmtype]]) * j + len(
                                                  NianDrum_note) + Unittime * i)] += NianDrum_note
                                elif drum_note_num < 90 and drumclass == 6:
                                    TingDrum_note = sm.fm.TingDrum_D_6_source.get(drum_note_num) * random.uniform(0.999,
                                                                                                                  1) * 0.4
                                    blank_wav[(start + Unittime * len(
                                        drum.drumlist[
                                            drum.drumlist_num[drumclass][drumrythmtype]]) * j + Unittime * i): (
                                                      start + Unittime * len(
                                                  drum.drumlist[drum.drumlist_num[drumclass][drumrythmtype]]) * j + len(
                                                  TingDrum_note) + Unittime * i)] += TingDrum_note

                                elif drum_note_num < 90 and drumclass == 7:
                                    WuxinDrum_note = sm.fm.WuxinDrum_D_7_source.get(drum_note_num) * random.uniform(
                                        0.999,
                                        1) * 0.35
                                    blank_wav[(start + Unittime * len(
                                        drum.drumlist[
                                            drum.drumlist_num[drumclass][drumrythmtype]]) * j + Unittime * i): (
                                                      start + Unittime * len(
                                                  drum.drumlist[drum.drumlist_num[drumclass][drumrythmtype]]) * j + len(
                                                  WuxinDrum_note) + Unittime * i)] += WuxinDrum_note

                                elif drum_note_num < 90 and drumclass == 8:
                                    WuHouDrum_note = sm.fm.WuHouDrum_D_8_source.get(drum_note_num) * random.uniform(
                                        0.999,
                                        1) * 0.5
                                    blank_wav[(start + Unittime * len(
                                        drum.drumlist[
                                            drum.drumlist_num[drumclass][drumrythmtype]]) * j + Unittime * i): (
                                                      start + Unittime * len(
                                                  drum.drumlist[drum.drumlist_num[drumclass][drumrythmtype]]) * j + len(
                                                  WuHouDrum_note) + Unittime * i)] += WuHouDrum_note

                                elif drum_note_num < 90 and drumclass == 9:
                                    XueyueHuaDrum_note = sm.fm.XueyueHuaDrum_D_9_source.get(
                                        drum_note_num) * random.uniform(
                                        0.8,
                                        1) * 0.8
                                    if len(blank_wav[(start + Unittime * len(
                                            drum.drumlist[
                                                drum.drumlist_num[drumclass][drumrythmtype]]) * j + Unittime * i): (
                                            start + Unittime * len(
                                        drum.drumlist[drum.drumlist_num[drumclass][drumrythmtype]]) * j + len(
                                        XueyueHuaDrum_note) + Unittime * i)]) == len(XueyueHuaDrum_note):
                                        blank_wav[(start + Unittime * len(
                                            drum.drumlist[
                                                drum.drumlist_num[drumclass][drumrythmtype]]) * j + Unittime * i): (
                                                          start + Unittime * len(
                                                      drum.drumlist[
                                                          drum.drumlist_num[drumclass][drumrythmtype]]) * j + len(
                                                      XueyueHuaDrum_note) + Unittime * i)] += XueyueHuaDrum_note
                            except Exception as e:
                                print('add drum exception: ', e)


def add_drum_midi_2_wav(blank_wav, midi, sm, md):
    # instruments are bass
    Unittime = int((sm.fm.piano_source.length * (130 / sm.bpm)) / 16)
    kongbaistart = 0  # sm.fm.piano_source.length

    k = 0
    zhangjie = 0
    zhangjiechange = 0
    zhangjie_num = md.multi_root_charpter[k]
    drumtype = sm.drumtype

    for xiaojie in tqdm(range(0, len(midi)), desc='drum midi wav: '):
        zhangjiechange = 0
        # 计算当前这个音在那个章节里
        if xiaojie * 8 > zhangjie_num:
            zhangjie_num += md.multi_root_charpter[k]
            k += 1
            zhangjie += 1
            zhangjiechange = 1

            start = int((xiaojie * 8) * Unittime) + kongbaistart

            drumrythmtype = random.randint(0, len(drumtype) - 1)
            try:
                # 计算当前这个音在那个章节里
                changdu = len(sm.bassclass[md.multi_root[zhangjie]])
            except:
                print('zhangjie', zhangjie)
                # print('md.multi_root[zhangjie]', md.multi_root[zhangjie])
                # print('sm.bassclass[md.multi_root[zhangjie]]', sm.bassclass[md.multi_root[zhangjie]])

            if changdu == 4:
                setdrum = 1
            elif changdu == 8:
                setdrum = 2
            else:
                setdrum = 0

            if setdrum == 1:
                for yin in range(len(drumtype[drumrythmtype])):
                    for i in range(len(drumtype[drumrythmtype][yin])):
                        drum_note_num = drumtype[drumrythmtype][yin][i]
                        if drum_note_num < 100 and sm.drum_Music_type == 0:
                            Drum_note = sm.fm.BiosDrum_D_10_source.get(drum_note_num) * 0.4
                            blank_wav[(start + Unittime * yin): (
                                    start + len(Drum_note) + Unittime * yin)] += Drum_note
                        if drum_note_num < 100 and sm.drum_Music_type == 1:
                            # Drum_note = sm.fm.NianDrum_D2_5_source.get(drum_note_num) * 0.4
                            # blank_wav[(start + Unittime * yin): (
                            #         start + len(Drum_note) + Unittime * yin)] += Drum_note
                            Drum_note = sm.fm.WuxinDrum_D2_7_source.get(drum_note_num) * 0.4
                            blank_wav[(start + Unittime * yin): (
                                    start + len(Drum_note) + Unittime * yin)] += Drum_note
                        if drum_note_num < 100 and sm.drum_Music_type == 2:
                            Drum_note = sm.fm.WuxinDrum_D2_7_source.get(drum_note_num) * 0.4
                            blank_wav[(start + Unittime * yin): (
                                    start + len(Drum_note) + Unittime * yin)] += Drum_note

            elif setdrum == 2:  # 因为一个midi只覆盖了一个64的音，如果是一个root有8个音，就要重复一遍鼓的midi
                for yin in range(len(drumtype[drumrythmtype])):
                    for i in range(len(drumtype[drumrythmtype][yin])):
                        drum_note_num = drumtype[drumrythmtype][yin][i]
                        if drum_note_num < 100 and sm.drum_Music_type == 0:
                            Drum_note = sm.fm.BiosDrum_D_10_source.get(drum_note_num) * 0.4
                            try:
                                blank_wav[(start + Unittime * yin): (
                                        start + len(Drum_note) + Unittime * yin)] += Drum_note
                                blank_wav[(start + Unittime * yin + 64 * Unittime): (
                                        start + len(Drum_note) + Unittime * yin + 64 * Unittime)] += Drum_note
                            except:
                                pass
                        if drum_note_num < 100 and sm.drum_Music_type == 1:
                            # Drum_note = sm.fm.NianDrum_D2_5_source.get(drum_note_num) * 0.4
                            # blank_wav[(start + Unittime * yin): (
                            #         start + len(Drum_note) + Unittime * yin)] += Drum_note
                            # blank_wav[(start + Unittime * yin + 64 * Unittime): (
                            #         start + len(Drum_note) + Unittime * yin + 64 * Unittime)] += Drum_note
                            try:
                                Drum_note = sm.fm.WuxinDrum_D2_7_source.get(drum_note_num) * 0.4
                                blank_wav[(start + Unittime * yin): (
                                        start + len(Drum_note) + Unittime * yin)] += Drum_note
                                blank_wav[(start + Unittime * yin + 64 * Unittime): (
                                        start + len(Drum_note) + Unittime * yin + 64 * Unittime)] += Drum_note
                            except:
                                pass
                        if drum_note_num < 100 and sm.drum_Music_type == 2:
                            try:
                                Drum_note = sm.fm.WuxinDrum_D2_7_source.get(drum_note_num) * 0.4
                                blank_wav[(start + Unittime * yin): (
                                        start + len(Drum_note) + Unittime * yin)] += Drum_note
                                blank_wav[(start + Unittime * yin + 64 * Unittime): (
                                        start + len(Drum_note) + Unittime * yin + 64 * Unittime)] += Drum_note
                            except:
                                pass

    return blank_wav


def random_int_list(start, stop, length):
    start, stop = (int(start), int(stop)) if start <= stop else (int(stop), int(start))
    length = int(abs(length)) if length else 0
    random_list = []
    for i in range(length):
        random_list.append(random.randint(start, stop))
    return random_list


if __name__ == '__main__':
    singsong = 0
    chapters_num = 12

    # 这是生成一系列通用的参数
    sm = SM.SettingsManager(
        root=None, root2=None, root3=None, hexiantype=None,
        drumclass=None, singsong=singsong, chapters_num=chapters_num,
        heavyorlight=None,
        bpm=None, tonality=None
    )
    # 这是生成一系列音乐详细的参数
    md = MD.MusicDetailManager(sm)
    # 生成bass
    music_bass = Genbass.genbass(sm, md)  # 24个音一个小batch
    timelength = len(music_bass)
    blanklenth = (timelength / 2 * 81415 * 130 / sm.bpm) // 81415
    # print('blanklenth: ', blanklenth, timelength/2)
    output_wav = np.tile(sm.fm.piano_source.none, int(blanklenth + sm.blank_len_after)).T

    add_drum_midi_2_wav(output_wav, music_bass, sm, md)
    # add_drum_2_wav(output_wav, music_bass, sm, md)

    wavfile.write('outmelo.wav', sm.sample_rate, output_wav)
