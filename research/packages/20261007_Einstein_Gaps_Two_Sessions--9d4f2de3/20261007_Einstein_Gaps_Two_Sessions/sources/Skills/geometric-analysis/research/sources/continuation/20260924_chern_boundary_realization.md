# Pointwise Einstein approximation on the Miyaoka–Yau numerical boundary

24 September 2026. This continuation removes externally prescribed saturation
and topological bubble-exclusion hypotheses at a realizable numerical boundary.
The Chern–Weil identities are classical; the new project conclusion is their
composition with compactness and actual-form supply. Global priority is not asserted.

## 1. The realization statement

Put \(T_\pm=2\chi\pm3\tau\) and
\[
 \delta(g)=\|\operatorname{Ric}_g^\sharp+I\|_{\infty,\mathrm{op}}.
\]
Use tensor Hilbert–Schmidt norms for Ricci, exterior norms for two-forms,
and endomorphism Hilbert–Schmidt norms for \(W^\pm\).

**Theorem A.** For every \(D>0\) there exists \(\varepsilon(D)>0\) with
the following property. Let \(M\) be a closed connected oriented smooth
four-manifold with
\[
 A:=T_+=3T_->0.                                           \tag{1}
\]
Let \(g\) have diameter at most \(D\). Suppose a Spin\(^c\) structure is
actually monopole-solvable for every metric conformally related to \(g\),
and its first Chern class \(a\) satisfies
\[
                          p=(a_g^+)^2\ge A.               \tag{2}
\]
If \(\delta(g)<\varepsilon(D)\), the **same oriented smooth manifold**
admits a complex-hyperbolic metric \(h\) with \(\operatorname{Ric}_h=-h\).
Its universal Riemannian cover is the complex hyperbolic plane of holomorphic
sectional curvature \(-2/3\).

No input Kähler structure, \(\pi_1\) or \(\pi_2\) hypothesis, Weyl bound,
class-square cost, Ricci-derivative bound, or functional-saturation assumption
is imposed. The class may depend on \(g\), but is fixed throughout its
conformal class. The threshold is uniform over the stated manifolds and classes.

Condition (1) is exactly \(\chi=3\tau>0\), not a general condition on
four-manifolds. Complex-hyperbolic existence fully supplies the Einstein
output required by the adopted Yau26 question on these inputs. The remaining
limitations are the diameter and numerical/gauge **input** conditions.

## 2. Saturation follows from the numerical boundary

Write
\[
 S=\int s^2,\quad P=\int|\operatorname{Ric}^{\circ}|^2,\quad
 W_\pm=\int|W^\pm|^2,\quad V=\operatorname{Vol}(g),
\]
\[
 \mathfrak D_2=\frac32(S+12W_+)-72\pi^2p,\qquad q=\mathfrak D_2/V.
\]
The actual-monopole inequalities give
\[
 S\ge32\pi^2p\ge32\pi^2A,\qquad \mathfrak D_2\ge0.          \tag{3}
\]
The opposite-orientation Chern–Weil formula is exactly
\[
                    S-32\pi^2A+48W_-=12P.                \tag{4}
\]
Consequently
\[
 0\le W_-\le P/4,\qquad 0\le S-32\pi^2A\le12P.
\]
Eliminating \(W_+\) with the other Chern–Weil formula first gives
\[
 \mathfrak D_2=\frac98S+\frac92P+36\pi^2A-72\pi^2p.
\]
Substitution of (4) gives a second exact balance:
\[
 \boxed{\mathfrak D_2+72\pi^2(p-A)+54W_-=18P.}             \tag{5}
\]
All terms on its left are nonnegative. Orthogonal trace decomposition and
\(|\operatorname{Ric}+g|^2\le4\delta^2\) now imply
\[
 \boxed{q\le72\delta^2,\qquad W_-/V\le\delta^2.}           \tag{6}
\]
Thus the previously independent gauge deficit and opposite Weyl energy
are forced small by the **original pointwise input**. This implication is
specific to (1)–(2), not a general property of almost-Einstein metrics.

Volume is also controlled:
\[
 V\ge\frac{2\pi^2A}{(1+\delta)^2},\qquad
 |V-2\pi^2A|\le(2\delta+4\delta^2)V.                       \tag{7}
\]
The second bound follows from
\(|S/V-16|\le32\delta+16\delta^2\) and
\(0\le S-32\pi^2A\le48\delta^2V\). No volume normalization is assumed.

## 3. Both Weyl halves exclude concentration without topology

Suppose Theorem A were false for a fixed \(D\). Choose counterexamples
\((M_j,g_j,a_j)\) with \(\delta_j\to0\) and no complex-hyperbolic metric
on their oriented smooth types. For large \(j\), \(\delta_j\le1/2\).
The positive integer \(A_j=T_+(M_j)\) is at least one, so (7) gives
\(V_j\ge8\pi^2/9\). Ricci is bounded on both sides. Bishop comparison
and the diameter bound give \(V_j\le V_0(D)\) and
\[
 c(D)r^4\le \operatorname{Vol}_{g_j}B_r(x)\le Cr^4
 \quad(0<r\le1).                                        \tag{8}
\]

Set \(r_j=\fint|\operatorname{Ric}+g_j|^2\) and
\(\kappa_j=r_j+q_j\le76\delta_j^2\).
The elementary amplitude consequence of the classical completed-square
estimate, recorded in Section 4 of the
[gauge-realization proof](20260923_gauge_saturation_ke.md), gives
\[
 \int_E|W^+|^2\le\frac43\operatorname{Vol}(E)
                          +\frac23\kappa_jV_j            \tag{9}
\]
for every measurable set \(E\). Meanwhile (6) gives
\[
                  \int_{M_j}|W^-|^2\to0.                \tag{10}
\]
Both halves therefore vanish on every shrinking ball in a harmonic-radius
blowup. There is no half-flat ALE core left to exclude by topology.

