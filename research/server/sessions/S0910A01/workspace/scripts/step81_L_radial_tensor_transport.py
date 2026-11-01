"""
Step 81: direct check that L transports the full EH radial kernel/obstruction
asymptotic tensor, not only the insertion 2-form omega2.

Ozuch line 369 gives, for zeta^+ and adapted basis zeta_(1)^+=zeta^+/|zeta|,
  o_1(zeta^+) = zeta_(1)^+ circ rho(zeta)^- / r^4 + O(r^-8).
The negative-orientation analogue is
  o_1(zeta^-) = zeta_(1)^- circ rho(zeta)^+ / r^4 + O(r^-8).
For L=single-factor antipodal, zeta=omega2, check pointwise
  L^* O_rad^- (Lx) = O_rad^+ (x)
with no sign change in the transported basis.
"""
import json
import numpy as np

def form_matrix(pairs):
    M=np.zeros((4,4),float)
    for i,j,v in pairs:
        M[i,j]=v; M[j,i]=-v
    return M

omega1p=form_matrix([(0,1,1),(2,3,1)])
omega2p=form_matrix([(0,2,1),(1,3,-1)])
omega3p=form_matrix([(0,3,1),(1,2,1)])
omega1m=form_matrix([(0,1,1),(2,3,-1)])
omega2m=form_matrix([(0,2,1),(1,3,1)])
omega3m=form_matrix([(0,3,1),(1,2,-1)])
SD=[omega1p,omega2p,omega3p]
ASD=[omega1m,omega2m,omega3m]
L=np.diag([1.,-1.,1.,1.])

def rho_plus_insert(x):
    r2=x@x; z=SD[1]
    return np.array([float(x@(z@ASD[j])@x/r2) for j in range(3)])

def rho_minus_insert(x):
    r2=x@x; z=ASD[1]
    return np.array([float(x@(z@SD[j])@x/r2) for j in range(3)])

def O_rad_plus(x):
    r2=x@x; rho=rho_plus_insert(x); z=SD[1]
    O=sum(rho[j]*(z@ASD[j]) for j in range(3))
    return O/(r2**2)

def O_rad_minus(x):
    r2=x@x; rho=rho_minus_insert(x); z=ASD[1]
    O=sum(rho[j]*(z@SD[j]) for j in range(3))
    return O/(r2**2)

np.random.seed(8113)
N=20000
X=np.random.randn(N,4); X=X/np.linalg.norm(X,axis=1,keepdims=True)
errs=[]
symerrs=[]
for x in X:
    y=L@x
    pulled=L.T@O_rad_minus(y)@L
    O=O_rad_plus(x)
    errs.append(float(np.max(np.abs(pulled-O))))
    symerrs.append(float(np.max(np.abs(O-O.T))))
# Check relation with H4 convention: O_rad = -2 H4 in previous script's convention.
examples=[]
for x in X[:3]:
    y=L@x
    examples.append({
        "x":x.tolist(),
        "O_rad_plus_diag":np.diag(O_rad_plus(x)).tolist(),
        "pulled_O_rad_minus_diag":np.diag(L.T@O_rad_minus(y)@L).tolist(),
        "max_error":float(np.max(np.abs(L.T@O_rad_minus(y)@L-O_rad_plus(x))))
    })
results={
    "step":81,
    "purpose":"direct L-transport check for full EH radial asymptotic kernel tensor O_1^4",
    "source_formula":"Ozuch Higher-order obstructions lines 366-371: o_k(zeta^+)=zeta_(k)^+ circ rho(zeta)^-/r^4 + O(|zeta|^3 r^-8), with negative-orientation analogue from lines 372-376.",
    "N_samples":N,
    "max_transport_error":max(errs),
    "max_symmetry_error_of_tensor":max(symerrs),
    "verified_plus_sign": bool(max(errs)<1e-12),
    "interpretation":"With radial kernel normalized as the derivative in the omega2 scale direction, L^* O_rad^- = O_rad^+ at the asymptotic tensor level; the projection-normalization factor is therefore +1 if the same L^2/flux convention is used on both chiralities.",
    "examples":examples
}
print(json.dumps(results,indent=2))
out="Sessions/S0910A01/workspace/data/step81_L_radial_tensor_transport.json"
with open(out,"w") as f: json.dump(results,f,indent=2)
print(f"\nWrote {out}")
