# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 58,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step58_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step58_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the proposed explicit Bianchi-VIII cohomogeneity-one almost-Kähler Einstein pair. Read the exact rational formulas and the underlying class-A convention/code. Check the mathematical chain: structure equations and orientation; coefficient normalization |Omega|^2=2; direct closure dOmega=0; Ric(g)=-3g; strictness q>0; and whether the reported opposite-chirality Weyl block W^-=0 follows. Identify any sign, normalization, or logical error. Give a concise rigorous proof route that does not depend on numerical ODE shooting or on primality of a modular ideal. Distinguish exact local existence from end extension and novelty.

## Integrated Scientific Memo

## Verification result

The explicit rational formulas define a genuine real-analytic **strictly almost-Kähler Einstein pair** on \(1/3<p<1\), with
\[
|\Omega|^2=2,\qquad d\Omega=0,\qquad
\operatorname{Ric}(g)=-3g,\qquad
|\nabla\Omega|^2=\frac{36(1-p^2)^3}{(1+3p^2)^3}>0.
\]
With the orientation below, the Weyl block opposite to \(\Omega\) vanishes exactly:
\[
W^-=0.
\]
These conclusions follow from explicit rational identities, not numerical shooting or assertions about a modular ideal.

The material contains two concrete bookkeeping issues: a homothety is required between the rational base point and the \(\lambda=-3\) metric, and the supplied checking script has an import-name mismatch. The bolt extension requires the correct circle period; its tensor smoothness can also be proved from the explicit formulas, as below. Novelty remains unresolved.

### 1. Structure equations, orientation, and an exact verification certificate

Use
\[
d\sigma_1=-2\sigma_2\wedge\sigma_3,\qquad
d\sigma_2=2\sigma_3\wedge\sigma_1,\qquad
d\sigma_3=2\sigma_1\wedge\sigma_2.
\]
Thus \(n=(-1,1,1)\), and the dual brackets are
\[
[X_2,X_3]=2X_1,\quad [X_3,X_1]=-2X_2,\quad [X_1,X_2]=-2X_3.
\]
In particular, \(X_1\) is elliptic, with adjoint rotation weight \(2\).

