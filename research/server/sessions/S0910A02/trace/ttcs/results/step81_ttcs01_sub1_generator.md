# TTCS Independent Branch Record

```json
{
  "step_id": 81,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step81_alignment_mechanism_definitive.md",
    "Sessions/S0910A02/workspace/data/step81_alignment_chain_exact.json",
    "Sessions/S0910A02/workspace/notes/step79_alignment_closure_and_collapse_transition.md"
  ]
}
```

## Task

On a compact oriented positive Einstein 4-manifold (M⁴, g) with Ric = 3g, s = 12, the Weitzenböck operator L = ∇*∇ - 2W⁺ + (s/3) on self-dual 2-forms has kernel of dimension b_+(M). Every known compact positive Einstein 4-manifold has min(b_+, b_-) ≤ 1. The crude summed-Weitzenböck chain gives Gursky-LeBrun (independent of b_+) with a 22.5% margin for χ=8, τ=0.

Generate mathematically precise conjectures and possible proof strategies for a b_+-DEPENDENT Weyl energy inequality. Specifically:

(A) Is there a spectral-theoretic argument (CLR, heat kernel, zeta function, Selberg-type) that bounds N_0(L) in terms of the negative-part integral ∫(2α-4)_+^n for appropriate n, with constants that depend on the Yamabe constant Y = 12√V, leading to ∫|W+|² ≥ f(b_+)·V with f(3) > 9?

(B) Is there an argument using the determinant of the Gram matrix G_ab(x) = ⟨ω_a(x), ω_b(x)⟩ of three harmonic SD forms? On a non-symplectic manifold, no form can be everywhere nonzero. The determinant det G measures the 'volume' of the harmonic forms in Λ⁺. Does Einstein rigidity constrain det G in a way that forces ∫|W+|² to be large?

(C) Is there a Bochner/Berger-type argument using the tensor T = Σ ω_a ⊗ ω_a directly? For b_+=3, T is a symmetric endomorphism of Λ⁺ with ∫trT = 3. Does T satisfy a useful PDE (from the individual Weitzenböck equations) that constrains its pointwise eigenvalue distribution?

(D) Is there an obstruction from mod-2 or integral characteristic classes, spin structures, or index theory that prevents positive Einstein metrics with b_+ ≥ 2 more directly?

For each direction, give the precise mathematical formulation and identify the decisive step that would need to be proved. Do not fabricate literature references.

## Output

Let  
\[
L=\nabla^*\nabla-2W^++4I_{\Lambda^+},\qquad  
B:=2W^+-4I_{\Lambda^+},
\]
so zero modes of \(L\) satisfy
\[
\nabla^*\nabla\omega=B\omega .
\]
Write the eigenvalues of \(W^+\) as \(\alpha\ge \beta\ge \gamma\), \(\alpha+\beta+\gamma=0\), and define the attractive scalar well
\[
q:=(2\alpha-4)_+ .
\]
Also let \(B_+\) be the positive spectral part of \(B\). Since a parallel self-dual form on a positive Einstein 4-manifold gives a Kähler-Einstein structure and hence \(b_+=1\), any case with \(b_+\ge2\) has no parallel self-dual section. Thus a spectral count for \(L\) should not have the CP\(^2\) “free Kähler mode” once \(b_+\ge2\).

Below are four precise theorem shapes that would produce a genuinely \(b_+\)-dependent Weyl energy estimate.

---

## (A) Spectral route: an Einstein-CLR inequality for \(L\)

### A1. Scalar-well formulation

A sharp useful form would be:

\[
\boxed{
b_+(M)\le \mathcal C_s\,Y^{-2}\int_M q^2\,dV
}
\qquad (b_+\ge2),
\]
where \(Y=12\sqrt V\) is the Yamabe constant of the Einstein metric.

The exponent is \(2\), because the base dimension is \(4\). The quantity \(Y^{-2}\int q^2\) is scale invariant.

The pointwise algebra
\[
q^2=(2\alpha-4)_+^2\le 4\alpha^2\le \frac83|W^+|^2
\]
would then give
\[
\int |W^+|^2\ge \frac38\int q^2
\ge \frac38\,\frac{b_+Y^2}{\mathcal C_s}
=\frac{54}{\mathcal C_s}\,b_+\,V .
\]
Thus
\[
\boxed{
f(b_+)=\frac{54}{\mathcal C_s}b_+ .
}
\]
For \(b_+=3\), this gives \(f(3)>9\) exactly when
\[
\boxed{\mathcal C_s<18.}
\]

