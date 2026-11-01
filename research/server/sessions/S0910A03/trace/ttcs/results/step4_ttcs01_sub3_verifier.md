# TTCS Independent Branch Record

```json
{
  "step_id": 4,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step4_weyl_profile_and_bubble_restriction.tex",
    "Sessions/S0910A03/workspace/notes/step3_boundary_near_saturation.tex"
  ]
}
```

## Task

Verify the following compactness argument chain for four-dimensional manifolds with two-sided Ricci pinching, and identify exactly where it succeeds and where it has gaps.

SETTING: M is a fixed closed connected smooth simply-connected 4-manifold. g_i is a sequence of smooth Riemannian metrics on M with δ_i := ||g_i^{-1}(Ric_{g_i} + g_i)||_{L^∞} → 0 (near negative Einstein).

CLAIM CHAIN:
1. |Ric_{g_i}| ≤ 1+δ_i ≤ 2 (uniform two-sided Ricci bound).
2. Vol(M, g_i) → V₀ > 0 (from Chern-Gauss-Bonnet and the Weyl profile analysis: see context files).
3. From (1)+(2): does Anderson's compactness theorem give C^{1,α} subsequential convergence g_i → g∞ on M? The theorem requires non-collapsing: Vol(B(p,1)) ≥ v > 0 for all p. Can this be deduced from |Ric| ≤ 2 and Vol(M) → V₀ on a FIXED manifold?
4. If non-collapsing holds: g∞ is C^{1,α} with Ric∞ = -g∞ distributionally. By DeTurck-Kazdan elliptic regularity in harmonic coordinates, g∞ is smooth. Hence g∞ is a smooth Einstein metric on M.
5. For the Seiberg-Witten spinor: the maximum principle gives |Φ|² ≤ |s| ≤ 4+4δ (uniform L^∞). The equation (-Δ + (2-u/2))u = 2|∇_AΦ|² with 2-u/2 ≥ 0 gives, by the strong maximum principle, that u = |Φ|² > 0 everywhere on the limit manifold (since ∫u² ≥ 32π²A > 0). This produces a symplectic form.
6. For the POSITIVE BRANCH (Ric ≈ +g): Myers gives diam ≤ π√3. Does this + Bishop-Gromov give non-collapsing automatically? Is there a volume lower bound for positive near-Einstein on a fixed manifold?

Precisely identify: which steps are rigorous, which need additional hypotheses, and whether non-collapsing can be obtained from the available data (Ricci bounds + volume + fixed topology + SW data).

## Output

# Scientific verification memo

## Overall result

For the \(\operatorname{Ric}\simeq-g\) sequence, the supplied analysis rigorously gives a uniform Ricci bound and, on the special Ishida–LeBrun critical family, a positive global volume limit. These facts do **not** provide a uniform lower bound for every unit ball. Even if such a unit-ball bound is added, bounded Ricci curvature alone does not give \(C^{1,\alpha}\) convergence on all of \(M\) in dimension four: curvature can concentrate and produce Ricci-flat bubbles, exactly as anticipated by Corollary B2.

With a uniform harmonic-radius or injectivity-radius estimate, the Einstein-limit argument is valid after pullback by diffeomorphisms. The proposed Seiberg–Witten strong-maximum-principle argument is not valid: its differential inequality has the wrong sign for excluding zeros, and a nowhere-zero spinor would still yield only a nondegenerate self-dual form, not automatically a closed symplectic form.

For \(\operatorname{Ric}\simeq+g\), Myers supplies a uniform diameter bound, and a separate global volume lower bound would then imply unit-ball non-collapsing by Bishop–Gromov. Myers and Bishop–Gromov do not themselves supply that global lower bound. On the manifolds carrying the positive-square monopole classes used in the supplied notes, positive scalar curvature already excludes this branch.

---

## 1. Uniform Ricci bound

Write
\[
E_i=g_i^{-1}(\operatorname{Ric}_{g_i}+g_i).
\]
Then
\[
g_i^{-1}\operatorname{Ric}_{g_i}=-I+E_i,\qquad
\|E_i\|_{\mathrm{op}}\le\delta_i.
\]
Therefore
\[
\|\operatorname{Ric}_{g_i}\|_{\mathrm{op}}\le1+\delta_i.
\]
For all sufficiently large \(i\), this is at most \(2\).

