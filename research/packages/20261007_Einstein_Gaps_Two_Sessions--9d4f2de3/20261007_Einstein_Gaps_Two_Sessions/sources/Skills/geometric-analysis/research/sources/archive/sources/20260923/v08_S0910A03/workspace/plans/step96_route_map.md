# Step 96 route map: from local charged germ to the global matching operator

## Established

1. The radial curved-base BVP is excluded before computation: its `r`-level `T^3`
   metrics are flat, hence the `delta >= 3/2` barrier applies.
2. The charged Koiso data evolve by the full `s`-dependent Gaussian Einstein system
   `q_n=2K`, `K_n=Ric(q)+3q-HK+2Kq^{-1}K`; constraints and signs were checked.
3. Exact center Taylor coefficients are
   `H_n=3-S`, `a_nn=-3-S-Q(s)`, `sigma_nn=6+Q(s)`.  For `S=1`, both outward
   sides initially expand, while the base circle contracts and orbit area expands.
4. The `N=96`, `n<=0.02` spectral evolution matches those coefficients and has
   Hamiltonian/momentum residuals `1.32e-4/2.29e-4`; it is short-collar evidence,
   not global continuation.
5. A compactly supported fixed-charge `K_X` numerator vanishes by algebraic
   integration by parts, independently of Noether.  The corrected relative ratio is
   about `4.8e-11`; this is a null control and implementation check, not an
   obstruction.

Full record: `workspace/notes/step96_charged_koiso_local_evolution_and_joint_matching.md`.

## Decisive object

Construct the gauge-fixed full residual map on `R x S^1`:

`E(V)=(H,T,Z,Bmix)` for `V=(phi,sigma,U,q,A;p)`, retaining every `s` mode,
Coulomb/conformal gauge, both expanded ends, and one shared charged-Koiso center.
Use the mixed-order principal block:

- `DT ~ Delta dot_sigma`,
- `DZ ~ Delta dot_U`,
- `D trH ~ -2 Delta dot_phi-Delta dot_sigma`,
- `DBmix ~ d dot_q`.

The principal symbol is already injective: the scalar/map block determinant is
`-2|xi|^8` and the full overdetermined Gram determinant is `4|xi|^20` with rank six
(`step96_linear_matching_symbol.py/.json`). Determine next its indicial roots,
Fredholm index, kernel, and cokernel on a compactified cylinder. Do not invent a
second-order equation for charge.

## Independent projections

The finite matching map must combine, rather than duplicate:

1. vector charge flux on each side;
2. end connection holonomies;
3. weighted TT/Hopf projections of traceless horizontal error;
4. global adjoint Noether fields spanning center to ends;
5. three target-Killing currents;
6. both halves' Dirichlet-to-Neumann data matched to the same center parameters
   `(S, charge, target phase/frame)`.

`X=grad sigma` is excluded as an independent projection because at fixed charge it
is the area equation tested against `Q`.

## Next computation

Build the *linearized* compactified Fourier--Chebyshev operator first.  Continue in
outer truncation `R` and resolutions `(N_tau,N_s)`, computing the smallest singular
values and normalized left/right singular fields with all blocks and gauges present.

- `s_min(R) ~ exp(-3R)` with a right mode localized in a distant charge taper and a
  left mode escaping/growing: redshift near-kernel, favoring construction.
- `s_min -> s_*>0` or a bounded left mode with nonzero center pairing: finite global
  obstruction suitable for proof.

No nonlinear two-end BVP should be attempted before this operator and its parameter
count are verified.  The unrestricted Yau-26 problem remains open; this is one
symmetry-class negative connector mechanism only.
