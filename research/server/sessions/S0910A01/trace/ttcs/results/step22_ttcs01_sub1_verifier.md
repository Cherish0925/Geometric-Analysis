# TTCS Independent Branch Record

```json
{
  "step_id": 22,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step22_current_energy_formulation.md",
    "Sessions/S0910A01/workspace/notes/step22_weak_nested_moment_estimate.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step22.md",
    "Sessions/S0910A01/workspace/scripts/step22_energy_normalization.py",
    "Sessions/S0910A01/workspace/scripts/step22_first_exit_energy.py",
    "Sessions/S0910A01/workspace/scripts/step22_weak_moment_ledger.py",
    "Sessions/S0910A03/workspace/notes/step20_weighted_wang_hierarchy_and_whitney_correction.md"
  ]
}
```

## Task

Verify the Step 22 repair to the cutoff-flow smoothing argument for Yau Problem 26's four-dimensional negative LeBrun/Ishida-LeBrun laboratory. Read the corrected notes and scripts. The scientific questions: (1) Does the correction correctly distinguish component energy int_U F^2 <= M Vol(U) from the false Whitney-volume-normal bound int_W F^2 <= C M Vol(W)? (2) Does the retained scale-invariant Whitney estimate ell^4 average_W F^2 and the Sobolev product A_W^2||F||_2 <= C r^2 sqrt(M) follow with the right powers? (3) Is the current component first-exit formulation Gamma(t)=sup A_alpha^2 H_2,alpha(t)^{1/2} the right way to prove energy persistence and cubic potential A^4 H_3 <= C Gamma^3/t? (4) Does the weak nested moment estimate use the correct weights H_q=int eta^2 a^(q-2)F^q and v_q=eta a^((q-1)/2)F^(q/2), and are the Holder/Sobolev exponents, finite-neighbor terms, and endpoint scalings scientifically consistent? Identify any remaining mathematical gaps or wrong inferences, especially about transition curvature closeness, metric displacement, unweighted defect Q, and plateau bounded-curvature needs. Do not decide the whole research route; give a mathematical verification memo.

## Output

# Mathematical verification memo

## 1. Component energy versus Whitney-ball energy

The correction in `step22_current_energy_formulation.md`, Section 1, is mathematically right. From

\[
\int_U F^2\,d\mu\le M\operatorname{Vol}(U)
\]

and \(W\subset U\), one obtains only

\[
\int_WF^2\le M\operatorname{Vol}(U),
\]

not a bound proportional to \(\operatorname{Vol}(W)\). Curvature energy may concentrate entirely in \(W\), so

\[
\fint_WF^2
\]

can increase by the volume ratio \(\operatorname{Vol}(U)/\operatorname{Vol}(W)\).

There is a minor geometric detail in (1.3). Since \(y\in B_{4r}(p)\),

\[
B_{5r}(p)\subset B_{9r}(y),
\]

rather than \(B_{5r}(p)\subset B_{5r}(y)\). Assuming the initial metric has the required Ricci lower bound or local volume-doubling estimate, Bishop–Gromov gives

\[
\frac{\operatorname{Vol}(B_\ell(y))}
     {\operatorname{Vol}(B_{9r}(y))}
\ge c\left(\frac{\ell}{9r}\right)^4.
\]

Because \(\operatorname{Vol}(U)\le\operatorname{Vol}(B_{9r}(y))\), this implies

\[
\operatorname{Vol}(W)\ge c\left(\frac{\ell}{9r}\right)^4\operatorname{Vol}(U).
\]

The factor \(9\) may be replaced by \(5\) after changing the constant \(b\), so the powers in (1.3)–(1.4) are unaffected. The volume comparison must come from the initial geometry; at later times it can be transferred to the same fixed domains using the bilipschitz estimate. Bilipschitz equivalence alone does not create a new Bishop–Gromov theorem for \(g(t)\).

Consequently,

\[
\fint_WF^2
\le C M\left(\frac r\ell\right)^4,
\qquad
\ell^4\fint_WF^2\le CMr^4.
\]

Thus the local mean may indeed grow as \(\chi_0^{-4}\) when \(\ell=cr\chi_0\).

## 2. Whitney Sobolev cancellation

The Sobolev scaling is also correct. In dimension four, the relative inequality has the form