There is a norm convention issue. If \(|\operatorname{Ric}|\) denotes the Hilbert–Schmidt tensor norm rather than the endomorphism norm, then in dimension four
\[
|\operatorname{Ric}_{g_i}|_{g_i}
\le \sqrt4\,(1+\delta_i)=2(1+\delta_i)\le4.
\]
Either estimate supplies the uniform finite Ricci bound required in compactness results.

The same eigenvalue calculation gives
\[
|s_i+4|\le4\delta_i,\qquad
|\operatorname{Ric}_{g_i}^{\circ}|^2\le4\delta_i^2.
\]

---

## 2. Global volume convergence

This is rigorous for the critical family treated in the supplied Step 3 note, not for an arbitrary fixed simply-connected four-manifold.

There,
\[
S_i=\frac1{96\pi^2}\int_M s_i^2\,d\mu_i
\longrightarrow \frac{16A}{27},
\]
while \(s_i^2\to16\) uniformly. Hence
\[
S_i=\frac{16+o(1)}{96\pi^2}\operatorname{Vol}(M,g_i),
\]
and therefore
\[
\operatorname{Vol}(M,g_i)\longrightarrow
6\pi^2\frac{16A}{27}
=\frac{32\pi^2A}{9}>0.
\]

For a general fixed \(M\), Chern–Gauss–Bonnet reads
\[
8\pi^2\chi(M)
=\int_M\left(
|W|^2-\frac12|\operatorname{Ric}^{\circ}|^2+\frac{s^2}{24}
\right)d\mu .
\]
The Weyl term is not determined by the Ricci tensor, so this identity alone does not determine a positive volume limit.

On the critical family, fixed topology, bounded volume, and the Ricci estimates also yield a uniform \(L^2\) bound for the full curvature. This controls total curvature energy but does not prevent that energy from concentrating into smaller and smaller regions.

---

## 3. Global volume does not imply unit-ball non-collapsing

The data
\[
|\operatorname{Ric}_{g_i}|\le \Lambda,\qquad
\operatorname{Vol}(M,g_i)\to V_0>0
\]
do not imply
\[
\operatorname{Vol}_{g_i}B_{g_i}(p,1)\ge v>0
\quad\text{for every }p.
\]

A Ricci lower bound and a diameter upper bound would suffice. Indeed, if
\(\operatorname{Ric}\ge-3K g\) and \(\operatorname{diam}M\le D\), relative Bishop–Gromov comparison gives
\[
\operatorname{Vol}B(p,1)
\ge
\frac{V_{-K}(1)}{V_{-K}(D)}\operatorname{Vol}(M)
\]
when \(D\ge1\). In the \(\operatorname{Ric}\simeq-g\) branch, however, there is no Myers diameter estimate, and none of the supplied equations bounds the diameter.

Simple connectivity does not provide a quantitative injectivity-radius estimate. Short contractible geodesic loops, small conjugate radius, and curvature concentration are all compatible with simple connectivity.

### Contribution of the Seiberg–Witten data

Let \(u_i=|\Phi_i|^2\). The monopole equations give
\[
|F_{A_i}^{+}|^2=\frac{u_i^2}{8},
\]
and harmonic projection gives, in the conventions used in the notes,
\[
\int_M u_i^2\,d\mu_i
\ge32\pi^2(a_i^+)^2
\ge32\pi^2A.
\]
Together with
\[
u_i\le4(1+\delta_i),
\]
this recovers only a global volume lower bound:
\[
\operatorname{Vol}(M,g_i)
\ge
\frac{32\pi^2A}{16(1+\delta_i)^2}.
\]
It gives no lower bound for every ball. The spinor mass may be concentrated on part of the manifold. A uniform Harnack estimate capable of propagating that mass would itself require local Sobolev or harmonic-coordinate control, which is precisely the unresolved geometric input.

There is also a formula typo in the supplied Step 4 note: it writes
\[
|F_A^+|=|\Phi|^4/8.
\]
The correct identity is
\[
|F_A^+|^2=|\Phi|^4/8.
\]
The desired uniform bound remains valid after this correction.

