# TTCS Independent Branch Record

```json
{
  "step_id": 24,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step24_buffered_support_energy_test.md",
    "Sessions/S0910A01/workspace/scripts/step24_buffered_support_algebra.py",
    "Sessions/S0910A01/workspace/notes/step20_closed_tensor_estimate.md",
    "Sessions/S0910A01/workspace/notes/step16_preceptor_review_smoothing_architecture.md",
    "Sessions/S0910A03/workspace/notes/step22_critical_energy_lemma_formulation.md"
  ]
}
```

## Task

Verify the Step 24 buffered selected-support energy formulation for the normalized cutoff flow in the Yau 26 four-dimensional negative LeBrun laboratory. Read the note and script together with the prior tensor-structure note and support-geometry correction. Focus on whether separating the physical cutoff chi from the auxiliary energy cutoff eta really avoids bad-center/all-center smallness, whether the weighted cubic moment is the right one for the q=2 and q=3 estimates, whether the time-average propagation for A^4 H3(t) is mathematically justified or needs repair, and whether the triangular Q estimate has hidden terms or unsupported assumptions. Return a direct scientific memo: valid structural points, precise mathematical gaps, corrections, and which exact inequalities remain load-bearing.

## Output

# Scientific memo

## Overall finding

The buffered arrangement
\[
\operatorname{supp}\chi\Subset\{\eta=1\}\Subset\Omega_\eta
\]
is a genuine repair of the all-center smallness problem at the energy level. Every evolving term is contained in one domain whose initial \(L^2\)-curvature is controlled by the maximal-function condition at the single selected point \(p\). No neighboring center is needed for the \(q=2\), \(q=3\), or defect Sobolev estimates.

The remaining work is analytic rather than combinatorial: exact tensor inequalities under the evolving metric, persistence of the Sobolev inequality and cutoff-gradient bounds for a uniform time, and uniform smooth existence of the cutoff flow. The \(q=3\) reaction estimate also needs a different Sobolev variable from the one suggested by the “spatially subcritical” explanation.

## 1. Buffered support geometry

The identities
\[
a|\nabla\eta|^2=0,\qquad
\langle\nabla a,\nabla\eta\rangle=0,\qquad
\operatorname{supp}a\subset\{\eta=1\}
\]
are valid for every \(g(t)\), provided \(a=\chi^2\), \(\chi,\eta\) are time-independent, and \(\eta=1\) on an open neighborhood of \(\operatorname{supp}\chi\). They are support identities and do not depend on metric comparison.

On the open collar containing \(\operatorname{supp}\nabla\eta\), \(a\equiv0\), hence
\[
\partial_tg=0.
\]
Thus \(g(t)\), its curvature, its volume form, and \(E(t)\) are exactly fixed there. This is stronger and more precise than any finite-propagation statement.

If
\[
\mathcal M_{R_0}(|\Rm_{g_0}|^2)(p)\le K_0,\qquad L_\eta r\le R_0,
\]
then the same selected point directly gives
\[
\int_{\Omega_\eta}F(0)^2
 \le (1+K_0)\operatorname{Vol}_{g_0}(\Omega_\eta).
\]
Together with
\[
A_\Omega^2\le C(L_\eta)r^2
       \operatorname{Vol}_{g_0}(\Omega_\eta)^{-1/2},
\]
this yields
\[
A_\Omega^2\|F(0)\|_{L^2(\Omega_\eta)}
 \le C(L_\eta)r^2\sqrt{1+K_0}.
\]
The collapsed volume cancels correctly. If the chosen relative Sobolev theorem uses a dilated ball, that dilation must also lie inside \(B_{R_0}(p)\); this only changes the fixed support ratios and still uses the same point \(p\).

The volume-retaining thinning statement needs an explicit static packing lemma: begin with an \(r\)-separated family of selected good points, use local doubling from the Ricci lower bound to obtain bounded degree for intersections of \(B_{L_\eta r}(p_j)\), and then use a weighted coloring argument. Merely thinning an arbitrary family does not by itself give the stated volume fraction.

## 2. The \(q=2\) cubic moment is the correct one

Write
\[
S=A_\Omega^2,\qquad
Y(t)=\int aF^3\,d\mu_t.
\]
Because \(\eta=1\) on \(\operatorname{supp}a\),
\[
Y=\int(\chi F)^2F.
\]
Consequently,
\[
Y\le
\|F\|_{L^2(\operatorname{supp}\chi)}
\|\chi F\|_{L^4(\Omega_\eta)}^2.
\]
The Sobolev estimate and
\[
|\nabla(\chi F)|^2
 \le C a|\nabla F|^2+C|\nabla\chi|^2F^2
\]
give
\[
Y\le C\beta_a(t)\bigl(D_2+r^{-2}H_2\bigr),
\qquad
\beta_a(t):=
S\|F(t)\|_{L^2(\operatorname{supp}\chi)}.
\]
Here
\[
\beta_a(t)\le S H_2(t)^{1/2}
\]
because \(\eta=1\) throughout \(\operatorname{supp}\chi\). This active parameter is better suited to the first-exit argument than the note’s
\[
S\|F\|_{L^2(\Omega_\eta)}.
\]

