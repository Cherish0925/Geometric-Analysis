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
