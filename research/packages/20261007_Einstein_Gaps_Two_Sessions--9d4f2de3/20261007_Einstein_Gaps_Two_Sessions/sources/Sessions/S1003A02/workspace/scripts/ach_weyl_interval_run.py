"""Run and summarize the CAPD off-bolt Weyl certificate for Theorem E.

The C++ program transports each outward-rounded Fuchsian initial box from
t=0.01 to t=0.5 and evaluates both diagonal chiral curvature blocks.  Since
the metric is Einstein with s=-24, adding 2 to each reported raw eigenvalue
gives the Weyl eigenvalue.  Pairwise gaps are unchanged.

A point-box comparison against the independent coordinate/JAX calculation is
performed first.  Then all forty d-tiles are enclosed.  The output records the
smallest distance of every signed gap from zero and the discriminant lower
bounds, as well as the point-comparison errors.
"""
from pathlib import Path
import json, subprocess, sys
import numpy as np

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
BOXES=ROOT/'data'/'ach_capd'/'fuchs_boxes_N6_complex_v2.json'
EXE=HERE/'ach_weyl_interval'
OUT=ROOT/'data'/'ach_capd'/'weyl_discriminant_t0.5.json'
sys.path.insert(0,str(HERE))
from ach_weyl_degeneracy_offbolt import evaluate_d


def ff(s):
    return float.fromhex(s)


def iv(x):
    return [ff(x[0]),ff(x[1])]


def invoke(box):
    args=[str(EXE),'0.49','30']+[repr(float(x)) for pair in box for x in pair]
    p=subprocess.run(args,text=True,capture_output=True,check=True)
    rec=json.loads(p.stdout)
    for key in ['endpoint_hex','Araw','Braw','Agaps','Bgaps']:
        rec[key]=[iv(x) for x in rec[key]]
    rec['Adisc']=iv(rec['Adisc']); rec['Bdisc']=iv(rec['Bdisc'])
    return rec


def gap_distance(g):
    lo,hi=g
    return 0.0 if lo<=0<=hi else min(abs(lo),abs(hi))


def sorted_mid_weyl(raw):
    return np.sort(np.array([(x[0]+x[1])/2+2 for x in raw]))


def main():
    src=json.loads(BOXES.read_text())
    tiles=src['boxes']
    # First use a zero-width midpoint box and compare with independent coordinates.
    j=min(range(len(tiles)),key=lambda i:abs(sum(tiles[i]['d'])/2-0.286999618893))
    b=tiles[j]['binary64_box']; point=[[sum(x)/2]*2 for x in b]
    dmid=point[6][0]
    pc=invoke(point)
    # Compare the CAPD curvature formulas against coordinate/JAX curvature on
    # the very same CAPD endpoint midpoint (not a separately initialized shoot).
    from einstein_bolt_shoot import rhs
    from ach_weyl_degeneracy_offbolt import metric_local,blocks,ANG
    import jax.numpy as jnp
    ep=np.array([sum(x)/2 for x in pc['endpoint_hex']])
    m,de,L3,ym,eta,y3,_=ep
    L=np.array([m+de/2,m-de/2,L3]); yy=np.array([ym+eta/2,ym-eta/2,y3])
    yp=rhs(0.5,np.r_[L,yy])[3:]
    aa=np.exp(L); ap=aa*yy; app=aa*(yy*yy+yp)
    JA,JB,scal,ric0=blocks(metric_local(0.5,aa,ap,app),jnp.r_[jnp.array([0.5]),ANG])
    fA=np.sort(np.linalg.eigvalsh(JA)); fB=np.sort(np.linalg.eigvalsh(JB))
    # CAPD A corresponds to coordinate/JAX B and conversely under the basis labels.
    cA=sorted_mid_weyl(pc['Araw']); cB=sorted_mid_weyl(pc['Braw'])
    comparison={
      'tile':j,'d_mid':dmid,'endpoint_midpoint_scalar':scal,
      'endpoint_midpoint_ric0_norm':ric0,
      'capd_A_weyl_sorted':cA.tolist(),'jax_B_weyl_sorted':fB.tolist(),
      'capd_B_weyl_sorted':cB.tolist(),'jax_A_weyl_sorted':fA.tolist(),
      'max_abs_error_A_vs_jaxB':float(np.max(np.abs(cA-fB))),
      'max_abs_error_B_vs_jaxA':float(np.max(np.abs(cB-fA))),
      'capd_point_A_gaps':pc['Agaps'],'capd_point_B_gaps':pc['Bgaps']}
    print('point comparison',json.dumps(comparison))

    rows=[]
    for i,tile in enumerate(tiles):
        q=invoke(tile['binary64_box'])
        row={'tile':i,'d':tile['d'],'Araw':q['Araw'],'Braw':q['Braw'],
             'Agaps':q['Agaps'],'Bgaps':q['Bgaps'],
             'Adisc':q['Adisc'],'Bdisc':q['Bdisc'],
             'endpoint':q['endpoint_hex']}
        rows.append(row)
        print(i,tile['d'],'min gaps',min(map(gap_distance,q['Agaps'])),min(map(gap_distance,q['Bgaps'])))
    allAg=[gap_distance(g) for r in rows for g in r['Agaps']]
    allBg=[gap_distance(g) for r in rows for g in r['Bgaps']]
    out={'status':'rigorous CAPD transport from outward-rounded analytic Fuchsian boxes',
         'input':str(BOXES),'time_interval':[0.01,0.5],'duration':0.49,
         'order':30,'tiles':len(rows),'point_comparison':comparison,
         'minimum_abs_A_gap_lower':min(allAg),
         'minimum_abs_B_gap_lower':min(allBg),
         'minimum_A_discriminant_lower':min(r['Adisc'][0] for r in rows),
         'minimum_B_discriminant_lower':min(r['Bdisc'][0] for r in rows),
         'all_gaps_exclude_zero':all(x>0 for x in allAg+allBg),
         'rows':rows}
    OUT.write_text(json.dumps(out,indent=1)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k!='rows'},indent=1))

if __name__=='__main__': main()
