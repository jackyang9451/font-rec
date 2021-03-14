"""
用来测试算法快不快
1 定义一个_rootDir用来指定测试集的地址
2 开始计时
3 循环对每个图片调用算法
4 结束
"""

import os
import imagehash
import time
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

rootDir = '../蚌-肚 01'


def getTimes(f):
    y = []
    for i in range(6):
        start = time.time()
        for item in os.listdir(rootDir):
            for font in os.listdir(os.path.join(rootDir, item)):
                f(Image.open(os.path.join(rootDir, item, font)))
        end = time.time()
        y.append(end - start)
    return y



# 兼容汉字

plt.rcParams['font.family'] = ['sans-serif']

plt.rcParams['font.sans-serif'] = ['SimHei']

y1 = getTimes(imagehash.average_hash)
y2 = getTimes(imagehash.dhash)
y3 = getTimes(imagehash.phash)

x = [1, 2, 3, 4, 5, 6]

plt.plot(x, y1, '^-r', label='AH')
plt.plot(x, y2, 'o-g', label='DH')
plt.plot(x, y3, 's-b', label='PH')
plt.plot(x, [np.mean(y3)]*6, '--b')
plt.plot(x, [np.mean(y2)]*6, '--g')
plt.plot(x, [np.mean(y1)]*6, '--r')

plt.xlabel('次数')
plt.ylabel('执行时间')
plt.title("各种哈希算法执行时间比较")
plt.legend()

plt.show()
