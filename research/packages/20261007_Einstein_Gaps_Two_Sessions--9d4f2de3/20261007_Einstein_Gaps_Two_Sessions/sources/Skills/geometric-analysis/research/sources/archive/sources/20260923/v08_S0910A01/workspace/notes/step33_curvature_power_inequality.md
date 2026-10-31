# Step 33: Explicit curvature power inequality for the normalized cutoff flow

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

**Step 34 superseding correction.**  Use
`workspace/notes/step34_integrated_potential_q3_and_defect.md` for the current
fixed-exponent layer.  Two entries in this Step 33 note are superseded: the moving
volume term in §2 must be put into the curvature reaction by
\(|s+4|\le CF\), not bounded by \(C\delta K_p\) before defect persistence; and
the pre-absorption diffusion/tensor dissipation is
\(-pD_p^{\rm Rm}-p(p-2)D_p^F\), not the intermediate
\(-pD_p^{\rm Rm}-p(p-3)D_p^F\).  Step 34 also replaces the regularized
three-factor route to \(J_6\) by A03 Step 35's unregularized two-factor absorption
using \(w_6=\eta\chi^5|E|^3\) and only the localized \(K_2^\eta\) seed.

## 0. Purpose and scope

This note derives the curvature energy inequality
\[
K_p'+c_p\mathcal D_p
\le C p^N(r^{-2}+1+\mathcal S^2Y)K_p+C_0p
\tag{0.1}
\]
for the buffered cutoff flow on one macro-support, tracking every integration
by parts to identify which terms require full-tensor dissipation
\(D_p^{\operatorname{Rm}}\) and which need only the radial \(D_p^F\).  The
derivation uses the conventions from Step 32 / A03 Step 34:
\[
\partial_tg=-2aE,\qquad a=\chi^2,\qquad E=\operatorname{Ric}+g,
\]
\[
F=(1+|\operatorname{Rm}|^2)^{1/2},\qquad
K_p=\int a^{p-2}F^p\,d\mu,\qquad
z_p=a^{(p-1)/2}F^{p/2}.
\]
\[
\|z\|_4^2\le \mathcal S(\|\nabla z\|_2^2+r^{-2}\|z\|_2^2),
\qquad \mathcal S\asymp r^2/\sqrt V.
\tag{0.2}
\]
The auxiliary cutoff \(\eta\) satisfies \(\eta=1\) on \(\operatorname{supp}\chi\)
and \(\nabla\eta=0\) on \(\operatorname{supp}\chi\) (buffered stationary collar).
All integrals are over the support of \(\eta\).

The note is specific to dimension \(n=4\), but the calculation applies in
any dimension; only the Sobolev exponent and critical product change with \(n\).

## 1. Pointwise \(|\operatorname{Rm}|^2\) evolution

Under \(\partial_tg_{ij}=h_{ij}=-2aE_{ij}\), the curvature evolution is
\[
\partial_tR_{ijk}{}^l
=\nabla_i(\partial_t\Gamma^l_{jk})-\nabla_j(\partial_t\Gamma^l_{ik}),
\]
\[
\partial_t\Gamma^l_{jk}
=\tfrac12g^{lm}(\nabla_jh_{km}+\nabla_kh_{jm}-\nabla_mh_{jk}).
\]
The flow splits as \(h=-2a\operatorname{Ric}-2ag\).  The contribution of each
piece to \(\partial_t|\operatorname{Rm}|^2\) is enumerated below (schematic
bounds; sharp contractions appear in the signed dissipation calculation).

**A. Ricci-flow contribution** (\(h_1=-2a\operatorname{Ric}\)).

