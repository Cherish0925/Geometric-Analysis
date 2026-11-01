# TTCS Independent Branch Record

```json
{
  "step_id": 64,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step64_diffuse_twist_AAD_and_SW_zeros.md",
    "Sessions/S1003A02/workspace/notes/step63_frame_twist_flux_and_AK_identity.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md",
    "Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md",
    "Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md"
  ]
}
```

## Task

Verify and strengthen the mathematics of the Step-64 note. Focus on four load-bearing points: (1) the diffuse torsion scale inferred from Theorem 63.T, including constants in equations (64.3)-(64.4); (2) the weak H^{-1}-type estimate (64.7)-(64.9) derived from the Apostolov–Armstrong–Drăghici transition identity—check whether integration by parts really removes every curvature derivative, what norms/boundary hypotheses are needed, and whether the claimed dependence on Ric'', rho_*'', W3 is valid; (3) the scaling argument that topologically required Nijenhuis zeros can shrink without a scale-invariant L2 curvature payment; and (4) Proposition 64.H for a transverse C^2 spinor zero—check the Hopf-map formulas, frame-twist density, logarithmic coefficients, and the conclusion that the normalized SW Bloch field cannot directly be used as the smooth J in Theorem 63.T. Give corrected theorem statements with exact scope where needed, and explain what these results genuinely imply for the open-range Einstein-gap problem. Use the cited AAD source and prior Step-63 theorem as grounding; do not assume an unproved global near-minimizer decomposition.

## Output

# Scientific verification memo: Step 64

## 1. Diffuse torsion scale from Theorem 63.T

Let
\[
\gamma_J^-=\rho_0^J+t_J^-,
\qquad
t_J^-=(\alpha\wedge\beta)^-,
\]
and let \(h_a^-\) be the harmonic ASD representative of \(a^-\), normalized by
\([h_a^-]=a^-\). Write \(\mathsf H^-\) for \(L^2\)-projection to harmonic ASD forms. Since
\([\gamma_J]=2\pi a\), Hodge theory gives the exact vector identity
\[
\boxed{\;
\mathsf H^-(t_J^-)=2\pi h_a^--\mathsf H^-(\rho_0^J).
\;}
\tag{1.1}
\]
Under the conventions of Step 63, the sign in (1.1) is plus in front of \(2\pi h_a^-\). In the almost-Kähler case \(t_J^-=-(a\wedge Ja)^-\), but this does not change the sign in (1.1), because \(t_J^-\) was already defined as the term appearing in \(\gamma_J^-=\rho_0^J+t_J^-\).

Moreover,
\[
\|\rho_0^J\|_2^2
=\frac12\|\operatorname{Ric}_0'\|_2^2
\le \frac P2.
\tag{1.2}
\]
Thus, with
\[
K:=|a^-|_g^2=\|h_a^-\|_2^2=k+\Pi,
\]
one obtains the exact quantitative estimate
\[
\boxed{\;
\|t_J^-\|_2
\ge
\bigl(2\pi\sqrt K-\sqrt{P/2}\bigr)_+.
\;}
\tag{1.3}
\]

A useful orthogonal decomposition is
\[
\boxed{\;
\|t_J^-\|_2^2
=
\|2\pi h_a^--\mathsf H^-(\rho_0^J)\|_2^2
+\|(1-\mathsf H^-)t_J^-\|_2^2.
\;}
\tag{1.4}
\]
Consequently, \(P=o(k)\) fixes the harmonic projection of \(t_J^-\) to leading order, but does **not** force
\[
\|t_J^-\|_2=2\pi\sqrt{k+\Pi}+o(\sqrt k).
\]
Only the lower estimate follows. Asymptotic equality additionally requires
\[
\|(1-\mathsf H^-)t_J^-\|_2=o(\sqrt k).
\tag{1.5}
\]
Thus the full-field approximation appropriate to the minimal-twist branch is
\[
t_J^-=2\pi h_a^-+o_{L^2}(\sqrt k),
\tag{1.6}
\]
not the minus-sign version in (64.2). Equation (1.6) is an efficiency assumption, whereas its harmonic-projection version follows directly from (1.1).

