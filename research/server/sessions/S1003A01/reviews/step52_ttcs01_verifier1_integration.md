# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 52,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step52_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step52_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematics of Theorem 52.A (kernel-direction Burns insertion on an arbitrary Einstein four-manifold) and Lemma 52.C in workspace/notes/step52_kernel_insertion_theorem.md. Check specifically: (1) the SU(2)_- reduction in Section 2 (is the a^2 eps^2 CGB density really constant on S^3 for SU(2)_- -invariant data, and do the 10 tensors sym(v_i v_j)/u span all SU(2)_- -invariant degree-0 symmetric 2-tensors?), and whether the exact results in data/step52a/exact_su2minus_analysis.json (F_opt = -mu(mu - s/8) - |T|^2; family F = -|T|^2 with zero gradient; mixed-block linear term) are consistent with the script step52_exact_su2minus_fast.py and the convexity/averaging argument; (2) the W^- cross-term vanishing by SU(2)_- irreducibility; (3) the two-scale remainder argument of Section 3.2: Hadamard factorization R = r^4 z^2 rho, evenness in r via the antipodal map, the claim that only h2 and k0 enter rho(0,0), and the O(eps^2) control of core and outer transition; (4) Section 3.3: that the order-eps contribution equals minus an inner-boundary flux of a transgression form, that its leading constant is a U(2)_zeta-invariant linear function of Rm_p (so alpha s + beta W+(zeta,zeta)), that the r^1 term vanishes by parity, and that the Ch.5 CH construction legitimately calibrates beta = 12 alpha (does Ch.5's Bianchi-IX neck have the same leading flux as the additive normal-coordinate neck?); (5) Lemma 52.C: delta W+ = 0 with constant eigenvalues (a,-a/2,-a/2) forcing grad u = 0, and the Kahler eigenvalue contradiction; (6) the sign correction in Section 5 and Corollary 52.B. Report errors, missing steps, and any correction that changes the theorem statement, with precise repairs.

## Integrated Scientific Memo

# Verification memo: Theorem 52.A and Lemma 52.C

## Main conclusion

The logarithmic coefficient and Lemma 52.C are correct. Theorem 52.A has the stated expansion
\[
P(g_\varepsilon)=P(g)+8\pi^2
-4\pi^2|T|^2\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2),
\]
provided the inherited Step-50 \(W^-\) compatibility identity is used.

The note nevertheless needs several repairs:

- The definition of \(G(r,x)\) in §3.2 contains an erroneous factor \(r^{-2}\).
- Haar averaging requires an averaging-closed corrector class, not merely a group-stable set.
- The Ch.5 calibration is not established by the supplied materials: its neck formulas are absent. A direct characteristic-form computation, given below, removes this dependency and proves the exact first-order term
  \[
  -8\pi^2\varepsilon R^+_p(\zeta,\zeta).
  \]
- Corollary 52.B omits \(R^+_p=0\), and its “iff” must be restricted to the displayed two-scale ansatz with fixed degree-zero correctors.
- The conclusion in §5 that the contact set has empty interior requires \(s<0\). There is a separate \(s=0,\ R^+\equiv0\) branch.

The algebraic verification below uses the supplied polynomial, analysis script, and curvature-computation script; it does not assume access to the absent raw matrix or Step-50 identity script.

## 1. The \(SU(2)_-\) reduction is valid, with one qualification

Let \(H=SU(2)_-\), the quaternionic action commuting with \(J_1,J_2,J_3\). It acts freely and transitively on \(S^3\). The frame
\[
e_0(x)=x/r,\qquad e_m(x)=J_mx/r,\quad m=1,2,3,
\]
is orthonormal and \(H\)-equivariant.

When \(W^-=\operatorname{Ric}^\circ=0\), the curvature jet consists of \(s,W^+\), on which \(H\) acts trivially. Hence \(h_2\), \(k_B\), and invariant correctors are equivariant tensor fields. Naturality of the curvature density then makes its \(a^2\varepsilon^2\) coefficient an \(H\)-invariant scalar on \(S^3\). It is therefore constant.

