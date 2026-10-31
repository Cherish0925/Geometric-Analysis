# [SUPERSEDED — Step 65] the slice-defect invariant \(\mu_m\)

> **Correction (Step 65, Strategist-mandated).** This file's central claims are
> wrong: \(\mu_4\) is NOT unknown (it is \(\ge3(\sqrt3-1)/2\) by the session's
> Step 2 Chern–Gauss–Bonnet estimate); the Weyl tensor does NOT "absorb the
> discrepancy" (it appears on the forced-positive side); and the §7 caveat
> retracting the Euler-characteristic argument is backwards. Retained only as
> provenance. Use `step64_mu4_cascade_corrected.md` and
> `step65_mu4_correction_and_neck_fusion.md`. The bifurcation framing survives
> shifted up two dimensions: the live open invariant is \(\mu_5\), adjacent to
> the open negative-Einstein-on-tori question in \(n\ge5\); monitor, do not
> attack.

Session: S0910A03. Agent1 / Orchestrator. Phase: Explore.

## 1. The invariant

Define the slice-defect invariant
\[
\mu_m:=\inf_{\gamma\in\mathcal M(T^m),\ \operatorname{Vol}=1}
\|\operatorname{Ric}_\gamma+(m-1)\gamma\|_{C^0}.
\]

This measures how closely the \(m\)-torus can approximate a negative Einstein
metric in the \(C^0\) operator norm.

## 2. Known values

| \(m\) | \(\mu_m\) | Reason |
|-------|-----------|--------|
| 2 | \(1\) | Gauss–Bonnet: \(\int R\,dA=0\), so \(R\) cannot be uniformly close to \(-2\). |
| 3 | \(\ge 2/3\) | If \(\|\operatorname{Ric}+2g\|_{\mathrm{op}}<2/3\), all sectional curvatures are negative. Preissmann forbids \(\mathbb Z^3\) in a negatively curved closed manifold. |
| \(\ge4\) | unknown | Ricci no longer controls sectional curvature; Weyl absorbs the discrepancy. |

## 3. Why \(\mu_4\) is the bifurcation parameter

The flat-slice barrier (Step 63) blocks a neck whose slices are intrinsically
flat tori. The escape route is to use non-flat slices that are themselves
almost-Einstein. The warped product
\(g=dr^2+\cosh^2(r)\gamma\) has Ricci defect controlled by
\(\|\operatorname{Ric}_\gamma+(n-2)\gamma\|\). If \(\mu_{n-1}=0\), such slices
exist and the flat-slice barrier is bypassed.

