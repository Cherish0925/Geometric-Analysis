# Step 67: terminal recalibration recovery for the IL negative gap route

Session: S0910A01.  Agent4 / Preceptor.  Phase: Explore.

## 0. Purpose

This note checks the Step 66 worry that the terminal calibrated density might be a
new missing theorem.  The Strategist's correction is right: the existing terminal
argument in Step 28 §1 and Step 45 §§2,7 does **not** transport the initial Weyl
profile through the cutoff flow.  It reapplies the monopole inequalities and
Chern--Weil identities directly to the terminal closed metric on the same smooth
manifold.

The recovered result is a purely algebraic/topological lemma.  It is independent
of the cutoff-flow PDE except for the single input that a smooth terminal metric
exists and has terminal unweighted defect energy `Q(T)`.

## 1. Terminal recalibration lemma

Let
\[
M=\left(\#_{j=1}^m X_j\right)\# N,
\qquad m\in\{2,3\},\qquad b_+(N)=0,
\]
carry the Ishida--LeBrun monopole sign family used in the earlier notes.  Put
\[
A=\sum_j c_1^2(X_j)>0,
\qquad
D=4m-(2\chi+3\tau)(N),
\qquad
q=D-\frac A3.
\]
Then
\[
(2\chi+3\tau)(M)=A-D=\frac{2A}{3}-q .
\tag{1.1}
\]

Let `g` be any smooth Riemannian metric on `M` with the fixed complex
orientation.  Define
\[
\mathcal E=\operatorname{Ric}_g+g,
\qquad
Q=\int_M |\mathcal E|^2\,d\mu_g,
\]
and let
\[
E^\circ=\operatorname{Ric}_g-\frac{s}{4}g,
\qquad
I=\frac1{4\pi^2}\int_M\left(\frac{s^2}{24}+2|W^+|^2\right)d\mu_g,
\qquad
J=\frac1{4\pi^2}\int_M\frac{|E^\circ|^2}{2}\,d\mu_g .
\]
Here `W^+` is viewed as a symmetric trace-free endomorphism of `\Lambda^+`, with
operator Hilbert--Schmidt norm, as in `20260912.tex` lines 158--165.

Let `e_\ell` denote the negative-definite summands entering the sign family.  By
averaging the mixed Seiberg--Witten inequality over the exceptional signs,
\[
I\ge \frac23\left(A+\sum_\ell |e_\ell^+|^2\right).
\tag{1.2}
\]
Using Chern--Weil,
\[
I-J=2\chi+3\tau=\frac{2A}{3}-q.
\tag{1.3}
\]
Thus the averaged monopole deficit
\[
D_{\rm av}
=I-\frac23A-\frac23\sum_\ell |e_\ell^+|^2
=J-q-\frac23\sum_\ell |e_\ell^+|^2
\tag{1.4}
\]
satisfies
\[
0\le D_{\rm av}\le J\le \frac{Q}{8\pi^2}
\qquad (q\ge0).
\tag{1.5}
\]
The last inequality uses the orthogonal decomposition
\[
\mathcal E=E^\circ+\frac{s+4}{4}g,
\qquad
|\mathcal E|^2=|E^\circ|^2+\frac{(s+4)^2}{4}.
\tag{1.6}
\]
Consequently
\[
\int_M(s+4)^2\,d\mu_g\le4Q,
\qquad
J\le\frac{Q}{8\pi^2}.
\tag{1.7}
\]

Now set
\[
\nu=|W^+|,
\qquad
f=\frac23s-2\sqrt{\frac23}\,\nu,
a_*=\frac23s+2w,
\qquad
a_{*,-}=\min(a_*,0),
\]
where `w` is the lowest eigenvalue of `W^+`.  Define
\[
\mathcal G=f^2-a_{*,-}^2 .
\tag{1.8}
\]
The pointwise nonnegativity of `\mathcal G` does not require `s<0`: since
`w+sqrt(2/3)|W^+|>=0`, one has `a_*=f+2\xi` with `\xi>=0`; if `a_*<0`, then
`f<=a_*<0`, so `f^2>=a_*^2`, and if `a_*>=0`, the subtracted term vanishes.
This is the older negative-part formulation in Step 8, not the simplified
`u=-s` decomposition in `20260912.tex` lines 285--327, which explicitly assumes
`s<0`.

For every monopole sign class the refined LeBrun negative-part inequality gives
\[
\int_M a_{*,-}^2\,d\mu_g\ge32\pi^2(a^+)^2.
\tag{1.9}
\]
Averaging (1.9) over the sign family gives the same left side and the right side
`32\pi^2(A+\sum |e_\ell^+|^2)`.  Together with the exact square identity
\[
\frac{s^2}{24}+2\nu^2
=\frac1{12}f^2+\frac1{216}(s+8\sqrt6\,\nu)^2,
\tag{1.10}
\]
this implies
\[
4\pi^2D_{\rm av}
\ge
\frac1{12}\int_M\mathcal G\,d\mu_g
+\frac1{216}\int_M(s+8\sqrt6|W^+|)^2\,d\mu_g .
\tag{1.11}
\]
Therefore
\[
\int_M(s+8\sqrt6|W^+|)^2\,d\mu_g
\le864\pi^2D_{\rm av}
\le108Q,
\tag{1.12}
\]
and
\[
\int_M\mathcal G\,d\mu_g
\le48\pi^2D_{\rm av}
\le6Q.
\tag{1.13}
\]

Define the terminal calibration density
\[
\Phi=|\mathcal E|^2+(s+4)^2+(s+8\sqrt6|W^+|)^2+\mathcal G.
\tag{1.14}
\]
Combining (1.7), (1.12), and (1.13), for every smooth terminal metric on the
same IL smooth manifold with `q>=0`,
\[
\boxed{\int_M\Phi\,d\mu_g\le(1+4+108+6)Q=119Q.}
\tag{1.15}
\]
This is exactly the Step 28/45 estimate.  No density transport, boundary
transgression, or pointwise sign assumption on terminal scalar curvature is used.
If `q<0`, (1.4) would only give `D_av <= J+(-q)`, producing an extra negative-q
term.  In the restricted IL theorem `q>=0`, so such a term is absent.

## 2. Plug into the terminal pullback selection

At the observation time `T=theta r^2` of the selected-support flow, the terminal
metric is a closed smooth metric on the original smooth manifold.  Therefore the
lemma applies with
\[
Q(T)=\int|\operatorname{Ric}_{g(T)}+g(T)|^2\,d\mu_{g(T)}.
\]
The global unweighted defect propagation from Step 36/55 gives
\[
Q(T)\le e^{C(1+r^{-2})T+C_VV(T)}Q(0).
\tag{2.1}
\]
For a near-negative-Einstein input sequence, `Q(0)/A -> 0`, so for fixed
observation parameters,
\[
\frac1A\int_M\Phi(g(T))\,d\mu_{g(T)}\le119\frac{Q(T)}A\to0.
\tag{2.2}
\]

If the selected-support theorem supplies terminal inner centers `P_i` with
\[
\operatorname{Vol}_{g_i(T)}(P_i)\ge\alpha A_i,
\tag{2.3}
\]
and a fixed curvature/buffer radius `(K,rho)`, the Step 28/45 unit-tangent-bundle
Liouville argument gives, for the nonnegative density `\Phi`,
\[
\int_{P_i}A_\rho\Phi_i(p)\,d\mu_{g_i(T)}(p)
\le C(K,\rho)\int_{M_i}\Phi_i\,d\mu_{g_i(T)} .
\tag{2.4}
\]
Thus some `p_i in P_i` satisfies
\[
A_\rho\Phi_i(p_i)
\le\frac{C(K,\rho)}{\alpha A_i}\int_{M_i}\Phi_i
\to0.
\tag{2.5}
\]
The pullback ball `B_\rho(0)\subset T_{p_i}M_i` has bounded curvature and
Rauch noncollapse even if the base image collapses or self-overlaps.  Strong
harmonic-coordinate convergence plus `\Phi_i -> 0` then yields a smooth Einstein
germ with
\[
\operatorname{Ric}=-g,
\quad s=-4,
\quad |W^+|^2=1/24,
\quad \mathcal G=0.
\]
The gap algebra forces
\[
\operatorname{spec}(W^+)=(-1/6,1/12,1/12).
\]
Derdziński Proposition 5 then makes the Einstein germ locally Kähler with
constant conformal factor, but a Kähler--Einstein four-germ with `Ric=-g` has
`|W^+|^2=s^2/24=2/3`, not `1/24`.  This is the existing forbidden-germ
contradiction.

## 3. Relation with the 20260912 manuscript

The new manuscript is consistent with the recovered terminal lemma after separating
hypotheses.

* Lines 158--165 fix exactly the same four-dimensional Chern--Weil norms: trace-free
  Ricci as a two-tensor and `W^+` as an operator on `\Lambda^+`.
* Lines 285--327 present a useful nonnegative decomposition under the explicit
  local assumption `s<0`.  That display should not be used blindly for the
  terminal flowed metric.  The Step 8 negative-part density (1.8) is the correct
  sign-free interface.
* Lines 329--368 list restricted gap statements under extra geometric hypotheses
  available inside the manuscript alone: noncollapse, a global curvature bound,
  or Bach-flat/constant-scalar structure.  The session's additional selected-support
  smoothing route is a different mechanism: it attempts to create bounded-curvature
  pullback charts on `A`-proportional terminal volume, while the topological lemma
  above supplies the small terminal total density.

Thus the manuscript's restricted statements are not a disproof of the stronger IL
smoothing route, but they remind us that the flow must actually provide (2.3) and
the curvature/buffer conditions; the algebra alone does not.

## 4. What remains load-bearing after this recovery

This step removes one false missing piece: terminal IL calibration is already an
established algebraic lemma, recovered above.  The remaining load is more specific.

1. The selected-support flow stack must be assembled under the canonical convention
   `G=(g\owedge g)/(2(n-1))`, `T=Rm-G`, `Ric(G)=-g`, including the Step 55
   `(Gamma,V)` coupling, Step 62 three-factor defect Moser endpoint, Step 63
   curvature endpoint, Step 58--60 continuation hierarchy, and Step 65 per-datum
   existence/restart.  This note did not independently reprove all those modules.
2. The proof of terminal compactness must keep sequence-uniform low-order geometry
   separate from datum-dependent high-order restart bounds.  Step 56 §§4--5 states
   this correctly; Step 65 §4.5 has now been repaired to restore the missing
   Grönwall display.
3. The restricted IL theorem, even after assembly, remains a four-dimensional
   negative-sign result over a special Seiberg--Witten geography.  It is not the
   sign-unrestricted, all-dimensional Yau 26 resolution and carries no Lean 4
   formalization yet.
4. The valuable global fronts are now outside local no-go shortcuts: A03's exact
   local torus reversal makes the graph-neck problem a global half-core/matching
   problem, and A02's mixed `A_1` work can prove or obstruct particular
   desingularizations but not unrestricted Einstein nonexistence without a global
   theorem controlling arbitrary hypothetical Einstein metrics on that smooth type.

## 5. Evidence files checked

* Step 28 terminal recalibration and pullback selection:
  `Sessions/S0910A01/workspace/notes/step28_terminal_recalibration_pullback.md`,
  especially lines 30--150 and 179--220.
* Step 45 consolidated IL proof, §§2 and 7:
  `Sessions/S0910A01/workspace/notes/step45_consolidated_IL_negative_gap_proof.md`,
  especially lines 76--170 and 546--599.
* Step 8 negative-part density and Derdziński source verification:
  `Sessions/S0910A01/workspace/notes/step8_derdzinski_measure_local_theorem.md`,
  especially lines 83--155.
* Step 56 terminal compactness:
  `Sessions/S0910A01/workspace/notes/step56_common_time_and_terminal_compactness.md`,
  lines 308--419 and 429--469.
* New manuscript norm/decomposition comparison:
  `Skills/qiushi-yau26/references/research/20260912.tex`, lines 158--165,
  285--327, and 329--368.
* Script confirmation of constants:
  `Sessions/S0910A01/workspace/scripts/step28_terminal_pullback_constants.py`
  prints the constants `108`, `6`, and `119`.
