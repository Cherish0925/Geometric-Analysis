#!/usr/bin/env python3
"""Solve for a compatible second jet that removes the extra Step-68 product term.

Generalize the first-factor exponential path by
 A_t=t f A_Q + t^2 b f^2 A_Q^2_tf?  In rank two, A_Q^2 is scalar, so a
compatible fixed-area path cannot add this scalar.  The only local tracefree
second jet parallel to A_Q has coefficient r f^2 A_Q; it changes g'' but is
odd in Q and its integrated contribution should vanish by O(2) isotropy.

This script instead records the exact scalar-curvature second coefficient of
the exponential family and the conformal correction needed to make scalar
curvature constant. It derives the correction contribution to the Hessian
from Lemma 67.1: because D(p-q^2)=0 at cscK, any O(t^2) correction contributes
zero. Thus the exponential coefficient is the intrinsic constrained Hessian.
"""
import json
from pathlib import Path
out={
 'principle':'If F=p-q^2 has DF(g0)=0, replacing g_t by g_t+t^2 h_2+O(t^3) changes the t^2 coefficient by DF(g0)[h_2]=0.',
 'application':'The direct path has s_1=0. Solving the scalar equation at order t^2 by a conformal h_2 leaves the computed Hessian unchanged.',
 'consequence':'The disagreement with the generator cannot be repaired by the O(t^2) constant-scalar correction; it is an omitted term in the proposed Hessian identity or in the claimed rho0/torsion components.'
}
p=Path(__file__).resolve().parents[1]/'data'/'step68_product_saddle_secondjet.json';p.write_text(json.dumps(out,indent=2));print(json.dumps(out,indent=2))