With the normalization used in the scripts,
\[
F=\frac1{8\pi^2}\int_{S^3}q\,d\Omega
=\frac{q(x_0)}4,
\]
because \(\operatorname{vol}(S^3)=2\pi^2\). Thus the script’s single-point evaluation and division by four are correct.

### The ten tensors are the full invariant space

An invariant degree-zero ambient symmetric two-tensor is determined by its value at one sphere point. The stabilizer is trivial, so that value can be any element of \(\operatorname{Sym}^2(\mathbb R^4)^*\), a ten-dimensional space. Consequently
\[
\frac{\operatorname{sym}(v_i v_j^T)}u,\qquad 0\le i\le j\le3,
\]
form a basis of all such invariant tensors. These are ambient tensors, including radial components—not merely tensors intrinsic to \(S^3\).

### Convexity and averaging

The corrector-quadratic part of \(F\) is
\[
Q(k_0)=\frac1{8\pi^2}\int_{S^3}
\left(4|D_\delta W^+[k_0]|^2+
\frac{|D_\delta s[k_0]|^2}{12}\right)d\Omega.
\]
It is nonnegative, so \(F\) is convex. For the Haar average \(\bar k_0\),
\[
F(\bar k_0)\le \int_HF(h\cdot k_0)\,dh=F(k_0).
\]

The phrase “any \(SU(2)_-\)-stable class” is too broad. Replace it by:

> Any \(SU(2)_-\)-invariant corrector class closed under Haar averaging; in particular, the full smooth degree-zero space, or a suitable invariant linear or closed convex subspace.

Group stability alone does not keep the average inside an arbitrary nonconvex class. Also, averaging establishes equality of infima; attainment additionally follows here from the explicit finite-dimensional minimizer in the eigenvector sector.

## 2. Exact polynomial, optimum, and kernel family

For \(\zeta=J_3\) an eigenvector, put
\[
\mu=w_{33}+\frac{s}{12}
=\frac{s}{12}-w_{11}-w_{22}.
\]
Without diagonalizing the restriction to \(\zeta^\perp\),
\[
|T|^2=\frac{(w_{11}-w_{22})^2}{2}+2w_{12}^2.
\]
The supplied `Fopt` expands exactly to
\[
\boxed{F_{\mathrm{opt}}
=-\mu\left(\mu-\frac{s}{8}\right)-|T|^2.}
\]
Thus `Fopt_minus_Phi_w13=0 = -2*w12**2` is correct: the script’s \(\Phi\) omits the off-diagonal contribution to \(|T|^2\). The formula \(|T|^2=(\mu_1-\mu_2)^2/2\) is valid when \(\mu_1,\mu_2\) denote the actual eigenvalues of the restricted block.

The recorded corrector Hessian has spectrum
\[
0^{\times4},\quad 2,\quad4^{\times3},\quad8^{\times2}.
\]
It is positive semidefinite.

On the kernel locus,
\[
w_{22}=\frac{s}{12}-w_{11},\qquad w_{13}=w_{23}=0,
\]
the family in the note has script coefficients
\[
c_4=\frac{7A}{4}+\frac{T_{11}}3,\quad
c_7=\frac{7A}{4}-\frac{T_{11}}3,\quad
c_9=\frac A2,\quad
c_5=\frac{2T_{12}}3,\qquad A=-\frac{s}{12}.
\]
The factor two in \(c_5\) is necessary because the script uses the half-symmetrized basis. Substitution into the supplied polynomial gives
\[
F=-|T|^2,\qquad \partial_{c_i}F=0\quad(0\le i\le9).
\]
Convexity then proves global minimality.

At \(s=-24,\ T=\operatorname{diag}(3,-3)\), the coefficients are
\[
(c_4,c_7,c_9)=\left(\frac92,\frac52,1\right),\qquad F=-18.
\]
This reproduces the claimed CH coefficient without using Ch.5’s value \(-18\).

### Mixed block

