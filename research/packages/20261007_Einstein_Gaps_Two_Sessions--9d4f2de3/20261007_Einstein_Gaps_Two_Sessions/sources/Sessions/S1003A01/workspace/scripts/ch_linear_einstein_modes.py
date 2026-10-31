"""Linearized diagonal Bianchi-IX Einstein modes on complex hyperbolic space (Ric=-6g).

Conventions (Step 7): g=dt^2+a1^2 s1^2+a2^2 s2^2+a3^2 s3^2, d s_i=2 s_j^s_k,
  u_i = a_i' - (a_j^2+a_k^2-a_i^2)/(a_j a_k),  H_i=u_i+u_j u_k/2,
  r_i = u_i'/a_i,  v_i = 2H_i/(a_j a_k),  z_i=r_i-v_i  (|Ric0|^2=sum z_i^2),  s=-2 sum(r_i+v_i).
CH: a1=a3=A=sinh t, a2=B=sinh t cosh t, x=A^2=sinh^2 t, u=(0,3x,0).

Sectors (exchange a1<->a3 is a symmetry of CH):
  antisymmetric: a1=A e^{th/2}, a3=A e^{-th/2}, a2=B          -> variables v_-=du1-du3, theta
  symmetric:     a1=a3=A e^{sig}, a2=B e^{bet}                -> U(2)-invariant (Kahler/longitudinal + v_+)
Output: the linear operators, a check of the Step-7 torsion relation
  d/dx[(x/(1+x))^2 theta] = (1/2) f_- v_-,   f_-=x/(1+x)^{5/2},
and the explicit decaying 'mass' mode of each sector with dz=0, ds=0.
"""
import sympy as sp

t, eps = sp.symbols('t epsilon', positive=True)
x = sp.symbols('x', positive=True)
A = sp.sinh(t); B = sp.sinh(t)*sp.cosh(t)


def curvature(a):
    a1, a2, a3 = a
    idx = [(0, 1, 2), (1, 2, 0), (2, 0, 1)]
    u = [sp.diff(a[i], t) - (a[j]**2 + a[k]**2 - a[i]**2)/(a[j]*a[k]) for i, j, k in idx]
    H = [u[i] + u[j]*u[k]/2 for i, j, k in idx]
    r = [sp.diff(u[i], t)/a[i] for i, j, k in idx]
    v = [2*H[i]/(a[j]*a[k]) for i, j, k in idx]
    z = [r[i] - v[i] for i in range(3)]
    s = -2*sum(r[i] + v[i] for i in range(3))
    return u, z, s


def lin(expr):
    return sp.simplify(sp.diff(expr, eps).subs(eps, 0))


to_x = {sp.sinh(t): sp.sqrt(x), sp.cosh(t): sp.sqrt(1 + x)}

out = {}
# background check
u0, z0, s0 = curvature([A, B, A])
out['background'] = dict(z=[sp.simplify(zz) for zz in z0], s=sp.simplify(s0),
                         u=[sp.simplify(uu.rewrite(sp.exp)) for uu in u0])

# ---------------- antisymmetric sector ----------------
th = sp.Function('theta')(t)
uA, zA, sA = curvature([A*sp.exp(eps*th/2), B, A*sp.exp(-eps*th/2)])
du = [lin(e) for e in uA]
dz = [lin(e) for e in zA]
ds = lin(sA)
vminus = sp.simplify(du[0] - du[2])
out['anti'] = dict(du=du, dz=dz, ds=ds, vminus=vminus)
# torsion relation check, written in t: dx/dt = 2 sqrt(x(1+x)) = 2 sinh cosh
k = (sp.tanh(t))**4             # (x/(1+x))^2
fminus = sp.sinh(t)/sp.cosh(t)**5   # x/(1+x)^{5/2} = sinh^2/cosh^5 ... careful
fminus = sp.sinh(t)**2/sp.cosh(t)**5
lhs = sp.diff(k*th, t)/(2*sp.sinh(t)*sp.cosh(t))
rhs = sp.Rational(1, 2)*fminus*vminus
out['anti']['torsion_relation_residual'] = sp.simplify(lhs - rhs)

# ---------------- symmetric sector ----------------
sg = sp.Function('sigma')(t); bt = sp.Function('beta')(t)
uS, zS, sS = curvature([A*sp.exp(eps*sg), B*sp.exp(eps*bt), A*sp.exp(eps*sg)])
duS = [lin(e) for e in uS]; dzS = [lin(e) for e in zS]; dsS = lin(sS)
out['sym'] = dict(du=duS, dz=dzS, ds=dsS)

if __name__ == '__main__':
    for sec, d in out.items():
        print('=====', sec)
        for kk, vv in d.items():
            print(kk, ':', vv)
