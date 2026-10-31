# TTCS Independent Branch Record

```json
{
  "step_id": 39,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex",
    "Skills/geometric-analysis/research/paper/sections/field_interfaces_and_curvature_interactions.tex",
    "Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md",
    "Knowledge/objects/papers/Ricci-Curvature-Minimal-Volumes-and-Seiberg-Witten-Theory--995c93498a8f--cab40be18df4/object.md",
    "Knowledge/objects/papers/Four-Manifolds-Curvature-Bounds-and-Convex-Geometry--9dec43e67dff--ae37fe317499/object.md"
  ]
}
```

## Task

Check the gauge-theoretic quantifiers needed to apply the amplitude identity on arbitrary metrics and near-minimizing sequences. For the full blow-up sign family a_epsilon=c+sum epsilon_i E_i on M=X#k CPbar^2, distinguish: nonzero perturbed Seiberg-Witten invariant, monopole class, existence of an unperturbed solution for a fixed metric, irreducibility/reducibility, b^+>=2 versus b^+=1 chambers, and the role of a_epsilon^2=A-k>0 in the low-blow-up range. Decide whether the amplitude theorem genuinely holds for every scalar-negative metric in the chamber-independent range via LeBrun's limiting argument, whether reducibles can occur when A-k>0, and what exact hypotheses must be stated elsewhere. Also test whether simultaneous choice of all 2^k solutions requires any compatibility beyond individual existence. Give a precise corrected theorem statement and sequence corollary.

## Output

## Scientific memo: gauge-theoretic quantifiers behind the amplitude identity

### 1. The relevant logical chain

For a fixed Spin\(^c\) structure \(\mathfrak s\), the following are distinct statements.

1. **A Seiberg–Witten invariant is nonzero.**  
   This is a count or cohomological pairing formed from moduli spaces for generic perturbed equations. It initially gives solutions for regular generic metric–perturbation pairs in the relevant parameter component.

2. **Its determinant class is a monopole class.**  
   In the all-metric sense used in LeBrun’s 2006 paper, this means
   \[
   \forall g\quad \exists (\mathcal A,\Phi)\quad
   D_{\mathcal A}\Phi=0,\qquad F_{\mathcal A}^{+}=2i\sigma(\Phi),
   \]
   after the harmless spinor rescaling associated with the factor \(2\).

3. **The unperturbed equations have a solution for one fixed metric.**  
   This is only an existence statement at that metric.

4. **The solution is irreducible.**  
   This additionally means \(\Phi\not\equiv0\). The definition of a monopole class itself permits reducible solutions.

When \(b^{+}(M)\ge2\), a nonzero Seiberg–Witten invariant is independent of polarization and supplies an all-metric monopole class. For an arbitrary fixed metric \(g\), take regular perturbations \(\eta_n\to0\). The invariant being nonzero makes every corresponding regular moduli space nonempty. Abelian gauge compactness, the Weitzenböck bound, and elliptic regularity give a subsequence converging modulo gauge to a smooth unperturbed solution for \(g\). This is the limiting argument implicit in LeBrun 2001, Definition 1 and its surrounding discussion, and explicit in the modern all-metric terminology of LeBrun 2006, Definition 3.1.

Thus, in the chamber-independent setting,
\[
SW(\mathfrak s_\epsilon)\ne0\ \text{for every }\epsilon
\quad\Longrightarrow\quad
\forall g\;\forall\epsilon\;\exists(\mathcal A_\epsilon,\Phi_\epsilon).
\]
Because the sign set is finite, this is equivalent to
\[
\forall g\;\exists\bigl((\mathcal A_\epsilon,\Phi_\epsilon)\bigr)_
{\epsilon\in\{\pm1\}^{k}}.
\]
No regularity of the unperturbed moduli space and no genericity of \(g\) are involved in the last statement.

For
\[
M=X\#k\overline{\mathbf{CP}}^{\,2},\qquad
a_\epsilon=c+\sum_{i=1}^{k}\epsilon_iE_i,
\]
the standard blow-up theorem supplies Spin\(^c\) structures
\(\mathfrak s_\epsilon\), not merely real cohomology classes. This distinction matters if \(H^{2}(M;\mathbb Z)\) has \(2\)-torsion, since a determinant class by itself may not identify the Spin\(^c\) structure.

