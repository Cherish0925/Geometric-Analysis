# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 45,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step45_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step45_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Scientific verification of the Step-45 O10 note. Context: the O10 problem (density-free zero-Weyl endpoint lower bound for the four-manifold Einstein gap) and its escape regime chi/p->infinity, |W^-|/V->infinity, with a bounded resolvent negative spinor v, (L-2)v=q->0 in normalized L^2, m=|v|^2->m_*=128/81, and the Gibbons-Hawking/Taub-NUT tangent v=sqrt(m_*/2) d(bar f), m=m_*R/(R+ell). The note claims: (1) Taub-NUT-AdS with F=1+R(R+2ell)/3 is exactly Ric=-g with W^+=0 in the hyperkahler orientation (Cartan script + JSON supplied); (2) a tiling identity |Omega|=E_Omega/(2m_*) for flux-free completions and the interpretation of R(R+ell)^2=3ell/4 as a Wigner-Seitz radius of a nut lattice with base nut density theta Vbar/(pi ell); (3) the tidal coincidence ell/R_*^3->4/3, |W^-|^2->32/3; (4) Section 3: the radial/v0 solvability condition of the order-epsilon cell problem equals the flux balance, so there is no leading-order radial obstruction; (5) Proposition 4.1: on Einstein W^+=0 manifolds, nabla_X (dK)^+ = (s/6)(X wedge K)^+ for Killing K, with fixed-point values |(dK)^+| = 0 (nut), sqrt2 (bolt), 2sqrt2 (anti-nut) for unit-weight semi-free actions, giving the path bound int|K| >= 12/|s| from a nut to a bolt; checked on TNAdS; (6) the Stokes/Euler-number statement that a nut-only collapsed region must have boundary Euler number N, and the homogenized Helmholtz law Delta_gamma Vbar = -4 theta Vbar. Please check each mathematically: signs and constants (especially in Prop 4.1, the Killing identity nabla^2 K = R(.,K), the norms at fixed points, and whether the Lambda^- -> Lambda^+ block is Ric^0), the validity of the Stokes/Euler-number argument for semi-free circle actions (orbit-space boundary, orientation of nut charges relative to the 4D orientation and W^+), whether the claim that isolated cores are excluded 'by an exact identity' is justified or needs extra hypotheses (pointwise smallness of Delta m outside cells is not established in the unbounded-density regime), the Wigner-Seitz density and the averaged GH equation, and the interpretation in Section 6 (opening-volume heuristic, complex-hyperbolic cusp count). Identify any error, overstatement, or missing hypothesis, and state precisely which parts are rigorous, which formal, and which heuristic. Also say whether Prop 4.1 is known in the literature (quaternionic-Kahler moment map) only if you are confident, otherwise name the precise knowledge_request to make.

## Integrated Scientific Memo

# Verification of the Step‑45 O10 note

## Executive verdict

The note contains a valid exact model calculation, but its global O10 conclusions substantially exceed what has been proved.

The main corrections are:

1. **Proposition 4.1 has the wrong sign** under the sphere-positive curvature convention used by the Cartan script:
   \[
   \boxed{\nabla_X(dK^\flat)^+=-\frac{s}{6}(X^\flat\wedge K^\flat)^+.}
   \]
   The fixed-point norms and path bounds remain correct.

2. The equation
   \[
   R(R+\ell)^2=\frac{3\ell}{4}
   \]
   is the exact **finite-radius TN mass/flux balance**, not the exact equation for a TN ball of volume \(4\pi^2\ell^2\). The two radii agree only asymptotically.

3. “Isolated cheap insertions are excluded by an exact identity” is too strong. The global identity constrains total energy and forces depletion/flux balance, but does not give pointwise
   \(|\nabla v|^2\simeq2m\) outside cells and does not rule out isolated cores with transition or depletion shells.

4. Section 3 proves only a limited formal statement: the pure eigenvalue source has the expected scalar balance and no direct \(v_0^\perp\)-projection. The complete order-\(\varepsilon\) coupled cell solvability condition has not been computed.

5. The Euler-number/Stokes argument is rigorous only for an **exact, globally orientable, semi-free \(S^1\)-action**. No such action, or sufficiently controlled approximate action, is established for the O10 sequence. The identification “one zero of \(v\) = one positive nut” is also unproved.

