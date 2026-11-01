# TTCS Independent Branch Record

```json
{
  "step_id": 95,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step94_filler_screen_dichotomy.md",
    "Sessions/S1003A02/workspace/notes/step95_verified_transfer_lattice_thresholds.md",
    "Sessions/S1003A02/workspace/scripts/step95_filler_lattice_screen.py",
    "Sessions/S1003A02/workspace/data/step95/filler_lattice_screen_certificate.json",
    "Sessions/S1003A02/workspace/notes/step93_paired_A1_transfer_review.md"
  ]
}
```

## Task

Independently verify the mathematical substance of Step 95. Focus on (i) the exact supporting-plane identity and derivation of 9C_-+2C_++42k+12(3c2-c1^2)>=0; (ii) the k_b budget and its interpretation as a structural blind direction of smooth transfer; (iii) whether the finite canonical root search really justifies E6/E7/E8 non-embedding in any diagonal lattice, the A_r slot rule, and the classification of full-rank Kronheimer subsystems as sums of D-blocks; and (iv) the exact beta formula and D6/D7/mixed thresholds. Look hard for missing topological assumptions, overextension from bounded computation, or arithmetic errors. Distinguish what is a mathematical theorem from what remains merely a necessary arithmetic/lattice possibility. Return concrete corrections if needed.

## Output

# Scientific verification memo

## 1. Supporting-plane identity and transferred inequality

For
\[
F(x,T)=\bigl(\sqrt{8x}+\sqrt{T-x}\bigr)^2,
\qquad 0\le x\le T,
\]
direct expansion gives
\[
F=T+7x+4\sqrt{2x(T-x)}.
\]
Hence
\[
\begin{aligned}
9x+3T-F
 &=2(T+x)-4\sqrt{2x(T-x)}\\
 &=2\bigl(\sqrt{T-x}-\sqrt{2x}\bigr)^2\ge0.
\end{aligned}
\]
Thus
\[
F(x,T)\le 9x+3T,
\]
with equality exactly when \(T=3x\), including the zero endpoint. This verifies the central identity in Step 95 without appealing to concavity.

For an Einstein orbifold with Einstein constant \(<0\), the curvature ledger gives
\[
0\le x\le T_+^{\rm orb},\qquad x\le T_-^{\rm orb},
\]
and the mixed transfer gives
\[
F(x,T_+^{\rm orb})\ge6A+C_+.
\]
Therefore
\[
6A+C_+
\le F(x,T_+^{\rm orb})
\le9x+3T_+^{\rm orb}
\le9T_-^{\rm orb}+3T_+^{\rm orb}.
\]
Substituting
\[
T_+^{\rm orb}=A-k+C_+,\qquad
T_-^{\rm orb}=4c_2(X)-A+5k+C_-,
\]
one obtains
\[
\begin{aligned}
0
&\le 9(4c_2-A+5k+C_-)+3(A-k+C_+)-(6A+C_+)\\
&=9C_-+2C_++42k+36c_2-12A.
\end{aligned}
\]
Since \(A=c_1^2(X)\),
\[
\boxed{9C_-+2C_++42k+12\bigl(3c_2(X)-c_1^2(X)\bigr)\ge0.}
\]
All coefficients and signs in Step 95 are correct. Equality in this final inequality additionally requires \(x=T_-^{\rm orb}\) and \(T_+^{\rm orb}=3x\).

---

## 2. The \(k_b\) budget and what the transfer does not see

For a ball quotient, \(3c_2-c_1^2=0\). Under the Step-94 hypotheses on known Kähler ALE fillers:

- a complex-oriented filler has
  \[
  c_+=0,\qquad c_-=-4\bigl(\chi-|\Gamma|^{-1}\bigr);
  \]
- an orientation-reversed filler with nonzero \(b_2\) cannot embed into the \(-I_k\) kernel, so the reversed fillers under consideration are rank-zero Wahl spaces;
- for these ALE spaces, \(\chi=1+b_2\).

Writing
\[
k_b=k-\sum_j b_2(N_j),
\]
and
\[
S_{\rm cx}=\sum_{\rm cx}(1-|\Gamma_j|^{-1}),\qquad
S_{\rm rev}=\sum_{\rm rev}(1-n_j^{-2}),
\]
gives
\[
C_-=-4\bigl[(k-k_b)+S_{\rm cx}\bigr],
\qquad
C_+=-4S_{\rm rev}.
\]
Insertion into the transferred inequality yields
\[
0\le6k+36k_b-36S_{\rm cx}-8S_{\rm rev},
\]
or equivalently
\[
\boxed{
S_{\rm cx}+\frac29S_{\rm rev}\le\frac{k}{6}+k_b.
}
\]

For complex-oriented fillers only,
\[
T_-^{\rm orb}
=\frac A3+k+4k_b-4S_{\rm cx}.
\]
Combining this with \(T_-^{\rm orb}\ge x_{\min}\) gives
\[
\boxed{S_{\rm cx}\le k_b+\beta(k,A).}
\]
Thus one rank not represented in the fillers enlarges this particular charge budget by exactly one unit.

