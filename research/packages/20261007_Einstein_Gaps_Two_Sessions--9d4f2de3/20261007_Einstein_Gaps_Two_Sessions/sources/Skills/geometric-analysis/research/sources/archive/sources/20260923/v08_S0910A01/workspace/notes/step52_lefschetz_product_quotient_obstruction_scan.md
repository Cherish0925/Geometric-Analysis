# Step 52: Holomorphic Lefschetz obstruction scan for BCGP product-quotient rows

## 0. Mathematical role

Step 51 proved the direct singular-model bridge
\[
T_X^0 \cong (\pi_*T_Y)^G, \qquad
H^2(X,T_X^0) \cong H^2(Y,T_Y)^G,
\]
for a product quotient \(X=(C_1\times C_2)/G\) with isolated quotient singularities, and used equivariant Serre duality to identify the dual obstruction space with
\[
H^0(Y,\Omega_Y^1\otimes K_Y)^G =
\bigl(H^0(C_1,2K_{C_1})\otimes H^0(C_2,K_{C_2})\bigr)^G
\oplus
\bigl(H^0(C_1,K_{C_1})\otimes H^0(C_2,2K_{C_2})\bigr)^G .
\]
If this invariant space vanishes, Lee--Park globalization gives a strong sufficient mechanism for simultaneous Q-Gorenstein smoothing of all local RDP nodes; with ample canonical class, Aubin--Yau then gives a negative Kähler--Einstein metric on the smooth fiber and the ADE simultaneous-resolution bridge transfers it to the minimal resolution.

The Step 51 handoff proposed a direct bicanonical Chevalley--Weil formula. The strategist note correctly rejected that formula: in all-order-two inertia rows it would give the wrong value for every nontrivial character. This step replaces it by a uniform geometric character method using holomorphic Lefschetz. This method handles hyperelliptic curves and nonabelian groups without a separate irreducible-decomposition calculation.

## 1. Lefschetz formula and implementation

For a nonidentity automorphism \(u\) of a genus \(g\ge2\) curve \(C\), let \(\lambda_p\) be the tangent multiplier at a fixed point \(p\). With the pullback convention used consistently on both curves,
\[
\operatorname{Tr}(u\mid H^0(C,K_C))
=1+\sum_{p\in\mathrm{Fix}(u)}\frac{\lambda_p}{1-\lambda_p},
\]
where the \(1\) is the trace on \(H^1(K_C)\cong H^0(\mathcal O_C)^\vee\), and
\[
\operatorname{Tr}(u\mid H^0(C,2K_C))
=\sum_{p\in\mathrm{Fix}(u)}\frac{\lambda_p^2}{1-\lambda_p},
\]
because \(H^1(2K_C)=0\). At the identity the traces are \(g\) and \(3g-3\).

For the regular cover \(C\to\mathbb P^1\) with branch elements \(e_i\), fixed points of \(u\) are reconstructed from branch stabilizers: over the branch point with stabilizer \(H_i=\langle e_i\rangle\), a coset representative \(aH_i\) contributes a fixed point if \(a^{-1}ua=e_i^k\ne1\), and the local multiplier is a root of unity determined by \(k/|e_i|\) (the opposite exponent dualizes all characters but leaves invariant dimensions unchanged when used on both curves).

The target dimension is computed directly by the tensor-character average
\[
d=\frac1{|G|}\sum_{u\in G}\left(
\chi_{2,C_1}(u)\chi_{1,C_2}(u)+
\chi_{1,C_1}(u)\chi_{2,C_2}(u)
\right).
\]
The script checks group orders, genera via Riemann--Hurwitz, and the quotient condition \(\frac1{|G|}\sum_u\chi_{1,C_j}(u)=h^0(K_{\mathbb P^1})=0\). It also verifies that the final averages are integers.

Script: `workspace/scripts/step52_lefschetz_obstruction_dimensions.py`  
Data: `workspace/data/step52_lefschetz_obstruction_dimensions.json`

After the first successful run I added further safeguards and reran the script: it now recomputes every row with the opposite tangent-multiplier exponent to confirm the total invariant dimension is unchanged, checks that each displayed branch list separately generates the full group, checks branch-element orders against the expected signatures, and verifies the spherical identity using BCGP's left-product convention for the displayed permutation rows. It also asserts the expected row dimensions below as a regression guard. These are strong consistency checks, but still not a substitute for an exact cyclotomic or formal proof.

## 2. Independent check on the completed \(K^2=2,\;G=\mathbb Z_4^2\) row

For BCGP §6.7, with branch triples
\[
S_1=((1,3),(1,0),(2,1)),\qquad
S_2=((3,2),(0,1),(1,1)),
\]
the Lefschetz average gives
\[
d_{21}=0,\qquad d_{12}=0,
\qquad d=0.
\]
This independently checks the Step 50/51 character calculation without using the non-hyperelliptic symmetric-square shortcut. Fourier inversion of the Lefschetz traces recovers the Step 50 character tables after reversing the tangent-multiplier exponent (i.e. dualizing character labels). Thus the existing BCGP \(\mathbb Z_4^2,K^2=2\) Einstein-existence proof is strengthened rather than changed.

## 3. Results for the \(K^2=4\) BCGP rows

The scan covers all eleven \(K^2=4\) rows in BCGP Table 2/§6.9--§6.19. None has \(d=0\). Together with the §6.7 control row, the Step 52 scan covers twenty entries: §6.7 and §6.9--§6.27. It does not cover the remaining \(K^2=2\) entries §6.1--§6.6 or §6.8, so no uniqueness statement is made over the whole BCGP table.

