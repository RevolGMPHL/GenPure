import random

import scipy.signal
import numpy as np
import EQforPress as EQ


def add_EQforpress(sm, note, Q=0.8, gain=10):
    gainEQ = gain * random.random()
    sos = EQ.peak_filter_iir(880, gain=gainEQ, Q=Q, fs=sm.sample_rate)  # gain负值，就是陷波滤波器
    note = scipy.signal.sosfilt(sos, note)
    sos = EQ.peak_filter_iir(80, gain=-6, Q=Q, fs=sm.sample_rate)  # gain负值，就是陷波滤波器
    note = scipy.signal.sosfilt(sos, note)

    sos = EQ.peak_filter_iir(2500, gain=-np.random.randint(-20, 0), Q=0.6, fs=sm.sample_rate)  # gain负值，就是陷波滤波器
    note = scipy.signal.sosfilt(sos, note)

    return note


def add712note_2bass(sm, md, blank_wav, start, note_num, source, maximum, zhangjie, bassornoteamp, amp712):
    if note_num > maximum - 24:
        note_num -= 12
    if len(md.rythmlist[zhangjie]) <= 4:
        # print('add7')
        note7 = source.get(
            note_num + 7) * random.uniform(
            0.99,
            1) * amp712 * bassornoteamp
        note7 = add_EQforpress(sm, note7, Q=0.8, gain=10)
        blank_wav[start: (start + source.length)] += note7

        note12 = source.get(
            note_num + 12) * random.uniform(0.99, 1) * amp712 * bassornoteamp
        note12 = add_EQforpress(sm, note12, Q=0.8, gain=10)
        blank_wav[start: (start + source.length)] += note12
    elif 4 < len(md.rythmlist[zhangjie]) <= 6:
        # print('add12')
        note12 = source.get(
            note_num + 12) * random.uniform(0.99, 1) * amp712 * bassornoteamp
        note12 = add_EQforpress(sm, note12, Q=0.8, gain=10)
        blank_wav[start: (start + source.length)] += note12
    return blank_wav


def add_rythmbass(blank_wav, start, Unittime, length, note, pluslist, amplist):
    # pluslist 是哪几个后续跟上的音，amp是每个音的音量
    for i in range(len(pluslist)):
        blank_wav[(start + int(pluslist[i] * Unittime)): (start + len(note) + int(pluslist[i] * Unittime))] += note * \
                                                                                                               amplist[
                                                                                                                   i] * 0.9
    return blank_wav


