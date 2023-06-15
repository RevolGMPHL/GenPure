import tqdm
from torch.utils.data import Dataset as tDataset
from torch.utils.data import DataLoader
import numpy as np
import torch
from data_gendata import revise_bass_out_tonality, revise2yin

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')





def save_short_data_revise():# no random, not for dis, is for gen Model

    for i in tqdm.tqdm(range(1, 97)):
        input_bass_data = []
        input_ans_data = []
        output_ans_data = []
        input_bass = np.load('GenerData/data/NLPdata_revise/input_bass_'+ str(i*1000)+ '.npy', allow_pickle=True)
        input_ans = np.load('GenerData/data/NLPdata_revise/input_ans_'+ str(i*1000)+ '.npy', allow_pickle=True)
        output_ans = np.load('GenerData/data/NLPdata_revise/output_ans_'+ str(i*1000)+ '.npy', allow_pickle=True)
        # print('len: ', len(input_bass[1]))
        for j in range(1000):
            # if len(input_bass[j]) == 256:
            for k in range(len(input_bass[j])//8-1):
                # bass = input_bass[j]
                input_bass_data.append(input_bass[j][8*k:8*(k+1)])
                input_ans_data.append(input_ans[j][8*k:8*(k+1)])
                output_ans_data.append(output_ans[j][8*k:8*(k+1)])

        print('input_bass_data: ', np.array(input_bass_data)[0])
        # print('input_bass_data: ', np.array(input_bass_data).shape)
        print('input_ans_data: ', np.array(input_ans_data)[0])
        # print('input_ans_data: ', np.array(input_ans_data).shape)
        print('output_ans_data: ', np.array(output_ans_data)[0])
        # print('output_ans_data: ', np.array(output_ans_data).shape)

        np.save('GenerData/data/NLPdata_revise/revise/input_bass256_'+str(i), np.array(input_bass_data))
        np.save('GenerData/data/NLPdata_revise/revise/input_ans256_'+str(i), np.array(input_ans_data))
        np.save('GenerData/data/NLPdata_revise/revise/output_ans256_'+str(i), np.array(output_ans_data))
    print('save done!')

def save_short_data_revise_single():# no random, not for dis, is for gen Model

    for i in tqdm.tqdm(range(1, 70)):
        input_bass_data = []
        # input_ans_data = []
        output_ans_data = []
        input_bass = np.load('./GenerData/data/NLPdata/input_bass_'+ str(i*10000)+ '.npy', allow_pickle=True)
        input_ans = np.load('./GenerData/data/NLPdata/input_ans_'+ str(i*10000)+ '.npy', allow_pickle=True)
        output_ans = np.load('./GenerData/data/NLPdata/output_ans_'+ str(i*10000)+ '.npy', allow_pickle=True)
        # print('input_bass: ', input_bass)
        # print('input_ans: ', input_ans)
        # print('output_ans: ', output_ans)
        for j in range(10000):
            # if len(input_bass[j]) == 256:
            for k in range(len(input_bass[j])//2-1):
                # bass = input_bass[j]
                input_bass_data.append([ input_bass[j][1*k:1*(k+1)][0], input_ans[j][1*k:1*(k+1)][0] ])
                output_ans_data.append([130, output_ans[j][1*k:1*(k+1)][0], output_ans[j][1*k:1*(k+1)][0], 131])

        print('input_bass_data: ', np.array(input_bass_data)[0])
        print('input_bass_data: ', np.array(input_bass_data).shape)
        # print('input_ans_data: ', np.array(input_ans_data)[0])
        # print('input_ans_data: ', np.array(input_ans_data).shape)
        print('output_ans_data: ', np.array(output_ans_data)[0])
        print('output_ans_data: ', np.array(output_ans_data).shape)
        #
        np.save('./GenerData/data/NLPdata/revise/input_bass_'+str(i), np.array(input_bass_data))
        # np.save('./GenerData/data/NLPdata/revise/input_ans_'+str(i), np.array(input_ans_data))
        np.save('./GenerData/data/NLPdata/revise/output_ans_'+str(i), np.array(output_ans_data))
    print('save done!')


def save_short_data_nnan():# no random, not for dis, is for gen Model

    for i in tqdm.tqdm(range(1, 98)):
        input_bass_data = []
        input_ans_data = []
        output_ans_data = []
        input_bass = np.load('E:/CodeProject/1.1.Gen/GenMusic_Network/GenerMusic_Network/data/NLPdata_nnan/input_bass_'+ str(i*10000)+ '.npy', allow_pickle=True)
        input_ans = np.load('E:/CodeProject/1.1.Gen/GenMusic_Network/GenerMusic_Network/data/NLPdata_nnan/input_ans_'+ str(i*10000)+ '.npy', allow_pickle=True)
        output_ans = np.load('E:/CodeProject/1.1.Gen/GenMusic_Network/GenerMusic_Network/data/NLPdata_nnan/output_ans_'+ str(i*10000)+ '.npy', allow_pickle=True)
        print('len(input_bass): ', len(input_bass))
        print('len(input_bass[1]): ', len(input_bass[1]))
        for j in range(10000):
            # if len(input_bass[j]) == 256:
            for k in range(len(input_bass[j])//8-1):
                # bass = input_bass[j]
                input_bass_data.append(input_bass[j][8*k:8*(k+1)])
                input_ans_data.append(input_ans[j][8*k:8*(k+1)])
                output_ans_data.append(output_ans[j][8*k:8*(k+1)])

        print('input_bass_data: ', np.array(input_bass_data)[0])
        # print('input_bass_data: ', np.array(input_bass_data).shape)
        print('input_ans_data: ', np.array(input_ans_data)[0])
        # print('input_ans_data: ', np.array(input_ans_data).shape)
        print('output_ans_data: ', np.array(output_ans_data)[0])
        # print('output_ans_data: ', np.array(output_ans_data).shape)

        np.save('E:/CodeProject/1.1.Gen/GenMusic_Network/GenerMusic_Network/data/NLPdata/nnan/input_bass256_'+str(i), np.array(input_bass_data))
        np.save('E:/CodeProject/1.1.Gen/GenMusic_Network/GenerMusic_Network/data/NLPdata/nnan/input_ans256_'+str(i), np.array(input_ans_data))
        np.save('E:/CodeProject/1.1.Gen/GenMusic_Network/GenerMusic_Network/data/NLPdata/nnan/output_ans256_'+str(i), np.array(output_ans_data))
    print('save done!')


class BassData_genbass_unsquezz(tDataset):# for train the dis model
    def __init__(self, ):
        np.random.seed(2021)

        self.bass_12341234_list = np.load('/home/rg/project/re/0.base/gentest/data/NLPdata_genbass/bass_12341234/bass_12341234_list_10000.npy', allow_pickle=True)
        self.bass_part_list = np.load('/home/rg/project/re/0.base/gentest/data/NLPdata_genbass/bass_part/music_bass_part_list_10000.npy', allow_pickle=True)


        for i in range(1,60):
            print('BassData_genbass_unsquezz datainit: ', i)
            bass_12341234 = np.load(
                '/home/rg/project/re/0.base/gentest/data/NLPdata_genbass/bass_12341234/bass_12341234_list_'+str(i)+'0000.npy',
                allow_pickle=True)
            bass_part = np.load(
                '/home/rg/project/re/0.base/gentest/data/NLPdata_genbass/bass_part/music_bass_part_list_'+str(i)+'0000.npy',
                allow_pickle=True)
            self.bass_12341234_list = np.concatenate((self.bass_12341234_list, bass_12341234), axis=0)
            self.bass_part_list = np.concatenate((self.bass_part_list, bass_part), axis=0)
        print('self.bass_12341234_list: ', self.bass_12341234_list.shape)
    def __len__(self):
        return len(self.bass_12341234_list)
    def __getitem__(self, index):
        return  np.array(self.bass_12341234_list[index]+1), self.bass_part_list[index]+1, len(self.bass_part_list[index])

class BassData_genbass_squezz(tDataset):# for train the dis model
    def __init__(self, ):
        np.random.seed(2021)
        bass_11223344 = np.load('/home/rg/project/re/0.base/gentest/data/NLPdata_genbass/bass_11223344/bass_11223344_list.npy', allow_pickle=True)
        bass_rythm = np.load('/home/rg/project/re/0.base/gentest/data/NLPdata_genbass/bass_rythm/bass_rythm_list.npy', allow_pickle=True)
        bass_yin = np.load('/home/rg/project/re/0.base/gentest/data/NLPdata_genbass/bass_yin/bass_yin_list.npy', allow_pickle=True)


        self.bass_11223344 = bass_11223344
        self.bass_rythm = bass_rythm
        self.bass_yin = bass_yin


    def __len__(self):
        return len(self.bass_11223344)

    def __getitem__(self, index):
        return  np.array(self.bass_11223344[index]+1), self.bass_rythm[index]+1, self.bass_yin[index]+1, len(self.bass_yin[index])


class BassData_4_dis(tDataset):
    def __init__(self, ):
        np.random.seed(2021)
        self.x = np.load('./data/short/musicbass_short_musicbass4train.npy', allow_pickle=True)
        self.y = np.load('./data/short/musicbass_short_yesno4train.npy', allow_pickle=True)

        ones = np.ones((self.x.shape[0], 1)) * 101
        self.x = np.insert(self.x, 0, ones.T, axis=1)[:, :-1]
        # print('self.x: ', self.x)

    def __len__(self):
        return len(self.x)

    def __getitem__(self, index):
        return  self.x[index], self.y[index], len(self.y[index])


class BassData_4_rythm(tDataset):
    def __init__(self, ):
        np.random.seed(2021)
        self.musicbass = np.load('/home/rg/project/re/0.base/gentest/data/short_pure/musicbass_short_musicbass4train_pure.npy', allow_pickle=True)
        self.rythm = np.load('/home/rg/project/re/0.base/gentest/data/short_pure/musicbass_short_rythmlist4train_pure.npy', allow_pickle=True)

    def __len__(self):
        return len(self.musicbass)

    def __getitem__(self, index):
        return  self.musicbass[index]+1, self.rythm[index]+1, len(self.rythm[index])

class BassData_5_nnan(tDataset):
    def __init__(self, ):
        np.random.seed(2021)
        self.input_bass = np.load('/home/rg/project/re/0.base/gentest/data/NLPdata/nnan/input_bass256_1.npy', allow_pickle=True)
        print(self.input_bass)
        self.input_ans = np.load('/home/rg/project/re/0.base/gentest/data/NLPdata/nnan/input_ans256_1.npy', allow_pickle=True)
        self.output_ans = np.load('/home/rg/project/re/0.base/gentest/data/NLPdata/nnan/output_ans256_1.npy', allow_pickle=True)
        for i in range(40,80):
            print('datainit: ', i)
            self.input_bass = np.concatenate((self.input_bass, np.load('/home/rg/project/re/0.base/gentest/data/NLPdata/nnan/input_bass256_'+str(i)+'.npy', allow_pickle=True)), axis=0)
            self.input_ans = np.concatenate((self.input_ans, np.load('/home/rg/project/re/0.base/gentest/data/NLPdata/nnan/input_ans256_'+str(i)+'.npy', allow_pickle=True)), axis=0)
            self.output_ans = np.concatenate((self.output_ans, np.load('/home/rg/project/re/0.base/gentest/data/NLPdata/nnan/output_ans256_'+str(i)+'.npy', allow_pickle=True)), axis=0)

    def __len__(self):
        return len(self.input_bass)

    def __getitem__(self, index):
        return  self.input_bass[index], self.input_ans[index], self.output_ans[index], len(self.output_ans[index])

class BassData_6_revise(tDataset):
    def __init__(self, ):
        np.random.seed(2021)
        self.input_bass = np.load('GenerData/data/NLPdata_revise/revise/input_bass256_1.npy', allow_pickle=True)
        self.input_ans = np.load('GenerData/data/NLPdata_revise/revise/input_ans256_1.npy', allow_pickle=True)
        self.output_ans = np.load('GenerData/data/NLPdata_revise/revise/output_ans256_1.npy', allow_pickle=True)
        for i in range(1,97):
            print('datainit: ', i)
            self.input_bass = np.concatenate((self.input_bass, np.load('GenerData/data/NLPdata_revise/revise/input_bass256_'+str(i)+'.npy', allow_pickle=True)), axis=0)
            self.input_ans = np.concatenate((self.input_ans, np.load('GenerData/data/NLPdata_revise/revise/input_ans256_'+str(i)+'.npy', allow_pickle=True)), axis=0)
            self.output_ans = np.concatenate((self.output_ans, np.load('GenerData/data/NLPdata_revise/revise/output_ans256_'+str(i)+'.npy', allow_pickle=True)), axis=0)


    def __len__(self):
        return len(self.input_bass)

    def __getitem__(self, index):
        return  self.input_bass[index], self.input_ans[index], self.output_ans[index], len(self.output_ans[index])

class BassData_7_revise_single(tDataset):
    def __init__(self, ):
        np.random.seed(2021)
        self.input_bass = []
        self.output_melo = []
        for i in range(1000000):
            bass = np.random.randint(0, 72)
            bass = revise_bass_out_tonality(bass)
            self.input_bass.append(bass)

            melo = np.random.randint(48, 72)
            melo = revise2yin(melo, bass)
            self.output_melo.append(melo)

    def __len__(self):
        return len(self.input_bass)

    def __getitem__(self, index):
        return  self.input_bass[index], self.output_ans[index], len(self.output_ans[index])


if __name__ == "__main__":
    # dataset = BassData_5_nnan()
    # loader = DataLoader(dataset, batch_size=2, shuffle=True)
    # for batch_idx, batch in enumerate(loader):
    #     bass, output_ans, datalen = batch
    #     print('\nbass: ', bass.long())
    #     print('output_ans: ', output_ans.long())

    dataset = BassData_6_revise()
    loader = DataLoader(dataset, batch_size=2, shuffle=True)
    for batch_idx, batch in enumerate(loader):
        xbass, xinput, yout, datalen = batch
        print('\nxbass: ', xbass.long())
        print('xinput: ', xinput.long())
        print('yout: ', yout.long())

    # save_short_data()
    # save_short_data_pure()
    # save_short_data_nnan()
    # save_short_data_revise()
    # save_short_data_revise_single()