The supplied polynomial gives precisely
\[
F-F|_{w_{13}=0}
=\frac{2w_{13}}9(-9c_2+15c_6+7w_{13}).
\]
Here \(c_2\) is Hessian-null, with linear coefficient \(-2w_{13}\). Indeed,
\[
\mathcal L_{(\log r)J_2x}\delta
=2\,\frac{\operatorname{sym}(x\otimes J_2x)}{r^2}.
\]
For \(w_{13}\ne0\), the coefficient functional is unbounded below along this direction. This is compatible with convexity: a convex semidefinite quadratic can have a nonzero linear term on its nullspace.

One sentence needs correction. Mixed-block unboundedness occurs whenever the mixed block is nonzero, **not only** when \(\mu_\zeta=0\). Under the additional assumption \(\mu_\zeta=0\), a nonzero mixed block does force \(R^+\) to be indefinite. Conversely, for \(R^+\le0\),
\[
\langle R^+\zeta,\zeta\rangle=0\ \Longrightarrow\ R^+\zeta=0.
\]

### Script and data corrections

- `CH_family_coeffs` contains an unresolved symbolic first entry because `subs(chs).subs(ker)` reintroduces \(s,w_{11}\). Use `subs(ker).subs(chs)`. The correct value is \(9/2\).
- The computation script defaults to `data/step52`, whereas the analysis reads `data/step52a`; set `OUTDIR=step52a` or align the defaults.
- `Fopt_w13_part = 0` is computed after setting \(w_{13}=0\); it is not evidence for an unrestricted mixed-block optimum.
- The vanishing \(a\varepsilon\) coefficient is automatic from the flat Burns chiral curvature being zero. It does **not** establish vanishing of the geometric order-\(\varepsilon\) term.

The script’s inverse/frame expansions through fourth power suffice for bidegree \((2,2)\); its \(1/2\) normalization of the quaternionic two-form rows is consistent with an orthonormal \(\Lambda^+\) basis.

## 3. The \(W^-\) cross-term argument is correct

The integrated coefficient is an invariant quadratic form on jet plus corrector space. The \((s,W^+)\) data and \(k_0^{\ker}\) are \(SU(2)_-\)-fixed. The natural linear map
\[
W^-\longmapsto (h_W,k_0^W)
\]
is equivariant, and its image belongs to the spin-2 isotypic component.

Pairing a fixed vector with this image produces an invariant linear functional on the nontrivial irreducible spin-2 representation. Such a functional is zero. Hence all the integrated cross terms vanish.

Irreducibility does **not**, by itself, eliminate \(|W^-|^2\). For the self-term, expand the chiral curvature of
\[
\delta+a h_2+\varepsilon k_B+a\varepsilon k_0.
\]
Since all pure-Burns chiral coefficients vanish, the \(W^-\)-quadratic contribution at \(a^2\varepsilon^2\) is only the square of
\[
D_\delta\mathcal C[k_0^W]
+D_\delta^2\mathcal C[h_W,k_B].
\]
The inherited Step-50 identity makes this zero pointwise. Terms paired with the background chiral curvature cannot contribute a \(W^-\)-self-term because
\[
D_\delta\mathcal C[h_W]=0.
\]
Therefore
\[
F(k_0^{\ker}+k_0^W)=-|T|^2.
\]

This also establishes optimality on arbitrary Einstein jets over the full degree-zero class: after projecting to the invariant component, the remaining source/corrector contribution is a nonnegative square, and \(k_0^W\) cancels the \(W^-\) source. The note should cite both the degree decomposition and the compatibility identity, rather than attributing everything to irreducibility.

## 4. Two-scale remainder: correct after fixing \(G\)

Rename the cutoff radius \(t_0\), to distinguish it from the matrix \(T\).

The rescaled metric satisfies
\[
r^{-2}\Phi_r^*g=g(rx)
\]
in Cartesian components. Thus the correct definition is
\[
\boxed{G(r,x)=g(rx)-\delta
=r^2h_2+r^3h_3+\cdots,}
\]
not \(r^{-2}(g(rx)-\delta)\).

