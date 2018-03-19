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

## Rate parameters

## Simulations

## References

Lisman, J E. (1985) “A Mechanism for Memory Storage Insensitive to Molecular 
Turnover: A Bistable Autophosphorylating Kinase.” *PNAS*, **82**, 3055–57.
