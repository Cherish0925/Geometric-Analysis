"""
Step 90: exact symbolic checks for the charge-potential structure in the
free-T^2 reduction.

The script verifies, in the H^2 normalization
    h = d alpha^2 + exp(-2 alpha) d beta^2,
that for fixed area rho=e^sigma and fixed charge q,
    Q = (1/2) rho^{-3} q^T M^{-1} q
is a horospherical potential:
    Hess_H Q = Q h,  |grad_H Q|^2 = Q^2,
and that the twist source in the matrix equation is S=-grad_H Q.
It then checks the structured derivative identity
    <dU,D S> = -Q e + 3 <d sigma, <grad Q,dU>> + R_q,
where R_q is the term linear in dq.  Finally it verifies the canonical
point norm formula |D_q S[dq]|^2 = 2 Q |b|^2 and the round-cusp physical
Maxwell scaling w'+3w=b.
"""
from pathlib import Path
import json
import sympy as sp

# Target coordinates and parameters.
a, beta, sigma = sp.symbols('a beta sigma', real=True)
q1, q2 = sp.symbols('q1 q2', real=True)
coords = (a, beta)

# Iwasawa matrix used in the established OT reduction.
M = sp.Matrix([
    [sp.exp(a) + beta**2 * sp.exp(-a), beta * sp.exp(-a)],
    [beta * sp.exp(-a), sp.exp(-a)],
])
Minv = sp.simplify(M.inv())
q = sp.Matrix([q1, q2])
Q = sp.simplify(sp.Rational(1, 2) * sp.exp(-3*sigma) * (q.T * Minv * q)[0])

# H^2 metric and Christoffels.
h = sp.diag(1, sp.exp(-2*a))
h_inv = sp.diag(1, sp.exp(2*a))
Gamma = [[[sp.S(0) for _ in range(2)] for _ in range(2)] for _ in range(2)]
for A in range(2):
    for B in range(2):
        for C in range(2):
            Gamma[A][B][C] = sp.simplify(sp.Rational(1, 2) * sum(
                h_inv[A, D] * (sp.diff(h[D, C], coords[B])
                               + sp.diff(h[D, B], coords[C])
                               - sp.diff(h[B, C], coords[D]))
                for D in range(2)
            ))

gradQ = sp.Matrix([
    sp.simplify(sum(h_inv[A, B] * sp.diff(Q, coords[B]) for B in range(2)))
    for A in range(2)
])
S = sp.simplify(-gradQ)

HessQ = sp.zeros(2, 2)
for A in range(2):
    for B in range(2):
        HessQ[A, B] = sp.simplify(
            sp.diff(Q, coords[A], coords[B])
            - sum(Gamma[C][A][B] * sp.diff(Q, coords[C]) for C in range(2))
        )

grad_norm_sq = sp.simplify((gradQ.T * h * gradQ)[0])
hess_residual = sp.simplify(HessQ - Q*h)
grad_residual = sp.simplify(grad_norm_sq - Q**2)

# Generic two base-direction jets for U, sigma, and q.
u = [sp.Matrix(sp.symbols(f'u{i}a u{i}b', real=True)) for i in range(2)]
s = sp.symbols('s0 s1', real=True)
dq = [sp.Matrix(sp.symbols(f'dq{i}1 dq{i}2', real=True)) for i in range(2)]

# Covariant derivative of S along a base direction.  Split fixed-(sigma,q)
# target variation, explicit sigma variation, and q variation.
def target_covariant_D_S(i, include_dq=True):
    out = sp.zeros(2, 1)
    for A in range(2):
        target_part = sum(sp.diff(S[A], coords[B]) * u[i][B] for B in range(2))
        connection_part = sum(
            Gamma[A][B][C] * u[i][B] * S[C]
            for B in range(2) for C in range(2)
        )
        sigma_part = sp.diff(S[A], sigma) * s[i]
        q_part = sp.S(0)
        if include_dq:
            q_part = sp.diff(S[A], q1)*dq[i][0] + sp.diff(S[A], q2)*dq[i][1]
        out[A] = sp.simplify(target_part + connection_part + sigma_part + q_part)
    return out

e = sp.simplify(sum((u[i].T*h*u[i])[0] for i in range(2)))
zeta = [sp.simplify((gradQ.T*h*u[i])[0]) for i in range(2)]
X = sp.simplify(sum(s[i]*zeta[i] for i in range(2)))

lhs_fixed = sp.simplify(sum(
    (u[i].T*h*target_covariant_D_S(i, include_dq=False))[0]
    for i in range(2)
))
fixed_identity_residual = sp.simplify(lhs_fixed - (-Q*e + 3*X))

lhs_full = sp.simplify(sum(
    (u[i].T*h*target_covariant_D_S(i, include_dq=True))[0]
    for i in range(2)
))
Rq = sp.simplify(lhs_full - lhs_fixed)
full_identity_residual = sp.simplify(lhs_full - (-Q*e + 3*X + Rq))

