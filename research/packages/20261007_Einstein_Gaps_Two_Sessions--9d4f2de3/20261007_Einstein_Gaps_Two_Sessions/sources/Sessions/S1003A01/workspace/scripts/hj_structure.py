"""Hamilton--Jacobi structure of the diagonal Bianchi-IX trace-free Ricci cost (Step 17).

Controlled system (Ric_CH=-6g normalization irrelevant here; P is scale invariant):
    a_i' = u_i + gamma_i(a),        gamma_i=(a_j^2+a_k^2-a_i^2)/(a_j a_k)
    u_i' = 2 H_i/lambda_i + a_i z_i, H_i=u_i+u_j u_k/2, lambda_i=a_j a_k/a_i
cost density  L = W |z|^2/4,  W=a1 a2 a3,  P/(8 pi^2)=int L dt.

Checks, as rational identities in independent symbols a_i>0, u_i, z_i:
 (H1) For any state function S(a,u):
        L - dS/dt = (W/4) sum_i (z_i - 2 a_i S_{u_i}/W)^2 - H_S,
        H_S = D0 S + W^{-1} sum_i a_i^2 S_{u_i}^2.
 (H2) H_{-Phi} = -2 u1 u2 u3/lambda_2 for Phi=C-u2^2 (relative calibration 1.5).
 (H3) Lambda := -8 sum a_i H_i / W  (= 2s-4Ric_00 = -4 G_00) is a first integral of the
      zero-control flow D0, and s = Lambda - 2 sum z_i.  [the scalar identity uses
      s=-2 sum(r_i+v_i), r_i=u_i'/a_i, v_i=2H_i/(a_j a_k), verified in perp_cartan_verify.py]
 (H4) Pontryagin Hamiltonian  Ham = p_a.(u+gamma) + p_u.(2H/lambda) + sum a_i^2 p_{u_i}^2/W;
      scaling identity  sum a_i dHam/da_i = -(Ham - p_a.(u+gamma)),  hence
      d/dt (sum a_i p_{a_i}) = Ham along extremals.
 (H5) Scale covariance: for scale-invariant S (sum a_i S_{a_i}=0), H_S is homogeneous of
      degree -1 in a, so the sign of H_S depends only on (a2/a1, a3/a1, u).
"""
import sympy as sp

a = sp.symbols('a1:4', positive=True)
u = sp.symbols('u1:4', real=True)
z = sp.symbols('z1:4', real=True)
pa = sp.symbols('pa1:4', real=True)
pu = sp.symbols('pu1:4', real=True)
c = sp.Symbol('c', positive=True)
W = a[0]*a[1]*a[2]
def jk(i): return (i+1) % 3, (i+2) % 3
gam = [(a[jk(i)[0]]**2+a[jk(i)[1]]**2-a[i]**2)/(a[jk(i)[0]]*a[jk(i)[1]]) for i in range(3)]
H = [u[i]+u[jk(i)[0]]*u[jk(i)[1]]/2 for i in range(3)]
lam = [a[jk(i)[0]]*a[jk(i)[1]]/a[i] for i in range(3)]
adot = [u[i]+gam[i] for i in range(3)]
udot0 = [2*H[i]/lam[i] for i in range(3)]
udot = [udot0[i]+a[i]*z[i] for i in range(3)]
L = W*sum(zz**2 for zz in z)/4

def D0(S):
    return sum(sp.diff(S, a[i])*adot[i]+sp.diff(S, u[i])*udot0[i] for i in range(3))
def Dt(S):
    return sum(sp.diff(S, a[i])*adot[i]+sp.diff(S, u[i])*udot[i] for i in range(3))
def HS(S):
    return D0(S)+sum(a[i]**2*sp.diff(S, u[i])**2 for i in range(3))/W

checks = {}
Sgen = sp.Function('S')(*a, *u)
sq = W/4*sum((z[i]-2*a[i]*sp.diff(Sgen, u[i])/W)**2 for i in range(3))
checks['H1_square_completion'] = sp.simplify(sp.expand(L-Dt(Sgen)-(sq-HS(Sgen))))
C = sum(q**2 for q in u)+u[0]*u[1]*u[2]
Phi = C-u[1]**2
checks['H2_seed_hamiltonian'] = sp.simplify(HS(-Phi)+2*u[0]*u[1]*u[2]/lam[1])
Lam = -8*sum(a[i]*H[i] for i in range(3))/W
checks['H3_Lambda_first_integral'] = sp.simplify(D0(Lam))
# s = -2 sum (r_i+v_i) with r_i = udot_i/a_i = z_i + v_i
v = [2*H[i]/(a[jk(i)[0]]*a[jk(i)[1]]) for i in range(3)]
s = -2*sum(udot[i]/a[i]+v[i] for i in range(3))
checks['H3_scalar_relation'] = sp.simplify(s-(Lam-2*sum(z)))
Ham = sum(pa[i]*adot[i]+pu[i]*udot0[i] for i in range(3))+sum(a[i]**2*pu[i]**2 for i in range(3))/W
checks['H4_scaling'] = sp.simplify(sum(a[i]*sp.diff(Ham, a[i]) for i in range(3))
                                   + Ham - sum(pa[i]*adot[i] for i in range(3)))
# maximizing control
zstar = [2*a[i]*pu[i]/W for i in range(3)]
checks['H4_max_control'] = sp.simplify(sum(pa[i]*adot[i]+pu[i]*udot[i] for i in range(3)).subs(dict(zip(z, zstar)))
                                       - L.subs(dict(zip(z, zstar)))-Ham)
# H5: example scale-invariant S
al, be = sp.symbols('alpha beta', positive=True)
Sx = sp.Function('F')(a[1]/a[0], a[2]/a[0], *u)
hs = HS(Sx)
scaled = hs.subs({a[0]: c*a[0], a[1]: c*a[1], a[2]: c*a[2]}, simultaneous=True)
checks['H5_homogeneity'] = sp.simplify(scaled*c-hs)
# (H6) On N={u1=u3=0}:  d(a1 a3)/dt = 2 a2, i.e. omega_2 = a2 dt^sigma2 + a3 a1 sigma3^sigma1
#      is closed (d(sigma3^sigma1)=0, d sigma2 = 2 sigma3^sigma1).  N is the set where the
#      Lambda^+ connection (components u_i, curvature H_i, Chern-Simons C) reduces to U(1).
onN = {u[0]: 0, u[2]: 0}
checks['H6_omega2_closed_on_N'] = sp.simplify((a[0]*adot[2]+a[2]*adot[0]).subs(onN)-2*a[1])
# (H7) N is invariant under D0, and Phi, grad_u Phi vanish on N
checks['H7_N_invariant'] = sp.simplify(udot0[0].subs(onN))+sp.simplify(udot0[2].subs(onN))
checks['H7_Phi_on_N'] = sp.simplify(Phi.subs(onN))+sum(sp.simplify(sp.diff(Phi, q).subs(onN))**2 for q in u)
# dLambda/dt with control: linear in z (contracted Bianchi identity)
dLam = sp.simplify(Dt(Lam))
print('dLambda/dt =', sp.factor(dLam))
for k, val in checks.items():
    print(k, '=', val)
if any(val != 0 for val in checks.values()):
    raise SystemExit('HJ identity failure')
