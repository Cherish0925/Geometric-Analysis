# An integral Ricci gap from truncated rescaled monopoles

20 September 2026. The pointwise Ricci hypothesis can be removed from
the round-three monopole gap. The result below uses only integral
curvature errors. Its new ingredient is a modified rescaling weight that
bounds the spinor while charging its additional curvature cost to the
scalar L2 error. It does not require a pointwise scalar bound or a bound
on the fourth power of that weight.

The conclusion is a quantitative L2 obstruction for the stated actual
monopole families. It is not a general Einstein-existence theorem or a
resolution of unrestricted Yau26. The universal positive constants are
not numerically optimized.

## 1. The integral calibration theorem

Let (M,g) be a smooth closed oriented four-manifold. Write V=Vol(M,g),
\(E=\operatorname{Ric}+g\), \(e=s+4\), and use operator
Hilbert--Schmidt norm for the self-dual Weyl operator. Let

\[
 \mathcal O_0=\operatorname{Orb}\operatorname{diag}(-1/6,1/12,1/12),
 \qquad F=\operatorname{dist}_{\rm HS}(W^+,\mathcal O_0)^2,
\]
\[
 \mathcal C=\int(|E|^2+F),\qquad
 q=-s+\sqrt6|W^+|,\qquad q_+=\max(q,0).
\]

Suppose a is an actual monopole class for which the rescaled
Seiberg--Witten equations are solvable for every smooth positive weight,
and \(p=(a^+)^2>0\). Define

\[
 \Delta_+=\int q_+^2-72\pi^2p\ge0,\qquad
 \kappa=\frac{\mathcal C+\Delta_+}{V},\qquad
 B_a=\frac{(-a^2)_+}{V}.                                    \tag{1}
\]

**Theorem 1.** There is a universal c>0 such that

\[
 \boxed{(1+B_a)\kappa\ge c.}                               \tag{2}
\]

No pointwise curvature, scalar sign, Ricci lower bound, noncollapse,
Sobolev, volume, diameter or curvature-derivative hypothesis is imposed.
The actual monopole and its indicated Chern-square factor are essential
inputs. Norms of Ricci in this note are ordinary tensor norms.

The nonnegativity of \(\Delta_+\) follows from the spectral monopole
inequality. If \(w=\lambda_{\min}(W^+)\), then
\(w\ge-\sqrt{2/3}|W^+|\), so

\[
 (-(2s/3+2w))_+\le(2/3)q_+.
\]

