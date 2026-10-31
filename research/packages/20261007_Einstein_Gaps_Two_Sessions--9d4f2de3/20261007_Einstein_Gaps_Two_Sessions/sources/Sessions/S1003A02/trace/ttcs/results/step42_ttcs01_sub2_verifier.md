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

# Verification memo: Step 42 (Taubes period lemma, Theorem AKΓ, Propositions G and G′)

## 0. Results at a glance

| Item | Status |
|---|---|
| Lemma T, Corollaries T1 and T2 | Correct under stated hypotheses. Standard in the literature. |
| Closed identity \(C_+=A-k+P/8\pi^2\) | Correct. Consistent with the Step-40 normalization. |
| AKΓ in its \(\ell\)-form, \(C_+\ge A_\omega\,\Gamma(\theta)\) with \(A_\omega:=(K_\omega\cdot\omega)^2/\omega^2\) | Correct. |
| AKΓ in its \(A\)-form, \(A_\omega\ge A(1+\alpha)^2\) | **Not valid.** The reverse Cauchy–Schwarz step does not hold when \(b^+\ge2\). An explicit symplectic family has \(A_\omega\to0\). |
| Readings 1–3 | Survive (reading 1 via Hodge index; reading 3 because \(A_\omega=A\) holds in the formal state). |
| Reading 4 (linear torsion law) and Proposition G | Hold only under an extra period hypothesis. |
| Proposition G′ | Constants correct; one word ("precisely") must be weakened. |
| Section 3 "quantitative Armstrong" target | Mis-located. On the exact saturated class, Chern–Weil information already settles it. The real problem sits elsewhere (§5). |

The Blair-connection formulas that LeBrun gives (Convex Geometry paper, eqs. (10)–(11)) yield two further inequalities for every almost-Kähler metric. They exclude the Step-40 common mode **quantitatively**. Under a period hypothesis they also give a per-blow-up tariff for \(k>A/4\) in the almost-Kähler category (§4).

---

## 1. Lemma T, T1, T2

**Symplecticity.** A closed self-dual 2-form \(\psi\) satisfies \(\psi\wedge\psi=|\psi|^2d\mu\). If \(\psi\) is nowhere zero, it is symplectic for the given orientation. Rescaling \(g\) by \(|\psi|/\sqrt2\) keeps it self-dual and harmonic, so \(g\) becomes conformally almost-Kähler. Taubes' theorems need no metric. ✓

**Sign convention of SW⇒Gr.** Taubes (JAMS 1996) parametrizes spin\(^c\) structures as \(S_e=S_{\rm can}\otimes E\), with \(c_1(S_e)=2e-K_\omega\). For \(b^+>1\), \(SW(S_e)\ne0\) implies that \(e\) is carried by a \(J\)-curve for generic \(J\). Hence \(\omega\cdot e>0\) when \(e\ne0\); this is an area, so it does not depend on \(J\). The note uses exactly this convention. ✓

**Blow-up formula.** If \(X\) has simple type with basic classes \(\pm K_X\) (minimal Kähler surfaces with \(b^+>1\) qualify), then the basic classes of \(M\) are \(\pm K_X+\sum\pm E_i\). The canonical class \(K_\omega\) is basic (Taubes, plus charge conjugation). The two checks:

- \(2e_i-K_\omega=-(K_\omega-2e_i)\), which is a sign-flipped basic class. ✓
- \(2sK_X-K_\omega=sK_X-\sum e_i\), which is basic. ✓

**Sign of \(K_X\cdot\omega\).** The sign \(s\) is not universal. Both \(s=\pm1\) occur: \((X,-\omega_K)\) has canonical class \(-K_X\). For each \(\omega\), however, \(K_X\cdot\omega\neq0\) and \(\operatorname{sign}(K_X\cdot\omega)=s\). Writing \(|K_X\cdot\omega|\) is therefore correct, and \(\ell>0\).

**Needed hypotheses:**
- \(b^+(X)\ge2\) (no chambers);
- \(X\) of SW simple type with basic classes exactly \(\pm K_X\), \(K_X^2>0\);
- \(E_i\) the pulled-back exceptional classes.

