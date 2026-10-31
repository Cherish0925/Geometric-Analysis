# O10 audit: a quantitative obstruction to fixed-background extension of the actual cores

Scope: `00_READ_FIRST.md`, all three sources in volume 04 (in particular the final (6.6) and section 7), and I50/I51 in volume 01. This note proves a conditional local extension obstruction. It does not prove O10. The argument uses the original abelian monopole system, rather than reintroducing the positive term cancelled in final (6.6).

## 1. The parameter issue is benign in the actual current formulation

Volume 01, I51 section 2, takes an ordinary solution and divides its spinor by sqrt(2). The resulting *same* constant-weight solution satisfies

\[
D_A\Phi=0,\qquad F_A^+=2i\sigma(\Phi),\qquad 0\le|\Phi|^2\le2.
\]

The parameter beta appears in the estimates, not in this equation. In scalar curvature -4 the last bound follows from

\[
4\nabla_A^*\nabla_A\Phi+(2|\Phi|^2-4)\Phi=0
\]

and the maximum principle on a closed manifold. Thus the local theorem below has constants independent of beta. No identification with an older variable-weight solution is required.

## 2. Local polynomial regularity with no assumed derivative budget

**Proposition.** Fix a smooth metric and spin-c trivialization on a ball B_2, with a fixed nested family of interior balls down to B_1. The same statement holds uniformly in a smoothly bounded, uniformly elliptic family of such charts. Let an actual constant-weight solution be defined on B_2, and suppose |Phi| <= M there. Put

\[
K=\|F_A\|_{L^2(B_2)},\qquad L=1+K.
\]

For its cubic torsion tau, there is C depending only on M and the fixed chart geometry such that

\[
\sup_{B_1}|\nabla_{3A}\tau|\le C L^4.
\tag{A}
\]

In particular bounded determinant curvature energy on a fixed outer ball gives uniform interior bounds on the torsion derivative. No bound on its critical quartic norm was assumed.

**Proof with the growth in K retained.** All following estimates are interior estimates on successively smaller fixed balls; a finite number of radius losses is absorbed into C. Because the determinant connection is abelian and the ball is contractible, choose a Coulomb representative a with

\[
\|a\|_{W^{1,2}}\le C(1+K),\qquad \|a\|_4\le C(1+K).
\]

There is no small-curvature hypothesis: this is the linear Hodge estimate on a ball, not a nonabelian Uhlenbeck argument. Relative to a fixed smooth background Dirac operator D_0,

\[
D_0\Phi=-\tfrac12c(a)\Phi.
\]

The bound |Phi| <= M and the L4 Dirac estimate therefore give

\[
\|\Phi\|_{W^{1,4}}+\|\nabla_A\Phi\|_4\le CL.
\tag{B}
\]

The curvature satisfies the exact abelian Maxwell identities

\[
dF_A=0,\qquad \delta F_A=2\delta F_A^+
                  =4i\delta\sigma(\Phi).
\]

The source is bounded by C M |nabla_A Phi|, hence has L4 norm at most CL. First use the Hodge estimate at p=2 to obtain F_A in W^{1,2}, hence L4; then at p=4 to obtain

\[
\|F_A\|_{W^{1,4}}\le CL,\qquad \|F_A\|_8\le CL.
\tag{C}
\]

On a smaller ball rechoose the abelian Coulomb gauge at p=8. Its bound is

\[
\|a\|_{W^{1,8}}\le CL.
\]

The gauge change preserves the spinor amplitude bound. The Dirac estimate now gives Phi in W^{1,8} with norm <= CL. Reapplying Maxwell/Hodge at p=8 gives F_A in W^{1,8}, and then a in W^{2,8}, both with norm <= CL. Since W^{1,8} embeds in C^{0,alpha} and W^{2,8} in C^{1,alpha} in dimension four, products in the differentiated Dirac equation give successively

\[
\|\Phi\|_{W^{2,8}}\le CL^2,\qquad
\|\Phi\|_{W^{3,8}}\le CL^3.
\tag{D}
\]

For the last estimate, the only terms are a D^2 Phi, Da D Phi, and D^2 a Phi; their L8 bounds are respectively O(L^3), O(L^2), and O(L), using the original L-infinity bound for Phi in the last term. Background coefficients contribute smaller terms. Consequently

\[
\|\nabla_A\Phi\|_\infty\le CL^2,
\qquad \|\nabla_A^2\Phi\|_\infty\le CL^3.
\]

The algebraic definition of the actual cubic torsion implies

\[
|\nabla_{3A}\tau|
\le C\bigl(|\Phi|^2|\nabla_A^2\Phi|
            +|\Phi|\,|\nabla_A\Phi|^2\bigr),
\]

which proves (A). Constants absorb the fixed spin-c background and all chart radii. The exponent four is a convenient safe exponent, not a sharp claim. QED.

