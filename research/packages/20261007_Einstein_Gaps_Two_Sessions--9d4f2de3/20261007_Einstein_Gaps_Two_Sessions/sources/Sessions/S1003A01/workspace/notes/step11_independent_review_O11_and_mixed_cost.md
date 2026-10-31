# Step 11 — Independent review of the subthreshold cell and the corrected next cost problem

Session S1003A01, Agent4, Execute.

## 1. Review conclusion

The finite-scale perpendicular-cell theorem survives independent review.  For the explicit metric

\[
 g=\frac{dx^2}{4G}+F\sigma_1^2+x\sigma_2^2+xe^w\sigma_3^2,
 \qquad x_0=10^{-2},\quad X=8,
\]

whose 24 coefficient entries are the exact dyadic rationals represented by the binary64 numbers stored in
`workspace/data/perp_collar/x0.01_X8_J_d8.json`, the strict Arb implementation
`workspace/scripts/perp_rigorous_enclosure.py` now proves

\[
 \frac{J_6(g)}{8\pi^2}
 =\frac1{8\pi^2}\int|\operatorname{Ric}_g+6g|^2dV_g
 \in[0.999116243135324311\pm2.24\times10^{-19}].
\]

The local strict output is
`workspace/data/perp_collar/strict_rigorous_x0.01_X8_J_d8.json`.
It also encloses

\[
 \frac{P}{8\pi^2}=[0.999108702733592648\pm4.57\times10^{-19}],
 \qquad
 \frac{J_6-P}{8\pi^2}=[7.540401731663\times10^{-6}\pm3.79\times10^{-19}],
\]

and the exact decomposition \(J_6=P+(J_6-P)\) is reproduced at a separately split 320-bit integration to radius about \(5.1\times10^{-24}\).

No step of this review found a mathematical defect in the desingularized Ricci formula, the volume normalization, the bolt expansion, the exact-collar smoothing, the topological identification, or the global transfer.  Thus there is a smooth exact-CH-collar ordinary blow-up cell with
\[
 J_1<8\pi^2,
\]
and a balanced sequence over a suitable tower of covers with
\[
 \limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}<4.
\]
This gives a rigorous negative answer to the inherited coefficient-four question O11 in its universal-optimality form.  It does **not** determine the sharp first coefficient.

## 2. What was independently checked

### 2.1 Profile transcription and the strict enclosure

The executable perpendicular profile with `wpow=2`, `beta0=0` is
\[
\begin{aligned}
F&=(x-x_0)e^{q_F}+x_0S(u),\\
G&=\bigl(x-x_0+(x^2+x_0)S(u)\bigr)e^{q_G},\\
w&=\log(1+x)S(u)+u^2(1-u)^3C_w(u),
\end{aligned}
\]
where \(u=\log(x/x_0)/\ell\), \(S=10u^3-15u^4+6u^5\), and \(q_F,q_G\) use degree-seven Chebyshev expansions times \((1-u)^3\).  The derived shift of the constant term in \(q_G\) enforces \(q_F(0)+q_G(0)=0\) exactly.  Direct pointwise comparison against the independent peer reconstruction gave profile differences at five interior points between \(10^{-18}\) and \(3\times10^{-14}\), consistent with binary64 evaluation.

The Step-10 code's only avoidable trust-base caveat was that the Taylor-tail radius for
\(\phi(z)=(e^z-1)/z\) passed through a Python float.  Following the peer stress test, this was replaced locally by a pure-Arb implementation using `abs(z).lower()` and `abs(z).upper()`.  If the ball is separated from zero, the exact quotient formulas are used; otherwise the entire series is used with a rigorous geometric tail, increasing the truncation order if necessary so \(r/(N+1)<1\).  The local rerun exactly reproduced the peer strict result above.  All logarithms and square roots forward Arb's `analytic` flag; division by a ball containing zero returns a nonfinite enclosure and forces subdivision.  Hence the callback satisfies the `acb_calc_integrate` holomorphy contract.

The original JSON `P` and `J` fields are low-order optimization quadrature metadata and do not lie in the final narrow balls.  They play no role in the theorem.  The proof object is the Arb ball string in the strict output.  Similarly, JSON `lower`, `upper`, and `eta_certified` are binary64 convenience fields; rigorous citation should use the ball itself.

There is a documentation error in the header of the peer's `o11_perp_cell.py`: it mentions an extra \(xe^{-w}\) slot.  The executable code, frozen theorem, local enclosure, and independent reconstruction all use precisely \(F,x,xe^w\), as displayed above.

### 2.2 Curvature algebra and normalization

