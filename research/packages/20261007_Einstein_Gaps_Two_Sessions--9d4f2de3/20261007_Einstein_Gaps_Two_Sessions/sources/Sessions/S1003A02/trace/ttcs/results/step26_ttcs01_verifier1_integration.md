# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 26,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step26_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step26_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Read Step 25's exact CR-pinning identity, Lemma P, and conditional Theorem D as a geometric analyst. Verify constants, tensor/norm inequalities, control quantifiers, and what genuinely follows. Then analyze the proposed truncation lemma in the ACH diagonal block: identify the eigenmodes at standard CH, separate radial-translation/defining-function or other gauge directions from physical metric modes, and determine the weakest decay sufficient to splice a standard-CR finite-P or Einstein ACH metric to an exact CH collar with vanishing added P. Give either a complete proof route with explicit mode projections and estimates, or a precise mathematical obstruction/counterexample. Keep the relationship among zero infimum, attainment, and standard-CR Einstein existence exact.

## Integrated Scientific Memo

# Verification memo

## 1. CR pinning: exact identity, norms, and constants

Set
\[
D=y_g-y_h,\qquad S=y_f+y_g+y_h,\qquad e_i=\Ric_{ii}+6.
\]
Differentiating
\[
\widetilde\Phi=q+\frac14D-\zeta\sinh q
\]
with the controlled equations gives
\[
\boxed{\;
\widetilde\Phi'=F-\frac14(e_g-e_h),
\;}
\]
where
\[
\boxed{\;
F=
D\Bigl(1-\frac S4-\zeta\cosh q\Bigr)
+\zeta\sinh q\,(y_g+y_h-2)
+\frac{2\zeta^2}{\kappa^2}\sinh(2q).
\;} \tag{1}
\]
Since adding \(6g\), or subtracting the scalar trace, cancels in a component difference,
\[
e_g-e_h=\Ric^\circ_{gg}-\Ric^\circ_{hh}.
\]
Thus the control coefficient \(-1/4\) is exact and requires no scalar normalization or Einstein constraint.

A qualification is necessary: \(F\) is **not globally divisible by \(\zeta^2\)** as a smooth function of the six raw state variables. Writing \(F=\zeta^2G\) with bounded \(G\) is valid only in an ACH block imposing
\[
|(y_f,y_g,y_h,\kappa)-(2,1,1,1)|\le K\zeta
\]
and bounded \(q\). There (1) is \(O(\zeta^2)\). The supplied script verifies the control term and vanishing of \(F\) on \(E(q)\), but does not independently verify a globally regular polynomial \(G\).

For \(I=[T_0,T_1]\),
\[
P_I=2\pi^2\int_IW|\Ric^\circ|^2dt.
\]
Writing \(x=\Ric^\circ_{gg}\), \(y=\Ric^\circ_{hh}\),
\[
|\Ric^\circ|^2\ge x^2+y^2\ge\frac12(x-y)^2,
\]
hence
\[
P_I\ge \pi^2\int_IW(e_g-e_h)^2dt.
\]
Weighted Cauchy–Schwarz then gives
\[
\left|\widetilde\Phi(T_1)-\widetilde\Phi(T_0)-\int_I Fdt\right|
\le \frac14
 \left(\int_IW(e_g-e_h)^2dt\right)^{1/2}
 \left(\int_IW^{-1}dt\right)^{1/2},
\]
and therefore, since \(P=8\pi^2\widehat P\),
\[
\boxed{\;
\left|\widetilde\Phi(T_1)-\widetilde\Phi(T_0)-\int_I Fdt\right|
\le
\left(\frac{\widehat P_I}{2}\right)^{1/2}
\left(\int_I\frac{dt}{W}\right)^{1/2}.
\;} \tag{2}
\]
Lemma P and its constant are correct. It is useful only away from a bolt, where \(W>0\) and \(\int W^{-1}\) is finite.

### Corollary P1

