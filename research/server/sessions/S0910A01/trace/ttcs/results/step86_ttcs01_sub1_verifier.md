# TTCS Independent Branch Record

```json
{
  "step_id": 86,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Sessions/S0910A01/workspace/notes/step85_green_response_computational_bridge.md",
    "Sessions/S0910A01/workspace/data/step85_product_operator_sector_ledger.json"
  ]
}
```

## Task

I am computing the exact inter-node obstruction coefficient for mixed-chirality Einstein desingularization of the product orbifold O=(S^2xS^2)/Z_2 with four A_1 (R^4/Z_2) nodes, following Ozuch's higher-order obstruction theory. The decisive structural finding of this step is that the correct inter-node coefficient is NOT a bulk product-Lichnerowicz spectral sum (which produced frame-sensitive proxy numbers -1.22, +0.41, -0.53 in prior work), but Ozuch's exact BOUNDARY PAIRING formula from Proposition 2.10 and Corollary 2.12 of arXiv:2105.13193 (file: Knowledge/objects/papers/Higher-order-obstructions...object.md, lines 606-666). Specifically:
(a) Prop 2.10 line 616: nu_l = 3 * integral over S^3/Z_2 of <H^4, V_{l,2}>_e, valid when lambda_k=0, where H^4=H^4(zeta_j^pm) is the ALE bubble's r^{-4} multipole at source node j, and V_{l,2} is the r^{+2}-growing homogeneous component of the orbifold obstruction/Einstein-deformation basis mode v_l = O(g_o) evaluated near the singular point.
(b) Cor 2.12 line 660: sum_j |zeta_j| lambda_1^j(zeta,v) = C sum_l <v,v_l> nu_l(zeta,0) + O(...), linking bubble first-obstruction variation to orbifold nu_l.
(c) H^4(zeta^+) = -rho(zeta)^- o zeta^+ /(2r^4) and H^4(zeta^-) = -zeta^- o rho(zeta)^+/(2r^4) are DIFFERENT symmetric 2-tensors depending on chirality (established in prior Step 84 with tr(C_ab C_cd)=4 delta_ac delta_bd).

MY CLAIM TO VERIFY: The mixed-row chirality coefficient c_opp - c_same reduces to the difference of boundary pairings nu_l(+) - nu_l(-) = 3 integral over S^3/Z_2 of <H^4(zeta^+) - H^4(zeta^-), V_{l,2}> where V_{l,2} is chirality-independent (it is a property of the orbifold Einstein deformation, common to all fillings), and only the source multipole H^4 carries the chirality. This is a clean r^{-4} source against r^{+2} receiver spherical boundary integral, so ONLY the degree-2 (in the R^4 harmonic sense) part of the receiver V_{l,2} survives against the degree-2 source multipole H^4, by orthogonality of RP^3 Laplacian eigenspaces (line 574, 636). 

QUESTIONS: (1) Is this reduction faithful to Ozuch's Prop 2.10 / Cor 2.12, i.e. is the inter-node coefficient genuinely the boundary integral 3*int<H^4, V_{l,2}> rather than a bulk resolvent, and does the chirality dependence enter only through H^4 with V_{l,2} chirality-independent? (2) What exactly is V_{l,2} for the product orbifold O=(S^2xS^2)/Z_2 -- is it the r^2-Taylor coefficient of the orbifold's Einstein-deformation obstruction modes O(g_o) at the node, and is the relevant space here the H_2-type quadratic tensor with P_e H_2 = Lambda e (line 476)? (3) Does the requirement lambda_k=0 (first obstruction vanishing, which prior steps established via EH-direction-in-kernel choice) legitimately hold at the leading order so that the Prop 2.10 formula applies, or does the mixed-chirality assignment spoil lambda_k=0? (4) Is there a genuine risk that nu_l is a per-NODE quantity (each node contributes its own bar-h^4_j, summed in line 641) so that the 'inter-node' language must be interpreted as: node j's source H^4(zeta_j) pairs with the GLOBAL orbifold mode v_l which is delocalized over all four nodes -- meaning the coupling between distinct nodes is mediated by the global obstruction mode v_l, not by a direct node-to-node Green function? Please read the source lines 449-666 carefully and give a precise mathematical assessment of whether the boundary-pairing reduction is correct and what V_{l,2} and v_l concretely are for this product orbifold.

## Output

## Scientific verification memo

