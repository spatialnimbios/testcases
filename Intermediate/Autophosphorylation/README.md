# Autophosphorylation model

# System Dimensions  
Cube:  
L = 0.14422 um  
V = 0.003 um^3  

# Copy Numbers  
A: 103  
Ap: 5  
P: 9  

# Diffusion Coefficients [µm²/s]  
A: 100  
Ap: 100  
P: 100 

# Reactions
				
| Reactions | k_on| k_a, FPR |  sigma (nm)
| --- | --- | --- |  --- | 
| A -> Ap | 21.2 s-1 | same |  - |
| A + Ap -> A_Ap | 10 uM-1s-1 | 16.7 nm3/us | 1 |  
| A_Ap -> Ap + Ap | 200 1/s | same |  - |
| Ap + P -> Ap_P | 800 uM-1s-1 | 2820 nm3/us | 1 |  
| Ap_P -> A + P | 539 1/s | same | - |

# Solvers

ODE and SSA were run using RuleBender, with the included .bngl files.
Single-particle reaction-diffusion was run with NERDSS.

All model variations, including changes to D and both macroscopic and microscopic rates are included in the spreadsheet:
nerdss_inputs/Autophos_nerdss_parameters.xlsx
