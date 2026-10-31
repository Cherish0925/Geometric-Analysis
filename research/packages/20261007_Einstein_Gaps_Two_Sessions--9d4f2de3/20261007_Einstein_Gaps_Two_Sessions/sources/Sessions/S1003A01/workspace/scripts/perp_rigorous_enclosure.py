"""Rigorous ball-arithmetic enclosure of J_6/(8 pi^2) and P/(8 pi^2) for a frozen
fixed-slot perpendicular CH cell (Step 10, S1003A01).

Metric (Ric_CH = -6 g normalization, dsigma_1 = 2 sigma_2 ^ sigma_3 cyclic):
    g = dx^2/(4G) + h1 s1^2 + h2 s2^2 + h3 s3^2,   h1 = F, h2 = x, h3 = x e^w,
on x0 <= x <= X, exactly the profile of o11_perp_cell.PerpCell with wpow = 2,
aligned = False, beta0 = 0 (coefficients z interpreted as the exact binary doubles
stored in the record; x0 is the exact rational given by --x0 (default 1/100,
e.g. 3/100 for the authoritative X=128 certificate) and X exact).
Step 33: the output also records the exact dyadic endpoints of the Arb ball and
their outwardly rounded 30-digit decimals (lower rounded down, upper rounded up),
so no binary64 conversion enters the certified endpoint.

Cancellation-free representation.  With y = x - x0 = x0*ell*u*phi(ell*u),
phi(z) = (e^z - 1)/z entire, the profile gives
    F  = y * FH,   FH = e^{qF} + u^2 (10-15u+6u^2)/(ell*phi),
    G  = y * GH,   GH = (1 + (x^2+x0) u^2 (10-15u+6u^2)/(x0*ell*phi)) e^{qG},
    w  = y^2 * WH, WH = (log(1+x) u (10-15u+6u^2) + (1-u)^3 Cw)/(x0*ell*phi)^2,
and every Ricci component is written using only
    D1 = a1''/a1 = 2 (GH/FH) h1'' + h1' (GH' FH - GH FH')/FH^2,
    L1 Lj = (GH/FH) h1' hj'/hj,
    algebraic terms with (e^w-1)^2/h1 = y^3 WH^2 phi(w)^2/FH and
    sinh(w)/h1 = y WH shc(w)/FH,
so no removable singularity at the bolt u = 0 survives.  (' = d/dx, a_i = sqrt(h_i),
dots = d/dt with d/dt = 2 sqrt(G) d/dx.)

Orthonormal Ricci of a diagonal Bianchi-IX metric dt^2 + sum a_i^2 s_i^2:
    R00 = -(D1+D2+D3),
    Rii = -Di - Li (Lj + Lk) + 2 (a_i^4 - (a_j^2 - a_k^2)^2)/(a_i^2 a_j^2 a_k^2).
Density: J/(8 pi^2) = int_0^1 (1/8) x e^{w/2} sqrt(FH/GH) sum_a (R_aa + 6)^2 * ell x du.

The integral is enclosed with Arb's rigorous adaptive Gauss-Legendre integrator
(acb_calc_integrate), which bounds the integrand on complex ellipses; the integrand
is analytic in a neighbourhood of [0,1] after the desingularization above.

Usage: python perp_rigorous_enclosure.py RECORD.json [--prec 128] [--check]
Output: JSON with the enclosing balls, written to --out if given.
"""
import argparse, json, math, time
from fractions import Fraction
from pathlib import Path
from flint import arb, acb, ctx


# ---------- second-order jets in the variable u over acb ----------
class Jet:
    __slots__ = ('v', 'd', 'dd')

    def __init__(self, v, d=0, dd=0):
        self.v, self.d, self.dd = acb(v), acb(d), acb(dd)

    @staticmethod
    def lift(a):
        return a if isinstance(a, Jet) else Jet(a, 0, 0)

    def __add__(self, o):
        o = Jet.lift(o); return Jet(self.v+o.v, self.d+o.d, self.dd+o.dd)
    __radd__ = __add__

    def __sub__(self, o):
        o = Jet.lift(o); return Jet(self.v-o.v, self.d-o.d, self.dd-o.dd)

    def __rsub__(self, o):
        return Jet.lift(o) - self

    def __neg__(self):
        return Jet(-self.v, -self.d, -self.dd)

    def __mul__(self, o):
        o = Jet.lift(o)
        return Jet(self.v*o.v, self.d*o.v + self.v*o.d,
                   self.dd*o.v + 2*self.d*o.d + self.v*o.dd)
    __rmul__ = __mul__

    def __truediv__(self, o):
        o = Jet.lift(o)
        q = self.v/o.v
        qd = (self.d - q*o.d)/o.v
        qdd = (self.dd - 2*qd*o.d - q*o.dd)/o.v
        return Jet(q, qd, qdd)

    def __rtruediv__(self, o):
        return Jet.lift(o)/self

    def exp(self):
        e = self.v.exp(); return Jet(e, e*self.d, e*(self.dd + self.d*self.d))

    def log(self, analytic=False):
        L = self.v.log(analytic=analytic)
        return Jet(L, self.d/self.v, (self.dd*self.v - self.d*self.d)/(self.v*self.v))


