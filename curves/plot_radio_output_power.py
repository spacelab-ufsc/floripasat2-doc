# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import sys
import csv
import matplotlib.pyplot as plt

power = list()
freq = list()

with open(sys.argv[1]) as csvfile:
    reader = csv.reader(csvfile, delimiter=str(','), quotechar=str('|'))
    try:
        for row in reader:
            power.append(float(row[0]))     # y-axis
            freq.append(float(row[1]))      # x-axis
    except:
        pass

plt.plot([min(freq), max(freq)], [max(power), max(power)], '--r', label=('Max. Power (' + str(round(max(power), 2)) + ' dBm)'), linewidth=1.0)   # FFT curve

#if max(freq) > 400e6:
#    plt.plot([145.9e6, 145.9e6], [min(power), max(power)], '-.c', label='Freq. central (145,9 MHz)', linewidth=1.0) # Centre frequency
#else:
#    plt.plot([436.1e6, 436.1e6], [min(power), max(power)], '-.c', label='Freq. central (436,1 MHz)', linewidth=1.0) # Centre frequency

plt.plot(freq, power, '-b', label='FFT', linewidth=0.75)    # Max power curve

plt.grid(True, linestyle=':')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Power [dBm]')
plt.legend(loc='best')

ratio = 0.5
xleft, xright = plt.axes().get_xlim()
ybottom, ytop = plt.axes().get_ylim()
plt.axes().set_aspect(abs((xright-xleft)/(ybottom-ytop))*ratio)

if max(freq) > 400e6:
    plt.savefig('downlink_output_power.pdf', bbox_inches='tight', dpi=600, transparent=True)
else:
    plt.savefig('beacon_output_power.pdf', bbox_inches='tight', dpi=600, transparent=True)

plt.show()
