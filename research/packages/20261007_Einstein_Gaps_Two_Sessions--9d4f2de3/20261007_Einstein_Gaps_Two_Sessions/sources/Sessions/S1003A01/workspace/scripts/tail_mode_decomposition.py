"""Decompose the far field of a certified/optimized perpendicular CH cell into the exact
linearized Einstein modes of CH (Ric=-6g), using gauge-invariant quantities.

Cell metric (fixed perpendicular slot): g = dx^2/(4G) + F s1^2 + x s2^2 + x e^w s3^2.
Step-7 axes: (a1,a2,a3) = (sqrt x, sqrt(x e^w), sqrt F); CH: F=x, G=x(1+x), w=log(1+x),
u=(0,3x,0).  Gauge-invariant (vanish on CH, linear-order gauge invariant):
  theta = log(a1/a3),   v_- = u1-u3,   v_+ = u1+u3,
  delta2 = u2 - 3 a1 a3,
  m_est  = (a1 a3)^2 * ( a2^2/(a1 a3) - 1 - a1 a3 ).
Exact linear Einstein modes (scripts/ch_linear_mode_solve.py, calabi_ke_check.py):
  antisymmetric mass mode:  v_- = c f_-(x),  f_-=x/(1+x)^{5/2},
                            theta = -c (6x^2+4x+1)/(24 x^2 (1+x)^2),
  Kahler (Calabi) mass mode: a1=a3=sqrt x, a2^2=G=x+x^2+m/x  (exactly KE for all m; u unchanged).
Output: per-x estimates c_v=v_-/f_-, c_theta=theta/theta_1, m_est, v_+, delta2.
Usage: python tail_mode_decomposition.py RECORD.json [more records] --out OUT.json
"""
import argparse, json, math
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from perp_dual_cost import DualCell, load_record, seed_vector


def slot_fns(rec):
    deg = int(rec['deg']); x0 = float(rec['x0']); X = float(rec['X'])
    c = DualCell(x0, X, deg, deg, 50); c.aligned = False; c.wpow = 2
    z = jnp.asarray(seed_vector(c, rec)); prof = c.prof_factory(z)
    def radii(x):
        G, h = prof(x)
        return jnp.sqrt(jnp.array([h[1, 1], h[2, 2], h[0, 0]])), G   # (a1,a2,a3)
    def state(x):
        a, G = radii(x)
        da = jax.jacfwd(lambda xx: radii(xx)[0])(x) * 2*jnp.sqrt(G)
        a1, a2, a3 = a
        u1 = da[0] - (a2**2 + a3**2 - a1**2)/(a2*a3)
        u2 = da[1] - (a3**2 + a1**2 - a2**2)/(a3*a1)
        u3 = da[2] - (a1**2 + a2**2 - a3**2)/(a1*a2)
        return jnp.array([a1, a2, a3, u1, u2, u3, G])
    return jax.jit(jax.vmap(state)), x0, X


def fminus(x): return x/(1+x)**2.5
def theta1(x): return -(6*x*x + 4*x + 1)/(24*x*x*(1+x)**2)


def analyse(path, nx=400):
    rec = load_record(path)
    st, x0, X = slot_fns(rec)
    xs = np.exp(np.linspace(math.log(max(4*x0, .1)), math.log(X), nx))
    S = np.asarray(st(jnp.asarray(xs)))
    a1, a2, a3, u1, u2, u3, G = S.T
    th = np.log(a1/a3); vm = u1 - u3; vp = u1 + u3
    q = a1*a3
    d2 = u2 - 3*q
    mest = q*q*(a2**2/q - 1 - q)
    rows = []
    for i, x in enumerate(xs):
        rows.append(dict(x=float(x), theta=float(th[i]), vminus=float(vm[i]), vplus=float(vp[i]),
                         c_v=float(vm[i]/fminus(x)), c_theta=float(th[i]/theta1(x)),
                         m_est=float(mest[i]), delta2=float(d2[i])))
    return dict(record=str(path), x0=x0, X=X, J=rec.get('J'), P=rec.get('P'), rows=rows)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('records', nargs='+'); ap.add_argument('--out')
    a = ap.parse_args()
    res = [analyse(p) for p in a.records]
    for r in res:
        print('==', r['record'], 'x0', r['x0'], 'X', r['X'], 'J', r['J'])
        for row in r['rows'][::25]:
            print('x=%9.4f  c_v=%+.5f  c_th=%+.5f  m=%+.3e  v+=%+.3e  d2=%+.3e  th=%+.3e' % (
                row['x'], row['c_v'], row['c_theta'], row['m_est'], row['vplus'], row['delta2'], row['theta']))
    if a.out:
        Path(a.out).write_text(json.dumps(res) + '\n')

if __name__ == '__main__': main()
