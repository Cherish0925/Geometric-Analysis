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

## Verification memo on Step 89

The central representation-theoretic computations in Step 89 are correct in the convention used by the scripts and the O10 corpus. The numerical output matches the stated exact values. Several prose statements should be read with slightly sharper hypotheses; the corrections below are mostly qualifications of classification statements and of the passage from finite-density endpoint structure to density-free arguments.

---

## (i) Lemma 89.1: endpoint first jet, orbit, stabilizer, and script

### Algebraic form of the endpoint jet

At a point, choose a unitary frame \((e_1,e_2)\) of \(S^+\) with  
\[
\Phi=\sqrt{\rho_*}\,e_1,\qquad \rho_*=\frac43 .
\]
The condition
\[
\zeta_i=\langle \Phi,P_i\rangle=0
\]
forces each \(P_i\) to lie in the line \(\mathbb C e_2\). Hence
\[
P=\theta\otimes e_2
\]
for some complex covector \(\theta\in T^*_\mathbb C\).

The Dirac equation \(D_A\Phi=0\) becomes
\[
\sum_i c(e^i)P_i=c(\theta)e_2=0 .
\]
Using the Penrose identification \(T^*_\mathbb C\simeq S^+_0\otimes S^-_0\) and the Clifford rule
\[
c(\alpha\otimes s^-)\psi=\varepsilon(\alpha,\psi)s^-,
\]
the equation \(c(\theta)e_2=0\) forces the \(S^+_0\)-factor of \(\theta\) to be proportional to \(e_2\). Thus
\[
\theta=e_2\otimes s^-,\qquad s^-\in S^-_0,
\]
and therefore, invariantly,
\[
P=(e_2\otimes s^-)\otimes e_2 .
\]
The norm condition \(|P|^2=4/9\) fixes \(|s^-|^2\) in the corresponding convention.

This part of Lemma 89.1 is sound.

### Orbit dimension and stabilizer

The group \(\mathrm{Spin}^c(4)\) has real dimension \(7\). The endpoint jet set \(\mathcal O_*\) is described by
\[
|\Phi|^2=\rho_*,\qquad \langle \Phi,P_i\rangle=0,\qquad D_A\Phi=0,\qquad |P|^2=\frac49 .
\]
The Penrose description shows that a point of \(\mathcal O_*\) is determined by:

1. a unit vector \(\Phi\in S^+\), giving a real \(3\)-sphere modulo the relevant central identification, and  
2. a vector \(s^-\in S^-\) of fixed norm, again a real \(3\)-sphere.

The combined \(\mathrm{Spin}^c(4)\)-action is transitive on this set. The stabilizer of a representative is one-dimensional. Thus
\[
\dim_\mathbb R\mathcal O_*=6,\qquad \dim\operatorname{Stab}=7-6=1.
\]

The note’s explicit stabilizer
\[
U(1)_*=\{[\operatorname{diag}(\bar\lambda,\lambda),\operatorname{diag}(\bar\lambda^3,\lambda^3),\lambda]\}
\]
is compatible with the convention that \([A,B,\lambda]\) acts on \(S^\pm\) by \(\lambda A,\lambda B\) and on \(L=\det S^+\) by \(\lambda^2\). The effective character on \(L\) is therefore weight \(2\).

### Torsion norm

The cubic torsion is
\[
\tau=\sum_i c(e^i)\Phi\,(\Phi\wedge P_i).
\]
With the Clifford normalization used in the script,
\[
|\tau|^2=2\rho_*^2|P|^2
      =2\left(\frac43\right)^2\left(\frac49\right)
      =\frac{128}{81}=m_* .
\]
The factor \(2\) is a Clifford-norm factor coming from the restriction of the Clifford map to the Dirac kernel. If one writes the Penrose formula without specifying the tensor metric normalization, this factor can be missed. The script’s explicit gamma-matrix model fixes the convention and gives
\[
m_{\tau}^2=1.5802469135802462=\frac{128}{81}.
\]

### Script correctness

The script `step89_jet_stabilizer.py` is constructed correctly:

