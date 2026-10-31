# Step 22 — Hyperbolic volume/mass structure and the off-bolt Weyl theorem

Conventions follow `theorem_package_v1.md`. Two real-hyperbolic normalizations are used explicitly:

- closed scale: `K=-1`, `Ric=-3g`, `s=-12`;
- cell scale: `K=-2`, `Ric=-6g`, `s=-24`.

## 1. Closed hyperbolic blow-ups: a quantitative pointwise-Ricci theorem

Let \((Y,g_0)\) be a closed oriented real-hyperbolic four-manifold at
\(K=-1\), let
\[
X=Y\#k\overline{\mathbb{CP}}^{\,2},\qquad k\ge1,
\]
and let \(f:X\to Y\) be the degree-one pinch map. Relative Chern–Weil gives,
for every constant-scalar metric \(g\) on \(X\) with \(s_g=-12\),
\[
P(g)=8\pi^2k+4\int_X|W_g^+|^2+12\{\operatorname{Vol}_g(X)-\operatorname{Vol}_{g_0}(Y)\}. \tag{1.1}
\]
Here \(P=\int|\operatorname{Ric}^\circ|^2\) and the Weyl norm is the curvature-operator norm.

**Theorem H\(_\varepsilon\) (entropy gap with a Ricci floor).** If, in addition,
\[
\operatorname{Ric}_g\ge-3(1+\varepsilon)g,\qquad \varepsilon\ge0,
\]
then
\[
\operatorname{Vol}_g(X)\ge(1+\varepsilon)^{-2}\operatorname{Vol}_{g_0}(Y), \tag{1.2}
\]
and therefore
\[
P(g)\ge 8\pi^2k
-12\operatorname{Vol}_{g_0}(Y)\left[1-(1+\varepsilon)^{-2}\right]. \tag{1.3}
\]
If \(\varepsilon=0\), BCG rigidity says equality in (1.2) forces the pinch map to be homotopic to a Riemannian covering. This is impossible when \(k>0\). Hence for every \(k>0\),
\[
\operatorname{Ric}_g\ge-3g,\\ s_g=-12
\quad\Longrightarrow\quad
P(g)>8\pi^2k. \tag{1.4}
\]

**Proof.** The degree-one Besson–Courtois–Gallot inequality gives
\[
h(g)^4\operatorname{Vol}_g(X)\ge 3^4\operatorname{Vol}_{g_0}(Y).
\]
Bishop comparison under the stated Ricci floor gives
\(h(g)\le3\sqrt{1+\varepsilon}\). This proves (1.2). Substitution into
(1.1), followed by discarding \(4\int|W^+|^2\ge0\), proves (1.3).
Equality for \(\varepsilon=0\) is the BCG equality case. \(\square\)

This theorem is the exact coefficient-eight lower result in a natural
pointwise-Ricci class. Expanding its loss gives
\[
12\operatorname{Vol}(Y)[1-(1+\varepsilon)^{-2}]
=24\operatorname{Vol}(Y)\varepsilon+O(\varepsilon^2).
\]
It also isolates the critical difficulty: the unrestricted direct defect gives
only \(L^2\) control of \(\operatorname{Ric}^\circ\), not the Ricci floor needed
by Bishop comparison.

Primary source read: `Knowledge/objects/papers/Differentiable-rigidity-under-Ricci-curvature-lower-bound--cfb4c9cdd3c7--65a5a48bd00c/object.md`, especially Theorems 1.1 and 1.5 and the entropy derivation at lines 91–100.

## 2. The constant-scalar sharp gap and the hyperbolic volume problem

Equation (1.1) makes the unresolved scalar-normalized statement precise. The
degree-one scalar-volume inequality
\[
s_g\ge-12\quad\Longrightarrow\quad
\operatorname{Vol}_g(X)\ge\operatorname{Vol}_{g_0}(Y) \tag{2.1}
\]
would imply, for \(s_g\equiv-12\), the exact lower bound
\(P(g)\ge8\pi^2k\). Conversely, the volume inequality is exactly the missing
scalar input in this Chern–Weil route; the Weyl term means the numerical bound
\(P\ge8\pi^2k\) alone does not logically imply (2.1) for an individual
metric. Thus “equivalence” must be read as equivalence of the proposed
*field-free derivation* and the scalar-volume statement, not literal logical
equivalence metric by metric.

