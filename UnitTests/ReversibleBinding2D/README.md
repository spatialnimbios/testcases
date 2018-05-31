# Bimolecular Association 2D A+B<->C 

Bimolecular association in 2D. Equilibrium value should be correct for all methods.

# Species
A   1000 molecule.  D: 1um^2/s
B   1000 molecule.  D: 1um^2/s
C   0 molecule.  D: 0.5um^2/s

# Reactions 
A+B <->C    k_on=0.816 um^2/s, k_off=0.816 s-1

Equilibrium KD=1 um^-2.

For FPR, k_a=1 um^2/s and k_b=1 s-1.

# Geometry

Surface Area=1 um^2.

For Virtual cell, set the Cell to be a sphere with R=0.282um. The PM will have the correct SA of 1um^2.

# Simulation Parameters
Smoldyn and FPR used 1e-7 s time-step
MCell used 1e-6s time-step.

# RESULTS

Should recover A_eq=31.1267 copies. Takes ~1s to reach equilibrium.

