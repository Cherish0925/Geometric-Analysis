# TTCS Independent Branch Record

```json
{
  "step_id": 45,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step45_o10_cell_tiling_tidal_radius_charge.md",
    "Sessions/S1003A01/workspace/scripts/step45_tnads_cartan.py",
    "Sessions/S1003A01/workspace/data/step45/tnads_cartan.json",
    "Sessions/S1003A01/workspace/scripts/step45_killing_moment_check.py",
    "Sessions/S1003A01/workspace/data/step45/killing_moment_check.json",
    "Skills/geometric-analysis/research/sources/archive/sources/20261001-web-increment/Line1_Web_Increment_20260929_30/research/B/O10_Global_Compatibility.md",
    "Sessions/S1003A02/trace/ttcs/results/step2_ttcs01_generator2_integration.md"
  ]
}
```

## Task

Scientific verification of the Step-45 O10 note. Context: the O10 problem (density-free zero-Weyl endpoint lower bound for the four-manifold Einstein gap) and its escape regime chi/p->infinity, |W^-|/V->infinity, with a bounded resolvent negative spinor v, (L-2)v=q->0 in normalized L^2, m=|v|^2->m_*=128/81, and the Gibbons-Hawking/Taub-NUT tangent v=sqrt(m_*/2) d(bar f), m=m_*R/(R+ell). The note claims: (1) Taub-NUT-AdS with F=1+R(R+2ell)/3 is exactly Ric=-g with W^+=0 in the hyperkahler orientation (Cartan script + JSON supplied); (2) a tiling identity |Omega|=E_Omega/(2m_*) for flux-free completions and the interpretation of R(R+ell)^2=3ell/4 as a Wigner-Seitz radius of a nut lattice with base nut density theta Vbar/(pi ell); (3) the tidal coincidence ell/R_*^3->4/3, |W^-|^2->32/3; (4) Section 3: the radial/v0 solvability condition of the order-epsilon cell problem equals the flux balance, so there is no leading-order radial obstruction; (5) Proposition 4.1: on Einstein W^+=0 manifolds, nabla_X (dK)^+ = (s/6)(X wedge K)^+ for Killing K, with fixed-point values |(dK)^+| = 0 (nut), sqrt2 (bolt), 2sqrt2 (anti-nut) for unit-weight semi-free actions, giving the path bound int|K| >= 12/|s| from a nut to a bolt; checked on TNAdS; (6) the Stokes/Euler-number statement that a nut-only collapsed region must have boundary Euler number N, and the homogenized Helmholtz law Delta_gamma Vbar = -4 theta Vbar. Please check each mathematically: signs and constants (especially in Prop 4.1, the Killing identity nabla^2 K = R(.,K), the norms at fixed points, and whether the Lambda^- -> Lambda^+ block is Ric^0), the validity of the Stokes/Euler-number argument for semi-free circle actions (orbit-space boundary, orientation of nut charges relative to the 4D orientation and W^+), whether the claim that isolated cores are excluded 'by an exact identity' is justified or needs extra hypotheses (pointwise smallness of Delta m outside cells is not established in the unbounded-density regime), the Wigner-Seitz density and the averaged GH equation, and the interpretation in Section 6 (opening-volume heuristic, complex-hyperbolic cusp count). Identify any error, overstatement, or missing hypothesis, and state precisely which parts are rigorous, which formal, and which heuristic. Also say whether Prop 4.1 is known in the literature (quaternionic-Kahler moment map) only if you are confident, otherwise name the precise knowledge_request to make.

## Output

# Scientific verification memo

## Overall assessment

Step 45 contains several sound and useful calculations, especially the exact Taub–NUT–AdS geometry, the flux ledger, the tidal scaling, and the fixed-point norm computation. Three substantial corrections are needed:

1. The Killing-moment formula has the wrong sign in the standard curvature convention used by the curvature-operator decomposition. Its norm consequences and path constants remain correct.
2. The cubic
   \[
   R(R+\ell)^2=\frac{3\ell}{4}
   \]
   is the exact **TN flux/mass balance equation**, not the exact equation saying that a TN geodesic ball has volume \(4\pi^2\ell^2\). Those two radii agree only asymptotically.
