# TTCS Independent Branch Record

```json
{
  "step_id": 92,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step92_route_comparison_and_ab_heat_sign.md",
    "Sessions/S0910A01/workspace/notes/step91_receiver_and_adjacent_green.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step47_entropy_degree_theorem.md",
    "Sessions/S0910A01/workspace/data/step92_ab_heat_sign_formula.json",
    "Sessions/S0910A01/workspace/data/step91_adjacent_ab_heat_spectral.json"
  ]
}
```

## Task

Verify the Step 92 route comparison and AB adjacent heat sign argument. Read the Step 92 note plus the Step 91 product note, Step 47 entropy/degree note, and Step 92 support data. Check especially: (1) whether the hyperbolic X#X continuity and corrected Lohkamp-ratio statement are mathematically accurate; (2) whether the AB-sector reduction after adjacent m=2 polarization cancellation to K_adj^AB=(1/512)∫ e^s A(s)B(s) ds is consistent with Step 91 normalization; (3) whether the claimed sign proof B(s)<0 via monotonicity of the scalar heat kernel at antipodal points on S^2 is actually valid for all s>0, or whether it needs an additional theorem/proof/correction; and (4) what remains before the result affects the full Ozuch coefficient or Yau-26. Give a direct scientific memo with any errors and repairs.

## Output

# Scientific verification memo

## 1. Hyperbolic \(X\#X\) route

