# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 106,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step106_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step106_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify Theorem 105.Q and Corollaries 105.L/105.H in the Step-105 note. Check orientation and normalization from Theorem G and Dai–Wei, the scalar-cap vanishing argument, the C_+(Omega) decomposition, the cap contribution to the mixed LeBrun estimate, and the arithmetic 9k+8 sum c <=3A and A/11. Identify any gap or needed repair precisely. Also assess whether (E2) is exactly implied by D(g_i)->0 at a fixed nonzero Einstein normalization plus total-volume convergence.

## Integrated Scientific Memo

# Verification memo: Step 105

**The cap orientation, curvature normalizations, mixed-LeBrun coefficient \(8\), and singleton threshold \(A/11\) are correct.** The cap-energy decomposition can be proved without Dai–Wei asymptotics. The note nevertheless needs repairs concerning individual end-charge limits, cap-volume accounting, extra ball caps, and the interpretation of zero charge. The assertion about \(\mathscr D\) cannot be unconditional because its definition is absent from the supplied materials.

## 1. Theorem G and Dai–Wei conventions

Write \(T_+(D)=2\chi(D)+3\tau(D)\). Theorem G gives
\[
C_+(g;D)=\widehat P(g;D)+T_+(D)-\mathcal Q_+(\partial D),
\qquad \mathcal Q_+=2\mathcal E-3\mathcal H.
\]
Its coefficients follow directly from
\[
2e+3L
=\frac1{4\pi^2}
\left(2|W^+|^2-\frac12|\operatorname{Ric}^{\circ}|^2+\frac{s^2}{24}\right).
\]

Orient \(L_{\ell,\rho}\) outward from \(\Omega_\rho\). The same interface is oriented oppositely as a cap boundary, so
\[
\mathcal Q_+(\partial C_j^{(\rho)};g_i)
=-\sum_{\ell\in J_j}\mathcal Q_+(L_{\ell,\rho};g_i).
\]
Consequently, at fixed \(\rho\),
\[
a_j(\rho):=\lim_i C_+(g_i;C_j^{(\rho)})
=T_+(C_j)+\sum_{\ell\in J_j}\mathcal Q_+(L_{\ell,\rho};g_\infty).
\tag{1}
\]
Here \(\widehat P(g_i;C_j^{(\rho)})\to0\), and \(C^2\) convergence on a compact collar controls the boundary transgressions. Continuity of the signature eta contribution follows from its variation formula; its kernel is cohomological, so there is no kernel-crossing jump.

The APS normalization should be made explicit:
\[
\eta_{\mathrm{Step\,33}}=\frac12\eta_{\mathrm{sig,Dai\text{–}Wei}}.
\]
Indeed, Dai–Wei Theorem 3.5 states
\[
\tau=\int L-\frac12\,\mathrm a\!-\!\lim\eta_{\rm sig},
\]
whereas Step 33 defines \(\int L=\tau+\mathcal H\). Thus for the specified fibred cusps,
\[
\mathcal E^\infty=0,\qquad
\mathcal H^\infty=\frac12\,\mathrm a\!-\!\lim\eta_{\rm sig}.
\]
The corresponding fibred-boundary statement, used for ALF model checks, is Theorem 3.6/4.3.

Dai–Wei Theorem 5.1 and §6 give
\[
\mathcal H^\infty=\frac e3-\operatorname{sign}e,
\]
hence
\[
\mathcal Q_+^\infty=-e+3\operatorname{sign}e,\qquad
\mathcal Q_-^\infty=e-3\operatorname{sign}e.
\]
With cap-oriented Euler number \(e_{\rm out}=-e\),
\[
\boxed{c_+=T_+(C)+e_{\rm out}-3\operatorname{sign}e_{\rm out}.}
\tag{2}
\]

The supplied Dai–Wei text is internally inconsistent: Corollary 1.2 displays \(\tau-e/3+\operatorname{sign}e\), while Theorems 3.5/5.1 and §6 imply \(\tau+e/3-\operatorname{sign}e\). Step 105 uses the latter, consistently with the supplied model curvature calculation.

