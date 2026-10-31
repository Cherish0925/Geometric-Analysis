# Step 3 corrections: LeBrun constants, mixed SW pinching, and positive collapse

Session: S0910A02. Agent3/Explore. Purpose: stop and repair Step 2 before running the assigned collapse catalogue, because the prior negative-Einstein arithmetic and collapse interpretation contained load-bearing errors.

## 1. What must be retracted from Step 2

The following Step 2 claims are **not reliable and must not be used**:

1. **False LeBrun Lemma 2 arithmetic.** Step 2 wrote, for an Einstein metric in dimension 4,
   \[
   8\pi^2(2\chi+3\tau)=4\int |W^+|^2+\frac{16}{3}\lambda^2\operatorname{Vol}.
   \]
   This has a factor-4 error. Since \(s=4\lambda\),
   \[
   \int \frac{s^2}{24}\,d\mu=\frac{16\lambda^2}{24}\operatorname{Vol}=\frac23\lambda^2\operatorname{Vol},
   \]
   and the Chern--Gauss--Bonnet/signature identity gives
   \[
   2\chi+3\tau=\frac{1}{4\pi^2}\int\left(2|W^+|^2+\frac{s^2}{24}-\frac{|\mathring r|^2}{2}\right)d\mu.
   \]
   Thus, for Einstein metrics,
   \[
   8\pi^2(2\chi+3\tau)=4\int |W^+|^2+\frac{4}{3}\lambda^2\operatorname{Vol},
   \]
   and
   \[
   \int |W^+|^2=2\pi^2(2\chi+3\tau)-\frac13\lambda^2\operatorname{Vol}.
   \]
   The Step 2 conclusion “no negative Einstein for all \(0<k<A\)” is false.

