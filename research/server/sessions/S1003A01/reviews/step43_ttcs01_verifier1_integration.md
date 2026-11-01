# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 43,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step43_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step43_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Check the mathematics of the new note Sessions/S1003A01/workspace/notes/step43_period_linear_lebrun_ledger_and_ricci_flow.md, against A02's Step-48 note (LeB_full, Theorem Y, Y0) and the script that produced the numbers. Specifically: (1) Is Proposition 43.1 correct — that maximizing LeBrun's Proposition-4 bound over the sign family a_eps=K+sum eps_i E_i gives Pi_g >= (K.c + sum|E_i.c|)^2/c^2 - A for every c in H^+_g, hence a LINEAR period term 2 sum|e_i|, e_i=E_i.K^+, improving A02's quadratic |K^-|^2+sum|E_i^+|^2; and the exact formulas K.c=A, E_i.c=sigma_i, c^2=A-|sigma|^2, e_i=sigma_i+(G sigma)_i when c=K-sum sigma_i E_i is SD-harmonic? Are the sign conventions (K.E_i=0, E_i^2=-1, monopole classes K +- E_i under the sign-family hypothesis) right? (2) Theorem 43.2 and the scalar consequence Delta V >= 4 pi^2 sum|e_i|. (3) Corollary 43.3: does the ledger really reproduce the first-order slope 6t/pi of the aligned Kahler law P=2(2pi+6t)^2+L/4 (profile Ric=-6g, sigma=3t/pi after rescaling psi=6 omega), including the Yamabe-volume upper estimate 16 hatV = Y^2 <= int s^2 and the Kahler integrals int s = -8pi^2(A+sigma), V=2pi^2(A-sigma^2)? Check c_1(M)=-(K+E) pairings. (4) Remark 43.4 smoothness/strictness argument. (5) The numerical ledger: the tail-free Yamabe-volume identity int s^2 - 576 hatV = int[e^2+48ev-1152v^3-576v^4] (profile scale, e=s+24, v=u-1, equation -6 Lap u + s u + 24u^3=0) and the conversions Ric=-g (g1=6g) giving Delta V = 36 dV_profile, D_W = deltaW + (2/3)DeltaV, Y0 in the form 8pi^2-P(hat g)=4 deltaW-(4/3)DeltaV; the LeBrun integrand (sqrt6|W+|_g - 12u^2)^2 dV_g; and the correction of A02's quoted split. (6) Theorem 43.5 (Ricci flow). Report errors with corrected formulas; do not restate correct parts at length.

## Integrated Scientific Memo

# Verification memo

The main period-linear argument is sound, but Step 43 needs corrections in Remark 43.4, the interpretation of “improving” A02, and the numerical discussion. The finite-time part of Theorem 43.5 is not verifiable from the supplied sources.

## 1. Proposition 43.1

For \(c\in\mathcal H_g^+\),
\[
(a_\varepsilon^+)^2\ge \frac{(a_\varepsilon\!\cdot c)^2}{c^2}.
\]
Thus the claimed estimate is correct in the applications \(K\cdot c>0\):
\[
\Pi_g\ge
\frac{\bigl(K\cdot c+\sum_i|E_i\cdot c|\bigr)^2}{c^2}-A.
\]
For arbitrary \(c\), the sign-robust stronger formulation is
\[
\boxed{\;
\Pi_g\ge
\frac{\bigl(|K\cdot c|+\sum_i|E_i\cdot c|\bigr)^2}{c^2}-A,
\;}
\]
obtained by choosing \(\varepsilon_i\) relative to \(\operatorname{sign}(K\cdot c)\). This also implies the displayed statement.

For \(c=K^+\), with \(B=\sum_i|e_i|\),
\[
K\cdot K^+=(K^+)^2=A+|K^-|^2,
\]
and therefore
\[
\Pi_g\ge |K^-|^2+2B+\frac{B^2}{(K^+)^2}.
\]
This is correct.

