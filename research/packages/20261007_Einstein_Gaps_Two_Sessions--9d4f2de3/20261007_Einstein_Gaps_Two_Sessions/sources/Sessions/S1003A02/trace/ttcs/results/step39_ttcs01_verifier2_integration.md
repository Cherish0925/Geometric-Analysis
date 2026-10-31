# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 39,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step39_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step39_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check the gauge-theoretic quantifiers needed to apply the amplitude identity on arbitrary metrics and near-minimizing sequences. For the full blow-up sign family a_epsilon=c+sum epsilon_i E_i on M=X#k CPbar^2, distinguish: nonzero perturbed Seiberg-Witten invariant, monopole class, existence of an unperturbed solution for a fixed metric, irreducibility/reducibility, b^+>=2 versus b^+=1 chambers, and the role of a_epsilon^2=A-k>0 in the low-blow-up range. Decide whether the amplitude theorem genuinely holds for every scalar-negative metric in the chamber-independent range via LeBrun's limiting argument, whether reducibles can occur when A-k>0, and what exact hypotheses must be stated elsewhere. Also test whether simultaneous choice of all 2^k solutions requires any compatibility beyond individual existence. Give a precise corrected theorem statement and sequence corollary.

## Integrated Scientific Memo

## Correct gauge-theoretic quantifiers for the amplitude identity

Let
\[
M=X\#k\overline{\CP}^{\,2}\#\ell(S^1\times S^3),\qquad
a_\epsilon=c+\sum_{i=1}^k\epsilon_iE_i,\qquad \epsilon\in\{\pm1\}^k,
\]
with
\[
c^2=A,\qquad c\cdot E_i=0,\qquad E_i\cdot E_j=-\delta_{ij},
\]
so \(a_\epsilon^2=A-k\).

### 1. The four distinct assertions

For a fixed Spin\(^c\) structure \(\mathfrak s_\epsilon\) with determinant class \(a_\epsilon\), one must distinguish:

1. **Nonzero perturbed SW invariant.**  
   This concerns generic perturbed equations. For \(b^+\ge2\) it is chamber-independent; for \(b^+=1\) its chamber must be specified.

2. **Monopole class.**  
   This means
   \[
   \forall g\ \exists(A,\Phi)
   \]
   solving the **unperturbed** equations for \(\mathfrak s_\epsilon\). For a fixed polarization \(H\), the polarized version quantifies only over \(H\)-adapted metrics.

3. **Existence for one fixed metric.**  
   This is only
   \[
   \exists(A,\Phi)\quad\text{for the chosen }g.
   \]

4. **Irreducibility.**  
   This additionally requires \(\Phi\not\equiv0\). The definition of monopole class does not exclude reducibles.

In the chamber-independent range, a nonzero perturbed invariant implies the monopole-class assertion by LeBrun’s limiting argument: for a fixed arbitrary metric \(g\), choose generic perturbations tending to zero; nonvanishing gives perturbed solutions; gauge compactness, the Weitzenböck bound, and elliptic regularity produce a smooth unperturbed limit. The limiting solution need not be regular or unique.

Thus, when every \(\mathfrak s_\epsilon\) has chamber-independent nonzero invariant,
\[
\forall g\ \forall\epsilon\ \exists(A_\epsilon,\Phi_\epsilon).
\]
Since the sign set is finite, this is equivalent to
\[
\forall g\ \exists\bigl((A_\epsilon,\Phi_\epsilon)\bigr)_{\epsilon\in\{\pm1\}^k}.
\]

The text should formulate the supply in terms of actual Spin\(^c\) structures, not merely their real determinant classes; determinant classes need not determine Spin\(^c\) structures in the presence of \(2\)-torsion.

---

## 2. Does the theorem hold for every metric?

### Chamber-independent case \(b^+(M)\ge2\)

Yes. If the ordinary or higher-type invariant supplying each \(\mathfrak s_\epsilon\) is nonzero and chamber-independent, LeBrun’s limiting argument supplies an unperturbed solution for every smooth metric and every sign.

