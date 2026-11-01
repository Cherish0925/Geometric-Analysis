# Step 93 — paired-A1 orbifold transfer, exact variational law, and mixed filler screen

Session S1003A02, Agent4, Express. This note independently reads and consolidates A01 Step 74:
`Sessions/S1003A01/workspace/notes/step74_orbifold_transfer_theorem.md`, its script/data, peer messages
#870–#872, the primary LeBrun sources, and the two-task Step-93 TTCS verification
(`trace/ttcs/results/step93_ttcs01_verifier{1,2}_integration.md`). The statements below supersede only the
paired-\(A_1\) interpretation of Theorem 87.O; the exact Weyl-deficit formula itself remains valid.

Throughout, \(X\) is a compact complex-hyperbolic surface in its complex orientation,
\(A=c_1^2(X)\),
\[
V_m=X\#m(S^4/\mathbb Z_2),\qquad k=2m>0,
\]
and orbifold connected sums are at regular points. We use
\(P=\int|\operatorname{Ric}^\circ|^2\), \(S=\int s^2\),
\(I_\pm=\int|W^\pm|^2\), \(W=I_++I_-\), \(R=P+S/4\), and
\(\mathscr D=(4P+L_s)/R\).

## 1. Smooth topology and curvature transfer

### The resolved football