If the spectral argument naturally counts only the excess beyond one possible threshold mode,
\[
b_+-1\le \mathcal C_sY^{-2}\int q^2 ,
\]
then \(b_+=3\) requires
\[
\mathcal C_s<12.
\]

### A2. Matrix-well formulation

A more intrinsic bundle version is

\[
\boxed{
b_+(M)\le \mathcal C_m\,Y^{-2}\int_M \operatorname{tr}(B_+^2)\,dV .
}
\]

Since
\[
\operatorname{tr}(B_+^2)
=\sum_i(2w_i-4)_+^2
\le 4|W^+|^2 ,
\]
one obtains
\[
\int |W^+|^2
\ge \frac14\int \operatorname{tr}(B_+^2)
\ge \frac{36}{\mathcal C_m}\,b_+\,V .
\]
So
\[
\boxed{
f(b_+)=\frac{36}{\mathcal C_m}b_+ .
}
\]
For \(b_+=3\), \(f(3)>9\) follows from
\[
\boxed{\mathcal C_m<12.}
\]

### A3. Stronger “excess above the Kähler value” version

The Gursky-LeBrun base value is
\[
\int |W^+|^2\ge 6V.
\]
A sharper spectral-to-energy mechanism would use an estimate of the form
\[
\boxed{
\int q^2\le c_0\left(\int |W^+|^2-6V\right).
}
\]
Then the scalar CLR inequality gives
\[
\int |W^+|^2
\ge 6V+\frac{144}{c_0\mathcal C_s}b_+\,V .
\]
With the natural algebraic constant \(c_0=8/3\), this becomes
\[
\boxed{
\int |W^+|^2
\ge \left(6+\frac{54}{\mathcal C_s}b_+\right)V .
}
\]
For \(b_+=3\), \(f(3)>9\) would follow already from
\[
\mathcal C_s<54.
\]

The hard part is that the pointwise inequality only gives
\[
q^2\le \frac83(|W^+|^2-6)
\]
on the region where \(\alpha>2\), and the integral of the positive excess \((|W^+|^2-6)_+\) can in principle be larger than the global excess \(\int |W^+|^2-6V\). Thus the decisive extra theorem would be a non-oscillation estimate for Einstein \(W^+\):
\[
\boxed{
\int_M (|W^+|^2-6)_+\,dV
\le \Lambda\left(\int_M |W^+|^2\,dV-6V\right),
}
\]
or directly the displayed \(q^2\)-excess inequality.

### A4. Possible spectral proofs

1. **Birman-Schwinger/CLR.**  
   Use the comparison
   \[
   L\ge \nabla^*\nabla-qI
   \]
   and bound the dimension of subspaces on which
   \[
   \int |\nabla\sigma|^2-\int q|\sigma|^2\le0.
   \]
   The decisive step is an endpoint \(4\)-dimensional CLR estimate with Yamabe normalization and constant below the numerical thresholds above.

2. **Heat kernel domination.**  
   Kato domination gives a scalar heat kernel comparison for \(e^{-tL}\) by a scalar Schrödinger heat semigroup with potential \(q\). The Yamabe Sobolev inequality
   \[
   Y\|u\|_4^2\le 6\int|\nabla u|^2+12\int u^2
   \]
   supplies the heat kernel scale. The decisive step is keeping the compact heat kernel constant small enough after removing possible parallel self-dual sections.

3. **Zeta function route.**  
   For the nonnegative operator \(L\),
   \[
   \zeta_L(0)+b_+(M)=a_4(L),
   \]
   where \(a_4(L)\) is the local heat coefficient. Since \(a_4(L)\) is an explicit curvature integral involving \(W^+\), a lower estimate for \(\zeta_L(0)\) on positive Einstein 4-manifolds would give a direct \(b_+\)-energy inequality. The decisive step is a sign or quantitative lower estimate for \(\zeta_L(0)\) in this Einstein class.

4. **Einstein-specific improvement.**  
   A plain CLR theorem treats \(q\) as arbitrary. Here \(W^+\) satisfies the Einstein Weyl equation
   \[
   \nabla^*\nabla W^+ +6W^+-6(W^+\circ W^+)_0=0
   \]
   together with \(\delta W^+=0\). A better theorem would exploit this PDE for the potential itself. The decisive step is an endpoint spectral estimate for potentials constrained by this nonlinear curvature equation.

