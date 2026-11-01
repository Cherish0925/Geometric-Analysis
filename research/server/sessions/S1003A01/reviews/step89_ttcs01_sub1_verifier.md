# TTCS Independent Branch Record

```json
{
  "step_id": 89,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "failure_kind": "",
  "error": "",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step89_endpoint_jet_stabilizer_and_derivative_ladder.md",
    "Sessions/S1003A01/workspace/scripts/step89_jet_stabilizer.py",
    "Sessions/S1003A01/workspace/data/step89/jet_stabilizer.json",
    "Sessions/S1003A01/workspace/scripts/step89_wahl_isotropy.py",
    "Sessions/S1003A01/workspace/data/step89/wahl_isotropy.json",
    "Skills/geometric-analysis/research/sources/archive/sources/20261001-web-increment/Line1_Web_Increment_20260929_30/research/C/O10_Weak_Bianchi.md",
    "Skills/geometric-analysis/research/sources/archive/sources/20261001-web-increment/Line1_Web_Increment_20260929_30/research/C/O10_All_Finite_Density.md",
    "Sessions/S1003A01/workspace/notes/step47_o10_tn_core_free_at_energy_scale.md"
  ]
}
```

## Task

Verify the mathematics of the Step-89 note on the O10 endpoint jet stabilizer. Check carefully: (i) Lemma 89.1: that D_A Phi=0 together with zeta_i=<Phi,P_i>=0 forces P=e_2 (x) s^- (x) e_2 (Penrose form), that the endpoint first-jet level set is a single Spin^c(4) orbit of real dim 6 with 1-dim stabilizer acting nontrivially on L=det S^+, and that the numerical script's construction (stabilizer computed as null space of the infinitesimal action, covector index transforming by the commutator [Sigma,gamma]) is correct; (ii) Theorem 89.2: whether 'distance to the orbit tends to zero in measure' really follows from the cited endpoint convergences (A.15)-(A.16) and whether including zero-order curvature data (F_A^+, Ric+g, W^+, the ASD fit K) keeps the stabilizer argument valid; whether the claim that these are exactly the sections with density-free H^1 bounds via (A.12) is correct (note A.12 is a weighted/tail estimate); (iii) Theorem 89.3: whether identifying the surviving coefficient C with the unique charge-5 eigenvector (verified by |sigma|^2=4 rho* m*^3) and the residual Z_5 / minimal L^5 conclusion is sound, and what is genuinely assumed about the second-jet endpoint set; (iv) Section 4: the formula c_2(S^- (x) L)=(9a^2+T_-)/4 with T_-=2chi-3tau using p_1(Lambda^+-)=a^2-4c_2(S^+-), its reduction to 5chi+6tau, and the endpoint lower bound; (v) Corollary 89.4 (no natural first-order K^m sections from (g,omega,nabla omega) for almost-Kahler pairs) including the stabilizer diag(a, abar^2) computation; (vi) Section 6 Wahl isotropy weights at 1/n^2(1,n-1): the representation of the generator on S^+=Lambda^{00}+Lambda^{02}, the twists chi=zeta^{n j}, and the invariant-dimension conclusions in the json, including whether the twisted spin^c lifts are correctly modeled. Report errors with corrected statements, and assess what the result does and does not establish for density-free O10 and for closed Goldberg.

## Output

# Scientific verification memo

## Overall assessment

The first-jet isotropy calculation is mathematically correct, and the numerical Clifford computation implements the infinitesimal action with the right signs and bundle weights. The charge-\(5\) representation calculation is also correct for the second variable \(Q=\nabla v\) used in the finite-density O10 argument.

Four corrections are important:

1. The statement that all first-jet constructions covered by the isotropy theorem automatically have density-independent \(H^1\) bounds does not follow from the weighted/tail estimate (A.12).
2. The actual surviving coefficient in `O10_Weak_Bianchi.md` belongs to \(\nabla v\), where \(v\) is the resolvent field, not automatically to \(\nabla\tau\). Replacing \(\nabla v\) by the local second jet \(\nabla\tau\) requires an additional derivative comparison.
3. Uniqueness of the \(L^5\) construction holds for its endpoint linear symbol, not for arbitrary equivariant formulas away from the endpoint orbit.
4. The Wahl computation is correct for the explicitly chosen twists \(\chi^j=\zeta^{nj}\). It does not cover all characters of the local group \(\mathbb Z_{n^2}\) unless a global extension argument identifies precisely this family.

