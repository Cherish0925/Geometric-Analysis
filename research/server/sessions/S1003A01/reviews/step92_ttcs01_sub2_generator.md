# TTCS Independent Branch Record

```json
{
  "step_id": 92,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step91_dense_carrier_consistency_and_wahl_cone_withdrawal.md",
    "Sessions/S1003A01/workspace/notes/spirit_step91_global_reduction_and_carrier_scope.md",
    "Sessions/S1003A02/workspace/notes/step102_wahl_orbifold_realization_and_K2_invariance.md",
    "Sessions/S1003A02/workspace/notes/step105_cusp_channel_restored_and_cap_charge_theorem.md",
    "Sessions/S1003A01/workspace/notes/step83_normalized_action_weyl_deficit_and_AKE_degenerations.md",
    "Sessions/S1003A01/workspace/notes/step85_coupled_center_theorem_neck_trace_and_endpoint_reduction.md",
    "Sessions/S1003A01/workspace/notes/step87_csck_calibration_and_nodal_endpoint_rigidity.md"
  ]
}
```

## Task

The active goal is the unrestricted Einstein-gap programme on four-manifolds. Recent work produced three concrete global entrances for Q1 and one for Q4, but several proposed reductions were corrected. Read the supplied route synthesis, the realized Wahl-orbifold theorem, the corrected cap-charge theorem, and the established AKE endpoint results. Develop at most three mathematically serious next routes, each centered on a new implication that would materially advance Q1/Q2/Q4 rather than repackage known integral bounds. In particular compare: (i) a fixed supplied Seiberg–Witten field limit across shrinking Wahl rational-ball fillers, including what class-sensitive Einstein identity could become available after the limit; (ii) entropy/degree rigidity from the realized degree-one map to a compact complex-hyperbolic surface, noting that BCG’s direct sharp theorem is real-hyperbolic while the source may be non-Kähler; (iii) the zero-charge four-class Hopf-collapse cap and whether odd intersection form, w2, spin bordism, eta/Dirac, or F-structure theory can obstruct or construct it; (iv) a closed Goldberg route combining normalized action, no-concentration, and second-order center results. For each proposed route, state a precise theorem target, derive the key equations or topological invariant, identify one cheapest decisive calculation/source theorem, and explain what result would genuinely change the global programme. Do not assume compactness, supplied orbifold character, or exhaustive degeneration alternatives that the files do not prove.

## Output

## Memo: three decisive routes after the Wahl realization, the cap-charge law, and the AKE endpoint reductions

The present material shows that averaged curvature identities no longer decide the hard Q1 sectors. Wahl points preserve the same aggregate \(T_+\) and curvature inequalities as the smooth blowup, and a four-class Hopf cap with charge \(0\) is also invisible to the aggregate inequalities. The remaining decisive information must therefore be class-sensitive, parity-sensitive, or endpoint-rigidity-sensitive. I develop three routes: the supplied Seiberg–Witten limit through Wahl contractions, the zero-charge four-class Hopf cap, and the closed Goldberg route near Kähler–Einstein orbifold endpoints. The entropy/degree route is compared at the end and not developed as a primary route because its currently available sharp input is not yet matched to the non-Kähler orbifold source.

---

## Route 1. A fixed supplied Seiberg–Witten limit across shrinking Wahl rational-ball fillers

### The new implication

The point of this route is not to reprove the LeBrun inequalities on the orbifold, but to extract a **local, character-dependent contribution** from an actually supplied smooth monopole class after the Wahl ball is contracted. The files establish that no orbifold character has yet been identified, and that filler transfer alone supplies inequalities but no actual field. The new theorem target is therefore:

