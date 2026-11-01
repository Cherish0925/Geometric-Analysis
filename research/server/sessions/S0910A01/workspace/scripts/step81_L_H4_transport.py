"""
Step 81 supplementary check: the orientation-reversing single-factor antipodal L
transports the actual angular Ozuch H^4 tensor for a positive-chirality
omega2 insertion to the corresponding negative-chirality omega2 insertion,
without freezing rho_x.

Convention tested:
  H4_plus(zeta+)  = -1/(2 r^4) sum_j rho^-_j(x) (omega_j^- circ zeta+)
  rho^-_j(x)     = x^T (zeta+ circ omega_j^-) x / r^2
  H4_minus(zeta-) = -1/(2 r^4) sum_j rho^+_j(x) (omega_j^+ circ zeta-)
  rho^+_j(x)     = x^T (zeta- circ omega_j^+) x / r^2
with zeta+=omega2+, zeta-=omega2-.  L=diag(1,-1,1,1) sends
omega2+ to omega2- and swaps Lambda^+ and Lambda^-.
"""
import json
import numpy as np


def form_matrix(pairs):
    M = np.zeros((4, 4), dtype=float)
    for i, j, v in pairs:
        M[i, j] = v
        M[j, i] = -v
    return M

omega1p = form_matrix([(0,1,1),(2,3,1)])
omega2p = form_matrix([(0,2,1),(1,3,-1)])
omega3p = form_matrix([(0,3,1),(1,2,1)])
omega1m = form_matrix([(0,1,1),(2,3,-1)])
omega2m = form_matrix([(0,2,1),(1,3,1)])
omega3m = form_matrix([(0,3,1),(1,2,-1)])
SD = [omega1p, omega2p, omega3p]
ASD = [omega1m, omega2m, omega3m]
L = np.diag([1., -1., 1., 1.])


def rho_plus_insertion(x):
    # zeta = omega2+; output anti-self-dual component vector rho^-
    r2 = float(np.dot(x, x))
    zeta = SD[1]
    return np.array([float(x @ (zeta @ ASD[j]) @ x / r2) for j in range(3)])


def rho_minus_insertion(x):
    # zeta = omega2-; output self-dual component vector rho^+
    r2 = float(np.dot(x, x))
    zeta = ASD[1]
    return np.array([float(x @ (zeta @ SD[j]) @ x / r2) for j in range(3)])


def H4_plus(x):
    r2 = float(np.dot(x, x))
    rho = rho_plus_insertion(x)
    zeta = SD[1]
    H = np.zeros((4,4))
    for j in range(3):
        H += -rho[j] * (ASD[j] @ zeta)
    return H / (2 * r2**2)


def H4_minus(x):
    r2 = float(np.dot(x, x))
    rho = rho_minus_insertion(x)
    zeta = ASD[1]
    H = np.zeros((4,4))
    for j in range(3):
        H += -rho[j] * (SD[j] @ zeta)
    return H / (2 * r2**2)

# Coefficients of transported component vectors under L.
def coeff(M, basis):
    return np.array([float(np.sum(M*B)/np.sum(B*B)) for B in basis])

L_SD_to_ASD = np.column_stack([coeff(L.T @ SD[i] @ L, ASD) for i in range(3)])
L_ASD_to_SD = np.column_stack([coeff(L.T @ ASD[i] @ L, SD) for i in range(3)])

np.random.seed(8102)
N=20000
X=np.random.randn(N,4)
X=X/np.linalg.norm(X,axis=1,keepdims=True)
max_H_err=0.0
max_rho_err=0.0
sample_records=[]
for idx,x in enumerate(X):
    y=L@x
    # Pull target negative H4 back by L and compare to source positive H4.
    H_back = L.T @ H4_minus(y) @ L
    err=float(np.max(np.abs(H_back-H4_plus(x))))
    max_H_err=max(max_H_err,err)

    # Rho components should be transported by the same signed basis-change:
    # rho_minus(y) should equal S * rho_plus(x), with S mapping ASD components
    # from source to SD components at target.  For omega2 it is diag(-1,1,1)
    # in our basis conventions.
    rp=rho_plus_insertion(x)
    rm=rho_minus_insertion(y)
    pred=L_ASD_to_SD @ rp
    rerr=float(np.max(np.abs(rm-pred)))
    max_rho_err=max(max_rho_err,rerr)
    if idx < 3:
        sample_records.append({
            "x": x.tolist(),
            "rho_plus_at_x": rp.tolist(),
            "rho_minus_at_Lx": rm.tolist(),
            "predicted_rho_minus": pred.tolist(),
            "rho_error": rerr,
            "H4_pullback_error": err
        })

results={
    "step":81,
    "purpose":"verify L transports full angular H4 between opposite EH chiralities",
    "basis_transport":{
        "L_SD_to_ASD_columns":L_SD_to_ASD.tolist(),
        "L_ASD_to_SD_columns":L_ASD_to_SD.tolist(),
        "omega2_plus_to_omega2_minus":float(L_SD_to_ASD[1,1]),
        "omega2_minus_to_omega2_plus":float(L_ASD_to_SD[1,1])
    },
    "N_samples":N,
    "max_rho_transport_error":max_rho_err,
    "max_H4_transport_error":max_H_err,
    "verified": bool(max(max_rho_err,max_H_err)<1e-12),
    "samples":sample_records,
    "interpretation":"The actual spatial rho_x dependence is compatible with L; the single-factor antipodal maps the positive omega2 angular H4 source to the negative omega2 angular H4 source."
}
print(json.dumps(results,indent=2))
outpath="Sessions/S0910A01/workspace/data/step81_L_H4_transport.json"
with open(outpath,"w") as f:
    json.dump(results,f,indent=2)
print(f"\nWrote {outpath}")
