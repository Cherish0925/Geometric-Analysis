"""Step 37: SU(2)-invariant Seiberg--Witten monopole pair on the certified perpendicular cell.

Reduced system (derived and Lichnerowicz-checked in bianchi_sw_reduction.py), restricted to the
invariant subspace n2=alpha2=0 (consistent: the discrete symmetry of a diagonal metric):
  Phi in S^+ real, rho=|Phi|^2, Bloch n=(rho cos th, 0, rho sin th),  v_j=alpha_j/a_j,
  (log rho)' = 2c + v1 cos th + v3 sin th,     th' = v3 cos th - v1 sin th,
  alpha_j'   = a_j n_j - 2 a_j alpha_j/(a_k a_l)   (j=1,3),
  c = (a1^2+a2^2+a3^2)/(2 a1 a2 a3) - (1/2)(log a1 a2 a3)'.
Normalization: D_A Phi=0, c(F_A^+)Phi=rho Phi  =>  rho <= -s/2 (=12 for the Ric=-6 cell),
|f^+|^2=rho^2/2.  Slot 1 = bolt slot (collapses), slot 3 = CH fibre (CH Kaehler form omega_3).
Bolt data: alpha_1(0)=sigma=+-1 = c_1(L)[bolt]; regular solutions have n -> -sigma rho e_1 or rho(0)=0.
CH end: canonical Kaehler solution th=pi/2, rho=12, alpha_1=0, alpha_3=3 sinh^2 r.
Shooting parameters (rho0, beta), th = pi - beta t (sigma=+1); sigma=-1 follows by the exact mirror
(rho,th,alpha1,alpha3)->(rho,pi-th,-alpha1,alpha3), which is checked numerically.

Kinetic density for invariant spinors (q_c = -a_c'/a_c + (a_k^2+a_l^2-a_c^2)/(a1a2a3)):
  |nabla Phi|^2 = (c^2+|v|^2/4) rho + c v.n + sum_c [ (q_c^2+v_c^2) rho/4 + q_c v_c n_c/2 ],
  |zeta|^2 = rho'^2/4 + (1/4) sum_c (q_c n_c + v_c rho)^2,  rotation part = |nabla Phi|^2-|zeta|^2/rho.
Output: workspace/data/sw_perp_cell_pair.json
"""
import json, sys, math
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.integrate import solve_ivp
from scipy.optimize import least_squares

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT / 'Sessions' / 'S1003A01' / 'workspace' / 'scripts'))
sys.path.insert(0, str(ROOT / 'Sessions' / 'S1003A02' / 'workspace' / 'scripts'))
from perp_dual_cost import make_cell, load_record, seed_vector  # noqa

REC = ROOT / 'Sessions/S1003A01/workspace/data/perp_area/x00.03_X128_d20.json'
rec = load_record(REC)
x0 = float(rec['x0']); X = float(rec['X']); deg = int(rec.get('deg', 20))
cell = make_cell(x0, deg, 400, smooth_mode=True, X=X)
z = jnp.asarray(seed_vector(cell, rec)); prof = cell.prof_factory(z)

def slots_cell(x):
    G, h = prof(x); d = jnp.diag(h)
    return G, jnp.sqrt(d)
def slots_ch(x):
    return x*(1+x), jnp.sqrt(jnp.array([x, x, x*(1+x)]))
def geom_factory(fn):
    def geom(x):
        G, A = fn(x)
        Ax = jax.jacfwd(lambda xx: fn(xx)[1])(x)
        return G, A, 2*jnp.sqrt(G)*Ax      # a_i and da_i/dt
    return jax.jit(geom)
gcell = geom_factory(slots_cell); gch = geom_factory(slots_ch)
def geom(x):
    G, A, Ad = (gcell if x <= X else gch)(x)
    return float(G), np.asarray(A), np.asarray(Ad)

def rhs(x, y):
    lr, th, al1, al3 = y
    G, a, ad = geom(x)
    W = a.prod(); c = (a@a)/(2*W) - 0.5*(ad/a).sum()
    v1, v3 = al1/a[0], al3/a[2]; rho = math.exp(lr)
    dl = 2*c + v1*math.cos(th) + v3*math.sin(th)
    dth = v3*math.cos(th) - v1*math.sin(th)
    d1 = a[0]*rho*math.cos(th) - 2*a[0]*al1/(a[1]*a[2])
    d3 = a[2]*rho*math.sin(th) - 2*a[2]*al3/(a[0]*a[1])
    dtdx = 1/(2*math.sqrt(G))
    return [dl*dtdx, dth*dtdx, d1*dtdx, d3*dtdx]

Gp = float(jax.grad(lambda x: slots_cell(x)[0])(x0 + 1e-12))
dx0 = 1e-9
t0 = math.sqrt(dx0/Gp)
b0 = math.sqrt(x0)
XFAR = math.sinh(6.5)**2

