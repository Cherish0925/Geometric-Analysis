# TTCS Independent Branch Record

```json
{
  "step_id": 62,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step62_weyl_channel_reduction.md",
    "Sessions/S1003A02/workspace/notes/step48_yamabe_channel_and_localized_CH.md",
    "Sessions/S1003A02/workspace/plans/step61_open_range_global_mechanisms.md"
  ]
}
```

## Task

Research generation on the decisive remaining quantity in the four-manifold Einstein-gap lower-bound problem. Step 62 (file attached) shows that on M=X#kCP2bar (X minimal general type, A=c1^2(X), SW nonzero) the Einstein defect obeys the exact identity P/8pi^2=(k-kappa)+(upsilon-kappa)/3 at the Yamabe representative, with kappa the conformal Weyl deficit (kappa=A/2-(3/8pi^2)int|W+|^2) and upsilon the Yamabe excess, and LeBrun forces upsilon>=kappa+3kappa^2/4A. Hence the open-range lower bound is governed only by how much self-dual Weyl energy kappa per exceptional class a conformal structure can remove while keeping P small. Generate serious, mathematically specific mechanisms (a) to PROVE a bound kappa<=k+beta*p (or kappa_* = A/2-(3/8pi^2)inf int|W+|^2 <= k, or the stronger Gursky-type kappa<=k/2) — e.g. Weyl-energy localization/epsilon-regularity on blow-up necks, conformal capacity of a (-1)-class, harmonic ASD representatives of E_i and Weitzenböck formulas on Lambda^-, twistor or Penrose-type arguments, Bach-flow monotonicity, use of the full 2^k sign family on the Lambda^- side, orientation reversal with Bauer-Furuta; and (b) to REFUTE it by construction: conformal structures removing more than 8pi^2/3 of W+ energy per CP2bar summand at bounded P (ASD gluing à la Taubes/Donaldson-Friedman, large Burns cores, conformally symplectic or LeBrun-equality almost-Kähler metrics, period-violating approximations of the formal common mode). For each, state the precise inequality or construction, its quantifiers, which known objects (Kähler kappa<=0; certified CH cell kappa≈0.056/class, upsilon≈0.212/class; formal common mode kappa≈k) it must accommodate, and the cheapest decisive calculation. Do not invent literature; name precise knowledge requests if needed.

## Output

Write
\[
\mathcal W^\pm(g)=\int_M|W_g^\pm|^2\,d\mu_g,\qquad
p=\frac{P}{8\pi^2}.
\]
The proposed Weyl cap has a useful anti-self-dual equivalent:
\[
\boxed{\quad
\kappa\le k+\beta p
\iff
3\mathcal W^+ +\beta P\ge 4\pi^2(A-2k)
\iff
3\mathcal W^-+\beta P
\ge 4\pi^2(A-9\tau_X)+28\pi^2k .
\quad}\tag{1}
\]
The stronger Gursky-type estimate \(\kappa\le k/2\) is
\[
\boxed{\quad
3\mathcal W^-\ge 4\pi^2(A-9\tau_X)+32\pi^2k .
\quad}\tag{2}
\]
For a ball quotient \(A=9\tau_X\), the constants per exceptional summand are therefore

\[
\begin{array}{c|c}
\text{desired estimate}&\mathcal W^-\text{ required per }\overline{\mathbb{CP}}^{\,2}\\ \hline
\kappa\le k & 28\pi^2/3\\
\kappa\le k/2&32\pi^2/3\\
\text{isolated ASD }\overline{\mathbb{CP}}^{\,2}\text{ core}&12\pi^2.
\end{array}
\]

This is an important numerical reserve: an isolated ASD core carries \(36\pi^2\) in \(3\mathcal W^-\), whereas (1) asks for only \(28\pi^2\). The missing \(8\pi^2\) is exactly the amount that an interface transgression or collective deformation would have to remove to reach the formal common mode.

A second useful calibration is the small-\(h=k/A\) phase diagram. Put
\[
\kappa=k+q\,\frac{k^2}{A}+o(k^2/A),\qquad
p=r\,\frac{k^2}{A}+o(k^2/A).
\]
The identity \(\upsilon=3p-3k+4\kappa\) and LeBrun’s envelope imply
\[
\boxed{\quad r+q\ge\frac14.\quad}\tag{3}
\]
The formal common mode is \((q,r)=(0,\frac14)\). A LeBrun-extremal Einstein endpoint would be \((q,r)=(\frac14,0)\). Thus:

