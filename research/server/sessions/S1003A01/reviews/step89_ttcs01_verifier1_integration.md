# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 89,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step89_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step89_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematics of the Step-89 note on the O10 endpoint jet stabilizer. Check carefully: (i) Lemma 89.1: that D_A Phi=0 together with zeta_i=<Phi,P_i>=0 forces P=e_2 (x) s^- (x) e_2 (Penrose form), that the endpoint first-jet level set is a single Spin^c(4) orbit of real dim 6 with 1-dim stabilizer acting nontrivially on L=det S^+, and that the numerical script's construction (stabilizer computed as null space of the infinitesimal action, covector index transforming by the commutator [Sigma,gamma]) is correct; (ii) Theorem 89.2: whether 'distance to the orbit tends to zero in measure' really follows from the cited endpoint convergences (A.15)-(A.16) and whether including zero-order curvature data (F_A^+, Ric+g, W^+, the ASD fit K) keeps the stabilizer argument valid; whether the claim that these are exactly the sections with density-free H^1 bounds via (A.12) is correct (note A.12 is a weighted/tail estimate); (iii) Theorem 89.3: whether identifying the surviving coefficient C with the unique charge-5 eigenvector (verified by |sigma|^2=4 rho* m*^3) and the residual Z_5 / minimal L^5 conclusion is sound, and what is genuinely assumed about the second-jet endpoint set; (iv) Section 4: the formula c_2(S^- (x) L)=(9a^2+T_-)/4 with T_-=2chi-3tau using p_1(Lambda^+-)=a^2-4c_2(S^+-), its reduction to 5chi+6tau, and the endpoint lower bound; (v) Corollary 89.4 (no natural first-order K^m sections from (g,omega,nabla omega) for almost-Kahler pairs) including the stabilizer diag(a, abar^2) computation; (vi) Section 6 Wahl isotropy weights at 1/n^2(1,n-1): the representation of the generator on S^+=Lambda^{00}+Lambda^{02}, the twists chi=zeta^{n j}, and the invariant-dimension conclusions in the json, including whether the twisted spin^c lifts are correctly modeled. Report errors with corrected statements, and assess what the result does and does not establish for density-free O10 and for closed Goldberg.

## Integrated Scientific Memo

# Verification memo: Step 89 endpoint stabilizer

**The first-jet orbit and its charged circle stabilizer are correct. The numerical action is implemented correctly. The charge-\(5\) calculation is also correct as a representation calculation.** However, Step 89 overstates several analytic and classification consequences:

- (A.12), described as a weighted/tail estimate, does not give arbitrary first-jet maps density-free \(H^1\) bounds.
- The supplied finite-density argument controls \(\nabla v\), not automatically the local second jet \(\nabla\tau\).
- The residual \(\mathbb Z_5\) conclusion is conditional on a specified one-mode endpoint, not a classification of all second-order endpoints.
- A nearly nonvanishing, uniformly \(H^1\)-bounded section of a rank-two bundle does **not**, even with bounded curvature, force its \(c_2\) density to vanish. Section 4’s proposed rank-two implication is false under those hypotheses.
- The Wahl JSON is correct for its stated character family and convention, but neither classifies all local Spin\(^c\) lifts nor establishes which lifts extend globally.

The referenced complete-proof TeX, including the actual text of (A.12), (A.15), and (A.16), is not supplied. The conclusions below distinguish what follows from the displayed endpoint convergences from what would require inspecting that missing text.

## 1. Lemma 89.1 and `step89_jet_stabilizer.py`

### Penrose form and orbit

The orthogonality condition must mean the **complex Hermitian** condition
\[
\langle\Phi,P_i\rangle=0,
\]
not just its real part. Choose
\[
\Phi=\sqrt{\rho_*}\,e_1,\qquad e_2\perp e_1.
\]
Then \(P_i=\theta_i e_2\), with \(\theta\in T^*_{\mathbb C}\), and the Dirac equation becomes
\[
c(\theta)e_2=0.
\]
Under
\[
T^*_{\mathbb C}\cong S^+_0\otimes S^-_0,\qquad
c(x\otimes s^-)\psi=\varepsilon(x,\psi)s^-,
\]
the kernel is \(\mathbb C e_2\otimes S^-_0\). Consequently
\[
\boxed{P=(e_2\otimes s^-)\otimes e_2.}
\]
This notation uses a local spin representative; it does not assert an untwisted global tensor identity between Spin\(^c\) bundles.