**Bibliographic note.** The supplied paper is recorded as arXiv:2012.13316; the proposition and corollary numbering matches the supplied text.

### 1. What Proposition 2.10 actually computes

Fix the compact Einstein orbifold \((M_o,g_o)\), an orthonormal basis
\[
(v_l)_l\subset \mathbf O(g_o)=\ker_{L^2}P_{g_o},
\]
and a singular point \(p_j\). Write in a fixed Bianchi orbifold chart
\[
v_l=V^{(j)}_{l,0}+V^{(j)}_{l,2}+O(r_j^4).
\]
When the three first ALE coefficients \(\lambda_k^j\) vanish, Proposition 2.10 gives the **Fredholm compatibility coefficient**
\[
\nu_l^{(j)}
 =3\int_{\Sigma_j}
   \left\langle H_j^4,V^{(j)}_{l,2}\right\rangle_e\,d\sigma_e,
\qquad
\Sigma_j=S^3/\mathbb Z_2.
\]
For several singular points, linearity gives
\[
\nu_l^{\mathrm{tot}}
 =\sum_j\nu_l^{(j)}
 =3\sum_j\int_{\Sigma_j}
   \left\langle H_j^4,V^{(j)}_{l,2}\right\rangle_e\,d\sigma_e.
\]

Thus, for the coefficient \(\nu_l^{(j)}\) itself, the proposed chirality comparison is correct:
\[
\nu_l^{(j,+)}-\nu_l^{(j,-)}
=
3\int_{\Sigma_j}
\left\langle H_j^4(\zeta_j^+)-H_j^4(\zeta_j^-),
V^{(j)}_{l,2}\right\rangle_e\,d\sigma_e,
\]
provided the plus and minus tensors are transported into the same oriented orbifold chart. With \(g_o\), \(v_l\), and that chart fixed, \(V^{(j)}_{l,2}\) is independent of the ALE filling; the source tensor \(H_j^4\) carries the chirality in this formula.

The angular statement is also correct with one refinement. In Cartesian tensor components, \(H^4\) has scalar spherical harmonic degree \(2\). A homogeneous quadratic \(V_{l,2}\) may contain degree \(0\) and degree \(2\) pieces on \(S^3/\mathbb Z_2\); only its degree-\(2\) component contributes. This is the same eigenspace orthogonality used in the integrations by parts surrounding Proposition 2.10.

### 2. Why this is not generally the pairwise inter-node coefficient

Proposition 2.10 computes projection onto the global kernel \(\mathbf O(g_o)\). It does not compute the regular field generated by a source at \(p_j\) and evaluated at another point \(p_i\).

For one source, the global singular solution has the form
\[
P_{g_o}\bar h_j^4=\sum_l\nu_l^{(j)}v_l,
\qquad
\bar h_j^4\sim H_j^4\quad\text{near }p_j.
\]
At a distinct node \(p_i\), it is smooth and has an expansion
\[
\bar h_j^4
  =A_{ij,0}+A_{ij,2}+O(r_i^4).
\]
The contribution to the first obstruction at \(p_i\) is determined by the curvature jet of \(A_{ij,2}\), together with the coordinate correction from \(A_{ij,0}\), exactly as in the expression
\[
\lambda_k^i
 =c\left\langle
 R^\pm\!\left(\psi(A_{ij,0})_*(H_{i,2}+A_{ij,2})\right)
 \zeta_i^\pm,\zeta_{i,(k)}^\pm
 \right\rangle .
\]
Finding \(A_{ij,2}\) requires the complementary global solution of \(P_{g_o}\), equivalently a projected Green operator or an explicit global construction. The numbers \(\nu_l^{(j)}\) alone do not determine that jet.

Corollary 2.12 is an adjoint reciprocity identity:
\[
\sum_j|\zeta_j|\lambda_1^j(\zeta,v)
 =
 C\sum_l\langle v,v_l\rangle\,\nu_l(\zeta,0)
 +O(\|v\|^2|\zeta|^2).
\]
Here \(v\in\mathbf O(g_o)\) is a global infinitesimal Einstein deformation. The formula relates:

* variation of the **sum** of radial first obstructions under \(v\), and
* projection of the bubble sources onto global zero modes.

It contains neither a separate receiver index \(i\) nor the regular coefficient \(A_{ij,2}\). Therefore it does not identify a general pairwise coefficient \(c_{ij}\) with \(\nu_l^{(j)}\).

