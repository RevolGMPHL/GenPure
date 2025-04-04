drumlist_num = []
drumlist_num.append({0: 'Firefly1', 1: 'Firefly2'})
drumlist_num.append({0: 'Refrain1', 1: 'Refrain2', 2: 'Refrain3', 3: 'Refrain4', 4: 'Refrain5'})
drumlist_num.append(
    {0: 'ContinueVoyage1', 1: 'ContinueVoyage2', 2: 'ContinueVoyage3', 3: 'ContinueVoyage4', 4: 'ContinueVoyage5',
     5: 'ContinueVoyage6', 6: 'ContinueVoyage7'})
drumlist_num.append({0: 'CAN1', 1: 'CAN2', 2: 'CAN3', 3: 'CAN4'})
drumlist_num.append({0: 'Bing1', 1: 'Bing2'})
drumlist_num.append({0: 'Nian1', 1: 'Nian2'})
drumlist_num.append({0: 'Ting1', 1: 'Ting2', 2: 'Ting3', })
drumlist_num.append({0: 'Wuxin1', 1: 'Wuxin2', 2: 'Wuxin3', 3: 'Wuxin4', 4: 'Wuxin5', 5: 'Wuxin6', 6: 'Wuxin7'})
drumlist_num.append(
    {0: 'WuHou1', 1: 'WuHou2', 2: 'WuHou3', 3: 'WuHou4', 4: 'WuHou5', 5: 'WuHou6', 6: 'WuHou7', 7: 'WuHou8'})
drumlist_num.append({0: 'Xueyue1', 1: 'Xueyue2', 2: 'Xueyue3', 3: 'Xueyue4', 4: 'Xueyue5'})
# b2 = 0, c+3 = 1, c3 = 2, c4-2 = 3, c4-3 = 4, c4-3 = 10, d3 = 5, d4 = 6, e3-1 = 7, e3-3 = 8, e4 d+4 = 9, f+3 = 11


