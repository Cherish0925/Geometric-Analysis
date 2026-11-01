# TTCS Independent Branch Record

```json
{
  "step_id": 16,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/workspace/codex_loop/work/proved_vs_open.md",
    "Sessions/S0910A03/workspace/notes/step15_L2_chain_and_separated_demands.md",
    "Sessions/S0910A03/workspace/notes/step3_boundary_near_saturation.tex",
    "Sessions/S0910A03/workspace/notes/step6_local_projector_obstruction_and_collapse_reduction.tex"
  ]
}
```

## Task

Review the monopole-amplitude/eigenline transfer needed after selecting bounded-curvature exponential pullback charts in the fixed critical Ishida-LeBrun sequence. Use the exact quantitative deficit decomposition in the Codex report. Suppose at an evolved time one has global Q=∫|Ric+g|²→0 and hence the scalar-Weyl completion-square profile, and suppose bounded sectional curvature plus derivative estimates hold on a positive-volume buffered set P. Identify a single nonnegative density or finite family of densities whose small global integrals and exponential-chart averaging would guarantee on one pullback chart: (i) a quantitatively nonzero limiting harmonic self-dual form, (ii) lowest-W+ eigenvalue saturation, and (iii) enough compactness to pass these to a local Einstein limit. Carefully distinguish harmonic representative H_a, spinor quadratic form ψ/φ, the fact the selected sign class may depend on metric/time, and any equations not preserved by cutoff flow. Decide whether the existing identities actually make such joint chart selection possible, or expose an exact missing estimate. Do not use unique continuation as a substitute for quantitative local amplitude.

## Output

# Scientific verification memo

## 1. Selection of the monopole class at the evolved metric

Write the evolved metrics as \(\bar g_i\), and set

\[
E_i=\operatorname{Ric}_{\bar g_i}+\bar g_i,\qquad
Q_i=\int_M |E_i|^2\,d\mu_i\longrightarrow0,
\]

\[
w_i=|W_i^+|,\qquad q_i=-s_i+\sqrt6\,w_i,\qquad
t_i=s_i+8\sqrt6\,w_i.
\]

All monopole and harmonic objects below must be constructed for \(\bar g_i\), not transported from the initial metric.

For the finite Ishida–LeBrun sign family, choose \(a_i\) so that

\[
p_i=(a_i^+)^2\ge \operatorname{Av}_a(a^+)^2\ge A.
\]

Chern–Gauss–Bonnet and the completion square give

\[
K_i:=\frac1{72\pi^2}\int q_i^2
 \le A+\frac32R_i,
\qquad
R_i=\frac1{8\pi^2}\int|\operatorname{Ric}_i^\circ|^2.
\]

Thus the primitive deficit satisfies

\[
0\le \Delta_i:=\int q_i^2-72\pi^2p_i
\le108\pi^2R_i
\le \frac{27}{2}Q_i\longrightarrow0. \tag{1}
\]

The selected \(a_i\) may vary with \(i\). Since the sign family is finite on a fixed manifold, a subsequence has \(a_i=a\). Nothing local requires this stabilization, but it is useful when identifying the determinant line.

The completion profile also yields

\[
\int t_i^2\le108Q_i,\qquad
\int(s_i+4)^2\le4Q_i,
\]

and the exact relation

\[
q_i-\frac92=\frac18t_i-\frac98(s_i+4)
\]

implies

\[
\left\|q_i-\frac92\right\|_2^2\le C Q_i. \tag{2}
\]

## 2. A finite family of pointwise \(\ge0\) densities

Assume for the moment that the optimal-weight decomposition from the Codex report applies to \(\bar g_i\). Choose a diagonal sequence of smooth regularized weights \(f_i\) and rescaled monopoles

\[
D_{A_i}\Phi_i=0,\qquad -iF_{A_i}^+=f_i\sigma(\Phi_i).
\]

Use the report’s notation

\[
\psi_i=2\sqrt2\,\sigma(\Phi_i),\qquad
\varphi_i=\frac32\psi_i,\qquad
u_i=|\varphi_i|,
\]

and let \(H_i=H_{a_i}\) be the \(\bar g_i\)-harmonic self-dual representative of \(a_i^+\). Then

\[
f_i\varphi_i=3\sqrt2(-iF_{A_i}^+), \tag{3}
\]

but \(H_i\), \(\psi_i\), and \(\varphi_i\) are three distinct objects:

* \(H_i\) is closed, coclosed, self-dual, and satisfies
  \(\int|H_i|^2=p_i\).
* \(iF_{A_i}^+\) has harmonic projection \(2\pi H_i\), but need not itself be harmonic.
* \(\psi_i,\varphi_i\) are spinor quadratic forms and need not be closed or harmonic.

A useful single density is the sum

