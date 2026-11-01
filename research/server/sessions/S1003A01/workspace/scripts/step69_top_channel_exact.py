#!/usr/bin/env python3
"""Step 69: exact principal top-kernel/torsion correspondence in Darboux gauge.

For a homogeneous anti-J metric jet H_d with d=n+2, compute
  (i) the flat Einstein condition L_{d-2} H_d = 0;
  (ii) the first induced torsion variation v of degree d-1=n+1;
then express v in complex form
  v(z,w) = z h(w) + g(w),  w=bar z.

We build exact integer matrices for the metric kernel, the full real torsion
polynomial, the complement to the half-twistor image, and the scalar
polarization from Spirit Step 68.  The purpose is to establish (rather than
infer from matching ranks) that every flat-kernel metric jet has precisely the
claimed half-twistor type, and to compare the induced scalar image with the
formula
 -2 Re[ tr(bar B Dg) + (3n+8) bar c h + 4 (Dh)^T bar B z ].

Conventions follow A02's Darboux engine: Omega=J0^T, g=exp(H), H anti-J,
and a_k=<nabla_k Omega,phi>/4.  At linear order in H_d,
  delta a_k = -(1/4)(Gamma^l_{ki} Omega_lj + Gamma^l_{kj} Omega_il) phi_ij.
All coefficient matrices are exact integers/rationals (SymPy).
"""
from pathlib import Path
import itertools, json, sys
import numpy as np
import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import step68_flat_cokernel as F

OUT = HERE.parent / "data" / "step69"
OUT.mkdir(parents=True, exist_ok=True)

J0 = sp.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])
OM = J0.T
PHI = sp.Matrix([[0,0,1,0],[0,0,0,-1],[-1,0,0,0],[0,1,0,0]])
BS = [sp.Matrix(x) for x in F.anti_basis()]
I = sp.I
z1,z2,w1,w2 = sp.symbols('z1 z2 w1 w2', real=True)
xs = sp.symbols('x0:4', real=True)
SUB_ZW = {xs[0]:(z1+w1)/2, xs[1]:(z1-w1)/(2*I),
          xs[2]:(z2+w2)/2, xs[3]:(z2-w2)/(2*I)}
VARS = (z1,z2,w1,w2)


def mons_deg(d):
    return F.mons_deg(d)


def mon_expr(m):
    q=sp.S.One
    for x,e in zip(xs,m): q*=x**e
    return q


def dpoly_coeff(m,k):
    if m[k]==0: return 0,None
    mm=list(m); c=mm[k]; mm[k]-=1
    return c,tuple(mm)


def torsion_matrix(d):
    """Real coefficient map H_d -> a_{d-1}; rows k then degree-(d-1) monomial."""
    src=mons_deg(d); tgt=mons_deg(d-1); ti={m:i for i,m in enumerate(tgt)}
    M=sp.zeros(4*len(tgt),6*len(src))
    # Gamma^l_ki = 1/2 (d_k h_li + d_i h_lk - d_l h_ki)
    for aa,B in enumerate(BS):
      for q,m in enumerate(src):
        col=aa*len(src)+q
        for k in range(4):
          # coefficient tensor of nabla_k Omega, contracted with phi /4
          for deriv in range(4):
            c,mm=dpoly_coeff(m,deriv)
            if not c: continue
            coeff=sp.S.Zero
            for i in range(4):
              for j in range(4):
                if PHI[i,j]==0: continue
                # first connection term: -Gamma^l_ki Omega_lj
                for l in range(4):
                  gam=sp.Rational(1,2)*(
                       (B[l,i] if deriv==k else 0)
                      +(B[l,k] if deriv==i else 0)
                      -(B[k,i] if deriv==l else 0))
                  coeff += -sp.Rational(1,4)*PHI[i,j]*gam*OM[l,j]
                  # second: -Gamma^l_kj Omega_il
                  gam2=sp.Rational(1,2)*(
                       (B[l,j] if deriv==k else 0)
                      +(B[l,k] if deriv==j else 0)
                      -(B[k,j] if deriv==l else 0))
                  coeff += -sp.Rational(1,4)*PHI[i,j]*gam2*OM[i,l]
            if coeff:
              M[k*len(tgt)+ti[mm],col] += c*coeff
    return M


