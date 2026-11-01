# TTCS Independent Branch Record

```json
{
  "step_id": 93,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step74_orbifold_transfer_theorem.md",
    "Sessions/S1003A01/workspace/scripts/step74_neck_and_screen.py",
    "Sessions/S1003A01/workspace/data/step74/neck_and_screen.json",
    "Sessions/S1003A02/workspace/notes/step55_k1_orbifold_gate_charges_lattices_collapse.md",
    "Sessions/S1003A02/workspace/notes/theorem_package_v1.md",
    "Sessions/S1003A02/workspace/notes/state_of_problems_1_4.md"
  ]
}
```

## Task

Independently verify A01 Step-74 Theorems 74.B–D and assess the equality/attainment question for V_m. Check the mixed inequality transfer including bubble chirality and charge conventions, the Einstein-bulk optimization and asymptotic linear form, the Kähler Ricci-flat filler budget, and the screening interpretation. Then determine what, if anything, follows rigorously from W^-=0, constant s<0, |W^+|^2=s^2/24, P=8pi^2 k for an alpha_orb minimizer: does existing Derdzinski/LeBrun equality theory force a Kähler or almost-Kähler orbifold structure, and is such a structure topologically excluded on V_m? Distinguish a theorem from a plausible route and identify any exact source theorem needed.

## Output

# Verification memo: A01 Step 74 (Theorems 74.A–D, screening) and the attainment question on \(V_m\)

## 0. Summary

1. **Conventions and charges.** Everything rechecks: \(T_\pm\), the additivity (0.1), \(I_\pm(N)=-2\pi^2c_\pm(N)\) for Ricci-flat fillers, and the Kähler charges (0.2) (EH \((0,-6)\), \(A_3\) \((0,-15)\), \(A_6\) \((0,-192/7)\)).
2. **Theorem 74.A.** The lower bound, the Green football cap and the limiting values are correct.
3. **Attainment on \(V_m\) is now decided.** The infimum \(\inf P=8\pi^2k\) over orbifold metrics on \(V_m\) is never attained, and \(\alpha_{\rm orb}(V_m)\) is not attained for \(k<A/3\). The proof is a two-line Euler–Lagrange argument (§2). It needs neither Derdzinski nor LeBrun's equality theory. The case \(k=A/3\) reduces exactly to the existence of a half-conformally-flat orbifold conformal class on \(V_{A/6}\).
4. **Theorems 74.B and 74.C, and the expansion (3.2).** These are correct. I rederived the \(1/A\) correction \(-3(e-3d)^2/(4A)\) independently.
5. **Corollary 74.D.** The closed form \(x_{\min}\) and the budget are correct.
6. **Screening.** The pipeline is correct but needs three refinements, all rigorous or close to it (§5):
   - a lattice test removes most single-Kronheimer "survivors";
   - several rational-ball rows labelled "charge rows only" are actually realized Ricci-flat fillers in reversed orientation;
   - the \(b_2=1\) survivors would require a non-Kähler Ricci-flat ALE metric.
7. **Kähler and almost-Kähler structures.** Both are topologically excluded on \(V_m\) in the orientation of \(X\), by a parity (Wu) argument. However, the equality data do not force either structure; that implication is unproved, and it is also unnecessary.

## 1. Conventions and Theorem 74.A

**Gauss–Bonnet and signature.** These give \(8\pi^2T_\pm=4I_\pm+S/12-P\).
- For an Einstein metric: \(I_\pm=2\pi^2(T_\pm-x)\), \(x=S/96\pi^2\). ✓
- For a Ricci-flat filler: \(I_\pm=-2\pi^2c_\pm\). ✓
- In the Kähler case \(c_+=0\). Then \(3\tau+3\eta=2/|\Gamma|-2\chi\), so \(c_-=-4(\chi-1/|\Gamma|)\). ✓

**Orientation matching.** Kronheimer spaces in their complex orientation have intersection form \(-\)Cartan, consistent with \(\operatorname{span}E_i\cong-I_k\). ✓

**Topological numbers of \(V_m\).** \(\chi_{\rm orb}=A/3-m\), \(\tau_{\rm orb}=A/9\). Hence
- \(T_+=A-k\), consistent with \(C_+=0\);
- \(T_-=A/3-k\), consistent with \(C_-=-6k\). ✓