3. The order-\(\varepsilon\) radial solvability, Euler-charge application to O10 sequences, homogenized Einstein–Weyl equation, and cusp-volume discussion remain formal or heuristic. In particular, the O10 metrics have not been shown to possess an exact or approximate circle action.

The note therefore supplies strong model geometry but does not yet establish a density-free O10 obstruction.

---

## 1. Exact Taub–NUT–AdS cell

### 1.1 Einstein and chirality calculation

For
\[
H=1+\frac{\ell}{R},\qquad
F=1+\frac{R(R+2\ell)}3,
\]
and
\[
g=\frac HF\,dR^2+HR^2(\sigma_1^2+\sigma_2^2)
       +\ell^2\frac FH\,\sigma_3^2,
\]
the result
\[
\operatorname{Ric}=-g,\qquad s=-4,\qquad W^+=0
\]
is correct in the \(e^{0123}\) orientation used in `step45_tnads_cartan.py`.

The JSON presentation is less clean than the mathematics:

- `Ricci_diag` consists of four exact entries \(-1\), so the scalar is exactly \(-4\), even though the serialized `scalar` field remains an unsimplified radical expression.
- The radical occurring in `Wplus_sq_e0123` is a perfect square. If
  \[
  u=R(R+2\ell),
  \]
  then the polynomial outside the radical is \((u+3)^2\), while the radicand is \((u+3)^4\). Since \(u+3>0\), its square root is \((u+3)^2\), and \(W^+\) vanishes identically.
- The numerical sentence “\(\le 3\cdot10^{-21}\) at all tested points” does not match the last JSON row, which records approximately \(8.7\cdot10^{-18}\). This is cancellation error and has no mathematical significance once the perfect-square simplification is made.

The opposite Weyl block simplifies further to
\[
\operatorname{eig}(W^-)
=
\frac{\ell(1-\ell^2/3)}{(R+\ell)^3}(-1,-1,2),
\]
hence
\[
|W^-|^2
=
\frac{6\ell^2(1-\ell^2/3)^2}{(R+\ell)^6}.
\]
Thus its ratio to the TN value is exactly \((1-\ell^2/3)^2\), independent of \(R\). The observed relative discrepancy \(6.67\cdot10^{-5}\) at \(\ell=10^{-2}\) is consistent with this formula.

### 1.2 Volume and Laplacian

The identities
\[
AB^2C=\ell R(R+\ell),\qquad
\frac{B^2C}{A}=\ell R^2F
\]
are correct. With \(\int\sigma_1\wedge\sigma_2\wedge\sigma_3=16\pi^2\), the radial volume element is
\[
dV=16\pi^2\ell R(R+\ell)\,dR.
\]

The statement that the Einstein deformation is \(C^0\)-small on \(R\asymp\ell^{1/3}\) is also correct:
\[
F-1=\frac{R(R+2\ell)}3=O(\ell^{2/3}),
\]
while its second derivatives produce an order-one Ricci change. This is a useful explicit example of small metric displacement with order-one curvature response.

What it establishes is local: an exact Einstein, \(W^+\)-free metric exists with the desired TN core. Cutting such cells at \(R_*\) and fitting their induced data together is a separate geometric problem.

---

## 2. Flux identity, cell volume, and Wigner–Seitz density

### 2.1 Conditional flux identity

From
\[
\Delta m=2|\nabla v|^2-4m-2\operatorname{Re}\langle q,v\rangle
\]
with the div–grad scalar Laplacian,
\[
\int_{\partial\Omega}\partial_\nu m
=
2E_\Omega-4\int_\Omega m
-2\operatorname{Re}\int_\Omega\langle q,v\rangle.
\]
Consequently, if

\[
\int_{\partial\Omega}\partial_\nu m=o(\ell^2),\qquad
\int_\Omega\operatorname{Re}\langle q,v\rangle=o(\ell^2),
\]
and
\[
\int_\Omega|m-m_*|=o(\ell^2),
\]
then
\[
|\Omega|=\frac{E_\Omega}{2m_*}+o(\ell^2).
\]

This is rigorous under those quantitative assumptions. Merely saying \(m\to m_*\) “in measure” is enough only when it means convergence relative to \(\Omega\), together with uniform boundedness or another uniform-integrability input.

### 2.2 The exact radius correction

