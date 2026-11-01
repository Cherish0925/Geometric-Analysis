# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 97,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step97_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step97_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the mathematics added in Steps 95–96 for the Einstein-gap programme. Focus on the load-bearing scope of Lemma 96.Ş and Theorem 96.K. Read Şuvaina’s full primary source closely: Theorem B says a general non-simply-connected ALE Ricci-flat Kähler surface can be the minimal resolution of a possibly singular fibre, not only a smooth Q-Gorenstein fibre. Decide whether the current assertion that Kronheimer spaces plus the smooth quotient models N_{d,n,m}=M_{d,n}/Z_n are the complete list is correct as written. If not, determine whether H_2=A_{d-1}(-1), the charge, and Theorem 96.K extend to the partially resolved cases, or whether the theorem must be narrowed. Check the deck action on A_{dn-1} homology, boundary pi_1 surjectivity, torsion-freeness, the determinant/index argument, the full-rank D-block classification, placement of non-simply-connected A-type lattices, and the k=6/no-Wahl conclusion. Also read the integrated package/front matter and identify any exact statements that need repair. Give direct mathematical corrections with proof, not generic review.

## Integrated Scientific Memo

# Verification memo: Steps 95–96

## Verdict

**The classification sentence in Step 96 is incorrect as a statement about complex surfaces or metrics.** Şuvaina’s complete list is not just Kronheimer spaces and quotients of **smooth** affine fibres \(M_{d,n}/\mathbb Z_n\). Theorem B explicitly includes minimal resolutions of possibly singular deformation fibres.

**The omitted cases do not invalidate the lattice or curvature conclusions.** Lemma 96.Ş extends to them, with the same lattice, fundamental group, end and charge. After extending that lemma, Theorem 96.K needs no narrowing: its \(D_{\ge6}\), \(k\ge6\), and \(k=6\)/no-Wahl conclusions remain valid under its stated transfer and decay hypotheses.

The material also contains a separate substantive error: **Question 96.W’s unconditional index-\(n\) and discriminant-linking assertions do not follow from the hypotheses.**

## 1. Correct classification and the omitted cases

The relevant distinction is explicit in the supplied primary source:

- **Theorem A:** smooth \(\mathbb Q\)-Gorenstein fibres admit ALE Ricci-flat Kähler metrics.
- **Theorem B:** an arbitrary smooth ALE Ricci-flat Kähler surface is the **minimal resolution of a fibre** of a \(\mathbb Q\)-Gorenstein deformation.
- **End of its proof, §4:** in the non-simply-connected case, the fibre can have residual \(A\)-singularities, which are minimally resolved.
- **§3:** coincident complex parameters \(a_i\), separated by distinct real parameters \(b_i\), produce exceptional \((-2)\)-curves rather than a singular metric.

Thus the correct non-simply-connected class is
\[
N=\widetilde N/\mathbb Z_n,\qquad
\widetilde N=\operatorname{Res}_{\min}
 \left\{xy=\prod_{i=1}^{d}(z^n-c_i^n)\right\},
\]
with \(c_i\ne0\), allowing repeated \(c_i^n\). Its end is
\[
\frac1{dn^2}(1,dnm-1),\qquad (m,n)=1.
\]
The action on the canonical fibre is
\[
(x,y,z)\longmapsto(\rho x,\rho^{-1}y,\rho^m z),
\qquad \rho^n=1,
\]
and lifts to the resolution.

A concrete omitted complex surface is obtained from
\[
xy=(z^2-1)^2,\qquad (x,y,z)\mapsto(-x,-y,-z).
\]
The two \(A_1\)-points are exchanged. Resolve them with invariant Kähler parameters. The lifted action is free, and the quotient has end \(L(8,3)\) and contains a compact holomorphic \((-2)\)-curve. It therefore cannot be biholomorphic to one of the smooth affine quotients in the current statement.

### Why these cases have the same smooth topology

