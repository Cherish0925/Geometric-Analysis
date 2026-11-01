# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 59,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step59_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step59_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Analyze the zero of the torsion/Nijenhuis section in the closed four-dimensional negative-Einstein almost-Kähler problem. Starting from alpha=∇Ω as a section of E=Λ^{0,1}⊗Λ^{0,2}, the soldered equations (d_b alpha)^-=0, d_b^*alpha=2eta, and the AAD Bianchi/Weitzenböck equations recorded in the supplied notes, derive the strongest trustworthy leading-order constraints at a zero alpha(p)=0. Determine what can and cannot be concluded about vanishing order, isolated local index, sign of that index, and localized top Chern charge. Explore a consequential new route: whether Einstein curvature identities force the leading homogeneous coefficient map into a proper algebraic class incompatible with positive total c2, or instead allow the principal f=z model. Clearly distinguish a proved derivation from a plausible conjecture and point to the next decisive calculation.

## Integrated Scientific Memo

# Scientific memo: torsion zeros in the negative-Einstein almost-Kähler problem

## Main conclusion

The supplied equations force a **positive total localized top Chern charge** and, for a non-Kähler connected solution, **finite-order torsion zeros**. They do not establish isolatedness, a sign for individual indices, or exclusion of a finite-order zero.

A stronger leading-order calculation is available: every homogeneous leading coefficient satisfies
\[
\boxed{P_m(z,\bar z)=z\,h_{m-1}(\bar z)+g_m(\bar z),}
\]
where \(h_{m-1}\) is a scalar antiholomorphic homogeneous polynomial and \(g_m\) is a two-component antiholomorphic homogeneous polynomial. In particular, the principal model \(P_1=z\), with local degree \(+1\), survives the displayed leading equations and pointwise Einstein curvature identities.

This is **not** a constructed Einstein–almost-Kähler germ. Whether nonlinear prolongation excludes this model is the precise unresolved local object.

---

## 1. Topological charge and finite vanishing order

Write
\[
T=\nabla\Omega,\qquad E=\Lambda^{0,1}\otimes\Lambda^{0,2},
\]
identifying \(T\) with the underlying real section \(\alpha\) of the complex rank-two bundle \(E\). The source’s almost-Kähler identity identifies \(T=0\) with \(N=0\).

If \(x_1,x_2\) are the Chern roots of \(T^{1,0}M\), and \(c=x_1+x_2\), then \(\Lambda^{0,1}\) has roots \(x_1,x_2\), and \(\Lambda^{0,2}\) has root \(c\). Thus
\[
c_2(E)=(x_1+c)(x_2+c)
=c_2(TM,J)+2c_1(TM,J)^2,
\]
and
\[
\boxed{\langle c_2(E),[M]\rangle=5\chi+6\tau.}
\]

With the usual curvature-operator norms, a closed Einstein four-manifold satisfies
\[
8\pi^2\chi
=\int_M\left(|W^+|^2+|W^-|^2+\frac{s^2}{24}\right)d\mu,
\]
\[
4\pi^2(2\chi+3\tau)
=\int_M\left(2|W^+|^2+\frac{s^2}{24}\right)d\mu.
\]
For \(s<0\), both quantities are strictly positive, so
\[
5\chi+6\tau=\chi+2(2\chi+3\tau)>0.
\]
Consequently, \(\alpha\) must vanish somewhere.

Let \(Z=\alpha^{-1}(0)\). Pullback of the Thom class defines
\[
\mathfrak e(\alpha)\in H^4(M,M\setminus Z;\mathbb Z),
\]
whose image in \(H^4(M;\mathbb Z)\) is \(c_2(E)\). This is the appropriate **localized charge**, whether or not zeros are isolated.

For isolated zeros, transversality is unnecessary:
\[
\operatorname{ind}_p(\alpha)
=\deg\!\left(\alpha/|\alpha|:S^3_\varepsilon(p)\to S^3\right),
\qquad
\sum_{p\in Z}\operatorname{ind}_p(\alpha)=5\chi+6\tau.
\]
For a positive-dimensional zero set, this point-index formula does not apply. Perturbing the section can compute the Euler number but does not preserve the geometric PDE.

