# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 21:36:14 2018

@author: sondrbe
"""

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simps

noRisk = 0.0077
Es = [0.03, 0.08, 0.15, 0.30, 0.40]
stdevs = [x-noRisk for x in Es]

def sharpeRatio(E, stdev):
    return (E-noRisk) / stdev

def normal(x, E, stdev):
    return 1/(np.sqrt(2*np.pi*stdev**2))*np.exp(-(x-E)**2/(2*stdev**2))

normal_x = np.linspace(E-3,E+5,200)
normalDist = normal(normal_x, 1+E, 1+stdev)
#plt.plot(normal_x, normalDist)

for E, stdev in zip(Es, stdevs):
    normal_x = np.linspace(E-3,E+5,200)
    normalDist = normal(normal_x, 1+E, 1+stdev)
    plt.plot(normal_x, normalDist)    


x = np.linspace(0,365,365)

counter = 0
for E,stdev,col in zip(Es, stdevs,['r','y','b','g','m']):
    counter += 1
    normal_x = np.linspace(E-3,E+5,200)
    normalDist = normal(normal_x, 1+E, 1+stdev)
    #plt.plot(normal_x, normalDist)
    
    
    for ind1 in range(1,200):
        probs_max = simps(normalDist[:ind1], normal_x[:ind1]) / simps(normalDist, normal_x)
        if probs_max > 0.8:
            break
    E_std_max = normal_x[ind1]*E
    for ind2 in range(1,200):
        probs_min = simps(normalDist[:ind2], normal_x[:ind2]) / simps(normalDist, normal_x)
        if probs_min > 0.2:
            break
    E_std_min = normal_x[ind2]*E

    for E_spread in np.linspace(E_std_min, E_std_max, 120):
        E_cum = np.cumprod(np.array([E_spread/365+1.]*365))
        plt.plot(x,E_cum, col, alpha=0.4)
    #plt.plot(x,E_cum, col, alpha=0.4)        
    #E_mean = np.cumprod(np.array([E/365+1.]*365))
    #plt.plot(x, E_mean, col, alpha=0.4, linewidth=3., label='E'+str(counter))
plt.legend(loc='best')

