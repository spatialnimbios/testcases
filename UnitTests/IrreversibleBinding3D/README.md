# Bimolecular association in 3D (Irreversible)
A+A->C

While simple, these types of reactions require both a diffusional search and a reactive event, and they provide the building blocks for the majority of more complex models. Their accuracy is critical in determining the accuracy of more complex models. They can be solved essentially ‘exactly’ for the full time-dependent numerical solution, here using well-mixed, or uniform initial concentrations. 


As expected for all model parameters, there is no difference between the ODE, PDE, or stochastic Gillespie solutions, because these methods use the same macroscopic rates for association, and reactants were *uniformly distributed* in the volume. 

For the single particle RD methods, there are theoretical results we expect for bimolecular association models, independent of the algorithm. In 3D, we expect the kinetics of association beyond short time-scales to be the same for all methods because theoretically, the macroscopic rate equation is the correct description of the approach to equilibrium (Mattis, Tauber) (exceptions for when A0=B0 (Tauber) can be only effectively observed with high numerical precision on statistics (Johnson and Yogurtcu)). At short-times, the kinetics of association is slightly faster for single-particle RD when microscopic rates control binding upon collision between particles, because even with uniform initial conditions, some pairs of particles will be closer together than others. Practically, however, this faster kinetics is only visible when binding is diffusion-controlled, meaning nearly all collisions between reactants result in a binding event. 

# SPECIES
1. A          D=50nm^2/us 

# Reactions
Diffusion-Limited: 
A+A->C  k_f=756.635 uM-1.s-1. k_r=0

# Initial Conditions
A: Uniform, 16.6mM.   2000 copies 

# Geometry
V=2E-4 um^3.
Sphere with R=0.03628um or box with L=0.05849um

# Simulation parameters
Due to the relatively high density (16mM), a small time-step needs to be taken. Same dt used for all single-particle methods.

time-step: 1ns


# Results
For this diffusion controlled reaction, the single-particle simulations should have faster initial kinetics compared to the macroscopic rate methods (ODE, PDE, SSA).

# Rate LIMITED Bimolecular association in 3D (Irreversible)
A+A->C

If the reaction is rate-limited, or only weakly-diffusion influenced (smaller on rate), then over all time-scales, the results will converge, including all single-particle methods.

# Rate Limited Reaction
A+A->C k_f=1 uM-1.s-1. k_r=0
# Rate limited Initial Conditions
A: Uniform, 10uM. 2000 copies
# Geometry
V=0.3321 um^3
Box with L=0.6925um
Sphere with R=0.4296um

# Simulation Parameters
For this more standard physiologic concentration (10uM), a larger time-step can be used.

time-step: 0.1us


# Results
All simulations produce same kinetics.
