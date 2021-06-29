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
        

def acceler(pll):
    for i in pll:
        for j in pll:
           if i != j:
               r=((j.x[-1]-i.x[-1])**2 + (j.y[-1]-i.y[-1])**2 + (j.z[-1]-i.z[-1])**2)**.5
               a=.002/r**2
               
               axx = a* (j.x[-1]-i.x[-1])/r
               ayy = a* (j.y[-1]-i.y[-1])/r
               azz = a* (j.z[-1]-i.z[-1])/r
               
               j.vx.append(j.vx[-1]+axx)
               j.vy.append(j.vy[-1]+ayy)
               j.vz.append(j.vz[-1]+azz)
              
def acell(pl):
    
    for i in pl:
        for j in pl:
            if i!=j:
                r=((j.x[-1] - i.x[-1])**2+(j.y[-1]-i.y[-1])**2 + (j.z[-1]-i.z[-1])**2)**.5
                a=.001/r**2
                
                axx = a* (j.x[-1] - i.x[-1])/r
                ayy = a* (j.y[-1] - i.y[-1])/r
                azz = a* (j.z[-1] - i.z[-1])/r
                

                i.vx.append(i.vx[-1]+axx)
                i.vy.append(i.vy[-1]+ayy)
                i.vz.append(i.vz[-1]+azz)

    
                # i.x.append(i.x[-1]+i.vx[-1])
                # i.y.append(i.y[-1]+i.vy[-1])
                # i.z.append(i.z[-1]+i.vz[-1])
               
               
 
        

plane1 = Plane(2, 1, 1, .1, .1, .25)
plane2 = Plane(1, 2, 1, -.1, .1, -.3)
planetus = [plane1, plane2]


line, = ax.plot([], [], [], lw=2)
line1, = ax.plot([], [], [], lw=2)


def init():
    line.set_data([], [])
    line.set_3d_properties([])
    line1.set_data([], [])
    line1.set_3d_properties([])
    
    return line, line1



def update(frames):
    acell(planetus)
      
    line.set_data(plane1.x[:frames], plane1.y[:frames])
    line.set_3d_properties(plane1.z[:frames])
    line1.set_data(plane2.x[:frames], plane2.y[:frames])
    line1.set_3d_properties(plane2.z[:frames])
    
    return line, line1,

# N = 1000
# data = np.array(list(gen(N, plane1))).T
# data1 = np.array(list(gen(N, plane2))).T
# line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1])
# line1, = ax.plot(data1[0, 0:1], data1[1, 0:1], data1[2, 0:1])

# Setting the axes properties
ax.set_xlim3d([-10.0, 10.0])
ax.set_xlabel('X')

ax.set_ylim3d([-10.0, 10.0])
ax.set_ylabel('Y')

ax.set_zlim3d([-10.0, 10.0])
ax.set_zlabel('Z')

ani = animation.FuncAnimation(fig, update, init_func=init, frames=np.linspace(0, 1000, 1), interval=1, blit=False)
#ani.save('matplot003.gif', writer='imagemagick')
plt.show()