# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 15:36:19 2019

@author: explo
"""

import numpy as np

import matplotlib.pyplot as plot

time = np.arange(0, 10, 0.1);

amplitude = np.sin(time)
plot.plot(time, amplitude)
plot.title('Sine wave')
plot.xlabel('Time')
plot.ylabel('Amplitude = sin(time)')
plot.show()