Two interpretive refinements are important.

1. **\(k_b\) is a rank count, not a geometric collection of \(k_b\) exceptional spheres in the regular orbifold part.** Torsion at the spherical links can mix the integral lattices. The supplied topology proves only that \(k_b\) is the rank in the blow-up kernel not carried by the ALE pieces.

2. **The blindness belongs to the scalar and mixed LeBrun transfers used here.** These formulas see the placement of blow-up rank only through \(k_b\) and the charge sums. They do not see linking pairings, period-point data for individual classes, or singular-point monopole information. A different class-sensitive estimate could contain additional information.

There is also a concrete correction to the Wahl wording in Step 95. From \(b_2(B_{n,a})=0\), one may conclude that a Wahl filler contributes no rank to \(\sum b_2(N_j)\). It does **not** follow that every configuration containing a Wahl filler has \(k_b>0\). Kronheimer fillers could already contribute total rank \(k\), while additional Wahl fillers contribute only charges; then \(k_b=0\). Consequently:

- a configuration consisting only of Wahl fillers has \(k_b=k\);
- a Wahl point may coexist with a full-rank D-block system at \(k_b=0\);
- a complex-oriented Wahl point adds \(1-n^{-2}\) to the D-block cost;
- an orientation-reversed Wahl point enters with weight \(\frac29(1-n^{-2})\), and then the simple \(\beta\) formula no longer applies because \(C_+\ne0\).

The D-partition tables remain correct for the explicitly stated Kronheimer-only setting.

---

## 3. Root embeddings

### 3.1 Topological input required before the root calculation

The embedding into \(-I_k\) uses more than root arithmetic. It requires:

