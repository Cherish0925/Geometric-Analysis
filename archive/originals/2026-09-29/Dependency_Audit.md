# Dependency audit: what actually prevents closure of O10 and O11

2026-09-30 (Asia/Shanghai). This is an independent targeted audit, not a re-certification of the entire integrated manuscript.

## Materials actually read

- `upload/O10_Quantitative_Escape_and_O11_Boundary(1).md`, complete, especially Sections 1–6.
- `outputs/Line1_Continuation_20260929D/O10_Alternative_Global.md`, complete.
- D's `inherited/Strong_Current_Prerequisite.md` and `inherited/Direct_Resolvent_Prerequisite.md`, complete.
- Original integrated manuscript, Sections `single-parameter`, `endpoint-covariance`, the complete first-torsion projection in `zero-end-geometry`, and the phase-curvature discussion.
- B's bounded upper-amplitude cutoff and resolvent construction.

## 1. The weighted Hessian estimate does not introduce the missing Weyl bound

The important question is whether the strong-current prerequisite has covertly used a bound for the opposite Weyl curvature. Its displayed derivative-interchange proof does not.

For a bounded bundle section let
\[
P_i=\nabla_i u,\qquad H_{ij}=\nabla_iP_j,\qquad q=|P|^2.
\]
The exact identity is
\[
\int w|H|^2
=\int w\operatorname{Re}\langle H_{ij},H_{ji}\rangle
 +\tfrac12\int w\sum_{ij}|F_{ij}u|^2.
\]
In the mixed term integrate the derivative with index \(j\). The commutator is then
\[
\sum_j[\nabla_j,\nabla_i]P_j
=F*P+\operatorname{Ric}*P.
\]
The Riemann tensor contracts in its covector index to Ricci. There is no uncontracted Weyl tensor here and no differentiated bundle curvature. For \(Lu=f(|u|^2)u\), the remaining differentiated trace is bounded by \(C|P|\). The slow weight satisfies
\[
|dw|\sqrt q\le 2\epsilon w|H|,
\]
so its derivative costs a small multiple of \(\int w|H|^2\).

For the positive spinor, the relevant full bundle curvature is the curvature of \(S^+\): its trace-free block contains \(W^+\), scalar curvature and the Ricci off-diagonal block, while its central block is the determinant curvature. It does not contain \(W^-\). The bounded model for its ASD determinant part therefore gives exactly the required bounded-model-plus-small-error hypothesis.

Nor is that bounded model obtained by circular use of the *strong* weighted estimate. The original single-parameter proof first obtains an **unweighted** Hessian budget from the coarse determinant-curvature \(L^2\) budget. The class-square condition supplies this coarse bound: \(a^2\ge T_+\), together with Chern–Weil and small \(P/V\), controls \((-a^2)_+/V\). The weighted determinant fit is then derived from this coarse budget; only afterwards is the new slow-gradient estimate applied.

The actual dependency is thus
\[
\text{class-square/coarse curvature budget}
\Rightarrow\text{unweighted Hessian budget}
\Rightarrow\text{bounded determinant fit}
\Rightarrow\text{strong gradient tails}.
\]
It is not a cycle. This targeted audit found no missing \(W^-\) hypothesis at this point.

## 2. The quantitative logarithmic line-bundle lemma survives the growing energy

In the new attachment's Section 1, put \(E=1+\fint|\nabla s|^2\), \(L_\Delta=\log(1/\Delta)\). The spectral averaging selects
\[
\Delta^{1/2}\le\varepsilon\le\Delta^{1/4},\qquad
\varepsilon K(\varepsilon)\le 4E/L_\Delta.
\]
The critical transgression term is bounded by
\[
\sqrt{\varepsilon E(K+1)}
\le 2E/\sqrt{L_\Delta}+\sqrt E\,\Delta^{1/8}.
\]
The curvature-error term satisfies
\[
\sqrt{\Delta(K+1)}
\le 2\sqrt E\,\Delta^{1/4}/\sqrt{L_\Delta}+\sqrt\Delta.
\]
Since \(E\ge1\), all the remaining exponentially small terms are bounded by \(CE/\sqrt{L_\Delta}\). The claim does not need \(\varepsilon E\to0\); the low-amplitude volume estimate remains true when its right side exceeds one. The curvature and Ricci constants in the Hessian estimate are independent of \(E\), as stated.

Consequently this audit finds the displayed line-bundle estimate
\[
|c_1(K)^2[M]|/V\le CE/\sqrt{\log(1/\Delta)}
\]
valid under its stated hypotheses. It is not the source of the current difficulty.

## 3. A more consequential use of the new power-rate bookkeeping

