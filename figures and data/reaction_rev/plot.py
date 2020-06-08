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

theory1 = np.loadtxt('ReversibleBinding3D/Ka1000/AnalyticalSolutionToRateEqn.txt', skiprows = 1)

## load 2D reversible ##
ode2 = np.loadtxt('ReversibleBinding2D/ode_rev2d.txt')

pde2 = np.loadtxt('ReversibleBinding2D/pde_rev2d.txt')

ssa2 = np.loadtxt('ReversibleBinding2D/gillespie_mean_5trajs_rev2d.txt')

smoldyn2 = np.loadtxt('ReversibleBinding2D/smoldyn_mean2traj_rev2d.txt')

fpr2 = np.loadtxt('ReversibleBinding2D/FPR_shortAndLong_mean5traj_rev2d.txt', skiprows = 1)

theory2 = np.loadtxt('ReversibleBinding2D/Analytical_Rev2D_Aeq_RateEquationRiccati.txt', skiprows = 1)

## load 2D-3D reversible ##
ode3 = np.loadtxt('ReversibleMembraneRecruitment/ODE_rev3dto2d.txt')

pde3 = np.loadtxt('ReversibleMembraneRecruitment/PDE_rev3dto2d.txt')

ssa3 = np.loadtxt('ReversibleMembraneRecruitment/gillespie_mean5traj_rev3dto2d.txt', skiprows = 1)

smoldyn3 = np.loadtxt('ReversibleMembraneRecruitment/Smoldyn_Rev3Dto2D_start602_mean_sem_3traj1e-6.dat')

fpr3 = np.loadtxt('ReversibleMembraneRecruitment/FPRnerdss_avg10traj_ka500_kb250.txt', skiprows = 0)

#%%

########## Plot reversible ##########
## plot 3D reversible ##
fig, ax = plt.subplots(3)
ax[0].plot(ode1[:,0], ode1[:,1], '--', label='ODE', color = 'tab:blue')
ax[0].plot(pde1[:,0], pde1[:,1], '-.', label = 'PDE', color = 'tab:green')
ax[0].plot(fpr1[:,0]*10**-6, fpr1[:,1], linestyle=linestyles['densely dashdotdotted'], label='FPR', color = 'tab:red')
ax[0].plot(time_ssa1[:], ssa_ave1[:], ':', label='Gillespie', color = 'tab:purple')
ax[0].plot(smoldyn1[:,0], smoldyn1[:,1], linestyle=linestyles['densely dashed'], label='Smoldyn', color = 'tab:orange')
#ax[0].plot(theory1[:,0], theory1[:,1], '--', label='theory', color = 'black')
ax[0].set_xscale('log')
ax[0].set_xlim(10**-6, 5*1e0)
ax[0].set_ylim(0, 105000)
ax[0].ticklabel_format(axis='y', style='sci', scilimits=(4,4), useOffset=None, useLocale=None, useMathText=True)
ax[0].text(1.5*1e-6, 5000,r'$A + B \leftrightarrow C, 3D$')

axins = ax[0].inset_axes([0.57, 0.5, 0.40, 0.455])
axins.set_xlim(0.3, 2.0)
axins.set_ylim(530, 650)
ax[0].indicate_inset_zoom(axins)
axins.plot(ode1[:,0], ode1[:,1], '--', label='ODE', color = 'tab:blue')
axins.plot(pde1[:,0], pde1[:,1], '-.', label = 'PDE', color = 'tab:green')
axins.plot(fpr1[:,0]*10**-6, fpr1[:,1], linestyle=linestyles['densely dashdotdotted'], label='FPR', color = 'tab:red')
axins.plot(time_ssa1[:], ssa_ave1[:], ':', label='Gillespie', color = 'tab:purple')
axins.plot(smoldyn1[:,0], smoldyn1[:,1], linestyle=linestyles['densely dashed'], label='Smoldyn', color = 'tab:orange')
#axins.plot(theory1[:,0], theory1[:,1], '--', label='theory', color = 'black')
axins.set_xscale('log')
axins.set_xticks(np.concatenate([np.arange(0.3, 1.1, 0.1),[2]]))
axins.set_xticks([], True)
axins.set_xticklabels(['','', r'$5\cdot 10^{-1}$','' ,'','','', r'$10^0$'])

