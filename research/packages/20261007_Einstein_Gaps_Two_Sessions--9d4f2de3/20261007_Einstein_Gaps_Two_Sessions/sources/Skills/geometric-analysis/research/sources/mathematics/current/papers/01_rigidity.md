# An integral monopole obstruction to near-Einstein geometry

## Abstract

The principal analytic result developed in these twelve rounds is a scale-invariant, all-sign joint
gap between Ricci energy and a monopole topological ratio. It applies uniformly to actual monopole
classes with a controlled negative square, and hence universally to special classes. No pointwise
curvature bound, scalar-curvature sign, noncollapse, Sobolev constant, diameter bound, or bound on
the number of classes is assumed. The proof constructs a bounded auxiliary spinor, converts
near-equality in rescaled Seiberg–Witten inequalities into a smooth approximation of a forbidden
Weyl-curvature orbit, and closes the weak contracted-Bianchi equation using an intrinsic covariant
Hessian estimate.

This paper gives the connected proof and its topology-facing consequences. It also records why
several simpler routes fail, which independent geometric statements remain useful, and why the known
construction families do not automatically enter the obstructed topological range. The result is not
a solution of the unrestricted Yau26 question. Its originality relative to the wider literature has
not been established.

## 1. Conventions, principal theorem, and baseline

Let \(M\) be a smooth closed connected oriented four-manifold, with \(b^+(M)\ge2\). Set
\(T=2\chi(M)+3\tau(M)\). An actual monopole class means the real first Chern class \(a\) of a spin-c
structure whose unperturbed Seiberg–Witten equations have a solution for every metric. This is an
existence hypothesis, not a condition on a vector in the intersection form. For a metric \(g\),
write \(a^+\) for its self-dual harmonic projection and \(p=(a^+)^2\).

The norm of \(W^+\) is its Hilbert–Schmidt norm as a trace-free symmetric endomorphism of
\(\Lambda^+\). The associated four-tensor has squared norm \(4|W^+|^2\). Ricci norms are ordinary
tensor norms. Unless an average \(\fint=V^{-1}\int\) is displayed, integrals are unnormalized;
\(V=\operatorname{Vol}(M,g)\). For a real number \(x\), put \(x_-=\max\{-x,0\}\).

A monopole class is *special* if \(a^2\ge T\).
Let \(\mathcal C_{\rm sp}\) be the finite set of special real monopole
classes and define
\[
 \alpha_{\rm sp}^2=
 \inf_{H\in{\rm Gr}_{b^+}^{+}}
       \max_{a\in\mathcal C_{\rm sp}}(a_H^+)^2,\qquad
 \beta_{\rm sp}^2=
 \max_{v\in{\rm Hull}(\mathcal C_{\rm sp})}v^2 .
\]
Here \(H\) ranges over all maximal positive subspaces, not only those
known to be realized by metrics. Assume \(\alpha_{\rm sp}^2>0\).
Define the scale-invariant Ricci-energy fraction
\[
 \mathcal E(g)=
 \frac{4\int|\operatorname{Ric}^{\circ}|^2+
                  \int(s-\bar s)^2}{\int|\operatorname{Ric}|^2},
 \qquad \bar s=V^{-1}\int s .
\]
The denominator is nonzero under the positive monopole-projection
hypothesis.

**Theorem A: the all-sign special-monopole gap.**
There is a universal constant \(\varepsilon_0>0\) such that
\[
 \boxed{\quad
 \mathcal E(g)+
       \left(\frac{T}{\alpha_{\rm sp}^2}-\frac23\right)_+
       \ge\varepsilon_0 .
 \quad}                                                     \tag{1}
\]
The same assertion holds with any \(0<A\le\alpha_{\rm sp}^2\),
in particular \(A=\beta_{\rm sp}^2\) when this is positive.
It holds for every metric, with no additional geometric bounds.
The constant is existential and is not claimed to be sharp.

A more flexible version selects, for each metric, an actual class with \(p\ge A>0\) and
\(a^2\ge-C_AA\). Its constant depends only on \(C_A\). The alternative hypothesis \(a^2\ge T-C_AA\)
also suffices. These are square bounds on the selected classes, not bounds on Euler characteristic.
The distinction matters for arbitrary monopole sets. The final statements are [round4,
§§7–8](../round4_rigidity.md), [the all-sign corollary](../round4_all_sign_gap.md), and [round5,
§§2–3](../round5_rigidity.md).

