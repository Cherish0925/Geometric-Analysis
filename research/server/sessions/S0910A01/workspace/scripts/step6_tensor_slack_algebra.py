#!/usr/bin/env python3
"""
Step 6 algebra for the tensor-level near-equality route in Yau 26.

This script verifies the elementary identities used to separate the scalar
curvature-ratio remainder from the additional tensorial information needed for
Derdzinski-type local rigidity.
"""
import sympy as sp

# Eigenvalues of W^+ ordered alpha >= beta >= gamma; in the target gamma is the
# lowest eigenvalue w and alpha,beta are the two equal positive eigenvalues.
alpha, beta, gamma, s = sp.symbols('alpha beta gamma s', real=True)
trace_relation = sp.Eq(gamma, -alpha - beta)

u2 = alpha**2 + beta**2 + gamma**2
w = gamma
# Substitute trace-free relation to compute the algebraic two-eigenvalue defect.
u2_tf = sp.expand(u2.subs(gamma, -alpha - beta))
w_tf = (-alpha - beta)
eig_defect = sp.simplify(u2_tf - sp.Rational(3, 2) * w_tf**2)
print("Trace-free W^+ eigenvalue algebra")
print("|W|^2 with gamma=-alpha-beta =", u2_tf)
print("|W|^2 - (3/2)w^2 =", sp.factor(eig_defect))
print("Expected: (alpha-beta)^2/2")
assert sp.simplify(eig_defect - sp.Rational(1,2)*(alpha-beta)**2) == 0

# Pointwise slack between LeBrun's |W| version and the lowest-eigenvalue version.
u, w, s = sp.symbols('u w s', real=True)
c = sp.sqrt(sp.Rational(2,3))
T_absW = ((sp.Rational(2,3))*s - 2*c*u)**2
T_lowest = ((sp.Rational(2,3))*s + 2*w)**2
point_slack = sp.factor(T_absW - T_lowest)
print("\nPointwise slack T_absW - T_lowest =")
print(point_slack)
# Alternative positive factorization valid when s<0 and c*u+w>=0.
positive_factor = sp.factor(2*(c*u + w)*(-sp.Rational(4,3)*s + 2*c*u - 2*w))
print("Positive-factor form =")
print(positive_factor)
assert sp.simplify(point_slack - positive_factor) == 0

# Relation between c|W|+w and the eigenvalue degeneracy, assuming w is the lowest
# eigenvalue and |W|=u.
# c*u + w = c*u - t, t=-w.  The two-eigenvalue defect A=u^2-(3/2)t^2.
t = sp.symbols('t', positive=True, real=True)
Adef = sp.symbols('Adef', nonnegative=True, real=True)
expr = sp.simplify(c*u - t - (sp.Rational(2,3)*(u**2 - sp.Rational(3,2)*t**2)/(c*u + t)))
print("\nRelation c*u-t to eigenvalue defect simplifies to", sp.factor(expr))
assert sp.simplify(expr) == 0

# Target constants under s=-4, u=1/(2 sqrt(6)), c*u=t.
u_target = sp.Rational(1,2)/sp.sqrt(6)
t_target = c*u_target
alpha_target = beta_target = t_target/2
gamma_target = -t_target

# Standard Kähler surface convention: W^+ eigenvalues are
# (s/6, -s/12, -s/12).  For Ric=-g in dimension four, s=-4.
ske = sp.Integer(-4)
ke_eigs = [ske/6, -ske/12, -ske/12]
ke_norm_sq = sp.simplify(sum(x*x for x in ke_eigs))
print("\nTarget values")
print("u=|W^+| =", sp.simplify(u_target))
print("t=-w =", sp.simplify(t_target))
print("eigenvalues (alpha,beta,gamma) =", [sp.simplify(alpha_target), sp.simplify(beta_target), sp.simplify(gamma_target)])
print("|W|^2 =", sp.simplify(u_target**2))
print("s + 8 sqrt(6) u at s=-4 =", sp.simplify(-4 + 8*sp.sqrt(6)*u_target))
print("KE eigenvalues for Ric=-g (ordered) =", [sp.simplify(ke_eigs[1]), sp.simplify(ke_eigs[2]), sp.simplify(ke_eigs[0])])
print("KE |W|^2 =", ke_norm_sq)
print("target/KE eigenvalue ratio =", sp.simplify(alpha_target/ke_eigs[1]))
print("target/KE norm ratio =", sp.simplify(u_target/sp.sqrt(ke_norm_sq)))
assert sp.simplify(u_target**2 - sp.Rational(1,24)) == 0
assert sp.simplify(-4 + 8*sp.sqrt(6)*u_target) == 0
assert sp.simplify(gamma_target + sp.Rational(1,6)) == 0
assert sp.simplify(alpha_target - sp.Rational(1,12)) == 0
assert sp.simplify(ke_norm_sq - sp.Rational(2,3)) == 0
assert sp.simplify(alpha_target/ke_eigs[1] - sp.Rational(1,4)) == 0
assert sp.simplify(u_target/sp.sqrt(ke_norm_sq) - sp.Rational(1,4)) == 0

print("\nAll Step 6 tensor-slack algebra checks passed.")
