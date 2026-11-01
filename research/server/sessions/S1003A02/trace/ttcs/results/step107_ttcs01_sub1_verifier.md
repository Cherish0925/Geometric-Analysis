# TTCS Independent Branch Record

```json
{
  "step_id": 107,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step107_einstein_end_constraints_D4_object_and_specification.md",
    "Sessions/S1003A02/workspace/notes/step106_independent_cap_charge_and_D4_candidate.md",
    "Sessions/S1003A02/workspace/scripts/step107_cusp_end_constraints.py",
    "Sessions/S1003A02/workspace/data/step107/cusp_end_constraints.json",
    "Sessions/S1003A02/workspace/data/step106/D4_cap_ledger.json",
    "Knowledge/objects/papers/Hitchin-Thorpe-Inequality-for-Noncompact-Einstein-4--fd6e60eeeaa2--deedf5d03a5f/object.md"
  ]
}
```

## Task

Independently verify the new mathematics in notes/step107_einstein_end_constraints_D4_object_and_specification.md, grounded in the Step-106 note, the Step-107 script and its JSON output, and Dai-Wei. Check in particular: (1) Theorem 107.A: for an Einstein metric C^2-asymptotic to a circle-fibred cusp dr^2+g_B+e^{-2 kappa r} f^2 eta^2, is it correct that lambda=-kappa^2, f is constant (momentum constraint Ric(d_r, horizontal)=kappa*Yf/f) and K_B=lambda, so the base must be hyperbolic? Are there known Einstein examples contradicting this (e.g. complex hyperbolic, H^2xH^2, Biquard/Hitchin-type metrics)? Is the C^2 hypothesis implied by Dai-Wei's rescaled-tangent-bundle asymptotics? (2) Corollary 107.A': the cap charge formula c_+=T_+(C)+e-3 sign e with the stated orientation, genus independence via Dai-Wei Thm 5.1, and the exclusion of single disc-bundle caps over genus g>=2 via c_+=4-4g+e and the adjunction inequality (b_+(X)>=2). (3) Theorem 107.B (no finite-volume U(2)-invariant ends on S^3/Gamma with bounded curvature and G(nu,nu)>=0): check Lemma 107.B1 (Riccati bounds, second-largest-scale lower bound from r_i+r_j=4(x_i+x_j-x_k)/(x_i x_j)), the sign-case argument, and whether left-quotients S^3/Gamma with biaxial metrics are correctly covered. (4) Proposition 107.C triaxial argument. (5) Section 4: the Freedman homeomorphism claim for N_D4 union W (simple connectivity by van Kampen, form -I_4, orientation matching of the boundary S^3/Q8), and the orbifold reformulation with H_2(underlying)=Z_2. (6) Whether the stated consequences for the third nonattained-zero subchannel are exactly supported. Report errors with corrected statements, and any strengthening (e.g. a symmetry-free version of 107.B) that is genuinely provable.

## Output

# Independent verification memo

## Overall assessment

The tensor calculations behind Theorems 107.A–107.C are sound. The main substantive correction is that Dai–Wei’s rescaled-tangent-bundle asymptotics do **not** by themselves imply the relative \(C^2\) convergence assumed in 107.A. Thus 107.A is valid as stated, but 107.A′ does not yet apply to every Dai–Wei fibred cusp without an additional Einstein regularity argument.

The cap-charge formula, the smooth-surface disc-bundle exclusion, Theorem 107.B, and Proposition 107.C are mathematically consistent. The Freedman conclusion for \(N_{D4,\mathrm{trunc}}\cup W\) is also correct from the stated topology. The “minimal \(D_4\) resolution” phrasing and the “if and only if all three conditions hold” phrasing require additional relative smooth and analytic input.

---

## 1. Theorem 107.A

### 1.1 Leading Ricci tensor

