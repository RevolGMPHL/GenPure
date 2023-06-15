import random

from tqdm import tqdm


def add_ShuiYin_2_wav(blank_wav, midi, instruments, sm, md):
    # instruments are bass
    Unittime = int((sm.fm.piano_source.length * (130 / sm.bpm)) / 16)
    zhangjie = 0
    kongbaistart = 0  # sm.fm.piano_source.length
    k = 0
    zhangjie_num = md.multi_root_charpter[k]
    xiuzhengdelay = 6614

    for xiaojie in tqdm(range(0, len(midi)), desc="贴水印进度: "):
        for yin in range(0, 8):
            start = int((xiaojie * 8 + yin) * Unittime) + kongbaistart
            zhangjiechange = 0

            # 计算当前这个音在那个章节里
            if xiaojie * 8 + yin >= zhangjie_num:
                zhangjie_num += md.multi_root_charpter[k]
                k += 1
                zhangjie += 1
                zhangjiechange = 1

            if zhangjiechange == 1:
                Shuiyin_note = sm.fm.Shuiyin_source.get(1) * 0.6
                blank_wav[start - 10000: (start + len(Shuiyin_note) - 10000)] += Shuiyin_note


# 16个0.25 = 一个81415，那么一个【】是8个0.25
def add_Rise_2_wav(blank_wav, midi, instruments, sm, md):
    # instruments are bass
    Unittime = int((sm.fm.piano_source.length * (130 / sm.bpm)) / 16)
    zhangjie = 0
    kongbaistart = 0  # sm.fm.piano_source.length
    k = 0
    zhangjie_num = md.multi_root_charpter[k]
    xiuzhengdelay = 6614

    for xiaojie in tqdm(range(0, len(midi)), desc="Rise进度: "):
        for yin in range(0, 8):
            start = int((xiaojie * 8 + yin) * Unittime) + kongbaistart
            zhangjiechange = 0

            # 计算当前这个音在那个章节里
            if xiaojie * 8 + yin >= zhangjie_num:
                zhangjie_num += md.multi_root_charpter[k]
                k += 1
                zhangjie += 1
                zhangjiechange = 1

            bellnote = random.randint(0, sm.fm.Bell_source.maximum + 1 + 10)  #
            if zhangjiechange == 1 and bellnote < sm.fm.Bell_source.maximum:
                Bell_note = sm.fm.Bell_source.get(bellnote) * 0.5
                blank_wav[start: (start + len(Bell_note))] += Bell_note

            if sm.bpm > 100:
                rise_type = random.randint(0, 5)
            else:
                rise_type = random.randint(0, 4)

            rise_zero_type = random.randint(0, 6)
            if zhangjiechange == 1 and rise_type == 0 and zhangjie < len(md.multi_root_charpter):
                if rise_zero_type == 0:  # zhangjie < len(instruments) - 2 and
                    Rise_note = sm.fm.Rise_0_source.get(0) * 0.4
                    Rise_note2 = sm.fm.Rise_0_source.get(1) * 0.4

                    blank_wav[(start - len(Rise_note)): (start)] += Rise_note
                    blank_wav[start: (start + len(Rise_note2))] += Rise_note2

                if rise_zero_type == 1:
                    Rise_note = sm.fm.Rise_0_source.get(2) * 0.3
                    blank_wav[(start - len(Rise_note)): (start)] += Rise_note

                    Rise_note2 = sm.fm.Rise_0_source.get(3) * 0.6
                    blank_wav[start: (start + len(Rise_note2))] += Rise_note2

                if rise_zero_type == 2:
                    Rise_note = sm.fm.Rise_0_source.get(4) * 0.1
                    blank_wav[(start - len(Rise_note)): (start)] += Rise_note

                    Rise_note2 = sm.fm.Rise_0_source.get(5) * 0.1
                    blank_wav[start: (start + len(Rise_note2))] += Rise_note2

                if rise_zero_type == 3:
                    Rise_note = sm.fm.Rise_0_source.get(6) * 0.4
                    blank_wav[(start - len(Rise_note)): (start)] += Rise_note

                    Rise_note2 = sm.fm.Rise_0_source.get(7) * 0.4
                    blank_wav[start: (start + len(Rise_note2))] += Rise_note2

                if rise_zero_type == 4:
                    Rise_note = sm.fm.Rise_0_source.get(8) * 0.4
                    blank_wav[(start - len(Rise_note)): (start)] += Rise_note

                    Rise_note2 = sm.fm.Rise_0_source.get(9) * 0.4
                    blank_wav[start: (start + len(Rise_note2))] += Rise_note2

                if rise_zero_type == 5:
                    Rise_note = sm.fm.Rise_0_source.get(10) * 0.4
                    blank_wav[(start - len(Rise_note)): (start)] += Rise_note

                    Rise_note2 = sm.fm.Rise_0_source.get(11) * 0.4
                    blank_wav[start: (start + len(Rise_note2))] += Rise_note2

                if rise_zero_type == 6:
                    Rise_note = sm.fm.Rise_0_source.get(12) * 0.4
                    blank_wav[(start - len(Rise_note)): (start)] += Rise_note

                    Rise_note2 = sm.fm.Rise_0_source.get(13) * 0.4
                    blank_wav[start: (start + len(Rise_note2))] += Rise_note2

            if zhangjiechange == 1 and rise_type == 1:
                riseramdom = random.randint(0, 36) * 2
                Rise_note = sm.fm.Rise_1_source.get(9 + riseramdom) * 0.15
                blank_wav[(start - len(Rise_note)): (start)] += Rise_note
                Rise_note2 = sm.fm.Rise_1_source.get(10 + riseramdom) * 0.15
                blank_wav[start: (start + len(Rise_note2))] += Rise_note2
