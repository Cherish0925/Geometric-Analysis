"""Run the custom CAPD Einstein-bolt enclosure in short validated time segments.

The companion Arb script supplies the first interval box.  Each CAPD endpoint is
fed into the next segment, mitigating wrapping.  The final record preserves every
command-independent hexadecimal enclosure.  This is an IVP certificate for the
truncated bolt polynomial data; it does not supply the still-required Fuchsian tail.
"""
import argparse, json, math, subprocess
from pathlib import Path

HERE=Path(__file__).resolve().parent
BIN=HERE/'ach_bolt_capd'

def fhex(s): return float.fromhex(s)

def run(box,dt,order):
    args=['qiushi-yau26','env','ode',str(BIN),repr(dt),str(order)]
    for p in box: args += [repr(p[0]),repr(p[1])]
    cp=subprocess.run(args,check=True,text=True,capture_output=True)
    rec=json.loads(cp.stdout)
    rec['endpoint']=[[fhex(a),fhex(b)] for a,b in rec['endpoint_hex']]
    rec['compact_float']={k:[fhex(a),fhex(b)] for k,(a,b) in rec['compact'].items()}
    return rec

if __name__=='__main__':
    ap=argparse.ArgumentParser(); ap.add_argument('--initial',required=True); ap.add_argument('--duration',type=float,required=True)
    ap.add_argument('--dt',type=float,default=.02); ap.add_argument('--order',type=int,default=30); ap.add_argument('--out',required=True)
    a=ap.parse_args(); ini=json.loads(Path(a.initial).read_text()); box=ini['binary64_box']
    steps=[]; t=ini['t0']; remain=a.duration
    while remain>1e-15:
        h=min(a.dt,remain); rec=run(box,h,a.order); t+=h; remain-=h
        steps.append({'t':t,'dt':h,'endpoint_hex':rec['endpoint_hex'],'compact':rec['compact'],'compact_float':rec['compact_float']})
        box=rec['endpoint']
        widths=[p[1]-p[0] for p in box]
        print(t,'maxwidth',max(widths),'zeta',rec['compact_float']['zeta'],'ub',rec['compact_float']['ub'],flush=True)
        if not all(math.isfinite(x) for p in box for x in p): raise RuntimeError('nonfinite')
    out={'initial':a.initial,'duration':a.duration,'dt':a.dt,'order':a.order,'steps':steps,'final':steps[-1]}
    Path(a.out).write_text(json.dumps(out,indent=1)+'\n')
