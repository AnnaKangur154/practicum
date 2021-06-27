# -*- coding: utf-8 -*-
import numpy as np 
import pandas as pd
	
import matplotlib.pyplot as plt

from scipy.spatial.transform import Rotation as R

import math

#df = pd.read_csv('file.txt', header = None, sep=';', dtype = float)

#df = pd.read_csv('file.txt', header = None, sep=';', dtype = float, skiprows = 3950, nrows = 250)

df = pd.read_csv('file.txt', header = None, sep=';', dtype = float, skiprows = 4200, nrows = 500)


n = len(df)
print('n = ', n)



v1 = []

tim = []
for i in range(n-1):
    tim.append((df[0][i+1]-df[0][i])/ 10**7)

for i in range(n-1):
    tmp = (df[1][i+1] - df[1][i]) / tim[i]
    #if math.fabs(tmp) < 2000:
    v1.append(tmp)
#print(v1)    

r = []
ar = []
for i in range(n):
    r.append(R.from_quat([df[3][i], df[4][i], df[5][i], df[6][i]]))    
    ar.append(r[i].as_euler('xyz', degrees=True))   
ar = np.array(ar)

v2 = []
ae = []
for i in range(len(ar)-1):
    v2.append((ar[i+1,1]-ar[i,1]) / tim[i])
    ae.append(ar[i+1,1])


from scipy import signal


v3 = signal.medfilt(v1, 5)
v4 = signal.medfilt(v2, 5)

plt.title("Горизонтальное положение правого глаза")
#plt.plot(v1,label = "без фильтра")
plt.plot(v3,label = "с фильтром")
plt.legend()
plt.show()

plt.title("Положение головы")
plt.plot(v2,label = "без фильтра")
plt.plot(v4,label = "с фильтром")
plt.legend()
plt.show()



v = []
t = []








for i in range(n-1):
    tmp = v4[i] + v3[i] #math.fabs(v4[i] - v3[i])
    if tmp <= 8:
        v.append(tmp)
        t.append((df[0][i+1]-df[0][i])/10**7)

sumt = sum(t)
sumT = (df[0][n-1] - df[0][0])/10**7

print(sumt, sumT)

print(sumt/sumT)

vsum = []
for i in range(n-1):
    s = v3[i] + v4[i]
    vsum.append(s)
        
plt.title("Скорость глаза и скорость головы")
plt.plot(v3,label = "скорость глаза")
plt.plot(v4,label = "скорость головы")
plt.plot(vsum,label = "сумма")
plt.legend()
plt.xlim(150, 175)
plt.show()      
        




plt.title("Угол поворота головы и угол поворота глаза")
plt.plot(df[1],label = "угол глаза")
plt.plot(ae,label = "угол головы")

asum = []
for i in range(n-1):
    s = df[1][i] + ae[i]
    asum.append(s)
    
plt.plot(asum, label = "сумма")

plt.xlim(200, 400)


plt.legend()
plt.show()      
        




















        
        
        
        
        
        
        
        
        
        
        
        