The full-domain parameter can also be used, but the note omitted one line. Since \(\{\eta<1\}\) lies in the stationary collar,
\[
\|F(t)\|_{L^2(\Omega_\eta)}^2
 \le H_2(t)+
 \int_{\Omega_\eta\cap\{\eta<1\}}F(0)^2\,d\mu_0.
\]
Thus the full-domain norm is controlled by the evolving \(H_2\) plus a fixed initial contribution.

Conditional on the tensor inequality
\[
H_2'+cD_2\le CY+Cr^{-2}H_2,
\tag{2.1}
\]
smallness of \(\beta_a\) gives
\[
H_2'+c_1D_2\le C_1r^{-2}H_2.
\]
The first-exit closure is then valid:
\[
H_2(t)\le e^{C_1t/r^2}H_2(0),\qquad
\int_0^T D_2\le C H_2(0).
\]

Multiplying the integrated cubic estimate by \(S^2=A_\Omega^4\) gives
\[
S^2\int_0^T Y(t)\,dt
 \le C\beta_*\,S^2H_2(0)
 \le C\beta_0^3,
\tag{2.2}
\]
after defining \(\beta_0\) consistently from \(S H_2(0)^{1/2}\). This is the exact weighted moment produced by the \(q=2\) equation. A moment with weight \(a^{3/2}\) would not match its curvature reaction.

## 3. The \(q=3\) equation and the weight issue

Set
\[
Y=\int aF^3,\qquad
D_3=\int a^2F|\nabla\Rm|^2.
\]
The Step 20 power inequality applied with energy cutoff
\[
\zeta=\eta\chi
\]
has precisely this energy, since \(\zeta^2=\eta^2a=a\) on the active region. It gives schematically
\[
Y'+cD_3
 \le Cr^{-2}Y+C I_4,
\qquad
I_4=\int a^2F^4.
\tag{3.1}
\]
The regular cutoff terms close because
\[
|\nabla a|^2=4a|\nabla\chi|^2\le Cr^{-2}a.
\]

The explanation given for (6.2) through the “spatially subcritical” coefficient \(S^2Y\) is not presently derived. The natural variable for that argument,
\[
v=\sqrt a\,F^{3/2}=\chi F^{3/2},
\]
produces
\[
\int |\nabla\chi|^2F^3,
\]
which cannot be bounded by
\[
Cr^{-2}\int \chi^2F^3=Cr^{-2}Y.
\]
There is no uniform estimate \(|\nabla\chi|\le Cr^{-1}\chi\) for a compactly supported cutoff that reaches zero.

There is, however, a cleaner repair using the same critical parameter as the \(q=2\) estimate. Take
\[
u=aF^{3/2}.
\]
Then
\[
I_4=\int F\,u^2
 \le \|F\|_{L^2(\operatorname{supp}\chi)}\|u\|_4^2,
\]
while
\[
\begin{aligned}
\|\nabla u\|_2^2
&\le C\int a^2F|\nabla F|^2
  +C\int|\nabla a|^2F^3\\
&\le C D_3+Cr^{-2}Y.
\end{aligned}
\]
Therefore
\[
I_4\le C\beta_a(t)\bigl(D_3+r^{-2}Y\bigr).
\tag{3.2}
\]
For the fixed exponent \(q=3\), the initial radius can be chosen so that \(C\beta_a<c/2\). Equations (3.1)–(3.2) then yield the stronger linear estimate
\[
Y'\le Cr^{-2}Y.
\tag{3.3}
\]
Thus the quadratic term \(CS^2Y^2\) is unnecessary. It may remain as a harmless extra term, but its stated weighted interpolation argument is not supplied by the present notes.

## 4. Time-average propagation

The propagation mechanism is mathematically sound once either (3.3) or the displayed Riccati inequality has been proved.

From (2.2), for each \(0<t\le T\), there is \(s_0\in[t/2,t]\) such that
\[
S^2Y(s_0)
 \le \frac{2}{t}S^2\int_{t/2}^tY(s)\,ds
 \le \frac{C\beta_0^3}{t}.
\]
Using the linear estimate (3.3),
\[
Y(t)\le
e^{Cr^{-2}(t-s_0)}Y(s_0),
\]
and hence, for \(t\le\theta r^2\),
\[
S^2Y(t)\le \frac{C e^{C\theta}\beta_0^3}{t}.
\tag{4.1}
\]