- It builds Euclidean Clifford matrices in chiral form and checks the Clifford relations.
- It constructs the endpoint spinor \(\Phi=\sqrt{\rho_*}(1,0)\) and chooses \(P_i=\theta_i e_2\) with \(\theta\) in the kernel of \(\theta\mapsto c(\theta)e_2\).
- It computes the infinitesimal \(\mathrm{Spin}^c(4)\)-action on \((\Phi,P)\) by realifying the action and taking the null space.
- The covector index is transformed by the vector representation extracted from
  \[
  [\Sigma,\gamma_r]=\sum_s M_{sr}\gamma_s,
  \]
  which is the correct way to model the tangent index.
- The central \(U(1)\) acts on \(S^\pm\) with weight \(1\) and on \(L\) with weight \(2\), and it does not act on the tangent index. This is the correct \(\mathrm{Spin}^c\) convention.
- The second-jet action on \(Q=\nabla\tau\) uses \(S^-\otimes L\) weight \(3\), because \(S^-\) has weight \(1\) and \(L\) has weight \(2\). This is also correct.

The script finds:

\[
\text{orbit dim}=6,\qquad \text{stabilizer dim}=1,\qquad L\text{-weight}=2,
\]
and verifies that \(\tau\) is fixed by the stabilizer.

One qualification: the script verifies these facts at one chosen representative. The statement that the whole level set is a single orbit is supplied by the Penrose transitivity argument, not by the numerical null-space computation alone.

---

## (ii) Theorem 89.2: first-order no-go and convergence to the orbit

### Distance to \(\mathcal O_*\) in measure

The orbit \(\mathcal O_*\) is the common zero set of the continuous invariants
\[
|\Phi|^2-\rho_*,\qquad \zeta_i,\qquad D_A\Phi,\qquad |P|^2-\frac49 .
\]
If the corpus estimates (A.15)–(A.16) give convergence in normalized measure, or in normalized \(L^p\) for some finite \(p\), then
\[
\operatorname{dist}\bigl((\Phi_j,P_j),\mathcal O_*\bigr)\to0
\]
in normalized measure. The argument is the standard compactness one: the relevant jet values are bounded by the converging norms; if the distance from \(\mathcal O_*\) stayed above a fixed \(\varepsilon\) on a set of non-vanishing measure, a subsequence would converge to a point outside \(\mathcal O_*\) while all defining invariants converge to their endpoint values, which is impossible.

This inference is valid provided the cited convergences are pointwise-in-measure or \(L^p\) convergences. If one only had convergence of normalized integrals without tightness or tail control, the distance-in-measure conclusion would require an additional argument. In the finite-density O10 corpus, the convergences are strong enough.

### Including zero-order curvature data

The stabilizer argument remains valid for additional zero-order curvature inputs if their endpoint values are fixed by the same \(U(1)_*\). The examples listed satisfy this:

- \(F_A^+=2i\sigma(\Phi)\) is determined by \(\Phi\), hence fixed.
- \(\operatorname{Ric}+g\to0\) and \(W^+\to0\) are zero at the endpoint.
- The ASD fit \(K=-\frac98\rho^3Q/S\), with \(Q=-iq_-(\tau)\), is built from \(\tau\) and scalar invariants; since \(\tau\) is fixed, \(K\) is fixed.

If one allowed additional curvature data with an independent phase not determined by the first jet, the stabilizer could be smaller and the no-go statement would need to be reformulated. The theorem should be read as applying to natural maps whose extra zero-order arguments converge to \(U(1)_*\)-invariant functions of the endpoint jet.

### Equivariant maps to \(L^m\)

For \(x\in\mathcal O_*\) and \(g\in U(1)_*\), equivariance gives
\[
f(x)=f(gx)=\lambda^{2m}f(x).
\]
Since \(m\neq0\), the character \(\lambda^{2m}\) is nontrivial, so \(f(x)=0\). Continuity then gives \(f(\Phi_j,P_j)\to0\) in measure along endpoint sequences.

This part is correct.

### Density-free \(H^1\) statement

The sentence

> “The sections with density-free \(H^1\) bounds are exactly those whose nonvanishing is excluded here”

should be made more precise.

What is true is:

- The weighted Hessian estimate (A.12) controls \(P=\nabla_A\Phi\) in \(L^4\) and \(H=\nabla_A P\) in \(L^2\) without using \(W^-\). The curvature of \(S^+\) contains \(W^+\), scalar curvature, Ricci off-diagonal terms, and \(F_A\), but not \(W^-\).
- Therefore local polynomial sections built from \((\Phi,P)\), with controlled growth and compatible with the same tail or cutoff procedure used in (A.12), have density-free \(H^1\)-type estimates.
- The no-go theorem shows that every such charged first-order local section vanishes at the endpoint.

