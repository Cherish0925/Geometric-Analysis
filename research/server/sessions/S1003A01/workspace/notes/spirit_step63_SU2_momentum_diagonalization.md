# Spirit follow-up to Step 63: the non-diagonal SU(2) fallback is not additional Einstein freedom

This is a short geometric reduction for Core to check and integrate with the Step-63 regular-nut theorem. The same claim was already stated, without this derivation, in `step56_soldered_instanton_and_SU2_AKE.md`, §5. It concerns Riemannian SU(2) principal orbits and full invariance of the pair, not Bianchi VIII or noninvariant almost-Kähler forms.

## Mixed Einstein equation

On a principal interval choose the normal-geodesic gauge

 g=dt^2+H_ij(t) sigma_i sigma_j,

where H is a positive symmetric matrix and the fixed SU(2) Maurer–Cartan coframe satisfies d sigma_i=2 sigma_j wedge sigma_k. The cross terms with dt vanish in this gauge; the identification of the orbits is fixed by the normal geodesics.

At an arbitrary regular time t0, apply one constant SO(3) Lie-algebra automorphism to diagonalize H(t0), with diagonal entries a_i^2. In the orthonormal Milnor frame on that orbit, the symmetric second fundamental tensor has components

 K_ij=H'_ij/(2 a_i a_j).

Write the structure constants as [E_j,E_k]=n_i E_i, cyclically, with n_i=-2a_i/(a_ja_k) for the displayed Maurer–Cartan sign. The spatial connection satisfies nabla_{E_j}E_j=0, and direct Koszul calculation gives

 (div K)_i=(n_k-n_j) K_jk.

The sign in the Codazzi identification of Ric(∂t,E_i) is convention-dependent, but its vanishing is not. Einsteinity therefore gives

 (a_j^2-a_k^2) H'_jk=0

for each cyclic pair. Equivalently, in the fixed structure-constant Euclidean inner product,

 [H,H']=0.

The trace of K is spatially constant, so no omitted spatial derivative of tr K contributes to this constraint.

## One fixed frame, including repeated eigenvalues

At t0, H and H' are commuting real symmetric matrices. A constant SO(3) transformation diagonalizes them simultaneously; within a repeated eigenspace of H, simply diagonalize H'.

On H>0 the spatial Einstein equations constitute a smooth second-order ODE for H. Its diagonal subspace is invariant: the intrinsic Ricci tensor of a diagonal SU(2) orbit metric is diagonal, and the velocity terms preserve diagonality. Local uniqueness therefore keeps H diagonal in that single fixed frame. Continuing along the principal interval removes any concern about eigenvalue crossings. One does not need to transport a potentially singular eigenframe through them.

Thus non-diagonal Riemannian SU(2)-invariant Einstein metrics on this interval provide no extra geometric branch beyond the diagonal system. The singular nut endpoint does not interfere: establish the reduction at t0>0 and then apply the smooth nut extension in the same constant frame.

## Consequence for the current construction problem

A fully SU(2)-invariant two-form remains invariant after a constant Lie-algebra automorphism. In the diagonal metric it has exactly the general coefficient representation already used in Step 63. For the smooth nonzero limiting almost-Kähler form, use the nut chirality selected in that theorem.

Accordingly, after verifying this standard Codazzi reduction, the Step-63 conclusion is rigidity of the fully SU(2)-invariant regular-nut Einstein–almost-Kähler pair, not merely failure of a diagonal metric restriction. A large non-diagonal matrix recurrence would reproduce the same constraint in redundant variables.

This does not rule out an SU(2)-invariant Einstein metric carrying a noninvariant almost-Kähler form, a smaller symmetry group, or an unrestricted germ. Those are genuinely different representation choices. The unrestricted Step-62 cone and its finite-order evidence are unchanged. This reduction should prevent route churn within the same symmetric class, not be promoted into general local Goldberg rigidity.