The new attachment's Section 5 pursues a rate from the original error
\(\eta_0=\kappa_\beta+\beta^{-2}\) to actual field errors. Its stated conservative exponent is
\[
\theta=\frac{\epsilon_0}{16(1+\epsilon_0)},\qquad
\gamma=\frac{\epsilon_0}{1+\epsilon_0}.
\]
The elementary exponents in Sections 5.1–5.3 are consistent with the displayed inputs. For example, optimizing \(L^2\eta_0+L^{-2\epsilon_0}\) gives \(\eta_0^\gamma\). Converting the \(L^1\) torsion-mass rate to \(L^2\) using the gradient tail gives \(\|m-m_*\|_2\le C\eta_0^{\gamma/8}\), as stated.

For the upper-amplitude cutoff, the torsion Lichnerowicz formula gives a tail-gradient squared bound of order \(\eta_0^{\gamma/4}\). The potential term on a fixed tail is controlled by \(C|m-m_*|^2\), not merely by the weaker global \(L^1\) mass error. The fixed cap and the coercive resolvent then give \(H^1\) error \(O(\eta_0^{\gamma/8})\).

The additional errors appearing in D's positive-potential theorem must be included before combining the results. A particular missing item in the new attachment's shorter list is \(\|v-\tau\|_4\). It follows without a Sobolev inequality. On a fixed upper-amplitude region, boundedness gives
\[
\int|v-\tau|^4\le C\int|v-\tau|^2.
\]
On its complement the torsion mass tail gives
\[
\int_{|\tau|>L}|\tau|^4\le C\int|\,|\tau|^2-m_*|^2.
\]
Therefore
\[
\|v-\tau\|_4\le C\eta_0^{\gamma/16}.
\]
The positive phase on a fixed lower-amplitude region is bounded by \(C|\zeta|\). The positive connection fitting error is algebraic in \(v-\tau\) and the original current, with fixed lower denominators. The Hopf fit for \(v\) obeys
\[
\|Q(v)-Q(\tau)\|_2
\le C(\|v\|_4+\|\tau\|_4)\|v-\tau\|_4.
\]
These observations identify the extra comparisons needed to upgrade the new rate to D's full, fixed primitive error aggregate. They do not require a \(W^-\) bound.

**Consequential implication, subject to completing this common error-list audit:** D excludes
\[
e_D(1+b)^{3/2}\to0.
\]
Combining \(e_D\le C\eta_0^\theta\) with that exclusion is stronger than routing the same rate through the logarithmic line-bundle lemma. It would give a polynomial density dependence, schematically
\[
\eta_0\ge c(1+b)^{-3/(2\theta)},
\]
with a large, nonoptimal universal exponent. Establishing the quantitative version uses the explicit error bounds and fixed-height line resolvent in D; it is not obtained merely by changing the words in a sequence statement.

Thus, once D's fifth-line estimate is retained as a proved dependency, the newly tracked rate should first be connected to **that stronger theorem**. Re-deriving the logarithmic route alone underuses the available results.

## 4. Why this research can generate many correct pages without finishing either target

The present O10 machinery has a precise bottleneck. Positive-spinor estimates are independent of \(b\), but constructing and testing the differentiated negative-spinor object introduces
\[
\fint(|\nabla^2v|^2+|\nabla v|^4)\le C(1+b).
\]
Repeated improvements to truncation or interpolation then produce increasingly explicit relations between a small actual error and the same uncontrolled growth. Unless an additional equation restricts that growth, or a different test avoids paying it, those improvements do not prove the unrestricted endpoint gap. This is a mathematical obstruction in the **current proof route**, not a theorem that the original problem is inherently unsolvable or extremely hard.

O11 has a different missing implication: its known weak stationarity and adaptive tests do not connect their signed curvature term to the specific topological cost \(8\pi^2Q\). Improving the admissibility of these tests again does not by itself add that connection. The tasks are therefore not two routine omitted estimates of one already closed proof. One asks for a uniform endpoint exclusion in an uncontrolled geometric class; the other asks for a global sharp variational value over all metrics.

The present audit did not establish that a classical theorem already closes either original quantifier. Exact almost-Kähler or Einstein rigidity cannot be substituted for a varying weakly approximately constrained sequence without a valid passage to a limit. Likewise local stability of a known metric does not decide an infimum over all metrics. These are quantifier mismatches, independent of the quality of those classical results.

## 5. Audit boundary

The full first-torsion projection is explicitly stated and algebraically reduced in the original manuscript; it is not an unstated new consequence of the logarithmic lemma. This audit checked its position in the proof chain but has not independently reconstructed every Clifford component of that identity. The fifth-line Cartan symbol identities are likewise retained from the separate D audits, not newly verified here.

No counterexample to O10 or O11 is produced. No unrestricted endpoint theorem or sharp O11 value is claimed. The useful audit result is that the checked Hessian and line-bundle arguments are not circular, while the new error-rate bookkeeping has a stronger existing theorem to connect to than the logarithmic route alone.
