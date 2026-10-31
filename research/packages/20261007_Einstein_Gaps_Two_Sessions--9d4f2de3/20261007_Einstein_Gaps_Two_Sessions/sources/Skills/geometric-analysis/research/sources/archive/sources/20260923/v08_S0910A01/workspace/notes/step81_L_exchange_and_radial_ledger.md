# Step 81: single-factor antipodal exchange symmetry and the radial scale ledger

Session `S0910A01`. Agent3 / Actuator. Phase Execute.

## Purpose

Step 80 reduced the positive mixed-row product-orbifold construction to the even radial equations after the exact `A` and `J` symmetries removed the odd scalar modes and the transverse bubble projections.  This note records the next executable correction: the remaining radial response has the scale form
\[
F_i(t_1,t_2)=t_i\sum_j B_{ij}t_j^2+R_i,
\]
not `\sum_j B_{ij}t_j^3`.  The receiver factor `t_i` is part of Ozuch's finite-dimensional equation, while a source bubble contributes `t_j^2` through its `H^4` asymptotic and the corresponding regular Green response.

The note also verifies the single-factor antipodal symmetry
\[
L(x,y)=(-x,y)
\]
for the diagonal mixed chirality assignment.  This symmetry exchanges the two `A`-orbits of nodes and swaps four-dimensional orientation, hence exchanges `\Lambda^+` and `\Lambda^-`, exactly matching the opposite EH chiralities in the mixed row.

This remains a local desingularization computation around `(S^2\times S^2)/\langle(r_\pi,r_\pi)\rangle`; it is not a theorem about Einstein existence on the resulting smooth manifold and does not resolve Yau Problem 26.

## 1. Verified linear action of `L`

Use an oriented product tangent frame `(e_1,e_2,e_3,e_4)` near a node, with the first two directions tangent to the first sphere and the last two directions tangent to the second sphere.  In compatible frames at source and target nodes, the derivative of `L` is represented by
\[
D L=\operatorname{diag}(1,-1,1,1),\qquad \det(DL)=-1.
\]
Therefore `L` reverses the four-dimensional orientation and identifies `\Lambda^+` at the source with `\Lambda^-` at the target.

The script

`Sessions/S0910A01/workspace/scripts/step81_L_symmetry_scale_ledger.py`

produced

`Sessions/S0910A01/workspace/data/step81_L_symmetry_scale_ledger.json`.

The exact basis transport is
\[
\omega_1^+\mapsto -\omega_1^-,\qquad
\omega_2^+\mapsto \omega_2^-,\qquad
\omega_3^+\mapsto \omega_3^-,
\]
and conversely
\[
\omega_1^-\mapsto -\omega_1^+,
\qquad \omega_2^-\mapsto\omega_2^+,
\qquad \omega_3^-\mapsto\omega_3^+.
\]
Thus the rank-one curvature block transports correctly:
\[
R^+=\operatorname{diag}(1,0,0)\quad\longmapsto\quad
R^-=\operatorname{diag}(1,0,0),
\]
and the radial insertion direction has sign `+1`:
\[
\omega_2^+\longmapsto\omega_2^-.
\]

The same script records that `L` commutes with the quotient local action `\sigma=-I_4`, with `J`, and with the representative tangent action of `A`.  Globally this is also direct: all maps are factorwise sign, half-turn, or reflection maps on the two round spheres.

## 2. Node and chirality transport

Write `N=+1`, `S=-1`.  The diagonal mixed chirality assignment is
\[
\epsilon(NN)=\epsilon(SS)=+1,
\qquad
\epsilon(NS)=\epsilon(SN)=-1.
\]
Equivalently `\epsilon(s_1,s_2)=s_1s_2`.  Then
\[
A(s_1,s_2)=(-s_1,-s_2),\qquad
L(s_1,s_2)=(-s_1,s_2),
\]
so `A` preserves chirality and exchanges nodes inside each orbit, while `L` reverses chirality and exchanges the two `A`-orbits:
\[
\{NN,SS\}\longleftrightarrow\{NS,SN\}.
\]
Because `L` also swaps `\Lambda^+` and `\Lambda^-`, it is compatible with transporting positive EH insertions on the diagonal orbit to negative EH insertions on the off-diagonal orbit.  This compatibility is geometric, not an algebraic relabelling only.

## 3. Full angular `H^4` transport, not frozen `rho`

