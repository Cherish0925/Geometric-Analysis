# TTCS Independent Branch Record

```json
{
  "step_id": 68,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/trace/ttcs/results/step67_ttcs01_sub1_generator.md",
    "Sessions/S1003A02/workspace/notes/step67_cK_local_coercivity_at_cscK.md",
    "Sessions/S1003A02/workspace/notes/step66_rank_one_exceptional_ricci_rigidity.md",
    "Sessions/S1003A02/workspace/scripts/step68_product_saddle_direct.py",
    "Sessions/S1003A02/workspace/data/step68_product_saddle_direct_n0.json",
    "Sessions/S1003A02/workspace/data/step68_product_saddle_direct_n1.json",
    "Sessions/S1003A02/workspace/data/step68_product_saddle_direct_n2.json",
    "Sessions/S1003A02/workspace/scripts/step68_product_saddle_global_exact.py"
  ]
}
```

## Task

Independently verify or refute the Step-67 product cscK saddle formula using the actual fixed-symplectic family. Setting: M=Sigma_1(K1) x Sigma_2(K2), K1,K2<0; Q is the real part of a holomorphic quadratic differential on Sigma_1; Delta_2 f=mu f; g_t|_1=g_1(exp(t f g_1^{-1}Q)·,·), g_t|_2=g_2, with fixed omega. The claimed Taylor t^2 coefficient is 8pi^2(p-|c1^-|^2)_2 = [mu/4][mu+2(K1-K2)]||fQ||^2. Derive this from actual connection/curvature variation or an exact integrated identity, checking all factors and the claims Ric''_1=(mu/2)k, rho0'_1=0, int u_2=(mu/4)||k||^2, and (rho0,t_2^-)=-[(K1-K2)mu/8]||k||^2. Resolve the apparent conflict in the supplied direct-coordinate scripts: they use local q=z^n on H^2 and produce n-dependent extra terms, suggesting that a pointwise local density is not the global integrated Hessian. Explain precisely whether those extras are divergences/Bochner terms and whether the global saddle formula is valid. Also check that an O(t^2) conformal correction to exact constant scalar curvature leaves the coefficient unchanged by Lemma 67.1. Give a proof-quality memo, not a procedural checklist.

## Output

# Scientific memo: product cscK Hessian

## Result

For the fixed-symplectic family
\[
g_t|_{T\Sigma_1}=g_1\!\left(e^{tfA}\,\cdot,\cdot\right),
\qquad A=g_1^{-1}Q,
\qquad g_t|_{T\Sigma_2}=g_2,
\]
the Step-67 coefficient has a factor-two error in its curvature-difference term. With
\[
\mathcal F(g)=P(g)-8\pi^2|c_1^-|_g^2,
\qquad
\mathcal F(g_t)=t^2\mathcal F_2+O(t^3),
\]
the correct formula is
\[
\boxed{\;
\mathcal F_2
=
\frac{\mu}{4}\bigl[\mu+K_1-K_2\bigr]\|fQ\|_2^2 .
\;}
\tag{1}
\]
Thus the coefficient \(2(K_1-K_2)\) in Step 67 must be replaced by \(K_1-K_2\).

The statements
\[
\Ric''_1=\frac{\mu}{2}k,\qquad \rho'_{0,1}=0
\]
are correct. The torsion computation used in Step 67 doubles the induced \(T^*\otimes\Lambda^2\) norm. In the frame normalization compatible with
\[
\nabla\omega=a\otimes\phi-Ja\otimes J\phi,\qquad
|\phi|^2=2,\qquad
t^-=-(a\wedge Ja)^-,
\]
one instead has
\[
\boxed{\;
\int_M u_2=\frac{\mu}{8}\|fQ\|_2^2,\qquad
(\rho_0,t_2^-)
=-\frac{(K_1-K_2)\mu}{16}\|fQ\|_2^2 .
\;}
\tag{2}
\]

## 1. The harmonic \(c_1^-\) term is exactly constant

