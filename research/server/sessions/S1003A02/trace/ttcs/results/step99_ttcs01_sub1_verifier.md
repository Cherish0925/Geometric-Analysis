# TTCS Independent Branch Record

```json
{
  "step_id": 99,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step96_suvaina_lattice_and_kahler_filler_theorem.md",
    "Sessions/S1003A02/workspace/scripts/step98_wahl_gluing_lattice.py",
    "Sessions/S1003A02/workspace/data/step98/wahl_gluing_lattice.json",
    "Sessions/S1003A02/workspace/notes/step55_k1_orbifold_gate_charges_lattices_collapse.md"
  ]
}
```

## Task

Independently verify Proposition 98.W and Corollary 98.V in §3 of the Step-96/98 note. Reconstruct every Mayer–Vietoris, torsion, duality, Frattini, lattice-index, discriminant-linking, and five-square-block step. Check multiple Wahl balls, torsion in H1(X), boundary orientation/sign conventions, the generator/order calculation in the discriminant group, and the precise range k>=5t. Identify any missing hypothesis or overbroad conclusion, especially whether the bilinear condition can be said never to obstruct outside that range. Compare with the Step-55 second-filling condition and explain exactly why it is independent. Give a direct mathematical memo with repairs if needed.

## Output

# Scientific verification memo: Proposition 98.W and Corollary 98.V

## 1. Summary

Proposition 98.W is mathematically sound under the standard topology of a Wahl ball:
\[
\pi_1(B_{n,a})=H_1(B_{n,a})=\mathbb Z_n,\qquad H_2(B_{n,a})=0,
\]
and \(H_1(\partial B_{n,a})=\mathbb Z_{n^2}\to H_1(B_{n,a})\) is onto.

Corollary 98.V gives a valid uniform construction for \(k\ge 5t\). The number \(5t\) is sufficient, not optimal: five exceptional coordinates per Wahl point implement a fixed \(1\) plus Lagrange’s four-square theorem. No general conclusion for \(k<5t\) follows from this construction.

Three textual repairs are appropriate:

1. \(U=H_2(M)/\operatorname{Tor}\) is always unimodular, but it is automatically odd only when \(k\ge1\) or \(Q_X\) is already odd.
2. The group isomorphism
   \[
   L^*/L\cong H_1(\partial W)
   \]
   actually follows even when \(H_1(X)\) has torsion. Torsion-freeness of \(H_1(X)\) is needed in the supplied proof to identify the bilinear forms without additional torsion-linking information.
3. The sentence that the bilinear condition never obstructs should be restricted to:
   - \(k\ge5t\), and
   - the torsion-free \(H_1(X)\) setting when it is interpreted as the actual discriminant–linking relation of the complement.

The Step-55 second-filling condition is genuinely different. Corollary 98.V constructs an index-\(\prod n_j\) sublattice after rational-ball filling; it does not construct a primitive continued-fraction chain inside the unimodular lattice arising after resolution filling.

---

## 2. Mayer–Vietoris reconstruction

Write
\[
Y_j=\partial B_j,\qquad
G=H_1(Y)=\bigoplus_j\mathbb Z_{n_j^2},\qquad
R=\bigoplus_jH_1(B_j)=\bigoplus_j\mathbb Z_{n_j}.
\]
Let
\[
i:G\longrightarrow H_1(W),\qquad
j:G\longrightarrow R.
\]
For each Wahl ball, \(j_j:\mathbb Z_{n_j^2}\to\mathbb Z_{n_j}\) is onto, hence
\[
K:=\ker j=\bigoplus_j n_j\mathbb Z_{n_j^2}
       \cong\bigoplus_j\mathbb Z_{n_j}.
\]