### Almost-Kähler specialization

For an almost-Kähler structure,
\[
\nabla\Omega=a\otimes\phi-Ja\otimes J\phi,\qquad
u=|a|^2=\frac14|\nabla\Omega|^2,
\]
and
\[
t_J^-=-(a\wedge Ja)^-.
\]
Since \(a\wedge Ja\) is decomposable and has squared norm \(u^2\),
\[
\boxed{\;
|t_J^-|^2=\frac12u^2.
\;}
\tag{1.7}
\]
Combining (1.3) and (1.7) yields the corrected exact form of (64.3):
\[
\boxed{\;
\frac12\int_M u^2\,d\mu
\ge
\bigl(2\pi\sqrt{k+\Pi}-\sqrt{P/2}\bigr)_+^2.
\;}
\tag{1.8}
\]
If \(P=o(k)\) and \(\Pi=O(k)\), this becomes
\[
\frac12\int_Mu^2
\ge4\pi^2(k+\Pi)-o(k).
\tag{1.9}
\]
Without \(\Pi=O(k)\), the corresponding remainder is \(o(k+\Pi)\), not necessarily \(o(k)\). Also, \(P=o(k)\) alone does not imply \(\Pi=o(k)\); small \(\Pi\) belongs to the minimal-flux construction branch.

For volume \(V=\operatorname{Vol}(M,g)\), define
\[
u_{\mathrm{rms}}
=\left(\frac1V\int_Mu^2\right)^{1/2}.
\]
Then (1.8) gives
\[
u_{\mathrm{rms}}
\ge
\sqrt{\frac2V}\,
\bigl(2\pi\sqrt{k+\Pi}-\sqrt{P/2}\bigr)_+.
\tag{1.10}
\]
At \(V=2\pi^2A(1+o(1))\), with \(P=o(k)\),
\[
\boxed{\;
u_{\mathrm{rms}}
\ge
2\sqrt{\frac{k+\Pi}{A}}\,(1-o(1)).
\;}
\tag{1.11}
\]

The directly controlled norm of \(\nabla\Omega\) is its normalized \(L^4\) norm:
\[
\left(\frac1V\int_M|\nabla\Omega|^4\right)^{1/4}
=
\left(\frac{16}{V}\int_Mu^2\right)^{1/4}.
\]
Hence
\[
\boxed{\;
\left(\frac1V\int_M|\nabla\Omega|^4\right)^{1/4}
\ge
2\sqrt2\left(\frac{k+\Pi}{A}\right)^{1/4}(1-o(1)).
\;}
\tag{1.12}
\]
The expression \(|\nabla\Omega|_{\rm rms}\asymp(k/A)^{1/4}\) in (64.4) is therefore accurate only if it denotes normalized \(L^4\) size, or if diffuseness converts this \(L^4\) information into a typical pointwise size. The usual \(L^2\) RMS of \(|\nabla\Omega|\) is not bounded from below by (1.8) without additional control on concentration.

Finally, this entire \(u\)-based specialization presupposes an almost-Kähler \(J\). The Wu argument in Step 63 supplies an orthogonal almost-complex structure with the desired \(c_1\), but it does not make \(\Omega\) closed. Thus the diffuse almost-Kähler template is a particular geometric realization problem, not a necessary description of every metric with small \(P\).

---

## 2. The weak AAD transport estimate

Set
\[
S=\operatorname{Ric}'',\qquad \sigma=\rho_*''.
\]
AAD Corollary 1 and \(\kappa-s=6u\) give
\[
2d^Ju
=
2\langle\delta W_3^+,\Omega\rangle
+2\delta\sigma
-\langle\sigma,\nabla_J\Omega\rangle
+\langle A^+,\Omega\rangle,
\tag{2.1}
\]
where
\[
A_Z=(d^\nabla S)_Z+\iota_{JZ}d\rho_{\rm Ric},
\qquad
d\rho_{\rm Ric}=*\bigl(J\delta S\bigr)
\tag{2.2}
\]
by AAD equation (26).

### Correct weak formulation

