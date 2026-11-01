"""Derive the exact Ricci tensor for the T^2-invariant diagonal 4-metric
    g = dt^2 + exp(2a(t,th))*dth^2 + exp(2b(t,th))*dx^2 + exp(2c(t,th))*dy^2
and write the Einstein equations Ric_g = -3g as a 2D PDE system in (t,theta).

Output: printed formulas and a JSON record.
"""
import sympy as sp
import json
from pathlib import Path

# Coordinates: 0=t, 1=theta, 2=x, 3=y
t, th = sp.symbols('t theta')
a = sp.Function('a')(t, th)
b = sp.Function('b')(t, th)
c = sp.Function('c')(t, th)

# Shorthand derivatives
at, bt, ct = a.diff(t), b.diff(t), c.diff(t)
att, btt, ctt = a.diff(t,2), b.diff(t,2), c.diff(t,2)
ath, bth, cth = a.diff(th), b.diff(th), c.diff(th)
athth, bthth, cthth = a.diff(th,2), b.diff(th,2), c.diff(th,2)
atth, btth, ctth = a.diff(t,th), b.diff(t,th), c.diff(t,th)

# Metric components  g_{ii}
g00 = sp.Integer(1)
g11 = sp.exp(2*a)
g22 = sp.exp(2*b)
g33 = sp.exp(2*c)

diag = [g00, g11, g22, g33]
diag_inv = [1/g for g in diag]

# Non-zero Christoffel symbols Gamma^k_{ij}
# We'll compute directly from the diagonal metric formula:
# For diagonal metric: Gamma^k_{ij} = 0 unless (k=i=j), (k=j,i!=j), (k=i,j!=i with k!=j)
# specifically: Gamma^i_{ij} = (1/2) g^{ii} dg_{ii}/dx^j  (no sum)
#               Gamma^k_{ii} = -(1/2) g^{kk} dg_{ii}/dx^k  (k!=i)
# Everything zero otherwise.

coords = [t, th]  # Only t and th have derivatives
ncoords = 4

# Build Christoffel tensor symbolically
Gamma = [[[sp.Integer(0) for _ in range(ncoords)] for _ in range(ncoords)] for _ in range(ncoords)]

# Derivative of g_{ii} w.r.t. coordinate j (j = 0->t, 1->th)
def dg(i, j):
    """d(g_{ii})/d(coords[j])"""
    return diag[i].diff(coords[j])

# Gamma^i_{ij} = (1/(2 g_{ii})) * dg_{ii}/dx^j  (i,j both in {0,1,2,3})
# Gamma^k_{ii} = -(1/(2 g_{kk})) * dg_{ii}/dx^k  (k != i)
# Only j = 0 (t) and j = 1 (th) give nonzero derivatives.

# But we need 4x4 Christoffel; coords x,y have no derivatives.
# The only nonzero Gamma^k_{ij} involve at least one of {0,1} as an index.
# Let me compute the 4D Ricci from scratch carefully.

# For the diagonal metric g = diag(1, e^{2a}, e^{2b}, e^{2c}),
# with a,b,c functions of (t=x^0, theta=x^1) only, the Ricci tensor has
# the following nonzero components (by direct computation or e.g. Besse):

# R_{00} = -(a_{tt} + b_{tt} + c_{tt}) - (a_t^2 + b_t^2 + c_t^2)
R00 = -(att + btt + ctt) - (at**2 + bt**2 + ct**2)

# R_{11} = -(e^{2a} * a_{tt} + a_t*(a_t+b_t+c_t)*e^{2a})
#          -a_{thth} - a_th*(b_th+c_th)
#          + e^{-2a}*(b_th^2 + c_th^2)   -- wait, this needs care
# Let me use the standard warped-product formula more carefully.

# Actually, let's just compute Ricci directly from Christoffels.
# For g = diag(1, e^{2a}, e^{2b}, e^{2c}):

# Non-zero Christoffel symbols (using x^0=t, x^1=th, x^2=x, x^3=y):
# Group 1: Gamma^0_{ij} (upper index t)
#   Gamma^0_{11} = -g^{00} * (1/2)*dg_{11}/dt = -e^{2a}*a_t
#   Gamma^0_{22} = -e^{2b}*b_t
#   Gamma^0_{33} = -e^{2c}*c_t
# Group 2: Gamma^1_{ij} (upper index th)
#   Gamma^1_{01} = Gamma^1_{10} = a_t (= (1/2)*g^{11}*dg_{11}/dt)
#   Gamma^1_{11} = a_th (= (1/2)*g^{11}*dg_{11}/dth)
#   Gamma^1_{22} = -e^{2(b-a)}*b_th (= -(1/2)*g^{11}*dg_{22}/dth)
#   Gamma^1_{33} = -e^{2(c-a)}*c_th
# Group 3: Gamma^2_{ij} (upper index x)
#   Gamma^2_{02} = b_t,  Gamma^2_{12} = b_th
# Group 4: Gamma^3_{ij}
#   Gamma^3_{03} = c_t,  Gamma^3_{13} = c_th

print("Computing 4D Ricci tensor for T^2-invariant diagonal metric...")
print("g = dt^2 + e^{2a} dth^2 + e^{2b} dx^2 + e^{2c} dy^2\n")

