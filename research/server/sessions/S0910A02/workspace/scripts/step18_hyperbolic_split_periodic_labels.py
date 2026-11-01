"""
Step 18 (S0910A02): explicitly split the periodic-label intersection forms
as sums of hyperbolic planes H=[[0,1],[1,0]].

This strengthens the topology sanity check for the characteristic sequence
(1,0),(0,1),(-1,0),(0,-1),... on m=2k+2 facets.
"""
import json, os, sympy as sp

ROOT="Sessions/S0910A02"
OUT=os.path.join(ROOT,"workspace/data/step18_hyperbolic_split_periodic_labels.json")

def det2(u,v): return int(u[0]*v[1]-u[1]*v[0])

def labels(m):
    base=[(1,0),(0,1),(-1,0),(0,-1)]
    return [base[i%4] for i in range(m)]

def build_Q(lams):
    m=len(lams); Q=sp.zeros(m)
    for i in range(m):
        j=(i+1)%m; d=det2(lams[i],lams[j])
        if abs(d)!=1: raise ValueError((i,j,d))
        Q[i,j]=Q[j,i]=sp.Rational(1,d)
    q=sp.symbols(f'q0:{m}')
    for i in range(m): Q[i,i]=q[i]
    eqs=[]
    for a in range(2):
        row=sp.Matrix([lams[i][a] for i in range(m)]).T
        eqs+=list(row*Q)
    sol=sp.solve(eqs,q,dict=True)[0]
    return sp.Matrix(Q.subs(sol))

def form_for_period(m):
    lams=labels(m); Q=build_Q(lams)
    # eliminate x0,x1; free basis x2,...,x_{m-1}
    free=list(range(2,m))
    return sp.Matrix([[Q[i,j] for j in free] for i in free])

def split_hyperbolic(B):
    B=sp.Matrix(B)
    n=B.rows
    T=sp.eye(n)  # current basis vectors as columns in original basis
    pieces=[]
    active=list(range(n))
    current=B.copy()
    # Rather than mutate submatrices with bookkeeping complexity, maintain basis vectors.
    basis=[sp.eye(n).col(i) for i in range(n)]
    while len(basis)>0:
        r=len(basis)
        M=sp.Matrix([[ (basis[i].T*B*basis[j])[0] for j in range(r)] for i in range(r)])
        found=None
        for i in range(r):
            if M[i,i]!=0: continue
            for j in range(i+1,r):
                if M[j,j]==0 and abs(int(M[i,j]))==1:
                    found=(i,j,int(M[i,j])); break
            if found: break
        if found is None:
            raise ValueError(f"no obvious hyperbolic pair; remaining form {M}")
        i,j,s=found
        u=basis[i]
        v=basis[j] if s==1 else -basis[j]
        # Orthogonalize all other basis vectors against u,v.
        newbasis=[]
        for k,b in enumerate(basis):
            if k in (i,j): continue
            bu=(b.T*B*u)[0]
            bv=(b.T*B*v)[0]
            # b' = b - bv*u - bu*v makes <b',u>=<b',v>=0 when <u,v>=1.
            bp=sp.simplify(b - bv*u - bu*v)
            newbasis.append(bp)
        pieces.append({"u":[int(x) for x in list(u)],"v":[int(x) for x in list(v)]})
        basis=newbasis
    Ucols=[]
    for pair in pieces:
        Ucols.append(sp.Matrix(pair["u"])); Ucols.append(sp.Matrix(pair["v"]))
    U=sp.Matrix.hstack(*Ucols) if Ucols else sp.zeros(n)
    H=sp.zeros(n)
    for a in range(0,n,2):
        H[a,a+1]=H[a+1,a]=1
    check=sp.simplify(U.T*B*U-H)
    return pieces, [[str(U[i,j]) for j in range(U.cols)] for i in range(U.rows)], check

reports={}
for m in [4,6,8,10,12,14]:
    B=form_for_period(m)
    pieces,U,check=split_hyperbolic(B)
    reports[f"m{m}"]={
        "k":(m-2)//2,
        "intersection_matrix":[[str(B[i,j]) for j in range(B.cols)] for i in range(B.rows)],
        "hyperbolic_pairs":pieces,
        "congruence_matrix_columns_pairs_uv":U,
        "check_UtBU_minus_kH_zero": check==sp.zeros(B.rows),
        "det_U_abs": abs(int(sp.Matrix([[int(x) for x in row] for row in U]).det())) if B.rows>0 else 1
    }

os.makedirs(os.path.dirname(OUT),exist_ok=True)
with open(OUT,'w') as f: json.dump(reports,f,indent=2)
print(json.dumps(reports,indent=2))
print("Saved",OUT)
