# Step 7 — Verification of the perpendicular relative calibration and the exact CH endpoint map

Session S1003A01, Step 7, Agent4, Execute. This note checks the most load-bearing formulas from Step 6, replaces the apparent sign-changing CH obstruction by an exact endpoint operator, verifies the smooth geometric status of the numerical cells, and records the scope correction forced by the peer's positive-curvature bulk test.

## 1. Exact Cartan derivation of the spin formulation

Use
\[
g=dt^2+a^2\sigma_1^2+b^2\sigma_2^2+c^2\sigma_3^2,
\qquad d\sigma_i=2\sigma_j\wedge\sigma_k,
\qquad \int_{S^3}\sigma_1\sigma_2\sigma_3=2\pi^2.
\]
Put \(a_1=a,a_2=b,a_3=c\), cyclically define
\[
u_i=\dot a_i-\frac{a_j^2+a_k^2-a_i^2}{a_ja_k},
\quad H_i=u_i+\frac12u_ju_k,
\quad \lambda_i=\frac{a_ja_k}{a_i},
\]
and
\[
r_i=\frac{\dot u_i}{a_i},\qquad
v_i=\frac{2H_i}{a_ja_k},\qquad
C(u)=u_1^2+u_2^2+u_3^2+u_1u_2u_3.
\]

`scripts/perp_cartan_verify.py` derives the Levi--Civita connection and curvature directly from Cartan's equations, with independent first and second radial jets. SymPy reduces the following identities exactly to zero:
\[
|\operatorname{Ric}^{\circ}|^2=\sum_i(r_i-v_i)^2,
\qquad
s=-2\sum_i(r_i+v_i),                                      \tag{1.1}
\]
\[
\dot C=2\sum_iH_i\dot u_i=abc\sum_i r_iv_i,                \tag{1.2}
\]
\[
\frac{abc}{4}|\operatorname{Ric}^{\circ}|^2
=\sum_i\frac{\lambda_i}{4}
 \left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2.           \tag{1.3}
\]
Since the orbit volume is \(2\pi^2abc\,dt\),
\[
\frac{P}{8\pi^2}=\int\sum_i\frac{\lambda_i}{4}
 \left(\dot u_i-\frac{2H_i}{\lambda_i}\right)^2dt.         \tag{1.4}
\]
Thus the normalization and curvature-to-\(u\) formulas no longer depend only on agreement with a numerical coordinate-curvature implementation.

For
\[
\Phi=C-u_2^2=u_1^2+u_3^2+u_1u_2u_3,
\]
the purely algebraic checker `scripts/perp_relative_checks.py` verifies
\[
\boxed{\begin{aligned}
\frac{P}{8\pi^2}-1=\int\Big[&
\frac{\lambda_1}{4}\left(\dot u_1+\frac{2H_1}{\lambda_1}\right)^2
+\frac{\lambda_3}{4}\left(\dot u_3+\frac{2H_3}{\lambda_3}\right)^2\\
&+\frac{\lambda_2}{4}\left(\dot u_2-\frac{2u_2-u_1u_3}{\lambda_2}\right)^2
+\frac{2u_1u_2u_3}{\lambda_2}\Big]dt .
\end{aligned}}                                                \tag{1.5}
\]
The cubic has the **plus** sign shown here. It is a signed contribution. Replacing it by its negative part gives only a stronger sufficient inequality and loses favorable regions.

In the fixed perpendicular slot,
\[
(a,b,c)=(\sqrt x,\sqrt{xe^w},\sqrt F),
\]
and the endpoint states are
\[
u_{\rm bolt}=(0,0,-1),\qquad u_{\rm CH}=(0,3x,0).          \tag{1.6}
\]
Hence \(\Phi\) drops from 1 to 0 even though the total charge \(C\) grows to \(9x^2\) on CH.

## 2. Exact-CH quadratic forms and positive zero modes