**Theorem target A.**  
Let \(M=X\# k\overline{\mathbb{CP}}^2\), and let \(B_{n,1}\subset M\) be one of the embedded Wahl rational balls from Theorem 102.R. Fix a smooth basic class \(a\) on \(M\), with a chosen sign subsequence, and let \((A_i,\Phi_i)\) be Seiberg–Witten solutions for \(a\) along a sequence of metrics that contracts \(B_{n,1}\) to the Wahl point \(p\). After passing to a subsequence and choosing gauges on the complement \(W\), the monopoles converge to an orbifold monopole \((A_\infty,\Phi_\infty)\) on \(V\). The local \(\Gamma=\mathbb Z_{n^2}\) character of the determinant line at \(p\) is the image of \(a\) under the restriction map to the lens link, modulo the subgroup of twists that extend over the rational ball. If the limiting Einstein metric on \(V\) has \(\operatorname{Ric}=E g\) with \(E<0\), then the Weyl deficit satisfies a refined identity
\[
D(g)
=
\int_V\Bigl(\frac{s^2}{24}-|W^+|^2\Bigr)
\;\ge\;
2\pi^2\Bigl(
|c_1^{\mathrm{orb}}(L)^+|_{\mathrm{eff}}^2
-
T_+^{\mathrm{orb}}(V)
\Bigr),
\]
where
\[
|c_1^{\mathrm{orb}}(L)^+|_{\mathrm{eff}}^2
=
|c_1^{\mathrm{orb}}(L)^+|^2
+
\sum_p \delta_p(a).
\]
The numbers \(\delta_p(a)\) are local monopole-energy defects determined by the actual orbifold character of \(a\) at \(p\). In the smooth blowup normalization, if the supplied class has smooth self-dual square \(A+k_{\mathrm{block}}\) on the relevant block, the target inequality becomes
\[
D(g)
\;\ge\;
4\pi^2 k_{\mathrm{block}}
+
2\pi^2\sum_p \delta_p(a).
\]
If \(\delta_p(a)>0\) for the actual characters, Wahl points become visible to the Einstein-gap lower bound. If \(\delta_p(a)=0\) for all actual characters, then this route explains precisely why the Wahl sector remains aggregate-blind and forces the programme to rely on non-averaged geometric or derivative information.

### Key equations and mechanism

The Seiberg–Witten equations are
\[
D_A\Phi=0,
\qquad
F_A^+=\sigma(\Phi),
\qquad
|\sigma(\Phi)|^2=\frac{1}{8}|\Phi|^4.
\]
The Weitzenböck formula is
\[
D_A^*D_A\Phi
=
\nabla_A^*\nabla_A\Phi
+
\frac{s}{4}\Phi
+
\frac12 F_A^+\cdot \Phi.
\]
For an Einstein limit with \(s=4E<0\), integration gives the standard square-completion route to LeBrun’s scalar estimate. The new ingredient is that the determinant line on the orbifold is not determined only by its rational Chern class. The local character at the Wahl point enters through the exact sequence for the rational ball \(B\) and its lens link \(L=L(n^2,n-1)\):
\[
0
\to
H^2(B;\mathbb Z)\cong \mathbb Z_n
\to
H^2(L;\mathbb Z)\cong \mathbb Z_{n^2}
\to
H^3(B,L;\mathbb Z)\cong \mathbb Z_n
\to
0.
\]
Relative to a fixed extending spin\(^c\) reference, the possible twists form the subgroup \(n\mathbb Z_{n^2}\subset \mathbb Z_{n^2}\). The actual supplied smooth class \(a\) selects one coset. The spinor value at the orbifold point is allowed only in the invariant subspace
\[
(S^+_{\chi(a)})^\Gamma.
\]
If this invariant subspace is zero, \(\Phi_\infty(p)=0\) to a forced order; if it is nonzero, the spinor may have a nonzero value. Either alternative changes the local monopole energy.

A useful target definition of the local defect is
\[
\delta_p(a)
=
\frac{1}{8\pi^2}
\inf
\int_{U_p/\Gamma} |F_A^+|^2,
\]
where the infimum is taken over orbifold connections compatible with the prescribed link character \(\chi(a)\) and with the limiting monopole spinor behavior. Equivalently, \(\delta_p(a)\) may be read from the character-dependent local term in Kawasaki’s orbifold index formula for the spin\(^c\) Dirac operator, or from the APS \(\eta\)-contribution on the lens link.

### Cheapest decisive calculation or source theorem

The cheapest decisive step is a finite local calculation, not a global compactness theorem.

1. **Compute the actual character of a supplied basic class.**  
   For the PPS embedding of \(B_{n,1}\) into a \(V_{-4}\) block, write the plumbing matrix for the chain and compute the restriction map
   \[
   H^2(M;\mathbb Z)\to H^2(L(n^2,n-1);\mathbb Z)\cong \mathbb Z_{n^2}
   \]
   by Smith normal form. For a basic class
   \[
   a=K_X\pm E_1\pm\cdots\pm E_k,
   \]
   this gives an explicit residue \(r(a)\in \mathbb Z_{n^2}\), modulo the extending subgroup \(n\mathbb Z_{n^2}\). This replaces the earlier ad hoc character enumeration with the correct affine spin\(^c\) restriction.

2. **Compute the invariant spinor subspace.**  
   For the standard Wahl action \(\frac1{n^2}(1,n-1)\), compute the \(\Gamma\)-weights on \(S^+\) after twisting by \(r(a)\). The output is
   \[
   \dim (S^+_{r(a)})^\Gamma.
   \]
   This decides whether the limiting monopole spinor can be nonzero at \(p\), or must vanish to a specified order.

3. **Compute the local self-dual energy defect.**  
   On the model cone over \(L(n^2,n-1)\), or on the Şuvaina Ricci-flat Kähler ALE filler, compute the minimal \(L^2\) self-dual curvature energy for a unitary connection with link character \(r(a)\). This can be attacked by Fourier/Hodge decomposition on the lens link, or by the Kronheimer/Nakajima ALE instanton energy formulas. The desired output is the number \(\delta_{n}(r(a))\).

The needed source families are: Kawasaki’s orbifold index theorem; APS \(\eta\)-invariants for lens spaces; Kronheimer’s ALE instanton energy and McKay correspondence machinery; and an equivariant removable-singularity or Uhlenbeck compactness theorem for finite-energy Seiberg–Witten fields on orbifold cones.

### What would genuinely change

If the actual characters give \(\delta_p(a)>0\), then the Wahl orbifold alternative acquires a class-sensitive cost. The lower bound for the Weyl deficit improves from
\[
D(g)\ge 4\pi^2 k
\]
to
\[
D(g)\ge 4\pi^2 k + 2\pi^2\sum_p \delta_p(a).
\]
That would turn the Wahl channel from an invisible zero-gap possibility into a quantitatively controlled positive-gap sector for a range of \(A\) and \(k\), and would directly sharpen the optimal tariff in Q1/Q2.

If instead the actual characters give \(\delta_p(a)=0\) and nonzero invariant spinors are allowed, then this route proves that the supplied monopole field does not see the Wahl point beyond the known aggregate transfer. That is still a material advance: it removes the expectation that a simple SW limit will close Q1, and it redirects attention to non-averaged derivative identities, actual Einstein constructions, or the zero-charge cap channel.

---

## Route 2. The zero-charge four-class Hopf-collapse cap

### The new implication

The cap-charge theorem gives a precise law for how removed regions enter the Einstein-gap inequalities. For an exceptional \(S^3\)-Hopf cap carrying \(r\) blowup classes in the admissible chirality, the charge is
\[
c=4-r.
\]
Thus a cap carrying four classes has
\[
c=0.
\]
Such a cap is invisible to the transferred mixed estimate
\[
9k+8\sum_j c_j\le 3A.
\]
This is not a minor loophole: if such caps exist, they can absorb four blowup classes at no aggregate cost and allow the hard range \(0<k<A/3\) to remain open even after all currently proved curvature inequalities.

The theorem target is therefore a parity/F-structure dichotomy:

**Theorem target B.**  
Let
\[
C=\#4\,\overline{\mathbb{CP}}^2\setminus B^4
\]
with link \(S^3\) carrying the Taub-bolt chirality \(e_{\mathrm{out}}=-1\). Exactly one of the following holds:

1. **Obstruction.** There is no sequence of metrics on \(C\) with
   \[
   \int_C |W^+|^2\to0,
   \qquad
   \int_C s^2\to0,
   \qquad
   \int_C |\operatorname{Ric}^\circ|^2\to0,
   \]
   whose end collapses Hopf-wise with the admissible chirality, because the odd intersection lattice and the relative Stiefel–Whitney/Spin/Pin data cannot be carried by energy-free collapsed regions or by finite-energy hyperkähler bubbles.

2. **Construction.** The cap \(C\) admits such a zero-charge degeneration, built from an even hyperkähler bubble, for example of \(D_4\) ALF type, together with an energy-free collapsed sector carrying the odd coset of \(-I_4\) modulo the even sublattice.

Either outcome changes the programme. An obstruction removes the invisible four-class packing and forces positive charge into the collapse channel. A construction supplies an explicit zero-gap carrier for four blowup classes.

### Key topological and geometric invariants

The intersection lattice of the cap is
\[
H_2(C;\mathbb Z)/\mathrm{tors}
\cong
\mathbb Z^4,
\qquad
Q_C=-I_4.
\]
This lattice is odd. A simply connected finite-energy Ricci-flat bubble with \(W^+=0\) is hyperkähler in the orientation relevant to the cap, hence spin and even. Therefore the four odd generators of \(-I_4\) cannot all live in such a bubble. They must be represented either by non-simply-connected Ricci-flat pieces or by energy-free collapsed regions with an F-structure.

The even sublattice
\[
D_4=\{x\in \mathbb Z^4:\sum_i x_i\equiv 0\pmod 2\}
\]
has index \(2\) in \(\mathbb Z^4\). The cap lattice decomposes, informally, as
\[
-I_4 = -D_4 \;\cup\; \text{odd coset}.
\]
The \(D_4\) part has known hyperkähler ALF representatives. The decisive question is whether the odd coset can be carried by an energy-free collapse.

The cap charge identity gives
\[
c(C)=0
\]
for \(r=4\) and \(e_{\mathrm{out}}=-1\). Thus the signature/Euler/\(\eta\) combination that defines \(C_+\) has already been balanced. The remaining issue is parity and the topology of the collapsed sector.

A useful target invariant is a relative Spin/Pin-type invariant of the cap with its \(S^3\) link. For a compact 4-manifold with homology-sphere link, the intersection form together with the characteristic vector determines relative Spin/Pin data. For \(-I_4\), the characteristic vector
\[
w=(1,1,1,1)
\]
satisfies
\[
w^2=-4,
\]
but the lattice still contains odd vectors such as \((1,0,0,0)\). A relative Kirby–Taylor/Stong-type invariant, or equivalently a Pin-bordism class computed from the plumbing data, should distinguish a cap that can be assembled from even hyperkähler bubbles plus flat F-structure regions from one that cannot.

### Cheapest decisive calculation or source theorem

There are two parallel cheap tests.

#### Test B1: relative parity/Pin invariant

Compute the relative Pin or Kirby–Taylor invariant of
\[
C=\#4\,\overline{\mathbb{CP}}^2\setminus B^4
\]
from the diagonal form \(-I_4\) and the \(S^3\) link data. Then compute the same invariant for the known zero-\(W^+\) building blocks:

- hyperkähler ALE spaces of ADE type;
- \(D_m\) ALF spaces, especially the \(D_4\) case;
- flat quotients and torus-collapsed F-structure pieces.

If the invariant of \(C\) is not representable as a sum of the invariants of these allowed zero-energy pieces, the zero-charge cap is obstructed. The relevant source families are Kirby–Taylor invariants, Stong’s Pin bordism calculations, Kronheimer’s ALE classification, Cherkis–Hitchin/Minerbe ALF classification, and Cheeger–Gromov collapse with F-structures.

#### Test B2: circle-action orbit data

A natural way to realize an energy-free collapsed sector is through an \(S^1\) or \(T^2\) action. The Orlik–Raymond/Fintushel classification of smooth circle actions on compact 4-manifolds with \(S^3\) link gives discrete orbit data: fixed-point weights, Euler number, and the intersection form reconstructed from the orbit space. The target calculation is:

- impose link chirality \(e_{\mathrm{out}}=-1\);
- impose intersection form \(-I_4\);
- solve the weight/Euler compatibility equations.

If no solution exists, then the most natural symmetric collapse of the four-class cap is excluded. If a solution exists, it gives a concrete route to constructing the cap, either by cohomogeneity-one Einstein equations or by torus collapse.

### What would genuinely change

If the zero-charge four-class cap is obstructed, then any Hopf-collapse channel must contain caps with \(r<4\), hence positive charge. The inequality
\[
9k+8\sum_j c_j\le 3A
\]
then regains force. In the simplest singleton-cap case one recovers a threshold of the form
\[
k\le \frac{A}{11}
\]
rather than the smooth wall \(k<A/3\). More generally, the packing of exceptional classes into caps becomes quantitatively restricted, giving a positive gap over a much larger part of the hard range, at least under the cap decomposition hypotheses of Theorem 105.Q.

If the cap is constructed, then the programme gains an explicit invisible carrier. Gluing such a cap to a ball-quotient host would give a zero-gap sequence for blocks of four blowup classes, showing that the aggregate curvature laws are genuinely sharp and that Q1 cannot be settled without either a non-averaged derivative estimate or an actual global construction.

---

## Route 3. Closed Goldberg route via normalized action, no-concentration, and the CSCK secant

### The new implication

This route gives a possible complete closure of the strict almost-Kähler Einstein problem near a large class of Kähler–Einstein orbifold endpoints. It uses the established identities
\[
D(g)=T_{\mathrm{AK}}(g)
\]
for almost-Kähler Einstein metrics with self-dual \(\omega\), the local constancy of the normalized Einstein action on Einstein moduli, the no-concentration theorem for almost-Kähler degenerations, and the second-order center obstruction
\[
\operatorname{Ob}_2(H_1,\beta_1)=Q_0(\beta_1).
\]
The Step-87 CSCK calibration replaces the missing derivative estimate with a secant identity:
\[
\Lambda_I(g^{\mathrm{CSCK}})=E\,\zeta_r\,(1+o(1)),
\qquad
P(g^{\mathrm{CSCK}})=E^2\zeta_r^2(1+o(1)),
\]
where \(\zeta_r=\int_\delta \omega\) is the real Kronheimer period of the vanishing cycle.

The theorem target is:

**Theorem target C.**  
Let \(X_0\) be a canonically polarized surface with isolated \(A_1\) singularities, globally \(\mathbb Q\)-Gorenstein smoothable, with unobstructed locally trivial deformations and no holomorphic vector fields. Let \(V\) carry a Kähler–Einstein orbifold metric with \(\operatorname{Ric}=E g\), \(E<0\), and let \(M\) be a smoothing. Then there is a Gromov–Hausdorff neighbourhood \(\mathcal U\) of \(V\) such that every Einstein metric on \(M\) in \(\mathcal U\) is Kähler–Einstein. In particular, no strict almost-Kähler Einstein metric on \(M\) approaches \(V\).

For the one-node quintic this would close the local Goldberg problem near the nodal endpoint. For general \(A_1\) nodes it would supply a template.

### Key equations

At a Kähler–Einstein metric, any self-dual harmonic form can be written as
\[
\omega'=a\omega+\beta,
\qquad
\beta\in \operatorname{Re}H^{2,0}.
\]
Pointwise,
\[
|\omega'|^2=2a^2+|\beta|^2.
\]
Thus constant length forces \(\beta=0\). Moreover,
\[
\|Q_0(\beta)\|_{L^2}\ge c_V\|\beta\|_{L^2}^2,
\qquad
Q_0(\beta)=|\beta|^2-\fint|\beta|^2.
\]
This is the exact length obstruction.

The coupled second-order center theorem gives
\[
\operatorname{Ob}_2(H_1,\beta_1)=Q_0(\beta_1),
\]
with all mixed metric-form terms removable by holomorphic transport. Thus form rotation cannot generate a strict almost-Kähler branch at second order.

Along the Biquard–Rollin CSCK family, the Einstein defect is
\[
\operatorname{Ric}-E g=\rho_0(\cdot,J\cdot),
\]
where \(\rho_0\) is the harmonic anti-self-dual representative of
\[
[\rho_0]=2\pi c_1-E[\omega].
\]
With
\[
\zeta_r=\int_\delta \omega,
\]
one has the exact cohomological identity
\[
\frac{[\rho_0]}{\zeta_r}
=
-\frac{E}{T}\theta
+
\frac{E^2\varepsilon}{2\pi c_1^2}c_1,
\]
where \(T=\theta^2\to -2\) in a controlled nodal limit. The calibrated obstruction is then
\[
\Lambda_I=E\zeta_r(1+o(1)).
\]
The degree argument says: if the corrected CSCK family matches Ozuch’s reduced Einstein-modulo-obstruction parameters with relative displacement strictly less than \(1/2\), then it covers the reduced parameter space. Any Einstein zero must have \(\Lambda_I=0\), hence \(\zeta_r=0\), hence is Kähler–Einstein.

### Cheapest decisive calculation or source theorem

The decisive missing step is the uniform weighted modulation comparison between the CSCK family and one fixed Ozuch reduction. Concretely, one must prove
\[
\lim_{\zeta\to0}
\frac{
\bigl\langle \operatorname{Ric}(g^{\mathrm{CSCK}})-E g^{\mathrm{CSCK}},\,\hat o_I\bigr\rangle
}{
\zeta_r
}
=
E
\]
in Ozuch’s source norm, where \(\hat o_I\) is the \(L^2\)-unit normal obstruction tensor. This includes:

1. putting the CSCK metrics into Ozuch’s Bianchi gauge;
2. controlling the normalized harmonic defect \(\rho_0/\zeta_r\) in the weighted norm \(r_D^{-2}C^\alpha_\beta\);
3. proving uniformity of the Biquard–Rollin construction over all period rays, including the Weyl-related markings needed for both signs of \(\zeta_r\);
4. verifying the spectral complement: the only small TT directions are the exact Kodaira–Spencer kernel and the exact Hermitian eigenmode of eigenvalue \(-2E\).

The needed sources are Ozuch’s reduction and uniform inverse, Biquard–Rollin’s CSCK smoothing construction, and the standard elliptic/spectral gluing theory for orbifold degenerations. The one-node quintic is the right first object because the deformation theory is explicit: \(39\) locally trivial directions plus one smoothing direction, and \(H^{2,0}\neq0\), so the argument does not rely on vanishing holomorphic two-forms.

### What would genuinely change

If Theorem target C is proved, then a whole endpoint class is removed from the strict Goldberg problem. Any strict almost-Kähler Einstein metric must then live away from smoothable, unobstructed \(A_1\) Kähler–Einstein orbifold endpoints. This would convert the Step-83/85/87 machinery into a closed rigidity theorem rather than a conditional reduction.

If the weighted modulation comparison cannot be made uniform, the precise analytic obstruction is identified. That would also be valuable: it would indicate that strict branches, if they exist, are associated with non-smoothable orbifold points, obstructed locally trivial deformations, or endpoints where the CSCK comparison does not cover the reduced Einstein parameter space.

---

## Comparison with the entropy/degree route from the degree-one map \(V\to X\)

The realized Wahl orbifold \(V=V_{X,\mathbf n,k}\) comes with a degree-one map
\[
p:V\to X
\]
to the compact complex-hyperbolic surface \(X\). This gives a topological transfer:
\[
p^*[K_X]^2=A,
\]
and, if \(h\) is the complex-hyperbolic Kähler–Einstein metric on \(X\), the pullback class \(p^*[\omega_X]\) has positive square. A harmonic-map or entropy rigidity theorem could potentially convert this into an Einstein excess proportional to \(k\).

However, the sharp Besson–Courtois–Gallot entropy rigidity theorem is directly formulated for real-hyperbolic targets. The target here is complex-hyperbolic, and any Einstein metric on \(V\) in the Wahl sector would be non-Kähler in the inherited orientation by Proposition 102.K(c). Known complex-hyperbolic rigidity results often require the source to be Kähler, or the map to be holomorphic, or stronger curvature pinching than is presently available for the non-Kähler orbifold source.

Thus the entropy/degree route currently lacks a direct theorem that would produce a new Einstein identity for the Wahl orbifold without additional work. The cheapest decisive source check would be to find or prove a complex-hyperbolic entropy/harmonic-map rigidity theorem for degree-one maps from Einstein orbifolds that are not assumed Kähler. Such a theorem would need to give an excess depending on \(k\), or force the source to be Kähler, thereby contradicting Proposition 102.K(c). Until that input is located, the route mostly repackages the known degree-one topological transfer and does not yet supply a new class-sensitive or parity-sensitive implication. For that reason it is not developed here as one of the three primary routes.