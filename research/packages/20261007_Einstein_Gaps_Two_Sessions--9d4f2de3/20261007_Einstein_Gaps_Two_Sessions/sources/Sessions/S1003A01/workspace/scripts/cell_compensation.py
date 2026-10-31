"""Compensation diagnostics and constrained searches for the conformal triaxial cell.

This script works in the normalization of I54/I55:
  j = J/(2*pi^2), mu=r0^2, F_CH=1+r^2/6, Ric_CH=-g_CH.
It evaluates both exact decompositions

  j = M^2/(4 I_R) + R_X + R_Y + R_Z + R_V                      (I55 8.2)

and

  j-K = A0/(24*pi^2) + 2 B0/pi^2 + L/(8*pi^2)
        - N(2 m0-3N)/(8*pi^2 v_K),

where K=(2+mu)^2 R^4/(R^4-mu^2) is the conformally Kahler lower
bound.  The second identity is reported in normalized variables
m=m0/(2*pi^2), n=N/(2*pi^2), v=v_K/(2*pi^2).

The constrained mode minimizes j while approximately fixing n/m.  Its purpose
is not to prove C1, but to reveal which actual remainder pays the formal
nonintegrability gain in the only nontrivial range 0<n/m<2/3.
"""
import argparse, json, math, os, sys
import torch

sys.path.insert(0, os.path.dirname(__file__))
from cell_opt import Cell

torch.set_default_dtype(torch.float64)


def integral(cell, f):
    return torch.sum(cell.wx * cell.jac * f)


def diagnostics_tensor(cell, cF, cw, cp):
    (F, Fr, Frr), (w, wr, wrr), (p, pr, prr) = cell.fields(cF, cw, cp)
    r = cell.r
    e2p = torch.exp(2*p)

    EV = 1 - Frr/2 - 5*Fr/(2*r)
    EH = 1 - Fr/r + 4*(1-F)/r**2
    c = 4*(torch.cosh(2*w)-1)/r**2
    z = 8*torch.sinh(2*w)**2/(r**2*F)
    U = (-F*wrr - (Fr+3*F/r)*wr
         + 4*torch.sinh(4*w)/(r**2*F) - 4*torch.sinh(2*w)/r**2)
    D0 = EV + e2p - 1 - 3*F*prr - (2*Fr+3*F/r)*pr
    D3 = EV + e2p - 1 - F*prr - (2*Fr+5*F/r)*pr - 2*F*pr**2
    DH = EH + e2p - 1 - F*prr - (Fr+5*F/r)*pr - 2*F*pr**2

    a0 = D0 - 2*F*wr**2
    a3 = D3 - z
    ah = DH + c
    vw = U - 2*F*pr*wr
    X = 2*ah-a0-a3
    Y = a0+a3+2*ah
    Z = a0-a3

    j_direct = integral(cell, r**3*(a0**2+a3**2+2*ah**2+2*vw**2))
    IR = (cell.mu**-2-cell.Rc**-4)/4
    Pw = integral(cell, 2*F*wr**2/r + 8*(torch.cosh(2*w)-1)/r**3
                  + 8*torch.sinh(2*w)**2/(r**3*F))
    Tphi = integral(cell, 2*F*pr**2/r)
    q = Tphi-Pw
    M0 = 1+2/cell.mu
    M = M0-q
    rx = integral(cell, r**3*(X-M/(IR*r**4))**2)/4
    ry = integral(cell, r**3*Y**2)/4
    rz = integral(cell, r**3*Z**2)/2
    rv = integral(cell, 2*r**3*vw**2)
    proj = M**2/(4*IR)
    j_radial = proj+rx+ry+rz+rv

    # Almost-Kahler nonintegrability: n=N/(2*pi^2).
    n = integral(cell, 2*r**3*F*(wr+2*torch.sinh(2*w)/(r*F))**2)
    m = cell.Rc**4+2*cell.mu
    v = (cell.Rc**4-cell.mu**2)/4
    K = M0**2/(4*IR)
    gain_n = n*(2*m-3*n)/(4*v)
    gain_q = q*(2*M0-q)/(4*IR)

    # A0/(2*pi^2) from its defining scalar remainder.  Since
    # Y=e^(2p)(s_G+4), e^(2p)s_G=Y-4e^(2p).
    S_norm = integral(cell, r**3*(Y-4*e2p)**2)
    A0_norm = S_norm-(m+n)**2/v
    # Infer B0/(2*pi^2) from the exact I54 identity; this avoids a separate
    # curvature-operator implementation and is an independent consistency test.
    base = -cell.Rc**4 + m**2/(6*v) + 3*(n-m/3)**2/(4*v)
    B0_norm = (j_direct-4-base-A0_norm/12-ry)/4
    positive_i54 = A0_norm/12+4*B0_norm+ry

    return {
        'j': j_direct, 'j_radial': j_radial, 'K': torch.as_tensor(K),
        'deficit': j_direct-K,
        'mu': torch.as_tensor(cell.mu), 'Rc': torch.as_tensor(cell.Rc),
        'm': torch.as_tensor(m), 'v': torch.as_tensor(v), 'n': n,
        'nfrac': n/m, 'q': q, 'M': M, 'M0': torch.as_tensor(M0),
        'Pw': Pw, 'Tphi': Tphi,
        'proj': proj, 'rx': rx, 'ry': ry, 'rz': rz, 'rv': rv,
        'gain_q': gain_q, 'gain_n': gain_n,
        'S_norm': S_norm, 'A0_norm': A0_norm, 'B0_norm': B0_norm,
        'A_pay': A0_norm/12, 'B_pay': 4*B0_norm, 'scalar_pay': ry,
        'positive_i54': positive_i54,
        'radial_identity_error': j_direct-j_radial,
        'i54_identity_error': (j_direct-K)-(positive_i54-gain_n),
        'F_min_scaled': torch.min(F/(cell.x+1e-300)),
        'w_max': torch.max(torch.abs(w)), 'phi_max': torch.max(torch.abs(p)),
    }


