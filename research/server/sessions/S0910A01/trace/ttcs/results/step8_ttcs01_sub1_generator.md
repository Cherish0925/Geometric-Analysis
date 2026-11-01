# TTCS Independent Branch Record

```json
{
  "step_id": 8,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md",
    "Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md"
  ]
}
```

## Task

Using the Step 8 measure-local theorem and the Naber-Zhang collapsed regularity framework, propose the strongest mathematically precise next route for extending the Derdziński contradiction through local unwrapping of collapsed neighborhoods. Focus on what hypotheses would let small mean LeBrun deficits transfer to noncollapsed local covers with bounded multiplicity or controlled measure distortion, how maximal nilpotency-rank assumptions enter, and what collapse mechanisms remain outside such a route. Do not claim a full collapse classification; give testable lemmas or reductions that could materially advance Yau 26.

## Output

Let  

\[
F_i=|\operatorname{Ric}_{g_i}+g_i|^2+
(s_i+8\sqrt6|W_i^+|)^2+\xi_i(Q_i+P_i)\ge 0
\]

be the Step 8 LeBrun deficit density, with

\[
\fint_{M_i}F_i\,d\mu_i\to0,\qquad 
\|\operatorname{Ric}_{g_i}+g_i\|_{L^\infty}\to0 .
\]

The strongest next route is to isolate a class of collapsed points for which the local universal cover is both analytically usable by Naber–Zhang and measure-compatible with the base averaging. Then Step 8’s Derdziński contradiction repeats verbatim on the cover.

---

## 1. The right local transfer hypothesis

Let \(\pi:\widehat{B_{2R}(p)}\to B_{2R}(p)\) be the local universal or normal cover, \(\hat p\) a lift, and \(0<a<1\). Define the normalized lifted-ball pushforward

\[
\nu_{\hat p,aR}
=
{\pi_*(1_{B_{aR}(\hat p)}\,d\hat\mu)\over
\operatorname{Vol}_{\hat g}B_{aR}(\hat p)} .
\]

For any \(\phi\ge0\),

\[
\fint_{B_{aR}(\hat p)}\pi^*\phi\,d\hat\mu
=
\int_{B_{2R}(p)}\phi\,d\nu_{\hat p,aR}.
\]

Thus the exact measure condition needed is one of the following equivalent or nested forms.

### Relative multiplicity form

