import numpy as np

# a, b = input().split()
# a = int(a)
# b = int(b)
# mingongyue = []
#
# minab = min(a, b)
# for i in range(1, minab - 1):
#     if a%i == 0 and b%i == 0:
#         mingongyue.append(i)
#
# print(a*b/mingongyue[-1])

# 立方根
# a=int(input())
# n=a**(1.0/3)
# print(n)
# # print(round(n,1))


# 倒序
# a = input()
# print(a[::-1])

# 计算输入的负数的个数和输入的非负数的平均值
# a = input().split()
# cou = 0
# sum = 0
# for i in range(len(a)):
#     if int(a[i])<0:
#         cou += 1
#     else:
#         sum += int(a[i])
#
# print(cou)
# print(round(sum/(len(a) - cou), 1))

# num = int(input())
# for i in range(num):
#     inin = input()
#     if len(inin)<=8:
#         print(inin + '0'*(8-len(inin)))
#     else:
#         for j in range(len(inin) // 8):
#             # print(j, len(inin) // 8)
#             if j != len(inin) // 8 - 1:
#                 print(inin[j * 8:(j + 1) * 8])
#
#             else:
#                 print(inin[j * 8:(j + 1) * 8])
#                 print(inin[(j + 1) * 8:] + '0' * (8 - len(inin[(j + 1) * 8:])))
#

# import sys
#
# for line in sys.stdin:
#     a = line.split()
#     num = int(a[0])
#     for i in range(num):
#         inin = a[i]
#         if len(inin)<=8:
#             print(inin + '0'*(8-len(inin)))
#         else:
#             for j in range(len(inin) // 8):
#                 # print(j, len(inin) // 8)
#                 if j != len(inin) // 8 - 1:
#                     print(inin[j * 8:(j + 1) * 8])
#
#                 else:
#                     print(inin[j * 8:(j + 1) * 8])
#                     print(inin[(j + 1) * 8:] + '0' * (8 - len(inin[(j + 1) * 8:])))

# num = int(input())
# zhuang = input().split()
# # print(zhuang)
# now = 0
# cou = 1
# coulist = 1
#
# for i in range(0, num):
#     now = zhuang[i]
#     cou = 1
#     wavlist = []
#     for j in range(i, num):
#         if now < zhuang[j] and zhuang[j] not in wavlist:
#             wavlist.append(zhuang[j])
#             cou += 1
#     print()
#     if cou > coulist:
#         coulist = cou
# print(coulist)

# try:
#     while 1:
#         n = int(input())
#         s = bin(n)
#         print(s)
#         t = 0
#         i = 0
#         max1 = 0
#         while i < len(s):
#             if s[i] == '1':
#                 t += 1
#             else:
#                 max1 = max(max1, t)
#                 t = 0
#             i += 1
#         max1 = max(max1, t)
#         print(max1)
#
#
# except:
#     pass
#


# try:
#     while(1):
#         n= int(input())
#         s = bin(n)[2:]
#         cou = 0
#         maxcou = 0
#         #print(s)
#         for i in range(len(s)):
#             if s[i] == '1':
#                 # print('test')
#                 cou += 1
#             else:
#                 maxcou = max(maxcou, cou)
#                 cou = 0
#             maxcou = max(maxcou, cou)
#         print(maxcou)
# except:
#     pass

# import sys
#
# for line in sys.stdin:
#     line = line.strip()
#     if len(line) == 0:
#         pass
#     else:
#         flag = False
#         for windows in reversed(range(1, len(line) + 1)):
#
#             for i in range(len(line) - windows + 1):
#                 tmp = line[i:i + windows + 1]
#                 if tmp == tmp[::-1]:
#                     result = line[i:i + windows + 1]
#                     flag = True
#                     break
#             if flag:
#                 break
#         print(len(result))


# 大写
# if 'A' <= s <= 'Z':
# exch1_row,exch1_col,exch2_row,exch2_col=map(int, input().split())
# print(exch1_row,exch1_col,exch2_row,exch2_col)

