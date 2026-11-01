# Step 55 — The k = 1 orbifold gate: two-orientation charges with η-invariants, the degree-one lattice constraint, and what survives

> **Step-56 binding corrections:** see `step56_orbifold_attainment_zero_energy_bound_Tpoint_interaction.md` §0. The changes are:
> - Prop. 55.3 is restricted to simply connected regions.
> - Prop. 55.6 is reproved via Kähler + Siu.
> - The §6 collapse ledger is withdrawn.
> - Theorem 55.7 is reduced to a coarse trichotomy plus the additive budget.
Session S1003A02, Agent2, Execute. Continues `step54_k1_ball_quotient_attainment_theorem.md` (§5 binding) and the
strategist's note #70. Scripts and data:

- `workspace/scripts/step55_orbifold_bubble_charges.py` → `workspace/data/step55_orbifold_bubble_charges.json`
  (exact Dedekind-sum η-invariants, charges, convention checks, numerical \(P\) of LeBrun's \(\mathcal O(-n)\) metrics);
- `workspace/scripts/step55_Tchain_embeddings.py` → `workspace/data/step55_Tchain_embeddings.json`
  (primitive embeddings of T-singularity chain lattices into \(-I_{r+1}\), all \(n\le7\)).

Setting throughout: \(X\) a compact ball quotient, \(\Gamma=\pi_1X\) (torsion-free, Gromov hyperbolic, one-ended, freely
indecomposable), \(M=X\#\overline{\mathbb{CP}}^2\), \(A=c_1^2(X)\), \(T_+=2\chi+3\tau\), \(T_+(M)=A-1\), and (U): \(p_*(M)<8\pi^2\).
All statements about minimizing configurations are inside Anderson's case (I) with the analytic ledger of step54 §5(b)
(\(\mathrm H_{\rm lsc}\), bubble criticality by compact replacement, and derivative-controlled ALE decay of the bubbles,
\(\mathrm H_{\rm dec}\), now with nontrivial group).

**Outcome in one paragraph.** The strategist's degree-one reduction is correct after one added Seiberg–Witten input,
and it does kill the Kronheimer hyperkähler channel at \(k=1\). It does *not* close the orbifold gate. Pricing every
remaining bubble with the exact two-orientation charge (η included) gives: every orbifold bubble carrying \(E\) or \(2E\)
through a **cyclic** end costs \(\ge8\pi^2\) and is excluded by (U) (LeBrun's \(\mathcal O(-4)\) costs exactly \(8\pi^2\));
but charge-free or negatively charged channels survive: classes \(mE\), \(m\ge3\), through lens ends (first:
\(L(9,4)\), \(c_+=-23/9\)); \(2E\) through binary-dihedral ends \(D_5,D_9\); \(E\) itself through the binary-icosahedral end
(\(c_+=-7\)); and rational-ball bubbles. Among rational balls, the zero-charge ones are exactly the T-singularity Milnor
fibres (Ricci-flat Kähler ALE, \(P=0\)), and the degree-one map forces a sharp lattice condition: the T-chain must embed
**primitively** in a negative-definite unimodular lattice of rank \(r+1\). This fails for the strategist's simplest case
\(B_2=\mathrm{EH}/\mathbb Z_2\) (\(n=2\)) and exactly for \(n\equiv2,4,6\pmod 8\); it holds otherwise (first:
\(1/9(1,2)\), chain \([5,2]\)). The zero-charge bulk is provably **non-Kähler**, and a conservation identity
shows each needs \(C_+(V)<A-w(N)\) with \(w(N)\) the bubble's self-dual Weyl charge. The gate is therefore reduced to one
analytic question — an unrestricted lower bound for \(P\) on non-Kähler orbifolds rationally equivalent to \(X\) or
\(M\) — plus a finite explicit list for each \(|\Gamma|\).

---

## 1. Charges of ALE bubbles with nontrivial group

Let \(N\) be smooth, complete, ALE with one end \(\mathbb R^4/\Gamma_\infty\), oriented by \(M\), with derivative-controlled
decay of some order \(\tau_0>0\). For a cyclic end the generator acts by \((\zeta,\zeta^q)\), \(\zeta=e^{2\pi i/n}\), in the
orientation of \(N\). Put \(\eta(n,q):=-4\,s(q,n)\), where \(s\) is the Dedekind sum (APS signature-defect
convention). Chern–Gauss–Bonnet and APS give
\[
P(N)=4\!\int_N|W^\pm|^2+\tfrac1{12}\!\int_Ns^2+8\pi^2c_\pm(N),\qquad
c_\pm(N)=\frac{2}{|\Gamma_\infty|}-2\chi(N)\mp3\tau(N)\mp3\eta_{\Gamma_\infty}. \tag{1.1}
\]
Hence \(P(N)\ge8\pi^2\max\{c_+,c_-,0\}\).

**Convention checks (all exact, script).**

| bubble | \(c_+\) | \(c_-\) |
|---|---|---|
| Burns \(\mathcal O(-1)\) | 1 | −5 |
| Eguchi–Hanson | 0 | −6 |
| \(A_3\) hyperkähler | 0 | −15 |
| \(A_6\) hyperkähler | 0 | −192/7 |
| \(\mathrm{EH}/\mathbb Z_2\), complex orientation | 0 | −3 |

**New exact value (checked against the explicit metric).** LeBrun's scalar-flat Kähler ALE metric on \(\mathcal O(-n)\),
\[
g=\frac{dr^2}{V}+r^2(\sigma_1^2+\sigma_2^2)+r^2V\sigma_3^2,\qquad V=1+\frac{n-2}{r^2}+\frac{1-n}{r^4},
\]
has \(s\equiv0\) (symbolic) and \(W^+=0\), so (1.1) predicts
\[
P(\mathcal O(-n),g_{\rm LeB})=8\pi^2\frac{(n-2)^2}{n}.
\]
Direct numerical integration of \(\int|\operatorname{Ric}|^2\), using the orthonormal Bianchi-IX Ricci formulas of
`step48_bianchi_indicial.py` in the \(r\)-coordinate, agrees for \(n=1,\dots,8\) to \(10^{-14}\): the values are
\(1,0,1/3,1,9/5,8/3,25/7,9/2\) in units of \(8\pi^2\). This fixes the η sign: the \(\mathcal O(-n)\) end has
\(q=1\) and \(\eta(n,1)=-(n-1)(n-2)/(3n)\). The \(A_{n-1}\) end has \(q=-1\) and \(\eta=+(n-1)(n-2)/(3n)\).

**Conservation (ledger) identity.** If a bubble region \(N\) with end \(S^3/\Gamma\) is glued into an orbifold point of the
bulk \(V\), then \(\chi_{\rm orb}(V)=\chi(V^\circ)+1/|\Gamma|\) and \(\tau_{\rm orb}(V)=\tau(V^\circ)-\eta_N\). Hence
\[
T_+^{\rm orb}(V)=T_+(M)+c_+(N),\tag{1.2}
\]
and, with the bubble scalar-flat,
\[
\frac{P(V)+P(N)}{8\pi^2}=C_+(V)+w(N)-T_+(M),\qquad w(N):=\frac1{2\pi^2}\int_N|W^+|^2=\frac{P(N)}{8\pi^2}-c_+(N).\tag{1.3}
\]
Here \(C_+(V)=\frac1{2\pi^2}\int|W^+|^2+\frac1{96\pi^2}\int s^2\) is the orbifold integral. A whole subtree hanging below
an orbifold point telescopes to one effective smooth region \(N_{\rm eff}\): internal links cancel exactly as in Theorem G,
and \(4\int|W^+|^2\ge0\) on every piece. So (1.1)–(1.3) apply to \(N_{\rm eff}\).

(1.3) says what a bubble does. It removes \(w(N)\) units of self-dual Weyl energy from the bulk's budget, and the bulk
then needs \(C_+(V)<A-w(N)\) for the configuration to beat (U). The bulk always has \(C_+(V)\ge T_+^{\rm orb}(V)\); (1.2)
makes this the same necessary condition \(\max\{c_+,c_-,0\}<1\).

**Two-piece duality.** If a closed \(Z\) splits as \(N\cup_LW\) along a spherical space form and both pieces are read as ALE
with opposite ends, then \(c_+(N)+c_+(W)=4/|\Gamma|-T_+(Z)\). For \(Z=\overline{\mathbb{CP}}^2=C_2\cup(-B_2)\): \(1+(-3)=-2=1-3\).

---

## 2. Degree-one reduction for orbifold bubbles

**Lemma 55.1.** In a case-(I) configuration on \(M\), let \(N\) be the effective smooth region below any orbifold point
\(p\in V\) of the bulk, with link \(L=S^3/\Gamma_p\). Assume:

(SW\(_L\)) if \(M=A\cup_LB\) with \(L\) a spherical space form and \(b^+(A),b^+(B)\ge1\), then \(SW_M=0\). The one-sided
version also holds: if \(b^+(B)\ge1\), \(b^+(A)=0\), and \(\widehat B=B\cup\mathrm{cone}\) carries a PSC orbifold metric,
then \(SW_M=0\).

Assume also that \(X\) is not a fake projective plane (so \(b^+(M)\ge3\) and \(SW_M\ne0\)). Then \(\pi_1(N)\to\Gamma\) is
trivial, \(H_2(N;\mathbb Q)\to H_2(M;\mathbb Q)\) is injective with image in \(\ker(c_*:H_2(M)\to H_2(X))=\mathbb ZE\), and
\(b_2(N)\le1\). At most one orbifold point of \(V\) has \(b_2(N_{\rm eff})=1\); all the others are rational homology balls.

*Proof.* Van Kampen: \(\Gamma=\pi_1(V^\circ)*_{\Gamma_p}\pi_1(N)\) as a pushout. \(\Gamma_p\) is finite and \(\Gamma\) is
torsion-free, so \(\Gamma_p\) dies and \(\Gamma=\pi_1(V^\circ)/\langle\!\langle\Gamma_p\rangle\!\rangle*\pi_1(N)/\langle\!\langle\Gamma_p\rangle\!\rangle\).
Free indecomposability makes one factor trivial. Suppose the bulk factor were trivial. Then the classifying map
\(c:M\to X\) is null on \(V^\circ\), factors through \(M/V^\circ=\widehat N\), and has degree one. Then \(Q_X\) embeds in
\(Q_N\), so \(b^+(N)\ge3\) while \(b^+(V^\circ)\) is whatever remains. If \(b^+(V^\circ)\ge1\), (SW\(_L\)) gives a
contradiction. If \(b^+(V^\circ)=0\), \(N\) is scalar-flat ALE (bubble criticality, step54 §5(c)), its Green-function
compactification \(\widehat N\) is a PSC orbifold (Lemma 53.Y, orbifold point at infinity), and the one-sided (SW\(_L\))
again contradicts \(SW_M\ne0\). So the bubble factor is trivial and \(c|_N\) lifts to \(\widetilde X\) (contractible). Hence
\(H_2(N)\to H_2(X)\) is zero. Mayer–Vietoris over \(\mathbb Q\) (with \(H_{1,2}(L;\mathbb Q)=0\)) gives
\(H_2(M;\mathbb Q)=H_2(V^\circ;\mathbb Q)\oplus\bigoplus H_2(N_j;\mathbb Q)\) orthogonally, so the \(N_j\) contribute
orthogonal subspaces of the line \(\mathbb QE\). \(\square\)

(SW\(_L\)) is the standard vanishing theorem for splittings along PSC rational homology spheres when both sides have
\(b^+\ge1\). The one-sided orbifold-cap form is the analogue of Lemma 54.3. Both are to be cited precisely; they are
recorded as hypotheses, not re-proved.

**Corollary 55.2 (Kronheimer is a \(k\ge2\) phenomenon).** A hyperkähler ALE bubble has \(H_2\) spanned by \((-2)\)-classes,
while a \(b_2=1\) bubble region at \(k=1\) carries only \(\sigma\mapsto mE\) with \(\sigma^2=-m^2\neq-2\). So no Kronheimer
(\(\Gamma\subset SU(2)\), hyperkähler) bubble occurs at \(k=1\). For general \(k\) the same proof puts every bubble lattice
inside \(\operatorname{span}\{E_i\}\cong-I_k\): this is exactly the Step-52 root-lattice absorption (\(A_1\oplus A_1\subset\mathbb Z^2\), …).

---

## 3. Pricing the \(b_2=1\) orbifold bubbles

Here \(\chi(N)=2\), \(\tau(N)=-1\), and the class is \(mE\). If \(N\) is simply connected, \(|H_1(\partial N)|=m^2\). For a
cyclic end this means \(n=m^2\), and the linking form \(\langle\pm1/m^2\rangle\) forces \(q\) to be a unit square mod
\(m^2\) (\(q=1\) is the \(\mathcal O(-m^2)\) end). Then
\[
c_+=\frac{2}{m^2}-1-3\eta(m^2,q),\qquad c_-=\frac{2}{m^2}-7+3\eta(m^2,q).
\]

**Proposition 55.3.** (a) For \(m=1\) (trivial group: Burns type) and \(m=2\) (the only admissible \(q\) is \(1\), the
\(\mathcal O(-4)\) end), \(c_+=1\). So every such bubble costs \(\ge8\pi^2\), and by (U) and \(P(V)\ge0\) it cannot occur.
LeBrun's \(\mathcal O(-4)\) metric realizes the bound: \(P=8\pi^2\) exactly. *The class \(E\) or \(2E\) cannot escape into an
orbifold bubble with a cyclic end.*

(b) For \(m\ge3\), charge does not exclude: the admissible \(q\) with \(\max\{c_\pm\}<1\) are listed in the JSON. The first
ones are \(m=3\), \(q\in\{4,7\}\) (\(c_+=-23/9\), \(c_-=-5\)); \(m=4\), \(q=9\) (\(c_+=1/4\)); \(m=5\), \(q\in\{6,11,16,21\}\).
These lens spaces occur as boundaries of \(\langle-m^2\rangle\) traces (e.g. lens-space surgeries on \(T(2,5)\)), so the
topology is not empty.

(c) Non-cyclic ends. With \(\Gamma\subset SU(2)\) in the *reversed* orientation, \(c_+=4/|\Gamma|+r-3\ge1\) for every
\(D_r,E_r\), so all of those are excluded. With \(\Gamma\subset SU(2)\) in \(M\)'s orientation (η from Kronheimer's \(P=0\):
\(\eta=(2/|\Gamma|+r-2)/3\)): \(c_+=1-r\), \(c_-=4/|\Gamma|-9+r\). Charge excludes \(D_r\) for \(r\ge10\). It does not
exclude \(D_4,\dots,D_9,E_6,E_7,E_8\). Simple connectivity and the linking form (\(H_1\) cyclic of order \(m^2\) with form
\(\langle-1/m^2\rangle\)) leave \(m=2\): \(D_5,D_9\) (\(H_1=\mathbb Z_4\), \(r\equiv1\bmod4\)), and \(m=1\): \(E_8\). The last is a
bubble carrying \(E\) itself with Poincaré-sphere end, topologically the \(-1\)-trace of the left-handed trefoil, with
\(c_+=-7\) and \(c_-=-29/30\).

Interpretation through (1.3). Each surviving case has \(c_+<1\) and pushes charge into the bulk:
\(T_+^{\rm orb}(V)=A-1+c_+\) (for \(E_8\), \(A-8\)). To beat (U) the bulk needs \(C_+(V)<A-w(N)\) with
\(w(N)\ge\max\{0,-c_+,c_--c_+\}\) (for \(E_8\), \(w\ge7\)). An orbifold LeBrun estimate (\(C_+(V)\ge2A/3\), assuming an
orbifold SW package on \(V\) that retains the canonical class) would exclude a channel whenever \(A\le3w(N)\). So it
removes the strongly negative channels for small \(X\) only.

---

## 4. Rational-ball bubbles and the T-singularity channel

Here \(\chi=1\) and \(\tau=0\), \(n=|H_1(\partial N)|=m^2\), and \(c_\pm=2/n-2\mp3\eta\). Exact computation for \(m\le10\) and all
\(q\): about half the lens ends have \(\max c_\pm\ge1\) and are excluded. For \(m\ge3\) the maximum over \(q\) grows like
\(m^2\).

**Proposition 55.4 (zero charge = T-singularity Milnor fibres).** For every T-singularity \(\tfrac1{n^2}(1,na-1)\),
\(\gcd(n,a)=1\), \(n\le10\), the end has \(c_+=0\) in the complex orientation and \(c_-=-4(1-1/n^2)\) (exact, script). The
Milnor fibre \(B_{n,a}\) carries a Ricci-flat Kähler ALE metric, the free \(\mathbb Z_n\)-quotient of the \(A_{n-1}\) hyperkähler
metric (Şuvaina–Wright type; citation to register). In its complex orientation \(W^+=0\), so \(P=0\) attains the charge
bound. In the reversed orientation \(w=4(1-1/n^2)\). Example: \(\mathrm{EH}/\mathbb Z_2=D(T^*\mathbb{RP}^2)\) has charges
\((0,-3)\).

So a zero-charge rational-ball bubble is precisely the Riemannian shadow of a \(\mathbb Q\)-Gorenstein smoothing. Write the
bulk as \(V=(Y\setminus C)\cup\mathrm{cone}\), where \(C\) is the resolution chain. Then \(M=Y_C\) is the rational blowdown,
and (1.2) gives \(T_+^{\rm orb}(V)=A-1\): no charge moves.

**Theorem 55.5 (lattice condition for the zero-charge channel at \(k=1\)).** Suppose a case-(I) configuration on \(M\) has
a \(B_{n,a}\) bubble in its complex orientation. Let \(Y=V^\circ\cup C\), with \(C\) the minimal-resolution plumbing of
length \(r\). Then:

(i) \(\pi_1(Y)=\Gamma\), and \(Y\to X\) has degree one.

(ii) Every sphere of \(C\) lies in \(K=\ker c_*\subset H_2(Y)\), a negative-definite unimodular lattice of rank \(r+1\); for
\(r\le6\), \(K\cong-I_{r+1}\).

(iii) The chain lattice \(C_{n,a}\) embeds **primitively** in \(K\).

Consequently: **a primitive embedding into some negative-definite unimodular lattice of rank \(r+1\) exists iff
\(1-na\) is a unit square mod \(n^2\), iff \(n\) is odd or \(8\mid n\).** The zero-charge T-channel at \(k=1\) is therefore
impossible for \(n\equiv2,4,6\pmod 8\) and lattice-allowed otherwise. Exhaustive search into \(-I_{r+1}\)
(`step55_Tchain_embeddings.json`) confirms both directions for all \(n\le7\). Discriminant values were checked for all
79 T-singularities with \(n\le16\) (`step55_Tchain_discriminants.json`): \(\beta\equiv1-na\), and the unit-square test
matches the parity law.

*Proof.* (i) \(\pi_1(M)\) is the pushout of \(\pi_1(V^\circ)\leftarrow\pi_1(L)\to\pi_1(B)=\mathbb Z_n\), and the right map is onto. The
image of the finite group \(\pi_1(L)\) in the torsion-free \(\Gamma\) is trivial, so
\(\Gamma=\pi_1(V^\circ)/\langle\!\langle\pi_1L\rangle\!\rangle*\pi_1(B)/\langle\!\langle\pi_1L\rangle\!\rangle\) and the second factor is trivial.
Since \(C\) is simply connected, \(\pi_1(Y)=\pi_1(V^\circ)/\langle\!\langle\pi_1L\rangle\!\rangle=\Gamma\). Both classifying maps are
null on \(C\) and on \(B\), so both factor through \(V^\circ/\partial V^\circ\); hence \(\deg(Y\to X)=\deg(M\to X)=1\).

(ii) A degree-one map splits \(H_2(Y)=K\oplus c^!H_2(X)\) orthogonally with \(Q_Y|_{c^!H_2X}\cong Q_X\), so \(K\) is
unimodular. Its rank is \(b_2(M)+r-b_2(X)=r+1\), and its signature \(\tau(M)-r-\tau(X)=-(r+1)\). Spheres map to zero in
\(H_2(X)\) because \(\pi_2(X)=0\). Unimodular definite lattices of rank \(\le7\) are diagonal.

(iii) This is the step that uses torsion. The sequence of \((Y,V^\circ)\) gives
\(0\to\operatorname{coker}(H_2(Y)\to C^*)\to H_1(V^\circ)\to H_1(Y)\to0\). The cokernel \(G_c\), of order \(o\), equals
\(\operatorname{coker}(K\to C^*)\) because \(Q_X\perp C\), and it is the image of \(H_1(L)=\mathbb Z_{n^2}\). Mayer–Vietoris for
\(M=V^\circ\cup B\), with \(H_1(B)=\mathbb Z_n\) and \(H_1(L)\to H_1(B)\) onto, gives
\(|\mathrm{tors}\,H_1(M)|=|\mathrm{tors}\,H_1(Y)|\cdot\gcd(o,n)\). But \(\pi_1(M)=\pi_1(Y)=\Gamma\), so \(\gcd(o,n)=1\). Since
\(o\mid n^2\), \(o=1\): \(K\to C^*\) is onto, i.e. \(C\) is primitive. For the congruence: primitivity in unimodular \(K\) makes
\(C^\perp=\langle w\rangle\) with \(w^2=-n^2\) (\(\det C^\perp=\det C\)), and the gluing needs an anti-isometry
\(\operatorname{disc}(C)\cong-\operatorname{disc}\langle-n^2\rangle=\langle1/n^2\rangle\). The chain's discriminant form is
\(\langle\beta/n^2\rangle\) with \(\beta\equiv1-na\) (computed), so the condition is \(1-na\equiv u^2\pmod{n^2}\). Conversely, an
anti-isometry produces a unimodular overlattice, so the condition is also sufficient. Odd squares are \(\equiv1\pmod8\), while
\(1-na\equiv3,5,7\pmod8\) when \(v_2(n)\in\{1,2\}\); for \(v_2(n)\ge3\), \(1-na\equiv1\pmod8\). For odd primes, \(1-na\equiv1\pmod p\)
is a square by Hensel. For \(r+1\ge8\) the overlattice need not be \(-I_{r+1}\), but any unimodular \(K\) is admissible in (ii).
\(\square\)

**The strategist's \(S^4\)-free example is excluded; the first real one is \(n=3\).** For \(n=2\) (\(B_2=\mathrm{EH}/\mathbb Z_2\))
the only embedding of \(\langle-4\rangle\) in \(-I_2\) is \(2E'\), which is not primitive. Equivalently, the standard
\(B_2\subset\overline{\mathbb{CP}}^2\) (the complement of the conic) sits in the *reversed* orientation: charge \(-3\), bulk
\(V=X\#\overline{\mathbb P}(1,1,4)\) with \(T_+^{\rm orb}=A-4\) and \(w=3\). This is a negatively charged channel. For \(n=3\),
\(a=1\) (chain \([5,2]\)), \(v_1=2e_1+e_2\), \(v_2=-e_2-e_3\) is primitive in \(-I_3\). It is realized smoothly in
\(\#3\overline{\mathbb{CP}}^2\) by the spheres \(2E_1+E_2\) (conic \(\#\) line) and \(E_2+E_3\) (tube), meeting once. If the
rational blowdown \(Z=(\#3\overline{\mathbb{CP}}^2)_{C_{9,2}}\) is diffeomorphic to \(\overline{\mathbb{CP}}^2\) (it is a closed
negative-definite \(b_2=1\) manifold with \(H_1=0\); simple connectivity of the complement is still to be checked), then
\(M=X\#Z\) carries the zero-charge configuration. The bulk is the orbifold \(V=X\#\mathcal O_{9,2}\), rationally \(M\), with
one \(\tfrac19(1,2)\) point and \(T_+^{\rm orb}=A-1\); the bubble is the Ricci-flat \(B_{3,1}\) at cost \(0\).

**Proposition 55.6 (the zero-charge bulk is non-Kähler).** Suppose the orbifold \(V\) of the zero-charge channel were a
complex orbifold, with the T-point a complex quotient singularity. Then its minimal resolution \(Y\) is a compact complex
surface containing the holomorphic chain \(C\). Moreover \(\pi_1(Y)=\Gamma\), and \(Y\) has a degree-one map to \(X\) whose kernel
lattice is \(K\) of rank \(r+1\). \(Y\) has \(b^+\ge3\) and nonzero SW invariants (rational blowdown formula from \(SW_M\ne0\)), so it
is of general type. Its minimal model \(X'\) satisfies \(b_2(Y)-b_2(X')=r+1\) (the blow-down classes span \(K\)). Every curve
whose class lies in \(K=\ker c_*\) is contracted to points by \(Y\to X'\), so \(C\) lies in the exceptional locus of \(r+1\)
blow-ups. *Counting:* in a sequence of \(r+1\) point blow-ups each new exceptional curve starts with square \(-1\), and each
later centre lies on at most two earlier exceptional curves. Hence
\(\sum_{\text{all }r+1\text{ components}}(-D_j^2)\le(r+1)+2r=3r+1\). A T-chain (\(d=1\)) has \(\sum b_i=3r+1\): it is generated
from \([4]\) by \([b_1,\dots,b_r]\mapsto[2,b_1,\dots,b_r+1]\) or \([b_1+1,\dots,b_r,2]\), each step adding \(3\). The remaining
\((r+1)\)-st component contributes \(\ge1\), so \(3r+2\le3r+1\), a contradiction. \(\square\)

So in the Kähler category this channel cannot reach \(M\). Instead, a KE orbifold with T-points has
\(\mathbb Q\)-Gorenstein smoothings (Biquard–Rollin type, citation to register), which are minimal surfaces with two SW basic
classes rather than the four of \(M\). The \(b_2=1\) channels of §3 are not covered by this counting argument.

---

## 5. The reduced \(k=1\) theorem (orbifold part)

**Theorem 55.7.** Let \(X\) be a ball quotient other than a fake projective plane, and \(M=X\#\overline{\mathbb{CP}}^2\). In a
case-(I) minimizing configuration, assume \(\mathrm H_{\rm lsc}\), \(\mathrm H_{\rm dec}\) (any group), (SW\(_L\)) and bubble
criticality. Then exactly one of the following holds:

(A) every cone point has trivial group, and Theorem 54.A applies (attainment / Einstein-or-non-Bach-flat, modulo exotic
\(S^4\) caps and \(\mathrm H_{\rm eq},\mathrm H_{\rm rem}\));

(B) there is one orbifold point whose bubble region carries \(mE\), with \((m,\Gamma)\) in the explicit charge-allowed list
of Prop. 55.3 (so \(m\ge3\) for cyclic ends; \(m=2\) only with \(D_5,D_9\) ends; \(m=1\) only with the \(E_8\) end);

(C) all orbifold points are rational-ball bubbles with \(\max c_\pm<1\). Each is a T-type zero-charge ball with primitive
chain embedding (Thm 55.5; \(n\) odd or \(8\mid n\)), a negatively charged ball (e.g. reversed T-type), or a non-T ball
from the JSON list.

In (B) and (C) the bulk is a non-Kähler \(P\)-critical orbifold with
\[
p_*(M)\ \ge\ 8\pi^2\big[C_+(V)+\textstyle\sum w(N_j)-(A-1)\big],
\]
and, if every bubble in the configuration has \(P=0\) (the Ricci-flat T-balls), reassembly gives
\(p_*(M)=\alpha_{\rm orb}(V)=P(V,g_0)\), attained on the orbifold.

So the orbifold gate at \(k=1\) is equivalent to the following **orbifold threshold problem**: show
\(\alpha_{\rm orb}(V)\ge8\pi^2\bigl(1-\max\{c_+,c_-,0\}\bigr)\) (more precisely \(C_+(V)+w\ge A\)) for the explicit non-Kähler
orbifold degenerations \(V\) of \(M\) listed above, or construct one that beats the analytic CH cell. That construction
would be a genuine orbifold absorption of \(E\) (or \(3E\), …) and a new nonattainment mechanism.

What this does **not** do: it gives no unrestricted lower bound for \(P\) on orbifolds. LeBrun's \(2A/3\) is too weak except
for \(A\le3w\). The Kähler orbifold bound \(C_+\ge T_+^{\rm orb}\) is sharp (KE orbifolds) but irrelevant, since the bulks
are non-Kähler.

---

## 6. Collapse gate: what the hyperbolicity of \(\Gamma\) gives

**Lemma 55.8 (cyclic-image lemma).** Let \(f:\Sigma\to M\) be a map of a closed oriented surface whose composite
\(\pi_1\)-image in \(\Gamma\) is cyclic (e.g. \(\Sigma=S^2\) or \(T^2\), since abelian subgroups of the torsion-free hyperbolic
group \(\Gamma\) are cyclic). Then \(f_*[\Sigma]\in\operatorname{span}\{E_i\}\). More generally, every class in the image of
\(H_2(C)\to H_2(M)\) lies in \(\operatorname{span}E_i\) for any region \(C\) whose \(\pi_1\)-image in \(\Gamma\) is cyclic.

*Proof.* \(X=K(\Gamma,1)\), so \(c\circ f\) is determined up to homotopy by \(\pi_1\). A cyclic image factors through
\(K(\mathbb Z,1)=S^1\), so \((c\circ f)_*[\Sigma]=0\), and \(\ker c_*=\operatorname{span}E_i\). (The bounded-cohomology route,
in which \(H^2_b\to H^2\) is onto for hyperbolic \(\Gamma\) and the \(\ell^1\)-seminorm is a norm on \(H_2(\Gamma;\mathbb R)\), gives the
same for amenable images, which are cyclic here. It would add genuinely new information only through Gromov's
multiplicity-\(\le2\) vanishing, which \(F\)-structure covers do not satisfy in general.) \(\square\)

**What this settles and what it does not.**

- *Settled.* Combined with the step-54 free-circle spin lemma: a collapsing region with a free circle action, or with
  cyclic \(\pi_1\)-image, cannot carry \(E\) (\(E^2\) odd), and in the cyclic case carries no class of \(X\).
- *Not settled — the obstruction, stated sharply.* A collapsed region \(C\) carrying a negative class changes the ledger in
  the **wrong** direction for an exclusion. With \(\chi(C)=0\), (1.2) becomes \(T_+(\Omega)=A-1-3\tau(C)\) up to boundary
  η-terms. If \(\tau(C)=-1\), then \(P(\Omega)=8\pi^2[C_+(\Omega)-(A+2)]\) while \(P(C)\to0\) under bounded-curvature collapse. Charge
  accounting therefore forces no positive cost on the configuration. The whole burden moves to whether a complete
  finite-volume \(P\)-critical \(\Omega\) with collapsing ends can have \(C_+(\Omega)<A+3\) (to beat (U)), a regime where no
  estimate is available. Collapse is thus the one degeneration in which \(E\) can disappear from the topological ledger at
  zero bubble energy. It must be excluded topologically: show that no
  region with a positive-rank \(F\)-structure (finite isotropy allowed, no fixed points) contains a class of odd square.
  The supporting facts are that fixed-point-free \(S^1\)-actions on closed 4-manifolds have \(\tau=0\) (\(G\)-signature) and
  that free ones are spin. The missing pieces are the Seifert/finite-isotropy and torus-isotropy cases and the boundary
  η-terms of graph-manifold interfaces.

---

## 7. Remarks

1. *Einstein metrics on \(M\) sit far from the Yamabe-optimal classes* (strategist's remark, verified). Theorem Y at
   \(P=0\) gives \(8\pi^2k\le4\Delta V\), with \(\Delta V=(Y[g]^2-32\pi^2A)/16\). Hence \(Y[g_E]^2\ge32\pi^2(A+k)\), while
   \(\inf_{[g]}Y[g]^2=32\pi^2A\) (LeBrun). For \(k=1\): \(Y[g_E]^2\ge32\pi^2(A+1)\).
2. *Correction to the strategist's #70.* "Every bubble has \(H_2\subset\langle E\rangle\)" needs (SW\(_L\)); without it a bubble
   could carry \(\Gamma\). "Kronheimer excluded outright at \(k=1\)" is right. "What survives with \(\Gamma\ne1\) is a finite list"
   is right for each fixed \(|\Gamma|\), but the list is infinite in \(m\) and contains non-cyclic \(D_5,D_9,E_8\) ends. The
   \(\mathcal O(-4)\) candidate is excluded (charge exactly 1). The rational-ball case does survive, but not as
   \(\mathrm{EH}/\mathbb Z_2\) in the zero-charge orientation; its first zero-charge member is \(B_{3,1}\).
3. *Why charge alone cannot finish.* Conservation (1.3) shows every channel has total Kähler-type baseline exactly that of
   \(M\). The discriminating information must come from a non-Kähler orbifold estimate or from the CH-germ interaction,
   exactly as the analytic cell beats the Kähler baseline for smooth bubbles.
