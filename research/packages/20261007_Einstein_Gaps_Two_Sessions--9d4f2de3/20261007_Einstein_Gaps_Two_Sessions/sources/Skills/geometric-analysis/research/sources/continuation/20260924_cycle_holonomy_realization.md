# Cycle deformation, monodromy detection, and exact bidisk realization

24 September 2026. This note supplies a global transition test for the
allowed product branch. Small deformation on individual balls is replaced
by a bound accumulated around actual generators of the base fundamental
group. The test detects finite mapping-class monodromy; it does not assume
it, assume a nearby Einstein metric, or require solving the tensor equation
near the input metric. Classical surface theory then realizes an exact
Einstein metric on the original smooth total space.

The retained [Round 18 theorem](../mathematics/current/round18_twisted_operator.md)
starts with finite monodromy and describes the complete Einstein operator
and nearby solutions. Its conclusion is not being rediscovered here. The
additional bridge is from a differential cycle budget to that global
topological hypothesis. Two uses of the inherited Dehn-twist construction
show independently why local smallness and degeneration of the fiber cannot
be ignored. No claim about the nonexistence of general Einstein metrics on
those examples is made.

## 1. An intrinsic cycle budget

Let
\[
                 F_f\longrightarrow M\xrightarrow{\pi}B_b
                 \qquad(f,b\ge2)
\tag{1}
\]
be a smooth oriented bundle of closed connected oriented surfaces. Let
\(g\) be any smooth metric on \(M\), let \(V=\ker d\pi\), and use the
orthogonal Ehresmann connection \(H=V^\perp\). A Riemannian submersion,
horizontal integrability, or constant fiber curvature is not required in
the main theorem. Compactness makes horizontal lifting complete along
each finite path.

For a piecewise smooth based loop \(\gamma:[0,1]\to B\), let
\(\Phi_t:F_0\to F_{\gamma(t)}\) be horizontal transport, with
\(F_0=F_{\gamma(0)}\). Define metrics on the fixed surface \(F_0\) by
\[
 h_t=\Phi_t^*(g|_{F_{\gamma(t)}}),\qquad
 A_t=h_t^{-1}\dot h_t,\qquad
 A_t^0=A_t-\tfrac12\operatorname{tr}(A_t)I,
\]
and define the conformal cycle variation
\[
 \mathcal J_g(\gamma)
       =\frac12\int_0^1\sup_{y\in F_0}
                          \|A_t^0(y)\|_{\mathrm{op}}\,dt.
\tag{2}
\]
The expression is invariant under orientation-preserving reparametrization
of the loop and under a fixed change of marking of \(F_0\). It measures
variation of its conformal structure, not a change in total fiber area.
No choice of a representative of a formal monodromy class replaces the
actual transport in (2).

Let \(\Gamma=(\gamma_1,\ldots,\gamma_N)\) be based loops at a **common**
point \(b_0\), whose homotopy classes generate \(\pi_1(B,b_0)\). Put
\[
                    \mathcal J_g(\Gamma)=\max_i\mathcal J_g(\gamma_i).
\tag{3}
\]
Let \(x_0\in\mathcal T_f\) be the marked conformal class of
\(g|_{F_0}\). The thickness condition below refers to the systole of the
unique curvature \(-1\) metric in this conformal class. It is not a
lower bound for four-dimensional balls or an injectivity-radius bound for
the given metric.

**Theorem A (global monodromy detection and realization).** For every
\(f\ge2\) and \(\iota>0\), there is \(\varepsilon_{f,\iota}>0\)
such that the following holds. If (1) has a metric and generating loops
with
\[
 \operatorname{sys}(x_0)\ge\iota,
 \qquad \mathcal J_g(\Gamma)<\varepsilon_{f,\iota},
\tag{4}
\]
then its mapping-class monodromy has finite image \(G\). The original
smooth bundle is smoothly isomorphic to
\[
                   (\widehat B\times F_f)/G\longrightarrow B,
\tag{5}
\]
where \(\widehat B\to B\) is the connected regular cover associated
to the monodromy kernel, \(G\) acts freely on \(\widehat B\), and its
action on \(F_f\) is by orientation-preserving hyperbolic isometries.
Consequently the same smooth \(M\) carries an exact metric \(h\) with
\[
                \operatorname{Ric}_h=-h,
       \qquad (\widetilde M,\widetilde h)
               \cong\mathbb H^2_{-1}\times\mathbb H^2_{-1}.
\tag{6}
\]
It is Kähler for two opposite orientations. No closeness between \(g\)
and \(h\) is asserted. The threshold is independent of the genus of
the base, the number of generators, diameter, total volume, and the
order of the eventually detected finite group.

