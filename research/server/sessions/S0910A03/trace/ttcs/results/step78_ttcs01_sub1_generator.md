# TTCS Independent Branch Record

```json
{
  "step_id": 78,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step78_bianchi_vii0_verify.py",
    "Sessions/S0910A03/workspace/data/step78_bianchi_vii0_symbolic.json",
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md",
    "Sessions/S0910A03/workspace/notes/step76_center_energy_transport_and_scattering.md",
    "Sessions/S0910A03/workspace/notes/step77_pe_scattering_correction.md"
  ]
}
```

## Task

Using the same rotating-eigenframe Bianchi VII_0 ansatz and exact ODEs, search for the strongest rigorous invariant or monotonicity statement relevant to vanishing-defect graph connectors. The target is not a complete PE metric but a finite connector starting at a reflection face and needing to reach an expanding regime with u=a'/a positive, small full Ricci defect, and eventual compatibility with the Step 73 tail. Examine exact and delta-forced equations, Hamiltonian/normal constraints, possible integrating factors, and sign barriers. Develop concrete lemmas with explicit constants or state exactly why no stronger geometry-independent constant follows. Also infer what genuinely additional matrix/base mechanism a successful construction would need once this ansatz is excluded. Do not propose generic numerical optimization; give mathematical structure and testable equations.

## Output

The rotating-eigenframe Bianchi VII\(_0\) ansatz has a very strong one-sided structure.  It rules out not only complete PE behavior, but any finite vanishing-defect connector from a reflection face to a Step 73 expanding entry.

Let

\[
g=dr^2+a(r)^2dz^2+b(r)^2\omega_1^2+c(r)^2\omega_2^2,
\qquad
d=\log(b/c),
\]

