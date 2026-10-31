#!/usr/bin/env python3
"""Cross-check of c1_ricci_slow.py with EXPLICIT a = a0 cosh u, b = ell cosh t (generic z(t), zeta(u)),
plus a second, independent route: Cartan structure equations (connection 1-forms solved from
d e^i = - omega^i_j ^ e^j, curvature 2-forms Omega = d omega + omega^omega), no Christoffel symbols."""
import sympy as sp
from sympy.diffgeom import Manifold, Patch, CoordSystem
t, th, u, s = sp.symbols('t theta u s', real=True)
a0, ell = sp.symbols('a0 ell', positive=True)
z = sp.Function('z')(t); zeta = sp.Function('zeta')(u)
a = a0*sp.cosh(u); b = ell*sp.cosh(t)
X = [t, th, u, s]; n = 4
w = z*sp.diff(zeta, u)

# ---------- Route B: Cartan.  Represent a 1-form by its coefficient list in (dt,dtheta,du,ds).
e = [sp.Matrix([1,0,0,0]), sp.Matrix([0,b,0,0]), sp.Matrix([0,0,1,0]), sp.Matrix([0,0,a*w,a])]
Emat = sp.Matrix.hstack(*e).T            # rows = coframe components
Einv = Emat.inv()                         # columns = frame vectors e_i in coordinates: e_i^mu = Einv[mu,i]
def d1(om):                               # exterior derivative of 1-form -> antisymmetric matrix (d om)_{mu nu}
    return sp.Matrix(n, n, lambda m_, n_: sp.diff(om[n_], X[m_]) - sp.diff(om[m_], X[n_]))
# structure coefficients: d e^i = (1/2) c^i_{jk} e^j ^ e^k  with c^i_{jk} = (d e^i)(e_j,e_k)
c = [[[sp.simplify(sum(d1(e[i])[m_, n_]*Einv[m_, j]*Einv[n_, k] for m_ in range(n) for n_ in range(n)))
       for k in range(n)] for j in range(n)] for i in range(n)]
# Levi-Civita connection in ON frame: omega_{ij}(e_k) = (1/2)( c^i_{jk}... ) standard formula:
# omega_{ij}(e_k) = 1/2 [ -c^i_{jk} ... ]  -> use  Gamma_{kij} = <nabla_{e_k} e_j, e_i> = 1/2( c^k_{ij} + c^j_{ik} - c^i_{jk} ) with sign conv. below
# Convention: [e_j,e_k] = -c^i_{jk} e_i  (since d e^i(e_j,e_k) = -e^i([e_j,e_k])).
def bracket_coeff(i, j, k): return -c[i][j][k]          # [e_j,e_k] = sum_i bracket_coeff(i,j,k) e_i
# Koszul: 2<nabla_{e_j} e_k, e_i> = <[e_j,e_k],e_i> - <[e_k,e_i],e_j> + <[e_i,e_j],e_k>
Gam = [[[sp.simplify((bracket_coeff(i,j,k) - bracket_coeff(j,k,i) + bracket_coeff(k,i,j))/2)
         for k in range(n)] for j in range(n)] for i in range(n)]   # Gam[i][j][k] = <nabla_{e_j} e_k, e_i>
def edir(f_, j):  # derivative of function along e_j
    return sum(Einv[m_, j]*sp.diff(f_, X[m_]) for m_ in range(n))
# Riemann in frame: R(e_k,e_l)e_j = nabla_k nabla_l e_j - nabla_l nabla_k e_j - nabla_{[e_k,e_l]} e_j
def Rm(i, j, k, l):
    val = edir(Gam[i][l][j], k) - edir(Gam[i][k][j], l)
    val += sum(Gam[i][k][m_]*Gam[m_][l][j] - Gam[i][l][m_]*Gam[m_][k][j] for m_ in range(n))
    val -= sum(bracket_coeff(m_, k, l)*Gam[i][m_][j] for m_ in range(n))
    return val
Ric = sp.Matrix(n, n, lambda j, l: sp.simplify(sum(Rm(i, j, i, l) for i in range(n))))
v = a*sp.diff(zeta,u)*sp.diff(z,t); jj = sp.tanh(u); kk = sp.tanh(t)
claimed = sp.Matrix([[-v**2/2,0,0,(sp.diff(v,u)+2*jj*v)/2],[0,0,0,0],[0,0,-v**2/2,-(sp.diff(v,t)+kk*v)/2],
                     [(sp.diff(v,u)+2*jj*v)/2,0,-(sp.diff(v,t)+kk*v)/2,v**2/2]])
res = (Ric + sp.eye(4) - claimed).applyfunc(lambda x_: sp.simplify(x_.rewrite(sp.exp)))
print("structure constants: de^1(e0,e1) =", c[1][0][1], " de^3(e2,e3) =", sp.simplify(c[3][2][3]), " de^3(e0,e2) =", sp.simplify(c[3][0][2]))
print("Cartan/Koszul route: Phi_ON - claimed ="); sp.pprint(res)
