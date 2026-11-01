"""
Step 18 (S0910A02): quick checker for characteristic sequences of T^2 actions
on polygonal orbit spaces.

For a characteristic sequence lambda_i in Z^2 with det(lambda_i,lambda_{i+1})=±1,
we solve for the degree-2 intersection form Q on divisor classes x_i using:
  * x_i x_j = 0 for non-adjacent facets;
  * int x_i x_{i+1} = 1/det(lambda_i,lambda_{i+1});
  * the two linear relations sum_i lambda_{a,i} x_i = 0 lie in the kernel.
Then we restrict Q to a rational basis for Z^m / span(lambda rows) and compute
rank/signature over Q.  This is only a topology sanity check; it does not prove
an Orlik-Raymond classification theorem and does not construct a metric.
"""
import json, math, os
import sympy as sp

ROOT = "Sessions/S0910A02"
OUT = os.path.join(ROOT, "workspace/data/step18_toric_topology_checker.json")

def det2(u,v):
    return int(u[0]*v[1]-u[1]*v[0])

def build_Q(lams):
    m=len(lams)
    Q=sp.zeros(m)
    # adjacent products
    for i in range(m):
        j=(i+1)%m
        d=det2(lams[i],lams[j])
        if abs(d)!=1:
            raise ValueError(f"non-unimodular adjacent pair {i},{j}: det={d}")
        Q[i,j]=Q[j,i]=sp.Rational(1,d)
    # solve self squares q_i from kernel equations lambda rows * Q = 0
    q=sp.symbols(f'q0:{m}')
    for i in range(m):
        Q[i,i]=q[i]
    eqs=[]
    for a in range(2):
        row=sp.Matrix([lams[i][a] for i in range(m)]).T
        prod=row*Q
        eqs += list(prod)
    sol=sp.solve(eqs, q, dict=True)
    if not sol:
        return None, "no solution for self intersections"
    if len(sol)>1:
        # should be unique modulo degenerate/pathological choices
        pass
    Q=Q.subs(sol[0])
    return sp.Matrix(Q), None

def quotient_basis(lams):
    m=len(lams)
    L=sp.Matrix([[lams[i][0] for i in range(m)], [lams[i][1] for i in range(m)]])
    # Nullspace of L gives representatives of quotient dual? We need a basis of a
    # complement to row space in Q^m. Use nullspace of L (vectors c with L c=0):
    # if y=sum c_i x_i, linear relations vanish. Dimension m-2.
    ns=L.nullspace()
    return ns

def signature_of(lams):
    Q, err=build_Q(lams)
    if err:
        return {"error": err}
    ns=quotient_basis(lams)
    B=sp.Matrix([[ (u.T*Q*v)[0] for v in ns] for u in ns])
    # Numerical eigenvalues for signature; exact rank via sympy.
    evals=[complex(ev) for ev in [e.evalf(30) for e in B.eigenvals().keys() for _ in range(B.eigenvals()[e])]]
    pos=sum(1 for z in evals if z.real>1e-9)
    neg=sum(1 for z in evals if z.real<-1e-9)
    zero=len(evals)-pos-neg
    return {
        "m": len(lams),
        "b2_expected": len(lams)-2,
        "adjacent_dets": [det2(lams[i], lams[(i+1)%len(lams)]) for i in range(len(lams))],
        "Q_divisors": [[str(Q[i,j]) for j in range(len(lams))] for i in range(len(lams))],
        "quotient_basis": [[str(x) for x in v] for v in ns],
        "intersection_matrix_on_nullspace_basis": [[str(B[i,j]) for j in range(B.cols)] for i in range(B.rows)],
        "rank": int(B.rank()),
        "signature": int(pos-neg),
        "pos": pos,
        "neg": neg,
        "zero": zero,
        "homeomorphism_sanity": "signature 0 and b2=2k are consistent with #_k(S2xS2) over Q; integral parity/unimodularity still needs checking"
    }

def seq_period(m):
    base=[(1,0),(0,1),(-1,0),(0,-1)]
    return [base[i%4] for i in range(m)]

def seq_zigzag(m):
    # A simple alternating determinant ±1 sequence that exists for every even m.
    # It is not guaranteed to represent #_k(S2xS2); used for comparison.
    return [(1,0),(0,1),(-1,0),(0,-1)] + [(1,0),(0,1)]*((m-4)//2)

reports={}
for m in [4,6,8,10,12]:
    reports[f"period_m{m}"]=signature_of(seq_period(m))

# Hand-search a few m=6 sequences with small primitive labels to see if signature 0 occurs.
prims=[]
for a in range(-2,3):
    for b in range(-2,3):
        if (a,b)!=(0,0) and math.gcd(a,b)==1:
            prims.append((a,b))

def canonical_cyclic(seq):
    # crude de-dup for reports
    return tuple(seq)

hits=[]
start=[(1,0),(0,1)]
# DFS length 6 with adjacent det ±1 and closing det ±1, bounded labels.
def dfs(seq, target=6):
    if len(seq)==target:
        if abs(det2(seq[-1], seq[0]))==1:
            rep=signature_of(seq)
            if rep.get("rank")==target-2 and rep.get("signature")==0:
                hits.append({"labels": seq.copy(), "adjacent_dets": rep["adjacent_dets"], "matrix": rep["intersection_matrix_on_nullspace_basis"]})
        return
    for v in prims:
        if abs(det2(seq[-1],v))==1:
            seq.append(v)
            dfs(seq,target)
            seq.pop()

dfs(start,6)
reports["m6_small_signature0_hits_first10"] = hits[:10]
reports["m6_small_signature0_hit_count"] = len(hits)

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT,'w') as f:
    json.dump(reports,f,indent=2)
print(json.dumps(reports, indent=2))
print("Saved", OUT)