Step 79 showed that the frozen `rho` substitution is false.  The `L` symmetry was therefore tested using the actual angular formula.  With conventions
\[
H^4_+(\omega_2^+)=-\frac1{2r^4}\sum_j\rho^-_j(x)(\omega_j^-\circ\omega_2^+),
\quad
\rho^-_j(x)=\frac{x^T(\omega_2^+\circ\omega_j^-)x}{|x|^2},
\]
and
\[
H^4_-(\omega_2^-)=-\frac1{2r^4}\sum_j\rho^+_j(x)(\omega_j^+\circ\omega_2^-),
\quad
\rho^+_j(x)=\frac{x^T(\omega_2^-\circ\omega_j^+)x}{|x|^2},
\]
the script

`Sessions/S0910A01/workspace/scripts/step81_L_H4_transport.py`


A further check addresses the TTCS normalization concern.  Ozuch's asymptotic kernel formula (lines 366--371) gives
\[
\mathbf o_1(\zeta^+)=\frac{\zeta_{(1)}^+\circ\rho(\zeta)^-}{r^4}+O(r^{-8}),
\]
with the analogous negative-orientation formula from lines 372--376.  The script

`Sessions/S0910A01/workspace/scripts/step81_L_radial_tensor_transport.py`

produced

`Sessions/S0910A01/workspace/data/step81_L_radial_tensor_transport.json`.

It verified on 20,000 samples that
\[
L^*O_{\rm rad}^-(Lx)=O_{\rm rad}^+(x)
\]
for the complete leading radial asymptotic tensor, with maximum transport error `0.0`.  Thus, when the radial kernel is defined as the EH-family derivative in the `\omega_2` scale direction and both chiralities use the same `L^2` or flux normalization convention, the radial projection transport factor is `+1`.  This is still a leading-asymptotic check; the full Lyapunov--Schmidt proof must impose the same transported normalization on the global obstruction functionals.
produced

`Sessions/S0910A01/workspace/data/step81_L_H4_transport.json`.

On 20,000 random samples of `S^3`, the maximum transport error was exactly zero in floating arithmetic for both the component vector and the full tensor:
\[
\max|\rho^+(Lx)-L_*(\rho^-(x))|=0,
\qquad
\max|L^*H^4_-(Lx)-H^4_+(x)|=0.
\]
The transported component relation in these bases is
\[
\rho^+(Lx)=\operatorname{diag}(-1,1,1)\rho^-(x).
\]
This confirms that the single-factor antipodal symmetry is compatible with the complete spatial angular dependence of Ozuch's `H^4` term.

## 4. Consequence for the reduced radial equations

Let `F_1` denote the radial projection for orbit `\{NN,SS\}` and `F_2` the radial projection for orbit `\{NS,SN\}`.  With the radial projection basis transported by `L`, the symmetry gives
\[
F_2(t_1,t_2)=F_1(t_2,t_1).
\]
This relation does not make the two equations identical at arbitrary relative scales.  It relates the two functions after exchanging the scale variables.

The candidate cubic contribution must keep the receiver scale:
\[
F_i(t_1,t_2)
=t_i\bigl(B_{i1}t_1^2+B_{i2}t_2^2\bigr)+R_i.
\]

## 5. Orbit combinatorics of the candidate `B` coefficients

A separate executable check

`Sessions/S0910A01/workspace/scripts/step81_radial_B_combinatorics.py`

produced

`Sessions/S0910A01/workspace/data/step81_radial_B_combinatorics.json`.

For representative receiver `NN` in orbit 1, the four possible sources contribute as follows:

| source | relation | geometry | candidate scale | leading interpretation |
|---|---|---|---|---|
| `NN` | local self | local | `t_1 t_1^2` | local higher radial self-response after `\mu_1=0` |
| `NS` | cross orbit | adjacent | `t_1 t_2^2` | opposite-chirality adjacent Green response |
| `SN` | cross orbit | adjacent | `t_1 t_2^2` | opposite-chirality adjacent Green response |
| `SS` | same orbit companion | diagonal | `t_1 t_1^2` | same-chirality regular response; leading chirality-split kernel block expected zero, but higher/gauge terms must be tracked |

