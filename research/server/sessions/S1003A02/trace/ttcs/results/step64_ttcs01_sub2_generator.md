# TTCS Independent Branch Record

```json
{
  "step_id": 64,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step64_diffuse_twist_AAD_and_SW_zeros.md",
    "Sessions/S1003A02/workspace/notes/step63_frame_twist_flux_and_AK_identity.md",
    "Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md",
    "Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md"
  ]
}
```

## Task

Starting from the verified frame-twist theorem and the Step-64 diffuse-twist template, seek a genuinely stronger route toward either a global lower bound or a closed cheap construction. The hard quantity is the harmonic ASD projection of t_J^-=(alpha wedge beta)^- for a smooth best-sign almost complex structure, while AAD controls only derivatives/amplitude of torsion and normalized SW spinors are singular at zeros. Develop precise mathematical possibilities: an identity or inequality coupling H^-(t_J^-) to the second AAD Bianchi equation; a relative/renormalized spinor formula that retains zero/Hopf charges without divergent normalization; or a construction scheme realizing a diffuse nearly harmonic twist with shrinking zero cores and small Ricci defect. Distinguish consequences that follow now from conjectural entrances. Aim for testable formulas or an explicit model, not general suggestions.

## Output

The verified frame-twist theorem puts the exceptional ASD flux into a very sharp algebraic form. The remaining mathematical substance is not the size of the flux; it is the mechanism by which a smooth almost-complex frame can carry that flux while the Ricci defect stays small, and the way zero cores or transition interfaces enter that mechanism. Three routes appear especially productive.

---

## 0. Exact anchor: the harmonic twist is topological flux minus primitive Ricci form

For an orthogonal almost-complex structure \(J\) with fundamental form \(\Omega\), choose a local gauge \(\phi\in \Omega^\perp\), \(|\phi|^2=2\), and write

\[
\nabla\Omega=\alpha\otimes\phi+\beta\otimes J\phi,\qquad
\nabla\phi=-\alpha\otimes\Omega+b\otimes J\phi .
\]

The canonical Chern form is

\[
\gamma_J=-db=R(\Omega)+\alpha\wedge\beta,\qquad [\gamma_J]=2\pi c_1(J).
\]

Let

\[
t_J^-=(\alpha\wedge\beta)^- .
\]

Since \(R(\Omega)^-= \rho_0^J\), the ASD harmonic projection gives, up to the sign convention used for \(t_J^-\),

\[
\boxed{\;
\mathsf H^-(t_J^-)=2\pi h_{c_1(J)}^- - \rho_0^J .
\;}
\tag{0.1}
\]

Here \(h_{c_1(J)}^-\) is the \(g\)-harmonic ASD representative of \(c_1(J)^-\). In the almost-Kähler convention where \(t_J^-=-(a\wedge Ja)^-\), the same relation reads

\[
\mathsf H^-(t_J^-)=2\pi h_{c_1(J)}^- - \rho_0^J .
\]

Consequences already available:

1. Since \(|\rho_0^J|^2\le \frac12|\operatorname{Ric}_0'|^2\le \frac12P\), if \(P=o(k)\) and \(c_1(J)=a_\varepsilon\) is a best-sign class, then

   \[
   \|\mathsf H^-(t_J^-)\|_2
   =
   2\pi\sqrt{k+\Pi}+o(\sqrt{k}).
   \tag{0.2}
   \]

2. The problem is therefore not to force the flux to appear; the flux must appear. The open question is whether a smooth \(J\) can have a nearly harmonic twist of size \(2\pi\sqrt{k+\Pi}\) while the exact part of \(t_J^-\), the zero cores of the torsion field, and the curvature components \(W_3^+,\rho_*'',\operatorname{Ric}''\) remain cheap.

3. The AAD first transport identity controls only the nonconstant amplitude of the torsion:

   \[
   \|d^J u\|_{\mathcal H_u^{-1}}
   \le
   C\bigl(\|W_3^+\|_2+\|\rho_*''\|_2+\sqrt P\bigr),
   \tag{0.3}
   \]

   with \(u=|\nabla\Omega|^2/4\). It annihilates the mean diffuse mode and says nothing about the harmonic orientation of \(t_J^-\). The second AAD Bianchi identity is the only local equation that sees the phase/orientation of the moving frame.

---

## 1. Orientation contraction of the second AAD identity

For an almost-Kähler four-manifold, write the second AAD identity in the form

\[
\begin{aligned}
0={}&(du\wedge Z^\flat)''
+\frac{\kappa}{4}\nabla_{JZ}\Omega
-\nabla_{\rho_0(Z)}\Omega
+2(\delta W_3^+)_Z''  \\
&+\nabla_{\rho_*''(Z)}\Omega
+(\nabla_{JZ}\rho_*'')''
+(A_Z^+)'',
\end{aligned}
\tag{1.1}
\]

where

\[
A_Z=(d^\nabla\operatorname{Ric}'')_Z+\iota_{JZ}d\rho,
\qquad
d\rho=*(J\delta\operatorname{Ric}'').
\]

A concrete way to extract orientation information is to contract (1.1) with \(\nabla_{JZ}\Omega\) and sum over an orthonormal frame. Define

\[
\mathcal C_J
=
\sum_i\int
\left\langle
\text{RHS of (1.1) with }Z=e_i,\,
\nabla_{Je_i}\Omega
\right\rangle .
\]

Since the RHS is zero, \(\mathcal C_J=0\). Expanding gives

\[
\mathcal C_J
=
\int \kappa u
-
\sum_i\int
\left\langle
\nabla_{\rho_0(e_i)}\Omega,\,
\nabla_{Je_i}\Omega
\right\rangle
+
\mathcal R_{\text{trans}},
\tag{1.2}
\]

where \(\mathcal R_{\text{trans}}\) contains the \(du\), \(W_3^+\), \(\rho_*''\), and \(A^+\) contributions.

In the AAD gauge

\[
\nabla\Omega=a\otimes\phi-Ja\otimes J\phi,
\qquad u=|a|^2,
\]

one has the algebraic identity, to be verified in a symbolic frame,

\[
\sum_i
\left\langle
\nabla_{\rho_0(e_i)}\Omega,\,
\nabla_{Je_i}\Omega
\right\rangle
=
-2\left\langle \rho_0,\,(a\wedge Ja)^-\right\rangle .
\tag{1.3}
\]

With \(t_J^-=-(a\wedge Ja)^-\), this becomes

\[
\sum_i
\left\langle
\nabla_{\rho_0(e_i)}\Omega,\,
\nabla_{Je_i}\Omega
\right\rangle
=
2\langle\rho_0,t_J^-\rangle .
\tag{1.4}
\]

Thus (1.2) yields the integrated orientation relation

\[
\boxed{\;
\int \kappa u
-
2\int\langle\rho_0,t_J^-\rangle
=
-\mathcal R_{\text{trans}} .
\;}
\tag{1.5}
\]

Using \(\kappa=s+6u\) and \(s=-4\),

\[
\int (6u^2-4u)
-
2\int\langle\rho_0,t_J^-\rangle
=
-\mathcal R_{\text{trans}} .
\tag{1.6}
\]

Now decompose

\[
t_J^-=\mathsf H^-(t_J^-)+t_{\rm ex}^-
\]

and use (0.1):

\[
\mathsf H^-(t_J^-)=2\pi h^- -\rho_0 .
\]

Then

\[
2\int\langle\rho_0,t_J^-\rangle
=
4\pi\int\langle\rho_0,h^-\rangle
-
2\|\rho_0\|_2^2
+
2\int\langle\rho_0,t_{\rm ex}^-\rangle .
\tag{1.7}
\]

Therefore (1.6) becomes

\[
\boxed{\;
\int(6u^2-4u)
-
4\pi\int\langle\rho_0,h^-\rangle
+
2\|\rho_0\|_2^2
-
2\int\langle\rho_0,t_{\rm ex}^-\rangle
=
-\mathcal R_{\text{trans}} .
\;}
\tag{1.8}
\]

This is a refined companion to the integral AK identity

\[
P=
2\|\gamma_J^-\|_2^2
+
\int u(5u+s)
+
2\|\rho_*''\|_2^2
+
4\|W_3^+\|_2^2 .
\tag{1.9}
\]

The ordinary identity sees the moments of \(u\) and the total \(\gamma_J^-\). The contracted second Bianchi identity sees the alignment of \(\rho_0\) with the topological harmonic flux and the exact part of the twist.

### What follows now

If a near-minimizing sequence has

\[
\mathcal R_{\text{trans}}=o(k),
\qquad
\int\langle\rho_0,t_{\rm ex}^-\rangle=o(k),
\tag{1.10}
\]

then the two moment equations (1.8) and (1.9) must be satisfied simultaneously. The formal two-phase density with \(u=2/3\) on twist-carrying regions and \(u=0\) elsewhere is algebraically compatible with very small \(P\), but only if the transition contribution hidden in \(\mathcal R_{\text{trans}}\) is also small. Thus the decisive quantity is not merely the volume fraction of the \(u=2/3\) phase; it is the transition residual.

### Conjectural entrance: orientation coercivity

A strong route would be an estimate of the form

\[
\boxed{\;
\|\mathsf H^-(t_J^-)\|_2^2
\le
C\,A^{1/2}
\bigl(
\sqrt P+\|W_3^+\|_2+\|\rho_*''\|_2
\bigr)
+
\int u(|s|-5u)_+
+
\mathfrak C_{\rm core} .
\;}
\tag{1.11}
\]

Here \(\mathfrak C_{\rm core}\) is a transgression or zero-core contribution coming from the set where the torsion amplitude vanishes or the frame phase is singular. If a noncollapse theorem absorbs \(\mathfrak C_{\rm core}\) into \(P\), then with \(\|\mathsf H^-(t_J^-)\|_2^2\sim 4\pi^2 k\) one obtains a quadratic scale

\[
P\gtrsim \frac{k^2}{A}.
\tag{1.12}
\]

If instead one can make \(\mathfrak C_{\rm core}\) large while \(P=o(k)\), the construction route is open.

Equation (1.11) does not follow from (0.3). It requires using (1.1) as an elliptic phase equation for the moving frame, not merely as a transport equation for \(u\). The missing analytic substance is control of the phase operator appearing in (1.8).

A testable local version is:

\[
\left|
\int(6u^2-4u)
-
4\pi\int\langle\rho_0,h^-\rangle
+
2\|\rho_0\|_2^2
\right|
\le
C\sqrt A\,
\bigl(\sqrt P+\|W_3^+\|_2+\|\rho_*''\|_2\bigr)
+
\mathfrak C_{\rm core}.
\tag{1.13}
\]

This can be checked on explicit almost-Kähler local models, especially the AAD third-Gray family and cohomogeneity-one collars.

---

## 2. A renormalized spinor ledger retaining Hopf zero charges

The normalized Seiberg–Witten Bloch field

\[
n=\frac{q(\Phi)}{|q(\Phi)|}
\]

is singular at spinor zeros. The transverse-zero model shows that the unweighted frame twist has a logarithmic divergence:

\[
\int_{\epsilon<r<R}|(\alpha\wedge\beta)^-|^2
=
16\pi^2\log(R/\epsilon),
\tag{2.1}
\]

whereas the weighted quantity controlled by Theorem N is finite:

\[
\int_{B_R}\rho^2|\nabla n|^2=O(R^4),
\qquad
\int_{B_R}\rho^2|\nabla n|^2_{\mathcal W_2}=O(R^4).
\tag{2.2}
\]

Thus any canonical-field theorem based directly on \(q(\Phi)/|q(\Phi)|\) must either retain zero/Hopf data or replace the normalized field by a regularized supplier.

### 2.1. Regularized Bloch field

Let

\[
\psi=2\sqrt2\,\sigma(\Phi),
\qquad
\rho=|\psi|,
\]

and let \(\Omega_*\) be a smooth reference self-dual form of length \(\sqrt2\). Define a regularized direction by

\[
\Omega_\delta
=
\sqrt2\,
\frac{\psi+\delta\Omega_*}{|\psi+\delta\Omega_*|},
\qquad \delta>0,
\tag{2.3}
\]

wherever the denominator is nonzero. If antipodal intersections occur, they should be treated as defect locations; alternatively one uses several reference forms and a partition.

The associated pullback curvature of the \(S^2\)-frame is

\[
F_\delta=\Omega_\delta^*\omega_{S^2}.
\]

For the frame twist of the corresponding almost-complex structure,

\[
|t_{J_\delta}|^2
=
\frac12|F_\delta|^2
+
\text{Lee/amplitude terms}.
\tag{2.4}
\]

The important point is that \(F_\delta\) can be written without dividing by \(\rho\). Let

\[
V_\delta=\psi+\delta\Omega_* .
\]

Then, schematically,

\[
F_\delta
=
\frac{1}{|V_\delta|^3}
\,V_\delta\cdot(dV_\delta\wedge dV_\delta)
+
\text{reference-curvature terms}.
\tag{2.5}
\]

Near a transverse zero of \(\psi\), with \(\psi(x)\sim q(x)\sim |x|^2\) and Bloch map the radial Hopf map, (2.5) reproduces the logarithmic coefficient \(16\pi^2\) as \(\delta\to0\), but for fixed \(\delta\) the expression is smooth.

A Chern–Simons current gives the Hopf ledger. Locally choose a lift \(U_\delta:S^3\to S^3\) of \(\Omega_\delta\) and set

\[
A_\delta=\operatorname{Im}\langle U_\delta,dU_\delta\rangle,
\qquad
F_\delta=dA_\delta .
\]

Then

\[
H_\delta=A_\delta\wedge F_\delta
\tag{2.6}
\]

is the Hopf current. For a transverse zero \(z\) of \(\psi\),

\[
\lim_{\delta\to0}
\lim_{r\to0}
\int_{S^3_r(z)} H_\delta
=
16\pi^2\,\operatorname{ind}_z(q(\Phi)),
\tag{2.7}
\]

with the convention in which the radial Hopf model has unit index. The renormalized energy ledger is

\[
\mathcal E_{\rm Hopf}(\psi,\Omega_*)
=
\lim_{\delta\to0}
\left[
\int |F_\delta|^2
-
16\pi^2\sum_z |q_z|\log(1/\delta)
\right],
\tag{2.8}
\]

when the logarithmic parts are not canceled by other zeros or by the reference field. If Hopf charges are paired or canceled, the divergent terms are replaced by finite interaction energies.

This gives a precise replacement for the singular normalization \(q(\Phi)/|q(\Phi)|\): the zero/Hopf charges are retained in the current \(H_\delta\), while the field itself remains finite.

### 2.2. Density-matrix supplier

A more robust supplier avoids choosing a single reference form. Define a positive self-dual tensor

\[
S_\delta
=
\delta^2\,\Omega_*\otimes\Omega_*
+
\psi\otimes\psi .
\tag{2.9}
\]

Where the largest eigenvalue \(\lambda_1\) is simple, let \(e_1\) be the corresponding unit eigenvector and set

\[
\Omega_\delta=\sqrt2\,e_1 .
\tag{2.10}
\]

The eigenframe equation is

\[
\nabla e_1
=
\sum_{m\ge2}
\frac{\langle e_m,(\nabla S_\delta)e_1\rangle}{\lambda_1-\lambda_m}
\,e_m .
\tag{2.11}
\]

Hence

\[
|\nabla\Omega_\delta|^2
\le
2\,\frac{|\nabla S_\delta|^2}{\Delta_\delta^2},
\qquad
\Delta_\delta=\lambda_1-\lambda_2 .
\tag{2.12}
\]

Since

\[
\nabla S_\delta
=
\psi\otimes\nabla\psi+\nabla\psi\otimes\psi,
\tag{2.13}
\]

the right-hand side involves only \(\rho\nabla\psi\), not \(\nabla(\psi/\rho)\). The singular Bloch zeros are replaced by eigenvalue-crossing loci where \(\Delta_\delta=0\). Those crossing loci carry the same Hopf/topological information.

This gives a clean conditional theorem shape:

- If one can prove a spectral separation

  \[
  \Delta_\delta\ge c>0
  \tag{2.14}
  \]

  for the best-sign spinor family after adding a suitable reference term, then the unweighted twist of the canonical frame is controlled by the weighted Seiberg–Witten quantities.

- If \(\Delta_\delta\) must vanish, the zero/Hopf charges are concentrated on the crossing set, and the price is governed by the same Hopf current ledger (2.6)–(2.8).

A multi-sign version is also natural. For the sign family \(\{\Phi_\epsilon\}\), define

\[
S_{\delta,\mathbb E}
=
\delta^2\Omega_*\otimes\Omega_*
+
\mathbb E_\epsilon\bigl[\psi_\epsilon\otimes\psi_\epsilon\bigr].
\tag{2.15}
\]

The Walsh energy already measures variance among the \(\psi_\epsilon\). The eigenvector supplier would convert that variance into a smooth frame, while zero singularities are absorbed into eigenvalue crossings. The missing theorem is a quantitative relation between the Walsh energy, the eigenvalue gap \(\Delta_\delta\), and the harmonic projection of the resulting frame twist.

### 2.3. What follows now, and what is an entrance

Available now:

\[
\text{weighted rotation control}
\not\Rightarrow
\text{unweighted twist control}
\]

without zero/Hopf terms. Proposition 64.H gives the exact local coefficient.

Conjectural but precise entrances:

1. A gap theorem for \(S_{\delta,\mathbb E}\):

   \[
   \Delta_\delta\ge c(P,\mathcal W,\text{zero data}).
   \tag{2.16}
   \]

2. A Hopf-ledger lower estimate:

   \[
   \mathcal E_{\rm Hopf}(\psi,\Omega_*)
   \ge
   c\sum_z |q_z|
   \tag{2.17}
   \]

   unless the charges are arranged into neutral dipoles whose interaction energy is small.

3. A construction using neutral Hopf dipoles: pairs of opposite zero indices separated at scale \(\ell\) can cancel the logarithmic divergence while leaving a diffuse large-scale harmonic twist. If the dipole interaction energy can be made \(o(k)\), this supplies a cheap canonical field.

---

## 3. Construction scheme: diffuse nearly harmonic twist with shrinking Hopf cores

The Step-64 template can be made more explicit. The goal is a sequence \((g_j,J_j)\) with scalar \(-4\), \(P(g_j)=o(k)\), and

\[
t_{J_j}^-=-2\pi h_{a_j}^-+o_{L^2}(\sqrt{k}).
\tag{3.1}
\]

Let \(V\simeq 2\pi^2A\). The required diffuse torsion amplitude is

\[
\int u_j^2=8\pi^2(k+\Pi_j)+o(k),
\qquad
u_{\rm rms}\sim 2\sqrt{\frac{k}{A}}.
\tag{3.2}
\]

### 3.1. Diffuse twist field

Let \(h^-\) be the harmonic ASD representative of the best-sign exceptional flux, normalized by

\[
\|h^-\|_2^2=k+\Pi .
\]

Choose a cutoff \(\chi\) that is \(1\) away from small balls \(B_\ell\) and \(0\) inside them. Set

\[
t_{\rm diff}=-2\pi \chi\,h^-,
\tag{3.3}
\]

and choose a torsion amplitude \(u_{\rm diff}\) satisfying

\[
\frac12\int u_{\rm diff}^2
=
4\pi^2(k+\Pi)+o(k),
\qquad
u_{\rm diff}\approx 2\sqrt{\frac{k}{A}}
\quad\text{where }\chi=1.
\tag{3.4}
\]

One then seeks a smooth one-form-valued object \(a_{\rm diff}\) in the \(\Omega^\perp\) frame bundle such that

\[
|a_{\rm diff}|^2=u_{\rm diff},
\qquad
(a_{\rm diff}\wedge J a_{\rm diff})^- = t_{\rm diff}
\tag{3.5}
\]

away from the cores. Near each core, \(a_{\rm diff}\) should vanish with a Hopf-type leading term, so that the phase singularity is carried by the zero of the torsion field rather than by a singular unit direction.

In a radial core model, let the torsion amplitude behave as

\[
u(r)=u_0 f(r/\epsilon)^2,
\qquad
f(0)=0,\quad f(1)=1.
\tag{3.6}
\]

Then

\[
\int_{B_\epsilon}|u|^2=O(u_0^2\epsilon^4),
\qquad
\int_{B_\epsilon}|du|^2=O(u_0^2\epsilon^2).
\tag{3.7}
\]

Thus the core contribution to the \(L^2\) twist and to the amplitude derivative can be made small. The Hopf index is carried by the angular leading term of \(a_{\rm diff}\), but because the amplitude vanishes, the unweighted twist does not inherit the logarithmic divergence of the normalized Bloch field.

This is exactly the escape mechanism identified in Step 64, now expressed as a construction ansatz.

### 3.2. AAD compatibility equations

Given \(u_{\rm diff}\) and the desired phase of \(a_{\rm diff}\), the first AAD identity requires

\[
d^J u_{\rm diff}
=
2\langle\delta W_3^+,\Omega\rangle
+
2\delta\rho_*''
-
\langle\rho_*'',\nabla_J\Omega\rangle
+
\langle A^+,\Omega\rangle .
\tag{3.8}
\]

Because \(u_{\rm diff}\) is nearly constant, the left side is small in the natural \(\mathcal H_u^{-1}\) scale. One may therefore try to choose \(W_3^+\) and \(\rho_*''\) so that

\[
\|W_3^+\|_2+\|\rho_*''\|_2
=
o(\sqrt{k}).
\tag{3.9}
\]

The second AAD identity is the phase equation. Schematically,

\[
\frac{\kappa}{4}\nabla_{JZ}\Omega
-
\nabla_{\rho_0(Z)}\Omega
+
\text{derivative terms}
=
0.
\tag{3.10}
\]

Linearizing at a Kähler host with scalar \(-4\), the zeroth-order term has coefficient \(s/4=-1\). This is the same sign structure that permits strictly almost-Kähler \(s<0\) Einstein solutions. The relevant linear operator is the \(s<0\) Goldberg phase operator. Two opposite outcomes are possible:

- If this operator has a uniform right inverse on the relevant tower of metrics, then the phase residual can be absorbed with

  \[
  \|\rho_*''\|_2+\|\operatorname{Ric}''\|_2=o(\sqrt{k}),
  \]

  and the construction yields \(P=o(k)\).

- If its adjoint has a uniform coercive direction, the same ansatz produces a lower estimate for \(P\), potentially of per-class or \(k^2/A\) type.

Thus the decisive object is not the algebraic possibility of a diffuse twist; it is the invertibility or coercivity of the phase operator in (3.10).

### 3.3. Explicit local models to test

There are three exact or semi-explicit model families that can test the ansatz.

#### 3.3.1. Radial Hopf core with vanishing amplitude

Take a local frame in which the torsion one-form has Hopf angular dependence and radial amplitude \(f(r/\epsilon)\). Compute:

\[
\int |t|^2,\qquad
\int |du|^2,\qquad
\int |W_3^+|^2,
\]

and check the closedness condition \(d\Omega=0\) to leading order. The desired scaling is

\[
\int_{B_\epsilon}|t|^2=O(u_0^2\epsilon^4),
\qquad
\int_{B_\epsilon}|W_3^+|^2=o(u_0^2).
\tag{3.11}
\]

If such a core can be made smooth and the residual in (3.10) can be pushed into higher order, it supplies the basic zero cell for the diffuse construction.

#### 3.3.2. AAD third-Gray local family

The AAD classification gives explicit strictly almost-Kähler metrics satisfying the third Gray condition:

\[
g=g_\Sigma+w\,dz^{\otimes2}
+
\frac1w(dt+v\,dz)^{\otimes2},
\qquad
h=w+iv\ \text{holomorphic}.
\tag{3.12}
\]

Here the torsion amplitude is controlled by \(dh\). Critical points of \(h\) give zeros of the torsion amplitude with phase winding. Since the metrics satisfy exact Levi-Civita equations, one can compute directly:

\[
u,\qquad
d^J u,\qquad
W_3^+,\qquad
\gamma_J^-,
\qquad
P.
\]

This family is a strong testing ground for the claim that Hopf zeros can be carried by shrinking amplitude cores without large unweighted twist cost. The needed computation is the asymptotic energy near a critical point of \(h\), especially whether the phase winding contributes only \(O(u_0^2\epsilon^4)\) to \(\int|t|^2\).

#### 3.3.3. Product Einstein model

On \(\Sigma\times\Sigma'\) with equal constant curvature \(-1\) surface factors, the product metric is Einstein with \(P=0\). There exist orthogonal almost-complex structures for which \(c_1(J)^-\ne0\). For such \(J\), Theorem 63.T forces the entire ASD Chern flux to be carried by \(t_J^-\), with no Ricci defect.

This exact example shows that arbitrary-\(J\) coercivity cannot hold. It also supplies a target interior geometry for a cheap cap: one wants a region where \(R(\Omega)^-\approx0\) and the twist is nearly harmonic, then a transition to the host geometry.

---

## 4. Cap/transgression formulation of the lower-bound route

The localized Chern–Weil cap identity gives a clean ledger for exceptional regions. Let \(U\) be a compact exceptional region diffeomorphic to a connected sum of \(m\) opposite-sign projective pieces with a ball removed. Let \(\Sigma=\partial U\) be the interface three-manifold. Define

\[
Q(U)=\int_U\left(4|W^+|^2+\frac{s^2}{12}\right),
\tag{4.1}
\]

and let \(\mathfrak b(\Sigma)\) be the APS/transgression functional entering the localized Gauss–Bonnet/signature balance. Then

\[
\boxed{\;
P(U)
=
Q(U)+8\pi^2(m-2)+2\mathfrak b(\Sigma).
\;}
\tag{4.2}
\]

If \(U\) replaces a ball in a reference scalar \(-4\) metric with interface data matched up to an error \(\delta\), then

\[
P_g(U)
\ge
8\pi^2m-Q_h(B)-2\delta .
\tag{4.3}
\]

For a Kähler–Einstein reference with \(s=-4\), \(Q_h(B)\) is proportional to the replaced host volume.

The decisive estimate is a transgression-coercivity inequality of the form

\[
\boxed{\;
\bigl(8\pi^2-\mathfrak b(\Sigma)\bigr)_+
\le
q\,P(\text{collar})
+
\varepsilon_{\rm collapse}.
\;}
\tag{4.4}
\]

Here \(\varepsilon_{\rm collapse}\) measures the possibility of a long collapsed cusp collar in which the transgression term approaches \(8\pi^2\) while the bulk curvature energy tends to zero. If (4.4) holds with \(\varepsilon_{\rm collapse}\) controlled by the area of the exceptional sphere or by a harmonic-radius lower estimate, then summing over \(k\) exceptional caps gives a positive per-class contribution or at least a \(k^2/A\) scale.

If instead one can construct collapsed CH-cusp collars with

\[
\mathfrak b(\Sigma)\to 8\pi^2,
\qquad
P(\text{collar})\to0,
\tag{4.5}
\]

then the cap ledger permits very cheap joinings. This is the geometric form of the construction route.

### 4.1. Bianchi-IX test functional

A concrete restricted computation is the cohomogeneity-one ansatz

\[
g=dr^2+a(r)^2\sigma_1^2+b(r)^2\sigma_2^2+c(r)^2\sigma_3^2
\tag{4.6}
\]

on \(S^3\times I\), with an invariant almost-complex structure. One can compute:

\[
Q=\int(4|W^+|^2+s^2/12),
\qquad
\mathfrak b,
\qquad
\|t_J^-\|_2^2,
\tag{4.7}
\]

and minimize subject to outer CH-type interface data and an inner smooth bolt. Define

\[
I_1(L,h)
=
8\pi^2(1-2)+2\mathfrak b(L,h)+\inf Q .
\tag{4.8}
\]

The value of \(I_1\) decides, within this symmetric class, whether a single exceptional cap can be joined at subunit cost. If

\[
\inf_{L,h} I_1 < 8\pi^2,
\tag{4.9}
\]

a cheap cap exists in the ansatz. If

\[
\inf_{L,h} I_1 \ge 8\pi^2
\tag{4.10}
\]

except in the collapsed cusp limit, the cap route supports a tariff.

---

## 5. Competitor geometry and smooth-type information

The integral constraints used so far depend only on rational cohomology and Chern numbers. The formal saturating configuration resembles a disjoint union of the host and \(k\) opposite-sign ASD Einstein pieces with the rational numbers of an opposite-sign fake projective plane. Such a piece has the right volume and curvature numerology to carry one exceptional unit with \(P=0\) internally.

This produces a decisive comparison:

1. If one can glue \(k\) such pieces into the host through collapsed collars with total \(P=o(k)\), then the curvature identities alone cannot force a positive per-class tariff.

2. If the smooth type of the actual \(\overline{\mathbb{CP}}^{\,2}\) summand is essential, the obstruction must come from information not visible in the rational Chern ledger: simple connectivity, the precise Seiberg–Witten chamber, adjunction for the exceptional sphere, or the absence of a suitable ball quotient cap.

Thus a very informative target is the comparison between

\[
\alpha\bigl(X\#k\overline{\mathbb{CP}}^{\,2}\bigr)
\quad\text{and}\quad
\alpha\bigl(X\#k\,\overline{\mathrm{FPP}}\bigr),
\tag{5.1}
\]

where the second summand is a rational-homology opposite-sign projective-type piece if such a smooth or orbifold object can be supplied. If the second infimum is substantially smaller, then any positive gap for the first must use smooth-topological input beyond the shared curvature identities.

---

## 6. Summary of the decisive alternatives

The verified material gives the following exact structure:

\[
\mathsf H^-(t_J^-)=2\pi h^- -\rho_0^J,
\tag{6.1}
\]

\[
P=
2\|\gamma_J^-\|_2^2
+
\int u(5u+s)
+
2\|\rho_*''\|_2^2
+
4\|W_3^+\|_2^2,
\tag{6.2}
\]

\[
\|d^J u\|_{\mathcal H_u^{-1}}
\le
C(\|W_3^+\|_2+\|\rho_*''\|_2+\sqrt P).
\tag{6.3}
\]

The missing substance is one of the following precise mechanisms.

### Lower-bound mechanisms

1. **Orientation coercivity**: a second-Bianchi estimate controlling the harmonic projection of the twist,

   \[
   \|\mathsf H^-(t_J^-)\|_2^2
   \le
   C\sqrt A(\sqrt P+\|W_3^+\|_2+\|\rho_*''\|_2)
   +
   \mathfrak C_{\rm core},
   \]

   with \(\mathfrak C_{\rm core}\) absorbed by noncollapse.

2. **Hopf-ledger coercivity**: a renormalized spinor construction in which every unavoidable zero/Hopf charge contributes a positive finite amount to the unweighted twist unless canceled, together with a theorem that the best-sign class cannot arrange all charges into cheap neutral dipoles.

3. **Transgression coercivity**: the cap estimate

   \[
   (8\pi^2-\mathfrak b(\Sigma))_+
   \le
   qP(\text{collar})+\varepsilon_{\rm collapse},
   \]

   with \(\varepsilon_{\rm collapse}\) controlled by exceptional-sphere area or harmonic radius.

### Construction mechanisms

1. **Diffuse Hopf-core construction**: choose \(u\sim 2\sqrt{k/A}\) away from tiny cores, let the frame phase carry the required Hopf winding through zeros of the torsion amplitude, and solve the AAD phase equation using the \(s=-4\) Goldberg operator.

2. **Density-matrix canonical field**: use

   \[
   S_\delta=\delta^2\Omega_*\otimes\Omega_*+\psi\otimes\psi
   \]

   or its sign-averaged analogue. If the eigenvalue gap remains positive, the unweighted twist is controlled by weighted Seiberg–Witten quantities. If eigenvalue crossings occur, they supply the Hopf ledger.

3. **Cheap cap/gluing construction**: realize each exceptional unit by an ASD Einstein cap with rational \(\overline{\mathbb{CP}}^{\,2}\) numbers and join it through a collapsed collar for which \(\mathfrak b\to8\pi^2\) while \(P\to0\).

The strongest immediate tests are the radial Hopf-core computation, the AAD third-Gray local model near critical points of \(h\), the Bianchi-IX cap functional \(I_1(L,h)\), and the density-matrix eigenvalue gap for the Seiberg–Witten sign family. These convert the current obstruction into explicit quantities that can be computed, minimized, or proved coercive.