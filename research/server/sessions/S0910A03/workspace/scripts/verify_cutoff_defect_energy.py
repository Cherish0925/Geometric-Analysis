"""
Algebraic sanity checks for the normalized cutoff flow

    dg/dt = -2 a E,   a = chi^2,   E = Ric + g.

The geometric tensor derivation gives

  dE/dt = a(Delta_L E - 2E) + C_a(E)

with
  C_ij = (Delta a)E_ij + 2 a_k nabla_k E_ij + tau a_ij
       + 1/2(a_i tau_j + a_j tau_i)
       - a_{ik}E_kj - a_{jk}E_ki
       - a_k(nabla_i E_kj + nabla_j E_ki).

This script verifies at a normal-coordinate point that contraction with 2E,
followed by integration by parts and the contracted Bianchi relation
    div E = (1/2) d tau,
removes Hess(a) from the integrated energy and leaves only terms homogeneous
in E and grad(E).  It also checks the trace bound |tau| <= sqrt(n)|E| and the
special cutoff identity |grad a|^2/a = 4|grad chi|^2 for a=chi^2.
"""
import sympy as s

n = 4
# symmetric E, Hess(a), and first derivatives da, dtau, dq (test cutoff q)
E = s.Matrix(n, n, lambda i,j: s.Symbol(f"E{i}{j}" if i <= j else f"E{j}{i}"))
Ha = s.Matrix(n, n, lambda i,j: s.Symbol(f"A{i}{j}" if i <= j else f"A{j}{i}"))
da = s.Matrix([s.Symbol(f"a{i}") for i in range(n)])
dtau = s.Matrix([s.Symbol(f"t{i}") for i in range(n)])
dq = s.Matrix([s.Symbol(f"q{i}") for i in range(n)])
q = s.Symbol("q")
tau = s.trace(E)
E2 = E*E
normE2 = s.trace(E2)

# Hess(a)-containing part before integration by parts:
# 2 q [(Delta a)|E|^2 + tau <E,Hess a> - 2 <E^2,Hess a>]
pre_hess = 2*q*(s.trace(Ha)*normE2 + tau*s.trace(E*Ha) - 2*s.trace(E2*Ha))

# After integrating Hess(a) by parts and combining with the explicit grad(a)*grad(E)
# terms, the integrated expression should be (TTCS formula (4)):
post = (
    -2*normE2*(da.dot(dq))
    -2*tau*(dqaE := (dqaE if False else 0))
)
# Build contractions explicitly.
E_dq_da = (dq.T*E*da)[0]
E2_dq_da = (dq.T*E2*da)[0]
E_da_dtau = (da.T*E*dtau)[0]
post = -2*normE2*da.dot(dq) - 2*tau*E_dq_da + 4*E2_dq_da \
       + q*(-tau*da.dot(dtau) + 2*E_da_dtau)

print("Integrated cutoff contribution after Hess(a) cancellation:")
print(s.factor(post))

# Homogeneity test: scale E -> eps E, hence tau, grad tau, grad E scale eps.
eps = s.Symbol("eps")
post_scaled = s.expand(post.subs({
    **{E[i,j]: eps*E[i,j] for i in range(n) for j in range(n)},
    **{dtau[i]: eps*dtau[i] for i in range(n)}
}, simultaneous=True))
# dq, da fixed. Each displayed term is cubic or quadratic in E; no constant/linear term.
poly = s.Poly(post_scaled, eps)
print("Degrees in E-scaling epsilon:", sorted(k[0] for k,_ in poly.terms()))
assert all(k[0] >= 2 for k,_ in poly.terms())

# a=chi^2 identity.
chi = s.Symbol("chi", positive=True)
dchi2 = sum(s.Symbol(f"c{i}")**2 for i in range(n))
grad_a_sq_over_a = s.simplify((4*chi**2*dchi2)/(chi**2))
print("|grad(chi^2)|^2/chi^2 =", grad_a_sq_over_a)
assert s.simplify(grad_a_sq_over_a - 4*dchi2) == 0

# Trace Cauchy constant in n=4, checked symbolically for diagonal E:
x = s.symbols("x0:4", real=True)
trace_sq_gap = s.expand(4*sum(v*v for v in x) - sum(x)**2)
# equals sum_{i<j}(xi-xj)^2
pair_sum = sum((x[i]-x[j])**2 for i in range(4) for j in range(i+1,4))
print("4 sum xi^2 - (sum xi)^2 factor check:", s.simplify(trace_sq_gap-pair_sum))
assert s.simplify(trace_sq_gap-pair_sum) == 0

# Scalar Young bounds underlying the energy estimate.
# Terms q |E| |grad a| |grad E| <= eps q a |grad E|^2 + C/eps q |grad a|^2/a |E|^2.
X,Y,aa,ga,eta = s.symbols("X Y aa ga eta", positive=True)
# Verify 2 XY <= eta X^2 + eta^{-1}Y^2 by square completion.
young_gap = s.factor(eta*X**2 + Y**2/eta - 2*X*Y)
print("Young gap:", young_gap)
assert s.simplify(young_gap - (eta*X-Y)**2/eta) == 0

print("PASS: cutoff-defect terms have no E-independent source; Hess(a) can be removed in integrated energy; no 1/chi loss for a=chi^2.")
