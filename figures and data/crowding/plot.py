# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:01:00 2020

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

plt.rcParams.update({'font.size': 14})

#%%
########## Plot crowding 1 ##########

egfre_crowding1 = np.loadtxt('kfiitvals_vs_C_vsSEM_eGFRD.dat', skiprows=0)

fpr_crowding1 = np.loadtxt('kfitvals_vsC_vsSEM_FPR.dat', skiprows=0)


fig, ax = plt.subplots()
l2, caps2, c2 = ax.errorbar(fpr_crowding1[1:,0], fpr_crowding1[1:,1], fpr_crowding1[1:,2], uplims= True, lolims= True, marker='o', label = "FPR")
l, caps, c = ax.errorbar(egfre_crowding1[1:,0], egfre_crowding1[1:,1], egfre_crowding1[1:,2], uplims= True, lolims= True, marker='o', label = "eGFRD")
for cap in caps:
    cap.set_marker("_")
for cap in caps2:
    cap.set_marker("_")
ax.plot([-1, 1],[fpr_crowding1[0,1], fpr_crowding1[0,1]], color="black", linestyle = 'dashed')
ax.set_xlim(0, 0.26)
plt.legend(loc=0)
plt.xlabel(r'Volume Fraction Occupied $\phi$');
plt.ylabel(r'$k_{fit}=nm^3/\mu s$');

plt.savefig("crowding_C.svg",bbox_inches='tight', dpi = 400)
plt.savefig("crowding_C.pdf",bbox_inches='tight', dpi = 400)


#%%


########## Plot crowding 2 ##########
egfrd_crowding2 = np.loadtxt('GFRD_C0_time_vs_AvgOve10_vs_STDEV.dat', skiprows=0)
egfrd_crowding2[:,2] /= np.sqrt(10)

fpr_crowding2 = np.loadtxt('FPR_C0_dt1e-5us_time_vs_Avg80traj_vs_STDEV.dat', skiprows=1)
fpr_crowding2[:,2] = fpr_crowding2[:,2]/np.sqrt(80)

fpr_fit = 100*np.exp(-100*65.4/12500*fpr_crowding2[:,0]*1e6)
egfrd_fit = 100*np.exp(-100*64.88/12500*egfrd_crowding2[:,0]*1e6)

fig, ax = plt.subplots()
plt.plot([], [], ' ', label="Simulation")
ax.plot(fpr_crowding2[:,0]*1e6, fpr_crowding2[:,1],label = "FPR", color='tab:blue')
ax.plot(egfrd_crowding2[:,0]*1e6, egfrd_crowding2[:,1] ,label = "eGFRD", color='tab:orange')
ax.fill_between(fpr_crowding2[:,0]*1e6, fpr_crowding2[:,1]+fpr_crowding2[:,2], fpr_crowding2[:,1]-fpr_crowding2[:,2], alpha=0.4)
ax.fill_between(egfrd_crowding2[:,0]*1e6, egfrd_crowding2[:,1]+egfrd_crowding2[:,2], egfrd_crowding2[:,1]-egfrd_crowding2[:,2], alpha=0.4)
plt.plot([], [], ' ', label="Fit")
ax.plot(fpr_crowding2[:,0]*1e6, fpr_fit, linestyle=linestyles['dashed'], label = 'FPR', color='blue')
ax.plot(egfrd_crowding2[:,0]*1e6, egfrd_fit, linestyle=linestyles['densely dotted'], label = 'eGFRD', color = 'red')
ax.text(4, 50, r'$\phi$ = 0.008', fontsize = 18)

ax.set_xlim(0, 12)
ax.set_ylim(1e-1, 1e2)
ax.set_yscale('log')
ax.legend(loc = 3, labelspacing = 0.3)
plt.xlabel(r'time [$\mu s$]');
plt.ylabel(r'A(t)');

#plt.savefig("crowding_C0.pdf",bbox_inches='tight', dpi = 400)
#plt.savefig("crowding_C0.svg",bbox_inches='tight', dpi = 400)





########## Plot crowding 3 ##########
egfrd_crowding3 = np.loadtxt('GFRD_C25_time_vs_AvgOve10_vs_STDEV.dat', skiprows=0)
egfrd_crowding3[:,2] /= np.sqrt(10)

fpr_crowding3 = np.loadtxt('FPR_C25_dt5e-6us_time_vs_Avg80traj_vs_STDEV.dat', skiprows=1)
fpr_crowding3[:,2] = fpr_crowding3[:,2]/np.sqrt(80)

fpr_fit = 100*np.exp(-100*99/12500*fpr_crowding3[:,0]*1e6)
egfrd_fit = 100*np.exp(-100*87.3/12500*egfrd_crowding3[:,0]*1e6)

fig, ax = plt.subplots()
plt.plot([], [], ' ', label="Simulation")
ax.plot(fpr_crowding3[:,0]*1e6, fpr_crowding3[:,1],label = "FPR", color='tab:blue')
ax.plot(egfrd_crowding3[:,0]*1e6, egfrd_crowding3[:,1] ,label = "eGFRD", color='tab:orange')
ax.fill_between(fpr_crowding3[:,0]*1e6, fpr_crowding3[:,1]+fpr_crowding3[:,2], fpr_crowding3[:,1]-fpr_crowding3[:,2], alpha=0.4)
ax.fill_between(egfrd_crowding3[:,0]*1e6, egfrd_crowding3[:,1]+egfrd_crowding3[:,2], egfrd_crowding3[:,1]-egfrd_crowding3[:,2], alpha=0.4)
plt.plot([], [], ' ', label="Fit")
ax.plot(fpr_crowding3[:,0]*1e6, fpr_fit, linestyle=linestyles['dashed'], label = 'FPR', color='blue')
ax.plot(egfrd_crowding3[:,0]*1e6, egfrd_fit, linestyle=linestyles['densely dotted'], label = 'eGFRD', color = 'red')
ax.text(4, 50, r'$\phi$ = 0.25', fontsize = 18)

ax.set_xlim(0, 12)
ax.set_ylim(1e-1, 1e2)
ax.set_yscale('log')
ax.legend(loc = 0, labelspacing = 0.3)
plt.xlabel(r'time [$\mu s$]');
plt.ylabel(r'A(t)');

#plt.savefig("crowding_C25.svg",bbox_inches='tight', dpi = 400)
#plt.savefig("crowding_C25.pdf",bbox_inches='tight', dpi = 400)