---

## 1. Lemma 89.1 and the Clifford script

### 1.1 Algebraic form of the first jet

Fix
\[
\Phi=\sqrt{\rho_*}\,e_1,\qquad e_2\perp e_1.
\]
Since the spinor inner product is Hermitian,
\[
\langle \Phi,P_i\rangle=0
\]
implies
\[
P_i=\theta_i e_2
\]
for a complex covector \(\theta\in T^*_{\mathbb C}\).

Under the Penrose identification
\[
T^*_{\mathbb C}\simeq S^+_0\otimes S^-_0,
\]
Clifford multiplication has the form
\[
c(x\otimes s^-)\psi=\varepsilon(x,\psi)s^-.
\]
Hence
\[
0=D_A\Phi=\sum_i c(e^i)P_i=c(\theta)e_2
\]
means that the \(S^+_0\)-factor of \(\theta\) lies in \(\ker\varepsilon(\,\cdot\,,e_2)=\mathbb C e_2\). Therefore
\[
\theta=e_2\otimes s^-,\qquad
P=e_2\otimes s^-\otimes e_2.
\]
This part of Lemma 89.1 is correct.

The phase ambiguity \(e_2\mapsto u e_2\), \(s^-\mapsto u^{-2}s^-\) does not change the dimension count. For fixed \(\Phi\), the norm condition on \(P\) gives a three-dimensional real sphere in \(S^-_0\). The sphere of possible \(\Phi\)'s also has real dimension three. Thus the endpoint level set has real dimension six.

### 1.2 Transitivity and stabilizer

The \(SU(2)_-\) factor acts transitively on the unit sphere of \(S^-_0\), while \(\mathrm{Spin}^c(4)\) acts transitively on the fixed-radius sphere in \(S^+\). Thus the six-dimensional level set is one orbit.

For a representative with \(s^-=f_1\), the displayed subgroup
\[
h_\lambda=
[\operatorname{diag}(\bar\lambda,\lambda),
 \operatorname{diag}(\bar\lambda^3,\lambda^3),
 \lambda]
\]
does stabilize the complete jet:

- on \(\Phi=e_1\),
  \[
  \lambda\operatorname{diag}(\bar\lambda,\lambda)e_1=e_1;
  \]
- the tangent \(S^+\)-factor \(e_2\) contributes \(\lambda\);
- \(f_1\in S^-_0\) contributes \(\bar\lambda^3\);
- the output \(S^+\)-spinor \(e_2\) contributes \(\lambda^2\).

Their product is
\[
\lambda\bar\lambda^3\lambda^2=1.
\]
The determinant line transforms by
\[
\det(\lambda A)=\lambda^2.
\]
Consequently the stabilizer acts nontrivially on \(L\).

The group has dimension seven, so a six-dimensional orbit has a one-dimensional stabilizer. The explicit subgroup therefore gives the full connected stabilizer. Because
\[
[A(-\lambda),B(-\lambda),-\lambda]=[A(\lambda),B(\lambda),\lambda]
\]
in \(\mathrm{Spin}^c(4)\), the effective parameter is
\[
\mu=\lambda^2.
\]

The torsion lies in \(E=S^-\otimes L\). Its stabilized component acquires
\[
(\lambda\bar\lambda^3)\lambda^2=1,
\]
so the assertion that \(\tau\) is fixed is also correct.

### 1.3 Norm of the torsion

For the null Penrose tensor above, the Clifford normalization used by the script gives
\[
|\tau|^2=2|\Phi|^4|P|^2.
\]
Therefore
\[
|\tau|^2
=2\left(\frac43\right)^2\frac49
=\frac{128}{81},
\]
matching `jet_stabilizer.json`.

### 1.4 Numerical implementation

The script implements the infinitesimal action correctly.

- `Sig = 0.25*(gamma_a gamma_b-gamma_b gamma_a)` is the standard spin representation for the chosen \(so(4)\) basis.
- The matrices \(M\) are obtained from
  \[
  [\Sigma,\gamma_r]=\sum_s M_{sr}\gamma_s.
  \]
- Since \(M\) is skew-symmetric, the induced infinitesimal action on a covector is
  \[
  -M^T=M.
  \]
  Thus the term
  ```python
  sum(M[s_,i]*PP[i] for i in range(4))
  ```
  has the correct sign.
