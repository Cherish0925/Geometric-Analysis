# Step 95 — exact transfer algebra, diagonal-root embeddings, and finite-A D-block thresholds

Session S1003A02, Agent3, Execute. This note independently checks the first-priority assertions in
`step94_filler_screen_dichotomy.md`. Reproducible computation:

- script: `workspace/scripts/step95_filler_lattice_screen.py`;
- full exact output: `workspace/data/step95/filler_lattice_screen.json`;
- compact certificate: `workspace/data/step95/filler_lattice_screen_certificate.json`.

Run from the user root with

```text
qiushi-geometry env core python Sessions/S1003A02/workspace/scripts/step95_filler_lattice_screen.py
```

The successful run exited 0. The full JSON is 17,149,717 bytes and the compact certificate is 446,358 bytes. All algebra uses SymPy exactly; all thresholds use `fractions.Fraction`. The finite lattice search has deterministic canonicalization and stores its counters, witnesses, Gram matrices, and a SHA-256 digest (`2ac528ae74ecc7812ff3c8dbfe8aa235feaf7ba8fec7fff6b66c992863cde1f7`). A planned Wolfram repetition could not run because the installed Wolfram Engine license is expired; the script records the independent exact SymPy calculation instead.

## 1. The transferred inequality is exact

For
\[
F(x,T)=(\sqrt{8x}+\sqrt{T-x})^2,\qquad 0\le x\le T,
\]
the supporting-plane statement does not need an abstract concavity argument: direct algebra gives
\[
\boxed{9x+3T-F(x,T)=2\bigl(\sqrt{T-x}-\sqrt{2x}\bigr)^2\ge0.}
\]
Equality holds exactly when \(T=3x\). Insert
\[
T_+^{\rm orb}=A-k+C_+,
\qquad
T_-^{\rm orb}=4c_2(X)-A+5k+C_-,
\qquad x\le T_-^{\rm orb},
\]
and the mixed-transfer lower side \(F\ge6A+C_+\). Exact expansion yields
\[
\boxed{9C_-+2C_++42k+12(3c_2(X)-c_1^2(X))\ge0.}
\]
Thus the coefficient of the BMY defect in Step 94 is correct. For a ball quotient it vanishes.

For complex-oriented Kähler Ricci-flat fillers and reversed Wahl balls, write
\[
C_-=-4\{(k-k_b)+S_{\rm cx}\},\quad
C_+=-4S_{\rm rev},
\]
where
\[
S_{\rm cx}=\sum_{\rm cx}(1-|\Gamma_j|^{-1}),\qquad
S_{\rm rev}=\sum_{\rm rev}(1-n_j^{-2}).
\]
The exact expression becomes
\[
6k+36k_b-36S_{\rm cx}-8S_{\rm rev}\ge0,
\]
equivalently
\[
\boxed{S_{\rm cx}+\frac29S_{\rm rev}\le\frac k6+k_b.}
\]
This verifies the Step-94 \(k_b\) budget. Here \(k_b\) is only the rank of the blow-up kernel not represented by filler homology; it does not identify particular exceptional spheres in the regular bulk, because integral gluing can mix classes through finite-index lattices. Each retained rank enlarges this aggregate budget by one unit. The transfer can still exclude some \(k_b>0\) configurations (for example two \(D_2\) blocks at \(k=5,k_b=1\) have \(S_{\rm cx}=2>11/6\)). What it cannot see is class-by-class placement, linking, or singular monopole information once these aggregate budgets have slack. A Wahl ball contributes no absorbed rank, but may coexist with full-rank Kronheimer fillers, so its presence does not by itself imply \(k_b>0\). Pure Wahl configurations have \(k_b=k\); mixed configurations obey the displayed weighted budget. Excluding the surviving retained-rank or Wahl sectors requires information at the singularities themselves (for example APS/Dedekind terms coupled to a stronger global relation, orbifold monopole supply, or local analysis at type-T points), not repetition of the same aggregate smooth transfer.

## 2. Exact finite root search

### 2.1 Reduction to norm-two roots

Any isometric embedding of a simply-laced negative root lattice into \(-I_k\) becomes, after reversing signs, an embedding into \(I_k\). Every root has norm two, hence is exactly
\[
\pm e_i\pm e_j,
\]
with two nonzero coordinates. The script searches simple-root systems with their exact Cartan Gram matrix.

