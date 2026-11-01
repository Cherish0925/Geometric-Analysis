# Step 51 corrections, made durable in Step 52: residual entry, link charges, and the Kähler recovery theorem

Sources of the corrections: the three Step-51 verifier integrations
`trace/ttcs/results/step51_ttcs01_verifier{1,2,3}_integration.md` (branches `step51_ttcs01_sub{1..6}_verifier.md`),
Bour \cite{bour2010fourth}, Anderson (orbifold compactness), Tian–Viaclovsky (moduli of critical metrics),
Gursky–Viaclovsky (critical metrics on connected sums), Arezzo–Pacard (blow-up / desingularization of cscK),
and Streets, *The long time behavior of fourth-order curvature flows*
(`Knowledge/objects/papers/The-long-time-behavior-of-fourth-order-curvature-flows--5b1863f1c7b9--f1cab1a2d745/object.md`, \cite{streets2011long}).
This note supersedes the analytic parts (§§2–4) of `step50_minimizer_entry_PS_noncollapsed_alternative.md`; §5 (Kähler) of that note
survives in the corrected form below, §7 (family ledger) survives unchanged.

Notation. \(P(g)=\int|\mathrm{Ric}^\circ|^2\), \(Q(g)=\operatorname{grad}_{L^2}P(g)\), so \(DP_g(h)=\int\langle Q,h\rangle d\mu\).

## 1. What is proved about weighted descent

1. **Scaling.** \(Q(\lambda^2g)=\lambda^{-2}Q(g)\) as a \((0,2)\)-tensor; hence \(|Q|^2d\mu\) has weight \(\lambda^{-4}\) and
   \(\rho^4|Q|^2d\mu\) is scale invariant when \(\rho\) is a length. Rescaling a region by \(r\), \(\hat g=r^{-2}g\):
   \(\int_U|Q(\hat g)|^2d\mu_{\hat g}=r^4\int_U|Q(g)|^2d\mu_g\); if \(\rho\ge\kappa r\) on \(U\) this is \(\le\kappa^{-4}\int_U\rho^4|Q|^2\).
2. **Fixed-data weighted DeTurck flow.** For fixed smooth positive \(w\), fixed smooth \(g_0\) and background \(\bar g\),
   \(\partial_tg=-wQ(g)+\mathcal L_{wV_{\bar g}(g)}g\) is strongly parabolic (principal symbol \(w\,\sigma(D[-Q+\mathcal L_{V}])\); Bour's
   class with \(a=b=0\)) and has a unique smooth solution on a data-dependent interval \([0,T)\).
   \(\tfrac{d}{dt}P=-\int w|Q|^2\) (Lie terms do not change \(P\)).
3. **Averaging.** If the flow exists on \([0,S]\), some \(t_*\in[S/2,S]\) has
   \(\int w|Q(g(t_*))|^2\le \tfrac2S(P(g(S/2))-P(g(S)))\le\tfrac2S(P(g_0)-\alpha)\).
   The Step-50 intermediate inequality with \(P(g_0)-P(g(t_*))\) on the right is **false** and is withdrawn.
4. **Sequence form.** For a minimizing sequence with \(\delta_i=P(g_i)-\alpha\to0\), weighted flows existing up to \(T_i\) with
   \(\delta_i/T_i\to0\) produce \(g_i(t_i)\) with \(P(g_i(t_i))\le P(g_i)\) and \(\int w_i|Q(g_i(t_i))|^2\le2\delta_i/T_i\to0\).
   A uniform \(T_i\ge T_0\) is not logically needed; \(\delta_i/T_i\to0\) is.

## 2. What is false or unproved in Step 50 (Lemma W, Theorems 50.A–C)

- No uniform own-scale lifetime for arbitrary (possibly collapsed) data follows from Bour: Bour's Theorem 1.5 (BBS-type estimates)
  assumes the flow already exists with \(\|\mathrm{Rm}\|_\infty\le D\) and uses the Sobolev constant to pass to pointwise bounds.
  Streets' Theorem 1.3 (positive-time smoothing) and Corollary 1.9 (finite \(T\) forces \(\limsup|\mathrm{Rm}|=\infty\)) likewise assume
  a spacetime curvature bound or describe the singular time; neither gives a lifetime from initial data alone, and Streets' Remark 1.12
  records a noncollapsing estimate at the curvature scale as an open problem.
- All-order bounds \(\rho^j|\nabla^j\log\rho|\le C_j\) for a smoothed curvature radius are false in general from \(4\)-th order on
  (commutators bring \(\nabla\mathrm{Rm}\), unbounded under a mere curvature bound).