- The stabilizer matrix is realified before taking its null space, which is necessary because the Lie algebra parameters are real.
- The action on \(Q\in T^*\otimes(S^-\otimes L)\) uses gauge weight \(3\), as it should for \(S^-\otimes L\).

The script verifies the representative and its infinitesimal isotropy. Transitivity of the full endpoint level set comes from the analytic orbit argument above, not from the numerical rank alone.

---

## 2. Theorem 89.2

### 2.1 Convergence of distance to the orbit

Let
\[
R(\Phi,P)=
\left(
|\Phi|^2-\rho_*,
\{\langle\Phi,P_i\rangle\}_{i=1}^4,
\sum_i c(e^i)P_i,
|P|^2-\frac49
\right).
\]
The Dirac component is identically zero, and the remaining components tend to zero in measure provided (A.15)–(A.16) give the stated normalized \(L^p\) convergences.

The implication
\[
R(\Phi_j,P_j)\to0\ \text{in measure}
\quad\Longrightarrow\quad
\operatorname{dist}\big((\Phi_j,P_j),\mathcal O_*\big)\to0
\ \text{in measure}
\]
is valid. Indeed, on the sets where \(|\Phi_j|^2\) and \(|P_j|^2\) are close to their endpoint values, the jets lie in a fixed compact subset of the finite-dimensional representation. If distance from \(\mathcal O_*\) stayed at least \(\varepsilon\) while \(R\to0\), compactness would produce a limit satisfying all endpoint equations but lying outside \(\mathcal O_*\), contradicting Lemma 89.1.

This uses convergence of every defining residual, not merely convergence of their averages.

### 2.2 Equivariant vanishing

If \(x\in\mathcal O_*\) and \(h_\lambda\) belongs to its stabilizer, then for an equivariant map \(f\) into \(L^m\),
\[
f(x)=f(h_\lambda x)=\lambda^{2m}f(x).
\]
For \(m\ne0\), varying \(\lambda\) forces \(f(x)=0\). Continuity and convergence in measure to the orbit then give \(f(\Phi_j,P_j)\to0\) in measure.

### 2.3 Adding curvature variables

The isotropy argument remains valid for the listed endpoint curvature data:

- \(F_A^+=2i\sigma(\Phi)\) is an equivariant function of \(\Phi\);
- the endpoint values of \(\operatorname{Ric}+g\) and \(W^+\) are zero;
- an equivariant model \(K(\Phi,P)\) is fixed by every element stabilizing \((\Phi,P)\), since
  \[
  K(hx)=hK(x)=K(x).
  \]

For the rational expression defining \(K\), continuity is needed only on a neighborhood of the endpoint orbit where its denominator stays away from zero. If the actual anti-self-dual curvature is inserted instead of its model, one additionally needs the fit error to tend to zero in measure.

This extension is algebraic. An \(H^1\) estimate for a section depending on curvature would differentiate the curvature variables and hence require information on \(\nabla\operatorname{Ric}\), \(\nabla W^+\), or \(\nabla F_A\), none of which follows from the first-jet estimate.

### 2.4 The \(H^1\) sentence is too strong

The sentence

> “The sections with density-free \(H^1\) bounds are exactly those whose nonvanishing is excluded here”

does not follow from (A.12).

For a general first-jet map,
\[
\nabla f(\Phi,P)
=f_\Phi(\Phi,P)\,P+f_P(\Phi,P)\,H,
\qquad H=\nabla P.
\]
A weighted/tail estimate for \(H\) does not control the second term for an arbitrary continuous or polynomial \(f\). In particular:

- \(f_P\) may not contain the factor of \(|\Phi|\) needed to match a weighted Hessian term;
- high polynomial degree produces products such as \(|P|^k|H|\), not controlled by \(P\in L^4\) and \(H\in L^2\);
- low-amplitude sets can carry derivative concentration even though their relative volume tends to zero;
- curvature-dependent maps introduce derivatives of curvature.

A correct formulation is:

> The stabilizer theorem applies to every continuous equivariant first-jet map. A density-independent \(H^1\) estimate follows only for those maps whose differential and growth are compatible with the precise weighted and tail terms in (A.12).

The specific cubic torsion may possess this compatibility; arbitrary first-jet maps do not.

---

## 3. Theorem 89.3 and the charge-\(5\) mode

### 3.1 Weight calculation

