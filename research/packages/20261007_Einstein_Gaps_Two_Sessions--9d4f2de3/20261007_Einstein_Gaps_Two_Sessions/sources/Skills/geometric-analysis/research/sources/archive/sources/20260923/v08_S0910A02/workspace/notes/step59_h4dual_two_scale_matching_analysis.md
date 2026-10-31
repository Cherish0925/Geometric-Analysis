# Step 59: H4-dual necessity bridge — the two-scale matching crux

Session S0910A02. Agent2 / Constructor. Phase Execute.

## 0. Scope

This note develops the H4-dual necessity bridge to the point where the single
remaining analytic gap is identified precisely.  It is **not** a proof or
counterexample for Yau–26.  Its content is:

1. The precise open lemma whose proof or disproof decides the noncollapsed
   positive branch.
2. A verified decomposition of the argument into the interior equation (which
   works) and the two-scale matching (which is the gap).
3. A quantification of why the naive bootstrap fails.
4. The win-either-way dichotomy.

## 1. Setup and equation in the ALE frame

Let \((M^4,g_i)\) be a noncollapsed sequence with
\(\|\operatorname{Ric}_{g_i}-\Lambda g_i\|_{\mathrm{op}}\le\delta_i\to0\),
\(\Lambda>0\), converging in the Cheeger–Naber sense to an Einstein orbifold
\((M_o,g_o)\) with an \(A_1\) singularity at \(p\) and bubble scale
\(t_i\to0\).

In orbifold coordinates \(x\) at \(p\), define ALE coordinates \(y=x/\sqrt{t_i}\).
The ALE-frame metric is \(\tilde g_i(y)=g_i(\sqrt{t_i}y)\) (so that
\(g_i=t_i\tilde g_i\) as tensors).  By Cheeger–Naber:
\[
  \tilde g_i\to\mathbf{eh}_\zeta\quad\text{in }C^{1,\alpha}_{\mathrm{loc}}.
\]
Write \(h_i=\tilde g_i-\mathbf{eh}\) (suppressing \(\zeta\)).  Then
\(h_i\to0\) in \(C^{1,\alpha}(B_R)\) for each fixed \(R\).

**The Ricci equation in the ALE frame.**  Since Ricci is scale-invariant:
\[
  \operatorname{Ric}(\tilde g_i)
  =\operatorname{Ric}(g_i)
  =\Lambda g_i+E_i
  =\Lambda t_i\tilde g_i+E_i,
\]
where \(|E_i|_{\tilde g}\le t_i\delta_i\).  Expanding around
\(\mathbf{eh}\) (which is Ricci-flat):
\[
  P_{\mathbf{eh}}h_i = \Lambda t_i(\mathbf{eh}+h_i)+E_i-Q(h_i,h_i)+\text{gauge},
\]
where \(P_{\mathbf{eh}}=\tfrac12\nabla^*\nabla-\mathring R_{\mathbf{eh}}\)
is the Lichnerowicz operator.

## 2. Indicial structure on EH

The ALE space \(T^*S^2\cong(\mathbb R^4/\mathbb Z_2)\setminus\{0\}\) has
link \(\mathbb{RP}^3\).  For \(\mathbb Z_2\)-invariant TT 2-tensors, the
angular Laplacian eigenvalue for degree \(l\) is \(\mu_l=l(l+2)\) (even \(l\)
only).  The radial indicial equation \(\alpha(\alpha+2)=\mu_l\) gives:

| \(l\) | \(\mu\) | \(\alpha_+\) | \(\alpha_-\) | Growth | Decay |
|------:|--------:|-------------:|-------------:|-------:|------:|
| 0 | 0 | 0 | \(-2\) | \(\rho^0\) | \(\rho^{-2}\) |
| **2** | **8** | **2** | **\(-4\)** | **\(\rho^2\)** | **\(\rho^{-4}\)** |
| 4 | 24 | 4 | \(-6\) | \(\rho^4\) | \(\rho^{-6}\) |

**The obstruction pair is \(l=2\): \(\alpha=(2,-4)\).**  The growing mode
\(\rho^2\) is the orbifold quadratic \(H_2\).  The decaying mode \(\rho^{-4}\)
is the obstruction tensor \(\mathbf o_k\).

The boundary Wronskian on \(S_R=\{\rho=R\}\):
\[
  \mathcal B(R)
  =\tfrac12\int_{S_R}
    \bigl(\langle\nabla_\nu h,\mathbf o_k\rangle
    -\langle h,\nabla_\nu\mathbf o_k\rangle\bigr)\,dS.
\]
For homogeneous modes \(h\sim AR^2\), \(\mathbf o_k\sim BR^{-4}\): the product
\(|S_R|\cdot W(R)=R^3\cdot(-6R^{-3})=-6\) is **\(R\)-independent**.

