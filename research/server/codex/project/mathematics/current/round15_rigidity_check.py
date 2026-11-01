#!/usr/bin/env python3
"""Exact algebra for the realizable product calibration.

No old checking functions are imported. These checks do not verify gauge
existence, Cheeger--Tian regularity, or global compactness.
"""

import sympy as s

rat = s.Rational
k, rho, V, D, P = s.symbols("k rho V D P", positive=True)
K, W1, W2, Fminus, moment2, moment4 = s.symbols(
    "K W1 W2 Fminus moment2 moment4", real=True
)
grad, exterior = s.symbols("grad exterior", real=True)


def check(name, expr):
    residue = s.factor(s.expand(expr))
    assert residue == 0, (name, residue)
    print("PASS:", name)


# Scalar identity: 16 D = 8 k W1 - W2 + 8 ||F^-||^2,
# with 4 K = 4 k W1-W2.
check("exact scalar excess decomposition",
      (8*k*W1-W2+8*Fminus).subs(W2,4*k*W1-4*K)
      -4*(K+k*W1+2*Fminus))

psi = s.Matrix([rho,0,0])
model = rho**2*s.eye(3)/(48*k)-psi*psi.T/(16*k)
assert model == s.diag(-rho**2/(24*k),rho**2/(48*k),rho**2/(48*k))
check("Kahler-model squared norm",
      s.trace(model*model)-rho**4/(384*k*k))
assert model.subs(rho,4*k) == s.diag(-2*k/3,k/3,k/3)

# Hodge + Chern--Weil elimination, retaining the Ricci source P.
weyl_energy = 2*k*k*V/3-D+P/4
weyl_pair = grad/2-exterior-2*k*moment2/3
R2 = weyl_energy+moment4/(384*k*k)+weyl_pair/(8*k)
amp_polynomial = (moment4-32*k*k*moment2+256*k**4*V)/(384*k*k)
check("exact Weyl remainder identity",
      R2+D+exterior/(8*k)-P/4-amp_polynomial-grad/(16*k))

t = s.symbols("t", nonnegative=True)
amp = (16*k*k-rho*rho)**2/(384*k*k)
check("amplitude bound nonnegative decomposition",
      (2*k*(4*k-rho)/3-amp).subs(rho,4*k*(1-t))
      -rat(2,3)*k*k*t*(4*(1-t)+t*t*(4-t)))
# Each displayed factor is nonnegative on 0<=t<=1.

check("retained nonnegative remainder terms",
      (K+2*k*W1/3-D).subs(K,4*D-k*W1-2*Fminus)
      -(3*D-k*W1/3-2*Fminus))

check("single Weyl-block constant",
      2*(P/4+3*D)+2*rat(8,3)*D-(P/2+rat(34,3)*D))
check("full curvature-operator constant",
      2*(P/2+rat(34,3)*D)+P/2-(rat(3,2)*P+rat(68,3)*D))
assert 8*rat(68,3) == rat(544,3)

# Independent first-jet contraction. The self-dual basis has exterior
# norm one; omega below has exterior norm sqrt(2).
omega=[]
for pairs in (((0,1,1),(2,3,1)),
              ((0,2,1),(3,1,1)),
              ((0,3,1),(1,2,1))):
    w=s.zeros(4)
    for i,j,sign in pairs:
        w[i,j],w[j,i]=sign,-sign
    omega.append(w)

cj=s.symbols("c0:4", real=True)
aj=s.symbols("a0:4", real=True)
bj=s.symbols("b0:4", real=True)
jets=[s.Matrix([cj[i],aj[i],bj[i]]) for i in range(4)]
dm=[psi.dot(v)*s.eye(3)/(24*k)
    -(psi*v.T+v*psi.T)/(16*k) for v in jets]
grad_model=sum(s.trace(v.T*v) for v in dm)
grad_psi=sum(v.dot(v) for v in jets)
grad_rho=sum(v*v for v in cj)
check("correctly scaled polynomial derivative",
      grad_model-rho*rho*grad_psi/(128*k*k)
      -rho*rho*grad_rho/(384*k*k))

