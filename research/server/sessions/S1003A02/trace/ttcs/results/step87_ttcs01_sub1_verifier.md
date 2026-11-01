# TTCS Independent Branch Record

```json
{
  "step_id": 87,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/step56_orbifold_attainment_zero_energy_bound_Tpoint_interaction.md",
    "Sessions/S1003A02/workspace/scripts/step86_lemma86S_check.py",
    "Sessions/S1003A02/workspace/data/step86/lemma86S_check.json",
    "Knowledge/objects/papers/ALE-Ricci-flat-Kahler-metrics-and-deformations-of-quotient-surface-singu--9db598b6c84c--5ab7b434e210/object.md"
  ]
}
```

## Task

Independently verify the mathematical correctness and exact scope of Lemma 86.S and Lemma 86.S′ in theorem_package_v1.md. Focus on the cutoff scaling rho=epsilon^{tau/(tau+2)}, C^2 annular curvature and integral estimates, iteration for ALE trees, continuity of the Einstein defect, whether scalar variance is automatically controlled, and the Ricci-flat bulk case. For Wahl/T singularities, read Suvaina's primary source and determine whether the Milnor-fibre metrics have the derivative-controlled order-4 ALE asymptotics required. For Lemma 86.S′, decide the minimal hypotheses under which the displayed defect ledger follows, identify any missing denominator case or interaction term, and distinguish standard cutoff-glued families from arbitrary degenerating sequences. Give exact corrected statements/proofs where needed.

## Output

# Scientific verification memo: Lemmas 86.S and 86.S′

## 1. Main conclusions

1. **Lemma 86.S is mathematically valid** for a finite collection of isolated orbifold points, provided each ALE metric has an end chart satisfying
   \[
   |\partial^j(h-\delta)|\le C r^{-\tau-j},\qquad j=0,1,2,
   \]
   for some \(\tau>0\), and the end identifications produce the stated smooth resolution.

2. The choice
   \[
   \rho=\varepsilon^{\tau/(\tau+2)}
   \]
   is correct. It balances the orbifold Taylor error \(O(\rho^2)\) with the scaled ALE error \(O((\varepsilon/\rho)^\tau)\), gives uniformly bounded curvature on the cutoff annulus, and gives \(O(\rho^4)\) errors in all relevant curvature integrals.

3. For a compact bulk with \(R(g)=\int|\operatorname{Ric}_g|^2>0\),
   \[
   \mathscr D(g_\varepsilon)\longrightarrow \mathscr D(g).
   \]
   If \(g\) is Einstein with Einstein constant \(\Lambda\ne0\), then
   \[
   P(g_\varepsilon)=O(\rho^4),\qquad
   L_s(g_\varepsilon)=O(\rho^4),\qquad
   \mathscr D(g_\varepsilon)=O(\rho^4).
   \]
   Thus the scalar-variance condition formerly attached to these resolution constructions is automatic.

4. **A Ricci-flat bulk is a separate denominator case.** The same local cutoff construction gives
   \[
   P(g_\varepsilon)\to0,\qquad \mathscr D(g_\varepsilon)\to4,
   \]
   rather than \(\mathscr D\to0\). Hence this construction proves \(P_*=0\), but by itself gives no conclusion that \(\alpha=0\).

5. The finite ALE-tree extension is valid only when the relative smoothing parameters at all inner vertices also tend to zero. Because \(\int|\operatorname{Ric}|^2\) is scale invariant in dimension four, merely placing an inner neck at a small physical scale does not make its Ricci energy small.

6. **Şuvaina’s metrics do provide the needed order-four asymptotics with derivatives**, although her printed Definition 1.1 writes only
   \[
   g-h_0=O(r^{-4}),\qquad J-J_0=O(r^{-4})
   \]
   without explicit derivative symbols. The derivative estimates follow from her finite-centre Hitchin/Gibbons–Hawking construction after recentering the centres. This applies to the \(\mathbb Q\)-Gorenstein smoothings of all cyclic class-\(T\) singularities, including Wahl singularities.

