import os
import warnings
from enum import Enum, auto
from typing import Union, Callable, List

from scipy.io import wavfile


# offset 不是时间，是相对提高一些音程
class PianoSource:
    def __init__(self, minimum, maximum, offset, path, sample_rate=44100):
        self.minimum, self.maximum, self.offset, self.path, self.sample_rate = \
            minimum, maximum, offset, path, sample_rate
        self.piano_source = {i: None for i in range(
            self.minimum - self.offset,
                                                    self.maximum - self.offset + 1)}
        self.load(self.minimum - self.offset)
        self.length = len(self.piano_source[self.minimum - self.offset])  # 81415
        self.none = wavfile.read(self.path + 'none.wav')[1].T

    def load(self, n):
        self.piano_source[n] = wavfile.read(self.path + str(n + self.offset) + '.wav')[1]

    def get(self, n):
        if self.piano_source[n] is None:
            self.load(n)
        return self.piano_source[n]


# class InstrumentType(Enum):
#     NOTE = auto()
#     BASS = auto()
#     NOTE_AND_BASS = auto()
#     MOJIN = auto()
#
#     def support(self, instrument_type):
#         if self is InstrumentType.NOTE_AND_BASS:
#             return instrument_type in [InstrumentType.NOTE, InstrumentType.BASS, InstrumentType.NOTE_AND_BASS]
#         return self is instrument_type


class InstrumentLengthType(Enum):
    SHORT = auto()
    LONG = auto()
    LONG_CUT = auto()


class InstrumentSetting:
    def __init__(
            self,
            is_active: bool = True,
            length_type: InstrumentLengthType = InstrumentLengthType.SHORT,
            instrument_amp: float = 1.0,
            note_ti_qian_yin: Union[int, Callable[[int], int]] = 0,
            note_yan_yin: Union[int, Callable[[int], int]] = 0,
            blank_ti_qian_yin: int = 0,
            does_add_eq: bool = False,
            does_add_712: bool = False,
            does_add_34: Union[bool, Callable[[bool], bool]] = False,
            does_add_rythm: bool = False,
            does_add_712_note_to_bass: bool = False,
            add_decay_type: str = 'decay',
            ):
        self.is_active = is_active
        self.length_type = length_type
        self.instrument_amp = instrument_amp
        self.note_ti_qian_yin = note_ti_qian_yin
        self.note_yan_yin = note_yan_yin
        self.blank_ti_qian_yin = blank_ti_qian_yin
        self.does_add_eq = does_add_eq
        self.does_add_712 = does_add_712
        self.does_add_34 = does_add_34
        self.does_add_rythm = does_add_rythm
        self.does_add_712_note_to_bass = does_add_712_note_to_bass
        self.add_decay_type = add_decay_type

    def get_note_yan_yin(self, unit_time: int = None) -> int:
        if isinstance(self.note_yan_yin, int):
            return self.note_yan_yin
        assert unit_time is not None, 'note_yan_yin is a function, should input unit time to get'
        note_yan_yin = self.note_yan_yin
        return note_yan_yin(unit_time)

    def get_note_ti_qian_yin(self, unit_time: int = None) -> int:
        if isinstance(self.note_ti_qian_yin, int):
            return self.note_ti_qian_yin
        assert unit_time is not None, 'note_ti_qian_yin is a function, should input unit time to get'
        note_yan_yin = self.note_ti_qian_yin
        return note_yan_yin(unit_time)

    def get_does_add_34(self, does_add_34: bool = None) -> bool:
        if isinstance(self.does_add_34, bool):
            return self.does_add_34
        assert does_add_34 is not None, 'setting.does_add_34 is a function, should input does_add_34 to get'
        does_add_34_fun: Callable[[bool], bool] = self.does_add_34
        return does_add_34_fun(does_add_34)


class InstrumentSource:
    def load(self, n):
        # self.Instrument_source[n] = wavfile.read(self.path + str(n + self.offset) + '.wav')[1]
        # print("Source load path: ", os.path.join(self.path, str(n + self.offset) + '.wav'))
        warnings.filterwarnings("ignore")
        # print('self.path: ', self.path)
        self.Instrument_source[n] = wavfile.read(os.path.join(self.path, str(n + self.offset) + '.wav'))[1]

    def __init__(
            self,
            minimum: int,
            maximum: int,
            offset: int,
            path: str,
            type: str = '',
            name: str = '',
            sample_rate: int = 44100,
            instrument_setting_of_note: List[InstrumentSetting] = None,
            instrument_setting_of_bass: List[InstrumentSetting] = None,
            instrument_setting_of_mj: List[InstrumentSetting] = None
            ):
        self.minimum, self.maximum, self.offset, self.path, self.sample_rate = \
            minimum, maximum, offset, path, sample_rate
        self.Instrument_source = {i: None for i in range(
            self.minimum - self.offset,
            self.maximum - self.offset + 1
            )}
        self.load(self.minimum - self.offset)
        self.length = len(self.Instrument_source[self.minimum - self.offset])  # 81415
        warnings.filterwarnings("ignore")
        self.none = wavfile.read(os.path.join(self.path, 'none.wav'))[1].T
        self.sample_rate = wavfile.read(os.path.join(self.path, 'none.wav'))[0]
        self.local_path = os.path.abspath(os.path.dirname(__file__))
        self.type = type
        self.name = name
        self.instrument_setting_of_note = instrument_setting_of_note
        self.instrument_setting_of_bass = instrument_setting_of_bass
        self.instrument_setting_mj = instrument_setting_of_mj

    # TODO： 这里为了写鼓的时候，用名字，而不是单纯的数字，可能要改写成字典
    def load_drum(self, n):
        self.Instrument_source[n] = wavfile.read(os.path.join(self.path, str(n + self.offset) + '.wav'))[1]
        return self.Instrument_source[n]

    def get(self, n):
        if self.Instrument_source[n] is None:
            self.load(n)
        return self.Instrument_source[n]


class InstrumentSourceWithSetting:

    def __init__(self, source: InstrumentSource, setting: InstrumentSetting):
        self.source = source
        self.setting = setting
