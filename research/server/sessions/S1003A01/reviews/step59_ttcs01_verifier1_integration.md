# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 59,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step59_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step59_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the mathematical content of the proposed all-p Cartan/chirality and smooth-bolt completion for the explicit Bianchi-VIII negative Einstein almost-Kähler pair. Check sign and normalization conventions, whether the identities d_i'+h_i d_i=1 and 2W_i d_i-d_jd_k=-1 really imply W^-=0, whether the displayed W^+ eigenvalues and eta/W3 norms follow, and whether the polar slice formulas prove a smooth metric and 2-form across the bolt for compact-generator period 2π. Identify any hidden issue in the quotient/group lift or normal Euler degree. Also inspect the proposed c2(E)=5χ+6τ zero-charge interpretation and state exactly what is proved for nonisolated zeros versus what remains unknown about Einstein-AK zero germs. Give direct mathematical corrections, not process advice.

## Integrated Scientific Memo

# Verification memo

The all-\(p\) half-conformal calculation and the polar bolt extension are valid. The required global completion uses a lift of the surface group to \(SL(2,\mathbb R)\) **excluding \(-I\)**. With the orientations induced by \(\Omega\), the normal degree is **\(g-1\)**, not \(1-g\). The positive torsion charge proves the existence of zeros on a closed nonzero-scalar Einstein almost-Kähler manifold, but does not classify their germs or imply positivity of individual indices.

## 1. Cartan calculation, curvature sign, and chirality

Fix \(e^{0123}>0\), use cyclic \((i,j,k)\), and put
\[
\omega_i^\pm=e^{0i}\pm e^{jk},\qquad |\omega_i^\pm|^2=2.
\]
With Cartan’s convention
\[
de^a+\omega^a{}_b\wedge e^b=0,\qquad
\Theta^a{}_b=d\omega^a{}_b+\omega^a{}_c\wedge\omega^c{}_b,
\]
the structure equations give
\[
\omega^i{}_0=h_i e^i,\qquad
\omega^j{}_k=C_i e^i,\qquad C_i=W_j+W_k-W_i.
\]
In particular, **\(\omega^0{}_i=-h_i e^i\)**.

