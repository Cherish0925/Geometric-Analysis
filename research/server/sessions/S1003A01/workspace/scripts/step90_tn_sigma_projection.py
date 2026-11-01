"""Step 90: projected charge-five line section on the exact Taub--NUT core.

This tests whether the full second-derivative cost found in Step 47 survives the
specific contraction sigma = Phi wedge t(v).  We use the canonical Kahler
spinor realization S+ = Lambda^{0,0} + Lambda^{0,2}, S- = Lambda^{0,1}
for the hyperkahler complex structure I3.  The positive frame (1,bar theta1
wedge bar theta2) is parallel.  Clifford multiplication is implemented on
Lambda^{0,*}; its overall normalization is checked by reconstructing the exact
Step-47 cubic torsion t(Phi)=sqrt(2) rho_* a dbar f.

The script first samples sigma on general points, identifies its equivariant
form, and evaluates radial/angular scalings.  It writes a JSON record; the
scientific interpretation belongs in the companion Step-90 note.
"""
import json, os
import numpy as np
import sympy as sp

# Exterior algebra Lambda^{0,*} with ordered basis [1,e1,e2,e12].
def wedge_matrix(a):
    # wedge by e_a, a=0,1
    W = np.zeros((4,4), complex)
    if a == 0:
        W[1,0] = 1; W[3,2] = 1
    else:
        W[2,0] = 1; W[3,1] = -1
    return W

def contract_matrix(a):
    C = np.zeros((4,4), complex)
    if a == 0:
        C[0,1] = 1; C[2,3] = 1
    else:
        C[0,2] = 1; C[1,3] = -1
    return C

W1,W2 = wedge_matrix(0),wedge_matrix(1)
C1,C2 = contract_matrix(0),contract_matrix(1)
# bar theta_a=(E^{2a-1}-iE^{2a})/sqrt(2).  Standard c=sqrt(2)(wedge-contraction).
# The real Clifford maps square to -1.
cl = [W1-C1, 1j*(W1+C1), W2-C2, 1j*(W2+C2)]
for G in cl:
    assert np.allclose(G@G, -np.eye(4))
# even/odd coordinate selectors in full exterior basis.
even=[0,3]; odd=[1,2]
G_pm=[G[np.ix_(odd,even)] for G in cl]  # S+ -> S-
G_mp=[G[np.ix_(even,odd)] for G in cl]  # S- -> S+

def det2(x,y): return x[0]*y[1]-x[1]*y[0]

def torsion_plus(phi, P):
    return sum(G_pm[i]@phi * det2(phi,P[i]) for i in range(4))

def torsion_minus(v,Q):
    return sum(G_mp[i]@v * det2(v,Q[i]) for i in range(4))

# TN coordinate geometry.
r,th,ph,ell=sp.symbols('r th ph ell', positive=True, real=True)
ps=sp.symbols('ps', real=True)
X=[r,th,ph,ps]
V=1+ell/r
eta=[0,0,ell*sp.cos(th),1]
gb=sp.diag(1,r**2,r**2*sp.sin(th)**2,0)
g=sp.Matrix(4,4,lambda i,j: V*gb[i,j]+eta[i]*eta[j]/V)
gi=sp.simplify(g.inv())
Gam=[[[sp.simplify(sum(gi[a,d]*(sp.diff(g[d,b],X[c])+sp.diff(g[d,c],X[b])-sp.diff(g[b,c],X[d])) for d in range(4))/2)
       for c in range(4)] for b in range(4)] for a in range(4)]
x1=r*sp.sin(th)*sp.cos(ph); x2=r*sp.sin(th)*sp.sin(ph)
fb=x1-sp.I*x2
df=[sp.diff(fb,x) for x in X]
H=sp.Matrix(4,4,lambda b,c: sp.diff(df[c],X[b])-sum(Gam[a][b][c]*df[a] for a in range(4)))
J=sp.Matrix([x1,x2,r*sp.cos(th)]).jacobian(sp.Matrix([r,th,ph])); Ji=sp.simplify(J.inv())
fH=sp.lambdify((r,th,ph,ell),H,'numpy'); fJi=sp.lambdify((r,th,ph),Ji,'numpy')
ffb=sp.lambdify((r,th,ph),fb,'numpy')

def frame(rv,tv,pv,lv):
    vv=1+lv/rv; j=np.array(fJi(rv,tv,pv),float)
    out=[]
    for k in range(3):
        q=np.array([j[0,k],j[1,k],j[2,k],0.0])
        q[3]=-lv*np.cos(tv)*q[2]
        out.append(q/np.sqrt(vv))
    out.append(np.array([0.,0.,0.,np.sqrt(vv)]))
    return out

def cov01_components(vals):
    # vals q(E1),...,q(E4), for a (0,1)-form.
    return np.array([(vals[0]+1j*vals[1])/np.sqrt(2),
                     (vals[2]+1j*vals[3])/np.sqrt(2)],complex)

