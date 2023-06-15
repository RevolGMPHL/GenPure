from pretty_readmidi import PrettyMidi
from GenerData.MusicDetailManager import MusicDetailManager
from GenerData.SettingManager import SettingsManager
from GenerData.genbass import genbass
from GenerData import note_num_2_name_and_rebuild_rhythm as nn2n

from answer2midi_code import answer2midi
from Model_revise import Transformer_revise, PositionEmbedding_revise, Encoder_revise, Decoder_revise, EncoderLayer_revise, DecoderLayer_revise, MultiHead_revise, PositionWiseFFN_revise
from Model_nnan import Transformer_nnan, PositionEmbedding_nnan, Encoder_nnan, Decoder_nnan, EncoderLayer_nnan, DecoderLayer_nnan, MultiHead_nnan, PositionWiseFFN_nnan

import torch
import numpy as np
device = torch.device('cuda')
from Midi2WavV1_2 import wav_create_V1_2 as wav_create_v1
from Midi2WavV2 import wav_create_V2 as wav_create_v2
import soundfile as sf

def pad_zero(seqs, max_len):
    PAD_ID = 130
    padded = np.full((len(seqs), max_len), fill_value=PAD_ID, dtype=np.int32)
    for i, seq in enumerate(seqs):
        padded[i, :len(seq)] = seq
    return torch.from_numpy(padded)


def nnan(answers):
    answers['1'] = nn2n.end_melody(answers['1'], sm, md)
    answers['2'] = nn2n.end_melody(answers['2'], sm, md)
    answers['3'] = nn2n.end_melody(answers['3'], sm, md)
    xianjierandom = np.random.choice([0, 1, 2, 3, 4, 5, 6, 7],
                                     p=[0.2, 0.2, 0.05, 0.15, 0.1, 0.1, 0.1, 0.1])  # [0.4, 0.3, 0.3, ]
    # nn2n.add_start_melody(answers['1'], sm, md, xianjierandom)
    # answers['1'] = (nn2n.choice_4_rest(sm, md, answers['1']))
    answers['1'] = nn2n.ABAC_model(nn2n.choice_4_fd(answers['1'], 'note'), batch=0, sm=sm, md=md)
    answers['1'] = nn2n.count16notenum(answers['1'], sm=sm, md=md)

    answers['2'] = nn2n.ABAC_model(answers['2'], batch=0, sm=sm, md=md)
    # answers['2'] = nn2n.ABAC_model(nn2n.mj(answers['2'], sm, md), batch=0, sm=sm, md=md)
    answers['3'] = nn2n.ABAC_model(nn2n.mj(nn2n.choice_4_fd(answers['3'], 'note'), sm, md), batch=0, sm=sm, md=md)
    return answers

