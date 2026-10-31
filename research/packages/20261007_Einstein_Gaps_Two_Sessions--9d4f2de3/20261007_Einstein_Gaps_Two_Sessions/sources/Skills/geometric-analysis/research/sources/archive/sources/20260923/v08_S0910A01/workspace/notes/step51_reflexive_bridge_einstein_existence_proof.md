# Step 51: Reflexive extension bridge and Einstein existence for the BCGP Z₄² K²=2 row

## 0. Result

**Theorem.** Let $X = (C_1 \times C_2)/G$ be the canonical model of the BCGP $K^2=2$, $G=\mathbb Z_4^2$, $(T_1,T_2)=((4,4,4),(4,4,4))$ product-quotient row with branch triples $S_1=((1,3),(1,0),(2,1))$, $S_2=((3,2),(0,1),(1,1))$, having exactly six $A_1$ singularities and $\pi_1 = (\mathbb Z_2)^3$.  Let $S \to X$ be the minimal resolution.  Then:

1. $H^2(X, T_X^0) = 0$;
2. $X$ admits a global Q-Gorenstein smoothing that simultaneously smooths all six $A_1$ nodes;
3. The smooth fiber carries a negative Kähler--Einstein metric ($\operatorname{Ric}_h = -h$);
4. $S$ is diffeomorphic to the smooth fiber;
5. Therefore $S$ carries a smooth Einstein metric.

## 1. Setup

$G = \mathbb Z_4^2$ acts diagonally on $Y = C_1 \times C_2$, where $C_i$ are smooth genus-3 curves with $G$-actions given by the BCGP branch data.  Let $\pi: Y \to X = Y/G$ be the quotient map.

* $X$ is a normal projective surface with $K_X$ ample ($p_g=0$, $q=0$, $K^2=2>0$, surface of general type).
* $\operatorname{Sing}(X)$ consists of six isolated $A_1$ singularities (rational double points) arising from the six orbits of fixed points with stabilizer $\mathbb Z/2\mathbb Z \subset G$.
* The étale locus $U = X \setminus \operatorname{Sing}(X)$ has $\operatorname{codim}(\operatorname{Sing}(X)) = 2$.

## 2. The reflexive extension bridge

**Proposition 2.1.** $T_X^0 \cong (\pi_* T_Y)^G$.

*Proof.* We check three conditions:

**(a) Both sheaves are reflexive on $X$.**

$T_X^0 = \mathcal{Hom}(\Omega_X^1, \mathcal O_X) = (\Omega_X^1)^\vee$.  On a normal Noetherian scheme, the dual of any coherent sheaf is reflexive.  (Locally: for $A = \mathcal O_{X,x}$ a two-dimensional normal local ring with $\operatorname{depth} A = 2$, a finite presentation of $\Omega_A^1$ dualizes to a submodule of a free module of the correct depth; the depth lemma gives $\operatorname{depth} T_X^0 \ge 2$, which on a normal surface implies reflexivity.)  Thus $T_X^0$ is reflexive.

For $(\pi_* T_Y)^G$: at each $x \in X$, let $A = \mathcal O_{X,x}$ and let $B$ be the semi-local ring of $\pi^{-1}(x)$.  Each local factor $B_y$ is a two-dimensional regular (hence Cohen--Macaulay) local ring, and $(T_Y)_y$ is free over $B_y$.  Since $\pi$ is finite, a system of parameters of $A$ is also a system of parameters in each $B_y$, so $(\pi_* T_Y)_x$ is a maximal Cohen--Macaulay $A$-module (depth $2$).  The Reynolds operator $R = \frac{1}{|G|}\sum_g g^*$ is $\mathcal O_X$-linear and idempotent, giving a splitting $\pi_* T_Y = (\pi_* T_Y)^G \oplus \ker R$.  Direct summands inherit the depth, so $(\pi_* T_Y)^G$ has depth $\ge 2$ at every point.  On the normal surface $X$, a torsion-free coherent sheaf satisfying $S_2$ is reflexive.  Thus $(\pi_* T_Y)^G$ is reflexive.

