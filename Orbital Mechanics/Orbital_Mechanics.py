import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

plt.style.use('seaborn-poster')
fig = plt.figure(figsize = (10,10))
ax = plt.axes(projection='3d')

mu = 3.9860 * 10 ** 14
dt = 0.1

def mag(v):

    return (v[0]*v[0] + v[1]*v[1] + v[2]*v[2]) ** 0.5

def rk4_step(x0,v0,dt):

   k1 = v0
   a0 = - mu / x0 * 2
   k2 = k1 + a0 * dt
   x1= x0 + k2 * dt 
   a1 = - mu / x1 * 2
   k3 = k2 + a1 * dt
   x2 = x1 + k3 * dt
   a2 = - mu / x2 * 2
   k4 = k3 + a2 * dt
   
   xnext = x0 + (k1+2*k2+2*k3+k4) / 6 * dt
   vnext = (k1+2*k2+2*k3+k4)
   
   return (xnext,vnext)

# Initial Values
r = [384400 * 10 ** 3,565,854]
v = [1022,0,0]

rx = r[0]
ry = r[1]
rz = r[2]
    
vx = v[0]
vy = v[1]
vz = v[2]


for t in range(1000):
    
    rx = rk4_step(rx,vx,1)[0]
    ry = rk4_step(ry,vy,1)[0]
    rz = rk4_step(rz,vz,1)[0]

    vx = rk4_step(rx,vx,1)[1]
    vy = rk4_step(ry,vy,1)[1]
    vz = rk4_step(rz,vz,1)[1]
    
    ax.plot3d(rx,ry,rz)
    t = t+dt

plt.show()
     






  