---

## (B) Gram determinant route

Let \(\omega_1,\omega_2,\omega_3\) be an \(L^2\)-orthonormal basis of \(H^+_g\). Define the evaluation map
\[
\Omega_x:\mathbb R^3\to \Lambda_x^+,\qquad 
\Omega_x(e_a)=\omega_a(x),
\]
and
\[
G_{ab}(x)=\langle \omega_a(x),\omega_b(x)\rangle,\qquad
T=\Omega\Omega^*.
\]
Then \(G=\Omega^*\Omega\), \(T=\Omega\Omega^*\), and
\[
\det G=\det T=(\det\Omega)^2 .
\]

The determinant measures whether the three harmonic self-dual forms span \(\Lambda_x^+\). If \(\det G>0\) everywhere, then every nonzero linear combination
\[
\omega_u=\sum_a u_a\omega_a
\]
is a closed self-dual \(2\)-form with
\[
\omega_u\wedge\omega_u=|\omega_u|^2\,dV>0,
\]
hence symplectic. On a non-symplectic manifold, every projective direction \(u\in\mathbb RP^2\) must therefore have at least one zero:
\[
\exists x\in M:\quad \Omega_xu=0.
\]

### B1. Exact PDE for the Gram matrix

With \(\Delta=d^*d\) on functions and
\[
K_{ab}:=\langle\nabla\omega_a,\nabla\omega_b\rangle ,
\]
the Weitzenböck equation gives
\[
\boxed{
\frac12\Delta G_{ab}
=\langle B\omega_a,\omega_b\rangle-K_{ab}.
}
\]
Equivalently,
\[
\boxed{
\frac12\Delta G=\Omega^*B\Omega-K .
}
\]

On the open set where \(G>0\),
\[
\boxed{
\frac12\Delta\log\det G
=
\operatorname{tr}B
-\operatorname{tr}(G^{-1}K)
+\frac12\sum_i
\operatorname{tr}\!\left(G^{-1}(\nabla_iG)G^{-1}(\nabla_iG)\right).
}
\]
Since \(\operatorname{tr}B=-12\),
\[
\boxed{
\frac12\Delta\log\det G
=
-12
-\operatorname{tr}(G^{-1}K)
+\frac12|\nabla G|_G^2 .
}
\]

This is a very rigid equation: the determinant has a universal scalar-curvature forcing term \(-12\), while all geometry of the harmonic-frame degeneration is carried by the two derivative terms.

### B2. Determinant-rigidity conjecture

Define the normalized determinant
\[
\delta(x):=\frac{3(\det G)^{1/3}}{\operatorname{tr}G}\in[0,1].
\]
Here \(\delta=1\) means the three harmonic forms are pointwise isotropic in \(\Lambda^+\), while \(\delta=0\) means the evaluation map drops rank.

A useful theorem would be:

\[
\boxed{
\text{If } b_+=3 \text{ and no } H^+\text{-class is symplectic, then }
\int_M F(\delta,\operatorname{tr}G,\nabla G)\,dV
\ge c_0>0,
}
\]
where \(F\) must be chosen so that the Gram PDE converts this lower estimate into either

\[
\int |\nabla\Omega|^2\ge K_0
\]
or a pointwise-eigenvalue distribution estimate for \(T\).

The most useful quantitative target is not merely that \(\det G\) vanishes somewhere; isolated or thin vanishing can be cheap. The needed theorem is a **quantitative all-directions zero theorem**: because every \(u\in\mathbb RP^2\) has a zero of \(\omega_u\), the degeneracy set of \(\Omega\) must carry enough size, multiplicity, or winding to force energy into the Gram PDE.

### B3. Characteristic-class content of \(\det G\)

The bundle \(\Lambda^+\) has
\[
p_1(\Lambda^+)[M]=2\chi+3\tau .
\]
If \(\Omega\) were invertible everywhere, \(\Lambda^+\) would be trivial, hence \(p_1(\Lambda^+)=0\). Thus for \(\chi=8,\tau=0\),
\[
p_1(\Lambda^+)[M]=16,
\]
so the determinant degeneracy is topologically forced.

A sharp determinant proof would turn this topological charge into an analytic inequality. One possible formulation is:

\[
\boxed{
|2\chi+3\tau|
\le C\int_M \left(|\nabla P|^2\,\operatorname{tr}T+|W^+|^2\right)\,dV ,
}
\]
where
\[
P:=\frac{T}{\operatorname{tr}T}.
\]
The Chern-Weil identity alone only recovers the known curvature integral. The decisive step is a transgression formula using the harmonic frame \(\Omega\) on the level sets \(\{|\det\Omega|=\varepsilon\}\), followed by a uniform estimate as \(\varepsilon\downarrow0\).

### B4. Observable test for this route

The determinant route must distinguish two configurations:

1. **Isotropic harmonic frame:** \(G\approx \frac1V I\), \(\det G\) large on most of \(M\).  
   Then the refined Weitzenböck chain improves strongly.

2. **Three-lump frame:** each harmonic form concentrates in its own region; \(T\) is nearly rank one on most of the weighted mass.  
   Then \(\det G\approx0\) on most of the important region.

Thus the decisive theorem is a rigidity statement saying that the second configuration cannot solve the Einstein-coupled Gram PDE with small \(\int|W^+|^2\).

---

## (C) Direct tensor \(T=\sum\omega_a\otimes\omega_a\)

The tensor \(T\) is the natural object because it is basis-independent. Let
\[
u:=\operatorname{tr}T=\sum_a|\omega_a|^2,\qquad
P:=\frac{T}{u}
\]
on the set \(u>0\). Since the common zero set has measure zero, this is enough for integral identities.

### C1. Exact PDE for \(T\)

Let
\[
S:=\sum_i(\nabla_i\Omega)(\nabla_i\Omega)^*,
\]
a positive semidefinite endomorphism of \(\Lambda^+\). Then

\[
\boxed{
\nabla^*\nabla T=BT+TB-2S .
}
\]

Taking trace gives

\[
\boxed{
\frac12\Delta u=\operatorname{tr}(BT)-|\nabla\Omega|^2 .
}
\]

Integrating,
\[
\boxed{
\int|\nabla\Omega|^2=\int\operatorname{tr}(BT)
=\int\left(2\langle W^+,T\rangle-4u\right).
}
\]
Since \(\int u=3\), this is exactly the summed Weitzenböck identity
\[
\boxed{
K+12=2\int\langle W^+,T\rangle,
\qquad
K:=\int|\nabla\Omega|^2 .
}
\]

### C2. Normalized density-matrix equation

With \(T=uP\), \(\operatorname{tr}P=1\), one obtains

\[
\boxed{
\nabla^*\nabla P
-2\nabla_{\nabla\log u}P
=
BP+PB-2\operatorname{tr}(BP)P
-2u^{-1}(S-\operatorname{tr}S\,P).
}
\]

This is a drift-reaction equation on the compact convex space
\[
\mathcal D=\{P=P^*,\ P\ge0,\ \operatorname{tr}P=1\}.
\]
Rank-one \(P\) corresponds to complete alignment of all harmonic forms into one line in \(\Lambda^+\); \(P=I/3\) corresponds to perfect isotropy.

### C3. Refined Weitzenböck inequality using anisotropy

Since \(W^+\) is trace-free,
\[
\langle W^+,T\rangle
=u\langle W^+,P-I/3\rangle .
\]
Define
\[
\psi^2:=\operatorname{tr}(P-I/3)^2
=\operatorname{tr}(P^2)-\frac13,
\]
so \(0\le\psi^2\le 2/3\), with \(\psi^2=2/3\) exactly at rank one.

Then
\[
\langle W^+,T\rangle
\le u|W^+|\psi .
\]
Therefore
\[
K+12
\le
2\left(\int |W^+|^2\right)^{1/2}
\left(\int u^2\psi^2\right)^{1/2}.
\]

Set
\[
\Theta_T:=\frac{V}{9}\int u^2\psi^2\,dV .
\]
Then
\[
\boxed{
A_+:=\frac1V\int|W^+|^2
\ge
\frac{(K+12)^2}{36\Theta_T}.
}
\]

This is the cleanest \(T\)-based formulation. The crude chain corresponds to the worst value \(\psi^2=2/3\) together with no control of concentration.

### C4. Sufficient tensor theorem for \(f(3)>9\)

A direct \(T\)-rigidity theorem would be:

\[
\boxed{
\frac{(K+12)^2}{36\Theta_T}\ge 9+\varepsilon_0
}
\]
for some universal \(\varepsilon_0>0\) on every positive Einstein 4-manifold with \(b_+=3\).

Equivalently, it is enough to prove either

