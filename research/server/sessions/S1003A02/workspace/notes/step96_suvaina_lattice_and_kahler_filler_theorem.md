# Step 96 — integral lattice of Şuvaina class-T fillers; full absorption by all Kähler Ricci-flat ALE fillers; the Wahl gluing question

Session S1003A02, Agent2, Execute. Inputs: `step95_verified_transfer_lattice_thresholds.md` (transfer budget, signed-support
classification, D-block thresholds), `step94_filler_screen_dichotomy.md` (aspherical-host lattice embedding (L0)–(L1)),
Şuvaina's primary text `Knowledge/objects/papers/ALE-Ricci-flat-Kahler-metrics-and-deformations-of-quotient-surface-singu--9db598b6c84c--5ab7b434e210/object.md`
(Prop. 2.3, Prop. 4.4, Theorem B, §5), \cite{suvaina2011ale}.
Exact check: `workspace/scripts/step96_suvaina_lattice.py` → `workspace/data/step96/suvaina_lattice.json`
(102 cases \(1\le d\le6,\ 2\le n\le7,\ (m,n)=1\); all assertions pass). The script is a finite consistency check of the
permutation-lattice arithmetic; its transfer-index field uses the topological determinant prediction and is not an
independent computation of transfer. General coverage comes from the proof below, not from the finite range.

> **Step-98 repair (from the Step-97 independent reading, `trace/ttcs/results/step97_ttcs01_verifier1_integration.md`).**
> (1) §0 originally said that the smooth affine quotients \(M_{d,n}/\mathbb Z_n\) are the complete list. That is false
> biholomorphically: Şuvaina's Theorem B also contains minimal resolutions of *singular* invariant fibres. §0 and Lemma
> 96.Ş are now stated for the whole family, with the equivariant Gibbons–Hawking-centre argument showing that the
> lattice, \(\pi_1\), end, charge and cost are unchanged; Theorem 96.K is unaffected. (2) The former Question 96.W asserted
> an index-\(n\) sublattice and a full anti-isometry with the lens linking form; neither follows from Mayer–Vietoris alone.
> §3 replaces it by the corrected Step-99 result: torsion-free \(\pi_1(X)\) forces the boundary map to vanish, the full
> discriminant–linking identification survives torsion in \(H_1(X)\), the abstract condition is uniformly realizable for
> \(k\ge4t\) but can obstruct below that range, and compatible discriminant gluing already supplies the abstract primitive
> resolution-chain embedding. The Step-94 norm-four-vector reading is withdrawn.

## 0. Which Kähler Ricci-flat ALE fillers exist

Şuvaina's classification (Prop. 4.4 and Theorem B of the primary text) is complete for Kähler Ricci-flat ALE surfaces: the
universal cover is an ALE hyperkähler (Kronheimer) surface, \(\pi_1\) is finite cyclic, and if \(\pi_1=\mathbb Z_n\ne1\) the end
group is cyclic of type \(\frac1{dn^2}(1,dnm-1)\), \((m,n)=1\), and the universal cover is of type \(A_{dn-1}\). Theorem B says
that such a surface is the *minimal resolution of a fibre* of a \(\mathbb Q\)-Gorenstein deformation, and that fibre may be
singular. Precisely, the non-simply-connected members are
\[
N=\widetilde N/\mathbb Z_n,\qquad \widetilde N=\operatorname{Res}_{\min}\Bigl\{xy=\prod_{i=1}^d(z^n-c_i^n)\Bigr\},\qquad c_i\ne0,
\]
with repeated \(c_i^n\) allowed, and the deck generator \((x,y,z)\mapsto(\rho x,\rho^{-1}y,\rho^mz)\), \(\rho^n=1\), lifted to the
resolution. Example: \(xy=(z^2-1)^2\) with \((x,y,z)\mapsto(-x,-y,-z)\) exchanges its two \(A_1\) points; the invariant
resolution has a free action, end \(L(8,3)\), and contains a holomorphic \((-2)\)-curve, so it is not biholomorphic to any
smooth affine quotient. The smooth quotients \(N_{d,n,m}=M_{d,n}/\mathbb Z_n\) (distinct \(c_i^n\)) therefore do not exhaust the
class biholomorphically.

