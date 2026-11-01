# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 64,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step64_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step64_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify and strengthen the mathematics of the Step-64 note. Focus on four load-bearing points: (1) the diffuse torsion scale inferred from Theorem 63.T, including constants in equations (64.3)-(64.4); (2) the weak H^{-1}-type estimate (64.7)-(64.9) derived from the Apostolov–Armstrong–Drăghici transition identity—check whether integration by parts really removes every curvature derivative, what norms/boundary hypotheses are needed, and whether the claimed dependence on Ric'', rho_*'', W3 is valid; (3) the scaling argument that topologically required Nijenhuis zeros can shrink without a scale-invariant L2 curvature payment; and (4) Proposition 64.H for a transverse C^2 spinor zero—check the Hopf-map formulas, frame-twist density, logarithmic coefficients, and the conclusion that the normalized SW Bloch field cannot directly be used as the smooth J in Theorem 63.T. Give corrected theorem statements with exact scope where needed, and explain what these results genuinely imply for the open-range Einstein-gap problem. Use the cited AAD source and prior Step-63 theorem as grounding; do not assume an unproved global near-minimizer decomposition.

## Integrated Scientific Memo

# Verification and strengthening of Step 64

The principal identities survive verification, but several conclusions require narrower scope. In particular, Theorem 63.T fixes the **harmonic projection** of the frame twist, not its full norm; the AAD weak estimate is valid but noncoercive at the diffuse scale; shrinking Nijenhuis cores are not yet a geometric construction; and the exact Hopf coefficients apply only to the conformal linear zero model.

Throughout, \(P=\int|\operatorname{Ric}^{\circ}|^2\), \(|\Omega|^2=2\), and
\[
\gamma_J^-=\rho_0^J+t_J^-,
\qquad t_J^-=(\alpha\wedge\beta)^-.
\]
Write \(\mathsf H^-\) for projection onto harmonic ASD forms, and normalize \(h_a^-\) by \([h_a^-]=a^-\). For the maximizing sign class, set
\[
K:=|a^-|_g^2=k+\Pi.
\]

## 1. What Theorem 63.T actually forces

Since \([\gamma_J]=2\pi a\), the Hodge argument in Step 63 gives the exact vector identity
\[
\boxed{\mathsf H^-(t_J^-)=2\pi h_a^--\mathsf H^-(\rho_0^J).}
\tag{1}
\]
Moreover,
\[
\|\rho_0^J\|_2^2=\frac12\|\operatorname{Ric}_0'\|_2^2\le\frac P2.
\]
Consequently,
\[
\boxed{
\|\mathsf H^-(t_J^-)-2\pi h_a^-\|_2\le\sqrt{P/2},
\qquad
\|t_J^-\|_2\ge
\bigl(2\pi\sqrt K-\sqrt{P/2}\bigr)_+.
}
\tag{2}
\]

These statements hold for every smooth orthogonal \(J\) with \(c_1(J)=a\), without an almost-Kähler or SW assumption.

### Corrections to (64.1)–(64.2)

If \(P=o(k)\), then \(\|\rho_0^J\|_2=o(\sqrt k)\), but one obtains only a **lower bound** on \(\|t_J^-\|_2\). Indeed,
\[
\|t_J^-\|_2^2
=
\|2\pi h_a^--\mathsf H^-(\rho_0^J)\|_2^2
+\|(1-\mathsf H^-)t_J^-\|_2^2.
\tag{3}
\]
Thus the asserted asymptotic equality in (64.1) additionally requires
\[
\|(1-\mathsf H^-)t_J^-\|_2=o(\sqrt k).
\]
Under that efficiency hypothesis,
\[
\boxed{t_J^-=+2\pi h_a^-+o_{L^2}(\sqrt k).}
\tag{4}
\]
The minus sign in (64.2) is incorrect for the definition \(t_J^-=\gamma_J^--\rho_0^J\). In the AK convention \(t_J^-=-(a\wedge Ja)^-\), it is \(\mathsf H^-((a\wedge Ja)^-)\), not \(\mathsf H^-(t_J^-)\), that has the opposite sign.

