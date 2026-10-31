"""Step 29: connect the Step-28 almost-Kahler local action to the exact CH exterior response.

The numerical profile block reconstructs the linear CH variables from a nonlinear tail and evaluates
the exact CH quadratic bridge on them.  Exact nonlinear tail action is evaluated separately by
step29_local_AK_flux.py.

Linear antisymmetric CH variables (Step 19):
  theta = delta log(a1/a3),
  v_-   = delta u1-delta u3 = f(x) w(x),
  f=x/(1+x)^(5/2),  k=(x/(1+x))^2,
  (k theta)' = f^2 w/2.

With slow slots matched, q=theta and the AK Nijenhuis field is
  nu = -sqrt(x) w/[2(1+x)^(5/2)] = -v_-/(2 sqrt(x)).
This script symbolically proves that the quadratic AK Nijenhuis/W3 density
  L_AK = (2 lambda^2-6 nu^2) dVhat/dx
is the raw Ricci density mu (w')^2 plus an exact derivative A(x) w^2.
It then evaluates the boundary-corrected identity on actual LM cell tails and on
the exact outgoing Einstein mass mode (w=constant).

Usage:
  python step29_ak_exterior_bridge.py RECORD [--rho 10] [--n 12000] [--out OUT.json]
"""
import argparse, json, math, sys
from pathlib import Path
import numpy as np
import jax, jax.numpy as jnp
jax.config.update('jax_enable_x64', True)
from scipy.integrate import quad
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from perp_dual_cost import make_cell, load_record, seed_vector
from exterior_null_line import I_inf, finite_cost, k, Gf


def symbolic_bridge():
    x = sp.symbols('x', positive=True)
    w = sp.Function('w')(x)
    f = x/(1+x)**sp.Rational(5, 2)
    # CH hatted metric equals CH.  dT/dx=1/(2 sqrt(x(1+x))), dV/dx=x/2.
    nu = -f*w/(2*sp.sqrt(x))
    beta = (3-2*x)/(2*sp.sqrt(x*(1+x)))
    nu_T = 2*sp.sqrt(x*(1+x))*sp.diff(nu, x)
    lam = sp.simplify(nu_T/2 + beta*nu)
    Lak = sp.factor((2*lam**2 - 6*nu**2)*x/2)
    mu = x**3/(4*(1+x)**4)
    A = -x**2*(3*x-2)/(4*(1+x)**5)
    residual = sp.simplify(Lak - mu*sp.diff(w, x)**2 - sp.diff(A*w**2, x))
    return {
        'nu': str(sp.factor(nu)),
        'lambda': str(sp.factor(lam)),
        'L_AK': str(Lak),
        'mu': str(mu),
        'A': str(A),
        'identity_residual': str(residual),
        'statement': 'L_AK = mu*(dw/dx)^2 + d(A*w^2)/dx'
    }