**Exact identity.** Since \(W-12\pi^2\tau_{\rm orb}=2I_-\), we have \(w=2I_-\), and the lower-bound computation becomes
\[
P=8\pi^2k+\frac{S-32\pi^2A}{12}+4I_-,\qquad R=8\pi^2(A+k)+\frac{\sigma}{3}+4I_- .
\]
The weighted-mean argument for \(\mathscr D\ge4P/R\ge\min\{1,4k/(A+k)\}\) is correct.

**Green cap.** I checked each ingredient:
- \(u=1+r^{-2}\) is harmonic on \(\mathbb R^4\setminus0\), so \(s_h=-6u^{-3}\Delta u=0\).
- \(h\) is conformally flat.
- \(\iota\) is an orientation-preserving involutive isometry of \(h\). Inversion pulls \((1+r^2)^2r^{-4}\delta\) back to \(h\).
- Its fixed points are \(|x|=1\), \(\sigma x=x\), i.e. \(\pm e_4\). The differential there is \(\sigma(I-2e_4e_4^T)=-I\).
- Noncompact Gauss–Bonnet gives \(P(h)=32\pi^2\) (two AE ends, \(\chi=0\)) and \(P(G)=16\pi^2\).
- In the gluing, \(\varepsilon^2h=(1+\varepsilon^2/|y|^2)^2\delta_y\). With \(\rho=\varepsilon^{1/2}\), the tail is \(O((\varepsilon/\rho)^4)=O(\varepsilon^2)\).
- \(L_s\to0\), since \(s\) is constant outside and the caps have vanishing volume.
- Therefore \(\mathscr D\to4k/(A+k)\). ✓

**Supply hypothesis (SW).** Convexity over the sign classes gives \(\max(a^+)^2\ge(c_1^+)^2=A+|c_1^-|^2\ge A\). This is correct for \(b^+\ge2\).
- The package (§24.0) records that LeBrun's scalar estimate holds for all \(b^+\) by the polarization remark in \cite{lebrun2001ricci}. The scalar part \(S\ge32\pi^2A\) therefore also covers fake projective planes.
- The mixed estimate of LeBrun Prop. 3.8 (Knowledge object l. 299–301) must be read for its \(b^+=1\) statement before fake projective planes are included in 74.B–D.

## 2. Nonattainment on \(V_m\) (new; rigorous under (SW)+(R))

**Theorem.** Assume (SW) and (R). Then:
- (i) \(\inf_{\mathscr G_{\rm orb}(V_m)}P=8\pi^2k\) is attained for no \(m\ge1\);
- (ii) \(\inf_{\mathscr G_{\rm orb}(V_m)}\int s^2=32\pi^2A\) is not attained;
- (iii) for \(k=2m<A/3\), \(\alpha_{\rm orb}(V_m)=4k/(A+k)\) is not attained.

**Proof.**
1. Let \(g\) attain \(P=8\pi^2k\). The identity above forces \(S=32\pi^2A\) and \(I_-=0\).
2. Since \(S\ge32\pi^2A\) and \(I_-\ge0\) hold for every orbifold metric, \(g\) simultaneously minimizes \(\int s^2\) and \(I_-\).
3. For variations supported in the regular part, \(T_-^{\rm orb}\) is invariant.
4. A nonnegative functional that is quadratic in \(W^-\) has vanishing first variation where \(W^-\equiv0\). Hence \(g\) is a critical point of \(\int s^2\).
5. In dimension four the gradient of \(\int s^2\,d\mu\) is \(2\nabla^2s-2(\Delta s)g-2s\operatorname{Ric}+\tfrac12s^2g\). Its trace gives \(\Delta s=0\), so \(s\) is constant on the compact orbifold (\(s\) is continuous across cone points).
6. With \(s\) constant the gradient reduces to \(-2s\operatorname{Ric}^\circ=0\).
7. \(S>0\) gives \(s\neq0\). Hence \(g\) is Einstein and \(P=0<8\pi^2k\), a contradiction.

For (ii), the same argument applies to an \(S\)-minimizer, because \(P\ge8\pi^2k\) forbids an Einstein outcome. For (iii), an attaining metric at \(k<A/3\) has \(P=8\pi^2k=\inf P\) and is excluded by (i). ∎

**Equivalent formulation.** For \(W^-=0\), the Bach tensor (expressible through either \(W^\pm\)) vanishes. The \(P\)-gradient \(=-8B-s\operatorname{Ric}^\circ/6\) then forces \(s\operatorname{Ric}^\circ=0\).

