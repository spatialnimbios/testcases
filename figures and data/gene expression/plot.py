# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 15:43:39 2020

@author: phenning
"""

import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict
import scipy.io as sio

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

########## Plot gene expression ##########

gene_data = sio.loadmat('Original/MCellData/matlab.mat')
time = gene_data["excelt_osci"]
ode_a = gene_data["ode_osci_a"]
ode_r = gene_data["ode_osci_r"]
smoldyn_a = gene_data["smol_oci_a"]
smoldyn_r = gene_data["smol_osci_r"]
mcell_r = gene_data["mcelldat_r"]


fig, ax = plt.subplots()
ax.plot(time, ode_a)
ax.plot(time, ode_r)

#fig, ax = plt.subplots()
ax.plot(time, smoldyn_a)
ax.plot(time, smoldyn_r)

fig, ax = plt.subplots()
ax.plot(mcell_r)