Neither \(\Pi=o(k)\) nor diffuseness of harmonic representatives follows from \(P=o(k)\).

### Exact torsion constants

For an almost-Kähler structure, AAD (21) gives
\[
\nabla\Omega=a\otimes\phi-Ja\otimes J\phi,\qquad
u=|a|^2=\frac14|\nabla\Omega|^2.
\]
Because \(a\wedge Ja\) is decomposable,
\[
|t_J^-|^2=\frac12u^2.
\]
The corrected exact version of (64.3) is therefore
\[
\boxed{
\frac12\int u^2\ge
\bigl(2\pi\sqrt K-\sqrt{P/2}\bigr)_+^2.
}
\tag{5}
\]
If \(P=o(k)\) and \(K=O(k)\), this gives
\[
\frac12\int u^2\ge4\pi^2K-o(k).
\]
Without \(K=O(k)\), the relative statement \(4\pi^2K(1-o(1))\) remains valid, but the additive error need not be \(o(k)\).

For \(V=\operatorname{Vol}(M,g)\),
\[
u_{\rm rms}:=\left(V^{-1}\int u^2\right)^{1/2}
\ge\sqrt{\frac2V}\bigl(2\pi\sqrt K-\sqrt{P/2}\bigr)_+.
\tag{6}
\]
At the **additional volume hypothesis** \(V=2\pi^2A(1+o(1))\),
\[
\boxed{
u_{\rm rms}\ge2\sqrt{K/A}\,(1-o(1)),
\qquad
\|\nabla\Omega\|_{L^4,\mathrm{av}}
\ge2\sqrt2(K/A)^{1/4}(1-o(1)).
}
\tag{7}
\]
Here \(\|F\|_{L^4,\mathrm{av}}=(V^{-1}\int|F|^4)^{1/4}\).

Thus the coefficient \(2\) for \(u_{\rm rms}\) is correct. The second assertion in (64.4) should refer to normalized \(L^4\) size, not ordinary \(L^2\) RMS. Concentration can make \(\int u\) small while preserving \(\int u^2\); typical pointwise size and \(L^2\) RMS require diffuseness and an upper moment bound.

For general orthogonal \(J\), Theorem 63.T also gives
\[
\boxed{
\int|\nabla\Omega|^4
\ge32\bigl(2\pi\sqrt K-\sqrt{P/2}\bigr)_+^2.
}
\tag{8}
\]
Wu existence supplies such a \(J\), but does **not** supply \(d\Omega=0\). The AK diffuse template is therefore a special realization problem, not a necessary description of unrestricted near-minimizers.

## 2. The AAD weak estimate: valid, with precise scope

Put \(S=\operatorname{Ric}''\) and \(\sigma=\rho_*''\). AAD (20) gives \(\kappa-s=6u\), so Corollary 1, equation (37), is exactly
\[
2d^Ju=
2\langle\delta W_3^+,\Omega\rangle
+2\delta\sigma-\langle\sigma,\nabla_J\Omega\rangle
+\langle A^+,\Omega\rangle,
\tag{9}
\]
where
\[
A_Z=(d^\nabla S)_Z+\iota_{JZ}d\rho_{\rm Ric},
\qquad
d\rho_{\rm Ric}=*(J\delta S)
\tag{10}
\]
by AAD (26). No constant-scalar assumption is needed.

### Corrected weak transport theorem

On a smooth closed almost-Kähler four-manifold, for every smooth one-form \(\eta\),
\[
\boxed{
\begin{aligned}
2\left|\int\langle d^Ju,\eta\rangle\right|
\le C\bigl[
&(\|\sigma\|_2+\|S\|_2)\|\nabla\eta\|_2\\
&+(\|W_3^+\|_2+\|\sigma\|_2+\|S\|_2)
  \|\sqrt u\,\eta\|_2
\bigr],
\end{aligned}}
\tag{11}
\]
with a dimensional constant \(C\).

This strengthens (64.7): the \(W_3^+\) term requires no derivative of \(\eta\). The derivative removal is as follows.

