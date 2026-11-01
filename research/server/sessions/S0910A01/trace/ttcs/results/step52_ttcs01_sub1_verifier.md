# TTCS Independent Branch Record

```json
{
  "step_id": 52,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/scripts/step52_lefschetz_obstruction_dimensions.py",
    "Sessions/S0910A01/workspace/data/step52_lefschetz_obstruction_dimensions.json",
    "Sessions/S0910A01/workspace/notes/step52_lefschetz_product_quotient_obstruction_scan.md",
    "Sessions/S0910A01/workspace/notes/step51_reflexive_bridge_einstein_existence_proof.md",
    "Knowledge/objects/papers/Quotients-of-products-of-curves-new-surfaces-with-p-g-0-and-their-fundam--d97fcf2e6caa--2319c75d6a35/object.md"
  ]
}
```

## Task

Verify the Step 52 holomorphic Lefschetz computation and interpretation for BCGP product-quotient rows in the Yau 26 session. Please read the script, data, source excerpts, Step 51 proof note, and Step 52 note. Check: (i) the Lefschetz trace formulas and fixed-point/multiplier reconstruction from branch stabilizers; (ii) whether the tensor-character average correctly computes H^0(C1,2K)⊗H^0(C2,K) plus H^0(C1,K)⊗H^0(C2,2K) invariants; (iii) whether the numerical conclusions d=0 only for the K^2=2 Z4^2 row among the scanned BCGP rows are plausible from the supplied data; (iv) whether the interpretation is appropriately limited: d=0 supplies a sufficient global Q-Gorenstein smoothing route via Step 51, while d>0 is not a no-smoothing/no-Einstein theorem. Identify any load-bearing errors, convention risks, or source-assumption gaps that should be repaired before this result is used.

## Output

# Scientific memo: Step 52 holomorphic Lefschetz computation

## Overall assessment

The mathematical core of `step52_lefschetz_obstruction_dimensions.py` is correct under the standard interpretation of the BCGP spherical systems. The Lefschetz formulas, reconstruction of fixed points from inertia subgroups, tensor-character projection, and identification with the Step 51 obstruction group all fit together.

The supplied numerical table is internally coherent. Exact hand calculations reproduce:

- \(d=0\) for BCGP §6.7, \(G=\mathbb Z_4^2\);
- \(d=4\) for §6.18;
- \(d=6\) for §6.19;
- \(d=2\) for the first nonabelian test, §6.9 with \(G=S_5\).

Thus the reported statement is well supported for the 20 entries actually scanned: §6.7 and §§6.9–6.27. The seven section entries §§6.1–6.6 and §6.8, all with \(K^2=2\), are absent, so the result is not a computation of every BCGP \(K^2=2\) family.

Two items remain important for theorem-level use: the script does not directly verify that each branch tuple separately is a spherical generating system, and all character sums use floating-point roots of unity rather than exact cyclotomic arithmetic.

## 1. Lefschetz formulas

For a nonidentity finite-order automorphism \(u\) of a curve \(C\), with tangent multiplier \(\lambda_p\) at each fixed point, holomorphic Lefschetz gives
\[
\sum_q(-1)^q\operatorname{Tr}\bigl(u\mid H^q(C,L)\bigr)
=
\sum_{p\in\operatorname{Fix}(u)}
\frac{\operatorname{Tr}(u\mid L_p)}{1-\lambda_p}.
\]

For \(L=K_C\), pullback acts on \(K_{C,p}\) by \(\lambda_p\), while
\[
H^1(C,K_C)\cong H^0(C,\mathcal O_C)^\vee
\]
has trace \(1\). Hence
\[
\operatorname{Tr}(u\mid H^0(K_C))
=
1+\sum_p\frac{\lambda_p}{1-\lambda_p}.
\]

For \(L=2K_C\), \(H^1(C,2K_C)=0\) because \(g\ge2\), and the fiber action is \(\lambda_p^2\). Therefore
\[
\operatorname{Tr}(u\mid H^0(2K_C))
=
\sum_p\frac{\lambda_p^2}{1-\lambda_p}.
\]

At the identity, Riemann–Roch gives
\[
h^0(K_C)=g,\qquad h^0(2K_C)=3g-3.
\]

These are exactly the formulas implemented in `curve_traces`.

## 2. Reconstruction from branch stabilizers

