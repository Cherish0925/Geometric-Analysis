# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 28,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step28_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step28_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Check the mathematical correctness and scope of Theorem A and its supporting identities in the note step28_AK_gap_identity_nijenhuis_transport.md, for smooth diagonal Bianchi-IX O(-1) cells with an exact complex-hyperbolic collar (perpendicular class), in the units P/(8pi^2) with W dt volume units. Specifically: (1) the claim that g is conformal via u^2=phi/(a_g a_h) to a diagonal almost-Kahler metric with A_f=(A_gA_h)_T/2, and the symbolic formulas for the Nijenhuis scalar nu, kappa-shat=6nu^2, the linear transport lambda=nu_T/2+beta*nu, and the Chern identity as the exact Stokes formula (shat+2nu^2)w=d/dT[4P cosh q - P P'' - P'^2/2] (scripts step28_ak_nu_structure.py and step28_chern_stokes_check.py; compare with Apostolov-Armstrong-Draghici formulas (10),(13) in the supplied paper, including normalization of Omega, kappa, W3 eigenvalue lambda); (2) the four-step proof of Theorem A, especially the U(2) splitting |W+|^2=(3/2)W_ww^2+(1/2)(W_gg-W_hh)^2, the conformal weights (Wff/u^2, |W+|^2 dV invariance), boundary terms at the conical bolt (u^2~ct, phi~ct^2) and at the CH collar, and the use of the inherited relative identity 1-Phat=D_+-36Vexc-Sexc; (3) the bolt Nijenhuis charge law and the asymptotics nu~-1/(2ut), mu~t^{3/2}, and the leading-order cancellation of the 6G and (3/2)N densities at the bolt; (4) the far-field Hardy lemma and the CH Hardy radius x_H=3+(3/4)sqrt(15), including whether the stated inequality and the condition Lambda>=4sqrt3 are correctly derived, and whether the conclusion 'all gain is generated inside sinh^2 R<~6' is supported by the data or needs qualification; (5) the section-5 claims about non-diagonal extension (uniqueness of the relative SD harmonic form when b_+=0, the modulus a=int_E omega, near-symplectic zero sets, expected a-dependence of pinning and Chern terms). Identify any error, hidden assumption, or overstatement, and state the corrected mathematics precisely. Also say what in Theorem A is genuinely new structural information versus a rewriting of the inherited relative Weyl-volume identity.

## Integrated Scientific Memo

# Verification memo for Theorem A

## Verdict

The boxed identity in Theorem A is mathematically correct for the stated smooth diagonal, perpendicular \(O(-1)\) cells with an exact CH collar, once several normalization and terminology errors are corrected. Its proof is an exact repackaging of the inherited relative Weyl–volume/Chern–Weil identity, enriched by genuinely new almost-Kähler structure: canonical conformal reduction, exact pinning and Chern fluxes, Nijenhuis transport, forced bolt charge, bolt cancellation, and tail positivity.

The principal corrections are:

1. The canonical closed form and \(u\) have a factor-of-two ambiguity in the note.
2. \(\hat g=u^{2}g\) is almost-Kähler only on the complement of the bolt and is singular/degenerate at the bolt.
3. \(A_gv_g=-A_hv_h\) is false; the correct relation is \(v_g/A_g=-v_h/A_h\).
4. \(\hat s+2\nu^2\) is the Hermitian/Chern scalar, not the usual star scalar.
5. \(\Sigma\) alone is sign-indefinite, but \(12H+\Sigma\) is a nonnegative perfect square. Thus the identity can indeed be written with \(-\tfrac32N\) as its only negative term, without assuming \(s=-24\).
6. The Hardy conclusion applies to a terminal interval on which \(\Lambda\ge4\sqrt3\), not pointwise “wherever” this holds.
7. The non-diagonal extension is presently conditional: uniqueness is relative-cohomological, existence is not automatic, and the near-symplectic assertions require transversality.

---

## 1. Canonical conformal almost-Kähler structure

Let
\[
g=dt^2+a_f^2\sigma_f^2+a_g^2\sigma_g^2+a_h^2\sigma_h^2,
\qquad d\sigma_f=2\sigma_g\wedge\sigma_h .
\]

There are two equivalent normalizations.

### Standard almost-Kähler normalization