For the TN field,
\[
E(R)=8\pi^2m_*\ell^2\left(\frac{R}{R+\ell}\right)^2,
\qquad
M(R):=\int_{B_R}m
=\frac{16\pi^2}{3}m_*\ell R^3.
\]
The flux balance \(2E(R)=4M(R)\) is exactly
\[
\boxed{R(R+\ell)^2=\frac{3\ell}{4}}.
\]

By contrast, the TN geometric volume is
\[
\operatorname{Vol}(B_R)
=
16\pi^2\ell\left(\frac{R^3}{3}+\frac{\ell R^2}{2}\right).
\]
The exact equation \(\operatorname{Vol}(B_R)=4\pi^2\ell^2\) is
\[
\boxed{4R^3+6\ell R^2=3\ell},
\]
not the cubic used in Step 45.

At the flux-balance radius,
\[
\frac{E(R_*)}{2m_*}
=
4\pi^2\ell^2\left(\frac{R_*}{R_*+\ell}\right)^2,
\]
which tends to \(4\pi^2\ell^2\), and the geometric volume differs from this by relative order
\[
\frac{\ell}{R_*}=O(\ell^{2/3}).
\]
Thus the stated cell volume and Wigner radius are asymptotically correct, but the word “exactly” should be reserved for the weighted flux/mass equation.

### 2.3 Nut density

If \(N\) TN cores contribute a fraction \(\theta\) of the total energy \(2m_*\mathcal V_4\), then
\[
N\,(8\pi^2m_*\ell^2)
=
\theta(2m_*\mathcal V_4),
\]
so
\[
\frac{N}{\mathcal V_4}
=
\frac{\theta}{4\pi^2\ell^2}.
\]
The full four-volume per nut is therefore
\[
\frac{\mathcal V_4}{N}
=
\frac{4\pi^2\ell^2}{\theta}.
\]

In a GH region,
\[
dV_4=V\,d\psi\,dV_\gamma,\qquad \operatorname{period}(\psi)=4\pi\ell.
\]
If \(V\) varies slowly enough to be represented by \(\bar V\), then
\[
n_3
=
\frac{N}{\mathcal V_3}
=
4\pi\ell\,\bar V\,\frac{N}{\mathcal V_4}
=
\boxed{\frac{\theta\bar V}{\pi\ell}}.
\]
A Euclidean base ball containing one nut then obeys
\[
\frac{4\pi r^3}{3}=\frac1{n_3},
\qquad
r^3=\frac{3\ell}{4\theta\bar V}.
\]
At \(\theta=\bar V=1\), this agrees with \(R_*\) to leading order, not exactly at finite \(\ell\).

There are two distinct cells in this discussion:

- the flux-completion region, of asymptotic volume \(4\pi^2\ell^2\);
- the full Wigner cell, of average volume \(4\pi^2\ell^2/\theta\).

Keeping those notions separate resolves the apparent factor of \(\theta\).

### 2.4 “Isolated cores are excluded”

The global identity yields
\[
\int_M|\nabla v|^2
=
2m_*\operatorname{Vol}(M)+o(\operatorname{Vol}(M)).
\]
If TN cores account for a fixed fraction of this energy, it forces their number-density scaling. It does **not** by itself force
\[
|\nabla v|^2\simeq2m
\]
pointwise outside selected cells.

The pointwise formula
\[
\langle Lv,v\rangle
=
|\nabla v|^2+\frac12\Delta^+m
\]
still contains \(\Delta m\), which can concentrate on thin transition sets. Normalized \(L^2\) control of \((L-2)v\) and convergence of \(m\) in measure do not control this term pointwise. Scalar capacity models already exhibit precisely such concentration.

Thus the exact global ledger excludes a configuration with too few TN cores carrying all required energy, but it does not establish a pointwise energetic exterior or rule out widely separated cores unless the surface fluxes and local mass errors are also controlled.

---

## 3. Tidal radius

From
\[
R_*(R_*+\ell)^2=\frac{3\ell}{4},
\]
one obtains
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
These constants and the numerical table are correct.

Calling this a “tidal radius” is geometrically apt in the order-of-magnitude sense: the TN Weyl field has reached the ambient curvature scale \(O(1)\). It is not equality with a uniquely normalized scalar-curvature norm; the manuscript uses the \(3\times3\) curvature-operator norm for \(W^-\).