The search removes only signed-coordinate symmetries:

1. the first root is fixed to \(e_1-e_2\);
2. nodes are added in a connected breadth-first order;
3. a new root adjacent to the assigned connected subsystem can introduce at most one new coordinate;
4. a first new coordinate receives the next unused label and positive first sign.

A connected rank-\(r\) simple system therefore uses at most \(r+1\) coordinates. A negative search in \(I_{r+1}\) covers every larger diagonal lattice, since unused coordinates play no role. This is a finite exhaustive argument, not a bounded ambient-dimension heuristic.

### 2.2 Irreducible outcomes

The exact search establishes:

- \(A_2\) needs three coordinates;
- \(A_3=D_3\) embeds in three coordinates;
- for every tested \(4\le r\le12\), \(A_r\) does not embed in \(I_r\), while an explicit embedding in \(I_{r+1}\) is saved;
- the standard \(D_r\) embeddings in \(I_r\) are saved for \(2\le r\le12\);
- \(E_6,E_7,E_8\) have no embeddings in any diagonal lattice.

For the E-types, the exhaustive counters are especially small after canonicalization: each search tests 436 candidate roots, reaches 15 DFS states and no complete solution. The same early incompatibility occurs before the longer arms distinguish the three types. Exact Gram matrices accompany every positive witness.

The unrestricted classification uses a signed-support argument, rather than extrapolating the bounded \(A_r\) run. The roots of the embedded ADE lattice are reflection-closed. Represent each root \(\pm e_i\pm e_j\) by a signed edge on its coordinate support. On a connected support with \(m\) coordinate vertices, switch coordinate signs along a spanning tree so its edges are differences. Reflections in those roots generate all coordinate permutations. If all roots remain differences, reflection closure is \(A_{m-1}\), of rank \(m-1\); if one sum root occurs, permutations generate all sums and differences and the closure is \(D_m\), of rank \(m\). Thus \(A_r\) uses \(r+1\) coordinates except \(A_3=D_3\) (and \(A_1\) uses two), whereas a \(D_m\) block uses \(m\). Full rank in \(I_k\) leaves neither a difference-only component nor an unused coordinate. Hence a full-rank subsystem coming from known Kronheimer fillers is
\[
\boxed{\bigoplus_iD_{a_i},\qquad a_i\ge2,\qquad \sum_i a_i=k.}
\]
This also handles coordinate sharing: the low-rank block \(D_2=A_1\oplus A_1\) is exactly the orthogonal EH pair \(e_i-e_j,e_i+e_j\). The exact searches through \(A_{12}\) corroborate the general argument; they are not its logical basis. This confirms the Step-94 full-absorption lattice reduction and excludes the A- and E-type single-filler rows which survived curvature arithmetic alone. A full-rank sublattice need not equal \(I_k\): with \(q\) D-blocks it has determinant \(4^q\) and index \(2^q\), so boundary linking and integral gluing remain additional conditions.

## 3. Exact finite-\(A\) D-block screen

For a full-absorption partition \(k=\sum_i a_i\), define
\[
c(D_2)=1,\qquad c(D_3)=\frac34,
\qquad c(D_a)=1-\frac1{4(a-2)}\quad(a\ge4).
\]
The mixed-transfer condition is
\[
\sum_i c(D_{a_i})\le\beta(k,A),
\]
where the exact expression simplifies after
\(y=\sqrt{1-3k/A}\) to
\[
\boxed{\beta(k,A)=\frac{k(5y+1)}{18(1+y)}}.
\]
It is strictly increasing from \(k/18\) at the wall \(A=3k\) to \(k/6\) as \(A\to\infty\), and
\[
\frac{\beta}{k}=\frac16-\frac1{12}\frac{k}{A}
-\frac18\left(\frac{k}{A}\right)^2
-\frac{15}{64}\left(\frac{k}{A}\right)^3+O((k/A)^4).
\]
For a cost \(c\in(k/18,k/6)\), put \(r=18c/k\). The unique threshold is exact:
\[
y_{\rm crit}=\frac{r-1}{5-r},
\qquad
A_{\rm crit}=\frac{3k}{1-y_{\rm crit}^2}.
\]
The script enumerated every nondecreasing D-block partition for \(2\le k\le40\). There are 16,049 finite-\(A\) surviving partitions in this range, all retained in the full JSON; per-\(k\) counts and extremal rows are in the compact certificate.

