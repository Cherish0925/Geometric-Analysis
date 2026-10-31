# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 42,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step42_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step42_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify, as a strict geometric analyst, the three new results in the Step-42 note: (1) Lemma T (Taubes period lemma) and its Corollaries T1/T2 claiming that the Step-40 'formal common mode' (constant monopole amplitude, closed sign-independent self-dual form psi, all exceptional classes ASD harmonic) is topologically impossible on M = X # k CPbar^2 with b+(X)>=2 and basic classes ±K_X. Check the use of Taubes' SW=>Gr (sign conventions: class e with SW(2e-K_omega) nonzero is represented by J-curves), the blow-up formula, whether K_X·omega has a definite sign, and whether 'nowhere-vanishing self-dual harmonic form' really yields a symplectic form to which these apply. (2) Theorem AKGamma: for every almost-Kähler metric, C+ >= (l^2/(128 pi^2 V)) (3 theta^2 - 2 theta + 1) with l = 8 pi K_omega·[omega], theta = (1/l) int |nabla omega|^2, using LeBrun's conventions s* = s + |nabla omega|^2 = 2W+(omega,omega)+s/3 and Blair's formula int (s+s*) = 8 pi c1·[omega], [omega]^2 = 2V; check the pointwise bound, the Jensen step (sigma = -s sign-unrestricted), the reverse Cauchy-Schwarz step, the claimed equality class, and the identification of the Step-40 common mode as the alpha=0 equality case with beta(r) = 2 theta - 3 theta^2. Check the closed identity C+ = A - k + P/(8 pi^2) normalization against the Step-40 note. (3) Proposition G and G' (tariff ⇐ linear Goldberg estimate; c -> 0 ⇒ unbounded Goldberg ratio), including the constants kappa/(kappa+2) and kappa/(1+kappa). Report every error with its correction, state precisely which hypotheses are needed, and say whether any of these statements is already standard in the literature (LeBrun, Taubes, Armstrong, Apostolov–Drăghici) so that novelty is not overstated. Also judge whether the 'quantitative Armstrong' target in §3 is a correctly posed and genuinely weaker problem than quantitative Goldberg, and propose the sharpest tractable formulation.

## Integrated Scientific Memo

# Strict verification memo

## Verdict

1. **Lemma T and Corollaries T1/T2 are correct**, provided the basic-class hypothesis is stated literally: modulo torsion, \(X\) has exactly the basic classes \(\pm K_X\), so the blow-up has exactly
   \[
   \pm K_X+\sum_{i=1}^k\epsilon_iE_i.
   \]
   The Taubes sign convention is correct; \(K_X\!\cdot[\omega]\) itself has no fixed sign, but its sign is determined by the \(s=\pm1\) appearing in \(K_\omega\), so the absolute-value formula is right. A nowhere-zero self-dual harmonic form is indeed symplectic.

2. The **intrinsic \(\ell\)-version** of Theorem AK\(\Gamma\),
   \[
   C_+\ge \frac{\ell^2}{128\pi^2V}\bigl(3\theta^2-2\theta+1\bigr),
   \]
   is correct, including all constants, the sign-unrestricted Jensen argument, and the exact equality conditions.

   However, the further claim
   \[
   \frac{\ell^2}{128\pi^2V}\ge A(1+\alpha)^2
   \]
   is false under the stated hypotheses. The reverse Cauchy–Schwarz/Hodge-index argument does not apply to arbitrary positive-square classes when \(b^+\ge2\). Consequently, the \(A\)-valued tariff form of AK\(\Gamma\), the universal “saving \(\le2A\theta\)” assertion, and Proposition G as stated are not established without an extra period hypothesis.

3. **Proposition G** has the correct algebraic factor \(\kappa/(\kappa+2)\), conditional on the missing inequality \(P/(8\pi^2)\ge k-2A\theta\).

4. **Proposition G′** has the correct factor \(\kappa/(1+\kappa)\). But
   \[
   \frac{P}{8\pi^2k}\to0\Longrightarrow \frac{\mathcal N}{P}\to\infty
   \]
   is only a one-way implication; “precisely” is incorrect.

5. The proposed “quantitative Armstrong” target is logically weaker than a quantitative Goldberg estimate if restricted to an eigenvector/saturated subclass, but the exact saturated class is too narrow to capture the real difficulty. The sharp tractable target is a **near-saturated coercivity estimate with an explicit saturation defect**, or, more weakly, an \(L^4\)-torsion estimate on the \(W^+(\omega)^\perp=0\) class.

