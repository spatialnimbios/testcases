# Bimolecular Association, Reversible A+B<->C

This reaction build off of the irreversible unit test by adding the unimolecular dissociation reaction C->A+B.
This is a diffusion-controlled/influenced reaction. However, because the concentrations are not very high, during the short-time kinetics where single-particle reactions occur faster, the differences between the kinetics should be nearly imperceptible.  


# Species
1. A. D=1um^2/s
2. B  D=1um^2/s
3. C  D=1um^2/s

# Reactions
1. A+B<->C   k_on=14.764 uM-1.s-1.   k_off=0.0245 s-1

K_D=1.6605 nM

For FPR, intrinsic k_a=1000nm^3/us, intrinsic k_b=1 s-1

# Initial concentrations
A. 52uM     100,000 copies
B. 52uM     100,000 copies
C. 0uM

# Geometry
V=3.2 um^2
Sphere has R=0.91415 um
Box has L=1.473613 um

# Simulation Parameters
Time-step for single-particle methods of either 1us or 0.5us.

# Results
The kinetics of all methods should be nearly the same, as the particles are far enough apart at the initial concentration that rapid association events for single-particle methods are not common.

Equilibrium values of all simulations should be exact, where
A_eq is the quadratic root, A_eq= 1/2* [A0-B0+KD + sqrt( (A0-B0+KD)^2+4A0KD ) ]
A_eq=0.293uM.
Due to precision differences in specified copy numbers or Volume, simulated value should match exact inputs.