* \(\kappa_*\le k\) is exactly the assertion \(q\le0\);
* \(\kappa\le k+\beta p\) becomes \(q\le\beta r\);
* an extremal family moving along \(q+r=\frac14\) from the formal point toward the Einstein point would successively defeat the pure cap and then every fixed \(\beta\).

The exact first zero of the lower envelope \(L_A(k,\kappa)\) is
\[
\boxed{\quad
\kappa_E(k)=\frac A9\left(2+6\frac{k}{A}-2\sqrt{1-3\frac{k}{A}}\right)
=k+\frac{k^2}{4A}+O(k^3/A^2).
\quad}\tag{4}
\]

These two reformulations suggest the following substantive mechanisms.

---

## 1. Variational bubble decomposition plus a local \((-1)\)-capacity theorem

For \(\beta>0\), consider the scale-invariant quadratic functional
\[
\mathcal J_\beta(g)=3\mathcal W^+(g)+\beta P(g).
\]
Within each conformal class with \(Y<0\), the Yamabe representative minimizes the \(P\)-term because \(\mathcal W^+\) is conformally invariant and
\[
P(g)-P(\widetilde g)=\frac1{12}\left(\int s_g^2-Y[g]^2\right).
\]
Thus (1) is equivalent to the topological lower estimate
\[
\inf_g\mathcal J_\beta(g)\ge4\pi^2(A-2k).\tag{5}
\]

The useful local theorem would be the following.

### Local capacity statement

Let \(C_q\) be a complete or truncated scalar-\(-4\) core carrying intersection lattice \(-I_q\), with a controlled spherical or ACH end and with interface transgressions paired against the exterior piece. Then
\[
\boxed{\quad
3\,\mathcal W^-(C_q)+\beta P(C_q)+\mathfrak T(C_q)
\ge 28\pi^2q ,
\quad}\tag{6}
\]
where \(\mathfrak T\) is the explicit signature/Chern–Gauss–Bonnet transgression. On gluing all pieces, the \(\mathfrak T\)-terms cancel. The residual component carrying the minimal model must contribute
\[
3\mathcal W^-+\beta P\ge4\pi^2(A-9\tau_X).\tag{7}
\]
Equations (6)–(7) sum to (1).

For an exactly product spherical interface, the APS signature formula gives, with the orientation convention fixed,
\[
\mathcal W^-(C_q)-\mathcal W^+(C_q)=12\pi^2q.
\]
Hence an ASD bubble gives \(3\mathcal W^-=36\pi^2q\), leaving an \(8\pi^2q\) reserve relative to (6). The problem is therefore not the isolated bubble. It is whether interface geometry can extract more than \(8\pi^2\) per lattice generator.

A variational proof of (5) can be organized around near-minimizers of \(\mathcal J_\beta\). For \(\beta>0\), the Euler–Lagrange equation should have a fourth-order elliptic principal part modulo diffeomorphism and scale. The required regularity statement has the form
\[
\int_{B_{2r}}\bigl(|W|^2+|\operatorname{Ric}^\circ|^2\bigr)<\varepsilon_0
\Longrightarrow
r^2\sup_{B_r}|{\rm Rm}|+
r^3\sup_{B_r}|\nabla{\rm Rm}|
\le C\left(\int_{B_{2r}}(|W|^2+|\operatorname{Ric}^\circ|^2)\right)^{1/2}.
\tag{8}
\]
A bubble tree then assigns a rank \(q\) sublattice of \(-I_k\) to each concentrated cluster. The geometric task is to prove (6) for every such cluster, including nested clusters and collapsed ends.

This framework accommodates all three calibrations:

* Kähler blow-ups have \(\kappa\le0\), hence sit far above the required anti-self-dual energy.
* The certified CH cell has
  \[
  \mathcal W^-_{\rm cell}\simeq(12-0.150)\pi^2>28\pi^2/3,
  \]
  and \(p\simeq0.9957\), so (6) has ample room.
