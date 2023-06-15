import datetime
import os
from typing import Optional, List, Dict

from GenerData.instrument_class import InstrumentSource, InstrumentSetting, InstrumentLengthType, InstrumentSourceWithSetting
from GenerData.utils.utils import get_setting_from_env_or_json

note_resources_path = r'E:\project\DATA\note_resources' #get_setting_from_env_or_json('NOTE_RESOURCES')
print('FileManager.py note_resources_path: ', note_resources_path)

# Resources path
# instrument wav file
# todo: refactor: 分source、setting两个list，通过name关联（类似数据库关联表），setting对象里有source和type(note/bass/mj)，从而代替SourceAndSetting
print('note_resources_path: ', note_resources_path)
instrumentssss = [
    # melody
    InstrumentSource(
        minimum=24, maximum=108, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_0_Piano200319'
        ),
        name='piano',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=0.8,
            does_add_eq=True
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=86, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_1_EleGuita'
        ),
        name='EleGuita',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=0.8,
            does_add_eq=True
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.8,
            add_decay_type='decay',
            does_add_712_note_to_bass=True,
        )]
    ),
    InstrumentSource(
        minimum=57, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_2_Guita'
        ),
        name='Guita',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            instrument_amp=6,
            does_add_eq=True
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=3,
            add_decay_type='decay',
            does_add_712_note_to_bass=True,
        )]
    ),
    InstrumentSource(
        minimum=24, maximum=108, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_3_Pianoshort'
        ),
        name='Pianoshort',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            instrument_amp=0.6,
            does_add_eq=True,
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            is_active=False,
            instrument_amp=0.6,
            does_add_eq=True,
            does_add_712=True,
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=96, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_4_DeepMode'
        ),
        name='DeepMode',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            instrument_amp=3.5,
            note_yan_yin=3000,
            add_decay_type='decay_melody',
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=2,
            add_decay_type='decay',
            does_add_712_note_to_bass=True,
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=96, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_5_FluteandStrings'
        ),
        name='FluteandStrings',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            instrument_amp=3.5,
            add_decay_type='decay_long_melody',
            note_yan_yin=1000,
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.8,
            add_decay_type='decay',
            does_add_712_note_to_bass=True,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=108, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_6_PianoGrand'
        ),
        name='PianoGrand',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=0.6,
            does_add_eq=True,
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.5,
            add_decay_type='decay',
            does_add_712_note_to_bass=True,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=108, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_7_PianoPopKey'
        ),
        name='PianoPopKey',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=2.0,
            does_add_eq=True,
            does_add_34=True,
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.3,
            add_decay_type='decay',
            does_add_712_note_to_bass=True,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=96, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_8_GenPiano'
        ),
        name='GenPiano',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=2.8,
            does_add_eq=True,
            does_add_34=True,
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            instrument_amp=0.4,
            does_add_eq=True,
            does_add_712=True,
            does_add_34=True,
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=85, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_9_Violas'
        ),
        name='Violas',
        type='melody',
        instrument_setting_of_bass=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            instrument_amp=1.5,
            add_decay_type='decay_long_melody',
            does_add_712_note_to_bass=True,
            note_ti_qian_yin=1000,
            note_yan_yin=4000,
        )]
    ),
    InstrumentSource(
        minimum=55, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_10_Joshua', 'JoshuaContourVioLong'
        ),
        name='A_10_Joshua_JoshuaContourVioLong',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=2.2,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=5000,
            note_yan_yin=lambda unit_time: 2 * unit_time,
        )]
    ),
    InstrumentSource(
        minimum=55, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_10_Joshua', 'JoshuaContourVioShort'
        ),
        name='A_10_Joshua_JoshuaContourVioShort',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            instrument_amp=1.6,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=6000,
            note_yan_yin=lambda unit_time: 2 * unit_time,
        )]
    ),
    InstrumentSource(
        minimum=55, maximum=88, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_10_Joshua', 'JoshuaHarmonicVio'
        ),
        name='A_10_Joshua_JoshuaHarmonicVio',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.7,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=4000,
            note_yan_yin=lambda unit_time: 2 * unit_time,
        )]
    ),
    InstrumentSource(
        minimum=55, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_10_Joshua', 'JoshuaLongVio'
        ),
        name='A_10_Joshua_JoshuaLongVio',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.7,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=2000,
            note_yan_yin=lambda unit_time: int(1.5 * unit_time),
        )]
    ),
    InstrumentSource(
        minimum=55, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_10_Joshua', 'JoshuaSpiccato'
        ),
        name='A_10_Joshua_JoshuaSpiccato',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=0.6,
            does_add_eq=True,
        )]
    ),
    InstrumentSource(
        minimum=55, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_10_Joshua', 'JoshuaStaVio'
        ),
        name='A_10_Joshua_JoshuaStaVio',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=0.6,
            note_ti_qian_yin=1000,
            does_add_eq=True,
        )]
    ),
    InstrumentSource(
        minimum=42, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', '3Trump6Frnchhrns8va_Legato'
        ),
        name='A_11_Nucleus_0_3Trump6Frnchhrns8va_Legato',
        type='melody'
    ),
    InstrumentSource(
        minimum=29, maximum=51, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', '4Trmb2Tb8Va_Sustained'
        ),
        name='A_11_Nucleus_1_4Trmb2Tb8Va_Sustained',
        type='melody',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            add_decay_type='decay_hanning',
            note_ti_qian_yin=int(81415 / 8),
            note_yan_yin=lambda unit_time: unit_time * 2,
        )]
    ),
    InstrumentSource(
        minimum=24, maximum=48, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', '6Cello_4Bass_Spiccato'
        ),
        name='A_11_Nucleus_2_6Cello_4Bass_Spiccato',
        type='melody',
        instrument_setting_of_bass=[InstrumentSetting(
            note_ti_qian_yin=int(81415 / 16),
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=24, maximum=48, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', '6Cello_4Bass_Sustained'
        ),
        name='A_11_Nucleus_3_6Cello_4Bass_Sustained',
        type='melody',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.7,
            add_decay_type='decay_hanning',
            note_ti_qian_yin=int(81415 / 8),
            note_yan_yin=lambda unit_time: unit_time * 3,
        )]
    ),
    InstrumentSource(
        minimum=24, maximum=48, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'Bass_Spiccato'
        ),
        name='A_11_Nucleus_4_Bass_Spiccato',
        type='melody',
        instrument_setting_of_bass=[InstrumentSetting(
            instrument_amp=1.7,
            does_add_34=True,
            does_add_rythm=True,
            note_ti_qian_yin=int(81415 / 16),
        )]
    ),
    InstrumentSource(
        minimum=24, maximum=48, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'Bass_Sustained'
        ),
        name='A_11_Nucleus_5_Bass_Sustained',
        type='melody',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=1.2,
            add_decay_type='decay_hanning',
            note_ti_qian_yin=int(81415 / 8),
            note_yan_yin=lambda unit_time: unit_time * 3,
        )]
    ),
    InstrumentSource(
        minimum=29, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'Brass_Full'
        ),
        name='A_11_Nucleus_6_Brass_Full',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.7,
            add_decay_type='decay_hanning',
            note_yan_yin=lambda unit_time: int(1.5 * unit_time),
            blank_ti_qian_yin=int(81415 / 8),
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.7,
            add_decay_type='decay_hanning',
            note_ti_qian_yin=int(81415 / 8),
            note_yan_yin=lambda unit_time: unit_time * 3,
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'Brass_Full_Staccatissimo'
        ),
        name='A_11_Nucleus_7_Brass_Full_Staccatissimo',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.7,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=int(81415 / 16),
            note_yan_yin=lambda unit_time: int(1.5 * unit_time)
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            instrument_amp=0.5,
            note_ti_qian_yin=int(81415 / 8),
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'Cellos_Legato'
        ),
        name='A_11_Nucleus_8_Cellos_Legato',
        type='melody',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.7,
            add_decay_type='decay_hanning',
            note_ti_qian_yin=int(81415 / 8),
            note_yan_yin=lambda unit_time: unit_time * 3,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'Cellos_Pizzicato'
        ),
        name='A_11_Nucleus_9_Cellos_Pizzicato',
        type='melody',
        instrument_setting_of_bass=[InstrumentSetting(
            instrument_amp=1.2,
            note_ti_qian_yin=int(81415 / 16),
            does_add_34=True,
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'Cellos_Spiccato'
        ),
        name='A_11_Nucleus_10_Cellos_Spiccato',
        type='melody',
        instrument_setting_of_bass=[InstrumentSetting(
            note_ti_qian_yin=int(81415 / 16),
            does_add_34=True,
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=60, maximum=74, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'Choir_Sopranos_Staccato'
        ),
        name='A_11_Nucleus_11_Choir_Sopranos_Staccato',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            add_decay_type='decay_hanning',
            note_yan_yin=lambda unit_time: int(1.5 * unit_time),
            blank_ti_qian_yin=int(81415 / 16),
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            instrument_amp=1.3,
            note_ti_qian_yin=int(81415 / 16),
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=60, maximum=78, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'Choir_Sopranos_Sustained_A'
        ),
        name='A_11_Nucleus_12_Choir_Sopranos_Sustained_A',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            instrument_amp=1.5,
            add_decay_type='decay_long_melody',
            note_yan_yin=lambda unit_time: int(1.5 * unit_time),
            blank_ti_qian_yin=int(81415 / 16),
        )],
        instrument_setting_of_bass=[
            InstrumentSetting(
                length_type=InstrumentLengthType.LONG,
                instrument_amp=0.7,
                add_decay_type='decay_hanning',
                note_ti_qian_yin=int(81415 / 8),
                note_yan_yin=lambda unit_time: unit_time * 3,
            ),
            InstrumentSetting(
                length_type=InstrumentLengthType.LONG,
                add_decay_type='decay_long_melody',
                note_ti_qian_yin=int(81415 / 8),
                note_yan_yin=lambda unit_time: int(unit_time * 1.5),
            )
        ]
    ),
    InstrumentSource(
        minimum=60, maximum=78, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'Choir_Sopranos_Sustained_O'
        ),
        name='A_11_Nucleus_13_Choir_Sopranos_Sustained_O',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            instrument_amp=1.5,
            add_decay_type='decay_long_melody',
            blank_ti_qian_yin=int(81415 / 16),
            note_yan_yin=lambda unit_time: int(1.5 * unit_time),
        )],
        instrument_setting_of_bass=[
            InstrumentSetting(
                length_type=InstrumentLengthType.LONG,
                instrument_amp=5,
                add_decay_type='decay_hanning',
                note_ti_qian_yin=int(81415 / 8),
                note_yan_yin=lambda unit_time: int(3 * unit_time),
            ),
            InstrumentSetting(
                length_type=InstrumentLengthType.LONG,
                instrument_amp=5,
                add_decay_type='decay_long_melody',
                note_ti_qian_yin=int(81415 / 8),
                note_yan_yin=lambda unit_time: int(1.5 * unit_time),
            ),
        ]
    ),
    InstrumentSource(
        minimum=29, maximum=53, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'Low_Brass_Sustained'
        ),
        name='A_11_Nucleus_14_Low_Brass_Sustained',
        type='melody',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.5,
            add_decay_type='decay_hanning',
            note_ti_qian_yin=int(81415 / 8),
            note_yan_yin=lambda unit_time: int(3 * unit_time),
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'VioViaChord_Pizzicato'
        ),
        name='A_11_Nucleus_15_VioViaChord_Pizzicato',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            instrument_amp=1.7,
            add_decay_type='decay_long_melody',
            note_yan_yin=lambda unit_time: int(1.5 * unit_time),
            blank_ti_qian_yin=int(81415 / 8),
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'VioViaChord_Spiccato'
        ),
        name='A_11_Nucleus_16_VioViaChord_Spiccato',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.8,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=lambda unit_time: unit_time,
            note_yan_yin=lambda unit_time: int(1.5 * unit_time),
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'VioViaChord_Sustained'
        ),
        name='A_11_Nucleus_17_VioViaChord_Sustained',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.9,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=int(81415 / 12),
            note_yan_yin=lambda unit_time: 2 * unit_time,
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_11_Nucleus', 'VioViaChord_Tremolo'
        ),
        name='A_11_Nucleus_18_VioViaChord_Tremolo',
        type='melody'
    ),
    InstrumentSource(
        minimum=24, maximum=96, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_12_PianoGrandeursoft'
        ),
        name='A_12_PianoGrandeursoft',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=2.0,
            does_add_eq=True,
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            instrument_amp=2.0,
            does_add_eq=True,
        )]
    ),
    InstrumentSource(
        minimum=24, maximum=96, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_13_PianoGrandeurSoft2'
        ),
        name='A_13_PianoGrandeurSoft2',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=2,
            does_add_eq=True,
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            instrument_amp=1,
            does_add_eq=True,
        )]
    ),
    InstrumentSource(
        minimum=24, maximum=96, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_14_PianoMaverickSoft'
        ),
        name='A_14_PianoMaverickSoft',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=2,
            does_add_eq=True,
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            instrument_amp=2,
            does_add_eq=True,
        )]
    ),
    InstrumentSource(
        minimum=40, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'A_15_AmpleGuitaRaw'
        ),
        name='A_15_AmpleGuitaRaw',
        type='melody'
    ),

    # Note
    InstrumentSource(
        minimum=48, maximum=86, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_1_Guita2'
        ),
        name='Guita2_N_1',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=0.9,
            does_add_eq=True,
            does_add_34=True
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            instrument_amp=0.8,
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=98, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_2_Guzheng'
        ),
        name='Guzheng_N_2',
        type='melody'
    ),  # 特殊，一些音没有

    InstrumentSource(
        minimum=48, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_3_Kora'
        ),
        name='Kora_N_3',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            does_add_eq=True
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_4_StaHighVio'
        ),
        name='StaHighVio_N_4',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=1.5,
            does_add_eq=True
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_5_Nyatiti'
        ),
        name='Nyatiti_N_5',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            does_add_eq=True
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_6_Oud'
        ),
        name='Oud_N_6',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=0.8,
            does_add_eq=True
        )]
    ),
    InstrumentSource(
        minimum=60, maximum=108, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_7_MuteGuita'
        ),
        name='MuteGuita_N_7',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            instrument_amp=1.2,
            does_add_eq=True
        )]
    ),
    InstrumentSource(
        minimum=60, maximum=108, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_8_MuteGuita2'
        ),
        name='MuteGuita2_N_8',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            does_add_eq=True
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=91, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_9_Och'
        ),
        name='Och_N_9',
        type='melody'
    ),
    InstrumentSource(
        minimum=60, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_10_ViolinLong'
        ),
        name='ViolinLong_N_10',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.8,
            add_decay_type='decay_long_melody',
            note_yan_yin=8000,
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=96, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_11_Marimba'
        ),
        name='Marimba_N_11',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=1.0,
            does_add_eq=True,
        )]
    ),
    InstrumentSource(
        minimum=72, maximum=109, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_12_Xylophone'
        ),
        name='Xylophone_N_12',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=1.4,
            does_add_eq=True,
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=76, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_13_Sax'
        ),
        name='Sax_N_13',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=2.5,
            add_decay_type='decay_long_melody',
            note_yan_yin=6000,
        )]
    ),
    InstrumentSource(
        minimum=40, maximum=86, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_14_Ele_Heavy_Rocker'
        ),
        name='Ele_Heavy_Rocker_N_14',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.4,
            add_decay_type='decay_long_melody',
            note_yan_yin=6000,
        )]
    ),
    InstrumentSource(
        minimum=40, maximum=86, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_15_Ele_Higain_Breather'
        ),
        name='Ele_Higain_Breather_N_15',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.4,
            add_decay_type='decay_long_melody',
            note_yan_yin=6000,
        )]
    ),
    InstrumentSource(
        minimum=40, maximum=86, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_16_Ele_Right_in_Middle'
        ),
        name='Ele_Right_in_Middle_N_16',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.4,
            add_decay_type='decay_long_melody',
            note_yan_yin=6000,
        )]
    ),
    InstrumentSource(
        minimum=55, maximum=107, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_17_Woodwinds_Albion_Hi_Long'
        ),
        name='Woodwinds_Albion_Hi_Long_N_17',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=1.2,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=1000,
            note_yan_yin=lambda unit_time: unit_time * 2
        )]
    ),
    InstrumentSource(
        minimum=60, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_18_Woodwinds_Albion_Hi_Short'
        ),
        name='Woodwinds_Albion_Hi_Short_N_18',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=1.6,
        )]
    ),
    InstrumentSource(
        minimum=55, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_19_Brass_Albion_Hi_Long'
        ),
        name='Brass_Albion_Hi_Long_N_19',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.8,
            add_decay_type='decay_long_melody',
            note_yan_yin=lambda unit_time: unit_time,
            note_ti_qian_yin=1000,
        )]
    ),
    InstrumentSource(
        minimum=55, maximum=86, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_20_Brass_Albion_Hi_Short'
        ),
        name='Brass_Albion_Hi_Short_N_20',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=0.8,
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=86, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_21_ELE_DETALLED'
        ),
        name='N_21_ELE_DETALLED',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.4,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=4000,
            note_yan_yin=lambda unit_time: unit_time,
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=86, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_22_ELE_EPICROCK'
        ),
        name='N_22_ELE_EPICROCK',
        type='melody',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.4,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=3000,
            note_yan_yin=lambda unit_time: unit_time,
        )]
    ),
    InstrumentSource(
        minimum=61, maximum=74, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'N_23_Choir'
        ),
        name='N_23_Choir',
        type='melody'
    ),

    # Bass
    InstrumentSource(
        minimum=36, maximum=76, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_1_Bass'
        ),
        name='Bass_B_1',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.03,
            add_decay_type='decay',
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=67, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_2_Cello'
        ),
        name='Cello_B_2',
        type='bass'
    ),
    InstrumentSource(
        minimum=24, maximum=108, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_3_PianoLarge'
        ),
        name='PianoLarge_B_3',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            instrument_amp=0.18,
            does_add_eq=True,
        )],
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=0.1,
            does_add_eq=True,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=60, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_4_StaBassVio'
        ),
        name='StaBassVio_B_4',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            instrument_amp=1.8,
            does_add_eq=True,
            does_add_712=True,
            does_add_34=True,
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=45, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_5_DeltaBass'
        ),
        name='DeltaBass_B_5',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            instrument_amp=0.8,
            does_add_eq=True,
            does_add_712=True,
            does_add_34=True,
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=38, maximum=82, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_6_Choir'
        ),
        name='Choir_B_6',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=1.5,
            add_decay_type='decay',
            note_ti_qian_yin=1000,
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=76, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_7_FlutePersianNey'
        ),
        name='FlutePersianNey_B_7',
        type='bass',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            add_decay_type='decay_long_melody',
            note_yan_yin=6000,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=74, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_8_Flutesbansuri'
        ),
        name='Flutesbansuri_B_8',
        type='bass',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=2.8,
            add_decay_type='decay_long_melody',
            note_yan_yin=6000,
        )],
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            add_decay_type='decay',
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=96, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_9_Choir1'
        ),
        name='Choir1_B_9',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=2,
            add_decay_type='decay',
            does_add_712_note_to_bass=True,
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=96, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_10_EpicPadAdnromeda'
        ),
        name='EpicPadAdnromeda_B_10',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=1.8,
            add_decay_type='decay',
            does_add_712_note_to_bass=True,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_11_Bass_Dirty_Rock'
        ),
        name='Bass_Dirty_Rock_B_11',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG_CUT,
            instrument_amp=0.1,
            does_add_eq=True,
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_12_Bass_Scooped_Plec'
        ),
        name='Bass_Scooped_Plec_B_12',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG_CUT,
            instrument_amp=0.1,
            does_add_eq=True,
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_13_Bass_Song_Three'
        ),
        name='Bass_Song_Three_B_13',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG_CUT,
            instrument_amp=0.1,
            does_add_eq=True,
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=75, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_14_Bass_Vintage'
        ),
        name='Bass_Vintage_B_14',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG_CUT,
            instrument_amp=0.1,
            does_add_eq=True,
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=73, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_15_Bass_Wilde_Stereo'
        ),
        name='Bass_Wilde_Stereo_B_15',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG_CUT,
            instrument_amp=0.15,
            does_add_eq=True,
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=67, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_16_Woodwinds_Albion_Lo_Long'
        ),
        name='Woodwinds_Albion_Lo_Long_B_16',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.5,
            add_decay_type='decay_hanning',
            note_ti_qian_yin=2000,
            note_yan_yin=18000,
        )]
    ),
    InstrumentSource(
        minimum=24, maximum=67, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_17_Woodwinds_Albion_Lo_Short'
        ),
        name='Woodwinds_Albion_Lo_Short_B_17',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            does_add_eq=True,
            does_add_712=True,
            does_add_rythm=True,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=64, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_18_Brass_Albion_Lo_Long'
        ),
        name='Brass_Albion_Lo_Long_B_18',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.7,
            add_decay_type='decay_hanning',
            note_ti_qian_yin=2000,
            note_yan_yin=lambda unit_time: unit_time * 3,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=65, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_19_Brass_Albion_Lo_Short'
        ),
        name='Brass_Albion_Lo_Short_B_19',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            instrument_amp=0.5,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_20_Brass_Albion_Mid_Long'
        ),
        name='Brass_Albion_Mid_Long_B_20',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.7,
            add_decay_type='decay_hanning',
            note_ti_qian_yin=4500,
            note_yan_yin=lambda unit_time: unit_time * 3,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'B_21_Brass_Albion_Mid_Short'
        ),
        name='Brass_Albion_Mid_Short_B_21',
        type='bass',
        instrument_setting_of_bass=[InstrumentSetting(
            instrument_amp=0.5,
            does_add_rythm=True,
        )]
    ),

    # 中国风
    InstrumentSource(
        minimum=48, maximum=66, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'Z_0_AhhsomeChoir'
        ),
        name='Z_0_AhhsomeChoir',
        type='chinese',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            length_type=InstrumentLengthType.LONG,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=1000,
            note_yan_yin=lambda unit_time: unit_time,
        )]
    ),
    InstrumentSource(
        minimum=50, maximum=71, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'Z_1_Dizi_Leg'
        ),
        name='Z_1_Dizi_Leg',
        type='chinese',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=0.8,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=1000,
            note_yan_yin=lambda unit_time: unit_time,
        )]
    ),
    InstrumentSource(
        minimum=50, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'Z_2_Dizi_Penz'
        ),
        name='Z_2_Dizi_Penz',
        type='chinese',
        instrument_setting_of_note=[InstrumentSetting(
            is_active=False,
            instrument_amp=0.8,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=1000,
            note_yan_yin=lambda unit_time: unit_time,
        )]
    ),
    InstrumentSource(
        minimum=54, maximum=66, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'Z_3_Dizi_Xiao'
        ),
        name='Z_3_Dizi_Xiao',
        type='chinese',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            instrument_amp=1.8,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=1000,
            note_yan_yin=lambda unit_time: unit_time,
        )]
    ),
    InstrumentSource(
        minimum=36, maximum=88, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'Z_4_Guzheng'
        ),
        name='Z_4_Guzheng',
        type='chinese',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=0.5,
            does_add_eq=True,
            does_add_34=True,
        )]
    ),
    # note重复，1个开，1个没开
    InstrumentSource(
        minimum=48, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'Z_5_NanXiao'
        ),
        name='Z_5_NanXiao',
        type='chinese',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=1000,
            note_yan_yin=lambda unit_time: unit_time,
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'Z_6_Piccolo'
        ),
        name='Z_6_Piccolo',
        type='chinese',
        instrument_setting_of_note=[InstrumentSetting(
            length_type=InstrumentLengthType.LONG,
            add_decay_type='decay_long_melody',
            note_ti_qian_yin=1000,
            note_yan_yin=lambda unit_time: unit_time,
        )]
    ),
    InstrumentSource(
        minimum=48, maximum=95, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'Z_7_Zheng'
        ),
        name='Z_7_Zheng',
        type='chinese',
        instrument_setting_of_note=[InstrumentSetting(
            instrument_amp=0.6,
            does_add_eq=True,
        )]
    ),

    # Drum,
    InstrumentSource(
        minimum=0, maximum=3, offset=0,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'D_0_FireflyDrum'
        ),
        name='FireflyDrum_D_0',
        type='drum'
    ),
    InstrumentSource(
        minimum=0, maximum=11, offset=0,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'D_1_RefrainDrum'
        ),
        name='RefrainDrum_D_1',
        type='drum'
    ),
    InstrumentSource(
        minimum=0, maximum=4, offset=0,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'D_2_ContinueVoyageDrum'
        ),
        name='ContinueVoyageDrum_D_2',
        type='drum'
    ),
    InstrumentSource(
        minimum=0, maximum=3, offset=0,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'D_3_CANdrum'
        ),
        name='CANDrum_D_3',
        type='drum'
    ),
    InstrumentSource(
        minimum=0, maximum=5, offset=0,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'D_4_Bingdrum'
        ),
        name='BingDrum_D_4',
        type='drum'
    ),
    InstrumentSource(
        minimum=0, maximum=2, offset=0,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'D_5_Niandrum'
        ),
        name='NianDrum_D_5',
        type='drum'
    ),
    InstrumentSource(
        minimum=0, maximum=3, offset=0,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'D_6_Tingdrum'
        ),
        name='TingDrum_D_6',
        type='drum'
    ),
    InstrumentSource(
        minimum=0, maximum=4, offset=0,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'D_7_Wuxindrum'
        ),
        name='WuxinDrum_D_7',
        type='drum'
    ),
    InstrumentSource(
        minimum=0, maximum=9, offset=0,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'D_8_WuHouCidrum'
        ),
        name='WuHouDrum_D_8',
        type='drum'
    ),
    InstrumentSource(
        minimum=0, maximum=2, offset=0,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'D_9_XueyueHuadrum'
        ),
        name='XueyueHuaDrum_D_9',
        type='drum'
    ),
    InstrumentSource(
        minimum=36, maximum=71, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'D_10_BiosDrum'
        ),
        name='BiosDrum_D_10',
        type='drum'
    ),
    InstrumentSource(
        minimum=36, maximum=39, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'D2_5_Niandrum'
        ),
        name='NianDrum_D2_5',
        type='drum'
    ),
    InstrumentSource(
        minimum=35, maximum=51, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'D2_7_Wuxindrum'
        ),
        name='WuxinDrum_D2_7',
        type='drum'
    ),
    # Rise
    InstrumentSource(
        minimum=0, maximum=13, offset=0,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'Rise_0', 'Rise0'
        ),
        name='Rise_0',
        type='drum'
    ),
    InstrumentSource(
        minimum=9, maximum=82, offset=0,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'Rise_0', 'Rise1'
        ),
        name='Rise_1',
        type='drum'
    ),
    # 水印
    InstrumentSource(
        minimum=0, maximum=1, offset=0,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'Shuiyin'
        ),
        name='Shuiyin',
        type='drum'
    ),
    # 效果

    InstrumentSource(
        minimum=0, maximum=5, offset=0,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_0_Bell'
        ),
        name='Bell',
        type='effect'
    ),
    InstrumentSource(
        minimum=36, maximum=71, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_1_Pad', 'AmbientBass'
        ),
        name='E_1_Pad_AmbientBass',
        type='effect'
    ),
    InstrumentSource(
        minimum=29, maximum=60, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_1_Pad', 'AmbientBassFifths'
        ),
        name='E_1_Pad_AmbientBassFifths',
        type='effect'
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_1_Pad', 'BellCurve'
        ),
        name='E_1_Pad_BellCurve',
        type='effect'
    ),
    InstrumentSource(
        minimum=36, maximum=65, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_1_Pad', 'Clouds'
        ),
        name='E_1_Pad_Clouds',
        type='effect'
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_1_Pad', 'DiziPad'
        ),
        name='E_1_Pad_DiziPad',
        type='effect'
    ),
    InstrumentSource(
        minimum=28, maximum=60, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_1_Pad', 'FatAmbientBass'
        ),
        name='E_1_Pad_FatAmbientBass',
        type='effect'
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_1_Pad', 'FlutterPad'
        ),
        name='E_1_Pad_FlutterPad',
        type='effect'
    ),
    InstrumentSource(
        minimum=48, maximum=84, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_1_Pad', 'HorizonPad'
        ),
        name='E_1_Pad_HorizonPad',
        type='effect'
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_1_Pad', 'PadAirGuita'
        ),
        name='E_1_Pad_PadAirGuita',
        type='effect'
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_1_Pad', 'PedalSteel'
        ),
        name='E_1_Pad_PedalSteel',
        type='effect'
    ),
    InstrumentSource(
        minimum=41, maximum=65, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_1_Pad', 'ReverseDistancePad'
        ),
        name='E_1_Pad_ReverseDistancePad',
        type='effect'
    ),
    InstrumentSource(
        minimum=60, maximum=91, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_1_Pad', 'SusMPLegErhu'
        ),
        name='E_1_Pad_SusMPLegErhu',
        type='effect'
    ),
    InstrumentSource(
        minimum=60, maximum=91, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_1_Pad', 'SusMPLegErhu2'
        ),
        name='E_1_Pad_SusMPLegErhu2',
        type='effect'
    ),
    InstrumentSource(
        minimum=36, maximum=72, offset=12,
        path=os.path.join(
            note_resources_path, 'note_resources',
            'E_1_Pad', 'TonalPercussion'
        ),
        name='E_1_Pad_TonalPercussion',
        type='effect'
    ),
]