**Effect on the Step-74 text.** The "equality structure" paragraph of 74.A (\(W^-=0\), \(s\le0\), \(|W^+|^2=s^2/24\), \(P=8\pi^2k\)) describes an empty set. Its correct use is quantitative: near-minimizers have \(\sigma,I_-\to0\), and therefore the \(L^1\)-approximate versions of those pointwise relations.

**The value \(k=A/3\) (\(m=A/6\), requires \(\chi(\mathcal O_X)\) even).** Here \(2\chi_{\rm orb}=3\tau_{\rm orb}\), and
\[
\mathscr D-1=\frac{12I_-+L_s}{R}.
\]
So \(\alpha_{\rm orb}=1\) is attained **iff** \(V_{A/6}\) carries an orbifold metric with \(W^-\equiv0\) (complex orientation) and constant \(s\).
- Every orbifold metric has \(\|s^-\|_2^2\ge32\pi^2A\) by transfer. The conformal class therefore has \(Y<0\), the orbifold Yamabe problem is solvable, and \(s<0\) is automatic.
- Equivalently: attainment iff there is an anti-self-dual orbifold conformal structure on \(\overline{V_{A/6}}\).
- Such a metric is not \(P\)-critical (its gradient is \(-s\operatorname{Ric}^\circ/6\neq0\)), so §2 does not apply. This case remains open.
- A plausible route is Donaldson–Friedman / Kovalev–Singer orbifold gluing of the ball-quotient class (\(W^-=0\)) with round \(S^4/\mathbb Z_2\). The \(\mathbb Z_2\)-invariant \(H^2\) of \(S^4\) vanishes.
- The missing datum is \(H^2\) of the \(W^-=0\) deformation complex of the compact ball quotient. A source for this is needed.

## 3. Theorem 74.B

**Expansion and gluing.** The expansion \(\int(s-\sqrt6|W^+|)^2=S-2\sqrt6\int s|W^+|+6I_+\) is correct, and so is the region-by-region limit.
- In the scaled filler \(s=0\), so the integrand is \(6|W^+|^2\to6\int_N|W^+|^2\).
- On the annulus, \(|\mathrm{Rm}|\lesssim\rho^{-2}[\rho^2+(\varepsilon/\rho)^\tau]=O(1)\) at \(\rho=\varepsilon^{\tau/(\tau+2)}\). For EH, \(\varepsilon^4/\rho^6=1\). The volume is \(O(\rho^4)\).
- Applying Prop. 3.8 separately to each \(g_\varepsilon\), with its own monopole class, is legitimate. No convergence of classes is needed, because only the numerical lower bound \(72\pi^2A\) is used.

**Bubble ledger.** \(B_+=-2\pi^2C_+\) for Ricci-flat fillers and \(B_+=P(N)/4-2\pi^2c_+\) for scalar-flat fillers. Both are correct.

**Orientation.** "Bubble chirality" means \(\int_N|W^+|^2\) computed in \(M\)'s orientation. For Kähler fillers glued in complex orientation it vanishes. For a T-type ball glued in reversed orientation it equals \(8\pi^2(1-1/n^2)\) (see §5b).

**Hypotheses actually used.** (SW) on \(M_k\), (R) for the given fillers, and derivative-controlled decay.

## 4. Theorem 74.C, (3.1), (3.2) and Corollary 74.D

**Constraints.** For an Einstein bulk:
- \(x\ge A/3\) (scalar transfer);
- \(x\le T_\pm\) (from \(I_\pm\ge0\));
- Minkowski gives \(12\pi^2[\sqrt{8x}+\sqrt{T_+-x}]^2\ge72\pi^2A+12\pi^2C_+\), which is (3.1).

**Optimization.** \(f^2=7x+T_++2\sqrt8\sqrt{x(T_+-x)}\) is concave and maximal at \(x=8T_+/9\) with value \(9T_+\). Clipping to the interval is therefore exact.

**Large-\(A\) expansion.** Put \(d=C_-+5k\), \(e=C_+-k\), and evaluate at \(x=T_-\). I obtain
\[
f^2-6A-C_+=9C_-+2C_++42k+\frac{6d(e-d)-\tfrac34(e+d)^2}{A}+O(A^{-2}),
\]
and \(6d(e-d)-\tfrac34(e+d)^2=-\tfrac34(e-3d)^2\). This matches (3.2). Numerical check for \(A_5\), \(k=5\): \(e-3d=-10\) gives \(-75/A\), i.e. \(-8.3\times10^{-4}\) at \(A=90000\), matching the JSON.

