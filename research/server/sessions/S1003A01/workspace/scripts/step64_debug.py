import os, sys, json
import numpy as np
import jax, jax.numpy as jnp
jax.config.update("jax_enable_x64", True)
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import step62_zero_prolong as Z
D = 3
S = Z.setup(D); P = S["P"]; nvar = S["nvar"]
idx = np.where(P.deg >= 2)[0]; coldeg = np.tile(P.deg[idx], 16)
keep = S["keep"]; rt = S["rowtype"][keep]; rd = S["rowdeg"][keep]
level = np.where(rt == 1, rd, np.where(rt == 2, rd + 1, rd + 2))
sysf = lambda z: S["system"](z, 0.0)[jnp.array(keep)]
J = np.asarray(jax.jacfwd(sysf)(jnp.zeros(nvar)))
c3 = np.where(coldeg == 3)[0]; r3 = np.where(level == 3)[0]
print("rows level3", len(r3), "by type", [(t, int(((rt[r3]) == t).sum())) for t in (1, 2, 3)])
A3 = J[np.ix_(r3, c3)]
U, s, Vt = np.linalg.svd(A3); r = int((s > 1e-9*s[0]).sum()); K = Vt[r:].T
print("rank", r, "kernel", K.shape[1])
d2 = [c for c in range(P.M) if P.deg[c] == 2]
def tors(z):
    g, w = S["unpack"](z)
    dg = jnp.stack([P.d(g, k) for k in range(4)], 0)
    Gl = 0.5*(jnp.einsum('jlkp->ljkp', dg) + jnp.einsum('kljp->ljkp', dg) - dg)
    dw = jnp.stack([P.d(w, k) for k in range(4)], 0)
    T = dw - jnp.einsum('mkip,mj->kijp', Gl, jnp.array(Z.W0)) - jnp.einsum('mkjp,im->kijp', Gl, jnp.array(Z.W0))
    T = T[..., jnp.array(d2)]
    return jnp.stack([0.25*jnp.einsum('kijp,ij->kp', T, jnp.array(M)) for M in (Z.PHI, Z.PSI, Z.W0)])
F = np.asarray(jax.jacfwd(lambda z: tors(z).ravel())(jnp.zeros(nvar)))[:, c3]
FK = F @ K
na = 40
for nm, sl in [("a", slice(0, na)), ("psi", slice(na, 2*na)), ("om", slice(2*na, 3*na))]:
    print(nm, "rank", np.linalg.matrix_rank(FK[sl], 1e-9), "max", np.abs(FK[sl]).max())
# E1 check of a kernel vector
z = np.zeros(nvar); z[c3] = K[:, 0]
res = np.asarray(sysf(jnp.array(z)))
print("res on kernel vec", np.abs(res).max())
# gauge: x -> x + V(x), V quartic: delta g_ij = d_i V_j + d_j V_i (deg 3), delta w_ij = V^k d_k w + w_kj d_i V^k + w_ik d_j V^k (deg 3 part from w0)
