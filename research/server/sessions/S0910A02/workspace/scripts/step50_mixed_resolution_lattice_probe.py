"""
Step 50 exploratory lattice probe for the diagonal Z2 product quotient.

We use the smooth toric all-compatible resolution as a calibration.  Its fan
has eight divisors with four disjoint (-2)-curves over the A1 points.  In a
Picard basis D2..D7 the intersection matrix is the unimodular submatrix of the
toric divisor matrix.  This script records:
  * fan smoothness and the correct Picard intersection matrix (repairing the
    bad representative computation in step50_toric_fan_spin_probe.json);
  * the four disjoint (-2) exceptional classes inside I_{1,5};
  * the rational invariants expected after replacing r local (-2) fillings by
    orientation-reversed (+2) fillings.

It deliberately does NOT claim a complete integral intersection form for mixed
rows; that requires a boundary linking/gluing computation beyond this probe.
"""
import json, os
import sympy as sp

rays=[(1,0),(0,1),(-1,2),(-1,1),(-1,0),(0,-1),(1,-2),(1,-1)]
self_int=[-1,-2,-1,-2,-1,-2,-1,-2]

def det2(a,b): return a[0]*b[1]-a[1]*b[0]
N=len(rays)
Q=sp.zeros(N)
for i,s in enumerate(self_int):
    Q[i,i]=s
    Q[i,(i+1)%N]=1
    Q[(i+1)%N,i]=1
# For a smooth complete toric surface, quotient by the two linear relations.
# The submatrix on any six divisors whose complementary rays form a Z-basis is
# a unimodular Picard intersection matrix.  D2..D7 works because rays D0,D1 form det=1.
indices=list(range(2,8))
PicQ=Q.extract(indices, indices)
# Exceptional divisors D1,D3,D5,D7 in Picard basis D2..D7.
# Relations from ray coordinates: sum x_i D_i=0, sum y_i D_i=0.
# D0 +0D1 -D2-D3-D4+0D5+D6+D7=0.
# 0D0 +D1 +2D2+D3+0D4-D5-2D6-D7=0.
# Thus D1=-2D2-D3+D5+2D6+D7.
E_vectors={
    "E_at_D1": sp.Matrix([-2,-1,0,1,2,1]),
    "E_at_D3": sp.Matrix([0,1,0,0,0,0]),
    "E_at_D5": sp.Matrix([0,0,0,1,0,0]),
    "E_at_D7": sp.Matrix([0,0,0,0,0,1]),
}
E_names=list(E_vectors.keys())
E_mat=sp.Matrix.hstack(*[E_vectors[n] for n in E_names])
E_pair=E_mat.T*PicQ*E_mat
# Complement equations v^T Q E = 0.
# Compute nullspace over rationals and find a simple integer basis.
A=(PicQ*E_mat).T
null=A.nullspace()
K_basis=[]
for v in null:
    den=sp.ilcm(*[term.q for term in v])
    K_basis.append(sp.Matrix([int(den*term) for term in v]))
if K_basis:
    Kmat=sp.Matrix.hstack(*K_basis)
    Kpair=Kmat.T*PicQ*Kmat
else:
    Kpair=sp.zeros(0)

def sig(M):
    ev=[float(x) for x in M.evalf().eigenvals().keys() for _ in range(M.evalf().eigenvals()[x])] if M.shape[0] else []
    return [sum(1 for x in ev if x>1e-8), sum(1 for x in ev if x<-1e-8)]

def signature_numeric(M):
    if M.shape[0]==0: return [0,0]
    vals=[complex(v) for v in M.evalf().eigenvals().keys() for _ in range(M.evalf().eigenvals()[v])]
    return [sum(1 for z in vals if z.real>1e-8), sum(1 for z in vals if z.real<-1e-8)]

rows=[]
for r in range(5):
    bp=1+r; bm=5-r; tau=bp-bm; chi=2+bp+bm
    if r in (1,3):
        spin="non-spin forced if smooth simply connected, since odd signature is not divisible by 16 (Rokhlin) and even unimodular would require signature divisible by 8"
    elif r==2:
        spin="undetermined by this probe; even spin form would be 3H, odd form would be I_{3,3}; boundary quadratic refinement/Kirby calculation needed"
    else:
        spin="endpoint del Pezzo orientation is non-spin/odd"
    rows.append({"r_reversed":r,"b_plus":bp,"b_minus":bm,"tau":tau,"chi":chi,"spin_status":spin,"strict_Hitchin_Thorpe":2*chi>3*abs(tau)})

out={
    "purpose":"Step50 calibration and mixed-row topology minimum facts",
    "fan_rays":rays,
    "adjacent_determinants":[det2(rays[i],rays[(i+1)%N]) for i in range(N)],
    "smooth_fan":all(det2(rays[i],rays[(i+1)%N])==1 for i in range(N)),
    "toric_self_intersections":self_int,
    "picard_basis":"D2..D7; D0,D1 eliminated because their rays form a Z-basis",
    "picard_intersection_matrix":[[int(PicQ[i,j]) for j in range(PicQ.shape[1])] for i in range(PicQ.shape[0])],
    "picard_determinant":int(PicQ.det()),
    "picard_signature":signature_numeric(PicQ),
    "picard_even":all(int(PicQ[i,i])%2==0 for i in range(PicQ.shape[0])),
    "exceptional_vectors_in_picard_basis":{k:[int(x) for x in list(v)] for k,v in E_vectors.items()},
    "exceptional_pairing":[[int(E_pair[i,j]) for j in range(E_pair.shape[1])] for i in range(E_pair.shape[0])],
    "exceptional_disjoint_minus2":E_pair == -2*sp.eye(4),
    "orthogonal_complement_integer_basis":[[int(x) for x in list(v)] for v in K_basis],
    "orthogonal_complement_pairing":[[int(Kpair[i,j]) for j in range(Kpair.shape[1])] for i in range(Kpair.shape[0])],
    "orthogonal_complement_determinant":int(Kpair.det()) if Kpair.shape[0] else 1,
    "rows_minimum_facts":rows,
    "warning":"Mixed-row parity/spin for r=2 and exact smooth diffeomorphism type are not determined by this script. Do not use the old step50_toric_fan_spin_probe determinant -1296; it came from substituting linear-equivalence representatives into a degenerate divisor pairing."
}
ws=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out_path=os.path.join(ws,"data","step50_mixed_resolution_lattice_probe.json")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
with open(out_path,"w") as f: json.dump(out,f,indent=2)
print(json.dumps({
    "smooth_fan":out["smooth_fan"],
    "picard_det":out["picard_determinant"],
    "picard_signature":out["picard_signature"],
    "exceptional_pairing":out["exceptional_pairing"],
    "rows":rows,
    "warning":out["warning"]
}, indent=2))
