# Step 47: Preceptor review of the Step 46 mode-projection theorem

Session S0910A02. Agent4 / Preceptor. Phase Execute.

## 0. Target fidelity

The active target remains Yau's Problem 26 in its full session formulation: decide, for every dimension \(n\ge2\), whether dimension-only two-sided Ricci pinching forces the same closed connected smooth manifold to admit some Einstein metric, and ultimately supply a complete independently checkable Lean 4 proof or strict disproof.  The Step 46 object is only a four-dimensional, positive-sign, noncollapsed, bubble-obstruction route.  Even if repaired into a theorem, it would not settle positive collapse, the negative branch, dimensions \(n\ge5\), arbitrary non-Kleinian bubble groups, or Lean formalization.

This review preserves the valuable part of Step 46: the spin-2 representation calculation is a genuinely useful new structure.  It corrects three load-bearing issues before they harden into a false theorem: the illicit word "generic," the missing curvature-block invariance consequence, and the pointwise form of H4.

## 1. What Step 46 got right

### 1.1 The l=2 invariant-mode computation is valuable

Step 46 computed the invariant part of the five-dimensional spin-2 representation \(\operatorname{Sym}^2_0(\mathbb R^3)\) under the SO(3) image \(\Gamma/\{\pm1\}\) for Kleinian groups \(\Gamma\subset SU(2)\).  The data are in

- `workspace/scripts/step46_gamma_invariant_l2_modes.py`
- `workspace/data/step46_gamma_invariant_l2_modes.json`

The most important numerical/representation facts are:

- \(A_1\): the SO(3) image is trivial, so the invariant dimension is \(5\).
- Cyclic \(A_k\), \(k\ge2\): invariant dimension is positive but small (usually \(1\), with \(A_3\) giving \(3\)).
- Dihedral \(D_k\): invariant dimension is positive but small (\(D_4\) gives \(2\), higher cases \(1\)).
- Exceptional \(E_6,E_7,E_8\): the invariant dimension in the nontrivial chiral block is \(0\).  This agrees with the classical fact that the tetrahedral, octahedral and icosahedral rotation groups have no invariant traceless quadratic form.

This calculation is not a proof of Yau--26, but it turns the previously vague "exceptional locus" into finite representation theory.  It should be kept and extended only after the analytic bridge is put into a correct weak form.

### 1.2 The annulus-window idea is also useful, but only as bookkeeping

Step 46's window
\[
 t\ll r\ll \min(t^{1/2},t^{2/3}\delta^{-1/6})
\]
correctly records the intended scale separation: the Wronskian signal is radius-independent, while Ricci-defect and nonlinear remainders are subleading on a long dyadic range when the bubble scale \(t\to0\).  The data in `workspace/data/step46_annulus_window_analysis.json` confirm many available dyadic scales.

This does **not** by itself prove the analytic theorem.  The weak-type Cheeger--Naber harmonic-radius estimate gives good-set measure control; it does not hand a global differentiated annular gauge on a prescribed radius.  The correct use is a selection and cutoff argument in a weak pairing, not a pointwise ODE with uniform second derivatives.

## 2. Correction 1: remove "generic" from the Kähler corollary

Step 46's §4.3--§4.4 says that for a "generic" Kähler--Einstein orbifold limit, \(\det R_-(p)\ne0\), hence reversed bubbles are obstructed and \(b_+(M)=b_+(M_o)\).  This is not a theorem statement for a sequence supplied by compactness.  There is no probability space or moduli-family hypothesis in Yau--26; the sequence hands us a specific orbifold metric, specific singular points, and specific ALE directions.

The valid statement is a finite dichotomy:

**Corrected Kähler dichotomy (conditional on the analytic bridge).**  Let a noncollapsed positive \(C^0\)-Ricci-pinched sequence converge to a Kähler--Einstein orbifold \((M_o,g_o)\), and suppose the relevant bubble groups/directions lie in the scope of the mode-projection bridge.  Then for every singular point \(p_j\) and every reversed-bubble direction \(\zeta_j\), either
\[
 R_-(p_j)\zeta_j\ne0,
\]
which obstructs that reversed bubble, or the fixed limit lies in the explicit finite degeneracy locus
\[
 R_-(p_j)\zeta_j=0 .
\]
If all reversed directions are obstructed, then only compatible hyperkähler ALE bubbles occur, and the usual compactly supported intersection-form additivity gives \(b_+(M)=b_+(M_o)\) in the corresponding orientation convention.  If a reversed bubble is needed by topology, Yau--26 is not resolved; the task becomes classification of the finite degeneracy alternative at the relevant singular point/direction.