In particular, a pointwise near-Einstein input satisfying (4) has the
Einstein output required by Yau26 in this input class. In fact (4) alone
is sufficient: the theorem does not need the near-Einstein hypothesis.
Deriving (4) from a weaker original geometric input is a separate task;
Sections 4--6 identify what data it must retain. The companion
[Ricci-to-monodromy theorem](20260924_ricci_monodromy_realization.md)
performs this step for minimal surface submersions, using the horizontal
Ricci identity and a based short-generator argument. Its hypothesis is
\(2\operatorname{diam}(B)\sqrt{\delta+\|(K_B+1)_+\|_\infty}
<\varepsilon_{f,\iota}\), with the same constant as below.

## 2. The exact Teichmüller displacement estimate

We use \(d_T(x,y)=\frac12\inf\log K(\phi)\), where the infimum is
over quasiconformal maps in the prescribed marking class. Write
\(\rho:\pi_1(B)\to\operatorname{Mod}(F_f)\) for the monodromy.

**Lemma 1.** For every based loop,
\[
                    d_T(x_0,\rho(\gamma)x_0)
                          \le\mathcal J_g(\gamma).
\tag{7}
\]
The convention for the mapping-class action may replace \(\rho(\gamma)\)
by its inverse; the displacement is unchanged.

**Proof.** For any two nonzero fixed tangent vectors \(v,w\) at a point
of \(F_0\), differentiating the ratio of their squared lengths gives
\[
 \left|\frac d{dt}\log\frac{h_t(v,v)}{h_t(w,w)}\right|
                    \le2\|A_t^0\|_{\mathrm{op}}.
\tag{8}
\]
At a fixed point take vectors attaining the largest and smallest length
ratios between \(h_1\) and \(h_0\). Integration of (8) implies that
the logarithm of the quasiconformal dilatation of the identity between
these two conformal metrics is at most
\(\int\sup\|A_t^0\|_{\mathrm{op}}dt\). The metric \(h_1\) is
the pullback of \(g|_{F_0}\) by the actual return map \(\Phi_1\),
whose mapping class is \(\rho(\gamma)\). The definition of \(d_T\)
therefore gives (7). This proof does not discard rotations of the
principal directions or require that the matrices \(A_t\) commute.
\(\square\)

Although the connection need not be flat, isotopy classes of its return
maps are invariant under based homotopy of loops and obey the group
relations. Indeed horizontal lifting over a smooth homotopy gives an
isotopy of the resulting fiber diffeomorphisms. Thus the actual classes
used in (7) form the monodromy representation, not an unrelated list of
almost-isometries.

## 3. Small moves in a thick fiber force one finite group

**Lemma 2 (uniform finite-isotropy neighbourhood).** For fixed
\(f,\iota\), some \(\varepsilon_{f,\iota}>0\) has the following
property. If \(x\in\mathcal T_f\), \(\operatorname{sys}(x)\ge\iota\),
and every member of a set \(S\subset\operatorname{Mod}(F_f)\) moves
\(x\) by less than \(\varepsilon_{f,\iota}\), then \(\langle S\rangle\)
is finite. The number of elements of \(S\) need not be bounded.

**Proof.** We use two classical inputs: the mapping-class action on
Teichmüller space is proper, with finite stabilizers, and the quotient of
the fixed-systole thick part is compact by Mumford's compactness theorem.
Thus a compact set \(K\subset\mathcal T_f\) meets every thick orbit.

If the lemma failed, after simultaneous conjugation there would be
\(x_j\in K\), \(x_j\to x\), and sets \(S_j\) generating infinite
groups, with \(d_T(x_j,sx_j)<1/j\) for all \(s\in S_j\). For these
elements,
\[
              d_T(x,sx)\le2d_T(x,x_j)+1/j\longrightarrow0
\tag{9}
\]
uniformly in \(s\). Properness gives a neighbourhood \(U\) of \(x\)
such that only finitely many group elements can carry a smaller compact
neighbourhood into one meeting \(U\). Equivalently, since \(d_T\) is
proper, the set \(\{s:d_T(x,sx)\le1\}\) is finite. Its nonzero
displacements have a positive minimum. Hence, for large \(j\), every
member of \(S_j\) lies in \(\operatorname{Stab}(x)\). This finite
group contains \(\langle S_j\rangle\), a contradiction. A possible
finite kernel of the action, including the genus-two hyperelliptic
involution, causes no problem. \(\square\)

