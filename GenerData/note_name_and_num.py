# 这个是全部12个音的
# 我们要C0是0，C1是12，C2是24，C3是36
def note_name_2_num(name):
    note_num = 0

    if len(str(name)) == 2:
        if str(name)[0] == 'C':
            note_num = int(str(name)[1]) * 12
        elif str(name)[0] == 'D':
            note_num = int(str(name)[1]) * 12 + 2
        elif str(name)[0] == 'E':
            note_num = int(str(name)[1]) * 12 + 4
        elif str(name)[0] == 'F':
            note_num = int(str(name)[1]) * 12 + 5
        elif str(name)[0] == 'G':
            note_num = int(str(name)[1]) * 12 + 7
        elif str(name)[0] == 'A':
            note_num = int(str(name)[1]) * 12 + 9
        elif str(name)[0] == 'B':
            note_num = int(str(name)[1]) * 12 + 11

    elif len(str(name)) == 3:
        if str(name)[0] == 'C':
            note_num = int(str(name)[2]) * 12 + 1
        elif str(name)[0] == 'E':
            if (str(name)[1] == '-'):
                note_num = int(str(name)[2]) * 12 + 3
        elif str(name)[0] == 'F':
            note_num = int(str(name)[2]) * 12 + 6
        elif str(name)[0] == 'G':
            note_num = int(str(name)[2]) * 12 + 8
        if str(name)[0] == 'B':
            if str(name)[1] == '-':
                note_num = int(str(name)[2]) * 12 + 10
    if note_num == 0:
        print('note_num is 0: ', name)
    # print('Note2All_Num: ', note)

    return note_num


def note_num_2_name(num):
    note_name = ''
    # print('Num: ', Num)
    if num % 12 == 0:
        note_name = 'C' + str(int(num / 12))
    elif num % 12 == 1:
        note_name = 'C#' + str(int(num / 12))
    elif num % 12 == 2:
        note_name = 'D' + str(int(num / 12))
    elif num % 12 == 3:
        note_name = 'E-' + str(int(num / 12))
    elif num % 12 == 4:
        note_name = 'E' + str(int(num / 12))
    elif num % 12 == 5:
        note_name = 'F' + str(int(num / 12))
    elif num % 12 == 6:
        note_name = 'F#' + str(int(num / 12))
    elif num % 12 == 7:
        note_name = 'G' + str(int(num / 12))
    elif num % 12 == 8:
        note_name = 'G#' + str(int(num / 12))
    elif num % 12 == 9:
        note_name = 'A' + str(int(num / 12))
    elif num % 12 == 10:
        note_name = 'B-' + str(int(num / 12))
    elif num % 12 == 11:
        note_name = 'B' + str(int(num / 12))
    # print('new_note: ', int(100.68))

    return note_name