This gives the standard Lichnerowicz-type term multiplied by \(a\), plus cutoff
terms from the chain rule on \(a\).  At the level of \(|\operatorname{Rm}|^2\):
\[
\partial_t|\operatorname{Rm}|^2\big|_{h_1}
=a\Delta|\operatorname{Rm}|^2
-2a|\nabla\operatorname{Rm}|^2
+2a\langle\operatorname{Rm},\operatorname{Rm}*\operatorname{Rm}\rangle
+2\langle\operatorname{Rm},\nabla a*\nabla\operatorname{Rm}\rangle
+2\langle\operatorname{Rm},\nabla^2a*\operatorname{Rm}\rangle.
\tag{1.1}
\]
The first two terms are the Bochner pair.  The last two are cutoff terms.

**B. Conformal contribution** (\(h_2=-2ag\)).

This gives a curvature evolution
\(\partial_t\operatorname{Rm}|_{h_2}=-a\operatorname{Rm}
+g\owedge\nabla^2a+\nabla a\otimes\nabla a\),
contributing
\[
2\langle\operatorname{Rm},\partial_t\operatorname{Rm}|_{h_2}\rangle
=-2a|\operatorname{Rm}|^2+2\langle\operatorname{Rm},g\owedge\nabla^2a\rangle
+O(|\nabla a|^2|\operatorname{Rm}|).
\tag{1.2}
\]

**C. Metric variation of the norm.**

\[
\partial_t|T|^2\big|_{\text{metric}}
=-4h^{ip}T_{ijkl}T_p{}^{jkl}
=8aE^{ip}R_{ijkl}R_p{}^{jkl}
=8a|\operatorname{Rm}|^2+8a\mathring R^{ip}R_{ijkl}R_p{}^{jkl},
\tag{1.3}
\]
where \(\mathring R=\operatorname{Ric}-\frac sn g\) and the cubic contraction
is bounded by \(C|\operatorname{Ric}||\operatorname{Rm}|^2\le CF^3\).

**D. Volume form.**

\[
\partial_td\mu=-a(s+4)\,d\mu.
\tag{1.4}
\]

Assembling A--D and using \(F^2=1+|\operatorname{Rm}|^2\):
\[
\boxed{
\partial_tF^2=a\Delta F^2-2a|\nabla\operatorname{Rm}|^2
+\Sigma_{\operatorname{reac}}
+\Sigma_{\operatorname{cut}}
+\Sigma_{\operatorname{conf+met}},
}\tag{1.5}
\]
where
\begin{align}
|\Sigma_{\operatorname{reac}}|&\le CaF^3,\tag{1.6}\\
|\Sigma_{\operatorname{cut}}|&\le C(|\nabla a||\operatorname{Rm}||\nabla\operatorname{Rm}|
  +|\nabla^2a|F^2+|\nabla a|^2F),\tag{1.7}\\
|\Sigma_{\operatorname{conf+met}}|&\le CaF^2.\tag{1.8}
\end{align}
The bound (1.6) combines the Hamilton reaction from \(h_1\) and the cubic
contraction from the metric variation.  The bound (1.8) combines the conformal
\(-2a|\operatorname{Rm}|^2\) with the metric variation \(+8a|\operatorname{Rm}|^2\)
and the lower-order \(|\nabla a|^2|\operatorname{Rm}|\) terms; the net coefficient
depends on \(n\) but is a bounded constant.  The 1 inside \(F^2\) contributes
a controlled \(O(\operatorname{Vol})\) source.

## 2. Power energy computation

Set \(\psi=a^{p-2}\) (\(p\ge3\)).  Then
\[
K_p'=\tfrac p2\int\psi F^{p-2}\partial_tF^2\,d\mu
+\int\psi F^p\,\partial_td\mu.
\tag{2.0}
\]
The volume term:
\[
\left|\int\psi F^p\partial_td\mu\right|
=\left|\int a^{p-1}(s+4)F^p\right|
\le C\delta K_p.
\tag{2.V}
\]

### 2.1 Bochner term

