# Step 23 — The Yamabe identity: sharp conditional gap on hyperbolic blow-ups and the two-channel structure of marked cells

Conventions: \(P=\int|\mathrm{Ric}^\circ|^2\), \(S=\int s^2\), Weyl norms are curvature-operator norms,
\(R=\int|\mathrm{Ric}|^2=P+S/4\), \(\mathcal J=4P/R\), \(\mathcal E=\inf_\lambda\int|\mathrm{Ric}-\lambda g|^2/(\lambda^2V)=\mathcal J+\int(s-\bar s)^2/R\)
(`Skills/geometric-analysis/references/conventions-and-literature.md`). Same-metric Chern–Weil:
\(8\pi^2(2\chi+3\tau)=\int(4|W^+|^2-|\mathrm{Ric}^\circ|^2+s^2/12)\).

## 1. The conformal Yamabe identity (closed and relative)

Let \(g\) be a metric, \(\hat g=u^2g\), \(u>0\), with \(\hat s\equiv-24\), i.e.
\[
6\Delta_g u=s\,u+24u^3\qquad(\Delta=\operatorname{div}\nabla).\tag{1.1}
\]
Put \(\sigma=s+24\). Multiplying (1.1) by \(u\) and integrating,
\[
I:=\int(\sigma u^2+24u^4-24u^2)\,d\mu_g=-6\int|\nabla u|^2. \tag{1.2}
\]
The pointwise algebraic identity
\[
\frac{\sigma^2}{12}-4\sigma-48(u^4-1)+4(\sigma u^2+24u^4-24u^2)=\frac1{12}\bigl(\sigma+24(u^2-1)\bigr)^2
\]
and (1.2) give
\[
\int\Bigl(\frac{\sigma^2}{12}-4\sigma\Bigr)-48\int(u^4-1)
=\frac1{12}\int\bigl(\sigma+24(u^2-1)\bigr)^2+24\int|\nabla u|^2 .\tag{1.3}
\]
By (1.1), \(\sigma+24(u^2-1)=s+24u^2=6\Delta u/u\), so the first term on the right is \(3\int(\Delta u/u)^2\).

