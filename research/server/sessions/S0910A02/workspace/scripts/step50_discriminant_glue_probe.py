"""
Step 50 discriminant-form probe for mixed-sign replacements of the four A1
curves in the all-compatible toric resolution of (S2 x S2)/Z2.

Input lattice: the corrected Picard intersection matrix from
step50_mixed_resolution_lattice_probe.json, with four disjoint (-2) classes E_i.
We compute the finite gluing subgroup H = L/(K + A) inside the discriminant group
of K+A, where K is the orthogonal complement of the E_i and A=<E_i>.
Then we keep the same fractional boundary classes and flip the signs of selected
A_i from -2 to +2. This is a model for preserving the same RP3 boundary glue
while reversing EH chirality. If the resulting overlattice is integral and
unimodular, we record its parity/signature. If not, this warns that a full
boundary/Kirby calculation is needed; the probe does not prove impossibility.
"""
import json, os, itertools
import sympy as sp

ws=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
base_path=os.path.join(ws,"data","step50_mixed_resolution_lattice_probe.json")
with open(base_path) as f: base=json.load(f)
Q=sp.Matrix(base["picard_intersection_matrix"])
K_cols=[sp.Matrix(v) for v in base["orthogonal_complement_integer_basis"]]
E_cols=[sp.Matrix(v) for v in base["exceptional_vectors_in_picard_basis"].values()]
B=sp.Matrix.hstack(*(K_cols+E_cols))
S_Q=B.T*Q*B
Binv=B.inv()
# H generators: coordinates of each Picard basis vector in the S-basis, modulo Z.
Hgens=[]
for j in range(6):
    coords=Binv*sp.eye(6).col(j)
    frac=sp.Matrix([sp.Rational(c) - sp.floor(c) for c in coords])
    if any(c != 0 for c in frac):
        Hgens.append(frac)
# generate subgroup over denominators (empirically 2-torsion here)
def mod1_vec(v):
    return tuple(sp.Rational(x) - sp.floor(sp.Rational(x)) for x in list(v))
H=set([tuple([sp.Rational(0)]*6)])
for coeffs in itertools.product([0,1], repeat=len(Hgens)):
    v=sp.zeros(6,1)
    for c,g in zip(coeffs,Hgens):
        if c: v += g
    H.add(mod1_vec(v))
# reduce to actual generated set (some gens redundant)
Hlist=[sp.Matrix(h) for h in sorted(H, key=lambda x: tuple(float(y) for y in x))]

def bilinear_integral(M, gens):
    # Generated lattice S + H. Check pairings among H are integral; H already in S^* if coords valid.
    vals=[]
    ok=True
    for i,u in enumerate(gens):
        for j,v in enumerate(gens[:i+1]):
            val=(u.T*M*v)[0]
            vals.append(str(val))
            if val.q != 1: ok=False
    return ok, vals

def overlattice_matrix(M, Hgens_basis):
    # Pick independent fractional generators to form a basis together with enough S vectors.
    # For the known all-compatible case, easier: enumerate all vectors in S+H with small coeffs
    # and compute determinant/parity from a found Z-basis using Hermite normal form is nontrivial.
    pass

def signature_numeric(M):
    vals=[complex(v) for v in M.evalf().eigenvals().keys() for _ in range(M.evalf().eigenvals()[v])]
    return [sum(1 for z in vals if z.real>1e-8), sum(1 for z in vals if z.real<-1e-8)]

rows=[]
for reversed_set in itertools.chain.from_iterable(itertools.combinations(range(4), r) for r in range(5)):
    signs=[1 if i in reversed_set else -1 for i in range(4)]  # A_i square = 2*sign
    K_Q=S_Q[:2,:2]
    # K-A cross terms are zero in this basis by construction; A block flips signs.
    M=sp.zeros(6)
    M[:2,:2]=K_Q
    for i,s in enumerate(signs):
        M[2+i,2+i]=2*s
    ok, vals=bilinear_integral(M,Hlist)
    # If same H is integral, parity can be checked on all cosets h in H: vector norm hMh mod 2.
    even=True
    norms=[]
    if ok:
        for h in Hlist:
            norm=(h.T*M*h)[0]
            norms.append(str(norm))
            if (norm/2).q != 1:  # norm not an even integer for h; S generators all even in the K+A basis
                even=False
    else:
        even=None
    r=len(reversed_set)
    rows.append({
        "reversed_set": list(reversed_set),
        "r": r,
        "same_glue_integral": ok,
        "coset_norms_if_integral": norms,
        "same_glue_even": even,
        "rational_signature_expected": [1+r,5-r],
        "comment": "same discriminant glue model only; actual RP3 boundary gluing may differ" if ok else "same fractional glue not integral after sign flip; need full boundary/Kirby data"
    })

out={
    "purpose":"Probe whether the all-compatible discriminant gluing forces parity for mixed sign replacements.",
    "S_intersection_K_plus_A":[[int(S_Q[i,j]) for j in range(6)] for i in range(6)],
    "index_of_K_plus_A_in_all_compatible_L": abs(int(B.det())),
    "H_size": len(Hlist),
    "H_fractional_classes":[[str(x) for x in list(h)] for h in Hlist],
    "all_compatible_integrality_check": bilinear_integral(S_Q,Hlist)[0],
    "rows": rows,
    "conclusion":"The same-fractional-glue probe is only a model. It checks whether the all-compatible overlattice glue can be reused after sign flips. If it fails or gives multiple parity possibilities, Step50 should continue to record r=2 spin as unproved rather than asserting #3(S2xS2)."
}
out_path=os.path.join(ws,"data","step50_discriminant_glue_probe.json")
with open(out_path,"w") as f: json.dump(out,f,indent=2)
print(json.dumps({
    "index": out["index_of_K_plus_A_in_all_compatible_L"],
    "H_size": out["H_size"],
    "rows_summary":[{k:row[k] for k in ["reversed_set","r","same_glue_integral","same_glue_even","comment"]} for row in rows]
}, indent=2))