The installed baseline already proved an exact Einstein gap above \(T/A=2/3\), under a metricwise
monopole projection hypothesis and an Euler bound \(\chi\le LA\). It also contained a universal
exact gap for the indicated complex-surface blow-ups. Those conclusions are not discoveries of the
twelve rounds. The baseline's approximate results required bounded diameter, or a conditional
regularity mechanism for collapsing harmonic charts. See the preserved [rigidity
baseline](../baseline/research/20260916_rigidity.tex), [uniform-gap
baseline](../baseline/research/20260916_uniform_gap.tex), and [baseline research
synthesis](../baseline/research/20260916.md). The advance here is a different intrinsic analytic
closure, followed by removal of pointwise Ricci control and optimization over Einstein sign and
scale. It does not prove the baseline's proposed chart-regularity principle, and it does not subsume
every abstract projection hypothesis without the stated class-square control.

## 2. Rescaled monopoles and a scalar-safe near-equality argument

For the negative normalization, put
\[
 E=\operatorname{Ric}+g,\quad e=s+4,\quad
 \mathcal O_0={\rm Orbit}\,
       {\rm diag}(-1/6,1/12,1/12),\quad
 F=\operatorname{dist}(W^+,\mathcal O_0)^2 .
\]
Set \(q=-s+\sqrt6|W^+|\), \(q_+=\max(q,0)\), and
\[
 \Delta_+=\int q_+^2-72\pi^2p,\qquad
 \mathcal C=\int(|E|^2+F),\qquad
 \kappa=\frac{\mathcal C+\Delta_+}{V},\qquad
 B_a=\frac{(-a^2)_+}{V}.
                                                               \tag{2}
\]
The classical monopole inequalities imply \(\Delta_+\ge0\).
The core analytic assertion, from which (1) follows, is
\[
                         (1+B_a)\kappa\ge c>0.             \tag{3}
\]
Its proof occupies this and the next two sections.

