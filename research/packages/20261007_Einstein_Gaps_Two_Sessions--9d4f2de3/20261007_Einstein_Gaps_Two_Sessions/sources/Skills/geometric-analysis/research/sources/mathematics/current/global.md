# Global numerical closure: what the available inequalities do and do not force

Date: 2026-09-19. This is a local mathematical development record. The conclusions below concern explicit consequences and limitations of the supplied manuscripts; no new metric or Einstein nonexistence theorem is claimed.

Source directory: `/data/qiushi/qiushi_engine_v09/users/user2/Skills/qiushi-yau26/research/`.

## 1. The two-orientation numerical problem on the Dehn-twist bundle

Let a hypothetical Einstein metric on a connected finite cover of `E_D` be normalized by `Ric = -g`. Write

\[
 V_*=4\pi^2\chi,\qquad A=2\chi=\frac{V_*}{2\pi^2},\qquad
 V=xV_*.
\]

The existing manuscript proves the necessary window `1 < x < 3`, zero signature, and

\[
 s=-4,\qquad
 \int |W^+|^2=\int |W^-|^2=V_*(1-x/3),\qquad
 \int|\operatorname{Rm}|^2=8V_*.
\tag{1}
\]

Here Weyl norms are Hilbert--Schmidt norms as operators on self-dual/anti-self-dual two-forms; the full Riemann tensor has the four-index norm. See `20260916_global.tex:831–885`.

For either orientation let `u=|W^±|` and `w=lambda_min(W^±)`. The actual monopole-class bounds include

\[
 \int s^2\ge16V_*,\qquad
 \int(\tfrac23s+2w)^2\ge16V_*,\qquad
 \int(s-\sqrt6u)^2\ge36V_*.
\tag{2}
\]

The negative-part convention in the spectral inequality can be omitted here because `s=-4` and `w<=0`. The mixed inequality and common-polarization numerical feasibility are already discussed in `20260912.tex:4411–4497`; they are not new results of this note.

### Proposition 1: the scalar--Weyl upper bounds leave the whole interval open

For every `1<x<3`, both orientations' scalar, least-eigenvalue, mixed scalar--Weyl, Chern--Gauss--Bonnet and signature constraints admit simultaneous algebraic curvature data. Even requiring distinct Weyl eigenvalues almost everywhere and a positive-sectional-curvature plane does not empty this numerical feasible set.

This is a statement about algebraic distributions, not metrics or solutions of the differential Einstein equation.

**Proof of the scalar--Weyl feasibility.** By Cauchy--Schwarz, in the correct direction,

\[
 \int(s-\sqrt6u)^2
 \le V_* B(x),\qquad
 B(x)=\bigl(4\sqrt x+\sqrt{6-2x}\bigr)^2.
\tag{3}
\]

This is an upper bound on an expression that monopole theory bounds below. It is therefore a necessary compatibility test, not a new lower bound. Equality in (3) holds for constant `u`. The function

\[
 F(x)=4\sqrt x+\sqrt{6-2x}
\]

is strictly concave on `(0,3)`, with `F(1)=6` and `F(3)=4sqrt(3)>6`. Its graph lies above the endpoint chord, so `B(x)>36` throughout `1<x<3`.

Also `w>=-sqrt(2/3)u`. Choosing constant Weyl spectra

\[
 (-2a,a,a),\qquad a^2=\frac{3-x}{18x}
\]

realizes the energies (1), and gives

\[
 \int(\tfrac23s+2w)^2=\frac49V_*B(x)>16V_*.
\tag{4}
\]

The scalar bound is strict because `16xV_*>16V_*`. Both Weyl halves can use these data independently with equal energies, retaining zero signature.

The repeated eigenvalues in this preliminary maximizing distribution are not being proposed as exact Einstein geometry. For any fixed interior `x`, all inequalities have strict slack. Perturbing both spectra to distinct eigenvalues while preserving their norms therefore preserves the inequalities. A small positive-measure state with spectra `(-H,0,H)` in both halves, with `H>1/3`, yields an algebraic positive-sectional-curvature plane. Choosing its measure sufficiently small and adjusting the remaining state's norm preserves the energy constraints and strict inequalities. The two Weyl halves are the independent trace-free blocks of an algebraic curvature operator with scalar `-4` and zero traceless Ricci. Thus this modification remains algebraically legitimate. No curvature differential identities or global bundle realization are implied.

### An explicit interior witness with all eigenvalues distinct