*They do exhaust it smoothly (Step-99 proof repair).* In the Gibbons–Hawking description the cover has \(dn\) distinct
three-dimensional centres \(p_{ij}=(b_i,c_i\rho^j)\in\mathbb R\times\mathbb C\). Coincident complex projections
\(c_i^n=c_{i'}^n\) are separated by real moment coordinates \(b_i\ne b_{i'}\); the corresponding compact \((-2)\)-curves are
residual exceptional curves, not singularities of the metric. No centre lies on the rotation axis: a factor \(z^n\)
would put a deck-fixed singular point at the origin of the canonical fibre, contradicting Şuvaina's freeness; equivalently,
the GH circle collapses at an axis centre, so the lifted deck action fixes that point.

Admissible centre sets are \(d\)-point configurations in the connected three-manifold
\((\mathbb R\times\mathbb C^*)/\mathbb Z_n\cong\mathbb R\times\mathbb C^*\). Hence one may join the resolved-fibre configuration
to one with distinct \(c_i^n\) by an ambient isotopy downstairs and lift it to a compactly supported
\(\mathbb Z_n\)-equivariant isotopy, fixed near infinity and avoiding the axis. Equality of ordinary Chern numbers alone
would not justify an equivariant lift, because the fibre character is additional data. Instead, view the GH circle
bundles as one equivariant family over the moving-centre complement; equivariant homotopy invariance gives an isomorphism
of the endpoint bundles. Equivalently, horizontally lift the base isotopy using a
\(\mathbb Z_n\times S^1\)-invariant family connection, normalized to be the identity near infinity. Since every centre has
trivial stabilizer, the map extends orbitwise across the Hopf fillings. Thus the covers and quotients are equivariantly,
orientation-preservingly diffeomorphic with their marked ends preserved.

So the Kähler Ricci-flat fillers are exactly: Kronheimer ADE spaces, and the Şuvaina family above, which includes the
minimal resolutions of singular fibres (\(d=1\): Wahl rational balls). Every member of the Şuvaina family is
equivariantly diffeomorphic to a smooth-fibre model \(N_{d,n,m}\). Şuvaina's source classifies only the Kähler category.
The material read in this programme supplies no non-Kähler Ricci-flat ALE space; this is not a literature-wide
nonexistence statement.

## 1. Lemma 96.Ş (integral topology of a Şuvaina filler) [P]

Let \(N\) be any non-simply-connected member of the Şuvaina family of §0: the smooth model \(N_{d,n,m}\) or a quotient
of the minimal resolution of a singular invariant fibre, \(d\ge1\), \(n\ge2\), \((m,n)=1\). Boundary statements refer to a
large compact truncation. Then \(\pi_1(N)=H_1(N)=\mathbb Z_n\), \(\chi(N)=d\), \(\partial N\) is the lens space
\(L(dn^2,dnm-1)\), \(H_3(N)=0\), and
\[
\boxed{H_2(N;\mathbb Z)\ \cong\ A_{d-1}(-1)\quad\text{(torsion-free, an isometry of integral lattices)}.}
\]
Moreover the transfer \(\pi^!:H_2(N)\to H_2(M_{d,n})\) maps \(H_2(N)\) onto the full invariant lattice \(H_2(M_{d,n})^{\mathbb Z_n}\).

*Proof.* By §0, \(N\) is equivariantly and orientation-preservingly diffeomorphic to a smooth-fibre model, so it is enough
to treat \(N_{d,n,m}\). The argument below in fact only uses the distinct three-dimensional Gibbons–Hawking centres and
the signless deck permutation, so it applies verbatim to the resolved fibres too. (a) *Model of the cover.* \(M=M_{d,n}=\{xy=\prod_{i=1}^d\prod_{j=0}^{n-1}(z-c_i\rho^j)\}\) is an \(A_{dn-1}\) Milnor fibre
(Gibbons–Hawking with the \(dn\) points arranged as \(d\) regular \(n\)-gons, Şuvaina §5). Label the roots \(p_{ij}=c_i\rho^j\).
\(H_2(M)\) is the sum-zero sublattice \(\Lambda\subset\mathbb Z^{dn}\) with form \(-\sum x_a^2\): an oriented arc from \(p_a\) to \(p_b\)
lifts (circle fibres collapsing at the ends) to a sphere of class \(e_a-e_b\). The deck generator acts by
\((x,y,z)\mapsto(\rho x,\rho^{-1}y,\rho^mz)\); it maps arcs to arcs with their orientation and rotates each circle fibre, so it
acts on \(\Lambda\) by the permutation \(p_{ij}\mapsto p_{i,j+m}\), without signs. Each orbit is one \(n\)-gon.

