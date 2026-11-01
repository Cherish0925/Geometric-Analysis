# Step 48 — The Yamabe channel of the blow-up saving, and localized complex-hyperbolic coercivity

Session S1003A02, Agent2, Execute. Scripts/data:
`workspace/scripts/step48_theoremY.py` → `workspace/data/step48_theoremY.json` (exact field-sup formula, Ψ, sharp constant);
`workspace/scripts/step48_lemmaP.py` → `workspace/data/step48_lemmaP.json` (independent brute-force optimisation of the saving density);
`workspace/scripts/step48_bianchi_indicial.py` → `workspace/data/step48_bianchi_indicial.json` (indicial roots of SU(2)-invariant Einstein tails on \(\mathbb{CH}^2\)).

Setting throughout: \(X\) minimal of general type, \(A=c_1^2(X)\), \(M=X\#k\overline{\mathbb{CP}}^{\,2}\), the all-metric sign-family hypotheses of Theorems N/W/K (b⁺≥2, or the chamber hypotheses recorded in package §3.6). \(\hat g\) is the Yamabe representative of \([g]\) normalised to \(s\equiv-4\), \(\hat V=\operatorname{Vol}(\hat g)\), so \(Y[g]^2=16\hat V\). \(P(g)\ge P(\hat g)\). Norms on \(\Lambda^+\) are endomorphism norms; the scalar-\(-4\) Kähler orbit \(\mathcal K\) has spectrum \((-\tfrac23,\tfrac13,\tfrac13)\), \(|W_*|^2=\tfrac23\).

---

## 1. The saving density depends only on \((\mu_{\min}(W^+),|W^+|)\)

Theorem K used the pointwise density (field amplitude \(r=\rho\in[0,2]\), direction \(n\))
\[
f(W,r,n)=r^2M(n,n)-4|M|^2+p(r),\qquad M=W-\tfrac{r^2}{4}\bigl(\tfrac I3-nn^{T}\bigr),\qquad p(r)=\tfrac{(2-r)(r-1)(3r+2)}3 .
\]
**Proposition 48.1 (exact).** For every traceless symmetric \(W\) and unit \(n\),
\[
f(W,r,n)=-r^2\,W(n,n)-4|W|^2+p(r).
\]
*Proof.* \(M\) is traceless, so \(M(n,n)=-\langle M,P_n\rangle\) with \(P_n=I/3-nn^T\), \(|P_n|^2=\tfrac23\). Then \(\langle M,P_n\rangle=\langle W,P_n\rangle-r^2/6\) and \(|M|^2=|W|^2-\tfrac{r^2}{2}\langle W,P_n\rangle+\tfrac{r^4}{24}\); substitution cancels the \(r^4\) terms and gives \(r^2\langle W,P_n\rangle-4|W|^2+p\), and \(\langle W,P_n\rangle=-W(n,n)\). (Symbolic residual 0 in the script.) ∎

Hence, with \(x:=-\mu_{\min}(W)\ge0\) and \(p(r)=-r^3+\tfrac73r^2-\tfrac43\),
\[
\sup_{r\in[0,2],\,|n|=1}f(W,r,n)=\varphi(x)-4|W|^2,\qquad
\varphi(x)=\begin{cases}\tfrac12 r_*^3-\tfrac43,& r_*=\tfrac{6x+14}{9},\ 0\le x\le\tfrac23,\\[2pt] 4x,& x\ge\tfrac23,\end{cases}
\]
the optimum being \(n=\) the \(\mu_{\min}\)-eigenvector and \(r=\min(r_*,2)\). \(\varphi\) is \(C^1\) at \(x=2/3\) (\(\varphi=8/3\), \(\varphi'=4\)). The constraint \(r\le2\) is the maximum principle \(|\Phi|^2\le-s=4\).

Consequences. (a) Theorem K's sharp constant is recovered at once: along the magnitude direction, spectrum \((-x,x/2,x/2)\), \(\varphi(x)-6x^2\) has slope \(-4\) in \(x\) at \(x=2/3^-\) and \(\operatorname{dist}=\sqrt{3/2}\,|x-\tfrac23|\), so \(C_{\mathcal K}=4/\sqrt{3/2}=4\sqrt6/3\). (b) **All directional information in Theorem W's pointwise content is the lowest eigenvalue of \(W^+\).** The rank-one/eigenline structure of \(W^+\) enters only through \(\mu_{\min}\); the splitting of the upper pair enters only through \(|W^+|^2\).

## 2. Theorem Y: the linear saving channel is the Yamabe excess

Write \(D_W:=\int_M(\tfrac23-|W^+_{\hat g}|^2)\,d\mu_{\hat g}\) (Weyl-energy deficit below the Kähler value) and \(\Delta V:=\hat V-2\pi^2A=(Y[g]^2-32\pi^2A)/16\) (Yamabe excess over LeBrun's invariant \(\mathcal Y(M)^2=32\pi^2A\)). The closed identity \(C_+=A-k+P/8\pi^2\) at \(s\equiv-4\) reads exactly
\[
8\pi^2k-P(\hat g)=4D_W-4\Delta V .\tag{Y0}
\]
Define the pointwise orbit penalty
\[
\Psi(W):=\tfrac43+2|W|^2-\varphi(-\mu_{\min}(W))\ \ (=2(\tfrac23-|W|^2)-\sup f).
\]
**Lemma 48.2.** \(\Psi\ge0\), \(\Psi=0\) exactly on \(\mathcal K\), and \(\Psi(W)\ge\tfrac{10}{9}\operatorname{dist}(W,\mathcal K)^2\), the constant \(10/9\) being sharp (approached along the magnitude-deficit direction \(x\uparrow2/3\)).
*Proof (exact eigenvalue algebra; TTCS-verified).* Write the spectrum as \((-x,\tfrac x2-\sigma,\tfrac x2+\sigma)\), so \(|W|^2=\tfrac32x^2+2\sigma^2\) and \(\operatorname{dist}^2=\tfrac32(x-\tfrac23)^2+2\sigma^2\). Then exactly
\[
\Psi=\tfrac53h^2+\tfrac4{27}h^3+4\sigma^2\ \ (h=\tfrac23-x\ge0),\qquad \Psi=3t^2+4\sigma^2=2\operatorname{dist}^2\ \ (t=x-\tfrac23\ge0),
\]
so \(\Psi-\tfrac{10}9\operatorname{dist}^2=\tfrac4{27}h^3+\tfrac{16}9\sigma^2\), resp. \(\tfrac43t^2+\tfrac{16}9\sigma^2\), both \(\ge0\); along \(\sigma=0\), \(\Psi/\operatorname{dist}^2=\tfrac{10}9+\tfrac8{81}h\to\tfrac{10}9\) (an infimum, not attained off \(\mathcal K\)). Since \(\operatorname{dist}^2=\tfrac32(x-\tfrac23)^2+2\sigma^2\) (Hoffman–Wielandt, sorted eigenvalues), the limiting ratios at the orbit are \((5/3)/(3/2)=10/9\) for \(x<2/3\), \(3/(3/2)=2\) for \(x>2/3\), and \(4/2=2\) for splitting; away from the orbit the ratio is larger (e.g. \(W=0\): \(\Psi=0.7846\), \(\operatorname{dist}^2=2/3\), ratio \(1.177\); as \(|W|\to\infty\), ratio \(\to2\)). (The numerical scan agrees; its values marginally below \(10/9\) are cancellation error. The brute-force file `step48_lemmaP.json` is not valid corroboration: its Nelder–Mead steps left \(r\le2\).) ∎

**Theorem Y.** Under the sign-family hypotheses, for every metric \(g\) on \(M\),
\[
\boxed{\;8\pi^2k-P(g)\ \le\ 8\pi^2k-P(\hat g)\ \le\ 4\Delta V-2\int_M\Psi(W^+_{\hat g})\,d\mu_{\hat g}\ \le\ \frac{Y[g]^2-32\pi^2A}{4}-\frac{20}{9}\int_M\operatorname{dist}(W^+_{\hat g},\mathcal K)^2d\mu_{\hat g}.\;}
\]
*Proof.* Averaging Theorem W over the sign family and dropping its nonpositive \(\zeta\)/Walsh terms gives \(8\pi^2k-P(\hat g)\le\int\sup f=2D_W-\int\Psi\) (Prop. 48.1). Eliminate \(D_W\) with (Y0): \(8\pi^2k-P\le\tfrac12(8\pi^2k-P+4\Delta V)-\int\Psi\). ∎

*Relation to LeBrun.* LeBrun's Proposition 4 (`Knowledge/objects/papers/math-0111228-…/object.md`, line 148), \(\int(s-\sqrt6|W^+|)^2\ge72\pi^2(a^+)^2\), applied with the sign \(a=K_X+\sum\varepsilon_iE_i\) maximising \((a^+)^2\ge A\) (averaging gives \(\mathbb E|a_\varepsilon^-|^2=|K_X^-|^2+\sum|E_i^-|^2\ge k\)), yields in the same variables, with \(u=\sqrt6|W^+|-2\),
\[
8\pi^2k-P(\hat g)\le4\Delta V-\tfrac49\int u^2 .\tag{Y-LeB}
\]
Retaining the period term (TTCS step48 verifier 1): with \(\Pi_g:=(a^+)^2-A\ge Q_{\rm per}:=|K_X^-|^2+\sum_i|E_i^+|^2\) (harmonic parts for \([g]\)),
\[
8\pi^2k-P(\hat g)\le4\Delta V-\tfrac49\int(\sqrt6|W^+|-2)^2-16\pi^2\Pi_g,\qquad \Delta V\ge2\pi^2\Pi_g\ \text{(LeBrun's scalar estimate)}.\tag{LeB\(_{\rm full}\)}
\]
So the leading statement "saving \(\le4\times\)Yamabe excess" is LeBrun's mixed estimate rewritten through (Y0); at fixed \(\Delta V\), open exceptional periods *reduce* the admissible saving. Theorem Y adds what LeBrun's \(|W^+|\)-only estimate cannot see: the orbit penalty \(4\sigma^2\) on splitting of the degenerate pair (to which (Y-LeB) is blind at quadratic order, since \(u=O(\sigma^2)\)), and a stronger penalty on excess magnitude (\(\tfrac13(3x-2)^2\cdot2\) vs \(\tfrac49(3x-2)^2\)). On the saving side \(x<2/3\) (magnitude deficit) (Y-LeB) is the stronger: \(\tfrac49u^2=4h^2\) against \(2\Psi=\tfrac{10}3h^2\). Both hold simultaneously.

**Corollary Y1 (necessary Yamabe excess).** If \(P(g)\le8\pi^2ck\), then
\[
Y[g]^2\ \ge\ 32\pi^2\bigl(A+(1-c)k\bigr)+\tfrac{80}{9}\int\operatorname{dist}(W^+_{\hat g},\mathcal K)^2 ,
\qquad\text{i.e. }\ \Delta V\ge2\pi^2(1-c)k .
\]
Every subunit family lives in conformal classes whose Yamabe constant lies a definite amount below LeBrun's \(\mathcal Y(M)=-4\pi\sqrt{2A}\): \(|Y[g]|\ge4\pi\sqrt{2(A+(1-c)k)}\). For the certified coefficient, \(\Delta V\ge0.085614\) per exceptional class (same number as the depletion bound \(L\)). This is the quantitative, class-dependent non-attainment form of LeBrun's Yamabe theorem that a subunit family must exhibit.

**Corollary Y2 (where Theorem K sits).** The only first-order channel of Theorem W is the magnitude deficit \(4E(\hat\omega,\hat\omega)=2(\tfrac23-|W^+|^2)+2|E|^2\); by (Y0) its integral is \(2D_W=\tfrac12(8\pi^2k-P)+2\Delta V\). Thus Theorem K's linear \(L^1\) requirement is a consequence-level shadow; the governing unknown is the pair \((D_W,\Delta V)\), and a tariff \(P(\hat g)\ge8\pi^2ck\) (equivalently, as a statement over all metrics, \(\inf P\ge8\pi^2ck\)) is *equivalent* (by (Y0)) to \(D_W-\Delta V\le2\pi^2(1-c)k\). Theorem Y gives \(D_W-\Delta V\le\Delta V-\tfrac12\int\Psi\): the Weyl deficit can exceed the Yamabe excess by at most the Yamabe excess.

**Checks against the mandatory objects.**
* *KE ball quotient* (\(k=0\)): \(\Delta V=0\), \(\Psi\equiv0\), equality.
* *Certified perpendicular cell* (corrected Step-49 Yamabe ledger; floating except for the pre-existing interval certificate for \(P\)): in units divided by \(8\pi^2\), \(1-P(\widehat g)=0.0043391\), \(\Delta V=0.053096\), the conformal Weyl deficit is \(\delta W=0.018784\), and \(D_W=\delta W+(2/3)\Delta V\simeq0.05418\). Hence \(4D_W\simeq0.21672\), \(4\Delta V\simeq0.21238\), with their difference equal to the saving. The previously displayed \(0.07513\) and \(0.07080\) were instead \(4\delta W\) and \((4/3)\Delta V\). Step 49 computes \(\int\Psi/(8\pi^2)=0.01323261\), so \(2\int\Psi/(8\pi^2)=0.0264652\). The correct Theorem-Y allowance is \(4\Delta V-(1-P(\widehat g))\simeq0.2081\); the earlier \(0.0332\) number was another consequence of the channel misidentification and is withdrawn. The closed theorem still requires a genuine closed replica and its actual sign-family fields; the isolated cell measurement is a consistency test. The strict saving is a small difference of much larger Weyl and relative-volume channels.
* *Formal common mode* (\(h=k/A\), \(r=2-h\), axial \(x=\tfrac23-h\), \(\hat V=8\pi^2A/(2-h)^2\)): in units \(8\pi^2k/(2-h)^2\), LHS \(=4-5h\), \(4\Delta V=4-h\), \(2\int\Psi=\tfrac{10}3h+\tfrac8{27}h^2\), RHS \(=4-\tfrac{13}3h-\tfrac8{27}h^2\). Slack \(\tfrac23h-\tfrac8{27}h^2\), i.e. \(O(k^2/A)\): the formal mode saturates Theorem Y to leading order. Its saving is financed by \(\Delta V\approx2\pi^2k\), not by Weyl. (Its amplitude \(2-h\) differs from the pointwise optimum \(2-\tfrac23h\); that is the slack.) With \(u=-3h\), \(\tfrac49\int u^2/\mathcal U=4h\), so **the formal mode saturates (Y-LeB) exactly**; equality in (LeB\(_{\rm full}\)) forces \(\Pi_g=0\), i.e. null exceptional periods — precisely what Lemma T forbids for an exact closed mode. The LeBrun equality class and the Taubes obstruction therefore meet at the formal common mode.
* *Rotated (conformally symplectic) cells*: Theorem Y is a statement about the smooth Yamabe representative of \([g]\) and is insensitive to the degenerate almost-Kähler representative of Step 46.V/47. (Only continuity and persistence of strict subthreshold cost are established for that family; agreement of \(P,\Delta V,W^+\) with the diagonal cell to \(O(\psi^2)\) is not established.)

So the strategist's conformal-class formulation is now exact: every lower-bound attempt for O11 must bound the Weyl deficit of the Yamabe representative by its Yamabe excess with a factor better than \(1+(\text{const})k/\Delta V\); fields give factor 2 (Theorem Y), LeBrun gives factor 2 on magnitude, and neither can do better pointwise because the formal common mode saturates both.

## 3. Localized complex-hyperbolic coercivity (Riemannian, no field selection)

Normalisation \(\operatorname{Ric}_0=-6g_0\) on a closed ball quotient \(X_0=\Gamma\backslash\mathbb{CH}^2\) (holomorphic curvature \(-4\)); \(L:=\tfrac12(\nabla^*\nabla-2\mathring R)\) on \(S^2T^*X_0\), so that in Bianchi/DeTurck gauge with \(s\equiv-24\), \(\operatorname{Ric}(g_0+h)+6(g_0+h)=\operatorname{Ric}^\circ_{g_0+h}=Lh+Q(h)\), \(|Q|\le C(|h||\nabla^2h|+|\nabla h|^2)\) (Step 46 §3).

**Proposition 48.3 (global gap, every quotient).** \(\langle Lu,u\rangle\ge\|u\|^2\) for all \(u\in H^2(S^2T^*X_0)\), for every \(\Gamma\).
*Proof.* \(L^2S^2=TT\oplus\overline{\operatorname{im}T}\), \(T(X,f)=\delta^*X+fg\), since \(T^*h=(\delta h,\operatorname{tr}h)\) up to constants. On an Einstein manifold \(\Delta_L\delta^*=\delta^*\Delta_H\) and \(\Delta_L(fg)=(\Delta f)g\); with \(L=\tfrac12\Delta_L+6\) this gives \(LT=TD\), \(D=\operatorname{diag}(\tfrac12\Delta_H+6,\ \tfrac12\Delta_0+6)\ge6\). \(T^*T\) has entries \(\delta\delta^*\) (a function of \(\Delta_H\) and \(d\delta\)), \(4\), and \(\mp d,\mp\delta\), all of which intertwine \(\Delta_0,\Delta_H\); hence \([T^*T,D]=0\) and \(\langle LTw,Tw\rangle=\langle T^*TDw,w\rangle\ge6\|Tw\|^2\). On TT, Koiso's identity (Step 44 G1) gives \(\langle Lh,h\rangle=\tfrac12\|d^\nabla h\|^2+\tfrac12\langle(6-\mathring R)h,h\rangle\ge\|h\|^2\) since \(\mathring R\le4\). Both summands are \(L\)-invariant (self-adjointness). Only \(\Delta_H,\Delta_0\ge0\) were used, so no small eigenvalue of the quotient (e.g. \(b_1\neq0\)) enters. ∎

**Proposition 48.4 (Combes–Thomas).** For Lipschitz \(\phi\) with \(|d\phi|\le a<\sqrt2\): \(\|e^{\phi}L^{-1}e^{-\phi}\|_{L^2\to L^2}\le(1-a^2/2)^{-1}\).
*Proof.* For real \(u\), \(\langle e^{\phi}\nabla^*\nabla(e^{-\phi}u),u\rangle=\|\nabla u\|^2-\int|d\phi|^2|u|^2\) exactly, so \(\langle e^\phi Le^{-\phi}u,u\rangle\ge(1-a^2/2)\|u\|^2\). ∎

**Theorem 48.L (localized coercivity).** Let \(B\subset X_0\) be any closed set (e.g. a union of \(k\) balls, no separation assumed), \(\tilde d\) a smoothed distance to \(B\) (\(|\tilde d-d|\le C_\eta\), \(|\nabla\tilde d|\le1+\eta\), \(|\nabla^2\tilde d|\le C_\eta\); built equivariantly on \(\mathbb{CH}^2\)), and let \(g\) be a metric with \(s_g\equiv-24\) on a region identified with \(\{\tilde d\ge\tfrac12\}\) such that \(h=g-g_0\) is **assumed** to be in (nonlinear DeTurck/Bianchi) gauge there and \(\|h\|_{C^{2,\alpha}_{ul}}\le\varepsilon\). (Producing this gauge on a region with boundary is a separate matter: the harmonic-map Jacobi operator \(\nabla^*\nabla+6\) is coercive, but uniform boundary regularity of level sets must be arranged, or the metric extended to \(X_0\) and the Step-46 global gauge used.) The remainder obeys \(|Q|\le C(|h||\nabla^2h|+|\nabla h|^2+|h|^2)\). For every \(a<\sqrt2\) there are \(\varepsilon_0,C\) depending only on \(a\) and model constants (not on \(\Gamma\), \(B\), \(k\)) such that for \(\varepsilon\le\varepsilon_0\), \(T\ge2\):
\[
\|h\|_{H^2(d\ge T)}\le C\bigl(\|\operatorname{Ric}^\circ_g\|_{L^2(d\ge1)}+e^{-aT}\Lambda\bigr),\qquad \Lambda:=\|h\|_{H^1(1\le d\le2)} .
\]
*Proof.* Let \(\chi\) cut off (0 for \(d\le1\), 1 for \(d\ge2\)) and extend \(\chi h\) by 0 to \(X_0\). Then \(L(\chi h)=\chi(\operatorname{Ric}^\circ-Q)+[L,\chi]h\), with \([L,\chi]h=-\nabla_{\nabla\chi}h+\tfrac12(\Delta\chi)h\) supported in the layer. Split \(\chi h=h_1+h_2\), \(h_1=L^{-1}(\chi\operatorname{Ric}^\circ)\) (\(\|h_1\|_{H^2}\le C\|\operatorname{Ric}^\circ\|\) by 48.3 and model elliptic estimates), \(Lh_2=-\chi Q+[L,\chi]h\). With \(\phi=a\min(d,T)\), Prop. 48.4 plus weighted elliptic regularity (\(|d\phi|\le a\)) give \(\|e^\phi h_2\|_{H^2}\le C(e^{2a}\Lambda+\varepsilon\|e^\phi\chi h\|_{H^2})\), and \(\|e^\phi h_1\|_{H^2}\le e^{aT}C\|\operatorname{Ric}^\circ\|\); absorb \(\varepsilon\|e^\phi h_2\|_{H^2}\). Multiply by \(e^{-aT}\) on \(\{d\ge T\}\). ∎

The Combes–Thomas rate \(\sqrt2\) is not the true tail rate. The actual Einstein tails, computed in the SU(2)-invariant (diagonal Bianchi IX) sector about \(dr^2+\sinh^2r(\sigma_1^2+\sigma_2^2)+\sinh^2r\cosh^2r\,\sigma_3^2\) (script; exponents of \(|h|_g\sim e^{-\nu r}\)):

| mode | indicial roots \(\nu\) (all four Einstein equations imposed) |
|---|---|
| triaxial \(a=-b\) (J-anti-invariant, complex-structure / CR deformation) | \(0\) (CR change at infinity, cf. Theorem E's Rossi parameter), **\(4\)** |
| U(2) squashing \(a=b\), \(c\) | \(-2\) (growing), \(0\) (radial translation), \(6\) |

(The spatial-equation determinant in the data file also has \(\nu=8\); it violates the \(E_{00}\) constraint, \((-48,-48,-32)\cdot(1,1,2)=-160\neq0\), and is spurious.)

Volume grows like \(e^{4r}\). Hence, in the diagonal SU(2)-invariant sector: the U(2) (magnitude) tail decays like \(e^{-6r}\) and is \(L^1\)-summable — its effect on \(D_W\) and \(\Delta V\) is localized at the core; the J-anti tail decays at exactly the marginal rate \(e^{-4r}\). By the \(1\leftrightarrow2\) axis symmetry (\(q\mapsto-q\)) at constant scalar curvature, \(\mu_{\min}\) and \(|W^+|^2\) change only at \(O(q^2)\). Step 49 computes the missing first-order split: for \(A=\sinh r(1+\varepsilon e^{-4r})\), \(B=\sinh r(1-\varepsilon e^{-4r})\), \(C=\sinh r\cosh r\), \(e^{4r}\partial_\varepsilon W^+|_0\to\operatorname{diag}(-12,12,0)\) at \(\operatorname{Ric}=-6\). At scalar \(-4\), \(\sigma=2|\varepsilon|e^{-4r}+O(|\varepsilon|e^{-6r})+O(\varepsilon^2e^{-8r})\), so Theorem K has a marginal linear tail whereas \(\Psi=16\varepsilon^2e^{-8r}+O(\varepsilon^2e^{-10r})\) is integrable. Indicial spectra outside the diagonal SU(2) ansatz are not computed.

**Lemma 48.5 (bulk volume is quadratic).** In the setting of 48.L, with \(\Omega=\{d\ge1\}\) and outward normal \(\nu\),
\[
\operatorname{Vol}_g(\Omega)-\operatorname{Vol}_{g_0}(\Omega)=\tfrac1{24}\oint_{\partial\Omega}\partial_\nu\operatorname{tr}h+O\bigl(\|h\|^2_{H^2(\Omega)}\bigr).
\]
*Proof.* \(s'_{g_0}(h)=\Delta\operatorname{tr}h+\delta\delta h-\langle\operatorname{Ric}_0,h\rangle\) (Besse 1.174, \(\Delta=\delta d\)); Bianchi gauge \(\delta h=-\tfrac12d\operatorname{tr}h+O(h\nabla h)\) gives \(s'(h)=\tfrac12(\Delta+12)\operatorname{tr}h+\delta O(h\nabla h)\). Since \(s_g=s_0\), \(\tfrac12(\Delta+12)\operatorname{tr}h=Q_s\), \(|Q_s|\le C(|h||\nabla^2h|+|\nabla h|^2)\). Integrate over \(\Omega\) (\(\int_\Omega\Delta f=-\oint\partial_\nu f\)) and use \(d\mu_g=(1+\tfrac12\operatorname{tr}h+O(|h|^2))d\mu_0\). ∎

**Theorem 48.LY (near-CH reduction of O11 to cores).** Assume the sign-family hypotheses, that \(X\) itself is a ball quotient \(X_0=\Gamma\backslash\mathbb{CH}^2\) (so \(\operatorname{Vol}(X_0,\hat g_0)=2\pi^2A\) with \(\hat g_0=6g_0\) at \(s=-4\); for a different reference quotient the term \(-8\pi^2(c_1^2(X_0)-A)\) must be retained), and that \(\tilde g=\hat g/6\) satisfies the hypotheses of 48.L on \(F(\{\tilde d\ge1/2\})\subset M\). Put \(\Omega_2=\{\tilde d\ge2\}\), \(U_2=M\setminus F(\Omega_2)\) (enlarged cores), and define the marked core Yamabe excess at \(s=-4\),
\[
\Delta V_{U}:=\operatorname{Vol}_{\hat g}(U_2)-\operatorname{Vol}_{\hat g_0}(\{\tilde d<2\})+\tfrac14\oint_{\tilde d=2}\partial_{\hat\nu_0}\operatorname{tr}_{\hat g_0}(\hat g-\hat g_0)
\]
(\(=36\times\) the \(s=-24\) quantity with coefficient \(1/24\)); for exact-CH collars it is the relative volume of Theorem C. It depends on the marking, gauge and interface germ. Then, with \(C\) independent of \(\Gamma,k,B\),
\[
\boxed{\;8\pi^2k-P(g)\le4\Delta V_U-\tfrac{20}9\int_{U_2}\operatorname{dist}(W^+,\mathcal K)^2+C\bigl(P(g)+\Lambda^2\bigr),\qquad
P(g)\ \ge\ \frac{8\pi^2k-4\Delta V_U-C\Lambda^2}{1+C}.\;}
\]
*Proof.* Theorem Y with \(\Delta V=\Delta V_U+[\operatorname{Vol}_{\hat g}(\Omega_2)-\operatorname{Vol}_{\hat g_0}(\Omega_2)-\tfrac14\oint\partial_\nu\operatorname{tr}]\), Lemma 48.5 (rescaled), and Theorem 48.L applied with nested cutoffs so that \(\|h\|^2_{H^2(\Omega_2)}\le C(P+\Lambda^2)\), \(\Lambda\) the \(H^1\) norm on the transition layer \(\{1\le\tilde d\le2\}\); drop the bulk part of \(\int\Psi\ge0\); use \(P(\hat g)\le P(g)\). (Statement and repairs verified in `trace/ttcs/results/step48_ttcs01_verifier2_integration.md`.) ∎

Meaning. In the regime where the Yamabe representative is uniformly-locally \(C^{2,\alpha}\) close to a ball quotient away from enlarged cores, **a per-class tariff holds unless the cores carry a total Yamabe/relative-volume excess of order \(2\pi^2(1-c)k\), or the collars carry quadratic mismatch \(\Lambda^2\gtrsim k\).** Diffuse bulk saving is not merely quadratically priced (as \(A_C\) gave for the canonical branch) but absent at linear order, and this needs no branch selection: only Theorem W's field-averaged pointwise bound and LeBrun's Yamabe value. The certified cell is consistent: its saving is the near-cancellation \(4D_{W,U}-4\Delta V_U\) of two order-\(0.07\) core quantities.

What this does not do. It does not bound \(\Delta V_U\) for a core; it does not apply when the bulk is far from every ball quotient (the formal common mode lives there, with \(\Delta V\approx2\pi^2k\) diffuse); it does not treat hosts that are not ball quotients (general-type \(X\) with \(c_1^2<3c_2\)) — there the reference is not Einstein-rigid and Theorem 48.L has no model.

## 4. Consequences for the program

1. The two-scale conjecture's lower side is now precisely: *bound \(D_W-\Delta V\) on the Yamabe representative.* Equivalently (Y0): \(P=8\pi^2k+4\Delta V-4D_W\). Fields bound \(D_W\le2\Delta V-\tfrac12\int\Psi\). A tariff needs \(D_W\le\Delta V+2\pi^2(1-c)k\).
2. Corollary Y1 gives a conformally invariant necessary condition that any construction with \(c\to0\) must meet: \(\Delta V\ge2\pi^2k(1-o(1))\), i.e. Yamabe constants \(|Y|\ge4\pi\sqrt{2(A+k)}(1-o(1))\), and simultaneously \(W^+\) with deficit \(D_W\approx2\Delta V\) concentrated near the magnitude-deficit direction with \(\mu_{\min}\)-eigenvector aligned to the monopole direction and amplitude \(r=r_*(x)\).
3. In the near-CH regime the remaining object is the per-core inequality \(D_{W,U}-\Delta V_U\le(1-c_0)2\pi^2\), a statement about marked cells with CH-asymptotic (not exact) collars, whose J-anti tails decay only like \(e^{-4r}\). This is where the cell programme (Theorem C, certified intervals) and the global theory now meet.
4. For the conformal-class route suggested by the strategist: period opening enters twice — it forces Yamabe excess, \(\Delta V\ge2\pi^2Q_{\rm per}\), and it subtracts \(16\pi^2\Pi_g\ge16\pi^2Q_{\rm per}\) from the admissible saving at fixed \(\Delta V\) (LeB\(_{\rm full}\)). A tariff would follow from (LeB\(_{\rm full}\)) only if one could force \(\Pi_g\gtrsim k\) or bound \(\Delta V-4\pi^2\Pi_g\); no available result does either, and A01's rotated cells show \(\Pi_g\) can be small (quadratic period stiffness).
