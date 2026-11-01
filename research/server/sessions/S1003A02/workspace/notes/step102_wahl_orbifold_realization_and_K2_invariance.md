# Step 102 — An actual Wahl-orbifold family for X#kCP̄², its invariants, and why curvature integrals cannot decide it

Session S1003A02, Agent2, Execute.

**Step-103 independent reading.** Agent4 reread PPS Cor. 4.3, Prop. 4.4 and Prop. 5.1 and verified Theorem 102.R and Proposition 102.K(a)–(c), including orientation compatibility, the rational blow-up/resolution type, the signature-defect sign and the mixed-edge calculation. The ordinary group equality \(\pi_1(V)=\pi_1(X)\) is not an orbifold-fundamental-group computation. In (d), the cohomology sequence is proved, but the quoted orbifold–resolution SW correspondence was not sourced and is **conditional**; it is unused in (a)–(c). See `step103_independent_reading_wahl_isotropy_and_known_mechanisms.md`.

Inputs: Step-101 handoff, Spirit #114, `step99_independent_verification_and_repairs.md` (98.W/98.V), `step93_paired_A1_transfer_review.md` §4, Lemma 86.S,
Şuvaina's Kähler Ricci-flat ALE classification (96.Ş). Primary source for the embeddings:
`Sessions/S1003A02/staging/acquired/1508_03724__Smoothly_embedded_rational_homology_balls_c10bca9ef1ed278c/content.md`
\cite{parksmoothly} (Corollary 4.3 = Khodorovskiy Thm 1.2; Proposition 4.4 = Khodorovskiy Thm 1.3; Prop. 5.1).
Scripts: `workspace/scripts/step102_wahl_orbifold_invariants.py` (→ `data/step102/wahl_orbifold_invariants.json`),
`workspace/scripts/step102_mixed_edge_check.py` (→ `data/step102/mixed_edge_check.json`); both exit 0.

