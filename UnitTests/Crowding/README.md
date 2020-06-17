# Crowding influenced bimolecular association
# System Dimensions  
Box:  
L = 23.21 nm  
V = 12500 nm^3  

# Copy Numbers  
A: 100  
B: 100  
A-B: 0	(only in eGFRD)  
C: depends on the crowding factor.  
The tested crowding factors are;  
0.8% -> Nc = 0  
5%   -> Nc = 994  
10%  -> Nc = 2187  
15%  -> Nc = 3381  
20%  -> Nc = 4575  
25%  -> Nc = 5768  

# Diffusion Coefficients [µm²/s]  
A: 10  
B: 10  
A-B: 0  (only in eGFRD)  
C: 10  

# Radius [nm]  
A: 0.5  
B: 0.5  
A-B: 0.5 (only in eGFRD)  
C: 0.5  

# Reactions
				
| Reactions | k_a,FPR| k, eGFRD|  
| --- | --- | --- |  
| A + B -> C + B |    | - |  
| A + B -> A-B | - | 85*$10^-21$ m$^3$/s |  
| A-B -> C + B | - | $\infty$ |  