What is not proved is a converse classification of all possible density-free \(H^1\) sections. Nonlocal sections, resolvent-based sections, or sections involving curvature components with independent phases are not covered by that “exactly” statement. Also, (A.12) is a weighted/tail estimate, so automatic \(H^1\) control for an arbitrary continuous equivariant map is not implied without growth and cutoff hypotheses.

A corrected formulation is:

> Among local natural first-order sections of nonzero line power built polynomially or with controlled growth from \((\Phi,\nabla\Phi)\), the density-free Hessian estimate applies, but the endpoint stabilizer forces all such charged sections to vanish. This does not classify nonlocal or curvature-compensated constructions.

---

## (iii) Theorem 89.3: second jet, charge 5, and the forced \(L^5\)

### Second-jet weights

The second-jet object is
\[
Q=\nabla\tau\in T^*\otimes E,\qquad E=S^-\otimes L .
\]
As a complex vector space this has dimension \(8\). The script computes the \(U(1)_*\)-weights on \(Q\), measured in units of the \(L\)-charge, as
\[
\{-2,-1,1,2,4,5\}.
\]
This agrees with the statement in the note.

The functional
\[
\sigma(Q)=\Phi\wedge t(\tau;Q)
\]
is checked to be an eigenfunctional of raw weight \(10\), i.e. charge \(5\) relative to \(L\), since \(L\) has raw weight \(2\). The script gives
\[
\frac{\text{eigenvalue}/i}{L\text{-weight}}=4.999999999999995.
\]
The charge-5 eigenspace is one-dimensional.

### Normalization and endpoint value

Taking \(q_{10}\) in the charge-5 eigenspace with
\[
|q_{10}|^2=2m_*,
\]
the script computes
\[
|\sigma(q_{10})|^2=21.046194528963063,
\]
while
\[
4\rho_*m_*^3
=4\cdot\frac43\left(\frac{128}{81}\right)^3
=21.04619452896307.
\]
The ratio is \(0.9999999999999997\). This identifies the algebraic charge-5 direction with the corpus coefficient \(C=(\nabla_{\bar Z_2}v)_2\) and the phase \(c=C/(2\sqrt a)\), for which the finite-density analysis gives \(|c|\to1\).

This identification is sound.

### Residual \(\mathbb Z_5\) and minimal line power

Let \(\mu=\lambda^2\) be the effective character on \(L\). The charge-5 coefficient \(c\) transforms as
\[
c\mapsto \mu^5 c .
\]
If the endpoint second-jet data consist only of \(\mathcal O_*\) together with a nonzero charge-5 phase \(c\), then the stabilizer of a chosen phase is
\[
\mu^5=1,
\]
i.e. \(\mathbb Z_5\). On \(L^m\), this residual group acts by \(\mu^m\). A nonzero invariant value is possible only if \(\mu^m=1\) for every fifth root \(\mu\), hence only if
\[
5\mid m.
\]
Thus \(L^5\) is the first line power capable of detecting the charge-5 endpoint phase through a local natural section.

This argument is correct under the stated endpoint hypothesis.

### What is genuinely assumed

The theorem assumes the calibrated finite-density second-jet structure:

1. the first jet lies in \(\mathcal O_*\);
2. all components of \(\nabla\tau\) of weights \(-2,-1,1,2,4\) tend to zero in measure;
3. the charge-5 component has nonzero constant modulus, with only its phase undetermined;
4. the section under consideration is local and natural, depending pointwise on jets up to order \((\Phi,\nabla\Phi,\nabla\tau)\).

This structure is established in the finite-density O10 setting, where the Euler-density bound controls the required derivatives. It is not established for a general density-free endpoint. In a \(c\)-depleted phase, or in an endpoint where other second-jet weights survive, the residual stabilizer and the minimal detectable line power can be different.

Thus the conclusion

> “\(L^{\otimes5}\) is forced, not chosen”

is correct for local natural sections at the calibrated charge-5 endpoint. It is not a universal statement about all possible density-free endpoint configurations.

---

## (iv) Section 4: characteristic class of \(E=S^-\otimes L\)

### Characteristic-class formula

