# Step 94 — What the transferred forced-zero field can actually constrain

Session S1003A01, Agent1, Explore. Inputs: Step 93 §8; Spirit #125; the corrected mixed Einstein edge in `spirit_step85_full_mixed_endpoint_correction.md`; the weighted-pencil and normalized-linear-coercivity sections of `Skills/geometric-analysis/research/Curvature_Realizability.tex`; LeBrun's source record `Knowledge/objects/papers/Weyl-curvature-Einstein-metrics-and-Seiberg-Witten-theory--09b745ed7106--adbf7ae87208/object.md`; and TTCS integration `trace/ttcs/results/step94_ttcs01_generator2_integration.md`.

## 1. The question sharpened

Let \(V\) be one of the marked Wahl orbifolds covered by Proposition 93.Y, and suppose hypothetically that \(g\) is a negative Einstein orbifold metric in the complex orientation. Write
\[
\operatorname{Ric}=-(\lambda/4)g,\qquad s=-\lambda<0,
\]
and let \((A,\Phi)\) be a Step-93 supplied unperturbed monopole for a forced-zero sign class, selected so that
\[
p=(a_g^+)^2\ge A_0,
\qquad \Phi(p_0)=\nabla_A\Phi(p_0)=0
\]
at the Wahl point \(p_0\). Put \(U=|\Phi|^2\) in the Step-93 ordinary normalization. Then
\[
0\le U\le\lambda,
\qquad 4G:=4\int|\nabla_A\Phi|^2=\int U(\lambda-U),
\]
and the exact scalar-slack identity is
\[
\boxed{\lambda^2V-\int U^2=8G+\int(\lambda-U)^2.}\tag{94.1}
\]
The forced zero makes the right side strictly positive for each fixed metric. Spirit #125 correctly observes that this is not yet an Einstein obstruction: the full mixed LeBrun inequality already requires nonzero scalar/Weyl slack in the range \(0<k<A_0/3\), and extra scalar excess can be absorbed there.

The relevant question is therefore not whether a zero costs scalar energy, but whether the *same supplied field* forces a part of the Einstein scalar--\(W^+\) budget that cannot coexist with \(P=\int|\operatorname{Ric}^{\circ}|^2=0\).

## 2. Exact Einstein budget and the available slack

For \(T_+^{\mathrm{orb}}=A_0-k\), Chern--Weil at an Einstein metric gives
\[
4\pi^2(A_0-k)=\frac{S}{24}+2W,
\qquad S=\lambda^2V,
\qquad W=\int|W^+|^2.\tag{94.2}
\]
The full one-field mixed estimate is
\[
(\sqrt S+\sqrt{6W})^2\ge72\pi^2p\ge72\pi^2A_0.\tag{94.3}
\]
Putting \(x=S/(96\pi^2)\), (94.2)--(94.3) imply
\[
[\sqrt{8x}+\sqrt{A_0-k-x}]^2\ge6A_0,\tag{94.4}
\]
so the least allowed scalar scale is
\[
x_{\min}=\frac{A_0}{27}\left[4-\sqrt{1-3k/A_0}\right]^2.\tag{94.5}
\]
Equivalently,
\[
D_W:=S/24-W\ge4\pi^2k+rac{8\pi^2A_0}{9}
\left[1-\sqrt{1-3k/A_0}\right]^2.\tag{94.6}
\]
For any candidate strictly above (94.5), the mixed inequality has room to absorb a scalar zero cost. Thus a lower bound on \(\lambda r_0^2\), by itself, does not exclude Einstein metrics.

There is also unavoidable projection slack. Every supplied blow-up class satisfies
\[
a^2=A_0-k=T_+^{\mathrm{orb}},\qquad
p=a^2+\|a^-\|^2.
\]
Hence \(p-A_0=\|a^-\|^2-k\) can be nonzero. Selecting a forced-zero class with \(p\ge A_0\) is enough for (94.3), but it does not identify \(p\), and the zero character does not itself lower-bound \(p-A_0\). A contradiction at the sharp mixed edge would require controlling this projection term together with the field's analytical deficit.

## 3. The same-field deficit decomposition

The corpus weighted-pencil theorem provides the right parent quantity. For \(w=\sqrt6|W^+|\),
\[
\mathfrak D_\beta(g,a)=\frac{\beta+1}{\beta}\int(s^2+\beta w^2)-72\pi^2p,
\]
with exact decomposition
\[
\mathfrak D_\beta
=\underbrace{\left(\int(-s+w)_+^2-72\pi^2p\right)}_{\Delta_+}
+\int(-s+w)_-^2+\frac1\beta\int(s+\beta w)^2.\tag{94.7}
\]
At a negative Einstein metric, \((-s+w)_-=0\). Theorem 1 of the weighted-pencil section therefore gives, for every finite \(L>2\),
\[
\boxed{\mathfrak D_\beta\ge
c'_L\frac{\beta}{\beta+1}(\beta-2)^2V,
\quad 2\le\beta\le L,}\tag{94.8}
\]
because here \(a^2=T_+^{\mathrm{orb}}\). This is already a stronger differential compatibility statement than the classical mixed inequality away from \(\beta=2\). It is not yet an exclusion: after (94.2), (94.8) is another lower half-plane in \((S,W,V,p)\), and \(V=S/\lambda^2\) is scale-covariant in exactly the way needed to keep the inequality scale invariant. No current topological upper budget contradicts it throughout \(0<k<A_0/3\).

