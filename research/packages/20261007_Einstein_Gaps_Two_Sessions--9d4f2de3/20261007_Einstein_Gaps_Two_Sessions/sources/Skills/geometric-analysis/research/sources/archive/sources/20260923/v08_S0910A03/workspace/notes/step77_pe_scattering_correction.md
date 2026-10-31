# Step 77: PE expansion, three-object distinction, and corrected scattering formulation

Session `S0910A03`, Agent2 / Explore.

## 0. Corrections to Step 76

The Step 76 note `step76_center_energy_transport_and_scattering.md` contains
three errors that must be corrected before the scattering formulation.

**Error 1 (twist energy)**: Equation (9.5) should read
\[
 \frac12\operatorname{tr}\bigl((U^{-1}U_s)^2\bigr)
 =\frac14e^{-\phi}\phi_z^2+\frac14p^2,
 \tag{0.1}
\]
not $\frac14e^{-\phi}(\phi_z^2+p^2)$.  The $p^2$ coefficient is $1/4$,
independent of $e^{-\phi}$.  The scalar curvature formula and integrated
variance condition are unaffected.  (Corrected in the note.)

**Error 2 (three-object conflation)**: Section 9 proposes testing whether a
Li--Liu boundary representative $q_\partial$ can have scalar curvature $-6$.
But $R(q_0)=-6$ is the center condition at $S=0$, while the conformal infinity
$\gamma$ at $r\to\infty$ satisfies $R_\gamma\le-24$ in the center-normalized global-foliation setting (see Section 2 below).  These
are at opposite ends of the manifold.  There is no reason to require
$R(\gamma)=-6$.  Failure of this false identification would not exclude a
reflected core.

**Error 3 (leading PE stress)**: Section 7B treats $e^{2r}(S-I)^\circ$ as
filling-dependent.  In fact its limit $\operatorname{Sch}(\gamma)^{\circ\sharp}$
is determined by conformal infinity alone.  The filling information enters only
at next order through the transverse-traceless (TT) datum $g_3$:
\[
 e^{3r}\bigl[S^\circ-\operatorname{Sch}(\gamma)^{\circ\sharp}e^{-2r}\bigr]
 \longrightarrow
 -\tfrac32\,\gamma^{-1}g_3.
 \tag{0.2}
\]
Matching only $\gamma$ does not distinguish fillings.

## 1. Three distinct geometric objects

| Object | Location | Condition | Notes |
|--------|----------|-----------|-------|
| $q_0$ (center metric) | $r=0$, the reflection face $S=0$ | $R(q_0)=-6$ | Intrinsic $T^3$ metric; carries $K_{\rm orb}\ge3$, $\langle d_s^2\rangle_\rho\ge12$ |
| $\gamma$ (conformal infinity) | $r\to\infty$, the PE boundary | $R_\gamma\le-24$ under the center-normalized global foliation; strict somewhere | A priori unrelated to $q_0$; negative Yamabe |
| $g_3$ (TT datum) | PE expansion coefficient | $\operatorname{tr}_\gamma g_3=0$, $\operatorname{div}_\gamma g_3=0$ | The **nonlocal filling datum**; determines the Einstein filling beyond $[\gamma]$ |

The center metric $q_0$ is determined by the reflection condition and the
equation $R(q_0)=-6$.  It carries the center theorem's orbit-plane curvature
and the integrated anisotropy energy.

The conformal infinity $\gamma$ is determined by the PE expansion as $r\to\infty$.
It satisfies $R_\gamma\le-24$ under the assumptions of Section 2, with strictness somewhere.  It is not the center metric and need
not have scalar curvature $-6$.

The TT datum $g_3$ carries all information about the Einstein filling beyond the
conformal class.  Different fillings with the same conformal infinity differ in
$g_3$.

## 2. The conformal infinity scalar curvature bound

**Proposition (scope corrected in Step 78).** Let $(M^4,g)$ be a Riemannian
manifold with $\operatorname{Ric}=-3g$, diffeomorphic to
$[0,\infty)\times T^3$, with a totally geodesic $T^3$ boundary at $r=0$
(i.e., $S(0)=0$). Assume that the outward normal exponential map supplies a
smooth global foliation through the PE end. If $g$ is Poincaré--Einstein as
$r\to\infty$ with center-normalized conformal representative $\gamma$, then,
pointwise along each normal ray,
\[
 \boxed{
 R_\gamma(x)=-12-4\int_0^\infty e^{2r}|S-I|^2(r,x)\,dr\le-24.
 }
\tag{2.1}
\]
Equality everywhere is impossible on $T^3$, hence strict inequality occurs at
at least one boundary point. This argument does not prove pointwise strictness
at every boundary point.

