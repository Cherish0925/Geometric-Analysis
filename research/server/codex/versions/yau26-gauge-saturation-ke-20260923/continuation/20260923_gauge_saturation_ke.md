# From actual monopole saturation to a Kähler–Einstein realization

23 September 2026. New composition theorem. The inherited bounded-form
construction and the compact-regime realization proof remain unchanged.
This note proves that their combination eliminates the separately assumed
half-Weyl bound and yields a global Kähler structure, not merely an Einstein
metric or an eigenline on a double cover.

## 1. Statement from the original geometric and gauge input

Use exterior-algebra norms on two-forms, Hilbert–Schmidt norms on the Weyl
endomorphism of \(\Lambda^+\), and tensor norms on Ricci. Define
\[
 \delta_-(g)=\|\operatorname{Ric}_g^\sharp+I\|_{\infty,\mathrm{op}},
 \qquad r(g)=\fint_M|\operatorname{Ric}_g+g|^2.
 \tag{1}
\]
Fix a Spin\(^c\) structure whose unperturbed monopole equations are solvable
for every metric in the conformal class \([g]\). It is an **actual** gauge
input, not an arbitrary cohomology vector. The structure may depend on the
input metric but is fixed through its auxiliary positive conformal weights.
Write \(a\) for its real first Chern class, \(p=(a_g^+)^2\), and
\[
 \mathfrak D_2(g,a)
  =\frac32\int_M\bigl(s_g^2+12|W_g^+|^2\bigr)\,d\mu_g
           -72\pi^2p\ge0,
 \qquad q(g,a)=\frac{\mathfrak D_2(g,a)}{\operatorname{Vol}(g)}.
 \tag{2}
\]
The nonnegativity is the classical monopole curvature inequality. This is
the parameter-two deficit, not an Einstein defect. Its exact equality set
contains compatible constant-scalar-curvature Kähler metrics, including
non-Einstein ones.

**Theorem A (saturation implies exact realization).** For every
\(D,A_0>0\) there is \(\varepsilon(D,A_0)>0\) such that the following
holds. Let \(M\) be a closed connected smooth oriented aspherical
four-manifold. If \(g\) and an actual conformally solvable Spin\(^c\)
structure satisfy
\[
 \operatorname{diam}(g)\le D,\qquad p\ge A_0,
 \qquad \delta_-(g)+q(g,a)<\varepsilon(D,A_0),
 \tag{3}
\]
then the **same oriented smooth manifold** admits a smooth complex structure
\(J\) and a smooth Kähler metric \(h\) such that
\[
                          \operatorname{Ric}_h=-h.
 \tag{4}
\]
The complex orientation agrees with the specified orientation. No finite
cover is needed. The threshold is uniform across changing manifolds and
metric-dependent actual classes. No separate half-Weyl bound, curvature
energy bound, lower volume bound, square-cost bound, Sobolev constant,
injectivity-radius bound, or Ricci-derivative bound is an assumption.

The diameter bound, asphericity and actual positive projection budget are
retained. The simultaneous smallness in (3) is essential to the argument:
pointwise Ricci pinching alone does not automatically make \(q\) small.
No claim is made that the original \(g\) itself is Kähler, that its original
Spin\(^c\) structure must be canonical for the produced complex structure,
or that a numerical threshold has been computed.

This is a first-line realization theorem rather than another forbidden-mode
estimate. Its proof does not try to contradict the allowed Kähler–Einstein
mode. It shows that, under the stated global conditions, this mode is
realized on the original smooth type.

## 2. The two inherited inputs used in the proof

The [actual-form theorem](../mathematics/current/line1_composed_application.md)
supplies, for
\[
                  \kappa=r+q\le1/2880,
\]
and each \(0<\eta\le1/4\), a single smooth self-dual two-form \(\omega\)
such that
\[
 \|\omega\|_\infty\le2\sqrt3,
 \qquad \fint(|\omega|^2-2)^2\le720\kappa+\eta,
 \tag{5}
\]
\[
 \fint|\nabla\omega|^2
        \le13\kappa+4\sqrt{2\kappa}+\eta.
 \tag{6}
\]
All estimates in (5)–(6) are independent of \((-a^2)_+/\operatorname{Vol}\).
The square cost in the inherited theorem is needed for its additional
Hodge-Laplacian estimate, which is **not used here**. The bound (5) is
proved in Section 2 of that source before any second-order estimate.

