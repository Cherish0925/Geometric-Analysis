# TTCS Independent Branch Record

```json
{
  "step_id": 99,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step96_suvaina_lattice_and_kahler_filler_theorem.md",
    "Knowledge/objects/papers/ALE-Ricci-flat-Kahler-metrics-and-deformations-of-quotient-surface-singu--9db598b6c84c--5ab7b434e210/object.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/state_of_problems_1_4.md",
    "Sessions/S1003A02/workspace/notes/step58_consolidated_hypothesis_ledger.md",
    "Sessions/S1003A02/workspace/notes/step94_filler_screen_dichotomy.md",
    "Knowledge/objects/papers/Einstein-Metrics-Symplectic-Minimality-and-Pseudo--a623e9917b57--dd585f36cd43/object.md"
  ]
}
```

## Task

Independently verify the Step-98 extension of Lemma 96.Ş to minimal resolutions of singular invariant fibres and the synchronized scientific scope in the theorem package, front matter, hypothesis ledger, and Step-94 binding correction. Read Şuvaina's primary source as grounding. Check the equivariant Gibbons–Hawking-centre isotopy, topology, H1/H2, determinant and transfer-index arguments; distinguish source statements from the new diffeomorphism argument. Then inspect whether package/front-matter claims about 96.K, 98.W/98.V, ALE decay, Armstrong/Problem 4, and the conditional T_AK statement have exact hypotheses and no global overstatement. Return concrete mathematical corrections only where warranted.

## Output

# Scientific verification memo

## 1. Şuvaina source versus the Step-98 addition

Şuvaina’s paper supplies the following ingredients:

- Proposition 4.4: the universal cover of a non-simply-connected ALE Ricci-flat Kähler surface is hyperkähler, and the deck group is finite cyclic.
- Theorem B: the surface is the minimal resolution of a fibre of a one-parameter \(\mathbb Q\)-Gorenstein deformation; the fibre may itself be singular.
- Proposition 2.3: the relevant invariant fibres have
  \[
  xy=\prod_{i=1}^{d}(z^n-c_i^n),
  \qquad
  (x,y,z)\mapsto(\rho x,\rho^{-1}y,\rho^m z).
  \]
- Theorem 3.1 and the discussion preceding it: repeated complex roots produce rational double points in the chosen complex structure, while distinct real moment parameters \(b_i\) give their minimal resolution in the smooth Gibbons–Hawking manifold.
- Section 5: for smooth fibres, the \(dn\) Gibbons–Hawking centres form \(d\) regular \(n\)-gons, and the cyclic action rotates each polygon while translating the circle fibre.

The paper does **not** state that resolved singular fibres are equivariantly diffeomorphic to smooth-fibre models. That is the new Step-98 argument. This distinction is presented correctly in the revised Step-96 note and the theorem package.

## 2. Equivariant centre isotopy

For a resolved invariant fibre, the Gibbons–Hawking centres can be written, up to the source’s conjugation and sign conventions, as
\[
p_{ij}=(b_i,c_i\rho^j)\in\mathbb R\times\mathbb C.
\]

The proposed isotopy is mathematically sound:

