# TTCS Independent Branch Record

```json
{
  "step_id": 81,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step81_alignment_mechanism_definitive.md",
    "Sessions/S0910A02/workspace/data/step81_alignment_chain_exact.json",
    "Sessions/S0910A02/workspace/data/step81_spectral_analysis.json",
    "Sessions/S0910A02/workspace/notes/step79_alignment_closure_and_collapse_transition.md"
  ]
}
```

## Task

Verify and extend the following analysis of the harmonic-form alignment mechanism for positive Einstein 4-manifolds.

The key result: the summed Weitzenböck chain for b_+ independent harmonic self-dual forms on a positive Einstein 4-manifold reduces, after Cauchy-Schwarz with θ=0 (rank-1 T) and κ=1 (constant trT), to EXACTLY the Gursky-LeBrun inequality ∫|W+|² ≥ ∫s²/24, independent of b_+. The margin for χ=8, τ=0 rows is exactly √(3/2) ≈ 22.5%.

Three questions to verify and check for errors or missed opportunities:

1. Is the b_+ cancellation correct? The chain is: (s/3)b_+ ≤ 2√(2/3)(∫|W+|²)^{1/2}(∫(trT)²)^{1/2}, and with Q-orthonormal forms, ∫trT = b_+, κ=1 gives (∫(trT)²)^{1/2} = b_+/√V, so b_+ cancels. Is this the sharpest possible use of the Weitzenböck formula, or is there a better way to exploit b_+ ≥ 3 that doesn't go through the crude α·trT bound?

2. The degeneracy defect: on b_+ ≥ 2 Einstein, β ≠ -α/2 somewhere (otherwise Kähler, b_+=1). Does any known result quantify the measure or depth of this deviation? Does the refined Kato |∇W+|² ≥ (5/3)|∇|W+||² (Gursky-LeBrun) combine with a Sobolev inequality to give a quantitative strict inequality for b_+ ≥ 2?

3. The CLR/spectral reformulation: the Weitzenböck operator L = ∇*∇ - 2W+ + (s/3) has b_+ zero modes. On Kähler (b_+=1): potential V = diag(0,6,6) ≥ 0, one zero mode with zero potential. For b_+ = 3: need 3 zero modes, forcing more negative potential. Does this give a b_+-dependent Weyl bound through any known spectral inequality (CLR, Li-Yau, Berezin, or other)?

## Output

# Scientific verification memo

## 1. The \(b_+\)-cancellation is algebraically correct, but the relation to Gursky–LeBrun needs qualification

Let \(b=b_+\), \(f=\operatorname{tr}T=\sum_a|\omega_a|^2\), and
\[
E_+=\int_M |W^+|^2\,dV,\qquad
G=\sum_a\int_M|\nabla\omega_a|^2\,dV .
\]
For an \(L^2\)-orthonormal basis of harmonic self-dual forms,
\[
\int_M f\,dV=b.
\]
The summed Weitzenböck identity is
\[
G+\frac{s}{3}b=2\int_M\langle W^+,T\rangle\,dV.
\]
Since \(T\ge0\) and \(\alpha\) is the largest eigenvalue of \(W^+\),
\[
\langle W^+,T\rangle\le \alpha f
 \le \sqrt{\frac23}|W^+|f.
\]
Consequently,
\[
G+\frac{s}{3}b
 \le 2\sqrt{\frac23}\,E_+^{1/2}\left(\int_M f^2\right)^{1/2}.
\]
With
\[
\kappa^2=\frac{V\int f^2}{b^2},
\]
this becomes
\[
\frac{G}{b}+\frac{s}{3}
 \le 2\sqrt{\frac23}\,\kappa\sqrt{\frac{E_+}{V}}.
\]
Thus \(b\) cancels exactly, even for arbitrary \(\kappa\). Dropping \(G\) gives
\[
\frac{E_+}{V}\ge \frac{s^2}{24\kappa^2}.
\]
For \(s=12\),
\[
\frac{E_+}{V}\ge \frac6{\kappa^2}.
\]

The important distinction is that \(\kappa=1\) is not automatic. Jensen gives \(\kappa\ge1\), with equality precisely when
\[
f=\sum_a|\omega_a|^2=\frac bV
\]
almost everywhere. Therefore setting \(\kappa=1\) identifies the strongest numerical value obtainable from this particular Cauchy–Schwarz arrangement:
\[
E_+\ge \frac{s^2V}{24}.
\]
It does not derive the full Gursky–LeBrun theorem for a general, spatially varying harmonic-form density. Gursky–LeBrun obtains the same inequality without assuming \(f\) constant, using the refined Kato and Yamabe machinery. The crude summed chain coincides with their numerical constant only in its uniform-density extremal model. The \(\mathbb{CP}^2\) calibration has exactly this structure: the Kähler form is parallel and has constant norm.

