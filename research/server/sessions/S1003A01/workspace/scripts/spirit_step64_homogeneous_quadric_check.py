"""Focused check: compare the ten Step-64 quadrics with the leading Delta-q identity.

The geometric derivation, not this numerical span comparison, must establish the
identity. Polynomial coefficients below are dyadic rationals evaluated exactly
in binary arithmetic on integer coordinate vectors. The saved Step-64 matrices
are rounded to eight decimal places, so the span comparison is numerical.
"""
from pathlib import Path
import json
import numpy as np

WS = Path(__file__).resolve().parents[1]
source = WS / 'data/step64/intrinsic_lam-1.0_s0.json'
saved = json.loads(source.read_text())
G = np.array(saved['quadrics_w'], dtype=float).reshape(10, -1)
_, sg, Vg = np.linalg.svd(G, full_matrices=False)
Gspan = Vg[sg > 1e-7 * sg[0]]


def phi(w, x):
    """A^2-S^2-8|h|^2-6 Re<f, dbar h> for f=z*h+Q(zbar,zbar)."""
    c = w[:8] + 1j * w[8:]
    delta = c[:2]
    Q = np.zeros((2, 2, 2), complex)  # indices: inputs a,b, output t
    Q[0, 0] = c[2:4]
    Q[0, 1] = Q[1, 0] = c[4:6]
    Q[1, 1] = c[6:8]
    z = np.array([x[0] + 1j*x[1], x[2] + 1j*x[3]])
    h = np.dot(delta, z.conj())
    f = z*h + np.einsum('abt,a,b->t', Q, z.conj(), z.conj())
    B = np.outer(z, delta) + 2*np.einsum('abt,a->tb', Q, z.conj())
    return float(-np.trace(B.conj() @ B).real - 8*abs(h)**2
                 - 6*np.vdot(f, delta).real)


xeye = np.eye(4)
xpairs = [(i,j) for i in range(4) for j in range(i,4)]

def coefficients(w):
    diag = np.array([phi(w,x) for x in xeye])
    return np.array([diag[i] if i == j else
                     phi(w,xeye[i]+xeye[j])-diag[i]-diag[j]
                     for i,j in xpairs])

E = np.eye(16)
H = np.zeros((10,16,16))
for i in range(16):
    for j in range(16):
        H[:,i,j] = (coefficients(E[i]+E[j])-coefficients(E[i]-E[j]))/4
Hflat = H.reshape(10,-1)
_, sh, Vh = np.linalg.svd(Hflat, full_matrices=False)
Hspan = Vh[sh > 1e-10*sh[0]]
errs = np.linalg.norm(Hflat-(Hflat @ Gspan.T) @ Gspan,axis=1)/np.linalg.norm(Hflat,axis=1)
principal = np.linalg.svd(Hspan @ Gspan.T,compute_uv=False)

# Trace is a multiple of |Q|^2-|P|^2+(15/4)|delta|^2.
def scalar(w):
    c = w[:8] + 1j*w[8:]
    d = c[:2]
    qnorm = np.vdot(c[2:4],c[2:4]).real+2*np.vdot(c[4:6],c[4:6]).real+np.vdot(c[6:8],c[6:8]).real
    P = np.array([c[4]-c[3],c[6]-c[5]])
    return float(qnorm-np.vdot(P,P).real+(15/4)*np.vdot(d,d).real)
M = np.array([[(scalar(E[i]+E[j])-scalar(E[i]-E[j]))/4
              for j in range(16)] for i in range(16)])
Htrace = sum(H[k] for k,(i,j) in enumerate(xpairs) if i==j)
trace_err = float(np.max(np.abs(Htrace+8*M)))

# Surface restrictions as in Step 64: d1=Q11^1=Q11^2=Q12^2=0.
keep = [1,4,6,7,9,12,14,15]
Hsurf = H[:,keep][:,:,keep].reshape(10,-1)
surf_sv = np.linalg.svd(Hsurf,compute_uv=False)

out = {
    'identity': '||A_f||^2-||S_f||^2-8|h|^2-6 Re(sum conjugate(f_i)*dbar_i h)=0',
    'source_coefficient_pairs': xpairs,
    'rank_predicted_quadrics': len(Hspan),
    'rank_saved_quadrics': len(Gspan),
    'relative_coefficient_projection_errors': errs.tolist(),
    'principal_angle_cosines': principal.tolist(),
    'exact_dyadic_trace_error_for_Htrace_equals_minus8_scalar': trace_err,
    'surface_rank': int((surf_sv>1e-10*surf_sv[0]).sum()),
    'surface_singular_values': surf_sv.tolist(),
    'predicted_quadric_matrices': H.tolist(),
    'interpretation': 'Ten coefficient equations agree with saved numerical span to rounding precision. This does not independently prove completeness of the nonlinear jet obstruction.'
}
od = WS/'data/spirit_step64'; od.mkdir(exist_ok=True)
(od/'homogeneous_quadric_comparison.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k!='predicted_quadric_matrices'},indent=2))
assert len(Hspan)==10 and trace_err==0
assert max(errs)<1e-7
