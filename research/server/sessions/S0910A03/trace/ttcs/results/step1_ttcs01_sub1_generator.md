# TTCS Independent Branch Record

```json
{
  "step_id": 1,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/briefing/aligned_research_goal.md",
    "Sessions/S0910A03/workspace/briefing/Session.md",
    "Knowledge/objects/papers/The-Calabi-metric-and-desingularization-of-Einstein-orbifolds--3b9fd6e4b2cd--c8fe6b2cf08c/object.md",
    "Knowledge/objects/papers/Noncollapsed-degeneration-of-Einstein-4-manifolds-I--20d576a9333c--50e8cddb3834/object.md",
    "Knowledge/objects/papers/Integrability-of-Einstein-deformations-and-desingularizations--8e63541ce32f--b5af64ba3e90/object.md"
  ]
}
```

## Task

The active goal is to prove or refute the dimensionwise existence of a nondegenerate Ricci pinching interval forcing the underlying closed smooth manifold to admit some Einstein metric. Develop the strongest serious counterexample mechanisms suggested by Einstein-orbifold resolution/gluing. In particular, derive carefully whether the refined approximate metrics in Morteza–Viaclovsky can have unweighted operator norm |g_t^{-1}(Ric(g_t)-Lambda g_t)| tending to zero after all scalings, including the ALE core, transition annulus, and obstruction term. Then identify what topology/global theorem would be needed to exclude every Einstein metric, not just nearby ones. Explore concrete orbifold/resolution choices and compute chi,tau where feasible. Do not assume the route works; expose exact fatal points and possible repairs.

## Output

### 1. Homothetic logic for the Yau interval

For a constant rescaling \(\hat g=a g\),
\[
\operatorname{Ric}_{\hat g}=\operatorname{Ric}_g,\qquad 
\hat g^{-1}\operatorname{Ric}_{\hat g}=a^{-1}g^{-1}\operatorname{Ric}_g .
\]
Thus any fixed metric with bounded Ricci operator can be rescaled so that all Ricci eigenvalues lie in any interval containing \(0\). Therefore, in every dimension where some closed smooth manifold admits no Einstein metric, a valid forcing interval cannot cross \(0\). The serious cases are intervals entirely in \((0,\infty)\) or entirely in \((-\infty,0)\).

For a one-sided interval, a counterexample mechanism must produce on a non-Einstein smooth manifold metrics whose Ricci operator is not merely bounded, but lies in an arbitrarily narrow one-sided band after homothety. In practice this means a uniform almost-Einstein estimate
\[
\bigl\|g^{-1}(\operatorname{Ric}_g-\Lambda g)\bigr\|_{L^\infty}\to 0
\]
with \(\Lambda\neq 0\), or at least an eigenvalue ratio tending to \(1\). This is exactly where the Morteza–Viaclovsky obstruction term becomes decisive.

---

### 2. Unweighted Ricci operator for the Morteza–Viaclovsky refined metrics

Let \(m=2n\), \(n\ge 3\). In the ALE chart of the Calabi space \(X=\mathcal O(-n)\to \mathbb{CP}^{n-1}\), Morteza–Viaclovsky construct
\[
h_t=g_{\rm cal}+t h,
\]
where
\[
d_{g_{\rm cal}}\operatorname{Ric}(h)=\Lambda g_{\rm cal}+\lambda o,\qquad B_{g_{\rm cal}}h=0,
\]
and \(o\) spans the decaying infinitesimal Einstein deformations of \(g_{\rm cal}\):
\[
o=\frac{1}{1+r^{2n}}\Bigl(-\overline{g_{FS}}+(n-1)d\bar r^2+(n-1)\bar\theta^2\Bigr).
\]

The refined compact approximate metric \(g_t\) has three regions.

#### Outer orbifold region

Here \(g_t=g_0\), so
\[
\operatorname{Ric}_{g_t}-\Lambda g_t=0.
\]

#### ALE core

