# Circadian Clock Oscillator / coupled gene expression
Original model published in:
Vilar, J. M.G. et al, Mechanisms of noise-resistance in genetic oscillators. PNAS, 99:5988-5992 (2002)

# System Dimensions  
Sphere  
R = 1 um  
V = 4.19 um3  

Box (in NERDSS)  
L = 1.612 um  
V = 4.19 um3

# Copy Numbers  
mRNA_R: 0  
A: 0  
R: 0  
PrmA: 0.000397 uM = 1 molec  
PrmR: 0.000397 uM = 1 molec  
C: 0  
PrmA_bound: 0  
PrmR_bound: 0  
mRNA_A:0   

# Diffusion Coefficients [µm²/s]  
mRNA_R: 10  
A: 10  
R: 10  
PrmA: 10  
PrmR: 10  
AR: 10  
PrmA_bound: 10  
PrmR_bound: 10  
mRNA_A: 10  

# Reactions
				
| Reactions | k_on | k_a, NERDSS | k_off | k_b, NERDSS |  sigma (nm) |
| --- | --- | --- | --- | --- | --- |
| A + R -> AR  | 1204 uM-1s-1 | 356262.9 nm3/us | - |  -|  8 |
| PrmA -> PrmA + mRNA_A | 50 s-1 | 50 s-1 | - | - |  - |
| PrmA_bound -> PrmA_bound + mRNA_A | 500 s-1 | 500 s-1 | - | - | - |  
| PrmR -> PrmR + mRNA_R | 0.01 s-1 | 0.01 s-1 | - | - |  - |
| PrmR_bound -> PrmR_bound + mRNA_R | 50 s-1 | 50 s-1 | - | - | - |  
| PrmA + A <-> PrmA_bound | 602 uM-1s-1 | 4888.6 nm3/us | 50 s-1 | 244.5 s-1 |  5 |
| PrmR + A <-> PrmR_bound | 602 uM-1s-1 | 4888.6 nm3/us | 100 s-1 | 489.02 s-1 |  5 |
| mRNA_A -> mRNA_A + A | 50 s-1 | 50 s-1 | - | - |  - |
| mRNA_R -> mRNA_R + R | 5 s-1 | 5 s-1 | - | - |  - |
| mRNA_A -> NULL | 10 s-1 | 10 s-1 | - | - |  - |
| mRNA_R -> NULL | 0.5 s-1 | 0.5 s-1 | - | - |  - |
| A -> NULL | 1 s-1 | 1 s-1 | - | - |  - |
| R -> NULL | 0.2 s-1 | 0.2 s-1 | - | - |  - |
| AR -> R | 1 s-1 | 1 s-1 | - | - |  - |


# Model Modifications
# Slower R decay
In this model, one modification is made:
For reaction R -> NULL, the rate is dropped from 0.2 s^-1 to 0.05 s^-1,
causing oscillations to cease in the deterministic models.

# Localized and Immobilized Gene Promoters
In spatial models, we created a new model that localized the PrmA and PrmR at the cell center.
For the PDE, this meant that they were uniformly distributed in a sphere of radius R=0.1um, at a concentration of 0.3964uM.
Hence still a single molecule of each PrmA and PrmR. 
The diffusion coefficients of Promoters (bound and unbound) in these localized models was always set to D_PRMA=0 and D_PRMR=0.


For all variations to the model, including changes to D and localization of the Prm molecules, see:
NERDSS gene_expression/ClockModel_NerdssParameters.xlsx

Note: the D_z component of promoters in NERDSS is set to 1E-8 rather than exactly zero, otherwise it is interpreted as bound to the surface. 

# Time-step considerations
For the single-particle simulations, the density of reactants limited the time-step to ~10us. However, the unimolecular reactions had such high rates that they also placed constraints on the time-step, particularly for slow Diffusion (Dtot=DA+DB). In NERDSS simulations, unimolecular reactions are evaluated as a population, so of N molecules that can react according to rate k1, m events are chosen, which is significantly more accurate than looping over all N molecules individually, particularly for large time-steps. However, the promoter unbinding in this model (rxn 6 and 7) has only N=1. For large time-steps then, the average number of events that occur is less than the theoretical value. 
Error for N=1 can be quantified via avg_m_sim / avg_m_theory =exp(-kdeltat). As exp(-kdeltat)->1, the error goes to zero. 

For original model, used dt=1 x10^-5 s.
For localized promoters, used dt=5 x10^-7 s. 

