# Coupled Expression Dynamics

# System Dimensions  
Sphere  
R = 1 um  
V = 4.19 um3  

Box (in MCell)  
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
C: 10  
PrmA_bound: 10  
PrmR_bound: 10  
mRNA_A: 10  

# Reactions
				
| Reactions | k_on | k_a, FPR | k_off | k_off, FPR |  
| --- | --- | --- | --- |  
| A + R -> AR  | 1204 uM-1s-1 | 356262.9 nm3/us | - |  -|  
| PrmA -> PrmA + mRNA_A | 50 s-1 | 50 s-1 | - | - |  
| PrmA_bound -> PrmA_bound + mRNA_A | 500 s-1 | 500 s-1 | - | - |  
| PrmR -> PrmR + mRNA_R | 0.01 s-1 | 0.01 s-1 | - | - |  
| PrmR_bound -> PrmR_bound + mRNA_R | 50 s-1 | 50 s-1 | - | - |  
| PrmA + A <-> PrmA_bound | 602 uM-1s-1 | 4888.6 nm3/us | 50 s-1 | 244.5 s-1 |  
| PrmR + A <-> PrmR_bound | 602 uM-1s-1 | 4888.6 nm3/us | 100 s-1 | 489.02 s-1 |  
| mRNA_A -> mRNA_A + A | 50 s-1 | 50 s-1 | - | - |  
| mRNA_R -> mRNA_R + R | 5 s-1 | 5 s-1 | - | - |  
| mRNA_A -> NULL | 10 s-1 | 10 s-1 | - | - |  
| mRNA_R -> NULL | 0.5 s-1 | 0.5 s-1 | - | - |  
| A -> NULL | 1 s-1 | 1 s-1 | - | - |  
| R -> NULL | 0.2 s-1 | 0.2 s-1 | - | - |  
| AR -> R | 1 s-1 | 1 s-1 | - | - |  
  