def phi_derivs(z, N=48):
    """Enclose phi(z)=(exp(z)-1)/z and its first two derivatives.

    The Taylor remainder radius is computed wholly in Arb.  If an input ball is
    separated from zero we may use the closed quotient formulas.  Otherwise we
    use the entire series, increasing N until the geometric tail estimate has
    ratio strictly below one.  Thus no floating-point radius enters the proof.
    """
    m = abs(z)
    if m.lower() > 1:
        e = z.exp()
        p0 = (e - 1)/z
        p1 = (z*e - e + 1)/(z*z)
        p2 = (z*z*e - 2*z*e + 2*e - 2)/(z*z*z)
        return p0, p1, p2
    r = m.upper()
    while r >= N + 1:
        N *= 2
    s0 = acb(0); s1 = acb(0); s2 = acb(0); zk = acb(1)
    for k in range(N):
        s0 += zk/arb(math.factorial(k+1))
        s1 += zk*(k+1)/arb(math.factorial(k+2))
        s2 += zk*((k+1)*(k+2))/arb(math.factorial(k+3))
        zk = zk*z
    # Every coefficient in all three tails is <= 1/k!, and r/(N+1)<1.
    t = r**N/arb(math.factorial(N))/(1 - r/(N+1))
    err = acb(arb(0, t), arb(0, t))
    return s0+err, s1+err, s2+err


def phi_val(z):
    return phi_derivs(z)[0]


def cheb_jets(n, zj):
    T = [Jet(1), zj]
    for k in range(2, n):
        T.append(2*zj*T[-1] - T[-2])
    return T[:n]


class FrozenCell:
    def __init__(self, rec, x0=None, X=None):
        self.deg = int(rec['deg'])
        z = [arb(float(v)) for v in rec['z']]          # exact binary doubles
        d = self.deg
        self.cF = z[:d]; cG = z[d:2*d]; self.cw = z[2*d:3*d]
        self.x0 = arb(x0) if x0 is not None else arb(1)/100
        self.X = arb(X) if X is not None else arb(float(rec['X']))
        self.ell = (self.X/self.x0).log()
        # bolt shift: qF(0)+qG(0)=0 exactly (T_k(-1)=(-1)^k)
        shift = -sum(((-1)**k)*(self.cF[k] + cG[k]) for k in range(d))
        cG = list(cG); cG[0] = cG[0] + shift
        self.cG = cG

    def ricci(self, u, analytic=False, want_profile=False):
        x0, ell = acb(self.x0), acb(self.ell)
        uj = Jet(u, 1, 0)
        xj = x0*Jet(ell*u, ell, 0).exp()
        p0, p1, p2 = phi_derivs(ell*u)
        phij = Jet(p0, ell*p1, ell*ell*p2)
        yj = x0*ell*uj*phij
        T = cheb_jets(self.deg, 2*uj - 1)
        CF = sum((T[k]*acb(self.cF[k]) for k in range(self.deg)), Jet(0))
        CG = sum((T[k]*acb(self.cG[k]) for k in range(self.deg)), Jet(0))
        CW = sum((T[k]*acb(self.cw[k]) for k in range(self.deg)), Jet(0))
        om = 1 - uj; om3 = om*om*om
        poly = 10 - 15*uj + 6*uj*uj               # S(u) = u^3 * poly
        FH = (om3*CF).exp() + uj*uj*poly/(ell*phij)
        GH = (1 + (xj*xj + x0)*uj*uj*poly/(x0*ell*phij))*(om3*CG).exp()
        L1x = (1 + xj).log(analytic=analytic)
        wj = L1x*uj*uj*uj*poly + uj*uj*om3*CW
        WH = (L1x.v*u*poly.v + om3.v*CW.v)/((x0*ell*p0)**2)

        x = xj.v
        def dx(f):   # u-jet -> (f, f_x, f_xx)
            fx = f.d/(ell*x)
            fxx = (f.dd - ell*f.d)/(ell*ell*x*x)
            return f.v, fx, fxx
        h1j = yj*FH; Gj = yj*GH; h3j = xj*wj.exp()
        h1, h1x, h1xx = dx(h1j)
        FHv, FHx, _ = dx(FH)
        GHv, GHx, _ = dx(GH)
        Gv, Gx, _ = dx(Gj)
        h3, h3x, h3xx = dx(h3j)
        y = yj.v; w = wj.v; ew = w.exp(); WHv = WH
        rho = GHv/FHv
        D1 = 2*rho*h1xx + h1x*(GHx*FHv - GHv*FHx)/(FHv*FHv)
        D2 = Gx/x - Gv/(x*x)
        D3 = Gx*h3x/h3 + 2*Gv*h3xx/h3 - Gv*h3x*h3x/(h3*h3)
        L12 = rho*h1x/x
        L13 = rho*h1x*h3x/h3
        L23 = Gv*h3x/(x*h3)
        E1 = phi_val(w); shc = (E1 + phi_val(-w))/2
        A1 = 2*h1/(x*h3) - 2*y*y*y*WHv*WHv*E1*E1/(FHv*ew)
        A2 = -4*y*WHv*shc/FHv + 4/x - 2*h1/(x*x*ew)
        A3 = 4*y*WHv*shc/FHv + 4/(x*ew) - 2*h1/(x*x*ew)
        R = [-(D1+D2+D3), -D1-L12-L13+A1, -D2-L12-L23+A2, -D3-L13-L23+A3]
        vol = x*(w/2).exp()*(FHv/GHv).sqrt(analytic=analytic)*ell*x/8   # dV/(8 pi^2 du)
        if want_profile:
            return R, vol, dict(x=x, FH=FHv, GH=GHv, w=w, h1=h1, G=Gv, h3=h3)
        return R, vol

    def integrand(self, which):
        def f(u, analytic):
            R, vol = self.ricci(u, analytic)
            if which == 'J':
                return vol*sum((r + 6)**2 for r in R)
            s = sum(R)
            if which == 'P':
                return vol*sum((r - s/4)**2 for r in R)
            if which == 'S':   # (1/4)(s+24)^2
                return vol*(s + 24)**2/4
        return f


