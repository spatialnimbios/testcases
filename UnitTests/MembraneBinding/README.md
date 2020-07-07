# Membrane binding (3D -> 2D)
Bimolecular association. This test examines a volume molecule irreversibly binding to a surface molecule. This case is important to determine whether the method accurately achieves the proper kinetics and equilibrium. Binding to the membrane is via specific molecules on the surface, not just as an adsorption reaction at the surface. 

Molecules in solution can bind to molecules that are restricted to the 2D membrane surface, such as lipids or proteins bound to the membrane. In solution and on the membrane, molecules diffuse. The bimolecular association involves a 3D search of the solution molecule for a partner on the membrane. Thus, the K_D has solution units (i.e. uM). The equilibrium is thus the same as if both molecules were in solution, where concentrations of membrane bound molecules is measured via copy numbers/Volume.  The kinetics, however, are affected by the spatial localization of the membrane bound molecules.


# Species and Diffusion Coefficients:
| specie | Dim. | D (um^2/s) |
| --- | --- | --- |
| A | 3D | 30    |
| B | 2D |  1    |
| C | 2D | 0.97  |

# Geometry:
Rectangular Prism
Volume - 1 um^3
Surface Area - 4.84 um^2
X,Y Side Length - 2.2 um
Z Side Length - 0.207 um

# Initial Conditions (Species, Concentration, Number of Molecules):
A       1 uM                    602 molecules
B       6045 molecules.um^2     29,258 molecules

# Reaction (Equation, Kf, Kr):
A + B <-> C   
| kon (s^-1uM^-1)| koff (s^-1)| k_a3D (nm^3/us) | k_b, NERDSS (s^-1) | sigma (nm) |
| --- | --- | --- | --- | ---
| 84.4 | 70.085 | 500 | 250 | 1 |


K_D=0.83uM

Aeq= 10.3 copies. or 0.017uM
Ceq=591.7 copies, or 0.983uM



# Simulation parameters

dt=1e-7s (NERDSS)

# Rate Definitions for Single Particle Methods
In both FPR and MCell, the macroscopic on rate for 3D+2D particle interactions must be multiplied by two to reach the proper equilibrium relative to mass-action. This is because the flux into the membrane bound particles only happens from the top half of the spherical particles, resulting in only half the total expected flux. FPR performs this adjustment internally, so the user does not have to be aware of this factor of two! MCell does not perform it internally: the user must input twice the rate to recover the proper equilibrium and/or kinetics.  

For NERDSS simulations, the datapoints were only saved every 10us, so we reran 10 trajectories for 10us only to store points every 0.1us. 

# RESULTS

For this diffusion-limited reaction with very high lipid concentrations, there is a substantially faster kinetics for the non-spatial simulations. This is because with spatial resolution, the smallish number of A molecules has to diffuse to the surface before encoutering one of the many lipids. In the non-spatial simulations, the lipid molecules are homogenoeusly distributed in the single volume.




