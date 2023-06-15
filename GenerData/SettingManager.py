import os

import numpy as np
from scipy import stats

import GenerData.read_midi as read_midi
from GenerData.FileManager import FileManager
from GenerData.bassclass import bass_class

class SettingsManager:


    # 16个0.25音
    rythmclass = [
        [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5],  # two step

        [0, 0.25, 0.5, 0.75, 1.0, 1.5, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75],  # two step

        [0, 0.5, 1.0, 1.25, 1.5, 1.75, 2.5, 3.0, 3.5], [0, 0.5, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0],  # 稻香

        [0, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.75, 3, 3.25, 3.5, 3.75],  # two step

        [0, 1, 2.0, 2.5, 3.0, 3.5, ], [0, 1.0, 2.0, 2.5, 3.0, ],  # 稻香 # [0.0, 1.0, 2.0],

        [0, 0.5, 1.0, 1.5, 2.0], [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0], [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5],

        [0, 0.5, 0.75, 1.25, 1.5, 2, ], [0, 0.5, 0.75, 1.5, 2, 2.5, 2.75, 3.5], [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0],

        [0, 0.5, 1.0, 1.5, 2, 2.5, 3, ],
        # [0, 0.5, 0.75, 1.25, 1.5, 2, 2.25, 2.5, 2.75, 3, 3.25,  3.5],
        [0, 0.75, 1.5, 2], [0, 0.75, 1.5, 2, 2.5, 2.75, 3], [0, 0.75, 1.5, 2, 2.5, 2.75, 3], [0, 0.75, 1.5, 2.25, 3],

        [0, 1, 1.5, 3, ], [0, 1, 1.75, 2, 2.5, 3], [0, 1, 2, 3, ], [0, 1, 2, 2.5, 3],

        [0, 1.25, 2.5, 3],

        [0, 1.5, 3], [0, 1.5, 2, 3], [0, 1.5, 2, 2.5, 3, 3.5], [0, 1.5, 2, 3], [0, 1.5, 2.5, 3], [0, 1.5, 2.5, 3],

        [0, 2, ],  # two step

        [0, 2, 3], [0, 2, 3.5],

        [0, 3],  # s四月
    ]
    rythmclass_minyao = [

        [0, 0.5, 1.0, 1.25, 1.5, 1.75, 2.5, 3.0, 3.5], [0, 0.5, 1.0, 1.25, 1.5, 2.0, 2.5, 3.0],  # 稻香

        [0, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 2.75, 3, 3.25, 3.5, 3.75],  # two step

        [0, 0.5, 1, 1.5, 2.0, 2.25, 2.5, 2.75, 3.0, 3.25, 3.5, 3.75],

        [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0], [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5],

        [0, 0.5, 0.75, 1.5, 2, 2.5, 2.75, 3.5], [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0],

        [0, 0.25, 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.5],

        [0, 0.75, 1.5, 2, 2.5, 2.75, 3], [0, 0.75, 1.5, 2, 2.5, 2.75, 3],

    ]

    # 给bass用的节奏型
    bassrythmclass = [
        [0, 1.5, 2, 3.5], [0, 3, ],  # 稻香
    ]

    chordclass = [[0, 4, 7, 12, 16, 19, 24], [0, 3, 7, 12, 15, 19, 24], [0, 3, 6, 12, 15, 18, 24],
                  [0, 4, 7, 11, 12, 16, 19, 23], [0, 4, 7, 10, 12, 16, 19, 22], [0, 3, 7, 10, 12, 15, 19, 22],
                  [0, 3, 6, 10, 12, 15, 18, 22]]  # D, E, A # D=2 E=4 A=9

    def __init__(self,
                 root=None, root2=None, root3=None,
                 drumclass=None, singsong=0, chapters_num=12,
                 heavyorlight=None,
                 bpm=None, tonality=None,dianyinornot=0,fdmj=0,
                 pure_power=None, voice_power=None
                 ):

        # 决定了和弦的类型
        self.singsong = singsong
        self.blank_len_after = 6
        self.addmelodyornot = 1
        self.sample_rate = 44100
        is_power_in_range = lambda power: power is not None and 0 < power < 2
        self.pure_power = pure_power if is_power_in_range(pure_power) else 0.5
        self.voice_power = voice_power if is_power_in_range(voice_power) else 0.6
        root_range = range(0, len(bass_class))
        self.root = root if root in root_range else np.random.choice(root_range)
        self.bassclass = bass_class
        self.dianyinornot = dianyinornot
        self.fdmj = fdmj
        # self.root = random.randint(0, len(self.bassclass) - 1) if root is None else root
        if np.random.choice([0.5, 0.5], p=[0, 1]):
            self.root2 = root2 if root2 in root_range else np.random.choice(root_range)
        else:
            self.root2 = self.root

        if np.random.choice([0.7, 0.3], p=[0, 1]):
            self.root3 = root3 if root3 in root_range else np.random.choice(root_range)
        else:
            self.root3 = self.root
        # self.root2 = self.root
        # self.root3 = self.root
        # self.root2 = random.randint(0, len(self.bassclass) - 1) if root2 is None else root2
        # print('sm root: ', self.root)
        # print('sm root2: ', self.root2)
        # print('sm root3: ', self.root3)

        self.heavyorlight = heavyorlight if heavyorlight in [0, 1] else np.random.choice([0, 1], p=[0.5, 0.5])
        # if self.heavyorlight == 0:
        #     print('sm heavyorlight: light')
        # elif self.heavyorlight == 1:
        #     print('sm heavyorlight: heavy')

        drumclass_range = range(0, 13)  # range(0, 10)#drum数量（0-N）的 N+1，比如最大D9，那这个右边就写10
        self.drumclass = drumclass if drumclass in drumclass_range else np.random.choice(drumclass_range)
        print('sm drumclass: ', self.drumclass)

        # bpm_range, bpm_rate = get_Gaussian_curve(Gausslenth=65, Gaussmean=0.5, Variance=0.5, start=45)
        self.bpm = bpm # if bpm in bpm_range else np.random.choice(bpm_range, p=bpm_rate)

        # 决定了整首曲子的调性
        # tonality_range = range(0, 11)
        self.tonality = tonality #if tonality in tonality_range else np.random.choice(tonality_range)
        # self.tonality = random.randint(0, 11) if tonalidy is None else tonalidy
        # print('sm tonality: ', self.tonality)

        self.rythmshortlist = []
        self.rythmlonglist = []
        for i in range(4):
            self.rythm = self.rythmclass[np.random.randint(0, len(self.rythmclass) - 1)]
            self.rythm_start = self.rythmclass[np.random.randint(0, len(self.rythmclass) - 1)]

            while len(self.rythm) < 5:
                self.rythm = self.rythmclass[np.random.randint(0, len(self.rythmclass) - 1)]
            while len(self.rythm_start) >= 5:
                self.rythm_start = self.rythmclass[np.random.randint(0, len(self.rythmclass) - 1)]
            self.rythmshortlist.append(self.rythm_start)
            self.rythmlonglist.append(self.rythm)

        self.max_bass_instrument_num = 50  # 10+10+1# 一共有几种乐器用来演奏bass  第一个数字是只用在bass的乐器有多少，第二个数字是note和bass都有的乐器有几个
        self.max_note_instrument_num = 57  # 35  # 10+13+1# 一共有几种乐器用来演奏note  第一个数字是只用在note的乐器有多少，第二个数字是note和bass都有的乐器有几个

        self.max_fd_bass_instrument_num = 13
        self.max_fd_note_instrument_num = 20

        self.max_mj_note_instrument_num = 10

        self.max_pad_note_instrument_num = 13

        self.hexiantype = 0

        # 获得复调旋律和bass的两个乐器
        self.fd_instrument_bass = []
        self.fd_instrument_note = []
        self.fd_instrument_bass.append(
            np.random.randint(-self.max_fd_bass_instrument_num // 4, self.max_fd_bass_instrument_num))
        self.fd_instrument_bass.append(
            np.random.randint(-self.max_fd_bass_instrument_num // 4, self.max_fd_bass_instrument_num))
        self.fd_instrument_note.append(
            np.random.randint(-self.max_fd_note_instrument_num // 4, self.max_fd_note_instrument_num))
        self.fd_instrument_note.append(
            np.random.randint(-self.max_fd_note_instrument_num // 4, self.max_fd_note_instrument_num))

        # 获得模进的两个乐器
        self.mj_instrument_note = []
        self.mj_instrument_note.append(
            np.random.randint(-self.max_mj_note_instrument_num // 4, self.max_mj_note_instrument_num))
        self.mj_instrument_note.append(
            np.random.randint(-self.max_mj_note_instrument_num // 4, self.max_mj_note_instrument_num))

        # 获得模进的两个乐器
        self.pad_instrument_note = []
        self.pad_instrument_note.append(
            np.random.randint(-1, self.max_pad_note_instrument_num))
        self.pad_instrument_note.append(
            np.random.randint(-1, self.max_pad_note_instrument_num))

        self.chapters_num = chapters_num
        self.bpm = bpm
        # print('sm chapters_num: ', self.chapters_num)
        # print('sm bpm: ', self.bpm)

        self.fm = FileManager(setting_stamp='r' + str(self.root) + #'r2' + str(self.root2) + 'r3' + str(self.root3)
                                            't' + str(self.tonality) +
                                            'b' + str(self.bpm) + 'd' + str(self.drumclass))
        # if self.singsong == 1 :
        #     self.chapters_num, self.lyric_batch_len = DL.deal_with_lyric_part1()
        #     self.bpm = int(300 * 16 * 130 / (chapters_num * 64 * 6 * 1.84))
        # else:

        # 这里是ban掉一些bpm太快的，这里bpm太高的话，一些乐器是不能用的，得改这个方法。
        if self.bpm > 110:
            self.ban = [12, 13, 17, 18, 19, 22]
        else:
            # self.ban = [12, 13, 17, 18, 19]
            self.ban = []

        self.drumtype = []
        self.drum_Music_type = np.random.choice(range(0, 2))  # 0  #
        self.readmidi4drumlist(self.drum_Music_type)  # 把这首歌的bass存进basslist里
        # print('sm drum_Music_type: ', self.drum_Music_type)
        # print('sm drumtype: ', np.array(self.drumtype).shape)

    def readmidi4drumlist(self, bass_drum_type):
        base_path = os.path.abspath(os.path.dirname(__file__))
        # print('sm base_path', base_path)
        if bass_drum_type == 0:
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios01.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios02.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios03.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios04.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios05.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios06.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios07.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios08.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios09.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios10.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios11.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios12.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios13.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios14.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios15.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios16.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios17.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios18.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios19.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios20.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios21.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios22.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios23.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios24.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios25.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios26.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/bios/bios27.mid')))  # 4

        if bass_drum_type == 1:
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/Nian/Nian01.mid')))  # 0

        if bass_drum_type == 2:
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/Wuxin/Wuxin01.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/Wuxin/Wuxin02.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/Wuxin/Wuxin03.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/Wuxin/Wuxin04.mid')))  # 4
            self.drumtype.append(self.readmididrum(os.path.join(base_path, 'DrumMidi/Wuxin/Wuxin05.mid')))  # 4

    def readmididrum(self, midiname):
        bass1 = read_midi.ParseMidi(midiname, delta_time=0.25, tonality=0,
                                    melody_or_base='melody', train_or_run_or_wav='drum', note_or_chord='chord')
        # print('drumbass: ', bass1.splitted_num_notes)
        return bass1.splitted_num_notes


# 得到一个高斯的概率分布
# 输入参数是：
# Gausslenth：整个高斯X的点有几个
# Gaussmean，Variance：是高斯的中值和方差
# start：是高斯左端的开始点
def get_Gaussian_curve(Gausslenth=65, Gaussmean=0.30, Variance=0.4, start=55):
    x = np.linspace(0, 1, Gausslenth)
    mean = Gaussmean
    standard_devation = Variance
    norm = stats.norm(mean, standard_devation)
    y = norm.pdf(x) / norm.pdf(0)
    Gauss_rate = np.exp(y) / sum(np.exp(y))
    Gaussrange = start + np.arange(0, Gausslenth)

    return Gaussrange, Gauss_rate