Even if one retains
\[
Y'\le Cr^{-2}Y+CS^2Y^2,
\]
the same argument works because
\[
Y(t)\le Y(s_0)
 \exp\!\left(
 Cr^{-2}(t-s_0)+CS^2\int_{s_0}^tY(s)\,ds
 \right).
\]
The spacetime estimate controls the second exponent. Time averaging alone does not give the endpoint value; the forward differential inequality is the indispensable second step. Step 24 correctly adds that step, unlike the earlier parabolic-Sobolev wording.

## 5. Triangular defect energy

The combined variable \(E=\Ric+g\) is essential. Under
\[
\partial_tg=-2aE,
\]
its equation has the schematic homogeneous form
\[
\partial_tE
 =a\Delta_LE
  +(\nabla a)*\nabla E
  +(\nabla^2a)*E
  +a(\Rm*E)
  +a(E*E)
  -2aE.
\tag{5.1}
\]
Every term contains \(E\) or \(\nabla E\). In particular, an additive \((\nabla^2a)*g\) source cannot remain after the Ricci and normalization pieces are recombined: when \(E=0\), the velocity and every geometric time derivative vanish. The contrary statement in A03 Step 22, item 3, is incompatible with this stationarity identity.

Testing (5.1) against \(\eta^2E\) produces:

- \(X=\int\eta^2a|\nabla E|^2\) from the principal term;
- \(Cr^{-2}Q\) from \(\nabla a\) and \(\nabla^2a\), after one integration by parts and
  \[
  \frac{|\nabla a|^2}{a}=4|\nabla\chi|^2;
  \]
- no \(\nabla\eta\) contribution, owing to the stationary collar;
- \(CaF|E|^2\) from Lichnerowicz curvature, evolving tensor norms, the volume form, and the quadratic \(E\)-terms.

Thus the correct target is
\[
Q'+cX\le Cr^{-2}Q+C\int aF|E|^2.
\tag{5.2}
\]
The potential closes on the same selected support:
\[
\begin{aligned}
\int aF|E|^2
&=\int F|\chi E|^2\\
&\le \|F\|_{L^2(\operatorname{supp}\chi)}
       \|\chi E\|_4^2\\
&\le C\beta_a(t)\bigl(X+r^{-2}Q\bigr).
\end{aligned}
\tag{5.3}
\]
For small \(\beta_a\),
\[
Q'\le Cr^{-2}Q.
\tag{5.4}
\]
No curvature-only additive term appears. The remaining unproved part is the exact index-level derivation of (5.2), including all current-metric norm and measure variations.

For several supports, the global conclusion uses disjoint active supports and the fact that the complement is stationary. The local estimate itself does not provide the positive-volume plateau selection or the initial normalized smallness of the global \(Q\); those are separate geometric and topological inputs.

## 6. Uniform evolving geometry remains essential

All Sobolev applications above occur at time \(t\), whereas (2.2) in the note is stated for \(g_0\). A load-bearing estimate is therefore
\[
\|u\|_{L^4(g(t))}^2
 \le C S\left(
 \|\nabla u\|_{L^2(g(t))}^2+r^{-2}\|u\|_{L^2(g(t))}^2
 \right)
\tag{6.1}
\]
with \(C\) uniform for \(0\le t\le\theta r^2\). The same issue applies to
\[
|\nabla\chi|_{g(t)}\le Cr^{-1}.
\]

Step 24 does not derive metric equivalence or an evolving Sobolev estimate. Critical \(L^2\)-energy persistence alone does not control the pointwise speed \(aE\), so it does not directly imply such equivalence. Uniform smooth existence for the degenerate local flow on \([0,\theta r^2]\) is likewise an additional theorem component. These facts are needed before the first-exit argument becomes uniform across the LeBrun sequence.

## 7. Role of the script

`step24_buffered_support_algebra.py` correctly records:

- the \(r^2\sqrt{1+K_0}\) scaling of the critical parameter;
- cancellation of collapsed volume;
- the support identities;
- the monomial relation
  \[
  S^2\int Y\sim\beta^3;
  \]
- the time-average scale \(\beta^3/t\).

Its numerical absorption constant is illustrative, not a tensor constant. The script does not establish the curvature evolution, the \(q=3\) reaction estimate, evolving Sobolev control, flow existence, or the volume-retaining support selection.

## Load-bearing mathematical objects

The buffered program rests on the following exact statements:

1. Uniform evolving Sobolev and cutoff-gradient estimate (6.1).
2. Exact \(q=2\) tensor inequality (2.1).
3. Exact \(q=3\) tensor inequality (3.1), together with the repaired reaction estimate (3.2).
4. Exact triangular defect inequality (5.2).
5. Uniform smooth existence and metric control through \(t=\theta r^2\).
6. A fixed-ratio packing/coloring lemma retaining definite selected plateau volume.

Subject to these objects, the selected-support formulation genuinely removes the bad-center/all-center smallness issue, and the weighted cubic plus time-average mechanism closes entirely within each selected support.