The second input is the endpoint form of the
[compactness/realization theorem](20260923_compact_realization.md), Sections
3–5. Closed oriented aspherical four-manifolds with two-sided bounded Ricci,
uniformly bounded diameter, volume bounded below, and uniformly locally
equiintegrable \(|W^+|^2\) have a uniform harmonic-radius lower bound.
An almost-Einstein sequence then converges, after diffeomorphisms and a
subsequence, in \(C^{1,\alpha}\) and strongly in finite \(W^{2,p}\)
to a smooth exact Einstein metric on the common smooth type.

The geometric reason is important. At a vanishing harmonic radius the
rescaled Ricci tensor tends to zero and the equiintegrable Weyl half
disappears. Jiang–Naber gives finite total curvature energy. The resulting
complete nonflat Ricci-flat ASD limit is ALE by Bando–Kasue–Nakajima.
Its compact core would embed in the original manifold, contradicting the
[aspherical compact-core lemma](../mathematics/current/line1_aspherical_no_bubbles.md).
This includes rational-ball ALE quotients, not just bubbles containing
exceptional spheres. Harmonic-coordinate elliptic convergence uses the
small Ricci tensor itself, never derivatives of that tensor.

The substantive new connection is to use a classical amplitude consequence
of saturation for endpoint compactness, then pass the **global** supplied
forms to an actual parallel form on the limiting manifold. A separate
polynomial Weyl-surrogate or second-order form bound is not necessary here.

## 3. Positive projection and bounded diameter fix the volume regime

Consider any sequence satisfying the fixed \(D,A_0\) hypotheses with
\[
                    \delta_j+q_j\longrightarrow0.
 \tag{7}
\]
Discard finitely many terms so that \(\delta_j\le1/2\). Each Ricci
eigenvalue lies in \([-3/2,-1/2]\), so
\[
 |\operatorname{Ric}_{g_j}|\le3,
 \qquad -6\le s_{g_j}\le-2,
 \qquad r_j\le4\delta_j^2.
 \tag{8}
\]
The actual monopole scalar estimate gives
\[
 32\pi^2 A_0\le\int s_-^2
       \le16(1+\delta_j)^2V_j,
 \qquad V_j\ge\frac{8\pi^2A_0}{9}=:v_0.
 \tag{9}
\]
Bishop comparison, with \(\operatorname{Ric}\ge-3g\), gives
\[
                  V_j\le V_{-1}(D+1)=:V_0(D).
 \tag{10}
\]
It also gives uniform bounds
\[
 c(D,A_0)\rho^4\le\operatorname{Vol}_{g_j}B_\rho(x)
                         \le C\rho^4\quad(0<\rho\le1).
 \tag{11}
\]
For the lower bound compare with a ball of radius \(D+1\) and use (9).
For the upper bound use the small-radius model-ball estimate. These are
geometric ball bounds at every point, not merely a positive total volume.
They justify the noncollapsed compactness and curvature-energy input.

## 4. The gauge deficit prevents one-sided critical concentration

