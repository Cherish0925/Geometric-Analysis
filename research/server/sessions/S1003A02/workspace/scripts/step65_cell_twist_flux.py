#!/usr/bin/env python3
"""Step 65: exceptional-flux ledger of the certified perpendicular CH cell.

Input : A01 floating record of the x0=.03, X=128, degree-20 perpendicular cell
        (Sessions/S1003A01/workspace/data/perp_area/x00.03_X128_d20.json),
        reconstructed with A01's DualCell profile (read-only import).
Output: workspace/data/step65_cell_twist_flux.json

Geometry. Diagonal Bianchi IX, g = dt^2 + sum a_i^2 s_i^2, ds_i = 2 s_j^s_k,
slots (1,2,3) = (bolt, transverse, CH fibre).  Lambda^+ := chirality spanned by
w_i = e0^ei + ej^ek; its connection is  nabla w_i = -A_k w_j + A_j w_k,
A_k = -(v_k/a_k) e_k, v_k = adot_k - gamma_k, gamma_i=(a_j^2+a_k^2-a_i^2)/(a_j a_k).
In CH, w_3 = Kahler form (parallel).  At the bolt (a_1 -> 0) w_1 is smooth and
is the Burns Kahler direction; w_2, w_3 rotate (singular there).

Curvature operator: R(w_i^+) = R^+_i w_i^+ + m_i w_i^-, with
  R^+_i = (1/2)[-vdot_i/a_i - (2v_i + v_j v_k)/(a_j a_k)],
  m_i   = (1/2)[-vdot_i/a_i + (2v_i + v_j v_k)/(a_j a_k)]  (= (r_0+r_i)/2),
both cross-checked against the coordinate Ricci tensor below.

Almost-complex structures J_theta with Kahler form Omega = cos(th) w_1 + sin(th) w_3,
th = 0 at the bolt and th = pi/2 in the CH exterior (J = J_CH, Kahler, outside).
Twist t = alpha ^ beta with  alpha = Dn.e_phi, beta = Dn.e_psi, e_phi=(0,1,0),
e_psi = n x e_phi; the sign sigma in gamma_J = R(Omega) + sigma t is fixed by
d gamma_J = 0 (tested numerically).

Exceptional harmonic ASD form: the unique invariant closed ASD form smooth at the
bolt is h = phi w_1^-, phi = -G_h/(a_2 a_3), G_h' = -2 a_1 G_h/(a_2 a_3),
G_h(0) = 1/pi  (period of h on E equal to 1).  On a closed X#CP2bar obtained by
inserting the cell in a ball quotient, the SU(2)-average of the global harmonic
representative on the ball equals this h, so pairings with invariant forms
supported in the ball are exact.  Identity tested:  <gamma_J^-, h> = 2 pi c1(J).E = 2 pi.
"""
from pathlib import Path
import json, sys
import numpy as np
import jax
import jax.numpy as jnp
jax.config.update('jax_enable_x64', True)

HERE = Path(__file__).resolve().parent
WS = HERE.parent
PEER = WS.parents[1] / 'S1003A01' / 'workspace'
sys.path.insert(0, str(PEER / 'scripts'))
from perp_dual_cost import make_cell, load_record, seed_vector  # noqa: E402

PI = np.pi
REC = Path(sys.argv[1]) if len(sys.argv) > 1 else PEER / 'data' / 'perp_area' / 'x00.03_X128_d20.json'
OUT = Path(sys.argv[2]) if len(sys.argv) > 2 else WS / 'data' / 'step65_cell_twist_flux.json'
QUICK = '--quick' in sys.argv

rec = load_record(REC)
x0 = float(rec['x0']); X = float(rec['X']); deg = int(rec.get('deg', 6))
cell = make_cell(x0, deg, 400, smooth_mode=True, X=X)
prof = cell.prof_factory(jnp.asarray(seed_vector(cell, rec)))


def GA(x):
    """(G, a) with a = (bolt, transverse, CH fibre); exact CH beyond X."""
    def inside(x):
        G, h = prof(x)
        return G, jnp.sqrt(jnp.diag(h))
    def outside(x):
        return x + x*x, jnp.sqrt(jnp.array([x, x, x + x*x]))
    Gi, ai = inside(jnp.minimum(x, X))
    Go, ao = outside(x)
    w = x > X
    return jnp.where(w, Go, Gi), jnp.where(w, ao, ai)