* The formal common mode has \(\mathcal W^-/k=28\pi^2/3+o(1)\) on a ball quotient; it is the expected equality model for (6) with \(\beta=0\). Consequently, any local theorem with a larger constant would exclude the formal mode rather than explain it.

### Least expensive separating calculation

In the \(U(2)\)-invariant CH-to-bolt ansatz, compute the complete relative ledger
\[
\left(
3\mathcal W^-+\beta P,\;
\mathfrak T_{\rm sig},\;
\mathfrak T_{\rm GB}
\right)
\]
as functions of the bolt parameter and matching radius. The scalar curvature equation reduces the metric to a low-dimensional ODE system. The decisive quantity is
\[
\inf_{\text{regular bolt, fixed CH end}}
\left[3\mathcal W^-+\beta P+\mathfrak T\right].
\]
A value \(28\pi^2\) with the formal mode as a singular endpoint supports (6); a regular value below \(28\pi^2\) gives a direct construction violating the cap. Existing certified-cell machinery is already adapted to this one-dimensional interval computation.

For the ACH version, the precise source request is the APS/renormalized signature and Chern–Gauss–Bonnet formula for four-dimensional ACH metrics with fixed CR infinity, including the Biquard–Herzlich/Burns–Epstein transgression normalizations.

---

## 2. Harmonic exceptional forms and the \(\Lambda^-\) connection

Let \(\eta_i\) be the harmonic representative of \(E_i\), and write \(\eta_i=\eta_i^++\eta_i^-\). Their \(L^2\) Gram matrices obey
\[
G^-_{ij}=\delta_{ij}+G^+_{ij},\qquad G^-\ge I_k,
\tag{9}
\]
because \(E_i\cdot E_j=-\delta_{ij}\). Thus the exceptional lattice carries at least \(k\) units of harmonic anti-self-dual mass for every metric.

For each harmonic ASD form, the Weitzenböck equation at \(s=-4\) is
\[
0=\nabla^*\nabla\eta_i^- -2W^-(\eta_i^-)-\frac43\eta_i^-,
\]
and therefore
\[
2\int W^-(\eta_i^-,\eta_i^-)
=\int|\nabla\eta_i^-|^2-\frac43\int|\eta_i^-|^2.
\tag{10}
\]
Define the endomorphism of \(\Lambda^-\)
\[
\rho=\sum_{i=1}^k\eta_i^-\otimes\eta_i^-,
\qquad
\rho_0=\rho-\frac{\operatorname{tr}\rho}{3}I.
\]
Summing (10) gives the exact identity
\[
2\int\langle W^-,\rho_0\rangle
=\sum_i\|\nabla\eta_i^-\|_2^2-\frac43\sum_i\|\eta_i^-\|_2^2.
\tag{11}
\]

Equation (11) produces a genuine Weyl channel, but it also identifies the central analytic issue. If the forms spread isotropically through \(\Lambda^-\), then \(\rho_0\) can be small. If they concentrate, their \(L^4\) norms can be large and direct Cauchy–Schwarz estimates weaken. A useful theorem must therefore combine (11) with the curvature of the \(\Lambda^-\) connection:

* a nearly isotropic, slowly varying frame of \(\Lambda^-\) is incompatible with scalar curvature \(-4\) unless \(W^-\) or \(\operatorname{Ric}^\circ\) carries energy;
* concentration of the frame creates a bubble carrying a nontrivial sublattice, to which the local capacity estimate (6) applies.

The untwisted connection identity alone is tautological:
\[
\mathcal W^-+\frac1{48}\int s^2
=2\pi^2(2\chi-3\tau)+\frac14P.
\tag{12}
\]
Thus one must use the exceptional harmonic subspace, not merely the Levi-Civita \(\Lambda^-\) connection.

A precise frame estimate sufficient for (1) would be
\[
\boxed{\quad
3\mathcal W^-+\beta P
\ge4\pi^2(A-9\tau_X)+28\pi^2\,\operatorname{rank}\langle E_1,\dots,E_k\rangle .
\quad}\tag{13}
\]
The proof can be split by concentration scales of \(\rho\,d\mu\), with (11) on diffuse regions and (6) on concentrated regions.

