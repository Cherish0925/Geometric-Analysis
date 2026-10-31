# 第二卷：首项稳定性、移动核心与无规范延拓

Research snapshot: 0b1490791be560203b86a7d9834dcdc3cbc83b41.

I52、X09、I53全文。阅读顺序展示从指定规范切片到实际移动中心，再到无规范C0邻域结论。X09否定固定基底精确规范的自动供给；它不否定系数4，也不是更低能量构造。

Read 00_READ_FIRST.md for superseded statements. Each source below is complete and byte-preserved. Original local links remain relative to their source; locate other texts using 10_source_map_and_history.md. Formula numbers restart in each source.


---

## Source 1: 20260927_endpoint_covariance_and_surgery_limits.md

Original path: `continuation/20260927_endpoint_covariance_and_surgery_limits.md`

SHA-256: `d6d56c3c918a60b6a59a9886dc7c7f9c5f00b68a7b2a087ab0ca8d1e8cf2b89d`

BEGIN COMPLETE SOURCE

# Weak endpoint covariance and first-order stability of shrinking surgery

27 September 2026. Continuation of `e75105d`, not an export package.
The inputs and curvature conventions are those of
[I40/I41](20260927_conformal_separation_and_zero_end.md) and
[I51](20260927_constant_weight_and_global_fit.md).

The main construction-side conclusion is Theorem 9: on a suitably
chosen complex-hyperbolic shrinking-surgery recovery sequence, every
vanishing-amplitude perturbation in either of two specified TT or
Bianchi slices has first-order coefficient at least four. No rate
relative to \(h\), derivative bound, Sobolev constant, or competitive
endpoint energy is assumed. The proof retains the classical positive
Einstein operator on the exterior and charges cutoff errors only to
the surgery budget. Its nonlinear lower bound also identifies the
equality condition inside these slices. Sections 3--4 derive this
from the actual construction; Theorem 7 records the weaker estimate
which does not use the exterior gap.

The endpoint calculation in Sections 1--2 separately identifies the next
derivative controls and measures the phase curvature they still miss.
Neither the unrestricted weak zero-end gap nor the all-metric optimal
coefficient is proved here.

## 1. The weighted second derivative of the determinant field

Work with the same actual constant-weight solution as I51, with scalar
curvature minus four and class square at least \(T_+\). Throughout this
section all integral norms are normalized by \(V\). Write

\[
 \rho=|\Phi|^2\le2,\quad \Pi=\nabla_A\Phi,\quad H=\nabla_A\Pi,
 \quad \zeta=\langle\Phi,\Pi\rangle,\quad\gamma=\operatorname{Im}\zeta,
\]
\[
 \rho_*=4/3,\quad m_*=128/81,\quad
 \tau=t_\Phi,\quad m=|\tau|^2,\quad
 S=m_*+2\rho^2|\Pi|^2,\quad w=\rho^4/S,
 \quad \eta=r+D_\beta/V+\beta^{-2}\le1.
\]

The real ASD forms are \(f=-iF_A^-\) and \(Q=-iq_-(\tau)\), with

\[
 \rho^2\Delta_Hf+\rho^3f=-2Q+R,\qquad
 |R|\le C(\rho^3|\operatorname{Ric}^{\circ}|
                       +\rho^{3/2}|\zeta||\Pi|),\qquad |Q|^2=m^2/8.
 \tag{1.1}
\]

We use the following already proved, same-solution estimates from I51
Section 2.2; no identification with an earlier variable-weight solution
is made:

\[
 \fint\frac{(S-2m_*)^2}{S}\le C\sqrt\eta,\qquad
 K=-\frac{4m_*}{\rho_*^6}\frac{\rho^3Q}{S},\qquad
 \|K\|_\infty\le C,\qquad \fint|f-K|^2\le C\sqrt\eta.
 \tag{1.2}
\]

Also \(m\le S\), \(S\ge m_*>0\),

\[
 \fint(|\rho-\rho_*|^2+|\zeta|^2+|\operatorname{Ric}^{\circ}|^2)
 \le C\eta,\qquad
 \fint(|\Pi|^4+|H|^2+|\nabla\tau|^2)\le C.
 \tag{1.3}
\]

**Lemma 1.** Under these hypotheses,

\[
 \boxed{\fint w\{ |\Delta_Hf|^2+|\Delta\rho|^2\}\le C\sqrt\eta.}
 \tag{1.4}
\]

**Proof.** Put \(\lambda=4m_*/\rho_*^6\). Equation (1.1) gives

\[
 \rho^2\Delta_Hf=-\rho^3(f-K)
                 -(2-\lambda\rho^6/S)Q+R.
\]

Divide its squared norm by \(S\). The first term is controlled by (1.2).
For the second use

\[
 2-\lambda\rho^6/S
 =2(S-2m_*)/S+\lambda(\rho_*^6-\rho^6)/S,
\]

and \(m\le S\): its contribution is at most

\[
 C\frac{(S-2m_*)^2}{S}+C|\rho-\rho_*|^2.
\]

Finally \( |R|^2/S\le C(|\operatorname{Ric}^{\circ}|^2+|\zeta|^2)\),
because \(\rho^2|\Pi|^2/S\le1/2\). This proves the first bound.
The scalar equation is

\[
 \Delta\rho=-2|\Pi|^2+2\rho-\rho^2,
 \qquad
 \rho^2\Delta\rho=-(S-2m_*)+(2\rho^3-\rho^4-m_*).
\]

The last polynomial vanishes at \(\rho_*\). Squaring, dividing by \(S\),
and using (1.2)--(1.3) proves the second bound. QED.

This is a consequence of the existing saturation identities, not an
independent endpoint exclusion. In particular \(w\) is not bounded below
on the entire manifold.

## 2. A precise remaining current--Hessian correlation

The current is coclosed: \(\delta\gamma=0\). This follows by taking the
imaginary part of the divergence of \(\langle\Phi,\nabla_A\Phi\rangle\):
the rough Laplacian of \(\Phi\) is a real scalar multiple of \(\Phi\).
Since \(\delta f=-\gamma\), \(df=*\gamma\),

\[
 \Delta_H f=-2(d\gamma)^-.
 \tag{2.1}
\]

For a real coclosed one-form and a smooth nonnegative weight, integration
by parts and \(d(\gamma\wedge d\gamma)=d\gamma\wedge d\gamma\) give
the exact formula

\[
\begin{aligned}
 \int w|\nabla\gamma|^2={}&2\int w|(d\gamma)^-|^2+
 \int w|\gamma|^2-\int w\operatorname{Ric}^{\circ}(\gamma,\gamma)\\
 &-\int\langle dw,\nabla_{\gamma^\sharp}\gamma\rangle
   -\int dw\wedge\gamma\wedge d\gamma.
\end{aligned}
 \tag{2.2}
\]

Only Ricci, not \(W^-\), enters this one-form identity. Differentiation of
the particular weight gives

\[
 dw=\frac{4\rho^3(m_*+\rho^2|\Pi|^2)}{S^2}d\rho
       -\frac{4\rho^6}{S^2}\operatorname{Re}\langle\Pi,H\rangle.
 \tag{2.3}
\]

Define the dimensionless nonnegative correlation

\[
 \mathcal B=\fint
       \frac{\rho^8|\Pi|^2|\zeta|^2}{S^3}|H|^2.
 \tag{2.4}
\]

**Proposition 2.** The same actual solution satisfies

\[
 \boxed{\fint \frac{\rho^4}{S}|\nabla\zeta|^2
                         \le C\sqrt\eta+C\mathcal B.}
 \tag{2.5}
\]

**Proof.** The first term in (2.2) is small by (1.4) and (2.1).
The Ricci term is \(O(\sqrt\eta V)\), by the small \(L^2\) Ricci
error and the bounded \(L^4\) norm of \(\gamma\). Young's inequality
absorbs half of the gradient term from the two weight errors. The
remaining cost is bounded by \(C\int |\gamma|^2|dw|^2/w\).
By (2.3), the part containing \(d\rho\) is at most \(C|d\rho|^2\),
using \( |\gamma|^2\le\rho|\Pi|^2\) and

\[
 \frac{|dw|^2}{w}
 \le C\frac{\rho^2}{S}|d\rho|^2
       +C\frac{\rho^8|\Pi|^2}{S^3}|H|^2.
 \tag{2.6}
\]

The other part is \(C V\mathcal B\). Thus (2.5) holds for
\(\operatorname{Im}\zeta\). The weighted scalar Bochner formula is

\[
\begin{aligned}
 \int w|\nabla^2\rho|^2={}&\int w(\Delta\rho)^2
  -\int w\operatorname{Ric}(d\rho,d\rho)\\
 &-\int(\Delta\rho)\langle dw,d\rho\rangle
  -\int\langle dw,\nabla_{\nabla\rho}d\rho\rangle.
\end{aligned}
 \tag{2.7}
\]

Use (1.4), then (2.6), \( |d\rho|\le2|\zeta|\), and the same
absorption. This proves the assertion for
\(\operatorname{Re}\zeta=d\rho/2\). At zeros, (2.6) is used through
its nonsingular displayed upper bound; all original weights are smooth.
Equivalently one may first use \(w+\epsilon\) and pass to the limit.
QED.

The coefficient of \( |H|^2\) in (2.4) is uniformly bounded and tends
to zero in measure, but this does not make \(\mathcal B\) small from a
mere \(L^2\) Hessian bound. Uniform integrability of \( |H|^2\) relative
to normalized volume would suffice; the strictly weaker needed condition
is the correlation \(\mathcal B\to0\) itself. Neither is added to the
original input. On each region \(\rho\ge c>0,S\le L\), (2.5) would
then give strong current-derivative control. It would still not, by
itself, give zero-end exclusion or control the torsion index on tiny cores.

The derivative which is missing from the classical argument should not
be misidentified. In [Armstrong's thesis, Sections 3.3.1--3.3.3](https://johnarmstrongmaths.com/publications/resources/thesis.pdf),
the full first torsion projection is combined with **pointwise constant
torsion length**, and then a second Ricci identity and opposite-chirality
Bianchi. The full first projection has already been proved with error in
[I41, Section 14](20260927_conformal_separation_and_zero_end.md).
Average length convergence is not the pointwise derivative condition.
The local actual cores in I50/I51 also prevent replacing this missing
step by a claim that small quadratic derivative energy kills their index.

### 2.1 The normalized Hopf form still contains a length derivative

Put \(j_\tau=\operatorname{Im}\langle\tau,\nabla_{3A}\tau\rangle\)
and \(a=\rho^3/S\). In the Clifford conventions of I41,

\[
 \delta Q=-\tfrac12 j_\tau+E_\tau,\qquad
 |E_\tau|^2=\tfrac14 m|D^-_{3A}\tau|^2.
 \tag{2.8}
\]

This follows directly by differentiating the quadratic Hopf map: at a
point with \(\tau=\sqrt m(1,0)\), write \(D\tau=(A,B)\). The error
one-form has components
\(\frac{\sqrt m}{2}(-\operatorname{Im}A,-\operatorname{Re}A,
-\operatorname{Im}B,\operatorname{Re}B)\).
Therefore the same \(K=-\lambda aQ\) as in (1.2) satisfies

\[
 \delta K=\frac{\lambda}{2}
       \{a j_\tau+2\iota_{\nabla a}Q\}-\lambda aE_\tau,
 \qquad \fint |aE_\tau|^2\le C\eta.
 \tag{2.9}
\]

For the last estimate insert I51's actual torsion Dirac equation,
\[
 |D^-_{3A}\tau|\le C|\zeta||\Pi|
                    +C\rho^{3/2}|W^+-W_0|,
\]
and use \(m\le2\rho^2|\Pi|^2\), \(S\ge m_*\). The coefficients of
\(|\zeta|^2\) and \(|W^+-W_0|^2\) after multiplication by \(a^2m\)
are uniformly bounded.

The first term of (2.9) is not automatically small. Even in the exact
principal projection with \(\rho\) constant, the two almost-complex
structures of opposite orientation give
\[
 j_\tau=-\tfrac12J_+dm,\qquad Q=-m\Omega_-/4,\qquad
 a j_\tau+2\iota_{\nabla a}Q
     =-\tfrac a2\bigl(J_+-\tfrac mS J_-\bigr)dm.
 \tag{2.10}
\]
At \(m=m_*\), \(S=2m_*\), the operator in parentheses has norm
bounded below by \(1/2\) on one-forms, by the reverse triangle
inequality. Thus normalization of the Hopf form does not cancel this
radial derivative. The actual projection errors must also be controlled;
(2.10) is not substituted as an exact identity for the approximate
sequence.

### 2.2 What the next differentiated equation must control

Weak control of the length derivative is available without resolving
\(\mathcal B\). The exact Clifford identity
\[
 \nu:=2\rho^2|\Pi|^2-m
       =2\rho|\zeta|^2+|c(\zeta)\Phi|^2
\]
gives \(\fint\nu\le C\eta\). Cauchy--Schwarz in (1.2), together
with the bounded average of \(S\), gives
\(\fint|m-m_*|\le C\eta^{1/4}\).
More precisely, for bounded Lipschitz \(F\), splitting into
\(S\le L\) and its complement, with a fixed sufficiently large \(L\),
gives
\[
 \fint |F(m)-F(m_*)|^2\le C_F\sqrt\eta. \tag{2.11}
\]
On the first set use (1.2) and \(\nu^2\le C_L\nu\); on the second
use boundedness of \(F\) and
\((S-2m_*)^2/S\ge cS\).
Consequently \(dF(m)\) is small as a distribution tested against
one-forms with bounded normalized \(L^2\) divergence, with bound
\(C_F\eta^{1/4}\). A cutoff depending only on \(\rho\) preserves
this conclusion by \(d\rho\) being small. A cutoff in \(S\) does
not follow at this strength: its derivative contains \(H\), and
the extra product is only \(L^1\)-small against bounded tests.

This weak statement does not control the derivative of the normalized
phase connection \(\theta_\tau=j_\tau/m\). The next Ricci interchange
in (2.10) contains \(d(J_+d\log m)\), not just \(dm\) in a negative
norm. The distinction can be measured on the already available local
actual simple-zero solutions. Their rescaled limit on a fixed mass
shell is
\[
 \tau=(\bar z_1,\bar z_2)/\ell,\qquad m=|x|^2/\ell^2,
 \qquad 0<m_1<m<m_2.
\]
Direct polar integration gives
\[
 \int|d\theta_\tau|^2=4\pi^2\log(m_2/m_1),\qquad
 \int\frac{|dm|^2}{m^2}|\nabla(\tau/|\tau|)|^2
       =12\pi^2\log(m_2/m_1). \tag{2.12}
\]
Indeed \(|d\theta_\tau|^2=4/r^4\),
\(|dm|^2/m^2=4/r^2\),
\(|\nabla(\tau/|\tau|)|^2=3/r^2\), and
\(\operatorname{Area}(S^3)=2\pi^2\).
For a radial cutoff decreasing from one to zero,
\[
 -\frac{1}{4\pi^2}\int d\chi\wedge\theta_\tau\wedge d\theta_\tau=1.
 \tag{2.13}
\]
The actual local corrections converge in the rescaled differentiable
norms on this nonzero shell, so (2.12) persists up to \(o(1)\);
the corresponding local flux is \(1+o(1)\).
Meanwhile the shell's phase \(L^2\) norm and bounded truncation's
negative derivative norm tend to zero. The weighted controls in
Sections 1--2 and the covariance contribution on each such shrinking
core can also tend to zero, as in I51's scale calculation.

Thus the phase curvature is a specific remaining critical quantity.
The calculation does not furnish a closed calibrated zero-end sequence:
it measures what the local equations permit before matching to the
exterior. A global cancellation would have to be proved using that
matching or further actual equations, not negative-norm convergence
alone.

## 3. The actual shrinking-surgery class, with arbitrary backgrounds

Let \(X\) be a closed complex-hyperbolic surface, \(A=c_1^2(X)>0\),
and fix

\[
 M=X\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3),
 \quad Q=k+4\ell=Ah,\quad C_Q=8\pi^2Q,
 \quad 0<h\le1/3.
\]

Here \(Q\) is the surgery number, unrelated to the ASD form in Section 1.
Retain the actual polarized scalar budget of this family, for \(X\)
and \(M\). On a metric \(g\) on \(X\) put

\[
 P_g=\int|\operatorname{Ric}^{\circ}|^2,\quad
 S_g=\int s^2,\quad R_g=P_g+S_g/4,
 \quad L_g=S_g-(\int s)^2/V_g.
\]

