# A scalar-band remainder for LeBrun's Ricci-energy inequality

23 September 2026. This note concerns the equality geometry of LeBrun's
Proposition 4.1: constant-scalar-curvature Kähler metrics, not necessarily
Einstein metrics. It derives a global smooth self-dual form, a polynomial
Weyl approximation, and differential remainder estimates from that
proposition's defect. No Einstein or trace-free-Ricci bound is assumed.

The weighted-monopole identities underlying the argument were already
derived in [the Round 3 monopole proof](round3_monopole_input.md),
Sections 1–4. Their use below is
different from the Einstein-defect argument: the only small energy is the
LeBrun defect, and the target includes non-Einstein cscK metrics. The added
geometric hypothesis is a two-sided negative scalar-curvature band.

## 1. Statement and conventions

Let \((M,g)\) be a connected closed oriented smooth four-manifold. Fix a
Spin\(^c\) structure with real first Chern class \(a\), and assume that its
ordinary unperturbed Seiberg–Witten equations are solvable for every metric
conformal to \(g\). The class may be selected separately for each metric;
it is held fixed while the conformal weight varies. Set

\[
 p=(a_g^+)^2>0,
 \qquad -S\le s_g\le-s_0<0,
 \qquad S\ge s_0>0.
 \tag{1}
\]

This is a metricwise polarized hypothesis, not the assertion that one
fixed class is a monopole class for all metrics on \(M\).

Use the exterior-algebra norm on forms and the Hilbert–Schmidt operator
norm on \(W^+:\Lambda^+\to\Lambda^+\). All integrals use \(g\). Define

\[
\begin{aligned}
 w&=\sqrt6\,|W^+|, &q&=-s+w, &t&=s+2w, &V&=\operatorname{Vol}_g(M),\\
 D&=\frac1{4\pi^2}\int_M
       \left(\frac{s^2}{24}+\frac{|W^+|^2}{2}\right)-\frac p2,
 &\delta&=144\pi^2D,
 &\Delta&=\int_Mq^2-72\pi^2p,\\
 K&=\frac S{\sqrt{s_0}},
 &C_0&=\left(1+\frac{3S}{2s_0}\right)^2.
\end{aligned}
\tag{2}
\]

Here \(q\ge s_0\). We will prove, not assume, that

\[
 \boxed{\delta=\Delta+\frac12\int_Mt^2,\qquad\Delta\ge0.}
 \tag{3}
\]

**Theorem.** For every \(\eta>0\) there is a smooth positive weight
\(f\), a smooth weighted Seiberg–Witten solution \((A,\Phi)\), and its
smooth self-dual two-form

\[
 D_A\Phi=0,\qquad -iF_A^+=f\sigma(\Phi),\qquad
 \psi=2\sqrt2\,\sigma(\Phi),\qquad
 \rho=|\Phi|^2=|\psi|\le K,
 \tag{4}
\]

such that all the following estimates hold simultaneously. Although
\(\psi\) may vanish, \(\rho=|\Phi|^2\) is smooth, so no nonsmooth norm
derivative is involved:

\[
\begin{aligned}
 \int|d\rho|^2&\le\frac{2\Delta}{27}+\eta,
 &\int|d\psi|^2&\le\frac{2\Delta}{27}+\eta,\\
 \int q\left(\rho-\frac23\sqrt q\right)^2
   &\le\frac{4\Delta}{9}+\eta,
 &\int E_\lambda&\le\frac{2\Delta}{27}+\eta,
\end{aligned}
\tag{5}
\]

where

\[
 E_\lambda=\langle W^+\psi,\psi\rangle+\frac w3\rho^2\ge0.
 \tag{6}
\]

In (5), \(d\psi\) is the exterior derivative, not the covariant
derivative. Define a smooth trace-free symmetric endomorphism of
\(\Lambda^+\) by

\[
 \mathcal B_\psi=\frac{\rho^2}{8}I-\frac38\psi\otimes\psi.
 \tag{7}
\]