Compatibility with the formal mode is restrictive: there \(E_i^+\to0\), so \(G^-\to I_k\), and (13) must approach equality. Hence no estimate based only on \(G^-\ge I_k\) can have a coefficient exceeding \(28\pi^2\). The certified cell should instead give a strict surplus. Computing its harmonic generator \(\eta^-\), the profile of \(\rho_0\), and both sides of (11) would reveal whether the surplus comes from anisotropy, derivative energy, or the core transgression.

### Full sign-family refinement

For each SW solution associated with \(a_\varepsilon\), let \(F_\varepsilon^-\) be the ASD part of its determinant curvature. Since
\[
dF_\varepsilon=0,\qquad
F_\varepsilon^+=q(\Phi_\varepsilon),
\]
one has
\[
d^*F_\varepsilon^-=-d^*F_\varepsilon^+.
\]
Applying the Hodge Weitzenböck formula to \(F_\varepsilon^-\), then averaging over \(\varepsilon\), introduces \(W^-\) while retaining the exact covariance
\[
2^{-k}\sum_\varepsilon \|a_\varepsilon^-\|^2
=|K_X^-|^2+\sum_i|E_i^-|^2
\ge k.
\tag{14}
\]
The terms involving \(d^*F_\varepsilon^+\) can be written through \(\nabla q(\Phi_\varepsilon)\) and compared with the spinor Weitzenböck energy; the mixed curvature term \( \operatorname{Ric}^\circ\!\cdot F^+\) is payable by \(P\) through Young’s inequality.

The least expensive calculation is a complete coefficient-level derivation of this averaged ASD curvature identity. The decisive algebraic point is whether the scalar contribution from (14) survives in the trace-free \(\Lambda^-\) channel or cancels into \(\operatorname{tr}\rho\). Survival with coefficient \(28\pi^2\) would yield (13); complete cancellation would show that the sign family supplies anti-self-dual mass but not anti-self-dual anisotropy.

---

## 3. A Gursky-type estimate on critical metrics

The strong target can be softened to
\[
\mathcal W^+\ge\frac{4\pi^2}{3}(A-k)-cP,
\tag{15}
\]
which is equivalent to
\[
\kappa\le\frac{k}{2}+3c\,p.
\tag{16}
\]
For \(c\) independent of \(A/k\), this still excludes realization of the formal common mode when \(k/A\to0\), since the formal discrepancy from \(k/2\) is order \(k\) whereas \(P\) is order \(k^2/A\).

The natural place for (15) is not the class of all constant-scalar-curvature metrics, but critical points of \(\mathcal J_\beta\) or Bach-flat Yamabe metrics. The ordinary harmonic-Weyl identity
\[
0=\int\left(
|\nabla W^+|^2+\frac{s}{2}|W^+|^2-18\det W^+
\right)
\tag{17}
\]
has the wrong scalar sign at \(s=-4\): the scalar term is \(-2|W^+|^2\). Thus the positive-Yamabe Gursky proof does not transfer by formal substitution. A new term must come either from the SW spinor, from the Euler–Lagrange equation for \(\mathcal J_\beta\), or from the exceptional harmonic frame.

For a Bach-flat Yamabe metric, \(d^\nabla\operatorname{Ric}^\circ\), \(\delta W^\pm\), and \(W(\operatorname{Ric}^\circ,\operatorname{Ric}^\circ)\) are tied by the Bach equation. Pairing that equation with \(\operatorname{Ric}^\circ\) gives a route to
\[
\|\delta W^+\|_2^2+\|\nabla\operatorname{Ric}^\circ\|_2^2
\le C\int |W|\,|\operatorname{Ric}^\circ|^2+C P.
\tag{18}
\]
Combined with the SW curvature estimate and an interpolation inequality, this could produce (15) for critical metrics. Variational compactness would then transfer it to the infimum of \(\mathcal J_\beta\).

The most economical calculation is the exact integrated Bach identity at \(s=-4\), with all coefficients, followed by evaluation on:

* a Kähler metric, where \(\kappa\le0\);
* the certified cell after closing it into a critical approximation;
* the formal common tensor, which should violate (15) at first order unless its missing Bianchi/period equations supply an equally large term.

