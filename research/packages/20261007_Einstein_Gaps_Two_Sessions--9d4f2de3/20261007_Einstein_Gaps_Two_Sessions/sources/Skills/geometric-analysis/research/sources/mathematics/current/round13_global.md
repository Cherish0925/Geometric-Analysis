# Volume nonattainment obstructs continuous all-mode Einstein repair

21 September 2026.

## 1. The new implication

Fix a closed integer-shear manifold \(M=M(h,g;u,f)\), with
\(h\ge1\), \(g\ge2\), and nonzero integral shear, satisfying the
construction and topology theorems of Rounds 11--12. Put

\[
 V_*:=\frac{4\pi^2}{9}\chi(M).
\]

The earlier results supply smooth metrics \(G_\ell\), \(0<\ell<\ell_0\),
on this one marked smooth manifold, with

\[
 \operatorname{Vol}(G_\ell)=V_*,\qquad
 \|G_\ell^{-1}\operatorname{Ric}_{G_\ell}+3I\|_\infty\to0.
 \tag{1}
\]

Every exact Einstein metric on \(M\) has negative Einstein constant.
After normalization to \(\operatorname{Ric}_H=-3H\), it satisfies

\[
                    \operatorname{Vol}(H)>V_* .          \tag{2}
\]

The strictness in (2) follows from the actual monopole scalar estimate:
equality would produce a parallel self-dual two-form and hence a Kähler
metric, contrary to the established virtual Kähler obstruction. It does
not follow merely from the existence of a degenerating minimizing sequence.
The precise source is [Round 11, Sections 2 and 6](round11_variational.md).

**Theorem 1 (no connected exact repair).** There is no continuous family
of normalized Einstein metrics \(H_\ell\), \(0<\ell<\ell_1\), continuous
in the smooth topology or in a fixed \(C^{k,\alpha}\) topology,
\(k\ge2\), such that

\[
 \operatorname{Ric}_{H_\ell}=-3H_\ell,\qquad
 \|G_\ell^{-1}(H_\ell-G_\ell)\|_{L^\infty,\mathrm{op}}
       \longrightarrow0.
 \tag{3}
\]

The same conclusion holds with \(H_\ell\) replaced in (3) by arbitrary
diffeomorphic pullbacks. The pullbacks need not be continuously selected
if the classes \([H_\ell]\) form a continuous path in Einstein moduli.
No invariance, adapted splitting, local Killing field, or restriction on
the correction modes is imposed.

This is an application of classical Einstein-moduli volume constancy to
the sharp but unattained volume of the new closed construction. The
moduli fact is not claimed as new. Unlike the preceding local-symmetry
obstruction, this result also excludes a continuous family of completely
nonsymmetric small corrections. It does not exclude an isolated exact
metric or a sequence in different moduli components.

## 2. Volume constancy and the proof

Let \(H(t)\) be a \(C^1\) path of metrics satisfying
\(\operatorname{Ric}_{H(t)}=\lambda H(t)\) for a fixed nonzero
\(\lambda\). Set \(q=\partial_tH\). The scalar-curvature variation is

\[
 \partial_t s=-\langle\operatorname{Ric},q\rangle
              +\operatorname{div}\operatorname{div}q
              -\Delta\operatorname{tr}q.
\]

Here \(s=n\lambda\) is constant in \(t\). Integrating over the closed
manifold gives

\[
 0=-\lambda\int_M\operatorname{tr}_{H}q\,d\mu_H,
 \qquad
 \frac{d}{dt}\operatorname{Vol}(H)
        =\frac12\int_M\operatorname{tr}_{H}q\,d\mu_H=0.
 \tag{4}
\]