The cell parameter
\[
\varepsilon=\frac{\ell}{R_*}\asymp\ell^{2/3}
\]
is also consistent:
\[
R_*^2\asymp\varepsilon,
\]
so Einstein and eigenvalue terms enter at order \(\varepsilon\) after rescaling to unit cell size, while an order-one physical gradient of \(\Phi\) produces variation \(O(R_*)=O(\varepsilon^{1/2})\).

---

## 4. Order-\(\varepsilon\) radial solvability

The scalar identity does identify the \(v_0\)-component of a fully specified self-adjoint cell problem: pairing the corrected rough-Laplacian equation with \(v_0\) and integrating gives the same mass/flux ledger.

However, the current note has not yet specified enough to conclude that the complete radial sector has no order-\(\varepsilon\) obstruction. The required mathematical data include:

- the actual periodic or matching conditions on the Wigner cell;
- the self-adjoint domain of the cell operator;
- the moving-interface contribution;
- the order-\(\varepsilon\) determinant-curvature and torsion-parent terms;
- local control showing that the rescaled \(q\)-term is smaller than order \(\varepsilon\);
- the kernel and cokernel for that particular realization.

The pointwise orthogonality
\[
\langle v_0^\perp,v_0\rangle=0
\]
does show that the pure source \(2v_0\) has no \(v_0^\perp\)-component. It says nothing yet about the \(v_0^\perp\)-components of
\[
(\delta L)v_0,\qquad
\text{torsion forcing},\qquad
\text{determinant-curvature forcing}.
\]

Accordingly, the scientifically supported conclusion is narrower:

> The eigenvalue term has a scalar projection that can be balanced by the flux/mass choice, and it has no direct projection onto \(v_0^\perp\). The complete order-\(\varepsilon\) coupled solvability conditions remain unevaluated.

The observation that \(|f|^2=R^2(1-n_3^2)\) contains an \(l=2\) component correctly excludes an \(SU(2)\)-radial truncation. A \(T^2\)-equivariant formulation in \((R,n_3)\) can retain all harmonics generated by the nonlinear terms and is the natural reduced system.

---

## 5. Killing-moment identity

### 5.1 Sign correction

Use the standard conventions
\[
R(X,Y)=\nabla_X\nabla_Y-\nabla_Y\nabla_X-\nabla_{[X,Y]},
\]
and choose the curvature operator so that a space form of sectional curvature \(k\) has \(\mathcal R=kI\). For a Killing field \(K\),
\[
\nabla_X(\nabla K)=R(X,K),
\]
but converting the skew endomorphism \(\nabla K\) into the two-form \(dK^\flat=2\nabla K\) introduces a sign:
\[
\boxed{\nabla_XdK^\flat=-2\mathcal R(X^\flat\wedge K^\flat)}.
\]
Therefore, on an Einstein four-manifold with \(W^+=0\),
\[
\boxed{
\nabla_X(dK^\flat)^+
=
-\frac{s}{6}(X^\flat\wedge K^\flat)^+.
}
\]

More generally,
\[
\nabla_X(dK^\flat)^+
=
-2\left(W^++\frac{s}{12}I\right)(X\wedge K)^+
-2B(X\wedge K)^-,
\]
where
\[
B:\Lambda^-\longrightarrow\Lambda^+
\]
is the curvature-operator block induced by \(\operatorname{Ric}^\circ\). Thus the note is correct that the \(\Lambda^-\to\Lambda^+\) block is the trace-free Ricci tensor, but the displayed sign in Proposition 4.1 is reversed under these conventions.

The TNAdS computation confirms the corrected sign. There,
\[
|(dK)^+|=\frac{2\sqrt2}{3}\ell R
\]
increases radially, while \(s=-4\). The formula with \(-s/6=2/3\) has the correct sign; the formula as printed does not.

### 5.2 Fixed-point norms

Let \(K\) have period \(2\pi\). At an isolated fixed point with weights \(a,b\in\{\pm1\}\),
\[
dK^\flat=2a\,e^{12}+2b\,e^{34},
\]
hence
\[
|(dK^\flat)^+|=\sqrt2\,|a+b|.
\]
Therefore:

- compatible nut, weights \((1,-1)\): \(0\);
- anti-nut, weights \((1,1)\): \(2\sqrt2\);
- bolt, one zero tangent weight and one unit normal weight: \(\sqrt2\).

These constants are correct.