(b) *Free action and basic invariants.* A fixed point would need \(x=y=0\) and \(z=0\) (as \((m,n)=1\)), but \(z=0\) is not on \(M\)
since \(c_i\ne0\). Hence \(\pi_1(N)=\mathbb Z_n\) (\(M\) is simply connected), \(\chi(N)=\chi(M)/n=d\), \(b_1=b_3=0\), \(b_2=d-1\).
\(H_3(N)\cong H^1(N,\partial N)=0\) because \(H^0(N)\to H^0(\partial N)\) is an isomorphism and \(H^1(N)=0\).

(c) *Torsion-freeness.* \(\partial M\) is connected, so every deck transformation is realized by a path in \(\partial M\): the
inclusion \(\pi_1(\partial N)\to\pi_1(N)=\mathbb Z_n\) is onto. In the exact sequence
\(H_1(\partial N)\to H_1(N)\to H_1(N,\partial N)\to\tilde H_0(\partial N)=0\), therefore \(H_1(N,\partial N)=0\). By Lefschetz duality
and universal coefficients, \(0=H_1(N,\partial N)\cong H^3(N)\supseteq\mathrm{Ext}(H_2(N),\mathbb Z)\cong\mathrm{Tors}\,H_2(N)\).

(d) *Determinant.* With \(H_2(\partial N)=0\), \(H_3(N)=0\), \(T=H_1(N)\), \(F=H_2(N)\) free, the sequence
\(0\to F\to H^2(N)\to H_1(\partial N)\to T\to0\), with \(H^2(N)\cong F^*\oplus\operatorname{Ext}(T,\mathbb Z)\) and the first map
equal to \(Q_N\) followed by the free projection, gives (here \(T^*\) means \(\operatorname{Ext}(T,\mathbb Z)\), of order \(n\), not
\(\operatorname{Hom}(T,\mathbb Z)=0\))
\(|H_1(\partial N)|=|\det Q_N|\,|T|^2\), i.e. \(dn^2=|\det Q_N|\,n^2\), so \(|\det Q_N|=d\).

(e) *Identification.* For a free degree-\(n\) cover, \(\pi_*\pi^!=n\) and \(\pi^!u\cdot\pi^!v=n\,(u\cdot v)\); since \(F\) is free,
\(\pi^!\) is injective with image in \(I=\Lambda^{\mathbb Z_n}\). \(I\) has basis \(O_i-O_d\) (\(O_i\) the orbit sum of the \(i\)-th
\(n\)-gon), and \(\frac1n(O_i-O_d)\cdot(O_j-O_d)=-(\delta_{ij}+1)\): the Gram matrix of \(A_{d-1}(-1)\) in a non-simple basis, of
determinant \(\pm d\). If \(\pi^!F\) had index \(j\) in \(I\), then \(|\det Q_N|=dj^2\); by (d), \(j=1\). \(\square\)

*Coinvariants, all \(d,n\).* Group homology applied to \(0\to\Lambda\to\mathbb Z[\mathbb Z_n]^d\to\mathbb Z\to0\) (regular modules
have vanishing positive group homology) gives \(0\to\mathbb Z_n\to\Lambda_{\mathbb Z_n}\to\mathbb Z^{d-1}\to0\), so
\(\Lambda_{\mathbb Z_n}\cong\mathbb Z^{d-1}\oplus\mathbb Z_n\) for every \(d,n\).

*Charges (unchanged by residual resolution).* In the complex orientation \(W^+=0\) and Gauss–Bonnet gives
\(\int|W^-|^2=8\pi^2(d-1/(dn^2))\), so the rank-subtracted cost is \(c(N)=1-1/(dn^2)\).

*Finite consistency (script).* The coinvariant lattice \(\Lambda_{\mathbb Z_n}\) has rank \(d-1\) and torsion exactly
\(\mathbb Z_n\) in all 102 cases; in the Cartan–Leray sequence \(H_2(N)=\mathrm{coker}(d^3:H_3(\mathbb Z_n)=\mathbb Z_n\to\Lambda_{\mathbb Z_n})\), so
(c) is equivalent to \(d^3\) being onto that torsion, as it must be for \(d=1\) where \(H_2(\text{Wahl ball})=0\) is classical.
The scaled invariant Gram matrix has determinant \(d\) and the invariant basis is saturated in every case.

