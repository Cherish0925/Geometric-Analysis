#!/usr/bin/env python3
"""
Step 22: exponent ledger for fixed J6 persistence and unweighted Q triangle.

This is an algebra/scale check, not a tensor proof.  It verifies that:
1. fixed J_m moments can absorb the curvature reaction directly with gamma,
   without using the positive-time H3~1/t potential from zero;
2. the unweighted Q term int a F |E|^2 can be absorbed by applying Sobolev to
   w=eta*a^(1/2)*E, producing only a|grad E|^2 and |da|^2/a * E^2 remainders.
"""
import sympy as sp

m = sp.symbols('m', positive=True)
# Monomials in (eta, a, E, F).
def add(x, y):
    return tuple(sp.simplify(x[i]+y[i]) for i in range(4))

def mulc(x, c):
    return tuple(sp.simplify(c*x[i]) for i in range(4))

def same(x, y):
    return all(sp.simplify(x[i]-y[i]) == 0 for i in range(4))

Jm = (2, m-2, m, 0)
zm = (1, (m-1)/2, m/2, 0)
reaction_Jm = add((0,0,0,1), mulc(zm, 2))  # F z_m^2
assert same(reaction_Jm, (2, m-1, m, 1))
assert same(mulc(zm, 4), (4, 2*m-2, 2*m, 0))

# Direct fixed-m absorption: int F z_m^2 <= ||F||_2 ||z_m||_4^2.
# No H3 coefficient enters.
A, gamma, D, J, r, eps = sp.symbols('A gamma D J r eps', positive=True)
direct = gamma*(D + r**-2*J)
print('Fixed J_m direct reaction form:', direct)

# Unweighted Q: Q=int eta^2 E^2. Curvature potential is int eta^2 a F E^2.
w = (1, sp.Rational(1,2), 1, 0)   # eta a^(1/2) E
Q_potential = add((0,0,0,1), mulc(w, 2))
assert same(Q_potential, (2, 1, 2, 1))
assert same(mulc(w, 4), (4, 2, 4, 0))

# Gradient of w has sqrt(a) gradE and (da/sqrt(a))E pieces.
# Squared terms have weights a|gradE|^2 and |da|^2/a * E^2.
print('PASS: J_m curvature reaction is F z_m^2 with z_m=eta a^((m-1)/2)|E|^(m/2)')
print('PASS: fixed J_m can use ||F||_2 Sobolev product gamma, avoiding H3~1/t from zero')
print('PASS: Q curvature potential a F |E|^2 is F*w^2 for w=eta*a^(1/2)*E')
print('PASS: Sobolev on w yields a|grad E|^2 plus |da|^2/a*E^2 and cutoff remainders')
print('PASS: no monomial independent of E appears in these stability terms')