# ======================

piano_source = InstrumentSource(
    minimum=24, maximum=108, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_0_Piano200319'
    ),
    type='melody'
)
EleGuita_source = InstrumentSource(
    minimum=48, maximum=86, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_1_EleGuita'
    ),
    type='melody'
)
Guita_source = InstrumentSource(
    minimum=57, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_2_Guita'
    ),
    type='melody'
)
Pianoshort_source = InstrumentSource(
    minimum=24, maximum=108, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_3_Pianoshort'
    ),
    type='melody'
)
DeepMode_source = InstrumentSource(
    minimum=48, maximum=96, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_4_DeepMode'
    ),
    type='melody'
)
FluteandStrings_source = InstrumentSource(
    minimum=48, maximum=96, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_5_FluteandStrings'
    ),
    type='melody'
)
PianoGrand_source = InstrumentSource(
    minimum=36, maximum=108, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_6_PianoGrand'
    ),
    type='melody'
)
PianoPopKey_source = InstrumentSource(
    minimum=36, maximum=108, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_7_PianoPopKey'
    ),
    type='melody'
)
GenPiano_source = InstrumentSource(
    minimum=36, maximum=96, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_8_GenPiano'
    ),
    type='melody'
)
Violas_source = InstrumentSource(
    minimum=48, maximum=85, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_9_Violas'
    ),
    type='melody'
)

A_10_Joshua_JoshuaContourVioLong_source = InstrumentSource(
    minimum=55, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_10_Joshua', 'JoshuaContourVioLong'
    ),
    type='melody'
)
A_10_Joshua_JoshuaContourVioShort_source = InstrumentSource(
    minimum=55, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_10_Joshua', 'JoshuaContourVioShort'
    ),
    type='melody'
)
A_10_Joshua_JoshuaHarmonicVio_source = InstrumentSource(
    minimum=55, maximum=88, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_10_Joshua', 'JoshuaHarmonicVio'
    ),
    type='melody'
)
A_10_Joshua_JoshuaLongVio_source = InstrumentSource(
    minimum=55, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_10_Joshua', 'JoshuaLongVio'
    ),
    type='melody'
)
A_10_Joshua_JoshuaSpiccato_source = InstrumentSource(
    minimum=55, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_10_Joshua', 'JoshuaSpiccato'
    ),
    type='melody'
)
A_10_Joshua_JoshuaStaVio_source = InstrumentSource(
    minimum=55, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_10_Joshua', 'JoshuaStaVio'
    ),
    type='melody'
)

A_11_Nucleus_0_3Trump6Frnchhrns8va_Legato_source = InstrumentSource(
    minimum=42, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path,
        'note_resources',
        'A_11_Nucleus',
        '3Trump6Frnchhrns8va_Legato'
    ),
    type='melody'
)
A_11_Nucleus_1_4Trmb2Tb8Va_Sustained_source = InstrumentSource(
    minimum=29, maximum=51, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_11_Nucleus',
        '4Trmb2Tb8Va_Sustained'
    ),
    type='melody'
)
A_11_Nucleus_2_6Cello_4Bass_Spiccato_source = InstrumentSource(
    minimum=24, maximum=48, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_11_Nucleus',
        '6Cello_4Bass_Spiccato'
    ),
    type='melody'
)
A_11_Nucleus_3_6Cello_4Bass_Sustained_source = InstrumentSource(
    minimum=24, maximum=48, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_11_Nucleus',
        '6Cello_4Bass_Sustained'
    ),
    type='melody'
)
A_11_Nucleus_4_Bass_Spiccato_source = InstrumentSource(
    minimum=24, maximum=48, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_11_Nucleus', 'Bass_Spiccato'
    ),
    type='melody'
)
A_11_Nucleus_5_Bass_Sustained_source = InstrumentSource(
    minimum=24, maximum=48, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_11_Nucleus', 'Bass_Sustained'
    ),
    type='melody'
)
A_11_Nucleus_6_Brass_Full_source = InstrumentSource(
    minimum=29, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_11_Nucleus', 'Brass_Full'
    ),
    type='melody'
)
A_11_Nucleus_7_Brass_Full_Staccatissimo_source = InstrumentSource(
    minimum=48, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path,
        'note_resources',
        'A_11_Nucleus',
        'Brass_Full_Staccatissimo'
    ),
    type='melody'
)
A_11_Nucleus_8_Cellos_Legato_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_11_Nucleus', 'Cellos_Legato'
    ),
    type='melody'
)
A_11_Nucleus_9_Cellos_Pizzicato_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_11_Nucleus', 'Cellos_Pizzicato'
    ),
    type='melody'
)
A_11_Nucleus_10_Cellos_Spiccato_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_11_Nucleus', 'Cellos_Spiccato'
    ),
    type='melody'
)
A_11_Nucleus_11_Choir_Sopranos_Staccato_source = InstrumentSource(
    minimum=60, maximum=74, offset=12,
    path=os.path.join(
        note_resources_path,
        'note_resources',
        'A_11_Nucleus',
        'Choir_Sopranos_Staccato'
    ),
    type='melody'
)
A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source = InstrumentSource(
    minimum=60, maximum=78, offset=12,
    path=os.path.join(
        note_resources_path,
        'note_resources',
        'A_11_Nucleus',
        'Choir_Sopranos_Sustained_A'
    ),
    type='melody'
)
A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source = InstrumentSource(
    minimum=60, maximum=78, offset=12,
    path=os.path.join(
        note_resources_path,
        'note_resources',
        'A_11_Nucleus',
        'Choir_Sopranos_Sustained_O'
    ),
    type='melody'
)
A_11_Nucleus_14_Low_Brass_Sustained_source = InstrumentSource(
    minimum=29, maximum=53, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_11_Nucleus', 'Low_Brass_Sustained'
    ),
    type='melody'
)
A_11_Nucleus_15_VioViaChord_Pizzicato_source = InstrumentSource(
    minimum=48, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_11_Nucleus',
        'VioViaChord_Pizzicato'
    ),
    type='melody'
)
A_11_Nucleus_16_VioViaChord_Spiccato_source = InstrumentSource(
    minimum=48, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_11_Nucleus',
        'VioViaChord_Spiccato'
    ),
    type='melody'
)
A_11_Nucleus_17_VioViaChord_Sustained_source = InstrumentSource(
    minimum=48, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_11_Nucleus',
        'VioViaChord_Sustained'
    ),
    type='melody'
)
A_11_Nucleus_18_VioViaChord_Tremolo_source = InstrumentSource(
    minimum=48, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_11_Nucleus', 'VioViaChord_Tremolo'
    ),
    type='melody'
)
A_12_PianoGrandeursoft_source = InstrumentSource(
    minimum=24, maximum=96, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_12_PianoGrandeursoft'
    ),
    type='melody'
)
A_13_PianoGrandeurSoft2_source = InstrumentSource(
    minimum=24, maximum=96, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_13_PianoGrandeurSoft2'
    ),
    type='melody'
)
A_14_PianoMaverickSoft_source = InstrumentSource(
    minimum=24, maximum=96, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_14_PianoMaverickSoft'
    ),
    type='melody'
)
A_15_AmpleGuitaRaw_source = InstrumentSource(
    minimum=40, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'A_15_AmpleGuitaRaw'
    ),
    type='melody'
)