For a unit-speed curve,
\[
|(X\wedge K)^+|
=
\frac{|X\wedge K|}{\sqrt2}
\le\frac{|K|}{\sqrt2}.
\]
Starting from a compatible nut where \((dK)^+=0\),
\[
\Delta |(dK)^+|
\le
\frac{|s|}{6\sqrt2}\int_\gamma|K|.
\]
Thus
\[
\int_\gamma|K|
\ge\frac{12}{|s|}
\]
to reach a bolt value, and
\[
\int_\gamma|K|
\ge\frac{24}{|s|}
\]
to reach an anti-nut value. For \(s=-4\), these are \(3\) and \(6\).

TNAdS actually saturates the radial bolt-value estimate:
\[
A\,|K|=2\ell,\qquad
\int_0^{3/(2\ell)}|K|\,ds
=
\int_0^{3/(2\ell)}2\ell\,dR=3.
\]
There is no bolt at that radius; only the moment norm has reached the value that a unit-weight bolt would have.

### 5.3 Literature status

The structural identity is standard in quaternionic–Kähler geometry: the \(\mathfrak{sp}(1)\) component of \(\nabla K\) is the quaternionic moment section, and its covariant derivative is contraction of \(K\) with the quaternionic curvature. In four dimensions, with the relevant orientation, this becomes the self-dual Einstein Killing-moment equation above. The coefficient \(s/6\) follows from the curvature block \(s/12\) and \(dK=2\nabla K\); the overall sign depends on the stated conventions.

---

## 6. Euler charge for semi-free circle actions

For an **exact** semi-free \(S^1\)-action, the local topology is sound. Remove small invariant balls around isolated fixed points and pass to the free orbit space. If \(F\) is the curvature of a principal-circle connection, then
\[
dF=0,
\]
and Stokes gives that the sum of the Chern numbers on all oriented two-surface components of \(\partial B\) is zero.

The two isolated fixed-point chiralities have opposite local Euler signs. Once the global circle orientation and quotient orientation are fixed, all compatible unit-weight nuts have the same local sign, while anti-nuts have the opposite sign. Hence a region containing \(N\) compatible nuts and no other fixed components transmits Euler number of magnitude \(N\) through its outer interface.

For a bolt, the contribution is global: it is determined by the Euler number of the normal circle bundle, equivalently the bolt self-intersection. It should not be described as one unit “at every bolt point.” The moment norm \(\sqrt2\) is pointwise, while the topological contribution is an integral over the bolt.

Three additional assumptions are required before applying this to an O10 sequence:

1. The O10 metrics have not been shown to carry an exact semi-free circle action.
2. Even an approximate collapsed circle structure has not been produced from normalized \(L^2\) curvature information.
3. The relation “one zero of \(v\) per nut” presupposes TN-type isolated zeros with local index \(+1\). In general, \(c_2(E_-)\) is the signed index sum of zeros of a transverse section; it does not itself identify those zeros with geometric nuts.

Thus the Stokes theorem is rigorous for an exact circle-action model, whereas
\[
N\asymp \frac{\theta\mathcal V_4}{\ell^2}
\]
and the identification of this \(N\) with the large \(c_2(E_-)\) density are model-dependent.

There is also a prior analytic issue in transferring the moment estimate: even if a genuine Killing field existed, four-dimensional normalized \(L^2\) control of \(W^+\) and \(\operatorname{Ric}^\circ\) does not control their integrals along individual curves. A trace estimate, regularity theorem, or a genuinely integrated three-dimensional version would be needed.

---

## 7. Averaged GH equation and Helmholtz law

For flat-base GH geometry with
\[
H=1+\frac{\ell}{R},
\]
the div–grad convention gives
\[
\Delta_\gamma V=-4\pi\ell\sum_a\delta_a.
\]
After coarse averaging,
\[
\Delta_\gamma\bar V=-4\pi\ell\,n_3.
\]
Substituting
\[
n_3=\frac{\theta\bar V}{\pi\ell}
\]
gives
\[
\boxed{\Delta_\gamma\bar V=-4\theta\bar V}.
\]
For a fibre-invariant function in the GH metric,
\[
\Delta_g f=V^{-1}\Delta_\gamma f,
\]
so formally
\[
\Delta_g\bar V=-4\theta.
\]

