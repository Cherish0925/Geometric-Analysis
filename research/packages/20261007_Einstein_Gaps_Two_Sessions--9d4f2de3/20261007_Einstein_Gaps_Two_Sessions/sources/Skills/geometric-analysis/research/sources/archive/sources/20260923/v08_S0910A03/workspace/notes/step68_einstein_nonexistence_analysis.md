# Step 68: Einstein nonexistence on E_D — harmonic-map approach and interface with fibered rigidity

Session: S0910A03. Agent2 / Constructor. Phase: Explore.

## The central open question

The surface bundle E_D (Dehn-twist, p,q ≥ 2) has δ → 0 on a fixed
manifold (manuscript Ch. 6). Einstein nonexistence would immediately give
a negative-branch Yau 26 counterexample in dimension 4. All standard
tools fail; this note explores what additional mechanism could work.

## Constraints on a hypothetical Einstein metric

If g is Einstein on E_D with Ric = λg:

1. **λ < 0** forced: λ > 0 excluded by Bonnet–Myers (π₁ infinite);
   λ = 0 excluded by Berger holonomy classification + b₁ = 2p+2q−1 > 4
   (no hyper-Kähler, no flat with b₁ > 4).

2. **Volume is not topologically fixed.** For an Einstein four-metric,
   \(8\pi^2\chi=\int(|W|^2+\tfrac23\lambda^2)\,dV\).  Thus after
   normalizing \(\lambda=-1\), one only gets \(\operatorname{Vol}\le
   12\pi^2\chi=3V_0\); the monopole lower endpoint is strict, so a
   hypothetical metric has \(V_0<\operatorname{Vol}<3V_0\).  The
   approximating metrics have volume exactly \(V_0\), but an unrelated
   Einstein output need not.

3. **Full curvature energy**: every Einstein metric attains
   \(\int|\operatorname{Rm}|^2=32\pi^2\chi=8V_0\) (raw four-index norm),
   independent of its normalized volume. This is why full-energy attainment,
   unlike Ricci-energy attainment, remains equivalent to Einstein existence.

4. **No sec ≤ 0** (Kapovich–Leeb): the Einstein metric must have some
   positive sectional curvatures.

5. **No complex structure on any finite cover** (Kotschick).

## Harmonic-map approach: a potential exclusion mechanism

### Setup
The fiber projection π: E_D → Σ_q defines a homotopy class of maps.
For any Riemannian metric g on E_D and any metric h on Σ_q, there
exists an energy-minimizing harmonic map f: (E_D, g) → (Σ_q, h) in this
homotopy class (Eells–Sampson, since target has non-positive curvature).

### Key chain of implications (if certain conditions hold)
1. f submersion (no critical points) → fibers are closed surfaces of genus p
2. fibers minimal + horizontal conformal → f is harmonic morphism
3. Wood 1992 (for Einstein source): harmonic morphism to surface
   → integrable complex structure on E_D
4. But Kotschick: no complex structure on E_D → **CONTRADICTION**

### What actually holds
- Step 1: NOT guaranteed. Energy-minimizing harmonic maps to surfaces
  CAN have critical points (branch points in complex language).
  For a map homotopic to a fiber bundle projection, the generic fiber
  is a closed surface of the right genus, but the map may degenerate at
  isolated points.

- Step 2: Even if f is a submersion, the fiber minimality and horizontal
  conformality are strong conditions that don't follow from harmonicity.
  For an arbitrary Einstein metric g, the harmonic representative of the
  projection class need not respect the original fiber structure at all.

- Step 3: The full Wood theorem requires "harmonic morphism" not just
  "harmonic map + submersion". A harmonic map is a harmonic morphism
  iff additionally horizontally conformal.

### What could make this work
**Conjecture**: For any Einstein metric g on E_D with λ = −1, the
energy-minimizing harmonic map f: (E_D, g) → (Σ_q, hyp) is a harmonic
morphism (hence a submersion, minimal fibers, horizontally conformal).

This would be a strong statement. Evidence for/against:

**For**: The aspherical structure K(G,1) means the homotopy type completely
determines the manifold. The fiber-base structure is reflected in π₁.
An Einstein metric can't ignore this structure entirely.

