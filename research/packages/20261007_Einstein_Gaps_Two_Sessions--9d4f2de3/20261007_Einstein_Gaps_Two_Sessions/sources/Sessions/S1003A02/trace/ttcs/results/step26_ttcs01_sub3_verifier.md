# TTCS Independent Branch Record

```json
{
  "step_id": 26,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step25_diagonal_cell_compactness_and_CR_pinning.md",
    "Sessions/S1003A02/workspace/scripts/cr_pinning_check.py",
    "Sessions/S1003A02/workspace/scripts/squash_escape_cost.py",
    "Sessions/S1003A02/workspace/scripts/ach_projected.py",
    "Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md",
    "Sessions/S1003A02/workspace/notes/step20_burns_response_and_neck_quantization.md"
  ]
}
```

## Task

Read Step 25's exact CR-pinning identity, Lemma P, and conditional Theorem D as a geometric analyst. Verify constants, tensor/norm inequalities, control quantifiers, and what genuinely follows. Then analyze the proposed truncation lemma in the ACH diagonal block: identify the eigenmodes at standard CH, separate radial-translation/defining-function or other gauge directions from physical metric modes, and determine the weakest decay sufficient to splice a standard-CR finite-P or Einstein ACH metric to an exact CH collar with vanishing added P. Give either a complete proof route with explicit mode projections and estimates, or a precise mathematical obstruction/counterexample. Keep the relationship among zero infimum, attainment, and standard-CR Einstein existence exact.

## Output

# Scientific verification memo

## 1. Exact CR-pinning identity and constants

Write
\[
D=y_g-y_h,\qquad S=y_f+y_g+y_h,\qquad
e_i=\operatorname{Ric}_{ii}+6 .
\]
Using the displayed potentials in `ach_projected.py`, direct differentiation of
\[
\widetilde\Phi=q+\frac14D-\zeta\sinh q
\]
gives
\[
\widetilde\Phi'
=
F(y,\kappa,q,\zeta)-\frac14(e_g-e_h),                                    \tag{1}
\]
where the uncontrolled drift in the raw six variables is
\[
\boxed{
F=
D\Bigl(1-\frac S4-\zeta\cosh q\Bigr)
+\zeta\sinh q\,(y_g+y_h-2)
+\frac{2\zeta^2}{\kappa^2}\sinh(2q).
}                                                                       \tag{2}
\]
Thus the control coefficient \(-1/4\) is exact, and
\[
e_g-e_h=\operatorname{Ric}^{\circ}_{gg}-\operatorname{Ric}^{\circ}_{hh}
\]
without any scalar-curvature assumption.

There is one presentational issue in (1.1): in the raw compact variables, \(F\) is not algebraically divisible by \(\zeta^2\). One may write \(F=\zeta^2G\) either by defining \(G=F/\zeta^2\) for \(\zeta>0\), or in the blown-up ACH block coordinates where every deviation from \(E(q)\) is \(O(\zeta)\). Formula (2) shows why \(G\) is bounded on such blocks: \(F\) has no linear term at \(E(q)\), hence \(F=O(\zeta^2)\) when the block imposes \(X-E(q)=O(\zeta)\). The script `cr_pinning_check.py` verifies the control term and that the free part vanishes at \(E(q)\), but it does not compare `dPhi_free` with a separately entered regular polynomial \(G\). The interval bounds on \(G\) therefore belong to the ACH block computation, not to that script alone.

### Norm and volume factors

For \(I=[T_0,T_1]\), since \(dV=2\pi^2W\,dt\),
\[
P_I=2\pi^2\int_I W|\operatorname{Ric}^{\circ}|^2\,dt.
\]
Putting \(x=\operatorname{Ric}^{\circ}_{gg}\), \(y=\operatorname{Ric}^{\circ}_{hh}\),
\[
|\operatorname{Ric}^{\circ}|^2\ge x^2+y^2
\ge\frac12(x-y)^2.
\]
Consequently,
\[
P_I\ge\pi^2\int_IW(e_g-e_h)^2\,dt.
\]
Integrating (1) and applying weighted Cauchy–Schwarz gives
\[
\begin{aligned}
\left|\widetilde\Phi(T_1)-\widetilde\Phi(T_0)-\int_I F\,dt\right|
&\le \frac14
 \left(\int_IW(e_g-e_h)^2dt\right)^{1/2}
 \left(\int_I\frac{dt}{W}\right)^{1/2}\\
&\le
\left(\frac{\widehat P_I}{2}\right)^{1/2}
\left(\int_I\frac{dt}{W}\right)^{1/2},
\end{aligned}
\]
because \(P=8\pi^2\widehat P\). Thus the constant in Lemma P is correct.