Put
\[
u(r,b)=e^{-\kappa r}f(b),\qquad
g_0=dr^2+g_B+u^2\eta^2.
\]
Ignoring the connection curvature for one moment, this is a one-dimensional warped extension of \(dr^2+g_B\). The standard warped formulas give
\[
\operatorname{Ric}_{g_0}(\partial_r,\partial_r)
=-u^{-1}\partial_r^2u=-\kappa^2,
\]
and, for \(Y\in TB\),
\[
\operatorname{Ric}_{g_0}(\partial_r,\widehat Y)
=-u^{-1}\operatorname{Hess}u(\partial_r,Y)
=\kappa\,Y(\log f).
\]
This agrees with the exact \(\kappa=1\) SymPy output
\[
\operatorname{Ric}(\partial_r,\widehat{\partial_x})=\frac{f_x}{f}.
\]

Before \(f\) is known to be constant, the horizontal component is
\[
\operatorname{Ric}_{g_0}|_{TB}
=
K_Bg_B-f^{-1}\operatorname{Hess}_Bf
+O(e^{-2\kappa r}),
\]
while the curvature \(d\eta\) contributes through the O’Neill tensor with squared size
\[
u^2|d\eta|_{g_B}^2=O(e^{-2\kappa r}).
\]
Thus the connection does not alter the limiting equations.

If
\[
\sum_{j=0}^2|\nabla_{g_0}^j(g-g_0)|_{g_0}\longrightarrow0,
\]
then
\[
|\operatorname{Ric}_g-\operatorname{Ric}_{g_0}|_{g_0}\longrightarrow0.
\]
The Einstein equation therefore yields, successively,
\[
\lambda=-\kappa^2,\qquad
Yf=0,\qquad
K_B=\lambda.
\]
Hence \(f\) is constant and \(B\) has constant curvature \(-\kappa^2\). For an orbifold base,
\[
2\pi\chi^{\mathrm{orb}}(B)
=\int_BK_B\,dA
=\lambda\,\operatorname{Area}(B)<0.
\]

So Theorem 107.A is correct under its stated relative \(C^2\) hypothesis. In fact, its proof only needs
\[
g-g_0=o(1),\qquad
\operatorname{Ric}_g-\operatorname{Ric}_{g_0}=o(1)
\]
in a \(g_0\)-orthonormal frame.

### 1.2 Relation to Dai–Wei asymptotics

Dai–Wei Definition 3.1 permits a perturbation \(a=xa_1\) in the fibred metric before conformal rescaling. In a local fibre coordinate \(\theta\) and horizontal coordinate \(y\), one may take
\[
a_1=q(\theta)\left(\frac{dy}{x}\right)^2.
\]
After passing to the cusp metric, this produces a horizontal perturbation
\[
xq(\theta)\,dy^2.
\]
But the cusp-unit vertical vector is \(x^{-1}\partial_\theta\), and therefore
\[
\nabla_{x^{-1}\partial_\theta}
\bigl(xq(\theta)\,dy^2\bigr)
\sim q'(\theta)\,dy^2,
\]
which need not tend to zero. A second vertical derivative can be larger still. Consequently, smooth decay in the rescaled bundle does not imply physical relative \(C^1\), much less relative \(C^2\), convergence.

This example is not Einstein; it demonstrates the logical difference between the two asymptotic notions. To obtain 107.A′ from Dai–Wei’s definition, one needs an additional theorem showing that the Einstein equation removes such fibre-dependent coefficients, or one must include the relative Ricci/\(C^2\) convergence as a separate hypothesis.

### 1.3 Named examples

- A quotient of \(\mathbb H^2_{-\kappa^2}\times\mathbb H^2_{-\kappa^2}\), with a cusp in one factor and a compact quotient in the other, is an exact example:
  \[
  dr^2+g_B+e^{-2\kappa r}d\theta^2,
  \qquad K_B=-\kappa^2.
  \]
  It confirms the theorem.

- A standard complex-hyperbolic cusp has several shrinking directions, with different radial weights on the horizontal and central directions of its Heisenberg cross-section. It is not a fixed two-dimensional base with only an \(S^1\) fibre shrinking.

- Real-hyperbolic cusps shrink the entire three-dimensional cross-section and likewise lie outside this model.

