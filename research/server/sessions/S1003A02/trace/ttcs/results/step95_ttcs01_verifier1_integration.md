# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 95,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step95_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step95_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the mathematical substance of Step 95. Focus on (i) the exact supporting-plane identity and derivation of 9C_-+2C_++42k+12(3c2-c1^2)>=0; (ii) the k_b budget and its interpretation as a structural blind direction of smooth transfer; (iii) whether the finite canonical root search really justifies E6/E7/E8 non-embedding in any diagonal lattice, the A_r slot rule, and the classification of full-rank Kronheimer subsystems as sums of D-blocks; and (iv) the exact beta formula and D6/D7/mixed thresholds. Look hard for missing topological assumptions, overextension from bounded computation, or arithmetic errors. Distinguish what is a mathematical theorem from what remains merely a necessary arithmetic/lattice possibility. Return concrete corrections if needed.

## Integrated Scientific Memo

# Step 95 verification: correct algebra and thresholds, with scope corrections

**The supporting-plane identity, charge coefficients, exact \(\beta\), and displayed \(D\)-block thresholds are correct.** The canonical search genuinely proves \(E_6,E_7,E_8\) non-embedding in every standard diagonal lattice. Two substantive repairs are needed:

1. The universal \(A_r\) slot rule and full-rank \(D\)-block classification need a structural proof, not extrapolation from the \(r\le12\) computation. Such a proof is supplied below.
2. The statements that every Wahl configuration has \(k_b>0\), and that retained-rank configurations are categorically beyond smooth transfer, are too strong.

The geometric conclusions remain conditional on the supplied resolution/transfer lemmas. Passing the screen is not a construction.

## 1. Supporting plane and host inequality

On \(0\le x\le T\),
\[
F(x,T)=T+7x+4\sqrt{2x(T-x)}.
\]
Consequently,
\[
\boxed{
9x+3T-F(x,T)
=2\bigl(\sqrt{T-x}-\sqrt{2x}\bigr)^2.
}
\]
Equality is exactly \(T=3x\), including \((x,T)=(0,0)\).

For the Einstein bulk, the supplied curvature and mixed-transfer statements give
\[
6A+C_+\le F(x,T_+^{\rm orb}),\qquad
x\le T_-^{\rm orb}.
\]
Thus
\[
6A+C_+
\le F(x,T_+^{\rm orb})
\le9x+3T_+^{\rm orb}
\le9T_-^{\rm orb}+3T_+^{\rm orb}.
\]
Using
\[
T_+^{\rm orb}=A-k+C_+,\qquad
T_-^{\rm orb}=4c_2-A+5k+C_-,
\]
gives
\[
\boxed{
9C_-+2C_++42k+12(3c_2-c_1^2)\ge0.
}
\]
There is no sign or coefficient error.

This is a **necessary tangent-envelope inequality**, not the entire transferred screen. Equality requires equality in every preceding step: mixed transfer, the \(L^2\) triangle/Cauchy–Schwarz estimate producing \(F\), \(T_+^{\rm orb}=3x\), and \(x=T_-^{\rm orb}\). In particular, it implies \(I_-=0\). These equality requirements should not be inferred merely from passing the inequality.