Then

\[
 \boxed{
 \int|W^+-\mathcal B_\psi|^2
 \le\frac1{27}\int t^2+
       \left(\frac{C_0}{27}+\frac1{18}\right)\Delta+\eta
 \le\frac{2C_0+7}{54}\,\delta+\eta.}
 \tag{8}
\]

The full covariant derivative satisfies the stronger retained identity
estimate

\[
\begin{aligned}
 \int|\nabla\psi|^2
 &\le\frac{4\Delta}{27}-\frac13\int t\rho^2+\eta\\
 &\le\frac{4\Delta}{27}+
          \frac{K^2}{3}\sqrt{V\int t^2}+\eta\\
 &\le\frac{4\delta}{27}+\frac{K^2}{3}\sqrt{2V\delta}+\eta.
\end{aligned}
\tag{9}
\]

Let \(H\) denote the harmonic self-dual representative of \(a_g^+\),
with the curvature convention
\(\operatorname{proj}_{\mathcal H^+}(iF_A^+)=2\pi H\). There is also
actual harmonic-projection control:

\[
 \left\|\sqrt q\,\psi+4\sqrt2\pi H\right\|_2^2
 \le\frac{4\Delta}{9}+\eta.
 \tag{10}
\]

If \(\lambda_1(g)>0\) is the first positive scalar Laplace eigenvalue,
then

\[
\begin{aligned}
 \int(s-\bar s)^2
 &\le\frac13\int t^2+
       \left(\frac{4C_0}{3}+\frac{2K^2}{\lambda_1(g)}\right)\Delta\\
 &\le\left(\frac23+\frac{4C_0}{3}
                   +\frac{2K^2}{\lambda_1(g)}\right)\delta.
\end{aligned}
\tag{11}
\]

The last estimate is about \(g\) alone and has no \(\eta\): apply the
preceding construction for arbitrarily small \(\eta\). Uniform scalar
oscillation control along degenerating metrics requires control of the
displayed spectral factor; none is implicit here.

If \(D=0\), the weight can be taken exactly as \(f=\sqrt q\), and all
slack terms vanish. The metric is negative cscK, with the complex
structure induced by its nonvanishing positive spinor. No conclusion
\(\operatorname{Ric}^{\circ}=0\) follows.

## 2. Weighted solvability and a derivative-free amplitude bound

For any smooth positive \(f\), solve the ordinary equations for
\(\widehat g=f^{-2}g\). Write \(\beta:S_g^+\to S_{\widehat g}^+\)
for the fiberwise isometric conformal spinor identification. The spinor
on \(g\) is

\[
 \Phi=f^{-3/2}\beta^{-1}\widehat\Phi.
 \tag{12}
\]

Dirac conformal covariance gives \(D_A^g\Phi=0\). As differential
two-forms the unscaled quadratic map obeys
\(\sigma_{\widehat g}(\beta\zeta)=f^{-2}\sigma_g(\zeta)\).
Consequently
\(\sigma_g(\Phi)=f^{-1}\sigma_{\widehat g}(\widehat\Phi)\).
The self-dual splitting of two-forms is conformally invariant, giving
(4). This calculation keeps separate the bundle identification, the
spinor weight, and the two-form weight.

Normalize \(|\sigma(\Phi)|^2=|\Phi|^4/8\). The spinor Weitzenböck
equation is

\[
 4\nabla_A^*\nabla_A\Phi+(s+f\rho)\Phi=0.
 \tag{13}
\]

At a maximum of \(\rho\), this implies \(f\rho\le-s\).
Choose smooth \(f_j\ge\sqrt{s_0}\) converging uniformly to
\(\sqrt q\). Such approximants exist on the fixed compact manifold,
including when \(|W^+|\) is nonsmooth at its zeros. Then every solution
chosen for \(f_j\) has \(\rho_j\le S/\sqrt{s_0}=K\), independently
of all derivatives of \(f_j\).

