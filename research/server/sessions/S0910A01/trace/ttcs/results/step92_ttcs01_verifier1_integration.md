# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 92,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step92_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step92_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 92 route comparison and AB adjacent heat sign argument. Read the Step 92 note plus the Step 91 product note, Step 47 entropy/degree note, and Step 92 support data. Check especially: (1) whether the hyperbolic X#X continuity and corrected Lohkamp-ratio statement are mathematically accurate; (2) whether the AB-sector reduction after adjacent m=2 polarization cancellation to K_adj^AB=(1/512)∫ e^s A(s)B(s) ds is consistent with Step 91 normalization; (3) whether the claimed sign proof B(s)<0 via monotonicity of the scalar heat kernel at antipodal points on S^2 is actually valid for all s>0, or whether it needs an additional theorem/proof/correction; and (4) what remains before the result affects the full Ozuch coefficient or Yau-26. Give a direct scientific memo with any errors and repairs.

## Integrated Scientific Memo

# Step 92 verification memo

## 1. Hyperbolic \(X\#X\): correct, with two wording qualifications

Assume
\[
-3(1+\varepsilon)g\le \operatorname{Ric}_g\le -3(1-\varepsilon)g,
\qquad 0\le \varepsilon\le \frac13.
\]
Writing the Ricci eigenvalues as \(-3x_i\), \(x_i\in[1-\varepsilon,1+\varepsilon]\), the four-dimensional Chern–Gauss–Bonnet Ricci term is
\[
Q:=\frac{s^2}{24}-\frac{|E|^2}{2}
=\frac{s^2}{6}-\frac{|\operatorname{Ric}|^2}{2}.
\]
Its minimum on this box is attained at the all-low vertex for \(\varepsilon\le1/3\), giving
\[
Q\ge 6(1-\varepsilon)^2.
\]
Thus, for \(M=X\#X\),
\[
\operatorname{Vol}(M,g)
\le
\frac{4\pi^2}{3}\frac{\chi(M)}{(1-\varepsilon)^2}
=
\frac{2\operatorname{Vol}(X)(1-1/\chi(X))}
{(1-\varepsilon)^2}.
\]

After scaling \(q=(1+\varepsilon)g\), one has \(\operatorname{Ric}_q\ge-3q\). The degree-two map \(X\#X\to X\) and BCG imply
\[
\operatorname{Vol}(M,g)\ge
\frac{2\operatorname{Vol}(X)}{(1+\varepsilon)^2}.
\]
Hence no such metric exists when
\[
\varepsilon<
\frac{1-\sqrt{1-1/\chi(X)}}{1+\sqrt{1-1/\chi(X)}}
=
\frac1{4\chi(X)}+O(\chi(X)^{-2}).
\]
At equality, BCG rigidity would force a degree-two Riemannian covering, impossible because
\[
\chi(X\#X)=2\chi(X)-2\ne2\chi(X).
\]

This is the same fixed-target obstruction as Step 47 in a sharper normalization. Two corrections to phrasing:

* The lower bound is furnished by **BCG**, not Bishop comparison.
* The displayed box estimate explicitly uses \(\varepsilon\le1/3\).

The all-sign no-Einstein conclusion for \(X\#X\) is correct: Myers excludes positive Einstein metrics, compact Ricci-flat fundamental-group structure excludes zero Einstein metrics, and BCG plus CGB excludes negative Einstein metrics.

### Lohkamp ratio

The scaling observation is correct if \(a,b\) are the sharp global extremal magnitudes. For
\[
-bg\le\operatorname{Ric}_g\le-ag,\qquad 0<a<b,
\]
and a prescribed \(c<C<0\), write \(c=-\beta\), \(C=-\alpha\), with \(\beta>\alpha>0\). A scale \(g'=tg\) fits the prescribed interval exactly when
\[
\frac b\beta\le t\le\frac a\alpha,
\]
which is possible iff
\[
\frac ba\le\frac{|c|}{|C|}.
\]
If \(a,b\) are merely nonsharp enclosing constants, this ratio condition is sufficient but not necessary. Thus Lohkamp’s \(\operatorname{Ric}<0\) result alone does not provide arbitrarily tight two-sided negative pinching.

The unresolved geometric object remains a sequence \(X_i\#X_i\) with maximum normalized Ricci defect tending to zero—or a theorem preventing such a sequence. Global volume growth does not suppress pointwise neck error.

---

## 2. AB reduction and the factor \(1/512\): internally consistent

With
\[
p_{\ell k}=\frac{\mu_\ell+\mu_k}{2}-1,\qquad
\mu_j=j(j+1),
\]
the residual adjacent series is
\[
K_\tau^{AB}
=\frac1{512}\sum_{\ell,k\ge1}(-1)^k
\frac{(2\ell+1)(2k+1)\mu_\ell\mu_k}{p_{\ell k}}
e^{-\tau p_{\ell k}}.
\]
This normalization agrees with Step 91’s
\[
S_{\rm odd}=\frac{\pi^2}{2}R_{\rm odd}
\]
and its quotient norm. In particular, the \((\ell,k)=(1,1)\) term at \(\tau=0\) equals
\[
-\frac{3\cdot3\cdot2\cdot2}{512}=-\frac9{128},
\]
exactly matching the Step 91 axial limit.

For \(\tau>0\), absolute convergence permits
\[
\frac{e^{-\tau p}}p=\int_\tau^\infty e^{-sp}\,ds,
\]
and therefore
\[
K_\tau^{AB}
=\frac1{512}\int_\tau^\infty e^sA(s)B(s)\,ds,
\]
where
\[
A(s)=\sum_{\ell\ge1}(2\ell+1)\mu_\ell e^{-s\mu_\ell/2},
\qquad
B(s)=\sum_{k\ge1}(-1)^k(2k+1)\mu_k e^{-s\mu_k/2}.
\]

The supplied spectral data support exact cancellation of the four \(m=2\) polarization channels with relative signs
\[
+1,-1,+1,-1.
\]
However, the source bundle contains numerical/table evidence rather than the promised written Hessian/star-matrix derivation. Because the individual channels diverge as \(\tau\downarrow0\), exact cancellation must be proved mode-by-mode before passing to the limit; it cannot safely be inferred from floating-point cancellation.

A wording repair is also advisable: “only the \(m=0\) series remains” describes the residual polarization class, but the factors \(2\ell+1\) and \(2k+1\) arise from shell/addition-theorem collapse, not from a literal single-\(m\) degeneracy.

---

## 3. \(B(s)<0\): conclusion correct, Step 92’s stated proof is incomplete

The heat-kernel identity is correct:
\[
p_t(\pi)=\frac1{4\pi}\sum_{\ell\ge0}(2\ell+1)(-1)^\ell e^{-t\mu_\ell},
\]
hence
\[
B(s)=-4\pi\,\partial_t p_t(\pi)\big|_{t=s/2}.
\]

The Step 92 prose does not by itself prove strict pointwise negativity for every \(s>0\). Radial monotonicity and the minimum principle yield nondecrease of the antipodal value; even strict increase as a function of time does not automatically imply a strictly positive derivative at every time. Thus an additional theorem or argument is required.

A direct repair uses the dimension-raising identity. With \(x=\cos r\),
\[
p_t^{(2)}(x)=\frac1{4\pi}\sum_{\ell\ge0}
(2\ell+1)P_\ell(x)e^{-\ell(\ell+1)t},
\]
and differentiation of the Gegenbauer expansion gives
\[
\partial_xp_t^{(2)}(x)=2\pi e^{-2t}p_t^{(4)}(x).
\]
For a zonal function on \(S^2\),
\[
\Delta=(1-x^2)\partial_x^2-2x\partial_x.
\]
At \(x=-1\),
\[
\partial_t p_t^{(2)}(-1)
=\Delta p_t^{(2)}(-1)
=2\partial_xp_t^{(2)}(-1)
=4\pi e^{-2t}p_t^{(4)}(-1)>0,
\]
because the heat kernel on connected \(S^4\) is strictly positive for \(t>0\). Consequently
\[
\boxed{B(s)=-16\pi^2e^{-s}p_{s/2}^{(4)}(-1)<0.}
\]
Therefore
\[
\boxed{
K_\tau^{AB}
=-\frac{\pi^2}{32}
\int_\tau^\infty A(s)p_{s/2}^{(4)}(-1)\,ds<0.
}
\]
This also makes convergence transparent: near \(s=0\), \(A(s)=O(s^{-2})\) while the antipodal heat kernel is off-diagonally exponentially small; as \(s\to\infty\),
\[
A(s)=6e^{-s}+O(e^{-3s}),
\]
while \(p_{s/2}^{(4)}(-1)\) tends to a finite positive constant.

Thus the strict sign is rigorous after adding this identity. The numerical value
\[
K_{\rm adj}^{AB}\approx-0.03144249732
\]
is strongly corroborated by the heat ladder, though rigorous certification of those decimal digits would require explicit interval tail bounds. The small-\(s\) alternating samples in the JSON are ill-conditioned and correctly provide no sign evidence.

---

## 4. What is actually established, and what remains

The verified result is only:

> In the Step 91 principal source/receiver convention, after exact \(m=2\) polarization cancellation, the off-diagonal adjacent AB transfer is finite and strictly negative.

It is not yet the full Ozuch coefficient. The missing coefficient-level ingredients are:

1. A written exact proof of the \(m=2\) cancellation.
2. Derivation of the source from the actual Eguchi–Hanson \(H^4\) asymptotic tensor.
3. Quotient-isotropy and symmetric-product normalization.
4. Bianchi correction and gauge projection for the actual source.
5. AA and BB trace-free tensor sectors, including the omitted magnetic modes.
6. Proof of transported-frame signs and equality of all ordered adjacent coefficients.
7. Differentiated heat-kernel bounds and justified limiting/interchange operations for every source component.
8. Matching with the \(t_i\lambda_i+t_i^2\mu_i\) expansion at order \(t_it_j^2\), with remainder below that interaction order.
9. Calibration against self-interactions and the all-same-chirality branch.

The true ALE source multiplier could change the convention-dependent sign, and AA/BB or gauge terms could reinforce or cancel the AB contribution.

Even a nonzero complete adjacent coefficient would obstruct only the selected mixed-chirality desingularization chart. It would not prove that the resulting smooth manifold admits no Einstein metric elsewhere in its metric space. To affect Yau–26 one would additionally need:

* identification of the resulting smooth manifold;
* a family of smooth metrics on it with operator-norm Ricci pinching tending to a scalar;
* exclusion of every Einstein metric on that same smooth manifold, for all signs of \(\lambda\).

Accordingly, Step 92 supplies a genuine analytic sector theorem and a useful local gluing invariant, but neither a complete Ozuch obstruction nor a Yau–26 conclusion.