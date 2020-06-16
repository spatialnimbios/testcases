# Coupled Expression Dynamics

# System Dimensions  
Sphere  
R = 1 um  
V = 4.19 um^3  

Box (in MCell)  
L = 1.612 um
V = 4.19 um^3  

# Copy Numbers  
mRNA_R: 0  
A: 0  
R: 0  
PrmA: 0.000397 uM = 1  
PrmR: 0.000397 uM = 1  
AR: 0  
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
				
| Reactions | k_on | k_off |  
| --- | --- | --- |  
| A + R -> AR  | 1204 uM-1s-1 | - |  
| PrmA -> PrmA + mRNA_A | 50 s-1 | - |  
| PrmA_bound -> PrmA_bound + mRNA_A | 500 s-1 | - |  
| PrmR -> PrmR + mRNA_R | 0.01 s-1 | - |  
| PrmR_bound -> PrmR_bound + mRNA_R | 50 s-1 | - |  
| PrmA + A <-> PrmA_bound | 602 uM-1s-1 | 50 s-1 |  
| PrmR + A <-> PrmR_bound | 602 uM-1s-1 | 100 s-1 |  
| mRNA_A -> mRNA_A + A | 50 s-1 | - |  
| mRNA_R -> mRNA_R + R | 5 s-1 | - |  
| mRNA_A -> NULL | 10 s-1 | - |  
| mRNA_R -> NULL | 0.5 s-1 | - |  
| A -> NULL | 1 s-1 | - |
| R -> NULL | 0.2 s-1 | - |
| AR -> R | 1 s-1 | - |
  
