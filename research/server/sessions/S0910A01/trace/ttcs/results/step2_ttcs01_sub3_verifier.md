# TTCS Independent Branch Record

```json
{
  "step_id": 2,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step2_mechanisms_analysis.md",
    "Knowledge/objects/papers/ALMOST-EINSTEIN-MANIFOLDS-OF-NEGATIVE-RICCI--c331e7060106--bcf9bda031d7/object.md",
    "Knowledge/objects/papers/4-Manifolds-without-Einstein-Metrics--c95911daf050--cd7839b9cc3d/object.md"
  ]
}
```

## Task

Verify the following quantitative analysis for Yau Problem 26:

1. MIN-OO CORRECTION: The condition in Min-Oo 1990 (JDG 32, 457-472) is d²·max|K| < Λ² (diameter-curvature product, scale-invariant), NOT r⁻²·max|K|. Check this against the OCR source: §3 normalization reads 'max|K(0)| = 1, d(0) < Λ'. Under g→λg: d²K → d²K (invariant) vs r⁻²K → λ(r⁻²K) (not invariant).

2. POSITIVE BRANCH BOUND: For M = X#k CP̄² (LeBrun no-Einstein, 2A/3 < k < A, A=c₁²(X)), combining: (i) LeBrun ∫s²dV ≥ 32π²A, (ii) CGB(+): 4π²(A-k) = ∫[2|W⁺|² + s²/24 - |E|²/2]dV, (iii) Bishop-Gromov V ≤ 24π²/(1-δ)² for σ=+1 gives 12δ²/(1-δ)² ≥ k-2A/3, hence δ_+ ≥ 1/7 uniformly. But stronger: non-trivial SW on LeBrun manifolds prevents s > 0, so δ_+ ≥ 1.

3. NEGATIVE BRANCH: Same integral bound gives δ² ≥ (k-2A/3)/(3(A-k)) using V ≤ 4π²(A-k)/f(δ) from CGB. For varying manifolds with A→∞, this → 0. Check the derivation chain and whether the constants are correct.

4. Verify that the structural asymmetry (positive has Myers+BG+SW control, negative has none) is correctly stated and that no additional constraint on the negative branch has been overlooked.

## Output

# Scientific verification memo

Assume throughout that \(\delta_\sigma(g)\) denotes eigenvalue pinching:
\[
\delta_\sigma(g)=\sup_{x\in M}\max_i |\rho_i(x)-\sigma|,
\]
where \(\rho_i\) are the eigenvalues of \(\operatorname{Ric}_g\) relative to \(g\). In dimension four, with \(E=\operatorname{Ric}-\frac{s}{4}g\),
\[
|E|^2=\sum_i(\rho_i-\bar\rho)^2
\le \sum_i(\rho_i-\sigma)^2\le 4\delta_\sigma^2.
\]

## 1. Min-Oo’s geometric hypothesis

The correction to
\[
d^2\max |K|<\Lambda^2
\]
is correct.

The source defines \(d\) as diameter and \(r\) as average scalar curvature. Its OCR-corrupted hypothesis `rf 2max|K|<Λ 2` is resolved by equation (3.01), where the normalized conditions are
\[
\max |K(0)|=1,\qquad d(0)<\Lambda.
\]
Indeed, starting from a metric with \(\max|K|=L>0\), the homothety \(\widehat g=L g\) gives
\[
\max|K_{\widehat g}|=1,\qquad
d_{\widehat g}=\sqrt{L}\,d_g,
\]
so \(d_{\widehat g}<\Lambda\) is exactly \(d_g^2L<\Lambda^2\).

Under \(g\mapsto\lambda g\),
\[
d\mapsto\lambda^{1/2}d,\qquad
K\mapsto\lambda^{-1}K,\qquad
r\mapsto\lambda^{-1}r.
\]
Consequently,
\[
d^2\max|K|\mapsto d^2\max|K|,
\]
whereas
\[
r^{-2}\max|K|\mapsto
(\lambda^{-1}r)^{-2}\lambda^{-1}\max|K|
=\lambda r^{-2}\max|K|.
\]
Thus the latter expression cannot be the theorem’s normalized geometric quantity.

There is also a likely OCR error in the dimension symbol. The OCR reads \(n>3\), but the theorem is immediately followed by a discussion of dimension three, and the Basic Lemma separately treats \(n=3\). The symbols displayed as \(n>3\) and \(n>4\) are therefore strongly indicated to be \(n\ge3\) and \(n\ge4\), respectively. The native PDF glyph was not acquired in the supplied object, so this particular symbol is not directly visible there.

For \(\sigma=-1\) pinching, let \(a=-r/n\). Then \(a\in[1-\delta,1+\delta]\), and for every unit vector,
\[
\left|\frac{n\,p}{r}-1\right|
=\left|\frac{-p}{a}-1\right|
\le \frac{2\delta}{1-\delta}.
\]
Hence a no-Einstein sequence with \(\delta\to0\) must satisfy
\[
d^2\max|K|\longrightarrow\infty;
\]
otherwise a bounded subsequence would eventually satisfy Min-Oo’s theorem.