6. The GH homogenization depends on how the background potential \(\bar V\) enters the scaled one-centre energy. The note’s linear Helmholtz law follows only if the four-volume per core is taken independent of \(\bar V\). If \(\bar V\) is the local GH background and the asymptotic field norm is fixed, homothety gives instead
   \[
   n_3=\frac{\theta\bar V^2}{\pi\ell},
   \qquad
   \Delta_\gamma\bar V=-4\theta\bar V^2.
   \]
   Thus the advertised Helmholtz equation is not established as written.

7. TNAdS does **not** discharge its nut charge: it carries the same circle-bundle degree outward while the circle opens. The complex-hyperbolic cusp count is a scaling heuristic, not an obstruction theorem.

Accordingly, Step 45 supplies strong exact model geometry and useful necessary ledgers, but no density-free O10 contradiction.

---

## 1. Exact Taub–NUT–AdS calculation

Let
\[
H=1+\frac{\ell}{R},\qquad
F=1+\frac{R(R+2\ell)}3,
\]
and
\[
g=\frac HF\,dR^2+HR^2(\sigma_1^2+\sigma_2^2)
+\ell^2\frac FH\,\sigma_3^2 .
\]

### Verified conclusions

The Cartan calculation supports, in the \(e^{0123}\) orientation,
\[
\boxed{\operatorname{Ric}=-g,\qquad s=-4,\qquad W^+=0.}
\]

The JSON’s scalar expression is merely unsimplified: its four Ricci diagonal entries are exactly \(-1\), hence \(s=-4\).

The apparent numerical residual in \(W^+\) is cancellation error. Setting
\[
u=R(R+2\ell),
\]
the radical in the JSON is \((u+3)^4\), while the polynomial outside it is \((u+3)^2\). Since \(u+3>0\), the difference vanishes identically. The note’s statement that the numerical residual is always at most \(3\cdot10^{-21}\) misquotes its own data—the final row is about \(8.7\cdot10^{-18}\)—but exact vanishing makes this harmless.

The remaining exact formulas are
\[
AB^2C=\ell R(R+\ell),\qquad
\frac{B^2C}{A}=\ell R^2F.
\]
Thus
\[
dV=16\pi^2\ell R(R+\ell)\,dR
\]
after angular integration, exactly as for TN.

The opposite Weyl tensor simplifies to
\[
\operatorname{eig}(W^-)
=
\frac{\ell(1-\ell^2/3)}{(R+\ell)^3}(-1,-1,2),
\]
and hence
\[
|W^-|^2
=
\frac{6\ell^2(1-\ell^2/3)^2}{(R+\ell)^6}.
\]
Therefore the TNAdS/TN squared-norm ratio is exactly
\[
(1-\ell^2/3)^2,
\]
independent of \(R\). This sharpens the note’s numerical “essentially unchanged” statement.

At the cell scale \(R\asymp\ell^{1/3}\),
\[
F-1=O(\ell^{2/3}),
\]
so the metric is \(C^0\)-close to TN while its Ricci curvature changes by order one. This is a valid and useful local model observation.

### Scope

This proves the existence of an exact Einstein, \(W^+\)-free continuation of the one-centre TN geometry. It does **not** prove that truncated TNAdS cells can be glued into an O10 sequence with compatible induced metric, connection, spinor, and flux data.

---

## 2. Integrated tiling identity and the balance radius

With the div–grad convention,
\[
\Delta m
=
2|\nabla v|^2-4m-2\operatorname{Re}\langle q,v\rangle .
\]
Integration over \(\Omega\) yields
\[
\int_{\partial\Omega}\partial_\nu m
=
2E_\Omega-4\int_\Omega m
-2\operatorname{Re}\int_\Omega\langle q,v\rangle .
\]

Thus
\[
|\Omega|
=
\frac{E_\Omega}{2m_*}+o(\ell^2)
\]
is rigorous provided, quantitatively,
\[
\int_{\partial\Omega}\partial_\nu m=o(\ell^2),\qquad
\int_\Omega\operatorname{Re}\langle q,v\rangle=o(\ell^2),
\]
and
\[
\int_\Omega|m-m_*|=o(\ell^2).
\]
Convergence merely “in measure” is insufficient without boundedness or uniform integrability. Global normalized estimates also do not imply these hypotheses for every individual cell; at best they give good-cell statements after a selection argument.