A related constructive use of Bach flow is also sharp. Since \(\mathcal W^+\) differs from the total Weyl functional by a topological constant, Bach flow decreases \(\mathcal W^+\) by a multiple of \(\int|B|^2\). Starting from a large-core metric and repeatedly passing to its Yamabe representative produces a curve \(t\mapsto(\kappa(t),p(t))\). Convergence to a Bach-flat metric with \(\kappa>k+\beta p\) would produce the opposite result; convergence to a classified critical metric satisfying (15) would support the proof route.

The exact source request is the four-dimensional compactness and bubble-tree theory for critical points of general quadratic curvature functionals
\[
a\int|W|^2+b\int|\operatorname{Ric}^\circ|^2
\]
when the Yamabe constant is below zero, including the hypotheses needed for uniform Sobolev control.

---

## 4. Twistor and orientation-reversal mechanisms

Twistor theory is most effective near the ASD endpoint, not near the fine threshold \(\kappa=k\). A violation slightly above \(k\) still has
\[
\mathcal W^+\sim\frac{4\pi^2}{3}(A-2k),
\]
which is order \(A\) for \(k<A/3\); the twistor almost-complex structure is therefore not close to integrable in an absolute \(L^2\) sense. Twistor methods become decisive if a construction drives \(\kappa\) toward \(A/2\), so that \(\mathcal W^+\to0\).

For such a sequence, the Atiyah–Hitchin–Singer deformation complex and Penrose transform could turn small \(\mathcal W^+\) into an approximate complex twistor space. The required quantitative statement is an \(L^2\)-to-\(C^\alpha\) estimate for the twistor Nijenhuis tensor under the curvature control supplied by a \(\mathcal J_\beta\)-critical sequence. Topological Chern numbers of the twistor space would then constrain the number of \(\overline{\mathbb{CP}}^{\,2}\) summands.

Orientation reversal converts \(\mathcal W^-_M\) to \(\mathcal W^+_{\bar M}\). A Bauer–Furuta route would need stable cohomotopy classes on
\[
\bar M=\bar X\#k\mathbb{CP}^2
\]
strong enough to imply directly
\[
3\mathcal W^+_{\bar M}+\beta P
\ge4\pi^2(A-9\tau_X)+28\pi^2k.
\tag{19}
\]
Ordinary SW estimates on \(\bar M\) still mix scalar and Weyl energy and tend to reproduce the same Yamabe channel rather than (19). The genuinely new ingredient would be a reverse-orientation stable class whose expected dimension or join structure records all \(k\) positive generators.

