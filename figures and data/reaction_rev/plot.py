# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 17:01:00 2020

@author: phenning
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io as sio

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
default_y = 6.5*1.4

plt.gcf().set_size_inches(default_x, default_y)
plt.rcParams.update({'font.size': 12})
#%%
########## load data ##########

## load 3D reversible ##
ode1 = sio.loadmat('ReversibleBinding3D/Ka1000/ODE.mat')
ode1 = ode1["det1D_1000"]

pde1 = sio.loadmat('ReversibleBinding3D/Ka1000/PDE.mat')
pde1 = pde1["det3D_1000"]

ssa1 = sio.loadmat('ReversibleBinding3D/Ka1000/gillespie_1000.mat')
ssa1 = ssa1["gillespie_1000"]
time_ssa1 = np.arange(0, 2.87, 1e-5)
ssa_time_tmp = ssa1[:,0]
ssa_ave1 = time_ssa1*0
for run in range(10):
    ssa_time_tmp = ssa1[:,run*2]
    for (time, i) in zip(time_ssa1, range(len(time_ssa1))):
        ssa_ave1[i] += ssa1[np.argmax(ssa_time_tmp > time)-1, run*2+1] 
ssa_ave1 /=10
del ssa1, ssa_time_tmp, time, run, i


smoldyn1 = sio.loadmat('ReversibleBinding3D/Ka1000/Smoldyn.mat')
smoldyn1 = smoldyn1["smoldyn_1000"]

fpr1 = sio.loadmat('ReversibleBinding3D/Ka1000/fpr_1000.mat')
fpr1 = fpr1["fpr_1000"]

mcell1 = np.loadtxt('ReversibleBinding3D/Ka1000/MCELL_A.Cube.dat')

theory1 = np.loadtxt('ReversibleBinding3D/Ka1000/AnalyticalSolutionToRateEqn.txt', skiprows = 1)

## load 2D reversible ##
ode2 = sio.loadmat('ReversibleBinding2D/GRAPH_AND_DATA/det1D_1.mat')
ode2 = ode2["det1D_1"]

pde2 = sio.loadmat('ReversibleBinding2D/GRAPH_AND_DATA/det3D_1.mat')
pde2 = pde2["det3D_1"]

ssa2 = np.loadtxt('ReversibleBinding2D/GRAPH_AND_DATA/gillespie_ka1_10trajavg.dat')

smoldyn2 = np.loadtxt('ReversibleBinding2D/GRAPH_AND_DATA/smoldyn_ka1_10trajavg.dat')

fpr2 = np.loadtxt('ReversibleBinding2D/GRAPH_AND_DATA/fpr_1_traj50.dat')

mcell2 = sio.loadmat('ReversibleBinding2D/GRAPH_AND_DATA/mcell_1.mat')
mcell2 = mcell2["mcell_1"]

theory2 = sio.loadmat('ReversibleBinding2D/GRAPH_AND_DATA/theory_1.mat')
theory2 = theory2["theory_1"]

## load 2D-3D reversible ##
ode3 = sio.loadmat('ReversibleMembraneRecruitment/GRAPH_AND_DATA/det1D.mat')
ode3 = ode3["det1D"]

pde3 = sio.loadmat('ReversibleMembraneRecruitment/GRAPH_AND_DATA/det3D.mat')
pde3 = pde3["det3D"]

# calc ave
ssa3 = sio.loadmat('ReversibleMembraneRecruitment/GRAPH_AND_DATA/gillespie.mat')
ssa3 = ssa3["gillespie"]
time_ssa3 = np.arange(0, 4.8, 0.01)
ssa_time_tmp = ssa3[:,0]
ssa_ave3 = time_ssa3*0
for run in range(10):
    ssa_time_tmp = ssa3[:,run*2]
    for (time, i) in zip(time_ssa3, range(len(time_ssa3))):
        ssa_ave3[i] += ssa3[np.argmax(ssa_time_tmp > time)-1, run*2+1] 
ssa_ave3 /=10
del ssa3, ssa_time_tmp, time, run, i

#calc ave
smoldyn3 = sio.loadmat('ReversibleMembraneRecruitment/GRAPH_AND_DATA/smoldyn.mat')
smoldyn3 = smoldyn3["smoldyn"]
smoldyn_time3 = smoldyn3[:,0]
smoldyn_ave = np.average(smoldyn3[:, 1::2], axis=1)
del smoldyn3

fpr3 = sio.loadmat('ReversibleMembraneRecruitment/GRAPH_AND_DATA/fpr.mat')
fpr3 = fpr3["fpr"]

mcell3 = sio.loadmat('ReversibleMembraneRecruitment/GRAPH_AND_DATA/mcell.mat')
mcell3 = mcell3["mcell"]

#%%

########## Plot reversible ##########
## plot 3D reversible ##
fig, ax = plt.subplots(3)
ax[0].plot(ode1[:,0], ode1[:,1], '--', label='ODE')
ax[0].plot(pde1[:,0], pde1[:,1], '-.', label = 'PDE')
ax[0].plot(time_ssa1[:], ssa_ave1[:], ':', label='Gillespie')
ax[0].plot(smoldyn1[:,0], smoldyn1[:,1], linestyle=linestyles['densely dashed'], label='Smoldyn')
ax[0].plot(fpr1[:,0]*10**-6, fpr1[:,1], label='FPR')
ax[0].plot(mcell1[:,0], mcell1[:,1], linestyle=linestyles['dashdotdotted'], label= 'MCell')
ax[0].plot(theory1[:,0], theory1[:,1], '--', label='theory', color = 'black')
ax[0].set_xscale('log')
ax[0].set_xlim(10**-6, 5*1e0)
ax[0].set_ylim(0, 100000)
#ax[0].legend(loc=1)
ax[0].ticklabel_format(axis='y', style='sci', scilimits=(4,4), useOffset=None, useLocale=None, useMathText=True)
ax[0].text(1.5*1e-6, 88000,r'$A + B \leftrightarrow C, 3D$')