The only endpoint where the right side of (94.8) vanishes is \(\beta=2\), the actual Kähler--Einstein branch. At this endpoint the corpus does retain same-field information. In the \(\operatorname{Ric}=-g\), \(s=-4\) scale, define
\[
D_2=\frac32S+18W-72\pi^2p.
\]
The actual weighted solution produces a bounded self-dual polynomial form \(\omega=q(\Phi)\) and a polynomial Weyl model \(W_0(\omega)\) such that, schematically and with the corpus universal constants,
\[
J_++\|\rho-\rho_0\|_2^2+
\|W^+-W_0\|_2^2+
\|\operatorname{Ric}+g\|_2^2
\le C D_2,\tag{94.9}
\]
\[
\|\omega+2\pi H_a\|_2^2\le C D_2,
\qquad
\int|d\omega|^2+\int|\nabla\omega|^2\le G(D_2/V)V.\tag{94.10}
\]
Thus \(D_2\to0\) forces the *same field* toward a nowhere-zero constant-length harmonic form, aligns its harmonic representative, and forces \(W^+\) toward the Kähler polynomial model. A forced zero is incompatible with exact \(D_2=0\), which recovers strictness. But zeros in real dimension four are \(H^1\)-cheap: without a controlled geometric scale, (94.9)--(94.10) admit \(D_2\downarrow0\) through a shrinking zero neighborhood.

This identifies the precise quantity to which a marked-character estimate must attach:
\[
\boxed{D_2/V\quad\text{(or an equivalent retained sum in (94.9)--(94.10)), not scalar slack alone.}}\tag{94.11}
\]
A useful point-sensitive theorem would have to prove
\[
D_2\ge \mathcal C(\chi_{\rm loc},g,A,\Phi)>0\tag{94.12}
\]
for the forced marked character, and then combine (94.12) with (94.2), projection control, and a topological upper relation strong enough to make \(P=0\) impossible. A mere bound on (94.1) does not do this.

## 4. What the marked link character does not supply

The clean-context marked-link analysis in `step94_ttcs01_generator2_integration.md` eliminates several tempting shortcuts.

1. For every extendible twist \(m=nj\in n\mathbb Z/n^2\mathbb Z\), the exact Step-93 Kawasaki calculation gives
\[
\delta(m)=\delta(0).
\]
Using the same positive-scalar-curvature cap, the relative reduced Dirac eta invariant is therefore exactly zero. The character produces no new APS rho term.

2. The extendible subgroup is isotropic for the lens-space linking form. Its flat holonomy is real marked information but can be carried by a flat determinant connection on the Ricci-flat Wahl filler at zero abelian curvature cost.

3. If the spinor zero is isolated, an equivariant normalized-spinor degree \(D_{p_0}\) satisfies
\[
D_{p_0}(n-1)\equiv m(m-n)\equiv0\pmod{n^2}.
\]
Thus the character forces no nonzero fractional local Euler residue. Any surviving integer degree is not fixed by the character and is cheap in unnormalized \(H^1\) energy.

4. Ordinary stress, Weitzenböck, Chern--Simons and Pohozaev fluxes vanish on shrinking links by removability and the order-at-least-two zero. Renormalizing by powers of radius or \(|\Phi|\) extracts a jet invariant, not a conserved unscaled flux.

5. The invariant algebra
\[
W^+(p_0)=\mu\operatorname{diag}(2,-1,-1)
\]
has no scale-independent local mass. Because \(\Phi(p_0)=\nabla_A\Phi(p_0)=0\), curvature first enters the Dirac Taylor recursion only after the leading flat equivariant monogenic mode.

Therefore the field-transfer theorem does not yet hide an unused topological boundary payment. The first genuinely new local datum would be the actual leading equivariant Dirac jet
\[
0\ne P_\ell\in \ker D_0\cap
\operatorname{Hom}_\Gamma(\operatorname{Sym}^\ell T_{p_0},S^+_{p_0}),
\qquad \ell\ge2,\tag{94.13}
\]
and its curvature-sensitive continuation equation for the next Taylor coefficient. The character restricts the possible \(P_\ell\), but does not select one or its amplitude.

## 5. Route decision

