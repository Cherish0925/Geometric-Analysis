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

# Scientific verification memo: Steps 95–96

## 1. Main finding

The sentence in Step 96 §0 that all non-simply-connected ALE Ricci-flat Kähler surfaces are the smooth quotients
\[
N_{d,n,m}=M_{d,n}/\mathbb Z_n
\]
is not correct as written.

Şuvaina’s Theorem A concerns smooth \(\mathbb Q\)-Gorenstein fibres. Theorem B is strictly broader: a general ALE Ricci-flat Kähler surface can be the **minimal resolution of a singular fibre**. In the non-simply-connected case, its universal cover is the minimal resolution of a possibly singular \(A_{dn-1}\)-fibre, and the cyclic action is the one induced from Proposition 2.3. The last paragraph of the proof of Theorem B states explicitly that residual singularities can occur and are of \(A\)-type.

These extra spaces are omitted by the displayed smooth affine model. They introduce no new lattice or curvature cost, however. Lemma 96.Ş extends to all of them, and with that extension Theorem 96.K remains valid for every ALE Ricci-flat Kähler filler classified by Şuvaina.

A concrete omitted example is
\[
xy=(z^2-1)^2,\qquad
(x,y,z)\longmapsto(-x,-y,-z).
\]
The fibre has two \(A_1\) points, at \(z=\pm1\), exchanged by \(\mathbb Z_2\). The action lifts freely to the minimal resolution. Its quotient is an ALE Ricci-flat Kähler surface with end \(L(8,3)\), \(H_1=\mathbb Z_2\), and \(H_2\cong A_1(-1)\). It contains a compact holomorphic exceptional curve and is therefore not one of the smooth affine quotients used in Step 96 §1.

---

## 2. Corrected form of Lemma 96.Ş

### Generalized lemma

Let \(N\) be any smooth, non-simply-connected ALE Ricci-flat Kähler surface. Then there are integers
\[
d\ge1,\qquad n\ge2,\qquad (m,n)=1,
\]
such that:

1. \(\pi_1(N)=H_1(N)=\mathbb Z_n\);
2. the end is
   \[
   \frac1{dn^2}(1,dnm-1),
   \qquad
   Y=\partial N_R=L(dn^2,dnm-1)
   \]
   for a sufficiently large compact truncation \(N_R\);
3. the universal cover \(\widetilde N\) is an \(A_{dn-1}\) Kronheimer space, possibly the minimal resolution of a singular deformation fibre;
4.
   \[
   \chi(N)=d,\qquad H_3(N;\mathbb Z)=0;
   \]
5.
   \[
   \boxed{(H_2(N;\mathbb Z),Q_N)\cong A_{d-1}(-1)}
   \]
   with no torsion;
6. the transfer
   \[
   \operatorname{tr}:H_2(N;\mathbb Z)\longrightarrow H_2(\widetilde N;\mathbb Z)
   \]
   maps onto the full \(\mathbb Z_n\)-invariant lattice.

### Proof of the deck action

Şuvaina’s Gibbons–Hawking description gives \(dn\) centres arranged as \(d\) regular \(n\)-gons:
\[
p_{i,j}=(b_i,c_i\rho^j),\qquad
1\le i\le d,\quad j\in\mathbb Z/n.
\]
For a singular complex fibre, some \(c_i^n\) coincide. The corresponding resolution parameters separate the centres in the \(b\)-direction. Thus the Gibbons–Hawking centres remain distinct even when the canonical complex fibre is singular.

The deck generator rotates the complex plane and the circle fibre:
\[
p_{i,j}\longmapsto p_{i,j+m}.
\]
It preserves the orientation of the base path and of the circle fibre. Hence on
\[
\Lambda=H_2(\widetilde N;\mathbb Z)
 =\left\{(x_{i,j})\in\mathbb Z^{dn}:\sum_{i,j}x_{i,j}=0\right\},
\qquad
Q_{\widetilde N}(x,x)=-\sum x_{i,j}^2,
\]
the action is the unsigned permutation of \(d\) disjoint \(n\)-cycles. This remains true for the partially resolved fibres.

Put
\[
O_i=\sum_{j=0}^{n-1}e_{i,j}.
\]
The invariant lattice is
\[
I=\Lambda^{\mathbb Z_n}
 =\left\{\sum_i a_iO_i:\sum_i a_i=0\right\},
\]
with basis \(u_i=O_i-O_d\), \(1\le i<d\). Its scaled form is
\[
\frac1nQ_{\widetilde N}(u_i,u_j)=-(\delta_{ij}+1).
\]
This is \(A_{d-1}(-1)\), written in the basis \(e_i-e_d\), and has determinant \(d\).

### Integral topology

Since \(\widetilde N\) is simply connected and the action is free,
\[
\pi_1(N)=\mathbb Z_n,\qquad \chi(N)=\frac{\chi(\widetilde N)}n
=\frac{dn}{n}=d.
\]

