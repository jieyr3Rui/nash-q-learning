#方法一，利用关键字
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from data import *

def plot_line(ax, point1, point2, color='r'):
    line = np.linspace(point1, point2, num=50)
    ax.plot(line[:,0], line[:,1], line[:,2], c=color)

#定义坐标轴
fig = plt.figure()
ax1 = plt.axes(projection='3d')

pos = np.array(p)


x = pos[:, 0]
y = pos[:, 1]
z = pos[:, 2]

ax1.scatter3D(x,y,z, cmap='Blues')  #绘制散点图

for i in range(pN):
    for j in range(i+1, pN):
        if c[i][j] == 1:
            plot_line(ax1, pos[i], pos[j], 'r')


plot_line(ax1, [0, 0, 60], [600, 0, 60], 'w')
plot_line(ax1, [0, 700, 140], [600, 700, 140], 'w')

plt.xlim(0, 600)
plt.ylim(0, 700)

plt.show()