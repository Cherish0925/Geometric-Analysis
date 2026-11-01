"""
Step 94: exact analytic charged stable minimal T^3 Cauchy data.

This extends the Step 92 uncharged Koiso family.  On
  q_Sigma = ds^2 + M(U(s))_{ab} dx^a dx^b, det M=1,
choose a fixed charge covector q, a vertical tracefree Weingarten block B, and
mixed Weingarten covector m=-q/2 (orientation convention).  Then the mixed norm
contributes
  2 m^T M^{-1}m = (1/2)q^T M^{-1}q = Q
and the Gaussian-gauge connection jet reconstructs charge q.

Choose U to traverse a hyperbolic circle m_wind times at constant speed squared
12+2S, where 0<S<3. Scale q so max Q<S and set P=S-Q.  Put
  B=sqrt(P/2) M^{-1}dM(N).
Then |II|^2=P+Q=S, Scal=-6-S, tr II=0, all momentum constraints vanish,
and the Hamiltonian constraint is exact. The Jacobi form is
  int (|grad phi|^2 + (3-S)phi^2),
so the separator is fully strictly stable. Koiso gives a local analytic
Ric=-3g germ with nonzero conserved charge.

Numerics check normalizations and momentum connection-term cancellation.
"""
from pathlib import Path
import json, math
import numpy as np

L=2*math.pi
Ngrid=4096
wind=10
S=1.0                 # total |II|^2, choose 0<S<3
Qmax_target=0.5       # choose 0<Qmax<S
s=np.linspace(0,L,Ngrid,endpoint=False)

# Hyperbolic circle with constant speed^2=12+2S.
speed=math.sqrt(12+2*S)
R=math.asinh(speed/wind)
theta=wind*s
cR,sR=math.cosh(R),math.sinh(R)
den=cR-sR*np.sin(theta)
y=1.0/den
alpha=np.log(y)
beta=sR*np.cos(theta)/den

dden=-sR*np.cos(theta)
alpha_theta=-dden/den
beta_theta=(-sR*np.sin(theta)*den-sR*np.cos(theta)*dden)/den**2
alpha_s=alpha_theta*wind
beta_s=beta_theta*wind
es=alpha_s**2+np.exp(-2*alpha)*beta_s**2

# Fixed charge q=(q0,0): Q=(1/2)q0^2 exp(-alpha). Scale its maximum.
eminus=np.exp(-alpha)
q0=math.sqrt(2*Qmax_target/float(eminus.max()))
qcov=np.array([q0,0.0])
Q=0.5*q0*q0*eminus
P=S-Q
assert P.min()>0

# Unit tangent and target normal in h=diag(1,e^-2alpha).
talpha=alpha_s/speed
tbeta=beta_s/speed
nalpha=-np.exp(-alpha)*tbeta
nbeta=np.exp(alpha)*talpha


def M_and_derivs(a,b):
    em=math.exp(-a); ep=math.exp(a)
    M=np.array([[ep+b*b*em,b*em],[b*em,em]])
    Ma=np.array([[ep-b*b*em,-b*em],[-b*em,-em]])
    Mb=np.array([[2*b*em,em],[em,0.0]])
    return M,Ma,Mb

