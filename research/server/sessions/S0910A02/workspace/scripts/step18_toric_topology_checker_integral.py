"""
Step 18 (S0910A02): integral quotient-basis topology checker for labeled
T^2 polygon characteristic sequences.

Input labels lambda_i in Z^2 with adjacent determinants ±1.  Use the standard
quasitoric/toric cohomology presentation.  For an omniorientation with adjacent
intersection int(x_i x_{i+1}) = 1/det(lambda_i,lambda_{i+1}) and nonadjacent
products zero, determine self-products by imposing that the two linear relations
R_a=sum_i lambda_i[a] x_i pair trivially with all x_j.  Then eliminate a
unimodular pair of variables using the two relations to get an integral quotient
basis and compute its intersection matrix.

This is a sanity checker for candidate #_k(S2xS2) rod label families, not a
replacement for a sourced Orlik-Raymond proof or a smooth metric construction.
"""
import json, math, os
import sympy as sp

ROOT = "Sessions/S0910A02"
OUT = os.path.join(ROOT, "workspace/data/step18_toric_topology_checker_integral.json")

def det2(u,v):
    return int(u[0]*v[1]-u[1]*v[0])

def build_Q(lams):
    m=len(lams)
    Q=sp.zeros(m)
    for i in range(m):
        j=(i+1)%m
        d=det2(lams[i],lams[j])
        if abs(d)!=1:
            raise ValueError(f"non-unimodular adjacent pair {i},{j}: det={d}")
        Q[i,j]=Q[j,i]=sp.Rational(1,d)
    q=sp.symbols(f'q0:{m}')
    for i in range(m): Q[i,i]=q[i]
    eqs=[]
    for a in range(2):
        row=sp.Matrix([lams[i][a] for i in range(m)]).T
        eqs += list(row*Q)
    sol=sp.solve(eqs, q, dict=True)
    if not sol: raise ValueError("no self-intersection solution")
    return sp.Matrix(Q.subs(sol[0]))

def eliminate_pair_matrix(lams, pair=None):
    m=len(lams)
    if pair is None:
        pair=None
        for i in range(m):
            for j in range(i+1,m):
                if abs(det2(lams[i],lams[j]))==1:
                    pair=(i,j); break
            if pair: break
    i,j=pair
    A=sp.Matrix([[lams[i][0], lams[j][0]],[lams[i][1], lams[j][1]]])
    if abs(int(A.det()))!=1:
        raise ValueError("chosen pair not unimodular")
    free=[r for r in range(m) if r not in pair]
    # The free degree-2 generators are the original divisor classes x_f for
    # f in free.  Eliminating x_i,x_j expresses non-free variables in terms of
    # these generators, but it does NOT mean that the generator x_f is the sum
    # of all its equivalent representatives.  Thus the intersection matrix of
    # the chosen free basis is the solved Q restricted to the free indices.
    # We still return the elimination matrix for audit/debugging.
    inv=A.inv()
    subst=sp.zeros(m,len(free))
    for col,f in enumerate(free):
        subst[f,col]=1
        coeff=-inv*sp.Matrix([lams[f][0], lams[f][1]])
        subst[i,col]=sp.simplify(coeff[0])
        subst[j,col]=sp.simplify(coeff[1])
    return subst, free, pair

def parity(B):
    return all(int(B[i,i])%2==0 for i in range(B.rows))

def det_abs(B):
    return abs(int(sp.Matrix(B).det())) if B.rows>0 else 1

def diag_signature(B):
    # Use symmetric numerical inertia rather than symbolic roots.  SymPy may
    # represent exact eigenvalues of an indefinite integer matrix by complex
    # radicals even when the final values are real.
    import numpy as np
    A=np.array([[float(sp.N(B[i,j],30)) for j in range(B.cols)] for i in range(B.rows)], dtype=float)
    A=(A+A.T)/2.0
    vals=np.linalg.eigvalsh(A)
    pos=int(np.sum(vals>1e-8))
    neg=int(np.sum(vals<-1e-8))
    zero=int(len(vals)-pos-neg)
    return pos,neg,zero