### Exact finite-radius balance

For the TN field,
\[
E(R)=8\pi^2m_*\ell^2
\left(\frac{R}{R+\ell}\right)^2,
\qquad
M(R):=\int_{B_R}m
=
\frac{16\pi^2}{3}m_*\ell R^3.
\]
The exact condition \(2E(R)=4M(R)\) is
\[
\boxed{R(R+\ell)^2=\frac{3\ell}{4}.}
\]

This is a weighted mass/flux equation. It is **not** the exact equation saying that the geometric volume of the TN ball equals \(4\pi^2\ell^2\). Indeed,
\[
\operatorname{Vol}(B_R)
=
16\pi^2\ell\left(\frac{R^3}{3}
+\frac{\ell R^2}{2}\right),
\]
so
\[
\operatorname{Vol}(B_R)=4\pi^2\ell^2
\quad\Longleftrightarrow\quad
\boxed{4R^3+6\ell R^2=3\ell.}
\]

At the flux-balance radius,
\[
\frac{E(R_*)}{2m_*}
=
4\pi^2\ell^2
\left(\frac{R_*}{R_*+\ell}\right)^2
=
4\pi^2\ell^2\bigl(1+O(\ell^{2/3})\bigr),
\]
so the note’s cell-volume statement is asymptotically correct, not exact.

### What the exact identity does—and does not—exclude

The closed-manifold identity gives
\[
\int_M|\nabla v|^2
=
2\int_Mm+\operatorname{Re}\int_M\langle q,v\rangle .
\]
Hence a prescribed number of TN cores cannot account for arbitrary fractions of the global energy: their number and the required complementary depletion/energy region obey an exact ledger.

It does not imply pointwise
\[
|\nabla v|^2\simeq2m
\]
outside chosen cells. The pointwise formula retains a Laplacian term:
\[
\langle Lv,v\rangle
=
|\nabla v|^2+\frac12\Delta^+m
\]
up to convention. Neither \((L-2)v\to0\) in normalized \(L^2\) nor \(m\to m_*\) in measure controls \(\Delta m\) pointwise. Thin transition sets can carry the necessary flux or capacity.

A defensible exact reformulation is a **depletion law**. If a flux-free region \(\Omega\) contains a core \(B\), then schematically
\[
\int_{\Omega\setminus B}
\bigl(2m-|\nabla v|^2\bigr)
=
E_B-2\int_Bm+o(\ell^2).
\]
Thus every core requires a compensating region, but this does not rule out geometrically isolated cores with depletion shells. The statements “isolated cheap insertions are excluded” and “the exterior is pointwise energetic” should be removed or weakened.

---

## 3. Tidal constants

From
\[
R_*(R_*+\ell)^2=\frac{3\ell}{4},
\]
one gets
\[
\frac{\ell}{R_*^3}
=
\frac43\left(1+\frac{\ell}{R_*}\right)^2
\longrightarrow\frac43.
\]
For TN,
\[
|W^-|^2(R_*)
=
\frac{6\ell^2}{(R_*+\ell)^6}
=
\frac{32}{3}
\left(\frac{R_*}{R_*+\ell}\right)^2
\longrightarrow\frac{32}{3}.
\]

Therefore
\[
\boxed{\ell/R_*^3\to4/3,\qquad |W^-|^2(R_*)\to32/3}
\]
is correct in the note’s curvature-operator norm.

This is not an independent numerical coincidence: the cell-volume balance fixes \(R_*^3\asymp\ell\), while the TN tidal scale is \(\ell/R^3\). Nevertheless, it correctly identifies the cell boundary as the region where the one-centre Weyl field becomes order one.

Also,
\[
\varepsilon=\frac{\ell}{R_*}\asymp\ell^{2/3},
\qquad
R_*^2\asymp\varepsilon.
\]
Thus the Einstein and eigenvalue terms enter at order \(\varepsilon\) in unit-cell variables. This scale counting is sound.

---

## 4. Section 3: order-\(\varepsilon\) solvability

The scalar identity does support the following limited assertion:

- once a particular self-adjoint cell problem and its boundary conditions are fixed, pairing the correction equation with \(v_0\) reproduces the same integrated mass/flux condition;
- the direct eigenvalue source \(2v_0\) is pointwise orthogonal to \(v_0^\perp\).

