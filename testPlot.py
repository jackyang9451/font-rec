# import matplotlib.pyplot as plt
# import numpy as np
# plt.rcParams['font.family'] = ['sans-serif']
# plt.rcParams['font.sans-serif'] = ['SimHei']
#
# data = {'a': np.arange(50),
#         'c': np.random.randint(0, 50, 50),
#         'd': np.random.randn(50)}
# data['b'] = ['AH'] * 50
# data['d'] = np.abs(data['d']) * 100
#
# plt.scatter('a', 'b', c='c', s='d', data=data)
# plt.xlabel('相关距离S')
# plt.ylabel('哈希算法')
# plt.annotate('最近的值', xy=(2, 1), xytext=(3, 1.5),
#              arrowprops=dict(facecolor='black', shrink=0.05),
#              )
#
# plt.show()


import matplotlib.pyplot as plt
import numpy as np

x = [1, 2, 3, 4]
y = [4, 5, 6, 7]

fig, axs = plt.subplots(3, 1)

axs[0].plot(x, y)
axs[0].plot(y, x)
axs[0].set_title('设置一个title')






plt.show()
