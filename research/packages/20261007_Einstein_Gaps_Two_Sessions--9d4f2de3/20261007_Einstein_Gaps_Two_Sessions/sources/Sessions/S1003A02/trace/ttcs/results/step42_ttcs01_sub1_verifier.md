# TTCS Independent Branch Record

```json
{
  "step_id": 42,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md",
    "Sessions/S1003A02/workspace/scripts/step42_ak_torsion_profile.py",
    "Sessions/S1003A02/workspace/data/step42_ak_torsion_profile.json",
    "Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md",
    "Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md",
    "Knowledge/objects/papers/Four-Manifolds-Curvature-Bounds-and-Convex-Geometry--9dec43e67dff--ae37fe317499/object.md"
  ]
}
```

## Task

Verify, as a strict geometric analyst, the three new results in the Step-42 note: (1) Lemma T (Taubes period lemma) and its Corollaries T1/T2 claiming that the Step-40 'formal common mode' (constant monopole amplitude, closed sign-independent self-dual form psi, all exceptional classes ASD harmonic) is topologically impossible on M = X # k CPbar^2 with b+(X)>=2 and basic classes ±K_X. Check the use of Taubes' SW=>Gr (sign conventions: class e with SW(2e-K_omega) nonzero is represented by J-curves), the blow-up formula, whether K_X·omega has a definite sign, and whether 'nowhere-vanishing self-dual harmonic form' really yields a symplectic form to which these apply. (2) Theorem AKGamma: for every almost-Kähler metric, C+ >= (l^2/(128 pi^2 V)) (3 theta^2 - 2 theta + 1) with l = 8 pi K_omega·[omega], theta = (1/l) int |nabla omega|^2, using LeBrun's conventions s* = s + |nabla omega|^2 = 2W+(omega,omega)+s/3 and Blair's formula int (s+s*) = 8 pi c1·[omega], [omega]^2 = 2V; check the pointwise bound, the Jensen step (sigma = -s sign-unrestricted), the reverse Cauchy-Schwarz step, the claimed equality class, and the identification of the Step-40 common mode as the alpha=0 equality case with beta(r) = 2 theta - 3 theta^2. Check the closed identity C+ = A - k + P/(8 pi^2) normalization against the Step-40 note. (3) Proposition G and G' (tariff ⇐ linear Goldberg estimate; c -> 0 ⇒ unbounded Goldberg ratio), including the constants kappa/(kappa+2) and kappa/(1+kappa). Report every error with its correction, state precisely which hypotheses are needed, and say whether any of these statements is already standard in the literature (LeBrun, Taubes, Armstrong, Apostolov–Drăghici) so that novelty is not overstated. Also judge whether the 'quantitative Armstrong' target in §3 is a correctly posed and genuinely weaker problem than quantitative Goldberg, and propose the sharpest tractable formulation.

## Output

# Scientific verification memo

## Executive findings