By *standard shrinking surgery* we mean inserting scalar-flat ASD Burns
pieces at blowups and conformally flat scalar-flat Schwarzschild necks
at the handles, with the unchanged exterior of the fixed smooth metric
\(g\). This is the classical construction used in
[LeBrun, Theorem 4.3](https://arxiv.org/html/math/0003068), applied in
normal-coordinate balls. It is not an arbitrary metric on \(M\).
The precise limits are

\[
 V_\epsilon\to V_g,\quad \int s_\epsilon\to\int s_g,
 \quad S_\epsilon\to S_g,\quad
 \int|W_\epsilon^+|^2\to\int|W_g^+|^2,
 \quad P_\epsilon\to P_g+C_Q,\quad R_\epsilon\to R_g+C_Q.
 \tag{3.1}
\]

The last two follow from Chern--Weil and \(T_+(M)=T_+(X)-Q\).
One can arrange uniformly bounded negative scalar curvature at fixed
\(g,k,\ell\). At cutting radius \(R\), the background normal-coordinate
cutoff has bounded curvature; an ALE scale \(a=o(R^2)\) makes the
model contribution \(O(a^2/R^4)\) bounded on the transition annulus.
The interiors are scalar-flat, and the changed volume tends to zero.
All constants may depend on this fixed background and these finite
surgery data. For a varying family the radii are subsequently chosen
diagonally, not by an unjustified uniform injectivity estimate.

The raw limiting relative Einstein defect is therefore

\[
 \mathcal F_Q(g)=4-\frac{(\int s_g)^2}{V_g(R_g+C_Q)}.
 \tag{3.2}
\]

### 3.1 Conformal minimization before and after surgery

Let \(\widehat g\) be the scalar-minus-four Yamabe representative of
\([g]\), and put \(\delta=S_g-S_{\widehat g}\ge0\). I41 gives
\(P_g=P_{\widehat g}+\delta/12\) and
\(R_g=R_{\widehat g}+\delta/3\). Define

\[
 \alpha_Q=\frac{4(P_{\widehat g}+C_Q)}{R_{\widehat g}+C_Q}.
\]

Direct substitution proves the exact identity

\[
 \boxed{\mathcal F_Q(g)-\alpha_Q
 =\frac{(1-\alpha_Q)\delta/3+L_g}{R_g+C_Q}.}
 \tag{3.3}
\]

If \(\alpha_Q<1\), Yamabe normalization minimizes this raw limiting
functional in the conformal class. If \(\alpha_Q\ge1\), use instead

\[
 \mathcal F_Q(g)=
 \frac{\alpha_Q(R_{\widehat g}+C_Q)+\delta/3+L_g}
      {R_{\widehat g}+C_Q+\delta/3}\ge1.
\]

Normalization **after** surgery needs a separate argument; (3.3) alone
does not identify its limit for a nonconstant-scalar background.

**Lemma 3 (negative Yamabe continuity for these shrinking surgeries).**
For fixed \(g,k,\ell\), the above construction can be chosen so that

\[
 Y(M,[g_\epsilon])\longrightarrow Y(X,[g])<0.
 \tag{3.4}
\]

**Proof.** Cut off the background Yamabe minimizer on the shrinking
coordinate balls. Their total Dirichlet capacity tends to zero, which
gives the upper bound on the limit in (3.4). In particular the surgery
Yamabe constants are bounded above by a fixed negative number for small
scales. Normalize their positive minimizers by \(\int u_\epsilon^4=1\).
The uniform bound \(s_\epsilon^-\le K\), the equation

\[
 6\Delta u_\epsilon+s_\epsilon u_\epsilon
                      =Y_\epsilon u_\epsilon^3,
\]

and the maximum principle give \(\|u_\epsilon\|_\infty^2
\le K/|Y_\epsilon|\le C\). The energy equation also bounds
\(\int|du_\epsilon|^2\): explicitly
\(Y_\epsilon\ge-KV_\epsilon^{1/2}\) and
\(6\int|du_\epsilon|^2\le KV_\epsilon^{1/2}\).
Choose a cutoff \(\chi_\epsilon\) which
vanishes on all changed cores, is one outside slightly larger unchanged
coordinate balls, and has \(\int|d\chi_\epsilon|^2\to0\).
Extend \(\chi_\epsilon u_\epsilon\) by zero to \(X\).
The removed \(L^4\) mass tends to zero by the volume and supremum bounds.
On expanding its Yamabe numerator, discard the removed nonnegative
gradient term. The removed negative scalar term tends to zero, and
the cutoff cross term is bounded by

\[
 C\|u_\epsilon\|_\infty
       \|d\chi_\epsilon\|_2\|du_\epsilon\|_2=o(1).
\]

Thus \(Y(X,[g])\le Y_\epsilon+o(1)\), proving the lower bound. QED.

Conformal invariance of Weyl energy and I41's exact conformal identity
now imply, for scalar-minus-four representatives of the outputs,

\[
 \widehat V_\epsilon\to V_{\widehat g},\qquad
 \widehat P_\epsilon\to P_{\widehat g}+C_Q,\qquad
 \widehat R_\epsilon\to R_{\widehat g}+C_Q,
 \qquad \mathcal E(\widehat g_\epsilon)\to\alpha_Q.
 \tag{3.5}
\]

### 3.2 Exact restricted infimum and the first-order penalty

**Proposition 4.** The infimum of the limiting defects in (3.2) and
(3.5), over all smooth backgrounds on \(X\), is

\[
 \boxed{\frac{4h}{1+h}.} \tag{3.6}
\]

This is an infimum in the specified construction class, not an infimum
over all metrics on the balanced \(M\).

**Proof.** On the Yamabe background the scalar budget and the opposite
chiral identity on \(X\), where \(T_-=A/3\), give

\[
 2\pi^2A\le V_{\widehat g}\le2\pi^2A+3P_{\widehat g}/4.
\]

Consequently

\[
 \alpha_Q\ge
 \frac{4(P_{\widehat g}+8\pi^2Ah)}
      {8\pi^2A(1+h)+4P_{\widehat g}}
 \ge\frac{4h}{1+h}. \tag{3.7}
\]

For the raw functional use the two cases after (3.3). The
complex-hyperbolic background gives equality in the limiting value.
For \(h<1/3\) the quantitative excess in (3.7) is

\[
 \alpha_Q-\frac{4h}{1+h}\ge
 \frac{4(1-3h)P_{\widehat g}}
 {(1+h)\{8\pi^2A(1+h)+4P_{\widehat g}\}}. \tag{3.8}
\]

There is a stronger exact way to see the classical content. Write
\(B_g=\int_X|W_g^-|^2\). The opposite Chern--Weil identity gives
\(R_g=8\pi^2A+4P_g-12B_g\), and hence

\[
 \boxed{\mathcal F_Q(g)-\frac{4h}{1+h}
 =\frac{4(1-3h)P_g+48hB_g+(1+h)L_g}
       {(1+h)(R_g+C_Q)}.} \tag{3.9a}
\]

Thus the finite-\(h\) lower bound does not even require the scalar
monopole budget. For \(0<h<1/3\), equality in this limit forces
\(P_g=B_g=L_g=0\). At \(h=1/3\) it only forces \(B_g=L_g=0\).
Eliminating \(P_g\) gives the equivalent form

\[
 \mathcal F_Q(g)-\frac{4h}{1+h}
 =\frac{(1-3h)(S_g-32\pi^2A)/3+16\int_X|W_g^-|^2+(1+h)L_g}
       {(1+h)(R_g+C_Q)}. \tag{3.9b}
\]

This is the same scalar--signature mechanism as I44, not a new
independent differential obstruction. The new use here keeps arbitrary
backgrounds and the post-surgery conformal limit explicit. QED.

For \(h_j\to0\), take all surgery errors to be \(o(Q_j)\), after fixing
each background. If the normalized outputs have defect \(O(h_j)\),
(3.8) forces \(P_{\widehat g_j}=O(Q_j)\), and

\[
 \boxed{\frac{\mathcal E(\widehat g_{j,\epsilon_j})}{h_j}
 =4+\frac{P_{\widehat g_j}}{2\pi^2Q_j}+o(1).} \tag{3.10}
\]

For competitive **raw** outputs, (3.3) additionally forces
\(\delta_j,L_{g_j}=O(Q_j)\), and

\[
 \frac{\mathcal E(g_{j,\epsilon_j})}{h_j}
 =4+\frac{P_{\widehat g_j}}{2\pi^2Q_j}
      +\frac{\delta_j}{24\pi^2Q_j}
      +\frac{L_{g_j}}{8\pi^2Q_j}+o(1). \tag{3.11}
\]

In this class, leading coefficient four is equivalent to the displayed
nonnegative penalties being \(o(Q_j)\). In (3.10) only the first penalty
remains. A claim that the two extra penalties survive normalization on
\(M\) would be incorrect. No uniform geometry across \(j\) was used:
the fixed-\(j\) limits (3.1) and (3.4) allow a diagonal with every stated
error \(o(Q_j)\).

## 4. What a perturbation of these metrics must change

Let \(g_j^0\) be a complex-hyperbolic shrinking-surgery sequence chosen
with scalar error \(\int(s+4)^2=o(Q_j)\). Let \(C_j\) contain all changed
cores and transition regions, and \(N_j=M_j\setminus C_j\) be the exact
complex-hyperbolic exterior. Then

\[
 \int_{C_j}|\operatorname{Ric}_{g_j^0}^{\circ}|^2
                    =8\pi^2Q_j+o(Q_j).
\]

Consider actual positive metrics \(g_j=g_j^0+\epsilon_j q_j\), with
\(\epsilon_j=O(\sqrt{h_j})\), and identify tensor \(L^2\) spaces by
pointwise isometries and the volume density. Assume uniform small metric
comparison, and the following explicit expansion, rather than an
unproved uniform differentiability on collapsing cores:

\[
 T_j=T_j^0+\epsilon_j L_jq_j+e_j,\quad
 \|e_j\|_{2,C_j}=o(\sqrt{Q_j}),
 \quad\epsilon_j^2\|L_jq_j\|_{2,C_j}^2=o(Q_j).
 \tag{4.1}
\]

Here \(T_j\) is the identified traceless Ricci tensor and \(L_j\) its
identified linearization. The analogous exterior expansion is assumed
with \(o(\sqrt{Q_j})\) remainder and
\(\epsilon_j\|L_jq_j\|_{2,N_j}=O(\sqrt{Q_j})\). The cross term on
the cores is \(o(Q_j)\) by Cauchy--Schwarz; the exterior has \(T_j^0=0\).
Therefore

\[
 P_{g_j}=8\pi^2Q_j+
       \epsilon_j^2\|L_jq_j\|_{2,N_j}^2+o(Q_j). \tag{4.2}
\]

If also \(\int(s_{g_j}+4)^2=o(Q_j)\), I51's exact scalar comparison
shows that Yamabe normalization changes \(P\) by \(o(Q_j)\).
Competitive normalized outputs on the balanced family then satisfy

\[
 \frac{\mathcal E(\widehat g_j)}{h_j}
 =4+\frac{\epsilon_j^2\|L_jq_j\|_{2,N_j}^2}{2\pi^2Q_j}+o(1).
 \tag{4.3}
\]

TT variations with uniformly controlled physical derivatives and
integrated core linearization energy \(O(Q_j)\) satisfy the smallness
in (4.1). The exterior first scalar variation vanishes because it is
Einstein and the variation is TT. Control in an expanding rescaled ALE
domain must be **integrated**; a rescaled \(C^2\) supremum alone does not
supply (4.1).

Conversely retain the \(o(\sqrt{Q_j})\) expansion remainder but not the
core energy smallness. Suppose the normalized sequence has
\(\mathcal E/h_j\le4-\sigma+o(1)\), for \(0<\sigma<4\), and retain
the scalar-error hypothesis. The balanced chiral and scalar budgets
give \(\widehat V_j=2\pi^2A_j+O(Q_j)\), whence

\[
 P_{g_j}\le 8\pi^2Q_j(1-\sigma/4)+o(Q_j).
\]

The reverse triangle inequality on \(C_j\) forces

\[
 \boxed{\liminf_j
 \frac{|\epsilon_j|\|L_jq_j\|_{2,C_j}}{\sqrt{Q_j}}
 \ge\sqrt{8\pi^2}\bigl(1-\sqrt{1-\sigma/4}\bigr)>0.} \tag{4.4}
\]

Thus at amplitude \(O(\sqrt h)\), a successful perturbation with a
controlled expansion needs core linearized energy of order at least
\(A\), not merely \(Ah\). This is a necessary escape scale within the
specified perturbative description. It neither constructs that escape
nor excludes a genuinely nonperturbative geometry. Arbitrarily changing
an isolated core while retaining cheap inverse-surgery collars is already
covered by I44's Weyl-only cap inequality, and is not counted again here.

There is also a necessary sign. The upper energy bound and (4.1) first
give \(|\epsilon_j|\|L_jq_j\|_{2,C_j}=O(\sqrt{Q_j})\), so squaring
the expansion is legitimate. Any proposed improvement as above must obey

\[
 -\epsilon_j\langle T_j^0,L_jq_j\rangle_{L^2(C_j)}
 \ge\pi^2\sigma Q_j
        +\tfrac12\epsilon_j^2\|L_jq_j\|_{2,C_j}^2+o(Q_j).
 \tag{4.5}
\]

Large core derivative energy alone is not enough: it must cancel the
existing core Ricci tensor with this sign. This statement uses the raw
tensor expansion and the scalar identity
\(P_{g_j}=P_{\widehat g_j}+o(Q_j)\). It does **not** infer tensor
closeness from that scalar energy identity.

### 4.1 A conformal tensor estimate without a Sobolev constant

The preceding distinction can be resolved under a stronger, explicit
scalar hypothesis. This auxiliary lemma does not require gauge theory.

**Lemma 5.** On a closed four-manifold let
\(\widehat g=e^{2f}g\) have scalar curvature \(-4\), and write
\(Z=\operatorname{Ric}^{\circ}_g\),
\(\widehat Z=\operatorname{Ric}^{\circ}_{\widehat g}\) as covariant
two-tensors. If \(\eta_f=\|f\|_\infty\) is sufficiently small, then

\[
 \boxed{\|\widehat Z-Z\|_{2,g}
 \le C\{\|s_g+4\|_{2,g}+\eta_f\|Z\|_{2,g}\}.} \tag{4.6}
\]

The constant is dimensional. No pointwise Ricci, diameter, or Sobolev
bound is used.

**Proof.** All norms in this proof are for \(g\), and
\(\Delta=d^*d\). Put
\[
 B=\widehat Z-Z=-2(\nabla^2f)_0+2(df\otimes df)_0,\quad
 T=\|B\|_2,\quad H=\|\nabla^2f\|_2,\quad
 D=\|\Delta f\|_2,\quad G=\|df\|_4^2,\quad a=\|s_g+4\|_2.
\]
Conformal invariance of the \(L^2\) norm of covariant two-tensors in
dimension four and \(\operatorname{div}Z=ds/4\) give the exact formula
\[
 T^2=P_{\widehat g}-P_g
       -\int(s_g+4)\Delta f-4\int Z(df,df). \tag{4.7}
\]
The negative constant-scalar representative is the Yamabe minimizer.
The conformal Chern--Weil identity therefore gives
\(P_{\widehat g}-P_g\le0\), and
\[
 T^2\le aD+4\sqrt{P_g}\,G. \tag{4.8}
\]
Integrating \(\operatorname{div}(f|df|^2\nabla f)\) proves
\(G\le\eta_f(2H+D)\le4\eta_f H\).
The apparent volume term in the scalar equation is unnecessary. Set
\(u=e^f\), \(v=u-1\), \(e=s_g+4\). The exact equation is
\[
 6\Delta v+4u(u+1)v=-eu.
\]
Testing with \(v\), and using the uniform upper and positive lower
bounds on \(u\), gives
\(\|v\|_2+\|dv\|_2\le Ca\).
In particular \(\|e^{2f}-1\|_2\le Ca\).
Trace splitting and the conformal scalar equation now give
\[
 H\le T/2+G+D/2,\qquad
 6\Delta f=-s_g-4e^{2f}+6|df|^2,\qquad
 D\le Ca+G.
\]
For sufficiently small \(\eta_f\), absorption yields
\[
 H\le C(T+a),\quad G\le C\eta_f(T+a),\quad
 D\le Ca+C\eta_f T.
\]
Substitute into (4.8) and solve the resulting quadratic inequality in
\(T\). This proves (4.6), and also
\[
 \|\nabla^2f\|_2+\|\Delta f\|_2\le C(a+\eta_f\sqrt{P_g}),
 \qquad \|f\|_2+\|df\|_2\le Ca.
\]
QED.

In particular, if
\[
 |s_g+4|_\infty=O(h),\quad P_g=O(Ah),\quad V_g=O(A),
\]
then the maximum principle in the Yamabe equation gives
\(\eta_f=O(h)\). Formula (4.6) implies
\[
 \|\widehat Z-Z\|_{2,g}=O(h\sqrt A)=o(\sqrt{Ah}). \tag{4.9}
\]
This implication includes the extra pointwise scalar hypothesis;
\(\int(s_g+4)^2=o(Ah)\) alone was not used to claim (4.9).

### 4.2 Nonzero diffuse TT variations at the first-order scale

The class in (4.2)--(4.3) is not restricted to a formal or zero
variation. On the same covering-and-surgery family there are actual
metrics, after Yamabe normalization, with
\[
 \boxed{\frac{\mathcal E(\widehat g_j)}{h_j}
       =4+\frac{\tau^2c_0}{2\pi^2}+o(1),\qquad c_0>0,} \tag{4.10}
\]
for each fixed real \(\tau\). Here is a construction and its quantifiers.

Reserve one small evenly covered chart in the fixed complex-hyperbolic
base, and all its lifts in \(X_j\), before choosing surgery points.
All finitely many surgery points can be chosen in the complement. There
are \(d_j=A_j/A_{\rm base}\) disjoint reserved charts.
Let \(b_{j,t}\) be the raw shrinking-surgery metric and
\(g^0_{j,t}=u_{j,t}^2b_{j,t}\) its scalar-minus-four representative.
For each fixed \(j\), Lemma 3, the uniform supremum estimate in its
proof, elliptic bootstrapping away from the punctures, and removability
of bounded solutions imply
\(u_{j,t}\to1\) smoothly on all reserved compact charts. The limit is
one by uniqueness of the negative constant-scalar representative.
Choose \(t_j\) so that the error on these finitely many charts is
\(o(h_j^2)\) in \(C^8\), simultaneously with all earlier energy errors.
This is a diagonal choice, not a uniform injectivity assertion.

On these charts \(g_j^0\) is exactly conformal to the
complex-hyperbolic metric, so it is Bach-flat. Let
\(\mathcal B_{\rm Bach}\) denote the Bach tensor and let \(a_j\) be
the sum of lifted compactly supported symmetric seed tensors. Set
\[
 q_j=D\mathcal B_{\rm Bach}|_{g_j^0}(a_j).
\]
This is a smooth global TT tensor, extended by zero: differentiate the
trace and divergence identities for the Bach tensor, noting that the
background Bach tensor vanishes on the support. These identities and
the transverse-traceless principal symbol are classical; see
[Gursky--Viaclovsky, Section 1.4 and Theorem 3.10](https://arxiv.org/pdf/1105.4648).
The order-six principal symbol of
\(D\operatorname{Ric}^{\circ}\circ D\mathcal B_{\rm Bach}\) is a
nonzero multiple of \(|\xi|^6\) on transverse trace-free symbol tensors.
For an explicit seed, take normal coordinates at a point, a nonzero
symmetric matrix \(H_0\) with \((H_0)_{1i}=0\),
\(\operatorname{tr}H_0=0\), and \(a=\chi(x)(x^1)^6H_0\), where
\(\chi\) is compactly supported and equals one near that point.
Every jet below order six vanishes there; the displayed principal
symbol makes the limiting linearized Ricci tensor nonzero.
Thus \(q_j\) has uniformly bounded physical \(C^2\) norm and
\[
 \int|L_jq_j|^2=(c_0+o(1))A_j,\qquad c_0>0.
\]

The positive metrics \(g_j=g_j^0+\tau\sqrt{h_j}\,q_j\) are unchanged
near every core. Their first scalar variation is
\(-\langle Z_j^0,q_j\rangle=o(h_j^2)\) on the support, and their
second variation is uniformly bounded. Hence
\(|s_{g_j}+4|_\infty=O(h_j)\). The Ricci Taylor remainder has
\(L^2\) norm \(O(h_j\sqrt{A_j})=o(\sqrt{Q_j})\), and
\[
 P_{g_j}=8\pi^2Q_j+\tau^2c_0Q_j+o(Q_j).
\]
Lemma 5 controls the final conformal tensor change by
\(o(\sqrt{Q_j})\); the exact scalar energy identity also gives
\(P_{\widehat g_j}-P_{g_j}=o(Q_j)\).
The balanced-family scalar and chiral budgets give
\(\widehat V_j=2\pi^2A_j+O(Q_j)\), proving (4.10).
Actual monopole supply persists by the same all-metric topological
input as before; no locally constructed spinor replaces that input.

This construction measures a genuine diffuse first-order payment. It
does not establish positivity in every reduced TT direction, exclude
core-correlated modes satisfying (4.5), or determine the unrestricted
optimal coefficient.

### 4.3 First-order stability on almost-critical recovery sequences

For suitably chosen recovery metrics the perturbative exclusion is
stronger than the core norm threshold (4.4). It covers core-supported
directions as well, provided the full curvature expansion is valid at
the required scale.

Choose the normalized shrinking-surgery bases \(g_j^0\) so that
\[
 P_j^0=8\pi^2Q_j+o(Q_j),\quad V_j^0=O(A_j),\quad
 \operatorname{Vol}(C_j)=o(Q_j),\quad
 P_{N_j}^0=o(Q_j^2/A_j). \tag{4.11}
\]
These choices are compatible with Section 4.2. For each fixed \(j\),
first choose small exclusion balls about its finitely many surgery
centers, then shrink the gluing scales further. Lemma 3 and local
smooth convergence give the exterior bound; the uniform supremum bound
on the conformal factor gives the core volume bound.

Let \(\mathcal B_W=\operatorname{grad}\int|W|^2\), in the operator
Weyl convention used throughout the project. On the raw construction
this gradient vanishes on the unchanged Einstein exterior and on the
scalar-flat ASD or conformally flat donors. On each gluing annulus of
radius \(R_i\), the rescaled metric is \(C^4\)-close to Euclidean
with error \(\varepsilon_i=O(R_i^2+(a_i/R_i)^2)\).
This fourth-order assertion follows from the explicit donors:
the Burns potential \(r^2+a_i^2\log r^2\) and the Schwarzschild
metric \((1+a_i^2/r^2)^2g_{\rm Eucl}\) have
\[
 |\partial^k(g-g_{\rm Eucl})|\le C_k a_i^2r^{-2-k},
 \qquad 0\le k\le4
\]
on either relevant asymptotically flat chart. Fixed rescaled smooth
cutoffs preserve these bounds. A second-derivative gluing estimate
alone would not have justified the following Bach estimate.

Fourth-order locality now gives
\(\int_{\mathrm{annulus}_i}|\mathcal B_W|\le C\varepsilon_i\).
There are \(O(Q_j)\) annuli and their errors can tend uniformly to
zero. The covariant Bach gradient has conformal weight \(-2\);
its \(L^1\) norm in four dimensions is conformally invariant.
Therefore
\[
 \|\mathcal B_W(g_j^0)\|_1=o(Q_j),\qquad
 \|Z_j^0\|_1
 \le\sqrt{P_{C_j}^0\operatorname{Vol}(C_j)}
       +\sqrt{P_{N_j}^0V_j^0}=o(Q_j). \tag{4.12}
\]
From \(P=2\int|W|^2+S/12-16\pi^2\chi\) and \(s=-4\),
\[
 \operatorname{grad}P=2\mathcal B_W+\tfrac23 Z,\qquad
 \|\operatorname{grad}P(g_j^0)\|_1=o(Q_j). \tag{4.13}
\]

**Proposition 6.** Let \(q_j\) be smooth symmetric tensors with
\(\|q_j\|_\infty\le C\). Normalize the positive path
\(g_j^0+tq_j\) to scalar \(-4\), denoting it by \(\widehat g_j(t)\).
Take \(t_j=O(\sqrt{h_j})\). Identify the final traceless Ricci
tensors isometrically with the fixed \(L^2\) space at \(g_j^0\),
including the square root of the volume density, and write
\[
 \mathcal Z_j(t_j)=Z_j^0+t_j\dot{\mathcal Z}_j(0)+e_j. \tag{4.14}
\]
If \(\|e_j\|_2=o(\sqrt{Q_j})\) and the outputs are competitive,
\(\mathcal E(\widehat g_j(t_j))=O(h_j)\), then
\[
 P_{\widehat g_j(t_j)}
     =8\pi^2Q_j+t_j^2\|\dot{\mathcal Z}_j(0)\|_2^2+o(Q_j),
 \qquad \liminf_j\frac{\mathcal E(\widehat g_j(t_j))}{h_j}\ge4.
 \tag{4.15}
\]
No TT hypothesis is required for this conditional assertion.

**Proof.** The identification is essential. For initial velocity
\(v=\dot g\), \(H_0=g^{-1}v\), its derivative is
\[
 \dot{\mathcal Z}
   =\dot Z-\tfrac12(H_0Z+ZH_0)
                   +\tfrac14(\operatorname{tr}H_0)Z,\qquad
 2\langle Z,\dot{\mathcal Z}\rangle_{L^2}=P'(v). \tag{4.16}
\]
For a conformal velocity \(2\phi g\), the identification corrections
cancel in four dimensions, and \(P'(2\phi g)=0\) at constant scalar
curvature. Hence the normalized path derivative satisfies
\[
 2\langle Z_j^0,\dot{\mathcal Z}_j(0)\rangle
   =P'_{g_j^0}(q_j)=o(Q_j)
\]
by (4.13). The scalar and chiral budgets turn competitiveness into
\(P_{\widehat g_j(t_j)}=O(Q_j)\) and
\(\widehat V_j=2\pi^2A_j+O(Q_j)\).
The triangle inequality in (4.14) gives
\(|t_j|\|\dot{\mathcal Z}_j(0)\|_2=O(\sqrt{Q_j})\).
Squaring (4.14), with its stated remainder, proves (4.15). QED.

There is a quantitative converse that does not assume a small
remainder. Define \(e_j\) by the exact difference (4.14). If an actual
normalized path with the same bounded initial direction satisfies
\(\mathcal E/h_j\le4-\sigma+o(1)\), \(0<\sigma<4\), then
\[
 \boxed{\liminf_j\frac{\|e_j\|_2^2}{Q_j}
 \ge8\pi^2\left(1-\sqrt{1-\sigma/4}\right)^2.} \tag{4.17}
\]
Indeed (4.13) implies
\(\|Z_j^0+t_j\dot{\mathcal Z}_j(0)\|_2^2
\ge(8\pi^2+o(1))Q_j\), whereas the final squared norm is at most
\((8\pi^2(1-\sigma/4)+o(1))Q_j\). Apply the reverse triangle
inequality. This bound is a Hilbert-space consequence with an actual
geometric hypothesis; it does not construct such a path.

Thus on these recovery bases, simply arranging a large core
linearization cannot satisfy (4.5) within the small-remainder class.
A putative improvement must create the quantitatively nonnegligible
nonlinear curvature remainder (4.17), or use a different base geometry.
Neither possibility has been excluded.

### 4.4 Competitive energy supplies the missing Taylor control

The remainder hypothesis in Proposition 6 can be removed in a
substantially larger, explicitly gauged class. In this section all
derivatives and unmarked norms are for \(g_j^0\).

**Theorem 7 (small-amplitude TT competitors).** Let \(g_j^0\) be
the recovery sequence of (4.11)--(4.13). Let \(k_j\) be any smooth
symmetric tensors with
\[
 \operatorname{tr}_{g_j^0}k_j=0,\qquad
 \delta_{g_j^0}k_j=0,\qquad a_j=\|k_j\|_\infty\longrightarrow0.
\]
Suppose \(k_j\) is supported in \(U_j\), and put
\(K_j=\|\operatorname{Rm}(g_j^0)\|_{L^2(U_j)}\).
If
\[
 a_j^2 K_j=o(\sqrt{Q_j}),\qquad
 \mathcal E(\widehat{g_j^0+k_j})=O(h_j),
 \tag{4.18}
\]
where the hat denotes negative Yamabe normalization, then
\[
 \boxed{\liminf_j
     \frac{\mathcal E(\widehat{g_j^0+k_j})}{h_j}\ge4.} \tag{4.19}
\]
There are no assumed derivative bounds or Taylor remainders.
Globally \(K_j=O(\sqrt{A_j})\): for the full Riemann tensor norm,
\(\int|\operatorname{Rm}|^2=32\pi^2\chi+4P\), and
\(\chi(M_j)=O(A_j)\). Thus
\(a_j=o(h_j^{1/4})\) is sufficient.

**Proof.** We first record the geometry-independent tensor estimate
that supplies the second derivatives. On any closed manifold, for a
smooth tensor \(k\), put \(a=\|k\|_\infty\) and
\(H=\|\nabla^2k\|_2\). Integration by parts gives
\[
 \|\nabla k\|_4^2\le CaH. \tag{4.20}
\]
To see this, integrate the divergence of the vector field with
components \(|\nabla k|^2\langle k,\nabla_i k\rangle\), and bound
the resulting Hessian terms by
\(CaH\|\nabla k\|_4^2\).
For the Hessian estimate regard
\(\alpha=\nabla k\) as a one-form valued in \(E=S^2T^*M\).
The bundle-valued Weitzenbock identity gives
\[
 H^2=\|d^\nabla\alpha\|_2^2+
        \|\delta^\nabla\alpha\|_2^2
                -\int\langle\mathcal R\alpha,\alpha\rangle.
\]
Here \(d^\nabla\alpha=F_Ek\),
\(\delta^\nabla\alpha=\nabla^*\nabla k\), and
\(|F_E|+|\mathcal R|\le C|\operatorname{Rm}|\).
Consequently
\[
 H^2\le\|\nabla^*\nabla k\|_2^2+Ca^2K^2
            +CK\|\nabla k\|_4^2
       \le\|\nabla^*\nabla k\|_2^2+Ca^2K^2+CaKH.
 \tag{4.21}
\]
This classical identity is stated, for example, in
[Oh--Kim, Appendix 23](https://www.matrix-inst.org.au/wp_Matrix2016/wp-content/uploads/2023/07/OhKim.pdf).
No curvature derivative is taken. Curvature is only integrated where \(k\) or
its derivatives is supported, with no artificial boundary. Equations
(4.20)--(4.21) imply
\[
 H\le C\{\|\nabla^*\nabla k\|_2+aK\}.
\]
For an exactly TT tensor the principal part of
\(DZ_{g^0}(k)\) is one half of this rough Laplacian; every other
term is \(\operatorname{Rm}*k\). Therefore
\[
 H\le C\{\|DZ_{g^0}(k)\|_2+aK\}. \tag{4.22}
\]
Neither (4.20) nor (4.21) uses a Sobolev or injectivity constant.

For \(a\) sufficiently small, the connection-difference formula
for \(g=g^0+k\) gives exact Ricci and scalar Taylor remainders
bounded by
\[
 C\{aH+\|\nabla k\|_4^2+a^2K\}
 \le C(aH+a^2K). \tag{4.23}
\]
This follows by expanding the inverse metric once: the second-order
terms are bounded by
\(C(a|\nabla^2k|+|\nabla k|^2+a^2|\operatorname{Rm}|)\).
Here and below the constants are uniform under \(a\) small.
The first scalar variation in TT gauge is
\(-\langle Z^0,k\rangle\). With
\(b=\|s_g+4\|_{2,g}\) and \(\|Z^0\|_2=O(\sqrt Q)\),
\[
 b\le C(a\sqrt Q+aH+a^2K). \tag{4.24}
\]

The competitive energy is assumed for the final Yamabe metric, not
silently transferred to \(g\). The balanced-family scalar and chiral
budgets give \(P_{\widehat g}=O(Q)\). The exact conformal identity
and the negative Yamabe variational inequality give
\[
 0\le P_g-P_{\widehat g}
       =\frac{S_g-Y([g])^2}{12}\le\frac{b^2}{12}. \tag{4.25}
\]
For completeness, if \(I=\int s_g<0\), then
\(Y([g])^2\ge I^2/V_g\), and
\(S_g-I^2/V_g\le\int(s_g+4)^2\).
If \(I\ge0\), the latter integral is at least \(S_g\), which
also proves (4.25). The actual family supplies \(Y([g])<0\).
Thus \(\sqrt{P_g}\le C\sqrt Q+Cb\), without a bound on the
normalizing conformal factor.

Insert the nonlinear Ricci expansion into (4.22), use (4.23)--(4.25),
and absorb the terms \(CaH\). This gives
\[
 H\le C(\sqrt Q+aK),\qquad
 b+\|\operatorname{Rem}_Z\|_2
                  \le C(a\sqrt Q+a^2K). \tag{4.26}
\]
By (4.18), both terms on the right of the second inequality are
\(o(\sqrt Q)\). In particular \(P_g-P_{\widehat g}=o(Q)\).

It remains to preserve the metric and volume factors in the tensor
expansion. Let \(I_k\) be the norm-preserving identification used in
(4.16), and \(\dot{\mathcal Z}_0(k)\) its derivative. Smooth
pointwise matrix calculus, (4.23), and (4.26) give
\[
 \|I_k Z_g-Z^0-\dot{\mathcal Z}_0(k)\|_2
       \le C(a\sqrt Q+a^2K)=o(\sqrt Q).
 \tag{4.27}
\]
The extra terms are bounded by
\(Ca\|DZ(k)\|_2+Ca^2\|Z^0\|_2\) in addition to
(4.23), so no uncontrolled change of volume has been suppressed.
Since \(P_g=O(Q)\), the linearized tensor also has norm
\(O(\sqrt Q)\). Consequently
\[
 P_g=P_{g^0}+P'_{g^0}(k)
                 +\|\dot{\mathcal Z}_0(k)\|_2^2+o(Q)
        \ge8\pi^2Q+o(Q).
 \tag{4.28}
\]
Here \(|P'_{g^0}(k)|\le a\|\operatorname{grad}P(g^0)\|_1=o(Q)\).
Combine with (4.25)--(4.26) and
\(\widehat V=2\pi^2A+O(Q)\) to obtain (4.19). QED.

On the chosen surgery cores,
\(\|\operatorname{Rm}(g_j^0)\|_{L^2(C_j)}^2=O(Q_j)\):
the Weyl energy is the conformally invariant donor-and-annulus energy,
the Ricci energy is \(O(Q_j)\), and the scalar term is controlled by
the core volume. Thus every vanishing-amplitude core-supported TT
competitor satisfies (4.18), even with arbitrarily high derivatives.
For perturbations leaving the old cheap collars unchanged, I44's cap
argument already gives the exclusion; this special case is a
consistency check, not a new application. The broader assertion here
allows global TT changes with no collar derivative bound.

There is a related gauge formulation without a TT decomposition.

**Corollary 8 (constant-scalar Bianchi slice).** Suppose instead that
the actual endpoints \(g_j=g_j^0+k_j\) already satisfy
\[
 s_{g_j}=-4,\quad
 \beta_{g_j^0}k_j
    :=\delta_{g_j^0}k_j+\tfrac12d\operatorname{tr}_{g_j^0}k_j=0,
 \quad \|k_j\|_\infty=o(h_j^{1/4}),\quad
 \mathcal E(g_j)=O(h_j).
 \tag{4.29}
\]
Then \(\liminf\mathcal E(g_j)/h_j\ge4\).

**Proof.** Use \(F(g)=\operatorname{Ric}_g+g\).
In this gauge \(DF(k)\) has principal part
\(\frac12\nabla^*\nabla k\); the remaining terms are
\(\operatorname{Rm}*k+k\). Replace \(K\) in (4.22) by
\(\widetilde K=K+\sqrt{V_{g^0}}=O(\sqrt A)\).
At both endpoints \(F=Z\), of norm \(O(\sqrt Q)\).
The same connection-difference formula and absorption give
\[
 H\le C(\sqrt Q+a\widetilde K),\qquad
 \|\operatorname{Rem}_F\|_2
                  \le C(a\sqrt Q+a^2\widetilde K)=o(\sqrt Q).
\]
Finally use
\(\int|F|^2=P+\frac14\int(s+4)^2\).
This functional equals \(P\) at both endpoints and its first
derivative equals \(P'\) at \(g^0\). The identified expansion
therefore has exactly the sign argument in (4.28). QED.

These are actual, derivative-free small-amplitude assertions in the
specified gauges, not assertions that arbitrary nearby metrics admit
a uniformly controlled gauge change. The radius \(o(h^{1/4})\) is
sufficient; its sharpness is not proved. A successful sub-four
construction must lie outside these classes. The unrestricted
coefficient and classification of all near-minimizers remain open.

### 4.5 Using the actual exterior removes the shrinking amplitude rate

The loss \(a^2\sqrt A\) in Theorem 7 charges for the entire background
curvature. The chosen recovery sequence has more structure: outside
the surgery cores it is close to a complex-hyperbolic metric whose
full-tensor Einstein operator has a uniform positive gap. Retaining
that structure removes the \(h^{1/4}\) restriction.

**Theorem 9 (vanishing-amplitude stability).** The recovery sequence
in (4.11)--(4.13), on the established balanced family with
\(h_j\to0\) and \(U_j=1+h_j+O(h_j^2)\), can be chosen so that both
of the following hold:

- If \(k_j\) is exactly TT relative to \(g_j^0\),
  and \(\|k_j\|_\infty\to0\), then
  \(\liminf\mathcal E(\widehat{g_j^0+k_j})/h_j\ge4\).
- If \(k_j\) is exactly in the Bianchi gauge of (4.29),
  both endpoints have scalar curvature \(-4\),
  and \(\|k_j\|_\infty\to0\), the same lower bound holds.

No relation between the amplitude and \(h_j\), and no derivative
bound or competitive-energy premise, is assumed. The gauges remain
genuine hypotheses. More precisely, for \(a=\|k\|_\infty\le a_0\)
and \(x=\|\mathcal A_0(k)\|_2\), where \(\mathcal A_0\) is the
norm-preserving identified derivative defined below, there are uniform
positive constants \(c,C,a_0\) such that
\[
 \boxed{P_{\rm final}\ge P_0+DP_0[k]+c x^2-Ca^2Q.} \tag{4.29a}
\]
The bases are selected before the perturbations. In particular the
error from their near-stationarity is uniform for \(a\le a_0\).

**Proof: the geometric decomposition.** In each \(X_j\), choose
disjoint balls \(B(p_i,4R_i)\) about all surgery centers, with
\(N_j=k_j^{\rm surg}+2\ell_j\le Q_j\),
\(R_i\le r_0\), and \(\sum_i R_i^4=o(Q_j)\).
Here \(k_j^{\rm surg}\) is the blowup count, not the tensor.
Reserve the seed charts of Section 4.2 separately.
Choose the insertion scales much smaller than these radii. For each
fixed \(j\), the normalized metrics converge smoothly to the CH
background outside the punctures. To justify this for the normalized
metrics, Lemma 3 gives bounded positive Yamabe factors, their \(H^1\)
energies and convergence of the Yamabe constants. Local elliptic
compactness and removability at the finitely many points produce a
nonzero Yamabe minimizer on the original closed \(X_j\). No \(L^4\)
mass is lost at the points, by the supremum and volume bounds.
Uniqueness of the negative normalized representative identifies the
limit with the CH metric. The diagonal can therefore ensure
arbitrarily small \(C^2\) discrepancy on the complement of
\(\bigcup_i B(p_i,R_i/2)\), including all forthcoming cutoff annuli.
All comparisons here use the fixed CH coordinates; the exterior is
not falsely declared exactly CH after normalization.

Let \(C_j=\bigcup_i B(p_i,2R_i)\) denote the corresponding regions
after surgery, and \(N_j^{\rm ext}=M_j\setminus C_j\).
The core curvature budget is
\[
 \|\operatorname{Rm}_0\|_{L^2(C_j)}\le C\sqrt{Q_j}. \tag{4.30}
\]
Indeed the local Weyl integrals are conformally invariant and have
bounded cost per explicit donor; the annuli and CH balls add
\(O(N_j)+o(Q_j)\). The Ricci energy is bounded by \(P_j^0=O(Q_j)\)
and the scalar term by the core volume. The same argument applies to
slightly enlarged cores. The scalar curvature of the raw construction
has a uniform negative lower bound, so the Yamabe supremum estimate
keeps these normalized core volumes \(o(Q_j)\).

**The classical exterior estimate.** On every closed CH surface
normalized by \(\operatorname{Ric}=-g\), put
\(L_{\rm CH}=\nabla^*\nabla-2\mathring R\).
Koiso's identity and the CH curvature action give, for every symmetric
two-tensor \(v\), not only TT tensors,
\[
 \langle L_{\rm CH}v,v\rangle\ge\tfrac13\|v\|_2^2,\qquad
 \|v\|_{H^2}\le C\|L_{\rm CH}v\|_2. \tag{4.31}
\]
The constant is independent of the covering degree. See
[Wu, Section 3, Lemmas 3.2 and 3.6 and Proposition 3.7](https://arxiv.org/abs/1106.0511).
In these conventions the holomorphic sectional curvature is \(-2/3\);
the curvature-action eigenvalues on trace, Hermitian trace-free and
anti-Hermitian tensors are \(-1,-1/3,2/3\).
Koiso's formula has the corresponding positive zero-order coefficients
\(2,4/3,1/3\). The \(H^2\) bound follows by the integrated tensor
Weitzenbock formula and bounded parallel curvature. Thus (4.31)
does not infer a quantitative gap from qualitative local rigidity.

**Localization without a gauge projection.** Write \(a=\|k\|_\infty\),
\(H=\|\nabla^2k\|_2\), and
\(B_1=\|k\|_{H^1(N^{\rm ext})}\).
For the Bianchi case define, on all symmetric tensors,
\[
 \mathcal L_0^F v=\nabla_0^*\nabla_0v
          -2\mathring R_0v+Z_0\circ v+v\circ Z_0.
\]
For the TT case use
\(\mathcal L_0^Z v=\mathcal L_0^Fv+
\frac12\langle Z_0,v\rangle g_0\).
The original gauge condition gives respectively
\(\mathcal L_0^Fk=2DF_0(k)\) and
\(\mathcal L_0^Zk=2DZ_0(k)\).
Let \(L_0(k)\) denote the applicable derivative \(DF_0(k)\)
or \(DZ_0(k)\).

Splitting the bundle Weitzenbock identity (4.21) between core and
exterior, using (4.30) on the core and bounded curvature outside,
gives
\[
 H\le C\{\|L_0(k)\|_2+a\sqrt Q+B_1\}. \tag{4.32}
\]
For detail, the curvature-square term is at most
\(Ca^2Q+C\|k\|_{2,N^{\rm ext}}^2\).
The core curvature-gradient term is at most
\(C\sqrt Q\|\nabla k\|_4^2\le Ca\sqrt Q H\);
the exterior term is at most \(C B_1^2\).
The rough Laplacian is then replaced by \(\mathcal L_0k\);
its zero-order term is bounded by
\(Ca\sqrt Q+C\|k\|_{2,N^{\rm ext}}\).

Choose \(\chi=0\) on the inner balls, \(\chi=1\) outside the
slightly larger balls, with transitions only in the CH-close annuli.
Include every transition annulus in \(C_j\), so that \(\chi=1\)
on \(N_j^{\rm ext}\).
Then \(v=\chi k\) extends smoothly by zero to the complete covering
surface \(X_j\). The cutoff is not TT or in Bianchi gauge, and need
not be: (4.31) is an all-tensor estimate, and
\[
 \mathcal L_0(\chi k)=2\chi L_0(k)
                   +[\nabla_0^*\nabla_0,\chi]k. \tag{4.33}
\]
On its support, the small \(C^2\) metric discrepancy gives
\(\|(L_{\rm CH}-\mathcal L_0)v\|_2
\le C\epsilon_j\|v\|_{H^2}\), which is absorbed using (4.31).

The cutoff commutator has no hidden volume cost. Each annulus has
\(\int|\nabla^2\chi|^2=O(1)\), so
\(\|k\nabla^2\chi\|_2\le Ca\sqrt Q\).
For \(w=|d\chi|^2\), integration by parts gives
\[
 \int w|\nabla k|^2
 \le Ca\sqrt Q\,H+Ca^2Q. \tag{4.34}
\]
Indeed the Hessian term is bounded by
\(a\|w\|_2H\), with \(\|w\|_2=O(\sqrt Q)\).
The other term is absorbed by Young's inequality and
\(|dw|^2/w\le4|\nabla^2\chi|^2\).
Consequently, for any fixed \(\theta>0\),
\[
 \|d\chi\otimes\nabla k\|_2
                 \le\theta H+C_\theta a\sqrt Q.
\]
Equations (4.31)--(4.34), followed by absorption with \(\theta\)
small, prove the stronger graph estimate
\[
 \boxed{H+\|\chi k\|_{H^2(X_j,g_{\rm CH})}
                 +\||\operatorname{Rm}_0|\,|k|\|_2
       \le C\{\|L_0(k)\|_2+a\sqrt Q\}.} \tag{4.35}
\]
The last term is the full pointwise product, not just one favorable
curvature action. On the core it is at most \(Ca\sqrt Q\); outside
it is controlled by \(B_1\).

**The nonlinear conclusion.** The exact Taylor remainders now satisfy
\[
 \|\operatorname{Rem}\|_2
 \le C\{aH+\|\nabla k\|_4^2+
                       \||\operatorname{Rm}_0||k|^2\|_2\}
 \le Ca\{\|L_0(k)\|_2+a\sqrt Q\}. \tag{4.36}
\]
There is no \(a^2\sqrt A\) term.
For TT input, put \(b=\|s_{g^0+k}+4\|_{2,g^0+k}\).
Its linear term is \(-\langle Z_0,k\rangle\), so
\[
 b\le Ca\sqrt Q+
                  Ca\{\|DZ_0(k)\|_2+a\sqrt Q\}.
\]
There is a stronger closure than first assuming competitive energy.
Let \(\mathcal A_0(k)\) be the identified \(Z\)-derivative in the
TT case, and the identified \(F\)-derivative in the Bianchi case,
using (4.16); put \(x=\|\mathcal A_0(k)\|_2\).
The identification correction is at most \(Ca\sqrt Q\).
If \(e\) is the exact remainder in the raw identified tensor, (4.36)
and pointwise matrix calculus give
\[
 \|e\|_2\le Ca x+Ca^2\sqrt Q,\qquad
 b\le Ca(\sqrt Q+x). \tag{4.37}
\]
The second inequality is needed only for the TT/Yamabe case.
At the constant-scalar base,
\(2\langle Z_0,\mathcal A_0(k)\rangle=DP_0[k]\).
This also holds for \(F\), since its squared norm differs from
\(P\) by \(\frac14\int(s+4)^2\).
Expand the exact identified squared norm and drop \(\|e\|_2^2\).
In the TT case then subtract at most \(b^2/12\) using (4.25);
in the Bianchi case both endpoints already have \(F=Z\).
In either case,
\[
 P_{\rm final}
 \ge P_0+DP_0[k]+(1-Ca)x^2-Ca\sqrt Q\,x-Ca^2Q.
\]
Take \(a_0\) sufficiently small and complete the square in \(x\).
This proves (4.29a), with a positive part of \(x^2\) retained.
There was no assumption that \(x=O(\sqrt Q)\).

By (4.13), write
\(\|{\rm grad}P(g_j^0)\|_1=\epsilon_jQ_j\), \(\epsilon_j\to0\).
Then
\(P_{\rm final}/Q\ge 8\pi^2-Ca^2-o(1)\), uniformly for
\(a\le a_0\). To turn this into the relative defect, use the actual
family's chiral budget
\[
 R_{\rm final}-4P_{\rm final}\le8\pi^2A U,\qquad
 \mathcal E_{\rm final}=\frac{4P_{\rm final}}{R_{\rm final}}.
\]
The function \(P\mapsto4P/(4P+8\pi^2AU)\) is increasing. Consequently,
with \(d_j=Ca_j^2+o(1)\) chosen so \(8\pi^2-d_j>0\),
\[
 \frac{\mathcal E_{\rm final}}{h_j}
 \ge\frac{4(8\pi^2-d_j)}
             {8\pi^2U_j+4h_j(8\pi^2-d_j)}
 \ge 4-C'a_j^2-o(1). \tag{4.38}
\]
This proves the theorem, including noncompetitive endpoints. QED.
For the qualitative lower-limit assertion alone, a violating
subsequence would already be competitive. The added content of
(4.29a) is the uniform quadratic lower bound and its quantitative
equality consequences, not merely removal of that premise.

**Corollary 10 (first-order equality in these slices).** Under the
hypotheses of Theorem 9 with \(a_j\to0\), the following are equivalent:
\[
 \frac{\mathcal E_{\rm final}}{h_j}\longrightarrow4,
 \qquad \|\mathcal A_0(k_j)\|_2^2=o(Q_j). \tag{4.39}
\]
Either condition implies
\[
 \|\nabla_0^2k_j\|_2+
 \|\chi_j k_j\|_{H^2(X_j,g_{\rm CH})}
 +\||\operatorname{Rm}_0|\,|k_j|\|_2=o(\sqrt{Q_j}). \tag{4.40}
\]
These are norms of the raw gauge-fixed perturbation, not a claim of
uniform metric convergence after Yamabe normalization.

**Proof.** If \(\mathcal E/h\to4\), the chiral budget gives
\[
 P_{\rm final}\le
 \frac{2\pi^2AU\mathcal E_{\rm final}}{1-\mathcal E_{\rm final}}
       =(8\pi^2+o(1))Q.
\]
Combine with (4.29a), \(P_0=8\pi^2Q+o(Q)\) and \(a\to0\).
Conversely, \(x=o(\sqrt Q)\) in (4.37) makes the identified
remainder and scalar residual \(o(\sqrt Q)\); the exact expansion
and (4.25) give \(P_{\rm final}=8\pi^2Q+o(Q)\).
The actual scalar budget gives \(V_{\rm final}\ge2\pi^2A\), and
the chiral budget gives
\(4V_{\rm final}\le8\pi^2AU+3P_{\rm final}\).
Thus \(V_{\rm final}=2\pi^2A+O(Q)\), proving (4.39).
Finally apply (4.35) and
\(\|L_0(k)\|_2\le x+Ca\sqrt Q\) to get (4.40). QED.

Equivalently, in these exact gauges the full raw norm
\(\|k_j\|_{H^2(g_j^0)}\) is \(o(\sqrt{Q_j})\).
Indeed the exterior \(L^2\) norm is controlled by (4.40), while
the core norm is at most \(a_j\sqrt{\operatorname{Vol}(C_j)}
=o(\sqrt{Q_j})\). Integration by parts then controls the global
first derivative by the zeroth and second derivatives. Conversely,
this full \(H^2\) bound, \(a_j\to0\), and the core curvature
budget imply the curvature-product bound in (4.40), so the explicit
gauge linearization gives \(x_j=o(\sqrt{Q_j})\).

There is also low-order control of the actual final normalization,
without assuming its conformal factor uniformly close to one.
Write \(\widehat g=v^2g_{\rm raw}\), \(v>0\), and
\(\delta=S_{\rm raw}-S_{\widehat g}\). All norms in the following
identities use the raw metric. The exact scalar comparison gives
\[
 b^2=\delta+16\|v^2-1\|_2^2
                       +48\|d\log v\|_2^2,\qquad
 \delta=36\|\Delta v/v\|_2^2+48\|dv\|_2^2. \tag{4.40a}
\]
The first equality is I41's comparison written with the inverse
conformal factor. For the second, substitute
\(s_{\rm raw}=-6\Delta v/v-4v^2\), using the nonnegative
Laplacian, square, and integrate
\(\int v\Delta v=\int|dv|^2\).
At first-order equality, (4.37) gives \(b=o(\sqrt Q)\). Hence
\[
 \|v^2-1\|_2+\|v-1\|_2+\|dv\|_2+
       \|d\log v\|_2+\|\Delta v/v\|_2=o(\sqrt Q),
 \quad \int|v-1|^4=o(Q). \tag{4.40b}
\]
In particular
\(\|\widehat g-g_{\rm raw}\|_{2,g_{\rm raw}}
=2\|v^2-1\|_2=o(\sqrt Q)\).
This is a genuine low-order normalization conclusion, not an
\(L^\infty\), Hessian, or normalized-Ricci-tensor comparison.
Since raw and base norms are uniformly equivalent, it also gives
\(\|\widehat g-g_j^0\|_{L^2(g_j^0)}=o(\sqrt{Q_j})\).
The nonzero diffuse TT examples of Section 4.2 realize this class
nontrivially. Take its bounded seeds \(q_j\) and
\(k_j=h_j^{3/4}q_j\). Then
\(x_j^2=(c_0+o(1))h_j^{1/2}Q_j=o(Q_j)\), with \(c_0>0\).
In (4.29a) the first-variation error is
\(o(h_j^{3/4}Q_j)\), and \(a_j^2Q_j=O(h_j^{3/2}Q_j)\).
Thus \(P_{\rm final}>P_0\) eventually: these final metrics are
not merely isometric copies of the bases, yet have coefficient
four. A fixed nonzero parameter instead has the positive quadratic
payment in (4.10).

The equality class even allows unbounded raw curvature. Choose a
compact Euclidean seed \(a_*\) whose sixth-order
\(DZ_{\rm Eucl}(DB_{\rm Eucl}a_*)\) is nonzero, as in Section 4.2.
In each reserved chart replace it by
\(a_\ell(x)=\ell^4a_*(x/\ell)\), and apply the actual Bach
linearization on the locally Bach-flat normalized base.
The resulting global tensors \(q_{j,\ell}\) are exactly TT,
\(\|q_{j,\ell}\|_\infty=O(1)\), and, by four-dimensional scaling,
\[
 \|DZ_0(q_{j,\ell})\|_2^2=(c_*+o(1))A_j,\qquad c_*>0.
\]
The supports are disjoint chart balls; smooth background coefficients
converge after rescaling to their Euclidean principal symbols.
Take \(\ell_j=h_j\) and \(k_j=h_j^{3/4}q_{j,\ell_j}\).
Their identified derivative square is
\((c_*+o(1))h_j^{1/2}Q_j=o(Q_j)\), but at a fixed rescaled
seed point the raw traceless-Ricci perturbation has order
\(h_j^{3/4}\ell_j^{-2}=h_j^{-5/4}\).
The pointwise nonlinear term is smaller by a factor \(O(h_j^{3/4})\).
Thus these actual raw metrics have unbounded pointwise curvature,
and their normalized outputs still have first-order coefficient four
and \(P_{\rm final}>P_0\) by (4.29a).
No pointwise curvature assertion is made for those normalized outputs.
This is a test of the stated derivative-free theorem, not a new
solution of the unrestricted near-minimizer problem.

More generally, competitive outputs in Theorem 9 obey the full
first-order expansion
\[
 P_{\rm final}=8\pi^2Q+\|\mathcal A_0(k)\|_2^2+o(Q),\qquad
 \frac{\mathcal E_{\rm final}}h
       =4+\frac{\|\mathcal A_0(k)\|_2^2}{2\pi^2Q}+o(1),
 \tag{4.41}
\]
because competitiveness and (4.29a) give \(x=O(\sqrt Q)\);
(4.37), near-stationarity and the scalar/chiral volume bounds finish
the expansion. In particular any fixed improvement
\(\mathcal E/h\le4-\sigma\) forces \(a\ge c\sqrt{\sigma}\)
for all sufficiently large \(j\), whenever \(a\le a_0\).

This last step uses the actual CH exterior and the core \(L^2\)
budget; it is stronger than merely shrinking the radius in Theorem 7.
It also shows why arbitrary high derivatives do not themselves yield a
sub-four competitor in these vanishing-amplitude slices. It does not
provide a uniform gauge-fixing map, a fixed nonvanishing-amplitude
classification, or a classification of arbitrary near-minimizers.
The CH exterior is essential: on general negative KE backgrounds,
TT infinitesimal Einstein deformations may exist, and (4.31) need
not hold. The present theorem does not discard those genuine modes.

### 4.6 A measurable gauge error can replace exact Bianchi gauge

The preceding proof also yields a useful nonexact-gauge criterion.
Here both actual endpoints have scalar curvature \(-4\); this is
not a claim about an arbitrary unnormalized input followed by Yamabe
normalization.

**Corollary 11 (amplitude-weighted gauge error).** Use the selected
bases of Theorem 9. Let \(g_j=g_j^0+k_j\) have scalar curvature
\(-4\), and put
\[
 a_j=\|k_j\|_{\infty,g_j^0},\qquad
 G_j=\|\delta_0^*\beta_0 k_j\|_{2,g_j^0},\qquad
 \beta_0k=\delta_0k+\tfrac12d\operatorname{tr}_0k.
\]
If \(a_j\to0\) and \(a_jG_j=o(\sqrt{Q_j})\), then
\(\liminf_j\mathcal E(g_j)/h_j\ge4\).
There is no competitive-energy premise. For \(a\le a_0\), the
quantitative bound, with \(x=\|\mathcal A_0^F(k)\|_2\), is
\[
 \boxed{P_g\ge P_0+DP_0[k]+c x^2
             -C\{a^2Q+aG\sqrt Q+a^2G^2\}.} \tag{4.42}
\]

**Proof.** With \(\delta=-\operatorname{div}\) and
\(\delta^*\) the symmetrized covariant derivative, the exact
linearization is
\[
 DF_0(k)=\tfrac12\mathcal L_0^Fk-\delta_0^*\beta_0k.
\]
Repeating the cutoff proof with this explicit source gives
\[
 \|\nabla^2k\|_2+\|\chi k\|_{H^2(X_j,g_{\rm CH})}
          +\||\operatorname{Rm}_0|\,|k|\|_2
 \le C\{\|DF_0(k)\|_2+G+a\sqrt Q\}. \tag{4.43}
\]
Since the identified derivative differs by at most \(Ca\sqrt Q\),
the exact identified remainder satisfies
\[
 \|e\|_2\le Ca x+CaG+Ca^2\sqrt Q.
\]
At both endpoints \(F=Z\). Expand its squared norm as before.
The terms involving \(x\) are absorbed into a fixed fraction of
\(x^2\); the others are bounded by the last term of (4.42).
This proves the finite inequality. The stated asymptotic conditions
make that last term \(o(Q)\); near-stationarity and the monotone
chiral conversion (4.38) prove the conclusion. QED.

In this larger class, the equivalence
\(\mathcal E/h\to4\) if and only if \(x^2=o(Q)\) also holds.
However the unweighted derivative conclusion (4.40) need not follow:
\(G\) itself need not be \(o(\sqrt Q)\). Its amplitude-weighted
size, not its full norm, controls the nonlinear energy loss.

Constant scalar curvature does not supply this gauge condition.
For example, on the reserved uniformly controlled charts take
diffeomorphisms equal to the identity near their boundaries, with
the local shear
\[
 \phi_j(x)=
 (x_1,x_2+(a_j/\lambda_j)\chi(x)\sin(\lambda_jx_1),x_3,x_4).
\]
Replicate over the lifted charts and put \(g_j=\phi_j^*g_j^0\).
These are actual scalar-minus-four metrics with exactly the same
\(P,V,\mathcal E\) as the base. Their difference has supremum
norm comparable to \(a_j\), whereas on \(\chi=1\) the principal
term of \(\delta^*\beta k\) has size
\(a_j\lambda_j^2/2\).
Consequently \(G_j\) is bounded below by a constant times
\(a_j\lambda_j^2\sqrt{A_j}\), after taking the frequencies
large enough to dominate the bounded-coordinate lower-order errors.
Thus even \(a_jG_j/\sqrt{Q_j}\) can diverge.
This is pure coordinate motion, not a lower-energy geometry:
the inverse diffeomorphism restores the exact base.
It shows why a uniform gauge-fixing result, rather than a scalar
or energy estimate alone, is required to pass to arbitrary nearby
metrics modulo diffeomorphisms.

The weighted condition is genuinely weaker than \(G=o(\sqrt Q)\).
In the same pullback construction choose \(a_j=h_j\) and
\(\lambda_j=h_j^{-2/3}\). Then
\[
 G_j/\sqrt{Q_j}\asymp h_j^{-5/6}\longrightarrow\infty,\qquad
 a_jG_j/\sqrt{Q_j}\asymp h_j^{1/6}\longrightarrow0.
\]
These actual representatives satisfy Corollary 11 and retain the
base energy exactly. This check uses diffeomorphism invariance,
not a new family of lower-energy metrics.

**Nonconstant-scalar inputs.** One may also relax TT before the
final Yamabe normalization, provided the additional scalar-linear
error is retained. For a general smooth \(k\), define
\[
 D=\|Ds_0[k]\|_2,\qquad
 G=\|\delta_0^*\beta_0k\|_2,\qquad
 x=\|\mathcal A_0^Z(k)\|_2.
\]
For \(a=\|k\|_\infty\le a_0\), the same proof gives
\[
 \boxed{P_{\widehat{g_0+k}}\ge P_0+DP_0[k]+c x^2
       -C\{a^2Q+aG\sqrt Q+a^2G^2+D^2\}.} \tag{4.44}
\]
Indeed \(DF_0(k)=DZ_0(k)+\frac14Ds_0[k]g_0\).
The graph estimate therefore has right side
\(C(x+D+G+a\sqrt Q)\).
Its raw identified remainder is bounded by
\(Ca(x+D+G)+Ca^2\sqrt Q\), and its scalar residual by
\(D+Ca(x+D+G+a\sqrt Q)\).
Subtract (4.25), complete the squares in \(x\), and use
\(aD\sqrt Q\le(a^2Q+D^2)/2\). This proves (4.44).
Consequently the conditions
\[
 a_j\to0,\qquad a_jG_j=o(\sqrt{Q_j}),\qquad
 D_j=o(\sqrt{Q_j})
\]
are sufficient for the coefficient-four lower bound, with equality
if and only if \(x_j^2=o(Q_j)\).
At first-order equality the low-order final-factor conclusions
(4.40a)--(4.40b) persist; they are not asserted for arbitrary
noncompetitive outputs.
Exact TT is included because
\(Ds_0[k]=-\langle Z_0,k\rangle\).
Neither the scalar-linear nor the weighted gauge condition has been
proved automatic for arbitrary small-amplitude inputs.

Only the trace-free gauge forcing is needed in these two estimates.
Precisely, \(G\) can be replaced in (4.42) and (4.44) by
\(G^\circ=\|(\delta^*\beta_0k)^\circ\|_2\).
This is a refinement of the same criterion, not another gauge-existence
claim. Here is the trace calculation, to specify why no scalar
direction has been suppressed. Write \(t=\operatorname{tr}_0k\)
and \(q=k-tg_0/4\). The exact identities are
\[
 DZ_0[k]=\tfrac12\mathcal L_0^Fq-(\delta^*\beta_0k)^\circ
                     +\tfrac14\langle Z_0,k\rangle g_0,
 \qquad
 Ds_0[k]=(\tfrac34\Delta+1)t+\delta\delta q-\langle Z_0,q\rangle.
 \tag{4.45}
\]
Apply the patched full-tensor estimate to \(q\) with the displayed
source. This bounds its graph norm by
\(C(x_Z+G^\circ+a\sqrt Q)\).
The positive scalar operator in (4.45) then gives
\[
 \|t\|_2+\|\Delta t\|_2
       \le C(D+\|\nabla^2q\|_2+a\sqrt Q).
\]
For its Hessian use scalar Bochner with
\(\operatorname{Ric}_0=Z_0-g_0\),
\(\|Z_0\|_2=O(\sqrt Q)\), and
\(\|dt\|_4^2\le Ca\|\nabla^2t\|_2\).
Young's inequality costs only \(Ca^2Q\), not \(Ca^2A\).
The trace curvature-product norm is bounded on the core by
\(Ca\sqrt Q\) and on the bounded-curvature exterior by \(C\|t\|_2\).
Thus the complete graph norm is at most
\(C(x_Z+G^\circ+D+a\sqrt Q)\).
For constant-scalar endpoints the exact scalar expansion gives
\(D\le Ca\) times this graph norm. If the F-identification is used,
\(x_Z\le x_F+D/2\), so the \(D\) term still absorbs for small \(a\).
The previous remainder and square-completion proofs now apply with
\(G^\circ\), retaining \(D^2\) only in the general raw/Yamabe case.

## 5. Exact scope of this continuation

The weak zero endpoint still requires an additional differential or
global implication. Equations (1.4) and (2.5) identify a weighted
derivative control and the specific covariance which obstructs an
unweighted conclusion; they do not dispose of it by interpolation.
The existing small local cores are not closed actual escape sequences.

The construction-side conclusion is complete in its defined class:
arbitrary backgrounds and subsequent Yamabe minimization have the
limits (3.2), (3.5), with the sharp value (3.6), penalties (3.10)--(3.11),
and perturbative escape threshold (4.4)--(4.5). The conformal tensor
lemma and (4.10) supply a nonzero actual test of the diffuse variation.
Proposition 6 then treats core directions on the specified
almost-critical recovery sequence, and (4.17) measures the nonlinear
change required of any successful path there.
Theorem 7 and Corollary 8 remove the assumed Taylor control in two
explicit small-amplitude gauges by absorbing the actual competitive
energy. Theorem 9 uses the classical all-tensor CH gap and actual
cutoff/core geometry to remove the \(h\)-dependent amplitude rate
and the competitive-energy premise. Its direct nonlinear inequality
retains a positive quadratic term; Corollary 10 identifies the
first-order equality condition within the specified actual slices.
Corollary 11 permits amplitude-weighted gauge error on actual
constant-scalar endpoints; it does not automatically place other
metrics in that class.
I44 already supplies the underlying unchanged-cap obstruction.
These deductions constrain first-order geometry but do not determine
the all-metric theorem's coefficient.

The next unresolved implications are therefore concrete: control the
actual correlation and the subsequent torsion-length derivative relation,
or build a closed zero-end sequence; and on the balanced family, control
the full signed \(Ah\)-scale remainder or realize geometry beyond the
construction/perturbation class above. No additional field supplier,
global core decomposition, or all-metric optimality is asserted.
For the new stability route the missing intrinsic step is a uniform
amplitude-preserving gauge reduction through the shrinking donors.
Its vector-field linearization is
\(\beta_0(\mathcal L_Xg_0)=(\nabla^*\nabla-\operatorname{Ric}_0)X^\flat\).
The CH symmetric-tensor gap used here does not itself solve that
global nonlinear gauge problem.


END COMPLETE SOURCE


---

## Source 2: 20260928_marked_centers_and_harmonic_slices.md

Original path: `continuation/20260928_marked_centers_and_harmonic_slices.md`

SHA-256: `e8e771f0cfa241480a8c884cff096a1ce13a76e8b1099dc72a36ad95f57e1475`

BEGIN COMPLETE SOURCE

# Moving surgery centers and uniform first-order stability

28 September 2026. Continuation of 3409fe5. This is a local research
proof, not a web-review package.

The previous [I52 proof](20260927_endpoint_covariance_and_surgery_limits.md)
established first-order stability of selected shrinking-surgery metrics
inside explicit TT or Bianchi slices. The missing passage from arbitrary
nearby metrics to a fixed slice is not merely an unproved estimate.
The construction below shows that such a passage, with uniformly bounded
metric distortion, can fail on the actual recovery family.

The obstruction is a marked geometric variable. A harmonic map on the
smooth negatively curved limit is fixed by its homotopy class, whereas
an isotopy on the resolved manifold must preserve the exceptional class
and hence its concentration point. Moving that point relative to the
limiting harmonic map makes the two requirements incompatible.

The positive continuation keeps the centers as parameters. I52's
first-order inequality then holds uniformly on compact configuration
families, including their conformal and diffeomorphism saturations.
It does not assert that every nearby metric admits this parametrization.
Continuing past this obstruction, the companion
[matched-cap proof I53](20260928_intrinsic_caps_and_stability.md)
now removes the gauge and scalar assumptions from the lower first-order
bound near selected recovery bases. It does not solve a fixed exact slice.

## 1. Notation and actual recovery geometry

Let \(X\) be a closed complex-hyperbolic surface with
\(\operatorname{Ric}(g_X)=-g_X\), and let \(A=c_1^2(X)\). On
\[
 M=X\# k\overline{\mathbb {CP}}^{\,2}
       \#\ell(S^1\times S^3),\qquad k\ge1,
\]
put \(Q=k+4\ell\), \(h=Q/A\), and
\[
 P(g)=\int|\operatorname{Ric}^{\circ}_g|^2,\quad
 S(g)=\int s_g^2,\quad R(g)=\int|\operatorname{Ric}_g|^2.
\]
The relative Einstein defect is the same functional as in I40--I52.
For a scalar-minus-four metric it is
\[
 \mathcal E(g)=\frac{4P(g)}{R(g)}
             =\frac{4P(g)}{P(g)+4V(g)}.                 \tag{1.1}
\]
All classes and actual monopole suppliers are inherited from the same
smooth manifolds. No new local solution is substituted for a closed
conformal supplier.

We use the actual Burns blowup and two-ended scalar-flat Schwarzschild
handle constructions of LeBrun, Theorem 4.3, with negative Yamabe
normalization as justified in I52, Section 3. For a fixed \(X,k,\ell\),
their normalized shrinking limits satisfy
\[
 P(g_t)\longrightarrow8\pi^2Q,\qquad
 V(g_t)\longrightarrow2\pi^2A,\qquad
 \mathcal E(g_t)\longrightarrow\frac{4h}{1+h}.         \tag{1.2}
\]
The last limit is a recovery value, not an assertion about the
unrestricted infimum.

For the marked argument it is important to specify the handles.
We put the two mouths of each handle in one shrinking background
ball. If \(R_t\) is its outer radius, \(d_t\) the separation of the
mouths, \(r_t\) their cutoff radius and \(a_t\) the donor scale, choose
\[
 a_t\ll r_t^2,\qquad r_t\ll d_t\ll R_t\longrightarrow0. \tag{1.3}
\]
All clusters are disjoint, and the limiting cluster points are distinct.
First select the cluster sizes; then choose the inner scales sufficiently
small for the finitely many required energy and normalization errors.
This is a fixed-topology diagonal, before taking any large-cover limit.

The whole handle cluster has diameter tending to zero. The Schwarzschild
neck has diameter \(O(r_t)\), and the remaining cluster has diameter
\(O(R_t)\). The normalized Yamabe factors have a uniform upper bound
from the uniform negative lower bound for the raw scalar curvature.
These statements also hold for the Burns regions. The metrics converge
smoothly to the background off the finite set of limiting points.
Consequently the marked metric spaces converge to the smooth \(X\).

This choice is essential: handles joining two fixed distinct points
would instead identify those points in the metric limit. We do not
use that different limit here. Clustering does not change the smooth
topology, the actual supplier, or the costs in (1.2).

The cutoffs and the exterior estimates of I52 remain available. One
uses an enclosing cutoff for each whole cluster and much smaller
cutoffs at the two mouths for construction. There is bounded curvature
energy per cluster, and the transition errors are chosen arbitrarily
small. Thus these clustered bases can satisfy all the selections in
I52, Theorem 9, simultaneously with (1.3).

## 2. Comparing normalization without resolving the cores again

The following elementary observation is useful when the raw metrics
agree near the entire singular region.

**Lemma 1 (relative Yamabe normalization).** Suppose \(b_{0,t}\) and
\(b_{1,t}\) are smooth raw metrics on the same closed manifold, equal
outside a fixed regular region \(K\). Let
\(g_{0,t}=u_t^2b_{0,t}\) have scalar curvature \(-4\). Assume on a
neighborhood of \(K\) that
\[
 u_t\longrightarrow1\text{ in }C^2,\qquad
 b_{i,t}\longrightarrow b_i\text{ smoothly},\qquad s_{b_i}=-4.
                                                               \tag{2.1}
\]
If \(\|b_{1,t}-b_{0,t}\|_{L^\infty(b_{0,t})}\le a\), then their
scalar-minus-four Yamabe representatives satisfy
\[
 \|g_{1,t}-g_{0,t}\|_{L^\infty(g_{0,t})}\le a+o_t(1)(1+a).       \tag{2.2}
\]
No lower bound for the size of the cores is needed.

**Proof.** Put \(\widetilde g_t=u_t^2b_{1,t}\).
It equals \(g_{0,t}\) off \(K\). The conformal scalar formula and
(2.1) show
\[
 \delta_t:=\|s_{\widetilde g_t}+4\|_\infty\longrightarrow0.
\]
For sufficiently small \(t\), this metric has negative scalar
curvature. Write its normalized representative as
\(g_{1,t}=v_t^2\widetilde g_t\). At the maximum and minimum of \(v_t\),
the scalar equation gives
\[
 1-\delta_t/4\le v_t^2\le1+\delta_t/4.                         \tag{2.3}
\]
The common \(u_t^2\) cancels in the relative pointwise tensor norm,
which proves (2.2). QED.

This proof requires only the already established exterior convergence.
It does not infer uniform convergence of \(u_t\) on every rescaled
donor from exterior convergence.

## 3. A fixed-base Bianchi slice can have unbounded distortion

Our divergence convention is
\[
 \beta_g q=\delta_gq+\tfrac12d\,\operatorname{tr}_gq,\qquad
 (\delta_gq)_j=-\nabla^i q_{ij}.
\]
For a diffeomorphism \(\varphi\), set \(q=\varphi^*g_1\). Direct
contraction of the connection difference gives
\[
 \tau(\operatorname{id}:(M,g_0)\to(M,q))^k
       =-q^{k\ell}(\beta_{g_0}q)_\ell.                         \tag{3.1}
\]
Thus
\(\beta_{g_0}(\varphi^*g_1-g_0)=0\) is exactly the harmonic-map
equation for \(\varphi:(M,g_0)\to(M,g_1)\), not only its linearization.

**Theorem 2 (marked obstruction to a uniform fixed slice).**
For the balanced actual family used in I40--I52, with \(h_j\to0\)
and at least one blowup, there exist scalar-minus-four recovery
metrics \(g_j^0,g_j^1\) on the same \(M_j\) such that
\[
 \|g_j^1-g_j^0\|_{L^\infty(g_j^0)}\longrightarrow0,\qquad
 \frac{\mathcal E(g_j^0)}{h_j}\longrightarrow4,\qquad
 \frac{\mathcal E(g_j^1)}{h_j}\longrightarrow4,                 \tag{3.2}
\]
and every \(\varphi\in\operatorname{Diff}_0(M_j)\) satisfying
\[
 \beta_{g_j^0}(\varphi^*g_j^1-g_j^0)=0                         \tag{3.3}
\]
has bilipschitz constant greater than \(j\), measured from \(g_j^0\)
to \(g_j^1\). If no such diffeomorphism exists, the statement has
the usual empty-set meaning.
The same examples can also be chosen with
\[
 \|\delta_{g_j^0}^*\beta_{g_j^0}(g_j^1-g_j^0)\|_2=o(\sqrt{Q_j}).
                                                               \tag{3.3a}
\]
Thus even a small actual gauge residual does not imply a uniformly
controlled exact gauge at the fixed marked base.

The bases \(g_j^0\) may in addition satisfy the selections of I52.
In particular there is no automatic uniformly bounded, let alone
vanishing-amplitude, exact Bianchi representative relative to those
fixed bases under just constant scalar curvature, competitive energy,
and \(C^0\) closeness.

**Proof: move the smooth background while retaining the marked core.**
First keep \(X,k,\ell\) fixed. Choose one exceptional point \(p\).
In a CH chart about \(p\), choose a local Killing field moving \(p\),
multiply it by a cutoff, and let \(\psi_\epsilon\) be its small-time
flow. It is isotopic to the identity, is a genuine local CH isometry
on a smaller neighborhood of \(p\), and is the identity near all
other surgery clusters and outside a larger chart. Set
\[
 b_\epsilon=\psi_\epsilon^*g_X .
\]
Then \(b_\epsilon=g_X\) near every donor and outside a fixed regular
annulus \(K\), while
\[
 \|b_\epsilon-g_X\|_{C^m}\le C_m|\epsilon|,\qquad
 \psi_\epsilon^{-1}(p)\ne p\quad(\epsilon\ne0).                 \tag{3.4}
\]
Perform exactly the same marked surgeries at exactly the same
points in \(g_X\) and \(b_\epsilon\). The two raw metrics are identical
near all donors, and differ only on \(K\). Normalize them to obtain
\(g_{0,t}\) and \(g_{\epsilon,t}\).
Lemma 1 and the recovery limits give, for fixed \(\epsilon\),
\[
 \|g_{\epsilon,t}-g_{0,t}\|_{L^\infty(g_{0,t})}
       \le C|\epsilon|+o_t(1),                               \tag{3.5}
\]
and (1.2) for both families.

**Proof: compactness of a hypothetical bounded-distortion gauge.**
Suppose for this fixed nonzero \(\epsilon\) there are \(t_n\to0\)
and \(L\)-bilipschitz maps
\(\varphi_n\in\operatorname{Diff}_0(M)\) satisfying (3.3).
The collapsing regions described in Section 1 have diameter tending
to zero. Uniform convergence on the smooth exterior, or equivalently
the elementary compactness of bilipschitz maps between the resulting
compact metric spaces, produces a bilipschitz homeomorphism
\[
 F:(X,g_X)\longrightarrow(X,b_\epsilon).                     \tag{3.6}
\]
The inverse maps converge as well, so this is not merely a continuous
map onto a quotient.

The exceptional class at \(p\) forces
\[
 F(p)=p.                                                     \tag{3.7}
\]
Indeed the exceptional sphere \(E_p\) in the source has diameter
tending to zero. Its image also does, and
\([\varphi_n(E_p)]=[E_p]\ne0\) in \(H_2(M;\mathbb Z)\).
If its limit were a regular point of the target \(X\), it would
eventually lie in a contractible coordinate ball and have zero class.
If its limit were another exceptional point \(q\), it would lie in
one fixed small enclosing topological neighborhood of that cluster,
whose image in \(H_2(M)\) is
\(\mathbb Z[E_q]\), not \(\mathbb Z[E_p]\).
A whole handle cluster has \(H_2=0\).
These exhaust the points other than \(p\), proving (3.7).
We use the entire neighborhoods and their marked homology, not just
terminal bubbles.

**Proof: the limit is in the identity homotopy class.**
Collapse maps \(\pi_n:M\to X\) induce the usual quotient
\[
 \pi_1(M)=\pi_1(X)*F_\ell\longrightarrow\pi_1(X).
\]
Isotopy of \(\varphi_n\) gives
\(\pi_n\circ\varphi_n\simeq\pi_n\).
Choose generators on loops avoiding the finite source cluster set
and \(F^{-1}\) of the target cluster set. On these loops the convergence
is in the ordinary smooth regions, so the induced outer homomorphism
of \(F\) on \(\pi_1(X)\) is the identity. The CH manifold \(X\) is
aspherical. Hence \(F\) is homotopic to the identity.
This argument explicitly kills the free handle generators; it does
not identify \(\pi_1(M)\) with \(\pi_1(X)\).

**Proof: the harmonic limit contradicts the mark.**
By (3.1), each \(\varphi_n\) is harmonic. Away from the finite set
consisting of source cluster points and inverse images of target
cluster points, both metrics converge smoothly and the differential
of \(\varphi_n\) is uniformly bounded. In coordinates the harmonic
equation has bounded right-hand side; interior elliptic estimates
and bootstrapping give smooth convergence there.

The limit (3.6) is Lipschitz on the smooth compact \(X\).
In the weak harmonic equation a cutoff at a missing point has an
error bounded by \(C r^3\): the derivative of the map is bounded
and the cutoff has derivative \(O(r^{-1})\) on a four-dimensional
annulus of volume \(O(r^4)\). The equation therefore extends weakly
across every missing point. Coordinate elliptic regularity makes
\(F\) a smooth harmonic map on all of \(X\).

The map \(\psi_\epsilon^{-1}:(X,g_X)\to(X,b_\epsilon)\) is an
isometry, hence harmonic, and is homotopic to the identity.
Strictly negative sectional curvature of \(b_\epsilon\) makes
this harmonic map unique in its homotopy class. One may apply
[Hartman, Section 1(H), rank-greater-than-one corollary, p.675](https://math.jhu.edu/~js/Math646/hartman.harmonic.pdf).
Equivalently, geodesic-homotopy energy convexity is strict against
the rank-four isometry unless the homotopy is stationary.
Thus \(F=\psi_\epsilon^{-1}\), contradicting (3.7) and (3.4).

We have proved that for each fixed nonzero \(\epsilon\) and each
finite \(L\), sufficiently small donor scales exclude every such
\(L\)-bilipschitz gauge.

**Proof: the balanced diagonal.**
Return to \(X_j,k_j,\ell_j\). Choose \(\epsilon_j\to0\), using
uniformly controlled lifted CH charts; if needed choose it even
smaller to absorb any chart constant. For each fixed \(j,\epsilon_j\),
choose the clustered donor scales so small that:

- the just-proved exclusion holds with \(L=j\);
- the relative error in (3.5) tends to zero;
- both errors in (1.2) are \(o(Q_j)\) in \(P\) and small enough
  in \(V\) to give (3.2);
- all the core, exterior, and near-stationarity errors required in
  I52 are at most a prescribed number tending to zero.

Each list is finite at fixed \(j\), so the same diagonal satisfies
all requirements. Since \(4/(1+h_j)\to4\), (3.2) follows.
No assertion about the rate at which the necessary bilipschitz
constant diverges is required. The remaining strengthening (3.3a)
is proved next and is included in the same diagonal. QED.

### 3.1 The counterexamples still satisfy the approximate-gauge criterion

This is a positive coverage statement as well as a distinction between
an approximate and an exact gauge. Write
\[
 r_t=u_t^2(b_{\epsilon,t}-b_{0,t}),\qquad
 \widetilde g_t=g_{0,t}+r_t,\qquad
 g_{\epsilon,t}=e^{2f_t}\widetilde g_t,\qquad w_t=e^{2f_t}-1.
\]
The tensor \(r_t\) is supported in the regular annulus \(K\), with
\(\|r_t\|_{C^2(g_{0,t},K)}\le C|\epsilon|\). Lemma 1 gives
\(\|f_t\|_\infty\le C\delta_t\), where
\(s_{\widetilde g_t}+4\) is supported in \(K\), has supremum
\(\delta_t\to0\), and has \(L^2\) norm \(O(\delta_t)\).
Also \(P(\widetilde g_t)\le C Q\), since outside \(K\) it is the
same metric as \(g_{0,t}\), while its curvature on \(K\) converges
smoothly to that of the CH background \(b_\epsilon\).

The derivative bounds proved in I52, Lemma 5, now apply on
\(\widetilde g_t\):
\[
 \|\nabla^2 f_t\|_2\le C\delta_t(1+\sqrt Q),\qquad
 \|df_t\|_2\le C\delta_t,\qquad
 \|df_t\|_4^2\le C\delta_t^2(1+\sqrt Q).               \tag{3.8}
\]
Changing the connection in these estimates back to \(g_{0,t}\)
only costs \(C|\epsilon|\|df_t\|_{2,K}\); the two metrics agree
off \(K\). Consequently the Hessian of \(w_t\) has the same first
bound in (3.8).

Put \(k_t=g_{\epsilon,t}-g_{0,t}
       =w_tg_{0,t}+(1+w_t)r_t\). The exact product rules are
\[
 \beta_0(wg_0)=dw,\qquad
 \beta_0(fr)=f\beta_0r+
       \bigl(\tfrac12\operatorname{tr}_0r\,I-r^\sharp\bigr)df .
\]
One further derivative therefore gives
\[
 \|\delta_0^*\beta_0 k_t\|_2
    \le C\{|\epsilon|+\delta_t(1+\sqrt Q)\}.           \tag{3.9}
\]
Choose the donor scales also to ensure
\(\delta_t(1+\sqrt Q)\le|\epsilon|\).
With \(\epsilon_j\to0\) and \(Q_j\ge1\), equations (3.5) and
(3.9) prove (3.3a) and
\[
 \|k_j\|_\infty\,
       \|\delta_0^*\beta_0 k_j\|_2=o(\sqrt{Q_j}).       \tag{3.10}
\]
Thus these actual examples are already covered by the approximate
criterion of I52, Corollary 11. They do not refute that criterion
or show that moving centers is the only way to retain coefficient
four. What fails is the attempted replacement of a small residual
by a uniformly controlled exact fixed-base harmonic slice.
If a chosen regular chart or cutoff has constants depending on \(j\),
choose the displacement first so that the resulting
\(C_j|\epsilon_j|\to0\), and then the donor scales so that
\(C_j\delta_j(1+\sqrt{Q_j})\le C_j|\epsilon_j|\).
This is permitted by the fixed-\(j\), fixed-displacement argument
and does not change the exact-gauge exclusion.

**What the theorem does not say.** These are not sub-four metrics,
not failures of actual monopole supply, and not counterexamples to
I52 or to Yau26. It also does not exclude other useful gauges,
changing the background centers, or approximate gauge equations.
It rules out a precise proposed reduction to a fixed exact Bianchi
slice, even on competitive actual recovery metrics.

## 4. Retaining the centers gives a positive uniform extension

The obstruction above disappears for its explicit family if the centers
are moved with the background. Let \(\mathbf p\) be the marked centers
and local frames in the first construction and
\(\mathbf q=\psi_\epsilon(\mathbf p)\). The local isometry at each
affected center extends over the corresponding Burns donor using the
transported frame; the other donors are unchanged. Thus there is a
marked diffeomorphism between the two surgery manifolds with the exact
raw identity
\[
 b_{\epsilon,t}
     =\Psi_\epsilon^*b_t(g_X,\mathbf q).                       \tag{4.1}
\]
Negative Yamabe normalization commutes with pullback, by uniqueness, so
\[
 g_{\epsilon,t}
     =\Psi_\epsilon^*g_t(g_X,\mathbf q).                       \tag{4.2}
\]
This is an exact equivalence, not an approximate gauge assertion.
The family defeated a fixed center, not the full family of centers.

We next record the uniform statement which follows from the actual
estimates of I52; keeping it uniform is important when the number
and positions of the cores vary.

**Theorem 3 (uniform moving-center stability).** For each \(j\), let
\(K_j\) be a compact set of marked, pairwise distinct cluster-center
configurations and frames in the CH cover \(X_j\), with the fixed
counts \(k_j,\ell_j\). The enclosing balls are disjoint and lie
in uniformly controlled CH charts. There are recovery families
\(g_j^0(\mathbf p)\), \(\mathbf p\in K_j\), whose diagonal errors
are uniform on \(K_j\), such that the conclusion of I52, Theorem 9
holds for every choice \(\mathbf p_j\in K_j\), with constants
independent of these choices.

In particular, if \(a_j=\|k_j^{\mathrm{met}}\|_\infty\to0\) and
\(k_j^{\mathrm{met}}\) is TT relative to
\(g_j^0(\mathbf p_j)\), then
\[
 \liminf_j
 \frac{\mathcal E\!\left(\widehat{g_j^0(\mathbf p_j)
                                    +k_j^{\mathrm{met}}}\right)}
      {h_j}\ge4.                                             \tag{4.3}
\]
The same holds in the constant-scalar Bianchi version of I52.
The exact-gauge quadratic lower bound and equality criterion are
uniform as well. The symbol \(k_j^{\mathrm{met}}\) is a tensor and
is distinct from the blowup count \(k_j\).

**Proof.** For each fixed \(j\), compactness of \(K_j\) supplies a
positive minimum separation of its distinct cluster centers, not
a separation independent of \(j\). Choose enclosing radii below
that separation and so small that their fourth powers sum to
at most \(\varepsilon_jQ_j\), with \(\varepsilon_j\to0\).
Within the handle clusters use the further hierarchy (1.3).
All local metric and cutoff estimates take place in CH charts.
The number of cutoffs is \(O(Q_j)\); each has uniformly bounded
scale-invariant second-derivative cost.

The donor costs, scalar lower bound, and exterior convergence are
uniform over a compact configuration set at fixed \(j\).
For completeness, nonuniform exterior convergence would give
a sequence of configurations converging in \(K_j\).
After moving their finitely many centers by smooth chart
identifications, the capacity and negative-Yamabe uniqueness
proof of I52, Lemma 3, applies to the limiting configuration,
contradicting that failure. Local elliptic estimates give the
required exterior \(C^2\) convergence. The raw and normalized
Bach and Ricci-gradient errors are treated in the same finite
compact family. A common sufficiently small scale therefore
makes their errors at most \(\varepsilon_jQ_j\).
In particular impose the actual stronger exterior selection
\(P_{\rm ext}\le\varepsilon_j^2Q_j^2/A_j\), as well as
\(\|\operatorname{grad}P(g_j^0)\|_1\le\varepsilon_jQ_j\).
An exterior bound of only \(o(Q_j)\) would not justify that
near-stationarity statement.

The constants in the remaining I52 argument use only the universal
CH tensor gap, the bounded energy per donor, the disjoint cutoff
estimates, and these selected errors. They do not use the minimum
separation itself. Hence its graph estimate and square completion
give, uniformly in \(\mathbf p\),
\[
 P_{\mathrm{final}}\ge8\pi^2Q_j+c x_j^2
                         -C a_j^2Q_j-\varepsilon_jQ_j,        \tag{4.4}
\]
where \(x_j\) is the appropriate norm-preserving identified
linearization from I52. The same opposite-chirality conversion
proves (4.3). The matching expansion in the competitive case
gives the inherited equality criterion \(x_j^2=o(Q_j)\).
QED.

There need not be a global trivialization of the entire configuration
bundle of smooth manifolds. The assertions are fiberwise and invariant
under the marked local identifications. For the one-parameter family
in Theorem 2 a contractible chart of configurations suffices.

**Corollary 4 (conformal and diffeomorphism saturation).**
The lower bound (4.3) is unchanged if one takes any orientation-preserving
pullback and any positive smooth conformal multiple of its output.
Neither the conformal factor nor the diffeomorphism needs a uniform
coordinate bound.

**Proof.** Diffeomorphism invariance is exact. If \(\widehat g\)
is the negative constant-scalar representative of a conformal class
and \(g\) is any other representative, put
\[
 \delta=S(g)-S(\widehat g)\ge0,\qquad
 L=S(g)-\frac{(\int s_g)^2}{V(g)}\ge0.
\]
The four-dimensional conformal curvature identities give
\[
 P(g)=P(\widehat g)+\delta/12,\qquad
 R(g)=R(\widehat g)+\delta/3.
\]
Consequently
\[
 \mathcal E(g)=
 \frac{\mathcal E(\widehat g)R(\widehat g)+\delta/3+L}
      {R(\widehat g)+\delta/3}
 \ge \min\{\mathcal E(\widehat g),1\}.                         \tag{4.5}
\]
Since \(h_j\to0\), this inequality transfers (4.3), including cases
of noncompetitive conformal representatives. QED.

Theorems 2--3 belong together: a configuration family is genuinely
needed for the proposed uniformly controlled exact-slice description
of these explicit \(C^0\)-nearby recovery metrics, and the first-order
estimate is uniform when that variable is kept. The approximate
criterion supplies a separate fixed-base route for this example.
We have not proved that this modulated family covers all nearby
metrics, nor that every unrestricted near-minimizer lies near it.

## 5. The intrinsic continuation: matched collars without a global slice

A second route avoids a global harmonic slice. The
[complete companion proof](20260928_intrinsic_caps_and_stability.md)
constructs a full-curvature cap of cost
\(C(\int|\operatorname{Rm}|^2+\|g-e\|_\infty^2)\), matching the
actual outer collar exactly. Localized DeTurck smoothing supplies
an interior smooth band; a fixed-input frozen-collar estimate and
critical energy control complete the two matches.

No scalar normalization is needed. Directly, for
\(\mathcal E<1/2\), Chern--Gauss--Bonnet gives total curvature
\(O(\chi)=O(A_j)\). In \(L_j\) disjoint fixed-ratio bands around
each marked blowup, minimum-energy selection gives
\[
 \sum_i\int_{\mathcal A_{i,j}}|\operatorname{Rm}|^2
        \le C A_j/L_j=o(Q_j)\quad\text{if }L_jh_j\to\infty.
                                                               \tag{5.1}
\]
The annuli enclose designated blowups, not handles. Leave any
energy-bad cores unremoved; their count is \(o(Q_j)\) when
\(L_jh_j\to\infty\). The partial signature identity charges these
retained blowups explicitly. It gives
\[
 \mathcal E(g_j)\ge\frac{4h_j}{1+h_j}
                      -C/L_j-C(k_j/A_j)a_j^2.        \tag{5.1a}
\]
This proves the coefficient-four lower bound for arbitrary
\(C^0\)-nearby smooth competitors on selected long-annulus bases,
and computes the infimum in every shrinking \(C^0\) neighborhood.
It also allows \(o(Q_j)\) wholly unstructured blowups and only
mean-square small annular amplitudes.

The remaining all-metric question is whether unrestricted
near-minimizers possess enough such marked annuli. The cap itself
is no longer the missing step. No global conformal normalization
is used to infer zeroth-order closeness.

There is no static curvature-supremum estimate for arbitrary metrics
from these inputs. For example, on a fixed local annulus consider
\[
 g=dx_1^2+e^{2u(x_1)}dx_2^2+e^{-2u(x_1)}dx_3^2
                  +v(x_1)^2dx_4^2,\qquad
 v''=(2r^2-(u')^2)v,\quad v(0)=1,\ v'(0)=0.
\]
Its scalar curvature is exactly \(-4r^2\). With a compactly supported
slab \(u=a\psi((x_1-c)/\ell)\), on a bounded interval,
\[
 \|g-g_{\mathrm{Eucl}}\|_\infty
       =O(a+r^2+a^2/\ell),\qquad
 \int|\operatorname{Rm}|^2=O(a^2/\ell^3+r^4),\qquad
 \|\operatorname{Rm}\|_\infty\gtrsim a/\ell^2 .
                                                               \tag{5.2}
\]
Choose \(a=\ell^p\), \(3/2<p<2\), and \(r\to0\). Then the first
two quantities vanish while the last diverges. The estimates follow
from the multiply warped curvature formulas and the displayed ODE;
\(v\) stays positive because \(r^2+a^2/\ell\to0\).
This local test does not disprove a low-energy cap.

Positive-time Ricci smoothing is a possible construction tool, but
matching the original collar remains an extra step. Even using an
actual Ricci flow rather than DeTurck coordinates, a variable-time
graph \(g_\theta(x)=g(x,\theta(x))\) creates connection terms
\[
 B^k{}_{ij}
 =-g^{k\ell}\{\operatorname{Ric}_{j\ell}\theta_i
             +\operatorname{Ric}_{i\ell}\theta_j
             -\operatorname{Ric}_{ij}\theta_\ell\}.            \tag{5.3}
\]
Its curvature includes \(d\theta\,\nabla\operatorname{Ric}\),
\(\nabla^2\theta\,\operatorname{Ric}\), and
\(|d\theta|^2(\partial_t\operatorname{Ric}
                       +\operatorname{Ric}*\operatorname{Ric})\).
Pointwise smoothing bounds of size \(a/t\) alone give a
nonintegrable majorant near the hypersurface where \(\theta=0\).
These terms explain why positive-time smoothing alone was insufficient.
I53 instead uses a spatially localized flow with the full
\(\mathcal L_{qW}\) term, controls its integrated energy, and
then restores the original collar. It does not use a variable-time
graph or assert that the original metric has bounded curvature.

## 6. Status and classical inputs

The new actual counterexample is registered as X09. The uniform
moving-center and conformal extensions are recorded with I52,
not counted as several separate breakthroughs.

O11, the all-metric coefficient on the balanced family, remains open.
O10, the unrestricted actual weak zero-Weyl endpoint, also remains
open. The present theorem neither supplies a closed endpoint escape
nor rules one out. The continued endpoint equations are maintained
separately in the research record.

Classical inputs used here are the Burns/Schwarzschild recovery
construction and negative Yamabe theory already made explicit in
I52, the elementary harmonic-map identity (3.1), and Hartman's
negative-curvature uniqueness theorem. The core-position obstruction
and its actual balanced diagonal are the conclusions proved here.
No worldwide priority claim follows from this local derivation.

## Appendix A. The exact Schwarzschild donor has no negative gauge mode

The marked obstruction should not be attributed to an unverified
negative mode on the handle donor. Its vector Jacobi quadratic form
can be evaluated directly.

Write the four-dimensional Riemannian scalar-flat Schwarzschild metric as
\[
 g_S=\rho^2(dt^2+\gamma_{S^3}),\qquad
 \rho=2a\cosh t,\quad v=\tanh t,\quad \sigma=\operatorname{sech}^2t .
\]
Its coordinate Ricci components are
\(\operatorname{Ric}_{tt}=-3\sigma\) and
\(\operatorname{Ric}_{ab}=\sigma\gamma_{ab}\).
For a compactly supported vector field set
\[
 \mathcal Q_S(X)=\int
       (|\nabla X|^2-\operatorname{Ric}(X,X))\,dV .
\]
Decompose angular components by scalar gradients and coclosed vector
harmonics on the round unit \(S^3\). For a scalar harmonic \(Y\) with
\(\int Y^2=1\), \(-\Delta_\gamma Y=\lambda Y\),
\(\lambda=l(l+2)\), take
\(X=u(t)Y\partial_t+f(t)\nabla Y\).
Integration by parts in the radial first-derivative terms gives
\[
 \mathcal Q_S(X)=\int\rho^4\{
 u'^2+\lambda f'^2+(\lambda+2\sigma)u^2
       +\lambda(\lambda-4)f^2-4\lambda vuf\}\,dt .
\]
After \(z=\rho^2u\), \(y=\sqrt{\lambda}\rho^2f\), this is
\[
 \int\left\{z'^2+y'^2+
 \left\langle
 \begin{pmatrix}
 \lambda+4&-2\sqrt{\lambda}\,v\\
 -2\sqrt{\lambda}\,v&\lambda-2\sigma
 \end{pmatrix}
 \binom zy,\binom zy\right\rangle\right\}\,dt .          \tag{A.1}
\]
For \(\lambda\ge3\) the matrix minus the identity has nonnegative
diagonal and determinant
\[
       (\lambda-3)(\lambda+3-2v^2)\ge0 .
\]
The radial \(\lambda=0\) block is \(z'^2+4z^2\).
For a coclosed vector harmonic with rough eigenvalue \(\mu\), the
corresponding potential is \(\mu+2-2\sigma\).
Here \(\mu\ge2\): the integrated symmetric-gradient identity on
\(S^3\), with divergence zero and Ricci \(2\gamma\), gives
\(\int|\nabla V|^2\ge2\int|V|^2\).
These blocks exhaust the vector fields. Hence
\[
 \mathcal Q_S(X)\ge\int\rho^{-2}|X|^2\,dV .             \tag{A.2}
\]
Since
\(\operatorname{Ric}(X,X)\le\rho^{-2}|X|^2\), also
\[
 \mathcal Q_S(X)\ge\frac13
       \int(|\nabla X|^2+\rho^{-2}|X|^2)\,dV .         \tag{A.3}
\]
The inequality extends by cutoff density to this finite-energy
space. It excludes a finite-energy kernel or negative mode on the
exact donor. It says nothing about a uniform supremum estimate for
the strain of a gauge through an entire degenerating marked manifold;
Theorem 2 shows why that stronger statement needs different data.


END COMPLETE SOURCE


---

## Source 3: 20260928_intrinsic_caps_and_stability.md

Original path: `continuation/20260928_intrinsic_caps_and_stability.md`

SHA-256: `f4b0ba5966f3e532aa3fc9bbd02328163b6e6da272210414af3ecc834384fde6`

BEGIN COMPLETE SOURCE

# Low-energy matched caps and gauge-free first-order stability

28 September 2026. Continuation of I44 and I52, after the marked-center
construction. All statements below concern actual smooth metrics.

The local construction fills a nearly Euclidean annulus at a cost
controlled by its full curvature energy and its zeroth-order deviation.
It preserves the original outer collar exactly. Applied on sufficiently
long annular ranges, it removes the gauge and scalar-curvature hypotheses
from the lower first-order bound near selected recovery metrics.
It does not parametrize arbitrary near-minimizers.

## 1. A matched cap from zeroth-order closeness and critical energy

Let \(e\) denote the Euclidean metric and
\(\mathcal A=\{1<|x|<4\}\subset\mathbb R^4\).
The curvature norm can use either standard tensor convention; the
universal constants absorb that fixed choice.

**Theorem 1 (small-energy matched cap).**
There are \(a_0,\varepsilon_0,C>0\) such that every smooth metric \(g\)
on \(\mathcal A\) with
\[
 a=\|g-e\|_{L^\infty(e)}\le a_0,\qquad
 E_0=\int_{\mathcal A}|\operatorname{Rm}_g|^2\,dV_g
          \le\varepsilon_0
\]
has a smooth extension \(G\) to \(B_4\), equal to \(g\) on
\(\{7/2<|x|<4\}\), satisfying
\[
 \int_{B_4}|\operatorname{Rm}_G|^2\,dV_G
                         \le C(E_0+a^2).                    \tag{1.1}
\]
There is no derivative bound on the input. No boundary diffeomorphism
is needed. In particular (1.1) bounds the self-dual Weyl cost.

The proof uses a localized Ricci--DeTurck deformation. The metric
is not required to solve any stationary equation. The small
\(C^0\) hypothesis supplies the parabolic and Sobolev control; we
do not invoke curvature-only harmonic-coordinate regularity.

### 1.1 Regularization and a uniform smoothing time

Embed \(B_5\) in a fixed flat torus. Extend \(g\) as
\(g_0=e+\zeta(g-e)\), where \(\zeta\) is supported in \(\mathcal A\)
and equals one on
\[
 \Omega=\{9/8<|x|<15/4\}.
\]
This is a smooth positive extension with the same small supremum
bound. Its curvature away from \(\Omega\) can be arbitrarily large;
no estimate below charges that curvature.

Choose a fixed smooth radial cutoff with
\[
 \operatorname{supp}\chi\subset\{5/4<|x|<13/4\},\qquad
 \chi=1\ \text{on }\{7/4<|x|<9/4\},\qquad 0\le\chi\le1 .
\]
For \(0<\eta<1\), put \(q=\chi^2+\eta^2\), and solve
\[
 \partial_tg_\eta=-2q\,\operatorname{Ric}(g_\eta)
                    +\mathcal L_{qW(g_\eta)}g_\eta,\qquad
 W^k(g)=g^{ab}\Gamma(g)^k_{ab},\qquad g_\eta(0)=g_0.   \tag{1.2}
\]
The background connection is the flat one. The full Lie derivative
\(\mathcal L_{qW}\), not \(q\mathcal L_W\), is important both
for the coordinate equation and the geometric energy identity.
For every fixed \(\eta>0\), this is a smooth strictly parabolic
system. Local existence is the classical DeTurck reduction and
quasilinear parabolic existence theorem.

Here is the uniform continuation estimate needed for the proof.
Write \(u=g_\eta-e\). In flat coordinates (1.2) takes the form
\[
 \partial_tu=q\,g_\eta^{ab}\partial_{ab}u
             +q\,\mathcal Q(g_\eta,Du,Du)
             +Dq\cdot\mathcal B(g_\eta)Du,              \tag{1.3}
\]
with smooth bounded algebraic coefficients while \(|u|\) is small.
Set
\[
 L=\partial_t-qg_\eta^{ab}\partial_{ab},\qquad
 v=|u|_e^2,\qquad w=q|Du|_e^2 .
\]
The fixed cutoff gives
\[
 |Dq|^2/q+|D^2q|\le C_\chi
\]
uniformly in \(\eta\). Differentiating (1.3), using ellipticity
near \(e\), and absorbing mixed Hessian terms by Young's inequality
gives
\[
 Lv\le-cw+Cv,\qquad
 Lw\le-cq^2|D^2u|^2+Cw^2+Cw.                         \tag{1.4}
\]
For clarity, differentiation of the principal coefficient contributes
\(qDq\,Du\,D^2u\) and \(q^2(Du)^2D^2u\). Their costs are bounded
by a fraction of \(q^2|D^2u|^2\) plus \(Cw+Cw^2\).
The differentiated cutoff drift contributes \(D^2q\,w\) and
\((|Dq|/\sqrt q)w^{3/2}\), bounded by the same right side.
No third derivative of \(q\) or input derivative bound is used.
In the first inequality the nonlinear term is \(O(|u|w)\);
choosing \(a_0\) small absorbs it.

Fix \(T>0\) independent of the input, and take \(K>2e^{CT}\).
Then \(v\le a^2e^{Ct}\) while the solution exists. At a spatial
maximum of \(F=w/(Ka^2-v)\), the quotient gradient terms cancel,
and (1.4) implies
\[
 LF\le\{C(Ka^2-v)-c\}F^2+CF
                   \le-c'F^2+CF.                    \tag{1.5}
\]
After reducing \(a_0\), scalar comparison yields
\[
 \|u(t)\|_\infty\le Ca,\qquad
 q|Du(t)|^2\le Ca^2/t\quad(0<t\le T).                \tag{1.6}
\]
The case \(a=0\) is the stationary flat solution.

For fixed \(\eta\), the second estimate is an ordinary gradient bound
on every \([\delta,T]\), because \(q\ge\eta^2\).
Together with uniform ellipticity and small \(\|u\|_\infty\),
smooth parabolic continuation extends this solution to the same
time \(T\). The constants for higher global derivatives may depend
on \(\eta\); that is harmless. On compact subbands where \(\chi=1\),
interior parabolic estimates applied to (1.3) instead give
\[
 \|g_\eta(T)-e\|_{C^2(\{15/8<|x|<17/8\})}\le Ca,     \tag{1.7}
\]
uniformly in \(\eta\). One first uses (1.6) on \([T/2,T]\);
rescaling \(u\) by \(a\) gives bounded coefficients and then the
usual interior bootstrap. This explains the linear dependence on
\(a\) in (1.7), not just a bound independent of the input.

### 1.2 Keeping the actual outer collar

For a fixed smooth \(g_0\), let \(H(s)\) be its ordinary smooth
Ricci--DeTurck flow on its initial existence interval. For
\(\eta^2T\) in that interval, \(h_\eta(t)=H(\eta^2t)\) tends
to \(g_0\) in \(C^\infty\), uniformly for \(0\le t\le T\).
On any collar \(U\) where \(\chi=0\), both \(g_\eta\) and
\(h_\eta\) solve the same \(\eta^2\)-speed DeTurck equation.

Their difference \(z\), initially zero, satisfies
\[
 \partial_t z=\eta^2g_\eta^{ab}\partial_{ab}z
       +\eta^2\mathcal Q(g_\eta,Dz,Dz)
       +\eta^2B_{g_0}Dz+\eta^2C_{g_0}z.               \tag{1.8}
\]
The last two coefficients, also depending algebraically on \(g_\eta,z\),
are bounded by constants of this fixed smooth datum, uniformly for
small \(\eta\); this follows by expanding
\(Dg_\eta=Dh_\eta+Dz\). Smallness of \(z\) absorbs its quadratic
gradient term in the equation for \(|z|^2\). Therefore
\[
 (\partial_t-\eta^2g_\eta^{ab}\partial_{ab})|z|^2
                                      \le C_{g_0}\eta^2|z|^2 .
\]
Exponential barriers from the two boundary components of \(U\)
give, on every smaller collar at distance \(d>0\),
\[
 |z|\le C_{g_0}\exp[-c d^2/(\eta^2t)],\qquad 0<t\le T. \tag{1.9}
\]
For example use barriers \(e^{-\lambda r+C\eta^2\lambda^2t+
C_{g_0}\eta^2t}\) in the radial distance, and optimize \(\lambda\).
Terms from the radial Hessian are absorbed by increasing \(C\).

Interior parabolic estimates on spatial scale \(\eta\sqrt t\),
followed by differentiation on smaller collars, multiply (1.9)
only by powers of \((\eta\sqrt t)^{-1}\).
The rescaled coefficient bounds follow from (1.6) and interior
bootstrapping; the coefficients involving \(h_\eta\) are smooth
for this fixed datum. Thus, for each fixed integer \(m\),
\[
 g_\eta\longrightarrow g_0\quad\hbox{in }C^m
 \text{ on smaller }\{\chi=0\}\text{ collars, uniformly on }[0,T].
                                                               \tag{1.10}
\]
Exponential decay also handles \(t\downarrow0\).
No smooth limit through the degeneracy interface is asserted.
Only collars a positive distance from \(\operatorname{supp}\chi\)
are used.

There is an independent classical check of this collar step.
On a ball inside such a buffer put \(s=\eta^2t\). The rescaled flow
is the ordinary small-\(C^0\) DeTurck flow.
[Schnürer--Schulze--Simon, Theorem 4.4](https://arxiv.org/pdf/0706.0421)
gives interior derivatives up to the initial time, depending on the
fixed smooth initial metric, not on boundary derivatives. Integrating
the local equation gives \(O_{g_0}(\eta^2T)\) convergence in each
fixed interior \(C^m\) norm. This checks the uniform-in-time version
of (1.10); it is not used to assert a global smooth degenerate flow.

### 1.3 Critical energy is retained in the annulus

Put \(E_\eta(t)=\int_\Omega|\operatorname{Rm}(g_\eta)|^2\).
The geometric curvature variation for \(-2q\operatorname{Ric}\)
has the structure
\[
 q\Delta\operatorname{Rm}
 +\nabla q*\nabla\operatorname{Rm}
 +\nabla^2q*\operatorname{Rm}
 +q\operatorname{Rm}*\operatorname{Rm}.
\]
It is the localized Ricci curvature equation of
[Yang, Section 9, equation (9.7)](https://www.numdam.org/item/10.24033/asens.1644.pdf).
Here only that equation is used, not his theorem's additional
\(L^p\) Ricci hypothesis. The Lie derivative in (1.2) contributes
only boundary transport to the integral.

Integrate the \(\nabla^2q\) term by parts. Metric compatibility
then gives, with \(D_\eta=\int_\Omega q|\nabla\operatorname{Rm}|^2\),
\[
 E_\eta'\le-cD_\eta+CE_\eta+
          C\int_\Omega q|\operatorname{Rm}|^3+B_\eta. \tag{1.11}
\]
Every mixed derivative is absorbed using
\(|\nabla q|^2/q\le C\), which follows from the coordinate cutoff
bound and zeroth-order metric equivalence. In particular no bound on the metric Hessian of
\(\chi\) is assumed. Near \(\partial\Omega\), \(q=\eta^2\)
and \(Dq=0\). Equation (1.10), with \(m=3\), bounds all
diffusion and transport fluxes there, so
\[
                         |B_\eta|\le C_{g_0}\eta^2.   \tag{1.12}
\]
Large curvature of the arbitrary extension outside \(\Omega\)
does not enter this inequality.

One may alternatively estimate the Hessian term directly:
\(|\nabla_g^2q|\le C(1+a/\sqrt t)\) by (1.6).
This replaces \(CE_\eta\) in (1.11) by
\(C(1+a/\sqrt t)E_\eta\). Its uniformly integrable time coefficient
gives the same conclusion below, without that integration by parts.

The inhomogeneous Sobolev inequality on the fixed annulus is uniform
because \(g_\eta\) stays uniformly close to \(e\).
Apply it and Kato's inequality to \(\sqrt q|\operatorname{Rm}|\):
\[
 \|\sqrt q|\operatorname{Rm}|\|_4^2
        \le C(D_\eta+E_\eta),\qquad
 \int_\Omega q|\operatorname{Rm}|^3
        \le C\sqrt{E_\eta}(D_\eta+E_\eta).             \tag{1.13}
\]
No zero boundary values are needed in this inhomogeneous inequality.
Choose \(\varepsilon_0\) small and then \(\eta\) small for the
fixed datum. A continuity bootstrap absorbs the first term on
the right of (1.13) into (1.11). Gronwall gives
\[
                     E_\eta(T)\le CE_0+C_{g_0}\eta^2. \tag{1.14}
\]
Both the time and \(C\) are independent of input derivatives.

### 1.4 Finishing the smooth cap

On \(15/8<|x|<17/8\), interpolate from \(e\) on the inside to
\(g_\eta(T)\) on the outside using a fixed smooth cutoff.
Equation (1.7) bounds its full curvature cost by \(Ca^2\).
Use \(e\) further inside and \(g_\eta(T)\) up to radius \(27/8\).

On \(27/8<|x|<7/2\), interpolate back to the original \(g\),
then use \(g\) for \(7/2<|x|<4\). This second collar lies in
the region of (1.10). Its metric converges in \(C^2\) to the
original one for this fixed datum, so its curvature integral
equals the original collar integral plus \(o_\eta(1)\).
Convex interpolation preserves positivity.

The resulting smooth cap has total cost
\[
 C(E_0+a^2)+C_{g_0}\eta^2+o_\eta(1).
\]
If \(E_0+a^2>0\), choose \(\eta\) so that the last errors are at
most \(E_0+a^2\). This choice may depend on every derivative of
the individual input, but the final bound does not. If both
quantities are zero, the input is \(e\) and the flat cap suffices.
This proves Theorem 1.

## 2. Near-Einstein energy supplies the global curvature budget

For a closed oriented four-manifold set
\[
 \mathcal E(g)=\inf_{\lambda\ne0}
   \frac{\int|\operatorname{Ric}_g-\lambda g|^2\,dV_g}{\lambda^2V_g},
 \qquad V_g=\operatorname{Vol}_g(M),
\]
and write
\[
 P=\int|\operatorname{Ric}^{\circ}|^2,\quad
 S=\int s^2,\quad R=P+S/4,\quad
 L_s=S-\frac{(\int s)^2}{V}\ge0 .
\]
In the actual positive-budget family \(R>0\), and
\(\mathcal E=(4P+L_s)/R\). Hence \(P\le\mathcal E R/4\).
The Chern--Gauss--Bonnet identity gives
\[
 8\pi^2\chi
 =\int(|W^+|^2+|W^-|^2)+R/6-2P/3
 \ge(1-\mathcal E)R/6.                               \tag{2.1}
\]
Consequently, if \(\mathcal E<1/2\),
\[
 R\le96\pi^2\chi,\qquad
                   \int|\operatorname{Rm}|^2\le C\chi. \tag{2.2}
\]
The second estimate follows by inserting this bound into the
same identity and the curvature decomposition. These bounds need
neither scalar normalization nor a volume estimate.

On the balanced actual family
\[
 M_j=X_j\# k_j\overline{\mathbb {CP}}^{\,2}
           \#\ell_j(S^1\times S^3),\quad
 A_j=c_1^2(X_j),\quad Q_j=k_j+4\ell_j,\quad 0<h_j=Q_j/A_j\to0,
\]
one has
\(\chi(M_j)=A_j/3+k_j-2\ell_j=O(A_j)\).
Thus every sequence with bounded \(\mathcal E/h_j\) automatically
has full curvature energy \(O(A_j)\).

Here \(X_j\) has its complex orientation and is a finite cover of
the fixed closed complex-hyperbolic surface used in I44/I52.
The blowup and handle class supply is the inherited actual one of
I03, not a formal vector on a cap. Its two classical all-metric
budgets used below are, explicitly,
\[
             S\ge32\pi^2A,\qquad R\ge8\pi^2A(1+h).
\]
They are the scalar and Ricci-energy inequalities detailed in
[I44, Sections 5--6](20260927_covering_geometry_and_sharp_subfamilies.md),
with classical input from [LeBrun](https://arxiv.org/html/math/0003068).
No monopole supply is demanded on the auxiliary capped manifold.

## 3. Long marked annuli force the optimal first-order lower bound

**Theorem 2 (annular first-order stability).**
On the actual family above, suppose that around every marked blowup
core there are \(L_j\) disjoint fixed-ratio annular bands, all core
families mutually disjoint. Each band has marked coordinates,
identifying its filled inside with the corresponding blowdown ball.
It encloses only its designated blowup, not a handle or another core.
Assume, after scaling each band to \(\mathcal A\), that
\[
 \max_{i,\nu}\|g_j-e\|_{C^0(\mathcal A_{i,\nu,j})}
          =a_j\longrightarrow0,\qquad
                         L_jh_j\longrightarrow\infty. \tag{3.1}
\]
Then
\[
                       \liminf_j\frac{\mathcal E(g_j)}{h_j}\ge4.
                                                               \tag{3.2}
\]
There is no scalar, gauge, derivative, or stationary assumption.
Away from these annuli the metric is arbitrary.

**Proof.** If the ratio has no bounded subsequence there is nothing
to prove. On any bounded subsequence, (2.2) supplies total curvature
energy \(O(A_j)\). Choose a minimum-energy band for each blowup.
Their total energy satisfies
\[
                         \sum_i E_{i,j}\le CA_j/L_j.   \tag{3.3}
\]
Call a selected band bad if \(E_{i,j}>\varepsilon_0\), and let
\(b_j\) be the number of bad blowups. Then
\(b_j\le CA_j/(L_j\varepsilon_0)=o(Q_j)\).
Theorem 1 applies to every good band. Replace only those insides
by matched balls; all handles and bad blowups remain unchanged.
The resulting closed manifold is
\(N_j=X_j\#b_j\overline{\mathbb{CP}}^{\,2}
       \#\ell_j(S^1\times S^3)\).
The sum of self-dual Weyl cap costs is
\[
 C_{+,j}\le C\left(A_j/L_j+k_j a_j^2\right)=o(Q_j).    \tag{3.4}
\]
Indeed \(A_j/(L_jQ_j)=1/(L_jh_j)\to0\) and \(k_j\le Q_j\).
No maximum individual energy needs to tend to zero.

The partial-blowdown version of
[I44, Theorem 5](20260927_covering_geometry_and_sharp_subfamilies.md)
retains the cost of the \(b_j\) unremoved blowups. Suppressing \(j\),
the signature formula and the original scalar identity give
\[
 \begin{aligned}
 B_M&=12\pi^2(k-b)+B_N+K_+-C_+,\\
 P_M&=8\pi^2(Q-6b)+(S_M-S_0)/12+4(B_N+K_+-C_+),
 \end{aligned}                                             \tag{3.5}
\]
where \(S_0=32\pi^2A\), \(B_N=\int_N|W_N^-|^2\),
and \(K_+\) is the positive-Weyl energy of the removed cores.
Consequently
\[
\begin{aligned}
 &(1+h)R_M\left(\mathcal E_M-\frac{4h}{1+h}\right)\\
 &\quad=\frac{1-3h}{3}(S_M-S_0)+16(B_N+K_+-C_+)
                 +(1+h)L_s-192\pi^2b .
\end{aligned}                                             \tag{3.6}
\]
The actual scalar/projection budget on \(M\) gives
\(S_M\ge S_0\) and \(R_M\ge8\pi^2A(1+h)\). For \(h\le1/3\)
all terms except the two displayed costs are nonnegative. Hence
\[
 \frac{\mathcal E(g_j)}{h_j}\ge\frac4{1+h_j}
       -\frac{24b_j+2C_{+,j}/\pi^2}{Q_j(1+h_j)^2}.     \tag{3.7}
\]
The two costs are \(o(Q_j)\), proving (3.2).
No conformal reduction occurred.
The cap is an auxiliary smooth metric, so it need not carry
a new monopole solution. The original actual supplier remains
on \(M_j\), exactly as required by I44. QED.

The proof gives a finite, all-metric estimate, not only a sequential
statement. For \(0<h\le1/7\), \(a\le a_0\), \(L\ge1\), and
\(\chi/A\) bounded as on this family,
\[
 \boxed{\mathcal E(g)\ge\frac{4h}{1+h}
                -C\left(\frac1L+\frac{k}{A}a^2\right).} \tag{3.8}
\]
If \(\mathcal E<1/2\), the proof just given applies with
\(b\le CA/(L\varepsilon_0)\), whether or not \(A/L\) is small.
If \(\mathcal E\ge1/2\), (3.8) follows immediately from
\(4h/(1+h)\le1/2\). This explains why the competitive-energy
premise is not an assumption of the result.

There is a useful robustness form. Leave \(r\) marked blowups without
any prescribed annular family, and let \(a_i\) be the maximal amplitude
over the \(L\) bands of each remaining blowup. Discard also those with
\(a_i>a_0\), at most \(a_0^{-2}\sum_i a_i^2\) of them.
The same partial-cap proof gives
\[
 \mathcal E(g)\ge\frac{4h}{1+h}
       -C\left(\frac rA+\frac1L+\frac1A\sum_i a_i^2\right).
                                                               \tag{3.8a}
\]
Thus \(r=o(Q)\), \(\sum_i a_i^2=o(Q)\), and \(Lh\to\infty\)
suffice for (3.2). A maximum amplitude tending to zero at every
core is not necessary. The unstructured regions are retained, not
silently filled, and their number is charged in the identity.

One can average amplitudes over the bands as well. If \(a_{i\nu}\)
is the amplitude of band \(\nu\) at core \(i\), select the band
minimizing \(E_{i\nu}+a_{i\nu}^2\). The sum of selected scores is at
most \(CA/L+L^{-1}\sum_{i,\nu}a_{i\nu}^2\).
Discard scores larger than \(\min\{\varepsilon_0,a_0^2\}\);
the others satisfy both cap hypotheses. Thus (3.8a) improves to
\[
 \mathcal E(g)\ge\frac{4h}{1+h}
       -C\left(\frac rA+\frac1L+
                      \frac1{AL}\sum_{i,\nu}a_{i\nu}^2\right).
                                                               \tag{3.8b}
\]
This is the same partial-cap argument, not a regularity assertion
for the discarded bands.

**Corollary 3 (arbitrary \(C^0\)-small perturbations of selected recoveries).**
The CH shrinking-surgery bases can be selected so that every sequence
of smooth metrics \(g_j\) satisfying
\[
                   \|g_j-g_j^0\|_{L^\infty(g_j^0)}\to0
\]
obeys (3.2). This removes the TT, Bianchi, constant-scalar and
amplitude-rate assumptions from the lower-bound part of I52.

**Proof.** At each fixed \(j\), choose \(L_j\) with \(L_jh_j\to\infty\).
Inside each disjoint CH blowup chart choose a finite annular range
of that many bands, with outer radius so small that the scaled CH
deviation on every band is at most a prescribed \(\varepsilon_j\to0\).
Keep its innermost radius positive at this fixed \(j\), and then
take the actual donor scale sufficiently smaller.
The exterior Yamabe convergence of I52 is uniform on this fixed
finite union, so the normalized recovery is Euclidean-close there.
Choose the donor scales to make that additional error at most
\(\varepsilon_j\), along with all previous recovery selections.
Now take the outer \(j\)-diagonal.

This order of choices matters. No control of the Yamabe factor
on every rescaled donor is inferred from exterior convergence.
For the stated competitors, the annular amplitude in (3.1) is
at most \(C(\varepsilon_j+\|g_j-g_j^0\|_\infty)\), which tends
to zero. Theorem 2 applies. QED.

The statement is invariant under simultaneous pullback. Thus a
competitor which can be made \(C^0\)-close to these bases by any
orientation-preserving diffeomorphism is also covered; no bound on
that diffeomorphism is needed. The compact moving-center selection
from the companion proof remains available by choosing the finite
annular ranges uniformly at each fixed compact configuration set.
The old exact-slice quadratic remainder and equality characterization
remain separate stronger conclusions inside their specified slices.

### 3.1 The minimum over every shrinking zeroth-order neighborhood

This extension determines an actual variational infimum, not only the
energy of a prescribed perturbation. Let \(b_j\to0\) be the maximum
Euclidean error of the selected base on its marked annuli. For small
fixed \(\rho_0>0\), define
\[
 m_j(\rho)=\inf\left\{\frac{\mathcal E(g)}{h_j}:
       g\text{ smooth},\
       \|g-g_j^0\|_{L^\infty(g_j^0)}\le\rho\right\},
 \qquad 0\le\rho\le\rho_0 .
\]
The amplitude on each band is at most
\(b_j+(1+b_j)\rho\). Equation (3.8) and \(k_j\le Q_j\) give
\[
 \frac4{1+h_j}
   -C\left((L_jh_j)^{-1}+(b_j+\rho)^2\right)
 \le m_j(\rho)\le\frac{\mathcal E(g_j^0)}{h_j}.        \tag{3.9}
\]
The right side tends to four by the actual recovery construction.
It follows for every radius sequence \(\rho_j\to0\), with no rate
relative to \(h_j\), that
\[
                         \lim_j m_j(\rho_j)=4.        \tag{3.10}
\]
Also both iterated lower/upper limits as \(\rho\downarrow0\) equal
four. No existence of the inner \(j\)-limit for a fixed positive
\(\rho\) is asserted: (3.9) gives only the interval
\([4-C\rho^2,4]\) in that case.

For the intrinsic distance
\[
 d_j(g)=\inf_{\varphi\in\operatorname{Diff}^+(M_j)}
       \|\varphi^*g-g_j^0\|_{L^\infty(g_j^0)},
\]
approximate the infimum by diffeomorphisms and use invariance of
\(\mathcal E\). The same lower bound holds with \(\rho=d_j(g)\)
whenever this distance is small. In particular, for every fixed
\(\delta>0\), a subsequence satisfying
\(\mathcal E(g_j)/h_j\le4-\delta\) must eventually satisfy
\[
                    d_j(g_j)\ge c\min\{\rho_0,\sqrt\delta\}>0.
                                                               \tag{3.11}
\]
The vanishing \(b_j,(L_jh_j)^{-1},h_j\) errors are absorbed first.
This is separation from the selected recovery orbits, not a
classification of such a putative new geometry. It also does not
prove that every coefficient-four sequence approaches those orbits.
The quadratic error in (3.9) is a proved bound, not a claim of
optimal amplitude dependence.

## 4. What changed and what remains

The matched cap is stronger than the previously requested vanishing
modulus: its cost is quadratic in the zeroth-order amplitude plus
the actual curvature energy. The localized flow does not need to
preserve the gauge fields or converge to an Einstein metric. It
constructs a temporary filling metric used in an exact topological
identity. This distinction avoids imposing unnecessary flow conditions.

The fixed-base exact-gauge obstruction in X09 therefore does not
block the first-order estimate. The intrinsic cap argument covers
arbitrary \(C^0\)-nearby competitors without solving that gauge.
The unrestricted infimum over every metric on \(M_j\) is still
not computed: no theorem here supplies the long Euclidean-close
annuli for all near-minimizers. The general weak zero-Weyl endpoint
is also unchanged.

Classical inputs are DeTurck's strictly parabolic formulation,
smooth parabolic existence and interior estimates, Yang's localized
curvature evolution, and the Sobolev inequality on a fixed annulus.
The localized continuation, collar freezing, matching construction,
and their application to the actual surgery problem are proved
above. This record makes no worldwide priority claim.


END COMPLETE SOURCE
