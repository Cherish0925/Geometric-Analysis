# Step 38: continuation repair and support normalization

Session: S0910A01.  Agent3 / Execute.

## 0. Purpose and correction of the Step 37 state

Step 37 announced that the shifted continuation theorem and the first-exit flow
platform were closed.  That announcement is withdrawn.  The inserted Lemma 1.2a
was not a valid replacement for Wang's unweighted curvature-derivative module.
The point is local and structural:

\[
U=aT=a(\operatorname{Rm}+G),\qquad \operatorname{Ric}(U)=aE,
\quad a=\chi^2.
\]

Thus \(|U|\le K\) implies
\[
|aE|=|\operatorname{Ric}(U)|\le C K,
\]
not \(|aE|\le C\chi^2K\).  In the region \(\chi<\delta\), the flow velocity is
bounded but not quadratically small in \(\chi\).  Even a genuinely small
\(C^0\) metric displacement would not control curvature derivatives.  Also, the
fixed coordinate derivatives of the scalar cutoff do not control the evolving
covariant derivatives \(\nabla^j\chi\); those derivatives are coupled to the
connection evolution.  Therefore the split
\(\{\chi\ge\delta\}\cup\{\chi<\delta\}\) does not recover
\(\nabla^k\operatorname{Rm}\) from \(\nabla^kU\) in the transition region.

What survives from Step 37 is useful but conditional:

- \(|U|\) controls \(|aE|\), hence metric bilipschitz evolution by the logarithmic
  estimate.
- The zero-order unweighted \(L^p(\operatorname{Rm})\) propagation is still
  plausible by the Wang Lemma 4.10 mechanism, after the Step 35 Hessian-\(a\)
  splitting.
- The first-exit self-improvement remains a conditional implication once a true
  continuation theorem and the weighted Moser endpoints are available.

The repair must follow Wang's actual order:

\[
\text{weighted equation for }U=aT
\quad\Longleftrightarrow\quad
\text{cutoff jets }\nabla^j\chi
\quad\Longleftrightarrow\quad
\text{unweighted curvature derivatives }\nabla^j\operatorname{Rm}.
\]

## 1. Correct weighted shifted equation

Let
\[
T=\operatorname{Rm}+G,
\qquad G={g\owedge g\over6},
\qquad U=aT.
\]
At each time \(\nabla G=0\), and the shift is chosen so that
\(\operatorname{Ric}(T)=E\) and \(\operatorname{Ric}(U)=aE\).  The connection
variation is
\[
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U),
\tag{1.1}
\]
so every cutoff-jet evolution is driven by derivatives of \(U\), not by a split
\(da*E+a\nabla E\).

Wang's Lemma 4.5 for \(\chi^2\operatorname{Rm}\) shows the necessary weighted
pattern.  In the normalized shifted equation, the corresponding schematic
formula is
\[
\begin{aligned}
\partial_t\nabla^mU
={}& a\Delta\nabla^mU \\
&+\sum_{i+j+k=m+2,\;k\le m+1}
   \nabla^i\chi*\nabla^j\chi*\nabla^kU \\
&+\sum_{i+j+k=m,\;k\le m-1}
   \nabla^i a*\nabla^jU*\nabla^k\operatorname{Rm} \\
&+ U*\nabla^mU+\mathcal L_m^{G,\mathrm{norm}}.
\end{aligned}
\tag{1.2}
\]
Here \(\mathcal L_m^{G,\mathrm{norm}}\) contains only terms with at most
\(m\) derivatives of \(U\), at most \(m+1\) derivatives of \(\chi\), and
unweighted curvature derivatives of order \(\le m-1\).  The important correction
relative to Step 37 is that the first line of cutoff terms contains
\(\nabla^kU\), not \(\nabla^k\operatorname{Rm}\).  Consequently the highest
cutoff allocations at level \(m\) are
\[
\Gamma_1=\chi\nabla^{m+2}\chi*U,
\quad
\Gamma_2=\nabla\chi*\nabla^{m+1}\chi*U,
\quad
\Gamma_3=\chi\nabla^{m+1}\chi*\nabla U,
\quad
\Gamma_4=\chi\nabla\chi*\nabla^{m+1}U.
\tag{1.3}
\]
These are the same top structures as Wang Proposition 4.14, with
\(\chi^2\operatorname{Rm}\) replaced by \(U\).  They do not contain an uncontrolled
unweighted \(\nabla^m\operatorname{Rm}\) at the weighted top level.

