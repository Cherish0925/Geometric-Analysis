# TTCS Independent Branch Record

```json
{
  "step_id": 4,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step4_weyl_profile_and_bubble_restriction.tex",
    "Sessions/S0910A03/workspace/notes/step3_boundary_near_saturation.tex"
  ]
}
```

## Task

For the non-collapsing problem under two-sided Ricci pinching on a fixed closed 4-manifold:

The key difficulty: we have |Ric_g| ≤ Λ and Vol(M,g) ≥ V₀ > 0 on a FIXED compact manifold M, but we need Vol(B(p,r)) ≥ v₀ r⁴ for ALL p and small r (non-collapsing). Without sectional curvature bounds, the standard Cheeger-Fukaya-Gromov collapse theory doesn't apply.

Propose mechanisms or arguments that could establish non-collapsing, or explain precisely why it might fail (with an explicit model). Consider:

1. Can the diameter grow without bound on a FIXED manifold M with |Ric| ≤ 2? If so, give an example. If not, explain why fixed topology constrains diameter growth under Ricci bounds.

2. Does the Seiberg-Witten data (uniform L^∞ bound on spinor, integral lower bound ∫|Φ|⁴ ≥ cA, first-order elliptic equation D_AΦ = 0) provide any additional compactness beyond what pure Riemannian geometry gives?

3. For the POSITIVE branch (Ric ≈ +g): is there a volume lower bound from Myers + topology?

4. Can the recent Cheeger-Colding-Naber theory (under only Ricci bounds) give non-collapsing in dimension 4, perhaps using the constrained topology of connected sums of algebraic surfaces?

5. Could the Weyl profile concentration ∫(|W+|-1/(2√6))² = O(Aδ²) combined with volume convergence provide additional geometric control?

Give specific mathematical arguments or counterexamples, not just references.

## Output

The pure Riemannian implication

\[
|\operatorname{Ric}_g|\le \Lambda,\qquad \operatorname{Vol}(M,g)\ge V_0
\quad\Longrightarrow\quad
\operatorname{Vol}B(p,r)\ge v_0 r^4
\]

is false on a fixed smooth 4-manifold. Any proof for the Ishida–LeBrun critical manifolds would therefore need to use extra structure: the Seiberg–Witten near-equality mechanism, the special connected-sum topology, or the Weyl profile. Here are the sharp mechanisms.

---

### 1. Diameter can grow on a fixed 4-manifold with \(|\operatorname{Ric}|\le 2\)

A very explicit exact Einstein model comes from degenerating hyperbolic surfaces.

Let \(\Sigma_g\) be a closed surface of genus \(g\ge2\), and let \(h_i\) be hyperbolic metrics with a simple closed geodesic of length \(\ell_i\to0\). The collar lemma gives a collar

\[
(-w_i,w_i)\times S^1,\qquad
h_i=d\rho^2+\ell_i^2\cosh^2\rho\,d\theta^2,
\]

with

\[
w_i=\operatorname{arsinh}\left(\frac1{\sinh(\ell_i/2)}\right)
\sim \log\frac4{\ell_i}\to\infty.
\]

