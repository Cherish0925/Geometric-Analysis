# Step 58: Relative critical-to-subcritical bridge on the exact cutoff flow

Session: S0910A03. Agent3 / Actuator. Phase: Execute.

## 0. Purpose and correction

This note repairs the first-exit curvature branch at the earliest point where the
Step 57 assembly depended on an uncontrolled initial cubic moment.  We work on one
buffered support for the exact flow
\[
 \partial_tg=-2aE,\qquad E=\operatorname{Ric}_g+g,\qquad a=\chi^2,
\]
with
\[
 \chi=1\text{ on }B_{5r},\quad \operatorname{supp}\chi\subset B_{6r},
 \quad \eta=1\text{ on }B_{6r},\quad
 \operatorname{supp}\eta\subset B_{7r},
\]
and \(a=da=0\) on \(\operatorname{supp}d\eta\).  Put
\[
 T=\operatorname{Rm}+\frac{g\owedge g}{2(n-1)},\qquad
 F=F_T=(1+|T|^2)^{1/2}.
\]
The quantities are
\[
 H(t)=\int\eta^2F^2,\qquad
 D(t)=\int\eta^2a|\nabla T|^2,\qquad
 Y(t)=\int\eta^2aF^3.
\tag{0.1}
\]

The Step 57 formula
\[
 H(t)\lesssim H(0)+r^2Y(0)
\]
is unusable for a collapse-uniform first exit: the critical \(L^2\) curvature
budget imposes no bound on \(Y(0)\).  The correct direction is the reverse one:
control \(Y\) at every time by \(H\) and \(D\), absorb it directly in the
\(H\)-equation, and only then obtain a positive-time \(Y\)-slice.  Thus no
initial cubic curvature enters the observation time.

There are two different Sobolev variables and they must not be interchanged:
\[
 w_2=\chi F=a^{1/2}F
 \quad\text{for the critical }H\to\int Y\text{ step},
\tag{0.2}
\]
whereas
\[
 z_3=\eta aF^{3/2}
 \quad\text{for the }q=3\text{ evolution}.
\tag{0.3}
\]
The old expression \(a^{1/2}F^{3/2}\) loses one factor \(a^{1/2}\) in the
\(q=3\) gradient/dissipation interface.

## 1. Relative \(H\)-inequality: no global additive constant

The tensor calculation of Step 57 gives the principal, first-cutoff-derivative,
and signed-Hessian terms
\[
 H'+c_0D\le C_0Y+C_1(1+r^{-2})H.
\tag{1.1}
\]
This is the relative form of that calculation.  In particular, the displayed
additive constant in Step 57 (7.1) is removed as follows.

Every zero-order term is integrated over the active support and has one of the
forms
\[
 \int\eta^2a,\qquad
 \int\eta^2aF,\qquad
 \int\eta^2aF^2,\qquad
 \int\eta^2aF^3.
\]
Since \(0\le a\le1\), \(F\ge1\),
\[
 \int\eta^2a\le H,
 \qquad \int\eta^2aF\le H,
 \qquad \int\eta^2aF^2\le H,
 \qquad \int\eta^2aF^3=Y.
\tag{1.2}
\]
Terms left by signed integration by parts have size \(Cr^{-2}H\).  Thus a
constant bounded only by \(\operatorname{Vol}(M)\) is neither needed nor allowed;
all sources are local and relative to \(H\) or \(Y\).  The same observation
incorporates the norm and moving-measure terms, with any sharper
\(\|aE\|_\infty H\) coefficient retained later in the joint metric/Sobolev
bootstrap.

## 2. Direct critical absorption and spacetime \(Y\)

