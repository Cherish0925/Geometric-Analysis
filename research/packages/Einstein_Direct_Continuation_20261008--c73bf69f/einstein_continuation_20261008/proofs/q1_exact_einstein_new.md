# Q1: exact Einstein continuation, 8 October 2026

## Outcome

No new unrestricted nonexistence theorem or Einstein example has been proved in this continuation. In particular the remaining small-blowup range of LeBrun's question is not closed. The analysis below identifies an exact route that would close it, and shows why the current flux equality and scalar budgets do not supply its missing premise. The classical results are attributed rather than registered as new progress.

## The actual target

Let X be a minimal complex surface of general type, A=c_1^2(X)>0, and M=X#k CPbar2, k>=1. The ordinary actual classes are a_e=K+sum e_i E_i, with a_e^2=T=2chi+3tau=A-k. The inherited N1 obstruction excludes k/A>1/3-epsilon_0 in its stated supply range. This note concerns the remaining small k/A, and does not re-prove that estimate.

Every Einstein candidate has negative scalar curvature: the ordinary positive monopole budget excludes nonnegative scalar curvature. Fix s=-4. Write w=Vol^{-1} integral |W+|^2, V=Vol, and choose one actual class a with p=(a_g^+)^2>=A. At an Einstein metric P=0 and

    4 pi^2 T/V = 2/3 + 2 w.

For the project's parameter defect, the exact identity is

    D_beta/V = 4 + 16/beta + 6(beta-5) w - 72 pi^2(p-T)/V.

This follows by substituting the Chern-Weil identity in

    D_beta/V = 16(1+1/beta)+6(beta+1)w-72 pi^2 p/V.

For example at beta=2,

    D_2/V = 12-18w-72 pi^2(p-T)/V.

Thus p-T>=k>0 is compatible with D_2>=0 by lowering the Weyl density below its KE value w=2/3. This is the actual remaining possibility. A new contradiction cannot be obtained by pretending w retains the KE value merely because Ric is Einstein.

## A direct sufficient geometric input

LeBrun's published theorem gives an exact alternative to solving the full P-infimum first.

**Classical theorem (LeBrun).** If (M,g,omega) is compact almost-Kahler Einstein and its star-scalar curvature s*=s+|nabla omega|^2 is everywhere negative, M cannot be smoothly decomposed as N#CPbar2.

Consequently any proof that an Einstein metric on the above M admits a compatible closed self-dual form omega, |omega|^2=2, satisfying

    sup_M |nabla omega|^2 < -s

would exclude every k>=1 at once. There is no small-k loss in this implication. It does not require Q2's sharp infimum.

The same paper's Theorem B gives, under b+>1 and s*<=-s/m for m>1,

    k < A/(m+2).

These statements already belong to LeBrun 2005 and are not new theorems of this continuation.

## Why current inputs do not yield the form

1. The attachment's equality theorem for harmonic flux reads: if s is constant and L_h=0, then either g is Einstein, or g admits an aligned almost-Kahler structure. On the Einstein branch B=0, F_h=0 and L_h=0 for every nonzero harmonic ASD h. In the proof, the construction divides by the nonzero aligned amplitude c; at P=0 one has c=0. Hence the theorem supplies no omega whatsoever in the very branch Q1 must eliminate. Removing the word 'either' would be a circular proof.

2. A nontrivial actual SW spinor is not itself a compatible symplectic form. Its quadratic form is F_A^+ up to convention; dF_A=0 gives dF_A^+=-dF_A^- rather than dF_A^+=0. Normalizing its pointwise length also introduces a radial derivative. Neither Einstein Ricci nor a^2=T eliminates these terms. In fact p-a^2>=k records nonzero anti-self-dual cohomological content.

3. A harmonic self-dual form from Hodge theory has variable length and may have zeros. Conformal normalization produces an almost-Kahler structure only away from its zero set; the conformally changed metric need not remain Einstein. Thus the classical minimality theorem cannot be applied after this normalization without an additional argument.

4. The new complete noncompact strictly almost-Kahler Einstein model shows why the metric's Einstein equation alone cannot force integrability by a pointwise identity. In that model s=-12 and |nabla omega|^2<=32/3, so s*<0. It is entirely consistent with LeBrun's theorem: compactness and exceptional-sphere topology are indispensable to that theorem.

## The geometric information still needed

A successful application of the minimality route would have to construct the same metric's global compatible symplectic form (and obtain the required star-scalar control), not merely an almost complex structure, a harmonic class, a local normalized spinor, or a form for a conformal metric. No such construction has been derived from the supplied N1/I41/FD2 estimates.

Alternatively, an Einstein-specific inequality could directly bound the Weyl deficit below its necessary threshold. The existing scalar/Weyl envelope permits Einstein data; its exact inversion is a restriction but not a contradiction. This continuation obtains no new signed equation that excludes those data.

## Sources checked

- C. LeBrun, *Einstein Metrics, Symplectic Minimality, and Pseudo-Holomorphic Curves*, Annals of Global Analysis and Geometry 28 (2005), 157–177; DOI 10.1007/s10455-005-3892-5. Primary full preprint: https://arxiv.org/pdf/math/0409290 . Theorems A and B are on printed pp.4–5; Proposition 2.1 constructs the canonical connection under an already given almost-Kahler structure. Browser source turn808view0.
- C. LeBrun, *Einstein Metrics, Complex Surfaces, and Symplectic 4-Manifolds*, Math. Proc. Cambridge Philos. Soc.147 (2009),1–8, https://arxiv.org/pdf/0803.3743 . The unrestricted nonminimal general-type question is in the final discussion.
- User source: upload/01_Research_Synthesis.tex, 'What Q1 already inherits'; upload/03_Subsequent_Mathematical_Developments.tex, 'Constant-scalar equality structure'.

The source LeBrun preprint mentions Oguri–Sekigawa's claimed s* upper bound conditionally. This note does not adopt that claim as an established universal estimate.