# Store Christoffel symbols in a dict for sparse access
Chr = {}
# Group 0
Chr[(0,1,1)] = -sp.exp(2*a)*at
Chr[(0,2,2)] = -sp.exp(2*b)*bt
Chr[(0,3,3)] = -sp.exp(2*c)*ct
# Group 1
Chr[(1,0,1)] = at; Chr[(1,1,0)] = at
Chr[(1,1,1)] = ath
Chr[(1,2,2)] = -sp.exp(2*(b-a))*bth
Chr[(1,3,3)] = -sp.exp(2*(c-a))*cth
# Group 2
Chr[(2,0,2)] = bt; Chr[(2,2,0)] = bt
Chr[(2,1,2)] = bth; Chr[(2,2,1)] = bth
# Group 3
Chr[(3,0,3)] = ct; Chr[(3,3,0)] = ct
Chr[(3,1,3)] = cth; Chr[(3,3,1)] = cth

def get_chr(k,i,j):
    return Chr.get((k,i,j), sp.Integer(0))

# Ricci_{mu nu} = partial_rho Gamma^rho_{mu nu}
#               - partial_nu Gamma^rho_{mu rho}
#               + Gamma^rho_{rho lambda} Gamma^lambda_{mu nu}
#               - Gamma^rho_{nu lambda} Gamma^lambda_{mu rho}
# Only rho, lambda in {0,1,2,3}; but partials only w.r.t. t,th (indices 0,1).

def ricci_component(mu, nu):
    """Compute R_{mu nu}."""
    result = sp.Integer(0)
    for rho in range(4):
        G_rho_mu_nu = get_chr(rho, mu, nu)
        # partial_rho of Gamma^rho_{mu nu}: only rho=0 or 1 give derivatives
        if rho <= 1:
            result += G_rho_mu_nu.diff(coords[rho])
        # -partial_nu of Gamma^rho_{mu rho}
        G_rho_mu_rho = get_chr(rho, mu, rho)
        if nu <= 1:
            result -= G_rho_mu_rho.diff(coords[nu])
        # Gamma^rho_{rho lambda} Gamma^lambda_{mu nu}
        for lam in range(4):
            result += get_chr(rho, rho, lam) * get_chr(lam, mu, nu)
            result -= get_chr(rho, nu, lam) * get_chr(lam, mu, rho)
    return sp.expand(result)

# Compute the distinct nonzero components
print("=== Ricci components ===")
ric = {}
for mu in range(4):
    for nu in range(mu, 4):
        r = ricci_component(mu, nu)
        r = sp.simplify(r)
        if r != 0:
            ric[(mu,nu)] = r
            label = f"R_{{{mu}{nu}}}"
            print(f"\n{label} = {r}")

# Now form the Einstein equations: R_{mu nu} + 3 g_{mu nu} = 0
print("\n\n=== Einstein equations E_{mu nu} = R_{mu nu} + 3 g_{mu nu} = 0 ===")
ein = {}
for (mu,nu), r in ric.items():
    gval = diag[mu] if mu == nu else sp.Integer(0)
    e = r + 3*gval
    ein[(mu,nu)] = sp.simplify(e)
    print(f"\nE_{{{mu}{nu}}} = {ein[(mu,nu)]}")

# Also compute for the orthonormal frame: E^hat_{ij} = g^{ii} E_{ij}
print("\n\n=== Orthonormal Einstein defect E^hat ===")
for (mu,nu), e in ein.items():
    factor = diag_inv[mu] if mu == nu else sp.sqrt(diag_inv[mu]*diag_inv[nu])
    ehat = sp.simplify(factor * e)
    print(f"\nE^hat_{{{mu}{nu}}} = {ehat}")

# Verify: at the exact hyperbolic cusp a=0, b=t, c=t, all E should vanish
print("\n\n=== Verification: exact hyperbolic cusp a=0, b=t, c=t ===")
for (mu,nu), e in ein.items():
    val = e.subs([(a, sp.Integer(0)), (b, t), (c, t)])
    val = sp.simplify(val)
    print(f"E_{{{mu}{nu}}} at cusp = {val}")

# Verify: round S^3 cusp a=t, b=t, c=t
print("\n=== Verification: round cusp a=t, b=t, c=t ===")
for (mu,nu), e in ein.items():
    val = e.subs([(a, t), (b, t), (c, t)])
    val = sp.simplify(val)
    print(f"E_{{{mu}{nu}}} at round cusp = {val}")

# Save summary
path = Path(__file__).resolve().parents[1]/'data'/'step70_ricci_T2inv.json'
summary = {
    'description': 'Exact Ricci for T^2-inv diagonal 4-metric',
    'metric': 'g = dt^2 + e^{2a} dth^2 + e^{2b} dx^2 + e^{2c} dy^2',
    'Ricci_components': {f"R_{{{mu}{nu}}}": str(r) for (mu,nu),r in ric.items()},
    'Einstein_equations': {f"E_{{{mu}{nu}}}": str(e) for (mu,nu),e in ein.items()},
}
path.write_text(json.dumps(summary, indent=2), encoding='utf-8')
print(f"\nWrote {path}")
