# TTCS Independent Branch Record

```json
{
  "step_id": 10,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step8_cover_mean_transport_and_model_scope_corrections.md",
    "Sessions/S0910A03/workspace/notes/step9_maximal_function_and_weitzenbock_rotation.tex",
    "Sessions/S0910A03/workspace/notes/step9_regularity_false_and_new_direction.tex",
    "Sessions/S0910A03/workspace/scripts/compute_taub_nut_ads_curvature.py",
    "Sessions/S0910A03/workspace/scripts/analyze_taub_nut_ads_multiscale.py",
    "Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md",
    "Knowledge/objects/papers/Ricci-flow-smoothing-for-locally-collapsing-manifolds-arXiv--fd31dbed4f1f--11306ef80968/object.md"
  ]
}
```

## Task

Develop a rigorous multiscale route for the following specific problem. On a fixed critical Ishida–LeBrun four-manifold suppose Ric(g_i)+g_i tends to zero in operator L-infinity norm, the calibrated nonnegative deficit has total integral tending to zero, and a positive-volume maximal-function set has uniformly bounded averages of |Rm|^2 and vanishing averages of the deficit for every radius up to 1. We may choose, for each point, the buffered downstairs domain before taking its normal/universal cover, at a radius r0 depending only on the curvature-mean bound K. Generate the strongest plausible theorem or countermodel about existence of a fixed r0 and a cover with a noncollapsed harmonic chart. Explicitly analyze persistent rank failure across all radii, the distinction between covers of B_R(p) for different R, and how the calibrated Weyl profile can exclude real-hyperbolic or Taub–NUT-type escape. Give concrete lemmas and proof ideas, not a survey, and identify exactly which statement would advance the fixed-topology negative branch.

## Output

### Fixed-scale statement that would move the Ric \(\approx -g\) branch

The useful target is not “curvature-mean control forces noncollapse.” Taub–NUT–AdS already shows that is too weak. The right fixed-scale statement must include the calibrated deficit.

A sharp formulation is:

\[
(\star_K)\quad
\exists\, r_*(K)>0,\ v_*(K)>0
\]
such that for every sequence in the fixed critical Ishida–LeBrun setting and every positive-volume good set \(G_i\) with

\[
\mathcal M_1|\mathrm{Rm}_{g_i}|^2\le K,\qquad
\mathcal M_1F_i\le \varepsilon_i\to0
\]

on \(G_i\), there exist \(p_i\in G_i\), a scale

\[
\rho_i\in[r_*(K),1/10],
\]

and a connected normal cover

\[
\pi_i:(\widehat U_i,\hat p_i)\longrightarrow B_{10\rho_i}(p_i)
\]

such that

\[
\operatorname{Vol}_{\hat g_i} B_{\rho_i}(\hat p_i)\ge v_*(K)\rho_i^4 .
\]

Once \((\star_K)\) is known, the rest is essentially settled. The mean-transfer lemma gives, for every \(a\le \rho_i/3\),

\[
\fint_{B_a(\hat p_i)}\pi_i^*|\mathrm{Rm}_{g_i}|^2\le C K,\qquad
\fint_{B_a(\hat p_i)}\pi_i^*F_i\le C\varepsilon_i .
\]

Choose \(a=a(K)\ll r_*(K)\) so that \(CK\,V_{-1}^{(4)}(a)<\epsilon_{\mathrm{And}}\). The cover-volume lower bound and Bishop–Gromov give noncollapse at all smaller radii, hence Anderson-type harmonic-radius control on \(B_{ca}(\hat p_i)\). In harmonic coordinates,

\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=-2(\operatorname{Ric}_{g_i})_{jk}+Q(g_i^{-1},\partial g_i),
\]

and \(\|\operatorname{Ric}_{g_i}+g_i\|_{L^\infty}\to0\) gives smooth subsequential convergence on a smaller chart to an Einstein germ