Let \(M\) be closed and smooth, and let \(\eta\) be a smooth one-form. Define
\[
D_u(\eta):=\|\nabla\eta\|_2+\|\sqrt u\,\eta\|_2.
\tag{2.3}
\]
Then
\[
\boxed{\;
2\left|\int_M\langle d^Ju,\eta\rangle\,d\mu\right|
\le
C\bigl(\|W_3^+\|_2+\|\sigma\|_2+\|S\|_2\bigr)D_u(\eta),
\;}
\tag{2.4}
\]
where \(C\) is dimensional and independent of \(g,J,\eta\).

The curvature derivatives in (2.1) are indeed removed:

* For the \(W_3^+\) term,
  \[
  \int\eta^Z\langle(\delta W_3^+)_Z,\Omega\rangle
  =
  \pm\int\langle W_3^+,\nabla(\eta\otimes\Omega)\rangle,
  \]
  so
  \[
  |I_{W_3}|
  \le C\|W_3^+\|_2
  \bigl(\|\nabla\eta\|_2+\||\nabla\Omega|\,\eta\|_2\bigr).
  \]
  Since \(|\nabla\Omega|=2\sqrt u\), this is controlled by \(D_u(\eta)\).

* The divergence of \(\sigma\) is treated similarly:
  \[
  \left|\int\langle\delta\sigma,\eta\rangle\right|
  \le C\|\sigma\|_2\|\nabla\eta\|_2.
  \]
  The algebraic term involving \(\nabla\Omega\) satisfies
  \[
  \left|\int\eta^Z\langle\sigma,\nabla_{JZ}\Omega\rangle\right|
  \le2\|\sigma\|_2\|\sqrt u\,\eta\|_2.
  \]

* Since \(\Omega\) is self-dual,
  \[
  \langle A_Z^+,\Omega\rangle=\langle A_Z,\Omega\rangle.
  \]
  Integrating the \(d^\nabla S\) term moves the derivative to \(\eta\) and \(\Omega\), giving
  \[
  C\|S\|_2D_u(\eta).
  \]

* For the remaining part of \(A\), equation (2.2) turns
  \[
  \eta^Z\langle\iota_{JZ}d\rho_{\rm Ric},\Omega\rangle
  \]
  into an algebraic contraction of \(\delta S\) with a one-form built from \(J,\Omega,\eta\). A second integration by parts leaves \(S\) paired with \(\nabla\eta\) and \((\nabla J)\eta\). Since \(|\nabla J|=|\nabla\Omega|=2\sqrt u\), it is again controlled by \(C\|S\|_2D_u(\eta)\).

Thus no \(\nabla\operatorname{Rm}\) norm remains in (2.4). The identity \(d\rho_{\rm Ric}=*(J\delta S)\) is essential; treating \(d\rho_{\rm Ric}\) as an independent tensor would not yield the displayed estimate.

The clean global statement uses a closed manifold. On a domain \(U\), the same estimate holds for \(\eta\in C_c^\infty(U;T^*U)\). For unrestricted \(\eta\) on \(U\), additional \(\partial U\)-integrals involving the normal fluxes of \(W_3^+\), \(\sigma\), and \(S\) remain; mere \(L^2\) control does not automatically define all of those traces.

### Weighted dual seminorm

Define
\[
\|\xi\|_{\dot{\mathcal H}^{-1}_u}
:=
\sup_{D_u(\eta)\le1}
\left|\int_M\langle\xi,\eta\rangle\,d\mu\right|.
\tag{2.5}
\]
This is the dual of the weighted homogeneous energy
\(\|\nabla\eta\|_2+\|\sqrt u\,\eta\|_2\), rather than the usual inhomogeneous \(H^{-1}\) norm. If \(u\equiv0\), it is interpreted modulo parallel one-forms; in that case \(d^Ju=0\) anyway.

Since \(\|S\|_2\le\sqrt P\), (2.4) gives
\[
\boxed{\;
\|d^Ju\|_{\dot{\mathcal H}^{-1}_u}
\le
C\bigl(\|W_3^+\|_2+\|\rho_*''\|_2+\sqrt P\bigr).
\;}
\tag{2.6}
\]

