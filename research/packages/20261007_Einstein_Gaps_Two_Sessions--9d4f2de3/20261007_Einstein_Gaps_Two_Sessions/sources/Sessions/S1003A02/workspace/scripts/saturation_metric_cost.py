"""Independent cost evaluation of a collocated saturation trajectory as an actual metric.

The forward scale-free dynamics is exponentially unstable in the collapsed neck, so
re-shooting is not a meaningful test.  Instead we build an actual C^1 metric
    g = dt^2 + sum_i exp(2 L_i) sigma_i^2
from the node data alone: cubic Hermite interpolants in tau for x, z (node slopes chi and
-eta z/3 from the state) and for p (node slope from the dynamics at the node controls),
h = int p dtau (exact), t = int e^h dtau.  Then
    y_i = dL_i/dt,  y_i' = d^2L_i/dt^2   (analytic from the interpolants),
the Ricci tensor is computed from the classical diagonal Bianchi-IX formulas
    Ric00 = -sum (y_i'+y_i^2),   Ric_ii = -y_i' - y_i sum y_j + Pot_i(L),
and hatP = int W |Ric0|^2/4 dt.  This never uses the control/potential formulas
(VD,Vx,VH) except for the node value of dp/dtau.  The terminal node is an exact CH
first jet, so the metric continues by the exact homothetic CH collar.
Usage: python saturation_metric_cost.py file.json [...]
"""
import json, math, sys
from pathlib import Path
import numpy as np
from numpy.polynomial.legendre import leggauss


def pots_state(x, z):
    em4 = np.exp(-4*x/3); ep2 = np.exp(2*x/3); ep8 = np.exp(8*x/3)
    VD = 4*z**-4*(em4-ep2)+4*(ep2*z*z-em4*z**8)
    Vx = 4*z**-4*(ep8-em4)+4*z*z*(em4-ep2)
    VH = (2/3)*z**-4*(ep8-2*ep2+em4)-(4/3)*z*z*(ep2+em4)+(2/3)*em4*z**8
    return VD, Vx, VH


def herm(y0, y1, d0, d1, hh, s):
    """cubic Hermite on [0,hh] at local s; returns value, first, second derivative."""
    u = s/hh
    h00 = 2*u**3-3*u**2+1; h10 = u**3-2*u**2+u; h01 = -2*u**3+3*u**2; h11 = u**3-u**2
    a00 = (6*u**2-6*u)/hh; a10 = 3*u**2-4*u+1; a01 = (-6*u**2+6*u)/hh; a11 = 3*u**2-2*u
    b00 = (12*u-6)/hh**2; b10 = (6*u-4)/hh; b01 = (-12*u+6)/hh**2; b11 = (6*u-2)/hh
    v = h00*y0+h10*hh*d0+h01*y1+h11*hh*d1
    dv = a00*y0+a10*d0+a01*y1+a11*d1
    ddv = b00*y0+b10*d0+b01*y1+b11*d1
    return v, dv, ddv


def herm_int(y0, y1, d0, d1, hh, s):
    """integral from 0 to s of the cubic Hermite interpolant."""
    u = s/hh
    I00 = hh*(u**4/2-u**3+u); I10 = hh*hh*(u**4/4-2*u**3/3+u**2/2)
    I01 = hh*(-u**4/2+u**3); I11 = hh*hh*(u**4/4-u**3/3)
    return I00*y0+I10*d0+I01*y1+I11*d1


def evaluate(path, ng=24):
    rec = json.loads(Path(path).read_text())
    X = np.array(rec['X'], float); U = np.array(rec['U'], float); T = float(rec['T'])
    N = X.shape[0]-1; hh = T/N
    x, z, p, chi, eta = X.T
    xi = chi+eta/2
    VD, Vx, VH = pots_state(x, z)
    pdot = p*p-xi*xi/3-eta*eta/4+VH/2-U[:, 0]/2
    xdot = chi; zdot = -eta*z/3
    gx, gw = leggauss(ng)
    hcur = 0.0; tcur = 0.0; cost = 0.0; smin, smax = np.inf, -np.inf
    for k in range(N):
        s = (gx+1)*hh/2; w = gw*hh/2
        xv, xd, xdd = herm(x[k], x[k+1], xdot[k], xdot[k+1], hh, s)
        zv, zd, zdd = herm(z[k], z[k+1], zdot[k], zdot[k+1], hh, s)
        pv, pd, _ = herm(p[k], p[k+1], pdot[k], pdot[k+1], hh, s)
        hv = hcur+herm_int(p[k], p[k+1], pdot[k], pdot[k+1], hh, s)
        q = -3*np.log(zv); qd = -3*zd/zv; qdd = -3*(zdd/zv-(zd/zv)**2)
        be = xv+q/2; bed = xd+qd/2; bedd = xdd+qdd/2
        Ls = [hv+2*be/3, hv-be/3+q/2, hv-be/3-q/2]
        Ld = [pv+2*bed/3, pv-bed/3+qd/2, pv-bed/3-qd/2]
        Ldd = [pd+2*bedd/3, pd-bedd/3+qdd/2, pd-bedd/3-qdd/2]
        r = np.exp(hv)
        y = np.array([Ld[i]/r for i in range(3)])
        yp = np.array([(Ldd[i]-Ld[i]*pv)/r**2 for i in range(3)])
        L = np.array(Ls)
        Pot = []
        for i in range(3):
            j, kk = (i+1) % 3, (i+2) % 3
            Pot.append(2*np.exp(2*L[i]-2*L[j]-2*L[kk])-8*np.exp(-2*L[i])*np.sinh(L[j]-L[kk])**2)
        Pot = np.array(Pot)
        R0 = -np.sum(yp+y*y, axis=0); Ri = -yp-y*np.sum(y, axis=0)+Pot
        sc = R0+Ri.sum(0)
        ric0 = (R0-sc/4)**2+np.sum((Ri-sc/4)**2, axis=0)
        Wv = np.exp(L.sum(0))
        cost += float(np.sum(w*Wv*ric0/4*r))          # dt = r dtau
        smin = min(smin, float(np.min(sc*r*r))); smax = max(smax, float(np.max(sc*r*r)))
        hcur = float(hcur+herm_int(p[k], p[k+1], pdot[k], pdot[k+1], hh, hh))
    return {'path': str(path), 'eps': rec['eps'], 'N': N, 'collocation_cost': rec['cost'],
            'metric_cost': cost, 'relative_difference': (cost-rec['cost'])/rec['cost'],
            'scale_free_scalar_range': [smin, smax], 't_ch': rec['t_ch']}


if __name__ == '__main__':
    print(json.dumps([evaluate(p) for p in sys.argv[1:]], indent=1))
