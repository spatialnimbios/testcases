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
|   A   | 108               |
|   P   |   9               |

## Rate parameters

Second set of values is for simulation 

FOR SIMULATION BNGL FILE SHARED, ALL THESE RATES ARE MULTIPLIED BY 1E4.

|Parameter| Value | Units   | Value | Units
|-------|---------|---------|---------|---------|
|   k1  |2.12e-3 | 1/s  | 2.12e-3 | 1/s
|   k2  |1.00e3  | 1/M 1/s  | 5.56e-4 | 1/molec 1/s
|   k3  |2.00e-2  |  1/s  | 2.00e-2 | 1/s
|   k4  |8.00e4  | 1/M 1/s  | 4.44e-2 | 1/molec 1/s
|   k5  |5.39e-2  |  1/s  |5.39e-2  |  1/s 


## Simulations
Diffusion constant Re Jim: 100 um2/s for A and Phos.
## References

Lisman, J E. (1985) “A Mechanism for Memory Storage Insensitive to Molecular 
Turnover: A Bistable Autophosphorylating Kinase.” *PNAS*, **82**, 3055–57.
