# Autophosphorylation model

This is a simple model of an autophosphorylating kinase based on an early model of Lisman (1985). The parameters of the model, initial concentrations and rate parameters, have been chosen so that the system has two stable fixed points (Ap at steady state is 1.70 molecules in the low state and 35.47 molecules in the high state for the ODE version of the model). 

## Species
The model has two molecular entities: a kinase, A, and a phosphatase, P. The model has three additional species: Ap, the phosphorylated kinase, A_Ap, the complex between an unphosphorylated kinase and a phosphorylated kinase, and Ap_P, the complex between the phosphorylated kinase and the phosphatase. 

## Reactions
(1) Spontaneous phosphorylation of A:

    A -> Ap k1

(2) A binds Ap:

    A + Ap -> A_Ap k2

(3) Catalytic conversion of A_Ap complex:

    A_Ap -> Ap + Ap k3
    
(4) Ap binds P:

    Ap + P -> Ap_P k4
    
(5) Catalytic conversion of Ap_P complex:

    Ap_P -> A + P k5
 

## Geometry

Cube with volume 0.003 um^3

## Initial concentrations

|Species| Concentration (molecules)
|-------|-------------------|
|   A   | 103
|   Ap  |   5
|   P   |   9               |

## Rate parameters

Second set of values is for simulation 


|Parameter| Value | Units   | Value | Units
|-------|---------|---------|---------|---------|
|   k1  |2.12e1 | 1/s  | 2.12e1 | 1/s
|   k2  |1.00e7  | 1/M 1/s  | 5.56 | 1/molec 1/s
|   k3  |2.00e2  |  1/s  | 2.00e2 | 1/s
|   k4  |8.00e8  | 1/M 1/s  | 4.44e2 | 1/molec 1/s
|   k5  |5.39e2  |  1/s  |5.39e2  |  1/s 

For single-particle Smoluchowski:
Parameter| Value | Units   | Value | Units
|-------|---------|---------|---------|---------|
|   k1  |2.12e1 | 1/s  | 
|   k2  |16.7  | nm3/us  | sigma: 1 nm, Dtot=200nm2/us
|   k3  |2.00e2  |  1/s  | 
|   k4  |2820  | nm3/us  | sigma: 1 nm, Dtot=200nm2/us
|   k5  |5.39e2  |  1/s  |

Note that in Agarwal et al, the binding reactions were also reversible, with rates 20/s for Rxn (2) and 10/s for Rxn (1). 
The rates from Agarwal et al have all been increased by 1e4. 

## Simulations
Diffusion constant  100 um2/s each for A and Phos.

## Results
Switching occurs between low and high states in SSA and single-particle simulations. 
Addition of reversible binding makes time spent in high state less, but otherwise similar switching results.

To put data points in states, used copy numbers of Ap and A, and a simple 2D cutoff. If Ap < 20 AND A>50 put in state 1 (low), else put in state 2. This works well, also agrees well with an HMM. 
Calculated intervals in states 1 and 2, and took averages of them, and Std of intervals ~200-300 intervals per 20s trajectory. 

Stdev of state probabilities calculated from first 10s and second 10s analysis of NERDSS.

Times are in Units of seconds. 

|State. | Prob SSA      |   Prob NERDSS|. <time> SSA | <time> NERDSS |
|-------|---------------|--------------|-------------|------------|
|   1 Low   | 0.16  | 0.16+-0.02  | 0.008 +-0.1 | 0.008 +-0.05
|   2 High  | 0.84  | 0.84+-0.02   | 0.06 +-0.3 | 0.04 +-0.19


## References

Lisman, J E. (1985) “A Mechanism for Memory Storage Insensitive to Molecular 
Turnover: A Bistable Autophosphorylating Kinase.” *PNAS*, **82**, 3055–57.

"On the precision of quasi steady state assumptions in stochastic dynamics", Agarwal et al J Chem Phys 2012: Thorsten got parameters from this paper. 