On the neck,
\[
\widehat g_{r,z}
=\delta+G(r,x)+zk_B+zr^2k_0,\qquad z=\varepsilon/r^2.
\]
This is smooth as a family of metrics near the unit sphere for
\[
|r|\le t_0,\qquad 0\le z\le1/4.
\]
Smooth Taylor expansion suffices; real analyticity is unnecessary.

### Evenness and factorization

For the antipodal map \(A(x)=-x\),
\[
A^*\widehat g_{r,z}=\widehat g_{-r,z}.
\]
Both \(k_B\) and the chosen \(k_0\), including \(k_0^W\), are even. The antipodal map preserves orientation in \(\mathbb R^4\) and on \(S^3\). Consequently the sphere-averaged density satisfies
\[
\Psi(-r,z)=\Psi(r,z).
\]

At \(r=0\), the metric is exactly Burns with parameter \(z\), so \(\mathcal C=0\). The perturbation begins at \(r^2\), giving
\[
\mathcal C(\widehat g_{r,z})=r^2\mathcal C_2(z)+O(r^3),
\qquad \Psi(r,z)=r^4\widetilde\Psi(r,z),
\]
with smooth, even \(\widetilde\Psi\). Therefore
\[
R=\Psi(r,z)-\Psi(r,0)-z\partial_z\Psi(r,0)
=r^4z^2\rho(r,z),
\]
by Taylor’s integral remainder in \(z\). This explicitly justifies the joint Hadamard factorization and smoothness of \(\rho\).

The \(r^4\) coefficient of the density is
\[
|\mathcal C_2(z)|^2_{\delta+zk_B}\,dV_{\delta+zk_B}.
\]
It depends only on \(h_2,k_0,k_B\). Higher background jets cannot enter it. Hence
\[
\rho(0,0)=F,\qquad |\rho(r,z)-F|\le C(r^2+z),
\]
where the \(r^2\) bound uses evenness.

Integration gives
\[
\int_{2\sqrt\varepsilon}^{t_0}R\,\frac{dr}{r}
=\frac F2\varepsilon^2\log(1/\varepsilon)+O_{t_0}(\varepsilon^2),
\]
since
\[
\int_{2\sqrt\varepsilon}^{t_0}
\left(r^2+\frac{\varepsilon}{r^2}\right)\frac{dr}{r}=O_{t_0}(1).
\]

### Core and outer transition

On the fixed scaled core annulus,
\[
\varepsilon^{-1}\Phi_{\sqrt\varepsilon}^*g_\varepsilon
=g_{\mathrm{Burns},1}+O_{C^2}(\varepsilon).
\]
Burns has \(\mathcal C=0\), so its perturbed \(f\)-integral is \(O(\varepsilon^2)\). The removed background ball also contributes \(O(\varepsilon^2)\).

For the outer transition,
\[
f(g+\varepsilon\chi k)-f(g)
=\varepsilon Df_g[\chi k]+O_{t_0}(\varepsilon^2).
\]
Only the Taylor remainder is \(O(\varepsilon^2)\). The entire outer contribution generally is not: its linear term must be combined with the neck linear term and converted to flux.

Positivity, agreement of the metric formulas, and smooth extension across the Burns exceptional sphere are valid for sufficiently small \(\varepsilon\).

## 5. First-order flux: a direct proof replacing CH calibration

At an Einstein metric,
\[
D(|\operatorname{Ric}^\circ|^2dV)_g[h]=0.
\]
The pointwise characteristic-form identity therefore gives
\[
Df_g[h]=d\Theta_g(h).
\]
The neck and outer linear terms combine to
\[
\varepsilon\int_{r\ge2\sqrt\varepsilon}Df_g[\chi_{\rm out}k]
=-\varepsilon\int_{S_{2\sqrt\varepsilon}}\Theta_g(k).
\]
The minus sign is correct: the inner boundary has the opposite orientation to the boundary of the ball.

For \(k_B=O(r^{-2})\), the connection variation is \(O(r^{-3})\); pairing with background curvature and integrating over \(S_r\) yields a constant limit. For degree-zero \(k_0\), the connection variation is \(O(r^{-1})\), so its flux is \(O(r^2)\). Antipodal symmetry eliminates the term linear in \(r\). Thus
\[
\int_{S_r}\Theta_g(k)=\theta_2+O(r^2).
\]

