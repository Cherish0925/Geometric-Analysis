#!/usr/bin/env python3
"""Step 73: derive a rigorous self-dual Weyl saving from the certified CH cell.

The frozen cell is exactly CH on its outer collar and replaces a CH ball by a
one-blow-up cell.  In the Ric=-6g normalization let

  p = P_cell/(8 pi^2),
  q = (J_6-P)/(8 pi^2) = (1/(32 pi^2)) int (s+24)^2.

For the relative cell, Chern--Gauss--Bonnet plus signature gives

  P/(8 pi^2) = 1 + 4 Delta W_+/(8 pi^2) + Delta S/(96 pi^2),
  Delta S/(96 pi^2) = 2 Delta V/(pi^2) - 4 Delta T/(pi^2) + (2/3) q,

where Delta V and Delta T are respectively the changes in volume and total
scalar integral relative to the removed CH ball.  The latter two are enclosed
by the same Arb analytic quadrature used for P and q.  This script imports the
verified desingularized FrozenCell evaluator and adds V and total-scalar
relative integrands.  All input coefficients are frozen exact binary dyadics.
"""
import argparse, json, sys, time
from fractions import Fraction
from pathlib import Path
from flint import arb, acb, ctx

ROOT = Path(__file__).resolve().parents[4]
A01S = ROOT/'Sessions'/'S1003A01'/'workspace'/'scripts'
sys.path.insert(0, str(A01S))
from perp_rigorous_enclosure import FrozenCell, _dyadic, _dec  # noqa: E402


def integrate(cell, fun, tol, pieces):
    val = acb(0)
    for k in range(pieces):
        lo, hi = arb(k)/pieces, arb(k+1)/pieces
        val += acb.integral(fun, lo, hi, rel_tol=tol, abs_tol=tol/pieces)
    return val.real


def enc(re):
    lo_fr, up_fr = _dyadic(re.lower()), _dyadic(re.upper())
    return dict(ball=re.str(30, radius=True),
                lower_dec_outward=_dec(lo_fr, False),
                upper_dec_outward=_dec(up_fr, True),
                lower_dyadic=[str(lo_fr.numerator),str(lo_fr.denominator)],
                upper_dyadic=[str(up_fr.numerator),str(up_fr.denominator)])


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--record',default='Sessions/S1003A01/workspace/data/perp_area/x00.03_X128_d20.json')
    ap.add_argument('--P',default='Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_P_exact.json')
    ap.add_argument('--Q',default='Sessions/S1003A01/workspace/data/step33/rigorous_x00.03_X128_d20_S_exact.json')
    ap.add_argument('--out',default='Sessions/S1003A02/workspace/data/step73_certified_weyl_saving.json')
    ap.add_argument('--prec',type=int,default=192)
    ap.add_argument('--tol',type=float,default=1e-16)
    ap.add_argument('--pieces',type=int,default=2)
    a=ap.parse_args(); ctx.prec=a.prec
    rec=json.load(open(ROOT/a.record)); cell=FrozenCell(rec)
    cell.x0=arb(3)/100; cell.ell=(cell.X/cell.x0).log()

    # FrozenCell vol is dV/(8 pi^2 du). CH has s=-24 and the same x-gauge
    # volume density x*ell*x/8 because F=x, G=x+x^2, w=0.
    def dV(u, analytic):
        R, vol, pr = cell.ricci(u, analytic, want_profile=True)
        vol_ch = pr['x']*cell.ell*pr['x']/8
        return vol-vol_ch
    def dT(u, analytic):
        R, vol, pr = cell.ricci(u, analytic, want_profile=True)
        vol_ch = pr['x']*cell.ell*pr['x']/8
        return sum(R)*vol + 24*vol_ch

    t=time.time(); dv8=integrate(cell,dV,a.tol,a.pieces); dt8=integrate(cell,dT,a.tol,a.pieces)
    Pj=json.load(open(ROOT/a.P))['P']; Qj=json.load(open(ROOT/a.Q))['S']
    def json_interval(obj):
        # Reconstruct the exact dyadic hull rather than reparsing the shortened
        # human-readable ball string.
        ln,ld=map(int,obj['lower_dyadic']); un,ud=map(int,obj['upper_dyadic'])
        lo=arb(ln)/ld; hi=arb(un)/ud
        return arb.union(lo,hi)
    p=json_interval(Pj); q=json_interval(Qj)
    # dimensionless v=Delta V/(8pi2), t=Delta int s/(8pi2).
    # Delta S/(96pi2) = (2/3)*(Delta S/(64pi2));
    # Delta S/(32pi2)= q + 12 t + 144 v from expanding (s+24)^2.
    # Therefore Delta S/(96pi2)=(q+12t+144v)/3.
    ds96=(q + 12*dt8 + 144*dv8)/3
    # delta = (W_CH^+ - W_cell^+)/(4 pi^2), positive saving unit.
    # p = 1 + 2*(Delta W_+/(4pi2)) + ds96, hence delta=(1+ds96-p)/2.
    delta=(1+ds96-p)/2
    loss=1-delta                       # deficit loss in units 4pi2 per blow-up
    hcrit=1/(3*loss)
    # Equivalently k/A < hcrit guarantees positive total Weyl deficit.
    out=dict(record=a.record,prec=a.prec,tol=a.tol,pieces=a.pieces,seconds=time.time()-t,
             definitions=dict(p='P/(8pi^2)',q='int(s+24)^2/(32pi^2)',
                              dv8='Delta Vol/(8pi^2)',dt8='Delta int(s)/(8pi^2)',
                              ds96='Delta int(s^2)/(96pi^2)',
                              delta='(int_CH|W+|^2-int_cell|W+|^2)/(4pi^2)',
                              loss='1-delta',hcrit='1/(3 loss)'),
             p=enc(p),q=enc(q),dv8=enc(dv8),dt8=enc(dt8),ds96=enc(ds96),
             delta=enc(delta),loss=enc(loss),hcrit=enc(hcrit),
             theorem_safe=dict(delta_lower=enc(delta)['lower_dec_outward'],
                               loss_upper=enc(loss)['upper_dec_outward'],
                               hcrit_lower=enc(hcrit)['lower_dec_outward']))
    Path(ROOT/a.out).parent.mkdir(parents=True,exist_ok=True)
    Path(ROOT/a.out).write_text(json.dumps(out,indent=1)+'\n')
    print(json.dumps(out,indent=1))

if __name__=='__main__': main()