\[
\boxed{
\Theta_T<\frac49
}
\]
when \(K\) is small, or else prove that large \(\Theta_T\) forces \(K\) large enough to compensate:
\[
\boxed{
K>18\sqrt{\Theta_T}-12 .
}
\]

At the worst rank-one value \(\Theta_T=2/3\), this requires only
\[
K>18\sqrt{2/3}-12\approx 2.697 .
\]

So a surprisingly small universal lower estimate for \(K=\int|\nabla\Omega|^2\), provided concentration is also controlled, would close the \(22.5\%\) gap.

### C5. Bochner/Berger maximum principle signatures

At a maximum point of \(u=\operatorname{tr}T\), the trace equation gives
\[
\operatorname{tr}(BT)\ge |\nabla\Omega|^2\ge0,
\]
hence
\[
\langle W^+,P\rangle\ge 2 .
\]
Thus the harmonic-frame density must align with the part of \(W^+\) where eigenvalues reach at least the Kähler value \(2\). This generalizes the single-form Berger observation: at a maximum of \(|\omega|^2\), one has \(\alpha\ge2\).

The decisive tensor step is to turn this pointwise maximum information into an integral eigenvalue-distribution estimate for \(P\). A plausible theorem shape is:

\[
\boxed{
\int_M u^2\left(\operatorname{tr}(P^2)-\frac13\right)dV
\le
\left(\frac49-\eta\right)\frac{9}{V}
+
C\int_M|\nabla P|^2u\,dV,
}
\]
combined with a second estimate absorbing the \(|\nabla P|^2u\) term through the \(P\)-equation.

The term
\[
-2u^{-1}(S-\operatorname{tr}S\,P)
\]
in the normalized PDE is the key. If it can be shown to push \(P\) away from the rank-one stratum in an averaged sense, then the tensor route gives the desired \(b_+\)-dependent inequality.

---

## (D) Characteristic classes, spin, and index theory

### D1. Standard topological obstructions do not see \(b_+\ge2\) sharply

Positive Einstein implies positive scalar curvature, so:

- If \(M\) is spin, Lichnerowicz gives no harmonic spinors, hence
  \[
  \hat A(M)=-\frac{\tau}{8}=0.
  \]
  Thus spin positive Einstein forces \(\tau=0\), but this still allows \(b_+=b_-\ge2\).

- Hitchin-Thorpe gives
  \[
  2\chi\ge 3|\tau|,
  \]
  with equality belonging to the Ricci-flat situation. For \(\chi=8,\tau=0\), this gives no \(b_+\)-specific obstruction.

- Seiberg-Witten invariants vanish under positive scalar curvature, so they do not distinguish positive Einstein from general positive-scalar geometry in the relevant rows.

Thus a direct index-theoretic obstruction would need to be more refined than the standard Dirac, signature, or Seiberg-Witten packages.

### D2. The \(\Lambda^+\) characteristic-class route

The strongest topological input naturally tied to \(b_+\) is the SO(3) bundle \(\Lambda^+\):
\[
\boxed{
p_1(\Lambda^+)[M]=2\chi+3\tau,\qquad
w_2(\Lambda^+)=w_2(TM).
}
\]

The harmonic evaluation map
\[
\Omega:\underline{\mathbb R}^{\,b_+}\to \Lambda^+
\]
is a collection of \(b_+\) distinguished sections of \(\Lambda^+\). For \(b_+=3\), it is a square matrix of sections. Its degeneracy records the obstruction to trivializing \(\Lambda^+\).

A precise mod-2 family formulation is this. Over \(M\times\mathbb RP^2\), let \(\ell\) be the tautological line and define the universal section
\[
\mathcal W(x,[u])=\omega_u(x)
\]
of
\[
\pi_M^*\Lambda^+\otimes \ell^* .
\]
If transverse, its zero set represents the top Stiefel-Whitney class
\[
w_3(\pi_M^*\Lambda^+\otimes \ell^*)
=
w_3(\Lambda^+)+a\,w_2(\Lambda^+)+a^3,
\]
where \(a=w_1(\ell)\). Since \(a^3=0\) on \(\mathbb RP^2\), this reduces to
\[
w_3(\Lambda^+)+a\,w_2(M).
\]

For spin simply connected examples, this mod-2 class vanishes, so mod-2 data alone is too weak there. The integral class \(p_1(\Lambda^+)\), however, remains nonzero when \(2\chi+3\tau\ne0\).

