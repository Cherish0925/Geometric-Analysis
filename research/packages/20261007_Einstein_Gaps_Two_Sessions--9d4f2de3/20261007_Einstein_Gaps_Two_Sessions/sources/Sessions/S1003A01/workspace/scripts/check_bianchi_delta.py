"""Check the divergence operator used in angular_normalized_gauge.pointdata.

(1) Pure-trace modes h=phi g: delta h = -d phi.
(2) Gauge tangents h=L_X g: beta(h)=delta h+(1/2)d tr h equals the Bochner form
    -(nabla^k nabla_k X)_j - Ric_jk X^k, computed independently by autodiff.
"""
import json
import numpy as np, jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
import angular_normalized_gauge as ng
from o11_rotated_cell import curvature_scalars

REC = '../data/perp_direct/lm3_x00.038_X512_d28.json'
B = ng.build(REC, 2, 2, 4, 4, 3, 0.9, 100.0, 2, 2, True, 'col', 4)
meta = B['meta']; ntf, ntr, nkx = meta['n_tf'], meta['n_tr'], meta['n_kx']
base = B['base']; modes = B['modes']; vecf = B['vecfields']

def christ(y):
    g = base(y); gi = jnp.linalg.inv(g); dg = jax.jacfwd(base)(y)
    t = jnp.einsum('dik->dki', dg) + dg - jnp.einsum('kid->dki', dg)
    return 0.5*jnp.einsum('ld,dki->lki', gi, t)

def ricci(y):
    g = base(y); Gm = christ(y); dG = jax.jacfwd(christ)(y)   # dG[a,b,c,e]=d_e Gam^a_bc
    # R_bd = d_a Gam^a_db - d_d Gam^a_ab + Gam^a_ae Gam^e_db - Gam^a_de Gam^e_ab
    return (jnp.einsum('adba->bd', dG) - jnp.einsum('aabd->bd', dG)
            + jnp.einsum('aae,edb->bd', Gm, Gm) - jnp.einsum('ade,eab->bd', Gm, Gm))

out = []
for y in [jnp.array([0.5, 0.7, 1.1, 2.3]), jnp.array([5.0, 2.1, 0.6, 4.0]), jnp.array([0.09, 1.7, 2.2, 0.4])]:
    sig, gram, divX, F, V, dl, dF, gi = [np.asarray(t) for t in B['pointdata'](y)]
    md, _ = modes(y); g = np.asarray(base(y))
    phi = lambda yy: modes(yy)[0][ntf:ntf+ntr, 0, 0]/base(yy)[0, 0]
    dphi = np.asarray(jax.jacfwd(phi)(y))
    e1 = np.abs(dl[ntf:ntf+ntr] + dphi).max()/np.abs(dphi).max()
    # (2) Bochner for X fields
    def Xcov(yy):  # nabla_k X^a  -> [i,a,k]
        X = vecf(yy); dX = jax.jacfwd(vecf)(yy)
        return dX + jnp.einsum('aki,ji->jak', christ(yy), X) * 0 + jnp.einsum('aik,ji->jak', christ(yy), X)
    nX = Xcov(y); dnX = jax.jacfwd(Xcov)(y)      # [i,a,k,l] = d_l nabla_k X^a
    Gm = christ(y)
    # nabla_l nabla_k X^a = d_l(nabla_k X^a) + Gam^a_lm nabla_k X^m - Gam^m_lk nabla_m X^a
    nnX = dnX + jnp.einsum('alm,imk->iakl', Gm, nX) - jnp.einsum('mlk,iam->iakl', Gm, nX)
    gij = jnp.linalg.inv(base(y))
    lapX = jnp.einsum('kl,iakl->ia', gij, nnX)
    Ric = ricci(y); gm = base(y)
    X = vecf(y)
    boch = -jnp.einsum('ja,ia->ij', gm, lapX) - jnp.einsum('jk,ik->ij', Ric, X)
    LX = md[ntf+ntr:]
    trLX = jnp.einsum('ab,iab->i', gij, LX)
    # beta from code: delta of the KX tensor (trace free) + (1/2) d tr L_X g ; KX = LX - (1/2)divX g
    # delta(KX) = delta LX + (1/2) d divX ; beta(LX) = delta LX + (1/2) d tr LX = delta(KX) - (1/2) d divX + d divX
    ddiv = jax.jacfwd(lambda yy: modes(yy)[1])(y)      # d divX
    beta_code = dl[ntf+ntr:] + 0.5*np.asarray(ddiv)
    e2 = float(np.abs(beta_code - np.asarray(boch)).max()/np.abs(np.asarray(boch)).max())
    out.append(dict(y=[float(v) for v in y], trace_delta_rel=float(e1), bochner_rel=e2,
                    ric_trace=float(jnp.einsum('ab,ab->', gij, Ric))))
print(json.dumps(out, indent=1))