The relevant Mayer–Vietoris segment is
\[
G\xrightarrow{(i,j)}H_1(W)\oplus R
 \longrightarrow H_1(M)
 \longrightarrow H_0(Y)
 \longrightarrow H_0(W)\oplus\bigoplus_jH_0(B_j).
\]
The last map sends
\[
(r_1,\ldots,r_t)\longmapsto
\bigl(\textstyle\sum_jr_j,-r_1,\ldots,-r_t\bigr),
\]
up to a uniform sign convention, and is injective. Therefore
\[
H_1(W)\oplus R\longrightarrow H_1(M)
\]
is onto.

Since
\[
\pi_1(B_j)=\mathbb Z_{n_j}
   \longrightarrow \pi_1(M)=\pi_1(X)
\]
maps a finite group into a torsion-free group, it is trivial. Thus the induced map \(H_1(B_j)\to H_1(M)\) is zero. Consequently every \((0,b)\in H_1(W)\oplus R\) lies in the kernel of the map to \(H_1(M)\), so exactness gives
\[
j(\ker i)=R.
\]
Equivalently,
\[
\ker i+K=G.
\]

### Frattini step

For a finite abelian group,
\[
\Phi(G)=\bigoplus_p pG_p.
\]
On the \(p\)-primary part of \(\mathbb Z_{n_j^2}\), multiplication by \(n_j\) contains at least one factor of \(p\). Hence
\[
K\subseteq\Phi(G).
\]
Thus
\[
\ker i+\Phi(G)=G.
\]
A subgroup of a finite group whose image generates \(G/\Phi(G)\) is the whole group. Therefore
\[
\boxed{i=0.}
\]
This argument works unchanged for multiple Wahl balls, including repeated primes among the \(n_j\).

---

## 3. \(H_2\), cokernel, and torsion

Because \(H_2(Y)=0\) and \(H_2(B_j)=0\), Mayer–Vietoris gives
\[
0\longrightarrow H_2(W)
 \longrightarrow H_2(M)
 \longrightarrow G
 \xrightarrow{(i,j)}H_1(W)\oplus R.
\]
Since \(i=0\),
\[
\ker(i,j)=\ker j=K,
\]
and hence
\[
\boxed{0\longrightarrow H_2(W)
 \longrightarrow H_2(M)
 \longrightarrow K\longrightarrow0.}
\]

The \(H_1\)-sequence now reduces to
\[
H_1(M)\cong
\frac{H_1(W)\oplus R}{0\oplus R}
\cong H_1(W).
\]
Thus
\[
\boxed{H_1(W)\cong H_1(M)\cong H_1(X).}
\]

For the pair \((W,Y)\),
\[
G\xrightarrow{i=0}H_1(W)\longrightarrow H_1(W,Y)
 \longrightarrow H_0(Y)\longrightarrow H_0(W).
\]
The final kernel is \(\mathbb Z^{t-1}\), so
\[
0\longrightarrow H_1(W)
 \longrightarrow H_1(W,Y)
 \longrightarrow\mathbb Z^{t-1}
 \longrightarrow0.
\]
Therefore
\[
\operatorname{Tor}H_1(W,Y)
 \cong\operatorname{Tor}H_1(W).
\]

Lefschetz duality and universal coefficients give
\[
H_1(W,Y)\cong H^3(W),
\]
and
\[
\operatorname{Tor}H^3(W)
 \cong\operatorname{Ext}(H_2(W),\mathbb Z)
 \cong\operatorname{Tor}H_2(W).
\]
Hence
\[
\operatorname{Tor}H_2(W)
 \cong\operatorname{Tor}H_1(W).
\]
For the closed oriented four-manifold \(M\), Poincaré duality and universal coefficients similarly give
\[
\operatorname{Tor}H_2(M)
 \cong\operatorname{Tor}H_1(M).
\]
Since \(H_1(W)\cong H_1(M)\), the two torsion subgroups of \(H_2\) have the same order. The injection \(H_2(W)\to H_2(M)\) restricts to an injection between them, so it is an isomorphism:
\[
\boxed{\operatorname{Tor}H_2(W)\xrightarrow{\;\cong\;}
       \operatorname{Tor}H_2(M).}
\]

