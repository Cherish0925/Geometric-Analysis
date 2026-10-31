# TTCS Independent Branch Record

```json
{
  "step_id": 2,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step2_blowup_cell_problem_O11.md",
    "Sessions/S1003A02/workspace/scripts/u2_curvature.py",
    "Sessions/S1003A02/workspace/scripts/u2_xcoord.py",
    "Sessions/S1003A02/workspace/scripts/kahler_cell_exact.py",
    "Sessions/S1003A02/workspace/scripts/u2_cell_jax_log.py",
    "Sessions/S1003A02/workspace/data/u2grid/u2_cell_grid2.jsonl",
    "Sessions/S1003A02/workspace/figures/u2_cell_cost.png",
    "Skills/geometric-analysis/references/conventions-and-literature.md",
    "Skills/geometric-analysis/references/results-and-questions.md"
  ]
}
```

## Task

Check the mathematics and code behind the O11 blow-up cell computation for four-manifold Einstein gaps. (1) Verify the exact identity P - 8 pi^2 Q = (S - 32 pi^2 A)/12 + 4(W_+ - (4/3) pi^2 A) on X # k CP2bar # l(S^1xS^3) with Hilbert-Schmidt norms on two-forms (conventions file), and the cell identity P(U) = 8pi^2 + 4 Delta W_+ + Delta S/12 for a blown-up ball agreeing with complex hyperbolic metric near the boundary; check signs, orientation (complex orientation, E.E=-1) and that Burns gives exactly 8 pi^2. (2) Check the U(2) cohomogeneity-one curvature code: frame brackets, Koszul formula, curvature-operator sign, the identification of the complex orientation (the script's 'SD' block is anti-complex since FS gives W+=0 there), bolt regularity F'(x0)G'(x0)=1 for O(-1), smoothness/H^2 matching at X, and the Kahler exact optimum P/8pi^2 = 1 + 6x0 + 9x0^2(1+X^-2). (3) Check the claim that the linear coefficient 6x0 equals the Hodge-index Kahler bound (c1.omega)^2/omega^2 with epsilon = 3 x0 in Ric=-6g units. (4) Judge whether the numerical evidence (table in the note) really supports 'every U(2) cell has P > 8pi^2 and the slope tends to 6 also for non-Kahler cells', and identify any parametrization blind spot (e.g. phi=(1-u)^3 freezing near X, monotone b=sqrt(x), fixed outer CH region, degree 12) that could hide a cell with P < 8pi^2. (5) Assess the heuristic that the order-x0 coefficient is universal beyond U(2) because Burns is critical; state precisely what would have to be proved and whether log terms could enter. Give a direct scientific memo with any errors found and their consequences.

## Output

# Verification memo: the O11 blow-up cell computation (Step 2 note and U(2) scripts)

## Summary

- **Exact identities.** The global identity, the cell identity and Burns \(=8\pi^2\) are correct. The orientation handling in the code is correct, but the docstring of `u2_curvature.py` states the orientation the wrong way round.
- **Kähler cells.** The exact Kähler optimum \(1+6x_0+9x_0^2(1+X^{-2})\) is correct; I re-derived it. The coefficient 6 is a theorem for Kähler cells with no symmetry, by relative Chern–Weil plus Cauchy–Schwarz.
- **Numerics.** The data support slope \(\to6\) within U(2). They also show a resolvable \(x_0^2\log(1/x_0)\) saving.
- **The main gap.** Every U(2) metric is Hermitian for a complex structure that agrees with \(J_{\rm CH}\). The family therefore cannot see a Burns bubble whose complex structure is rotated relative to \(J_{\rm CH}\). The U(2)-invariance argument for universality in §4 of the note does not cover this modulus.

## 1. The global and cell identities

**Global identity.** From \(4\pi^2T_+=S/24+2W_+-P/2\) one gets \(P=S/12+4W_+-8\pi^2T_+\).

- \(T_+\) drops by 1 per \(\overline{\mathbb{CP}}^2\) summand (χ+1, τ−1).
- \(T_+\) drops by 4 per \(S^1\times S^3\) summand (χ−2, τ unchanged).
- Hence \(T_+(M)=A-Q\).

