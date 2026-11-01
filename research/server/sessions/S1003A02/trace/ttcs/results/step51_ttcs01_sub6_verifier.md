# TTCS Independent Branch Record

```json
{
  "step_id": 51,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 3,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step50_minimizer_entry_PS_noncollapsed_alternative.md",
    "Knowledge/objects/papers/Blowing-up-and-desingularizing-constant-scalar-curvature--7e9bd4072728--db5d10d44a5c/object.md"
  ]
}
```

## Task

Verify Theorem K-infinity in the Step-50 note: for the blow-up (including infinitely-near points) of any minimal compact complex surface of general type, is inf over Kähler metrics of P exactly 8π²k and not attained? Check the lower formula and Hodge-index argument for nef non-ample K_X; the Arezzo-Pacard hypotheses on the canonical orbifold and subsequent smooth blow-ups; the Kähler class signs and epsilon expansion; whether negative cscK metrics are Yamabe representatives; and the statement D_W=0, DeltaV→0. Return a precise theorem, scope, and any needed repair.

## Output

# Verification memo: Theorem K∞ (Step 50, §5)

## Summary

The core statement holds. For a fixed complex surface \(M\) obtained by blowing up a minimal surface of general type \(X\) at \(k\ge1\) points, distinct or infinitely near,
\[
\inf\{P(g):g\ \text{Kähler on }(M,J)\}=8\pi^2k,
\]
and this infimum is not attained. The lower-bound formula, the Hodge-index argument for nef but non-ample \(K_X\), the Kähler-class signs, the \(\varepsilon\)-expansion, the Yamabe identification, and \(D_W=0\), \(\Delta V\to0\) all hold.

Three points in the written proof need repair:

1. **Infinitely-near points.** The classes \(E_i\) must be total transforms \(\mathcal E_i\), not exceptional curves.
2. **Placement of blow-up centres.** The "simultaneous Theorem 1.3" construction only reaches blow-up centres that are distinct and lie off the \((-2)\)-configuration. General centres need a two-stage, two-parameter construction.
3. **Which Kähler metrics.** The phrase "Kähler on \(M\)" must mean Kähler for the fixed complex structure \(J\). Extending it to all complex structures on the smooth manifold uses input that is not in the supplied sources.

There is also a free \(k=0\) companion statement.

## 1. Lower formula

Step 36 gives
\[
\widehat P=\frac{(K_M\cdot\Omega)^2}{\Omega^2}+\frac1{32\pi^2}\int(s-\bar s)^2-A+k.
\]
I rederived it from the package conventions.

- Combining \(8\pi^2\chi\) and \(12\pi^2\tau\) gives \(8\pi^2(2\chi+3\tau)=\int(4|W^+|^2-|\mathrm{Ric}^\circ|^2+s^2/12)\).
- For a Kähler metric \(|W^+|^2=s^2/24\), so \(P=\tfrac14\int s^2-8\pi^2c_1^2(M)\).
- The average scalar curvature satisfies \(\int s\,d\mu=4\pi c_1\cdot\Omega\) and \(\mathrm{Vol}=\Omega^2/2\). Hence \(\tfrac14\bar s^2\mathrm{Vol}=8\pi^2(K_M\cdot\Omega)^2/\Omega^2\).
- Finally \(c_1^2(M)=K_X^2-k=A-k\), for distinct and infinitely-near points alike.

**Repair for infinitely-near points.** Write \(K_M=\pi^*K_X+\sum_i\mathcal E_i\), where \(\mathcal E_i\) is the total transform of the \(i\)-th exceptional curve. These satisfy \(\mathcal E_i\cdot\mathcal E_j=-\delta_{ij}\) and \(\mathcal E_i\cdot\pi^*K_X=0\). Each \(\mathcal E_i\) is effective, being a strict transform plus later exceptional curves with positive coefficients. Hence \(\mathcal E_i\cdot\Omega>0\). The positivity argument in the note uses exactly this, so it should be stated with \(\mathcal E_i\).

**Hodge index with \(K_X\) nef but not ample.** On a Kähler surface the intersection form on \(H^{1,1}_{\mathbb R}\) has signature \((1,h^{1,1}-1)\). Since \(\Omega^2>0\), every real \((1,1)\)-class \(D\) satisfies \((D\cdot\Omega)^2\ge D^2\,\Omega^2\). No ampleness of \(D\) is needed, and not even \(D^2>0\).

