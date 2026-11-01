# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 99,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step99_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step99_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the Step-98 extension of Lemma 96.Ş to minimal resolutions of singular invariant fibres and the synchronized scientific scope in the theorem package, front matter, hypothesis ledger, and Step-94 binding correction. Read Şuvaina's primary source as grounding. Check the equivariant Gibbons–Hawking-centre isotopy, topology, H1/H2, determinant and transfer-index arguments; distinguish source statements from the new diffeomorphism argument. Then inspect whether package/front-matter claims about 96.K, 98.W/98.V, ALE decay, Armstrong/Problem 4, and the conditional T_AK statement have exact hypotheses and no global overstatement. Return concrete mathematical corrections only where warranted.

## Integrated Scientific Memo

# Verification memo: Step-98 extension of Lemma 96.Ş and synchronized scope

## Summary

The Step-98 mathematics holds. Lemma 96.Ş extends to minimal resolutions of singular invariant fibres, and Theorem 96.K, Proposition 98.W and Corollary 98.V are correct. Both independent branches (complete) and my own rechecks agree on this.

The corrections needed are of four kinds:

1. **Proof repair.** The equivariant isotopy step does not justify lifting the isotopy to the circle bundles. It needs a stronger argument (§2).
2. **Scope.** Several summaries drop the hypotheses \(k\ge5t\) and "\(H_1(X)\) torsion-free" from 98.V/98.W. One Step-96 sentence overstates what 96.K decides.
3. **Problem 4 wording.** The zero count needs a transversality qualifier. The exceptional-curve sentence overstates what LeBrun's Cor. 3.6 supplies.
4. **\(T_{AK}\).** The "conditional" consequence is an identity of Gauss–Bonnet and signature. It needs an explicit orientation hypothesis and should not be labelled conditional on A01's identity (i).

---

## 1. Source statements versus the new argument

**Stated in Şuvaina (arXiv:1102.2672).**
- **Prop. 4.4.** The universal cover is ALE hyperkähler, and \(\pi_1\) is finite cyclic.
- **Theorem B.** \((N,J)\) is the minimal resolution of a fibre of a one-parameter \(\mathbb Q\)-Gorenstein deformation. For \(\pi_1\ne1\) the universal cover is of type \(A_{dn-1}\) and the end is \(\frac1{dn^2}(1,dnm-1)\).
- **Proof of Theorem B.** \(G\) acts freely on the canonical model \(M^s\), by the tree argument: a tree has one more sphere than intersection points. The singularities of \(M^s\) are of type A, and \(M\) is their minimal resolution. For the case containing \((-2)\)-curves the source invokes Prop. 2.4, which is Manetti's 1990 preprint. Completeness of the class therefore rests on that cited result.
- **Prop. 2.3.** This gives the invariant family \(xy=z^{dn}+\sum e_{jn}z^{(d-j)n}\).
- **§3, following Hitchin.**
  - Coincident \(a_i\) with distinct \(b_i\) give exceptional \((-2)\)-curves; equal \(b_i\) give an orbifold.
  - The \(\mathbb Z_n\)-invariance computation forces \(b_{i,j}=b_i\).
  - Şuvaina writes this computation under the hypothesis "\(M\) smooth, \(c_i^n\) distinct". It does not use distinctness of the \(a_{ij}\), so it transfers verbatim to the resolved singular fibre. The note should say it *reuses* this computation, not that Şuvaina states the GH model of the resolved singular fibre.
- **§5.** This gives the GH polygon model and the action \(\rho(a)=\rho^{-m}a\), \(\rho(\theta)=\rho\theta\).

**New in Steps 96/98.** The equivariant, orientation-preserving diffeomorphism of every resolved singular-fibre member to a smooth-fibre model \(N_{d,n,m}\). Step 96 §0 and package §22.6(7) already present it as new, not as a source statement.

**Why \(c_i\ne0\).** This should be stated as forced, not assumed. Suppose \(z^n\) divides the right-hand side. Then the origin lies on the fibre, is fixed by \((\rho x,\rho^{-1}y,\rho^mz)\), and is a singular point of \(M^s\). This contradicts freeness on the canonical model. In GH terms, a centre on the rotation axis is a fixed point of the lifted action, because the fibre circle collapses there.

