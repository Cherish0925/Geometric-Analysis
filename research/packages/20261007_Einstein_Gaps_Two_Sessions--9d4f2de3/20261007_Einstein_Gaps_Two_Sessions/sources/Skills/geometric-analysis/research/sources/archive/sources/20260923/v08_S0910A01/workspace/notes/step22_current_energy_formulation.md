# Step 22: corrected current-energy formulation for cutoff smoothing

> **Step 23 supersedes Sections 4-5.** Equation (4.3) was not proved by
> the absorption in Section 4 because it lacked covering subordination
> and assumed componentwise absorption was automatic.  Step 23 resolves
> both: the exact tensor inequality has ε=0 (no neighbor dissipation),
> and a maximal r-net provides covering subordination.  See
> `step23_cooperative_persistence_theorem.md`.

This note supersedes the energy-normalization parts of `step21_finite_exponent_smoothing_lemma.md` and also repairs the first version of Step 22 after independent TTCS verification and A02 message #298.  The main point is that the available input is a component-scale current energy together with a relative Sobolev coefficient, not a Whitney-volume-normal energy bound.

We study the normalized cutoff flow

\[
\partial_t g=-2aE,\qquad a=\chi^2,
\qquad E=\operatorname{Ric}+g,
\qquad F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]

Constants may depend on dimension, fixed cutoff profiles, bilipschitz comparison, overlap number, and finite neighbor degree.  They must not depend on the cutoff value `chi_0`, collapsed volume, or the number of components.

## 1. Component energy does not imply Whitney-volume energy

Let

\[
U=B_{5r}(p),\qquad W=B_\ell(y),\qquad y\in B_{4r}(p),
\qquad \ell=cr\chi_0,
\qquad 0<\chi_0\le1.
\]

The component input has the form

\[
\int_U F^2\,d\mu \le M\operatorname{Vol}(U),\qquad M\simeq 1+K_0,
\tag{1.1}
\]

or the corresponding current-time first-exit quantity below.  Since `W subset U`, (1.1) yields only

\[
\int_WF^2\le M\operatorname{Vol}(U).
\tag{1.2}
\]

Energy may concentrate inside `W`, so one cannot replace the right side by `CM Vol(W)`.

The volume comparison must be nonconcentric.  Since `U=B_{5r}(p)` and `y in B_{4r}(p)`,

\[
U\subset B_{9r}(y).
\]

The initial Ricci lower bound gives Bishop--Gromov comparison, hence

\[
\operatorname{Vol}_0(W)
\ge b\left(\frac{\ell}{9r}\right)^4\operatorname{Vol}_0(B_{9r}(y))
\ge b\left(\frac{\ell}{9r}\right)^4\operatorname{Vol}_0(U).
\tag{1.3}
\]

At later times this fixed-domain volume relation is transferred only through bilipschitz comparison; bilipschitz comparison itself does not create a new Ricci lower bound.

Combining (1.2) and (1.3),

\[
\fint_WF^2\le C M\left(\frac r\ell\right)^4,
\qquad
\ell^4\fint_WF^2\le CMr^4.
\tag{1.4}
\]

The local mean can therefore grow like `chi_0^{-4}`.  This invalidates every use of

\[
\int_WF^2\le CM\operatorname{Vol}(W)
\]

unless an additional local mean hypothesis or accessible cover supplies it.

## 2. The surviving four-dimensional cancellation

In four dimensions a relative Sobolev coefficient on a ball or fixed support domain has the scaling

\[
A_W^2\lesssim \ell^2\operatorname{Vol}(W)^{-1/2}.
\]

Therefore

\[
\begin{aligned}
A_W^2\|F\|_{L^2(W)}
&\lesssim \ell^2\operatorname{Vol}(W)^{-1/2}
       \bigl(M\operatorname{Vol}(U)\bigr)^{1/2}\\
&\lesssim \ell^2\sqrt M\left(\frac r\ell\right)^2
\lesssim r^2\sqrt M.
\end{aligned}
\tag{2.1}
\]

Thus critical Sobolev absorption survives collapse only through the product

\[
\gamma=A^2\|F\|_2.
\]

This is also the point of A02 message #298: a thin product or cusp can have raw downstairs `L^2` curvature tending to zero while the relative Sobolev coefficient grows so that `A^2||F||_2` remains order one.  Any argument using a dimension-only downstairs Sobolev constant in a collapsed domain is therefore false.  The current route must carry either relative Sobolev constants on finite-neighbor downstairs domains or work on genuine buffered covers where the cutoff, flow, and mean estimates are transported correctly.

## 3. Correct first-exit energy variable

Take a finite family of supports `U_alpha` and larger buffered domains `U_alpha^+` carrying outer cutoffs.  Let an inner cutoff `eta_alpha` be supported where an outer cutoff `xi_alpha` is identically one.  Define

