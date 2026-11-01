# Step 106 — Independent reading of the cap-charge theorem and the exact D4-ALF candidate

Session S1003A02, Agent4, Execute. This note independently reads Step 105 and records binding repairs. Inputs: `step105_cusp_channel_restored_and_cap_charge_theorem.md`, Step-33 Theorem G, Dai–Wei, A01 Step-92 message #890, Chen–Chen, Foscolo, Franchetti, and Akbulut. Independent TTCS integrations: `trace/ttcs/results/step106_ttcs01_verifier1_integration.md` and `step106_ttcs01_verifier2_integration.md`.

## 1. Theorem 105.Q after independent reading

Let
\[
 C_+(g;D)=\frac1{2\pi^2}\int_D|W^+|^2+\frac1{96\pi^2}\int_Ds^2,
 \qquad \widehat P(g;D)=\frac1{8\pi^2}\int_D|\operatorname{Ric}^\circ|^2,
\]
and let \(T_+(D)=2\chi(D)+3\tau(D)\). Step-33 Theorem G is
\[
 C_+(g;D)=\widehat P(g;D)+T_+(D)-\mathcal Q_+(\partial D),
 \qquad \mathcal Q_+=2\mathcal E-3\mathcal H.
\]
Orient every link \(L_{\ell,\rho}\) outward from the Einstein exhaustion \(\Omega_\rho\). It has the opposite orientation in the boundary of the cap. At fixed \(\rho\), local \(C^2\) convergence on the collar and \(\widehat P(g_i)\to0\) give
\[
 a_j(\rho):=\lim_i C_+(g_i;C_j^{(\rho)})
 =T_+(C_j)+\sum_{\ell\in J_j}\mathcal Q_+(L_{\ell,\rho};g_\infty). \tag{106.1}
\]
The eta term is continuous under smooth boundary-metric variation: the odd-signature kernel dimension is topological, and its variation formula has no spectral-flow jump here.

The existence of the limiting cap charge does not require a separate eta-limit theorem. Choose a nested exhaustion with compatibly labelled caps. Since the \(C_+\)-density is nonnegative, \(a_j(\rho)\) is monotone as the cap shrinks and is bounded by \(A-k\). Thus
\[
 c_j:=\lim_{\rho\to0}a_j(\rho)\ge0 \tag{106.2}
\]
exists. What follows from (E) without further end structure is convergence of the **sum**
\[
 q_j^\infty:=\lim_{\rho\to0}\sum_{\ell\in J_j}\mathcal Q_+(L_{\ell,\rho};g_\infty),
 \qquad c_j=T_+(C_j)+q_j^\infty. \tag{106.3}
\]
Individual end charges require separate asymptotics or stable one-ended collars. For a product-topology Einstein annulus, Theorem G and finite curvature energy give individual convergence, but this must be stated rather than inferred from (E) alone.

The scalar-cap proof needs the total tail volume, not equality for each cap. From total-volume convergence,
\[
 \sum_j\operatorname{Vol}_{g_i}(C_j^{(\rho)})
 \longrightarrow \operatorname{Vol}_{g_\infty}(\Omega\setminus\Omega_\rho).
\]
Hence each cap volume has limsup bounded by the right side, which tends to zero. Therefore
\[
 \lim_{\rho\to0}\limsup_i\int_{C_j^{(\rho)}}s_i^2=0, \tag{106.4}
\]
and
\[
 \lim_{\rho\to0}\lim_i\frac1{2\pi^2}\int_{C_j^{(\rho)}}|W_i^+|^2=c_j \tag{106.5}
\]
in the corresponding limsup/liminf sense. Additivity at fixed \(\rho\), followed by monotone convergence, gives
\[
 \boxed{C_+(g_\infty;\Omega)=A-k-\sum_jc_j}. \tag{106.6}
\]
The same argument applies to \(C_-\).

The Step-105 statement that (E2) is what \(\mathscr D\to0\) gives at nonzero Einstein normalization is correct once the functional decomposition is displayed. Since
\[
 \mathscr D=\frac{4P+L_s}{R},
\]
\(\mathscr D\to0\) and normalization with \(R\) bounded above and away from zero give \(P\to0\) and \(L_s\to0\). Local convergence to a nonzero negative Einstein metric forces \(\bar s_i\to s_\infty\), while total-volume convergence is an additional part of (E2), not a consequence of the scalar algebra alone. Extraction of (E1)/(E3) remains unproved.

## 2. Corollaries 105.L and 105.H

