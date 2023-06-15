import numpy as np

hexie_list = [
    [0, 4, 7], [], [0, 3, 7], [], [0, 3, 7], [0, 4, 7], [],
    [0, 4, 7], [], [0, 3, 7], [], [0, 3, 7], [0, 4, 7]
]
out_tonality = [1, 3, 6, 8, 10]

def revise_bass_out_tonality(bass):
    while bass%12 in out_tonality:
        bass += 1
    return bass

def revise2yin(melo, bass):
    rbass = bass%12
    while abs(melo-bass)%12 not in hexie_list[rbass] or melo%12 in out_tonality:
        melo += 1
    return melo



if __name__ == '__main__':
    bass = 38
    bass = revise_bass_out_tonality(bass)
    print(bass)

    melo = 39
    melo = revise2yin(melo, bass)
    print(melo)