def add_rythmbass_select(blank_wav, start, Unittime, length, note, note7, note12, basstype, add712=0):
    if basstype == 0:
        blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                  length, note,
                                  pluslist=[2, 3, 5, 6, 7, 8],
                                  amplist=[1.2, 1.1, 1.3, 1.2, 1.2, 1])
        if add712 == 1:
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note7,
                                      pluslist=[2, 3, 5, 6, 7, 8],
                                      amplist=[1.2, 1.1, 1.3, 1.2, 1.2, 1])
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note12,
                                      pluslist=[2, 3, 5, 6, 7, 8],
                                      amplist=[1.2, 1.1, 1.3, 1.2, 1.2, 1])

    elif basstype == 1:
        blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                  length, note,
                                  pluslist=[2, 4, 6],
                                  amplist=[1.3, 1.2, 1.2])
        if add712 == 1:
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note7,
                                      pluslist=[2, 4, 6],
                                      amplist=[1.3, 1.2, 1.2])
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note12,
                                      pluslist=[2, 4, 6],
                                      amplist=[1.3, 1.2, 1.2])

    elif basstype == 2:
        blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                  length, note,
                                  pluslist=[1, 2, 3, 4, 5, 6, 7],
                                  amplist=[0.8, 1.3, 0.8, 1.3, 0.8, 1.3, 0.8])
        if add712 == 1:
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note7,
                                      pluslist=[1, 2, 3, 4, 5, 6, 7],
                                      amplist=[0.8, 1.3, 0.8, 1.3, 0.8, 1.3, 0.8])
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note12,
                                      pluslist=[1, 2, 3, 4, 5, 6, 7],
                                      amplist=[0.8, 1.3, 0.8, 1.3, 0.8, 1.3, 0.8])

    elif basstype == 3:
        blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                  length, note,
                                  pluslist=[1, 1.3, 2, 3, 3.5, 4, 5, 5.5, 6, 7],
                                  amplist=[0.8, 0.8, 1.2, 1.3, 0.8, 1.3, 0.8, 0.8, 0.8, 0.8])
        if add712 == 1:
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note7,
                                      pluslist=[1, 1.3, 2, 3, 3.5, 4, 5, 5.5, 6, 7],
                                      amplist=[0.8, 0.8, 1.2, 1.3, 0.8, 1.3, 0.8, 0.8, 0.8, 0.8])
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note12,
                                      pluslist=[1, 1.3, 2, 3, 3.5, 4, 5, 5.5, 6, 7],
                                      amplist=[0.8, 0.8, 1.2, 1.3, 0.8, 1.3, 0.8, 0.8, 0.8, 0.8])

    elif basstype == 4:
        blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                  length, note,
                                  pluslist=[1, 2, 3, 4, 5, 6, 7],
                                  amplist=[0.6, 0.6, 1.3, 0.6, 0.6, 1.3, 0.8])
        if add712 == 1:
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note7,
                                      pluslist=[1, 2, 3, 4, 5, 6, 7],
                                      amplist=[0.6, 0.6, 1.3, 0.6, 0.6, 1.3, 0.8])
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note12,
                                      pluslist=[1, 2, 3, 4, 5, 6, 7],
                                      amplist=[0.6, 0.6, 1.3, 0.6, 0.6, 1.3, 0.8])
    elif basstype == 5:
        blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                  length, note,
                                  pluslist=[1.3, 2, 3, 4.5, 5, 6, 7],
                                  amplist=[0.6, 0.6, 1.3, 0.8, 0.8, 0.7, 0.5])
        if add712 == 1:
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note7,
                                      pluslist=[1.3, 2, 3, 4.5, 5, 6, 7],
                                      amplist=[0.6, 0.6, 1.3, 0.8, 0.8, 0.7, 0.5])
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note12,
                                      pluslist=[1.3, 2, 3, 4.5, 5, 6, 7],
                                      amplist=[0.6, 0.6, 1.3, 0.8, 0.8, 0.7, 0.5])

    elif basstype == 6:
        blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                  length, note,
                                  pluslist=[0.5, 1, 2, 3, 4, 5, 6, 7],
                                  amplist=[1.0, 1.0, 1.0, 0.6, 1.0, 0.6, 1.0, 0.6])
        if add712 == 1:
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note7,
                                      pluslist=[0.5, 1, 2, 3, 4, 5, 6, 7],
                                      amplist=[1.0, 1.0, 1.0, 0.6, 1.0, 0.6, 1.0, 0.6])
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note12,
                                      pluslist=[0.5, 1, 2, 3, 4, 5, 6, 7],
                                      amplist=[1.0, 1.0, 1.0, 0.6, 1.0, 0.6, 1.0, 0.6])
    elif basstype == 7:
        blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                  length, note,
                                  pluslist=[0.5, 1, 2, 2.5, 3, 4, 4.5, 5, 6, 7],
                                  amplist=[1.2, 1.2, 1.3, 1.2, 1.2, 1.3, 1.2, 1.2, 1.3, 0.8])
        if add712 == 1:
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note7,
                                      pluslist=[0.5, 1, 2, 2.5, 3, 4, 4.5, 5, 6, 7],
                                      amplist=[1.2, 1.2, 1.3, 1.2, 1.2, 1.3, 1.2, 1.2, 1.3, 0.8])
            blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                      length, note12,
                                      pluslist=[0.5, 1, 2, 2.5, 3, 4, 4.5, 5, 6, 7],
                                      amplist=[1.2, 1.2, 1.3, 1.2, 1.2, 1.3, 1.2, 1.2, 1.3, 0.8])
    elif basstype == 8:
        blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                  length, note,
                                  pluslist=[4, 6, ],
                                  amplist=[1.0, 1.0, ])

        blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                  length, note7,
                                  pluslist=[4, 6, ],
                                  amplist=[1.0, 1.0, ])
        blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                  length, note12,
                                  pluslist=[4, 6, ],
                                  amplist=[1.0, 1.0, ])
    elif basstype == 9:
        blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                  length, note,
                                  pluslist=[2, 3, 4, 6, 7],
                                  amplist=[1.0, 1.0, 1.3, 1.0, 1.0])

        blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                  length, note7,
                                  pluslist=[2, 3, 4, 6, 7],
                                  amplist=[1.0, 1.0, 1.3, 1.0, 1.0])
        blank_wav = add_rythmbass(blank_wav, start, Unittime,
                                  length, note12,
                                  pluslist=[2, 3, 4, 6, 7],
                                  amplist=[1.0, 1.0, 1.3, 1.0, 1.0])

    return blank_wav
