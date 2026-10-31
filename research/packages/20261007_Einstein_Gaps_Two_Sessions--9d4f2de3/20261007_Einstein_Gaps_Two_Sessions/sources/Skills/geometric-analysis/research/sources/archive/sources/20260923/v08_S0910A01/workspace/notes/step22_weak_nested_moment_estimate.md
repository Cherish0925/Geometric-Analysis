# Step 22: corrected weak nested moment estimate

This note repairs the first Step 22 weak-estimate note using TTCS verification.  It keeps the corrected current-energy normalization from `step22_current_energy_formulation.md` and explicitly tracks inner/outer cutoffs, finite-neighbor domains, and time interval nesting.  It remains a derivation framework: the exact tensor inequality and the triangular unweighted defect estimate still have to be written term by term.

We work under

\[
\partial_t g=-2aE,
\qquad a=\chi^2,
\qquad E=\operatorname{Ric}+g,
\qquad F=(1+|\operatorname{Rm}|^2)^{1/2}.
\]

For curvature moments define

\[
H_{q,k}=\int \eta_k^2a^{q-2}F^q\,d\mu,
\qquad
v_{q,k}=\eta_k a^{(q-1)/2}F^{q/2}.
\tag{0.1}
\]

For defect moments define

\[
J_{m,k}=\int \eta_k^2a^{m-2}|E|^m\,d\mu,
\qquad
z_{m,k}=\eta_k a^{(m-1)/2}|E|^{m/2}.
\tag{0.2}
\]

The limit of `H_q^{1/q}` and `J_m^{1/m}` is the weighted quantity `aF` or `a|E|`; no division by `a` is used at the zero set.

## 1. Nested spatial cutoffs

Let

\[
\eta_{k+1}\prec \eta_k\prec \xi_k,
\]

where `xi_k=1` on `supp eta_k`; all supports stay inside a fixed finite-neighbor star.  The derivative bounds are

\[
|d\eta_k|\le C2^k/\ell
\]

on a Whitney ball with `ell=cr chi0`.  Since `a≈chi0^2` there,

\[
a|d\eta_k|^2\le C4^k r^{-2}.
\tag{1.1}
\]

The regular cutoff term satisfies

\[
|da|^2/a=4|d\chi|^2\le Cr^{-2}.
\tag{1.2}
\]

A component-scale version has the same estimates with `ell` replaced by `r` and `a<=1`.

## 2. Tensor power input

The Step 20 tensor variation is expected to yield, for each fixed `q>=2`,

\[
\frac{d}{ds}H_{q,k}+c_qD_{q,k}
\le Cq^2\left(
\int a^{q-1}|d\eta_k|^2F^q
+
\int \eta_k^2\frac{|da|^2}{a}a^{q-2}F^q
+
\int\eta_k^2a^{q-1}F^{q+1}
\right),
\tag{2.1}
\]

where

\[
D_{q,k}\simeq\int |\nabla v_{q,k}|^2.
\]

Using (1.1)--(1.2), the first two terms are bounded by an outer moment:

\[
Cq^24^k r^{-2}H_{q,k}^{out},
\tag{2.2}
\]

where `H_{q,k}^{out}` is defined with the cutoff `xi_k`.  The outer cutoff is necessary because `eta_k` may vanish at the edge of the support.

## 3. Reaction term with correct cutoff powers

Let

\[
R_q=\int\eta_k^2a^{q-1}F^{q+1}.
\]

Use the outer cubic potential

\[
H_{3,k}^{out}=\int\xi_k^2aF^3,
\]

and define

\[
K_{q,k}=\int\eta_k^3a^{3q/2-2}F^{3q/2}.
\]

Because `xi_k=1` on `supp eta_k`, Hölder gives

\[
R_q\le (H_{3,k}^{out})^{1/3}K_{q,k}^{2/3}.
\tag{3.1}
\]

The cutoff exponents now match the Sobolev variable:

\[
K_{q,k}\le H_{q,k}^{1/2}\|v_{q,k}\|_4^2,
\tag{3.2}
\]

since

\[
H_{q,k}^{1/2}\|v_{q,k}\|_4^2
=\left(\int\eta_k^2a^{q-2}F^q\right)^{1/2}
 \left(\int\eta_k^4a^{2q-2}F^{2q}\right)^{1/2},
\]

and Hölder gives the intermediate `eta^3` density.  The first version's equality `H_{2q}^{1/2}=||v_q||_4^2` suppressed this cutoff issue.

The four-dimensional relative Sobolev inequality gives

\[
\|v_{q,k}\|_4^2
\le A_k^2\left(D_{q,k}+C4^k r^{-2}H_{q,k}^{out}\right).
\tag{3.3}
\]

Combining (3.1)--(3.3) and applying Young's inequality,

\[
R_q
\le \epsilon D_{q,k}
+C\left(4^k r^{-2}+\epsilon^{-2}A_k^4H_{3,k}^{out}\right)H_{q,k}^{out}.
\tag{3.4}
\]

If the current-energy loop supplies

\[
A_k^4H_{3,k}^{out}(s)
\le C\Gamma_*^3/s,
\qquad s\in[t/2,t],
\tag{3.5}
\]

then on that positive-time slab

\[
R_q
\le \epsilon D_{q,k}
+C4^k(t^{-1}+r^{-2})H_{q,k}^{out}.
\tag{3.6}
\]

The defect reaction is analogous:

