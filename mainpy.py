#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 01:14:29 2021

@author: CagriCivici
"""

import strider
import padding
import plotting


import numpy as np
import matplotlib.pyplot as plt

#plotting settings
plt.rcParams['figure.figsize'] = (5.0, 4.0) 
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'Greys'


def main():
    
    
    np.random.seed(1)
    x = np.random.randn(4, 5, 5, 2)
    kernel = np.random.randn(2,2)
    
    #x = np.random.randint(9, size=(5, 5))
    #x = [[1,1,1,1,1],[2,2,2,2,2],[4,4,4,4,4],[3,3,3,3,3],[5,5,5,5,5]]
    kernel = [[0,1,1],[1,0,1],[1,1,0]]
    s = 2     #stride
    
    
    x = x[0,:,:,0]
    y = np.array(kernel)
    
    n = x.shape[0] 
    f = y.shape[0] 


    pad = 1
    x_pad = padding.padder(x,pad,pad)
    output_pad = strider.strider(x_pad, y, s, pad,n,f)
    
    
    pad = 0
    output = strider.strider(x, y, s, pad,n,f)
    
    plotting.plotter(x, x_pad, "x", "x_pad", "x_x_pad")
    plotting.plotter(output, output_pad, "y: without padding", "y: with padding", "output")
    
    
    return output, output_pad
    
    

if __name__ == "__main__":
    output,output_pad = main()
    
    
else:
    print("other mains")