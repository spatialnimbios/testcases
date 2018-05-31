# Irreversible Binding 2D

This test case examines the irreversible interaction between two distinct species. The 2D irreversible binding test case assesses whether the simulation method depicts the proper kinetics for an irreversible reaction in two-dimensions.        

<pre>
Species and Diffusion Coefficients:
A       1 nm^2.us-1
B       1 nm^2.us-1
C       0.5 nm^2.us-1

Initial Conditions (Species, Number of Molecules):
A       1000 molecules
B       1000 molecules
C       0 molecules

Reaction (Equation, Kf, Kr):
A + B -> C   k_on=4.2495 um^2.s-1. k_off=0

For FPR intrinsic k_a=100 um^2.s-1

Equation for converting between the macroscopic k_on2D and microscopic k_a2D is in Yogurtcu et al, 2015. Attached in matlab kon2D_value.m

Geometry:
Surface Area= 1um^2


MCell Parameters
Geometry:
Plane
Surface Area - 1 um^2
Side Length - 1 um

Time Step: 1e-6 s
Length of Simulation: 1 s
Number of Seeds (MCell): 10


VCell Parameters
Geometry:
Spherical Box
Cell Effective Radius - 0.080 um

Time Step: 1e-7 s
End Time: 1 s
Number of Trajectories Averaged: 10

FPR Time step: 1e-7s

MORE RATE-LIMITED REACTION
A + B -> C   k_on=0.816 um^2.s-1. k_off=0

For FPR intrinsic k_a=1 um^2.s-1

RESULTS:
Smoldyn is far off, and a newer version of the software needs to be checked. 
MCell is also off for the diffusion-controlled system (higher k_on).

References: Yogurtcu, O.N. and Johnson, M.E. Theory of bi-molecular association dynamics in 2D for accurate model and experimental parameterization of binding rates, J Chem Phys. 143:084117 (2015).

</pre>
