# The integral gap with polarization-dependent monopoles

## Result

The integral theorem applies to the full polarized Seiberg--Witten
connected-sum setting of LeBrun's Proposition 3.2, not only to complex
surfaces. In particular, the restriction `b_+(X)>1` can be removed from
the integral blow-up corollary. The analytic proof only needs a monopole
on the conformal class of the metric being tested, not one spin-c
structure that works simultaneously for all polarizations.

**General theorem.** Let `N` be a closed oriented four-manifold with
`b_+(N)>0` and `T_0=2\chi(N)+3\tau(N)>0`. Suppose a spin-c structure
with real Chern class `c` has a nonzero ordinary Seiberg--Witten
invariant. If `b_+(N)=1`, require nonvanishing in the chamber of
sufficiently small perturbations, not merely in an arbitrary chamber.
Put `A=c^2`; nonnegative expected dimension gives `A\ge T_0>0`.
For

\[
 M=N\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3),
 \qquad T_M=T_0-k-4\ell,
\]

the round-four integral theorem implies

\[
 \boxed{\mathcal E(g)+(T_M/A-2/3)_+\ge c_* .}              \tag{G1}
\]

The constant is universal. A useful weaker form is

\[
 \boxed{\mathcal E(g)+
         (1/3-(k+4\ell)/T_0)_+\ge c_* .}                 \tag{G2}
\]

This includes symplectic bases when their canonical class has the
specified nonzero invariant. For `b_+>1`, Taubes' invariant provides
this input whenever `c_1^2>0`. For `b_+=1`, the small-perturbation
chamber condition remains part of the statement; a symplectic structure
alone must not be substituted for it. See Section 2a for the insertion
and chamber details.

**Complex-surface corollary.** Let `X` be a closed minimal complex surface of general type,
`A=c_1^2(X)>0`, and

\[
 M=X\#k\overline{\mathbb{CP}}^{\,2}
          \#\ell(S^1\times S^3),\qquad k,\ell\ge0.
\]

Assume the integral calibration theorem proved in
[round 4](skill/references/rounds/round4_rigidity.md). There is a universal
constant `c_*>0`, independent of `X,k,ell` and the smooth metric `g`, such
that

\[
 \boxed{\quad
 \mathcal E(g)+
       \left(\frac13-\frac{k+4\ell}{A}\right)_+\ge c_* ,
 \qquad
 \mathcal E(g)=\inf_{\lambda\ne0}
  \frac{\int_M|\operatorname{Ric}_g-\lambda g|_g^2\,d\mu_g}
       {\lambda^2\operatorname{Vol}_g(M)} .\quad}             \tag{1}
\]

In particular, this includes `b_+(X)=1`. The constant is the same universal
constant supplied by the earlier topology-transfer argument. No new
geometric assumption is needed. This is an extension of the scope of
that analytic theorem, not an independent replacement for its proof.

## 1. The precise equation needed by the integral proof

Fix a metric `g` on a closed oriented four-manifold and a spin-c structure
`s` with real first Chern class `a`. The sufficient input is

\[
 \text{for every smooth }f>0,\qquad
 D_A\Phi=0,\qquad -iF_A^+=f\sigma(\Phi)
 \quad\text{has a solution on }(M,g).                       \tag{2}
\]

The same spin-c structure must work as `f` varies. It may depend on the
original metric `g`. Neither a chamber-independent invariant nor a
finite set of all-metric monopole classes is used in the analytic proof.

To see the minimal hypothesis directly, suppose the unperturbed equations
for `s` are solvable for every metric conformal to `g`. For a prescribed
`f`, solve them on `\widehat g=f^{-2}g`. Conformal covariance identifies
the spinor bundles and gives

\[
 \Phi=f^{-3/2}\widehat\Phi,\qquad
 D_A^g\Phi=0,\qquad
 \sigma_g(\Phi)=f^{-1}\sigma_{\widehat g}(\widehat\Phi).
\]

