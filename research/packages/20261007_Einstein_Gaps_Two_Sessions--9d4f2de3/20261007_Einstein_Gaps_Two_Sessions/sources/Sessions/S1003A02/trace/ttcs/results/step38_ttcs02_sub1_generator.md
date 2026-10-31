# TTCS Independent Branch Record

```json
{
  "step_id": 38,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md",
    "Sessions/S1003A02/workspace/scripts/paired_cross_field_algebra.py",
    "Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex",
    "Knowledge/objects/papers/Algebraic-surfaces-and-Seiberg-Witten-invariants--d573804ced34--70869ee25818/object.md"
  ]
}
```

## Task

Develop the paired-monopole route into an exact covariant PDE/energy identity, or show structurally why it cannot yield a per-exceptional-class excess. Let two actual Seiberg-Witten solutions correspond to determinant classes differing by 2E_i, with relative twisting line N of c1=E_i, u=<Phi',Phi> in N* and w=Phi wedge Phi'. Starting from the Dirac and curvature equations in the stated normalization, derive as far as possible: covariant derivative/Bochner equations for u and w; how the relative connection curvature (f-f')/2 enters; whether a Bogomolny/vortex completion relates its 4pi^2 negative-square charge to amplitude depletion, |w|^2, or relative spin-direction energy; and what hypotheses would make a positive tariff possible. Test the formula against the two essential regimes: Kähler amplitude vortex along E, and perpendicular null-period geometry where orthogonality/rotation can carry the zero. A useful result should be an exact identity, a precise conditional inequality, or a precise obstruction/countermechanism—not a generic research list.

## Output

Let
\[
D_A\Phi=0,\qquad F_A^+=2i\sigma(\Phi),\qquad
D_{A'}\Phi'=0,\qquad F_{A'}^+=2i\sigma(\Phi'),
\]
and put
\[
f=-iF_A,\qquad f'=-iF_{A'},\qquad
\rho=|\Phi|^2,\qquad \rho'=|\Phi'|^2.
\]
Assume
\[
a' =a+2E,\qquad E^2=-1,
\]
and choose \(N\) with \(c_1(N)=E\), so that \(S_{a'}^+=S_a^+\otimes N\). Write \(A'=A+2B\), where \(B\) is the induced connection on \(N\). Define
\[
h=\frac{f-f'}2,\qquad \bar f=\frac{f+f'}2 .
\]
Then \(h\) is the real curvature of \(N^*\), while \(\bar f\) is the real curvature on
\[
D:=\det S_a^+\otimes N,\qquad c_1(D)=\frac{a+a'}2.
\]

## 1. Exact relative-curvature identity

Set
\[
u=\langle\Phi',\Phi\rangle\in\Gamma(N^*),\qquad
w=\Phi\wedge\Phi'\in\Gamma(D).
\]
Writing
\[
f^+=\frac{\rho}{\sqrt2}n,\qquad
f'^+=\frac{\rho'}{\sqrt2}n',\qquad |n|=|n'|=1,
\]
the Fierz identities give
\[
|u|^2=\rho\rho'\frac{1+n\cdot n'}2,\qquad
|w|^2=\rho\rho'\frac{1-n\cdot n'}2,
\]
and hence
\[
|u|^2+|w|^2=\rho\rho'.
\]
Since \(h^+=(f^+-f'^+)/2\),
\[
\boxed{
|h^+|^2=\frac{(\rho-\rho')^2}{8}+\frac{|w|^2}{2}
       =\frac{(\rho+\rho')^2-4|u|^2}{8}.
}
\]
Chern–Weil gives
\[
\int_M h\wedge h=4\pi^2E^2=-4\pi^2,
\]
so
\[
\boxed{
\|h^-\|_2^2-\|h^+\|_2^2=4\pi^2
}
\]
and therefore
\[
\boxed{
\|h\|_2^2
=4\pi^2+2\|h^+\|_2^2
=4\pi^2+\int_M
 \left[\frac{(\rho-\rho')^2}{4}+|w|^2\right]d\mu .
}
\tag{1}
\]
This is the exact covariant Yang–Mills completion for the relative line. Its \(4\pi^2\) term is the unavoidable \(E^2=-1\) contribution. Every additional relative-curvature contribution is precisely amplitude mismatch plus spinor orthogonality.

At a point where \(u=0\) and both amplitudes are positive,
\[
n'=-n,\qquad |w|^2=\rho\rho'.
\]
Thus \(u\) can vanish without either spinor vanishing: the zero is carried entirely by relative spin direction.

## 2. Covariant equations for \(u\) and \(w\)

The spinor Weitzenböck formula in the normalization of the question is
\[
\nabla_A^*\nabla_A\Phi+
 \left(\frac{s}{4}+\frac{\rho}{2}\right)\Phi=0,
\qquad
\nabla_{A'}^*\nabla_{A'}\Phi'+
 \left(\frac{s}{4}+\frac{\rho'}2\right)\Phi'=0.
\tag{2}
\]
The induced covariant derivatives satisfy
\[
\nabla u
=\langle\nabla_{A'}\Phi',\Phi\rangle
 +\langle\Phi',\nabla_A\Phi\rangle,
\tag{3}
\]
\[
\nabla w
=(\nabla_A\Phi)\wedge\Phi'
 +\Phi\wedge(\nabla_{A'}\Phi').
\tag{4}
\]
Applying the product Laplacian to (3)–(4) and using (2) gives the exact equations
\[
\boxed{
\left(\nabla_{N^*}^*\nabla_{N^*}
+\frac{s}{2}+\frac{\rho+\rho'}2\right)u
=-2\sum_\alpha
 \left\langle\nabla_{A',e_\alpha}\Phi',
                  \nabla_{A,e_\alpha}\Phi\right\rangle ,
}
\tag{5}
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
\tag{6}
\]
The relative and middle curvatures enter through
\[
[\nabla^{N^*}_X,\nabla^{N^*}_Y]u=i\,h(X,Y)u,
\qquad
[\nabla^D_X,\nabla^D_Y]w=i\,\bar f(X,Y)w.
\tag{7}
\]
Thus the scalar Bochner equation for \(u\) contains no zeroth-order \(h\)-term. Curvature appears only after commuting two derivatives, and then as \(h\,u\). Precisely where topology forces \(u\) to vanish, this curvature coupling degenerates. Meanwhile \(w\), which is large at an orthogonality zero, sees \(\bar f\), not \(h\).

At \(s=-4\), equations (5)–(6) become
\[
\left(\nabla^*\nabla-\frac{4-\rho-\rho'}2\right)u
=-2\sum_\alpha
 \langle\nabla_\alpha\Phi',\nabla_\alpha\Phi\rangle,
\tag{8}
\]
with the analogous equation for \(w\). Integration yields
\[
\|\nabla u\|_2^2
-\frac12\int(4-\rho-\rho')|u|^2
=-2\operatorname{Re}\int
 \left\langle
 \sum_\alpha\langle\nabla_\alpha\Phi',
                        \nabla_\alpha\Phi\rangle,u
 \right\rangle .
\tag{9}
\]
The right side has no fixed sign. The Dirac equations remove only the Clifford trace of \(\nabla\Phi\) and \(\nabla\Phi'\); their twistor components remain independent and are exactly what enters (5)–(6). Consequently neither \(u\) nor \(w\) obeys a closed scalar vortex equation on a general Riemannian four-manifold.

A useful first-derivative estimate follows directly from the rank-two Lagrange identity:
\[
\boxed{
|\nabla u|^2+|\nabla w|^2
\le
2\left(\rho'|\nabla_A\Phi|^2
      +\rho|\nabla_{A'}\Phi'|^2\right).
}
\tag{10}
\]
Since \(0\le\rho,\rho'\le2\) at \(s=-4\),
\[
\|\nabla u\|_2^2+\|\nabla w\|_2^2
\le4(K+K').
\tag{11}
\]
Topology can therefore force spinor kinetic energy through variation of \((u,w)\), but in the simultaneous-field identity that kinetic term occurs with a minus sign.

For the projective spin directions,
\[
|\nabla_A\Phi|^2
=\frac{|\zeta|^2}{\rho}+\frac{\rho}{4}|\nabla n|^2,
\qquad
|\nabla_{A'}\Phi'|^2
=\frac{|\zeta'|^2}{\rho'}+\frac{\rho'}4|\nabla n'|^2.
\tag{12}
\]
In particular,
\[
\frac{\rho}{4}|\nabla n|^2
+\frac{\rho'}4|\nabla n'|^2
\ge
\frac{\rho\rho'}{4(\rho+\rho')}
 |\nabla(n-n')|^2.
\tag{13}
\]
This identifies the relative spin-rotation channel exactly, but again its energy contributes to \(K+K'\).

## 3. Why the pair can unwind through \(w\)

The pair of bilinears is a section
\[
q=(u,w)\in\Gamma(\mathcal Q),\qquad
\mathcal Q=N^*\oplus D,
\]
with
\[
|q|^2=\rho\rho'.
\tag{14}
\]
For the one-flip pair
\[
a=c-E,\qquad a'=c+E,\qquad c\cdot E=0,
\]
one has
\[
c_1(N^*)=-E,\qquad c_1(D)=c,
\]
and hence
\[
\boxed{
c_2(\mathcal Q)=(-E)\cdot c=0.
}
\tag{15}
\]
Thus the rank-two section \(q\) carries no four-dimensional zero number. If both spinors are nonzero, \(q\) is automatically nonzero even though \(u\) must have a zero cycle representing \(-E\).

Locally, after normalization,
\[
\frac{(u,w)}{\sqrt{\rho\rho'}}\in S^3.
\]
The phase winding of \(u\) on a small normal circle is an \(S^1\)-vortex only when \(w\equiv0\). Inside \(S^3\) that loop is contractible because \(\pi_1(S^3)=0\): it can be filled by turning on \(w\). This is the precise topological form of the orthogonality mechanism.

For a transverse \(u\), its phase current gives, with compatible orientation,
\[
h=2\pi[Z_u]+d j_u
\tag{16}
\]
as currents. Equation (16) records the class of \(Z_u\), but contains no norm estimate. When \(u=0\) because the two spinors are orthogonal, the first component of \(q\) vanishes while the second remains large.

## 4. Exact Kähler vortex completion

The Kähler situation adds the missing complex first-order structure. Let \((M,g,J,\omega)\) be Kähler, \(|\omega|^2=2\), and let \(H\) be the real curvature of a Hermitian line bundle \(\mathcal L\), with
\[
[H/(2\pi)]=\gamma.
\]
Choose the unitary convention for which
\[
\|\nabla\varphi\|_2^2
=2\|\bar\partial_H\varphi\|_2^2
+\int(\Lambda H)|\varphi|^2\,d\mu.
\tag{17}
\]
For every constant \(\tau>0\),
\[
\boxed{
\begin{aligned}
&\int_M\left(
 |H|^2+|\nabla\varphi|^2
 +\frac14(\tau-|\varphi|^2)^2\right)d\mu\\
={}&-\int_MH\wedge H+\tau\int_MH\wedge\omega\\
&+\int_M\left[
 2|H^{2,0}+H^{0,2}|^2
 +2|\bar\partial_H\varphi|^2
 +\left(\Lambda H-\frac{\tau-|\varphi|^2}{2}\right)^2
 \right]d\mu .
\end{aligned}
}
\tag{18}
\]
This follows from
\[
|H|^2d\mu
=-H\wedge H+
\left[(\Lambda H)^2+2|H^{2,0}+H^{0,2}|^2\right]d\mu
\]
and completion of the scalar square.

If \(\gamma^2=-1\), then
\[
\boxed{
\mathcal E_\tau(H,\varphi)
=
4\pi^2+2\pi\tau\,\gamma\cdot[\omega]
+\text{the three squares in \((18)\)}.
}
\tag{19}
\]
Reversing the bundle sign replaces \((H,\bar\partial)\) by \((-H,\partial)\).

Now suppose one SW spinor is parallel with \(|\Phi|^2=\tau\), and the second is aligned:
\[
\Phi'=\varphi\,p,\qquad \Phi=\sqrt\tau\,p,
\]
for a parallel unit spinor \(p\). Then
\[
w=0,\qquad |u|^2=\tau|\varphi|^2.
\]
The Dirac equation becomes the appropriate holomorphic equation for \(\varphi\), while the curvature equation gives
\[
\Lambda H=\frac{\tau-|\varphi|^2}{2}.
\tag{20}
\]
Thus all three squares in (18) vanish. A zero of \(u\) is then necessarily an amplitude zero, and the energy above \(4\pi^2\) is the period term
\[
2\pi\tau\,|\gamma\cdot[\omega]|.
\tag{21}
\]

For a Kähler blow-up, \([\omega]\cdot E=e>0\), so each fixed Kähler class produces a strict period contribution. As \(e\to0\), this contribution tends to zero. This agrees with the strict inequality \(P>8\pi^2k\) for each Kähler metric and the recovery value \(8\pi^2k\) when exceptional areas shrink.

Equation (18) is not by itself a lower estimate for \(P\): its kinetic term has a plus sign, whereas the simultaneous SW identity subtracts spinor kinetic energy. Kähler scalar geometry supplies the additional relation used in the blow-up theorem.

## 5. The perpendicular null-period regime

When the compatible two-form has
\[
[\omega]\cdot E=0,
\]
the period term in (19) disappears. More importantly, the non-Kähler pair is not confined to \(w=0\). The zero of \(u\) may be realized by
\[
\rho,\rho'>0,\qquad n'=-n,\qquad |w|^2=\rho\rho'.
\]
Identity (1) then prices orthogonality only through the volume integral of \(|w|^2\). A codimension-two zero set has zero four-volume, so its pointwise value gives no fixed integral.

A tubular scaling makes this explicit. If the exceptional sphere has area \(A_E\) and the spin direction rotates across a normal disk of radius \(r\), then typically
\[
|\nabla n|\sim r^{-1},\qquad
\operatorname{Vol}(\text{tube})\sim A_Er^2.
\]
Hence
\[
\int_{\text{tube}}|\nabla n|^2=O(A_E),\qquad
\int_{\text{tube}}|w|^2=O(A_Er^2).
\tag{22}
\]
The \(4\pi^2\) relative Yang–Mills contribution remains fixed by (1), while the rotation and orthogonality additions can vanish when \(A_E\to0\). This is exactly the channel available to a perpendicular cell. The isolated cell need not carry a symmetric SW pair; the calculation describes how any closed-host pair can evade an amplitude-vortex estimate once its exterior data permit \(w\neq0\).

## 6. The precise estimate needed for a unit tariff

For one exceptional class and no handle term, define
\[
\mathcal R(\Phi)
=
8\|\zeta\|_2^2
+4\|W^+-W_0\|_2^2
+\int b(\rho)(2-\rho)^2,
\qquad
b(t)=\frac{-t^2+8t+2}{6}.
\]
The simultaneous identity specializes exactly to
\[
\boxed{
P-8\pi^2
=
2\|\bar f^-\|_2^2
+2\|h^+\|_2^2
+\frac{\mathcal R(\Phi)+\mathcal R(\Phi')}{2}
-2(K+K').
}
\tag{23}
\]
Thus \(P\ge8\pi^2\) follows precisely from
\[
2(K+K')
\le
2\|\bar f^-\|_2^2
+2\|h^+\|_2^2
+\frac{\mathcal R(\Phi)+\mathcal R(\Phi')}{2}.
\tag{24}
\]
Equations (5)–(15) do not imply (24). There are two independent reasons:

1. **Common amplitude mode.** At the algebraic level, aligned spinors with
   \(\rho=\rho'=2-\varepsilon\) have \(h^+=w=0\). Their kinetic identity is linear in \(\varepsilon\),
   \[
   K+K'=\frac12\int\!\left[\rho(2-\rho)+\rho'(2-\rho')\right],
   \]
   while the displayed amplitude squares are quadratic in \(\varepsilon\). Pair-relative quantities do not see this common depletion.

2. **Rank-two rotation mode.** The class of \(u\) can be transferred into the \(w\)-component because \(c_2(N^*\oplus D)=0\). The resulting spin-direction energy lies in \(K+K'\), with the sign shown in (23).

A strict excess would follow from a quantitative strengthening: for some \(\theta>0\),
\[
2(K+K')
\le
2\|\bar f^-\|_2^2
+\frac{\mathcal R(\Phi)+\mathcal R(\Phi')}{2}
+(2-\theta)\|h^+\|_2^2.
\tag{25}
\]
Then
\[
P\ge8\pi^2+\theta\|h^+\|_2^2.
\tag{26}
\]
There are concrete geometric settings in which \(\|h^+\|_2\) itself is priced. If a closed self-dual form \(\omega\) satisfies
\[
|E\cdot[\omega]|\ge d_0>0,\qquad \|\omega\|_2^2\le V_0,
\]
then
\[
\|h^+\|_2^2
\ge
\frac{\left|\int h\wedge\omega\right|^2}{\|\omega\|_2^2}
\ge\frac{4\pi^2d_0^2}{V_0}.
\tag{27}
\]
Combined with (25), this gives a fixed per-class addition. The perpendicular regime has \(d_0=0\), so (27) supplies nothing.

Alternatively, suppose \(u\) is transverse, \(\rho,\rho'\ge m>0\) near \(Z_u\), \(|\nabla|w||\le L\), and a tube of radius \(r_0\le m/(2L)\) around \(Z_u\) has volume at least \(V_0\). Since \(|w|\ge m\) on \(Z_u\),
\[
2\|h^+\|_2^2
\ge\int|w|^2
\ge\frac{m^2V_0}{4}.
\tag{28}
\]
Together with (25), this gives
\[
P\ge8\pi^2+\frac{\theta m^2V_0}{8}.
\tag{29}
\]
The essential inputs here are a persistent tube, amplitude lower estimates, derivative control, and control of the common kinetic mode. They are absent in collapsing or null-period geometries.

In summary, the paired equations yield the exact relative Yang–Mills identity (1), the bilinear Bochner system (5)–(7), and the exact one-pair curvature-cost formula (23). They also reveal why topology alone does not supply the desired tariff: \(u\) is not governed by a scalar vortex equation, its curvature coupling vanishes at its own zero set, and the rank-two field \((u,w)\) can unwind the \(u\)-vortex through spinor orthogonality. Kähler geometry suppresses that channel by imposing \(w=0\) and produces the period term (19); perpendicular null-period geometry retains the rotation channel and provides no metric-uniform addition beyond the \(4\pi^2\) relative Yang–Mills charge.