The invariant-functional argument correctly gives
\[
\theta_2=\alpha s+\beta W^+(\zeta,\zeta).
\]
The following calculation fixes both constants, without Ch.5 or Step 8.

### Characteristic-form calculation

For the induced connection on \(\Lambda^+\),
\[
p_1(\Lambda^+)=p_1(TX)+2e(TX),
\]
and the supplied CGB identity becomes
\[
f-|\operatorname{Ric}^\circ|^2dV=8\pi^2p_1(\Lambda^+).
\]
Using
\[
p_1(\Lambda^+)=-\frac1{8\pi^2}\operatorname{tr}(F^+\wedge F^+),
\]
one may take
\[
\Theta_g(h)=-2\operatorname{tr}\bigl(\dot A^+[h]\wedge F^+\bigr).
\]

Let \(\Omega=\sqrt2\,\zeta\) be the flat Kähler form and
\[
\eta=r^{-2}\iota_x\Omega.
\]
Then
\[
\Omega=r\,dr\wedge\eta+\frac{r^2}{2}d\eta,
\qquad \int_{S^3}\eta\wedge d\eta=4\pi^2.
\]

The entire flat Burns family is Kähler for this complex structure. In the Hermitian orthonormal-frame identification, its \(\Lambda^+\) connection fixes \(\zeta\); its variation lies in the one-dimensional stabilizer algebra. Let \(L_\zeta\) be its rotation generator, normalized by
\[
\operatorname{tr}(L_\zeta^2)=-2.
\]
The associated connection one-form is the Ricci connection, up to simultaneous sign conventions for connection and curvature. Since
\[
\det_{\mathbb C}g_{\mathrm{Burns},\varepsilon}=1+\varepsilon/r^2,
\]
its variation can be written
\[
\dot a=-\frac12d^c(r^{-2})=r^{-2}\eta,
\qquad \dot A^+[k_B]=L_\zeta\,\dot a.
\]
Here \(d^cf=-df\circ J\).

For an Einstein background, the \(L_\zeta\)-component of \(F^+\) has diagonal part
\[
\mu_\zeta\Omega,\qquad \mu_\zeta=R^+(\zeta,\zeta).
\]
Its off-diagonal self-dual components have zero pairing after sphere integration. Background corrections to the flat connection variation contribute only \(O(r^2)\) to the flux. Hence
\[
\begin{aligned}
\theta_2
&=4\mu_\zeta\int_{S_r}r^{-2}\eta\wedge\Omega\\
&=4\mu_\zeta\cdot\frac12\int_{S^3}\eta\wedge d\eta\\
&=\boxed{8\pi^2\mu_\zeta}.
\end{aligned}
\]
Thus
\[
\boxed{\text{linear contribution}=-8\pi^2\varepsilon\mu_\zeta,}
\qquad
\alpha=\frac{2\pi^2}{3},\quad\beta=8\pi^2=12\alpha.
\]
This independently repairs the flux step and agrees with the Step-50 value \(\ell=-\mu_\zeta\) in \(P/8\pi^2\) normalization.

### What remains unverified about the CH comparison

The supplied context does not contain Ch.5’s Bianchi–IX formulas. Therefore it does not establish the claimed normal-coordinate equivalence of its leading flux.

A valid comparison must show that the singular linear perturbation is a nonzero multiple of \(k_B\), modulo gauge terms and degree-zero or less singular terms, and justify the relevant core asymptotics. Degree-zero additions do not change the constant flux; gauge terms have vanishing small-sphere flux. An additional nongauge degree-\(-2\) perturbation cannot simply be ignored.

Accordingly, the CH calibration is an unproved comparison in the original note. The direct computation above makes it unnecessary.

## 6. Theorem 52.A and Lemma 52.C

For \(R^+\zeta=0\), the linear flux vanishes. Combining
\[
F=-|T|^2,\qquad
8\pi^2\cdot\frac F2=-4\pi^2|T|^2,
\]
with the drop of \(2\chi+3\tau\) by one proves the stated theorem.

