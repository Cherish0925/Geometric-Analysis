"""
Step 94: verify the invariant fixed-charge identity for the physical twist energy.

On H^2 in Iwasawa coordinates
  h = d alpha^2 + exp(-2 alpha) d beta^2,
  M = [[exp(alpha)+beta^2 exp(-alpha), beta exp(-alpha)],
       [beta exp(-alpha), exp(-alpha)]].
For fixed q=(q1,q2), set
  F=(1/2) q^T M^{-1}q,  b=log F.
The script verifies
  Hess_h F = F h,
  |grad_h F|^2 = F^2,
  Hess_h b = h-db tensor db,
  |grad_h b|^2=1.
It then performs the invariant drift-chain algebra for
  Q=exp(-3 sigma) F(U),
  L sigma=6+Q, tau_sigma(U)=-Q grad b,
and checks
  L log Q = -18-4Q + e - |d(b o U)|^2.
The last term is the target energy transverse to grad b and is nonnegative.
"""
from pathlib import Path
import json
import sympy as sp

alpha, beta, q1, q2 = sp.symbols('alpha beta q1 q2', real=True)
q = sp.Matrix([q1, q2])
M = sp.Matrix([
    [sp.exp(alpha) + beta**2*sp.exp(-alpha), beta*sp.exp(-alpha)],
    [beta*sp.exp(-alpha), sp.exp(-alpha)],
])
Minv = sp.simplify(M.inv())
F = sp.factor(sp.Rational(1,2)*(q.T*Minv*q)[0])
bfun = sp.log(F)

# h=diag(1,e^-2a), h^{-1}=diag(1,e^2a)
h = sp.diag(1, sp.exp(-2*alpha))
hinv = sp.diag(1, sp.exp(2*alpha))
coords = [alpha, beta]

# Christoffels of h
Gamma = [[ [sp.S(0) for _ in range(2)] for _ in range(2)] for _ in range(2)]
for k in range(2):
    for i in range(2):
        for j in range(2):
            Gamma[k][i][j] = sp.simplify(sp.Rational(1,2)*sum(
                hinv[k,l]*(sp.diff(h[l,j],coords[i])+sp.diff(h[l,i],coords[j])-sp.diff(h[i,j],coords[l]))
                for l in range(2)))

def hessian(f):
    return sp.Matrix(2,2,lambda i,j: sp.simplify(
        sp.diff(f,coords[i],coords[j])-sum(Gamma[k][i][j]*sp.diff(f,coords[k]) for k in range(2))))

def gradnorm2(f):
    df = sp.Matrix([sp.diff(f,c) for c in coords])
    return sp.simplify((df.T*hinv*df)[0])

HF = hessian(F)
Hb = hessian(bfun)
db = sp.Matrix([sp.diff(bfun,c) for c in coords])
res_HF = HF.applyfunc(lambda x: sp.simplify(x)) - (F*h).applyfunc(lambda x: sp.simplify(x))
res_gF = sp.factor(gradnorm2(F)-F**2)
res_Hb = (Hb-(h-db*db.T)).applyfunc(lambda x: sp.simplify(sp.factor(x)))
res_gb = sp.factor(gradnorm2(bfun)-1)

# Abstract invariant chain rule. At one base point use target-coordinate derivative vectors
# u_r,u_z. B_i = db(u_i), e=sum h(u_i,u_i), b_energy=sum B_i^2.
Q,e,b_energy = sp.symbols('Q e b_energy', nonnegative=True)
# L(b o U)=Hess b:dU^2 + db(tau_sigma U)
#             =(e-b_energy) + db(-Q grad b)=e-b_energy-Q.
L_bU = e-b_energy-Q
L_logQ = sp.expand(-3*(6+Q)+L_bU)
expected = -18-4*Q+e-b_energy
res_chain = sp.expand(L_logQ-expected)

# Decompose transverse energy explicitly in the orthonormal target frame.
# Let p_i=<u_i,grad b>, t_i=<u_i,J grad b>. Then e-b_energy=sum t_i^2.
pr,pz,tr,tz = sp.symbols('p_r p_z t_r t_z', real=True)
decomp_res = sp.expand((pr**2+tr**2+pz**2+tz**2)-(pr**2+pz**2)-(tr**2+tz**2))

# Scalar sign check: at a critical point of Q, the identity gives L log Q
# = -18-4Q+e_perp. No sign follows without a bound on e_perp.
eperp = sp.symbols('e_perp', nonnegative=True)
critical_expression = -18-4*Q+eperp

out = {
    'F': str(F),
    'M_inverse': str(Minv),
    'christoffels_nonzero': {
        'Gamma^alpha_beta_beta': str(Gamma[0][1][1]),
        'Gamma^beta_alpha_beta': str(Gamma[1][0][1]),
        'Gamma^beta_beta_alpha': str(Gamma[1][1][0]),
    },
    'residual_HessF_minus_Fh': [[str(sp.simplify(res_HF[i,j])) for j in range(2)] for i in range(2)],
    'residual_gradF2_minus_F2': str(res_gF),
    'residual_HesslogF_minus_h_plus_dbdB': [[str(sp.simplify(res_Hb[i,j])) for j in range(2)] for i in range(2)],
    'residual_gradlogF2_minus_1': str(res_gb),
    'L_beta_composed_U': 'e - |d(beta o U)|^2 - Q',
    'L_log_physical_Q': str(L_logQ),
    'expected_L_log_physical_Q': str(expected),
    'chain_rule_residual': str(res_chain),
    'transverse_decomposition_residual': str(decomp_res),
    'critical_point_expression': str(critical_expression),
    'interpretation': 'For fixed nonzero charge, L log Q=-18-4Q+e_perp. The diagonal charge-aligned reduction has e_perp=0. In general e_perp>=0 can offset the negative reaction, so the diagonal identity does not extend unchanged and gives no maximum exclusion.',
}

assert all(x == '0' for row in out['residual_HessF_minus_Fh'] for x in row)
assert out['residual_gradF2_minus_F2'] == '0'
assert all(x == '0' for row in out['residual_HesslogF_minus_h_plus_dbdB'] for x in row)
assert out['residual_gradlogF2_minus_1'] == '0'
assert out['chain_rule_residual'] == '0'
assert out['transverse_decomposition_residual'] == '0'

path=Path('workspace/data/step94_invariant_charge_identity.json')
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
print(f'wrote {path}')