However, the **clean amplitude identity with \(2-\rho_\epsilon\)** is a theorem for metrics with
\[
s_g\equiv-4,
\]
not for arbitrary pointwise scalar-negative metrics. For a general negative Yamabe conformal class, it applies to its scalar-\(-4\) Yamabe representative. If \(g\) itself has nonconstant \(s_g<0\), exact monopoles still exist, but the maximum-principle bound, kinetic formula, and polynomial decomposition involving \(2-\rho\) change.

Accordingly:

- “every metric” is correct for monopole existence;
- “every scalar-negative metric” is correct for the displayed amplitude formula only if it means every **constant-scalar-curvature** negative metric after homothetic normalization, or every negative Yamabe class after passing to its normalized Yamabe representative.

### \(b^+(M)=1\)

Here “the SW invariant is nonzero” is incomplete unless the chamber is named. The safe hypothesis is:

> For every \(\epsilon\), the invariant is nonzero in the chamber containing the zero-perturbation pairs \((g,0)\).

If \(a_\epsilon^2=A-k>0\), then
\[
(a_{\epsilon,g}^+)^2
=a_\epsilon^2+\|a_{\epsilon,g}^-\|^2
\ge A-k>0
\]
for every metric, so \((g,0)\) never crosses a wall. Moreover,
\[
c\cdot a_\epsilon=A>0,\qquad c^2>0,\qquad a_\epsilon^2>0,
\]
so all sign classes lie in the same positive-cone component as \(c\). This permits a coherent chamber choice across the full sign family.

But \(A-k>0\) does **not** itself prove the chamber invariant is nonzero. A chamber-specific blow-up or higher-type theorem must provide that input. Statements intended to avoid this bookkeeping should retain \(b^+\ge2\).

---

## 3. Reducibles and the role of \(A-k>0\)

A reducible unperturbed solution has \(\Phi\equiv0\), hence \(F_A^+=0\). With
\[
f=-iF_A,\qquad [f/(2\pi)]=a_\epsilon,
\]
Chern–Weil gives
\[
4\pi^2a_\epsilon^2
=\|f^+\|_2^2-\|f^-\|_2^2
=-\|f^-\|_2^2\le0.
\]
Therefore
\[
A-k>0\quad\Longrightarrow\quad
\text{every unperturbed solution for every sign is irreducible.}
\]

This is metric-independent and also prevents a sequence of perturbed irreducibles from converging to a reducible unperturbed solution.

In fact, if \(a_\epsilon\neq0\), the weaker condition \(a_\epsilon^2\ge0\) already excludes reducibles, because the anti-self-dual subspace is negative definite. The strict inequality \(A-k>0\) is nevertheless the clean low-blow-up assumption because it gives the uniform projection bound
\[
(a_{\epsilon,g}^+)^2\ge A-k>0
\]
and excludes \(b^+=1\) walls uniformly.

Positivity of \(A-k\) is **not** used in the Walsh algebra or in the formal exact identity once actual solutions have been supplied. Outside the positive-square range, reducible solutions may occur; the algebraic identity still makes sense, but chamber-independent full-sign supply may fail when \(b^+=1\).

---

## 4. No simultaneous compatibility condition

No compatibility beyond individual existence is needed.

For a fixed metric, choose independently one solution in every sign moduli space. The identity uses only gauge-invariant quantities
\[
f_\epsilon=-iF_{A_\epsilon},\quad
\rho_\epsilon=|\Phi_\epsilon|^2,\quad
\zeta_\epsilon=\langle\Phi_\epsilon,\nabla_{A_\epsilon}\Phi_\epsilon\rangle,
\quad W_{0,\epsilon},
\]
and the real closed forms \(f_\epsilon\) may be Walsh-averaged even though they are curvatures of different determinant bundles.

No common perturbation sequence, common gauge, smooth dependence on \(\epsilon\), smooth dependence on \(g\), or coupling equation is required. The only bookkeeping requirement is that the chosen solution for sign \(\epsilon\) has determinant class \(+a_\epsilon\); arbitrarily replacing some by solutions for \(-a_\epsilon\) would destroy the Walsh cohomology identities.

