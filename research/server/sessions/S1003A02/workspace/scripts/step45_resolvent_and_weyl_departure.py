#!/usr/bin/env python3
"""Step 45 exact/numerical checks for Lemma M and the Kähler-orbit saving bound.

All complex-hyperbolic exponents are in the holomorphic-sectional-curvature -4
normalization.  The scalar radial density grows like exp(2 rho r), rho=n=2.
"""
from __future__ import annotations
import json
from pathlib import Path
import sympy as sp
from scipy.optimize import differential_evolution, minimize_scalar

# ---------- Part I: homogeneous resolvent exponents ----------
n = sp.Integer(2)
rho_hc = sp.Integer(2)
l_abs = sp.Integer(3)                 # K^{-1} has |l|=n+1
nu_discrete = l_abs - n              # lowest discrete-series parameter
landau_ground = sp.Integer(12)        # |i Lambda F_{K^-1}|, hol sect -4
# The homogeneous connection Laplacian is const-Casimir, so its eigenvalue is
# affine in -nu^2.  Calibrate on the lowest discrete series.
continuous_shift = sp.simplify(landau_ground + nu_discrete**2)
nu_zero_line = sp.sqrt(continuous_shift)
line_decay = sp.simplify(rho_hc + nu_zero_line)
line_l1_margin = sp.simplify(line_decay - 2*rho_hc)

# One-form block of L^*L at hol sect -4:
# B_1 = d d^* + 1/2 d^*d + 6.
# exact sector: Delta_1+6, with scalar/exact continuous threshold alpha_0=rho^2=4;
# coexact sector: 1/2(Delta_1+12), with alpha_1=1 on CH^2.
alpha_scalar = rho_hc**2
alpha_one = sp.Integer(1)
s_exact = sp.sqrt(alpha_scalar + 6)
s_coexact = sp.sqrt(alpha_one + 12)
exact_decay = sp.simplify(rho_hc + s_exact)
coexact_decay = sp.simplify(rho_hc + s_coexact)
exact_l1_margin = sp.simplify(exact_decay - 2*rho_hc)
coexact_l1_margin = sp.simplify(coexact_decay - 2*rho_hc)

# Verify the direct inverse identity in formal commuting variables x and y,
# where y=d d^*, y=x on exact forms and y=0 on coexact forms.
x, y = sp.symbols('x y', nonnegative=True)
B = sp.Rational(1,2)*x + sp.Rational(1,2)*y + 6
# Candidate: 2(Delta_1+12)^-1 - d(Delta_0+6)^-1(Delta_0+12)^-1 d^*.
# On a one-form eigenmode the second term has multiplier -y/((x+6)(x+12)).
Binv = sp.Rational(2,1)/(x+12) - y/((x+6)*(x+12))
identity_exact = sp.factor((B*Binv - 1).subs(y, x))
identity_coexact = sp.factor((B*Binv - 1).subs(y, 0))

# ---------- Part II: pointwise Theorem-W saving near the Kähler orbit ----------
r, q, t = sp.symbols('r q t', real=True)
pamp = (2-r)*(r-1)*(3*r+2)/3
f_star = sp.factor(r**2*q - r**2/3 - sp.Rational(8,3) + pamp)
expected = -((2-r)**2*(r+1) + r**2*(1-q))
f_star_residual = sp.factor(f_star - expected)
# Linear coefficient G=r^2 K_n - 8 W_*. Its norm depends only on q=<n,w>^2.
G2 = sp.factor(sp.Rational(2,3)*r**4 + sp.Rational(128,3)
               -16*r**2*(q-sp.Rational(1,3)))
G2_canonical = sp.simplify(G2.subs({r:2,q:1}))
G2_boxmax = sp.simplify(G2.subs({r:2,q:0}))

