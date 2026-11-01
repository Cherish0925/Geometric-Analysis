"""Compute the neck Ricci tensor directly from coordinate Christoffels.

This is independent of using the conformal Ricci transformation as an input.
It checks a local model, not the global collar or monopole existence.
"""
import sympy as s

t, theta, x, y = s.symbols("t theta x y", real=True)
ell = s.symbols("ell", positive=True)
coords = (t, theta, x, y)
f = s.Function("f")(t)
metric = s.diag(s.exp(2*f), s.exp(2*f)*ell**2*s.cosh(t)**2,
                s.exp(2*f), s.exp(2*f+2*x))
inv = s.diag(*[1/metric[i,i] for i in range(4)])
gamma = [[[s.simplify(sum(inv[k,l]*(s.diff(metric[l,j],coords[i])
              +s.diff(metric[l,i],coords[j])-s.diff(metric[i,j],coords[l]))/2
               for l in range(4)))
            for j in range(4)] for i in range(4)] for k in range(4)]
ric = s.zeros(4)
for i in range(4):
    for j in range(4):
        ric[i,j] = s.simplify(sum(
            s.diff(gamma[k][i][j],coords[k])-s.diff(gamma[k][i][k],coords[j])
            +sum(gamma[k][i][j]*gamma[l][k][l]
                 -gamma[l][i][k]*gamma[k][j][l] for l in range(4))
            for k in range(4)))
fp, fpp = s.diff(f,t), s.diff(f,t,2)
predicted = s.diag(-1-3*fpp-s.tanh(t)*fp,
    ell**2*s.cosh(t)**2*(-1-fpp-3*s.tanh(t)*fp-2*fp**2),
    -1-fpp-s.tanh(t)*fp-2*fp**2,
    s.exp(2*x)*(-1-fpp-s.tanh(t)*fp-2*fp**2))
for i in range(4):
    for j in range(i,4):
        assert s.simplify(s.expand_trig(ric[i,j]-predicted[i,j])) == 0, (i,j)
scalar = s.simplify(sum(inv[i,i]*ric[i,i] for i in range(4)))
residual = scalar-s.exp(-2*f)*(-4-6*fpp-6*s.tanh(t)*fp-6*fp**2)
assert s.simplify(s.expand_trig(residual).rewrite(s.exp)) == 0, residual
print("PASS: 10 independent symmetric Ricci components and scalar trace.")