The sphere of \(\Phi\)’s has real dimension three. For fixed \(\Phi\), the allowed \(P\)’s of fixed nonzero norm form a sphere in a complex two-dimensional kernel, also of real dimension three. The \(SU(2)_-\) factor acts transitively on the latter sphere. Thus the level set is one Spin\(^c(4)\) orbit of real dimension six.

For a representative with \(s^-=f_1\), its stabilizer is
\[
h_\lambda=
\left[
\operatorname{diag}(\bar\lambda,\lambda),
\operatorname{diag}(\bar\lambda^3,\lambda^3),
\lambda
\right].
\]
Indeed, the three factors in \(P=e_2\otimes f_1\otimes e_2\) acquire weights
\[
\lambda,\quad\bar\lambda^3,\quad\lambda^2,
\]
whose product is one. Solving the stabilizer equations also shows there are no additional disconnected components.

Since \(h_{-\lambda}=h_\lambda\) in Spin\(^c(4)\), the effective circle parameter is
\[
\mu=\lambda^2.
\]
It acts on \(L=\det S^+\) by \(\mu\). Thus “weight \(2\)” is correct relative to the double-cover parameter \(\lambda\); relative to the effective circle, \(L\) has weight one.

The Clifford normalization in the script gives
\[
|\tau|^2=2|\Phi|^4|P|^2
=2\left(\frac43\right)^2\frac49
=\boxed{\frac{128}{81}}.
\]
The factor two depends on the tensor/Clifford norm normalization and is correctly fixed by the explicit model.

### Numerical action

The construction in `step89_jet_stabilizer.py` is mathematically consistent:

1. The gamma matrices satisfy the displayed positive Euclidean Clifford relation.
2. The spin generators are
   \[
   \Sigma_{ab}=\tfrac14[\gamma_a,\gamma_b].
   \]
3. The vector representation is extracted from
   \[
   [\Sigma,\gamma_r]=\sum_s M_{sr}\gamma_s.
   \]
4. The covector representation is \(-M^T=M\), because \(M\) is skew-symmetric. Hence the script’s term
   \[
   (\delta P)_s=(\Sigma_++it)P_s+\sum_iM_{si}P_i
   \]
   has the **correct sign**.
5. Realifying the infinitesimal action before computing its null space correctly restricts the Lie-algebra coefficients to real values.
6. On \(E=S^-\otimes L\), the central weight is three, correctly implemented as \(\Sigma_-+3it\).

The JSON is consistent with these calculations. Its numerical null space establishes the infinitesimal stabilizer at the chosen representative; the Penrose argument, not numerical rank alone, establishes global transitivity.

## 2. Theorem 89.2: valid algebraic obstruction, overstated regularity consequence

### Distance to the orbit in measure

The displayed convergences are sufficient **if they are genuine normalized \(L^p\) or measure convergences of all defining residuals**:
\[
|\Phi_j|^2\to\rho_*,\qquad
\langle\Phi_j,P_{j,i}\rangle\to0,\qquad
|P_j|^2\to4/9,
\]
with \(c(P_j)=0\) exactly.

Here is the missing compactness argument. Put
\[
R(\Phi,P)=
\left(
|\Phi|^2-\rho_*,
\langle\Phi,P\rangle,
c(P),
|P|^2-\tfrac49
\right).
\]
Where the first and last residuals are small, \((\Phi,P)\) lies in a fixed bounded subset of the finite-dimensional representation. For every \(\varepsilon>0\), compactness gives a \(\delta>0\) such that
\[
|R(\Phi,P)|<\delta
\quad\Longrightarrow\quad
\operatorname{dist}((\Phi,P),\mathcal O_*)<\varepsilon.
\]
Otherwise a bounded sequence with residual tending to zero would converge to a point outside \(\mathcal O_*\) satisfying all its defining equations. Therefore
\[
\boxed{\operatorname{dist}((\Phi_j,P_j),\mathcal O_*)\to0
\quad\text{in normalized measure}.}
\]