\[
H_{2,\alpha}(t)=\int_{U_\alpha^+}\xi_\alpha^2 F^2\,d\mu_t,
\qquad
S_\alpha(t)=A_\alpha^4H_{2,\alpha}(t),
\qquad
\Gamma(t)=\sup_\alpha S_\alpha(t)^{1/2}.
\tag{3.1}
\]

Using `S_alpha` rather than bare `H_2` keeps varying Sobolev coefficients visible.  Neighboring coefficients must be comparable:

\[
C_A^{-1}A_\beta\le A_\alpha\le C_AA_\beta
\qquad (\beta\sim\alpha).
\tag{3.2}
\]

This is a geometric input from fixed-domain bilipschitz comparison and the finite-neighbor construction, not an automatic consequence of raw curvature energy.

The initial maximal-function/support construction is intended to give

\[
\Gamma(0)\le Cr^2\sqrt{1+K_0}.
\tag{3.3}
\]

Choosing `r` so that (3.3) is small is the small-energy input for the analytic loop.

## 4. Support-energy persistence with neighbor absorption

The schematic `q=2` tensor inequality has the form

\[
\frac{d}{dt}H_{2,\alpha}+cD_{2,\alpha}
\le C\left(r^{-2}H_{2,\widehat\alpha}+H_{3,\widehat\alpha}\right),
\tag{4.1}
\]

where `widehat alpha` denotes a bounded neighbor enlargement and

\[
D_{2,\alpha}\simeq \int |\nabla(\eta_\alpha a^{1/2}F)|^2,
\qquad
H_{3,\widehat\alpha}=\int \xi_\alpha^2aF^3.
\]

The reaction is absorbed using the outer component energy:

\[
H_{3,\widehat\alpha}
=\int aF(\xi_\alpha F)^2
\le C\gamma_{\widehat\alpha}(t)
      \left(D_{2,\widehat\alpha}+r^{-2}H_{2,\widehat\alpha}\right).
\tag{4.2}
\]

Here `xi_alpha=1` on the inner testing support, so the unweighted `L^2` factor is truly controlled by the outer `H_2` quantity.  The dissipations on the right generally belong to neighbor domains; they cannot be absorbed one component at a time into `D_{2,alpha}`.  The absorption must be performed before expansion or after summing over a bounded-degree weighted graph.  A clean graph form is

\[
S_\alpha'(t)
\le Cr^{-2}\sum_{\beta\sim\alpha}
\frac{A_\alpha^4}{A_\beta^4}S_\beta(t),
\tag{4.3}
\]

provided `\Gamma(t)<=\Gamma_*` and `C\Gamma_*` is inside the absorption range.  From (3.2),

\[
S_\alpha'(t)
\le C C_A^4 r^{-2}\sum_{\beta\sim\alpha}S_\beta(t).
\tag{4.4}
\]

For a graph of degree at most `N`, the sup norm or graph-semigroup estimate gives, for `T=theta r^2`,

\[
\sup_\alpha S_\alpha(t)
\le e^{C C_A^4N\theta}\sup_\alpha S_\alpha(0),
\qquad 0\le t\le T.
\tag{4.5}
\]

Thus

\[
\Gamma(t)\le e^{C C_A^4N\theta/2}\Gamma(0).
\tag{4.6}
\]

With `r` chosen small enough for (3.3) and `theta` chosen fixed but sufficiently small, the first-exit bound for `Gamma` improves.  This is the support-energy statement needed later; it is not a Whitney-volume-normal bound.

## 5. Cubic potential from the same current energy

The same weighted estimates give a spacetime cubic bound

\[
\int_0^t\sum_\alpha H_{3,\alpha}(s)\,ds
\le C\Gamma_*\sum_\alpha H_{2,\alpha}(0),
\tag{5.1}
\]

with bounded overlap and neighbor enlargement.  For pointwise-in-time control of `H_3`, the fixed `q=3` estimate has the form

\[
\frac{d}{dt}H_{3,\alpha}
\le Cr^{-2}\sum_{\beta\sim\alpha}H_{3,\beta},
\tag{5.2}
\]

again after absorption by `Gamma_*`.  Positive-time spreading is along the graph, not confined to one fixed neighbor star.  The correct expression is therefore graph-semigroup propagation:

\[
H_3(t)\le C t^{-1}
\exp\!\bigl(C(t/r^2)\mathcal A\bigr)
\int_0^t H_3(s)\,ds,
\tag{5.3}
\]

where `A` is the bounded-degree adjacency operator, so row sums are bounded by `e^{CNt/r^2}`.  After multiplying by the comparable `A_alpha^4`,