---

## 4. What Anderson compactness supplies

A lower bound on all unit balls improves the situation but does not by itself produce \(C^{1,\alpha}\) convergence on every point of \(M\).

From
\[
\operatorname{Vol}B(p,1)\ge v
\]
and a Ricci lower bound, Bishop–Gromov gives lower volume ratios at all radii \(r\le1\). Together with the global volume upper bound, this also gives a diameter upper bound by packing disjoint small balls along a minimizing geodesic.

Nevertheless, in dimension four, bounded Ricci curvature and volume non-collapsing permit curvature concentration. The Chern–Gauss–Bonnet energy bound then supports convergence on the regular part, with finitely many concentration points under the standard four-dimensional small-energy regularity theory. It does not exclude a bubble tree.

This is exactly consistent with the supplied Corollary B2:

* any smooth vanishing-scale blow-up is Ricci-flat;
* the Weyl-profile estimate forces \(W_+=0\) on such a blow-up;
* \(W_-\) remains free to concentrate.

Thus Eguchi–Hanson-type hyperkähler bubbles are not removed by unit-ball non-collapsing. Their unit-scale volume ratios can stay uniformly positive while their geometric scale tends to zero.

A uniform harmonic-radius lower bound, or an injectivity-radius estimate strong enough to imply one, would remove this phenomenon and yield global \(C^{1,\alpha}\) compactness after pullback by diffeomorphisms. Raw convergence \(g_i\to g_\infty\) without diffeomorphisms is not invariantly meaningful.

---

## 5. Conditional Einstein regularity

Assume there are diffeomorphisms \(\varphi_i:M\to M\) such that
\[
\varphi_i^*g_i\to g_\infty
\]
in harmonic coordinates with uniform \(C^{1,\alpha}\) and weak \(W^{2,p}\) control for some \(p>2\). Write
\[
\operatorname{Ric}_{g_i}=-g_i+r_i,\qquad
\|r_i\|_{L^\infty}\to0.
\]

In harmonic coordinates,
\[
\operatorname{Ric}_{jk}
=
-\frac12g^{ab}\partial_a\partial_b g_{jk}
+Q_{jk}(g^{-1},\partial g).
\]
The \(W^{2,p}\) control permits passage to the weak equation
\[
\operatorname{Ric}_{g_\infty}=-g_\infty.
\]
DeTurck–Kazdan elliptic regularity then makes \(g_\infty\) smooth, indeed real analytic in harmonic coordinates.

Thus the Einstein-limit step is valid under harmonic-coordinate compactness. Mere abstract \(C^{1,\alpha}\) convergence is not by itself enough to pass Ricci curvature, since Ricci contains second derivatives.

---

## 6. The Seiberg–Witten maximum-principle step

The uniform spinor estimate is valid, with the more precise formulation
\[
u_i(x)\le \max_M(-s_i,0)\le4(1+\delta_i).
\]
It is not generally true that \(u_i(x)\le|s_i(x)|\) pointwise; the standard argument is applied at a global maximum of \(u_i\).

For the Laplacian convention used in the supplied Weitzenböck formula,
\[
0=2\Delta u+4|\nabla_A\Phi|^2+s\,u+u^2,
\]
the exact equation is
\[
\left(-\Delta-\frac{s}{2}-\frac{u}{2}\right)u
=2|\nabla_A\Phi|^2.
\]
At a smooth limit with \(s=-4\),
\[
\left(-\Delta+2-\frac{u}{2}\right)u
=2|\nabla_A\Phi|^2.
\]

The proposed strong-maximum-principle conclusion does not follow. Setting
\(\Delta_0=-\Delta=\operatorname{div}\nabla\), the equation becomes
\[
\left(\Delta_0+2-\frac{u}{2}\right)u
=2|\nabla_A\Phi|^2\ge0.
\]
At a point where \(u=0\),
\[
\Delta_0u=2|\nabla_A\Phi|^2\ge0,
\]
which is entirely compatible with \(u\ge0\) having an interior zero. The right-hand side has the sign that permits such zeros. The integral lower bound proves only that \(u\not\equiv0\); it does not imply \(u>0\) everywhere. This agrees with the Step 4 note’s own statement that pointwise non-vanishing remains unresolved.