Because \(\operatorname{tr}A=0\),
\[
\det(e^{tfA})=1.
\]
Hence the area form of the first block remains \(\omega_1\), and the total volume form is fixed. The compatible almost-complex structure is
\[
J_t|_{T\Sigma_1}=e^{-tfA}J_1,\qquad J_t|_{T\Sigma_2}=J_2,
\]
so \(\omega=\omega_1+\omega_2\) is fixed.

For every \(t\),
\[
*_t\omega_1=\omega_2,\qquad *_t\omega_2=\omega_1.
\]
Consequently
\[
\eta:=\omega_1-\omega_2
\]
is closed, anti-self-dual and harmonic for every \(g_t\). Moreover,
\[
K_1\omega_1+K_2\omega_2
\]
represents \(2\pi c_1(J_t)=2\pi c_1(J_0)\) and is harmonic for every \(t\). Its anti-self-dual part is
\[
\rho_0=\frac{K_1-K_2}{2}\eta.
\]
Therefore \(|c_1^-|_{g_t}^2\) is exactly constant along this family, not merely stationary. Thus
\[
\mathcal F_2=P_2.
\tag{3}
\]

## 2. Linearized Ricci tensor

The tensor \(k=fQ\) satisfies
\[
\operatorname{tr}k=0,\qquad \delta k=0,\qquad s'(k)=0.
\]
For a tracefree Codazzi tensor on the first factor,
\[
\nabla^*\nabla Q=-2K_1Q.
\]
Hence
\[
\nabla^*\nabla k=(\mu-2K_1)k.
\]
Using
\[
(D\Ric)k
=
\frac12\left(
\nabla^*\nabla k+\Ric\circ k+k\circ\Ric-2\mathring Rk
\right),
\]
together with
\[
\Ric\circ k+k\circ\Ric=2K_1k,\qquad
\mathring Rk=-K_1k,
\]
gives
\[
(D\Ric)k=\left(K_1+\frac{\mu}{2}\right)k.
\tag{4}
\]

The tensor
\[
\overline{\Ric}_t=K_1g_t|_{T\Sigma_1}+K_2g_2
\]
is \(J_t\)-invariant and has derivative \(K_1k\). Subtracting this moving invariant part from (4) yields
\[
\boxed{\Ric''_1=\frac{\mu}{2}k.}
\tag{5}
\]
Its squared norm is therefore
\[
\|\Ric''_1\|_2^2=\frac{\mu^2}{4}\|k\|_2^2.
\tag{6}
\]

