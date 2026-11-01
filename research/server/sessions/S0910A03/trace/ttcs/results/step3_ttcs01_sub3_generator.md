# TTCS Independent Branch Record

```json
{
  "step_id": 3,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/Curvature-Connected-Sums-and-Seiberg-Witten-Theory--7e92a6723434--2ac6d11897c5/object.md",
    "Knowledge/objects/papers/The-Yamabe-invariant-of-a-class-of-symplectic-4-manifolds--93fc75a3247d--f4170b4b9bdb/object.md",
    "Knowledge/objects/papers/The-Calabi-metric-and-desingularization-of-Einstein-orbifolds--3b9fd6e4b2cd--c8fe6b2cf08c/object.md",
    "Sessions/S0910A03/workspace/notes/step2_cap_analysis_and_route.tex"
  ]
}
```

## Task

Find a high-value geometric mechanism that could decide whether Ishida–LeBrun Theorem 7 boundary families can have uniform negative Ricci defect δ_-→0. Compare two mechanisms grounded in the supplied sources: (i) near-equality compactness leading to Kähler/symplectic structure, and (ii) degeneration into negative Kähler–Einstein/orbifold pieces plus scalar-flat ASD/ALE neck pieces. Analyze which local model would be required by pointwise Ric≈-g, why standard conformal/long-neck constructions saturating L2 functionals fail or might be altered, and formulate one or more precise intermediate theorems whose proof would materially advance Yau 26. Keep global Einstein nonexistence distinct from nonexistence near a degeneration.

## Output

### 1. The threshold identity behind the Ishida–LeBrun examples

