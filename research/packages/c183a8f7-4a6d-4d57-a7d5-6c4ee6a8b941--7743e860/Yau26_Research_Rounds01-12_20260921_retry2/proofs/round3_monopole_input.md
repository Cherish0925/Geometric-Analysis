# Quantified monopole inequalities and a bounded Weyl model

19 September 2026. This note derives the monopole input to
`round3_rigidity.md` independently of the live Skill and research Session.
The foundational input is an actual Seiberg--Witten monopole class;
the scalar and two-form Weitzenbock identities are stated with their
normalizations below. No Einstein condition is assumed.

## 1. Conventions and rescaled solvability

Let (M,g) be a closed oriented smooth four-manifold, with a spin-c
structure of determinant line L and class \(a=c_1(L)\). Assume that the
ordinary, unperturbed Seiberg--Witten equations for this structure have
a solution for every metric conformal to g. An actual monopole class,
with solutions for every metric, supplies this hypothesis. In applications
where the class is obtained from a Seiberg--Witten invariant, all
nonvanishing and chamber hypotheses must be verified separately.

Write H for the real harmonic self-dual representative of \(a^+\),
normalized by

\[
 p=\|H\|_2^2=(a^+)^2>0,
 \qquad \operatorname{proj}_{\mathcal H^+}(iF_A^+)=2\pi H.
                                                               \tag{1}
\]

Two-forms have their usual exterior-algebra norm. The Weyl operator
\(W^+:\Lambda^+\to\Lambda^+\) has its operator Hilbert--Schmidt norm.
For the quadratic spinor map use

\[
 |\sigma(\Phi)|^2=|\Phi|^4/8,\qquad
 \psi=2\sqrt2\sigma(\Phi),\qquad
 \rho=|\Phi|^2=|\psi|.
\]

For every smooth positive function f one has a solution on g of

\[
 D_A\Phi=0,\qquad -iF_A^+=f\sigma(\Phi).                    \tag{2}
\]

