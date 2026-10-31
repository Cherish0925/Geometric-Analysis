# First-line advance: energy exclusion, variable calibration and global periods

23 September 2026. Baseline: `8113dd1` (the preceding composition package).

## 1. A new global energy exclusion on actual smooth manifolds

For the actual polarized-monopole family
\[
 M=X\#k\overline{\mathbb{CP}}^{\,2}\#m(S^1\times S^3),\quad
 A=c_1^2(X)>0,\quad h=(k+4m)/A\in(0,1/3),
\]
put
\[
 e=\frac{\int|\operatorname{Ric}|^2}{8\pi^2A},\qquad
 F(h)=\frac{(4-\sqrt{1-3h})^2}{9}.
\]
The [energy-envelope theorem](line1_energy_envelope_gap.md) proves
\[
 \mathcal E(g)+(e-F(h))_+\ge\varepsilon h^2
\]
with a universal positive constant and the full relative Einstein defect
(all nonzero target signs). In particular every Einstein metric, if
one exists, has \(e\ge F(h)+\varepsilon h^2\). Positive and zero
Einstein constants are excluded separately by the actual scalar
monopole bound.

The classical optimization already gives \(e\ge F(h)\) for Einstein
metrics. The new differential input makes the separation uniform and
stable under integral Ricci error. Parameter eight alone loses the
energy coordinate in Chern--Weil; selecting a parameter depending on
\(h\) restores it. This is an actual application, not merely a list
of functional parameters. For
\((\Sigma_2\times\Sigma_2)\#2\overline{\mathbb{CP}}^{\,2}\),
the bound is \(e\ge49/36+\varepsilon/16\) for every hypothetical
Einstein metric.

It is a global restriction on all outputs, not an exclusion of all
outputs. A separate energy upper bound would be needed for nonexistence.

## 2. The calibration amplitude may now vary in space

The [sourced identity](line1_variable_calibration.md) handles
\[
 A=t(x)\left(\tfrac23I-\omega\otimes\omega\right),\qquad
 |\omega|^2=2,
\]
without discarding derivatives of \(t\). Its conformal kernel is
absorbed by \(\widehat g=|t|^{2/3}g\).

The [negative-branch selection theorem](line1_variable_negative_selection.md)
adds a global coercive scalar test. For \(0<m\le t\le M_0\),
\[
 \fint\left(|dt|^2+(t-\tfrac12)^2+|\nabla\omega|^2\right)
 \le C_{m,M_0}\left(d+\sqrt{dH_2}\right),
\]
where \(d=\fint(|\operatorname{Ric}+g|^2+|W^+-A|^2)\) and
\(H_2=\fint|\nabla^2A|^2\). No scalar spectral gap is used:
the restoring term comes from the negative scalar-curvature equation.
Uniformly negative \(t\) instead forces \((1+H_2)d\ge c_m>0\).

This removes a constant-amplitude restriction of the earlier analytic
criterion. It does not remove the nonvanishing eigenline or joint
derivative-budget requirements. The exact conformal-Kähler implication
is classical; the present research contribution is the sourced integral
estimate and its negative-branch stability argument.

## 3. Multiple actual classes constrain global positive cup directions

The [period-inertia theorem](line1_period_inertia.md) uses simultaneous
endpoint saturation for actual conformally solvable classes. It gives
signed alignment of their positive harmonic projections and a matrix
decomposition
\[
 Q=q_1\alpha\alpha^{\mathsf T}+R-N,\quad R,N\ge0,
 \quad\operatorname{tr}R\le(m-1)J,
\]
where \(Q\) is their normalized cup-product matrix and
\[
 J=\left(300\sqrt\kappa+
                  12\sqrt{(13\kappa+4\sqrt{2\kappa})/\lambda_1}\right)^2.
\]
Thus \(\nu_2(Q)\le(m-1)J\). Two robust positive cup directions
force either non-small endpoint defect or scalar spectral degeneration.
Unlike the earlier equal-positive-square argument, this deduction does
not require equal class squares, a topological-square lower bound or a
negative-square budget. The uncontrolled negative Gram matrix is retained.
Its spectral dependence is explicit; no new all-metrics topological
nonexistence result follows without further input.

## Mathematical inheritance and verification

All three developments use the Skill's fixed normalization and preserve
the actual-class requirements. The previous main paper and original
derivations remain unchanged in this snapshot. These are research
manuscripts, not a claim that Yau26 has been solved or that publication
priority has been exhaustively established.

New checks target the new first-jet identities, weighted scalar algebra,
energy-envelope reduction and period-matrix argument. They do not rerun
the historical archive as a substitute for research. The proofs, TeX,
PDFs and exact outputs are included. Run
`python verify_line1_advance.py --output NEW_DIRECTORY` with SymPy.

No live Session, model configuration, service or installed v08/v09 Skill
was modified.
