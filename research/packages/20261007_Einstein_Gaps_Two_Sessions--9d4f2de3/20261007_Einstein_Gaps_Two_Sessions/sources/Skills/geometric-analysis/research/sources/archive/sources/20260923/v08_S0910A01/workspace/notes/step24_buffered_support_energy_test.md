# Step 24: buffered selected-support energy test for the cutoff flow

Session: S0910A01.  Agent3 / Actuator.  Phase: Execute.

## 0. Correction to Step 23 in the actual selected-good-support problem

The Step 23 dissipation-locality observation is valid and important: when the
Sobolev test variable is supported in one energy domain, absorption uses the
same domain's dissipation rather than neighbor dissipations.  However, the
Step 23 maximal-net repair is not an established input for the real LeBrun
sequence construction.  A maximal `r`-net on all of `M` contains centers outside
the maximal-function good set.  The global Chern--Weil mean gives only a total
curvature budget, not small critical energy

\[
A_\alpha^2\|F\|_{L^2(U_\alpha)}\ll1
\]

at every such center.  Therefore the graph lemma should be retained only as a
conditional lemma for a family with all-center smallness.  It cannot be used as
an established replacement for Li's all-center hypothesis in the selected-good
support construction.

This note tests a simpler support-local formulation that uses only the energy
hypothesis actually available from a selected maximal-function good center.

## 1. Buffered support geometry

Let `p` be a selected good point in the maximal-function set

\[
\mathcal M_{R_0}(|\operatorname{Rm}_{g_0}|^2)(p)\le K_0.
\]

Choose fixed constants

\[
1<L_{\rm pl}<L_\chi<L_\eta,
\qquad L_\eta r\le R_0,
\]

and define

\[
\Omega_\eta=B_{L_\eta r}(p),\qquad
\Omega_\chi\Subset B_{L_\chi r}(p),\qquad
\Pi=B_{L_{\rm pl}r}(p).
\]

Choose cutoffs

\[
\chi\in C_c^\infty(\Omega_\chi),\quad \chi\equiv1\text{ on }\Pi,
\quad |\nabla\chi|\le C/r,
\]

and

\[
\eta\in C_c^\infty(\Omega_\eta),\quad
\eta\equiv1\text{ on a neighborhood of }\operatorname{supp}\chi,
\quad \operatorname{supp}\nabla\eta\subset\{\chi=0\}^{\circ}.
\]

Set

\[
a=\chi^2,
\qquad E=\operatorname{Ric}+g,
\qquad F=(1+|\operatorname{Rm}|^2)^{1/2},
\]

and run

\[
\partial_t g=-2aE.
\]

The collar where `\nabla\eta` lives is exactly stationary because `a=0` on an
open neighborhood of `supp \nabla\eta`.  This is only a coefficient-support
fact, not a finite-propagation assertion.  It gives the pointwise cancellations

\[
a|\nabla\eta|^2=0,
\qquad \nabla a\cdot\nabla\eta=0,
\qquad \operatorname{supp}(a)\subset\{\eta=1\}.
\tag{1.1}
\]

For separated selected supports, the `\Omega_\eta` can be made disjoint by a
fixed-ratio thinning.  The volume lost is controlled by Bishop--Gromov and is
only a fixed factor, as in the earlier Vitali construction.  Thus this analysis
can be summed over a definite-volume selected family without ever covering the
bad set.

## 2. Initial critical smallness on the same selected support

The good-point condition controls the whole auxiliary support:

\[
\int_{\Omega_\eta}|\operatorname{Rm}|^2\le
K_0\operatorname{Vol}(\Omega_\eta).
\]

Since `F^2=1+|Rm|^2`, write

\[
H_2(0)=\int\eta^2F^2\le M\operatorname{Vol}(\Omega_\eta),
\qquad M=1+K_0.
\tag{2.1}
\]

The four-dimensional relative Sobolev inequality on `\Omega_\eta` has the form

\[
\|u\|_{L^4(\Omega_\eta)}^2
\le A_\Omega^2\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right),
\qquad
A_\Omega^2\le C(L_\eta) r^2\operatorname{Vol}(\Omega_\eta)^{-1/2}.
\tag{2.2}
\]

Therefore the critical product available on the selected support is