- \(X\) aspherical with torsion-free \(\pi_1(X)\);
- \(M_k\cong X\#k\overline{\mathbb{CP}}^{\,2}\);
- finite \(\pi_1\) for each ALE filler;
- spherical space-form links, so rational Mayer–Vietoris gives injectivity and orthogonality.

If \(c:M_k\to X=K(\pi_1X,1)\) is the classifying map, then \(c|_{N_j}\) is null-homotopic because its induced fundamental-group image is finite inside a torsion-free group. Hence
\[
H_2(N_j;\mathbb Z)/{\rm tors}\longrightarrow
\ker c_*\cong -I_k
\]
is an isometric injection. These hypotheses are essential for the D-block conclusion.

### 3.2 What the canonical search establishes

After reversing the sign of the form, every norm-two vector in \(I_k\) is
\[
\pm e_i\pm e_j.
\]
The canonical reduction in the script is logically sound:

- signed coordinate permutations send the first simple root to \(e_1-e_2\);
- in a connected breadth-first Dynkin ordering, every new simple root is adjacent to an assigned root;
- therefore it shares an already used coordinate and introduces at most one new coordinate;
- a connected rank-\(r\) embedding uses at most \(r+1\) coordinates;
- the first sign of a newly introduced coordinate may be fixed by flipping that unused coordinate.

Thus the \(E_r\) searches in \(I_{r+1}\) cover embeddings into every larger diagonal lattice. The stored zero-solution searches for \(E_6,E_7,E_8\) therefore do establish their non-embedding, conditional only on the visibly implemented exhaustive enumeration.

The computation for \(A_r\), however, was run only through \(r=12\). That finite run alone does not establish the universal \(A_r\) slot statement, and isolated connected searches do not by themselves handle coordinate sharing among orthogonal components.

### 3.3 A uniform signed-support proof

The universal statements can be supplied by a short root-theoretic argument.

Represent each root \(\pm e_i\pm e_j\) as a signed edge between coordinate vertices \(i,j\). On a coordinate-connected component with \(m\) vertices, switch coordinate signs along a spanning tree so that every tree edge is \(e_i-e_j\).

- If every remaining edge is also of difference type after switching, the reflection closure is
  \[
  A_{m-1}=\{\pm(e_i-e_j)\},
  \]
  of rank \(m-1\).

- If some remaining edge is of sum type \(e_i+e_j\), permutations generated by the tree reflections produce every sum and difference root. The reflection closure is
  \[
  D_m=\{\pm e_i\pm e_j\},
  \]
  of rank \(m\).

The conventions are \(D_2=A_1\oplus A_1\) and \(D_3=A_3\). This proves uniformly that:

1. no \(E_6,E_7,E_8\) root system embeds into any \(I_k\);
2. \(A_2\) needs three coordinates;
3. \(A_3=D_3\) uses three coordinates;
4. every \(A_r\), \(r\ge4\), uses \(r+1\) coordinates;
5. a full-rank root subsystem of \(D_k\) is exactly
   \[
   \boxed{\bigoplus_iD_{a_i},\qquad a_i\ge2,\quad\sum_i a_i=k.}
   \]

This argument also handles the only coordinate-sharing exception relevant here: two orthogonal \(A_1\) roots \(e_i-e_j\) and \(e_i+e_j\) form \(D_2\).

Hence the root conclusions in Step 95 are mathematically correct, but the universal theorem should rest on this signed-support lemma or a standard root-subsystem theorem, rather than on the \(A_2,\ldots,A_{12}\) run.

### 3.4 What the lattice result does not construct

A full-rank D-system is still only an isometric sublattice of \(-I_k\). If there are \(q\) D-blocks, its determinant is \(4^q\) and its index in \(I_k\) is \(2^q\). The scripts do not supply the required discriminant-linking compatibility, a compact complement, an orbifold topology, or an Einstein metric.

The D-block theorem also does not include Şuvaina fillers with \(d\ge2\), because their integral intersection forms were not established in the supplied material.

---

## 4. Exact \(\beta\) formula and thresholds

Let
\[
y=\sqrt{1-\frac{3k}{A}},\qquad A=\frac{3k}{1-y^2},
\]
and
\[
x_{\min}=\frac A{27}(4-y)^2.
\]
Then
\[
\begin{aligned}
\beta(k,A)
&=\frac14\left(\frac A3+k-x_{\min}\right)\\
&=\boxed{\frac{k(5y+1)}{18(1+y)}}.
\end{aligned}
\]
Its derivative with respect to \(y\) is
\[
\frac{2k}{9(1+y)^2}>0.
\]
Thus, for \(A>3k\),
\[
\frac{k}{18}<\beta(k,A)<\frac{k}{6},
\]
with the endpoint values understood as limits. The series is
\[
\frac{\beta}{k}
=\frac16-\frac1{12}\frac{k}{A}
-\frac18\left(\frac{k}{A}\right)^2
-\frac{15}{64}\left(\frac{k}{A}\right)^3
+O\!\left((k/A)^4\right),
\]
so the Step-95 expansion is correct.

For total D-cost \(c\in(k/18,k/6)\), put
\[
r=\frac{18c}{k}.
\]
Solving \(c=\beta(k,A)\) gives
\[
y_{\rm crit}=\frac{r-1}{5-r},
\qquad
A_{\rm crit}=\frac{3k}{1-y_{\rm crit}^2}.
\]
If \(c\ge k/6\), no finite \(A\) satisfies the inequality. If \(c\le k/18\), every \(A>3k\) satisfies this particular arithmetic condition.

The key rows recompute as follows:

\[
\begin{array}{c|c|c|c|c}
\text{blocks} & k & c & y_{\rm crit} & A_{\rm crit}\\ \hline
D_6 & 6 & 15/16 & 29/35 & 3675/64\\
D_7 & 7 & 19/20 & 101/179 & 32041/1040\\
D_3\oplus D_8 & 11 & 41/24 & 79/97 & 9409/96\\
D_4\oplus D_7 & 11 & 73/40 & 437/443 & 196249/160\\
D_2\oplus D_{10} & 12 & 63/32 & 125/131 & 51483/128
\end{array}
\]

Their decimal values and first multiples of nine are:

\[
\begin{array}{c|c|c}
\text{blocks} & A_{\rm crit}\text{ approximately} &
\min\{A\in9\mathbb Z:A>3k,\ A\ge A_{\rm crit}\}\\ \hline
D_6 & 57.421875 & 63\\
D_7 & 30.808654 & 36\\
D_3\oplus D_8 & 98.010417 & 99\\
D_4\oplus D_7 & 1226.55625 & 1233\\
D_2\oplus D_{10} & 402.210938 & 405
\end{array}
\]

These values agree with the certificate. In particular, the Step-94 estimates for \(D_6\) and \(D_7\) were only asymptotic approximations; Step 95 supplies the correct finite-\(A\) values.

For a compact ball quotient,
\[
A=3c_2,\qquad \tau=\frac{A}{9}\in\mathbb Z,
\]
so \(A\in9\mathbb Z\). The entries \(63,36,\ldots\) are merely the first multiples of nine satisfying the arithmetic inequalities; they do not assert the existence of ball quotients with those Chern numbers.

The partition enumeration is exact for \(2\le k\le40\), with 16,049 passing D-partitions in that interval. The formulas are valid for arbitrary \(k\), but the stored enumeration stops at \(40\). The first full-rank row at \(k=6\) and the first mixed rows at \(k=11\) are nevertheless established because every smaller partition was enumerated and the small-block inequality
\[
c(D_a)>\frac a6,\qquad 2\le a\le5,
\]
also proves that some block \(D_a\), \(a\ge6\), is necessary.

## 5. Mathematical status

The following are established conditional results:

- the supporting-plane identity and the transferred curvature inequality;
- the \(k_b\) charge budget under the stated Kähler ALE and ball-quotient hypotheses;
- the universal ADE-to-diagonal classification once the signed-support argument is included;
- the exact \(\beta\) formula and all displayed D-block thresholds.

A passing D-row supplies only necessary curvature and lattice data. It does not supply a compact orbifold, a compatible complement, an Einstein metric, or a sequence relevant to the Einstein-gap infimum. Rank-zero Wahl additions and Şuvaina \(d\ge2\) fillers require separate arithmetic and topology from the pure Kronheimer D-partition table.