Compactness of the zero set alone is not sufficient; control of the norms supplies the needed boundedness. Convergence only of averaged energies would not establish this conclusion.

### Equivariant vanishing and curvature inputs

For an equivariant continuous map into \(L^m\), \(m\ne0\),
\[
f(x)=f(h_\lambda x)=\lambda^{2m}f(x)
\]
forces \(f(x)=0\) on \(\mathcal O_*\). Uniform continuity near the compact orbit then gives convergence to zero in measure.

Adding the listed curvature data preserves this argument:

- \(F_A^+\) is an equivariant function of \(\Phi\).
- The endpoint values of \(\operatorname{Ric}+g\) and \(W^+\) are zero.
- The ASD model \(K(\Phi,P)\) is fixed by the stabilizer because it is equivariant.

For the rational formula defining \(K\), its denominator must remain nonzero near the orbit. If the input is actual \(F_A^-\), rather than \(K\), the fit error must also tend to zero in measure. These are sufficient conditions for convergence to the **graph orbit**
\[
\{(x,K(x),F_A^+(x),0,0):x\in\mathcal O_*\}.
\]
An independent surviving curvature component, especially \(W^-\), need not preserve this stabilizer.

### Correction to the \(H^1\) claim

The sentence asserting that these are “exactly” the sections with density-free \(H^1\) bounds is incorrect. Neither arbitrary continuity nor arbitrary polynomial dependence yields an \(H^1\) estimate.

For a differentiable first-jet map,
\[
\nabla f=f_\Phi P+f_P H,\qquad H=\nabla P.
\]
A weighted bound for \(H\) only controls \(f_PH\) when the coefficient \(f_P\) matches that weight. Even unweighted \(P\in L^4\), \(H\in L^2\) would not control arbitrary products \(|P|^kH\). Small relative volume of low-amplitude or tail sets does not by itself eliminate derivative concentration there.

Curvature-dependent maps additionally produce derivatives of curvature, which are not controlled by the first-jet estimate.

**Correct statement:**
> Every continuous equivariant charged first-jet map vanishes on the endpoint orbit. Density-free \(H^1\) estimates hold only for particular constructions whose differential and growth are compatible with the precise weighted/tail estimate.

For the cubic torsion, one has schematically
\[
|\nabla\tau|
\le C\bigl(|\Phi||P|^2+|\Phi|^2|H|\bigr).
\]
Thus its \(H^1\) estimate may follow from matching weighted terms and the monopole amplitude bound. It must be checked against the actual (A.12); the assertion of an unweighted \(H\in L^2\) bound is not justified by the supplied material.

## 3. Theorem 89.3: charge \(5\), conditional \(\mathbb Z_5\), and the resolvent/local-jet distinction

### Exact representation calculation

In units of the effective \(L\)-charge \(\mu\),
\[
T^*_{\mathbb C}:\quad -2,-1,1,2,
\qquad
E=S^-\otimes L:\quad 0,3.
\]
Therefore
\[
T^*_{\mathbb C}\otimes E:
\quad\boxed{-2,-1,1,1,2,2,4,5}.
\]
The charge-\(5\) eigenspace is complex one-dimensional.

At the endpoint representative, the functional
\[
\ell(Q)=\Phi\wedge t(\tau;Q)
\]
takes values in \(L^5\). Equivariance requires
\[
\ell(hQ)=\mu^5\ell(Q),
\]
so it vanishes on all weights other than five. It is nonzero on that line. With \(|Q|^2=2m_*\), the norm calculation gives
\[
\boxed{|\ell(Q)|^2=4\rho_*m_*^3},
\]
as recorded in the JSON.

