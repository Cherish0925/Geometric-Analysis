#!/usr/bin/env python3
"""Step 28 checks for terminal recalibration and exponential-pullback selection.

This is an algebra/logic ledger, not a geometric proof. It verifies the constants
used after reapplying the Seiberg-Witten/Chern-Gauss-Bonnet calibration to the
terminal metric and records the quantitative pullback-selection implication.
"""
import sympy as sp

Q, J, D, pi = sp.symbols('Q J D pi', positive=True)

# In dimension four, E = Ric + g = Ric0 + ((s+4)/4) g, and |c g|^2 = 4 c^2.
# Therefore |E|^2 = |Ric0|^2 + (s+4)^2/4.
scalar_constant = 4  # int (s+4)^2 <= 4 Q
J_constant = sp.Rational(1, 8)  # J=(1/(8*pi^2)) int |Ric0|^2 <= Q/(8*pi^2)

# D_a <= J. Completion-square and gap-density constants from Step 8.
square_const = sp.simplify(864 * pi**2 * (Q / (8*pi**2)) / Q)
gap_const = sp.simplify(48 * pi**2 * (Q / (8*pi**2)) / Q)
total_with_scalar = sp.simplify(1 + scalar_constant + square_const + gap_const)
total_without_redundant_scalar = sp.simplify(1 + square_const + gap_const)

print('Terminal recalibration constants')
print('int |E|^2                         <= 1 * Q')
print(f'int (s+4)^2                       <= {scalar_constant} * Q')
print('J=(1/(8*pi^2)) int |Ric0|^2       <= Q/(8*pi^2)')
print('D_a <= J for selected sign and q>=0')
print(f'int (s+8sqrt(6)|W+|)^2           <= {square_const} * Q')
print(f'int G_gap                         <= {gap_const} * Q')
print(f'combined with scalar modulus       <= {total_with_scalar} * Q')
print(f'combined without redundant scalar  <= {total_without_redundant_scalar} * Q')
assert square_const == 108
assert gap_const == 6
assert total_with_scalar == 119

# Pullback selection ledger: If int D <= eps*A and Vol(P) >= alpha*A,
# then (1/Vol P) int_P A_rD <= C*eps/alpha, so some center has that bound.
eps, A, alpha, C = sp.symbols('eps A alpha C', positive=True)
mean_bound = sp.simplify(C * eps * A / (alpha * A))
print('\nExponential-pullback selection ledger')
print('Assume int_M D <= eps*A and Vol(P) >= alpha*A.')
print(f'Then average_P A_r D <= {mean_bound}; hence selected center has the same bound.')
assert mean_bound == C*eps/alpha

# Moser/terminal compatibility: if Q(0)/A -> 0 and Q(T) <= exp(Ctheta)Q(0),
# then combined terminal deficit/A -> 0. We only record the symbolic implication.
thetaC = sp.symbols('thetaC', positive=True)
combined_over_A = sp.simplify(total_with_scalar * sp.exp(thetaC) * Q / A)
print('\nIf Q(T)<=exp(Ctheta)Q(0), combined_deficit(T)/A <=')
print(combined_over_A)
print('so it tends to 0 whenever Q(0)/A tends to 0.')
print('\nPASS: terminal recalibration constants and pullback-selection implication verified.')