**(b) The diagonal $G$-action is free in codimension one, and the two sheaves agree on $U$.**

The action of $G = \mathbb Z_4^2$ on $C_i$ is faithful (the branch triples generate $G$).  A nontrivial automorphism of a smooth curve fixes only finitely many points, so the diagonal action on $Y = C_1 \times C_2$ has no fixed curves: its non-free locus is a finite set of points.  The quotient map $\pi: Y \to X$ is therefore étale outside the images of those fixed points, i.e., on $U = X \setminus \operatorname{Sing}(X)$.  (BCGP classifies the non-free orbits as exactly six points with stabilizer $\mathbb Z/2\mathbb Z$, giving six $A_1$ singularities on $X$.)

On $U$, $\pi^{-1}(U) \to U$ is a finite étale $G$-cover, so $T_U = (\pi_* T_{\pi^{-1}(U)})^G$ by standard étale descent.  Since $T_X^0|_U = T_U$ (the reflexive tangent sheaf agrees with the tangent sheaf on the smooth locus), the claim follows.

**(c) Reflexive extension is unique.**

On a normal variety of dimension $\ge 2$, two reflexive sheaves that agree on the complement of a closed subset of codimension $\ge 2$ are isomorphic.  Since $\operatorname{Sing}(X)$ is a finite set on the surface $X$, this applies.  $\square$

## 3. Cohomological comparison

**Proposition 3.1.** $H^2(X, T_X^0) = H^2(Y, T_Y)^G$.

*Proof.* By Proposition 2.1, $H^2(X, T_X^0) = H^2(X, (\pi_* T_Y)^G)$.

**Step 1:** The Reynolds operator $R = \frac{1}{|G|}\sum_{g \in G} g^*$ splits $\pi_* T_Y = (\pi_* T_Y)^G \oplus \ker(R)$, so
$$H^i(X, (\pi_* T_Y)^G) = H^i(X, \pi_* T_Y)^G.$$

**Step 2:** Since $\pi$ is finite (hence affine), $R^j\pi_* = 0$ for $j > 0$, so the Leray spectral sequence gives $H^i(X, \pi_* T_Y) = H^i(Y, T_Y)$.

Combining: $H^2(X, T_X^0) = H^2(Y, T_Y)^G$.  $\square$

## 4. Vanishing via equivariant Serre duality and Künneth

**Proposition 4.1.** $H^2(Y, T_Y)^G = 0$.

*Proof.*

**Step 1: Equivariant Serre duality.**

$Y = C_1 \times C_2$ is a smooth projective surface with $K_Y = K_{C_1} \boxtimes K_{C_2}$.  Serre duality gives a perfect pairing
$$H^2(Y, T_Y) \times H^0(Y, \Omega_Y^1 \otimes K_Y) \longrightarrow H^2(Y, K_Y) \xrightarrow{\operatorname{tr}} \mathbb C.$$
The trace map $\operatorname{tr}$ is $G$-equivariant (it sends the fundamental class, which is $G$-invariant, to $1$).  Hence the pairing is $G$-equivariant for the diagonal $G$-action on the left.  Taking $G$-invariants:
$$H^2(Y, T_Y)^G \cong \bigl(H^0(Y, \Omega_Y^1 \otimes K_Y)^G\bigr)^{\!\vee}.$$
(Using: for a finite group in char $0$, $(V^\vee)^G \cong (V^G)^\vee$.)

**Step 2: Künneth decomposition.**

On $Y = C_1 \times C_2$:
$$\Omega_Y^1 = \Omega_{C_1}^1 \boxtimes \mathcal O_{C_2} \oplus \mathcal O_{C_1} \boxtimes \Omega_{C_2}^1 = K_{C_1} \boxtimes \mathcal O_{C_2} \oplus \mathcal O_{C_1} \boxtimes K_{C_2}.$$
Thus
$$\Omega_Y^1 \otimes K_Y = (K_{C_1}^{\otimes 2} \boxtimes K_{C_2}) \oplus (K_{C_1} \boxtimes K_{C_2}^{\otimes 2}).$$
By Künneth:
$$H^0(Y, \Omega_Y^1 \otimes K_Y) = \bigl(H^0(C_1, 2K_{C_1}) \otimes H^0(C_2, K_{C_2})\bigr) \oplus \bigl(H^0(C_1, K_{C_1}) \otimes H^0(C_2, 2K_{C_2})\bigr).$$

