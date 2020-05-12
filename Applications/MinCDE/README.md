# Min CDE

Diffusion that is slow enough or occurs over large enough length scales, coupled with reactions, can establish spatial gradients of concentrations and subsequent oscillations in space and time. By construction, these dynamics are lost in non-spatial models. In a simplified model of bacterial cell division, the MinD and MinE proteins (Huang et al, PNAS 2003) spatially control the location of cell division by creating an oscillating spatial gradient of both proteins in the cytosol and on the membrane. 

In the Huang et al paper, there is no membrane diffusion.	

# SPECIES     	
D. Coeff (um2.s-1)	Huang paper Copy Numbers/um (?).	


1	MinDD	      	  2.5 um2.s-1  		0

2	MinDT	     	   2.5 um2.s-1		1000 /um

3	minDt.minE  	    0 um2.s-1		0

4	MinE	           2.5 um2.s-1		350 homodimers/um	

5	minDt	   	   0 um2.s-1		0

Copy Numbers (from Shih et al 2002 EMBO J) have minDT=2000 proteins, and E=1400 monomers. Since E is active as a homodimer (Huang et al), the simulated copy numbers would then be 700. The ratio of minDT:E is then 2.857.

# Actual Initial concentrations used that maintain the same ratio of 1000:350 minDT:E. 
Within the cylinder used (h=4um, R=0.5um), we simulated 4730 copies of minDT and 1655 copies of E. 
For Virtual Cell, both minDT and E were initially uniform throughout the Volume. This is the simplest initialization, although it is not what Huang et al did: In Huang et al, in Figure 2, there is a spatial gradient even at time zero. In Kerr et al, PNAS 2006 (MCell), the also initialized with a gradient. 
Both of those simulations used 4000 minDT and 1400 E, which is 2.1143uM and 0.74uM, respectively. 
Kerr et al also used the 1000:350 ratio, and a 4:1 ratio. 

1. MinDD: 0

2. MinDT: 2.1143uM

3. minDt.minE: 0

4. MinE: 0.875 uM

5. minDt: 0

*If initial conc. of minDT and E is instead 1.2686uM and 0.444uM, the oscillations disappear!!


# Notes:
1. *Huang et al note the E is only active as a homodimer, so observed copy numbers in a cell should be halved to capture the copy numbers of active species. Hence they use 350/um rather than 700/um. 

2. MinDD, MinDT, and MinE are all cytosolic.
3. minDt and minDt.minE are both on the membrane.

# GEOMETRY: 
Cylinder. In Huang et al, They do not use spherical caps on the ends of the cylinder.

R=0.5um

L=4um


# REACTIONS:

	Reactions	Kf	
	
1.1	MinDT → minDt	                      0.025 um.s-1		

2.2	MinDT + minDt → 2minDt	                  0.903s-1.uM-1		

3.3	MinDT + minDt.minE → minDt + minDt.minE	      0.903 s-1.uM-1	

4.4	MinE + minDt → minDt.minE                      56.0 s-1.uM-1

5.5	minDt.minE → MinDD + MinE	            0.7s-1		

6.6	MinDD → MinDT	     1s-1	



NOTE FOR RXN 2: Here we produce two minDt molecules. The cytosolic MinDT, collides with minDt on the membrane, and when it is successful, it turns into minDt, which is on the surface.

NOTE FOR RXN 1: Surface Adsorption reaction. Units for VCELL 15.055 molecules/um2/s/uM

## Results:
For initial concentrations of 2.5uM and 0.875uM (same ratio but higher total copies), the symmetric oscillations at the beginning for the PDE are more visible. 

# SMOLDYN:

Using the model specified above, Smoldyn shows temporal oscillations of minDt and minDt.minE, but they are noisy and do not correspond to anti-correlated oscillations from one end of the cylinder relative to the middle. Even for 400s. Adding membrane diffusion seems to help, or a non-uniform initial condition. In the PDE, the oscillations are symmetric for the first ~250s before they become unstable and revert to the pole-to-pole oscillations seen exclusively in Huang et al and Kerr et al.

Philipp got Smoldyn to work by adding in membrane diffusion at 0.05 𝜇m2/s  for both minDt and minDt.minE. He also initialized MinDT half in solution (2000 MinDT) and half on membrane (2000 minDt). He showed that the dynamics of the Smoldyn model were also affected by the choice of the unbinding radius for Rxn 5.5 --when MinDT dissociates from the membrane. 




# REFERENCES
Huang, K.C. et al, Dynamic structures in Escherichia coli: Spontaneous formation of MinE rings and MinD polar zones, PNAS, 100:12724-12728 (2003).
Kerr, R.A. et al, Division accuracty in a stochastic Min Model, PNAS, (2006).