The orientation-matched resolution of the two \(A_1\) points of \(S^4/\mathbb Z_2\) by complex-oriented
Eguchi–Hanson spaces is diffeomorphic to
\(\overline{\mathbb{CP}}^{\,2}\#\overline{\mathbb{CP}}^{\,2}\).
A01 gives a \(T^2\)-equivariant proof: write
\(S^4=\{(t,w)\in\mathbb R\times\mathbb C^2:t^2+|w|^2=1\}\), quotient by \(w\mapsto-w\),
and resolve each pole by toric \(\mathcal O(-2)\). The resolution is simply connected, has orbit disk with four
edges, and has unimodular form \(-I_2\); Orlik–Raymond identifies it with the double reversed projective plane.
Thus resolving all \(2m\) singular points of \(V_m\) gives
\(M_k=X\#k\overline{\mathbb{CP}}^{\,2}\). This agrees with Lemma 52.6 and its lattice formulas
\(E_{2j-1},E_{2j}=\tfrac12(e_j\pm f_j)\).

### Scalar transfer needs no extra SW assumption

LeBrun's Yamabe theorem gives
\[
\mathcal Y(M_k)=-4\pi\sqrt{2A}
\]
for every general-type blow-up, including \(b^+=1\). Hence every smooth metric \(\widetilde g\) on \(M_k\) satisfies
\[
\int_{M_k}(s^-_{\widetilde g})^2\ge32\pi^2A.
\]
Resolve an arbitrary smooth orbifold metric \(g\) on \(V_m\) by scaled EH spaces. Lemma 86.S, with
\(\tau=4\), \(\rho=\varepsilon^{2/3}\), gives convergence of the negative scalar square as well as \(S\) and \(P\):
\[
\int(s^-_{g_\varepsilon})^2\longrightarrow\int_{V_m}(s^-_g)^2,
\qquad S(g_\varepsilon)\to S(g),\qquad P(g_\varepsilon)\to P(g).
\]
Therefore every orbifold metric on \(V_m\) obeys the unconditional bound
\[
\boxed{\int_{V_m}(s^-_g)^2\ge32\pi^2A,\qquad S(g)\ge32\pi^2A.}
\]
The hypothesis \(R>0\) in the full-defect continuity statement is irrelevant here; it is needed only when taking a
quotient defining \(\mathscr D\).

The smooth mixed inequality also has all-\(b^+\) scope. LeBrun 2001, Theorem 2.3, together with the metric-wise
class selected in Proposition 3.2, gives
\[
\int_{M_k}(s-\sqrt6|W^+|)^2\ge72\pi^2A
\]
for every smooth metric on \(M_k\). Proposition 3.2 explicitly notes polarization independence when the source square
is positive, even for \(b^+=1\). Thus fake projective planes require no additional chamber hypothesis in the statements
below.

## 2. Exact paired-\(A_1\) orbifold law

The orbifold characteristic numbers are
\[
\chi_{\rm orb}(V_m)=\frac A3-m,\qquad \tau_{\rm orb}(V_m)=\frac A9.
\]
The \(A_1\) link has zero signature \(\eta\)-term. Thus
\[
I_+-I_-=\frac{4\pi^2A}{3},\qquad W\ge\frac{4\pi^2A}{3}.
\]
Put
\[
\sigma=S-32\pi^2A\ge0,\qquad
w=W-\frac{4\pi^2A}{3}=2I_-\ge0.
\]
Orbifold Gauss–Bonnet gives the exact ledger
\[
\boxed{
P=8\pi^2k+\frac{\sigma}{12}+2w,
\qquad
R=8\pi^2(A+k)+\frac{\sigma}{3}+2w.}
\]
Consequently \(4P/R\) is the weighted mean of
\(4k/(A+k),1,4\) with weights
\(8\pi^2(A+k),\sigma/3,2w\), and
\[
P\ge8\pi^2k,
\qquad
\mathscr D\ge\min\left\{1,\frac{4k}{A+k}\right\}.
\]
In particular, \(V_m\) carries no Einstein orbifold metric for any \(m\ge1\).
This replaces the weaker consequence of 87.O that an Einstein metric would merely require \(k<A/3\).

### Recovery by the Green football cap

On \(\mathbb R^4\setminus\{0\}\),
\[
h=(1+r^{-2})^2\delta
\]
is scalar-flat and conformally flat, with
\[
P(h)=32\pi^2,
\qquad
\int_{r>R}|\operatorname{Ric}^\circ_h|^2
=\frac{\pi^2(96R^2+32)}{(1+R^2)^3}
=\frac{96\pi^2}{R^4}+O(R^{-6}).
\]
The involution
\[
\iota(x)=\operatorname{diag}(-1,-1,-1,1)x/|x|^2
\]
is an orientation-preserving isometry, exchanges the two ends, has fixed points \(\pm e_4\), and has derivative
\(-I\) there. Its quotient is the football minus a regular point, with two \(A_1\) points, one ordinary AE end, and
\(P=16\pi^2\). Insert \(m\) such caps into the CH metric using \(\rho=\varepsilon^{1/2}\). Transition curvature is
\(O(1)\) on volume \(O(\varepsilon^2)\), and cap-tail energy is \(O(\varepsilon^2)\). Hence
\[
P\to8\pi^2k,\quad S\to32\pi^2A,\quad W\to\frac{4\pi^2A}{3},\quad L_s\to0,
\quad \mathscr D\to\frac{4k}{A+k}.
\]
The ordinary long round-cylinder construction at a regular point gives \(\mathscr D\to1\). Therefore
\[
\boxed{
P_{*,\rm orb}(V_m)=8\pi^2k,
\qquad
\alpha_{\rm orb}(V_m)=\min\left\{1,\frac{4k}{A+k}\right\}.}
\]
The old deficit theorem remains:
\[
d_{*,\rm orb}(V_m)=4\pi^2\left(\frac A3-k\right)
=4\pi^2\left(\frac A3-2m\right).
\]

## 3. Attainment

### The \(P\)-infimum is never attained

Suppose \(P=8\pi^2k\). The ledger forces \(S=32\pi^2A\) and \(W^-=0\). Since a global minimizer of \(P\) is
stationary, and
\[
P=\frac1{12}\int s^2+2\int|W|^2-16\pi^2\chi_{\rm orb},
\qquad
\int|W|^2=12\pi^2\tau_{\rm orb}+2\int|W^-|^2,
\]
the first variation of the Weyl term vanishes at \(W^-=0\); hence the metric is critical for \(\int s^2\).
The Euler equation on the regular locus is
\[
\nabla^2s-(\Delta s)g-s\operatorname{Ric}+\frac14s^2g=0.
\]
Its trace gives \(\Delta s=0\), and compact orbifold integration makes \(s\) constant. Since
\(S=32\pi^2A>0\), \(s\ne0\), so the trace-free part gives \(\operatorname{Ric}^\circ=0\), contradicting
\(P=8\pi^2k>0\). Thus
\[
\boxed{P(g)>8\pi^2k\text{ for every individual orbifold metric on }V_m.}
\]

It follows that \(\alpha_{\rm orb}\) is not attained when \(k<A/3\), since equality in the weighted-mean lower bound
would force the impossible \(P\)-minimum. It is not attained when \(k>A/3\), because every metric has
\(4P/R>1\) strictly. At the wall \(k=A/3\),
\[
\mathscr D-1=\frac{12I_-+L_s}{R};
\]
attainment is equivalent to an orbifold metric with \(W^-=0\) and constant \(s<0\). Such a metric, if it exists, has
\(S>32\pi^2A\) and \(P>8\pi^2k\). This single wall-existence question remains open.

The former equalities \(W^-=0\), \(s\le0\), \(|W^+|^2=s^2/24\), \(P=8\pi^2k\) describe only a hypothetical
\(P\)-attainer, now excluded. They do not invoke Derdziński: norm equality does not force a two-eigenvalue spectrum,
and neither \(\delta W^+=0\) nor a Codazzi Ricci tensor has been proved. Numerical transfer of LeBrun's inequality also
does not itself transfer its monopole equality structure to the orbifold.

## 4. Mixed transfer and general Ricci-flat filler constraints

Let a compact orbifold \(V\) resolve to \(M_k\) by orientation-matched scalar-flat ALE fillers \(N_j\), and put
\(B_+=\sum_j\int_{N_j}|W^+|^2\). The smooth mixed inequality passes to the limit as
\[
\boxed{
\int_V(s-\sqrt6|W^+|)^2+6B_+\ge72\pi^2A.}
\]
For Ricci-flat fillers, \(B_+=-2\pi^2C_+\), so the right-hand form is
\[
\int_V(s-\sqrt6|W^+|)^2\ge72\pi^2A+12\pi^2C_+.
\]
Chirality matters: a Ricci-flat Kähler filler in its complex orientation has
\[
c_+=0,
\qquad c_-=-4\left(\chi(N)-|\Gamma|^{-1}\right),
\]
whereas reversing orientation interchanges the two charges.

If the compact bulk is Einstein, write \(x=S/(96\pi^2)\) and
\[
T_+=A-k+C_+,
\qquad
T_-=\frac A3+5k+C_-.
\]
Then a necessary condition is
\[
\frac A3\le x\le\min(T_+,T_-),
\qquad
\boxed{\left[\sqrt{8x}+\sqrt{T_+-x}\right]^2\ge6A+C_+.}
\]
The left side is concave, with maximum \(9T_+\) at \(x=8T_+/9\). With
\(e=C_+-k\), \(d=C_-+5k\), the endpoint expansion is
\[
9C_-+2C_++42k-rac{3(e-3d)^2}{4A}+O(A^{-2})\ge0.
\]
Moreover, the concavity tangent bound gives the exact finite-\(A\) necessary inequality
\[
\boxed{9C_-+2C_++42k\ge0.}
\]

For complex-oriented Ricci-flat Kähler fillers, \(C_+=0\), and
\[
x_{\min}=\frac A{27}\left(4-\sqrt{1-3k/A}\right)^2.
\]
An Einstein bulk requires
\[
\boxed{
\sum_j\left(\chi(N_j)-|\Gamma_j|^{-1}\right)
\le\frac14\left(\frac A3+5k-x_{\min}\right)
=\frac{7k}{6}-\frac{k^2}{12A}-\frac{k^3}{8A^2}+O(k^4/A^3).}
\]
If the fillers carry all \(k\) exceptional ranks, this implies
\(\sum_j(1-|\Gamma_j|^{-1})<k/6\). Passing this numerical test is only necessary: actual Ricci-flat ALE existence,
orientation, embedding, resolution topology, and existence of the negative Einstein compact bulk remain separate.
The A01 screen must be read at this scope; sampled first-passing values are not exact thresholds.

The mixed transfer rules out the former scalar-only first survivor \(L(9,4)\), the paired-\(A_1\) pattern, \(A_1\)–\(A_5\),
\(D_4,D_5\) when a single Kronheimer filler carries exactly its rank, and most charge-compatible cyclic rows. Surviving
charge rows are not constructions. In particular, rows with both charges negative would require non-Kähler Ricci-flat
ALE metrics, none supplied here.

## 5. Consequences for the global programme

1. Ordinary paired-\(A_1\) absorption over a ball quotient is now closed as a zero-gap/Einstein-bulk route for every
   \(k=2m>0\), including \(0<k<A/3\). It does not merely fail past \(1/3\).
2. Since smooth Burns response gives \(P_*(M_k)<8\pi^2k\), a smooth \(P\)-minimizing sequence cannot converge smoothly on
   the regular locus to a metric on this fixed \(V_m\): lower semicontinuity alone would give
   \(\liminf P\ge8\pi^2k>P_*(M_k)\). No energy identity is needed.
3. The exact orbifold law does not bound arbitrary smooth metrics and does not exclude different orbifold topologies,
   Wahl smoothings, mixed host–exceptional lattices, or collapse.
4. The centre \(0<k<A/3\) therefore retains the same three global alternatives, but its second alternative is narrowed:
   any absorbing negative Einstein orbifold must have singular/topological data different from ordinary
   \(X\#m(S^4/\mathbb Z_2)\).