\[
\int\eta_k^2a^{m-1}F|E|^m
\le \epsilon X_{m,k}
+C\left(4^k r^{-2}+\epsilon^{-2}A_k^4H_{3,k}^{out}\right)J_{m,k}^{out}.
\tag{3.7}
\]

Here `J_m^{out}` uses the outer cutoff.  For a fixed base exponent such as `m=6`, this same critical absorption can give positive-time persistence of `J_6` without integrating the singular `H_3(s)~s^{-1}` coefficient from time zero.

## 4. Correct time intervals

Fix the target time `t>0`.  Use shrinking intervals

\[
I_k=\left[\frac t2+\frac t4(1-2^{-k}),\ t\right].
\tag{4.1}
\]

Then

\[
I_0=[t/2,t],\qquad I_1=[5t/8,t],\qquad I_k\downarrow[3t/4,t].
\]

Choose a time cutoff `rho_k` supported in `I_k`, identically one on `I_{k+1}`, with

\[
|\rho_k'|\le C2^k t^{-1}\le C4^k t^{-1}.
\tag{4.2}
\]

This corrects the first version, whose intervals were expanding rather than shrinking.

## 5. Weak time-space estimate

Multiply (2.1) by `rho_k^2`, integrate over `I_k`, use (2.2), (3.6), and (4.2), and absorb `epsilon D_{q,k}`.  The result has the form

\[
\sup_{s\in I_{k+1}}H_{q,k+1}(s)
+
\int_{I_{k+1}}D_{q,k+1}(s)\,ds
\le
Cq^\sigma4^k(t^{-1}+r^{-2})
\iint_{Q_k}a^{q-2}F^q.
\tag{5.1}
\]

All right-side spatial integrals are taken on the outer cutoff/domain corresponding to `Q_k`; the finite-neighbor star is enlarged once at each nesting level but remains inside a bounded family by construction.  The factor `q^sigma` contains tensor contraction, chain-rule, and Young losses.

For the defect hierarchy,

\[
\sup_{s\in I_{k+1}}J_{m,k+1}(s)
+
\int_{I_{k+1}}X_{m,k+1}(s)\,ds
\le
Cm^\sigma4^k(t^{-1}+r^{-2})
\iint_{Q_k}a^{m-2}|E|^m.
\tag{5.2}
\]

Equations (5.1)--(5.2) are the corrected version of A03 equation (11.1) in the present notation, conditional on the exact tensor inequality and current cubic potential.

## 6. Infinite product and endpoint scales

From (5.1), spatial Sobolev applied to `v_{q,k}` yields

\[
M_{3q/2}(Q_{k+1})
\le CA_k^2\left[Cq^\sigma4^k(t^{-1}+r^{-2})M_q(Q_k)\right]^{3/2}.
\tag{6.1}
\]

Taking the `2/(3q)` power gives the recurrence

\[
M_{3q/2}(Q_{k+1})^{2/(3q)}
\le (CA_k^2)^{2/(3q)}
\left[Cq^\sigma4^k(t^{-1}+r^{-2})\right]^{1/q}
M_q(Q_k)^{1/q}.
\tag{6.2}
\]

For `q_{k+1}=3q_k/2`, the sums `sum 1/q_k` and `sum k/q_k` converge.  Neighbor and Sobolev comparability factors also enter with summable exponents.  With base `q0=2`,

\[
\|aF(t)\|_\infty
\le CA^2(t^{-1}+r^{-2})^{3/2}M_2(Q_0)^{1/2}.
\tag{6.3}
\]

If `t<=r^2` and the current energy loop gives `M_2(Q_0)<=tH_2<=t\Gamma_*^2/A^4`, then

\[
\|aF(t)\|_\infty\le C\Gamma_*/t.
\tag{6.4}
\]

For the defect with base `m0=6`, once fixed `J_6` persistence is proved,

\[
\|aE(t)\|_\infty
\le C\delta(r^2/t)^{1/3}.
\tag{6.5}
\]

The endpoint powers agree with A03's product script and with `workspace/scripts/step22_weak_moment_ledger.py` after the cutoff corrections.

## 7. Remaining mathematical content

The algebraic weights and endpoint powers are now consistent, but the following are still mathematical work:

1. prove the exact tensor inequality (2.1) for `-2a(Ric+g)`, including measure evolution, `F` regularization, inverse-metric terms, and all Hessian-`a` integrations by parts;
2. implement the finite-neighbor graph absorption rigorously for `S_alpha=A_alpha^4H_{2,alpha}`;
3. prove the graph-semigroup cubic potential `A^4H_3<=C Gamma^3/t` from the same current energy;
4. prove fixed `J_6` persistence before running the defect `m -> 3m/2` product;
5. prove the unweighted triangular defect estimate `Q'_alpha<=Cr^{-2}sum Q_beta` without curvature-only source terms;
6. obtain plateau curvature bounds over a short positive time interval and use exponential-pullback averaging for the calibrated Derdzinski contradiction.

Even if all these are achieved, the result addresses only the critical four-dimensional negative LeBrun/Ishida--LeBrun laboratory, not the positive branch, arbitrary four-manifolds, dimensions `n>=5`, or the full Yau 26 proposition.

## Files

- Exponent ledger: `workspace/scripts/step22_weak_moment_ledger.py`
- Current energy formulation: `workspace/notes/step22_current_energy_formulation.md`
- TTCS verification: `trace/ttcs/results/step22_ttcs01_verifier1_integration.md`
- A03 source: `Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md`
