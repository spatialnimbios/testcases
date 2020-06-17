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
A: 10  
Ap: 10  
P: 10  

# Reactions
				
| Reactions | k_on| k_a, FPR |  
| --- | --- | --- |  
| A -> Ap | 21.2 s-1 | 2.12 s-1 |  
| A + Ap -> A_Ap | 10 uM-1s-1 | 1.67 nm3/us |  
| A_Ap -> Ap + Ap | 200 1/s | 20 s-1 |  
| Ap + P -> Ap_P | 800 uM-1s-1 | 282.0 nm3/us |  
| Ap_P -> A + P | 539 1/s | 53.9 s-1 |	 