**Example.** Take \(xy=(z^2-1)^2\) with the action of \(-1\), so \(n=2\), \(m=1\), \(d=2\).
- The end is \(L(8,3)\).
- The four centres are \((b_1,\pm1)\) and \((b_2,\pm1)\) with \(b_1\ne b_2\).
- The deck map swaps the two vertical arcs, i.e. the two \((-2)\)-curves. The quotient contains one \((-2)\)-curve \(C\), with \(\pi^![C]=O_1-O_2\) of norm \(-4=2\cdot(-2)\), consistent with \(A_1(-1)\).
- A smooth affine Milnor fibre contains no compact curves. The claim of non-biholomorphism therefore stands.

---

## 2. The equivariant GH-centre isotopy: required repair

The note says the isotopy "lifts to the circle bundles, whose Chern numbers around corresponding centres agree". That is insufficient. \(\mathbb Z_n\)-equivariant circle bundles over \(\mathbb R^3\setminus C\) are classified by equivariant cohomology \(H^2_{\mathbb Z_n}\). This group carries extra data, the character of the action on the fibre, that ordinary Chern numbers do not see.

The following replacement argument proves everything Step 98 uses, including the coincident-projection case.

**(a) Connectedness.** The admissible centre sets are unions of \(d\) free \(\mathbb Z_n\)-orbits in \(\mathbb R\times\mathbb C^*\).
- Via \((b,a)\mapsto(b,a^n)\) these correspond to \(d\) distinct points in \((\mathbb R\times\mathbb C^*)/\mathbb Z_n\cong\mathbb R\times\mathbb C^*\).
- This is a connected 3-manifold, so its configuration space of \(d\) distinct points is connected.
- Choose a compactly supported ambient isotopy downstairs. It lifts through the free degree-\(n\) covering to a compactly supported \(\mathbb Z_n\)-equivariant isotopy that avoids the axis and is the identity near infinity.
- The argument uses only three-dimensional distinctness, which Şuvaina guarantees for the smooth resolution (equal \(b_i\) would give an orbifold). Coincident complex projections are therefore covered automatically.

**(b) Equivariant bundle identification.** Two routes work.
- *Family route (Branch 2).* The bundles \(P_{C_t}\) form one equivariant bundle over \(\{(x,t):x\notin C_t\}\). The isotopy identifies this space with \((\mathbb R^3\setminus C_0)\times[0,1]\). Equivariant homotopy invariance for a finite group then gives \(P_{C_0}\cong\phi_1^*P_{C_1}\) equivariantly, with the fibre character fixed by the identity near infinity.
- *Connection route (Branch 1).* Take a \(\mathbb Z_n\times S^1\)-invariant family connection. The deck action \(\rho\theta\) commutes with the \(S^1\)-action. Integrate the horizontal lift of the base isotopy.

In both routes:
- each centre has trivial stabilizer, so the Hopf fillings extend orbitwise;
- orientation is preserved;
- the map is the identity near infinity, so the orientation-matched equivariant end chart required by Lemma 86.S is unchanged.

With this repair, \(\pi_1\), the end, the lattice and the charge are invariants of \((d,n,m)\) alone, as claimed.

---

## 3. Topology, \(H_1/H_2\), determinant, transfer index (verified)

Let \(M=\widetilde N\) be the \(dn\)-centre cover. Then \(H_2(M)=\Lambda=\{x\in\mathbb Z^{dn}:\sum x_a=0\}\) with form \(-\sum x_a^2\). The deck map preserves arc direction and fibre orientation, so it acts by the *unsigned* permutation \(p_{ij}\mapsto p_{i,j+m}\), with \(d\) orbits of length \(n\).

- **Basic invariants.** \(\pi_1=H_1=\mathbb Z_n\), \(\chi=d\), \(b_2=d-1\), and \(H_3(N)\cong H^1(N,\partial N)=0\).
- **Torsion-freeness (two independent proofs).**
  1. *Note's proof.* \(\partial M\) is connected, so \(\pi_1\partial N\to\pi_1N\) is onto. Hence \(H_1(N,\partial N)=0\), and \(\mathrm{Ext}(H_2N,\mathbb Z)\subset H^3(N)=0\).
  2. *Cartan–Leray (Branch 2).* \(E^\infty_{3,0}=\ker(d^3:\mathbb Z_n\to\Lambda_{\mathbb Z_n})\) must vanish because \(H_3(N)=0\), using \(E_{1,1}=0\). By the coinvariant computation \(\Lambda_{\mathbb Z_n}\cong\mathbb Z^{d-1}\oplus\mathbb Z_n\), an injective \(d^3\) lands onto the torsion summand. Since \(H_2(\mathbb Z_n;\mathbb Z)=0\), \(H_2(N)=\operatorname{coker}d^3\cong\mathbb Z^{d-1}\).
  
  So \(H_3=0\) already implies (c).