Here
\[
g_t=t h_t=t(g_{\rm cal}+t h).
\]
Since constant rescaling does not change Ricci as a \((0,2)\)-tensor,
\[
\operatorname{Ric}_{g_t}=\operatorname{Ric}_{h_t}.
\]
Morteza–Viaclovsky prove
\[
\bigl|\operatorname{Ric}_{h_t}-t\Lambda h_t-t\lambda o\bigr|_{g_{\rm cal}}
\le C t^2\rho^2,
\qquad \rho=\max(1,r).
\]
Therefore
\[
\operatorname{Ric}_{g_t}-\Lambda g_t=t\lambda o+R_t,
\qquad |R_t|_{g_{\rm cal}}\le C t^2\rho^2.
\]
Taking the Ricci operator with respect to \(g_t=t h_t\),
\[
g_t^{-1}(\operatorname{Ric}_{g_t}-\Lambda g_t)
=
\lambda h_t^{-1}o+t^{-1}h_t^{-1}R_t.
\]
On the whole ALE core \(r\le \tfrac12 t^{-1/4}\),
\[
\bigl|t^{-1}h_t^{-1}R_t\bigr|
\le C t\rho^2\le C t^{1/2}\to 0.
\]
But the obstruction part survives:
\[
\lambda h_t^{-1}o\to \lambda g_{\rm cal}^{-1}o
\]
on every compact subset of \(X\). The endomorphism \(g_{\rm cal}^{-1}o\) has eigenvalues
\[
-\frac1{1+r^{2n}}
\quad\text{on the horizontal } \mathbb{CP}^{n-1}\text{ directions},
\]
and
\[
\frac{n-1}{1+r^{2n}}
\quad\text{on the }(d\bar r,\bar\theta)\text{ directions}.
\]
Hence, if \(\lambda\neq0\),
\[
\sup_{\text{ALE core}}
\bigl|g_t^{-1}(\operatorname{Ric}_{g_t}-\Lambda g_t)\bigr|
\not\to 0.
\]
More precisely, near the zero section it stays comparable to \(|\lambda|\).

Thus the refined compact MV metric is not uniformly almost Einstein at nonzero scale whenever the first obstruction is nonzero.

#### Transition annulus

In the transition region
\[
r\sim t^{-1/4},\qquad g_t\sim t g_{\rm euc}.
\]
Morteza–Viaclovsky prove
\[
\bigl|\operatorname{Ric}_{g_t}-\Lambda g_t-t\lambda\chi_t o\bigr|_{g_{\rm cal}}
\le C t^2\rho^2.
\]
Taking the operator norm with \(g_t^{-1}\sim t^{-1}g_{\rm euc}^{-1}\),
\[
\bigl|g_t^{-1}(\text{remainder})\bigr|
\le C t\rho^2
\sim C t^{1/2}\to0.
\]
The obstruction term contributes
\[
g_t^{-1}(t\lambda\chi_t o)
\sim \lambda\chi_t\,g_{\rm euc}^{-1}o.
\]
But on the ALE end
\[
|g_{\rm euc}^{-1}o|\sim r^{-2n},
\]
so in the transition annulus
\[
|\lambda\chi_t g_{\rm euc}^{-1}o|
\lesssim |\lambda|t^{n/2}\to0.
\]
Thus the transition annulus is harmless in unweighted operator norm. The entire obstruction is concentrated, at operator level, on the compact ALE core.

#### Effect of an additional global homothety

If \(\hat g_t=a_t g_t\) and one compares with Einstein constant \(\Lambda/a_t\), then
\[
\hat g_t^{-1}\bigl(\operatorname{Ric}_{\hat g_t}-(\Lambda/a_t)\hat g_t\bigr)
=
a_t^{-1}g_t^{-1}(\operatorname{Ric}_{g_t}-\Lambda g_t).
\]
So \(a_t\to\infty\) makes the defect vanish, but simultaneously
\[
\hat g_t^{-1}\operatorname{Ric}_{\hat g_t}
=
a_t^{-1}g_t^{-1}\operatorname{Ric}_{g_t}
\to0.
\]
This only helps intervals containing \(0\). For a one-sided interval away from \(0\), the homothety scale must stay comparable to a fixed nonzero value, and the ALE-core obstruction remains visible.

---

### 3. What the obstruction does to the Ricci eigenvalues