The chiral combinations can be specified without ambiguity as
\[
F_i^+=\Theta^i{}_0-\Theta^j{}_k,\qquad
F_i^-=\Theta^i{}_0+\Theta^j{}_k.
\]
Writing \(b_i=h_i-C_i\), \(d_i=h_i+C_i\), direct expansion yields
\[
F_i^+=(b_i'+h_i b_i)e^{0i}
 +(2W_i b_i+b_jb_k)e^{jk},
\]
\[
F_i^-=(d_i'+h_i d_i)e^{0i}
 +(2W_i d_i-d_jd_k)e^{jk}.
\]
Thus the quadratic signs in the proposed calculation are correct. Calling these “spin-connection triples” requires specifying generators; the formulas above avoid any hidden factor of two.

For the explicit metric, set
\[
H=1+3p^2,\qquad D=(3p-1)(3p+1)H,\qquad y=\sqrt D>0.
\]
The geodesic derivative is
\[
\frac d{dt}
=\frac{(1-p^2)y}{2H}
 \left(\partial_p+\frac{D'}{2y}\partial_y\right).
\]
The supplied expressions simplify to
\[
(d_1,d_2,d_3)
=\left(\frac{2y}{(3p-1)H},
       \frac{2y}{(3p+1)H},
       \frac{y}{4p}\right),
\]
\[
(b_1,b_2,b_3)
=\left(-\frac{6py(p-1)^2}{(3p-1)H^2},
        \frac{6py(p+1)^2}{(3p+1)H^2},
        \frac{3y(p-1)^2(p+1)^2}{4pH^2}\right).
\]
Differentiation and substitution of \(y^2=D\) give
\[
d_i'+h_i d_i=1,\qquad
2W_i d_i-d_jd_k=-1,
\]
and
\[
b_i'+h_i b_i=2W_i b_i+b_jb_k.
\]
These are exactly the zero residuals recorded in `step59/chiral_exact.json`; the script performs rational identities in a quadratic field, not numerical sampling.

Consequently
\[
F_i^-=\omega_i^-.
\]
In the curvature-operator convention of the supplied AAD paper,
\[
\mathcal R(\omega_i^\pm)=-F_i^\pm.
\]
This sign follows from the index placement above; for example, constant sectional curvature \(-1\) gives precisely \(F_i^\pm=\omega_i^\pm\). Hence
\[
\mathcal R|_{\Lambda^-}=-I.
\]
Since \(s=-12\),
\[
\mathcal R|_{\Lambda^-}=W^-+\frac{s}{12}I=W^--I,
\]
so
\[
\boxed{W^-=0\quad\text{for every }1/3<p<1.}
\]

The earlier Koszul matrix \(2I\) is not an operator with eigenvalue \(2\): it uses forms of squared norm \(2\) and opposite curvature-index sign. Its conversion is consistent with \(-I\).

## 2. \(W^+\), \(\eta\), and \(W_3^+\)

Let \(\rho_i=b_i'+h_i b_i\). Since \(F_i^+=\rho_i\omega_i^+\),
\[
\mathcal R_+\omega_i^+=-\rho_i\omega_i^+,\qquad
w_i=1-\rho_i.
\]
This produces the proposed eigenvalues:
\[
w_1=-\frac{4(9p^6-18p^5-9p^4-6p^3+9p^2-1)}{H^3},
\]
\[
w_2=-\frac{4(9p^6+18p^5-9p^4+6p^3+9p^2-1)}{H^3},
\]
\[
w_3=\frac{8(9p^6-9p^4+9p^2-1)}{H^3}.
\]
Their sum is zero, and their limit is \((1,-2,1)\). Since \(\Omega\to\omega_2^+\), this agrees with the Kähler Weyl eigenvalues \(s/6=-2\) and \(-s/12=1\). This checks normalization, but the limiting spectrum alone does not identify the full boundary geometry with complex hyperbolic geometry.

Write
\[
\Omega=\sqrt{X_1}\omega_1^++\sqrt{X_2}\omega_2^+,\qquad
\Psi=-\sqrt{X_2}\omega_1^++\sqrt{X_1}\omega_2^+.
\]
Both have squared norm \(2\). Therefore
\[
\eta=\operatorname{pr}_{\Omega^\perp}W^+(\Omega)
=\sqrt{X_1X_2}(w_2-w_1)\Psi.
\]
Using
\[
w_1-w_2=\frac{48p^3}{H^2},
\]
gives
\[
\boxed{|\eta|^2
=\frac{18(1-p^2)^3(9p^2-1)}{H^4}.}
\]

On \(\Omega^\perp\), the **compressed** Weyl operator has diagonal entries
\[
a=X_2w_1+X_1w_2,\qquad w_3
\]
in the orthonormal basis \(\Psi/\sqrt2,\omega_3^+/\sqrt2\). It is important to say “compressed”: \(W^+\) does not preserve \(\Omega^\perp\) when \(\eta\ne0\). Its trace-free part is \(W_3^+\), with eigenvalues \(\pm(a-w_3)/2\). Thus
\[
|W_3^+|^2=\frac12(a-w_3)^2,
\]
and
\[
a-w_3=-\frac{9(1-p^2)^2(9p^2-1)}{H^3}.
\]
Hence
\[
\boxed{|W_3^+|^2
=\frac{81(1-p^2)^4(9p^2-1)^2}{2H^6}.}
\]
Here \(\eta\) has the ordinary form norm and \(W_3^+\) the Hilbert–Schmidt operator norm on two-forms. The corresponding full four-index curvature-tensor squared norm is four times the operator squared norm.

In particular, \(|\eta|^2>0\) throughout the open interval: this pair is not in the third-Gray branch. The formerly conditional radial profiles are now justified. The supplied radial integrals
\[
64,\quad \frac{512}{3},\quad32,\quad16
\]
for \(q,q^2,|\eta|^2,|W_3^+|^2\), respectively, remain **per unit invariant orbit volume**. Their stated balance is consequently an actual identity for this pair.

## 3. The polar formulas prove all-orders bolt smoothness

The analyticity assertion can be justified directly. Put \(u=\sqrt{p-1/3}\). Since \(G\) has a simple pole at \(p=1/3\), \(dr/du\) is positive and analytic in \(u^2\). Thus \(r\) is an odd analytic function of \(u\) with nonzero linear coefficient. Its inverse is odd analytic, so \(p-1/3\) is analytic in \(r^2\).

Consequently
\[
a_1=r\,u_1(r^2),\quad u_1(0)=1,\qquad
x_2=r\,u_2(r^2),
\]
while \(A_2,A_3,x_1\) are analytic in \(r^2\). The supplied series establish the exact analytic divisibilities
\[
A_1-r^2\in r^4\mathbb R\{r^2\},\qquad
A_2-A_3\in r^4\mathbb R\{r^2\}.
\]

For a compact-generator angle of period \(2\pi\), write locally
\[
\sigma_1=d\theta+A,\qquad
\sigma_2+i\sigma_3=e^{2i\theta}\eta_0,
\]
and set \(z=re^{i\theta}\), \(Dz=dz+izA\). Then
\[
dr+ir\sigma_1=e^{-i\theta}Dz,
\]
and the exact metric formulas are
\[
dr^2+A_1\sigma_1^2
=|Dz|^2+
 \frac{A_1-r^2}{r^4}\bigl(\operatorname{Im}(\bar zDz)\bigr)^2,
\]
\[
A_2\sigma_2^2+A_3\sigma_3^2
=\frac{A_2+A_3}{2}|\eta_0|^2+
 \frac{A_2-A_3}{2r^4}\operatorname{Re}(z^4\eta_0^2).
\]
All coefficients are analytic in \(|z|^2\), and the limiting metric is positive:
\[
g|_{z=0}=|dz|^2+6|\eta_0|^2.
\]
This proves the weight-four anisotropy condition at every order.

For the mixed two-form component, put
\[
C_r=x_2a_2=ru(r^2),\qquad
C_\theta=x_2a_3a_1=r^2v(r^2),\qquad u(0)=v(0)=4,
\]
and \(f_\pm=(C_r\pm C_\theta/r)/2\). Direct expansion verifies
\[
\Omega_2=
\operatorname{Re}\left\{
\left[\frac{f_+}{r}zDz+
      \frac{f_-}{r^3}z^3D\bar z\right]\wedge\eta_0
\right\},
\qquad D\bar z=d\bar z-i\bar zA.
\]
Indeed,
\[
\frac{f_+}{r}=\frac{u+v}{2},\qquad
\frac{f_-}{r^3}=\frac{u-v}{2r^2}
\]
are analytic in \(r^2\), because \(u(0)=v(0)\).

Also
\[
\Omega_1=x_1a_1\,dr\wedge\sigma_1+
          x_1a_2a_3\,\sigma_2\wedge\sigma_3
\]
extends: \(r\,dr\wedge\sigma_1\) is smooth, and \(\sigma_2\wedge\sigma_3\) is a base area form. At the bolt \(\Omega_2=0\) and
\[
\Omega=\text{normal area}+6\,\sigma_2\wedge\sigma_3.
\]
Thus \(\Omega\) remains nondegenerate. Closure, \(|\Omega|^2=2\), the Einstein equation, and \(W^-=0\) extend across the bolt. Moreover,
\[
q|_{\rm bolt}=\frac{32}{3}>0:
\]
**the bolt is not a torsion zero**.

## 4. Global lift and the normal Euler sign

For the stated generator in \(SL(2,\mathbb R)\),
\[
\exp(2\pi E_1)=I,\qquad \exp(\pi E_1)=-I.
\]
Take a cocompact torsion-free uniformizing group
\(\bar\Gamma<PSL(2,\mathbb R)\), and a genuine lifted subgroup
\[
\Gamma<SL(2,\mathbb R),\qquad
\Gamma\cong\bar\Gamma,\qquad -I\notin\Gamma.
\]
Such lifts correspond to the surface’s spin structures. Then
\[
P=\Gamma\backslash SL(2,\mathbb R)\longrightarrow\Sigma
\]
has fiber period \(2\pi\), as required by \(A_1\sim r^2\).

Using the **full inverse image** of \(\bar\Gamma\), or the \(PSL\) quotient itself, instead gives effective period \(\pi\). With the present radial normalization the bolt then has a normal cone of angle \(\pi\), not a smooth disk. This is a genuine distinction even though the central action preserves the displayed tensors.

The normal-degree disagreement is resolved by the nonsingular polar frame. From
\[
Dz=(dx-yA)+i(dy+xA)
\]
the oriented normal connection coefficient is
\[
\omega^{\nu_1}{}_{\nu_2}=-A.
\]
The bolt tangent coframe connection is
\[
\omega^2{}_3=2A.
\]
Since \(dA=-2\sigma_2\wedge\sigma_3\),
\[
e(N)=\left[-\frac{dA}{2\pi}\right],\qquad
e(T\Sigma)=\left[\frac{2dA}{2\pi}\right].
\]
Therefore
\[
\boxed{e(N)=-\frac12e(T\Sigma),\qquad \deg N=g-1.}
\]
The contrary calculation uses \(\omega^0{}_1=+h_1e^1\), whereas Cartan gives \(\omega^0{}_1=-h_1e^1\); it also treats a singular polar frame as a regular bolt frame.

Transition functions provide an independent check. If a local group section changes by \(k(\phi)\), then
\[
A'=A+d\phi,\qquad z'=e^{-i\phi}z,\qquad
\eta_0'=e^{2i\phi}\eta_0.
\]
These laws make the polar expressions gauge invariant and show
\[
N^{\otimes2}\cong K_\Sigma
\]
as complex line bundles. Thus the completion has the topology of a square root of \(K_\Sigma\), with its choice determined by the lift. This is a bundle statement, not a claim that the ambient almost complex structure is integrable.

For this quotient,
\[
\int_\Sigma\sigma_2\wedge\sigma_3=\pi(g-1),\qquad
\int_P\sigma_{123}=2\pi^2(g-1).
\]
These factors fix the global normalization of the radial integrals. Together with the infinite radial distance at \(p=1\), the smooth compact-bolt completion gives a complete noncompact pair.

## 5. What the torsion charge proves, including nonisolated zeros

The supplied AAD paper identifies
\[
\mathcal T=\nabla\Omega\in
\llbracket E\rrbracket,\qquad
E=\Lambda^{0,1}\otimes\Lambda^{0,2}.
\]
For Chern roots \(x_1,x_2\) of the complex tangent bundle, \(E\) has roots
\[
2x_1+x_2,\qquad x_1+2x_2.
\]
Hence
\[
c_2(E)=c_2(TM)+2c_1(TM)^2,\qquad
\boxed{\langle c_2(E),[M]\rangle=5\chi+6\tau.}
\]

For a closed Einstein manifold with \(s\ne0\), curvature formulas give both
\[
\chi>0,\qquad
2\chi+3\tau
=\frac1{4\pi^2}\int_M
\left(2|W^+|^2+\frac{s^2}{24}\right)d\mu>0.
\]
Thus
\[
5\chi+6\tau=\chi+2(2\chi+3\tau)>0.
\]
The actual torsion section must therefore vanish somewhere.

More precisely, if \(Z=\{\mathcal T=0\}\), pulling back the Thom class defines
\[
e_Z(\mathcal T)\in H^4(M,M\setminus Z;\mathbb Z),
\]
whose image in \(H^4(M;\mathbb Z)\) is \(c_2(E)\). This **nonzero supported class is proved even when zeros are nonisolated**.

If all zeros are isolated,
\[
\sum_{x\in Z}\operatorname{ind}_x(\mathcal T)=5\chi+6\tau.
\]
For nonisolated zeros, topology supplies neither a canonical pointwise index nor positive multiplicities on analytic strata. Isolated compact components can have total localized contributions, but their signs and geometry are not determined by this identity. Perturbing the section to make it transverse computes the class; it does not establish transversality of the Einstein–AK torsion itself.

## 6. Precise remaining zero-germ question

There is a useful conclusion beyond the restricted AAD continuation theorem: a smooth Einstein metric is analytic in harmonic coordinates, and the closed self-dual form \(\Omega\) is harmonic. Analytic elliptic regularity therefore makes \(\Omega\), \(\nabla\Omega\), and \(q\) analytic **also across \(q=0\)**. An infinite-order torsion zero forces local Kählerness. A non-Kähler germ can only have finite-order zeros.

This does not exclude such zeros. AAD Proposition 1 assumes the third Gray condition, including \(\eta=0\); Einstein alone supplies only \(\operatorname{Ric}''=0\). Its Proposition 3 extends an opposite Kähler structure using the special classified geometry, not analyticity alone. Remark 1(i) also records stronger point-zero rigidity when \(\operatorname{Ric}''=W_3^+=0\), again an extra curvature hypothesis.

The proposed principal-symbol warning is valid. At a zero, the necessary condition for
\[
\alpha=f_1d\bar z_1+f_2d\bar z_2
\]
permits
\[
f=cz+B\bar z.
\]
In particular \(f=z\) has degree \(+1\). One correction: \(f=\bar z\) in **complex dimension two also has degree \(+1\)**, not \(-1\). A negative-degree symbol-level example is
\[
f=(z_1+2\bar z_1,\ z_2),
\]
whose real determinant is \((1-4)\cdot1<0\). None of these is a constructed Einstein–AK germ.

Accordingly, the supplied material does **not** resolve whether the complete Einstein–almost-Kähler equations admit a non-Kähler negative-Einstein germ with a finite-order torsion zero, whether such zeros can be isolated or positive-dimensional, or which local indices occur. Resolving that object requires compatibility with the full nonlinear curvature and prolonged equations, not merely the type symbol or the positive global Chern number.