### The \(22.5\%\) number

For \(\chi=8,\tau=0\), \(\operatorname{Ric}=3g\), \(s=12\),
\[
E_+=32\pi^2-3V,
\qquad
A:=\frac{E_+}{V}=\frac{32\pi^2}{V}-3.
\]
Bishop gives \(V\le 8\pi^2/3\), hence \(A\ge9\). The formal rank-one, \(\kappa=1\) ratio is
\[
\frac{2\sqrt{2/3}\sqrt A}{4}=\sqrt{\frac A6}.
\]
At the Bishop volume this is
\[
\sqrt{\frac96}=\sqrt{\frac32}=1.224744\ldots.
\]
Thus \(22.47\%\) is the least excess allowed by the Bishop estimate. Equality in Bishop would force the round \(S^4\), so on a \(\chi=8\) manifold one actually has \(A>9\); the corresponding ratio is strictly larger than \(\sqrt{3/2}\), although the supplied estimates do not quantify the strictness.

---

## 2. A sharper matrix use of the summed formula

The crude estimate \(\langle W^+,T\rangle\le\alpha f\) discards all information except \(\operatorname{tr}T\). Since \(W^+\) is trace-free, the natural exact object is
\[
T_0=T-\frac f3 I.
\]
Then
\[
\langle W^+,T\rangle=\langle W^+,T_0\rangle
 \le |W^+|\,|T_0|.
\]
If \(r_i=t_i/f\), where \(t_1\ge t_2\ge t_3\ge0\), then
\[
\frac{|T_0|^2}{f^2}
 =r_1^2+r_2^2+r_3^2-\frac13.
\]
This gives the exact anisotropy parameter
\[
q(T)=\frac{|T_0|}{f}\in\left[0,\sqrt{\frac23}\right].
\]
The notable models are

\[
\begin{array}{c|c}
(t_1,t_2,t_3)/f & q(T)\\ \hline
(1,0,0) & \sqrt{2/3}\\
(1/2,1/2,0) & 1/\sqrt6\\
(1/3,1/3,1/3) & 0.
\end{array}
\]

Consequently,
\[
G+\frac{s}{3}b
 \le 2E_+^{1/2}\left(\int_M f^2q(T)^2\,dV\right)^{1/2}.
\]
This is strictly sharper than the \(\alpha f\) estimate whenever \(T\) is not rank one. It also shows exactly where any \(b_+\)-sensitive information must enter: a weighted upper estimate for \(q(T)\), an upper estimate for \(\kappa\), or a lower estimate for \(G/b\).

### Correction to the stated \(\theta\)-analysis

The exact rearrangement inequality is
\[
\langle W^+,T\rangle
 \le \alpha t_1+\beta t_2+\gamma t_3
 =\alpha f-(\alpha-\beta)t_2-(\alpha-\gamma)t_3.
\]
If \(\theta=t_2/f\) and one takes the worst case \(t_3=0\), optimization over trace-free \(W^+\) with \(|W^+|=1\) gives
\[
C_\theta
 =\sqrt{\frac23-2\theta+2\theta^2}.
\]
This reproduces \(\theta_*=0.127322\ldots\) at \(A=9\).

Two statements in the supplied note require correction:

1. For \(t_1\ge t_2\ge t_3\ge0\),
   \[
   0\le \frac{t_2}{f}\le\frac12,
   \]
   not \(1/3\). The value \(1/3\) describes full isotropy, but is not the largest possible middle-eigenvalue ratio.

2. The statement that the method cannot close for \(A>18\) “regardless of isotropy” is incorrect. At \((t_1,t_2,t_3)=f(1/2,1/2,0)\), the coefficient is \(1/\sqrt6\), which reaches the formal threshold \(A=24\). At full isotropy, \(\langle W^+,T\rangle=0\), which is incompatible with the positive scalar term for every \(A\). The real missing estimate is quantitative proximity of \(T\) to isotropy, not an absolute \(A=18\) obstruction.

### What \(b_+\ge2\) provides pointwise