Let
\[
L=H_2(W)/\operatorname{Tor},\qquad
U=H_2(M)/\operatorname{Tor}.
\]
The induced map \(L\to U\) is injective, and the torsion is already contained in the image of \(H_2(W)\). Thus
\[
\boxed{U/L\cong K\cong\bigoplus_j\mathbb Z_{n_j}.}
\]
In particular,
\[
[U:L]=\prod_jn_j.
\]
Since \(U\) is unimodular,
\[
\boxed{|\det L|=[U:L]^2=\prod_jn_j^2.}
\]

The description
\[
U\cong Q_X\oplus(-I_k)
\]
is correct. Calling \(U\) odd requires \(k\ge1\) or odd \(Q_X\).

---

## 4. Discriminant group and torsion in \(H_1(X)\)

If \(H_1(X)\) is torsion-free, then \(H_1(W)\) and \(H_2(W)\) are torsion-free. Lefschetz duality and universal coefficients yield
\[
H_2(W,Y)\cong H^2(W)\cong L^*.
\]
The pair sequence becomes
\[
0\longrightarrow L\xrightarrow{Q_L}L^*
 \longrightarrow H_1(Y)\longrightarrow0,
\]
so
\[
\boxed{L^*/L\cong H_1(Y)
       =\bigoplus_j\mathbb Z_{n_j^2}.}
\]

There is a slight strengthening available. Even when \(H_1(X)\) has torsion, the group isomorphism still follows. Indeed,
\[
0\to H_2(W)\to H_2(W,Y)\to H_1(Y)\to0,
\]
and the torsion subgroup of \(H_2(W)\) maps isomorphically onto the torsion subgroup of \(H_2(W,Y)\). Quotienting both terms by torsion gives
\[
0\to L\to L^*\to H_1(Y)\to0.
\]
Thus \(L^*/L\cong H_1(Y)\) as groups in all cases covered by items 1–3.

What remains dependent on the torsion-free \(H_1(X)\) assumption is the direct identification of the bilinear pairings. When \(\operatorname{Ext}(H_1(W),\mathbb Z)\ne0\), its torsion-linking contribution is present at chain level. The displayed proof in the note does not determine how that contribution modifies the identification with the linking form.

### Orientation and sign

Let \(Y_j^B=\partial B_j\) carry the outward orientation from \(B_j\). Then
\[
\partial W=-\coprod_jY_j^B.
\]
Hence
\[
\lambda_{\partial W}
 =-\bigoplus_j\lambda_{Y_j^B}.
\]
With
\[
b_L([x],[y])=Q_L(x,y)\pmod{\mathbb Z},
\]
the standard chain convention gives \(b_L=\lambda_{\partial W}\); an alternative definition of linking reverses all signs simultaneously. The note’s “up to the global sign convention” is therefore appropriate, provided that sign is fixed uniformly rather than independently on each component.

For a cyclic lens pairing of order \(p\), one convention gives \(q/p\), another \(q^{-1}/p\). These define the same square class because
\[
q^{-1}=q(q^{-1})^2\pmod p.
\]
Thus the use of \(q=n_ja_j-1\), rather than \(q^{-1}\), is harmless once multiplication by unit squares is allowed.

Finally, \(U/L\subset L^*/L\) is isotropic: pairings of elements of \(U\) are integral. Its order is
\[
|U/L|=\prod_jn_j=\sqrt{|L^*/L|},
\]
so it is a metabolizer. Compatibility of the Mayer–Vietoris connecting map with restriction to \(H_2(W,Y)\) identifies it with
\[
K=\bigoplus_jn_j\mathbb Z_{n_j^2}.
\]

---

## 5. Verification of the five-coordinate construction