def floats(d):
    return {k: float(v.detach().cpu()) if torch.is_tensor(v) else v for k,v in d.items()}


def scale_w_to_target(cell, cF, direction, cp, target_n, max_scale=4.0):
    """Scale a fixed coefficient direction until n approximately hits target."""
    with torch.no_grad():
        lo, hi = 0.0, 1e-4
        def nv(a):
            return float(diagnostics_tensor(cell, cF, a*direction, cp)['n'])
        while nv(hi) < target_n and hi < max_scale:
            hi *= 2
        if hi >= max_scale and nv(hi) < target_n:
            return hi*direction
        for _ in range(60):
            mid=(lo+hi)/2
            if nv(mid) < target_n: lo=mid
            else: hi=mid
        return ((lo+hi)/2)*direction


def constrained_run(mu, Rc, deg, nfrac_target, seed=0, nq=700,
                    outer=8, inner=1200, rho=2000.0, init=None,
                    preopt_iters=2500):
    cell=Cell(mu,Rc,deg,nq=nq,coord='log')
    torch.manual_seed(seed)
    ncoef=deg+1
    if init is None:
        # First optimize the unconstrained biaxial (F,phi) sector.  This supplies
        # the inexpensive background on which nonintegrability should be tested;
        # starting from F=F_CH forces the optimizer through an unnecessarily
        # high-cost topology-changing profile and obscures compensation.
        cF=torch.zeros(ncoef,requires_grad=True)
        cp=torch.zeros(ncoef,requires_grad=True)
        cw0=torch.zeros(ncoef)
        pre=torch.optim.LBFGS([cF,cp],lr=1,max_iter=preopt_iters,history_size=60,
                              tolerance_grad=1e-11,tolerance_change=1e-14,
                              line_search_fn='strong_wolfe')
        def preclosure():
            pre.zero_grad()
            d=diagnostics_tensor(cell,cF,cw0,cp)
            positivity=torch.relu(1e-3-d['F_min_scaled'])**2*1e6
            loss=d['j']+positivity
            loss.backward()
            return loss
        pre.step(preclosure)
        cF=cF.detach(); cp=cp.detach()
        # Low Chebyshev modes are the least oscillatory ways to create N; using
        # them as independent starts is substantially more informative than a
        # random high-frequency direction.  Later seeds use reproducible random
        # directions to retain a broad search.
        if seed < min(4, ncoef):
            direction=torch.zeros(ncoef)
            direction[seed]=1.0
        else:
            direction=torch.randn(ncoef)
            direction=direction/torch.linalg.norm(direction)
        target=nfrac_target*(Rc**4+2*mu)
        cw=scale_w_to_target(cell,cF,direction,cp,target)
    else:
        cF=torch.tensor(init['cF'])
        cw=torch.tensor(init['cw'])
        cp=torch.tensor(init['cp'])
    cF.requires_grad_(True); cw.requires_grad_(True); cp.requires_grad_(True)
    target=torch.as_tensor(nfrac_target*(Rc**4+2*mu))
    lam=torch.tensor(0.0)
    history=[]
    for oi in range(outer):
        opt=torch.optim.LBFGS([cF,cw,cp],lr=0.7,max_iter=inner,history_size=60,
                              tolerance_grad=1e-11,tolerance_change=1e-14,
                              line_search_fn='strong_wolfe')
        def closure():
            opt.zero_grad()
            d=diagnostics_tensor(cell,cF,cw,cp)
            con=d['n']-target
            positivity=torch.relu(1e-3-d['F_min_scaled'])**2*1e6
            # Target only the magnitude of almost-Kahler nonintegrability.  A
            # minimizer at fixed n may choose either sign of w; constraining the
            # signed/weighted radial moment q would test a different question.
            loss=d['j']+lam*con+rho*con**2/2+positivity
            loss.backward()
            return loss
        opt.step(closure)
        d=diagnostics_tensor(cell,cF,cw,cp)
        con=(d['n']-target).detach()
        lam=(lam+rho*con).detach()
        history.append(dict(outer=oi,constraint=float(con),j=float(d['j']),
                            deficit=float(d['deficit']),nfrac=float(d['nfrac'])))
        if abs(float(con)) < 2e-6:
            break
    d=floats(diagnostics_tensor(cell,cF,cw,cp))
    d.update(nfrac_target=nfrac_target,seed=seed,deg=deg,history=history,
             cF=cF.detach().tolist(),cw=cw.detach().tolist(),cp=cp.detach().tolist())
    return d


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--mu',type=float,default=0.1)
    ap.add_argument('--Rc',type=float,default=2.0)
    ap.add_argument('--deg',type=int,default=16)
    ap.add_argument('--nq',type=int,default=700)
    ap.add_argument('--nfrac',type=float,nargs='+',default=[0.05,0.15,1/3,0.5,0.63])
    ap.add_argument('--seeds',type=int,default=2)
    ap.add_argument('--outer',type=int,default=8)
    ap.add_argument('--inner',type=int,default=1200)
    ap.add_argument('--rho',type=float,default=2000.0)
    ap.add_argument('--preopt-iters',type=int,default=2500)
    ap.add_argument('--out',required=True)
    a=ap.parse_args()
    os.makedirs(os.path.dirname(a.out),exist_ok=True)
    with open(a.out,'w') as fh:
        for nf in a.nfrac:
            for seed in range(a.seeds):
                res=constrained_run(a.mu,a.Rc,a.deg,nf,seed,a.nq,a.outer,a.inner,
                                    a.rho,preopt_iters=a.preopt_iters)
                fh.write(json.dumps(res)+'\n'); fh.flush()
                keys=['nfrac_target','seed','j','K','deficit','nfrac','q','gain_n',
                      'A_pay','B_pay','scalar_pay','rx','ry','rz','rv',
                      'radial_identity_error','i54_identity_error']
                print(json.dumps({k:res[k] for k in keys}),flush=True)


if __name__=='__main__':
    main()