Let \(a=c_1(L)\). In the Spin\(^c(4)\) convention used by the O10 corpus,
\[
c_1(S^-)=a,
\]
and
\[
p_1(\Lambda^-)=a^2-4c_2(S^-).
\]
The note uses
\[
p_1(\Lambda^+)=2\chi+3\tau,\qquad
p_1(\Lambda^-)=3\tau-2\chi.
\]
With
\[
T_-=2\chi-3\tau,
\]
this means
\[
p_1(\Lambda^-)=-T_- .
\]
Therefore
\[
c_2(S^-)=\frac{a^2-p_1(\Lambda^-)}4
          =\frac{a^2+T_-}{4}.
\]

For \(E=S^-\otimes L\), the rank-two tensor formula gives
\[
c_2(S^-\otimes L)
=c_2(S^-)+c_1(S^-)a+a^2
=c_2(S^-)+2a^2.
\]
Substituting the expression for \(c_2(S^-)\),
\[
c_2(E)=\frac{a^2+T_-}{4}+2a^2
      =\frac{9a^2+T_-}{4}.
\]

This derivation is correct, provided one uses the sign convention
\[
p_1(\Lambda^-)=3\tau-2\chi=-T_- .
\]
If one writes \(p_1(\Lambda^-)=2\chi-3\tau\) instead, the sign of the \(T_-\) term changes. The Step-89 formula is consistent with the \(S^-\) convention used in the corpus and with the almost-Kähler check below.

### Almost-Kähler check

For an almost-Kähler four-manifold with canonical Spin\(^c\) data,
\[
a^2=2\chi+3\tau=T_+.
\]
Then
\[
c_2(E)
=\frac{9(2\chi+3\tau)+(2\chi-3\tau)}4
=5\chi+6\tau.
\]
This matches the Euler class of the almost-Kähler torsion bundle \(\Lambda^{0,1}\otimes\Lambda^{0,2}\) used in Step 58. This is a strong consistency check of the sign convention.

### Endpoint density bound

The note states that at the endpoint
\[
\frac{a^2}{V}\to\frac1{6\pi^2},
\qquad
\frac{T_-}{V}\ge \frac1{6\pi^2}-o(1).
\]
Then
\[
\frac{c_2(E)}VV
=\frac{9a^2/V+T_-/V}{4}
\ge \frac{9/(6\pi^2)+1/(6\pi^2)}4
=\frac{5}{12\pi^2}.
\]
The arithmetic is correct. The lower bound on \(T_-/V\) is an input from the surrounding O10/topological budget, not something proved inside Step 89.

### Rank-two interpretation

The structural point is also correct:

- \(E=S^-\otimes L\) carries the natural section \(\tau\), which is first order in \(\Phi\).
- The estimate \(\nabla\tau\in L^2\) is density-free in the same sense as the first-order Hessian estimate.
- But the curvature of \(E\) contains \(W^-\).
- In a Taub–NUT nut phase, \(\tau\) has isolated zeros at nuts, and the \(c_2(E)\)-type charge is carried by the \(W^-\) energy concentrated at those cores.

Thus a rank-two transgression argument would require either control of the zeros or a curvature model not containing \(W^-\). The note correctly identifies this as the obstruction to a simple density-free rank-two proof.

---

## (v) Corollary 89.4: almost-Kähler first-order no-go

Let \((g,\omega)\) be almost-Kähler. The relevant torsion is
\[
\alpha\in \Lambda^{0,1}\otimes K^{-1}.
\]
At a point where \(\alpha\neq0\), use \(U(2)\) to put \(\alpha\) into the form \((r,0)\). The stabilizer consists of diagonal matrices
\[
\operatorname{diag}(a,\bar a^2),\qquad |a|=1.
\]
Indeed, the first component of \(\alpha\) has weight
\[
\frac{\bar z_1}{z_1z_2},
\]
and for \(z_1=a,\ z_2=\bar a^2\),
\[
\frac{\bar a}{a\bar a^2}=1.
\]
The canonical bundle \(K=\Lambda^{2,0}\) has weight
\[
z_1z_2=a\bar a^2=\bar a,
\]
which is nontrivial. Hence \(K^m\) has weight \(\bar a^m\). A natural \(K^m\)-valued function of \(\alpha\) invariant under the stabilizer must therefore vanish for every \(m\neq0\).