\[
\operatorname{Ric}_{g_\infty}=-g_\infty .
\]

The pulled-back deficit has vanishing mean, so the limit has

\[
s_\infty=-4,\qquad |W^+_\infty|=\frac1{2\sqrt6},\qquad
\operatorname{Spec}(W^+_\infty)=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

The established projector obstruction then excludes this germ. Thus proving \((\star_K)\) would eliminate the fixed-topology Ric \(\approx -g\) sequence.

If one rescales by \(\rho_i^{-2}\), curvature-operator eigenvalues scale by \(\rho_i^2\). The limiting Einstein constant is \(-\rho_\infty^2\), with \(\rho_\infty\ge r_*(K)>0\), and the calibrated spectrum becomes

\[
\left(-\frac{\rho_\infty^2}{6},
\frac{\rho_\infty^2}{12},
\frac{\rho_\infty^2}{12}\right),
\]

so the same projector obstruction applies.

---

## 1. Why the cover radius matters

For \(R_1<R_2\), the universal cover of \(B_{R_2}(p)\), restricted to \(B_{R_1}(p)\), is not the universal cover of \(B_{R_1}(p)\). It corresponds to

\[
\ker\!\left[\pi_1(B_{R_1}(p))\to \pi_1(B_{R_2}(p))\right].
\]

Hence a short fiber loop can be unwrapped by the universal cover of \(B_{R_1}(p)\) but not by the universal cover of \(B_{R_2}(p)\). This is exactly the Taub–NUT mechanism: the short Hopf circle is visible in a small annular domain, but becomes nullhomotopic once the NUT lies inside the chosen buffer.

Thus the rank at scale \(\rho\) should be recorded as

\[
\Gamma_i(p;\rho,A,\delta)
=
\operatorname{Image}\left[
\pi_1(B_{\delta\rho}(p))
\to
\pi_1(B_{A\rho}(p))
\right],
\]

not as a single group attached to \(p\). The buffer \(A\rho\) is part of the geometry.

At a collapsed scale, suppose

\[
B_{A\rho}(p)\approx B_A(0^{k-\ell},z^\ell)\subset
\mathbb R^{k-\ell}\times Z^\ell,
\qquad \ell\le3.
\]

The collapsed codimension is \(4-k\). If

\[
\operatorname{rank}\Gamma_i(p;\rho,A,\delta)=4-k,
\]

and the residual model has noncollapsing radius bounded below, Naber–Zhang gives a harmonic chart on the local universal cover. Therefore persistent absence of a cover chart forces one of the following at every \(\rho\in[r_*(K),1]\):

1. rank drops below \(4-k\);
2. the residual \(Z^\ell\) degenerates at every candidate scale;
3. the apparent model is still four-dimensional, in which case a noncollapsed subball exists and the small-energy argument gives a chart.

Thus the only serious alternative is persistent rank loss or residual degeneration, both meaning: the point lies near a contractible-fiber core at every macroscopic scale.

---

## 2. Rank resurrection away from cores

A useful lemma to prove is the following.

### Lemma A: rank resurrection in a regular fibered annulus

Let \(B_{A\rho}(p)\) be a bounded-curvature collapsed region with an infranil fibration over a \(k\)-dimensional base on the subregion \(B_{c\rho}(p)\), and suppose no singular fiber or contractible-fiber core meets \(B_{c\rho}(p)\). Then, for \(\rho'\le c\rho\),

\[
\operatorname{rank}\operatorname{Image}\left[
\pi_1(B_{\delta\rho'}(p))\to \pi_1(B_{A'\rho'}(p))
\right]
=4-k
\]

for fixed \(A'\), \(\delta\), once the collapse is sufficiently strong.

Proof idea: over a contractible base ball the fibration is topologically

\[
D^k\times F^{4-k},
\]

with \(F\) an infranil fiber. The fiber subgroup injects into the smaller buffered region as long as the nullhomotopy cannot pass through a singular core. Thus the fibered fundamental group has full nilpotency rank.

Consequence: if rank loss persists for every \(\rho\ge r_*(K)\), then every such \(\rho\)-ball around \(p\) must meet a core where at least one collapsed direction contracts.

This is the precise replacement for the false “curvature mean gives noncollapse” idea.

---

## 3. Calibrated deficit excludes real-hyperbolic escape

On a Ric \(\approx -g\) four-manifold,

\[
s_i=-4+o(1).
\]

The scalar–Weyl square inside \(F_i\) gives

\[
(s_i+8\sqrt6\,|W_i^+|)^2.
\]

Hence, for large \(i\),

\[
|W_i^+|\le \frac1{4\sqrt6}
\quad\Longrightarrow\quad
(s_i+8\sqrt6\,|W_i^+|)^2\ge c_0>0.
\]

Therefore, for any good point \(p_i\in G_i\),

\[
\frac{\operatorname{Vol}\{x\in B_r(p_i): |W_i^+(x)|\le 1/(4\sqrt6)\}}
{\operatorname{Vol}B_r(p_i)}
\le C\,\fint_{B_r(p_i)}F_i
\to0
\]

for every \(r\le1\).

A real-hyperbolic model with \(\operatorname{Ric}=-g\) has

\[
W^+=0,\qquad s=-4,
\]

so

\[
(s+8\sqrt6|W^+|)^2=16.
\]

Thus a real-hyperbolic cusp, or any region whose volume is mostly real-hyperbolic, cannot contain a maximal-function good point. Even if such a region has maximal nilpotency rank and its universal cover is noncollapsed, it cannot be part of the calibrated good set.

---

## 4. Taub–NUT–AdS is also excluded by the calibrated profile

The curvature-mean-only countermodel is the small-\(\nu\) Taub–NUT–AdS metric

\[
g_\nu=\frac{dr^2}{F_\nu(r)}
+(r^2-\nu^2)d\Omega^2
+4\nu^2F_\nu(r)(d\psi+\cos\theta\,d\phi)^2,
\]

\[
F_\nu(r)=\frac{r-\nu}{r+\nu}
\left(1+\frac{(r-\nu)(r+3\nu)}{3}\right),
\qquad r\ge\nu,
\]

with

\[
\operatorname{Ric}_{g_\nu}=-g_\nu .
\]

The exact Weyl invariant is

\[
|W|^2
=
\frac{32\nu^2(4\nu^2-3)^2}{3(r+\nu)^6}.
\]

For fixed physical \(r>0\),

\[
|W|^2\to0,
\]

so the scalar–Weyl part of \(F\) tends to \(16\). Near the NUT scale \(r=\nu x\),

\[
|W|^2\sim \nu^{-4}\cdot \frac{96}{(x+1)^6},
\]

so the Weyl magnitude is far above the calibrated value. The equation

\[
|W^+|^2=\frac1{24}
\]

can only hold, in the favorable orientation, around

\[
r_\nu\sim 2304^{1/6}\nu^{1/3}.
\]

Moreover the good radial shell has relative thickness \(O(\eta)\) if the allowed Weyl error is \(O(\eta)\). A ball of radius comparable to \(r_\nu\) contains a definite portion where the scalar–Weyl square is bounded below. A ball at fixed physical radius is mostly in the \(W\approx0\) zone. A ball at NUT scale sees \(|W|\gg1\).

Thus no point in the Taub–NUT–AdS family satisfies

\[
\mathcal M_1F_\nu\to0.
\]

The same mechanism rules out any Taub–NUT-type rank-loss cap whose regular annulus has the usual NUT profile: the short circle can be contractible in a large buffer, but the calibrated deficit sees the cap.

This is the decisive difference between:

\[
\fint|\mathrm{Rm}|^2\le K
\]

and

\[
\fint|\mathrm{Rm}|^2\le K,\qquad \fint F\to0.
\]

The first allows Taub–NUT–AdS; the second does not.

---

## 5. What persistent rank loss would have to look like

If \((\star_K)\) is not true, then after passing to good points \(p_i\), for every dyadic scale

\[
\rho_j=2^{-j},\qquad r_*(K)\le\rho_j\le1,
\]

and every useful buffer \(A\rho_j\), the collapsed fiber rank is smaller than the collapsed codimension, or the residual model degenerates further.

By Lemma A, this means \(p_i\) is \(O(\rho_j)\)-close to a core where some collapsed direction contracts, for every such \(j\). Therefore the good set would be covered by points lying near multiscale contractible-fiber cores.

The known escape models do not work:

- real-hyperbolic collars have \(W^+=0\);
- Taub–NUT collars have \(W^+\) too small on fixed annuli, too large near the NUT, and calibrated only on a thin transition shell of vanishing volume;
- ordinary rank-\(\ge2\) flat torus collapse is incompatible with the near-harmonic self-dual form structure: two independent definite self-dual forms force near-parallelism, while the Weitzenböck identity gives \(O(1)\) gradient energy.

Thus a genuine countermodel would need an exotic calibrated rank-loss cap, not a standard Einstein cusp or NUT cap.

---

## 6. Rank-one reduction: the static equations

The most concrete remaining model is rank-one collapse. Write a local \(S^1\)-collapsed metric in Kaluza–Klein form

\[
g_i=g_{B,i}+\ell_i^2\phi_i^2(d\psi+A_i)^2,
\qquad \ell_i\to0.
\]

In the bounded-curvature regular region, the leading Einstein equations reduce to the static system on the three-dimensional base:

\[
\operatorname{Ric}_{B}-\phi^{-1}\nabla^2\phi=-g_B,
\qquad
\Delta_B\phi=\phi.
\tag{S}
\]

If \(e_1,e_2,e_3\) diagonalize \(\operatorname{Ric}_B\) with eigenvalues \(r_1,r_2,r_3\), then the four-dimensional self-dual Weyl eigenvalues in the collapsed limit are

\[
w_i=-\frac23-r_i,
\qquad r_1+r_2+r_3=-2.
\]

The calibrated spectrum

\[
\left(-\frac16,\frac1{12},\frac1{12}\right)
\]

therefore forces

\[
\operatorname{Spec}(\operatorname{Ric}_B)
=
\left(-\frac12,-\frac34,-\frac34\right).
\tag{C}
\]

Equivalently,

\[
\nabla^2\phi
=
\phi(\operatorname{Ric}_B+g_B)
\]

has eigenvalues

\[
\left(\frac12\phi,\frac14\phi,\frac14\phi\right).
\]

So a rank-one calibrated regular region must solve the overdetermined system

\[
(S)+(C).
\tag{SC}
\]

This is a precise reduced problem. A theorem excluding smooth or NUT-ended solutions of \((SC)\) would eliminate the rank-one persistent-loss mechanism.

A plausible local obstruction is:

### Lemma B: no calibrated static NUT cap

There is no pointed rank-one Einstein collapse with a smooth contractible \(S^1\)-fiber core, bounded normalized curvature, and \(F\to0\) on a definite-volume annulus.

Proof route:

1. Smooth collapse of a circle orbit at an isolated core imposes a Hopf-type tangent model.
2. The orbit-space tangent is the cone coming from the Hopf quotient.
3. The leading curvature profile near such a core is isotropic in the base directions; in the Taub–NUT–AdS model this gives the hyperbolic-base profile and \(W^+\to0\) away from the thin transition shell.
4. The calibrated static equations require anisotropic base Ricci eigenvalues \((-1/2,-3/4,-3/4)\) on a full-volume region.
5. These two asymptotics cannot match across a bounded-curvature cap without producing a definite \(F\)-mean on some annulus.

This lemma is much more targeted than a general collapsed regularity theorem and directly attacks the only remaining rank-one escape.

---

## 7. Higher-rank collapse and topological charge

For rank \(\ge2\), there is an independent form-theoretic obstruction.

At the calibrated Einstein spectrum, harmonic self-dual forms have

\[
\int|\nabla H|^2
\ge c\int |H|^2,
\]

with \(c=1\) on the simple eigenspace and \(c=3/2\) on the double eigenspace in the \(\lambda=-1\) normalization. Thus the self-dual eigenline rotates at \(O(1)\) rate.

In a flat torus collapse of rank \(2\) or \(3\), two or three locally definite self-dual forms become basic. Closedness plus near-constant Gram matrix then forces their covariant derivatives to vanish in the collapse limit, contradicting the Weitzenböck rotation energy. Hence flat regular collapse of rank at least \(2\) is not a viable carrier of the good set.

The remaining higher-rank possibilities must involve nil-twist, singular fibers, or non-basic self-dual connection curvature. These are exactly the places where

\[
p_1(\Lambda^2_+)=2\chi+3\tau
\]

can localize. On a regular collapse over a base of dimension at most \(3\), if the self-dual connection is pulled back from the base, then

\[
\Omega_E\wedge\Omega_E=0.
\]

Since the critical Ishida–LeBrun manifold has

\[
\int p_1(\Lambda^2_+)=\frac{2A}{3}>0,
\]

a positive amount of self-dual connection curvature must sit in non-basic or singular regions. A quantitative charge-packing lemma would say that such regions cannot be \(r_*(K)\)-dense in the positive-volume good set while \(\mathcal M_1F_i\to0\) and \(\mathcal M_1|\mathrm{Rm}|^2\le K\).

A useful formulation is:

### Lemma C: calibrated charge-packing

For every \(K\) there exist \(r_*(K),\eta_*(K)>0\) such that any \(r_*\)-separated family of rank-loss cores meeting the calibrated good set carries either

\[
\int |\mathrm{Rm}|^2\ge \eta_*
\]

or

\[
\fint_{B_{c r_*}}F\ge \eta_*.
\]

Since the total \(\int|\mathrm{Rm}|^2\) is topologically bounded and \(F\)-means vanish on \(G_i\), such cores cannot be dense around a fixed positive-volume good set.

---

## 8. The decisive multiscale dichotomy

The whole problem can be compressed to the following dichotomy.

For \(p_i\in G_i\), either:

### Case I: rank recovers at some fixed scale

There exists \(\rho_i\in[r_*(K),1/10]\) and a buffer \(B_{10\rho_i}(p_i)\) such that the relevant fibered group has maximal rank. Then Naber–Zhang gives a noncollapsed local cover; mean transfer gives small \(F\); harmonic compactness gives the calibrated Einstein germ; projector obstruction excludes it.

### Case II: rank loss persists at every fixed scale

Then every \(\rho\in[r_*(K),1]\) sees a nearby contractible-fiber core. Real-hyperbolic and Taub–NUT-type cores force a definite scalar–Weyl deficit on some ball centered at \(p_i\), contradicting \(p_i\in G_i\). Flat higher-rank collapse conflicts with the self-dual form rotation. The only possible survivor is an exotic calibrated rank-loss cap satisfying the static rank-one system \((SC)\) or a nil-twisted analogue carrying the required \(p_1(\Lambda^2_+)\) charge without producing \(F\)-mass.

Thus the exact statement that would advance the fixed-topology Ric \(\approx -g\) branch is \((\star_K)\), or equivalently:

\[
\boxed{
\text{A positive-volume calibrated good set cannot be covered at every fixed scale by rank-loss cores.}
}
\]

A countermodel would need to exhibit a closed sequence whose good set is supported on exotic calibrated rank-loss caps with \(F\to0\) at every centered scale. Real-hyperbolic cusps and Taub–NUT–AdS caps do not have the required Weyl profile.