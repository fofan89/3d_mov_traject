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





class Plane():
    def __init__(self, x, y, z, vx, vy, vz):
        self.x = [x]
        self.y = [y]
        self.z = [z]
        
        self.vx = [vx]
        self.vy = [vy]
        self.vz = [vz]
    
    def acell(self):
        r=(self.x[-1]**2+self.y[-1]**2+self.z[-1]**2)**.5
        a=.2/r**2
        
        axx = a* -self.x[-1]/r
        ayy = a* -self.y[-1]/r
        azz = a* -self.z[-1]/r
        
        self.vx.append(self.vx[-1]+axx)
        self.vy.append(self.vy[-1]+ayy)
        self.vz.append(self.vz[-1]+azz)
        

        self.x.append(self.x[-1]+self.vx[-1])
        self.y.append(self.y[-1]+self.vy[-1])
        self.z.append(self.z[-1]+self.vz[-1])
        
        
        
# vx=[.1]
# vy=[.1]
# vz=[.25]


# x1=[2]
# y1=[1]
# z1=[1]

plane1 = Plane(2, 1, 1, .1, .1, .25)

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
        
        # axx,ayy,azz = acel(x1[-1], y1[-1], z1[-1])

        
        # vx.append(vx[-1]+axx)
        # vy.append(vy[-1]+ayy)
        # vz.append(vz[-1]+azz)
        

        # x1.append(x1[-1]+vx[-1])
        # y1.append(y1[-1]+vy[-1])
        # z1.append(z1[-1]+vz[-1])
        
        plane1.acell()
        
        
        yield np.array([plane1.x[-1], plane1.y[-1], plane1.z[-1]])

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