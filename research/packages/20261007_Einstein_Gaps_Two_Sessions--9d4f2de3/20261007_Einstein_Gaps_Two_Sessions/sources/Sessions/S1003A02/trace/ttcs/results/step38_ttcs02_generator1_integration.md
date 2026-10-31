# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 38,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step38_ttcs02_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step38_ttcs02_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop the paired-monopole route into an exact covariant PDE/energy identity, or show structurally why it cannot yield a per-exceptional-class excess. Let two actual Seiberg-Witten solutions correspond to determinant classes differing by 2E_i, with relative twisting line N of c1=E_i, u=<Phi',Phi> in N* and w=Phi wedge Phi'. Starting from the Dirac and curvature equations in the stated normalization, derive as far as possible: covariant derivative/Bochner equations for u and w; how the relative connection curvature (f-f')/2 enters; whether a Bogomolny/vortex completion relates its 4pi^2 negative-square charge to amplitude depletion, |w|^2, or relative spin-direction energy; and what hypotheses would make a positive tariff possible. Test the formula against the two essential regimes: Kähler amplitude vortex along E, and perpendicular null-period geometry where orthogonality/rotation can carry the zero. A useful result should be an exact identity, a precise conditional inequality, or a precise obstruction/countermechanism—not a generic research list.

## Integrated Scientific Memo

## Paired monopoles: exact covariant identities and the obstruction to an exceptional-class excess