No change to its numerical coefficient is needed. Closedness gives \(P(g)=0\); without closedness, global \(P\) requires finite integrals or a relative/local interpretation. The local construction actually only requires the background to be Einstein on the insertion ball.

### Lemma 52.C is correct

Locally choose a unit eigenform \(u\) for the simple eigenvalue \(a\ne0\):
\[
W^+=\frac{3a}{2}u\otimes u-\frac a2I.
\]
Because \(a=-s/12\) is constant and \(g\) is Einstein,
\[
0=\delta W^+\quad\Longrightarrow\quad
(\nabla^iu_{ij})u_{kl}+u_{ij}\nabla^iu_{kl}=0.
\]
Contracting with \(u^{kl}\), constant norm gives
\[
\nabla^iu_{ij}=0.
\]
Consequently
\[
u_{ij}\nabla^iu_{kl}=0.
\]
A nonzero self-dual form is nondegenerate, with \(u_i{}^ku_k{}^j=-c\delta_i{}^j\), \(c>0\). Thus \(\nabla u=0\).

The resulting parallel complex structure makes the metric locally Kähler, with
\[
W^+(u)=\frac{s}{6}u.
\]
But the assumed eigenvalue gives \(W^+(u)=-s u/12\), forcing \(s=0\), a contradiction. The possible global sign ambiguity of \(u\) is irrelevant.

The displayed Weitzenböck evaluation also gives \(-9a^2\), consistent with a local maximum; the lemma does not exclude isolated contact points.

## 7. Corrected Corollary 52.B and §5

For an eigenvector orientation and an optimal fixed degree-zero corrector,
\[
\frac{P(g_\varepsilon)-P(g)-8\pi^2}{8\pi^2}
=-\mu_\zeta\varepsilon
+\frac12\left[-\mu_\zeta\left(\mu_\zeta-\frac{s}{8}\right)-|T|^2\right]
\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2).
\]

Therefore the corollary’s existence criterion is correct **within this ansatz and at these two orders**:

- A positive eigenvalue gives a first-order decrease.
- A kernel vector with \(T\ne0\) gives a logarithmic decrease.

The complete list of cases without either decrease is
\[
\boxed{
\begin{array}{ll}
\text{(i)}&R^+<0;\\
\text{(ii)}&s<0,\quad\operatorname{spec}(R^+)=(0,s/8,s/8);\\
\text{(iii)}&R^+=0\quad(s=0,\ W^+=0).
\end{array}}
\]
Case (iii) is missing from the note. These are not claims about the unresolved \(O(\varepsilon^2)\) term or about all possible insertion geometries.

The sign correction in §5 is valid:
\[
F_{\rm opt}\big|_{\ker R^+}=-|T|^2\le0,
\qquad
W^+=0\Longrightarrow F_{\rm opt}=s^2/288>0
\quad(s\ne0).
\]
In \(R^+<0\), the positive first-order cost dominates any logarithmic term. The inequality
\[
-\mu(\mu-s/8)>0\quad(s/8<\mu<0)
\]
concerns only that summand; positivity of the full \(F\) also requires it to exceed \(|T|^2\).

For the surviving-bulk discussion, separate the scalar-curvature cases:

- If \(s<0\), excluded nondegenerate kernel points leave only the simple-kernel contact spectrum in (ii). Lemma 52.C makes this contact set closed with empty interior, so \(R^+<0\) off it.
- If \(s=0\), \(R^+\le0\) and trace zero force \(R^+\equiv0\). The empty-interior conclusion does not apply.
- If \(s>0\), \(R^+\le0\) is impossible.

Finally, for \(s<0\), writing \(a=-s/12\), the constraints \(\lambda_i(W^+)\le a\) and \(\sum\lambda_i=0\) give
\[
|W^+|^2\le6a^2=\frac{s^2}{24}.
\]
Equality requires spectrum \((a,a,-2a)\), hence a two-dimensional kernel of \(R^+\) with \(T\ne0\). It is excluded by Theorem 52.A. Thus the claimed strict Weyl bound in the negative-scalar surviving branch is justified.