# Note
Guita2_N_1_source = InstrumentSource(
    minimum=48, maximum=86, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_1_Guita2'
    ),
    type='melody'
)
Guzheng_N_2_source = InstrumentSource(
    minimum=48, maximum=98, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_2_Guzheng'
    ),
    type='melody'
)  # 特殊，一些音没有

Kora_N_3_source = InstrumentSource(
    minimum=48, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_3_Kora'
    ),
    type='melody'
)
StaHighVio_N_4_source = InstrumentSource(
    minimum=48, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_4_StaHighVio'
    ),
    type='melody'
)
Nyatiti_N_5_source = InstrumentSource(
    minimum=48, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_5_Nyatiti'
    ),
    type='melody'
)
Oud_N_6_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_6_Oud'
    ),
    type='melody'
)
MuteGuita_N_7_source = InstrumentSource(
    minimum=60, maximum=108, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_7_MuteGuita'
    ),
    type='melody'
)
MuteGuita2_N_8_source = InstrumentSource(
    minimum=60, maximum=108, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_8_MuteGuita2'
    ),
    type='melody'
)
Och_N_9_source = InstrumentSource(
    minimum=36, maximum=91, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_9_Och'
    ),
    type='melody'
)
ViolinLong_N_10_source = InstrumentSource(
    minimum=60, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_10_ViolinLong'
    ),
    type='melody'
)
Marimba_N_11_source = InstrumentSource(
    minimum=48, maximum=96, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_11_Marimba'
    ),
    type='melody'
)
Xylophone_N_12_source = InstrumentSource(
    minimum=72, maximum=109, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_12_Xylophone'
    ),
    type='melody'
)
Sax_N_13_source = InstrumentSource(
    minimum=48, maximum=76, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_13_Sax'
    ),
    type='melody'
)