Two globally independent harmonic self-dual forms are not automatically pointwise independent merely because both are nonzero. Nevertheless, their collinearity cannot hold on an open set. If \(\eta=f\omega\) there and \(\omega\ne0\), then self-duality gives
\[
\omega\wedge\omega=|\omega|^2\,dV,
\]
so \(\omega\) is symplectic. From \(d\omega=d\eta=0\),
\[
df\wedge\omega=0,
\]
and hence \(df=0\). Unique continuation then gives global dependence. Analyticity of Einstein metrics and harmonic forms therefore yields \(\operatorname{rank}T\ge2\) almost everywhere when \(b_+\ge2\).

This proves only
\[
q(T)<\sqrt{\frac23}
\quad\text{almost everywhere},
\]
with no uniform amount. Three forms need not make \(T\) rank three almost everywhere. Thin-neck metrics also show that the intersection-form normalization \(\int\langle\omega_a,\omega_b\rangle=\delta_{ab}\) is compatible with densities concentrated in largely separate regions. Such metrics are not exact positive Einstein metrics, but they demonstrate why topology and unique continuation alone do not control \(t_2/f\).

A further important point is that a lower Weyl estimate
\[
E_+\ge f(b_+)V,\qquad f(3)>9,
\]
would not by itself rule out positive Einstein metrics on these rows. Since
\[
A=\frac{32\pi^2}{V}-3
\]
is unbounded as \(V\to0\), the inequality \(A\ge f(3)\) merely supplies another upper estimate for \(V\). A complete exclusion from this mechanism would need an upper estimate for \(A\), a lower estimate for \(V\), or a relation forcing the effective anisotropy \(\kappa q\) to decay as \(A\) grows.

---

## 3. The algebraic degeneracy defect and refined Kato inequality

Write
\[
\beta=-\frac{\alpha}{2}+u,\qquad
\gamma=-\frac{\alpha}{2}-u.
\]
Then the deviation from the repeated-eigenvalue pattern is exactly
\[
D:=|W^+|^2-\frac32\alpha^2
 =2u^2
 =\frac12(\beta-\gamma)^2.
\]
Thus \(D=0\) precisely when
\[
(\alpha,\beta,\gamma)
 =\left(\alpha,-\frac\alpha2,-\frac\alpha2\right).
\]

The Derdziński interpretation in the note is too strong. For an Einstein metric, \(\delta W^+=0\), and the repeated-eigenvalue pattern gives a locally conformally Kähler structure on the region where \(W^+\ne0\). It does not imply \(\nabla W^+=0\). The Page and Chen–LeBrun–Weber metrics are relevant countermodels: they are Einstein and conformally Kähler in the appropriate orientation, but not locally symmetric.

Under the compact positive-Einstein hypotheses used by Wu/LeBrun, the global repeated-eigenvalue regime leads to the conformally Kähler family and ultimately \(b_+=1\). Hence \(b_+\ge2\) implies \(D>0\) somewhere, and continuity gives a nonempty open region with \(D>0\). None of the cited results supplies a dimension-only lower estimate for either the volume of this region or the integral
\[
\int_M D\,dV.
\]

The refined Kato inequality
\[
|\nabla W^+|^2\ge\frac53|\nabla|W^+||^2
\]
does not directly measure \(D\). Repeated-eigenvalue, conformally Kähler Einstein metrics may have \(D=0\) while \(\nabla W^+\ne0\). Combining refined Kato, the Derdziński Bochner identity, and the Yamabe inequality yields rigidity at equality and therefore
\[
E_+>\frac{s^2V}{24}
\]
when \(b_+\ge2\). It does not produce
\[
E_+\ge (1+\varepsilon)\frac{s^2V}{24}
\]
with \(\varepsilon>0\) depending only on dimension or \(b_+\).

The analytic reason is visible in the Yamabe constant:
\[
Y([g])=s\sqrt V
\]
for a positive Einstein metric. Along a volume-collapsing normalized sequence, \(Y\to0\), so the Sobolev control used in the refined-Kato argument weakens. A numerical stability statement would require additional compactness input such as a volume lower estimate together with curvature or injectivity control.

---

## 4. The spectral reformulation is promising, but the stated CLR inequality is not valid as written