The cutoff-jet equation follows from (1.1): for \(\ell\ge2\),
\[
\partial_t\nabla^\ell\chi
=
\sum_{b=0}^{\ell-2}\nabla^b\nabla\operatorname{Ric}(U)*\nabla^{\ell-1-b}\chi
+\text{lower contractions},
\tag{1.4}
\]
and after absorbing contractions into notation,
\[
\partial_t|\nabla^{m+1}\chi|
\le C\sum_{b=0}^{m}|\nabla^bU|\,|\nabla^{m+1-b}\chi|
       +\text{lower terms}.
\tag{1.5}
\]
This is the shifted form of Wang Lemma 4.6.

## 2. Base weighted pair \((\nabla U,\nabla^2\chi)\)

Write
\[
V=\nabla U,
\qquad Z=\nabla^2\chi.
\]
Testing the \(m=1\) case of (1.2) against \(|V|^{p-2}V\) gives the dissipative
term
\[
-cp\int a|\nabla V|^2|V|^{p-2}.
\tag{2.1}
\]
The two top terms requiring care are
\[
I_1=\int |V|^{p-2}\langle V,\chi\nabla^3\chi*U\rangle,
\qquad
I_2=\int |V|^{p-2}\langle V,\chi Z*V\rangle.
\]
For \(I_1\), integrate one derivative off \(\nabla^3\chi\).  The term where the
derivative hits \(|V|^{p-2}V\) is bounded by
\[
\varepsilon\int a|\nabla V|^2|V|^{p-2}
+C_{\varepsilon}K^2\int |Z|^2|V|^{p-2},
\]
and
\[
\int |Z|^2|V|^{p-2}
\le \|Z\|_p^2\|V\|_p^{p-2}
\le C_p(\|Z\|_p^p+\|V\|_p^p).
\tag{2.2}
\]
Terms where the derivative hits \(\chi\) or \(U\) are lower: they contain
\(d\chi\), \(U\), or \(V\) and are bounded by the same pair
\(\|Z\|_p^p+\|V\|_p^p\) plus already known zero-order curvature quantities.
The single-Hessian term \(I_2\) has the signed form of Step 35/A03 Step 38;
after one signed integration by parts it contributes
\[
\varepsilon\int a|\nabla V|^2|V|^{p-2}
+C_{p,\varepsilon}r^{-2}\int |V|^p.
\tag{2.3}
\]
The \(\Gamma_4=\chi\nabla\chi*\nabla^2U\) term is directly absorbed into
(2.1), leaving \(Cr^{-2}\|V\|_p^p\).

From (1.5) with \(m=1\), the tensor variation gives \(\partial_tZ=\nabla U*d\chi+U*Z+\) lower contractions.  Thus
\[
{d\over dt}\|Z\|_p^p
\le C\int |V|\,|d\chi|\,|Z|^{p-1}+C\int |U|\,|Z|^p+C\|Z\|_p^p+C
\le C_{p,K,r}(\|V\|_p^p+\|Z\|_p^p+1).
\tag{2.4}
\]
\]
Thus the repaired base pair has the form
\[
{d\over dt}\bigl(\|\nabla U\|_p^p+\|\nabla^2\chi\|_p^p\bigr)
\le C_{p,K,r}\bigl(\|\nabla U\|_p^p+\|\nabla^2\chi\|_p^p+1+\|\operatorname{Rm}\|_{q}^{q}\bigr),
\tag{2.5}
\]
where \(q\) is finite and is supplied by the zero-order Wang Lemma 4.10 module.
This replaces Step 37's false route through unweighted \(\nabla\operatorname{Rm}\).

## 3. Shifted Wang Proposition 4.13 module for unweighted curvature derivatives

The unweighted curvature-derivative estimates are not recovered by dividing by
\(a\).  They must be proved from the unweighted curvature equation, exactly as in
Wang Proposition 4.13.

Assume for a fixed \(m\ge1\) and for all finite exponents needed below:

1. \(\|\nabla^i\chi\|_{L^q}<\infty\) for \(0\le i\le m+1\);
2. \(\|\nabla^j\operatorname{Rm}\|_{L^q}<\infty\) for \(0\le j\le m-1\), with
   the zero-order case supplied by Lemma 4.10;
3. \(\|U\|_{L^\infty}<\infty\), hence \(\|a\operatorname{Rm}\|_\infty<\infty\)
   and \(\|aE\|_\infty<\infty\);
4. metric and \(|d\chi|\) are bounded on the positive-time slab.

Then the shifted normalized version of Wang Proposition 4.13 gives
\[
\|\nabla^m\operatorname{Rm}\|_{L^p}<\infty.
\tag{3.1}
\]
The schematic inequality after testing the \(\nabla^m\operatorname{Rm}\) equation
against \(|\nabla^m\operatorname{Rm}|^{p-2}\nabla^m\operatorname{Rm}\) is
\[
\begin{aligned}
{d\over dt}\|R_m\|_p^p
&+c\int a|\nabla R_m|^2|R_m|^{p-2} \\
&\le C\|R_m\|_p^p+C
 + C\sum \int B_1\cdots B_N |R_m|^{p-1}
 + C\sum \int B_1\cdots B_N |R_m|^{p-2},
\end{aligned}
\tag{3.2}
\]
where \(R_m=\nabla^m\operatorname{Rm}\), the \(B_j\)'s are cutoff jets,
lower curvature derivatives, \(U\), or bounded coefficients.  The only term with
\(\nabla R_m\) after integrating \(\chi\nabla^{m+2}\chi*\operatorname{Rm}\) is
controlled by
\[
\varepsilon\int a|\nabla R_m|^2|R_m|^{p-2}
+C_\varepsilon\int |\nabla^{m+1}\chi|^2|\operatorname{Rm}|^2|R_m|^{p-2}.
\tag{3.3}
\]
The finite exponent choice is explicit:
\[
\int |\nabla^{m+1}\chi|^2|\operatorname{Rm}|^2|R_m|^{p-2}
\le
\|\nabla^{m+1}\chi\|_{2p}^2
\|\operatorname{Rm}\|_{2p}^2
\|R_m\|_p^{p-2}.
\tag{3.4}
\]
Young gives a polynomial expression in the known norms plus \(C\|R_m\|_p^p\).
For a product with \(N\) lower factors,
\[
\int B_1\cdots B_N |R_m|^{p-1}
\le \prod_{j=1}^{N}\|B_j\|_{Np}\,\|R_m\|_p^{p-1},
\tag{3.5}
\]
because \(N/(Np)+(p-1)/p=1\).  This supplies the finite Hölder exponents missing
from Step 37.  Normalization terms from \(-2ag\) and shift terms from \(G\) add
only lower products of the same form, since \(\nabla G=0\) and derivatives of
\(aG\) are cutoff-jet terms.

## 4. Higher weighted pair and closure pattern

Suppose the unweighted module has supplied
\(\|\nabla^{m-1}\operatorname{Rm}\|_{L^q}\) for all finite \(q\) required at
level \(m\).  Let
\[
V_m=\nabla^mU,
\qquad Z_m=\nabla^{m+1}\chi.
\]
Testing (1.2) gives
\[
{d\over dt}\|V_m\|_p^p
+c\int a|\nabla V_m|^2|V_m|^{p-2}
\le C_{m,p,K,r}\bigl(\|V_m\|_p^p+\|Z_m\|_p^p+1\bigr)
+\mathcal I_{m-1},
\tag{4.1}
\]
where \(\mathcal I_{m-1}\) contains only lower levels and the just-proved
\(\nabla^{m-1}\operatorname{Rm}\) norms.  The estimates for the top terms in
(1.3) use only the current pair:

- \(\Gamma_4\) is absorbed by diffusion.
- For \(\Gamma_1\), integration by parts gives the model remainder
  \(\int |Z_m|^2|U|^2|V_m|^{p-2}\), controlled by
  \[
  K^2\|Z_m\|_p^2\|V_m\|_p^{p-2}
  \le C_{p,K}(\|Z_m\|_p^p+\|V_m\|_p^p+1).
  \tag{4.2}
  \]