The geometric input is not independently reproved by Step 95: it uses the smooth scalar/mixed inequalities on \(X\#k\overline{\mathbb{CP}}^2\) and the decay-controlled ALE resolution convergence stated in Steps 93–94. Within those supplied hypotheses, the derivation is sound. The scalar transfer forces the Einstein scalar curvature to be negative because \(A>0\).

## 2. Topological hypotheses and the meaning of \(k_b\)

The diagonal lattice restriction requires:

- \(X\) aspherical with torsion-free \(\pi_1(X)\);
- an **orientation-preserving** identification of the resolved manifold with \(X\#k\overline{\mathbb{CP}}^2\);
- finite fundamental group for each filler;
- rational-homology-sphere links.

Choose the pinch/classifying map \(c:M_k\to X\). Its restriction to a filler is null-homotopic: the induced fundamental-group image is finite in a torsion-free group, and \(X\) is a \(K(\pi,1)\). Rational Mayer–Vietoris supplies injectivity and orthogonality of the filler homology. Passing to free integral homology therefore gives an isometric injection
\[
\bigoplus_j H_2(N_j;\mathbb Z)/{\rm tors}
\hookrightarrow
\ker c_*\cong -I_k.
\]
No primitivity of this injection follows or is needed.

These assumptions justify exclusion of reversed Kähler fillers with positive \(b_2\). They do **not** hold for arbitrary general-type hosts, where filler classes can involve host homology.

For the known Kähler fillers, \(\chi(N_j)=1+b_2(N_j)\). Set
\[
k_b=k-\sum_jb_2(N_j),\quad
S_{\rm cx}=\sum_{\rm cx}(1-|\Gamma_j|^{-1}),\quad
S_{\rm rev}=\sum_{\rm rev}(1-n_j^{-2}).
\]
On a ball quotient,
\[
C_-=-4[(k-k_b)+S_{\rm cx}],\qquad C_+=-4S_{\rm rev},
\]
and hence
\[
\boxed{
S_{\rm cx}+\frac29S_{\rm rev}\le\frac k6+k_b.
}
\]
The coefficient of \(k_b\) is exactly one. For complex-oriented fillers alone,
\[
T_-^{\rm orb}=\frac A3+k+4k_b-4S_{\rm cx},
\]
so the sharper finite-\(A\) condition becomes
\[
\boxed{S_{\rm cx}\le k_b+\beta(k,A).}
\]

### Necessary interpretive corrections

**\(k_b\) is a rank deficit, not a collection of exceptional spheres in the regular bulk.** It counts the rank of the blow-up kernel not represented by filler homology. Integral gluing may mix classes through finite-index lattices. It does not establish that particular \(E_i\), or embedded exceptional spheres, survive in the regular locus.

**The structural blindness is limited to information discarded by these aggregate scalar/mixed estimates.** They contain no class-by-class periods, linking information, or singular monopole data. But they can still exclude configurations with \(k_b>0\). For example, four EH fillers occupying two \(D_2\) coordinate blocks, with \(k=5\) and \(k_b=1\), have
\[
S_{\rm cx}=2>\frac56+1.
\]
Thus retained rank does not guarantee passage.

Conversely, “blindness holds only when the number of fillers is at most \(k_b\)” is also incorrect. That count is merely a sufficient condition for automatic passage of the displayed **charge budgets**, since each individual cost is less than one. Many configurations with more fillers also pass. The exact tests are the weighted budget and, when \(C_+=0\), the \(\beta\) budget. With reversed fillers, one must additionally check the full scalar/domain and mixed feasibility conditions involving \(T_+^{\rm orb}\).

**A Wahl filler does not imply \(k_b>0\).** Its \(b_2=0\) means only that it contributes no absorbed rank.

- A configuration consisting only of Wahl fillers has \(k_b=k\).
- A full-rank Kronheimer system can coexist, arithmetically, with additional Wahl fillers while retaining \(k_b=0\).
- Complex-oriented Wahl additions increase \(S_{\rm cx}\), leaving \(C_+=0\), so the same \(\beta\) formula applies with the enlarged cost.
- Reversed Wahl additions change \(C_+\); the displayed pure-complex \(\beta\) formula then no longer applies.

Whether such combinations exist topologically is separate. Step 95 should replace “every Wahl channel lies in precisely this blind direction” with the rank-zero statement above. Also, for pure complex Wahl configurations, \(S_{\rm cx}\le7k/6\) is only the tangent test; the sharper test in \(A>3k\) is
\[
S_{\rm cx}\le k+\beta(k,A)<7k/6.
\]

## 3. Root search: exhaustive E-test, repaired universal classification

Here “diagonal lattice” must mean the **standard integral unimodular lattice \(I_k\)**, or \(-I_k\) after changing signs—not an arbitrary diagonal form.

### Why the finite E-search covers every ambient dimension

Every norm-two integral vector in \(I_k\) is \(\pm e_i\pm e_j\). The script’s canonicalization is valid:

1. Signed permutations send the first simple root to \(e_1-e_2\).
2. In the connected breadth-first ordering, each added simple root has inner product \(-1\) with an assigned root.
3. Such roots share exactly one coordinate, so an added root introduces at most one new coordinate.
4. New coordinates can be assigned consecutive labels and their first signs fixed by sign flips that preserve all earlier roots.

A connected rank-\(r\) simple system therefore uses at most \(r+1\) coordinates. Searching \(I_{r+1}\) exhausts embeddings into all \(I_k\). Inspection of `candidate_roots` and `embedding_search` shows that the code implements this reduction without further unjustified pruning.

Thus the certificate’s negative E-searches establish the claimed non-embedding, rather than merely testing bounded ambient dimensions. Their identical counters are consistent with a common obstruction on the \(E_6\) subdiagram.

### Uniform proof replacing extrapolation of the A-tests

The \(A_r\) computations stop at \(r=12\). Alone they do not prove the universal slot rule or account for coordinate sharing between orthogonal components. Both issues admit an elementary signed-support proof.

Take the image root set of an ADE lattice and draw a signed edge for each root \(\pm e_i\pm e_j\), joining its coordinate supports. The image root set is reflection-closed: root reflections in the source become the corresponding integral reflections in \(I_k\).

On each connected coordinate-support component with \(m\) vertices, switch coordinate signs along a spanning tree so its tree roots are differences \(e_i-e_j\). Their reflections generate all coordinate permutations on that component.

- If all roots are differences after switching, reflection closure is exactly
  \[
  A_{m-1}=\{\pm(e_i-e_j):i\ne j\},
  \]
  of rank \(m-1\).
- If a sum root \(e_i+e_j\) occurs, those permutations generate all sum roots as well, giving exactly
  \[
  D_m=\{\pm e_i\pm e_j:i\ne j\},
  \]
  of rank \(m\).

The low-rank conventions are \(D_2=A_1\oplus A_1\) and \(D_3=A_3\). This proves, for every rank:

\[
\begin{array}{c|c}
\text{irreducible system}&\text{minimum coordinates}\\ \hline
A_1&2\\
A_2&3\\
A_3&3\\
A_r,\ r\ge4&r+1\\
D_r,\ r\ge4&r
\end{array}
\]
and excludes all E-types.

It also proves the full-rank classification. Every difference-only support component loses one rank relative to its coordinates; unused coordinates lose rank as well. Therefore a root subsystem of total rank \(k\) in \(I_k\) has only \(D\)-support components:
\[
\boxed{
R\cong\bigoplus_iD_{a_i},\qquad a_i\ge2,\qquad \sum_i a_i=k.
}
\]
This handles coordinate sharing: the exceptional sharing is precisely the orthogonal EH pair \(e_i-e_j,e_i+e_j\), forming \(D_2\).

**The universal lattice conclusions are correct once this proof is included.** The bounded A-search should be described as corroboration, not their general proof.

Full rank does not mean equality with \(I_k\). For \(q\) blocks the determinant is \(4^q\), and the index is \(2^q\). Boundary linking, integral gluing, and smooth realizability remain additional constraints.

## 4. Exact \(\beta\), thresholds, and the wall

For complex-oriented fillers, \(C_+=0\). Since
\[
\max_{0\le x\le A-k}F(x,A-k)=9(A-k),
\]
mixed feasibility requires \(A\ge3k\). The lower root of \(F=6A\) is
\[
x_{\min}=\frac A{27}\left(4-\sqrt{1-\frac{3k}{A}}\right)^2.
\]
It lies on the increasing branch and is at least \(A/3\).

Writing \(y=\sqrt{1-3k/A}\),
\[
\boxed{
\beta(k,A)
=\frac14\left(\frac A3+k-x_{\min}\right)
=\frac{k(5y+1)}{18(1+y)}.
}
\]
Moreover,
\[
\frac{d\beta}{dy}=\frac{2k}{9(1+y)^2}>0,
\]
and
\[
\frac{\beta}{k}
=\frac16-\frac{k}{12A}-\frac18\left(\frac{k}{A}\right)^2
-\frac{15}{64}\left(\frac{k}{A}\right)^3
+O((k/A)^4).
\]
All displayed coefficients are correct.

For a total cost \(c\in(k/18,k/6)\), the exact threshold is
\[
r=\frac{18c}{k},\qquad
y_{\rm crit}=\frac{r-1}{5-r},\qquad
\boxed{A_{\rm crit}=\frac{3k}{1-y_{\rm crit}^2}.}
\]
Costs \(c\ge k/6\) fail at every finite \(A\); costs \(c\le k/18\) pass this arithmetic test throughout \(A\ge3k\).

The key certificate rows check exactly:

| Configuration | \(k\) | Cost | \(A_{\rm crit}\) | First off-wall \(A\in9\mathbb Z\) |
|---|---:|---:|---:|---:|
| \(D_6\) | 6 | \(15/16\) | \(3675/64=57.421875\) | 63 |
| \(D_7\) | 7 | \(19/20\) | \(32041/1040\approx30.808654\) | 36 |
| \(D_3\oplus D_8\) | 11 | \(41/24\) | \(9409/96\approx98.010417\) | 99 |
| \(D_4\oplus D_7\) | 11 | \(73/40\) | \(196249/160=1226.55625\) | 1233 |
| \(D_2\oplus D_{10}\) | 12 | \(63/32\) | \(51483/128\approx402.210938\) | 405 |

The Step-94 leading-order estimates are therefore superseded by these exact values. The first mixed survivors at \(k=11\) are correct. For \(k\le10\), all multiple-block partitions fail; the least expensive two-block partition at \(k=10\), \(D_3\oplus D_7\), already costs \(17/10>10/6\).

For ball quotients, \(A/9=\tau(X)\in\mathbb Z\). “First allowed multiple of nine” means only first **arithmetically passing value**, not existence of a host or Einstein orbifold with that value.

### Wall correction

The script deliberately imposes \(A>3k\). Transfer itself permits \(A=3k\), where
\[
x=\frac{16A}{27},\qquad \beta=\frac{k}{18}.
\]
Thus, for example, \(D_{18}\) at \(A=54\) passes the charge screen. Its listed value \(63\) is the first **off-wall** multiple of nine.

At this wall, mixed feasibility forces \(x=8T_+/9\) and equality in the estimate producing \(F\), hence constant \(|W^+|\) for an Einstein bulk. It does **not** by itself force \(W^-=0\): that additionally requires \(T_-^{\rm orb}=x\). For a full absorption this means total cost exactly \(k/18\). Wall rigidity/existence remains unresolved.

## 5. Correct theorem and remaining mathematical objects

Under the stated aspherical-host, oriented-resolution, and transfer hypotheses, **Kronheimer-only full absorption** forces a full-rank sum of \(D\)-blocks and
\[
\sum_i c(D_{a_i})\le\beta(k,A).
\]
Since \(c(D_a)>a/6\) for \(2\le a\le5\), some block has \(a_i\ge6\); hence \(k\ge6\). At \(k=6\), the only passing configuration is \(D_6\), requiring \(A\ge3675/64\), and therefore \(A\ge63\) for a ball quotient.

This remains a **necessary curvature-and-lattice theorem**, not an existence theorem. Its unresolved geometric content is:

- realization of the filler embeddings with compatible boundary linking and the prescribed smooth resolution;
- existence of the negative Einstein metric on the resulting compact orbifold;
- integral forms of the Şuvaina \(d\ge2\) fillers, not established here.

A rational-homology-ball complement inside a localized \(\#k\overline{\mathbb{CP}}^2\) model is one possible construction requirement, not a consequence of \(k_b=0\) for every orbifold configuration. The general bulk complement retains host homology.

The supplied script and certificate support the finite enumeration through \(k=40\); the signed-support proof supplies the missing unrestricted lattice theorem. No surviving row supplies an Einstein metric, an absorbing construction, or an Einstein-gap minimizing sequence.