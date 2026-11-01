# TTCS Independent Branch Record

```json
{
  "step_id": 10,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step10_accessible_cover_reassessment.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step10.md",
    "Sessions/S0910A01/workspace/notes/step9_general_cover_transport.md",
    "Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md",
    "Sessions/S0910A01/workspace/notes/sources/lott_1708_06780_collapsing_almost_ricci_flat_4_manifolds.txt",
    "Knowledge/objects/papers/Topology-and-ε-regularity-theorems-on-collapsed-manifolds-with-Ricci-cu--4c64d7206fcd--56043259b64c/object.md",
    "Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md"
  ]
}
```

## Task

Read the corrected Step 10 reassessment and route plan for the Yau 26 Ricci-pinching project. Check the mathematical scope and consistency of the fixed-scale accessible-cover theorem, the use of the normal-cover mean lemma, Naber--Zhang Proposition 6.4, Lott's orbit-volume formula, Cheeger--Naber positive-branch statements, and the four-dimensional energy bookkeeping. Identify any remaining overstatement, missing hypothesis, coefficient/sign issue, or stronger next mathematical target. Treat the goal as rigorous progress toward proving or refuting the full proposition, not final exposition.

## Output

# Scientific verification memo

## Overall assessment

The Step 10 repair is mathematically coherent in its main structure. The Lott formula, the Naber–Zhang interface, the four-dimensional Cheeger–Naber distinction, the calibrated Weyl spectrum, and the corrected signature coefficient are consistent with the supplied sources.

Four points still require formal repair:

1. The normal-cover transport lemma needs a genuine precompact-core hypothesis; its displayed “buffer” condition is otherwise tautological.
2. The accessible-point set needs the exact Naber–Zhang constants, model assumptions, and a measurable formulation.
3. The displayed \(\mathrm{Nil}^3\) orbit-volume ODE has the corrected sign, but periodic exclusion requires a second ODE, not that equation alone.
4. The full-curvature energy formula uses curvature-operator norm. Without saying so, it differs by a factor \(4\) from the usual \((0,4)\)-tensor norm.

Subject to these repairs, the fixed-scale accessible-cover conclusion is sound.

---

## 1. Normal-cover mean transport

The multiplicity-cancellation argument in `step9_general_cover_transport.md` is correct in substance. For a regular cover, normality makes the deck group transitive on every fiber, and the estimates

\[
m_r(x)\le N(2r),
\qquad
N(2r)\operatorname{Vol}B_r(p)
 \le \operatorname{Vol}B_{3r}(\hat p)
\]

do yield

\[
\fint_{B_r(\hat p)}\pi^*\varphi
\le
\frac{\operatorname{Vol}B_{3r}(\hat p)}
     {\operatorname{Vol}B_r(\hat p)}
\fint_{B_r(p)}\varphi
\le
\frac{V_{-K}^{(n)}(3r)}{V_{-K}^{(n)}(r)}
\fint_{B_r(p)}\varphi .
\]

Two technical details in the written lemma need strengthening.

### 1.1 The “buffer” hypothesis

If \(B_{3r}(\hat p)\) is defined intrinsically in \(\widehat U\), then

\[
B_{3r}(\hat p)\subset \widehat U
\]

says nothing. Finiteness of

\[
N(2r)=\#\{\gamma:d(\hat p,\gamma\hat p)<2r\}
\]

and local Bishop–Gromov comparison require a core that stays away from the edge of the covering domain. A sufficient formulation is

\[
\overline{B_{3r}(\hat p)}\Subset \widehat U,
\]

with the lifted Ricci lower bound on a neighborhood of that closed ball. Another clean formulation is that the cover extends over \(B_{4r}(p)\), while all balls used in the estimate lie over \(B_{3r}(p)\).

This is automatic in the intended application to the universal cover of \(B_1(p)\) after choosing \(3r<1\), but it is not automatic in the abstract lemma as currently written.

### 1.2 Measurable selection

The assertion that all closest-lift tie sets are smooth codimension-one submanifolds is stronger than needed and is not generally justified in the presence of cut loci. A standard measurable construction suffices:

- enumerate the countable deck group;
- select a lift minimizing distance to \(\hat p\);
- resolve ties by the enumeration.

The area formula for the resulting measurable section gives