* **The \(W_3^+\) contraction is already algebraic.** Since \(W_3^+\) takes values orthogonal to \(\Omega\), differentiating
  \(\langle W_3^+(\cdot),\Omega\rangle=0\) gives
  \[
  |\langle\delta W_3^+,\Omega\rangle|
  \le C|W_3^+|\,|\nabla\Omega|.
  \]
  This is also the algebraic contraction used in AAD’s proof of Lemma 5.

* **The \(\delta\sigma\) term** pairs with \(d\eta\) after integration by parts. Its algebraic companion is bounded by
  \(2\|\sigma\|_2\|\sqrt u\,\eta\|_2\).

* **The \(d^\nabla S\) term** moves its derivative onto \(\eta\otimes\Omega\).

* **The \(d\rho_{\rm Ric}\) term** is first replaced using (10). It becomes \(\delta S\) contracted against an algebraic one-form \(B(J,\Omega,\eta)\). Integrating by parts gives
  \[
  \left|\int\langle\delta S,B\rangle\right|
  \le C\|S\|_2
  \bigl(\|\nabla\eta\|_2+\|\sqrt u\,\eta\|_2\bigr).
  \]
  Derivatives of \(J\) and \(\Omega\) are controlled algebraically by \(\sqrt u\).

Thus **every curvature derivative is removed**, and the stated dependence on \(W_3^+,\rho_*'',\operatorname{Ric}''\) is valid. Equation (10) is essential: no independent norm of \(d\rho_{\rm Ric}\), scalar-curvature derivative, or full Cotton tensor is needed.

### Norm and boundary qualifications

Define
\[
D_u(\eta)=\|\nabla\eta\|_2+\|\sqrt u\,\eta\|_2,
\qquad
\|\xi\|_{\dot{\mathcal H}^{-1}_u}
=\sup_{D_u(\eta)\le1}\left|\int\langle\xi,\eta\rangle\right|.
\tag{12}
\]
This is a weighted homogeneous dual seminorm, not automatically the usual inhomogeneous \(H^{-1}\) norm. Null test directions are handled by quotienting the kernel of \(D_u\); the functional in (11) annihilates that kernel.

The estimate extends to the corresponding completion of smooth tests. On a domain \(U\), it holds without boundary terms for compactly supported tests, or \(H^1_0\) tests with the weighted integrability required in (12). Arbitrary boundary tests leave curvature-flux terms. Interior \(L^2\) curvature control alone does not control those traces. The same qualification is indispensable on a punctured manifold.

Since \(\|S\|_2\le\sqrt P\), (64.8) is valid:
\[
\|d^Ju\|_{\dot{\mathcal H}^{-1}_u}
\le C(\|W_3^+\|_2+\|\rho_*''\|_2+\sqrt P).
\tag{13}
\]
Using the verified identity 63.AK,
\[
P=2\|\gamma_J^-\|_2^2+\int u(5u+s)
  +2\|\rho_*''\|_2^2+4\|W_3^+\|_2^2,
\]
one obtains
\[
2\|\rho_*''\|_2^2+4\|W_3^+\|_2^2
\le P+\int u(|s|-5u)_+,
\]
and hence
\[
\boxed{
\|d^Ju\|_{\dot{\mathcal H}^{-1}_u}^2
\le C\left[P+\int u(|s|-5u)_+\right].
}
\tag{14}
\]
Thus (64.9) is correct. It annihilates the constant amplitude mode and does not control twist orientation or its harmonic projection.

## 3. A stronger constraint on the diffuse AK template

Two consequences clarify why (14) cannot price that template.

### Mean torsion is a period/volume slack

From AAD’s canonical Chern form,
\[
\gamma_J^+=\frac{s+2u}{4}\Omega+\rho_*'',
\]
and \(d\Omega=0\),
\[
2\pi a\cdot[\Omega]=\int(s/2+u).
\]
At \(s=-4\),
\[
\boxed{\int u=2V+2\pi a\cdot[\Omega].}
\tag{15}
\]