**Novelty.** The decomposition \(K_\omega=K_{\min}+\sum E_i\) with \(\omega\cdot E_i>0\), and \(K\cdot\omega\ge0\), are standard consequences of SW=Gr in symplectic topology (Taubes; Li–Liu; McDuff). LeBrun (*Ricci curvature…*, end of the proof of Prop. 3.2) uses precisely this argument: \(E_j\) is carried by a pseudo-holomorphic sphere, which contradicts \([\omega]\cdot E_j=0\). T1 is immediate from this. T2 is the same argument applied to the formal state.

**T2 check.** Closedness of \(\psi_\epsilon\propto F^+_{A_\epsilon}\) forces \(F^+\) to be harmonic. Its class is then \(\propto a_\epsilon^{+}\). Sign-independence gives \(E_i^+=0\). With \(\psi=rn\) nowhere zero, T1 gives a contradiction. ✓

**Bolt remark.** "Zero period *precisely because* the form vanishes on the bolt" is specific to the \(U(2)\)-symmetric model. In general, a zero period on an embedded sphere does not force vanishing on it. Zero sets of generic self-dual harmonic forms are circles.

---

## 2. Theorem AKΓ

### What checks out

- **Closed identity.** Gauss–Bonnet plus signature gives \(\frac1{2\pi^2}\!\int|W^+|^2+\frac1{96\pi^2}\!\int s^2=(2\chi+3\tau)+\frac1{8\pi^2}\!\int|\mathring r|^2\), with \(2\chi+3\tau=A-k\). At \(s=-4\) this is Step 40's \(P=4W_++\tfrac43V-8\pi^2(A-k)\). ✓
- **Conventions.** \(W^+(\omega,\omega)=2W^+(u,u)\), so \(W^+(u,u)=s/6+\delta/4\). Kähler check: eigenvalue \(s/6\), \(|W^+|^2=s^2/24\). ✓
- **Pointwise bound.** \(|W^+|^2\ge\frac32W^+(u,u)^2\) for any trace-free symmetric \(3\times3\) matrix and unit \(u\). This gives \(G=[2\sigma^2+(3\delta-2\sigma)^2]/192\pi^2\). ✓
- **Blair.** \(\int(2\sigma-\delta)=\ell\). ✓
- **Jensen.** Only convexity of \(G\) on \(\mathbb R^2\) is used, so no sign constraint on \(\sigma\) is needed. One finds \(VG(\bar\sigma,\bar\delta)=\frac{\ell^2}{V}\cdot\frac{3/2\,(1-2\theta+3\theta^2)}{192\pi^2}=\frac{\ell^2\Gamma(\theta)}{128\pi^2V}\). ✓

**Equality class of the \(\ell\)-form.** \(W^+=\mathrm{diag}(\lambda,-\lambda/2,-\lambda/2)\) along \(\omega\), and \(s,s^*\) individually constant. This is LeBrun's *saturated* class (Def. 2.3 of the 2006 paper), modified in two ways:
- it is narrower, since \(s\) and \(s^*\) must each be constant, not just \(s+s^*\);
- it is wider, since \(\omega\) need not be the lowest eigenvector (\(\lambda>0\) iff \(\theta>1/2\)).

### The error

Note that \(\ell^2/(128\pi^2V)=(K_\omega\cdot\omega)^2/\omega^2=:A_\omega\). The step \(|K_X\cdot\omega|\ge\sqrt{K_X^2\,\omega^2}\) holds iff the plane \(\mathrm{span}\{K_X,[\omega]\}\) is not positive definite. Inside \(H^2(M)\) of signature \((b^+,b^-)\) with \(b^+\ge2\), positive-definite planes exist. The script hides this: `prefactor_at_area_zero` substitutes \(\ell=8\pi\sqrt{2AV}\), so it encodes the inequality as an identity.

**Counterexample to the step.** Take \(X\) minimal of general type with \(p_g\ge1\), Kähler \((g,\omega_K)\), and holomorphic \(\vartheta\ne0\). Set
\[
\omega_t=\omega_K+t\,\mathrm{Re}\,\vartheta .
\]
- \(\omega_t\) is self-dual harmonic and pointwise \(\perp\omega_K\), so it is nowhere zero, hence symplectic.
- It is almost-Kähler for the conformal metric \(g_t=(|\omega_t|_g/\sqrt2)\,g\).
- \(K_{\omega_t}=K_X\) by deformation.
- \(K_X\cdot[\mathrm{Re}\,\vartheta]=0\), since \(K_X\) is of type \((1,1)\).
- \([\omega_t]^2=\omega_K^2+t^2\int|\mathrm{Re}\,\vartheta|^2\).