# def handle(waits, ins, outs, result: list):
#     print('\nwaits: ', waits)
#     print('ins: ', ins)
#     print('outs: ', outs)
#     if not waits and not ins:
#         print('vccwaits: ', waits)
#         print('aaains: ', ins, '\n\n\n')
#         result.append(outs)
#     if ins:
#         temp_outs = outs + ins[-1] + ' '
#         handle(waits, ins[:-1], temp_outs, result)
#     if waits:
#         temp_ins = ins
#         print('temp_ins: ', temp_ins)
#         temp_ins.append(waits[0])
#         handle(waits[1:], temp_ins, outs, result)
#
# n = int(input())
# waits = input().strip().split(' ')
# result = []
# ins = []
# outs = ''
# handle(waits, ins, outs, result)
#
# result = sorted(result)
# for s in result:
#     print('go')
#     print('s', s)
#
# 遍历()
#
#
# 遍历()
# {
#     走右边()
#     走左边()
# }
#
# 走右边()
# {
#     走右边()
#     走左边()
# }
#
# 走左边()
# {
#     走右边()
#     走左边()
# }


# aa = [11, 22, 33, 44, 55]
# res = filter(lambda x:x<33, aa)
# for i in res:
#     print(i)

# while True:
#     try:
#         s = input().strip().split(' ')
#         #print(s)
#         for i in range(len(s)):
#             if '；' in s[i] and '：' not in s[i]:
#                 s[i] = s[i] + ' ' + s[i+1]
#                 s[i+1] = ''
#         print(len(s))
#         for i in list(s):
#             print(i.replace('“', '').replace('”', ''))
#     except:break


# x=[1,222,222,4,5555,222,7,8,9,10]
# x.remove(2)
# print(x)
# print(x[:])
#
# dp = [[0 for i in range(3)] for j in range(5)]
# print(dp)


# str = "this";
# str2 = str.rjust(10, '0')
# print(str2)
# print(len(str2))

# x=['1', '222', '33', '4', '5555', '6', '7', '8', '9', '10']
# y = sorted(x)
# print(y)

# a = 10
# b = int(a, 2)
# print(b)
#
# # 判断素数
# def issu(x):
#     tem = 2
#     while tem**2<=x:
#         if x%tem==0:
#             return False
#         tem+=1
#     return True

# from collections import defaultdict
# s=[('yellow',1),('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d=defaultdict(list)
# for k, v in s:
#     d[k].append(v)
# # a=sorted(d.items())
# print(d.keys())
# print(d.items())
# print(d.values())
# print(d['yellow'])

# x = {1:[0], 2:'a', 3:'a', }
# print(x[1])

# print(round(5.5))
# print(round(5.4))
# print(int('10001', 2))
# a = [1,2,3]
# print(a[len(a)-1])


# # bpm 生成test

#
#
#
# bpm_x = np.linspace(0, 1, 70)
# mean = 0.45
# standard_devation = 0.3
# norm = stats.norm(mean, standard_devation)
# bpm_y = norm.pdf(bpm_x) / norm.pdf(0)
# bpm_rate = np.exp(bpm_y)/sum(np.exp(bpm_y))
# # plt.plot(decay_x, aa)
# # plt.show()
# bpm = None
# bpm_range = 55 + np.arange(0, 70)
# bpm = bpm if bpm in bpm_range else np.random.choice(bpm_range, 1, p = bpm_rate)
# print(bpm)

# 压限器
doublex = []
x = np.linspace(0, 69, 70)
# doublex = np.append(doublex, x)
# doublex = np.append(doublex, x).reshape(2, len(x)).T
# print(doublex)
# # print(x)
# xx = [xdata*0.6 if xdata>60 else xdata for xdata in x]
# # print(xx)


# xxx = np.where(x < 40, x, x*0.6)
# print(xxx)
rootchoice = np.array([18, 6])
root = np.random.choice(rootchoice, p=[0.8, 0.2])
print(root)