def involution(p):
    return sp.conjugate(p).xreplace({z1:w1,z2:w2,w1:z1,w2:z2})


def real_poly_matrix(polys, degree):
    """Columns real polynomials -> coefficient matrix in x monomials."""
    mons=mons_deg(degree)
    rows=[]
    for m in mons:
      rows.append([sp.Poly(sp.expand(p),*xs).as_dict().get(m,0) for p in polys])
    return sp.Matrix(rows)


def ht_basis(n):
    """Real basis columns for v=z h(w)+g(w), returned as 4 real component polynomials in x."""
    cols=[]; labels=[]; hg=[]
    # convert complex component polynomial p(z,w) to Re/Im after z=x+iy,w=x-iy
    back={z1:xs[0]+I*xs[1],w1:xs[0]-I*xs[1],z2:xs[2]+I*xs[3],w2:xs[2]-I*xs[3]}
    for j in range(n+1):
      h0=w1**j*w2**(n-j)
      for phase,name in ((1,'re'),(I,'im')):
        h=phase*h0; g=sp.zeros(2,1)
        vv=sp.Matrix([z1*h,z2*h])
        vx=[sp.expand_complex(vv[k].subs(back)).as_real_imag()[0] for k in range(2)]
        vy=[sp.expand_complex(vv[k].subs(back)).as_real_imag()[1] for k in range(2)]
        cols.append([vx[0],vy[0],vx[1],vy[1]]); labels.append(f'h{j}_{name}'); hg.append((h,g))
    for k in range(2):
      for j in range(n+2):
        for phase,name in ((1,'re'),(I,'im')):
          h=sp.S.Zero; g=sp.zeros(2,1); g[k]=phase*w1**j*w2**(n+1-j)
          vv=g
          vx=[sp.expand_complex(vv[r].subs(back)).as_real_imag()[0] for r in range(2)]
          vy=[sp.expand_complex(vv[r].subs(back)).as_real_imag()[1] for r in range(2)]
          cols.append([vx[0],vy[0],vx[1],vy[1]]); labels.append(f'g{k}_{j}_{name}'); hg.append((h,g))
    mons=mons_deg(n+1); H=sp.zeros(4*len(mons),len(cols))
    for col,ps in enumerate(cols):
      for comp,p in enumerate(ps):
        pd=sp.Poly(p,*xs).as_dict()
        for r,m in enumerate(mons): H[comp*len(mons)+r,col]=pd.get(m,0)
    return H,labels,hg


def scalar_formula_matrix(n,c,B,hg):
    """Coefficient map from half-twistor parameters to real scalar degree n."""
    cols=[]
    z=sp.Matrix([z1,z2]); ws=(w1,w2)
    for h,g in hg:
      Dh=sp.Matrix([sp.diff(h,t) for t in ws])
      Dg=g.jacobian(ws)
      # Follow the Step-65/Spirit convention literally: ordinary matrix trace
      # tr(bar(B) Dg), with entrywise conjugation but no adjoint.
      q=sp.trace(sp.conjugate(B)*Dg)
      q+=(3*n+8)*sp.conjugate(c)*h+4*(Dh.T*sp.conjugate(B)*z)[0]
      cols.append(sp.expand(-q-involution(q)))
    # coefficients in x coordinates, where z=x+iy,w=x-iy
    back={z1:xs[0]+I*xs[1],w1:xs[0]-I*xs[1],z2:xs[2]+I*xs[3],w2:xs[2]-I*xs[3]}
    mons=mons_deg(n); A=sp.zeros(len(mons),len(cols))
    for j,p in enumerate(cols):
      p=sp.expand(p.subs(back)); pd=sp.Poly(p,*xs).as_dict()
      for r,m in enumerate(mons): A[r,j]=sp.simplify(pd.get(m,0))
    return A