**Against**: A general Riemannian metric on E_D can rotate the "fiber"
directions arbitrarily. The harmonic map might have energy minimized by
configurations far from submersion.

### A weaker approach
Instead of showing f is a harmonic morphism, we could try:

If f is a submersion → the fibered Einstein equations (Ch. 8) apply →
two rigidity theorems exclude adapted Einstein → f must have critical points.

If f has critical points → study the critical set. For a map between
4-manifold and surface, the critical set is generically a surface.
Could the topology of E_D force a contradiction with having an Einstein
metric and critical-point harmonic representative?

**This requires new analysis of the harmonic map critical set interacting
with the Einstein equation.**

## Entropy-based approach: why it fails for E_D

Kotschick's bound A ≥ B (where A = χ − (3/2)|τ|, B = h⁴Vol/(108π²)):
- A(E_D) = 4(p−1)(q−1) (since τ = 0)
- B(E_D) ≈ 16V₀/(108π²) = 16·16π²(p−1)(q−1)/(108π²)
  = 256(p−1)(q−1)/108 ≈ 2.37(p−1)(q−1)

Wait, this gives B ≈ 2.37·A/4. For A ≈ 4(p−1)(q−1) and B ≈ 2.37(p−1)(q−1):
A − B ≈ (4 − 2.37)(p−1)(q−1) > 0. So A > B always, no contradiction.

The entropy bound cannot exclude Einstein on E_D because E_D is "too
product-like" — its entropy is less than the hyperbolic rate.

For M_d = X_d # Q (hyperbolic #Q): A = c_d − t_Q, B = c_d, giving A < B.
This works because the hyperbolic piece dominates the entropy.

**Correction.** A high-genus surface bundle over a high-genus surface has
positive simplicial volume; bounded Euler-class pairings give positivity.
Since \(E_D\) is aspherical, its classifying map certainly does not factor
through the base in the way previously asserted.  The manuscript's actual
bounds leave numerical slack: \(\lambda(E_D)^4\le36\pi^2c\) and
\((2/3)\|E_D\|\le\lambda(E_D)^4\), so the standard Einstein entropy and
simplicial-volume inequalities do not contradict existence.  The route fails
because the available constants are too weak, not because simplicial volume
vanishes.

## Graph manifold construction: the earlier volume inference is withdrawn

The manuscript's \(\delta>\operatorname{csch}^2(R/\sqrt3)\) estimate is for
boundaries of deleted hyperbolic **balls** in the \(\operatorname{Ric}=-g\)
normalization; those spheres grow with \(R\).  It is not a cusp-depth area
estimate.  For flat cusp interfaces the outward mean curvature is independent
of truncation depth, and in the \(\operatorname{Ric}=-3g\) normalization the
finite-boundary theorem gives only the length cost
\(L\ge(2/k)\operatorname{artanh}(1/k)\),
\(k=\sqrt{1+\delta/3}\).

No favorable neck-volume conclusion follows.  In an expanding layer
\(g=dr^2+f(r)^2\gamma_r\), volume is
\(\int f^3\operatorname{Vol}(\gamma_r)dr\), while intrinsic curvature enters
as \(f^{-2}\operatorname{Ric}_{\gamma_r}\).  Slow variation suppresses normal
terms but shrinking \(f\) amplifies any nonflat slice curvature.  A fixed
normalized Einstein core also cannot be homothetically shrunk while preserving
\(\operatorname{Ric}\simeq-3g\).  The live question is a coupled anisotropic
compensation from the Koiso germ into the expanding cusp regime.

## Summary of the research state

| Route | Has δ→0 | Has no-Einstein | Difficulty |
|-------|---------|-----------------|------------|
| Surface bundle E_D | ✓ (Θ(ε³)) | OPEN | All standard tools fail |
| Extended graph manifold | OPEN | ✓ (Di Cerbo) | Global construction |
| M_d = X_d # Q | OPEN | ✓ (Kotschick) | Construction (handle + surgery) |

The hardest questions are:
1. Does E_D carry an Einstein metric?
2. Can δ → 0 be achieved on an extended graph manifold?
3. Is there a third class of manifolds combining both properties?

Files referenced: 20260912.tex (Chs. 6, 8, 10), step68_manuscript_absorption.md
