#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 01:14:29 2021

@author: CagriCivici
"""

def strider(x,y,s,p,n,f):
    import numpy as np

    x = np.array(x)
    print(x)
    y = np.array(y)


    scan_row = int((n+2*p-f)/s+1) 
    scan_column = int((n+2*p-f)/s+1)  
   


    temp_arr = np.zeros((scan_row ,scan_column))

    for j in range (scan_row):

       for i in range(scan_column):
           
           start_row = s*j
           finish_row = s*j+f
           start_column = s*i
           finish_column = s*i+f
           x_clip = x[start_row:finish_row, start_column:finish_column]
           sum_value = np.sum(np.multiply(x_clip,y))
           temp_arr[j][i] = sum_value
        
    print(temp_arr)
    return temp_arr
    

    
    