The Ricci form of \(\overline{\Ric}_t\) is the fixed form
\[
K_1\omega_1+K_2\omega_2.
\]
The remaining term \((\mu/2)k\) is \(J_t\)-anti-invariant to first order. Hence the primitive \(J_t\)-invariant Ricci form has
\[
\boxed{\rho'_{0,1}=0.}
\tag{7}
\]

## 3. Direct torsion calculation and the factor two

At a point choose an orthonormal frame
\[
e_2=J_1e_1,\qquad e_4=J_2e_3,
\]
and rotate it so that
\[
Q=q\bigl((e^1)^2-(e^2)^2\bigr),\qquad df=c\,e^3.
\]
Thus
\[
|Q|^2=2q^2,\qquad |df|^2=c^2.
\]

Let \(C=D\nabla(k)\). Its relevant mixed components are
\[
C_{e_1}e_1=-\frac{qc}{2}e_3,\qquad
C_{e_2}e_2=\frac{qc}{2}e_3,
\]
\[
C_{e_1}e_3=\frac{qc}{2}e_1,\qquad
C_{e_2}e_3=-\frac{qc}{2}e_2.
\]
The terms involving derivatives of \(Q\) contribute no pure-\(T\Sigma_1\) torsion: for each fixed point of \(\Sigma_2\), the first block is a two-dimensional metric with fixed area form \(\omega_1\), so its Levi-Civita connection preserves \(\omega_1\).

Writing \(T=(\nabla\omega)'_0\), one obtains
\[
T_{e_1}=\frac{qc}{2}(e^{14}+e^{23}),\qquad
T_{e_2}=\frac{qc}{2}(e^{13}-e^{24}),
\qquad T_{e_3}=T_{e_4}=0.
\tag{8}
\]
With the induced \(T^*\otimes\Lambda^2\) norm,
\[
|T|^2=q^2c^2
=\frac12|df|^2|Q|^2.
\tag{9}
\]
This is the missing factor in Step 67.

Set
\[
\phi=e^{13}-e^{24},\qquad J\phi=e^{14}+e^{23}.
\]
Then (8) has the standard form
\[
T=a_1\otimes\phi-Ja_1\otimes J\phi,
\qquad
a_1=\frac{qc}{2}e^2
\]
up to an inessential simultaneous sign. Therefore
\[
u_2=|a_1|^2
=\frac18|df|^2|Q|^2.
\]
After integration,
\[
\boxed{\int_Mu_2=\frac{\mu}{8}\|fQ\|_2^2.}
\tag{10}
\]

Furthermore,
\[
(a_1\wedge Ja_1)^-
=\frac{u_2}{2}(\omega_1-\omega_2),
\]
so
\[
t_2^-=-\frac{u_2}{2}\eta.
\]
Since \(\rho_0=r\eta\), \(r=(K_1-K_2)/2\), and \(|\eta|^2=2\),
\[
(\rho_0,t_2^-)
=-r\int_Mu_2
=-\frac{(K_1-K_2)\mu}{16}\|fQ\|_2^2.
\tag{11}
\]

If one instead identifies \(\nabla\omega\) with \(\nabla J\) and uses the unrestricted \((0,3)\)-tensor norm, its norm is twice (9). In that notation the displayed \(\mu/4\) for \(u_2\) appears, but the formula for \(t^-\) must then acquire a compensating factor \(1/2\). Mixing the two normalizations doubles the twist pairing.

## 4. Hessian from the almost-Kähler identity

Insert (6), (7), and (11) into
\[
\mathcal F_2
=
\|\Ric''_1\|_2^2
-4(\rho_0,t_2^-)
+2\|(\rho'_{0,1})^{\perp\mathcal H}\|_2^2.
\]
This gives
\[
\mathcal F_2
=
\left[
\frac{\mu^2}{4}
+\frac{(K_1-K_2)\mu}{4}
\right]\|fQ\|_2^2,
\]
which is (1).

## 5. Independent integrated curvature calculation

There is also a direct way to see the same coefficient. Let
\[
\widehat g_\varepsilon=g_1(e^{\varepsilon A}\cdot,\cdot),
\qquad
K(\widehat g_\varepsilon)
=K_1+\varepsilon^2\kappa_2(Q)+O(\varepsilon^3).
\]
The linear curvature term vanishes because \(Q\) is TT and Codazzi. The area form of \(\widehat g_\varepsilon\) is fixed, so Gauss–Bonnet gives
\[
\int_{\Sigma_1}\kappa_2(Q)\,dA_1=0.
\tag{12}
\]

Expanding the mixed Christoffel symbols
\[
\Gamma^i_{\alpha j}
=\frac t2 f_\alpha A^i{}_j+O(t^2),\qquad
\Gamma^\alpha_{ij}
=-\frac t2 f^\alpha Q_{ij}+O(t^2)
\]
and then \(\int|\Ric^\circ|^2\) gives
\[
\begin{aligned}
P_2={}&
\frac14
\left(\int_{\Sigma_1}|Q|^2\,dA_1\right)
\left[
\int_{\Sigma_2}(\Delta f)^2\,dA_2
+(K_1-K_2)\int_{\Sigma_2}|df|^2\,dA_2
\right]
\\
&\quad
+2(K_1-K_2)
\left(\int_{\Sigma_2}f^2\,dA_2\right)
\left(\int_{\Sigma_1}\kappa_2(Q)\,dA_1\right).
\end{aligned}
\tag{13}
\]
The second line vanishes by (12). Since
\[
\int|df|^2=\mu\int f^2,\qquad
\int(\Delta f)^2=\mu^2\int f^2,
\]
equation (13) again yields (1).

A transparent factor test comes from the flat-fiber continuation \(K_1=0\), where \(Q=q(dx_1^2-dx_2^2)\) is parallel:
\[
g_t=e^{tqf}dx_1^2+e^{-tqf}dx_2^2+g_2.
\]
Putting \(a=tqf/2\), one finds
\[
\frac{\Ric_{11}}{g_{11}}=\Delta a,\qquad
\frac{\Ric_{22}}{g_{22}}=-\Delta a,\qquad
\Ric_{\alpha\beta}=K_2g_{\alpha\beta}-2a_\alpha a_\beta,
\]
\[
s=2K_2-2|da|^2.
\]
The \(t^2\) coefficient is
\[
P_2
=
\frac{\mu}{4}(\mu-K_2)\|fQ\|_2^2,
\]
rather than \(\frac{\mu}{4}(\mu-2K_2)\|fQ\|_2^2\).

## 6. Meaning of the \(q=z^n\) terms in the coordinate script

The three JSON files give
\[
R_n
=
\frac14\left[
\mu^2+(K_1-K_2)\mu
+2(n+1)(n+3)K_1(K_1-K_2)
\right].
\tag{14}
\]
The first two terms are exactly the integrated coefficient (1). The last term is the local intrinsic-curvature contribution
\[
2(K_1-K_2)\frac{\kappa_2(Q)}{|Q|^2}.
\]
At \(z=i\), the script’s local tensors satisfy
\[
\frac{\kappa_2(Q)}{|Q|^2}
=
\frac{(n+1)(n+3)}{4}K_1.
\tag{15}
\]

These terms are second variations of the surface Euler density. Since the area form is fixed,
\[
\kappa_2(Q)\,dA_1
\]
is a curvature-transgression divergence, and its integral on a closed surface is zero. Expanding it in derivatives of \(Q\) and using
\[
\nabla^*\nabla Q=-2K_1Q
\]
produces the equivalent Bochner cancellation.

The local functions \(q=z^n\) are not compact automorphic quadratic differentials, and the script samples only one point. It therefore retains the divergence density. This fully explains the \(n\)-dependence, but it does not restore the extra factor in the Step-67 formula. The surviving common part of the direct script is precisely (1).

The file `step68_product_saddle_global_exact.py` is not an independent derivation: it explicitly inserts
\[
(\rho_0,t_2^-)=-\frac{(K_1-K_2)\mu}{8}\|k\|^2
\]
before simplifying.

## 7. Constant-scalar correction

Since \(s'(k)=0\), the scalar variation starts at order \(t^2\). For a conformal correction \(e^{2v_t}g_t\), the linearized scalar operator at \(g_0\) is
\[
6\Delta-2s.
\]
It is invertible when \(s<0\), so one obtains an exact constant-scalar family with
\[
v_t=O(t^2).
\]

Lemma 67.1 gives
\[
D\mathcal F(g_0)=0
\]
on all metric variations. If the conformally corrected path differs by \(t^2h_2+O(t^3)\), its quadratic coefficient changes by \(D\mathcal F(g_0)[h_2]=0\). Therefore the correction leaves (1) unchanged.

## Consequence for the product saddle

If \(K_1<K_2\), this mode has Hessian value below zero exactly when
\[
\boxed{0<\mu<K_2-K_1.}
\]
The Step-67 threshold \(2(K_2-K_1)\) is twice too large. For
\[
K_1=-2,\qquad K_2=-1,
\]
one needs \(\mu<1\), not merely \(\mu<2\); at \(\mu=1\) the quadratic coefficient is zero.

Since compact hyperbolic surfaces can have arbitrarily small first eigenvalue under separating-neck degeneration, explicit product saddles still exist. They produce nearby non-Kähler constant-scalar metrics with
\[
P<8\pi^2|c_1^-|^2
\]
at quadratic order, and hence still show that \(c_K\ge 2\) is not universal for these products.