This does **not** yet prove that the full radial sector has no leading-order obstruction. The missing data include:

1. the precise periodic or matching boundary conditions on the Wigner cell;
2. the self-adjoint realization of the linearized operator;
3. moving-boundary/interface terms;
4. the complete order-\(\varepsilon\) metric, torsion-parent, determinant-curvature, and monopole forcing;
5. the rescaled order of the \(q\)-error on individual cells;
6. the actual kernel and cokernel for a lattice cell rather than a round TN domain.

Orthogonality of \(2v_0\) to \(v_0^\perp\) says nothing about
\[
(\delta L)v_0,\qquad
\text{torsion forcing},\qquad
\text{determinant-curvature forcing}.
\]
On a rotationally symmetric round cell, representation symmetry may kill additional pairings, but that conclusion does not automatically survive a periodic lattice cell.

The justified statement is therefore:

> The pure eigenvalue source has one scalar solvability condition, equivalent to the flux/mass balance, and no direct \(v_0^\perp\)-projection. The complete order-\(\varepsilon\) coupled solvability conditions remain uncomputed.

The note is correct that \(|f|^2=R^2(1-n_3^2)\) contains an \(l=2\) component, so an \(SU(2)\)-radial ODE is not a closed nonlinear truncation. A \(T^2\)-equivariant problem in \((R,n_3)\) is the appropriate reduced setting.

---

## 5. Correct Killing-moment identity

Adopt
\[
R(X,Y)=\nabla_X\nabla_Y-\nabla_Y\nabla_X-\nabla_{[X,Y]},
\]
and the curvature operator convention for which a space form of curvature \(k\) has \(\mathcal R=kI\). For a Killing field \(K\),
\[
\nabla_X\nabla K=R(X,K)
\]
as a skew endomorphism. Converting the skew endomorphism \(\nabla K\) to
\[
dK^\flat=2(\nabla K)^\flat
\]
introduces the sign
\[
\boxed{\nabla_XdK^\flat=-2\mathcal R(X^\flat\wedge K^\flat).}
\]

In dimension four,
\[
\mathcal R=
\begin{pmatrix}
W^++\frac{s}{12}I & B\\
B^* & W^-+\frac{s}{12}I
\end{pmatrix},
\]
where \(B:\Lambda^-\to\Lambda^+\) is the block represented by \(\operatorname{Ric}^\circ\). Thus the note is correct that the \(\Lambda^-\to\Lambda^+\) block is trace-free Ricci, subject to the usual identification and harmless normalization conventions.

Projection gives
\[
\nabla_X(dK^\flat)^+
=
-2\left(W^++\frac{s}{12}I\right)
(X^\flat\wedge K^\flat)^+
-2B(X^\flat\wedge K^\flat)^-.
\]
Hence on Einstein \(W^+=0\) manifolds,
\[
\boxed{
\nabla_X(dK^\flat)^+
=
-\frac{s}{6}(X^\flat\wedge K^\flat)^+.
}
\]

The sign printed in Proposition 4.1 is therefore wrong. TNAdS confirms the corrected sign: for \(s=-4\), the coefficient is \(-s/6=+2/3\), consistent with the radially increasing value
\[
|(dK)^+|=\frac{2\sqrt2}{3}\ell R.
\]
The supplied script used \(|s|/6\), so it could not detect the sign error.

### Fixed-point norms

Normalize \(K\) to have period \(2\pi\). At an isolated fixed point with unit weights \(a,b\in\{\pm1\}\),
\[
dK^\flat=2a\,e^{12}+2b\,e^{34},
\]
so
\[
|(dK^\flat)^+|=\sqrt2\,|a+b|.
\]
Therefore:

- compatible/triholomorphic nut, weights \((1,-1)\):
  \[
  |(dK)^+|=0;
  \]
- anti-nut, weights \((1,1)\):
  \[
  |(dK)^+|=2\sqrt2;
  \]
- bolt, one zero tangent weight and one unit normal weight:
  \[
  |(dK)^+|=\sqrt2.
  \]

These constants are correct. The bolt norm is pointwise, whereas a bolt’s topological contribution is the Euler number of its normal bundle, not “one unit at every bolt point.”