Under the effective parameter \(\mu=\lambda^2\), the complexified cotangent representation has weights
\[
-2,\,-1,\,1,\,2.
\]
The bundle
\[
E=S^-\otimes L
\]
has weights \(0\) and \(3\): one component is the stabilized torsion direction, while the other transforms by \(\mu^3\).

Therefore
\[
Q\in T^*_{\mathbb C}\otimes E
\]
has weight multiset
\[
\{-2,-1,1,1,2,2,4,5\}.
\]
Thus the set of weights is
\[
\{-2,-1,1,2,4,5\},
\]
and the weight-\(5\) space is one-dimensional. This agrees with `jet_stabilizer.json`.

The map
\[
Q\longmapsto \Phi\wedge t(\tau;Q)
\]
is equivariant into \(L^5\), so it can be nonzero only on the weight-\(5\) line. The script verifies that it is nonzero there and obtains
\[
|\sigma|^2
=4\rho_*m_*^3
=21.0461945289\ldots .
\]
The weight computation plus this nonvanishing identifies the surviving coefficient with the charge-\(5\) direction.

### 3.2 Residual isotropy

Assume the endpoint second data consist of:

- the first-jet orbit \(\mathcal O_*\);
- one nonzero weight-\(5\) component \(c\) of fixed modulus;
- all other \(Q\)-components tending to zero.

The first-jet stabilizer acts by
\[
c\longmapsto\mu^5c.
\]
It acts transitively on the phase circle of \(c\), and the stabilizer of a fixed nonzero \(c\) is
\[
\{\mu:\mu^5=1\}\simeq\mathbb Z_5.
\]
On \(L^m\), this group acts by \(\mu^m\). A nonzero equivariant value can therefore occur only if
\[
5\mid m.
\]
The smallest positive line power allowed by this isotropy is \(L^5\).

This is a necessary representation-theoretic condition. The actual section \(\sigma\) supplies a nonzero \(L^5\) value in the finite-density setting.

### 3.3 Important correction: \(Q=\nabla v\), not automatically \(\nabla\tau\)

Equations (2), (8), and (9) of `O10_Weak_Bianchi.md` concern
\[
C=(\nabla_{\bar Z_2}v)_2,
\]
where \(v\) is the resolvent field. They establish the one-mode endpoint structure for
\[
Q=\nabla v\in T^*\otimes(S^-\otimes L).
\]

The Step-89 note instead introduces \(Q=\nabla\tau\). These are not interchangeable from the supplied material. To formulate Theorem 89.3 as a theorem about the local second jet of \(\Phi\), one needs
\[
\nabla v-\nabla\tau\to0
\]
in a topology strong enough to transfer the component decomposition. No such statement appears in the displayed sources.

Thus the directly supported formulation is:

> The endpoint pair \((v,\nabla v)\) has a unique surviving charge-\(5\) mode.

Because \(v\) is produced by a resolvent, this is an extended, nonlocal jet. The same representation calculation applies to \((\tau,\nabla\tau)\), but the required endpoint convergence for \(\nabla\tau\) remains separate.

### 3.4 Meaning of uniqueness

“One-dimensional weight-\(5\) space” implies uniqueness up to scale of the endpoint linear symbol
\[
Q\mapsto L^5.
\]
It does not imply uniqueness of all global equivariant formulas. Two natural formulas may:

- agree to first order on the endpoint orbit;
- differ by terms vanishing on that orbit;
- depend nonlinearly on \(Q\);
- depend on additional jets or nonlocal fields.

Likewise, the isotropy calculation shows that an endpoint-nonzero local construction must sense the charge-\(5\) phase. It does not prove that every estimate for its derivative must be expressed through the full \(W^-\) energy. The available derivative-interchange estimate does use \(W^-\), and the Taub–NUT calculations show the same critical scaling, but a selected PDE identity could in principle control the phase derivative without estimating every component of \(\nabla Q\).

---

## 4. The rank-two bundle \(E=S^-\otimes L\)

Let \(a=c_1(L)=c_1(S^-)\). Since
\[
p_1(\Lambda^-)=3\operatorname{sign}(M)-2\chi(M)
\]
and
\[
p_1(\Lambda^-)=a^2-4c_2(S^-),
\]
one obtains
\[
c_2(S^-)
=\frac{a^2+2\chi-3\operatorname{sign}(M)}4
=\frac{a^2+T_-}{4},
\qquad
T_-=2\chi-3\operatorname{sign}(M).
\]