For
\[
c=K-\sum_i\sigma_iE_i\in\mathcal H_g^+,
\]
the conventions \(K\cdot E_i=0\), \(E_i\cdot E_j=-\delta_{ij}\) give exactly
\[
K\cdot c=A,\qquad E_i\cdot c=\sigma_i,\qquad
c^2=A-|\sigma|_2^2.
\]
Moreover,
\[
K^+=c+\sum_j\sigma_jE_j^+,
\qquad
e_i=E_i\cdot K^+
=\sigma_i+\sum_jG_{ij}\sigma_j.
\]
All signs are correct. In fact,
\[
\frac{(A+|\sigma|_1)^2}{A-|\sigma|_2^2}-A
=
2|\sigma|_1+|\sigma|_2^2+
\frac{(|\sigma|_1+|\sigma|_2^2)^2}{A-|\sigma|_2^2}.
\]

The blow-up conventions are also consistent:
\[
K_M=K+\sum_iE_i,\qquad c_1(M)=-(K+\sum_iE_i),
\]
and the assumed monopole family \(K+\sum_i\varepsilon_iE_i\) is the correct sign family.

### Necessary qualification

The new estimate does **not** uniformly dominate A02’s averaged quadratic estimate when \(b^+>1\). One may have
\[
e_i=E_i\cdot K^+=0,\qquad E_i^+\ne0.
\]
Hence “improving A02” should mean “adding a first-order period charge in directions with nonzero \(e_i\),” not pointwise domination for every metric. A safe combined statement is
\[
\Pi_g\ge |K^-|^2+
\max\left\{
2\sum_i|e_i|+\frac{(\sum_i|e_i|)^2}{(K^+)^2},
\ \sum_i|E_i^+|^2
\right\}.
\]
The first term can be sharpened by retaining
\(\bigl|\sum_i\operatorname{sign}(e_i)E_i^+\bigr|^2\).

For multiple rotated cells, \(e=(I+G)\sigma\) does not imply
\(\|e\|_1\ge\|\sigma\|_1\). The direct \(c\)-estimate
\[
\Pi_g\ge2\|\sigma\|_1+\|\sigma\|_2^2
\]
should be used there. The one-cell conversion is valid.

## 2. Theorem 43.2

The theorem follows correctly from LeB\(_{\rm full}\):
\[
P(\hat g)\ge
8\pi^2k-4\Delta V_{\rm free}
+8\pi^2\Pi_g
+\frac49\int(\sqrt6|W^+|-2)^2,
\]
where
\[
\Delta V_{\rm free}=\Delta V-2\pi^2\Pi_g\ge0.
\]
Substituting \(\Pi_g\ge2\sum_i|e_i|\) gives the displayed bound, and the scalar estimate gives
\[
\Delta V\ge2\pi^2\Pi_g
\ge4\pi^2\sum_i|e_i|.
\]
Both conclusions are correct. The harmonic splitting is conformally invariant in dimension four, so using the period data for \(g\) and the Yamabe representative causes no issue.

A stronger retained scalar consequence is
\[
\Delta V\ge2\pi^2\left[
|K^-|^2+2\sum_i|e_i|
+\frac{(\sum_i|e_i|)^2}{(K^+)^2}
\right].
\]

## 3. Corollary 43.3

For one exceptional class,
\[
c=\frac{[\psi]}{2\pi}=K-\sigma E,\qquad c_1(M)=-(K+E).
\]
Hence
\[
c_1(M)\cdot c=-(K+E)\cdot(K-\sigma E)=-(A+\sigma),
\]
and
\[
c^2=A-\sigma^2.
\]
Therefore the stated Kähler integrals are correct:
\[
\int s\,d\mu=-8\pi^2(A+\sigma),\qquad
V=2\pi^2(A-\sigma^2).
\]
If \(t=\int_E\omega\) in the profile scale and \(\psi=6\omega\), then
\[
2\pi\sigma=\int_E\psi=6t,\qquad \sigma=\frac{3t}{\pi}.
\]
Since for one class \(e=\sigma(1+G_{11})\ge\sigma\), the period ledger yields
\[
P\ge 8\pi^2\left(1+\frac{6t}{\pi}\right)-4\Delta V_{\rm free}.
\]

The Yamabe calculation can be strengthened from the note’s asymptotic form to an exact inequality. Since
\[
\int s^2
=L_s+\frac{(\int s)^2}{V}
=L_s+32\pi^2\frac{(A+\sigma)^2}{A-\sigma^2},
\]
and \(16\hat V=Y[g]^2\le\int s^2\),
\[
4\Delta V
\le
8\pi^2\left[
\frac{(A+\sigma)^2}{A-\sigma^2}-A
\right]+\frac{L_s}{4}.
\]
The bracket is precisely the \(c=K-\sigma E\) lower bound for \(\Pi_g\). Thus
\[
\boxed{\;4\Delta V_{\rm free}\le \frac{L_s}{4}\;}
\]
without an \(O(\sigma^2)\) error, and consequently
\[
P\ge
8\pi^2\left(1+\frac{6t}{\pi}\right)
-\frac{L_s}{4}
+\frac49\int(\sqrt6|W^+|-2)^2.
\]