The remaining obstruction is the matching between the flat cusp cross-sections
(required by the hyperbolic pieces) and the almost-Einstein neck interior. The
transition is governed by the Raychaudhuri equation
\(H'=-\operatorname{Ric}(\nu,\nu)-|A|^2\). If \(\mu_{n-1}=0\), one can choose
\(\gamma\) so that the required shear \(|A^0|\) is arbitrarily small, potentially
driving the matching defect to zero.

Therefore:

- **If \(\mu_4>0\)**: the 4D graph-manifold gap theorem follows via the traced
  Gauss equation coupling; the flat-slice barrier is absolute.
- **If \(\mu_4=0\)**: the 5D+ counterexample route opens; one can construct
  arbitrarily tight negative-pinched metrics on higher-dimensional graph
  manifolds (which are candidates for no-Einstein topology).

The same logic applies to \(\mu_m\) for \(m\ge5\), but \(\mu_4\) is the first
unknown case and controls the \(n=5\) problem.

## 4. Approaches to computing \(\mu_4\)

1. **Variational.** Study the \(L^2\)-norm of the Einstein operator on \(T^4\)
   near the flat metric. The linearization is the Lichnerowicz Laplacian; its
   kernel corresponds to flat deformations. The question is whether nonlinear
   terms allow a sequence with \(\|\operatorname{Ric}+3g\|_{C^0}\to0\).

2. **Kaluza–Klein / torus bundle.** Use the KK stress equations. On \(T^4\),
   \(\dim\Lambda^2=6\), \(\dim\operatorname{Sym}^2=10\). The stress equation
   \(\sum F^a\odot F^a=c\,g\) is overdetermined for a single form but may be
   solvable with several forms. A solution would give an almost-Einstein
   metric on a torus bundle, which could specialize to \(T^4\).

3. **Ricci flow.** Run Ricci flow on \(T^4\) from a non-flat initial metric.
   If the flow develops a singularity that rescales to an almost-Einstein
   soliton with \(\operatorname{Ric}\approx-3g\), that would indicate
   \(\mu_4=0\). If the flow always converges to flat, \(\mu_4>0\) is plausible.

4. **Gluing.** Attempt to glue Eguchi–Hanson or other ALE bubbles into \(T^4\)
   at points. The Brendle–Kapouleas mechanism produces almost-Einstein
   metrics on resolutions; whether the underlying smooth manifold can be \(T^4\)
   is a topological question.

## 5. Connection to the KK gauge-stress construction

The TTCS generator identified the KK mechanism as the strongest constructive
route to a higher-dimensional counterexample. For a principal torus bundle
\(T^k\to M^n\to B^m\), the Ricci tensor decomposes into base stress, fiber
stress, and Yang–Mills terms. On a flat base \(T^m\), harmonic 2-forms are
constant-coefficient. The stress equation is a quadratic map from
\(\Lambda^2(\mathbb R^m)\) to \(\operatorname{Sym}^2(\mathbb R^m)\).

- For \(m=3\) (total dimension 4 with \(k=1\)): overdetermined; the 3D slice
  lemma obstruction manifests.
- For \(m=4\) (total dimension 5 with \(k=1\), or 6 with \(k=2\)): still
  constrained, but with more fibers the system relaxes.
- For \(m\ge5\): underdetermined or balanced; one can find collections of
  closed, co-closed 2-forms whose symmetric square sum is proportional to the
  metric.

If a non-trivial bundle over \(T^m\) with exponential fundamental-group growth
(e.g. a solvmanifold or generalized graph manifold) can be equipped with such a
KK metric, it would carry \(\operatorname{Ric}\approx-(n-1)g\) while a
Bochner/Preissmann-type argument excludes exact Einstein metrics. This is the
concrete higher-dimensional counterexample candidate.

## 6. Actionable priority

**Compute or estimate \(\mu_4\).** This single invariant acts as the
bifurcation parameter for the entire Yau 26 negative branch in higher
dimensions. Simultaneously, formulate the KK stress equation as a convex
optimization problem over the period lattice of \(T^m\) to test
constructibility of counterexamples in \(n\ge5\).

## 7. Current evidence on \(\mu_4\)

The linearized Einstein operator at flat \(T^4\) has a spectral gap, but
\(\mu_4\) is a global question over all metrics. Known results:

- Anderson (1990) gives \(\varepsilon\)-regularity under Ricci bounds and
  noncollapse.
- Kapovitch–Lott (2017) shows noncollapsed almost-Ricci-flat 4-manifolds are
  K3 or flat.
- For the negative Einstein scale \(\|\operatorname{Ric}+3g\|_{C^0}\to0\), no
  analogous classification is known.

\(\mu_4>0\) is plausible but unproved. \(\mu_4=0\) would require a collapsing
sequence of \(T^4\) metrics with \(\operatorname{Ric}\to-3g\) uniformly, which
no known construction produces. The Brendle–Kapouleas mechanism produces
almost-Einstein metrics on resolutions of orbifolds, but the underlying smooth
manifold is not \(T^4\).

## 7. Caveat

The TTCS generator's claim that the 4D Euler characteristic directly obstructs
approximate Einstein metrics on \(\chi=0\) graph manifolds is **false**: the Weyl
tensor is unconstrained by Ricci pinching and absorbs the defect. The
obstruction works only via the coupled entropy–volume–LeBrun chain (Step 64).
Do not use the vacuous curvature-energy argument.
