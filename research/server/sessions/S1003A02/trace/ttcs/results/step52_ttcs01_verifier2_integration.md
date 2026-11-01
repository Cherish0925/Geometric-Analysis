# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 52,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step52_ttcs01_sub5_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step52_ttcs01_sub6_verifier.md"
    }
  ]
}
```

## Exact Task

Verify Section 3 of the Step-52 note ('Kronheimer absorption of exceptional classes') and Proposition 52.10. Check: (a) Lemma 52.6 lattice facts (which ADE lattices or sums admit integral odd overlattices containing norm -1 vectors; A1+A1 in Z^2, A3=D3 in Z^3, D_n in Z^n; A8's index-3 overlattice is E8; the claim that k=1 cannot be absorbed), and whether 'E in R⊗Q' is the right notion given that links are rational homology spheres; (b) Theorem 52.7(a): S^4/Z2 with ι(z,x)=(-z,x), both points SU(2)-type for either orientation, gluing two Eguchi–Hanson spaces with τ=-2 gives CP2bar#CP2bar — check χ, τ, η=0, π_1, the T^2-action lifting to the toric EH resolutions, and the Orlik–Raymond conclusion; identify E1±E2; (c) Theorem 52.7(b): orientation bookkeeping for L(4,1), L(4,3), the A3 plumbing and the rational ball B_2, π_1, homeomorphism to #3CP2bar, and what is still needed for diffeomorphism; (d) the characteristic bookkeeping in the JSON (χ_orb, τ_orb, η_{Z4}=1/2 from 3η=r-2+2/|Γ|, the Theorem-G charges 1,0,0,2,3); (e) Corollary 52.8: the O(ε²) gluing estimate for Ricci-flat ALE into orbifold metrics, the identification X#(S^4/Z2)=(X#X)/ι with two isolated fixed points and P_orb=P_Z/2, hence α(X#2CP2bar) ≤ (1/2)α^ι(X#X); (f) Corollary 52.9: (i) unconditional, (ii) conditional, (iii) the refutation of 'every exceptional class in the bulk', (iv) the orbifold LeBrun estimate reproducing k ≤ A/3 in every absorption pattern (state precisely the orbifold SW input needed), (v) the non-Kähler argument via basic classes; and the global judgment paragraph. Also judge novelty: is this absorption phenomenon standard in the literature (e.g. resolutions of S^4/Z2, Kummer-type constructions, rational blowdown), and which statements need a citation rather than a proof. Return corrected statements.

## Integrated Scientific Memo

# Section 3 and Proposition 52.10: verification and corrected statements

## Overall verdict

The two explicit absorption constructions are valid:

\[
A_1\oplus A_1\subset -\mathbb Z^2,\qquad
A_3=D_3\subset-\mathbb Z^3,
\]

and give, respectively, two- and three-class absorption. The \(S^4/\mathbb Z_2\) resolution is indeed
\(\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2\). The \(A_3\) construction gives a simply connected negative-definite manifold \(Q_3\) homeomorphic to \(\#3\overline{\mathbb{CP}}^2\); its standard diffeomorphism type is not established in the note.

The characteristic-number and Theorem-G computations in the JSON are correct. The gluing inequality

\[
\alpha(X\#2\overline{\mathbb{CP}}^2)
\le \frac12\alpha^\iota(X\#X)
\]

is justified.

Four substantive corrections are needed:

1. “By rank, \(k=1\) cannot be absorbed” is false without an additional hypothesis restricting the entire bubble lattice to the blow-up subspace.
2. Proposition 52.10 should state conservation of the signed pair \((C_+,C_-)\), not merely conservation after taking the nonlinear scalar charge.
3. Corollary 52.9(iv) needs substantially stronger orbifold Seiberg–Witten input than the current wording states.
4. Corollary 52.9(v)’s basic-class-count argument is not valid in that generality; a direct characteristic-class parity argument gives a stronger correct result.

---

## 1. Lemma 52.6: lattice statement

Let

\[
L=H_2(M;\mathbb Z)/\operatorname{Tor},
\qquad
R\subset L
\]

be the image of the direct sum of the ALE root lattices. Since the links are rational homology spheres, rational Mayer–Vietoris separates bulk and bubble homology. Thus the correct integral object is the saturation

\[
R^{\mathrm{sat}}=(R\otimes\mathbb Q)\cap L.
\]

For an integral exceptional class \(E\in L\),

\[
E\in R\otimes\mathbb Q
\quad\Longleftrightarrow\quad
E\in R^{\mathrm{sat}}.
\]

Thus \(E\in R\otimes\mathbb Q\) is the right rational-homology definition of absorption, provided the actual embedded root lattice is meant. An abstract overlattice containing a norm \(-1\) vector proves only algebraic possibility; realization also requires the actual discriminant-form gluing across the links.

### Explicit embeddings

With the ambient form \(-I\),

\[
A_1\oplus A_1
=\langle a,b\rangle,\qquad
a=e_1+e_2,\quad b=e_1-e_2,
\]

has index \(2\) in \(-\mathbb Z^2\), and

\[
e_1=\frac{a+b}{2},\qquad e_2=\frac{a-b}{2}.
\]

Likewise, for

\[
a_1=e_2-e_3,\quad a_2=e_1-e_2,\quad a_3=e_2+e_3,
\]

the \(a_i\) form an \(A_3=D_3\) chain of index \(2\) in \(-\mathbb Z^3\), with

\[
\begin{aligned}
e_1&=\tfrac12a_1+a_2+\tfrac12a_3,\\
e_2&=\tfrac12a_1+\tfrac12a_3,\\
e_3&=-\tfrac12a_1+\tfrac12a_3.
\end{aligned}
\]

More generally,

\[
D_n=\{x\in\mathbb Z^n:\ \textstyle\sum_i x_i\equiv0\pmod2\}
\subset\mathbb Z^n
\]

has index \(2\), and the ambient basis vectors have norm \(-1\).

The stated exceptional irreducible cases are also correct:

- \(A_1,A_2,E_6,E_7\): their discriminants are not squares, so no same-rank unimodular overlattice exists.
- \(E_8\): already even unimodular, hence no norm \(-1\) vectors.
- \(A_8\): its index-\(3\) integral unimodular extension is \(E_8\), again even.
- Among irreducible ADE lattices, an odd integral extension containing norm \(-1\) vectors occurs for \(A_3=D_3\) and \(D_n\), \(n\ge4\); the reducible \(D_2=A_1\oplus A_1\) is the two-class case.

For arbitrary ADE direct sums, the complete criterion is not merely “square discriminant”: one must find an integral isotropic gluing subgroup in the discriminant form whose overlattice contains a vector of norm \(-1\). Cross-component gluing is essential, as \(A_1\oplus A_1\) demonstrates.

### Correction to the \(k=1\) claim

The unconditional sentence

> “By rank, \(k=1\) cannot be absorbed”

must be deleted. It is only valid under a condition such as

\[
R\otimes\mathbb Q
\subset \operatorname{span}_{\mathbb Q}\{E_1,\ldots,E_k\},
\]

i.e. the bubble lattice is entirely contained in the pure blow-up subspace. For \(k=1\), no nonzero ADE root can lie in \(\mathbb QE\), because \(a=qE\) and \(a^2=-2\) would imply \(q^2=2\), impossible for \(q\in\mathbb Q\).

Without this restriction, a higher-rank \(D_n\) lattice can mix the designated exceptional class with pre-existing homology from \(X\). Therefore the examples prove that one \(A_1\) bubble does not absorb a class, not that a single distinguished blow-up class can never be absorbed in any larger lattice configuration.

A corrected lemma is:

> **Corrected Lemma 52.6.**  
> For the actual embedded root lattice \(R\subset L=H_2(M;\mathbb Z)/\mathrm{Tor}\), define absorption of an exceptional class \(E\) by
> \[
> E\in R^{\mathrm{sat}}=(R\otimes\mathbb Q)\cap L.
> \]
> The embeddings
> \[
> A_1\oplus A_1\subset-\mathbb Z^2,\qquad
> A_3=D_3\subset-\mathbb Z^3,\qquad
> D_n\subset-\mathbb Z^n
> \]
> have index \(2\) and contain the displayed norm \(-1\) classes in their saturations. The index-\(3\) integral extension of \(A_8\) is even \(E_8\) and contains no norm \(-1\) vector. A single \(A_1\) configuration cannot absorb a norm \(-1\) integral class. More generally, one exceptional class cannot be absorbed if the entire root span is assumed to lie in its one-dimensional rational blow-up span.

---

## 2. Theorem 52.7(a): resolving \(S^4/\mathbb Z_2\)

The involution

\[
\iota(z_1,z_2,x)=(-z_1,-z_2,x)
\]

has exactly the fixed points \((0,0,\pm1)\). At each, the tangent representation is \(-I\) on \(\mathbb R^4\). This is an \(A_1\) representation for either orientation: the central element \(-1\) lies in either half-spin \(SU(2)\) factor.

The quotient’s underlying topological space is the suspension of \(\mathbb{RP}^3\), and its regular complement is \(\mathbb{RP}^3\times I\).

### Characteristic numbers

\[
\chi_{\rm orb}(S^4/\mathbb Z_2)=1,\qquad
\tau_{\rm orb}(S^4/\mathbb Z_2)=0.
\]

For Eguchi–Hanson,

\[
\chi=2,\qquad \tau=-1,\qquad
3\eta_{\mathbb Z_2}=1-2+\frac22=0.
\]

Replacing both cone points therefore gives

\[
\chi=1+2\left(2-\frac12\right)=4,\qquad
\tau=0+2(-1+0)=-2.
\]

Equivalently, using ordinary Euler characteristic, the suspension has \(\chi_{\rm top}=2\), and each replacement raises \(\chi\) by \(1\).

### Fundamental group

The regular middle region has fundamental group \(\mathbb Z_2\). Each truncated Eguchi–Hanson space is simply connected, and the map

\[
\pi_1(\mathbb{RP}^3)\longrightarrow
\pi_1(\mathbb{RP}^3\times I)
\]

is an isomorphism. Gluing even one EH end kills this group, so the resolution is simply connected.

### Torus action and smooth type

The coordinatewise \(T^2\)-action on \(\mathbb C^2\) commutes with \(\iota\), descends to the quotient, and lifts to the toric minimal resolutions of the two \(A_1\) points. After dividing out any finite ineffective kernel, the resolved manifold has an effective \(T^2\)-action.

Orlik–Raymond classification then identifies the simply connected manifold from its negative-definite rank-two form:

\[
\widehat{S^4/\mathbb Z_2}
\cong
\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2.
\]

In a diagonal basis \(E_1,E_2\), the two disjoint root spheres are, up to signs and interchange,

\[
E_1+E_2,\qquad E_1-E_2.
\]

Thus Theorem 52.7(a) is correct, subject to citing the toric resolution and Orlik–Raymond classification.

---

## 3. Theorem 52.7(b): \(B_2\), \(A_3\), and \(Q_3\)

Fix the convention that the \(\frac14(1,3)\) singularity has link \(L(4,3)\). The negative \(A_3\) plumbing has boundary \(L(4,3)\), since

\[
\frac43=[2,2,2].
\]

The rational ball

\[
B_2=\mathbb{CP}^2\setminus N(\text{conic})
\]

has

\[
\partial B_2\cong L(4,1)\cong -L(4,3),
\qquad
\pi_1(B_2)=\mathbb Z_2.
\]

The note should distinguish oriented equality from unoriented diffeomorphism, rather than writing the lens-space identifications ambiguously.

Let

\[
Q_3=B_2\cup_{L(4,1)} P_{A_3},
\]

where \(P_{A_3}\) is the negative \(A_3\) plumbing. The boundary map

\[
\pi_1(L(4,1))=\mathbb Z_4
\twoheadrightarrow \pi_1(B_2)=\mathbb Z_2
\]

is surjective, while \(P_{A_3}\) is simply connected. Van Kampen gives

\[
\pi_1(Q_3)=1.
\]

Since \(B_2\) is a rational homology ball and \(P_{A_3}\) retracts onto the three-sphere chain,

\[
\chi(Q_3)=1+4=5,\qquad
b_2(Q_3)=3,\qquad
\tau(Q_3)=-3.
\]

The integral intersection lattice is the odd unimodular saturation

\[
A_3\subset-\mathbb Z^3.
\]

Donaldson diagonalization identifies its smooth intersection form as \(-I_3\), and Freedman gives

\[
Q_3\approx_{\rm homeo}
\#3\overline{\mathbb{CP}}^2.
\]

The note correctly does not claim a diffeomorphism. To obtain one, it still needs either:

1. an explicit Kirby reduction to three disjoint \((-1)\)-framed handles; or
2. a proof that the circle actions on \(B_2\) and the toric \(A_3\) plumbing match under the chosen lens-space gluing, including isotropy weights and boundary fiber slopes, followed by the appropriate circle-action classification theorem.

The mere existence of actions on both pieces is insufficient. Until this is supplied, all \(A_3\) conclusions should be stated for \(Q_3\), not for the standard \(\#3\overline{\mathbb{CP}}^2\).

---

## 4. Characteristic bookkeeping

For a rank-\(r\) Kronheimer ALE space,

\[
\chi=1+r,\qquad \tau=-r,\qquad
3\eta_\Gamma=r-2+\frac2{|\Gamma|}.
\]

Hence

\[
\eta_{\mathbb Z_2}=0,\qquad
\eta_{\mathbb Z_4}=\frac12.
\]

For

\[
\Sigma_4=B_2\cup\operatorname{cone}(L(4,3)),
\]

the underlying topological Euler characteristic is \(2\), so

\[
\chi_{\rm orb}(\Sigma_4)
=2-\left(1-\frac14\right)=\frac54.
\]

The resolution formula

\[
-3=\tau_{\rm orb}(\Sigma_4)+\tau(A_3)+\eta_{\mathbb Z_4}
\]

gives

\[
\tau_{\rm orb}(\Sigma_4)=-\frac12.
\]

Thus:

\[
\begin{array}{c|cc}
\text{construction}&\Delta\chi&\Delta\tau\\ \hline
X\#(S^4/\mathbb Z_2)+2\,EH&2&-2\\
X\#\Sigma_4+A_3&3&-3
\end{array}
\]

and

\[
(2\chi+3\tau)_{\rm orb}
=
\begin{cases}
(2\chi+3\tau)(X)-2,&X\#(S^4/\mathbb Z_2),\\
(2\chi+3\tau)(X)-3,&X\#\Sigma_4.
\end{cases}
\]

These JSON entries are correct.

The script does not itself prove every mathematical annotation:

- `all_roots_norm_-2` checks the listed simple generators, not all roots;
- the \(A_8,E_8,D_4\) overlattice descriptions are hard-coded;
- \(\tau_{\rm orb}(\Sigma_4)\) is reconstructed from the expected resolved signature.

These are documentation issues, not numerical errors.

---

## 5. Proposition 52.10: the ledger conserved is the signed pair

Define

\[
C_\sigma(\Omega)=
\sum_{\rm out}q_\sigma(\Gamma)
-\sum_{\rm in}q_\sigma(\Gamma)
-\bigl(2\chi(\Omega)+3\sigma\tau(\Omega)\bigr),
\]

where

\[
q_\sigma(\Gamma)=\frac2{|\Gamma|}-3\sigma\eta_\Gamma,
\qquad \sigma=\pm1.
\]

The computations are:

\[
\begin{array}{c|c|c}
\text{block}&(C_+,C_-)&[\,\max(C_+,C_-,0)\,]\\ \hline
\text{Burns}&(1,-5)&1\\
EH&(0,-6)&0\\
A_3&(0,-15)&0\\
S^4/\mathbb Z_2\text{ cell}&(2,2)&2\\
\Sigma_4\text{ cell}&(3,0)&3\\
D\#2\overline{\mathbb{CP}}^2\text{ cell}&(2,-10)&2\\
D\#3\overline{\mathbb{CP}}^2\text{ cell}&(3,-15)&3.
\end{array}
\]

The exact conservation identities are

\[
(2,2)+2(0,-6)=(2,-10)
\]

and

\[
(3,0)+(0,-15)=(3,-15).
\]

Internal link contributions cancel linearly at the level of each \(C_\sigma\). They do not, in general, cancel after applying \(\max\{0,C_+,C_-\}\). Consequently, Proposition 52.10 should be rewritten as follows.

> **Corrected Proposition 52.10.**  
> For the standard flat/round germs in the two absorption constructions, the signed Theorem-G ledger \((C_+,C_-)\) is conserved under replacing the smooth blow-up cell by the corresponding orbifold cell plus its Kronheimer resolution blocks:
> \[
> (C_+,C_-)_{S^4/\mathbb Z_2\ {\rm cell}}
> +2(C_+,C_-)_{EH}
> =(2,-10),
> \]
> \[
> (C_+,C_-)_{\Sigma_4\ {\rm cell}}
> +(C_+,C_-)_{A_3}
> =(3,-15).
> \]
> These equal the ledgers of \(D\#2\overline{\mathbb{CP}}^2\) and \(D\#3\overline{\mathbb{CP}}^2\), respectively. Their scalar lower-bound charges are therefore \(2\) and \(3\). The Kronheimer blocks have scalar charge \(0\), while the corresponding orbifold cells carry the entire positive scalar charge.

The final interpretation is sound only in this restricted standard-germ setting: topology does not make the zero-cost ALE blocks cheaper than zero; any improvement over a standard smooth-cell bound would have to arise from nonstandard boundary germs and ambient-curvature interaction. It is not a universal additive conservation theorem for arbitrary geometries.

---

## 6. Corollary 52.8

Near an orbifold point,

\[
g_{\rm orb}=\delta+O(\rho^2),
\]

while a scaled Ricci-flat ALE metric satisfies

\[
g_{\epsilon,\rm ALE}
=\delta+O(\epsilon^4\rho^{-4}).
\]

Choose the interpolation radius

\[
\rho\asymp\epsilon^{1/2}.
\]

Then second derivatives of the interpolated error are \(O(1)\), so

\[
|\operatorname{Ric}^\circ|=O(1)
\]

on an annulus of volume \(O(\rho^4)=O(\epsilon^2)\). The removed orbifold ball has the same order of volume, and the ALE interior is Ricci-flat. Hence

\[
P(g_\epsilon)
=P_{\rm orb}(g)+O(\epsilon^2).
\]

Therefore

\[
\alpha(\operatorname{resolution}(Y))
\le\alpha_{\rm orb}(Y).
\]

For the double-cover construction, perform equivariant connected sums at a free \(\iota\)-orbit of two points. The cover is

\[
Z=X\#S^4\#X\cong X\#X,
\]

with an involution interchanging the two \(X\)-summands and retaining the two fixed points from the middle \(S^4\). Its quotient is

\[
Z/\iota\cong X\#(S^4/\mathbb Z_2).
\]

Invariant smooth metrics upstairs correspond to orbifold-smooth metrics downstairs, and

\[
P_Z=2P_{\rm orb}.
\]

Thus

\[
\alpha_{\rm orb}\bigl(X\#(S^4/\mathbb Z_2)\bigr)
=\frac12\alpha^\iota(X\#X)
\]

and

\[
\boxed{
\alpha(X\#2\overline{\mathbb{CP}}^2)
\le\frac12\alpha^\iota(X\#X).
}
\]

The \(m>1\) assertion about the topology of the double cover,

\[
X\#X\#(m-1)(S^1\times S^3),
\]

requires an explicit equivariant connected-sum argument and should not be used without one.

---

## 7. Corollary 52.9

### (i) Unconditional direction

Correct:

> If \(M\) is obtained by resolving a compact Einstein orbifold using Ricci-flat ALE spaces, including a finite bubble tree inserted at separated scales, then \(\alpha(M)=0\).

The Einstein bulk and Ricci-flat ALE pieces have \(P=0\), while the gluing contributions tend to zero.

### (ii) Conditional converse

Correct subject to the stated compactness and selection hypotheses. If a noncollapsed selected sequence has \(\alpha(M)=0\), lower semicontinuity forces every nonnegative bulk and bubble contribution to vanish. Thus the bulk components are Einstein and the ALE bubbles are Ricci-flat.

A nontrivial Ricci-flat ALE space cannot have trivial asymptotic group: if \(\Gamma=1\), its asymptotic volume ratio is \(1\), and Bishop–Gromov rigidity gives Euclidean space. The single-ended assertion follows from the standard end theory under nonnegative Ricci curvature.

### (iii) Failure of “every exceptional class lies in the bulk”

Correct, but should be phrased in homological terms:

> Exceptional classes need not project nontrivially to the rational homology of the orbifold bulk. They may lie in the saturation of the ALE root lattice inside the total integral homology.

The resolution of round \(S^4/\mathbb Z_2\) already gives a concrete zero-gap example in which both exceptional classes lie in the rational span of the two \(A_1\) roots.

### (iv) Orbifold LeBrun estimate

The numerical implication

\[
A-k\ge \frac23A
\quad\Longrightarrow\quad
k\le \frac A3
\]

is correct. The current hypothesis is not sufficient to derive it.

A precise sufficient package is:

1. The bulk \(Y\) supports the relevant orbifold Spin\(^c\) structures, and the orbifold Seiberg–Witten/monopole estimate applies in the required chamber:
   \[
   (2\chi+3\tau)_{\rm orb}(Y)
   \ge \frac23(c_Y^+)^2.
   \]
2. A projected canonical component \(K_0\) exists with
   \[
   K_0^2=A.
   \]
3. Absorbed exceptional classes project to zero.
4. For every sign choice among the unabsorbed classes,
   \[
   c_\varepsilon
   =K_0+\sum_{j=1}^{u}\varepsilon_j e_j,
   \qquad \varepsilon_j=\pm1,
   \]
   the corresponding orbifold Spin\(^c\) structure exists and supplies a nonzero invariant, or an equivalent theorem directly provides one class satisfying
   \[
   (c_Y^+)^2\ge A.
   \]

Indeed,

\[
2^{-u}\sum_{\varepsilon}
\left\|
\left(K_0+\sum_j\varepsilon_je_j\right)^+
\right\|^2
=
\|K_0^+\|^2+\sum_j\|e_j^+\|^2
\ge K_0^2=A.
\]

Hence at least one sign choice has \((c_\varepsilon^+)^2\ge A\), and then

\[
A-k=(2\chi+3\tau)_{\rm orb}(Y)
\ge\frac23A.
\]

A single unspecified nonzero orbifold invariant for “the projected class” does not establish this. The required descent of Spin\(^c\) structures, local isotropy representations, chamber conditions, and nonvanishing/gluing theorem are not proved in Section 3 and need citation or a separate theorem.

### (v) Non-Kähler result

The basic-class-count argument should be removed. A minimal surface of general type need not have only \(\pm K\) as basic classes, and the argument also becomes sensitive to the unresolved smooth structure of \(Q_3\).

There is a direct, stronger proof. If \(Y\) is a complex orbifold with \(SU(2)\) quotient singularities and

\[
\pi:Z\to Y
\]

is its minimal crepant resolution, then

\[
K_Z\cdot r=0
\]

for every exceptional root \(r\in R\). Therefore, if an integral class \(E\) satisfies \(E\in R\otimes\mathbb Q\), then

\[
K_Z\cdot E=0.
\]

But the canonical class is characteristic, so for every integral \(E\),

\[
K_Z\cdot E\equiv E^2\pmod2.
\]

If \(E^2=-1\), the right side is \(1\pmod2\), contradicting \(K_Z\cdot E=0\). Thus:

> **Corrected Corollary 52.9(v).**  
> In the crepant resolution of a complex orbifold with \(SU(2)\) quotient singularities, no integral class of odd square—hence no exceptional class of square \(-1\)—can belong to the rational span of the exceptional root lattice. Consequently, any Einstein orbifold realizing the EH-pair or \(A_3\) absorption pattern cannot carry a compatible global complex-orbifold structure for which those singularities are complex \(SU(2)\) quotient singularities. In particular, it cannot be Kähler in that compatible sense.

This is stronger than excluding complete absorption: it excludes absorption of even one square-\(-1\) integral class in the complex crepant setting.

---

## 8. Corrected global judgment

The valid conclusion is:

> In the range \(0<k<A/3\), a positive Einstein gap must control not only exact Einstein metrics on \(X\#k\overline{\mathbb{CP}}^2\), but also absorbing Einstein orbifolds and potentially nonattaining near-Einstein sequences on their finite covers. For the EH-pair construction,
> \[
> \alpha(X\#2\overline{\mathbb{CP}}^2)
> \le\alpha_{\rm orb}(X\#S^4/\mathbb Z_2)
> =\frac12\alpha^\iota(X\#X).
> \]
> Hence positivity downstairs implies positivity for the corresponding orbifold and invariant problem upstairs. Since blow-up classes may lie in the saturation of the ALE root lattice, a lower-bound argument that assigns an independent charge to every standard exceptional generator cannot be valid using rational intersection-lattice data alone. Any surviving tariff must detect additional data such as boundary germs, discriminant/linking forms, local Spin\(^c\) representations, monopole flux, or ambient-curvature interaction.

Only the \(S^4/\mathbb Z_2\) construction has the stated involution-cover equivalence. No analogous cover of the \(\Sigma_4\) construction has been established in the note.

Also, “at least as hard as Einstein existence” is too weak if interpreted literally: proving \(\alpha>0\) must rule out \(P\to0\) sequences even when no exact Einstein metric exists.

---

## 9. Novelty and citations

The underlying topology is standard rather than new:

- integral overlattices, discriminant forms, and primitive closures of ADE lattices;
- Kummer-type nonprimitive root-lattice embeddings;
- \(S^4/\mathbb Z_2\) as the suspension of \(\mathbb{RP}^3\);
- toric resolutions of \(A_1\) and \(A_3\) singularities;
- rational blowdown/rational blow-up using \(B_2\) and the \(A_3\) plumbing;
- APS/Kawasaki signature corrections and Kronheimer ALE topology;
- Orlik–Raymond and circle-action classifications.

These need citations rather than presentation as novel constructions. In particular, the claimed \(Q_3\) diffeomorphism needs either an existing Kirby/circle-action citation or a complete proof.

What may be genuinely distinctive is the application of these standard mechanisms to the Einstein-gap functional:

\[
\alpha(X\#2\overline{\mathbb{CP}}^2)
\le\frac12\alpha^\iota(X\#X),
\]

the observation that zero-\(P\) Kronheimer blocks can move exceptional topology out of the rational bulk, and the signed-ledger identities showing where the standard-germ charge is relocated. Those applications may be stated as new only after a literature search; the general “absorption” phenomenon itself is classical.

The orbifold LeBrun argument especially requires an exact citation matching isolated ADE singularities, Spin\(^c\) descent, chamber assumptions, and nonvanishing. It should remain explicitly conditional until such a theorem is identified.