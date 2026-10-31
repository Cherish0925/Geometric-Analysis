# TTCS Independent Branch Record

```json
{
  "step_id": 40,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step40_nijenhuis_form_and_pointwise_exhaustion.md",
    "Sessions/S1003A02/workspace/notes/step38_kahler_and_paired_field_scope.md",
    "Skills/geometric-analysis/research/paper/sections/variational_selection_and_global_cost.tex"
  ]
}
```

## Task

Research problem: for M = X # k CPbar^2 (X minimal general type, A=c_1^2(X)), is there c>0 with P(g)=int|Ric^o|^2 >= 8 pi^2 c k for every metric when 0<k<A/3 (LeBrun only gives k - A/3), or can metrics drive P/(8pi^2 k) to 0? The Step-40 note proves: the whole Seiberg-Witten saving equals (1/2) E int rho^2 |nabla n|^2_{W2} (Nijenhuis energy of the monopole almost-complex structures) minus nonnegative terms, equivalently Weyl rise W^+(n,n) > aligned value; and that every POINTWISE combination of the exact field identities is exhausted exactly at LeBrun's threshold (binding at uniform amplitude rho=3/2). The Step-38 note shows the exceptional charge of a sign flip lives in the anti-self-dual relative curvature h^- and that paired zeros unwind through S^3. Propose the strongest concrete mathematical mechanisms (with equations, not slogans) that could supply k-dependence through genuinely global or differential information: e.g. localization of Nijenhuis energy by the fixed 4pi^2 of h^- near a 2-cycle dual to E_i, elliptic/Bochner estimates for the SW almost-complex structure, harmonic-projection J_epsilon terms, the zeta (Lee-form) cost, or integral constraints across the 2^k sign family. For each, state the precise inequality to prove, why it could hold, which test object (certified perpendicular cell with saving 0.43%, Kaehler blow-ups, diffuse-rotation metrics) could falsify it, and its cheapest decisive check. Equally, construct the most plausible counter-mechanism: a family where Nijenhuis rotation at density ~1 over volume ~10 pi^2 (1-c) per class has o(k) Walsh and zeta cost, and say what geometric construction might realize it.

## Output

The central issue is **whether exceptional topology can be carried by nearly Ricci-flat geometry while the monopole structures rotate elsewhere**. The supplied identities separate these two phenomena, but do not yet couple their locations or scales.

Write
\[
\mathcal N=\mathbb E_\epsilon\int_M
 \rho_\epsilon^2|\nabla n_\epsilon|_{\mathcal W_2}^2,
\]
and let \(\mathcal R\) denote the sum of the amplitude, Lee, Weyl-alignment, and Walsh terms subtracted in Theorem N. Then
\[
P=8\pi^2k-\frac12\mathcal N+\mathcal R.                 \tag{1}
\]
A sufficient differential estimate for a positive tariff is
\[
\boxed{\frac12\mathcal N\le \mathcal R+C P,}            \tag{2}
\]
with \(C\) independent of \(X,k\) in the family under consideration. It gives
\[
P\ge \frac{8\pi^2}{1+C}\,k.
\]
Equation (2) becomes substantive only when derived from differential equations, topology of marked regions, or spectral estimates—not from another rearrangement of (1). A universal unit tariff is incompatible with the certified cell; the scientifically relevant target is a finite \(C\), rather than \(C=0\).

There are four particularly concrete ways to attack this coupling.

## 1. Projective-spinor curvature: exceptional charge must appear in Berry curvature when Ricci and Lee costs are small

There is a useful differential identity stronger than the paired Chern–Weil completion.

