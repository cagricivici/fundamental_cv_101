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
    
    #x: input
    np.random.seed(1)
    x = np.random.rand(4, 5, 5, 2)
    #x = np.random.randint(9, size=(5, 5))
    x = x[0,:,:,0]
    
    #kernel: filter
    kernel = np.random.randn(2,2)
    
    s = 2     #stride
    n = x.shape[0] 
    f = kernel.shape[0] 
    
    #padding on x matrix
    pad = 1
    x_pad = padding.padder(x,pad,pad)
    output_pad = strider.strider(x_pad, kernel, s, pad,n,f)
    
    #no padding on x matrix
    pad = 0
    output = strider.strider(x, kernel, s, pad,n,f)
    
    #plotting inputs
    plotting.plotter(x, x_pad, "x", "x_pad", "x_x_pad")
    #plotting convolution outputs
    plotting.plotter(output, output_pad, "y: without padding", "y: with padding", "output")
    
    return output, output_pad
    

if __name__ == "__main__":
    output,output_pad = main()
    
    #dimension results of padding and no padding 
    print("y without padding:", output.shape)
    print("y with padding:", output_pad.shape)
    
    
else:
    print("other mains")