- \(\Gamma_2\) gives \(\int |Z_m||U||V_m|^{p-1}\), and
  \[
  K\int |Z_m||V_m|^{p-1}
  \le C_{p,K}(\|Z_m\|_p^p+\|V_m\|_p^p).
  \tag{4.3}
  \]
- \(\Gamma_3\) contains \(Z_m*\nabla U\).  It must **not** be estimated by putting \(\nabla U\) in \(L^\infty\) at the first nontrivial levels.  A03 Step 40 gives the correct \(m=2\) mechanism: for \(V=\nabla^2U\), \(Z=\nabla^3\chi=\nabla\Theta\), \(W=\nabla U\), integrate once more off \(Z\) in
  \[
  \int \chi Z*W*|V|^{p-2}V.
  \]
  The residuals are \(d\chi*\Theta*W*P(V)\), \(\chi\Theta*V*P(V)\) (signed Hessian), and \(\chi\Theta*W*\nabla P(V)\) (weighted dissipation plus \(\int\Theta^2W^2|V|^{p-2}\), controlled by base-pair finite norms at exponents such as \(4p\)).  This avoids any current \(Z\in L^{2p}\) or \(W\in L^\infty\) input.  For the base level \(m=1\), the term is part of the pair estimate of §2.  For arbitrary \(m\), the analogous repeated integration and finite-exponent schedule remain to be written.

The cutoff-jet evolution (1.5) similarly yields
\[
{d\over dt}\|Z_m\|_p^p
\le C_{m,p,K,r}\bigl(\|V_m\|_p^p+\|Z_m\|_p^p+1\bigr)
+\mathcal I_{m-1}.
\tag{4.4}
\]
Hence
\[
Y_m(t):=\|\nabla^mU(t)\|_p^p+\|\nabla^{m+1}\chi(t)\|_p^p
\]
satisfies
\[
Y_m'\le C_{m,p,K,r}(Y_m+1)+\mathcal I_{m-1}.
\tag{4.5}
\]
A Volterra/Gronwall comparison gives finite per-datum bounds on a positive-time
slab.  This is the actual continuation route.  It depends on the unweighted
module (3.1), not on the invalid division-by-\(a\) or small-drift argument.

Once all \(\nabla^mU\), all evolving cutoff jets, and all
\(\nabla^m\operatorname{Rm}\) are finite on \([\tau,T_{\max})\), smooth extension
is recovered without dividing by \(a\):
\[
\partial_tg=-2\operatorname{Ric}(U),
\qquad
\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U).
\tag{4.6}
\]
The right-hand sides and all their spatial derivatives are bounded in fixed
positive-time charts, so \(g(t)\) has a smooth limit as \(t\uparrow T_{\max}\).
The per-datum transported-DeTurck short-time construction can then restart from
that terminal metric.  This is the correct replacement for Step 37's Lemma 1.2a.

This note has not yet expanded every tensor contraction in (1.2) or every
normalization/\(G\) lower term; it records the repaired dependency pattern and the
finite-exponent estimates that remove the specific Step 37 obstruction.

## 5. Correct support-selection normalization