**Proof of Theorem A.** Lemmas 1--2 place all the generating monodromies
in a single finite group. It is insufficient to check that each generator
has finite order separately; Lemma 2 is precisely what controls the group
they generate.

Kerckhoff's Nielsen realization theorem realizes the finite image \(G\)
as isometries of one curvature \(-1\) metric on the fiber. Give \(B\)
any hyperbolic metric and \(\widehat B\) its lift. The diagonal action
on \(\widehat B\times F_f\) is free because its first component is
a deck action, even if its fiber action has fixed points. The product
metric descends smoothly and satisfies (6).

It remains to identify the smooth total space, not merely its group.
The identity component \(\operatorname{Diff}_0^+(F_f)\) is contractible
by Earle--Eells. Therefore
\(B\operatorname{Diff}^+(F_f)\simeq B\operatorname{Mod}(F_f)\), and
oriented smooth surface bundles over \(B\) are classified by conjugacy
classes of their monodromy representations. The original bundle and the
constructed suspension have the same representation, hence are smoothly
bundle-isomorphic. Pulling back the descended metric proves existence on
the original \(M\). The two product complex structures are invariant
under the orientation-preserving diagonal action, so both descend.
\(\square\)

This proof is a composition with classical global surface theory, not a
new Nielsen realization theorem. It uses neither a global tensor inverse
nor the assumption that a candidate Einstein metric preserves the input
bundle. It constructs one that does; that suffices for existence.

## 4. Differential and opposite-form versions

Let \(\mathrm{II}(Y,Z)=(\nabla_YZ)^H\) for vertical \(Y,Z\). For a
horizontal vector \(X\), define the symmetric vertical endomorphism
\(S_X\) by
\[
                  g(S_XY,Z)=g(\mathrm{II}(Y,Z),X).
\]
For the projectable horizontal field that lifts \(\dot\gamma\),
\[
 (\mathcal L_Xg)|_{V\times V}=-2g(S_X\cdot,\cdot),
 \quad
 \mathcal J_g(\gamma)=\int_0^1
               \sup_{F_{\gamma(t)}}\|S_X^0\|_{\mathrm{op}}dt.
\tag{10}
\]
Indeed metric compatibility gives
\(g(\nabla_YX,Z)=-g(X,\nabla_YZ)\); the symmetric sum is the Lie
derivative. Pulling this identity back by \(\Phi_t\) gives (10).

Consequently, for a Riemannian submersion onto \((B,k)\),
\[
 \mathcal J_g(\Gamma)
 \le\Lambda_k(\Gamma)
       \sup_{|X|=1,\ X\in H}\|S_X^0\|_{\mathrm{op}},
 \qquad \Lambda_k(\Gamma)=\max_i\operatorname{Length}_k(\gamma_i).
\tag{11}
\]
Both factors matter. One cannot replace the right side by the local
deformation amplitude alone on a base with arbitrarily long essential
loops.

Here is a form-level version that keeps exact integrability explicit.
Suppose two smooth forms satisfy
\[
 *\omega_+=\omega_+,\quad *\omega_-=-\omega_-,\quad
 |\omega_\pm|^2=2,\quad d\omega_\pm=0.
\tag{12}
\]
Put \(\alpha=(\omega_++\omega_-)/2\) and
\(\beta=(\omega_+-\omega_-)/2\). Then \(\alpha,\beta\) have
rank two, \(\alpha^2=\beta^2=0\), and \(\alpha\wedge\beta\)
never vanishes, up to the choice of orientation/sign. Their kernel
distributions are transverse, orthogonal, and integrable: if a closed
constant-rank two-form annihilates \(Y,Z\), Cartan's formula gives
\(\iota_{[Y,Z]}\alpha=0\). This is an exact symplectic pair, not an
inference from approximate closedness.

