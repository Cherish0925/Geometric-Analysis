# TTCS Independent Branch Record

```json
{
  "step_id": 97,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step96_suvaina_lattice_and_kahler_filler_theorem.md",
    "Sessions/S1003A02/workspace/scripts/step96_suvaina_lattice.py",
    "Sessions/S1003A02/workspace/data/step96/suvaina_lattice.json",
    "Sessions/S1003A02/workspace/notes/step95_verified_transfer_lattice_thresholds.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/state_of_problems_1_4.md",
    "Sessions/S1003A02/workspace/notes/step58_consolidated_hypothesis_ledger.md",
    "Knowledge/objects/papers/ALE-Ricci-flat-Kahler-metrics-and-deformations-of-quotient-surface-singu--9db598b6c84c--5ab7b434e210/object.md"
  ]
}
```

## Task

Independently verify the mathematics added in Steps 95–96 for the Einstein-gap programme. Focus on the load-bearing scope of Lemma 96.Ş and Theorem 96.K. Read Şuvaina’s full primary source closely: Theorem B says a general non-simply-connected ALE Ricci-flat Kähler surface can be the minimal resolution of a possibly singular fibre, not only a smooth Q-Gorenstein fibre. Decide whether the current assertion that Kronheimer spaces plus the smooth quotient models N_{d,n,m}=M_{d,n}/Z_n are the complete list is correct as written. If not, determine whether H_2=A_{d-1}(-1), the charge, and Theorem 96.K extend to the partially resolved cases, or whether the theorem must be narrowed. Check the deck action on A_{dn-1} homology, boundary pi_1 surjectivity, torsion-freeness, the determinant/index argument, the full-rank D-block classification, placement of non-simply-connected A-type lattices, and the k=6/no-Wahl conclusion. Also read the integrated package/front matter and identify any exact statements that need repair. Give direct mathematical corrections with proof, not generic review.

## Output

# Verification memo: Steps 95–96 (Şuvaina fillers, Lemma 96.Ş, Theorem 96.K)

## Summary

- **The filler list is wrong as written, but the numbers survive.** "Kronheimer spaces plus the smooth quotients \(N_{d,n,m}=M_{d,n}/\mathbb Z_n\)" is not Şuvaina's complete list of Kähler Ricci-flat ALE surfaces. Theorem B also produces \(\mathbb Z_n\)-quotients of minimal resolutions of *singular* invariant fibres, so those cases must be added.
- **These extra cases are \(\mathbb Z_n\)-equivariantly diffeomorphic to \(N_{d,n,m}\).** The proof is in §1. Every topological input of Lemma 96.Ş therefore holds for them.
- **Theorem 96.K needs no narrowing.** Lemma 96.Ş, the filler costs and every number in Theorem 96.K transfer verbatim to the partially resolved cases. Only the sentence describing the list must be rewritten.
- **The other checked items are correct as proved:** the lattice computation, the D-block classification, the \(k\ge6\) bound and the \(k=6\) lone-\(D_6\), no-Wahl conclusion.
- **Several adjacent statements in the package need repair** (§6). The most consequential is the derivative-decay attribution for Kronheimer \(D_a\) fillers in Lemma 86.S.

## 1. What Şuvaina's Theorem B actually gives, and the corrected list

**What the source says.** Theorem B and its proof (end of §4) say the following. \((N,J)\) is the minimal resolution of a fibre \(M^s\) of a one-parameter \(\mathbb Q\)-Gorenstein deformation of \(\mathbb C^2/H\). "If the fiber \(M^s\) has singularities, they must be of the type \(A\)." The universal cover is \(A_{dn-1}\) and the \(\mathbb Z_n\)-action is that of Prop. 2.3.

In §3, Hitchin's data are a GH configuration with \(a_{ij}=-\bar c_i\rho^{-j}\) and \(b_{ij}=b_i\). Coincident \(a\)-values with distinct \(b\)-values give \((-2)\)-curves. So the general non-simply-connected filler is \(N=\widetilde M/\mathbb Z_n\), where:

- \(\widetilde M\) is the GH space on \(dn\) distinct points forming \(d\) regular \(n\)-gons \(\{(b_i,-\bar c_i\rho^{-j})\}\);
- every \(c_i\ne0\), since a centre on the axis would be a fixed point (the origin lies on the fibre exactly when some \(c_i^n=0\));
- the \(c_i^n\) **need not be distinct**. Coincidence \(c_{i'}^n=c_i^n\) is allowed when \(b_{i'}\ne b_i\).

