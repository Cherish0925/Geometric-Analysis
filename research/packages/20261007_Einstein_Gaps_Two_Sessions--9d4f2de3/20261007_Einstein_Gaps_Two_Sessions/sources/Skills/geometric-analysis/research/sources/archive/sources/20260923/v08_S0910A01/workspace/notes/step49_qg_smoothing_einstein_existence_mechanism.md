# Step 49: Q-Gorenstein smoothing as a testable Einstein-existence mechanism for product-quotient surfaces

> **Step 50 correction.** Sections 1 and 7 of the original Step 49 note stated the product-quotient reversal too categorically. The valid gain is a concrete global-smoothing mechanism to test. No global smoothing has yet been established for every selected product-quotient model, mixed-chirality fillings remain outside the complex-smoothing/Aubin--Yau mechanism, and failure of complex smoothing would not prove absence of an unrelated Einstein metric. See `workspace/notes/step50_global_smoothing_evidence_campedelli_front.md`.

## 1. Summary and main conclusions

This note establishes three facts that together sharpen the role of product-quotient surfaces in the Yau 26 research:

**A.** The $b_+ = 1$ of every $p_g = q = 0$ product-quotient resolution with only $A_1$ nodes rules out the Ishida–LeBrun connected-sum decomposition ($m \ge 2$ general-type blocks). Searching for IL overlap is therefore unnecessary.

**B.** The kernel-directed Eguchi–Hanson replacement at each $A_1$ node corresponds, via the hyperkähler parameter identification, to a complex smoothing of the node—not to a holomorphic resolution in the original complex structure. The local gluing parameters that make the Ricci defect vanish in the first obstruction are exactly the local deformation parameters for a Q-Gorenstein smoothing.

