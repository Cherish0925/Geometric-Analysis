# TTCS Independent Branch Record

```json
{
  "step_id": 3,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/Spin-Manifolds-Einstein-Metrics-and-Differential-Topology--c5d29fae197e--75ec82ead070/object.md",
    "Knowledge/objects/papers/Weyl-Curvature-Einstein-Metrics-and-Seiberg-Witten-Theory--010d90d7328e--6fed64eff4e5/object.md",
    "Knowledge/objects/papers/Four-Manifolds-Curvature-Bounds-and-Convex-Geometry--9dec43e67dff--ae37fe317499/object.md",
    "Knowledge/objects/papers/Curvature-Connected-Sums-and-Seiberg-Witten-Theory--7e92a6723434--2ac6d11897c5/object.md",
    "Sessions/S0910A03/workspace/notes/step2_corrected_prop4_analysis.tex"
  ]
}
```

## Task

We study Yau Problem 26 in dimension 4. For Ishida–LeBrun boundary manifolds M=(#_{j=1}^m X_j)#N with m=2 or 3, A=sum c1^2(X_j), and D=4m-(2χ+3τ)(N)=A/3, published Proposition 4 is strict for every metric but gives no uniform normalized gap. Assume a sequence g_i has ||Ric(g_i)+g_i||_op=δ_i→0. Derive the strongest consequences you can from the genuine scalar–Weyl inequality, Chern–Gauss–Bonnet, monopole sign choices/convex hull, and equality structure. Identify exactly what normalized energies, periods, spinors/forms, and concentration measures must converge; distinguish conclusions needing volume/noncollapse/Sobolev bounds. Explore whether there is a route to force a forbidden symplectic structure, or instead a plausible degeneration geometry. Do not use the false Weyl-only lower bound. Seek new rigorous lemmas or a sharp research formulation useful for resolving the negative branch.

## Output

### Setup and normalized quantities

Write  
\[
M=\Big(\#_{j=1}^m X_j\Big)\# N,\qquad m=2\ \text{or}\ 3,
\]
\[
A=\sum_{j=1}^m A_j,\qquad A_j=c_1^2(X_j)>0,
\]
and assume the equality-case Ishida–LeBrun number
\[
D:=4m-(2\chi+3\tau)(N)=A/3.
\]
Then
\[
(2\chi+3\tau)(M)=A-D=\frac{2A}{3}.
\]

For a metric \(g_i\), set
\[
S_i=\frac1{4\pi^2}\int_M\frac{s_i^2}{24}\,d\mu_i,\qquad
W_i^+=\frac1{4\pi^2}\int_M2|W_{+,i}|^2\,d\mu_i,
\]
\[
R_i=\frac1{4\pi^2}\int_M\frac{|\mathring{\mathrm{Ric}}_i|^2}{2}\,d\mu_i,
\qquad
I_i=S_i+W_i^+.
\]
Chern–Gauss–Bonnet gives
\[
I_i-R_i=\frac{2A}{3}. \tag{1}
\]

Also define the genuine scalar–Weyl quantity
\[
K_i=\frac1{72\pi^2}\int_M\bigl(s_i-\sqrt6\,|W_{+,i}|\bigr)^2\,d\mu_i.
\]
The algebraic inequality used in LeBrun’s scalar–Weyl estimate is
\[
I_i\ge \frac23 K_i, \tag{2}
\]
and Proposition 4 gives
\[
K_i\ge (a_i^+)^2
\]
for every monopole class \(a\), where \(a_i^+\) is the \(g_i\)-self-dual harmonic projection.

Everything below uses this \(K_i\)-inequality; no stand-alone lower estimate for \(W_+\) enters.

---

## 1. Consequences of \(\|\mathrm{Ric}_{g_i}+g_i\|_{\mathrm{op}}=\delta_i\to0\)

Let \(e_i=\mathrm{Ric}_{g_i}+g_i\). Its eigenvalues satisfy \(|e_{\alpha}|\le \delta_i\). Hence, for large \(i\),
\[
|s_i+4|\le 4\delta_i,\qquad s_i<0,
\]
and
\[
|\mathring{\mathrm{Ric}}_i|^2\le 4\delta_i^2.
\]
Since
\[
s_i^2\ge 16(1-\delta_i)^2,
\]
one has the ratio estimate
\[
R_i\le q_i S_i,\qquad q_i=\frac{3\delta_i^2}{(1-\delta_i)^2}\to0. \tag{3}
\]
Using \(S_i\le I_i\) and (1),
\[
I_i=\frac{2A}{3}+R_i\le \frac{2A}{3}+q_i I_i,
\]
so
\[
I_i\le \frac{2A/3}{1-q_i},\qquad R_i\to0. \tag{4}
\]
Therefore
\[
I_i\to \frac{2A}{3}. \tag{5}
\]

This is the first key point: an almost \(\mathrm{Ric}=-g\) sequence would force the Chern–Gauss–Bonnet identity to approach the Einstein equality value, even though no Einstein metric exists.

---

## 2. Period convergence from all monopole sign choices

Let \(c_j=c_1(X_j)\). Ishida–LeBrun/Bauer–Furuta gives monopole classes of the form
\[
a_{\varepsilon,\eta}
=
\sum_{j=1}^m \varepsilon_j c_j+\sum_{\ell=1}^k \eta_\ell E_\ell,
\qquad
\varepsilon_j,\eta_\ell\in\{\pm1\},
\]
where the \(E_\ell\) come from the \(b_+(N)=0\) summand and satisfy \(E_\ell^2=-1\), mutually orthogonally in the usual diagonal model.

For each \(g_i\), let \(v_i^+\) and \(v_i^-\) denote the self-dual and anti-self-dual harmonic projections. Average \((a_{\varepsilon,\eta,i}^+)^2\) over all sign choices. Cross terms cancel, giving
\[
2^{-(m+k)}\sum_{\varepsilon,\eta}(a_{\varepsilon,\eta,i}^+)^2
=
\sum_{j=1}^m (c_{j,i}^+)^2+\sum_{\ell=1}^k(E_{\ell,i}^+)^2.
\]
Since
\[
(c_{j,i}^+)^2=c_j^2+\|c_{j,i}^-\|^2=A_j+\|c_{j,i}^-\|^2,
\]
we get
\[
2^{-(m+k)}\sum_{\varepsilon,\eta}(a_{\varepsilon,\eta,i}^+)^2
=
A+
\sum_{j=1}^m\|c_{j,i}^-\|^2
+
\sum_{\ell=1}^k(E_{\ell,i}^+)^2. \tag{6}
\]

On the other hand, for every sign choice,
\[
I_i\ge \frac23(a_{\varepsilon,\eta,i}^+)^2.
\]
Thus
\[
\max_{\varepsilon,\eta}(a_{\varepsilon,\eta,i}^+)^2
\le \frac32 I_i
=
A+\frac32R_i. \tag{7}
\]
Combining (6) and (7),
\[
0\le 
\sum_{j=1}^m\|c_{j,i}^-\|^2
+
\sum_{\ell=1}^k(E_{\ell,i}^+)^2
\le \frac32 R_i\to0. \tag{8}
\]

So the period planes satisfy, quantitatively,
\[
c_{j,i}^-\to0\quad\forall j,
\qquad
E_{\ell,i}^+\to0\quad\forall \ell. \tag{9}
\]
Equivalently, the \(g_i\)-self-dual subspaces asymptotically contain the positive span of the \(c_j\)’s and become orthogonal to the \(N\)-classes.

In particular, for every monopole vertex,
\[
(a_{\varepsilon,\eta,i}^+)^2\to A, \tag{10}
\]
and for two vertices,
\[
a_{\varepsilon,\eta,i}^+\cdot a_{\varepsilon',\eta',i}^+
\to
\sum_{j=1}^m \varepsilon_j\varepsilon'_j A_j. \tag{11}
\]

---

## 3. Saturation of the scalar–Weyl inequality and exact energy limits

For every fixed monopole vertex \(a=a_{\varepsilon,\eta}\),
\[
I_i\ge \frac23K_i\ge \frac23(a_i^+)^2.
\]
Using (5) and (10),
\[
I_i\to\frac{2A}{3},\qquad K_i\to A,
\]
and both defects vanish:
\[
I_i-\frac23K_i\to0,\qquad K_i-(a_i^+)^2\to0. \tag{12}
\]

Since \(s_i<0\), write
\[
x_i=-s_i>0,\qquad w_i=|W_{+,i}|.
\]
The algebraic defect has the exact form
\[
I_i-\frac23K_i
=
\frac1{864\pi^2}\int_M\bigl(x_i-8\sqrt6\,w_i\bigr)^2\,d\mu_i. \tag{13}
\]
Thus
\[
\int_M\bigl(x_i-8\sqrt6\,w_i\bigr)^2\,d\mu_i\to0. \tag{14}
\]
But \(x_i\to4\) uniformly and the volumes are bounded by (4), hence
\[
|W_{+,i}|\to \frac1{2\sqrt6}
\quad\text{in }L^2(d\mu_i). \tag{15}
\]

Consequently
\[
W_i^+=\frac18 S_i+o(1).
\]
Since \(I_i=S_i+W_i^+\to2A/3\),
\[
S_i\to \frac{16A}{27},\qquad
W_i^+\to \frac{2A}{27}. \tag{16}
\]
Also
\[
\mathrm{Vol}(M,g_i)\to 6\pi^2\cdot \frac{16A}{27}
=
\frac{32\pi^2A}{9}. \tag{17}
\]

So an almost \(\mathrm{Ric}=-g\) sequence would have the rigid normalized energy profile
\[
\boxed{
R_i\to0,\quad
S_i\to\frac{16A}{27},\quad
W_i^+\to\frac{2A}{27},\quad
K_i\to A,\quad
\mathrm{Vol}_i\to\frac{32\pi^2A}{9}.
}
\]

For the opposite orientation,
\[
S_i+W_i^- -R_i=(2\chi-3\tau)(M),
\]
so
\[
W_i^-\to (2\chi-3\tau)(M)-\frac{16A}{27}.
\]
Thus the full \(L^2\)-curvature remains bounded.

---

## 4. Curvature and volume measures

The convergence is stronger than convergence of total integrals. Since \(s_i^2\to16\) uniformly and \(|W_{+,i}|^2\to1/24\) in \(L^1(d\mu_i)\),
\[
\int_M\left|
\frac{s_i^2}{96\pi^2}
-
\frac1{6\pi^2}
\right|\,d\mu_i\to0, \tag{18}
\]
\[
\int_M\left|
\frac{|W_{+,i}|^2}{2\pi^2}
-
\frac1{48\pi^2}
\right|\,d\mu_i\to0, \tag{19}
\]
and
\[
\int_M\frac{|\mathring{\mathrm{Ric}}_i|^2}{8\pi^2}\,d\mu_i\to0. \tag{20}
\]

Thus if \(d\mu_i\) converges weakly as a Radon measure to \(\mu\) after passing to a subsequence, then
\[
\frac{s_i^2}{96\pi^2}\,d\mu_i\to \frac1{6\pi^2}\mu,
\]
\[
\frac{2|W_{+,i}|^2}{4\pi^2}\,d\mu_i\to \frac1{48\pi^2}\mu,
\]
and the trace-free Ricci measure tends to zero.

The volume measure itself may concentrate or collapse geometrically; (18)–(20) say that the scalar and self-dual Weyl energy densities follow it with fixed densities.

---

## 5. Spinor and self-dual form package forced by near equality

Fix one monopole vertex \(a\). Take the rescaled Seiberg–Witten equations with
\[
f_i^2=x_i+\sqrt6\,w_i
=
-s_i+\sqrt6|W_{+,i}|.
\]
Since \(x_i\to4\) and \(w_i\to1/(2\sqrt6)\) in \(L^2\),
\[
f_i\to \frac3{\sqrt2}
\quad\text{in }L^4(d\mu_i).
\]

Let \((A_i,\Phi_i)\) solve the rescaled equations
\[
D_{A_i}\Phi_i=0,\qquad -iF_{A_i}^+=f_i\sigma(\Phi_i).
\]
Set
\[
\psi_i=2\sqrt2\,\sigma(\Phi_i)\in\Omega_i^+,
\qquad
\varphi_i=\frac32\psi_i.
\]
Near equality in the scalar–Weyl proof forces all Hölder and harmonic-projection defects in that proof to vanish. In particular,
\[
\bigl\||\psi_i|-\sqrt2\bigr\|_{L^2(d\mu_i)}\to0, \tag{21}
\]
\[
\|d\psi_i\|_{L^2(d\mu_i)}\to0, \tag{22}
\]
and
\[
\int_M |iF_{A_i}^+|^2\,d\mu_i
\to
4\pi^2A. \tag{23}
\]

Let \(h_i^a\) be the \(g_i\)-harmonic self-dual representative of the class \(a_i^+\). The harmonic projection part of the proof gives
\[
\|\,iF_{A_i}^+-2\pi h_i^a\,\|_{L^2(d\mu_i)}\to0. \tag{24}
\]
Using
\[
f_i\psi_i=2\sqrt2(-iF_{A_i}^+)
\]
and \(f_i\to3/\sqrt2\), (21) gives
\[
\int_M\left|
|2\pi h_i^a|^2-\frac98
\right|\,d\mu_i\to0,
\]
equivalently
\[
\int_M\left|
|h_i^a|^2-\frac{9}{32\pi^2}
\right|\,d\mu_i\to0. \tag{25}
\]

So every monopole vertex produces a harmonic self-dual form whose pointwise length is asymptotically the same positive constant in \(L^1\), while its cohomology class tends to the corresponding signed sum of the \(c_j\)’s.

The Weyl-eigenline defect also vanishes:
\[
\int_M
\left(
\sqrt{\frac23}\,|W_{+,i}|\,|\psi_i|^2
+
W_{+,i}(\psi_i,\psi_i)
\right)d\mu_i\to0. \tag{26}
\]
Thus the spinor 2-form is asymptotically in the lowest eigendirection of \(W_+\), and the other two eigenvalues of \(W_+\) are asymptotically equal wherever the equality structure persists smoothly.

---

## 6. Phase measures from the \(m\) canonical classes

Let \(u_{j,i}\) denote the harmonic self-dual representative of \(c_{j,i}^+\). Since \(E_{\ell,i}^+\to0\), the harmonic representative of a vertex \(a_{\varepsilon,\eta}\) is
\[
h_i^{\varepsilon,\eta}
=
\sum_{j=1}^m \varepsilon_j u_{j,i}+o_{L^2}(1).
\]
By (25), for every \(\varepsilon\in\{\pm1\}^m\),
\[
\left\|
\left|\sum_{j=1}^m\varepsilon_j u_{j,i}\right|^2
-
\frac{9}{32\pi^2}
\right\|_{L^1(d\mu_i)}
\to0. \tag{27}
\]

Averaging (27) over signs gives
\[
\left\|
\sum_{j=1}^m |u_{j,i}|^2
-
\frac{9}{32\pi^2}
\right\|_{L^1(d\mu_i)}
\to0. \tag{28}
\]
Walsh sign-polarization gives, for \(p\ne q\),
\[
\int_M |\langle u_{p,i},u_{q,i}\rangle|\,d\mu_i\to0. \tag{29}
\]

Define densities
\[
\theta_{j,i}
=
\frac{|u_{j,i}|^2}{9/(32\pi^2)}.
\]
Then
\[
\sum_{j=1}^m\theta_{j,i}\to1\quad\text{in }L^1(d\mu_i),
\]
and
\[
\int_M\theta_{j,i}\,d\mu_i
\to
\frac{32\pi^2A_j}{9}. \tag{30}
\]
After passing to a subsequence, the measures
\[
\theta_{j,i}\,d\mu_i
\]
converge weakly to phase measures \(\mu_j\) with
\[
\sum_{j=1}^m\mu_j=\mu,
\qquad
\mu_j(M)=\frac{32\pi^2A_j}{9}. \tag{31}
\]

These \(\mu_j\)’s are the natural concentration measures attached to the \(X_j\)-summands. The \(N\)-classes have vanishing self-dual energy by (8), so the \(N\)-topology must be carried by anti-self-dual Weyl concentration, thin regions, or singular/collapsed geometry.

---

## 7. What extra compactness would force

### Smooth noncollapsed regions lead to a local contradiction

Suppose a subsequence has a smooth four-dimensional pointed limit on some open set, with enough control to pass (15), (20), and (26) to the limit. The limit metric satisfies
\[
\mathrm{Ric}=-g,\qquad s=-4,\qquad |W_+|=\frac1{2\sqrt6}.
\]
The equality structure from (26) gives
\[
\operatorname{Spec}(W_+)=\left\{-\frac16,\frac1{12},\frac1{12}\right\}. \tag{32}
\]

But an oriented Einstein four-manifold has harmonic self-dual Weyl tensor. Derdziński’s theorem says that if \(W_+\neq0\) has two equal eigenvalues on an open set, then the metric is locally conformal to Kähler; if \(|W_+|\) is constant, the metric itself is locally Kähler. For a Kähler surface with \(s=-4\),
\[
\operatorname{Spec}(W_+)=\left\{-\frac23,\frac13,\frac13\right\},
\]
so (32) cannot occur.

Thus any putative \(\delta_i\to0\) sequence must avoid producing a smooth noncollapsed four-dimensional region carrying positive limiting volume. This is much stronger than the published strictness statement: it says that equality can only be approached through collapse, singular formation, or loss of the analytic compactness needed to pass the eigenline structure to a smooth limit.

Relevant source family: Derdziński’s harmonic self-dual Weyl tensor theorem for Einstein four-manifolds; Anderson/Cheeger–Tian compactness for four-dimensional Einstein or almost-Einstein metrics with \(L^2\)-curvature and noncollapse.

### Route to a symplectic contradiction

For a fixed vertex \(a\), (21)–(24) say that \(\psi_i\) is an almost closed self-dual form of almost constant length \(\sqrt2\), and it is \(L^2\)-close to a closed harmonic self-dual form \(h_i^a\) after scaling.

If one had uniform Sobolev and elliptic control strong enough to upgrade (25) to a pointwise lower estimate
\[
|h_i^a|\ge c>0
\]
for large \(i\), then \(h_i^a\) would be a closed self-dual nonvanishing 2-form, hence a symplectic form. The spinor reduction would identify the associated almost-complex anti-canonical class with \(a\). Since \(M\) is a connected sum with \(m>1\) and \(b_+>1\) on more than one summand, ordinary Seiberg–Witten invariants vanish, while Taubes gives a nonzero invariant for a symplectic four-manifold with \(b_+>1\). This would contradict the topology.

The missing analytic substance is exactly the upgrade from \(L^1/L^2\) almost-constant length to a pointwise lower estimate. Uniform Sobolev constants, curvature-radius control, or a noncollapsed Einstein-orbifold compactness theorem could supply it.

### Multiple-form route

The phase identities (27)–(29) are even sharper. On a smooth region where the Weyl eigenline structure passes to the limit, all sign sums
\[
\sum_j\varepsilon_j u_j
\]
must lie in the same lowest eigendirection of \(W_+\). But (29) says the individual \(u_j\)’s are pointwise orthogonal in the \(L^1\) limit. Both can hold only if, at almost every regular point, at most one phase density \(\theta_j\) is present.

Thus a compactness theorem would force a phase separation:
\[
\theta_j\theta_\ell\to0\quad(j\ne \ell),
\]
with limiting regions of volumes
\[
\frac{32\pi^2A_j}{9}.
\]
Interfaces between phases would be precisely where necks, collapse, or curvature concentration occur. A connected smooth four-dimensional limit with two phases present on the same open set is incompatible with the equality structure.

---

## 8. Plausible degeneration geometry

If such a sequence exists, the formulas above leave very little freedom.

It must have:

\[
s_i\to-4,\qquad
\mathring{\mathrm{Ric}}_i\to0\ \text{in }L^2,
\qquad
|W_{+,i}|\to\frac1{2\sqrt6}\ \text{in }L^2,
\]
\[
\mathrm{Vol}_i\to\frac{32\pi^2A}{9},
\]
and the period planes must satisfy
\[
c_{j,i}^-\to0,\qquad E_{\ell,i}^+\to0.
\]

The natural picture is not a smooth Einstein limit on \(M\). Rather, the \(X_j\)-classes define phase measures \(\mu_j\) with prescribed masses \(32\pi^2A_j/9\), while the \(N\)-classes disappear from the self-dual period data. The connected-sum necks and the \(N\)-topology would have to live in collapsed or singular regions, likely through anti-self-dual Weyl concentration and loss of harmonic-form pointwise control.

A sharp formulation for the remaining problem is:

> Can a sequence of metrics on these equality-case Ishida–LeBrun manifolds satisfy the energy, period, spinor, and phase-measure limits above while every positive-volume region avoids smooth four-dimensional noncollapsed convergence?

Equivalently, resolving the \(\mathrm{Ric}\approx -g\) side in dimension four reduces to a compactness/collapse theorem for almost-Einstein metrics carrying the full Bauer–Furuta family of near-saturating Seiberg–Witten forms.