Ele_Heavy_Rocker_N_14_source = InstrumentSource(
    minimum=40, maximum=86, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_14_Ele_Heavy_Rocker'
    ),
    type='melody'
)
Ele_Higain_Breather_N_15_source = InstrumentSource(
    minimum=40, maximum=86, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_15_Ele_Higain_Breather'
    ),
    type='melody'
)
Ele_Right_in_Middle_N_16_source = InstrumentSource(
    minimum=40, maximum=86, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_16_Ele_Right_in_Middle'
    ),
    type='melody'
)
Woodwinds_Albion_Hi_Long_N_17_source = InstrumentSource(
    minimum=55, maximum=107, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_17_Woodwinds_Albion_Hi_Long'
    ),
    type='melody'
)
Woodwinds_Albion_Hi_Short_N_18_source = InstrumentSource(
    minimum=60, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_18_Woodwinds_Albion_Hi_Short'
    ),
    type='melody'
)

Brass_Albion_Hi_Long_N_19_source = InstrumentSource(
    minimum=55, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_19_Brass_Albion_Hi_Long'
    ),
    type='melody'
)
Brass_Albion_Hi_Short_N_20_source = InstrumentSource(
    minimum=55, maximum=86, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_20_Brass_Albion_Hi_Short'
    ),
    type='melody'
)
N_21_ELE_DETALLED_source = InstrumentSource(
    minimum=48, maximum=86, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_21_ELE_DETALLED'
    ),
    type='melody'
)
N_22_ELE_EPICROCK_source = InstrumentSource(
    minimum=48, maximum=86, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_22_ELE_EPICROCK'
    ),
    type='melody'
)
N_23_Choir_source = InstrumentSource(
    minimum=61, maximum=74, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'N_23_Choir'
    ),
    type='melody'
)

# Bass
Bass_B_1_source = InstrumentSource(
    minimum=36, maximum=76, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_1_Bass'
    ),
    type='bass'
)
Cello_B_2_source = InstrumentSource(
    minimum=36, maximum=67, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_2_Cello'
    ),
    type='bass'
)
PianoLarge_B_3_source = InstrumentSource(
    minimum=24, maximum=108, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_3_PianoLarge'
    ),
    type='bass'
)
StaBassVio_B_4_source = InstrumentSource(
    minimum=36, maximum=60, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_4_StaBassVio'
    ),
    type='bass'
)
DeltaBass_B_5_source = InstrumentSource(
    minimum=45, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_5_DeltaBass'
    ),
    type='bass'
)
Choir_B_6_source = InstrumentSource(
    minimum=38, maximum=82, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_6_Choir'
    ),
    type='bass'
)
FlutePersianNey_B_7_source = InstrumentSource(
    minimum=48, maximum=76, offset=12,
    path=os.path.join(
        note_resources_path,
        'note_resources',
        'B_7_FlutePersianNey'
    ),
    type='bass'
)
Flutesbansuri_B_8_source = InstrumentSource(
    minimum=36, maximum=74, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_8_Flutesbansuri'
    ),
    type='bass'
)
Choir1_B_9_source = InstrumentSource(
    minimum=48, maximum=96, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_9_Choir1'
    ),
    type='bass'
)
EpicPadAdnromeda_B_10_source = InstrumentSource(
    minimum=48, maximum=96, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_10_EpicPadAdnromeda'
    ),
    type='bass'
)

