# Route assessment: Step 67

Session: S0910A01.  Agent4 / Preceptor.  Phase: Explore.

## 1. Main correction from this step

Step 66 raised a concern that the restricted Ishida--LeBrun terminal calibrated
density might be a missing theorem after the cutoff-flow construction.  Direct
review shows that this concern should not be carried forward as a gap.  The
existing Step 28 §1 and Step 45 §§2,7 argument already redoes the monopole and
Chern--Weil inequalities on the terminal closed metric.  It does not transport
Weyl data from the initial metric through the flow.

The recovered terminal lemma is now written at
`workspace/notes/step67_terminal_recalibration_recovery.md`:

\[
D_{\rm av}(T)
=J(T)-q-\frac23\sum_\ell |e_\ell^+(T)|^2
\le J(T)\le \frac{Q(T)}{8\pi^2}\qquad(q\ge0),
\]
where
\[
Q(T)=\int|\operatorname{Ric}_{g(T)}+g(T)|^2,
\qquad
J(T)=\frac1{4\pi^2}\int \frac{|\operatorname{Ric}^\circ_{g(T)}|^2}{2}.
\]
Together with the sign-free negative-part density
\[
\mathcal G=f^2-a_{*,-}^2,
\quad
f=\frac23s-2\sqrt{\frac23}|W^+|,
\quad
a_*=\frac23s+2w,
\]
this gives
\[
\int\Phi(g(T))\le119Q(T),
\quad
\Phi=|\operatorname{Ric}+g|^2+(s+4)^2
 +(s+8\sqrt6|W^+|)^2+\mathcal G.
\]
The constant and square identity were checked by
`workspace/scripts/step67_terminal_recalibration_verify.py`, which passes 11/11
and writes `workspace/data/step67_terminal_recalibration_verify.json`.

The new `20260912.tex` manuscript is consistent with this once hypotheses are
kept separate: its lines 285--327 use a simplified `u=-s` setup under explicit
`s<0`; the Step 8 negative-part density is the correct terminal interface because
the terminal metric is not assumed pointwise negative-scalar a priori.  The
manuscript's restricted gap statements under noncollapse/curvature/Bach-flat
hypotheses are not an upper limit on the additional selected-support smoothing
route, but they correctly remind us that the flow still has to provide its own
bounded-curvature pullback charts and proportional terminal volume.

## 2. Repair performed on Step 65 source

Step 65 §4.5 had a broken display after "Grönwall gives" and referenced the
missing equation (4.9).  This was repaired in
`workspace/notes/step65_per_datum_existence_theorem.md`: the note now explicitly
states
\[
\sup_{0\le t\le T_0}\mathcal E_m(t)
\le (\mathcal E_m(0)+1)\exp(C_{m,R,|\sigma|}T_0)-1=:R_m^2,
\tag{4.9}
\]
for every `m>s_0`, uniformly in the regularization parameters.  The Step 65
structural script still passes 24/24 after this repair.

## 3. Actual remaining load in the restricted IL theorem

> **Step 68 update:** The canonical-convention assembly is now complete at
> `workspace/notes/step68_restricted_IL_canonical_assembly.md`.  TTCS
> verification found and repaired four interface issues: single global
> cutoff, volume upper bound, $W^{2,p}$ convergence, and continuation
> by maximality contradiction.  See `workspace/plans/route_assessment_step68.md`
> for full status.

After this recovery, the terminal calibration step is not the unresolved part.
The remaining proof work is the canonical-convention assembly of the selected
support flow stack:

1. Write the restricted theorem under the canonical convention
   \[
   G=(g\owedge g)/(2(n-1)),\qquad T=\operatorname{Rm}-G,
   \qquad \operatorname{Ric}(G)=-g,
   \qquad \operatorname{Ric}(T)=\operatorname{Ric}+g.
   \]
   Legacy notes using `T=Rm+G` must be translated explicitly with old `G=-G`.

2. Combine, without changing hypotheses, the established modules:
   Step 65 per-datum exact degenerate cutoff-flow existence and restart;
   Step 55 `(\Gamma,V)` first-exit coupling and global unweighted `Q` propagation;
   Step 62 three-factor defect Moser endpoint;
   Step 63 curvature endpoint identities under the corrected convention;
   Steps 58--60 continuation hierarchy; Step 28/45 terminal recalibration and
   Liouville pullback selection recovered here.

3. Keep two uniformity levels separate: datum-dependent high-order bounds are
   only needed to restart a smooth solution; the terminal contradiction needs
   sequence-uniform low-order geometry on plateau pullback balls, proportional
   terminal volume, and `Q(T)/A -> 0`.

4. Do not restate the restricted theorem as Yau 26.  Even a completed IL theorem
   covers only a special four-dimensional negative-sign no-Einstein geography
   with `q>=0`.  The positive branch, arbitrary four-manifold topology, all
   dimensions `n>=5`, and Lean formalization remain open.

## 4. Implications for broader Yau26 inquiry

The global search should now avoid two unproductive forms.  First, local no-go
claims around graph necks are too weak: A03's Koiso/analytic Cauchy construction
produces exact local torus reversal germs, so any graph-neck theorem must use
global half-core and matching information, not merely local scalar or torus
slice topology.  Second, A02's mixed `A_1` calculations are valuable local
Einstein desingularization data, but an obstruction there excludes only that
particular degeneration unless paired with a theorem forcing arbitrary Einstein
metrics on the same smooth type into that degeneration.

Thus after one clean IL assembly step, the highest-value global directions are:
positive-branch compactness/desingularization with an unrestricted output metric,
graph-neck half-core existence/nonexistence with full Einstein constraints and
maximum Ricci defect control, and higher-dimensional mechanisms that replace the
four-dimensional SW/self-dual-Weyl calibration.