7. **Lemma 86.S′ is valid when \(R(g)+\sum P(N_j)>0\)** and for the stated cutoff-glued families. Its displayed quotient needs a separate interpretation when that denominator is zero. In that case the standard local cutoff construction has \(\mathscr D\to4\).

8. The sentence that a scalar-flat bubble “moves the value toward \(4\), and does so exactly when \(P(N)>0\)” needs refinement. For \(R(g)>0\), writing \(Q=\sum P(N_j)\),
   \[
   \mathscr D_\infty
   =\frac{R(g)\mathscr D(g)+4Q}{R(g)+Q}
   =\mathscr D(g)+\frac{(4-\mathscr D(g))Q}{R(g)+Q}.
   \]
   The increase is strict precisely when \(Q>0\) and \(\int s_g\ne0\). If \(\mathscr D(g)=4\), adding such bubbles leaves the value equal to \(4\).

---

## 2. The cutoff calculation

Work in an orbifold normal chart \(B/\Gamma\), with Euclidean coordinates on the cover. Write
\[
g=\delta+q_g,\qquad
|\partial^j q_g|\le C r^{2-j},\qquad 0\le j\le2.
\]
For an ALE metric \(h\), assume
\[
h=\delta+q_h,\qquad
|\partial^j q_h|\le C R^{-\tau-j},\qquad 0\le j\le2.
\]

After scaling \(h\) by \(\varepsilon^2\) and using the physical coordinate \(y=\varepsilon x\), its components are
\[
h_\varepsilon(y)=h(y/\varepsilon)
                =\delta+q_h(y/\varepsilon).
\]
On \(r=|y|\asymp\rho\),
\[
\sum_{j=0}^2 \rho^j|\partial^j q_g|
 \le C\rho^2,
\qquad
\sum_{j=0}^2 \rho^j|\partial^j q_{h,\varepsilon}|
 \le C\left(\frac{\varepsilon}{\rho}\right)^\tau.
\]

Let
\[
\eta_{\varepsilon,\rho}
   =\rho^2+\left(\frac{\varepsilon}{\rho}\right)^\tau.
\]
A radial cutoff with derivatives \(O(\rho^{-j})\) gives
\[
\sum_{j=0}^2\rho^j
   |\partial^j(g_\varepsilon-\delta)|
   \le C\eta_{\varepsilon,\rho}
\]
on the transition annulus. Consequently,
\[
|\operatorname{Rm}_{g_\varepsilon}|
 \le C\rho^{-2}\eta_{\varepsilon,\rho},
\]
where the quadratic first-derivative terms are absorbed because
\(\eta_{\varepsilon,\rho}\to0\).

Balancing the two metric errors gives
\[
\rho^2=\left(\frac{\varepsilon}{\rho}\right)^\tau,
\qquad
\rho=\varepsilon^{\tau/(\tau+2)}.
\]
Thus \(\eta_{\varepsilon,\rho}=O(\rho^2)\), and
\[
|\operatorname{Rm}_{g_\varepsilon}|\le C
\]
on the annulus. Its volume is \(O(\rho^4)\), so
\[
\int_{\rm ann}|\operatorname{Ric}|^2=O(\rho^4),
\quad
\int_{\rm ann}s^2=O(\rho^4),
\quad
\int_{\rm ann}|s|=O(\rho^4).
\]

The inserted truncated ALE region also has volume \(O(\rho^4)\):
\[
\varepsilon^4
\operatorname{Vol}_h\{R\le\rho/\varepsilon\}
=O\!\left(
\varepsilon^4(\rho/\varepsilon)^4
\right)
=O(\rho^4).
\]
For a Ricci-flat filler its Ricci and scalar contributions vanish identically there. The deleted orbifold ball contributes \(O(\rho^4)\) because the original curvature is bounded.

