# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 61,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step61_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step61_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Research goal: a lower bound for α(M)=inf_g ∫|Ric°|² on M=X#kCP̄² (X minimal general type, A=c1²(X)) in the open range 0<k<A/3. Equivalently, the inequality C₊(g)=(1/2π²)∫|W⁺|²+(1/96π²)∫s² ≥ A−(1−c)k for some c>0, or a k²/A-type law, or a construction showing P/k→0. The files record what is known. Proved: LeBrun's monopole bound gives only C₊≥2A/3. The fixed-complex Kähler infimum is exactly 8π²k. A certified non-Kähler cell has P/8π² ≈ 0.99566 per blow-up. The new local laws (Theorem 59.R/Φ, Theorem 61.EH) show that the tensor R⁺=W⁺+s/12 governs both Burns (CP̄²-bubble, positive mass) and Eguchi–Hanson insertion costs: first order through the kernel, second order through the splitting of the complementary eigenvalues. Theorem Y/K give necessary Yamabe/Weyl-departure conditions. The Anderson ledger gives conditional minimizer structure, with collapse and (N0) gates open. Task: propose the two or three most promising genuinely new mechanisms that could yield a GLOBAL lower bound P≥c·k·f(k/A) for all metrics in the open range, or a decisive construction with P/k→0. Each must accommodate the certified sub-unit cell and the formal common mode P≈2π²k²/A. Possible ingredients include: a global identity combining the monopole Weitzenböck formula with the local R⁺-response law (e.g. a 'response-weighted' SW estimate); a Yamabe-excess obstruction; using that near-minimizers must have R⁺≤0 with |T|² controlled at bubble points to feed back into the C₊ integral; and the collapse gate. For each mechanism give the precise inequality to aim for and its quantifiers, the first decisive calculation or counterexample test, and the exact place where previous attempts failed (from the files) that it circumvents. Do not propose additive universal surgery tariffs or Weyl-only arguments, which are known to fail.

## Integrated Scientific Memo

## Scientific memo: three global mechanisms worth testing

The common unknown is a **collective response to exceptional topology**, not a local blow-up price. The supplied results already rule out a unit surgery tariff, while Ricci-flat ALE insertions show that some topological changes can occur at arbitrarily small \(P\).

Use the dimensionless variables
\[
p=\frac{P}{8\pi ^2},\qquad
d=A-C_+=k-p.
\]
Indeed,
\[
C_+=\frac1{2\pi ^2}\int |R^+|^2,\qquad
|R^+|^2=|W^+|^2+\frac{s^2}{48},
\]
and Chern–Weil gives \(p=C_+-A+k\).