In the Gibbons–Hawking description, the cover has \(dn\) **distinct three-dimensional centres**
\[
p_{ij}=(b_i,c_i\rho^j),\qquad j\in\mathbb Z/n.
\]
Repeated \(c_i^n\) are permitted provided the corresponding \(b_i\) differ. A centre on the rotation axis would be a fixed point of the deck action, so \(c_i\ne0\).

Perturb the \(c_i\) equivariantly so their \(n\)-th powers become distinct, keeping every three-dimensional centre distinct. An equivariant isotopy of the base, compactly supported around the centre orbits, carries the old centres to the new ones. It lifts to the circle bundles, whose Chern numbers around corresponding centres agree, and extends across the Hopf fillings. Consequently the covers, and then their quotients, are orientation-preservingly equivariantly diffeomorphic, with the end identification preserved.

Hence “smooth quotients give the complete list” is false **biholomorphically**, but can be repaired to “they represent all smooth topological types,” with the preceding argument supplied.

## 2. Extended Lemma 96.Ş, with integral proof

**Corrected lemma.** Let \(N\) be any smooth non-simply-connected ALE Ricci-flat Kähler surface in Şuvaina’s classification, including minimal resolutions of singular fibres. Then
\[
\pi_1(N)=H_1(N;\mathbb Z)=\mathbb Z_n,\quad
\chi(N)=d,\quad H_3(N;\mathbb Z)=0,
\]
its large truncation has boundary
\[
Y=L(dn^2,dnm-1),
\]
and
\[
\boxed{(H_2(N;\mathbb Z),Q_N)\cong A_{d-1}(-1).}
\]
In particular \(H_2(N;\mathbb Z)\) is torsion-free. Transfer onto the cover is exactly the full invariant lattice.

Here and below, boundary and duality statements refer to a sufficiently large compact truncation.

### Deck action: no signs

For the \(A_{dn-1}\) cover,
\[
\Lambda=H_2(\widetilde N;\mathbb Z)
 =\left\{x\in\mathbb Z^{dn}:\sum_a x_a=0\right\},
\qquad Q_{\widetilde N}(x,y)=-\sum_a x_ay_a .
\]
A sphere over an oriented path between centres represents \(e_a-e_b\). The deck transformation preserves the circle-fibre orientation and carries the oriented path to its oriented image. Therefore it sends
\[
e_a-e_b\longmapsto e_{ga}-e_{gb},
\]
not its negative. The action is a permutation consisting of \(d\) disjoint \(n\)-cycles. Coincident complex projections do not affect this argument: the three-dimensional centres remain distinct.

### Boundary surjectivity and torsion-freeness

The universal cover has one connected end, by Şuvaina’s Lemma 4.2. Its lifted boundary is therefore connected. A boundary path from \(x\) to \(gx\) projects to a loop representing \(g\), proving
\[
\pi_1(Y)\twoheadrightarrow\pi_1(N).
\]
This also agrees with the end-group extension in Remark 4.3.

Since \(H^1(N;\mathbb Z)=0\) and \(Y\) is connected, the cohomology sequence and Poincaré–Lefschetz duality give
\[
H_3(N)\cong H^1(N,Y)=0.
\]
The homology sequence gives \(H_1(N,Y)=0\). Consequently
\[
H^3(N)\cong H_1(N,Y)=0,
\]
and universal coefficients force
\[
\operatorname{Ext}(H_2(N),\mathbb Z)=0.
\]
Thus \(H_2(N)\) is torsion-free. Also
\[
\chi(N)=\chi(\widetilde N)/n=dn/n=d,\qquad b_2(N)=d-1.
\]

### Determinant and transfer index