rho0=4/3; aa=np.sqrt(2)/3; mstar=128/81; Cv=np.sqrt(mstar/2)

def point(rv,tv,pv,lv=1.0):
    vv=1+lv/rv; es=frame(rv,tv,pv,lv); hn=np.array(fH(rv,tv,pv,lv),complex)
    fbc=complex(ffb(rv,tv,pv))
    phi=np.array([np.sqrt(rho0),aa*fbc],complex)
    # dbar f on the orthonormal frame.
    dvals=np.array([sum(complex(df[j].subs({r:rv,th:tv,ph:pv,ell:lv}))*es[i][j] for j in range(4)) for i in range(4)])
    # Positive first derivative in the parallel S+ frame.
    P=np.array([[0,aa*dvals[i]] for i in range(4)],complex)
    tau_alg=torsion_plus(phi,P)
    tau_exact=Cv*cov01_components(dvals)
    # Q_i = nabla_{E_i} v; H is the covariant Hessian of fbar.
    qarr=[]
    for ei in es:
        vals=np.array([ei@hn@ej for ej in es],complex)
        qarr.append(Cv*cov01_components(vals))
    Q=np.array(qarr)
    tvspin=torsion_minus(tau_exact,Q)
    sigma=det2(phi,tvspin)
    return dict(V=vv,fbar=fbc,phi=phi,dvals=dvals,tau_alg=tau_alg,
                tau_exact=tau_exact,Q=Q,tv=tvspin,sigma=sigma)

samples=[]
K2_exact=8388608/1594323
formula_res=[]
for rv,tv,pv in [(0.15,.7,.2),(.3,1.2,.8),(1.,.9,1.7),(3.,2.1,.4),(10.,1.4,2.2)]:
    z=point(rv,tv,pv)
    ratio=z['tau_alg'][0]/z['tau_exact'][0] if abs(z['tau_exact'][0])>1e-12 else z['tau_alg'][1]/z['tau_exact'][1]
    K=z['sigma']*(rv+1)**3/z['fbar']
    formula_res.append(abs(K*K-K2_exact))
    samples.append(dict(r=rv,th=tv,ph=pv,V=z['V'],fbar=[z['fbar'].real,z['fbar'].imag],
                        torsion_reconstruction_ratio=[ratio.real,ratio.imag],
                        fitted_K=[K.real,K.imag],fitted_K2=float((K*K).real),
                        sigma=[z['sigma'].real,z['sigma'].imag],sigma_abs2=float(abs(z['sigma'])**2),
                        tv_norm2=float(np.vdot(z['tv'],z['tv']).real),
                        Q_norm2=float(np.vdot(z['Q'],z['Q']).real)))

# Scaling in the NUT parameter.  Fit sigma*(r+ell)^3/(ell*fbar).
ell_scaling=[]
for lv in [.125,.25,.5,1.,2.,4.]:
    rv=.7*lv; tv=1.1; pv=.6; z=point(rv,tv,pv,lv)
    K=z['sigma']*(rv+lv)**3/(lv*z['fbar'])
    ell_scaling.append(dict(ell=lv,r=rv,fitted_K_with_ell=[K.real,K.imag],fitted_K2=float((K*K).real)))

# Angular tests at fixed r, and power-law probes in r.
angular=[]
for rv in [.2,1.,5.]:
    vals=[]
    for tv in [.4,.9,1.4,2.0,2.6]:
        for pv in [.1,.7,1.9]:
            z=point(rv,tv,pv); vals.append(z['sigma'])
    angular.append(dict(r=rv,abs_min=float(min(abs(x) for x in vals)),abs_max=float(max(abs(x) for x in vals)),
                        values=[[x.real,x.imag] for x in vals]))
rad=[]
for rv in np.logspace(-3,3,25):
    z=point(float(rv),1.1,.6)
    rad.append(dict(r=float(rv),abs_sigma=float(abs(z['sigma'])),abs2=float(abs(z['sigma'])**2),
                    Q_norm2=float(np.vdot(z['Q'],z['Q']).real)))
out=dict(conventions='canonical Kahler spinors; TN ell=1 unless stated',rho_star=rho0,a=aa,mstar=mstar,
         exact_projected_formula='sigma=sqrt(8388608/1594323)*ell*fbar/(r+ell)^3 in the chosen parallel trivialization',
         max_formula_K2_residual=float(max(formula_res)),ell_scaling=ell_scaling,samples=samples,angular=angular,radial=rad)
print(json.dumps(out,indent=1))
here=os.path.dirname(os.path.abspath(__file__)); od=os.path.join(here,'..','data','step90'); os.makedirs(od,exist_ok=True)
json.dump(out,open(os.path.join(od,'tn_sigma_projection.json'),'w'),indent=1)