- The usual Biquard/Hitchin conformally compact or ACH families have expanding conformal ends rather than finite-volume fixed-base fibred cusps.

Thus none of these supplies a counterexample to 107.A. The broad literature statement that no other example exists is not established by the supplied sources.

---

## 2. Corollary 107.A′ and cap charges

### 2.1 Orientation and the Dai–Wei eta term

Let \(e=e_C\) be the Euler number computed using the orientation induced on \(\partial C\). Dai–Wei Theorem 5.1 gives
\[
\mathcal H^\infty
=\frac12\,a\!-\!\lim\eta
=\frac e3-\operatorname{sign}e.
\]
Theorem 3.5 gives vanishing Euler transgression. Hence
\[
\mathcal Q_+(\partial C)
=-3\mathcal H^\infty
=-e+3\operatorname{sign}e.
\]
For a cap sequence with \(\widehat P(C)\to0\), Theorem G gives
\[
c_+(C)
=T_+(C)-\mathcal Q_+(\partial C)
=T_+(C)+e-3\operatorname{sign}e.
\]
Thus (107.1) is correct. If the same link is oriented outward from \(\Omega\), both its orientation and the signed Euler number reverse, giving the same final cap formula.

Genus independence also follows exactly from Dai–Wei: in base dimension two, only the degree-zero part of \(L(TB)\) contributes, and
\[
\left(\frac1{\tanh e}-\frac1e\right)_{[2]}=\frac e3.
\]

### 2.2 Disc-bundle calculation

For \(C=D_e(\Sigma_g)\),
\[
\chi(C)=2-2g,\qquad
\tau(C)=\operatorname{sign}e,
\]
with \(\tau=0\) when \(e=0\). Therefore
\[
T_+(C)=4-4g+3\operatorname{sign}e,
\]
and
\[
\boxed{c_+(C)=4-4g+e}.
\]

For \(g\ge2\):

- if \(e\le0\), then \(c_+<0\), incompatible with its realization as a limit of the \(C_+\)-curvature integral;
- if \(e>0\), then \(c_+\ge0\) requires
  \[
  e\ge4g-4.
  \]

