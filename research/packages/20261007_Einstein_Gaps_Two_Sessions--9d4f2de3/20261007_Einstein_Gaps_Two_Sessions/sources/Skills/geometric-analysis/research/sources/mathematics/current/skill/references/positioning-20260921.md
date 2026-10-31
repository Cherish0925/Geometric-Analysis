# Integral Einstein obstruction: mathematical position and comparison

This note locates the integral rigidity result within the existing curvature
theory. Full hypotheses and proofs remain in the
[integral rigidity paper](../research/20260921_rigidity.tex), especially
`prop:optimization`, `thm:core`, `eq:general-gap` and `cor:blowups`.

## Two different functionals

Let $X$ be a closed minimal complex surface of general type,
$A=c_1^2(X)>0$, and $M=X\#k\overline{\mathbb{CP}}^2$.
LeBrun's Theorem 4.3 computes the absolute Ricci-energy infimum

$$I_r(M)=\inf_g\int_M|\operatorname{Ric}_g|_g^2\,d\mu_g
       =8\pi^2(A+k).$$

His paper also proves sharp scalar/Weyl estimates, Einstein nonexistence
results and minimal-volume statements. Corollary 3.4 gives the classical
$k\ge A/3$ blow-up obstruction. Its contribution is not limited to examining
exact Einstein metrics. See [LeBrun, *Ricci Curvature, Minimal Volumes, and
Seiberg–Witten Theory*, Inventiones Mathematicae 145 (2001), 279–316](https://arxiv.org/pdf/math/0003068).

The current manuscript instead studies, for each metric,

$$\mathcal E(g)=\inf_{\lambda\ne0}
\frac{\int_M|\operatorname{Ric}_g-\lambda g|_g^2\,d\mu_g}
{\lambda^2\operatorname{Vol}_g(M)}.$$

Write $V=\operatorname{Vol}_g(M)$, $R_2=\int|\operatorname{Ric}|^2$,
$S=\int s$, $\bar s=S/V$, and
$\operatorname{Ric}^{\circ}=\operatorname{Ric}-(s/4)g$. For $R_2>0$,

$$\mathcal E(g)=4-\frac{S^2}{VR_2}
=\frac{4\int|\operatorname{Ric}^{\circ}|^2+
             \int(s-\bar s)^2}{R_2}.$$

Indeed, with $t=1/\lambda$, the minimized expression is
$(R_2/V)t^2-2(S/V)t+4$. If $S\ne0$, its minimum occurs at
$\lambda=R_2/S$. If $S=0<R_2$, the infimum is $4$ and is approached as
$|\lambda|\to\infty$. If $\operatorname{Ric}=0$, the original definition
also gives $4$; the quotient involving $R_2$ is then undefined.

Both functionals are scale-invariant in dimension four. The distinction is
not scale invariance: $I_r$ measures the least total Ricci energy on a smooth
manifold, while $\mathcal E$ measures a metric's relative deviation from a
nonzero constant-Einstein equation. A positive lower bound for $R_2$ alone
does not force a positive lower bound for the numerator in the last quotient.
For example, a non-Ricci-flat Einstein metric has $R_2>0$ and
$\mathcal E=0$. This explains why the two conclusions are different; it is
not, by itself, a proof of bibliographic novelty.

## What the integral gap adds in its stated family

Under the manuscript's blow-up hypotheses, including $b_+(X)>1$, put
$d=(1/3-k/A)_+$. Its conclusion is

$$\mathcal E(g)+d\ge c_*>0,$$

uniformly in $X,k,g$, without diameter, noncollapse, Sobolev or full-curvature
bounds. This controls approximate inputs, not merely exact solutions.
When $d\le c_*/2$, every metric satisfies $\mathcal E(g)\ge c_*/2$.
Since $\mathcal E(g)\le4\delta_\sigma(g)^2$, both normalized pointwise
defects are at least $\sqrt{c_*/8}$ in that band.

For a non-Ricci-flat Einstein metric, $\mathcal E=0$, so $d\ge c_*$.
Ricci-flat metrics are excluded separately by the actual-monopole scalar
inequality and positive self-dual projection. Thus the exact topological
obstruction follows as a specialization of the stronger integral statement;
a closed nonexistence band can use width $c_*/2$ to avoid endpoint ambiguity.

The appropriate description is **a quantitative integral strengthening of
the LeBrun–Seiberg–Witten Einstein obstruction in the stated families**.
The restriction $b_+(X)>1$ here is important: the cited classical
Theorem 4.3 and Corollary 3.4 do not require that restriction. Moreover,
the current paper's positive-normalization estimate uses classical
inequalities; the new analytic mechanism addresses the negative-normalization
near-equality problem before the two signs are combined.
Here “stability” means persistence of an obstruction under small normalized
Ricci error. It does not mean that an approximate metric is close to an
Einstein metric, that a correction exists, or that Ricci flow converges.
The result does not subsume LeBrun's entire Ricci-energy or minimal-volume
theory, and its abstract form still requires actual monopole solutions and
control of their class-square cost.

## Development of the proof and the next mathematical questions

The [earlier exact-gap argument](../research/20260916_uniform_gap.tex) passes
from topological near-equality to a controlled local Einstein development
and a forbidden Weyl spectrum. It relies on exact-Einstein regularity.

The [twelve-round development](rounds/SYNTHESIS.md) changes the mechanism.
Small Ricci error cannot simply be differentiated, and first-order weak
control did not justify a divergence self-test. Bounded weighted monopoles,
scalar clipping and second-order covariant estimates supply that missing
control on the original metric. A smooth polynomial Weyl model then permits
integration by parts in the weak Bianchi identity. The resulting two limits
for its divergence energy are incompatible. This is the analytic connection
between the classical curvature input and the current integral gap, not an
assumption of uniform geometric compactness.

The useful extension questions are correspondingly precise: can actual
classes be selected with a smaller negative-square cost; can another
realizable calibration model admit a source-aware or boundary self-test;
can a different solvable gauge system supply the required bounded field?
Positive branches, higher dimensions and non-monopole obstructions remain
open alternatives. For the specified closed shear examples, the ratio
$(2\chi+3\tau)/\alpha^2=1$ does not enter the critical $2/3$ band; their
approximate metrics cannot be paired with another topology's obstruction
to manufacture a counterexample.

## Literature comparison and communication

[LeBrun's *An Overview of Einstein 4-Manifolds* (2026)](https://arxiv.org/abs/2609.03033)
is a current entry to the literature, alongside the sources cited in the
integral paper. A theorem-level comparison should match the smooth category,
actual class assumptions, norm, normalization, constants and treatment of
degeneration. The comparison above checks the named classical results;
it does not establish that no equivalent theorem exists elsewhere.

Use the precise gap and proof mechanism to explain the contribution. A
metaphorical “error barrier” means a positive lower bound in this Riemannian
metric family and norm, not a physical barrier or a statement about Lorentzian
geometry. Surgery changes the smooth object and requires a new check of both
the monopole hypotheses and the input construction. Journal predictions and
claims such as “the field made no progress for 25 years” supply no mathematical
premise and are not conclusions of this comparison.

## Source supplement

The supplied [Skill3 coverage review](skill3-coverage-audit-20260921.md) is
retained verbatim as an external review, not as an additional proof. Its
positioning recommendations are addressed above.

The review names a second three-manuscript set: *从统一间隙到更广Einstein判定*,
*跨尺度匹配与新闭拓扑*, and *同一光滑流形与原题闭合*. Those originals were not
present in the reviewed server locations. The ZIP in the Downloads directory
is byte-identical to the earlier uploaded ZIP, whose three sources are already
preserved in [the source archive](next-stage-sources.zip). The review reports
substantial content overlap, but that is not a substitute for comparing the
missing originals. Their individual coverage remains unverified; no missing
manuscript has been reconstructed from its title.