\[
\beta_0=A_\Omega^2\|F(0)\|_{L^2(\Omega_\eta)}
\le C(L_\eta)r^2\sqrt{1+K_0}.
\tag{2.3}
\]

Collapsed volume cancels.  The smoothing scale `r` must be chosen after the
fixed support ratios and tensor constants so that `C_*\beta_0` is below the
absorption threshold.  The script
`workspace/scripts/step24_buffered_support_algebra.py` verifies this scaling and
computes the required smaller `r` when sample constants are inserted.

## 3. Whole-support H2 tensor inequality

The desired weak tensor estimate under the cutoff flow is

\[
\frac{d}{dt}H_2+cD_2
\le C\int \eta^2aF^3+C r^{-2}H_2,
\tag{3.1}
\]

where

\[
H_2=\int\eta^2F^2,
\qquad
D_2=\int\eta^2a|\nabla\operatorname{Rm}|^2.
\]

The Step 20 tensor ledger gives this schematic form after integrating the
`\nabla^2a` terms by parts: the principal `a\Delta` term supplies `D_2`; the
regular cutoff terms are measured by `|\nabla a|^2/a=4|\nabla\chi|^2\le Cr^{-2}`;
and the terms involving `\nabla\eta` vanish by (1.1).  Algebraic curvature,
metric-norm, and volume-form variations contribute at most the cubic reaction
and lower order `r^{-2}H_2` (using `|E|\le CF`).  A complete proof still requires
writing the exact tensor variation, but the support structure removes the old
localization obstruction.

## 4. Absorbing the weighted cubic on the same support

Because `\eta=1` on `supp a`,

\[
R_2:=\int\eta^2aF^3=\int_{\operatorname{supp}\chi}(\chi F)^2F.
\]

Hölder and Sobolev on the single selected support give

\[
R_2
\le \|F\|_{L^2(\operatorname{supp}\chi)}\,\|\chi F\|_{L^4(\Omega_\eta)}^2
\le \beta_a(t)\left(D_2+C r^{-2}H_2\right),
\tag{4.1}
\]

where the active first-exit parameter is

\[
\beta_a(t)=A_\Omega^2\|F(t)\|_{L^2(\operatorname{supp}\chi)}
\le A_\Omega^2H_2(t)^{1/2}.
\]

One may also use the full `\Omega_\eta` norm, but then the stationary collar must
be written explicitly:

\[
\|F(t)\|_{L^2(\Omega_\eta)}^2
\le H_2(t)+\int_{\Omega_\eta\cap\{\eta<1\}}F(0)^2\,d\mu_0.
\]

Indeed,

\[
\|\nabla(\chi F)\|_2^2
\le 2\int a|\nabla F|^2+2\int|\nabla\chi|^2F^2
\le C(D_2+r^{-2}H_2).
\]

Assume a first-exit interval on which `\beta_a(t)\le2\beta_0` and choose
`C\beta_0<c/4`.  Substitution into (3.1) yields the closed support estimate