### Path bounds

For unit-speed \(X\),
\[
|(X\wedge K)^+|
=
\frac{|X\wedge K|}{\sqrt2}
\le \frac{|K|}{\sqrt2}.
\]
Consequently,
\[
\left|\frac{d}{dt}|(dK)^+|\right|
\le\frac{|s|}{6\sqrt2}|K|.
\]
Starting from a compatible nut gives
\[
\boxed{\int_\gamma |K|\,ds\ge\frac{12}{|s|}}
\]
before the bolt value can be attained, and
\[
\boxed{\int_\gamma |K|\,ds\ge\frac{24}{|s|}}
\]
before the anti-nut value can be attained. For \(s=-4\), these are \(3\) and \(6\).

TNAdS sharply realizes the first **moment-value threshold**:
\[
A|K|=2\ell,\qquad
\int_0^{3/(2\ell)}|K|\,ds
=\int_0^{3/(2\ell)}2\ell\,dR=3.
\]
There is no actual bolt at \(R=3/(2\ell)\); only \(|(dK)^+|\) has reached the value \(\sqrt2\) that a unit-weight bolt would have.

The phrase “loss of triholomorphic type occurs together with opening” is also too strong: \((dK)^+\) becomes nonzero immediately for \(R>0\). What occurs near \(R=3/(2\ell)\) is attainment of the bolt norm together with an order-one orbit size.

### Literature status

The structural identity is the four-dimensional self-dual Einstein form of the quaternionic-Kähler Killing moment-map equation. The exact normalization and sign are convention-dependent. A precise literature check, if needed, should request:

> **Knowledge request:** Locate an explicit statement, with curvature and Hodge-star conventions, of the four-dimensional self-dual Einstein Killing-field identity
> \[
> \nabla_X(dK)^{\mathrm{sd}}
> =c\,s\,(X\wedge K)^{\mathrm{sd}},
> \]
> and its interpretation as the quaternionic-Kähler moment map, preferably in Tod/Przanowski/Calderbank–Pedersen or standard quaternionic-Kähler moment-map references; determine the exact coefficient and sign under sphere-positive curvature conventions.

It is safe to call the structure standard, but a specific citation and normalization should not be asserted without that check.

---

## 6. Stokes and Euler number for circle actions

For an exact, globally oriented, semi-free \(S^1\)-action, remove invariant neighborhoods of fixed components and quotient the free part by \(S^1\). If \(F\) is the curvature of a principal-circle connection, then
\[
dF=0,
\]
and Stokes says that the sum of the Chern numbers over all oriented boundary components of the orbit space is zero.

Each isolated fixed point contributes local bundle degree \(\pm1\). After fixing the circle and quotient orientations:

- compatible nuts have one sign;
- anti-nuts have the opposite sign;
- bolts enter through the Euler number/self-intersection of their normal circle bundle.

Thus a region containing \(N\) compatible nuts and no other fixed components transmits outer boundary degree of magnitude \(N\). A closed orbit space containing only same-sign nuts is impossible.

This topological statement is rigorous **only under the following hypotheses**:

1. an exact global \(S^1\)-action exists on the region;
2. it is semi-free;
3. the circle orientation is globally consistent—no \(\mathbb Z_2\)-twisted local circle structure;
4. the relevant boundary is a genuine free-orbit boundary;
5. local nut signs are fixed relative to the global four-dimensional orientation.

These hypotheses are not established for the O10 sequence. In particular:

- normalized \(L^2\) smallness of \(W^+\) and \(\operatorname{Ric}^\circ\), with unbounded \(W^-\), does not produce a semi-free circle action or even a controlled global \(N\)-structure;
- pathwise curvature-error control does not follow from four-dimensional \(L^2\) control;
- \(c_2(E_-)\) is the signed index sum of zeros of a transverse section, but no theorem identifies every zero of \(v\) with a TN nut of index \(+1\).

Therefore
\[
N\asymp\theta V/\ell^2
\]
is a model count, not yet a theorem about the actual O10 sequence.

The statement “bolts and anti-nuts are the only possible opposite contributions” is true within a globally orientable semi-free circle-action model, but not for a merely local or sign-twisted collapse structure.