Pairwise Fierz formulas require fixed twisting identifications between the Spin\(^c\) bundles, but those are topological identifications, not compatibility conditions on the selected solutions.

---

## 5. Correct full-sign amplitude theorem

### Theorem

Let
\[
M=X\#k\overline{\CP}^{\,2}\#\ell(S^1\times S^3)
\]
and fix, for every \(\epsilon\in\{\pm1\}^k\), a Spin\(^c\) structure \(\mathfrak s_\epsilon\) with determinant class
\[
a_\epsilon=c+\sum_i\epsilon_iE_i.
\]
Assume that every \(\mathfrak s_\epsilon\) is an all-metric monopole structure. It suffices, for example, that:

- \(b^+(M)\ge2\) and each relevant chamber-independent invariant is nonzero; or
- \(b^+(M)=1\), the zero-perturbation chamber is fixed, and the invariant of every \(\mathfrak s_\epsilon\) is nonzero in that chamber.

Assume also the simple-type/topological normalization
\[
c^2=A=(2\chi+3\tau)(X).
\]
For \(\ell>0\), the supplier is the appropriate higher-type/holonomy-constrained invariant; its expected dimension is \(\ell\), rather than an ordinary zero-dimensional numerical invariant.

Let \(g\) be any smooth metric on \(M\) with \(s_g=-4\). For each \(\epsilon\), choose independently an unperturbed solution
\[
D_{A_\epsilon}\Phi_\epsilon=0,\qquad
F_{A_\epsilon}^+=2i\sigma(\Phi_\epsilon).
\]
Set
\[
\rho_\epsilon=|\Phi_\epsilon|^2,\qquad
f_\epsilon=-iF_{A_\epsilon},\qquad
\zeta_\epsilon=\langle\Phi_\epsilon,\nabla_{A_\epsilon}\Phi_\epsilon\rangle,
\]
and
\[
f_I=2^{-k}\sum_\epsilon
\left(\prod_{i\in I}\epsilon_i\right)f_\epsilon.
\]
Also define
\[
\psi_\epsilon=2\sqrt2\,\sigma(\Phi_\epsilon),\qquad
W_{0,\epsilon}
=\frac14\left(\frac{\rho_\epsilon^2}{3}\Id
-\psi_\epsilon\otimes\psi_\epsilon\right),
\]
and
\[
b(t)=\frac{-t^2+8t+2}{6}.
\]

Then
\[
0\le\rho_\epsilon\le2,\qquad
K_\epsilon:=\int|\nabla_{A_\epsilon}\Phi_\epsilon|^2
=\frac12\int\rho_\epsilon(2-\rho_\epsilon),
\]
and the exact identity
\[
\boxed{
P(g)-8\pi^2Q
+4\mathbb E_\epsilon\int_M(2-\rho_\epsilon)\,d\mu_g
=\mathcal B(g,\boldsymbol\Phi)
}
\]
holds, where \(Q=k+4\ell\) and
\[
\begin{aligned}
\mathcal B={}&
2\|f_\varnothing^-\|_2^2
+2\sum_{I\ne\varnothing}\|f_I^+\|_2^2\\
&+\mathbb E_\epsilon\left[
8\|\zeta_\epsilon\|_2^2
+4\|W^+-W_{0,\epsilon}\|_2^2
+\int_M\bigl(b(\rho_\epsilon)+2\bigr)
(2-\rho_\epsilon)^2\,d\mu_g
\right]\ge0.
\end{aligned}
\]
Since \(b(t)\ge1/3\) on \([0,2]\), all displayed terms are nonnegative. Hence
\[
\boxed{
P(g)\ge8\pi^2Q
-4\mathbb E_\epsilon\int_M(2-\rho_\epsilon)\,d\mu_g.
}
\]

If \(A-k>0\), every chosen solution is automatically irreducible.

The coefficient \(4\) follows exactly from
\[
P-8\pi^2Q=\mathscr A-4\mathbb E K_\epsilon
\]
and
\[
4K_\epsilon
=4\int(2-\rho_\epsilon)
-2\int(2-\rho_\epsilon)^2.
\]