If
\[
\Omega=d(\phi\,\sigma_f),\qquad |\Omega|_{\hat g}^{2}=2,
\]
then self-duality gives
\[
\frac{\phi'}{\phi}=\frac{2a_f}{a_ga_h},
\]
and the conformal factor must be
\[
\boxed{u^2=\frac{2\phi}{a_ga_h}}.
\]
On CH,
\[
\phi=\frac12a_ga_h,
\]
so \(u=1\).

### Script/note normalization

The computations instead use the doubled form
\[
\omega=2\Omega=d(\mathcal P\,\sigma_f),\qquad
\mathcal P=A_gA_h,
\]
and then
\[
\boxed{u^2=\frac{\mathcal P}{a_ga_h}}.
\]
In this normalization \(\mathcal P=2\phi\). The note mixes these two conventions when it writes both \(d(\phi\sigma_f)\) and \(u^2=\phi/(a_ga_h)=1\) on CH.

With
\[
dT=u\,dt,\qquad A_i=ua_i,\qquad \mathcal P=A_gA_h,
\]
one obtains
\[
\mathcal P_T=2A_f,
\qquad
\boxed{A_f=\frac12(A_gA_h)_T}.
\]
Thus the almost-Kähler constraint is correct.

### Behavior at the perpendicular bolt

For a smooth perpendicular bolt,
\[
a_h=t+O(t^3),\qquad a_f=b+O(t^2),\qquad a_g=b+O(t^2),
\]
and
\[
\mathcal P\sim Ct^2,\qquad u^2\sim ct,\qquad T\sim \frac23\sqrt c\,t^{3/2}.
\]
Hence
\[
A_f,A_g\asymp T^{1/3},\qquad A_h\asymp T.
\]

Therefore:

> \(\hat g=u^2g\) is a genuine almost-Kähler metric on \(C\setminus E\), but it does not extend as a smooth positive-definite metric across the bolt \(E\). The canonical closed form vanishes on \(E\), and the relevant densities and endpoint fluxes remain integrable.

Calling the hatted end a “conical bolt” is inaccurate: it is an anisotropic power-law singular end.

---

## 2. Nijenhuis scalar, \(\kappa\), and \(W_3^+\)

Set
\[
v_i=(A_i)_T-\gamma_i,\qquad
\gamma_i=\frac{A_j^2+A_k^2-A_i^2}{A_jA_k}.
\]

The note’s relation
\[
A_gv_g=-A_hv_h
\]
is false. The correct identity is
\[
\boxed{\frac{v_g}{A_g}=-\frac{v_h}{A_h}},
\qquad\text{equivalently}\qquad
A_hv_g=-A_gv_h.
\]
This correction is also visible directly in `ak_hatted_structure.json`.

Define
\[
\boxed{
\nu=\frac{v_h}{A_h}=-\frac{v_g}{A_g}
=-\frac12\left(q_T+\frac{4\sinh q}{A_f}\right).
}
\]
With the AAD normalization \(|\Omega|^2=2\),
\[
|a|^2=\nu^2,\qquad |\nabla\Omega|^2=4\nu^2.
\]
AAD formula (10) therefore gives
\[
\boxed{\kappa-\hat s=6\nu^2},
\qquad
\kappa=6\widehat W^+_{\Omega\Omega}.
\]
This matches the symbolic output exactly.

The \(W_3^+\) eigenvalues on the \(J\)-anti-invariant two-plane are \(\pm\lambda\), with
\[
\boxed{
\lambda=\frac{\widehat W^+_{gg}-\widehat W^+_{hh}}2
=\frac12\nu_T+\beta\nu,
}
\]
where
\[
\boxed{
\beta=-\frac{(A_f)_T}{2A_f}+\frac{2\cosh q}{A_f}.
}
\]
Thus the note’s \(\lambda\) agrees with the AAD \(W_3^+\) eigenvalue. Diagonal symmetry gives \(W_2^+=0\).

The comment that the \(|a|^2\) term in AAD (13) “cancels” is plausible as an interpretation of the gauge-specialized formula, but the reliable result is the direct symbolic/Cartan identity above.

### Anti-invariant Ricci claim

The displayed formulas are correct:
\[
\widehat D
=
2\nu_T+\nu\left(
\frac{2(A_f)_T}{A_f}
-\frac{8\cosh q}{A_f}
+\frac{4A_f}{A_gA_h}
\right),
\]
and
\[
\widehat{\operatorname{Ric}}_{00}
-\widehat{\operatorname{Ric}}_{ff}
=
-2\nu^2-\frac{8\nu\sinh q}{A_f}.
\]

The statement “both vanish iff \(\nu=0\)” must be interpreted as vanishing identically on an open interval, not as a pointwise algebraic equivalence. On an interval, the nonzero branch from the second equation,
\[
\nu=-\frac{4\sinh q}{A_f},
\]
combined with the definition of \(\nu\), gives \(q_T=4\sinh q/A_f\); substitution in \(\widehat D=0\) forces \(q=0\), hence \(\nu=0\). At a single point, \(\nu_T\) can be adjusted independently, so pointwise equivalence does not follow.

---

## 3. Correct interpretation of the Chern–Stokes scalar

The usual star scalar satisfies
\[
\hat s_{\mathrm{star}}-\hat s
=|\nabla\Omega|^2=4\nu^2.
\]
The scalar representing the Chern/Hermitian connection is
\[
s^\nabla
=\frac{\hat s+\hat s_{\mathrm{star}}}{2}
=\hat s+2\nu^2.
\]

Thus the note’s symbol \(\hat s^*\) is misnamed. The verified Stokes identity is
\[
\boxed{
s^\nabla\,A_fA_gA_h
=
\frac d{dT}\left[
4\mathcal P\cosh q
-\mathcal P\mathcal P_{TT}
-\frac12\mathcal P_T^2
\right].
}
\]

Also
\[
A_fA_gA_h
=\frac12\mathcal P\mathcal P_T
=\frac d{dT}\frac{\mathcal P^2}{4}.
\]

On the CH end,
\[
\mathcal P=\sinh^2T,\qquad q=0,
\]
and the bracket is
\[
-6\sinh^4T.
\]
If \(X=\sinh^2R\), then
\[
\hat V=\int d\hat V=\frac{X^2}{4}=V_{\rm CH}
\]
and
\[
\boxed{
\int s^\nabla\,d\hat V=-6X^2=-24V_{\rm CH}.
}
\]

At the perpendicular bolt,
\[
\mathcal P=O(t^2),\quad
\cosh q=O(t^{-1}),\quad
\mathcal P_T=O(t^{1/2}),\quad
\mathcal P_{TT}=O(t^{-1}),
\]
so every term in the bracket is \(O(t)\). The bolt contributes no limiting Stokes flux.

---

## 4. Verification of Theorem A

Write
\[
p=\widehat W^+_{\Omega\Omega},\qquad
\delta=p+4,\qquad
2\lambda=\widehat W^+_{gg}-\widehat W^+_{hh}.
\]

### 4.1 \(U(2)\) splitting

Since \(\widehat W^+\) is diagonal and trace-free,
\[
\boxed{
|\widehat W^+|^2
=\frac32p^2
+\frac12(\widehat W^+_{gg}-\widehat W^+_{hh})^2.
}
\]
Equivalently,
\[
|\widehat W^+|^2
=24-12\delta+\frac32\delta^2+2\lambda^2.
\]

This coefficient convention agrees with AAD: \(W_3^+\) has eigenvalues \(\pm\lambda\), hence norm squared \(2\lambda^2\).

### 4.2 Conformal weights

In dimension four,
\[
\widehat W^+=u^{-2}W^+
\]
as an endomorphism of normalized self-dual two-forms, and
\[
|W^+|_g^2\,dV_g
=
|\widehat W^+|_{\hat g}^2\,dV_{\hat g}.
\]
Thus, in particular,
\[
\widehat W_{ff}=W_{ff}/u^2,
\qquad dV_{\hat g}=u^4W\,dt.
\]

Using \(\hat V=V_{\rm CH}\),
\[
\boxed{
D_+
=
24V_{\rm exc}
+12\int\delta\,d\hat V
-\frac32Q_\delta-\frac12Q_A.
}
\]

### 4.3 Mean of \(\delta\)

Since
\[
\kappa=\hat s+6\nu^2=s^\nabla+4\nu^2,
\]
we have
\[
\delta=\frac{\kappa}{6}+4
=\frac{s^\nabla}{6}+\frac23\nu^2+4.
\]
Using the Chern integral and \(N=4\int\nu^2d\hat V\),
\[
\boxed{\int\delta\,d\hat V=\frac N6}.
\]

### 4.4 Scalar conformal formula and volume

The conformal scalar formula gives
\[
\hat s=u^{-3}(-6\Delta_gu+su).
\]
After integration by parts,
\[
\boxed{
\int\hat s\,d\hat V
=
6G+\int su^2W\,dt.
}
\]
The endpoint term vanishes because
\[
uu'W=O(t)\to0
\]
at the bolt, while \(u\equiv1\) and \(u'=0\) on the exact collar.

Also,
\[
\int\hat s\,d\hat V
=
\int s^\nabla\,d\hat V-2\int\nu^2d\hat V
=
-24V_{\rm CH}-\frac N2.
\]
This yields
\[
\boxed{
V_{\rm exc}
=
H+\frac G2+\frac N{24}
+\frac1{12}\int(s+24)u^2W\,dt.
}
\]

### 4.5 Substitution into the inherited identity

Substituting these formulas into
\[
1-\widehat P
=
D_+-36V_{\rm exc}-S_{\rm exc},
\qquad
S_{\rm exc}
=\int W\left(\frac{s^2}{48}-12\right)dt,
\]
gives exactly
\[
\boxed{
\widehat P-1
=
12H+6G+\frac32Q_\delta+\frac12Q_A-\frac32N+\Sigma,
}
\]
with
\[
\Sigma
=
\int W(s+24)(u^2-1)\,dt
+\int W\frac{(s+24)^2}{48}\,dt.
\]

So the boxed theorem and all coefficients are correct.

---

## 5. Sign structure: correction and stronger formulation

The note says that all terms except \(-\tfrac32N\) are nonnegative. As written with a separate \(\Sigma\), this is false: \(\Sigma\) need not have fixed sign.

However, there is an exact completion of the square:
\[
12(u^2-1)^2
+(s+24)(u^2-1)
+\frac{(s+24)^2}{48}
=
12\left(u^2+\frac{s}{24}\right)^2.
\]
Therefore define
\[
H_s:=\int W\left(u^2+\frac{s}{24}\right)^2dt.
\]
Then Theorem A is equivalently
\[
\boxed{
\widehat P-1
=
12H_s+6G+\frac32Q_\delta+\frac12Q_A-\frac32N.
}
\]

This is the cleanest form. It proves, for all metrics in the stated class—not only \(s=-24\)—that the Nijenhuis energy is the only term carrying a negative coefficient.

Consequently, if \(\nu\equiv0\),
\[
\widehat P-1
=
12H_s+6G+\frac32Q_\delta+\frac12Q_A\ge0.
\]
In the perpendicular class equality is excluded by the bolt asymptotics, so an integrable canonical structure cannot produce a subthreshold cell.

For \(s\equiv-24\), \(H_s=H\) and \(\Sigma=0\), recovering the note’s special form.

---

## 6. Bolt Nijenhuis charge and leading cancellation

Near the perpendicular bolt,
\[
q=\log(b/t)+O(t^2),
\qquad
q'+\frac{4\sinh q}{a_f}
=\frac1t+O(t).
\]
Since \(q_T=q'/u\) and \(A_f=ua_f\),
\[
\boxed{
\nu=-\frac1{2ut}+O(t^{-1/2})
\asymp t^{-3/2}.
}
\]

The transport equation is
\[
\nu_T+2\beta\nu=2\lambda.
\]
Let
\[
\frac{\mu_T}{\mu}=2\beta.
\]
Then
\[
\mu
=
\frac{C}{ua_f}
\exp\left(\int\frac{4\cosh q}{a_f}\,dt\right)
\asymp t^{3/2}.
\]
Therefore
\[
K=\lim_{t\to0}\mu\nu
\]
is finite and nonzero after fixing the multiplicative normalization of \(\mu\). Since \(\nu=0\) on the exact CH collar,
\[
\boxed{
K=-2\int_{\rm cell}\mu\lambda\,dT.
}
\]

The nonzero numerical value of \(K\) is normalization-dependent; the statement \(K\ne0\) and the charge law are invariant.

If
\[
u^2=ct+O(t^3),
\]
then
\[
6u'^2W\longrightarrow\frac32cb^2,
\]
while
\[
\frac32(4\nu^2u^4W)
=
6\nu^2u^4W
\longrightarrow\frac32cb^2.
\]
Thus
\[
\boxed{
6G-\frac32N
}
\]
has exact leading-order density cancellation at the bolt. This part of the note is correct.

A useful exact reformulation is obtained by setting
\[
\psi=\mu\nu,\qquad \rho=\frac{w}{\mu^2},
\quad w=A_fA_gA_h.
\]
Then
\[
\lambda=\frac{\psi_T}{2\mu},
\]
and
\[
\frac12Q_A-\frac32N
=
\int \rho\left(\frac12\psi_T^2-6\psi^2\right)dT.
\]
Moreover,
\[
Q_A=\int\rho\,\psi_T^2\,dT
\ge
\frac{K^2}{\int\rho^{-1}\,dT},
\]
provided the outer normalization is fixed. This makes the “unwinding cost” precise.

### Numerical-script caveats

The symbolic transport identity is valid, but two numerical diagnostics in the supplied JSON are not reliable:

- `law_residual` is hard-coded to zero by an `if False` branch.
- `transport_rel_residual_max` is enormous because `np.gradient` is applied using a cumulative quadrature-weight surrogate rather than the actual node coordinate.

The integrated charge residual `law_residual_from_i30 ≈ 10^{-12}` is the meaningful numerical check.

---

## 7. Far-field Hardy lemma

Starting from
\[
\nu_T=2\lambda-2\beta\nu,
\]
one gets
\[
(\nu^2w)_T
=
4\nu\lambda w+\Lambda\nu^2w,
\qquad
\Lambda=\frac{w_T}{w}-4\beta.
\]

Let \([T_0,T_1]\) be a terminal interval whose right endpoint lies in the exact collar, so \(\nu(T_1)=0\), and assume
\[
\Lambda\ge c>0
\]
throughout the interval. Integration gives
\[
cI+\nu(T_0)^2w(T_0)
\le4\sqrt{IJ},
\]
where
\[
I=\int_{T_0}^{T_1}\nu^2w\,dT,\qquad
J=\int_{T_0}^{T_1}\lambda^2w\,dT.
\]
Hence
\[
\boxed{I\le\frac{16}{c^2}J}.
\]
Therefore
\[
2J-6I\ge0
\]
whenever
\[
\boxed{c\ge4\sqrt3}.
\]

The wording must be “on a terminal interval where \(\Lambda\ge4\sqrt3\),” because the boundary condition \(\nu=0\) at the collar is essential.

On CH,
\[
\boxed{
\Lambda_{\rm CH}
=
\frac{8x-3}{\sqrt{x(1+x)}},
\qquad x=\sinh^2R.
}
\]
Solving \(\Lambda_{\rm CH}=4\sqrt3\) yields
\[
\boxed{
x_H=3+\frac34\sqrt{15}\approx5.90474.
}
\]
The other root of the squared equation is inadmissible because \(8x-3<0\).

### Scope of the localization claim

For the supplied \(x_0=.038\) data,
\[
x_*=5.9488,\qquad
\text{far Nijenhuis sector}=0.00588>0,
\]
and
\[
\frac{\int_{\rm far}\nu^2d\hat V}
{\int_{\rm far}\lambda^2d\hat V}
=0.1749<\frac13.
\]
Thus the negative Nijenhuis–\(W_3\) contribution is indeed generated before the final crossing near \(x\simeq6\) in that sample. The summaries indicate the same behavior for the other two recorded optimized cells.

The correct general statement is:

> Once an actual cell enters a terminal region satisfying \(\Lambda\ge4\sqrt3\), its combined \(W_3\)–Nijenhuis sector can no longer lower the gap.

It is not a universal theorem that every diagonal cell reaches this regime at \(x\simeq6\), because outside the exact collar \(x\) is only the chosen cell coordinate, not intrinsically \(\sinh^2R\). The phrase “all gain is generated inside \(\sinh^2R\lesssim6\)” should therefore be qualified as a conclusion for the displayed numerical family and for the Nijenhuis sector in this decomposition, not as a theorem for arbitrary competitors.

The Hardy estimate is sufficient but not sharp. The exact tail problem is the weighted spectral form
\[
\int \rho\left(\frac12\psi_T^2-6\psi^2\right)dT,
\]
whose sign is governed by the first eigenvalue of
\[
-\rho^{-1}(\rho\psi_T)_T
\]
relative to \(12\).

---

## 8. Non-diagonal extension

### Uniqueness

Suppose two closed self-dual forms agree with the prescribed CH form on the collar. Their difference \(\eta\) is compactly supported and defines a relative class in \(H^2(C,\partial C)\). Since \(\eta\) is self-dual,
\[
\int_C\eta\wedge\eta=\int_C|\eta|^2\,dV\ge0.
\]
For an \(O(-1)\) cell, the relative intersection form is negative definite, so the left side is \(\le0\). Hence \(\eta=0\).

Thus uniqueness is correct, but the precise hypothesis is:

> the collar-relative intersection form has no positive direction,

not merely an unqualified statement that “\(b_+=0\).”

### Existence

Existence is not automatic. Solving
\[
d\omega=0,\qquad \omega\in\Lambda^+,
\]
with a prescribed full collar germ is an overdetermined boundary-extension problem. It is solved by the ODE in the diagonal class; it cannot be assumed for a general non-diagonal metric. Therefore \(a(g)=\int_E\omega\) is defined only on the subset where such an extension exists, unless one replaces it by a suitable global period-map construction after gluing.

### The modulus \(a\)

With the standard normalization \(|\Omega|^2=2\),
\[
a=\int_E\Omega.
\]
In the perpendicular diagonal class, \(\Omega|_E=0\), so \(a=0\). In an aligned Kähler cell, \(a>0\).

For relative class
\[
[\Omega]=[\Omega_{\rm CH}]-a\,e,\qquad e^2=-1,
\]
one expects
\[
\operatorname{Vol}(\hat g)
=
V_{\rm CH}-\frac{a^2}{2}
\]
in physical normalization, while
\[
\int s^\nabla\,dV
=
4\pi c_1(J)\cdot[\Omega]
\]
contains a linear \(a\)-term whose sign depends on \(c_1(J)\cdot E\). Thus the expected quadratic pinning and linear Chern dependence are mathematically well motivated, but their coefficients must be stated only after fixing:

- whether the basic form is \(\Omega\) or \(2\Omega\);
- the exceptional-sphere orientation;
- physical versus \(W\,dt\) volume units;
- the relative first Chern class.

The stronger aligned-cell formula proposed in one branch is not needed for verification of the perpendicular theorem and should not be asserted without a separate, fully normalized derivation.

### Zero sets

A transverse section of the rank-three bundle \(\Lambda^+\) over a four-manifold has a one-dimensional zero set. Hence a generic closed self-dual form can be near-symplectic under an appropriate transversality theorem.

But:

- prescribed collar data restrict the admissible space, so transversality is not automatic;
- the perpendicular diagonal form vanishes on the entire exceptional sphere, a two-dimensional non-transverse zero set.

Therefore the note’s zero-set discussion is a plausible program, not a proved extension.

### \(W_2^+\) coefficient

In block form,
\[
W^+
=
\begin{pmatrix}
p & \zeta^T\\
\zeta & -\frac p2 I+W_3
\end{pmatrix},
\]
so
\[
|W^+|^2
=
\frac32p^2+2|\zeta|^2+|W_3|^2.
\]
If \(W_3\) has eigenvalues \(\pm\lambda\), then
\[
|W_3|^2=2\lambda^2.
\]

Thus the additional term is \(2|\zeta|^2\). Writing it as \(2|W_2^+|^2\) is correct only if \(|W_2^+|\) denotes the off-block vector norm \(|\zeta|\). If \(W_2^+\) denotes the full curvature tensor component, its Hilbert–Schmidt norm already includes that factor.

---

## 9. What is genuinely new

The boxed equality is not an independent topological identity or a new lower bound. Algebraically it follows from
\[
1-\widehat P
=
D_+-36V_{\rm exc}-S_{\rm exc}
\]
after substituting the Weyl splitting, Chern flux, and conformal scalar formula. In that sense, Theorem A is an exact rewriting of the inherited relative \(2\chi+3\tau\)/Weyl–volume identity.

Its genuinely new structural content is the identification of the geometric mechanism behind that identity:

1. Every diagonal perpendicular cell admits a canonical conformal almost-Kähler representation on the complement of the bolt.
2. The hatted volume is exactly pinned:
   \[
   \hat V=V_{\rm CH}.
   \]
3. The Chern flux gives
   \[
   \int\delta\,d\hat V=N/6.
   \]
4. The entire scalar/conformal part is the square
   \[
   12\int W\left(u^2+\frac{s}{24}\right)^2dt.
   \]
5. The \(W_3^+\) mode and nonintegrability obey the first-order transport law
   \[
   \lambda=\frac12\nu_T+\beta\nu.
   \]
6. The perpendicular bolt forces a nonzero Nijenhuis charge.
7. The conformal-gradient and Nijenhuis densities cancel to leading order at the bolt.
8. A terminal Hardy/spectral estimate makes the far Nijenhuis sector nonnegative.

Thus the strongest corrected form is
\[
\boxed{
\widehat P-1
=
12\int W\left(u^2+\frac{s}{24}\right)^2dt
+6G+\frac32Q_\delta+\frac12Q_A-\frac32N.
}
\]

What remains unresolved is a sharp near-zone inequality coupling the forced charge/Nijenhuis field to the conformal factor and \(\delta\) before the Hardy-positive tail. That is the exact analytic object needed to turn the structural decomposition into a uniform lower bound.