2. **The basic-class-square dispute was aimed at the wrong quantity.** For \(M=X\#k\overline{\mathbb{CP}}{}^2\), individual basic/monopole classes of the form \(c_1(X)+\sum \pm E_i\) have topological square \(A-k\), but LeBrun's curvature estimates use the self-dual projection \((a^+)^2\), and the sign trick/convex hull gives \((a^+)^2\ge A=c_1^2(X)\) for every metric. Therefore S0910A01's use of \(A\) in the curvature lower bound is correct.

3. **The apparent \(1/\sqrt A\) degeneration at \(k=\lceil 2A/3\rceil\) measures distance to the threshold, not large-\(A\) weakening.** The repaired bounds are homogeneous in \((A,k)\) and depend on \(p=k/A\). At fixed \(p\), they give a positive constant lower bound.

4. **The “no bad positive collapse = no collapse” slogan is false.** Round lens spaces \(S^3/\mathbb Z_m\) have constant sectional curvature 1 and hence \(\operatorname{Ric}=2g\) exactly while collapsing as \(m\to\infty\). Tight positive pinching permits collapse; the real question is whether such collapse forces Einstein-compatible quotient/orbifold-bundle topology, not whether it is absent.

## 2. Source-grade checks

### LeBrun 1996 (`Four-Manifolds without Einstein Metrics`)

Knowledge file: `Knowledge/objects/papers/Four-Manifolds-without-Einstein-Metrics--5b090e14de27--d63c56d541e8/object.md`.

Relevant lines read in Step 3:

- Lines 60--63: Witten/LeBrun scalar curvature estimate
  \[
  \int_M s^2\,d\mu\ge 32\pi^2(c_1^+)^2.
  \]
- Lines 67--99: for \(M=X\# k\overline{\mathbb{CP}}{}^2\), sign choices among the \(2^k\) blow-up classes give \((c_1(M,J_S)^+)^2\ge c_1^2(X)=A\), yielding
  \[
  \int_Ms^2\,d\mu>32\pi^2A.
  \]
- Lines 103--117: Theorem 3 states that if \(k\ge \frac23c_1^2(X)\), then \(M\) has no Einstein metric. This is the convention-independent checkpoint: the scalar-only argument gives the literature threshold \(k/A\ge2/3\), not the erroneous all-\(k<A\) threshold.

For an Einstein metric with \(C=2\chi+3\tau=A-k\), scalar estimate \(16\lambda^2V>32\pi^2A\) gives \(\lambda^2V>2\pi^2A\), and corrected CGB gives
\[
\int |W^+|^2 < 2\pi^2(A-k)-\frac{2}{3}\pi^2A
=2\pi^2\left(\frac23A-k\right).
\]
Thus nonnegativity contradicts only \(k\ge2A/3\) (strictness handles equality in LeBrun's statement), exactly as the source says.

### Ishida--LeBrun / LeBrun Proposition 4 mixed estimate

Knowledge file: `Knowledge/objects/papers/Curvature-Connected-Sums-and-Seiberg-Witten-Theory--7e92a6723434--2ac6d11897c5/object.md`.

Relevant lines read in Step 3:

- Lines 149--151: Proposition 4 states
  \[
  \int_M(s-\sqrt6|W^+|)^2d\mu\ge72\pi^2(a^+)^2.
  \]
- Lines 410--413: by Cauchy--Schwarz and triangle inequalities,
  \[
  \frac{1}{4\pi^2}\int\left(\frac{s^2}{24}+2|W^+|^2\right)d\mu\ge\frac23(a^+)^2.
  \]
- Lines 417--418 apply this with \((a^+)^2\) bounded below by a sum of \(c_1^2\)'s.

For a single blow-up family \(M=X\#k\overline{\mathbb{CP}}{}^2\), the same LeBrun sign trick gives \((a^+)^2\ge A\). Combining the mixed estimate with CGB for any metric gives
\[
\frac{1}{4\pi^2}\int\frac{|\mathring r|^2}{2}\,d\mu
\ge \frac23A-(A-k)=k-\frac13A.
\]
This is a metric-level lower bound on traceless Ricci energy whenever \(k>A/3\), not merely an Einstein contradiction.

## 3. Repaired pinching obstruction for \(\delta_-\)

Let \(g\) be normalized by \(\|\operatorname{Ric}_g+g\|_{op}\le\delta<1\). If the Ricci endomorphism eigenvalues are \(-1+e_i\), \(|e_i|\le\delta\), then
\[
|\mathring r|^2\le\sum_i e_i^2\le4\delta^2,
\qquad
\frac{s^2}{24}\ge\frac23(1-\delta)^2.
\]
Let \(C=A-k\). Dropping \(W^+\ge0\) in CGB gives the volume upper bound
\[
V\le \frac{4\pi^2C}{\frac23(1-\delta)^2-2\delta^2}
\]
as long as the denominator is positive. The mixed lower bound plus CGB gives
\[
4\pi^2\left(k-\frac13A\right)
\le \int\frac{|\mathring r|^2}{2}
\le 2\delta^2V.
\]
Combining these inequalities yields
\[
\left(k-\frac13A\right)\left[\frac23(1-\delta)^2-2\delta^2\right]
\le2\delta^2(A-k),
\]
which simplifies to
\[
\frac{\delta}{1-\delta}\ge\sqrt{\frac{k/A-1/3}{2}}
\qquad(k/A>1/3).
\]
Equivalently,
\[
\delta\ge \frac{\sqrt{(p-1/3)/2}}{1+\sqrt{(p-1/3)/2}},\quad p=k/A.
\]
At \(p=2/3\), this gives \(\delta\ge1/(1+\sqrt6)\approx0.289897949\). Hence fixed-ratio LeBrun families in the known no-Einstein range cannot have \(\delta_-\to0\). The only way this integral machinery allows \(\delta_-\to0\) is \(p=k/A\to1/3^+\), i.e. approaching the refined obstruction boundary.

This calculation was independently checked by running the peer script `Sessions/S0910A01/workspace/scripts/mixed_sw_bound_analysis.py` and by our script `Sessions/S0910A02/workspace/scripts/step3_corrected_lebrun_bounds.py`. The JSON result is saved at `Sessions/S0910A02/workspace/data/step3_corrected_lebrun_bounds.json`.

## 4. About the refined direct optimization requested by the Strategist

The rough test suggested maximizing
\[
16V+8\sqrt6\sqrt{W_2V}+6W_2
\]
with \(V\le6\pi^2(A-k)\) and \(W_2\le2\pi^2(A-k)-V/3\). At \(\delta=0\) this gives the exact maximum
\[
108\pi^2(A-k),
\]
so comparison with the lower bound \(72\pi^2A\) saturates at \(k/A=1/3\). This confirms the qualitative boundary in the exact-Einstein limit.

However, for \(\delta>0\), this direct objective is only a weaker necessary test if used with only separate bounds on \(s\), \(W^+\), and volume; it does not use the exact CGB relation
\[
\int\left(\frac{s^2}{24}+2|W^+|^2\right)=4\pi^2(A-k)+\int\frac{|\mathring r|^2}{2}
\]
and therefore misses the sharper \(O(\delta^2)\) traceless-Ricci obstruction above. The mixed estimate plus CGB subtraction is the stronger and cleaner theorem for pinching.

## 5. Repaired interpretation of positive collapse

Step 2's Berger computation remains useful as a warning about **fixed-bundle shrinking with fixed connection curvature**: for the Berger metrics on \(S^{2n+1}\), fixed Hopf base and fixed Chern data with fiber scale \(t\to0\) produce vertical Ricci eigenvalues tending to zero while horizontal eigenvalues remain positive, so \(\delta_+\to1\).

But this does **not** imply that tight positive pinching excludes collapse. Round space forms/lens spaces show the opposite:
\[
S^3/\mathbb Z_m\quad\text{with the quotient of the round metric has}\quad \operatorname{Ric}=2g
\]
for every \(m\), while the shortest Hopf-fiber loop has length \(2\pi/m\), so volume and injectivity radius collapse as \(m\to\infty\). More generally, a fixed-topology collapse catalogue will mostly rediscover anisotropy, whereas pinching-compatible collapse may require changing topological/orbifold data (e.g. Chern number or finite quotient order) with the collapse scale.

The corrected positive-branch question is therefore:

> If a sequence of closed \(n\)-manifolds admits \(\delta_+\to0\) metrics and collapses, does the collapse structure force each underlying smooth manifold already to carry an Einstein metric (for instance as a spherical/Einstein quotient or an Einstein-compatible orbifold-bundle resolution)?

This is a topology/structure question in the spirit of Anderson, Cheeger--Tian, Cheeger--Fukaya--Gromov, not a simple exclusion of collapse.

## 6. Research consequence for Yau Problem 26

The main progress of this correction is negative but valuable: the only known dimension-four all-sign no-Einstein examples produced by Seiberg--Witten/Chern--Weil mechanisms are much less plausible as refutations of \(P_4^-\) than Step 2 suggested. Any no-Einstein theorem derived from a curvature integral inequality that is valid for all metrics tends to be stable under small traceless-Ricci error; it excludes not only exact Einstein metrics but also sufficiently tightly Ricci-pinched inputs, with a pinching gap controlled by the strictness margin. Therefore a \(P_4^-\) counterexample would likely need either

1. to approach the precise boundary where the integral obstruction margin vanishes (for LeBrun, \(k/A\to1/3^+\)), while also excluding all Einstein signs, or
2. a genuinely non-perturbative Einstein obstruction that uses \(\mathring r\equiv0\) in a discontinuous way and does not yield a stable integral gap.

This is not a proof of Yau 26. It is a sharpening of the closure standard for refutation: construction of tight negative pinching on LeBrun manifolds at fixed obstruction margin is ruled out by the mixed SW bound; the surviving refutation slot is narrower and source-dependent.

## 7. Additional source check: LeBrun 2001 gives the exact \(A/3\) threshold

After writing the main correction, I read the later source `Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md`.

Important lines:

- Lines 74--76 of the object say explicitly that if a minimal complex surface \(X\) is blown up \(k\) times, the result \(M=X\#k\overline{\mathbb{CP}}{}^2\) does not admit Einstein metrics if \(k\ge\frac13c_1^2(X)\), improving earlier results.
- Lines 281--299 prove Proposition 3.1:
  \[
  \frac{1}{4\pi^2}\int\left(\frac{s^2}{24}+2|W_+|^2\right)d\mu\ge\frac23(c_1^+)^2.
  \]
- Lines 301--328 prove Proposition 3.2, including \((c_1^+)^2\ge(2\chi+3\tau)(X)\) after blow-ups and equality exclusion unless no blow-up/surgery occurs.
- Lines 330--349 give Theorem 3.3 and Corollary 3.4: for \(M=X\#k\overline{\mathbb{CP}}{}^2\#\ell(S^1\times S^3)\), no Einstein if \(k+4\ell\ge\frac13(2\chi+3\tau)(X)\); for minimal complex general type, no Einstein if \(k\ge A/3\).

This strengthens and source-grounds the Step 3 correction: the \(A/3\) range is not merely an extrapolated peer-script consequence; it is an explicit LeBrun 2001 theorem. The pinching lower bound derived here is a Yau26-specific stability version of the same mixed-integral obstruction for \(\delta_-\)-pinched input metrics. It still does not prove Yau26, because it covers a Seiberg--Witten four-dimensional no-Einstein family rather than arbitrary manifolds/all dimensions.

Caution: the peer script `mixed_sw_bound_analysis.py` contains a printed comment that an old scalar-only bound depends on \(A\). Interpreted correctly, homogeneous scalar-only bounds depend on \(p=k/A\) and the distance \(p-2/3\); the observed \(1/\sqrt A\) decay occurs only for the special integer-edge sequence \(k=\lceil2A/3\rceil\), where \(p-2/3=O(1/A)\). This does not affect the main mixed-bound conclusion.
