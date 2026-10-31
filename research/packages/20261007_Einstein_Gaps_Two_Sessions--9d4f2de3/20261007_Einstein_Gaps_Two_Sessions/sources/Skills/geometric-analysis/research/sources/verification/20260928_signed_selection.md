# Signed selection: derivation and verification record

28 September 2026. Base `0fb009cc41d22bd218abd3f0ae1cf2c108867c4e`.
Local branch `local/yau26-cell-cost-20260928`. No external package,
upload, service change, or mutation of the preserved baseline.

## Mathematical change

[The continuous proof](../continuation/20260928_signed_characteristic_selection.md)
does not claim a new value of the unrestricted infimum. It proves:

1. I55's measurable bulk selection is equivalent to N>=Q-o(Q) for
   competitive metrics, with N defined from the signed characteristic
   density rather than an unspecified topological charge.
2. Demailly's classical weak Morse inequality supplies N>=k for genuine
   Kahler blowups. This is an attributed classical-input consequence.
3. Actual scalar-minus-four competitive metrics on the original balanced
   family violate N>=Q-o(Q). Their coefficient is greater than four.
4. True o(h)-excess near-minimizers contain only o(Q) disjoint nontrivial
   full-CH-collar cells from a fixed smooth compact family. The proof
   uses finite simultaneous variations, not a stationary equation
   assigned to an arbitrary minimizing sequence.

The original all-metric coefficient and weak zero endpoint remain open.
The stronger all-competitive selector is now refuted rather than left
as a task to be repeatedly attempted. Actual-field costs outside the
negative-density set are retained in the exact compensation identity.

## Independent derivation and review

Three fresh-context GPT-6 Astra agents at max reasoning worked read-only;
the root agent alone edited this branch.

- `bulk_selection_20260928b`: actual scalar equation, CH local scalar
  gluing, fixed-j handle/Yamabe limits, same balanced topology, then
  the near-minimizer finite-variation consequence.
- `coupled_cell_global_20260928b`: independent radial characteristic
  primitive and negative-mass variation; independent review of the
  scalar equation, Delay hypotheses and fixed-j limiting argument.
- `zero_cubic_gap_20260928b`: actual hyperbolic-core test of the final
  signed identity, calibrated fit scale and sharp critical shell costs.

The root independently checked the negative-mass selection equivalence,
the holomorphic Morse supplier, the local scalar gluing hypothesis,
the finite-moment variation and the cutoff minimization. The two
independent cell calculations agreed on the second variation of N.
Agent agreement is bounded proof review, not an external correctness
or originality certification.

One proposed extrapolation was rejected during calculation: the
fixed-mu mass-loss coefficient is not uniform under shrinking the
bolt with a fixed rescaled bump. Its support shoulders already force
N>=1-O(mu). The final construction fixes parameters before taking
the cover-dilution limit, and does not make the rejected inference.

## Primary literature checked

