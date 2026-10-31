# Eguchi--Hanson outer flux is not killed by pointwise P-criticality

Internal calculation for the reduced-energy continuation. This is a statement about the local first-variation concomitant, not a construction of a global P-critical metric.

Write `P(g)=integral |E_g|^2`, `E=Ric-sg/4`. In Euclidean four-space let J be orthogonal, J^2=-I, with J pairing (e1,e2) and (e3,e4). The leading Eguchi--Hanson tail in radial coordinates is

\[
h_{ij}(x)=\frac{x_ix_j-(Jx)_i(Jx)_j}{r^6}
=\frac18\bigl(\partial_i\partial_j-J_i{}^kJ_j{}^l\partial_k\partial_l\bigr)r^{-2}.
\]

It is trace-free, divergence-free and harmonic away from the origin, of homogeneity -4. Its coefficient in a gluing at length a is a^4, up to the chosen bolt normalization.

Use the distributional extension given by the displayed derivatives. Since `Delta r^{-2}=-4 pi^2 delta_0`, direct computation gives

\[
\partial_i h_{ij}=-\frac{\pi^2}{2}\partial_j\delta_0,
\quad
D\operatorname{Ric}^{\circ}_e(h)_{ij}
=-\frac{\pi^2}{4}(\partial_i\partial_j+J_i{}^kJ_j{}^l\partial_k\partial_l)\delta_0
+\frac{\pi^2}{8}\delta_{ij}\Delta\delta_0.
\]

For a smooth trace-free divergence-free test tensor E this yields

\[
\langle D\operatorname{Ric}^{\circ}_e(h),E\rangle
=-\frac{\pi^2}{4}J_i{}^kJ_j{}^l\partial_k\partial_l E_{ij}(0).
\]

This is **not** a multiple of `Delta E`. Accordingly it is not annihilated by the principal P-critical equation.

An explicit example fixes the distinction. Set

\[
f=x_1^2-x_3^2,\qquad A=\operatorname{diag}(0,1,0,-1),\qquad E=fA,
\]

\[
H_4=-\frac{x_1^4-x_3^4}{6}A.
\]

Then

\[
\operatorname{tr}H_4=0,\quad\operatorname{div}H_4=0,\quad
D\operatorname{Ric}^{\circ}_e(H_4)=-\tfrac12\Delta H_4=E,
\]

\[
\operatorname{tr}E=0,\quad\operatorname{div}E=0,\quad\Delta E=0,
\qquad J_i{}^kJ_j{}^l\partial_k\partial_l E_{ij}=4.
\]

Thus H4 is an infinitesimal P-critical deformation of the flat metric (`2 L* L H4=0`) whose fourth-jet contribution to the EH flux is nonzero. In particular its two-jet is zero; local curvature-squared expressions cannot record this term.

The boundary normalization can be checked without distributions. For radial outward normal on S^3, trace-free/divergence-free fields have Green concomitant

\[
\mathcal B(E,h)=-\frac12\int_{S^3}
\{E_{ij}\partial_r h_{ij}-h_{ij}\partial_rE_{ij}\}\,dS.
\]

The respective homogeneities are 2 and -4; using spherical moments gives

\[
\int_{S^3}\langle E,h\rangle=-\frac{\pi^2}{3},\qquad
\mathcal B(E,h)=-\pi^2.
\]

On a punctured closed outer region the inner normal reverses the sign. Its first variation of P therefore contributes `+2 pi^2 epsilon a^4` for the jet `epsilon H4`, divided by the order of the local quotient group. Both signs of epsilon are permitted by this local principal compatibility. This is **not** an asserted coefficient for an existing global gluing: the full curved concomitant also has lower-jet curvature terms and must be matched to the inner construction.

## What this rules out and what remains

One cannot infer from `grad P(g0)=0` that the puncture flux of a singular ALE-tail variation vanishes. That inference discards the Green concomitant. At an Einstein background E vanishes identically, so this particular flux does vanish. At a general non-Einstein P-critical background, neither criticality nor E(p)=0 alone removes its derivative contributions.

A universal obstruction-square reduced energy would require an additional identity forcing the *full* fourth-jet flux to combine with the renormalized inner contribution. The local P-critical principal equation is insufficient. A global minimization/stability condition could add information, but must be invoked and proved separately.

## Closely related verified primary result

Tristan Ozuch, *Integrability of Einstein deformations and desingularizations*, arXiv:2105.13193, Theorem 0.4 (=4.6) and Remark 0.5, identifies mixed H2 / H^4 trace-free Ricci obstructions for an Einstein orbifold and an integrable Ricci-flat ALE bubble. They involve the ALE reduced volume and the r^-6 asymptotic Weyl curvature. The latter is not the Weyl value at the conformal compactification point, which vanishes for order-four ALE ends. This supplies a relevant conserved-flux framework, but its theorem concerns Einstein desingularizations and does not assert positivity of reduced P on non-Einstein P-critical orbifolds.

Source: https://arxiv.org/pdf/2105.13193