The Step 92 continuity statement is mathematically sound. Let
\[
-3(1+\varepsilon)g\le \operatorname{Ric}_g\le -3(1-\varepsilon)g,
\qquad 0\le\varepsilon\le \frac13,
\]
and write the Ricci eigenvalues as \(-3x_i\), where \(x_i\in[1-\varepsilon,1+\varepsilon]\). In dimension four,
\[
\frac{s^2}{24}-\frac{|E|^2}{2}
=\frac{s^2}{6}-\frac{|\operatorname{Ric}|^2}{2}
=\frac32\Big(\sum_i x_i\Big)^2-\frac92\sum_i x_i^2.
\]
For each variable separately this quadratic is concave, so its minimum on the box occurs at a vertex. If exactly \(k\) of the \(x_i\) equal \(1+\varepsilon\), the first competitors to the all-low vertex give
\[
Q_1-Q_0=6\varepsilon(1-3\varepsilon),\qquad
Q_2-Q_0=12\varepsilon(1-2\varepsilon).
\]
The remaining two are larger. Hence, for \(\varepsilon\le1/3\),
\[
\frac{s^2}{24}-\frac{|E|^2}{2}\ge 6(1-\varepsilon)^2.
\]
This validates the sharpened Chern–Gauss–Bonnet estimate
\[
\operatorname{Vol}(X\#X,g)
\le
\frac{4\pi^2}{3}\,
\frac{2\chi(X)-2}{(1-\varepsilon)^2}
=
\frac{2\operatorname{Vol}(X)(1-1/\chi(X))}
{(1-\varepsilon)^2}.
\]

For the lower estimate, set \(q=(1+\varepsilon)g\). Then
\[
\operatorname{Ric}_q=\operatorname{Ric}_g\ge-3q,
\qquad
\operatorname{Vol}_q=(1+\varepsilon)^2\operatorname{Vol}_g.
\]
The degree-two map \(X\#X\to X\) and BCG yield
\[
\operatorname{Vol}_g(X\#X)
\ge \frac{2\operatorname{Vol}(X)}{(1+\varepsilon)^2}.
\]
Thus the two bounds are incompatible when
\[
\varepsilon<
\frac{1-\sqrt{1-1/\chi(X)}}{1+\sqrt{1-1/\chi(X)}}
=
\frac1{4\chi(X)}+O(\chi(X)^{-2}).
\]
The displayed lower-volume estimate comes from BCG; Bishop comparison is not needed and does not itself produce this degree-sensitive lower bound. At the endpoint, the BCG equality case would force a two-sheeted Riemannian covering, contradicting
\[
\chi(X\#X)=2\chi(X)-2\ne2\chi(X),
\]
so the endpoint is excluded as well whenever the equality theorem is invoked. The condition \(\varepsilon\le1/3\) remains part of the box argument.

The no-Einstein argument for \(X\#X\) is also correct:

- \(\lambda>0\) contradicts Myers because \(\pi_1(X\#X)=\pi_1(X)*\pi_1(X)\) is infinite.
- \(\lambda=0\) contradicts the virtually abelian structure of compact Ricci-flat fundamental groups.
- For \(\lambda<0\), scale to \(\operatorname{Ric}=-3g\). BCG gives volume at least \(2\operatorname{Vol}(X)\), while Chern–Gauss–Bonnet gives
  \[
  \operatorname{Vol}(X\#X,g)
  \le\frac{4\pi^2}{3}\chi(X\#X)
  =2\operatorname{Vol}(X)-\frac{8\pi^2}{3}.
  \]

Consequently, a sequence with pinching error tending to zero would indeed address the normalized \(\lambda<0\) branch, but it would necessarily remain above the target-dependent BCG–CGB margin; decay slower than \(1/\chi(X_i)\) is not excluded by the present calculation.

### Lohkamp scaling statement

The geometric point is correct after making \(a,b\) extremal. If \(\rho_i(x)\) are the eigenvalues of \(g^{-1}\operatorname{Ric}_g\), define
\[
a=\min_{x,i}(-\rho_i(x)),\qquad
b=\max_{x,i}(-\rho_i(x)).
\]
For \(g'=tg\), the Ricci eigenvalues relative to \(g'\) are \(\rho_i/t\), so \(b/a\) is unchanged. Writing \(c=-\beta\), \(C=-\alpha\), with \(\beta>\alpha>0\), a scaling fitting
\[
cg'\le\operatorname{Ric}_{g'}\le Cg'
\]
exists exactly when
\[
\frac b\beta\le\frac a\alpha,
\qquad\text{equivalently}\qquad
\frac ba\le\frac{|c|}{|C|}.
\]
If \(a,b\) are merely loose enclosing constants, that ratio condition is sufficient but not necessary. The Step 92 sentence is therefore exact when \(a,b\) denote the sharp global extrema.

## 2. AB formula and normalization

The factor \(1/512\) is internally consistent with the Step 91 receiver and source conventions. For an \(L^2\)-normalized zonal harmonic,
\[
Y_{\ell0}(N)=\sqrt{\frac{2\ell+1}{4\pi}},
\qquad
Y_{\ell0}(S)=(-1)^\ell Y_{\ell0}(N),
\]
and its isotropic Hessian coefficient at a pole is
\[
q_\ell=-\frac{\mu_\ell}{2}Y_{\ell0},
\qquad \mu_\ell=\ell(\ell+1).
\]
For the coexact–coexact mode, the sparse receiver gives \(R=q_\ell q_k\), up to the fixed Step 91 orientation convention. Hence
\[
R_{NN}R_{NS}
=
(-1)^k\frac{(2\ell+1)(2k+1)\mu_\ell^2\mu_k^2}
{256\pi^2}.
\]
Dividing by the stated quotient norm \(\mu_\ell\mu_k\) and multiplying by the principal source factor \(\pi^2/2\) gives
\[
\frac1{512}(-1)^k(2\ell+1)(2k+1)\mu_\ell\mu_k.
\]
With
\[
p_{\ell k}=\frac{\mu_\ell+\mu_k}{2}-1,
\]
this reproduces exactly
\[
K_\tau^{AB}
=
\frac1{512}\sum_{\ell,k\ge1}
(-1)^k
\frac{(2\ell+1)(2k+1)\mu_\ell\mu_k}{p_{\ell k}}
e^{-\tau p_{\ell k}}.
\]
As a useful normalization test, the \((\ell,k)=(1,1)\) term at \(\tau=0\) is
\[
-\frac{3\cdot3\cdot2\cdot2}{512}=-\frac9{128},
\]
matching the Step 91 axial value.

The \(m=2\) cancellation is consistent with the supplied numerical decomposition: the four exact/coexact polarization channels have equal eigenvalues, equal norms and relative signs
\[
+1,-1,+1,-1.
\]
The matrix mechanism can be expressed using
\[
D=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
O=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
J=\begin{pmatrix}0&-1\\1&0\end{pmatrix},
\]
with \(JD=O\) and \(JO=-D\). Together with the transported pole frames, these identities produce equal absolute receiver products and the displayed sign pattern. The supplied material does not yet contain that written mode-by-mode derivation, although the JSON data exhibit the exact cancellation at every sampled \(\tau\). Once the termwise matrix identity is included, no conditional rearrangement issue remains.

Using
\[
\frac{e^{-\tau p}}p=\int_\tau^\infty e^{-sp}\,ds
\]
then gives
\[
K_\tau^{AB}
=
\frac1{512}\int_\tau^\infty e^sA(s)B(s)\,ds,
\]
with the Step 92 definitions of \(A\) and \(B\). This is an Abel/heat-regularized value; the double series at \(\tau=0\) is not being asserted to converge absolutely.

## 3. Heat-kernel sign

The resulting sign is correct, but the inference in the prose needs one additional step. Spatial radial monotonicity makes the antipodal value the global minimum, and the heat semigroup makes that minimum increase with time. This gives
\[
\partial_t p_t(\pi)\ge0,\qquad B(s)\le0.
\]
Strict increase of a smooth function does not by itself imply that its derivative is \(>0\) at every individual time. Thus the sentence “strict increase, therefore \(B(s)<0\) for every \(s>0\)” does not follow solely from the stated maximum-principle argument. It already suffices for the integral sign, since strict semigroup increase ensures that the derivative is positive on nonempty open sets.

There is, however, a short exact proof of the stronger pointwise statement. Put \(x=\cos r\), and let \(p_t^{(d)}(x)\) denote the heat kernel on the unit \(S^d\). From
\[
p_t^{(2)}(x)=\frac1{4\pi}\sum_{\ell\ge0}
(2\ell+1)P_\ell(x)e^{-\ell(\ell+1)t}
\]
and \(P_\ell'(x)=C_{\ell-1}^{3/2}(x)\), comparison with the \(S^4\) spectral expansion gives
\[
\partial_xp_t^{(2)}(x)
=
2\pi e^{-2t}p_t^{(4)}(x).
\]
For a zonal function on \(S^2\),
\[
\Delta=(1-x^2)\partial_x^2-2x\partial_x.
\]
At the antipode \(x=-1\),
\[
\partial_t p_t^{(2)}(-1)
=
2\partial_xp_t^{(2)}(-1)
=
4\pi e^{-2t}p_t^{(4)}(-1)>0,
\]
because the heat kernel on connected \(S^4\) is positive for every \(t>0\). Therefore
\[
\boxed{
B(s)=-16\pi^2e^{-s}p_{s/2}^{(4)}(-1)<0.
}
\]
Substitution gives the particularly transparent formula
\[
\boxed{
K_\tau^{AB}
=
-\frac{\pi^2}{32}
\int_\tau^\infty
A(s)\,p_{s/2}^{(4)}(-1)\,ds<0.
}
\]

This also proves convergence. As \(s\downarrow0\),
\[
A(s)=O(s^{-2}),
\]
while the \(S^4\) heat kernel between antipodal points has off-diagonal exponential decay. As \(s\to\infty\),
\[
A(s)=6e^{-s}+O(e^{-3s}),
\qquad
p_{s/2}^{(4)}(-1)\longrightarrow \frac1{\operatorname{Vol}(S^4)}.
\]
Hence the integral is absolutely finite at both ends. The decimal
\[
-0.03144249732
\]
is strongly supported by the \(\tau\)-ladder and by the exact \(-9/128\) low-mode test, though the supplied data do not attach interval-enclosed numerical tails to the final digits. The sign itself is fully analytic.

## 4. Relation to the full Ozuch coefficient and Yau–26

The established mathematical object is the off-diagonal adjacent AB transfer in the Step 91 principal convention. The full coefficient still depends on:

1. the actual Eguchi–Hanson \(H^4\) asymptotic tensor and its ALE Green-pairing normalization;
2. the quotient isotropy factor and the precise convention for \(\odot\);
3. Bianchi correction, gauge projection and the regularized inverse used in the gluing chart;
4. the AA and BB tensor-harmonic sectors, including the omitted magnetic tensor modes noted in Step 91;
5. transported node-frame signs and equality of all ordered adjacent coefficients;
6. differentiated heat-kernel estimates for every source component;
7. identification with the \(t_i\lambda_i+t_i^2\mu_i\) radial expansion and an error smaller than the \(t_it_j^2\) interaction;
8. calibration against the all-same chirality family and the local self-interaction terms.

The actual ALE source multiplier could also reverse the convention-dependent sign, and AA/BB contributions could reinforce or cancel the AB term. Thus the current result determines a genuine sector sign, not yet the sign of the complete radial coefficient.

Even a nonzero complete adjacent coefficient concerns Einstein correction near this mixed-chirality desingularization chart. Connection to Yau–26 additionally requires the smooth type of the desingularized manifold, a family of metrics with operator Ricci pinching tending to an Einstein constant, and a proof that the same smooth manifold carries no Einstein metric for any \(\lambda\). A local gluing obstruction does not exclude an Einstein metric elsewhere in the space of metrics.