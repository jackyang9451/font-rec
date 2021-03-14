"""
对各种hash算法表现进行探究
1 计算待测字体hash值
2 计算各字体集与待测字体的相似距离
3 数据可视化
"""
import os
from PIL import Image
import imagehash
import numpy as np
import matplotlib.pyplot as plt


# 计算待测字体的f0
def getF0Hash(img, func):
    return func(Image.open(img))


"""
计算字体集相似距离S
1 拿到字体集的dir
2 S = sigma(f_i - f0) / n
"""


def getS(dir, f0, func):
    f_list = []
    for img_i in os.listdir(os.path.join(rootDir, dir)):
        f_list.append(func(Image.open(os.path.join(rootDir, dir, img_i))) - f0)
    return np.mean(f_list)


"""
绘图函数
需要以下几个信息
坐标x、y
坐标xy代表的文字
hash函数名称
"""


def showPic(x, y, fontName):
    # 兼容汉字
    plt.rcParams['font.family'] = ['sans-serif']
    plt.rcParams['font.sans-serif'] = ['SimHei']

    _x = np.array(x)
    _y = [y] * len(_x)
    fontName = np.array(fontName)
    s = 100
    for idx, text in enumerate(fontName):
        plt.text(_x[idx], _y[idx], text)
    plt.scatter(_x, _y, s=s)
    plt.xlabel('相关距离S')
    plt.ylabel('哈希算法')
    plt.title('算法相似距离图')

fuc_map = {
        'AH': {
            'name': 'AH',
            'fuc': imagehash.average_hash
        },
        'DH': {
            'name': 'DH',
            'fuc': imagehash.dhash
        },
        'PH': {
            'name': 'PH',
            'fuc': imagehash.phash
        },
    }
rootDir = 'hashImg'

if __name__ == '__main__':
    # 待测字体
    testImg = 'hashImg/冬/冬-赵构.jpg'
    func_info = fuc_map['AH']
    _func = func_info['fuc']
    func_name = func_info['name']

    f0_hash = getF0Hash(testImg, _func)
    print('f0为: %s' % f0_hash)
    s_list = []
    s_list_name = []
    for D in os.listdir(rootDir):
        s = getS(D, f0_hash, _func)
        print('待测字体: %s与字体集: %s 的相似度S为: %.2f' % (testImg, D, s))
        s_list.append(s)
        s_list_name.append(D)

    showPic(s_list, func_name, s_list_name)

    func_info = fuc_map['DH']
    _func = func_info['fuc']
    func_name = func_info['name']

    f0_hash = getF0Hash(testImg, _func)
    print('f0为: %s' % f0_hash)
    s_list = []
    s_list_name = []
    for D in os.listdir(rootDir):
        s = getS(D, f0_hash, _func)
        print('待测字体: %s与字体集: %s 的相似度S为: %.2f' % (testImg, D, s))
        s_list.append(s)
        s_list_name.append(D)

    showPic(s_list, func_name, s_list_name)

    func_info = fuc_map['PH']
    _func = func_info['fuc']
    func_name = func_info['name']

    f0_hash = getF0Hash(testImg, _func)
    print('f0为: %s' % f0_hash)
    s_list = []
    s_list_name = []
    for D in os.listdir(rootDir):
        s = getS(D, f0_hash, _func)
        print('待测字体: %s与字体集: %s 的相似度S为: %.2f' % (testImg, D, s))
        s_list.append(s)
        s_list_name.append(D)

    showPic(s_list, func_name, s_list_name)

plt.show()