\[
\operatorname{Vol}S=\operatorname{Vol}B_r(p).
\]

With these two changes, the transport theorem is rigorous and independent of sheet number or deck-group growth.

---

## 2. Fixed-scale accessible-cover theorem

A precise reusable version can be stated as follows.

Let \(E_i\subset M_i\) be measurable. Suppose every \(p\in E_i\) admits integers
\(0\le \ell\le k\le4\) and a pointed Ricci-limit space
\((Z^\ell,z)\), with \(\ell\le3\), such that

\[
d_{GH}\!\left(
B_2(p),
B_2(0^{k-\ell},z)
\right)<\delta_*(4,r_*),
\]

\[
r_c(z)\ge r_*,
\]

and

\[
\operatorname{rank}\Gamma_{\delta_*}(p)=4-k,
\qquad
\Gamma_{\delta_*}(p)
=
\operatorname{Image}\!\left[
\pi_1(B_{\delta_*}(p))
\to \pi_1(B_2(p))
\right].
\]

Here \(\delta_*(4,r_*)\) is the uniform constant supplied by Naber–Zhang after using their explicit dependence on the model noncollapsing radius. The local compactness assumption from Proposition 6.4 must also be included; it holds on the closed manifolds under consideration.

Then, for a LeBrun near-critical sequence satisfying

\[
\fint_{M_i}F_i\longrightarrow0,
\qquad
F_i\ge0,
\]

one has

\[
\frac{\operatorname{Vol}E_i}{\operatorname{Vol}M_i}\longrightarrow0.
\]

### Verification of the proof

Naber–Zhang Proposition 6.4 gives a uniform number

\[
h_*=h_*(4,r_*)>0
\]

such that the lift of \(p\) to the universal cover of \(B_1(p)\) has \(C^1\)-harmonic radius at least \(h_*\). Choose

\[
0<a<\min\{1/4,h_*/4\}.
\]

If \(\operatorname{Vol}E_i\ge\eta\operatorname{Vol}M_i\), fixed-radius averaging gives a point \(p_i\in E_i\) with

\[
\fint_{B_a(p_i)}F_i\longrightarrow0.
\]

On the universal cover \(\pi_i:\widetilde{B_1(p_i)}\to B_1(p_i)\), the corrected transport lemma gives

\[
\fint_{B_a(\tilde p_i)}\pi_i^*F_i\longrightarrow0.
\]

The harmonic-radius estimate supplies a fixed Euclidean coordinate domain inside \(B_a(\tilde p_i)\). Bounded Ricci curvature and the harmonic-coordinate equation give uniform finite-\(W^{2,p}\) estimates. For \(p>4\), subsequential \(C^{1,\alpha}\) convergence follows; the relation

\[
\operatorname{Ric}_{g_i}=-g_i+e_i,
\qquad
\|e_i\|_{L^\infty}\to0,
\]

then improves convergence to strong \(W^{2,p}\) on a smaller chart. The limit is smooth and satisfies

\[
\operatorname{Ric}_{g_\infty}=-g_\infty.
\]

Strong \(W^{2,p}\) convergence passes the curvature tensor strongly in \(L^p\). Since eigenvalues of a symmetric matrix depend Lipschitz-continuously on that matrix, the Weyl eigenvalue term and \(\mathcal G_i\) pass in \(L^1\). Thus