To verify this, solve the ordinary equations for
\(\widehat g=f^{-2}g\). Under the canonical identification of spinor
bundles, conformal covariance gives
\(\Phi=f^{-3/2}\widehat\Phi\) and
\(D_A^g\Phi=0\). As differential two-forms,
\(\sigma_g(\Phi)=f^{-1}\sigma_{\widehat g}(\widehat\Phi)\).
The self-dual splitting of two-forms is conformally invariant, proving
(2). This is the rescaling used in
[LeBrun, Lemma 3.7](https://arxiv.org/abs/math/0611450).

The normalized spinor and two-form Weitzenbock formulas are

\[
 4\nabla_A^*\nabla_A\Phi+(s+f\rho)\Phi=0,                    \tag{3}
\]
\[
 \|d\psi\|_2^2+\|d^*\psi\|_2^2
 =\int\left(|\nabla\psi|^2+\frac{s}{3}\rho^2
                     -2\langle W^+\psi,\psi\rangle\right).  \tag{4}
\]

The quadratic map is parallel. In a unitary spin frame it is the Hopf
map \(z\mapsto(2\operatorname{Re}(z_1\bar z_2),
2\operatorname{Im}(z_1\bar z_2),|z_1|^2-|z_2|^2)\), up to an
orthogonal change in \(\Lambda^+\). Its differential satisfies

\[
 |d\psi_z(v)|^2
 =4|z|^2|v|^2-4\bigl(\operatorname{Im}\langle z,v\rangle\bigr)^2
 \le4|z|^2|v|^2.                                           \tag{5}
\]

Thus the quadratic-map defect used below is nonnegative pointwise.

## 2. Retaining all four differential defects

Put \(u_W=|W^+|\), \(\alpha=\sqrt{2/3}u_W\), and
\(q=-s+\sqrt6u_W=-s+3\alpha\). For this section assume q is positive.
Define

\[
\begin{aligned}
 D_{\rm amp}&=2\int|d\rho|^2,\\
 D_{\rm quad}&=\int(4\rho|\nabla_A\Phi|^2-|\nabla\psi|^2),\\
 D_{\rm H}&=\int(|d\psi|^2+|d^*\psi|^2),\\
 D_{\rm eig}&=2\int\bigl(\langle W^+\psi,\psi\rangle
                                      +\alpha\rho^2\bigr),
 \qquad D_0=D_{\rm amp}+D_{\rm quad}+D_{\rm H}+D_{\rm eig}.
\end{aligned}                                               \tag{6}
\]

All terms are nonnegative. For the last, the smallest eigenvalue of a
trace-free symmetric three-by-three operator satisfies
\(\lambda_{\min}\ge-\sqrt{2/3}|W^+|=-\alpha\): if that eigenvalue
is w, the other two sum to -w and contribute at least \(w^2/2\) to
the squared norm, so \(|W^+|^2\ge3w^2/2\).

Pair (3) with \(\rho\Phi\) and integrate. Since
\(d\rho=2\operatorname{Re}\langle\nabla_A\Phi,\Phi\rangle\),

\[
 2\int|d\rho|^2+4\int\rho|\nabla_A\Phi|^2
                  +\int s\rho^2+\int f\rho^3=0.             \tag{7}
\]

Combine (7) with (4), then add the eigenvalue defect. This gives the
exact identity

\[
 D_0=\int\left(\frac23q\rho^2-f\rho^3\right).
\]

Write \(\varphi=3\psi/2\), \(u=|\varphi|=3\rho/2\). Then

\[
 P_f:=\int(qu^2-fu^3)=\frac{27}{8}D_0\ge0.                  \tag{8}
\]

## 3. Two Holder inequalities and the exact total deficit

For any smooth positive f define

\[
 X=\left(\int q^3f^{-2}\right)^{1/3},\quad
 Y=\left(\int f^4\right)^{1/3},\quad
 Z=\int fu^3,\quad C=\int f^2u^2,
\]
\[
 H_1=XZ^{2/3}-\int qu^2\ge0,\qquad
 H_2=YZ^{2/3}-C\ge0.
\]

The first is Holder applied to
\((q^3f^{-2})^{1/3}(fu^3)^{2/3}\); the second uses
\((f^4)^{1/3}(fu^3)^{2/3}\). Since p>0 the spinor cannot vanish
identically: otherwise \(F_A^+=0\), contradicting (1). Thus Z>0.

Let \(J_A=\|iF_A^+-2\pi H\|_2^2\). Hodge orthogonality, together
with \(f\varphi=-3\sqrt2\,iF_A^+\), gives

\[
 C=18\|F_A^+\|_2^2=72\pi^2p+18J_A.                       \tag{9}
\]

Because \(P_f+H_1=Z^{2/3}(X-Z^{1/3})\), straightforward factorization
now yields the exact decomposition

\[
 YX^2-72\pi^2p
 =18J_A+H_2+Y\frac{X+Z^{1/3}}{Z^{2/3}}(P_f+H_1).         \tag{10}
\]

The right side is a sum of nonnegative quantities.

For the optimal weight \(f=\sqrt q\), initially treating it as smooth,
put

\[
 \mathcal E=\int q^2,\qquad
 \Delta=\mathcal E-72\pi^2p,\qquad
 \theta=(Z/\mathcal E)^{1/3}.
\]

Now \(X=Y=\mathcal E^{1/3}\), \(H_1=H_2=:H\), and
\(P_f+H\ge0\) implies \(0<\theta\le1\). Equation (10) becomes

\[
 \Delta=18J_A+H+\frac{1+\theta}{\theta^2}(P_f+H).
\]

Since the last coefficient is at least two,

\[
 \boxed{\quad J_A\le\Delta/18,\quad P_f\le\Delta/2,
 \quad H\le\Delta/3,\quad D_0\le4\Delta/27.\quad}          \tag{11}
\]

In particular \(\Delta\ge0\). Self-duality implies
\(|d^*\psi|=|d\psi|\), so

\[
 \|d\rho\|_2^2\le2\Delta/27,
 \qquad\|d\psi\|_2^2\le2\Delta/27.                        \tag{12}
\]

## 4. Amplitude and harmonic projection

Use the probability measure \(d\nu=f^4d\mu/\mathcal E\) and
\(r=u/f\). Write \(c=\int r^2d\nu=C/\mathcal E\),
\(z=\int r^3d\nu=Z/\mathcal E\), and \(m=\int r\,d\nu\).
Equations (8) and Holder give \(z\le c\le z^{2/3}\), hence
\(0<c\le1\). Another Cauchy--Schwarz inequality gives
\(c^2\le mz\le mc\), so \(m\ge c\). Therefore

\[
 \int f^2(u-f)^2
 =\mathcal E(c-2m+1)
 \le\mathcal E-C=\Delta-18J_A\le\Delta.                    \tag{13}
\]

The sign and normalization in (9) also give

\[
 \|f\varphi+6\sqrt2\pi H\|_2^2=18J_A\le\Delta.           \tag{14}
\]

Combining (13) and (14) with the reverse triangle inequality for norms,

\[
 \left\||2\pi H|-\frac{q}{3\sqrt2}\right\|_2
 \le2\sqrt{\Delta/18},\qquad
 \left\||H|-\frac{q}{6\sqrt2\pi}\right\|_2^2
 \le\frac{\Delta}{18\pi^2}.                              \tag{15}
\]

### Smooth approximation of the optimal weight

The function \(|W^+|\), and hence \(\sqrt q\), need not be smooth.
In the application \(q\ge3\), \(-s\le5\). Choose smooth positive
\(f_j\ge\sqrt3\) converging uniformly to \(\sqrt q\) and solve (2).
At a maximum of \(\rho_j\), (3) gives
\(f_j\rho_j\le-s\). Consequently \(\rho_j\le5/\sqrt3<3\),
uniformly in j. This bound is independent of derivatives of f_j.

All identities (6)--(10) hold exactly for these solutions.
Their left side in (10) tends to \(\Delta\). Moreover, if
\(\vartheta_j=Z_j^{1/3}/X_j\), then \(0<\vartheta_j\le1\) and

\[
 Y_j\frac{X_j+Z_j^{1/3}}{Z_j^{2/3}}
 =\frac{Y_j}{X_j}\frac{1+\vartheta_j}{\vartheta_j^2}
 \ge2\frac{Y_j}{X_j}\longrightarrow2.
\]

This proves (11)--(12) with errors tending to zero without requiring
spinor convergence; the two Holder remainders differ by o(1), because
\(X_j-Y_j\to0\), \(f_j^2-q\to0\) uniformly, and \(u_j\) is bounded.
For (13), evaluate the moments instead with the
fixed optimal weight \(\sqrt q\) and the variable bounded \(u_j\).
Uniform convergence and (8) give \(z_j\le c_j+o(1)\);
Holder still gives \(c_j\le z_j^{2/3}\). Thus \(c_j\le1+o(1)\).
Since \(c_j\ge72\pi^2p/\mathcal E-o(1)>0\),
\(m_j\ge c_j^2/z_j\ge c_j-o(1)\). The same calculation yields
(13) with an o(1) error. Replacing \(\sqrt q\) by f_j changes the
integrals by o(1), by the amplitude bound on this fixed compact metric.

The projected-curvature identity (14) is exact for f_j before applying
the deficit bound. Thus (13)--(15) hold with arbitrarily small errors.
In statements below one can make the sum of all such errors at most
any prescribed \(\eta>0\). This is done separately on each manifold;
it does not require a common approximation rate along varying geometries.

## 5. Eigenline alignment on any controlled spectral region

Let \(\lambda_1\le\lambda_2\le\lambda_3\) be the eigenvalues of W+.
On a measurable region U where \(\lambda_2-\lambda_1\ge\gamma>0\),
let \(\Pi\) project onto the lowest eigenline. Since
\(\lambda_1+\alpha\ge0\),

\[
 \langle W^+\psi,\psi\rangle+\alpha\rho^2
 =\sum_j(\lambda_j+\alpha)|\psi_j|^2
 \ge\gamma|(I-\Pi)\psi|^2.
\]

Equations (6) and (11) imply

\[
 \int_U|(I-\Pi)\psi|^2\le\frac{2\Delta}{27\gamma}+\eta,
 \qquad
 \int_U|(I-\Pi)\varphi|^2\le\frac{\Delta}{6\gamma}+\eta.   \tag{16}
\]

If also \(q\le F_*^2\) on U, (14) and a two-term squared triangle
inequality imply, after making the approximation arbitrarily accurate,

\[
 \int_U|(I-\Pi)H|^2
 \le\left(\frac1{36\pi^2}
                 +\frac{F_*^2}{216\gamma\pi^2}\right)\Delta. \tag{17}
\]

No derivative or global orientation of the eigenline is asserted.

## 6. The lowest-eigenvalue curvature integral

This subsection does not require q>0 or scalar negativity. Set

\[
 w=\lambda_{\min}(W^+),\qquad b=2s/3+2w,
 \qquad h=(-b)_+=\max(-b,0).
\]

Omit \(D_{\rm eig}\) from (6). Equations (4) and (7) then give

\[
 0\le D_{\rm amp}+D_{\rm quad}+D_{\rm H}
 =\int\left(-\frac23s\rho^2
                 -2\langle W^+\psi,\psi\rangle-f\rho^3\right).
\]

Since \(\langle W^+\psi,\psi\rangle\ge w\rho^2\),

\[
 \int f\rho^3\le\int(-b)\rho^2\le\int h\rho^2.           \tag{18}
\]

Choose any smooth positive \(q_\epsilon\ge h\) converging uniformly
to h, and solve the rescaled equations with
\(f_\epsilon=\sqrt{q_\epsilon}\). Put
\(C_\epsilon=\int f_\epsilon^2\rho^2\),
\(Z_\epsilon=\int f_\epsilon\rho^3\), and
\(Q_\epsilon=\int f_\epsilon^4\). Equations (1)--(2) give

\[
 32\pi^2p\le8\|F_A^+\|_2^2=C_\epsilon,
 \qquad Z_\epsilon\le C_\epsilon.
\]

Holder yields
\(C_\epsilon\le Q_\epsilon^{1/3}Z_\epsilon^{2/3}
\le Q_\epsilon^{1/3}C_\epsilon^{2/3}\). Since p>0,
division proves \(C_\epsilon\le Q_\epsilon\). Letting epsilon tend
to zero proves, with \(x_-=\min\{x,0\}\),

\[
 \boxed{\quad
 \int(2s/3+2w)_-^2\ge32\pi^2p.\quad}                      \tag{19}
\]

This argument is valid even when h vanishes; no uniform spinor bound
is needed for this particular limiting step. If s<0, then w<=0 and
b<0, so (19) is exactly
\(\int(2s/3+2w)^2\ge32\pi^2p\). It is the lowest-eigenvalue
estimate appearing in the proof of
[LeBrun's Theorem 2.3](https://arxiv.org/abs/math/0003068), here
derived directly from the rescaled equations.

For comparison, pairing the ordinary f=1 equation (3) with Phi gives
\(\int\rho^2\le\int(-s)_+\rho\). Cauchy--Schwarz and
\(\int\rho^2=8\|F_A^+\|_2^2\ge32\pi^2p\) give
\(\int s_-^2\ge32\pi^2p\). If scalar curvature is everywhere
nonnegative, (3) forces \(\Phi=0\) and \(F_A^+=0\), contradicting
p>0. The sign obstruction and the spectral estimate are distinct claims.

## 7. A global bounded smooth approximation to W+

Assume henceforth \(\delta=\|g^{-1}\operatorname{Ric}+I\|_{\infty,op}
\le1/64\). Put

\[
 E=\operatorname{Ric}+g,\quad e=s+4,\quad t=s+8\sqrt6u_W,
 \quad G=(2s/3-2\alpha)^2-(2s/3+2w)^2,
\]
\[
 \mathcal D=|E|^2+e^2+t^2+G,\qquad d_{\rm cal}=\int\mathcal D.
\]

One has \(-5\le s\le-3\), \(q\ge3\), and \(G\ge0\).
Set \(z=w+\alpha\). Trace-freeness and the norm inequality imply
\(0\le z\le\alpha\), and direct expansion gives

\[
 G=2z(-4s/3+4\alpha-2z)\ge8z.                              \tag{20}
\]

Let \(U=\{\mathcal D\le1/64\}\) and \(B=M\setminus U\).
Then \(\operatorname{Vol}(B)\le64d_{\rm cal}\). On U,

\[
 \alpha=(t-s)/24,\qquad
 61/384\le\alpha\le67/384,\qquad z\le1/512.
\]

The remaining two eigenvalues are
\(-w/2\pm\sqrt{2u_W^2-3w^2}/2\), so

\[
 \lambda_2-\lambda_1
 =\frac32(\alpha-z)-\frac12\sqrt{6\alpha z-3z^2}
 >1/8.                                                     \tag{21}
\]

The last inequality follows by inserting the preceding rational bounds;
also \(q\le587/128<5\) on U. Choose a measurable lowest-eigenline
projection Pi everywhere, agreeing with the simple eigenline on U, and
put \(y=(I-\Pi)\psi\). The maximum principle gives \(\rho\le3\).
Equation (16) on U and this bound on B yield

\[
 \int|y|^2\le16\Delta/27+576d_{\rm cal}+\eta.              \tag{22}
\]

The amplitude has a global constant target. The exact identity
\(q-9/2=(t-9e)/8\) implies
\(\|q-9/2\|_2^2\le41d_{\rm cal}/32\). Equation (13), q>=3,
and \(|\sqrt q-\sqrt{9/2}|^2\le(q-9/2)^2/12\) give

\[
 \|\rho-\sqrt2\|_2^2
 \le8\Delta/27+41d_{\rm cal}/432+\eta.                    \tag{23}
\]

For the measurable operator \(A_0(\Pi)=I/12-\Pi/4\), one has

\[
\begin{split}
 |W^+-A_0(\Pi)|^2
 &=u_W^2+1/24+w/2\\
 &=\frac32(\alpha-1/6)^2+z/2
 \le(t^2+e^2)/192+G/16\le\mathcal D/16.                  \tag{24}
\end{split}
\]

Now form the smooth tensor, without dividing by rho,

\[
 A_\psi=\rho^2I/24-\psi\otimes\psi/8.
\]

Its eigenvalues are \(-\rho^2/12,\rho^2/24,\rho^2/24\), and
\(|A_\psi|^2=\rho^4/96\). The rank-one identity

\[
 |\psi\otimes\psi-\rho^2\Pi|^2=2\rho^2|y|^2
\]

and a squared triangle inequality give

\[
 |A_\psi-A_0(\Pi)|^2
 \le\rho^2|y|^2/16+(\rho^2-2)^2/48.
\]

Use \(\rho\le3\), \((3+\sqrt2)^2<20\), and (22)--(24):

\[
\begin{split}
 \|W^+-A_\psi\|_2^2
 &\le d_{\rm cal}/8+(9/8)\int|y|^2
                         +(20/24)\|\rho-\sqrt2\|_2^2\\
 &\le\frac{74}{81}\Delta
       +\left(\frac18+648+\frac{205}{2592}\right)d_{\rm cal}
       +\eta\\
 &\le\boxed{\Delta+649d_{\rm cal}+\eta}.                 \tag{25}
\end{split}
\]

Also \(\|A_\psi\|_\infty\le9/(4\sqrt6)\). Equations (12),
(23), and (25) are precisely the quantitative inputs used in the
intrinsic Hessian proof. They hold simultaneously for a sufficiently
accurate smooth approximation on each metric. Neither a global
eigenvalue gap nor a spinor nonvanishing assumption has been introduced.

## 8. Weighted Hodge and the divergence-energy normalization

Here are also the local identities needed for the positive lower bound
on divergence energy in `round3_rigidity.md`. They involve only smooth
self-dual forms and the metric connection. Define

\[
 B_\psi=(s/3)\rho^2-2\langle W^+\psi,\psi\rangle,
 \qquad C_\psi=\langle\iota_{\nabla\rho}\psi,*d\psi\rangle.
\]

Testing the two-form Hodge equation against \(\rho^2\psi\), with
the nonnegative Hodge Laplacian, gives

\[
 \int\rho^2\bigl(|\nabla\psi|^2+B_\psi-2|d\psi|^2\bigr)
 =4\int\rho C_\psi-2\int\rho^2|d\rho|^2.                 \tag{26}
\]

Indeed, self-duality combines the two Hodge energies to
\(2\langle d\psi,d(\rho^2\psi)\rangle\). Their cross term is
\(4\rho\langle*d\psi,\iota_{\nabla\rho}\psi\rangle\).
On the rough-Laplacian side, differentiating \(\rho^2\psi\)
adds \(2\rho^2|d\rho|^2\) to the main weighted gradient energy.
These two integrations by parts prove (26), including the signs.

For an orthonormal basis \(\epsilon_a\) of \(\Lambda^+\), put
\(\omega_a=\sqrt2\epsilon_a\). The four-tensor corresponding to
a self-adjoint trace-free operator A is

\[
 W(A)_{ijkl}=\tfrac12\sum_{ab}A_{ab}(\omega_a)_{ij}(\omega_b)_{kl}.
\]

Let \(J_\psi=\nabla^iW(A_\psi)_{ijkl}\), with its ordinary
three-index norm. At a point where rho>0 choose a parallel frame at
that point with \(\psi=\rho\epsilon_1\) and write
\(\nabla_m\psi=c_m\epsilon_1+a_m\epsilon_2+b_m\epsilon_3\).
Then \(c_m=\partial_m\rho\), and direct differentiation gives

\[
 \nabla_m A_\psi=
 \begin{pmatrix}
 -\rho c_m/6&-\rho a_m/8&-\rho b_m/8\\
 -\rho a_m/8&\rho c_m/12&0\\
 -\rho b_m/8&0&\rho c_m/12
 \end{pmatrix}.
\]

Taking its Hilbert--Schmidt norm gives

\[
 |\nabla A_\psi|^2
 =\rho^2|\nabla\psi|^2/32+\rho^2|d\rho|^2/96.             \tag{27}
\]

Insert the same matrix into the displayed four-tensor formula and
contract its first index. Using the explicit oriented frame
\(\omega_1=dx^{01}+dx^{23}\),
\(\omega_2=dx^{02}+dx^{31}\),
\(\omega_3=dx^{03}+dx^{12}\) gives

\[
 |\nabla A_\psi|^2-|J_\psi|^2
 =\frac{\rho^2}{64}(|\nabla\psi|^2-2|d\psi|^2)
   +\frac{\rho^2}{32}|d\rho|^2-\frac\rho{16}C_\psi.       \tag{28}
\]

This is a pointwise quadratic identity in the twelve real entries
\((c_m,a_m,b_m)\). The complete contraction is also reproduced in
the preserved local checker `round2_rigidity_check.py`. All terms
extend across zeros; here \(\rho=|\Phi|^2\) is itself smooth.

Eliminating the weighted gradient from (26)--(28) yields the exact
integrated formula

\[
 \int|J_\psi|^2
 =-\frac1{64}\int\rho^2B_\psi
  +\frac1{16}\int\rho^2|d\psi|^2
  -\frac5{96}\int\rho^2|d\rho|^2
  +\frac18\int\rho C_\psi.                               \tag{29}
\]

Since \(A_\psi\psi=-\rho^2\psi/12\), writing
\(W^+=A_\psi+R\) makes its first integrand

\[
 -\rho^2B_\psi/64
 =-s\rho^4/192-\rho^6/384
                       +\rho^2\langle R\psi,\psi\rangle/32.
\]

At \(s=-4\), \(\rho=\sqrt2\), and R=0 this equals 1/16.
The bounded amplitude, (12), (23), and (25) therefore give, with
\(V=\operatorname{Vol}M\) and
\(\varepsilon=\delta^2+(\Delta+d_{\rm cal})/V\),

\[
 \fint|J_\psi|^2
 \ge\frac1{16}-C\left(\sqrt{\varepsilon+\eta/V}
                                    +\varepsilon+\eta/V\right).
                                                               \tag{30}
\]

For the cross term use
\(|C_\psi|\le\rho|d\rho||d\psi|\) and Cauchy--Schwarz.
Polynomial amplitude errors are bounded by
\(C\fint|\rho-\sqrt2|\); the R term is bounded by
\(C\fint|R|\). These estimates require no control of
\(\nabla\psi\) on a varying bad set.

## Verification and provenance

The rescaled-solvability and classical curvature estimates are established
Seiberg--Witten inputs, with primary references linked above. The
nonnegative-deficit decomposition and its constants have been fully
derived here; no live file is a mathematical premise. The elementary
constant and polynomial checks are reproduced in
`round3_monopole_input_check.py`. These checks verify algebra, while the
analytic and topological assumptions remain exactly those stated here.
