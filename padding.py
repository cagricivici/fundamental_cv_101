#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 10 01:09:22 2021

@author: CagriCivici
"""

import numpy as np

def padder(arr,pad1,pad2):
    
    
     #((top, bottom), (left, right))
    padd_arr = np.pad(arr, ((pad1,pad2),(pad1,pad2)),mode='constant', constant_values = 0)
    print("arr",arr)
    
    
    return padd_arr