**Closed form (exact LeBrun identity).** On a closed manifold with Yamabe constant \(Y[g]<0\), let \(\hat g\) be the
Yamabe metric normalized to \(\hat s=-24\); then \(Y[g]^2=576\,\mathrm{Vol}(\hat g)\) and (1.3) reads
\[
\int s_g^2\,d\mu_g=Y[g]^2+36\int\Bigl(\frac{\Delta u}{u}\Bigr)^2+288\int|\nabla u|^2. \tag{1.4}
\]
This sharpens LeBrun's inequality \(\int s^2\ge Y[g]^2\) (equality iff \(s\) constant) to an identity. With
P scale-invariant and \(W^+\) conformally invariant this is equivalent to the identity found independently by S1003A01
(message #776): \(P(g)-P(\hat g)=24\int|\nabla u|^2+3\int(\Delta u/u)^2\).

**Relative form (marked cells).** Let \((U,g)\) be complete and exactly the \(\mathrm{Ric}=-6\) model (real hyperbolic
\(K=-2\), or complex hyperbolic, holomorphic curvature \(-4\)) outside a compact set, and let \(\hat g=u^2g\) be the
complete solution of (1.1) with \(u\to1\). On the exact exterior the linearization of (1.1) is \(6\Delta w=48w\); its
decaying radial solutions are \(w\sim e^{-4\sqrt2\,t}\) (H\(^4\), with volume growth \(e^{3\sqrt2t}\)) and
\(w\sim e^{-(2+2\sqrt3)t}\) (CH\(^2\), volume growth \(e^{4t}\)). All integrands in (1.3) are therefore integrable,
the boundary flux \(\oint u\partial_\nu u\to0\), and with \(B\) the model ball replaced by the cell,
\[
\int_{U_{\rm int}}\frac{s^2}{12}-48\,\mathrm{Vol}(B)
=48\,\mathrm{RV}(\hat g)+3\int\Bigl(\frac{\Delta u}{u}\Bigr)^2+24\int|\nabla u|^2,
\qquad
\mathrm{RV}(\hat g)=\bigl[\mathrm{Vol}_g(U_{\rm int})-\mathrm{Vol}(B)\bigr]+\int(u^4-1)\,d\mu_g. \tag{1.5}
\]
\(\mathrm{RV}(\hat g)\) is the renormalized volume of \(\hat g\) relative to the model for the **fixed marked end**
(the identification of the exterior with the model exterior is part of the data). In (1.5) the conformal integral
\(\int(u^4-1)\,d\mu_g\) runs over the **whole complete cell**, not only over \(U_{\rm int}\); \(U_{\rm int}\) and the model
ball \(B\) are matched truncations (same exterior cut). With this definition moving the cut through the exact end
changes neither \(\mathrm{RV}\) nor \(\Delta W_+\). (Step-24 repair.) Since \(W^+\) is conformally invariant, combining with
\(P_{\rm cell}-8\pi^2=4\Delta W_++[\int_{U_{\rm int}}s^2/12-48\mathrm{Vol}(B)]\) gives

**Theorem C (two-channel cell identity).** Let \(U\) be a complete marked cell of topology \((k,\ell)\) (i.e. \(D^4\#k\overline{\mathbb{CP}}^2\) with \(\ell\) handles), exactly equal to the
H\(^4\) or CH\(^2\) model outside a compact set for a fixed marking of the end, and let \(u\to1\) solve (1.1) with
\(u-1\) and its first two derivatives decaying faster than the inverse volume growth (\(e^{-3\sqrt2t}\) for H\(^4\), \(e^{-4t}\)
for CH; the rates above give this). Then, with the matched relative volume (1.5),
\[
P_{\rm cell}(g)-8\pi^2(k+4\ell)=4\Delta W_+ +48\,\mathrm{RV}(\hat g)+3\int\Bigl(\frac{\Delta u}{u}\Bigr)^2+24\int|\nabla u|^2,\tag{1.6}
\]
(the constant is \(8\pi^2\) for one blow-up)
and \(P_{\rm cell}(\hat g)-8\pi^2(k+4\ell)=4\Delta W_++48\,\mathrm{RV}(\hat g)\) exactly. The closed identity (1.4) is the
exact defect form of LeBrun's estimate; it is already implicit in LeBrun's 1996 Lemma 1 computation
\cite{lebrun1996four}, so its novelty here is the relative (cell) version and its use as a channel decomposition. In real-hyperbolic bulk
\(\Delta W_+=\int|W^+|^2\ge0\). Hence

- the H\(^4\) cell lower bound \(P_{\rm cell}\ge8\pi^2\) follows from the renormalized-volume comparison
  \(\mathrm{RV}(\hat g)\ge0\) for complete \(\hat s\equiv-24\) metrics on \(D\#k\overline{\mathbb{CP}}^2\) conformal to
  exact-H\(^4\)-collar metrics (a local, topological form of the hyperbolic Schoen volume question), and is equivalent
  to the statement \(\inf\{4\int|W^+|^2+48\mathrm{RV}(\hat g)\}\ge0\) over such \(\hat g\);
- in complex-hyperbolic bulk the Weyl channel \(4\Delta W_+\) has no sign and is the only possible saving channel if
  \(\mathrm{RV}\ge0\).

Existence of \(u\): for exact-H\(^4\) exteriors the cell is conformally compact and the Loewner–Nirenberg /
Aviles–McOwen / Andersson–Chruściel–Friedrich solution exists and is unique. **For exact-CH exteriors existence is now
unconditional** (S1003A01, `Sessions/S1003A01/workspace/notes/step22_exact_CH_conformal_reduction.md`, read and
checked in Step 24): piecewise weak barriers \(u_-=0\) on the core, \(1-e^{-a(r-R)}\) on the end, and \(u_+=M\) on the core,
\(1+(M-1)e^{-a(r-R)}\) on the end have the correct jump signs for \(-6\Delta\); exhaustion, Harnack positivity and a
maximum-principle comparison give a unique positive \(u\to1\) for **every** smooth exact-CH-ended cell, with no sign
condition on \(s\) (the spectral criticality \(6\lambda_0(CH^2)+s_{CH}=0\) is circumvented by the barriers). Bootstrapping
gives \(u-1=O(e^{-mr})\) with all derivatives for every \(4<m<2+2\sqrt3\). Consequently Theorem C holds for every
smooth exact-CH-ended cell, and the exact-ended \(J_6\) infimum equals the infimum of \(P\) over complete scalar \(-24\)
metrics asymptotic to the same marked CH end at a rate \(>4\).

## 2. Numerical evaluation of the channels (all diagonal cells available in both bulks)

Script `workspace/scripts/cell_yamabe_rv.py` (finite-volume Newton solve of (1.1) in \(z=\log x\) from the bolt to
\(x=10^{12}\); interior integrals by Simpson in \(q=\sqrt u\) with ball-density subtraction; every row run at
\(N=2000\) and \(4000\); the residual of (1.5) falls by \(\approx4\times\), i.e. it is the \(O(h^2)\) discretization error).
Data: `workspace/data/cell_yamabe_rv_h4.json`, `workspace/data/cell_yamabe_rv_ch_*.json`. Units: \(8\pi^2\).

| bulk | cell | \(P-1\) | \(4\Delta W_+\) | \(48\,\mathrm{RV}(\hat g)\) | \(Q=3\int(\Delta u/u)^2+24\int|\nabla u|^2\) |
|---|---|---|---|---|---|
| H4 | x0=.003,X=64 | .0060564 | .0000448 | .0059746 | .0000384 |
| H4 | x0=.01,X=64 | .0204669 | .0004287 | .0196932 | .0003408 |
| H4 | x0=.03,X=64 | .0630696 | .0032069 | .0573917 | .0024755 |
| H4 | x0=.1,X=64 | .2212945 | .0242920 | .1763832 | .0206208 |
| H4 | x0=.3,X=64 | .7138523 | .1198339 | .4646966 | .1293328 |
| H4 | x0=1,X=64 | 2.7837715 | .5616916 | 1.3830789 | .8390285 |
| H4 | x0=.03, J-opt | .0646201 | .0035830 | .0609064 | .0001296 |
| CH | x0=.003,X=64 | −.0002048 | −.0063926 | .0061871 | .0000001 |
| CH | x0=.01,X=64 | −.0012996 | −.0229953 | .0216969 | .0000005 |
| CH | x0=.03,X=64 (certified witness) | −.0041516 | −.0747382 | .0706363 | .0000018 |
| CH | x0=.05,X=128 | −.0037125 | −.1252945 | .1216119 | .0000034 |

Findings.

1. \(\mathrm{RV}(\hat g)>0\) in every cell of both bulks, including the certified cheap CH witness and H\(^4\) cells
   up to \(x_0=1\). In two CH cells the raw volume difference \(\mathrm{Vol}_g-\mathrm{Vol}(B)\) is negative
   (\(-3.4\times10^{-4}\) at \(x_0=.01\)); the conformal normalization restores positivity, so the relevant object is
   \(\mathrm{RV}(\hat g)\), not the raw volume.
2. **The cheap CH cell pays in renormalized volume and saves entirely in Weyl curvature.** At the certified witness,
   \(48\mathrm{RV}=+0.0706\), \(Q=2\times10^{-6}\), \(4\Delta W_+=-0.0747\). The scalar/volume channel is a cost in both
   bulks; the CH/H\(^4\) contrast lies in the Weyl channel alone.
3. **The two halves of \(\mathbf R^+=W^++\tfrac{s}{12}I\) in Theorem F are the two channels.** As \(x_0\to0\):
   \(48\mathrm{RV}/x_0=1.992,1.968,1.913\) (H\(^4\)) and \(2.062,2.170,2.355\) (CH) \(\to 2=-s_p/12\);
   \(4\Delta W_+/x_0=0.015,0.043,0.107\to0=W^+_p\) (H\(^4\)) and \(-2.131,-2.300,-2.491\to-2=-W^+_p(\zeta,\zeta)\) for the
   perpendicular CH direction. The quadratic terms scale like \(x_0^2\) (\(Q/x_0^2\approx4.3,3.4,2.8\) for H\(^4\)).
   In the Burns-gluing proof of Theorem F, the scalar flux \(4\pi^2x_0\) produces
   \(\Delta S/12=-8\pi^2x_0s_p/12+O(x_0^{6/5})\) and the self-dual flux \(\Phi_{++}=\pi^2\zeta\otimes\zeta\) produces
   \(4\Delta W_+=-8\pi^2x_0W^+_p(\zeta,\zeta)+O(x_0^{6/5})\); by (1.5), \(48\mathrm{RV}(\hat g)=\Delta S/12-Q\). The
   numerical \(Q=O(x_0^2)\) says that the first-order scalar response *is* the renormalized volume of the Yamabe
   representative. A proof of \(Q=o(x_0)\) for the Burns-glued metrics would make this a theorem
   (\(\sigma\approx24\) on a core of volume \(O(x_0^2)\), \(w=O(x_0)\) there; the estimate needed is an
   \(L^2\) bound on \(\nabla w\) at that scale).
4. The H\(^4\) Yamabe correction decays exactly at the real-hyperbolic mass order (\(\rho^4\)); its coefficient \(c\)
   (`decay_coeff_c`) is positive in every H\(^4\) cell (\(c/x_0\approx0.034\) for small cells), consistent with
   Chruściel–Delay positivity and Huang–Jang–Martin rigidity for \(\hat g\). The CH indicial root \(2+2\sqrt3\) is not
   tied to any mass order; no CH mass statement is drawn.

## 3. Hyperbolic blow-ups: exact Chern–Weil reduction to the Yamabe invariant

Let \(Y\) be a closed oriented real-hyperbolic four-manifold, \(X_k=Y\#k\overline{\mathbb{CP}}^2\),
\(Y_{\rm hyp}=Y[g_{\rm hyp}]<0\). Gauss–Bonnet for \(g_{\rm hyp}\) gives \(Y_{\rm hyp}^2/12=16\pi^2\chi(Y)\), and
\((2\chi+3\tau)(X_k)=2\chi(Y)-k\). Therefore, **for every metric** \(g\) on \(X_k\),
\[
P(g)=8\pi^2k+4\int|W^+|^2+\frac{S(g)-Y_{\rm hyp}^2}{12}. \tag{3.1}
\]
If \(Y[g]<0\), (1.4) refines this to
\[
P(g)=8\pi^2k+4\int|W^+|^2+\frac{Y[g]^2-Y_{\rm hyp}^2}{12}+3\int\Bigl(\frac{\Delta u}{u}\Bigr)^2+24\int|\nabla u|^2 .\tag{3.2}
\]
Kobayashi's connected-sum inequality (\(\overline{\mathbb{CP}}^2\) has positive Yamabe invariant) gives
\(Y(X_k)\ge Y(Y)\ge Y_{\rm hyp}\); \(Y(X_k)\) is nondecreasing in \(k\).

**Theorem H (sharp gap on hyperbolic blow-ups, conditional on one Yamabe identity).** Assume
\[
\mathcal Y(Y\#k\overline{\mathbb{CP}}^2)=Y_{\rm hyp}. \tag{H}
\]
((H) is the conjunction of Schoen's conjecture \(\mathcal Y(Y)=Y_{\rm hyp}\) and blow-up invariance
\(\mathcal Y(X_k)=\mathcal Y(Y)\); it implies (H) for every \(k'\le k\).) Then:

1. \(P(g)>8\pi^2k\) for every metric on \(X_k\), and \(\inf P=8\pi^2k\). The infimum is not attained.
2. In the \(\mathcal E\)-normalization, for \(1\le k\le2\chi(Y)\),
   \[
   \alpha(X_k)=\inf\mathcal E=\inf\mathcal J=\frac{4k}{k+6\chi(Y)},
   \]
   For \(1\le k<2\chi(Y)\) this value is not attained. At the endpoint \(k=2\chi(Y)\) the common infimum equals \(1\)
   (unconditionally, since \(\mathcal J\ge1\) there by (3.1)); attainment of \(\mathcal J=1\) is equivalent to an
   anti-self-dual metric on \(X_k\), attainment of \(\mathcal E=1\) additionally to constant scalar curvature, and the
   present argument does not exclude either. (Step-24 correction.)
3. Every \(P\)-minimizing sequence satisfies \(\int|W^+|^2\to0\), \(Y[g_j]\to Y_{\rm hyp}\),
   \(\int|\nabla u_j|^2+\int(\Delta u_j/u_j)^2\to0\): minimizing sequences become globally asymptotically
   half-conformally-flat and Yamabe-extremal. That the total \(8\pi^2k\) is carried as \(8\pi^2\) by each exceptional
   class is known only for the explicit Burns sequences; for an arbitrary minimizing sequence it requires a
   localization theorem that is not available. (Step-24 correction.)

*Proof.* (1) Under (H), \(Y[g]\le\mathcal Y(X_k)=Y_{\rm hyp}<0\) for every \(g\), so \(Y[g]^2\ge Y_{\rm hyp}^2\) and
(3.2) gives \(P\ge8\pi^2k\). Upper bound: Theorem F at \(k\) distinct points of \((Y,g_{\rm hyp})\), where
\(\mathbf R^+=-2I\) in the \(\mathrm{Ric}=-6\) scale, gives metrics with
\(P=8\pi^2k(1+2x_0)+O(kx_0^{6/5})\to8\pi^2k\). If \(P(g)=8\pi^2k\), equality in (3.2) forces \(\nabla u=0\), so \(g\)
has constant negative scalar curvature and \(Y[g]=\mathcal Y(X_k)\): \(g\) attains the Yamabe invariant
\(\sup_{[g]}\inf\). A metric attaining a nonpositive Yamabe invariant is Einstein (LeBrun \cite{lebrun1996four}, §2,
via the Schoen variational argument; equivalently it minimizes \(\int s^2\) over all metrics, Ishida–LeBrun
Prop. 12, and the Euler–Lagrange equation \(-2s\,\mathrm{Ric}+\tfrac12s^2g=0\) for constant \(s\ne0\) gives
\(\mathrm{Ric}=\tfrac s4g\)). Then \(P(g)=0<8\pi^2k\), a contradiction; strictness of \(P>8\pi^2k\) follows the same way.
Independently, Sambusetti's entropy theorem excludes Einstein metrics on \(X_k\).
(2) Write \(t=P/S\), so \(\mathcal J=16t/(4t+1)\) is increasing in \(t\). By (3.1),
\(t\ge\tfrac1{12}-8\pi^2(2\chi(Y)-k)/S\). For \(k\le2\chi(Y)\) the right side increases with \(S\), and
\(S\ge Y[g]^2\ge Y_{\rm hyp}^2=192\pi^2\chi(Y)\) (LeBrun's estimate and (H)) gives \(t\ge k/(24\chi(Y))\), i.e.
\(\mathcal E\ge\mathcal J\ge4k/(k+6\chi(Y))\). The Burns sequences have \(P\to8\pi^2k\), \(S\to Y_{\rm hyp}^2\) and
\(\int(s-\bar s)^2\to0\) (the scalar curvature differs from \(-24\) only on cores of volume \(O(x_0^2)\)), so
\(\mathcal E\to4k/(k+6\chi(Y))\). Non-attainment for \(k<2\chi(Y)\): equality forces \(P=8\pi^2k\), excluded by (1). At
\(k=2\chi(Y)\) the bound \(\mathcal J\ge1\) is attained exactly by anti-self-dual metrics (\(P-S/12=4\int|W^+|^2\) there),
which (1) does not exclude. (3) is read off from (3.2) and \(S\to Y_{\rm hyp}^2\). \(\square\)

**Unconditional content.** Without (H), put \(y_k=\mathcal Y(X_k)^2/Y_{\rm hyp}^2\in[0,1]\) (with \(y_k=0\) if
\(\mathcal Y(X_k)\ge0\)). The same argument gives, for every metric,
\[
P\ge8\pi^2k-\frac{(1-y_k)Y_{\rm hyp}^2}{12},\qquad
\frac{P}{S}\ge\frac{2\chi(Y)y_k-(2\chi(Y)-k)}{24\chi(Y)y_k}\quad(k\le2\chi(Y)),
\]
while Theorem F gives \(\inf P\le8\pi^2k\) and \(\alpha(X_k)\le4k/(k+6\chi(Y))\). Thus on hyperbolic blow-ups the
lower-bound problem is controlled by the Yamabe invariant: \(\alpha(X_k)>0\) whenever \(y_k>1-k/(2\chi(Y))\);
\(y_k=1\) is **sufficient** for the sharp value \(\inf P=8\pi^2k\) (the Yamabe lower estimate then meets the Burns upper
estimate) but is not proved necessary, since for \(y_k<1\) the decomposition does not exclude compensation by the
Weyl and conformal-square terms; any shortfall below \(8\pi^2k\) is at most \((1-y_k)\cdot16\pi^2\chi(Y)\). For
\(k>2\chi(Y)\), (3.1) gives \(P-S/12\ge8\pi^2(k-2\chi(Y))>0\), so \(\mathcal E\ge\mathcal J>1\) **pointwise**, but conformal
inflation (\(S\to\infty\) in a fixed conformal class with \(W^+\) fixed) gives \(\inf\mathcal J=1\); there is no uniform
separation of \(\mathcal J\) above one, and \(\inf\mathcal E\) is only known to lie between \(1\) and the Burns value
\(4k/(k+6\chi(Y))\). (Step-24 correction.)

**Relation to Theorem H\(_\varepsilon\).** H\(_\varepsilon\) (Step 22) is the pointwise-Ricci shadow: under
\(\mathrm{Ric}\ge-3(1+\varepsilon)g\), BCG entropy plus Bishop supplies the volume comparison that (H) supplies for
every metric. The dimension-four difficulty on this family is located in the Yamabe invariant: (H) is the only missing
input, and no \(L^2\)-regularity question remains once it is available.

Status of (H): the retrieved sources (LeBrun 1996, Ishida–LeBrun, Akutagawa–Botvinnik–Kobayashi–Seshadri,
Kotschick's survey, `Differentiable rigidity...`) compute \(\mathcal Y\) for Seiberg–Witten/Bauer–Furuta-supplied
families and record the three-dimensional Perelman result; none proves Schoen's conjecture or blow-up invariance for
closed real-hyperbolic four-manifolds. The Brendle–Chodosh asymptotically hyperbolic volume comparison was not
retrieved by this Step's request. (H) is therefore recorded as the single open hypothesis.

## 4. What this changes

- The scalar side of both the closed and the cell problems is now an exact identity rather than an inequality; the
  only non-sign-definite terms are \(\Delta W_+\) and a renormalized/Yamabe volume.
- The CH/H\(^4\) contrast is completely located: identical positive volume cost \(\approx-x_0s/12\), opposite Weyl
  response \(-x_0W^+(\zeta,\zeta)\). **Superseded target (Step 24):** a linear trade-off
  \(4\Delta W_+\ge-\Lambda\cdot48\mathrm{RV}-\eta\) is not a usable lower-bound target. In the CH kernel direction Theorem F
  forces the two channels to cancel at first order, so the measured \(\Lambda\in[1.03,1.06]\) tends to \(1\) and
  \(\Lambda-1\) is a second-order Weyl excess; and \(\Lambda>1\) gives no absolute bound without an upper bound on RV. The
  correct cell problem is absolute:
  \(\inf\{8\pi^2+4\Delta W_++48\mathrm{RV}(\hat g)\}>0\) over complete scalar \(-24\) metrics asymptotic to the marked
  standard CH end on \(O(-1)\). The certified cheap cells delete only \(\Delta W_+\approx-1.5\) of self-dual Weyl energy,
  whereas a zero-cost cell with \(\mathrm{RV}\ge0\) must delete at least \(2\pi^2\approx19.7\) (relative signature
  \(\Delta W_+-\int|W^-|^2=-12\pi^2\)); they are perturbative Burns bubbles far from the zero-cost regime, so positivity
  of \(p_{1,0}\) is a compactness-and-degeneration statement, not a profile optimization.
- For H\(^4\) cells, \(\mathrm{RV}(\hat g)\ge0\) (all tested cells positive, with first-order value \(x_0/24\)) is the
  precise local statement; it is a topological, asymptotically-hyperbolic analogue of the closed problem (H).