**Step 3: Character computation (verified by script).**

Using the actual BCGP §6.7 branch triples $S_1 = ((1,3),(1,0),(2,1))$, $S_2 = ((3,2),(0,1),(1,1))$, Chevalley--Weil for abelian covers of $\mathbb P^1$ gives (each character pair $(a,b) \in (\mathbb Z/4\mathbb Z)^2$):

$H^0(K_{C_1})$: characters $(2,3)$, $(3,0)$, $(3,1)$ — total $g_1 = 3$ ✓

$H^0(K_{C_2})$: characters $(0,3)$, $(1,2)$, $(3,3)$ — total $g_2 = 3$ ✓

Both curves are non-hyperelliptic.  If $C_i$ were hyperelliptic with involution $\iota$, then either $\iota \in G$ or $\iota \notin G$.  If $\iota \in G$, then $\iota$ has order $2$ and fixes $2g+2 = 8$ points on a genus-$3$ curve, but the script verifies that every order-$2$ element of $G$ fixes at most $4$ points on each curve — contradiction.  If $\iota \notin G$, then $G$ acts faithfully on $C_i/\langle\iota\rangle \cong \mathbb P^1$, giving an embedding $\mathbb Z_4^2 \hookrightarrow \operatorname{PGL}_2(\mathbb C)$; but every finite abelian subgroup of $\operatorname{PGL}_2(\mathbb C)$ is cyclic or $\cong (\mathbb Z/2)^2$, which cannot contain $\mathbb Z_4^2$ — contradiction.  Hence both $C_i$ are non-hyperelliptic, and $\operatorname{Sym}^2 H^0(K_{C_i}) \xrightarrow{\sim} H^0(2K_{C_i})$ by the $G$-equivariant canonical multiplication map.

$H^0(2K_{C_1})$: characters $(0,2)$, $(1,0)$, $(1,3)$, $(2,0)$, $(2,1)$, $(2,2)$ — total $6 = \binom{3+1}{2}$ ✓

$H^0(2K_{C_2})$: characters $(0,1)$, $(0,2)$, $(1,1)$, $(2,0)$, $(2,2)$, $(3,2)$ — total $6$ ✓

**Invariant dimensions:**

For $\bigl(H^0(2K_{C_1}) \otimes H^0(K_{C_2})\bigr)^G$: need characters $\chi_1 + \chi_2 = (0,0) \bmod 4$.

| $\chi_1$ from $H^0(2K_{C_1})$ | Need $\chi_2 = -\chi_1$ | In $H^0(K_{C_2})$? |
|---|---|---|
| $(0,2)$ | $(0,2)$ | No (have $(0,3),(1,2),(3,3)$) |
| $(1,0)$ | $(3,0)$ | No |
| $(1,3)$ | $(3,1)$ | No |
| $(2,0)$ | $(2,0)$ | No |
| $(2,1)$ | $(2,3)$ | No |
| $(2,2)$ | $(2,2)$ | No |

Result: $\dim = 0$.

For $\bigl(H^0(K_{C_1}) \otimes H^0(2K_{C_2})\bigr)^G$:

| $\chi_1$ from $H^0(K_{C_1})$ | Need $\chi_2 = -\chi_1$ | In $H^0(2K_{C_2})$? |
|---|---|---|
| $(2,3)$ | $(2,1)$ | No (have $(0,1),(0,2),(1,1),(2,0),(2,2),(3,2)$) |
| $(3,0)$ | $(1,0)$ | No |
| $(3,1)$ | $(1,3)$ | No |

Result: $\dim = 0$.

**Conclusion:** $H^0(Y, \Omega_Y^1 \otimes K_Y)^G = 0$, hence $H^2(Y, T_Y)^G = 0$, hence $H^2(X, T_X^0) = 0$.  $\square$

