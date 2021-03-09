"""
收集的图像进行二值化处理，全部统一为白底黑字
步骤：
    1 获取目录下所有目录
    2 获取目录下文件
    3 对文件进行灰度化后进行二值化
        根据灰度化后左上角第一像素进行阈值设定（？）
    4 灰度化后进行保存，重命名文件
"""
import os
from PIL import Image


# 图像的二值化，用于统一图片的格式
def Binarization(Img):
    # 区分背景黑白的阈值 获取图像左上角像素值
    background = Img.getpixel((0, 0))

    pix = []

    for i in range(256):
        # 背景为亮色 背景变为白色 字体变为黑色
        if background > 100:
            if i < background:
                pix.append(0)
            else:
                pix.append(1)
        # 背景为黑色 背景变为白色 字体变为黑色
        else:
            if i > background:
                pix.append(0)
            else:
                pix.append(1)

    return Img.point(pix, '1')


# 1
fonts = [x for x in os.listdir('../../草书')]

for x in fonts:
    curDir = os.path.join('../../草书', x)
    for name in os.listdir(curDir):
        try:
            img = Image.open(os.path.join(curDir, name))
        except:
            print('打开文件发生错误')
        Img = img.convert('L')
        ImagBi = Binarization(Img)
        if not os.path.exists(os.path.join('pic-convert', x)):
            os.makedirs(os.path.join('pic-convert', x))

        ImagBi.save(os.path.join('pic-convert', x, name))