At `x=2`, use a probability distribution with weights `1/12` and `11/12`. In both orientations choose spectra

\[
 (-a,0,a),\qquad (-t,0,t),\qquad
 t=\frac1{100},\quad a=\sqrt{1-11t^2}.
\tag{5}
\]

They are distinct in both states, and

\[
 \mathbb E|W^\pm|^2=\frac16,
 \qquad \int|W^\pm|^2=\frac13V_*.
\]

Each spectral monopole integral is exactly

\[
 \frac1{V_*}\int(\tfrac23s+2w)^2
 =\frac{134+16(a+11t)}9>\frac{50}3>16.
\tag{6}
\]

Each mixed integral is

\[
 \frac1{V_*}\int(s-\sqrt6|W^\pm|)^2
 =34+\frac{8\sqrt3}{3}(a+11t)>36.
\tag{7}
\]

At the high-amplitude state, the largest sectional curvature of the associated algebraic Einstein curvature tensor is `-1/3+a>0`. Indeed the self-dual and anti-self-dual components of a unit simple bivector have equal norm `1/sqrt(2)` and can be aligned with both maximal eigenvectors. All data in (1) hold, while `integral s^2=32V_*` and `integral |Ric|^2=8V_*` strictly exceed their monopole lower bounds.

For the limiting rational witness `t=0,a=1`, the calibration density used in the uniform-gap manuscript has integral `132V_*`, below its allowed `144V_*`. To check this directly, use

\[
 \int F=216\int(s^2/24+2|W^\pm|^2)
       -18\int(\tfrac23s+2w)^2
       =432V_*-300V_*=132V_*.
\]

The generic perturbation (5) decreases this calibration integral further. Thus the simultaneous inequalities do not accidentally force the calibration density toward the forbidden zero-density configuration.

### The uniform exact-Einstein gap does not close this interval

The general theorem in `20260916_uniform_gap.tex:269–322` reads

\[
 \frac{2\chi+3\tau}{A}\ge\frac23+\eta(L),\qquad \chi/A\le L.
\]

For the present canonical lower bound, `A=2chi`, `tau=0`, `L=1/2`; it says only

\[
 1\ge\frac23+\eta(1/2).
\tag{8}
\]

Products of two closed hyperbolic surfaces, normalized by `Ric=-g`, satisfy the same monopole hypothesis, `A=2chi`, and `tau=0`. They are actual exact Einstein examples. Consequently every universal choice in this theorem necessarily satisfies `eta(1/2)<=1/3`. Applying the theorem in both orientations gives the same inequality twice, and does not exclude `E_D` or constrain `x` further.

Moreover, the manuscripts already show simultaneous saturation of both orientations' common-polarization numerical lower bounds along the approximate sequence (`20260912.tex:4411–4449`). Larger lower bounds cannot be obtained just by taking nonnegative combinations of that same data. A new restriction specific to polarizations realized by *exact Einstein metrics*, a differential Weyl identity, or monodromy-sensitive information would be additional mathematical input.

## 2. A topology-independent conditional obstruction for a connector

Use the hyperbolic normalization `Ric≈-3g`. Let `N` replace cusp tails in a closed matched graph-manifold metric, retain the exact hyperbolic exterior, and assume the Euler budget agrees with the block sum. Let

\[
 \epsilon=\|g^{-1}\operatorname{Ric}+3I\|_\infty,\quad
 r=\frac{V_{\rm rem}}{V_N},\quad
 w=\fint_N|W|^2.
\]

The relative identity in `20260916_global.tex:247–290` yields

\[
 |2w+12(1-r)|\le8\epsilon+4\epsilon^2.
\tag{9}
\]

It applies to a smoothly matched closed metric. A bare trial domain requires its boundary transgression terms. If the exterior changes, the additional curvature and reference-volume terms in the source must be retained.

### Proposition 2: a normalized connector budget gives a uniform defect gap

If `w>=w0` and `r<=1+w0/6-kappa` for some `kappa>0`, then

\[
 \epsilon\ge\sqrt{1+3\kappa}-1,
 \qquad
 \delta_-\ge\frac13(\sqrt{1+3\kappa}-1).
\tag{10}
\]

The second bound uses `h=3g`, hence `delta_-(h)=epsilon/3`. In particular, if `V_N>=(1+c)V_rem` with `c>0`, then

\[
 \epsilon\ge\sqrt{1+\frac{3c}{1+c}}-1.
\tag{11}
\]

