# Strict spectral stability of the complete negative Einstein example

## Statement and attribution

Let `(M,g)` be the complete smooth metric constructed by the user's A01 manuscript and independently verified in `Q4_Complete_Example_and_Fino_Question.tex`. In the normalization used there,

\[
 \operatorname{Ric}=-3g,\qquad \widehat R_-=-\operatorname{Id}_{\Lambda^-}.
\]

The following is an application/localization of Diego Artacho's September 2026 chiral stability identity, not a new general stability theorem:

\[
\boxed{\int_M\langle Ah,h\rangle\,dV\ge2\int_M|h|^2\,dV,
\quad A=\Delta_L-2E=\nabla^*\nabla-2\mathring R,\quad E=-3,}
\tag{1}
\]

for **every smooth compactly supported trace-free symmetric two-tensor** `h`. No divergence condition is needed in (1). In particular it holds for transverse-traceless (TT) variations. The curvature operator convention is `widehat R=K Id` on a space form of sectional curvature `K`; tensor norms are the usual Hilbert–Schmidt norms, not the full four-index Riemann norm.

Moreover the Friedrichs realization of `A` on trace-free L2 tensors has spectrum in `[2,infinity)` and bounded inverse of operator norm at most `1/2`. Every smooth L2 solution of `Ah=0` vanishes.

For compactly supported TT `h`, the full Einstein residual energy

\[
 P(g)=\int_M|\operatorname{Ric}^{\circ}|^2\,dV
\]

has the exact second variation

\[
\boxed{P''_g(h,h)=\frac12\|Ah\|_{L^2}^2\ge2\|h\|_{L^2}^2.}
\tag{2}
\]

These statements strengthen the geometric description of the complete example by an actual spectral estimate. They neither produce a closed Goldberg counterexample nor prove nonlinear rigidity for variations changing the geometry at infinity.

## 1. Local identity and why compact support suffices

Artacho, arXiv:2609.15159, Proposition 3.1, constructs on any oriented four-manifold a canonical spin-h structure using the auxiliary bundle `Lambda+`; its twisted spinor bundle has a unit parallel section `psi`. Orientation reversal uses `Lambda-` instead. This construction is bundle-theoretic and imposes neither compactness nor finite volume.

The associated parallel isometric bundle map is

\[
 \Phi(h)=h_{ij}e_i\cdot\psi\otimes e^j,
\]

and `mathcal D` is the associated twisted Dirac operator on spinor-valued one-forms. In arXiv:2512.01620, Section 3, Lemma 3 is a **local differential identity**. Pairing that identity with `Phi(h)`, using `Ric=Eg`, and using the curvature endomorphism `R_psi` of arXiv:2609.15159, gives

\[
 \|\mathcal D\Phi(h)\|_2^2
 =\int\langle Ah,h\rangle
   +E\|h\|_2^2+\int\langle R_\psi h,h\rangle. \tag{3}
\]

The passage from the local formula to (3) uses only formal adjointness and integration by parts. For `h` of compact support all terms have compact support and there is no boundary term, regardless of the volume or ends of `M`. Thus we are using the source's proof, not importing its compact-manifold theorem without checking its hypotheses.

Under the canonical identification

\[
 \operatorname{Sym}^2_0T^*M\simeq\Lambda^+\otimes\Lambda^-,
\]

Artacho's equation (4.1) is

\[
 R_\psi=(2\widehat R_+-E\operatorname{Id})\otimes\operatorname{Id}.
\]

Substituting into (3) yields the exact integrated identity

\[
 \int\langle Ah,h\rangle
 =\|\mathcal D\Phi(h)\|_2^2
 -2\int\langle(\widehat R_+\otimes\operatorname{Id})h,h\rangle. \tag{4}
\]

Reverse orientation and use `widehat R_-=-Id` for the inherited example. Then

\[
\boxed{\int\langle Ah,h\rangle
       =\|\mathcal D\Phi_-(h)\|_2^2+2\|h\|_2^2.} \tag{5}
\]

This proves (1), with the numerical constant `2` in the normalization `Ric=-3g`. The proof does not use the almost-Kähler form or an additional almost-Kähler restriction on variations: it concerns the metric and all trace-free variations.

## 2. The complete L2 problem

