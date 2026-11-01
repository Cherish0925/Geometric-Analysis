# TTCS Independent Branch Record

```json
{
  "step_id": 58,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/spirit_step57_rational_branch_and_global_tests.md",
    "Sessions/S1003A01/workspace/notes/step57_bianchiVIII_strict_AKE_negative.md",
    "Sessions/S1003A01/workspace/scripts/step57_classA_metric_only.py",
    "Sessions/S1003A01/workspace/scripts/step56_bianchiA_ake.py",
    "Sessions/S1003A01/workspace/scripts/step56_akeA_propagate.py"
  ]
}
```

## Task

Independently verify the proposed explicit Bianchi-VIII cohomogeneity-one almost-Kähler Einstein pair. Read the exact rational formulas and the underlying class-A convention/code. Check the mathematical chain: structure equations and orientation; coefficient normalization |Omega|^2=2; direct closure dOmega=0; Ric(g)=-3g; strictness q>0; and whether the reported opposite-chirality Weyl block W^-=0 follows. Identify any sign, normalization, or logical error. Give a concise rigorous proof route that does not depend on numerical ODE shooting or on primality of a modular ideal. Distinguish exact local existence from end extension and novelty.

## Output

# Verification of the Step‑57 Bianchi‑VIII almost‑Kähler Einstein pair

## Summary

The local object is correct. I re-derived every convention independently. The explicit rational metric matches the exact rational point, and the Einstein, closure, unit-length, strictness and \(W^-\) relations hold exactly at the rational points tested. The pair is a self-dual Einstein metric with \(\lambda=-3\) and a strictly almost-Kähler (AK) form \(\Omega\in\Lambda^+\).

Everything reduces to rational identities in \(p\), so no ODE shooting and no primality statement is needed.

The bolt also closes, with one condition: the group must be \(SL(2,\mathbb R)\), not \(PSL\), and \(-I\notin\Gamma\). The weight analysis for \(\Omega\) works out with weight 1. Weight 3 would have made \(x_2\sim t\) singular.

Novelty is not settled by anything in the files.

## 1. Conventions

**Structure equations.** With \(n=(-1,1,1)\) and \(d\sigma_i=2n_i\sigma_j\wedge\sigma_k\), the brackets are \([X_2,X_3]=2X_1\), \([X_3,X_1]=-2X_2\), \([X_1,X_2]=-2X_3\). This is \(\mathfrak{sl}(2,\mathbb R)\), and \(X_1\) is the elliptic generator because \(\mathrm{ad}X_1\) has eigenvalues \(\pm2i\). In the metric's own frame, \(de_i=h_i\,e_0\wedge e_i+2W_i\,e_j\wedge e_k\).

**Ricci formulas.** Milnor's formula with structure constants \(2W_i\) gives
\[
\mathrm{Ric}^{(3)}_{ii}=2\big(W_i^2-(W_j-W_k)^2\big).
\]
Hence \(\mathrm{Ric}_{ii}=-h_i'-h_iS+\mathrm{Ric}^{(3)}_{ii}\) and \(\mathrm{Ric}_{00}=-\sum(h_i'+h_i^2)\). The Gauss equation \(R^{(3)}=2\lambda+2\sum h_ih_j\) reproduces \(Q+\lambda=0\) with the stated \(Q\).

**Vanishing off-diagonal Ricci.** The map \(\sigma_j,\sigma_k\mapsto-\sigma_j,-\sigma_k\) is a Lie-algebra automorphism. It therefore induces local isometries forming a Klein four-group, which forces \(\mathrm{Ric}_{0i}=\mathrm{Ric}_{ij}=0\) and makes the curvature operator block-diagonal on the planes \(\mathrm{span}\{e_{0i},e_{jk}\}\).

