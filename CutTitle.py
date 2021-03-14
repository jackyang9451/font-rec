"""
去除有水印图片的水印

1 遍历拿到所有图像
2 截去底部长方形区域
3 保存新的图片
"""

from PIL import Image
import os


def CutTile(img):
    cropped = img.crop((0, 0, 378, 378))
    return cropped


for x in os.listdir('TestPic'):
    img = Image.open(os.path.join('TestPic', x))
    CutTile(img).save(os.path.join('TestPic', x))


