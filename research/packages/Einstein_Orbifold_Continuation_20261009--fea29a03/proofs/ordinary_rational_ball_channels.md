# Ordinary ASD rational-ball channels on every single blow-up

Date: 2026-10-09. This note answers the concrete topological question left after the 2026-10-08 spherical-lattice exclusion. It uses classical embedding and ALE existence theorems, with their orientations retained. It does not assert that the constructed degenerating sequences minimize P.

## 1. The ordinary orientation is not excluded

**Proposition.** For every closed oriented smooth four-manifold X, the smooth manifold

\[
M=X\#\overline{\mathbb {CP}}^{,2}
\]

contains, orientation-preservingly, the standard rational ball B_{n,1} for every odd integer n>=3. In particular this is true if X is aspherical. Each inclusion induces the zero map from pi_1(B_{n,1})=Z_n into pi_1(M).

**Proof.** A nonsingular complex conic in CP^2 is an embedded sphere of self-intersection +4. Reversing the ambient orientation gives an embedded sphere C in CPbar^2 of square -4. Choose the connected-sum ball disjoint from C. Its normal disk bundle V_{-4} then embeds in the CPbar^2 summand of M. Khodorovskiy's Theorem 1.3 gives an orientation-preserving smooth embedding

\[
B_{n,1}\hookrightarrow V_{-4}\qquad(n\ge3\text{ odd}).
\]

For n=3 this already follows from her Theorem 1.2, with n+1=4. Composition proves the claimed embedding. Since V_{-4} retracts onto a two-sphere, its fundamental group is trivial; hence the induced map on pi_1 factors through zero. No ambient fundamental-group injectivity has been assumed. QED.

These are the usual rational balls with boundary L(n^2,n-1) in the negative-plumbing convention, rather than their orientation reversals. The embedding theorem is a classical smooth theorem, not a new construction here. The fact that some such embeddings cannot be symplectic does not exclude their use by unrestricted Riemannian competitors.

## 2. The embedded cores carry zero-P ALE geometries

By Suvaina's Theorem A and Proposition 3.3, the interior N_n of B_{n,1}, equivalently the Q-Gorenstein smoothing of the cyclic quotient singularity 1/n^2(1,n-1), carries a complete ALE Ricci-flat Kähler metric. Its invariants are

\[
\chi(N_n)=1,\quad b_2(N_n)=0,\quad
\pi_1(N_n)=\mathbb Z_n,\quad |\Gamma_\infty|=n^2.
\]

Use the complex orientation. Scalar-flat Kähler in real dimension four implies W^+=0; thus

\[
P(N_n)=0,\qquad W_+(N_n)=0,\qquad
\int_{N_n}|W^-|^2=8\pi^2(1-n^{-2}).
\]

The last identity is the ALE Gauss-Bonnet formula in the project's curvature-operator normalization. For n=3 the full curvature integral is 64 pi^2/9. This is the opposite curvature orientation from the embedded -B_2 used in the previous note, and is precisely the orientation invisible to the positive-hand Weyl budget.

## 3. Actual smooth degeneration on the fixed manifold

Collapse the specified B_{n,1} to its standard flat quotient cone and denote the resulting compact orbifold by O_n. Its single singularity has local group 1/n^2(1,n-1). For any smooth orbifold metric g_0 on O_n there exist smooth metrics g_a on the same fixed manifold M such that

\[
g_a\longrightarrow g_0\quad\text{smoothly away from the singular point},
\qquad P(g_a)\longrightarrow P_{\rm orb}(g_0),
\]

and N_n is the rescaled bubble.

Here is the complete cutoff estimate. In orbifold normal coordinates write g_0=delta+h_0, with D^j h_0=O(r^{2-j}). Suvaina's ALE model has order-four decay; after scaling by a^2 its correction h_N satisfies D^j h_N=O(a^4 r^{-4-j}), j<=2. On the annulus r_a<=r<=2r_a, r_a=a^{1/2}, interpolate with a fixed radial cutoff. Its curvature is bounded by C(1+a^4 r_a^{-6}), hence uniformly bounded. The annulus has volume O(r_a^4), and its P integral is o(1). The inner exact ALE region is Ricci-flat and contributes zero to P. The omitted orbifold ball also contributes o(1). This proves the asserted P convergence. Since r_a/a tends to infinity, the rescaled interior exhausts N_n. Constants may depend on the chosen n and the fixed bulk metric; no uniform-in-n gluing statement is needed.

