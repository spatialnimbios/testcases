# Min CDE adapted form Huang et al. PNAS 2006  

# System Dimensions  
Cylinder: r = 0.5 um, h = 4 um    

# Copy Numbers  
MinDD: 0  
MinDT: 2000  
minDt-minE: 0  
MinE: 1400  
minDt: 2000  

# Diffusion Coefficients [µm²/s]  
MinDD: 2.5  
MinDT: 2.5  
minDt-minE: 0.05  
MinE: 2.5  
minDt: 0.05  

# Reactions
				
| Reactions | k| 
| --- | --- |
| MinDT -> minDt | 0.025 um.s-1 |    
| MinDT + minDt -> 2minDt | 0.903s-1.uM-1 |  
| MinDT + minDt.minE -> minDt + minDt.minE | 0.903s-1.uM-1 |  
| MinE + minDt -> minDt.minE | 56.0 s-1.uM-1 |  
| minDt.minE -> MinDD + MinE | 0.7s-1 |  
| MinDD -> MinDT | 1s-1 |  

# Notes:
1. *Huang et al note the E is only active as a homodimer, so observed copy numbers in a cell should be halved to capture the copy numbers of active species. Hence they use 350/um rather than 700/um.  
2. MinDD, MinDT, and MinE are all cytosolic.  
3. minDt and minDt.minE are both on the membrane.  
