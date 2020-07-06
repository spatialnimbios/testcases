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
				
| Reactions | k_on| k_a, FPR |  
| --- | --- | --- |  
| A -> Ap | 21.2 s-1 | 21. s-1 |  
| A + Ap -> A_Ap | 10 uM-1s-1 | 16.7 nm3/us |  
| A_Ap -> Ap + Ap | 200 1/s | 200s-1 |  
| Ap + P -> Ap_P | 800 uM-1s-1 | 2820 nm3/us |  
| Ap_P -> A + P | 539 1/s | 539 s-1 |	 

# Solvers

ODE and SSA were run using RuleBender, with the included .bngl files.
Single-particle reaction-diffusion was run with NERDSS.