For finitely many points, summing these estimates gives
\[
\begin{aligned}
V(g_\varepsilon)&=V(g)+O\!\left(\sum_j\rho_j^4\right),\\
\int s_{g_\varepsilon}
 &=\int s_g+O\!\left(\sum_j\rho_j^4\right),\\
\int s_{g_\varepsilon}^2
 &=\int s_g^2+O\!\left(\sum_j\rho_j^4\right),\\
R(g_\varepsilon)
 &=R(g)+O\!\left(\sum_j\rho_j^4\right),\\
P(g_\varepsilon)
 &=P(g)+O\!\left(\sum_j\rho_j^4\right),\\
L_s(g_\varepsilon)
 &=L_s(g)+O\!\left(\sum_j\rho_j^4\right).
\end{aligned}
\]

These are the precise estimates underlying Lemma 86.S.

---

## 3. Continuity of the Einstein defect

Put
\[
S(g)=\int s_g,\qquad R(g)=\int|\operatorname{Ric}_g|^2.
\]
For \(R(g)>0\),
\[
\mathscr D(g)
 =\inf_{\lambda\ne0}
 \left[
 \frac{R}{\lambda^2V}
 -\frac{2S}{\lambda V}+4
 \right]
 =4-\frac{S^2}{VR}.
\]
This remains valid when \(S=0\), where the value \(4\) is approached as \(|\lambda|\to\infty\). Also,
\[
\mathscr D(g)=\frac{4P(g)+L_s(g)}{R(g)}.
\]

Since the map
\[
(V,S,R)\longmapsto 4-\frac{S^2}{VR}
\]
is smooth on \(V>0,\ R>0\), the preceding integral estimates imply
\[
\mathscr D(g_\varepsilon)
 =\mathscr D(g)
 +O\!\left(\sum_j\rho_j^4\right).
\]

### Einstein bulk with \(\Lambda\ne0\)

If \(\operatorname{Ric}_g=\Lambda g\), then
\[
R(g)=4\Lambda^2V(g)>0,\qquad
P(g)=L_s(g)=0.
\]
Outside the shrinking gluing regions the new metric remains exactly Einstein. Inside a Ricci-flat filler,
\[
|\operatorname{Ric}_{g_\varepsilon}-\Lambda g_\varepsilon|^2
 =4\Lambda^2,
\]
but the filler volume is \(O(\rho^4)\). The transition annulus also contributes \(O(\rho^4)\). Hence directly,
\[
\mathscr D(g_\varepsilon)
 \le
 \frac{\int|\operatorname{Ric}_{g_\varepsilon}
              -\Lambda g_\varepsilon|^2}
      {\Lambda^2V(g_\varepsilon)}
 =O(\rho^4).
\]

Separately,
\[
P(g_\varepsilon)=O(\rho^4).
\]
The average scalar changes by \(O(\rho^4)\). The scalar differs by \(O(1)\) from \(4\Lambda\) only on a region of volume \(O(\rho^4)\), while on the exterior its difference from the new average is \(O(\rho^4)\). Therefore
\[
L_s(g_\varepsilon)=O(\rho^4).
\]
This proves that scalar variance is automatically controlled in the nonzero-Einstein-scale construction.

---

## 4. Ricci-flat compact bulk

When \(g\) is Ricci-flat, \(R(g)=S(g)=0\), so the continuity formula above cannot be used. By the original definition,
\[
\mathscr D(g)=4.
\]

