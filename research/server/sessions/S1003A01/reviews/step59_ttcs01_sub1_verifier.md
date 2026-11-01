# TTCS Independent Branch Record

```json
{
  "step_id": 59,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step58_verified_bianchiVIII_AKE_and_closed_zero_locus.md",
    "Sessions/S1003A01/workspace/notes/spirit_step58_chiral_bolt_and_zero_charge.md",
    "Sessions/S1003A01/workspace/scripts/step59_chiral_exact.py",
    "Sessions/S1003A01/workspace/data/step59/chiral_exact.json",
    "Sessions/S1003A01/workspace/data/step58/global_exact.json",
    "Sessions/S1003A01/workspace/scripts/step58_exact_bianchiVIII_fast.py",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md"
  ]
}
```

## Task

Independently verify the mathematical content of the proposed all-p Cartan/chirality and smooth-bolt completion for the explicit Bianchi-VIII negative Einstein almost-Kähler pair. Check sign and normalization conventions, whether the identities d_i'+h_i d_i=1 and 2W_i d_i-d_jd_k=-1 really imply W^-=0, whether the displayed W^+ eigenvalues and eta/W3 norms follow, and whether the polar slice formulas prove a smooth metric and 2-form across the bolt for compact-generator period 2π. Identify any hidden issue in the quotient/group lift or normal Euler degree. Also inspect the proposed c2(E)=5χ+6τ zero-charge interpretation and state exactly what is proved for nonisolated zeros versus what remains unknown about Einstein-AK zero germs. Give direct mathematical corrections, not process advice.

## Output

# Scientific verification memo

## 1. Cartan decomposition and chirality