Put \(a=\pi^*K_X\cdot\Omega\) and \(b=\sum_i\mathcal E_i\cdot\Omega\). Nefness of \(K_X\) gives \(a\ge0\), and effectivity gives \(b>0\). Then
\[
(a+b)^2>a^2\ge A\,\Omega^2,
\]
so \(\widehat P>k\) strictly for every Kähler metric. In particular \(\widehat P=k\) is never attained.

**Sharper exact identity.** Decompose \(\Omega=t\,\pi^*K_X+\beta\) with \(\beta\cdot\pi^*K_X=0\). Then \(t>0\) and \(\beta^2\le0\) by Hodge index, and \(K_M\cdot\beta=b\). This gives
\[
\widehat P-k=\frac{2tAb+b^2+A|\beta^2|}{t^2A+\beta^2}+\frac1{32\pi^2}\int(s-\bar s)^2 .
\]
All three numerator terms are nonnegative, and \(b>0\).

Consequence: a sequence of Kähler metrics with \(\widehat P\to k\) must satisfy three things at once:
- the normalized exceptional areas tend to zero, \(b/t\to0\);
- the normalized class converges to \([\pi^*K_X]\), i.e. \(|\beta^2|/t^2\to0\);
- the Calabi energy tends to zero.

This is the Kähler-category counterpart of Theorem 50.C(3): the class degenerates onto the canonical (orbifold) model, and each blow-up costs one unit. The identity is worth recording as part of the theorem.

## 2. Arezzo–Pacard hypotheses

**Canonical model.** The pluricanonical model \(\bar X\) has only isolated singularities with \(\Gamma_j\subset SU(2)\) (AP §1, items (i)–(ii)). It carries a Kähler–Einstein orbifold metric with negative scalar curvature (Kobayashi, AP item (iv)). Its automorphism group is discrete (AP item (iii), Cor 8.3 proof), so \(\bar X\) is nondegenerate in the AP sense.

**Crepant bubbles.** Kronheimer/Joyce crepant resolutions satisfy assumption (iv) of Theorem 1.3 when \(m=2\). Joyce's Theorem 7.1 gives \(\tilde\varphi=|u|^{-2}+O(|u|^\gamma)\), so (15) holds with log-coefficient \(0\).

**Burns bubbles.** The Burns metric has potential \(\tfrac12|u|^2+\log|u|^2\) (AP §7), which satisfies (15).

**Blow-up classes.** Theorem 1.1 gives \(\pi^*[\omega]-\varepsilon^2\sum a_jPD[E_j]\). This agrees with \([\eta_j]=-a_jPD[E_j]\), and \(\Omega\cdot E_j=\varepsilon^2a_j>0\).

**Nondegeneracy after blowing up.** Every blow-up of \(X\) is still of general type, so it has no nonzero holomorphic vector fields (AP §8 (vii)). This holds whether \(K_X\) is ample or only nef, so Theorem 1.1 can be iterated.

**Repair: placement of centres.** Theorem 1.3 inserts bubbles at points \(p_j\) of the orbifold \(\bar X\). A smooth point of \(\bar X\) corresponds to a point of \(X\) off the \((-2)\)-curves. Blow-ups centred on a \((-2)\)-curve, and blow-ups at infinitely-near points, are not reached by a single application. AP's own Cor 8.3 proof uses the sequence that covers every case:

1. Apply Theorem 1.3 on \(\bar X\) with crepant bubbles. This gives cscK on \(X\) in class \(\lambda K_X+\varepsilon^2c\), where \(K_X\cdot c=0\) and \(c^2<0\). The inequality is strict because a Kähler class of a Kronheimer metric is nonzero on every \((-2)\)-curve.
2. Apply Theorem 1.1 at arbitrary points of \(X\) with parameter \(\delta<\delta_0(\varepsilon)\).
3. Iterate Theorem 1.1 for infinitely-near points.

Here \(\lambda\) is any positive constant; with \(\mathrm{Ric}=-\omega\) one has \(\lambda=2\pi\).

## 3. Expansion, checked exactly

For cscK metrics the Calabi term vanishes, so \(\widehat P\) depends only on the class. Write \(S=\sum a_j\), \(\Sigma_2=\sum a_j^2\), and \(C=c^2<0\).

- Classes: \(K_M\cdot\Omega=\lambda A+\delta^2S\) and \(\Omega^2=\lambda^2A+\varepsilon^4C-\delta^4\Sigma_2\).
- Cross terms vanish: \(\pi^*K\cdot c=\pi^*K\cdot E=c\cdot E=0\), and \(K_M\cdot E=-1\).