Now use the exact Step-63 identity
\[
P
=
2\|\gamma_J^-\|_2^2
+\int_Mu(5u+s)
+2\|\rho_*''\|_2^2
+4\|W_3^+\|_2^2.
\tag{2.7}
\]
Pointwise,
\[
u(5u+s)\ge-u(|s|-5u)_+.
\]
Therefore
\[
2\|\rho_*''\|_2^2+4\|W_3^+\|_2^2
\le
P+\int_Mu(|s|-5u)_+.
\tag{2.8}
\]
Combining (2.6)–(2.8) yields
\[
\boxed{\;
\|d^Ju\|_{\dot{\mathcal H}^{-1}_u}^2
\le
C\left[
P+\int_Mu(|s|-5u)_+
\right].
\;}
\tag{2.9}
\]

Equations (2.4)–(2.9) are valid as stated for smooth closed almost-Kähler four-manifolds. They control \(du\), hence only amplitude variation. They do not control the constant mode of \(u\), the harmonic projection of \(t_J^-\), or the direction of the quadratic form \(\alpha\wedge\beta\). In particular, (2.9) does not yield an estimate of the form
\[
\|\mathsf H^-(t_J^-)\|_2
\lesssim
\|W_3^+\|_2+\|\rho_*''\|_2+\sqrt P.
\]

---

## 3. Shrinking Nijenhuis zeros and energy scaling

