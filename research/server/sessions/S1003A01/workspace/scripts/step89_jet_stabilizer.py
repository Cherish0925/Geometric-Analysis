"""Step 89: stabilizer of the O10 endpoint jet and the minimal detectable line power.

Question.  At the hypothetical O10 endpoint (s=-4, D_A Phi=0, rho=|Phi|^2 -> 4/3,
zeta_i=<Phi,P_i> -> 0, |P|^2 -> 4/9, P_i = nabla_i Phi), which natural line sections
L^m built pointwise from the jets of the actual monopole can be nonzero?

Method.  Explicit Euclidean Clifford model on R^4, chiral basis.  Spin^c(4) acts by
  X=(omega in so(4), t in R):  S^+-> Sigma(omega)+i t,  S^- -> Sigma(omega)+i t,
  L=det S^+ -> 2 i t,  covector index -> vector rep M(omega).
We
 (1) build the endpoint first jet (Phi_*, P_*) and check m=|tau|^2 = 128/81,
 (2) compute the stabilizer algebra of (Phi_*,P_*) and its weight on L,
 (3) check that the endpoint first-jet set is one Spin^c orbit (dimension count),
 (4) compute the stabilizer weights on the second-jet space Q=nabla tau in T*(x)S^-(x)L,
 (5) check that sigma=Phi ^ t(tau;Q) in L^5 is the weight-10 eigen-functional, that the
     weight-10 eigenspace is one-dimensional, and that a Q of norm^2 = 2 m_* in that
     eigenspace gives |sigma|^2 = 4 rho_* m_*^3 (the corpus endpoint value with |c|=1).
Output: workspace/data/step89/jet_stabilizer.json
"""
import json, os, itertools
import numpy as np
from scipy.linalg import null_space

np.set_printoptions(precision=6, suppress=True)
I2 = np.eye(2); s1 = np.array([[0, 1], [1, 0]], complex); s2 = np.array([[0, -1j], [1j, 0]]); s3 = np.array([[1, 0], [0, -1]], complex)
sig = [I2, -1j*s1, -1j*s2, -1j*s3]
sigb = [I2, 1j*s1, 1j*s2, 1j*s3]
Z = np.zeros((2, 2))
gam = [np.block([[Z, sig[m]], [sigb[m], Z]]) for m in range(4)]
for a in range(4):
    for b in range(4):
        assert np.allclose(gam[a]@gam[b]+gam[b]@gam[a], 2*(a == b)*np.eye(4))
g5 = gam[0]@gam[1]@gam[2]@gam[3]
w, U = np.linalg.eigh((g5+g5.conj().T)/2)  # g5 hermitian here
# S^+ := eigenvalue +1 block, S^- := -1 block (convention; the other choice is the reversed orientation)
Up = U[:, w > 0]; Um = U[:, w < 0]
Pp = Up@Up.conj().T; Pm = Um@Um.conj().T

def so4_basis():
    B = []
    for a, b in itertools.combinations(range(4), 2):
        E = np.zeros((4, 4)); E[a, b] = 1; E[b, a] = -1
        B.append(((a, b), E))
    return B
SO4 = so4_basis()
Sig = [0.25*(gam[a]@gam[b]-gam[b]@gam[a]) for (a, b), _ in SO4]
# vector action M with [Sigma, gamma_r] = sum_s M[s,r] gamma_s
Mv = []
for S in Sig:
    M = np.zeros((4, 4))
    for r in range(4):
        C = S@gam[r]-gam[r]@S
        for s_ in range(4):
            M[s_, r] = np.real(np.trace(gam[s_].conj().T@C))/4
        assert np.allclose(C, sum(M[s_, r]*gam[s_] for s_ in range(4)))
    Mv.append(M)

# coordinates on S^+ and S^- (2-dim each)
def to4p(x): return Up@x
def to4m(x): return Um@x
def detp(x, y): return x[0]*y[1]-x[1]*y[0]          # Lambda^2 S^+ = L (frame e_+1^e_+2)
def detm(x, y): return x[0]*y[1]-x[1]*y[0]
SigP = [Up.conj().T@S@Up for S in Sig]; SigM = [Um.conj().T@S@Um for S in Sig]
GmP = [Um.conj().T@g@Up for g in gam]   # gamma: S^+ -> S^-
GpM = [Up.conj().T@g@Um for g in gam]   # gamma: S^- -> S^+

rho_s = 4/3; mstar = 128/81
# endpoint first jet
Phi = np.sqrt(rho_s)*np.array([1, 0], complex)
e2 = np.array([0, 1], complex)
# P_i = theta_i e2 with sum theta_i gamma_i e2 = 0
A = np.array([GmP[i]@e2 for i in range(4)]).T   # 2x4
th_space = null_space(A)  # complex 4x2
theta = th_space[:, 0]
theta = theta/np.linalg.norm(theta)*np.sqrt(4/9)
P = np.array([theta[i]*e2 for i in range(4)])  # 4x2
assert np.allclose(sum(GmP[i]@P[i] for i in range(4)), 0)
# cubic torsion tau = sum_i gamma_i Phi (Phi ^ P_i)  in S^- (x) L
def torsion_plus(Ph, PP):
    return sum(GmP[i]@Ph*detp(Ph, PP[i]) for i in range(4))
