"""
Step 92: exact model calculations for the full weighted separator Jacobi form.

The invariant stability inequality is
    int rho V phi^2 <= int rho[(phi_s)^2 + a phi^2],
where a=3-E_nunu and V=kappa^2+h_nu^2/2+e_nu/2+Q.
Equivalently, the lowest periodic eigenvalue of
    J = -rho^{-1}(rho phi')' + a - V
is nonnegative.

This script computes two exact comparison families on a circle of length L:
(1) constant V, where lambda_0=a-V;
(2) a square concentration V=A on an interval of width ell and zero elsewhere,
    using the exact zero-eigenvalue transfer matrix.  The latter shows that
    stability permits arbitrarily high, sufficiently narrow spikes: for small ell,
    A_crit ~ 2 sqrt(a)/ell (fixed unweighted mass), so no pointwise ceiling or
    universal width follows from stability alone.

It also records the exact tent-function Rayleigh estimate, valid for arbitrary
nonnegative V and constant rho, which controls local mass by 2/r + 2 a r.
"""
from pathlib import Path
import json
import math
from scipy.optimize import brentq
import numpy as np


def transfer_osc(k: float, length: float) -> np.ndarray:
    """Transfer for y'' + k^2 y = 0."""
    if abs(k) < 1e-14:
        return np.array([[1.0, length], [0.0, 1.0]])
    c = math.cos(k * length)
    s = math.sin(k * length)
    return np.array([[c, s / k], [-k * s, c]])


def transfer_hyp(mu: float, length: float) -> np.ndarray:
    """Transfer for y'' - mu^2 y = 0."""
    if abs(mu) < 1e-14:
        return np.array([[1.0, length], [0.0, 1.0]])
    c = math.cosh(mu * length)
    s = math.sinh(mu * length)
    return np.array([[c, s / mu], [mu * s, c]])


def trace_monodromy(A: float, ell: float, L: float, a: float) -> float:
    """Trace of zero-energy monodromy for J=-d2+a-A 1_[0,ell]."""
    outside = L - ell
    Mout = transfer_hyp(math.sqrt(a), outside)
    if A >= a:
        Min = transfer_osc(math.sqrt(A - a), ell)
    else:
        Min = transfer_hyp(math.sqrt(a - A), ell)
    return float(np.trace(Mout @ Min))


def first_critical_amplitude(ell: float, L: float, a: float) -> float:
    """First A>a with periodic zero mode: trace(monodromy)=2."""
    def f(A):
        return trace_monodromy(A, ell, L, a) - 2.0

    lo = a
    flo = f(lo)
    # Find first sign change, before possible later bands.
    grid = np.geomspace(max(a + 1e-10, 1e-10), max(a + 1e8 / ell**2, 1e4), 20000)
    prev_A, prev_f = lo, flo
    for A in grid:
        fa = f(float(A))
        if prev_f == 0:
            return prev_A
        if fa == 0 or fa * prev_f < 0:
            return float(brentq(f, prev_A, float(A), xtol=1e-13, rtol=1e-13))
        prev_A, prev_f = float(A), fa
    raise RuntimeError(f"no first crossing found for ell={ell}")


L = 2 * math.pi
a = 3.0
ells = [1.0, 0.5, 0.25, 0.125, 0.0625, 0.03125]
rows = []
for ell in ells:
    Acrit = first_critical_amplitude(ell, L, a)
    rows.append({
        "ell": ell,
        "A_crit": Acrit,
        "mass_Aell": Acrit * ell,
        "Aell_over_2sqrt_a": Acrit * ell / (2 * math.sqrt(a)),
        "Aell2": Acrit * ell * ell,
        "trace_at_critical_minus_2": trace_monodromy(Acrit, ell, L, a) - 2.0,
    })

# For phi(s)=max(1-|s-s0|/r,0), direct integrals are
# int |phi'|^2 = 2/r and int phi^2 = 2r/3 <= 2r.
# Since phi>=1/2 on |s-s0|<=r/2,
# int_{I_{r/2}} V <= 4[int |phi'|^2+a int phi^2]
# = 8/r + (8/3) a r.  The cruder Lipschitz cutoff with a plateau gives
# the same capacity scaling C(1/r+a r).
tent = {
    "phi": "max(1-|s-s0|/r,0)",
    "dirichlet_integral": "2/r",
    "L2_integral": "2r/3",
    "lower_on_inner_interval": "phi^2 >= 1/4 on |s-s0| <= r/2",
    "local_mass_bound": "int_{|s-s0|<=r/2} V ds <= 8/r + (8/3)*a*r",
    "interpretation": "capacity control only; RHS diverges as r->0",
}

out = {
    "model": "periodic circle, rho=1, J=-d2+a-V",
    "L": L,
    "a": a,
    "constant_potential": {
        "lowest_eigenvalue": "a-V0",
        "stability_condition": "V0 <= a",
    },
    "square_spike_critical_rows": rows,
    "small_width_asymptotic": "A_crit*ell -> 2*sqrt(a)*tanh(sqrt(a)*L/2); for a=3,L=2pi this is about 3.46397 (close to, but not equal to, 2sqrt(3))",
    "tent_test": tent,
    "scientific_conclusion": "The full Jacobi form strengthens the average test but does not bound sup V or impose a universal concentration width. Maxwell/scalar equations would need to supply an independent transport or regularity scale.",
}

path = Path("workspace/data/step92_jacobi_concentration_models.json")
path.parent.mkdir(parents=True, exist_ok=True)
path.write_text(json.dumps(out, indent=2), encoding="utf-8")
print(json.dumps(out, indent=2))
print(f"wrote {path}")
