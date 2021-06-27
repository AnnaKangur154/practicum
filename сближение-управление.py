# -*- coding: utf-8 -*-

x0 = -0.5203646
z0 = 0.4121385

x1 = -0.5381485
z1 = 0.3654952

x2 = -0.5765352
z2 = 0.353218

x3 = -0.5842284
z3 = 0.3596607

x4 = -0.4997233
z4 = 0.3687667

xr = -0.1973027
zr = -8.266576

xl = -0.837943
zl = 9.055133

import matplotlib.pyplot as plt 
import numpy as np

x = np.array([x0, x1, x2, x3, x4])
z = np.array([z0, z1, z2, z3, z4])

n = len(x)
for i in range(n):
    x[i] = x[i] - x0
    z[i] = z[i] - z0
print(x)
print(z)    
xl -= x0
zl -= z0

xr -= x0
zr -= z0


#plt.title("") 
fig, ax = plt.subplots() 
for i in range(n):
    ax.plot(x[i], z[i], 'o', color='b')
    plt.text(x[i], z[i], i, fontsize=10)
ax.plot(xr, zr, 'o', color='r')
plt.text(xr, zr, 'u = 4', fontsize=10)  
ax.plot(xl, zl, 'o', color='r')
plt.text(xl, zl, 'u = -4', fontsize=10)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_xlabel('ось сближения')
ax.set_ylabel('ось управления')
plt.show()  

#plt.title("") 
fig, ax = plt.subplots() 
for i in range(n):
    ax.plot(x[i], z[i], 'o', color='b')
    plt.text(x[i], z[i], i, fontsize=10)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_xlabel('ось сближения')
ax.set_ylabel('ось управления')
 

xmax = x[0]
ind = 0
for i in range(1,n):
    if xmax < abs(x[i]):
        xmax = abs(x[i])
        ind = i

ax.plot([x[ind], 0],[z[ind],z[ind]], c='red')

circle = plt.Circle((0, z[ind]), x[ind], fill=False)
ax.set_aspect(1)
ax.add_artist(circle)
plt.show() 


#plt.title("") 
fig, ax = plt.subplots() 
for i in range(n):
    ax.plot(x[i], z[i], 'o', color='b')
    plt.text(x[i], z[i], i, fontsize=10)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_xlabel('ось сближения')
ax.set_ylabel('ось управления')

ax.plot([x[ind], 0],[z[ind],z[ind]], c='red')

circle = plt.Circle((0, z[ind]), x[ind], fill=False)
ax.set_aspect(1)
ax.add_artist(circle)
plt.ylim(-0.15, 0.025)
plt.xlim(-0.1, 0.1)
plt.show() 

'''# изначально x = -20 

# 50% от исходного x = -10
x01 = -0.5287454 #-0.5287454 
z01 = 0.1965987  #0.1965987

x31 = -0.558143
z31 = -0.02336011

# расстояние 200% от исходного x = -40
x02 = -0.4601043
z02 = 0.8275512

x32 = -0.6269785
z32 = -0.09575509


# изначально t = 70

# 70% от исходного t = 50c
x03 = -0.5005707
z03 = 0.4123563

x33 = -0.5720876
z33 = -0.04866795

# 200% от исходного  t = 140c
x04 = -0.5394551
z04 = 0.4106779

x34 = -0.6028596
z34 = -0.04892139'''

fig, ax = plt.subplots() 
for i in range(n):
    ax.plot(x[i], z[i], 'o', color='b')
    plt.text(x[i], z[i], i, fontsize=10)
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_xlabel('ось сближения')
ax.set_ylabel('ось управления')
ax.plot([x[ind], 0],[z[ind],z[ind]], c='red')
circle = plt.Circle((0, z[ind]), x[ind], fill=False)
ax.set_aspect(1)
ax.add_artist(circle)


#70% расстояние и время
x01 = -0.5111117
z01 = 0.2848325

x11 = -0.5314217
z11 = 0.2529218

x21 = -0.5591679 #-0.5587428
z21 = 0.2450711  #0.2459523

x31 = -0.5437531 #-0.5438256
z31 = 0.2499173  #0.2521057

x41 = -0.4751464
z41 = 0.2565514

x_n1 = [x01, x11, x21, x31, x41]
z_n1 = [z01, z11, z21, z31, z41] 

for i in range(len(x_n1)):
    x_n1[i] -= x0
    z_n1[i] -= z0
    ax.plot(x_n1[i], z_n1[i], 'o', color='g')
    plt.text(x_n1[i], z_n1[i], i, fontsize=10)
   
    
#200%
x02 = -0.4923833
z02 = 0.8231903

x12 = -0.5068601
z12 = 0.7470212

x22 = -0.5558994
z22 = 0.718879

x32 = -0.6295996
z32 = 0.7319248

x42 = -0.4874882
z42 = 0.7431421

x_n2 = [x02, x12, x22, x32, x42]
z_n2 = [z02, z12, z22, z32, z42] 

for i in range(len(x_n2)):
    x_n2[i] -= x0
    z_n2[i] -= z0
    ax.plot(x_n2[i], z_n2[i], 'o', color='r')
    plt.text(x_n2[i], z_n2[i], i, fontsize=10)
plt.xlim(-0.4, 0.4)    
plt.show()

fig, ax = plt.subplots() 
for i in range(len(x_n1)):
    ax.plot(x_n1[i], z_n1[i], 'o', color='g')
    plt.text(x_n1[i], z_n1[i], i, fontsize=10)
    
ax.axhline(y=0, color='k')
ax.axvline(x=0, color='k')
ax.set_xlabel('ось сближения')
ax.set_ylabel('ось управления')

xmax = x_n1[0]
ind = 0
for i in range(1,len(x_n1)):
    if xmax < abs(x_n1[i]):
        xmax = abs(x_n1[i])
        ind = i

ax.plot([x_n1[ind], 0],[z_n1[ind],z_n1[ind]], c='red')

circle = plt.Circle((0, z_n1[ind]), x_n1[ind], fill=False)
ax.set_aspect(1)
ax.add_artist(circle)
plt.show() 









