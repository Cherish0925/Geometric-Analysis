# Step 59 — chiral completion, smooth Bianchi-VIII filling, and charged torsion zeros

## 1. Exact geometric completion of the explicit pair

The local theorem of Step 58 is now strengthened to a complete noncompact theorem. For the explicit metric and almost-Kähler form on \(1/3<p<1\), define
\[
C_i=W_j+W_k-W_i,\qquad b_i=h_i-C_i,\qquad d_i=h_i+C_i.
\]
For the oriented orthonormal coframe with
\[
de^i=h_i e^{0i}+2W_i e^{jk},
\]
Cartan's two chiral curvatures are
\[
F_i^+=(b_i'+h_i b_i)e^{0i}+(2W_i b_i+b_jb_k)e^{jk},
\]
\[
F_i^-=(d_i'+h_i d_i)e^{0i}+(2W_i d_i-d_jd_k)e^{jk}.
\]
Exact reduction in \(\mathbb Q(p,y)/(y^2-(3p-1)(3p+1)(3p^2+1))\) proves
\[
d_i'+h_id_i=1,\qquad2W_id_i-d_jd_k=-1,
\qquad b_i'+h_ib_i=2W_ib_i+b_jb_k.
\]
Therefore \(F_i^-=e^{0i}-e^{jk}\), and the curvature operator on \(\Lambda^-\) is \(-I\). Since \(s=-12\),
\[
\mathcal R|_{\Lambda^-}=W^-+{s\over12}I=W^--I,
\]
so \(W^-=0\) identically. This is exact all along the interval. The prior three rational-point matrices were only convention checks.

The exact self-dual Weyl eigenvalues are
\[
\begin{aligned}
w_1&=-{4(9p^6-18p^5-9p^4-6p^3+9p^2-1)\over(3p^2+1)^3},\\
w_2&=-{4(9p^6+18p^5-9p^4+6p^3+9p^2-1)\over(3p^2+1)^3},\\
w_3&={8(9p^6-9p^4+9p^2-1)\over(3p^2+1)^3}.
\end{aligned}
\]
They sum to zero and tend to \((1,-2,1)\), with \(\Omega\to\omega_2\), agreeing with the negative Kähler-Einstein normalization. Writing \(\Omega=\sqrt{X_1}\omega_1+\sqrt{X_2}\omega_2\), one obtains
\[
|\eta|^2=2X_1X_2(w_1-w_2)^2
={18(1-p^2)^3(9p^2-1)\over(1+3p^2)^4},
\]
\[
|W_3^+|^2={1\over2}(X_2w_1+X_1w_2-w_3)^2
={81(1-p^2)^4(9p^2-1)^2\over2(1+3p^2)^6}.
\]
Here the first is a form norm and the second the Hilbert--Schmidt operator norm. The calculation is reproduced by `workspace/scripts/step59_chiral_exact.py`; exact output is `workspace/data/step59/chiral_exact.json`. Independent TTCS branches checked the connection signs, the common curvature-index conversion, the norm factors, and the CH limiting normalization.

The radial integrals from Step 58 are therefore geometric, not conditional:
\[
\int q=64,\quad\int q^2={512\over3},\quad
\int|\eta|^2=32,\quad\int|W_3^+|^2=16
\]
per unit invariant orbit volume, and
\[
\int\left(|\eta|^2+2|W_3^+|^2+{3q^2\over16}-{3q\over2}\right)=0.
\]
Thus the strict negative-Einstein pair realizes the familiar AAD balance exactly; that balance cannot by itself prove closed integrability.

## 2. Smooth bolt and global quotient

Let \(r\) be outward geodesic distance from \(p=1/3\). Analytic inversion gives \(p-1/3\in r^2\mathbb R\{r^2\}\), while
\[
A_1-r^2\in r^4\mathbb R\{r^2\},\qquad
A_2-A_3\in r^4\mathbb R\{r^2\},
\qquad X_2\in r^2\mathbb R\{r^2\}.
\]
Choose a cocompact torsion-free \(\bar\Gamma<PSL(2,\mathbb R)\) and a lift \(\Gamma<SL(2,\mathbb R)\) avoiding \(-I\). Such lifts correspond to spin structures. The compact generator then has period \(2\pi\), rather than \(\pi\). On a local section write
\[
\sigma_1=d\theta+A,\qquad \sigma_2+i\sigma_3=e^{2i\theta}\eta_0,
\qquad z=re^{i\theta},\qquad Dz=dz+izA.
\]
The exact polar formulas are
\[
dr^2+A_1\sigma_1^2
=|Dz|^2+{A_1-r^2\over r^4}\bigl(\operatorname{Im}(\bar zDz)\bigr)^2,
\]
\[
A_2\sigma_2^2+A_3\sigma_3^2
={A_2+A_3\over2}|\eta_0|^2
+{A_2-A_3\over2r^4}\operatorname{Re}(z^4\eta_0^2).
\]
Every coefficient is analytic in \(|z|^2\), and the limiting horizontal metric is positive.

For the mixed form component, set
\[
C_r=\sqrt{X_2A_2}=ru(r^2),\qquad
C_\theta=\sqrt{X_2A_3A_1}=r^2v(r^2),\qquad u(0)=v(0)=4,
\]
\[
f_\pm={1\over2}\left(C_r\pm{C_\theta\over r}\right).
\]
Then
\[
\Omega_2=\operatorname{Re}\left\{\left[{f_+\over r}zDz+{f_-\over r^3}z^3D\bar z\right]\wedge\eta_0\right\}.
\]
Both \(f_+/r=(u+v)/2\) and \(f_-/r^3=(u-v)/(2r^2)\) are analytic. The remaining component is an analytic combination of the normal and base area forms. Thus \(g\) and \(\Omega\) extend smoothly and nondegenerately across the bolt. Closedness, unit norm, \(\operatorname{Ric}=-3g\), \(W^-=0\), and strictness extend; in fact \(q=32/3\) at the bolt. The far end has infinite radial length, so the completed pair is a complete noncompact strictly almost-Kähler Einstein four-manifold.

The completed manifold is the disk bundle over \(\Sigma_g\) associated to the chosen lift. The nonsingular polar coframe gives normal connection \(-A\) and tangent connection \(2A\), hence
\[
e(N)=-{1\over2}e(T\Sigma),\qquad\deg N=g-1,
\qquad N^{\otimes2}\cong K_\Sigma.
\]
The TTCS integrator and one branch obtained this sign; a second anonymous branch obtained the opposite sign by treating the fiber-coordinate transformation as the line-frame transformation. The regular gauge transition is \(A'=A+d\phi\), \(z'=e^{-i\phi}z\), \(\eta_0'=e^{2i\phi}\eta_0\). Because fiber coordinates transform inversely to a line frame, the normal frame transforms by \(e^{i\phi}\), so \(N^2=K_\Sigma\) and \(\deg N=g-1\). A quotient containing \(-I\) has effective period \(\pi\) and gives a cone rather than this smooth disk bundle.

The orbit normalization is
\[
\int_{\Sigma_g}\sigma_2\wedge\sigma_3=\pi(g-1),\qquad
\int_{\Gamma\backslash SL(2,\mathbb R)}\sigma_{123}=2\pi^2(g-1).
\]

## 3. The closed problem is a charged-zero problem

For any closed almost-Kähler four-manifold, the torsion is the real section underlying
\[
T=\nabla\Omega\in E:=\Lambda^{0,1}\otimes\Lambda^{0,2},
\]
a complex rank-two bundle. With Chern roots \(x_1,x_2\), the roots of \(E\) are \(2x_1+x_2\) and \(x_1+2x_2\), so
\[
c_2(E)=c_2(TM)+2c_1(TM)^2,
\qquad \langle c_2(E),[M]\rangle=5\chi+6\tau.
\]
For a closed Einstein metric with nonzero scalar curvature,
\[
\chi>0,
\qquad 2\chi+3\tau={1\over4\pi^2}\int\left(2|W^+|^2+{s^2\over24}\right)>0,
\]
therefore
\[
5\chi+6\tau=\chi+2(2\chi+3\tau)>0.
\]
This refines Armstrong's nowhere-zero obstruction. If \(Z=T^{-1}(0)\), the pulled-back Thom class gives a nonzero class
\[
e_Z(T)\in H^4(M,M\setminus Z;\mathbb Z)
\]
mapping to \(c_2(E)\). For isolated zeros,
\[
\sum_{x\in Z}\operatorname{ind}_x(T)=5\chi+6\tau.
\]
For nonisolated zeros the supported class remains, but neither pointwise multiplicities nor positive signs follow from topology. Perturbing the section computes the Euler class but does not preserve the Einstein--almost-Kähler equations.

Einstein metrics are analytic in harmonic coordinates, and \(\Omega\) is harmonic; hence \(T\) is analytic. Infinite-order vanishing forces local Kählerness, but finite-order zeros remain possible. At a zero, choose a unitary frame and write the leading homogeneous coefficient as
\[
P_m=(f_1d\bar z_1+f_2d\bar z_2)\otimes\ell.
\]
The principal part of \((d_bT)^-=0\) is
\[
\partial_{z_1}f_2=0,\qquad
\partial_{z_2}f_1=0,\qquad
\partial_{z_1}f_1=\partial_{z_2}f_2.
\]
Its complete homogeneous solution is
\[
\boxed{f_i=z_i h_{m-1}(\bar z)+g_i^{(m)}(\bar z).}
\]
For \(m=1\),
\[
P_1=cz+B\bar z.
\]
The divergence fixes the leading \(\eta\), while the antisymmetric part of \(B\) fixes the leading \(W_3^+\); the complex symmetric part of \(B\) is invisible to both leading exterior derivative and divergence. This is precisely the symmetric-Hessian freedom already exposed by the Step-56 h-test.

Both signs of a nondegenerate isolated index occur in this necessary principal class:
\[
P_1=z\quad\Rightarrow\quad\operatorname{ind}=+1,
\]
whereas, for example,
\[
P_1=(z_1+2\bar z_1,z_2)\quad\Rightarrow\quad\operatorname{ind}=-1.
\]
Thus the positive total top Chern number does not combine with the principal soldered equation to force a contradiction. Higher-order antiholomorphic models can carry positive degree as well. These are not Einstein germs; they establish what any successful argument must add.

At a zero, the Einstein AAD Bianchi equation implies
\[
\delta\eta=0,
\qquad (\nabla_{JZ}\eta)''+2(\delta W_3^+)_Z''=0,
\]
and the Weitzenböck equation gives
\[
(\nabla^*\nabla T)_X=2(\nabla_X\eta)''.
\]
These constrain the next jets, not the leading \(c,B\) alone. If the vanishing order is at least two, the Ricci identities force \(\eta=W_3^+=0\) at the zero and the pointwise \(W^+\) spectrum is Kähler type, but neighborhood integrability does not follow.

The next decisive local computation is therefore the first nonlinear prolongation at a positive-charge model such as \(P_1=cz\), retaining the Levi-Civita soldering, algebraic curvature symmetries, closure and constant norm of \(\Omega\), the full Einstein equation, and differentiated AAD identities. The terms
\[
\nabla^2q(X,Y)=2\langle(\nabla_XT),(\nabla_YT)\rangle,
\qquad
\nabla^2\kappa(X,Y)=3\langle(\nabla_XT),(\nabla_YT)\rangle
\]
and the quadratic couplings \(\nabla(T_\eta)\) are the first information absent from the frozen principal system. Compatibility through one prolongation would not construct a germ, but incompatibility would produce a genuine new local restriction. A complementary geometric target is extension of the Kähler-nullity line/opposite almost-complex structure across the zero: on a linking \(S^3\), its Hopf class equals the local torsion index, so such extension would force zero index. AAD proves this extension only in its third-Gray branch, not for unrestricted Einstein pairs.

## 4. Literature position

A fresh retrieval again found only publisher metadata for Armstrong's `An ansatz for almost-Kähler, Einstein 4-manifolds` (DOI 10.1515/crll.2002.009; citation key `armstrong2002ansatz`), so comparison with its explicit formulas remains unresolved. Full-text Bianchi-VIII sources retrieved in the same search concern diagonal vacuum self-duality in Ashtekar variables or neutral-signature non-diagonal Einstein metrics; they do not establish the present Riemannian almost-Kähler pair, smooth hyperbolic bolt, and ACH end. The absence of identification is not a priority result. The complete pair is mathematically usable independent of whether Armstrong's inaccessible ansatz already contains an equivalent metric.

## 5. Scope within the full programme

This complete noncompact pair proves that negative Einstein almost-Kähler differential compatibility supports strict geometry with nonzero \(\eta\), nonzero \(W_3^+\), finite torsion budgets, and no finite torsion zero. It rules out any closed Goldberg proof based solely on coercivity over the open strict set or on the existing integral balance. It does not answer the closed problem because its top Chern charge escapes to infinity.

Separately, A02's orientation-free defect identity
\[
E-1={6(\int|W|^2-8\pi^2\chi)+L_s\over R}
\]
and universal long-neck construction imply \(\alpha\le1\) on every closed four-manifold; \(2\chi\le3|\tau|\) forces \(\alpha=1\), and \(\alpha<1\) is equivalent to strict Weyl deficit. This corrects earlier orientation-specific summaries but does not alter the AKE construction. The certified balanced upper coefficient, Einstein-kernel Burns insertion, O10/O11 work, and Problems 1--3 remain separate active parts of the human goal.
