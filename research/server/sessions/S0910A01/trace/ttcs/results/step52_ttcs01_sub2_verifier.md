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

## Verification memo — Step 52 holomorphic Lefschetz obstruction scan

Overall the computation rests on correct trace formulas, a correct fixed-point reconstruction, and a correct invariant-dimension identity, and its central number ($d=0$ only for the $K^2=2$, $\mathbb Z_4^2$ row) is corroborated where an independent computation exists. The interpretation is stated at the right strength. The points that genuinely carry weight and deserve attention are the rotation-number normalization for the nonabelian rows, the fact that `expected_d` is a self-assertion rather than a check, and the reliance of the identification $d=h^2(X,T_X^0)$ on the Step 51 bridge.

### (i) Trace formulas and fixed-point/multiplier reconstruction — correct

The two formulas are the Atiyah–Bott holomorphic Lefschetz numbers for $L=K_C$ and $L=2K_C$. For $L=K_C$, at a fixed point the fiber map is multiplication by the tangent multiplier $\lambda_p$ and $\det(1-d\sigma_p)=1-\lambda_p$; since $\sigma$ acts trivially on $H^1(K_C)\cong H^0(\mathcal O_C)^\vee$ (trace $1$), one gets
$$\operatorname{Tr}(u\mid H^0(K_C))=1+\sum_p\frac{\lambda_p}{1-\lambda_p}.$$
This is exactly the script's formula, and it passes a decisive test: the hyperelliptic involution on genus $g$ has $2g+2$ fixed points with $\lambda=-1$, giving $1+(2g+2)(-\tfrac12)=-g$, matching the known fact that the hyperelliptic involution acts by $-1$ on $H^0(K)$. For $L=2K_C$ the fiber map is $\lambda_p^2$, $H^1(2K_C)=0$ for $g\ge2$, so $\operatorname{Tr}(u\mid H^0(2K_C))=\sum_p \lambda_p^2/(1-\lambda_p)$, with identity value $3g-3$. Both identity values ($g$, $3g-3$) are correct.

The fixed-point enumeration is right. Points over the $i$-th branch point form $G/\langle e_i\rangle$; the point $a\langle e_i\rangle$ has stabilizer $a\langle e_i\rangle a^{-1}$, so $u$ fixes it iff $a^{-1}ua=e_i^{k}\in\langle e_i\rangle$. The code uses one left-coset representative per point and tests `conjugate_by(a,u)`$=a^{-1}ua$, and the rotation number of $u=ae_i^{k}a^{-1}$ at that point is $\zeta_r^{k}$ (conjugation preserves the tangent character). For abelian $G$ every point over $p_i$ carries the same stabilizer and the code correctly reproduces the $|G|/r$ fixed points with a common multiplier. The Riemann–Hurwitz genus test and the $\tfrac1{|G|}\sum_u\operatorname{Tr}(u\mid H^0(K))=g(C/G)=0$ test (asserted to $2\times10^{-6}$) are genuine consistency conditions on the whole fixed-point/multiplier structure and pass; these are the strongest in-script mathematical guards.

### (ii) The tensor-character average is the right object

For a $G$-representation $A\otimes B$ under the diagonal action, $\dim(A\otimes B)^G=\tfrac1{|G|}\sum_u\chi_A(u)\chi_B(u)$ — an ordinary product of characters, no conjugation. The script computes exactly $\tfrac1{|G|}\sum_u\chi_{2K,C_1}(u)\chi_{K,C_2}(u)+\tfrac1{|G|}\sum_u\chi_{K,C_1}(u)\chi_{2K,C_2}(u)$, which is $\dim(H^0(2K_1)\otimes H^0(K_2))^G+\dim(H^0(K_1)\otimes H^0(2K_2))^G$, i.e. Step 51's Künneth decomposition of $H^0(Y,\Omega^1_Y\otimes K_Y)^G$. Correctness requires the same multiplier convention on both curves; the code uses one `tangent_sign` for both, so the product is the true invariant count and not a $\operatorname{Hom}_G$ dimension. The re-run with the opposite exponent (`res_dual`) tests the physically meaningful invariance: dualizing every character preserves invariant dimensions. This is the appropriate consistency test and it passes on every row.

### (iii) Numerical conclusion is plausible and cross-checked where possible