With \(V_*=2\pi^2|a^+|^2=2\pi^2(A+\Pi)\), this is equivalently
\[
\int u=
2\sqrt V(\sqrt V-\sqrt{V_*})
+2\pi\left(a^+\cdot[\Omega]+|a^+|\,|[\Omega]|\right).
\tag{16}
\]
The second term is nonnegative by Cauchy–Schwarz in \(H_g^+\). The first is nonnegative **when the monopole scalar-curvature estimate supplies \(V\ge V_*\)**; that input is not part of bare AK geometry.

Thus diffuse torsion must be financed by volume excess and/or period misalignment. It need not be financed by \(P\).

### The diffuse template requires substantial Weyl load

Let
\[
E_\perp=2\|\rho_*''\|_2^2+4\|W_3^+\|_2^2.
\]
The triangle inequality gives
\[
\|\gamma_J^-\|_2
\le\sqrt{P/2}+\|u\|_2/\sqrt2.
\]
Substitution in 63.AK yields the exact lower bound
\[
\boxed{
E_\perp\ge4\int u-6\int u^2-2\sqrt P\,\|u\|_2.
}
\tag{17}
\]
For an efficient diffuse profile with \(K\simeq k\), \(V\simeq2\pi^2A\), \(k/A\to0\), and \(P=o(k)\),
\[
\int u\simeq4\pi^2\sqrt{kA},
\qquad
\int u^2\simeq8\pi^2k.
\]
The exact identity and (17) then give
\[
E_\perp\simeq4\int u\simeq16\pi^2\sqrt{kA}.
\tag{18}
\]
The required \(W_2/W_3\) energy is therefore much larger than \(k\), although it remains a vanishing fraction of host-scale energy \(A\). The right side of (14) has this same \(\sqrt{kA}\) scale; it cannot exclude torsion fluctuations whose squared weak norm is only of order \(k\).

There is also a second-jet consequence. AAD (19) bounds \(\rho_*''\) by contracted \(\nabla^2\Omega\). In a gauge with \(b=0\) at a point, AAD (23) bounds \(W_3^+\) by \(\nabla^2\Omega\) and \(u\). Hence
\[
E_\perp\le C\left(\|\nabla^2\Omega\|_2^2+\int u^2\right),
\]
so
\[
\boxed{
\|\nabla^2\Omega\|_2^2
\ge c\int u-C\int u^2-C\sqrt P\,\|u\|_2.
}
\tag{19}
\]
The diffuse template therefore cannot be a globally slowly varying torsion field: its second-jet energy is of order \(\sqrt{kA}\), comparable to its first-jet energy in the \(s=-4\) normalization. This is an integral statement; it does not establish pointwise unit-scale oscillation everywhere.

Equation (64.11) correctly transcribes AAD (38). Pairing it with \(\nabla_{JZ}\Omega\) introduces \(\nabla^2\Omega\), while its \(\kappa/4\) term has the unfavorable negative-scalar sign. Equations (18)–(19) make the derivative-loss issue concrete. Cauchy–Schwarz alone gives a balance, not a gap.

## 4. Nijenhuis zeros: what the scaling proves, and what it does not

The Nijenhuis section lies in the complex rank-two bundle
\[
E=T^{1,0}M\otimes K^{-1},
\qquad
c_2(E)=c_2(TM,J)+2c_1(J)^2.
\]
Thus
\[
\langle c_2(E),[M]\rangle
=5\chi+6\tau=c_2(X)+2A-k.
\tag{20}
\]
A nonzero value forces a zero, as also follows from AAD Lemma 2. A signed count requires transverse isolated zeros; arbitrary Nijenhuis zero sets need not have that form. This count is generally host-scale, not one zero per exceptional class.

In a local trivialization, consider the **section model**
\[
q_\epsilon(x)=\sqrt{u_0}\,f(r/\epsilon)\frac{x}{r},
\]
where \(f(t)=t\) near zero and \(f(t)=1\) for \(t\ge1\). Its linking phase has degree one, while
\[
\begin{aligned}
\||q_\epsilon|^2-u_0\|_{L^2(B_\epsilon)}^2
 &=O(u_0^2\epsilon^4),\\
\int_{B_\epsilon}|d|q_\epsilon|^2|^2
 &=O(u_0^2\epsilon^2),\\
\int_{B_\epsilon}|\nabla q_\epsilon|^2
 &=O(u_0\epsilon^2).
\end{aligned}
\tag{21}
\]
The amplitude defect has derivative of homogeneous \(H^{-1}\) size \(O(u_0\epsilon^2)\). Multiplication by \(J\) preserves this estimate up to a dimensional constant in the weighted norm, since
\[
D_u(J\eta)\le C D_u(\eta).
\]