The exact value is
\[
\widehat P-k=\frac{2\lambda A\delta^2S+\delta^4(S^2+A\Sigma_2)+A\varepsilon^4|C|}{\lambda^2A+\varepsilon^4C-\delta^4\Sigma_2}>0 .
\]
This tends to \(0\) as \(\varepsilon\to0\) and then \(\delta\to0\); a diagonal choice of parameters suffices. When \(\delta=\varepsilon\) it reproduces the note's \(k+2\varepsilon^2S/\lambda+O(\varepsilon^4)\).

For infinitely-near points, each further blow-up with parameter \(\delta_i\) changes \(K\cdot\Omega\) by \(+\delta_i^2a_i\), \(\Omega^2\) by \(-\delta_i^4a_i^2\), and \(c_1^2\) by \(-1\). Taking iterated limits gives \(k\).

## 4. Yamabe representatives, \(D_W\) and \(\Delta V\)

**Sign of the scalar curvature.** For cscK, \(s\equiv\bar s=-8\pi\,K_M\cdot\Omega/\Omega^2\). This is strictly negative by §1, so every cscK metric on \(M\) has negative scalar curvature. AP's sign-preservation statement is not even needed.

**Yamabe identification.** In a conformal class with negative Yamabe constant, the constant-scalar-curvature metric is unique up to homothety (maximum principle). So the cscK metric, rescaled to \(s=-4\), is the Yamabe representative \(\hat g\).

**\(D_W=0\).** In that scaling \(|W^+|^2=s^2/24=2/3\) pointwise, so \(D_W=0\) exactly.

**\(\Delta V\).** Scale invariance of \(s^2\mathrm{Vol}\) gives \(\mathrm{Vol}(\hat g)=2\pi^2(K_M\cdot\Omega)^2/\Omega^2\). Hence
\[
\Delta V:=\mathrm{Vol}(\hat g)-2\pi^2A=2\pi^2(\widehat P-k)>0,\qquad \Delta V\to0 .
\]
This is consistent with (Y0): \(8\pi^2k-P=4(D_W-\Delta V)\). I rederived (Y0) as an identity for \(P(\hat g)\), with \(\Delta V\) defined as above.

**Applicability.** The identity \(\widehat P-k=\Delta V/2\pi^2\) applies only to cscK members. For a non-cscK Kähler metric, \(\hat g\) is not Kähler and \(P(\hat g)\ne P(g)\).

**Bubbles.** Burns bubbles are scalar-flat Kähler, hence anti-self-dual (\(W^+\equiv0\)), with \(\widehat P=\mathfrak c=1\). Crepant bubbles are hyperkähler and contribute \(0\). This matches the bubbling picture in the note.

## 5. Precise theorem

**Theorem K∞.** Let \(X\) be a minimal compact complex surface of general type, with \(K_X\) nef, and \(A=K_X^2\). Let \(M\) be obtained from \(X\) by \(k\) blow-ups, distinct or infinitely near.

(a) Every Kähler metric \(g\) on \((M,J)\) satisfies the exact identity of §1, so \(P(g)>8\pi^2k\).

(b) There are cscK metrics \(g_{\varepsilon,\delta}\), with negative scalar curvature, which are Yamabe representatives with \(D_W=0\), satisfying \(P(g_{\varepsilon,\delta})\to8\pi^2k\). Hence \(\inf_{\text{Kähler}}P=8\pi^2k\), and for \(k\ge1\) it is not attained.

(c) If \(k=0\), the infimum is \(0\). It is attained exactly when \(K_X\) is ample (KE metric). If \(K_X\) is nef but not ample, Hodge-index equality would force \(\Omega\propto K_X\), which is not a Kähler class. The crepant family gives \(\widehat P=A\varepsilon^4|C|/(\lambda^2A+\varepsilon^4C)\to0\).

## 6. What remains unresolved

These points concern the meaning of "Kähler on \(M\)" if it is read as Kähler for any complex structure on the smooth manifold.

- **Same orientation.** One would need the Kodaira dimension and \(K_{\min}^2\), and hence \(k\), to be oriented-diffeomorphism invariants. These are Seiberg–Witten results (Friedman–Morgan; Witten when \(b^+>1\)). They are not among the supplied sources and would have to be cited.
- **Opposite orientation.** If \(b^-(M)\ge2\), then \(\bar M\) has \(b^+\ge2\) and contains an embedded sphere of square \(+1\) in a nontrivial class. A Kähler surface with \(b^+\ge2\) has nonzero SW invariants, which excludes such a sphere, so \(\bar M\) carries no Kähler structure. Only the case \(b_2(X)=1\) (fake projective planes) with \(k=1\) is left open by this argument.