If the transition remains in one ACH box and
\[
y_g+y_h\ge c_B>0,\qquad \kappa\ge\kappa_{\min}>0,
\]
then
\[
(\zeta^2)'=-2(y_g+y_h)\zeta^2
\]
and \(W=\kappa/\zeta^2\) imply
\[
\left|\int_T^\infty Fdt\right|
\le \frac{\sup_B|G|}{2c_B}\zeta(T)^2=:\delta(T),
\]
and
\[
\int_T^\infty\frac{dt}{W}
=\int_T^\infty\frac{\zeta^2}{\kappa}dt
\le \frac{\zeta(T)^2}{2c_B\kappa_{\min}}.
\]
Thus the intrinsic pinning estimate is
\[
\boxed{\;
\widehat P_{[T,\infty)}
\ge
4c_B\kappa_{\min}
\frac{(|\widetilde\Phi(T)|-\delta(T))_+^2}{\zeta(T)^2}.
\;} \tag{3}
\]
This avoids any cell-dependent radial-offset constant. Under the note’s stronger hypothesis
\[
W\ge \frac c{16}e^{4t},
\]
(2) gives exactly
\[
\boxed{\;
\widehat P_{[T,\infty)}
\ge\frac c2e^{4T}
\bigl(|\widetilde\Phi(T)|-\delta(T)\bigr)_+^2.
\;} \tag{4}
\]
All constants in (1.2)–(1.3) are therefore correct, provided block membership and the volume bound hold throughout the transition.

For CH,
\[
W=\sinh^3t\cosh t\sim\frac1{16}e^{4t},
\qquad \int_T^\infty W^{-1}dt\sim4e^{-4T}.
\]
The linear antisymmetric calculation gives
\[
m\sim4e^{-4t},\quad w\sim\frac18e^{-4t},\quad
M(t)\sim e^{-4t},\quad G(T)\sim2e^{-4T},
\]
so
\[
Q_{\min}\sim\frac12C^2e^{4T}.
\]
Thus the factor \(1/2\) is asymptotically sharp. The script has a harmless reporting typo: the coefficient of \(w\sim e^{-4t}/8\) is obtained from \(w e^{4t}\), not \(w e^{-4t}\).

The nonstandard Einstein filling can only be ruled out as a bounded-cost completion while the entire correcting trajectory remains in a chain of ACH boxes covering its \(q\)-range. The supplied verified ranges leave \(q\in(0.3,0.7)\) unstated; this requires an additional elementary box bound or interval verification.

---

## 2. Standard-CH eigenmodes and their meaning

At
\[
E(0)=(2,1,1,1,0,0)
\]
in coordinates \((y_f,y_g,y_h,\kappa,q,\zeta)\), a convenient eigenbasis is
\[
\begin{array}{c|c|l}
\lambda&v_\lambda&\text{meaning}\\ \hline
2&(4,-3,-3,5,0,0)&\text{outgoing/non-ACH Einstein mode},\\
0&(0,0,0,0,1,0)&\text{Rossi/CR boundary deformation},\\
-2&(0,1,1,1,0,2)&\text{CH radial phase/defining-function mode},\\
-4&(0,1,-1,0,-\tfrac12,0)&\text{physical antisymmetric mode},\\
-6&(-4,1,1,1,0,0)&\text{physical symmetric mode},\\
-8&(2,1,1,0,0,0)&\text{constraint-transverse mode}.
\end{array} \tag{5}
\]
Signs of individual eigenvectors are immaterial.

The exact CH orbit, parameterized by \(z=\zeta\), is
\[
H(z)=
\left(
\sqrt{1+z}+\frac1{\sqrt{1+z}},
\sqrt{1+z},\sqrt{1+z},
\sqrt{1+z},0,z
\right). \tag{6}
\]
Its tangent at \(z=0\) is half the \(-2\) vector. Therefore the \(e^{-2t}\) term is not a physical metric mode: it changes the radial origin, equivalently the defining function/contact-form representative. The normalization \(\Ric=-6g\) already fixes the overall metric scale.

Put
\[
x=y_f-2,\quad a=\frac{y_g+y_h}{2}-1,\quad
k=\kappa-1,\quad d=\frac{y_g-y_h}{2}.
\]
Linear modal coefficients may be taken as
\[
\begin{aligned}
A_+&=\frac{x-2a+6k-2\zeta}{40},&
A_{-2}&=\frac{\zeta}{2},\\
A_{-6}&=\frac{-x+2a+2k-2\zeta}{8},&
A_{-8}&=\frac{x+3a+k-2\zeta}{5},\\
A_{-4}&=d,&
A_0&=q+\frac d2.
\end{aligned} \tag{7}
\]
The nonlinear replacement of \(A_0\) is \(\widetilde\Phi\).

For the Hamiltonian expression
\[
\mathcal C
=y_fy_g+y_gy_h+y_hy_f-6-\frac12\sum_i\Pot_i,
\]
\[
\mathcal C_{\rm lin}=2x+6a+2k-4\zeta=10A_{-8}. \tag{8}
\]
Hence an Einstein end has no \(-8\) mode. For a scalar-\(-24\) metric,
\[
e_0:=\Ric_{tt}+6,\qquad
e_0=2\mathcal C+e_f+e_g+e_h,
\]
and \(e_0+e_f+e_g+e_h=0\), so
\[
\boxed{\mathcal C=e_0=-(e_f+e_g+e_h).} \tag{9}
\]
Thus the \(-8\) component is a forced non-Einstein response and must not be omitted from a finite-\(P\) truncation argument.