- **Determinant.** \(F\to F^*\oplus\mathrm{Ext}(T,\mathbb Z)\) is injective with \(F^*\)-component \(Q_N\). Its cokernel therefore has order \(|\det Q_N|\cdot n\), whatever the \(\mathrm{Ext}\)-component is. That cokernel equals \(\ker(H_1\partial N\to T)\), of order \(dn^2/n\). Hence \(|\det Q_N|=d\), with no need for a "free projection" choice.
- **Transfer.**
  - The invariant lattice has basis \(O_i-O_d\), with \(\frac1n\)-scaled Gram matrix \(-(\delta_{ij}+1)\). This is \(A_{d-1}(-1)\), of determinant \(\pm d\).
  - \(\pi^!\) satisfies \(\pi^!u\cdot\pi^!v=nQ_N(u,v)\), so index \(j\) gives \(|\det Q_N|=dj^2\). Hence \(j=1\), and \(\pi^!\) is onto \(\Lambda^{\mathbb Z_n}\).
  - For \(d=1\) the lattice is zero (Wahl ball), consistently.
- **Charge.** \(c(N)=1-1/(dn^2)\) is topological (ALE Gauss–Bonnet with \(W^+=0\) in the complex orientation), so it is unchanged by residual resolution.

The finite script (102 cases) is a consistency check only. As the note says, its transfer field uses the determinant prediction and is not an independent check.

---

## 4. Theorem 96.K (verified) and one overstatement

**Recomputed.**
- **Costs.**
  - \(D_2\in\{1,\ \tfrac12+\tfrac78,\ \tfrac74\}\) and beyond.
  - \(D_3\): \(\tfrac34\) (Kronheimer) or \(\ge\tfrac{15}{16}\) (Şuvaina \(d=4\)).
  - \(D_a=1-\frac1{4(a-2)}\).
- **Threshold.** \(\beta=k(5y+1)/[18(1+y)]\). For \(k=6\): \(\beta\ge15/16\iff35y\ge29\iff A\ge3675/64\approx57.42\). Ball quotients have \(9\mid A\), so \(A\ge63\).
- **No Wahl points at \(k=6\).**
  - A complex Wahl ball adds \(\ge3/4\), exceeding the remaining budget.
  - A reversed one needs \(\tfrac29(1-1/n^2)\le1-\tfrac{15}{16}\), which is impossible.
- **Block structure.** The roots of an orthogonal sum of definite lattices are the union of the roots of the summands. \(D_{a\ge4}\) is irreducible, and every Şuvaina lattice is of type A. Hence Şuvaina fillers appear only as \(A_1\subset D_2\) (\(d=2\)) or as \(D_3=A_3\) (\(d=4\)).
- **Lattice embedding.** The (L0) embedding uses only that the filler's \(\pi_1\) is finite and that \(X\) is aspherical with torsion-free \(\pi_1\). Both hypotheses are carried in the statement.

**Correction (Step 96 §4).** The note says: "Smooth transfer plus integral topology now decides the Kähler-filler full-absorption sector completely at the level of necessary data". This contradicts §2 of the same note, which lists the index-\(2^q\) prism-manifold linking compatibility as not done. Replace with:

> "…decides it at the level of transferred curvature and lattice-embedding data; the index-\(2^q\) gluing against the prism-manifold linking forms is not examined."

---

## 5. Proposition 98.W and Corollary 98.V: verified, with text corrections

**Proof checks.**
- **(1)** \(K=\oplus n_j\mathbb Z_{n_j^2}\subset\oplus\mathrm{rad}(n_j)\mathbb Z_{n_j^2}=\Phi(G)\). Since \(\ker i+K=G\), it follows that \(i=0\).
  - *Typo:* "Every prime dividing \(n_j\) divides \(n_j\)" should read "every prime dividing \(n_j^2\) divides \(n_j\)".