The same paper provides a sharp internal comparison: on the flat \(\mathbb T^4/\mathbb Z_2\), the global kernel tensors are constant, hence \(V_{l,2}=0\) and these \(\nu_l\) vanish. Nevertheless Sections 3–4 obtain nonzero bubble-to-bubble curvature interactions through the periodized \(H^4\) field \(B_x^L\). Thus kernel projection and direct inter-node propagation are mathematically distinct objects.

A link-flux representation of \(c_{ij}\) may still be derived by pairing the source at \(j\) with an adjoint singular receiver field centered at \(i\). That receiver field is generally not one of the smooth zero modes \(v_l\).

### 3. The product orbifold: explicit \(\mathbf O(g_o)\) and \(V_{l,2}\)

Take the standard simultaneous half-turn on the two unit spheres, with four fixed points. Let
\[
g_o=g_A+g_B,\qquad \operatorname{Ric}(g_o)=g_o,
\]
and let \(u_A,u_B\) be the invariant height functions on the two factors. The sector formulas in the supplied ledger give the four-dimensional kernel
\[
\mathbf O(g_o)
 =
 \operatorname{span}\{
 u_Ag_A,\ u_Ag_B,\ u_Bg_A,\ u_Bg_B
 \}.
\]
There are no zero modes in the mixed one-form or trace-free tensor sectors. On the quotient, an orthonormal basis can be obtained by multiplying these tensors by
\[
\kappa=\frac{\sqrt3}{4\pi}.
\]

At a node \(p_{\sigma,\tau}\), where
\[
u_A(p_{\sigma,\tau})=\sigma,\qquad
u_B(p_{\sigma,\tau})=\tau,\qquad
\sigma,\tau\in\{\pm1\},
\]
use factorwise stereographic coordinates \(x\in\mathbb R^2\), \(y\in\mathbb R^2\). These are Bianchi coordinates relative to
\[
e=E_A+E_B,
\]
because in dimension two \(B_e(fE_A)=0\) when \(f\) depends only on \(x\), and similarly for \(E_B\). The expansions are
\[
g_A=E_A-\frac12|x|^2E_A+O(r^4),\qquad
g_B=E_B-\frac12|y|^2E_B+O(r^4),
\]
and
\[
u_A=\sigma\left(1-\frac12|x|^2\right)+O(r^4),\qquad
u_B=\tau\left(1-\frac12|y|^2\right)+O(r^4).
\]

Hence one may take
\[
\begin{array}{c|c|c}
v_l&V_{l,0}^{(j)}&V_{l,2}^{(j)}\\ \hline
\kappa u_Ag_A&
\kappa\sigma E_A&
-\kappa\sigma |x|^2E_A\\[2mm]
\kappa u_Ag_B&
\kappa\sigma E_B&
-\dfrac{\kappa\sigma}{2}(|x|^2+|y|^2)E_B\\[2mm]
\kappa u_Bg_A&
\kappa\tau E_A&
-\dfrac{\kappa\tau}{2}(|x|^2+|y|^2)E_A\\[2mm]
\kappa u_Bg_B&
\kappa\tau E_B&
-\kappa\tau |y|^2E_B .
\end{array}
\]

These \(V_{l,2}\) are not the \(H_2\) appearing in
\[
g_o=e+H_2+O(r^4),\qquad P_eH_2=\Lambda e.
\]
For the product metric,
\[
H_2=-\frac12\bigl(|x|^2E_A+|y|^2E_B\bigr),
\qquad
P_eH_2=e,
\]
since \(\Lambda=1\). By contrast, \(V_{l,2}\) is the quadratic Taylor term of a global tensor \(v_l\in\ker P_{g_o}\), and its equation comes from expanding
\[
P_{g_o}v_l=0.
\]
It includes the interaction of \(V_{l,0}\) with the curvature term \(H_2\); it does not satisfy \(P_eV_{l,2}=\Lambda e\). In the displayed basis one finds instead
\[
P_eV_{l,2}=2V_{l,0}.
\]

### 4. A product-specific consequence: the \(\nu_l\) pairings vanish

Use adapted two-form bases with
\[
\omega_1^+=\operatorname{vol}_A+\operatorname{vol}_B,\qquad
\omega_1^-=\operatorname{vol}_A-\operatorname{vol}_B.
\]
For the product curvature,
\[
R^+=\operatorname{diag}(1,0,0),\qquad
R^-=\operatorname{diag}(1,0,0).
\]
Thus the admissible Eguchi–Hanson directions lie in
\[
K^\pm=\operatorname{span}\{\omega_2^\pm,\omega_3^\pm\}.
\]