On the set where \(\Phi_\epsilon\neq0\), put
\[
u_\epsilon=\frac{\Phi_\epsilon}{\sqrt{\rho_\epsilon}},
\qquad
\nabla_{\mathcal A_\epsilon}u_\epsilon
   =i\beta_\epsilon u_\epsilon+v_\epsilon u_\epsilon^\perp.
\]
In a unitary frame beginning with \(u_\epsilon\), the \(11\)-entry of the spinor curvature is
\[
(F_{\nabla_{\mathcal A_\epsilon}})_{11}
   =i\,d\beta_\epsilon-\bar v_\epsilon\wedge v_\epsilon.
\]
Define real two-forms
\[
r(n_\epsilon)=-i\langle u_\epsilon,F_{\nabla^{\rm LC}}u_\epsilon\rangle,
\qquad
B_\epsilon=-i\,\bar v_\epsilon\wedge v_\epsilon .
\]
Because the determinant curvature enters the spinor connection as \(if_\epsilon/2\),
\[
\boxed{\frac12f_\epsilon=d\beta_\epsilon-r(n_\epsilon)-B_\epsilon.}       \tag{3}
\]
The important feature is
\[
|r(n_\epsilon)^-|\le C_4|\operatorname{Ric}^{\circ}|,
\qquad
|B_\epsilon|\le C_4|\nabla n_\epsilon|^2.                 \tag{4}
\]
The anti-self-dual part of the Levi–Civita curvature acting on \(S^+\) is the off-diagonal curvature block determined by \(\operatorname{Ric}^{\circ}\); \(W^-\) does not enter it.

