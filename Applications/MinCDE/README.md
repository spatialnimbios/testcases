# Min CDE

Diffusion that is slow enough or occurs over large enough length scales can establish spatial gradients of concentrations and subsequent oscillations in space and time. By construction, these dynamics are lost in non-spatial models. In a simplified model of bacterial cell division, the MinD and MinE proteins (Huang et al, PNAS 2003) spatially control the location of cell division by creating an oscillating spatial gradient of both proteins in the cytosol and on the membrane. 

In the Huang et al paper, there is no membrane diffusion.	

# SPECIES     Copy Numbers (from Shih et al 2002 EMBO J)	D. Coeff (um2.s-1)	Huang et al paper copy numbers.	


1	minDD	    0	        2.5um2.s-1  0

2	minDT	    2000	    2.5um2.s-1	1000 /um

3	EminDt  	0	        0um2.s-1		0

4	E	        1400* monomers	    2.5um2.s-1	350 homodimers/um	

5	minDt	    0	        0um2.s-1		0


# Actual Initial concentrations used that maintain the same ratio of 1000:350 minDT:E. 
Within the cylinder used (h=4um, R=0.5um), this corresponds to 4730 copies of minDT and 1655 copies of E. 

1. minDD: 0

2. minDT: 2.5uM

3. EminDt: 0

4. E: 0.875 uM

5. minDt: 0

If initial conc. of minDT and E is instead 1.2686uM and 0.444uM, the oscillations disappear!


# Notes:
1. *Huang et al note the E is only active as a homodimer, so observed copy numbers in a cell (1400) should be halved to capture the copy numbers of active species. Hence they use 350/um rather than 700/um. 

2. minDD, minDT, and E are all cytosolic.
3. minDt and EminDt are both on the membrane.

# GEOMETRY: 
Cylinder. In Huang et al, They do not use spherical caps on the ends of the cylinder.

R=0.5um

L=4um


# REACTIONS:

	Reactions	Kf	
	
1.1	minDD -> minDT	                      1 s-1		

2.2	EminDt -> minDD + E	                  0.7 s-1		

3.3	minDt + E -> EminDt	                  56.0 (s-1.uM-1)	

4.4	minDT -> minDt	                      0.025 um.s-1	

5.5	minDt + minDT -> 2 minDt	            0.903 (s-1.uM-1)		

6.6	EminDt + minDT -> minDt + EminDt	    0.903 (s-1.uM-1)	



NOTE FOR RXN 5: Here we produce two minDt molecules. The cytosolic minDT, collides with minDt on the membrane, and when it is successful, it turns into minDt, which is on the surface.

NOTE FOR RXN 4: Units for VCELL 15.055 molecules/um2/s/uM





# REFERENCES
Huang, K.C. et al, Dynamic structures in Escherichia coli: Spontaneous formation of MinE rings and MinD polar zones, PNAS, 100:12724-12728 (2003).