A particularly informative conjectural target is
\[
\boxed{d_+^2\le BAp.}\tag{G}
\]
For every smooth metric on every \(X\#k\overline{\mathbb{CP}}^2\) in the stated range, this would imply
\[
p\ge
\left(\sqrt{\frac{BA}{4}+k}-\sqrt{\frac{BA}{4}}\right)^2
=\frac{k^2}{BA}+O\!\left(\frac{k^3}{A^2}\right).
\]
The candidate \(B=4\) matches the formal common mode
\[
P\sim 2\pi ^2\frac{k^2}{A}.
\]
It also permits the certified sub-unit cell: \(p/k\simeq0.9956627\) means \(d/k\simeq0.0043373\), far from the collective regime \(d\simeq k\).

The following three mechanisms give distinct ways to establish—or decisively refute—(G).

---

## 1. Preserve the blow-up hypercube in a Ricci-response identity

### Information discarded by the existing monopole bound

Let \(K\) denote the pullback of the canonical class and \(E_j\) the total-transform exceptional classes. Wherever the required metric-independent monopole statement holds for the entire sign family, use
\[
a_\varepsilon=K+\sum_{j=1}^k\varepsilon_jE_j,
\qquad \varepsilon_j=\pm1.
\]
The cohomological identity
\[
\begin{aligned}
\mathfrak D_g
&=2^{-k}\sum_\varepsilon
   \big((a_\varepsilon^+)^2-a_\varepsilon^2\big)\\
&=(K^+)^2-A+\sum_j|E_j^+|^2+k\\
&=|K^-|^2+\sum_j|E_j^+|^2+k
\ge k
\end{aligned}\tag{1.1}
\]
is exact. Thus the full sign family retains an anti-self-dual defect of at least \(k\), even when the usual convex-hull estimate retains only the canonical square \(A\).

This does **not** yet imply an Einstein gap. The missing step is to turn this retained defect into a response paired with \({\rm Ric}^\circ\), rather than another estimate involving only scalar or Weyl norms.

### Precise inequality to seek

A useful realization of (G), with \(B=4\), would be a symmetric trace-free tensor \(\mathbb T_g\), constructed from the monopole family, such that for every admissible \(g\) with \(d>0\),
\[
4\pi ^2d
\le \left|\int\langle{\rm Ric}^\circ,\mathbb T_g\rangle\right|,
\qquad
\|\mathbb T_g\|_2^2\le8\pi ^2A. \tag{1.2}
\]
Cauchy–Schwarz gives exactly \(d^2\le4Ap\).

The stronger branch proposal
\[
\left(4\pi ^2\mathfrak D_g-\frac12P\right)_+
\le|\langle{\rm Ric}^\circ,\mathbb T_g\rangle|
\tag{1.3}
\]
would suffice because \(\mathfrak D_g\ge k\), but it is substantially stronger than needed. In particular, \(\mathfrak D_g\) also contains metric-dependent period energy. The first derivation should determine whether that energy cancels, has a favorable sign, or makes (1.3) untenable.

An initial universal bound
\[
\|\mathbb T_g\|_2^2\le C\pi ^2A
\]
is already scientifically decisive; the sharp constant need not be assumed.

### First decisive calculation

Carry out the metric variation of the monopole Weitzenböck completion **on shell**, retaining divergences and then averaging over signs. Candidate tensor terms include
\[
(F_A^+\circ F_A^-)^\circ,\qquad
\operatorname{Re}\langle\nabla_i\Phi,\nabla_j\Phi\rangle^\circ,
\qquad
(\nabla^2|\Phi|^2)^\circ.
\]
But their presence is not automatic: the first variation of a completed-square functional can vanish on a solution. The decisive question is whether a nonzero cohomological-response term survives after all on-shell cancellations.

The calculation should produce one of two concrete outcomes:

* an identity
  \[
  4\pi ^2d
  =\int\langle{\rm Ric}^\circ,\mathbb T_g\rangle-\mathcal Q_g,
  \qquad \mathcal Q_g\ge0,
  \tag{1.4}
  \]
  followed by an \(L^2\) bound on \(\mathbb T_g\); or
* a surviving term involving uncontrolled spinor gradients, inverse-spinor weights, or period energy that prevents that bound.

The local normalization test is the **boundary flux**, not an assumed identification of the SW stress with the \(P\)-stress:
\[
\delta_{\rm Burns}P=-8\pi ^2\varepsilon R^+(\zeta,\zeta)+\cdots.
\]
On an Einstein kernel direction, the next response must be consistent with
\[
-4\pi ^2|T|^2\varepsilon^2\log(1/\varepsilon),
\]
where \(T\) is the trace-free complementary \(2\times2\) block. Matching this flux would establish a genuine bridge between monopoles and the local insertion law. Failure to match it would reject this particular stress construction, not the global gap conjecture.

A Kähler blow-up degeneration provides a second calibration: \(p\to k\), hence \(d\to0\). The resulting estimate must become weak there, rather than reconstruct a forbidden unit tariff.

### What this circumvents—and what it does not assume

The ledger’s \(C_+\ge2A/3\) loses the exceptional information before a Ricci-response estimate is available. Equation (1.1) preserves that information; (1.4) identifies the exact new analytic object required to use it.

The whole hypercube must be justified with the appropriate SW hypotheses. The supplied material does not establish a blanket metric-independent hypercube statement for every minimal general-type surface, especially in chamber-dependent cases. An all-metrics theorem cannot silently inherit the \(b^+\ge3\) scope of other results.

---

## 2. A Yamabe susceptibility estimate, with a collective capacity interpretation

This route separates two questions:

1. how much scalar departure is required to lower \(C_+\) below \(A\);
2. whether that scalar departure can occur with arbitrarily small \(P\).

The first is a monopole-curvature question. The second is the new global susceptibility problem.

### Conformal reduction

In a negative conformal class, the Yamabe representative minimizes \(\int s^2\), while \(\int|W^+|^2\) is conformally invariant. Consequently it also minimizes \(P\) in that class, by the exact Chern–Weil identity.

For unit-volume Yamabe representatives, set
\[
x=\sqrt{\frac{\int s^2}{32\pi ^2A}},
\qquad
y=\sqrt{\frac{\int|W^+|^2}{(4/3)\pi ^2A}}.
\]
The scalar monopole estimate recorded in the ledger gives \(x\ge1\), and
\[
\frac{C_+}{A}=\frac{x^2+2y^2}{3}. \tag{2.1}
\]
Equivalently,
\[
E_Y=\frac1{96\pi ^2}\int s^2-\frac A3
=\frac A3(x^2-1),
\]
\[
R_W=\frac{2A}{3}-\frac1{2\pi ^2}\int|W^+|^2,
\qquad d=R_W-E_Y. \tag{2.2}
\]
Thus a cheap configuration requires a **Weyl departure exceeding its Yamabe excess by approximately \(k\)**. Scalar excess alone is not an obstruction.

### Precise inequality to seek

A concrete susceptibility target is
\[
\boxed{\quad
p(g)\ge\gamma A(x(g)-1)^2
\quad}\tag{2.3}
\]
for every unit-volume Yamabe representative with \(C_+<A\), with a universal \(\gamma>0\).

The restriction \(C_+<A\) is important: it is precisely the unresolved regime, and avoids imposing an unnecessary global scalar estimate on metrics already satisfying \(p\ge k\).

To convert (2.3) into a gap, one needs a scalar–Weyl envelope. A sharply testable candidate is
\[
2x+y\ge3. \tag{2.4}
\]
Its normalization corresponds to the mixed monopole-curvature estimate
\[
\int(s-\sqrt6\,|W^+|)^2\ge72\pi ^2A
\]
on a negative constant-scalar representative, followed by
\(\int|W^+|\le\|W^+\|_2\). The latter mixed estimate is **not stated in the supplied files**, so (2.4) must be derived or supplied with its exact hypotheses; it should not be treated as an established input here.

If (2.4) holds, write \(t=x-1\). For \(0\le t\le1/2\),
\[
\frac dA
=1-\frac{x^2+2y^2}{3}
\le2t-3t^2\le2t.
\]
For \(t\ge1/2\), \(d/A\le1\le2t\), so in all cases
\[
d\le2A(x-1). \tag{2.5}
\]
Combining with (2.3),
\[
d^2\le\frac4\gamma Ap. \tag{2.6}
\]
Hence \(\gamma=1\) would give the formal sharp response constant \(B=4\).

This formulation accommodates the common mode rather than excluding it. When \(d\sim k\ll A\), it permits
\[
x-1\sim\frac{k}{2A},\qquad
E_Y\sim\frac k3,\qquad
p\sim\frac{k^2}{4A}.
\]
In particular, a proposed bound \(E_Y\lesssim p\) would be too strong for this common-mode scenario. The appropriate susceptibility is quadratic:
\[
p\gtrsim \frac{E_Y^2}{A}
\]
in the small-departure regime.

### First decisive calculation: scalar response of a balanced multi-cell family

For a KE bulk, insert kernel-direction Burns cells and solve the Yamabe equation for the resulting smooth metric:
\[
-6\Delta_g u+s_gu=s_Yu^3,\qquad \int u^4\,d\mu_g=1.
\]
Then evaluate both \(P(u^2g)\) and \(x(u^2g)\). The trace-free Ricci transformation makes the relevant energy explicit:
\[
{\rm Ric}_{u^2g}^{\circ}
=
\left({\rm Ric}_g
-2\nabla^2\log u
+2\,d\log u\otimes d\log u\right)^\circ.
\tag{2.7}
\]

The decisive coefficient is the rank-one term arising from the **sum of scalar sources**, not another single-cell logarithm. The calculation should determine whether
\[
p\ge\gamma A(x-1)^2
\]
holds to leading order, and whether the corresponding bulk response produces \(1/(4A)\).

There is a crucial correction to the second branch: Yamabe normalization does **not** add a compulsory positive cost to an arbitrary competitor. It lowers or preserves \(P\) in the conformal class. Therefore a “hidden conformal cost” is not a valid argument. What is needed is a lower bound for the energy of the normalized metric itself.

### Tensor capacity: a complementary representation of the same response

The local laws suggest a renormalized interaction matrix, but its source and sign must be derived, not guessed as
\(\delta_p(\zeta\otimes\zeta-I/3)\).

For selected noncollapsed near-minimizers, seek a decomposition
\[
p\ge\sum_j e_j+r^{T}G_Br-o(1),\qquad
e_j\ge0,\qquad
\sum_jr_j=d+o(1), \tag{2.8}
\]
and the capacity bound
\[
\mathbf1^{T}G_B^{-1}\mathbf1\le BA. \tag{2.9}
\]
Quadratic duality would then give
\[
r^{T}G_Br\ge\frac{(\sum_jr_j)^2}{BA}.
\]
This is a collective bound; neither \(e_j\) nor a diagonal matrix entry is required to equal a unit blow-up price.

The first concrete calculation is a **two-cell** matched expansion on a compact complex-hyperbolic quotient:

* obtain the sources from the exact Burns boundary flux;
* compute the cross-term after allowing bulk relaxation;
* distinguish the scalar response channel from pure scaling and gauge zero modes;
* extract the canonical rank-one channel and the remaining spectrum.

Pure constant rescaling has zero Einstein defect. Thus a “constant mode gives charge-squared/volume” argument is insufficient: one must identify a non-gauge response mode actually carrying the exceptional deficit.

There is also a sign issue. The optimized Burns logarithm is negative. A positive capacity matrix cannot be read directly from that logarithm; it requires a correct renormalization and accounting for bulk relaxation. If the two-cell Schur complement has an uncontrolled negative or null collective mode, the proposed lower-bound representation fails and instead supplies useful construction data.

### Where this bypasses previous failures

The ledger explicitly leaves balanced matching and batch-gluing interactions open. The susceptibility and capacity formulations isolate that missing object. They also turn Yamabe/Weyl necessary conditions into a proposed sufficient quantitative obstruction, without relying on Weyl alone.

The local rigidity input remains conditional and quantitative:
\[
R^+\le0,\qquad
|T|^2\lesssim |{\rm Ric}^\circ|^2
\]
on the kernel stratum when the Ricci residual has not been explicitly canceled. Pointwise restrictions at finitely many bubble points do not themselves control an integral; the response operator or capacity estimate must supply that connection. Moreover, \(\delta W^+=0\) cannot be assumed on a merely \(P\)-critical bulk.

---

## 3. An interface-response ledger that either prices absorption or realizes a zero-gap reservoir

This mechanism addresses the channels not covered by smooth-bulk susceptibility: orbifold absorption, finite-isotropy collapse, and cusp-domain complements.

### The essential correction: EH obstruction is not a positive gap

Theorem 61.EH gives, near a prescribed EH insertion,
\[
P=\pi ^2a^4|R^+\zeta|^2+o(a^4).
\]
Even if \(R^+\zeta\ne0\), this tends to zero as \(a\to0\). Likewise, a nonzero second obstruction only changes the rate.

Therefore:

* vanishing \(R^+\zeta\) or higher obstruction is **not necessary** for an \(\alpha=0\) construction;
* positivity of an EH obstruction cannot produce a scale-independent lower bound;
* computing the second EH obstruction is valuable for rates and Einstein existence, but is not the first decisive test for this global gap.

Once a compact Einstein orbifold has compatible Ricci-flat ALE replacements producing the required smooth manifold, corrected Proposition 59.N already gives \(\alpha=0\). The decisive issue is **global topology and Einstein-core realization**.

Nor does 61.EH remove \((N_0)\): it estimates perturbations of a known Ricci-flat EH bubble, not arbitrary non-Ricci-flat orbifold bubbles. Its extension from weighted neighborhoods to arbitrary near-minimizers is explicitly open.

### Precise interface inequality to seek

Cut a selected minimizing sequence into thick regions, ALE regions, and collapsed transition regions. First construct an exactly normalized ledger
\[
\mathscr C_i=C_+(g_i)+o(1).
\tag{3.1}
\]
When expressed in Euler/signature and spin\(^c\) data, this ledger contains the appropriate transgression and APS corrections.

The target is
\[
\boxed{\quad
(A-\mathscr C_i)_+^2
\le BA\,p(g_i)+o(1).
\quad}\tag{3.2}
\]
Its quantifier must include:

* nontrivial cone groups and non-Ricci-flat bubble channels;
* locally free collapse, including finite isotropy;
* graph-type interfaces and finite-volume Einstein domains;
* shrinking bad balls carrying nontrivial topology.

It is not legitimate simply to add an unspecified
\(\eta_{\rm sign}+\eta_{\rm Dirac}\) to the chiral curvature integral. The two APS formulas have different coefficients and depend on the boundary spin\(^c\) restriction. Exact normalization and gluing determine the combination.

### First decisive test: can the boundary data absorb an odd exceptional lattice?

For the interfaces already present in the sources—\(\mathbb{RP}^3\), spherical space forms, and Wahl lens spaces
\[
L(n^2,nm-1),
\]
compute:

1. the discriminant linking pairing and its characteristic quadratic refinement;
2. all relevant restrictions of \(K+\sum\varepsilon_jE_j\);
3. the correctly normalized signature and spin\(^c\)-Dirac boundary corrections;
4. the lattice obtained after gluing, including the finite-index enlargement.

The enlargement matters: the local EH bolt lattice has square \(-2\), not an odd exceptional generator. Odd global classes can arise only after the full gluing is accounted for. A model normalization test is the supplied \(S^4/\mathbb Z_2\) resolution to the two-\(\overline{\mathbb{CP}}^2\) manifold, up to the orientation convention. A second test is recovery of the recorded Wahl alternatives \(n\) odd or \(8\mid n\).

For collapse, free-circle spin arguments handle only the simplest region. Finite isotropy and interface gluing are precisely where an odd class might enter. The exact adiabatic correction must be computed there; an asserted three-dimensional Yang–Mills price is not yet an established consequence.

### Two scientifically decisive outcomes

**Residual response.** If the assembled characteristic data cannot absorb the exceptional charge freely, identify a residual \(q_i\) satisfying, for example,
\[
q_i\ge\theta\,d_i-o(1),\qquad
q_i^2\le C A p_i+o(1).
\tag{3.3}
\]
This supplies the missing interface/collapse version of (G). The second inequality is an analytic response estimate; APS arithmetic alone cannot prove it.

**A realizable reservoir.** If the interface calculation admits complete absorption, seek an actual Einstein core and compatible fillings with
\[
M\cong X\#k\overline{\mathbb{CP}}^2,\qquad
A>3k.
\tag{3.4}
\]
A verified compact Einstein orbifold with Ricci-flat ALE-tree replacements realizing (3.4) gives \(\alpha(M)=0\), regardless of EH obstruction coefficients. A complete finite-volume Einstein domain with explicitly bounded-curvature collapsing fillings gives the analogous cusp construction.

Intersection-form agreement and a characteristic vector are necessary but not sufficient. The construction must establish the smooth diffeomorphism type and the minimal general-type model \(X\). Complex canonical resolutions and the familiar Kähler orbifold mechanisms do not provide this nonminimal example; the supplied materials point instead to a genuinely non-Kähler core or a cusp/F-collapse complement.

For a varying family, (3.4) plus gluing errors \(P_\ell=o(k_\ell)\) would give the requested \(P_\ell/k_\ell\to0\). A single such manifold with \(\alpha=0\) would already refute any positive universal lower bound applying to it.

### Exact gates this addresses

The ledger leaves orbifold absorption at the threshold
\[
C_+(V)+\sum_jw(N_j)\ge A,
\]
which is essentially the unresolved global inequality itself. The interface calculation adds independent characteristic and spectral data rather than restating that threshold.

Likewise, \(\chi>0\) excludes a global bounded-curvature collapse with \({\rm MinVol}=0\), but it does **not** exclude Anderson’s total-collapse alternative with topology concentrated in shrinking bad balls. The third mechanism must include those balls. Partial-collapse constructions in corrected 59.D demonstrate why finite-volume Einstein cores with vanishing-volume transitions cannot be dismissed on energetic grounds.

---

## The precise new objects

The strongest advances supported by the supplied material are these three sharply specified missing objects:

1. **A nonvanishing on-shell monopole response identity** retaining the exceptional hypercube and pairing its residual with \({\rm Ric}^\circ\).
2. **A quadratic Yamabe susceptibility or positive collective capacity channel**, with the two-cell cross-term determining whether the formal \(1/(4A)\) coefficient is real.
3. **A normalized characteristic/interface response ledger**, capable of distinguishing priced exceptional charge from an actual zero-energy orbifold or cusp reservoir.

None is established by the present sources. Together they preserve the certified sub-unit construction, the formal \(k^2/A\) mode, and the genuine zero-gap escape channels. They also locate the decisive uncertainties more narrowly than another local expansion: whether the response identity survives on shell, whether its collective channel is coercive after bulk relaxation, and whether exceptional topology can be globally absorbed into a realizable Einstein degeneration.