In the pure blow-up case,
\[
a_\epsilon^{2}=A-k=(2\chi+3\tau)(M),
\]
so every \(\mathfrak s_\epsilon\) has expected dimension
\[
d(\mathfrak s_\epsilon)
 =\frac{a_\epsilon^{2}-(2\chi+3\tau)(M)}4=0.
\]
Here the relevant invariant is the ordinary numerical Seiberg–Witten invariant.

---

### 2. Reducibles when \(A-k>0\)

A reducible unperturbed solution has \(\Phi\equiv0\), hence
\[
F_{\mathcal A}^{+}=0.
\]
Writing \(f=-iF_{\mathcal A}\), with \([f/(2\pi)]=a_\epsilon\), Chern–Weil gives
\[
4\pi^{2}a_\epsilon^{2}
 =\|f^{+}\|_{2}^{2}-\|f^{-}\|_{2}^{2}
 =-\|f^{-}\|_{2}^{2}\le0.
\]
Therefore
\[
a_\epsilon^{2}=A-k>0
\quad\Longrightarrow\quad
\text{every unperturbed solution is irreducible.}
\]

This conclusion is metric-independent and does not use the scalar curvature. It also shows that a compactness limit of perturbed solutions cannot become reducible in the low-blow-up regime.

The positivity \(A-k>0\) is not required for the algebraic simultaneous-field identity once actual solutions have been chosen. Its principal roles are:

- irreducibility of every exact solution;
- exclusion of an unperturbed wall when \(b^{+}=1\);
- a direct proof that every conformal class has Yamabe constant \(<0\), because a Yamabe metric with scalar curvature \(\ge0\) would force a reducible solution.

---

### 3. The \(b^{+}=1\) chamber issue

For \(b^{+}=1\), the phrase “the Seiberg–Witten invariant is nonzero” is incomplete unless the chamber is named. A nonzero invariant in one chamber does not by itself produce an exact solution at metrics whose zero perturbation belongs to the other chamber.

If \(a_\epsilon^{2}=A-k>0\), then for every metric
\[
(a_{\epsilon,g}^{+})^{2}
 =a_\epsilon^{2}+\|a_{\epsilon,g}^{-}\|^{2}
 \ge A-k>0.
\]
Hence \((g,0)\) never lies on the wall \(a_{\epsilon,g}^{+}=0\). After choosing a component of the positive cone, the unperturbed pairs \((g,0)\) remain in one chamber as \(g\) varies.

Moreover,
\[
c\cdot a_\epsilon=A>0,\qquad c^{2}=A>0,\qquad a_\epsilon^{2}>0,
\]
so all \(a_\epsilon\) lie in the same positive-cone component as \(c\). The chamber choice can therefore be made coherently across the entire sign family.

Consequently, the all-metric conclusion also holds for \(b^{+}=1\) provided that, for every \(\epsilon\), the invariant is known to be nonzero in the chamber containing the zero-perturbation pairs \((g,0)\). Positivity of \(A-k\) removes wall crossing along those pairs, but it does not by itself compute the chamber invariant. The blow-up formula must be invoked in the named chamber.

For statements intended to avoid chamber bookkeeping, \(b^{+}\ge2\) is the clean hypothesis.

---

### 4. Which scalar-curvature hypothesis is actually used

The limiting Seiberg–Witten argument gives an unperturbed solution for **every smooth metric**, independently of its scalar curvature.

The clean amplitude formula with \(2-\rho_\epsilon\), however, is tied to
\[
s_g\equiv-4.
\]
For the normalization
\[
D_{\mathcal A}\Phi=0,\qquad F_{\mathcal A}^{+}=2i\sigma(\Phi),
\qquad \rho=|\Phi|^{2},
\]
the Weitzenböck identity is
\[
0=4\int|\nabla_{\mathcal A}\Phi|^{2}
  +\int s\rho+2\int\rho^{2}.
\]
At \(s=-4\), the maximum principle and integration give
\[
0\le\rho\le2,\qquad
K:=\int|\nabla_{\mathcal A}\Phi|^{2}
 =\frac12\int\rho(2-\rho).
\]

Thus:

- if \(g\) has constant scalar curvature \(<0\), a homothety puts it in the form \(s=-4\), and the stated amplitude formula applies;
- if \(s_g(x)<0\) but is not constant, exact solutions still exist, but the polynomial identity involving \(2-\rho\) is not the same;
- if \(g\) is replaced by its Yamabe representative and then normalized to \(s=-4\), the amplitude formula applies to that representative, not to the original metric.