### General expected dimension

If
\[
d_X=\frac{c^2-(2\chi+3\tau)(X)}4\ne0,
\]
then the benchmark is not \(8\pi^2Q\). Since the induced expected dimension is \(d_X+\ell\), the Chern–Weil constant becomes
\[
8\pi^2\bigl(k+4\ell+4d_X\bigr).
\]
Thus the simple-type equality \(c^2=(2\chi+3\tau)(X)\) must be stated wherever the benchmark \(8\pi^2Q\) is used.

---

## 6. Arbitrary metrics via Yamabe normalization

Suppose every conformal class has negative Yamabe constant—for example, this follows from the all-metric irreducible supply in the \(A-k>0\) range. Given an arbitrary metric \(g\), let \(\widehat g\in[g]\) be its Yamabe representative, scaled so that \(s_{\widehat g}=-4\). Then
\[
P(g)-P(\widehat g)
=\frac{S(g)-S(\widehat g)}{12}\ge0,
\]
so
\[
P(g)\ge P(\widehat g)
\ge8\pi^2Q
-4\mathbb E_\epsilon
\int_M(2-\rho_{\widehat g,\epsilon})\,d\mu_{\widehat g}.
\]
The fields and amplitude deficit here belong to \(\widehat g\), not to the original nonconstant-scalar metric.

---

## 7. Sequence corollary

Let
\[
M_j=X_j\#k_j\overline{\CP}^{\,2}
\#\ell_j(S^1\times S^3),\qquad
Q_j=k_j+4\ell_j,
\]
and assume the full sign-family hypotheses above for every \(j\). Let \(g_j\) be any sequence with \(s_{g_j}=-4\), including the Yamabe-normalized variationally selected near-minimizers.

For each \(j\), choose independently one exact solution for every sign and put
\[
D_j=\mathbb E_\epsilon
\int_{M_j}(2-\rho_{j,\epsilon})\,d\mu_{g_j}.
\]
Then
\[
\boxed{
P(g_j)-8\pi^2Q_j+4D_j=\mathcal B_j,\qquad \mathcal B_j\ge0,
}
\]
and therefore
\[
D_j\ge
\frac{(8\pi^2Q_j-P(g_j))_+}{4}.
\]

Consequently:

- if
  \[
  P(g_j)\le8\pi^2(1-\delta)Q_j,
  \]
  then every field choice satisfies
  \[
  D_j\ge2\pi^2\delta Q_j;
  \]
- if for some choices \(D_j=o(Q_j)\), then
  \[
  P(g_j)\ge8\pi^2Q_j-o(Q_j);
  \]
- for a selected minimizing sequence \(P(g_j)-p_j\to0\), recovery then yields
  \[
  \frac{p_j}{8\pi^2Q_j}\to1,
  \qquad
  \frac{\alpha_j}{h_j}\to4,
  \]
  provided \(D_j=o(Q_j)\).

Near-minimality alone does not imply \(D_j=o(Q_j)\). The identity only proves that any first-order saving below \(8\pi^2Q_j\) must be paid for by an average amplitude deficit of corresponding size.

---

## 8. Exact hypotheses that should appear in the surrounding paper

The field arguments should explicitly state:

1. the full sign family consists of fixed Spin\(^c\) structures, not only real classes;
2. for \(b^+\ge2\), every sign structure has a chamber-independent nonzero invariant;
3. for \(b^+=1\), the chamber containing \((g,0)\) is named and nonvanishing is assumed or proved there;
4. \(A-k>0\) is used for irreducibility, uniform avoidance of walls, and negative-Yamabe consequences—not for Walsh algebra;
5. the clean amplitude formula applies at \(s\equiv-4\), or after Yamabe/homothetic normalization;
6. \(c^2=(2\chi+3\tau)(X)\) is required for the benchmark \(Q=k+4\ell\);
7. handle summands require the higher-type/holonomy-constrained supplier rather than an ordinary zero-dimensional invariant;
8. no compatibility among the independently chosen \(2^k\) solutions is assumed.