J=s.MutableDenseNDimArray.zeros(4,4,4)
for j in range(4):
    for a in range(4):
        for b in range(4):
            J[j,a,b]=sum(dm[i][u,v]*omega[u][i,j]*omega[v][a,b]/2
                for i in range(4) for u in range(3) for v in range(3))
J2=sum(J[j,a,b]**2 for j in range(4)
       for a in range(4) for b in range(4))
nabla_form=[sum((jets[i][u]*omega[u] for u in range(3)),s.zeros(4))
            /s.sqrt(2) for i in range(4)]
dform=s.MutableDenseNDimArray.zeros(4,4,4)
for i in range(4):
    for j in range(4):
        for a in range(4):
            dform[i,j,a]=(nabla_form[i][j,a]+nabla_form[j][a,i]
                          +nabla_form[a][i,j])
dform2=sum(dform[i,j,a]**2 for i in range(4)
           for j in range(4) for a in range(4))/6
star=[sum(s.LeviCivita(i,j,a,b)*dform[i,j,a]
          for i in range(4) for j in range(4)
          for a in range(4))/6 for b in range(4)]
interior=[sum(cj[i]*rho*omega[0][i,j]/s.sqrt(2) for i in range(4))
          for j in range(4)]
cross=sum(interior[j]*star[j] for j in range(4))
check("full twelve-variable first-jet identity",
      grad_model-J2-rho*rho*(grad_psi-2*dform2)/(256*k*k)
      -rho*rho*grad_rho/(128*k*k)+rho*cross/(64*k*k))

# Weighted Hodge elimination produces all source terms in (17).
G,B,H,N,C=s.symbols("G B H N C", real=True)
jet_integral=G/(128*k*k)+N/(384*k*k)-(G-2*H)/(256*k*k)\
             -N/(128*k*k)+C/(64*k*k)
weighted=jet_integral.subs(G,2*H-B+4*C-2*N)
check("weighted self-test coefficients",
      weighted-(-B/(256*k*k)+H/(64*k*k)
                -5*N/(384*k*k)+C/(32*k*k)))
check("surviving algebraic source",
      -rho*rho*(-4*k*rho*rho/3+rho**4/(12*k))/(256*k*k)
      -rho**4*(16*k*k-rho*rho)/(3072*k**3))
assert (rho**4*(16*k*k-rho*rho)).subs(rho,4*k)==0

# Product model on Lambda+ plus Lambda-: rank-two curvature operator.
curv=s.diag(-k,0,0,-k,0,0)
check("full four-index product norm",4*s.trace(curv*curv)-8*k*k)

# Independent frame calculation for both closed pure-shear plane forms.
# C_i[:,j] are components of nabla_i e_j in an orthonormal frame.
q,b=s.symbols("q b",real=True)
conn=[s.zeros(4) for _ in range(4)]
conn[0][2,1],conn[0][1,2]=q,-q
conn[1][1,0],conn[1][0,1]=b,-b
conn[1][2,0],conn[1][0,2]=q,-q
conn[2][1,0],conn[2][0,1]=q,-q
for sign in (1,-1):
    form=s.zeros(4)
    form[0,1],form[1,0]=1,-1
    form[2,3],form[3,2]=sign,-sign
    derivatives=[-C.T*form-form*C for C in conn]
    energies=[s.trace(d.T*d)/2 for d in derivatives]
    assert [s.simplify(e) for e in energies]==[2*q*q,2*q*q,0,0]
    check(f"shear canonical energy, orientation {sign}",
          sum(energies)-4*q*q)

ell, Bbeta=s.symbols("ell Bbeta",positive=True)
volume_coefficient=s.sqrt(3)*Bbeta/(24*s.pi**3)
check("normalized cubic source",9*volume_coefficient
      -3*s.sqrt(3)*Bbeta/(8*s.pi**3))
print("All exact product-boundary checks passed.")
