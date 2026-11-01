# TTCS Independent Branch Record

```json
{
  "step_id": 99,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step96_suvaina_lattice_and_kahler_filler_theorem.md",
    "Knowledge/objects/papers/ALE-Ricci-flat-Kahler-metrics-and-deformations-of-quotient-surface-singu--9db598b6c84c--5ab7b434e210/object.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/state_of_problems_1_4.md",
    "Sessions/S1003A02/workspace/notes/step58_consolidated_hypothesis_ledger.md",
    "Sessions/S1003A02/workspace/notes/step94_filler_screen_dichotomy.md",
    "Knowledge/objects/papers/Einstein-Metrics-Symplectic-Minimality-and-Pseudo--a623e9917b57--dd585f36cd43/object.md"
  ]
}
```

## Task

Independently verify the Step-98 extension of Lemma 96.Ş to minimal resolutions of singular invariant fibres and the synchronized scientific scope in the theorem package, front matter, hypothesis ledger, and Step-94 binding correction. Read Şuvaina's primary source as grounding. Check the equivariant Gibbons–Hawking-centre isotopy, topology, H1/H2, determinant and transfer-index arguments; distinguish source statements from the new diffeomorphism argument. Then inspect whether package/front-matter claims about 96.K, 98.W/98.V, ALE decay, Armstrong/Problem 4, and the conditional T_AK statement have exact hypotheses and no global overstatement. Return concrete mathematical corrections only where warranted.

## Output

# Verification memo: Step-98 extension of Lemma 96.Ş and its synchronization (96.K, 98.W/98.V, ALE decay, Problem 4, T_AK)

## Summary

- The singular-fibre extension of Lemma 96.Ş is correct, and so are its H₁, H₂, determinant and transfer-index arguments. The equivariant isotopy needs two repairs in wording and proof (§1.2).
- Theorem 96.K, Proposition 98.W and Corollary 98.V check out line by line. Two textual slips need fixing: one in 98.W(1) and one in a front-matter sentence.
- The T_AK statement in the front matter should not be labelled conditional on A01's identity (i). Under Gauss–Bonnet alone, its "first consequence" is an identity for every Einstein metric, and (iii) is an inherited fact.

## 1. Lemma 96.Ş for minimal resolutions of singular invariant fibres

### 1.1 What Şuvaina states, and what is new

**Source statements.**
- Prop. 4.4 states that the universal cover is ALE hyperkähler and that π₁ is finite cyclic.
- Theorem B states that \((N,J)\) is the minimal resolution of a fibre of a one-parameter ℚ-Gorenstein deformation. For π₁ ≠ 1 the universal cover is \(A_{dn-1}\) and the end is \(\frac1{dn^2}(1,dnm-1)\).
- In the proof of Theorem B: the singular points of the fibre \(M^s\) are of type A, and G acts freely on the canonical model. The argument is that a tree configuration has one more sphere than intersection points.
- §3, citing Hitchin: coincident \(a_i\) with distinct \(b_i\) give exceptional (−2)-curves; equal \(b_i\) give an orbifold.
- §5: the Gibbons–Hawking (GH) polygon description and the action \(\rho(a)=\rho^{-m}a,\ \rho(\theta)=\rho\theta\).

**Two source points relevant here.**
- The source's treatment of the case with (−2)-curves goes through Prop. 2.4, which is quoted from Manetti's 1990 preprint.
- Şuvaina's §3 invariance computation is written under the hypothesis "M smooth, \(c_i^n\) distinct". For the singular-fibre case it applies verbatim, because the twistor invariance condition \(p_{i-m}(u)=\ldots\Rightarrow b_i=b_{i-m}\) never uses distinctness of the \(a_{ij}\). The note should say that it reuses this computation rather than present the GH description of the resolved singular fibre as stated by Şuvaina.

**New in Step 96/98.** The equivariant diffeomorphism to a smooth-fibre model.

