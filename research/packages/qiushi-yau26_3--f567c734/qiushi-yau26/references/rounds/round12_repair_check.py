"""Direct-coordinate check of the invariant collar Einstein constraint.

The local test includes nonzero S, H, electric F, magnetic F, and d_F a.
It does not check global Einstein existence or a general repair theorem.
Run with: qiushi-yau26 env numeric python round12_repair_check.py
"""

import sympy as s

a, ap, app = s.symbols("a ap app", positive=True)
u, up, upp, v, vp, vpp = s.symbols("u up upp v vp vpp", real=True)
z, zp, zpp, c, m, x = s.symbols("z zp zpp c m x", real=True)


def simp(expr):
    return s.factor(s.cancel(s.expand(expr)))


def diff(expr, index):
    if index == 0:
        return (ap*s.diff(expr, a)+app*s.diff(expr, ap)
                +up*s.diff(expr, u)+upp*s.diff(expr, up)
                +vp*s.diff(expr, v)+vpp*s.diff(expr, vp)
                +zp*s.diff(expr, z)+zpp*s.diff(expr, zp))
    if index == 2:
        # a(t,x)=A(t)e^(mx); ap and app carry the same spatial factor.
        return s.diff(expr, x)+m*(a*s.diff(expr, a)+ap*s.diff(expr, ap)+app*s.diff(expr, app))
    return s.S.Zero


# Coordinates are t, phi, x, y. h_t=e^(2u)dx²+e^(2v)dy².
# theta=dphi+z(t)dx+c*x*dy. Hence beta=zp*dx, B=c*dx^dy.
theta = s.Matrix([0, 1, z, c*x])
g = s.diag(1, 0, s.exp(2*u), s.exp(2*v)) + a*a*theta*theta.T
inverse = g.inv().applyfunc(simp)
gamma = [[[s.S.Zero for _ in range(4)] for _ in range(4)] for _ in range(4)]
for k in range(4):
    for i in range(4):
        for j in range(i, 4):
            gamma[k][i][j] = gamma[k][j][i] = simp(sum(
                inverse[k, l]*(diff(g[l, j], i)+diff(g[l, i], j)-diff(g[i, j], l))
                for l in range(4))/2)


def ricci(i, j):
    return simp(sum(diff(gamma[k][i][j], k)-diff(gamma[k][i][k], j)
        +sum(gamma[k][i][j]*gamma[l][k][l]-gamma[l][i][k]*gamma[k][j][l]
             for l in range(4)) for k in range(4)))


rho_u = simp(ricci(1, 1)/(a*a))
rho_t = ricci(0, 0)
beta_sq = zp*zp*s.exp(-2*u)
b_tensor_sq = 2*c*c*s.exp(-2*u-2*v)
laplace_ratio = m*m*s.exp(-2*u)
H = up+vp
S_sq = up*up+vp*vp
expected_u = -(app+H*ap)/a-laplace_ratio+a*a*(2*beta_sq+b_tensor_sq)/4
expected_t = -upp-vpp-S_sq-app/a-a*a*beta_sq/2
assert simp(rho_u-expected_u) == 0
assert simp(rho_t-expected_t) == 0
expected_D = upp+vpp-ap*H/a+S_sq-laplace_ratio+a*a*(beta_sq+b_tensor_sq/4)
assert simp(rho_u-rho_t-expected_D) == 0
print("PASS: coordinate Ric(U,U), Ric(T,T), and full difference identity")

# Explicit negative controls: neither the magnetic coefficient nor spatial
# Laplacian nor H term can be omitted.
assert simp((rho_u-rho_t)-(expected_D+a*a*b_tensor_sq/4)) != 0
assert simp((rho_u-rho_t)-(expected_D+laplace_ratio)) != 0
assert simp((rho_u-rho_t)-(expected_D+ap*H/a)) != 0
print("PASS: three wrong magnetic/Laplacian/trace formulas rejected")

# The scalar receiver is exact, not only a leading-order calculation.
weighted_H_derivative = (upp+vpp)/a-ap*H/(a*a)
positive_source = S_sq/a+a*(beta_sq+b_tensor_sq/4)
assert simp(weighted_H_derivative+positive_source
            -(expected_D+laplace_ratio)/a) == 0
print("PASS: weighted nonlinear receiver identity")

# Cosh collar integral and exact cancellation of the shrinking endpoint radius.
t, k, cc, LL = s.symbols("t k cc LL", positive=True)
radius = cc*s.cosh(k*t)
primitive = cc*s.sinh(k*t)/k
assert s.simplify(s.diff(primitive, t)-radius) == 0
I_a = 2*cc*s.sinh(k*LL)/k
A = cc*s.cosh(k*LL)
assert s.simplify(I_a/A-2*s.tanh(k*LL)/k) == 0
Lambda, eta = s.symbols("Lambda eta", positive=True)
bound = (Lambda*2*A/k)*(2*Lambda*eta/A)
assert s.simplify(bound-4*Lambda**2*eta/k) == 0
print("PASS: endpoint radius cancels in the Teichmueller repair estimate")

# Beta=a^-3 b/I3 satisfies the Maxwell transport equation for fixed h.
Qcharge = s.symbols("Qcharge", real=True)
beta_profile = Qcharge/a**3
assert s.simplify(diff(a**3*beta_profile, 0)) == 0
# Exact elementary integrals after z=tanh(kt).
zz = s.symbols("zz", real=True)
sech3_integral = s.integrate(s.sqrt(1-zz**2), (zz, -1, 1))
sech5_integral = s.integrate((1-zz**2)**s.Rational(3, 2), (zz, -1, 1))
assert s.simplify(sech3_integral-s.pi/2) == 0
assert s.simplify(sech5_integral-3*s.pi/8) == 0
ratio = (sech5_integral/(k*cc**5))/(sech3_integral/(k*cc**3))**2
assert s.simplify(ratio-3*k*cc/(2*s.pi)) == 0
print("PASS: conserved Maxwell flux and collapsed shear energy coefficient")
print("All local symbolic checks passed; global scope remains as in round12_repair.md.")
