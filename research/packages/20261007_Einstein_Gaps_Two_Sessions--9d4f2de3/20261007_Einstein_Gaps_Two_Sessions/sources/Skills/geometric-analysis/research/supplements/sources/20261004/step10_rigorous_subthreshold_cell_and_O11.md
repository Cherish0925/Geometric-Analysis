# Step 10 — Rigorous subthreshold perpendicular cell; the balanced coefficient four is not sharp

Session S1003A01, Step 10, Agent2, Execute.  Builds on Step 7 (Cartan verification, bolt jets), Step 8 (collar scan), Step 9 (frozen witness, transfer chain).

## 1. Statement

**Theorem (finite-scale subthreshold cell).** Let \(x_0=1/100\), \(X=8\), and let \(z\in\mathbb Q^{24}\) be the 24 binary doubles stored in
`workspace/data/perp_collar/x0.01_X8_J_d8.json`.  Define on \(x_0\le x\le X\), with \(u=\log(x/x_0)/\ell\), \(\ell=\log(X/x_0)\), \(S(u)=10u^3-15u^4+6u^5\), \(T_k\) Chebyshev polynomials of \(2u-1\),

\[
\begin{aligned}
q_F&=(1-u)^3\textstyle\sum_{k<8}z_kT_k,\qquad q_G=(1-u)^3\sum_{k<8}\tilde z_{8+k}T_k,\\
F&=(x-x_0)e^{q_F}+x_0S,\qquad G=\big(x-x_0+(x^2+x_0)S\big)e^{q_G},\\
w&=\log(1+x)\,S+u^2(1-u)^3\textstyle\sum_{k<8}z_{16+k}T_k,
\end{aligned}
\]

where \(\tilde z\) equals \(z\) except \(\tilde z_8=z_8-\sum_k(-1)^k(z_k+z_{8+k})\) (so \(q_F(0)+q_G(0)=0\)).  The metric

\[
g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^{w}\sigma_3^2,\qquad d\sigma_1=2\sigma_2\wedge\sigma_3\ \text{(cyclic)},
\]

closed by the exceptional sphere at \(x=x_0\) and continued by the exact complex-hyperbolic metric (\(F=x,\ G=x+x^2,\ e^w=1+x\), \(\operatorname{Ric}=-6g\)) for \(x\ge X\), is a \(C^2\) metric on a ball of \(\mathbb{CH}^2\) blown up once, \(D\#\overline{\mathbb{CP}}^2\), and

\[
\boxed{\frac{1}{8\pi^2}\int|\operatorname{Ric}+6g|^2\,dV\in[0.99911624314\pm7.0\times10^{-12}],}
\]
\[
\frac{1}{8\pi^2}\int|\operatorname{Ric}^\circ|^2\in[0.99910870273\pm5.8\times10^{-12}],\qquad
\frac{1}{8\pi^2}\cdot\frac14\int(s+24)^2\in[7.54040\times10^{-6}\pm3.6\times10^{-12}].
\]

Thus \(J_6/(8\pi^2)\le1-\eta\) with \(\eta=8.8375686\times10^{-4}\) certified.  The second frozen profile `x00.01_X16_J_d8.json` (\(X=16\)) gives \(J_6/(8\pi^2)\in[0.99890294372\pm2.4\times10^{-12}]\), \(\eta_{16}=1.0970563\times10^{-3}\).

**Corollary (O11, negative answer).** There is a smooth single-blowup cell with exact CH collar and \(J_1\le 8\pi^2(1-\eta/2)\) (in the I54 normalization \(\operatorname{Ric}_D=-g\)).  Consequently there is a balanced surgery sequence \(M_j\) (same proportions \(k_j/Q_j\to2/9\), \(\ell_j/Q_j\to7/36\) as the inherited family, over a suitably chosen tower of covers) with

\[
\limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}\le \frac{28}{9}+\frac{J_1}{9\pi^2}\le 4-\frac{4\eta}{9},
\]

and, letting the smoothing width tend to zero (one sequence per width), for every \(\epsilon>0\) a sequence with \(\limsup\alpha/h\le 4-\tfrac{8\eta}{9}+\epsilon\).  With the \(X=16\) witness: \(4-8\eta_{16}/9=3.99902484\).  **The coefficient four is not the optimal first-order coefficient of the balanced family over all admissible metrics.**

## 2. The cancellation-free representation (why the Step-9 Arb attempt failed and this one works)

Step 9 evaluated raw spin variables; near the bolt they contain \(y^{-1/2}\), \(y^{-1}\) pieces whose cancellation destroys interval arithmetic.  Here the orthonormal Ricci of \(dt^2+\sum a_i^2\sigma_i^2\) is used in the classical form

