"""Step 47: second-jet null compatibility of delta = sum_i P_i (x) (Phi ^ P_i) at the calibrated endpoint.

Pointwise algebra in the corpus Clifford convention (S^+ -> S^-):
  C1=I, C2=diag(i,-i), C3=[[0,1],[-1,0]], C4=[[0,-i],[-i,0]].
Phi=(sqrt(rho),0) in the frame (u,u_perp); P_i=(alpha_i,beta_i); H_ji=nabla_j P_i=(h_ji,k_ji).
Dirac: sum_i C_i P_i = 0;  differentiated Dirac: sum_i C_i H_ji = 0 for each j.
nabla_j delta = sum_i [H_ji w_i + P_i (P_j ^ P_i + Phi ^ H_ji)],  w_i = Phi ^ P_i  (X^Y = X1 Y2 - X2 Y1).
We impose the calibrated first jet alpha=0, beta=(t,-it,0,0), and test
 (A) zeta-stationary Hessian h_ji = -conj(beta_j) beta_i / sqrt(rho), k free subject to Dirac;
 (B) arbitrary h (no zeta stationarity), k subject to Dirac.
Output: workspace/data/step47/second_jet_null.json
"""
import json, os
import sympy as sp
t, rho = sp.symbols('t rho', positive=True)
sr = sp.sqrt(rho)
C = [sp.eye(2), sp.diag(sp.I, -sp.I), sp.Matrix([[0, 1], [-1, 0]]), sp.Matrix([[0, -sp.I], [-sp.I, 0]])]
alpha = [0, 0, 0, 0]
beta = [t, -sp.I*t, 0, 0]
P = [sp.Matrix([alpha[i], beta[i]]) for i in range(4)]
Phi = sp.Matrix([sr, 0])
def wedge(X, Y):
    return X[0]*Y[1] - X[1]*Y[0]
assert sp.simplify(sum((C[i]*P[i] for i in range(4)), sp.zeros(2, 1))) == sp.zeros(2, 1)
def run(hmode):
    out = {}
    for j in range(4):
        if hmode == 'stationary':
            h = [-sp.conjugate(beta[j])*beta[i]/sr for i in range(4)]
        else:
            h = list(sp.symbols(f'h{j}_0:4'))
        k = list(sp.symbols(f'k{j}_0:4'))
        H = [sp.Matrix([h[i], k[i]]) for i in range(4)]
        eqs = list(sum((C[i]*H[i] for i in range(4)), sp.zeros(2, 1)))
        sol = sp.solve(eqs, [k[1], k[3]], dict=True)[0]   # Dirac fixes k1,k3 in terms of the rest
        w = [wedge(Phi, P[i]) for i in range(4)]
        nd = sp.zeros(2, 1)
        for i in range(4):
            nd += H[i]*w[i] + P[i]*(wedge(P[j], P[i]) + wedge(Phi, H[i]))
        nd = sp.simplify(nd.subs(sol))
        out[f'j={j+1}'] = [str(sp.simplify(nd[0])), str(sp.simplify(nd[1]))]
    return out
res = dict(stationary_hessian=run('stationary'), arbitrary_hessian=run('free'))
print(json.dumps(res, indent=1))
here = os.path.dirname(os.path.abspath(__file__))
od = os.path.join(here, '..', 'data', 'step47'); os.makedirs(od, exist_ok=True)
with open(os.path.join(od, 'second_jet_null.json'), 'w') as fh:
    json.dump(res, fh, indent=1)
