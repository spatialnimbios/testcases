# Membrane localization model  

# System Dimensions  
Box: 0.47 * 0.47 * 5 um  
SA: 0.2209  
V: 1.1045  

# Copy Numbers  
A: 1 uM = 665 molec  
B: 1 uM = 665 molec  
M: 17000 molec/um^2 = 3755 molec  
AB: 0	  
MA: 0  
BM: 0  
MAB: 0  
ABM: 0  
MABM: 0  	

# Diffusion Coefficients [µm²/s]  
A: 50  
B: 50  
M: 0.5  
AB: 25  
MA: 0.495  
BM: 0.495  
MAB: 0.2488  
ABM: 0.2488  
MABM: 0.2475  

# Reactions
				
| Reactions | k_a,FPR| k_on| k_b,FPR| k_off|
| --- | --- | --- | --- | --- |
| A + B <-> AB | 0.08303 nm^3/us | 50000.0 M-1s-1 | 1.000 s-1 | 1.0 s-1 |  
| M + A <-> MA | 3.3386 nm^3/us | 2.0 uM-1s-1 | 1.0053 s-1 | 1.0 s-1 |  
| M + B <-> BM | 3.3386 nm^3/us | 2.0 uM-1s-1 | 1.0053 s-1 | 1.0 s-1 |  
|M + AB <-> MAB |		3.3386 nm^3/us|	2.0 uM-1s-1|	1.0053 s-1|	1.0 s-1|
|M + AB <-> ABM|		3.3386 nm^3/us|	2.0 uM-1s-1|	1.0053 s-1|	1.0 s-1|
|MA + B <-> MAB|		0.08303 nm^3/us|	50000.0 M-1s-1|	1.000 s-1|	1.0 s-1|
|BM + A <-> ABM|		0.08303 nm^3/us|	50000.0 M-1s-1|	1.000 s-1|	1.0 s-1|
|MA + BM <-> MABM|		0.0415 nm^2/us|	0.0415 um^2/s|	1.0 s-1|	1.0 s-1|
|MAB + M <-> MABM|		1.6693 nm^2/us|	1.6611 um^2/s|	1.0053 s-1|	1.0 s-1|
|ABM + M <-> MABM|		1.6693 nm^2/us|	1.6611 um^2/s|	1.0053 s-1|	1.0 s-1|
  
The Smoldyn model was run 10 times in the stand alone Verion 2.61.  
The Gillespie (N=10), ODE and PDE models were run in Vcell.  
The NERDSS model was run x times in the stand alone Version.  