This verifies the representation and normalization. **Matching a scalar norm alone would not identify \(C\).** The identification also uses the adapted-frame projection equations in `O10_Weak_Bianchi.md`, which leave precisely
\[
C=(\nabla_{\bar Z_2}v)_2
\]
and give
\[
|C|^2\to4m_*,
\qquad
|\nabla v|^2=\tfrac12|C|^2+o_{L^1}(1).
\]
Together, these show that the surviving coefficient is the charge-\(5\) component of \(\nabla v\).

### What the supplied sources actually establish

`O10_Weak_Bianchi.md` proves the one-mode structure for the **resolvent field**
\[
Q=\nabla v.
\]
It does not state that
\[
\nabla v-\nabla\tau\to0.
\]
Consequently its equations (2) and (9) do **not** establish the asserted local endpoint structure for \(Q=\nabla\tau\).

To transfer the conclusion to the local second jet, one needs a derivative comparison in measure, or stronger, together with the appropriate zero-order identification of \(v\) with the first-jet torsion direction. Those comparison statements are not displayed in the supplied sources. The representation computation applies to either field, but their endpoint estimates are not interchangeable.

A correct formulation separates two results:

- **Conditional local result:** if \((\Phi,P,\nabla\tau)\) approaches the specified single charge-\(5\) endpoint, the residual-isotropy conclusion follows.
- **Finite-density analytic result:** the displayed sources establish a single charge-\(5\) mode for \((v,\nabla v)\) in compatible adapted frames, and construct the nonlocal/resolvent-based section \(\Phi\wedge t(v)\).

The sources also explicitly show that deriving this mode and its nonzero modulus uses the finite \(W^-\)-energy budget. It is not an established unrestricted-density endpoint.

### Residual isotropy and uniqueness

Suppose the augmented endpoint is exactly the first-jet orbit plus one nonzero charge-\(5\) component of fixed modulus, with every other component zero. Its stabilizer is
\[
\{\mu:\mu^5=1\}\cong\mathbb Z_5.
\]
Hence a nonzero value in \(L^m\) is possible only when
\[
\boxed{5\mid m}.
\]
The construction \(\ell\) supplies a nonzero \(L^5\) value, so five is the smallest positive permitted exponent for this endpoint.

The uniqueness assertion means
\[
\dim_{\mathbb C}\operatorname{Hom}_{U(1)_*}
(T^*_{\mathbb C}\otimes E,L^5)=1.
\]
It is uniqueness of the **endpoint complex-linear symbol**, not uniqueness of global formulas. Formulas may differ by terms vanishing on the orbit, or depend nonlinearly on the higher variables.

Nor does \(\nabla\tau\) encode the full second jet \(\nabla P\). Additional second-jet components invisible to \(\nabla\tau\) could reduce the stabilizer further. Thus this is not a theorem about every construction using the full second jet.

Finally, the Taub–NUT derivative integrals do not prove that every possible topology-detecting section must have its \(H^1\) estimate controlled “only” by \(W^-\). They demonstrate a critical concentration mechanism for the stated fields. A selected differential identity, cancellation, or nonlocal construction remains logically possible.

## 4. Section 4: correct characteristic numbers; false rank-two transgression implication

Write \(\operatorname{sign}(M)\) for the signature, to avoid confusion with the torsion \(\tau\). Since
\[
c_1(S^-)=a,\qquad
p_1(\Lambda^-)=3\operatorname{sign}(M)-2\chi=-T_-,
\]
the identity
\[
p_1(\Lambda^-)=a^2-4c_2(S^-)
\]
gives
\[
c_2(S^-)=\frac{a^2+T_-}{4}.
\]
For a rank-two bundle \(V\),
\[
c_2(V\otimes L)=c_2(V)+c_1(V)a+a^2.
\]
Therefore
\[
\boxed{c_2(S^-\otimes L)=\frac{9a^2+T_-}{4}.}
\]
If \(a^2=2\chi+3\operatorname{sign}(M)\), this becomes
\[
\boxed{5\chi+6\operatorname{sign}(M)}.
\]