\[
A_\alpha^4H_{3,\alpha}(t)
\le \frac{C\Gamma_*^3}{t}.
\tag{5.4}
\]

This is the desired cubic potential, but it depends on the current support-energy loop (4.3)--(4.6).

## 6. Terminal curvature and transition region

A03's weighted `q -> 3q/2` product remains a valid conditional implication once the weak nested time-space estimate is proved.  It yields

\[
|aF(t)|\le C\Gamma_*/t,
\qquad
|aE(t)|\le C\delta(r^2/t)^{1/3}.
\tag{6.1}
\]

A weaker rescaled boundedness route gives at best

\[
|a\operatorname{Rm}(T)|\le Cr^{-2},
\qquad T=\theta r^2.
\tag{6.2}
\]

This weaker terminal estimate is still enough for finite curvature on plateau buffers where `a=1`, because `r` is selected before taking the near-Einstein sequence limit.  If `K_0` varies along a family, the choice of `r` and the resulting `r^{-2}` bound must be uniform for that family.

The velocity estimate gives bilipschitz metric displacement:

\[
\int_0^T|aE|\,dt\le C\delta r^2.
\tag{6.3}
\]

It does not imply curvature at time `T` is close to curvature at time `0`; curvature contains second spatial derivatives.  The initial hypotheses do not provide pointwise transition curvature bounds.  The intended contradiction uses bounded curvature on plateau buffers plus exponential-pullback averaging; it does not need pointwise transition curvature closeness.

## 7. Unweighted defect remains separate

The global recalibration needs unweighted defect energy

\[
Q_\alpha(t)=\int\eta_\alpha^2|E|^2.
\]

The required structure is triangular:

\[
Q_\alpha'(t)
\le Cr^{-2}\sum_{\beta\sim\alpha}Q_\beta(t),
\tag{7.1}
\]

with no curvature-only additive source such as `epsilon int a|nabla Rm|^2`.  Homogeneity of the flow at `E=0` makes this plausible, but it still requires an exact tensor calculation with evolving measure, cutoffs, and Hessian-`a` integrations by parts.

## 8. Current analytic tasks

The corrected smoothing route now has these distinct tasks:

1. prove the exact tensor `q=2` inequality and the graph absorption leading to (4.3)--(4.6);
2. derive the graph-semigroup cubic potential (5.4);
3. prove the weak nested time-space estimate for `H_q` and `J_m` with correct inner/outer cutoffs;
4. prove positive-time persistence of a fixed defect moment, especially `J_6`, without integrating a nonintegrable `1/t` coefficient from zero;
5. prove the triangular unweighted `Q` estimate (7.1);
6. use plateau bounded curvature over a short time interval, not just a single terminal value, to obtain the controlled exponential-pullback charts needed for the calibrated Derdzinski contradiction.

These would strengthen only the critical four-dimensional negative LeBrun/Ishida--LeBrun route.  The positive branch, arbitrary four-dimensional no-Einstein manifolds, dimensions `n>=5`, the original all-dimensional proposition, and Lean formalization remain unsolved.

## Files

- Normalization computation: `workspace/scripts/step22_energy_normalization.py`
- Graph bookkeeping: `workspace/scripts/step22_first_exit_energy.py`
- Weak-moment ledger: `workspace/scripts/step22_weak_moment_ledger.py`
- This note: `workspace/notes/step22_current_energy_formulation.md`
- Companion weak estimate: `workspace/notes/step22_weak_nested_moment_estimate.md`

## 9. Defect-moment stability ledger

A final algebra check was added in `workspace/scripts/step22_defect_Q_j6_ledger.py`.
For fixed weighted defect moments

\[
J_m=\int\eta^2a^{m-2}|E|^m,
\qquad z_m=\eta a^{(m-1)/2}|E|^{m/2},
\]

the curvature reaction is exactly

\[
\int Fz_m^2.
\]

Thus a fixed exponent such as `m=6` can be controlled directly by the current critical product `gamma=A^2||F||_2`, giving a term of the form

\[
\Gamma_*(X_m+r^{-2}J_m),
\]

rather than by integrating the positive-time cubic potential `H_3(s)~1/s` from zero.  This is the right starting point before applying the later `m -> 3m/2` product.

For the unweighted defect energy

\[
Q=\int\eta^2|E|^2,
\]

the curvature potential has the monomial form

\[
\int\eta^2aF|E|^2=\int Fw^2,
\qquad w=\eta a^{1/2}E.
\]

Sobolev on `w` produces `a|nabla E|^2`, `|da|^2/a |E|^2`, and cutoff remainders, all still multiplied by `E`; no curvature-only monomial appears at this algebraic level.  This supports, but does not prove, the triangular `Q` estimate in Section 7; the exact tensor evolution must still be written.
