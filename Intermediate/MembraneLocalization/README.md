#Copy Numbers
P1: 1 uM
P2: 1 uM
M: 17000 molec/um^2
P1P2: 0	
P1M: 0
P2M: 0
P1P2M: 0
P2P1M: 0
MP1P2M:0	

#Diffusion Coefficients
P1: 50	
P2: 50	
M: 0.5	
P1P2: 25	
P1M: 0.495	
P2M: 0.495	
P1P2M: 0.2488	
P2P1M: 0.2488	
MP1P2M: 0.2475	

#System Dimensions
Box: 0.47x0.47x0.76 um
Sphere: R=2.2854um

#Reactions
				
Reactions		k_a,FPR	     k_on	        k_b,FPR	              k_off
P1 + P2 <-> P1P2		16.828 nm^3/us	10.0 uM-1s-1	1.0100 s-1	1.0 s-1
M + P1 <-> P1M		3.3386 nm^3/us	2.0 uM-1s-1	1.0053 s-1	1.0 s-1
M + P2 <-> P2M		3.3386 nm^3/us	2.0 uM-1s-1	1.0053 s-1	1.0 s-1
M + P1P2 <-> P1P2M		3.3386 nm^3/us	2.0 uM-1s-1	1.0053 s-1	1.0 s-1
M + P1P2 <-> P2P1M		3.3386 nm^3/us	2.0 uM-1s-1	1.0053 s-1	1.0 s-1
P1M + P2 <-> P2P1M		16.828 nm^3/us	10.0 uM-1s-1	1.0100 s-1	1.0 s-1
P2M + P1 <-> P1P2M		16.828 nm^3/us	10.0 uM-1s-1	1.0100 s-1	1.0 s-1
P1M + P2M <-> MP1P2M		-	8.3056 um^2/s	-	1.0 s-1
P1P2M + M <-> MP1P2M		-	1.6611 um^2/s	-	1.0 s-1
P2P1M + M <-> M P1P2M		-	1.6611 um^2/s	-	1.0 s-1