The first finite calculation is to compute the stable cohomotopy connected-sum class and expected dimensions for \(\bar X\#k\mathbb{CP}^2\), rather than assuming that orientation reversal preserves useful monopole data. The exact source request is the Bauer–Furuta connected-sum theorem under orientation reversal and its behavior for general-type surfaces with \(b^+\ge2\).

---

## 5. Macroscopic Burns/CH cells as a direct construction

Let \(B_R\) be a CH ball in a scalar-\(-4\) ball quotient. Since \(|W^+|^2=2/3\) on the host,
\[
\frac{3}{8\pi^2}\int_{B_R}|W^+_{\rm CH}|^2
=\frac{\operatorname{Vol}(B_R)}{4\pi^2}.
\tag{20}
\]
Replace \(B_R\) by a regular \(\overline{\mathbb{CP}}^{\,2}\)-core and transition annulus. Define its relative Weyl gain and Ricci cost by
\[
c_R=\frac{3}{8\pi^2}
\left[
\int_{B_R}|W^+_{\rm CH}|^2
-\int_{\text{replacement}}|W^+|^2
\right],
\qquad
e_R=\frac1{8\pi^2}
\int_{\text{replacement}}|\operatorname{Ric}^\circ|^2,
\tag{21}
\]
with the common collar contribution written in relative form.

A family of \(k_m\) well-separated replicas in covers \(X_m\), followed by global Yamabe normalization, would have
\[
\kappa(g_m)=k_m c_R+o(k_m),\qquad
p(\widetilde g_m)\le k_m e_R+o(k_m).
\tag{22}
\]
Consequently:

* \(c_R>1\) refutes \(\kappa_*\le k\);
* \(c_R>1+\beta e_R\) refutes the \(\beta\)-susceptibility estimate;
* \(c_R>1/2\) refutes the strong Gursky-type estimate;
* a sequence with \(c_R-1>0\) and \(e_R/(c_R-1)\to0\) defeats every fixed \(\beta\).

A perfectly ASD replacement with negligible annulus energy would have \(c_R=\operatorname{Vol}(B_R)/(4\pi^2)\); thus the pure-cap threshold is exactly the radius at which the removed CH volume reaches \(4\pi^2\). The actual problem is whether transition energy prevents this ideal value.

This construction naturally contains the known objects. Small Burns insertions have \(c_R\to0\). The certified cell has \(c_R\simeq0.056\), still far below one. A macroscopic cell approaching \(c_R=1\) would be a localized realization of the formal common mode.

The least expensive calculation is the radial optimization of
\[
3\mathcal W^++\lambda P
\]
among regular Bianchi IX metrics matching the CH metric to second order at radius \(R\). The output should be the Pareto curve \(R\mapsto(c_R,e_R)\), followed by the radial Yamabe solve. A packing construction additionally needs a source family of compact CH surfaces with sufficiently large injectivity radius or a controlled density of disjoint \(R\)-balls; the precise source request is large-injectivity-radius towers or Benjamini–Schramm families of compact complex-hyperbolic surfaces.

---

## 6. Continuation along the LeBrun equality curve

The most direct construction beyond the formal mode is a one-parameter family approaching equality in LeBrun’s mixed estimate:
\[
\upsilon=\upsilon_L(\kappa),\qquad
p=L_A(k,\kappa),\qquad
k\le\kappa\le\kappa_E(k).
\tag{23}
\]
Every \(\kappa>k\) on this curve refutes the pure cap. For a fixed \(\beta\), it refutes \(\kappa\le k+\beta p\) whenever
\[
\kappa-k>\beta L_A(k,\kappa).
\tag{24}
\]
Near \(k/A=0\), this is the segment \(q+r=1/4\) with \(q>\beta r\).

LeBrun equality imposes a special almost-Kähler structure. In the sign-family setting it also drives
\[
\Pi=|K_X^-|^2+\sum_i|E_i^+|^2\to0.
\tag{25}
\]
If \(\omega\) is the resulting self-dual symplectic form, then \(E_i\cdot[\omega]\to0\). Exact vanishing conflicts with the Taubes exceptional-period mechanism, but periods tending to zero are topologically possible through collapsing exceptional spheres. Therefore the construction is a coupled singular perturbation:

1. exceptional symplectic areas tend to zero;
2. the bulk Weyl eigenvalue shifts by order \(h=k/A\);
3. the Ricci cost moves from \(r=1/4\) toward \(r=0\);
4. the LeBrun slack and \(\Pi\) remain \(o(k^2/A)\).

The formal common mode is the endpoint \(q=0\), \(r=1/4\). The Einstein endpoint \(q=1/4\), \(r=0\) would be a compact strictly almost-Kähler Einstein metric of scalar curvature below zero. This connects the Einstein-gap problem to the unresolved part of the Goldberg program.

The cheapest separating calculation is a second-order Lyapunov–Schmidt expansion around the formal mode, retaining the exceptional-period parameter \(t\):
\[
\kappa=k+q(t)\frac{k^2}{A}+o(k^2/A),\quad
p=r(t)\frac{k^2}{A}+o(k^2/A),\quad
\Pi=\pi(t)\frac{k^2}{A}+o(k^2/A).
\tag{26}
\]
The key number is the sign of \(q'(0)\), together with whether \(r'(0)=-q'(0)\) and \(\pi(t)\to0\). A positive \(q'(0)\) produces a route beyond the cap; a forced \(q(t)\le0\) is the sought quantitative Taubes effect.

For rotated conformally symplectic cells, the relevant expansion is
\[
\kappa(\psi)=\kappa(0)+a\psi^2+O(\psi^3),\quad
p(\psi)=p(0)+b\psi^2+O(\psi^3),\quad
\Pi(\psi)=c\psi^2+O(\psi^3).
\tag{27}
\]
A pure frame rotation does not change \(|W^+|^2\), so \(a\) comes entirely from the metric correction and Yamabe solve. Computing \(a,b,c\) is therefore much more informative than period opening alone.

The exact source request is LeBrun’s complete equality analysis for the mixed curvature estimate, including the resulting almost-Kähler PDE and all regularity hypotheses, together with current results on compact strictly almost-Kähler Einstein four-manifolds with scalar curvature below zero.

---

## 7. ASD gluing and exact ASD endpoints

Any conformal ASD metric on \(M\) has
\[
\kappa=\frac A2.
\]
Thus for \(k<A/2\) it immediately refutes \(\kappa_*\le k\), regardless of its Ricci cost. It refutes \(\kappa\le k+\beta p\) whenever
\[
\frac A2-k>\beta p.
\tag{28}
\]
An ASD Einstein metric has \(p=0\) and would defeat every finite-\(\beta\) estimate.

The SW mixed estimate gives a useful compatibility calculation. For an ASD Einstein metric, the identity gives
\[
\upsilon=2A-3k.
\]
LeBrun with \(W^+=0\) requires \(\upsilon\ge5A/4\), hence
\[
\boxed{\quad k\le A/4.\quad}\tag{29}
\]
So the natural search interval for an ASD Einstein counterexample is \(0<k\le A/4\). For \(A/4<k<A/3\), the SW estimate already rules out this particular endpoint, though non-ASD Einstein metrics remain possible.

Taubes’ theorem that sufficiently many blow-ups admit ASD conformal structures becomes decisive only if its blow-up count can enter \(k<A/3\). The deformation-complex index gives a quick numerical reference. With the usual orientation convention,
\[
\operatorname{ind}_{ASD}(X\#k\overline{\mathbb{CP}}^{\,2})
=\frac12(15\chi_X+29\tau_X)-7k.
\tag{30}
\]
For a ball quotient, \(\chi=A/3\), \(\tau=A/9\), so
\[
\operatorname{ind}_{ASD}=\frac{37}{9}A-7k.
\tag{31}
\]
It remains strongly positive throughout \(k<A/3\); the index by itself does not produce the \(A/3\) threshold. What matters is the actual obstruction-space dimension killed by each ASD summand in Taubes or Donaldson–Friedman gluing.

The least expensive literature calculation is to extract an explicit blow-up count from Taubes’ construction in terms of \(\chi,\tau\) or the ASD obstruction dimension, and then evaluate \(k/A\) on covers of a fixed general-type surface. The precise source requests are:

* Taubes’ explicit dependence of the required number of \(\overline{\mathbb{CP}}^{\,2}\) summands on the initial manifold;
* Donaldson–Friedman gluing with obstruction spaces retained quantitatively;
* ASD orbifold constructions whose smooth resolutions are \(X\#k\overline{\mathbb{CP}}^{\,2}\);
* scalar and Ricci-energy estimates after passing an ASD conformal class to its Yamabe representative.

---

## Most discriminating quantities

Across all these mechanisms, four computations separate the possibilities with little redundancy:

1. **Single-core relative capacity**
   \[
   \inf\bigl(3\mathcal W^-+\beta P+\mathfrak T\bigr)
   \quad\text{on a regular CH-asymptotic }(-1)\text{-core}.
   \]
   The decisive constants are \(28\pi^2\) and \(32\pi^2\).

2. **Averaged ASD Weitzenböck identity for the full sign family**, with all trace-free and source terms retained. This determines whether the \(k\) units in (14) genuinely force \(W^-\).

3. **Second-order continuation away from the formal common mode**, producing the pair \((q,r)\). The line \(q+r=1/4\) is fixed by LeBrun; the sign of \(q\) is the remaining topology-sensitive information.

4. **Explicit ASD blow-up counts and Ricci cost after Yamabe normalization**. An ASD Einstein example with \(k\le A/4\) would settle the construction side immediately; an ASD family with \(p/(\frac A2-k)\to0\) would defeat every fixed susceptibility coefficient.

The central geometric distinction is now sharp: isolated \((-1)\)-bubbles naturally carry more than enough ASD Weyl energy, while the formal common mode removes exactly the \(8\pi^2\) reserve per summand through a collective, period-degenerate response. A proof must show that this reserve cannot be fully extracted by smooth cores and interfaces; a construction must exhibit precisely how it is extracted.