**Proof.** The assumptions give `2w+12(1-r)>=12kappa`. Combining with (9), dividing by four and completing the square gives (10). For (11), use `w0=0` and `kappa=c/(1+c)`.

These bounds are independent of cover degree, Euler characteristic, and absolute connector volume. A common covering/quotient volume factor cancels. They identify exactly the extra geometric inequality that would turn a connector volume/Weyl cost into a uniform pointwise obstruction.

The exact Ricci-box optimization in `curvature_box.md` further strengthens
(10) to a two-branch bound. The same geometric hypotheses remain necessary;
the following concentration example survives both estimates.

Conversely, a sequence with vanishing defect only forces

\[
 r=1+w/6+o(1).
\tag{12}
\]

This can have `r>1`: removed cusp volume can pay the connector's Weyl energy. Nonzero `w` alone does not contradict the budgets.

## 3. A compatible graph-manifold numerical model, even as topology varies

### Proposition 3: the displayed CGB/volume/Weyl constraints alone have no uniform defect gap

Fix a reference hyperbolic volume `V_ref=4pi^2 chi/3`. Take the total volume equal to `V_ref`, retain the hyperbolic exterior, and prescribe the following algebraic data on a putative connector of volume `V_N=V_rem`:

\[
 \operatorname{spec}(g^{-1}\operatorname{Ric})
 =(-3-\epsilon,-3-\epsilon,-3+\epsilon,-3+\epsilon),\qquad
 \fint_N|W|^2=2\epsilon^2.
\tag{13}
\]

Use equal Weyl-half energies. Then `s=-12`, `|Ric°|^2=4epsilon^2`, and its Ricci contribution to CGB is `6-2epsilon^2`. Adding the Weyl contribution gives mean CGB density exactly `6`, matching the unchanged exterior and the reference Euler characteristic. Signature is zero. The relative identity is exact:

\[
 2\int_N|W|^2+12(V_N-V_{\rm rem})
 =4\epsilon^2V_N
 =\int_N|\operatorname{Ric}^{\circ}|^2.
\tag{14}
\]

Both minimal-Ricci-volume lower bounds and the near-Einstein CGB volume upper bounds admit `V=V_ref`. The normalized full Ricci defect is `epsilon/3`, which can tend to zero.

A nonvanishing Weyl amplitude, required by nonhyperbolic topology, is numerically compatible as well: on a fraction `epsilon^2/8` of the connector choose `W^+=W^-=diag(-2,0,2)`, and elsewhere choose zero. Each half then has mean-square norm `epsilon^2`, as needed. There is an algebraic positive-sectional-curvature plane in the high-amplitude state. The amplitude remains fixed while its relative-volume support tends to zero. Small generic perturbations may be made if needed; no generic-Weyl requirement is used for graph topology here.

For a varying-cover illustration, choose admissible topologies with `chi_j=d_j chi_0` and set `epsilon_j=d_j^(-1/2)`. The displayed numerical constraints remain compatible. Even for fixed topology they remain compatible: the high-Weyl region merely has vanishing volume. This is not a construction of metrics, peripheral covers, a connector, or compatible derivatives. It proves that these *numerical constraints*, without a lower bound on the cost of concentrating the nonhyperbolic topology, cannot themselves force a positive uniform defect.

This separates the remaining tasks: an actual connector family must solve the full Ricci system and the common-end lattice/holonomy matching; an obstruction must provide a geometric lower cost such as Proposition 2's hypothesis. Increasing exterior volume or cover degree does neither by itself.

## 4. Checked scope and research consequence

The E_D scalar--Weyl function (3) was already present in the cumulative manuscript. The additions here are its explicit least-eigenvalue realization in both orientations, a generic-spectrum positive-sectional-curvature witness, calibration against the exact-gap theorem, and the dimensionless connector tradeoff (10)–(11) with a compatible numerical concentration model.

`global_check.py` checks the exact symbolic energies, spectral and mixed integrals, CGB identities, calibration identity, and gap inversion. Its finite numerical samples check the displayed formulas; they do not validate a metric, solve a PDE, or certify any existence claim.

The computations do not narrow `1<x<3` for E_D. They establish a precise negative conclusion about this attempted closure: adding the available two-orientation numerical inequalities and the stated uniform topological gap supplies no contradiction. The missing information must couple exact geometry to monodromy/polarization or quantitatively constrain concentration in a connector.