**\(c_i\ne0\) is forced, not assumed.** Suppose \(z^n\) divides \(\prod(z^n-c_i^n)\). Then the origin lies on the fibre, is fixed by \((x,y,z)\mapsto(\rho x,\rho^{-1}y,\rho^mz)\), and is an \(A_{\ge n-1}\) point of \(M^s\). This contradicts Şuvaina's freeness of G on the canonical model. The note asserts \(c_i\neq0\) but should cite this freeness as the reason.

**Example check.** Take \(xy=(z^2-1)^2\) with the action \(-1\), so \(n=2\), \(m=1\), \(d=2\).
- The end is \(\frac18(1,3)=L(8,3)\).
- The two \(A_1\) points \((0,0,\pm1)\) are swapped by the action.
- The invariant resolution therefore carries a free action, and the quotient contains one (−2)-curve.
- All of this is correct.

### 1.2 The equivariant GH-centre isotopy: two repairs

**(a) Connectedness argument.** The "perturb the \(c_i\)" step can be replaced by an exact statement.
- The admissible centre sets are unions of d free \(\mathbb Z_n\)-orbits in \(\mathbb R\times\mathbb C^*\), where the action is rotation by \(\rho^{-m}\).
- Such sets correspond bijectively to d-point configurations in the quotient \((\mathbb R\times\mathbb C^*)/\mathbb Z_n\cong\mathbb R\times\mathbb C^*\), via \(a\mapsto a^n\).
- This is a connected 3-manifold, so its configuration space of d distinct points is connected. Any two admissible centre sets with the same \((d,n,m)\) are therefore joined by an equivariant, compactly supported isotopy that avoids the axis.
- This gives at once that diffeomorphism type does not depend on \(c\). It also covers coincident projections, since only three-dimensional distinctness is used.

**(b) Lifting the isotopy.** "The isotopy lifts since Chern numbers around corresponding centres agree" is not enough.
- \(\mathbb Z_n\)-equivariant circle bundles over \(\mathbb R^3\setminus C\) are classified by \(H^2_{\mathbb Z_n}\), which carries torsion from \(H^2(B\mathbb Z_n)=\mathbb Z_n\) (the character on the fibre over the axis).
- The correct argument: the GH bundles \(P_{C_t}\) form one equivariant bundle over \(\{(x,t):x\notin C_t\}\). The map \((x,t)\mapsto(\phi_t^{-1}x,t)\) identifies this space with \((\mathbb R^3\setminus C_0)\times[0,1]\). Equivariant homotopy invariance for the finite group then gives an equivariant isomorphism \(P_{C_0}\cong\phi_1^*P_{C_1}\).
- Each centre has trivial stabilizer, so the Hopf fillings extend orbitwise.
- The isotopy is the identity near infinity, so the end identification is preserved.

### 1.3 Topology, H₁/H₂, determinant, transfer

All steps verified independently.

- **Basic invariants.** \(\chi(\widetilde N)=dn\) gives \(\chi(N)=d\). The invariant rank of the permutation module is \(d-1\), which gives \(b_2=d-1\).
- **\(H_3=0\).** By Lefschetz duality \(H_3(N)\cong H^1(N,\partial N)\), and this vanishes because \(H^0(N)\to H^0(\partial N)\) is an isomorphism.
- **Torsion-freeness, and a shortcut.** \(\partial\widetilde N\) is connected, so \(\pi_1\partial N\to\pi_1N\) is onto. Hence \(H_1(N,\partial N)=0\), so \(\operatorname{Ext}(H_2N,\mathbb Z)\subset H^3(N)=0\). Shortcut: in the Cartan–Leray sequence the only differential is \(d^3:\mathbb Z_n\to\Lambda_{\mathbb Z_n}\cong\mathbb Z^{d-1}\oplus\mathbb Z_n\), and \(H_3(N)=0\) already forces \(d^3\) to be injective. An injection of \(\mathbb Z_n\) lands in the torsion summand and is therefore onto it. So (b) alone implies (c).
- **Determinant.** For an injective map \(F\to F^*\oplus\mathbb Z_n\) whose \(F^*\)-component is \(Q_N\), the cokernel has order \(|\det Q_N|\cdot n\) for any \(\mathbb Z_n\)-component. Since \(|\ker(H_1\partial N\to H_1N)|=dn^2/n\), this gives \(|\det Q_N|=d\). This matches (d) and makes the "free projection" wording unnecessary.
- **Transfer.** The invariant lattice is \(\{\sum t_iO_i:\sum t_i=0\}\). Its Gram matrix scaled by \(1/n\) is \(-(\delta_{ij}+1)\), which is \(A_{d-1}(-1)\) in the basis \(f_i-f_d\). The index \(j\) of \(\pi^!F\) satisfies \(dj^2=d\), so \(j=1\).
- **Signless permutation.** The deck generator preserves arc direction and fibre orientation, so it acts by a permutation without signs.
- **Charge.** \(c=1-1/(dn^2)\) is topological and is unchanged by the residual resolution.