After matching the CH phase, an Einstein standard-CR end has only the physical rates \(4\) and \(6\) (with faster nonlinear/resonant terms). A finite-\(P\), scalar-normalized end additionally has forced unstable and \(-8\) responses, but these can still be \(o(e^{-2t})\).

---

## 3. Correct truncation theorem

The truncation lemma as stated in Step 25 is missing control of the scalar channel. Finite \(P\) controls only \(\Ric^\circ\), while the state equations use \(e_i=\Ric_{ii}+6\). A valid statement is:

> **Truncation theorem.** Let \(g\) be a complete diagonal metric whose tail stays in a fixed sufficiently small standard ACH block, with \(\widetilde\Phi(t)\to0\), and suppose either  
> (i) \(s_g=-24\) and \(P(g)<\infty\), or  
> (ii) \(J_6(g)=\int|\Ric+6g|^2<\infty\).  
> Then there exist diagonal \(g_R\), equal to \(g\) on \(t\le R\) and exactly CH on \(t\ge R+1\), such that
> \[
> P(g_R)\to P(g).
> \]
> In case (ii), also \(J_6(g_R)\to J_6(g)\).

### Gauge-free variables

Subtract CH at the same \(\zeta\):
\[
\begin{aligned}
\bar x&=y_f-\left(\sqrt{1+\zeta}+\frac1{\sqrt{1+\zeta}}\right),\\
\bar a&=\frac{y_g+y_h}{2}-\sqrt{1+\zeta},\\
\bar k&=\kappa-\sqrt{1+\zeta},\qquad
d=\frac{y_g-y_h}{2}.
\end{aligned}
\]
Use
\[
U=\frac{\bar x-2\bar a+6\bar k}{40},\quad
V_6=\frac{-\bar x+2\bar a+2\bar k}{8},\quad
V_8=\frac{\bar x+3\bar a+\bar k}{5},
\quad d,\quad\widetilde\Phi. \tag{10}
\]
The \(-2\) phase mode has disappeared. In these variables the controlled system has linear rates
\[
2,\,-6,\,-8,\,-4,\,0
\]
and schematic normal form
\[
\begin{aligned}
U'&=2U+N_U+B_Ue,\\
V_6'&=-6V_6+N_6+B_6e,\\
V_8'&=-8V_8+N_8+B_8e,\\
d'&=-4d+N_4-\tfrac12(e_g-e_h),\\
\widetilde\Phi'&=N_0-\tfrac14(e_g-e_h),
\end{aligned} \tag{11}
\]
where
\[
|N_i|\le C(\zeta+|Y|)|Y|
\]
in a small block and \(N_i=0\) on the CH curve. The center family \(E(q)\) consists of equilibria, so there is no isolated center drift such as \(c\widetilde\Phi^2\).

Under \(s=-24\),
\[
\widehat P_{\rm tail}
=\frac14\int W\sum_{\alpha=0,f,g,h}e_\alpha^2dt,
\qquad W\asymp e^{4t}.
\]
Therefore
\[
e^{2t}e_\alpha(t)\in L^2. \tag{12}
\]
Stable Duhamel estimates, the terminal representation of the bounded unstable mode, and Lemma P for the neutral component then give
\[
\boxed{\;
|U|+|V_6|+|V_8|+|d|+|\widetilde\Phi|
=o(e^{-2t})=o(\zeta).
\;} \tag{13}
\]
Because
\[
\partial_q\widetilde\Phi=1-\zeta\cosh q
\]
is bounded away from zero in the standard block, \(q=o(e^{-2t})\) as well.

For an exact Einstein end, \(e_\alpha=0\), \(V_8=0\), and the stable-manifold expansion improves this to
\[
X-H(\zeta)=O(e^{-4t})
\]
after phase matching.

### Splice and weakest decay