For example, Taub–NUT with \(W^-=0\) has
\[
\frac1{8\pi^2}\int|W^+|^2=1,
\qquad C_+=4.
\]
Equation (2), with \((\chi,\tau,e_{\rm out})=(1,0,-1)\), gives \(4\). The table should list **\(C_+=4\)** rather than putting the differently normalized value \(1\) beneath a \(C_+\) heading. The script correctly reproduces this arithmetic, but its hardcoded expected values are consistency checks, not new proofs of the model geometries. In particular, the Step-27 Taub-bolt calculation itself is not included here.

## 2. Theorem 105.Q: a repaired proof and its precise scope

### Cap-charge existence does not require an eta-limit hypothesis

Use an increasing exhaustion and label the complementary components compatibly, so that the caps shrink:
\[
C_j^{(\rho_2)}\subset C_j^{(\rho_1)}
\quad\text{when }\rho_2<\rho_1.
\]
This compatibility should be explicit in (E3), including compatibility with the convergence diffeomorphisms.

Since the \(C_+\) density is nonnegative,
\[
0\le a_j(\rho_2)\le a_j(\rho_1).
\]
Moreover,
\[
a_j(\rho)\le\lim_iC_+(g_i;M)=A-k.
\]
Therefore
\[
c_j=\lim_{\rho\to0}a_j(\rho)
\]
exists and is nonnegative. Equation (1) then proves that the **summed boundary charge**
\[
q_j^\infty:=
\lim_{\rho\to0}
\sum_{\ell\in J_j}\mathcal Q_+(L_{\ell,\rho};g_\infty)
\]
exists, with
\[
\boxed{c_j=T_+(C_j)+q_j^\infty.}
\tag{3}
\]

Thus it is unnecessary to impose fibred asymptotics merely to establish cap-charge existence. The apparent circular sentence “the charge converges by the first identity itself” becomes a proof once this monotonicity argument is supplied.

There is, however, a distinction between **summed and individual end charges**. If a cap meets several ends, convergence of the sum does not alone prove convergence of each summand. The theorem should either:

- use \(q_j^\infty\) as in (3); or
- explicitly supply stable product end collars, individual charge limits, or Dai–Wei asymptotics.

For stable product collars, Theorem G on the Einstein annulus between two cuts gives
\[
\mathcal Q_+(L_{\ell,\rho_2})
-\mathcal Q_+(L_{\ell,\rho_1})
=-C_+(g_\infty;\text{annulus}),
\]
because its Euler characteristic and signature vanish. This proves individual charge convergence from the finite curvature energy established below.

### Scalar-cap vanishing: the volume statement needs correction

For several caps, the note incorrectly identifies **each cap’s volume** with the **whole tail volume**. What follows immediately is
\[
\sum_j\operatorname{Vol}_{g_i}(C_j^{(\rho)})
=\operatorname{Vol}_{g_i}(M)-\operatorname{Vol}_{g_i}(\Omega_\rho)
\longrightarrow
V_\infty-\operatorname{Vol}_{g_\infty}(\Omega_\rho).
\]
Hence, for every \(j\),
\[
\limsup_i\operatorname{Vol}_{g_i}(C_j^{(\rho)})
\le\operatorname{Vol}_{g_\infty}(\Omega\setminus\Omega_\rho).
\]
The right side tends to zero. Therefore
\[
\begin{aligned}
\int_{C_j^{(\rho)}}s_i^2
&\le
2\int_M(s_i-\bar s_i)^2
+2\bar s_i^2\operatorname{Vol}_{g_i}(C_j^{(\rho)}),\\
\lim_{\rho\to0}\limsup_i\int_{C_j^{(\rho)}}s_i^2&=0.
\end{aligned}
\tag{4}
\]

Together with the existence of \(a_j(\rho)\), this yields the robust formulation
\[
\lim_{\rho\to0}\limsup_i
\frac1{2\pi^2}\int_{C_j^{(\rho)}}|W_i^+|^2
=
\lim_{\rho\to0}\liminf_i
\frac1{2\pi^2}\int_{C_j^{(\rho)}}|W_i^+|^2
=c_j.
\tag{5}
\]
Literal inner limits for each cap’s scalar or Weyl integral need not follow from the volume calculation alone. They can be justified by a compatible no-loss-of-volume argument identifying each cap’s associated tail, or replaced throughout by (4)–(5). The latter suffices for every stated curvature inequality.