The endpoint lower bound can be derived directly from the curvature identity:
\[
T_-=\frac1{4\pi^2}\int
\left(2|W^-|^2+\frac{s^2}{24}
-\frac{|\operatorname{Ric}^{\circ}|^2}{2}\right)dV.
\]
At \(s=-4\), with \(\operatorname{Ric}+g\to0\) in normalized \(L^2\),
\[
\frac{T_-}{V}\ge\frac1{6\pi^2}-o(1).
\]
Using the supplied endpoint \(a^2/V\to1/(6\pi^2)\) yields
\[
\boxed{\frac{c_2(E)}V\ge\frac5{12\pi^2}-o(1).}
\]

### Why the proposed rank-two inference fails

Section 4 says that a bounded curvature model plus small \(L^2\) error, together with the nearly nonvanishing \(H^1\) section, would force \(c_2(E)/V\to0\). These hypotheses do not suffice.

A counterexample exists on a **fixed** closed four-manifold. Take a complex rank-two bundle over \(S^4\) with \(c_2=1\), a smooth fixed connection, and a fixed smooth metric. A unit section exists on the complement of one point. In a local trivialization near that point, choose its angular behavior to be a degree-one map
\[
S^3\longrightarrow S^3.
\]
Its derivative is \(O(r^{-1})\), so
\[
\int_0^{r_0}|\nabla s|^2r^3\,dr<\infty.
\]
Cut the section smoothly to zero inside radius \(\varepsilon\). The transition costs \(O(\varepsilon^2)\) in Dirichlet energy; the resulting smooth sections satisfy
\[
\sup_\varepsilon\|\nabla s_\varepsilon\|_2<\infty,
\qquad |s_\varepsilon|\to1\text{ strongly in }L^2.
\]
Curvature and Ricci are bounded, with zero curvature-fit error, but \(c_2/V\) stays nonzero.

The obstruction is the degree carried by the normalized section on \(S^3\); rank-two transgression has angular terms absent from the rank-one identity. **The rank-one theorem cannot be generalized in the form asserted.**

The Taub–NUT calculations remain useful evidence for inexpensive point zeros and derivative concentration. But without a local index computation or Chern transgression including boundary terms, \(\int|W^-|^2=8\pi^2\) is not itself a demonstrated local \(c_2(E)\)-charge.

## 5. Corollary 89.4: correct within its local scope

For an almost-Kähler four-dimensional first jet, \(d\omega=0\) restricts the intrinsic torsion to
\[
\alpha\in\Lambda^{0,1}\otimes K^{-1}
\cong\overline{\mathbb C}^2\otimes\det^{-1}
\]
in the note’s coframe convention.

Put a nonzero \(\alpha\) in its first component. The subgroup
\[
h_a=\operatorname{diag}(a,\bar a^2)
\]
fixes it because
\[
\bar a\,(\det h_a)^{-1}
=\bar a\,(\bar a)^{-1}=1.
\]
On \(K=\det\), it acts by
\[
\det h_a=\bar a,
\]
a nontrivial character. Thus every equivariant \(K^m\)-valued function of this first jet vanishes for \(m\ne0\). At \(\alpha=0\), the full \(U(2)\) stabilizer gives the same conclusion.

Accordingly, Corollary 89.4 is correct for pointwise natural constructions from the almost-Kähler first jet. It does not imply that all methods detecting \(c_1(K)\) must construct such a section. Curvature, higher jets, global integrals, gauge theory, and nonlocal operations are outside its scope.

## 6. Wahl isotropy and twisted Spin\(^c\) lifts

### Representation convention

The script uses the **pullback/coframe convention**
\[
dz_1,dz_2:\quad 1,n-1,\qquad
d\bar z_1,d\bar z_2:\quad -1,-(n-1)
\]
modulo \(N=n^2\). In this convention,
\[
S^+=\Lambda^{0,0}\oplus\Lambda^{0,2}
\quad\text{has weights}\quad 0,-n.
\]
This is consistent. Using a forward geometric fiber action instead reverses the relevant characters; the twist label must be reversed consistently too.

Twisting the canonical Spin\(^c\) structure by a line character \(\zeta^k\) gives
\[
S^\pm_k=S^\pm_0\otimes\zeta^k,\qquad
L_k=L_0\otimes\zeta^{2k}.
\]
Thus adding \(k\) to the spinor weights, as the script does, is correct. Adding \(k\) only to the determinant would not model that twist correctly.

