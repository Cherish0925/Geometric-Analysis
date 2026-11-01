# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 55,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step55_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step55_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematics of the Step-55 note (k=1 orbifold gate for P=int|Ric°|^2 on M = X # CP2bar, X a compact ball quotient). Check carefully and report concrete errors with corrections: (1) the two-orientation ALE charge formula (1.1) c_± = 2/|Γ| − 2χ ∓ 3τ ∓ 3η with η = −4 s(q,n) (Dedekind sum), its sign conventions as fixed by Burns, Eguchi–Hanson, A_{n−1}, and the numerically verified LeBrun O(−n) value P = 8π²(n−2)²/n; (2) the ledger identities (1.2) T_+^orb(V) = T_+(M) + c_+(N) and (1.3); (3) Lemma 55.1 (degree-one/free-indecomposability argument that orbifold bubble regions have H_2 ⊂ ZE, including whether the one-sided SW vanishing with a PSC orbifold cap is a correct/standard input); (4) Prop 55.3: the claim that m=1,2 cyclic-end b2=1 bubbles have c_+=1 (linking-form restriction q a unit square mod m^2), the surviving lists, and the noncyclic D_5, D_9, E_8 analysis (orientation and linking-form compatibility, the trefoil-trace realization); (5) Prop 55.4 (T-singularity Milnor fibres have charge 0 in complex orientation and −4(1−1/n²) reversed; Ricci-flat Kähler ALE on them); (6) Theorem 55.5: π1 pushout, degree one, K unimodular negative definite of rank r+1, the H_1-torsion argument forcing primitivity (gcd(o,n)=1 ⇒ o=1), and the discriminant criterion 1−na unit square mod n² ⇔ n odd or 8|n — including whether the discriminant form of the T-chain is ⟨(1−na)/n²⟩ and whether the anti-isometry condition is stated with the right sign; (7) Prop 55.6 blow-up counting argument (Σ(−D_j²) ≤ 3r+1 over r+1 exceptional components; T-chains have Σb_i = 3r+1) and its use of SW/general type; (8) Lemma 55.8 and the collapse discussion, especially the claim that a collapsed region with τ(C) = −1 would make the ledger favorable to absorption. Also say whether the n=3 example ([5,2] chain realized by 2E1+E2 and E2+E3 in #3CP2bar) is correct as a lattice/topology statement, and whether Theorem 55.7's trichotomy follows. Write a direct mathematical memo.

## Integrated Scientific Memo

# Mathematical memo: verification of Step 55

The ALE charge formulas, their orientation conventions, the orbifold ledger, and the T-chain discriminant/primitivity argument are correct. The principal errors are in extending these results to an exhaustive bubble classification, in the original proof of Proposition 55.6, and in the collapse ledger. The detailed version of Theorem 55.7 does not follow as written.

## 1. ALE charges and orientation conventions

Use the outward orientation on the ALE link and the APS convention
\[
\tau(N)=\frac1{12\pi^2}\int_N\bigl(|W^+|^2-|W^-|^2\bigr)-\eta_N.
\]
Chern–Gauss–Bonnet is
\[
8\pi^2\left(\chi(N)-\frac1{|\Gamma_\infty|}\right)
=\int_N\left(|W^+|^2+|W^-|^2-\frac12|\Ric^\circ|^2+\frac{s^2}{24}\right).
\]
Eliminating one Weyl term gives
\[
P(N)=4\int_N|W^\pm|^2+\frac1{12}\int_Ns^2+8\pi^2c_\pm(N),
\]
\[
\boxed{c_\pm(N)=\frac2{|\Gamma_\infty|}-2\chi(N)\mp3\tau(N)\mp3\eta_N.}
\]
Thus (1.1) and
\[
P(N)\ge8\pi^2\max\{c_+,c_-,0\}
\]
are correct, subject to the stated decay needed for the boundary formulas.

For the quotient action \((z_1,z_2)\mapsto(\zeta z_1,\zeta^qz_2)\), the choice
\[
\eta(n,q)=-4s(q,n)
\]
is consistent with this signature formula. Reversing orientation changes \(\tau,\eta\) to their negatives and exchanges \(c_+,c_-\).