Standard analytic regularity also gives a useful conclusion beyond the restricted AAD unique-continuation theorem: Einstein metrics are analytic in harmonic coordinates; \(\Omega\), being closed and self-dual, is harmonic and hence analytic for that analytic metric. Therefore \(T\) is analytic. On a connected non-Kähler solution, every zero has finite order:
\[
\alpha=P_m+O(r^{m+1}),\qquad m\ge1,\quad P_m\ne0.
\]
Infinite-order vanishing would imply \(\alpha\equiv0\). No uniform upper bound on \(m\) follows.

Moreover,
\[
q=|T|^2=|P_m|^2+O(r^{2m+1}),
\]
so its vanishing order is \(2m\), and
\[
dq(p)=0,\qquad
\nabla^2q(p)(X,Y)=2\langle\nabla_XT,\nabla_YT\rangle.
\]

---

## 2. Complete classification of the leading principal coefficient

Choose normal coordinates adapted to \(J(p)\), a unitary frame \(\ell\) of \(\Lambda^{0,2}\), and connection gauge \(b(p)=0\). At a torsion zero, \(\nabla J(p)=0\), so freezing \(J\) and the frame introduces no contribution at the leading derivative order.

Write
\[
P_m=(f_1\,d\bar z^1+f_2\,d\bar z^2)\otimes\ell.
\]
The lowest-order part of \((d_b\alpha)^-=0\) is
\[
\partial_{z_1}f_2=0,\qquad
\partial_{z_2}f_1=0,\qquad
\partial_{z_1}f_1=\partial_{z_2}f_2=:h.
\]
Commuting derivatives gives
\[
\partial_{z_1}h
=\partial_{z_1}\partial_{z_2}f_2=0,\qquad
\partial_{z_2}h
=\partial_{z_2}\partial_{z_1}f_1=0.
\]
Hence \(h\) is antiholomorphic, and integration yields
\[
\boxed{f_i=z_i h(\bar z)+g_i(\bar z).}
\]
Homogeneity fixes the respective degrees to \(m-1\) and \(m\).

The divergence equation is sourced:
\[
\boxed{\eta_{m-1}=\tfrac12d^*P_m.}
\]
It does **not** require \(P_m\) to be coclosed. For \(z_j=x_j+iy_j\) with Euclidean metric,
\[
d^*P_m=-2\sum_i\partial_{z_i}f_i=-4h\,\ell,
\]
up to the fixed conversion between complex coefficients and the real AAD normalization.

The exterior derivative is
\[
dP_m
=h\sum_i dz^i\wedge d\bar z^i
+k\,d\bar z^1\wedge d\bar z^2,
\]
where
\[
k=z_2\partial_{\bar z_1}h-z_1\partial_{\bar z_2}h
+\partial_{\bar z_1}g_2-\partial_{\bar z_2}g_1.
\]
Thus \(h\) supplies the leading transverse curvature \(\eta\), while \(k\) supplies the leading transverse trace-free curvature \(W_3^+\), with convention-dependent fixed factors.

For \(m=1\), this becomes
\[
\boxed{P_1(z)=cz+B\bar z,\qquad c\in\mathbb C,\ B\in M_2(\mathbb C).}
\]
There are **ten real parameters**, not thirteen. They split into

- two real parameters in \(c\), determining \(\eta(p)\);
- two in \(B_{21}-B_{12}\), determining \(W_3^+(p)\);
- six in the complex symmetric part \(B_{\rm sym}\), invisible to both \(dP_1\) and \(d^*P_1\).

The last six parameters are the genuine symmetric-Hessian freedom at this order.

### Higher-order zeros force Kähler-type curvature at the point

If \(m\ge2\), then \(\nabla T(p)=0\). The Ricci identities
\[
da-Ja\wedge b=-R(J\phi),\qquad
d(Ja)+a\wedge b=-R(\phi)
\]
give
\[
R(\phi)(p)=R(J\phi)(p)=0.
\]
Einstein symmetry of the curvature operator therefore implies
\[
\eta(p)=0,\qquad W_3^+(p)=0.
\]
Since \(\kappa=s+\frac32q\), the self-dual Weyl operator at \(p\) has Kähler-type eigenvalues
\[
s/6,\quad -s/12,\quad -s/12.
\]
This is a **pointwise** conclusion, not neighborhood integrability.

More generally, the off-diagonal curvature is \(O(r^{m-1})\), so
\[
\eta,\ W_3^+=O(r^{m-1}).
\]
Their displayed degree-\((m-1)\) coefficients may vanish.