## 3. Four nonnegative defects and the total remainder

For a smooth weight and its solution define

\[
\begin{aligned}
 D_{\rm amp}&=2\int|d\rho|^2,\\
 D_{\rm quad}&=\int(4\rho|\nabla_A\Phi|^2-|\nabla\psi|^2),\\
 D_H&=\int(|d\psi|^2+|d^*\psi|^2)=2\int|d\psi|^2,\\
 D_{\rm eig}&=2\int E_\lambda,
 \qquad D_0=D_{\rm amp}+D_{\rm quad}+D_H+D_{\rm eig}.
\end{aligned}
\tag{14}
\]

Each term is nonnegative. For \(D_{\rm quad}\), the quadratic map is
the parallel Hopf map, whose differential satisfies

\[
 |d\psi_z(v)|^2
 =4|z|^2|v|^2-4(\operatorname{Im}\langle z,v\rangle)^2
 \le4|z|^2|v|^2.
 \tag{15}
\]

For \(D_{\rm eig}\), the least eigenvalue of a trace-free symmetric
three-by-three matrix is at least
\(-\sqrt{2/3}|W^+|=-w/3\).

Pair (13) with \(\rho\Phi\) and integrate by parts:

\[
 2\int|d\rho|^2+4\int\rho|\nabla_A\Phi|^2
          +\int s\rho^2+\int f\rho^3=0.
 \tag{16}
\]

The self-dual two-form Weitzenböck formula reads

\[
 D_H=\int\left(|\nabla\psi|^2+\frac s3\rho^2
                    -2\langle W^+\psi,\psi\rangle\right).
 \tag{17}
\]

Combining (16) and (17) gives the exact identity

\[
 D_0=\int\left(\frac23q\rho^2-f\rho^3\right).
 \tag{18}
\]

Let \(u=3\rho/2\) and

\[
 \begin{aligned}
 P&=\int(qu^2-fu^3)=\frac{27}{8}D_0,&
 X&=\left(\int q^3f^{-2}\right)^{1/3},\\
 Y&=\left(\int f^4\right)^{1/3},&
 Z&=\int fu^3,\qquad C=\int f^2u^2.
 \end{aligned}
 \tag{19}
\]

Hölder gives two nonnegative remainders

\[
 H_1=XZ^{2/3}-\int qu^2,\qquad H_2=YZ^{2/3}-C.
 \tag{20}
\]

Hodge orthogonality and the actual curvature equation give

\[
 C=18\|F_A^+\|_2^2=72\pi^2p+18J,
 \qquad J=\|iF_A^+-2\pi H\|_2^2.
 \tag{21}
\]

Here \(p>0\) implies \(Z>0\). Direct factorization yields

\[
 YX^2-72\pi^2p
 =18J+H_2+
       Y\frac{X+Z^{1/3}}{Z^{2/3}}(P+H_1).
 \tag{22}
\]

First suppose \(f=\sqrt q\) is smooth. Put
\(E=\int q^2\), \(\theta=(Z/E)^{1/3}\). Then
\(X=Y=E^{1/3}\), \(H_1=H_2=H\), and \(0<\theta\le1\).
Thus

\[
 \Delta=18J+H+\frac{1+\theta}{\theta^2}(P+H),
 \qquad
 J\le\frac\Delta{18},\quad
 P\le\frac\Delta2,\quad
 D_0\le\frac{4\Delta}{27}.
 \tag{23}
\]

This proves the differential and eigenvalue assertions in (5).

For amplitude control use the probability measure
\(d\nu=q^2d\mu/E\), set \(r=u/\sqrt q\), and write
\(c=\int r^2d\nu\), \(z=\int r^3d\nu\), \(m=\int r\,d\nu\).
The inequalities above imply \(z\le c\le z^{2/3}\), so \(c\le1\).
Cauchy–Schwarz gives \(c^2\le mz\le mc\), hence \(m\ge c\).
Therefore

