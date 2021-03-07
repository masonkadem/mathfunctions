#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 15:02:41 2021

@author: masonkadem
"""

import matplotlib.pyplot as plt
import numpy as np

def plotftn(y):
"""linearly spaced numbers for x-axis"""
    x = np.linspace(-5,5,100)

"""ftn here"""
    y = y

    # setting the axes at the centre
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    
    # plot the function
    plt.plot(x,y, 'g')
    
    # show the plot
    plt.show()