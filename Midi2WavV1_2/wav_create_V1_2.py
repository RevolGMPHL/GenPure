import numpy as np
import scipy.signal
from pydub import AudioSegment
from scipy.io import wavfile

import EQforPress as EQ
from GenerData.MusicDetailManager import MusicDetailManager
from GenerData.SettingManager import SettingsManager
from Midi2WavV1_2 import wav_create_drum_V1_2 as wc_drum
from Midi2WavV1_2 import wav_create_fd_V1_2 as wc_fd
from Midi2WavV1_2 import wav_create_mj_V1_2 as wc_mj
from Midi2WavV1_2 import wav_create_pad_V1_2 as wc_pad
from Midi2WavV1_2 import wav_create_rise_V1_2 as wc_rise
from Midi2WavV1_2.wav_add2wav import add_note_2_wav


def compress(OutWav):
    owav0 = OutWav.T[0]
    owav1 = OutWav.T[1]
    doublex = []

    OutWav_after_compress0 = np.where(owav0 < np.max(owav0) * 0.35, owav0, owav0 * 0.5)
    OutWav_after_compress1 = np.where(owav1 < np.max(owav1) * 0.35, owav1, owav1 * 0.5)

    doublex = np.append(doublex, OutWav_after_compress0)
    doublex = np.append(doublex, OutWav_after_compress1).reshape(2, len(OutWav_after_compress1)).T
    return doublex


def generate_wav(
        sing_midi_answer: list,
        answer: dict,
        music_bass: list,
        md: MusicDetailManager,
        sm: SettingsManager,
        ) -> np.array:
    timelength = len(music_bass)
    # print('timelength: ', timelength)

    answer1 = answer['1']
    answer2 = answer['2']
    answer3 = answer['3']

    base_instruments = md.multi_instrument_bass_new
    melody_instruments = md.multi_instrument_melody_new
    sing_melody_new_instrument = md.sing_instrument_new
    print('bass_instruments = ', base_instruments)
    print('melo_instruments = ', melody_instruments)
    if sm.bpm < 130:
        blanklenth = (timelength / 2 * 81415 * 130 / sm.bpm) // 81415
        output_wav = np.tile(sm.fm.piano_source.none, int(blanklenth + sm.blank_len_after)).T


        last_blank = output_wav.copy()
    else:
        output_wav = np.tile(sm.fm.piano_source.none, int(timelength / 2 + sm.blank_len_after)).T
        last_blank = output_wav.copy()

    # 加上两个旋律
    add_note_2_wav(output_wav, music_bass, base_instruments, sm, md, bassornoteamp=0.6, bass_or_note='bass')

    wc_pad.add_pad_2_wav(output_wav, music_bass, sm, md, bassornoteamp=1)

    if sm.addmelodyornot == 1:
        add_note_2_wav(output_wav, answer1, melody_instruments, sm, md, bassornoteamp=0.8, bass_or_note='note')
        if sm.singsong == 1:
            add_note_2_wav(output_wav, sing_midi_answer, sing_melody_new_instrument, sm, md, bassornoteamp=1.5,
                           bass_or_note='note')
        fd_amp = 0.4 + np.random.choice([0.0, 0.1, 0.2], p=[0.6, 0.2, 0.2])
    else:
        fd_amp = 0.5 + np.random.choice([0.0, 0.1, 0.2], p=[0.3, 0.3, 0.4])

    for i in range(len(answer2)):
        for j in range(0, 8):
            answer2[i][j] += 12

    if sm.fdmj == 1:
        wc_fd.add_longnoteins_2_wav(output_wav, answer2, sm, md, bassornoteamp=fd_amp)
        #
        wc_mj.add_mj_ins_2_wav(output_wav, answer3, sm, md, bassornoteamp=fd_amp)


    # 加上鼓
    # if np.random.randint(0, 1) == 1:
    print('\nwav v12 sm.drumclass: ', sm.drumclass)
    if sm.drumclass > 2:
        sm.drumclass -= 3
        print('sm.drumclass1: ',sm.drumclass )
        wc_drum.add_drum_2_wav(output_wav, music_bass, sm, md)
    else:
        print('sm.drumclass2: ', sm.drumclass)
        wc_drum.add_drum_midi_2_wav(output_wav, music_bass, sm, md)

    # wc_rise.add_ShuiYin_2_wav(output_wav, answer1, base_instruments, sm, md)
    if np.random.choice([0, 1], p=[0.15, 0.85]):
        # 加上rise
        wc_rise.add_Rise_2_wav(output_wav, answer1, base_instruments, sm, md)

    sos = EQ.peak_filter_iir(80, gain=-6, Q=0.5, fs=sm.sample_rate)  # gain负值，就是陷波滤波器
    output_wav = scipy.signal.sosfilt(sos, output_wav)
    sos = EQ.peak_filter_iir(320, gain=-12, Q=0.8, fs=sm.sample_rate)  # gain负值，就是陷波滤波器
    output_wav = scipy.signal.sosfilt(sos, output_wav)
    sos = EQ.peak_filter_iir(3600, gain=4, Q=0.5, fs=sm.sample_rate)  # gain负值，就是陷波滤波器
    output_wav = scipy.signal.sosfilt(sos, output_wav)
    last_blank += output_wav
    last_blank *= 0.6  # 简陋版压限器


    wav_filename = sm.fm.wav_music_output_name['1'][:-4]
    print('midi save to: ', wav_filename)

    # 保存wav
    # wavfile.write(wav_filename, sm.sample_rate, last_blank)

    return last_blank






# output_wav直接存mp3，但是会破音
def save_array_2_mp3(array: np.array,
                     filename: str,
                     sample_rate: int):
    int16_array = np.int16(array * 2 ** 15)
    music = AudioSegment(int16_array.tobytes(),
                         frame_rate=sample_rate,
                         sample_width=2,  # 2 byte (16 bit)
                         channels=2)
    music.export(filename, format='mp3', bitrate="320k")


def add_rythmbass(blank_wav, start, Unittime, length, note, pluslist, amplist):
    # pluslist 是哪几个后续跟上的音，amp是每个音的音量
    for i in range(len(pluslist)):
        blank_wav[(start + int(pluslist[i] * Unittime)): (start + len(note) + int(pluslist[i] * Unittime))] += note * \
                                                                                                               amplist[
                                                                                                                   i] * 0.9
    return blank_wav


def get_next_note_distance(midi, xiaojie, yin):
    rawyin = yin
    if xiaojie < len(midi) - 1:
        while (yin < 7):
            yin += 1
            if midi[xiaojie][yin] < 100:
                # print('yin - rawyin7 , ', yin - rawyin, yin, rawyin)
                return yin - rawyin
        xiaojie += 1
        while (yin < 15):
            yin += 1
            if midi[xiaojie][yin - 8] < 100:
                # print('yin - rawyin15 , ', yin - rawyin, yin, rawyin)
                return yin - rawyin
    else:
        return 8