Write \(F=H_2(N)\), \(T=H_1(N)=\mathbb Z_n\). The relevant exact sequence is
\[
0\longrightarrow F\longrightarrow H^2(N)
 \longrightarrow H_1(Y)\longrightarrow T\longrightarrow0.
\]
Universal coefficients identify the torsion of \(H^2(N)\) with
\(\operatorname{Ext}(T,\mathbb Z)\), of order \(n\). Projection of the first map to the free quotient is the intersection map \(Q_N:F\to F^*\). Thus
\[
|H_1(Y)|=|\det Q_N|\,|T|^2,
\]
and
\[
dn^2=|\det Q_N|n^2,\qquad |\det Q_N|=d.
\]
The original notation \(T^*\) should mean the finite dual or \(\operatorname{Ext}(T,\mathbb Z)\), **not** \(\operatorname{Hom}(T,\mathbb Z)=0\).

Let \(O_i=\sum_j e_{ij}\). Then
\[
I=\Lambda^{\mathbb Z_n}
 =\left\{\sum_i a_iO_i:\sum_i a_i=0\right\},
\]
and
\[
\frac1nQ_{\widetilde N}(O_i-O_d,O_j-O_d)
 =-(\delta_{ij}+1).
\]
This is \(A_{d-1}(-1)\) with determinant \(d\).

Transfer satisfies
\[
\pi_*\pi^!=n,\qquad
Q_{\widetilde N}(\pi^!u,\pi^!v)=nQ_N(u,v).
\]
It is injective because \(F\) is free. If its image has index \(j\) in \(I\), then
\[
|\det Q_N|=dj^2.
\]
Hence \(j=1\), proving the assertion integrally, including \(d=1\).

The coinvariant calculation also has an unrestricted algebraic proof. Apply group homology to
\[
0\to\Lambda\to\mathbb Z[\mathbb Z_n]^d\to\mathbb Z\to0.
\]
The regular modules have vanishing positive group homology, giving
\[
0\to\mathbb Z_n\to\Lambda_{\mathbb Z_n}
 \to\mathbb Z^{d-1}\to0.
\]
Therefore
\[
\Lambda_{\mathbb Z_n}\cong\mathbb Z^{d-1}\oplus\mathbb Z_n.
\]
The Cartan–Leray \(d^3\) kills this entire torsion summand, by the independently proved torsion-freeness of \(H_2(N)\).

### Charges are unchanged

In the complex orientation, Ricci-flat Kähler implies \(W^+=0\). Gauss–Bonnet gives
\[
\int_N|W^-|^2=8\pi^2\left(d-\frac1{dn^2}\right).
\]
Thus the charges in the programme’s conventions are
\[
C_+(N)=0,\qquad
C_-(N)=-4\left(d-\frac1{dn^2}\right),
\]
with the two interchanged on orientation reversal. The rank-subtracted cost is
\[
\boxed{c(N)=1-\frac1{dn^2}.}
\]
No charge, lattice or cost changes upon resolving residual \(A\)-points.

## 3. Theorem 96.K survives the extension

### Aspherical-host embedding and orientation

For the degree-one pinch \(f:M_k\to X\), every restriction \(f|_{N_j}\) is null-homotopic: its finite fundamental group maps trivially to torsion-free \(\pi_1(X)\), and \(X\) is a \(K(\pi,1)\). Thus filler homology maps into
\[
\ker(f_*:H_2(M_k)/\mathrm{Tor}\to H_2(X)/\mathrm{Tor})
 =-I_k.
\]
The filler intersection form is nondegenerate, so inclusion is injective and isometric on its free homology. Disjoint fillers give orthogonal images.

A positive-rank reversed Kähler filler has positive-definite intersection form, impossible inside \(-I_k\). Hence only rank-zero fillers can be reversed. In the classified family these are Wahl balls.

### Full-rank root classification

Every norm-two vector of \(I_k\) is \(\pm e_i\pm e_j\). The norm-two vectors of the embedded orthogonal sum of root lattices are reflection-closed.

On a connected coordinate support of size \(m\), switch coordinate signs so a spanning tree consists of difference roots. Their reflections generate all coordinate permutations and all difference roots.

