# Step 3 theorem note: stable integral obstructions to Ricci pinching in dimension four

This note extracts a reusable principle from the corrected LeBrun/Ishida--LeBrun calculation. It is not a proof of Yau Problem 26; it is a precise obstruction theorem for one class of four-dimensional refutation routes.

## Setup

Let \((M^4,g)\) be a closed oriented Riemannian four-manifold and write
\[
T_+(M)=2\chi(M)+3\tau(M),
\qquad
F_+(g)=\frac1{4\pi^2}\int_M\left(\frac{s_g^2}{24}+2|W_g^+|^2\right)d\mu_g.
\]
The Chern--Gauss--Bonnet/signature identity is
\[
T_+(M)=F_+(g)-\frac1{4\pi^2}\int_M\frac{|\mathring r_g|^2}{2}\,d\mu_g. \tag{CGB+}
\]
Here \(\mathring r\) is the trace-free Ricci tensor. Thus any topological or gauge-theoretic inequality of the form
\[
F_+(g)\ge L_+\qquad\text{for every Riemannian metric }g\text{ on }M \tag{I+}
\]
has two different consequences:

1. If \(g\) is Einstein, then \(\mathring r_g=0\), so \(T_+(M)=F_+(g)\ge L_+\). Therefore \(L_+>T_+(M)\) rules out Einstein metrics.
2. If \(g\) is merely tightly Ricci-pinched, then (CGB+) shows that the excess \(L_+-T_+(M)\) must be supplied by trace-free Ricci energy. This turns the Einstein obstruction into a quantitative lower bound for \(\delta\).

## Stable obstruction theorem

Assume \(T_+(M)>0\) and \((I+)\) holds with \(L_+>T_+(M)\). Suppose \(g\) satisfies normalized negative Ricci pinching
\[
\|\operatorname{Ric}_g+g\|_{op}\le \delta<1.
\]
If
\[
b(\delta):=\frac23(1-\delta)^2-2\delta^2>0,
\]
then
\[
\frac{\delta}{1-\delta}\ge
\sqrt{\frac{L_+-T_+(M)}{3L_+}}. \tag{*}
\]

The same proof works for positive normalized pinching \(\|\operatorname{Ric}_g-g\|_{op}\le\delta<1\) because only \(s^2\) and \(|\mathring r|^2\) enter. It also works with \(T_-=2\chi-3\tau\), \(F_-(g)=\frac1{4\pi^2}\int(s^2/24+2|W^-|^2)\), after reversing orientation or replacing \(+\) by \(-\).

### Proof

Let the eigenvalues of the Ricci endomorphism relative to the target \(\sigma g\), \(\sigma=\pm1\), be \(\sigma+e_i\) with \(|e_i|\le\delta\). Then
\[
|s|\ge4(1-\delta),
\qquad
|\mathring r|^2=\sum_i(e_i-\bar e)^2\le\sum_i e_i^2\le4\delta^2.
\]
Combining \((I+)\) with \((CGB+)\) gives
\[
L_+-T_+(M)\le \frac1{4\pi^2}\int\frac{|\mathring r|^2}{2}
\le \frac{\delta^2}{2\pi^2}\operatorname{Vol}(M,g). \tag{1}
\]
On the other hand, from \((CGB+)\), \(W^+\ge0\), and the pointwise bounds above,
\[
T_+(M)\ge \frac{\operatorname{Vol}(M,g)}{4\pi^2}
\left[\frac23(1-\delta)^2-2\delta^2\right]
=\frac{\operatorname{Vol}(M,g)}{4\pi^2}b(\delta). \tag{2}
\]
Thus \(\operatorname{Vol}\le4\pi^2T_+/b(\delta)\). Insert this into (1):
\[
(L_+-T_+)b(\delta)
\le 2T_+\delta^2.
\]
Since \(b(\delta)=\frac23(1-\delta)^2-2\delta^2\), this implies
\[
(L_+-T_+)\frac23(1-\delta)^2
\le 2\bigl(T_++L_+-T_+\bigr)\delta^2=2L_+\delta^2.
\]
Dividing by \(2/3\) and taking square roots gives (*).

The proof deliberately uses only integral inequalities valid for all metrics, the four-dimensional curvature identity, and pointwise Ricci pinching. Therefore it captures precisely why such Einstein nonexistence mechanisms are perturbatively stable under small trace-free Ricci error.

