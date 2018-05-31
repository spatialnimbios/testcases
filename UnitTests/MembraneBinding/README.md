# Membrane binding
Bimolecular association. This test examines a volume molecule irreversibly binding to a surface molecule. This case is important to determine whether the method accurately achieves the proper kinetics and equilibrium. Binding to the membrane is via specific molecules on the surface, not just as an adsorption reaction at the surface. 

Molecules in solution can bind to molecules that are restricted to the 2D membrane surface, such as lipids or proteins bound to the membrane. In solution and on the membrane, molecules diffuse. The bimolecular association involves a 3D search of the solution molecule for a partner on the membrane. Thus, the K_D has solution units (i.e. uM). The equilibrium is thus the same as if both molecules were in solution, where concentrations of membrane bound molecules is measured via copy numbers/Volume.  The kinetics, however, are affected by the spatial localization of the membrane bound molecules.

# Irreversible Diffusion-limited Reaction


# Species and Diffusion Coefficients:
A (3D)      30 nm^2.us-1
B (2D)      1 nm^2.us-1
C (3D)      0.97 nm^2.us-1

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


# RESULTS

For this diffusion-limited reaction with very high lipid concentrations, there is a substantially faster kinetics for the non-spatial simulations. This is because with spatial resolution, the smallish number of A molecules has to diffuse to the surface before encoutering one of the many lipids. In the non-spatial simulations, the lipid molecules are homogenoeusly distributed in the single volume.


# Reversible, rate-limited binding

eversible Membrane Recruitment (Figure 9b)
This test case examines a volume molecule reversibly binding to a surface molecule. Slightly more complicated than the irreversible case, the reversib\
le recruitment test case determines whether the dissociation reaction properly releases the volume molecule into the correct compartment. In addition,\
 this test case assess whether the method uses the correct effective reaction rates between volume and surface molecules.

# Species and Diffusion Coefficients:
A (3D)      10 nm^2.us-1
B (2D)      1 nm^2.us-1
C (3D)      0.91 nm^2.us-1

# Geometry:
Cube
Volume - 0.064 um^3
Surface Area - 0.16 um^2
Side Length - 0.4 um

# Initial Conditions (Species, Concentration, Number of Molecules):
A       25.945 uM               1000 molecules
B       6250 molecules.um^2     1000 molecules



# Reaction (Equation, Kf, Kr):
A + B <-> C   0.30 s-1.uM-1    1 s-1

# Sim parameters
Time Step: 1e-6 s
Length of Simulation: 10 s
Number of Seeds (MCell): 1


# Results:
Aeq=299.9 molecules or 7.781uM
Ceq=700.1 molecules