The checks are:
\[
\begin{array}{c|cc}
N&c_+&c_-\\ \hline
\text{Burns}&1&-5\\
\text{Eguchi--Hanson}&0&-6\\
A_3&0&-15\\
A_6&0&-192/7\\
B_{2,1}=\mathrm{EH}/\mathbb Z_2&0&-3 .
\end{array}
\]
More generally, for \(A_{n-1}\),
\[
\eta(n,-1)=\frac{(n-1)(n-2)}{3n},\qquad
(c_+,c_-)=\left(0,-4n+\frac4n\right).
\]

For \(\mathcal O(-n)\), \(q=1\), \(\chi=2\), \(\tau=-1\), and
\[
\eta(n,1)=-\frac{(n-1)(n-2)}{3n}.
\]
Therefore
\[
c_+=\frac{(n-2)^2}{n}.
\]
Since LeBrun’s metric is scalar-flat Kähler in its complex orientation, \(W^+=0\), and hence
\[
\boxed{P(g_{\rm LeB})=8\pi^2\frac{(n-2)^2}{n}.}
\]
This is an exact consequence, not merely a numerical prediction. The supplied quadrature script is consistent with it.

A minor inherited typo in Step 54 should also be removed: reversing Burns exchanges \(1,-5\); it does not leave the \(+\)-charge equal to \(1\). The maximum two-orientation bound remains \(1\).

## 2. Ledger identities

Let \(M=V^\circ\cup_LN\), with \(L=S^3/\Gamma_\infty\). Then
\[
\chi(M)=\chi(V^\circ)+\chi(N),\qquad
\tau(M)=\tau(V^\circ)+\tau(N),
\]
whereas
\[
\chi_{\rm orb}(V)=\chi(V^\circ)+\frac1{|\Gamma_\infty|},\qquad
\tau_{\rm orb}(V)=\tau(V^\circ)-\eta_N.
\]
Consequently
\[
\boxed{T_+^{\rm orb}(V)=T_+(M)+c_+(N).}
\]
Thus (1.2) has the correct sign.

For scalar-flat \(N\), set
\[
w(N)=\frac1{2\pi^2}\int_N|W^+|^2,\qquad
C_+(V)=\frac1{2\pi^2}\int_V|W^+|^2+\frac1{96\pi^2}\int_Vs^2.
\]
Then
\[
\frac{P(V)}{8\pi^2}=C_+(V)-T_+^{\rm orb}(V),\qquad
\frac{P(N)}{8\pi^2}=w(N)+c_+(N),
\]
and therefore
\[
\boxed{\frac{P(V)+P(N)}{8\pi^2}
=C_+(V)+w(N)-T_+(M).}
\]
This verifies (1.3). For several attachment regions, replace \(c_+\) and \(w\) by their sums.

An effective bubble subtree need not possess one complete smooth ALE metric. The valid interpretation is a reconstructed topological region whose curvature integrals are sums over the limiting pieces. Internal link terms cancel, so the ledger telescopes.

Under lower semicontinuity and (U), one obtains the **additive** restriction
\[
\boxed{\sum_j\max\{c_+(N_j),c_-(N_j),0\}<1,}
\]
not merely a separate restriction at each point. The condition for beating \(8\pi^2\) is
\[
C_+(V)+\sum_jw(N_j)<A.
\]
Nonnegativity of \(P(V)\) alone tests the \(+\)-charge; the full two-orientation restriction also uses the other ALE identity.

## 3. Lemma 55.1: valid conditional reduction, but not simple connectivity

Write
\[
G_A=\pi_1(V^\circ),\quad G_N=\pi_1(N),\quad H=\pi_1(L).
\]
Since the finite group \(H\) maps trivially into the torsion-free group \(\Gamma\), van Kampen yields
\[
\Gamma\cong
\left(G_A/\langle\!\langle H\rangle\!\rangle\right)*
\left(G_N/\langle\!\langle H\rangle\!\rangle\right).
\]
Free indecomposability puts \(\Gamma\) in exactly one factor.