For Ricci-flat fillers, all scalar curvature of the cutoff metric is supported in the union \(A_\varepsilon\) of the transition regions, whose volume tends to zero. Whenever \(R(g_\varepsilon)>0\),
\[
\left|\int s_{g_\varepsilon}\right|^2
 \le \operatorname{Vol}(A_\varepsilon)
       \int s_{g_\varepsilon}^2
 \le4\,\operatorname{Vol}(A_\varepsilon)
       R(g_\varepsilon),
\]
because \(s^2\le4|\operatorname{Ric}|^2\) in dimension four. Hence
\[
0\le
4-\mathscr D(g_\varepsilon)
=\frac{S(g_\varepsilon)^2}
       {V(g_\varepsilon)R(g_\varepsilon)}
\le
\frac{4\operatorname{Vol}(A_\varepsilon)}
     {V(g_\varepsilon)}
\longrightarrow0.
\]
If \(R(g_\varepsilon)=0\), the definition already gives
\(\mathscr D(g_\varepsilon)=4\).

Thus
\[
\boxed{\mathscr D(g_\varepsilon)\to4}
\]
for this Ricci-flat-bulk construction, while
\[
P(g_\varepsilon)\to0.
\]
This is the precise reason that a Ricci-flat orbifold resolution proves \(P_*=0\) but does not produce an \(\alpha=0\) sequence.

---

## 5. Finite ALE trees

Suppose a Ricci-flat ALE filler is itself an orbifold with further isolated points. Resolve an inner point using a relative scale \(\delta\), and let
\[
\sigma=\delta^{\tau/(\tau+2)}
\]
be its cutoff radius in the unscaled parent metric. The inner transition contributes
\[
\int|\operatorname{Ric}|^2=O(\sigma^4)
\]
in parent units.

After the entire parent is scaled by \(\varepsilon^2\), this integral remains \(O(\sigma^4)\), because the \(L^2\) Ricci energy is scale invariant in dimension four. Therefore physical nesting alone is insufficient: every relative inner parameter must satisfy
\[
\sigma_v(\varepsilon)\longrightarrow0.
\]
For a finite tree it is enough that
\[
E_\varepsilon
 =\sum_{\text{outer }j}\rho_j^4
  +\sum_{\text{inner vertices }v}\sigma_v^4
 \longrightarrow0.
\]
Then all conclusions above hold with \(O(E_\varepsilon)\). If the stated outer \(O(\rho^4)\) rate is desired, one can choose
\[
\sum_v\sigma_v^4=O(\rho^4).
\]

This is the precise form of the iteration statement.

---

## 6. Şuvaina’s class-\(T\) and Wahl metrics

The primary source establishes:

- Theorem A: every nearby fibre of a one-parameter \(\mathbb Q\)-Gorenstein smoothing of an isolated quotient surface singularity carries an ALE Ricci-flat Kähler metric in every Kähler class.
- Definition 1.1 records
  \[
  g-h_0=O(r^{-4}),\qquad J-J_0=O(r^{-4}).
  \]
  The printed definition does not explicitly write estimates for \(\partial^jg\).

For cyclic class-\(T\) singularities
\[
\frac1{dn^2}(1,dnm-1),
\]
Şuvaina identifies the smoothing as a free \(\mathbb Z_n\)-quotient of an \(A_{dn-1}\) smoothing and constructs the metric from a finite-centre Hitchin/Gibbons–Hawking metric. On the cover,
\[
V(x)=\frac12\sum_{\alpha=1}^{dn}\frac1{|x-x_\alpha|}.
\]
After translating the centre set so that
\[
\sum_\alpha x_\alpha=0,
\]
the multipole expansion gives, for the three-dimensional radius \(\varrho=|x|\),
\[
V=\frac{dn}{2\varrho}+O(\varrho^{-3}),
\qquad
\partial^m\!\left(V-\frac{dn}{2\varrho}\right)
 =O(\varrho^{-3-m})
\]
for every fixed \(m\). The dipole term is absent because of the recentering.

The four-dimensional cone radius satisfies
\[
R^2\asymp\varrho.
\]
Thus the relative metric perturbation is
\[
O(\varrho^{-2})=O(R^{-4}),
\]
and differentiating the explicit harmonic and connection formulas gives
\[
|\partial^j(h-\delta)|
 \le C_jR^{-4-j}.
\]
The finite free quotient preserves these estimates.

