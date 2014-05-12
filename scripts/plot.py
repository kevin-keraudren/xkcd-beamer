#!/usr/bin/python

from xkcdplot import XKCDify
import pylab
import numpy as np
import scipy

recall = [98.75,90.63,96.47,93.34]
precision = [57.05,90.35,73.33,93.11]
x = [1,2,3,4]
xticks = ['Box\n detection',
          'RF/CRF\n segmentation',
          'Enlarged\n segmentation',
          'Final\n segmentation']

pylab.rcParams['figure.figsize'] = 9.8,6

ax = pylab.axes()

#ax.plot( x, recall, c='red' )
#ax.plot( x, precision, c='blue' )

new_x = np.linspace(1,4, 80)
new_recall = np.interp(new_x,x, recall)
new_precision = np.interp(new_x,x, precision)

ax.plot( new_x, new_recall, c='red', label="recall" )
ax.plot( new_x, new_precision, c='blue', label="precision" )

ax.text(1.22, 84, "99%")
ax.plot([1, 1.2], [99, 85], '-k', lw=0.5)

ax.text(2.32, 101, "91%")
ax.plot([2, 2.3], [92, 102], '-k', lw=0.5)

ax.text(3.32, 69, "96%")
ax.plot([3, 3.3], [95, 70], '-k', lw=0.5)

ax.text(4.22, 84, "93%")
ax.plot([4, 4.2], [92, 85], '-k', lw=0.5)

ax.set_xlim(0.6, 4.4)
ax.set_ylim(0, 100)

pylab.xticks(x, xticks)
print pylab.xticks()
#ax.set_title("Idea")

# set legend position
ax.legend(loc='center right')

pylab.savefig('plot1.pdf')

XKCDify( ax,
        expand_axes=True,
        ticks=True, xticks_inside=True, yticks_inside=False)

pylab.savefig('plot2.pdf')