At \(\alpha=0\), the stabilizer is all of \(U(2)\), and again no nonzero charged \(K^m\)-invariant exists. By continuity, every natural first-order section of \(K^m\), \(m\neq0\), built pointwise from \((g,\omega,\nabla\omega)\) without curvature vanishes identically.

This proof is correct.

The consequence for closed Goldberg arguments is also correct: any identity that would produce a charged canonical-line section from only the first jet of \(\omega\) is algebraically obstructed. Curvature terms, such as the \(W^+\)-component \(\eta\), or second-jet expressions, such as \(dd^c\log q\), are unavoidable if one wants to detect \(c_1(K)\).

---

## (vi) Wahl cone-point isotropy

### Weight model

For a Wahl cone point of type
\[
\frac1{n^2}(1,n-1),
\]
the generator \(\zeta=\exp(2\pi i/n^2)\) acts on holomorphic coordinates with weights
\[
w_1=1,\qquad w_2=n-1.
\]
The complexified cotangent weights are
\[
1,\ n-1,\ -1,\ -(n-1).
\]
For the canonical complex-orbifold Spin\(^c\) structure,
\[
S^+=\Lambda^{0,0}\oplus\Lambda^{0,2},
\]
with weights
\[
0,\quad -(w_1+w_2)=-n.
\]
Twisting by \(\chi^j\), where \(\chi=\zeta^n\), adds \(nj\) to the \(S^+\) weights. Thus the twisted \(S^+\) weights are
\[
nj,\qquad n(j-1).
\]
A component is invariant exactly when its exponent is \(0\mod n^2\).

This model is correct for the canonical orbifold Spin\(^c\) structure twisted by determinant-type characters \(\chi^j\).

### Monopole values

The invariant condition
\[
nj\equiv0\mod n^2
\quad\text{or}\quad
n(j-1)\equiv0\mod n^2
\]
gives \(j=0\) or \(j=1\) among \(0\le j\le n-1\). Therefore:

- for \(j=0\), the invariant value lies in \(\Lambda^{0,0}\);
- for \(j=1\), the invariant value lies in \(\Lambda^{0,2}\otimes\chi\);
- for \(n\ge3\) and \(2\le j\le n-1\), the monopole has a forced zero at the cone point.

This agrees with the JSON output.

### First jet of \(\Phi\)

The first jet weights are obtained by adding the cotangent weights
\[
1,\ n-1,\ -1,\ -(n-1)
\]
to the \(S^+\) weights. For \(j=0,1\), none of the resulting weights is \(0\mod n^2\) for any \(n\ge2\). Hence
\[
\nabla\Phi(p)=0
\]
for every twist and every \(n\ge2\). The JSON records `Phi_first_jet=0` in all cases, which is consistent.

### Self-dual two-forms

The complexified self-dual forms split as
\[
\Lambda^+_\mathbb C=\mathbb C\omega_0\oplus \Lambda^{2,0}\oplus\Lambda^{0,2}.
\]
The weights of \(\Lambda^{2,0}\oplus\Lambda^{0,2}\) are \(\pm n\), which are not \(0\mod n^2\) for \(n\ge2\). Hence the invariant part is only
\[
\mathbb R\omega_0.
\]
This gives the statement that any invariant almost-Kähler form at the cone point agrees, up to sign, with the cone complex structure.

### \(\nabla\omega\) in the \(\Lambda^{2,0}\) direction

The weights for the \(\Lambda^{2,0}\)-part of \(\nabla\omega\) are
\[
T^*_\mathbb C\otimes(\Lambda^{2,0}\oplus\Lambda^{0,2}),
\]
i.e. sums of \(\pm n\) with the cotangent weights. None is \(0\mod n^2\). Thus the \(\Lambda^{2,0}\)-part of \(\nabla\omega(p)\) vanishes. The JSON agrees.

### Torsion bundle \(E=\Lambda^{0,1}\otimes\Lambda^{0,2}\)

The weights of \(E\) are
\[
-1-n,\qquad -(n-1)-n=-2n+1.
\]
Neither is \(0\mod n^2\), so the torsion value vanishes at the cone point.

For the first jet, add cotangent weights. For \(n\ge3\), no sum is \(0\mod n^2\), so the first jet also vanishes. For \(n=2\), the JSON gives invariant dimension \(4\). This means that a first jet is allowed at \(n=2\).

