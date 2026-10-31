# Step 78 route map: finite connector mechanisms after the VII_0 barrier

## Research position

The full Yau 26 problem is unresolved.  The graph-manifold route still separates
into (i) Einstein nonexistence on the eventual smooth manifold and (ii) a
negative almost-Einstein construction.  Step 73 supplies a low-cost expanding
tail; the missing object is a finite, constraint-compatible connector from a
reflection-type graph core into that tail.

Step 78 rules out one important apparent escape.  In the homogeneous rotating
Bianchi VII_0 ansatz, a full pointwise defect bound `||Ric+3g||<=delta<=3/5`
forces `a'/a<0`, increasing orbit anisotropy, and intrinsic curvature at least
`6-4delta` on every positive-radius slice.  Therefore it cannot approach
`S=I` or the scaled-flat Step 73 interface.  This is a robust finite-interval
barrier, not merely failure of an exact PE completion.

## What remains scientifically plausible

A successful connector must do something absent from fixed helical rotation:

1. let the orbit-shape map depend on two base variables so anisotropy energy can
   be transported spatially and diluted by expansion;
2. use the full matrix target `SL(2,R)/SO(2)`, allowing the target-space tension
   to turn rather than monotonically increase one scalar anisotropy coordinate;
3. activate off-diagonal shape/Codazzi channels while satisfying every Ricci
   component and the Hamilton and momentum equations;
4. exploit a long parameter-dependent region in which pointwise defect tends to
   zero but exponentially weighted defect moments supply finite stress.

The next construction should therefore formulate the finite forced connector
itself, not assume a complete non-ASD PE filling.  A complete reflected filling
is a useful sufficient exact model.  Li--Liu is useful as an outer-end matrix
and cusp benchmark; a usual decaying Jacobi kernel preserving the cusp end does
not open a second PE end.  Any cusp-opening analysis must be a singularly
translated transition, small on fixed compact sets and order one in a receding
inner region.

## Next mathematical object

Derive a two-base-variable `T^2`-invariant Einstein--DeTurck connector system in
variables

- base metric on `(r,z)`;
- orbit area `rho`;
- full unimodular orbit matrix `U in SL(2,R)/SO(2)`;
- DeTurck vector and all Hamilton--Codazzi components.

Retain a prescribed small defect tensor as a source, because the construction
only needs `sup|E| -> 0`, not an exact Einstein core.  Seek an energy/stress law
for
`div(rho U^{-1} grad U)` and determine whether expansion can transfer the
center-normalized order-one orbit energy to a large-weight, low-density exit
while the normal and momentum equations remain compatible.  Before large
computation, identify a finite-dimensional matrix path or asymptotic scaling
whose full residual can be evaluated analytically.  The decisive signal is a
parameter family with every normalized Ricci component tending to zero and exit
`S-I`, scaled intrinsic curvature, and attachment jets tending to zero.

If the full matrix system still has a sign-preserving potential analogous to
`K=2k^2 a^{-2}sinh^2 d`, derive it as a genuine connector obstruction.  If not,
locate the exact term that breaks the VII_0 invariant region and test whether it
can dominate at vanishing defect.

## Corrected PE side result

Under a global smooth normal foliation from center to PE end, the Riccati
comparison yields `R_gamma(x)<=-24` for the center-normalized representative.
It proves only that strict inequality occurs somewhere; equality on a single
ray is not globally excluded by Preissmann.  With `u_H=3-H`,
`w=3(1-tanh r)`, `z=u_H-w`, and `Z=e^{2r}z`, the consistent equation is

`Z' = (u_H+w)Z/3 + e^{2r}|P|^2`,

and `-R_gamma/4 = 6 + lim Z`.  This is background structure, not the main next
allocation.

## Positive branch

The mixed-chirality smooth manifold `#_3(S^2 x S^2)` has `b_+=3`, whereas a
positive Kähler--Einstein surface is del Pezzo with `b_+=1`.  Thus the mixed
case cannot be solved by a stronger KE theorem.  The peer order-three radial
coefficient remains meaningful as a test of a non-Kähler desingularization,
but it does not settle arbitrary Einstein existence or nonexistence.  Continue
to exchange exact calculations with peers without diverting this session from
the finite negative connector mechanism.

## Key files

- `workspace/notes/step78_rotating_eigenframe_barrier.md`
- `workspace/scripts/step78_bianchi_vii0_verify.py`
- `workspace/data/step78_bianchi_vii0_symbolic.json`
- `trace/ttcs/results/step78_ttcs01_verifier1_integration.md`
- `trace/ttcs/results/step78_ttcs01_generator1_integration.md`
- corrected `workspace/notes/step77_pe_scattering_correction.md`