On the ALE core,
\[
g_t^{-1}\operatorname{Ric}_{g_t}
=
\Lambda I+\lambda\,g_{\rm cal}^{-1}o+o(1).
\]
Near the zero section the limiting eigenvalues are
\[
\Lambda-\lambda
\quad\text{on }T\mathbb{CP}^{n-1},
\]
and
\[
\Lambda+(n-1)\lambda
\quad\text{on the two normal/Hopf directions}.
\]
Thus a one-sided positive pinching band requires
\[
\Lambda-\lambda>0,\qquad \Lambda+(n-1)\lambda>0,
\]
and an interval with \(C<0\) requires both inequalities reversed. If \(|\lambda|/|\Lambda|\) is not small, the core can even force mixed Ricci signs.

Using the projection normalization from Proposition 3.2,
\[
\|o\|_{L^2(g_{\rm cal})}^2=(n-1)\frac{\omega_{2n-1}}{n}.
\]
For a constant sectional curvature orbifold with sectional curvature \(K\),
\[
\Lambda=(2n-1)K,\qquad 
\langle \mathcal R(\omega),\omega\rangle=4nK,
\]
so the MV projection gives
\[
\lambda=-(n-1)K.
\]
Hence the ALE-core Ricci eigenvalues tend to
\[
(3n-2)K
\quad\text{and}\quad
\bigl(2n-1-(n-1)^2\bigr)K
=
(-n^2+4n-2)K.
\]
For real dimension \(6\) (\(n=3\)), these are \(7K\) and \(K\), so the ratio is already \(7\). For \(n\ge4\), the second eigenvalue is \(<0\) when \(K>0\). Thus the spherical football examples in real dimensions \(8,10,\dots\) do not give positive Ricci pinching at all in the refined MV metric; the ALE core has mixed Ricci signs.

For a compact Kähler–Einstein orbifold with \(\Lambda\neq0\), MV note
\[
\langle \mathcal R(\omega),\omega\rangle=2R=4n\Lambda.
\]
The same normalization gives
\[
\lambda=-\Lambda.
\]
The ALE-core Ricci eigenvalues tend to
\[
2\Lambda
\quad\text{and}\quad
(2-n)\Lambda.
\]
Thus for \(n\ge3\), a positive Kähler–Einstein orbifold produces mixed Ricci signs in the core after Calabi resolution, and similarly for \(\Lambda<0\) with signs reversed. These are strong local obstructions to using the obvious KE compact examples for one-sided pinching.

---

### 4. What would be needed to exclude every Einstein metric

The MV and Biquard–Ozuch obstructions exclude Einstein metrics arising from the specific orbifold-resolution degeneration, or from metrics close to the glued approximate metric in weighted norms. They do not by themselves rule out an unrelated Einstein metric on the same smooth manifold.

To turn this into a counterexample to the Yau statement, one needs a diffeomorphism-invariant theorem saying the resolved smooth manifold carries no Einstein metric at all.

In dimension four, the basic tool is Hitchin–Thorpe:
\[
2\chi(M)\ge 3|\tau(M)|
\]
for every closed oriented Einstein four-manifold. Equality has a rigid Ricci-flat half-conformally flat structure, so many equality cases are also excluded by Hitchin’s equality analysis.

Stronger tools include Seiberg–Witten/LeBrun inequalities, especially for manifolds of the form
\[
X\# k\overline{\mathbb{CP}}^{2}
\]
with \(X\) a minimal complex surface of general type and \(k\) large relative to \(c_1^2(X)\).

Without such a global topological theorem, one only obtains:
- no Einstein metric near the glued MV metric;
- no Einstein sequence degenerating to a prescribed obstructed orbifold in the Ozuch setting;
- but not “no Einstein metric on the smooth manifold”.

That is the main gap between local gluing obstructions and a full Yau-26 refutation.

---

### 5. Concrete topological computations

#### 5.1 Football \(S^4/\mathbb Z_k\)

Let \(\mathbb Z_k\) act on the first four coordinates of \(S^4\subset\mathbb R^5\), giving two \(A_{k-1}\)-type singularities. Replacing each cone point by the \(A_{k-1}\) plumbing increases Euler characteristic by \(k-1\). Since the underlying quotient has \(\chi=2\),
\[
\chi(M)=2+2(k-1)=2k.
\]