Let \(C\to\mathbb P^1\) be a regular \(G\)-cover with branch element \(e_i\) of order \(r_i\), and let \(H_i=\langle e_i\rangle\). The points over the corresponding branch value are represented by cosets \(aH_i\). Under the left \(G\)-action,
\[
\operatorname{Stab}(aH_i)=aH_i a^{-1}.
\]
Thus \(u\) fixes \(aH_i\) precisely when
\[
a^{-1}ua=e_i^k\ne1.
\]
If \(e_i\) acts in a local coordinate by \(\zeta_{r_i}\), then \(u\) has tangent multiplier \(\zeta_{r_i}^k\) at that point. Replacing \(\zeta_{r_i}\) by its inverse corresponds to the alternate left/right monodromy convention.

The implementation follows this literally:

- `left_coset_reps(H)` enumerates \(aH\);
- `conjugate_by(a,u)` computes \(a^{-1}ua\);
- `power_index` recovers \(k\);
- the exponential produces \(\exp(\pm2\pi i k/r)\).

Every fixed point is counted exactly once. Repeated branch elements represent distinct branch values and are therefore correctly counted repeatedly.

The simultaneous sign reversal on both curves sends every character \(\chi(u)\) to \(\chi(u^{-1})\). The final group average is unchanged after the substitution \(u\mapsto u^{-1}\). Consequently, the `tangent_sign=-1` rerun confirms a mathematical invariance identity rather than supplying an independent numerical calculation. An opposite sign on only one factor could change the tensor multiplicity, so the common monodromy convention for the two BCGP covers is the relevant fact. Both branch systems are presented in the source under the same spherical-system convention.

## 3. Tensor-character average

Step 51 gives
\[
H^2(X,T_X^0)^\vee
\cong
H^0(Y,\Omega_Y^1\otimes K_Y)^G,
\qquad Y=C_1\times C_2.
\]
The product decomposition is
\[
H^0(Y,\Omega_Y^1\otimes K_Y)
=
H^0(2K_{C_1})\otimes H^0(K_{C_2})
\oplus
H^0(K_{C_1})\otimes H^0(2K_{C_2}).
\]

For a representation \(V\), the averaging operator
\[
P_G=\frac1{|G|}\sum_{u\in G}\rho_V(u)
\]
projects onto \(V^G\). Therefore
\[
\dim V^G=\frac1{|G|}\sum_{u\in G}\chi_V(u).
\]
Since the character of \(V\otimes W\) is \(\chi_V(u)\chi_W(u)\), the implemented expression
\[
d=\frac1{|G|}\sum_{u\in G}
\left[
\chi_{2K,C_1}(u)\chi_{K,C_2}(u)
+
\chi_{K,C_1}(u)\chi_{2K,C_2}(u)
\right]
\]
is correct. There should be no complex conjugation here: conjugation would compute a Hom-space multiplicity rather than invariants of the diagonal tensor product.

The use of the same concrete group element \(u\) in both branch systems is also correct because BCGP uses the diagonal action of one identified group \(G\), not an action \(u\) on one factor and \(u^{-1}\) on the other.

## 4. Numerical verification

### Abelian rows

The Fourier decompositions in the JSON permit exact integer comparisons.

For §6.7, the inverse characters needed to pair
\[
H^0(2K_{C_1})\quad\text{with}\quad H^0(K_{C_2})
\]
do not occur, and the same is true for the other summand. Hence
\[
d_{21}=d_{12}=0.
\]
This agrees with the independent Step 50/51 character calculation.

For §6.18:

- \(H^0(2K_{C_1})\) has exactly two character occurrences pairing with \(H^0(K_{C_2})\);
- \(H^0(K_{C_1})\) has exactly two pairing with \(H^0(2K_{C_2})\).

Thus
\[
d_{21}=2,\qquad d_{12}=2,\qquad d=4.
\]

For §6.19, every character is self-inverse. The relevant intersections each have multiplicity three:
\[
d_{21}=3,\qquad d_{12}=3,\qquad d=6.
\]

These reproduce the JSON without floating-point evaluation.

### Exact nonabelian test: §6.9, \(G=S_5\)

The source branch types are:

- \(C_1\): \((2),(4),(5)\), with genus \(4\);
- \(C_2\): \((3),(3,2),(3,2)\), with genus \(21\).

Classwise Lefschetz calculation gives the following pairs
\((\chi_K,\chi_{2K})\):

| conjugacy type | class size | \(C_1\) | \(C_2\) |
|---|---:|---:|---:|
| \(1\) | 1 | \((4,9)\) | \((21,60)\) |
| \((2)\) | 10 | \((-2,3)\) | \((-1,2)\) |
| \((2^2)\) | 15 | \((0,1)\) | \((1,0)\) |
| \((3)\) | 20 | \((1,0)\) | \((-3,0)\) |
| \((3,2)\) | 20 | \((1,0)\) | \((-1,-4)\) |
| \((4)\) | 30 | \((0,-1)\) | \((1,0)\) |
| \((5)\) | 24 | \((-1,-1)\) | \((1,0)\) |

