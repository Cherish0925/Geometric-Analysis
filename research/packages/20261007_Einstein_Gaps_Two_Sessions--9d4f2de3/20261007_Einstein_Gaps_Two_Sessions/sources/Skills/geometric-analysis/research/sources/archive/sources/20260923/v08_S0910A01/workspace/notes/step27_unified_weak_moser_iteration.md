# Step 27: Unified weak Moser iteration for weighted curvature and defect

**CORRECTION (Step 30):** Step 29 correctly noticed that the direct
comparison of \(\|z_p\|_3^3\) with \(H_{3p/2}\) has a half-power cutoff-weight
gap, but its proposed ordinary unweighted-\(U\) Moser replacement was not
justified because the operator is still \(a\Delta\).  The weighted hierarchy is
repaired instead by the mixed time-slice estimate
\[
H_{3p/2}=\int (a^{p-2}f^p)^{1/2}z_p^2
\le H_p^{1/2}\|z_p\|_4^2,
\]
followed by Sobolev and the existing energy/dissipation bound for \(z_p\).
This supplies the desired \(p\mapsto3p/2\) recurrence with polynomial losses.
See `workspace/notes/step30_weighted_moser_and_family_repair.md` and
`workspace/scripts/step30_weighted_moser_family_repair.py`.  The shifted
curvature \(U=a(\operatorname{Rm}+G)\) remains valuable for velocity and
continuation identities, but not as an ordinary uniformly parabolic first-bound
Moser variable.

**CORRECTION (Step 32):** The Step 31 withdrawal of the positive-time endpoint
forms was itself unsupported.  A collapse-independent unnormalized Dirichlet
Sobolev constant is false, but no such constant is needed: in the fixed
convention
\(\|z\|_4^2\le C_S(\|\nabla z\|_2^2+r^{-2}\|z\|_2^2)\),
\(\beta=C_SH_2(0)^{1/2}\), the direct nested spacetime recurrence gives
\(\|aF(t)\|_\infty\lesssim\beta/t\) from the same-support curvature seed and
\(\|aE(t)\|_\infty\lesssim\delta(r^2/t)^{1/3}\) from fixed \(J_6\) persistence.
These are conditional on the tensor-energy, \(H_3\), \(J_6\), and \(Q\) estimates
from time zero; see `workspace/notes/step32_nested_moser_and_tensor_audit.md`.

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 0. Purpose and advance

This note replaces the two separate regularity programs (curvature Moser and
defect Moser) with one common iteration template.  The key structural advance
over Steps 24--26 is the **three-factor Hölder absorption**: the curvature
reaction is bounded using the positive-time cubic potential \(Y\) as a
coefficient, not as a direct critical threshold.  This removes the deteriorating
constant \(\beta<C/q\) that blocked all-exponent critical absorption and makes
the \(p\)-dependence polynomial (compatible with the Moser product).

Both the support-wide weighted curvature bound \(\|aF\|_\infty\le C\beta/t\)
and the support-wide weighted velocity bound
\(\|aE\|_\infty\le C\delta(r^2/t)^{1/3}\)
emerge from the same lemma with different seeds and the same Sobolev
cancellation structure verified in `step27_three_factor_absorption.py`.

**Correction to Step 26**: Yang B.1 cannot be invoked as a black box because
the defect equation has anisotropic \(\nabla^2a\cdot E\) contractions rather
than the scalar \(\chi\Delta\chi\) structure.  We use Yang's iteration
*template* (Appendix A, lines 963--1066), not its literal scalar hypotheses.

## 1. Setting

On one buffered selected support:
- flow \(\partial_tg=-2aE\), \(a=\chi^2\), \(E=\operatorname{Ric}+g\);
- \(\eta=1\) on \(\operatorname{supp}\chi\),
  \(\operatorname{supp}\nabla\eta\subset\{\chi=0\}\);
- \(F=(1+|\operatorname{Rm}|^2)^{1/2}\);
- relative Sobolev constant \(S=A_\Omega^2\sim r^2/\operatorname{Vol}(\Omega)^{1/2}\);
- positive-time q=3 weighted curvature moment \(Y(t)=\int aF^3\,d\mu_t\).