Hence \(A_{\omega_t}\to0\). The same works on blow-ups. This refutes the proof step. Whether the final inequality \(C_+\ge A\Gamma(\theta)\) still holds is unresolved: along this family \(\theta_t\) presumably grows, and \(C_+\ge2A/3\) holds by LeBrun anyway.

**Correct hypothesis (H\(_L\)).** Decompose \([\omega]=c\,K_X+\eta_X+\sum c_iE_i\) with \(\eta_X\perp K_X\) in \(H^2(X)\). Then
\[
\text{(H}_L)\iff \eta_X^2\le\sum_i a_i^2 .
\]
This holds for Kähler metrics, because \(K_X\) and \(\omega\) lie in the Lorentzian \(H^{1,1}\). It also holds whenever the \(X\)-part of the period stays in the \(K_X\)-Lorentzian slice; for example, \(\eta_X=0\), as in perturbations of a KE period along \(H^{1,1}\). It fails for perturbations along \(H^{2,0}\oplus H^{0,2}\), which is the counterexample direction.

### Status of the readings

| Reading | Status | Reason |
|---|---|---|
| 1 (Kähler) | Correct | \(\theta=0\) means \(\nabla\omega=0\), so \(J_\omega\) is integrable and Hodge index gives H\(_L\). This is the Step-38 tariff. |
| 2 | Correct as \(C_+\ge\frac23 A\) | In the AK category alone one only gets \(\frac23(K_\omega^+)^2\) (see (i) in §4). The \(A\) version comes from LeBrun's sign-chosen monopole class, not from \(K_\omega\). |
| 3 | Verified | \(\delta=4h\), \(\ell=4rV\), \(A_\omega=A\) exactly (forced by \(\mathcal W=0\)), \(\theta=h/(2-h)\), \(2\theta-3\theta^2=16/r-5-12/r^2=\beta(r)\). The common mode is the equality case with \(A_\omega=A\). |
| 4 (saving \(\le2A\theta\)) | Requires H\(_L\) | Without it, only saving \(\le\frac13(A-A_\omega)+2A_\omega\theta\) is available (if \((K_\omega^+)^2\ge A\)). |

---

## 3. Propositions G and G′

**Proposition G.** The algebra \(p\ge k-2p/\kappa\Rightarrow p\ge\kappa k/(\kappa+2)\) is correct. It uses \(p\ge k-2A\theta\), so **H\(_L\) is required** on the class \(\mathcal C\). Without H\(_L\), the hypothesis must also pay the polarization defect: a hypothesis \(p\ge\kappa[A_\omega\theta+\frac16(A-A_\omega)]\), together with \((K_\omega^+)^2\ge A\), gives the same conclusion. Keeping the quadratic term sharpens the result slightly: \(p\ge k-2p/\kappa+3p^2/(\kappa^2A)\).

**Proposition G′.** This uses Theorem N, valid for all metrics, so it is unaffected by the AKΓ error.

- \(P\ge\kappa\mathcal N\) together with \(\mathcal N\ge8\pi^2k-P\) gives \(P\ge8\pi^2k\,\kappa/(1+\kappa)\). ✓
- The ratios are measured at the Yamabe representative \(\hat g\). For \(Y<0\), \(C_+\) is minimized there, so \(P(g)\ge P(\hat g)\). ✓
- \(\mathcal N\) is evaluated at \(\hat g\) on the chosen simultaneous solutions.
- Numbers: \((1-c)/c=0.0043373/0.99566=0.004356\); \(c/(1-c)\approx229.6\). ✓

**Correction.** The assertion that \(c\to0\) is "*precisely*" an unbounded Goldberg ratio should read "*only if*". An unbounded \(\mathcal N/P\) does not force \(c\to0\).

---

## 4. What the Blair connection adds