\[
\boxed{
H_2'+c_1D_2\le C_1r^{-2}H_2.}
\tag{4.2}
\]

Thus, for `T=\theta r^2` with fixed small `\theta`,

\[
H_2(t)\le e^{C_1\theta}H_2(0),
\qquad
\int_0^T D_2\le C H_2(0),
\tag{4.3}
\]

and the first-exit bound for `\beta_a(t)` self-improves if `\theta` is small.
This closes independently on each selected support; no net on bad centers and
no graph over all of `M` is used.

## 5. Correct weighted cubic spacetime control

Integrating (4.1) with (4.3) gives

\[
\int_0^T R_2(t)\,dt
\le C\beta_*H_2(0).
\]

Equivalently,

\[
\boxed{
A_\Omega^4\int_0^T\int aF^3\le C\beta_*^3.}
\tag{5.1}
\]

This is the correctly weighted cubic moment.  It should not be replaced by the
unweighted parabolic-Sobolev moment obtained from applying Sobolev to
`\eta\sqrt a F`, which carries a different weight such as
`\eta^3a^{3/2}F^3`.  The reaction that appears in the curvature equation is
`aF^3`, and (5.1) is the exact quantity generated by the same absorption
that controlled `H_2`.

## 6. Fixed q=3 propagation from a time average

For the `q=3` weighted moment

\[
Y(t)=\int\eta^2aF^3,
\]

the fixed-exponent tensor inequality should have the form

\[
Y'(t)+cD_3(t)
\le C r^{-2}Y(t)+C I_4(t),
\qquad
D_3=\int\eta^2a^2F|\nabla\operatorname{Rm}|^2,
\qquad
I_4=\int\eta^2a^2F^4.
\tag{6.1}
\]

The clean absorption of `I_4` does not use a Riccati coefficient.  Take

\[
u=aF^{3/2}.
\]

Because `\eta=1` on `supp a`,

\[
I_4=\int F\,u^2
\le \|F\|_{L^2(\operatorname{supp}\chi)}\|u\|_{L^4(\Omega_\eta)}^2.
\]

The gradient satisfies

\[
\|\nabla u\|_2^2
\le C D_3+C\int |\nabla a|^2F^3
\le C D_3+C r^{-2}Y,
\tag{6.2}
\]

since `|\nabla a|^2=4a|\nabla\chi|^2\le Cr^{-2}a`.  Thus

\[
\boxed{
I_4\le C\beta_a(t)(D_3+r^{-2}Y).}
\tag{6.3}
\]

For `C\beta_a(t)<c/2`, (6.1)--(6.3) give the linear propagation inequality

\[
Y'(t)\le C r^{-2}Y(t).
\tag{6.4}
\]

From (5.1), for every target `0<t\le T` there is `s_0\in[t/2,t]` such that

\[
A_\Omega^4Y(s_0)
\le {2\over t}A_\Omega^4\int_{t/2}^tY(s)\,ds
\le {C\beta_*^3\over t}.
\tag{6.5}
\]

Forward propagation by (6.4) gives

\[
\boxed{
A_\Omega^4Y(t)
\le {C\beta_*^3\over t},
\qquad 0<t\le T.}
\tag{6.6}
\]

This avoids the component-dependent starting-time problem of the graph version:
the time average and forward propagation are performed independently on each
selected support.  The previous draft's estimate
`I_4\le\epsilon D_3+C(r^{-2}+A_\Omega^4Y)Y` was not supported by the cutoff
algebra; the variable `aF^{3/2}` is the correct one for the `q=3` reaction.

## 7. Triangular unweighted defect estimate on the same support

Let

\[
Q(t)=\int\eta^2|E|^2.
\]

The defect equation under `\partial_tg=-2aE` is homogeneous in `E`:

\[
\partial_tE=a\Delta_LE-2aE+(\nabla a)*\nabla E+(\nabla^2a)*E
+a(\operatorname{Rm}*E)+a(E*E).
\tag{7.1}
\]

Testing by `\eta^2E` and using (1.1) gives

\[
Q'+cX
\le C r^{-2}Q+C\int\eta^2aF|E|^2,
\qquad
X=\int\eta^2a|\nabla E|^2.
\tag{7.2}
\]

The curvature potential is absorbed with `w=\eta\chi E`; because `\eta=1` on
`supp\chi`,

\[
\int aF|E|^2
\le \|F\|_{L^2(\operatorname{supp}\chi)}\|\chi E\|_{L^4}^2
\le \beta_a(t)(X+C r^{-2}Q).
\tag{7.3}
\]

For small `\beta_a`,

\[
\boxed{Q'\le C r^{-2}Q.}
\tag{7.4}
\]

Summing (7.4) over the disjoint selected supports preserves the normalized
unweighted defect on the active region.  The frozen complement has `a=0`, hence
is unchanged by the cutoff flow; for the final LeBrun recalibration one must
combine this active-region estimate with the volume/density selection that
produces enough smoothed plateau mass carrying small Step 8 tensor defects.  The
support-local estimate by itself does not control bad regions that were never
selected.

## 8. What this achieves and what remains

The buffered-support formulation has three advantages over the Step 23 maximal
net for the actual sequence:

1. its initial smallness comes from the selected good support, where the
   maximal-function hypothesis genuinely holds;
2. it includes the entire transition region of the physical cutoff `\chi` in the
   energy estimate;
3. the auxiliary collar where `\nabla\eta` lives is stationary and does not
   introduce parabolic influence terms.

The remaining load-bearing work is the exact tensor proof of (3.1), (6.1), and
(7.2) for the normalized cutoff flow, including metric-norm and volume-form
terms, without hidden all-center assumptions.  Once these inequalities are
established, the downstream two-stage architecture remains: (i) (5.1)--(6.6)
produce the positive-time weighted `H_3` bound; (ii) the subcritical Moser
hierarchy yields `|a\operatorname{Rm}|\le C\beta/t`; (iii) the triangular `Q`
estimate and defect moments propagate small Einstein defect; (iv) bounded
curvature on plateaux plus exponential-pullback averaging can feed the Step 8
Derdziński calibrated-germ contradiction.

This still addresses only the critical four-dimensional negative
LeBrun/Ishida--LeBrun laboratory.  It does not settle the positive branch,
arbitrary four-dimensional topology, dimensions `n\ge5`, the original Yau 26
proposition, or Lean formalization.

## 9. Script evidence

- `workspace/scripts/step24_buffered_support_algebra.py`: verifies the fixed-ratio
  support cancellations, the collapse-free critical product, the need to choose
  `r` after constants, the integrated weighted cubic scale
  `A^4\int\!\int aF^3\lesssim\beta^3`, the time-average propagation scale
  `A^4H_3(t)\lesssim\beta^3/t`, and the triangular `Q` amplification.

## 10. TTCS verification and repairs

TTCS verification (`trace/ttcs/results/step24_ttcs01_verifier1_integration.md`)
supported the main buffered-support idea and supplied two important repairs that
have been incorporated above.

1. The active first-exit parameter should be
   \[
   \beta_a(t)=A_\Omega^2\|F(t)\|_{L^2(\operatorname{supp}\chi)},
   \]
   not necessarily the full `\Omega_\eta` norm.  The full norm is still usable
   only after adding the stationary-collar term explicitly.
2. The `q=3` reaction `I_4=\int a^2F^4` should be absorbed with
   `u=aF^{3/2}`, producing the linear estimate
   \[
   I_4\le C\beta_a(D_3+r^{-2}Y),
   \]
   not by the unsupported Riccati interpolation in the first draft.  The time
   average plus forward propagation then gives `A_\Omega^4Y(t)\lesssim
   \beta^3/t`.

TTCS also emphasized that evolving Sobolev control, exact tensor inequalities,
uniform smooth existence, and the bridge from selected supports to global
normalized defect remain mathematical work, not consequences of the support
algebra.

## 11. Static packing/coloring for selected supports

The script `workspace/scripts/step24_packing_coloring.py` checks a crude but
collapse-free selected-support packing mechanism.  Starting from the
maximal-function good set `G` with `Vol(G)\ge g_0Vol(M)`, choose a maximal
disjoint `B_r(p_j)` family with centers in `G`, so that `G\subset\cup_jB_{5r}(p_j)`.
For fixed support radius `L_\eta r`, the intersection graph of the supports
`B_{L_\eta r}(p_j)` has bounded degree under the Ricci lower bound: a neighbor
center lies in `B_{2L_\eta r}(p_i)`, and the disjoint `B_{r/2}(p_j)` balls pack
inside `B_{(2L_\eta+1/2)r}(p_i)`.  Therefore a weighted coloring selects one
color class with pairwise disjoint supports and total `B_r`-ball volume at least

\[
{g_0\over BG(5)(D+1)}\operatorname{Vol}(M),
\]

where `D` is the fixed degree bound.  With the illustrative constants
`r=0.0017`, `L_\eta=8`, the script reports `BG(5)=625.0236`,
`D\le1.19\times10^6`, and a retained volume fraction `6.74\times10^{-10}` for
`g_0=1/2`.  This fraction is tiny but sequence-independent, which is all the
Derdziński averaging route needs.  The estimate is static; it does not prove the
flow inequalities.

## 12. Codex tensor-derivation worker

A bounded Codex worker was started in exec mode with proposal
`workspace/codex_loop/Research_Project_Proposal.md`.  Its task is to derive the
index-level curvature and defect energy inequalities for
`\partial_tg=-2\chi^2(\operatorname{Ric}+g)` and report under
`workspace/codex_loop/Research_Report.md` and `workspace/codex_loop/work/`.  A
later step should check the worker status once and inspect the report before
using any result.