On compactly supported trace-free tensors the quadratic form of `A` is densely defined, symmetric and bounded below by `2`. The Friedrichs extension therefore has spectrum in `[2,infinity)`, and functional calculus gives an inverse on L2 of norm at most `1/2`.

For the explicit model, all curvature components are uniformly bounded: the rational expressions extend to the bolt and have finite limits at the infinite end. Consequently the form domain is the closure of compactly supported smooth tensors in the H1 form norm. The coercive estimate extends by form closure.

There is also a direct verification that no extra smooth L2 zero mode is hidden at infinity. Suppose `Ah=0` and `h` is smooth, trace-free and L2. Completeness provides compactly supported Lipschitz cutoffs `chi_R`, equal to one on the metric ball of radius `R`, supported in the ball of radius `2R`, with `|d chi_R|<=C/R`. Smooth approximation is harmless. Local integration by parts gives the IMS identity

\[
 \int\langle A(\chi_Rh),\chi_Rh\rangle
 =\operatorname{Re}\int\langle Ah,\chi_R^2h\rangle
  +\int|d\chi_R|^2|h|^2
 =\int|d\chi_R|^2|h|^2. \tag{6}
\]

Apply (1) to `chi_Rh`; **it need not remain divergence-free**, which is why the trace-free formulation matters. We obtain

\[
 2\int\chi_R^2|h|^2\le\frac{C^2}{R^2}\|h\|_2^2.
\]

Letting `R` tend to infinity gives `h=0`. No a priori H1 assumption on the zero mode was used; smooth local regularity and L2 suffice for these compactly supported integrations.

This proves L2 infinitesimal Einstein rigidity in TT gauge. It does not rule out infinitesimal Einstein deformations that are not L2, such as changes of asymptotic data, and it does not by itself establish a nonlinear moduli theorem.

## 3. Einstein–Hilbert and Ricci-defect Hessians

The complete example has infinite volume, so the unrenormalized global Einstein–Hilbert integral is not a finite functional. For compactly supported metric changes use the relative cosmological Einstein–Hilbert action

\[
 \mathcal S_{\mathrm{rel}}(\widetilde g;g)
 =\int_M\big[(s_{\widetilde g}-2E)dV_{\widetilde g}
             -(s_g-2E)dV_g\big],\qquad E=-3. \tag{7}
\]

Its integrand is a compactly supported density difference. The background is critical, and on TT variations the standard Hessian formula gives

\[
 \mathcal S_{\mathrm{rel}}''(h,h)
 =-\frac12\int\langle Ah,h\rangle
 \le-\|h\|_2^2. \tag{8}
\]

Thus the sign is the usual one: Einstein–Hilbert stability means negative Hessian on TT directions.

For `P`, no subtraction is necessary: the Einstein background has zero integrand and a compactly supported change gives finite energy. On TT tensors,

\[
 s'_g[h]=0,\qquad
 (\operatorname{Ric}^{\circ})'_g[h]
 =\frac12\Delta_Lh-Eh=\frac12Ah.
\]

All terms differentiating the norm and volume vanish in the second derivative because `Ric^circ=0`. Hence

\[
 P''_g(h,h)=2\| (\operatorname{Ric}^{\circ})'_g[h]\|_2^2
 =\frac12\|Ah\|_2^2.
\]

Finally, (1) and Cauchy–Schwarz imply `||Ah||_2>=2||h||_2`, proving (2).

This is stronger than observing merely that `P>=0` and `P(g)=0`: it gives a uniform L2 coercive constant after the TT restriction. It is still a local/spectral conclusion, not a new global minimization classification.

## Primary sources

1. Diego Artacho, *Stability of Einstein 4-manifolds satisfying a chiral curvature condition*, arXiv:2609.15159v1, submitted 14 September 2026. Proposition 3.1, Theorem 1.2, and equation (4.1). https://arxiv.org/pdf/2609.15159 ; https://arxiv.org/html/2609.15159v1
2. Diego Artacho, *On the stability of Einstein metrics carrying a special twisted spinor*, arXiv:2512.01620v1. Section 3, Lemma 3 and Corollary 4 contain the local identity and its integrated proof. https://arxiv.org/html/2512.01620v1

The general spinorial identity and chiral criterion belong to these sources. The application, compact-support localization, normalization `2`, cutoff verification, and the resulting `P` Hessian have been written out here for the inherited complete example.