Fix one Wahl point and write
\[
n=n_j,\qquad q=na-1,\qquad \sigma\in\{\pm1\}.
\]
Since \(\gcd(q,n)=1\), choose the least positive residue
\[
N\equiv-\sigma q\pmod{n^2}.
\]
Then \(\gcd(N,n)=1\) and \(N-1\ge0\). Lagrange’s theorem gives
\[
N-1=x_1^2+x_2^2+x_3^2+x_4^2.
\]
In a five-coordinate block of \(-I_k\), take
\[
v=(1,x_1,x_2,x_3,x_4).
\]
Then
\[
v^2=-N,
\]
and \(v\) is primitive because its first coordinate is \(1\). This is the exact source of the number five: one fixed square plus four arbitrary squares. A unit \(u\) can also be included by choosing
\[
N\equiv-\sigma q\,u^2\pmod{n^2},
\]
but \(u=1\) already proves existence.

For \(t\) points, use disjoint five-coordinate blocks. The vectors satisfy
\[
v_i\cdot v_j=0\qquad(i\ne j).
\]
Define
\[
\phi:U\longrightarrow\bigoplus_j\mathbb Z_{n_j},
\qquad
\phi(x)=(x\cdot v_j\bmod n_j)_j,
\]
and
\[
L=\ker\phi.
\]
Each component is onto because pairing with the first basis vector in its block gives \(\pm1\). Therefore
\[
[U:L]=\prod_jn_j.
\]

Set
\[
g_j=\frac{v_j}{n_j}\in L^*.
\]
For \(x\in L\), \(x\cdot v_j\) is divisible by \(n_j\), so \(g_j\) indeed lies in \(L^*\).

To compute its order in \(L^*/L\), suppose \(r g_j\in L\). Since \(v_j\) is primitive,
\[
\frac r{n_j}v_j\in U
\quad\Longrightarrow\quad n_j\mid r.
\]
Write \(r=n_js\). Membership \(sv_j\in L\) requires
\[
0\equiv sv_j\cdot v_j=-sN_j\pmod{n_j}.
\]
Because \(\gcd(N_j,n_j)=1\), this implies \(n_j\mid s\). Hence
\[
\operatorname{ord}(g_j)=n_j^2.
\]
Disjoint support gives no relations between the different \(g_j\). Since
\[
\prod_j\operatorname{ord}(g_j)
 =\prod_jn_j^2
 =|L^*/L|,
\]
they generate:
\[
\boxed{L^*/L\cong\bigoplus_j\mathbb Z_{n_j^2}.}
\]

Their pairings are
\[
b_L(g_j,g_j)
 =\frac{v_j^2}{n_j^2}
 =-\frac{N_j}{n_j^2}
 \equiv\frac{\sigma_jq_ju_j^2}{n_j^2}\pmod1,
\]
and
\[
b_L(g_i,g_j)=0\qquad(i\ne j).
\]
Moreover
\[
n_jg_j=v_j\pmod L
\]
generates the order-\(n_j\) subgroup \(U/L\) in the \(j\)-th cyclic factor. Thus the construction also reproduces the prescribed metabolizer.

The script’s 54 cases and Smith form
\[
(1,1,1,1,n^2)
\]
agree with this derivation. The multi-point statement is not explicitly computed by the script, but follows immediately from the orthogonal direct sum of the five-coordinate blocks.

---

## 6. Meaning of \(k\ge5t\)

The construction consumes exactly \(5t\) exceptional coordinates and leaves \(Q_X\) and all unused exceptional coordinates unchanged. Therefore it proves:

\[
\boxed{k\ge5t\quad\Longrightarrow\quad
\text{the required abstract bilinear lattice exists}.}
\]

This is not an optimal threshold. For \(k<5t\), several possibilities remain:

- some residues may be represented with fewer than five squares;
- different vectors may share coordinates while remaining orthogonal;
- \(Q_X\) may supply suitable vectors;
- arithmetic of a particular lens form may prevent a low-rank realization.

