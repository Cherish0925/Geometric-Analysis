"""Step 98b: optimize a complete SPD matrix transition using cubic Hermite controls.

Unlike the single quintic baseline, this represents the logarithmic matrix X(r,s)
by piecewise cubic Hermite interpolation through free interior values/slopes.  Exact
charged-Koiso value/first jet is fixed at the center, and the expanding attachment
X=2RI, X_r=2I is fixed at the outer endpoint.  The SPD map
q=q0^(1/2) exp(X) q0^(1/2) retains the full orbit matrix and mixed directions.

Residual evaluation reuses step98_full_matrix_joint_transition.py and includes all
Ricci blocks with invariant generalized-eigenvalue norms.  This is a finite-dimensional
experiment, not a theorem.
"""
from __future__ import annotations
import argparse, importlib.util, json, math
from pathlib import Path
import numpy as np
from scipy.interpolate import CubicHermiteSpline
from scipy.optimize import least_squares

HERE=Path(__file__).resolve().parent
SESSION=HERE.parents[1]
p=HERE/'step98_full_matrix_joint_transition.py'
spec=importlib.util.spec_from_file_location('fm',p); fm=importlib.util.module_from_spec(spec);spec.loader.exec_module(fm)


def controls_from_baseline(geom,R,sign,knots):
    ns=len(geom['s']); z=np.zeros_like(geom['q0']); I=np.eye(3)[None,:,:]*np.ones((ns,1,1))
    coeff=fm.quintic_coefficients(z,2*sign*geom['A'],2*geom['B'],2*R*I,2*I,np.zeros_like(I),R)
    t=knots/R
    vals=fm.eval_poly(coeff,t)
    # derivative in n
    dcoeff=np.stack([k*coeff[k] for k in range(1,6)],axis=0)/R
    slopes=fm.eval_poly(dcoeff,t)
    return vals,slopes


def build_basis(s,wind,richer):
    mats,names=fm.matrix_basis(s,wind,richer)
    # Orthonormalize the sampled Frobenius inner product to improve conditioning.
    A=np.stack([m.ravel() for m in mats],axis=1)
    Q,R=np.linalg.qr(A)
    rank=np.sum(np.abs(np.diag(R))>1e-10)
    Q=Q[:,:rank]
    mats2=[Q[:,j].reshape(mats[0].shape)*math.sqrt(len(s)) for j in range(rank)]
    return mats2,names[:rank]


def perturb_controls(basev,based,theta,basis,free_value_ids,free_slope_ids):
    vals=basev.copy(); slopes=based.copy(); p=0
    for kid in free_value_ids:
        for b in basis:
            vals[kid]+=theta[p]*b; p+=1
    for kid in free_slope_ids:
        for b in basis:
            slopes[kid]+=theta[p]*b; p+=1
    return vals,slopes


def build_q(geom,R,nr,sign,theta,knot_fracs,basis,free_value_ids,free_slope_ids):
    t,Dt,D2t=fm.chebyshev_lobatto_01(nr); r=R*t; knots=R*np.array(knot_fracs)
    bv,bd=controls_from_baseline(geom,R,sign,knots)
    vals,slopes=perturb_controls(bv,bd,theta,basis,free_value_ids,free_slope_ids)
    # Interpolate every matrix component and s-point simultaneously.
    spl=CubicHermiteSpline(knots,vals,slopes,axis=0)
    X=spl(r); Xn=spl(r,1); Xnn=spl(r,2)
    nr0,ns=X.shape[:2]; q=np.zeros_like(X); qn=np.zeros_like(X); qnn=np.zeros_like(X)
    # q derivatives are evaluated spectrally from q except exact endpoints; this avoids
    # implementing the noncommuting Frechet derivative of exp at interior points.
    for a in range(nr0):
      for b in range(ns): q[a,b]=geom['sq'][b]@fm.sym_exp(X[a,b])@geom['sq'][b]
    Dr=Dt/R;D2r=D2t/(R*R)
    qn,qnn=fm.normal_derivatives(q,Dr,D2r)
    target_qnn=2*(geom['ric0']+3*geom['q0']+2*np.einsum('sij,sjk,skl->sil',geom['k0'],np.linalg.inv(geom['q0']),geom['k0']))
    qn[0]=2*sign*geom['k0']; qnn[0]=target_qnn
    qn[-1]=2*q[-1];qnn[-1]=4*q[-1]
    res=fm.full_residual(q,Dr,D2r,qn_override=qn,qnn_override=qnn)
    return r,q,res