For a rank-two bundle \(V\) and a line bundle of first Chern class \(a\),
\[
c_2(V\otimes L)=c_2(V)+c_1(V)a+a^2.
\]
Taking \(V=S^-\) gives
\[
c_2(S^-\otimes L)
=\frac{a^2+T_-}{4}+a^2+a^2
=\boxed{\frac{9a^2+T_-}{4}}.
\]

If
\[
a^2=2\chi+3\operatorname{sign}(M),
\]
then
\[
c_2(E)
=\frac{9(2\chi+3\operatorname{sign})+
        2\chi-3\operatorname{sign}}4
=5\chi+6\operatorname{sign}(M).
\]
All these formulas are correct.

The endpoint density calculation is also correct:
\[
\frac{a^2}{V}\to\frac1{6\pi^2},
\qquad
\frac{T_-}{V}\ge\frac1{6\pi^2}-o(1)
\]
imply
\[
\frac{c_2(E)}V
\ge
\frac14\frac{10}{6\pi^2}-o(1)
=
\frac5{12\pi^2}-o(1).
\]

The topological formula alone does not produce a contradiction. A rank-two analogue of the line transgression theorem would require its own analytic proof. The line theorem in `O10_All_Finite_Density.md` cannot simply be cited for \(E\). Moreover, the connection on \(S^-\) contains \(W^-\), exactly as stated in Section 4.

The Taub–NUT calculations support the geometric picture that zeros of the torsion section can be inexpensive in normalized \(H^1\) while curvature energy concentrates at the nuts. Since the local zero index has not been computed, the phrase that each core “carries the \(c_2\)-charge” should be read as curvature-energy localization rather than an established local Chern-number identity.

---

## 5. Almost-Kähler isotropy and Corollary 89.4

For an almost-Kähler four-manifold, the intrinsic torsion is represented by
\[
\alpha\in\Lambda^{0,1}\otimes K^{-1}
\simeq\overline{\mathbb C}^2\otimes\det^{-1}.
\]
Choose a nonzero torsion vector in the first component. For
\[
h_a=\operatorname{diag}(a,\bar a^2),
\]
the first factor \(\overline{\mathbb C}^2\) contributes \(\bar a\), while
\[
\det h_a=a\bar a^2=\bar a,
\qquad
(\det h_a)^{-1}=a.
\]
Thus
\[
\bar a\cdot a=1,
\]
so \(h_a\) stabilizes \(\alpha\).

On the canonical line \(K=\det\), the same subgroup acts by
\[
\det h_a=\bar a.
\]
Hence it acts on \(K^m\) by \(\bar a^m\), which is nontrivial for \(m\ne0\). Any \(U(2)\)-equivariant value in \(K^m\) must therefore vanish at \(\alpha\ne0\). At \(\alpha=0\), the stabilizer is all of \(U(2)\), and the determinant character again forces vanishing.

Corollary 89.4 is therefore correct for pointwise natural constructions, meaning continuous \(U(2)\)-equivariant functions of the almost-Kähler intrinsic torsion.

It does not address constructions involving:

- \(\nabla\alpha\);
- curvature;
- elliptic projections or other nonlocal operations;
- global gauge-theoretic or integral data.

Consequently, the result explains why a local canonical-line section cannot be obtained from \((g,\omega,\nabla\omega)\) alone. It does not prove that every closed Goldberg argument must use one of the particular identities listed in Step 89.

---

## 6. Wahl isotropy computation

Let
\[
\Gamma=\mathbb Z_{n^2},\qquad
\zeta=e^{2\pi i/n^2},
\]
with generator acting on holomorphic coordinates by weights
\[
(1,n-1).
\]
For the canonical complex Spin\(^c\) structure,
\[
S^+=\Lambda^{0,0}\oplus\Lambda^{0,2}.
\]
The pullback weights are
\[
0,\qquad -(1+n-1)=-n.
\]

For the twist
\[
\chi^j=\zeta^{nj},\qquad 0\le j<n,
\]
the two \(S^+\) weights become
\[
nj,\qquad n(j-1).
\]
Modulo \(n^2\):

- \(nj\equiv0\) only for \(j=0\);
- \(n(j-1)\equiv0\) only for \(j=1\).

Thus the monopole value conclusions in the JSON are correct.

### 6.1 First jet of the monopole