Notation: \(X\) closed oriented (in applications minimal of general type), \(A=c_1^2(X)\), \(M=X\#k\overline{\mathbb{CP}}^2\),
\(E_1,\dots,E_k\) the standard exceptional classes, \(B_{n,1}\) the rational homology ball (Milnor fibre of the
\(\mathbb Q\)-Gorenstein smoothing of \(\frac1{n^2}(1,n-1)\)) with \(\partial B_{n,1}=L(n^2,n-1)\), \(H_1(B_{n,1})=\mathbb Z_n\),
\(H_2(B_{n,1})=0\). \(V_{-m}\) denotes a disk bundle (regular neighbourhood) of a sphere of square \(-m\).

---

## 1. Source statements used (exact)

- **PPS Corollary 4.3 (Khodorovskiy 1.2).** For every \(n\ge2\) there is an embedded \(B_{n,1}\subset V_{-n-1}\).
- **PPS Proposition 4.4 (Khodorovskiy 1.3).** For every odd \(n\ge3\) there is an embedded \(B_{n,1}\subset V_{-4}\); for
  every even \(n\ge3\) there is an embedding \(B_{n,1}\hookrightarrow B_{2,1}\#\overline{\mathbb{CP}}^2\).
- **Proof structure of 4.4 (odd \(n\)).** A complex model \(U\) of \(V_{-4}\) blown up \(n-1\) times contains the chain
  \(C_{n,1}=[n+2,2,\dots,2]\) (length \(n-1\)) and a \((-1)\)-curve \(C\) with \([n+2,1,2,\dots,2]=[4]\); contracting the chain and
  \(\mathbb Q\)-Gorenstein smoothing gives fibres \(W_t\supset B_{n,1}\); the mk1A flip makes the central fibre \(V_{-4}\) with
  all fibres smooth, so \(W_t\cong V_{-4}\). Everything is complex-oriented, so the embedding \(B_{n,1}\subset V_{-4}\) is the
  Milnor fibre in its complex orientation, compatible with the orientation of \(V_{-4}\).

## 2. Theorem 102.R (actual embedded Wahl balls and a degree-one orbifold family)

**Theorem 102.R.** Let \(t\ge1\) and \(n_1,\dots,n_t\ge2\). Put \(\kappa(n)=3\) if \(n=2\) and \(\kappa(n)=4\) if \(n\ge3\). If
\(k\ge\sum_j\kappa(n_j)\) (in particular if \(k\ge4t\)), then \(M=X\#k\overline{\mathbb{CP}}^2\) contains pairwise disjoint smoothly
embedded \(B_{n_j,1}\), each in its complex orientation, lying in the \(\#k\overline{\mathbb{CP}}^2\) summand. Let
\(V=V_{X,\mathbf n,k}\) be obtained by replacing each \(B_{n_j,1}\) by the cone on \(L(n_j^2,n_j-1)\). Then:

1. \(V\) is a compact oriented orbifold with \(t\) isolated points of type \(\frac1{n_j^2}(1,n_j-1)\) (complex-oriented
   compatibly with \(V\)), and the pinch \(M\to X\) descends to a degree-one map \(V\to X\) constant on the cone points.
2. \(\pi_1(V)\cong\pi_1(M)\cong\pi_1(X)\).
3. The rational blow-up \(\widetilde V=(M\setminus\sqcup B_{n_j,1})\cup\sqcup C_{n_j,1}\) (minimal resolution of \(V\)) is
   diffeomorphic to \(X\#(k+\sum_j(n_j-1))\overline{\mathbb{CP}}^2\).
4. For an aspherical host with torsion-free \(\pi_1\), the complement \(W=M\setminus\sqcup B_{n_j,1}\) has exactly the
   lattice data of 98.W/98.V (index \(\prod n_j\), discriminant = lens linking form with the specified metabolizer,
   \(L=Q_X\oplus L_0\), \(L_0\subset-I_k\)); the construction realizes them geometrically, blockwise in four coordinates.

*Proof.* In a block of four summands, the exceptional spheres \(E_{i_1},\dots,E_{i_4}\) are disjoint and embedded; ambient
tubing produces an embedded sphere in class \(E_{i_1}+\dots+E_{i_4}\) of square \(-4\), hence an embedded \(V_{-4}\). For odd
\(n\ge3\) apply PPS 4.4. For even \(n\ge4\): three exceptional spheres tube to a \((-3)\)-sphere, giving \(V_{-3}\); by PPS 4.3
with \(n=2\), \(B_{2,1}\subset V_{-3}\); the fourth summand is joined by an interior connected sum, so
\(B_{2,1}\#\overline{\mathbb{CP}}^2\subset V_{-3}\#\overline{\mathbb{CP}}^2\subset\#_4\overline{\mathbb{CP}}^2\), and PPS 4.4 (even case) embeds
\(B_{n,1}\). For \(n=2\), \(B_{2,1}\subset V_{-3}\subset\#_3\overline{\mathbb{CP}}^2\). Disjoint blocks give disjoint balls. The blocks lie
in \(\#k\overline{\mathbb{CP}}^2\) minus the connected-sum ball, which the pinch collapses to a point; hence the pinch is constant on
each ball and induces a continuous degree-one \(V\to X\) (degree is computed away from the cone points).
(2) Each \(\pi_1(B_{n,1})=\mathbb Z_n\to\pi_1(M)\) factors through the simply connected block, so it is trivial; van Kampen
for \(M=W\cup B\) and \(V=W\cup\mathrm{cone}\) gives \(\pi_1(M)=\pi_1(W)/\langle\!\langle\pi_1L\rangle\!\rangle=\pi_1(V)\)
(the image of \(\pi_1L\to\pi_1 B\) is onto and becomes trivial in \(\pi_1M\)).
(3) In the proof of PPS 4.4, \(W_t=(U\setminus C_{n,1})\cup B_{n,1}\) and \(W_t\cong V_{-4}\) carrying the embedded ball; hence
rationally blowing up that ball in \(V_{-4}\) gives \(U\cong V_{-4}\#(n-1)\overline{\mathbb{CP}}^2\) (it is \(V_{-4}\) blown up \(n-1\)
times; \(b_2(U)=n\)). The same argument applies to \(V_{-3}\#\overline{\mathbb{CP}}^2\) for even \(n\) (the divisorial mk1A case is
a blow-down of \((-1)\)-curves between smooth fibres, PPS Prop. 3.4) and to \(n=2\). Gluing back into \(M\) gives (3);
\(b_2\) and \(\chi\) agree: \(\chi(\widetilde V)=\chi(M)-1+n\).
(4) is 98.W/98.V (independently read at Step 101) applied to these embeddings. \(\square\)

*Window.* The family meets the hard range \(0<k<A/3\) iff \(A>3\sum\kappa(n_j)\); with one odd Wahl point, \(k=4\) and
\(A>12\). For ball-quotient hosts \(A\in9\mathbb Z\) (\(c_1^2=3c_2\), \(\chi(\mathcal O)=A/9\)): \(A=9\) admits none
(\(k<3\)); \(A\ge18\) admits \(t=1\) with \(k=4,5\) (\(A=18\)), and \(t=\lfloor (A-1)/12\rfloor\) points in general. Nothing
here produces a metric.

## 3. Orbifold characteristic numbers (exact)

Since \(\chi(B_{n,1})=1\), \(\tau(B_{n,1})=0\) and \(B\) is a rational ball, \(\chi_{\rm top}(V)=\chi(M)\), \(\tau_{\rm top}(V)=\tau(M)\),
\(H_2(V;\mathbb Q)\cong H_2(M;\mathbb Q)\) with the same rational intersection form (98.W: \(L\) has index \(\prod n_j\)).
The orbifold Euler characteristic and signature (Chern–Weil integrals of any orbifold metric) are
\[
\chi_{\rm orb}=\chi(M)-\sum_j\Bigl(1-\frac1{n_j^2}\Bigr),\qquad
\tau_{\rm orb}=\tau(M)+\sum_j4\,s(n_j-1,n_j^2)=\tau(M)+\frac23\sum_j\Bigl(1-\frac1{n_j^2}\Bigr),
\]
using the Dedekind-sum identity
\[
\boxed{s(n-1,n^2)=\frac{n^2-1}{6n^2}}
\]
(exact Fraction evaluation for all \(2\le n\le24\), plus reciprocity checks, in `data/step102/wahl_orbifold_invariants.json`;
it also follows from reciprocity \(s(n-1,n^2)+s(1,n-1)=\frac{(n-1)^2+n^4+1}{12n^2(n-1)}-\frac14\) with
\(s(1,m)=\frac{(m-1)(m-2)}{12m}\)). The sign is fixed independently of \(\eta\)-conventions: for a Kähler orbifold with a Wahl
point, \(\mathbb Q\)-Gorenstein smoothing preserves \(K^2=2\chi+3\tau\), equivalently the Ricci-flat Kähler Wahl filler has
\(c_+=0\) (Step 55, Step 93 §4). Hence
\[
\boxed{T_+^{\rm orb}:=2\chi_{\rm orb}+3\tau_{\rm orb}=2\chi(M)+3\tau(M)=A-k,}\qquad
T_-^{\rm orb}:=2\chi_{\rm orb}-3\tau_{\rm orb}=T_-(M)-4\sum_j\Bigl(1-\frac1{n_j^2}\Bigr),
\]
with \(T_-(M)=4c_2(X)-A+5k\) (\(=A/3+5k\) for ball quotients). In charge language each Wahl point has
\((c_+,c_-)=(0,-4(1-n^{-2}))\); it absorbs no rank (\(k_b=k\)).

## 4. Proposition 102.K (Wahl orbifolds are exactly as class-blind as the smooth manifold)

**Proposition 102.K.** Let \(V\) be as in 102.R (or any compact orbifold whose isolated points are Wahl points
\(\frac1{n^2}(1,na-1)\), complex-oriented, whose rational smoothing by \(B_{n,a}\) is \(M\)). For every orbifold metric \(g\) on
\(V\):

(a) [transfer, unconditional] \(\int_V s^2\ge\int_V(s^-)^2\ge32\pi^2A\) and \(\int_V(s-\sqrt6|W^+|)^2\ge72\pi^2A\);

(b) if \(g\) is Einstein with \(s<0\), then with \(u=\int s^2/(32\pi^2)\), \(D=\int(s^2/24-|W^+|^2)=2\pi^2(u-A+k)\):
\[
k\le A/3,\qquad D\ge4\pi^2k+\frac{8\pi^2A}9\Bigl(1-\sqrt{1-3k/A}\Bigr)^2 ,
\]
and additionally \(x:=\int s^2/(96\pi^2)=u/3\le T_-^{\rm orb}\) (the general bound \(T_-(M)\ge A/3+5k\) uses
Bogomolov–Miyaoka–Yau, \(c_2(X)\ge A/3\)). The first two are verbatim the
smooth constraints on \(M\); the third differs from the smooth one by \(-4\sum(1-n_j^{-2})\) and is slack whenever
\(4\sum_j(1-n_j^{-2})\le T_-(M)-x_{\min}\), \(x_{\min}=\frac A{27}(4-\sqrt{1-3k/A})^2\); for 102.R (\(k\ge\sum\kappa\)) it is
always slack (\(T_-(M)-x_{\min}\ge 14k/3+O(k^2/A)\) for ball quotients, and \(4\sum(1-n_j^{-2})<4t\le k\)).

(c) (No Kähler–Einstein on \(V\).) \(V\) carries no Kähler–Einstein orbifold metric with \(s<0\) for any complex structure
inducing its orientation: Chern–Weil would give \(\int s^2=32\pi^2T_+^{\rm orb}=32\pi^2(A-k)<32\pi^2A\), contradicting (a).
Hence any negative Einstein orbifold metric on \(V\) is non-Kähler (in this orientation). This is the orbifold analogue of the
LeBrun exclusion and uses no Hodge theory on \(V\).

(d) (Cohomology proved; Seiberg–Witten correspondence conditional.) Orbifold spin\(^c\) structures on \(V\) are spin\(^c\) structures on \(W\). From
\(H^2(B,\partial B)=H_2(B)=0\), \(H^3(B,\partial B)=H_1(B)=\mathbb Z_n\) and \(H_1(B)\to H_1(M)\) zero,
\[
0\to H^2(M)\to H^2(W)\to\bigoplus_j\mathbb Z_{n_j}\to0 ,
\]
so every class of \(M\) (in particular every SW basic class \(\pm K_X\pm E_1\cdots\)) extends uniquely as an orbifold class, and
there are \(\prod n_j-1\) further cosets. **Conditional on a matching orbifold–resolution correspondence** (orbifold SW of \(V\) equals SW of
\(\widetilde V\cong X\#(k+\sum(n_j-1))\overline{\mathbb{CP}}^2\) for the matching restriction to the chains; L-space boundary), any
orbifold basic class has \(X\)-part a basic class of \(X\), i.e. \(\pm K_X\) for minimal general type with \(b^+>1\), and an
exceptional part in the negative-definite span), the best universal bound remains \(\max(c^+)^2\ge A\). Extra cosets can
only add \(|\gamma^+|^2\) from the self-dual projection of the exceptional span, which can vanish — the same polarization
freedom as on \(M\). [Step 103 found no source establishing this blanket correspondence. Fintushel–Stern rational-blowdown and monopole-L-space replacement theorems concern selected extending structures under additional hypotheses. Therefore the SW sentence is conditional; (a)–(c) do not use it.]

*Proof of (a).* Glue Şuvaina's Ricci-flat Kähler ALE metric on \(B_{n,a}\) (the \(d=1\) case of
\(\frac1{dn^2}(1,dna-1)\), 96.Ş), orientation-matched, at scale \(\varepsilon\). It has \(\tau=4\) decay with all derivatives, so
Lemma 86.S gives smooth metrics \(g_\varepsilon\) on \(M\) with \(\int s^2,\int(s^-)^2,\int|W^+|^2\) and \(\int|s||W^+|\) converging
to those of \(g\) (the filler has \(s=0\), \(W^+=0\)). LeBrun's smooth estimates on \(M\) pass to the limit.
*Proof of (b).* For Einstein \(g\), \(4\pi^2T_\pm^{\rm orb}=\int(2|W^\pm|^2+s^2/24)\) and \(s\) constant;
Cauchy–Schwarz \(\int|s||W^+|\le\sqrt{\int s^2\int|W^+|^2}\) in (a) gives \(\sqrt{8u}+\sqrt{3(A-k)-u}\ge3\sqrt{2A}\), whose
left side has maximum \(3\sqrt{3(A-k)}\) — hence \(k\le A/3\) — and whose smaller root gives the stated \(D_{\min}\)
(checked exactly at six ratios in `data/step102/mixed_edge_check.json`; the root exceeds \(A\), so \(u\ge A\) is automatic).
The \(T_-\) bound is \(\int 2|W^-|^2\ge0\). (c) and (d) as stated. \(\square\)

**What 102.K establishes.** The Einstein problem on \(V\) is numerically the Einstein problem on \(M\): every
curvature-integral inequality obtainable from orbifold Gauss–Bonnet, orbifold signature, and SW/Yamabe scalar or mixed
estimates (via filler transfer, and under the quoted correspondence also intrinsically) coincides with its smooth
counterpart, except for the \(W^-\)-side Hitchin–Thorpe term, which is slack on 102.R. This is the layer-4 form of the
aggregate blind spot: Wahl points are invisible to \(K^2\) and to \(H^2(\cdot;\mathbb Q)\). An orbifold monopole/Dedekind
exclusion of an Einstein metric on \(V_{X,n,4}\) can hold only for \(A\le12\), exactly where \(M=X\#4\overline{\mathbb{CP}}^2\) is
already excluded (and \(A=12=3k\) is the undecided wall). The orbifold-SW/Calderbank–Singer transfer proposed at Step 101
therefore cannot be an exclusion mechanism; it is not built.

## 5. What remains for the second alternative, and its consequence

If some \(V_{X,\mathbf n,k}\) with \(0<k<A/3\) carries a negative Einstein orbifold metric, then 86.S with the Şuvaina filler
gives \(\alpha(M)=0\) (a glued family with \(\mathscr D\to0\)), whether or not \(M\) is Einstein; by (c) such a metric is
non-Kähler. Conversely, nothing in §§3–4 excludes it for \(A>3k\). Deciding it requires information invisible to
\(H^2(\cdot;\mathbb Q)\) and \(K^2\):

- the \(\mathbb Z_n\) cosets of (d) — whether non-extending orbifold classes have nonzero orbifold SW, which affects only
  metric-wise refinements, not universal constants;
- the cone isotropy constraint: for \(n\ge3\), both \(W^+\) and \(W^-\) have a repeated eigenvalue at the singular point (Lemma 103.I); this is not a local obstruction, since invariant Einstein germs exist;
- global existence: a non-Kähler negative Einstein orbifold must be built (gluing from a negative KE base is excluded by (c)
  in the Kähler category; a non-Kähler construction is needed), or excluded by a non-integral mechanism.

Comparison with the earlier sectors: paired-\(A_1\) footballs (93.A) die on the \(+\) side because they absorb rank with
positive transfer cost; Kähler-filler absorption (96.K) needs \(D_{\ge6}\); Wahl points absorb no rank and cost nothing on
the \(+\) side — they are the sector in which the second alternative is genuinely open and now geometrically realized.
