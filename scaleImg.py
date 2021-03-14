"""
比较缩放对图像相似度的影响
需要公用x轴进行比较
1 计算相似度代码已经有了
"""
from getHashPerformance import getF0Hash, getS, fuc_map, rootDir
import matplotlib.pyplot as plt
import numpy as np
import os
from PIL import Image



if __name__ == '__main__':
    testImg = 'hashImg/冬/冬-赵构.jpg'
    func_info = fuc_map['DH']
    _func = func_info['fuc']
    func_name = func_info['name']

    hash_387 = _func(Image.open(testImg))
    s_list = []
    s_list_name = []
    for D in os.listdir(rootDir):
        s = getS(D, hash_387, _func)
        # print('待测字体: %s与字体集: %s 的相似度S为: %.2f' % (testImg, D, s))
        s_list.append(s)
        s_list_name.append(D)
    ax1 = plt.subplot(311)
    plt.scatter(s_list, [func_name] * 20)
    plt.setp(ax1.get_xticklabels(), visible=False)




    hash_1 = _func(Image.open(testImg).rotate(10))
    s_list = []
    s_list_name = []
    for D in os.listdir(rootDir):
        s = getS(D, hash_1, _func)
        # print('待测字体: %s与字体集: %s 的相似度S为: %.2f' % (testImg, D, s))
        s_list.append(s)
        s_list_name.append(D)
    ax2 = plt.subplot(312, sharex=ax1)
    plt.scatter(s_list, [func_name] * 20)
    plt.setp(ax2.get_xticklabels(), visible=False)

    hash_0 = _func(Image.open(testImg).rotate(30))
    s_list = []
    s_list_name = []
    for D in os.listdir(rootDir):
        s = getS(D, hash_0, _func)
        # print('待测字体: %s与字体集: %s 的相似度S为: %.2f' % (testImg, D, s))
        s_list.append(s)
        s_list_name.append(D)
    ax2 = plt.subplot(313, sharex=ax1)
    plt.scatter(s_list, [func_name] * 20)

    plt.show()