## Application: LeBrun blow-ups

Let \(M=X\#k\overline{\mathbb{CP}}{}^2\), where \(X\) is a minimal complex surface of general type, and write \(A=c_1^2(X)>0\). Then
\[
T_+(M)=2\chi(M)+3\tau(M)=A-k.
\]
LeBrun's 2001 estimate gives, for every metric,
\[
F_+(g)\ge \frac23 A.
\]
This is source-checked in `Knowledge/objects/papers/Ricci-curvature-minimal-volumes-and-Seiberg-Witten-theory--16b01946d13f--cab40be18df4/object.md`, lines 281--349, and is equivalent to Corollary 3.4's no-Einstein theorem for \(k\ge A/3\). Applying (*) with \(L_+=2A/3\) and \(T_+=A-k\) gives, for \(p=k/A>1/3\),
\[
\frac{\delta}{1-\delta}\ge\sqrt{\frac{k-A/3}{2A}}
=\sqrt{\frac{p-1/3}{2}}.
\]
Hence any LeBrun blow-up family with \(k/A\ge1/3+\eta\) has a uniform positive lower bound for both positive- and negative-normalized Ricci pinching (subject to the relevant sign being compatible with other obstructions). In particular, these integral-obstruction no-Einstein examples cannot yield a fixed-margin \(\delta_-\to0\) refutation of Yau26.

The only surviving LeBrun-type slot visible to this theorem is a sequence with \(k/A\to1/3^+\) (including integer-edge cases \(k=\lceil A/3\rceil\)) where the margin \(L_+-T_+\to0\). Such a sequence still needs an actual construction of tightly negatively Ricci-pinched metrics and must also respect the exact all-sign no-Einstein status.

## Research meaning

A counterexample to the full Yau26 proposition in dimension four cannot be obtained from a known Seiberg--Witten/Chern--Weil obstruction at fixed positive margin plus an arbitrarily tight Ricci-pinched input, because the obstruction itself gives a pinching gap. A viable refutation must either approach the zero-margin boundary of such inequalities or use an Einstein obstruction genuinely discontinuous at \(\mathring r=0\) (for example one based on exact holonomy/classification/rigidity rather than a curvature integral inequality valid for all metrics).


## Step 4 addendum: endpoint and scope cautions

Agent4/Preceptor checked this note against the Step 3 TTCS verifier and the regenerated script. The stable obstruction formula remains correct in its stated small-pinching regime, but later use should observe the following details.

1. In the scalar-only LeBrun 1996 threshold, the endpoint `p=k/A=2/3` is contradictory because the scalar curvature estimate used there is strict for blow-ups; do not use the older script flag that treated the formal zero coefficient as non-contradictory. The repaired script is `Sessions/S0910A02/workspace/scripts/step3_corrected_lebrun_bounds.py` and the regenerated JSON is `Sessions/S0910A02/workspace/data/step3_corrected_lebrun_bounds.json`.
2. The displayed volume proof of the mixed pinching gap directly assumes `T_+=A-k>0`, hence `1/3<p<1` for the standard LeBrun blow-up family. If `b(delta)<=0`, then already `delta>=1/(1+sqrt(3))`, which is outside the tight-pinching window and stronger than the small-gap estimates being used.
3. The endpoint `p=1/3` in LeBrun's no-Einstein theorem uses equality/strictness analysis (almost-Kähler equality and Taubes area obstruction), not only the weak inequality `F_+>=2A/3`. Near this endpoint, the correct live question is quantitative near-equality under pointwise Ricci pinching, not another fixed-margin integral estimate.
4. The algebraic positive-normalized version is formally sign-blind, but for general-type blow-ups with nonzero monopole classes it is usually vacuous for `delta_+<1`, since positive pinching forces positive scalar/Ricci and is already incompatible with the monopole obstruction. This family therefore cannot defeat the positive branch required for a full `Q_4` refutation.
5. A successful negative-branch sequence near `p->1/3+` would not by itself refute the original Yau26 proposition; refutation in dimension four must also defeat `P_4^+`.

For the broader route review and the four-dimensional full-Weyl CGB accounting, see `Sessions/S0910A02/workspace/notes/step4_preceptor_energy_accounting_and_route_review.md`.