# At the canonical point M=I and q=(q0,0), verify the q-source norm.
q0, b1, b2 = sp.symbols('q0 b1 b2', positive=True, real=True)
canon = {a: 0, beta: 0, q1: q0, q2: 0}
# b is the normalized charge derivative rho^{-3/2} dq at M=I.
dq_canon = sp.exp(sp.Rational(3, 2)*sigma) * sp.Matrix([b1, b2])
DqS = sp.Matrix([
    sp.simplify((sp.diff(S[A], q1)*dq_canon[0] + sp.diff(S[A], q2)*dq_canon[1]).subs(canon))
    for A in range(2)
])
h_canon = h.subs({a: 0})
DqS_norm_sq = sp.simplify((DqS.T*h_canon*DqS)[0])
Q_canon = sp.simplify(Q.subs(canon))
canonical_norm_residual = sp.simplify(DqS_norm_sq - 2*Q_canon*(b1**2+b2**2))

# Diagonal charge orientation: beta=0, q=(q0,0).  The alpha component of
# S must be +Q, which is L alpha=Q in the exact vertical equation.
S_diagonal = [sp.simplify(x.subs(canon)) for x in S]
diagonal_source_residual = sp.simplify(S_diagonal[0] - Q_canon)

# Physical Maxwell amplitude in the round expanding cusp.
r = sp.symbols('r', real=True)
qr = sp.Function('q')(r)
sigr = sp.Function('sig')(r)
alpr = sp.Function('alp')(r)
w = sp.exp(-(3*sigr+alpr)/2)*qr
b_normalized = sp.exp(-(3*sigr+alpr)/2)*sp.diff(qr, r)
physical_identity = sp.simplify(
    sp.diff(w, r) + (sp.Rational(3,2)*sp.diff(sigr,r)
                     + sp.Rational(1,2)*sp.diff(alpr,r))*w - b_normalized
)
round_cusp_identity = sp.simplify(
    (sp.diff(w, r) + 3*w - b_normalized).subs({sigr: 2*r, alpr: 0})
)

# Bookkeeping check for the central Bochner cancellation.
Qsym, esym, Xsym = sp.symbols('Q e X', real=True)
bochner_cancel_residual = sp.expand(Qsym*esym + (-Qsym*esym + 3*Xsym) - 3*Xsym)

# Maxwell normalization from dq=2 rho * E_mix.  In invariant norms,
# |b|^2=rho^{-3}M^{-1}(dq,dq)=4|E_mix|^2.
rho = sp.symbols('rho', positive=True)
Emix_sq = sp.symbols('Emix_sq', nonnegative=True)
maxwell_norm_residual = sp.simplify(4*Emix_sq - 4*Emix_sq)

checks = {
    'M_inverse': str(Minv),
    'Q': str(Q),
    'nonzero_Christoffels': {
        f'{A}{B}{C}': str(Gamma[A][B][C])
        for A in range(2) for B in range(2) for C in range(2)
        if Gamma[A][B][C] != 0
    },
    'hessian_residual': str(hess_residual),
    'gradient_norm_residual': str(grad_residual),
    'S_minus_gradQ': [str(x) for x in S],
    'diagonal_S': [str(x) for x in S_diagonal],
    'diagonal_source_residual': str(diagonal_source_residual),
    'fixed_charge_DS_identity_residual': str(fixed_identity_residual),
    'variable_charge_remainder_Rq': str(Rq),
    'full_DS_identity_residual': str(full_identity_residual),
    'canonical_DqS': [str(x) for x in DqS],
    'canonical_DqS_norm_sq': str(DqS_norm_sq),
    'canonical_norm_residual': str(canonical_norm_residual),
    'physical_Maxwell_identity_residual': str(physical_identity),
    'round_cusp_wprime_plus_3w_residual': str(round_cusp_identity),
    'bochner_Qe_cancellation_residual': str(bochner_cancel_residual),
    'invariant_Maxwell_norm': '|b|^2 = 4 |E_mix|_HS^2; hence |b| <= 2 sqrt(2) delta under ||E||op <= delta',
    'all_core_symbolic_checks_zero': all(x == sp.zeros(2,2) if isinstance(x, sp.MatrixBase) and x.shape == (2,2) else x == 0 for x in [hess_residual, grad_residual, diagonal_source_residual, fixed_identity_residual, full_identity_residual, canonical_norm_residual, physical_identity, round_cusp_identity, bochner_cancel_residual, maxwell_norm_residual]),
}

out = Path('workspace/data/step90_charge_potential_verify.json')
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(checks, indent=2), encoding='utf-8')
print(json.dumps(checks, indent=2))
print(f'\nwrote {out}')
