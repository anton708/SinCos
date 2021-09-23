#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:25:11 2021

@author: Anton
"""
import numpy as np
import matplotlib.pyplot as m

#create array from 0 to 2*pi by incremements of 0.1
x = np.arange(0,2*np.pi,0.1)

#plot
m.plot(x, np.sin(x), label="sin")  #Sin graph
m.plot(x,np.cos(x),label="cos")    #Cos graph
m.title('Sin-Cos Graph')           #Add title
m.xticks([0,np.pi/2,np.pi,3*np.pi/2,2*np.pi],['0', '\u03C0/2', '\u03C0','3\u03C0/2','2\u03C0'])     #label x values
m.legend()   #create legend
m.show()
