#!/usr/bin/env python3
"""Exact local and scaling checks; not certification of the global PDE proof."""
from itertools import product
import json
import sympy as s

x, y = s.symbols("x y", real=True, positive=True)
coords = (x, y)
Gamma = [[[s.S.Zero for _ in range(2)] for _ in range(2)] for _ in range(2)]
Gamma[0][0][1] = Gamma[0][1][0] = -1/y
Gamma[1][0][0], Gamma[1][1][1] = 1/y, -1/y


def covder(tensor):
    """Covariant derivative of a covariant tensor, derivative slot first."""
    rank = len(next(iter(tensor)))
    result = {}
    for a in range(2):
        for inds in product(range(2), repeat=rank):
            expression = s.diff(tensor[inds], coords[a])
            for slot, index in enumerate(inds):
                for p in range(2):
                    replaced = inds[:slot] + (p,) + inds[slot+1:]
                    expression -= Gamma[p][a][index]*tensor[replaced]
            result[(a,)+inds] = s.simplify(expression)
    return result


def rough(tensor):
    twice = covder(covder(tensor))
    return {inds: s.simplify(-y*y*sum(twice[(a,a)+inds] for a in range(2)))
            for inds in tensor}


def divergence(tensor):
    first = covder(tensor)
    return {(j,): s.simplify(-y*y*sum(first[(a,a,j)] for a in range(2)))
            for j in range(2)}


def conformal_killing(alpha):
    first = covder(alpha)
    sym = {(i,j): (first[(i,j)]+first[(j,i)])/2 for i,j in product(range(2), repeat=2)}
    euclidean_trace = sym[(0,0)]+sym[(1,1)]
    return {(i,j): s.simplify(value-(euclidean_trace/2 if i == j else 0))
            for (i,j), value in sym.items()}


def einstein_surface(tensor):
    lap = rough(tensor)
    euclidean_trace = tensor[(0,0)]+tensor[(1,1)]
    return {(i,j): s.simplify(lap[(i,j)]/2-tensor[(i,j)]
                  +(euclidean_trace if i == j else 0))
            for i,j in tensor}


alpha = {(0,): s.Function("a")(x,y), (1,): s.Function("b")(x,y)}
Dalpha = conformal_killing(alpha)
rough_alpha = rough(alpha)
Aalpha = {i: s.simplify((rough_alpha[i]+alpha[i])/2) for i in alpha}
assert all(s.simplify(divergence(Dalpha)[i]-Aalpha[i]) == 0 for i in alpha)
assert all(s.simplify(einstein_surface(Dalpha)[i]-conformal_killing(Aalpha)[i]) == 0
           for i in Dalpha)

p, q = s.Function("p")(x,y), s.Function("q")(x,y)
tracefree = {(0,0): p, (0,1): q, (1,0): q, (1,1): -p}
assert all(s.simplify(einstein_surface(tracefree)[i]
                      -conformal_killing(divergence(tracefree))[i]) == 0 for i in tracefree)

z, omega = s.symbols("z omega", real=True)
# Nonnegative Laplacian: Delta F(z)=F'(z) Delta z-F''(z)|dz|^2.
assert s.simplify(-s.diff(s.cos(omega*z),z,2)-omega**2*s.cos(omega*z)) == 0

# Deck-orbit mean is zero: (1-r)(1+...+r^(m-1))=1-r^m.
r = s.symbols("r")
for m in range(2,41):
    assert s.expand((1-r)*sum(r**j for j in range(m))-(1-r**m)) == 0

# Multiplication by a positive weight does not preserve the mean-zero space.
a, theta = s.symbols("a theta", real=True)
mean = s.integrate((1+a*s.cos(theta))*s.cos(theta), (theta,0,2*s.pi))/(2*s.pi)
assert s.simplify(mean-a/2) == 0

# m^-2 amplitude, m^-4 residual and the obstruction to exponent >1/2.
m, eps0, exponent = s.symbols("m eps0 exponent", positive=True)
t = eps0/m**2
assert s.simplify(t/m**2+t**2-(eps0+eps0**2)/m**4) == 0
assert s.simplify((m**(-2)/(m**(-4))**exponent)/m**(4*exponent-2)) == 1

print(json.dumps({
    "scope": "exact coordinate identities and finite algebra only; not PDE or topology verification",
    "checks_passed": 7,
    "surface_operator": "L(D alpha)=D((rough+1)alpha/2), curvature -1",
    "surface_TT_identity": "L=D delta on trace-free tensors",
    "cyclic_mode": "Delta cos(omega z)=omega^2 |dz|^2 cos(omega z) when Delta z=0",
    "localization_negative_control": "mean((1+a cos(theta))*cos(theta))=a/2",
    "nonlinear_scales": "distance m^-2, residual m^-4"
}, indent=2))