\[
\begin{aligned}
\mathcal G_i={}&|E_i|^2+
 \left(q_i-\frac92\right)^2\\
&+\left(|2\pi H_i|-\frac{q_i}{3\sqrt2}\right)^2\\
&+\left|f_i\varphi_i+6\sqrt2\pi H_i\right|^2\\
&+2\left[
 W_i^+(\psi_i,\psi_i)
 +\sqrt{\frac23}\,w_i|\psi_i|^2
 \right].                                                     \tag{4}
\end{aligned}
\]

Every summand is pointwise \(\ge0\). For the last one, the algebraic estimate for a trace-free symmetric endomorphism of a three-dimensional Euclidean space is

\[
W(v,v)\ge-\sqrt{\frac23}|W|\,|v|^2.
\]

The quantitative decomposition gives

\[
\int\left|f_i\varphi_i+6\sqrt2\pi H_i\right|^2
 =18J_{A_i}\le\Delta_i+o(1),                                  \tag{5}
\]

\[
\int\left(|2\pi H_i|-\frac{q_i}{3\sqrt2}\right)^2
 \le\frac{2}{9}\Delta_i+o(1),                                 \tag{6}
\]

and

\[
2\int\left[
 W_i^+(\psi_i,\psi_i)
 +\sqrt{\frac23}\,w_i|\psi_i|^2
 \right]
 \le\frac4{27}\Delta_i+o(1).                                  \tag{7}
\]

Together with (1)–(2),

\[
\int_M\mathcal G_i\longrightarrow0.                            \tag{8}
\]

This density simultaneously carries the Einstein defect, calibrated curvature profile, quantitative harmonic-form amplitude, curvature-to-harmonic projection, and lowest-eigenline error.

## 3. Replacing the spinor density by a harmonic-form eigenline density

On a buffered region \(U_i\) where \(W_i^+\) and the relevant weights are uniformly bounded, define

\[
B_i=W_i^++\sqrt{\frac23}\,w_i I_{\Lambda^+},
\qquad
\mathfrak e_i=2\langle B_iH_i,H_i\rangle\ge0.                  \tag{9}
\]

Set

\[
\widetilde H_i=-\frac{f_i\varphi_i}{6\sqrt2\pi}
              =-\frac{f_i\psi_i}{4\sqrt2\pi}.
\]

Equation (5) says

\[
\|H_i-\widetilde H_i\|_2^2
\le\frac{\Delta_i+o(1)}{72\pi^2}.                              \tag{10}
\]

Moreover, if \(d_{{\rm eig},i}\) denotes the last density in (4), then

\[
2\langle B_i\widetilde H_i,\widetilde H_i\rangle
 =\frac{f_i^2}{32\pi^2}\,d_{{\rm eig},i}.                      \tag{11}
\]

If \(f_i\le F\) and \(\|B_i\|_{\mathrm{op}}\le C_U\) on \(U_i\), the triangle inequality in the \(B_i^{1/2}\)-seminorm gives

\[
\int_{U_i}\mathfrak e_i
\le C(F,C_U)\left[
 \int_M d_{{\rm eig},i}
 +\int_M|H_i-\widetilde H_i|^2
 \right]\longrightarrow0.                                    \tag{12}
\]

Thus on the regular region one may use the reduced harmonic density

\[
\mathcal D_i=
 |E_i|^2+
 \left(q_i-\frac92\right)^2+
 \left(|2\pi H_i|-\frac{q_i}{3\sqrt2}\right)^2+
 \mathfrak e_i.                                               \tag{13}
\]

It has vanishing integral over \(U_i\). This formulation avoids any need for compactness of the spinors themselves.

## 4. Joint exponential-chart averaging

Suppose \(P_i\subset U_i\) has

\[
\operatorname{Vol}(P_i)\ge v_0>0
\]

and is buffered so that \(\exp_p(B_{2r}(0_p))\subset U_i\) for every \(p\in P_i\). Choose \(r\) below the conjugate-radius scale supplied by the sectional-curvature bound.

For a density \(D_i\ge0\), define

\[
\mathcal A_i(p)=
 \int_{B_r(0_p)}
 D_i(\exp_pv)\,
 d\mu_{\exp_p^*\bar g_i}(v).
\]

Jacobi-field comparison bounds the exponential Jacobian. Invariance of Liouville measure under geodesic flow then gives

\[
\int_{P_i}\mathcal A_i(p)\,d\mu_i(p)
 \le C(r,K)\int_{U_i}D_i\,d\mu_i.                              \tag{14}
\]

This remains valid even when the exponential chart wraps over its image; injectivity of \(\exp_p\) is not needed. Applying (14) to the sum (13) produces centers \(p_i\in P_i\) with

\[
\int_{B_r(0)}
 \exp_{p_i}^*\mathcal D_i\longrightarrow0.                     \tag{15}
\]