All almost-Kähler metrics satisfy the following. The inputs are:
- \(iF_B^+=\frac{s+s^*}8\omega+W^+(\omega)^\perp\) and \(iF_B^-=\frac{s-s^*}8\hat\omega+\mathring\varrho\), with \(|\hat\omega|=\sqrt2\) (LeBrun 2006, eqs. (10)–(11));
- \([iF_B/2\pi]=-K_\omega\);
- Lemma 2.1 and its ASD analogue, \(\int|F^\pm|^2\ge4\pi^2|(K_\omega^\pm)^2|\);
- \(|\mathring r|^2\ge2|\mathring\varrho|^2\), with equality iff Ricci is \(J\)-invariant.

**Notation.** In an orthonormal frame \((u,e_2,e_3)\) of \(\Lambda^+\):
- \(a=W^+(u,u)\);
- \(b\) is the off-diagonal vector, so \(|W^+(\omega)^\perp|^2=2|b|^2\);
- \(C_0\) is the trace-free part of the \(\omega^\perp\) block;
- \(L=2\sigma-\delta=-(s+s^*)\);
- \(X:=\frac1{128\pi^2}\int|\nabla\omega|^4\).

Two facts drive everything. First, \(|W^+|^2=\frac32a^2+2|b|^2+|C_0|^2\). Second, \(\int|F_B^+|^2=\int L^2/32+2\int|b|^2\ge4\pi^2(K_\omega^+)^2\).

**(i) Exact refinement of LeBrun's 2/3 bound.**
\[
C_+=\tfrac23(K_\omega^+)^2+\tfrac1{96\pi^2}\!\int(s-2s^*)^2+\tfrac2{3\pi^2}\!\int|b|^2+\tfrac1{6\pi^2}\!\int|F_B^+-\mathcal H F_B^+|^2+\tfrac1{2\pi^2}\!\int|C_0|^2 .
\]
- Applying Jensen to the second term gives \(C_+\ge\frac23(K_\omega^+)^2+\frac13A_\omega(1-3\theta)^2\). This is never weaker than the \(\ell\)-form of AKΓ, since \(A_\omega\le(K_\omega^+)^2\).
- Kähler cscK gives equality: \(\frac23+\frac13\).

**(iii) Weight-1/4 combination.**
\[
C_+\ge\tfrac12(K_\omega^+)^2+X+\tfrac1{256\pi^2}\!\int(2\sigma-3\delta)^2 .
\]
Equality forces \(b=0\), \(C_0=0\) and \(\sigma=\frac32\delta\), i.e. \(W^+(u,u)=0\), so **\(W^+\equiv0\)**. For an ASD almost-Kähler metric the Weitzenböck formula gives \(\delta=-2s/3\) automatically.

**(ii) Ricci–Blair tariff.**
\[
\frac{P}{8\pi^2}\ \ge\ \Bigl(\sqrt{|(K_\omega^-)^2|}-\sqrt X\Bigr)_+^2,\qquad |(K_\omega^-)^2|=(K_\omega^+)^2-(A-k).
\]
- Proof: \(\mathring\varrho=iF_B^-+\delta\hat\omega/8\), and \(\|\delta\hat\omega/8\|_{L^2}=2\pi\sqrt X\).
- At \(\delta=0\) this is exactly the Kähler/Step-38 tariff.
- Under (H\(_+\)), \((K_\omega^+)^2\ge A\) (implied by H\(_L\)), we get \(|(K_\omega^-)^2|\ge k\).
- Diffuse torsion therefore pays a cost of order \(k\). The exceptional charge sits in \(h^-\) and must be absorbed by \(J\)-invariant traceless Ricci, unless the \(L^4\) torsion energy is \(\gtrsim128\pi^2k\).

**Consequences**

1. **Common mode excluded quantitatively, without Lemma T.**
   - The common mode has \(A_\omega=A\) and \(X=Ah^2/(2-h)^2\).
   - (ii) requires \(p\ge A(\sqrt h-h/(2-h))^2\approx Ah\).
   - The state actually has \(p=A[h-16/(2-h)+5+12/(2-h)^2]\approx Ah^2/4\).
   - At \(h=0.1\): the state has \(0.00305A\), while (ii) requires \(0.0695A\).
   - The curvature data of the formal state are therefore inconsistent with Chern–Weil for the Blair connection.