The support construction must use a volume-average maximal function, not
\(r^{-4}\int\) or \(r^4\int\).  Let
\[
K_0={1\over\operatorname{Vol}M}\int_M |\operatorname{Rm}|^2\,d\mu,
\qquad
\mathcal M_R f(x)=\sup_{0<s\le R}\fint_{B_s(x)} f\,d\mu.
\tag{5.1}
\]
Under the near-negative pinching, \(\operatorname{Ric}\ge-2g\) for all large
sequence index, so balls of radii \(\le R\) have a uniform local doubling constant.
The weak maximal inequality gives
\[
\operatorname{Vol}\{x:\mathcal M_R(|\operatorname{Rm}|^2)(x)>\Lambda K_0\}
\le {C_D(R)\over\Lambda}\operatorname{Vol}M.
\tag{5.2}
\]
Choose \(\Lambda\) large enough that the good set
\[
G_R(\Lambda)=\{\mathcal M_R(|\operatorname{Rm}|^2)\le\Lambda K_0\}
\tag{5.3}
\]
has volume at least \(\eta_0\operatorname{Vol}M\), with fixed \(\eta_0>0\).  Then
choose a fixed small radius
\[
r\le R/10,
\qquad
r^4\Lambda \overline K_0\le \varepsilon_{\mathrm{Li}},
\qquad
C_{\mathrm{Sob}}r^2(1+\Lambda\overline K_0)^{1/2}\le\gamma_*,
\tag{5.4}
\]
where \(\overline K_0\) is a sequence-uniform upper bound for the mean full
curvature energy.  For every \(x\in G_R(\Lambda)\),
\[
r^4\fint_{B_r(x)}|\operatorname{Rm}|^2\le\varepsilon_{\mathrm{Li}}.
\tag{5.5}
\]
One must still match the exact small-energy hypothesis of the smoothing theorem used downstream.  If that theorem asks for the unnormalized four-dimensional critical quantity \(\int_{B_r}|\operatorname{Rm}|^2\), then Bishop--Gromov upper volume under the Ricci lower bound gives
\[
\int_{B_r(x)}|\operatorname{Rm}|^2
\le C_{BG}r^4\Lambda\overline K_0,
\]
so the same small choice of \(r\) works.  This implication uses only an upper ball-volume comparison; it does not assert local noncollapse.
\[
K_2^\eta\le (1+\Lambda\overline K_0)\operatorname{Vol}(B_{R_0r}(x)).
\tag{5.6}
\]
The Sobolev-volume product is then
\[
\mathcal S(K_2^\eta)^{1/2}
\le C{r^2\over \operatorname{Vol}(B_{R_0r})^{1/2}}
   \bigl((1+\Lambda\overline K_0)\operatorname{Vol}(B_{R_0r})\bigr)^{1/2}
= C r^2(1+\Lambda\overline K_0)^{1/2}.
\tag{5.7}
\]
This is the collapse cancellation required by the weighted estimates.

The lower bound \(\operatorname{Vol}(M_i)/A_i\ge c>0\) used to convert good
volume into \(A_i\)-proportional plateau volume comes from the calibrated
near-critical identities, not from an Euler-characteristic upper estimate.  With
\[
I_i={1\over4\pi^2}\int\left({s_i^2\over24}+2|W_i^+|^2\right),
\qquad
I_i/A_i\to {2\over3},
\]
and terminal or initial calibration
\[
\int(s_i+4)^2=o(A_i),
\qquad
\int(s_i+8\sqrt6|W_i^+|)^2=o(A_i),
\tag{5.8}
\]
one has
\[
{s_i^2\over24}+2|W_i^+|^2={3\over4}+e_i,
\qquad
\int |e_i|=o(A_i)
\tag{5.9}
\]
(using the already known \(\operatorname{Vol}/A=O(1)\)).  Therefore
\[
{3\over4}\operatorname{Vol}(M_i)+o(A_i)=4\pi^2 I_i
={8\pi^2\over3}A_i+o(A_i),
\]
so
\[
\operatorname{Vol}(M_i)/A_i\to {32\pi^2\over9}.
\tag{5.10}
\]
A maximal separated net in \(G_R(\Lambda)\), followed by Bishop-Gromov packing
and a finite coloring of the enlarged supports, can then select one
macro-disjoint color with total inner plateau volume
\[
\sum_{\alpha\in\mathcal C}\operatorname{Vol}(P_\alpha)
\ge \alpha A_i
\tag{5.11}
\]
for a fixed \(\alpha>0\), provided the radii and buffer factors are fixed.  The
point of (5.10) is that the retained fraction of total volume is also a retained
fraction of the topology scale \(A_i\).

## 6. Current state after this repair

The flow route is not closed.  The repaired continuation plan now has the right
objects: weighted shifted equations for \(U\), Wang's unweighted curvature module,
finite Hölder exponents, and recovery of a smooth terminal metric through
\(\partial_tg=-2\operatorname{Ric}(U)\).  The support front also has the correct
normalization: large average-energy threshold for volume retention, then small
fixed radius for critical smallness and Sobolev-product cancellation.

What remains mathematical work, not exposition, is to expand (1.2) from the
all-lower tensor variation and verify every \(G\)/normalization lower term in the
induction, then integrate the repaired continuation theorem with the conditional
K2--Y--J6--Q estimates and the selected supports.  Even success here would only
address the near-critical Ishida--LeBrun negative laboratory in dimension four,
not the full Yau 26 proposition, the positive branch, higher dimensions, or Lean
formalization.
