# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 07:55:03 2021

@author: fofan
"""

from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation

fig = plt.figure()
ax = p3.Axes3D(fig)

# def gen(n):
#     phi = 0
#     while phi < 2*np.pi:
#         yield np.array([np.cos(phi), np.sin(phi), phi])
#         phi += 2*np.pi/n

vx=[.1]
vy=[.1]
vz=[.25]

x1=[2]
y1=[1]
z1=[1]

def acel(x,y,z):
    r=(x**2+y**2+z**2)**.5
    a=.2/r**2
    
    axx = a* -x/r
    ayy = a* -y/r
    azz = a* -z/r
    
    return axx,ayy,azz
    

def gen(n):    
    phi = 0
    while phi < 1000:
        
        axx,ayy,azz = acel(x1[-1], y1[-1], z1[-1])
        
        vx.append(vx[-1]+axx)
        vy.append(vy[-1]+ayy)
        vz.append(vz[-1]+azz)
        
        x1.append(x1[-1]+vx[-1])
        y1.append(y1[-1]+vy[-1])
        z1.append(z1[-1]+vz[-1])
        
        yield np.array([x1[-1], y1[-1], z1[-1]])
        phi += .1


def update(num, data, line):
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])

N = 1000
data = np.array(list(gen(N))).T
line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])

# Setting the axes properties
ax.set_xlim3d([-10.0, 10.0])
ax.set_xlabel('X')

ax.set_ylim3d([-10.0, 10.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-10.0, 10.0])
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=1, blit=False)
#ani.save('matplot003.gif', writer='imagemagick')
plt.show()