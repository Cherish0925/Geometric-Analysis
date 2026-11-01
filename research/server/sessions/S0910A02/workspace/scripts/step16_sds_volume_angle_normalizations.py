"""
Step 16: volume and cone-angle normalizations for the Euclidean
Schwarzschild-de Sitter separated rod germ.

The Step-15 convention normalizes the theta-period so that the smaller
black-hole/rod bolt is smooth.  With this convention the second (cosmological)
bolt has cone angle 2*pi*mu(A), and the total block volume tends to 0 as
A->infty.  If instead the period is chosen to smooth the cosmological bolt, the
small bolt has cone angle 2*pi/mu(A), and the volume tends to Vol(S^4_Ric=g)=24*pi^2.
This script records the exact formulas so later notes do not conflate these two
normalizations.
"""
import math, json
from pathlib import Path


def vals(A):
    kappa = 1+2*A
    if A == 0:
        aplus = 1.0
        mu = 1.0
        vol_first = 16*math.pi**2
    else:
        aplus = (-1+math.sqrt(9+24*A))/2
        mu = (2*aplus+1)/(aplus*(aplus+2))
        # physical S2 metric has area 4*pi/kappa when a=1.
        # p = a'/A, so int p a^2 dr = (a_+^3-1)/(3A).
        vol_first = (2*math.pi) * (4*math.pi/kappa) * ((aplus**3-1)/(3*A))
    vol_second = vol_first/mu
    return {
        'A': A,
        'kappa': kappa,
        'a_plus': aplus,
        'mu_second_if_first_smooth': mu,
        'cone_angle_second_if_first_smooth': 2*math.pi*mu,
        'cone_angle_first_if_second_smooth': 2*math.pi/mu,
        'volume_if_first_small_bolt_smooth': vol_first,
        'volume_if_second_cosmological_bolt_smooth': vol_second,
        'volume_first_over_16pi2': vol_first/(16*math.pi**2),
        'volume_second_over_24pi2': vol_second/(24*math.pi**2),
    }

samples=[vals(A) for A in [0,0.01,0.1,0.5,1,4,9,16,100,400,10000]]
report={
    'title':'Step 16 SdS volume/angle normalizations',
    'first_smooth_convention':'theta period 2*pi at the small/black-hole bolt; second bolt cone angle 2*pi*mu; volume ->0 as A->infty',
    'second_smooth_convention':'theta period enlarged by 1/mu to smooth the cosmological bolt; first bolt cone angle 2*pi/mu; volume ->24*pi^2 as A->infty',
    'Nariai_limit':'A=0 gives mu=1 and both normalizations coincide with S2xS2, volume 16*pi^2',
    'deSitter_limit':'A->infty gives M->0. The geometric region approaches de Sitter/S4 only in the second-smooth period; in the first-smooth period the circle length collapses and volume tends 0.',
    'samples':samples,
}
out=Path('Sessions/S0910A02/workspace/data/step16_sds_volume_angle_normalizations.json')
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text(json.dumps(report, indent=2), encoding='utf-8')
print(json.dumps(report, indent=2))
print(f'Saved {out}')