\[
R_{00}=-\sum_i\frac{\ddot a_i}{a_i},\qquad
R_{ii}=-\frac{\ddot a_i}{a_i}-\frac{\dot a_i}{a_i}\Big(\frac{\dot a_j}{a_j}+\frac{\dot a_k}{a_k}\Big)+\frac{2\big(a_i^4-(a_j^2-a_k^2)^2\big)}{a_i^2a_j^2a_k^2},
\]

(checked against the Cartan derivation of `perp_cartan_verify.py` by `check_bianchi_ricci_closed_form.py`), with \(h_i=a_i^2\), \(d/dt=2\sqrt G\,d/dx\).  Only products of the form \(\dot a_i\dot a_j/(a_ia_j)=G h_i'h_j'/(h_ih_j)\) and \(\ddot a_i/a_i=G'h_i'/h_i+2Gh_i''/h_i-Gh_i'^2/h_i^2\) occur — never \(\dot a_1^2/a_1^2\) alone.  Writing

\[
y=x-x_0=x_0\ell u\,\varphi(\ell u),\quad \varphi(z)=\frac{e^z-1}{z},\qquad
F=y\hat F,\ G=y\hat G,\ w=y^2\hat w,
\]
\[
\hat F=e^{q_F}+\frac{u^2(10-15u+6u^2)}{\ell\varphi},\quad
\hat G=\Big(1+\frac{(x^2+x_0)u^2(10-15u+6u^2)}{x_0\ell\varphi}\Big)e^{q_G},\quad
\hat w=\frac{\log(1+x)u(10-15u+6u^2)+(1-u)^3C_w}{(x_0\ell\varphi)^2},
\]

all three are entire-type functions of \(u\), positive on \([0,1]\).  The only bolt-singular combinations become regular identities:

\[
\frac{\ddot a_1}{a_1}=2\frac{\hat G}{\hat F}h_1''+h_1'\frac{\hat G'\hat F-\hat G\hat F'}{\hat F^2},\qquad
\frac{\dot a_1\dot a_j}{a_1a_j}=\frac{\hat G}{\hat F}\frac{h_1'h_j'}{h_j},
\]
\[
\frac{(h_2-h_3)^2}{h_1h_2h_3}=\frac{y^3\hat w^2\varphi(w)^2}{\hat F e^w},\qquad
\frac{2(h_2^2-(h_3-h_1)^2)}{h_1h_2h_3}=-\frac{4y\hat w\,\mathrm{shc}(w)}{\hat F}+\frac4x-\frac{2h_1}{x^2e^w},
\]
and the analogue for \(i=3\) (\(\mathrm{shc}(w)=\sinh w/w\)).  The density
\[
\frac{dJ_6}{8\pi^2\,du}=\frac18\,x\,e^{w/2}\sqrt{\hat F/\hat G}\;\sum_a(R_{aa}+6)^2\;\ell x
\]
is therefore holomorphic on a complex neighbourhood of \([0,1]\).  Volume normalization: \(dV=\pi^2\sqrt{h_1h_2h_3/G}\,dx\) (\(\int\sigma_{123}=2\pi^2\)).

**Rigorous integration.** `workspace/scripts/perp_rigorous_enclosure.py` evaluates this density with second-order jets over complex balls (python-flint `acb`), with \(\varphi,\varphi',\varphi''\) from the closed form for \(|z|>1\) and from the Taylor series with explicit tail bound \(r^N/N!\,(1-r/(N+1))^{-1}\) for \(|z|\le1\); \(\sqrt{\cdot}\) and \(\log\) are called with the analytic flag, and division by a ball containing zero returns a non-finite value.  Hence the function satisfies the holomorphic-enclosure contract of Arb's `acb_calc_integrate` (Petras-type Gauss–Legendre with error bounds from the complex ellipse), and `acb.integral` returns a rigorous enclosure.  Runs at 128/192/256 bits and tolerances \(10^{-6}\)–\(10^{-13}\) all give nested enclosures; the loose \(10^{-6}\) run already certified \(J<1\) ([0.9991 ± 3.4e-5]).  Outputs: `workspace/data/perp_collar/rigorous_x0.01_X8_J_d8.json`, `rigorous_x00.01_X16_J_d8.json` (include pointwise checks: at \(u=1\) all \(R_{aa}=-6\) to \(10^{-14}\); at \(u=0\) the values are finite with \(R_{00}=R_{11}=-206.2910940\), \(R_{22}=R_{33}=193.5719039\), the symmetry expected at a smooth bolt).  Consistency: \(J-P\) agrees with the scalar ball; the floating values of three independent codes (local coordinate curvature, local spin formula, peer's import-free reconstruction 0.9991162431353) lie inside the ball.

## 3. Admissibility of the frozen profile

* *Positivity:* \(1-S=(1-u)^3(1+3u+6u^2)\) and \(10-15u+6u^2>0\), so \(0\le S\le1\) on \([0,1]\); hence \(\hat F\ge e^{q_F}>0\), \(\hat G>0\), \(h_2=x>0\), \(h_3>0\).
* *Bolt:* \(t=\int dx/(2\sqrt G)\) gives \(y=\hat G(0)t^2+O(t^4)\), \(a_1^2=yF̂=\hat F(0)\hat G(0)t^2+\dots=t^2+O(t^4)\) because \(q_F(0)+q_G(0)=0\) exactly; \(a_2^2,a_3^2\) are smooth in \(t^2\) and \(a_2^2-a_3^2=x(1-e^w)=O(t^4)\) times a smooth function of \(t^2\), the weight-four condition for the \(\sigma_2,\sigma_3\) plane under the Hopf circle.  All profile functions are real-analytic in \(y\) near \(0\) (through \(u=\ell^{-1}\log(1+y/x_0)\)).  These are the standard smoothness conditions at a Hopf bolt with full fibre period (\(a_1'(0)=1\)); the Step 7 bolt expansion confirmed them.
* *Topology/orientation:* the circle generated by the \(\sigma_1\)-dual field is conjugate in \(SU(2)\) to the \(\sigma_3\) one by right translation, which is isotopic to the identity on \(S^3\).  Hence the perpendicular cell is oriented-diffeomorphic rel boundary to the aligned Burns blow-up \(D\#\overline{\mathbb{CP}}^2\): \(k=1,\ell=0,q=1\) in I54 (1.1)–(2.3).
* *Collar:* each deviation \(d_F=F-x=(x-x_0)(e^{q_F}-1)-x_0(1-S)\), \(d_G=G-(x+x^2)=(x+x^2)(e^{q_G}-1)-(x^2+x_0)(1-S)e^{q_G}\), \(d_w=w-\log(1+x)=-\log(1+x)(1-S)+u^2(1-u)^3C_w\) is analytic on a neighbourhood of \([x_0,X]\) and vanishes to order three at \(X\).
* *Normalization:* \(\tilde g=6g\) has \(\operatorname{Ric}=-\tilde g\) on the collar and \(\int|\operatorname{Ric}_{\tilde g}+\tilde g|^2_{\tilde g}dV_{\tilde g}=J_6(g)\).  The collar radius in \(\operatorname{Ric}=-g\) units is \(\sqrt6\,\operatorname{arsinh}\sqrt X\approx4.32\).

## 4. Smoothing lemma (analytic; no second interval computation needed)

Fix \(\chi\in C^\infty(\mathbb R)\), \(\chi=1\) on \([1,\infty)\), \(\chi=0\) on \((-\infty,1/2]\), and for \(0<\delta<(X-x_0)/2\) put \(\chi_\delta(x)=\chi((X-x)/\delta)\).  Let \(g_\delta\) be defined by \(F_\delta=x+\chi_\delta d_F\), \(G_\delta=x+x^2+\chi_\delta d_G\), \(w_\delta=\log(1+x)+\chi_\delta d_w\).  Then:

1. \(g_\delta=g\) for \(x\le X-\delta\) (bolt unchanged) and \(g_\delta\) is exactly CH for \(x\ge X-\delta/2\); \(g_\delta\) is \(C^\infty\) everywhere (analytic data times a smooth cutoff on \((x_0,X)\), exact CH beyond).
2. On \(B_\delta=[X-\delta,X]\): \(|d^{(k)}|\le C(X-x)^{3-k}\le C\delta^{3-k}\) and \(|\chi_\delta^{(k)}|\le C_\chi\delta^{-k}\), so \(\|g_\delta-g_{CH}\|_{C^2(B_\delta)}+\|g-g_{CH}\|_{C^2(B_\delta)}\le C'\delta\).  For \(\delta\) small, \(F_\delta,G_\delta,h_{3,\delta}\ge X/2\) on \(B_\delta\) (positivity), and since \(\operatorname{Ric}+6g\) is a smooth function of the 2-jet vanishing at the CH jet, \(|\operatorname{Ric}+6g|\le C''\delta\) on \(B_\delta\) for both metrics.
3. Therefore \(|J_6(g_\delta)-J_6(g)|\le 2C''^2\delta^2\operatorname{Vol}(B_\delta)=O(\delta^3)\to0\).

Choose \(\delta\) with this error \(\le 8\pi^2\eta/2\): \(J_6(g_\delta)\le8\pi^2(1-\eta/2)\).  Constants depend only on the frozen profile.  (Directly attaching the \(C^2\) profile is also already a \(W^{2,\infty}\) metric with the stated energy; the smoothing is only needed for the smooth class \(\mathscr G(M)\).)

## 5. Global transfer

I54 §2: inserting the single-blowup cell in \(k\)-sites and treating the \(\ell\) handle surgeries by the inherited shrinking construction gives, with \(k_j/Q_j\to2/9\), \(4\ell_j/Q_j\to7/9\),
\[
\mathcal E(g_j)/h_j\to \frac{2}{9}\frac{J_1}{2\pi^2}+\frac79\cdot\frac{8\pi^2}{2\pi^2}=\frac{28}9+\frac{J_1}{9\pi^2},
\]
and \(J_1=8\pi^2(1-\epsilon_0)\) gives \(4-8\epsilon_0/9\).  The fixed buffered ball of radius \(r\) (\(\approx4.32\) plus buffer) is supplied as in Step 9: in a lattice \(\Gamma\) only finitely many \(\gamma\ne1\) have \(d(p,\gamma p)\le 2r\); residual finiteness gives finite index \(\Gamma_*\) avoiding them; covers inside \(\Gamma_*\) contain a number of disjoint lifts proportional to \(A_j\gg Q_j\).  The statement is existential: a balanced sequence over a suitably chosen tower, not every preassigned cover tower.

## 6. Meaning inside the programme

* The inherited all-metric lower theory is unaffected: the whole-AE threshold (Step 5) and aligned diagonal/Kähler cell bounds hold in their regimes; the new cell is a fixed-scale core–background interaction in the \(\omega^\perp\) kernel of \(R^+\) for a negative Kähler–Einstein background (Step 8 response law: first-order critical, second-order cubic compensation, enhanced by a large collar).
* O11 is now reformulated: the optimal (all-metric, best-sequence) balanced first coefficient \(c_*=\inf\limsup\alpha_j/h_j\) satisfies \(c_{\rm inh}\le c_*<4\), where \(c_{\rm inh}>0\) is the inherited actual-field lower constant.  The single-blowup-plus-separated-handle route has the form \(28/9+8\kappa_1/9\), where \(\kappa_1=\inf J_1/(8\pi^2)\) over single-blowup exact-CH cells.  The inherited exact handle-only theorem implies that every pure-handle exact-CH cell satisfies \(J\ge32\pi^2\ell\), with infimum \(32\pi^2\ell\); isolated handle improvement is therefore impossible.  The distinct collective question is whether a mixed \((k,\ell)\) cell is strictly cheaper than its blow-up and pure-handle parts.  For the balanced block this asks whether \(\mathfrak J_{8,7}<8\mathfrak J_{1,0}+224\pi^2\), while a cell coefficient is \(\mathfrak J_{8,7}/(72\pi^2)\).  Open: the single- and multi-blowup infima, mixed-cell nonadditivity, complete large-collar limits, matching lower bounds, and unrestricted global competitors.
* Lower bound side for the general first coefficient remains: \(c\,h\le\alpha\) with inherited \(c\); the positive gap for these families is untouched.

Step 11 independently reviewed the proof, replaced the float-mediated \(\phi\)-tail radius by a pure-Arb bound, and reran the strict certificate.  The review and corrected cost formulation are in `workspace/notes/step11_independent_review_O11_and_mixed_cost.md`; the canonical local certificate is `workspace/data/perp_collar/strict_rigorous_x0.01_X8_J_d8.json`.

## 7. Symbolic verification record

`check_bianchi_ricci_closed_form.py` (task output `workspace/tasks/s10_t11_tool1/stdout.log`): closed-form Ricci minus Cartan Ricci = [0,0,0,0] (exact `sympy.cancel`), and the desingularized rewrites of \(D_1\), \(A_1,A_2,A_3\) have residual 0.  Together with the rigorous `acb.integral` enclosure this makes the energy statement of §1 a computer-assisted theorem whose remaining trust base is (i) Arb/acb_calc_integrate correctness, (ii) the holomorphic-enclosure contract of the integrand code (reviewable, ~150 lines), and (iii) the transcription of the profile formula from `o11_perp_cell.PerpCell` (wpow=2, perpendicular, beta0=0), which is corroborated by agreement with the three floating implementations to \(10^{-11}\).