def ddt(f):
    """d/dt of a function of x (dt = dx / (2 sqrt G))."""
    def g(x):
        G, _ = GA(x)
        return 2*jnp.sqrt(G)*jax.jacfwd(f)(x)
    return g


def a_of(x): return GA(x)[1]
adot = ddt(a_of)


def gam(x):
    a = a_of(x); a1, a2, a3 = a
    return jnp.array([(a2**2+a3**2-a1**2)/(a2*a3), (a3**2+a1**2-a2**2)/(a3*a1),
                      (a1**2+a2**2-a3**2)/(a1*a2)])


def vfun(x): return adot(x) - gam(x)
vdot = ddt(vfun)
addot = ddt(adot)


def curv(x):
    a = a_of(x); v = vfun(x); vd = vdot(x)
    vj = jnp.roll(v, -1); vk = jnp.roll(v, -2); aj = jnp.roll(a, -1); ak = jnp.roll(a, -2)
    Rp = 0.5*(-vd/a - (2*v + vj*vk)/(aj*ak))
    m = 0.5*(-vd/a + (2*v + vj*vk)/(aj*ak))
    return Rp, m


def ricci_check(x):
    a = a_of(x); ad = adot(x); add = addot(x)
    y = ad/a
    yt = add/a - y*y
    S = jnp.sum(y); W = jnp.prod(a)
    aj = jnp.roll(a, -1); ak = jnp.roll(a, -2)
    P = 2*(a**4 - (aj**2-ak**2)**2)/W**2
    R00 = -jnp.sum(yt + y*y); Rii = -yt - S*y + P
    s = R00 + jnp.sum(Rii)
    r0 = R00 - s/4; ri = Rii - s/4
    return s, (r0 + ri)/2, jnp.sum(jnp.concatenate([jnp.array([r0]), ri])**2)


def make_theta(za, zb):
    def th(x):
        u = jnp.clip((jnp.log(x) - za)/(zb - za), 0.0, 1.0)
        return 0.5*PI*(10*u**3 - 15*u**4 + 6*u**5)
    return th


def comps(theta, sigma):
    thdot = ddt(theta)
    def f(x):
        a = a_of(x); v = vfun(x); Rp, m = curv(x)
        th = theta(x); td = thdot(x); c, s = jnp.cos(th), jnp.sin(th)
        a1, a2, a3 = a; v1, v2, v3 = v
        t1m = 0.5*(s*td*v1/a1 - c*v2*v3/(a2*a3))
        t3m = 0.5*(-c*td*v3/a3 - s*v1*v2/(a1*a2))
        t1p = 0.5*(s*td*v1/a1 + c*v2*v3/(a2*a3))
        t3p = 0.5*(-c*td*v3/a3 + s*v1*v2/(a1*a2))
        g1p = c*Rp[0] + sigma*t1p; g1m = c*m[0] + sigma*t1m
        g3p = s*Rp[2] + sigma*t3p; g3m = s*m[2] + sigma*t3m
        return jnp.array([t1m, t3m, t1p, t3p, g1p, g1m, g3p, g3m, c*m[0], s*m[2]])
    def closed_res(x):
        a = a_of(x)
        def G1(xx):
            q = f(xx); aa = a_of(xx); return (q[4]-q[5])*aa[1]*aa[2]
        def G3(xx):
            q = f(xx); aa = a_of(xx); return (q[6]-q[7])*aa[0]*aa[1]
        q = f(x)
        r1 = ddt(G1)(x) - 2*(q[4]+q[5])*a[0]
        r3 = ddt(G3)(x) - 2*(q[6]+q[7])*a[2]
        scale = 1 + jnp.abs(ddt(G1)(x)) + jnp.abs(ddt(G3)(x))
        return jnp.array([r1, r3])/scale
    return f, closed_res


# ---------------- grid -----------------
ell = np.log(X/x0)
un = np.unique(np.concatenate([np.geomspace(1e-11, 1e-3, 700), np.geomspace(1e-3, 5e-2, 700),
                               np.linspace(5e-2, 1.0, 6000)]))
xin = x0*np.exp(ell*un)
zout = np.linspace(np.log(X), np.log(1e12), 6001)[1:]
xs = np.concatenate([xin, np.exp(zout)])
z = np.log(xs)
XJ = jnp.asarray(xs)