The signature depends on the chirality with which the two ALE fillings are glued. If the two chiralities cancel, then
\[
\tau(M)=0.
\]
If both contribute with the same sign, then formally
\[
\tau(M)=\pm 2(k-1).
\]
The natural football geometry pairs the two ends in opposite chiralities, so the useful HT-violating case is not obtained directly. If one could construct a positive Einstein orbifold with the same total ADE rank but same-chirality singularities, then Hitchin–Thorpe would become powerful:
\[
3\cdot 2(k-1)>2\cdot 2k
\quad\Longleftrightarrow\quad
k\ge4.
\]
So a same-chirality positive Einstein orbifold with two \(A_{k-1}\) singularities and \(k\ge4\) would be a very strong target. The missing object is the orbifold itself, not the topological calculation.

#### 5.2 \(S^{2n}/\Gamma_n\) in the MV higher-dimensional setting

For the real \(2n\)-dimensional football \(S^{2n}/\Gamma_n\), resolving each of the two singularities by the Calabi space \(\mathcal O(-n)\to\mathbb{CP}^{n-1}\) replaces a cone point of Euler characteristic \(1\) by a space retracting to \(\mathbb{CP}^{n-1}\), whose Euler characteristic is \(n\). Hence
\[
\chi(M)=2+2(n-1)=2n.
\]
There is no four-dimensional Hitchin–Thorpe obstruction in real dimension \(2n\ge6\). One would need a different global non-Einstein theorem, and none is supplied by the local MV obstruction.

#### 5.3 Kummer-type flat examples

The flat examples calibrate the construction but do not give counterexamples.

- \(T^4/\mathbb Z_2\) has \(16\) \(A_1\) singularities. The minimal resolution is K3:
  \[
  \chi=24,\qquad \tau=-16,
  \]
  and it admits Ricci-flat Kähler metrics.

- The MV example \(T^6/\mathbb Z_3\) has \(27\) \(\Gamma_3\) singularities. Replacing each singular point by \(\mathcal O(-3)\to\mathbb{CP}^2\) increases the topological Euler characteristic by \(2\) per point; the known crepant resolution is Calabi–Yau and admits Ricci-flat metrics. The MV obstruction vanishes because the orbifold germ is flat.

Thus flat orbifolds show how \(\lambda=0\) leads to genuine Einstein resolutions, not to non-Einstein topology.

#### 5.4 Weighted projective planes

For a weighted projective plane \(\mathbb{CP}^2_{(a,b,c)}\), let \(L\) be the total length of the Hirzebruch–Jung chains in its minimal resolution. The resolution is a rational surface with
\[
\chi=3+L,\qquad \tau=1-L.
\]
For \(L\ge2\),
\[
2\chi-3|\tau|
=
2(3+L)-3(L-1)
=
9-L.
\]
Thus \(L\ge10\) violates Hitchin–Thorpe, and \(L=9\) is also incompatible except in the rigid equality geometries.

This is topologically excellent. The geometric break point is local: Ricci-flat ALE gluing requires the local group to be of ADE type in dimension four. For positive Kähler–Einstein orbifolds with only Du Val singularities, the crepant resolution is a weak del Pezzo surface, forcing
\[
K^2=9-L>0,
\]
so \(L\le8\). Hence the HT-excluding weighted-projective resolutions typically involve non-ADE singularities, where the available ALE models are scalar-flat Kähler rather than Ricci-flat, and they cannot be inserted into an Einstein gluing with bounded Ricci operator after scaling.

#### 5.5 Hyperbolic four-orbifolds with \(A_1\) singularities

For compact \(K<0\) orbifolds with isolated \(A_1\) singularities, resolving by Eguchi–Hanson spaces gives natural metrics whose Ricci tensor is close to the hyperbolic value away from the ALE cores, while the obstruction concentrates on the cores. Ozuch’s theorem gives strong non-desingularization statements for spherical and hyperbolic orbifolds with \(A_1\) singularities.

But Hitchin–Thorpe usually does not exclude the resolved topology. In the clean all-same-chirality heuristic with \(N\) \(A_1\) points,
\[
\chi(M)\approx \chi_{\rm orb}+\frac32 N,\qquad \tau(M)\approx -N,
\]
so
\[
2\chi(M)-3|\tau(M)|\approx 2\chi_{\rm orb}>0.
\]
Thus one needs either a more delicate signature computation for a special orbifold or a Seiberg–Witten/LeBrun obstruction for the resolved smooth manifold.

---

### 6. Serious repair routes

The orbifold-gluing route becomes genuinely dangerous for Yau-26 only if one of the following can be realized.