The self-dual decomposition of two-forms is conformally invariant in
dimension four, so these are exactly (2). This is the argument in
[LeBrun, Lemma 3.7](https://arxiv.org/pdf/math/0611450), with its existence
input restricted to the one conformal class where it is needed.

In particular, let `H=H_g^+` be the polarization determined by `g` and
suppose `s` is a *polarized monopole*: its unperturbed equations are
solvable for every `H`-adapted metric. Every metric conformal to `g` is
`H`-adapted. Indeed, a self-dual harmonic two-form is equivalently a
closed self-dual two-form, and both conditions are unchanged by conformal
rescaling. A polarized monopole therefore supplies (2).

This is stronger than knowing one solution for `g`, but weaker than
requiring an all-metric monopole class. There is no variation across a
chamber wall while the weight is changed: the polarization remains fixed.

## 2. Polarized topology-transfer lemma

Put `T=2\chi(M)+3\tau(M)`. Suppose every smooth metric `g` admits a
spin-c structure as in (2), with

\[
                    (a_g^+)^2\ge A>0,\qquad a^2\ge T.       \tag{3}
\]

Then the round-four proof gives

\[
 \mathcal E(g)+(T/A-2/3)_+\ge c_*>0.                        \tag{4}
\]

Here is why the proof survives the weakened existence hypothesis.

* The truncated weights are constructed separately on each fixed metric.
  Equation (2) supplies every auxiliary spinor used in the limiting
  smooth-majorant argument. No derivative of `a` or continuity of its
  selection in metric space occurs.
* The scalar and spectral monopole inequalities use these same weighted
  solutions. Their topological right-hand side is `(a_g^+)^2` for this
  one spin-c structure.
* The determinant-connection energy is controlled by
  `\|F_A\|_2^2=2\|F_A^+\|_2^2-4\pi^2a^2`. Thus the square condition
  in (3), not chamber independence, is the relevant topological input to
  the second-order estimate.
* The smooth Weyl model and weak Bianchi self-test are intrinsic operations
  on `g`. They use no comparison of monopoles on different metrics.

For the negative normalization put `r=\fint|Ric+g|^2` and
`d=(T/A-2/3)_+`. The estimates from the original proof are

\[
 \kappa\le1215(r+d)\quad(r\le1),\qquad
 \frac{A}{V}\le\frac{4+r}{4\pi^2}.
\]

If `r\le1/4`, Chern--Weil gives `4\pi^2T\ge V/4>0`. Hence (3)
makes the negative-square cost `B_a=(-a^2)_+/V` vanish in the only branch
where a small-error contradiction is needed. The integral calibration
gap therefore yields `r+d\ge\min\{1/4,c/1215\}`. The other branch is
immediate.

For positive normalization the classical scalar monopole bound and
Chern--Weil give `\fint|Ric-g|^2+d>1/4`, as in
[the all-sign argument](skill/references/rounds/round4_all_sign_gap.md).
Constant rescaling preserves `H` and (3). Taking the scale infimum in
both signs proves (4). This proves the lemma without introducing any
new estimates into the round-four analytic argument.

## 2a. General bases: dimensions and insertions

For the general theorem, nonzero invariant means that some homogeneous
insertion `z` has

\[
 SW_{N,\mathfrak s}(z)\ne0,\qquad
 \deg z=d_N=(c^2-T_0)/4.
\]

The insertion algebra is `\mathbb Z[U]\otimes\Lambda^*(H_1(N)/torsion)`
with `\deg U=2` and degree one for a loop. This includes the
zero-dimensional invariant, for which `z=1`; it does not assume that
every nonzero invariant is a zero-dimensional count.

The ordinary blow-up formula preserves `d_N` for Chern classes
`c\pm E`. Each added `S^1\times S^3` raises the expected dimension by
one. The polynomial-valued formulation and the chamber-compatible
blow-up formula are explicit in
[Ozsvath--Szabo, Section 1 and Theorem 3.2](https://arxiv.org/pdf/math/0005268).
Their Proposition 2.2 and Remark 2.3 give the surgery identity
`SW_{N',s'}(z\,\mu(C))=SW_{N,s}(z)` and raises dimension by one;
surgery on a standard null-homologous two-sphere in a ball is the
`S^1\times S^3` addition, with `C` its new loop. Remark 2.3 explicitly
retains `b_+=1` when the two invariants use corresponding chambers.
Accordingly the gluing formula used in
[LeBrun, Proposition 3.2](https://arxiv.org/pdf/math/0003068) retains
the original insertion `z` and adds the loop insertions
`\beta_1\wedge\cdots\wedge\beta_\ell`. The resulting dimension is

\[
 \frac{(c^2-k)-(T_0-k-4\ell)}4=d_N+\ell.                 \tag{G3}
\]

For each polarization `H` on `M`, choose the exceptional signs by (5)
below. The chamber-compatible polarized gluing gives a nonzero
invariant at `H` for the selected class `a_H=c-\sum E_j`, with these
insertions. This is a classical gauge-theoretic input, not a deduction
from the dimension identity (G3). In the zero-dimensional base case
the inserted invariant is exactly the holonomy invariant written in
LeBrun's proof. With a positive-dimensional base invariant, its original
insertions are retained rather than replaced by the new loop factors.

The Lorentzian intersection form when `b_+(N)=1` makes the base
small-perturbation chamber unambiguous over all metrics: since `c^2>0`,
`c_H^+` never vanishes. The base invariant therefore persists under
changes of polarization. This says nothing about the invariant in the
other, large-perturbation chamber. After the connected sums it is the
*selected polarized* invariant which is used, as in Section 3.

The chamber matching can also be seen explicitly. Orient the unit
generator `\omega` of `H` so that `c\cdot\omega>0`. Its projection
`\omega_N` to the base summand has positive square, lies in the
corresponding component of the base positive cone, and satisfies
`c\cdot\omega_N=c\cdot\omega`. Condition (5) makes
`E_j\cdot\omega\le0`. Therefore

\[
 a_H\cdot\omega=c\cdot\omega-\sum_jE_j\cdot\omega
                       \ge c\cdot\omega>0.               \tag{G5}
\]

The signs defining the small-perturbation chamber on the base and the
blow-up agree. This is why the compatible chamber in the gluing formula
is the actual small-perturbation chamber at the prescribed metric,
rather than an arbitrary chamber chosen only to make an invariant
nonzero. The handle additions do not change the second-cohomology
intersection form.

Projection and square computations now give

\[
 (a_H^+)^2\ge c^2=A,\qquad
 a_H^2=c^2-k\ge T_0-k=T_M+4\ell\ge T_M.                 \tag{G4}
\]

The lemma proves (G1). For (G2), simply apply the same lemma using the
smaller projection budget `T_0` instead of `A`; no comparison of ratios
with an uncontrolled sign is needed. This completes the general proof.

## 3. The actual chamber input for general-type surfaces

For the stated `X`, write `c=c_1(X)` pulled back to `M` and choose
exceptional generators `E_j` with `E_i\cdot E_j=-\delta_{ij}` and
`c\cdot E_j=0`. Fix an arbitrary metric and its polarization `H`.
Orient the exceptional generators so that

\[
                         c_H^+\cdot E_j\le0.               \tag{5}
\]

The chamber-sensitive input is exactly the construction in
[LeBrun, Proposition 3.2, proof on pp. 17--18](https://arxiv.org/pdf/math/0003068).
It supplies a spin-c structure with

\[
 a_H=c-\sum_{j=1}^kE_j,
\]

whose small-perturbation Seiberg--Witten invariant at polarization `H`
is nonzero. When `\ell>0`, the invariant includes the `\ell` holonomy
insertions from the `S^1\times S^3` summands. Nonvanishing implies
unperturbed solvability for every `H`-adapted metric. The polarized
definition and this implication appear on pp. 6--7 of the same paper.

This classical input includes `b_+(X)=1`: on the minimal surface,
`c^2=A>0` prevents the projection of `c` from vanishing and removes the
polarization wall for its small-perturbation invariant. On the blown-up
manifold the selected class and exceptional signs are allowed to depend
on `H`. In particular, when `A-k<0`, one must not replace this statement
by the unsupported assertion that all signed blow-up classes are
all-metric monopoles simultaneously.

The two required numerical bounds are explicit. Since the anti-self-dual
intersection form is negative definite,

\[
\begin{aligned}
 (a_H^+)^2
 &= (c_H^+)^2-2\sum_jc_H^+\cdot E_j
                         +\left(\sum_jE_{j,H}^+\right)^2\\
 &\ge(c_H^+)^2\ge c^2=A.                                  \tag{6}
\end{aligned}
\]

Also,

\[
 a_H^2=A-k,
 \qquad T=A-k-4\ell,
 \qquad a_H^2=T+4\ell\ge T.                               \tag{7}
\]

The structure selected at `H` stays fixed for all the weights in (2).
Thus (3) holds for every metric. Substituting (7) into (4) proves (1).

The proof of the classical gluing input is not being claimed as new.
The new deduction is that its polarized form already satisfies the
stronger integral theorem's full auxiliary-equation requirement.

## 4. Consequences and the precise increase in coverage

Write `D=k+4\ell` and `d=(1/3-D/A)_+`. In four dimensions,

\[
 4\delta_\sigma(g)^2+d\ge c_*\qquad(\sigma=\pm1),          \tag{8}
\]

because tensor Hilbert--Schmidt norm squared is at most four times
endomorphism operator norm squared. Hence `d\le c_*/2` gives

\[
                 \delta_\sigma(g)\ge\sqrt{c_*/8}.          \tag{9}
\]

The scalar monopole bound also excludes Ricci-flat metrics. For any
non-Ricci-flat Einstein metric `\mathcal E=0`; consequently

\[
 D\ge(1/3-c_*/2)A
 \quad\Longrightarrow\quad
 M\text{ has no Einstein metric of any sign}.              \tag{10}
\]

More importantly for the original problem, the same topologies cannot
support either sign of arbitrarily tight Ricci pinching, even in the
weaker normalized integral sense (1). They therefore cannot be used as
near-Einstein counterexample topologies inside this band.

The extension includes blow-ups of `p_g=0` minimal surfaces of general
type, and their indicated handle additions. A useful *critical*, rather
than strictly supercritical, example is supplied by
[Park--Park--Shin, Theorem 1.1](https://arxiv.org/abs/0708.0273): a
simply connected minimal complex surface `X` with `p_g=0` and `A=3`.
Its one-point blow-up has

\[
 b_+=1,\qquad k/A=1/3,\qquad
                      \mathcal E(g)\ge c_*               \tag{11}
\]

for every smooth metric. The integral gap at this exact critical ratio
is not supplied by merely substituting into the classical estimate
whose right-hand side is proportional to `k/A-1/3`. Nor can this
particular example be reduced to the old high-`b_+` theorem by passing
to a connected finite cover: its fundamental group is trivial.

The blow-up of a minimal numerical Campedelli surface also has `d=0`
(`A=2,k=1`), but lies strictly beyond the critical ratio. Neither
application asserts nonexistence on the unblown minimal surface: for
`k=\ell=0`, the topological term is `1/3`.

There is no new positive-Ricci class construction here. Rational or
ruled manifolds with `b_+=1` are not included merely because they have
one positive direction. Their gauge-theoretic hypothesis is different.
Nor is any claim made that an unspecified negative-definite summand
has the polarized gluing property used above.

## 5. Relation to the existing manuscripts

The existing main statement in
`skill/research/20260921_rigidity.tex`, Corollary `cor:blowups`, assumes
`b_+(X)>1`. Its analytic core already explicitly states that
conformal-class weighted solvability suffices. The present note joins
that fact to the chamber-sensitive classical input and removes the
restriction in this concrete application.

The earlier long manuscript `skill/research/20260912.tex` already records
the classical polarized estimate for `X#k CPbar^2#ell(S^1 x S^3)`.
Accordingly, neither the topology formula nor the underlying polarized
Seiberg--Witten theorem is a new result of this round. What changes is
the availability of the uniform **integral** gap for the complete
general-type family, including `b_+=1` and all the standard handle
additions.

This is a genuine enlargement of the theorem's domain. It does not
produce a new analytic self-testing mechanism, prove a universal
four-dimensional rigidity theorem, or settle the unrestricted Yau26
problem. Its mathematical point is that conformal solvability is the
correct hypothesis: demanding a chamber-independent all-metric class
would unnecessarily discard an applicable part of the classical theory.