In particular,

\[
P_*(M)\le P_{*,\rm orb}(O_n).
\]

This inequality alone does not imply equality or produce a minimizing degeneration.

## 4. Why the reversed-bubble exclusion does not extend

Put e_n=1-n^{-2}. The ordinary ASD bubble has Euler curvature integral e_n and signature curvature integral -2e_n/3. Therefore

\[
\chi_{\rm orb}(O_n)=\chi(M)-e_n,
\qquad \tau_{\rm curv,orb}(O_n)=\tau(M)+\frac23e_n.
\]

Consequently

\[
\boxed{(2\chi+3\tau)_{\rm curv,orb}(O_n)=(2\chi+3\tau)(M).}
\]

This exact cancellation distinguishes ordinary ASD bubbles from the reversed B_2 bubble, where the positive-hand topological curvature combination decreased by 3. Real cohomology and its pairing are unchanged by replacing a rational ball by its cone.

Thus even if both actual classes K+E and K-E transfer to O_n with projected budget at least A, the classical monopole bound is only

\[
P_{\rm orb}\ge8\pi^2\{\tfrac23 A-(A-1)\}
=8\pi^2(1-A/3).
\]

It provides none of the additional 3 units in the reversed-B_2 bound. There is no hidden factor n that strengthens this estimate as the quotient order grows. For A>3 the displayed lower bound is negative and adds nothing to nonnegativity; for smaller A it remains below the standard 8 pi^2 threshold.

## 5. Consequence for the attainment strategy

The single-blow-up spherical lattice excludes all embedded positive-b_2 cores in Wright's half-conformally-flat Ricci-flat ALE class, but does not eliminate that class entirely. The ordinary rational-ball branch survives as an actual smooth embedding and an actual smooth Riemannian degeneration, for all odd n>=3. This is not merely a formal matrix or energy budget.

The separate statement that -B_2 compact-orbifold limits are excluded below 8 pi^2 for A<=9 remains unaffected. It cannot be promoted to an exclusion of all zero-P bubbles. To obtain smooth attainment, an argument must use additional information about a genuine minimizing sequence or show a strict variational improvement over the relevant orbifold boundary. Topology and the inherited positive-hand projection budget alone do not provide that conclusion.

## Sources checked in the original papers

1. Tatyana Khodorovskiy, *Smooth Embeddings of Rational Homology Balls*, Topology and its Applications 161 (2014), 386-396; arXiv:1212.4391. Theorems 1.2 and 1.3 are on PDF page 2. The proof of Theorem 1.3, PDF pages 8-12, gives the actual oriented Kirby construction. PDF page 13 states that these odd-n rational balls are spin. https://arxiv.org/pdf/1212.4391
2. Ioana Suvaina, *ALE Ricci-flat Kahler metrics and deformations of quotient surface singularities*, arXiv:1102.2672. Theorem A, Definition 1.1 (order-four ALE decay), and Proposition 3.3 (the rational-ball metrics with end L(n^2,nm-1)) supply the geometry. https://arxiv.org/pdf/1102.2672
3. Heesang Park, Jongil Park and Dongsoo Shin, *Smoothly embedded rational homology balls*, arXiv:1508.03724, Proposition 4.4, gives a second proof of Khodorovskiy's odd-n embedding using complex threefold methods. https://arxiv.org/pdf/1508.03724

Web retrieval IDs for the parent: turn851view0 (Khodorovskiy full paper), turn851view1 and turn852view0 (Suvaina full paper and exact statements), turn851view2 (Park-Park-Shin full paper). The first two classical ingredients are being combined for this project's degeneration question, not claimed as newly discovered mathematical theorems.