For \(k=nj\), the positive-spinor weights are
\[
nj,\quad n(j-1).
\]
They contain an invariant precisely for \(j=0\) or \(j=1\), in the respective components stated in the note. Every cotangent weight is \(\pm1\) modulo \(n\), while both spinor weights are divisible by \(n\). Hence
\[
(T^*_{\mathbb C}\otimes S^+_{nj})^\Gamma=0
\]
for every displayed twist. This proves the JSON conclusions for all \(n\ge2\), not merely \(2\le n\le15\).

### Almost-Kähler entries

The self-dual weights are \(0,n,-n\), so the invariant real subspace is \(\mathbb R\omega_0\). For an orientation-compatible normalized AK form,
\[
\omega(p)=\pm\omega_0.
\]
The covariant derivative has no component along \(\omega(p)\), and no invariant component in the remaining self-dual directions; thus \(\nabla\omega(p)=0\).

For the untwisted torsion bundle
\[
E=\Lambda^{0,1}\otimes\Lambda^{0,2},
\]
the weights are
\[
-(n+1),\quad -(2n-1).
\]
There are no invariant values. Adding cotangent weights gives no invariant first jet for \(n\ge3\). For \(n=2\), both \(E\)-weights are \(-3\), and the two cotangent weights \(-1\) give four invariant combinations modulo four.

Thus the JSON is correct, but its entry \(4\) is **complex dimension four**, or real dimension eight in the full underlying real derivative space. It is an ambient invariant-jet dimension; differential constraints may reduce realizable jets.

### Which lifts are covered

The family \(\zeta^{nj}\) comprises only \(n\) of the \(n^2\) local characters. For a general twist \(\zeta^k\):

- a spinor value is allowed only for \(k\equiv0,n\pmod{n^2}\);
- first derivatives need not vanish—for example \(k=1\) permits the sum \(1+(-1)=0\).

Therefore “every twist” must mean **every twist in the displayed order-\(n\) family**. Identifying this family with the globally admissible or smoothing-extendible Spin\(^c\) structures requires the actual restriction map and its affine base point. The script supplies neither.

The JSON’s torsion entries concern the ordinary AK bundle. For the cubic torsion of a twisted monopole,
\[
E_k=E_0\otimes\zeta^{3k},
\]
so the weights must be shifted by \(3k\). It is not the same representation calculation. In addition, the cubic definition gives \(t_\Phi(p)=0\) whenever \(\nabla\Phi(p)=0\), independently of ambient invariant-space dimensions.

The later claims about absence of a KE orbifold metric or comparison branch depend on propositions not supplied here; they are not consequences of these isotropy calculations.

## 7. Precise consequences for O10 and closed Goldberg

The sound density-free conclusion is an **algebraic first-order obstruction**: at the stated calibrated first-jet endpoint, no continuous local equivariant section of nonzero \(L\)-power can remain nonzero, including the specified curvature graph inputs.

The supplied finite-density sources also establish the nonzero charge-\(5\) coefficient of \(\nabla v\) and the \(L^5\) section used in their rank-one argument. Step 89 does not establish:

- that the same one-mode endpoint holds for \(\nabla\tau\);
- a classification of all full second jets;
- density-free amplitude or phase-gradient control;
- a rank-two replacement for the rank-one lemma;
- exclusion or construction of a closed \(c\)-depleted nut phase;
- an unrestricted density-free O10 gap.

Step 47’s estimate \(\|\nabla N_\tau\|_{2,\mathrm{avg}}\to0\) remains a **conditional candidate input**, not the necessary form of every local argument; Step 47 itself says that downstream implications still require verification. Other higher-jet endpoint structures and nonlocal mechanisms remain possible.

For closed Goldberg, Corollary 89.4 rigorously excludes charged canonical-line sections constructed pointwise from \((g,\omega,\nabla\omega)\) alone. That is a useful structural limitation on one class of proofs—not a solution of the closed Goldberg problem or a classification of all ways to detect canonical topology.