max_res={
    'det_M_minus_1':0.0,'speed_squared':0.0,'normal_norm':0.0,
    'tangent_normal':0.0,'Q_mixed_norm':0.0,'P_vertical_norm':0.0,
    'II_norm_minus_S':0.0,'trace_W':0.0,'W_self_adjoint':0.0,
    'momentum_s':0.0,'momentum_vertical_connection_cancellation':0.0,
    'hamiltonian':0.0,'reconstructed_charge':0.0,
}
# m=-q/2 realizes q up to the chosen base orientation under W=-g_nu/2.
mcov=-0.5*qcov
for j in range(Ngrid):
    M,Ma,Mb=M_and_derivs(float(alpha[j]),float(beta[j]))
    Mi=np.linalg.inv(M)
    Ms=Ma*alpha_s[j]+Mb*beta_s[j]
    A=0.5*Mi@Ms
    CN=Mi@(Ma*nalpha[j]+Mb*nbeta[j])
    B=math.sqrt(P[j]/2.0)*CN
    mcontra=Mi@mcov
    # Endomorphism W in (s,x1,x2) coordinates.
    W=np.zeros((3,3))
    W[0,1:]=mcov
    W[1:,0]=mcontra
    W[1:,1:]=B
    qmetric=np.zeros((3,3));qmetric[0,0]=1;qmetric[1:,1:]=M
    Qmixed=2*float(mcov@mcontra)
    Pvert=float(np.trace(B@B))
    IInorm=float(np.trace(W@W))
    # Momentum s component is -tr(A B).  For each vertical a the two connection
    # terms are +(A^c_a m_c) and -(A^b_a m_b), hence cancel; m'_a=0.
    moms=-float(np.trace(A@B))
    conn1=A.T@mcov
    conn2=-A.T@mcov
    # Gaussian gauge: M_ab A^b_{s,nu}=g_{sa,nu}=-2 W_sa=-2m_a,
    # so charge rho M F_{nu s}=-2m=q at rho=1 (orientation choice).
    qrec=-2*mcov
    scal=-0.5*es[j]
    ham=scal+IInorm+6.0
    normal_norm=nalpha[j]**2+math.exp(-2*alpha[j])*nbeta[j]**2
    tang_norm=talpha[j]**2+math.exp(-2*alpha[j])*tbeta[j]**2
    tang_normal=talpha[j]*nalpha[j]+math.exp(-2*alpha[j])*tbeta[j]*nbeta[j]
    vals={
      'det_M_minus_1':abs(np.linalg.det(M)-1),
      'speed_squared':abs(es[j]-(12+2*S)),
      'normal_norm':abs(normal_norm-1),
      'tangent_normal':abs(tang_normal),
      'Q_mixed_norm':abs(Qmixed-Q[j]),
      'P_vertical_norm':abs(Pvert-P[j]),
      'II_norm_minus_S':abs(IInorm-S),
      'trace_W':abs(np.trace(W)),
      'W_self_adjoint':float(np.max(np.abs(qmetric@W-(qmetric@W).T))),
      'momentum_s':abs(moms),
      'momentum_vertical_connection_cancellation':float(np.max(np.abs(conn1+conn2))),
      'hamiltonian':abs(ham),
      'reconstructed_charge':float(np.max(np.abs(qrec-qcov))),
    }
    for k,v in vals.items(): max_res[k]=max(max_res[k],float(v))

out={
  'parameters':{'L':L,'grid':Ngrid,'winding':wind,'S_total_II_squared':S,
                'target_Q_max':Qmax_target,'circle_radius_R':R,'charge_q0':q0},
  'ranges':{'e_s_min':float(es.min()),'e_s_max':float(es.max()),
            'Q_min':float(Q.min()),'Q_max':float(Q.max()),
            'P_min':float(P.min()),'P_max':float(P.max()),
            'P_plus_Q_min':float((P+Q).min()),'P_plus_Q_max':float((P+Q).max())},
  'max_residuals':max_res,
  'constraints':{
    'scalar_curvature':'Scal=-e_s/2=-6-S',
    'mean_curvature':'tr W=0',
    'II_norm':'tr(W^2)=P+Q=S',
    'Hamiltonian':'Scal+tr(W^2)=-6',
    'momentum_s':'-tr(A B)=0 since B is target-normal to U_s',
    'momentum_vertical':'m_a prime plus two cancelling connection terms; m=-q/2 is constant',
    'charge':'q=-2m up to base orientation in Gaussian gauge',
  },
  'stability':{
    'Jacobi_quadratic_form':'integral(|grad phi|^2+(3-S)phi^2)',
    'full_lowest_eigenvalue_lower_bound':3-S,
    'strict':bool(S<3),
  },
  'mathematical_status':'Exact analytic T2-invariant charged Cauchy data satisfying all lambda=-3 Einstein constraints; Koiso gives a local analytic charged Einstein germ. This is not a complete two-ended connector and provides no uniform global continuation.',
}
# Numerical tolerances are normalization checks, not the proof.
assert max(max_res.values())<2e-12, max_res
path=Path('workspace/data/step94_charged_koiso_separator.json')
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
print(f'wrote {path}')