| BCGP row | group | genera from displayed branches | \(d_{21}\) | \(d_{12}\) | total \(d\) |
|---|---:|---:|---:|---:|---:|
| §6.9 | \(\mathfrak S_5\) | \((4,21)\) | 1 | 1 | 2 |
| §6.10 | \(\mathfrak A_5\) | \((11,4)\) | 2 | 1 | 3 |
| §6.11 | \(\mathfrak S_4\times\mathbb Z_2\) | \((13,3)\) | 2 | 1 | 3 |
| §6.12 | \(\mathfrak S_4\times\mathbb Z_2\) | \((13,3)\) | 3 | 1 | 4 |
| §6.13 | \(\mathbb Z_2^4\rtimes\mathbb Z_2\) | \((5,5)\) | 2 | 2 | 4 |
| §6.14 | \(\mathfrak S_4\) | \((7,3)\) | 3 | 1 | 4 |
| §6.15 | \(\mathfrak S_3\times\mathbb Z_3\) | \((4,4)\) | 2 | 1 | 3 |
| §6.16 | \(\mathbb Z_3^2\rtimes\mathbb Z_2\) | \((4,4)\) | 2 | 2 | 4 |
| §6.17 | \(D_4\times\mathbb Z_2\) | \((5,3)\) | 3 | 2 | 5 |
| §6.18 | \(\mathbb Z_4\times\mathbb Z_2\) | \((3,3)\) | 2 | 2 | 4 |
| §6.19 | \(\mathbb Z_2^3\) | \((3,3)\) | 3 | 3 | 6 |

The two abelian genus-three rows are exactly where the old symmetric-square shortcut was dangerous. In §6.18 both curves are hyperelliptic (maximal fixed count 8 for the relevant involutions), and the Lefschetz computation gives \(d=4\), not zero. In §6.19 all inertia groups have order two; the rejected fractional-part formula would have been meaningless here, while Lefschetz gives \(d=6\).

## 4. Results for the \(K^2=6\) BCGP rows

The same method handles all eight \(K^2=6\) rows, including the nonabelian groups, without decomposing representations into irreducibles. None has \(d=0\).

| BCGP row | group | genera from displayed branches | \(d_{21}\) | \(d_{12}\) | total \(d\) |
|---|---:|---:|---:|---:|---:|
| §6.20 | \(\mathfrak A_6\) | \((19,16)\) | 2 | 2 | 4 |
| §6.21 | \(\mathfrak A_6\) | \((19,16)\) | 2 | 2 | 4 |
| §6.22 | \(\mathfrak S_5\times\mathbb Z_2\) | \((11,19)\) | 2 | 2 | 4 |
| §6.23 | \(\mathrm{PSL}(2,7)\) | \((19,8)\) | 2 | 2 | 4 |
| §6.24 | \(\mathrm{PSL}(2,7)\) | \((19,8)\) | 2 | 2 | 4 |
| §6.25 | \(\mathfrak A_5\) | \((16,4)\) | 3 | 2 | 5 |
| §6.26 | \(\mathfrak S_4\times\mathbb Z_2\) | \((19,3)\) | 4 | 2 | 6 |
| §6.27 | \(D_4\times\mathbb Z_2\) | \((7,3)\) | 4 | 3 | 7 |

The source section sometimes lists the two branch systems in the reverse genus order compared with Table 2; the script records the genera implied by the displayed §6 branch lists. This does not affect the total invariant dimension.

## 5. Interpretation for the product-quotient front

1. **The \(K^2=2,\mathbb Z_4^2\) existence result is special within this scan.** Its obstruction-dual invariant dimension vanishes, so Step 51's reflexive bridge supplies a direct Lee--Park smoothing mechanism.

2. **The same sufficient vanishing does not extend to the BCGP \(K^2=4\) or \(K^2=6\) rows.** In these rows \(H^2(X,T_X^0)\) is nonzero according to the Lefschetz character average. Therefore the simple theorem “all local node smoothings globalize because \(H^2(T_X^0)=0\)” is unavailable.

3. **Nonvanishing is not a negative Einstein conclusion.** It says only that the strong sufficient condition fails. The actual deformation image in the product of local smoothing spaces may still contain vectors with all node coordinates nonzero, possibly through a more delicate linear obstruction map or nonlinear lifting. Even if a chosen complex smoothing fails, the underlying smooth manifold could carry an Einstein metric through another complex structure or a non-Kähler Einstein metric.

4. **This is useful route control, not classification exhaustion.** The computation clarifies where global compatibility of local smoothing parameters becomes mathematically consequential. It deepens the relation between local approximate Einstein gluing and exact Einstein existence: local Eguchi--Hanson kernel directions may exist, but global complex geometry decides whether they assemble into an exact KE-producing smoothing. Exhausting more table entries is not by itself a route to the dimension-only Yau 26 proposition.

5. **Next mathematical object if this front is pursued:** for nonzero \(d\), compute the actual local-to-global map from global deformations into the direct sum of local \(A_1\) smoothing parameters (and its obstruction map), rather than treating \(d>0\) as failure. This would distinguish rows where all node parameters can still be nonzero from rows with genuine global compatibility constraints.

## 6. Relation to the full Yau 26 goal

This step strengthens the existence/control side of the product-quotient laboratory but does not solve the original Ricci-pinching proposition. The main contribution to Yau 26 is conceptual: a smooth four-manifold that arises naturally from a local approximate-Einstein gluing picture can carry an exact Einstein metric via a different complex structure, so any counterexample route must exclude all output Einstein metrics, not just the metric or complex structure used to build the pinched input. The positive branch, higher-dimensional branch, and the analytic IL flow module remain separate central fronts.