- Uniform \(C^2\)-closeness \(\|\rho^{-2}(g_t-g_0)\|_{C^2}\le Ct^\theta\) is false (high-frequency curvature ripples are smoothed in time ~ wavelength\(^4\)).
- The reverse scale comparison \(r_{g(t_*)}\le C\rho_{g_0}\) is false: fine curvature structure determining a small input radius can be
  erased at vanishing \(P\)-cost; but this is exactly what Step 50.B needed in order to transfer the input-weight residual to the output's
  point-picked scale. The lower comparison \(r_{g_t}\gtrsim\rho_{g_0}\) is plausible under a genuine smoothing theorem but unproved.
- The weighted flow leaves the \(s=-4\) slice. Yamabe projection does not increase \(P\) in nonpositive classes
  (\(P=2\int|W|^2+\frac1{12}\int s^2-16\pi^2\chi\)), but \(Q\) is not conformally covariant, so the residual is not transported.
  Normalization to \(s=-4\) is legitimate only after an exact critical limit is obtained (then \(\Delta s=0\), \(s\) constant).

Consequently Theorems 50.A–C are **not proved** for arbitrary noncollapsed minimizing sequences.

## 3. Corrected conditional structure theorem (Step-51 form)

Hypotheses on a unit-volume sequence \(g_i\), \(P(g_i)\to\alpha(M)\): (PS) \(\int\rho_i^4|Q(g_i)|^2\to0\) with \(\rho_i\) comparable to the
output curvature scale; (NC) \(\operatorname{vol}B(x,r)\ge\nu_0r^4\), \(r\le1\); (S) uniform local Sobolev inequality; (R) own-scale
derivative bounds \(\rho^{m+2}|\nabla^m\mathrm{Rm}|\le C_m\). (Step 52 removes (R) and replaces \(\rho\) by the energy radius; see
`step52_...` note.) Conclusions:

1. small-energy control in modulus form; Anderson's linear estimate is used only on exact critical blow-up limits;
2. orbifold limit \((V,g_\infty)\), \(Q(g_\infty)=0\) on the regular part, \(s\) constant on each regular component;
3. ALE bubbles are exact \(P\)-critical with \(s\in L^2\) harmonic, hence \(s\equiv0\), hence Bach-flat (\(B=\tfrac s3\mathrm{Ric}^\circ\));
4. **only lower semicontinuity**: \(\alpha=P(g_\infty)+\sum_bP(N_b)+E_{\rm neck}\), \(E_{\rm neck}\ge0\); a no-neck theorem is separate;
5. no concentration \(\Rightarrow\) \(\alpha\) attained by a smooth \(P\)-critical metric on \(M\);
6. \(\alpha=0\Rightarrow\) Einstein bulk components and Ricci-flat ALE bubbles; \(\Gamma=1\) Ricci-flat ALE are flat (Bishop–Gromov),
   so nontrivial zero-cost concentration passes through \(\Gamma\neq1\) links.

\(P\)-criticality is \(B^{1/6}\)-flatness (\(P=\tfrac12\mathcal B_{1/6}-16\pi^2\chi\) in the GV parametrization). The critical equation
controls a second divergence of the Weyl tensor; it does not determine \(\delta W^+\) algebraically and does not remove the second-jet
terms of the Step-43 Cotton pairing.

## 4. Link-charge ledger (Theorem G, corrected)

With \(q_\sigma(\Gamma)=\tfrac2{|\Gamma|}-3\sigma\eta_\Gamma\) and the convention
\(\tfrac1{12\pi^2}\int(|W^+|^2-|W^-|^2)=\tau+\sum_e\eta_{\Gamma_e}\):

- smooth multi-ended scalar-flat ALE \(N\):
  \(\widehat P(N)\ge\big[2\sum_e|\Gamma_e|^{-1}-2\chi(N)+3|\tau(N)+\sum_e\eta_{\Gamma_e}|\big]_+\);
- truncated block \(\Omega\) with outer and inner (orbifold) links:
  \(\widehat P(\Omega)=\tfrac1{2\pi^2}\int|W^\sigma|^2+\tfrac1{96\pi^2}\int s^2-(2\chi+3\sigma\tau)(\Omega)+\sum_{\rm out}q_\sigma-\sum_{\rm in}q_\sigma\);
  internal links cancel only after the whole tree is assembled;
- tests: flat \(\mathbb R^4\): 0; Burns: 1; Eguchi–Hanson: 0 (\(\eta_{\mathbb Z_2}=0\)); Kronheimer ADE with \(b_2=r\): 0, with
  \(3\eta_\Gamma=r-2+2/|\Gamma|\);