For one flip,
\[
h=\frac{f_\epsilon-f_{\epsilon'}}2
 =d(\beta_\epsilon-\beta_{\epsilon'})
  -[r(n_\epsilon)-r(n_{\epsilon'})]
  -[B_\epsilon-B_{\epsilon'}].                          \tag{5}
\]
Thus, if \(P\) and the Lee terms are small, the fixed class of \(h^-\) must be carried by the difference of the Berry curvatures. This identifies exactly which differential object can couple the exceptional class to monopole rotation.

### A preliminary estimate that should be accessible

Suppose, initially, that all spinors are nowhere zero. Harmonic projection removes \(d\beta_\epsilon\). Applying Walsh decomposition to (3), and using
\[
\sum_{i=1}^k\|(f_{\{i\}})_H^-\|_2^2\ge4\pi^2k,
\]
gives, with dimensional constants,
\[
\boxed{
k\le C\left[
P+\mathbb E_\epsilon\int_M|\nabla n_\epsilon|^4
\right].}                                               \tag{6}
\]
For spinors with zeros, the corresponding formula includes the phase periods around their zero sets. Weighted cutoffs then introduce amplitude and Lee terms. Those terms need explicit treatment; the zero set cannot simply be discarded.

Estimate (6) is useful because it reveals a critical distinction:
\[
\int|\nabla n|^4\sim1,\qquad
\int|\nabla n|^2\sim r^2
\]
for a rotation concentrated in a four-dimensional region of radius \(r\). The exceptional charge can persist while its contribution to the saving tends to zero.

### The genuinely stronger theorem shape

A useful concentration theorem would produce marked defect regions \(U_i\) such that
\[
\mathcal N\!\left(\bigcup_iU_i\right)
 \le C\sum_i r_i^2,
\qquad
\sum_i\int_{U_i}|B_i|^2\asymp k,                         \tag{7}
\]
and an exterior estimate
\[
\boxed{
\frac12\mathcal N\!\left(M\setminus\bigcup_iU_i\right)
 \le \mathcal R\!\left(M\setminus\bigcup_iU_i\right)
       +C P+o(k).}                                      \tag{8}
\]
When \(\sum_i r_i^2=o(k)\), (7)–(8) yield (2).

The conceptual division is precise: Berry curvature identifies the topology-carrying defects; a separate elliptic estimate must price **common rotation outside those defects**.

**Distinguishing objects.** Small Kähler blow-ups should concentrate the charge with vanishing \(\mathcal N\). The perpendicular cell tests whether appreciable saving necessarily extends beyond the charge concentration region. A diffuse common rotation superposed on tiny relative defects would directly test (8), while leaving (6) intact.

**Decisive computation.** The curvature-block formula (4) and identity (3) can be derived in the same Clifford conventions used in Step 40. Numerical field tests require actual monopoles on closed replicas: isolated invariant-cell solutions do not determine the fields selected by the closed geometry.

## 2. Price the common mode through the Einstein deformation operator

The most difficult channel is not relative rotation between signs. It is a common almost-Kähler rotation shared by nearly all signs.

When \(\rho=r>0\) is constant and \(\zeta=0\), the Dirac equation gives
\[
d\psi=0,\qquad
|\nabla n|^2=2(2-r).
\]
Since \(\psi=rn\) is harmonic,
\[
\nabla^*\nabla n=2W^+n+\frac43n,
\]
and therefore
\[
\boxed{W^+(n,n)=\frac43-r.}                              \tag{9}
\]
This is a genuine global almost-Kähler channel, not an algebraic artifact. An estimate pricing it by \(P\) touches the same mathematical territory as the Goldberg problem for Einstein almost-Kähler metrics with \(s<0\).

A tractable version is quantitative rigidity near an Einstein Kähler bulk.

Let \(g_0\) be Einstein with \(\operatorname{Ric}_{g_0}=-g_0\). In transverse-traceless gauge,
\[
D(\operatorname{Ric}^{\circ})_{g_0}[H]
 =\mathcal L_EH
 =\frac12\bigl(\nabla^*\nabla H-2\mathring RH\bigr).
\]
Consequently,
\[
P(g_0+tH)=t^2\|\mathcal L_EH\|_2^2+O(t^3),
\qquad
D^2P_{g_0}[H,H]=2\|\mathcal L_EH\|_2^2.                 \tag{10}
\]
This also explains why a generic descent argument is not automatically available near an Einstein configuration.

### A concrete spectral quantity

For variations preserving a compatible symplectic form to first order, let \(\mathcal T H\) be the linearized Nijenhuis tensor. The informative quotient is
\[
\boxed{
C_{\rm AK}(g_0)
 =\sup_H
 \frac{\|\mathcal T H\|_2^2}
      {\|\mathcal L_EH\|_2^2},}                          \tag{11}
\]
after removing diffeomorphism directions and tangent directions to actual Kähler–Einstein moduli.

A uniform finite value of (11), together with nonlinear elliptic control, would support
\[
\mathcal N_B
 \le C P_B+
 C\left(\mathcal R_{\rm Lee,B}
       +\mathcal R_{\rm amp,B}
       +\mathcal R_{\rm align,B}\right)                 \tag{12}
\]
on a regular bulk \(B\). To reach (2), the coefficients of the remainder terms must permit absorption into the exact coefficients in Theorem N.

Why this might hold is unusually concrete: at a Kähler–Einstein metric the aligned eigendirection of \(W^+\) is simple. Weyl alignment locks the monopole direction to that eigendirection, while the Einstein operator controls the non-Kähler metric perturbation producing torsion. Kähler moduli themselves carry no Nijenhuis energy.

The obstruction is equally concrete. If there are normalized tensors \(H_j\) with
\[
\|\mathcal T H_j\|_2=1,\qquad
\|\mathcal L_EH_j\|_2\longrightarrow0,                  \tag{13}
\]
then large-scale nonintegrable rotation can be generated at very small Ricci cost. Covering families, long regions, and collapsing geometry are the natural places for such modes.

**Distinguishing objects.** Kähler blow-ups have zero numerator. The certified cell measures a finite-amplitude departure from the perturbative regime. Diffuse-rotation metrics should produce either a large value of (11) or a breakdown of the identification with a smooth Einstein bulk.

**Decisive computation.** A spectral calculation of (11) on the complex-hyperbolic model, first for compactly supported modes and then on the relevant covering families, would separate a robust torsion gap from long-wavelength softness. The source families are Einstein deformation theory, Koiso-type Kähler decompositions, and Sekigawa integral identities. The needed information is the coefficient and spectral sign in the torsion sector, not merely an inequality with an unspecified constant.

## 3. Whole marked cores: telescope quotient corrections before assigning an exceptional cost

The supplied AE formula already gives a strong mechanism:
\[
P_N=8\pi^2m+4W_N^++\frac1{12}S_N
\]
for a one-ended whole AE core with \(b_1=0\), \(b_2=m\), and intersection form having signature \(-m\).

Its important extension is to **a complete marked bubble tree**, rather than its terminal ALE pieces. Terminal quotient-ended Ricci-flat pieces may cost zero. Their end corrections must be combined with those of the connecting regions before one interprets the exceptional topology.

For a compact marked region \(U\) with outer three-sphere, write
\[
8\pi^2\chi(U)
 =W_U^++W_U^--\frac12P_U+\frac1{24}S_U+\mathcal B_G,
\]
\[
12\pi^2\tau(U)=W_U^+-W_U^-+\mathcal B_\sigma.
\]
If \(\chi(U)=m+1\), \(\tau(U)=-m\), then
\[
\boxed{
P_U=8\pi^2m+4W_U^++\frac1{12}S_U+\mathcal T_U,
\quad
\mathcal T_U=2\mathcal B_G+2\mathcal B_\sigma-16\pi^2.}   \tag{14}
\]
A Euclidean outer marking gives \(\mathcal T_U\to0\).

### The substantive theorem shape

For selected near-minimizers, the desired geometric alternative is:

* topology carried by shrinking regions admits whole outer markings with
  \[
  \sum_i m_i=k_{\rm core},\qquad
  \sum_i(\mathcal T_{U_i})_-=o(k);
  \]
* topology not carried by those regions lies in a regular part where a torsion/Ricci estimate of the form (12) applies.

Here \((x)_-=\max\{-x,0\}\). The first part yields
\[
\sum_iP_{U_i}\ge8\pi^2k_{\rm core}-o(k).                 \tag{15}
\]
The second part must supply the remaining \(k-k_{\rm core}\) dependence.

This is stronger than assuming that every exceptional class becomes an AE bubble. It permits macroscopic surgery geometry, but requires it to enter the common-mode analysis instead.

There is an important reason not to estimate \(\mathcal T_U\) by \(P_U\) for arbitrary outer cuts. Enlarging \(U\) through an Einstein region changes \(\mathcal T_U\) by the scalar and Weyl characteristic densities, even though that added region has \(P=0\). The useful object is a whole rescaled core with a Euclidean outer marking, or a relative comparison retaining the background curvature terms.

**Distinguishing objects.** Burns recovery gives the microscopic unit cost. Eguchi–Hanson tests the quotient correction: assigning it a unit exceptional cost would contradict its Ricci-flatness. The certified perpendicular cell tests finite-scale exchange; its saving shows that not every competitive metric can be described solely by microscopic AE cores.

**Decisive computation.** The end terms can be telescoped symbolically across a model tree. For the cell, evaluating (14) on a nested family of outer hypersurfaces reveals whether the saving is carried by the inner surgery or by a macroscopic collar. This needs only the metric, not a monopole solution.

## 4. The full sign family: topology gives separation in \(C^0\), whereas Walsh measures separation in \(L^2\)

There is a strong topological statement behind the paired fields.

If two spinors are everywhere nonzero and their directions never become antipodal, the normalized interpolation between their directions defines a homotopy of the associated almost-complex structures. Their determinant classes would then agree. Thus a nontrivial sign flip forces either a spinor zero or an antipodal event.

But the Walsh identity measures
\[
\mathbb E_{\epsilon,\epsilon'}
 \|f_\epsilon^+-f_{\epsilon'}^+\|_2^2
 =2\sum_{I\ne\varnothing}\|f_I^+\|_2^2,                 \tag{16}
\]
not pointwise separation. Codimension-two defects can make these events almost invisible to (16).

The differential information that might bridge the two is a uniform elliptic upgrade. For example, in a regular region with \(\rho,\rho'\ge r_0>0\),
\[
\|\nabla(f_\epsilon^+-f_{\epsilon'}^+)\|_\infty\le L
\]
makes an antipodal point contribute a definite amount
\[
\|f_\epsilon^+-f_{\epsilon'}^+\|_2^2
 \ge c\,r_0^6L^{-4}
\]
under a corresponding volume estimate. A linear-in-\(k\) result additionally requires geometric separation of the independent exceptional events.

A precise relative-polarization target is
\[
\boxed{
\|h_{\epsilon\epsilon'}^+\|_2^2
+\mathcal C_{\epsilon\epsilon'}^{\rm Lee}
+\mathcal C_{\epsilon\epsilon'}^{\rm amp}
+C P
\ge \eta\,4\pi^2 d_H(\epsilon,\epsilon'),}              \tag{17}
\]
where the Lee and amplitude quantities are explicitly specified derivative costs. Averaging over all pairs uses
\[
\mathbb E_{\epsilon,\epsilon'}d_H(\epsilon,\epsilon')=\frac k2
\]
and avoids a loss from \(2^k\) fields.

Equation (17) cannot hold from topology alone. It requires an elliptic estimate preventing the relative defects from becoming arbitrarily thin. Moreover, it prices relative modes, not the common mode of Section 2.

There is also a Fourier issue. Summing nearest-neighbour edge energies gives
\[
\sum_i\mathbb E_\epsilon
 \|f_\epsilon^+-f_{\epsilon^{(i)}}^+\|_2^2
 =4\sum_{I\ne\varnothing}|I|\,\|f_I^+\|_2^2.            \tag{18}
\]
The extra factor \(|I|\) cannot be dropped. An edge estimate of order \(k\) may yield only an order-one unweighted Walsh estimate. All-pairs control such as (17), or a genuine low-degree theorem for the nonlinear sign dependence, is needed.

Finally, the Hodge information has a specific direction. Since
\[
f_\epsilon^+=\psi_\epsilon/\sqrt2,\qquad
|d\psi_\epsilon|^2=2\rho_\epsilon|b_\epsilon|^2,
\]
a positive spectral gap \(\lambda_1\) on the orthogonal complement of harmonic self-dual forms gives
\[
\boxed{
J_\epsilon\le\lambda_1^{-1}\|\zeta_\epsilon\|_2^2.}      \tag{19}
\]
Thus small Lee cost makes the self-dual curvature almost harmonic. It does not eliminate Nijenhuis rotation: a harmonic self-dual form can define a nonintegrable almost-Kähler structure.

**Distinguishing objects.** Shrinking Kähler blow-ups test concentration of relative events. The perpendicular cell tests null exceptional periods. A diffuse common harmonic form with tiny sign-dependent defects tests the separation between (17) and the common-mode estimate.

**Decisive computation.** On a closed example, the informative outputs are the all-pairs quantity in (16), the degree-weighted quantity in (18), \(J_\epsilon\), and the locations of antipodal or amplitude-zero events. Increasing the number of fields without these spatial and Fourier distinctions would add little information.

## 5. A much sharper counter-mechanism: shallow rotation spread over the entire host

The suggested order-one saving density on volume of order \(k\) is plausible at the level of the identities. There is an even more efficient sparse mechanism: amplitude depletion of order \(k/A\) spread over volume of order \(A\).

Consider the formal common-mode state
\[
\rho=r,\qquad \zeta=0,\qquad
W^+n=\left(\frac43-r\right)n,
\]
with the other Weyl eigenvalues equal. Then
\[
|\nabla n|^2=2(2-r),\qquad
|W^+|^2=\frac32\left(\frac43-r\right)^2.
\]
If Walsh and harmonic-projection excesses vanish formally,
\[
r^2V=8\pi^2A.
\]
Substitution into the closed curvature identity gives
\[
\boxed{
\frac{P}{8\pi^2}
 =k-A\,\beta(r),\qquad
\beta(r)=\frac{16}{r}-5-\frac{12}{r^2}.}                 \tag{20}
\]
The saving density is exactly
\[
\boxed{
16r-5r^2-12
 =\frac45-5\left(r-\frac85\right)^2.}                   \tag{21}
\]
Hence:

* \(r=3/2\) gives \(\beta(r)=1/3\), reproducing the LeBrun extremal algebra.
* \(r=8/5\) gives saving density \(4/5\), so saving \(8\pi^2(1-c)k\) requires volume \(10\pi^2(1-c)k\).
* For every \(0<h=k/A<1/3\), equation \(\beta(r)=h\) has a solution on the branch \(3/2<r<2\).

On the sparse branch,
\[
r=2-h+O(h^2).
\]
Consequently,
\[
|\nabla n|^2=2h+O(h^2),\qquad V=2\pi^2A+O(k).
\]
The Nijenhuis contribution is of order \(k\), but the amplitude and Weyl-alignment penalties are only
\[
O(Ah^2)=O(kh)=o(k).                                    \tag{22}
\]
This is the cleanest diffuse route toward \(P/(8\pi^2k)\to0\) permitted by the supplied equations.

It is not yet a metric construction. Two global problems remain.

### The sign structures cannot coincide everywhere

An exactly common, nowhere-zero monopole direction would determine one almost-complex determinant class, not all \(a_\epsilon\). The possible realization is a common diffuse structure away from small defects, with sign-dependent relative rotations inside those defects.

For defects of radius \(r_i\),
\[
\text{self-dual disagreement}=O(r_i^4),\qquad
\text{Lee and Dirichlet contributions}=O(r_i^2)
\]
is dimensionally compatible with a fixed anti-self-dual curvature charge. Thus
\[
\sum_i r_i^2=o(k)
\]
could make Walsh and Lee costs small. The Berry identity explains how the topological distinction would survive.

### Ordinary Burns cores cannot supply a vanishing-\(P\) construction

A Burns core already contributes \(8\pi^2\) per class. Since \(P\) is an integral of a squared tensor, a diffuse exterior cannot cancel that contribution. The topology-carrying pieces themselves must have small \(P\), or the exceptional topology must remain macroscopic rather than becoming whole AE cores.

There is a concrete alternative worth examining: **Ricci-flat Taub-bolt cores with ALF ends**.

The classical Euclidean Taub-bolt metric is
\[
g=F(r)(d\tau+2n\cos\theta\,d\phi)^2
  +F(r)^{-1}dr^2+(r^2-n^2)d\Omega_2^2,
\]
\[
F(r)=\frac{r^2-2mr+n^2}{r^2-n^2},
\qquad
m=\frac54n,\qquad r\ge2n,\qquad \tau\sim\tau+8\pi n.
\]
It is Ricci-flat, its bolt is a two-sphere, and its topology is the disk bundle of Euler number of magnitude one; orientation can be chosen so that the bolt represents a class of square \(-1\). Its end is ALF, not AE. Thus it provides an explicit topology-carrying core with
\[
P_{\rm core}=0
\]
that is not covered by the whole-AE tariff.

The decisive issue is the transition. A Taub-bolt core completed through a Euclidean outer region must recover the AE cost. A potentially different construction retains the collapsed Hopf direction through a long region and joins it to a compatible collapsed or Einstein filling geometry. The required quantitative result is
\[
P_{\rm transition}=o(1)\quad\text{per exceptional class},               \tag{23}
\]
while preserving the smooth topology \(X\#k\overline{\mathbf{CP}}^2\).

Taub-bolt also has self-dual Weyl energy that need not be small in the relevant orientation. Therefore small Walsh and Lee costs alone do not establish the diffuse construction: its Weyl-alignment contribution must be included in the saving balance.

The exact source topics are the topology and regularity of Euclidean Taub-bolt instantons, ALF curvature transgressions, and Einstein Taub-NUT/Taub-bolt fillings with the same conformal infinity. The cheapest decisive calculation is the Ricci energy of a variable-length interpolation from the ALF end, including its outer characteristic corrections. A positive asymptotic transition cost restores the tariff mechanism; decay as in (23) makes the collapsed route materially stronger.

---

The most informative scientific comparison is therefore between two complete mechanisms:

\[
\text{Berry-charge concentration}
+\text{whole-core accounting}
+\text{bulk Einstein coercivity}
\quad\Longrightarrow\quad P\gtrsim k,
\]
versus
\[
\text{low-cost non-AE topology carriers}
+\text{common diffuse almost-Kähler rotation}
+\text{small relative-field costs}
\quad\Longrightarrow\quad P=o(k).
\]

The fixed \(4\pi^2\) in \(h^-\) alone does not choose between them. The deciding information is the geometry of the outer marking of the topology-carrying region and the spectral cost of common nonintegrable rotation.