drumlist = {
    # 0
    'Firefly1': [[0], [100], [100], [100], [100], [3], [3], [3],
                 [2], [100], [100], [100], [100], [100], [0], [100],
                 [0], [100], [100], [100], [100], [3], [3], [3],
                 [2], [100], [100], [100], [100], [100], [100], [100], ],

    'Firefly2': [[0], [100], [100], [3],
                 [2], [100], [100], [0],
                 [0], [100], [100], [3],
                 [2], [100], [100], [100], ],

    # 1
    'Refrain1': [[2, 11], [100], [11], [100], [7, 11], [100], [11], [100],
                 [1, 11], [100], [1, 11], [100], [7, 11], [100], [11], [100],
                 [1, 11], [100], [11], [100], [7, 11], [100], [11], [100],
                 [11], [100], [1, 11], [100], [5, 11], [100], [11], [100], ],

    'Refrain2': [[2, 11, 3], [100], [11], [100], [5, 11], [100], [11], [100],
                 [2, 11], [100], [2, 11], [100], [5, 11], [100], [11], [100],
                 [2, 11], [100], [11], [100], [5, 11], [100], [11], [100],
                 [11], [100], [2, 11], [100], [5, 11], [100], [11], [100], ],

    'Refrain3': [[2, 11, 9], [100], [11, 9], [0], [8, 11, 9], [100], [11, 9], [100],
                 [1, 11, 9], [100], [1, 11, 9], [100], [8, 11, 9], [100], [11, 9], [100],
                 [1, 11, 9], [100], [11, 9], [0], [8, 11, 9], [100], [11, 9], [100],
                 [11], [100], [1, 11], [100], [5, 11], [100], [11], [100], ],

    'Refrain4': [[2, 11], [100], [11], [0], [8, 11], [100], [11], [100],
                 [2, 11], [100], [2, 11], [100], [8, 11], [100], [11], [100],
                 [1, 11], [100], [11], [0], [11, 9], [100], [11], [100],
                 [10, 11], [100], [2, 11], [2], [1, 5, 11], [1, 5, ], [2, 11], [100], ],

    'Refrain5': [[2, 11], [100], [11], [0], [8, 11], [100], [11], [100],
                 [1, 11], [100], [1, 11], [100], [8, 11], [100], [11], [100],
                 [1, 11, 6], [100], [11], [0], [8, 11], [0], [0, 11], [100],
                 [0, 11], [100], [0, 11], [100], [5, 11, 6], [100], [0, 11], [100], ],

    # 2
    # c5=0, c + 4=1, g + 3=2,  d+5=3
    'ContinueVoyage1': [[0], [100], [1], [100], [100], [100], [1], [100],
                        [1], [100], [1], [100], [100], [100], [0], [0],
                        [0], [100], [1], [0], [100], [100], [1], [100],
                        [1], [100], [1], [100], [100], [0], [0], [0], ],

    'ContinueVoyage2': [[0], [100], [1], [100], [100], [100], [1], [100],
                        [1], [100], [1], [100], [100], [100], [0], [0],
                        [0], [100], [1], [0], [100], [100], [1], [100],
                        [1], [100], [1], [100], [1], [100], [0], [0], ],

    'ContinueVoyage3': [[0], [100], [2], [100], [3], [100], [2], [100],
                        [2], [100], [2], [100], [3], [100], [0], [0],
                        [0], [100], [2], [100], [3], [100], [2], [100],
                        [2], [100], [2], [100], [3], [0], [0], [0], ],

    'ContinueVoyage4': [[0], [100], [2], [100], [3], [100], [0], [0],
                        [2], [100], [2], [100], [3], [100], [0], [0],
                        [0], [100], [2], [0], [3], [100], [2], [100],
                        [2], [100], [2], [100], [3], [100], [3], [3], ],

    'ContinueVoyage5': [[0], [100], [2], [100], [4], [100], [0], [0],
                        [0], [100], [2], [100], [4], [100], [0], [0],
                        [0], [100], [2], [100], [4], [100], [2], [100],
                        [2], [100], [2], [100], [4], [0], [0], [0], ],

    'ContinueVoyage6': [[0], [100], [2], [100], [4], [100], [0], [0],
                        [2], [100], [2], [100], [4], [100], [0], [0],
                        [0], [100], [2], [0], [4], [100], [2], [100],
                        [2], [100], [2], [100], [4], [2], [4], [4], ],

    'ContinueVoyage7': [[0], [100], [1], [100], [4], [100], [1], [100],
                        [1], [100], [1], [100], [4], [100], [0], [0],
                        [0], [100], [1], [0], [4], [100], [1], [100],
                        [1], [100], [2], [100], [4, 1], [0], [0], [0], ],
    # 3
    # GB=0, G = 1, GF=2,  B=3
    'CAN1': [[0], [1], [1], [0], [2], [0], [1], [0],
             [0], [100], [1], [100], [2], [100], [1], [100],
             [0], [100], [1], [100], [2], [100], [1], [100],
             [0], [100], [100], [100], [2], [100], [100], [100], ],

    'CAN2': [[0], [100], [100], [100], [2], [100], [100], [100],
             [0], [100], [100], [3], [2], [3], [100], [3],
             [0], [100], [100], [100], [2], [100], [100], [100],
             [0], [100], [1], [100], [2], [100], [1], [100], ],

    'CAN3': [[0], [1], [1], [1], [2], [1], [1], [1],
             [0], [100], [1], [100], [2], [100], [1], [100],
             [0], [100], [1], [100], [2], [100], [1], [100],
             [0], [100], [1], [100], [2], [100], [1], [100], ],

    'CAN4': [[0], [100], [1], [3], [2], [3], [1], [3],
             [0], [100], [1], [100], [2], [100], [1], [100],
             [0], [100], [1], [100], [2], [100], [1], [100],
             [0], [100], [1], [100], [2], [100], [1], [100], ],
    # 4
    'Bing1': [[0], [100], [100], [100], [4], [100], [100], [0],
              [0], [0], [0], [100], [4], [100], [100], [100],
              [0], [100], [100], [100], [4], [100], [100], [0],
              [0], [0], [0], [100], [4], [100], [100], [100], ],

    'Bing2': [[2], [100], [100], [100], [4], [3], [3, 3], [3],
              [0], [0], [0], [100], [4], [100], [100], [100],
              [0], [100], [100], [100], [4], [100], [100], [0],
              [0], [0], [0], [100], [4], [100], [100], [100], ],
    # 5
    'Nian1': [[0], [100], [1], [100], [2], [100], [100], [100],
              [0], [100], [1], [100], [2], [100], [2], [2],
              [0], [100], [1], [100], [2], [100], [100], [100],
              [0], [100], [1], [100], [2], [100], [2], [2], ],

    'Nian2': [[0], [100], [1], [100], [2], [100], [100], [100],
              [0], [100], [1], [100], [2], [100], [2], [2],
              [0], [100], [1], [100], [2], [100], [0], [2],
              [0], [100], [1], [100], [2], [2], [2], [2], ],
    # 6
    'Ting1': [[3, 0], [100], [100], [100], [1], [100], [100], [100],
              [2], [100], [3], [100], [2], [100], [3], [100],
              [3, 0], [100], [100], [100], [1], [100], [100], [100],
              [2], [100], [3], [100], [1], [100], [100], [100], ],

    'Ting2': [[3, 0], [100], [100], [100], [1], [100], [100], [100],
              [2], [100], [3], [100], [2], [100], [3], [100],
              [3, 0], [100], [100], [100], [1], [100], [100], [100],
              [2], [100], [3], [100], [1], [100], [3], [100], ],

    'Ting3': [[3, 0], [100], [100], [100], [1], [100], [100], [100],
              [2], [100], [3], [100], [2], [100], [3], [100],
              [3, 0], [100], [100], [100], [1], [100], [100], [100],
              [2], [100], [3], [100], [1], [3], [2], [3], ],
    # 7
    'Wuxin1': [[0, 1], [100], [100], [100], [3], [100], [1], [2],
               [1], [100], [1], [100], [3], [100], [1], [100],
               [2], [100], [2], [100], [3], [100], [1], [2],
               [1], [3], [1], [100], [3], [100], [1], [3], ],
    'Wuxin2': [[2], [100], [100], [100], [3], [100], [1], [2],
               [1], [100], [1], [100], [3], [100], [1], [100],
               [2], [100], [2], [100], [3], [100], [1], [2],
               [1], [3], [1], [100], [3], [100], [1], [3], ],
    'Wuxin3': [[0, 2], [100], [4], [100], [4, 3], [100], [4, 1], [2],
               [4, 1], [100], [4, 1], [100], [4, 3], [100], [4, 1], [100],
               [4, 2], [100], [4, 2], [100], [4, 3], [100], [4, 1], [2],
               [4, 1], [3], [4, 1], [100], [4, 3], [100], [4, 1], [3], ],
    'Wuxin4': [[0, 2], [100], [2], [3], [100], [1], [1], [2],
               [1], [100], [1], [100], [3], [100], [1], [1],
               [4, 1], [100], [1], [3], [0], [100], [1], [2],
               [1], [3], [4, 1], [100], [3], [100], [1], [3], ],
    'Wuxin5': [[2], [100], [1], [3], [100], [1], [1], [100],
               [1], [1], [1], [100], [3], [100], [1], [100],
               [2], [100], [2], [100], [3], [100], [1], [2],
               [1], [3], [1], [100], [3], [100], [1], [3], ],
    'Wuxin6': [[0, 2], [100], [4], [100], [3], [100], [4], [1],
               [4, 3], [1], [4, 1], [100], [4, 3], [100], [4, 1], [100],
               [4, 2], [100], [4, 2], [2], [4, 3], [100], [4, 1], [1],
               [4], [3], [4, 1], [100], [4, 3], [100], [4, 1], [3], ],
    'Wuxin7': [[0, 2], [100], [4], [100], [3], [100], [4], [1],
               [4, 1], [100], [4, 1], [100], [4, 3], [100], [4, 1], [100],
               [4, 2], [100], [4, 2], [100], [4, 3], [100], [4, 1], [2],
               [4, 1], [3], [4, 1], [100], [4, 3], [100], [4, 1], [3], ],
    # 8
    'WuHou1': [[0, 2], [100], [100], [0, 2], [1, 2], [0], [2], [100],
               [100], [0], [2], [100], [100], [0], [2], [100],
               [0], [100], [0], [100], [2], [100], [0], [0],
               [0], [100], [0, 2], [2], [0, 2], [100], [0, 2], [100], ],

    'WuHou2': [[0], [100], [0], [100], [1], [100], [0], [100],
               [0], [100], [2], [0, 2], [100], [100], [0], [100],
               [0], [100], [100], [1], [100], [100], [1, 2], [2],
               [100], [100], [2], [1, 2], [3], [3], [0, 3], [100], ],

    'WuHou3': [[0], [100], [0], [100], [1], [100], [0], [100],
               [0], [100], [2], [0, 2], [100], [100], [0], [100],
               [0], [100], [100], [1], [100], [100], [1, 2], [2],
               [100], [100], [2], [1, 2], [3], [3], [0, 3], [100], ],

    'WuHou4': [[4, 0, 2], [100], [4], [0, 2], [6, 1, 2], [0], [5, 2], [5],
               [100], [0], [2, 4], [4], [6], [0], [2, 4], [100],
               [0, 4], [100], [0, 4], [100], [2, 6], [100], [0, 4], [0, 4],
               [0], [100], [0, 2, 5], [2, 5], [0, 2, 9], [100], [0, 2, 4], [100], ],

    'WuHou5': [[0, 4], [100], [0, 4], [100], [1, 6], [100], [0, 4], [4],
               [0], [100], [2, 5], [0, 2, 5], [9], [100], [0, 4], [100],
               [0, 4], [100], [4], [1], [6], [100], [1, 2, 4], [2, 4],
               [7], [100], [2, 5], [1, 2, 5], [3, 9], [3], [0, 3, 4], [100], ],

    'WuHou6': [[0, 4], [100], [0, 4], [100], [1, 6], [100], [0, 5], [5],
               [0], [100], [2, 4], [0, 2, 4], [6], [100], [0, 4], [100],
               [0, 4], [100], [4], [1], [6], [100], [1, 2, 4], [2, 4],
               [7], [100], [2, 5], [1, 2, 5], [3, 9], [3], [0, 3, 4], [100], ],

    'WuHou7': [[0, 4], [100], [0, 4], [100], [1, 6], [100], [0, 5], [5],
               [0], [100], [2, 4], [0, 2, 4], [6], [100], [0, 4], [100],
               [0, 4], [100], [4], [1], [6], [100], [1, 2, 4], [2, 4],
               [100], [100], [2, 5], [1, 2, 5], [3, 9], [3], [0, 3, 4], [100], ],

    'WuHou8': [[0, 4, 8], [100], [0, 4], [100], [1, 6], [100], [0, 4], [4],
               [0], [100], [2, 5], [0, 2, 5], [9], [100], [0, 4], [100],
               [0, 4], [100], [4], [1], [6], [100], [1, 2, 4, 8], [2, 4, 8],
               [7], [100], [2, 5], [1, 2, 5], [3, 9, 7], [3], [0, 3, 4], [100], ],

    'WuHou9': [[5], [100], [5], [100], [6], [100], [5], [100],
               [100], [100], [5], [5], [6], [100], [100], [100],
               [5], [100], [5], [100], [6], [100], [5], [100],
               [100], [100], [5], [5], [6], [100], [100], [100], ],
    'WuHou10': [[5], [100], [5], [100], [6], [100], [5], [100],
                [100], [100], [5], [5], [6], [100], [5], [100],
                [5], [100], [5], [100], [5], [100], [5], [100],
                [100], [100], [100], [100], [5], [5], [5], [5], ],

    'Xueyue1': [[0, 1], [100], [100], [100], [100], [100], [100], [100],
                [2], [100], [100], [100], [100], [100], [1], [100],
                [1], [100], [100], [100], [1], [100], [100], [100],
                [2], [100], [100], [100], [100], [100], [100], [100], ],
    'Xueyue2': [[0, 1], [100], [100], [100], [100], [100], [100], [100],
                [2], [100], [100], [100], [100], [100], [1], [100],
                [1], [100], [100], [100], [1], [100], [100], [100],
                [2], [100], [100], [100], [100], [100], [100], [100], ],
    'Xueyue3': [[0, 1], [100], [100], [100], [100], [100], [100], [100],
                [2], [100], [100], [100], [100], [100], [1], [100],
                [1], [100], [100], [100], [1], [100], [100], [100],
                [2], [100], [100], [100], [100], [100], [100], [100], ],
    'Xueyue4': [[0, 1], [100], [100], [100], [100], [100], [100], [100],
                [2], [100], [100], [100], [100], [100], [1], [100],
                [1], [100], [100], [100], [1], [100], [100], [100],
                [2], [100], [1], [100], [1], [100], [1], [100], ],

    'Xueyue5': [[0, 1], [100], [100], [100], [100], [100], [100], [100],
                [2], [100], [1], [100], [1], [100], [1], [100],
                [1], [100], [100], [100], [1], [100], [100], [100],
                [2], [100], [1], [100], [1], [1], [1], [1], ],
}


# print(len(drumlist_num[1]))
# print(drumlist[drumlist_num[0][0]])


def get_next_note_distance(midi, xiaojie, yin):
    rawyin = yin
    while (yin < 7):
        yin += 1
        if midi[xiaojie][yin] < 100:
            return yin - rawyin
    xiaojie += 1
    while (yin < 15):
        yin += 1
        if midi[xiaojie][yin - 8] < 100:
            return yin - rawyin
# import notetest
# yindistance = get_next_note_distance(notetest.answer11, xiaojie=0, yin=7)
# print(yindistance)