\[
 \int q(u-\sqrt q)^2=E(c-2m+1)\le E-C\le\Delta.
 \tag{24}
\]

Finally \(f\psi=-2\sqrt2\,iF_A^+\); (21) gives (10).

For the general approximants \(f_j\), (18)–(22) remain exact. Their
left side in (22) tends to \(\Delta\). If
\(\vartheta_j=Z_j^{1/3}/X_j\), then
\(0<\vartheta_j\le1\) and the last coefficient is at least
\(2Y_j/X_j\to2\). Hence (23) holds with errors tending to zero.
For (24), retain the fixed measure \(q^2d\mu/E\). Uniform convergence
of the weights and \(u_j\le3K/2\) give
\(z_j\le c_j+o(1)\), while Hölder still gives
\(c_j\le z_j^{2/3}\). Moreover
\(c_j\ge72\pi^2p/E-o(1)>0\). It follows that
\(c_j\le1+o(1)\) and \(m_j\ge c_j-o(1)\), proving (24) with
vanishing error. Harmonic-projection control follows in the same way
from the exact curvature equation. Choose a single sufficiently large
\(j\) to make every error below any prescribed allowance.

No convergence of spinors, uniform derivative bounds for the weights,
or common smoothing rate along varying geometries is used. All asserted
forms are smooth actual weighted-monopole forms, not formal algebraic
choices of a Weyl eigenline.

## 4. The defect split and polynomial Weyl approximation

The pointwise scalar identity is

\[
 \frac{s^2}{24}+\frac{|W^+|^2}{2}
 =\frac{q^2}{36}+\frac{t^2}{72}.
 \tag{25}
\]

Integration gives (3); \(\Delta\ge0\) was established in (22)–(23).

For any \(\psi\), without assuming it is an eigenvector or is nonzero,
trace-freeness of \(W^+\) gives

\[
 \boxed{
 |W^+-\mathcal B_\psi|^2
  =\frac16\left(w-\frac34\rho^2\right)^2
                         +\frac34E_\lambda.}
 \tag{26}
\]

For example, \(|\mathcal B_\psi|^2=3\rho^4/32\) and
\(-2\langle W^+,\mathcal B_\psi\rangle
=3\langle W^+\psi,\psi\rangle/4\); completing the square proves
(26). This avoids eigenline choices and division by spectral gaps.

Set \(a_0=q-u^2\). Because \(q\ge s_0\) and \(u\le3K/2\),

\[
 \int a_0^2
 \le C_0\int q(u-\sqrt q)^2\le C_0\Delta+\eta.
 \tag{27}
\]

The relation \(w-3\rho^2/4=(t+a_0)/3\), (26), (27), and (5)
give (8). All approximation errors can be decreased in advance to
absorb their fixed coefficients into the displayed \(\eta\).

## 5. Covariant derivative, scalar oscillation, and equality

Rearranging (17) using (6) yields the exact identity

\[
 \int|\nabla\psi|^2=D_H+D_{\rm eig}-\frac13\int t\rho^2.
 \tag{28}
\]

The two nonnegative terms on the right are bounded jointly by \(D_0\),
not merely separately. Equations (23), (3), and Cauchy–Schwarz prove
(9). In particular the unconditional conclusion has order
\(\delta+\sqrt{V\delta}\) with the displayed scalar-band factor;
it is not a linear \(C\delta\) estimate. If the additional sign
\(t\ge0\) holds, (28) does give
\(\int|\nabla\psi|^2\le4\Delta/27+\eta\).

To prove (11), Poincaré and \(0\le\rho\le K\) give

\[
 \int(\rho^2-\bar\rho^{\,2})^2
 \le4K^2\int(\rho-\bar\rho)^2
 \le\frac{8K^2}{27\lambda_1(g)}\Delta+\eta.
 \tag{29}
\]