Hence there is no incompatibility between choosing a chart with amplitude, eigenline, curvature-profile, and Einstein errors all small. Summing the densities before averaging makes the selection simultaneous.

## 5. Passage to the local Einstein metric and harmonic form

Let

\[
\widehat g_i=\exp_{p_i}^*\bar g_i,\qquad
\widehat H_i=\exp_{p_i}^*H_i.
\]

Uniform curvature-derivative estimates on the buffered region yield, after frame choices and a subsequence,

\[
\widehat g_i\longrightarrow g_\infty
\]

smoothly on a smaller Euclidean ball.

The modulus terms in (15) give a uniform local \(L^2\) bound for \(\widehat H_i\). Since

\[
d\widehat H_i=0,\qquad
d_{\widehat g_i}^*\widehat H_i=0,\qquad
*_{\widehat g_i}\widehat H_i=\widehat H_i,                     \tag{16}
\]

interior Hodge estimates provide smooth subsequential convergence

\[
\widehat H_i\longrightarrow H_\infty.
\]

The four parts of (13) then give

\[
\operatorname{Ric}_{g_\infty}=-g_\infty,\qquad s_\infty=-4,    \tag{17}
\]

\[
q_\infty=\frac92,\qquad
|W_\infty^+|=\frac1{2\sqrt6},                                  \tag{18}
\]

and

\[
|H_\infty|
 =\frac{1}{2\pi}\frac{9/2}{3\sqrt2}
 =\frac{3}{4\sqrt2\pi}>0.                                     \tag{19}
\]

Equation (19) is quantitative local amplitude. Unique continuation plays no role.

Finally,

\[
\left\langle
 \left(W_\infty^+
 +\sqrt{\frac23}|W_\infty^+|I\right)H_\infty,
 H_\infty
\right\rangle=0.
\]

The endomorphism in parentheses is positive semidefinite and \(H_\infty\neq0\), so

\[
W_\infty^+H_\infty
 =-\sqrt{\frac23}|W_\infty^+|H_\infty.
\]

Equality in the trace-free \(3\times3\) eigenvalue estimate forces

\[
\operatorname{Spec}(W_\infty^+)
 =\left(-\frac16,\frac1{12},\frac1{12}\right).                 \tag{20}
\]

Thus the densities above provide precisely the amplitude and eigenline information needed for the calibrated local Einstein model.

## 6. What the cutoff flow does not transport

The following structures are not preserved by carrying the initial objects along the cutoff flow:

* harmonicity and self-duality of \(H_a\);
* the harmonic projection \(a^+\);
* the equations for \(A,\Phi,\psi,\varphi\);
* the identity \(f\varphi=3\sqrt2(-iF_A^+)\);
* the optimal weight \(f=\sqrt q\);
* the Hodge decomposition of \(iF_A^+\).

The valid construction is instead: fix the evolved metric, select \(a_i\) for that metric, form its evolved-metric harmonic representative, and solve the rescaled monopole equations anew. The topological monopole property survives the metric deformation, which is enough for this reconstruction.

## 7. Exact estimate absent from the stated evolved-time hypotheses

The Codex decomposition assumes

\[
q=-s+\sqrt6|W^+|>0
\]

globally. This follows for the original pointwise pinched metrics, but global \(Q_i\to0\) at the evolved time gives only

\[
q_i\longrightarrow\frac92\quad\text{in }L^2.
\]

It does not ensure \(q_i>0\) everywhere. Small sets with \(q_i\le0\) are compatible with this \(L^2\) statement. Consequently, the globally admissible optimal weight \(f_i=\sqrt{q_i}\) used in (10)–(17) of the Codex report is not presently available from the supplied assumptions. The two Hölder gaps in that derivation also use the positivity of \(q_i\).

The exact missing analytic statement can be expressed as either:

\[
\exists f_i>0\text{ smooth}:\qquad
L_{f_i}-72\pi^2p_i\longrightarrow0,
\qquad
\sup_{U_i}f_i<\infty,                                         \tag{21}
\]

with the decomposition (9) yielding (5)–(7), or an extended decomposition using

\[
q_i^\sharp=\max\{q_i,0\},
\]

in which the contribution from \(\max\{-q_i,0\}\) appears as an additional term \(\ge0\). Since (2) implies

\[
\int\max\{-q_i,0\}^2\longrightarrow0,
\]

such an extension would recover the same chart densities. That extension is not established in the supplied report.

Therefore:

* once (5)–(7) are available at the evolved metric, the finite-density averaging gives one chart with quantitative amplitude, lowest-eigenline saturation, and harmonic-form compactness;
* global \(Q_i\to0\) and the scalar–Weyl completion profile alone do not yet supply (5)–(7) through the exact decomposition as currently written;
* the unresolved bridge is the admissible-weight statement (21), equivalently a version of the decomposition adapted to \(q_i^\sharp\), or a global evolved-time estimate \(q_i\ge\eta>0\).