def numerical_tail(record, rho=10.0, n=12000):
    rec = load_record(record)
    x0, X = float(rec['x0']), float(rec['X'])
    deg = int(rec.get('deg', rec.get('degU', 6)))
    cell = make_cell(x0, deg, 400, smooth_mode=True, X=X)
    z = jnp.asarray(seed_vector(cell, rec)); prof = cell.prof_factory(z)

    def slots(x):
        G, h = prof(x); d = jnp.diag(h)
        # Step-28 order (f,g,h)=(old CH fibre, old transverse, old bolt)
        return G, jnp.sqrt(jnp.array([d[2], d[1], d[0]]))

    def data(x):
        G, A = slots(x)
        Ax = jax.jacfwd(lambda xx: slots(xx)[1])(x)
        At = 2*jnp.sqrt(G)*Ax
        af, ag, ah = A; yf, yg, yh = At/A
        # self-dual spin data in hatted=original approximation are not used: on a
        # sufficiently far CH tail u=1 to numerical precision and the exact bridge
        # can be evaluated through w=v_-/f.
        q = jnp.log(ag/ah)
        qt = yg-yh
        vminus = None
        # torsion relation in exact CH variables: w = 2 (k q)_x / f^2.
        qx = jax.grad(lambda xx: jnp.log(slots(xx)[1][1]/slots(xx)[1][2]))(x)
        kval = (x/(1+x))**2
        kx = 2*x/(1+x)**3
        f2 = x*x/(1+x)**5
        w = 2*(kx*q + kval*qx)/f2
        wx = jax.grad(lambda xx: (
            2*((2*xx/(1+xx)**3)*jnp.log(slots(xx)[1][1]/slots(xx)[1][2])
               +(xx/(1+xx))**2*jax.grad(lambda yy: jnp.log(slots(yy)[1][1]/slots(yy)[1][2]))(xx))
            /(xx*xx/(1+xx)**5)))(x)
        nu = -jnp.sqrt(x)*w/(2*(1+x)**2.5)
        beta = (3-2*x)/(2*jnp.sqrt(x*(1+x)))
        nu_x = jax.grad(lambda xx: -jnp.sqrt(xx)*(
            2*((2*xx/(1+xx)**3)*jnp.log(slots(xx)[1][1]/slots(xx)[1][2])
               +(xx/(1+xx))**2*jax.grad(lambda yy: jnp.log(slots(yy)[1][1]/slots(yy)[1][2]))(xx))
            /(xx*xx/(1+xx)**5))/(2*(1+xx)**2.5))(x)
        lam = jnp.sqrt(x*(1+x))*nu_x + beta*nu
        return q, w, wx, nu, lam

    xs = np.geomspace(rho, X*(1-1e-8), n)
    qv, wv, wpv, nuv, lamv = [np.asarray(a) for a in jax.vmap(data)(jnp.asarray(xs))]
    mu_v = xs**3/(4*(1+xs)**4)
    A_v = -xs**2*(3*xs-2)/(4*(1+xs)**5)
    raw_dens = mu_v*wpv**2
    ak_dens = xs*(2*lamv**2-6*nuv**2)/2
    raw = float(np.trapezoid(raw_dens, xs))
    ak = float(np.trapezoid(ak_dens, xs))
    boundary = float(A_v[-1]*wv[-1]**2 - A_v[0]*wv[0]**2)
    # exact exterior response inferred from entrance trace (infinite CH end)
    w0 = float(wv[0]); Theta = float(qv[0]); m = -2*k(rho)*Theta
    delta = m - w0*Gf(rho); I = I_inf(rho)
    eext = delta*delta/I; lam_ext = -delta/I
    efinite, nu_fin, lam_fin = finite_cost(rho, X, w0, m)
    return {
        'evaluation_scope': 'CH quadratic bridge reconstructed from the nonlinear profile; not the exact nonlinear tail action',
        'record': record, 'rho': rho, 'X': X, 'entrance': {'q': Theta, 'w': w0, 'wp': float(wpv[0]),
                    'nu': float(nuv[0]), 'lambda_AK': float(lamv[0]), 'A': float(A_v[0])},
        'exit': {'q': float(qv[-1]), 'w': float(wv[-1]), 'A': float(A_v[-1])},
        'raw_tail_from_profile': raw,
        'AK_tail_from_profile': ak,
        'boundary_Aw2_exit_minus_entry': boundary,
        'bridge_residual_profile': ak - raw - boundary,
        'exterior_response': {'m': m, 'delta': delta, 'I': I,
                              'lambda_costate': lam_ext, 'E_ext_inf': eext,
                              'E_ext_finite_X': efinite, 'finite_nu': nu_fin,
                              'finite_lambda': lam_fin},
        'AK_tail_predicted_finite_from_response_and_flux': efinite + boundary,
        'AK_tail_predicted_infinite_from_response_and_entry_flux': eext - float(A_v[0])*w0*w0,
        'note': 'Finite-X prediction uses the same entrance trace and exact collar endpoint; infinite prediction assumes A*w^2 -> 0.'
    }


def mass_mode(rho):
    # w=c is the exact decaying Einstein mass mode; normalize c=1.
    A = lambda x: -x*x*(3*x-2)/(4*(1+x)**5)
    # Integral of L_AK=A' for w=1, while raw Ricci action is zero.
    ak = -A(rho)
    return {'rho': rho, 'w': 1.0, 'raw_Ricci_action': 0.0,
            'AK_tail_action': ak, 'entry_interface_Aw2': A(rho),
            'AK_plus_entry_interface': ak + A(rho),
            'interpretation': 'Einstein mass mode has zero raw action; nonzero AK tail is exactly cancelled by interface flux.'}


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('--rho', type=float, default=10.0)
    ap.add_argument('--n', type=int, default=12000); ap.add_argument('--out')
    a = ap.parse_args()
    out = {'symbolic': symbolic_bridge(), 'mass_mode': mass_mode(a.rho),
           'profile': numerical_tail(a.record, a.rho, a.n)}
    txt = json.dumps(out, indent=1); print(txt)
    if a.out: Path(a.out).write_text(txt+'\n')

if __name__ == '__main__':
    main()