def shoot(params, sigma=1, dense=False):
    rho0, beta = params
    th0 = (math.pi - beta*t0) if sigma == 1 else (beta*t0)
    al1 = sigma*(1 - (rho0/2 + 1/x0)*t0**2)
    al3 = b0*rho0*(beta if sigma == 1 else beta)*t0**2/4
    y0 = [math.log(rho0), th0, al1, al3]
    sol = solve_ivp(rhs, (x0 + dx0, XFAR), y0, method='LSODA', rtol=1e-10, atol=1e-12,
                    dense_output=dense)
    return sol

def resid(params, sigma=1):
    sol = shoot(params, sigma)
    if not sol.success: return [1e3, 1e3]
    lr, th = sol.y[0, -1], sol.y[1, -1]
    return [lr - math.log(12.0), th - math.pi/2]

out = {'record': str(REC.relative_to(ROOT)), 'x0': x0, 'X': X, 't0': t0}
best = None
for g in [(12.0, 0.0), (10.0, 1.0), (8.0, 2.0), (12.0, -1.0), (6.0, 3.0)]:
    try:
        r = least_squares(resid, g, args=(1,), xtol=1e-14, ftol=1e-14, max_nfev=200)
        if best is None or r.cost < best.cost: best = r
        print('guess', g, '->', r.x, r.cost, flush=True)
    except Exception as e:
        print('fail', g, e)
out['sigma+'] = dict(rho0=best.x[0], beta=best.x[1], cost=best.cost)
# mirror check: sigma=-1 with th -> pi - th: th0 = beta t0
rm = least_squares(resid, best.x, args=(-1,), xtol=1e-14, ftol=1e-14, max_nfev=200)
out['sigma-'] = dict(rho0=rm.x[0], beta=rm.x[1], cost=rm.cost)

# diagnostics on the sigma=+1 solution
sol = shoot(best.x, 1, dense=True)
xs = np.concatenate([x0 + dx0 + np.geomspace(1e-9, 1e-3, 2000), np.geomspace(x0*1.04, XFAR, 20000)])
xs = xs[(xs > x0 + dx0) & (xs < XFAR)]; xs.sort()
Y = sol.sol(xs)
rows = []
for x, (lr, th, al1, al3) in zip(xs, Y.T):
    G, a, ad = geom(x)
    W = a.prod(); rho = math.exp(lr)
    v = np.array([al1/a[0], 0.0, al3/a[2]])
    n = np.array([rho*math.cos(th), 0.0, rho*math.sin(th)])
    c = (a@a)/(2*W) - 0.5*(ad/a).sum()
    q = np.array([-ad[i]/a[i] + (a[(i+1) % 3]**2 + a[(i+2) % 3]**2 - a[i]**2)/W for i in range(3)])
    kin = (c*c + v@v/4)*rho + c*(v@n) + np.sum((q*q + v*v)*rho/4 + q*v*n/2)
    dlr = 2*c + v@n/rho
    zeta2 = (rho*dlr)**2/4 + 0.25*np.sum((q*n + v*rho)**2)
    rot = kin - zeta2/rho
    rows.append([x, math.asinh(math.sqrt(min(x, 1e300))), W, 2*math.sqrt(G), rho, th, kin, zeta2, rot])
R = np.array(rows)
x_, W_, dxdt = R[:, 0], R[:, 2], R[:, 3]
dt = np.gradient(x_)/dxdt
def integ(f): return float(np.sum(f*W_*dt)/4)       # (1/8pi^2) * 2pi^2 int W f dt
rho = R[:, 4]
out['diag'] = dict(
    rho_bolt=float(rho[0]), th_bolt=float(R[0, 5]), rho_min=float(rho.min()), x_rho_min=float(x_[rho.argmin()]),
    K_over_8pi2=integ(R[:, 6]), weitz_K_over_8pi2=integ(rho*(12-rho)/2),
    zeta_over_rho_over_8pi2=integ(R[:, 7]/rho), rotation_over_8pi2=integ(R[:, 8]),
    deficit_int_over_8pi2=integ(6*(12-rho)),   # int (2-rho_hat) dvol_hat /8pi2, rho_hat=rho/6, dvol_hat=36 dvol
    amp_bound_4deficit=4*integ(6*(12-rho)),
    n1_sq_over_8pi2=integ((rho*np.cos(R[:, 5]))**2/2),
)
prof_out = R[::200].tolist()
out['profile_cols'] = ['x', 'r_CH', 'W', 'dxdt', 'rho', 'theta', 'kin', 'zeta2', 'rot']
out['profile'] = prof_out
path = ROOT / 'Sessions/S1003A02/workspace/data/sw_perp_cell_pair.json'
path.write_text(json.dumps(out, indent=1) + '\n')
print(json.dumps({k: v for k, v in out.items() if k != 'profile'}, indent=1))
