from tqdm import tqdm

from . import wav_create_note_V1_2 as wc_note


def add_pad_2_wav(blank_wav, midi, sm, md, bassornoteamp):
    # instruments are melody
    Unittime = int((sm.fm.piano_source.length * (130 / sm.bpm)) / 16)
    kongbaistart = 0  # sm.fm.piano_source.length
    zhangjie = 0
    k = 0
    zhangjie_num = md.multi_root_charpter[k]
    multi_root_charpter = md.multi_root_charpter
    strength_less = 0.99
    pad_instrument_note_list = md.pad_instrument_note_list
    for xiaojie in tqdm(range(0, len(midi)), desc="Pad进度: "):
        for yin in range(0, 8):
            start = int((xiaojie * 8 + yin) * Unittime) + kongbaistart
            # 计算当前这个音在那个章节里
            if xiaojie * 8 + yin > zhangjie_num:
                zhangjie_num += multi_root_charpter[k]
                k += 1
                zhangjie += 1

                if zhangjie < len(pad_instrument_note_list):
                    padinstrumentnum = pad_instrument_note_list[zhangjie]  # 0<=x<=3
            if zhangjie == 0 and sm.addmelodyornot == 1:
                padinstrumentnum = -1
            elif zhangjie == 0:
                padinstrumentnum = md.pad_instrument_note_list[0]

            if yin == 0 and padinstrumentnum in [0]:
                E_1_Pad_AmbientBass_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.E_1_Pad_AmbientBass_source,
                                      start, E_1_Pad_AmbientBass_source_note_num, Unittime, next_note_distance=12,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )
            if yin == 0 and padinstrumentnum in [1]:
                E_1_Pad_AmbientBassFifths_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.E_1_Pad_AmbientBassFifths_source,
                                      start, E_1_Pad_AmbientBassFifths_source_note_num, Unittime, next_note_distance=12,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )
            if yin == 0 and padinstrumentnum in [2]:
                E_1_Pad_BellCurve_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.E_1_Pad_BellCurve_source,
                                      start, E_1_Pad_BellCurve_source_note_num, Unittime, next_note_distance=12,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.2, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )
            if yin == 0 and padinstrumentnum in [3]:
                E_1_Pad_Clouds_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.E_1_Pad_Clouds_source,
                                      start, E_1_Pad_Clouds_source_note_num, Unittime, next_note_distance=12,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.4, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )
            if yin == 0 and padinstrumentnum in [4]:
                E_1_Pad_DiziPad_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.E_1_Pad_DiziPad_source,
                                      start, E_1_Pad_DiziPad_source_note_num, Unittime, next_note_distance=12,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.2, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )
            if yin == 0 and padinstrumentnum in [5]:
                E_1_Pad_FatAmbientBass_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.E_1_Pad_FatAmbientBass_source,
                                      start, E_1_Pad_FatAmbientBass_source_note_num, Unittime, next_note_distance=12,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.2, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )
            if yin == 0 and padinstrumentnum in [6]:
                E_1_Pad_FlutterPad_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.E_1_Pad_FlutterPad_source,
                                      start, E_1_Pad_FlutterPad_source_note_num, Unittime, next_note_distance=12,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.2, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )

            if yin == 0 and padinstrumentnum in [7]:
                E_1_Pad_HorizonPad_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.E_1_Pad_HorizonPad_source,
                                      start, E_1_Pad_HorizonPad_source_note_num, Unittime, next_note_distance=12,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )
            if yin == 0 and padinstrumentnum in [8]:
                E_1_Pad_PadAirGuita_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.E_1_Pad_PadAirGuita_source,
                                      start, E_1_Pad_PadAirGuita_source_note_num, Unittime, next_note_distance=12,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )
            if yin == 0 and padinstrumentnum in [9]:
                E_1_Pad_PedalSteel_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.E_1_Pad_PedalSteel_source,
                                      start, E_1_Pad_PedalSteel_source_note_num, Unittime, next_note_distance=12,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.4, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )
            if yin == 0 and padinstrumentnum in [10]:
                E_1_Pad_ReverseDistancePad_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.E_1_Pad_ReverseDistancePad_source,
                                      start, E_1_Pad_ReverseDistancePad_source_note_num, Unittime,
                                      next_note_distance=12,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.8, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )
            if yin == 0 and padinstrumentnum in [11]:
                E_1_Pad_SusMPLegErhu_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.E_1_Pad_SusMPLegErhu_source,
                                      start, E_1_Pad_SusMPLegErhu_source_note_num, Unittime, next_note_distance=12,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.03, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )
            if yin == 0 and padinstrumentnum in [12]:
                E_1_Pad_SusMPLegErhu2_source_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.E_1_Pad_SusMPLegErhu2_source,
                                      start, E_1_Pad_SusMPLegErhu2_source_source_note_num, Unittime,
                                      next_note_distance=12,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.03, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )
            if yin == 0 and padinstrumentnum in [13]:
                E_1_Pad_TonalPercussion_source_note_num = int(midi[xiaojie][yin])
                wc_note.long_note2wav(sm, md, blank_wav, zhangjie, sm.fm.E_1_Pad_TonalPercussion_source,
                                      start, E_1_Pad_TonalPercussion_source_note_num, Unittime, next_note_distance=12,
                                      bassornoteamp=bassornoteamp, instrument_Amp=0.6, strength_less=strength_less,
                                      addDecayType='decay_long_melody', add712note2bass='no',
                                      NoteTiqianyin=0, NoteYanyin=Unittime,
                                      BlankTiqianyin=0, )