On CH,
\[
a=c=\sqrt x,\quad b=\sqrt{x(1+x)},\quad
\lambda_1=\lambda_3=\sqrt{x(1+x)},\quad
\lambda_2=\sqrt{\frac{x}{1+x}},\quad dt=\frac{dx}{2\sqrt{x(1+x)}}.
\]
For transverse perturbations \(\xi=\delta u_1\), \(\zeta=\delta u_3\), let \(v_\pm=\xi\pm\zeta\). The quadratic CH part of (1.5), after one integration by parts, is
\[
\mathcal A_{CH}^{(2)}=Q_+[v_+]+Q_-[v_-]
 +[\beta_+v_+^2+\beta_-v_-^2]_{\rho}^{1},                    \tag{2.1}
\]
where
\[
p=\frac{x(1+x)}4,\qquad \beta_\pm=\frac{2\pm3x}{8},
\]
\[
Q_\pm[v]=\int_\rho^1\{p(v')^2+V_\pm v^2\}\,dx,             \tag{2.2}
\]
\[
V_+=\frac{4+18x+15x^2}{16x(1+x)},\qquad
V_-=\frac{4-18x+3x^2}{16x(1+x)}.                              \tag{2.3}
\]
The signed cubic in (1.5) contributes
\[
3\xi\zeta\,dx=\frac34(v_+^2-v_-^2)\,dx,                     \tag{2.4}
\]
so it is already fully included in (2.1)--(2.3).

`scripts/perp_ground_state_check.py` verifies the exact positive zero modes
\[
f_+(x)=x\sqrt{1+x},\qquad
f_-(x)=\frac{x}{(1+x)^{5/2}},                                 \tag{2.5}
\]
\[
-(pf_\pm')'+V_\pm f_\pm=0,\qquad
p\frac{f_\pm'}{f_\pm}=\beta_\pm.                             \tag{2.6}
\]
The rational Riccati forms of both identities were separately checked in Lean; see `proofs/PerpGroundState.lean` and dependency certificate `proofs/perp-ground-state-check.json`. The named minus theorem depends only on `propext`, `Classical.choice`, and `Quot.sound` in the configured Mathlib project.

For every smooth \(v\),
\[
\boxed{Q_\pm[v]=\int_\rho^1pf_\pm^2
 \left((v/f_\pm)'\right)^2dx+[\beta_\pm v^2]_\rho^1.}        \tag{2.7}
\]
Therefore the sign-changing \(V_-\) does not create a negative compactly supported bulk mode on exact CH. With \(v(1)=0\), however, the lower boundary flux remains.

## 3. Sharp CH Dirichlet-to-Neumann map

Let
\[
R_\pm(\rho)=\int_\rho^1\frac{dx}{p f_\pm^2}.
\]
For fixed \(v(\rho)=V\), \(v(1)=0\), weighted Cauchy--Schwarz in (2.7) is sharp and gives
\[
Q_\pm[v]\ge \kappa_\pm(\rho)V^2,
\qquad
\kappa_\pm=\frac1{f_\pm(\rho)^2R_\pm(\rho)}-\beta_\pm(\rho).\tag{3.1}
\]
The extremizer is
\[
v_{\pm,*}(x)=V\frac{f_\pm(x)}{f_\pm(\rho)}
 \frac{R_\pm(x)}{R_\pm(\rho)},\qquad
R_\pm(x)=\int_x^1\frac{ds}{pf_\pm^2}.                        \tag{3.2}
\]
Define
\[
\Delta_-(\rho)=1+8\rho-12\rho^2\log\rho-8\rho^3-\rho^4,
\]
\[
\Delta_+(\rho)=1-3\rho-2\rho^2+4\rho^3
 +6\rho^2(1+\rho)\log\frac{1+\rho}{2\rho}.
\]
Direct integration gives
\[
\kappa_- =\frac{(1+\rho)^5}{2\Delta_-}-\frac{2-3\rho}{8},
\qquad
\kappa_+=\frac1{2\Delta_+}-\frac{2+3\rho}{8}.                \tag{3.3}
\]

Equation (2.1) contains a second copy of the trace coefficient, produced when the unintegrated quadratic action is put into Sturm form. Thus, for terminal matching \(v_\pm(1)=0\), the **full CH quadratic action** obeys
\[
\boxed{\mathcal A_{CH}^{(2)}\ge
 d_+(\rho)V_+^2+d_-(\rho)V_-^2,}                              \tag{3.4}
\]
where
\[
d_+=\frac1{2\Delta_+}-\frac{2+3\rho}{4},
\qquad
d_-=\frac{(1+\rho)^5}{2\Delta_-}-\frac{2-3\rho}{4}.  \tag{3.5}
\]
As \(\rho\downarrow0\),
\[
d_+=\frac34\rho+O(\rho^2|\log\rho|),\qquad
 d_-=-\frac34\rho+O(\rho^2|\log\rho|).                      \tag{3.6}
\]
These asymptotics and the numerical values below were also independently checked from the closed formulas; they do not come from a fit to the cell profiles.
At \(\rho=.1\), \(d_+\approx .05274\), \(d_-\approx-.03565\). The transition must therefore supply the signed trace payment
\[
\boxed{\mathcal A_{tr}^{(2)}
 +d_+(\rho)V_+^2+d_-(\rho)V_-^2\ge0.}                        \tag{3.7}
\]
This is the precise inner-to-CH comparison, much narrower than asking for positivity of an unrestricted sign-changing potential.

## 4. What torsion-free reconstruction adds

The radii and spin variables are not independent:
\[
\dot a_i=u_i+\gamma_i(a),\qquad
\gamma_i=\frac{a_j^2+a_k^2-a_i^2}{a_ja_k}.                   \tag{4.1}
\]
Exactly,
\[
\frac d{dt}\log\frac ac=
\frac{u_1}{a}-\frac{u_3}{c}+\frac{2(c^2-a^2)}{abc}.           \tag{4.2}
\]
Linearize on CH, write \(\theta=\delta\log(a/c)\). Then
\[
\boxed{\frac d{dx}\left[\left(\frac{x}{1+x}\right)^2\theta\right]
 =\frac12f_-(x)v_-(x).}                                      \tag{4.3}
\]
The same \(f_-\) selected by the Sturm factorization is therefore the natural adjoint weight of the metric evolution. With \(\theta(1)=0\),
\[
\int_\rho^1f_-v_-\,dx
=-2\left(\frac{\rho}{1+\rho}\right)^2\theta(\rho).         \tag{4.4}
\]
This moment relation adds an explicit nonnegative square to the sharp minus-channel endpoint problem, but it is not alone sufficient: the transition value \(\theta(\rho)\) can align to make that square vanish. The remaining quadratic theorem is a joint trace inequality in \((V_+,V_-,\theta)\), under regular bolt data and the longitudinal endpoint relations. The full finite-amplitude theorem is its variable-coefficient nonlinear analogue along (4.1), with the signed cubic retained.

Smoothness also does not make the cubic favorable. If
\[
a=A+\alpha t^2+O(t^4),\quad b=A+\alpha t^2+O(t^4),\quad
c=t+\gamma t^3+O(t^5),
\]
then
\[
u_1=u_2=\left(2\alpha-A^{-1}\right)t+O(t^3),\qquad
u_3=-1+O(t^2),
\]
so
\[
\frac{2u_1u_2u_3}{\lambda_2}
=-2(2\alpha-A^{-1})^2t+O(t^3).                               \tag{4.5}
\]
The adverse chamber is generic next to the bolt; compensation must be integrated.

## 5. Geometric validity of the computed competitors

For the implemented fixed-slot profile
\[
g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2,
\]
ordinary bolt smoothness requires
\[
F'(x_0)G'(x_0)=1,\qquad w=O((x-x_0)^2)=O(t^4).                \tag{5.1}
\]
The coefficient shift in the scripts enforces the first condition, and all main runs use `wpow=2`, which enforces the second. `wpow=1` is generally not smooth.

The stored polynomial profiles are not literally CH on an open collar, but they match
\[
F_0=x,\quad G_0=x(1+x),\quad w_0=\log(1+x)
\]
through their second \(x\)-jets at \(X\). If \(q=(F-F_0,G-G_0,w-w_0)\) and
\[
|\partial_x^jq|\le A(X-x)^{3-j},\qquad j=0,1,2,3,
\]
then multiplying \(q\) by a smooth cutoff that is one on \(x\le X-2\varepsilon\) and zero on \(x\ge X-\varepsilon\) gives an exact-CH-collar metric with
\[
|\Delta P|+|\Delta J_6|\le CA^2\varepsilon^3.                \tag{5.2}
\]
This follows because the cutoff metric two-jet differs from CH by \(O(A\varepsilon)\) on an interval of length \(O(\varepsilon)\), while both defect curvatures vanish on CH. The actual envelopes vanish cubically at \(X\), so (5.2) applies profile by profile. Thus their reported costs are limits of genuine smooth exact-collar costs.

## 6. Numerical interpretation after exact factorization

`scripts/perp_transition_analysis.py` evaluates the signed relative action and the exact-CH comparison on the degree-8 \(x_0=.01\) P- and J-target records. For the J-target profile,
\[
P/(8\pi^2)-1=.0018558270
=.0034706397-.0016148127,                                    \tag{6.1}
\]
where the last two numbers are relative squares and the full cubic. The cubic itself splits as
\[
C_+=2.7244\times10^{-5},\qquad C_-=-.0016420567.              \tag{6.2}
\]
Thus positive-cubic regions are small here but real; they must not be discarded in the theorem. At a cut near \(x=.1\), the profile is still about 5--10% away from exact CH in its radii/weights, so the exact operator is a comparison endpoint, not an identity for that non-CH outer portion.

The peer's exported smooth \(x_0=.03\), degree-10 profile was independently evaluated only from \(G,h\) and their first two derivatives in `scripts/perp_export_spin_eval.py`; see `data/perp_dual/peer_export_x003_spin.json`. The coordinate-free positive-square reconstruction gives \(P/(8\pi^2)=1.01857832\), within \(1.75\times10^{-5}\) of the peer curvature value. The relative identity gives
\[
1+.0206129103-.0020170647=1.0185958456,                       \tag{6.3}
\]
reproducing the peer value to the grid accuracy. Here
\[
C_+=.0005819731,
\qquad C_-=-.0025990378,                                     \tag{6.4}
\]
and the independently evaluated scalar square is .0044287927, giving \(J_6/(8\pi^2)\approx1.02300711\). The charge minimum is .118394 near \(x=.107755\). No subthreshold perpendicular profile has been found.

## 7. Scope correction from the signed complex-space-form experiment

Peer S1003A02 proposed the general first-order response
\[
\frac{P(g_a)-P(g;B_a)}{8\pi^2}
=1-a^2\mathcal R_p^+(\zeta,\zeta)+o(a^2),
\qquad \mathcal R^+=W^++\frac{s}{12}I,                        \tag{7.1}
\]
whose proof still requires the full matrix-valued Burns ALE boundary transgression. This Session independently reran the aligned complex-space-form specialization with
\[
K_{bulk}=x+\kappa x^2,
\qquad s=-24\kappa,
\qquad x_0=a^2=.001,
\qquad X=.25.
\]
The outputs are `data/perp_dual/general_bulk_FS_x0001.json` and `general_bulk_CH_x0001.json`:
\[
\kappa=-1:\quad P/(8\pi^2)=.9941059313,
\quad (P/(8\pi^2)-1)/x_0=-5.89407,                            \tag{7.2}
\]
\[
\kappa=+1:\quad P/(8\pi^2)=1.0060581122,
\quad (P/(8\pi^2)-1)/x_0=+6.05811.                            \tag{7.3}
\]
These are direct same-metric \(P\)-integrals with optimizer gradients about \(3\times10^{-7}\), and they exhibit the predicted sign reversal. In particular, a universal statement that every blow-up cell on every Einstein or complex-space-form background costs at least \(8\pi^2\) is false: positive Kähler--Einstein curvature has an explicit U(2)-symmetric subthreshold \(P\) cell. This does **not** contradict the balanced CH problem, whose bulk has the opposite sign; it shows that any general lower theory must retain the background curvature operator, and that the CH coefficient-four problem is a second-order kernel-direction problem rather than a universal local topological charge theorem.

The FS computation concerns \(P\), not the CH-normalized Einstein cost \(J_6\), and it lies outside the negative-KE balanced-family hypotheses. It is nevertheless decisive for the proposed unified theory: the local cell response is curvature-sensitive.

## 8. Present conclusion and next theorem target

The Step-6 relative calibration is correct, including factors, orientation, endpoint term, and cubic sign. The sign-changing exact-CH potential is no longer the unresolved bulk problem: both channels possess positive ground states, and their sharp outgoing Dirichlet-to-Neumann forms are explicit. Exact collar replacement is mathematically valid for the stored smooth profiles. The load-bearing unresolved inequality is now the inner transition payment (3.7), strengthened by the torsion-free moment relation (4.4), first at quadratic order and then at finite amplitude. For \(J_6\), the scalar square supplies additional rank-one coercivity and should be analyzed separately rather than inferred from \(P\).

This remains a theorem target only for the diagonal perpendicular CH class. Even a proof there would not establish the unrestricted cell conjecture or the balanced all-metric coefficient. Beyond symmetry, the natural problem is the gauge-fixed spectral/relative-calibration analogue. Across backgrounds, (7.1) suggests a deeper classification: positive eigenvalues of \(\mathcal R^+\) create first-order cheap cells, negative eigenvalues make aligned cells costly, and kernel directions force a second-order interaction theory.

A small implementation error was also repaired during this review: `perp_dual_cost.py eval` previously read the dual record's degree only from `degU` and therefore silently treated a degree-8 dual record as degree 6. It now reads `deg` first and reproduces the stored degree-8 J-target value \(P/(8\pi^2)=1.0018558257\), \(J_6/(8\pi^2)=1.0019394136\). This did not affect the earlier sweeps, which constructed their cells directly, but it matters for reproducible re-evaluation.
