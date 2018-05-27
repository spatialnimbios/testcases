# Coupled Expression Dynamics
Oscillations in protein expression levels can exhibit sensitivity to copy number fluctuations that are only captured in stochastic solvers such as Gillespie or single-particle RD. Based on a simple model of circadian oscillations (Vilar et al, PNAS 2002), we have simulated the behavior of an activator protein A and repressor protein R that are produced from mRNA transcribed from a single copy of a gene (one for each protein). Coupling of A and R expression is driven by positive feedback of the activator A, which binds to each gene’s promoters to enhance transcription. Protein R also binds to A to effectively degrade it, and all proteins and mRNA are degraded. If the degradation rate of protein R is slow, the oscillations will end in the deterministic model, but persist in the stochastic method. 


Species Initial Concentration Diffusion Coefficient

1. A 0 uM (0 molecules) 10 um2/s
2. R 0 uM (0 molecules) 10 um2/s
3. C 0 uM (0 molecules) 10 um2/s
4. PrmA 0.000397 uM (1 molecule) 10 um2/s
5. PrmA_bound 0 uM (0 molecules) 10 um2/s
6. PrmR 0.000397 uM (1 molecule) 10 um2/s
7. PrmR_bound 0 uM (0 molecules) 10 um2/s
8. mRNA_A 0 uM (0 molecules) 10 um2/s
9. mRNA_R 0 uM (0 molecules) 10 um2/s

Reactions

1. A + R → C (1204 uM-1s-1) 
2. PrmA → PrmA + mRNA_A (50 s-1)
3. PrmA_bound → PrmA_bound + mRNA_A (500 s-1)
4. PrmR → PrmR + mRNA_R (0.01 s-1)
5. PrmR_bound → PrmR_bound + mRNA_R (50 s-1)
6. PrmA + A ↔ PrmA_bound (602 uM-1s-1) (50 s-1)
7. PrmR + A↔ PrmR_bound (602 uM-1s-1) (100 s-1)
8. mRNA_A → mRNA_A + A (50 s-1)
9. mRNA_R → mRNA_R + R (5 s-1)
10. mRNA_A → NULL (10 s-1)
11. mRNA_R → NULL (0.5 s-1)
12. A → NULL (1 s-1)
13. R→ NULL (0.2 s-1)
14. C→ R (1 s-1)

Parameters

V=4.189um^3 (Sphere with R=1um). 
Run time=200 s. 

Alternative systems:
Oscillations are eliminated in deterministic simulations when protein R degradation is slowed from 0.2 to 0.05 s-1: Rxn #13, R→ NULL (0.05 s-1)



References: Vilar, J. M.G. et al, Mechanisms of noise-resistance in genetic oscillators. PNAS, 99:5988-5992 (2002).