\[
\|u\|_{L^4(W)}^2
\le A_W^2
\left(
\int_W|\nabla u|^2+\ell^{-2}\int_Wu^2
\right),
\]

with

\[
A_W^2\le C\ell^2\operatorname{Vol}(W)^{-1/2}.
\]

Using the component budget,

\[
\begin{aligned}
A_W^2\|F\|_{L^2(W)}
&\le
C\ell^2\operatorname{Vol}(W)^{-1/2}
\bigl(M\operatorname{Vol}(U)\bigr)^{1/2}\\
&\le
C\ell^2\sqrt M\left(\frac r\ell\right)^2\\
&=
Cr^2\sqrt M.
\end{aligned}
\]

The cancellation is exactly four-dimensional. The script `step22_energy_normalization.py` correctly illustrates both facts: the normalized mean grows like \(\chi_0^{-4}\), while \(\ell^4\fint_WF^2\) and \(A_W^2\|F\|_2\) remain independent of \(\chi_0\). The script is a scaling computation, not a substitute for the geometric volume and Sobolev theorems.

## 3. Current component energy and the cubic potential

The quantity

\[
\gamma_\alpha(t)=A_\alpha^2H_{2,\alpha}(t)^{1/2},
\qquad
\Gamma(t)=\sup_\alpha\gamma_\alpha(t),
\]

is the correct critical parameter. Indeed, with an outer cutoff equal to one on the support of the tested function,

\[
H_{3,\alpha}
=
\int aF(\eta F)^2
\le
\|F\|_{L^2(\widehat U_\alpha)}
\|\eta a^{1/2}F\|_4^2
\le
C\gamma_{\widehat\alpha}
\left(D_{2,\alpha}+r^{-2}H_{2,\widehat\alpha}\right).
\]

This explains why current \(L^2\) curvature energy, rather than initial energy plus metric equivalence, is needed for absorption.

Several localization details remain unresolved in equations (2.3)–(2.7):

1. **Outer energy is required.**  
   If \(H_{2,\alpha}=\int\eta_\alpha^2F^2\), it does not control
   \(\int_{\operatorname{supp}\eta_\alpha}F^2\), because \(\eta_\alpha\) becomes small near its cutoff edge. The critical parameter must use an outer cutoff \(\widehat\eta_\alpha\equiv1\) on the entire region where the inner test is active.

2. **Neighbor dissipation cannot be absorbed componentwise as written.**  
   From
   \[
   H'_{2,\alpha}+cD_{2,\alpha}
   \le C\sum_{\beta\sim\alpha}
   \bigl(r^{-2}H_{2,\beta}+H_{3,\beta}\bigr)
   \]
   and
   \[
   H_{3,\beta}\le C\Gamma(D_{2,\beta}+r^{-2}H_{2,\beta}),
   \]
   the right side contains \(D_{2,\beta}\) for neighboring \(\beta\). Those terms cannot be absorbed into \(D_{2,\alpha}\) one equation at a time. Either each reaction must be paired with its own dissipation before the neighbor enlargement, or a weighted sum of graph equations must be used.

3. **The Sobolev coefficients must remain inside the graph estimate.**  
   Equation (2.6) controls \(\sup H_{2,\alpha}\), but this does not directly control
   \(\sup A_\alpha^4H_{2,\alpha}\) when component volumes vary. The natural graph variable is
   \[
   S_\alpha=A_\alpha^4H_{2,\alpha}=\gamma_\alpha^2.
   \]
   Neighboring fixed-radius balls have comparable volumes, hence comparable \(A_\alpha\), under the stated initial volume geometry. One then obtains schematically
   \[
   S_\alpha'
   \le Cr^{-2}\sum_{\beta\sim\alpha}
   \frac{A_\alpha^4}{A_\beta^4}S_\beta,
   \]
   and bounded neighbor ratios permit a Dini-supremum Gronwall argument independent of the number of components.

Subject to those localization repairs, the route to

\[
A_\alpha^4H_{3,\alpha}(t)
\le \frac{C\Gamma_*^3}{t}
\]

is sound: the \(q=2\) inequality supplies spacetime \(H_3\), the fixed \(q=3\) inequality propagates \(H_3\) forward, and backward averaging removes any need for an initial \(H_3(0)\) estimate.