def _dyadic(x):
    m, e = x.mid().man_exp()
    return Fraction(int(m)) * (Fraction(2) ** int(e))


def _dec(fr, up, digits=30):
    scale = 10 ** digits
    n = fr * scale
    q = n.numerator // n.denominator
    if up and q * n.denominator != n.numerator:
        q += 1
    s = '-' if q < 0 else ''
    q = abs(q)
    return s + str(q // scale) + '.' + str(q % scale).zfill(digits)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('record')
    ap.add_argument('--prec', type=int, default=128)
    ap.add_argument('--tol', type=float, default=1e-14)
    ap.add_argument('--which', default='J,P')
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--pieces', type=int, default=1, help='rigorously sum this many equal subinterval enclosures')
    ap.add_argument('--out')
    ap.add_argument('--x0', default='1/100', help='exact rational bolt parameter, e.g. 3/100')
    a = ap.parse_args()
    ctx.prec = a.prec
    rec = json.loads(Path(a.record).read_text())
    fr = Fraction(a.x0)
    assert abs(float(fr) - float(rec.get('x0', 0.01))) < 1e-12, 'x0 does not match record'
    cell = FrozenCell(rec)
    cell.x0 = arb(fr.numerator)/fr.denominator
    cell.ell = (cell.X/cell.x0).log()
    out = dict(record=a.record, x0=a.x0, X=rec['X'], deg=cell.deg, prec=a.prec,
               float_record=dict(P=rec.get('P'), J=rec.get('J')))
    if a.check:
        # pointwise: CH collar should give Ric=-6g at u=1; bolt values finite at u=0
        for uu in ['0', '0.000001', '0.3', '0.999999', '1']:
            R, vol = cell.ricci(acb(arb(uu)))
            out.setdefault('pointwise', {})[uu] = [r.real.str(10) for r in R] + [vol.real.str(10)]
    for which in a.which.split(','):
        t0 = time.time(); val = acb(0)
        for k in range(a.pieces):
            lo=arb(k)/a.pieces; hi=arb(k+1)/a.pieces
            val += acb.integral(cell.integrand(which), lo, hi,
                                rel_tol=a.tol, abs_tol=a.tol/a.pieces)
        re = val.real
        out[which] = dict(ball=re.str(30, radius=True), lower=float(re.lower()),
                          upper=float(re.upper()), rad=float(re.rad()), sec=time.time()-t0,
                          imag_rad=float(val.imag.rad()), pieces=a.pieces)
        lo_fr, up_fr = _dyadic(re.lower()), _dyadic(re.upper())
        out[which].update(lower_dec_outward=_dec(lo_fr, False), upper_dec_outward=_dec(up_fr, True),
                          upper_dyadic=[str(up_fr.numerator), str(up_fr.denominator)],
                          lower_dyadic=[str(lo_fr.numerator), str(lo_fr.denominator)])
    if 'J' in out:
        out['certified_J_below_1'] = bool(out['J']['upper'] < 1.0)
        out['eta_certified'] = 1.0 - out['J']['upper']
        upJ = Fraction(int(out['J']['upper_dyadic'][0]), int(out['J']['upper_dyadic'][1]))
        out['certified_J_below_1_exact'] = bool(upJ < 1)
        out['eta_certified_dec_outward_down'] = _dec(1 - upJ, False)
        # balanced coefficient 4 - 8 eta/9, rounded up (a valid upper bound)
        out['balanced_coefficient_dec_outward_up'] = _dec(4 - Fraction(8, 9) * (1 - upJ), True)
    text = json.dumps(out, indent=1); print(text)
    if a.out:
        Path(a.out).write_text(text + '\n')


if __name__ == '__main__':
    main()
