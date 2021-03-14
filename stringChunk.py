"""
递归截取字符串中的数据
s: 文章字符串
"""

stringList = []

def findByName(s, name, index):
    nextIndex = s.find(name, index)
    if nextIndex != -1:
        chunkString(nextIndex)
        findByName(name, nextIndex)


def chunkString(index):
    # 截取当前索引前后各20各文章
    frontString = ''
    endString = ''
    stringList.append(frontString)
    stringList.append(endString)

findByName(s, '贾宝玉', 0)