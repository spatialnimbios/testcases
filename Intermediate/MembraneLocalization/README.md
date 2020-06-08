# System Dimensions
Box: 0.47x0.47x5 um  

SA: 0.2209
V: 1.1045

# Copy Numbers  
P1: 1 uM  
P2: 1 uM  
M: 17000 molec/um^2  
P1P2: 0	  
P1M: 0  
P2M: 0  
P1P2M: 0  
P2P1M: 0  
MP1P2M:0  	

# Diffusion Coefficients [µm²/s]  
P1: 50  
P2: 50  
M: 0.5  
P1P2: 25  
P1M: 0.495  
P2M: 0.495  
P1P2M: 0.2488  
P2P1M: 0.2488  
MP1P2M: 0.2475 

# Radius [nm] 
P1:   
P2:   
M:   
P1P2:   
P1M:   
P2M: 
P1P2M: 
P2P1M: 
MP1P2M: 

# Reactions
				
| Reactions | k_a,FPR| k_on| k_b,FPR| k_off|
| --- | --- | --- | --- | --- |
| P1 + P2 <-> P1P2 | 0.08303 nm^3/us | 50000.0 M-1s-1 | 1.000 s-1 | 1.0 s-1 |  
| M + P1 <-> P1M | 3.3386 nm^3/us | 2.0 uM-1s-1 | 1.0053 s-1 | 1.0 s-1 |  
| M + P2 <-> P2M | 3.3386 nm^3/us | 2.0 uM-1s-1 | 1.0053 s-1 | 1.0 s-1 |  
|M + P1P2 <-> P1P2M|		3.3386 nm^3/us|	2.0 uM-1s-1|	1.0053 s-1|	1.0 s-1|
|M + P1P2 <-> P2P1M|		3.3386 nm^3/us|	2.0 uM-1s-1|	1.0053 s-1|	1.0 s-1|
|P1M + P2 <-> P2P1M|		0.08303 nm^3/us|	50000.0 M-1s-1|	1.000 s-1|	1.0 s-1|
|P2M + P1 <-> P1P2M|		0.08303 nm^3/us|	50000.0 M-1s-1|	1.000 s-1|	1.0 s-1|
|P1M + P2M <-> MP1P2M|		0.0415 nm^2/us|	0.0415 um^2/s|	1.0 s-1|	1.0 s-1|
|P1P2M + M <-> MP1P2M|		1.6693 nm^2/us|	1.6611 um^2/s|	1.0053 s-1|	1.0 s-1|
|P2P1M + M <-> M P1P2M|		1.6693 nm^2/us|	1.6611 um^2/s|	1.0053 s-1|	1.0 s-1|

# Results
The relative SA to Volume is a critical parameter for determining the equilibrium populations. It also influences the kinetics, but for kinetics, results are also sensitive to the geometry--whether it is a box with a surface on one side, or a sphere surrounded by membrane.
As thte distance to the membrane grows, the spatial models start to produce slower kinetics than well-mixed systems, particularly when the reaction with the surface is diffusion-limited (most collisions result in binding). 

FPR, ODE, PDE, produce the same equilibrium. Smoldyn is off due to incorrect 2D reactions.