Take the displayed \(G,A_i\) from `spirit_step57_rational_branch_and_global_tests.md`, and set
\[
e^0=dt=\sqrt G\,dp,\qquad e^i=a_i\sigma_i,\qquad a_i=\sqrt{A_i},
\]
orienting by \(e^{0123}>0\). All metric coefficients are positive on \(I=(1/3,1)\). Then
\[
de^i=h_i e^{0i}+2W_i e^{jk},
\qquad
h_i=\frac{a_i'}{a_i},\quad
W_i=\frac{n_i a_i}{a_ja_k},
\]
where primes here denote \(d/dt\).

Here is a small, wholly rational certificate for checking all curvature identities. Put
\[
R=1+3p^2,\qquad
k=\frac{dp}{dt},\qquad
k^2=\frac{(1-p^2)^2(9p^2-1)}{4R},
\]
and write
\[
h_i=kH_i,\qquad W_i=kV_i.
\]
Directly from the metric,
\[
\begin{aligned}
H_1&=\frac12\left(\frac3{3p-1}+\frac{6p}{R}
+\frac1{1-p}-\frac2{1+p}\right),\\
H_2&=\frac12\left(\frac3{3p+1}+\frac{6p}{R}
+\frac2{1-p}-\frac1{1+p}\right),\\
H_3&=\frac1p+\frac{p}{1-p^2}-\frac{3p}{R},
\end{aligned}
\]
and
\[
V_1=-\frac{R}{4p(1+p)(3p+1)},\qquad
V_2=\frac{R}{4p(1-p)(3p-1)},\qquad
V_3=\frac{12p}{(9p^2-1)R}.
\]
Also,
\[
\ell:=\frac{d}{dp}\log k
=-\frac{2p}{1-p^2}+\frac{9p}{9p^2-1}-\frac{3p}{R}.
\]
No square roots remain in the identities below; their denominators are nonzero on \(I\).

### 2. Einstein equation and scale normalization

The Cartan/Koszul convention in `step56_bianchiA_ake.py` is consistent with
\[
\operatorname{Ric}_{00}=-\sum_i(h_i'+h_i^2),
\]
\[
\operatorname{Ric}_{ii}
=-h_i'-h_iS+2\bigl(W_i^2-(W_j-W_k)^2\bigr),
\qquad S=\sum_i h_i.
\]
Off-diagonal Ricci components vanish. One way to see this without a large computation is to use the sign-changing Lie-algebra automorphisms that preserve the diagonal metric.

Substitution of the rational certificate gives the identities
\[
k^2\left[
\sum_{i<j}H_iH_j+\sum_iV_i^2-2\sum_{i<j}V_iV_j
\right]=3,
\]
and, for each cyclic \((i,j,k)\),
\[
k^2\left[
\frac{dH_i}{dp}+\ell H_i+H_i\sum_mH_m
-2\bigl(V_i^2-(V_j-V_k)^2\bigr)
\right]=3.
\]
They are proved simply by clearing denominators and expanding. Equivalently,
\[
Q=3,\qquad
h_i'=-h_iS+2\bigl(W_i^2-(W_j-W_k)^2\bigr)+3.
\]
These imply \(\operatorname{Ric}_{ii}=-3\); the constraint \(Q=3\) then gives \(\operatorname{Ric}_{00}=-3\). Thus
\[
\boxed{\operatorname{Ric}(g)=-3g,\qquad s=-12.}
\]

**Scale correction.** At \(p=1/2\),
\[
(h,W)=\frac{3\sqrt{35}}{16}
\left(
\frac{176}{147},\frac{656}{735},\frac{76}{147};
-\frac1{15},1,\frac{192}{245}
\right).
\]
The unscaled rational point has \(Q=256/105\), not \(3\). Its correct Einstein constant is \(-256/105\). Multiplication of \(h,W\) by \(3\sqrt{35}/16\) gives \(Q=3\), as required by the explicit metric. There is no error in the rational metric, but combining the unscaled point with \(\lambda=-3\) would be erroneous.

### 3. Almost-Kähler normalization and direct closure

For cyclic \((i,j,k)\), set
\[
\omega_i=e^{0i}+e^{jk}.
\]
Under the stated orientation,
\[
*\omega_i=\omega_i,\qquad
\langle\omega_i,\omega_j\rangle=2\delta_{ij}.
\]
Take
\[
\Omega=x_1\omega_1+x_2\omega_2,\qquad x_i=\sqrt{X_i}>0,
\]
with the displayed \(X_1,X_2\). The polynomial identity
\[
(1-p)^3(3p+1)+(1+p)^3(3p-1)=16p^3
\]
proves \(X_1+X_2=1\). Consequently,
\[
|\Omega|^2=2,\qquad \Omega\wedge\Omega=2\,dV_g.
\]
This is the correct normalization for the compatible orthogonal almost-complex structure; the coefficient vector, not the form, has norm \(1\).

The structure equations give directly
\[
d\omega_i=(h_j+h_k-2W_i)e^{0jk}.
\]
Therefore
\[
d\Omega=\sum_{i=1}^2(x_i'-\mu_i x_i)e^{0jk},
\qquad \mu_i=2W_i-h_j-h_k.
\]
Writing
\[
\rho=\sqrt{\frac{9p^2-1}{R}},\qquad k=\frac{(1-p^2)\rho}{2},
\]
the explicit functions satisfy
\[
\mu_1=\frac{k}{2}\frac{d}{dp}\log X_1
=-\frac{3(1+p)^3\rho}{4p(3p+1)},
\]
\[
\mu_2=\frac{k}{2}\frac{d}{dp}\log X_2
=\frac{3(1-p)^3\rho}{4p(3p-1)}.
\]
Hence \(x_i'=\mu_i x_i\), proving
\[
\boxed{d\Omega=0.}
\]
This checks the closure signs directly, independently of the invariance tower.

### 4. Strictness

Define
\[
C_i=W_i-W_j-W_k,\qquad b_i=h_i+C_i.
\]
The orthonormal-frame connection gives
\[
|\nabla\Omega|^2
=2\left[
X_1\mu_1^2+X_2\mu_2^2+b_3^2+X_1b_2^2+X_2b_1^2
\right].
\]
Substitution yields exactly
\[
\boxed{q(p)=\frac{36(1-p^2)^3}{R^3}.}
\]
It is positive everywhere on \(I\), tends to \(32/3\) at \(p=1/3\), and tends to zero at \(p=1\). Since an integrable compatible almost-complex structure with closed fundamental form is Kähler, \(q>0\) proves pointwise strictness throughout the interior.

### 5. Exact proof of the opposite-chirality Weyl claim

Use the curvature-operator convention in which a constant sectional curvature \(c\) metric has \(\mathcal R=c\,\mathrm{Id}\). The Cartan connection gives
\[
K_{0i}=-(h_i'+h_i^2),
\]
and the mixed curvature entry
\[
P_i:=\langle\mathcal R(e^{0i}),e^{jk}\rangle
=-(C_i'+h_iC_i).
\]
Equivalently,
\[
P_i=-2h_iW_i-C_kh_j-C_jh_k.
\]
This fixes the mixed-curvature sign unambiguously.

The same diagonal-metric symmetries make \(\mathcal R\) block diagonal on
\[
\operatorname{span}\{e^{0i},e^{jk}\}.
\]
Einstein implies \(K_{jk}=K_{0i}\), so its eigenvalue on
\[
\phi_i^-=\frac{e^{0i}-e^{jk}}{\sqrt2}
\]
is \(K_{0i}-P_i\).

The remaining exact certificate is especially short:
\[
\boxed{(h_i-C_i)'+h_i(h_i-C_i)=1,\qquad i=1,2,3.}
\]
For verification using only rational expressions, put \(D_i=V_i-V_j-V_k\). The boxed identities are precisely
\[
k^2\left[
\frac{d}{dp}(H_i-D_i)+(\ell+H_i)(H_i-D_i)
\right]=1.
\]
Again, clearing denominators proves them by polynomial expansion.

Thus
\[
K_{0i}-P_i=-1,\qquad
\mathcal R|_{\Lambda^-}=-\mathrm{Id}.
\]
Since \(s/12=-1\),
\[
\mathcal R|_{\Lambda^-}=W^-+\frac{s}{12}\mathrm{Id}
\quad\Longrightarrow\quad
\boxed{W^-=0.}
\]
This is indeed the chirality opposite to the self-dual form \(\Omega\). Reversing orientation exchanges the names \(W^+\) and \(W^-\).

As a useful normalization check, at \(p=1/2\) the \(W^+\) eigenvalues are
\[
\frac1{343}(124,-548,424).
\]
For the norm-\(\sqrt2\) form \(\Omega\),
\[
|W^+(\Omega)^\perp|^2=\frac{2430}{2401}.
\]
Using \(\Omega/\sqrt2\) instead divides this squared quantity by \(2\); numerical reports of \(\eta\) must specify that convention.

### 6. End extension: a separate, but provable, statement

The foregoing already proves exact local existence on the open interval. Endpoint geometry is not needed for that theorem.

#### Finite endpoint

Put \(\delta=p-1/3\), and let \(t=0\) at the finite endpoint. The rational formulas imply analytically
\[
\delta=\frac29t^2+O(t^4),
\]
and
\[
a_1=t\,b(t^2),\quad b(0)=1,\qquad
a_2,a_3\ \text{analytic in }t^2,
\]
\[
a_2-a_3=t^4c(t^2),\qquad
x_1\ \text{analytic in }t^2,\qquad
x_2=t\,d(t^2).
\]
The analyticity assertion follows by setting \(r=\sqrt\delta\): \(dt/dr\) is analytic, even, and nonzero at zero, so its inverse is analytic and odd.

These orders prove smoothness in the appropriate disk-bundle model, including the previously missing check for \(\Omega\). Locally write
\[
\sigma_1=d\psi+\beta,\qquad
\zeta:=\sigma_2+i\sigma_3=e^{2i\psi}\zeta_0,\qquad
z=t e^{i\psi},
\]
where \(\beta,\zeta_0\) are forms on the bolt chart. Then
\[
dt+it\sigma_1=e^{-i\psi}(dz+iz\beta),
\qquad
dt-it\sigma_1=e^{i\psi}(d\bar z-i\bar z\beta).
\]

The trace-free horizontal part of the metric has weight \(4\) and coefficient \(a_2^2-a_3^2=O(t^4)\), hence is smooth. The radial-circle correction is also smooth because
\[
a_1^2-t^2=t^4\,(\text{analytic in }t^2).
\]

For the mixed part of \(\Omega\), write
\[
\begin{aligned}
&x_2\bigl(a_2\,dt\wedge\sigma_2+a_1a_3\,\sigma_3\wedge\sigma_1\bigr)\\
&\quad=\frac{x_2(a_2+ba_3)}2
\,\operatorname{Re}\bigl((dt+it\sigma_1)\wedge\zeta\bigr)\\
&\qquad+\frac{x_2(a_2-ba_3)}2
\,\operatorname{Re}\bigl((dt-it\sigma_1)\wedge\zeta\bigr).
\end{aligned}
\]
The two coefficients are respectively \(t\) times an analytic even function and \(t^3\) times an analytic even function. They cancel the angular weights \(1\) and \(3\) through \(te^{i\psi}=z\) and \(t^3e^{3i\psi}=z^3\). The \(x_1\omega_1\) part is smooth as well, using \(t\,dt\wedge d\psi=dx\wedge dy\). Thus both \(g\) and \(\Omega\), and hence \(J\), extend smoothly.

This proof needs a collapsing \(X_1\)-circle of period \(2\pi\). The standard \(SL(2,\mathbb R)\) normalization provides it; the corresponding \(PSL(2,\mathbb R)\) circle has period \(\pi\) and gives a cone rather than this smooth bolt. For a surface quotient, take a torsion-free cocompact surface lattice lifted to \(SL(2,\mathbb R)\), excluding \(-I\). The extension is on the associated disk bundle
\[
\Gamma\backslash\bigl(SL(2,\mathbb R)\times_{S^1}\mathbb R^2\bigr).
\]

#### Infinite endpoint

As \(p\to1\),
\[
\sqrt G\sim\frac1{\sqrt2(1-p)},
\]
so radial distance diverges. Also,
\[
A_1\sim\frac8{3(1-p)},\quad
A_2\sim\frac{32}{3(1-p)^2},\quad
A_3\sim\frac8{1-p}.
\]
Consequently the smoothly attached lattice-quotient example is complete. These asymptotics establish the reported \(1:2:1\) growth rates; a precise ACH identification requires the additional normal-form comparison and is not needed for completeness.

### 7. Corrections and scope

- In `step57_classA_metric_only.py`, `check()` imports `step56_ake_propagate`, whereas the supplied file is named `step56_akeA_propagate.py`. Without an additional alias/module, that check does not run as written.
- Exact checks at finitely many rational points are not by themselves proofs of identities. The rational certificates above remove that gap; alternatively, a degree-bounded interpolation proof would require an explicit numerator-degree bound and enough exact samples.
- The invariant-ideal existence argument does **not** need primality, but its generator and tangency files are absent from this bounded input. The explicit metric proof bypasses them entirely.
- Local validity, smooth complete extension under the stated group conditions, and novelty are distinct. No supplied literature establishes whether this is a known family. Literature uncertainty does not weaken the exact local theorem.
- This pair does not resolve the closed negative-scalar Goldberg problem. In particular, its strictly positive invariant \(q\) has unattained infimum zero, so no compact quotient preserving this full pair can exist.