For the embedded zero section \(\Sigma\subset X\#k\overline{\mathbb{CP}}^2\), the Seiberg–Witten adjunction inequality gives
\[
2g-2\ge [\Sigma]^2+|L\cdot[\Sigma]|
\ge e,
\]
using \(b_+(X)\ge2\) and a stated blow-up basic class \(L\). This contradicts \(e\ge4g-4\).

Hence the exclusion of an ordinary smooth disc-bundle cap over \(\Sigma_g\), \(g\ge2\), is correct. This argument does not automatically treat Seifert orbifold bases; an orbifold cap would require the corresponding orbifold intersection and adjunction calculation.

The finite search in the JSON is consistent with the formula, while the general exclusion comes from the two symbolic inequalities above, not from the finite table.

### 2.3 Corrected form of 107.A′

A fully supported statement is:

> If an Einstein end has the relative Ricci or relative \(C^2\) asymptotics of 107.A, then its smooth fixed base has genus \(g\ge2\), and no cap consisting of one ordinary disc bundle \(D_e(\Sigma_g)\) can occur under the stated Seiberg–Witten hypotheses.

Replacing the relative \(C^2\) assumption solely by Dai–Wei’s rescaled smoothness is not yet justified.

---

## 3. Theorem 107.B

### 3.1 Lemma 107.B1

For
\[
\lambda_i=\frac{a_i'}{a_i},
\qquad
K(\partial_t,e_i)=-(\lambda_i'+\lambda_i^2),
\]
the curvature bound gives
\[
\lambda_i'=-\lambda_i^2+O(K).
\]
A value below \(-\sqrt K\) is driven to \(-\infty\) in finite forward time by Riccati comparison, contradicting positivity of \(a_i\) on the complete product end. Values above \(\sqrt K\) cannot increase past the maximum of their initial value and \(\sqrt K\). Thus \(|\lambda_i|\le\Lambda\) on a tail.

Order \(x_1\ge x_2\ge x_3\), where \(x_i=a_i^2\). The script correctly verifies
\[
r_1+r_2
=\frac{4(x_1+x_2-x_3)}{x_1x_2}
\ge \frac4{x_2}.
\]
The Gauss equation gives
\[
\operatorname{Ric}_\Sigma(e_i,e_i)
=
\operatorname{Ric}_g(e_i,e_i)
-K(e_i,\nu)+\lambda_iH-\lambda_i^2.
\]
Every term on the right is bounded, so \(r_1+r_2\) is bounded above. Consequently \(x_2\ge b_0^2>0\). The second-largest orbit scale therefore stays uniformly positive. Lemma 107.B1 is correct.

### 3.2 Finite volume and the two sign cases

Since \(|(\log v)'|\le3\Lambda\) and \(\int v\,dt<\infty\), one has \(v\to0\). In the biaxial case \(v=a^2c\), and the second-largest scale is always \(a\); hence
\[
a\ge b_0,\qquad c\to0.
\]

The Hamiltonian identity and \(G(\nu,\nu)\ge0\) give
\[
\lambda_a(\lambda_a+2\lambda_c)
=\sigma_2
\ge \frac12s_\Sigma
=\frac4{a^2}-\frac{c^2}{a^4}>0
\]
on a tail. Therefore \(\lambda_a\) has a fixed nonzero sign.

If \(\lambda_a>0\), then \(\lambda_a+2\lambda_c>0\), and
\[
(\log v)'
=2\lambda_a+\lambda_c
=\frac32\lambda_a+\frac12(\lambda_a+2\lambda_c)>0,
\]
contradicting \(v\to0\).

If \(\lambda_a<0\), then \(a\) decreases. Once \(c\le a\),
\[
\sigma_2\ge\frac3{a^2}
\ge\frac3{a(t_2)^2}.
\]
Since \(|\lambda_a+2\lambda_c|\le3\Lambda\),
\[
|\lambda_a|
\ge\frac1{a(t_2)^2\Lambda},
\]
so \(a\) decays exponentially, contradicting \(a\ge b_0\).

Theorem 107.B is therefore correct.

### 3.3 Quotient and symmetry wording

Because the \(\sigma_i\) are left-invariant, the metric descends to
\[
\Gamma\backslash SU(2)
\]
for \(\Gamma\subset SU(2)\) acting on the left. This includes the one-sided cyclic, quaternionic, prism, and binary-polyhedral space forms listed in the note.

For a nonnormal \(\Gamma\), a global \(U(2)\) action on the quotient need not descend. The precise title is therefore:

> no finite-volume biaxial Bianchi IX end on a one-sided spherical space form, equivalently no such end whose lift to \(S^3\) is \(U(2)\)-invariant.

The local proof and all conclusions are unchanged.

### 3.4 Finite-energy strengthening

The supplied Cheeger–Tian estimate yields a useful corollary already implicit in Step 107. If a complete Einstein tail has finite \(L^2\) curvature, then its tail energy tends to zero. Unit balls sufficiently far out have energy below the Cheeger–Tian threshold, hence
\[
|\operatorname{Rm}|\le C
\]
there. Thus the explicit bounded-curvature assumption in 107.B can be replaced, for the intended application, by finite total curvature energy.

---

## 4. Proposition 107.C

Assume \(\sigma_2\ge\delta>0\) on a tail. Since
\[
H^2-3\sigma_2
=\frac12\bigl[(\lambda_1-\lambda_2)^2
+(\lambda_2-\lambda_3)^2
+(\lambda_3-\lambda_1)^2\bigr]\ge0,
\]
\(H\) never vanishes and has constant sign. Finite volume gives \(v\to0\), so \(H>0\) is impossible.

Suppose \(H<0\). For \(u=\lambda_i+\lambda_j\ge0\), with \(\lambda_k=H-u\),
\[
\sigma_2
=\lambda_i\lambda_j+\lambda_ku
\le\frac{u^2}{4}+(H-u)u
=Hu-\frac34u^2\le0,
\]
contradicting \(\sigma_2>0\). Hence every pair sum is \(<0\).

With \(|\lambda_k|\le\Lambda\),
\[
\delta\le\sigma_2
\le \frac{u^2}{4}+\Lambda|u|,
\]
so every \(|u|\) is bounded below by a positive constant. Therefore every pair product \(a_ia_j\) decays exponentially. In particular, the product of the two largest scales tends to zero, forcing the second-largest scale to tend to zero, contrary to Lemma 107.B1.

This proves the main triaxial statement.

For \(\operatorname{Ric}=-3g\),
\[
G(\nu,\nu)=3,\qquad
\sigma_2=\frac12s_\Sigma+3,
\]
so \(\liminf s_\Sigma>-6\) is exactly the required strict lower estimate. Ordering \(a_1\ge a_2\ge a_3\),
\[
s_\Sigma\ge\frac4{a_2^2}
-2\frac{(a_1^2-a_2^2)^2}{a_1^2a_2^2a_3^2}.
\]
Thus
\[
\limsup
\frac{(a_1^2-a_2^2)^2}
{a_1^2a_2^2a_3^2}<3
\]
implies \(\liminf s_\Sigma>-6\). Proposition 107.C is correct. “Anisotropy \(<\sqrt3\)” should mean explicitly
\[
\frac{|a_1^2-a_2^2|}{a_1a_2a_3}<\sqrt3
\]
asymptotically, after the \(\operatorname{Ric}=-3g\) normalization.

No symmetry-free extension follows from these calculations alone. Such an extension needs a foliation whose second fundamental form is controlled and whose two horizontal directions remain uniformly noncollapsed; neither object is produced by the supplied material.

---

## 5. The \(D_4\) topological object

### 5.1 The closed union \(M_4=N_{\mathrm{trunc}}\cup W\)

The van Kampen calculation is correct:
\[
\pi_1(N)=1,\qquad
\pi_1(W)=\mathbb Z_2,
\]
and
\[
Q_8=\pi_1(S^3/Q_8)\longrightarrow\pi_1(W)
\]
is onto. Since the same gluing group maps trivially into \(\pi_1(N)\), its image kills all of \(\pi_1(W)\), giving
\[
\pi_1(M_4)=1.
\]

Also
\[
\chi(M_4)=5+1=6,\qquad
\tau(M_4)=-4.
\]
Hence \(b_2=4\), \(b_+=0\), and \(b_-=4\). Mayer–Vietoris gives
\[
H_2(N)\hookrightarrow H_2(M_4)
\]
with quotient of order two, because
\[
\ker\!\left(
H_1(S^3/Q_8)=(\mathbb Z_2)^2
\to H_1(W)=\mathbb Z_2
\right)\cong\mathbb Z_2.
\]
Thus the \(D_4\) lattice sits with index two.

There is also a direct strengthening: since \(M_4\) is smooth, closed, simply connected, and all four intersection-form eigenvalues are \(<0\), Donaldson’s theorem gives
\[
Q_{M_4}\cong -I_4.
\]
Freedman’s theorem, together with vanishing Kirby–Siebenmann class for a smooth manifold, then gives
\[
M_4\cong_{\mathrm{homeo}}
\#4\overline{\mathbb{CP}}^2.
\]
This part of Section 4 is correct.

Choosing the orientation of \(W\) oppositely to the induced orientation on the end of \(N\) supplies the required oriented gluing. No extra numerical sign enters the intersection calculation because \(H_2(W)=0\).

### 5.2 The cone-filled orbifold

Let
\[
V_Q=W\cup c(S^3/Q_8).
\]
Van Kampen gives \(\pi_1(V_Q)=1\). The Mayer–Vietoris segment is
\[
0\longrightarrow H_2(V_Q)
\longrightarrow(\mathbb Z_2)^2
\longrightarrow\mathbb Z_2
\longrightarrow0,
\]
so
\[
H_2(V_Q;\mathbb Z)\cong\mathbb Z_2.
\]
Moreover \(H_4(V_Q)=\mathbb Z\) and the other reduced rational homology groups vanish. Hence its underlying space is a rational homology \(4\)-sphere but not a homotopy \(4\)-sphere. This computation is correct.

The phrase “minimal \(D_4\) resolution” additionally uses a relative identification of \(N_{\mathrm{trunc}}\) with the standard \(D_4\) plumbing resolving \(\mathbb R^4/Q_8\). Step 106 supplies the lattice, fundamental group, and end, but not a relative Kirby diagram establishing that identification. Accordingly:

- if \(N_{\mathrm{trunc}}\) is identified relative to \(S^3/Q_8\) with the standard \(D_4\) plumbing, then the orbifold reformulation is equivalent to (D4-1);
- without that relative identification, the phrase “minimal resolution” contains extra smooth information.

Similarly, a concrete Kirby sequence could establish (D4-1), but no such sequence appears in the supplied files.

### 5.3 Status of (D4-1)–(D4-3)

The charge ledger is internally consistent:
\[
(\chi,\tau)=(5,-4),\qquad
C_+=0,\qquad C_-=20,
\]
and therefore
\[
\int|W^-|^2=40\pi^2.
\]
The D4-ALF end and the Hopf outer link have matching pairs \((-2,2)\), so Theorem G imposes no residual chiral charge on \(Z=W\setminus B^4\). This is a necessary compatibility, not a construction of \(h_i\).

The statement that the architecture is realized “if and only if” (D4-1)–(D4-3) all hold is stronger than the supplied analysis. Even their joint validity would still require a one-parameter gluing construction with:

\[
\widehat P(g_i)\to0,\qquad
\text{scalar-fluctuation term}\to0,
\]
compatible collar scales, total-volume control, and the intended topology of the closed metrics. Conversely, these three items are necessary only relative to this chosen D4-ALF/\(W\) architecture, not for every possible four-class degeneration.

A precise supported formulation is:

> (D4-1) and (D4-2) describe a topologically and charge-compatible four-class cap proposal; (D4-3) describes a possible Einstein host. An actual near-Einstein sequence requires a further global gluing theorem with curvature and volume estimates.

---

## 6. Consequences for the third zero-infimum channel

The following conclusions are supported:

1. Under relative \(C^2\) or relative Ricci asymptotics, a fixed-base circle-fibred Einstein cusp has hyperbolic base.
2. Ordinary single disc-bundle caps over smooth bases of genus \(g\ge2\) are excluded by
   \[
   c_+=4-4g+e
   \]
   together with adjunction.
3. Finite-energy biaxial Bianchi IX ends on one-sided spherical space forms cannot have finite volume.
4. The same holds for triaxial ends satisfying
   \[
   \liminf\sigma_2>0,
   \]
   in particular under the displayed small-anisotropy estimate.
5. The D4-ALF/\(W\) object passes all currently computed topology and two-chirality charge identities.
6. Complex- and real-hyperbolic cusps with shrinking base directions are untouched by 107.A–107.C.
7. Multi-surface caps over hyperbolic-base links are not classified by the present argument.

The following statements need revised wording:

- “Every Dai–Wei fibred cusp has hyperbolic base” needs the extra relative Ricci/\(C^2\) result discussed above.
- “No finite-volume \(U(2)\)-invariant end on \(S^3/\Gamma\)” should refer to an end whose lift is biaxial \(U(2)\)-invariant.
- “No example of any kind is known” is a literature-status statement not documented by the supplied papers.
- The symmetry-free Hopf-end exclusion remains unresolved by the present equations.
- The specification appendix is appropriately labeled as a research target. Its observations about chiral invisibility are supported by \(C_+=0\), \(C_-=20\), but the assertion that every future smooth relation must literally contain \(W^-\) or separate field data is heuristic; another invariant could encode the same information indirectly.

The strongest immediately available additions are the finite-energy replacement for bounded curvature in 107.B/107.C and the Donaldson derivation of \(Q_{M_4}\cong-I_4\).