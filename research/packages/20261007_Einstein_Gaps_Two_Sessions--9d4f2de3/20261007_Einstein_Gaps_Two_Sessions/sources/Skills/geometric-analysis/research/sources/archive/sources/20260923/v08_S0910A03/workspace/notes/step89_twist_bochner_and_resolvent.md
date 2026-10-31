# Step 89: Variable-fibre T² reduction with twist — Bochner sign and resolvent extension

Session `S0910A03`, Agent2 / Execute.

> **Superseded for spatially variable/forced twist by Step 90.** This note correctly
> derives the direct twist Ricci blocks and the sign of the Einstein-solved drift
> curvature. Its resolvent curve assumes spatially constant \(Q\). In the actual
> forced problem \(Q(x)\) varies, the target source is
> \(S_F=-\nabla_{\mathbb H^2}Q\), and its derivative contributes \(-Qe\), exactly
> cancelling the apparent \(+Qe\) drift improvement. Use
> `workspace/notes/step90_structured_forced_twist_and_radial_escape.md` for the
> structured variable-charge equations and current scope.

## 1. Full T²-reduction with twist

### Metric
\[
g=\gamma_B+G_{ab}(d\xi^a+A^a)(d\xi^b+A^b),\qquad
G=e^\sigma M,\quad\det M=1,\quad \rho=e^\sigma.
\]
Connection curvature: \(F^a=dA^a=f^a\mathrm{vol}_{\gamma_B}\) on the 2D base.

### Charge and twist energy
\[
q_a=\rho G_{ab}f^b=\rho^2M_{ab}f^b,\qquad
Q=\tfrac12G_{ab}f^af^b=\tfrac12\rho^{-3}\,q^TM^{-1}q.
\tag{1.1}
\]

### Symbolic Ricci verification

A full SymPy computation for the 4D metric
\[
g=e^{2\lambda}(dr^2+dz^2)+e^{\sigma+\alpha}(d\xi_1+Pdz)^2+e^{\sigma-\alpha}d\xi_2^2
\]
(with all functions of \((r,z)\)) establishes:

**Orbit twist Ricci:**
\[
\operatorname{Ric}^{\rm twist}_{ab}=\tfrac12G_{ac}G_{bd}f^cf^d.
\tag{1.2}
\]
The factor is \(1/2\), not 1. Verified: \(\operatorname{Ric}^{\rm twist}_{22}/(G_{11}^2f_1^2)=1/2\).

**Base twist Ricci (direct):**
\[
\operatorname{Ric}^{\rm twist}_{ij}=-Q\gamma_{ij}.
\tag{1.3}
\]
Verified: \(\operatorname{Ric}^{\rm twist}_{rr}/(e^{2\lambda}Q)=-1\).

**Orbit trace → area equation:**
\[
G^{ab}\operatorname{Ric}^{\rm twist}_{ab}=Q,\qquad
\boxed{L\sigma=6+Q.}
\tag{1.4}
\]

**Maxwell conservation (mixed Ricci):**
For exact Einstein, the charge \(q_a\) is constant. In coordinates:
\[
\operatorname{Ric}(e_r,V_1)\propto\partial_z q_1,\qquad
\operatorname{Ric}(e_z,V_1)\propto\partial_r q_1.
\]

**Orbit traceless (diagonal \(M\), \(f_2=0\)):**
\[
L\alpha=Q,\qquad |S_F|^2=Q^2.
\tag{1.5}
\]

All formulas verified symbolically and numerically in
`workspace/scripts/step89_symbolic_twist_ricci.py` and
`workspace/data/step89_symbolic_twist_ricci.json`.

## 2. Critical sign propagation

The direct base twist Ricci is \(-Q\gamma_B\) (equation (1.3)). However, the
full horizontal Einstein equation reads
\[
\operatorname{Ric}_B-\operatorname{Hess}\sigma
-\tfrac12d\sigma^2-\tfrac12U^*h_{\mathbb H^2}-Q\gamma_B=-3\gamma_B.
\]
Solving for the drift curvature:
\[
\boxed{\operatorname{Ric}_B-\operatorname{Hess}\sigma
=(-3+Q)\gamma_B+\tfrac12d\sigma^2+\tfrac12U^*h_{\mathbb H^2}+E_B.}
\tag{2.1}
\]
The \(-Q\gamma_B\) on the LHS becomes \(+Q\gamma_B\) on the RHS. Therefore the
effective drift curvature is
\[
\operatorname{Ric}^4_\sigma
=(-3+Q+\delta_-)\gamma_B+\tfrac12U^*h_{\mathbb H^2},
\tag{2.2}
\]
where \(\delta_-\) accounts for the base defect. The curvature parameter is
\(K=3-Q+\delta\), and for \(Q<3\) the geometry is \(CD(-(3-Q+\delta),4)\).

**The twist is favorable for the base curvature bound.** A previous intermediate
analysis in this Step incorrectly concluded \(\operatorname{Ric}^4_\sigma=
-(3+Q)\gamma_B+\cdots\), failing to flip the sign when solving the Einstein
equation. The TTCS verifier caught this error. The Step 88 TTCS generator's
final formulas were correct despite its own sloppy intermediate sign reasoning.

## 3. Modified Bochner identity

Using the weighted Bochner formula for maps \(U:(B,\gamma_B,e^\sigma)\to\mathbb H^2\),
with target curvature \(-1\) giving \(+2\det A\):
\[
\tfrac12Le
=|DdU|^2+\tfrac12|dU(\nabla\sigma)|^2+\Phi(A)-(3-Q)e
+\operatorname{div}_\sigma V-|S_F|^2+E_B{:}A,
\tag{3.1}
\]
where \(\Phi(A)=\tfrac12\operatorname{tr}(A^2)+2\det A\ge\tfrac12e^2\) and
\(V(X)=\langle dU(X),\tau_\sigma(U)\rangle\).

