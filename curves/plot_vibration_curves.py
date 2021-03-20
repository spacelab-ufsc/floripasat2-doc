# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import csv
import matplotlib.pyplot as plt

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# -- Sine Test--------------------------------
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

frequency = [4, 7, 100]
acceptance = [0.34, 0.9, 0.9]
qualification = [0.22, 0.6, 0.6]

plt.loglog(frequency, acceptance, '-b', label='Acceptance')
plt.loglog(frequency, qualification, '--r', label='Qualification')

plt.xlim(1, 100)
plt.ylim(0.1, 10)

plt.grid(True, which='both', linestyle=':')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Acceleration [G]')
plt.legend(loc='best')

ratio = 0.05
xleft, xright = plt.axes().get_xlim()
ybottom, ytop = plt.axes().get_ylim()
plt.axes().set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)

plt.savefig('sine_test.pdf', bbox_inches='tight', dpi=600, transparent=True)

plt.show()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# -- Random Vibration ------------------------
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

frequency = [20, 300, 600, 2000]
acceptance = [0.0043, 0.08, 0.08, 0.0071]
qualification = [0.00215, 0.04, 0.04, 0.0036]

plt.loglog(frequency, acceptance, '-b', label='Acceptance')
plt.loglog(frequency, qualification, '--r', label='Qualification')

plt.xlim(10, 1000)
plt.ylim(0.001, 0.1)

plt.grid(True, which='both', linestyle=':')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Acceleration [G]')
plt.legend(loc='best')

ratio = 0.00005
xleft, xright = plt.axes().get_xlim()
ybottom, ytop = plt.axes().get_ylim()
plt.axes().set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)

plt.savefig('random_vibration.pdf', bbox_inches='tight', dpi=600, transparent=True)

plt.show()