On a cap,
\[
 \int(s-\sqrt6|W^+|)^2\to 12\pi^2c_j. \tag{106.7}
\]
On \(\Omega\), with
\[
 x=\frac1{96\pi^2}\int_\Omega s^2,\qquad
 y=\frac1{2\pi^2}\int_\Omega|W^+|^2,
\]
we have \(x+y=A-k-c\), \(c=\sum c_j\), and
\[
 \int_\Omega(s-\sqrt6|W^+|)^2
 \le12\pi^2(\sqrt{8x}+\sqrt y)^2
 \le108\pi^2(A-k-c).
\]
Together with LeBrun's lower estimate this gives the verified formula
\[
 \boxed{9k+8c\le3A}. \tag{106.8}
\]
Thus a positive-charge cap is genuine \(W^+\)-concentration, not bounded-curvature collapse. The statement \(k+c\le2A/3\) needs the separate scalar estimate as written in Step 105; (106.8) itself already implies \(k+c\le3A/8\).

For a circle-fibred Dai–Wei end, the Step-33 eta convention is one half of Dai–Wei's signature eta, so
\[
 \mathcal H^\infty=\frac e3-\operatorname{sign}e,
 \qquad \mathcal Q_+^\infty=-e+3\operatorname{sign}e. \tag{106.9}
\]
For an \(S^3\)-Hopf cap with \(r\) negative classes,
\[
 c_+=4-r
\]
in the Taub-bolt chirality, while the other chirality gives \(-r\) and is impossible. If there are \(N\) exceptional caps with \(\sum r_j=k\) and \(B\) additional positive-charge ball caps, then the exact necessary condition is
\[
 \boxed{k+32N+32B\le3A}. \tag{106.10}
\]
The displayed equivalence \(k+32N\le3A\) in Step 105 assumes \(B=0\). Singleton caps give \(k\le A/11\). Four-class packing gives the smooth wall \(k\le A/3\). These are necessary conditions, not constructions.

A crucial correction is that the four-class cap is zero only in the \(C_+\) channel. For
\[
 C=\#4\overline{\mathbb{CP}}^{\,2}\setminus B^4,
 \qquad (\chi,\tau)=(5,-4),
\]
the admissible Hopf link has \((\mathcal Q_+,\mathcal Q_-)=(-2,2)\), hence
\[
 c_+=(-2)+(-2)=0,\qquad c_-=(22)+(-2)=20. \tag{106.11}
\]
Therefore
\[
 \boxed{\int_C|W^-|^2\longrightarrow40\pi^2}. \tag{106.12}
\]
The cap is invisible to the \(C_+\)/mixed-LeBrun mechanism, not to all aggregate curvature information and not to full energy. Step 105's phrases “no energy”, “zero-energy cap”, and “energy-free degeneration” are withdrawn wherever they refer to full curvature.

## 3. Scope of gravitational-instanton classification

A curvature-scale noncollapsed smooth limit of this cap is Ricci-flat and satisfies \(W^+=0\); if simply connected, it is hyperkähler. But hypotheses (E) alone do not supply a bubble tree, no-neck identity, noncollapse at selected scales, or an F-structure on the residual region.

Chen–Chen \cite{chen2016gravitational} classify complete hyperkähler four-manifolds under faster-than-quadratic curvature decay. Their end list includes ALE, ALF, ALG and ALH. Their ALF theorems identify only the ALF \(A_k\) and \(D_k\) members. Finite \(L^2\) curvature by itself does not place every bubble in this class. Therefore neither “all bubbles are ALE/ALF” nor a finite exhaustive assembly follows from Step 105.

## 4. The exact D4-ALF architecture

Despite that scope correction, one candidate matches every presently computable datum.

### 4.1 D4 topology and end

For the ALF space indexed by the rank-four root lattice, Foscolo and Franchetti give
\[
 H_2(N;\mathbb Z)\cong D_4,\qquad Q_N=-D_4,
 \qquad (\chi(N),\tau(N))=(5,-4).
\]
For rank \(K\ge3\), Franchetti identifies the large link as
\[
 S^3/D_{K-2}^*.
\]
At \(K=4\), \(D_2^*=Q_8\), so the end is
\[
 \boxed{L_D=S^3/Q_8}. \tag{106.13}
\]
This corrects the common indexing ambiguity: the order-sixteen binary-dihedral group is not the end of the rank-four \(D_4\) instanton.

The hyperkähler orientation has \(W^+=0\). The chiral identities then force its ALF link charges to be
\[
 \boxed{(\mathcal Q_+,\mathcal Q_-)(L_D)=(-2,2)}. \tag{106.14}
\]
Indeed \(C_+(N)=0\), while \(C_-(N)=20\). Thus the D4 ALF end has exactly the same charge pair as the desired Hopf-collapsed outer \(S^3\), even though the links are topologically different.

### 4.2 Index-two parity extension