With \(s=12\),
\[
L=\nabla^*\nabla+U,\qquad U=4I-2W^+,
\]
and
\[
\operatorname{spec}(U)
 =(4-2\alpha,\,4-2\beta,\,4-2\gamma).
\]
There can be two eigenvalues of \(U\) below zero: both \(\alpha\) and \(\beta\) may exceed \(2\). Trace-freeness only ensures \(\gamma\le0\). Therefore the attractive matrix part is
\[
P_+=(2W^+-4I)_+,
\]
with
\[
\operatorname{tr}(P_+^2)
 =(2\alpha-4)_+^2+(2\beta-4)_+^2.
\]
Keeping only the \(\alpha\)-channel misses a possible second channel.

More fundamentally, the proposed estimate
\[
b_+\le \frac{C}{Y^2}\int(2\alpha-4)_+^2\,dV
\]
cannot count the kernel on a compact manifold. On Kähler–Einstein \(\mathbb{CP}^2\),
\[
U=\operatorname{diag}(0,6,6),\qquad P_+=0,
\]
yet \(L\) has the parallel Kähler form in its kernel. Ordinary CLR counts eigenvalues strictly below zero for a coercive background operator; it does not count threshold modes of \(\nabla^*\nabla-P\) when the rough Laplacian itself has parallel zero modes.

### A correct coercive formulation

Introduce
\[
H=\nabla^*\nabla+\frac{s}{6}I,\qquad
Q=2W^+-\frac{s}{6}I,
\]
so that
\[
L=H-Q.
\]
The Yamabe inequality and the diamagnetic inequality give the coercive Sobolev estimate
\[
\langle H\phi,\phi\rangle
 \ge \frac{Y}{6}\|\phi\|_{L^4}^2.
\]
If \(\dim\ker L=b_+\), then the min–max principle implies that \(H-Q_+\) has at least \(b_+\) eigenvalues at or below zero. Applying CLR after an arbitrarily small enlargement of \(Q_+\) yields a schematic, mathematically appropriate estimate
\[
b_+
 \le \frac{C_{\mathrm{CLR}}}{Y^2}
 \int_M\operatorname{tr}\!\left(2W^+-\frac{s}{6}I\right)_+^2\,dV,
\]
where the coefficient absorbs the Sobolev normalization, bundle rank, and CLR constant.

For \(s=12\), the relevant attractive eigenvalues are
\[
(2\alpha-2)_+,\qquad (2\beta-2)_+.
\]
This formulation correctly counts the Kähler zero mode. Indeed, on \(\mathbb{CP}^2\),
\[
Q=\operatorname{diag}(2,-4,-4),\qquad
\int\operatorname{tr}(Q_+^2)=4V,
\qquad
Y^2=144V.
\]
Thus any estimate written with the coefficient exactly as above must have
\[
C_{\mathrm{CLR}}\ge36
\]
in order to accommodate \(b_+=1\). This also shows why the Euclidean coefficient \(0.019\) and the reported threshold \(5.9\) are not directly comparable to the compact threshold problem.

Since
\[
\operatorname{tr}(Q_+^2)\le4|W^+|^2,
\]
the corrected CLR estimate implies only
\[
\frac{E_+}{V}\ge \frac{36\,b_+}{C_{\mathrm{CLR}}}
\qquad (s=12).
\]
This is genuinely \(b_+\)-dependent, but it is another lower estimate for \(A=E_+/V\), and \(A\) can grow without bound as \(V\to0\). It therefore does not by itself exclude the \(\chi=8,\tau=0\) rows.

Li–Yau heat-kernel estimates, Berezin bounds, and Birman–Schwinger methods encounter the same structural issues: threshold kernel modes, possible parallel sections, two attractive matrix channels, and constants controlled by the compact Sobolev geometry. No supplied spectral result produces the sharp volume-sensitive relation needed here.

## Bottom line

- The algebraic \(b_+\)-cancellation is correct.
- The crude chain equals the Gursky–LeBrun numerical constant only in the formal \(\kappa=1\) model; it is not a derivation of their general theorem.
- The \(22.47\%\) factor is the Bishop-ceiling benchmark and is unattained on a \(\chi=8\) manifold.
- The exact matrix refinement is governed by \(T_0\), not only \(t_2/\operatorname{tr}T\); the stated maximum \(\theta=1/3\) and the absolute \(A=18\) cutoff are incorrect.
- Refined Kato gives strictness for \(b_+\ge2\), but no dimension-only quantitative amount.
- The original CLR inequality cannot count the Kähler threshold mode and omits a possible \(\beta\)-channel. A shifted coercive CLR formulation is valid in principle, but its constants and the unbounded behavior of \(A\) prevent the desired positive-Einstein exclusion.