- single-ended smooth \(\Gamma=1\) bubble with capped \(b^+=0\), \(b_2=m\), \(b_1=q\): \(\widehat P\ge m+4q\) (Step 50's \(m-2q\) is wrong);
  \(\kappa\) such ends: \(\ge b_2+4b_1+4\kappa-4\).

Hence "scalar-flat bubbles never save" is false (Kronheimer bubbles carry topology at zero cost); the true statement is that single-ended,
\(\Gamma=1\), negative-definite bubbles pay at least their \(b_2+4b_1\). General topology is reconstruction by gluing truncated blocks along
\(S^3/\Gamma\) links, not an ordinary connected sum; SW connected-sum vanishing applies only after a genuine smooth connected-sum splitting;
Donaldson diagonalization fixes intersection forms, not diffeomorphism types. Exact bulk attainment with bubbles,
\(\alpha(M)=\alpha(\widehat V)+8\pi^2r\), needs a true splitting \(M\cong\widehat V\#r\overline{\mathbb{CP}}^2\), matching link payment, and the
Burns upper bound.

**Certified-cell consequence (restricted).** For \(M=X\#\overline{\mathbb{CP}}^2\) with \(\widehat\alpha(M)\le0.995662732771115<1\), under the
conditional structure theorem no separated smooth \(\Gamma=1\) region with capped \(b^+=0\) and \(b_2+4b_1\ge1\) can occur (in particular
\(b_1>0\) is expensive, not an escape). Remaining alternatives: no concentration (smooth \(B^{1/6}\)-flat minimizer), \(\Gamma\ne1\) links,
positive-\(b^+\) transfer (when a genuine connected-sum splitting exists), homology-trivial \(\Gamma=1\) regions, Sobolev degeneration or collapse.

## 5. Theorem \(K_\infty\) (proved; fixed complex structure)

Let \(X\) be a minimal compact complex surface of general type, \(A=K_X^2\), and \((M,J)\) obtained by \(k\) successive blow-ups at smooth
points of intermediate surfaces (distinct or infinitely near). Then
\[
\inf\{P(g):g\ \text{Kähler for }J\}=8\pi^2k,
\]
and for \(k\ge1\) every Kähler metric has \(P>8\pi^2k\).

*Lower bound.* With total-transform classes \(e_i\) (\(e_i\cdot e_j=-\delta_{ij}\), \(\pi^*K_X\cdot e_i=0\), \(K_M=\pi^*K_X+\sum e_i\),
\(e_i\cdot\Omega>0\)) and \(L=\pi^*K_X\) nef and big, Hodge index gives \((L\cdot\Omega)^2\ge A\Omega^2\), and
\[
\frac{P}{8\pi^2}=\frac{(K_M\cdot\Omega)^2}{\Omega^2}+\frac1{32\pi^2}\int(s-\bar s)^2-A+k>k .
\]
Quantitatively, \(\Omega=tL+\beta\), \(b=\sum e_i\cdot\Omega\): \(P/8\pi^2-k=\frac{2tAb+b^2+A|\beta^2|}{t^2A+\beta^2}+\frac1{32\pi^2}\int(s-\bar s)^2\).

*Recovery.* Arezzo–Pacard Thm 1.3 desingularizes the negative KE canonical orbifold (\(SU(2)\) singularities, discrete automorphisms,
crepant ALE models) to cscK metrics on \(X\) in classes \(\lambda K_X+\xi_\delta\), \(\xi_\delta\to0\); Thm 1.1 is then applied successively at
the prescribed smooth points with independent parameters \(t_i\) (nondegeneracy persists since automorphisms are discrete). With
\(\Omega=\pi^*\Omega_\delta-\sum t_ie_i\), \(T=\sum t_i\), \(Q=\sum t_i^2\):
\(P/8\pi^2=k+\frac{(\lambda A+T)^2}{\lambda^2A+\xi_\delta^2-Q}-A\to k\). A common-scale expansion
\(k+\frac{2\varepsilon^2}{\lambda}\sum a_i+O(\varepsilon^4)\) holds only under a common parametrization.

*Yamabe variables.* Negative cscK metrics are Yamabe representatives up to scale; at \(s=-4\), \(|W^+|^2=2/3\) pointwise, so \(D_W=0\)
exactly and \(P-8\pi^2k=4\Delta V\), \(\Delta V\to0\) along the recovery family. The statement concerns the fixed \(J\) only.
For \(k=0\) the infimum \(0\) is attained iff \(K_X\) is ample.

## 6. O10 separation (reply #822 to A01)

Metric residuals, weighted Weyl concentration and Theorem-G link charges are metric data; they give no control of the boundary degree of a
monopole line bundle or of a common leading spinor/connection jet on finite marked blocks. Finite-block O10 statements must import actual-field
trace, flux and Chern–Simons/relative-degree control.
