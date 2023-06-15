import numpy as np
import GenerData.generate_instruments as GIns
from GenerData.SettingManager import SettingsManager
from GenerData.bassclass import bass_class


class MusicDetailManager:

    def __init__(self,
                 sm: SettingsManager,
                 melo_instruments: list = None, bass_instruments: list = None):

        singsong = sm.singsong
        chapters_num = sm.chapters_num
        root = sm.root
        root2 = sm.root2
        root3 = sm.root3
        drumclass = sm.drumclass
        rythm = sm.rythm
        rythm_start = sm.rythm_start


        # print('rythm: ', rythm)
        # print('rythm_start: ', rythm_start)
        ban = sm.ban
        fd_instrument_bass = sm.fd_instrument_bass
        fd_instrument_note = sm.fd_instrument_note
        mj_instrument_note = sm.mj_instrument_note
        pad_instrument_note = sm.pad_instrument_note
        max_bass_instrument_num = sm.max_bass_instrument_num
        max_note_instrument_num = sm.max_note_instrument_num
        # print('chapters_num: ', chapters_num)


        self.multi_root = []

        self.rannoteinstru_num = np.random.randint(1, 3)  # 这个应该是每个章节选择乐器的数量
        self.ranbassinstru_num = np.random.randint(1, 3)

        ###################################################################################################
        ###################################################################################################
        # TODO：另外四种乐器的保存
        self.drumclasslist = []

        self.fd_instrument_bass_list = []
        self.fd_instrument_note_list = []
        self.mj_instrument_note_list = []
        self.pad_instrument_note_list = []

        # 每个章节有多少个音
        self.multi_root_charpter = []
        self.rythmlist = []
        for i in range(chapters_num):
            self.fd_instrument_bass_list.append(fd_instrument_bass[np.random.randint(0, 2)])
            self.fd_instrument_note_list.append(fd_instrument_note[np.random.randint(0, 2)])
            self.mj_instrument_note_list.append(mj_instrument_note[np.random.randint(0, 2)])
            self.pad_instrument_note_list.append(pad_instrument_note[np.random.randint(0, 2)])
            if drumclass >2:
                drumclass -= 3
            self.drumclasslist.append(np.random.choice([-2, drumclass], p=[0.5, 0.5]))

        # print('\nfd_instrument_bass_list   ', len(self.fd_instrument_bass_list),
        #       '\n', self.fd_instrument_bass_list)
        # print('fd_instrument_note_list   ', len(self.fd_instrument_note_list),
        #       '\n', self.fd_instrument_note_list)
        # print('mj_instrument_note_list   ', len(self.mj_instrument_note_list),
        #       '\n', self.mj_instrument_note_list)
        # print('pad_instrument_note_list   ', len(self.pad_instrument_note_list),
        #       '\n', self.pad_instrument_note_list)
        if self.drumclasslist[0] > 0:
            self.drumclasslist[0] = -2
        # print('\ndrumclasslist: ', self.drumclasslist)

        # 这里修改乐器列表
        self.base_instruments_set = range(0, max_bass_instrument_num)  # 这里是取全部
        self.melody_instruments_set = range(0, max_note_instrument_num)
        self.melody_instruments_set = [i for i in self.melody_instruments_set if i not in ban]

        self.multi_instrument_bass_new, self.multi_instrument_melody_new, self.sing_instrument_new = \
            GIns.get_instrument_list(chapters_num, self.melody_instruments_set, self.base_instruments_set,
                                     self.drumclasslist)
        # print('ins: ', instruments)
        if melo_instruments is not None:
            assert len(melo_instruments) == chapters_num
            self.multi_instrument_melody_new = melo_instruments
        if bass_instruments is not None:
            assert len(bass_instruments) == chapters_num
            self.multi_instrument_bass_new = bass_instruments
        # 根据乐器来拼wav，之前是通过时间
        # 用来存放一共用到了什么乐器
        self.Melody_Allinstrumentslist = []
        for i in range(len(self.multi_instrument_melody_new)):
            self.Melody_Allinstrumentslist += self.multi_instrument_melody_new[i]
        self.Melody_Allinstrumentslist = list(set(self.Melody_Allinstrumentslist))
        # print('multi_instrument_melody_new: ', len(self.multi_instrument_melody_new), self.multi_instrument_melody_new)
        # print('Melody_Allinstrumentslist: ', len(self.Melody_Allinstrumentslist), self.Melody_Allinstrumentslist)

        self.Bass_Allinstrumentslist = []
        for i in range(len(self.multi_instrument_bass_new)):
            self.Bass_Allinstrumentslist += self.multi_instrument_bass_new[i]
        self.Bass_Allinstrumentslist = list(set(self.Bass_Allinstrumentslist))
        # print('multi_instrument_bass_new: ', len(self.multi_instrument_bass_new), self.multi_instrument_bass_new)
        # print('Bass_Allinstrumentslist: ', len(self.Bass_Allinstrumentslist), self.Bass_Allinstrumentslist)

        # TODO: 更新更多乐器类型
        for i in range(0, chapters_num):
            # 每个章节对应的根音组合类型
            roottype = np.random.randint(0, 100)
            if roottype >= 85:
                self.multi_root.append(root3)
            elif 70 <= roottype < 85:
                self.multi_root.append(root2)
            elif roottype < 70:
                self.multi_root.append(root)

        for i in range(0, chapters_num//2):
            if np.random.choice((0, 1), p=[0.6, 0.4])==1:
                rynum = np.random.randint(len(sm.rythmlonglist))
                self.rythmlist.append(sm.rythmlonglist[rynum])
                self.rythmlist.append(sm.rythmlonglist[rynum])
            else :
                rynum = np.random.randint(len(sm.rythmshortlist))
                self.rythmlist.append(sm.rythmshortlist[rynum])
                self.rythmlist.append(sm.rythmshortlist[rynum])

        for i in range(0, len(self.multi_root)):
            # 每个章节的长度
            self.multi_root_charpter.append(len(bass_class[self.multi_root[i]]) * 16)

        # if sm.singsong == 1:
        #     self.saveyinlist = DL.deal_with_lyric_part2(chapters_num, sm.lyric_batch_len, self.multi_root_charpter)

        # print('\nrythmlist长度: ', len(self.rythmlist), '\nrythmlist: ', self.rythmlist)
        # print('\nmulti_root长度: ', len(self.multi_root), '\nmulti_root: ', self.multi_root)
        # print('multi_root_charpter长度: ', len(self.multi_root_charpter),
        #       '\nmulti_root_charpter: ', self.multi_root_charpter, '\n')