The smooth-fibre models \(M_{d,n}\) are only the stratum where all \(c_i^n\) are distinct.

**Proposition (equivariant topological rigidity).** Every such \(N\) is orientation-preservingly diffeomorphic to the smooth-fibre model \(N_{d,n,m}\), by a diffeomorphism that respects the end chart.

*Proof.*
1. The configuration space is
\[
\mathcal C=\{(b_i,c_i)\in(\mathbb R\times\mathbb C^*)^d:\ \neg(b_i=b_{i'}\ \&\ c_{i'}\in\mu_nc_i)\ \text{for } i\ne i'\}.
\]
It is the complement in a connected \(3d\)-manifold of finitely many submanifolds of real codimension 3 (one real equation for the \(b\)'s, one complex equation for the \(c\)'s). Hence \(\mathcal C\) is connected.
2. \(\mathcal C\) contains the open dense smooth-fibre stratum.
3. Along a path in \(\mathcal C\), the GH total spaces form a smooth family.
4. The deck map \((\theta,b,a)\mapsto(\rho\theta,b,\rho^{-m}a)\) is defined uniformly in the parameter and acts freely.
5. Outside a large ball, the family is the fixed circle bundle of Chern class \(dn\) over \(\mathbb R^3\setminus B_R\).
6. Equivariant Ehresmann therefore gives a \(\mathbb Z_n\)-equivariant trivialization, and it descends to the quotients. \(\square\)

**Consequences.**
- For \(d=1\) there is only one polygon, so no coincidences can occur. The Wahl-ball channel is exactly Prop. 3.3 and is unaffected.
- For \(d\ge2\), an orbit of \(n\) disjoint, freely permuted \((-2)\)-curves descends to one embedded \((-2)\)-sphere in \(N\). Its transfer is \(O_i-O_{i'}\), of norm \(\frac1n(-2n)=-2\): a root of \(A_{d-1}(-1)\). This is a useful consistency check on Lemma 96.Ş.

**Corrected statement for Step 96 §0, package §22.6(7) and front-matter §1.**
> "The non-simply-connected Kähler Ricci-flat ALE surfaces are the \(\mathbb Z_n\)-quotients of minimal resolutions of \(\mathbb Z_n\)-invariant fibres \(xy=\prod_i(z^n-c_i^n)\), \(c_i\ne0\), whose singular points (if any) are of type \(A\) and freely permuted. Each is equivariantly diffeomorphic to \(N_{d,n,m}\); its end is \(\frac1{dn^2}(1,dnm-1)\)."

## 2. Lemma 96.Ş, step by step

**(a) Deck action on \(H_2(\widetilde M)\).** \(H_2(\widetilde M)\) is the sum-zero lattice \(\Lambda\subset\mathbb Z^{dn}\) with form \(-\sum x^2\). This holds for any configuration of distinct points, using arcs that avoid other centres; the class depends only on the endpoints.

The deck generator fixes \(\omega_J\). In Hitchin's coordinates \(b\) is the \(\omega_J\)-moment coordinate, so \(b\mapsto b\). The induced map on \(\mathbb R^3\) is a rotation, and the generator preserves orientation, so the GH circle orientation is also preserved. It therefore maps the sphere over an oriented arc \(p_a\to p_b\) to the sphere over \(gp_a\to gp_b\) with the same orientation. The result is a signless permutation \(p_{ij}\mapsto p_{i,j\pm m}\); the sign convention of \(m\) is immaterial.

**(b) Euler characteristic and Betti numbers.**
- \(\chi(\widetilde M)=dn\), so \(\chi(N)=d\).
- \(H_1(N)\) is finite, so \(b_2(N)=d-1\).
- By Lefschetz duality \(H_3(N)\cong H^1(N,\partial N)=0\): \(H^0(N)\to H^0(\partial N)\) is an isomorphism and \(H^1(N;\mathbb Z)=\mathrm{Hom}(\mathbb Z_n,\mathbb Z)=0\).

**(c) \(\pi_1(\partial N)\to\pi_1(N)\) is onto.** \(\partial\widetilde M\) is connected, and a path from \(x\) to \(gx\) projects to a loop representing \(g\). Hence \(H_1(N,\partial N)=0\). Lefschetz duality and the universal coefficient theorem then give
\[
0=H^3(N)=\mathrm{Hom}(H_3,\mathbb Z)\oplus\mathrm{Ext}(H_2N,\mathbb Z),
\]
so \(H_2(N)\) is torsion-free. Correct.

**(d) Determinant.** In \(F\to F^*\oplus T^*\to H_1\partial N\to T\to0\), write \(L\) for the image of \(F\). Then
\[
0\to T/(T\cap L)\to (F^*\oplus T)/L\to F^*/\pi L\to 0,
\]
and \(T\cap L=0\) because \(L\) injects into \(F^*\). Hence \(|H_1\partial N|=|\det Q_N|\,|T|^2\), so \(dn^2=|\det Q_N|\,n^2\) and \(|\det Q_N|=d\). Correct.

**(e) Index one.**
- \(\Lambda^{\mathbb Z_n}\) consists of the integer combinations \(\sum t_iO_i\) with \(\sum t_i=0\).
- \((O_i-O_d)\cdot(O_j-O_d)=-n(\delta_{ij}+1)\), and dividing by \(n\) gives the Gram matrix of \(A_{d-1}(-1)\), of determinant \(d\).
- \(Q_N=\frac1n\,\pi^!\cdot\pi^!\) on an index-\(j\) sublattice gives \(|\det Q_N|=dj^2\), so \(j=1\). Correct.

**What the script does and does not check.**
- `index_of_transfer_image` is set by comparing \(\det G\) with the predicted value \(d\). That is the same identity being tested, so it is not an independent check of surjectivity of \(\pi^!\); surjectivity rests on (c)–(d).
- The assertion checks only that the coinvariant torsion order divides \(n\). The JSON shows exactly \([n]\) in all 102 cases (\(\sum_{n=2}^7\varphi(n)=17\), times 6 values of \(d\)).
- The Cartan–Leray reading is right: \(E^\infty_{1,1}=E^\infty_{2,0}=0\), so \(H_2(N)=\mathrm{coker}(d^3:\mathbb Z_n\to\Lambda_{\mathbb Z_n})\).

## 3. Filler costs

The cost of a filler is \(\chi-1/|\Gamma|-b_2\). For a Şuvaina filler this is \(d-1/(dn^2)-(d-1)=1-1/(dn^2)\). Every Ricci-flat Kähler surface is locally hyperkähler, hence anti-self-dual and scalar-flat in the complex orientation, so
\[
\int|W^-|^2=8\pi^2\bigl(\chi-1/|\Gamma|\bigr),
\]
and the charges are topological plus the \(\eta\)-invariant of the end. They are identical for partially resolved fillers.

The cost increases in \(n\), so the minima occur at \(n=2\):

| Variant | Cost |
|---|---|
| Şuvaina \(d=2\) | \(7/8\) |
| \(D_2\) blocks | \(1,\ 11/8,\ 7/4\) |
| Şuvaina \(d=4\) | \(15/16>3/4\) |

All of these match the script.

## 4. 95.F: full-rank root systems in \(I_k\)

**Root components.** In an orthogonal sum of even definite lattices, a norm-2 vector lies in a single summand. Each filler lattice is an irreducible root lattice (Kronheimer ADE; Şuvaina \(A_{d-1}\)). So the root-system components are exactly the filler root systems.

**Which components can share coordinates.**
- An \(A_1\) component \(e_1-e_2\) shares coordinates only with \(e_1+e_2\): roots \(e_1\pm e_3\) have inner product \(\pm1\) with it.
- A difference-type \(A_{m-1}\) with \(m\ge3\) shares none. An orthogonal root would need \(x_1=\dots=x_m\) with exactly two entries nonzero, which is impossible.
- A \(D_m\) with \(m\ge3\) shares none either. For a root \(\pm e_i\pm e_j\) with \(i\in S\), choose \(l\in S\setminus\{i,j\}\); then \(e_i\pm e_l\) has inner product \(\pm1\) with it.

**Conclusion.**
- On each support, the restricted system is \(A_{m-1}\) (rank \(m-1\)) or \(D_m\) (rank \(m\)).
- Full rank forces every support to be of type \(D\) and the supports to cover all \(k\) coordinates.
- \(D_2\) is any pair of \(A_1\) fillers (EH or Şuvaina \(d=2\)), and \(D_3\) is an \(A_3\) filler realized on 3 coordinates.
- A Şuvaina \(A_{d-1}\) with \(d=3\) or \(d\ge5\) cannot lie in a full-rank system.
- Each \(D_{a\ge4}\) block is a single Kronheimer \(D_a\) filler.

Correct. The Step-95 sentence "\(D_2\) is exactly the orthogonal EH pair" should read "a pair of orthogonal \(A_1\) fillers".

## 5. The \(k\ge6\), \(k=6\) and no-Wahl conclusions

**Small blocks cannot balance.** With \(k_b=0\), the budget is \(\sum_i(c_i-a_i/6)\le\beta-k/6<0\). The values of \(c-a/6\) are:

| Block | \(c-a/6\) |
|---|---|
| \(D_2\) | \(2/3\) |
| \(D_3\) | \(1/4\) |
| \(D_4\) | \(5/24\) |
| \(D_5\) | \(1/12\) |
| \(D_6\) | \(-1/16\) |

So some block must have \(a\ge6\).

**At \(k=6\).** The only possible partition is a single \(D_6\).

**No Wahl point fits.** The crude budget \(S_{\rm cx}+\frac29S_{\rm rev}\le1\) already forbids every Wahl point:
- a complex-oriented Wahl ball costs at least \(3/4\), and \(15/16+3/4>1\);
- a reversed one needs \(S_{\rm rev}\le9/32\), but its cost \(1-1/n^2\ge3/4\) exceeds that.

**Threshold for \(A\).** With \(r=45/16\), \(y=29/35\) and \(A=18\cdot1225/384=3675/64\), the formula gives \(\beta=15/16\) exactly. Ball quotients have \(A\in9\mathbb Z\), so \(A\ge63\). Verified.

## 6. Exact repairs elsewhere in the package and front matter

**(i) Filler list.** Replace "complete by Şuvaina's classification" and "a complete list" (package §22.6(7) item 96.Ş; §24.1(4)(e); front-matter §1) with the corrected statement in §1, or append "up to \(\mathbb Z_n\)-equivariant diffeomorphism".

**(ii) Lemma 86.S, derivative decay.** The phrase "derivative control follows from the centred finite-centre Gibbons–Hawking formula" covers only \(A\)-type fillers.
- For Şuvaina fillers it holds after a \(b\)-translation to zero centroid. That translation commutes with the deck action, and the \(a\)-centroid is already 0 by symmetry.
- The surviving sector of Theorem 96.K consists of Kronheimer \(D_{a\ge6}\) fillers, which are not GH spaces. Their order-4 decay with derivatives needs a separate source. The standard reference is Bando–Kasue–Nakajima (order-4 ALE structure of Ricci-flat ALE four-manifolds), but it is not among the supplied files and must be retrieved before it is cited.

**(iii) Question 96.W.**
- \(H_2(M_k)\) has torsion \(\cong\mathrm{Tors}\,H_1(X)\) whenever \(\Gamma^{ab}\) has torsion. The "odd unimodular lattice" is \(H_2/\mathrm{Tors}\).
- The asserted index \(n\) is not automatic. From Mayer–Vietoris, using that \(H_1(B)\to H_1(M_k)\) is zero by null-homotopy,
\[
|\mathrm{coker}(H_2W\to H_2M_k)|=n/|i(\ker j)|,
\]
where \(j:H_1\partial B\twoheadrightarrow\mathbb Z_n\) and \(i:H_1\partial B\to H_1W\). The index equals \(n\), and \(\det L=\pm n^2\), exactly when the order-\(n\) metabolizer \(\ker j\) dies in \(H_1(W)\).
- The discriminant form of \(Q_W\) equals the linking form of \(\partial W\) only when \(H_1(W)\) is torsion-free; otherwise it is a subquotient of it.
- The recalled Step-94 witness \(e_1+e_2+e_3+e_4\) requires 4 coordinates of \(-I_k\), not "from \(k\ge3\)", unless \(\langle\pm1\rangle\) summands of \(H_2(X)\) are used. Note also that its orthogonal complement in \(I_4\) is \(A_3\), and that \(\mathbb Zv\oplus A_3\) has index 4, not 2.

**(iv) Unchanged statements.**
- The front-matter Weyl-deficit form \(d/(Y^2/3-2d)\) agrees with package §1 \(d/(P+Y^2/4)\), via \(P=Y^2/12-2d\) at the Yamabe metric.
- (L0), using a null-homotopic \(N_j\to X=B\Gamma\), and (L1), saying a reversed filler of positive rank would carry a positive-definite form inside \(-I_k\), are correct.
- Both are equally valid for partially resolved fillers.

## Net effect

Lemma 96.Ş and Theorem 96.K hold for **all** Kähler Ricci-flat ALE fillers, including the partially resolved Şuvaina quotients. The necessary repairs are to the wording of the filler list, the \(D\)-type decay citation in Lemma 86.S, and the formulation of Question 96.W.