*Proof.*  The Riccati equation for $\operatorname{Ric}=-3g$ gives
$H'=-|S|^2+3$, hence $(H-3)'+2(H-3)+|S-I|^2=0$.  Equivalently,
\[
 \frac{d}{dr}\bigl[e^{2r}(3-H)\bigr]=e^{2r}|S-I|^2.
 \tag{2.2}
\]
Integrating from $r=0$ (where $H(0)=0$) to $R$:
\[
 e^{2R}(3-H(R))=3+\int_0^R e^{2r}|S-I|^2\,dr.
 \tag{2.3}
\]
The Fefferman--Graham expansion for $n=3$ gives
\[
 g_\rho=\gamma-\operatorname{Sch}(\gamma)\rho^2+g_3\rho^3+O(\rho^4),
 \qquad \rho=e^{-r},
\]
where $\operatorname{Sch}(\gamma)_{ij}=\operatorname{Ric}_{ij}-\frac{R_\gamma}4\gamma_{ij}$
and $g_3$ is TT.  The shape operator satisfies
\[
 S=I+\operatorname{Sch}(\gamma)^{\sharp}e^{-2r}
 -\tfrac32\gamma^{-1}g_3\,e^{-3r}+O(e^{-4r}).
 \tag{2.4}
\]
Taking the trace (using $\operatorname{tr}(\gamma^{-1}g_3)=0$):
\[
 H=3+\frac{R_\gamma}4\,e^{-2r}+O(e^{-4r}),
 \qquad
 3-H=-\frac{R_\gamma}4\,e^{-2r}+O(e^{-4r}).
 \tag{2.5}
\]
Hence $e^{2R}(3-H(R))\to-R_\gamma/4$ as $R\to\infty$.  Combining with (2.3):
\[
 -\frac{R_\gamma}4=3+\int_0^\infty e^{2r}|S-I|^2\,dr\ge3.
 \tag{2.6}
\]
Therefore $R_\gamma\le-12$.  But a sharper bound follows from Riccati
comparison.  Since $|S|^2\ge H^2/3$ (Cauchy--Schwarz on a $3\times3$ matrix),
$H'=3-|S|^2\le 3-H^2/3$.  The ODE $y'=3-y^2/3$, $y(0)=0$ has solution
$y=3\tanh r$, so $H(r)\le 3\tanh r$ and
\[
 e^{2r}(3-H(r))\ge e^{2r}\cdot 3(1-\tanh r)\longrightarrow 6.
 \tag{2.7}
\]
Hence $-R_\gamma/4\ge 6$, giving $R_\gamma\le-24$ pointwise. Equality along
one ray forces $S=(H/3)I$ only along that ray. If equality held on every ray,
then $S=(H/3)I$ globally, hence
$g=dr^2+\cosh^2(r)\,q_0$ with $\operatorname{Ric}(q_0)=-2q_0$. In dimension
three this means constant sectional curvature $-1$, impossible on $T^3$
(Preissmann: $\pi_1(T^3)=\mathbb Z^3$ is abelian). Thus equality cannot hold
everywhere, but this comparison alone does not exclude isolated equality rays.
Pointwise the shear integral satisfies
\[
 \int_0^\infty e^{2r}|S-I|^2\,dr\ge 3.
\tag{2.8}
\]

**Remark on gauge and foliation dependence.** The bound $R_\gamma\le-24$ holds
for the center-normalized boundary representative, i.e., the conformal infinity
selected by the geodesic defining function $\rho=e^{-r}$ anchored at the
reflection center $r=0$. It also presupposes that this normal coordinate reaches
the PE end without focal breakdown. It is not a conformal invariant: a different
representative $\widetilde\gamma=a^2\gamma$ with center at $\widetilde r_0=
-\log a$ shifts the formula accordingly. $\square$

## 3. The PE expansion: traceless stress and the filling datum

The traceless shape operator decomposes as
\[
 S^\circ=\operatorname{Sch}(\gamma)^{\circ\sharp}\,e^{-2r}
 -\tfrac32\,\gamma^{-1}g_3\,e^{-3r}+O(e^{-4r}).
 \tag{3.1}
\]
(Here $g_3$ is TT, so $\gamma^{-1}g_3$ is already traceless.)