The topological first-order coefficient agrees with
\[
2(2\pi+6t)^2
=8\pi^2\left(1+\frac{6t}{\pi}\right)+O(t^2).
\]
However, the exact Kähler law has \(+L_s/4\), while the lower ledger has
\(-L_s/4\). Thus “exactly the first-order slope” is justified for the explicit period/topological term; equality of the full first derivative additionally requires \(L_s=o(t)\), for example \(L_s=O(t^2)\).

## 4. Remark 43.4

The smoothness assertion is correct under \(Y<0\): the normalized Yamabe representative is unique and depends smoothly on the metric, and harmonic projections vary smoothly.

The derivative formula is wrong in general. Since
\[
(a_\varepsilon^+)^2-(a_{-\varepsilon}^+)^2
=4\sum_i\varepsilon_i e_i
\]
and
\[
e(\psi)=(I+G(\psi))\sigma(\psi),\qquad \sigma(0)=0,
\]
one has
\[
e'(0)=(I+G(0))\sigma'(0).
\]
Therefore
\[
\boxed{\;
F_\varepsilon'(0)-F_{-\varepsilon}'(0)
=-64\pi^2\,
\varepsilon\cdot (I+G(0))\sigma'(0).
\;}
\]
The formula in the note is valid only when \(G(0)\sigma'(0)=0\), in particular if all \(E_i^+(0)=0\).

The qualitative strictness survives: \(G(0)\) is positive semidefinite, so \(I+G(0)\) is positive definite. If \(\sigma'(0)\ne0\), choose \(\varepsilon\) so that
\(\varepsilon\cdot e'(0)\ne0\). If both nonnegative functions
\(F_\varepsilon,F_{-\varepsilon}\) had common value zero at \(0\), each derivative would vanish, contradicting the corrected derivative difference.

The quantitative optimization also needs an interval hypothesis. If, on \(|\psi|\le r\), the relevant even/odd second-order remainders are bounded by \(\Lambda\psi^2/2\), then with
\[
d=32\pi^2|\varepsilon\cdot e'(0)|
\]
one obtains
\[
F(0)\ge
\sup_{0\le\rho\le r}\left(d\rho-\frac{\Lambda}{2}\rho^2\right).
\]
This equals \(d^2/(2\Lambda)\) only if \(d/\Lambda\le r\). The note’s unrestricted optimization of a local expansion is therefore not justified as written.

## 5. Numerical ledger

### Exact identity

With \(s=-24+e\) and \(u=1+v\),
\[
s^2-576u^4-
\left(e^2+48ev-1152v^3-576v^4\right)
=-288\Delta v.
\]
After integration, assuming zero bolt and asymptotic flux,
\[
\int s^2-576\hat V
=
\int\left(e^2+48ev-1152v^3-576v^4\right).
\]
The tail-free identity is correct.

### Scale and Weyl conversions

For \(g_1=6g\),
\[
dV_{g_1}=36\,dV_g,\qquad
\Delta V_{s=-4}=36\,\Delta V_{\rm profile}.
\]
Also
\[
D_W=\delta W+\frac23\Delta V,
\]
and hence
\[
8\pi^2-P(\hat g)
=4D_W-4\Delta V
=4\delta W-\frac43\Delta V.
\]
These formulas are correct.

The LeBrun density conversion is also correct:
\[
(\sqrt6|W^+_{\hat g_1}|-2)^2\,dV_{\hat g_1}
=
(\sqrt6|W^+_g|-12u^2)^2\,dV_g.
\]

### A02 split and table values

Using the tail-free value
\[
\Delta V=0.0530962911742
\]
and
\[
\delta W=0.0187835500983,
\]
one gets
\[
4\Delta V=0.212385164697,
\]
\[
D_W=\delta W+\frac23\Delta V=0.0541810775478,
\qquad
4D_W=0.216724310191.
\]
Meanwhile,
\[
4\delta W=0.0751342003932,\qquad
\frac43\Delta V=0.0707950548990.
\]
Their difference is \(0.00433914549\), agreeing with the saving
\(1-P(\hat g)=0.00433913961\) up to the Gauss–Bonnet quadrature error. Thus the correction of A02 is right: the quoted \(0.07513\) and \(0.07080\) are \(4\delta W\) and \((4/3)\Delta V=48\Delta V_{\rm profile}\), not \(4D_W\) and \(4\Delta V\).

### Data-file inconsistency

The JSON headline fields are not the values used in the note’s table:
\[
\texttt{DeltaV}=0.0532416946,\qquad
\texttt{D\_W}=0.0542780131,
\]
whereas the table uses `DeltaV_identity` and recomputes \(D_W\). Likewise the table’s LeBrun slack is `F_LeB_identity`, not `F_LeB`. This should be made explicit or the output schema changed so the certified headline values are the identity-based ones.

The direct/identity discrepancy is not merely an amplification of numerical error in \(v(X)\). In this script, `I()` truncates exterior integration near \(100X\), while the PDE solve extends to \(10^4X\). Algebraically,
\[
\Delta V_{\rm direct}-\Delta V_{\rm identity}
=3\,R_{\rm trap},
\]
where \(R_{\rm trap}\) is the trapezoidal integral of the Yamabe equation:
\[
3(4.84677989\times10^{-5})
=1.45403\times10^{-4},
\]
matching the observed discrepancy. It is principally the omitted physical tail/finite-flux truncation, not a spurious \(10^{-8}\) boundary-value perturbation. The tail-free identity is still the correct quantity to use.

The reported pointwise residual
\[
\texttt{residual\_max}=0.2429
\]
is large in absolute terms, although likely dominated by near-bolt conditioning where the discrete operator has huge coefficients. It does not invalidate the integrated identities, but the note should not treat it as a pointwise-certified solve without a weighted residual or a regular-coordinate residual estimate. The finite-volume integrated residual suggests uncertainty of order \(10^{-5}\) in \(4\Delta V\), immaterial to the qualitative conclusions but relevant to quoted final digits.

Finally, the sentence saying an eigenvalue rises from \(-4\) to \(-1.12\) refers to the **profile metric** \(g\). In the \(s=-4\) Yamabe scale the CH eigenvalue is \(-2/3\), and \(-1.122\) becomes approximately
\[
-\frac{1.122}{6u^2}\approx-0.187.
\]
The eigenline/slot statement is conformally invariant and remains valid; only the scale label is wrong.

The computed cell-plus-CH-end quantities are relative noncompact model ledgers. They support the local arithmetic, but are not by themselves evaluations of the closed-manifold monopole inequalities; a closed host requires the collar/global Yamabe bookkeeping emphasized in A02.

## 6. Theorem 43.5

For an immortal normalized flow with uniformly bounded scalar curvature, the argument is correct. One has
\[
\bar s'=\frac{2P}{V}-\frac{L_s}{2V}.
\]
Using the negative Yamabe invariant and the scalar minimum evolution yields time-integrability of \(L_s\); boundedness of \(\bar s\) then gives
\[
\int_0^\infty P\,dt<\infty.
\]
Consequently there are \(t_j\to\infty\) such that
\[
P(t_j)+L_s(t_j)\to0.
\]
Since
\[
S(t_j)\ge Y[g(t_j)]^2\ge Y(M)^2>0,
\]
\[
\mathscr D(g(t_j))
=\frac{4P(t_j)+L_s(t_j)}{P(t_j)+S(t_j)/4}\to0,
\]
contradicting \(\alpha(M)>0\).

Thus the supplied material establishes
\[
T_{\max}=\infty,\quad Y(M)<0,\quad\alpha(M)>0
\quad\Longrightarrow\quad
\sup_{M\times[0,\infty)}|s|=\infty.
\]

The finite-time branch depends entirely on the external “family 351, Theorem 1.1,” whose statement is absent. The normalized-to-unnormalized conversion is fine, but the conclusion requires the strong theorem:

> A closed four-dimensional Ricci flow with uniformly bounded scalar curvature up to a finite maximal time extends smoothly past that time on the same smooth manifold.

An orbifold-limit or weak-continuation theorem is insufficient. Therefore Theorem 43.5 in its stated “every maximal flow” form is conditional on verifying that exact smooth extension statement; it is not independently established by the supplied files.