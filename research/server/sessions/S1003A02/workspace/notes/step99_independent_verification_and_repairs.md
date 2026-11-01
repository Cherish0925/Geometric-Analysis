# Step 99 — independent verification of the Step-98 Wahl/Şuvaina repairs

Session S1003A02, Agent4, Execute.  Readback target: `step96_suvaina_lattice_and_kahler_filler_theorem.md`, the Step-98 scripts/data, the theorem package, front matter, Step-58 ledger, Step-94 binding correction, Şuvaina's primary source, LeBrun 2005, and Theorem 55.5.  Independent TTCS records: `trace/ttcs/results/step99_ttcs01_verifier{1,2}_integration.md` and four complete branch records.  New exact check: `scripts/step99_wahl_four_coordinate_check.py` → `data/step99/wahl_four_coordinate_check.json` (158 cases through n=16; all pass).

## 1. Proposition 98.W: corrected definitive form

Let \(M=X\#k\overline{\mathbb{CP}}^2\), where \(X\) is aspherical and \(\pi_1X\) is torsion-free.  Let \(B_j=B_{n_j,a_j}\subset M\) be disjoint Wahl balls, \(Y_j=\partial B_j\), \(Y=\coprod Y_j\), and \(W=\overline{M\setminus\coprod B_j}\), assumed connected.  Put
\[
G=H_1(Y)=\bigoplus_j\mathbb Z_{n_j^2},\qquad
K=\ker[G\to\bigoplus_jH_1(B_j)]=\bigoplus_jn_j\mathbb Z_{n_j^2}.
\]
Then the boundary map \(i:G\to H_1(W)\) vanishes.  Indeed, finite \(\pi_1(B_j)\) maps trivially into torsion-free \(\pi_1(M)\); Mayer--Vietoris gives \(\ker i+K=G\); and \(K\subset\Phi(G)\), so the Frattini property gives \(\ker i=G\).  Consequently
\[
0\to H_2(W)\to H_2(M)\to K\to0,
\qquad H_1(W)\cong H_1(M)\cong H_1(X).
\]
The torsion subgroups of \(H_2(W)\) and \(H_2(M)\) map isomorphically (pair sequence, Lefschetz duality, UCT).  Thus, with
\[
L=H_2(W)/\operatorname{Tor},\qquad U=H_2(M)/\operatorname{Tor},
\]
one has \(0\to L\to U\to K\to0\), \([U:L]=\prod n_j\), and \(|\det L|=\prod n_j^2\).  The lattice \(U\) is unimodular (and is odd here when \(k\ge1\)).

The previous torsion-free-\(H_1(X)\) qualification is unnecessary.  In the pair sequence
\[
0\to H_2(W)\xrightarrow JH_2(W,Y)\to G\to0,
\]
the torsion map is an isomorphism: its source and target have equal finite order and \(J\) is injective.  Splitting groups as \(H_2(W)=L\oplus T\), \(H_2(W,Y)=L^*\oplus T'\), the map has block form \(J(l,t)=(Q_Ll,\varphi(l)+\psi(t))\), with \(\psi:T\to T'\) an isomorphism.  Eliminating the torsion block yields
\[
0\to L\xrightarrow{Q_L}L^*\to G\to0.
\]
The standard relative-intersection calculation then identifies the discriminant form of \(L\) with the linking form of \(\partial W=\coprod(-Y_j)\), up to the one global convention sign; torsion contributes zero to the integer-valued absolute--relative pairing.  Under this identification, the subgroup \(U/L\) is not merely abstractly isomorphic to \(K\): it maps to the specified subgroup \(K\subset G\), which is a metabolizer.

Asphericity adds a useful splitting.  The classifying/collapse map \(c:M\to X\) is null on every \(B_j\), because its restriction lifts to contractible \(\widetilde X\).  Relative cohomology and duality therefore place \(c^!H_2(X)\) inside the image of \(H_2(W)\).  Since \(Q_X\) is unimodular on free homology,
\[
L=Q_X\oplus L_0,\qquad L_0\subset-I_k.
\]
Thus host directions cannot supply coordinates for the Wahl discriminant.  In particular there is no Wahl ball at \(k=0\), and \(k\ge\max_p\#\{j:p\mid n_j\}\).

## 2. Corollary 98.V: four coordinates, low-rank obstructions, and the resolution filling

For one Wahl point let \(q=na-1\) and let \(\sigma=\pm1\) encode the oriented boundary-linking target.  Choose a positive integer
\[
N\equiv-\sigma q u^2\pmod{n^2},\qquad (u,n)=1.
\]
Then \((N,n)=1\).  By Lagrange, write \(N=v_1^2+\cdots+v_4^2\).  The content of \(v\) is coprime to \(n\), so \(x\mapsto x\cdot v\pmod n\) is onto.  For
\[
L_v=\{x\in-I_4:x\cdot v\equiv0\pmod n\},
\]
one has index \(n\), discriminant group \(\mathbb Z_{n^2}\), generator \(v/n\), and self-pairing
\[
(v/n)^2=-N/n^2\equiv\sigma q u^2/n^2\pmod1.
\]
The generator has exact order \(n^2\): if \(rv/n\) is integral, the content condition gives \(n\mid r\); writing \(r=ns\), membership in \(L_v\) and \((N,n)=1\) give \(n\mid s\).  Disjoint four-coordinate blocks give the multi-point theorem:
\[
\boxed{k\ge4t\quad\Longrightarrow\quad\text{the required forms and the specified metabolizer are realizable.}}
\]
This improves the Step-98 sufficient range \(k\ge5t\).  Four is a sharp uniform one-point bound: for \((n,a,\sigma)=(8,1,-1)\), the target norm is \(7\bmod8\), hence cannot be a sum of three squares.  Below \(4t\) bilinear data can obstruct.  For example, complex-oriented \(B_{2,1}\) requires norm \(3\bmod4\), so rank one or two cannot work.  The exact finite Step-99 check covers 158 one-point cases, \(2\le n\le16\), both signs: all Gram determinants, Smith forms and square classes pass; the minimum square-rank counts are 81 of rank 1, 46 of rank 2, 19 of rank 3, and 12 of rank 4.

The Step-98 assertion that the minimal-resolution filling gives a separate unexamined integral condition is withdrawn.  Let \(C=\coprod C_{n_j,a_j}\) be the compatible resolution plumbing and \(Y'=W\cup C\).  The boundary anti-isometry glues \(L\oplus C\) to a unimodular lattice; its glue subgroup is the graph of the discriminant anti-isometry.  Therefore \(C\) is primitive, \(L\) is primitive, and \(C^\perp=L\).  At \(k=1\) this is exactly Theorem 55.5: the complement is \(\langle-n^2\rangle\), and compatibility is
\[
1-na\equiv u^2\pmod{n^2},
\]
equivalently \(n\) odd or \(8\mid n\) in the complex orientation.  In higher rank, a bare embedding into *some* unimodular lattice can be weaker than compatibility with the prescribed rational filling \(-I_k\), but compatible complement data already supply the abstract primitive-chain embedding.  What remains topologically is geometric realization (embedded balls/plumbings, the prescribed complement and degree-one map) and possible characteristic/spin\(^c\) refinements, not a second independent bilinear condition.

## 3. Lemma 96.Ş extension

Şuvaina's primary source does include minimal resolutions of possibly singular invariant fibres.  The extension of the topology to them is valid after one proof repair.  Admissible GH centre configurations are \(d\)-point configurations in the connected three-manifold \((\mathbb R\times\mathbb C^*)/\mathbb Z_n\), so they are joined by a compactly supported equivariant isotopy avoiding the axis and fixed near infinity.  The former sentence “matching Chern numbers make the isotopy lift” was insufficient because equivariant circle bundles also carry a fibre character.  Instead, take the family of GH bundles over the moving-centre complement and use equivariant homotopy invariance (equivalently, horizontally lift the base isotopy using a \(\mathbb Z_n\times S^1\)-invariant family connection).  The lift is fixed near infinity, commutes with the deck action, and extends orbitwise across the Hopf fillings.  This proves the equivariant orientation-preserving diffeomorphism to a smooth-fibre model with marked end.

The rest is sound: the deck action is the signless permutation on the \(A_{dn-1}\) lattice; boundary \(\pi_1\)-surjectivity gives torsion-free \(H_2\); \(|H_1(\partial N)|=dn^2\), \(|H_1(N)|=n\) give \(|\det Q_N|=d\); comparison with the scaled invariant lattice gives transfer index one and
\[
H_1(N)=\mathbb Z_n,\qquad H_2(N)=A_{d-1}(-1),\qquad c(N)=1-1/(dn^2).
\]
Theorem 96.K therefore stands.  Its conclusion decides transferred curvature and lattice-embedding data, not the remaining index-\(2^q\) prism-linking compatibility or geometric/Einstein existence.

## 4. Problem 4 and source scope

The torsion-zero statement is correct, but “total signed index” needs an isolated-zero qualification: if zeros are isolated their local indices sum to \(5\chi+6\tau\); generally \(c_2(E)\) is the localized Euler class of the section.  LeBrun 2005 Proposition 2.4 supplies a second direct proof that a compact AKE metric has a torsion zero.  Corollary 3.6 gives, for the fixed almost-Kähler metric, a possibly singular/disconnected \(J\)-holomorphic cycle with \(c_1\cdot C=1\), not necessarily an embedded exceptional sphere.  Corollary 3.2 rearranges to the curve torsion inequality.

Finally, the quantity
\[
T:=\int(s^2/24-|W^+|^2)
\]
satisfies for every Einstein metric
\[
s^2V=32\pi^2(2\chi+3\tau)+16T
\]
by Gauss--Bonnet/signature.  On \(M=X\#k\overline{\mathbb{CP}}^2\) with the given orientation, LeBrun's scalar bound yields \(T\ge2\pi^2k\).  Thus A01's proposed \(T_{AK}\ge2\pi^2k\), once \(T_{AK}=T\), is the inherited Einstein curvature bound and adds no new obstruction.  The genuinely unchecked AK statements are the identity \(|s|Q/16=\int|\eta|^2+T_{AK}\), the identification of its torsion-defined \(T_{AK}\) with \(T\), and the canonical-cycle equality.