Script: `workspace/scripts/step59_h4dual_indicial_and_matching.py`.
Data: `workspace/data/step59_h4dual_indicial_and_matching.json`.

## 3. What the interior equation gives (without matching)

Define \(f_i=h_i/t_i\).  Dividing the ALE-frame equation by \(t_i\):
\[
  P_{\mathbf{eh}}f_i
  =\Lambda\mathbf{eh}
  +\Lambda t_i f_i
  +E_i/t_i
  -t_i^{-1}Q(t_if_i,t_if_i)
  +\text{gauge}.
\]
The source is \(\Lambda\mathbf{eh}+O(\delta_i)+O(t_i|f_i|)+O(t_i|f_i|^2)\).

**If \(f_i\) is bounded on \(B_R\):** Arzelà–Ascoli gives a subsequential
limit \(f\) satisfying
\[
  P_{\mathbf{eh}}f=\Lambda\mathbf{eh}+\sum_{k=1}^3\lambda_k\mathbf o_k
\]
for some \(\lambda_k\in\mathbb R\).  The \(\lambda_k\) are the cokernel
projections determined by the boundary data of \(f\) at infinity.

**Ozuch's identification.**  If additionally \(f\sim H_2+O(\rho^{-2})\) at
infinity (where \(H_2\) is the orbifold quadratic), then by the uniqueness of
\(\underline h_2\) (Ozuch Lemma 2.3 and equation (24)):
\[
  \lambda_k=c\langle R_\varepsilon(p)\zeta,\zeta_{(k)}\rangle,
\]
hence \(R_\varepsilon(p)\zeta=0\).

**Without the matching,** \(\lambda_k\) is undetermined.  Different
subsequences could converge to different solutions with different
\(\lambda_k\), corresponding to different large-\(\rho\) behaviors.

## 4. The matching: where the gap lives

The matching asks: does \(h_i\approx t_i H_2(\rho)\) at large but growing
\(\rho\)?  Equivalently: does \(f_i=h_i/t_i\) grow like \(\rho^2\) at
large \(\rho\), with the correct angular structure?

**What the orbifold convergence gives.** At orbifold distance \(\eta\) from
\(p\), i.e.\ ALE radius \(\rho=\eta/\sqrt{t_i}\):
\[
  h_i(\eta/\sqrt{t_i})
  =\tilde g_i-\mathbf{eh}
  \to g_o(\eta)-\delta
  =H_2(\eta)+O(\eta^4).
\]
And \(t_i\underline h_2(\eta/\sqrt{t_i})
\approx t_i\cdot\eta^2/t_i\cdot\hat H_2(\theta)
=H_2(\eta)\).

**So the values match at the boundary.**  The problem is propagating this
matching across the \(\sim\frac12|\log_2 t_i|\) doubling scales between
\(\rho=O(1)\) and \(\rho=\eta/\sqrt{t_i}\).

## 5. Why the naive bootstrap fails

The elliptic interior estimate on \(B_R\):
\[
  \|h_i\|_{C^0(B_{R/2})}
  \le C_R\bigl(\|P_{\mathbf{eh}}h_i\|_{L^p(B_R)}+\|h_i\|_{C^0(\partial B_R)}\bigr).
\]
Applied iteratively from the matching radius \(R_i=\eta/\sqrt{t_i}\) down
to \(\rho=O(1)\):
\[
  \varepsilon_i(R)\le C_R\,\varepsilon_i(2R)+C_R\,t_i.
\]
After \(k\sim\frac12|\log_2 t_i|\) steps:
\[
  \varepsilon_i(R_0)
  \le\prod_{j=0}^{k-1}C_{2^jR_0}\cdot\varepsilon_i(R_i)
  +\text{geometric sum}\cdot t_i.
\]
The product grows as \(C_0^k\sim t_i^{-c/2}\) for some \(c>0\), while the
boundary value is \(\varepsilon_i(R_i)=H_2(\eta)=O(\eta^2)\).  The bound
becomes \(O(\eta^2 t_i^{-c/2})\), which diverges.

**The bootstrap fails because the elliptic constant accumulates
exponentially over \(\sim|\log t_i|\) scales.** This is a logarithmic-scale
propagation problem.

## 6. What would close the gap: weighted elliptic estimates

In the exact Einstein setting, Biquard and Ozuch use **weighted Hölder
norms** \(C^{k,\alpha}_\beta\) with weight \(\rho^{-\beta}\) to control all
scales simultaneously.  The Lichnerowicz operator
\(P_{\mathbf{eh}}:C^{2,\alpha}_\beta\to C^{0,\alpha}_{\beta-2}\) is Fredholm
for \(\beta\) not an indicial root, with known kernel and cokernel.