Therefore
\[
\begin{aligned}
120\,d_{21}
&=9\cdot21
+10(3)(-1)
+15(1)(1)
+30(-1)(1)
+24(-1)(1)\\
&=120,
\end{aligned}
\]
and
\[
120\,d_{12}
=
4\cdot60+10(-2)(2)+20(1)(-4)=120.
\]
Thus
\[
d_{21}=1,\qquad d_{12}=1,\qquad d=2,
\]
exactly as reported.

### Remaining rows

The remaining values have strong internal support:

- every generated permutation group has the expected order;
- Riemann–Hurwitz reproduces the displayed genera;
- the averaged canonical character is numerically zero, as required by \(C_i/G\simeq\mathbb P^1\);
- all final averages lie within about \(10^{-15}\) of integers;
- the note and JSON agree row by row.

The embedded `expected_d` dictionary was evidently populated from the same numerical work. It protects against later code changes but is not independent mathematical evidence. Exact cyclotomic sums or a second classwise implementation would convert the full table into an exact finite computation.

## 5. Source assumptions not asserted by the script

The fixed-point construction presupposes that each branch list is a connected spherical system:

\[
\prod_i e_i=1,\qquad
\langle e_1,\ldots,e_r\rangle=G,
\qquad
\operatorname{ord}(e_i)=m_i.
\]

The BCGP §6 excerpts present the lists precisely as spherical generators, so the mathematics has source support. The script, however, constructs the permutation group from `S1 + S2`. It does not verify that `S1` and `S2` separately generate the full group, nor that each product is the identity. A transcription error preserving the union-generated group order could therefore pass the present tests.

The concrete missing software assertions are:

- product of each branch list equals the identity;
- subgroup generated by each branch list equals the stored group;
- each branch element has the source signature order.

The permutation parser is otherwise suitable for the displayed BCGP data: all multi-cycle strings used here consist of disjoint cycles, so its stated convention causes no ambiguity.

## 6. Interpretation through Step 51

The Step 51 bridge is mathematically sound:

1. \(T_X^0\) and \((\pi_*T_Y)^G\) are reflexive;
2. they agree on the étale locus;
3. the omitted set has codimension two;
4. finite pushforward and the Reynolds splitting give
   \[
   H^2(X,T_X^0)\cong H^2(Y,T_Y)^G.
   \]

Thus the computed number is
\[
d=\dim H^2(X,T_X^0).
\]

When \(d=0\), the Lee–Park globalization theorem quoted in Step 51 applies to the BCGP node surface: its singularities are \(A_1\) points, hence locally Q-Gorenstein smoothable, and vanishing of \(H^2(T_X^0)\) supplies the stated globalization mechanism. Since \(K_X\) is ample and remains ample on nearby smooth fibers, Aubin–Yau gives a metric satisfying \(\operatorname{Ric}=-h\). The ADE simultaneous-resolution argument then transfers such a metric to the underlying smooth manifold of the minimal resolution.

The exact Lee–Park proposition is not included among the supplied source excerpts. Consequently, the passage from cohomological vanishing to an actual disk family simultaneously smoothing every node rests on the quotation in Step 51. The theorem assumptions and its disk-level conclusion need the cited source passage attached to the final proof record.

For \(d>0\), the only conclusion is
\[
H^2(X,T_X^0)\ne0.
\]
This does not determine the local-to-global obstruction map
\[
H^0(\widetilde T_X^1)\longrightarrow H^2(T_X^0).
\]
Its kernel may still contain a vector whose node coordinates are all nonzero, and further deformation structure may still produce a simultaneous smoothing. Nor does \(d>0\) say anything decisive about Einstein metrics arising from another complex structure or by non-Kähler constructions. The Step 52 note states this distinction correctly.

## Final finding

No load-bearing mathematical error appears in the Lefschetz or tensor-character method. The reported pattern is credible and partly reproduced exactly:
\[
d=0\ \text{for §6.7},\qquad d>0\ \text{for every scanned \(K^2=4,6\) entry}.
\]

For rigorous reuse, the remaining scientific record consists of exact branch-system assertions, exact cyclotomic character sums for all rows, the explicit Lee–Park source passage, and wording that identifies the scanned set as §6.7 plus §§6.9–6.27 rather than all BCGP product-quotient families.