The lemma applies on intervals on which \(W>0\). At a bolt, \(\int dt/W\) usually diverges, making the estimate vacuous there but not incorrect.

### Corollary P1

If the metric is exactly CH after \(T_1\), then \(\widetilde\Phi(T_1)=0\), and \(F=0\) on the exact CH segment. If throughout the transition
\[
y_g+y_h\ge c_B>0,
\]
then
\[
(\zeta^2)'=-2(y_g+y_h)\zeta^2\le-2c_B\zeta^2,
\]
so
\[
\left|\int_T^\infty \zeta^2G\,dt\right|
\le \frac{\sup_B|G|}{2c_B}\,\zeta(T)^2=\delta(T).
\]
If also \(W\ge c e^{4t}/16\), then
\[
\int_T^\infty\frac{dt}{W}
\le \frac{4}{c}e^{-4T}.
\]
Lemma P therefore yields
\[
\boxed{
\widehat P_{[T,\infty)}
\ge \frac c2 e^{4T}
       \bigl(|\widetilde\Phi(T)|-\delta(T)\bigr)_+^2 .
}                                                                       \tag{3}
\]
All constants in (1.2)–(1.3) are correct. The block and volume hypotheses must hold at every point of the transition interval, not merely at its two ends.

### Sharpness calculation

For exact CH,
\[
W_{\rm CH}=\sinh^3t\cosh t\sim\frac1{16}e^{4t},
\qquad
\int_T^\infty W_{\rm CH}^{-1}dt\sim4e^{-4T}.
\]
In `squash_escape_cost.py`,
\[
m\sim4e^{-4t},\qquad
w\sim\frac18e^{-4t},\qquad
M(t)=\int_t^\infty m\sim e^{-4t},
\]
and hence
\[
G(T)=\int_T^\infty\frac{M(t)^2}{w(t)}dt
\sim2e^{-4T}.
\]
Therefore
\[
Q_{\min}(T)\sim\frac12 C^2e^{4T},
\]
matching (3) with \(c=1\). In this antisymmetric sector the invariant components of the trace-free Ricci tensor vanish and the \(g,h\) components are opposite, so both tensor inequalities used in Lemma P are asymptotically saturated.

There is a minor reporting error in the script: to extract the coefficient of \(w\sim e^{-4t}/8\), the symbolic limit should be `limit(w*exp(4*t),t,oo)`, whereas the code uses `w*exp(-4*t)`. The hand asymptotic and numerical values of \(G(T)\) are unaffected.

---

## 2. Linear modes at standard CH

At
\[
E(0)=(2,1,1,1,0,0)
\]
the Jacobian in the order
\[
(y_f,y_g,y_h,\kappa,q,\zeta)
\]
has the following eigenvectors:

\[
\begin{array}{c|c|l}
\lambda & \text{eigenvector} & \text{geometric meaning}\\ \hline
2 &(4,-3,-3,5,0,0)& \text{outgoing Einstein mode}\\
0 &(0,0,0,0,1,0)& \text{CR/Rossi parameter}\\
-2 &(0,1,1,1,0,2)& \text{translation of the CH radial phase}\\
-4 &(0,1,-1,0,-\tfrac12,0)& \text{antisymmetric physical mode}\\
-6 &(-4,1,1,1,0,0)& \text{symmetric physical mode}\\
-8 &(2,1,1,0,0,0)& \text{Einstein-constraint transverse mode}.
\end{array}                                                            \tag{4}
\]

The rate-\(2\) decaying mode is not a second physical CH scale. The normalization \(\operatorname{Ric}=-6g\) fixes the metric scale. This mode changes the origin of the CH radial coordinate, equivalently the defining function or contact-form representative at conformal infinity.