The one fully independent confirmation is the $K^2=2$, $\mathbb Z_4^2$ row: the Lefschetz Fourier inversion in `step52…json` (C1_K $=(2,3),(3,0),(3,1)$; C1_2K $=(0,2),(1,0),(1,3),(2,0),(2,1),(2,2)$; and the $C_2$ analogues) reproduces exactly the character tables that Step 51 obtained by an entirely different route (explicit abelian Chevalley–Weil plus the $\operatorname{Sym}^2 H^0(K)\xrightarrow{\sim}H^0(2K)$ map), and both give $d=0$. Since Step 52 does not use the $\operatorname{Sym}^2$ shortcut, this both validates Step 51 and removes the non-hyperelliptic hypothesis that shortcut needed — genuinely valuable, because rows 6.18/6.19 are hyperelliptic or all-order-two and the shortcut is unavailable there. The complex parts of all totals are $\sim10^{-16}$, reals are clean integers, and integrality is asserted. So $d=0$ being special to the $\mathbb Z_4^2$ row among the scanned entries is well supported by the supplied evidence.

Two points about what the numbers are: the dictionary `expected_d` with `assert res == expected_d[...]` is a regression fixture, not an independent verification — the note says as much. The real verification content is genus/order/`avgK`=0/integrality/dualization plus the Step 51 abelian match.

### (iv) Interpretation is at the right strength

The note states $d=0$ gives, via the Step 51 reflexive bridge and Lee–Park Prop 2.4(2), unobstructed globalization of local $A_1$ smoothings, hence a simultaneous $\mathbb Q$-Gorenstein smoothing, ampleness persistence, an Aubin–Yau metric with $\operatorname{Ric}_h=-h$, and diffeomorphism to the minimal resolution — a correct sufficient mechanism. For $d>0$ it says only that this sufficient vanishing route is unavailable; the local-to-global deformation image may still meet the all-nodes-nonzero locus, and another complex structure or a non-Kähler Einstein metric could exist. This does not assert non-existence of a smoothing or of an Einstein metric, and it correctly notes that the Ricci-pinching Yau-26 proposition is untouched. The identification $d=h^2(X,T_X^0)$ is valid for all scanned rows because BCGP Prop 5.2/Cor 5.4 force only $A_1$ nodes ($t=8-K^2$), so the Step 51 chain $T_X^0\cong(\pi_*T_Y)^G$, $H^2(X,T_X^0)\cong H^2(Y,T_Y)^G\cong (H^0(\Omega^1_Y\otimes K_Y)^G)^\vee$ (used only finiteness of $G$, codimension-two singular locus, reflexivity, and equivariant Serre duality) transfers unchanged.

### Points to settle before this is used further

1. **Rotation-number normalization for the nonabelian rows.** The invariant dimension $d$ is sensitive to the actual local rotation numbers, not just the conjugacy class of each branch element: the code assumes each BCGP branch element $e_i$ acts as the primitive $\exp(2\pi i/r_i)$ at its fixed point, and multipliers of $u=ae_i^k a^{-1}$ are $\exp(\pm2\pi i k/r_i)$. This is BCGP's spherical-generator convention and is confirmed for the three abelian rows by the Step 51 character match. The `tangent_sign` test only probes $\lambda\to\lambda^{-1}$, and `avgK`$=0$ can hold under a self-consistent but mis-normalized rotation assignment, so for the eight nonabelian rows this normalization currently rests on trusting the source convention with no independent confirmation in the supplied material. An inexpensive confirmation would be a second, representation-theoretic computation of one nonabelian $H^0(2K)$ character (e.g. the $A_5$ or $\mathrm{PSL}(2,7)$ row) from an ordinary character table, compared against the Lefschetz output.

2. **The product-one/spherical condition is not enforced in-script.** `curve_traces` uses only the branch multiset and orders; it never checks $\prod_i e_i=1$ or that the tuple is a genuine spherical system. The genus (RH) and $H^0(K)^G=0$ tests are partial guards but do not fully certify that the branch data defines the intended BCGP $G$-cover. The values are correct because the tuples are copied verbatim from BCGP §6; adding an assertion that the ordered product of each `branch`/`S_i` list is the identity would close this gap directly.

3. **`parse_perm` on non-disjoint cycle products.** The code comments that its left-to-right composition convention is unchecked for non-disjoint products and relies on the listed branch elements being mostly disjoint. The order/genus assertions catch gross mis-parses, but a mis-parse that preserves element orders and the group order could survive; the product-one check in point 2 would also harden this.

None of these alters the fully cross-checked $\mathbb Z_4^2$, $K^2=2$, $d=0$ conclusion or the mechanism attached to it. They bear on the confidence one places in the eight nonabelian $d>0$ values, which in any case enter only as "this sufficient vanishing route is unavailable," a statement that does not depend on the exact integer $d$.