**Corollary 74.D.** Solving \(\sqrt{8u}+\sqrt{1-h-u}=\sqrt6\) gives \((9/8)a^2-2\sqrt6a+5+h=0\), \(a=\sqrt{8u}\), whence
\[
u=\tfrac1{27}\bigl(4\pm\sqrt{1-3h}\bigr)^2 .
\]
The smaller root is \(x_{\min}\). The identity \(x_{\min}-(A+k)/3=\frac{4A}{27}(1-t)^2\) checks. Together these give \(C_->-14k/3\), the budget \(7k/6-k^2/(12A)+\dots\), and the value \(1.15544\) at \((9,1)\). ✓

**Reading of the budget.** \(r>6(1-1/|\Gamma|)\) excludes \(A_1\)–\(A_5\), \(D_4\), \(D_5\) (\(A_5\) at equality) and admits \(A_{\ge6}\), \(D_{\ge6}\), \(E_r\). This is consistent with the table.

## 5. Screening interpretation: three refinements

**(a) Lattice test for Kronheimer fillers (rigorous).**
- \(X\) is aspherical and \(N\) is simply connected, so \(H_2(N)\to H_2(X)\) is zero (the cyclic-image lemma, 55.8; no SW\(_L\) needed). Thus \(H_2(N)\), with form \(-\)Cartan, embeds isometrically into \(\operatorname{span}E_i\cong-I_k\).
- Root vectors go to norm-2 vectors of \(\mathbb Z^k\), which form the \(D_k\) root system. By Dynkin's classification, the root subsystems of \(D_k\) are sums of \(A\)- and \(D\)-types, and \(A_r\subset D_k\) needs \(k\ge r+1\) except \(A_3=D_3\).
- Consequences:
  - \(E_6,E_7,E_8\) fillers never occur in any \(M_k\). For \(E_8\) a direct proof: unimodular \(E_8\subset\mathbb Z^k\) splits, \(\mathbb Z^k=E_8\oplus L\), so the number of norm-1 vectors would be at most \(2(k-8)<2k\).
  - \(A_n\) for \(n\ge4\) cannot carry exactly \(k=n\) classes.
- The single-filler, \(k=\)rank survivors are therefore reduced to \(D_n\), \(n\ge6\): \(D_6\) from \(A\ge90\), \(D_7\) from \(A\ge36\).
- The rows \(A_6\)–\(A_{10}\), \(E_6\)–\(E_8\) at \(k=\)rank, and \(E_8\) at every \(k\), are removed.
- \(D_n\subset\mathbb Z^n\) has index 2. This is compatible with \(\mathbb Z_2\)-torsion in \(H_1(V^\circ)\), as in the paired-\(A_1\) case.