One precision: the script counts complex invariant dimensions. Thus the entry
\[
\texttt{torsion\_first\_jet\_TstarE}=4
\]
for \(n=2\) is \(4\) complex dimensions, or \(8\) real dimensions if one counts the underlying real jet of a complex section. The note’s phrase “a 4-dimensional first jet” should be understood as complex-dimensional unless otherwise specified.

### Twisted lifts and possible additional characters

The script twists by \(\chi^j=\zeta^{nj}\), i.e. by characters of order dividing \(n\). These are the natural determinant-character twists. If one allows a more general flat line twist by \(\zeta^k\), the same calculation applies with \(nj\) replaced by \(k\). The monopole value can be nonzero only when
\[
k\equiv0\quad\text{or}\quad k\equiv n\pmod{n^2}.
\]
Thus the twists \(j=0,1\) are exactly the ones relevant for possible nonzero monopole values.

A subtle point: the JSON torsion calculation uses the untwisted form bundle
\[
E=\Lambda^{0,1}\otimes\Lambda^{0,2}.
\]
If one instead considers the cubic torsion bundle associated to a twisted monopole, the bundle acquires an additional character, effectively \(\chi^{3j}\). The value of the torsion still vanishes for all relevant twists, because the congruences remain impossible modulo \(n\). For \(j=0,1\), the first-jet conclusions are unchanged: \(n=2\) allows a first jet, while \(n\ge3\) forces the first jet to vanish. For other twists, extra invariant first jets can occur, but those twists already force \(\Phi(p)=0\), so they do not affect the monopole-torsion conclusion.

Thus the JSON conclusions are correct for the untwisted almost-Kähler torsion bundle, and they remain valid for the relevant twisted monopole torsion bundles after the appropriate character is included.

---

## What Step 89 establishes for density-free O10

Step 89 establishes a precise algebraic structure at the finite-density O10 endpoint:

1. The first-order endpoint jet has a one-dimensional stabilizer acting nontrivially on \(L\).
2. Consequently, every local natural first-order section of nonzero line power built from \((\Phi,\nabla\Phi)\) vanishes at the endpoint.
3. At second order, the only surviving calibrated component is the charge-5 coefficient \(c\).
4. The residual stabilizer is \(\mathbb Z_5\), so \(L^5\) is the minimal line power through which a local natural section can remain nonzero.
5. The section \(\sigma=\Phi\wedge t(v)\) used in the finite-density proof is the unique charge-5 linear functional in the second-jet space.
6. The rank-two bundle \(E=S^-\otimes L\) carries a density-free section \(\tau\), but its curvature sees \(W^-\), and point zeros of \(\tau\) can carry topological charge.

This closes the search for an order-lowered local polynomial line section that would give a density-free rank-one transgression.

It does **not** by itself prove density-free O10. What remains is the analytic and geometric problem identified in Step 47:

- either prove a density-free critical estimate for the charge-5 Nijenhuis phase, for example a normalized \(H^1\)-type estimate of the form
  \[
  \|\nabla N_\tau\|_{2,\mathrm{av}}\to0,
  \]
  along every hypothetical zero-end sequence;
- or construct, or rule out, a closed \(c\)-depleted nut phase in which the charge-5 coefficient is absent and the topological charge is carried by dense Taub–NUT cores.

Step 89 shows that any local density-free route must take one of these forms. It does not supply the estimate, does not treat nonlocal sections, and does not determine the integrability or nonexistence of the \(c\)-depleted macroscopic phase.

---

## What Step 89 establishes for closed Goldberg

For almost-Kähler four-manifolds, Corollary 89.4 gives an algebraic explanation for the repeated appearance of curvature or second-jet terms in Goldberg-type identities. A first-order natural section of \(K^m\), \(m\neq0\), built only from \((g,\omega,\nabla\omega)\), cannot exist. Therefore any closed Goldberg identity that detects \(c_1(K)\) must pass through curvature, such as the \(W^+\)-component \(\eta\), or through second-order torsion expressions, such as \(dd^c\log q\).

This is a genuine structural result. It does not rule out higher-order or curvature-dependent Goldberg identities, and it does not by itself settle the existence or nonexistence of closed Goldberg metrics. It identifies the algebraic reason first-order canonical-line constructions cannot succeed.