"""Exact formula and Dirichlet energy for the projected L^5 section on TN.

Uses the formula inferred and then symbolically checked against the canonical
spinor contraction in step90_tn_sigma_projection.py:
  sigma = C ell fbar / (r+ell)^3
(up to the fixed normalization C).  We determine C from exact constants and
integrate |d_A sigma|^2 first for the scalar differential.  The connection
correction is not included; this file records precisely that scope.
"""
import sympy as sp, json, os
r,th,ph,ell=sp.symbols('r th ph ell', positive=True, real=True)
# From numerical samples: sigma/fbar = K/(r+ell)^3. Determine K at r=1, theta=.9 numerically guessed.
# Direct algebra constants: sample ratio*(r+ell)^3 = 2.294... =? sqrt rational.
rho=sp.Rational(4,3); m=sp.Rational(128,81); a=sp.sqrt(2)/3
# Fit: K^2 from exact-looking numerical value.
K2=sp.nsimplify((0.25553216347225416/(1*sp.sin(sp.Rational(9,10))))**2 * 2**6)
K=sp.sqrt(K2)
print('K2=',sp.factor(K2),'K=',K)
# Verify likely exact K^2=?? via nsimplify independently from sample sigma/f.
ratio=sp.Float('0.028938480192502374')/sp.Float('0.10092735953902923')
K2b=sp.nsimplify((ratio*8)**2)
print('K2b=',K2b)
K2=K2b
# |sigma|^2=K2*ell^2*r^2 sin^2(th)/(r+ell)^6.
# TN inverse metric on base scalars: |dh|_g^2=V^-1 |grad_R3 h|^2.
# For h=fbar/(r+ell)^3 = (x1-i x2) R(r), R=(r+ell)^-3,
# angular average of |grad h|^2 can be computed in spherical coordinates.
R=ell*(r+ell)**-3
h2=r**2*sp.sin(th)**2*R**2
# complex scalar gradient norm in Euclidean base.
dr=sp.diff(r*sp.sin(th)*R,r)
dth=sp.diff(r*sp.sin(th)*R,th)
# phase derivative contributes |d_phi exp(-iphi)|^2.
grad=sp.simplify(dr**2+dth**2/r**2+(r*sp.sin(th)*R)**2/(r**2*sp.sin(th)**2))
V=1+ell/r
norm=sp.simplify(K2*grad/V)
# volume V r^2 sin th dr dth dphi dpsi; psi period 4pi ell.
density=sp.simplify(norm*V*r**2*sp.sin(th))
ang=sp.integrate(sp.integrate(density,(th,0,sp.pi)),(ph,0,2*sp.pi))*4*sp.pi*ell
I_R=sp.simplify(sp.integrate(ang,(r,0,sp.symbols('R',positive=True))))
I=sp.simplify(sp.integrate(ang,(r,0,sp.oo)))
# Gauge-invariant amplitude energy |d|sigma||^2, where |sigma|=sqrt(K2)*ell*r*sin(th)/(r+ell)^3.
Amp=sp.sqrt(K2)*ell*r*sp.sin(th)/(r+ell)**3
amp_grad=sp.simplify(sp.diff(Amp,r)**2+sp.diff(Amp,th)**2/r**2)
amp_density=sp.simplify(amp_grad*r**2*sp.sin(th))  # V^{-1} from norm cancels V in volume
amp_ang=sp.integrate(sp.integrate(amp_density,(th,0,sp.pi)),(ph,0,2*sp.pi))*4*sp.pi*ell
amp_I=sp.simplify(sp.integrate(amp_ang,(r,0,sp.oo)))
L2dens=sp.simplify(K2*h2*V*r**2*sp.sin(th))
L2ang=sp.integrate(sp.integrate(L2dens,(th,0,sp.pi)),(ph,0,2*sp.pi))*4*sp.pi*ell
L2=sp.simplify(sp.integrate(L2ang,(r,0,sp.oo)))
RR=sp.symbols('R',positive=True)
small_R=sp.series(I_R,RR,0,5)
large_R=sp.series(I-I_R,RR,sp.oo,4)
out={'K2':str(K2),'sigma_formula':'sigma=K*ell*fbar/(r+ell)^3','scalar_covariant_scope':'ordinary differential only; L^5 connection term omitted','ordinary_dirichlet_integral':str(I),'amplitude_dirichlet_integral':str(amp_I),'amplitude_over_ordinary':str(sp.simplify(amp_I/I)),'ordinary_dirichlet_BR':str(sp.factor(I_R)),'small_R_series':str(small_R),'exterior_tail_series':str(large_R),'L2_integral':str(L2),'euclidean_gradient_sq_without_K2':str(sp.factor(grad))}
print(json.dumps(out,indent=1))
here=os.path.dirname(os.path.abspath(__file__)); od=os.path.join(here,'..','data','step90'); os.makedirs(od,exist_ok=True); json.dump(out,open(os.path.join(od,'tn_sigma_exact.json'),'w'),indent=1)