#### A. Small nonzero first obstruction

Find a family of compact Einstein orbifolds with the same resolved smooth topology \(M\), Einstein constant \(\Lambda\neq0\), and MV obstruction coefficient
\[
\mathfrak o
=
n\langle\mathcal R(\omega),\omega\rangle+2(n-2)R
\]
arbitrarily small but nonzero at the singularity. Then the ALE-core eigenvalue spread becomes arbitrarily small:
\[
g_t^{-1}\operatorname{Ric}_{g_t}
=
\Lambda I+\lambda g_{\rm cal}^{-1}o+o(1),
\qquad |\lambda/\Lambda|\ll1.
\]
After homothety, this could fit any prescribed one-sided interval. The nonzero obstruction would still prevent the obvious Einstein desingularization, while a global theorem such as Hitchin–Thorpe or LeBrun would exclude unrelated Einstein metrics.

Needed source families: compact Einstein orbifolds with a tunable curvature tensor at a \(\Gamma_n\) singularity. Natural search directions are self-dual Einstein orbifolds, Page–Pope/Bérard-Bergery families, and weighted/quasi-smooth Einstein orbifolds with ADE points.

#### B. Vanishing first obstruction but higher obstruction or topology obstruction

If \(\lambda=0\), the refined MV metric satisfies
\[
\bigl\|g_t^{-1}(\operatorname{Ric}_{g_t}-\Lambda g_t)\bigr\|_{L^\infty}
=O(t^{1/2})\to0.
\]
This is the ideal Ricci-pinching mechanism. To make it refute Yau-26, the resolved smooth manifold must admit no Einstein metric. Then some higher obstruction or global obstruction must prevent exact Einstein desingularization.

Needed ingredients:
1. a compact Einstein orbifold with \(\mathfrak o=0\);
2. a Calabi/Eguchi–Hanson/ADE Ricci-flat resolution;
3. resolved topology excluded by HT or SW/LeBrun.

Flat Kummer examples satisfy (1) and (2), but not (3), since they are Ricci-flat. The missing examples are nonflat compact orbifolds with \(\mathfrak o=0\) and globally non-Einstein resolutions.

#### C. Same-chirality high-rank ADE singularities

In four dimensions, if an orbifold has underlying invariants \((\chi_0,\tau_0)\) and ADE fillings of total ranks \(r_i\) with signs \(\varepsilon_i=\pm1\), then a useful topological model is
\[
\chi(M)=\chi_0+\sum_i r_i,\qquad
\tau(M)=\tau_0-\sum_i\varepsilon_i r_i.
\]
Hitchin–Thorpe excludes Einstein metrics if
\[
3\left|\tau_0-\sum_i\varepsilon_i r_i\right|
>
2\left(\chi_0+\sum_i r_i\right).
\]
For \(\chi_0=2,\tau_0=0\), five same-chirality \(A_1\) singularities would already suffice. The hard part is finding a compact Einstein orbifold with isolated same-chirality ADE singularities and with a first obstruction that is zero or arbitrarily small.

---

### 7. Bottom line

The refined MV approximate metrics with nonzero first obstruction do **not** have
\[
\bigl|g_t^{-1}(\operatorname{Ric}_{g_t}-\Lambda g_t)\bigr|\to0
\]
at nonzero scale. The obstruction term disappears in the transition annulus but survives on the compact ALE core. For many natural positive or \(C<0\) orbifolds, it even forces mixed Ricci signs in real dimension at least six.

Therefore, the strongest counterexample route is not “take any obstructed MV desingularization.” It must add one of two missing pieces:

1. tune the first obstruction to zero or arbitrarily small while keeping a non-Einstein resolved topology; or  
2. find a global theorem excluding all Einstein metrics on the resolved manifold, plus enough Ricci eigenvalue control to fit any one-sided interval.

The most promising concrete four-dimensional topological targets are resolutions with many same-chirality ADE singularities or rational surfaces with \(L\ge9\) exceptional-chain length, because their \((\chi,\tau)\) can violate Hitchin–Thorpe. The main geometric obstacle is that known positive Einstein ADE orbifolds tend to have weak del Pezzo resolutions with \(L\le8\), while HT-excluding weighted-projective examples usually involve non-ADE local groups and hence lack Ricci-flat ALE bubbles.