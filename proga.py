# -*- coding: utf-8 -*-
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy import signal

def main(a, b, c = 0, d = 0):
    veye0 = veye[a:b]
    plt.title("Скорость отклонения положения (град/с)")
    plt.plot(veye0, label = "Правого зрачка")
    vhead0 = vhead[a:b]
    plt.plot(vhead0, label = "Головы (град/с)")
    plt.legend()
    plt.show()
    time0 = time[a:b]
    
    
    plt.title("Скорость отклонения правого зрачка (град/с)")
    plt.plot(veye0, label = "без фильтра")
    veye3 = signal.medfilt(veye0, 3)
    plt.plot(veye3, label = "медианный фильтр 3")
    veye5 = signal.medfilt(veye0, 5)
    plt.plot(veye5, label = "медианный фильтр 5")
    plt.legend()
    plt.show()
    
    
    plt.title("Скорость отклонения головы (град/с)")
    plt.plot(vhead0, label = "без фильтра")
    vhead3 = signal.medfilt(vhead0, 3)
    plt.plot(vhead3, label = "медианный фильтр 3")
    vhead5 = signal.medfilt(vhead0, 5)
    plt.plot(vhead5, label = "медианный фильтр 5")
    plt.legend()
    plt.show()
    
    n = len(veye5)
    v = []
    for i in range(n):
        v.append(veye5[i] + vhead5[i])
    
    plt.title("Скорости")
    plt.plot(veye5, label = "глаз", c = 'pink')
    plt.plot(vhead5, label = "голова", c = '#ab99b8')
    plt.legend()
    plt.show()
    
    plt.title("Скорости")
    plt.plot(veye5, label = "глаз", c = 'pink')
    plt.plot(vhead5, label = "голова", c = '#ab99b8')
    plt.plot(v, label = "cумма скоростей", c = 'r')
    plt.legend()
    #plt.xlim(0, 10)
    plt.show()
    
    S = 0
    for i in range(n):
        if v[i] <= 4:
            S += time0[i]
    
    print(S/sum(time0))
    
    if d != 0:
        plt.title("Скорости")
        plt.plot(veye5, label = "глаз", c = 'pink')
        plt.plot(vhead5, label = "голова", c = '#ab99b8')
        plt.plot(v, label = "cумма скоростей", c = 'r')
        plt.legend()
        plt.xlim(c, d)
        plt.show()





#df = pd.read_csv('file.txt', header = None, sep=';', dtype = float)

#df = pd.read_csv('file.txt', header = None, sep=';', dtype = float, skiprows = 3950, nrows = 250)

df = pd.read_csv('data.txt', header = None, sep=';', dtype = float)
n = len(df)

time = []
for i in range(n-1):
    time.append((df[0][i+1] - df[0][i]) * 1e-7)

veye = []
for i in range(n-1):
    veye.append((df[1][i+1] - df[1][i]) / time[i])
    
plt.title("Скорость отклонения положения (град/с)")
plt.plot(veye, label = "Правого зрачка")


euler = []
from scipy.spatial.transform import Rotation as R
for i in range(n):
    euler.append(R.from_quat([df[3][i], df[4][i], df[5][i], df[6][i]]).as_euler('xyz', degrees=True))
euler = np.array(euler)
vhead = []
for i in range(n-1):
    vhead.append((euler[i+1,1] - euler[i,1]) / time[i]) 

plt.plot(vhead, label = "Головы (град/с)")
plt.legend()
plt.show()

main(2200, 2500)
#main(2500, 2900, 0)
main(3300, 3800, 355, 365)














        
        
        
        
        
        
        
        
        
        
        
        