tau = torsion_plus(Phi, P)
m_val = float(np.vdot(tau, tau).real)

# Lie algebra action on the jet
def act(X, Ph, PP, weightS=1):
    om, t = X[:6], X[6]
    SP = sum(om[k]*SigP[k] for k in range(6)); M = sum(om[k]*Mv[k] for k in range(6))
    dPh = SP@Ph+1j*t*Ph
    dP = np.array([SP@PP[s_]+1j*t*PP[s_]+sum(M[s_, i]*PP[i] for i in range(4)) for s_ in range(4)])
    return dPh, dP

def realvec(z): z = np.ravel(z); return np.concatenate([z.real, z.imag])
cols = []
for k in range(7):
    X = np.zeros(7); X[k] = 1
    dPh, dP = act(X, Phi, P)
    cols.append(np.concatenate([realvec(dPh), realvec(dP)]))
Amat = np.array(cols).T
stab = null_space(Amat)
orbit_dim = 7-stab.shape[1]
Xs = stab[:, 0]/stab[6, 0] if abs(stab[6, 0]) > 1e-12 else stab[:, 0]
L_weight = 2*Xs[6]   # weight of the stabilizer generator on L (units: i*)

# check stabilizer fixes tau
om, t = Xs[:6], Xs[6]
SM = sum(om[k]*SigM[k] for k in range(6)); M = sum(om[k]*Mv[k] for k in range(6))
dtau = SM@tau+3j*t*tau
# second-jet space Q_s in S^-(x)L, s=1..4 : action dQ_s = (SM+3it)Q_s + sum_i M[s,i]Q_i
Op = np.zeros((8, 8), complex)
for s_ in range(4):
    for i in range(4):
        blk = (SM+3j*t*np.eye(2)) if s_ == i else np.zeros((2, 2), complex)
        Op[2*s_:2*s_+2, 2*i:2*i+2] = blk+M[s_, i]*np.eye(2)
ev, evec = np.linalg.eig(Op)
weights_Q = sorted(np.round((ev/1j).real, 8))

def sigma_of(Q):
    Qs = Q.reshape(4, 2)
    tt = sum(GpM[i]@tau*detm(tau, Qs[i]) for i in range(4))  # t(tau;Q) in S^+(x)L^4
    return detp(Phi, tt)
# sigma is linear in Q: find its covector and check eigen-property sigma(Op Q) = 10 i sigma(Q)
sig_cov = np.array([sigma_of(np.eye(8)[k]) for k in range(8)])
lhs = sig_cov@Op
ratio = None
nz = np.argmax(abs(sig_cov))
ratio = lhs[nz]/sig_cov[nz]
eig_check = np.allclose(lhs, ratio*sig_cov)
# weight-10 eigenspace (in units of the L weight 2: weight 10 = L^5)
target = 5*L_weight
idx = [k for k in range(8) if abs((ev[k]/1j).real-target) < 1e-8]
dim10 = len(idx)
q10 = evec[:, idx[0]]; q10 = q10/np.linalg.norm(q10)*np.sqrt(2*mstar)
sig10 = sigma_of(q10)
sig_sq = abs(sig10)**2
corpus = 4*rho_s*mstar**3
# all charged weights available linearly at second order (units of L-charge m)
charges_Q = sorted(set(np.round(np.array(weights_Q)/L_weight, 6)))

out = dict(
    m_tau_sq=m_val, mstar=mstar,
    orbit_dim=orbit_dim, endpoint_set_dim_expected=6, stabilizer_dim=int(stab.shape[1]),
    stabilizer_generator=[float(x) for x in Xs], L_weight=float(L_weight),
    tau_fixed_by_stabilizer=bool(np.allclose(dtau, 0)),
    Q_weights_over_L_weight=[float(x) for x in charges_Q],
    sigma_eigenvalue_over_i_over_L_weight=float((ratio/1j).real/L_weight),
    sigma_is_eigenfunctional=bool(eig_check),
    dim_weight_L5_eigenspace=dim10,
    sigma_sq_at_norm2mstar=float(sig_sq), corpus_4rho_m3=corpus, ratio=float(sig_sq/corpus))
print(json.dumps(out, indent=1))
here = os.path.dirname(os.path.abspath(__file__))
od = os.path.join(here, '..', 'data', 'step89'); os.makedirs(od, exist_ok=True)
json.dump(out, open(os.path.join(od, 'jet_stabilizer.json'), 'w'), indent=1)