We have \(\kappa_j=r_j+q_j\to0\). Put
\(w_j=\sqrt6|W^+_{g_j}|\), \(e_j=s_j+4\), and \(z_j=s_j+2w_j\).
The completed-square decomposition of the signed monopole inequality gives
\(\int z_j^2\le2\mathfrak D_2\), while
\(\fint e_j^2\le4r_j\). Hence
\[
 \fint(w_j-2)^2
    =\frac14\fint(z_j-e_j)^2
    \le q_j+2r_j\le2\kappa_j.
 \tag{12}
\]
This is equation (7) of the inherited actual-form paper, and precedes its
form construction. The elementary inequality
\[
             |W^+|^2=w^2/6\le\frac13(w-2)^2+\frac43
 \tag{13}
\]
therefore implies, for every measurable subset \(E\subset M_j\),
\[
 \int_E|W^+_{g_j}|^2
          \le\frac43\operatorname{Vol}_{g_j}(E)
                            +\frac23\kappa_jV_j.
 \tag{14}
\]
In particular, (11) yields
\[
 \sup_x\int_{B_\rho(x)}|W^+_{g_j}|^2
       \le\frac43C\rho^4+\frac23V_0\kappa_j.
 \tag{15}
\]
This is stronger than bounded total \(L^2\) energy: it rules out a
nonzero critical half-Weyl mass at arbitrarily small scales in the sequence.

For completeness, a common equiintegrability modulus does follow from
(15). Given \(\epsilon>0\), make the second term less than
\(\epsilon/2\) on the tail, and then take \(\rho\) small so that
the first term is less than \(\epsilon/2\). The finitely many preceding
smooth compact metrics have uniformly vanishing small-ball integrals too.
Taking the minimum of these radius choices proves
\[
 \lim_{\rho\downarrow0}\sup_j\sup_x
           \int_{B_\rho(x)}|W^+_{g_j}|^2=0.
 \tag{16}
\]
The modulus may depend on the sequence. That is sufficient for the
contradiction proof of the uniform threshold below. We do not claim that
a bare fixed upper bound on \(\kappa\) supplies (16) without a smallness
or limiting argument.

An equivalent direct check avoids introducing a modulus. If harmonic
radii \(\rho_j\to0\), then on each fixed-radius ball for
\(\widehat g_j=\rho_j^{-2}g_j\), scale invariance gives
\[
 \int_{B_R(\widehat g_j)}|W^+_{\widehat g_j}|^2
 \le\frac43C(R\rho_j)^4+\frac23V_0\kappa_j\longrightarrow0.
 \tag{17}
\]
This is exactly the vanishing needed in the no-ALE-core blowup argument.
It requires no supercritical \(L^q\) estimate and no full pointwise
curvature estimate on the original inputs.

## 5. From convergence of metrics to a global parallel form

Apply the inherited endpoint compactness to (8)–(11) and (16). After
a subsequence there are a fixed closed oriented smooth \(M_\infty\),
orientation-preserving diffeomorphisms \(\phi_j:M_\infty\to M_j\),
and a smooth metric \(h\) such that, with \(h_j=\phi_j^*g_j\),
\[
 h_j\longrightarrow h\quad\text{in }C^{1,\alpha}
         \text{ and strongly in }W^{2,p}\ (p<\infty),
 \qquad\operatorname{Ric}_h=-h.
 \tag{18}
\]
For any one fixed \(\alpha<1\), these convergences hold along a
suitable subsequence. The limiting smooth structure is the original
smooth type of every sufficiently late term, not merely its topology.

Choose \(\eta_j\downarrow0\) and actual forms \(\omega_j\) satisfying
(5)–(6). Pull them back by the same diffeomorphisms and call the forms
\(\widetilde\omega_j\). They remain uniformly bounded in \(L^\infty\),
and (6), (10) imply
\[
                  \|\nabla^{h_j}\widetilde\omega_j\|_{L^2(h_j)}
                                   \longrightarrow0.
 \tag{19}
\]
Because \(h_j\to h\) in \(C^1\), the difference of their connections
tends uniformly to zero. Thus
\[
 \|\nabla^h\widetilde\omega_j\|_{L^2(h)}
 \le C\|\nabla^{h_j}\widetilde\omega_j\|_{L^2(h_j)}
       +o(1)\|\widetilde\omega_j\|_{L^2(h)}\longrightarrow0.
 \tag{20}
\]
The forms are bounded in \(H^1(M_\infty,h)\). Rellich compactness gives
strong \(L^2\) convergence to a globally defined form \(\omega_\infty\).
Passing (20) weakly proves \(\nabla^h\omega_\infty=0\).
The distributional parallel equation with smooth coefficients implies
smoothness, for example by taking its rough-Laplacian equation and using
elliptic regularity.