- **(3)** The chain is \(\mathrm{Tor}H_2W\cong\mathrm{Tor}H^3W\cong\mathrm{Tor}H_1(W,Y)\cong\mathrm{Tor}H_1W\cong\mathrm{Tor}H_1M\cong\mathrm{Tor}H_2M\). It is correct; the \(\mathbb Z^{t-1}\) cokernel is free. The snake lemma gives \(0\to L\to U\to K\to0\).
- **(4)** This step needs \(\mathrm{Ext}(H_1X,\mathbb Z)=0\). That holds only if \(H_1(X)\) is torsion-free, which is *not* implied by \(\pi_1(X)\) being torsion-free. Ball quotients can have torsion in \(H_1\).
- **98.V.**
  - \(v/n\) has order exactly \(n^2\): \(v\) is primitive and \(\gcd(N,n)=1\).
  - Its self-pairing is \(-N/n^2\).
  - A form on a cyclic group is fixed by its value on one generator modulo unit squares, and \(q^{-1}=q\cdot(q^{-1})^2\). So the lens-convention ambiguity is harmless.
  - The construction is *sufficient* for \(k\ge5t\). For \(k<5t\) nothing is proved. The single-coordinate condition "\(\mp(na-1)\) is a unit square mod \(n^2\)" is only a sufficient special case.

**Scope corrections (exact text).** The package §22.6(7) item and the Step-94 binding header are already correctly hedged. The following places are not.

| Location | Current | Replace with |
|---|---|---|
| `state_of_problems_1_4.md` §1 | "realizable for \(k\ge5\) per Wahl point, so it never obstructs" | "realizable for \(k\ge5t\); in that range, and when \(H_1(X)\) is torsion-free, it gives no bilinear obstruction. For \(k<5t\), or with torsion in \(H_1(X)\), it is not examined." |
| `state_of_problems_1_4.md` §5.1 | "Their integral gluing is now settled and carries no bilinear obstruction" | "Index and torsion are settled for torsion-free \(\pi_1(X)\); the discriminant–linking identification needs torsion-free \(H_1(X)\); no bilinear obstruction exists for \(k\ge5t\)." |
| Ledger II (98.W/98.V) | "never obstructs the Wahl channel at the bilinear level" | add "for \(k\ge5t\) and torsion-free \(H_1(X)\)" |
| Package §24.1(4)(e), §24.4 | "nor by the bilinear integral gluing data (98.W, 98.V)" | add "(for \(k\ge5t\), torsion-free \(H_1(X)\))" |
| Step 96 §3, intro and "Consequence for the Wahl sector" | "can always be satisfied once \(k\ge5\) per Wahl point" | add "when \(H_1(X)\) is torsion-free; otherwise the torsion-linking block of \(W\) must be included" |

The Step-94 note's §4 still displays the withdrawn witness \(v=e_1+e_2+e_3+e_4\). The binding header governs it, but an inline pointer at that line would prevent misreading.

---

## 6. ALE decay statements

- **Lemma 86.S needs only some \(\tau>0\) with two derivatives.** The value \(\tau=4\) is not load-bearing, so the attribution affects no conclusion.
- **Şuvaina's Definition 1.1** imposes \(O(r^{-4})\) on \(g\) and \(J\) without derivatives. The package's phrase "records order-four metric decay" is accurate.
- **GH derivative control (A-type, Şuvaina, resolved singular fibres).**
  - The complex dipole moment vanishes by polygon symmetry.
  - The \(b\)-dipole is removed by a translation along the \(b\)-axis, which commutes with the rotation and so is equivariant.
  - The resulting expansion \(V=\frac{dn}{2|x|}(1+O(|x|^{-2}))\), with \(|x|\sim r^2\), gives \(O(r^{-4})\) with all derivatives, and this passes to the free quotient.
- **Kronheimer \(D/E\) fillers.** These need the separate Bando–Kasue–Nakajima input. The supplied materials cannot confirm that the bib key `lidimensional` is that reference; the name suggests otherwise. Check `citation.bib`. If the key is a later restatement, write "BKN, as stated in [key], Def. 1.2/Thm 2.4".

---

## 7. Problem 4 and Armstrong attribution

**Verified.**
- \(E=\Lambda^{0,2}\otimes T^{1,0}\cong S_-\otimes L^{3/2}\), the conjugate of LeBrun's \(\alpha\in S_-\otimes L^{-3/2}\).
- \(c_2(E)=c_2+2c_1^2=5\chi+6\tau=\chi+2(2\chi+3\tau)\ge\chi>0\). This uses Hitchin–Thorpe for \(s\ne0\), which holds in either orientation.
- **Additional primary grounding in the bundle.** LeBrun 2005, Prop. 2.4 (attributed to Armstrong 1997) proves directly that \(s^*=s\) somewhere, i.e. \(\nabla\omega=0\), using \(|\nabla\omega|^2=s^*-s\).
  - Its proof gives \(2\chi+3\tau=c_1^2\) and \(2\chi-3\tau=-9c_1^2\), hence \(5\chi+6\tau=0\). This agrees with AAD Lemma 2.
  - Armstrong 2002 is correctly left unused.