The cohomology sequence for \((N_R,Y)\) gives
\[
H_3(N_R)\cong H^1(N_R,Y)=0,
\]
because \(H^0(N_R)\to H^0(Y)\) is an isomorphism and
\[
H^1(N_R;\mathbb Z)=\operatorname{Hom}(\mathbb Z_n,\mathbb Z)=0.
\]

The lifted end link is connected. Therefore the monodromy of
\[
\partial\widetilde N_R\longrightarrow Y
\]
surjects onto \(\mathbb Z_n\), equivalently
\[
H_1(Y)\longrightarrow H_1(N_R)=\mathbb Z_n
\]
is onto. Thus \(H_1(N_R,Y)=0\). Poincaré–Lefschetz duality and universal coefficients give
\[
0=H^3(N_R)\supset
\operatorname{Ext}(H_2(N_R),\mathbb Z),
\]
so \(H_2(N_R)\) has no torsion.

Let \(F=H_2(N_R)\) and \(T=H_1(N_R)=\mathbb Z_n\). The exact sequence
\[
0\longrightarrow F\longrightarrow H^2(N_R)
\longrightarrow H_1(Y)\longrightarrow T\longrightarrow0
\]
and
\[
\operatorname{tors}H^2(N_R)\cong\operatorname{Ext}(T,\mathbb Z)\cong\mathbb Z_n
\]
give
\[
|H_1(Y)|=|\det Q_N|\,|T|^2.
\]
Since \(|H_1(Y)|=dn^2\),
\[
|\det Q_N|=d.
\]

Transfer is injective because
\[
\pi_*\operatorname{tr}=n
\]
and \(F\) is free. If \(\operatorname{tr}F\) had index \(j\) in \(I\), then
\[
|\det Q_N|=d\,j^2.
\]
Since \(|\det Q_N|=d\), one obtains \(j=1\). This proves both the lattice identification and surjectivity onto \(I\).

### Curvature cost

The end group has order \(dn^2\), while
\[
\chi(N)=d,\qquad b_2(N)=d-1.
\]
Consequently the complex-oriented filler cost used in Steps 95–96 is always
\[
\chi(N)-\frac1{dn^2}-b_2(N)
 =1-\frac1{dn^2}.
\]
Partial resolution changes neither this number nor the integral lattice.

---

## 3. Effect on Theorem 96.K

No narrowing of Theorem 96.K is mathematically necessary. Its proof becomes complete after replacing the smooth-fibre version of Lemma 96.Ş by the generalized lemma above.

### Full-rank root classification

After reversing the sign of the form, every root in \(I_k\) is
\[
\pm e_i\pm e_j.
\]
For a connected coordinate support, switch coordinate signs along a spanning tree so that all tree roots are differences.

* If every root is a difference, reflections generate all \(e_i-e_j\), giving \(A_{m-1}\), of rank \(m-1\) on \(m\) coordinates.
* If one sum root occurs, reflections generate all sums and differences, giving \(D_m\), of rank \(m\).

For a root system of rank \(k\) inside \(I_k\), every difference-only component loses one rank relative to the number of coordinates it uses. Therefore a full-rank system has no \(A\)-component and no unused coordinate:
\[
R=\bigoplus_\nu D_{a_\nu},\qquad \sum_\nu a_\nu=k.
\]
This also proves the index statement:
\[
\det\!\left(\bigoplus_\nu D_{a_\nu}\right)=4^q,
\qquad
[I_k:\textstyle\bigoplus_\nu D_{a_\nu}]=2^q,
\]
where \(q\) is the number of blocks.

### Placement of non-simply-connected fillers

Every generalized Şuvaina filler still has lattice \(A_{d-1}\). Hence:

* \(d=2\): \(A_1\), usable only as one summand of
  \[
  D_2=A_1\oplus A_1;
  \]
* \(d=4\): \(A_3=D_3\), usable as an entire \(D_3\) block;
* all other \(d>1\): incompatible with a full-rank \(D\)-block decomposition.

For \(a\ge4\), \(D_a\) is irreducible and is not isometric to any \(A_r\). Thus every such block must be a single Kronheimer \(D_a\) filler. Singular fibres do not change this conclusion.

### Costs and the first possible rank

The least costs are
\[
c(D_2)=1,\qquad c(D_3)=\frac34,\qquad
c(D_a)=1-\frac1{4(a-2)}\quad(a\ge4).
\]
A generalized Şuvaina substitution has the same cost as in Step 96:
\[
1-\frac1{dn^2}.
\]
Thus
\[
c(D_2)\ge1,\quad
c(D_3)\ge\frac34,\quad
c(D_4)=\frac78,\quad
c(D_5)=\frac{11}{12},
\]
and each is strictly larger than its rank divided by \(6\). Since
\[
\beta(k,A)<\frac{k}{6}
\]
for finite \(A\), every surviving full-rank configuration contains a \(D_a\) block with \(a\ge6\). Therefore
\[
k\ge6.
\]