For a diagonal Bianchi-IX metric \(dt^2+\sum a_i^2\sigma_i^2\), with
\(d\sigma_i=2\sigma_j\wedge\sigma_k\), the enclosure uses
\[
 R_{00}=-\sum_i\frac{\ddot a_i}{a_i},\qquad
 R_{ii}=-\frac{\ddot a_i}{a_i}
 -\frac{\dot a_i}{a_i}\left(\frac{\dot a_j}{a_j}+\frac{\dot a_k}{a_k}\right)
 +\frac{2(a_i^4-(a_j^2-a_k^2)^2)}{a_i^2a_j^2a_k^2}.
\]
The symbolic comparison to the independently Cartan-derived tensor gives four zero residuals, and the bolt rewrites \(D_1,A_1,A_2,A_3\) likewise reduce exactly to zero.  Factoring
\[
 y=x-x_0,\qquad F=y\widehat F,\quad G=y\widehat G,\quad w=y^2\widehat w
\]
removes every apparent division by the collapsing direction.  The code then evaluates a holomorphic extension of the real density rather than a non-holomorphic absolute square.

With \(\int\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2\),
\[
 dV=\pi^2 x e^{w/2}\sqrt{\widehat F/\widehat G}\,dx,
\]
so the coded factor
\[
 \frac18xe^{w/2}\sqrt{\widehat F/\widehat G}\,\ell x\,du
\]
is exactly \(dV/(8\pi^2)\).  Thus the enclosed quantity is \(J_6/(8\pi^2)\), not a surrogate.

### 2.3 Bolt, topology, and smoothing

At the bolt,
\[
 F=f_1y+O(y^2),\quad G=g_1y+O(y^2),\quad f_1g_1=1,\quad w=O(y^2).
\]
For \(dt=dx/(2\sqrt G)\), this gives
\[
 F=t^2+O(t^4),\qquad x-xe^w=O(t^4).
\]
Under the chosen Maurer–Cartan normalization the collapsing Hopf circle has period \(2\pi\), so the first equation is the full-period no-cone condition.  The normal two-plane has isotropy weight two and its traceless quadratic part weight four, making the \(O(t^4)\) anisotropy exactly the smoothness condition.  The bolt is an ordinary \((-1)\)-sphere.

The circles dual to \(\sigma_1\) and \(\sigma_3\) are conjugate Hopf circles of the same handedness.  A conjugating rotation near the bolt can be deformed to the identity through the free-orbit region, producing an orientation-preserving diffeomorphism that is the identity on the outer collar.  Hence the perpendicular cell is
\[
 D\#\overline{\mathbb{CP}}^{\,2}
\]
rel outer boundary; it is not an oppositely oriented \(\mathbb{CP}^2\) cell.

At \(X\), each deviation from CH vanishes to third order.  If a width-\(\delta\) flat cutoff is applied, its two-jet differs from CH by \(O(\delta)\) on a region of volume \(O(\delta)\).  Since \(\operatorname{Ric}+6g\) vanishes at the CH two-jet,
\[
 |J_6(g_\delta)-J_6(g)|=O(\delta^3).
\]
For sufficiently small fixed \(\delta\), the metric is positive, smooth, unchanged near the bolt, and exactly CH on an outer collar.  The strict frozen margin is therefore preserved.  No second interval integration is needed.

### 2.4 Scaling, covers, and transfer

For \(\widetilde g=6g\),
\[
 \operatorname{Ric}_{\widetilde g}=-\widetilde g\quad\text{on the collar},
 \qquad
 \int|\operatorname{Ric}_{\widetilde g}+\widetilde g|^2dV_{\widetilde g}=J_6(g),
\]
because a covariant two-tensor norm contributes \(6^{-2}\) and four-dimensional volume contributes \(6^2\).

Residual finiteness supplies a finite cover with the fixed radius-\(\sqrt6\operatorname{arsinh}\sqrt8\) ball and buffer embedded: only finitely many lattice elements move a chosen lift by at most twice that radius, and a finite-index subgroup can avoid all of them.  Any further cover contains a number of disjoint lifted balls proportional to its degree and hence to \(A_j\).  Since \(Q_j=o(A_j)\), this supplies all surgery sites for an existential balanced sequence.

With \(k_j/Q_j\to2/9\) and \(\ell_j/Q_j\to7/36\), the I54 accounting gives
\[
 \limsup\frac{\alpha(M_j)}{h_j}
 \le \frac{28}{9}+\frac{J_1}{9\pi^2}.
\]
For the strict X=8 frozen value \(\eta_8=1-J_6/(8\pi^2)>0.0008837568646756\), a fixed sufficiently small smoothing gives some strict number below four; letting the smoothing widths tend to zero diagonally gives
\[
 \limsup\frac{\alpha(M_j)}{h_j}
 \le 4-\frac{8\eta_8}{9}
 <3.999214438342511.
\]
A fixed-width conservative form is \(4-4\eta_8/9<4\).  This statement applies to a suitably chosen cover tower, not every preassigned tower.

## 3. Pure handles are rigid at the local exact-CH level

Step 10 proposed searching for a pure handle cell below \(32\pi^2\ell\).  This is already impossible.

