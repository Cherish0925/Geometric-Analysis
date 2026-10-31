"""Diagnose loss of analyticity in the corrected long-cell Arb integrand.

Each requested real-u interval is evaluated as one complex box (midpoint plus equal
real/imaginary radius).  This is not an integration certificate; it identifies which
profile denominator or square-root argument first crosses zero under complex
enlargement, so a rigorous partition can be adapted in physical radius.
"""
import argparse,json,math
from fractions import Fraction
from pathlib import Path
from flint import arb,acb,ctx
from perp_rigorous_enclosure import FrozenCell


def safe_float(x,which):
    try: return float(getattr(x,which)())
    except Exception: return None


def main():
    ap=argparse.ArgumentParser(); ap.add_argument('record'); ap.add_argument('--x0',default='19/500')
    ap.add_argument('--pieces',type=int,default=64); ap.add_argument('--prec',type=int,default=128); ap.add_argument('--out')
    a=ap.parse_args();ctx.prec=a.prec;rec=json.loads(Path(a.record).read_text());fr=Fraction(a.x0)
    c=FrozenCell(rec);c.x0=arb(fr.numerator)/fr.denominator;c.ell=(c.X/c.x0).log()
    rows=[]
    for k in range(a.pieces):
        lo=k/a.pieces;hi=(k+1)/a.pieces;mid=(lo+hi)/2;rad=(hi-lo)/2
        u=acb(arb(mid,rad),arb(0,rad))
        row={'k':k,'ulo':lo,'uhi':hi}
        try:
            R,vol,p=c.ricci(u,analytic=True,want_profile=True)
            for name in ['FH','GH','h1','G','h3']:
                q=p[name].real;row[name+'_lower']=safe_float(q,'lower');row[name+'_upper']=safe_float(q,'upper')
            row['vol_finite']=bool(vol.is_finite());row['ric_finite']=all(bool(r.is_finite()) for r in R)
            row['imag_rad_max']=max([float(vol.imag.rad())]+[float(r.imag.rad()) for r in R])
        except Exception as e:
            row['error']=repr(e)
        rows.append(row)
    bad=[r for r in rows if ('error'in r or not r.get('vol_finite',False) or not r.get('ric_finite',False)
                              or any(r.get(n+'_lower') is None or r.get(n+'_lower')<=0 for n in ['FH','GH','h1','G','h3']))]
    out={'record':a.record,'x0':a.x0,'pieces':a.pieces,'prec':a.prec,'bad_count':len(bad),'bad':bad,'rows':rows}
    text=json.dumps(out,indent=1);print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=1))
    if a.out:Path(a.out).write_text(text+'\n')
if __name__=='__main__':main()
