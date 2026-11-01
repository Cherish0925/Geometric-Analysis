#!/usr/bin/env python3
"""Exact zero-order Weyl algebra; not a PDE or compactness verification."""
import sympy as s

t, b, sigma = s.symbols("t b sigma", real=True)
lam = [-4*t/3, 2*t/3-b/2, 2*t/3+b/2]
norm2 = s.expand(sum(x*x for x in lam))
assert s.simplify(sum(lam)) == 0
assert s.simplify(norm2 - (8*t*t/3+b*b/2)) == 0

# Ric = sigma*g gives scalar = 4*sigma, with nonnegative Laplacian.
# The nonnegative eigenvector-derivative term in Delta lambda_1 is not
# simulated here; multiplying by -3/4 turns it into a favorable term.
lowest_block = -2*sigma*lam[0] + 6*lam[0]**2 - 2*norm2
amplitude_block = s.expand(-s.Rational(3, 4)*lowest_block)
assert s.simplify(amplitude_block - (-2*sigma*t-4*t*t+3*b*b/4)) == 0
assert amplitude_block.subs({sigma: 0, b: 0}) == -4*t*t
assert s.factor(amplitude_block.subs(b, 0)) == -2*t*(sigma+2*t)
assert amplitude_block.subs({sigma: -1, b: 0, t: s.Rational(1, 2)}) == 0
print("PASS: Weyl norm, Einstein-scale roots, and Ricci-flat bubble amplitude equation")