Self-duality passes to the limit because the Hodge stars converge uniformly.
The uniform bound and strong \(L^2\) convergence also allow products to
converge in \(L^2\). The amplitude part of (5) therefore gives
\[
                      *_h\omega_\infty=\omega_\infty,
                 \qquad |\omega_\infty|_h^2=2.
 \tag{21}
\]
The amplitude statement first holds almost everywhere and then everywhere
by smoothness. In particular the limit form does not vanish.

Define \(J\) by \(h(JX,Y)=\omega_\infty(X,Y)\). The elementary
four-dimensional algebra of a self-dual form of norm \(\sqrt2\) gives
\(J^2=-I\). Parallelness gives \(\nabla^hJ=0\), so \(J\) is integrable
and \(d\omega_\infty=0\). Hence \((h,J)\) is Kähler, and (18) makes
it negative Kähler–Einstein.

The distinction from a local Weyl eigenline argument is substantial.
Each \(\omega_j\) was a **global actual form**, despite possibly having
zeros. Its limiting form is globally nonvanishing. No choice of a local
unit eigenvector, no orientability assertion about an eigenline bundle,
and no passage to a two-fold cover occurs.

## 6. Sequential compactness gives a fixed small-defect threshold

Suppose Theorem A is false for fixed \(D,A_0\). Choose manifolds,
metrics and actual classes meeting the topological and gauge hypotheses
with \(\delta_j+q_j<1/j\), but for which no compatible normalized
negative Kähler–Einstein metric exists on \(M_j\).

Sections 3–5 produce a smooth Kähler–Einstein pair \((h,J)\) on
\(M_\infty\) and diffeomorphisms \(\phi_j:M_\infty\to M_j\).
Transporting \((h,J)\) to every sufficiently late \(M_j\) contradicts
the choice of the sequence. This proves the existence of
\(\varepsilon(D,A_0)>0\). The argument allows the topology and actual
class to vary; neither is fixed in the contradiction sequence. \(\square\)

This last step is necessary. The theorem is not merely the assertion that
one already given sequence has a Kähler–Einstein limit. Nor does the
proof invent a sequence of improving metrics on the same manifold from
one small-error input. Uniformity is obtained by excluding a sequence of
counterexamples to the fixed-threshold statement.

## 7. Global consequences and a weaker topological input

### 7.1 A joint gap and its topological range

**Corollary B (joint gap on non-Kähler smooth types).** Fix \(D,A_0>0\).
On every closed connected oriented aspherical four-manifold admitting no
compatible Kähler structure, every input with
\(\operatorname{diam}(g)\le D\) and an actual conformally solvable
class satisfying \(p\ge A_0\) obeys
\[
                         \delta_-(g)+q(g,a)
                              \ge\varepsilon(D,A_0).
 \tag{22}
\]
The same conclusion holds on the larger class of such manifolds admitting
no compatible negative Kähler–Einstein metric. It follows directly by
contraposition of Theorem A.

For example, the inherited nonzero-shear self-gluings are aspherical and
have no Kähler finite cover; their specified actual classes have
\(a^2=2\chi>0\), hence \(p\ge a^2\). The theorem therefore applies to
that family whenever the bounded-diameter and simultaneous-deficit
conditions are considered. This is a constraint on arbitrary input
metrics, not only on the chosen shear construction. It does not rule out
Einstein metrics whose associated \(q\) stays away from zero.

In particular, a sequence on non-Kähler aspherical types with a fixed
positive projection budget and \(\delta_j+q_j\to0\) must have
\[
                           \operatorname{diam}(g_j)\to\infty.
 \tag{23}
\]
If diameters did not tend to infinity, a bounded subsequence would
contradict (22). Equation (23) is a joint-saturation escape theorem,
not a proof that every pointwise near-Einstein sequence saturates (2).