- [Demailly, arXiv:1003.5067](https://arxiv.org/html/1003.5067), equations
  (1.11)--(1.12), supplies the weak holomorphic Morse inequality in
  the required curvature-index convention. No converse is invoked.
- [Delay, arXiv:1003.5146](https://arxiv.org/html/1003.5146), Theorem 1.1
  and Propositions 2.2--2.5, supplies supported smooth scalar-curvature
  gluing for nearby metrics with no adjoint kernel. The CH kernel is
  excluded explicitly in the proof, not assumed from genericity.
- The ordinary actual supply, classical Ricci budget, shrinking handles,
  and exact conformal transfer are inherited from I03/I41/I44/I54;
  the new proof specifies the fixed-j order of limits needed here.

## Computation

Command: `python3 tools/check_signed_characteristic_mass.py`.
Seven exact tests pass: radial conformal characteristic primitive;
recovery primitive and negative mass; minimum second variation;
Kahler normalization; pluricanonical Euler difference; finite-moment
first variation; critical cutoff identity and minimizing energy.

The executable then integrates actual complete conformal cells with
mu=0.01, outer radius 2.5, fixed smooth cutoff from r=1 to r=2,
and the compactly supported bump specified in the program.

| epsilon | negative characteristic mass | J/(2 pi squared) |
| --- | --- | --- |
| 0 | 0.9999999999999992 | 4.041473585258187 |
| 0.01 | 0.999973955691314 | 4.077939349922743 |
| 0.02 | 0.9999013831424652 | 4.187334778471816 |

The total characteristic integral differs from R^4/4-1 by less than
1.3e-14 in these runs. Sample-bracketed density zeros are a numerical
receipt, not a proof that no unsampled zero exists. The small-parameter
existence and uniqueness argument is in the text. These computations
do not numerically implement Delay's PDE correction or certify the
global gluing theorem.

## Zero-end continuation

[Signed flux, Section 7](../continuation/20260928_signed_quartic_flux.md)
retains the actual-core calculation. On fixed torsion mass shells,
the critical H-minus and H-plus energies satisfy
E-minus minus (8/9) E-plus = 32 pi squared/3, with explicit sharp
cutoff infima. Nevertheless the final signed curvature identity is
zero on both sides because W-minus and traceless Ricci vanish on
those actual local cores. Their calibrated ASD fit costs scale-four,
and their quadratic derivative costs scale-two. No closed calibrated
exterior matching or endpoint contradiction is supplied.

The attempted global coupled-cell logarithmic estimate did not close.
The existing radial chiral equations admit coupled degeneration;
neither a new sub-four cell nor a uniform cost-versus-mass estimate was
obtained. This attempt is not registered as a theorem.

### Retained coordinate calculations for continuation

The coupled-cell agent also computed the full diagonal chiral variables.
In I55's radial conventions set
\[
 A=r\sqrt F\phi',\quad C=r\sqrt Fw'+2\sinh(2w)/\sqrt F,
\]
\[
 q_1=e^w(A+C),\quad q_2=e^{-w}(A-C),\quad
 q_3=2F+rF'/2+rF\phi'-2\cosh(2w).
\]
With
\[
 Q_i=(\sqrt F e^{-w}q_1'/r,\sqrt F e^wq_2'/r,q_3'/r)_i,
\]
\[
 P_i=\left(\frac{e^w(2q_1+q_2q_3)}{r^2\sqrt F},
 \frac{e^{-w}(2q_2+q_1q_3)}{r^2\sqrt F},
 \frac{2q_3+q_1q_2}{r^2}\right)_i,
\]
the reported exact coordinate checks are
\[
 e^{2\phi}s=-2\sum_i(Q_i+P_i),\quad
 e^{4\phi}|\operatorname{Ric}^{\circ}|^2=\sum_i(Q_i-P_i)^2,
 \quad (\sum_iq_i^2+q_1q_2q_3)'=r^3\sum_iQ_iP_i.
\]
The agent checked the scalar and Ricci identities symbolically; the
root's committed executable independently checks the complete w=0
characteristic formula. The general coupled expressions are retained
as a calculation entry point, not a new coercivity result.

For the actual hyperbolic simple-zero shell, the zero-end agent obtained
an additional Maxwell coefficient
\[
 \int|\delta(f-K)|^2=C_M(a,b)\ell^2+o(\ell^2),
\]
\[
 C_M=\pi^2\int_a^b\left\{
 \frac{16m_*^2m^2}{9(m_*+m)^4}
 +\frac{64m^3}{27(m_*+m)^3}\right\}dm.
\]
Its second term comes from angular contraction, so an axis-only
calculation is insufficient. This coefficient has not been added to
the main theorem or the independently replayed test suite. The main
text uses the fully displayed fit and shell costs instead.

## Text validation

The inherited relative-cell suite also passes all 23 tests, and the
signed-flux suite passes all 5 tests. Library verification preserves
884 baseline files and 10,191 archived source records; it reports no
byte-integrity or source-link failures. These checks do not certify PDE
existence, compactness, or historical originality.

The new proof and extended flux proof were rendered through the existing
math-node-preserving generator and compiled twice with XeLaTeX. The first
has 110 math nodes and 7 pages; the second has 118 math nodes and 9 pages.
Both reported no warnings or missing glyphs. The PDFs are
temporary validation products; editable MD and TeX are retained locally.
File-integrity checks are distinct from the analytic proofs above.