axins = ax[0].inset_axes([0.57, 0.5, 0.40, 0.47])
axins.set_xlim(0.3, 1.0)
axins.set_ylim(400, 650)
ax[0].indicate_inset_zoom(axins)
axins.plot(ode1[:,0], ode1[:,1], '--', label='ODE' )
axins.plot(pde1[:,0], pde1[:,1], '-.', label = 'PDE')
axins.plot(time_ssa1[:], ssa_ave1[:], ':', label='Gillespie')
axins.plot(smoldyn1[:,0], smoldyn1[:,1], linestyle=linestyles['densely dashed'], label='Smoldyn')
axins.plot(fpr1[:,0]*10**-6, fpr1[:,1], label='FPR')
axins.plot(mcell1[:,0], mcell1[:,1], linestyle=linestyles['dashdotdotted'], label= 'MCell')
axins.plot(theory1[:,0], theory1[:,1], '--', label='theory', color = 'black')
axins.set_xscale('log')
axins.set_xticks(np.arange(0.3, 1.1, 0.1))
axins.set_xticks([], True)
axins.set_xticklabels(['','', r'$5\cdot 10^{-1}$','' ,'','','', r'$10^0$'])

## plot 2D reversible ##
ax[1].plot(ode2[:,0], ode2[:,1], '--', label='ODE')
ax[1].plot(pde2[:,0], pde2[:,1], '-.', label = 'PDE')
ax[1].plot(ssa2[:,0]*10**-6, ssa2[:,1], ':', label='Gillespie')
ax[1].plot(smoldyn2[:,0], smoldyn2[:,1], linestyle=linestyles['densely dashed'], label='Smoldyn')
ax[1].plot(fpr2[:,0]*10**-6, fpr2[:,1], label='FPR')
ax[1].plot(mcell2[:,0], mcell2[:,1], linestyle=linestyles['dashdotdotted'], label= 'MCell')
ax[1].plot(theory2[:,0]*1e-6, theory2[:,1], '--', label='theory', color = 'black')
ax[1].set_xscale('log')
ax[1].set_xlim(1e-6, 5*1e0)
ax[1].legend(loc=1, labelspacing = 0.3)
ax[1].ticklabel_format(axis='y', style='plain', scilimits=(4,4), useOffset=None, useLocale=None, useMathText=None)
ax[1].set_ylabel('A(t)');
ax[1].text(1.5*1e-6, 880, r'$A + B \leftrightarrow C, 2D$');

## plot 2D-3D reversible ##
ax[2].plot(ode3[:,0], ode3[:,1], '--', label='ODE')
ax[2].plot(pde3[1:,0], pde3[1:,1], '-.', label = 'PDE')
ax[2].plot(time_ssa3[1:], ssa_ave3[1:], ':', label='Gillespie')
ax[2].plot(smoldyn_time3[1:], smoldyn_ave[1:], linestyle=linestyles['densely dashed'], label='Smoldyn')
ax[2].plot(fpr3[0:-1,0], fpr3[0:-1,1], label='FPR')
ax[2].plot(mcell3[:,0], mcell3[:,1], linestyle=linestyles['dashdotdotted'], label= 'MCell')
ax[2].set_xscale('log')
ax[2].set_xlim(1e-6,5*1e0)
#ax[2].legend(loc=1)
ax[2].ticklabel_format(axis='y', style='plain', scilimits=(4,4), useOffset=None, useLocale=None, useMathText=None)
ax[2].set_xlabel('time [s]');
ax[2].text(1.5*1e-6, 880, r'$A + B \leftrightarrow C, 3D-2D$');

axins = ax[2].inset_axes([0.1, 0.15, 0.55, 0.45])
axins.set_xlim(0.5, 3.0)
axins.set_ylim(280, 340)
ax[2].indicate_inset_zoom(axins)
axins.plot(ode3[:,0], ode3[:,1], '--', label='ODE' )
axins.plot(pde3[:,0], pde3[:,1], '-.', label = 'PDE')
axins.plot(time_ssa3[1:], ssa_ave3[1:], ':', label='Gillespie')
axins.plot(smoldyn_time3[1:], smoldyn_ave[1:], linestyle=linestyles['densely dashed'], label='Smoldyn')
axins.plot(fpr3[0:-1,0], fpr3[0:-1,1], label='FPR')
axins.plot(mcell3[:,0], mcell3[:,1], linestyle=linestyles['dashdotdotted'], label= 'MCell')
axins.set_xscale('log')
axins.set_xticks(np.concatenate([np.arange(0.5, 1, 0.1),np.arange(1, 4, 1)]))
axins.set_xticks([], True)
axins.set_xticklabels([r'$5\cdot 10^{-1}$','','','','', r'$10^{0}$','' , r'$3\cdot 10^{0}$'])

plt.gcf().set_size_inches(default_x, default_y)

plt.savefig("PAPER_rev_reactions.svg",bbox_inches='tight', dpi = 400)
plt.savefig("PAPER_rev_reactions.pdf",bbox_inches='tight', dpi = 400)
