# For f=f_*+G.E-4|E|^2, the best coefficient in f <= C|E| for a fixed
# (r,q) is max(0, |G|-4 sqrt(-f_*)). Numerically maximize it on [0,2]x[0,1].
def c_eff(z):
    rv, qv = z
    fst = -((2-rv)**2*(rv+1) + rv**2*(1-qv))
    g2 = (2/3)*rv**4 + 128/3 - 16*rv**2*(qv-1/3)
    return max(0.0, g2**0.5 - 4*(-fst)**0.5)
res = differential_evolution(lambda z: -c_eff(z), [(0,2),(0,1)],
                             tol=1e-13, polish=True, seed=451, workers=1)
r_opt, q_opt = map(float, res.x)
Csharp_num = float(-res.fun)
# Boundary scans to identify the maximizer robustly.
boundaries = {}
for name, fun in {
    'q=0': lambda rv: c_eff((rv,0.0)),
    'q=1': lambda rv: c_eff((rv,1.0)),
    'r=0': lambda qv: c_eff((0.0,qv)),
    'r=2': lambda qv: c_eff((2.0,qv)),
}.items():
    upper = 2 if name.startswith('q=') else 1
    rr = minimize_scalar(lambda z: -fun(z), bounds=(0,upper), method='bounded',
                         options={'xatol':1e-14})
    boundaries[name] = {'argmax':float(rr.x),'max':float(-rr.fun)}

# Exact canonical coefficient and the global crude gradient coefficient.
Ccanonical = sp.sqrt(G2_canonical)
Cgradient = sp.sqrt(G2_boxmax)

out = {
    'normalization': {
        'space':'CH^2, holomorphic sectional curvature -4',
        'rho_half_volume_growth':str(rho_hc),
        'volume_growth_exponent':str(2*rho_hc),
    },
    'Kminus1_line_sector': {
        'homogeneous_character_abs_l':str(l_abs),
        'lowest_discrete_parameter_abs_l_minus_n':str(nu_discrete),
        'landau_ground':str(landau_ground),
        'continuous_shift_H_of_nu_equals_shift_minus_nu2':str(continuous_shift),
        'zero_energy_nu':str(nu_zero_line),
        'green_decay_exponent':str(line_decay),
        'L1_margin_over_volume_growth':str(line_l1_margin),
        'numeric_margin':float(sp.N(line_l1_margin,20)),
    },
    'one_form_sector': {
        'operator':'B1=dd*+(1/2)d*d+6',
        'inverse_identity':'B1^{-1}=2(Delta_1+12)^{-1}-d(Delta_0+6)^{-1}(Delta_0+12)^{-1}d*',
        'identity_residual_exact':str(identity_exact),
        'identity_residual_coexact':str(identity_coexact),
        'exact_decay_exponent':str(exact_decay),
        'exact_L1_margin':str(exact_l1_margin),
        'coexact_decay_exponent':str(coexact_decay),
        'coexact_L1_margin':str(coexact_l1_margin),
        'numeric_margins':{
            'exact':float(sp.N(exact_l1_margin,20)),
            'coexact':float(sp.N(coexact_l1_margin,20)),
        },
    },
    'kahler_orbit_saving': {
        'f_star_factorization_residual':str(f_star_residual),
        'f_star':'-(2-r)^2(r+1)-r^2(1-q)',
        'G_norm_squared':str(G2),
        'canonical_G_norm_squared':str(G2_canonical),
        'boxmax_G_norm_squared':str(G2_boxmax),
        'canonical_linear_coefficient':str(Ccanonical),
        'global_gradient_coefficient':str(Cgradient),
        'sharp_ratio_coefficient_numerical':Csharp_num,
        'optimizer':{'rho':r_opt,'q_cos2':q_opt},
        'boundary_checks':boundaries,
        'interpretation':'Pointwise pure quadratic control by |E|^2 is impossible: at rho=2,n=omega, f=4E(omega,omega)-4|E|^2. The sharp linear ratio is attained at this canonical state.',
    }
}

path = Path(__file__).resolve().parents[1]/'data'/'step45_resolvent_and_weyl_departure.json'
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