**(b) Reversed-orientation T-type rows are realized fillers.** The rows \((c_+,c_-)=(-4(1-1/n^2),0)\), namely \(L(4,3)\), \(L(9,4)\), \(L(9,7)\), \(L(16,5)\), \(L(16,13)\), \(L(25,6)\), …, with \(q\equiv-(na-1)\), are the Şuvaina–Wahl Ricci-flat Kähler metrics with orientation reversed. They are not mere charge rows.
- Example: \(\bar B_2\) with bulk \(V=X\#\overline{\mathbb P}(1,1,4)\), a configuration already present in A02 §4.
- In \(M\)'s orientation the cone group \((i,i)\) becomes \((i,-i)\subset SU(2)\).
- These rows pass both tests from \(A\ge18\), with linear form \(42-8(1-1/n^2)\). They are the most concrete open Einstein-bulk candidates in the catalogue at \(k=1\).
- The rows with both charges nonzero (e.g. \((16,7)\), \((25,7)\)) would need a rational-ball Ricci-flat ALE metric that is Kähler in neither orientation. By the Şuvaina/Wright classification, Kähler Ricci-flat rational balls are T-type only (sources to register).

**(c) The \(b_2=1\) survivors.** This covers the 8 cyclic rows, e.g. \(L(49,23)\), and the \(D_5\)–\(E_8\) end rows.
- A simply connected Ricci-flat Kähler ALE surface has trivial canonical bundle and is hyperkähler, hence Kronheimer with \(b_2=\)rank and an \(SU(2)\) end.
- \(b_2=1\) then forces EH, whose end group has order \(2\), not a square.
- So every \(b_2=1\) survivor requires a simply connected non-Kähler Ricci-flat ALE metric. None is known; this is the Bando–Kasue–Nakajima question.
- For \(SU(2)\) ends, an exact source (Nakajima-type: Ricci-flat ALE with \(\Gamma\subset SU(2)\) is hyperkähler, under the source's hypotheses) would remove the ADE-end rows outright.

## 6. Does equality theory force a Kähler or almost-Kähler structure?

**Not as a theorem.**
- *Derdzinski (Compositio 1983).* The conclusion "\(|W^+|^{2/3}g\) Kähler" needs \(\delta W^+=0\) and degenerate spectrum of \(W^+\).
  - With \(W^-=0\) and \(s\) constant, \(\delta W^+\) is the Cotton tensor of \(\operatorname{Ric}^\circ\). This vanishes only if \(\operatorname{Ric}^\circ\) is Codazzi, which is not implied.
  - The equality chain fixes only \(|W^+|=|s|/\sqrt{24}\), not the spectrum of \(W^+\).
- *LeBrun's equality case.* Kähler metrics with constant \(s<0\) give \(\int(s-\sqrt6|W^+|)^2=\tfrac94S=72\pi^2(c_1^+)^2\), so they are the expected equality class. But the rigidity proof uses an actual monopole solution (\(\nabla\Phi=0\)), and \(V_m\) has none; 74.B was designed to avoid orbifold SW theory.
- *A limiting route.* Monopoles for \(g_\varepsilon\) satisfy \(|\Phi|^2\le\max(-s)\), and \(\int_{\rm fillers}|F_A^+|^2\to0\). Compactness on the regular part plus removable singularities would yield an orbifold solution on which LeBrun's chain becomes equality. This is plausible but unproved; it needs a precise orbifold removable-singularity statement.

**Topological exclusion (rigorous).** \(V_m\), in the orientation of \(X\), carries no orbifold almost-complex structure inducing that orientation, hence no Kähler or almost-Kähler orbifold structure.
1. \(-I\) commutes with every \(J\), so each \(A_1\) germ is \(\mathbb C^2/\pm1\). The structure is equivariantly homotopic to the standard one near the point.
2. Resolve by EH with its complex structure. The result is an almost-complex structure \(J'\) on a manifold diffeomorphic to \(M_{2m}\), by (R).
3. Since \(c_1(\mathrm{EH})=0\), \(c_1(J')\cdot C_j=0\) on the core spheres.
4. Lemma 52.6 gives \(E_{2j-1}=\tfrac12(C_{2j-1}+C_{2j})\) rationally, so \(c_1(J')\cdot E_i=0\).
5. But \(c_1(J')\) is characteristic, so \(c_1\cdot E_i\equiv E_i^2=-1\pmod2\). Contradiction.

This strengthens the parity lemma 52.9(v) to the almost-complex category. It is moot for attainment at \(k<A/3\) (§2). For the \(k=A/3\) problem it shows that any \(W^-=0\) minimizer is non-almost-Kähler.

## 7. Exact sources needed

| Input | Where it enters |
|---|---|
| LeBrun Prop. 3.8 (convex-geometry paper): statement, \(b^+=1\) form, equality case | 74.B–D for fake projective planes |
| Gradient of \(\int s^2\) in dimension 4; Bach via \(W^\pm\) (Besse, *Einstein Manifolds*, Ch. 4) | Theorem in §2 |
| Dynkin's classification of root subsystems of \(D_n\) | §5a |
| Şuvaina 2012 / Wright 2012 classification of Ricci-flat Kähler ALE quotients | §5b |
| Nakajima-type hyperkähler criterion for \(SU(2)\) ends | §5c |
| \(H^2\) of the \(W^-=0\) deformation complex of compact ball quotients, plus an orbifold Donaldson–Friedman theorem | \(k=A/3\) attainment |

Theorem 87.O's statement "Einstein \(V_m\) requires \(2m<A/3\)" (no SW input) is superseded by 74.A(1), which under (SW)+(R) excludes Einstein orbifold metrics on \(V_m\) for every \(m\).