2. **Exact AKΓ-equality class.** Here \(X=\theta^2A_\omega\), and Gauss–Bonnet gives \(p=k-A+A_\omega\Gamma(\theta)\) exactly. Combining with (ii) at \(A_\omega=A\):
   - either \(\theta=0\), or \(\theta\ge1-\sqrt{k/A}\);
   - consequently \(p\ge(2\sqrt k-\sqrt A)^2\).
   - The only formally admissible strictly almost-Kähler Einstein point is \(k=A/4\), \(\theta=\tfrac12\), \(W^+\equiv0\).
   - That point is excluded by Armstrong. It is also excluded by LeBrun's Theorem 3.8 (no ASD Einstein metric for \(k\ge A/4\)).
   - Monotone case (\(K^-=0\), \(k=0\)): this reduces to LeBrun's Theorem 4.10.

3. **Tariff for \(k>A/4\) under (H\(_+\)).** From (ii), \(\sqrt X\ge\sqrt k-\sqrt p\). From (iii), \(X\le A/2-k+p\). Together:
\[
\frac{P}{8\pi^2}\ \ge\ \frac{(4k-A)^2}{16k}\qquad(A/4<k).
\]
   - At \(k=A/3\) this gives \(A/48\), whereas LeBrun gives \(0\).
   - Optimizing the weight \(t\in[0,1/3]\) improves this to about \(0.023A\).
   - Einstein almost-Kähler metrics satisfying (H\(_+\)) are excluded for \(k>A/4\).
   - The extremal configuration is ASD, matching LeBrun's ASD threshold.

These computations depend only on LeBrun's eqs. (10)–(11) and the elementary algebra above. A symbolic re-derivation of \(|F_B^\pm|^2\) on an explicit strictly almost-Kähler example (e.g. a cohomogeneity-one family) would confirm the normalizations. An inequality of type (ii) may already appear in LeBrun's *Einstein metrics, symplectic minimality, and pseudo-holomorphic curves* (AGAG 2005, ref. [27] of the 2006 paper). That paper should be read before any novelty is asserted.

---

## 5. The "quantitative Armstrong" target

**On the exact saturated class with \(s,s^*\) constant**, \(P\) is an explicit function of \((\theta,A_\omega)\), and (ii) already gives explicit lower bounds (consequence 2 in §4). Armstrong's Bianchi-identity argument is needed only at the single point \(k=A/4\). So as posed — "\(P\ge\kappa A\theta\) on the saturating class" — the problem is formally weaker than quantitative Goldberg, but it is not where the difficulty lies.

**Near-saturation is not forced.** By (i), \(\|b\|^2\le\frac{3\pi^2}2(A/3-k+p)\). This is \(O(A)\) throughout the open range, so near-minimizers need not have \(\omega\) close to an eigenvector of \(W^+\).

**Where the open problem actually lies.** In the almost-Kähler category with (H\(_+\)), what remains is \(k\le A/4\). There, (ii) and (iii) allow \(p\to0\) with \(X\in[k,\,A/2-k]\), i.e. *concentrated* \(L^4\) torsion.

**Sharpest formulation.** An \(L^4\) Goldberg estimate
\[
\int|\mathring r|^2\ \ge\ \frac{\kappa}{16}\int|\nabla\omega|^4
\]
combined with (ii) gives \(P/8\pi^2\ge\kappa k/(1+\sqrt\kappa)^2\), for any \(k\). Compared with the note's linear \(L^1\) target:
- It is perturbatively free: near a Kähler host it is quartic against quadratic. The note's linear \(L^1\) target is quadratic against quadratic, and so carries the cover-tower spectral-gap problem.
- It is therefore strictly weaker than the note's target near Kähler hosts, and is a purely nonperturbative statement.
- It still implies Goldberg for Einstein almost-Kähler metrics, so it is open in general.

**Tractable sub-case: \(L^4\) quantitative Armstrong.** Restrict to almost-Kähler metrics with \(W^+(\omega)^\perp=0\), which is Armstrong's hypothesis and the setting of the AAD differential identities. On that class, prove \(\int|\mathring r|^2\ge\kappa'\int|\nabla\omega|^4\). Armstrong's theorem is the qualitative \(P=0\) endpoint of this statement.

**What remains unresolved independently of this:**
- (H\(_+\)) itself, i.e. whether an almost-Kähler metric on \(X\#k\overline{\mathbb{CP}}^2\) can have \((K_\omega^+)^2<A\);
- the all-metric monopole analogue of (ii). Step 40's Walsh \(h^-\) term is the natural candidate.