**Sanity checks.** The flat metric \(a_i=t\) and the hyperbolic metric \(a_i=\sinh t\) satisfy the stated \(h'\)-equations and the constraint.

**Closure.** Unimodularity gives \(d(\sigma_j\wedge\sigma_k)=0\). Therefore \(d\Omega=0\iff (x_ia_ja_k)'=2n_ix_ia_i\), which is \(x_i'=\mu_ix_i\) with \(\mu_i=2W_i-h_j-h_k\). This is correct for \(\omega_i=e_{0i}+e_{jk}\), which is self-dual in the orientation \(e_{0123}\).

**Normalization.** \(|\omega_i|^2=2\) in the form norm, so \(\sum x_i^2=1\) gives \(|\Omega|^2=2\). This is exactly the condition for \(J=g^{-1}\Omega\) to be an orthogonal almost-complex structure. There is no normalization error.

**Code.** `step57_classA_metric_only.py check` imports `step56_ake_propagate`, but the supplied file is `step56_akeA_propagate.py`. Either a second file exists or the check cannot run as written; this should be reconciled.

## 2. Exact checks of the rational formulas

**The point \(p=1/2\) is the exact point.** At \(p=1/2\) one gets \(A=(28/27,\,140/9,\,256/21)\) and \(G=448/45\). From these:
- \(W_1/W_2=-1/15\) and \(W_3/W_2=192/245\).
- \(h_i=\tfrac12(\ln A_i)_p/\sqrt G\) gives \(c\cdot(176/147,\ 656/735,\ 76/147)\) with \(c^2=315/256\), which is exactly the rescaling from \(Q=256/105\) to \(Q=3\).
- \(X=(5/32,\,27/32)\) and \(q=972/343=c^2\cdot 27648/12005\).

**Einstein equation, directly from \(A_1,G\).** With \(L_1=(\ln A_1)_p=176/21\), \(L_1'=-13504/441\) and \((\ln G)_p=-296/105\), I get \(h_1'=-324/343\). The right-hand side \(-h_1S+2(W_1^2-(W_2-W_3)^2)+3\) also equals \(-324/343\).

**Constraint at two points.** At \(p=1/2\), \(Q=256/105\) in unscaled units. At \(p=2/3\), with \(h,W\propto(912,1136,516;\,-49,735,320)/(336\sqrt7)\), the constraint gives exactly \(2370816/790272=3\).

**Unit length and closure.**
- \(X_1+X_2\equiv1\) identically: \((1-p)^3(3p+1)+(1+p)^3(3p-1)=16p^3\).
- At \(p=1/2\), \(d\ln X_1/dt=-81\sqrt{35}/140=2\mu_1\).

**Curve equation.** \(F(W)=0\) at the exact point, numerically to about \(10^{-6}\) by hand.

**The "Key lemma".** It is correct. Direct computation gives
\[
(\ln X_1)'-2\mu_1=-\frac{\Phi_1}{\mu_2(\mu_2-\mu_1)} .
\]

**The ideal-plus-exact-point route.** This route is logically sound without primality:
- If \(D(g_k)\in P\) for all generators \(g_k\), then along an analytic trajectory \(g(t)\) satisfies a linear ODE with \(g(0)=0\), so \(g\equiv0\).
- \(D Q=0\) once \(\lambda=-Q\) is substituted.
- The reconstruction \(a_i=|W_jW_k|^{-1/2}\) reproduces \(a_i'/a_i=h_i\) and \(|W_i|=a_i/(a_ja_k)\) with the correct sign pattern \((-,+,+)\).

## 3. The block \(W^-=0\), with an independent derivation

**Connection forms.** They are \(\omega^i{}_0=h_ie_i\) and \(\omega^j{}_k=\alpha_ie_i\), where \(\alpha_i=W_j+W_k-W_i\).

**Curvature.** This gives
\[
K_{0i}=-(h_i'+h_i^2),\qquad R_{0ijk}=\alpha_kh_j+\alpha_jh_k-2h_iW_i .
\]
The sign of the mixed term is fixed against \(K\) by pair symmetry of the curvature operator.

**Weyl eigenvalues.** Using \(K_{0i}=K_{jk}\) (Einstein), the eigenvalue on \(\omega_i^\mp\) is \(K_{0i}\mp R_{0ijk}\). Hence:
- \(W^-=0\iff K_{0i}-R_{0ijk}=\lambda/3\);
- the eigenvalues of \(W^+\) are \(w_i=2(K_{0i}+1)\).

**A first-order polynomial condition.** Substituting the Einstein equation for \(h_i'\) turns \(W^-=0\) into
\[
E_i=(h_i-W_i-W_j+W_k)h_j+(h_i-W_i-W_k+W_j)h_k+2h_iW_i-2W_i^2+2(W_j-W_k)^2+\tfrac23\lambda=0 .
\]
- \(\sum_i E_i=0\) follows from the Bianchi identity, so only two conditions are independent.
- \(E_i\) is the first-order statement \(F^-=\tfrac{\lambda}{3}\Sigma^-\) for the induced connection on \(\Lambda^-\).

**Exact verification of \(E_i\).**
- At \(p=1/2\), \(R_{0ijk}=(62,-274,212)/343=K_{0i}+1\) for all three \(i\).
- At \(p=2/3\), the numerators of \(E_1\) and \(E_2\) are exactly \(1580544-1580544=0\).

**Consistency with other reported values.**
- At \(p=1/2\), \(w=(124,-548,424)/343\). With \(X=(5/32,27/32)\) this gives \(|\eta|^2=2X_1X_2(w_1-w_2)^2=2430/2401\). This is exactly the Spirit formula's value, in the form norm.
- At the bolt, totally geodesic \(\Sigma\) with metric \(6(\sigma_2^2+\sigma_3^2)\) has \(K_{23}=-2/3\). Then \(w_1=2/3\) and \(w_2=w_3=-1/3\), which reproduces the reported spectrum \((-1/3,-1/3,2/3)\).
- The Step‑57 range \(\eta\approx0.4\text{–}0.7\) is the form-norm \(\eta\) divided by \(\sqrt2\). Its maximum is about \(1.06/\sqrt2\) near \(p\approx0.45\). The normalization should be stated.

## 4. Strictness

Strictness does not depend on the \(q\) formula. Kähler would force \(\Omega\) to be a \(W^+\)-eigenform. At \(p=1/2\) we have \(w_1\neq w_2\) and \(X_1X_2\neq0\), so \(\eta\neq0\) and \(J\) is not integrable.

Pointwise strictness on the whole interior follows from either of two facts:
- \(|\eta|^2>0\) on \((1/3,1)\), from the explicit formula;
- \(q=36(1-p^2)^3/(1+3p^2)^3>0\). This value checks at \(p=1/2\) and at the bolt value \(q=32/3\).

## 5. Proof route without numerics

Write \(\hat h_i=\sqrt G\,h_i=L_i/2\) and \(\hat W_i=\sqrt G\,W_i\). Then \(\hat W_i\) is rational: for example, \(A_1/(A_2A_3G)=(3p-1)^2(1-p)^4(1+p)^2/(256p^2)\) is a perfect square. Also \(d/dt=G^{-1/2}d/dp\).

After clearing a common denominator in \(p(1\pm p)(3p\pm1)(3p^2+1)\), each of the following becomes a polynomial identity in \(p\):
- the four Einstein equations;
- the two closure equations \(X_i'=2\mu_iX_i\);
- the two independent conditions \(E_i=0\).

Each identity can be proved by symbolic expansion, or by evaluation at more exact rational points than the degree of the cleared numerator. Unit length is already proved by hand.

This gives exact local existence on \(I\times\widetilde{SL}(2,\mathbb R)\) of a self-dual Einstein metric with \(\lambda=-3\) and a strictly AK, \(SL(2,\mathbb R)\)-invariant \(\Omega\). Neither the exact-point ODE argument nor the ideal is needed.

## 6. Ends of the manifold

**Far end \(p\to1\).** Exact asymptotics give \(\sqrt G\sim1/(\sqrt2(1-p))\). Hence \(t\sim-\tfrac1{\sqrt2}\ln(1-p)\), and the end is complete; the reported cutoff increments of about \(4.9\) match \(\ln 10^3/\sqrt2\).

The coefficients behave as follows:
- \(A_1\sim 8/(3(1-p))\), \(A_3\sim8/(1-p)\), \(A_2\sim32/(3(1-p)^2)\);
- hence \(h\to(1/\sqrt2,\sqrt2,1/\sqrt2)\), \(W_2\to1/\sqrt2\), and \(a_3/a_1\to\sqrt3\);
- the constraint closes as \(5/2+1/2=3\).

The growth is consistent with an asymptotically complex-hyperbolic (ACH) end with contact form \(\sigma_2\). Identifying it as ACH in the strict sense still needs a comparison with the Einstein ACH normal form, including the coefficient relation between \(\sigma_2^2\) and the Levi form \(2\sigma_3\wedge\sigma_1\).

**Bolt \(p\to1/3\).** Since \(\delta=t^2\cdot(\text{analytic in }t^2)\), every rational function analytic at \(p=1/3\) is even in \(t\). The metric conditions hold:
- \(A_1=t^2(1+O(t^2))\);
- \(A_2+A_3\) is even;
- \(A_2-A_3\propto(3p-1)^2=t^4\cdot\text{even}\).

This is exactly the weight-4 condition for the trace-free part, since \(\mathrm{ad}X_1\) has weight 2.

**Smoothness of \(\Omega\) at the bolt.** From \(L_{X_1}\sigma_2=-2\sigma_3\) and \(L_{X_1}\sigma_3=2\sigma_2\), the form \(\zeta=\sigma_2+i\sigma_3\) satisfies \(\zeta=e^{2i\psi}\zeta_0\). Also \(w=dt+it\sigma_1=e^{-i\psi}dz\), or \(e^{-i\psi}d\bar z\) with the other slice orientation; the result is the same either way.

The self-dual piece is \(\mathrm{Re}(w\wedge\zeta)=dt\wedge\sigma_2+t\,\sigma_3\wedge\sigma_1\), which has net weight 1. Its coefficient \(x_2\,e^{i\psi}\) with \(x_2=t\cdot\text{even}\) is smooth. The \((a_2-a_3)\) correction has weight 3 and coefficient \(O(t^5)=t^3\cdot\text{even}\). Finally, \(x_1=\sqrt{1-X_2}\) is even. So \(\Omega\) and \(J\) extend smoothly.

With opposite signs of \(n_2,n_3\), \(\Lambda^+\) would carry weight 3, and \(x_2\sim t\) would be singular. So the Spirit note was right that this has to be checked.

**Global group conditions.** The collapsing circle \(\exp(\theta X_1)\) must have period \(2\pi\), which holds in \(SL(2,\mathbb R)\) and fails in \(PSL\), where the bolt would be a \(\mathbb Z_2\) cone. In addition, \(\Gamma\) must lift to \(SL(2,\mathbb R)\) and must not contain \(-I=\exp(\pi X_1)\).

The resulting manifold is \(\Gamma\backslash(SL(2,\mathbb R)\times_{S^1}\mathbb R^2)\). This is the disk bundle of a square root of \(T\Sigma_g\), so the bolt has self-intersection \(\pm(g-1)\).

## 7. Points not decided by the files

**Novelty.** Armstrong 2002 (Crelle 542), the Apostolov–Drăghici survey, and self-dual Einstein Bianchi metrics are the relevant sources. Hitchin's Painlevé VI treatment is the \(SU(2)\) analogue. The rational, algebraic nature of this curve suggests identifying it with an algebraic Painlevé solution, but no supplied source does so. The phrase "the negative-scalar Goldberg statement fails locally" should wait for this comparison.

**Compact quotients.** The Spirit argument that compact quotients are impossible is correct but carries little content. \(q\) depends only on \(p\), and the manifold already contains a complete infinite end. It says nothing about closed AK Einstein manifolds.

**The integral identity \(\int(\cdots)\,dV=0\).** It is now unconditional once \(E_i\equiv0\) is proved. The integrand is finite at \(p=1\), with \(q\,dV/dp\to48\). Whether the identity reflects the compact AK balance or an accident of cancelling end fluxes requires computing the end flux explicitly. That computation is not in the files.