On the matched support, \(\eta=1\) wherever \(\chi\ne0\), hence
\[
 \begin{aligned}
 Y
 &=\int F(\chi F)^2\\
 &\le \|F\|_{L^2(\operatorname{supp}\chi)}\,\|\chi F\|_4^2\\
 &\le H^{1/2}\,\mathcal S
       \left(\|\nabla(\chi F)\|_2^2+r^{-2}\|\chi F\|_2^2\right).
 \end{aligned}
\tag{2.1}
\]
Here \(\mathcal S\) denotes the squared-norm Sobolev constant
\[
 \|v\|_4^2\le\mathcal S(\|\nabla v\|_2^2+r^{-2}\|v\|_2^2).
\tag{2.2}
\]
Because \(|dF|\le|\nabla T|\), \(|d\chi|\le C/r\), and \(\eta=1\) on the
active support,
\[
 \|\nabla(\chi F)\|_2^2
 \le 2\int a|\nabla T|^2+2\int|d\chi|^2F^2
 \le C(D+r^{-2}H),
\tag{2.3}
\]
and \(\|\chi F\|_2^2\le H\).  Consequently
\[
 \boxed{Y\le C\gamma(t)(D+r^{-2}H),\qquad
 \gamma(t):=\mathcal S(t)H(t)^{1/2}.}
\tag{2.4}
\]
This is the critical-to-subcritical bridge.  It uses \(w_2=\chi F\), not the
\(q=3\) variable.

