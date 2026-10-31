"""Exact jet-level Ricci tensor (numpy): input g, first and second coordinate derivatives at one point."""
import numpy as np


def ricci_from_jets(g, dg, ddg):
    """g[a,b], dg[c,a,b]=d_c g_ab, ddg[c,d,a,b]=d_c d_d g_ab  ->  (Ricci, Christoffel)."""
    gi = np.linalg.inv(g)
    dgi = -np.einsum('ab,cbd,de->cae', gi, dg, gi)
    C = 0.5 * (np.einsum('jmi->mij', dg) + np.einsum('imj->mij', dg) - dg)
    dC = 0.5 * (np.einsum('kjmi->kmij', ddg) + np.einsum('kimj->kmij', ddg) - ddg)
    Gam = np.einsum('lm,mij->lij', gi, C)
    dGam = np.einsum('klm,mij->klij', dgi, C) + np.einsum('lm,kmij->klij', gi, dC)
    Ric = (np.einsum('llik->ik', dGam) - np.einsum('klil->ik', dGam)
           + np.einsum('llm,mik->ik', Gam, Gam) - np.einsum('lkm,mil->ik', Gam, Gam))
    return Ric, Gam