For a Kähler–Einstein metric, the operator-norm spectrum of \(W^+\) is \((s/6,-s/12,-s/12)\). So \(|W^+|^2=s^2/24\), and \(P=0\) forces \(S_{KE}=32\pi^2A\) and \(W_+^{KE}=\tfrac43\pi^2A\). Expanding the right-hand side of the boxed identity gives \(S/12+4W_+-8\pi^2A\), which equals the left-hand side. ✓

The following consequences are also correct:
- the "48× deficit" statement;
- \(\Phi\ge A-o(Q)\) as the equivalent form of coefficient 4;
- LeBrun's \(\Phi\ge\frac23A\).

I checked the relaxation directly. With \(a=\sqrt S\) and \(b=\sqrt{6W_+}\), the problem is to minimise \(a^2/12+2b^2/3\) subject to \(a+b\ge\sqrt{72\pi^2A}\).
- The optimum is at \(a=8b\), giving \(F=\tfrac{16}{3}\pi^2A\).
- The ratio there is \(|W^+|/|s|=1/(8\sqrt6)=\sqrt6/48\).
- The scalar constraint is inactive (\(S\approx56.9\pi^2A\)). ✓

For the \(S^1\times S^3\) summands, \(S\ge32\pi^2A\) rests on the corpus supply statements. It is not re-derived here.