**C.** If the canonical model $Z$ admits a global Q-Gorenstein smoothing, then the smooth fiber $Z_t$ has ample canonical class (by openness of ampleness), hence carries a negative Kähler–Einstein metric (by Aubin–Yau), and is diffeomorphic to the minimal resolution $S$ (by Brieskorn's simultaneous resolution for rational double points). Therefore $S$ carries an Einstein metric.

**Consequence.** The product-quotient surface front now contains a concrete **existence mechanism to test**. When the relevant global Q-Gorenstein smoothing exists, the resolution carries an Einstein metric by the Aubin--Yau chain. Without that global smoothing, the front remains undecided rather than turning into an Einstein-nonexistence result.

## 2. The $b_+ = 1$ non-overlap with Ishida–LeBrun

For $p_g = q = 0$, $\chi_h = 1$, $K^2 \in \{2, 4, 6\}$ (the A1-only rows):

| $K^2$ | $\#A_1$ | $e$ | $\tau$ | $b_+$ | $b_-$ |
|-------|---------|-----|--------|--------|--------|
| 2     | 6       | 10  | $-6$   | 1      | 7      |
| 4     | 4       | 8   | $-4$   | 1      | 5      |
| 6     | 2       | 6   | $-2$   | 1      | 3      |

The IL theorem assumes $M = (\#_{j=1}^m X_j) \# N$ with $m \in \{2,3\}$, $b_+(N) = 0$, and each $X_j$ a surface of general type. Since $b_+(X_j) \ge 1$ (the Kähler class is a positive self-intersection class), $b_+(M) \ge m \ge 2$. But all our surfaces have $b_+ = 1$. Therefore **no product-quotient surface with $p_g = q = 0$ and only $A_1$ nodes can appear in the IL hypothesis set**.

This observation is elementary but dispositive: it eliminates the overlap concern raised in Step 48 and redirects effort toward the existence mechanism below.

## 3. Hyperkähler parameter identification: kernel = smoothing

### 3.1 Local A1 deformation theory

The $A_1$ singularity $\{uv - w^2 = 0\} \subset \mathbb{C}^3$ has:
- **Resolution**: blow up the origin, inserting $\mathbb{CP}^1$ with normal bundle $\mathcal{O}(-2)$.
- **Smoothing**: deform to $\{uv - w^2 = t\}$, smooth for $t \ne 0$ (the Milnor fiber $\cong T^*S^2$).

In the hyperkähler family of ALE metrics on the $A_1$ space $T^*\mathbb{CP}^1$, there are three real parameters $(\zeta_1, \zeta_2, \zeta_3)$:
- $\zeta_1 > 0$, $\zeta_2 = \zeta_3 = 0$: the resolution, with exceptional $\mathbb{CP}^1$ of Kähler area $\zeta_1$.
- $\zeta_1 = 0$, $(\zeta_2, \zeta_3) \ne (0,0)$: the complex smoothing, i.e., the Milnor fiber with complex parameter $t = \zeta_2 + i\zeta_3$.

### 3.2 Product Kähler–Einstein orbifold

On the product KE orbifold $(C_1 \times C_2)/G$ with $\operatorname{Ric} = \Lambda g$, the chiral curvature blocks are:
$$
R_+ = R_- = \operatorname{diag}(\Lambda, 0, 0).
$$
The nonzero eigendirection of $R_+$ is the Kähler form $\omega$. The two-dimensional kernel of $R_+$ corresponds to the real and imaginary parts of the $(2,0) + (0,2)$ directions.

In the Eguchi–Hanson desingularization, the first Ozuch obstruction lives in the cokernel of the linearized operator; it is annihilated by choosing the bubble parameter in the kernel of $R_+$. But the kernel of $R_+$ is exactly the $(2,0)+(0,2)$ plane, which corresponds to the **complex smoothing directions**, not the Kähler resolution direction.

### 3.3 Identification

Therefore: **the kernel-directed Eguchi–Hanson replacement that kills the first obstruction corresponds to a complex smoothing of each $A_1$ node, not a holomorphic resolution**. The local Riemannian parameters used by the approximate Einstein construction point in the same direction as the local Q-Gorenstein deformation parameters.

**TTCS correction (Step 49):** The identification requires care: the smoothing parameter $t$ in the versal deformation $\{uv - w^2 = t\}$ is $t \propto (\zeta_2 + i\zeta_3)^2$ (not $t = \zeta_2 + i\zeta_3$ directly), because the Weyl group $\mathbb{Z}/2\mathbb{Z}$ acts by $\zeta_{\mathbb{C}} \mapsto -\zeta_{\mathbb{C}}$. This is exactly the base change in Step 5 of the existence chain. Furthermore, the local Riemannian kernel-directed parameters are not automatically integrable complex deformation parameters; the passage from local ALE parameters to a global Q-Gorenstein family is controlled by different (nonlinear, global) theory. The correct statement is:

> The local near-Einstein construction and Q-Gorenstein smoothing share the same infinitesimal direction at each node. Whether both extend globally is a separate question for each.

This explains why the local approximate construction is available even though the resolution has K-trivial exceptional curves: the construction operates in the smoothing direction, not the resolution direction.

## 4. The Aubin–Yau Einstein existence chain

**Theorem (conditional).** Let $Z = (C_1 \times C_2)/G$ be a product-quotient canonical model with $p_g = q = 0$ and only $A_1$ singularities. Suppose $Z$ admits a global Q-Gorenstein smoothing $\pi: \mathcal{Z} \to \Delta$. Then the smooth four-manifold underlying the minimal resolution $S$ of $Z$ carries an Einstein metric.

**Proof sketch.** The chain has five links:

**(i) Ampleness persists.** $K_Z$ is ample (it's a canonical model of a surface of general type). In the flat projective family $\mathcal{Z} \to \Delta$ with Q-Cartier relative canonical divisor $K_{\mathcal{Z}/\Delta}$, some multiple $mK_{\mathcal{Z}/\Delta}$ is Cartier and ample on the central fiber. By semicontinuity of cohomology (or Nakai–Moishezon applied fiberwise), $mK_{Z_t}$ is ample for $t$ near $0$. Therefore $K_{Z_t}$ is ample. $\square$

**(ii) Aubin–Yau.** Since $Z_t$ is a smooth projective surface with ample canonical bundle, Aubin–Yau gives a unique Kähler–Einstein metric $\omega_t$ with $\operatorname{Ric}(\omega_t) = -\omega_t$. $\square$

**(iii) Simultaneous resolution.** The singularities of $Z_0$ are rational double points ($A_1$). By Brieskorn's theorem (see Shepherd-Barron \cite{shepherdbarron2017weyl}, Ito–Sato–Tosun \cite{ito2026resolutions}), after a finite base change $\Delta' \to \Delta$ (degree 2 for $A_1$, the Weyl group $\mathbb{Z}/2\mathbb{Z}$), the pulled-back family $\mathcal{Z}' \to \Delta'$ admits a simultaneous resolution $\widetilde{\mathcal{Z}}' \to \Delta'$: a smooth family whose central fiber is the minimal resolution $S$ of $Z$. $\square$

**(iv) Diffeomorphism.** Since $\widetilde{\mathcal{Z}}' \to \Delta'$ is a smooth proper family, Ehresmann's theorem gives a diffeomorphism between any two fibers. The central fiber is $S$; the general fiber is the minimal resolution of $Z'_t = Z_t$ (which is smooth, so the resolution is the identity). Therefore $S$ is diffeomorphic to $Z_t$ as smooth four-manifolds.

Additionally, by Choi–Park–Shin \cite{choi2018symplectic}: "rational double points contribute trivially because their Milnor fibers are symplectomorphic to their minimal resolutions." $\square$

**(v) Conclusion.** $S$ is diffeomorphic to $Z_t$, and $Z_t$ carries a Kähler–Einstein metric with $\operatorname{Ric} = -\omega_t$. Therefore the smooth four-manifold underlying $S$ carries an Einstein metric. $\square$

## 5. Obstruction analysis for global Q-Gorenstein smoothing

The key input not yet established is the **global** Q-Gorenstein smoothability.

### 5.1 The sufficient condition

By Lee–Park \cite{lee2007construction} Theorem 2.1:

> If $H^2(T_Z^0) = 0$, then every local Q-Gorenstein smoothing of the singularities can be globalized.

For a canonical model $Z$ with only rational double points, the Burns–Wahl comparison gives $H^2(T_Z^0) \cong H^2(T_S)$ where $S$ is the minimal resolution (see Park et al. \cite{park2012simply}). **TTCS correction:** The intermediate step via $T_S(-\log E)$ requires the Burns–Wahl result specific to RDPs; one should not write $H^2(T_S(-\log E)) = H^2(T_S)$ without citing this result precisely.

The Euler characteristic of the tangent bundle is:
$$
\chi(T_S) = \frac{1}{6}(7c_1^2 - 5c_2) = 2K^2 - 10 \quad \text{when } \chi_h = 1.
$$

Since $h^0(T_S) = 0$ for surfaces of general type:

| $K^2$ | $\chi(T_S)$ | $h^2 - h^1$ | $h^2 = 0$ possible? |
|-------|-------------|-------------|---------------------|
| 2     | $-6$        | $-6$        | **Yes**, if $h^1 = 6$ |
| 4     | $-2$        | $-2$        | **Yes**, if $h^1 = 2$ |
| 6     | $+2$        | $+2$        | **No**, $h^2 \ge 2$   |
| 8     | $+6$        | $+6$        | N/A (no singularities) |

**For $K^2 = 2$ and $K^2 = 4$**: The sufficient condition $H^2(T_S) = 0$ is numerically possible. Whether it holds for specific product-quotient families requires computing $H^0(\Omega^1_S \otimes K_S)$ using the fibration structure and equivariant cohomology. This is a concrete, tractable computation.

**For $K^2 = 6$**: The sufficient condition fails. However, Lee–Park's Theorem 2.2 provides an alternative: if there is a cyclic group action with a Q-Gorenstein smoothing of the quotient and certain cohomological vanishing, the smoothing lifts. Product-quotient surfaces often have such structure (they are quotients by construction). This is a concrete alternative route.

**For $K^2 = 8$**: Surfaces isogenous to a product (no singularities). The product metric $g_1 + g_2$ on $C_1 \times C_2$ descends to an Einstein metric on the étale quotient. No deformation needed.

### 5.2 What the sources say about specific families

The Bauer survey \cite{bauerproduct} and BCGP \cite{fallucca2026minimality} list the explicit families with their groups, signatures, and fundamental groups. For the $K^2 = 2$ case with 6 $A_1$ nodes, there are 7 explicit families (Table 2 in Bauer):

| $T_1$ | $T_2$ | $G$ | $H_1(S,\mathbb{Z})$ | $\pi_1(S)$ |
|--------|--------|-----|---------|---------|
| $2,3,7$ | $4^3$ | $\operatorname{PSL}(2,7)$ | $\mathbb{Z}_2^2$ | $\mathbb{Z}_2^2$ |
| $2,4,5$ | $2,6^2$ | $\mathfrak{S}_5$ | $\mathbb{Z}_3$ | $\mathbb{Z}_3$ |
| $2,5^2$ | $2^3,3$ | $\mathfrak{A}_5$ | $\mathbb{Z}_5$ | $\mathbb{Z}_5$ |
| $2,4,6$ | $2^3,4$ | $\mathfrak{S}_4 \times \mathbb{Z}_2$ | $\mathbb{Z}_2^2$ | $\mathbb{Z}_2^2$ |
| $2,6^2$ | $2^3,3$ | $\mathfrak{S}_3 \times \mathfrak{S}_3$ | $\mathbb{Z}_3$ | $\mathbb{Z}_3$ |
| $4^3$ | $4^3$ | $\mathbb{Z}_4^2$ | $\mathbb{Z}_2^3$ | $\mathbb{Z}_2^3$ |
| $2^3,4$ | $2^3,4$ | $D_4 \times \mathbb{Z}_2$ | $\mathbb{Z}_2 \times \mathbb{Z}_4$ | $\mathbb{Z}_2 \times \mathbb{Z}_4$ |

These are all finite-fundamental-group surfaces. The equivariant structure ($G$ acts on $C_1 \times C_2$) provides additional tools for computing the relevant $H^2$.

### 5.3 Connection to existing Q-Gorenstein constructions

Park et al. \cite{park2012simply} construct simply connected numerical Campedelli surfaces ($K^2 = 2$, $p_g = 0$) with involutions via Q-Gorenstein smoothing of surfaces with Wahl singularities. They prove $H^2 = 0$ in their specific setting. While their surfaces are different from product-quotient surfaces, the techniques (Serre duality, logarithmic tangent sheaf, involution-based vanishing) directly apply.

Keum–Lee–Park \cite{keum2010construction} and Urzúa \cite{urzagorenstein} further develop Q-Gorenstein smoothing constructions for surfaces of general type with $p_g = 0$. In particular, Urzúa's Proposition 2.7 shows that a minimal W-surface with $K^2 > 0$ has a canonical model with ample Q-Cartier canonical divisor and only T-singularities, confirming that ampleness persists in the Q-Gorenstein family.

## 6. Mixed-chirality and positive-branch caveats

The argument in §4 uses the **complex structure** of the canonical model, hence applies specifically to the Kähler/complex-smoothing directions. For **mixed-chirality** Eguchi–Hanson insertions (where the bubble orientation differs from the ambient one at some nodes), the parameter identification in §3 may give a non-holomorphic deformation of the singular model. Such a deformation would not be a Q-Gorenstein smoothing, and the Aubin–Yau argument would not apply.

For the **positive** product-quotient rows ($S^2 \times S^2$ quotients), the canonical class is anti-ample, so the Aubin–Yau mechanism does not produce Einstein metrics. The positive branch requires either:
- A Fano/Tian–Yau existence theorem (but these orbifolds have singularities and the smooth types are unknown), or
- An independent positive Einstein obstruction compatible with positive scalar curvature.

## 7. Research consequences for Yau 26

**A.** The product-quotient construction front now has a concrete route to Einstein existence. If global Q-Gorenstein smoothing can be established for a concrete $K^2=2$ or $K^2=4$ family, the same smooth manifold would carry a negative Kähler--Einstein metric via smoothing and Aubin--Yau. This would make that family compatible with the negative-sign form of Yau 26, while not proving the dimension-uniform proposition.

**B.** The $b_+ = 1$ observation rules out the specific Ishida--LeBrun connected-sum hypotheses for the ordinary $p_g=q=0$ product-quotient resolutions considered here.

**C.** This direction should not be used as a categorical obstruction route. A failed complex smoothing would leave exact Einstein existence open, and mixed-chirality fillings are not covered by the complex-smoothing/Aubin--Yau chain. The positive $S^2\times S^2$ quotient rows also need a separate positive-Einstein existence mechanism or a sign-compatible obstruction.

**D.** The next mathematical work is to test actual global smoothing, not merely numerical possibility. For a named family, use the actual two diagonal $G$-actions to compute the local-to-global deformation image and the relevant equivariant cohomology. Vanishing of $H^2(T_S)$ is a strong sufficient route; if it fails, the more informative object is whether an actual deformation component smooths all nodes.

## 8. Sources

- \cite{bauerproduct} Bauer, Product-Quotient Surfaces: Results and Problems (arXiv:1204.3409)
- \cite{lee2007construction} Lee–Park, A construction of Horikawa surface via Q-Gorenstein smoothings (arXiv:0708.3319)
- \cite{urzagorenstein} Urzúa, Q-Gorenstein smoothings of surfaces and degenerations (arXiv:1311.4844)
- \cite{park2012simply} Park–Shin–Urzúa, A simply connected numerical Campedelli surface (arXiv:1108.0797)
- \cite{keum2010construction} Keum–Lee–Park, Construction from elliptic surfaces via Q-Gorenstein smoothing (arXiv:1008.1222)
- \cite{ito2026resolutions} Ito–Sato–Tosun, Resolutions and deformations of cyclic quotient surface singularities (arXiv:2604.04472)
- \cite{shepherdbarron2017weyl} Shepherd-Barron, Weyl group covers for Brieskorn's resolutions (arXiv:1711.10439)
- \cite{choi2018symplectic} Choi–Park–Shin, Symplectic fillings of quotient surface singularities (arXiv:1811.07373)
- \cite{bombieri1973canonical} Bombieri, Canonical models of surfaces of general type (IHES 1973)
- \cite{kollr2018moduli} Kollár, Moduli of varieties of general type (arXiv:1008.0621)