def optimize_side(geom,R,nr,sign,knot_fracs,richer,max_nfev):
    basis,bnames=build_basis(geom['s'],int(geom['meta']['wind']),richer)
    # All interior knot values are free. Interior slopes are initially fixed to keep
    # parameter count moderate; optional richer Fourier content acts in all matrix blocks.
    freev=list(range(1,len(knot_fracs)-1)); freed=[]
    pcount=(len(freev)+len(freed))*len(basis); x0=np.zeros(pcount)
    def evaluate(x,detail=False):
        r,q,res=build_q(geom,R,nr,sign,x,knot_fracs,basis,freev,freed)
        if detail:return r,q,res
        return fm.weighted_vector(res)
    r,q,res0=evaluate(x0,True);F0=evaluate(x0)
    J=fm.finite_difference_jacobian(evaluate,x0,F0,2e-4)
    _,svd=fm.svd_analysis(J,F0,1e-2)
    ls=least_squares(evaluate,x0,jac='2-point',diff_step=2e-4,method='trf',
                     max_nfev=max_nfev,xtol=1e-8,ftol=1e-8,gtol=1e-8,verbose=0,
                     x_scale='jac')
    r,q,res1=evaluate(ls.x,True)
    # Straight line records whether residual and max norm improve smoothly.
    line=[]
    for a in [0,.125,.25,.5,.75,1.0]:
        rr,qq,re=evaluate(a*ls.x,True)
        line.append({'alpha':a,'vector_norm':float(np.linalg.norm(fm.weighted_vector(re))),**fm.summarize_half(rr,re)})
    order=np.argsort(-np.abs(ls.x))[:min(16,len(ls.x))]
    labels=[]
    for kid in freev:
      for bn in bnames:labels.append(f'value@{knot_fracs[kid]:.3f}:{bn}')
    return {
      'side':'positive' if sign>0 else 'negative','parameter_count':pcount,
      'baseline':fm.summarize_half(r,res0),'baseline_vector_norm':float(np.linalg.norm(F0)),
      'linear_svd':svd,
      'least_squares':{'success':bool(ls.success),'status':int(ls.status),'message':ls.message,
                       'nfev':int(ls.nfev),'cost':float(ls.cost),'optimality':float(ls.optimality),
                       'theta_norm':float(np.linalg.norm(ls.x))},
      'final':fm.summarize_half(r,res1),'final_vector_norm':float(np.linalg.norm(fm.weighted_vector(res1))),
      'line':line,'largest_coefficients':[{'name':labels[j],'value':float(ls.x[j])} for j in order]
    }


def main():
 ap=argparse.ArgumentParser();ap.add_argument('--nr',type=int,default=31);ap.add_argument('--ns',type=int,default=32)
 ap.add_argument('--R',type=float,default=1.5);ap.add_argument('--wind',type=int,default=2);ap.add_argument('--S',type=float,default=1.)
 ap.add_argument('--Qmax',type=float,default=.5);ap.add_argument('--richer',action='store_true');ap.add_argument('--max-nfev',type=int,default=5)
 ap.add_argument('--knots',default='0,0.2,0.45,0.7,1');ap.add_argument('--output',default='workspace/data/step98_spd_spline_transition.json')
 a=ap.parse_args();fr=[float(x) for x in a.knots.split(',')];geom=fm.center_geometry(a.ns,a.wind,a.S,a.Qmax)
 pos=optimize_side(geom,a.R,a.nr,+1,fr,a.richer,a.max_nfev);neg=optimize_side(geom,a.R,a.nr,-1,fr,a.richer,a.max_nfev)
 out={'model':'full SPD logarithmic matrix, piecewise cubic Hermite inner transition','parameters':vars(a),
      'positive_half':pos,'negative_half':neg,
      'joint':{'baseline_operator_sup':max(pos['baseline']['operator_sup'],neg['baseline']['operator_sup']),
               'final_operator_sup':max(pos['final']['operator_sup'],neg['final']['operator_sup']),
               'baseline_vector_norm':math.hypot(pos['baseline_vector_norm'],neg['baseline_vector_norm']),
               'final_vector_norm':math.hypot(pos['final_vector_norm'],neg['final_vector_norm'])},
      'status':'Finite-dimensional nonlinear matching experiment; not an existence/nonexistence result.'}
 path=Path(a.output);path=path if path.is_absolute() else SESSION/path;path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(out,indent=2))
 print(json.dumps({'output':str(path),'positive':{'baseline':pos['baseline'],'final':pos['final'],'ls':pos['least_squares']},
                   'negative':{'baseline':neg['baseline'],'final':neg['final'],'ls':neg['least_squares']},'joint':out['joint']},indent=2))
if __name__=='__main__':main()
