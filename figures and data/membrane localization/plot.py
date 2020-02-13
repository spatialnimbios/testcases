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

default_x = 5*1.4
default_y = 3*1.4

plt.gcf().set_size_inches(default_x, default_y)

#%%
## load data ##
ode_mem = np.loadtxt('Vcell/ode large.txt', skiprows=1)
ode_mem[:,1:9] *= 0.2209

pde_mem = np.loadtxt('Vcell/pde large.txt', skiprows=1)

ssa_mem = np.loadtxt('Vcell/SSA_mem_loc large/SSA_MA_MB_large.txt', delimiter=',')

smoldyn_mem = np.loadtxt('Smoldyn_MA_MB_large.txt', delimiter=',')

fpr_mem = np.loadtxt('Re__Data_etc_/IL_largeBox_Avgs.dat', skiprows=1)

## plot figure ##
fig, ax = plt.subplots()
ax.plot(ode_mem[:,0], ode_mem[:,4], '--', label='ODE')
ax.plot(pde_mem[:,0], pde_mem[:,4], '-.', label = 'PDE')
ax.plot(ssa_mem[0,:], ssa_mem[1,:], ':', label='Gillespie')
ax.plot(smoldyn_mem[:,0], smoldyn_mem[:,1], linestyle=linestyles['densely dashed'], label = 'Smoldyn')
ax.plot(fpr_mem[:,0]*10**(-6), fpr_mem[:,3], label='FPR')
plt.xlim(0, 2)
plt.legend(loc=1, labelspacing = 0.3)
plt.xlabel('time [s]');
plt.ylabel('AM(t)');

axins = ax.inset_axes([0.25, 0.6, 0.37, 0.37])
axins.set_xlim(3, 3.5)
axins.set_ylim(50, 70)
ax.indicate_inset_zoom(axins)
axins.plot(ode_mem[:,0], ode_mem[:,4], '--', label='ODE')
axins.plot(pde_mem[:,0], pde_mem[:,4], '-.', label = 'PDE')
axins.plot(ssa_mem[0,:], ssa_mem[1,:], ':', label='Gillespie')
axins.plot(smoldyn_mem[:,0], smoldyn_mem[:,1], linestyle=linestyles['densely dashed'], label = 'Smoldyn')
axins.plot(fpr_mem[:,0]*10**(-6), fpr_mem[:,3], label='FPR')
axins.set_xticks([3, 3.25, 3.5])
#axins.set_xticks([], False)
axins.set_xticklabels(['3.0','3.25','3.5'])

plt.savefig("plot_membrane_location.pdf",bbox_inches='tight', dpi = 400)
plt.savefig("plot_membrane_location.svg",bbox_inches='tight', dpi = 400)