For a Wahl singularity, \(d=1\), the centres form a regular \(n\)-gon and already have zero centre of mass. For general class-\(T\) smoothings, the centres form \(d\) regular \(n\)-gons; translation along their common axis removes the remaining centre-of-mass term. Therefore the Milnor-fibre metrics used in Lemmas 86.S and 86.S′ satisfy the required derivative-controlled order-four asymptotics, in particular for \(j=0,1,2\).

The strongest wording should therefore be:

> Şuvaina’s printed ALE definition records order-four metric decay. The derivative-controlled order-four form required by the cutoff proof follows from her explicit finite-centre Hitchin/Gibbons–Hawking construction.

For \(\tau=4\), the balanced radius is
\[
\rho=\varepsilon^{2/3}.
\]

---

## 7. Corrected form of Lemma 86.S

A precise version is:

> **Lemma 86.S.** Let \((V,g)\) be a compact oriented four-orbifold with finitely many isolated points \(p_j\), locally modeled on \(\mathbb R^4/\Gamma_j\), with \(\Gamma_j\) acting freely on \(S^3\). Assume \(R(g)>0\). For every \(j\), let \((N_j,h_j)\) be a Ricci-flat ALE space with the matching end and
> \[
> |\partial^\ell(h_j-\delta)|
> \le C r^{-\tau_j-\ell},
> \qquad \ell=0,1,2,
> \]
> for some \(\tau_j>0\). Glue \(\varepsilon_j^2h_j\) using
> \[
> \rho_j=\varepsilon_j^{\tau_j/(\tau_j+2)}.
> \]
> Then on the smooth resolution \(M\),
> \[
> \begin{aligned}
> V(g_\varepsilon)&=V(g)+O(E_\varepsilon),\\
> S(g_\varepsilon)&=S(g)+O(E_\varepsilon),\\
> R(g_\varepsilon)&=R(g)+O(E_\varepsilon),\\
> P(g_\varepsilon)&=P(g)+O(E_\varepsilon),\\
> L_s(g_\varepsilon)&=L_s(g)+O(E_\varepsilon),
> \end{aligned}
> \qquad
> E_\varepsilon=\sum_j\rho_j^4,
> \]
> and
> \[
> \mathscr D(g_\varepsilon)
> =\mathscr D(g)+O(E_\varepsilon).
> \]
> If \(g\) is Einstein with \(\Lambda\ne0\), then
> \[
> P(g_\varepsilon)+L_s(g_\varepsilon)=O(E_\varepsilon),
> \qquad
> \mathscr D(g_\varepsilon)=O(E_\varepsilon).
> \]
> Finite orbifold ALE trees are included when the sum of the relative inner-neck energies also tends to zero.

Add separately:

> If \(g\) is Ricci-flat and all fillers are Ricci-flat, the same construction gives
> \[
> P(g_\varepsilon)\to0,\qquad
> \mathscr D(g_\varepsilon)\to4.
> \]

---

## 8. Lemma 86.S′ and its denominator case

Let \(N_j\) be scalar-flat ALE or AE bubbles with
\[
Q=\sum_jP(N_j)<\infty.
\]
Since \(s_{N_j}=0\),
\[
R(N_j)=P(N_j).
\]
The same cutoff calculation gives
\[
\begin{aligned}
V(g_\varepsilon)&\to V(g),\\
S(g_\varepsilon)&\to S(g),\\
\int s_{g_\varepsilon}^2&\to\int s_g^2,\\
P(g_\varepsilon)&\to P(g)+Q,\\
R(g_\varepsilon)&\to R(g)+Q,\\
L_s(g_\varepsilon)&\to L_s(g).
\end{aligned}
\]
For an order-\(\tau\) bubble, the omitted tail satisfies
\[
\int_{R>\rho/\varepsilon}|\operatorname{Ric}|^2
 =O\!\left((\varepsilon/\rho)^{2\tau}\right)
 =O(\rho^4)
\]
at the balanced radius. The annular interaction is also \(O(\rho^4)\). Thus no interaction survives in the limit; finite-scale terms such as the Burns response vanish with the insertion scale.

