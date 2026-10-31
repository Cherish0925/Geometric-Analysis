# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 34,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step34_ttcs01_sub5_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step34_ttcs01_sub6_verifier.md"
    }
  ]
}
```

## Exact Task

Derive and critically assess the proposed symmetry-free two-part link calculus. Starting from a hypersurface foliation of a scalar-normalized four-manifold, write the Gauss and Codazzi constraints in conventions compatible with Ric°(nu,nu), Ric°(nu,.) and the second fundamental form; explain exactly which squared constraint components are controlled by integral |Ric°|^2 and how the diagonal Lemmas N, P and beta-pinning instantiate them. Compare this kinematic/constraint channel with Theorem G's characteristic boundary channel. Give a precise theorem-level general principle without claiming compactness or link regularity from L2 control alone. Note sign/convention dependencies that must be stated.

## Integrated Scientific Memo

# Symmetry-free two-part link calculus

## 1. Foliation conventions and Gauss–Codazzi constraints

Let \(C\subset (M^4,g)\) be foliated by closed hypersurfaces \(\Sigma_t\), and first use Gaussian gauge
\[
g=dt^2+h_t,\qquad \nu=\partial_t,\qquad
K(X,Y)=g(\nabla_X\nu,Y)=\frac12\partial_t h_t .
\]
Write
\[
\Theta=\operatorname{tr}_{h_t}K.
\]
Take
\[
R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z,
\]
so round spheres have positive sectional curvature.

The traced Gauss equation is
\[
R_{h}=s-2\operatorname{Ric}(\nu,\nu)+\Theta^2-|K|^2.
\]
Since \(\operatorname{Ric}^{\circ}=\operatorname{Ric}-\frac{s}{4}g\), define the Hamiltonian residual
\[
\boxed{
\mathcal C:=\operatorname{Ric}^{\circ}(\nu,\nu)
=\frac12\bigl(\Theta^2-|K|^2-R_h\bigr)+\frac{s}{4}.
}
\]
For \(s\equiv-24\),
\[
\boxed{
\mathcal C=\frac12\bigl(\Theta^2-|K|^2-R_h\bigr)-6.
}
\tag{1}
\]

With the same conventions, contracted Codazzi gives
\[
\boxed{
\mathcal J:=\operatorname{Ric}^{\circ}(\nu,\cdot)
=\operatorname{Ric}(\nu,\cdot)
=\operatorname{div}_{h}K-d\Theta .
}
\tag{2}
\]
Thus \(\mathcal C\) and \(\mathcal J\) are respectively the scalar Hamiltonian and vector momentum constraints.

The remaining five components are not constraints. Put
\[
\mathcal S
:=\left(\operatorname{Ric}^{\circ}|_{T\Sigma}\right)^{\circ_h}.
\]
In Gaussian gauge,
\[
\boxed{
\mathcal S=
\left(\operatorname{Ric}^{h}-\partial_tK-\Theta K+2K^2\right)^{\circ_h}.
}
\tag{3}
\]
This is the trace-free tangential evolution residual; it involves the second normal jet through \(\partial_tK\).

For a lapse \(g=N^2dt^2+h_t\), with zero shift, (1)–(2) remain valid geometrically when
\[
\nu=N^{-1}\partial_t,\qquad K=\tfrac12\mathcal L_\nu h,
\]
while the evolution equation acquires the usual \(N^{-1}\operatorname{Hess}_hN\) terms and
\[
d\mu_g=N\,dt\,d\mu_h.
\]

---

## 2. Exactly what \(\int|\operatorname{Ric}^{\circ}|^2\) controls

Relative to \(TM=\mathbb R\nu\oplus T\Sigma\),
\[
\operatorname{Ric}^{\circ}
=
\mathcal C\,\nu^\flat\otimes\nu^\flat
+2\nu^\flat\odot\mathcal J
+\mathcal S-\frac{\mathcal C}{3}h .
\]
The pieces are orthogonal, hence
\[
\boxed{
|\operatorname{Ric}^{\circ}|^2
=\frac43\mathcal C^2+2|\mathcal J|^2+|\mathcal S|^2.
}
\tag{4}
\]
Consequently, for
\[
P(g;C)=\int_C|\operatorname{Ric}^{\circ}|^2\,d\mu,
\]
one has the exact identity
\[
P(g;C)=
\int_C\left(\frac43\mathcal C^2+2|\mathcal J|^2+|\mathcal S|^2\right)d\mu,
\tag{5}
\]
and in particular
\[
\int_C\mathcal C^2\,d\mu\le\frac34P(g;C),\qquad
\int_C|\mathcal J|^2\,d\mu\le\frac12P(g;C),\qquad
\int_C|\mathcal S|^2\,d\mu\le P(g;C).
\tag{6}
\]

Thus the defect controls:

* the squared Hamiltonian residual \(\mathcal C^2\);
* the squared momentum residual \(|\mathcal J|^2\);
* the squared trace-free tangential evolution residual \(|\mathcal S|^2\).

It does **not** separately control \(R_h\), \(K\), \(\Theta\), intrinsic injectivity radius, or the individual terms in \(\operatorname{div}K-d\Theta\). In particular, small \(\mathcal C\) controls only
\[
\frac12(\Theta^2-|K|^2-R_h)\approx 6
\]
in weighted \(L^2\), not its three constituents.

A useful invariant dual estimate is: for a scalar \(f\), tangential vector \(X\), and tangential trace-free tensor \(T\),
\[
\left|
\int_C\bigl(f\mathcal C+\langle X,\mathcal J\rangle+\langle T,\mathcal S\rangle\bigr)d\mu
\right|^2
\le
P(g;C)
\int_C\left(\frac34f^2+\frac12|X|^2+|T|^2\right)d\mu .
\tag{7}
\]
Therefore every exact transport identity
\[
\mathcal A(\Sigma_b)-\mathcal A(\Sigma_a)-\mathcal F
=
\int_C\bigl(f\mathcal C+\langle X,\mathcal J\rangle+\langle T,\mathcal S\rangle\bigr)d\mu
\tag{8}
\]
implies
\[
\boxed{
\widehat P(C)\ge
\frac{|\mathcal A(\Sigma_b)-\mathcal A(\Sigma_a)-\mathcal F|^2}
{8\pi^2
\displaystyle\int_C
\left(\frac34f^2+\frac12|X|^2+|T|^2\right)d\mu},
}
\tag{9}
\]
where \(\widehat P=P/(8\pi^2)\). The subtraction \(\mathcal F\) is essential: it is the drift supplied by the reference Einstein or geometric evolution and therefore costs no Ricci defect.

---

## 3. Diagonal Bianchi–IX realization

For
\[
g=dt^2+a_f^2\sigma_f^2+a_g^2\sigma_g^2+a_h^2\sigma_h^2,\qquad
y_i=\frac{a_i'}{a_i},
\]
the eigenvalues of \(K\) are \(y_f,y_g,y_h\). Hence
\[
\Theta=y_f+y_g+y_h,\qquad
\frac12(\Theta^2-|K|^2)
=y_fy_g+y_gy_h+y_hy_f=\sigma_2(y).
\]
Thus (1) becomes
\[
\boxed{
\mathcal C=\sigma_2(y)-6-\frac12R^{(3)},
}
\tag{10}
\]
which is exactly Lemma N’s Hamiltonian field.

If
\[
e_\alpha=\operatorname{Ric}_{\alpha\alpha}+6,
\]
then \(s=-24\) gives \(e_0+e_f+e_g+e_h=0\), and
\[
\mathcal C=e_0=\frac12(e_0-e_f-e_g-e_h).
\]
In the notes’ Ricci-channel notation,
\[
\mathcal C=-\frac34H_{\mathrm{def}}.
\]

Define the two diagonal trace-free tangential projections
\[
E=e_f-\frac{e_g+e_h}{2},\qquad D=e_g-e_h .
\]
Then
\[
|\mathcal S|^2=\frac23E^2+\frac12D^2,
\]
so
\[
\boxed{
|\operatorname{Ric}^{\circ}|^2
=\frac43\mathcal C^2+\frac23E^2+\frac12D^2
=\frac34H_{\mathrm{def}}^2+\frac23E^2+\frac12D^2.
}
\tag{11}
\]
With the orbit normalization of the sources,
\[
\boxed{
\widehat P
=\int W\left(\frac{\mathcal C^2}{3}
+\frac{E^2}{6}
+\frac{D^2}{8}\right)dt,
\qquad W=a_fa_ga_h.
}
\tag{12}
\]

The contracted Bianchi and trace-Riccati equations reduce to the remaining parts of Lemma N:
\[
\mathcal C'=-2\Theta\mathcal C-\sum_i(\Theta-y_i)e_i,
\tag{13}
\]
and
\[
\Theta'=18-\Theta^2+R^{(3)}+\mathcal C.
\tag{14}
\]

A crucial structural point is that
\[
\mathcal J\equiv0
\]
in the homogeneous diagonal ansatz. Thus the diagonal theory tests the Hamiltonian component \(\mathcal C\) and two components \(E,D\) of the tangential evolution sector \(\mathcal S\), but not the symmetry-free momentum sector.

### Lemma P and \(D\)-pinning

Let
\[
q=\log(a_g/a_h),\qquad q'=y_g-y_h.
\]
The exact anisotropy equation is
\[
(Wq')'=W(P_g-P_h-D).
\tag{15}
\]
For the first-jet corrected observable
\[
\widetilde\Phi=q+\frac14q',
\]
this yields an identity of the form
\[
\boxed{
\widetilde\Phi'=F_\Phi-\frac14D,
}
\tag{16}
\]
where \(F_\Phi\) is the same derivative evaluated with \(D=0\). By (12),
\[
\boxed{
\left|\Delta\widetilde\Phi-\int F_\Phi\,dt\right|
\le
\sqrt{\frac{\widehat P}{2}}
\left(\int\frac{dt}{W}\right)^{1/2},
}
\tag{17}
\]
or
\[
\widehat P\ge
\frac{2|\Delta\widetilde\Phi-\int F_\Phi dt|^2}
{\int W^{-1}dt}.
\tag{18}
\]

Equivalently, choosing the Green costate
\[
K_G(t)=\int_t^{T_1}\frac{du}{W(u)}
\]
gives
\[
M=-\int WD\,K_G\,dt,\qquad
\boxed{
\widehat P\ge
\frac{M^2}{8\int WK_G^2dt}.
}
\tag{19}
\]

### Beta-pinning

For
\[
v=y_f-\frac{y_g+y_h}{2}
\]
and
\[
\widetilde B=
\log\frac{\kappa}{\sqrt{1+\zeta}}
+\frac14(v-\kappa^{-1}),
\]
the exact identity is
\[
\boxed{
\widetilde B'=F_\beta-\frac14E.
}
\tag{20}
\]
Thus
\[
\boxed{
\left|\Delta\widetilde B-\int F_\beta\,dt\right|
\le
\sqrt{\frac{3\widehat P}{8}}
\left(\int\frac{dt}{W}\right)^{1/2},
}
\tag{21}
\]
and
\[
\widehat P\ge
\frac{8|\Delta\widetilde B-\int F_\beta dt|^2}
{3\int W^{-1}dt}.
\tag{22}
\]

Therefore:

* Lemma N is the diagonal Hamiltonian-constraint penalty;
* Lemma P/\(D\)-Green pinning uses one projection of the tangential evolution residual;
* beta-pinning uses the other diagonal projection;
* neither Lemma P nor beta-pinning is a Codazzi estimate.

The denominators \(\int W^{-1}dt\) explain why volume growth and Lemma W-type expansion control are indispensable. A terminal CH first jet alone does not justify replacing the actual denominator by the exact-CH value.

---

## 4. Theorem G: the independent characteristic boundary channel

For every compact oriented \(\Omega\) with smooth boundary, the source establishes
\[
\boxed{
\widehat P(\Omega)
=
\frac1{2\pi^2}\int_\Omega|W^\pm|^2
+\frac1{96\pi^2}\int_\Omega s^2
-(2\chi(\Omega)\pm3\tau(\Omega))
+\mathcal Q_\pm(\partial\Omega),
}
\tag{23}
\]
where
\[
\mathcal Q_\pm=2\mathcal E\mp3\mathcal H.
\]
Here \(\mathcal E\) is the Euler transgression and
\[
\mathcal H=\eta+\int T_{p_1}
\]
is the APS eta term plus the local Pontryagin transgression.

For \(s=-24\), let
\[
\widehat V(\Omega)=\frac{2\operatorname{Vol}(\Omega)}{\pi^2}.
\]
Then
\[
\frac1{96\pi^2}\int_\Omega s^2=3\widehat V(\Omega)
\]
and
\[
\boxed{
\widehat P(\Omega)\ge
\mathcal Q_\pm(\partial\Omega)+3\widehat V(\Omega)
-(2\chi(\Omega)\pm3\tau(\Omega)).
}
\tag{24}
\]

For a slab \(C=[a,b]\times\Sigma\), \(\chi(C)=\tau(C)=0\), and if both endpoint charges are recorded using the nested-family outward convention, the inner link enters with reversed boundary orientation:
\[
\boxed{
\widehat P(C)\ge
\mathcal Q_\pm(\Sigma_b)-\mathcal Q_\pm(\Sigma_a)
+3\widehat V(C).
}
\tag{25}
\]

The distinction from the constraint/kinematic channel is exact:

| Characteristic channel | Constraint/kinematic channel |
|---|---|
| Symmetry-free and does not require a foliation | Requires a foliation or transport structure |
| Sees \(2\chi\pm3\tau\) and boundary transgressions | Resolves \(\operatorname{Ric}^{\circ}\) into \(\mathcal C,\mathcal J,\mathcal S\) |
| Prices endpoint link-charge changes | Prices drift-corrected shape and first-jet changes |
| Includes Weyl and scalar nonnegative remainders | Uses weighted Cauchy–Schwarz, often with \(\int W^{-1}\) |
| Can be weak if both charges decrease | Can remain strong during charge-neutral non-round opening |
| Requires controlled boundary germs to pass to limits | Requires controlled drift, weights, and visited state region |

The diagonal charge variation lemma is the symmetric reduction of Theorem G:
\[
\widehat P(C)\ge
\int_a^b\max\{0,\mathfrak b_+',\mathfrak b_-'\}\,dt .
\tag{26}
\]
Its symmetry-free counterpart is valid for any smooth fixed-topology foliation for which the link charges are differentiable:
\[
\boxed{
\widehat P(C)\ge
\int_a^b\max\{0,\mathcal Q_+'(t),\mathcal Q_-'(t)\}\,dt .
}
\tag{27}
\]
For volume-renormalized charges
\[
\mathfrak B_\pm(t)=\mathcal Q_\pm(\Sigma_t)+3\widehat V(\Omega_t),
\]
the analogous formula is
\[
\widehat P(C)\ge
\int_a^b\max\{0,\mathfrak B_+'(t),\mathfrak B_-'(t)\}\,dt.
\tag{28}
\]

The two channels bound the same \(\widehat P\); their lower bounds should normally be combined by a **maximum**, not added. Addition is justified only after splitting into disjoint regions or explicitly allocating orthogonal defect components.

The numerical/static phenomenon in Lemma Z fits this distinction. There are triaxial paths along which both characteristic charges remain low or decrease, so static charge sublevel geometry provides no obstruction. Kinematic admissibility nevertheless forces a substantial \(D\)-channel cost. That cost lies in \(\mathcal S\), not in an upward characteristic transgression.

A stronger leafwise “completion-of-square” interpretation of \(\mathcal Q_\pm'\) is plausible, but its detailed constants depend on the Weyl norm and magnetic-Weyl sign conventions and were not established in the supplied source files. It is not needed for the verified two-channel principle.

---

## 5. The theorem-level general principle

### Theorem (characteristic–constraint link calculus)

Let \((C^4,g)\) be a smooth oriented scalar-normalized region, \(s\equiv-24\), admitting a smooth Gaussian foliation by closed links \(\Sigma_t\), \(a\le t\le b\). Define \(K,\Theta,\mathcal C,\mathcal J,\mathcal S\) by (1)–(3).

Then:

1. **Orthogonal defect identity**
   \[
   P(g;C)=
   \int_C
   \left(\frac43\mathcal C^2+2|\mathcal J|^2+|\mathcal S|^2\right)d\mu .
   \tag{29}
   \]

2. **Characteristic identity**
   \[
   \widehat P(C)
   =
   \frac1{2\pi^2}\int_C|W^\pm|^2
   +3\widehat V(C)
   +\mathcal Q_\pm(\Sigma_b)-\mathcal Q_\pm(\Sigma_a).
   \tag{30}
   \]

3. **Transport inequality**  
   Every exact identity of the form (8) satisfies (9).

Consequently,
\[
\boxed{
\widehat P(C)\ge
\max\left\{
0,\;
\max_\pm\bigl[\Delta\mathcal Q_\pm+3\widehat V(C)\bigr],\;
\frac{|\mathcal M|^2}{8\pi^2\mathcal D}
\right\},
}
\tag{31}
\]
where
\[
\mathcal M=
\mathcal A(\Sigma_b)-\mathcal A(\Sigma_a)-\mathcal F,
\qquad
\mathcal D=
\int_C\left(\frac34f^2+\frac12|X|^2+|T|^2\right)d\mu.
\]

For a general compact foliated region \(\Omega\), rather than a slab, replace the characteristic term in (31) by
\[
\mathcal Q_\pm(\partial\Omega)+3\widehat V(\Omega)
-(2\chi(\Omega)\pm3\tau(\Omega)).
\tag{32}
\]

This is the precise symmetry-free content:

* Theorem G gives universal topology/characteristic calibrations.
* Gauss–Codazzi and the tangential evolution splitting give all Ricci-defect channels.
* Further pinning bounds arise only after specifying an observable, its reference drift, and its dual weight.
* The diagonal observables \(q,\beta,\widetilde\Phi,\widetilde B\) are not themselves symmetry-free; their invariant extension requires extra geometric structure selecting appropriate trace-free tensors.

---

## 6. No compactness or link regularity follows from \(L^2\) defect alone

The theorem is an accounting principle, not a compactness theorem. From bounded or small
\[
\int|\operatorname{Ric}^{\circ}|^2
\]
alone one cannot infer:

1. bounds on \(K\), \(R_h\), intrinsic injectivity radius, lapse, or focal radius;
2. existence of a globally smooth or focal-free foliation;
3. trace control of collar first jets on an arbitrarily chosen leaf;
4. convergence of the Euler or Pontryagin transgressions;
5. convergence of the APS eta contribution under collapse;
6. control of the Dai adiabatic correction from small eigenvalues;
7. convergence of localized Seiberg–Witten flux or Chern–Simons terms.

In particular, \(\mathcal E\) and \(\mathcal H\) depend on collar data, not merely on the intrinsic link metric. The diagonal Berger expression
\[
3\mathcal H
=
2(1-\lambda^2)^2+\lambda^2(U-V)^2
\]
shows explicitly that radial shear contributes to the boundary charge. Therefore the link-selection problem in the sources remains genuine: one needs additional hypotheses yielding controlled boundary germs, spectral behavior, and field-theoretic boundary terms.

Even \(\operatorname{Ric}^{\circ}=0\) does not freeze the foliation. An Einstein metric may undergo substantial nontrivial evolution, which is exactly why every pinning identity must subtract its Einstein drift.

---

## 7. Convention dependencies that must accompany every use

1. **Curvature sign.**  
   The formulas above use the convention for which round spheres have positive sectional curvature. Reversing the Riemann sign changes the Gauss, Riccati, Weyl, and characteristic formulas coherently.

2. **Second fundamental form.**  
   We used
   \[
   K(X,Y)=g(\nabla_X\nu,Y).
   \]
   Using \(-K\) reverses the Codazzi sign and changes all boundary transgression terms odd in \(K\).

3. **Normal direction.**  
   Under \(\nu\mapsto-\nu\),
   \[
   K\mapsto-K,\qquad
   \Theta\mapsto-\Theta,\qquad
   \mathcal J\mapsto-\mathcal J,
   \]
   while \(\mathcal C\) is unchanged. Inner boundary components carry the opposite boundary orientation.

4. **Four-dimensional orientation and chirality.**  
   Reversing orientation interchanges \(W^+\) and \(W^-\), changes the sign of \(\tau\), and exchanges the two chiral characteristic identities after adjusting induced link orientations.

5. **APS convention.**  
   The eta invariant, possible kernel convention, and local \(p_1\)-transgression must be normalized so that
   \[
   \int_\Omega L=\tau(\Omega)+\mathcal H(\partial\Omega).
   \]
   Numerical values of \(\mathcal Q_\pm\) are meaningless unless this convention and the Berger lift anchor are stated.

6. **Scalar normalization.**  
   The constant \(-6\) in (1) is specific to \(s=-24\). In general,
   \[
   \mathcal C=
   \frac12(\Theta^2-|K|^2-R_h)+\frac{s}{4}.
   \]

7. **Weyl norm.**  
   Any leafwise electric/magnetic-Weyl formula must specify whether \(|W^\pm|\) is the curvature-tensor norm or the \(\Lambda^2_\pm\)-endomorphism norm; these differ by a fixed factor. Theorem G’s constants determine the convention used in the sources.

8. **Bianchi–IX normalization.**  
   Formula (12) uses the invariant-form normalization for which the orbit integration gives
   \[
   \widehat P=\frac14\int W|\operatorname{Ric}^{\circ}|^2dt.
   \]
   Rescaling the invariant one-forms changes the displayed \(W\)-coefficients.

9. **Notation collision.**  
   The notes’ \(H_{\mathrm{def}}\) is a Ricci channel satisfying \(\mathcal C=-\frac34H_{\mathrm{def}}\); it is not the hypersurface mean curvature \(\Theta\).

The resulting calculus is genuinely two-part: characteristic charges account for topology and boundary transgression, while Gauss–Codazzi plus tangential evolution account for Hamiltonian, momentum, and kinematic mismatches. Neither channel, separately or together, supplies link compactness from critical \(L^2\) Ricci-defect control alone.