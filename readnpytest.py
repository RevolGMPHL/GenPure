import numpy as np

# data = np.load('./GenerData/data/NLPdata/input_bass_1000.npy', allow_pickle=True)
data = np.load('./GenerData/data/NLPdata/input_bass_test.npy', allow_pickle=True)
print(data)
print(len(data))
print(len(data[0]))