### 3.1 First blocks and corrected thresholds

A block of rank at most five has cost strictly larger than rank/6:
\[
c(D_2)-2/6=2/3,
\quad c(D_3)-3/6=1/4,
\quad c(D_4)-4/6=5/24,
\quad c(D_5)-5/6=1/12.
\]
Therefore every full-absorption survivor contains a block \(D_a\) with \(a\ge6\). In particular no full absorption is possible for \(k<6\).

The first single block is \(D_6\), with
\[
c=\frac{15}{16},
\qquad A_{\rm crit}=\frac{3675}{64}=57.421875.
\]
For ball-quotient values \(A\in9\mathbb Z\), the first allowed value is \(A=63\), not the Step-94 estimate \(A\gtrsim48\) and not the earlier sampled value 90. The next exact rows are
\[
\begin{array}{c|c|c|c}
\text{block}&c&A_{\rm crit}&\min(A\in9\mathbb Z)\\
D_7&19/20&32041/1040\approx30.80865&36\\
D_8&23/24&8281/288\approx28.75347&36\\
D_9&27/28&16641/560\approx29.71607&36\\
D_{10}&31/32&271441/8576\approx31.65124&36.
\end{array}
\]
All also satisfy the open-range requirement \(A>3k\). The script deliberately reports the first off-wall multiple of nine. Transfer itself allows \(A=3k\), where \(\beta=k/18\); any row with cost at most \(k/18\) is an equality-wall arithmetic candidate and belongs to the unresolved half-conformally-flat wall problem, not to the open-range table.

The first mixed survivors occur at \(k=11\):
\[
D_3\oplus D_8:
\quad c=41/24,
\quad A_{\rm crit}=9409/96\approx98.0104,
\quad A_{9\mathbb Z}^{\min}=99,
\]
and
\[
D_4\oplus D_7:
\quad c=73/40,
\quad A_{\rm crit}=196249/160\approx1226.556,
\quad A_{9\mathbb Z}^{\min}=1233.
\]
The first survivor containing \(D_2\) is \(D_2\oplus D_{10}\) at \(k=12\), with
\(A_{\rm crit}=51483/128\approx402.211\), first multiple of nine \(405\). Thus large blocks can subsidize small ones, but the finite-\(A\) price can be very high.

## 4. Scope and the resulting theorem

Combining the transferred inequality, the aspherical-host lattice embedding from Step 94, and the exact search gives the following statement.

**Full-absorption theorem (verified arithmetic and lattice form).** Let \(X\) be a compact ball quotient and suppose a negative Einstein orbifold resolves to \(X\#k\overline{\mathbb{CP}}^2\) using only known complex-oriented Kronheimer Ricci-flat ALE fillers, with all \(k\) exceptional ranks in the fillers (\(k_b=0\)). Then their root lattice is a full-rank sum \(\oplus_iD_{a_i}\), \(\sum a_i=k\), and it obeys the exact cost inequality above. In particular at least one \(a_i\ge6\), hence \(k\ge6\). For \(k=6\), the only arithmetic possibility is \(D_6\), and it requires \(A\ge3675/64\) (therefore \(A\ge63\) for a ball quotient). Every surviving row still requires a compact rational-homology complement and a negative Einstein metric; none is thereby constructed.

The phrase “using known Kähler Ricci-flat fillers” needs this Kronheimer/full-rank qualification. Şuvaina fillers with \(d\ge2\) were not classified in this Step. Wahl balls have rank zero: pure Wahl configurations have \(k_b=k\), but Wahl points can also accompany a full-rank Kronheimer system with \(k_b=0\), in which case they add charge cost without absorbing rank. Those are second-priority questions because the verified aggregate smooth-transfer inequality leaves many such configurations after its budget is applied.

The full-absorption theorem materially narrows the singular-bulk alternative but does not close it. It converts it into a topological/existence problem for a high-rank \(D_{\ge6}\) plumbing with a rational-homology complement and a compatible negative Einstein bulk. The retained-rank branch is not automatically allowed, but after the displayed aggregate budgets have slack it is outside the class-sensitive resolving power of this smooth transfer method.