The finite-neighborhood statement in (3.4) needs refinement. A coupled graph inequality generally propagates through paths of arbitrary graph length, although long paths have small semigroup weights for \(t\ll r^2\). A graph-semigroup estimate or an exponentially weighted local sum gives

\[
A_\alpha^4H_{3,\alpha}(t)
\le
\frac{C}{t}
\sum_\beta
\bigl[e^{C(t/r^2)\mathcal A}\bigr]_{\alpha\beta}
A_\beta^4\!\int_0^tH_{3,\beta}(s)\,ds,
\]

whose row sum is bounded by \(e^{CNt/r^2}\). That produces the desired \(\Gamma_*^3/t\) scale without dependence on the total number of components. A fixed finite star does not follow automatically from the displayed graph system.

`step22_first_exit_energy.py` correctly evaluates the scalar graph Gronwall factor after the differential system has been obtained. It does not address the neighbor-dissipation issue, outer cutoffs, or varying Sobolev coefficients.

## 4. Weighted moment hierarchy

The central weights are correct:

\[
H_q=\int\eta^2a^{q-2}F^q,
\qquad
v_q=\eta a^{(q-1)/2}F^{q/2}.
\]

They satisfy

\[
v_q^2=\eta^2a^{q-1}F^q,
\qquad
Fv_q^2=\eta^2a^{q-1}F^{q+1},
\]

and the endpoint is

\[
\left(a^{q-2}F^q\right)^{1/q}\longrightarrow aF.
\]

The \(a,F\) exponents in the Hölder interpolation are correct. There is, however, a cutoff-power discrepancy in equations (2.1)–(2.3) of `step22_weak_nested_moment_estimate.md`:

\[
H_{2q,k}^{1/2}
=
\left(\int\eta_k^2a^{2q-2}F^{2q}\right)^{1/2}
\]

is not equal to

\[
\|v_{q,k}\|_4^2
=
\left(\int\eta_k^4a^{2q-2}F^{2q}\right)^{1/2}.
\]

The required reaction estimate can nevertheless be recovered with an outer cubic cutoff. If \(\xi_k\equiv1\) on \(\operatorname{supp}\eta_k\), set

\[
H_{3,\widehat k}=\int\xi_k^2aF^3.
\]

Then

\[
R_q
\le
H_{3,\widehat k}^{1/3}K_q^{2/3},
\]

where

\[
K_q=\int\eta_k^3a^{3q/2-2}F^{3q/2}.
\]

Cauchy–Schwarz gives

\[
K_q
\le
H_{q,k}^{1/2}
\left(\int\eta_k^4a^{2q-2}F^{2q}\right)^{1/2}
=
H_{q,k}^{1/2}\|v_{q,k}\|_4^2.
\]

Therefore

\[
R_q
\le
CA_k^{4/3}H_{3,\widehat k}^{1/3}H_{q,k}^{1/3}
\left(D_{q,k}+L_kH_{q,\mathrm{outer}}\right)^{2/3},
\]

and Young’s inequality yields the intended coefficient

\[
\varepsilon D_{q,k}
+
C\varepsilon^{-2}A_k^4H_{3,\widehat k}H_{q,\mathrm{outer}}.
\]

Thus the power mechanism survives, but the displayed equalities need outer/inner cutoff notation. `step22_weak_moment_ledger.py` verifies only the \(a,F\) monomials; it does not track the powers of \(\eta\).

Similarly, the spatial cutoff term

\[
\int a^{q-1}|d\eta_k|^2F^q
\]

cannot be bounded by \(H_{q,k}=\int\eta_k^2a^{q-2}F^q\) using the same \(\eta_k\). It is bounded by the uncut moment on an outer region. The Whitney coefficient itself is right:

\[
a|d\eta_k|^2
\lesssim
\chi_0^2(2^k/\ell)^2
\lesssim 4^kr^{-2}.
\]

### Time-cylinder indexing

The intervals in Section 3 are ordered in the wrong direction:

\[
I_k=[t/2+2^{-k-2}t,t].
\]

For example,

\[
I_0=[3t/4,t],
\qquad
I_1=[5t/8,t],
\]

so \(I_1\) is larger than \(I_0\). A time cutoff supported in \(I_k\) therefore cannot equal one on \(I_{k+1}\). One suitable shrinking family is

\[
I_k=
\left[
\frac t2+\frac t4(1-2^{-k}),\,t
\right],
\]

