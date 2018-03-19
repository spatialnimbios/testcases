# Autophosphorylation model

This is a simple model of an autophosphorylating kinase based on an early model of Lisman (1985).

## Species
The model has two molecular entities: a kinase, A, and a phosphatase, P. The model has two additional species: Aphos, the phosphorylated kinase, and P_Aphos, which is the kinase-phosphatase complex. 

## Reactions
A undergoes spontaneous phosphorylation at a rate *S*:

    A -> Aphos S

A also undergoes autophosphorylation:

    A + Aphos -> Aphos + Aphos k_Aphos

P binds its substrate Aphos *reversibly*:

    P + Aphos <-> P_Aphos k_f, k_r
    
The P_Aphos complex gives rise to P and A:

    P_Aphos -> P + A k_cat

## Initial concentrations

|Species| Concentration (molecules)  |
|-------|-------------------|
|   A   | 100               |
|   P   |  10               |

## Rate parameters

|Parameter| Value | Units   |
|-------|---------|---------|
|   S   |variable | 1/s  |
| k_Aphos|  0.01  | µm<sup>3</sup>/s            |
| k_f|  0.4 | µm<sup>3</sup>/s             |
| k_r|  1.0 |1/s |
| k_cat| 1.0 |1/s|

## Simulations

## References

Lisman, J E. (1985) “A Mechanism for Memory Storage Insensitive to Molecular 
Turnover: A Bistable Autophosphorylating Kinase.” *PNAS*, **82**, 3055–57.
