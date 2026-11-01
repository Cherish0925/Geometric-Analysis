"""
Step 45 spin-boundary sanity check.

For A1 resolutions, treat each RP^3 boundary as carrying two spin structures.
A spin orbifold quotient with four singular boundaries induces some boundary
spin data s_i in {0,1}; an EH filling in one orientation may extend one of
the two structures, while reversed orientation may extend the opposite or the
same depending on the actual lift/framing.  The key point is logical: local
spinness of each piece is insufficient; global spin requires boundary matching
at every component.  If all orientation choices extended automatically, every
r-resolution would be spin.  But any closed smooth spin 4-manifold has signature
0 mod 16 (Rokhlin), which fails for r=0,1,3,4 in the Z2 table.  Hence at least
some boundary matching changes with orientation/lift and Step44's parity claim
cannot be inferred without explicit spin/Kirby data.
"""
import json, os
script_dir=os.path.dirname(os.path.abspath(__file__))
ws=os.path.dirname(script_dir)
out=os.path.join(ws,"data","step45_spin_boundary_sanity.json")

rows=[]
for r in range(5):
    bp=1+r
    bm=1+(4-r)
    tau=bp-bm
    rok_spin_allowed=(tau % 16)==0
    even_unimodular_possible=(tau % 8)==0  # lattice necessary in topological category
    stress=(bp==bm)
    rows.append({
        "r_reversed": r,
        "b_plus": bp,
        "b_minus": bm,
        "signature": tau,
        "spin_allowed_by_Rokhlin": rok_spin_allowed,
        "even_unimodular_lattice_possible": even_unimodular_possible,
        "balanced_stress_rational_data": stress,
        "consequence": "parity still must be proved" if stress else "cannot all be spin; naive all-pieces-spin argument fails"
    })

result={
    "purpose":"Logical audit of Step44 spin claim; not a full spin computation.",
    "boundary_spin_fact":"RP^3 has two spin structures; a spin filling extends only selected boundary data. Gluing spin pieces requires matching spin structures on each boundary component.",
    "Z2_resolution_rows":rows,
    "main_conclusion":"The assertion that the balanced r=2 resolution has form 3H requires an explicit parity/spin proof. Step44's argument from local liftability of -I4 and spinness of EH would incorrectly make all r spin, impossible by Rokhlin for nonzero-signature rows. Current rigorous topology: pi1=0 and b+=b-=3 for r=2; form is 3H only if evenness is separately established."
}
with open(out,'w') as f: json.dump(result,f,indent=2)
print(json.dumps({"output":out,"main_conclusion":result["main_conclusion"],"rows":rows},indent=2))