Dropping nonnegative terms:
\[
\boxed{\tfrac12Le\ge\tfrac12e(e-6+2Q)+\operatorname{div}_\sigma V-Q^2-\delta e.}
\tag{3.2}
\]
The reaction zero is at \(e=6-2Q+2\delta\), which is **lower** than the
OT value 6+2δ. Thus **twist strengthens the Bochner subsolution**.

## 4. Massive resolvent comparison

Set \(\kappa=6-2Q+2\delta\) and \(f=Q+2\delta\) (combined forcing). Then
\[
(-L+\kappa)e\le\kappa^2+2f^2-2\operatorname{div}_\sigma V,
\qquad |V|\le f\sqrt e.
\tag{4.1}
\]
The Fisher/resolvent gradient constant under \(CD(-(3-Q+\delta),4)\) is
\[
C_\kappa\le\frac2{\sqrt{3-Q+\delta}}.
\tag{4.2}
\]
Self-consistent closure:
\[
\boxed{B:=\sup e\le\left[\frac{2f}{\sqrt{3-Q+\delta}}
+\sqrt{2(3-Q+\delta)+\frac{5f^2}{3-Q+\delta}}\right]^2.}
\tag{4.3}
\]

Combined with the separator floor \(12+2Q-8\delta\), the obstruction holds when
the ceiling (4.3) is less than the floor.

## 5. Quantitative thresholds

### Exact Einstein with constant twist (\(\delta=0\))
\[
Q_*=0.8986\ldots
\]
Obstruction holds for \(0\le Q<Q_*\). At \(Q_*\): ceiling = floor = 13.797.

### Step 87 recovery
At \(Q=0\): \(\delta_*=0.24625\), exactly reproducing Step 87.

### Combined \((Q,\delta)\) threshold
| \(Q\) | Critical \(\delta_*\) |
|------:|-----:|
| 0.0 | 0.2463 |
| 0.2 | 0.2054 |
| 0.4 | 0.1570 |
| 0.6 | 0.1007 |
| 0.8 | 0.0356 |
| 0.9 | — |

Scripts and data: `workspace/scripts/step89_twist_resolvent_final.py`,
`workspace/data/step89_corrected_twist_resolvent.json`.

## 6. Structural constraint: exact twist and cusp ends

For exact Einstein with commuting Killing fields, the twist scalars
\(\alpha_a=\rho\langle[X,Y/\mu],V_a\rangle\) are constant \cite{liutoric}.
If the metric has an exact OT open end where \(F=0\), then \(\alpha_a=0\)
throughout the connected free region. The charge \(q_a=\rho^2M_{ab}f^b\) is
also zero.

**Exact-Einstein consequence only:** If the metric is Einstein throughout the
connected free region, an exact OT cusp open set forces the conserved charge to
vanish globally. This does **not** apply to an approximately Einstein interior:
its mixed Ricci defect sources \(dq\), so nonzero interior twist may coexist with
exact OT ends. The \(Q_*\) arithmetic is relevant only under the additional
spatially constant-\(Q\) specialization; the forced variable-charge case is open:
1. Merely asymptotic OT ends (where physical \(F\to0\) but \(q\ne0\))
2. Non-exact-cusp attachments
3. Forced (approximate Einstein) connectors with mixed Ricci defect

## 7. Separator floor with twist (verified)

On the minimal separator, the connection's normal derivative contributes to \(|\mathrm{II}|^2\):
\[
\sum_a|\mathrm{II}(T,E_a)|^2=\tfrac12G_{ab}f^af^b=Q.
\tag{7.1}
\]
Hence \(|\mathrm{II}|^2\ge Q\), and Step 88's identity gives:
\[
\langle e_s\rangle\ge12+2\langle Q\rangle-8\delta.
\tag{7.2}
\]
The separator floor is **raised** by twist.

## 8. Summary of twist effects

| Effect | Sign | Mechanism |
|--------|------|-----------|
| Drift curvature | Favorable (\(+Q\)) | Einstein eq moves \(-Q\gamma\) to opposite side |
| Bochner reaction | Favorable | Zero at \(6-2Q\) instead of \(6\) |
| Resolvent mass | Lower (\(6-2Q\)) | Stronger resolvent |
| Separator floor | Favorable (\(+2Q\)) | \(|\mathrm{II}|^2\ge Q\) from connection |
| Tension \(|S_F|^2\) | Adverse (\(-Q^2\)) | Orbit-map forcing |
| Area growth | Amplified | \(L\sigma=6+Q>6\) |
| Curvature bound | Improved | \(K=3-Q\) instead of \(3\) |

For spatially constant \(Q\), this bookkeeping gives the stated arithmetic crossing. It does not show a net strengthening for variable twist; Step 90 exhibits the exact \(+Qe\)/\(-Qe\) cancellation and a radial redshift-and-discharge mechanism.

## Provenance

- Symbolic verification: `workspace/scripts/step89_symbolic_twist_ricci.py` →
  `workspace/data/step89_symbolic_twist_ricci.json`
- Resolvent computation: `workspace/scripts/step89_twist_resolvent_final.py` →
  `workspace/data/step89_corrected_twist_resolvent.json`
- Independent TTCS verification:
  `trace/ttcs/results/step89_ttcs01_verifier1_integration.md`
- Supersedes: the incorrect intermediate claim in this Step that the base twist
  is adverse. The TTCS generator (Step 88) was correct in its final drift-curvature
  formula despite sloppy intermediate reasoning.