If
\[
R(g)+Q>0,
\]
then
\[
\boxed{
\mathscr D(g_\varepsilon)\longrightarrow
\frac{4P(g)+L_s(g)+4Q}{R(g)+Q}
=
4-\frac{S(g)^2}{V(g)\,[R(g)+Q]}.
}
\]

### Zero denominator

If
\[
R(g)+Q=0,
\]
then \(g\) is Ricci-flat and every scalar-flat bubble has \(P(N_j)=0\), hence is Ricci-flat. The displayed fraction is \(0/0\) and must not be used. For the standard local cutoff family, the argument from Section 4 gives
\[
\boxed{\mathscr D(g_\varepsilon)\to4.}
\]

### Minimal analytic assumptions

For the defect limit itself, the essential convergence relations are
\[
V(g_\varepsilon)\to V(g),\qquad
S(g_\varepsilon)\to S(g),\qquad
R(g_\varepsilon)\to R(g)+Q,
\]
together with \(R(g)+Q>0\). The stronger \(P\), scalar-square, and variance relations explain the displayed energy ledger term by term.

---

## 9. What Lemma 86.S′ says about zero defect

When \(R(g)+Q>0\), all terms in
\[
4P(g)+L_s(g)+4Q
\]
are \(\ge0\). Therefore the limiting defect is zero exactly when
\[
P(g)=0,\qquad L_s(g)=0,\qquad Q=0.
\]
Thus the compact bulk is Einstein with constant scalar curvature. Since the denominator is positive, its Einstein constant is nonzero. Every scalar-flat bubble has \(P(N_j)=0\), hence is Ricci-flat.

Accordingly, for this class of glued constructions, a zero defect arises precisely from a nonzero-scale Einstein bulk together with Ricci-flat bubbles.

---

## 10. Standard glued families versus arbitrary degenerations

Lemma 86.S′ is a construction theorem for metrics assembled by controlled cutoffs. It is not an energy-identity theorem for every sequence that develops bubbles.

For an arbitrary degenerating sequence, the displayed ledger additionally requires:

- convergence of the bulk volume and total scalar integral;
- no retained scalar-square energy on necks;
- no retained trace-free Ricci energy outside the listed bubbles;
- identification of every concentration component;
- no collapsed component carrying curvature energy not represented by the bulk and bubbles.

Without those properties, extra neck or concentration energy enters \(R\), \(P\), or \(\int s^2\), and the displayed formula changes. The standard cutoff construction has none of these surviving terms because every transition contribution is \(o(1)\).

---

## 11. Numerical file `step86_lemma86S_check.py`

The script correctly verifies the model curvature conventions:
\[
(s,|\operatorname{Ric}|^2)=
(0,0)\ \text{for flat and EH},\qquad
(12,36)\ \text{for the round metric}.
\]
Its round reference values, with the common angular factor omitted, are
\[
V=\frac1{12},\qquad
\int s=1,\qquad
\int|\operatorname{Ric}|^2=3.
\]

For the order-four choice \(\rho=a^{2/3}\), the data give
\[
\mathscr D=
0.07810,\ 0.01281,\ 0.002043,\ 0.0003231
\]
at \(a=0.1,0.05,0.025,0.0125\). The fitted exponent is \(2.6400\), close to
\[
\frac83=2.666\ldots,
\]
and \(\mathscr D/\rho^4\) approaches approximately \(38\). This is consistent with the proved \(O(\rho^4)=O(a^{8/3})\) law.

The integration and cutoff derivatives are floating-point computations, so this file is supporting numerical evidence rather than an interval proof. The symbolic exact-profile evaluations and the asymptotic trend are internally consistent.