On a provisional first-exit interval with \(\gamma(t)\le\gamma_*\) and
\(C_0C\gamma_*\le c_0/2\), substitution in (1.1) gives
\[
 \boxed{H'+c_1D\le C(1+r^{-2})H.}
\tag{2.5}
\]
Thus, for \(t\le\theta r^2\) and \(r\le1\),
\[
 H(t)\le e^{C\theta}H(0),
 \qquad
 \int_0^tD(s)\,ds\le C H(0).
\tag{2.6}
\]
Integrating (2.4), using \(\gamma(s)\le\Gamma\), gives
\[
 \boxed{
 \int_0^tY(s)\,ds
 \le C\Gamma\left(\int_0^tD(s)\,ds+r^{-2}\int_0^tH(s)\,ds\right)
 \le C\Gamma H(0).}
\tag{2.7}
\]
No \(Y(0)\), high Sobolev norm, or higher cutoff jet occurs.  If
\(\mathcal S(s)\le C\mathcal S(0)\), then
\[
 \int_0^t\mathcal S(s)^2Y(s)\,ds
 \le C\mathcal S(0)^2\Gamma H(0)
 \le C\Gamma^3,
\tag{2.8}
\]
where the last inequality uses
\(\mathcal S(0)H(0)^{1/2}=\gamma(0)\le\Gamma\).  This is the
integrable reaction coefficient required by every later curvature and defect
ladder.

The collapse cancellation is explicit: if
\(\mathcal S(0)\lesssim r^2V^{-1/2}\) and \(H(0)\lesssim K_0V\), then
\[
 \gamma(0)\lesssim r^2\sqrt{K_0},
\tag{2.9}
\]
independent of \(V\).  Smallness is obtained by choosing the working scale from
the local critical energy threshold, not by a noncollapse assumption.

## 3. The genuine \(q=3\) equation and positive-time slice

For \(p\ge3\) define
\[
 K_p=\int\eta^2a^{p-2}F^p,
 \quad
 z_p=\eta a^{(p-1)/2}F^{p/2},
\tag{3.1}
\]
with tensor and radial dissipations
\[
 D_p^T=\int\eta^2a^{p-1}F^{p-2}|\nabla T|^2,
 \qquad
 D_p^F=\int\eta^2a^{p-1}F^{p-2}|dF|^2.
\tag{3.2}
\]
The shifted tensor has the same principal derivative as \(\operatorname{Rm}\),
\(\nabla T=\nabla\operatorname{Rm}\).  Repeating the signed Hessian calculation
with test \((p/2)\eta^2a^{p-2}F^{p-2}\), the curvature Hessian contraction has
\[
 B_{\rm curv}=T*E+\text{dimensionally bounded lower contractions},
 \quad |B_{\rm curv}|\le CF^2,
 \quad |\nabla B_{\rm curv}|\le CF|\nabla T|.
\tag{3.3}
\]
All \(G\)-evolution and normalization terms are algebraic and are dominated by
\(Ca^{p-1}F^{p+1}+Ca^{p-1}F^p\).  Since \(F\ge1\), the latter is no larger
than the former.  The same signed integration by parts as in the \(p=2\) case
therefore gives
\[
 \boxed{
 K_p'+c\{pD_p^T+p(p-2)D_p^F\}
 \le Cp^N(1+r^{-2}+\mathcal S^2Y)K_p,
 \qquad p\ge3,}
\tag{3.4}
\]
for a fixed finite \(N\) (the existing tensor allocation gives \(N\le5\)).
There is no additive support-independent source.

The reaction estimate in (3.4) uses the exact three-factor identity on the
active set
\[
 a^{p-1}F^{p+1}
 =(aF^3)^{1/3}(a^{p-2}F^p)^{1/3}
   (a^{p-1}F^p)^{2/3}.
\tag{3.5}
\]
Hölder \((3,3,3)\) yields factors \(Y^{1/3}\), \(K_p^{1/3}\), and
\(\|z_p\|_4^{4/3}\).  This uses \(\eta=1\) on \(\operatorname{supp}a\);
equivalently one may distribute \(\eta^{2/3}\) among all three factors.
Sobolev on \(z_p\) and Young then give (3.4).

At \(p=3\),
\[
 z_3=\eta aF^{3/2},
 \quad z_3^2=\eta^2a^2F^3,
 \quad z_3^4=\eta^4a^4F^6.
\tag{3.6}
\]
This exactly matches the \(a^2\)-weighted dissipation in the \(K_3\) equation.
The variable \(\eta a^{1/2}F^{3/2}\) would instead have square weight \(a\)
and cannot be used here.

From (2.7), for every \(t>0\) there exists
\(\tau\in[t/4,t/2]\) such that
\[
 Y(\tau)\le {4\over t}\int_{t/4}^{t/2}Y(s)\,ds
 \le {C\Gamma H(0)\over t}.
\tag{3.7}
\]
Integrating (3.4) at \(p=3\) from \(\tau\) to \(t\), and using
\(t\le\theta r^2\) and (2.8), yields
\[
 \boxed{
 Y(t)\le {C\Gamma H(0)\over t},
 \qquad
 \mathcal S(t)^2Y(t)\le {CA^2\Gamma^3\over t}.}
\tag{3.8}
\]
Here \(\mathcal S(t)\le A\mathcal S(0)\) and
\(\mathcal S(0)H(0)^{1/2}=\gamma(0)\le\Gamma\).  This \(t^{-1}\) coefficient is used only on positive
dyadic slabs; it is never integrated from zero.

## 4. Curvature Moser endpoint from the curvature ladder

The curvature endpoint must come from (3.4), not from the all-\(p\) defect
inequality of Step 39.  Fix \(t>0\) and nested slabs
\[
 I_j=[\tau_j,t],\qquad
 \tau_j=t(1-2^{-(j+1)}),
 \qquad p_j=3(3/2)^j.
\tag{4.1}
\]
On \(I_0=[t/2,t]\), (3.8) gives
\(\mathcal S^2Y\le C\Gamma^3/t\).  A time cutoff in (3.4), followed by the
gradient identity
\[
 \|\nabla z_p\|_2^2
 \le Cp^2(D_p^T+D_p^F+r^{-2}K_p),
\tag{4.2}
\]
gives
\[
 \sup_{I_{j+1}}K_{p_j}
 +\int_{I_{j+1}}\|\nabla z_{p_j}\|_2^2
 \le L_j\int_{I_j}K_{p_j},
\tag{4.3}
\]
where a safe uncompressed coefficient is
\[
 L_j=Cp_j^{N+2}\left(\frac{4^j}{t}+1+r^{-2}+\frac{A^2\Gamma^3}{t}\right),
 \qquad L_j\ge r^{-2}.
\tag{4.4}
\]
Under the first-exit bounds \(\Gamma\le\Gamma_*\), \(t\le r^2\le1\), this may
be enlarged to \(C_{\Gamma_*,A}p_j^{N+2}4^j(t^{-1}+r^{-2})\).
The weighted interpolation is
\[
 K_{2p}=\|z_p\|_4^4,
 \qquad
 K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2}.
\tag{4.5}
\]
Spatial Sobolev plus time Hölder first gives the precise recurrence
\[
 \mathcal M_{p_{j+1},j+1}
 \le C\mathcal S(L_j\mathcal M_{p_j,j})^{1/2}
      (L_j+r^{-2})\mathcal M_{p_j,j},
 \qquad
 \mathcal M_{p,j}=\int_{I_j}K_p.
\tag{4.6}
\]
Since (4.4) chooses \(L_j\ge r^{-2}\), this simplifies to
\(\mathcal M_{p_{j+1},j+1}\le
 C\mathcal S(L_j\mathcal M_{p_j,j})^{3/2}\).