**Topological extension.** The same proof works on any class of closed
oriented smooth four-manifolds for which the compact-core non-embedding
lemma holds uniformly as a qualitative topological statement. In particular,
the [torsion-free, \(\pi_2=0\) core-exclusion extension](20260923_topological_core_scope.md)
allows asphericity to be replaced by
\[
                      \pi_1(M)\text{ torsion-free},
                            \qquad \pi_2(M)=0.
 \tag{24}
\]
Only the compact-core step uses this topology; all analytic estimates and
the threshold dependence are unchanged. The extension depends on the
separately proved core lemma, not on any assertion that (24) implies
asphericity. Connected sums with \(S^1\times S^3\) are a useful reason
to keep that distinction.

### 7.2 An actual fixed-manifold sharpness example for the diameter bound

The diameter hypothesis cannot be omitted from Theorem A, even if one adds
uniform bounds on full curvature and every fixed curvature derivative.
This is demonstrated by actual inherited metrics, not merely by a formal
escape alternative.

Fix one nonzero-shear self-gluing
\[
 M=M(h,g;u,f),\qquad h\ge1,\quad g\ge2,\quad [u]\ne0,
 \quad f\in\operatorname{Diff}^+(\Sigma_g).
 \tag{25}
\]
The [closed construction](../mathematics/current/round11_closed_gluing.md),
Sections 1 and 5, supplies \(G_\ell\) with
\(\operatorname{Ric}_{G_\ell}\) tending pointwise to \(-3G_\ell\)
and the **exact** volume \(4\pi^2\chi(M)/9\). Set \(g_\ell=3G_\ell\)
and
\[
 A=2\chi(M)>0,\qquad T=2\chi(M)+3\tau(M)=A.
\]
Then on this fixed closed smooth manifold
\[
 \delta_\ell\longrightarrow0,
 \qquad V_\ell=4\pi^2\chi(M)=2\pi^2A,
 \qquad\|\nabla^k\operatorname{Rm}_{g_\ell}\|_\infty\le C_k
                           \quad(k\ge0).
 \tag{26}
\]
The [topology proof](../mathematics/current/round11_graph_topology.md)
gives asphericity and signature zero. The
[virtual Kähler obstruction](../mathematics/current/round11_kahler.md)
excludes every Kähler structure even on a finite cover. The two symplectic
forms of the construction provide a fixed actual canonical class \(a\)
in the chosen orientation with
\[
                  a^2=A,\qquad p_\ell=(a_{g_\ell}^+)^2\ge A.
 \tag{27}
\]
Here \(b_+>1\), so the Taubes nonzero invariant supplies unperturbed
solutions for every metric and, in particular, every metric in each
\([g_\ell]\). The class-square calculation and this actual-supply
argument are in [Round 12](../mathematics/current/round12_global.md),
Sections 1–3, and [Round 11 variational theory](../mathematics/current/round11_variational.md),
Section 2. No metric-dependent formal replacement for this class is used.

It remains to check the extra saturation hypothesis of the new theorem.
Put \(S_2=\int s^2\), \(W_2=\int|W^+|^2\), and
\(P=\int|\operatorname{Ric}^{\circ}|^2\). Chern–Weil gives
\[
              4\pi^2T=S_2/24+2W_2-P/2,
\]
and eliminating \(W_2\) from (2) yields the exact identity
\[
 \mathfrak D_2
   =\frac98S_2+36\pi^2T+\frac92P-72\pi^2p.
 \tag{28}
\]
If \(\delta_\ell\le1/2\), then
\[
 S_2/V_\ell\le16(1+\delta_\ell)^2,
 \qquad P/V_\ell\le4\delta_\ell^2.
\]
The latter follows by orthogonal projection of \(\operatorname{Ric}+g\)
onto the traceless tensors. Using (26)–(28),
\[
 \begin{split}
 0\le q_\ell
 &\le18(1+\delta_\ell)^2+18\delta_\ell^2
                                 -\frac{36\pi^2A}{V_\ell}\\
 &=36\delta_\ell(1+\delta_\ell)\longrightarrow0.
 \end{split}
 \tag{29}
\]
Therefore this actual fixed manifold has simultaneous
\(\delta_\ell\to0\), \(q_\ell\to0\), a fixed positive actual
projection budget, zero negative-square cost, exact positive volume, and
the curvature bounds in (26), but it has no Kähler–Einstein metric because
it has no Kähler structure. Theorem A consequently forces
\[
                         \operatorname{diam}(g_\ell)\to\infty.
 \tag{30}
\]
More importantly, (25)–(29) refute the version of Theorem A with its
diameter hypothesis deleted. The preserved long-neck construction is thus
a genuine sharpness test for the new realization theorem. We have not
constructed new shear metrics or newly proved their virtual Kähler
obstruction; the new deduction is their simultaneous parameter-two
saturation and their exact role as counterexamples to diameter-free
Kähler–Einstein realization. This says nothing new about whether they
admit **non-Kähler** negative Einstein metrics, which remains open here.

