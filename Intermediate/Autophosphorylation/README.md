# Autophosphorylation model

This is a simple model of an autophosphorylating kinase based on an early model of Lisman (1985).

    A -> Ap S
    K1(Y~0) + K1(Y~P) -> K1(Y~P) + K1(Y~P) 0.01
    K1(Y~P) + P(b) <-> K1(Y~P!1).P(b!1) 0.4, 1 
    K1(Y~P!1).P(b!1) -> K1(Y~0) + P(b) 1

## References

Lisman, J E. (1985) “A Mechanism for Memory Storage Insensitive to Molecular 
Turnover: A Bistable Autophosphorylating Kinase.” *PNAS*, **82**, 3055–57.