The inequality
\(\int(2s/3+2w)_-^2\ge32\pi^2p\) therefore implies
\(\int q_+^2\ge72\pi^2p\). Its direct rescaled-equation proof is
in Section 6 of [the local monopole input](round3_monopole_input.md).
It is the signed form of the classical estimate in
[LeBrun's Theorem 2.3](https://arxiv.org/abs/math/0003068).

## 2. A Hessian estimate using only Ricci L2

Let u be a smooth bounded section of a Hermitian bundle with compatible
connection and curvature \(\mathscr F_{ij}\). Put K=\(\|u\|_\infty\)
and use \(|\mathscr F|^2=\sum_{ij}|\mathscr F_{ij}|_{\rm HS}^2\).
The covariant integration-by-parts identities proved in round three are

\[
 \|\nabla u\|_4^2\le4K\|\nabla^2u\|_2,                   \tag{3}
\]
\[
\begin{split}
 \int|\nabla^2u|^2={}&\int|\nabla^*\nabla u|^2
 -\int\operatorname{Ric}_{ij}\langle\nabla_i u,\nabla_j u\rangle\\
 &+\sum_{ij}\int\langle\mathscr F_{ij}\nabla_j u,\nabla_i u\rangle
 +\frac12\sum_{ij}\int|\mathscr F_{ij}u|^2.
\end{split}                                                \tag{4}
\]

Real parts of Hermitian products are understood. These formulas hold on
each closed metric; they contain no choice of coordinates or gauge.
Apply Holder and (3) to both curvature-gradient terms in (4). With
\(H=\|\nabla^2u\|_2\), their sum in absolute value is at most
\(4K(\|\operatorname{Ric}\|_2+\|\mathscr F\|_2)H\).
Young's inequality proves

\[
 \boxed{\quad
 \|\nabla^2u\|_2^2
 \le2\|\nabla^*\nabla u\|_2^2
       +32K^2\|\operatorname{Ric}\|_2^2
       +33K^2\|\mathscr F\|_2^2.\quad}                     \tag{5}
\]

Thus even a Ricci lower bound is unnecessary once the section is
bounded. The issue is to produce such a bounded spinor without losing
the monopole near-equality estimates.

## 3. The modified weight has a controlled scalar cost

Define the continuous positive functions

\[
 Q=\max(q,3),\qquad
 f_0=\max\left(\sqrt Q,\frac{(-s)_+}{4}\right).             \tag{6}
\]

Choose smooth majorants \(f_j\ge f_0\) converging uniformly to f_0
on the fixed compact metric, and solve

\[
 D_A\Phi=0,\qquad -iF_A^+=f_j\sigma(\Phi),\qquad
 \psi=2\sqrt2\sigma(\Phi),\quad \rho=|\Phi|^2=|\psi|,
 \quad u=3\rho/2.                                         \tag{7}
\]

Existence for each f_j is the standard conformal rescaling of an actual
monopole, as in [LeBrun, Lemma 3.7](https://arxiv.org/abs/math/0611450).
At a maximum of rho the spinor Weitzenbock equation gives
\(f_j\rho\le-s\), unless the spinor vanishes. Since
\(f_j\ge(-s)_+/4\),

\[
                 0\le\rho\le4,\qquad 0\le u\le6.          \tag{8}
\]

There are two elementary pointwise cost bounds:

\[
 0\le Q^2-q_+^2\le9e^2,\qquad
 0\le f_0^2-Q\le\frac9{16}e^2.                            \tag{9}
\]

For the first, the difference vanishes when q>=3; otherwise
\(s>-3\), hence e>1, and the difference is at most nine.
For the second, a nonzero difference requires
\((-s)_+>4\sqrt Q\ge4\sqrt3>6\). On that set
\((-s)_+\le3|s+4|\), and
\(f_0^2-Q\le(-s)_+^2/16\). This proves (9).

These estimates charge only scalar squared error. They do not require
the weight's fourth power to have a uniformly bounded integral.

All o(1) terms below refer to j tending to infinity with g and a fixed.
The spinor bound (8) is exact for every j. Uniform convergence of the
smooth majorants makes every stated integrated approximation error
arbitrarily small, without any convergence assumption on the solutions.

## 4. Preserve the near-equality argument using ideal moments

Use the four nonnegative defects from the self-contained monopole input:

\[
\begin{aligned}
 D_{\rm amp}&=2\int|d\rho|^2,\\
 D_{\rm quad}&=\int(4\rho|\nabla_A\Phi|^2-|\nabla\psi|^2),\\
 D_{\rm H}&=\int(|d\psi|^2+|d^*\psi|^2),\\
 D_{\rm eig}&=2\int(\langle W^+\psi,\psi\rangle
                              +\sqrt{2/3}|W^+|\rho^2),
 \qquad D_0=D_{\rm amp}+D_{\rm quad}+D_{\rm H}+D_{\rm eig}.
\end{aligned}
\]

The exact Weitzenbock subtraction is valid even when q changes sign:

\[
 \frac{27}{8}D_0=\int(qu^2-f_j u^3).                       \tag{10}
\]

Form the ideal moments using Q, while retaining the solution for f_j:

\[
 C=\int Qu^2,\quad Z=\int\sqrt Q\,u^3,\quad
 \mathcal E_Q=\int Q^2,\quad P=C-Z.
\]

Because \(Q\ge q\) and \(f_j\ge\sqrt Q\),

\[
 P=\frac{27}{8}D_0+
           \int(Q-q)u^2+\int(f_j-\sqrt Q)u^3\ge\frac{27}{8}D_0.
                                                               \tag{11}
\]

The actual curvature moment is different:

\[
 C_{\rm act}=\int f_j^2u^2
       =18\|F_A^+\|_2^2\ge72\pi^2p,
\]

but its difference from C is controlled by (8)--(9):

\[
 0\le C_{\rm act}-C
       \le\frac{81}{4}\int e^2+o(1).                     \tag{12}
\]

Holder gives \(C\le\mathcal E_Q^{1/3}Z^{2/3}\), and P>=0 gives
Z<=C, hence \(C\le\mathcal E_Q\). Combining this with (9) and (12),

\[
 0\le\mathcal E_Q-C\le
 S+o(1),\qquad S:=\Delta_++\frac{117}{4}\int e^2.           \tag{13}
\]

No topological lower bound was applied to the ideal moment without
accounting for (12).

The usual one-weight Holder algebra now applies to C,Z and \(\mathcal E_Q\).
If \(\theta=(Z/\mathcal E_Q)^{1/3}\in(0,1]\) and
\(H=\mathcal E_Q^{1/3}Z^{2/3}-C\), then

\[
 \mathcal E_Q-C=H+\frac{1+\theta}{\theta^2}(P+H)\ge2P.
\]

The amplitude-moment calculation, with probability measure
\(Q^2d\mu/\mathcal E_Q\), similarly gives
\(\int Q(u-\sqrt Q)^2\le\mathcal E_Q-C\). Therefore

\[
 D_0\le4S/27+o(1),\qquad
 \int Q(u-\sqrt Q)^2\le S+o(1),                           \tag{14}
\]
\[
 \|d\rho\|_2^2,\ \|d\psi\|_2^2\le2S/27+o(1).          \tag{15}
\]

This is the substantive replacement for the optimally weighted argument.
Directly inserting f_j into a bound involving \(\int f_j^4\) would
lose the critical L2 control. Equations (11)--(13) avoid that loss.

## 5. Approximate the calibrated Weyl orbit

Every tensor in \(\mathcal O_0\) has norm \(1/(2\sqrt6)\).
The reverse triangle inequality and \(e^2\le4|E|^2\) imply

\[
 \int(q-9/2)^2\le2\int e^2+12\int F\le12\mathcal C.
                                                               \tag{16}
\]

Clipping below three does not increase distance from 9/2. Since Q>=3,
(14) therefore yields

\[
 \|\rho-\sqrt2\|_2^2
 \le\frac8{27}S+\frac2{27}\int(Q-9/2)^2+o(1).             \tag{17}
\]

Let Pi be a measurable projection onto a lowest eigenvector of W+.
Then \(A_0(\Pi)=I/12-\Pi/4\) is a nearest point in \(\mathcal O_0\),
so \(|W^+-A_0(\Pi)|^2=F\). On \(U=\{F\le1/256\}\),
ordered-eigenvalue comparison with the target triple gives
\(\lambda_2-\lambda_1\ge1/4-2\sqrt F\ge1/8\).
The nonnegative spectral defect and (14) show

\[
 \int_U|(I-\Pi)\psi|^2\le16S/27+o(1).
\]

On the complement use \(\rho\le4\) and
\(\operatorname{Vol}(M\setminus U)\le256\int F\). Thus, for
\(y=(I-\Pi)\psi\),

\[
 \int|y|^2\le16S/27+4096\int F+o(1).                     \tag{18}
\]

Define the same smooth polynomial model as in round three,

\[
 A_\psi=\rho^2I/24-\psi\otimes\psi/8,\qquad R=W^+-A_\psi.
\]

The exact rank-one calculation gives
\(|A_\psi-A_0(\Pi)|^2\le\rho^2|y|^2/16+(\rho^2-2)^2/48\).
Since \(\rho\le4\) and \((4+\sqrt2)^2<36\), (17)--(18) imply

\[
 \|R\|_2^2
 \le\frac{44}{27}S+8194\int F
                   +\frac19\int(Q-9/2)^2+o(1)
 \le2\Delta_++8500\mathcal C+o(1).                        \tag{19}
\]

Here \(S\le\Delta_++117\mathcal C\). The large final numerical
coefficient is only a convenient universal bound.

## 6. Close the intrinsic estimate without pointwise curvature control

The elementary estimates

\[
 \int|W^+|^2\le2\int F+V/12,\quad
 \int|\operatorname{Ric}|^2\le2\int|E|^2+8V,\quad
 \int s^2\le8\int|E|^2+32V
\]

give L2 curvature budgets from \(\mathcal C\). Also, (9) and (16)
give \(\int f_j^2\le C(V+\mathcal C)+o(1)\).
Equation (7) and the determinant Chern--Weil identity imply

\[
 \|F_A\|_2^2
 =2\|F_A^+\|_2^2-4\pi^2a^2
 \le4\int f_j^2+4\pi^2(-a^2)_+.
\]

The curvature \(\mathscr F_A\) of the positive-spinor connection
contains only W+, scalar curvature, trace-free Ricci and determinant
curvature; the W-minus block acts trivially on positive spinors. Hence

\[
 \int|\mathscr F_A|^2\le C(V+\mathcal C+(-a^2)_+)+o(1).
                                                               \tag{20}
\]

The rough-Laplacian equation
\(4\nabla_A^*\nabla_A\Phi+(s+f_j\rho)\Phi=0\) and rho<=4 give

\[
 \int|\nabla_A^*\nabla_A\Phi|^2
 \le\frac12\int s^2+8\int f_j^2\le C(V+\mathcal C)+o(1).
\]

Apply (3) and (5), then differentiate the degree-four parallel polynomial
\(\Phi\mapsto A_\psi\). This proves

\[
 \int\left(|\nabla_A^2\Phi|^2+|\nabla_A\Phi|^4
                           +|\nabla^2A_\psi|^2\right)
 \le C(V+\mathcal C+(-a^2)_+)+o(1).                        \tag{21}
\]

Every term scales extensively before division by V. No normalized
Holder step has introduced an additional volume factor.

Let \(J_\psi=\operatorname{div}W(A_\psi)\), with the four-tensor
and three-index norm conventions of the local monopole input. Covariant
Bianchi and integration by parts give, for every smooth test tensor T,

\[
 \left|\int\langle J_\psi,T\rangle\right|
 \le C(\|E\|_2+\|R\|_2)\|\nabla T\|_2.
\]

Choose \(T=J_\psi\). Since
\(\|\nabla J_\psi\|_2\le C\|\nabla^2A_\psi\|_2\), (19)--(21)
give

\[
 \fint|J_\psi|^2\le C\sqrt\kappa\sqrt{1+\kappa+B_a}+o(1).
                                                               \tag{22}
\]

The exact weighted Hodge identity, derived in Section 8 of the local
input note, is

\[
\begin{split}
 \int|J_\psi|^2={}&-\frac1{64}\int\rho^2B_\psi
 +\frac1{16}\int\rho^2|d\psi|^2
 -\frac5{96}\int\rho^2|d\rho|^2\\
 &+\frac18\int\rho\langle\iota_{\nabla\rho}\psi,*d\psi\rangle,
 \quad B_\psi=(s/3)\rho^2-2\langle W^+\psi,\psi\rangle.
\end{split}
\]

Its curvature term is

\[
 -\rho^2B_\psi/64=-s\rho^4/192-\rho^6/384
                           +\rho^2\langle R\psi,\psi\rangle/32.
\]

At \(s=-4,\rho=\sqrt2,R=0\) it equals 1/16. The scalar error is
bounded by \(C\fint|e|\), because rho is bounded. Equations
(15), (17), and (19) control the other errors, so

\[
 \fint|J_\psi|^2\ge1/16-C(\sqrt\kappa+\kappa)+o(1).        \tag{23}
\]

Let the smooth-weight errors tend to zero. For sufficiently small
universal \(\kappa_0>0\), (23) is at least 1/32 when
\(\kappa\le\kappa_0\). Equation (22) then gives
\(\kappa(1+\kappa+B_a)\ge c_1>0\), hence
\((1+B_a)\kappa\ge c_1/2\) after taking \(\kappa_0\le1\).
For larger kappa, (2) is automatic after decreasing c. This proves
Theorem 1.

## 7. Transfer from integral Ricci error and topology

The result has a family consequence with no pointwise hypotheses.
Put

\[
 T=2\chi+3\tau,\qquad
 r(g)=\fint|\operatorname{Ric}+g|^2,
 \qquad d_T=(T/A-2/3)_+.
\]

Assume an actual monopole class has been selected with

\[
 p=(a^+)^2\ge A>0,\qquad a^2\ge-C_AA,
 \qquad C_A\ge0.                                         \tag{24}
\]

**Theorem 2.** With c from Theorem 1,

\[
 \boxed{\quad
 r(g)+d_T\ge
 \min\left\{1,\frac{c}{1215(1+5C_A/(4\pi^2))}\right\}>0.
 \quad}                                                  \tag{25}
\]

Here is the full algebraic passage, including scalar-positive regions.
Write \(\alpha=\sqrt{2/3}|W^+|\), \(w=\lambda_{\min}(W^+)\),
\(t=s+8\sqrt6|W^+|\),

\[
 b=2s/3+2w,\qquad
 G=(2s/3-2\alpha)^2-b_-^2\ge0,
 \qquad \Phi_*=|E|^2+e^2+t^2+G.
\]

The signed definition of G is needed where scalar curvature is positive.
It is nonnegative since \(b\ge2s/3-2\alpha\). The pointwise identity

\[
 t^2+18G=216(s^2/24+2|W^+|^2)-18b_-^2
\]

and \(\int b_-^2\ge32\pi^2A\), together with Chern--Weil,
give

\[
 \int\Phi_*\le109\int|E|^2+864\pi^2A d_T.                 \tag{26}
\]

For clarity, if \(P=\int|\operatorname{Ric}^{\circ}|^2\), then
\(\int(t^2+18G)\le108P+864\pi^2A d_T\), and
\(\int|E|^2=P+\frac14\int e^2\). These two statements prove (26).

One also has the global pointwise comparison

\[
                         F\le e^2+t^2+G.                 \tag{27}
\]

To check it, set z=w+alpha, so \(0\le z\le\alpha\) and
\(F=\frac32(\alpha-1/6)^2+z/2\), with
\(\alpha=(t-e+4)/24\). If s<=-3, then b<0 and G>=8z,
giving \(F\le(t^2+e^2)/192+G/16\). If s>-3, then e>1;
use \(4-e\le3e^2\), \(t\le(t^2+1)/2\), and z<=alpha to obtain
\(F\le(t^2+5e^2)/64\). Both imply (27).

The completed square

\[
 27(s^2/24+2|W^+|^2)-q^2=t^2/8
\]

also yields
\(\Delta_+\le(27/2)\int|E|^2+108\pi^2A d_T\).
Combining with (26)--(27),

\[
 \kappa\le\frac{245}{2}r+972\pi^2\frac AVd_T.             \tag{28}
\]

The scalar monopole estimate and \(s=-4+e\) give

\[
 32\pi^2A\le\int s_-^2\le\int s^2
       \le32V+8\int|E|^2,
 \qquad \frac AV\le\frac{4+r}{4\pi^2}.                   \tag{29}
\]

For r<=1 this bounds \(\kappa\le1215(r+d_T)\) and
\(B_a\le5C_A/(4\pi^2)\). Apply Theorem 1. If r>1 the other branch
of (25) is immediate.

The alternative square hypothesis \(a^2\ge T-C_AA\) also suffices,
with 1/4 replacing 1 in the minimum in (25). Indeed, when r<=1/4,
Chern--Weil and \(\|e\|_2\le2\sqrt{rV}\) imply

\[
 4\pi^2T\ge\frac1{24}(4-2\sqrt r)^2V-\frac r2V
                 \ge V/4>0.                             \tag{30}
\]

Then the alternative hypothesis implies (24); for r>1/4 the claim is
automatic. In particular the blow-up classes with \(a^2=T\), and the
actual full-sign connected-sum classes with \(a^2\ge T\), have a
universal constant with C_A=0. Their monopole-existence and projection
hypotheses remain exactly those stated in the local round-three family
notes; numerical topology alone does not supply them.

## 8. A scale-invariant curvature-energy formulation

For any metric define

\[
 \mathfrak r_-(g)=\inf_{\lambda>0}
 \frac{\int|\operatorname{Ric}_g+\lambda g|_g^2}
                         {\lambda^2V_g}.                 \tag{31}
\]

This quantity is invariant under constant rescaling. Apply Theorem 2
to \(\lambda g\): middle-dimensional harmonic projection is unchanged,
and its normalized Ricci error equals the integrand ratio in (31).
Therefore every family with the stated metricwise class selection obeys

\[
 \mathfrak r_-(g)+d_T\ge c(C_A)>0.     \tag{32}
\]

For the alternative class-square condition \(a^2\ge T-C_AA\), retain
the constant \(\min\{1/4,c/[1215(1+5C_A/(4\pi^2))]\}\) from Section 7
in (32); taking the scale infimum does not change that branch.

There is an explicit intrinsic expression. Put
\(S=\int s\), \(R_2=\int|\operatorname{Ric}|^2\), and
\(\bar s=S/V\). If S<0, the minimizing parameter is
\(\lambda_*=-R_2/S>0\), and

\[
 \boxed{\quad
 \mathfrak r_-(g)=4-\frac{S^2}{VR_2}
 =\frac{4\int|\operatorname{Ric}^{\circ}|^2
                      +\int(s-\bar s)^2}{\int|\operatorname{Ric}|^2}.
 \quad}                                                  \tag{33}
\]

If S>=0 the infimum is four. Thus (32) is a gap for the fraction of
Ricci energy coming from trace-free Ricci and scalar variation, in a
topological band around T/A=2/3. It rules out concentration-based
attempts to make this integral error vanish inside that band; it does
not merely exclude uniform pointwise pinching.

For example, in the blow-up family with its verified actual monopoles,

\[
 \mathfrak r_-(g)+\left(\frac13-\frac{k}{c_1^2(X)}\right)_+
                    \ge c_*>0
\]

with one constant for the family. The connected-sum version replaces k
by the topological quantity D specified in the actual full-sign setting.

## Verification and limits

`round4_rigidity_check.py` checks the truncation inequalities on their
declared branches, the ideal-moment factorization, Hessian absorption,
global orbit-distance comparison, family constants, and the exact
optimization in (33). They are algebra checks, not a replacement for
the monopole existence input or the integration-by-parts proofs.

The main change from round three is the bounded auxiliary solution for
a carefully modified weight, together with the explicit correction from
actual to ideal curvature moments. No compactness, smoothing theorem,
or pointwise Ricci assumption is used. The argument and all computations
remain in the isolated local worktree; no live assets were changed.