At \(k=6\), all partitions other than \(D_6\) use only blocks of rank at most five and are excluded. The \(D_6\) cost is
\[
c(D_6)=\frac{15}{16}.
\]
A complex-oriented Wahl ball costs at least \(3/4\); an oppositely oriented one has effective cost at least
\[
\frac29\cdot\frac34=\frac16.
\]
Even the latter gives
\[
\frac{15}{16}+\frac16=\frac{53}{48}>1>\beta(6,A),
\]
so no Wahl point can accompany the \(D_6\) filler.

Solving
\[
\beta(6,A)=\frac{15}{16}
\]
gives
\[
y=\frac{29}{35},\qquad
A=\frac{18}{1-(29/35)^2}
=\frac{3675}{64}.
\]
For a compact ball quotient, \(A=9\tau\in9\mathbb Z\), so the first possible value is \(A=63\). The \(k=6\), lone-\(D_6\), no-Wahl conclusion is therefore correct.

---

## 4. The Wahl gluing formulation also needs repair

Question 96.W begins with an index-\(n\) statement that is not automatic.

Let
\[
Y=\partial B=L(n^2,na-1),\qquad W=\overline{M\setminus B}.
\]
Mayer–Vietoris gives
\[
0\longrightarrow H_2(W)\longrightarrow H_2(M)
\longrightarrow H_1(Y)
\xrightarrow{(\phi_W,\phi_B)}
H_1(W)\oplus H_1(B)
\longrightarrow H_1(M)\longrightarrow0.
\]
For a Wahl ball,
\[
H_1(Y)=\mathbb Z_{n^2},\qquad H_1(B)=\mathbb Z_n,
\]
and \(\phi_B\) is onto. Put
\[
K_B=\ker\phi_B,\qquad |K_B|=n.
\]
Then
\[
\operatorname{coker}\bigl(H_2(W)\to H_2(M)\bigr)
\cong K_B\cap\ker\phi_W.
\]
Hence its order is some divisor \(r\mid n\), not automatically \(n\). In the torsion-free lattice setting the image has index \(r\), with determinant \(r^2\). Index \(n\) is equivalent to
\[
\phi_W(K_B)=0.
\]

The null-homotopy of \(B\to X\) is correct: \(X\) is aspherical and every homomorphism from the finite group \(\pi_1(B)\) to the torsion-free group \(\pi_1(X)\) is trivial. But this does not imply \(\phi_W(K_B)=0\).

Likewise, identifying the full discriminant bilinear form with the lens-space linking form requires the clean torsion situation in which the relevant end-link sequence realizes the entire discriminant group. With torsion in \(H_1(W)\) or \(H_2(M)\), extra finite-group data enter. Question 96.W should therefore be posed first in terms of the exact sequence above, asking which subgroups
\[
K_B\cap\ker\phi_W\subseteq\mathbb Z_n
\]
occur, and only then specializing to the index-\(n\) case.

---

## 5. Text and artifact repairs

The following locations need synchronized wording.

1. **`step96_suvaina_lattice_and_kahler_filler_theorem.md`, §0**  
   Replace the asserted complete list by:
   > Every non-simply-connected ALE Ricci-flat Kähler surface is the quotient by \(\mathbb Z_n\) of the minimal resolution of a possibly singular \(A_{dn-1}\) deformation fibre. The smooth quotients \(M_{d,n}/\mathbb Z_n\) form the smooth-fibre subfamily.

2. **Lemma 96.Ş**  
   State it for every surface in the preceding generalized class, not only for a smooth affine Milnor fibre.

3. **Theorem package §22.6(7), §24.1(4), §24.4; `state_of_problems_1_4.md`; `step58_consolidated_hypothesis_ledger.md`**  
   Replace “\(N_{d,n,m}=M_{d,n}/\mathbb Z_n\), complete by Şuvaina” by the minimal-resolution formulation. The lattice, cost, and \(D_{\ge6}\) conclusions remain unchanged.

4. **Question 96.W and its package summaries**  
   Replace the unconditional index-\(n\) and full linking-form statements by the Mayer–Vietoris formulation above.

5. **Python certificate**  
   `step96_suvaina_lattice.py` correctly evaluates the permutation lattice in the 102 listed cases. Its `saturated` field tests primitivity of the displayed columns in \(\mathbb Z^{dn}\); equality with the full invariant lattice comes from the orbit description, not from that Smith computation alone. Likewise `index_of_transfer_image` uses the topological determinant formula. The script is valid consistency data, while the general theorem rests on the analytic argument above.

6. **Statement about Ricci-flat ALE metrics lacking a Kähler structure**  
   Şuvaina’s paper classifies ALE Ricci-flat **Kähler** surfaces only. Any statement about the literature for ALE Ricci-flat metrics without a Kähler structure needs a separate source.

In summary: the smooth-model classification sentence is too narrow, but the load-bearing lattice and cost formulas extend to the omitted partially resolved fibres. After that repair, the \(D\)-block reduction, the necessity of a Kronheimer \(D_{a\ge6}\) filler, and the exact \(k=6\) conclusion remain mathematically intact.