Use
\(s=t/3-3\rho^2/2-2a_0/3\), subtract the constant
\(-3\bar\rho^{\,2}/2\), and apply
\((x+y+z)^2\le3(x^2+y^2+z^2)\). The mean \(\bar s\) minimizes
the squared scalar error over constants. Equations (27) and (29) give
(11) after letting the auxiliary allowance tend to zero.

When \(\delta=0\), (3) gives \(t=0\), so
\(w=-s/2>0\) and \(q=-3s/2\) are smooth. Use the exact weight
\(\sqrt q\). Now \(D_0=0\), \(d\rho=0\),
\(\rho=2\sqrt q/3>0\), and (28) gives \(\nabla\psi=0\).
Thus \(\sqrt2\psi/\rho\) is a parallel self-dual form of norm
\(\sqrt2\), defining a Kähler structure with the chosen orientation.
Its scalar curvature is constant and negative. The everywhere nonzero
positive spinor gives the compatible Spin\(^c\) structure. This is the
classical equality geometry, now visible directly in the retained
defects.

An unequal-curvature product of closed hyperbolic surfaces is an
essential check. With factor curvatures \(-\alpha,-\beta\),
\(\alpha,\beta>0\), its compatible Kähler class has
\(p=(\alpha+\beta)^2V/(8\pi^2)\), whereas
\(s=-2(\alpha+\beta)\), \(w=\alpha+\beta\), and \(D=0\).
But \(|\operatorname{Ric}^{\circ}|^2=(\alpha-\beta)^2\), which
need not vanish. Therefore this theorem supplies no unqualified
Einstein or trace-free-Ricci remainder.

## 6. Supplying a second-order budget

The preceding theorem has no second-order hypothesis. Such a budget can
also be obtained if one supplies integral Ricci and determinant-curvature
control. This step uses the bundle Hessian estimate established in
`round4_rigidity.md`, Section 2, and rederived in `round21_analytic.md`,
Section 2:

\[
\begin{aligned}
 \|\nabla^2u\|_2^2
 &\le2\|\nabla^*\nabla u\|_2^2
       +32\|u\|_\infty^2\|\operatorname{Ric}\|_2^2
       +33\|u\|_\infty^2\|\mathscr F\|_2^2,\\
 \|\nabla u\|_4^2&\le4\|u\|_\infty\|\nabla^2u\|_2.
\end{aligned}
\tag{30}
\]

Here \(\mathscr F\) is the compatible bundle connection curvature,
with component norm \(\sum_{ij}|\mathscr F_{ij}|_{\rm HS}^2\).
Equation (30) is an integration-by-parts estimate on a closed manifold;
it assumes no Sobolev constant or differentiated-curvature bound.

**Second-order corollary.** In addition to (1), assume

\[
 \fint|\operatorname{Ric}|^2\le R_0,\qquad
 \frac{(-a^2)_+}{V}\le A_0,\qquad
 \frac D V\le D_0^*.
 \tag{31}
\]

For every allowance \(\eta>0\), the solution in the theorem may be
chosen so that it also satisfies

\[
 \boxed{\fint\bigl(|\nabla^2\psi|^2+|\Delta_H\psi|^2\bigr)
       \le C(S,s_0,R_0,A_0,D_0^*).}
 \tag{32}
\]

The constant is independent of volume, injectivity radius, Sobolev
constants, and derivatives of the approximating weight.

**Proof.** To make the dependence explicit, put

\[
 H_W=\frac{S^2+288\pi^2D_0^*}{12},\qquad
 Q_1=S+\sqrt{6H_W}.
 \tag{33}
\]

Since \(w=(t-s)/2\), (3) gives
\(\fint|W^+|^2\le H_W\) and \(\fint q\le Q_1\).
Choose the smooth approximants sufficiently close that
\(f_j^2\le q+s_0\), in addition to \(f_j\ge\sqrt{s_0}\).
The weighted curvature equation and \(\rho\le K\) give