Write  
\[
M=\Bigl(\#_{j=1}^{m}X_j\Bigr)\#N,\qquad
A=\sum_{j=1}^{m}c_1^2(X_j),\qquad
D=4m-(2\chi+3\tau)(N).
\]
Then
\[
(2\chi+3\tau)(M)=A-D.
\]
For a metric \(g\), put
\[
Z_g=\operatorname{Ric}_g-\frac{s_g}{4}g,\qquad
\delta_-(g)=\bigl\|g^{-1}(\operatorname{Ric}_g+g)\bigr\|_{L^\infty}.
\]
If \(\delta_-(g)\leq\delta\), the eigenvalues \(x_\alpha\) of
\(g^{-1}(\operatorname{Ric}+g)\) satisfy \(|x_\alpha|\leq\delta\), hence
\[
|s+4|\leq4\delta,\qquad |Z|^2
=\sum_{\alpha=1}^{4}(x_\alpha-\bar x)^2\leq4\delta^2. \tag{1}
\]

The Gauss–Bonnet–signature formula and the Ishida–LeBrun monopole estimate give
\[
\begin{aligned}
Q(g)
&:=\frac1{4\pi^2}\int_M
 \left(\frac{s^2}{24}+2|W_+|^2\right)\,d\mu\\
&=A-D+\frac1{8\pi^2}\int_M|Z|^2\,d\mu
>\frac23A \qquad (m>1), \tag{2}
\end{aligned}
\]
where strictness comes from the absence of a symplectic structure on these connected sums. Therefore
\[
\int_M|Z|^2\,d\mu>8\pi^2\left(D-\frac A3\right). \tag{3}
\]
Away from the equality line \(D=A/3\), (1) and (3) imply
\[
\operatorname{Vol}_g(M)>
\frac{2\pi^2(D-A/3)}{\delta_-(g)^2}. \tag{4}
\]
Thus any tightly pinched sequence outside the equality line must have volume growing at least quadratically in \(\delta_-^{-1}\). On the equality line,
\[
Q(g)-\frac23A=\frac1{8\pi^2}\int_M|Z|^2\,d\mu>0. \tag{5}
\]
This is exactly where compactness versus geometric splitting becomes decisive.

---

## 2. Mechanism I: monopole near-equality plus compactness

Suppose \(D=A/3\) and \(g_i\) satisfies \(\delta_-(g_i)\to0\). If
\[
\delta_-(g_i)^2\operatorname{Vol}_{g_i}(M)\longrightarrow0, \tag{6}
\]
then (1) and (5) imply
\[
Q(g_i)\longrightarrow\frac23A.
\]
The proof of the estimate \(Q\ge 2A/3\) is a chain consisting of an algebraic curvature inequality followed by LeBrun’s Seiberg–Witten estimate
\[
\int_M\bigl(s-\sqrt6|W_+|\bigr)^2\,d\mu
\ge72\pi^2(a^+)^2.
\]
Consequently, if curvature and Seiberg–Witten energy do not escape, all remainder terms in this chain tend to zero. Compactness of the monopole pairs should then produce a limiting self-dual form of constant nonzero length. The equality analysis in the supplied Ishida–LeBrun source makes this form symplectic; for the scalar estimate, the stronger equality form is constant-scalar-curvature Kähler.

This mechanism would contradict the connected-sum topology when \(m>1\). Its missing geometric input is substantial: Ricci pinching alone gives neither an upper volume estimate nor diameter control nor pointwise Weyl control. The sharp Ishida–LeBrun sequences show precisely how equality may be approached without producing a global symplectic form: monopole energy separates among Kähler–Einstein orbifold pieces.

A useful quantitative theorem would be:

> **Monopole compactness theorem at the equality line.**  
> Let \(M\) be an Ishida–LeBrun equality-line manifold with \(m>1\). Suppose \(g_i\) satisfies
> \[
> \delta_-(g_i)\to0,\qquad
> \delta_-(g_i)^2\operatorname{Vol}_{g_i}(M)\to0,
> \]
> together with noncollapse at every curvature scale and a uniform diameter estimate. Then either:
> 1. the limiting monopole form extends across the bubble tree and gives a symplectic structure on \(M\); or
> 2. the macroscopic monopole mass lies on at least two components separated by a vanishing-scale Ricci-flat connector with at least two ALE ends.

The second alternative is geometrically impossible under the stated noncollapse, as explained below. A proof would remove the equality-line ambiguity under natural compactness hypotheses.

---

## 3. Mechanism II: the local model forced by pointwise pinching

There is a simple but strong scaling fact. Suppose \(U_i\subset M\), \(t_i\to0\), and
\[
\widehat g_i=t_i^{-1}\Phi_i^*g_i\longrightarrow q
\quad\text{in }C^2_{\mathrm{loc}}.
\]
Since Ricci as a \((0,2)\)-tensor is invariant under constant rescaling,
\[
\widehat g_i^{-1}
\bigl(\operatorname{Ric}_{\widehat g_i}+t_i\widehat g_i\bigr)
=t_i(\Phi_i^*g_i)^{-1}
\bigl(\operatorname{Ric}_{g_i}+g_i\bigr).
\]
Thus
\[
\left\|\widehat g_i^{-1}\operatorname{Ric}_{\widehat g_i}\right\|
\le t_i(1+\delta_-(g_i))\longrightarrow0,
\]
and every noncollapsed \(C^2\) small-scale model must satisfy
\[
\operatorname{Ric}_q=0. \tag{7}
\]

This immediately distinguishes pointwise pinching from \(L^2\)-optimal gluing.

### The Ishida–LeBrun connector is incompatible with (7)

The sharp \(\mathcal I_r\) construction consists of:

* Kähler–Einstein orbifold pieces \(\check X_j\);
* a conformal Green metric on \(N\setminus\{p_1,\ldots,p_m\}\), which is scalar-flat and anti-self-dual with \(m\) asymptotically flat ends;
* Ricci-flat gravitational instantons at orbifold points;
* interpolation annuli whose curvature contribution is small only after integration.

The Kähler–Einstein pieces and gravitational instantons have the correct macroscopic and small-scale equations. The multi-ended conformal Green connector does not. If it persisted as a scaled \(C^2\) model, (7) would make it Ricci-flat. But a complete Ricci-flat manifold with at least two ALE ends cannot exist: \(\operatorname{Ric}\ge0\) and multiple ends produce a line and a Cheeger–Gromoll splitting \(\mathbb R\times Y\); with two ends \(Y\) is compact, giving linear volume growth rather than ALE \(r^4\) growth.

There is therefore no family with \(\delta_-\to0\) that is asymptotic, after rescaling, to the standard Ishida–LeBrun multi-ended connector.

An exact conditional theorem is already available from this argument:

> **Separating-neck exclusion.**  
> Let \(g_i\) satisfy \(\delta_-(g_i)\to0\). Suppose a separating neck has scale \(t_i^{1/2}\to0\), its rescaling by \(t_i^{-1}\) is noncollapsed, and the rescaled necks exhaust a complete finite-energy space with at least two ALE ends. Then such a sequence cannot exist.

This excludes the supplied degeneration, though not every possible degeneration.

### Ordinary blowups have an even sharper local obstruction

For \(X\#\overline{\mathbb{CP}}^2\), a vanishing-scale exceptional region would require a Ricci-flat ALE metric on \(\mathcal O(-1)\to\mathbb{CP}^1\) with trivial group at infinity. A Ricci-flat ALE space with trivial group has asymptotic volume ratio \(1\). Bishop–Gromov equality then makes it Euclidean \(\mathbb R^4\), incompatible with the exceptional sphere.

The Burns metric does not supply the required model. Its scalar curvature is zero and its Ricci tensor is nonzero. For an exact scaled Burns region \(t\,g_{\mathrm{Burns}}\), scalar flatness alone gives
\[
|s+4|\le4\delta_-\quad\Longrightarrow\quad\delta_-\ge1.
\]
Its nonzero trace-free Ricci part actually produces relative Ricci terms of order \(t^{-1}\). Non-Ricci-flatness by itself does not compute a Lyapunov–Schmidt coefficient; the decisive fact is that it cannot be the leading small-scale metric in (7).

---

## 4. Why conformal and long-neck constructions control \(L^2\), not \(L^\infty\)

The Gromov–Lawson and conformal Green constructions place scalar-flat or positive-scalar-curvature geometry in a region whose volume tends to zero. This is ideal for
\[
\int s^2,\qquad \int|\operatorname{Ric}|^2,
\]
because a transition region may contribute arbitrarily little after integration. Pointwise pinching sees the largest defect, independently of volume.

For \(\widetilde g=e^{2u}g\) in dimension four,
\[
\operatorname{Ric}_{\widetilde g}
=\operatorname{Ric}_g
-2(\nabla^2u-du\otimes du)
-(\Delta u+2|du|^2)g.
\]
The scalar equation controls only the trace. Pointwise Einstein pinching additionally requires
\[
(\operatorname{Ric}_g)_0
-2(\nabla^2u-du\otimes du)_0\approx0, \tag{8}
\]
a tensor equation not imposed by Green’s functions or Yamabe gluing.

Even the most symmetric spherical throat illustrates the issue. For
\[
g=dt^2+f(t)^2g_{S^3(1)},
\]
the equations \(\operatorname{Ric}\approx-g\) read
\[
-3\frac{f''}{f}\approx-1,\qquad
\frac{2(1-(f')^2)-ff''}{f^2}\approx-1.
\]
At a two-sided throat, \(f'=0\). The first equation gives \(f''/f\approx1/3\), while the second tangential eigenvalue is then
\[
\frac{2}{f^2}-\frac13,
\]
whose distance from \(-1\) is at least \(2/3\). Hyperbolic warping has an apex and is monotone; it does not provide a narrow two-sided spherical connector. An anisotropically collapsed neck remains a separate possibility.

---

## 5. The first ALE obstruction is especially relevant to \(\delta_-\)

The Morteza–Viaclovsky source supplies the correct refined ansatz. On a Ricci-flat ALE cap \(q\), one seeks
\[
h_t=q+t h,
\]
where the quadratic term of \(h\) matches the Einstein orbifold jet. Their linear analysis gives
\[
\operatorname{Ric}(h_t)
=t\Lambda h_t+t\lambda o+O(t^2\rho^2).
\]
The physical cap metric is \(g_t=t h_t\), so
\[
g_t^{-1}\bigl(\operatorname{Ric}(g_t)-\Lambda g_t\bigr)
=\lambda h_t^{-1}o+O(t\rho^2). \tag{9}
\]
At the gluing radius \(\rho\asymp t^{-1/4}\), the last term is \(O(t^{1/2})\). Hence:

* if \(\lambda\ne0\), the cap contributes an order-one Ricci defect;
* if \(\lambda=0\), the refined approximate metric already has pointwise defect \(O(t^{1/2})\), even if later nonlinear obstructions prevent an exact Einstein metric.

This distinction is central for Yau 26. Exact Einstein desingularization may involve many successive obstructions. Uniform pinching only requires that the first residual be smaller than the metric scale. Thus a compact Einstein orbifold whose smooth resolution has no Einstein metric, but whose first ALE coefficients all vanish, is a plausible source of \(\delta_-\to0\).

In the supplied higher-dimensional Calabi model, vanishing is equivalent to
\[
n\langle\mathcal R(\omega),\omega\rangle
+2(n-2)R=0. \tag{10}
\]
For a Kähler–Einstein orbifold,
\(\langle\mathcal R(\omega),\omega\rangle=2R\), so the left side is
\[
4(n-1)R,
\]
which is nonzero when \(n\ge3\) and \(R\ne0\). Those natural desingularizations therefore retain an order-one defect. In real dimension four, rotational gluing parameters enter, as in Biquard’s analysis, so the corresponding projection must be computed with those rotations included.

A precise theorem suggested by (9) is:

> **First-order approximate desingularization theorem.**  
> Let \((M_0,g_0)\) be a compact Einstein orbifold with \(\operatorname{Ric}_{g_0}=-g_0\), and let its singularities admit one-ended Ricci-flat ALE fillings \(q_\alpha\). Assume the linear matching equations possess uniformly controlled right inverses modulo their \(L^2\) kernels.  
> 
> * If every first projection \(\lambda_\alpha\) can be made zero using the available rotational, scale, and orbifold-deformation parameters, the smooth desingularization carries metrics \(g_t\) with
>   \[
>   \delta_-(g_t)=O(t^\gamma)
>   \]
>   for some \(\gamma>0\).
> * If
>   \[
>   \inf_{\text{all matching parameters}}\max_\alpha|\lambda_\alpha|>0,
>   \]
>   every family with that orbifold/ALE asymptotic form has
>   \[
>   \liminf_{t\to0}\delta_-(g_t)>0.
>   \]

For approximate pinching, this theorem is more directly relevant than an exact Einstein gluing theorem.

---

## 6. The strongest combined geometric possibility

The two mechanisms fit into one proposed structure theorem:

> **Topology-core theorem for Ishida–LeBrun threshold manifolds.**  
> Let \(M\) be one of the \(m>1\) threshold examples and suppose \(g_i\) satisfies \(\delta_-(g_i)\to0\). Then one of the following occurs:
> 
> 1. after diffeomorphisms, a macroscopic component converges strongly enough for the Seiberg–Witten equality analysis to produce a symplectic structure extending over \(M\);
> 2. the connected-sum topology concentrates at vanishing scale, and a rescaling produces a noncollapsed complete Ricci-flat connector with at least two ALE ends;
> 3. the topology is carried by an anisotropically collapsed region or by a macroscopic region whose diameter diverges.

The first possibility conflicts with the Ishida–LeBrun connected-sum topology. The second conflicts with Ricci splitting and ALE volume growth. Thus the unresolved substance is concentrated in the third possibility: collapsed topology cores and diameter escape under two-sided Ricci pinching near \(-g\).

This also keeps two logically different statements separate:

* The Ishida–LeBrun monopole argument excludes every smooth Einstein metric on the specified manifold.
* Morteza–Viaclovsky or Biquard-type projections exclude Einstein metrics, or even \(\delta_-\to0\), only within a specified orbifold/ALE degeneration.
* Excluding the standard scalar-flat ASD connector does not by itself exclude a radically different pinched sequence.
* A vanishing first ALE projection could produce \(\delta_-\to0\) even when later terms preclude an exact Einstein metric.

The most decisive computation for a concrete threshold family is therefore the leading ALE projection for every plausible one-ended orbifold resolution, together with a topology argument showing that any separation into several Kähler–Einstein pieces would require a forbidden multi-ended Ricci-flat connector. A useful figure would represent the degeneration as a graph: macroscopic \(\operatorname{Ric}=-g\) vertices, one-ended Ricci-flat ALE bubbles attached at vertices, and separating edges. The supplied \(L^2\)-optimal construction places scalar-flat ASD metrics on the separating edges; pointwise pinching requires Ricci-flat edge models, which do not exist in the noncollapsed ALE category.