def first_jet_from_cB(c,B):
    """Real Jacobian D a for f=c z+B bar z, rows target real components."""
    Z=(z1,z2); W=(w1,w2); f=sp.Matrix([c*Z[k]+sum(B[k,j]*W[j] for j in range(2)) for k in range(2)])
    back={z1:xs[0]+I*xs[1],w1:xs[0]-I*xs[1],z2:xs[2]+I*xs[3],w2:xs[2]-I*xs[3]}
    fr=[sp.expand_complex(f[0].subs(back)).as_real_imag()[0],sp.expand_complex(f[0].subs(back)).as_real_imag()[1],sp.expand_complex(f[1].subs(back)).as_real_imag()[0],sp.expand_complex(f[1].subs(back)).as_real_imag()[1]]
    return sp.Matrix([[sp.diff(fr[i],xs[j]) for j in range(4)] for i in range(4)])


def kernel_basis_exact(L):
    return sp.Matrix(L.tolist()).nullspace()


def run(d,c,B):
    n=d-2
    L=sp.Matrix(F.L_matrix(d-2).tolist()) # factor 2 irrelevant
    K=sp.Matrix.hstack(*L.nullspace())
    T=torsion_matrix(d)
    TK=T*K
    H,labels,hg=ht_basis(n)
    # exact containment and image equality ranks
    rkTK=TK.rank(); rkH=H.rank(); rkjoin=sp.Matrix.hstack(H,TK).rank()
    # coordinates X with H X=TK; use gauss_jordan_solve columnwise
    Xcols=[]; coord_ok=True
    for j in range(TK.cols):
      try:
        sol,pars=H.gauss_jordan_solve(TK[:,j]); sol=sol.subs({p:0 for p in pars}); Xcols.append(sol)
      except ValueError:
        coord_ok=False; break
    X=sp.Matrix.hstack(*Xcols) if coord_ok else None
    Aform=scalar_formula_matrix(n,c,B,hg)
    induced=Aform*X if X is not None else None
    rec={'d':d,'n':n,'dim_ker_metric':K.cols,'rank_torsion_image':rkTK,
         'dim_half_twistor_parameter':H.cols,'rank_half_twistor_image':rkH,
         'rank_join':rkjoin,'contained':rkjoin==rkH,
         'onto_half_twistor':rkjoin==rkH and rkTK==rkH,
         'scalar_formula_rank_on_metric_kernel': induced.rank() if induced is not None else None,
         'scalar_formula_rank_full_ht':Aform.rank()}
    rec['expected_scalar_rank_strict_cone'] = 10 if n==2 else 4*(n+1)
    # radial moment exactly
    if n%2==0 and induced is not None:
      mons=mons_deg(n); rad=[]
      for m in mons:
        p=mon_expr(m)
        for _ in range(n//2): p=sum(sp.diff(p,x,x) for x in xs)
        rad.append(sp.expand(p))
      rv=sp.Matrix([rad])
      rec['radial_metric_image_zero']=bool((rv*induced).is_zero_matrix)
      rec['radial_ht_image_zero']=bool((rv*Aform).is_zero_matrix)
    return rec, {'L':L,'K':K,'T':T,'TK':TK,'H':H,'X':X,'Aform':Aform,'induced':induced}


def main():
    c=sp.S.One
    S=sp.Matrix([[2,1],[1,1+I]])
    B=S+sp.Matrix([[0,2+2*I],[-2-2*I,0]])
    records=[]
    # Exact d=4,6,8 are modest; d=10 may be expensive and is optional.
    ds=[int(x) for x in sys.argv[1:]] if len(sys.argv)>1 else [4,6,8]
    for d in ds:
      rec,mats=run(d,c,B); records.append(rec); print(json.dumps(rec),flush=True)
      # save compressed numeric matrices needed for independent comparisons
      to_real = lambda M: np.array([[float(sp.re(sp.N(x))) for x in M.row(i)] for i in range(M.rows)])
      np.savez_compressed(OUT/f'top_channel_d{d}.npz',
          K=to_real(mats['K']), TK=to_real(mats['TK']), H=to_real(mats['H']),
          X=to_real(mats['X']), Aform=to_real(mats['Aform']), induced=to_real(mats['induced']))
    (OUT/'top_channel_exact.json').write_text(json.dumps({'records':records},indent=2)+'\n')

if __name__=='__main__': main()