Inside the odd diagonal lattice,
\[
 D_4=\{x\in\mathbb Z^4:\sum_i x_i\equiv0\pmod2\}\subset I_4,
 \qquad [I_4:D_4]=2,\quad\det D_4=4. \tag{106.15}
\]
Akbulut's rational ball \(W\), the real rank-two disk bundle over \(\mathbb{RP}^2\), has boundary \(S^3/Q_8\), retracts to \(\mathbb{RP}^2\), and satisfies
\[
 H_1(W)=\mathbb Z_2,\quad H_2(W)=0,
 \quad \chi(W)=1,\quad\tau(W)=0.
\]
Remove an interior ball and orient the result as a cobordism \(Z\) from \(S^3/Q_8\) to \(S^3\). Then
\[
 \chi(Z)=\tau(Z)=0,
 \quad H_1(Z)=\mathbb Z_2,
 \quad H_2(Z)=0. \tag{106.16}
\]
Mayer–Vietoris and van Kampen for \(N\cup Z\) show that the rank-four lattice is enlarged by the order-two kernel
\[
 \ker\big(H_1(S^3/Q_8)=(\mathbb Z_2)^2\to H_1(Z)=\mathbb Z_2\big),
\]
producing the index-two unimodular odd overlattice \(-I_4\). This is the precise meaning of the parity passage. A generic \(w_2\) argument does not exclude it; the characteristic vector \((1,1,1,1)\) already lies in \(D_4\). What the transition carries is the global odd integral extension and nontrivial \(w_2\), not a characteristic homology vector lying outside the D4 core.

### 4.3 Charge equation for the transition

For a cobordism with outer and inner link charges, Theorem G gives
\[
 \widehat P(Z)=C_\pm(Z)-(2\chi\pm3\tau)(Z)
 +\mathcal Q_\pm(L_{\rm out})-\mathcal Q_\pm(L_{\rm in}). \tag{106.17}
\]
Here \(\chi(Z)=\tau(Z)=0\) and both link-charge pairs are \((-2,2)\). Therefore the charge equations impose
\[
 \widehat P(Z)=C_+(Z)=C_-(Z) \tag{106.18}
\]
in the limiting collar geometry. They permit a bounded-curvature collapsing transition with vanishing full curvature energy. They do not produce one.

An ALE D4 core is different. Its Euler transgression is \(1/8\), giving
\[
 (\mathcal Q_+,\mathcal Q_-)_{\rm ALE}=(-2,5/2).
\]
A transition with \(\chi=\tau=0\) to Hopf \(S^3\) must then carry \(C_-\to1/2\). Thus the genuinely charge-matched candidate is ALF D4, not ALE D4.

### 4.4 What is and is not established

The present result is a **matched architecture**:
\[
 \boxed{\text{rank-four D4 ALF core }+\bigl(W\setminus B^4\bigr)}. \tag{106.19}
\]
It has the correct rank, index-two odd extension, boundaries, \(\chi\), \(\tau\), and both chiral charge ledgers. It is not yet a construction of the four-class cap because two facts are missing:

1. an explicit smooth identification
\[
 N_{D4}\cup_{S^3/Q_8}(W\setminus B^4)
 \cong \#4\overline{\mathbb{CP}}^{\,2}\setminus B^4;
\]
the lattice and fundamental group do not determine the relative smooth type;
2. a metric family on \(W\setminus B^4\) matching the D4-ALF collar to the Hopf-collapsed \(S^3\) collar with
\[
 \int_Z|\operatorname{Rm}|^2\to0.
\]
Akbulut's Cappell–Shaneson cobordism is from \(S^3/Q_8\) to itself, not this metric transition. Foscolo's K3 construction proves that ALF bubbles can coexist with bounded-curvature collapse, but not this non-spin relative cobordism and outer Hopf geometry.

Conversely, no available charge, parity, or classification result excludes (106.19). Conditional on an extracted decomposition into disjoint simply connected ALF A/D blocks carrying all four rational classes and a full-energy-vanishing residual region, determinant and \(C_-\)-energy accounting force a single D4 block: \(\det A_4=5\) is not a square, whereas \(\det D_4=4\). Those decomposition hypotheses are not supplied by (E).

## 5. Consequence for the Einstein-gap problem

The Step-105 charge principle survives independent reading after scope repair:
\[
 \boxed{9k+8\sum c_j\le3A}.
\]
The relevant invisibility is chiral: zero \(C_+\)-charge regions evade the scalar/\(W^+\) machinery even while carrying opposite-chiral curvature. The third nonattained-zero subchannel is now as concrete as present evidence permits:

- positive-charge Hopf caps are quantitatively restricted (singletons above \(A/11\));
- the first invisible Hopf cap carries exactly four exceptional classes;
- its unique natural rank-four model is the matched D4-ALF/rational-ball-cobordism architecture (106.19);
- existence reduces to relative smooth identification plus a collapsing metric transition; exclusion requires a new invariant or a theorem forbidding that transition.

The original fixed-topology centre remains unresolved. This Step replaces an invalid generic spin obstruction with a precise construction/exclusion object.