Writing \(m_j=\mathcal M_{p_j,j}^{1/p_j}\),
\[
 m_{j+1}\le(C\mathcal S)^{2/(3p_j)}L_j^{1/p_j}m_j.
\tag{4.7}
\]
Both products converge because
\[
 \sum_jp_j^{-1}=3/p_0=1,
 \quad
 \sum_j{\log p_j+j\over p_j}<\infty,
 \quad
 {2\over3}\sum_jp_j^{-1}=2/p_0=2/3.
\tag{4.8}
\]
The seed comes from (2.7):
\[
 \mathcal M_{3,0}=\int_{t/2}^tY(s)\,ds\le C\Gamma H(0).
\tag{4.9}
\]
The total time-cutoff exponent is \(-3/p_0=-1\), while the Sobolev exponent
is \(2/p_0=2/3\).  Therefore
\[
 \|aF(t)\|_\infty
 \le {C\over t}\mathcal S^{2/3}(\Gamma H(0))^{1/3}.
\tag{4.10}
\]
Since \(\mathcal S H(0)^{1/2}\le C\Gamma\) on the first-exit interval,
\[
 \mathcal S^{2/3}(\Gamma H(0))^{1/3}
 =\Gamma^{1/3}(\mathcal S H(0)^{1/2})^{2/3}
 \le C\Gamma.
\]
Thus
\[
 \boxed{\|aF_T(t)\|_\infty\le {C\Gamma\over t}.}
\tag{4.11}
\]
This endpoint is free of \(Y(0)\) and collapse volume.  Polynomial \(p\)-loss
in (3.4) changes only the finite constant through (4.8).

## 5. What this establishes and what remains

The corrected curvature branch on any smooth provisional first-exit interval is
\[
 H(0)
 \Longrightarrow H(t),\ \int(D+Y)
 \Longrightarrow Y(t)\lesssim\Gamma H(0)/t
 \Longrightarrow \|aF_T(t)\|_\infty\lesssim\Gamma/t.
\tag{5.1}
\]
It never uses \(Y(0)\).  The only cutoff information in its constants is the
first derivative bound and the strict support buffer.  The algebraic and
exponent identities were checked in
`workspace/scripts/step58_critical_subcritical_verify.py` (54/54 checks).
The source tensor calculation is A01 Steps 34--35 together with the shifted
\(T\) calculation in A03 Step 57; the shift contributes only bounded algebraic
terms and preserves \(\nabla T=\nabla\operatorname{Rm}\).

This does not by itself establish the common observation time.  The defect
ladder must be coupled back to the metric/Sobolev first-exit pair, and positive-
time continuation across the small-\(a\) collar still needs a finite collection
of coupled levels sufficient to recover the Step 56 restart norm.  In
particular, pointwise bounded curvature does not bound \(C_3=\nabla^3\chi\) or
higher cutoff jets; the next pair still contains \(\chi C_4*U\) while
\(\partial_tC_3\) contains \(U_2\).  These terms require the signed staggered
estimates, not ordinary Shi estimates outside the plateau.

Even after that analytic mechanism is complete, it concerns a restricted
four-dimensional negative Ishida--LeBrun laboratory.  It is not a proof or
disproof of the all-dimensional Yau Problem 26 statement.