## 2. Theorem 96.K and Proposition 98.W / Corollary 98.V

### 2.1 Theorem 96.K

Recomputed:
- **Costs.** \(D_2\in\{\tfrac12+\tfrac12,\ \tfrac12+\tfrac78,\ \tfrac74\}\); \(A_3=\tfrac34\) against Şuvaina \(d=4\) at \(\ge\tfrac{15}{16}\); \(D_a=1-1/(4(a-2))\), from the binary dihedral group of order \(4(a-2)\).
- **β.** From \(x_{\min}\): \(\beta=A(1+5y)(1-y)/54=k(5y+1)/[18(1+y)]\).
- **\(D_6\) threshold.** \(\beta(6,A)\ge15/16\iff y\ge29/35\iff A\ge3675/64\).
- **No Wahl point at k=6.**
  - Complex Wahl balls add at least 3/4 and so exceed β.
  - Reversed Wahl balls in (94.2) would need \(1-1/n^2\le9/32\), which is impossible for \(n\ge2\).
- **Structure of full absorption.** The roots of an orthogonal sum of definite lattices are the union of the roots of the summands. \(D_{a\ge4}\) is irreducible, and every Şuvaina lattice is of type A. Together these give the block statement.
- **Hypothesis attached.** The statement correctly carries the ball-quotient (aspherical, torsion-free Γ) hypothesis required by (L0).

### 2.2 Proposition 98.W

- **Item (1).**
  - The Mayer–Vietoris sequence ends with \(\to0\) because \(H_0(Y)\to H_0(W)\oplus H_0(B)\) is injective.
  - \(K=\oplus n_j\mathbb Z_{n_j^2}\subset\oplus\operatorname{rad}(n_j)\mathbb Z_{n_j^2}=\Phi(G)\), and the Frattini step is valid.
  - Text fix: "Every prime dividing \(n_j\) divides \(n_j\)" should read "every prime dividing \(n_j^2\) divides \(n_j\)".
- **Item (3).** The chain \(\operatorname{Tor}H_2W\cong\operatorname{Tor}H^3W\) (universal coefficients) \(\cong\operatorname{Tor}H_1(W,Y)\) (Lefschetz) \(\cong\operatorname{Tor}H_1W\) is correct. The snake lemma then gives \(0\to L\to U\to K\to0\).
- **Item (4)** is correct as stated, with its hypothesis that \(H_1(X)\) is torsion-free.

### 2.3 Corollary 98.V

- The class \(v/n\) has order exactly \(n^2\) because \(\gcd(N,n)=1\) and \(v\) is primitive. Its self-pairing is \(-N/n^2\).
- A form on a cyclic group is determined by its value on a generator modulo unit squares. The value \(q^{-1}=q(q^{-1})^2\) is covered, so the lens-convention ambiguity does no harm.
- The construction is sufficient at \(k\ge5t\) and is not shown to be necessary. Front-matter fix: "realizable for \(k\ge5\) per Wahl point, so it never obstructs" should read "does not obstruct when \(k\ge5t\); for \(k<5t\) the single-coordinate arithmetic (\(\mp(na-1)\) a unit square mod \(n^2\)) together with the \(Q_X\) block decides". The package §1 and §22.6(7) wording is already correct.
- The even-\(n\) quadratic refinement is correctly listed as unexamined.