Finally, TNAdS does not “discharge” a nut charge. Its degree-one circle bundle persists through all finite-radius spheres and out toward infinity. It demonstrates **transmission of the charge while the circle opens**, not cancellation by a bolt or anti-nut.

---

## 7. Wigner–Seitz density and homogenized GH equation

There is an important normalization ambiguity overlooked in the note.

### If one freezes the unit-background core ledger

Taking the full four-volume per nut as
\[
\frac{4\pi^2\ell^2}{\theta}
\]
and using
\[
dV_4=4\pi\ell\,\bar V\,dV_\gamma
\]
gives
\[
n_3=\frac{\theta\bar V}{\pi\ell}.
\]
Then coarse averaging
\[
\Delta_\gamma V=-4\pi\ell\sum_a\delta_a
\]
gives
\[
\Delta_\gamma\bar V=-4\theta\bar V.
\]
This is the note’s formal Helmholtz law.

### If \(\bar V\) is the actual local GH background

Locally,
\[
V=\bar V+\frac{\ell}{R}
=\bar V\left(1+\frac{\ell/\bar V}{R}\right),
\]
and the metric is a homothety by \(\bar V\) of a TN metric with effective charge
\[
\ell'=\ell/\bar V.
\]
For the field normalized so that \(m\to m_*\), the Dirichlet energy scales under this homothety as
\[
E_{\rm core}
=
\bar V\cdot8\pi^2m_*(\ell')^2
=
\frac{8\pi^2m_*\ell^2}{\bar V}.
\]
The associated flux-completion four-volume is therefore
\[
\frac{E_{\rm core}}{2m_*}
=
\frac{4\pi^2\ell^2}{\bar V}.
\]
If such completions occupy fraction \(\theta\), then
\[
\frac{N}{V_4}
=
\frac{\theta\bar V}{4\pi^2\ell^2},
\]
and hence
\[
n_3
=
4\pi\ell\bar V\,\frac{N}{V_4}
=
\boxed{\frac{\theta\bar V^2}{\pi\ell}}.
\]
The averaged equation becomes
\[
\boxed{\Delta_\gamma\bar V=-4\theta\bar V^2,}
\]
or, for invariant functions,
\[
\boxed{\Delta_g\bar V=-4\theta\bar V.}
\]

This nonlinear law is the more internally consistent one if \(\bar V\) is permitted to vary macroscopically while the asymptotic field norm remains fixed. Therefore the note’s linear Helmholtz equation and its explicit
\(\sin(2\sqrt\theta r)/r\) profile should not be treated as established.

The sign-based compact-base obstruction survives either closure:
\[
\int\Delta_\gamma\bar V=0
\]
cannot equal the integral of a strictly negative source when \(\theta>0\) and \(\bar V>0\).

At the macroscopic Einstein scale, however, flat-base GH geometry itself ceases to apply. A Jones–Tod Einstein–Weyl/Toda homogenized equation would have to be derived from the actual metric and field system; merely replacing \(\Delta\) by an Einstein–Weyl operator does not determine the source or its power of \(\bar V\).

---

## 8. Circle opening and volume heuristics

For an exact Einstein region with \(\operatorname{Ric}=-g\) and Killing field \(K\), Bochner gives, with the div–grad convention,
\[
\frac12\Delta|K|^2
=
|\nabla K|^2-\operatorname{Ric}(K,K)
=
|\nabla K|^2+|K|^2.
\]
Thus an exact collapsed orbit length cannot remain approximately constant over arbitrarily long curvature-scale distances. This supports the opening phenomenon in TNAdS.

It also emphasizes a limitation: a closed negatively Einstein manifold has no nonzero global Killing field, so every exact circle-action discussion concerns a proper region, not the full closed manifold.

The proposed universal charge-discharge volume obstruction is not proved. In an exact invariant collar, a coarea estimate combined with the degree condition leads schematically to
\[
\operatorname{Vol}(T)
\gtrsim
N\inf_T\frac{|K|^2}{|dK|}.
\]
If
\[
|K|\asymp\ell,\qquad
N\asymp V/\ell^2,\qquad
|dK|\asymp1,
\]
this yields only an \(O(V)\) lower bound, not a contradiction. A superlinear cost such as \(V/\ell\) requires extra control of the form
\[
|dK|\lesssim |K|
\]
or another bound on the O’Neill tensor. In the O10 regime it is precisely possible that this large derivative is carried by the uncontrolled \(W^-\) geometry.

This isolates the relevant missing analytic quantity: the cost in \(\operatorname{Ric}^\circ\) and \(W^+\) of maintaining large \(|dK|/|K|\) at collapsed circle length.

### Complex-hyperbolic cusp

For the standard Nil-cusp scaling
\[
g\sim dt^2+e^{-2t}g_{T^2}+e^{-4t}\eta^2,
\]
the central circle length \(L\) scales like \(e^{-2t}\). For degree \(N\), a horosphere has volume proportional to \(NL^2\), so
\[
\operatorname{Vol}\{L\in[\ell,1]\}\asymp N,
\qquad
\operatorname{Vol}\{L\le\ell\}\asymp N\ell^2.
\]
If \(N\asymp V/\ell^2\), opening all the way to unit circle length costs \(\asymp V/\ell^2\), while retaining only the deep collapsed tail costs \(\asymp V\).

This is a plausible scaling heuristic. It is not an O10 obstruction because the following remain unchecked:

- orientation/sign compatibility between cusp degree and nut degree;
- a cap or gluing mechanism on the closed manifold;
- extension of the monopole and resolvent fields;
- control of the resulting Ricci and \(W^+\) defects.

The orientation-reversal observation is compatible with the standard fact that complex-hyperbolic surfaces are Bochner-flat in the complex orientation, so the vanishing Weyl half swaps after reversal.

---

## Final status table

| Step‑45 claim | Verification |
|---|---|
| TNAdS with the stated \(F\) has \(\operatorname{Ric}=-g\), \(s=-4\), \(W^+=0\) | **Rigorous and exact** |
| TNAdS volume density and radial Laplacian weight | **Rigorous and exact** |
| TNAdS \(W^-\) is asymptotic to TN \(W^-\) | **Rigorous; exact ratio \((1-\ell^2/3)^2\) for squared norms** |
| Flux-free identity \(|\Omega|=E_\Omega/(2m_*)+o(\ell^2)\) | **Rigorous under quantitative local flux, \(q\), and mass hypotheses** |
| \(R(R+\ell)^2=3\ell/4\) is the exact \(4\pi^2\ell^2\) volume radius | **Incorrect**; it is the exact mass/flux radius |
| Wigner–Seitz interpretation | **Formal/asymptotic**, requiring good cells and controlled background |
| Isolated cores excluded by an exact identity | **Overstatement**; only a global energy/depletion ledger is exact |
| Tidal limits \(4/3\) and \(32/3\) | **Rigorous** |
| Complete radial order-\(\varepsilon\) obstruction vanishes | **Not proved** |
| Pure \(2v_0\) source is balanced by scalar flux and orthogonal to \(v_0^\perp\) | **Formal but supported** |
| Proposition 4.1 as printed | **Wrong sign** |
| Corrected Killing-moment identity | **Rigorous** |
| Fixed-point norms \(0,\sqrt2,2\sqrt2\) | **Rigorous with period-\(2\pi\), unit-weight normalization** |
| Path bounds \(12/|s|\), \(24/|s|\) | **Rigorous for exact symmetry; sharp in the TNAdS moment-value sense** |
| Nut-only region has outer degree \(N\) | **Rigorous for exact globally oriented semi-free actions** |
| Application of that degree count to O10 | **Unproved** |
| TNAdS discharges nut charge | **Incorrect**; it transports the charge outward while opening |
| Linear Helmholtz law \(\Delta_\gamma\bar V=-4\theta\bar V\) | **Normalization-dependent and not established**; varying-background scaling gives \(-4\theta\bar V^2\) |
| Jones–Tod/Toda homogenization | **Formal open problem** |
| Complex-hyperbolic cusp volume obstruction | **Heuristic scaling only** |

The strongest durable content of the note is therefore: an exact TNAdS cell; the corrected mass/flux and tidal ledgers; the corrected Killing-moment identity with sharp path constants; and a conditional semi-free degree theorem. The unresolved bridge to density-free O10 is the construction or exclusion of a collapsed circle structure whose large \(|dK|/|K|\), lattice interactions, torsion-parent equation, and determinant-curvature equation remain compatible with small \(\operatorname{Ric}^\circ\) and \(W^+\) defects.