**Corrections.**
1. **Zero count (front matter §4).** "with total signed index \(5\chi+6\tau\)" should read: "if the torsion zeros are isolated, their local indices sum to \(5\chi+6\tau\); in general \(c_2(E)\) is the localized Euler class of the torsion section." With 76.Z (every nondegenerate zero has index \(+1\)): if all zeros are nondegenerate, there are exactly \(5\chi+6\tau\) of them.
2. **Exceptional-curve inequality (front matter §4; package Step-97/98 bullet).**
   - The inequality itself is LeBrun's Cor. 3.2 rearranged. On any \(J\)-holomorphic \(\Sigma\), for AK *Einstein* \(g\) with \(s<0\) constant, \(8\pi c_1\cdot\Sigma\le\int_\Sigma s^*\omega\) gives \(\int_\Sigma|\nabla\omega|^2\omega\ge8\pi c_1\cdot\Sigma+|s|\,\mathrm{Area}(\Sigma)\).
   - But "fixed-\(J\) exceptional curves from Corollary 3.6" overstates the source. Cor. 3.6 gives, for the fixed metric, a possibly singular, possibly disconnected \(J\)-holomorphic curve with \(c_1\cdot\Sigma=+1\), not an embedded \((-1)\)-sphere; embeddedness holds only for generic \(g\).
   - Curves representing each class \(E_i\) come from Cor. 3.5 and need \(b^+\ge2\) (basic classes \(c_1+2E_i\)), as in LeBrun's Theorem B.
   - The sentence should state these hypotheses.

---

## 8. The \(T_{AK}\) statement: reclassify and add the orientation hypothesis

For every Einstein metric, Gauss–Bonnet and the signature formula give, with \(T:=\int(s^2/24-|W^+|^2)\):
\[
s^2V=32\pi^2(2\chi+3\tau)+16T,\qquad 8\pi^2(\chi-3\tau)=T+3\int|W^-|^2 .
\]
Check: \(32\pi^2(2\chi+3\tau)=\int s^2/3+16\int|W^+|^2\) at \(\mathrm{Ric}^\circ=0\).

These are exactly A01's two "consequences of (i)", with \(T_{AK}=T\). So they need no almost-Kähler input once that identification is made. The only nontrivial content of A01's (i) is that the AK-defined \(T_{AK}\) (and \(|s|Q/16-\int|\eta|^2\)) equals \(T\). The canonical-cycle identity (ii) remains genuinely unverified.

**(iii) follows.** The deduction \(T\ge2\pi^2k\) from \(\int s^2\ge32\pi^2A\) (LeBrun 2001, orientation-independent) is correct. It is the inherited bound \(\int|W^+|^2\le\int s^2/24-2\pi^2k\), the general-\(k\) form of package §15 Remark 4.

**The algebra needs \(2\chi+3\tau=A-k\).** This holds only in the orientation of \(M=X\#k\overline{\mathbb{CP}}^2\). Two front-matter sentences therefore need hypotheses:
- "For any almost-complex structure, \(c_1^2=2\chi+3\tau=A-k\)" should read "for any almost-complex structure compatible with the orientation of \(M\)".
- (iii) requires the AK orientation to agree with \(M\)'s. In the reversed orientation \(c_1^2=2\chi-3\tau\), and the bound becomes vacuous.

**Replacement for "[C on (i)]":**

> "(iii) holds for every Einstein metric on \(M\), with the AK orientation equal to that of \(M\), provided \(T_{AK}=\int(s^2/24-|W^+|^2)\). Under that identification it is equivalent to the inherited Einstein bound \(\int|W^+|^2\le\int s^2/24-2\pi^2k\) and adds no new constraint. What remains unchecked is A01's AK-geometric identification in (i), and identity (ii)."

---

## 9. What remains open (unchanged by this verification)

- Completeness of the Şuvaina class in the \((-2)\)-curve case relies on Manetti's Prop. 2.4, which is cited by Şuvaina and not read here.
- The prism-manifold linking compatibility for the \(D\)-blocks of 96.K.
- The torsion-linking block for hosts with \(\mathrm{Tor}\,H_1(X)\ne0\).
- 98.V for \(k<5t\).
- The second-filling chain condition (general-\(k\) 55.5), and the \(w_2\)/spin\(^c\) refinement for even \(n_j\).
- The BKN citation key.
- A01's identities (i) and (ii).

None of these affects the correctness of Lemma 96.Ş on the full Şuvaina class or of Theorem 96.K as necessary conditions.