\[
\mathcal B=\tfrac p2\int\psi F^{p-2}\cdot a\Delta F^2
=p\int a^{p-1}F^{p-1}\Delta F+p\int a^{p-1}F^{p-2}|\nabla F|^2.
\tag{2.1a}
\]
Integration by parts on the first integral.  Set
\(\phi=a^{p-1}F^{p-1}\); then
\[
\nabla\phi=(p-1)a^{p-2}(\nabla a)F^{p-1}
+(p-1)a^{p-1}F^{p-2}\nabla F.
\]
\[
p\int a^{p-1}F^{p-1}\Delta F
=-p\int\nabla\phi\cdot\nabla F
=-p(p-1)\int a^{p-2}F^{p-1}\nabla a\cdot\nabla F
-p(p-1)\int a^{p-1}F^{p-2}|\nabla F|^2.
\]
Combining:
\[
\mathcal B=-p(p-2)D_p^F
-p(p-1)\underbrace{\int a^{p-2}F^{p-1}\nabla a\cdot\nabla F}_{I_a^{\nabla F}},
\tag{2.1b}
\]
where
\[
D_p^F:=\int a^{p-1}F^{p-2}|\nabla F|^2.
\]

### 2.2 Kato term

\[
\mathcal K=-p\int\psi F^{p-2}\cdot a(|\nabla\operatorname{Rm}|^2-|\nabla F|^2)
=-p(D_p^{\operatorname{Rm}}-D_p^F),
\tag{2.2}
\]
where \(D_p^{\operatorname{Rm}}:=\int a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2\).
This is nonpositive by Kato \(|\nabla F|\le|\nabla\operatorname{Rm}|\).

### 2.3 Net dissipation from Bochner + Kato

\[
\mathcal B+\mathcal K=-pD_p^{\operatorname{Rm}}-p(p-3)D_p^F
-p(p-1)I_a^{\nabla F}.
\tag{2.3}
\]
For \(p\ge3\), both dissipation coefficients are nonnegative.

### 2.4 Absorption of \(I_a^{\nabla F}\) (cutoff--radial cross term)

Using \(\nabla a=2\chi\nabla\chi\), \(|\nabla a|\le 2|\nabla\chi|\le Cr^{-1}\),
and \(a^{p-3}|\nabla a|^2=4a^{p-2}|\nabla\chi|^2\):
\begin{align}
|p(p-1)I_a^{\nabla F}|
&\le p(p-1)\int a^{p-2}|\nabla a|F^{p-1}|\nabla F|\\
&\le\varepsilon D_p^F
+C_\varepsilon p^2(p-1)^2
 \int a^{p-3}|\nabla a|^2F^p\\
&\le\varepsilon D_p^F+4C_\varepsilon p^4r^{-2}K_p.
\tag{2.4}
\end{align}

### 2.5 Cutoff first-derivative term from \(\nabla a*\nabla\operatorname{Rm}\)

From (1.7), the contribution to \(\frac p2\int\psi F^{p-2}\Sigma_{\rm cut}\)
includes
\[
I_B=Cp\int a^{p-2}|\nabla a|F^{p-1}|\nabla\operatorname{Rm}|.
\tag{2.5a}
\]
Young's inequality:
\[
I_B\le\varepsilon D_p^{\operatorname{Rm}}
+C_\varepsilon p^2\int a^{p-3}|\nabla a|^2 F^p
\le\varepsilon D_p^{\operatorname{Rm}}+4C_\varepsilon p^2r^{-2}K_p.
\tag{2.5b}
\]
This is the term that requires full-tensor dissipation, not merely \(D_p^F\).

### 2.6 Hessian-of-\(a\) term after IBP

From (1.7), there is a contribution
\[
I_C=Cp\int a^{p-2}|\nabla^2 a|F^p.
\tag{2.6a}
\]
We integrate one derivative from \(\nabla^2a\) onto the test weight.  Set
\(\Phi=a^{p-2}F^p\).  Then (schematically):
\[
\int|\nabla^2a|\Phi
\lesssim\int|\nabla a||\nabla\Phi|+\text{boundary}.
\]
The gradient hits three factors:
\[
\nabla\Phi=(p-2)a^{p-3}(\nabla a)F^p+pa^{p-2}F^{p-1}\nabla F.
\]