For clarity, the compactness argument is the following. If the minimum
\(C^{1,\alpha}\) harmonic radius \(\rho_j\to0\), rescale by \(\rho_j^{-2}\).
All harmonic radii are at least one, the base radius is one, and Ricci
tends uniformly to zero. Harmonic-coordinate compactness, (8), and the
metric equation give a complete smooth Ricci-flat limit with Euclidean
lower volume growth. Subtracting the limiting metric equation improves
convergence to strong local \(W^{2,p}\), all finite \(p\), recovering the
Hölder exponent used to normalize the harmonic radius. This uses no
derivative of Ricci. Section 4 of
[compact realization](20260923_compact_realization.md) supplies this
analytic argument before its ALE step.

Scale invariance of Weyl energy, (8)–(10), and strong curvature convergence
give \(W^+=W^-=0\) on the limit. Thus it is flat. A complete smooth flat
manifold with Euclidean lower volume growth at all scales is Euclidean:
an infinite deck group lowers the growth order, and a finite Euclidean
isometry group cannot act freely unless trivial. Harmonic charts on a
larger Euclidean ball transfer back and contradict the normalized base
harmonic radius. Hence harmonic radii are uniformly positive.

This particular proof needs neither a Jiang–Naber total-energy bound, nor
ALE asymptotics or classification, nor any homotopy restriction.
Global diameter and (8) give a finite atlas. After diffeomorphisms and a
subsequence the metrics converge on a common smooth oriented manifold
in \(C^{1,\alpha}\) and strongly in finite \(W^{2,p}\) to a smooth metric
\(h\) with \(\operatorname{Ric}_h=-h\) and \(W_h^-=0\).
No convergence of every derivative of the approximate metrics is asserted.

## 4. Global complex structure and the exact output

The retained
[actual-form theorem](../mathematics/current/line1_composed_application.md)
supplies global self-dual forms \(\omega_j\), of uniformly bounded amplitude,
with
\[
 \fint(|\omega_j|^2-2)^2\to0,\qquad
 \fint|\nabla\omega_j|^2\to0.                             \tag{11}
\]
These first-order estimates require no negative-square budget.
Transfer the forms to the common smooth manifold. The volume bounds and
\(C^1\) metric convergence give a fixed-metric \(H^1\) bound. Rellich
compactness gives strong \(L^2\) convergence to \(\omega\), and (11) gives
\(\nabla_h\omega=0\), \(|\omega|^2=2\). Thus \(\omega\) is smooth and
defines a global parallel orthogonal complex structure \(J\).
It is integrable and has the prescribed orientation; no double cover occurs.

A Kähler–Einstein surface with \(W^-=0\) has vanishing Bochner curvature,
hence constant holomorphic sectional curvature. With \(\operatorname{Ric}=-h\),
that curvature is \(-2/3\). Completeness identifies the universal cover
with the complex hyperbolic plane. Pull this exact metric back to each
sufficiently late \(M_j\), contradicting the counterexample choice.
This proves the uniform \(\varepsilon(D)\).

## 5. Suppliers, examples, and the actual increment

An actual conformally solvable class with \(a^2\ge T_+>0\) automatically
satisfies (2), because \(p=a^2+\|a_g^-\|^2\). A nonzero ordinary SW
invariant in nonnegative formal dimension, with applicable chamber
conditions, is a classical supplier. A formal cohomology vector is not.
For \(b_+=1\), retain the metricwise polarized/chamber argument.

Compact complex-hyperbolic surfaces and their canonical classes are real
equality models:
\[
 S=32\pi^2A,\quad P=W_-=\mathfrak D_2=0,\quad p=A,\quad V=2\pi^2A.
\]
The theorem does not assume the input smooth type already supports such a
structure. Conversely, on a smooth type satisfying the stated gauge supply
and (1), but not supporting complex-hyperbolic geometry, it gives a
diameter-dependent **pointwise defect gap**, not merely a joint deficit gap.

The zero-defect classification is classical Seiberg–Witten/Miyaoka–Yau
rigidity; (4)–(5) are classical identities. The project increment is the
uniform approximate-to-exact conclusion, with saturation and earlier
topological bubble-exclusion assumptions removed. The older unrestricted
integral obstacles remain distinct: they have no diameter hypothesis and
cover incompatible numerical regions. Here a compatible numerical boundary
produces an actual exact geometry.

No optimal threshold, new non-complex-hyperbolic example, or unrestricted
Yau26 solution is claimed.

## 6. Primary inputs and proof dependencies

- LeBrun, *Ricci Curvature, Minimal Volumes, and Seiberg–Witten Theory*,
  [Theorem 2.3, Proposition 4.1 and formula (1)](https://arxiv.org/html/math/0003068):
  actual conformal monopole inequalities and Chern–Weil normalization.
- LeBrun, *Einstein Metrics and Mostow Rigidity*, Math. Res. Lett. 2
  (1995), 1–8, [DOI](https://doi.org/10.4310/MRL.1995.v2.n1.a1):
  the classical exact rigidity comparison, not a new exact classification.
- Anderson, [harmonic-coordinate compactness](https://doi.org/10.1007/BF01233434),
  as used with the detailed metric-equation argument in the retained proof.

The actual-form construction remains a project PDE dependency. The finite
checks below verify only the two exact balances and the equality calibration.