If \(m_{\hat p,aR}(x)=\#(\pi^{-1}(x)\cap B_{aR}(\hat p))\), require

\[
m_{\hat p,aR}(x)
\le
L\,{\operatorname{Vol}_{\hat g}B_{aR}(\hat p)\over
\operatorname{Vol}_{g}B_{\sigma R}(p)}
\quad\text{for a.e. }x\in B_{\sigma R}(p),
\]

with \(\pi(B_{aR}(\hat p))\subset B_{\sigma R}(p)\), \(\sigma\sim a\). Then

\[
\fint_{B_{aR}(\hat p)}\pi^*\phi
\le
L\,\fint_{B_{\sigma R}(p)}\phi .
\]

The absolute multiplicity may diverge under collapse; the useful quantity is multiplicity divided by its natural average.

### Maximal-kernel form

A more flexible condition is

\[
\fint_{B_{aR}(\hat p)}\pi^*\phi
\le
L\,\mathcal M_R\phi(p),
\qquad
\mathcal M_R\phi(p)=\sup_{0<r\le R}\fint_{B_r(p)}\phi .
\]

This allows the pushforward kernel to be mildly concentrated near \(p\), as long as it is dominated by a dyadic radial kernel. It is robust for arbitrary \(L^1\) densities \(F_i\), where weak convergence of kernels alone would not be enough because \(F_i\) may concentrate.

Bishop–Gromov gives the local weak type estimate

\[
{\operatorname{Vol}\{p:\mathcal M_R F_i(p)>\alpha\}\over \operatorname{Vol}M_i}
\le
{C(4,R)\over \alpha}\fint_{M_i}F_i\to0 .
\]

Hence any subset occupying a fixed fraction of total volume contains points with \(\mathcal M_R F_i(p_i)\to0\).

---

## 2. Accessible-collapse exclusion theorem

Fix \(R_0>0\), \(\rho>0\), \(L<\infty\). Call \(p\in M_i\) unwrap-accessible if for some \(R\in[R_0,1]\) and some \(k\le3\):

1. **Model control.**
   \[
   d_{GH}\bigl(B_{2R}(p),B_{2R}(0^{k-\ell},z^\ell)\bigr)<\delta R,
   \]
   where \(\dim Z^\ell=\ell\le3\) and the Naber–Zhang model noncollapse radius satisfies \(r_c(z^\ell)\ge\rho\).

2. **Maximal fibered rank.**
   \[
   \operatorname{rank}\operatorname{Image}\bigl[
   \pi_1(B_{\delta R}(p))\to \pi_1(B_{2R}(p))
   \bigr]=4-k .
   \]

3. **Transfer.** For a lift \(\hat p\) to the local cover,
   \[
   \fint_{B_{aR}(\hat p)}\pi^*\phi
   \le
   L\,\mathcal M_R\phi(p)
   \quad\text{for all }\phi\ge0,
   \]
   with \(a<a_0(4,\rho)\) chosen below the Naber–Zhang harmonic-radius scale.

Then, along any Step 8 LeBrun near-equality sequence,

\[
{\operatorname{Vol}\{p:\ p\text{ unwrap-accessible}\}\over \operatorname{Vol}M_i}\to0 .
\]

Indeed, if this set had volume fraction \(\ge\eta>0\), the local maximal estimate gives \(p_i\) in it with \(\mathcal M_{1}F_i(p_i)\to0\). Transfer gives

\[
\fint_{B_{aR_i}(\hat p_i)}\pi_i^*F_i\to0 .
\]

Naber–Zhang Theorem 5.1 and Proposition 6.4, using the maximal rank \(4-k\) and \(\ell\le3\), give a uniform harmonic-radius lower bound on the cover:

\[
r_h(\hat p_i)\ge h_0(4,\rho)R_i\ge h_0R_0>0 .
\]

In harmonic coordinates on a smaller lifted ball, the Step 8 finite-\(W^{2,p}\) passage applies to the pulled-back metrics. A subsequence converges strongly in \(W^{2,p}\), \(p>2\), to a smooth Einstein metric

\[
\operatorname{Ric}_{g_\infty}=-g_\infty .
\]

The vanishing of the three terms in \(\pi_i^*F_i\) yields

\[
s_\infty=-4,\qquad |W_\infty^+|={1\over 2\sqrt6},\qquad
\operatorname{spec}(W_\infty^+)=
\left({1\over12},{1\over12},-{1\over6}\right).
\]

Since \(g_\infty\) is Einstein, \(\delta W_\infty^+=0\). Derdziński’s Proposition 5 applies: the conformal Kähler factor \((24|W_\infty^+|^2)^{1/3}\) is constant, so \(g_\infty\) is locally Kähler. But a Kähler–Einstein four-metric with \(\operatorname{Ric}=-g\) has

\[
|W^+|^2={2\over3},
\]

not \(1/24\). This is the same contradiction as Step 8.

So the entire collapsed extension reduces to proving the transfer estimate for large classes of maximal-rank collapse.

---

## 3. The key Naber–Zhang-to-transfer lemma to prove

The most valuable lemma is a deck-orbit counting theorem.

### Deck-orbit counting lemma

Let \((M_i^4,g_i,p_i)\) satisfy \(|\operatorname{Ric}|\le3\) and

\[
d_{GH}(B_{2R}(p_i),B_{2R}(0^{k-\ell},z_i^\ell))\to0,
\qquad
r_c(z_i^\ell)\ge\rho,
\qquad
k\le3,\ \ell\le3.
\]

Assume

\[
\operatorname{rank}\Gamma_{\delta R}(p_i)=4-k .
\]

Let \(\pi_i:\widehat{B_{2R}(p_i)}\to B_{2R}(p_i)\) be the local universal cover. Then for every fixed \(a<a_0(4,\rho)\),

\[
\pi_{i*}\left(
{1_{B_{aR}(\hat p_i)}d\hat\mu_i\over
\operatorname{Vol}B_{aR}(\hat p_i)}
\right)
\le
C(4,\rho,a)\,
{1_{B_{a'R}(p_i)}d\mu_i\over
\operatorname{Vol}B_{a'R}(p_i)}
+o_i(1)
\]

in the \(L^1\)-robust sense: equivalently,

\[
\fint_{B_{aR}(\hat p_i)}\pi_i^*\phi
\le
C(4,\rho,a)\fint_{B_{a'R}(p_i)}\phi+o_i(1)\mathcal M_R\phi(p_i)
\]

for every \(\phi\ge0\), with \(a'\sim a\). A dyadic version dominated by \(\mathcal M_R\phi(p_i)\) is equally useful.

Why maximal rank matters: Naber–Zhang’s algebraic construction gives graded short generators

\[
\sigma_{s,\alpha}
\]

for the nilpotent subgroup of the fibered group, with independent infinite cyclic factors totaling \(4-k\). Their powers move all points in a lifted ball by controlled amounts. In the equivariant limit, these generators produce a connected nilpotent Lie group orbit of dimension \(4-k\), exactly the missing dimension. The quotient by this orbit is the \(k\)-dimensional Ricci-limit model.

Thus the counting lemma is a quantitative lattice-counting statement for these graded deck transformations. The finite index \(w_0\) from Kapovitch–Wilking/Naber–Zhang only changes constants.

A model calculation supports the form. For

\[
B^k\times(\mathbb R^m/\varepsilon\mathbb Z^m),
\qquad m=4-k,
\]

the universal cover is \(B^k\times\mathbb R^m\). The pushforward of a lifted Euclidean ball has density

\[
\sim
{\omega_m(a^2R^2-|y|^2)_+^{m/2}\over
\varepsilon^m\,\omega_4(aR)^4},
\]

while

\[
\operatorname{Vol}B_{aR}(p_i)\sim \omega_k(aR)^k\varepsilon^m .
\]

The ratio is bounded by a constant depending only on \(k,m,a\). The nilpotent version should use Mal’cev coordinates and the graded generators from Naber–Zhang Section 4; Haar-volume comparison replaces the Euclidean lattice count.

---

## 4. Scientific payoff of the reduction

If the deck-orbit counting lemma is proved, then almost all volume in a Step 8 LeBrun near-equality sequence must avoid every fixed-scale, model-regular, maximal-rank collapse region. Equivalently, after removing \(o(\operatorname{Vol}M_i)\), every remaining collapsed point must exhibit at least one of the following mechanisms:

1. **Rank drop.**
   \[
   \operatorname{rank}\Gamma_{\delta R}(p)<4-k .
   \]
   The local cover does not recover all four dimensions. Singular fibers in torus-collapse models behave this way: one or more collapsed cycles vanish in the fibered fundamental group.

2. **No definite original scale.**  
   The usable unwrapping scale \(R_i\) tends to \(0\). After rescaling by \(R_i^{-2}\), the equation becomes Ricci-flat in the limit, and the calibrated LeBrun profile
   \[
   s=-4,\qquad |W^+|^2={1\over24}
   \]
   is no longer visible. The Derdziński contradiction is tied to the original normalization \(\operatorname{Ric}\approx-g\).

3. **Model degeneration.**  
   The Naber–Zhang constants may collapse through \(r_c(z_i)\to0\). This corresponds to base singularities or highly changing lower-dimensional models. A stratified version could handle fixed \(\rho\) first, then study what survives as \(\rho\downarrow0\).

4. **Four-dimensional bubble cores on covers.**  
   Naber–Zhang regularity uses residual dimension \(\ell\le3\). ALE/orbifold-type four-dimensional cores sit outside that input. Step 8 already permits \(o(\operatorname{Vol}M_i)\) noncollapsed islands, and such regions can still carry Euler or signature contribution.

5. **Uncontrolled lifted measure kernel.**  
   Even with maximal rank and cover noncollapse, the LeBrun deficit transfer can break if the lifted ball weights a tiny base subset far above its volume share. The deck-orbit counting lemma is precisely the mathematical object separating regular nil-collapse from such concentration.

This gives a sharp next target: prove relative multiplicity/equidistribution for Naber–Zhang maximal-rank collapse at fixed original scale. That would extend the Derdziński contradiction through the largest geometrically regular part of the collapsed regime, while reducing any surviving LeBrun sequence to rank-deficient fibers, model-degenerate strata, tiny-scale bubbles, or measure-distorted unwrapping.