## 2. The \(\sigma=+1\) estimate

Put
\[
A=c_1^2(X),\qquad B=A-k,\qquad q=k-\frac{2A}{3}>0.
\]
LeBrun’s Theorem 2 actually gives the strict estimate
\[
\int_M s^2\,dV>32\pi^2A.
\]
His Chern–Gauss–Bonnet/signature formula gives
\[
4\pi^2B
=\int_M\left(2|W^+|^2+\frac{s^2}{24}-\frac{|E|^2}{2}\right)dV.
\]
Dropping \(2|W^+|^2\) and inserting the scalar estimate yields
\[
4\pi^2B>\frac{4\pi^2A}{3}-\frac12\int_M|E|^2dV,
\]
and therefore
\[
\int_M|E|^2dV>8\pi^2q. \tag{2.1}
\]

If \(\delta=\delta_+(g)<1\), then
\[
\operatorname{Ric}\ge(1-\delta)g
=3\left(\frac{1-\delta}{3}\right)g.
\]
Myers and Bishop comparison give
\[
\operatorname{diam}(M)\le
\pi\sqrt{\frac{3}{1-\delta}},
\]
and
\[
V(M,g)\le
\operatorname{Vol}\!\left(S^4_{\kappa}\right),
\qquad \kappa=\frac{1-\delta}{3}.
\]
Since \(\operatorname{Vol}(S^4_1)=8\pi^2/3\),
\[
V(M,g)\le \frac{8\pi^2}{3}\kappa^{-2}
=\frac{24\pi^2}{(1-\delta)^2}. \tag{2.2}
\]
Combining (2.1), \(|E|^2\le4\delta^2\), and (2.2),
\[
8\pi^2q
<\int|E|^2
\le4\delta^2V
\le\frac{96\pi^2\delta^2}{(1-\delta)^2},
\]
so
\[
q<\frac{12\delta^2}{(1-\delta)^2}. \tag{2.3}
\]

Because \(A,k\in\mathbb Z\) and \(k>2A/3\),
\[
q\ge\frac13.
\]
Equation (2.3) then gives
\[
\frac{\delta}{1-\delta}>\frac16,
\qquad\text{hence}\qquad
\delta>\frac17.
\]
Using the weakened non-strict scalar estimate gives the stated \(\delta_+\ge1/7\).

### Seiberg–Witten strengthening

The conclusion
\[
\delta_+(g)\ge1
\]
is valid for the LeBrun manifolds under discussion.

If \(\delta_+(g)<1\), then
\[
s_g\ge4(1-\delta_+(g))>0.
\]
LeBrun’s proof chooses, for the polarization \(H^+(g)\), a spin\(^c\) structure with nonzero Seiberg–Witten invariant and \(c_1^+\ne0\). The Seiberg–Witten Weitzenböck identity has the form
\[
0=\int_M
\left(4|\nabla_A\Phi|^2+s|\Phi|^2+|\Phi|^4\right)dV
\]
up to normalization conventions. If \(s>0\), it forces \(\Phi=0\). The remaining equation \(F_A^+=0\) would imply \(c_1^+=0\), contradicting the selected class. For \(b^+=1\), this statement must be phrased with LeBrun’s metric-dependent polarization; his proof supplies precisely that polarization.

Thus these manifolds carry no metric with scalar curvature everywhere positive, and every metric satisfies \(\delta_+(g)\ge1\).

## 3. The \(\sigma=-1\) calculation

For \(\delta=\delta_-(g)<1\),
\[
s\le-4(1-\delta),\qquad
s^2\ge16(1-\delta)^2,\qquad
|E|^2\le4\delta^2.
\]
The same Chern–Gauss–Bonnet formula therefore gives
\[
4\pi^2B\ge f(\delta)V,
\]
where
\[
f(\delta)
=\frac{2}{3}(1-\delta)^2-2\delta^2
=\frac23(1-2\delta-2\delta^2). \tag{3.1}
\]
This produces
\[
V\le\frac{4\pi^2B}{f(\delta)} \tag{3.2}
\]
when
\[
f(\delta)>0
\quad\Longleftrightarrow\quad
\delta<\frac{\sqrt3-1}{2}
=\frac{1}{1+\sqrt3}. \tag{3.3}
\]

Combining (2.1), (3.2), and \(\int|E|^2\le4\delta^2V\) gives
\[
8\pi^2q
<\int|E|^2
\le\frac{16\pi^2B\delta^2}{f(\delta)}.
\]
Equivalently,
\[
q(1-2\delta-2\delta^2)<3B\delta^2. \tag{3.4}
\]