1. **Lemma T and Corollaries T1/T2 are valid** under the explicit hypothesis that the Seiberg–Witten basic classes of \(X\), modulo torsion, are exactly \(\pm K_X\), so that those of \(M=X\#k\overline{\mathbb{CP}}^{\,2}\) are exactly
   \[
   \pm K_X+\sum_{i=1}^k\epsilon_iE_i .
   \]
   The Taubes sign convention used in the note is consistent. A nowhere-zero self-dual harmonic form is indeed symplectic, and therefore cannot have zero exceptional period. The “formal common mode” is consequently impossible for actual monopole solutions.

2. The **analytic torsion-profile inequality**
   \[
   C_+\ge \frac{\ell^2}{128\pi^2V}\bigl(3\theta^2-2\theta+1\bigr)
   \]
   is correct, including its constants, Jensen step, and equality conditions.

   The subsequent estimate
   \[
   \frac{\ell^2}{128\pi^2V}\ge A(1+\alpha)^2
   \]
   is not valid under the stated hypotheses. The intersection form has \(b^+\ge2\), so the reverse Cauchy–Schwarz inequality does not apply to arbitrary positive-square classes \(K_X\) and \([\omega]\). This affects the \(A\)-valued version of AK\(\Gamma\), its rearranged tariff inequality, and the universal linear torsion law.

3. The common-mode algebra
   \[
   \delta=4h,\qquad \theta=\frac{h}{2-h},\qquad
   \beta(2-h)=2\theta-3\theta^2
   \]
   is correct. It saturates the analytic profile and additionally has the formal cohomological values \(\alpha=0\) and
   \[
   \frac{|K_X\cdot[\omega]|}{\sqrt{2AV}}=1.
   \]
   Lemma T excludes \(\alpha=0\) for an actual symplectic form on the blow-up.

4. **Proposition G has the correct algebraic constant**
   \[
   \frac{\kappa}{\kappa+2},
   \]
   but it requires, as a separate hypothesis,
   \[
   \frac{P}{8\pi^2}\ge k-2A\theta.
   \]
   That inequality does not follow for all almost-Kähler metrics from the valid part of AK\(\Gamma\).

5. **Proposition G′ has the correct constant**
   \[
   \frac{\kappa}{1+\kappa}.
   \]
   Moreover,
   \[
   \frac{P}{8\pi^2k}\to0
   \quad\Longrightarrow\quad
   \frac{\mathcal N}{P}\to\infty.
   \]
   The converse does not follow: \(\mathcal N/P\to\infty\) can occur while \(P/(8\pi^2k)\) stays away from zero because the exact monopole identity contains other subtractive terms.

---

## 1. Taubes period lemma

### 1.1 Required hypotheses

The precise topological input is:

- \(b^+(X)=b^+(M)\ge2\);
- \(A=K_X^2>0\);
- modulo torsion, the complete basic-class set of \(X\) is \(\{\pm K_X\}\);
- the ordinary blow-up formula therefore gives the complete basic-class set
  \[
  \mathfrak B(M)=
  \left\{
  sK_X+\sum_{i=1}^k\epsilon_iE_i:
  s,\epsilon_i\in\{\pm1\}
  \right\}.
  \]

The phrase “e.g. minimal surfaces of general type” is too broad as written. The supplied sources do not establish that every minimal surface of general type has only the two basic classes \(\pm K_X\). The exact basic-class hypothesis should remain explicit, or a separately justified subclass should be named.

Equalities among canonical and basic classes should formally be stated in \(H^2(M;\mathbb Z)/\mathrm{torsion}\). Torsion does not affect the periods used below.

### 1.2 Taubes sign convention

Let \(K_\omega=-c_1(TM,J)\) be the symplectic canonical class. In the convention used in Step 42, Taubes’ correspondence says that if
\[
SW(2e-K_\omega)\ne0,
\]
then the Poincaré dual of \(e\), when \(e\ne0\), is represented by a \(J\)-holomorphic subvariety for generic \(\omega\)-compatible \(J\). This is consistent with the canonical spin\(^c\) determinant class \(-K_\omega\): the class
\[
-K_\omega+2e=2e-K_\omega
\]
corresponds to the curve class \(e\).

Taubes directly supplies the basic class \(-K_\omega\), and conjugation supplies \(K_\omega\). Hence the assumed basic-class list gives
\[
K_\omega=sK_X+\sum_i\epsilon_iE_i.
\]
Set \(e_i=\epsilon_iE_i\). Then
\[
2e_i-K_\omega
=-sK_X+e_i-\sum_{j\ne i}e_j,
\]
which is another member of the blow-up basic-class list. Likewise,
\[
2sK_X-K_\omega=sK_X-\sum_ie_i
\]
is basic. Since \(e_i\ne0\) and \(sK_X\ne0\), Taubes gives \(J\)-holomorphic subvarieties in all these classes. Their symplectic areas are strictly positive:
\[
e_i\cdot[\omega]>0,\qquad sK_X\cdot[\omega]>0.
\]

It follows that
\[
e_i\cdot[\omega]=|E_i\cdot[\omega]|,
\qquad
sK_X\cdot[\omega]=|K_X\cdot[\omega]|.
\]
Therefore
\[
K_\omega\cdot[\omega]
=
|K_X\cdot[\omega]|+\sum_i|E_i\cdot[\omega]|.
\]

The sign of \(K_X\cdot[\omega]\) is not fixed relative to the initially chosen \(K_X\). It is the sign \(s\) selected by \(K_\omega\) that satisfies
\[
sK_X\cdot[\omega]>0.
\]
Thus the absolute-value formulation in Lemma T is the correct one.

The phrase “represented by \(J\)-holomorphic curves” is best read as “represented by a \(J\)-holomorphic subvariety/current.” Smooth connected representatives are not needed for the period argument.

### 1.3 Corollary T1

Let \(\psi\) be a self-dual harmonic two-form for \(g\). If \(\psi\) has no zeros, then
\[
\psi\wedge\psi=|\psi|_g^2\,d\mu_g>0.
\]
Since \(d\psi=0\), \(\psi\) is a symplectic form inducing the given orientation. Lemma T therefore gives
\[
|E_i\cdot[\psi]|>0
\]
for every exceptional class. Hence a self-dual harmonic form with
\[
E_i\cdot[\psi]=0
\]
must vanish somewhere.

If the harmonic representative of \(E_i\) is anti-self-dual, then for every self-dual harmonic \(\psi\),
\[
E_i\cdot[\psi]=0
\]
by Hodge orthogonality. Thus no nowhere-zero self-dual harmonic form exists.

The conformal statement is also correct. The Hodge star on two-forms is conformally invariant in dimension four. A closed nowhere-zero self-dual form becomes an almost-Kähler form after conformally rescaling \(g\) to make its norm \(\sqrt2\).

### 1.4 Corollary T2

For actual Seiberg–Witten solutions, the harmonic projection of the monopole two-form \(\psi_\epsilon\) is a fixed universal multiple of \(a_\epsilon^+\), where
\[
a_\epsilon=sK_X+\sum_i\epsilon_iE_i
\]
up to the convention-dependent overall sign. Flipping \(\epsilon_i\) changes the harmonic self-dual component by a non-zero multiple of \(E_i^+\).

Consequently:

- if all \(\psi_\epsilon\) have the same harmonic self-dual part, then every \(E_i^+=0\);
- if one \(\psi_\epsilon\) is closed, self-dual, and nowhere zero, then it is symplectic and Lemma T gives \(E_i\cdot[\psi_\epsilon]\ne0\), hence \(E_i^+\ne0\);
- neighboring sign choices therefore have distinct harmonic self-dual parts.

Thus the Step-40 state consisting of a constant-amplitude, closed, nowhere-zero, sign-independent monopole form together with all \(E_i\) anti-self-dual is topologically impossible.

This mechanism is already present in LeBrun’s proof of Proposition 3.2 in the supplied 2001 paper: equality would force zero exceptional symplectic area, while the sign-flipped basic class and Taubes produce a pseudoholomorphic exceptional curve of positive area. Lemma T packages that standard argument into a useful period identity.

---

## 2. The analytic part of Theorem AK\(\Gamma\)

Set
\[
\delta=s^*-s=|\nabla\omega|^2,\qquad
u=\frac{\omega}{\sqrt2},\qquad |u|=1,\qquad
\sigma=-s.
\]
From
\[
s^*=2W^+(\omega,\omega)+\frac{s}{3}
\]
one gets
\[
W^+(u,u)=\frac{s}{6}+\frac{\delta}{4}
=-\frac{\sigma}{6}+\frac{\delta}{4}.
\]

### 2.1 Pointwise Weyl estimate

For a trace-free self-adjoint endomorphism \(W:\Lambda^+\to\Lambda^+\) and a unit vector \(u\),
\[
|W|^2\ge\frac32\,W(u,u)^2.
\]
Indeed, after fixing \(W(u,u)=q\), the least norm occurs when \(u\) is an eigenvector and the other two eigenvalues are both \(-q/2\).

Therefore the \(C_+\)-density satisfies
\[
\begin{aligned}
\frac{|W^+|^2}{2\pi^2}+\frac{s^2}{96\pi^2}
&\ge
\frac{3}{4\pi^2}
\left(-\frac{\sigma}{6}+\frac{\delta}{4}\right)^2
+\frac{\sigma^2}{96\pi^2}\\
&=
G(\sigma,\delta),
\end{aligned}
\]
where
\[
G(\sigma,\delta)
=
\frac{2\sigma^2+(3\delta-2\sigma)^2}{192\pi^2}.
\]
Its Hessian has eigenvalues
\[
\frac{5-\sqrt{17}}{64\pi^2},
\qquad
\frac{5+\sqrt{17}}{64\pi^2},
\]
both strictly positive. No pointwise sign for \(\sigma=-s\) is required.

### 2.2 Blair identity and Jensen

Blair’s formula gives
\[
\int_M(s+s^*)\,d\mu
=
-8\pi K_\omega\cdot[\omega].
\]
With
\[
\ell=8\pi K_\omega\cdot[\omega]>0,
\qquad
\theta=\frac1\ell\int_M\delta\,d\mu,
\]
this becomes
\[
\int_M(2\sigma-\delta)\,d\mu=\ell.
\]
Hence
\[
\bar\delta=\frac{\theta\ell}{V},
\qquad
\bar\sigma=\frac{(1+\theta)\ell}{2V}.
\]

Strict convexity and Jensen yield
\[
C_+\ge V G(\bar\sigma,\bar\delta)
=
\frac{\ell^2}{128\pi^2V}
\left(3\theta^2-2\theta+1\right).
\]
Thus the analytic profile
\[
\boxed{
C_+\ge
\frac{\ell^2}{128\pi^2V}\Gamma(\theta),
\qquad
\Gamma(\theta)=3\theta^2-2\theta+1
}
\]
is correct.

### 2.3 Exact defect decomposition and equality

Let
\[
q=W^+(u,u).
\]
Then there is an exact decomposition
\[
C_+-
\frac{\ell^2}{128\pi^2V}\Gamma(\theta)
=
\mathfrak d_{\mathrm{sat}},
\]
where
\[
\begin{aligned}
\mathfrak d_{\mathrm{sat}}
={}&
\frac1{2\pi^2}
\int_M
\left(
|W^+|^2-\frac32q^2
\right)d\mu\\
&+
\int_M
G(\sigma-\bar\sigma,\delta-\bar\delta)\,d\mu
\ge0.
\end{aligned}
\]

Equality holds exactly when

1. \(u\) is an eigenvector of \(W^+\) and
   \[
   W^+|_{u^\perp}=-\frac12W^+(u,u)\operatorname{Id};
   \]
2. \(\sigma\) and \(\delta\) are constant.

Equivalently, in an orthonormal basis beginning with \(u\),
\[
W^+=\operatorname{diag}(\lambda,-\lambda/2,-\lambda/2),
\]
and \(s,s^*\) are constant.

This is somewhat narrower than LeBrun’s general saturated class. LeBrun’s Definition 2.3 requires \(s+s^*\) constant, \(\omega\) in the lowest Weyl eigenspace, and the other two eigenvalues equal. The profile equality requires \(s\) and \(s^*\) separately constant. Moreover,
\[
\lambda
=
\frac{\ell}{12V}(2\theta-1).
\]
Thus \(\omega\) is the lowest eigenvector only when \(\theta<1/2\). At \(\theta>1/2\), it is the highest eigenvector. At the LeBrun minimizer \(\theta=1/3\), the two notions agree.

---

## 3. The topological prefactor in AK\(\Gamma\)

Define
\[
a_i=|E_i\cdot[\omega]|,
\qquad
\alpha=\frac{\sum_i a_i}{\sqrt{2AV}},
\qquad
\eta=\frac{|K_X\cdot[\omega]|}{\sqrt{2AV}}.
\]
Lemma T gives the exact identity
\[
\ell
=
8\pi\sqrt{2AV}\,(\eta+\alpha).
\]
Therefore
\[
\boxed{
\frac{\ell^2}{128\pi^2V}
=
A(\eta+\alpha)^2.
}
\]

The universally valid torsion-profile statement is consequently
\[
\boxed{
C_+\ge A(\eta+\alpha)^2\Gamma(\theta).
}
\]

There is no general inequality \(\eta\ge1\) when \(b^+\ge2\). The reverse Cauchy–Schwarz inequality used in the note applies in a Lorentzian subspace with one positive direction, not to arbitrary positive-square vectors in an intersection form with at least two positive directions.

### 3.1 Geometric illustration

Let \(X\) be a Kähler surface with a non-zero holomorphic two-form \(\Omega\), and let \(\omega_0\) be a Kähler form. Put
\[
\omega_t=\omega_0+t\,\operatorname{Re}\Omega.
\]
The two summands are orthogonal self-dual forms for the Kähler metric, so
\[
\omega_t\wedge\omega_t
=
\omega_0\wedge\omega_0
+t^2\operatorname{Re}\Omega\wedge\operatorname{Re}\Omega
>0.
\]
Thus every \(\omega_t\) is symplectic. The path preserves the symplectic canonical class, while type considerations give
\[
K_X\cdot[\operatorname{Re}\Omega]=0.
\]
Hence
\[
K_X\cdot[\omega_t]=K_X\cdot[\omega_0]
\]
is constant, whereas
\[
[\omega_t]^2=[\omega_0]^2+t^2[\operatorname{Re}\Omega]^2
\]
grows with \(t\). Thus
\[
\eta_t=
\frac{|K_X\cdot[\omega_t]|}{\sqrt{K_X^2[\omega_t]^2}}
\longrightarrow0.
\]
Choosing compatible metrics makes these genuine almost-Kähler examples. Small symplectic blow-ups retain the same mechanism on \(X\#k\overline{\mathbb{CP}}^{\,2}\).

### 3.2 Corrected rearrangement

Writing
\[
p=\frac{P}{8\pi^2},
\]
the Chern–Gauss–Bonnet identity gives
\[
C_+=A-k+p.
\]
Therefore the corrected profile is
\[
\boxed{
p\ge
k-A+A(\eta+\alpha)^2\Gamma(\theta).
}
\]

The formula in the note,
\[
p\ge
k-A(2\theta-3\theta^2)
+A\bigl[(1+\alpha)^2-1\bigr]\Gamma(\theta),
\]
requires the additional period hypothesis \(\eta\ge1\).

A natural sufficient setting is the Kähler case \(\theta=0\). Then the relevant classes lie in the real \((1,1)\)-subspace, where the Hodge index theorem supplies the required reverse inequality. The Step-38 Kähler tariff is therefore unaffected.

For general almost-Kähler metrics, the standard LeBrun estimate
\[
C_+\ge\frac{2A}{3}
\]
still holds by the monopole-class/convex-hull argument in the supplied papers. It does not arise from the fixed symplectic-canonical period \(\ell\) when \(\eta<1\). Universally one may retain
\[
C_+\ge
\max\left\{
\frac{2A}{3},
\frac{\ell^2}{128\pi^2V}\Gamma(\theta)
\right\}.
\]

---

## 4. Step-40 common mode

Put \(r=2-h\), \(s=-4\), and use the Step-40 relations
\[
W^+(n,n)=\frac43-r,
\qquad
r^2V=8\pi^2A.
\]
The almost-Kähler identity gives
\[
-\frac23+\frac{\delta}{4}=\frac43-r,
\]
hence
\[
\delta=4(2-r)=4h.
\]
Blair’s identity gives
\[
\ell=(8-4h)V=4rV=\frac{32\pi^2A}{r}.
\]
Therefore
\[
\theta=\frac{\delta V}{\ell}
=\frac{h}{2-h}.
\]
Also,
\[
\frac{\ell^2}{128\pi^2V}=A,
\]
so the formal state has
\[
\eta=1,\qquad \alpha=0.
\]

Finally,
\[
\begin{aligned}
2\theta-3\theta^2
&=
\frac{2h}{2-h}-\frac{3h^2}{(2-h)^2}\\
&=
\frac{4h-5h^2}{(2-h)^2}\\
&=
\frac{16}{2-h}-5-\frac{12}{(2-h)^2}\\
&=\beta(2-h).
\end{aligned}
\]
Thus the common mode exactly saturates the analytic profile and the formal \(\eta=1,\alpha=0\) topological specialization.

Lemma T excludes \(\alpha=0\) on the actual blow-up because every exceptional period is strictly positive. This is a qualitative exclusion only; the period lemma by itself does not give a uniform lower estimate for \(\alpha\).

---

## 5. Closed identity normalization

With
\[
P=\int_M|\operatorname{Ric}^{\circ}|^2\,d\mu
\]
and
\[
2\chi(M)+3\tau(M)=A-k,
\]
Chern–Gauss–Bonnet gives
\[
A-k
=
\frac1{4\pi^2}
\int_M
\left(
2|W^+|^2+\frac{s^2}{24}
-\frac{|\operatorname{Ric}^{\circ}|^2}{2}
\right)d\mu.
\]
Therefore
\[
C_+
=
\frac1{2\pi^2}\int|W^+|^2
+\frac1{96\pi^2}\int s^2
=
A-k+\frac{P}{8\pi^2}.
\]

For the Step-40 normalization \(s=-4\),
\[
P
=
4\int|W^+|^2+\frac43V-8\pi^2(A-k),
\]
exactly as recorded there. The normalizations are consistent.

---

## 6. Proposition G

Assume \(\kappa>0\) and write \(p=P/(8\pi^2)\). If both
\[
p\ge k-2A\theta
\]
and
\[
p\ge\kappa A\theta
\]
hold, then
\[
A\theta\le\frac p\kappa,
\]
and hence
\[
p\ge k-\frac{2p}{\kappa}.
\]
Thus
\[
\boxed{
p\ge\frac{\kappa}{\kappa+2}\,k.
}
\]

The constant is correct and sharp for this two-line algebraic reduction.

Under the stated Step-42 hypotheses alone, however, the first input \(p\ge k-2A\theta\) is unavailable because it used \(\eta\ge1\). Proposition G is therefore valid in any class for which the period inequality
\[
|K_X\cdot[\omega]|\ge\sqrt{2AV}
\]
is separately known, or more directly in any class where \(p\ge k-2A\theta\) has been established by another argument.

---

## 7. Proposition G′

Assume Theorem N supplies
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

For a sequence with
\[
c_j=\frac{P_j}{8\pi^2k_j}>0,
\]
Theorem N gives
\[
\frac{\mathcal N_j}{P_j}
\ge
\frac{8\pi^2k_j-P_j}{P_j}
=
\frac{1-c_j}{c_j}.
\]
Thus, if \(c_j\to c\in(0,1)\),
\[
\liminf_j\frac{\mathcal N_j}{P_j}
\ge\frac{1-c}{c}.
\]
In particular,
\[
c_j\to0
\quad\Longrightarrow\quad
\frac{\mathcal N_j}{P_j}\to\infty.
\]

The reverse implication is not supplied by Theorem N. The ratio \(\mathcal N/P\) can diverge while \(P/(8\pi^2k)\) remains bounded away from zero, because large Nijenhuis energy may be offset by the other subtractive terms in the exact identity. Therefore “precisely” should be replaced by the one-way implication above.

For the stated cell coefficient \(c\approx0.9956627\),
\[
\frac{1-c}{c}\approx0.004356,
\qquad
\frac{c}{1-c}\approx229.6.
\]
Hence a replica to which \(P\ge\kappa\mathcal N\) applies would force
\[
\kappa\lesssim229.6.
\]
This is a necessary numerical consequence, not evidence that every smaller \(\kappa\) is attained.

---

## 8. Literature position

- **Lemma T:** a direct application of the blow-up formula and Taubes’ \(SW\Rightarrow Gr\) theorem. LeBrun’s 2001 Proposition 3.2 already uses the essential exceptional-period argument to rule out equality on a blow-up. The packaged identity is useful, but its ingredients and core obstruction are standard.

- **Blair and almost-Kähler identities:** standard and correctly normalized in the note.

- **The profile polynomial**
  \[
  \Gamma(\theta)=3\theta^2-2\theta+1
  \]
  is an elementary refinement obtained by retaining the total torsion parameter before minimizing. The minimum
  \[
  \min_{\theta\ge0}\Gamma(\theta)=\frac23
  \quad\text{at}\quad \theta=\frac13
  \]
  reproduces LeBrun’s known \(2/3\) constant. The explicit one-parameter profile does not appear verbatim in the supplied sources, but it is built entirely from their standard identities.

- **Equality geometry:** LeBrun’s Proposition 2.4 and the 2006 saturated almost-Kähler formalism already describe the Weyl eigenvalue structure and constant \(s+s^*\). The profile equality adds constancy of \(s\) and \(s^*\) separately.

- **Armstrong:** the supplied LeBrun source states the established theorem that a compact Einstein almost-Kähler four-manifold with \(\omega\) an eigenvector of \(W^+\) is Kähler.

- **Apostolov–Armstrong–Drăghici:** the supplied source states that, in the saturated setting, Kählerness is equivalent to \(J\)-invariance of the Ricci tensor.

- **Propositions G and G′:** these are algebraic consequences of the preceding inequalities rather than separate geometric theorems.

---

## 9. Quantitative Armstrong formulation

For a specified class \(\mathcal S\) of saturated almost-Kähler pairs, the quantity
\[
\kappa_{\mathcal S}
=
\inf_{\substack{(g,\omega)\in\mathcal S\\ \theta>0}}
\frac{P(g)}{8\pi^2A\theta}
\]
is well posed and scale invariant. The statement \(\kappa_{\mathcal S}>0\) is strictly weaker than an estimate over all almost-Kähler metrics because \(\mathcal S\) imposes the Weyl eigenvector condition and scalar/star-scalar structure. Armstrong’s theorem only says that the numerator cannot vanish when \(\theta>0\); it does not imply a uniform positive infimum along a degenerating sequence or a tower of covers.

The most tractable fixed-host version is local:

> Let \((Y,g_0,\omega_0)\) be a compact \(s<0\) Kähler–Einstein surface. After fixing scale and quotienting by diffeomorphisms and Kähler–Einstein moduli, there should exist \(\varepsilon,c>0\) such that every saturated almost-Kähler pair \((g,\omega)\) with
> \[
> \|(g,\omega)-(g_0,\omega_0)\|_{C^{2,\alpha}}<\varepsilon
> \]
> satisfies
> \[
> \frac{P(g)}{8\pi^2}\ge cA\theta.
> \]

At the linearized level, for variations \(v=(H,\dot\omega)\) satisfying the linearized almost-Kähler and saturation equations, this reduces to
\[
\|\mathcal T v\|_{L^2}^2
\le
C(g_0)\,
\|\mathcal L_{\mathrm{Ric}^{\circ}}v\|_{L^2}^2
\]
after removing gauge, scale, and Kähler–Einstein kernel directions. Koiso’s kernel statement cited in Step 40 supplies the essential fact that Einstein kernel directions carry no first-order torsion. On a fixed host, this is a standard elliptic-coercivity problem. A cover-uniform result additionally requires the corresponding operator constant and nonlinear elliptic estimates to remain uniform through the cover tower.

For near-saturating metrics, the exact defect
\[
\mathfrak d_{\mathrm{sat}}
=
C_+-
\frac{\ell^2}{128\pi^2V}\Gamma(\theta)
\]
suggests the robust form
\[
\boxed{
\frac{P}{8\pi^2}
+C\,\mathfrak d_{\mathrm{sat}}
\ge cA\theta.
}
\]
This reduces to quantitative Armstrong when \(\mathfrak d_{\mathrm{sat}}=0\), while still addressing sequences that only approach the Weyl/Jensen equality structure.

For a per-blow-up tariff in the full almost-Kähler category, one further needs control of the period-angle loss
\[
\eta=\frac{|K_X\cdot[\omega]|}{\sqrt{2AV}}.
\]
A suitable companion estimate would have the form
\[
A\bigl[1-(\eta+\alpha)^2\bigr]_+
\le
C_0\left(
\frac{P}{8\pi^2}
+\mathfrak d_{\mathrm{sat}}
\right).
\]
Without such period control, a quantitative Armstrong estimate can suppress the formal common mode but does not by itself restore Proposition G for all almost-Kähler metrics.