To see this exactly, parameterize the CH trajectory by \(z=\zeta\):
\[
H(z)=
\left(
\sqrt{1+z}+\frac1{\sqrt{1+z}},
\sqrt{1+z},\sqrt{1+z},
\sqrt{1+z},0,z
\right).                                                               \tag{5}
\]
Indeed, if \(z=\operatorname{csch}^2r\), then
\[
\kappa=\coth r=\sqrt{1+z},\qquad
y_g=y_h=\coth r,\qquad
y_f=\coth r+\tanh r.
\]
The tangent \(H'(0)\) is one half of the \(-2\) vector in (4).

### Explicit linear projections

Put
\[
x=y_f-2,\qquad
a=\frac{y_g+y_h}{2}-1,\qquad
k=\kappa-1,\qquad
d=\frac{y_g-y_h}{2}.
\]
The symmetric modal coefficients are
\[
\begin{aligned}
A_+&=\frac{x-2a+6k-2\zeta}{40},\\
A_{-2}&=\frac{\zeta}{2},\\
A_{-6}&=\frac{-x+2a+2k-2\zeta}{8},\\
A_{-8}&=\frac{x+3a+k-2\zeta}{5}.
\end{aligned}                                                          \tag{6}
\]
In the antisymmetric sector,
\[
A_{-4}=d,\qquad
A_0^{\rm lin}=q+\frac d2.
\]
The nonlinear neutral coordinate is precisely
\[
\widetilde\Phi=q+\frac d2-\zeta\sinh q.
\]

The Einstein Hamiltonian expression is
\[
\mathcal C
=y_fy_g+y_gy_h+y_hy_f-6-\frac12\sum_i\operatorname{Pot}_i .
\]
Its linearization is
\[
\mathcal C_{\rm lin}=2x+6a+2k-4\zeta=10A_{-8}.                          \tag{7}
\]
Hence an Einstein trajectory has no \(-8\) component. For a scalar-\(-24\) non-Einstein metric, define also
\[
e_0=\operatorname{Ric}_{tt}+6.
\]
The controlled equations give
\[
e_0=2\mathcal C+e_f+e_g+e_h.
\]
Since scalar \(-24\) means \(e_0+e_f+e_g+e_h=0\),
\[
\boxed{\mathcal C=e_0=-(e_f+e_g+e_h).}                                 \tag{8}
\]
Thus the \(-8\) direction can occur in a finite-\(P\) sequence as a forced response, although it is absent from the exact Einstein stable manifold. The Step 25 phrase “stable modes of rates \(4,6\)” is exact for Einstein metrics after radial-phase matching; finite-\(P\), scalar-normalized metrics also carry the controlled \(-8\) response.

---

## 3. A rigorous truncation statement

The form needed for Theorem D is the following.

### Truncation theorem

Let
\[
g=dt^2+\sum_i a_i(t)^2\sigma_i^2
\]
be a smooth diagonal metric for \(t\ge T_0\), satisfying:

1. \(s_g=-24\);
2. its state remains in a sufficiently small standard ACH block and converges to \(E(0)\);
3. \(\widetilde\Phi(t)\to0\);
4. \(P(g)<\infty\).

Then there are diagonal metrics \(g_R\), equal to \(g\) on \(t\le R\) and equal to a normalized CH metric on \(t\ge R+1\), such that
\[
P(g_R)\longrightarrow P(g).
\]
In fact the transition can be arranged so that
\[
\int_{[R,R+1]\times S^3}
|\operatorname{Ric}_{g_R}+6g_R|^2\,dV_{g_R}\longrightarrow0,             \tag{9}
\]
which also gives the required \(J_6\) approximation.

### Modal estimate underlying the theorem

Subtract the exact CH trajectory with the same value of \(\zeta\). Set
\[
\begin{aligned}
\bar x&=y_f-\left(\sqrt{1+\zeta}+\frac1{\sqrt{1+\zeta}}\right),\\
\bar a&=\frac{y_g+y_h}{2}-\sqrt{1+\zeta},\\
\bar k&=\kappa-\sqrt{1+\zeta},\\
d&=\frac{y_g-y_h}{2}.
\end{aligned}
\]
Use the transverse coordinates
\[
U=\frac{\bar x-2\bar a+6\bar k}{40},\quad
V_6=\frac{-\bar x+2\bar a+2\bar k}{8},\quad
V_8=\frac{\bar x+3\bar a+\bar k}{5},\quad
d,\quad\widetilde\Phi.                                                   \tag{10}
\]
The controlled system has the asymptotic normal form
\[
\begin{aligned}
U'&=2U+N_U-\frac{e_f-e_g-e_h}{40},\\
V_6'&=-6V_6+N_6+\frac{e_f-e_g-e_h}{8},\\
V_8'&=-8V_8+N_8-\frac{e_f+\frac32(e_g+e_h)}5,\\
d'&=-4d+N_4-\frac12(e_g-e_h),\\
\widetilde\Phi'&=N_0-\frac14(e_g-e_h).
\end{aligned}                                                          \tag{11}
\]
Here the \(N_i\) are smooth, vanish on the CH curve, and satisfy in a small block
\[
|N_i|\le C(\zeta+|V_s|)|V|,
\]
where \(V_s=(U,V_6,V_8,d)\); importantly, the center line \(E(q)\) consists entirely of equilibria, so there is no isolated \(\widetilde\Phi^2\) term driving slow center motion.

Because \(s=-24\),
\[
\widehat P_{\rm tail}
=\frac14\int W\sum_{\alpha=0,f,g,h}e_\alpha^2\,dt,
\]
and the ACH block gives \(W\asymp e^{4t}\). Therefore
\[
F_\alpha(t):=e^{2t}e_\alpha(t)\in L^2([T_0,\infty)).                    \tag{12}
\]

For a stable scalar equation \(v'=-\mu v+e^{-2t}F\), \(\mu>2\),
\[
e^{2t}v(t)
=e^{-(\mu-2)(t-T)}e^{2T}v(T)
+\int_T^t e^{-(\mu-2)(t-s)}F(s)\,ds,
\]
and the right side tends to zero because \(F\in L^2\). For the outgoing mode,
\[
U(t)=-\int_t^\infty e^{2(t-s)}
       \bigl(N_U(s)+e^{-2s}F_U(s)\bigr)\,ds,
\]
so \(e^{2t}U(t)\to0\). For the neutral coordinate, the standard-CR condition gives
\[
\widetilde\Phi(t)
=-\int_t^\infty\left(N_0(s)-\frac14(e_g-e_h)(s)\right)ds,
\]
and
\[
e^{2t}\left|\int_t^\infty e^{-2s}F(s)\,ds\right|
\le \frac12\|F\|_{L^2(t,\infty)}\longrightarrow0.
\]
The nonlinear terms are absorbed on a sufficiently far tail using their structural vanishing on the CH and center curves. This yields
\[
\boxed{
|U|+|V_6|+|V_8|+|d|+|\widetilde\Phi|
=o(e^{-2t}).
}                                                                       \tag{13}
\]
Since
\[
\partial_q\bigl(q+d/2-\zeta\sinh q\bigr)=1-\zeta\cosh q
\]
stays away from zero in the standard block, (13) also gives \(q=o(e^{-2t})\).

For an Einstein metric all \(e_\alpha\) vanish and \(\mathcal C=0\). The standard stable-manifold expansion then gives, after matching radial phase,
\[
X(t)-H(\zeta(t))=O(e^{-4t}),                                             \tag{14}
\]
with the leading physical modes given by the \(-4\) and \(-6\) vectors in (4). Products with the radial mode may introduce terms such as \(t e^{-6t}\), which remain far below the threshold needed below.

### Splicing construction

Let
\[
\rho_R=\operatorname{arsinh}\bigl(\zeta(R)^{-1/2}\bigr)
\]
and choose the CH comparison metric with radial phase
\[
\rho^0_R(t)=\rho_R+t-R.
\]
If \(L_i=\log a_i\) and \(L_i^0\) are the CH logarithmic profiles with this phase, then at \(t=R\)
\[
\begin{aligned}
L_g-L_g^0&=\frac q2,\\
L_h-L_h^0&=-\frac q2,\\
L_f-L_f^0&=\log\frac{\kappa}{\sqrt{1+\zeta}}.
\end{aligned}
\]
Moreover, if
\[
\rho(t)=\operatorname{arsinh}(\zeta(t)^{-1/2}),
\]
then
\[
\rho'(t)
=\frac{(y_g+y_h)/2}{\sqrt{1+\zeta}}
=1+\frac{\bar a}{\sqrt{1+\zeta}}.                                      \tag{15}
\]
Equations (13) and (15) imply, uniformly on fixed-length intervals,
\[
\sup_{t\in[R,R+1]}
e^{2R}\bigl(|L-L^0|+|(L-L^0)'|\bigr)\longrightarrow0.                   \tag{16}
\]

Choose a smooth cutoff \(\chi\), equal to one near \(R\) and zero near \(R+1\), and set
\[
\widetilde L_i=L_i^0+\chi(L_i-L_i^0).
\]
The curvature expressions are uniformly smooth functions of
\[
L_i',\quad L_i'',\quad e^{L_i-L_j-L_k}
\]
in the compact ACH block. The orbit equations give
\[
\int_R^{R+1}W|(L-L^0)''|^2dt
\le
C\int_R^{R+1}W\sum_i e_i^2dt+o(1).
\]
Consequently,
\[
\int_R^{R+1}
|\operatorname{Ric}_{\widetilde g}+6\widetilde g|^2dV_{\widetilde g}
\le
C\left[
\int_R^{R+1}W\sum_i e_i^2dt
+
e^{4R}\sup_{[R,R+1]}
\bigl(|L-L^0|^2+|(L-L^0)'|^2\bigr)
\right]\to0.
\]
This proves (9). Since the discarded original tail has \(P\)-mass tending to zero,
\[
P(g_R)=P(g; t\le R)+o(1)\to P(g).
\]

### Exact decay threshold

A convenient sufficient assumption is
\[
|\nabla^j(g-g_{\rm CH,phase})|=o(e^{-2t}),
\qquad j=0,1,2,
\]
in a CH orthonormal frame. A rate \(e^{-(2+\varepsilon)t}\) is more than is needed.

The sharp modal requirement is weaker:
\[
e^{2R}\inf_{\text{CH radial phase}}
\left(
|L(R)-L^0(R)|+|L'(R)-(L^0)'(R)|
\right)\longrightarrow0,                                                \tag{17}
\]
together with vanishing weighted Einstein residual on the tail. A physical transverse term \(Ce^{-2t}\) would contribute order \(C^2\) to any fixed-width splice; in the CR-neutral sector this is exactly quantified by (3). The \(e^{-2t}\) radial-translation term is exempt because it is tangent to the exact CH family and is removed by phase matching.

The scalar normalization matters in this proof. Finite \(P\) alone controls \(\operatorname{Ric}^{\circ}\), whereas the state equations use \(e_i=\operatorname{Ric}_{ii}+6\). Thus the truncation lemma as written needs either \(s=-24\), finite \(J_6=\int|\operatorname{Ric}+6g|^2\), or a separate weighted estimate for the scalar channel. In the intended scalar-normalized formulation of Theorem D, this issue is resolved.

---

## 4. What follows for Theorem D

Suppose \(g_j\) has uniformly bounded total cost, every tail from a common \(T_0\) stays in the verified standard ACH block, and the sequence converges locally to a complete smooth diagonal metric \(g_\infty\).

For each \(j\), apply Lemma P from \(T\) to its exact CH portion. Uniform block estimates give
\[
|\widetilde\Phi_j(T)|
\le C_1e^{-4T}+C_2e^{-2T}.
\]
Passing first \(j\to\infty\) and then \(T\to\infty\) gives
\[
\widetilde\Phi_\infty(T)\to0.
\]
Thus the limiting end has standard CR structure.

Lower semicontinuity gives
\[
P(g_\infty)\le \liminf_jP(g_j)=p^{\rm diag}_{1,0}.
\]
The truncation theorem supplies exact-CH-ended metrics \(g_{\infty,R}\) with
\[
P(g_{\infty,R})\to P(g_\infty),
\]
so the definition of the infimum gives the reverse inequality. Hence
\[
\boxed{P(g_\infty)=p^{\rm diag}_{1,0}.}
\]

If \(p^{\rm diag}_{1,0}>0\), the minimizer is not Einstein. For every compactly supported diagonal variation of \(g_\infty\), the unchanged tail can be truncated by the same construction; therefore the varied metric cannot have smaller \(P\). Once smooth variational regularity is available, \(g_\infty\) is \(P\)-critical in the diagonal class.

The exact zero relation is:

\[
\boxed{
\begin{array}{c}
\text{complete diagonal Einstein ACH metric on }O(-1)\\
\text{with standard CR infinity}
\end{array}
\Longrightarrow
p^{\rm diag}_{1,0}=0
}
\]
by truncation, while
\[
\boxed{
p^{\rm diag}_{1,0}=0
\ \text{and attainment in the complete scalar-\(-24\) class}
\Longrightarrow
\operatorname{Ric}(g_\infty)=-6g_\infty
}
\]
because \(P(g_\infty)=0\). Pinning supplies its standard CR infinity.

Thus a zero infimum by itself does not produce an Einstein filling when the sequence collapses, develops a non-Euclidean neck, or escapes through an unproved compactness mechanism. Conversely, a standard-CR Einstein filling produces arbitrarily small exact-collar cost but need not itself have an exact CH collar.

Finally, uniform bolt bounds and lower orbit-radius bounds are not, by themselves, an explicit local precompactness proof. The attainment argument also uses upper state estimates, control of curvature concentration on compact intervals, and regularity of the resulting minimizer. If those are included in “avoids alternatives 2–4,” the logical chain above is complete; otherwise they remain additional analytic input distinct from the truncation argument.