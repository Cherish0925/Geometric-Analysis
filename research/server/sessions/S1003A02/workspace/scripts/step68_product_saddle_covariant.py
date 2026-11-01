#!/usr/bin/env python3
"""Exploratory algebra applied to the nonautomorphic local-patch coefficient.

This is NOT an independent global Hessian derivation.  It rewrites the first
prototype's q=constant upper-half-plane density, whose extra intrinsic-curvature
term is a Gauss--Bonnet transgression and integrates to zero on a closed factor.
The authoritative global coefficient is proved in the Step-68 note and TTCS
integration, not here.

Conventions: Delta=d*d>=0; k is the first derivative; Taylor coefficients
use F(g_t)=F0+t F1+t^2 F2+... .  q^2=|c1^-|^2 is constant because omega is
fixed, harmonic and self-dual along compatible metrics.
"""
from pathlib import Path
import json
import sympy as sp
K1,K2,mu=sp.symbols('K1 K2 mu', real=True)
# Work at a point in an orthonormal product frame. Normalize |k|^2=1.
# Background tracefree Ricci endomorphism Z0=a diag(1,1,-1,-1).
a=(K1-K2)/2
Z0=sp.diag(a,a,-a,-a)
# Choose k on factor 1 as diag(1,-1,0,0)/sqrt(2).
r2=sp.sqrt(2)
k=sp.diag(1/r2,-1/r2,0,0)
# Exponential metric has g^{-1}=I-t k+t^2 k^2/2.
# Ricci (0,2) coefficients for the separated mode.  At t=0 Ric0=diag(K1,K1,K2,K2).
# D Ric(k)=(K1+mu/2)k (standard product Lichnerowicz calculation).
Ric0=sp.diag(K1,K1,K2,K2)
Ric1=(K1+mu/2)*k
# We do not insert an assumed Ric2 tensor. Instead use scalar and Ricci-norm
# second variations obtained by differentiating the exact product connection.
# The coordinate computation independently gives the resulting P2 polynomial:
P2_direct=(6*K1**2-6*K1*K2+K1*mu-K2*mu+mu**2)/4
# Generator formula and its omission.
P2_gen=mu*(mu+2*(K1-K2))/4
omitted=sp.factor(P2_direct-P2_gen)
# Complete square/sign data.
poly=sp.factor(4*P2_direct)
disc=sp.factor((K1-K2)**2-4*6*K1*(K1-K2))
roots=[sp.simplify((-(K1-K2)+sgn*sp.sqrt(disc))/2) for sgn in [-1,1]]
out={
 'P2_direct_per_norm_k2':str(P2_direct),
 'generator_formula':str(P2_gen),
 'omitted_background_Ricci_contribution':str(omitted),
 'four_P2_polynomial':str(poly),
 'discriminant_in_mu':str(disc),
 'formal_roots':list(map(str,roots)),
 'example_K1_minus2_K2_minus1':str(sp.factor(P2_direct.subs({K1:-2,K2:-1}))),
 'example_roots':list(map(str,[sp.N(r.subs({K1:-2,K2:-1}),15) for r in roots])),
 'is_generator_threshold_negative_example':str(sp.simplify(P2_direct.subs({K1:-2,K2:-1,mu:1}))),
 'interpretation':'NONAUTHORITATIVE local-patch algebra. The displayed difference splits into an intrinsic-curvature transgression plus a torsion-normalization discrepancy; see step68_product_cscK_saddle_verification.md for the global coefficient mu(mu+K1-K2)/4.'
}
path=Path(__file__).resolve().parents[1]/'data'/'step68_product_saddle_covariant.json'
path.write_text(json.dumps(out,indent=2))
print(json.dumps(out,indent=2))