For the pinched sequence, define \(w_i=h_i-t_i\underline h_2\).  The equation
for \(w_i\):
\[
  (P_{\mathbf{eh}}-\Lambda t_i)w_i
  =\Lambda t_i^2\underline h_2
  +E_i
  -Q(h_i,h_i)
  +\text{gauge}
  -t_i\sum\lambda_k\mathbf o_k.
\]
On the orbifold matching side: \(w_i\) at \(\rho=\eta/\sqrt{t_i}\) is
\(O(t_i\rho^{-2})+O(t_i^2\rho^4)=O(t_i^{3/2})\) (at the transition).

**Open Lemma (Weighted Two-Scale Matching).**
*Under the above hypotheses, there exist \(\beta\in(0,2)\) and
\(C=C(g_o,\eta)>0\) such that*
\[
  \|w_i\|_{C^{2,\alpha}_\beta(\mathbf{eh})}
  \le C(t_i+\delta_i)
\]
*for all sufficiently large \(i\).*

If this holds, then \(h_i=t_i\underline h_2+O(t_i+\delta_i)\) in
the weighted norm, which gives \(h_i=O(t_i\rho^{2-\beta})\) pointwise at
large \(\rho\) and \(h_i=O(t_i)\) on compact sets.  The matching is then
complete and \(f_i\to\underline h_2\) in \(C^{k,\alpha}_{\mathrm{loc}}\).

## 7. The dichotomy

**(A) If the Open Lemma holds:** The H4-dual necessity theorem follows.
Every noncollapsed \(C^0\)-Ricci-pinched sequence converging to an
\(A_1\)-orbifold must have bubble parameters satisfying
\(R_\varepsilon(p)\zeta=0\).  Combined with the ADE classification (Steps
46–47), this constrains all noncollapsed positive counterexamples to lie in
finite chiral degeneracy loci.

**(B) If the Open Lemma fails:** There exist pinched sequences whose
normalized bubble perturbation \(h_i/t_i\) does not converge to the orbifold
quadratic \(\underline h_2\).  Instead, the perturbation carries a "wild"
correction at a rate slower than \(t_i\) (e.g.\ \(t_i^{1-\epsilon}\)) that
contaminates the boundary data.  This opens a **counterexample channel**
through bubble formations whose fine structure is not controlled by the
orbifold curvature.

In either case, the result is a **theorem about the structure of Yau–26**,
not a proof or counterexample of the proposition itself.

## 8. The wall between Einstein endpoints

As a corollary of the noncollapsed analysis (Steps 55–57), the mixed-row
families are anchored between Einstein endpoints.  The endpoints \(r=0,N\)
minimize every \((\chi,\tau)\)-monotone Einstein inequality.  Since they are
known Einstein, interior rows satisfy all such inequalities automatically.
Therefore no obstruction that depends monotonically on
\((\chi,\tau,\|M\|,\deg)\) can exclude an interior row.

More precisely: the margin
\(2\chi-3|\tau|=4(h-1)^2+6\min(r,N-r)\) is smallest at the endpoints and
grows toward the center.  This includes Hitchin–Thorpe, Gromov–norm
\(\chi\ge c\|M\|\), and entropy/minimal-volume refinements.

This structural observation applies to both the positive and negative mirrors.
It explains why the noncollapsed wall is not an accident of the literature but
a built-in feature of the construction: compatible bubbling follows the
holomorphic route and lands on Einstein endpoints, while reversed bubbling
inserts \(+2\)-spheres that void Kähler and ordinary monopole machinery.

## 9. Implications for the full Yau–26 allocation

1. **Positive noncollapsed:** reduces to the Open Lemma for the matching,
   plus Einstein existence on the mixed rows (which no known tool settles).
2. **Positive collapse:** blocked at almost-Killing field production (Step 29).
   Chern–Weil is saturated (Step 58), so any obstruction must find a forced
   energy defect.  The next action is an adversarial construction attempt.
3. **Negative branch:** the LeBrun gap at \(p>1/3\) is stable; the \(p=1/3\)
   boundary has zero margin; the cutoff-flow route remains conditional.
4. **\(n\ge5\):** no closed non-Einstein manifold is known; refutation requires
   a major separate prerequisite.
5. **Lean:** deferred until a mathematical theorem is established.

No branch of Yau–26 is proved, refuted, or formalized.

## 10. Files

- Script: `workspace/scripts/step59_h4dual_indicial_and_matching.py`
- Data: `workspace/data/step59_h4dual_indicial_and_matching.json`
- This note: `workspace/notes/step59_h4dual_two_scale_matching_analysis.md`
- Prior notes: `step48_H4dual_and_biKahler_realizability.md`,
  `step49_positive_branch_wall_and_operator_norm.md`,
  `step57_dichotomy_and_kahler_exclusion.md`,
  `step58_biquard_ct_and_collapse_ceiling.md`
- Source: Ozuch lines 370–650 (obstruction theory),
  Biquard §4 Lemmas 4.1–4.2 (approximate metric estimates)
