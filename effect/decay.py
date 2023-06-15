# import matplotlib.pyplot as plt
import numpy as np
from scipy import stats


# 用来生成一个尾部衰减的函数，不然鼓会变得很奇怪
# 只能支持双数的length
def weaken_start_end(singe_note_length):
    x = np.linspace(-10, 10, singe_note_length // 2)  # 开始，结束，一共多少个点

    left_y = (1 + np.exp(-((x + 2) * 2))) ** -1  # 滤波器的左半边

    right_y = left_y[::-1]  # 滤波器的右半边

    w = np.concatenate([left_y, right_y])  # 一维的数据

    weaken_end_coefficient = [np.append(w[i], w[i]) for i in range(0, singe_note_length - 1)]  # 变成wav能用的二维模式

    return w, weaken_end_coefficient


def weaken_end(singe_note_length):
    x = np.linspace(-10, 10, singe_note_length)  # 开始，结束，一共多少个点

    left_y = (1 + np.exp(-((x + 4) * 2))) ** -1  # 滤波器的左半边

    right_y = left_y[::-1]  # 滤波器的右半边

    weaken_end_coefficient = [np.append(right_y[i], right_y[i]) for i in range(0, singe_note_length)]  # 变成wav能用的二维模式

    return right_y, weaken_end_coefficient


def decay1():
    data_len = 100
    data = np.random.rand(data_len)

    decay_x = np.linspace(0, 3.5, data_len)
    mean = 0
    standard_devation = 1.5
    norm = stats.norm(mean, standard_devation)
    decay_y = norm.pdf(decay_x) / norm.pdf(0)

    decay_data = data * decay_y

    plt.subplot(1, 2, 1)
    plt.plot(range(data_len), data)
    plt.subplot(1, 2, 2)
    plt.plot(range(data_len), decay_data)
    plt.show()


def decay2():
    data_len = 100
    data = np.random.rand(data_len)

    decay_x = np.linspace(0, 3.5, data_len)
    mean = -3
    standard_devation = 1.5
    norm = stats.norm(mean, standard_devation)
    decay_y = norm.pdf(decay_x) / norm.pdf(0)

    decay_data = data * decay_y

    plt.subplot(1, 2, 1)
    plt.plot(range(data_len), data)
    plt.subplot(1, 2, 2)
    plt.plot(range(data_len), decay_data)
    plt.show()


def decay(data_raw):
    data_len = 3200  # len(data_raw)

    decay_x = np.linspace(0, 3.5, data_len)
    mean = 0
    standard_devation = 1.5
    norm = stats.norm(mean, standard_devation)
    decay_y = norm.pdf(decay_x) / norm.pdf(0)
    # print('data_raw.T ', data_raw.T)
    # print('data_raw ', data_raw)
    data = data_raw.T
    data[0][-data_len:] = data[0][-data_len:] * decay_y
    data[1][-data_len:] = data[1][-data_len:] * decay_y
    data_raw = data.T
    return data_raw


def decay_melody(data_raw):
    data_len = 3200  # len(data_raw)
    decay_x = np.linspace(0, 3.5, data_len)
    mean = -4
    standard_devation = 0.7
    norm = stats.norm(mean, standard_devation)
    decay_y = norm.pdf(decay_x) / norm.pdf(0)
    # print('data_raw.T ', data_raw.T)
    # print('data_raw ', data_raw)
    data = data_raw.T
    data[0][-data_len:] = data[0][-data_len:] * decay_y
    data[1][-data_len:] = data[1][-data_len:] * decay_y
    data_raw = data.T
    return data_raw


def decay_long_melody(data_raw):
    data_len = len(data_raw) // 3
    decay_x = np.linspace(0, 3.5, data_len)
    mean = -1
    standard_devation = 1.6
    norm = stats.norm(mean, standard_devation)
    decay_y = norm.pdf(decay_x) / norm.pdf(0)
    data = data_raw.T
    data[0][-data_len:] = data[0][-data_len:] * decay_y
    data[1][-data_len:] = data[1][-data_len:] * decay_y
    data_raw = data.T
    return data_raw


def decay_hanning(data_raw):
    data = data_raw.T
    data[0] = data[0] * np.hanning(len(data[0]))
    data[1] = data[1] * np.hanning(len(data[1]))
    data_raw = data.T

    return data_raw


def decay_sing(data_raw, mean=0.0):
    data_len = 3200  # len(data_raw)

    decay_x = np.linspace(0, 3.5, data_len)

    standard_devation = 1.5
    norm = stats.norm(mean, standard_devation)
    decay_y = norm.pdf(decay_x) / norm.pdf(0)
    # print('data_raw.T ', data_raw.T)
    # print('data_raw ', data_raw)
    data = data_raw
    data[-data_len:] = data[-data_len:] * decay_y

    data_raw = data
    return data_raw


def decay_long_melody_sing(data_raw):
    data_len = len(data_raw) // 2
    decay_x = np.linspace(0, 3.5, data_len)
    sin = np.sin(decay_x * 400 * np.pi / 180) / 3 + 1

    mean = -2
    standard_devation = 1.6
    norm = stats.norm(mean, standard_devation)
    decay_y = norm.pdf(decay_x) / norm.pdf(0)
    data = data_raw
    data[-data_len:] = data[-data_len:] * decay_y * sin
    data_raw = data
    return data_raw


def decay_start_melody_sing(data_raw, mean=4, standard_devation=3.0):
    data_len = len(data_raw)
    decay_x = np.linspace(0, 4, data_len)

    norm = stats.norm(mean, standard_devation)
    decay_y = norm.pdf(decay_x) / norm.pdf(0)
    data = data_raw
    data[:data_len] = data[:data_len] * (decay_y / np.max(decay_y))
    data_raw = data
    return data_raw


if __name__ == '__main__':
    # fm = FM.FileManager( midi_name = 'test')
    #
    # singe_note_length = 81415
    #
    # y, weaken_end_coefficient = weaken_end(singe_note_length)
    #
    # EleGuita_note = fm.EleGuita_source.get(72) * weaken_end_coefficient
    #
    # x = np.linspace(0, 10, singe_note_length)
    #
    # plt.plot(x, y, ls="-", lw=2, label="plot figure")
    #
    # # 标签
    # plt.legend()
    #
    # plt.show()
    chuang = np.hanning(200)
    print(chuang)
    decay2()
