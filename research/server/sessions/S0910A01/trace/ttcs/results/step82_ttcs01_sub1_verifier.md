# TTCS Independent Branch Record

```json
{
  "step_id": 82,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step82_integrability_connection_and_existence_analysis.md",
    "Sessions/S0910A01/workspace/notes/step80_J_equivariant_all_order_reduction.md",
    "Sessions/S0910A01/workspace/notes/step81_L_exchange_and_radial_ledger.md",
    "Sessions/S0910A01/workspace/notes/step77_mixed_row_obstruction_repair.md",
    "Sessions/S0910A01/trace/ttcs/results/step80_ttcs01_verifier1_integration.md",
    "Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md",
    "Knowledge/objects/papers/Integrability-of-Einstein-deformations-and-desingularizations--8e63541ce32f--b5af64ba3e90/object.md"
  ]
}
```

## Task

Verify the following existence claim for Einstein desingularization of (S²×S²)/⟨(r_π,r_π)⟩:

CLAIM: Within the A+J+L equivariant family (insertion direction ω₂ fixed by J, equal scales by A+L symmetry, diagonal chirality pattern), ALL finite-dimensional obstructions tracked by Ozuch's O(t^{5/2}) error estimate vanish:
- λ_k = 0 for k=1,2,3 at each node (in-kernel insertion, ζ ∈ ker R⁺)
- μ₁ = 0 at each node (rank-one determinant: det R|_{ζ⊥} = 0)
- μ₂ = μ₃ = 0 at each node (J-parity: J acts as diag(-1,+1,-1) on adapted basis)
- ν_l = 0 (product orbifold has O(g_o) = {0}, no orbifold deformation parameters)

The combined Ozuch equation t·λ + t²·μ = O(t^{5/2}) becomes 0 = O(t^{5/2}), trivially satisfied.

CONSEQUENCE CLAIM: Under these conditions, Biquard's IFT ([Biq13] Theorem 14.3) produces an actual Einstein metric on the smooth resolution #₃(S²×S²) for sufficiently small t > 0.

SPECIFIC QUESTIONS TO CHECK:
1. Is the obstruction vanishing complete, or are there additional finite-dimensional conditions beyond λ, μ, ν that Ozuch tracks?
2. Does Biquard's IFT actually handle the case when ALL obstructions vanish identically (not just when they can be solved by parameter adjustment)? Is the map F(φ,v,t) = 0 being identically satisfied a degenerate or non-degenerate situation for the IFT?
3. The operator P on the product orbifold has a negative mode g₁-g₂ with eigenvalue -Λ. On the approximate desingularization, this mode survives (modified by O(t²)). Does this prevent the IFT contraction from closing? The eigenvalue is bounded away from zero, so the inverse norm should be O(1).
4. The orbifold deformation space O(g_o): is it truly trivial for (S²×S²)/Z₂? The round product has no TT kernel for P, but are there non-TT modes in O(g_o)?
5. The integrability condition: Ozuch requires 'integrable Einstein deformations' of both the orbifold and the ALE space. For the EH metric, are all deformations integrable? For the product orbifold with O(g_o) = {0}, is integrability vacuously satisfied?
6. The topology: with diagonal chirality (2 nodes +, 2 nodes -), the resolution has χ = 8, τ = 0, giving #₃(S²×S²). Is this correct?
7. Is there precedent in the literature for Einstein metrics on #₃(S²×S²)? This would be a new result if correct.

## Output

# Scientific verification memo

## Main finding

The displayed low-order coefficients satisfy the proposed cancellations, except that the stated reason for \(\nu_l=0\) is incorrect. More importantly, these cancellations do not make the complete Lyapunov–Schmidt obstruction map vanish.

The strongest result supported by the supplied material is:

> In the \(A+J+L\)-equivariant family, all transverse bubble projections and all global orbifold-kernel projections vanish by parity, while the known second-order radial coefficient vanishes algebraically. One \(J\)-even radial equation remains at higher order.