def generate_music(sm: SettingsManager,
                   md: MusicDetailManager,
                   outputwavpath: str) -> (str, str):
    answers = {'1':[], '2':[], '3':[]}
    revise_model = torch.load('./model/revise_model2.pth', map_location='cuda:0').to(device)
    nnan_model = torch.load('./model/nnan_model.pth', map_location='cuda:0').to(device)

    music_bass, splitbass = genbass(sm, md)  # 24个音一个小batch

    print('start compose!')
    for i in range(len(music_bass)//8):
        inputdata = pad_zero(np.array(music_bass).reshape(1, -1)[:, 8*i:8*(i+1)], 10).to(device)+1
        ranmelo = torch.tensor(pad_zero(np.random.randint(48, 80, size=(1, 8)), 10)).to(device)
        revise_pred = revise_model.inference(inputdata, ranmelo)[:, 1:9]-1
        nnan_pred = nnan_model.inference(inputdata, ranmelo)[:, 1:9]-1
        answers['1'].append(list(revise_pred[0].cpu().detach().numpy()))
        answers['2'].append(list(revise_pred[0].cpu().detach().numpy()))
        answers['3'].append(list(revise_pred[0].cpu().detach().numpy()))
    answers = nnan(answers)


    answer2midi(sm.tonality, answers['1'], splitbass, sm)
    sing_midi_answer = [None]
    print('answers: ', answers)
    wav_output = wav_create_v1.generate_wav(sing_midi_answer, answers, splitbass, md, sm)
    wav_output /= np.max(np.abs(wav_output))
    sf.write(outputwavpath, wav_output, 44100)

def midi2wav(md, sm):
    wav_create_v2.generate_wav(md, sm)

if __name__ == '__main__':


    pret = PrettyMidi()
    sm = SettingsManager(
        root=45, root2=45, root3=45,
        drumclass=10, singsong=0, chapters_num=6,
        heavyorlight=0,
        bpm=104, tonality=0, dianyinornot=1, fdmj=0
    )
    # 这是生成一系列音乐详细的参数
    # 这里是选择乐器，乐器表请查看  filemanager
    # melo_instruments = [[2], [2], [2], [2], [2], [2]]
    # bass_instruments = [[0], [0], [0], [0], [0], [0]]

    melo_instruments = None
    bass_instruments = None
    # # 8 雨

    # bass_instruments = [[ 14, 17, -2], [ 14, 17, -2],[ 14, 17, 19],[ 14, 17, 19],[ 14, 17, 19],[ 14, 17, -2],]
    # melo_instruments = [[ 54, 14,  -2, -2, -2], [54, 14,  -2, -2], [54, 55, 14,  -2],
    #                     [ 54, 55, 14, 2, -2], [ 54,  55, 2, -2], [54, 14, 2, -2, -2]]

    bass_instruments = [[11, 19, 27, 39, 44, -2, -2], [19, 41, -2, -2, -2, -2, -2], [10, 23, -2, -2, -2, -2, -2],
                        [10, -2, -2, -2, -2, -2, -2], [22, -2, -2, -2, -2, -2, -2], [34, -2, -2, -2, -2, -2, -2]]
    melo_instruments = [[7, 8, 19, 20, 36, -2], [6, 28, -2, -2, -2], [27, 32, 41, 29, -2, -2],
                        [18, 35, 28, -2, -2, -2], [22, 26, 42, -2, -2, -2], [3, 14, -2, -2, -2, -2]]

    # 如果想随机乐器，如下操作
    # 摇滚
    # melo_instruments = [[23, 38, 2, 24, -2, -2], [23, 24, -2, -2, -2, -2],[25, 23, 24, -2, -2, -2],[38, 23, 24, -2, -2, -2],[39, 38,23, 24, -2, -2],[39, 23, 24, -2, -2],]
    # bass_instruments = [[6, 12, 23, -2, -2, -2],[23, 6, 26, -2, -2, -2],[24, 6, 25, -2, -2, -2],[25, 6, 24, -2, -2, -2],[26, 6, 23, -2, -2, -2],[26, 6, 24, -2, -2, -2], ]

    # 电子
    # melo_instruments = [[3, 5, 6, -2, -2],[23, -2, -2, -2, -2],[24, 3, 39, -2, -2],[25, 5, -2, -2, -2],[55, 5, 6, -2, -2],[56, 6, 3, -2, -2],]
    # bass_instruments = [[23, 24, -2, -2, -2],[23, 25, -2, -2, -2],[23, 25, -2, -2, -2],[23, 25, -2, -2, -2],[24, 25, -2, -2, -2],[24, 25, -2, -2, -2],]


    # meloins = [1,2,4,5,6,17,19,26,27,29,43,44,45,49,55,56,21,22]
    # bassins = [0,1,3,4,5,6,7,8,9,10,11,12,13,15,16,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,47,48,49,]
    # melo_instruments = [[-2 for i in range(8)] for j in range(6)]
    # bass_instruments = [[-2 for i in range(8)] for j in range(6)]
    # for chapternum in range(6):
    #     for insnum in range(8):
    #         melo_instruments[chapternum][insnum] = meloins[np.random.randint(0,len(meloins))]
    #         bass_instruments[chapternum][insnum] = bassins[np.random.randint(0,len(bassins))]

    # 交响
    # base_instruments: [[3, 35, 31, 40, 32, 36, 47, 49], [19, 9, 9, 48, 43, 21, 32, 40], [44, 9, 8, 1, 6, 27, 42, 44],
    #                    [17, 11, 21, 22, 38, 23, 13, 41], [41, 17, 42, 32, 16, 27, 37, 12],
    #                    [29, 39, 33, 1, 38, 28, 36, 8]]
    # melody_instruments: [[2, 19, 19, 49, 45, 45, 21, 26], [29, 1, 43, 49, 56, 19, 27, 26],
    #                      [29, 43, 21, 5, 26, 1, 19, 5], [17, 45, 2, 19, 21, 6, 26, 29], [49, 1, 5, 44, 29, 49, 5, 27],
    #                      [56, 49, 49, 43, 21, 43, 4, 49]]



    md = MusicDetailManager(sm, melo_instruments, bass_instruments)

    generate_music(sm, md, outputwavpath='output/out2.wav')

    # midi2wav(md, sm)

