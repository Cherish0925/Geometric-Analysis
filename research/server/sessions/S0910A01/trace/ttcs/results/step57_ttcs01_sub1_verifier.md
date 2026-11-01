# TTCS Independent Branch Record

```json
{
  "step_id": 57,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step57_preceptor_deTurck_uniqueness_and_scope_review.md",
    "Sessions/S0910A01/workspace/notes/step56_common_time_and_terminal_compactness.md",
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md",
    "Sessions/S0910A03/workspace/notes/step59_finite_regularity_continuation_and_common_time.md",
    "Sessions/S0910A01/workspace/notes/step55_finite_restart_threshold_and_C3_exchange.md"
  ]
}
```

## Task

Verify the Step57 repair note for the restricted Ishida--LeBrun cutoff-flow route. Focus on the load-bearing issues, not style: (1) Is the rejection of Step56's raw metric-difference uniqueness argument mathematically justified? (2) Does the proposed coupled transported-cutoff DeTurck pair uniqueness energy for H=G1-G2 and b=beta1-beta2 plausibly close on a smooth per-datum overlap, especially the metric Lie-cross term, scalar transport term, and need for averaged (beta1^2+beta2^2)|DH|^2 dissipation? Identify any missing derivative, coefficient, or gauge-reconstruction issue. (3) Does the note correctly keep finite current-pair induction as an unfinished proof dependency rather than assuming it? (4) Does the corrected scope preserve the IL-class uniform A-cancellation and avoid the old topology-shrinking threshold or a mistaken no-Einstein conclusion? Return a concise mathematical memo with any necessary repairs or confirmations.

## Output

## Mathematical verification memo

### 1. Raw metric-difference estimate

The rejection of Step56 §2.6 is mathematically justified.

For the ungauged equation
\[
\partial_tg=-2a(\operatorname{Ric}_g+g),\qquad a=\chi^2,
\]
the linearization of Ricci in fixed coordinates contains
\[
\frac12\left(
\nabla_i\nabla^kh_{kj}
+\nabla_j\nabla^kh_{ki}
-\nabla_i\nabla_j\operatorname{tr}h
-\Delta h_{ij}\right)
+\operatorname{Rm}*h.
\]
Thus it is not simply \(-\frac12\Delta_Lh\) plus lower-order terms. The principal symbol retains the infinitesimal diffeomorphism directions; multiplication by \(a\) does not remove them, and derivatives of \(a\) contribute only lower differential order. For \(h=\mathcal L_Xg\), naturality gives
\[
D\operatorname{Ric}_g(\mathcal L_Xg)=\mathcal L_X\operatorname{Ric}_g,
\]
rather than a coercive tensor Laplacian on \(h\). Consequently the raw estimate used in the earlier Step56,
\[
\frac d{dt}\|h\|_2^2+\int a|\nabla h|^2\le C\|h\|_2^2,
\]
does not follow from the ungauged equation. This invalidates that particular proof, not uniqueness itself.

### 2. Coupled DeTurck-pair energy

The proposed pair argument is structurally sound on a smooth per-datum overlap, provided all norms and integration are taken relative to a fixed background metric.

Set
\[
A_i^{ab}=\beta_i^2G_i^{ab},\qquad
\bar A^{ab}=\frac12(A_1^{ab}+A_2^{ab}).
\]
After subtraction, the metric equation can indeed be arranged as
\[
\partial_tH
=\bar A^{ab}D_aD_bH+B^aD_aH+CH+fb+P^aD_ab,
\]
with
\[
\bar A^{ab}\xi_a\xi_b
\ge c(\beta_1^2+\beta_2^2)|\xi|_{\bar g}^2.
\]
The essential weighted structure is
\[
|D\bar A|+|B|
\le C\bigl(\beta_1+\beta_2+\beta_1^2+\beta_2^2\bigr),
\qquad
|P|\le C(\beta_1+\beta_2).
\]
These weights should be stated explicitly in place of generic bounded-coefficient notation. They are what permit absorption when either cutoff vanishes.

The Lie-cross term behaves correctly:
\[
d(\beta_1^2)\otimes W_1-d(\beta_2^2)\otimes W_2
\]
splits into terms of the forms
\[
\beta_iD\beta_i*DH,\qquad
\beta_iW_i*Db,\qquad
b\,D\beta_i*W_i,\qquad H\,d(\beta_i^2).
\]
For the \(Db\) contribution,
\[
\int H*P*Db
=-\int b*P*DH-\int b*(DP)*H.
\]
The first integral is absorbed by the weighted metric dissipation because \(P\) contains a factor \(\beta_i\). The second is zero-order; \(DP\) contains \(D\beta_i\), \(DW_i\), and hence at most \(D^2G_i\), all bounded under (2.2). No estimate for \(Db\) is required.

The scalar equation is most cleanly written using \(v_i=\beta_i^2W(G_i)\):
\[
\partial_tb=v_1\cdot Db+(v_1-v_2)\cdot D\beta_2,
\]
where
\[
|v_1-v_2|
\le C\beta_1^2(|DH|+|H|)
  +C(\beta_1+\beta_2)|b|.
\]
Testing by \(b\) gives
\[
\frac12\frac d{dt}\|b\|_2^2
\le C(\|b\|_2^2+\|H\|_2^2)
+\varepsilon\int\beta_1^2|DH|^2.
\]
Also,
\[
\int b\,v_1\cdot Db
=-\frac12\int \operatorname{div}v_1\,b^2,
\]
and \(\operatorname{div}v_1\) is bounded from the assumed smooth norms.