\[
u=\frac{a'}a,\quad v=\frac{b'}b,\quad w=\frac{c'}c,\quad
H=u+v+w,\quad p=d'=v-w.
\]

The symbolic calculation gives

\[
K=2k^2a^{-2}\sinh^2 d,\qquad
L=K\coth d,
\]

and, for \(E=\operatorname{Ric}+3g\),

\[
u'+Hu=3-K-E_z,
\tag{1}
\]

\[
d''+Hd'=2K\coth d-(E_1-E_2),
\tag{2}
\]

\[
(\log K)'=-2u+2\coth(d)d',
\tag{3}
\]

\[
H'+(u^2+v^2+w^2)=3-E_r.
\tag{4}
\]

The Hamilton relation obtained by subtracting (4) from the sum of the three tangential equations is

\[
H^2-(u^2+v^2+w^2)
=
6-K+E_r-E_z-E_1-E_2.
\tag{5}
\]

At a reflection face \(S(0)=0\), hence \(u(0)=v(0)=w(0)=0\), and therefore

\[
K(0)=6+E_r(0)-E_z(0)-E_1(0)-E_2(0).
\tag{6}
\]

Thus if \(\|E\|_{\rm op}\le \delta\),

\[
6-4\delta\le K(0)\le 6+4\delta.
\tag{7}
\]

For \(\delta<3/5\), in particular \(K(0)>0\), so \(d(0)\neq0\).  Put

\[
\sigma=\operatorname{sgn}d(0),\qquad D=\sigma d>0,\qquad q=D'=\sigma d'.
\]

Then

\[
q'+Hq=2K\coth D-\sigma(E_1-E_2),
\tag{8}
\]

\[
(\log K)'=-2u+2\coth D\,q.
\tag{9}
\]

The essential invariant region is

\[
u\le0,\qquad q\ge0,\qquad K\ge 6-4\delta.
\tag{10}
\]

Indeed, on \(q=0\),

\[
q'\ge 2(6-4\delta)-2\delta=12-10\delta>0;
\tag{11}
\]

on \(u=0\),

\[
u'\le 3-(6-4\delta)+\delta=-3+5\delta<0;
\tag{12}
\]

and on \(K=6-4\delta\),

\[
(\log K)'=-2u+2\coth D\,q\ge0.
\tag{13}
\]

Hence for every smooth finite interval on which \(\|E\|_{\rm op}\le\delta<3/5\),

\[
\boxed{
u(r)<0,\qquad D'(r)>0,\qquad K(r)\ge 6-4\delta
\quad (r>0).
}
\tag{14}
\]

In the exact case \(\delta=0\), this says

\[
a(r)\ \text{strictly decreases},\qquad |d(r)|\ \text{strictly increases},\qquad K(r)\ge6.
\tag{15}
\]

So the VII\(_0\) core moves away from a flat expanding cusp geometry: the \(z\)-scale contracts, the orbit anisotropy grows, and the intrinsic twist curvature cannot be diluted.

A quantitative form also follows from the normal equation.  Since

\[
H'\le 3+\delta-\frac13H^2,
\]

comparison gives

\[
H(r)\le 3\beta_\delta\tanh(\beta_\delta r),
\qquad
\beta_\delta=\sqrt{1+\delta/3}.
\tag{16}
\]

Define

\[
\Psi_\delta(r)=
\int_0^r
\left(
\frac{\cosh(\beta_\delta s)}{\cosh(\beta_\delta r)}
\right)^3ds
=
\frac{\sinh(\beta_\delta r)+\frac13\sinh^3(\beta_\delta r)}
{\beta_\delta\cosh^3(\beta_\delta r)}.
\tag{17}
\]

Then for \(\delta<3/5\),

\[
\boxed{
u(r)\le -(3-5\delta)\Psi_\delta(r),
}
\tag{18}
\]

\[
\boxed{
D'(r)\ge (12-10\delta)\Psi_\delta(r),
}
\tag{19}
\]

and

\[
\boxed{
(\log K)'(r)\ge 30(1-\delta)\Psi_\delta(r).
}
\tag{20}
\]

As \(r\to\infty\),

\[
\Psi_\delta(r)\to \frac1{3\beta_\delta},
\]

so any long VII\(_0\) connector has uniformly contracting \(a\), uniformly increasing anisotropy, and exponentially increasing \(K\).  In the exact case,

\[
u(r)\lesssim -1,\qquad D'(r)\gtrsim 4,\qquad (\log K)'(r)\gtrsim 10
\]

for large \(r\), in the precise comparison sense above.

The Hamilton relation gives an additional finite-interface obstruction.  From (5), (7), and \(K(r)\ge6-4\delta\),

\[
H^2-|S|^2
=
6-K+E_r-E_z-E_1-E_2
\le 8\delta.
\tag{21}
\]

Thus the shape operator never enters the hyperbolic-cusp cone.  If some slice had

\[
S=I+P,\qquad \|P\|_{\rm op}\le\varepsilon,
\]

then

\[
H^2-|S|^2
=
6+4\operatorname{tr}P+(\operatorname{tr}P)^2-|P|^2
\ge
6-12\varepsilon-6\varepsilon^2.
\tag{22}
\]

Combining (21) and (22), such a slice cannot occur whenever

\[
6-12\varepsilon-6\varepsilon^2>8\delta.
\tag{23}
\]

So a sequence with \(\delta_j\to0\) cannot reach any Step 73-compatible entry with \(S\to I\).  Even the weaker requirement \(u>0\) is already impossible by (14).

The intrinsic Ricci eigenvalues of a VII\(_0\) slice are

\[
-K,\qquad L,\qquad -L,
\qquad |L|=K|\coth D|\ge K.
\tag{24}
\]

Hence the normalized intrinsic curvature remains at least \(6-4\delta\).  A Step 73 tail entry requires the opposite behavior: an almost umbilic expanding slice with normalized intrinsic curvature tending to zero.  The VII\(_0\) ansatz cannot supply that interface.

The exact normal integrating factor,

\[
\frac{d}{dr}\left(e^{2r}(3-H)\right)
=
e^{2r}|S-I|^2,
\tag{25}
\]

and its forced version,

\[
\frac{d}{dr}\left(e^{2r}(3-H)\right)
=
e^{2r}\bigl(|S-I|^2+E_r\bigr),
\tag{26}
\]

are useful but weaker here.  In the forced equation, the term \(e^{2r}E_r\) can accumulate order-one size on intervals with \(r\sim \log(1/\delta)\).  The VII\(_0\) \(u,D,K\) barrier is stronger because it has an order-one gap in the tangential equations.

The numerical constant \(3/5\) comes exactly from

\[
K(0)\ge6-4\delta,\qquad
u'|_{u=0}\le 3-K+\delta.
\]

Thus the component inequalities alone give the inward sign

\[
3-(6-4\delta)+\delta<0
\iff
\delta<3/5.
\]

Raising this number would require information relating the center combination
\(E_r-E_z-E_1-E_2\) to later values of \(E_z\), or some derivative/integral control on \(E\).  The displayed ODEs with only \(\|E\|_{\rm op}\le\delta\) do not contain such a relation.

The scientific meaning is clear: the VII\(_0\) ansatz has reduced the orbit-shape dynamics to a scalar \(D(r)\) in a fixed direction of

\[
\mathrm{SL}(2,\mathbb R)/\mathrm{SO}(2),
\]

with repulsive potential

\[
K(D,a)=2k^2a^{-2}\sinh^2D,
\qquad
\partial_DK=2K\coth D.
\]

At the reflection face \(K\approx6\); thereafter \(a\) decreases and \(|D|\) increases, so the potential reinforces itself.

A successful connector must therefore use a mechanism absent from this ansatz.  In the orthogonally transitive \(T^2\)-invariant setting, with orbit metric

\[
G=\rho U,\qquad \det U=1,\qquad
U:\text{quotient}\to \mathrm{SL}(2,\mathbb R)/\mathrm{SO}(2),
\]

the scalar equation is replaced by the matrix divergence law

\[
\nabla_\gamma^i\bigl(\rho\,U^{-1}\nabla_iU\bigr)
=
-2\rho\,E_{\rm orb}^{\circ}.
\tag{27}
\]

For diagonal \(U=\operatorname{diag}(e^d,e^{-d})\), this reduces to

\[
\operatorname{div}_\gamma(\rho\nabla d)
=
-\rho(E_x-E_y).
\tag{28}
\]

The associated stress tensor is

\[
T_{ij}
=
\frac14\operatorname{tr}
\bigl(
U^{-1}\nabla_iU\,U^{-1}\nabla_jU
\bigr),
\tag{29}
\]

which in the scalar diagonal case is \(T_{ij}=\frac12 d_i d_j\).

Thus the missing mechanism is not another radial warping factor.  It is two-dimensional base transport and matrix-valued orbit-shape motion: \(z\)-dependent flux, covariance energy, and possibly off-diagonal twist directions.  Step 73’s expanding tail works precisely because the anisotropy equation becomes

\[
d_{rr}+3d_r+e^{-2r}d_{zz}\approx0,
\tag{30}
\]

so unweighted shear can decay while weighted stress survives.  The VII\(_0\) ODE has no \(d_{zz}\) transport and no rotation of the tension vector inside the hyperbolic-plane target.

A viable non-VII\(_0\) construction would need equations in which the center energy is carried by the flux/covariance law rather than by a one-signed scalar momentum.  Concretely, one should see terms of the form (27)–(29), with Hamilton and Codazzi compatibility, and with the normal balance

\[
(H-3)'+2(H-3)+|S-I|^2=-E_r
\tag{31}
\]

paid by base/matrix stress rather than by the homogeneous twist potential \(K\).  Off-diagonal orbit data of the Li–Liu type illustrate the needed direction: a twist variable \(A_z\) and DtN datum \(p\) enter the PE-infinity representative through

\[
A_z=\frac12e^\phi p,\qquad
R=-e^{-\phi}\phi_{zz}-\frac18p^2,
\tag{32}
\]

activating a matrix direction invisible in the scalar VII\(_0\) reduction.

So the VII\(_0\) ansatz is decisively excluded for vanishing-defect graph connectors; any successful route must break the scalar radial monotonicity by using genuine base dependence and full matrix orbit-shape dynamics.