Let
\[
D_A\Phi=0,\qquad F_A^+=2i\sigma(\Phi),\qquad
D_{A'}\Phi'=0,\qquad F_{A'}^+=2i\sigma(\Phi'),
\]
with determinant classes
\[
a'=a+2E,\qquad E^2=-1.
\]
Choose \(N\) with \(c_1(N)=E\), so \(S_{a'}^\pm\simeq S_a^\pm\otimes N\), and write \(A'=A+2B\), where \(B\) is the induced connection on \(N\). Put
\[
f=-iF_A,\qquad f'=-iF_{A'},\qquad
h:=\frac{f-f'}2,\qquad \bar f:=\frac{f+f'}2.
\]
Then \(h\) is the real curvature of \(N^*\), so
\[
[h/(2\pi)]=-E,
\]
whereas \(\bar f\) is the curvature of
\[
D:=\det S_a^+\otimes N,\qquad c_1(D)=\frac{a+a'}2.
\]

Define
\[
u=\langle\Phi',\Phi\rangle\in\Gamma(N^*),\qquad
w=\Phi\wedge\Phi'\in\Gamma(D),
\]
and \(\rho=|\Phi|^2,\ \rho'=|\Phi'|^2\).

### 1. Exact relative-curvature completion

Write
\[
f^+=\frac{\rho}{\sqrt2}n,\qquad
f'^+=\frac{\rho'}{\sqrt2}n',\qquad |n|=|n'|=1.
\]
The pointwise Fierz identities are
\[
|u|^2=\rho\rho'\frac{1+n\cdot n'}2,\qquad
|w|^2=\rho\rho'\frac{1-n\cdot n'}2,
\]
hence
\[
|u|^2+|w|^2=\rho\rho'.
\]
Since \(h^+=(f^+-f'^+)/2\),
\[
\boxed{
|h^+|^2
=\frac{(\rho-\rho')^2}{8}+\frac{|w|^2}{2}
=\frac{(\rho+\rho')^2-4|u|^2}{8}.
}
\tag{1}
\]

Chern–Weil gives, with the usual four-dimensional convention
\[
\int_M h\wedge h
=\|h^+\|_2^2-\|h^-\|_2^2
=4\pi^2E^2=-4\pi^2.
\]
Thus
\[
\boxed{\|h^-\|_2^2-\|h^+\|_2^2=4\pi^2}
\tag{2}
\]
and consequently
\[
\boxed{
\|h\|_2^2
=4\pi^2+2\|h^+\|_2^2
=4\pi^2+\int_M
\left[\frac{(\rho-\rho')^2}{4}+|w|^2\right]d\mu .
}
\tag{3}
\]

This is the exact relative \(U(1)\) Bogomolny/Yang–Mills completion. It gives a sharp structural answer:

* the fixed \(4\pi^2\) charge lies in the **anti-self-dual excess**;
* amplitude mismatch and relative spin-direction disagreement measure only \(h^+\);
* the Seiberg–Witten curvature equations prescribe \(h^+\), but do not pointwise prescribe \(h^-\).

Thus the topological charge is not converted by the local SW equations into a positive amount of amplitude depletion, \(|w|^2\), or spin-rotation energy. In the sign-averaged curvature identity, \(2\|h^-\|^2\) is precisely the already-known \(8\pi^2\) exceptional contribution, not an additional surplus.

At a zero of \(u\) with \(\rho\rho'>0\),
\[
n'=-n,\qquad |w|^2=\rho\rho',
\]
so topology can force \(u=0\) without forcing either spinor amplitude to vanish.

---

### 2. Exact bilinear Bochner system

The spinor Weitzenböck equations in this normalization are
\[
\nabla_A^*\nabla_A\Phi+
\left(\frac{s}{4}+\frac{\rho}{2}\right)\Phi=0,
\qquad
\nabla_{A'}^*\nabla_{A'}\Phi'+
\left(\frac{s}{4}+\frac{\rho'}2\right)\Phi'=0.
\tag{4}
\]
The induced first derivatives are
\[
\nabla^{N^*}u
=\langle\nabla_{A'}\Phi',\Phi\rangle
+\langle\Phi',\nabla_A\Phi\rangle,
\tag{5}
\]
\[
\nabla^D w
=(\nabla_A\Phi)\wedge\Phi'
+\Phi\wedge\nabla_{A'}\Phi'.
\tag{6}
\]
Applying the product rough Laplacian gives
\[
\boxed{
\left(\nabla_{N^*}^*\nabla_{N^*}
+\frac{s}{2}+\frac{\rho+\rho'}2\right)u
=-2\sum_\alpha
\left\langle\nabla_{A',e_\alpha}\Phi',
             \nabla_{A,e_\alpha}\Phi\right\rangle ,
}
\tag{7}
\]
and
\[
\boxed{
\left(\nabla_D^*\nabla_D
+\frac{s}{2}+\frac{\rho+\rho'}2\right)w
=-2\sum_\alpha
(\nabla_{A,e_\alpha}\Phi)
 \wedge(\nabla_{A',e_\alpha}\Phi').
}
\tag{8}
\]
The curvature enters through derivative commutators:
\[
[\nabla^{N^*}_X,\nabla^{N^*}_Y]u=i\,h(X,Y)u,
\qquad
[\nabla^D_X,\nabla^D_Y]w=i\,\bar f(X,Y)w,
\tag{9}
\]
up to the fixed sign convention for unitary curvature.

For \(s=-4\), (7) becomes
\[
\left(\nabla^*\nabla-\frac{4-\rho-\rho'}2\right)u
=-2\sum_\alpha
\langle\nabla_\alpha\Phi',\nabla_\alpha\Phi\rangle,
\tag{10}
\]
with the analogous equation for \(w\). Pairing with \(u\) and integrating yields
\[
\|\nabla u\|_2^2
-\frac12\int_M(4-\rho-\rho')|u|^2
=-2\operatorname{Re}\int_M
\left\langle
\sum_\alpha\langle\nabla_\alpha\Phi',
\nabla_\alpha\Phi\rangle,u
\right\rangle .
\tag{11}
\]
The cross term has no fixed sign. The Dirac equations kill only the Clifford traces of \(\nabla\Phi,\nabla\Phi'\); their twistor components remain and are exactly what appears on the right of (7)–(8). Hence, on a general Riemannian four-manifold, neither \(u\) nor \(w\) satisfies a closed scalar vortex equation.

In particular, commuting derivatives introduces \(h\,u\), which degenerates exactly on the topologically forced zero set of \(u\). Meanwhile \(w\), which is maximal at an orthogonality zero, couples to \(\bar f\), not to the relative curvature \(h\). This prevents a direct vortex completion from pairing the exceptional charge with the nonvanishing component.

A useful differential estimate is
\[
\boxed{
|\nabla u|^2+|\nabla w|^2
\le
2\left(\rho'|\nabla_A\Phi|^2
+\rho|\nabla_{A'}\Phi'|^2\right).
}
\tag{12}
\]
At \(s=-4\), \(0\le \rho,\rho'\le2\), so
\[
\|\nabla u\|_2^2+\|\nabla w\|_2^2\le4(K+K'),
\qquad
K=\|\nabla_A\Phi\|_2^2.
\tag{13}
\]
The projective spin-direction decomposition is
\[
|\nabla_A\Phi|^2
=\frac{|\zeta|^2}{\rho}+\frac{\rho}{4}|\nabla n|^2,
\qquad
\zeta=\langle\Phi,\nabla_A\Phi\rangle,
\tag{14}
\]
and similarly for \(\Phi'\). Thus relative rotation is genuinely contained in spinor kinetic energy—but that kinetic energy occurs with the adverse sign in the simultaneous-field curvature identity.

---

### 3. Topological reason the \(u\)-vortex can unwind

The combined bilinear
\[
q=(u,w)\in\Gamma(\mathcal Q),\qquad
\mathcal Q=N^*\oplus D
\]
satisfies
\[
|q|^2=\rho\rho'.
\tag{15}
\]
For a one-sign flip
\[
a=c-E,\qquad a'=c+E,\qquad c\cdot E=0,
\]
we have
\[
c_1(N^*)=-E,\qquad c_1(D)=c,
\]
and therefore
\[
\boxed{c_2(\mathcal Q)=(-E)\cdot c=0.}
\tag{16}
\]
Accordingly, although \(u\) has line-bundle class \(-E\) and a transverse \(u\) has a zero divisor dual to \(-E\), the rank-two field \(q=(u,w)\) has no forced four-dimensional zero number. If both spinors are nonzero, \(q\) never vanishes.

Locally,
\[
\frac{(u,w)}{\sqrt{\rho\rho'}}\in S^3.
\]
If \(w=0\), the phase of \(u\) lies in an \(S^1\) and supports the usual vortex winding. Once \(w\) is allowed, that loop sits in \(S^3\), where
\[
\pi_1(S^3)=0.
\]
It can therefore be filled by rotating from the \(u\)-component into the \(w\)-component. This is the precise topological mechanism by which a line-bundle zero is carried by spinor orthogonality rather than amplitude collapse.

A current identity such as
\[
h=2\pi[Z_u]+d j_u
\tag{17}
\]
records the divisor class but gives no metric-uniform \(L^2\) lower bound beyond (2). The current can be represented by a thin orthogonality transition with no fixed four-volume.

---

### 4. Exact one-pair position inside the simultaneous cost identity

For one exceptional sign pair, let
\[
\mathcal R(\Phi)
=
8\|\zeta\|_2^2
+4\|W^+-W_0\|_2^2
+\int_M b(\rho)(2-\rho)^2,
\qquad
b(t)=\frac{-t^2+8t+2}{6}.
\]
The supplied simultaneous identity specializes to
\[
\boxed{
P-8\pi^2
=
2\|\bar f^-\|_2^2
+2\|h^+\|_2^2
+\frac{\mathcal R(\Phi)+\mathcal R(\Phi')}{2}
-2(K+K').
}
\tag{18}
\]
Thus a unit tariff \(P\ge8\pi^2\) would follow from
\[
\boxed{
2(K+K')
\le
2\|\bar f^-\|_2^2+2\|h^+\|_2^2
+\frac{\mathcal R(\Phi)+\mathcal R(\Phi')}{2}.
}
\tag{19}
\]
The paired Bochner equations do not imply (19). There are two separate obstructions.

1. **Common amplitude depletion.** If the spinors are aligned and
   \(\rho=\rho'=2-\varepsilon\), then \(h^+=w=0\). Yet
   \[
   K+K'=\frac12\int\big[\rho(2-\rho)+\rho'(2-\rho')\big]
   \]
   is linear in \(\varepsilon\), whereas the displayed amplitude residuals are quadratic.

2. **Relative rotation.** The class of \(u\) can unwind into \(w\) because \(c_2(N^*\oplus D)=0\). Its rotation cost lies in \(K+K'\), which is subtracted in (18).

Hence the pair is not a new positive sector beyond the Walsh decomposition: \(h\) is the singleton Walsh curvature, \(\bar f\) the coordinate-averaged curvature, and (2) extracts exactly the known \(8\pi^2\) contribution. What remains is still the signed kinetic compensation problem.

A quantitatively useful sufficient hypothesis would be the strengthened estimate
\[
2(K+K')
\le
2\|\bar f^-\|_2^2
+\frac{\mathcal R(\Phi)+\mathcal R(\Phi')}{2}
+(2-\theta)\|h^+\|_2^2
\tag{20}
\]
for some \(\theta>0\). Then
\[
\boxed{P\ge8\pi^2+\theta\|h^+\|_2^2.}
\tag{21}
\]
This separates the two required inputs: coercive control of the kinetic modes, and a lower bound on the relative self-dual curvature.

Because \(h\) represents \(-2\pi E\),
\[
\boxed{
\|h^+\|_2^2
=\int_M\left[
\frac{(\rho-\rho')^2}{8}+\frac{|w|^2}{2}
\right]d\mu
\ge4\pi^2(E_g^+)^2.
}
\tag{22}
\]
Thus a uniform period/projection hypothesis
\[
(E_g^+)^2\ge\delta>0
\tag{23}
\]
combined with (20) gives
\[
P\ge8\pi^2+4\pi^2\theta\delta.
\]
Equivalently, if a closed self-dual form \(\omega\) satisfies
\[
|E\cdot[\omega]|\ge d_0,\qquad \|\omega\|_2^2\le V_0,
\]
then
\[
\|h^+\|_2^2
\ge \frac{4\pi^2d_0^2}{V_0}.
\tag{24}
\]
Such hypotheses fail precisely in the perpendicular regime.

---

### 5. Kähler amplitude vortex versus perpendicular null-period rotation

#### Kähler regime

Kähler geometry supplies the extra first-order complex structure absent from (7). For a Hermitian line bundle with real curvature \(H\), section \(\varphi\), and \(\tau>0\), one has the vortex completion
\[
\begin{aligned}
&\int_M\left(
|H|^2+|\nabla\varphi|^2
+\frac14(\tau-|\varphi|^2)^2\right)d\mu\\
={}&-\int_MH\wedge H+\tau\int_MH\wedge\omega\\
&+\int_M\left[
2|H^{2,0}+H^{0,2}|^2
+2|\bar\partial_H\varphi|^2
+\left(\Lambda H-\frac{\tau-|\varphi|^2}{2}\right)^2
\right]d\mu ,
\end{aligned}
\tag{25}
\]
with signs reversed when the conjugate bundle convention is used. If \([H/(2\pi)]=\gamma\), \(\gamma^2=-1\), its topological part is
\[
4\pi^2+2\pi\tau\,\gamma\cdot[\omega].
\tag{26}
\]

For aligned Kähler monopoles, \(w=0\); the Dirac equation becomes a holomorphic equation, and the curvature equation supplies the scalar vortex equation. Then a zero of \(u\) is necessarily an amplitude zero. On a blow-up,
\[
E\cdot[\omega]=e>0,
\]
so there is a strict period contribution for every fixed Kähler metric. As \(e\to0\), that extra period tends to zero, consistently with
\[
P>8\pi^2k
\]
for every Kähler blow-up metric but
\[
\inf_{\mathrm{K\ddot ahler}}P=8\pi^2k
\]
when a small-exceptional-area recovery family exists.

The vortex completion alone is not a bound for \(P\), since it contains kinetic energy with a positive sign while (18) subtracts it. The full Kähler tariff comes from the additional scalar-curvature/Hodge-index identity.

#### Perpendicular null-period regime

If the relevant self-dual period vanishes,
\[
E\cdot[\omega]=0
\quad\text{or equivalently in the sharp projection form}\quad
E_g^+=0,
\]
then (22) supplies no positive lower bound. The zero of \(u\) may instead occur with
\[
\rho,\rho'>0,\qquad n'=-n,\qquad |w|^2=\rho\rho'.
\]
There is no Poincaré–Lelong or Wirtinger tariff because the transition is not confined to the aligned \(w=0\) subbundle.

A tubular scaling illustrates the absence of uniform excess. If spin direction rotates across a normal disk of radius \(r\) around an exceptional sphere of area \(A_E\), then typically
\[
|\nabla n|\sim r^{-1},\qquad
\operatorname{Vol}(\text{tube})\sim A_Er^2,
\]
so
\[
\int_{\text{tube}}|\nabla n|^2=O(A_E),
\qquad
\int_{\text{tube}}|w|^2=O(A_Er^2).
\tag{27}
\]
Both can vanish as \(A_E\to0\), while the fixed \(4\pi^2\) in (2) remains stored in \(h^-\). This is the exact field-theoretic mechanism compatible with the supplied perpendicular cell having subunit Ricci cost.

---

## Conclusion

The paired-monopole route yields three exact results:

1. the relative curvature identity (1)–(3);
2. the covariant bilinear Bochner system (7)–(9);
3. the one-pair curvature-cost identity (18).

Together they show structurally why topology alone does **not** produce a per-exceptional-class excess beyond the already extracted \(8\pi^2\): the fixed negative-square charge lies in the field-undetermined anti-self-dual relative curvature, while the forced zero of \(u\) can unwind through the \(w\)-component and relative spin rotation. The pair is the singleton Walsh sector, not an additional coercive sector.

A positive excess requires genuinely global geometric input: both a kinetic compensation such as (20) and a noncollapse condition such as \((E_g^+)^2\ge\delta\), or equivalent persistent-tube/amplitude/derivative bounds. Kähler alignment provides such structure through holomorphicity and positive exceptional period. Perpendicular null-period geometry removes it and leaves the rotation channel available.