\[
s_\infty=-4,\qquad
|W_\infty^+|^2=\frac1{24},\qquad
\operatorname{Spec}(W_\infty^+)
=
\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

Derdziński’s factor is

\[
(24|W_\infty^+|^2)^{1/3}=1,
\]

so the limit is locally Kähler. A Kähler surface with \(s=-4\) has

\[
|W^+|^2=\frac{s^2}{24}=\frac23,
\]

contrary to \(1/24\). The local contradiction is therefore valid.

The separate condition that the local universal cover be “a genuine normal cover” is redundant: the universal cover of \(B_1(p)\) is regular. What matters is the precompact central ball described above.

For complete measure-theoretic precision, the theorem is best phrased for every measurable \(E_i\) whose points satisfy the listed properties, rather than asserting without proof that the full existence-defined set \(S_i(r_*)\) is Borel.

---

## 3. Lott’s orbit-volume formula and the \(\mathrm{Nil}^3\) sign

Lott’s equation (2.9) is quoted correctly:

\[
\Delta_B v
=
\left(\frac14|F|^2-\lambda N\right)v,
\qquad
v=\sqrt{\det G}.
\]

Its use requires the exact adapted metric, a free local abelian action, and determinant holonomy in \(\det^{-1}(\{\pm1\})\), so that \(v\) is globally defined. Proposition 2.10 also requires a parabolic quotient base and an upper bound for \(v\). The Step 10 restriction to exact model geometries is therefore appropriate.

For \(\lambda=-1\),

\[
\Delta_Bv=\left(\frac14|F|^2+N\right)v>0.
\]

A periodic one-dimensional base is impossible by integration. The real-hyperbolic example

\[
dt^2+e^{2t/\sqrt3}g_{T^3}
\]

is correctly normalized:

\[
\operatorname{Ric}=-g,\qquad
v=e^{\sqrt3t},\qquad
v''=3v.
\]

For diagonal \(\mathrm{Nil}^3\) orbits, let

\[
H_j=\frac{a_j'}{a_j},
\qquad
H=H_1+H_2+H_3,
\qquad
v'=Hv,
\qquad
\mu=\frac{a_3^2}{2a_1^2a_2^2}.
\]

The intrinsic Ricci eigenvalues of the orbit are

\[
(-\mu,-\mu,\mu).
\]

Summing the three tangential Einstein equations for
\(\operatorname{Ric}=-g\) gives

\[
H'+H^2=3-\mu,
\]

hence

\[
v''=(3-\mu)v.
\]

Thus the corrected sign in Step 10 is right.

This ODE alone does not exclude a periodic base because \(3-\mu\) has no fixed sign. The required second identity is readily derived. Put

\[
q=H_1+H_2-H_3.
\]

The individual tangential equations give

\[
q'+Hq=1-3\mu,
\]

so

\[
(vq)'=(1-3\mu)v.
\]

Periodicity would imply simultaneously

\[
\int (3-\mu)v\,dt=0,
\qquad
\int (1-3\mu)v\,dt=0.
\]

Writing \(I_0=\int v\) and \(I_\mu=\int\mu v\), these equations give

\[
I_\mu=3I_0,
\qquad
I_\mu=\frac13I_0,
\]

which is impossible since \(I_0>0\). This supplies the missing periodic argument.

The complex-hyperbolic cusp normalization is not explicitly calculated in the supplied artifacts. An explicit coframe and scale producing \(\operatorname{Ric}=-g\) would make that calibration independently reproducible.

---

## 4. Cheeger–Naber in the \(\operatorname{Ric}\approx g\) branch

The use of Cheeger–Naber Theorem 1.12 is correct in dimension four.

If

\[
\|g^{-1}(\operatorname{Ric}-g)\|_{\mathrm{op}}\le\delta_i,
\qquad
\delta_i\to0,
\]

then eventually

\[
\operatorname{Ric}\ge(1-\delta_i)g,
\]

so Myers gives a uniform diameter bound. Also, for \(\delta_i\le1/2\),

\[
|\operatorname{Ric}|_{\mathrm{HS}}
\le 2(1+\delta_i)\le3,
\]

which matches the theorem’s Ricci norm hypothesis.

A lower total-volume bound and the diameter bound give a lower unit-ball volume by Bishop–Gromov comparison. Hence pairwise nondiffeomorphic manifolds such as

\[
\#_k(S^2\times S^2)
\]

cannot carry a sequence of such metrics with both \(\delta_i\to0\) and total volume bounded below. Any sequence along \(k_i\to\infty\) with \(\delta_i\to0\) must have total volume tending to zero.

The Step 10 distinctions are correct:

- Theorem 1.12 is four-dimensional.
- Theorem 1.4 works in all dimensions but concerns codimension-four regularity of noncollapsed limits.
- Finite diffeomorphism type does not itself construct an Einstein metric.
- An orbifold limit does not by itself yield a smooth Einstein metric on the original manifold.

---

## 5. Four-dimensional energy bookkeeping

The signature calculation is correct:

\[
12\pi^2\tau(M)
=
\int_M\left(|W^+|^2-|W^-|^2\right)d\mu,
\]

and for

\[
M=X\#k\overline{\mathbb{CP}}^{\,2},
\qquad
\tau(M)=\tau(X)-k,
\]

one gets

\[
\int|W^-|^2
=
\int|W^+|^2
-12\pi^2\tau(X)
+12\pi^2k.
\]

The earlier coefficient \(32\pi^2k\) is indeed incorrect.

The full-curvature formula needs an explicit norm convention. If
\(\mathcal R:\Lambda^2\to\Lambda^2\) denotes the curvature operator, then

\[
|\mathcal R|^2
=
|W^+|^2+|W^-|^2+\frac12|E|^2+\frac{s^2}{24},
\]

and Chern–Gauss–Bonnet gives

\[
\int|\mathcal R|^2
=
8\pi^2\chi(M)+\int|E|^2.
\]

Thus, with

\[
J=\frac1{8\pi^2}\int|E|^2,
\]

\[
\int|\mathcal R|^2
=
8\pi^2\bigl(\chi(X)+k+J\bigr).
\]

For the usual \((0,4)\)-tensor norm,

\[
|\operatorname{Rm}|^2_{(0,4)}=4|\mathcal R|^2,
\]

so all coefficients are multiplied by \(4\). The script and note should identify which convention is used.

The calibrated values are internally consistent:

\[
\operatorname{Vol}\sim\frac{32}{9}\pi^2A,
\]

\[
\int\frac{s^2}{24}
\sim
\frac23\operatorname{Vol}
=
\frac{64}{27}\pi^2A,
\]

\[
\int|W^+|^2
\sim
\frac1{24}\operatorname{Vol}
=
\frac4{27}\pi^2A.
\]

Moreover, near \(\operatorname{Ric}=-g\),

\[
E=\operatorname{Ric}-\frac{s}{4}g=O(\delta_i),
\]

so if \(\operatorname{Vol}/A\) stays bounded,

\[
\frac{J_i}{A_i}\longrightarrow0.
\]

The remaining family-dependent input is therefore mainly a bound for
\(\chi(X_i)/A_i\), together with the already calibrated \(k_i/A_i\). No source passage establishing the required geography estimate for the chosen algebraic-surface family appears in the supplied files; that part remains source-dependent rather than following from Ricci pinching.

The dimensionless local quantity

\[
r^4\fint_{B_r(p)}|\mathcal R|^2
\]

is correct. A bounded global mean selects many balls with bounded local mean, but not necessarily with energy below an \(\epsilon\)-regularity threshold. It also does not create a harmonic chart on a collapsed base ball. Flat collapsing tori already show that zero curvature energy can coexist with vanishing base harmonic radius, while their normal covers restore accessibility.

---

## 6. Strongest concrete mathematical target

The clean bridge is a fixed-scale accessible-volume theorem. Define

\[
\mathcal A_i(a,v)=
\left\{
p\in M_i:
\begin{array}{l}
\text{there is a regular cover of }B_{4a}(p),\\
\overline{B_{3a}(\hat p)}\Subset\widehat U,\quad
\operatorname{Vol}B_a(\hat p)\ge va^4
\end{array}
\right\}.
\]

The decisive statement would be the existence of fixed \(a,v,\eta>0\) such that

\[
\operatorname{Vol}\mathcal A_i(a,v)
\ge
\eta\,\operatorname{Vol}M_i
\]

for every hypothetical LeBrun near-critical sequence with the established topology and energy budgets. The normal-cover transport theorem and the calibrated local contradiction would then rule out that sequence.

Naber–Zhang gives a concrete sufficient mechanism for membership in \(\mathcal A_i(a,v)\): a uniform model radius and maximal fibered nilpotency rank. Thus the substantive unresolved estimate is a quantitative bound on the volume occupied by points with

\[
\operatorname{rank}\Gamma_{\delta_*}(p)<4-k
\]

or with \(r_c(z)\to0\), possibly expressed through curvature-operator energy or Chern–Weil concentration.

Even such a theorem would address the selected four-dimensional LeBrun family, not universal pinching constants for every closed four-manifold or dimensions \(n\ne4\). Conversely, a refutation of the original proposition must defeat every possible interval \([c_n,C_n]\), including intervals of either sign; a near-critical \(\operatorname{Ric}\approx-g\) family alone would not do that.