Thus the result for piecewise \(C^1\) paths is elementary. For arbitrary
continuous paths use the classical local analytic structure of Einstein
premoduli: normalized scalar curvature is locally constant on unit-volume
Einstein moduli; equivalently, volume is locally constant when the
nonzero Einstein constant is fixed. In particular volume is constant on
each connected component, including obstructed or singular components.
The needed statement is explicitly recalled in
[Andersson--Moncrief, Section 2, p. 9 of the preprint](https://arxiv.org/pdf/0908.0784),
with its reference to Besse, Corollary 12.52. It does not require an
integrable deformation space. Their later dynamical theorems do impose
integrability, but those theorems are not being used here.

Write
\(\varepsilon_\ell=\|G_\ell^{-1}(H_\ell-G_\ell)\|_\infty\).
For \(\varepsilon_\ell<1\), the pointwise eigenvalue bounds give

\[
 (1-\varepsilon_\ell)^2V_*
 \le\operatorname{Vol}(H_\ell)
 \le(1+\varepsilon_\ell)^2V_*.
 \tag{5}
\]

Consequently (3) forces \(\operatorname{Vol}(H_\ell)\to V_*\).
Volume constancy makes that volume equal to \(V_*\) throughout the
connected family, contradicting (2). Diffeomorphisms do not change
volume, so the same proof treats the marked-distance formulation.

The proof also works for any continuous Einstein family whose normalized
volumes tend to \(V_*\), even without a tensor comparison to \(G_\ell\).

## 3. Componentwise distance and the only remaining accumulation mechanism

Let \(\mathcal E_{-3}(M)\) be the moduli space of metrics with
\(\operatorname{Ric}=-3g\), modulo diffeomorphisms. For a connected
component \(\mathcal C\), write its constant volume as \(V_{\mathcal C}\).
Equation (2) implies \(V_{\mathcal C}>V_*\). Define the relative distance

\[
 d_\ell(\mathcal C)
 :=\inf_{H\in\mathcal C,\,\varphi\in\operatorname{Diff}(M)}
 \|G_\ell^{-1}(\varphi^*H-G_\ell)\|_\infty.
\]

The upper half of (5) does not need \(\varepsilon<1\), and yields

\[
 \boxed{
 d_\ell(\mathcal C)
 \ge\sqrt{V_{\mathcal C}/V_*}-1>0
 \quad\hbox{for every }\ell .}
 \tag{6}
\]

Thus the constructed family stays a definite relative \(C^0\) distance
from every *fixed* exact Einstein component, including components with
no local symmetry. The constant depends on the component.

**Corollary 2.** If normalized exact metrics \(H_j\) are relatively
\(C^0\)-close to \(G_{\ell_j}\), with \(\ell_j\to0\), then
\(\operatorname{Vol}(H_j)\to V_*\) from above. After passing to a
subsequence they lie in pairwise distinct moduli components, with
pairwise distinct volumes. They cannot have a smoothly convergent
subsequence modulo diffeomorphisms.

For the component claim, finitely many strictly positive component
volume gaps cannot approach zero. A strictly decreasing subsequence of
volumes gives distinct volume values and hence distinct components.
A smooth limit would remain normalized Einstein with volume \(V_*\),
contradicting (2).

In particular, finiteness of the normalized Einstein volume spectrum
near \(V_*\) would exclude all sufficiently small repairs of (1).
Such finiteness has not been proved here. No compactness or component
finiteness is inferred just from fixed topology and bounded total
curvature energy. The unrestricted existence of a distant Einstein
metric remains a separate question even if near-minimum repair is
excluded.

## 4. Consequence for the full nonlinear repair operator

This consequence records what an all-mode inverse estimate would have
to overcome. It is not an assertion that a particular Hölder or Sobolev
inverse has already been computed.

Let
\(F_\ell:X_\ell\supset B(0,R_\ell)\to Y_\ell\)
be a complete gauge-fixed Einstein equation about \(G_\ell\).
Assume the Banach spaces admit continuous local trivializations in
\(\ell>0\), with both \(F_\ell(v)\) and \(DF_\ell(v)\) jointly
continuous after those trivializations, the latter in operator norm.
Require also that the realization \((\ell,v)\mapsto G_\ell+v\) is
continuous into a fixed \(C^{k,\alpha}\) metric topology, \(k\ge2\),
locally for \(\ell>0\). This holds for the usual geometric
\(C^{k,\alpha}\) correction spaces; a weaker space needs a separate
elliptic regularity and gauge argument. Suppose:

1. Every sufficiently small zero \(v\) gives a genuine smooth metric
   \(H=G_\ell+v\) satisfying \(\operatorname{Ric}_H=-3H\); the
   gauge equation has been removed by an actual argument.
2. \(\|G_\ell^{-1}v\|_\infty\le C_0\|v\|_{X_\ell}\), uniformly.
3. \(L_\ell=DF_\ell(0)\) is an isomorphism with
   \(\|L_\ell^{-1}\|\le B_\ell\), and
   \(\|F_\ell(0)\|\le r_\ell\).
4. On the ball used below,
   \(\|DF_\ell(v)-DF_\ell(w)\|
          \le K_\ell\|v-w\|_{X_\ell}\).

Use positive continuous upper bounds \(B_\ell,r_\ell,K_\ell\).
Zero residual would already contradict (2). Let
\(\rho_\ell=2B_\ell r_\ell\), and require
\(\rho_\ell<R_\ell\). The usual fixed-point map is

\[
 T_\ell(v)=-L_\ell^{-1}F_\ell(0)
  -L_\ell^{-1}\bigl(F_\ell(v)-F_\ell(0)-L_\ell v\bigr).
\]

Taylor's integral formula gives, for \(\|v\|\le\rho_\ell\),

\[
 \|T_\ell(v)\|
 \le B_\ell r_\ell+\tfrac12 B_\ell K_\ell\rho_\ell^2,
 \qquad
 \operatorname{Lip}(T_\ell)
 \le B_\ell K_\ell\rho_\ell
 =2B_\ell^2K_\ell r_\ell.
 \tag{7}
\]

If for every sufficiently small \(\ell\),

\[
 2B_\ell^2K_\ell r_\ell\le q<1,
 \qquad B_\ell r_\ell\longrightarrow0,
 \tag{8}
\]

then \(T_\ell\) maps its ball strictly into itself and is a contraction.
It produces a unique zero there. These zeros depend continuously on
\(\ell>0\): locally identify the Banach spaces and rescale the ball to
the unit ball; continuous contraction maps with common bound \(q<1\)
have continuous fixed points. Equivalently, the derivative at the zero
is invertible by the same Neumann estimate, and local implicit-function
branches coincide with the unique contraction zero. Continuity of the
ball radii and the strict interior estimate ensure this patching.
The resulting exact metrics satisfy (3), contradicting Theorem 1.

**Corollary 3 (failure of a tame full-mode Newton regime).** The hypotheses
above and (8) cannot all hold for every sufficiently small \(\ell\).
This includes operators with unrestricted angular and transverse modes.
A complement inverse alone does not meet the hypotheses: a genuine
kernel requires its full obstruction equation, which may prevent a
continuous family of zeros.

For an illustrative rate consequence, suppose
\(r_\ell\le C/|\log\ell|\), \(K_\ell\le K_0\), the small-radius
and gauge hypotheses hold, and the complete operators are continuously
invertible for all small \(\ell\). Then

\[
             B_\ell=o\bigl(\sqrt{|\log\ell|}\bigr)
             \quad\text{is impossible}.                 \tag{9}
\]

Indeed (9) would imply both parts of (8). Thus either invertibility,
the nonlinear/gauge regime, or the proposed inverse growth control must
fail arbitrarily far into the degeneration. Formula (9) is conditional
on the specified Banach norms and their uniform estimates; it is not a
pointwise-in-\(\ell\) lower bound for an unspecified spectral operator.

## 5. What both monopole orientations actually contribute

For completeness, the earlier all-metric inputs also yield a precise
period constraint, but do not by themselves turn the volume interval
into nonexistence. In the positive orientation the canonical classes
from Round 12 obey

\[
 a^2=Q,\qquad b^2=-Q,\qquad a\cdot b=0,\qquad Q=2\chi.
\]

For an exact normalized Einstein metric \(H\), put
\(t=\operatorname{Vol}(H)/V_*\). Scalar monopole estimates in the two
orientations give

\[
 \|a_H^-\|^2\le Q(t-1),\qquad
 \|b_H^+\|^2\le Q(t-1).                                \tag{10}
\]

Meanwhile Chern--Gauss--Bonnet and signature, using the curvature-
operator norm for \(W^\pm\), give

\[
 \int|W_H^+|^2=\int|W_H^-|^2
      =4\pi^2\chi-3\operatorname{Vol}(H),
 \qquad 1<t<3.                                         \tag{11}
\]

The upper endpoint would make \(W=0\) and hence the metric hyperbolic,
contrary to the embedded \(\mathbb Z^2\) subgroup. The lower endpoint
is excluded by (2). Equation (10) says that hypothetical Einstein
metrics at volumes approaching \(V_*\) must also approach the two
canonical Hodge polarizations. It does not force equality at a positive
volume excess.

The two orientations cannot be pooled into a single positive-square
monopole set. Nor does an entropy lower bound supply the missing volume
upper bound: a bound \(h(H)^4\operatorname{Vol}(H)\ge A\), combined with
the normalized Ricci comparison \(h(H)\le3\), yields
\(\operatorname{Vol}(H)\ge A/81\), in the lower-bound direction.
No additional entropy theorem on these particular sheared groups is
assumed here.

## 6. Position in the research

The added statement is the componentwise and continuous-family
obstruction, together with its full-mode inverse consequence. It uses
the sharp volume and nonattainment already proved in Round 11, rather
than claiming a new Seiberg--Witten estimate or a new general moduli
theorem. It is stronger than exclusion of symmetric repairs, but weaker
than exclusion of every exact repair sequence.

The newly isolated alternative is specific: a vanishing-size exact
repair sequence would require normalized Einstein volume values
accumulating at the unattained sharp value across infinitely many moduli
components. Proving that this cannot happen for these groups, or
constructing such a sequence, would resolve a substantially more precise
problem than an unspecified failure of the implicit-function theorem.
Neither alternative has been settled here, and a distant normalized
Einstein metric would still remain relevant to Yau26.

## References and verification

- [Round 11 variational proof](round11_variational.md): sharp scalar and
  Ricci-lower-bound volume, equality case, and its nonattainment.
- [Round 11 closed construction](round11_closed_gluing.md): fixed marked
  topology, all-block Ricci estimate, and exact volume.
- [Round 12 basic classes](round12_global.md): both canonical orientations
  and the separate monopole capacities.
- [Andersson--Moncrief, *Einstein spaces as attractors for the Einstein
  flow*, Section 2](https://arxiv.org/pdf/0908.0784): explicit local
  constancy statement for normalized Einstein moduli; the smooth-path
  argument was derived directly in (4).
- [LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg--Witten
  Theory*](https://arxiv.org/pdf/math/0003068): classical monopole scalar
  estimates and Chern--Weil conventions.

`round13_global_check.py` checks the normalization, first-variation
coefficient, determinant exponent, and contraction inequalities. It
does not certify the imported topology or solve an Einstein equation.