**Derivative on \(a^{p-2}\):**
\[
(p-2)\int a^{p-3}|\nabla a|^2F^p
=4(p-2)\int a^{p-2}|\nabla\chi|^2F^p
\le4(p-2)r^{-2}K_p.
\tag{2.6b}
\]

**Derivative on \(F^p\):**
\[
p\int a^{p-2}|\nabla a|F^{p-1}|\nabla F|
\le\varepsilon D_p^F+C_\varepsilon p^2r^{-2}K_p.
\tag{2.6c}
\]
(Same Young as in 2.4, without the extra \(p-1\) factor.)

Combining:
\[
I_C\le Cp\bigl[\varepsilon D_p^F+C_\varepsilon p^2r^{-2}K_p+(p-2)r^{-2}K_p\bigr]
\le\varepsilon D_p^F+Cp^4r^{-2}K_p.
\tag{2.6d}
\]

**TTCS correction (Step 33).**  The original "schematic IBP of
\(|\nabla^2a|\)" is **invalid**: one cannot integrate by parts on an
absolute value.  Two correct routes exist.

*Route A (direct pointwise bound).*  If one has the evolving
cutoff-Hessian bound \(|\nabla^2_{g(t)}a|\le Cr^{-2}\) (which requires
the coupled cutoff-jet induction of A03 Step 34 §6), then directly
\[
I_C\le Cpr^{-2}K_p,
\tag{2.6d'}
\]
with no dissipation consumed.

*Route B (honest tensor IBP).*  Keep the tensor contraction
\(T_H=p\int a^{p-2}F^{p-2}(\nabla_i\nabla_ja)B^{ij}(\operatorname{Rm})\)
with \(|B|\le CF^2\) and integrate by parts on the actual
\(\nabla_i\nabla_ja\).  The derivative falls on three factors:
\begin{align}
|T_H|&\le p(p-2)\int a^{p-3}|\nabla a|^2F^p
+p(p-2)\int a^{p-2}|\nabla a|F^{p-1}|\nabla F|\notag\\
&\quad+p\int a^{p-2}|\nabla a|F^{p-1}|\nabla\operatorname{Rm}|.
\tag{2.6e}
\end{align}
The first two are \(\le Cp^Nr^{-2}K_p+\varepsilon D_p^F\).  The third
genuinely requires full-tensor dissipation:
\[
\varepsilon D_p^{\operatorname{Rm}}+C_\varepsilon p^Nr^{-2}K_p.
\tag{2.6f}
\]
Since \(D_p^{\operatorname{Rm}}\) is available from the Kato term (§2.2),
this absorption is safe.  In either route the total Hessian contribution
is bounded by
\(\varepsilon(D_p^{\operatorname{Rm}}+D_p^F)+Cp^Nr^{-2}K_p\).

### 2.7 Cubic reaction

\[
R_p:=Cp\int a^{p-1}F^{p+1}.
\tag{2.7a}
\]
The three-factor Hölder identity:
\[
a^{p-1}F^{p+1}=(aF^3)^{1/3}(a^{p-2}F^p)^{1/3}z_p^{4/3}.
\tag{2.7b}
\]
Hölder with exponents \((3,3,3)\):
\[
R_p\le Cp\,Y^{1/3}K_p^{1/3}\|z_p\|_4^{4/3},
\qquad Y:=K_3=\int aF^3.
\tag{2.7c}
\]
Sobolev (0.2) gives \(\|z_p\|_4^{4/3}\le\mathcal S^{2/3}
(Cp^2D_p^G)^{2/3}\) where
\[
D_p^G:=D_p^F+r^{-2}K_p+4r^{-2}K_p=D_p^F+Cr^{-2}K_p
\tag{2.7d}
\]
(with the second localization from \(|\nabla z_p|^2\)).
Young absorption with exponents \((3/2,3)\) on
\(Y^{1/3}K_p^{1/3}\) and \((D_p^G)^{2/3}\):
\[
R_p\le\varepsilon D_p^G
+C_\varepsilon p^N \mathcal S^2 Y K_p.
\tag{2.7e}
\]

### 2.8 Conformal + metric variation + volume

These together contribute at most
\[
Cp\int a^{p-1}F^p+C\delta K_p\le CpK_p+C\delta K_p\le CpK_p.
\tag{2.8}
\]

## 3. Assembled inequality

Choosing \(\varepsilon\) in §2.4--2.7 small enough to absorb into
\(-pD_p^{\operatorname{Rm}}-p(p-3)D_p^F\), we obtain:

\[
\boxed{
K_p'+c\bigl[pD_p^{\operatorname{Rm}}+p(p-3)D_p^F\bigr]
\le Cp^N\bigl(r^{-2}+1+\mathcal S^2Y\bigr)K_p+C_0p,
}\tag{3.1}
\]
where \(C_0=O(\operatorname{Vol})\) and \(N\) is a universal constant
(explicitly \(N\le 5\) from the highest power in the Young/Hölder chain).
For Moser iteration, the relevant dissipation is
\[
D_p:=D_p^F+r^{-2}K_p,
\]
and (3.1) implies
\[
K_p'+cp^2D_p\le Cp^N(r^{-2}+1+\mathcal S^2Y)K_p+C_0p.
\tag{3.2}
\]

## 4. Defect power inequality (structure)

For the regularized defect \(f_\varepsilon=(|E|^2+\varepsilon)^{1/2}\), set
\[
J_p=\int a^{p-2}f_\varepsilon^p,\qquad
D_p^E=\int a^{p-1}f_\varepsilon^{p-2}|\nabla E|^2.
\]
The evolution of \(|E|^2\) follows the same pattern as \(|\operatorname{Rm}|^2\),
but the curvature reaction is replaced by \(a\operatorname{Rm}*E*E\), bounded
by \(CaF|E|^2\).  No purely curvature term appears because \(E=0\) is preserved
by the flow.

Repeating the §2 calculation with \(F\) replaced by \(f_\varepsilon\) and using
Kato regularization gives, after the same IBP chain:
\[
\boxed{
J_p'+c_pD_p^E
\le Cp^N\bigl(r^{-2}+1+\mathcal S^2R_p^E/J_p\bigr)J_p+C_0'p,
}\tag{4.1}
\]
where the defect reaction
\[
R_p^E=\int a^{p-1}Ff_\varepsilon^p
\tag{4.2}
\]
replaces the curvature reaction \(R_p=\int a^{p-1}F^{p+1}\).  The same
three-factor absorption applies, with the cubic potential \(Y\) appearing
through \(aF\) rather than \(aF^3\).  Explicitly:
\[
a^{p-1}Ff_\varepsilon^p
=(aF^3)^{1/3}(a^{p-2}f_\varepsilon^p)^{1/3}\tilde z_p^{4/3},
\qquad\tilde z_p=a^{(p-1)/2}f_\varepsilon^{p/2}.
\]
Hölder and Young give the same absorption form:
\[
R_p^E\le\varepsilon D_p^E+C_\varepsilon p^N\mathcal S^2YJ_p.
\tag{4.3}
\]
Therefore (4.1) becomes
\[
\boxed{
J_p'+c_pD_p^E
\le Cp^N(r^{-2}+1+\mathcal S^2Y)J_p+C_0'p.
}\tag{4.4}
\]

### 4.1 \(J_6\) persistence from time zero

The Gronwall coefficient in (4.4) is \(\Lambda(t)=Cp^N(r^{-2}+1+\mathcal S^2Y(t))\).
From the already-established integrated curvature seed (A03 Step 34,
eq.~3.2):
\[
\int_0^TY(s)\,ds\le C\gamma K_2(0).
\tag{4.5a}
\]
Within the moving-Sobolev first-exit regime \(\mathcal S(t)\le 2\mathcal S(0)\):
\[
\int_0^T\mathcal S^2Y(s)\,ds
\le C\mathcal S(0)^2\int_0^TY(s)\,ds
\le C\mathcal S(0)^2\gamma K_2(0)
=C\gamma^3,
\tag{4.5b}
\]
using \(\gamma=\mathcal S(0)K_2(0)^{1/2}\).  No smoothness-at-zero
patching is used; the integrated seed gives a bounded coefficient
directly.  Hence
\[
\int_0^T\Lambda(s)\,ds
\le C\bigl[\gamma^3+r^{-2}T+T\bigr]=:C_\Lambda.
\tag{4.5}
\]
Therefore
\[
J_6(T)\le J_6(0)\exp(C_\Lambda).
\tag{4.6}
\]
For a maximal-function good center, \(K_0\) is bounded and \(r,\theta\) are
fixed, so \(C_\Lambda\) is a \textbf{sequence-uniform} constant.  Since
\(J_6(0)\le C\delta^6V\), we get
\[
\boxed{J_6(T)\le C\delta^6V.}\tag{4.7}
\]
This does not use the pointwise curvature bound \(\|aF\|_\infty\le C\gamma/t\),
avoiding the nonintegrable \(1/t\) singularity at \(t=0\).  The mechanism is
that the integrated curvature seed (4.5a) directly gives a bounded Gronwall
coefficient (4.5b) without any initial-interval smoothness patching.

**Regularization source.**  The \(C_0'p\) source in (4.4) arises from the
Kato regularization \(f_\varepsilon=(|E|^2+\varepsilon)^{1/2}\).  Since
\(E=0\) is preserved by the flow, the unregularized evolution of \(|E|\)
is homogeneous in \(E\) and has no curvature-only source.  The
\(\varepsilon\)-dependent contribution scales as
\(\varepsilon\cdot(\text{bounded})\) and vanishes uniformly as
\(\varepsilon\to0\) after the Gronwall bound is closed.  Thus the final
estimate (4.7) has no additive curvature-only term.

## 5. Endpoint forms (conditional summary)

From §3--4 and the nested Moser recurrence (Step 32, §3--4):

**Curvature** (\(p_0=3\), seed \(\int_{t/2}^tY\le C\gamma K_2\)):
\[
\|aF(t)\|_\infty\le C\gamma/t,\qquad t\in(0,T].
\tag{5.1}
\]

**Defect** (\(p_0=6\), seed \(J_6\le C\delta^6V\) from (4.7)):
\[
\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3},\qquad t\in(0,T].
\tag{5.2}
\]

**Velocity:**
\[
V(T)=\int_0^T\|aE\|_\infty\,dt
\le C\delta\theta^{2/3}r^2\to0\quad\text{as }\delta\to0.
\tag{5.3}
\]

All conditional on the tensor energy inequalities (3.1), (4.4), the curvature
seed (q=3 propagation), smooth first-exit geometry, and moving
Sobolev/metric comparability.

## 6. Verification

Script `workspace/scripts/step33_curvature_power_verification.py` checks:
1. Exponent matching in the Bochner IBP (§2.1)
2. Net dissipation coefficients (§2.3)
3. Young absorption balance in §2.4--2.6
4. Three-factor Hölder identity (§2.7b)
5. Gradient of \(z_p\) decomposition
6. Sobolev exponents and Moser product convergence
7. Defect reaction identity (§4.2--4.3)
8. Gronwall integral finiteness (§4.5)
9. Endpoint volume cancellations (§5)

## 7. References

- Step 25: q=2 tensor energy derivation (this session)
- Step 32: nested Moser repair and tensor audit (this session)
- A03 Step 34: restored weighted-flow state and obligations
- A03 Codex: shifted-curvature continuation framework
