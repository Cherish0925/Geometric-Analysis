"""Compare frozen perpendicular cells at fixed physical CH radii.

Outputs metric eigenvalue ratios relative to CH, Einstein-defect components, and J shell
density per geodesic radius.  Fixed-r convergence versus outward drift is relevant to whether
the large-collar sequence approaches a finite-energy CH-asymptotic metric.
"""
import argparse,json,math
from pathlib import Path
from flint import acb,arb,ctx
from perp_rigorous_enclosure import FrozenCell


def one(path,rs):
    rec=json.loads(Path(path).read_text()); cell=FrozenCell(rec); X=float(rec['X']); ell=math.log(X/.01)
    rho=math.asinh(math.sqrt(X)); rows=[]
    for r in rs:
        if not (math.asinh(.1)<r<rho): continue
        x=math.sinh(r)**2; u=math.log(x/.01)/ell
        R,vol,p=cell.ricci(acb(arb(u)),want_profile=True)
        R=[float(v.real.mid()) for v in R]; F=float(p['h1'].real.mid()); G=float(p['G'].real.mid()); h3=float(p['h3'].real.mid())
        lam=[(x+x*x)/G,F/x,1.0,h3/(x+x*x)]
        jdu=float(vol.real.mid())*sum((v+6)**2 for v in R)
        dudr=2*math.sqrt((1+x)/x)/ell
        rows.append(dict(r=r,u=u,lambda_CH=lam,log_lambda_CH=[math.log(v) for v in lam],
                         E=[v+6 for v in R],J_shell_per_r_over_8pi2=jdu*dudr,
                         volume_ratio=math.sqrt(lam[0]*lam[1]*lam[2]*lam[3])))
    return dict(record=path,X=X,rho=rho,J=rec.get('J'),P=rec.get('P'),rows=rows)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('records',nargs='+'); ap.add_argument('--r',default='.15,.2,.3,.4,.6,.8,1,1.2,1.4,1.6,1.8,2,2.2,2.4,2.6'); ap.add_argument('--out')
    a=ap.parse_args(); ctx.prec=80; rs=[float(s) for s in a.r.split(',')]
    out=dict(radii=rs,profiles=[one(p,rs) for p in a.records]); text=json.dumps(out,indent=1); print(text)
    if a.out: Path(a.out).write_text(text+'\n')
if __name__=='__main__':main()