The **leading PE stress** is
\[
 e^{2r}S^\circ\longrightarrow\operatorname{Sch}(\gamma)^{\circ\sharp}
 =\operatorname{Ric}(\gamma)^{\circ\sharp},
 \tag{3.2}
\]
which is locally determined by $\gamma$.  Agreement of this leading stress does
not distinguish fillings and should not be treated as a scattering comparison.

The **renormalized nonlocal stress** is
\[
 \boxed{
 e^{3r}\bigl[S^\circ-\operatorname{Sch}^{\circ\sharp}e^{-2r}\bigr]
 \longrightarrow-\tfrac32\,\gamma^{-1}g_3.
 }
 \tag{3.3}
\]
This is the physically meaningful filling datum.  Two PE metrics with the same
conformal infinity but different $g_3$ have different physical traceless stress
at infinity.

In the CMC gauge (Section 5 of the Step 76 note), the traceless shape operator
$P$ satisfies
\[
 (e^{3a}P)'=e^a\operatorname{Ric}(q_r)^\circ,
\]
so $e^{3a}P$ approaches a finite limit.  This limit is (up to gauge) the same
as $-\frac32g_3^\sharp$.

## 4. ASD obstruction and non-ASD fillings

**Proposition.**  An anti-self-dual (ASD) Einstein four-manifold with
$\operatorname{Ric}=-3g$ cannot have a compact totally geodesic $T^3$
hypersurface.

*Proof.*  Reflection across a compact totally geodesic hypersurface is a local
isometry that reverses orientation.  If $W^+=0$ (ASD), the reflected metric has
$W^-=0$.  By real-analyticity of Einstein metrics in harmonic coordinates, both
conditions extend to a neighborhood: $W=0$.  With $\operatorname{Ric}=-3g$ and
$W=0$, the Riemann tensor is $\operatorname{Rm}=-g\owedge g$, giving constant
sectional curvature $-1$.  A totally geodesic $T^3$ in $\mathbb H^4$ inherits
sectional curvature $-1$, contradicting Preissmann's theorem ($\pi_1(T^3)=
\mathbb Z^3$ is abelian, impossible for negative sectional curvature).  $\square$

**Consequence for exact reflected fillings.** The Li--Liu Type-I metrics are ASD
and have one PE end plus one AH cusp end. They cannot be cut at a $T^3$ level and
reflected to create a two-ended metric with a center. Any exact reflected-center
Einstein filling on $[0,\infty)\times T^3$ must therefore be non-ASD. A finite
connector with small nonzero defect need not arise from such a complete filling.

This is important for the exact scattering problem: one cannot simply use the
Li--Liu Toda Dirichlet-to-Neumann map as the outer-end response for a reflected
core. The Li--Liu metrics remain an outer-end benchmark and a source of matrix
and twist mechanisms, but exact reflection requires a non-ASD filling.

## 5. Corrected scattering problem

The correct scattering question has two parts:

**Part A (PE filling space).**  For a given negative-scalar-curvature $T^3$ metric $\gamma$ compatible with the
center-normalized bound in Section 2, what is the space of PE Einstein fillings of
$[0,\infty)\times T^3$ with conformal infinity $[\gamma]$?  Specifically, what
TT tensors $g_3$ on $(T^3,\gamma)$ can appear as the nonlocal PE datum?

In Anderson's framework, the space of PE fillings is related to a boundary map
of Fredholm index zero.  The Li--Liu Toda equation selects ASD fillings.  The
non-ASD sector has not been systematically explored for this topology.

**Part B (center intersection).**  Among all compatible PE fillings (non-ASD), does there exist one whose backward evolution from the PE end
reaches $S=0$ at some finite distance?  Equivalently, does the map
\[
 \Phi:(\gamma,g_3)\mapsto S(0)
\]
(defined by solving the Einstein equation backward from the PE end to a smooth
point) have $0$ in its image?