Bass_Dirty_Rock_B_11_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_11_Bass_Dirty_Rock'
    ),
    type='bass'
)
Bass_Scooped_Plec_B_12_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_12_Bass_Scooped_Plec'
    ),
    type='bass'
)
Bass_Song_Three_B_13_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_13_Bass_Song_Three'
    ),
    type='bass'
)
Bass_Vintage_B_14_source = InstrumentSource(
    minimum=36, maximum=75, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_14_Bass_Vintage'
    ),
    type='bass'
)
Bass_Wilde_Stereo_B_15_source = InstrumentSource(
    minimum=36, maximum=73, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_15_Bass_Wilde_Stereo'
    ),
    type='bass'
)
Woodwinds_Albion_Lo_Long_B_16_source = InstrumentSource(
    minimum=36, maximum=67, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_16_Woodwinds_Albion_Lo_Long'
    ),
    type='bass'
)
Woodwinds_Albion_Lo_Short_B_17_source = InstrumentSource(
    minimum=24, maximum=67, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_17_Woodwinds_Albion_Lo_Short'
    ),
    type='bass'
)
Brass_Albion_Lo_Long_B_18_source = InstrumentSource(
    minimum=36, maximum=64, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_18_Brass_Albion_Lo_Long'
    ),
    type='bass'
)
Brass_Albion_Lo_Short_B_19_source = InstrumentSource(
    minimum=36, maximum=65, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_19_Brass_Albion_Lo_Short'
    ),
    type='bass'
)
Brass_Albion_Mid_Long_B_20_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_20_Brass_Albion_Mid_Long'
    ),
    type='bass'
)
Brass_Albion_Mid_Short_B_21_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'B_21_Brass_Albion_Mid_Short'
    ),
    type='bass'
)

# 中国风
Z_0_AhhsomeChoir_source = InstrumentSource(
    minimum=48, maximum=66, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'Z_0_AhhsomeChoir'
    )
)
Z_1_Dizi_Leg_source = InstrumentSource(
    minimum=50, maximum=71, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'Z_1_Dizi_Leg'
    )
)
Z_2_Dizi_Penz_source = InstrumentSource(
    minimum=50, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'Z_2_Dizi_Penz'
    )
)
Z_3_Dizi_Xiao_source = InstrumentSource(
    minimum=54, maximum=66, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'Z_3_Dizi_Xiao'
    )
)
Z_4_Guzheng_source = InstrumentSource(
    minimum=36, maximum=88, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'Z_4_Guzheng'
    )
)
Z_5_NanXiao_source = InstrumentSource(
    minimum=48, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'Z_5_NanXiao'
    )
)
Z_6_Piccolo_source = InstrumentSource(
    minimum=48, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'Z_6_Piccolo'
    )
)
Z_7_Zheng_source = InstrumentSource(
    minimum=48, maximum=95, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'Z_7_Zheng'
    )
)

# Drum
FireflyDrum_D_0_source = InstrumentSource(
    minimum=0, maximum=3, offset=0,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'D_0_FireflyDrum'
    )
)
RefrainDrum_D_1_source = InstrumentSource(
    minimum=0, maximum=11, offset=0,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'D_1_RefrainDrum'
    )
)
ContinueVoyageDrum_D_2_source = InstrumentSource(
    minimum=0, maximum=4, offset=0,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'D_2_ContinueVoyageDrum'
    )
)
CANDrum_D_3_source = InstrumentSource(
    minimum=0, maximum=3, offset=0,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'D_3_CANdrum'
    )
)
BingDrum_D_4_source = InstrumentSource(
    minimum=0, maximum=5, offset=0,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'D_4_Bingdrum'
    )
)

NianDrum_D_5_source = InstrumentSource(
    minimum=0, maximum=2, offset=0,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'D_5_Niandrum'
    )
)

TingDrum_D_6_source = InstrumentSource(
    minimum=0, maximum=3, offset=0,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'D_6_Tingdrum'
    )
)
WuxinDrum_D_7_source = InstrumentSource(
    minimum=0, maximum=4, offset=0,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'D_7_Wuxindrum'
    )
)
WuHouDrum_D_8_source = InstrumentSource(
    minimum=0, maximum=9, offset=0,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'D_8_WuHouCidrum'
    )
)
XueyueHuaDrum_D_9_source = InstrumentSource(
    minimum=0, maximum=2, offset=0,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'D_9_XueyueHuadrum'
    )
)
BiosDrum_D_10_source = InstrumentSource(
    minimum=36, maximum=71, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'D_10_BiosDrum'
    )
)
NianDrum_D2_5_source = InstrumentSource(
    minimum=36, maximum=39, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'D2_5_Niandrum'
    )
)
WuxinDrum_D2_7_source = InstrumentSource(
    minimum=35, maximum=51, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'D2_7_Wuxindrum'
    )
)
# Rise
Rise_0_source = InstrumentSource(
    minimum=0, maximum=13, offset=0,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'Rise_0', 'Rise0'
    )
)
Rise_1_source = InstrumentSource(
    minimum=9, maximum=82, offset=0,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'Rise_0', 'Rise1'
    )
)
# 水印
Shuiyin_source = InstrumentSource(
    minimum=0, maximum=1, offset=0,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'Shuiyin'
    )
)
# 效果
Bell_source = InstrumentSource(
    minimum=0, maximum=5, offset=0,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_0_Bell'
    )
)
E_1_Pad_AmbientBass_source = InstrumentSource(
    minimum=36, maximum=71, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_1_Pad', 'AmbientBass'
    )
)
E_1_Pad_AmbientBassFifths_source = InstrumentSource(
    minimum=29, maximum=60, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_1_Pad', 'AmbientBassFifths'
    )
)
E_1_Pad_BellCurve_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_1_Pad', 'BellCurve'
    )
)
E_1_Pad_Clouds_source = InstrumentSource(
    minimum=36, maximum=65, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_1_Pad', 'Clouds'
    )
)
E_1_Pad_DiziPad_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_1_Pad', 'DiziPad'
    )
)
E_1_Pad_FatAmbientBass_source = InstrumentSource(
    minimum=28, maximum=60, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_1_Pad', 'FatAmbientBass'
    )
)
E_1_Pad_FlutterPad_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_1_Pad', 'FlutterPad'
    )
)
E_1_Pad_HorizonPad_source = InstrumentSource(
    minimum=48, maximum=84, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_1_Pad', 'HorizonPad'
    )
)
E_1_Pad_PadAirGuita_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_1_Pad', 'PadAirGuita'
    )
)
E_1_Pad_PedalSteel_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_1_Pad', 'PedalSteel'
    )
)
E_1_Pad_ReverseDistancePad_source = InstrumentSource(
    minimum=41, maximum=65, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_1_Pad', 'ReverseDistancePad'
    )
)
E_1_Pad_SusMPLegErhu_source = InstrumentSource(
    minimum=60, maximum=91, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_1_Pad', 'SusMPLegErhu'
    )
)
E_1_Pad_SusMPLegErhu2_source = InstrumentSource(
    minimum=60, maximum=91, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_1_Pad', 'SusMPLegErhu2'
    )
)
E_1_Pad_TonalPercussion_source = InstrumentSource(
    minimum=36, maximum=72, offset=12,
    path=os.path.join(
        note_resources_path, 'note_resources',
        'E_1_Pad', 'TonalPercussion'
    )
)