## 8. What has changed, and what has not

The new implication is
\[
 \boxed{
 \begin{gathered}
 \text{actual gauge supply + positive projection + bounded diameter}\\
 +\ \text{pointwise negative Ricci approximation}
 +\ \text{parameter-two saturation}\\
 +\ \text{no admissible ALE core in the smooth type}\\
 \Longrightarrow\ \text{negative Kähler–Einstein realization on that type}.
 \end{gathered}}
\]
Three earlier conditions have not merely been renamed: the separate
volume lower bound is supplied by the actual gauge class; the independent
half-Weyl bound is replaced by derived critical equiintegrability; and
the limiting local Kähler mode is realized by a global parallel form.
The negative-square cost is absent because no second-order form estimate
is needed after geometric compactness has been established.

This is not a universal obstruction/existence dichotomy. The deficit
\(q\) and the diameter restriction still select a genuine regime, and
the relevant topological core exclusion does not hold on all four-manifolds.
In particular, aspherical negative Kähler–Einstein surfaces themselves
have \(\delta_-=q=0\) for their compatible canonical input, so the
allowed regime is nonempty. Unequal-curvature hyperbolic products have
\(q=0\) but nonzero Ricci error: they do not turn cscK saturation alone
into an Einstein implication. The theorem's output also need not preserve
a preassigned complex structure.

The proof is a new composition of the inherited first-line actual-field
estimate and no-bubble compactness mechanism. The monopole curvature
inequality, bounded-Ricci compactness, finite-energy ALE asymptotics and
ALE classification remain classical inputs. No exhaustive priority search
or field-wide novelty certification is claimed.

## 9. Sources and verification scope

- [Actual form supply](../mathematics/current/line1_composed_application.md),
  Sections 2–3, provides (5)–(6). Its second-order square-budget estimate
  is deliberately not invoked.
- [Compact realization](20260923_compact_realization.md), Sections 3–5,
  provides the critical equiintegrability endpoint, harmonic-coordinate
  regularity and topology-preserving compactness. The present proof
  verifies its endpoint hypothesis by (14)–(17).
- [Aspherical compact-core exclusion](../mathematics/current/line1_aspherical_no_bubbles.md),
  Section 1, treats the rational-ball as well as positive-\(b_2\) ALE cases.
- [LeBrun, Proposition 4.1](https://arxiv.org/html/math/0003068) supplies
  the classical parameter-two inequality and its cscK equality structure;
  it does not by itself give the small-defect realization threshold.
- [Jiang–Naber, Theorem 1.6](https://arxiv.org/html/1605.05583) supplies
  full \(L^2\) curvature energy from bounded Ricci and local noncollapse.
  No bound on a Ricci derivative is part of that theorem.
- The harmonic-coordinate convergence and exact ALE inputs are listed
  with their precise roles in the inherited compact-realization proof;
  the proof above does not claim smooth convergence of approximate
  Einstein metrics without elliptic justification.
- [Finite algebra check](20260923_gauge_saturation_ke_check.py) verifies
  the amplitude inequality, rescaling and elementary four-dimensional form
  algebra, together with (28)–(29). It is not a computer proof of compactness, gauge solvability,
  or the theorem's PDE inputs.