Take the orientation \(e^{0123}>0\) and
\[
\omega_i^\pm=e^{0i}\pm e^{jk},\qquad (i,j,k)\ \text{cyclic}.
\]
From
\[
de^i=h_i e^{0i}+2W_i e^{jk},
\]
Cartan’s first equation gives
\[
\omega^i{}_0=h_i e^i,\qquad \omega^j{}_k=C_i e^i,
\qquad C_i=W_j+W_k-W_i.
\]
The two spin-connection triples are, up to a common sign,
\[
b_i e^i,\qquad d_i e^i,\qquad b_i=h_i-C_i,\quad d_i=h_i+C_i.
\]
Cartan’s second equation then yields
\[
F_i^+=(b_i'+h_i b_i)e^{0i}
 +(2W_i b_i+b_jb_k)e^{jk},
\]
\[
F_i^-=(d_i'+h_i d_i)e^{0i}
 +(2W_i d_i-d_jd_k)e^{jk}.
\]
The opposite signs in the quadratic terms are the correct \(\mathfrak{su}(2)_\pm\) structure constants.

In the quadratic field \(y^2=(3p-1)(3p+1)(3p^2+1)\), the relevant expressions simplify to
\[
d_1=\frac{2y}{(3p-1)(3p^2+1)},\qquad
d_2=\frac{2y}{(3p+1)(3p^2+1)},\qquad
d_3=\frac{y}{4p}.
\]
Using
\[
\frac d{dt}
=\frac{(1-p^2)y}{2(3p^2+1)}
 \left(\partial_p+\frac{D'(p)}{2y}\partial_y\right),
\]
direct reduction modulo \(y^2-D(p)\) gives
\[
d_i'+h_i d_i=1,\qquad
2W_i d_i-d_jd_k=-1.
\]
Hence
\[
F_i^-=e^{0i}-e^{jk}=\omega_i^-.
\]
Thus the curvature of the \(\Lambda^-\) spin connection is scalar in all three directions and has no \(\Lambda^+\)-domain component. Consequently its trace-free part vanishes:
\[
W^-=0.
\]

The scalar sign requires one conversion. In the Singer–Thorpe operator normalization,
\[
\mathcal R|_{\Lambda^-}=W^-+\frac{s}{12}I=W^--I
\]
because \(s=-12\). The Cartan curvature coefficient above enters this operator with a common minus sign, so \(F_i^-=\omega_i^-\) corresponds to \(\mathcal R|_{\Lambda^-}=-I\). The earlier Koszul matrix \(2I\) is consistent: its basis forms have norm squared \(2\), and its tensor index ordering carries the opposite common sign. It is therefore not an operator eigenvalue \(+2\).

## 2. The \(W^+\) eigenvalues and normalization

Let
\[
r_i=b_i'+h_i b_i.
\]
The exact identities
\[
b_i'+h_i b_i=2W_i b_i+b_jb_k
\]
make \(F_i^+=r_i\omega_i^+\). In the same Singer–Thorpe conversion,
\[
\mathcal R_+\omega_i=-r_i\omega_i.
\]
Since \(\mathcal R_+=W^+-I\), the Weyl eigenvalues are therefore
\[
w_i=1-r_i.
\]
This gives exactly
\[
w_1=-\frac{4(9p^6-18p^5-9p^4-6p^3+9p^2-1)}
{(3p^2+1)^3},
\]
\[
w_2=-\frac{4(9p^6+18p^5-9p^4+6p^3+9p^2-1)}
{(3p^2+1)^3},
\]
\[
w_3=\frac{8(9p^6-9p^4+9p^2-1)}
{(3p^2+1)^3}.
\]
They satisfy
\[
w_1+w_2+w_3=0.
\]
Also,
\[
(w_1,w_2,w_3)\longrightarrow(1,-2,1)\qquad(p\to1),
\]
while \(\Omega\to\omega_2\). Thus the limiting Kähler direction has eigenvalue \(s/6=-2\), and the perpendicular directions have eigenvalue \(-s/12=1\). This independently fixes the sign in \(w_i=1-r_i\).

## 3. The \(\eta\) and \(W_3^+\) profiles

The basis \(\omega_i\) has \(|\omega_i|^2=2\). Put
\[
\Omega=\sqrt{X_1}\,\omega_1+\sqrt{X_2}\,\omega_2,
\qquad
\Psi=-\sqrt{X_2}\,\omega_1+\sqrt{X_1}\,\omega_2.
\]
Then \(|\Psi|^2=2\), and the component of \(W^+(\Omega)\) perpendicular to \(\Omega\) is
\[
\eta=\sqrt{X_1X_2}(w_2-w_1)\Psi.
\]
Since
\[
w_1-w_2=\frac{48p^3}{(3p^2+1)^2},
\]
one obtains
\[
|\eta|^2
=2X_1X_2(w_1-w_2)^2
=\frac{18(1-p^2)^3(9p^2-1)}{(3p^2+1)^4},
\]
which is the same as the displayed expression with
\(-18(p-1)^3(p+1)^3(3p-1)(3p+1)\).

On the plane spanned by \(\Psi,\omega_3\), the two diagonal entries of \(W^+\) are
\[
X_2w_1+X_1w_2,\qquad w_3.
\]
The trace-free anti-complex-linear part therefore has squared norm
\[
|W_3^+|^2
=\frac12\bigl(X_2w_1+X_1w_2-w_3\bigr)^2.
\]
Indeed,
\[
X_2w_1+X_1w_2-w_3
=-\frac{9(1-p^2)^2(9p^2-1)}{(3p^2+1)^3},
\]
so
\[
|W_3^+|^2
=\frac{81(1-p^2)^4(9p^2-1)^2}
{2(3p^2+1)^6}.
\]
These are Hilbert–Schmidt norms for \(W^+\) as an endomorphism of \(\Lambda^+\), matching the \(U(2)\) decomposition in the supplied AAD paper. If one instead uses the full \((0,4)\)-tensor norm, the squared Weyl-component norms acquire the usual factor \(4\).

## 4. Smooth extension at \(p=1/3\)

Let \(r\) be geodesic distance from the bolt and set \(a_i=\sqrt{A_i}\), \(x_i=\sqrt{X_i}\). The exact coefficients imply that \(p-\frac13\) is analytic in \(r^2\), and
\[
A_1=r^2+\frac29r^4+O(r^6),\qquad
A_2-A_3=\frac{10}{3}r^4+O(r^6),
\]
\[
X_2=\frac83r^2+O(r^4).
\]
Thus
\[
a_1=r\,u_1(r^2),\quad u_1(0)=1,
\]
while \(A_2,A_3,x_1\) are analytic in \(r^2\), and \(x_2=r\,u_2(r^2)\).

Choose the compact angle \(\theta\) with period \(2\pi\) and write locally
\[
\sigma_1=d\theta+A,\qquad
\sigma_2+i\sigma_3=e^{2i\theta}\eta_0.
\]
With \(z=re^{i\theta}\) and \(Dz=dz+izA\),
\[
dr+ir\sigma_1=e^{-i\theta}Dz.
\]
The radial-circle metric is exactly
\[
dr^2+a_1^2\sigma_1^2
=|Dz|^2+\frac{a_1^2-r^2}{r^4}
       \bigl(\operatorname{Im}(\bar zDz)\bigr)^2.
\]
Because \(a_1^2-r^2\) is divisible by \(r^4\) as an analytic function, this is smooth at \(z=0\).

The horizontal metric is
\[
A_2\sigma_2^2+A_3\sigma_3^2
=\frac{A_2+A_3}{2}|\eta_0|^2
+\frac{A_2-A_3}{2r^4}\operatorname{Re}(z^4\eta_0^2).
\]
The exact \(r^4\) divisibility of \(A_2-A_3\) supplies smoothness of the weight-four anisotropy. The limiting horizontal metric is positive and equals \(6|\eta_0|^2\).

For the mixed component of \(\Omega\), define
\[
C_r=x_2a_2,\qquad C_\theta=x_2a_3a_1,
\]
\[
f_+=\frac12\left(C_r+\frac{C_\theta}{r}\right),\qquad
f_-=\frac12\left(C_r-\frac{C_\theta}{r}\right).
\]
A direct expansion of the complex expression gives
\[
\Omega_2
=\operatorname{Re}\left\{
 \left[\frac{f_+}{r}zDz+\frac{f_-}{r^3}z^3D\bar z\right]
 \wedge\eta_0\right\}.
\]
Here
\[
C_r=4r+O(r^3),\qquad C_\theta=4r^2+O(r^4).
\]
More precisely, \(C_r=ru(r^2)\), \(C_\theta=r^2v(r^2)\), with \(u(0)=v(0)=4\). Hence
\[
\frac{f_+}{r}=\frac{u+v}{2},
\qquad
\frac{f_-}{r^3}=\frac{u-v}{2r^2}
\]
are analytic at \(r=0\). This establishes every Taylor order, not merely the displayed finite series.

The remaining part
\[
\Omega_1=x_1\left(a_1\,dr\wedge\sigma_1
                 +a_2a_3\,\sigma_2\wedge\sigma_3\right)
\]
is smooth because \(x_1a_1/r\) is analytic in \(r^2\), \(r\,dr\wedge\sigma_1\) is the smooth normal area form, and \(\sigma_2\wedge\sigma_3\) is the smooth bolt area form. At the bolt,
\[
\Omega=\text{normal area}+6\,\sigma_2\wedge\sigma_3,
\]
so it remains nondegenerate and has squared norm \(2\).

Thus \(g\) and \(\Omega\) extend smoothly; \(d\Omega=0\), \(\operatorname{Ric}=-3g\), and the norm identity extend by continuity. In particular,
\[
|\nabla\Omega|^2\longrightarrow\frac{32}{3},
\]
so the completed bolt remains strictly almost-Kähler.

## 5. The quotient and the normal Euler degree

Let
\[
K(t)=\exp(tE_1)\subset SL(2,\mathbb R).
\]
Then
\[
K(2\pi)=I,\qquad K(\pi)=-I,
\]
and the adjoint action on \(\sigma_2+i\sigma_3\) has weight \(2\).

For a compact genus-\(g\) surface, take a uniformizing group
\(\bar\Gamma<PSL(2,\mathbb R)\) and a genuine lift
\[
\Gamma<SL(2,\mathbb R),\qquad -I\notin\Gamma.
\]
Such lifts exist and are parametrized by the \(2^{2g}\) spin structures. Then
\[
P=\Gamma\backslash SL(2,\mathbb R)\longrightarrow\Sigma
\]
has compact fiber of period \(2\pi\), exactly as used in the polar coordinate \(z=re^{i\theta}\).

Using instead the full inverse image of \(\bar\Gamma\) in \(SL(2,\mathbb R)\) puts \(-I\) in the quotient group, making the effective period \(\pi\). With \(A_1\sim r^2\), that produces the local cone \(\mathbb R^2/\{\pm1\}\), rather than the smooth disk model. Thus the lifted subgroup avoiding \(-I\) is essential.

For the Euler sign, use the orientations induced by \(\Omega\). On a local section,
\[
dA=-2\sigma_2\wedge\sigma_3.
\]
The bolt Levi-Civita coframe connection is
\[
\omega_{23}=2A,
\]
whereas \(Dz=(dx-Ay)+i(dy+Ax)\) gives the normal coframe connection
\[
\omega_{\nu_1\nu_2}=-A.
\]
Therefore
\[
e(T\Sigma)=\left[\frac{2\,dA}{2\pi}\right],\qquad
e(N)=\left[\frac{-dA}{2\pi}\right]
=-\frac12e(T\Sigma).
\]
Since \(\deg T\Sigma=2-2g\),
\[
\deg N=g-1.
\]
The transition weights also give
\[
N^{\otimes2}\cong K_\Sigma.
\]
Thus the normal complex line is the theta characteristic selected by the chosen lift. The informal phrase “normal rotation \(A\), tangent rotation \(-2A\)” depends on whether vector or coframe connections are being described; the Chern–Weil formulas above fix the sign unambiguously.

## 6. The torsion zero class

For the almost-Kähler torsion,
\[
\mathcal T=\nabla\Omega\in
E=\Lambda^{0,1}\otimes\Lambda^{0,2},
\]
where \(E\) has complex rank \(2\). If \(x_1,x_2\) are the Chern roots of \(T^{1,0}M\), the roots of \(E\) are
\[
2x_1+x_2,\qquad x_1+2x_2.
\]
Hence
\[
c_2(E)=c_2(TM)+2c_1(TM)^2.
\]
Using
\[
c_2(TM)[M]=\chi,\qquad c_1(TM)^2[M]=2\chi+3\tau,
\]
one gets
\[
c_2(E)[M]=5\chi+6\tau.
\]

For a closed Einstein four-manifold with \(s\ne0\),
\[
\chi=\frac1{8\pi^2}\int_M
\left(|W^+|^2+|W^-|^2+\frac{s^2}{24}\right)d\mu>0,
\]
and
\[
2\chi+3\tau
=\frac1{4\pi^2}\int_M
\left(2|W^+|^2+\frac{s^2}{24}\right)d\mu>0.
\]
Therefore
\[
5\chi+6\tau=\chi+2(2\chi+3\tau)>0.
\]
So the actual torsion section must have a zero.

If
\[
Z=\{\mathcal T=0\},
\]
then pulling back the Thom class gives a localized class
\[
\mathfrak e_Z(\mathcal T)\in H^4(M,M\setminus Z;\mathbb Z)
\]
whose image in \(H^4(M;\mathbb Z)\) is \(c_2(E)\). This class is nonzero for the Einstein case above.

When \(Z\) consists of isolated points, excision identifies the localized class with their integer Brouwer indices, and
\[
\sum_{x\in Z}\operatorname{ind}_x(\mathcal T)=5\chi+6\tau.
\]
Individual indices need not be positive.

When \(Z\) has positive dimension or singular strata, there is no canonical integer attached to every point. The supported cohomology class remains defined, and separated connected components can carry localized contributions, but the topology alone does not specify multiplicities or signs along the strata.

## 7. What remains unresolved at a torsion zero

Einstein metrics are real analytic in harmonic coordinates. Since an almost-Kähler fundamental form is closed and self-dual, it is harmonic; analytic elliptic regularity therefore makes \(\Omega\) and \(\nabla\Omega\) analytic. A strictly almost-Kähler germ can consequently have only finite-order torsion zeros: infinite-order vanishing would make \(\nabla\Omega\) vanish in a neighborhood.

The AAD unique-continuation equation in the supplied paper assumes the third Gray identity, equivalently both \(J\)-invariant Ricci and the Weyl-eigenform condition for \(\Omega\). Einstein gives the first condition, but not the second. The present explicit metric has
\[
|\eta|^2>0\qquad\left(\frac13<p<1\right),
\]
so it exhibits precisely this distinction.

The principal type equation at a zero permits linear leading terms such as the displayed \(f=z\) model with an isolated nonzero local degree. That is a symbol-level torsion jet, not a solution of the complete Einstein–almost-Kähler prolongation.

Accordingly, the supplied mathematics establishes a nonzero total localized top Chern class on a closed Einstein–almost-Kähler four-manifold, but it does not determine whether the full field equations admit:

- an isolated finite-order torsion zero with \(q>0\) nearby;
- a higher-dimensional analytic zero set;
- prescribed local index signs;
- or a germ attaching a torsion zero to the strict geometry realized by this Bianchi-VIII solution.

The all-\(p\) half-conformal calculation and the smooth bolt completion themselves are valid with the quotient and norm conventions stated above.