## 5. Global Q-Gorenstein smoothing

By Lee--Park Proposition 2.4(2) (citing Kollár--Shepherd-Barron, Wahl, and Hacking; see the exact sequence in §2 of the Lee--Park source):

For a normal projective surface $X$ with quotient singularities, $H^2(T_X^0) = 0$ implies every local deformation of the singularities globalizes.

Each $A_1$ singularity is a rational double point, hence a T-singularity.  Its standard model is $\{xy - z^2 = 0\} \subset \mathbb C^3$, with versal Q-Gorenstein smoothing $\{xy - z^2 = \tau\}$ ($\tau \in \mathbb C$, one-dimensional).  With six $A_1$ points, $H^0(\widetilde T_X^1) = \mathbb C^6$ (one local parameter per node).

Lee--Park Proposition 2.4(2) states that $H^2(T_X^0) = 0$ implies the **obstruction** to globalizing local deformations vanishes, so every element of $H^0(\widetilde T_X^1)$ lifts to a global Q-Gorenstein deformation (not merely at the first-order/tangent level, but as an actual deformation over a disk $\Delta$).  Choosing a lift of a vector with all six components nonzero gives a one-parameter family $\mathcal X \to \Delta$ with $\tau_i(t) = a_i t + O(t^2)$, $a_i \ne 0$, so all six nodes are simultaneously smoothed for small $t \ne 0$.  The generic fiber $X_t$ is smooth.

## 6. Ampleness persistence and Aubin--Yau

$K_X$ is ample on $X$.  *Proof:* since $\pi: Y \to X$ is étale in codimension one and both $Y$, $X$ are normal, $\pi^* K_X = K_Y$ (ramification formula with trivial ramification divisor).  Now $K_Y = K_{C_1} \boxtimes K_{C_2}$ is ample on the product of genus-$3$ curves.  A line bundle is ample if and only if its pullback under a finite surjective morphism is ample (EGA III or Lazarsfeld, *Positivity*, 1.2.13), so $K_X$ is ample.

In the proper flat family $\mathcal X \to \Delta$, the Q-Cartier divisor $\omega_{\mathcal X/\Delta}^{[m]}$ (for suitable $m$) is a line bundle restricting to $mK_X$ (ample) on the central fiber.  Ampleness on fibers of a proper flat family is an open condition, so $mK_{X_t}$ is ample for small $t \ne 0$, hence $K_{X_t}$ is ample.

By Aubin--Yau (independently Aubin 1976, Yau 1978): on a compact Kähler manifold with ample canonical bundle, there exists a unique Kähler--Einstein metric $\omega$ with $\operatorname{Ric}(\omega) = -\omega$.  This gives a Riemannian metric $h$ on $X_t$ with $\operatorname{Ric}_h = -h$, i.e., a negative Einstein metric.

## 7. Smooth-topological bridge

**Claim:** The minimal resolution $S$ and the smooth fiber $X_t$ are diffeomorphic as smooth $4$-manifolds.

*Proof via ADE simultaneous resolution.*  Each $A_1$ singularity $\{xy - z^2 = 0\}$ admits a simultaneous resolution after the base change $\tau = s^2$.  Concretely, the family $\{xy - z^2 = s^2\}$ lifts to a family of smooth surfaces via the resolution of the total space.  Since the six nodes are disjoint, a single finite base change $t \mapsto s(t)$ produces a simultaneous resolution
$$\widetilde{\mathcal X} \to \Delta_s$$
whose central fiber ($s=0$) is the minimal resolution $S$ and whose other fibers are the original smooth fibers $X_{\tau(s)}$ (unchanged away from the nodes).  This family is proper and smooth (all fibers are smooth compact surfaces), so Ehresmann's theorem gives
$$S \cong_{\operatorname{diff}} X_t.$$