Consequently, neither Proposition 2.19 of Ozuch nor Biquard’s complement-space implicit-function argument currently produces an Einstein metric on \(\#_3(S^2\times S^2)\).

---

## 1. What vanishes, and what remains

For the product metric with \(\operatorname{Ric}=\Lambda g\),
\[
R^+=R^-=\operatorname{diag}(\Lambda,0,0).
\]
With insertion direction \(\phi=\omega_2\), the adapted basis is
\[
(\phi_{(1)},\phi_{(2)},\phi_{(3)})
=(\omega_2,\omega_1,\omega_3).
\]

The verified coefficient ledger is:

| Component | Status | Reason |
|---|---:|---|
| \(\lambda_1,\lambda_2,\lambda_3\) | \(0\) | \(R^\pm\omega_2=0\) |
| \(\mu_1\) | \(0\) | Ozuch Lemma 2.14 gives \(C\det(R^\pm|_{\omega_2^\perp})=0\) |
| transverse \(\mu_2,\mu_3\) | \(0\) | \(J\)-odd projections of a \(J\)-even residual |
| all higher transverse projections | \(0\) | same exact \(J\)-parity argument |
| global \(\nu_l\) | \(0\) in the \(A\)-invariant construction | all global kernel tensors are \(A\)-odd |
| higher radial projection | unresolved | radial EH kernel is \(J\)-even and transported by \(L\) with sign \(+1\) |

The Step 80 parity calculation is sound: \(J\) acts on both \(\Lambda^+\) and \(\Lambda^-\) as
\[
\operatorname{diag}(-1,+1,-1),
\]
and the EH insertion direction \(\omega_2\) is fixed. Once charts, cutoffs, reference metric, and complement correction are chosen equivariantly, the full projected residual onto \(\omega_1,\omega_3\) vanishes exactly, not merely through order \(t^2\).

The radial direction \(\omega_2\), however, is even. Step 81 also finds that \(L\) transports its leading kernel tensor with sign \(+1\). Thus \(L\) relates the two orbit equations but does not annihilate them:
\[
F_2(t_1,t_2)=F_1(t_2,t_1).
\]
At the first candidate interaction layer,
\[
F_i(t_1,t_2)
=t_i\sum_j B_{ij}t_j^2+\cdots,
\qquad
B=\begin{pmatrix}a&b\\ b&a\end{pmatrix}.
\]
On the \(L\)-fixed equal-scale line,
\[
F_1(t,t)=F_2(t,t)=(a+b)t^3+\cdots .
\]
Neither \(A\), \(J\), nor \(L\) forces \(a+b=0\). Ozuch Remark 2.11 also permits logarithmic terms at refined orders, so the first surviving expression could involve \(t^3\log t\).

### Logical direction of Proposition 2.19

Ozuch Proposition 2.19 starts by assuming that an exact nearby Einstein metric exists and then derives
\[
t_j\lambda_k^j+t_j^2\mu_k^j
=O(t_{\max}^{5/2}),
\qquad
\nu_l=O(t_{\max}^{5/2}).
\]
It is a necessary asymptotic relation, not an existence theorem.

After \(\lambda=\mu=0\), the formula
\[
0=O(t^{5/2})
\]
contains no information about the complete radial map. For example,
\[
F(t)=t^3
\]
satisfies \(F(t)=O(t^{5/2})\) as \(t\to0\), yet it has no nonzero small root. This is exactly why the order-three response identified in Steps 77 and 81 is invisible to the stated estimate.

There are no extra independent finite-dimensional directions in Ozuch Definition 2.16 beyond the EH parameter directions and the orbifold kernel directions. The missing substance consists of higher coefficients in the same surviving radial direction.

---

## 2. The product orbifold kernel is not trivial

The statement
\[
\mathbf O(g_o)=\{0\}
\]
is false for Ozuch’s definition
\[
\mathbf O(g_o)=\ker_{L^2}
\left(\frac12\nabla^*\nabla-\mathring R\right)
\]
on all symmetric two-tensors.

Let \(u_1,u_2\) be the axial degree-one spherical harmonics on the two factors. They descend through the half-turn quotient and satisfy
\[
\Delta u_i=2\Lambda u_i.
\]
Since each factor metric is parallel and
\[
\mathring R(u_i g_j)=\Lambda u_i g_j,
\]
one has
\[
P(u_i g_j)
=\frac12(2\Lambda)u_i g_j-\Lambda u_i g_j=0.
\]
Thus the full kernel contains, and Step 77 identifies it as, the four-dimensional space
\[
\operatorname{span}
\{u_1g_1,u_1g_2,u_2g_1,u_2g_2\}.
\]

This does not contradict the absence of a TT kernel. The tensor \(g_1-g_2\) is also not in this kernel:
\[
P(g_1-g_2)=-\Lambda(g_1-g_2).
\]

### Why \(\nu_l\) nevertheless vanishes equivariantly

Under the simultaneous antipodal map \(A\),
\[
A^*u_i=-u_i,\qquad A^*g_j=g_j.
\]
Hence every element of \(\mathbf O(g_o)\) is \(A\)-odd. For an \(A\)-even residual \(E\),
\[
\langle E,v\rangle
=\langle A^*E,A^*v\rangle
=-\langle E,v\rangle,
\]
so every global projection is zero.

Therefore the numerical conclusion \(\nu_l=0\) can be retained, but its mechanism is \(A\)-parity, not triviality of \(\mathbf O(g_o)\).

---

## 3. Integrability assumptions

### Eguchi–Hanson

The EH side satisfies the required integrability. Ozuch Proposition 1.16 and Remark 1.20 exhibit the exact Ricci-flat family
\[
\zeta\longmapsto \mathrm{eh}_{\zeta^\pm},
\]
whose three parameter derivatives span the \(L^2\) kernel. Thus all three EH kernel directions arise from actual Ricci-flat ALE metrics.

### Product orbifold

For the full four-dimensional kernel above, integrability is not vacuous and does not hold automatically.

Two directions are pure diffeomorphism directions:
\[
u_1g_1=-\frac1{2\Lambda}\mathcal L_{\nabla u_1}g,
\qquad
u_2g_2=-\frac1{2\Lambda}\mathcal L_{\nabla u_2}g.
\]
The cross directions are different. Step 77 computes
\[
B(a\,u_1g_1+b\,u_1g_2)=b\,du_1,
\]
and similarly for \(u_2\). Moreover \(u_1g_2\) cannot be a Lie derivative: if
\(\mathcal L_Xg=u_1g_2\), then for every fixed point of the first sphere the second-factor component \(X_2\) would satisfy
\[
\mathcal L_{X_2}g_2=u_1g_2.
\]
Taking the second-factor trace gives a constant nonzero divergence on a compact \(S^2\), contradicting the integral of a divergence.

Together with the supplied fact that the TT kernel is zero, this shows that the full kernel is not an integrable Einstein deformation space in Ozuch Definition 1.10.

In the \(A\)-invariant tensor space, all four kernel modes disappear, so integrability becomes vacuous there. An \(A\)-restricted version of the elliptic gluing argument is mathematically natural because the operator commutes with a finite group, but that reformulation is not the same as invoking the published full-space hypothesis verbatim.

Ozuch 2021 Proposition A.2 does not repair this point or the radial equation. Proposition A.2 concerns the self-interaction of a quadratic Einstein jet \(H_2\). The EH desingularization obstruction pairs the orbifold jet \(H_2\) with the ALE asymptotic \(H^4\). Section 4 of that paper also expressly states that it does not recover the higher-order data of Ozuch 2020.

---

## 4. What the implicit-function argument actually gives

The gluing analysis separates the equation into
\[
\Pi^\perp\Phi(g^A+x)=0,
\qquad
\Pi\Phi(g^A+x)=0,
\]
where \(\Pi\) projects onto the approximate obstruction space.

Uniform invertibility on the complement produces \(x=x(t)\) solving the first equation. The second equation is the reduced finite-dimensional map
\[
\mathcal F(t)=\Pi\Phi(g^A+x(t)).
\]
An exact Einstein metric requires
\[
\mathcal F(t)=0
\]
exactly.

If symmetry made the complete function \(\mathcal F\) identically zero, no derivative in the scale parameter would be needed; the complement-space implicit-function argument would then yield exact metrics for all sufficiently small scales. That is not the present situation. Only its first displayed coefficients vanish, while its radial component is even under every imposed symmetry.

At \(t=0\), the radial map has vanishing low derivatives, so ordinary parameter-space IFT does not produce a branch with \(t>0\). A coefficient such as \(a+b\), an exact identity annihilating the radial projection, or another finite-dimensional balancing mechanism is required.

The supplied Ozuch text uses Biquard Section 14 for local estimates, while repeatedly distinguishing Biquard’s asymptotically hyperbolic construction from the compact problem. No supplied theorem states that \(\lambda=\mu=\nu=0\) through the displayed orders yields a compact exact Einstein desingularization.

---

## 5. The \(g_1-g_2\) eigenmode

Because \(g_1-g_2\) is parallel,
\[
P(g_1-g_2)=-\Lambda(g_1-g_2).
\]
A corresponding mode on the glued metric should have eigenvalue
\[
-\Lambda+o(1),
\]
hence absolute value at least \(\Lambda/2\) for small \(t\). Its inverse contribution is therefore bounded.

Sign-indefiniteness of \(P\) does not obstruct an implicit-function argument; bijectivity on the complement is what matters. The full weighted inverse constant depends on all complement modes, not solely on \(g_1-g_2\), so a uniform weighted estimate still belongs to the gluing analysis. This particular eigenmode does not create a small eigenvalue or an extra finite-dimensional equation.

---

## 6. Topology

The Euler calculation is consistent:
\[
\chi\!\left((S^2\times S^2)/\mathbb Z_2\right)
=\frac{\chi(S^2\times S^2)+\chi(\mathrm{Fix})}{2}
=\frac{4+4}{2}=4.
\]
Resolving four \(A_1\) points replaces each point by an exceptional \(S^2\), increasing \(\chi\) by one:
\[
\chi(M)=8.
\]
With two chiralities of each sign,
\[
\tau(M)=0.
\]

However, \((\chi,\tau)=(8,0)\) alone does not distinguish
\[
3\mathbb{CP}^2\#3\overline{\mathbb{CP}}^{\,2}
\quad\text{from}\quad
\#_3(S^2\times S^2).
\]
Their intersection forms are respectively odd and even.

For the diagonal pattern
\[
\epsilon(NN)=\epsilon(SS)=+1,\qquad
\epsilon(NS)=\epsilon(SN)=-1,
\]
the two positive nodes occupy opposite corners. The topology table in Step 77 assigns this opposite-corner row the even form \(3H\), hence the standard smooth type
\[
\#_3(S^2\times S^2).
\]
The adjacent two-positive row instead gives
\(3\mathbb{CP}^2\#3\overline{\mathbb{CP}}^{\,2}\). These two manifolds are not equivalent by “wall-crossing.”

---

## 7. Literature status

None of the supplied papers constructs an Einstein metric on
\(\#_3(S^2\times S^2)\). They provide:

- same-chirality hyperkähler Kummer constructions;
- Einstein metrics modulo obstruction;
- necessary desingularization relations;
- asymptotically hyperbolic examples;
- higher-order obstruction calculations.

Thus the supplied references do not establish precedent for such a compact Einstein metric. A completed radial calculation plus complement estimate would yield a result not contained in these sources, but a literature-wide novelty statement requires bibliographic evidence beyond the files provided.

## Direct answers

1. **Independent finite directions:** no additional ones beyond bubble and orbifold-kernel directions in Ozuch’s setup; higher radial terms in an already present direction remain.
2. **IFT:** it works if the complete reduced map is identically zero. Vanishing of \(\lambda,\mu,\nu\) through the displayed orders does not establish that identity.
3. **Mode \(g_1-g_2\):** it stays uniformly separated from zero and does not by itself obstruct inversion.
4. **Orbifold kernel:** not trivial; it is four-dimensional in the supplied computation. Its projections vanish in the \(A\)-invariant sector by parity.
5. **Integrability:** EH yes; full product-orbifold kernel no. The \(A\)-invariant sector has no global kernel.
6. **Topology:** the diagonal opposite-corner pattern gives \(\#_3(S^2\times S^2)\) using the even intersection form; \(\chi\) and \(\tau\) alone do not determine this.
7. **Precedent:** none appears in the supplied literature; the existence theorem itself is not presently obtained.