Thus the combined estimate
\[
\frac d{dt}\bigl(\|H\|_2^2+A\|b\|_2^2\bigr)
+c\int(\beta_1^2+\beta_2^2)|DH|^2
\le C\bigl(\|H\|_2^2+A\|b\|_2^2\bigr)
\]
is plausible. One chooses \(A\), then chooses the Young parameter in the scalar estimate sufficiently small relative to \(A\). The averaged dissipation is valid and useful because it absorbs terms carrying either \(\beta_1\) or \(\beta_2\); a consistently one-sided subtraction could use only one weight, but the symmetric form is more robust.

A minor textual correction is needed in Step57 §2.3: before testing by \(b\), the forcing has the form \(\beta_1^2DH+H+b\); the factors \(\beta_1^2DH\,b\), \(Hb\), and \(b^2\) arise only after multiplication by \(b\).

### 3. Remaining gauge-correspondence step

Pair uniqueness does not by itself yet prove geometric overlap agreement.

From a known pair \((G,\beta)\), reconstruction is straightforward: solve the smooth ODE
\[
\partial_t\varphi=-\beta^2W(G)\circ\varphi,\qquad \varphi(\tau)=\mathrm{id},
\]
then
\[
g=\varphi^*G,\qquad \beta\circ\varphi=\chi,
\]
and the displayed pair system gives
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g+g).
\]

The reverse passage from a prescribed geometric solution \(g(t)\) to
\[
G=(\psi^{-1})^*g,\qquad \beta=\chi\circ\psi^{-1}
\]
requires more than the reconstruction ODE: \(W(G)\) depends on spatial derivatives of the unknown \(\psi\), so the equation for \(\psi\) is a DeTurck/harmonic-map type PDE, degenerate where \(\chi=0\). The supplied note says to “solve the DeTurck diffeomorphism equation” but does not establish this reverse gauge lemma.

The overlap argument therefore needs one of two concrete ingredients:

1. local smooth solvability and uniqueness of that reverse gauge equation, with identity data and the same fixed background for both geometric solutions; or  
2. a maximal branch maintained entirely in pair variables, together with restart bounds for the pair state \((G,\beta)\).

Once both geometric solutions are represented by pairs with identical data at the overlap time, the energy argument and the reconstruction ODE give geometric agreement.

### 4. Finite current-pair induction

Step57 correctly records the finite induction as unfinished mathematical work rather than using it as an established theorem. The scripts described in the notes verify derivative allocation and exponent arithmetic, not the tensor evolution identities.

The schematic formula (3.2) needs one explicit amendment. Since
\[
D^{m+2}(\chi^2)
=2\chi C_{m+2}
  +c_m\,C_1*C_{m+1}
  +\sum_{2\le j\le m}c_{m,j}C_j*C_{m+2-j},
\]
the \(U_m\) equation also contains
\[
C_1*C_{m+1}*U,
\]
and the \(T_m\) equation contains
\[
C_1*C_{m+1}*T.
\]
These terms already appear in Step55 at \(m=2\). They are manageable because \(C_1,U,T\) are bounded and \(C_{m+1}\) belongs to the current pair, but they cannot be placed in a remainder described as containing only previous levels. The general lemma should permit linear current-pair terms with bounded coefficients, together with the displayed \(\chi C_{m+2}\), \(\chi C_{m+1}\), and signed-Hessian terms.

The other load-bearing requirements listed in Step57 §3 are the right ones: preservation of the leading \(\chi\), no enlarged exponent for a current variable, control of \(\chi C_2*U_m\) and \(\chi C_2*T_m\) by signed integration, and absence of \(U_{m+1}\) from the \(C_{m+1}\) evolution.

### 5. IL-class constant and theorem meaning

The \(A\)-cancellation is algebraically correct:
\[
\int\Phi_i\le C\delta_i^2A_i,\qquad
\operatorname{Vol}(P_i^{\rm in})\ge c_0A_i
\]
imply
\[
\inf_{p\in P_i^{\rm in}}\mathcal A_\rho\Phi_i(p)
\le \frac{C}{c_0}\delta_i^2.
\]
Combined with a topology-independent local lower bound \(\eta\), this gives
\[
\delta_i^2\ge \frac{c_0\eta}{C}.
\]
There is no residual \(A_i^{-1/2}\) factor. Uniformity over the stated IL family still requires \(C,c_0,K,\rho,\eta\) and the support/flow constants to be independent of the varying characteristic numbers; Step57 states this dependence correctly.

The resulting statement excludes sequences in that IL family satisfying
\[
\|\operatorname{Ric}_g+g\|_{\infty,\mathrm{op}}\to0.
\]
It does not imply that the underlying smooth manifold carries no Einstein metric; such a fact, when available, comes from separate gauge-theoretic topology. It also does not address the positive-Ricci side, general four-manifolds, \(n\ge5\), or the full Yau problem.

**Overall:** the raw uniqueness correction is correct, the coupled pair energy has the right weighted mechanism, and the \(A\)-cancellation is preserved. The principal unresolved point in the overlap argument is the reverse geometric-to-pair gauge construction. The finite induction remains genuinely pending, with the additional current term \(C_1*C_{m+1}*(U\text{ or }T)\) required in its general tensor ledger.