*Remark.* The local topological content is that for $A_1$, the compact Milnor fiber $D(T^*S^2)$ and the resolution neighborhood $D(\mathcal O_{\mathbb P^1}(-2))$ are both disk bundles over $S^2$ with Euler number $-2$ and boundary $\mathbb{RP}^3$, hence diffeomorphic as manifolds-with-boundary.  For general ADE singularities (not just $A_1$), the same conclusion holds by Brieskorn's theorem.  For non-RDP T-singularities, the Milnor fiber and resolution neighborhood are generally *not* diffeomorphic — the gluing produces rational blowdowns instead.  $\square$

## 8. Conclusion

Combining §2--§7: the smooth $4$-manifold $S$ (the minimal resolution of the BCGP $\mathbb Z_4^2$ canonical model with six $A_1$ nodes) is diffeomorphic to $X_t$, which carries a negative Kähler--Einstein metric.  Therefore $S$ carries a smooth Einstein metric with $\operatorname{Ric}_h = -h$.  $\square$

## 9. Relation to the classical (Z₂)³ Campedelli component

The explicit six-nodal Campedelli model from `step50_six_nodal_campedelli_arrangement.py` provides an independent, more elementary Einstein existence example: the smoothing is constructed directly by moving seven lines to general position, bypassing the $H^2 = 0$ machinery entirely.  That model lies in the Alexeev--Pardini $(\mathbb Z_2)^3$ component.

Whether the BCGP $G = \mathbb Z_4^2$ row also lies in the same moduli component is a separate question.  The shared fundamental group $(\mathbb Z_2)^3$ and numerical invariants ($K^2=2$, $p_g=q=0$) do not determine the moduli component.  The reflexive extension proof is self-contained and applies to the BCGP row directly, regardless of this identification.

## 10. IL scaling correction

A03 peer message #386 and A02 message #382 initially claimed that the restricted negative Ishida--LeBrun gap must degenerate as $\delta_0 \sim A^{-1/2}$.  A03 #386 now withdraws this claim.

The correct proportional-volume argument is:
$$\int_M \Phi \le 119Q \le C\delta^2 \operatorname{Vol}(M),$$
$$\operatorname{Vol}(P) \ge \alpha\,\operatorname{Vol}(M) \quad \text{(where $P$ is the good-center set)},$$
$$\frac{1}{\operatorname{Vol}(P)}\int_P m(p)\,dp \le \frac{C \int \Phi}{\operatorname{Vol}(P)} \le \frac{C\delta^2 \operatorname{Vol}(M)}{\alpha \operatorname{Vol}(M)} = \frac{C}{\alpha}\delta^2.$$
Hence some good center $p$ has $m(p) \le (C/\alpha)\delta^2$, uniformly in the topological parameter $A$.  The local lower bound $m(p) \ge \eta > 0$ (from forbidden-germ compactness) then requires $\delta \ge \sqrt{\alpha\eta/C}$, which is dimension-dependent but $A$-independent.

The key point: $A$ appears in both the total error budget ($\sim \delta^2 A$) and the total center volume ($\sim \alpha A$), so it cancels.  The earlier A02/A03 argument localized to a single unit ball rather than averaging over the proportional center volume.

The restricted IL negative gap theorem remains conditional on a fully proved regularized-flow module (the coupled transported-coefficient start is not yet established).  It should not be promoted to a dimension-only result (it applies within the specific IL geography), but neither should it be demoted to a per-topology result on unverified scaling grounds.

## 11. Files and dependencies

* Character computation: `workspace/scripts/step50_z4x4_character_smoothing_test.py` (passed, Step 50)
* Hand-verification: §4 of this note
* Verification script: `workspace/scripts/step51_reflexive_bridge_verify.py` (this step)
* Classical model: `workspace/scripts/step50_six_nodal_campedelli_arrangement.py` (passed, Step 50)
* Lee--Park source: Knowledge, `A-construction-of-Horikawa-surface-via-Q-Gorenstein-smoothings`, Proposition 2.4
* BCGP source: Knowledge, `Quotients-of-products-of-curves`, §6.7
* Global smoothing evidence note: `workspace/notes/step50_global_smoothing_evidence_campedelli_front.md`
* This note supersedes the categorical claims in Step 49's note; those have already been corrected in place (Step 50).
