# Spirit follow-up to Step 62: a global consequence for clean torsion-zero surfaces

This is a short consequence proposed for Core's independent integration. It uses the proved Step-62 cone together with the primary AAD bundle and canonical-curvature identities, not numerical completeness of the cone or a new higher-order identity. It makes no priority claim and does not resolve singular or isolated torsion zeros.

## Proposition

Let (M^4,g,J,Omega) be Einstein almost-Kähler with scalar curvature s != 0. The ambient manifold need not be compact. There is no closed smooth embedded surface C contained in Z={T=nabla Omega=0} on which nabla T is everywhere nonzero.

In particular, a compact clean two-dimensional torsion-zero component is impossible. Here clean means ker(DT_p)=T_p C and rank_R(DT_p)=2 along C. The slightly stronger formulation above implies cleanliness along the given surface from the cone.

## Proof

At a torsion zero use Step 62's first-jet coefficients

f(z)=c z+B bar(z),  B=S+A,  S^T=S,  A^T=-A,

with

||A||^2=8|c|^2+||S||^2,

det_R Df=9|c|^4+|det B|^2.

Since T vanishes identically on C, every tangent vector to C lies in ker(DT). Thus DT is singular. The determinant formula gives c=0 and det B=0. Since DT is nonzero by hypothesis, B is a nonzero complex rank-one matrix. Consequently DT has real rank two and its kernel is a J-complex line. Its kernel equals TC. In particular C is J-invariant, has its J-induced orientation, and Omega|_C is the positive induced area form. This uses no transverse holomorphicity or integrability of J on a neighborhood.

The same cone gives A != 0. The exact curvature dictionary of Step 62 therefore gives

eta=0,  W_3^+ != 0

at every point of C. These vanishing statements are independent of the two eta norm conventions used in Steps 59 and 62.

AAD's U(2) curvature decomposition identifies W_3^+ as a section of the complex line K_J^{-2} (underlying real rank two). A nowhere-zero restriction of this section trivializes K_J^{-2}|_C as a complex line. Hence

2<c1(M,J),[C]>=0,

and in particular <c1(M,J),[C]>=0.

On the other hand AAD's canonical Chern form is

gamma_J=-db=R(Omega)-a wedge Ja,

and [gamma_J]=2 pi c1(M,J). On C, T=0 means a=0. Einsteinity, the zero Rayleigh value r=s/6, and eta=0 give

R(Omega)=(s/4)Omega,

so

2 pi <c1(M,J),[C]> = integral_C gamma_J
= (s/4) integral_C Omega
= (s/4) Area_g(C) != 0.

This contradicts the trivialization supplied by W_3^+.

## Scope and research consequence

- The proposition is sensitive to s != 0 despite the pointwise cone itself being scalar-curvature independent. The new information comes from the actual canonical connection restricted to a compact J-complex surface.
- It does not exclude isolated nondegenerate zeros, whose index is +1, nor degenerate isolated zeros.
- It does not establish that arbitrary positive-dimensional analytic zero sets are clean surfaces. A compact zero set may contain higher-order points with DT=0, singular strata, or lower-dimensional strata. One cannot compactify a regular rank-two stratum without accounting for those ends.
- More generally, every closed smooth surface lying in Z must meet {DT=0}. What happens there is a precise remaining bridge: the forced W_3^+ section can vanish there, allowing nonzero canonical degree.
- The Ricci-flat Gibbons–Hawking finite-order-zero control is consistent: s=0 removes the canonical-degree contradiction. Noncompact zero surfaces are also consistent.
- The Bianchi-VIII/Fino bolt is a critical surface of q with q>0, not a torsion-zero surface. This proposition says nothing against its negative Euler contribution in the separate Morse–Bott discussion.
- For a general negative-Einstein germ, a convergent isolated cone zero would still be valuable. The proposition concerns compact positive-dimensional charge, a complementary global question rather than a replacement for that construction test.

## Proof anchors

Step 62: `workspace/notes/step62_torsion_zero_prolongation.md`, Theorem 62.A and Corollaries 62.B–C; exact coframe dictionary and determinant argument in `trace/ttcs/results/step62_ttcs01_verifier1_integration.md`.

Primary AAD source: `Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md`, U(2) decomposition around lines 135–147 (W_3^+ as K_J^{-2}) and canonical Chern form around lines 224–235 (gamma_J=R(Omega)-a wedge Ja, representing 2 pi c1).

## A concrete higher-order question suggested by the proof

Suppose a closed smooth surface C in Z has a dense rank-two locus, but DT vanishes at exceptional points. Then its tangent bundle is J-invariant by continuity, eta=0 along all of C, and the same canonical curvature calculation gives

<c1(K_J^{-2}),[C]> = s Area_g(C)/(4 pi).

For s<0 this degree is negative. The restriction W_3^+|_C is nonzero on the rank-two locus and vanishes wherever DT=0. If its zeros on C are isolated, their signed winding numbers must sum to this negative degree. This is not yet a contradiction: W_3^+ is only a smooth section, not a proved holomorphic one. It identifies specific information a higher-order AAD calculation could supply: constrain the local winding of W_3^+ along these exceptional zero points. If zeros are nonisolated, retain the localized first Chern class instead. No holomorphicity of a surrounding splitting, or of this restricted section, is assumed.
