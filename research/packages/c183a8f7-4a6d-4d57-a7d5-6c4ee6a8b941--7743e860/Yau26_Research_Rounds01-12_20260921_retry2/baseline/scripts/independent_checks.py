"""Bounded checks for the OT extension, AH budget and marked filling algebra.

These are finite algebraic checks, not classification or global gluing proofs.
Original independent programs are extracted by source_archive.py and can be
checked with --original-check NAME in an isolated working directory.
"""
from __future__ import annotations

import argparse
import contextlib
import io
import json
from pathlib import Path
import re
import runpy
import sys

sys.dont_write_bytecode = True


def require(condition, message):
    if not bool(condition):
        raise ValueError(message)


def zero(value):
    import sympy as s
    return all(s.simplify(x) == 0 for x in value) if isinstance(value, s.MatrixBase) else s.simplify(value) == 0


def ot_critical():
    import sympy as s
    ep, energy = s.symbols('epsilon energy', nonnegative=True)
    # Nonpositive smaller Hessian eigenvalue: trace/2 <= TF norm <= energy/8+ep/2.
    bound = s.solve((3-ep)/2-energy/8-ep/2, energy)[0]
    require(zero(bound-(12-8*ep)), 'OT critical-point factor')
    require(not zero(bound-(12-4*ep)), 'Incorrect block-error factor accepted')
    k, target = 3+ep, 12-8*ep
    left = s.expand(k*(target-2*k)-4*ep**2)
    polynomial = s.expand(left**2-64*ep**2*k*target)
    endpoints = (s.Rational(24624, 100000), s.Rational(24626, 100000))
    for point, sign in zip(endpoints, (1, -1)):
        require(left.subs(ep, point)>0 and target.subs(ep, point)>0, 'Invalid radical squaring')
        require(sign*polynomial.subs(ep, point)>0, 'OT threshold bracket')
    # Exact trace-free Hessian cancellation in two base dimensions.
    p,q,a,b,c,d=s.symbols('p q a b c d')
    gradient=s.Matrix([p,q]); A=s.Matrix([[a,b],[b,c]]); E=s.Matrix([[a,d],[d,b]])
    tf=lambda M:M-s.eye(2)*s.trace(M)/2
    hess_sigma=-gradient*gradient.T/2-A/2-E
    require(zero(tf(hess_sigma/2+gradient*gradient.T/4)+tf(A)/4+tf(E)/2), 'Hess mu trace-free cancellation')
    require(not zero(tf(hess_sigma/2+gradient*gradient.T/4)+tf(A)/2+tf(E)/2), 'Wrong shape coefficient accepted')
    return {'scope':'critical-point algebra and exact rational root bracket; heat kernel and Morse proof are in the paper',
            'epsilon_star_bracket':['0.24624','0.24626'], 'negative_controls_rejected':2}


def ah_matching():
    import sympy as s
    ep=s.symbols('epsilon',nonnegative=True)
    coefficient=s.expand((12-4*ep)**2/24-2*ep**2)
    require(zero(coefficient-(6-4*ep-s.Rational(4,3)*ep**2)), 'CGB normalization')
    require(coefficient.subs(ep,s.Rational(1,4))>0, 'Nonpositive fixed-topology budget')
    require(not zero(coefficient-(6-4*ep)), 'Dropped quadratic term accepted')
    # Flat diagonal slices: direct warped Ricci versus J-block formulas.
    u=s.symbols('u0:3'); v=s.symbols('v0:3')
    shape=[1+x for x in u]; J=s.diag(*[2*x for x in u]); Jp=s.diag(*[2*x for x in v])
    direct_normal=3-sum(v[i]+shape[i]**2 for i in range(3))
    formula_normal=-s.trace(J)-s.trace(Jp)/2-s.trace(J*J)/4
    direct_tangent=s.diag(*[3-v[i]-shape[i]*sum(shape) for i in range(3)])
    formula_tangent=-Jp/2-3*J/2-s.trace(J)*s.eye(3)/2-s.trace(J)*J/4
    require(zero(direct_normal-formula_normal) and zero(direct_tangent-formula_tangent), 'AH Ricci blocks')
    require(not zero(direct_tangent-(formula_tangent+s.trace(J)*s.eye(3)/2)), 'Missing tangential trace accepted')
    # A coordinate translation rescales q in its description, preserving the physical section.
    t,c=s.symbols('t c',real=True)
    require(zero(s.exp(2*(t+c))*s.exp(-2*c)-s.exp(2*t)), 'Coordinate scale identity')
    require(s.limit(s.exp(3*t)/3,t,s.oo)==s.oo, 'AH core volume growth')
    return {'scope':'CGB coefficient, diagonal Ricci blocks and physical scaling; not a closed connector construction',
            'volume_coefficient':str(coefficient), 'negative_controls_rejected':2}


