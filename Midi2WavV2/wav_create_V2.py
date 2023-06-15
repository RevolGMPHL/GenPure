from GenerData.MusicDetailManager import MusicDetailManager
from GenerData.SettingManager import SettingsManager
import numpy as np
import scipy.signal
from pydub import AudioSegment
from scipy.io import wavfile
import Midi2WavV2.create_wav as create_wav
import soundfile as sf


def generate_wav(
        md: MusicDetailManager,
        sm: SettingsManager,
        ) -> np.array:
    pass

    # midiname_bass = 'E:/DATA/4.midi合集/purepiano/seeyouagain_leftbpm100.mid'
    # midiname_melo = 'E:/DATA/4.midi合集/purepiano/seeyouagain_rightbpm100.mid'
    print('name: ', sm.fm.wav_music_output_name['1'])
    midiname_bass = sm.fm.wav_music_output_name['1'][:-6] + '_bass.mid'
    midiname_melo = sm.fm.wav_music_output_name['1'][:-6] + '_melo.mid'

    instru_name_melo = 'E:/DATA/0.note_resources_fushang/2021_note_resources/Piano/PianoNoirePure4好多曲谱/'


    wav_bass = create_wav.Long_Piano_wavcreate(sm, midiname_bass, instru_name_melo)*0.6
    wav_melo = create_wav.Long_Piano_wavcreate(sm, midiname_melo, instru_name_melo)
    wav_out = None
    if wav_melo.shape[1] > wav_bass.shape[1]:
        wav_out = wav_melo
        wav_out[:, :wav_bass.shape[1]] += wav_bass
    else:
        wav_out = wav_bass
        wav_out[:, :wav_melo.shape[1]] += wav_melo
    # wav_melo = create_wav.Long_Piano_wavcreate(midiname_melo, instru_name_melo)
    # wav_melo = create_wav.Guita_wavcreate(midiname_melo, instru_name_melo)

    wavmax = np.max(wav_out)
    wavout = wav_out/wavmax * 0.9
    print(np.max(wavout))
    sf.write('E:/CodeProject/20.Output/Midi2WAV_output/out.wav', wavout.T, 44100)