\[
 \fint|F_A^+|^2\le\frac{K^2}{8}(Q_1+s_0),\qquad
 \fint|F_A|^2
 =2\fint|F_A^+|^2-\frac{4\pi^2a^2}{V}
 \le\frac{K^2}{4}(Q_1+s_0)+4\pi^2A_0.
 \tag{34}
\]

The curvature of the positive-spinor connection satisfies the
dimensional representation estimate

\[
 |\mathscr F^{S^+}|^2
 \le C\bigl(|W^+|^2+s^2+|\operatorname{Ric}^{\circ}|^2
                                      +|F_A|^2\bigr).
 \tag{35}
\]

The \(W^-\) block acts trivially on the positive-spin representation;
it does not enter this estimate. Hence its normalized integral is
bounded by a constant depending only on the parameters in (31).
Equation (13) and \(|\Phi|^2\le K\) give

\[
 \fint|\nabla_A^*\nabla_A\Phi|^2
 \le\frac K8\left[S^2+K^2(Q_1+s_0)\right].
 \tag{36}
\]

Apply (30) to \(\Phi\), whose supremum norm is at most \(\sqrt K\).
Equations (31), (35), and (36) bound
\(\fint|\nabla_A^2\Phi|^2\). The second inequality in (30) then
gives

\[
 \fint|\nabla_A\Phi|^4
 \le16K\,\fint|\nabla_A^2\Phi|^2.
 \tag{37}
\]

Twice differentiating the parallel quadratic map, rather than
differentiating its PDE or the weight, gives

\[
 |\nabla^2\psi|^2
 \le C\bigl(K|\nabla_A^2\Phi|^2+|\nabla_A\Phi|^4\bigr).
 \tag{38}
\]

Finally use
\(\Delta_H\psi=\nabla^*\nabla\psi+(s/3)\psi-2W^+\psi\),
\(|\nabla^*\nabla\psi|^2\le4|\nabla^2\psi|^2\), and
\(|\psi|\le K\). This proves (32). The bounds hold uniformly for
all sufficiently close approximants, so selecting one that meets the
first-order allowances causes no further loss. In particular the
proof never assumes a bound on \(df_j\).

## 7. The realizable negative-Einstein Weyl branch

The same actual form supplies the *allowed* branch in the
[Round 21 two-form criterion](round21_analytic.md). This is a form-production result,
not an additional Einstein obstruction.

Set

\[
 \omega=\frac{\sqrt3}{2}\psi,\qquad
 A_{\omega,1/2}=\frac12
       \left(\frac{|\omega|^2}{3}I-\omega\otimes\omega\right)
       =\mathcal B_\psi,
 \qquad r=\fint|\operatorname{Ric}+g|^2.
 \tag{39}
\]

Writing \(e=s+4\) and retaining \(a_0=q-9\rho^2/4\), one has the
exact amplitude identity

\[
 |\omega|^2-2=\frac t6-\frac e2-\frac{a_0}{3}.
 \tag{40}
\]

Since \(|e|^2\le4|\operatorname{Ric}+g|^2\), it follows that

\[
 \int(|\omega|^2-2)^2
 \le\frac1{12}\int t^2+3\int|\operatorname{Ric}+g|^2
                                  +\frac{C_0}{3}\Delta+\eta.
 \tag{41}
\]

Consequently the zeroth-order calibration defect obeys

\[
\begin{aligned}
 d_{1/2}
 &:={\fint}\left(|\operatorname{Ric}+g|^2
       +|W^+-A_{\omega,1/2}|^2+(|\omega|^2-2)^2\right)\\
 &\le4r+\frac{13}{108V}\int t^2
       +\left(\frac{10C_0}{27}+\frac1{18}\right)\frac\Delta V
       +\eta\\
 &\le4r+\frac{10C_0+8}{27}\frac\delta V+\eta.
\end{aligned}
\tag{42}
\]