For every smooth positive \(f\), conformal covariance supplies a
solution
\[
 D_A\Phi=0,\qquad -iF_A^+=f\sigma(\Phi),\qquad
 \psi=2\sqrt2\,\sigma(\Phi),\quad
 \rho=|\Phi|^2=|\psi|,\quad u=3\rho/2.
                                                               \tag{4}
\]
We use \(|\sigma(\Phi)|^2=|\Phi|^4/8\).
One way to see existence is to solve the ordinary equations for
\(\widehat g=f^{-2}g\) and use the spinor conformal weight
\(\Phi=f^{-3/2}\widehat\Phi\).
This requires an actual monopole, not just a formal curvature identity.
The classical rescaling and curvature inequalities are in
[LeBrun, Lemma 3.7 and Proposition 3.8](https://arxiv.org/abs/math/0611450).

The spinor and self-dual-form Weitzenböck formulas give four
nonnegative defects:
\[
 \begin{aligned}
 D_{\rm amp}&=2\int|d\rho|^2,\\
 D_{\rm quad}&=\int(4\rho|\nabla_A\Phi|^2-|\nabla\psi|^2),\\
 D_{\rm H}&=\int(|d\psi|^2+|d^*\psi|^2),\\
 D_{\rm eig}&=2\int\bigl(\langle W^+\psi,\psi\rangle
                        +\sqrt{2/3}|W^+|\rho^2\bigr).
 \end{aligned}
\]
The second is nonnegative by the derivative inequality for the
quadratic spinor map; the fourth uses the lowest-eigenvalue bound for
a trace-free symmetric three-by-three matrix.
Writing \(D_0\) for their sum, their exact subtraction is
\[
                  \frac{27}{8}D_0=\int(qu^2-fu^3).         \tag{5}
\]
In particular this identity remains valid when \(q\) changes sign.

The same calculation with the actual smallest eigenvalue \(w\) yields
\[
 \int(2s/3+2w)_-^2\ge32\pi^2p,\qquad
 \int s_-^2\ge32\pi^2p.                                  \tag{6}
\]
For the first inequality, choose weights tending from above to the
square root of \((2s/3+2w)_-\), using strictly positive regularizations.
The curvature moment is bounded below by \(32\pi^2p\), whereas Hölder
and the corresponding nonnegative Weitzenböck deficit bound it above
by the fourth-power weight integral. Taking the regularization limit
gives (6). The full constants, conformal identification, quadratic
derivative calculation, and weighted-form identities are derived in
[the self-contained monopole input](../round3_monopole_input.md).

The optimized choice \(f=\sqrt q\) is not scalar-safe for general
metrics: \(q\) may be negative, and the maximum-principle spinor bound
may be lost. Instead set
\[
 Q=\max(q,3),\qquad
 f_0=\max\left\{\sqrt Q,\frac{(-s)_+}{4}\right\},
                                                               \tag{7}
\]
and solve (4) for smooth majorants \(f_j\ge f_0\) converging uniformly
on each fixed compact metric; no monotonicity is required.
The maximum principle gives \(0\le\rho\le4\), hence \(0\le u\le6\).
The modification costs only scalar squared error:
\[
 0\le Q^2-q_+^2\le9e^2,\qquad
 0\le f_0^2-Q\le\frac9{16}e^2.                            \tag{8}
\]
Neither a bound on derivatives of the weight nor a uniform bound on
\(\int f_j^4\) is required.

The important distinction is between *ideal* and *actual* moments.
For the solution associated to \(f_j\), let
\[
 C=\int Qu^2,\quad Z=\int\sqrt Q\,u^3,\quad
 E_Q=\int Q^2,\quad P=C-Z .
\]
Equation (5) gives
\[
 P=\frac{27}{8}D_0+
       \int(Q-q)u^2+\int(f_j-\sqrt Q)u^3\ge\frac{27}{8}D_0.
                                                               \tag{9}
\]
Topology controls \(C_{\rm act}=\int f_j^2u^2
=18\|F_A^+\|_2^2\ge72\pi^2p\), not \(C\) directly.
The bounded spinor and (8) supply the missing comparison:
\[
 0\le C_{\rm act}-C\le\frac{81}{4}\int e^2+o(1).
\]
Hölder gives \(C\le E_Q^{1/3}Z^{2/3}\), and \(Z\le C\) then gives
\[
 0\le E_Q-C\le S_0+o(1),\qquad
 S_0=\Delta_++\frac{117}{4}\int e^2.                       \tag{10}
\]
Writing \(\theta=(Z/E_Q)^{1/3}\) and
\(H=E_Q^{1/3}Z^{2/3}-C\), one has
\[
 E_Q-C=H+\frac{1+\theta}{\theta^2}(P+H)\ge2P.
\]
The corresponding moment calculation for the probability measure
\(Q^2d\mu/E_Q\) gives
\[
 D_0\le\frac4{27}S_0+o(1),\qquad
 \int Q(u-\sqrt Q)^2\le S_0+o(1),\qquad
 \|d\rho\|_2^2,\ \|d\psi\|_2^2\le\frac2{27}S_0+o(1).
                                                               \tag{11}
\]
Every error here can be made arbitrarily small for the fixed metric;
there is no assumed convergence of the solutions as \(j\to\infty\).
In a varying-volume argument the approximation error is chosen small
relative to \(V\). This order of choices prevents a hidden uniform
smoothing assumption. See [round4, §§3–4](../round4_rigidity.md).

## 3. A smooth Weyl model and an intrinsic second-derivative estimate

Near the orbit \(\mathcal O_0\), the quantity \(q\) is near \(9/2\):
\[
 \int(q-9/2)^2\le12\mathcal C .
\]
Clipping at three does not increase that squared distance.
Consequently (11) also controls \(\rho-\sqrt2\) in \(L^2\).
Let \(\Pi\) be a measurable projection onto a lowest Weyl eigenline.
On \(\{F\le1/256\}\), its spectral gap is at least \(1/8\).
On the complement, the volume is at most \(256\int F\).
The eigenline defect in (11), this good-set gap, and \(\rho\le4\)
therefore control the component \((I-\Pi)\psi\) globally in \(L^2\).
No global smooth eigenline or nonvanishing spinor is assumed.

The globally smooth replacement is the polynomial
\[
             A_\psi=\frac{\rho^2}{24}I-\frac18\psi\otimes\psi .
                                                               \tag{12}
\]
At \(\rho=\sqrt2\) it lies in \(\mathcal O_0\).
For \(A_0=I/12-\Pi/4\), the elementary rank-one identity gives
\[
 |A_\psi-A_0|^2
 \le\frac{\rho^2}{16}|(I-\Pi)\psi|^2
             +\frac{(\rho^2-2)^2}{48}.
\]
Combining this with (10)–(11) yields the sufficient estimate
\[
 R=W^+-A_\psi,\qquad
                    \|R\|_2^2\le2\Delta_++8500\mathcal C+o(1).
                                                               \tag{13}
\]
The coefficient is convenient, not optimized.
The source proof is [round4, §5](../round4_rigidity.md);
[round2 rigidity](../round2_rigidity.md) contains the earlier global
good-set/bad-set and phase-averaging constructions.

The crucial regularity is intrinsic. For a bounded section \(v\) of
a metric bundle over a closed four-manifold, let
\(H=\nabla^2v\), \(L=\operatorname{tr}\nabla^2v\), and
\(K=\|v\|_\infty\).
Integrating the divergence of
\(|\nabla v|^2\langle v,\nabla v\rangle^\sharp\) gives
\[
                       \|\nabla v\|_4^2\le4K\|H\|_2.       \tag{14}
\]
This is a covariant integration-by-parts inequality, not a Sobolev
embedding with a geometric constant.
If \(\mathcal F_{ij}\) denotes the bundle curvature, use the ordered
norm \(|\mathcal F|^2=\sum_{ij}|\mathcal F_{ij}|_{\rm HS}^2\).
Commuting derivatives and integrating once gives the exact formula
\[
 \begin{aligned}
 \int|H|^2={}&\int|L|^2-
        \int{\rm Ric}_{ij}\langle\nabla_i v,\nabla_jv\rangle\\
 &+\sum_{ij}\int\langle\mathcal F_{ij}\nabla_jv,\nabla_i v\rangle
       +\frac12\sum_{ij}\int|\mathcal F_{ij}v|^2 .
 \end{aligned}
\]
Thus (14) and absorption imply
\[
 \|H\|_2^2\le2\|L\|_2^2+
                   32K^2\|{\rm Ric}\|_2^2+33K^2\|\mathcal F\|_2^2 .
                                                               \tag{15}
\]
No derivative of curvature remains. Curvature need not be small.

Apply this to the spinor in (4). The curvature of the positive spin
connection uses only \(W^+\), scalar curvature, trace-free Ricci, and
the determinant curvature; \(W^-\) acts trivially on its spin factor.
Chern–Weil gives
\[
 \|F_A\|_2^2=2\|F_A^+\|_2^2-4\pi^2a^2
       \le4\int f_j^2+4\pi^2(-a^2)_+ .
\]
The spinor equation bounds the rough Laplacian using \(s\), \(f_j\),
and \(\rho\le4\). Equations (8), (13), and (15) now give
\[
 \int\bigl(|\nabla_A^2\Phi|^2+|\nabla_A\Phi|^4+
                              |\nabla^2A_\psi|^2\bigr)
       \le C\bigl(V+\mathcal C+(-a^2)_+\bigr)+o(1).
                                                               \tag{16}
\]
The quartic spinor polynomial in (12) accounts for the last term.
All estimates are extensive before normalization, so no unrecorded
volume factor enters. The first version removed full-curvature bounds
under pointwise Ricci control in [round3 rigidity](../round3_rigidity.md).
The \(L^2\)-Ricci version (15) and the clipped weight remove that
remaining pointwise assumption in [round4, §§2 and 6](../round4_rigidity.md).

## 4. Weak Bianchi becomes a contradiction, not a tautology

Let \(J_\psi=\operatorname{div}{\mathcal W}(A_\psi)\), where
\(\mathcal W\) denotes the Weyl four-tensor identification.
The contracted Bianchi identity, \(W^+=A_\psi+R\), and integration
by parts imply, for every smooth test tensor \(U\),
\[
 \left|\int\langle J_\psi,U\rangle\right|
     \le C(\|E\|_2+\|R\|_2)\|\nabla U\|_2 .
                                                               \tag{17}
\]
This is an intrinsic \(H^{-1}\) estimate on the metric under study.
It does not identify Sobolev spaces across a collapsing sequence.
By (16), it is now legitimate to test with \(U=J_\psi\), obtaining
\[
               \fint|J_\psi|^2
                  \le C\sqrt\kappa\sqrt{1+\kappa+B_a}+o(1).
                                                               \tag{18}
\]

There is also a lower bound. The weighted self-dual-form
Weitzenböck identity and an explicit first-jet contraction give
\[
 \begin{aligned}
 \int|J_\psi|^2={}&-\frac1{64}\int\rho^2 B_\psi
       +\frac1{16}\int\rho^2|d\psi|^2
       -\frac5{96}\int\rho^2|d\rho|^2\\
       &+\frac18\int\rho
                   \langle\iota_{\nabla\rho}\psi,*d\psi\rangle,\\
 B_\psi={}&\frac{s}{3}\rho^2-2\langle W^+\psi,\psi\rangle .
 \end{aligned}
\]
The first term, after substituting (12), is
\[
 -\frac{\rho^2B_\psi}{64}
   =-\frac{s\rho^4}{192}-\frac{\rho^6}{384}
                          +\frac{\rho^2\langle R\psi,\psi\rangle}{32}.
\]
At the calibration \(s=-4,\rho=\sqrt2,R=0\), this equals \(1/16\).
The amplitude and differential defects bound every error, hence
\[
                   \fint|J_\psi|^2
                       \ge\frac1{16}-C(\sqrt\kappa+\kappa)+o(1).
                                                               \tag{19}
\]
For sufficiently small \(\kappa\), (18)–(19) force
\(\kappa(1+\kappa+B_a)\ge c\); outside that small range the desired
lower bound is immediate. This proves (3).
The first-jet identities are proved in
[the monopole-input appendix](../round3_monopole_input.md), not
assumed as a compactness statement.

The logical improvement over the earlier weak argument is specific. A bounded \(W^{1,2}\) Weyl
model, an \(L^2\)-small remainder, and an \(H^{-1}\)-small divergence do not by themselves imply
strong control of derivative energy. In the formal calibration, the model retains positive
derivative energies, including the \(1/16\) in (19). The weighted Weitzenböck identity alone merely
reproduces this fact. Estimate (16) supplies the additional derivative needed in (17). This is why
the proof survives collapse without extracting a regular limit manifold.

## 5. Topological transfer, sign optimization, and actual class selection

The passage from (3) to Ricci energy uses the exact identity
\[
 4\pi^2T=\int\left(\frac{s^2}{24}+2|W^+|^2
                                      -\frac12|{\rm Ric}^{\circ}|^2\right).
                                                               \tag{20}
\]
Put \(r=\fint|{\rm Ric}+g|^2\) and \(d=(T/A-2/3)_+\).
To allow scalar-positive regions, set
\[
 \alpha=\sqrt{2/3}|W^+|,\quad w=\lambda_{\min}(W^+),\quad
 t=s+8\sqrt6|W^+|,\quad b=2s/3+2w,\quad
 G=(2s/3-2\alpha)^2-b_-^2\ge0 .
\]
The negative part in \(G\) is essential; deleting it invalidates
nonnegativity for unrestricted scalar curvature.
The algebraic identity
\[
 t^2+18G=216(s^2/24+2|W^+|^2)-18b_-^2
\]
and (6), (20) give
\[
 \int(|E|^2+e^2+t^2+G)
                    \le109\int|E|^2+864\pi^2Ad .
\]
Pointwise \(F\le e^2+t^2+G\); the proof separates \(s\le-3\) from
\(s>-3\). Also
\[
 27(s^2/24+2|W^+|^2)-q^2=t^2/8 .
\]
It follows that
\[
 \kappa\le\frac{245}{2}r+972\pi^2(A/V)d,\qquad
 \frac AV\le\frac{4+r}{4\pi^2}.
                                                               \tag{21}
\]
For \(r\le1\), this gives \(\kappa\le1215(r+d)\).
If \(a^2\ge-C_AA\), then \(B_a\le5C_A/(4\pi^2)\), and (3)
proves a positive lower bound for \(r+d\).
For \(a^2\ge T-C_AA\), restrict first to \(r\le1/4\):
\[
 4\pi^2T\ge
       \left((4-2\sqrt r)^2/24-r/2\right)V\ge V/4>0.
\]
The first square condition follows, while \(r>1/4\) is an immediate
alternative. This is why the \(1/4\) branch must remain in that version.

The positive normalization requires only classical inputs.
If \(r_+=\fint|{\rm Ric}-g|^2\), then (6) implies
\(A/V\le r_+/(8\pi^2)\).
When \(r_+\le1/4\), (20) gives \(4\pi^2T/V\ge1/4\).
If also \(d\le1/4\), the previous upper bound instead gives
\(4\pi^2T/V\le11/96\), a contradiction.
Thus \(r_++d>1/4\).
Combining both signs and rescaling the metric proves
\[
 \inf_{\lambda\ne0}
      \frac{\int|{\rm Ric}-\lambda g|^2}{\lambda^2V}+d
                                                        \ge c(C_A)>0.
                                                               \tag{22}
\]
If \(S=\int s\) and \(R_2=\int|{\rm Ric}|^2\), the infimum is
\(4-S^2/(VR_2)=\mathcal E(g)\).
For \(S\ne0\) it is attained at \(\lambda=R_2/S\); for \(S=0\)
the infimum is four. The positive branch is a classical corollary,
not a second independent analytic method.

It remains to supply actual classes. For a finite monopole set
\(\mathcal C_0\), convexity gives
\[
 v^2\le(v_H^+)^2\le
       \sum_i t_i(a_{i,H}^+)^2\le\max_i(a_{i,H}^+)^2
       \quad\text{when }v=\sum_i t_i a_i.
\]
Hence \(\beta_0^2\le\alpha_0^2\), and every metric admits a selected
class with \(p\ge\alpha_0^2\).
Nonzero chamber-independent ordinary SW invariants and nonzero
Bauer–Furuta invariants give persistence under generic perturbations.
The expected dimension \((a^2-T)/4\) must then be nonnegative, so
these classes are special. This is the established implication
recorded in [Kotschick's monopole-class discussion](https://arxiv.org/abs/math/0306022);
it is not a new transversality theorem.
Together with (22), it proves Theorem A.

For all ordinary monopole classes on a fixed manifold, the same argument works with
\(C_M=\max_a(-a^2)_+/\alpha_{\rm all}^2\), when \(\alpha_{\rm all}^2>0\). Its constant depends on
\(C_M\). Generic-perturbation transversality cannot simply be imposed on an ordinary class defined
only by unperturbed metricwise existence. Nor does convex geometry remove this dependence: in
signature \((2,1)\), the four vectors \(\pm(1,0,L),\pm(1,0,-L)\) have \(\alpha^2=\beta^2=1\) but
square \(1-L^2\). This is an algebraic counterexample to an inference, not a realized family of
monopole classes.

For \(M=X\#k\overline{\mathbb{CP}}^{\,2}\), where \(X\) is minimal
of general type, \(b^+(X)>1\), and \(A=c_1^2(X)>0\), the actual
full-sign classes have square \(A-k=T\).
Averaging their projected squares selects \(p\ge A\), yielding
\[
             \mathcal E(g)+(1/3-k/A)_+\ge c_*>0
                                                               \tag{23}
\]
uniformly in \(X,k,g\).
The preceding pointwise-Ricci versions are preserved in
[the round3 joint gap](../round3_joint_gap.md) and
[the controlled-square extension](../round3_general_monopole.md).
Their hypotheses are weakened by the integral theorem, not invalidated.
More generally, let \(X\) have \(b^+(X)\ge2\) and a nonzero
chamber-independent SW class \(c\) with \(A=c^2>0\).
Let \(N\) be closed oriented with \(b^+(N)=0\), and use the verified
full-sign connected-sum input
\(a_\epsilon=c+\sum\epsilon_i e_i\), \(e_ie_j=-\delta_{ij}\).
Then \(A\ge T_X\). For \(k=b_2(N)\), \(\ell=b_1(N)\), and
\(D=k+4\ell\), one has \(T_{X\#N}=T_X-D\),
\(a_\epsilon^2=A-k\ge T_{X\#N}\), and a sign average gives \(p\ge A\).
Thus (22) gives
\[
       \mathcal E(g)+((T_X-D)/A-2/3)_+\ge\varepsilon_0 .
\]
The required gauge-theoretic gluing theorem and its precise input,
including the standard \(N=k\overline{\mathbb{CP}}^{\,2}
\#\ell(S^1\times S^3)\), are stated in
[round5, §4](../round5_rigidity.md).
Betti numbers alone do not provide those monopoles.

## 6. Supporting results and routes that cannot replace the proof

Several earlier results retain independent value. For \(s=-4\) and \(\operatorname{div}W^+=0\), an
explicit scalar polynomial in \(|W^+|^2\) and \(\det W^+\) has strictly positive Laplacian if the
spectrum stays in a sufficiently small box around \((-1/6,1/12,1/12)\). A maximum principle excludes
that whole box. However, no globally defined \(C^2\), orthogonally invariant scalar multiplier can
simultaneously have a nonnegative derivative quadratic term for every harmonic-Weyl first jet and a
strictly positive reaction at this orbit. Restriction to the negative double-eigenvalue ray
\(u\,{\rm diag}(-2,1,1)/\sqrt6\) gives \((u^{2/3}\varphi'(u))'\ge0\), hence \(\varphi'\ge0\); the
required reaction has the opposite sign. A separate jet test excludes the same two sign properties
for locally defined homogeneous degree-two invariant multipliers. These results rule out specified
scalar strategies, not all maximum principles; see [round1 rigidity](../rigidity.md).

Small Ricci error also does not control Cotton energy. On a closed negative Einstein background, an
actual oscillatory metric perturbation of amplitude \(\epsilon/k^2\) has Ricci error \(O(\epsilon)\)
and bounded full curvature, but Cotton energy bounded below by \(c\epsilon^2k^2\). Taking
\(\epsilon\to0\) and \(k\) sufficiently large makes Cotton energy diverge. The construction is a
metric counterexample to that estimate, not to the monopole gap. A separate algebraic concentration
example shows why small quadratic calibration defect need not control cubic Weyl terms; it is
explicitly not asserted to be curvature of actual metrics. See [round1 rigidity](../rigidity.md) and
its [independent review](../rigidity_review.md).

At the functional endpoint, bounded auxiliary fields and small \(L^2\) remainders do not suffice to
control products \(R\nabla a\) in \(H^{-1}\). The localized oscillatory example in [round2
rigidity](../round2_rigidity.md) establishes this without claiming the fields solve monopole
equations. It explains why (16), rather than an unsupported product estimate, is the load-bearing
step in the final argument.

There is also a genuinely geometric result without monopoles:
for each full-curvature bound \(K\),
\[
 |{\rm Rm}|\le K
 \quad\Longrightarrow\quad
 \fint\bigl(|{\rm Ric}+g|^2+
                 {\rm dist}(W^+,\mathcal O_0)^2\bigr)\ge c(K)>0 .
\]
Its proof in [round2 rigidity, §9](../round2_rigidity.md) uses buffered
exponential-coordinate pullbacks, multiplicity control, and local
elliptic estimates; collapse is allowed.
On already controlled charts, the injective symbol
\(|\sigma_D(\xi)A|^2=|\xi|^2|A|_{\rm HS}^2\) supplies strong local
\(L^2\) curvature convergence without a Cotton \(L^2\) bound.
This is proved in [round2 weak curvature](../round2_weak_curvature.md).
These geometric statements
remain distinct: the later monopole theorem removes the curvature bound
using extra equations, not for arbitrary metrics.
The localized version says that fixed-radius neighborhoods of the high-curvature
set fill asymptotically all volume in a hypothetical calibrated degeneration;
it does not say that the high-curvature set itself has positive volume.

The exact Ricci-box calculation gives useful noncritical estimates.
If the Ricci eigenvalues are \(-1+a_i\), \(|a_i|\le d\le1\), then
\[
 \frac{s^2}{24}-\frac12|{\rm Ric}^{\circ}|^2
 \ge
 \begin{cases}
  \frac23(1-d)^2,&0\le d\le1/3,\\
  \frac23(1+d)(1-2d),&1/3\le d\le1.
 \end{cases}
\]
In particular \(d<1/2\) implies the strict Hitchin–Thorpe inequality.
The corresponding \(-3g\) normalization supplies closed volume bounds
and conditional connector-volume obstructions, provided the retained
end volume and the closed Chern–Weil budget are genuinely matched.
See [the curvature-box proof and checker](../curvature_box.md).

For the fixed blow-up ratio \(p=k/A>1/3\), exact box optimization
improves the elementary Ricci-error lower bound to
\[
 d\ge
 \begin{cases}
 \sqrt{(3p-1)/(p+5)},&1/3<p\le2\sqrt3-3,\\
 \bigl(\sqrt{(3p-1)(3p+15)}-(3p-1)\bigr)/8,
                         &2\sqrt3-3\le p<1 .
 \end{cases}
\]
For \(p\ge1\), \(d\ge1/2\).
This is sharp optimization of the relevant algebraic quotient,
not an assertion that a metric attains the box extremizer.
It tends to zero at \(p=1/3\), so it does not replace (23).
See [the fixed-ratio argument](../fixed_ratio.md).

## 7. What the obstruction says about the actual constructions

The original slow-twist surface bundles \(E_D\), their indicated finite covers, and the later closed
product-block examples carry near-Einstein sequences but do not lie in the critical monopole band.
For \(E_D\), both orientations have \(\alpha_{\rm all}^2=\beta_{\rm all}^2 =\alpha_{\rm
sp}^2=\beta_{\rm sp}^2=T\). The near-Einstein scalar budget gives the upper bound; the canonical
class gives the lower bound. Their ratio is one, not \(2/3\). This baseline-compatible fact must not
be turned into a new no-Einstein theorem for \(E_D\). The later exact computation of basic classes
on the one-block self-gluings likewise does not move their monopole ratio into the forbidden range;
see [round12 global](../round12_global.md). Classical monopole equality cases also determine several
variational infima on those gluings, but attainment of the full-curvature infimum is equivalent to
the still-open existence of an Einstein metric. That distinction is proved in [round11
variational](../round11_variational.md) and developed in Chapter 3.

The connected-sum result does obstruct modified objects. If \(X\) is one of the verified symplectic
inputs with \(A=T_X>0\) and \(D/A\) is sufficiently near or above \(1/3\), then every metric on
\(X\#N\) has a positive Ricci-energy fraction. Any surgery proposal preserving arbitrarily tight
near-Einstein metrics through that modification is impossible. This is a statement about the
modified smooth manifold, not evidence that the unmodified construction has no Einstein metric.

For hyperbolic \(A_1\) resolutions, the incompatibility is sharper.
Assume an actual uniformly near-negative-Einstein sequence on a fixed
resolution, with fixed \({\rm Ric}=-g\) orbifold exterior, limiting
volume \(V_0\), and vanishing replacement-region volume.
Put \(B=V_0/(6\pi^2)\); let \(m\) count the positively oriented
signature contributions among the Eguchi–Hanson replacements.
Then
\[
 T=B+6m,\qquad
 \lim\int|W^+|^2=12\pi^2m,\qquad
             \alpha_{\rm all}^2\le\frac43B+m .
\]
The \(L^1\) Weyl contribution of the shrinking regions tends to zero.
Consequently \(T/\alpha_{\rm all}^2\ge3/4\), whenever the denominator
is positive. The filling and exterior hypotheses are essential;
an orbifold label alone is not a construction theorem.
The full accounting is [round5, §6](../round5_rigidity.md).
Positive-scalar input families cannot supply positive monopole projection:
the spinor Weitzenböck formula forces reducibility. They therefore require
a different obstruction, with chamber-sensitive \(b^+=1\) cases kept separate.

The filling-independent extension in [round7 endpoint](../round7_endpoint.md)
assumes a fixed smooth \(M\), uniform Ricci defect tending to zero,
volume tending to \(V_0\), and replacement-region volume tending to zero.
It also requires a fixed negative Einstein orbifold exterior and
convergence of the exterior first and second moments of \(|W^+|\).
Gromov–Hausdorff convergence alone does not provide these hypotheses.
Write \(w_0=|W_O^+|\) and let \(E_{\rm bub}\ge0\) be the limiting
self-dual Weyl energy in the vanishing-volume regions. Define
\[
 T_0=\frac1{4\pi^2}\int_O(2/3+2w_0^2),\qquad
 J_0=\frac1{72\pi^2}\int_O(4+\sqrt6w_0)^2,\qquad
 D_0=J_0+\frac{E_{\rm bub}}{12\pi^2}.
\]
Then
\[
 T=T_0+\frac{E_{\rm bub}}{2\pi^2},\qquad
 \alpha_{\rm all}^2\le
       \min\{V_0/(2\pi^2),D_0\},
\]
and the decisive exact identity is
\[
 T-\frac23D_0=
   \frac4{9\pi^2}
     \left[\int_O\left(w_0-\frac1{2\sqrt6}\right)^2+E_{\rm bub}\right].
                                                               \tag{24}
\]
Thus curvature concentration does not drive such a construction
toward the critical ratio: its contribution has ratio six.
Near-criticality would require vanishing normalized bubble energy,
the indicated bulk Weyl-modulus calibration, and saturation by
actual monopole classes simultaneously.

Real-hyperbolic, complex-hyperbolic, and bidisk bulks remain at ratio at least \(3/4\) in either
orientation under these hypotheses. For a Kähler bulk in its complex orientation, the stronger lower
bound is \(1+E_{\rm bub}/V_0\). In the opposite orientation, the algebraic critical Chern slope is
\(c_1^2/c_2=32/11\). This is a selection criterion, not an example: no suitable construction or
monopole saturation follows from the slope calculation. Nor does constant calibrated Weyl norm alone
yield the forbidden eigenvalue spectrum. This distinction prevents an unjustified strictness claim
for arbitrary negative Einstein orbifold bulks. Construction hypotheses and global topology are
treated in [Chapter 2](02_constructions.md) and [Chapter 3](03_global.md).

## 8. Later gauge work, verification, and remaining scope

The later nonabelian investigation sought a different route to the same closed objects, since
changing constants in (1) cannot bridge the ratio-one examples. It did not produce the needed
unperturbed coupled solutions. The early literal-projection algebra was not identified conclusively
with all of Leung's published twisting conventions; the unconditional rank-one no-transfer inference
was withheld. The preserved [round7 note](../round7_rigidity.md) must be read with that
qualification, not as a proof that every natural transfer fails.

There are nevertheless concrete constraints and constructions. [Round8](../round8_nonabelian.md)
gives a Chern–Weil lower bound for curvature or second-fundamental-form energy of a projective line.
[Round9](../round9_nonabelian.md) constructs anisotropic seeds solving Dirac and determinant-trace
equations, leaving the trace-free curvature equation unsolved. [Round10](../round10_nonabelian.md)
shows that balanced full-rank seeds with small anti-self-dual curvature cannot close that final
equation by a small residual correction. [Round11](../round11_rankone.md) identifies the line
second-fundamental-form term at rank one, where the Dirac right inverse need not become singular.
These are auxiliary-system results with explicitly fixed conventions.

[Round12 uniformization](../round12_uniformization.md) derives a corrected block connection and
tracks its central Chern class and graded energy. A block connection preserving an indefinite
Hermitian form cannot use a positive-unitary energy argument without the additional graded identity.
The resulting explicitly defined system has a conditional classification; it is not asserted to
coincide with the entire published converse or to be supplied by Taubes. The [Schoen-surface
control](../round12_control.md) confirms the logical boundary: ordinary SW information, negative
Einstein geometry, and signature zero do not force local symmetry. The fuller gauge and global
discussion belongs to Chapter 3.

The methodological gain is intrinsic derivative control of an actual bounded field,
allowing the weak Bianchi equation to be tested against its own divergence.
Clipping preserves this mechanism at the scale-invariant \(L^2\) threshold.
Minimax selection organizes established gauge inputs; the positive branch,
curvature-box optimization, and concentration accounting use classical identities.

The [coverage ledger](01_rigidity_coverage.tsv) records every supporting proof,
review, and checker, including the [integral checker](../round4_rigidity_check.py).
These scripts verify coefficients, Clifford contractions, finite-dimensional
extrema, and examples; they do not prove PDE existence or establish priority.

No theorem here constructs a global Einstein metric, excludes every Einstein metric
on the ratio-one families, or regularizes arbitrary near-Einstein sequences.
The completed result is (1), its verified topology transfers, and the compatibility
restrictions specifying where this obstruction addresses the original problem.