1. If \(c_i^n=c_{i'}^n\), the complex projections coincide as cyclic orbits. Smoothness of the resolved metric requires the associated three-dimensional centres to remain distinct, which is supplied by distinct \(b_i\) within each repeated-root cluster. Coincidence of both \(b_i\) and the complex projection would leave a Gibbons–Hawking orbifold point rather than the smooth minimal resolution.

2. Every \(c_i\) is nonzero. A centre with \(c_i=0\) lies on the rotation axis. The base rotation fixes that centre, and the circle fibre collapses there, so the deck transformation fixes the corresponding point of the four-manifold. This contradicts freeness.

3. The centre representatives \(c_i\) may therefore be perturbed slightly in the free locus so that all \(c_i^n\) become distinct. Equivariant configuration space in the three-dimensional free locus is path connected, so the perturbation extends to a compactly supported \(\mathbb Z_n\)-equivariant isotopy of \(\mathbb R^3\), equal to the identity near infinity.

4. The principal \(S^1\)-bundle over the complement of the centres has Chern number \(-1\) on every small linking sphere. The isotopy preserves these classes and therefore identifies the bundles.

One proof sentence should be strengthened here. Equality of ordinary Chern classes alone does not record the chosen cyclic lift. A fully explicit version is:

> Choose a \(\mathbb Z_n\times S^1\)-invariant connection and integrate the invariant horizontal lift of the compactly supported base isotopy, normalized to be the identity near infinity. The resulting bundle isomorphism commutes with the deck action and extends across each Hopf filling.

This supplies the equivariant lift, fixes the character at infinity, and proves an orientation-preserving diffeomorphism with the end marking unchanged.

## 3. Topology and lattice of the quotient

Let \(M\) denote the \(dn\)-centre cover and \(N=M/\mathbb Z_n\).

### Cover lattice and deck action

The standard Gibbons–Hawking identification gives
\[
H_2(M;\mathbb Z)=
\Lambda=\left\{(x_a)\in\mathbb Z^{dn}:\sum_a x_a=0\right\},
\qquad
Q_M(x,x)=-\sum_a x_a^2.
\]
An arc from \(p_a\) to \(p_b\) gives the class \(e_a-e_b\).

The deck transformation preserves the orientation of the base arc and translates the circle fibre orientation-preservingly. Its action is therefore the unsigned permutation
\[
p_{ij}\longmapsto p_{i,j+m}.
\]
Since \((m,n)=1\), each fixed \(i\) gives one orbit of length \(n\).

### Fundamental and rational homology groups

The cover \(M\) is simply connected and the action is free, hence
\[
\pi_1(N)=H_1(N;\mathbb Z)=\mathbb Z_n.
\]
Also
\[
\chi(M)=dn,\qquad \chi(N)=d.
\]
Finite-cover transfer over \(\mathbb Q\) gives
\[
H_q(N;\mathbb Q)\cong H_q(M;\mathbb Q)^{\mathbb Z_n}.
\]
The invariant part of \(H_2(M;\mathbb Q)\) has dimension \(d-1\), while \(H_3(M)=0\). Thus
\[
b_2(N)=d-1,\qquad b_3(N)=0.
\]

Integral \(H_3(N)=0\) follows from
\[
H_3(N)\cong H^1(N,\partial N),
\]
the isomorphism \(H^0(N)\to H^0(\partial N)\), and \(H^1(N;\mathbb Z)=0\).

### Torsion in \(H_2\)

The cover of the link is connected, so
\[
\pi_1(\partial N)\longrightarrow\pi_1(N)=\mathbb Z_n
\]
is onto. Hence \(H_1(N,\partial N)=0\). Lefschetz duality and universal coefficients then give
\[
\operatorname{Ext}(H_2(N),\mathbb Z)=0,
\]
so \(H_2(N;\mathbb Z)\) is free.

### Determinant

Put \(F=H_2(N;\mathbb Z)\), \(T=H_1(N;\mathbb Z)\), and \(Y=\partial N\). The exact sequence
\[
0\longrightarrow F\longrightarrow H^2(N)
\longrightarrow H_1(Y)\longrightarrow T\longrightarrow0
\]
has
\[
H^2(N)\cong F^*\oplus\operatorname{Ext}(T,\mathbb Z).
\]
Projection of the first map to \(F^*\) is the intersection form \(Q_N\). Therefore
\[
|H_1(Y)|=|\det Q_N|\,|T|^2.
\]
Using
\[
|H_1(Y)|=dn^2,\qquad |T|=n
\]
gives
\[
|\det Q_N|=d.
\]

### Transfer index

The invariant lattice \(I=\Lambda^{\mathbb Z_n}\) has basis
\[
O_i-O_d,\qquad O_i=\sum_{j=0}^{n-1}e_{ij}.
\]
With the form divided by \(n\),
\[
\frac1n (O_i-O_d)\cdot(O_j-O_d)=-(\delta_{ij}+1),
\]
whose determinant has absolute value \(d\). Thus \((I,\frac1nQ_M)\cong A_{d-1}(-1)\).

For transfer \(t=\pi^!:H_2(N)\to H_2(M)\),
\[
t(u)\cdot t(v)=n\,Q_N(u,v).
\]
If \(t(H_2(N))\) had index \(j\) in \(I\), then
\[
|\det Q_N|=d\,j^2.
\]
Since the preceding calculation gives \(|\det Q_N|=d\), one has \(j=1\). Therefore
\[
H_2(N;\mathbb Z)\cong A_{d-1}(-1)
\]
and transfer is onto the full invariant lattice. This argument also covers \(d=1\), with the rank-zero lattice and determinant convention \(1\).

The curvature cost
\[
c(N)=1-\frac1{dn^2}
\]
then follows from ALE Gauss–Bonnet, \(\chi(N)=d\), and \(W^+=0\) in the complex orientation.

## 4. Consequences for Theorem 96.K and ALE decay

The extension does not alter Theorem 96.K:

- every positive-rank Şuvaina filler contributes an \(A_{d-1}\) root lattice;
- full-rank embedding in \(-I_k\) permits such a component only as \(A_1\subset D_2\) or \(A_3=D_3\);
- blocks \(D_a\), \(a\ge4\), must come from a single Kronheimer filler;
- the cost comparison still forces a Kronheimer \(D_a\) with \(a\ge6\);
- at \(k=6\), the sole configuration is \(D_6\), with
  \[
  A\ge\frac{3675}{64},
  \]
  and the ball-quotient divisibility \(9\mid A\) gives \(A\ge63\).

The documents correctly keep this theorem within the Kähler Ricci-flat ALE category and do not infer the absence of non-Kähler Ricci-flat ALE spaces.

The decay attribution is also scientifically correct:

- Şuvaina’s Definition 1.1 records order-four metric decay but not the needed derivative estimates by itself.
- For \(A\)-type and Şuvaina spaces, all derivative estimates follow from the centred finite-centre Gibbons–Hawking expansion and passage to the free finite quotient.
- For Kronheimer \(D/E\) spaces, the separate Bando–Kasue–Nakajima input supplies the derivative-controlled ALE coordinates.

## 5. Proposition 98.W and Corollary 98.V

The Mayer–Vietoris argument is correct. The key group-theoretic step is
\[
\ker i+K=H_1(Y),
\qquad
K\subset\Phi(H_1(Y)),
\]
where \(\Phi\) is the Frattini subgroup. Hence \(i=0\). It follows that
\[
\operatorname{coker}\bigl(H_2(W)\to H_2(M)\bigr)
\cong\bigoplus_j\mathbb Z_{n_j},
\]
torsion in \(H_2(W)\) maps isomorphically to torsion in \(H_2(M)\), and the free complement lattice has index
\[
\prod_j n_j.
\]

When \(H_1(X)\) is torsion-free, the further identification
\[
L^*/L\cong\bigoplus_j\mathbb Z_{n_j^2}
\]
with the lens-space linking forms is valid.

The five-coordinate construction in 98.V is also correct. For a primitive vector \(v\) with
\[
v^2=-N,\qquad
N\equiv-\sigma(na-1)u^2\pmod{n^2},
\]
the lattice
\[
L=\{x:x\cdot v\equiv0\pmod n\}
\]
has index \(n\), discriminant group generated by \(v/n\) of order \(n^2\), and the required self-pairing. Lagrange’s four-square theorem supplies \(N=1+\sum_{r=1}^4x_r^2\).

### Textual corrections warranted

Several summaries use broader wording than 98.W establishes:

1. In `state_of_problems_1_4.md` §§1 and 5.1, “so it never obstructs” should read:
   > it supplies no bilinear obstruction in the proven stable range \(k\ge5t\), provided the relevant discriminant identification is available.

2. In `theorem_package_v1.md` §24.4 and the corresponding late summary in `step58_consolidated_hypothesis_ledger.md`, add:
   > The identification with the direct sum of lens linking forms requires torsion-free \(H_1(X)\). If \(H_1(X)\) has torsion, the torsion-linking block of \(W\) remains to be incorporated.

3. The “Consequence for the Wahl sector” in the Step-96 note should carry the same \(H_1(X)\)-torsion qualification. For a general ball quotient, torsion-free \(\pi_1(X)\) does not imply torsion-free \(H_1(X)\).

The Step-94 binding correction already states these hypotheses accurately.

## 6. Armstrong/Problem 4 and the \(T_{AK}\) statement

The source attribution is correctly repaired. LeBrun’s Proposition 2.4 directly proves that a compact almost-Kähler Einstein four-manifold has a point where \(s^*=s\), equivalently a torsion zero. The elementary bundle computation
\[
E=\Lambda^{0,2}\otimes T^{1,0},\qquad
c_2(E)=c_2+2c_1^2=5\chi+6\tau
\]
is correct, and
\[
5\chi+6\tau=\chi+2(2\chi+3\tau)>\chi>0
\]
for a nonzero-scalar Einstein metric with the almost-complex orientation. Armstrong 2002 is not needed for this step.

One front-matter sentence needs a transversality qualification. Replace

> “with total signed index \(5\chi+6\tau\)”

by

> “if the torsion zeros are isolated, their local indices sum to \(5\chi+6\tau\); in general \(c_2(E)\) is represented by the localized Euler class or by the zero cycle of a transverse perturbation.”

Finally, the conditional deduction
\[
T_{AK}\ge2\pi^2k
\]
is algebraically correct from
\[
s^2V=32\pi^2c_1^2+16T_{AK},
\qquad
\int s^2\ge32\pi^2A,
\qquad
c_1^2=A-k.
\]
Its statement should explicitly require that the almost-Kähler orientation agrees with the orientation in
\[
M=X\#k\overline{\mathbb{CP}}^2.
\]
With the opposite orientation, the relevant topological number is \(2\chi-3\tau\), not \(A-k\). The deduction uses only the first displayed identity; the canonical-cycle identity is not needed.