The Step-93 marked bubble-tree proposal is not ready for large investment. Before classifying bubble transport, one must first derive a relative identity whose transported datum contributes to \(D_2\), harmonic/Weyl alignment, or another combined budget that can contradict \(P=0\). The link invariants above do not provide it.
The strongest Wahl-specific next experiment is consequently local and finite. Its first part is an exact rational representation calculation, `workspace/scripts/step94_wahl_monogenic_modes.py` → `workspace/data/step94/wahl_monogenic_modes.json` (current version authoritative). With \(\Gamma=\frac1{n^2}(1,n-1)\), fibre weights \((m,m-n)\), \(m=nj\), and the coefficient-weight convention of Step 93, the compatible (equivariant) flat Dirac operator is
\[
D^+=\begin{pmatrix}\partial_{z_1}&\partial_{\bar z_2}\\-\partial_{z_2}&\partial_{\bar z_1}\end{pmatrix},
\qquad (D^+)^*D^+=-\tfrac14\Delta I,
\]
whose two summands in each row carry the same character (output weights \((m-1,m-(n-1))\)). For every odd \(n\ge3\) and every forced extendible twist \(j=2,\dots,n-1\), the first permitted degree of a nonzero equivariant homogeneous monogenic spinor is
\[
\boxed{\ell_{\min}(n,j)=2\min\{j-1,\,n-j\}.}\tag{94.14}
\]
*Proof.* Write a monomial \(z_1^az_2^b\bar z_1^c\bar z_2^d\), \(P=a-c\), \(Q=b-d\); its weight is \(P-Q+nQ\). If its degree \(\ell<n\) and its weight is \(\equiv0\pmod n\), then \(P=Q=r\), the weight is \(nr\) and \(\ell\ge2|r|\). The two components require \(r\equiv j\) and \(r\equiv j-1\pmod n\) respectively, so no input exists below \(2\min\{j-1,n-j\}\le n-1\). The bound is attained by \((0,(z_1z_2)^{j-1})\) when \(j-1\le n-j\) and by \(((\bar z_1\bar z_2)^{n-j},0)\) otherwise, both killed by \(D^+\); the first-degree kernel is one-dimensional except at \(j=(n+1)/2\), where it is two-dimensional. \(\square\) The exact data reproduce the tables \(2\); \(2,4,2\); \(2,4,6,4,2\); \(\dots\) for \(n=3,\dots,11\). Equivariant polynomial surjectivity follows from \(D^+(D^+)^*=-\Delta/4\) and averaging.

For the classes actually supplied by Proposition 93.C when odd \(n\ge5\) (odd subsets \(F\subset\{1,2,3,4\}\), \(j_F=h(-1_{1\in F}+1_{2\in F}+1_{3\in F}+1_{4\in F})\), \(h=(n+1)/2\)), the twists are \(j=(n-1)/2,(n+1)/2,(n+3)/2\) with multiplicities \(1,6,1\) and \(\ell_{\min}=n-3,n-1,n-3\). Hence every supplied forced field satisfies \(\operatorname{ord}_{p_0}\Phi\ge n-3\) (\(\ge2\) for \(n=3\)); the forced-subfamily averaging of Step 93 §8 is unaffected. Representation theory gives a minimum, not the actual order or amplitude.

*Correction record.* The first version of the script paired \(\begin{pmatrix}\partial_{\bar z_1}&\partial_{\bar z_2}\\-\partial_{z_2}&\partial_{z_1}\end{pmatrix}\) with the weights \((m,m-n)\); that matrix is not equivariant for those weights (row summands differ in character by \(2\)) and its output \(\ell=n\) is an artefact. See `trace/ttcs/results/step94_ttcs02_verifier1_integration.md`.

The next work was to compute the curvature-sensitive Taylor recursion of the coupled SW system at an Einstein Wahl point and to test whether any sign-definite pairing survives. **This has been settled in Step 95** (`step95_sw_formal_completion_at_wahl_points_and_route_value.md`, Theorem 95.1): the recursion is triangular with an equivariant polynomial right inverse at every degree, for every invariant metric jet, so no finite-order pairing survives; the marked order and amplitude are locally free. The Wahl zero route therefore has no present path beyond scalar strictness, and new investment returns to Q4's closed problem or Q2/Q3, without declaring global compatibility exhausted.
This is substantially narrower than a degeneration classification and directly tests the implication Spirit #125 asks for. If the local pairing is freely cancellable, the Wahl zero route has no present path beyond scalar strictness; priority should then return to Q4's closed endpoint or Q2/Q3's all-metric/attainment problem rather than accumulating bubble-tree structure without an Einstein consequence.

## 6. Preserved conclusions

- Theorem 93.A and the lossless actual-field transfer remain useful and unchanged.
- Forced-zero class selection retains \(p\ge A_0\) and proves fixed-metric strict scalar inequality, but no uniform Einstein gap.
- The full mixed edge (94.5)--(94.6), not \(D_W=4\pi^2k\), is the current necessary Einstein budget.
- The weighted-pencil family already encodes same-field differential compatibility away from \(\beta=2\); its endpoint retained fields show exactly where a forced zero would have to enter.
- No presently identified marked lens-space invariant converts the forced character into trace-free Ricci energy.