### D3. Index-theoretic theorem shape that would matter

A genuinely useful index theorem would construct an elliptic operator \(\mathcal D\) whose index contains \(b_+-1\) or \(b_+\), and whose Weitzenböck formula has curvature term controlled by \(W^+\). The desired structure is:

\[
\boxed{
\mathcal D^*\mathcal D
=
\nabla^*\nabla+\mathcal R_0+\mathcal R(W^+),
}
\]
with
\[
\operatorname{ind}\mathcal D = c_1 b_+ + c_2\chi+c_3\tau ,
\]
and with a positivity estimate for \(\mathcal R_0+\mathcal R(W^+)\) unless \(\int|W^+|^2\) is large.

Possible candidates include twisted Dirac or Rarita-Schwinger type operators on spin manifolds, using
\[
\Lambda^+\cong \operatorname{Sym}^2 S^+
\]
when a spin structure exists. Harmonic self-dual forms then resemble symmetric spinor fields, and \(W^+\) acts naturally on them. The decisive step is to identify an operator whose kernel contains, or is forced by, \(H^+_g\), while its index is topological and its curvature term has the right sign structure.

### D4. Characteristic-charge plus analysis

The most promising index/topology hybrid is not a pure obstruction but a charge-energy inequality:

\[
\boxed{
\text{degeneracy charge of }\Omega
\quad\Longrightarrow\quad
\int |W^+|^2\ge 6V+\eta(b_+)V .
}
\]

Concretely, one would use:

1. \(p_1(\Lambda^+)[M]=2\chi+3\tau\);
2. the harmonic frame \(\Omega\);
3. Chern-Weil written in the \(\Omega\)-gauge away from \(\det\Omega=0\);
4. level-set transgression as \(|\det\Omega|\to0\);
5. the Gram or \(T\)-PDE to convert degeneracy charge into \(\int|W^+|^2\).

The decisive step is a quantitative transgression formula showing that the degeneracy of the harmonic frame contributes an additional positive amount beyond the ordinary Chern-Weil identity.

---

## Most concrete high-value conjectures

The cleanest formulations to pursue are:

### Conjecture 1: Einstein-CLR

For every compact positive Einstein 4-manifold with \(b_+\ge2\),
\[
\boxed{
b_+\le \mathcal C_s\,Y^{-2}\int(2\alpha-4)_+^2\,dV
}
\]
with
\[
\boxed{\mathcal C_s<18.}
\]
This immediately gives
\[
\int |W^+|^2\ge f(b_+)V,\qquad
f(3)>9.
\]

### Conjecture 2: Tensor anisotropy estimate

For \(b_+=3\), with
\[
u=\operatorname{tr}T,\qquad
P=T/u,\qquad
\Theta_T=\frac{V}{9}\int u^2\operatorname{tr}(P-I/3)^2\,dV,
\]
one has
\[
\boxed{
\frac{(K+12)^2}{36\Theta_T}>9,
\qquad
K=\int|\nabla\Omega|^2 .
}
\]
This is exactly the condition needed by the refined summed-Weitzenböck identity.

### Conjecture 3: Determinant degeneracy charge

For \(b_+=3\), the zero structure of
\[
\det G=(\det\Omega)^2
\]
carries enough \(p_1(\Lambda^+)=2\chi+3\tau\) charge to force either tensor isotropy or gradient energy:
\[
\boxed{
\det G\text{ degeneracy }+\text{ Einstein Gram PDE}
\Longrightarrow
\Theta_T<4/9
\quad\text{or}\quad
K>2.697 .
}
\]
Either alternative yields \(f(3)>9\).

### Conjecture 4: Twisted-index curvature inequality

There exists a natural Dirac-type or SO(3)-gauge elliptic complex tied to \(\Lambda^+\) whose index detects \(b_+\), and whose Weitzenböck formula gives
\[
\boxed{
b_+\le C\,Y^{-2}\int \Phi(W^+)\,dV
}
\]
with \(\Phi(W^+)\) comparable to \((2\alpha-4)_+^2\) or \(\operatorname{tr}(B_+^2)\) and with constant below the thresholds above.

Among these, the most sharply formulated and immediately testable are the Einstein-CLR inequality and the \(T\)-anisotropy identity. The determinant and characteristic-class routes are deeper because they attempt to explain why the three-lump rank-one configuration cannot be realized by an exact positive Einstein metric with small \(W^+\)-energy.