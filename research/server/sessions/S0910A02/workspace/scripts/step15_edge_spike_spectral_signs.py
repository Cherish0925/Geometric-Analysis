"""
Step 15 sign-controlled spectral probe.

Question: does the 2D spectral constraint lambda_1^Dir <= 2 forbid localized
negative base curvature near geodesic right-angle edges?

We use conformal rectangles g=e^{2phi}(dx^2+dy^2), with phi=f(d) depending on
inward distance d to the boundary and f'(0)=0, so straight boundary segments
remain geodesic and right angles remain right angles.  Curvature is
K=-e^{-2phi}Delta phi.  Two signs:
  +phi collar: positive K at the edge, negative K in an interior subcollar;
  -phi collar: negative K at the edge, positive K in an interior subcollar.
The generalized eigenproblem is -Delta_E u = lambda e^{2phi}u, then the metric
is rescaled to fixed area A0.
"""
import json, math, os
import numpy as np
from scipy.sparse import diags
from scipy.sparse.linalg import eigsh

HERE=os.path.dirname(os.path.abspath(__file__))
DATA=os.path.abspath(os.path.join(HERE,"..","data"))
os.makedirs(DATA,exist_ok=True)
A0=10.0
j0=2.404825557695773
A_FK=math.pi*j0*j0/2
L=math.sqrt(A0)


def solve(sign=-1, amp=1.0, width=0.05, N=70):
    Nx=Ny=N; Lx=Ly=L
    hx=Lx/(Nx+1); hy=Ly/(Ny+1)
    xs=(np.arange(Nx)+1)*hx; ys=(np.arange(Ny)+1)*hy
    X,Y=np.meshgrid(xs,ys,indexing='ij')
    d=np.minimum.reduce([X,Lx-X,Y,Ly-Y])
    phi=sign*amp*np.exp(-(d/width)**2)
    weight=np.exp(2*phi).reshape(-1)
    area=float(np.sum(weight)*hx*hy)
    n=Nx*Ny
    main=np.full(n,2/hx**2+2/hy**2)
    off1=np.full(n-1,-1/hy**2)
    for i in range(Nx):
        if i*Ny+Ny-1<n-1: off1[i*Ny+Ny-1]=0.0
    offN=np.full(n-Ny,-1/hx**2)
    A=diags([main,off1,off1,offN,offN],[0,-1,1,-Ny,Ny],format='csr')
    M=diags(weight,0,format='csr')
    lam=float(eigsh(A,k=1,M=M,sigma=0.0,which='LM',return_eigenvectors=False)[0])
    cscale=A0/area
    lam_scaled=lam/cscale
    # analytic 1D normal curvature at edge and at d=width
    def f(dval): return sign*amp*math.exp(-(dval/width)**2)
    def fpp(dval):
        return sign*amp*math.exp(-(dval/width)**2)*(-2/width**2+4*dval**2/width**4)
    K_edge=-math.exp(-2*f(0.0))*fpp(0.0)
    K_at_w=-math.exp(-2*f(width))*fpp(width)
    # finite difference interior extrema
    ph=phi
    lap=np.zeros_like(ph)
    lap[1:-1,1:-1]=((ph[2:,1:-1]-2*ph[1:-1,1:-1]+ph[:-2,1:-1])/hx**2+
                    (ph[1:-1,2:]-2*ph[1:-1,1:-1]+ph[1:-1,:-2])/hy**2)
    K=-np.exp(-2*ph)*lap
    KdA=K*np.exp(2*ph)*hx*hy
    return dict(sign=sign, amp=amp, width=width, N=N,
                area_raw=area, lambda1_raw=lam, lambda1_scaled=lam_scaled,
                spectral_bound_2=bool(lam_scaled<=2.0),
                K_edge_analytic=K_edge, K_at_width_analytic=K_at_w,
                minK_interior=float(np.min(K[1:-1,1:-1])),
                maxK_interior=float(np.max(K[1:-1,1:-1])),
                int_K_negative_interior=float(np.sum(np.minimum(KdA[1:-1,1:-1],0))),
                int_K_positive_interior=float(np.sum(np.maximum(KdA[1:-1,1:-1],0))))

cases=[]
for sign in [-1,1]:
    for amp in [0.25,0.5,1.0,2.0,3.0]:
        for width in [0.03,0.05,0.08,0.12]:
            cases.append(solve(sign=sign,amp=amp,width=width,N=60))

# select cases with negative edge curvature and lambda<=2
neg_edge_good=[c for c in cases if c['K_edge_analytic']<0 and c['spectral_bound_2']]
strong_neg_edge=[c for c in cases if c['K_edge_analytic']<0]
strong_neg_edge=sorted(strong_neg_edge,key=lambda c:c['K_edge_analytic'])[:8]

report={
  'title':'Step 15 sign-controlled edge spectral test',
  'area_target':A0,
  'Faber_Krahn_area_delta0':A_FK,
  'cases':cases,
  'negative_edge_and_lambda<=2_count':len(neg_edge_good),
  'negative_edge_good_examples':neg_edge_good[:10],
  'strongest_negative_edge_cases':strong_neg_edge,
  'finding':('There are conformal right-angle/geodesic-edge rectangle relaxations with K_edge<0 and lambda1_scaled<=2 for moderate narrow collars. Thus the Dirichlet spectral bound and McKean/Cheng-type global intuition do not forbid localized negative edge curvature. Stronger or wider negative-edge collars can violate lambda<=2 after fixed-area normalization, so spectral geometry limits the spike size but does not exclude the boundary-bubble mechanism.'),
  'limitations':['2D conformal relaxation only; not a toric 4D Ricci-pinched metric','does not enforce primitive rod fiber ODE or full reduced Ricci inequalities','curvature signs include compensating positive collars as required by Gauss-Bonnet']
}
OUT=os.path.join(DATA,'step15_edge_spike_spectral_signs.json')
with open(OUT,'w') as f: json.dump(report,f,indent=2)
print(json.dumps({
 'title':report['title'],
 'negative_edge_and_lambda<=2_count':len(neg_edge_good),
 'negative_edge_good_examples':[{k:c[k] for k in ['sign','amp','width','lambda1_scaled','K_edge_analytic','K_at_width_analytic','minK_interior','maxK_interior']} for c in neg_edge_good[:8]],
 'strongest_negative_edge_cases':[{k:c[k] for k in ['sign','amp','width','lambda1_scaled','spectral_bound_2','K_edge_analytic']} for c in strong_neg_edge],
 'finding':report['finding'],
 'saved':OUT},indent=2))