---

## 3. What the AAD equations add at the zero

At \(p\),
\[
T=0,\quad q=0,\quad dq=0,\quad \kappa=s.
\]
The Einstein specialization of AAD’s Bianchi equation becomes
\[
\boxed{
(\delta\eta)_Z\Omega+\nabla_{JZ}\eta
+2(\delta W_3^+)_Z=0.
}
\]

An important refinement follows from \(W_3^+(\Omega)=0\). Differentiating that algebraic identity shows that the \(\Omega\)-component of \(\delta W_3^+\) is algebraic in \(W_3^+\) and \(T\); hence it vanishes at \(p\). Also \(\langle\nabla\eta,\Omega\rangle=0\) there. Taking the \(\Omega\)-component therefore gives
\[
\boxed{\delta\eta(p)=0,}
\]
and the remaining equation is
\[
\boxed{(\nabla_{JZ}\eta)''+2(\delta W_3^+)_Z''=0.}
\]
The Weitzenböck equation then reduces to
\[
\boxed{
(\nabla^*\nabla T)_X(p)=2(\nabla_X\eta)''(p).
}
\]

These are constraints on the next jets, not additional algebraic equations solely on \(c,B\). In particular, \(\eta(p)\) need not vanish at a first-order zero. The correct statement is that **the pointwise equations permit nonzero \(\eta(p)\)**; neither “generic occurrence” nor occurrence in an actual germ has been proved.

Likewise, the assertion that the ASD equation is “automatic at a zero” needs qualification. Einstein curvature makes its right-hand side self-dual through the Ricci identities, but this still imposes the six real derivative constraints above. The equation is a differential consequence in curvature variables, not a vacuous condition on arbitrary jets.

### Why the principal Bianchi/Weitzenböck terms do not immediately exclude \(P_m\)

At the frozen leading level, curvature is recovered from \(dP_m\), and its exterior Bianchi identity is \(d^2P_m=0\). The divergence is recovered from \(d^*P_m\). Their associated second-order identity is the flat Hodge identity.

This explains why the displayed principal equations do not independently eliminate \(h,g\). It does **not** establish formal integrability of the soldered nonlinear system: the Levi-Civita connection, \(J\), curvature symmetry, and constant-length harmonic form must remain linked throughout prolongation.

---

## 4. Isolated index: what is and is not controlled

For a nondegenerate first-order zero,
\[
\operatorname{ind}_p(\alpha)
=\operatorname{sgn}\det_{\mathbb R}(cz+B\bar z).
\]
The real determinant equals
\[
\det_{\mathbb C}
\begin{pmatrix}cI&B\\ \bar B&\bar cI\end{pmatrix}
=\det_{\mathbb C}(|c|^2I-\bar B B).
\]

Both signs occur among admissible principal coefficients:
\[
P_1=z:\quad \det_{\mathbb R}=1,\quad \operatorname{ind}=+1;
\]
\[
P_1=(z_1+2\bar z_1,z_2):
\quad \det_{\mathbb R}=-3,\quad \operatorname{ind}=-1.
\]
These two coefficients have the same \(c\) and antisymmetric part of \(B\), and hence the same \(\eta(p)\) and \(W_3^+(p)\). Their different indices are caused entirely by the curvature-invisible \(B_{\rm sym}\).

If \(\eta(p)=0\), then \(c=0\). A nondegenerate coefficient is then conjugate-linear:
\[
P_1=B\bar z,\qquad
\det_{\mathbb R}P_1=|\det_{\mathbb C}B|^2>0.
\]
Thus even vanishing of \(\eta\) **at the zero** would not provide a nonpositive-index theorem.

For higher-order zeros, if \(P_m\) has no zero on \(S^3\), then
\[
\operatorname{ind}_p(\alpha)=\deg(P_m/|P_m|).
\]
If \(P_m\) does vanish on the sphere, higher coefficients can decide both isolatedness and index; the leading coefficient alone is insufficient.

The principal equations allow arbitrarily high-order positive-charge models:
\[
P_m=(\bar z_1^{\,m},\bar z_2^{\,m}),\qquad
\deg(P_m/|P_m|)=m^2.
\]
They satisfy \(dP_m=d^*P_m=0\). These are only principal models, not negative-Einstein germs, but they show that neither finite order nor absence of leading \(\eta\) excludes positive charge.

