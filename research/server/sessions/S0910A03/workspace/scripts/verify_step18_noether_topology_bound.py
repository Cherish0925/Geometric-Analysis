#!/usr/bin/env python3
"""
Exact topological arithmetic behind the Step 18 Noether replacement.

For minimal complex surfaces of general type X_j, write
  a_j = c1^2(X_j), c_j = c2(X_j), q_j = chi_h(X_j).
Noether: a_j + c_j = 12 q_j.
Noether inequality: a_j >= 2 p_g(X_j)-4 and q_j=1-q+p_g <= 1+p_g
imply q_j <= (a_j+6)/2, hence c_j <= 5 a_j+36.

For M=(#_{j=1}^m X_j)#N, m=2 or 3, with
  A=sum a_j, D=4m-(2chi+3tau)(N)=A/3,
we verify the connected-sum Euler formula and isolate exactly what must be
assumed about N to bound chi(M)/A from above.
"""
import sympy as sp

m, A, sumc2, chiN = sp.symbols('m A sumc2 chiN', positive=True)
# Connected sum of m surfaces and N: chi(M)=sum chi(X_j)+chi(N)-2m.
chiM = sumc2 + chiN - 2*m
print("chi(M) =", chiM)

# Sum of Noether bounds c2_j <= 5 a_j + 36.
upper_sumc2 = 5*A + 36*m
upper_chiM = sp.expand(upper_sumc2 + chiN - 2*m)
print("Using Noether inequality: chi(M) <=", upper_chiM)
assert sp.expand(upper_chiM - (5*A + 34*m + chiN)) == 0

# Critical relation fixes T_N=(2chi+3tau)(N)=4m-A/3, not chiN alone.
tauN = sp.symbols('tauN')
TN = 2*chiN + 3*tauN
critical_sub = sp.solve(sp.Eq(TN, 4*m-A/3), tauN)[0]
print("Critical relation gives tau(N) =", critical_sub)
# Verify chiN remains a free symbol after solving for tauN.
assert chiN in critical_sub.free_symbols

# If N is negative definite with b1=0 and b2=k, then chiN=2+k,
# tauN=-k, so T_N=4-k and D=k. At D=A/3, k=A/3.
k = sp.symbols('k', nonnegative=True)
chiN_nd = 2+k
tauN_nd = -k
TN_nd = sp.expand(2*chiN_nd+3*tauN_nd)
D_nd = sp.expand(4*m-TN_nd)
print("For b1=0 negative-definite N: T_N=", TN_nd, ", D=", D_nd)
# Note: Ishida-LeBrun D definition includes 4m; for connected sum choice N often
# has a convention-dependent 4m offset. We therefore do not identify D=k
# without checking the exact N used in the theorem.

# General useful conditional: if chiN <= cN*A+C_N, then
# chiM/A <= 5+cN+(34m+C_N)/A.
cN, CN = sp.symbols('cN CN', nonnegative=True)
ratio_bound = sp.simplify((5*A + 34*m + cN*A + CN)/A)
print("If chi(N)<=cN*A+CN, then chi(M)/A <=", ratio_bound)
assert sp.simplify(ratio_bound-(5+cN+(34*m+CN)/A)) == 0

print("PASS: Noether yields c2(X_j)<=5c1^2(X_j)+36, but the critical D relation alone does not bound chi(N); the N hypotheses must be checked explicitly.")