There is a second independent issue. Even if \(\Phi\) were nowhere zero, its quadratic form \(\sigma(\Phi)\) would give a nondegenerate self-dual two-form and hence an almost-Hermitian structure, but not automatically a symplectic form. From
\[
F_A^+=i\sigma(\Phi),\qquad dF_A=0,
\]
one obtains
\[
dF_A^+=-dF_A^-,
\]
not \(dF_A^+=0\). Closedness must come from the equality characterization in LeBrun’s Proposition 3.8 or an equivalent argument.

Under genuine smooth global convergence, the Step 3 energy equalities can instead be passed to the limit, and Proposition 3.8 supplies the closed constant-length self-dual form directly. That is the scientifically valid route to the almost-Kähler structure.

---

## 7. The \(\operatorname{Ric}\simeq+g\) branch

If
\[
\|g_i^{-1}(\operatorname{Ric}_{g_i}-g_i)\|_{\mathrm{op}}
\le\delta_i<1,
\]
then
\[
\operatorname{Ric}_{g_i}\ge(1-\delta_i)g_i
=3\left(\frac{1-\delta_i}{3}\right)g_i.
\]
Myers gives
\[
\operatorname{diam}(M,g_i)
\le
\pi\sqrt{\frac{3}{1-\delta_i}}.
\]
Thus
\[
\limsup_i\operatorname{diam}(M,g_i)\le\pi\sqrt3,
\]
but the bound \(\pi\sqrt3\) is not exact for each \(i\) unless
\(\operatorname{Ric}_{g_i}\ge g_i\).

If one separately knows
\[
\operatorname{Vol}(M,g_i)\ge V_*>0,
\]
then unit-ball non-collapsing follows. For large \(i\), \(\operatorname{Ric}\ge0\), and with a uniform diameter bound \(D_*\ge1\), Bishop–Gromov gives
\[
\operatorname{Vol}B(p,1)
\ge \frac{\operatorname{Vol}(M,g_i)}{D_*^4}
\ge\frac{V_*}{D_*^4}.
\]

Myers and Bishop–Gromov do not supply \(V_*\). Bishop–Gromov gives a volume upper bound in this setting. Chern–Gauss–Bonnet also gives no general lower bound because the Weyl energy can absorb the fixed Euler term.

For the manifolds in the supplied notes carrying a monopole class \(a\) with \(a^2>0\), the positive branch is excluded more directly. When \(\delta_i<1\),
\[
s_i\ge4(1-\delta_i)>0.
\]
Integrating the Seiberg–Witten Weitzenböck formula forces
\[
\Phi_i\equiv0,\qquad F_{A_i}^+\equiv0.
\]
Hence \(a_i^+=0\), impossible when
\[
(a_i^+)^2=a^2+\|a_i^-\|^2>0.
\]
Here the Seiberg–Witten data eliminate the metrics rather than produce a volume estimate.

---

## Precise logical summary

\[
\boxed{\text{Ricci pinching}+\text{critical-family profile}
\Longrightarrow
|\operatorname{Ric}|\le\Lambda,\quad \operatorname{Vol}\to V_0>0.}
\]

The next implication is unavailable:
\[
|\operatorname{Ric}|\le\Lambda,\quad \operatorname{Vol}\ge V_*
\;\not\Longrightarrow\;
\inf_{p}\operatorname{Vol}B(p,1)>0.
\]

Even after adding unit-ball non-collapsing,
\[
\text{unit-ball non-collapsing}+\text{Ricci bound}
\]
still permits four-dimensional curvature concentration and hyperkähler bubbles.

With a uniform harmonic-radius estimate,
\[
\text{harmonic-coordinate compactness}
\Longrightarrow
g_\infty\text{ smooth and }\operatorname{Ric}_{g_\infty}=-g_\infty.
\]

The spinor integral lower bound does not remove the spinor zero set, and nowhere-zero spinor data alone do not establish closedness of the associated two-form. The equality theorem in Proposition 3.8 is the supplied mechanism that produces the required closed almost-Kähler form under smooth global convergence.