### The global decomposition is correct

At fixed \(\rho\), additivity and local convergence give
\[
A-k
=C_+(g_\infty;\Omega_\rho)+\sum_j a_j(\rho).
\]
Monotone convergence therefore proves
\[
\boxed{C_+(g_\infty;\Omega)=A-k-\sum_jc_j.}
\tag{6}
\]
It also proves finiteness of the Einstein-side energy. No Dai–Wei end classification is needed for (6).

The same argument applies to \(C_-\). It is this energy argument—not an assumed independent eta-limit theorem—that closes the aggregate decomposition.

## 3. Corollary 105.L: exact cap contribution and arithmetic

Let
\[
I(g;D)=\int_D(s-\sqrt6|W^+|)^2.
\]
The cap contribution is not merely bounded by its Weyl energy; it approaches it in the double-limit sense. Indeed,
\[
\left|I(g_i;C)-6\int_C|W_i^+|^2\right|
\le
\int_Cs_i^2+
2\sqrt6\,\|s_i\|_{L^2(C)}\|W_i^+\|_{L^2(C)}.
\]
The Weyl norms are uniformly bounded by the total \(C_+\) budget. Equations (4)–(5) imply
\[
\boxed{
\lim_{\rho\to0}\limsup_i I(g_i;C_j^{(\rho)})
=
\lim_{\rho\to0}\liminf_i I(g_i;C_j^{(\rho)})
=12\pi^2c_j.}
\tag{7}
\]

On \(\Omega\), put
\[
x=\frac1{96\pi^2}\int_\Omega s_\infty^2,\qquad
y=\frac1{2\pi^2}\int_\Omega|W_\infty^+|^2.
\]
Then \(x+y=A-k-c\), where \(c=\sum_jc_j\), and
\[
I(g_\infty;\Omega)
\le12\pi^2(\sqrt{8x}+\sqrt y)^2
\le108\pi^2(x+y).
\]
Passing the global mixed estimate through the decomposition gives
\[
72\pi^2A
\le108\pi^2(A-k-c)+12\pi^2c.
\]
Thus
\[
6A\le9A-9k-8c,
\qquad
\boxed{9k+8c\le3A.}
\tag{8}
\]

All constants are correct.

The additional statement \(k+c\le2A/3\) is true, but its stated proof invokes the separate scalar estimate \(\int s^2\ge32\pi^2A\), not explicitly included in the corollary’s hypotheses. No additional hypothesis is needed for that conclusion: since \(k,c\ge0\), (8) already implies the stronger bound
\[
\boxed{k+c\le3A/8.}
\]
If the intended assertion is specifically \(x\ge A/3\), the scalar estimate must be included explicitly.

Positive \(c_j\) forces \(W^+\)-energy concentration in vanishing volume and excludes uniformly bounded-curvature collapse on that cap. Calling this a resolved bubble decomposition requires additional compactness results; concentration alone does not provide them.

## 4. Corollary 105.H: correct thresholds, with two important qualifications

For the specified negative-definite \(S^3\) cap,
\[
\chi=1+r,\qquad \tau=-r,\qquad T_+=2-r.
\]
Equation (2) gives
\[
c_+=
\begin{cases}
4-r,&e_{\rm out}=-1,\\
-r,&e_{\rm out}=+1.
\end{cases}
\]
Hence an exceptional cap with \(r\ge1\) must use the first chirality, and \(r\le4\).

For \(N\) exceptional caps with \(\sum r_j=k\),
\[
c_{\rm exceptional}=4N-k.
\]
If there are additionally \(q\) charge-\(4\) ball caps, the exact necessary condition is
\[
\boxed{k+32N+32q\le3A.}
\tag{9}
\]
Charge-zero balls do not alter it. The note’s \(k+32N\le3A\) is still necessary, but its displayed equivalence omits \(32q\).

