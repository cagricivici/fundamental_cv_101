#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 21:40:28 2021

@author: CagriCivici
"""

import numpy as np
import matplotlib.pyplot as plt

#plotting settings
plt.rcParams['figure.figsize'] = (5.0, 4.0) 
plt.rcParams['image.interpolation'] = 'nearest'
plt.rcParams['image.cmap'] = 'Greys'

import pandas as pd

from PIL import Image

import os

def y_shape(input,filter,pad1,pad2):

  n1 = input.shape[0]
  n2 = input.shape[1]

  f1 = filter.shape[0]
  f2 = filter.shape[1]
  
  no_pad = pad1==0 and pad2==0

  if no_pad == True:
    print("there is no padding")

  else: 
    print("padding applied")
    
  y = str(n1+2*pad1-f1+1)+'x'+str(n2+2*pad2-f2+1)
  return y
    


def zero_padding(arr,pad1,pad2):
      
  #((top, bottom), (left, right))
  padd_arr = np.pad(arr, ((pad1,pad2),(pad1,pad2)),mode='constant', constant_values = 0)
    
  return padd_arr



np.random.seed(1)
x = np.random.randn(4, 3, 3, 2)
filtre = np.random.randn(2,2)


pad1 = 2
pad2 = 1


x_pad = zero_padding(x[0,:,:,0],pad1, pad2)

fig, axarr = plt.subplots(1, 2)

axarr[0].set_title('x')
axarr[0].imshow(x[0,:,:,0])
axarr[1].set_title('x_pad')
axarr[1].imshow(x_pad)

fig.savefig("./padding.JPEG")

y= y_shape(x[0,0,:,:],filtre,pad1,pad2)

print("x size:",x.shape[1],'x',x.shape[2])
print("filter size:",filtre.shape[0],'x',filtre.shape[1])

print("(w padding)Convolution output:",y)
print("(w/o padding)Convolution output:",y_shape(x[0,0,:,:],filtre,0,0))

fig_img = Image.open('padding.JPEG')
fig_img.show()