- With no sum root, the system is \(A_{m-1}\), of rank \(m-1\).
- With a sum root, permutations and reflections generate every sum and difference, giving \(D_m\), of rank \(m\).

Full rank leaves neither an unused coordinate nor a difference-only support. Therefore
\[
\boxed{\bigoplus_iD_{a_i},\qquad a_i\ge2,\qquad \sum_i a_i=k.}
\]
This proves the unrestricted result rather than extrapolating the finite search. It also excludes the \(E\)-types from every diagonal lattice.

Each \(D_a\) has determinant \(4\), including \(D_2=A_1^2\) and \(D_3=A_3\). For \(q\) blocks, the inclusion has index \(2^q\); it is not generally primitive.

Since a generalized Şuvaina lattice is \(A_{d-1}\), a positive-rank such filler can occur only:

- as one \(A_1\) constituent of \(D_2\), when \(d=2\);
- as an entire \(D_3=A_3\), when \(d=4\).

Every \(D_a\), \(a\ge4\), is irreducible and must be a single Kronheimer \(D_a\) filler. This remains true for partially resolved fibres.

### Costs, threshold and no Wahl points

The minimum costs are
\[
c(D_2)=1,\quad c(D_3)=\frac34,\quad
c(D_a)=1-\frac1{4(a-2)}\quad(a\ge4).
\]
Şuvaina substitutions raise the low-block costs:
\[
D_2:\quad 1,\ \ge\frac{11}{8},\ \ge\frac74;
\qquad
D_3:\quad \frac34,\ \ge\frac{15}{16}.
\]
For ranks \(2,3,4,5\),
\[
c(D_a)-a/6=\frac23,\ \frac14,\ \frac5{24},\ \frac1{12}.
\]
The transferred coarse budget under full absorption is
\[
S_{\rm cx}+\frac29S_{\rm rev}\le k/6.
\]
It follows that some block has rank at least six, and therefore is Kronheimer.

At \(k=6\), the only surviving positive-rank configuration is \(D_6\), with cost \(15/16\). Even the cheapest reversed Wahl point adds \(1/6\), giving
\[
\frac{15}{16}+\frac16=\frac{53}{48}>1.
\]
Thus **no Wahl point of either orientation fits**. The finite-\(A\) condition then has only complex-oriented fillers and is precisely
\[
\frac{15}{16}\le\beta(6,A).
\]
Equality gives
\[
y=\frac{29}{35},\qquad A_{\rm crit}=\frac{3675}{64}.
\]
Since a compact ball quotient has \(A=9\tau\in9\mathbb Z\), the first allowed value is \(63\).

These are necessary conditions, not existence statements.

The Step-95 transfer algebra is also correct:
\[
9x+3T-(\sqrt{8x}+\sqrt{T-x})^2
 =2(\sqrt{T-x}-\sqrt{2x})^2.
\]
It yields the displayed host-general envelope and weighted coarse budget. The finite-\(A\) \(\beta\) formula is exact for the complex-oriented sector. For reversed Wahl additions, the weighted \(\beta\) bound is a necessary envelope, not the sharp mixed-orientation threshold; this distinction does not affect the no-Wahl argument above.

## 4. Question 96.W must be reformulated

Let \(B\) be a Wahl ball, \(Y=\partial B\), and \(W=\overline{M_k\setminus B}\). Mayer–Vietoris gives
\[
0\to H_2(W)\to H_2(M_k)\to H_1(Y)
 \xrightarrow{(i,j)}H_1(W)\oplus H_1(B)\to H_1(M_k)\to0.
\]
Here
\[
H_1(Y)=\mathbb Z_{n^2},\qquad H_1(B)=\mathbb Z_n,\qquad
K=\ker j,\quad |K|=n.
\]
Therefore
\[
\boxed{\operatorname{coker}(H_2(W)\to H_2(M_k))
 \cong K\cap\ker i.}
\]
Its order is a divisor \(r\mid n\), not automatically \(n\). The order equals \(n\) precisely when \(i(K)=0\).