For negative Yamabe invariant, (2.1) is the assertion
\[
Y(X)\le Y(Y)=-12\operatorname{Vol}_{g_0}(Y)^{1/2}. \tag{2.2}
\]
The standard connected-sum inequality supplies the opposite inequality
\(Y(X)\ge Y(Y)\) because \(\overline{\mathbb{CP}}^2\) has positive Yamabe
invariant. Consequently (2.1) on the blow-up is equivalent to the Yamabe
identity
\[
Y\!\left(Y\#k\overline{\mathbb{CP}}^{\,2}\right)=Y(Y). \tag{2.3}
\]
The available primary sources establish this identity for important
Seiberg–Witten-supplied families, but not for arbitrary closed
real-hyperbolic four-manifolds. `Differentiable rigidity...` records that
Perelman settles the corresponding scalar-volume infimum in dimension three,
whereas in dimensions at least four the general connected-sum/Yamabe argument
only gives the easy inequality. No source retrieved here proves (2.3) in
four dimensions. This is the degree-one hyperbolic scalar-volume problem often
associated with Schoen's volume comparison question; we retain its unresolved
status rather than promote it to a theorem.

## 3. Exact-H\(^4\)-exterior cells: scalar-floor topology is impossible

Let \((M^4,g)\) be complete without boundary, exactly hyperbolic of sectional
curvature \(-1\) outside a compact set, with spherical end, and suppose
\(s_g\ge-12\). Chruściel–Delay's Theorem 1.6 states that in dimensions
\(3\le n\le7\) such a manifold is isometrically diffeomorphic to
\(\mathbb H^n\); their proof is non-spin. In general their Theorem 1.3 derives
AH energy positivity from the asymptotically Euclidean positive mass theorem,
and Huang–Jang–Martin supply zero-mass rigidity. For an exactly hyperbolic
exterior the mass vector is zero, so rigidity applies.

After scaling to the cell normalization, this yields:

**Theorem H\(_\mathrm{cell}\).** A complete exact-\(H^4\)-exterior
four-manifold with \(s\ge-24\) is hyperbolic space. Therefore no
\(D\#k\overline{\mathbb{CP}}^2\), \(k\ge1\), exact-\(H^4\)-collar cell can
satisfy \(s\ge-24\) everywhere.

Primary sources:

- `Knowledge/objects/papers/The-hyperbolic-positive-energy-theorem--8a032b16b3af--cfd203eab901/object.md`, Theorems 1.3 and 1.6;
- `Knowledge/objects/papers/Mass-Rigidity-for-Hyperbolic-Manifolds--36e83c2bd58b--2559be97cc05/object.md`, Theorem 3.

This is stronger and more general than the diagonal computations, but it does
not yet imply \(P\ge8\pi^2\): every topologically nontrivial competitor must
dip below the hyperbolic scalar value, and a sharp integral theorem must show
that its \((s+24)^2\) payment and Weyl energy dominate any negative
cosmological Einstein–Hilbert response. The positive-mass theorem supplies the
rigid scalar-floor half of the desired calibration, not the quantitative
completion for metrics that cross below the floor.

## 4. Why the complex-hyperbolic witness evades this rigidity

Maerten–Minerbe's ACH positive-mass theorem applies to a **spin,
asymptotically complex-hyperbolic Kähler/Hermitian manifold** with
\(s\ge s_{CH}\); in even complex dimension it additionally assumes
contractibility. It is not a non-spin all-metric theorem on
\(O(-1)\). See
`Knowledge/objects/papers/A-mass-for-asymptotically-complex-hyperbolic-manifolds--0585fd23b4a7--593794dd4404/object.md`, Theorem 0.1.

The certified cheap perpendicular CH cell also leaves the scalar-floor regime
explicitly. `workspace/scripts/ch_cell_scalar_min.py` evaluates the same
frozen metric used by the Arb cost certificate. At the bolt,
\[
s=-24.802356352356668<-24,
\]
and a 6801-point profile gives \(s<-24\) from the bolt through approximately
\(u=0.9428\), approaching \(-24\) in the exact collar. The value at the bolt is
directly enclosed using the Arb point evaluation. Record:
`workspace/data/ch_cell_scalar_profile_x003_X64.json`.

Thus this witness would not contradict even an all-metric ACH theorem carrying
the hypothesis \(s\ge s_{CH}\). The real/complex contrast is therefore
sharper than “real AH has a non-spin theorem, complex AH does not”: the CH
witness violates both the known structural hypotheses and the scalar lower
bound.

## 5. Computer-assisted off-bolt Weyl theorem for Theorem E

The Step-21 C++ draft was not correct. It used a wrong sign in solving the
Einstein equations for orbit sectional curvatures and inferred mixed curvature
entries from an invalid shortcut. `workspace/scripts/ach_weyl_interval.cpp`
now computes:

- \(K_{0i}=-(y_i'+y_i^2)\);
- \(K_{ij}\) from \(\operatorname{Ric}_{ii}=K_{0i}+K_{ij}+K_{ik}=-6\);
- the mixed entries directly from the Cartan connection, e.g.
  \[
  R_{0123}=-y_1n_1+y_2A+y_3C,
  \]
  with \(n_i=2a_i/(a_ja_k)\),
  \(A=(n_1+n_2-n_3)/2\), and cyclic analogues.

The runner `workspace/scripts/ach_weyl_interval_run.py` first compares the
CAPD formula to the independent coordinate/JAX curvature evaluation at the
same CAPD endpoint midpoint. The sorted spectra agree within
\(5.6\times10^{-15}\); the reconstructed scalar is \(-24\), and the
trace-free Ricci norm is \(8.5\times10^{-15}\).

It then transports all forty outward-rounded analytic Fuchsian boxes from
\(t=.01\) to \(t=.5\). Every signed pairwise gap in both chiral blocks excludes
zero. The weakest lower distances from zero are
\[
0.966994778415921,
\qquad
0.003926698448708077,
\]
and the corresponding discriminant lower bounds are
\[
66.18831770098221,
\qquad
0.0006333125307976167.
\]
The complete interval record is
`workspace/data/ach_capd/weyl_discriminant_t0.5.json`.

**Theorem E\(^+\).** The validated ACH Einstein metric of Theorem E has simple
Weyl spectrum in both chiralities at \(t=.5\). Hence no metric conformal to it
is Kähler in either orientation on a neighborhood of that orbit. Because the
Einstein metric is real analytic, a conformally Kähler structure on any
nonempty open set would force the appropriate Weyl discriminant to vanish
identically; the certified nonzero value excludes this. Thus the metric is not
conformally Kähler on any nonempty open set in either orientation.

This strictly strengthens the exact bolt result: the bolt proves non-Kähler and
non-half-conformally-flat, whereas the off-bolt interval theorem excludes
local conformal Kählerness.
