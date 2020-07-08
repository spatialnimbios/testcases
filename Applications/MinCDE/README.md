# Min CDE  
adapted form Huang et al. PNAS 2006  

# System Dimensions  
Cylinder:  
r = 0.5 um  
h = 4 um  

# Initial Copy Numbers and Diffusion coefficients
In PDE, MinD-ATP and MinE are well-mixed in the solution volume.
In Smoldyn, MinE is well-mixed in the solution volume. MinD-ATP was split between 3D and 2D evenly.

| specie | conc (uM) | copy number | D (um^2/s) | D_Smoldyn |
| --- | --- | --- | --- | --- |
| MinD-ATP | 2.1143 | 4000 | 2.5 | 2.5 |
| MinD-ATP2D | 0.   | 0.   | 0 | 0.05 |
| MinE | 0.74 | 1400 | 2.5 | 2.5 |
| MinD-ADP | 0 | 0 | 2.5 | 2.5 |
| MinD-ATP.MinE2D | 0 | 0 | 0 | 0.05 |




# Reactions  
| Reactions | k | 
| --- | --- |
| MinD-ATP -> MinD-ATP2D | 0.025 um.s-1 |  
| MinD-ATP + MinD-ATP2D -> 2MinD-ATP2D | 0.903 s-1.uM-1 |  
| MinD-ATP + MinD-ATP.MinE2D -> MinD-ATP2D + MinD-ATP.MinE2D | 0.903 s-1.uM-1 |  
| MinE + MinD-ATP2D -> MinD-ATP.MinE2D | 56.0 s-1.uM-1 |  
| MinD-ATP.MinE2D -> MinD-ADP + MinE | 0.7 s-1 |  
| MinD-ADP -> MinD-ATP | 1 s-1 |  

# Notes:
1. *Huang et al note the E is only active as a homodimer, so observed copy numbers in a cell should be halved to capture the copy numbers of active species. Hence they use 350/um rather than 700/um.  
2. MinD-ADP, MinD-ATP, and MinE are all cytosolic.  
3. MinD-ATP2D and MinD-ATP.MinE2D are both on the membrane.  