There is an additional torsion distinction. Ball-quotient hypotheses do not imply torsion-free \(H_1(X)\) or \(H_2(X)\). Set
\[
F=H_2(M_k)/\mathrm{Tor},\qquad
L=\operatorname{im}(H_2(W)\to F).
\]
If
\[
t=\left|\frac{\mathrm{Tor}\,H_2(M_k)}
 {\mathrm{Tor}\,H_2(M_k)\cap\operatorname{im}H_2(W)}\right|,
\]
then
\[
[F:L]=r/t,\qquad |\det L|=(r/t)^2.
\]
Thus even the free-lattice index requires torsion bookkeeping.

Nor is the entire discriminant bilinear form automatically anti-isometric to the entire lens-space linking form. That identification holds in a clean case such as torsion-free \(H_1(W)\); otherwise the boundary exact sequence gives the relevant linking **subquotient**, with further torsion data.

The null-homotopy \(B\to X\) remains correct, but does not force \(i(K)=0\). The corrected question should ask for the boundary maps \(i,j\), their kernel intersection, and the torsion data before specializing to index-\(n\) lattices.

Finally,
\[
v=e_1+e_2+e_3+e_4
\]
requires four diagonal coordinates. In \(I_4\),
\[
v^\perp=A_3,\qquad
[I_4:\mathbb Zv\oplus A_3]=4.
\]
It is not, as presently recalled, a witness using only the exceptional kernel “from \(k\ge3\),” and by itself is not a Wahl embedding construction.

## 5. Exact synchronized repairs

1. **Step 96 §0, package §22.6(7), §24.1(4)(e), and front-matter classification wording:** replace the smooth-fibre complete-list assertion by the minimal-resolution formulation in §1 above.

2. **Lemma 96.Ş:** state it for the entire classified non-simply-connected family and use the extended proof above. The theorem’s scope then genuinely covers all Kähler Ricci-flat ALE fillers.

3. **Question 96.W and its summaries in the package/front matter:** remove unconditional index \(n\), determinant \(n^2\), and whole-linking-form claims; replace them with the exact sequence in §4.

4. **Lemma 86.S’s decay attribution:** centred Gibbons–Hawking formulas justify derivative decay for \(A\)-type covers and Şuvaina quotients, including the resolved cases. They do **not** justify it for Kronheimer \(D/E\)-spaces. Those require a separate argument or verified source. Theorem 96.K already assumes derivative-controlled decay, so its conditional proof is unaffected.

5. **Front matter, Problem 2’s optimized Burns coefficient:** append the hypotheses \(\operatorname{Ric}^{\circ}_p=0\) and that \(\zeta\) is an \(R^+_p\)-eigenvector, as required by the package’s Theorem 59.R. General \(P\)-critical insertion uses \(\Phi(\mathrm{Rm}_p,\zeta,K)\), not the displayed optimized eigenvalue formula without qualifications.

6. **Functional notation:** the formula \((4P+L_s)/R\) requires \(R>0\). At \(R=0\), use the original definition, which gives \(\mathscr D=4\).

7. **Computational artifact:** the 102-case certificate correctly checks the permutation-lattice arithmetic. Its transfer-index field uses the topological determinant prediction; it is not an independent computation of transfer. General coverage comes from the proof, not the finite range. Update the script’s classification docstring accordingly.

8. **Literature scope:** Şuvaina’s source classifies the Kähler category only. “No non-Kähler Ricci-flat ALE spaces are known” should be attributed to a separately verified literature survey, or narrowed to “none is supplied in this material.”

**Mathematical outcome:** the central full-absorption obstruction survives intact after a genuine extension of Lemma 96.Ş. The unresolved objects remain compatible integral gluing and a compact negative Einstein orbifold realizing the surviving data. The corrected Wahl question must retain boundary-map and torsion information; its current lattice-only formulation discards precisely the information needed to determine the index.