This is exactly the situation for the selected near-minimizing metrics: the metric is first replaced by its Yamabe representative and normalized, and the all-metric monopole supply is then applied to the resulting \(g_j\).

---

### 5. Corrected amplitude theorem

**Theorem — full-sign amplitude identity.**  
Let
\[
M=X\#k\overline{\mathbf{CP}}^{\,2},\qquad
c^{2}=A,\qquad
c\cdot E_i=0,\qquad E_i\cdot E_m=-\delta_{im}.
\]
For each \(\epsilon\in\{\pm1\}^{k}\), fix a Spin\(^c\) structure
\(\mathfrak s_\epsilon\) with determinant class
\[
a_\epsilon=c+\sum_i\epsilon_iE_i.
\]
Assume either:

1. every \(\mathfrak s_\epsilon\) defines an all-metric monopole class; or
2. \(b^{+}(M)\ge2\) and \(SW(\mathfrak s_\epsilon)\ne0\) for every \(\epsilon\).

Let \(g\) be any smooth metric on \(M\) with \(s_g=-4\). Then one may choose, independently for every \(\epsilon\), a smooth unperturbed solution
\[
D_{\mathcal A_\epsilon}\Phi_\epsilon=0,\qquad
F_{\mathcal A_\epsilon}^{+}=2i\sigma(\Phi_\epsilon).
\]
Put
\[
\rho_\epsilon=|\Phi_\epsilon|^{2},\qquad
f_\epsilon=-iF_{\mathcal A_\epsilon},\qquad
\zeta_\epsilon=
 \langle\Phi_\epsilon,\nabla_{\mathcal A_\epsilon}\Phi_\epsilon\rangle,
\]
and define the Walsh components
\[
f_I=2^{-k}\sum_{\epsilon}
 \left(\prod_{i\in I}\epsilon_i\right)f_\epsilon.
\]
Also set
\[
\psi_\epsilon=2\sqrt2\,\sigma(\Phi_\epsilon),\qquad
W_{0,\epsilon}
 =\frac14\left(\frac{\rho_\epsilon^{2}}3\operatorname{Id}
                     -\psi_\epsilon\otimes\psi_\epsilon\right),
\]
and
\[
b(t)=\frac{-t^{2}+8t+2}{6}.
\]
Then \(0\le\rho_\epsilon\le2\), and
\[
\boxed{
P(g)-8\pi^{2}k
 +4\mathbb E_\epsilon\int_M(2-\rho_\epsilon)\,d\mu_g
 =\mathcal B(g,\boldsymbol\Phi),
}
\]
where
\[
\begin{aligned}
\mathcal B={}&
 2\|f_\varnothing^{-}\|_{2}^{2}
 +2\sum_{I\ne\varnothing}\|f_I^{+}\|_{2}^{2}\\
&+\mathbb E_\epsilon\left[
 8\|\zeta_\epsilon\|_{2}^{2}
 +4\|W^{+}-W_{0,\epsilon}\|_{2}^{2}
 +\int_M\bigl(b(\rho_\epsilon)+2\bigr)
                 (2-\rho_\epsilon)^{2}\,d\mu_g
 \right]\ge0.
\end{aligned}
\]
In particular,
\[
\boxed{
P(g)\ge8\pi^{2}k
 -4\mathbb E_\epsilon\int_M(2-\rho_\epsilon)\,d\mu_g.
}
\]

If \(A-k>0\), every solution appearing above is irreducible.

#### Derivation of the coefficient four

The previously established simultaneous-field identity is
\[
P-8\pi^{2}k=\mathscr A-4\mathbb E_\epsilon K_\epsilon.
\]
At \(s=-4\),
\[
K_\epsilon
 =\frac12\int\rho_\epsilon(2-\rho_\epsilon).
\]
Writing \(x_\epsilon=2-\rho_\epsilon\),
\[
4K_\epsilon
 =4\int x_\epsilon-2\int x_\epsilon^{2}.
\]
Substitution adds \(2\int x_\epsilon^{2}\) to the old amplitude polynomial, changing \(b(\rho)\) to \(b(\rho)+2\). Since \(b(t)\ge1/3\) for \(0\le t\le2\), every term in \(\mathcal B\) has sign \(\ge0\).