Gv, av = [np.asarray(t) for t in jax.vmap(GA)(XJ)]
dtdz = xs/(2*np.sqrt(Gv))                          # dt/dz
vol = 2*PI**2*np.prod(av, axis=1)*dtdz             # d mu / dz
Rp, m = [np.asarray(t) for t in jax.vmap(curv)(XJ)]
sC, mC, ric2 = [np.asarray(t) for t in jax.vmap(ricci_check)(XJ)]
v = np.asarray(jax.vmap(vfun)(XJ))


def trap(y): return float(np.sum(0.5*(y[1:]+y[:-1])*np.diff(z)))


def cumtrap(y): return np.concatenate([[0.0], np.cumsum(0.5*(y[1:]+y[:-1])*np.diff(z))])


checks = {
    'max_rel_m_vs_ricci': float(np.max(np.abs(m - mC))/np.max(np.abs(mC))),
    'max_trace_Rplus_minus_s_over_4': float(np.max(np.abs(Rp.sum(1) - sC/4))),
    'P_from_4sum_m2': trap(4*np.sum(m*m, 1)*vol)/(8*PI**2),
    'P_from_ricci': trap(ric2*vol)/(8*PI**2),
    'P_record': rec.get('P'),
}

# exceptional harmonic ASD form
I = cumtrap(av[:, 0]/(av[:, 1]*av[:, 2])*dtdz)
G0 = 1/PI
Gh = G0*np.exp(-2*I)
phi = -Gh/(av[:, 1]*av[:, 2])
h_norm2_cell = trap(2*phi**2*vol)
checks['h_norm2_cell'] = h_norm2_cell
checks['h_norm2_formula_1_minus_ratio2'] = 1 - (Gh[-1]/G0)**2
checks['Ginf_over_G0'] = float(Gh[-1]/G0)

# exceptional Ricci flux of J_1 (theta = 0 on the Ricci support)
FE = trap(2*m[:, 0]*phi*vol)
twist_J1_density = 2*(-0.5*v[:, 1]*v[:, 2]/(av[:, 1]*av[:, 2]))*phi*vol
P = checks['P_from_ricci']*8*PI**2
rho_full_m1 = trap(2*m[:, 0]**2*vol)

profiles = {
    'early_bolt_layer': (np.log(x0), np.log(x0)+0.7),
    'core_scale': (np.log(x0)+0.7, np.log(x0)+2.5),
    'mid_cell': (np.log(1.0), np.log(10.0)),
    'outer_cell': (np.log(20.0), np.log(X)),
    'late_CH_exterior': (np.log(X)+0.5, np.log(X)+3.0),
}

res = {}
for sigma in (+1.0, -1.0):
    f, cr = comps(make_theta(*profiles['core_scale']), sigma)
    sub = XJ[::97]
    r = np.asarray(jax.vmap(cr)(sub))
    res[sigma] = float(np.nanmax(np.abs(r)))
checks['closedness_residual_sigma_plus'] = res[1.0]
checks['closedness_residual_sigma_minus'] = res[-1.0]
sigma = 1.0 if res[1.0] < res[-1.0] else -1.0
checks['sigma_selected'] = sigma

out_prof = {}
for name, (za, zb) in ([] if QUICK else profiles.items()):
    f, cr = comps(make_theta(za, zb), sigma)
    q = np.asarray(jax.vmap(f)(XJ))
    t1m, t3m, t1p, t3p, g1p, g1m, g3p, g3m, rho1, rho3 = q.T
    tau = trap(2*sigma*t1m*phi*vol)
    Fr = trap(2*rho1*phi*vol)
    tm2 = trap(2*(t1m**2 + t3m**2)*vol)
    tp2 = trap(2*(t1p**2 + t3p**2)*vol)
    rho2 = trap(2*(rho1**2 + rho3**2)*vol)
    dens = 2*sigma*t1m*phi*vol
    cs = cumtrap(dens)
    def zq(qq):
        if abs(cs[-1]) < 1e-300: return None
        k = np.searchsorted(cs/cs[-1], qq); k = min(k, len(xs)-1)
        return float(xs[k]/x0)
    out_prof[name] = {
        'window_x': [float(np.exp(za)), float(np.exp(zb))],
        'ricci_flux_<rho0,h>': Fr, 'twist_flux_<t-,h>': tau,
        'identity_sum_over_2pi': (Fr + tau)/(2*PI),
        'norm_t_minus': float(np.sqrt(tm2)), 'norm_t_plus': float(np.sqrt(tp2)),
        'harmonic_efficiency_tau_over_|t-|norm_h': tau/np.sqrt(tm2)/np.sqrt(h_norm2_cell) if tm2 > 0 else None,
        'norm2_rho0': rho2, 'P_over_2': P/2,
        'half_norm2_Ric_anti_invariant': P/2 - rho2,
        'twist_flux_quantiles_x_over_x0': {str(qq): zq(qq) for qq in (0.1, 0.5, 0.9)},
    }

