#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
from music21 import note, chord, converter

from GenerData.note_name_and_num import note_name_2_num
from GenerData.note_name_and_num import note_num_2_name


class Midi:
    def __init__(self):
        self.names = []
        self.nums = []
        self.offsets = []


class ParseMidi:

    # When only use self.midi without self.data, than train_or_run can be set to None
    def __init__(self, midi_file_name, delta_time, tonality=0,
                 melody_or_base='melody', train_or_run_or_wav='wav', note_or_chord='note'):
        self.midi_file_name = midi_file_name
        self.delta_time = delta_time
        self.tonality = tonality
        self.melody_or_base = melody_or_base
        self.train_or_run_or_wav = train_or_run_or_wav
        self.note_or_chord = note_or_chord
        self.midi = Midi()
        self.data = None

        if self.note_or_chord == 'note':
            self.get_notes()
            if self.train_or_run_or_wav in ['train', 'run']:
                self.splitted_num_notes, self.splitted_num_notes_with_two_random_bars = self.split_notes()
                if self.melody_or_base == 'melody':
                    self.data = self.get_triple_melody()
                elif self.melody_or_base == 'base':
                    if self.train_or_run_or_wav == 'train':
                        self.data = self.get_triple_base()
                    elif self.train_or_run_or_wav == 'run':
                        self.data = self.get_double_plus_random_base()
        elif self.note_or_chord == 'chord':
            self.get_notes_and_chords()
            if self.train_or_run_or_wav in ['train', 'run']:
                pass
            elif self.train_or_run_or_wav in ['drum']:
                self.splitted_num_notes = self.split_drum_notes()

    def get_notes(self):
        stream = converter.parse(self.midi_file_name)
        # 读取整个midi乐谱
        for element in stream.flat.getElementsByClass(["Note", "Chord"]):
            pitch = ''
            # 这个是判断是不是柱式和弦
            # 如果是单音
            if isinstance(element, note.Note):
                pitch = str(element.pitch)
            # 如果是柱式和弦
            elif isinstance(element, chord.Chord):
                # print(element.volume)
                chord_nums = [note_name_2_num(str(n.pitch)) for n in element]
                extreme_chord_num = min(chord_nums) if self.melody_or_base == 'base' else max(chord_nums)
                pitch = str(note_num_2_name(extreme_chord_num))
            self.midi.names.append(pitch)
            self.midi.nums.append(note_name_2_num(pitch))
            self.midi.offsets.append(element.offset)

    def get_notes_and_chords(self):
        stream = converter.parse(self.midi_file_name)
        for element in stream.flat.getElementsByClass(["Note", "Chord"]):
            pitches = []
            # 这个是判断是不是柱式和弦
            # 如果是单音
            if isinstance(element, note.Note):
                pitches.append(str(element.pitch))
            # 如果是柱式和弦
            elif isinstance(element, chord.Chord):
                pitches = [str(e.pitch) for e in element]
            self.midi.names.append(pitches)
            self.midi.nums.append([note_name_2_num(pitch) for pitch in pitches])
            self.midi.offsets.append(element.offset)

    def split_notes(self):
        # notes_num_full_length这个list，把空白的音的地方填上130的音，把整个音的序列降维度
        # 第一步，制作一个长度和原来整首曲子时间长度相同的list（全部130）
        num_of_batch = int(self.midi.offsets[-1])
        num_of_batch = (num_of_batch // 8 + 1) * 8
        notes_num_full_length = 130 + self.tonality * np.random.randint(low=0, high=2, size=num_of_batch * 4)
        # 第二步，把每个音对应的地方，把全部空白音的list那些130替换掉
        for i, offset in enumerate(self.midi.offsets):
            notes_num_full_length[int(offset * 4)] = self.midi.nums[i]

        # 把原来的note_list，按每8个音，切成一小个list，一小个list
        assert len(notes_num_full_length) % 8 == 0
        splitted_num_notes = notes_num_full_length.reshape(-1, 8)

        # [[A], [B], [C]] to [[A], [B], [C], [Random], [Random]]
        # n * 8           to (n + 2) * 8
        splitted_num_notes_with_two_random_bars = np.append(splitted_num_notes,
                                                            np.random.randint(150, 161, size=(2, 8)),
                                                            axis=0)
        return splitted_num_notes, splitted_num_notes_with_two_random_bars

    def split_drum_notes(self):
        # notes_num_full_length这个list，把空白的音的地方填上130的音，把整个音的序列降维度
        # 第一步，制作一个长度和原来整首曲子时间长度相同的list（全部130）
        num_of_batch = 64
        notes_num_full_length = [[130]] * num_of_batch

        # 第二步，把每个音对应的地方，把全部空白音的list那些130替换掉
        for i, offset in enumerate(self.midi.offsets):
            notes_num_full_length[int(offset * 4)] = self.midi.nums[i]

        return notes_num_full_length

    # 生成3个连续小节，用于训练模型
    def get_triple_base(self):
        assert self.melody_or_base == 'base'
        # [[A], [B], [C], [R1], [R2]] to [[[A], [B], [C]], [[B], [C], [R1]], [[C], [R1], [R2]]]
        # (n + 2) * 8                 to n * 3 * 8
        #                     reshape to [[A, B, C], [B, C, R1], [C, R1, R2]]
        #                     reshape to n * 24
        return np.reshape([self.splitted_num_notes_with_two_random_bars[i:i + 3]
                           for i in range(len(self.splitted_num_notes))],
                          newshape=(-1, 24))

    # 生成一个随机+调性交叉的小节，用于跑模型（更新2019.10.23 更新了用来生成的和弦部分的random，让他不是纯150，这样出来的旋律离调音会少一些）
    def get_random_base_bar(self, data):
        assert self.melody_or_base == 'base'
        data_set = np.unique(data)
        four_nums_from_data_set = np.random.choice(data_set, 4)
        four_nums_from_tonality = (130 + self.tonality) * np.ones(4)
        return np.stack((four_nums_from_data_set, four_nums_from_tonality)).T.flatten()

    # 生成2个连续小节+1个随机小节，用于跑模型
    def get_double_plus_random_base(self):
        assert self.melody_or_base == 'base'
        # [[A], [B], [C], [R1], [R2]] to [[[A], [B], [C&R]], [[B], [C], [R1&R]], [[C], [R1], [R2&R]]]
        # (n + 2) * 8                 to n * 3 * 8
        #                     reshape to n * 24
        return np.reshape([[self.splitted_num_notes_with_two_random_bars[i],
                            self.splitted_num_notes_with_two_random_bars[i + 1],
                            self.get_random_base_bar(self.splitted_num_notes_with_two_random_bars[i + 2])]
                           for i in range(len(self.splitted_num_notes))],
                          newshape=(-1, 24))

    def get_triple_melody(self):
        assert self.melody_or_base == 'melody'
        # [[A], [B], [C]] to [[[A], [A], [A]], [[B], [B], [B]], [[C], [C], [C]]]
        # n * 8           to n * 3 * 8
        #         reshape to [[A, A, A], [B, B, B], [C, C, C]
        #         reshape to n * 24
        return np.reshape([[bar] * 3 for bar in self.splitted_num_notes],
                          newshape=(-1, 24))

    def not_shorter_than(self, length):
        if len(self.data) < length:
            print('Lengthen the data from {} to {}.'.format(len(self.data), length))
            addition = np.random.randint(150, 159, size=(length - len(self.data), 24))
            self.data = np.vstack(self.data, addition)