def two_pole():
    import sympy as s
    # Algebra supporting the actual equivariant gluing argument, not smooth classification itself.
    Q0=s.Matrix([[-2,1],[1,0]]); P0=s.Matrix([[0,1],[1,1]])
    Q1=s.Matrix([[-2,1],[1,-1]]); P1=s.Matrix([[1,0],[1,1]])
    require(abs(P0.det())==1 and P0.T*Q0*P0==s.Matrix([[0,1],[1,0]]), 'Hyperbolic handle form')
    require(abs(P1.det())==1 and P1.T*Q1*P1==-s.eye(2), 'Definite handle form')
    require(all((x*x-y*y)%4 != 2 for x in range(4) for y in range(4)), 'Odd indefinite form excludes square +/-2')
    require(Q0.det()!=Q1.det(), 'Indefinite/definite form confusion')
    require(Q1 != s.Matrix([[-2,1],[1,0]]), 'Wrong second framing accepted')
    rows=[]
    for positive in (False,True):
        for negative in (False,True):
            rows.append({'P_plus':positive,'P_minus':negative,'Q':positive or negative})
    require(next(r['Q'] for r in rows if not r['P_plus'] and r['P_minus']), 'Single-sign disproof error')
    return {'scope':'integral handle forms, parity and sign-branch logic; smooth type also requires the actual torus action',
            'branch_truth_table':rows, 'negative_controls_rejected':2}


ORIGINALS={
 'ot':'final_review/r4_OT_identities.py',
 'core':'final_review/r2_core.py',
 'weyl':'final_review/r1_weylgauge.py',
 'log':'verify/v2_logidentity.py',
 'bundle':'audit_bundle/c1_explicit_crosscheck.py',
 'ah':'final_review/r6_gaussian_blocks.py',
 'bochner':'audit_obstructions/itemG_bochner_identity.py',
}


def check_original(name, source_root):
    # The caller must first extract a checked package, then run in its sandbox.
    import sympy as s
    from source_archive import checked_sources
    package=Path(__file__).resolve().parents[1]
    sources=checked_sources(package)
    relative=ORIGINALS[name]
    path=Path(source_root)/relative
    require(path.is_file() and path.read_bytes()==sources[relative], 'Original script differs from embedded source')
    capture=io.StringIO()
    with contextlib.redirect_stdout(capture):
        ns=runpy.run_path(str(path),run_name='__main__')
    output=capture.getvalue()
    if name=='ot':
        require(zero(ns['Ric'][:2,:2]-ns['claim_base']), 'Original OT base block')
        require(zero(ns['Ric'][:2,2:]), 'Original OT mixed block')
        require(zero(ns['trF']+ns['lap'](ns['sig'])+ns['gradsq']), 'Original OT fibre trace')
        require(zero(ns['EF0']+ns['Mi']*ns['tau']/2), 'Original OT fibre trace-free block')
    elif name=='core':
        require(zero(ns['R0']) and zero(ns['D']-ns['k']), 'Original EH core linearization')
        require(s.limit(ns['hss']-ns['h33'],ns['rho'],1)==0, 'Original bolt mismatch')
    elif name=='weyl':
        require(ns['ric'](ns['Rs'])==s.eye(4), 'Original core far-field contraction')
        require(zero(ns['DRic'](ns['Hstar'])-s.eye(4)), 'Original Weyl-jet Ricci')
        require(zero(ns['DRic'](ns['K'])), 'Original Weyl kernel')
    elif name=='log':
        require(zero(ns['diff']), 'Original final dimension logarithmic identity')
        require(len(re.findall(r'max residual zero\?\s+True',output))==2 and 'False' not in output,
                'Original dimension 4 or 5 logarithmic identity')
    elif name=='bundle':
        require(zero(ns['res']), 'Original full ED Ricci matrix')
    elif name=='ah':
        values=re.findall(r'resid ([0-9.+eE-]+)',output)
        require(len(values)==12 and all(abs(float(v))<1e-10 for v in values), 'Original sampled Gaussian blocks')
    elif name=='bochner':
        values=re.findall(r'at the origin = (.+)',output)
        require(len(values)==5 and all(v.strip()=='0' for v in values), 'Original rational-jet Bochner identity')
    require('False' not in output, 'Original diagnostic reports failure')
    return {'status':'passed','source':relative,'output':output,
            'scope':'inspected original finite computation; not its source report\'s global claims'}


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--original-check',choices=ORIGINALS,required=True)
    parser.add_argument('--source-root',type=Path,required=True)
    args=parser.parse_args()
    try:
        print(json.dumps(check_original(args.original_check,args.source_root),ensure_ascii=False))
    except Exception as exc:
        print(json.dumps({'status':'failed','error':str(exc)}))
        raise SystemExit(1)