Let
\[
 C=D\#\ell(S^1\times S^3)
\]
carry any smooth metric equal to the \(\operatorname{Ric}=-g\) CH metric on its full outer collar, and put
\[
 J(C)=\int_C|\operatorname{Ric}+g|^2.
\]
Insert one fixed copy into arbitrarily large finite covers with \(c_1^2=A\).  The resulting handle-only manifold has \(h_A=4\ell/A\), and the exact cell formula yields
\[
 \frac{\mathcal E(g_A)}{h_A}\longrightarrow\frac{J(C)}{8\pi^2\ell}.
\]
The inherited all-metric theorem gives
\[
 \alpha(M_A)=\frac{4h_A}{1+h_A},
\]
and \(\alpha(M_A)\le\mathcal E(g_A)\).  Hence
\[
 \frac{J(C)}{8\pi^2\ell}\ge4,
\qquad\boxed{J(C)\ge32\pi^2\ell}.
\]
The inherited equality theory makes the inequality strict for each fixed smooth \(\ell>0\) cell, while shrinking handle cores approach the value.  Thus
\[
 \inf J(C)=32\pi^2\ell
\]
and the infimum is not attained for \(\ell>0\).

An equivalent relative identity is
\[
 J(C)-32\pi^2\ell
 =\frac{S_C-16d}{12}+4B_C+\frac14\int_C(s+4)^2,
\]
where \(S_C=\int_Cs^2\), \(B_C=\int_C|W^-|^2\), and \(d=\operatorname{Vol}(D)\).  Gluing the cell into a CH cover and applying the inherited metricwise scalar inequality gives \(S_C\ge16d\), so every term on the right is nonnegative.

Consequently, the \(28/9\) floor of a construction that treats all handles in separate pure-handle cells is not removable by a better isolated handle ansatz.

## 4. The distinct mixed-cell problem

For
\[
 C=D\#k\overline{\mathbb{CP}}^{\,2}\#\ell(S^1\times S^3),
\qquad q=k+4\ell,
\]
define the unrestricted exact-CH cell cost
\[
 \mathfrak J_{k,\ell}=\inf_C\int_C|\operatorname{Ric}+g|^2,
\]
allowing the outer CH ball radius to vary.  The established facts include
\[
 \mathfrak J_{0,\ell}=32\pi^2\ell,
 \qquad
 \mathfrak J_{1,0}<8\pi^2.
\]
Pure-handle rigidity does **not** imply
\[
 \mathfrak J_{k,\ell}\ge\mathfrak J_{k,0}+32\pi^2\ell.
\]
A connected mixed cell need not split along exact CH collars, and the scalar and Weyl terms belong to the whole metric.

The common relative identity can be written
\[
 J-8\pi^2q
 =\frac{S_C-16d}{12}+\frac14\int_C(s+4)^2
 -4\left(\frac{2d}{3}-W_C\right),
\]
with
\[
 \frac{2d}{3}-W_C=12\pi^2k-B_C\le12\pi^2k.
\]
Thus handles add topological cost but supply no independent positive self-dual-Weyl-depletion budget; only blow-ups do.  A mixed saving, if present, must arise because handle topology changes how the same metric uses the blow-up-funded Weyl depletion and pays its scalar/Ricci cost.  This is collective nonadditivity, not isolated handle improvement.

For the balanced proportions the smallest integer mixed block is \((k,\ell,q)=(8,7,36)\).  Its coefficient is
\[
 c_{\rm mix}=\frac{\mathfrak J_{8,7}}{72\pi^2}.
\]
The separated construction costs
\[
 \mathfrak J_{\rm sep}=8\mathfrak J_{1,0}+224\pi^2.
\]
The interaction question is therefore
\[
 \boxed{\mathfrak J_{8,7}<8\mathfrak J_{1,0}+224\pi^2\ ?}
\]
More generally one should study subadditivity and the large-block limit of \(\mathfrak J_{k,\ell}\).  To beat the separated construction's absolute \(28/9\) floor one would need the much stronger inequality
\[
 \mathfrak J_{8,7}<224\pi^2.
\]
This remains distinct from both the single-blow-up infimum \(\mathfrak J_{1,0}\) and unrestricted global competitors not assembled from fixed exact-CH cells.

## 5. Corrections to the Step-10 synthesis

1. The statement “can handle cells be improved below \(32\pi^2\)” must be deleted as an open route.  The answer is no for every pure-handle exact-CH cell.
2. The original float-based Taylor radius has been replaced in the local proof script by a pure-Arb radius; the strict output is now the canonical certificate.
3. The frozen profile is an exact dyadic-coefficient metric, not an exact-decimal-rational metric.
4. The narrow Arb ball does not contain the low-order `P` and `J` metadata stored by the optimizer; those numbers are not proof inputs.
5. The peer high-precision output reruns the regularized enclosure implementation.  Genuine formula independence comes from the peer JAX spin/transgression reconstruction, which matches the strict center to about \(10^{-15}\).
6. The O11 result changes the sharp question rather than completing the broader Einstein-gap programme.  Matching lower bounds, mixed-cell cost, multi-blow-up interaction, unrestricted competitors, degeneration, O10, and fixed-manifold attainment remain active.
