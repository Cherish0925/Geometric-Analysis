# Step 42 — Almost-Kähler torsion profile, the Taubes period lemma, and the Goldberg reduction of the tariff

Session S1003A02, Agent2. Setting: \(M=X\#k\overline{\mathbb{CP}}^2\), \(X\) minimal with \(b^+(X)\ge2\),
Seiberg–Witten basic classes exactly \(\pm K_X\) modulo torsion (an assumption to be checked for each \(X\); it is not automatic for every minimal surface of general type), \(A=K_X^2>0\),
\(E_i\) the exceptional classes, \(0<k<A/3\) the open range. Closed identity
\(C_+:=\frac1{2\pi^2}\int|W^+|^2+\frac1{96\pi^2}\int s^2=A-k+P/(8\pi^2)\).
Script/data: `workspace/scripts/step42_ak_torsion_profile.py` → `workspace/data/step42_ak_torsion_profile.json`
(all algebra below verified symbolically).

Conventions for an almost-Kähler metric \((g,\omega)\), \(|\omega|^2=2\), \(u=\omega/\sqrt2\) (LeBrun,
*Four-manifolds, curvature bounds and convex geometry*, and *Ricci curvature, minimal volumes and SW theory*,
Prop. 2.4 and Blair's formula there):
\[
s^*=s+|\nabla\omega|^2=2W^+(\omega,\omega)+\tfrac s3,\qquad
\int(s+s^*)\,d\mu=8\pi\,c_1(\omega)\cdot[\omega]=-8\pi K_\omega\cdot[\omega],\qquad [\omega]^2=2V .
\]
Hence \(W^+(u,u)=s/6+\delta/4\) with \(\delta:=s^*-s=|\nabla\omega|^2\ge0\), and \(\delta\equiv0\) iff Kähler.

## 1. Taubes period lemma

**Lemma T.** Let \(\omega\) be a symplectic form on \(M\) (for instance a nowhere-vanishing self-dual
harmonic form of any metric). Then \(K_\omega=sK_X+\sum_i\epsilon_iE_i\) for signs \(s,\epsilon_i\), the classes
\(e_i:=\epsilon_iE_i\) and \(sK_X\) are represented by \(J\)-holomorphic curves for generic compatible \(J\), and
\[
K_\omega\cdot[\omega]=|K_X\cdot[\omega]|+\sum_i a_i,\qquad a_i:=|E_i\cdot[\omega]|>0 .
\]
*Proof.* \(b^+(M)\ge2\). Taubes: \(K_\omega\) is a basic class; by the blow-up formula the basic classes of
\(M\) are \(\pm K_X+\sum\pm E_i\). Taubes' SW\(\Rightarrow\)Gr: a class \(e\) with \(SW(2e-K_\omega)\neq0\) is
represented by a \(J\)-holomorphic curve, hence \(\omega\cdot e>0\) if \(e\ne0\). For \(e=e_i\),
\(2e_i-K_\omega=-(K_\omega-2e_i)\) and \(K_\omega-2e_i\) is the basic class with the \(i\)-th sign flipped;
for \(e=sK_X\), \(2sK_X-K_\omega=sK_X-\sum e_i\) is basic. So \(\omega\cdot e_i>0\), \(\omega\cdot sK_X>0\), and
\(K_\omega\cdot\omega=s K_X\cdot\omega+\sum\omega\cdot e_i\). \(\square\)

**Corollary T1 (null periods force zeros).** For any metric \(g\) on \(M\), a self-dual harmonic form with zero
period on some \(E_i\) vanishes somewhere. In particular, if some \(E_i\) is anti-self-dual harmonic for \(g\),
then \(g\) admits no nowhere-vanishing self-dual harmonic form (no conformally almost-Kähler structure).

**Corollary T2 (the Step-40 formal common mode is topologically excluded).** The Step-40 state
(constant \(\rho=r\), \(\zeta=0\), \(d\psi_\epsilon=0\), \(\psi_\epsilon\) independent of \(\epsilon\)) requires every
\(E_i\) to be ASD harmonic and \(\psi=r n\) to be a nowhere-vanishing harmonic self-dual form. This contradicts
T1. More precisely, if one monopole form \(\psi_\epsilon\) is closed and nowhere zero, then
\(\omega\propto\psi_\epsilon\) is symplectic, every \(E_i^{+,h}\ne0\), and the harmonic parts of the
\(\psi_{\epsilon}\) are genuinely sign-dependent.

*Consistency with the cell.* In the symmetric perpendicular cell the canonical closed self-dual form has zero
period on \(E\) and **vanishes along the exceptional sphere**: in A01's \(x_0=.038,X=128\) profile
(`Sessions/S1003A01/workspace/data/step28/gap_lm3_x00.038_X128_d24.json`) the conformal factor \(u\) with
\(|\omega|_g=\sqrt2u^2\) is \(0.0072\) at the first bolt sample and \(1\) at the CH end. In this symmetric model the
null-period mechanism is a degenerate (bolt-vanishing) closed form, not an almost-Kähler structure (in general a
zero integral over a sphere does not force pointwise vanishing on it); in a closed host it becomes a zero set of
the harmonic form or acquires a positive exceptional period.
Literature status (Step-42 verification): Lemma T packages a standard argument — LeBrun's 2001 Proposition 3.2
already uses the sign-flipped basic class and Taubes to contradict zero exceptional symplectic area. New here is
only its use against the Step-40 common mode.

*What T does not give.* No quantitative cost: the replacement for the common mode may use (a) tiny but
positive exceptional areas \(a_i\) (small \(J\)-holomorphic spheres, Walsh self-dual variance
\(\sim\sum a_i^2/V\)), or (b) thin near-symplectic zero sets of the harmonic part with \(\psi_\epsilon\)
non-closed, whose \(\zeta\)/\(d\psi\) cost tends to zero with the tube radius unless the geometry is bounded
at unit scale (and even then it is \(O(1)\) per zero component, not per class). Lemma T therefore turns
"exceptional classes are ASD" into "exceptional classes are small pseudoholomorphic spheres or are
linked to zeros of the harmonic form"; neither alternative carries a per-class tariff by itself.

## 2. Theorem AKΓ (almost-Kähler torsion-profile inequality)

**Theorem AKΓ.** For every almost-Kähler metric \((g,\omega)\) on \(M\), put
\[
\ell:=8\pi K_\omega\cdot[\omega]=8\pi\Bigl(|K_X\cdot\omega|+\sum_ia_i\Bigr),\qquad
\theta:=\frac1\ell\int(s^*-s)\,d\mu\ \ (\ge0).
\]
Then
\[
C_+\ \ge\ \frac{\ell^2}{128\pi^2V}\,\Gamma(\theta),\qquad \Gamma(\theta)=3\theta^2-2\theta+1,
\qquad \frac{\ell^2}{128\pi^2V}= A\,(\eta+\alpha)^2,\quad \eta=\frac{|K_X\cdot\omega|}{\sqrt{2AV}},\ \alpha=\frac{\sum a_i}{\sqrt{2AV}}>0 .
\]
Equivalently
\[
\frac{P}{8\pi^2}\ \ge\ k-A+A(\eta+\alpha)^2\Gamma(\theta).
\]
**Correction (Step-42 verification, `trace/ttcs/results/step42_ttcs01_verifier1_integration.md`).** The
first draft claimed \(\eta\ge1\) by reverse Cauchy–Schwarz. That is false when \(b^+\ge2\): two positive-square
classes need not span a Lorentzian plane. Counter-mechanism: on a Kähler \(X\) with \(p_g>0\),
\(\omega_t=\omega_0+t\operatorname{Re}\Omega\) is symplectic with \(K_{\omega_t}=K_X\), \(K_X\cdot\operatorname{Re}\Omega=0\), so \(\eta\to0\).
\(\eta\ge1\) holds under the Lorentzian hypothesis (H\(_L\)) \(|K_X\cdot\omega|\ge\sqrt{K_X^2[\omega]^2}\) (e.g. classes in one
\((1,1)\) Hodge-index plane, the Kähler case). Without (H\(_L\)) the almost-Kähler bound loses the period angle;
for arbitrary metrics LeBrun's monopole projection \((c_1^+)^2\ge c_1^2\) still gives \(2A/3\). Under (H\(_L\)):
\(P/(8\pi^2)\ge k-A(2\theta-3\theta^2)+A[(1+\alpha)^2-1]\Gamma(\theta)\).
*Proof.* With \(\sigma=-s\), \(|W^+|^2\ge\frac32W^+(u,u)^2\) (trace-free) gives the pointwise bound
\(C_+\)-density \(\ge G(\sigma,\delta)=[2\sigma^2+(3\delta-2\sigma)^2]/(192\pi^2)\), a positive-definite
quadratic form. Blair's formula fixes \(\int(2\sigma-\delta)=\ell\) exactly, so the means are
\(\bar\sigma=(1+\theta)\ell/2V\), \(\bar\delta=\theta\ell/V\); Jensen gives \(C_+\ge VG(\bar\sigma,\bar\delta)=
\ell^2\Gamma(\theta)/(128\pi^2V)\). Lemma T and the reverse Cauchy–Schwarz inequality
\(|K_X\cdot\omega|\ge\sqrt{K_X^2[\omega]^2}=\sqrt{2AV}\) for two positive-square classes give the prefactor. \(\square\)

Equality in the \(\ell\)-form holds iff \(W^+=\mathrm{diag}(\lambda,-\lambda/2,-\lambda/2)\) along \(\omega\) and
\(s,s^*\) are separately constant; then \(\lambda=\ell(2\theta-1)/(12V)\), so \(\omega\) is the lowest eigenvector only
for \(\theta<1/2\). This overlaps with, but is not identical to, LeBrun's saturating class of Prop. 2.4 (which
has \(s+s^*\) constant and \(\omega\) in the lowest eigenspace). Exact defect:
\(\mathfrak d_{AK}=\frac1{2\pi^2}\int(|W^+|^2-\frac32W^+(u,u)^2)+\int G(\sigma-\bar\sigma,\delta-\bar\delta)\ge0\).

**Readings.**
1. \(\theta=0\) (Kähler, where Hodge index gives (H\(_L\))): \(C_+\ge A(1+\alpha)^2\), i.e.
   \(P/(8\pi^2)\ge k+A[(1+\alpha)^2-1]\). This is the Step-38 Kähler tariff, strengthened by the exceptional areas.
2. \(\min_\theta\Gamma=2/3\) at \(\theta=1/3\) (\(\bar\delta=\bar\sigma/2\), i.e. \(s^*=s/2\), the extremal of
   LeBrun's Cauchy–Schwarz constant \(48\)): LeBrun's \(C_+\ge2A/3\). The almost-Kähler category alone therefore
   also stops at \(2/3\), at a definite torsion fraction rather than at a Kähler point; this is the
   almost-Kähler face of Theorem E (whose binding amplitude \(\rho=3/2\) corresponds to \(h=1/2\),
   \(\theta=h/(2-h)=1/3\)).
3. The Step-40 formal common mode is exactly the \(\alpha=0\) equality case: with \(r=2-h\) one finds
   \(\delta=4h\), \(\bar\sigma=4\), \(\theta=h/(2-h)\), and \(\beta(r)=2\theta-3\theta^2\) identically. Lemma T shows
   \(\alpha>0\) strictly, so the equality case is never attained on \(M\); but \(\alpha\) can be arbitrarily
   small, so the strictness is not quantitative.
4. **Linear torsion law (under (H\(_L\))).** \(1-\Gamma(\theta)=2\theta-3\theta^2\le2\theta\): in the almost-Kähler category the
   saving \(k-P/(8\pi^2)\) is at most \(2A\theta\), i.e. at most \(\frac{2A}{\ell}\int|\nabla\omega|^2\), linear in
   torsion. This is the almost-Kähler counterpart of Theorem N (whose free channel is the Nijenhuis energy).

## 3. The tariff is a quantitative Goldberg statement (reduction theorem)

**Proposition G (almost-Kähler form; conditional on (H\(_L\)), or on the inequality \(p\ge k-2A\theta\)).** Suppose a class \(\mathcal C\) of almost-Kähler metrics on \(M\) satisfying (H\(_L\))
satisfies the linear torsion estimate \(P\ge8\pi^2\kappa A\,\theta\) (scale-invariant; \(\theta\) as above). Then
every \(g\in\mathcal C\) satisfies
\[
\frac{P}{8\pi^2}\ \ge\ \frac{\kappa}{\kappa+2}\,k .
\]
*Proof.* \(p=P/8\pi^2\ge k-2A\theta\ge k-2p/\kappa\). \(\square\)

**Proposition G′ (all metrics, monopole form).** Under the all-metric field hypotheses of §3.6 of the
package (b⁺≥2 simple type, \(A-k>0\), scalar \(-4\) representative), Theorem N gives
\(8\pi^2k-P\le\mathcal N:=\frac12\mathbb E\int\rho^2|\nabla n|^2_{W_2}\). If \(P\ge\kappa\mathcal N\) on a class of
metrics, then \(P\ge8\pi^2k\,\kappa/(1+\kappa)\) there. Conversely, any sequence with \(P/(8\pi^2k)\to c\) has
\(\mathcal N/P\ge (1-c)/c\) asymptotically (since \(\mathcal N\ge8\pi^2k-P\)); a \(c\to0\) sequence is necessarily (not
conversely) a sequence along which the monopole Goldberg ratio \(\mathcal N/P\) is unbounded. The certified cell (if it had a
closed-host replica with the same normalized saving) would require \(\mathcal N/P\ge0.0043373/0.99566\approx0.004356\),
compatible with any \(\kappa\le229\); the certified upper coefficient bounds the best possible Goldberg constant
on the relevant class by \(\kappa\le c/(1-c)\approx229.6\) only if that replica exists.

So the per-blow-up tariff in the open range is implied by, and its failure \(c\to0\) implies the failure of, a
**linear** negative-scalar Goldberg estimate for the monopole almost-complex structures. Goldberg itself
(\(P=0\Rightarrow\nabla J=0\)) is open for \(s<0\) in general; Sekigawa's integral formula has the wrong sign there.
Within the saturating class of Theorem AKΓ (W⁺ Kähler-type along ω, \(s,s^*\) constant) the \(P=0\) endpoint
is Armstrong's theorem (no compact Einstein strictly almost-Kähler 4-manifold with ω an eigenvector of
\(W^+\)), cited by LeBrun as Corollary 2.5. The natural first coercive target is therefore a **quantitative
Armstrong theorem**: on the saturating (or near-saturating) class, \(P\ge\kappa\,A\theta\) with \(\kappa\)
independent of the cover. This is strictly weaker than quantitative Goldberg and is exactly what is needed
to exclude approximate common modes, because by AKΓ any almost-Kähler metric with saving comparable to
\(2A\theta\) must be close to the saturating class (the deficits in \(|W^+|^2\ge\frac32W^+(u,u)^2\) and in Jensen
are subtracted from the saving).

## 4. Superseded formulation

The Step-39/41 dichotomy "diffuse depletion pays unless \(W^+\) co-rotates with \(n\)" is superseded: in
almost-Kähler geometry \(W^+(n,n)\) rises with torsion automatically (\(W^+(u,u)=s/6+\delta/4\)), co-rotation is
free, the misalignment remainder is quadratic in torsion while the saving is linear (AKΓ, Theorem N). The
Cotton/Derdziński slack identified in Step 41 is still the correct name of the *stationary* endpoint
(δW⁺=0), but the coercive question is the linear Goldberg/Armstrong estimate above.

## 5. Open

- Correctly posed coercive target (from the Step-42 verification): **near-saturated quantitative Armstrong**,
  \(P/(8\pi^2)+C\,\mathfrak d_{AK}\ge c\,A\theta\) on a class with period control, with a companion control of the period
  loss \(A[1-(\eta+\alpha)^2]_+\); weaker nonperturbative variant on \(W^+(\omega)^\perp=0\):
  \(\int|\mathrm{Ric}^\circ|^2\ge c\int|\nabla\omega|^4\) (quartic, retains Armstrong's endpoint). Perturbative fixed-host version
  \(\int|\mathrm{Ric}^\circ|^2\ge c(g_0)\int|\nabla\omega|^2\) modulo gauge/KE moduli is elliptic; cover uniformity is the real
  content.
- Quantitative Armstrong on the saturating class: write AAD's differential Bianchi identities for
  \(W^+=\mathrm{diag}(\lambda,-\lambda/2,-\lambda/2)\) with constant \(s,s^*\) and determine whether \(\int|\mathrm{Ric}^\circ|^2\)
  controls \(\int|\nabla\omega|^2\) linearly; test on cohomogeneity-one almost-Kähler families.
- Monopole version: replace "almost-Kähler" by the monopole structure with \(\rho\) near constant; Lemma T
  says the harmonic part must vanish or carry positive exceptional periods; quantify either alternative.
- Gromov monotonicity gives \(a_i\ge c\,r_0^2\) when the almost-Kähler geometry is bounded at scale \(r_0\)
  around the sphere; with \(\alpha\ge kc r_0^2/\sqrt{2AV}\) this adds \(\approx2A\alpha\) to the right side of
  AKΓ, a per-class tariff proportional to \(r_0^2/\sqrt{AV}\) — real but scale-degenerate.