## 3. Applying it to the newest actual simple core

Volume 04, final source section 7, provides actual solutions with

\[
\tau_\ell(\ell y)=(\bar z_1,\bar z_2)+o(1)
\quad\hbox{in }C^1
\]

on a fixed rescaled mass shell. On this shell, the gauge-invariant norm satisfies |tau_ell|(ell y)=|y|+o_C1(1). Its radial derivative is therefore at least c/ell. Kato gives |d|tau_ell|| <= |nabla_3A tau_ell|, without needing any choice of connection gauge. Thus for all sufficiently small ell,

\[
\sup_{\text{core shell}}|\nabla_{3A}\tau_\ell|
\ge c_*/\ell.
\tag{E}
\]

Suppose this *same actual solution* extends to a fixed ball B_2 with the same fixed hyperbolic geometry and |Phi| <= sqrt(2). Combining (A) and (E),

\[
K\ge (c_*/(C\ell))^{1/4}-1.
\]

After reducing the admissible ell,

\[
\boxed{\int_{B_2}|F_A|^2\ge c\ell^{-1/2}.}
\tag{F}
\]

The section 7 core has determinant energy O(ell^4). Hence almost all of this divergent cost must occur in its outer extension. If K_-(Phi,nabla Phi) denotes the uniformly bounded ASD model already constructed in I51, then F_A^+ is uniformly bounded by the amplitude equation and

\[
\int_{B_2}|F_A^- -K_-|^2
\ge \tfrac12\int_{B_2}|F_A|^2-C\operatorname{Vol}(B_2)
\ge c'\ell^{-1/2}-C'.
\tag{G}
\]

This ties the extension obstruction to the *actual fitted defect*, not just an arbitrary auxiliary energy. It is an explicit quantitative version of why a locally cheap actual core need not admit a cheap calibrated exterior.

The same conclusion applies to any fixed-degree I50 core after replacing c_* by a seed-dependent constant. It also applies to the split simple cores provided each has its own fixed-size bounded-geometry actual extension ball. No uniform-in-degree implicit-function radius is presumed.

## 4. A density consequence on closed actual sequences

Suppose a putative O10 sequence contains N_j such cores with ell_i <= epsilon_j -> 0. Assume their extension balls obey the fixed chart hypotheses above and have overlap at most Lambda. Summing (F), and using the inherited normalized bound int |F_A|^2 <= C V, yields

\[
N_j/V_j\le C\Lambda\,\epsilon_j^{1/2}\longrightarrow0.
\tag{H}
\]

Using (G) and the actual fit error int |F_A^- -K_-|^2 <= C epsilon_* V sharpens this to

\[
N_j/V_j\le C\Lambda\,\epsilon_*\epsilon_j^{1/2}
\]

for sufficiently small epsilon_j, with constants uniform in beta. For simple cores the index is one, so these particular extension configurations cannot carry the volume-scale positive torsion index required by I50 (3.4). For high-index cores a further index-versus-derivative bound is needed before replacing N by total index; this note does not silently make that replacement.

## 5. What remains outside the proposition

The local metric must remain controlled all the way to the fixed outer radius. Weak integral Ricci control does not provide such charts. The radius may shrink with the core, sectional curvature may concentrate, or a quotient ball may collapse. Passing to a noncollapsed covering chart is not free: the pulled-back curvature integral can grow with covering multiplicity even when base energy is controlled.

Thus the result is a strict no-go for *fixed-background outer matching*, not a proof of general O10. It complements I51 section 3.1, whose cutoff region had volume O(r^4) and hence allowed a shrinking matching scale. Here fixed-radius abelian elliptic propagation produces the divergent outer cost. It also distinguishes the actual simple-core constructions from a closed sequence: extending their bounded spinor data across a macroscopic regular region is costly.

The final identity (6.6) continues to vanish on the actual hyperbolic local cores. Nothing here alters that identity or restores its cancelled characteristic budget. The new information enters through the full Dirac-Maxwell elliptic system *on the outer region*, where the constructions had supplied no solution.

## 6. Concrete continuation suggested by the proven obstruction

Any attempt to globalize these cores cheaply must lose at least one of: fixed outer radius, controlled metric charts, bounded covering multiplicity, or the original same-solution amplitude bound. The last is unavailable on the closed scalar-minus-four constant-weight problem. A useful next quantitative target is therefore to replace the fixed-chart hypothesis by an estimate that charges the failure of those charts to the actual Ricci/Weyl and determinant budgets. That is a new geometric regularity problem; a generic no-loss statement for existing atoms alone does not supply it.

Status: (A)--(H) are conditional propositions with the above local regularity proof. Their general mechanism is classical abelian elliptic regularity; the application to the supplied shrinking actual cores and the explicit outer-fit cost are the additions derived here. No novelty claim relative to the literature, no unrestricted zero-end theorem, and no closed escape construction are made.