---

# 1. Taubes period lemma

## 1.1 Exact hypotheses

The argument needs:

- \(M=X\#k\overline{\mathbb{CP}}^{\,2}\), oriented as the blow-up;
- \(b^+(M)=b^+(X)\ge2\), avoiding chambers;
- \(K_X^2=A>0\);
- modulo torsion, the complete Seiberg–Witten basic-class set of \(X\) is exactly \(\{\pm K_X\}\);
- hence, by the blow-up formula,
  \[
  \mathfrak B(M)=
  \left\{sK_X+\sum_{i=1}^k\epsilon_iE_i:
  s,\epsilon_i=\pm1\right\}.
  \]

“Minimal surfaces of general type” is too broad as an automatic example: the supplied sources do not establish that every such surface has only the two basic classes \(\pm K_X\). Retain the exact basic-class assumption.

## 1.2 Taubes convention and periods

For a symplectic form \(\omega\), write \(K_\omega=-c_1(TM,J)\). In the convention used here, Taubes’ \(SW\Rightarrow Gr\) theorem says:

\[
SW(2e-K_\omega)\ne0
\quad\Longrightarrow\quad
PD(e)
\text{ is represented by a \(J\)-holomorphic subvariety}
\]
for generic \(\omega\)-compatible \(J\). For nonzero \(e\),
\[
e\cdot[\omega]>0.
\]

Taubes supplies the canonical basic class (up to the usual conjugation convention), and conjugation supplies its negative. Therefore the assumed list gives
\[
K_\omega=sK_X+\sum_i\epsilon_iE_i.
\]
Put \(e_i=\epsilon_iE_i\). Then
\[
2e_i-K_\omega
=-sK_X+e_i-\sum_{j\ne i}e_j
\]
is again a blow-up basic class. Also,
\[
2sK_X-K_\omega=sK_X-\sum_i e_i
\]
is basic. Since \(e_i\ne0\) and \(sK_X\ne0\), Taubes gives
\[
e_i\cdot[\omega]>0,\qquad sK_X\cdot[\omega]>0.
\]
Thus
\[
e_i\cdot[\omega]=|E_i\cdot[\omega]|,\qquad
sK_X\cdot[\omega]=|K_X\cdot[\omega]|.
\]
Consequently,
\[
\boxed{
K_\omega\cdot[\omega]
=
|K_X\cdot[\omega]|+\sum_i|E_i\cdot[\omega]|.
}
\]

The sign of \(K_X\cdot[\omega]\) is not fixed relative to a once-and-for-all choice of \(K_X\). What is definite is
\[
sK_X\cdot[\omega]>0.
\]
The absolute value in Lemma T is therefore essential.

For rigor, replace “represented by \(J\)-holomorphic curves” with “represented by a \(J\)-holomorphic subvariety/current”; smooth connected representatives are unnecessary.

## 1.3 Nowhere-zero self-dual harmonic forms

If \(\psi\) is self-dual and harmonic, then \(d\psi=0\). If it is nowhere zero,
\[
\psi\wedge\psi=|\psi|_g^2\,d\mu_g>0,
\]
so \(\psi\) is a symplectic form inducing the given orientation. No constant norm is needed for Taubes.

Moreover, conformally rescaling \(g\) makes \(|\psi|\equiv\sqrt2\): the Hodge star on two-forms is conformally invariant in dimension four. Thus “nowhere-zero self-dual harmonic” is equivalent to admitting a conformally almost-Kähler representative.

Applying Lemma T to \(\psi\) gives
\[
|E_i\cdot[\psi]|>0
\]
for every exceptional class. Hence:

\[
E_i\cdot[\psi]=0
\quad\Longrightarrow\quad
\psi\text{ has a zero}.
\]

If the harmonic representative of \(E_i\) is anti-self-dual, it is intersection-orthogonal to every self-dual harmonic form, so every such form has zero \(E_i\)-period. Therefore no nowhere-zero self-dual harmonic form exists. Corollary T1 is correct.

## 1.4 T2 and the Step-40 common mode

For an actual monopole solution, the harmonic projection of the self-dual curvature/monopole two-form is a fixed multiple of the self-dual harmonic projection of its spin\(^c\) class
\[
a_\epsilon=sK_X+\sum_i\epsilon_iE_i
\]
(up to the overall convention). Flipping \(\epsilon_i\) changes that harmonic component by a nonzero multiple of \(E_i^+\).

Therefore:

- sign-independent harmonic monopole forms force \(E_i^+=0\) for all \(i\);
- if one sign-independent form is closed and nowhere zero, it is symplectic;
- Lemma T then forces every exceptional period, hence every \(E_i^+\), to be nonzero.

This is a contradiction. Thus the Step-40 formal state—closed, nowhere-zero, sign-independent common form and all exceptional classes ASD—is impossible.

The statement “zero period precisely because the form vanishes on the exceptional sphere” is valid for the cited symmetric cell model, not as a general principle. In general, vanishing integral over a sphere need not imply pointwise vanishing on that sphere.

## 1.5 Literature status

This obstruction is standard in substance. LeBrun’s proof of Proposition 3.2 in the supplied 2001 paper already uses the sign-flipped basic class and Taubes to contradict zero exceptional symplectic area. Lemma T is a useful packaged period identity, but should not be presented as a fundamentally new Taubes-type theorem.

---

# 2. Theorem AK\(\Gamma\)

Set
\[
u=\frac{\omega}{\sqrt2},\qquad |u|=1,\qquad
\delta=s^*-s=|\nabla\omega|^2,\qquad
\sigma=-s.
\]
Since
\[
s^*=2W^+(\omega,\omega)+\frac{s}{3},
\]
and \(W^+(\omega,\omega)=2W^+(u,u)\),
\[
W^+(u,u)=\frac{s}{6}+\frac{\delta}{4}
=-\frac{\sigma}{6}+\frac{\delta}{4}.
\]

## 2.1 Pointwise estimate

For any trace-free self-adjoint endomorphism \(W:\Lambda^+\to\Lambda^+\) and unit \(u\),
\[
|W|^2\ge\frac32W(u,u)^2.
\]
At fixed \(q=W(u,u)\), the minimum occurs when \(u\) is an eigenvector and the other eigenvalues are \(-q/2,-q/2\).

Therefore,
\[
\begin{aligned}
\frac{|W^+|^2}{2\pi^2}+\frac{s^2}{96\pi^2}
&\ge
\frac{3}{4\pi^2}
\left(-\frac{\sigma}{6}+\frac{\delta}{4}\right)^2
+\frac{\sigma^2}{96\pi^2}\\
&=
\frac{2\sigma^2+(3\delta-2\sigma)^2}{192\pi^2}
=:G(\sigma,\delta).
\end{aligned}
\]
The Hessian eigenvalues are
\[
\frac{5-\sqrt{17}}{64\pi^2},
\qquad
\frac{5+\sqrt{17}}{64\pi^2},
\]
so \(G\) is strictly convex on all of \(\mathbb R^2\). No assumption \(\sigma\ge0\), equivalently \(s\le0\), is used.

## 2.2 Blair identity and Jensen

Blair’s formula is
\[
\int_M(s+s^*)\,d\mu
=-8\pi K_\omega\cdot[\omega].
\]
Define
\[
\ell=8\pi K_\omega\cdot[\omega]>0,\qquad
\theta=\frac1\ell\int_M\delta\,d\mu.
\]
Then
\[
\int_M(2\sigma-\delta)\,d\mu=\ell.
\]
Hence
\[
\bar\delta=\frac{\theta\ell}{V},
\qquad
\bar\sigma=\frac{(1+\theta)\ell}{2V}.
\]
Jensen gives
\[
\begin{aligned}
C_+
&\ge V G(\bar\sigma,\bar\delta)\\
&=
\frac{\ell^2}{128\pi^2V}
\left(3\theta^2-2\theta+1\right).
\end{aligned}
\]
Thus
\[
\boxed{
C_+\ge
\frac{\ell^2}{128\pi^2V}\Gamma(\theta),
\qquad
\Gamma(\theta)=3\theta^2-2\theta+1
}
\]
is correct.

Since
\[
\Gamma(\theta)=3\left(\theta-\frac13\right)^2+\frac23,
\]
its minimum is \(2/3\) at \(\theta=1/3\).

## 2.3 Equality conditions

There is an exact nonnegative defect
\[
\begin{aligned}
\mathfrak d_{\rm AK}
:={}&
C_+-
\frac{\ell^2}{128\pi^2V}\Gamma(\theta)\\
={}&
\frac1{2\pi^2}\int_M
\left(|W^+|^2-\frac32W^+(u,u)^2\right)d\mu\\
&+\int_M
G(\sigma-\bar\sigma,\delta-\bar\delta)\,d\mu.
\end{aligned}
\]
Equality holds iff:

1. \(u\) is an eigenvector of \(W^+\), and on \(u^\perp\),
   \[
   W^+=-\frac12W^+(u,u)\operatorname{Id};
   \]
2. \(\sigma\) and \(\delta\) are constant, equivalently \(s\) and \(s^*\) are separately constant.

Thus, in an orthonormal basis beginning with \(u\),
\[
W^+=\operatorname{diag}(\lambda,-\lambda/2,-\lambda/2).
\]

This should not be identified without qualification with all of LeBrun’s “saturated” class. LeBrun requires \(s+s^*\) constant, \(\omega\) in the lowest eigenspace, and the other eigenvalues equal. AK\(\Gamma\)-equality requires the stronger separate constancy of \(s,s^*\), but it does not always put \(\omega\) in the lowest eigenspace. Indeed,
\[
\lambda=\frac{\ell}{12V}(2\theta-1),
\]
so \(\omega\) is the lowest eigenvector only for \(\theta<1/2\), is null-eigen at \(\theta=1/2\), and is the highest eigenvector for \(\theta>1/2\).

---

# 3. Fatal error in the \(A\)-prefactor

Write
\[
a_i=|E_i\cdot[\omega]|,\qquad
\alpha=\frac{\sum_i a_i}{\sqrt{2AV}},
\qquad
\eta=\frac{|K_X\cdot[\omega]|}{\sqrt{2AV}}.
\]
Lemma T gives
\[
\ell=8\pi\sqrt{2AV}\,(\eta+\alpha),
\]
hence exactly
\[
\boxed{
\frac{\ell^2}{128\pi^2V}=A(\eta+\alpha)^2.
}
\]
Therefore the valid topological form is
\[
\boxed{
C_+\ge A(\eta+\alpha)^2\Gamma(\theta).
}
\]

The note asserts \(\eta\ge1\) by “reverse Cauchy–Schwarz for two positive-square classes.” This is invalid when \(b^+\ge2\): a plane spanned by two positive-square classes can be positive definite, whereas reverse Cauchy–Schwarz only holds in a Lorentzian subspace with one positive direction.

A concrete symplectic countermechanism exists. Let \(X\) be Kähler with a nonzero holomorphic two-form \(\Omega\), and set
\[
\omega_t=\omega_0+t\,\operatorname{Re}\Omega.
\]
The summands are orthogonal self-dual forms for the Kähler metric, and \(\omega_t\) is nowhere zero and symplectic. Along the deformation,
\[
K_{\omega_t}=K_X,\qquad
K_X\cdot[\operatorname{Re}\Omega]=0,
\]
whereas
\[
[\omega_t]^2=[\omega_0]^2+t^2[\operatorname{Re}\Omega]^2.
\]
Thus
\[
\frac{|K_X\cdot[\omega_t]|}
{\sqrt{K_X^2[\omega_t]^2}}
\longrightarrow0.
\]
The same mechanism persists after sufficiently small symplectic blow-ups.

Hence the asserted inequality
\[
\frac{\ell^2}{128\pi^2V}\ge A(1+\alpha)^2
\]
is false in general.

A sufficient additional hypothesis is
\[
\tag{H\(_L\)}
|K_X\cdot[\omega]|\ge\sqrt{K_X^2[\omega]^2}.
\]
This holds, for example, when the relevant classes lie in a common Lorentzian \((1,1)\)-subspace, as in the Kähler case by the Hodge index theorem.

The corrected rearrangement is
\[
\boxed{
\frac{P}{8\pi^2}
\ge
k-A+A(\eta+\alpha)^2\Gamma(\theta).
}
\]
The note’s formula with \(1+\alpha\) requires (H\(_L\)).

The symbolic script does not verify the disputed step: it substitutes
\[
\ell=8\pi\sqrt{2AV}
\]
and therefore assumes \(\eta=1,\alpha=0\) rather than proving a period inequality.

---

# 4. Common-mode calculation

For the Step-40 formal state, put \(r=2-h\), \(s=-4\), and
\[
W^+(n,n)=\frac43-r,\qquad
r^2V=8\pi^2A.
\]
The almost-Kähler identity gives
\[
-\frac23+\frac{\delta}{4}=\frac43-r,
\]
so
\[
\delta=4(2-r)=4h.
\]
Blair gives
\[
\ell=(8-4h)V=4rV=\frac{32\pi^2A}{r}.
\]
Thus
\[
\theta=\frac{\delta V}{\ell}
=\frac{h}{2-h}.
\]
Also
\[
\frac{\ell^2}{128\pi^2V}=A,
\]
so formally
\[
\eta=1,\qquad \alpha=0.
\]
Finally,
\[
\begin{aligned}
2\theta-3\theta^2
&=\frac{2h}{2-h}-\frac{3h^2}{(2-h)^2}\\
&=\frac{16}{2-h}-5-\frac{12}{(2-h)^2}\\
&=\beta(2-h).
\end{aligned}
\]

Therefore the Step-40 common mode is indeed an AK\(\Gamma\)-equality state with the additional formal period values \(\eta=1,\alpha=0\). Lemma T excludes \(\alpha=0\) for an actual symplectic form on the blow-up. This exclusion is qualitative: the period lemma alone gives no uniform positive lower bound for \(\alpha\).

---

# 5. Closed identity normalization

Chern–Gauss–Bonnet and signature give
\[
2\chi+3\tau
=
\frac1{4\pi^2}\int_M
\left(
2|W^+|^2+\frac{s^2}{24}
-\frac{|\operatorname{Ric}^{\circ}|^2}{2}
\right)d\mu.
\]
For \(M=X\#k\overline{\mathbb{CP}}^{\,2}\),
\[
2\chi(M)+3\tau(M)=A-k.
\]
Thus, with \(P=\int|\operatorname{Ric}^{\circ}|^2d\mu\),
\[
\boxed{
C_+
=
\frac1{2\pi^2}\int|W^+|^2
+\frac1{96\pi^2}\int s^2
=
A-k+\frac{P}{8\pi^2}.
}
\]
At \(s=-4\),
\[
P
=
4\int|W^+|^2+\frac43V-8\pi^2(A-k),
\]
which is exactly the Step-40 normalization.

---

# 6. Proposition G

Let \(p=P/(8\pi^2)\). If one has both
\[
p\ge k-2A\theta
\]
and
\[
p\ge\kappa A\theta,\qquad \kappa>0,
\]
then
\[
A\theta\le\frac p\kappa,
\]
and therefore
\[
p\ge k-\frac{2p}{\kappa}.
\]
Hence
\[
\boxed{
p\ge\frac{\kappa}{\kappa+2}\,k.
}
\]
The constant is correct and optimal for this algebraic reduction.

But the first premise does not follow from the valid \(\ell\)-version of AK\(\Gamma\) for arbitrary almost-Kähler metrics. Proposition G must therefore be restated as conditional on either:

- (H\(_L\)); or
- the direct estimate \(p\ge k-2A\theta\); or
- another estimate controlling the period-angle loss \(\eta\).

Without such an assumption, Proposition G is not proved.

---

# 7. Proposition G′

Assume Theorem N gives
\[
8\pi^2k-P\le\mathcal N
\]
and suppose
\[
P\ge\kappa\mathcal N,\qquad \kappa>0.
\]
Then
\[
P\ge\kappa(8\pi^2k-P),
\]
so
\[
\boxed{
P\ge8\pi^2k\,\frac{\kappa}{1+\kappa}.
}
\]
The constant is correct.

For a sequence
\[
c_j=\frac{P_j}{8\pi^2k_j}>0,
\]
one has
\[
\frac{\mathcal N_j}{P_j}
\ge
\frac{8\pi^2k_j-P_j}{P_j}
=
\frac{1-c_j}{c_j}.
\]
Thus
\[
c_j\to0
\quad\Longrightarrow\quad
\frac{\mathcal N_j}{P_j}\to\infty.
\]
The converse does not follow. Large \(\mathcal N/P\) can coexist with \(c\) bounded away from zero because the exact identity contains other nonnegative costs that may offset the Nijenhuis term. Replace “precisely” by “necessarily.”

For the stated coefficient \(c\approx0.9956627\),
\[
\frac{1-c}{c}\approx0.004356,\qquad
\frac{c}{1-c}\approx229.6.
\]
A genuine closed replica satisfying \(P\ge\kappa\mathcal N\) would therefore force \(\kappa\lesssim229.6\). This is only a necessary upper bound, not evidence for existence of such a constant.

The all-metric hypotheses must remain explicit: the scalar \(-4\) Yamabe representative, the simultaneous monopole solutions, and the Step-40 assumptions under which Theorem N was derived.

---

# 8. Literature and novelty

- **Taubes period obstruction:** standard consequence of the blow-up formula and \(SW\Rightarrow Gr\); LeBrun’s 2001 Proposition 3.2 already uses the essential zero-exceptional-period contradiction.

- **Blair identities**
  \[
  s^*=s+|\nabla\omega|^2,\qquad
  \int(s+s^*)=8\pi c_1\cdot[\omega]
  \]
  are standard.

- **LeBrun’s \(2/3\) curvature bound and equality geometry** are standard. The polynomial
  \[
  \Gamma(\theta)=3\theta^2-2\theta+1
  \]
  is a useful elementary refinement retaining the mean torsion parameter before minimization. Its minimum reproduces LeBrun’s \(2/3\) constant. Novelty should be claimed, if at all, only for this explicit profile/defect packaging, not for the underlying bound or saturated geometry.

- **Armstrong:** the supplied source records the theorem that a compact Einstein almost-Kähler four-manifold with \(\omega\) an eigenvector of \(W^+\) cannot be strictly almost-Kähler.

- **Apostolov–Armstrong–Drăghici:** the supplied source records that in the relevant saturated setting, Kählerness is equivalent to \(J\)-invariance of Ricci.

- **G and G′:** algebraic consequences, not independent geometric theorems.

---

# 9. Quantitative Armstrong: correct formulation

A statement restricted to a saturated/eigenvector subclass is formally weaker than a quantitative Goldberg estimate over all almost-Kähler metrics. But the note’s exact target
\[
P\ge\kappa A\theta
\]
has two problems:

1. \(A\theta\) is not naturally tied to the fixed symplectic canonical period without controlling
   \[
   \eta=\frac{|K_X\cdot[\omega]|}{\sqrt{2AV}};
   \]
2. the exact equality class is so rigid that Chern–Weil/Blair identities may already yield substantial restrictions, while near-minimizers need not lie exactly in that class.

The cleanest source-grounded formulation is:

> **Near-saturated quantitative Armstrong.**  
> On a specified class of almost-Kähler metrics satisfying the needed period control, prove constants \(c,C>0\) such that
> \[
> \boxed{
> \frac{P}{8\pi^2}
> +C\,\mathfrak d_{\rm AK}
> \ge cA\theta,
> }
> \]
> where
> \[
> \mathfrak d_{\rm AK}
> =
> C_+-
> \frac{\ell^2}{128\pi^2V}\Gamma(\theta)\ge0.
> \]

This reduces to a quantitative Armstrong estimate on the exact AK\(\Gamma\)-equality class and remains meaningful for near-equality sequences.

A still weaker and plausibly more tractable nonperturbative target is:

> On the class \(W^+(\omega)^\perp=0\), prove
> \[
> \boxed{
> \int|\operatorname{Ric}^{\circ}|^2
> \ge c\int|\nabla\omega|^4.
> }
> \]

This is weaker near a Kähler metric than an \(L^2\)-torsion estimate because the right side is quartic in a small deformation. It retains Armstrong’s qualitative \(P=0\) endpoint and aligns with the Apostolov–Armstrong–Drăghici differential identities.

For a fixed negative Kähler–Einstein host, the perturbative \(L^2\) version is also well posed after fixing scale and quotienting by diffeomorphisms and Kähler–Einstein moduli:
\[
\int|\operatorname{Ric}^{\circ}|^2
\ge c(g_0)\int|\nabla\omega|^2.
\]
Its linearization is an elliptic coercivity statement once gauge and kernel directions are removed. Uniformity over cover towers is genuinely stronger and requires a uniform spectral gap.

Finally, any full almost-Kähler tariff must also control the period defect. A natural companion term is
\[
A\,[1-(\eta+\alpha)^2]_+.
\]
Without controlling this quantity, quantitative Armstrong alone cannot recover the invalid universal step \(A_\omega\ge A(1+\alpha)^2\).

## Corrected core theorem

The defensible Step-42 result is therefore:

\[
\boxed{
C_+
\ge
\frac{(K_\omega\cdot[\omega])^2}{2V}
\,\Gamma(\theta)
=
A(\eta+\alpha)^2\Gamma(\theta),
}
\]
with
\[
\Gamma(\theta)=3\theta^2-2\theta+1,
\]
and equality exactly under the Weyl and constancy conditions above. The stronger replacement \(\eta+\alpha\ge1+\alpha\) requires an additional Lorentzian/Hodge-index period hypothesis and is false in general.