Thus the exclusion of \(\#_k(S^2\times S^2)\), \(k\ge2\), is not an unconditional corollary.  It is the consequence in the obstructed side of the dichotomy.  The other side is exactly the case that can decide the stress family and must be analyzed, not assumed away.

This correction is essential because earlier false turns had the same form: "admissibility" silently assumed the desired obstruction, "alternating labels exclude struts" treated a local condition as global closure, and the product linearization imposed invalid boundary data.  Here "generic" would again hide the hard case.

## 3. Correction 2: use the invariant-mode computation on the curvature block itself

At an orbifold fixed point, the curvature tensor is invariant under the isotropy group.  In chiral form, the block \(R^\pm=W^\pm+\frac\Lambda3 I\) commutes with the isotropy action on \(\Lambda^\pm\).  Therefore the traceless Weyl part \(W^\pm\) belongs to
\[
 \operatorname{Sym}^2_0(\Lambda^\pm)^\Gamma .
\]
On whichever chiral block the local group acts through \(G=\Gamma/\{\pm1\}\subset SO(3)\), this is exactly the same spin-2 invariant representation computed in Step 46.  I verified this again by solving the linear invariance equations for generator matrices; the record is

- `workspace/scripts/step47_curvature_invariant_degeneracy.py`
- `workspace/data/step47_curvature_invariant_degeneracy.json`

### 3.1 Finite degeneracy equations

Let \(a=\Lambda/3>0\).  In a \(G\)-adapted frame for the nontrivial chiral block:

- \(A_1\): \(G\) is trivial.  \(W\) is an arbitrary traceless symmetric \(3\times3\) matrix, and the degeneracy equation is the full cubic
  \[
  \det(aI+W)=0.
  \]
  This is the large double-degeneracy locus represented by the bi-Kähler product quotient.

- \(A_2,A_4,A_5,\ldots\) and most cyclic cases: \(W=\operatorname{diag}(-u/2,-u/2,u)\), so
  \[
  \det(aI+W)=(a-u/2)^2(a+u).
  \]
  Kernel occurs only at the scalar values \(u=2a\) or \(u=-a\).

- \(A_3\): the SO(3) image has order \(2\), so
  \[
   W=\begin{pmatrix}x&y&0\\y&z&0\\0&0&-x-z\end{pmatrix},
  \]
  and the degeneracy equation is
  \[
  (a-x-z)\bigl((a+x)(a+z)-y^2\bigr)=0.
  \]

- \(D_4\): the invariant space is diagonal \(W=\operatorname{diag}(x,y,-x-y)\), giving
  \[
  (a+x)(a+y)(a-x-y)=0.
  \]

- Higher \(D_k\): the same one-parameter axisymmetric equation as most cyclic cases.

- \(E_6,E_7,E_8\): \(W=0\) on the nontrivial block, hence
  \[
   R=aI,
  \]
  which is invertible for \(\Lambda>0\).

### 3.2 Consequence for Step 46's E-type claim

Step 46 described E-type compatible bubbles as a second first-order exceptional locus because no invariant \(l=2\) mode exists in the nontrivial block.  That is incomplete and, for positive Kähler limits, misleading.  The same absence of invariant spin-2 modes forces the curvature block itself to be scalar there; for \(\Lambda>0\) the scalar block \((\Lambda/3)I\) has no kernel.  Thus E-type is not a bi-Kähler-like double-degeneracy loophole for the block on which the isotropy acts nontrivially.

There is a convention caveat.  In the standard complex Kleinian convention, \(\Gamma\subset SU(2)\) fixes the Kähler/hyperkähler chiral triple and acts by the adjoint representation on the opposite block.  Some session notes use the opposite SU(2) naming.  The invariant statement is convention-free: the pinned Kähler block \(R_+=\operatorname{diag}(\Lambda,0,0)\) can occur only on a chiral block where the isotropy action allows that nonzero traceless Weyl tensor.  If an E-type group acted nontrivially on the pinned block, such a positive Kähler orbifold point would be impossible; if it acts on the opposite block, that opposite block is \((\Lambda/3)I\) and reversed bubbles are first-order obstructed.

Therefore the honest exceptional target is much sharper than Step 46 stated.  The largest loophole is \(A_1\), where \(\Gamma/\{\pm1\}\) is trivial and both chiral blocks can be unconstrained by isotropy; this is exactly where the product quotient sits.  For \(A_k\), \(k\ge2\), and \(D_k\), degeneracy is not a vague generic/non-generic condition but one or two explicit scalar equations in an adapted frame.  For E-type, the nontrivial block is not degenerate in positive Einstein normalization.

## 4. Correction 3: H4 must be dual/weak, not a pointwise ODE

Step 46's H4 says that each smooth \(g_i\) gives a classical radial mode function satisfying
\[
 a''+\frac3\rho a'-\frac8{\rho^2}a=S_i,
 \qquad |S_i|\le C(\delta_i+|h_i|^2/\rho^2+\Lambda t_i^2).
\]
The reassurance "each \(g_i\) is smooth" is not enough.  The constant in such a pointwise estimate would require uniform second-order control of the metric perturbation on the annulus.  Step 11's Calderón--Zygmund spike was constructed precisely to show that \(C^0\) Ricci pinching plus weak convergence does **not** give such a pointwise second-derivative bound.  A proof that differentiates the metric pointwise would reintroduce the false regularity route.

The correct H4 target is a dual integration-by-parts statement.

### 4.1 Weak pairing form

On a selected cone-comparison annulus \(A\), take a compactly supported tensor
\[
 T=\phi(\rho)Y(\theta)
\]
where \(Y\) is a \(\Gamma\)-invariant trace-free divergence-free \(l=2\) angular tensor, and choose \(T\) trace-free and divergence-free up to cutoff errors.  Pair the actual pointwise hypothesis with \(T\):
\[
 \left|\int_A \langle \operatorname{Ric}(g_i)-\Lambda g_i,T\rangle\,d\mu_{g_i}\right|
 \le C\delta_i\int_A |T|\,d\mu_{g_i}.
\]
Now expand the Ricci tensor around the cone metric only inside this integral.  The linearized Ricci/Eintein operator is second order in \(h_i=g_i-g_C\), but after integration by parts every derivative falls on the known test tensor:
\[
 \int_A\langle D\operatorname{Ric}_{g_C}(h_i)-\Lambda h_i,T\rangle
 =\int_A\langle h_i,(D\operatorname{Ric}_{g_C}-\Lambda)^*T\rangle
 +\text{controlled boundary/cutoff terms}.
\]
No derivative of \(h_i\) is used in the leading linear term.  The gauge terms vanish when \(T\) is TT, modulo boundary/cutoff terms; this is the reason the TT test formulation is superior to a Bianchi-gauge pointwise ODE.

The nonlinear remainder must still be estimated, but its dangerous second-derivative pieces can be integrated by parts once more, leaving terms controlled by \(C^0\)-smallness of \(h_i\), finite \(W^{1,2}\)/\(W^{2,p}\) harmonic-coordinate control on the good set, and the annular cutoff scale.  This is the actual hard analytic lemma.  It is no longer invalidated by the Step 11 spike, because spikes with large Hessian but small Ricci are invisible to the leading dual pairing except through controlled weak norms.

### 4.2 Distributional one-dimensional equation

Testing against all compactly supported radial profiles \(\phi\) in the selected angular mode gives the scalar coefficient
\[
 a_i(\rho)=\rho^{-2}\int_{S_\rho/\Gamma}\langle h_i,Y\rangle\,dS
\]
not as a pointwise classical solution with a uniform source, but as a distributional solution of the adjoint radial equation:
\[
 \int (a_i L^*\phi)\,w(\rho)d\rho = O(\delta_i)\|\phi\|_{*}+O(\text{quadratic}+\text{cutoff}+\text{bad-set errors}).
\]
One-dimensional regularity/ODE Green formulas then imply, on a fixed dyadic annulus away from the cutoff boundary,
\[
 a_i(\rho)=\alpha_i\rho^2+eta_i\rho^{-4}+O(\delta_i+	ext{controlled weak errors}).
\]
The Wronskian coefficient extraction is a bounded linear functional of \(a_i\), hence survives in the distributional setting.  This is the proof direction that should replace Step 46's H4.

### 4.3 Revised dependency status

- H1/H2 remain source-supported compactness and almost-cone inputs, but only within their actual scope.
- H3 should be weakened: it needs a cone-comparison chart with \(L^\infty\)-small metric values on most of the annulus plus cutoff control of the bad set, not a differentiated global Bianchi/harmonic gauge.
- H4 should be restated as **H4\(_{dual}\)**: the TT test-field pairing above produces the radial distributional equation and Wronskian functional with errors bounded by the Step 46 window.  This is still unproved, but it is a concrete analytic lemma rather than an ill-posed pointwise regularity assertion.

This is the highest-value next theorem-producing target: prove H4\(_{dual}\) on a fixed good annulus.

## 5. Additional scope gap: Kleinian/ADE is not all Cheeger--Naber bubbling

Step 46's theorem statement starts with cone links \(S^3/\Gamma_k\) from Cheeger--Naber but then analyzes only \(\Gamma\subset SU(2)\) Kleinian/ADE groups and hyperkähler ALE bubbles.  General noncollapsed bounded-Ricci four-dimensional limits can have finite \(\Gamma\subset SO(4)\) acting freely on \(S^3\), and general Ricci-flat ALE bubbles need not be covered by Kronheimer's ADE list unless an additional self-dual/Kähler/hyperkähler hypothesis is proved.

Ozuch's source, line 116, says that the proof would also yield an obstruction for other Kleinian singularities by Biquard's lemmas; it does not give an all-\(SO(4)\) statement.  Hence the current mode-projection theorem should be advertised as a Kleinian/hyperkähler-ALE bridge, not as a full noncollapsed positive four-dimensional theorem.  Closing this mismatch would require either:

1. a theorem that every bubble relevant to the positive branch is Kleinian/hyperkähler in the required orientation, or
2. a representation and Pohozaev theory for arbitrary spherical space-form Ricci-flat ALE ends.

No such theorem is currently in the A02 record.

## 6. Corrected value for Yau--26

The Step 46/47 route is still valuable, but its true contribution is narrower and cleaner:

- It can produce a necessary first-order obstruction for noncollapsed positive four-dimensional sequences with Kleinian/ADE ALE bubbles, if H4\(_{dual}\) is proved.
- The obstruction should be vectorial and direction-specific: \(R_\pm(p)\zeta=0\), not merely \(\det R_\pm(p)=0\).
- Applications to \(\#_k(S^2\times S^2)\) must be written as finite alternatives, not as generic exclusions.  If topology forces reversed bubbles and all required reversed directions are nondegenerate, then the sequence is impossible.  If the fixed limit satisfies the explicit degeneracy equations, the classification of that finite exceptional locus becomes the next problem.
- The missing curvature-invariance half of the representation calculation shrinks the exceptional locus: \(A_1\) is the main large double-degeneracy case; \(A_k\), \(k\ge2\), and \(D_k\) reduce to explicit scalar equations; E-type nontrivial blocks are scalar positive and not kernel-bearing for \(\Lambda>0\).
- None of this handles positive collapse, negative pinching, high dimensions, or the formal Lean proof.  It is a route-A theorem candidate, not a resolution of Yau--26.

## 7. Concrete next work

The next strongest research action is for Agent2 to build the dual H4 lemma in a proof note, not another scope inventory.  The note should:

1. define the cone annulus, tensor harmonic \(Y\), radial test profile \(\phi\), and TT/cutoff conditions;
2. write the exact weak pairing against \(\operatorname{Ric}(g_i)-\Lambda g_i\);
3. integrate the linearized Ricci operator by parts and show gauge terms vanish for TT tests, tracking all boundary/cutoff terms;
4. bound the nonlinear remainder without pointwise \(\nabla^2 h\), using only \(C^0\)-small metric values, first-derivative/weak harmonic-coordinate control, and the Step 46 annulus window;
5. derive the scalar distributional radial equation and Wronskian coefficient functional;
6. state clearly what remains if the bad-set or chart-patching estimate cannot be closed.

In parallel or after that, the finite degeneracy classification should be sharpened for \(A_1\), \(A_k\), and \(D_k\), but it should not replace H4\(_{dual}\); without H4\(_{dual}\), the finite equations are only formal constraints.

## 8. Files

- Reviewed theorem: `workspace/notes/step46_mode_projection_vector_obstruction_theorem.md` (patched with a Step 47 warning).
- Step 46 invariant modes: `workspace/data/step46_gamma_invariant_l2_modes.json`.
- Step 46 annulus window: `workspace/data/step46_annulus_window_analysis.json`.
- Step 47 curvature-invariance audit: `workspace/scripts/step47_curvature_invariant_degeneracy.py`, `workspace/data/step47_curvature_invariant_degeneracy.json`.
- Regularity warning: `workspace/notes/step11_cz_spike_and_proposition_A.md`.
- Bi-Kähler/topology correction: `workspace/notes/step45_preceptor_review_biKahler_loophole.md`.
- Source anchor: Ozuch higher-obstruction source, especially lines 83--116 and 512--514.

No branch of Yau--26 is proved or refuted by this review.
