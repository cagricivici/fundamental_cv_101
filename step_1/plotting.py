#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 22:24:45 2021

@author: CagriCivici
"""

from PIL import Image

import matplotlib.pyplot as plt

def plotter (x,y,title1,title2,figname):
    
    #plotting 
    fig, axarr = plt.subplots(1, 2)

    axarr[0].set_title(title1)
    axarr[0].imshow(x)
    axarr[1].set_title(title2)
    axarr[1].imshow(y)
    
    #saving
    fig.savefig("./"+figname+".JPEG")

    #opening
    fig_img = Image.open("./"+figname+".JPEG")
    fig_img.show()