# J-independent ledger with theta=0 on the Ricci support
hn = np.sqrt(h_norm2_cell)
ledger = {
    'F_E_ricci_flux_over_2pi': FE/(2*PI),
    'tau_J1_over_2pi': trap(sigma*twist_J1_density)/(2*PI),
    'p': P/(8*PI**2),
    'hodge_lower_bound_(F_E/2pi)^2/|h|^2': (FE/(2*PI))**2/h_norm2_cell,
    'hodge_lower_bound_global_|h|=1': (FE/(2*PI))**2,
    'fraction_of_P_in_w1_block': 4*rho_full_m1/P/2,
    'loss_nonharmonic_over_4pi2': (P/2 - FE**2/h_norm2_cell)/(4*PI**2),
}
cs = cumtrap(sigma*twist_J1_density)
ledger['tau_J1_quantiles_x_over_x0'] = {str(qq): float(xs[min(np.searchsorted(cs/cs[-1], qq), len(xs)-1)]/x0)
                                        for qq in (0.1, 0.25, 0.5, 0.75, 0.9)}
csm = cumtrap(2*m[:, 0]*phi*vol)
ledger['F_E_quantiles_x_over_x0'] = {str(qq): float(xs[min(np.searchsorted(csm/csm[-1], qq), len(xs)-1)]/x0)
                                     for qq in (0.1, 0.5, 0.9)}
csP = cumtrap(ric2*vol)
ledger['P_quantiles_x_over_x0'] = {str(qq): float(xs[min(np.searchsorted(csP/csP[-1], qq), len(xs)-1)]/x0)
                                   for qq in (0.1, 0.5, 0.9)}
# sign structure of twist density
ledger['F_E_sup_over_J_over_2pi_(int 2|m1 phi|)'] = trap(2*np.abs(m[:, 0]*phi)*vol)/(2*PI)
incell = xs <= X
t1_J1 = -0.5*v[:, 1]*v[:, 2]/(av[:, 1]*av[:, 2])   # J_1 twist is pure w_1^- on the cell
tn = np.sqrt(trap(np.where(incell, 2*t1_J1**2*vol, 0.0)))
hn_c = np.sqrt(trap(np.where(incell, 2*phi**2*vol, 0.0)))
ledger['J1_twist_norm_on_cell'] = tn
ledger['J1_twist_harmonic_efficiency_on_cell'] = trap(np.where(incell, sigma*twist_J1_density, 0.0))/(tn*hn_c)
ledger['flux_deficit_delta'] = 1 - FE/(2*PI)
ledger['saving_1_minus_p'] = 1 - P/(8*PI**2)
ledger['saving_over_2delta'] = (1 - P/(8*PI**2))/(2*(1 - FE/(2*PI)))
ledger['tau_J1_positive_part_over_2pi'] = trap(np.maximum(sigma*twist_J1_density, 0))/(2*PI)
ledger['tau_J1_negative_part_over_2pi'] = trap(np.minimum(sigma*twist_J1_density, 0))/(2*PI)

# profile samples
idx = np.unique(np.r_[np.searchsorted(xs, x0*np.geomspace(1.0001, 1e4, 25)), np.searchsorted(xs, [X, 2*X, 10*X])])
idx = idx[idx < len(xs)]
samples = [{'x_over_x0': float(xs[i]/x0), 'a': av[i].tolist(), 'v': v[i].tolist(), 'm': m[i].tolist(),
            'Rplus': Rp[i].tolist(), 'phi': float(phi[i])} for i in idx]

out = {'status': 'floating quadrature on reconstructed A01 cell (not interval certified)',
       'record': str(REC), 'x0': x0, 'X': X, 'checks': checks, 'ledger_theta0_on_cell': ledger,
       'profiles': out_prof, 'samples': samples}
OUT.write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps({k: out[k] for k in ('checks', 'ledger_theta0_on_cell', 'profiles')}, indent=1))