The sign and factor \(4\) are correct. On flat \(\mathbb R^3\), a regular radial solution has the form
\[
\bar V(r)=C\frac{\sin(2\sqrt\theta\,r)}{r},
\]
so it reaches its first zero at a distance of order \(\theta^{-1/2}\). On a compact base,
\[
0=\int\Delta_\gamma\bar V
=-4\theta\int\bar V
\]
excludes a positive solution when \(\theta>0\).

This derivation is a flat GH homogenization. At the macroscopic Einstein scale, the geometry is not GH: Jones–Tod uses an Einstein–Weyl base and a generalized monopole equation whose coefficient depends on the Weyl-connection convention. The source term proportional to \(\bar V\), and its coupling to Toda data, has not been derived in the note. The spectral observation for a hyperbolic model is mathematically reasonable—positive \((-\Delta)\)-eigenfunctions occur up to the generalized spectral bottom—but it is not yet an equation for the actual Toda system.

---

## 8. Circle opening and the complex-hyperbolic cusp

TNAdS does not cancel its nut charge through a bolt or anti-nut. It carries the unit Euler class outward while the orbit length grows. Thus it models transmission of charge out of the collapsed phase, not topological cancellation.

The complex-hyperbolic cusp discussion has a plausible scaling basis. In a standard horospherical normalization,
\[
g=dt^2+e^{-2t}g_{T^2}+e^{-4t}\eta^2,
\]
where the central circle length \(L\) scales like \(e^{-2t}\). For a Nil quotient with Euler number \(N\), the horizontal area is proportional to \(NL\), so the three-volume of a horosphere scales as
\[
N L^2.
\]
Since \(dt\asymp dL/L\),
\[
\operatorname{Vol}\{L\in[\ell,1]\}
\asymp
N\int_\ell^1L\,dL
\asymp N,
\]
whereas the deeper tail \(0<L\le\ell\) has volume
\[
\asymp N\ell^2.
\]
With \(N\asymp\mathcal V_4/\ell^2\), these become respectively
\[
\asymp\frac{\mathcal V_4}{\ell^2},
\qquad
\asymp\mathcal V_4.
\]

This supports the rough count in Step 45: opening a charge-\(N\) cusp from circle size \(\ell\) to unit size is much too voluminous, while retaining only the deeply collapsed tail has the correct order of volume. It does not yet yield an O10 theorem because no gluing, truncation, field extension, or defect estimate has been supplied. The reversed orientation statement is correct: a complex-hyperbolic surface is Bochner-flat, so the vanishing Weyl half becomes \(W^+\) after orientation reversal.

---

## 9. Final scientific classification

### Exact or rigorous under explicitly stated assumptions

- TNAdS is Einstein with \(\operatorname{Ric}=-g\) and \(W^+=0\).
- Its volume density and radial Laplacian weight are as stated.
- The integrated mass/flux identity is correct when its surface, \(q\), and relative mass hypotheses hold.
- The tidal constants \(4/3\) and \(32/3\) are correct.
- The fixed-point moment norms and path constants \(12/|s|\), \(24/|s|\) are correct.
- The semi-free circle Stokes relation is correct for an exact action.
- The raw flat-base GH Poisson equation and its factor \(4\) after density closure are correct.

### Formal but mathematically well motivated

- Wigner-cell interpretation and base density for a locally uniform TN lattice.
- The order-\(\varepsilon\) cell expansion.
- The statement that the pure eigenvalue source has no \(v_0^\perp\)-projection.
- Replacement of GH by an Einstein–Weyl/Toda homogenized equation.
- Transfer of Killing-moment control to collapsed O10 sequences.

### Heuristic at present

- Complete absence of an order-\(\varepsilon\) radial obstruction in the full torsion/determinant system.
- Identification of every large-\(c_2(E_-)\) unit with one TN nut.
- Existence of a global collapsed nut phase with a semi-free circle structure.
- A universal volume cost for transmitting or cancelling all \(N\) units of Euler charge.
- The complex-hyperbolic cusp as an actual O10-compatible absorber.

The principal concrete corrections are therefore the sign
\[
\nabla_X(dK)^+=-\frac{s}{6}(X\wedge K)^+,
\]
and the distinction between the exact flux radius
\[
R(R+\ell)^2=\frac{3\ell}{4}
\]
and the exact TN volume radius
\[
4R^3+6\ell R^2=3\ell.
\]