# Step 74 — Curvature transfer through Ricci-flat resolution: the exact paired-A1 law and the Einstein-bulk budget

Agent2, Execute. Inputs: Step 73, Spirit #81–#82 (`spirit_step72_orbifold_scalar_transfer.md`,
`spirit_step73_mixed_curvature_transfer.md`), A02 Lemma 86.S / 86.S′ / Theorem 87.O
(`S1003A02/workspace/notes/theorem_package_v1.md` lines 741–750, 1294–1300), A02 Step-55 charges
(eq. (1.1) of `step55_k1_orbifold_gate_charges_lattices_collapse.md`), LeBrun Prop. 3.8
\cite{lebrun2023four} (Knowledge object `Four-Manifolds-Curvature-Bounds-and-Convex-Geometry`, l. 299–301),
Ju–Viaclovsky \cite{ju2023conformally}, Viaclovsky \cite{viaclovsky2010monopole}, Ishida–LeBrun \cite{ishida2003curvature}.
Computation: `workspace/scripts/step74_neck_and_screen.py` → `workspace/data/step74/neck_and_screen.json`.

## 0. Conventions

$X$ compact complex-hyperbolic surface in its complex orientation, $A=c_1^2(X)\in9\mathbb Z_{>0}$,
$\chi(X)=A/3$, $\tau(X)=A/9$. $M_k=X\#k\overline{\mathbb{CP}}^2$, $\mathcal Y(M_k)=-4\pi\sqrt{2A}$.
$P=\int|\operatorname{Ric}^\circ|^2$, $S=\int s^2$, $I_\pm=\int|W^\pm|^2$, $W=I_++I_-$, $R=\int|\operatorname{Ric}|^2=P+S/4$,
$\mathscr D=E=(4P+L_s)/R$ with $L_s=\int(s-\bar s)^2$. On a compact orbifold with isolated singularities
$$
16\pi^2\chi_{\rm orb}=\tfrac{S}{12}+2W-P,\qquad 12\pi^2\tau_{\rm orb}=I_+-I_-,
$$
$\chi_{\rm orb}$ the Satake Euler characteristic and $\tau_{\rm orb}$ including the APS $\eta$ link terms.
Put $T_\pm=2\chi_{\rm orb}\pm3\tau_{\rm orb}$. For an ALE filler $N$ (oriented by $M$) A02's charges are
$c_\pm(N)=2/|\Gamma|-2\chi(N)\mp3\tau(N)\mp3\eta_\Gamma$, so that $P(N)=4I_\pm(N)+S(N)/12+8\pi^2c_\pm(N)$.
If an orbifold $V$ is resolved by fillers $N_j$ to $M_k$, additivity of $\chi$ and of $\tau$ (Novikov + APS) gives
$$
T_+(V)=A-k+C_+,\qquad T_-(V)=\tfrac A3+5k+C_-,\qquad C_\pm=\textstyle\sum_jc_\pm(N_j).\tag{0.1}
$$
For a Ricci-flat filler, $I_\pm(N)=-2\pi^2c_\pm(N)$, so both $c_\pm\le0$. For a Ricci-flat **Kähler** filler in its
complex orientation $W^+=0$, hence
$$
c_+=0,\qquad c_-=-4\big(\chi(N)-1/|\Gamma|\big).\tag{0.2}
$$
(Checks: EH $(0,-6)$, $A_3$ $(0,-15)$, $A_6$ $(0,-192/7)$, T-type Milnor fibres $(0,-4(1-1/n))$, all agreeing with A02's exact table.)

**Metricwise curvature supply.** LeBrun's Yamabe theorem for general-type blow-ups gives, for every smooth metric on $M_k$,
$\int(s^-)^2\ge32\pi^2A$ and hence $S\ge32\pi^2A$, including when $b^+=1$. For the mixed estimate, LeBrun's polarized
Proposition 3.2 selects, for the current polarization $H=H_g^+$, exceptional signs such that
$a_H=c_1(X)-\sum E_j$ has a nonzero small-perturbation invariant and $(a_H^+)^2\ge A$. The selected class may depend on
$H$ but stays fixed through the conformal argument. Theorem 2.3 then gives
$\int(s-\sqrt6|W^+|)^2\ge72\pi^2A$. Since $c_1(X)^2=A>0$ prevents a polarization wall, fake projective planes are included;
there is no residual $A=9$ exception. See `step75_review_nonattainment_and_root_restriction.md` §1.

---

## 1. Theorem 74.A (exact paired-A1 orbifold law)

Let $V_m=X\#m(S^4/\mathbb Z_2)$, $k=2m\ge2$, and let $\mathscr G_{\rm orb}(V_m)$ be all smooth orbifold metrics.
Use the metricwise curvature supply above.

**Topological input (R).** The orientation-matched resolution of the two $A_1$ points of $O=S^4/\mathbb Z_2$ by
complex-oriented Eguchi–Hanson spaces is diffeomorphic to $\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2$, so the resolution of $V_m$ is
$M_{2m}$. *Proof.* Write $S^4=\{(t,w)\in\mathbb R\times\mathbb C^2:t^2+|w|^2=1\}$ with involution $w\mapsto-w$; the
standard $T^2$ action rotating $w_1,w_2$ commutes with it, and $-1=(\pi,\pi)\in T^2$. The resolution $N$ is obtained by
replacing the two cone neighbourhoods of the poles by complex-oriented $T^*S^2=\mathcal O(-2)$, i.e. by the toric
resolution of $\mathbb C^2/\pm1$; Eguchi–Hanson is $U(2)$-invariant, so the gluing is $T^2/\mathbb Z_2$-equivariant. Thus $N$
carries a smooth effective $T^2$ action whose orbit space is a disk with four edges. Van Kampen ($\pi_1(\mathcal O(-2))=1$)
gives $\pi_1(N)=1$; Mayer–Vietoris shows $H_2(N)$ contains the two disjoint $(-2)$-spheres with index $2$, so the form is the
unique rank-two negative-definite unimodular lattice $-I_2$. By the Orlik–Raymond classification of simply connected
$T^2$-four-manifolds (equivariant connected sums of $S^4,\pm\mathbb{CP}^2,S^2\times S^2$), $N\cong\overline{\mathbb{CP}}^2\#\overline{\mathbb{CP}}^2$
(the only such sum with form $-I_2$). Connected sum at regular points then gives $M_{2m}$. $\square$
A modern locator for the smooth/topological torus-action classification and the original Orlik–Raymond references is \cite{corro2022torus}; the explicit smooth weighted-orbit data and the role of the smooth classification are recorded in `step75_review_nonattainment_and_root_restriction.md` §2. A bare lattice/Freedman argument would give only the homeomorphism type.

1. every $g$ has $S\ge32\pi^2A$, $P\ge8\pi^2k$, and $\mathscr D(g)\ge\min\{1,4k/(A+k)\}$; in particular **$V_m$ carries no
   Einstein orbifold metric for any $m\ge1$**;
2. $\inf_{\mathscr G_{\rm orb}(V_m)}P=8\pi^2k$ and $\alpha_{\rm orb}(V_m)=\min\{1,4k/(A+k)\}$.

**Proof of the lower bounds.** Lemma 86.S resolves every orbifold metric by $2m$ orientation-matched scaled
Eguchi–Hanson spaces to smooth metrics $g_\varepsilon$ on $M_k$ with $S(g_\varepsilon)\to S(g)$ and $P(g_\varepsilon)\to P(g)$
(the convergence of $S$ uses only $O(\rho^4)$ volume and bounded curvature on the annuli; no condition $R>0$). Hence
$S(g)\ge32\pi^2A$. Here $\chi_{\rm orb}=A/3-m$, $\tau_{\rm orb}=A/9$ (the $A_1$ $\eta$ term vanishes), so
$W\ge12\pi^2\tau_{\rm orb}=4\pi^2A/3$. With $\sigma=S-32\pi^2A\ge0$, $w=W-4\pi^2A/3\ge0$ Gauss–Bonnet gives
$$
P=8\pi^2k+\tfrac{\sigma}{12}+2w,\qquad R=8\pi^2(A+k)+\tfrac\sigma3+2w .
$$
So $4P/R$ is the weighted mean of $4k/(A+k)$, $1$, $4$ with weights $8\pi^2(A+k),\sigma/3,2w$, and $\mathscr D\ge4P/R$.
An Einstein metric would have $P=0<8\pi^2k$.

**Proof of the upper bounds (Green football cap).** On $\mathbb R^4\setminus0$ let
$h=(1+r^{-2})^2\delta$, the conformal-Laplacian Green blow-up of the round $S^4$ at two antipodal points. Exact symbolic
computation (script, part (a)) gives $s_h\equiv0$, $W_h\equiv0$ (conformally flat), $|\operatorname{Ric}^\circ_h|=8\sqrt3\,r^{-4}+O(r^{-6})$ and
$$
P(h)=32\pi^2,\qquad \int_{|x|>\varrho}|\operatorname{Ric}^\circ_h|^2=\frac{96\pi^2}{\varrho^4}+O(\varrho^{-6}).
$$
The map $\iota(x)=\sigma x/|x|^2$, $\sigma=\operatorname{diag}(-1,-1,-1,1)$, is an isometry of $h$ exchanging the two
ends, with fixed points exactly $(0,0,0,\pm1)$ and linearization $-I$ there. Thus $G=(\mathbb R^4\setminus0,h)/\iota$ is
the Green blow-up of $O=S^4/\mathbb Z_2$ at a regular point (Ju–Viaclovsky's construction \cite{ju2023conformally}):
a complete scalar-flat, conformally flat orbifold with two $A_1$ points and one ordinary AE end
$\{|x|>1\}$, metric $\delta+O(r^{-2})$ with $k$-th derivatives $O(r^{-2-k})$, and $P(G)=16\pi^2$. As a check,
noncompact Gauss–Bonnet $\chi_{\rm orb}(G)=\chi_{\rm orb}(O)-1=0=-P/(16\pi^2)+1$ (end term $+1$).

Fix distinct points $y_1,\dots,y_m\in X$ and $g_X$-normal coordinates $y$ there, $g_X=\delta+O(|y|^2)$. Remove
$|y|<\rho$ and attach the compact truncated cap $\{|x|\le 2\rho/\varepsilon\}\subset G$ with metric $\varepsilon^2h$, whose end
region is $(1+\varepsilon^2|y|^{-2})^2\delta$ in $y=\varepsilon x$ (the full cap core, including both $A_1$ points, sits behind this
end); outside $|y|>2\rho$ put $g_X$, and on the
annulus interpolate $g_\varepsilon=\delta+\chi_{\rm out}(g_X-\delta)+\chi_{\rm in}(\varepsilon^2h-\delta)$ with standard
cutoffs. Choose $\rho=\varepsilon^{1/2}$. On the annulus $|\partial^j(g_X-\delta)|\lesssim\rho^{2-j}$ and
$|\partial^j(\varepsilon^2h-\delta)|\lesssim\varepsilon^2\rho^{-2-j}$, $j\le2$, so all curvature components of
$g_\varepsilon$ are $O(1)$ there, on volume $O(\rho^4)=O(\varepsilon^2)$. Inside, the metric is exactly the scaled cap,
contributing $s=0$, $W=0$ and $P=16\pi^2-O((\varepsilon/\rho)^4)=16\pi^2-O(\varepsilon^2)$ per cap; outside it is exactly
complex-hyperbolic ($P=0$, $S=32\pi^2A$, $W=I_+=4\pi^2A/3$) minus volume $O(\rho^4)$. Hence, with all errors
$O(\varepsilon^2)$,
$$
P\to8\pi^2k,\ S\to32\pi^2A,\ W\to\tfrac{4\pi^2A}3,\ \operatorname{Vol}\to\operatorname{Vol}(g_X),\ \textstyle\int s\to s_X\operatorname{Vol}(g_X),\ L_s\to0,
$$
and $\mathscr D(g_\varepsilon)\to 4\cdot8\pi^2k/(8\pi^2(A+k))=4k/(A+k)$. The resulting orbifold is
$X\#m\,O=V_m$. The ceiling one is supplied by the universal dumbbell–cylinder construction (A02 package §1.2), which is a
connected sum at one regular point and so applies verbatim on orbifolds. Directly: a unit round
$S^3\times[0,L]$ inserted at a regular point with fixed transitions has $s=6$, $|\operatorname{Ric}|^2=12$,
$|\operatorname{Ric}^\circ|^2=3$ on the cylinder, so $4P$ and $R$ both grow like $12\cdot2\pi^2L$ while $L_s=O(1)$, giving
$\mathscr D\to1$. $\square$

**Equality and attainment.** A hypothetical metric with $P=8\pi^2k$ would have $\sigma=w=0$, but no such metric exists.
Indeed, it would also attain the all-metric scalar floor $S=32\pi^2A$. Conformal first variation of $S$ gives $\Delta s=0$;
then $s$ is a nonzero constant, and trace-free first variation gives $\operatorname{Ric}^\circ=0$, contradicting
$P=8\pi^2k>0$. Consequently $P(g)>8\pi^2k$ for every individual orbifold metric.

For $q=4k/(A+k)$ and $B=8\pi^2(A+k)$ one has
$$
\mathscr D-q=\frac{(1-q)\sigma/3+2(4-q)w+L_s}{R},\qquad
\mathscr D-1=\frac{(q-1)B+6w+L_s}{R}.
$$
Thus $\alpha_{\rm orb}$ is not attained for $k<A/3$ (equality would attain the $P$ floor) or for $k>A/3$ (the second
expression is strictly positive). At $k=A/3$, attainment is equivalent to $W^-=0$ and constant scalar curvature;
transfer of $\int(s^-)^2\ge32\pi^2A$ makes the constant negative, and nonattainment of the $P$ floor forces $\sigma>0$.
This single wall-existence question remains open. Full variations and equality formulas are in
`step75_review_nonattainment_and_root_restriction.md` §§3–4.

## 2. Theorem 74.B (mixed curvature transfer with bubble chirality)

Let $(V,g)$ be a compact orbifold whose isolated singular points are resolved by orientation-matched scalar-flat ALE
fillers $N_j$ (decay and gluing as in Lemma 86.S/86.S′) to $M_k$. Put $B_+=\sum_j\int_{N_j}|W^+|^2$. Under (SW)
$$
\int_V(s-\sqrt6|W^+|)^2+6B_+\ \ge\ 72\pi^2A. \tag{2.1}
$$
*Proof.* Expand $\int(s-\sqrt6|W^+|)^2=S-2\sqrt6\int s|W^+|+6I_+$ on the glued metrics $g_\varepsilon$, to each of which
Prop. 3.8 applies with its own monopole class (no convergence of classes is needed). Outside the annuli and fillers the metric is
$g$. In the scaled fillers $s\equiv0$ and $I_+\to\int_{N_j}|W^+|^2$ (tail $\to0$). On the annuli curvature is bounded and
volume is $O(\rho^4)$. Therefore $S\to S(g)$, $\int s|W^+|\to\int_Vs|W^+|$, $I_+\to I_+(g)+B_+$. $\square$

For Ricci-flat fillers $B_+=-2\pi^2C_+$, and (2.1) reads $\int_V(s-\sqrt6|W^+|)^2\ge72\pi^2A+12\pi^2C_+$.
For Ricci-flat Kähler fillers in their complex orientation, $C_+=0$ and the smooth inequality transfers without loss.
For a scalar-flat non-Ricci-flat filler, $B_+=P(N)/4-2\pi^2c_+(N)$ and the configuration also pays $P(N)>0$.

## 3. Theorem 74.C (necessary conditions for an Einstein orbifold bulk)

Let $V$ be as in §2 with Ricci-flat fillers, and suppose $g$ is Einstein. The negative-Yamabe exclusion of 86.S forces
$\lambda<0$. Put $x=S/(96\pi^2)$; Einstein Chern–Weil gives $I_\pm=2\pi^2(T_\pm-x)$. Then:

* (scalar transfer + positivity) $A/3\le x\le\min(T_+,T_-)$;
* (mixed transfer + Cauchy–Schwarz; constancy of $s$ and the sign of $\lambda$ are not needed for this bound)
$$
\big[\sqrt{8x}+\sqrt{T_+-x}\big]^2\ \ge\ 6A+C_+ . \tag{3.1}
$$

The left side of (3.1) is concave in $x$ with maximum $9T_+$ at $x=8T_+/9$; the test is evaluated by clipping this point to
the interval. With (0.1), expanding at large $A$ (the cap $x\le T_-=A/3+5k+C_-$ binds) gives the linear forms
$$
\text{scalar: } C_-+5k\ge0,\qquad \text{mixed: } 9C_-+2C_++42k-\frac{3(e-3d)^2}{4A}+O(A^{-2})\ \ge\ 0, \tag{3.2}
$$
with $e=C_+-k$, $d=C_-+5k$ (verifier's expansion). The negative $1/A$ correction explains why leading-order marginal
rows (e.g. $A_5$ at $k=5$) fail at every finite $A$.
For $C_+=0$ the exact form is $T_-\ge x_{\min}=\frac A{27}\big[4-\sqrt{1-3k/A}\big]^2$, with
$x_{\min}-\frac{A+k}3=\frac{4A}{27}(1-\sqrt{1-3k/A})^2>0$; in particular $k\le A/3$ and $C_->-14k/3$.

**Corollary 74.D (Kähler Ricci-flat filler budget).** If all fillers are Ricci-flat Kähler ALE spaces in their complex
orientation (Kronheimer ADE spaces, Šuvaina/T-type Milnor fibres, or any other), an Einstein bulk requires
$$
\sum_j\Big(\chi(N_j)-\frac1{|\Gamma_j|}\Big)\le\frac14\Big(\frac A3+5k-x_{\min}\Big)=\frac{7k}{6}-\frac{k^2}{12A}-O\!\Big(\frac{k^3}{A^2}\Big),
$$
obtained by inserting (0.2) into $T_-\ge x_{\min}$. Exact values of the right side are in the
JSON (`kaehler_RF_budget_exact`): e.g. $1.1554$ ($A=9,k=1$), $2.2738$ ($A=9,k=2$), $3.4428$ ($A=18,k=3$),
tending to $7k/6$. A filler with $b_2=r$ contributes $r+1-1/|\Gamma|\ge r+\tfrac12$. If the fillers carry all $k$ classes
($\sum r_j=k$) the budget requires $\sum_j(1-1/|\Gamma_j|)<k/6$; for one filler, $r\ge6(1-1/|\Gamma|)$ at leading order.
This is a *sufficient-rank-per-filler* condition: few fillers each of rank $\gtrsim6$ (larger $|\Gamma|$ at fixed rank makes it
slightly harder, not easier). The screening was run on ten sample values of $A$ plus the asymptotic form; it is a
necessary condition only.

## 4. Screening results (script part (c); A ranges over $9,18,\dots,90000$)

**Paired A1 ($V_m$).** $C_-=-6k$: fails both scalar ($-k<0$) and mixed ($-12k<0$) — consistent with Theorem 74.A.

**Single Kronheimer filler carrying $k$ classes.** With $k=\operatorname{rank}$: excluded for every $A$ for
$A_1,\dots,A_5,D_4,D_5$ (mixed linear forms $-12,-12,-9,-4.8,0,-7.5,-3$; $A_3$ at $k=3$ passes scalar at equality and
fails mixed, as Spirit #82 predicted; $A_5$ is marginal at leading order and fails at every finite $A$). Survives the necessary test for
$A_n$ ($n\ge6$, from $A\ge27$–$36$), $D_6$ ($A\ge90$), $D_7$, $E_6$ ($A\ge90$), $E_7$, $E_8$ ($A\ge36$). With extra bulk
exceptional classes ($k=\operatorname{rank}+1$) every listed filler passes for $A\ge9$–$18$.

**A02 Step-55 $k=1$ catalogue** (single $b_2\le1$ filler; only rows with $c_\pm\le0$ can be Ricci-flat):
* cyclic $b_2=1$ ends: 147 rows, 52 Ricci-flat-compatible, 46 pass the scalar test at large $A$, **only 8 pass the mixed test**:
  $L(49,23),L(49,32)$ $(-335/49,-53/49)$; $L(81,52),L(81,67)$ $(-527/81,-13/9)$; $L(121,15),L(121,113)$ $(-959/121,-5/121)$;
  $L(121,47),L(121,103)$ $(-695/121,-269/121)$, each from $A\ge27$. In particular A02's first survivor $L(9,4)$, $(c_+,c_-)=(-23/9,-5)$,
  passes scalar at equality and is **excluded** by the mixed test (linear form $-8.1$).
* $b_2=1$ ADE-end rows (hypothetical; *not* Kronheimer spaces, which have $b_2=\operatorname{rank}$): 13 rows, 8 Ricci-flat-compatible;
  $D_4$ excluded; $D_5$ ($A\ge90$), $D_6$–$D_8$, $E_6$–$E_8$ ($A\ge27$) survive the necessary test.
* rational balls: all 98 Ricci-flat-compatible rows survive both tests (computed; their charges are small, $c_\pm\ge-4(1-1/|\Gamma|)$). The T-type rows with $c_+=0$ are actual Ricci-flat Kähler (Šuvaina) fillers; the others are only charge rows.

**Status of survivors.** Passing (3.1) is necessary, not sufficient. For every survivor the missing information is
(a) whether the filler topology is realized by an actual Ricci-flat ALE metric (known only for Kronheimer and T-type
Milnor-fibre/Šuvaina fillers in the lists above), (b) whether the required plumbing/rational ball embeds in $M_k$ with
the bulk $V$ of the stated topology, and (c) existence of a negative Einstein metric on $V$, which by 86.S would give
$\alpha(M_k)=0$ — still not a smooth Einstein metric on $M_k$.

## 5. Consequence for minimizing configurations

Smooth finite-scale constructions (Burns kernel insertion, the certified perpendicular cell) give
$P_*(M_k)<8\pi^2k$. Consider a $P$-minimizing sequence on $M_k$ converging smoothly on compact subsets of the regular
locus to a smooth orbifold metric on $V_m$. Hypotheses used: (i) this local smooth convergence (no energy identity is needed:
nonnegativity of $|\operatorname{Ric}^\circ|^2$ gives $\liminf P(g_i)\ge P(V_m)$); (ii) the limit is a smooth orbifold metric on
$V_m$ in the sense of §1; (iii) (SW) and (R). Then $\liminf P(g_i)\ge8\pi^2k>P_*$: this architecture cannot be the limit of a
minimizing sequence, regardless of bubble or neck energy. The orbifold bound is not a
lower bound for smooth metrics: the strict gap records finite-scale relaxation unavailable to a singular bulk.

## 6. What changed

* The $V_m$ branch is closed for Einstein existence at every $k$, and its restricted variational problem is solved
  exactly: $\inf P=8\pi^2k$, $\alpha_{\rm orb}=\min\{1,4k/(A+k)\}$, with a fully explicit realizing family.
* The general principle: Ricci-flat (or scalar-flat) resolution transfers the **entire** smooth Seiberg–Witten curvature
  inequality to the singular bulk, with an explicit bubble $W^+$ ledger; no orbifold monopole theory is needed.
* The mixed transfer is genuinely stronger than scalar transfer: it removes 38 of 46 scalar-surviving cyclic $k=1$ rows,
  the $A_3$ ($k=3$) and $D_4$ configurations, and yields the clean budget of Cor. 74.D for Kähler Ricci-flat fillers.