At radius \(R\), choose the CH comparison phase by
\[
\zeta_{\rm CH}(\rho_R)=\zeta(R),
\qquad
\rho_R=\operatorname{arsinh}\bigl(\zeta(R)^{-1/2}\bigr).
\]
Let
\[
D_i=\log a_i-\log a_i^{\rm CH}
\]
for this phase. Then (13), propagated over a unit interval, gives
\[
\sup_{[R,R+1]}(|D|+|D'|)=o(e^{-2R}). \tag{14}
\]
Choose \(\chi=1\) near \(R\), \(\chi=0\) near \(R+1\), and define
\[
\log a_i^R=\log a_i^{\rm CH}+\chi D_i.
\]
Since the diagonal Ricci formulas are affine in \(y_i'=(\log a_i)''\), the original second derivatives occur multiplied by \(\chi\); the genuinely added cutoff terms involve only \(D,D'\). Consequently
\[
\int_{R}^{R+1}|\Ric_{g_R}+6g_R|^2dV_{g_R}
\le
C\int_R^{R+1}W\sum_\alpha e_\alpha^2dt
+
C\,W(R)\sup_{[R,R+1]}(|D|+|D'|)^2,
\]
and both terms tend to zero. The discarded original tail also has vanishing \(P\)-mass. Hence \(P(g_R)\to P(g)\).

The weakest useful fixed-width splice condition is therefore
\[
\boxed{\;
\sup_{[R_k,R_k+1]}(|D|+|D'|)
=o(\zeta(R_k))=o(e^{-2R_k})
\quad\text{for some }R_k\to\infty,
\;} \tag{15}
\]
plus vanishing weighted residual on the discarded tail. Full \(C^2\) decay is unnecessary in this ODE setting. A physical \(Ce^{-2t}\) mismatch would contribute order \(C^2\), while the \(e^{-2t}\) CH phase mode is harmless because it is removed exactly.

There is no linear boundary term: this is a direct squared-residual estimate, not an integration-by-parts or Chern–Weil comparison. Thus the relevant threshold is \(>2\), unlike the \(>4\) decay needed in Step 22 to eliminate linear transgression terms.

The genuine obstruction is the neutral CR mode. A nonzero Rossi limit gives
\[
\widehat P_{\rm completion}\gtrsim
\frac{|\widetilde\Phi_\infty|^2}{\zeta(R)^2},
\]
so the cost diverges. The nonstandard Einstein filling is precisely such an obstruction: finite curvature defect, even zero defect, does not imply cheap exact-CH truncation unless the CR infinity is standard.

---

## 4. Exact consequences for Theorem D

The compactness statement must include:

1. scalar normalization \(s=-24\), or uniformly finite \(J_6\);
2. one ACH block with uniform \(T_0,K,\zeta_0,q_0\);
3. sufficient two-sided compact-state/curvature control to obtain a smooth local limit, including control at the bolt.

Uniform bolt bounds and orbit noncollapse alone do not automatically provide all required upper curvature and \(H^2_{\rm loc}\) estimates.

Under these inputs, Lemma P implies that the local limit has
\[
\widetilde\Phi_\infty(t)\to0.
\]
Lower semicontinuity gives
\[
P(g_\infty)\le p^{\rm diag}_{1,0}.
\]
Truncation supplies exact-CH metrics approaching \(g_\infty\), so by the definition of the exact-ended infimum,
\[
P(g_\infty)\ge p^{\rm diag}_{1,0}.
\]
Hence
\[
\boxed{P(g_\infty)=p^{\rm diag}_{1,0}.}
\]
This is attainment in the **extended complete standard-CR ACH class**, not necessarily in the original exact-CH-ended class.

The logically exact zero statements are:
\[
\boxed{
\text{standard-CR complete diagonal Einstein ACH filling}
\Longrightarrow p^{\rm diag}_{1,0}=0
}
\]
by Einstein truncation, and
\[
\boxed{
p^{\rm diag}_{1,0}=0
+\text{compactness/attainment in the extended class}
\Longrightarrow
\Ric(g_\infty)=-6g_\infty.
}
\]
Zero infimum alone does **not** imply an Einstein filling: collapse, concentration, or failure of compactness may prevent attainment.

Conversely, the standard-CR Einstein filling need not itself possess an exact CH collar; it merely yields exact-collar approximants of cost tending to zero. For \(O(-1)\), Lemma R excludes a zero-cost Einstein metric with an exact CH collar, so if \(p=0\), the exact-ended infimum is not attained.

For \(p>0\), the extended-class minimizer is non-Einstein. Compactly supported diagonal variations show diagonal \(P\)-criticality once regularity is established. A claim of full unrestricted criticality requires a careful symmetry argument and treatment of gauge/lapse variations; it is not needed for Theorem D.

Finally, the proposed large-volume shadowing exclusion remains conditional. The numerically observed face trajectories are not a proof of the global phase portrait. Moreover, the collapsing \(\kappa\uparrow\) branch can drive \(W\) down and merge into an interior-neck/collapse alternative, where weighted control ceases to be expensive. Thus “large-volume excursion excluded” is justified only while the orbit remains in a uniformly large-\(W\) region and after a validated face-dynamics or Lyapunov argument.