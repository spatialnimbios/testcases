# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:47:21 2020

@author: phenning
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms

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

ssa = np.loadtxt('ssa_1e4_20s_time_Ap_Au_stateID.dat', skiprows = 0)
ssa_time = ssa[:,0]
ssa_Ap = ssa[:,1]
ssa_Au = ssa[:,2]
ssa_low =ssa[:,3]

FPR = np.loadtxt('NERDSS_s1e4_20s_time_Ap_Au_StateID_per10.dat', skiprows = 1)
FPR_time = FPR[:,0]
FPR_Ap = FPR[:,1]
FPR_Au = FPR[:,2]
FPR_low =FPR[:,3]

high = np.loadtxt('ode_hi.gdat', skiprows = 1)
high_time = high[:,0]
high_Ap = high[:,1]

low = np.loadtxt('ode_lo.gdat', skiprows = 1)
low_time = low[:,0]
low_Ap = low[:,1]


## plot figure ##
fig, ax = plt.subplots(2,1)
trans = mtransforms.blended_transform_factory(ax[0].transData, ax[0].transAxes)
ax[0].plot(ssa_time, ssa_Ap, label='Ap', color = 'tab:blue', linewidth=1)
ax[0].plot(ssa_time, ssa_Au, label = 'A', color = 'tab:orange', linewidth=1)
ax[0].plot(low_time, low_Ap, label = 'ODE', color = 'black', linestyle=linestyles['dashed'])
ax[0].plot(high_time, high_Ap, color = 'black', linestyle=linestyles['dashed'])
ax[0].fill_between(ssa_time, 0, 85, where=ssa_low == 1, facecolor='darkgray', alpha=1, transform=trans)
ax[0].xaxis.set_major_formatter(plt.NullFormatter())

ax[0].set_xlim(0, 20)
ax[0].set_ylim(0, 150)
ax[0].legend(loc=1, labelspacing = 0.3, ncol = 3)
#ax[0].set_xlabel('time [s]');
ax[0].set_ylabel('N(t)')
#ax[0].set_title('SSA')

trans = mtransforms.blended_transform_factory(ax[1].transData, ax[1].transAxes)
ax[1].plot(FPR_time, FPR_Ap, label='Ap', color = 'tab:blue', linewidth=1)
ax[1].plot(FPR_time, FPR_Au, label = 'A', color = 'tab:orange', linewidth=1)
ax[1].plot(low_time, low_Ap, label = 'ODE', color = 'black', linestyle=linestyles['dashed'])
ax[1].plot(high_time, high_Ap, color = 'black', linestyle=linestyles['dashed'])
ax[1].fill_between(FPR_time, 0, 85, where=FPR_low == 1, facecolor='darkgray', alpha=1, transform=trans)


ax[1].set_xlim(0, 20)
ax[1].set_ylim(0, 150)
ax[1].legend(loc=1, labelspacing = 0.3, ncol = 3)
ax[1].set_xlabel('time [s]');
#ax[1].set_title('FPR')
ax[1].set_ylabel('N(t)');
default_x = 5.043
default_y = 2.895
plt.rcParams.update({'font.size': 8})


plt.gcf().set_size_inches(default_x, default_y)

plt.savefig("plot_switch.pdf",bbox_inches='tight', dpi = 400)
plt.savefig("plot_switch.svg",bbox_inches='tight', dpi = 400)