## plot 2D reversible ##
ax[1].plot(ode2[:,0], ode2[:,1], '--', label='ODE', color = 'tab:blue')
ax[1].plot(pde2[1:-1,0], pde2[1:-1,1], '-.', label = 'PDE', color = 'tab:green')
ax[1].plot(fpr2[1:-1,0], fpr2[1:-1,1], linestyle=linestyles['densely dashdotdotted'], label='FPR', color = 'tab:red')
ax[1].plot(ssa2[:,0], ssa2[:,1], ':', label='Gillespie', color = 'tab:purple')
ax[1].plot(smoldyn2[1:-1,0], smoldyn2[1:-1,1], linestyle=linestyles['densely dashed'], label='Smoldyn', color = 'tab:orange')
#ax[1].plot(theory2[:,0], theory2[:,1], '--', label='theory', color = 'black')
ax[1].set_xscale('log')
ax[1].set_xlim(1e-6, 5*1e0)
ax[1].legend(loc=1, labelspacing = 0.3)
ax[1].set_ylim(0, 1050)
ax[1].ticklabel_format(axis='y', style='plain', scilimits=(4,4), useOffset=None, useLocale=None, useMathText=None)
ax[1].set_ylabel('A(t)');
ax[1].text(1.5*1e-6, 50, r'$A + B \leftrightarrow C, 2D$');

## plot 2D-3D reversible ##
ax[2].plot(ode3[:,0], ode3[:,1], '--', label='ODE', color = 'tab:blue')
ax[2].plot(pde3[1:,0], pde3[1:,1], '-.', label = 'PDE', color = 'tab:green')
ax[2].plot(fpr3[:,0]*1e-6, fpr3[:,1], linestyle=linestyles['densely dashdotdotted'], label='FPR', color = 'tab:red')
ax[2].plot(ssa3[:,0], ssa3[:,1], ':', label='Gillespie', color = 'tab:purple')
ax[2].plot(smoldyn3[:,0], smoldyn3[:,1], linestyle=linestyles['densely dashed'], label='Smoldyn', color = 'tab:orange')
ax[2].set_xscale('log')
ax[2].set_xlim(1e-6,5*1e0)
ax[2].set_ylim(0, 630)
ax[2].ticklabel_format(axis='y', style='plain', scilimits=(4,4), useOffset=None, useLocale=None, useMathText=None)
ax[2].set_xlabel('time [s]');
ax[2].text(1.5*1e-6, 30, r'$A + B \leftrightarrow C, 3D-2D$');

axins = ax[2].inset_axes([0.56, 0.5, 0.40, 0.455])
axins.set_xlim(0.001, 0.1)
axins.set_ylim(0, 50)
ax[2].indicate_inset_zoom(axins)
axins.plot(ode3[:,0], ode3[:,1], '--', label='ODE', color = 'tab:blue')
axins.plot(pde3[:,0], pde3[:,1], '-.', label = 'PDE', color = 'tab:green')
axins.plot(fpr3[:,0]*1e-6, fpr3[:,1], linestyle=linestyles['densely dashdotdotted'], label='FPR', color = 'tab:red')
axins.plot(ssa3[:,0], ssa3[:,1], ':', label='Gillespie', color = 'tab:purple')
axins.plot(smoldyn3[:,0], smoldyn3[:,1], linestyle=linestyles['densely dashed'], label='Smoldyn', color = 'tab:orange')
axins.set_xscale('log')

plt.gcf().set_size_inches(default_x, default_y)

plt.savefig("PAPER_rev_reactions.svg",bbox_inches='tight', dpi = 400)
plt.savefig("PAPER_rev_reactions.pdf",bbox_inches='tight', dpi = 400)
plt.savefig("PAPER_rev_reactions.png",bbox_inches='tight', dpi = 400)
















