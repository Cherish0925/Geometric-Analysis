"""
Step 81: exact combinatorial decomposition of the candidate radial B coefficients
for the A+J+L-symmetric diagonal mixed row of (S^2 x S^2)/<sigma>.

This does NOT compute analytic Green coefficients.  It prevents a common error:
for the opposite-corner spin row, the two A-orbits are the diagonal nodes and
the off-diagonal nodes.  Cross-orbit pairs are all adjacent (differ in one
S^2 factor); same-orbit companion pairs are diagonal and same-chirality.

For a single representative receiver in orbit i:
  F_i = t_i[(local_i + same_orbit_companion_i)*t_i^2
            + (sum over two cross-orbit sources)*t_j^2] + ...
A and L reduce these to two coefficient classes in transported normalization.
"""
import json
from collections import Counter

# N=+1, S=-1, nodes in order used in prior steps
nodes = [(1,1), (1,-1), (-1,1), (-1,-1)]
node_names = {(1,1):"NN", (1,-1):"NS", (-1,1):"SN", (-1,-1):"SS"}

def name(n): return node_names[n]
def A(n): return (-n[0], -n[1])
def L(n): return (-n[0], n[1])
def chir(n): return n[0]*n[1]
def orbit(n): return 1 if chir(n)==1 else 2

def geom(p,q):
    d = (p[0]!=q[0]) + (p[1]!=q[1])
    if d==0: return "local"
    if d==1: return "adjacent"
    return "diagonal"

def relation_to_receiver(receiver, source):
    if source == receiver:
        return "local_self"
    if orbit(source) == orbit(receiver):
        return "same_orbit_companion"
    return "cross_orbit"

# Build representative equations for NN (orbit1) and NS (orbit2).  A exchanges
# NN<->SS and NS<->SN, so these representatives suffice.
representatives = {1:(1,1), 2:(1,-1)}
reports = {}
for o, r in representatives.items():
    terms=[]
    for s in nodes:
        terms.append({
            "receiver": name(r),
            "source": name(s),
            "receiver_orbit": orbit(r),
            "source_orbit": orbit(s),
            "receiver_chirality": chir(r),
            "source_chirality": chir(s),
            "relation": relation_to_receiver(r,s),
            "geometry": geom(r,s),
            "same_chirality": chir(r)==chir(s),
            "candidate_scale_factor": f"t{o}*t{orbit(s)}^2",
            "leading_kernel_block_expectation": (
                "local higher radial self-response after mu1=0" if s==r else
                "same-chirality regular H4 response: leading chirality-split kernel block expected zero; keep possible higher/gauge contribution" if orbit(s)==o else
                "opposite-chirality adjacent Green response: leading cross coefficient class C_adj"
            )
        })
    reports[f"orbit{o}_representative_{name(r)}"] = terms

# Count coefficient classes per representative equation.
class_counts={}
for key, terms in reports.items():
    cnt=Counter()
    for term in terms:
        if term["relation"]=="local_self":
            cnt["local_self"] += 1
        elif term["relation"]=="same_orbit_companion":
            cnt[f"same_orbit_{term['geometry']}_{'samechir' if term['same_chirality'] else 'oppchir'}"] += 1
        else:
            cnt[f"cross_orbit_{term['geometry']}_{'samechir' if term['same_chirality'] else 'oppchir'}"] += 1
    class_counts[key]=dict(cnt)

# Symbolic decomposition in single-representative normalization.
# Let s = local self coefficient; d = same-orbit diagonal same-chirality coefficient;
# c = opposite-chirality adjacent cross coefficient for one source.
# Then each representative sees one local self, one same-orbit diagonal source,
# and two adjacent opposite-orbit sources.
decomposition = {
    "single_representative_normalization": {
        "F1": "t1*((s+d)*t1^2 + 2*c*t2^2) + higher/log terms",
        "F2": "t2*(2*c*t1^2 + (s+d)*t2^2) + higher/log terms",
        "a": "s+d (where d may vanish at the leading chirality-split Green block, but is retained until the full projected expansion proves it)",
        "b": "2*c (two adjacent opposite-chirality sources for each representative receiver)"
    },
    "orbit_sum_normalization": {
        "F1_sum": "2*t1*((s+d)*t1^2 + 2*c*t2^2) + ...",
        "F2_sum": "2*t2*(2*c*t1^2 + (s+d)*t2^2) + ...",
        "note": "Orbit averaging removes the common factor 2 and returns the single-representative form."
    },
    "important_correction": "For the opposite-corner/diagonal spin row, cross-orbit mixed-chirality pairs are adjacent, not diagonal. The diagonal geometry appears in same-orbit companion pairs with the same chirality, whose leading kernel-block shift is expected to vanish by the chirality split but must remain tracked for higher/gauge terms."
}

# Symmetry checks under L and A for term classes.
transport_checks=[]
for r in nodes:
    for s in nodes:
        term=(orbit(r), relation_to_receiver(r,s), geom(r,s), chir(r)==chir(s))
        Lterm=(orbit(L(r)), relation_to_receiver(L(r),L(s)), geom(L(r),L(s)), chir(L(r))==chir(L(s)))
        Aterm=(orbit(A(r)), relation_to_receiver(A(r),A(s)), geom(A(r),A(s)), chir(A(r))==chir(A(s)))
        transport_checks.append({
            "receiver_source": [name(r), name(s)],
            "term": term,
            "L_receiver_source": [name(L(r)), name(L(s))],
            "L_term": Lterm,
            "A_receiver_source": [name(A(r)), name(A(s))],
            "A_term": Aterm,
            "L_preserves_class_after_orbit_exchange": term[1:]==Lterm[1:],
            "A_preserves_class_within_orbit": term==Aterm
        })

results={
    "step":81,
    "purpose":"combinatorial decomposition of the candidate radial B matrix for the A+J+L diagonal mixed row",
    "nodes":[{"node":name(n),"orbit":orbit(n),"chirality":chir(n),"A":name(A(n)),"L":name(L(n))} for n in nodes],
    "representative_term_reports":reports,
    "class_counts_per_representative":class_counts,
    "decomposition":decomposition,
    "symmetry_checks":{
        "all_L_preserve_classes_after_orbit_exchange": all(t["L_preserves_class_after_orbit_exchange"] for t in transport_checks),
        "all_A_preserve_classes_within_orbit": all(t["A_preserves_class_within_orbit"] for t in transport_checks),
        "examples": transport_checks[:8]
    },
    "candidate_B_form":"[[a,b],[b,a]] with a=s+d, b=2c in single-representative/averaged orbit normalization",
    "positive_kernel_condition":"a+b=0; if a=-b!=0 then t1/t2 -> 1; if a=b=0 compute next layer",
    "status":"coefficient architecture only; analytic values s,d,c require the full projected expansion and Green/self-response computation"
}

print(json.dumps(results, indent=2))
out="Sessions/S0910A01/workspace/data/step81_radial_B_combinatorics.json"
with open(out,"w") as f:
    json.dump(results,f,indent=2)
print(f"\nWrote {out}")