The constraints on the image include:
- $R(q_0)=-6$ (trace of $S'(0)=\operatorname{Ric}_{q_0}+3I$, giving
  $\operatorname{tr}S'(0)=3$);
- Center theorem: $\lambda_{\min}S'(0)\le-3$;
- Integrated center energy: $\langle d_s^2\rangle_\rho\ge12$;
- Normal identity: $-R_\gamma/4=3+\int_0^\infty e^{2r}|S-I|^2\,dr$;
- ASD exclusion: $g_3$ cannot be in the Li--Liu ASD sector.

**Why the Step 76 Section 9 question was misposed.**  Section 9 asks whether
the Li--Liu DtN map $\phi\mapsto p$ intersects the pointwise equation
$R(q_\partial)=-6$.  But:
1. This conflates $q_0$ and $\gamma$: the center metric $q_0$ has $R=-6$, while
   the center-normalized $\gamma$ obeys the distinct bound of Section 2.
2. A solution of $R(\gamma)=-6$ on the Li--Liu boundary family would select a
   specific $\gamma$, not produce a center.
3. Even if such $\gamma$ existed, the Li--Liu filling would be ASD and therefore
   incompatible with reflection (Section 4).

The correct question uses the non-ASD filling space and asks about backward
evolution, not about equating boundary scalars.

## 6. The expanding-mode picture in the corrected framework

The Step 73 expanding tail and the Step 76 expanding-mode calculations remain
valid as transport mechanisms.  For the reflected anisotropy mode on the flat
background:
\[
 \psi(t)\to\frac{\sinh k}k,\qquad
 e^{2t}\psi'(t)\to k\sinh k.
\]
This shows that unweighted shear $|S-I|^2$ near the PE end decays as
$O(e^{-4r})$ while the TT stress $e^{3r}S^\circ$ remains bounded.  The tail
mechanism can flatten anisotropy at small Ricci cost, and the mode analysis
shows how center anisotropy maps into PE stress.

In the corrected framework, the anisotropy at the center (carrying energy
$\langle d_s^2\rangle_\rho\ge12$) evolves into a specific $g_3$ at the PE end.
The question is whether this $g_3$ lies in the non-ASD PE filling space for
some compatible center-normalized $\gamma$.

## 7. Remaining research objects

The corrected formulation identifies two concrete mathematical objects:

### 7A. Non-ASD PE fillings on $\mathbb R\times T^3$

Does there exist a non-ASD, complete, $\operatorname{Ric}=-3g$ metric on
$\mathbb R\times T^3$ with two PE ends?  The Li--Liu source covers one-PE-plus-
one-cusp (ASD, one-ended except for the rigid Ricci-flat case with zero-Yamabe
conformal infinity).  Two-PE-ended metrics with negative-Yamabe conformal
infinity are not excluded by the Witten--Yau / Cai--Galloway / Li--Liu Proposition
6.6.

Such a metric, if it existed, would provide the reflected-center core.

### 7B. Center-PE shear integral

For any reflected core, the accumulated weighted shear satisfies
\[
 \int_0^\infty e^{2r}|S-I|^2\,dr=\frac{-R_\gamma-12}4>0.
 \tag{7.1}
\]
Can this be bounded below in terms of the center data?  Since $|S(0)-I|^2=3$
and $|S'(0)|^2\ge27$:
\[
 \int_0^\infty e^{2r}|S-I|^2\,dr
 \ge\int_0^\varepsilon\bigl(3+(|S'|^2-6)r^2+O(r^3)\bigr)dr
 =3\varepsilon+\frac{|S'(0)|^2-6}{3}\varepsilon^3+O(\varepsilon^4).
 \tag{7.2}
(Note: the linear term in $|S-I|^2=-6r+\cdots$ is cancelled by the $e^{2r}$
expansion, so the integrand is $3+(|S'|^2-6)r^2+O(r^3)$.)
\]
A stronger lower bound from the Riccati equation would further constrain $R_\gamma$.

### 7C. Shear integral upper bound

Conversely, is there a universal upper bound on the shear integral for reflected
Einstein cores on $T^3$?  Such a bound would constrain $R_\gamma$ from below and
limit the conformal infinity geometry.

## 8. Evidence files

- `workspace/scripts/step77_pe_expansion_verify.py` → `workspace/data/step77_pe_expansion.json`
- Corrected `workspace/notes/step76_center_energy_transport_and_scattering.md`
  (twist energy eq.\ 9.5 fixed)
- Step 75 center theorem and note (unchanged, using $-3+3\delta$)
- Primary Li--Liu source:
  `Knowledge/objects/papers/Poincaré-Einstein-4-manifolds-with-cusps--d36d062e94d0--09d8ca1fbe38/object.md`