The q=2 and q=3 curvature estimates from Steps 24--25 give
\[
  S^2Y(t)\le\frac{C\beta^3}{t},\qquad 0<t\le\theta r^2,
\tag{1.1}
\]
where \(\beta=S\|F\|_{L^2(\operatorname{supp}\chi)}\) and the flow exists
with metric comparison on \([0,t]\).

## 2. Power-energy inequality

For a nonnegative function \(f\) on \((\operatorname{supp}\eta,g(t))\) and
exponent \(p\ge p_0\), define
\[
  H_p(f,t)=\int a^{p-2}f^p\,d\mu_t,\qquad
  D_p(f,t)=\int a^{p-1}f^{p-2}|\nabla f|^2\,d\mu_t,
\tag{2.1}
\]
\[
  z_p=a^{(p-1)/2}f^{p/2},\qquad
  R_p=\int a^{p-1}Ff^p\,d\mu_t.
\tag{2.2}
\]

From the geometric evolution of \(f=F\) or \(f\approx|E|\) under the cutoff
flow (Steps 25--26 tensor derivation, Codex report, A03 derivation), testing
against \(a^{p-2}f^{p-2}f\) and integrating by parts gives the schematic
power-energy inequality:

\[
\boxed{
  H_p'(f)+c_pD_p(f)\le C_pr^{-2}H_p(f)+C_pR_p+\text{source}_p.}
\tag{2.3}
\]

Step 28 correction and A03 alignment.  In the active-region formulation used
for the iteration, the curvature equation is taken in A03's general-\(p\)
form
\[
  K_p'+c\|\nabla Z_p\|_2^2
  \le Cp^2r^{-2}K_p+Cp\int\eta^2a^{p-1}F\Phi^p,
\]
for \(\Phi=F\), and the same form for regularized \(\Phi=|E|\).  The possible
zero-order contribution caused by using \(F=(1+|\operatorname{Rm}|^2)^{1/2}\)
is absorbed into \(Cp^Nr^{-2}K_p\) because \(F\ge1\) on the active region; it
is not a separate seed in the iteration.  For the defect equation there is no
curvature-only additive source: all terms contain \(E\), \(\nabla E\), or their
traces.

The constants have only polynomial growth in \(p\) (A03 records \(p^3\) after
absorption).  This is compatible with the time-cutoff recurrence below, but it
should not be exponentiated through a separate Gronwall factor at each \(p\).
The key cancellations:

1. Transition gradients: \(|da|^2/a=4|d\chi|^2\le Cr^{-2}\) removes the apparent
   \(a^{-1}\) degeneracy; this produces \(C_pr^{-2}H_p\).
2. Hessian of \(a\): after IBP, the cross term \(\nabla a\cdot\nabla\eta\) vanishes
   because \(\nabla a=2\chi\nabla\chi=0\) wherever \(\nabla\eta\ne0\).
3. The dissipation weight is \(a^{p-1}\) from the principal coefficient \(a\) in
   the equation and the testing weight \(a^{p-2}\).

For \(f=|E|\), the function \(|E|^p\) is smooth when \(E\ne0\) but needs
regularization at zeros.  Replace \(|E|\) by
\((|E|^2+\varepsilon)^{1/2}\) and pass to the limit; the power-energy
inequality (2.3) survives in the distributional sense.  For even integer
exponents \(p=2k\), the function \(|E|^{2k}\) is smooth and no regularization
is needed.

## 3. Three-factor absorption

**Lemma (Three-factor Hölder).** On the selected support,
\[
  R_p\le Y^{1/3}\,H_p^{1/3}\,\|z_p\|_4^{4/3}.
\tag{3.1}
\]

*Proof.* Factor the integrand:
\[
  a^{p-1}Ff^p=(aF^3)^{1/3}\cdot(a^{p-2}f^p)^{1/3}\cdot z_p^{4/3}.
\]
This is exact: the powers of \(a\) are \(\tfrac13+\tfrac{p-2}{3}+\tfrac{2(p-1)}{3}=p-1\),
of \(F\): \(1\), and of \(f\): \(\tfrac p3+\tfrac{2p}{3}=p\).

Apply Hölder with exponents \((3,3,3)\):
\[
  R_p\le\bigl(\textstyle\int aF^3\bigr)^{1/3}
  \bigl(\textstyle\int a^{p-2}f^p\bigr)^{1/3}
  \bigl(\textstyle\int z_p^4\bigr)^{1/3}
  =Y^{1/3}H_p^{1/3}\|z_p\|_4^{4/3}.\qquad\square
\]

**Gradient of \(z_p\).**  Since \(z_p=a^{(p-1)/2}f^{p/2}\),
\[
  \nabla z_p=\tfrac{p-1}{2}a^{(p-3)/2}f^{p/2}\nabla a
  +\tfrac p2 a^{(p-1)/2}f^{(p-2)/2}\nabla f.
\]
Using \(|\nabla a|^2/a=4|\nabla\chi|^2\le Cr^{-2}\):
\[
  \|\nabla z_p\|_2^2\le C_p D_p+C_p r^{-2}H_p.
\tag{3.2}
\]
On the stationary collar \(\{\nabla\eta\ne0\}\), both \(a=0\) and \(z_p=0\), so
\(\nabla\eta\) terms vanish.

**Sobolev embedding.** On the selected support with metric comparison,
\[
  \|z_p\|_4^2\le S\bigl(\|\nabla z_p\|_2^2+r^{-2}\|z_p\|_2^2\bigr)
  \le C_pS(D_p+r^{-2}H_p),
\tag{3.3}
\]
using \(\|z_p\|_2^2=\int a^{p-1}f^p\le H_p\) (since \(a\le1\)).

**Young's inequality.**  From (3.1) and (3.3):
\[
  R_p\le Y^{1/3}H_p^{1/3}\cdot\bigl[C_pS(D_p+r^{-2}H_p)\bigr]^{2/3}.
\]
Write \(R_p\le A\cdot B^{2/3}\) with \(A=Y^{1/3}H_p^{1/3}(C_pS)^{2/3}\),
\(B=D_p+r^{-2}H_p\).  Apply Young (\(ab^{2/3}\le\varepsilon b+C_\varepsilon a^3\)):
\[
  R_p\le\varepsilon(D_p+r^{-2}H_p)+C_\varepsilon C_p^2S^2YH_p.
\tag{3.4}
\]

Choosing \(\varepsilon\) so that \(\varepsilon\le c_p/(2C_p)\):
\[
\boxed{
  H_p'+\frac{c_p}{2}D_p
  \le\bigl(C_p'r^{-2}+C_p''S^2Y(t)\bigr)H_p.}
\tag{3.5}
\]

Here the active-region zero-order curvature contribution has been absorbed into
\(C_p'r^{-2}H_p\) using \(F\ge1\), and the defect equation has no curvature-only
source.  The curvature potential \(Y\) enters **linearly** as a coefficient, not
as a critical threshold that deteriorates with \(p\); Step 28 uses it inside the
time-cutoff recurrence below, rather than exponentiating it by a separate
Gronwall estimate at each exponent.

## 4. Moser iteration on a time slab \([t/2,t]\)

This section is corrected in Step 28 to match A03 Sections 5.2--5.3.  The
iteration follows Yang Appendix A as a time-cutoff recurrence, not as a
separate Gronwall estimate at each exponent.  Set \(\kappa=1+2/n=3/2\) in four
dimensions and \(p_k=p_0\kappa^k\).  On nested intervals
\([\tau_k,t]\),
\(\tau_0=t/2\), \(\tau_k=t(1-2^{-(k+1)})\), use a time cutoff supported in
\([\tau_k,t]\), equal to one on \([\tau_{k+1},t]\), and satisfying
\(|\zeta_k'|\le C4^k/t\).

On the slab \([t/2,t]\), the q=3 curvature layer gives the pointwise-in-time
coefficient
\[
  S^2Y(s)\le {C\beta^3\over s}\le {2C\beta^3\over t}.
\tag{4.1}
\]
After the three-factor absorption, the power inequality has the form
\[
  K_{p_k}'+c\|\nabla Z_{p_k}\|_2^2
  \le Cp_k^N\bigl(r^{-2}+\beta^3/t\bigr)K_{p_k},
\tag{4.2}
\]
with a fixed finite \(N\) (A03 obtains \(N=3\) after all cutoff and Young
losses).  The time-cutoff energy estimate gives
\[
  \sup_{[\tau_{k+1},t]}K_{p_k}
  +\int_{\tau_{k+1}}^t\|\nabla Z_{p_k}\|_2^2
  \le L_k\,\mathcal M_{p_k,k},
\tag{4.3}
\]
where
\[
  L_k=Cp_k^N4^k(t^{-1}+r^{-2}),
  \qquad
  \mathcal M_{p,k}=\int_{\tau_k}^t K_p(s)\,ds .
\]
The spatial Sobolev step and Hölder in time give
\[
  \mathcal M_{p_{k+1},k+1}
  \le C S\,(L_k\mathcal M_{p_k,k})^{3/2}.
\tag{4.4}
\]
Equivalently, with \(m_k=\mathcal M_{p_k,k}^{1/p_k}\),
\[
  m_{k+1}\le (CS)^{1/(\kappa p_k)}L_k^{1/p_k}m_k
  =(CS)^{2/(3p_k)}L_k^{1/p_k}m_k.
\tag{4.5}
\]
The reciprocal-exponent sum is
\[
  \sum_{k\ge0}{1\over p_k}
  ={1\over p_0}{\kappa\over\kappa-1}
  ={n+2\over 2p_0},
\tag{4.6}
\]
while the net Sobolev power is
\[
  {1\over\kappa}\sum_{k\ge0}{1\over p_k}={n\over2p_0}.
\tag{4.7}
\]
Moreover \(\sum_k(\log L_k)/p_k<\infty\), because \(p_k\) grows geometrically
whereas \(\log L_k\) grows only like \(k+\\log p_k\).  Thus polynomial
\(p\)-growth remains harmless inside the recurrence.

The endpoint form used below is therefore
\[
  \|a f(t)\|_\infty
  \le C S^{n/(2p_0)} t^{-(1+n/2)/p_0}
  \bigl(\textstyle\int_{t/2}^t H_{p_0}(s)\,ds\bigr)^{1/p_0},
\tag{4.8}
\]
with the convergent product absorbed into \(C\).

## 5. Curvature output: \(f=F\), \(p_0=3\)

**Seed.** \(H_3(F)=\int aF^3=Y\).  From (1.1):
\[
  \int_{t/2}^t Y(s)\,ds\le\frac{C\beta^3}{S^2}\ln2.
\tag{5.1}
\]

**Moser exponents.** \(n/(2p_0)=2/3\), \((1+n/2)/p_0=1\).

**Volume cancellation.**  The potential condition from (1.1) gives
\(\mu=\beta/S^{2/3}\) (time-independent), and
\[
  S^2\mu^3=\beta^3.
\tag{5.2}
\]
The output is
\[
  \|aF(t)\|_\infty\le C\cdot S^{2/3}\cdot t^{-1}\cdot
  \bigl(C\beta^3/S^2\bigr)^{1/3}
  =C\cdot S^{2/3}\cdot t^{-1}\cdot\frac{\beta}{S^{2/3}}
  =\frac{C\beta}{t}.
\tag{5.3}
\]
The Sobolev factor \(S^{2/3}\) cancels exactly between the Moser prefactor and
the seed.  Since \(\beta\le Cr^2\sqrt{1+K_0}\):
\[
\boxed{
  \|a\operatorname{Rm}(t)\|_\infty
  \le\|aF(t)\|_\infty\le\frac{Cr^2\sqrt{1+K_0}}{t}.}
\tag{5.4}
\]
This is a support-wide weighted curvature bound, valid for all
\(0<t\le\theta r^2\), **independent of collapsed volume**.  It is sufficient
for:
- Yang/Wang extension mechanism;
- Shi-type weighted derivative estimates;
- plateau interior curvature \(|\operatorname{Rm}|\le C/t\) (where \(a=1\)).

## 6. Defect output: \(f=|E|\), \(p_0=6\)

**Seed.** \(H_6(|E|)=J_6=\int a^4|E|^6\).  From fixed-exponent persistence
(Step 26, inequality (2.9)):
\[
  J_6(t)\le e^{C\theta}J_6(0)\le C\delta^6\operatorname{Vol}(\Omega).
\tag{6.1}
\]
Therefore
\[
  \int_{t/2}^t J_6(s)\,ds\le C\delta^6\operatorname{Vol}(\Omega)\cdot t.
\tag{6.2}
\]

**Moser exponents.** \(n/(2p_0)=1/3\), \((1+n/2)/p_0=1/2\).

**Volume cancellation.**  The output is
\[
  \|aE(t)\|_\infty\le C\cdot S^{1/3}\cdot t^{-1/2}\cdot
  \bigl(C\delta^6\operatorname{Vol}(\Omega)\cdot t\bigr)^{1/6}.
\tag{6.3}
\]
Substituting \(S=r^2/V^{1/2}\) with \(V=\operatorname{Vol}(\Omega)\):
\[
  S^{1/3}\cdot V^{1/6}=(r^2/V^{1/2})^{1/3}\cdot V^{1/6}
  =r^{2/3}/V^{1/6}\cdot V^{1/6}=r^{2/3}.
\tag{6.4}
\]
The volume factor cancels exactly.  Collecting:
\[
\boxed{
  \|aE(t)\|_\infty\le C\delta\left(\frac{r^2}{t}\right)^{1/3},
  \qquad 0<t\le\theta r^2.}
\tag{6.5}
\]

**Metric drift.**
\[
  V(\theta r^2)=\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
  \le C\delta r^{2/3}\int_0^{\theta r^2}t^{-1/3}\,dt
  =\frac{3C}{2}\delta\theta^{2/3}r^2.
\tag{6.6}
\]
This is \(O(\delta r^2)\), tending to zero along the near-critical sequence.
For \(\delta\) sufficiently small (depending on \(\theta\) and the
bilipschitz tolerance \(\varepsilon_{\rm met}\)):
\[
\boxed{
  e^{-2V}g_0\le g(\theta r^2)\le e^{2V}g_0
  \quad\text{on all of }\operatorname{supp}\chi.}
\tag{6.7}
\]
This self-improving metric comparison closes the first-exit bootstrap for
Sobolev control, cutoff-gradient bounds, and \(\beta\) persistence.

## 7. Why one lemma suffices

The three-factor absorption treats `Y` as a time-dependent coefficient in the
power-energy inequality (3.5), and the time-cutoff recurrence in §4 prevents
polynomial `p`-losses from being exponentiated at each step.  The Moser
iteration is the same Yang Appendix A mechanism for both functions.  The only
difference between curvature and defect is the seed exponent and the initial
data source:

| quantity | \(f\) | \(p_0\) | seed | \(S^{n/(2p_0)}\) | volume factor | net output |
|----------|-------|---------|------|-------------------|---------------|------------|
| curvature | \(F\) | 3 | \(Y\le C\beta^3/(S^2t)\) | \(S^{2/3}\) | \(\beta/S^{2/3}\) from seed | \(C\beta/t\) |
| defect | \(\|E\|\) | 6 | \(J_6\le C\delta^6V\) | \(S^{1/3}\) | \(V^{1/6}\) from seed | \(C\delta(r^2/t)^{1/3}\) |

In both cases the volume-dependent Sobolev factor cancels against the volume
in the seed.  This is a four-dimensional coincidence:
\(n/(2p_0)=2/3\) and \(1/3\) match the volume exponents
\(V^{-1/3}\) and \(V^{-1/6}\) in \(S\) against \(V^{1/3}\) and \(V^{1/6}\) in
the seed.

## 8. Why Yang B.1 is used as a template, not a black box

Yang's Theorem B.1 (source lines 1127--1136) assumes the scalar structure
\[
  \partial_tf\le\chi^2(\Delta f+uf)+2a\chi|\nabla\chi||\nabla f|+b(|\nabla\chi|^2-\chi\Delta\chi)f.
\]
The defect equation instead has
\[
  \partial_tE=a(\Delta_LE-2E)+\mathcal C_a(E),
\]
where the Hessian-cutoff terms \(\mathcal C_a\) include anisotropic contractions
\(\nabla^2a\cdot E\), not the scalar combination \(\chi\Delta\chi\cdot f\).
After integration by parts in the power-energy estimate, these produce
controlled coefficients (polynomial in \(p\), bounded by cutoff-gradient
quantities), but they do not reduce pointwise to Yang's scalar lower-order
structure.

What transfers from Yang's proof is the **iteration architecture**:
energy inequality \(\to\) Sobolev step \(\to\) time-cutoff \(\to\) Moser product.
The three-factor absorption replaces Yang's use of an \(L^{q/2}\) potential
norm with the spacetime \(Y\) moment; the Moser product converges for the same
reason (polynomial coefficient growth, geometric exponent decay).

## 9. Required inputs (conditional)

The output (5.4) and (6.5) are conditional on:

1. **Power-energy inequality (2.3)** with polynomial \(p\)-dependence for both
   \(f=F\) and \(f=|E|\).  The tensor derivation in Steps 25 and 26 (and the
   Codex report) supplies a schematic version.  The remaining work is full
   index-level formulas including moving-norm, moving-volume, Lichnerowicz
   reaction, Hessian IBP, Kato regularization for \(|E|\), and exact constant
   tracking for the first several \(p_k\).

2. **Positive-time q=3 curvature potential** (1.1).  This comes from the q=2
   and q=3 energy estimates (Steps 24--25) and is itself conditional on the q=2
   critical absorption.  The three-factor method also applies to the q=2 estimate
   itself, with \(Y(0)\) replacing the time-evolved \(Y(t)\); the initial-energy
   critical product \(\beta_0\) is used for the first absorption, then the
   positive-time \(Y\) estimate feeds back.

3. **Fixed-exponent \(J_6\) persistence** (6.1).  This is Step 26, inequality
   (2.9), using the same three-factor absorption at \(p=6\).

4. **Smooth existence and continuation** of the cutoff flow to \(\theta r^2\).
   The weighted curvature bound (5.4) is what Yang/Wang extension needs.  For the
   normalized equation \(\partial_tg=-2\chi^2(\operatorname{Ric}+g)\), the
   DeTurck construction with transported coefficient recovers the fixed spatial
   \(\chi^2\) after pullback.  The lower-order \(-2\chi^2g\) is compactly
   supported with no second derivatives.

5. **Metric comparison and Sobolev persistence.** Controlled by (6.7).

The first-exit bootstrap couples these: assume all conditions hold on
\([0,T)\); improve via (5.4), (6.5), (6.7); extend by Wang to \(T+\varepsilon\).
This is the Yang Section 9 pattern.

## 10. Connection to the downstream route

After the weighted estimates:

1. **Plateau regularity.** On \(\{a=1\}\), (5.4) gives
   \(|\operatorname{Rm}|\le C\beta/t\), which is a standard parabolic
   curvature bound.  Shi estimates then give derivative bounds.

2. **Global defect preservation.** By the Step 25 identity,
   \(Q_{\rm global}(t)\le e^{C\theta}Q_{\rm global}(0)\le C\delta^2\operatorname{Vol}(M)\cdot A\).
   Since \(\operatorname{Vol}(M)/A=O(1)\), \(Q_{\rm global}/A\to0\).

3. **Terminal calibration.** The mixed SW and tensor-gap inequalities
   from Steps 3--8 apply to the terminal metric \(g(\theta r^2)\).  These
   nonnegative deficit densities are averaged over bounded-curvature plateaux,
   whose sequence-independent volume fraction (however small) suffices under
   metric comparability.

4. **Smooth Einstein germ.** Bounded curvature and
   \(W^{2,p}\) convergence in harmonic charts yield a smooth Einstein limit
   carrying the calibrated Weyl spectrum.

5. **Derdziński contradiction.** The calibrated spectrum conflicts with
   the local Kähler structure forced by harmonic \(W^+\) with at most two
   eigenvalues.

Steps 1--5 are conditional consequences of the weighted estimates.  The
analytic core of the negative four-dimensional route is now reduced to proving
the power-energy inequality (2.3) with the stated \(p\)-dependence.

## 11. What this does not prove

- The full Yau Problem 26 proposition for all dimensions \(n\ge2\).
- The positive branch in any dimension.
- The negative branch for arbitrary four-manifolds outside the LeBrun/Ishida--LeBrun
  laboratory.
- Dimensions \(n\ge5\), where positive collapse can be Einstein-compatible.
- Lean 4 formalization.

## References

- `workspace/notes/step25_tensor_energy_derivation.md` (q=2 and Q schematic)
- `workspace/notes/step26_weighted_velocity_and_local_flow.md` (fixed-p J_p, Yang source)
- `workspace/codex_loop/work/tensor_energy_derivation.md` (Codex tensor ledger)
- `workspace/scripts/step27_three_factor_absorption.py` (algebraic verification)
- Yang source: `Knowledge/objects/papers/Convergence-of-riemannian-manifolds-with-integral-bounds--2b2a6e7ac566--6b3174861309/object.md`,
  Appendix A (lines 963--1066), Section 8--9 (lines 787--878), Appendix B (lines 1111--1136)
- Wang/Yang pseudolocality: `Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md`