For an almost-Kähler four-manifold, the Nijenhuis tensor can be viewed as a section of the complex rank-two bundle
\[
E=T^{1,0}M\otimes K^{-1}.
\]
Its top Chern number is
\[
\langle c_2(E),[M]\rangle
=
\langle c_2(TM,J)+2c_1(J)^2,[M]\rangle
=
5\chi+6\tau.
\tag{3.1}
\]
On \(M=X\#k\overline{\mathbb{CP}}^{\,2}\),
\[
5\chi(M)+6\tau(M)=c_2(X)+2A-k.
\tag{3.2}
\]
Whenever this number is nonzero, \(N\) must vanish somewhere. This is a qualitative topological statement.

The relevant scaling can be seen in a local trivialization. Let
\[
q_\epsilon(x)
=
\sqrt{u_0}\,f(r/\epsilon)\,\frac{x}{r},
\]
where \(f(t)=t\) near \(0\) and \(f(t)=1\) for \(t\ge1\). Then \(q_\epsilon\) is smooth at the origin, its normalized phase on \(S_\epsilon^3\) has degree one, and
\[
u_\epsilon:=|q_\epsilon|^2
=
u_0 f(r/\epsilon)^2.
\]
Direct scaling gives
\[
\|u_\epsilon-u_0\|_{L^2(B_\epsilon)}^2
=O(u_0^2\epsilon^4),
\tag{3.3}
\]
\[
\int_{B_\epsilon}|du_\epsilon|^2
=O(u_0^2\epsilon^2),
\tag{3.4}
\]
and
\[
\int_{B_\epsilon}|\nabla q_\epsilon|^2
=O(u_0\epsilon^2).
\tag{3.5}
\]
Moreover,
\[
\|d(u_\epsilon-u_0)\|_{\dot H^{-1}}
\le C\|u_\epsilon-u_0\|_2
=O(u_0\epsilon^2).
\tag{3.6}
\]
The corresponding weighted estimate for \(d^Ju\) has the same scaling when \(|\nabla J|\sim\sqrt u\).

The scale-invariant topological quantity lives instead at exponent three on the linking sphere:
\[
\int_{S_\epsilon^3}
\left|d\left(\frac{q_\epsilon}{|q_\epsilon|}\right)\right|^3
=
\int_{S^3}|d\Theta|^3,
\tag{3.7}
\]
where \(\Theta:S^3\to S^3\) is the phase map. Its bulk \(L^2\) first-derivative energy scales as \(\epsilon^2\).

Therefore the zero index alone does not provide a fixed contribution to the weighted \(H^{-1}\) norm in (2.5), to \(\int|\nabla N|^2\), or to the quadratic twist inside the shrinking core. This does not construct an almost-Kähler metric realizing the model: \(N=\nabla J\) is constrained by closure of \(\Omega\), the Ricci identities, and the two AAD Bianchi equations. It establishes the narrower but important fact that the Chern number and isolated zero degree, by themselves, do not assign a fixed \(L^2\)-curvature cost to each core. Any such cost must come from the geometric PDE or from a lower geometric scale, not merely from the zero index.

---

## 4. Proposition 64.H: exact model and general transverse zero

### 4.1 Exact standard linear model

Let
\[
\Phi_0(x)
=
(z_1,z_2)
=
(x_1+ix_2,\;x_3+ix_4),
\qquad
\rho=|\Phi_0|^2=r^2.
\]
Its unit-spinor Bloch field is the radial Hopf map
\[
n(x)=\frac1{r^2}
\left(
2(x_1x_3+x_2x_4),\,
2(x_2x_3-x_1x_4),\,
x_1^2+x_2^2-x_3^2-x_4^2
\right).
\tag{4.1}
\]
The Hopf map \(S^3\to S^2\) has horizontal singular values \(2,2\) and radial and fiber singular values zero. Hence
\[
\boxed{\;
|\nabla n|^2=\frac8{r^2}.
\;}
\tag{4.2}
\]
If \(\omega_{S^2}\) is the area form of the unit two-sphere, then
\[
\boxed{\;
|n^*\omega_{S^2}|^2=\frac{16}{r^4}.
\;}
\tag{4.3}
\]

Set \(\Omega=\sqrt2\,n\), choose a local oriented orthonormal frame
\((\phi/\sqrt2,J\phi/\sqrt2)\) of \(\Omega^\perp\), and write
\[
\nabla\Omega=\alpha\otimes\phi+\beta\otimes J\phi.
\]
Then
\[
\nabla n=\alpha\otimes\frac{\phi}{\sqrt2}
+\beta\otimes\frac{J\phi}{\sqrt2},
\qquad
\alpha\wedge\beta=n^*\omega_{S^2}.
\tag{4.4}
\]
Because \(\alpha\wedge\beta\) is decomposable,
\[
|(\alpha\wedge\beta)^-|^2
=
\frac12|\alpha\wedge\beta|^2.
\]
Thus
\[
\boxed{\;
|(\alpha\wedge\beta)^-|^2=\frac8{r^4}.
\;}
\tag{4.5}
\]

Using \(|S^3|=2\pi^2\),
\[
\boxed{\;
\int_{\epsilon<r<R}|\nabla n|^4\,d\mu
=
128\pi^2\log\frac R\epsilon,
\;}
\tag{4.6}
\]
and
\[
\boxed{\;
\int_{\epsilon<r<R}|(\alpha\wedge\beta)^-|^2\,d\mu
=
16\pi^2\log\frac R\epsilon.
\;}
\tag{4.7}
\]
The weighted integrals are finite and have exact values
\[
\boxed{\;
\int_{B_R}\rho^2|\nabla n|^2\,d\mu
=
\frac{8\pi^2}{3}R^6,
\qquad
\int_{B_R}\rho|\nabla n|^2\,d\mu
=
4\pi^2R^4.
\;}
\tag{4.8}
\]

### 4.2 General transverse \(C^2\) zero

Suppose now
\[
\Phi(x)=Lx+O(r^2),
\]
where \(L:\mathbb R^4\to\mathbb C^2\) is a real-linear isomorphism. In smooth orthonormal trivializations,
\[
n(r,\theta)=f_L(\theta)+O(r),
\qquad
f_L=H\circ\widehat L:S^3\to S^2,
\tag{4.9}
\]
where \(H\) is the Hopf map and
\[
\widehat L(\theta)=\frac{L\theta}{|L\theta|}.
\]
The degree of \(\widehat L\) is \(\operatorname{sign}\det_{\mathbb R}L\), so \(f_L\) has Hopf invariant \(\pm1\). In particular, \(f_L^*\omega_{S^2}\not\equiv0\).

As \(\epsilon\downarrow0\), for fixed sufficiently small \(R\),
\[
\int_{\epsilon<r<R}|\nabla n|^4
=
C_4(L)\log\frac R\epsilon+O(1),
\qquad
C_4(L)=\int_{S^3}|df_L|^4>0,
\tag{4.10}
\]
and
\[
\int_{\epsilon<r<R}|(\alpha\wedge\beta)^-|^2
=
C_t(L)\log\frac R\epsilon+O(1),
\tag{4.11}
\]
where
\[
C_t(L)
=
\frac12\int_{S^3}|f_L^*\omega_{S^2}|^2>0.
\tag{4.12}
\]
Also \(\rho\asymp r^2\), so
\[
\int_{B_R}\rho^2|\nabla n|^2=O(R^6),
\qquad
\int_{B_R}\rho|\nabla n|^2=O(R^4).
\tag{4.13}
\]

The coefficients \(128\pi^2\) and \(16\pi^2\) are exact for the standard conformal linear model \(L=\mathrm{Id}\). An arbitrary bounded linear normalization changes the metric and generally changes the logarithmic coefficients. Thus Proposition 64.H should separate the exact standard model from the general transverse-zero asymptotics (4.10)–(4.12).

### 4.3 Extension obstruction

For every sufficiently small \(r\), the map
\[
n|_{S_r^3}:S^3\to S^2
\]
has Hopf invariant \(\pm1\). If it extended continuously as a unit self-dual form over \(B_r^4\), its restriction to \(S_r^3\) would be null-homotopic, which is impossible. Therefore the normalized Bloch field cannot be replaced inside an isolated small ball while kept unchanged outside.

This has three precise consequences:

1. \(n\) is not a global smooth orthogonal almost-complex structure.
2. Its frame twist is not in \(L^2\) near a transverse zero; it diverges logarithmically.
3. The SW quantity
   \[
   \int\rho^2|\nabla n|_{\mathcal W_2}^2
   \]
   can tend to zero near the same zero, since it is bounded above by the full weighted integral in (4.8) or (4.13).

Hence Theorem N cannot directly estimate the twist appearing in Theorem 63.T. A smooth \(J\) with the same \(c_1\) may exist by Wu theory, but its construction cannot agree with the normalized Bloch field off disjoint tiny balls around transverse zeros. Any comparison must retain the zero indices and determinant connection, or account for a global modification joining the local Hopf charges.

---

## 5. Consequences for the open-range Einstein-gap problem

The verified content is the following.

* For a **smooth almost-Kähler** representative in the best class, small \(P\) forces the harmonic projection of the ASD frame twist to carry almost all of the flux \(2\pi a^-\). The minimal normalized torsion scale is
  \[
  u_{\mathrm{rms}}\gtrsim2\sqrt{\frac{k+\Pi}{A}},
  \qquad
  \|\nabla\Omega\|_{L^4,\mathrm{av}}
  \gtrsim2\sqrt2\left(\frac{k+\Pi}{A}\right)^{1/4}.
  \]
  Equality at this scale additionally requires little nonharmonic twist.

* The first AAD transition identity gives a genuine derivative-free weak estimate, but only for \(d^Ju\). It does not price the mean diffuse mode or the harmonic projection in (1.1).

* The nonzero top Chern number of the Nijenhuis bundle forces zeros, but isolated zero cores can shrink with \(H^{-1}\) amplitude cost and bulk first-derivative energy tending to zero. Topology alone therefore supplies no fixed per-core contribution to \(P\).

* A transverse SW spinor zero produces a Hopf singularity whose unweighted frame twist has logarithmic divergence, while the amplitude-weighted SW rotation tends to zero. Thus normalized SW spinors do not furnish the smooth \(J\) required by Theorem 63.T.

These results do not yield a positive per-class tariff or a \(k^2/A\) estimate. They also do not produce a closed low-\(P\) metric. The unresolved mathematical object is a relation between the large harmonic projection
\[
\mathsf H^-(t_J^-)\simeq2\pi h_a^-
\]
and curvature quantities controlled by \(P\), with the zero charges and any geometric degeneration explicitly retained. Without such a relation, the diffuse harmonic-twist configuration remains compatible with the established integral identities, though not yet realized by a metric satisfying the full Gauss–Ricci–Bianchi system.