def report(lams, name):
    Q=build_Q(lams)
    P,free,pair=eliminate_pair_matrix(lams)
    B=sp.Matrix([[Q[i,j] for j in free] for i in free])
    pos,neg,zero=diag_signature(B)
    m=len(lams)
    b2=m-2
    topo=[]
    if B.rank()==b2 and det_abs(B)==1 and pos==neg and parity(B):
        topo.append(f"even unimodular indefinite rank {b2}, signature 0: consistent with #{b2//2}(S2xS2)")
    if B.rank()==b2 and det_abs(B)==1 and not parity(B):
        topo.append("odd unimodular form: connected sum of CP2 and CPbar pieces rather than pure S2xS2")
    return {
        "name": name,
        "labels": [list(v) for v in lams],
        "m": m,
        "b2": b2,
        "adjacent_dets": [det2(lams[i],lams[(i+1)%m]) for i in range(m)],
        "eliminated_pair": pair,
        "free_indices_basis": free,
        "intersection_matrix_integral_basis": [[str(B[i,j]) for j in range(B.cols)] for i in range(B.rows)],
        "rank": int(B.rank()),
        "det_abs": det_abs(B),
        "parity_even": parity(B),
        "pos": pos,
        "neg": neg,
        "zero": zero,
        "signature": pos-neg,
        "topology_sanity": topo or ["not identified as #k(S2xS2) by this coarse form test"]
    }

def seq_period(m):
    base=[(1,0),(0,1),(-1,0),(0,-1)]
    return [base[i%4] for i in range(m)]

# A blow-up style sequence in fans: insert sums of adjacent vectors.  Starting
# from square (1,0),(0,1),(-1,0),(0,-1), repeated corner blowups produce odd
# forms, included as a check that the code can distinguish them.
def blowup_square(num):
    seq=[(1,0),(0,1),(-1,0),(0,-1)]
    for _ in range(num):
        # blow up the first corner by inserting v_i+v_{i+1}
        v=(seq[0][0]+seq[1][0], seq[0][1]+seq[1][1])
        seq.insert(1,v)
    return seq

reports={}
for m in [4,6,8,10,12]:
    reports[f"period_m{m}"]=report(seq_period(m), f"period_m{m}")
for b in [1,2,3,4]:
    reports[f"blowup_square_{b}"]=report(blowup_square(b), f"blowup_square_{b}")

# Search small m=6 sequences whose integral intersection form is even unimodular signature 0.
prims=[]
for a in range(-2,3):
    for b in range(-2,3):
        if (a,b)!=(0,0) and math.gcd(a,b)==1:
            prims.append((a,b))
hits=[]
def dfs(seq,target=6):
    if len(seq)==target:
        if abs(det2(seq[-1],seq[0]))==1:
            try:
                rep=report(seq,"hit")
            except Exception:
                return
            if rep["rank"]==target-2 and rep["det_abs"]==1 and rep["parity_even"] and rep["signature"]==0:
                hits.append({"labels":rep["labels"],"adjacent_dets":rep["adjacent_dets"],"matrix":rep["intersection_matrix_integral_basis"]})
        return
    for v in prims:
        if abs(det2(seq[-1],v))==1:
            seq.append(v); dfs(seq,target); seq.pop()

dfs([(1,0),(0,1)],6)
reports["m6_even_unimodular_signature0_hit_count"]=len(hits)
reports["m6_even_unimodular_signature0_hits_first5"]=hits[:5]

os.makedirs(os.path.dirname(OUT),exist_ok=True)
with open(OUT,'w') as f: json.dump(reports,f,indent=2)
print(json.dumps(reports,indent=2))
print("Saved",OUT)