Here the free approximation allowance was chosen to be \(\eta V\)
before division by volume. Under (31), (32) also provides
\(\fint|\Delta_H\omega|^2\le C(S,s_0,R_0,A_0,D_0^*)\).
Thus both the bounded calibration and its second-order source budget
are supplied by actual monopole equations.

A common sufficient condition for the negative-square budget is

\[
 a^2\ge T:=2\chi(M)+3\tau(M).
 \tag{43}
\]

It must be verified for the selected class; it does not follow merely
from conformal-class solvability. With the current norm conventions,
Chern–Weil gives

\[
 4\pi^2T=\int\left(2|W^+|^2+\frac{s^2}{24}
                                  -\frac{|\operatorname{Ric}^{\circ}|^2}{2}\right),
 \qquad
 \frac{(-a^2)_+}{V}\le\frac r{8\pi^2}.
 \tag{44}
\]

Also \(\fint|\operatorname{Ric}|^2\le8+2r\). Therefore, in a fixed
scalar band, bounds on \(r\) and \(D/V\), together with (43), are
sufficient for all the budgets in this corollary. There is no separate
uncontrolled negative-square parameter in that special application.

At \(r=D=0\), the form has norm \(\sqrt2\), is parallel, and yields
the Kähler–Einstein Weyl amplitude \(t_{\rm branch}=1/2\) in the
notation of Round 21. This branch is realizable. For small positive
defects, the argument yields the displayed form and curvature estimates,
not a global metric correction to an exact Einstein metric.

## 8. Scaling, relation to prior results, and use

Under \(g\mapsto cg\), the quantities \(s,w,q,S,s_0\) scale by
\(c^{-1}\), \(K\) by \(c^{-1/2}\), \(V\) by \(c^2\), and
\(\lambda_1\) by \(c^{-1}\). The numbers
\(\delta,\Delta,C_0,K^2\sqrt V,K^2/\lambda_1\) are unchanged.
Transporting the weighted solution rescales its differential two-form
\(\psi\) by \(c^{1/2}\), consistently with every displayed energy.

The theorem requires neither \(W^-\) control nor a uniform Sobolev,
injectivity-radius, volume, or diameter bound. It does require the
scalar band and actual weighted-monopole solvability. These hypotheses
are not consequences of merely specifying a cohomology vector.

Relative to Round 17, the new control parameter is \(D_{LB}\) alone:
it retains the full cscK equality set and uses no Ricci-error input.
Relative to `round21_analytic.md`, the form here is produced by actual
monopole equations. Sections 6–7 state the additional hypotheses that
supply its Hodge-Laplacian budget; the first-order theorem alone must not
be used as if that budget were automatic. Pointwise near-negative-Einstein
metrics provide a scalar band, but small LeBrun defect remains a separate
condition to be established.

The useful new remainder is (8), together with the actual global form
and its differential controls (5), (9), and (10). It does not assert
closeness of metrics to a global Kähler metric, compactness of a
degenerating family, or exclusion of all Einstein metrics on the smooth
manifold. Those statements require additional arguments.

### Sources

- Claude LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten
  Theory*, Proposition 4.1 and Proposition 4.2,
  [original paper](https://arxiv.org/abs/math/0003068).
- Claude LeBrun, *Four-manifolds, curvature bounds, and convex geometry*,
  Lemma 3.7, [weighted equations](https://arxiv.org/abs/math/0611450).
- `round3_monopole_input.md`, Sections 1–4: quadratic-map normalization,
  four retained defects, Hölder remainders, and smooth approximation.
- `round17_integral.md`: earlier arbitrary-scalar structural estimates
  with different curvature/Ricci and topological error inputs.
- The scalar-band hypotheses, cscK polynomial fit, and estimates
  (8)–(11) are established in this note. The finite symbolic check
  `line1_scalar_band_check.py` checks algebra and the unequal-product
  calibration; it does not verify weighted solvability or the analytic
  existence hypothesis.