Assume one distribution is the vertical tangent bundle of a smooth
surface bundle as in (1). This compact-leaf/leaf-space condition is not
automatic. If \(P\) is its orthogonal projection and \(J_\pm\) are
the endomorphisms associated with \(\omega_\pm\), then, with one
of the two signs,
\[
 P=\tfrac12(I\pm J_+J_-),\qquad
 |\nabla P|\le\frac1{\sqrt2}
                     (|\nabla\omega_+|+|\nabla\omega_-|).
\tag{13}
\]
We use Hilbert--Schmidt norms for tensors and the standard exterior norm
for forms; \(|\nabla J|^2=2|\nabla\omega|^2\). Also
\(\|S_X^0\|_{\mathrm{op}}\le |X||\nabla P|\). Thus, under the
Riemannian-submersion hypothesis, Theorem A applies if
\[
 \frac{\Lambda_k(\Gamma)}{\sqrt2}
       \bigl(\|\nabla\omega_+\|_\infty+
             \|\nabla\omega_-\|_\infty\bigr)
                              <\varepsilon_{f,\iota}.
\tag{14}
\]
The sharper loopwise test (10) is preferable when deformation is
inhomogeneous. No bound on second derivatives of these forms is used.

The actual-form supply theorem currently gives mean derivative bounds;
the collapsed-bulk theorem gives local limiting parallel forms. Neither
alone proves (12), the existence of the global fibration, or the cycle
estimate (10). The present theorem specifies a genuine sufficient
global input rather than declaring those missing implications automatic.

## 5. Sharpness I: thick fibers and uniform near-parallelism do not suffice

We extract additional consequences of the inherited fixed bundle \(E_D\),
not a newly constructed smooth object. Fix \(f,b\ge2\), a positive
Dehn twist \(D\) about a nonseparating curve of \(F_f\), and the
epimorphism \(u:\pi_1(B_b)\to\mathbb Z\) that sends one standard
generator to 1 and all others to 0. Its monodromy is \([D]^{u(\gamma)}\).
Choose a basepoint of the fiber off the twist support, so the suspension
has a section and
\[
 \pi_1(E_D)=\pi_1(F_f)\rtimes\pi_1(B_b),\qquad
 b_1(E_D)=2f+2b-1.
\tag{15}
\]
The last equality follows because a nonseparating twist acts by a
rank-one transvection on \(H_1(F_f;\mathbb R)\); its coinvariant
space has dimension \(2f-1\). In particular \(E_D\) admits no
Kähler metric, since the first Betti number of a compact Kähler manifold
is even. This simple obstruction is sufficient here; the stronger
inherited finite-cover obstructions are not needed.