The formula
\[
\delta^2\ge\frac{q}{3B}
\]
does **not** follow as an exact finite-\(\delta\) inequality. It results from replacing \(f(\delta)\) by its leading value \(2/3\). The exact quadratic obtained from (3.4) is
\[
(A-q)\delta^2+2q\delta-q>0,
\]
because \(2q+3B=A-q\). Its positive root is
\[
\boxed{\;
\delta_0
=\frac{\sqrt{Aq}-q}{A-q}
=\frac{\sqrt q}{\sqrt A+\sqrt q}.
\;} \tag{3.5}
\]
For \(\delta\) satisfying (3.3), equation (3.4) gives \(\delta>\delta_0\). If \(\delta\ge1/(1+\sqrt3)\), the same conclusion is automatic because \(0<q<A/3\) implies
\[
\delta_0<\frac{1}{1+\sqrt3}.
\]
Thus the rigorous global estimate from this chain is
\[
\boxed{\;
\delta_-(g)>
\frac{\sqrt{k-2A/3}}
{\sqrt A+\sqrt{k-2A/3}}.
\;} \tag{3.6}
\]

If \(\varepsilon=q/B\to0\), then
\[
\delta_0^2
=\frac{\varepsilon}
{3+4\varepsilon+2\sqrt{3\varepsilon(1+\varepsilon)}}
=\frac{\varepsilon}{3}
\left(1-\frac{2}{\sqrt3}\sqrt\varepsilon+O(\varepsilon)\right).
\]
Hence
\[
\delta_0^2\sim\frac{q}{3B},
\]
but the right-hand side is slightly larger than \(\delta_0^2\) at finite \(A,k\).

For the numerical examples:

- \(A=100,\ k=67,\ q=1/3\):
  \[
  \delta_0=\frac{\sqrt{1/3}}{10+\sqrt{1/3}}
  \approx0.0546,
  \]
  rather than the approximate \(0.058\).

- \(A=10000,\ k=6668,\ q=4/3\):
  \[
  \delta_0\approx0.01142.
  \]

For the smallest integer \(k\) satisfying the strict inequality \(k>2A/3\),
\[
k_{\min}=\left\lfloor\frac{2A}{3}\right\rfloor+1,
\]
not \(\lceil2A/3\rceil+1\) in general. The corresponding \(q\) is \(1\), \(1/3\), or \(2/3\), according to \(A\bmod3\). Thus
\[
\delta_0=O(A^{-1/2})\longrightarrow0.
\]
This is a lower estimate tending to zero; it does not provide metrics realizing such pinching.

## 4. Geometric asymmetry and surviving \(\sigma=-1\) information

The main asymmetry is correct:

- For \(\sigma=+1\) and \(\delta<1\), Myers supplies a diameter upper bound and Bishop supplies a dimension-only volume upper bound after normalization.
- For \(\sigma=-1\), Ricci pinching alone supplies neither type of global upper bound.

A concrete demonstration comes from finite covers of a closed hyperbolic manifold. If \(g\) has sectional curvature \(-1\), then
\[
\operatorname{Ric}_g=-(n-1)g.
\]
For \(h=(n-1)g\),
\[
\operatorname{Ric}_h=-h.
\]
Finite connected covers retain this exact Ricci equation, while their volumes multiply by the covering degree. Their diameters cannot remain uniformly bounded, since a Ricci lower bound together with a fixed diameter would give a volume upper bound by Bishop comparison. Thus even exact \(\operatorname{Ric}=-g\) does not control total volume or diameter.

The word “none” would nevertheless be too broad. The supplied equations retain several substantial constraints on the \(\sigma=-1\) side:

1. **Min-Oo:** bounded \(d^2\max|K|\) plus sufficiently small Ricci deviation produces an Einstein metric.

2. **Four-dimensional topology:** for either sign,
   \[
   4\pi^2(2\chi\pm3\tau)\ge f(\delta)V.
   \]
   When \(f(\delta)>0\), this yields
   \[
   2\chi>3|\tau|.
   \]

3. **Seiberg–Witten scalar estimates:** \(s<0\) does not force monopole solutions to vanish, but LeBrun’s \(L^2\)-scalar estimate still gives the lower bound (2.1).

4. **Local Bishop comparison:** the Ricci lower bound controls volumes of metric balls relative to the corresponding model. It does not become a topology-independent total-volume estimate without a diameter input.

5. **Weyl curvature:** in dimensions \(n\ge4\), Ricci pinching controls the scalar and trace-free Ricci pieces but not \(W\):
   \[
   \mathrm{Rm}
   =W+\frac{1}{n-2}E\owedge g
     +\frac{s}{2n(n-1)}g\owedge g.
   \]
   Hence \(\max|K|\) is not controlled by \(\delta_-\). In dimension three \(W=0\), so Ricci pinching does control the full curvature tensor; diameter growth remains available there.

Finally, the supplied note contains one logical inconsistency. If
\[
Q_n\Longleftrightarrow P_n^+\lor P_n^-
\]
is the intended equivalence, then for fixed \(n\), either \(P_n^+\) or \(P_n^-\) establishes \(Q_n\); proving both is stronger. Making \(Q_n\) false requires both branch statements to be false.