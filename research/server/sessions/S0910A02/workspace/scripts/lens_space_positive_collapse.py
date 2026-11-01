#!/usr/bin/env python3
"""
Round lens spaces as an exact positive-Einstein collapse model for Yau26.

Purpose: correct the false inference from the fixed-topology Berger computation.
The quotient S^3/Z_m with the round metric is exactly Einstein for every m,
while volume and injectivity radius go to zero. After scaling by 2, Ric=g, so
δ_+=0 exactly in the normalized positive branch.
"""
from __future__ import annotations
import math

print("Round lens spaces L(m,1)=S^3/Z_m with normalized metric h=2*g_round")
print("Ric_h = h exactly, so delta_+(h)=0 for every m; nevertheless inj and volume collapse.")
print(f"{'m':>6} {'delta_+':>9} {'Vol(h)':>14} {'inj(h)':>14} {'diam_bound_note':>18}")
print("-"*70)
for m in [1,2,3,5,10,20,50,100,1000,10000]:
    vol_round = 2*math.pi**2/m
    inj_round = math.pi/m if m >= 2 else math.pi
    # h=2*g_round, lengths scale sqrt(2), volumes scale 2^(3/2)
    vol_h = (2**1.5)*vol_round
    inj_h = math.sqrt(2)*inj_round
    print(f"{m:6d} {0.0:9.1f} {vol_h:14.8e} {inj_h:14.8e} {'Ric=h exact':>18}")
print("\nConclusion: tight positive Ricci pinching permits collapse. The relevant")
print("positive-branch problem is to understand whether such collapse is always")
print("Einstein-compatible in topology/quotient/orbifold-bundle structure, not to")
print("exclude collapse by Ricci anisotropy alone.")