For representative receiver `NS` in orbit 2 the same table is transported by `L`.  Thus, in single-representative or orbit-averaged normalization,
\[
F_1=t_1\bigl((s+d)t_1^2+2c t_2^2\bigr)+\cdots,
\qquad
F_2=t_2\bigl(2c t_1^2+(s+d)t_2^2\bigr)+\cdots.
\]
Here `s` denotes the local self coefficient, `d` the same-orbit diagonal/same-chirality companion contribution, and `c` one adjacent opposite-chirality cross contribution.  Therefore
\[
a=s+d,\qquad b=2c
\]
for the exchange-symmetric matrix.  A useful correction follows: for the opposite-corner spin row, the cross-orbit mixed-chirality sources are all adjacent; the diagonal geometry occurs in same-orbit same-chirality companion pairs.  Since same-chirality leading kernel-block shifts are expected to vanish by the chirality split, it is plausible that `d` vanishes at the first Green-response layer, but this must be proved in the complete projected expansion rather than assumed.
The `L` relation then forces
\[
B=\begin{pmatrix}a&b\\ b&a\end{pmatrix}
\]
provided the two radial obstruction functionals are normalized by `L`-transport.  The linear-form check `\omega_2^+\mapsto\omega_2^-` fixes the sign of the insertion direction, but a complete proof of the `+1` factor must also transport the full EH radial kernel/obstruction tensor and its flux or `L^2` normalization; by naturality one expects
\[
L^*\mathbf o_{\mathrm{rad}}^- = \mathbf o_{\mathrm{rad}}^+,
\]
when `\mathbf o_{\mathrm{rad}}` is defined as the derivative of the EH family in the `\omega_2` scale direction.

For positive scales, division by `t_i>0` gives the candidate leading equation
\[
\begin{pmatrix}a&b\\ b&a\end{pmatrix}
\begin{pmatrix}t_1^2\\t_2^2\end{pmatrix}=0.
\]
Writing `x=t_1^2>0`, `y=t_2^2>0`, the two equations are `ax+by=0` and `bx+ay=0`; adding gives `(a+b)(x+y)=0`.  Thus a positive-scale kernel requires `a+b=0`.  If `a=-b\ne0`, then `x=y`, so any surviving nonzero-matrix branch is asymptotically equal-scale.  If `a=b=0`, the whole candidate cubic matrix vanishes and the next order must be computed.  The exchange symmetry alone does not imply any of these cancellations.

## 6. What the coefficients must contain

The self coefficient `a` and cross coefficient `b` are not bare pointwise values of `H^4`.  They are coefficients in a projected expansion after the lower-order `A+J+det` cancellations.  They should include, in the same normalization:

1. local self-response at one node, including the next radial term after the determinant cancellation of `\mu_1`;
2. regular inter-node response: a source at node `j` has size `t_j^2`, the product resolvent transports its singular-subtracted source to a regular second jet at node `i`, and the receiver first obstruction contributes `t_i`;
3. even responses from the surviving shape direction `g_1-g_2` and any other nonkernel modes in the chosen slice;
4. Bianchi/DeTurck corrections and cutoff/matching contributions;
5. any powers or logarithmic factors arising from the refined projected expansion.

The current Ozuch necessary estimate
\[
t_i\lambda_i+t_i^2\mu_i=O(t_{\max}^{5/2})
\]
is not sharp enough to expose an order-three response at comparable scales.  Remark 2.11 in the Ozuch source also warns that higher asymptotic terms such as `H_4^4` can contain logarithms, so the first true even radial layer might involve `t_i t_j^2\log t_j` or related scale-log terms rather than a pure constant matrix.  The mathematical task is therefore to build a projected expansion of the form
\[
F_i(t_1,t_2)=t_i\sum_jB_{ij}t_j^2+o\bigl(t_i(t_1^2+t_2^2)\bigr)
\]
on a comparable positive scale cone, or else to identify the actual intervening powers and logarithms.  The coefficients `a,b` are useful only when their status in this refined expansion is explicit.

## 7. Relation to the broader Yau--26 work

This symmetry does not produce an Einstein metric.  It reduces the positive mixed-row desingularization problem to two numerical/geometric radial coefficients and a sharper expansion problem.  A controlled nonzero value at the first true radial order would obstruct this particular comparable-scale, `A+J`-equivariant degeneration.  A cancellation would open the next radial equation, not by itself yield a nonlinear solution.

The full Yau Problem 26 remains open.  The restricted IL negative-gap theorem, graph-neck negative laboratory, and A02's positive Einstein topology tests are separate live research fronts.  The present value of the mixed-row calculation is that it probes whether tight positive near-Einstein orbifold degenerations are naturally completed by exact positive Einstein metrics or instead encounter a robust even radial obstruction.

## 8. Files

- `workspace/scripts/step81_L_symmetry_scale_ledger.py`
- `workspace/data/step81_L_symmetry_scale_ledger.json`
- `workspace/scripts/step81_L_H4_transport.py`
- `workspace/data/step81_L_H4_transport.json`
- `workspace/scripts/step81_radial_B_combinatorics.py`
- `workspace/data/step81_radial_B_combinatorics.json`
- TTCS verification: `trace/ttcs/results/step81_ttcs01_verifier1_integration.md`
- Previous structural note: `workspace/notes/step80_J_equivariant_all_order_reduction.md`
- Previous angular repair: `workspace/notes/step79_angular_rho_and_tilt_repair.md`