The thresholds follow:
\[
N=k\quad\Longrightarrow\quad33k\le3A
\quad\Longrightarrow\quad\boxed{k\le A/11}.
\]
If \(4\mid k\) and all exceptional caps carry four classes,
\[
N=k/4,\qquad c_{\rm exceptional}=0,\qquad k\le A/3.
\]
For arbitrary \(k\), optimal packing gives the sharper integer condition
\[
\boxed{k+32\left\lceil k/4\right\rceil+32q\le3A.}
\]
A single four-class cap with \(q=0\) is compatible with (8) precisely when \(A\ge12\).

These are **necessary numerical conditions**, not existence or sufficiency statements. “Survives precisely as configurations” should mean only “is not excluded by this estimate.”

### Zero \(C_+\)-charge is not zero curvature energy

The phrase “invisible to every aggregate curvature inequality” is false. For the four-class cap,
\[
\chi=5,\qquad\tau=-4,\qquad e_{\rm out}=-1.
\]
Its Einstein-side Euler number is \(+1\), so \(\mathcal Q_-^\infty=-2\). The opposite-chirality identity gives
\[
\boxed{c_-=(2\chi-3\tau)-2=22-2=20.}
\]
Thus the cap necessarily carries
\[
\frac1{2\pi^2}\int|W^-|^2\longrightarrow20,
\qquad
\int|W^-|^2\longrightarrow40\pi^2,
\]
even though its scalar, traceless-Ricci, and \(W^+\) energies vanish.

It is invisible to the **\(C_+\)/mixed-LeBrun obstruction**, not energy-free. If smooth noncollapsed rescaled limits exist, they are ASD Ricci-flat; simply connected such limits are hyperkähler and spin. But (E) alone does not establish a bubble tree, an F-structure, or localization of the odd part of \(-I_4\) into collapsed regions. The proposed lattice/spin mechanism remains a construction or obstruction problem, not a consequence of Theorem 105.Q.

## 5. Is (E2) “exactly” implied by \(\mathscr D\to0\)?

The supplied input does not define \(\mathscr D\). The exact answer depends on that definition and on what “fixed Einstein normalization” fixes.

For the scale-invariant optimal full residual,
\[
\mathscr D_{\rm opt}(g)
=\frac1{8\pi^2}\int
\left|\operatorname{Ric}-\frac{\bar s}{4}g\right|^2,
\]
orthogonality gives
\[
\boxed{\mathscr D_{\rm opt}
=\widehat P+\frac1{32\pi^2}\int(s-\bar s)^2.}
\]
Thus vanishing is exactly equivalent to vanishing of the two defect terms in (E2). If normalization fixes \(\bar s=s_\infty\ne0\), adding total-volume convergence gives all of (E2).

Alternatively, (E1) already pins the mean scalar: on any positive-volume compact \(K\Subset\Omega\),
\[
\operatorname{Vol}_{g_i}(K)|\bar s_i-s_\infty|^2
\le2\int_K(s_i-\bar s_i)^2+
2\int_K(s_i-s_\infty)^2\longrightarrow0.
\]

For the fixed-\(\lambda\) residual, \(\lambda=s_\infty/4\),
\[
\mathscr D_\lambda
=\widehat P+\frac1{32\pi^2}\int(s-\bar s)^2
+\frac{\operatorname{Vol}(g)}{32\pi^2}(\bar s-4\lambda)^2.
\]
With total volume tending to a positive finite limit, \(\mathscr D_\lambda\to0\) is equivalent to the three curvature/scalar conditions in (E2). A fixed-\(\lambda\) functional is not itself scale invariant unless \(\lambda\) scales with the metric.

If \(\mathscr D\) controls only \(\widehat P\), scalar variance is not supplied by these algebraic identities; further analytic information is required. Total-volume convergence alone does not supply it or fix the mean scalar.

**Accordingly, Step 105 should display the defining decomposition of \(\mathscr D\) before claiming exact implication.** Even for the full residual, vanishing does not establish the extraction, compatible cap topology, or no-loss-of-volume structure in (E1)/(E3); those remain separate geometric hypotheses.