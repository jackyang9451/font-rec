"""
计算字体Hash值 并且进行持久化
字体对象：
    字体
    字体文件名
    ahash值
    phash值
    dhash值
    whash值
具体步骤
    1 标准数据集中便利字体类型
    2 便利某个字体的所有文件
    3 构建字体对象
    4 将字体对象放入list
    5 持久化
"""
import imagehash
import os
from PIL import Image
import json

rootPah = '../标准数据集'


class Font:

    def __init__(self, fontType, fontFilePath):
        self.fontType = fontType
        self.fontFilePath = fontFilePath
        img = Image.open(fontFilePath)
        self.aHash = str(imagehash.average_hash(img))
        self.dHash = str(imagehash.dhash(img))
        self.pHash = str(imagehash.phash(img))
        self.wHash = str(imagehash.whash(img))


list = []

for fontType in [x for x in os.listdir(rootPah)]:
    fontTypeList = []
    for item in os.listdir(os.path.join(rootPah, fontType)):
        img = Image.open(os.path.join(rootPah, fontType, item))
        font = {
            'fontType': fontType,
            'fontFilePath': os.path.join(rootPah, fontType, item),
            'aHash': str(imagehash.average_hash(img)),
            'dHash': str(imagehash.dhash(img)),
            'pHash': str(imagehash.phash(img)),
            'wHash': str(imagehash.whash(img)),
        }
        fontTypeList.append(font)

    list.append(fontTypeList)

fp = open('obj.json', 'w')
json.dump(list, fp)
fp.close()
