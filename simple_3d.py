from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np



fig = plt.figure()

ax = fig.gca(projection="3d")

ax.set_xlim3d([-10.0, 10.0])
ax.set_ylim3d([-10.0, 10.0])
ax.set_zlim3d([-10.0, 10.0])

# elevation = 10
# viewing_angle = 125

# ax.view_init(elev=elevation, azim=viewing_angle)
line, = ax.plot([], [], [])
line1, = ax.plot([], [], [])
line2, = ax.plot([], [], [])




class Planetus():
    def __init__(self, x, y, z, vx, vy, vz, m):
        self.x = np.array([x])
        self.y = np.array([y])
        self.z = np.array([z])
        
        self.vx = [vx]
        self.vy = [vy]
        self.vz = [vz]
        
        self.m = m


planet1 = Planetus(1, 2, 5, .1, .2, .1, 5)
planet2 = Planetus(-1, 2, 5, .1, .2, .1, 25)
planet3 = Planetus(-3, 2, 5, .1, .2, .1, 1)
planetuss = [planet1, planet2, planet3]

def acell(pl):
    r=(pl.x[-1]**2+pl.y[-1]**2+pl.z[-1]**2)**.5
    a=.5/r**2
    
    axx = a* -pl.x[-1]/r
    ayy = a* -pl.y[-1]/r
    azz = a* -pl.z[-1]/r
    
    pl.vx.append(pl.vx[-1]+axx)
    pl.vy.append(pl.vy[-1]+ayy)
    pl.vz.append(pl.vz[-1]+azz)
    

def acceler(pll):
    for i in pll:
        for j in pll:
           if i != j:
               r=((j.x[-1]-i.x[-1])**2 + (j.y[-1]-i.y[-1])**2 + (j.z[-1]-i.z[-1])**2)**.5
               a=.0001*i.m/r**2
               
               axx = a* (j.x[-1]-i.x[-1])/r
               ayy = a* (j.y[-1]-i.y[-1])/r
               azz = a* (j.z[-1]-i.z[-1])/r
               
               j.vx.append(j.vx[-1]+axx)
               j.vy.append(j.vy[-1]+ayy)
               j.vz.append(j.vz[-1]+azz)

    

for i in range(2000):
    
    acell(planet1)
    acell(planet2)
    acell(planet3)
    
    acceler(planetuss)
    
    planet1.x = np.append(planet1.x, planet1.x[-1]+planet1.vx[-1])
    planet1.y = np.append(planet1.y, planet1.y[-1]+planet1.vy[-1])
    planet1.z = np.append(planet1.z, planet1.z[-1]+planet1.vz[-1])
    
    planet2.x = np.append(planet2.x, planet2.x[-1]+planet2.vx[-1])
    planet2.y = np.append(planet2.y, planet2.y[-1]+planet2.vy[-1])
    planet2.z = np.append(planet2.z, planet2.z[-1]+planet2.vz[-1])
    
    planet3.x = np.append(planet3.x, planet3.x[-1]+planet3.vx[-1])
    planet3.y = np.append(planet3.y, planet3.y[-1]+planet3.vy[-1])
    planet3.z = np.append(planet3.z, planet3.z[-1]+planet3.vz[-1])




def animate(i):
    
    if i>50:
        planet1.x=np.delete(planet1.x,[0])
        planet1.y=np.delete(planet1.y,[0])
        planet1.z=np.delete(planet1.z,[0])
    

    line.set_data(planet1.x[:i], planet1.y[:i])
    line.set_3d_properties(planet1.z[:i])
    
    line1.set_data(planet2.x[:i], planet2.y[:i])
    line1.set_3d_properties(planet2.z[:i])
    
    line2.set_data(planet3.x[:i], planet3.y[:i])
    line2.set_3d_properties(planet3.z[:i])
    

    fig.canvas.draw()

    return line, line1, line2, 


anim = animation.FuncAnimation(fig, animate, frames=1000, interval=25)

plt.show()