class FileManager:
    # Current absolute path
    base_path = os.path.abspath(os.path.dirname(__file__))

    def __init__(self, setting_stamp='', load_stamp=''):
        # The hole stamp includes 2 parts: 1st is timestamp, 2ed is setting_stamp.
        # The parameter load_stamp is hole stamp.
        # A FileManager instance can be restored by only (hole) stamp.
        if load_stamp:
            self.stamp = load_stamp
        else:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')
            self.stamp = timestamp + '_' + setting_stamp if setting_stamp else timestamp
        self.__setOutputPath()
        self.__setModelPath()
        self.__setResourcePath()

    def __eq__(self, other):
        return self.stamp == other.stamp

    # Output file paths
    def __setOutputPath(self):
        # Create file paths based on self.stamp
        base_path = self.base_path
        stamp = self.stamp
        # wav
        self.wav_music_output_name = {str(i): os.path.join(
            base_path, 'output', 'wav',
            stamp + '_' + str(i) + '.wav'
        )
            for i in range(1, 4)}
        self.wav_mj_output_name = os.path.join(
            base_path, 'output', 'wav',
            stamp + '_mm' + '.wav'
        )

        self.wav_fd_output_name = os.path.join(
            base_path, 'output', 'wav',
            stamp + '_ff' + '.wav'
        )

        self.wav_drum_output_name = os.path.join(
            base_path, 'output', 'wav',
            stamp + '_drum' + '.wav'
        )
        # mp3
        self.mp3_music_output_name = {str(i): os.path.join(
            base_path, 'output', 'mp3',
            stamp + '_' + str(i) + '.mp3'
        )
            for i in range(1, 4)}
        # midi
        self.midi_sing_output_name = os.path.join(
            base_path, 'output', 'midi',
            stamp + '_sing.mid'
        )

        self.midi_base_output_name = os.path.join(
            base_path, 'output', 'midi',
            stamp + '_base.mid'
        )
        self.midi_melody_output_name = {str(i): os.path.join(
            base_path, 'output', 'midi',
            stamp + '_melody_' + str(i) + '.mid'
        )
            for i in range(1, 4)}
        # np.array in txt
        self.array_base_output_name = os.path.join(
            base_path, 'output', 'array',
            stamp + '_base.txt'
        )
        self.array_base_instrument_name = {str(i): os.path.join(
            base_path, 'output', 'array',
            stamp + '_base_instrument_' + str(i) + '.txt'
        )
            for i in range(1, 4)}
        self.array_melody_output_name = {str(i): os.path.join(
            base_path, 'output', 'array',
            stamp + '_melody_' + str(i) + '.txt'
        )
            for i in range(1, 4)}
        self.array_melody_instrument_name = {str(i): os.path.join(
            base_path, 'output', 'array',
            stamp + '_melody_instrument_' + str(i) + '.txt'
        )
            for i in range(1, 4)}
        self.setting_output_name = os.path.join(
            base_path, 'output', 'setting',
            stamp + '.setting'
        )

    # Tensorflow model files
    def __setModelPath(self):
        # self.model_base_name = 'Midi3.1_all_midi_2_Ctonality'
        # self.model_base_name = '/2020.3.2小model/Midi3.1_all_midi_2_Ctonality'
        # self.model_name = os.path.join('2020330小model', '0330Ctonality.ckpt')
        self.model_name = os.path.join(
            self.base_path, 'model', '2020328小model',
            '0327Ctonality.ckpt'
        )  # 这个模型重音太多，好在小，运算起来快
        self.model_path = os.path.join(self.base_path, 'model')
        self.model = os.path.join(self.model_path, self.model_name)

    # Sound source
    def __setResourcePath(self):
        # self.instruments = instruments
        # instrument wav file
        self.piano_source = piano_source
        self.EleGuita_source = EleGuita_source
        self.Guita_source = Guita_source
        self.Pianoshort_source = Pianoshort_source
        self.DeepMode_source = DeepMode_source
        self.FluteandStrings_source = FluteandStrings_source
        self.PianoGrand_source = PianoGrand_source
        self.PianoPopKey_source = PianoPopKey_source
        self.GenPiano_source = GenPiano_source
        self.Violas_source = Violas_source
        self.A_10_Joshua_JoshuaContourVioLong_source = A_10_Joshua_JoshuaContourVioLong_source
        self.A_10_Joshua_JoshuaContourVioShort_source = A_10_Joshua_JoshuaContourVioShort_source
        self.A_10_Joshua_JoshuaHarmonicVio_source = A_10_Joshua_JoshuaHarmonicVio_source
        self.A_10_Joshua_JoshuaLongVio_source = A_10_Joshua_JoshuaLongVio_source
        self.A_10_Joshua_JoshuaSpiccato_source = A_10_Joshua_JoshuaSpiccato_source
        self.A_10_Joshua_JoshuaStaVio_source = A_10_Joshua_JoshuaStaVio_source

        self.A_11_Nucleus_0_3Trump6Frnchhrns8va_Legato_source = A_11_Nucleus_0_3Trump6Frnchhrns8va_Legato_source  # N
        self.A_11_Nucleus_1_4Trmb2Tb8Va_Sustained_source = A_11_Nucleus_1_4Trmb2Tb8Va_Sustained_source  # B
        self.A_11_Nucleus_2_6Cello_4Bass_Spiccato_source = A_11_Nucleus_2_6Cello_4Bass_Spiccato_source  # B
        self.A_11_Nucleus_3_6Cello_4Bass_Sustained_source = A_11_Nucleus_3_6Cello_4Bass_Sustained_source  # B
        self.A_11_Nucleus_4_Bass_Spiccato_source = A_11_Nucleus_4_Bass_Spiccato_source  # B
        self.A_11_Nucleus_5_Bass_Sustained_source = A_11_Nucleus_5_Bass_Sustained_source  # B
        self.A_11_Nucleus_6_Brass_Full_source = A_11_Nucleus_6_Brass_Full_source  # A
        self.A_11_Nucleus_7_Brass_Full_Staccatissimo_source = A_11_Nucleus_7_Brass_Full_Staccatissimo_source
        self.A_11_Nucleus_8_Cellos_Legato_source = A_11_Nucleus_8_Cellos_Legato_source  # B
        self.A_11_Nucleus_9_Cellos_Pizzicato_source = A_11_Nucleus_9_Cellos_Pizzicato_source  # B
        self.A_11_Nucleus_10_Cellos_Spiccato_source = A_11_Nucleus_10_Cellos_Spiccato_source  # B
        self.A_11_Nucleus_11_Choir_Sopranos_Staccato_source = A_11_Nucleus_11_Choir_Sopranos_Staccato_source  # A
        self.A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source = A_11_Nucleus_12_Choir_Sopranos_Sustained_A_source  # A
        self.A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source = A_11_Nucleus_13_Choir_Sopranos_Sustained_O_source  # A
        self.A_11_Nucleus_14_Low_Brass_Sustained_source = A_11_Nucleus_14_Low_Brass_Sustained_source  # B

        self.A_11_Nucleus_15_VioViaChord_Pizzicato_source = A_11_Nucleus_15_VioViaChord_Pizzicato_source  # N
        self.A_11_Nucleus_16_VioViaChord_Spiccato_source = A_11_Nucleus_16_VioViaChord_Spiccato_source  # N
        self.A_11_Nucleus_17_VioViaChord_Sustained_source = A_11_Nucleus_17_VioViaChord_Sustained_source  # N
        self.A_11_Nucleus_18_VioViaChord_Tremolo_source = A_11_Nucleus_18_VioViaChord_Tremolo_source  # N

        self.A_12_PianoGrandeursoft_source = A_12_PianoGrandeursoft_source
        self.A_13_PianoGrandeurSoft2_source = A_13_PianoGrandeurSoft2_source
        self.A_14_PianoMaverickSoft_source = A_14_PianoMaverickSoft_source
        self.A_15_AmpleGuitaRaw_source = A_15_AmpleGuitaRaw_source

        # Note
        self.Guita2_N_1_source = Guita2_N_1_source
        self.Guzheng_N_2_source = Guzheng_N_2_source
        self.Kora_N_3_source = Kora_N_3_source
        self.StaHighVio_N_4_source = StaHighVio_N_4_source
        self.Nyatiti_N_5_source = Nyatiti_N_5_source
        self.Oud_N_6_source = Oud_N_6_source
        self.MuteGuita_N_7_source = MuteGuita_N_7_source
        self.MuteGuita2_N_8_source = MuteGuita2_N_8_source
        self.Och_N_9_source = Och_N_9_source
        self.ViolinLong_N_10_source = ViolinLong_N_10_source
        self.Marimba_N_11_source = Marimba_N_11_source
        self.Xylophone_N_12_source = Xylophone_N_12_source
        self.Sax_N_13_source = Sax_N_13_source

        self.Ele_Heavy_Rocker_N_14_source = Ele_Heavy_Rocker_N_14_source
        self.Ele_Higain_Breather_N_15_source = Ele_Higain_Breather_N_15_source
        self.Ele_Right_in_Middle_N_16_source = Ele_Right_in_Middle_N_16_source
        self.Woodwinds_Albion_Hi_Long_N_17_source = Woodwinds_Albion_Hi_Long_N_17_source
        self.Woodwinds_Albion_Hi_Short_N_18_source = Woodwinds_Albion_Hi_Short_N_18_source
        self.Brass_Albion_Hi_Long_N_19_source = Brass_Albion_Hi_Long_N_19_source
        self.Brass_Albion_Hi_Short_N_20_source = Brass_Albion_Hi_Short_N_20_source
        self.N_21_ELE_DETALLED_source = N_21_ELE_DETALLED_source
        self.N_22_ELE_EPICROCK_source = N_22_ELE_EPICROCK_source
        self.N_23_Choir_source = N_23_Choir_source

        # Bass
        self.Bass_B_1_source = Bass_B_1_source
        self.Cello_B_2_source = Cello_B_2_source
        self.PianoLarge_B_3_source = PianoLarge_B_3_source
        self.StaBassVio_B_4_source = StaBassVio_B_4_source
        self.DeltaBass_B_5_source = DeltaBass_B_5_source
        self.Choir_B_6_source = Choir_B_6_source
        self.FlutePersianNey_B_7_source = FlutePersianNey_B_7_source
        self.Flutesbansuri_B_8_source = Flutesbansuri_B_8_source
        self.Choir1_B_9_source = Choir1_B_9_source
        self.EpicPadAdnromeda_B_10_source = EpicPadAdnromeda_B_10_source

        self.Bass_Dirty_Rock_B_11_source = Bass_Dirty_Rock_B_11_source
        self.Bass_Scooped_Plec_B_12_source = Bass_Scooped_Plec_B_12_source
        self.Bass_Song_Three_B_13_source = Bass_Song_Three_B_13_source
        self.Bass_Vintage_B_14_source = Bass_Vintage_B_14_source
        self.Bass_Wilde_Stereo_B_15_source = Bass_Wilde_Stereo_B_15_source
        self.Woodwinds_Albion_Lo_Long_B_16_source = Woodwinds_Albion_Lo_Long_B_16_source
        self.Woodwinds_Albion_Lo_Short_B_17_source = Woodwinds_Albion_Lo_Short_B_17_source
        self.Brass_Albion_Lo_Long_B_18_source = Brass_Albion_Lo_Long_B_18_source
        self.Brass_Albion_Lo_Short_B_19_source = Brass_Albion_Lo_Short_B_19_source
        self.Brass_Albion_Mid_Long_B_20_source = Brass_Albion_Mid_Long_B_20_source
        self.Brass_Albion_Mid_Short_B_21_source = Brass_Albion_Mid_Short_B_21_source

        # Drum
        self.FireflyDrum_D_0_source = FireflyDrum_D_0_source
        self.RefrainDrum_D_1_source = RefrainDrum_D_1_source
        self.ContinueVoyageDrum_D_2_source = ContinueVoyageDrum_D_2_source
        self.CANDrum_D_3_source = CANDrum_D_3_source
        self.BingDrum_D_4_source = BingDrum_D_4_source
        self.NianDrum_D_5_source = NianDrum_D_5_source
        self.TingDrum_D_6_source = TingDrum_D_6_source
        self.WuxinDrum_D_7_source = WuxinDrum_D_7_source
        self.WuHouDrum_D_8_source = WuHouDrum_D_8_source
        self.XueyueHuaDrum_D_9_source = XueyueHuaDrum_D_9_source
        self.BiosDrum_D_10_source = BiosDrum_D_10_source
        self.NianDrum_D2_5_source = NianDrum_D2_5_source
        self.WuxinDrum_D2_7_source = WuxinDrum_D2_7_source

        # 中国风
        self.Z_0_AhhsomeChoir_source = Z_0_AhhsomeChoir_source
        self.Z_1_Dizi_Leg_source = Z_1_Dizi_Leg_source
        self.Z_2_Dizi_Penz_source = Z_2_Dizi_Penz_source
        self.Z_3_Dizi_Xiao_source = Z_3_Dizi_Xiao_source
        self.Z_4_Guzheng_source = Z_4_Guzheng_source
        self.Z_5_NanXiao_source = Z_5_NanXiao_source
        self.Z_6_Piccolo_source = Z_6_Piccolo_source
        self.Z_7_Zheng_source = Z_7_Zheng_source

        # Rise
        self.Rise_0_source = Rise_0_source
        self.Rise_1_source = Rise_1_source
        # 水印
        self.Shuiyin_source = Shuiyin_source
        # 效果
        self.Bell_source = Bell_source

        self.E_1_Pad_AmbientBass_source = E_1_Pad_AmbientBass_source
        self.E_1_Pad_AmbientBassFifths_source = E_1_Pad_AmbientBassFifths_source
        self.E_1_Pad_BellCurve_source = E_1_Pad_BellCurve_source
        self.E_1_Pad_Clouds_source = E_1_Pad_Clouds_source
        self.E_1_Pad_DiziPad_source = E_1_Pad_DiziPad_source
        self.E_1_Pad_FatAmbientBass_source = E_1_Pad_FatAmbientBass_source
        self.E_1_Pad_FlutterPad_source = E_1_Pad_FlutterPad_source
        self.E_1_Pad_HorizonPad_source = E_1_Pad_HorizonPad_source
        self.E_1_Pad_PadAirGuita_source = E_1_Pad_PadAirGuita_source
        self.E_1_Pad_PedalSteel_source = E_1_Pad_PedalSteel_source
        self.E_1_Pad_ReverseDistancePad_source = E_1_Pad_ReverseDistancePad_source
        self.E_1_Pad_SusMPLegErhu_source = E_1_Pad_SusMPLegErhu_source
        self.E_1_Pad_SusMPLegErhu2_source = E_1_Pad_SusMPLegErhu2_source
        self.E_1_Pad_TonalPercussion_source = E_1_Pad_TonalPercussion_source

    def __get_active_instrument_source_with_settings(self, setting_attr_name: str) -> List[InstrumentSourceWithSetting]:
        source_with_settings = []
        for instrument in self.instruments:
            source_with_settings += [InstrumentSourceWithSetting(instrument, setting) for setting in
                                     (getattr(instrument, setting_attr_name) or []) if setting.is_active]
        return source_with_settings

    def __get_active_note_instrument_source_with_settings(self) -> List[InstrumentSourceWithSetting]:
        return self.__get_active_instrument_source_with_settings('instrument_setting_of_note')

    def __get_active_bass_instrument_source_with_settings(self) -> List[InstrumentSourceWithSetting]:
        return self.__get_active_instrument_source_with_settings('instrument_setting_of_bass')

    def __get_active_mj_instrument_source_with_settings(self) -> List[InstrumentSourceWithSetting]:
        return self.__get_active_instrument_source_with_settings('instrument_setting_of_mj')

    def __get_active_instrument_source_with_settings_by_type(self, instrument_type: str) -> List[
        InstrumentSourceWithSetting]:
        if instrument_type == 'note':
            return self.__get_active_note_instrument_source_with_settings()
        elif instrument_type == 'bass':
            return self.__get_active_bass_instrument_source_with_settings()
        elif instrument_type == 'mj':
            return self.__get_active_mj_instrument_source_with_settings()
        return []

    def get_instrument_source_with_setting_by_type_and_num(self, instrument_type: str, index: int) -> Optional[
        InstrumentSourceWithSetting]:
        filtered_instruments = self.__get_active_instrument_source_with_settings_by_type(instrument_type)
        if 0 <= index < len(filtered_instruments):
            return filtered_instruments[index]
        return None

    def get_instrument_source_by_name(self, name: str) -> Optional[InstrumentSource]:
        filtered_instruments = list(
            filter(
                lambda instrument: instrument.name == name,
                self.instruments
            )
        )
        return filtered_instruments[0] if len(filtered_instruments) > 0 else None

    def get_instrument_source_with_settings_by_type(self, instrument_type: str) -> List[Dict]:
        filtered_instruments = self.__get_active_instrument_source_with_settings_by_type(instrument_type)
        result = []
        for (i, instrument) in enumerate(filtered_instruments):
            if instrument.is_active:
                result.append(
                    {
                        'index': i,
                        'instrument_source_with_setting': instrument
                    }
                )
        return result