Let \((\Sigma_{g'},k)\) be another fixed hyperbolic surface, and set

\[
M=\Sigma_g\times \Sigma_{g'},\qquad g_i=h_i\oplus k.
\]

Then

\[
\operatorname{Ric}_{g_i}=-g_i,
\]

so the sequence satisfies the strongest possible two-sided Ricci pinching around \(-g\). The volume is fixed:

\[
\operatorname{Vol}(M,g_i)
=16\pi^2(g-1)(g'-1).
\]

But

\[
\operatorname{diam}(M,g_i)\ge w_i\to\infty.
\]

Local four-volume also collapses. Choose \(p_i\) on the short geodesic in \((\Sigma_g,h_i)\) and \(q\in \Sigma_{g'}\). For fixed \(0<r<1\) and \(i\) large,

\[
B_{g_i}((p_i,q),r)
\subset B_{h_i}(p_i,r)\times B_k(q,r).
\]

Inside the collar,

\[
\operatorname{Area}_{h_i} B_{h_i}(p_i,r)
\le \int_{-r}^{r}\ell_i\cosh\rho\,d\rho
=2\ell_i\sinh r.
\]

Hence

\[
\operatorname{Vol}_{g_i} B_{g_i}((p_i,q),r)
\le C(r,k)\,\ell_i\to0.
\]

So no uniform \(v_0 r^4\) lower bound exists, even though \(M\) is fixed, \(\operatorname{Ric}=-g\), and total volume is fixed.

A flat model shows the same phenomenon even more simply:

\[
M=T^4,\qquad 
g_i=L_i^2d\theta_1^2+\varepsilon_i^2(d\theta_2^2+d\theta_3^2+d\theta_4^2),
\qquad L_i\varepsilon_i^3=1.
\]

Then \(\operatorname{Ric}_{g_i}=0\), \(\operatorname{Vol}=1\), \(\operatorname{diam}\sim L_i\to\infty\), and balls of fixed radius wrap around the tiny \(T^3\)-directions and have volume \(\sim r\varepsilon_i^3\to0\).

Thus fixed topology alone does not bound diameter under \(|\operatorname{Ric}|\le2\).

What would suffice is diameter control. If \(\operatorname{Ric}\ge -3H g\), \(\operatorname{diam}\le D\), and \(\operatorname{Vol}M\ge V_0\), Bishop–Gromov gives

\[
\operatorname{Vol}B(p,r)
\ge 
V_0\,\frac{V_{-H}(r)}{V_{-H}(D)},
\]

where \(V_{-H}(r)\) is the radius-\(r\) ball volume in the simply connected 4-dimensional space form of curvature \(-H\). For \(0<r\le r_*\),

\[
V_{-H}(r)\ge c(H,r_*)r^4,
\]

so one obtains

\[
\operatorname{Vol}B(p,r)\ge v_0 r^4.
\]

The missing geometric input is therefore not merely total volume; it is a diameter or equivalent all-scale thickness mechanism.

There is one important topology-sensitive contrast. A thin round connected-sum neck cannot be long under Ricci control. For a rotationally symmetric neck

\[
g=dt^2+f(t)^2g_{S^3},
\]

the Ricci eigenvalues are

\[
\operatorname{Ric}_{tt}=-3\frac{f''}{f},
\]

and

\[
\operatorname{Ric}_{S^3}
=
\frac{2(1-(f')^2)-ff''}{f^2}.
\]

If \(f\le \varepsilon\) and \(|\operatorname{Ric}|\le2\), then

\[
|f''|\le C\varepsilon,\qquad |1-(f')^2|\le C\varepsilon^2.
\]

Thus \(|f'|\approx1\), so the region where \(f\le\varepsilon\) has length \(O(\varepsilon)\). A long thin round \(S^3\)-tube is impossible. This is why connected-sum topology may help if every possible diameter-producing corridor must look spherical. The hyperbolic-surface example escapes through an \(S^1\)-collar, and cusp-like models escape through nil or torus sections.

---

### 2. What the Seiberg–Witten data gives, and what it does not give

Let

\[
u=|\Phi|^2.
\]

For an unperturbed Seiberg–Witten solution,

\[
D_A\Phi=0,\qquad F_A^+=\sigma(\Phi),
\]

one has the scalar Weitzenböck identity

\[
0=2\Delta u+4|\nabla_A\Phi|^2+s u+u^2.
\]

If \(s\approx -4\), the maximum principle gives

\[
u\le 4+o(1).
\]

A lower bound

\[
\int_M u^2\,d\mu=\int_M|\Phi|^4\,d\mu\ge cA
\]

combined with \(u\le C\) gives only a lower bound for the measure of the region where \(\Phi\) is nontrivial. It does not force every ball to contain spinor mass.

The first-order equation also does not by itself prevent collapse. On a flat collapsed \(T^4\) with a spin structure admitting parallel spinors, one can take \(\Phi\) constant and \(D\Phi=0\), with uniform \(L^\infty\) bound and fixed \(\int|\Phi|^4\), while local four-volume collapses. This model does not satisfy the full curvature equation \(F_A^+=\sigma(\Phi)\) in the Ric \(\approx -g\) regime, but it shows that the Dirac equation plus spinor mass is not a geometric thickness mechanism.

The real issue is that the integral near-equality quantities can pass through thin regions almost invisibly. On a product tube

\[
Z_\eta=[-1,1]\times Y_\eta^3,\qquad \operatorname{Vol}(Y_\eta)=\eta,
\]

a scalar profile \(u(t)\) changing from \(4\) to \(0\) across the tube has

\[
\int_{Z_\eta}|du|^2\,d\mu
=
\eta\int_{-1}^1 |u'(t)|^2\,dt
=O(\eta),
\]

and similarly any reaction deficit integrated over the tube is \(O(\eta)\). Thus a vanishing-volume topology core can carry spinor zeros or phase transitions at negligible cost in the global Seiberg–Witten inequalities.

To extract geometric compactness from SW data, one would need something stronger than

\[
\|\Phi\|_{L^\infty}\le C,\qquad \int|\Phi|^4\ge cA,\qquad D_A\Phi=0.
\]

Useful stronger structures would be, for example:

\[
|\Phi|\ge \eta>0\quad\text{pointwise},
\]

or a self-dual harmonic form \(\omega_i\) with

\[
|\omega_i|\to \text{constant}>0
\]

in a topology strong enough to produce an almost-Kähler form. But those upgrades require Sobolev, harmonic-radius, or local volume input. The SW equations give the right elliptic identities, yet collapsed tubes can hide the exact places where pointwise lower bounds are lost.

---

### 3. Positive branch: Myers plus total volume gives local noncollapse

For Ricci pinching near \(+g\), the situation is much better once a total volume lower bound is known.

Assume

\[
\operatorname{Ric}_g\ge (1-\delta)g,\qquad 0<\delta<1.
\]

In dimension \(4\), write

\[
(1-\delta)g=3k\,g,\qquad k=\frac{1-\delta}{3}.
\]

Myers gives

\[
\operatorname{diam}(M,g)\le \frac{\pi}{\sqrt{k}}
=
\pi\sqrt{\frac3{1-\delta}}.
\]

If also

\[
\operatorname{Vol}(M,g)\ge V_0,
\]

then Bishop–Gromov yields, for every \(p\in M\),

\[
\operatorname{Vol}B(p,r)
\ge 
V_0\,
\frac{V_k(r)}{V_k(D)},
\qquad
D=\pi\sqrt{\frac3{1-\delta}},
\]

where \(V_k(r)\) is the radius-\(r\) ball volume in the 4-sphere of sectional curvature \(k\). Hence, for \(0<r\le r_*\),

\[
\operatorname{Vol}B(p,r)\ge v_0 r^4,
\]

with \(v_0=v_0(V_0,\delta,r_*)>0\).

So in the positive branch, the combination

\[
\operatorname{Ric}\approx +g
\quad+\quad
\operatorname{Vol}M\ge V_0
\]

does give the desired local noncollapse.

What Myers does not supply is the total volume lower bound itself. In four dimensions, Chern–Weil gives

\[
8\pi^2\chi(M)
=
\int_M
\left(
|W|^2-\frac12|\operatorname{Ric}^\circ|^2+\frac{s^2}{24}
\right)d\mu.
\]

If \(\operatorname{Ric}\approx g\), then \(s\approx4\) and \(\operatorname{Ric}^\circ\approx0\), so

\[
8\pi^2\chi(M)
=
\int_M |W|^2\,d\mu
+
\left(\frac23+o(1)\right)\operatorname{Vol}(M,g).
\]

This gives an upper relation for the volume, not a lower one, because the Weyl energy can carry the topological term. In special geometric classes, such as Kähler–Einstein Fano metrics, cohomology fixes the volume through the Kähler class; but Myers plus smooth topology alone does not produce a general numerical \(V_0\).

For the Ishida–LeBrun manifolds with nontrivial Seiberg–Witten input, the positive branch is often empty for a simpler reason: Ric \(\approx +g\) gives \(s>0\), while SW invariants obstruct positive scalar curvature.

---

### 4. What Cheeger–Colding–Naber theory can and cannot supply

Cheeger–Colding–Naber theory is powerful once a ball is already known to be noncollapsed. In dimension four, a typical form is:

\[
|\operatorname{Ric}|\le 3,\qquad
\operatorname{Vol}B(p,1)\ge v
\quad\Longrightarrow\quad
\int_{B(p,1/2)}|\operatorname{Rm}|^2\le C(v),
\]

with quantitative control of the singular strata and regularity scale. But the lower volume ratio is an input, not an output.

For a collapsed ball under two-sided Ricci bounds, the theory describes possible lower-dimensional behavior rather than eliminating it. After rescaling a small ball \(B(p,r)\), the Ricci tensor becomes \(O(r^2)\), so collapsed tangent geometries may look like lower-dimensional Ricci-flat or almost Ricci-flat spaces with nilpotent local symmetry.

The relevant complementary source family is the Kapovitch–Wilking generalized Margulis lemma and the Naber–Zhang work on bounded-Ricci collapse. These results say, roughly, that collapsed balls under Ricci lower bounds carry almost nilpotent local fundamental groups. In a simply connected closed 4-manifold, those small loops can still die outside the ball; K3 elliptic-fibration collapse is the standard mental model. Thus trivial global \(\pi_1\) does not by itself stop local torus or circle collapse.

For connected sums of algebraic surfaces, topology might enter through the following more refined mechanism:

- collapsed regions should carry local \(S^1\), \(T^2\), or \(T^3\)-type nil directions;
- the connected-sum topology, intersection form, and SW canonical classes must then be carried by transition cores where those fibers vanish;
- Euler and signature densities must concentrate in those cores, because smooth bounded-curvature collapse contributes little to Chern–Weil integrals;
- harmonic representatives of the Bauer–Furuta sign classes should become almost basic on the collapsed regions, forcing their \(L^2\)-mass and pairings into the cores.

This is a plausible way to combine Ricci-collapse theory with the special topology, but it is not a direct Cheeger–Colding–Naber consequence. The observable quantities would be:

\[
\operatorname{rank}\operatorname{im}\big[\pi_1(B(p,\varepsilon r))\to \pi_1(B(p,r))\big],
\]

the distribution of

\[
|W_+|^2,\quad |W_-|^2,\quad |\operatorname{Ric}^\circ|^2,
\]

and the \(L^2\)-mass of the harmonic self-dual representatives of the SW classes.

---

### 5. Weyl profile concentration helps, but not by itself

The profile

\[
\int_M
\left(
|W_+|-\frac1{2\sqrt6}
\right)^2d\mu
=
O(A\delta^2)
\]

is extremely restrictive for macroscopic regions.

For the exact Einstein product model above,

\[
M=\Sigma_g\times\Sigma_{g'},
\qquad \operatorname{Ric}=-g,
\]

one computes

\[
s=-4.
\]

With the product orientation, the curvature operator on \(\Lambda^+\) has eigenvalues

\[
-1,\ 0,\ 0
\]

before subtracting \(s/12=-1/3\). Hence

\[
W_+\text{ has eigenvalues }
-\frac23,\ \frac13,\ \frac13,
\]

and

\[
|W_+|^2=\frac49+\frac19+\frac19=\frac23,
\qquad
|W_+|=\frac2{\sqrt6}.
\]

Thus

\[
\left(
|W_+|-\frac1{2\sqrt6}
\right)^2
=
\left(
\frac2{\sqrt6}-\frac1{2\sqrt6}
\right)^2
=
\frac38.
\]

Any product-hyperbolic region of volume \(V\) contributes \(\frac38V\) to the profile deficit. Since the hyperbolic collar in the surface degeneration has macroscopic area, the Weyl profile excludes this entire exact Einstein collapse channel in the Ishida–LeBrun near-equality setting.

Similarly, a real-hyperbolic 4-cusp scaled to \(\operatorname{Ric}=-g\),

\[
g=dt^2+e^{-2t/\sqrt3}g_{T^3},
\]

has sectional curvature \(-1/3\), hence \(W_+=0\). Its profile discrepancy is

\[
\left(0-\frac1{2\sqrt6}\right)^2=\frac1{24}.
\]

A macroscopic real-hyperbolic cusp region is also excluded by the Weyl profile.

However, the profile does not control points lying in regions of vanishing volume. A real-hyperbolic cusp segment

\[
[T,T+L]\times T^3,
\qquad
g=dt^2+e^{-2t/\sqrt3}g_{T^3},
\]

has volume

\[
\operatorname{Vol}\sim C e^{-\sqrt3T}(1-e^{-\sqrt3L}).
\]

By taking \(T\) large, one obtains an arbitrarily long Ric \(=-g\) collapsed tendril of arbitrarily small volume. Its Weyl-profile cost is only

\[
\frac1{24}\operatorname{Vol}.
\]

Balls near the far end have very small four-volume, while the global profile barely changes. Turning this cusp segment into a closed fixed-manifold construction with uniformly pinched Ricci is a hard gluing problem, but as a local model it explains why an \(L^2\) Weyl profile alone cannot imply pointwise noncollapse.

The profile becomes powerful only if paired with an additional principle of the following type:

1. every collapsed diameter-producing corridor has a macroscopic subregion modeled on product-hyperbolic, real-hyperbolic, Kähler–Einstein, or scalar-flat geometries; or  
2. every collapsed topology core carries quantized \(W_+\)-energy incompatible with the calibrated value; or  
3. the near-equality SW forms force a pointwise nonzero self-dual form on all regions outside finitely many hyperkähler bubbles.

Without such an additional mechanism, the profile permits a small-volume collapsed core, and all-point noncollapse remains out of reach.

The strongest present synthesis is therefore:

- Pure Ricci bounds plus total volume do not give local noncollapse on a fixed 4-manifold.
- Positive Ricci pinching plus total volume does, via Myers and Bishop–Gromov.
- SW data gives global mass and elliptic identities, but collapsed cores can hide spinor zeros and phase transitions.
- Cheeger–Colding–Naber theory organizes collapsed regions but does not remove them without extra topological or analytic input.
- The Weyl profile excludes macroscopic known Einstein-collapse geometries, especially \(\Sigma_g\times\Sigma_{g'}\) degenerations and real-hyperbolic/Kähler–Einstein bulk, but it does not see vanishing-volume tendrils or topology cores.