## 2. Theorem 96.K (full absorption by Kähler Ricci-flat fillers over a ball quotient) [P, as necessary conditions]

*Hypotheses.* \(X\) a compact ball quotient (aspherical, \(\Gamma=\pi_1X\) torsion-free), \(A=c_1^2(X)\); \(V\) a compact oriented
negative Einstein orbifold with isolated singular points whose links are spherical space forms; each point is resolved by
a Kähler Ricci-flat ALE filler \(N_j\) with orientation-matched equivariant end chart and derivative-controlled decay
(Lemma 86.S), the result being diffeomorphic, preserving orientation, to \(M_k=X\#k\overline{\mathbb{CP}}^2\); the transferred
scalar and mixed Seiberg–Witten inequalities of Steps 93–95 apply. *Full absorption* means \(k_b:=k-\sum_jb_2(N_j)=0\).

*Conclusion.* Every filler of positive rank is complex-oriented (reversed Kähler fillers are rational balls, (L1));
the free lattices \(H_2(N_j)\) embed orthogonally and isometrically in \(\ker(H_2M_k\to H_2X)=-I_k\) ((L0), valid since every
\(\pi_1(N_j)\) is finite); and the roots of \(\bigoplus_jH_2(N_j)\) form a full-rank reflection-closed system of norm-two
vectors. By the signed-support classification of Step 95, it is \(\bigoplus_iD_{a_i}\), \(\sum a_i=k\). By Lemma 96.Ş every
Şuvaina lattice is of type \(A\), so a Şuvaina filler of positive rank can occur only as an \(A_1\) summand of a \(D_2\) block
(\(d=2\)) or as a whole \(D_3=A_3\) block (\(d=4\)); every block \(D_a\), \(a\ge4\), is a single Kronheimer \(D_a\) filler
(\(D_a\) is irreducible). Wahl balls (\(d=1\)), of either orientation, absorb no rank and only add cost. The exact costs are
\[
c(D_2)\in\{1,\ \tfrac{11}8\text{ or more},\ \tfrac74\text{ or more}\},\quad
c(D_3)\in\{\tfrac34,\ \ge\tfrac{15}{16}\},\quad c(D_a)=1-\tfrac1{4(a-2)}\ (a\ge4),
\]
(Kronheimer value first; Şuvaina substitutes cost \(1-1/(dn^2)\) with \(n\ge2\)), plus \(1-1/n^2\) per complex Wahl ball and
\(\frac29(1-1/n^2)\) per reversed one, and the transferred condition is
\(\sum c\le\beta(k,A)=k(5y+1)/[18(1+y)]\), \(y=\sqrt{1-3k/A}\). Every block of rank \(\le5\) has cost \(>\)rank\(/6\) in all
variants, so:

> **Full absorption of all exceptional ranks by Kähler Ricci-flat ALE fillers over a ball quotient requires a Kronheimer
> \(D_a\) filler with \(a\ge6\); hence \(k\ge6\). At \(k=6\) the only possibility is a single \(D_6\) filler with no Wahl points,
> and it requires \(A\ge3675/64\), so \(A\ge63\). Şuvaina fillers and Wahl balls can only raise every threshold of the
> Step-95 table.**

The theorem gives necessary curvature-and-lattice data only. A surviving configuration still needs (i) integral gluing:
the finite-index (index \(2^q\) for \(q\) D-blocks) inclusion of \(\bigoplus D_{a_i}\) in \(I_k\) must be compatible with the
linking forms of the prism-manifold links; (ii) a compact orbifold bulk realizing the complement topology; (iii) a
negative Einstein orbifold metric on it. None is known. Nothing here constructs an orbifold, an Einstein metric, or a
minimizing sequence.

## 3. The retained-rank and Wahl sector: corrected integral gluing (Steps 98–99)

For \(k_b>0\), or for configurations containing Wahl points, the transferred aggregate inequalities can still fail
(Step 95: two \(D_2\) at \(k=5\), \(k_b=1\)), but once they pass they carry no class-by-class information. The former
Question 96.W asserted an index and full linking anti-isometry without deriving the boundary map. Step 98 supplied the
Mayer--Vietoris/Frattini argument; the independent Step-99 reading completes the torsion block, improves the uniform
realization range, and identifies its precise relation to the resolution filling.

*Setting.* \(M=X\#k\overline{\mathbb{CP}}^2\), where \(X\) is aspherical and \(\pi_1(X)\) is torsion-free (e.g. a ball
quotient). Let \(B_1,\ldots,B_t\subset M\) be disjoint embedded Wahl balls,
\(B_j=B_{n_j,a_j}\), with \(H_1(B_j)=\mathbb Z_{n_j}\), \(H_2(B_j)=0\), and oriented link
\(Y_j=L(n_j^2,n_ja_j-1)\). Assume \(W=\overline{M\setminus\bigcup B_j}\) is connected and write
\[
Y=\partial W=\bigsqcup_j(-\partial B_j),\quad
G=H_1(Y)=\bigoplus_j\mathbb Z_{n_j^2},\quad
K=\ker[G\to\bigoplus_jH_1(B_j)]=\bigoplus_jn_j\mathbb Z_{n_j^2}.
\]
Let \(i:G\to H_1(W)\) be the boundary map.

**Proposition 98.W (integral gluing of Wahl balls; repaired Step 99) [P].** In this setting:
1. \(i=0\);
2. \(0\to H_2(W)\to H_2(M)\to K\to0\), and \(H_1(W)\cong H_1(M)\cong H_1(X)\);
3. torsion in \(H_2(W)\) maps isomorphically onto torsion in \(H_2(M)\). Thus, for
   \(L=H_2(W)/\operatorname{Tor}\) and \(U=H_2(M)/\operatorname{Tor}\),
   \[
   0\to L\to U\to K\to0,\qquad [U:L]=\prod_jn_j,\qquad |\det L|=\prod_jn_j^2;
   \]
4. without any extra hypothesis on \(H_1(X)\),
   \[
   0\to L\xrightarrow{Q_L}L^*\to G\to0.
   \]
   The discriminant bilinear form of \(L\) is the linking form of \(\partial W\), up to the single global convention
   sign, and under this identification the subgroup \(U/L\) is the specified metabolizer \(K\subset G\).
5. the aspherical classifying map splits off the host lattice:
   \[
   L=Q_X\oplus L_0,\qquad L_0\subset-I_k.
   \]
   Hence host directions cannot supply the Wahl discriminant. In particular \(k>0\), and
   \(k\ge\max_p\#\{j:p\mid n_j\}\).

*Proof.* Each boundary map \(H_1(Y_j)=\mathbb Z_{n_j^2}\to H_1(B_j)=\mathbb Z_{n_j}\) is onto. A finite
\(\pi_1(B_j)\) maps trivially into torsion-free \(\pi_1(M)\), so Mayer--Vietoris gives \(\ker i+K=G\).
Since \(K\subset\Phi(G)\), the Frattini subgroup, \(\ker i=G\), proving (1). The relevant \(H_2\) and \(H_1\)
segments then give (2). The pair sequence
\[
0\to H_1(W)\to H_1(W,Y)\to\mathbb Z^{t-1}\to0
\]
and Lefschetz duality/UCT identify the torsion orders of \(H_2(W)\), \(H_1(W)\), \(H_1(M)\), and \(H_2(M)\).
The injection on \(H_2\) is therefore an isomorphism on torsion, giving (3).

For (4), write the pair map after group splittings as
\[
H_2(W)=L\oplus T\ni(l,t)\longmapsto(Q_Ll,\varphi(l)+\psi(t))\in L^*\oplus T'=H_2(W,Y).
\]
The torsion map \(\psi:T\to T'\) is an isomorphism by (3). Eliminating it leaves
\(0\to L\xrightarrow{Q_L}L^*\to G\to0\). In the usual relative-intersection definition of boundary linking,
torsion contributes zero to the integer-valued absolute--relative pairing, so the induced form is \(\pm Q_L^{-1}\bmod1\).
Naturality identifies the image of \(U/L\) with \(K\); it is isotropic and has order \(\sqrt{|G|}\).

For (5), the classifying/collapse map \(c:M\to X\) is null on each \(B_j\), because its restriction lifts to the
contractible universal cover of aspherical \(X\). Relative cohomology, excision and duality therefore place
\(c^!H_2(X)\) in the image of \(H_2(W)\). The unimodular host lattice splits off orthogonally, leaving
\(L_0\subset-I_k\). The displayed consequences follow. \(\square\)

**Corollary 98.V (uniform four-coordinate realization, with low-rank obstructions) [P, repaired Step 99].** For any
\((n_j,a_j)\), orientations, and \(k\ge4t\), there is an index-\(\prod n_j\) sublattice
\(L_0\subset-I_k\) realizing the required direct-sum discriminant forms and the specified metabolizer \(K\). For each
point put \(q_j=n_ja_j-1\) and choose
\[
N_j\equiv-\sigma_jq_ju_j^2\pmod{n_j^2},\qquad (u_j,n_j)=1.
\]
Then \((N_j,n_j)=1\), and Lagrange gives \(N_j=v_{j1}^2+\cdots+v_{j4}^2\). On disjoint four-coordinate blocks set
\[
L_0=\bigcap_j\{x:x\cdot v_j\equiv0\pmod{n_j}\}.
\]
The content of \(v_j\) is coprime to \(n_j\), so each congruence map is onto. The class \(v_j/n_j\) has exact order
\(n_j^2\) and self-pairing
\[
-N_j/n_j^2\equiv\sigma_jq_ju_j^2/n_j^2\pmod1;
\]
its multiple \(v_j=n_j(v_j/n_j)\) generates the corresponding factor of \(K\). Orthogonal blocks give the result.

Four is a sharp uniform one-point bound: for \((n,a,\sigma)=(8,1,-1)\), every target norm is \(7\bmod8\), hence is not
a sum of three squares. Below \(4t\) the bilinear condition can obstruct. For example, complex-oriented \(B_{2,1}\)
requires norm \(3\bmod4\), impossible with one or two squares. The exact script
`scripts/step99_wahl_four_coordinate_check.py` → `data/step99/wahl_four_coordinate_check.json` checks 158 one-point cases
through \(n=16\), both signs: all determinants, Smith forms and square classes pass; minimum square ranks occur with
counts \(81,46,19,12\) for ranks \(1,2,3,4\). The older five-coordinate script remains a valid nonoptimal check.

**Relation to Theorem 55.5 (not an independent abstract condition).** Replace the balls by their compatible
minimal-resolution plumbings \(C=\coprod C_{n_j,a_j}\) and set \(Y'=W\cup C\). The boundary anti-isometry glues
\(L\oplus C\) to a unimodular lattice by the graph of the discriminant anti-isometry. Consequently \(C\) and \(L\) are
primitive and \(C^\perp=L\). At \(k=1\), this is exactly Theorem 55.5: the complement is
\(\langle-n^2\rangle\), and the complex-oriented compatibility is
\[
1-na\equiv u^2\pmod{n^2},
\]
equivalently \(n\) odd or \(8\mid n\). In higher rank, a bare chain embedding into *some* unimodular lattice can be
weaker than compatibility with the prescribed rational-filling overlattice \(-I_k\), but compatible complement data
already supply the abstract primitive-chain embedding. The remaining topological work is geometric realization of
embedded balls/plumbings and the prescribed complement/degree-one map, plus characteristic or spin\(^c\) refinements;
it is not a second independent bilinear test.

**Consequence for the Wahl sector.** Aggregate transfer still carries no class placement once its budget passes.
Integral topology now says more precisely: the bilinear condition may exclude low-rank configurations, but is uniformly
realizable for \(k\ge4t\); it also implies the abstract resolution-chain primitivity. Even a compatible topological
realization would not construct a negative Einstein orbifold. The genuinely new information still needed is geometric
realization/refinement and singular analysis: APS/Dedekind terms coupled to another global identity, orbifold
Seiberg--Witten supply, or local type-T analysis.

The Step-94 reading through the norm-four vector \(e_1+e_2+e_3+e_4\) is withdrawn. Corollary 98.V in its repaired form
supersedes it.

## 4. What this changes

Smooth transfer plus integral topology decides the Kähler-filler full-absorption sector at the level of transferred
curvature and lattice-embedding data: it requires a high-rank Kronheimer \(D_{\ge6}\) block. The index-\(2^q\)
prism-linking compatibility, compact complement, and negative Einstein metric remain unconstructed. The undecided
singular sectors are:
- (a) \(D_{\ge6}\) full absorption: prism-linking compatibility and geometric/Einstein existence;
- (b) retained-rank/Wahl configurations: low-rank bilinear restrictions, geometric realization and characteristic
  refinements, then APS/Dedekind, orbifold-monopole or type-T information;
- (c) non-Kähler Ricci-flat ALE fillers, none supplied by the material read here.
