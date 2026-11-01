"""Step 62: evaluate the predicted zero identity on the admissible first-torsion-jet space L.

Prediction (Laplacian of q = 4<W+u,u> - 2s/3 at a torsion zero, with Einstein Weitzenbock
 nabla^*nabla W+ = -(s/2)W+ + 6 W+^2 - 2 tr(W+^2) Id  and  nabla^*nabla u = 2W+u - (s/3)u):
    |nabla^2 Omega|^2 = 4 tr(V^2) - 12 |eta|^2 ,   V = trace-free block of W+ on Omega^perp.
Here |nabla^2 Omega|^2 = sum_{k,l} |nabla_k nabla_l Omega|^2 (form norm, |Omega|^2=2) = |Mvec|^2/2.
Phi(M) := |Mvec|^2/2 - 4 trV^2 + 12|eta|^2 must vanish on admissible jets.
"""
import os, json
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.join(HERE, "..", "data", "step62")
L = np.load(os.path.join(OUT, "linear.npz"))
G = L["G"]  # (eta1, eta2, W3a, W3b) = G @ Mvec ; W3a=(V11-V22)/2, W3b=V12 ; trV^2 = 2(W3a^2+W3b^2)
def Phi_form(B):
    E = G @ B
    eta = E[:2]; w3 = E[2:]
    Q = 0.5*B.T @ B - 4*2*(w3.T @ w3) + 12*(eta.T @ eta)
    return Q
out = {}
for name in ["Llin", "A", "S", "Lb"]:
    B = L[name]; Q = Phi_form(B); ev = np.linalg.eigvalsh((Q + Q.T)/2)
    E = G @ B
    out[name] = {"dim": int(B.shape[1]), "Phi_eigs": ev.tolist(),
                 "half_norm_eigs": np.linalg.eigvalsh(0.5*B.T @ B).tolist(),
                 "trV2_eigs": np.linalg.eigvalsh(2*E[2:].T @ E[2:]).tolist(),
                 "eta2_eigs": np.linalg.eigvalsh(E[:2].T @ E[:2]).tolist()}
gh = json.load(open(os.path.join(OUT, "gh_D4.json")))
m = np.concatenate([np.array(gh["Mmat"]).ravel(), np.array(gh["Npsi"]).ravel()])
E = G @ m
out["gh"] = {"half_norm": float(0.5*m @ m), "eta": E[:2].tolist(), "W3": E[2:].tolist(),
             "Phi": float(0.5*m @ m - 8*E[2:] @ E[2:] + 12*E[:2] @ E[:2]),
             "S_component_norm": float(np.linalg.norm(L["S"].T @ m)), "A_component_norm": float(np.linalg.norm(L["A"].T @ m)),
             "c_component_norm": float(np.linalg.norm(L["Llin"].T @ m))}
print(json.dumps(out, indent=1))
OUT2 = os.path.join(HERE, "..", "data", "step62b"); os.makedirs(OUT2, exist_ok=True)
json.dump(out, open(os.path.join(OUT2, "phi_prediction.json"), "w"), indent=1)
