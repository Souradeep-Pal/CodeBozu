import tkinter
import sys
import matplotlib
matplotlib.use('TkAgg')
#for display on tkinter window

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([2, 6])
ypoints = np.array([0, 250])
#line will be plotted from (2,0) to (0,250)

#by default, plot() plots a line between points 
plt.plot(xpoints, ypoints)
plt.show()

#use 'o' to just show points
plt.plot(xpoints, ypoints, 'o')
plt.show()

#multiple points can be plotted
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])
plt.plot(xpoints, ypoints)
plt.show()

#default x-values are [1,2,3,4,...]
ypoints = np.array([3, 8, 1, 10, 5, 7])
plt.plot(ypoints)
plt.show()

#markers
#examples include 'o', '*', '.' and ',' signifying circle, star, point and pixel
ypoints = np.array([3, 8, 1, 10])
plt.plot(ypoints, marker = 'o')
plt.show()
# 'o' denotes marker reference
# ':' denotes line reference
# 'r' denotes colour reference
plt.plot(ypoints, 'o:r')
plt.show()
#marker size(ms)
plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()
#marker edge colour
plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
plt.show()
#marker face colour
plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
plt.show()


plt.savefig(sys.stdout.buffer)
sys.stdout.flush()