If it were the bubble factor, the degree-one classifying map \(M\to X\) would factor through the cone compactification of \(N\). Rational Poincaré duality then gives
\[
Q_X\hookrightarrow Q_N,\qquad b^+(N)\ge b^+(X)\ge3.
\]
The stipulated SW vanishing excludes this possibility. Thus the image of \(\pi_1(N)\) in \(\Gamma\) is trivial, and \(N\to X\) lifts to the contractible universal cover. Mayer–Vietoris across rational homology spheres now gives the orthogonal injection
\[
H_2(N;\mathbb Q)\hookrightarrow\ker\bigl(H_2(M;\mathbb Q)\to H_2(X;\mathbb Q)\bigr)=\mathbb QE.
\]
Hence \(b_2(N)\le1\), and at most one attachment region has \(b_2=1\).

The conclusion should distinguish coefficients: the rational image lies in \(\mathbb QE\); integral classes have image in \(\mathbb ZE\).

### The one-sided SW input

The two-sided PSC rational-homology-sphere splitting vanishing is the usual neck-stretching input. The one-sided statement is a valid extension of that mechanism, but “PSC orbifold cap” is not by itself a complete citation or proof. It requires:

* puncturing the orbifold chart and bending equivariantly to a PSC cylindrical end with spherical-space-form cross-section;
* accounting for the finitely many boundary flat reducible limits;
* choosing a small self-dual perturbation away from all their affine reducible walls, using \(b^+(N)>0\);
* the corresponding neck-stretching compactness theorem.

PSC excludes irreducibles; the generic perturbation excludes reducibles. For an effective subtree, one must also justify PSC compactification by gluing its piecewise caps. Step 55 appropriately records this as a hypothesis, but should not describe the exact orbifold-cap formulation as already supplied by an unspecified standard theorem.

Most importantly,
\[
\boxed{\pi_1(N)\to\Gamma\text{ trivial does not imply }\pi_1(N)=1.}
\]
What follows is
\[
\pi_1(N)/\langle\!\langle\pi_1(L)\rangle\!\rangle=1.
\]
This distinction invalidates the unrestricted use of Proposition 55.3.

The exclusion of Kronheimer bubbles nevertheless survives: their \((-2)\)-classes cannot inject into the integral line generated by \(E\), whose nonzero squares are \(-m^2\).

## 4. Proposition 55.3: correct restricted calculations, incomplete classification

### Simply connected cyclic-end regions

If \(N\) is simply connected, \(b_2(N)=1\), and its generator maps to \(mE\), then
\[
Q_N=\langle-m^2\rangle,\qquad |H_1(L)|=m^2.
\]
With the quotient-link orientation fixed by \(\partial\mathcal O(-m^2)\), the boundary linking form is \(\langle+1/m^2\rangle\). Equivalently, the lattice discriminant is \(\langle-1/m^2\rangle\). Matching the lens linking form forces \(q\) to be a unit square modulo \(m^2\).

The note’s notation \(\langle\pm1/m^2\rangle\) is too loose: the oriented sign must be fixed. Allowing both signs would also allow negative unit squares and would destroy the stated \(m=2\) conclusion.

With the correct oriented restriction,
\[
c_+=\frac2{m^2}-1-3\eta(m^2,q),\qquad
c_-=\frac2{m^2}-7+3\eta(m^2,q).
\]
For \(m=1\), and for \(m=2\) with its only admissible \(q=1\bmod4\), \(c_+=1\). The \(8\pi^2\) exclusion and its realization by LeBrun’s \(\mathcal O(-4)\) are correct **under simple connectivity**.

The listed initial survivors also check:
\[
m=3,\ q=4,7:\quad(c_+,c_-)=(-23/9,-5),
\]
and
\[
m=4,\ q=9:\quad c_+=1/4.
\]
These are arithmetic possibilities, not an existence classification of fillings or critical ALE metrics. Lens surgeries realize some examples; they do not establish realization of every listed parameter.

### Why the unrestricted cyclic-end exclusion fails

Let \(t=|\operatorname{Tor}H_1(N)|\). Boundary normal generation implies \(H_1(L)\to H_1(N)\) is onto. For a rank-one region of the type in Lemma 55.1, the relative homology sequence gives
\[
\boxed{|H_1(L)|=m^2t^2.}
\]
Thus the cyclic group order need not equal \(m^2\), and the boundary form is not determined by \(\langle-m^2\rangle\) alone.