---

### 6. No extra compatibility among the \(2^{k}\) solutions

The exact identity holds for **every independent choice** of one solution in each moduli space. It requires no:

- common perturbation sequence;
- common gauge;
- smooth dependence on \(\epsilon\), on \(g\), or on a sequence index;
- coupling equation between different sign classes.

The curvature forms \(f_\epsilon\) are ordinary real closed two-forms on the same manifold and can therefore be added and Walsh-averaged even though they arise from different determinant bundles. Gauge transformations leave all terms in the identity unchanged.

The pairwise Fierz rewriting
\[
2\sum_{I\ne\varnothing}\|f_I^{+}\|_{2}^{2}
 =\mathbb E_{\epsilon,\epsilon'}\int_M
 \left[
 \frac{(\rho_\epsilon-\rho_{\epsilon'})^{2}}2
 +2|w_{\epsilon\epsilon'}|^{2}
 \right]d\mu
\]
uses fixed twisting identifications
\[
S_{\epsilon'}^{+}\cong S_\epsilon^{+}\otimes N_{\epsilon'\epsilon}.
\]
The standard blow-up Spin\(^c\) family carries these identifications. They are topological identifications only; the selected solutions need not satisfy any relation across the pair.

---

### 7. Sequence corollary

**Corollary — arbitrary normalized sequences and selected near-minimizers.**  
Let
\[
M_j=X_j\#k_j\overline{\mathbf{CP}}^{\,2}
\]
carry the full sign family of Spin\(^c\) structures with chamber-independent nonzero Seiberg–Witten invariants. Let \(g_j\) be any sequence of smooth metrics with \(s_{g_j}=-4\); in particular, \(g_j\) may be the Yamabe-normalized variationally selected sequence satisfying
\[
P(g_j)-p_j\longrightarrow0.
\]
For each \(j\), all \(2^{k_j}\) exact solutions can be chosen on the same metric \(g_j\). Defining
\[
D_j=\mathbb E_\epsilon
       \int_{M_j}(2-\rho_{j,\epsilon})\,d\mu_{g_j},
\]
one has
\[
P(g_j)-8\pi^{2}k_j+4D_j=\mathcal B_j,\qquad
\mathcal B_j\ge0.
\]
Consequently,
\[
D_j\ge
 \frac{\bigl(8\pi^{2}k_j-P(g_j)\bigr)_{+}}4.
\]
In particular:

- if
  \[
  P(g_j)\le8\pi^{2}(1-\delta)k_j
  \]
  for a fixed \(\delta>0\), then
  \[
  D_j\ge2\pi^{2}\delta\,k_j;
  \]
- if an independent estimate gives \(D_j=o(k_j)\), then
  \[
  P(g_j)\ge8\pi^{2}k_j-o(k_j).
  \]

Near-minimality itself does not determine \(D_j\); the exact identity records that a saving below \(8\pi^{2}k_j\) must be carried by an average amplitude depletion of the displayed size.

When \(A_j-k_j>0\), every field in this sequence is irreducible.

---

### 8. Statements needed in the surrounding text

The field sections should explicitly record the following assumptions:

1. the full sign **Spin\(^c\) structures** are fixed, not only their real determinant classes;
2. for \(b^{+}\ge2\), every sign structure has a chamber-independent nonzero Seiberg–Witten invariant;
3. for \(b^{+}=1\), the chamber containing the zero-perturbation pairs is named and the invariant is nonzero there;
4. the clean amplitude identity is asserted for \(s=-4\), or after homothetic normalization of a constant scalar metric with scalar \(<0\);
5. \(A-k>0\) is invoked when irreducibility or absence of an unperturbed wall is used, not as an ingredient in the Walsh algebra;
6. no compatibility among independently selected solutions is assumed.

For manifolds with additional \(S^{1}\times S^{3}\) summands, the expected dimension is
\[
\frac{(A-k)-(A-k-4\ell)}4=\ell.
\]
The supplier is then the higher-type, holonomy-constrained invariant discussed in LeBrun 2001 and attributed there to Ozsváth–Szabó, rather than an ordinary zero-dimensional numerical invariant. Once that invariant supplies exact fields for every metric, the same argument applies with the topological benchmark
\[
8\pi^{2}(k+4\ell).
\]