The degree detects the scale-invariant boundary quantity
\[
\int_{S_\epsilon^3}|d(q_\epsilon/|q_\epsilon|)|^3,
\]
not the vanishing bulk quantity in (21). By contrast, a fixed nontrivial **metric** rescaled to radius \(\epsilon\) has curvature of order \(\epsilon^{-2}\) and scale-invariant \(L^2\) curvature. These are different scaling problems.

The justified conclusion is:

> Isolated zero index and the first AAD amplitude estimate alone impose no fixed per-core cost in \(P\).

It is **not** yet justified to conclude that actual AK metrics realize arbitrary degree-one cores with vanishing curvature payment. The proposed compatible-\(J\) implant estimate in the branch work requires a realization proof satisfying \(d\Omega=0\), the prescribed exterior Nijenhuis data, and the curvature identities; Yamabe normalization is another unresolved step. Moreover, shrinking the amplitude core does not erase the phase geometry on the exterior annulus.

The sentence “four-dimensional \(L^2\) curvature is supercritical” should be removed: it is critical under metric scaling. What is subcritical for isolated zero degree is the bulk \(L^2\) **first-derivative section energy**.

Likewise, Step 64’s claimed conditional theorem that a noncollapsed bulk and lower harmonic radius automatically price the cores in \(P\) is unsupported. Such hypotheses can restrict concentration and control second jets, but do not turn Weyl/second-jet energy into tracefree-Ricci energy. A separate coercivity statement is required.

## 5. Corrected Proposition 64.H

### Exact standard Hopf model

For
\[
\Phi_0=(x_1+ix_2,\;x_3+ix_4),\qquad \rho=r^2,
\]
the normalized Bloch field is precisely (64.12):
\[
n=\frac1{r^2}
\left(2(x_1x_3+x_2x_4),\
2(x_2x_3-x_1x_4),\
x_1^2+x_2^2-x_3^2-x_4^2\right).
\]
For the unit \(S^2\) area form,
\[
|dn|^2=\frac8{r^2},
\qquad
|n^*\omega_{S^2}|^2=\frac{16}{r^4}.
\tag{22}
\]

With \(\Omega=\sqrt2\,n\) in a parallel orthonormal trivialization of \(\Lambda^+\),
\[
dn=\alpha\otimes(\phi/\sqrt2)+\beta\otimes(J\phi/\sqrt2),
\qquad
\alpha\wedge\beta=\pm n^*\omega_{S^2}.
\]
The sign depends on tangent-frame orientation and is irrelevant to the norms. Since the two-form is decomposable,
\[
\boxed{|t_J^-|^2=\frac8{r^4}.}
\tag{23}
\]
Consequently all logarithmic constants in the standard model are correct:
\[
\boxed{
\int_{\epsilon<r<R}|dn|^4=128\pi^2\log(R/\epsilon),
\qquad
\int_{\epsilon<r<R}|t_J^-|^2=16\pi^2\log(R/\epsilon).
}
\tag{24}
\]
The weighted integrals are, more precisely,
\[
\boxed{
\int_{B_R}\rho^2|dn|^2=\frac{8\pi^2}{3}R^6,
\qquad
\int_{B_R}\rho|dn|^2=4\pi^2R^4.
}
\tag{25}
\]

### General transverse \(C^2\) zero