A concrete local topological counterexample to the claimed charge restriction is
\[
N=\bar B_{t,a}\,\natural\,
(\overline{\mathbb{CP}}^2\setminus B^4).
\]
It has cyclic boundary, \(\pi_1(N)=\mathbb Z_t\) normally generated by the boundary, and \(Q_N=\langle-1\rangle\). Its charges are
\[
(c_+,c_-)=\left(-3+\frac4{t^2},-5\right).
\]
For \(t=2\), the end is of quotient type \(L(4,3)\) and the charges are \((-2,-5)\).

This disproves the inference from Lemma 55.1 to “every cyclic-end region carrying \(E\) costs \(8\pi^2\).” It does **not** construct a critical ALE metric or prove that this region embeds as a minimizing bubble region in the specified \(M\).

### ADE ends

For an \(SU(2)\) end in the Kronheimer orientation,
\[
\eta_\Gamma=\frac{2/|\Gamma|+r-2}{3}.
\]
For a negative rank-one region,
\[
\boxed{c_+=1-r,\qquad c_-=\frac4{|\Gamma|}+r-9.}
\]
Reversing the end orientation gives
\[
c_+=\frac4{|\Gamma|}+r-3,
\]
which excludes the reversed \(D,E\) cases.

In the simply connected rank-one setting:

* even \(D_r\) has noncyclic \(H_1=\mathbb Z_2\oplus\mathbb Z_2\);
* odd \(D_r\) has \(H_1=\mathbb Z_4\), with lattice discriminant \(\langle-r/4\rangle\);
* matching \(\langle-1/4\rangle\) requires \(r\equiv1\bmod4\);
* charge then leaves \(D_5,D_9\);
* \(E_6,E_7\) fail the square-order condition;
* \(E_8\) permits \(m=1\), with
  \[
  (c_+,c_-)=(-7,-29/30).
  \]

The \((-1)\)-trace of the left-handed trefoil has the Poincaré-sphere boundary with the orientation of the negative \(E_8\) plumbing, so that realization is correct. It supplies topology, not the required ALE metric.

Finally, cyclic groups and pure binary ADE groups do not exhaust finite free \(SO(4)\) actions on \(S^3\). Consequently neither the rank-one nor rational-ball table exhausts spherical-space-form ends.

## 5. Proposition 55.4: T-ball formulas hold for all parameters