The complexified cotangent weights are
\[
1,\ n-1,\ -1,\ -(n-1).
\]
Each is congruent to \(1\) or \(-1\) modulo \(n\), while both twisted spinor weights are divisible by \(n\). Therefore no sum can be zero modulo \(n^2\). Hence
\[
\bigl(T^*_{\mathbb C}\otimes S^+\otimes\chi^j\bigr)^\Gamma=0
\]
for every displayed \(\chi^j\) and every \(n\ge2\).

### 6.2 Almost-Kähler form

The self-dual form weights are
\[
0,\ n,\ -n,
\]
corresponding to \(\omega_0,\Lambda^{2,0},\Lambda^{0,2}\). Since \(n\not\equiv0\pmod{n^2}\), only the real line \(\mathbb R\omega_0\) is invariant. Thus an invariant unit almost-Kähler form agrees with \(\pm\omega_0\) at the cone point.

Because \(\nabla\omega\) is orthogonal to \(\omega\), it takes values in the real \(\Lambda^{2,0}\oplus\Lambda^{0,2}\) part. Adding any cotangent weight to \(\pm n\) never gives zero modulo \(n^2\) for \(n\ge2\). Hence \(\nabla\omega(p)=0\).

### 6.3 Torsion and its first jet

For
\[
E=\Lambda^{0,1}\otimes\Lambda^{0,2},
\]
the weights are
\[
-(n+1),\qquad -(2n-1).
\]
Neither is zero modulo \(n^2\), so the torsion vanishes at the cone point.

Adding the four cotangent weights gives no invariant component for \(n\ge3\). For \(n=2\),
\[
T^*_{\mathbb C}\text{ has weights }1,1,-1,-1,
\qquad
E\text{ has weights }-3,-3,
\]
and the four combinations \((-1)+(-3)=-4\) are invariant modulo \(4\). The JSON value `4` is therefore correct.

This is complex dimension four, equivalently real dimension eight for the derivative of a complex rank-two torsion section. The note should state which dimension convention is intended.

### 6.4 Which twisted lifts are covered

The script correctly models the family
\[
(\Lambda^{0,*})\otimes\chi^j,
\qquad \chi=\zeta^n,
\]
and twisting a Spin\(^c\) structure by a line character does multiply both spinor bundles by that character.

However, the local orbifold group has all characters \(\zeta^k\), \(0\le k<n^2\). The conclusions are not valid for every such local twist. For example, twisting by \(\zeta^1\) gives an \(S^+\) weight \(1\), which combines with the cotangent weight \(-1\) to produce an invariant first derivative.

Thus the correct wording is:

> The JSON conclusions hold for the \(n\) twists by the order-\(n\) subgroup generated by \(\chi=\zeta^n\).

If these are intended to be exactly the Spin\(^c\) structures extending across the Wahl smoothing or rational homology ball, the identification of the global restriction map with the subgroup \(\langle\zeta^n\rangle\), and the choice of the canonical affine base point, must be supplied separately. The representation script itself does not establish that global identification.

---

## 7. Consequences for the two research directions

### Density-independent O10

The Step-89 work establishes:

- a complete algebraic obstruction to nonzero charged first-jet sections at the calibrated endpoint;
- a unique charge-\(5\) direction in \(T^*\otimes(S^-\otimes L)\);
- residual isotropy \(\mathbb Z_5\) when that mode has fixed nonzero modulus;
- the representation-theoretic minimality of \(L^5\) for this augmented endpoint;
- compatibility of the finite-density section \(\Phi\wedge t(v)\) with that charge.

It does not establish:

- a density-independent \(H^1\) estimate for arbitrary first-jet maps;
- the same one-mode structure for the local field \(\nabla\tau\) without comparing it to \(\nabla v\);
- control of the phase derivative of \(c\);
- exclusion of a \(c\)-depleted nut phase;
- a density-independent Einstein gap.

The strongest supported interpretation is that any local endpoint-nonzero charged construction must use higher-jet information, and the finite-density O10 construction uses the unique charge-\(5\) mode of \(\nabla v\).

### Closed Goldberg

Corollary 89.4 rigorously removes pointwise canonical-line sections built only from the first almost-Kähler jet. It explains the recurring appearance of curvature or \(\nabla\alpha\) in the known local identities. It does not settle the closed Goldberg problem and does not exclude global integral, gauge-theoretic, or nonlocal mechanisms.