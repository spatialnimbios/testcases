# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:47:21 2020

@author: phenning
"""
import numpy as np
import matplotlib.pyplot as plt

from collections import OrderedDict

linestyles = OrderedDict(
    [('solid',               (0, ())),
     ('loosely dotted',      (0, (1, 10))),
     ('dotted',              (0, (1, 5))),
     ('densely dotted',      (0, (1, 1))),

     ('loosely dashed',      (0, (5, 10))),
     ('dashed',              (0, (5, 5))),
     ('densely dashed',      (0, (5, 1))),

     ('loosely dashdotted',  (0, (3, 10, 1, 10))),
     ('dashdotted',          (0, (3, 5, 1, 5))),
     ('densely dashdotted',  (0, (3, 1, 1, 1))),

     ('loosely dashdotdotted', (0, (3, 10, 1, 10, 1, 10))),
     ('dashdotdotted',         (0, (3, 5, 1, 5, 1, 5))),
     ('densely dashdotdotted', (0, (3, 1, 1, 1, 1, 1)))])

import matplotlib.ticker as mticker
f = mticker.ScalarFormatter(useMathText=True)
f.set_powerlimits((-3,3))
"${}$".format(f.format_data(0.0001))

default_x = 7*1.4
default_y = 3*1.4

plt.gcf().set_size_inches(default_x, default_y)

#%%
## load data ##

ssa = np.loadtxt('Auto_thorsten_ssa.gdat', skiprows = 1)
time = ssa[:,0]
Ap = ssa[:,1]
Ap_P = ssa[:,2]
P_tot =ssa[:,3]

## plot figure ##
fig, ax = plt.subplots()
ax.plot(time, Ap, label='Ap', color = 'tab:blue')
ax.plot(time, Ap_P, label = 'Ap_P', color = 'tab:orange')

plt.xlim(0, 10)
plt.ylim(0, 72)
plt.legend(loc=9, labelspacing = 0.3, ncol = 2)
plt.xlabel('time [s]');
plt.ylabel('N(t)');


plt.savefig("plot_switch.pdf",bbox_inches='tight', dpi = 400)
plt.savefig("plot_switch.svg",bbox_inches='tight', dpi = 400)