For
\[
\frac1{n^2}(1,na-1),\qquad 1\le a<n,\quad (n,a)=1,
\]
the Milnor fibre satisfies
\[
\chi(B_{n,a})=1,\qquad \tau(B_{n,a})=0,\qquad
\pi_1(B_{n,a})=\mathbb Z_n.
\]
The charge statement is not limited to \(n\le10\). It follows from the exact identity
\[
s(na-1,n^2)=\frac16\left(1-\frac1{n^2}\right).
\]
For example, the Hirzebruch–Jung formula
\[
12s(q,p)=\sum_i(b_i-3)+\frac{q+q'}p
\]
proves it: a Wahl chain has \(\sum_i(b_i-3)=1\), and
\[
q=na-1,\qquad q'=n(n-a)-1,\qquad q+q'=n^2-2.
\]
Hence
\[
\eta=-\frac23\left(1-\frac1{n^2}\right),
\]
and
\[
\boxed{(c_+,c_-)=\left(0,-4\left(1-\frac1{n^2}\right)\right)}
\]
in the complex orientation. Reversal exchanges these values.

These fibres carry Ricci-flat Kähler ALE metrics as suitable free \(\mathbb Z_n\)-quotients of \(A_{n-1}\) spaces. Thus \(P=0\), \(W^+=0\), and
\[
w_{\rm reversed}=4(1-1/n^2).
\]

The converse assertion
> “zero-charge rational balls are precisely T-singularity Milnor fibres”

is not proved by the supplied material. A boundary charge does not determine a filling’s diffeomorphism type or establish existence of a Ricci-flat metric. The script’s `rational_ball_lens` entries are hypothetical charge calculations for \(\chi=1,\tau=0\), not a classification of actual rational-ball fillings.

Also, “T-singularity” should here mean the \(d=1\), or Wahl, subclass. General T-singularity Milnor fibres need not be rational balls.

## 6. Theorem 55.5: the lattice theorem is correct

### Fundamental group, degree and kernel

For \(W=V^\circ\), the map
\[
\pi_1(L)=\mathbb Z_{n^2}\longrightarrow\pi_1(B_{n,a})=\mathbb Z_n
\]
is onto. Since the boundary group dies in \(\Gamma\),
\[
\pi_1(M)=\pi_1(W)/\langle\!\langle\pi_1(L)\rangle\!\rangle
=\pi_1(Y).
\]
The compatible classifying maps, constant on \(B\) and on the simply connected plumbing \(C\), have the same degree, namely one.

On free integral homology, degree one gives
\[
H_2(Y)/\mathrm{tors}=c^!H_2(X)/\mathrm{tors}\ \perp\ K.
\]
Thus \(K\) is unimodular. Rational blow-up gives
\[
\operatorname{rank}K=r+1,\qquad \operatorname{sign}K=-(r+1).
\]
All chain spheres lie in \(K\), because \(X\) is aspherical. For \(r+1\le7\), \(K\cong-I_{r+1}\).

### Primitivity

Let
\[
G_c=\operatorname{coker}(K\to C^*),\qquad |G_c|=o.
\]
The relative sequence identifies \(G_c\) with the image of \(H_1(L)\) in \(H_1(W)\), so \(o\mid n^2\), and
\[
0\to G_c\to H_1(W)\to H_1(Y)\to0.
\]
Mayer–Vietoris for \(W\cup B\) gives
\[
\frac{|\operatorname{Tor}H_1(M)|}
{|\operatorname{Tor}H_1(Y)|}=\gcd(o,n).
\]
One way to see the factor is to eliminate the \(\mathbb Z_n\) summand: the remaining quotient of the cyclic group \(G_c\) is \(G_c/nG_c\), of order \(\gcd(o,n)\).

Since \(M,Y\) have the same fundamental group,
\[
\gcd(o,n)=1.
\]
Together with \(o\mid n^2\), this forces \(o=1\). Surjectivity \(K\to C^*\) is equivalent to primitivity of \(C\subset K\).

### Discriminant sign and parity law

For the negative chain matrix \(G\),
\[
(G^{-1})_{11}=-\frac{na-1}{n^2}.
\]
Therefore its **bilinear** discriminant form is
\[
\boxed{\operatorname{disc}(C)=
\left\langle\frac{1-na}{n^2}\right\rangle\quad\text{in }\mathbb Q/\mathbb Z.}
\]
The primitive rank-one complement is \(\langle-n^2\rangle\), whose discriminant form is \(\langle-1/n^2\rangle\). Unimodular gluing requires an anti-isometry, so
\[
\operatorname{disc}(C)\cong
-\operatorname{disc}\langle-n^2\rangle
=\langle+1/n^2\rangle.
\]
The sign in Step 55 is correct:
\[
\boxed{1-na\equiv u^2\pmod{n^2},\qquad (u,n)=1.}
\]
Conversely, the graph of such an anti-isometry produces an integral negative-definite unimodular overlattice with primitive \(C\). No even-lattice quadratic refinement is required.

The arithmetic equivalence is
\[
\boxed{1-na\text{ is a unit square mod }n^2
\iff n\text{ is odd or }8\mid n.}
\]
At odd primes dividing \(n\), Hensel lifting applies since \(1-na\equiv1\bmod p\). For the 2-primary part:

* \(v_2(n)=1\): obstruction \(1-na\equiv3\bmod4\);
* \(v_2(n)=2\): obstruction \(1-na\equiv5\bmod8\);
* \(v_2(n)\ge3\): \(1-na\equiv1\bmod8\), sufficient for an odd unit to be a square modulo higher powers of \(2\).

The note’s mod-\(8\) explanation for \(v_2(n)=1\) should be replaced by the mod-\(4\) argument.

This proves abstract lattice allowance, not geometric realization of the kernel lattice or the degeneration.

The supplied embedding search confirms the existence/nonexistence conclusions through \(n=7\), but is not wholly exhaustive: \(n=7,a=6\) reaches the 4000-result cap. Its explicit primitive embedding suffices for existence.

## 7. The \(n=3\), \([5,2]\) example

The primitive lattice embedding is correct:
\[
v_1=2E_1+E_2,\qquad v_2=-E_2-E_3,
\]
\[
(v_i\cdot v_j)=
\begin{pmatrix}-5&1\\1&-2\end{pmatrix}.
\]
The maximal minors have gcd \(1\), and the orthogonal complement is generated by
\[
E_1-2E_2+2E_3,\qquad w^2=-9.
\]
With \(v_2=E_2+E_3\), the mutual intersection is \(-1\); reversing that sphere’s orientation gives the plumbing convention \(+1\).

The conic–line connected sum and the line–line tube give smooth embedded spheres meeting once. For this explicit construction, the complement’s simple connectivity can also be checked using auxiliary lines:

* a line in the third summand meets only the second chain sphere, once, so its punctured disk kills that meridian;
* an additional line in the second summand meets each chain sphere once, so its punctured annulus relates their meridians;
* hence both meridians are trivial. They normally generate the complement group because the ambient connected sum is simply connected.

The tubes and connected-sum balls can be chosen away from these auxiliary lines. Thus this model has simply connected complement; the surjection \(\pi_1(L)\to\pi_1(B_{3,1})\) then gives simply connected rational blowdown \(Z\).

Consequently \(Z\) has rank-one negative intersection form and is **homeomorphic** to \(\overline{\mathbb{CP}}^2\). A diffeomorphism \(Z\cong\overline{\mathbb{CP}}^2\), or the sufficient weaker identification \(X\#Z\cong M\), still needs a smooth-topological argument. No critical orbifold metric follows from the plumbing construction.

## 8. Proposition 55.6: correct counting, invalid original setup, repair available

The original implications
\[
b^+\ge3,\ SW\ne0\ \Longrightarrow\ \text{general type}
\]
and
\[
\text{general type}\ \Longrightarrow\
\text{exactly }r+1\text{ exceptional classes spanning }K
\]
are not justified. The first is false in general, and the second does not follow from degree one or the kernel calculation.

The conclusion can be repaired without SW:

1. Since \(\pi_1(Y)=\pi_1(X)\), \(b_1(Y)=b_1(X)\) is even. A compact complex surface with even \(b_1\) is Kähler.
2. The degree-one map \(Y\to X\) has a harmonic representative.
3. The target is complex hyperbolic, hence strongly negatively curved. Nonzero degree forces real rank \(4\) somewhere; Siu rigidity makes the map holomorphic or antiholomorphic.
4. After conjugating the target if necessary, it is a degree-one holomorphic map, hence a birational morphism.
5. Therefore \(Y\) is \(X\) blown up exactly \(r+1\) times. Since \(X\) contains no rational curves, every sphere of the holomorphic T-chain is exceptional.

Now the counting argument is valid. If there are \(r+1\) blow-ups, every exceptional component starts at square \(-1\), and each later centre lies on at most two existing exceptional components. Hence
\[
\sum_{j=1}^{r+1}(-D_j^2)\le(r+1)+2r=3r+1.
\]
A Wahl chain of length \(r\) has
\[
\sum_{i=1}^rb_i=3r+1,
\]
while the remaining exceptional component contributes at least \(1\). This contradicts the upper bound.

Thus the complex-orientation zero-charge T-channel cannot have a compact complex-orbifold bulk with that complex quotient singularity. This proof does not establish non-Kählerness for rank-one channels, reversed T-balls, or arbitrary non-T balls.

## 9. Lemma 55.8 and collapse

Lemma 55.8 is correct. A map to \(X=K(\Gamma,1)\) whose fundamental-group image is cyclic factors, up to homotopy, through \(S^1\). Its \(H_2\)-map vanishes, so the image in \(H_2(M)\) lies in the exceptional lattice.

But **cyclic fundamental-group image alone does not exclude \(E\)**. It only puts the image in \(\mathbb ZE\). A punctured \(\overline{\mathbb{CP}}^2\), for example, has trivial fundamental group and carries an odd-square class.

For a region with a free circle action, the separate spin argument is correct:
\[
TC\cong\pi^*TB\oplus\underline{\mathbb R},
\]
and the oriented three-dimensional quotient is parallelizable. Thus classes carried by that region have even square. This is not automatically an argument for finite-isotropy actions or general positive-rank \(F\)-structures.

### The collapse ledger is wrong as used

Purely topologically, if \(\chi(C)=0\) and \(\tau(C)=-1\), then
\[
T_+^{\rm top}(\Omega)=T_+(M)-3\tau(C)=A+2.
\]
However, \(\Omega\) has boundary. Its curvature integral is not governed by this number without APS and Gauss–Bonnet transgression terms.

If \(C\) has bounded full curvature and volume tending to zero, then
\[
P(C),\quad\int_C|W^+|^2,\quad\int_Cs^2\longrightarrow0.
\]
The exact closed-manifold identity therefore gives, in the absence of other contributions,
\[
\boxed{\frac{P(g_i)}{8\pi^2}
=C_+(\Omega_i)-(A-1)+o(1).}
\]
The threshold remains \(C_+(\Omega_i)<A+o(1)\). Boundary terms compensate the topological signature carried by \(C\).

Accordingly, \(\tau(C)=-1\) does **not** make the ledger favorable to absorption. Read literally, the asserted floor \(C_+(\Omega)\ge A+2\) would instead exclude a sub-\(8\pi^2\) configuration. What remains possible is that a bounded-curvature collapsed region carrying \(E\) contributes vanishing curvature energy, with its topology balanced by interface terms. Whether such a region exists under the relevant collapse hypotheses remains a topological and geometric question, not a consequence of the displayed signature calculation.

## 10. Correct scope of Theorem 55.7

Conditional on Lemma 55.1’s SW and compactification inputs, the defensible coarse alternatives are:

1. no nontrivial-group cone points;
2. one nontrivial-group attachment region has \(b_2=1\), and all other such regions are rational homology balls;
3. nontrivial-group cone points exist, and all their attachment regions are rational homology balls.

These are disjoint when stated this way. Case 2 may include additional rational-ball points and trivial-group concentration points; coexistence does not itself invalidate this coarse trichotomy.

The **detailed** theorem is not established because:

* the rank-one list assumes simple connectivity and omits general spherical-space-form groups;
* the rational-ball charge table neither classifies actual fillings nor covers all groups or parameters;
* “zero charge iff T-type” is unproved;
* universal non-Kählerness in cases (B), (C) exceeds Proposition 55.6;
* the additive charge budget must be imposed.

The total-energy lower bound is nevertheless correct:
\[
p_*(M)\ge8\pi^2\left[C_+(V)+\sum_jw(N_j)-(A-1)\right].
\]

### Zero-energy bubbles and reassembly

The claimed equality for \(P=0\) bubbles is valid once ordinary smooth-orbifold regularity and the stated ALE decay permit vanishing-error gluing. This can be justified directly rather than treated as unexplained energy equality.

At physical gluing radius \(\rho\), with bubble scale \(\varepsilon\), the orbifold metric differs from its flat cone by \(O(\rho^2)\), while the scaled ALE metric differs by \(O((\varepsilon/\rho)^{\tau_0})\), with derivative control. A cutoff interpolation has annular curvature-energy error bounded by
\[
O\!\left(\rho^4+(\varepsilon/\rho)^{2\tau_0}\right).
\]
Choosing \(\rho=\varepsilon^a\), \(0<a<1\), makes this vanish. Thus any smooth orbifold metric on the fixed bulk can be recovered on the specified smoothing \(M\), with no added \(P\)-energy when the bubbles are Ricci-flat. Combined with lower semicontinuity,
\[
\boxed{p_*(M)=\alpha_{\rm orb}(V)=P(V,g_0).}
\]
If smooth orbifold regularity of \(g_0\) has not been established, that is the precise remaining analytic prerequisite.

Finally, the exact threshold problem is
\[
\boxed{C_+(V)+\sum_jw(N_j)\ge A.}
\]
The proposed bound involving only \(1-\max\{c_+,c_-,0\}\) is a sufficient charge-based exclusion, not an equivalent formulation: actual bubble energy can exceed its charge lower bound.

**Bottom line:** retain the charge/ledger machinery, the conditional exceptional-line reduction, the T-ball formulas, and Theorem 55.5. Restrict Proposition 55.3 explicitly; replace Proposition 55.6’s SW argument by the Kähler–Siu–blow-up proof; correct the collapse discussion; and replace Theorem 55.7’s exhaustive classification by the coarse homological alternatives plus the additive energy threshold.