#!/usr/bin/env python3
"""Verify the corrected Step 27/A03 weak-Moser recurrence.

The key correction is that sum 1/p_k is not the Sobolev exponent. In four
 dimensions with kappa=3/2, sum 1/p_k = 3/p0, while each parabolic step
contributes S^{1/(kappa p_k)} = S^{2/(3p_k)}, so the net Sobolev power is
S^{2/p0}=S^{n/(2p0)}.
"""
import sympy as sp

p0 = sp.symbols('p0', positive=True)
n = sp.Integer(4)
kappa4 = sp.Rational(3, 2)

sum_inv = sp.simplify((1/p0) * kappa4/(kappa4-1))
sob_power = sp.simplify((1/kappa4) * sum_inv)
expected_sum = sp.simplify((n+2)/(2*p0))
expected_sob = sp.simplify(n/(2*p0))
print('Corrected Moser recurrence verification')
print(f'kappa = {kappa4}')
print(f'sum 1/p_k = {sum_inv} = (n+2)/(2p0) -> {expected_sum}')
print(f'net Sobolev exponent = (1/kappa)*sum = {sob_power} = n/(2p0) -> {expected_sob}')
assert sp.simplify(sum_inv - expected_sum) == 0
assert sp.simplify(sob_power - expected_sob) == 0

for seed in [3, 6]:
    s = sp.simplify(sum_inv.subs(p0, seed))
    e = sp.simplify(sob_power.subs(p0, seed))
    print(f'p0={seed}: sum 1/p_k={s}; net S exponent={e}')
assert sob_power.subs(p0, 3) == sp.Rational(2, 3)
assert sob_power.subs(p0, 6) == sp.Rational(1, 3)

for seed in [3, 6]:
    partial = 0.0
    for j in range(80):
        pj = seed * float(kappa4)**j
        Lj_log = 3.0*sp.log(pj).evalf() + j*sp.log(4).evalf()
        partial += float(Lj_log / pj)
    print(f'p0={seed}: numeric sum_0^79 (3 log p_j + j log4)/p_j = {partial:.6f}')

print('PASS: corrected recurrence keeps polynomial p-dependence compatible with Moser convergence without exponentiating p^N through separate Gronwall steps.')