Use the inherited area-preserving hyperbolic twist path on a fixed fiber:
\[
 h_z=du^2+a(u)^2(ds+z\zeta'(u)du)^2,
 \quad a(u)=a_0\cosh u,
 \quad h_1=D^*h_0,
 \quad dA_{h_z}=a(u)du\wedge ds.
\tag{16}
\]
It is extended by the fixed hyperbolic metric outside the collar.
The path \(z\in[0,1]\) is compact, so all its hyperbolic systoles
have a common positive lower bound. These are not globally trivial
deformations: an intermediate collar rotation is not a global isotopy
that removes \(D\).

On a long pinching base collar set
\[
 g_L=dt^2+b_L(t)^2d\theta^2+h_{z(t)},\qquad
 b_L(t)=\ell\cosh t,\quad z(t)=\eta(t/L),
\tag{17}
\]
where \(\eta\) is monotone from 0 to 1 and constant near the ends.
The source construction closes (17) by the marked Dehn twist, on the
fixed \(E_D\), and proves
\[
 \|\operatorname{Ric}_{g_L}^{\sharp}+I\|_\infty=O(L^{-1}),
 \qquad \operatorname{Vol}(g_L)=16\pi^2(f-1)(b-1).
\tag{18}
\]
No region-volume argument is used for this maximum-norm estimate.

The horizontal and vertical area forms \(\alpha_L,\beta\) glue
globally, are closed, and satisfy
\[
 \omega_{+,L}=\alpha_L+\beta,\qquad
 \omega_{-,L}=\alpha_L-\beta,
 \quad *\omega_{\pm,L}=\pm\omega_{\pm,L},
 \quad |\omega_{\pm,L}|^2=2.
\tag{19}
\]
Closedness uses the **fixed pointwise fiber area form** in (16), not
just its fixed integral. The marked gluing preserves that form. The
horizontal distribution is flat, and the only mixed second fundamental
terms are produced by \(\partial_th_{z(t)}\). Writing
\(Q=a\zeta'\), \(v=Qz'\), their orthonormal matrix is
\[
                   S_{\partial_t}
                    =-\frac v2\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{20}
\]
Thus \(|\nabla P|=|v|\), and the connection on the two rank-two
blocks gives \(|\nabla\omega_{\pm,L}|\le C|v|\). Therefore
\[
                 \|\nabla\omega_{\pm,L}\|_\infty=O(L^{-1}).
\tag{21}
\]
The forms are also harmonic, by (19) and closedness.

Nevertheless (15) prohibits any exact Kähler output. Along a loop that
crosses the twist collar once and otherwise remains in the product
region, (20) and monotonicity give the **nonvanishing** cycle budget
\[
                  \mathcal J_{g_L}(\gamma)
                             =\frac12\|Q\|_\infty.
\tag{22}
\]
In particular it is at least \(d_T(x_0,Dx_0)>0\). An infinite-order
twist cannot fix a hyperbolic conformal structure, whose automorphism
group is finite. The deformation amplitude in (21) vanishes, but the
length over which it accumulates diverges. At least one essential cycle
retains the global information.

Thus even **closed, nowhere-zero, exactly normalized opposite forms**,
uniform near-parallelism, pointwise near-Einstein curvature, and thick
fiber conformal classes do not imply global KE realization without
control of transition cycles. This is stronger than merely observing
that an exceptional set in an average theorem might carry topology.

## 6. Sharpness II: vanishing cycle distortion does not replace fiber thickness

Keep the same smooth bundle and now keep a fixed hyperbolic base and a
fixed base collar. Pinch the twisting curve in the fiber to length
\(\lambda\downarrow0\). In its hyperbolic collar use the angular
period 1 and write \(a_\lambda(u)=\lambda\cosh u\). Fix a nonnegative
smooth \(\chi\), supported in \((-u_0,u_0)\), with positive integral,
and choose
\[
 C_\chi=\int_{-u_0}^{u_0}\chi(u)\operatorname{sech}u\,du,
 \qquad
 \zeta'(u)=\frac{\chi(u)}{C_\chi\cosh u}.
\tag{23}
\]
The integral of \(\zeta'\) is 1, so the return map is still one full
Dehn twist, not a small fractional topological twist. But
\[
                     Q_\lambda=a_\lambda\zeta'
                            =\lambda\chi/C_\chi
\tag{24}
\]
and all its fixed-order \(u\)-derivatives are \(O(\lambda)\).
The increasingly wide hyperbolic collar contains this fixed support.
Extend the hyperbolic fiber metrics using any fixed marked pinching
family; the construction remains on the same smooth bundle because its
mapping class remains \([D]\).

Take a fixed smooth monotone \(z(t)\) across the fixed base collar.
For completeness, in the orthonormal frame of (17) the inherited exact
Ricci defect is
\[
 \operatorname{Ric}+g=
 \begin{pmatrix}
 -v^2/2&0&0&(v_u+2jv)/2\\
 0&0&0&0\\
 0&0&-v^2/2&-(v_t+kv)/2\\
 (v_u+2jv)/2&0&-(v_t+kv)/2&v^2/2
 \end{pmatrix},
 \quad j=\tanh u,\ k=b'/b,\ v=Q_\lambda z'.
\tag{25}
\]
All the functions on the fixed base collar have bounded derivatives.
Equations (24)--(25), together with the product metric off the supports,
therefore give
\[
 \delta_-(g_\lambda)=O(\lambda),\qquad
 \|\nabla\omega_{\pm,\lambda}\|_\infty=O(\lambda),\qquad
 \mathcal J_{g_\lambda}(\Gamma)=O(\lambda).
\tag{26}
\]
A fixed standard based generating system has bounded base lengths. Its
only nontrivial return map is \(D\); the other loops can be chosen to
avoid the active collar or to run along it at constant \(t\). In (26)
the forms still satisfy all the exact conditions (19).

The image of monodromy is nevertheless infinite cyclic, and (15) still
rules out Kähler geometry. The missing hypothesis is precisely the
fiber conformal thickness: its systole is at most \(\lambda\). This
is an explicit small-displacement failure at the boundary of moduli
space, not a failure of Lemma 2. Both circle collapse and long fiber
diameter are genuine; the base geometry does not degenerate.

### These are also actual bilateral near-saturation examples

Both constructions have symplectic structures (19) in the two
orientations. They have
\[
 \tau(E_D)=0,\quad A=2\chi(E_D)=8(f-1)(b-1)>0,
 \quad V=2\pi^2A,
 \quad p_\pm\ge A.
\tag{27}
\]
For the signature, the chosen monodromy extends over a handlebody
because it factors through one free generator; the surface bundle is
the boundary of the resulting oriented five-dimensional bundle. For
the class supply, \(b_+=b_->1\), so Taubes's symplectic canonical
classes have nonzero ordinary SW invariants in the two orientations.
They are actual for every metric and throughout the conformal weight
construction used in the inherited first-line estimates. Their squares
are \(A\), hence their positive projected squares are at least \(A\).
These class-supply facts and the weighted-solvability passage are the
same inherited classical inputs, not a new gauge theorem here.

Write \(q_\pm\) for the bilateral normalized deficits of I25/I30.
The exact inherited energy identity gives
\[
 q_\pm=\frac9{2V}
       \left[\int|\operatorname{Ric}|^2-8\pi^2(2p_\pm-A)\right].
\]
Since \(\fint|\operatorname{Ric}|^2\le4(1+\delta_-)^2\),
\[
                    0\le q_\pm\le36\delta_-+18\delta_-^2\to0.
\tag{28}
\]
Thus the two sharpness examples lie in the actual bilateral gauge
near-saturation regime, not only in an abstract almost-product class.
They do **not** disprove Yau26: arbitrary non-Kähler Einstein existence
on \(E_D\) remains undecided by these statements.

## 7. What this bridge changes

The inputs (4) are nonempty and not merely the equation for an existing
Einstein metric. Every finite-monodromy bundle has a connection and
invariant fiber metric with \(\mathcal J=0\); the base metric and its
diameter can be arbitrary. Smooth changes of the metric and connection
retain (4) for a fixed generating system when sufficiently small, while
the input need not be Einstein. More generally, trace changes of fiber
metrics do not affect (2), so input scalar curvature and scale are not
required to be close to a product normalization.

Unlike Round 18, one need not know the monodromy image in advance, supply
an exact reference metric, or discard slow Teichmüller coefficient
functions. Their cumulative deformation is precisely what (2) measures.
The proof constructs the global quotient only after this data has forced
finite monodromy. It does not classify all nearby Einstein metrics or
provide a uniform inverse on the quotient; those remain distinct claims
in Round 18.

For the first line, the resulting mathematical choice is specific:
local product estimates must be accompanied by a mechanism controlling
global cycle distortion and escape toward the boundary of fiber moduli.
Making every local form derivative small, even uniformly with exact
closedness, does not remove those two independent alternatives. The
actual examples above rule out that proposed shortcut while Theorem A
gives a sufficient global replacement. No new smooth topology or
world-first priority is asserted for this composition.

## 8. Sources and attribution

- D. Mumford, *A remark on Mahler's compactness theorem*, Proceedings of
  the AMS **28** (1971), 289--294. The fixed-genus hyperbolic systole
  criterion supplies compact thick moduli. [Primary article](https://doi.org/10.2307/2037802).
- S. P. Kerckhoff, *The Nielsen realization problem*, Annals of
  Mathematics **117** (1983), 235--265, Theorems 4--5. The original text
  also records proper discontinuity and finite isotropy of the
  mapping-class action. [Primary article](https://annals.math.princeton.edu/1983/117-2/p02);
  [full text](https://poisson.phc.dm.unipi.it/~camponovo/Kerckhoff-NielsenRealizationProblem-1983.pdf).
- C. J. Earle and J. Eells, *The diffeomorphism group of a compact
  Riemann surface*, Bulletin of the AMS **73** (1967), 557--559,
  Theorem 1(c); and *A fibre bundle description of Teichmüller theory*,
  Journal of Differential Geometry **3** (1969), 19--43. The contractible
  identity component supplies the smooth bundle classification used
  above. [1967 primary announcement](https://doi.org/10.1090/S0002-9904-1967-11746-4);
  [1969 article](https://doi.org/10.4310/jdg/1214428816).
- The actual fixed \(E_D\) construction, the full Ricci matrix, and
  the topology/gauge inputs are retained in
  [the global paper, Section 7](../mathematics/current/skill/research/20260916_global.tex),
  and [the detailed construction](../mathematics/current/skill/research/20260912.tex),
  labels `BUN:slow`, `BUN:ricci-matrix`, `BUNTOP:object`.
  The two new cycle-budget comparisons are consequences of those inputs.
- [Bilateral compact realization](20260924_bilateral_realization.md)
  and [collapsed bilateral bulk](20260924_collapsed_bilateral_bulk.md)
  have different hypotheses and conclusions from this note. Neither
  is silently applied to infer a smooth global leaf space.

The accompanying finite check verifies the two-dimensional variation
normalizations, the shear shape matrix, the transvection rank, and (28).
It does not verify bundle classification, gauge solvability, or the
analytic existence argument by computation.