Accordingly, the bilinear condition cannot be declared universally absent for \(k<5t\) from the present argument.

When \(H_1(X)\) has torsion, the same abstract lattice \(L\subset U\) still exists, but the supplied derivation does not identify its discriminant pairing with the actual linking pairing of \(\partial W\). The broad Wahl-sector sentence should therefore distinguish abstract lattice realizability from the torsion-linking structure of an actual complement.

---

## 7. Independence from the Step-55 second filling

The two constructions concern different closed four-manifolds.

### Rational-ball filling

For
\[
M=W\cup B_{n,a},
\]
Proposition 98.W studies the finite-index inclusion
\[
L=H_2(W)/\operatorname{Tor}
 \subset U=H_2(M)/\operatorname{Tor}.
\]
Corollary 98.V realizes the lens linking form by a congruence kernel
\[
L=\{x\in U:x\cdot v\equiv0\pmod n\}.
\]
No continued-fraction plumbing appears.

### Resolution filling

Replacing the Wahl ball by the minimal-resolution plumbing \(C_{n,a}\) gives
\[
Y'=W\cup C_{n,a}.
\]
Step 55 uses a degree-one map \(Y'\to X\) to place the full chain lattice inside the unimodular kernel of \(H_2(Y')\to H_2(X)\). At \(k=1\), this kernel has rank \(r+1\), while the chain has rank \(r\). Its orthogonal complement therefore has rank one and square \(-n^2\). Primitivity forces an anti-isometry
\[
A_{C_{n,a}}
 \cong -A_{\langle-n^2\rangle}.
\]
Since the chain coefficient is
\[
\beta\equiv1-na\pmod{n^2},
\]
this becomes
\[
1-na\equiv u^2\pmod{n^2},
\]
equivalently \(n\) odd or \(8\mid n\).

Corollary 98.V supplies neither the chain vectors with their continued-fraction Gram matrix nor their primitivity in the second-filled unimodular lattice. It also supplies no degree-one map to \(X\). Thus it cannot imply the Step-55 congruence.

The \(n=2,a=1\) example makes the distinction explicit. With the usual lens convention,
\[
Q_X\oplus\langle-4\rangle
 \subset Q_X\oplus\langle-1\rangle
\]
is an index-two sublattice with discriminant form \(\langle-1/4\rangle\), so the rational-ball complement relation is algebraically realizable. In contrast, the resolution chain is \(\langle-4\rangle\), and a primitive embedding into \(-I_2\) does not exist: every integer solution of
\[
x^2+y^2=4
\]
is \((\pm2,0)\) or \((0,\pm2)\), hence divisible by \(2\). This is precisely the Step-55 \(B_2\) phenomenon.

For general \(k\), the second-filled kernel has rank \(r+k\), and the primitive chain-embedding problem has additional room. Corollary 98.V does not settle that general-\(k\) problem.

---

## 8. Recommended corrected formulation

A precise version is:

> For standard Wahl balls embedded in \(M=X\#k\overline{\mathbb{CP}}^2\) with torsion-free \(\pi_1(X)\), items 1–3 of Proposition 98.W hold. Moreover \(L^*/L\cong H_1(\partial W)\) as groups. If \(H_1(X)\) is torsion-free, this isomorphism identifies the discriminant pairing with the linking pairing of \(\partial W\), up to the single global sign convention, and \(U/L\) corresponds to the canonical metabolizer.
>
> For every collection of \(t\) Wahl links and every choice of orientations, \(k\ge5t\) guarantees an abstract index-\(\prod n_j\) sublattice of \(Q_X\oplus(-I_k)\) with the required cyclic discriminant forms and metabolizer. This is a uniform sufficient construction, not a minimal-rank theorem. It does not address torsion-linking refinements when \(H_1(X)\) has torsion, characteristic or spin\(^c\) refinements, or the primitive plumbing embedding arising from the resolution filling.