**Cell identity.** The Gauss–Bonnet and signature transgression terms at \(\partial U\), and the η-term, depend only on \((F,F',G)\) at \(x=X\).
- These are matched.
- \(\Delta(2\chi+3\tau)=(2-3)-(1+0)\cdot\) [relative] \(=-1\) in the complex orientation, where \(E\cdot E=-1\).
- This gives \(P(U)=8\pi^2+4\Delta W_++\Delta S/12\). ✓

C¹ matching is sufficient. The optimum \(K_{\rm opt}\) matches CH only in \(H,H'\), so \(K''\) jumps at \(X\). The metric is then \(C^{1,1}\), \(P\) is finite, and the transgression terms are matched.

**Burns.** \(K=x-x_0\) gives \(L=2x_0\) and \(P=4\pi^2\int_{x_0}^\infty4x_0^2x^{-3}dx=8\pi^2\). ✓ Independently, for the ALE end, signature gives \(W_-=12\pi^2\) and Gauss–Bonnet then gives \(P=8\pi^2\).

**Redundancy in point 3 of §3.** With matched edge data, the signature formula gives \(W_-(U)=12\pi^2+\Delta W_+\) exactly. The data confirm this to all printed digits: \(x_0=3\cdot10^{-4}\) gives \(1+0.0023876/12=1.000199\). So "\(W_-(U)>12\pi^2\)" is the same fact as \(\Delta W_+>0\), not an independent observation.

**A literature anchor.** \(W_-(U)\ge12\pi^2\) is a relative analogue of Gursky's \(\int|W^\pm|^2\ge\frac{4\pi^2}{3}(2\chi\pm3\tau)\), which is attained by CP² Fubini–Study. Gursky's hypothesis of positive Yamabe constant does not hold here, so this is an analogy, not a derivation.

## 2. Curvature code

**Frame and connection.**
- **Brackets.** \([E_0,E_i]\), \([E_1,E_2]=(2a/b^2)E_3\), \([E_2,E_3]=(2/a)E_1\) and \([E_3,E_1]=(2/a)E_2\) all follow from \([X_i,X_j]=2\epsilon_{ijk}X_k\). ✓
- **Koszul formula.** \(\Gamma_{ijk}=\tfrac12(c_{ijk}-c_{jki}+c_{kij})\). ✓
- **Covariant derivative.** It differentiates only along \(E_0\), which is correct because the coefficients depend only on \(t\). ✓
- **Curvature and Ricci.** \(R=\nabla\nabla-\nabla\nabla-\nabla_{[\,,]}\) and \(\mathrm{Ric}_{jk}=\sum_i\langle R(E_i,E_j)E_k,E_i\rangle\). ✓

**Curvature operator.** \(-\tfrac14\sum R_{ijkl}F^{ij}H^{kl}\) gives \(+K\) on unit 2-forms, so the round sphere is positive. Also:
- \(\operatorname{tr}\) on \(\Lambda^\pm\) is \(s/4\), so \(W^\pm=A_\pm-s/12\).
- The Hilbert–Schmidt sum matches the manuscript convention. ✓

**Orientation.**
- With \(d\sigma_3=-2\sigma_1\wedge\sigma_2\), one has \(\tfrac12d(b^2\sigma_3)=(bb'/a)e^{03}-e^{12}\).
- So under \(a=bb'\) the Kähler form is \(e^{03}-e^{12}\). This form is anti-self-dual for \(e^0\wedge e^3\wedge e^1\wedge e^2\), which is \(+e^{0123}\).
- The complex orientation is therefore the opposite one, and the docstring of `u2_curvature.py` is wrong.
- The swap `wpsq_c = conv(U.wmsq)` in `u2_xcoord.py` is correct.
- The identity check confirms this. With the other orientation, \(\Delta(2\chi+3\tau)\) would be +5 and the check would be off by O(1), not \(10^{-10}\).

**x-coordinate and volume.** \(d/dt=2\sqrt G\,d/dx\); \(a''\) and \(b''\) need only \(F_2\) and \(G_1\). The volume density is \(dV=\pi^2x\sqrt{F/G}\,dx\). The ball reference values are correct: \(F_{\rm ball}=144\pi^2X^2/2\), \(S_{\rm ball}=288\pi^2X^2\) and \(W_+^{\rm ball}=12\pi^2X^2\). ✓

**Bolt regularity.** The \(X_3\)-orbits are great circles of length \(2\pi\), so smoothness needs \(a'(0)=1\), i.e. \(F'G'=1\).
- \(x-x_0\) is a smooth function of \(t^2\), so \(a\) is odd and \(b\) is even. No higher parity conditions arise.
- The bolt has area \(\pi x_0\), and its normal circle bundle is the Hopf fibration. In the complex orientation the bolt is the \(-1\) curve.
- The JAX bolt shift enforces \(p_1(0)+p_2(0)=0\) correctly through \(T_0\). ✓

**Exact Kähler optimum.** The kernel of \(L=x^2H''-2H\) is spanned by \(x^2\) and \(1/x\). With the four boundary values:
- \(c_2=2x_0+6\alpha x_0^2+2c_1x_0^3\);
- \(c_1\simeq-8(x_0+3x_0^2)/X^3\);
- \(\alpha-1\simeq3(x_0+3x_0^2)/X^2\).

Expanding \(\frac{P}{8\pi^2}=\tfrac12[c_1^2(X^4-x_0^4)/4+2c_1c_2(X-x_0)+c_2^2(\tfrac1{2x_0^2}-\tfrac1{2X^2})]\), the \(x_0^2/X^2\) terms are \(18-1+8-16=9\). This gives \(1+6x_0+9x_0^2(1+X^{-2})+O(x_0^3)\), matching `P_kahler` (for example 1.0180818 at \(x_0=0.003\), \(X=10\)). ✓

## 3. Hodge index and a non-symmetric Kähler cell bound

In Ric \(=-6g\) units, \([\omega]=-\mu c_1\) with \(\mu=\pi/3\), and \(\varepsilon=\mathrm{Area}(E)/\mu=3x_0\).
- \(32\pi^2(c_1\cdot\omega)^2/\omega^2=32\pi^2[(A+ke)^2/(A-ke^2)]\) with \(e=3x_0\).
- With \(P=S/4-8\pi^2(A-k)\) for Kähler metrics, this gives \(P/8\pi^2\ge k(1+6x_0+9x_0^2)+O(k^2x_0^2/A)\).

So the per-site **second-order** term 9 also matches the cell optimum as \(X\to\infty\). The scale-invariant form \(1+|\lambda|\mathrm{Area}(E)/\pi\) is correct. Two qualifications:

- The note assumes classes proportional to \(\pi^*c_1\). Other directions of \(\omega_X\) only increase \((c_1\cdot\omega)^2/\omega^2\).
- Globally, LeBrun's \(S\ge32\pi^2A\) together with \(|W^+|^2=s^2/24\) already gives \(P\ge8\pi^2k\) for every Kähler metric.

**A stronger local statement without symmetry.** For any Kähler cell whose complex structure agrees with \(J_{\rm CH}\) near \(\partial U\):

- 4ΔW₊ = ΔS/6, so \(P(U)-8\pi^2=\Delta S/4\).
- Relative Chern–Weil gives \(\int_Us-\int_Bs=-4\pi\,\mathrm{Area}(E)=-4\pi^2x_0\). This is checked in U(2): \(\pi^2[8x-4(xK)']\) gives \(-12\pi^2X^2-4\pi^2x_0\) against \(-12\pi^2X^2\).
- The volume change is \(V_U=V_B-\pi^2x_0^2/2\).
- Cauchy–Schwarz then gives
\[
\frac{P(U)}{8\pi^2}\ge1+\frac{1}{16}\Big[\frac{(12X^2+4x_0)^2}{X^2-x_0^2}-144X^2\Big]=1+6x_0+9x_0^2+\frac{x_0^2}{X^2}+O(x_0^3).
\]

This lies below the U(2) optimum only in the \(X^{-2}\) term, so the coefficient 6 is a symmetry-free Kähler theorem.

The global Kähler infimum in a fixed class is the constant-scalar-curvature value. Arezzo–Pacard blow-up theorems should realise it; the citation should be confirmed. That would make the Kähler side of O11 closed: cost \(8\pi^2(1+6x_0+\dots)\) per site, approached only as the areas tend to zero.

## 4. What the U(2) numerics support

**Supported.**
- 1+6x₀ is the leading behaviour for U(2) cells.
- The minimum over \(x_0\) of the cell cost occurs as \(x_0\to0\).
- The data are independent of \(X\).

The improvement over Kähler is second order, but it is a logarithmic second order, as the three converged small-\(x_0\) runs at \(X=10\) show:

| \(x_0\) | \((P_K-P_{nK})/(8\pi^2x_0^2)\) | \((6-\kappa)/x_0\) |
|---|---|---|
| 3e-4 | 73.2 | 64.2 |
| 3e-3 | 50.5 | 41.5 |
| 3e-2 | 27.4 | 18.3 |

These fit \(\kappa\approx6-9.9\,x_0\log(1/x_0)+15.9\,x_0\) to about 2.5% at the third point. A power law fits much worse. So the U(2) cost is
\[
P/8\pi^2\approx1+6x_0-c\,x_0^2\log(1/x_0)+O(x_0^2),\qquad c\approx10.
\]
The exact Kähler formula has no logarithm, so the log comes from the non-Kähler relaxation. A degree sweep (12 vs 16 vs 20) on these three points would show whether \(c\) is resolved.

**Corrections to the note's numbers.**
- At \(x_0=3\cdot10^{-4}\) the non-Kähler gain is \(0.022x_0\) relative to Kähler (\(0.019x_0\) relative to \(6x_0\)), not \(0.06x_0\).
- The "0.5x₀" at 0.03 is measured against \(6x_0\); against Kähler it is \(0.82x_0\).

**Convergence.** Many runs stopped on the function-evaluation cap. SciPy's default `maxfun` = 15000 binds before `maxiter` = 20000. The table rows \(x_0=3\) and \(x_0=10\) (X=50) are unconverged, and so are several X=2 and X=10 rows. They remain valid upper bounds for the U(2) infimum.

**"Every U(2) cell has P > 8π²" is not shown.** Minima over a parametrised family are upper bounds on the infimum. A lower bound needs an argument.

**Blind spots, in decreasing importance.**

**(a) A structural restriction.** The U(2) ansatz imposes more than radial symmetry:
- The isotropy U(1) forces \(J E_0=\pm E_3\) and \(JE_1=\pm E_2\).
- The (1,0)-forms are \(dt+ia\sigma_3\) and \(\sigma_1\mp i\sigma_2\).
- \(d(\sigma_1\mp i\sigma_2)=\pm2i\,\sigma_3\wedge(\sigma_1\mp i\sigma_2)\), and \(d(dt+ia\sigma_3)=ia'dt\wedge\sigma_3-2ia\,\sigma_1\wedge\sigma_2\) is of type (1,1).
- So both \(J_\pm\) are integrable for **every** \((a,b)\). Every metric in the family is Hermitian in both orientations.
- The isotropy forces \(W^\pm\) to have spectrum \((2\mu,-\mu,-\mu)\), so \(|W^+|^2=\kappa_+^2/24\), where \(\kappa_+\) is the Hermitian conformal scalar curvature.

This explains why the data split exactly as in the Kähler case (\(4\Delta W_+\approx4x_0\), \(\Delta S/12\approx2x_0\)).

It also suggests a proof route for U(2) cells. Use a relative Chern–Weil identity for \(\int\kappa\) in the Gauduchon gauge, in place of \(\int s=4\pi c_1\cdot[\omega]\). The Lee-form relation between \(\kappa\) and \(s\) and the edge terms still need to be worked out.

The same structure is the blind spot. The family contains only competitors whose complex structure extends \(J_{\rm CH}\). It excludes a bubble whose \(J_B\) is rotated relative to \(J_{\rm CH}\); see §5.

**(b) Local optimiser started from the Kähler optimum.** The functional is non-convex, and other U(2) basins are not explored.

**(c) Monotone b.** Writing \(x=b^2\) excludes necks. Such configurations are plausibly costlier, but this is not tested.

**(d) The factor \(\phi=(1-u)^3\).** It freezes roughly the outer e-fold (\(\phi<10^{-3}\) for \(u>0.9\)). This is harmless given the observed independence of \(X\).

**(e) Degree 12.** Adequate for 1+6x₀. The log coefficient \(c\) is what is sensitive to it.

## 5. Universality beyond U(2)

### The modulus the note's argument misses

The ALE cell identity shows that Burns minimises \(P\) among decaying fillings of \(\mathrm{Bl}_0\mathbb C^2\), with value \(8\pi^2\). The minimisers include Burns with **any** complex structure \(J_B\) in the twistor sphere \(S^2\subset\Lambda^+_p\).

Once the bubble is glued into CH, the relative position of \(J_B\) is a genuine parameter. The isotropy \(U(2)_p\) of CH fixes \(\omega_{\rm CH}\) and acts on \(S^2\) by rotations about it. Invariance therefore makes the first-order coefficient a function \(\kappa(\cos^2\theta)\) of the angle θ between \(\omega_B\) and \(\omega_{\rm CH}\), not a constant.

If the order-\(x_0\) term is linear in the curvature at the site, the only invariants are \(s(p)\) and \(\langle W^+(p)\omega_B,\omega_B\rangle=\tfrac{s}{12}(3\cos^2\theta-1)\). The other two pieces drop out: \(\mathrm{Ric}^\circ\in\Lambda^+\otimes\Lambda^-\) and \(W^-\) would need a \(\Lambda^-\) datum, which \(\omega_B\) does not supply. So in that case
\[
\kappa(\theta)=a+b\,P_2(\cos\theta).
\]

The U(2) data fix only \(\kappa(0)=6\). Suppose, purely heuristically, that the aligned \(4\Delta W_+\approx4x_0\) were entirely the traceless pairing. Then \(\kappa(\pi/2)\) would be as low as 0. Curvature×tail terms can carry an isotropic part, so this is not derived. But the sign and size of \(b\) decide whether 6 is the first-order optimum.

A \(\theta\) with \(\kappa(\theta)<0\) would give cells with \(P(U)<8\pi^2\) and hence \(\limsup\alpha/h<4\). The corpus lower bound \(\alpha\ge ch\) does not exclude this.

### The computation that settles θ

All Burns bubbles with any \(J_B\), and CH itself, are invariant under \(SU(2)_L=SU(2)_-\). So the rotated competitors are cohomogeneity-one Bianchi IX metrics \(dt^2+g_{ij}(t)\sigma_i\sigma_j\).

- At θ = π/2 the metric is diagonal and triaxial.
  - Near the bolt: \(a_1\to0\) with \(a_1'=1\), and \(a_2=a_3\).
  - Outside the cell: \((\sinh t,\sinh t,\sinh t\cosh t)\).
- Intermediate θ requires off-diagonal \(g_{13}\).

`u2_curvature.py` is generic frame-bracket code and extends directly to this ansatz. Within this family, \(\kappa(\theta)\) is an ODE-level computation.

### What a universality theorem needs

Let \(g_{\varepsilon,\theta}\) be the gluing of the \(\varepsilon\)-scaled, θ-rotated Burns bubble into CH, with \(\varepsilon^2=x_0\). The following three pieces would give \(P\ge8\pi^2(1+\kappa_{\min}x_0)-Cx_0^2\log(1/x_0)\) for all metrics within \(\eta\) of \(\{g_{\varepsilon,\theta}\}\) in a weighted \(C^{2,\alpha}_\delta\) norm, with no symmetry assumed.

- **(i) Nondegeneracy.** The Hessian of \(4W_++S/12\) at Burns, on weighted decaying 2-tensors modulo diffeomorphisms, has kernel equal to the scalar-flat ASD deformations. This is plausibly only scaling and rotations, since the conformal compactification is the rigid \(\overline{\mathbb{CP}}^2\); this needs proof.
- **(ii) The order-x₀ term.** It is \(\kappa(\theta)x_0\), given as the pairing of the Burns \(r^{-2}\) tail with the regular part of the solution of the linearised outer Euler–Lagrange problem on CH. The independence of \(X\) in the data shows the term is set below the cell scale. The Kähler value comes from the bolt shift \(c_2=2x_0+6\alpha x_0^2\).
- **(iii) Lyapunov–Schmidt reduction.** Competitors near the stratum cannot beat \(\min_\theta\) at order \(x_0\). The intrinsic scale should be defined by the minimal area in the class \(E\) or by the tail coefficient, since \(x_0\) is a U(2) quantity.

### Log terms

**No log at order \(x_0\).** A term \(x_0\log(1/x_0)\) needs a density \(\sim x_0R\,r^{-4}\), i.e. a cross term between the Burns curvature tail (\(x_0r^{-4}\)) and the background curvature. These all vanish:
- Burns has \(s=W^+=0\) identically.
- CH has \(\mathrm{Ric}^\circ=0\) and \(W^-=0\).
- The \(S^3\)-averages of the tail's \(\mathrm{Ric}^\circ\) and \(W^-\) are \(SU(2)_-\)-invariant elements of irreducible representations, hence zero. This holds for any Einstein background.

Deviations \(\delta\) of the bubble from Burns enter as \(\delta\,x_0\log(1/x_0)\) against an \(O(\delta^2)\) cost, so they only reach order \(x_0^2\log^2(1/x_0)\).

**Log at order \(x_0^2\).** Terms \(x_0^2R^2r^{-1}\) integrate to \(x_0^2\log(1/x_0)\). The numerical fit (\(c\approx10\)) is evidence that this term is present.

## 6. Corrections to carry into the note and code

1. **Docstring of `u2_curvature.py`.** \(e^0\wedge e^3\wedge e^1\wedge e^2\) is the anti-complex orientation. The swap in `u2_xcoord.py` is correct and confirmed by the identity check.
2. **\(W_-(U)>12\pi^2\).** It equals \(\Delta W_+>0\) via the signature formula, so it is not separate evidence.
3. **The "0.06x₀" figure.** It should read \(0.022x_0\) relative to Kähler. The non-Kähler gain is better stated as \(\approx10x_0^2\log(1/x_0)\).
4. **Unconverged runs.** Runs stopped on the evaluation cap should be marked in the table.
5. **"Every U(2) cell has P > 8π²".** For Kähler cells this is a theorem (§3, no symmetry needed). For non-Kähler U(2) cells it is a numerical upper-bound observation. A proof could come from the Hermitian structure of all U(2) metrics.
6. **The universality heuristic.** U(2)-invariance does not make the first-order pairing constant, because of the \(J_B\)-orientation modulus. The SU(2)-invariant Bianchi IX family is the smallest class that contains it.
7. **Figure.** The right panel cannot show the log structure. Plotting \((6-\kappa)/x_0\) against \(\log(1/x_0)\) would make the \(x_0^2\log\) term visible as a straight line.