The trace-free block-difference tensor \(E_A-E_B\) is proportional to
\[
C_{11}=\omega_1^+\circ\omega_1^-.
\]
Every \(V_{l,2}\) displayed above is a scalar function times \(E_A\) or \(E_B\); after removing its total trace, its matrix component is therefore along \(C_{11}\).

For \(\zeta^+\in K^+\),
\[
H^4(\zeta^+)
\in\operatorname{span}\{C_{ab}:a=2,3\},
\]
while for \(\zeta^-\in K^-\),
\[
H^4(\zeta^-)
\in\operatorname{span}\{C_{ab}:b=2,3\}.
\]
Neither family contains \(C_{11}\). Using
\[
\operatorname{tr}(C_{ab}C_{cd})
 =4\delta_{ac}\delta_{bd},
\]
one obtains pointwise
\[
\langle H^4(\zeta^\pm),V_{l,2}\rangle_e=0.
\]
Consequently,
\[
\nu_l^{(j,+)}=\nu_l^{(j,-)}=0
\]
for every node \(j\), every global zero mode \(v_l\), and every Eguchi–Hanson direction in the corresponding curvature kernel.

This is strong evidence that a nonzero mixed-row coefficient on this product orbifold cannot be the difference \(\nu_l(+)-\nu_l(-)\). Such a coefficient must come from the regular complementary field \(A_{ij,2}\), a nonlinear term, or a different receiver pairing.

### 5. The condition \(\lambda_k=0\)

At the undeformed product orbifold,
\[
\lambda_k^j
 =c\left\langle
 R^\pm\zeta_j^\pm,\zeta_{j,(k)}^\pm
 \right\rangle.
\]
Because both \(R^+\) and \(R^-\) have the two-dimensional kernels above, choosing
\[
\zeta_j^\pm\in K^\pm
\]
makes all three \(\lambda_k^j\) vanish exactly. Assigning plus chirality at some nodes and minus chirality at others does not alter this local fact.

After adding the regular field produced by another bubble, the curvature jet at the receiving node changes, and the resulting first-order change in \(\lambda_k^i\) is precisely part of the desired inter-node interaction. Thus the hypothesis \(\lambda_k^j(\zeta,0)=0\) is valid for applying Proposition 2.10 to the undeformed source problem, but it does not make the induced receiver coefficient vanish automatically.

### 6. Per-node interpretation

Yes, \(\nu_l^{(j)}\) is naturally attached to a source node \(j\), and the paper sums these contributions. It measures how the singular source at \(j\) pairs with the local quadratic jet, at that same node, of a global delocalized zero mode \(v_l\).

There are therefore two distinct propagation mechanisms:

1. **Finite-dimensional zero-mode projection**
   \[
   H_j^4\longmapsto \nu_l^{(j)}.
   \]
   This can couple several nodes after the global deformation parameters are solved for.

2. **Complementary global propagation**
   \[
   H_j^4\longmapsto \bar h_j^4
   \longmapsto A_{ij,2}
   \longmapsto \lambda_k^i.
   \]
   This is the direct pairwise interaction and retains the projected inverse of \(P_{g_o}\).

For the product orbifold and curvature-kernel Eguchi–Hanson directions, the first mechanism gives zero by the explicit \(C_{ab}\) computation above. The second mechanism remains the relevant object for a nonzero \(c_{\mathrm{opp}}-c_{\mathrm{same}}\).

Finally, Corollary 2.12 also uses the integrability assumption from Definition 1.10 to produce the Einstein family \(g_v\). The supplied sector calculation establishes the four-dimensional kernel, but it does not establish nonlinear integrability of all four modes. The two modes \(u_Ag_A\) and \(u_Bg_B\) are pure diffeomorphism directions since
\[
\mathcal L_{\nabla u_A}g_o=-2u_Ag_A,\qquad
\mathcal L_{\nabla u_B}g_o=-2u_Bg_B.
\]
The two cross modes require a separate Kuranishi computation before Corollary 2.12 can be applied to arbitrary \(v\in\mathbf O(g_o)\). Proposition 2.10’s linear flux formula itself remains well-defined.