which starts at \(t/2\) and shrinks toward \([3t/4,t]\). Its transition derivatives are bounded by \(C2^k/t\), hence also by the stated \(C4^k/t\).

After correcting the spatial and temporal nesting, the parabolic recurrence and endpoint powers are consistent:

\[
\|aF(t)\|_\infty
\le
CA^2(t^{-1}+r^{-2})^{3/2}M_2^{1/2}
\le
\frac{C\Gamma_*}{t}
\quad (t\le r^2).
\]

For the defect hierarchy with \(m_0=6\),

\[
\|aE(t)\|_\infty
\le
CA^{2/3}(t^{-1}+r^{-2})^{1/2}M_6^{1/6}
\le
C\delta(r^2/t)^{1/3}.
\]

The last substitution requires positive-time persistence of \(J_6\), not merely \(J_6(0)\le\delta^6V\). For this fixed exponent one can use direct critical absorption:

\[
\int Fz_6^2
\le
A^2\|F\|_2(D_6+r^{-2}J_6)
\le
\Gamma_*(D_6+r^{-2}J_6).
\]

This avoids integrating the singular \(H_3(s)\sim s^{-1}\) potential from time zero.

## 5. Transition, metric displacement, and plateau geometry

The removal of transition-curvature closeness is correct. From

\[
\partial_tg=-2aE
\]

and the pointwise velocity estimate,

\[
\int_0^T|aE|\,dt
\le
C\delta r^{2/3}T^{2/3}
=
C\delta r^2
\quad\text{for }T=\theta r^2,
\]

one obtains bilipschitz control of \(g(T)\) relative to \(g(0)\). This supplies no control of second spatial derivatives of the metric, so it gives no estimate for

\[
\operatorname{Rm}(T)-\operatorname{Rm}(0).
\]

Also, \(|a\operatorname{Rm}|\) says nothing pointwise where \(a\) is very small.

On an open plateau buffer where \(a=1\),

\[
|a\operatorname{Rm}(T)|\le Cr^{-2}
\]

does yield a terminal curvature bound. For smooth geometric convergence or a controlled Einstein germ, a terminal curvature bound alone does not provide curvature derivatives or injectivity radius. A curvature bound on a full interval such as \([T/2,T]\), on a slightly larger plateau buffer, allows interior normalized-Ricci-flow derivative estimates. Collapse still requires the exponential-pullback formulation rather than ordinary injective coordinate balls.

## 6. Unweighted defect energy

The triangular form

\[
Q_\alpha'(t)
\le
Cr^{-2}\sum_{\beta\sim\alpha}Q_\beta(t)
\]

is structurally plausible because the evolution of \(E=\operatorname{Ric}+g\) under \(-2aE\) is homogeneous in \(E\): if \(E=0\), the velocity and the variation of \(E\) vanish. Expanding derivatives of \(aE\) produces terms involving \(E,\nabla E\), and fixed derivatives of \(a\), but no curvature-only source should remain.

This equation is not yet derived in the supplied material. The exact tensor computation must show that testing by \(\eta^2E\) produces only terms absorbable by

\[
\int \eta^2a|\nabla E|^2,
\qquad
\Gamma_*\int \eta^2a|\nabla E|^2,
\qquad
r^{-2}\int_{\mathrm{outer}}|E|^2,
\]

with no additive curvature dissipation. Once that is established, summing over a bounded-overlap partition is appropriate for global \(Q\), since the sum of local initial energies is comparable to the global initial energy. Outside the support of \(a\), the metric is stationary.

## 7. Net mathematical status

The Step 22 repair successfully fixes the central normalization error and preserves the four-dimensional critical mechanism:

- component energy does not imply Whitney-volume-normal energy;
- \(\ell^4\fint_WF^2\) and \(A_W^2\|F\|_2\) have the stated powers;
- current critical energy is the right first-exit quantity;
- the \(a^{q-2}\) hierarchy, Hölder powers, infinite product, and terminal \(aF,aE\) scalings are correct.

The remaining proof substance is concentrated in the exact tensor inequalities, outer/inner cutoff placement, absorption of neighbor dissipation, Sobolev-weighted graph propagation, corrected time nesting, fixed-\(J_6\) persistence, the triangular \(Q\) computation, and smooth existence/extension for the normalized spatially cut off flow. The scripts verify scaling and exponent ledgers but do not settle those tensor and localization steps.