Finally, localized charge is not the integral of a smooth Chern–Weil density over a shrinking ball. Such an integral tends to zero. The nonzero integer is a relative Euler obstruction, represented by boundary/transgression data associated with the normalized section.

---

## 5. Consequential route: a precise obstruction through the opposite structure

There is a geometric formulation of the charge problem that connects directly to AAD.

Near an isolated zero, trivialize \(E\). On a small surrounding sphere,
\[
u=\alpha/|\alpha|:S^3\to S^3
\]
has degree \(\operatorname{ind}_p(\alpha)\). The Kähler-nullity line \(D\), or its orthogonal line \(D^\perp\), depends only on the projective coefficient of \(\alpha\). Thus its map to \(\mathbb CP^1\) is the Hopf projection composed with \(u\), up to fixed identifications:
\[
S^3\xrightarrow{u}S^3\xrightarrow{H}\mathbb CP^1.
\]
With compatible conventions,
\[
\operatorname{Hopf}(H\circ u)=\deg(u).
\]

Therefore:

\[
\boxed{\text{Extension of the nullity splitting across an isolated zero forces its index to be zero.}}
\]

Equivalently, extension of the associated opposite almost complex structure \(I\) supplies an obstruction to the \(P_1=z\) model: that model has a nontrivial Hopf class.

This is a proved topological implication, **not a proved extension theorem in the unrestricted Einstein problem**. In AAD Proposition 3, extension follows from the third-Gray classification, an opposite Kähler structure, and functions constant along the nullity complement. Those ingredients are absent when \(\eta\ne0\). Analyticity alone cannot replace them.

This formulation identifies a concrete alternative to determinant inequalities: establish extension, or suitable control of its obstruction, from the full Einstein identities. Positive-dimensional zero components would still require their relative Euler charge to be analyzed.

---

## 6. The unresolved prolongation and the next decisive calculation

The established leading algebraic class contains \(P_1=z\), an open neighborhood of positive-determinant coefficients, and negative-determinant coefficients. Pointwise Einstein curvature identities do not restrict this class to nonpositive index.

The first genuinely nonlinear test is obtained by differentiating the AAD system at a first-order zero. Put
\[
L_X=(\nabla_XT)_p.
\]
Then
\[
\nabla^2q(p)(X,Y)=2\langle L_X,L_Y\rangle,\qquad
\nabla^2\kappa(p)(X,Y)=3\langle L_X,L_Y\rangle,
\]
while differentiated coupling terms include
\[
\nabla_Y(T_{\eta(Z)})\big|_p=L_Y(\eta(Z)),
\qquad
\nabla_Y(T_{J\eta(X)})\big|_p=L_Y(J\eta(X)).
\]
These are precisely the quadratic terms omitted by a frozen-symbol analysis.

A decisive finite computation would fix
\[
P_1=cz,\qquad c\ne0,\qquad B=0,
\]
derive \(\eta(p)\) and \(W_3^+(p)=0\) from the Ricci identities, and solve the first nonlinear prolongation while retaining:

- torsion-free Cartan equations and the curvature operator’s algebraic symmetries;
- closure and constant norm of \(\Omega\), with \(J\) determined by \(\Omega\);
- the full Einstein condition;
- Ricci identities, Bianchi equations, and their differentiated relations.

The unknown higher jets must be eliminated rather than treating derivatives of \(\eta,W_3^+\) as independent forcing. Scalar curvature must remain symbolic, or the relative size of \(|c|\) and \(|s|\) must be retained; there is no established justification for fixing both independently.

An exact incompatibility would give the sought additional polynomial relation on \(L\). Compatibility would show only that the positive-charge model survives that prolongation—not that a formal germ exists to all orders or converges.

The supplied material does not contain this calculation. It also does not justify the stronger assertion that every relevant third-jet compatibility has already been checked. Numerical truncated jets and raw dimension counts cannot resolve it; Step 55 explicitly demonstrates why universal Ricci-symbol and Bianchi dependencies must be removed.

**Scientific endpoint:** positive localized charge and the full leading coefficient class are determined. The unresolved question is whether nonlinear soldered Einstein prolongation excludes positive-charge zero models—or forces extension of the nullity splitting across their zeros. A determinant-degeneracy result alone would not close the problem, because degenerate isolated zeros and positive-dimensional zero loci can still carry nonzero relative Euler charge.