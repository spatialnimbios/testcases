# Membrane binding
Bimolecular association. This test examines a volume molecule irreversibly binding to a surface molecule. This case is important to determine whether the method accurately achieves the proper kinetics and equilibrium. Binding to the membrane is via specific molecules on the surface, not just as an adsorption reaction at the surface. 

Molecules in solution can bind to molecules that are restricted to the 2D membrane surface, such as lipids or proteins bound to the membrane. In solution and on the membrane, molecules diffuse. The bimolecular association involves a 3D search of the solution molecule for a partner on the membrane. Thus, the K_D has solution units (i.e. uM). The equilibrium is thus the same as if both molecules were in solution, where concentrations of membrane bound molecules is measured via copy numbers/Volume.  The kinetics, however, are affected by the spatial localization of the membrane bound molecules.

# Irreversible Diffusion-limited Reaction


# Species and Diffusion Coefficients:
| A | (3D) | 30 nm^2.us-1   |
| B | (2D) |  1 nm^2.us-1   |
| C | (2D) | 0.97 nm^2.us-1 |

# Geometry:
Rectangular Prism
Volume - 1 um^3
Surface Area - 4.84 um^2
X,Y Side Length - 2.2 um
Z Side Length - 0.207 um

# Initial Conditions (Species, Concentration, Number of Molecules):
A       1 uM                    602 molecules
B       6045 molecules.um^2     29,330 molecules

# Reaction (Equation, Kf, Kr):
A + B -> C   84.41 s-1.uM-1    0 s-1





# Simulation parameters

Time Step: 1e-6 s
Length of Simulation: 1 s
Number of Seeds (MCell): 10

# Rate Definitions for Single Particle Methods
In both FPR and MCell, the macroscopic on rate for 3D+2D particle interactions must be multiplied by two to reach the proper equilibrium relative to mass-action. This is because the flux into the membrane bound particles only happens from the top half of the spherical particles, resulting in only half the total expected flux. FPR performs this adjustment internally, so the user does not have to be aware of this factor of two! MCell does not perform it internally: the user must input twice the rate to recover the proper equilibrium and/or kinetics.  

For NERDSS simulations, the datapoints were only saved every 10us, so we reran 10 trajectories for 10us only to store points every 0.1us. 

# RESULTS

For this diffusion-limited reaction with very high lipid concentrations, there is a substantially faster kinetics for the non-spatial simulations. This is because with spatial resolution, the smallish number of A molecules has to diffuse to the surface before encoutering one of the many lipids. In the non-spatial simulations, the lipid molecules are homogenoeusly distributed in the single volume.