Let \(\Phi(p)=0\), with invertible real-linear derivative
\(L:T_pM\to W_p^+\). In normal coordinates and smooth orthonormal trivializations,
\[
\Phi(x)=Lx+O(r^2),
\qquad
n(r,\theta)=f_L(\theta)+O(r),
\qquad
\nabla n=r^{-1}d_{S^3}f_L+O(1),
\]
where
\[
f_L=H\circ\widehat L,\qquad
\widehat L(\theta)=L\theta/|L\theta|.
\]
For fixed sufficiently small \(R\),
\[
\boxed{
\begin{aligned}
\int_{\epsilon<r<R}|\nabla n|^4
 &=C_4(L)\log(R/\epsilon)+O(1),\\
\int_{\epsilon<r<R}|t_J^-|^2
 &=C_t(L)\log(R/\epsilon)+O(1),
\end{aligned}}
\tag{26}
\]
with
\[
C_4(L)=\int_{S^3}|df_L|^4>0,
\qquad
C_t(L)=\frac12\int_{S^3}|f_L^*\omega_{S^2}|^2>0.
\tag{27}
\]
Here the sphere carries the round metric induced by \(g_p\). Smooth connection terms contribute only integrable errors. The coefficients are \(128\pi^2\) and \(16\pi^2\) when \(L\) is conformal; arbitrary bounded linear coordinate changes do not preserve them.

Since \(\rho\asymp r^2\), the weighted bounds remain \(O(R^6)\) and \(O(R^4)\). The linking map has Hopf invariant
\[
\operatorname{Hopf}(f_L)=\operatorname{sign}\det_{\mathbb R}L=\pm1.
\]
It therefore cannot extend continuously as a unit self-dual form over the ball while its boundary values remain fixed.

### Exact consequence for the SW field

At a transverse zero, the normalized field is neither a global smooth \(J\) nor a field with \(L^2\) frame twist. Nevertheless, Theorem N’s weighted rotation is locally finite and tends to zero with the ball radius, since its \(\mathcal W_2\) part is bounded by the full weighted integral.

Hence **Theorem N cannot directly furnish the smooth field or the unweighted critical norm required by 63.T**.

This is a conditional statement about transverse zeros, not a theorem that all SW zeros are transverse or have this exact model. Two further qualifications matter:

* A zero-free spinor does furnish a smooth orthogonal \(J\) with determinant class \(a\). Even then, weighted \(L^2\) rotation does not control the \(L^4\) rotation needed for quadratic twist.
* For a best-class spinor bundle,
  \[
  \langle c_2(W^+),[M]\rangle
  =\frac{a^2-(2\chi+3\tau)}4=0.
  \]
  If all zeros are transverse, their signed Hopf charges sum to zero. Aggregate cancelling charges can be repaired by global modifications, unlike one isolated charged ball. Neither a uniform repair cost nor a bound by Theorem N follows from this cancellation.

A punctured Gauss–Hodge comparison must therefore retain boundary/zero charges and the determinant connection, rather than discard them by normalization.

## 6. Genuine implications for the open-range gap

The verified advance is a sharper necessary-condition system:

1. Every smooth best-class \(J\) on a low-\(P\) metric carries almost all exceptional ASD flux in \(\mathsf H^-(t_J^-)\).
2. An efficient **AK** realization has the quartic torsion scale (7), not the former \(u=k/A\) scale.
3. If that torsion is diffuse, it requires period/volume slack and \(W_2/W_3\) energy of order \(\sqrt{kA}\), together with comparable second-jet energy.
4. The first AAD identity controls amplitude variation but is noncoercive at precisely that scale. The second retains orientation information but introduces the unfavorable sign and second-jet terms.
5. Nijenhuis zero topology gives no proved per-core \(P\)-tariff; SW normalization introduces a different, genuinely critical Hopf singularity.

No positive tariff, \(k^2/A\) lower bound, zero-gap sequence, or global near-minimizer decomposition follows.

The remaining scientific object is not the value of the harmonic projection—it is already pinned by (1)—but the **geometric cost of realizing that fixed harmonic flux as quadratic frame twist**, while satisfying the full differential system. A useful new estimate must couple this realization to quantities noncircularly controlled by \(P\), including any zero-charge or boundary-transgression terms. Conversely, a low-cost construction must realize the period slack, large Weyl load, second jets, and harmonic twist simultaneously in actual closed metrics. The present identities neither obstruct nor construct such a realization.