## 3. ALE decay statements

- **What Lemma 86.S needs.** Only some \(\tau>0\) with two derivatives. The rate τ = 4 does not bear weight in the lemma, so precision about attribution affects no conclusion.
- **Şuvaina's Definition 1.1.** It is a definition (order \(r^{-4}\) for \(g\) and \(J\), with no derivatives), and the theorems are stated in that class. The text is accurate in calling it a record of order-four decay.
- **GH derivative control.**
  - A centred configuration kills the dipole term, giving \(V=\tfrac{k}{2|x|}(1+O(|x|^{-2}))\) with \(|x|\sim r^2\), hence \(O(r^{-4})\) with all derivatives.
  - Şuvaina's polygons can be centred by a b-axis translation, which commutes with the rotation and so is equivariant.
  - The GH end chart is equivariant.
- **Kronheimer D/E fillers.** The cite key `lidimensional` does not read as a Bando–Kasue–Nakajima reference. If it is a later paper restating BKN, write "BKN, as restated in [key], Def. 1.2/Thm 2.4" after checking `citation.bib`.

## 4. Problem 4 and Armstrong

- **Chern class.** \(c_2(K^{-1}\otimes T^{1,0})=c_2+2c_1^2=5\chi+6\tau\) is correct.
- **Hitchin–Thorpe step.** With \(s\ne0\), \(5\chi+6\tau\ge5\chi-4\chi=\chi\ge s^2V/(192\pi^2)>0\).
- **Second primary grounding in hand.** LeBrun 2005, Prop. 2.4 (attributed to Armstrong 1997 [2]) proves directly that \(s^*=s\) somewhere on any compact AKE manifold. It does so via \(\hat J\) with anticanonical bundle \(L^{-3}\). That argument gives \(\chi=-2c_1^2\) and \(\tau=\tfrac53c_1^2\), hence \(5\chi+6\tau=0\), which agrees with the AAD Lemma 2 form.
- **Attribution.** Keeping Armstrong 2002 unused is correct.

## 5. The T_AK statement: replace the conditional label

**Identification.** For every Einstein metric, Gauss–Bonnet and the signature formula give
\[
s^2V=32\pi^2c_1^2+16\int\Bigl(\tfrac{s^2}{24}-|W^+|^2\Bigr),\qquad
8\pi^2(\chi-3\tau)=\int\Bigl(\tfrac{s^2}{24}-|W^+|^2\Bigr)+3\int|W^-|^2 .
\]
- These are exactly A01's two consequences of (i), with \(T_{AK}=\int(s^2/24-|W^+|^2)\).
- They therefore hold if and only if \(T_{AK}\) equals this integral, with no almost-Kähler input.

**Consequence for (iii).** For any Einstein metric on \(M\), combining these identities with \(c_1^2=A-k\) and LeBrun's \(s^2V\ge32\pi^2A\) gives
\[
T=s^2V/16-2\pi^2(A-k)\ge2\pi^2k .
\]
This is the inherited bound \(\int|W^+|^2\le\int s^2/24-2\pi^2k\), the general-k form of package §15 Remark 4.

**Correction.**
- Replace "[C on (i)]" by: "(iii) holds for every Einstein metric on M provided \(T_{AK}=\int(s^2/24-|W^+|^2)\). It then adds no constraint beyond Gauss–Bonnet plus LeBrun."
- The only content that remains unchecked is the canonical-cycle identity (ii).

## 6. Step-94 binding header

- The Step-97/98 header correctly withdraws the norm-four vector and points to 98.W/98.V.
- It also correctly records that the Step-94 lattice question about Şuvaina fillers, \(Q_N\cong A_{d-1}(-1)\), is now proved for the whole class.
- §4's line "Theorem 55.5 is a k = 1 law [N, tentative]" still displays the withdrawn witness \(v=e_1+e_2+e_3+e_4\). A strike-through or inline pointer there would prevent misreading. The header already governs it.