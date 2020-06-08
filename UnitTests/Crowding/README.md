# Crowding influenced bimolecular association

Experiment setting for eGFRD: 

All simulations were performed in a box of the size (23.21nm)^3 = (50nm * 10^(-1/3))^3.
The particles A, B and C have a radius of 0.5 nm and a diffusion coefficient of 10^-11 m^2/s. The first reaction rule is

A+B -> A-B @ ki = 85*10^-21 m^3/s

where ki is the intrinsic rate. A and B form the complex A-B (r = 0.5 nm, D = 0), since eGFRD only allows one product in a bimolecular reaction. Therefore, a second reaction rule is needed.

A-B -> B + C @ ki = inf,

where the rate ki is infinity (those are possible for first-order reactions), the complex A-B decays after a short time (it looks like A-B exists only for a few ns at most). The simulation starts with 100 A and 100 B particles. The number of C particles is chosen in a way, that A+B+C fill x % of the box (crowding factor). 

The tested crowding factors are;
0.8% -> Nc = 0
5%   -> Nc = 994
10%  -> Nc = 2187
15%  -> Nc = 3381
20%  -> Nc = 4575
25%  -> Nc = 5768

Experiment setting for NERDSS:

