"""Exact m=2 coefficient check for the homogeneous torsion-zero identity.

For f_2(z,zbar)=z h(zbar)+Q(zbar,zbar), compute over Q the ten
coefficients in the four real source variables of

    ||A||^2-||S||^2-8|h|^2-6 Re sum_i conjugate(f_i) dbar_i h.

The script records exact ranks, the spatial trace identity, and the restriction
to a smooth zero surface tangent to {z2=0}.  It is an exact companion to the
floating span comparison in spirit_step64_homogeneous_quadric_check.py.
"""
from pathlib import Path
import json
import sympy as sp

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / "data" / "step65"
OUT.mkdir(parents=True, exist_ok=True)

# Eight complex intrinsic coefficients, represented by 16 real variables.
names = ["d1", "d2", "Q11_1", "Q11_2", "Q12_1", "Q12_2", "Q22_1", "Q22_2"]
r = sp.symbols(" ".join(n + "r" for n in names), real=True)
i = sp.symbols(" ".join(n + "i" for n in names), real=True)
c = [r[k] + sp.I*i[k] for k in range(8)]
d1, d2, q111, q112, q121, q122, q221, q222 = c
x = sp.symbols("x0:4", real=True)
z = sp.Matrix([x[0] + sp.I*x[1], x[2] + sp.I*x[3]])
w = sp.conjugate(z)
delta = sp.Matrix([d1, d2])

# Q[a,b,t], symmetric in a,b.
Q = [[[sp.S.Zero for _ in range(2)] for _ in range(2)] for _ in range(2)]
Q[0][0] = [q111, q112]
Q[0][1] = Q[1][0] = [q121, q122]
Q[1][1] = [q221, q222]

h = (delta.T*w)[0]
f = sp.Matrix([
    z[t]*h + sum(Q[a][b][t]*w[a]*w[b] for a in range(2) for b in range(2))
    for t in range(2)
])
B = sp.Matrix(2, 2, lambda t, b:
              z[t]*delta[b] + 2*sum(Q[a][b][t]*w[a] for a in range(2)))
A = (B-B.T)/2
S = (B+B.T)/2
norm2 = lambda M: sp.expand(sum(sp.conjugate(v)*v for v in M))
source = sp.re(sum(sp.conjugate(f[t])*delta[t] for t in range(2)))
H = sp.expand(norm2(A)-norm2(S)-8*sp.conjugate(h)*h-6*source)
H = sp.expand_complex(H)
px = sp.Poly(H, *x)
pairs = [(a,b) for a in range(4) for b in range(a,4)]
coeff = []
for a,b in pairs:
    ex = [0]*4
    ex[a] += 1
    ex[b] += 1
    coeff.append(sp.factor(px.coeff_monomial(tuple(ex))))
assert all(sum(m) == 2 for m in px.monoms())

# Convert each quadratic in the 16 real intrinsic variables to a symmetric matrix.
y = list(r)+list(i)
def qmatrix(poly, vars_):
    return sp.hessian(poly, vars_)/2
Mats = [qmatrix(q, y) for q in coeff]
flat = sp.Matrix([[M[a,b] for a in range(16) for b in range(16)] for M in Mats])
rank_all = flat.rank()

# Spatial trace and invariant scalar.
trace = sp.factor(sum(coeff[k] for k,(a,b) in enumerate(pairs) if a == b))
Qnorm = (abs(q111)**2 + abs(q112)**2 + 2*abs(q121)**2 +
         2*abs(q122)**2 + abs(q221)**2 + abs(q222)**2)
P1 = q121-q112
P2 = q221-q122
scalar = sp.expand_complex(Qnorm-abs(P1)**2-abs(P2)**2+sp.Rational(15,4)*(abs(d1)**2+abs(d2)**2))
trace_residual = sp.simplify(trace+8*scalar)

# Surface conditions d1=Q11_1=Q11_2=Q12_2=0.
zero_complex = [d1, q111, q112, q122]
subs_surface = {}
for v in zero_complex:
    subs_surface[sp.re(v)] = 0
    subs_surface[sp.im(v)] = 0
# Explicit substitution in the underlying real variables is more reliable.
for idx in [0,2,3,5]:
    subs_surface[r[idx]] = 0
    subs_surface[i[idx]] = 0
coeff_surface = [sp.factor(q.subs(subs_surface)) for q in coeff]
keep_idx = [1,4,6,7, 9,12,14,15]
ykeep = [y[k] for k in keep_idx]
Msurf = [qmatrix(q, ykeep) for q in coeff_surface]
flat_surface = sp.Matrix([[M[a,b] for a in range(8) for b in range(8)] for M in Msurf])
rank_surface = flat_surface.rank()
trace_surface = sp.factor(trace.subs(subs_surface))
expected_surface = -8*(abs(q121)**2+abs(q222)**2+sp.Rational(15,4)*abs(d2)**2)
expected_surface = sp.expand_complex(expected_surface).subs(subs_surface)
surface_trace_residual = sp.simplify(trace_surface-expected_surface)

# The real zero locus on the surface follows from the negative sum of squares.
normal_form_free = [str(q221)]
forced_zero = [str(d2), str(q121), str(q222)]

out = {
    "identity": "||A||^2-||S||^2-8|h|^2-6 Re sum conj(f_i) dbar_i h",
    "source_pairs": pairs,
    "rank_ten_coefficient_quadrics_over_Q": rank_all,
    "spatial_trace": str(trace),
    "trace_plus_8_invariant_scalar": str(trace_residual),
    "surface_rank_over_Q": rank_surface,
    "surface_trace": str(trace_surface),
    "surface_trace_expected": str(expected_surface),
    "surface_trace_residual": str(surface_trace_residual),
    "surface_real_zero_consequence": {
        "forced_zero_complex_coefficients": forced_zero,
        "remaining_free_complex_coefficient": normal_form_free,
        "normal_form": "f2 = kappa*conjugate(z2)^2*e1"
    },
    "coefficient_polynomials": [str(q) for q in coeff]
}
path = OUT / "homogeneous_identity_m2_exact.json"
path.write_text(json.dumps(out, indent=2))
print(json.dumps({k:v for k,v in out.items() if k != "coefficient_polynomials"}, indent=2))
assert rank_all == 10
assert trace_residual == 0
assert rank_surface == 3
assert surface_trace_residual == 0
