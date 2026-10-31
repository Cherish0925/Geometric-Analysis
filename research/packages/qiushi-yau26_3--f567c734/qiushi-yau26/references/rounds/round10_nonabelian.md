# Full-rank nonabelian seeds have a non-small final curvature equation

21 September 2026.

The partial seeds from round 9 solve Dirac and determinant curvature,
but not the remaining traceless-curvature equation. This note proves
that, for balanced slow-interpolation metrics and a fixed uniformly
positive polar factor, that remaining equation has a positive averaged
residual. Neither a small critical-curvature change of connection nor a
small `L4` change of spinor can remove it.

The main identity applies to arbitrary coupled connections, not merely
parallel spinors or reducible ansatzes. A possible solution must instead
acquire a definite anti-self-dual nonabelian curvature energy, lose rank,
or leave the seed by a non-small amount. No Einstein nonexistence or
nonabelian-moduli emptiness is inferred.

## 1. Quadratic map and conventions actually used

Let `W=S_L^+`, `E=W`, and `phi:W->E`. The curvature equation is

\[
                     F_A^+=\tau(\phi).                 \tag{1}
\]

The quadratic map is the source-factor trace-free projection on the
published p. 21 of [Leung, *Non-Abelian Seiberg--Witten equations on
Einstein manifolds*](https://archive.ymsc.tsinghua.edu.cn/pacm_download/60/582-2000_Leung_NonAbelian_SW_eqt_on_Einstein_mfd_Crelle_Journal.pdf).
It retains the full target `u(E)` factor. In particular, it is not the
fixed-determinant PU(2) quadratic map.

Use the positive Hilbert--Schmidt norm on endomorphisms. As in round 9,
define the positive normalization constant `kappa` by

\[
 |\operatorname{tr}_E\tau(\phi)|
      =\kappa\,|\sigma_1^2-\sigma_2^2|,                 \tag{2}
\]

where `sigma_i` are the singular values. Thus `kappa` is the norm of
the target trace of the quadratic map of a unit rank-one field. For
coefficient-one tensor projection and Clifford norm
`|rho(eta)|_HS=2|eta|`, `kappa=1/(2 sqrt(2))`. Keeping `kappa` explicit
allows the printed Clifford normalization without guessing its scale.
The sign, transpose, and source-dual identifications do not affect any
norm identity below.

**Lemma 1 (the determinant term).** At every point,

\[
\begin{split}
 |\tau(\phi)|^2
   &=\kappa^2\left[(\sigma_1^2-\sigma_2^2)^2
                      +6\sigma_1^2\sigma_2^2\right],\\
 |\operatorname{tr}\tau(\phi)|^2-|\tau(\phi)|^2
   &=-6\kappa^2\det(\phi^*\phi).
\end{split}                                                   \tag{3}
\]

**Proof.** Use singular-value frames, so `phi=diag(x,y)`, `x,y>=0`.
Take a self-dual basis `eta_1,eta_2,eta_3` of squared norm two. Up to
orthogonal changes of the source basis, a possible transpose in the
second Pauli matrix, and a common sign, the coefficients of `tau` are

\[
                  i c H\sigma_jH,\qquad
 H=\operatorname{diag}(x,y),\qquad c=\kappa/\sqrt2.
\]

Their squared norms sum to
`2c²(x⁴+y⁴+4x²y²)`, whereas the squared target-trace norm is
`2c²(x²-y²)²`. Their difference is `-12c²x²y²`.
This proves (3), including at rank loss by continuity. QED.

Only the source-factor tensor projection is needed. The disputed
transfer of a parallel field in Leung's equality argument, recorded
in the appendix to round9_nonabelian.md, is not used.

## 2. A full coupled anti-self-dual energy identity

Use the Chern convention `c_1(E)=[i tr F_A/(2 pi)]`. The symbol `c_2(E)`
below means its evaluation on the oriented fundamental class. For an
endomorphism-valued two-form `B`, put

\[
                       q(B)=|\operatorname{tr}B|^2-|B|^2.
\]

Since `E` has rank two, `q(B)=|B_cent|²-|B_0|²`; the corresponding
quadratic-form operator has norm one. Chern--Weil theory gives

\[
             8\pi^2c_2(E)=\int_X[q(F_A^+)-q(F_A^-)].   \tag{4}
\]

The sign can be checked on an `SU(2)` anti-self-dual connection:
the right side is `integral |F_A^-|²`, hence `c_2>=0`.

**Theorem 2.** Every solution of the full curvature equation (1),
whether or not its Dirac equation holds, satisfies

\[
 \boxed{\quad
 \|(F_A^-)_0\|_2^2
 =8\pi^2c_2(E)+\tfrac12\|\operatorname{tr}F_A^-\|_2^2
                +6\kappa^2\int_X\det(\phi^*\phi).
 \quad}                                                    \tag{5}
\]

For an arbitrary pair with residual `R=F_A^+-tau(phi)`, if `c_2(E)=0`,

\[
 \boxed{\quad
 6\kappa^2\int_X\det(\phi^*\phi)
 \le\|(F_A^-)_0\|_2^2
                   +2\|\tau(\phi)\|_2\|R\|_2+\|R\|_2^2.
 \quad}                                                    \tag{6}
\]

**Proof.** Substitute (3) into (4), and use
`q(F_A^-)=|tr F_A^-|²/2-|(F_A^-)_0|²` to get (5).
For a residual, the error in replacing `q(tau+R)` by `q(tau)` is at
most `2|tau||R|+|R|²`, since the quadratic-form operator of `q` has
norm one. Drop the nonpositive term `-|tr F_A^-|²/2` and integrate.
QED.

On every canonical almost-complex spin-c bundle,
`W=C plus K^{-1}` and `c_2(W)=0`. Thus (5)--(6) apply to the actual
surface bundles, not just to the exact product. If a sequence has
bounded `||phi||4`, `||R||2->0`, and `||(F_A^-)_0||2->0`, then

\[
                         \int_X\sigma_1^2\sigma_2^2\to0.\tag{7}
\]

This is rank loss in the integrated determinant, not a claim that the
spinor converges pointwise or that its image becomes parallel. The
connection may remain genuinely coupled.

For other spin-c structures `c_2(W)=(a²-T)/4`, `T=2chi+3tau`, and
the exact topological term in (5) must be retained. Changing the
determinant is not a way to reuse the canonical zero term silently.

## 3. The exact product residual

On the product of two curvature `-1` surfaces, choose the complex
orientation and let `omega` be its Kähler form, `|omega|²=2`. In the
canonical splitting `W=C plus K^{-1}`, the induced connection is

\[
           A_0=d\oplus B,\qquad F_{A_0}=\operatorname{diag}(0,i\omega),
           \qquad F_{A_0}^-=0.                          \tag{8}
\]

Here curvature means the curvature of the unitary covariant derivative;
with `rho_Ric=-omega`, the anticanonical curvature is `-i rho_Ric=i omega`.
The canonical spinor description and this line-curvature convention are
also given in [Dai--Wang--Wei, *On the Stability of Kähler--Einstein
Metrics*, Section 2](https://users.math.msu.edu/users/xwang/dww3.pdf).

Take a positive parallel `H=diag(x,y)` solving the trace equation.
It is a Dirac solution for `A_0` because source and target connections
are the induced ones. Define

\[
 q_0={1\over\sqrt2\kappa}={1\over2c},\qquad
 t={x^2+y^2\over2}>q_0,\qquad m=2ct=\sqrt2\kappa t>1.  \tag{9}
\]

The two possible relative-sign labelings have
`x²=t+epsilon q_0`, `y²=t-epsilon q_0`, `epsilon=+1` or `-1`.
In that labeling the Kähler-form coefficient of `tau(H)` is
`epsilon i c diag(x²,-y²)`, and the two perpendicular coefficients
have magnitude `cxy`. The trace equation is exactly
`epsilon c(x²-y²)=1`.

The complete, trace-free residual has squared norm

\[
\begin{split}
 |F_{A_0}^+-\tau(H)|^2
   &=4c^2x^4+8c^2x^2y^2\\
   &=3m^2+2\epsilon m-1\\
   &\ge(m-1)(3m+1)>0.                                \tag{10}
\end{split}
\]

The first term is the target-diagonal residual in the `omega`
direction. The second comes from the two self-dual directions
perpendicular to `omega`, where the product connection has zero
curvature but the quadratic map has off-diagonal entries proportional
to `xy`. In particular the calculation does not omit the off-diagonal
target equations.

The inequality and its strict positivity for `m>1` are valid in either
relative-sign convention. No assertion about which rank-one endpoint
solves the published system is needed or made. The exact source-dual
and curvature-sign comparison still matters for that endpoint: at
`m=1` the two displayed branches have residual squared zero and four,
respectively. One must not use the smaller branch as an existence claim.
What (10) decisively establishes is that **every fixed uniformly
full-rank product seed fails the remaining equation at order zero**.

## 4. A small explicit harmonic-source correction on the actual metrics

A global Hodge estimate on a collapsing family would not justify the
claim that the harmonic source connection is close to the canonical
one. Instead the balanced interpolation permits an explicit primitive.

Use the actual slow-interpolation construction in
[round8_multitwist.md](round8_multitwist.md), choosing each fixed twist
profile with `zeta'(u)` even on its symmetric geodesic collar. This
choice is permitted in that construction, preserves the prescribed
single Dehn twist and the fixed smooth bundle, and is imposed here as
an explicit additional profile condition. The conclusion below is not
claimed for every unbalanced profile.

In an active collar use the oriented orthonormal coframe

\[
 e^0=dt,\quad e^1=b(t)d\theta,\quad e^2=du,\quad
 e^3=a(u)(ds+z(t)\zeta'(u)du),
 \quad k=b'/b,\quad j=a'/a,\quad v=a\zeta'z'.          \tag{11}
\]

Here `a=a_0 cosh u`, `b=ell cosh t`, and
`z(t)=eta(t/L)` is constant near the ends. Thus

\[
 de^1=ke^0\wedge e^1,\qquad
 de^3=je^2\wedge e^3+ve^0\wedge e^2.
\]

Let `J E_0=E_1`, `J E_2=E_3`. Its fundamental form
`omega_L=e^0 wedge e^1+e^2 wedge e^3` is the globally defined closed
sum of the two area forms. It is self-dual, hence exactly harmonic.

The determinant connection `B_L` of the Hermitian connection
`nabla^J=nabla-(1/2)J(nabla J)` on `T^{1,0}X` has local one-form

\[
                   B_L=i(ke^1+je^3-\tfrac12ve^0).      \tag{12}
\]

Indeed Koszul's formula gives
`<nabla E_0,E_1>+<nabla E_2,E_3>=k e^1+j e^3-v e^0/2`;
Hermitian projection preserves this complex trace. Differentiating (12),
using `k_t+k²=j_u+j²=1`, gives the exact formula

\[
 F_{B_L}=i\omega_L
       +i(jv+\tfrac12v_u)e^0\wedge e^2
 =i\omega_L+i z'(t) C(u)\,dt\wedge du,
 \quad C(u)={3a'\zeta'+a\zeta''\over2}.                 \tag{13}
\]

The function `C` is odd and supported away from the fibre-collar ends.
Thus its integral across the collar is zero. There is a compactly
supported primitive `P'=C`. Set

\[
                    \beta_L=-i z'(t)P(u)\,dt.          \tag{14}
\]

It extends by zero outside the active region and satisfies

\[
 F_{B_L}-i\omega_L=d\beta_L,\qquad
 \|\nabla^r\beta_L\|_\infty=O(L^{-1})
 \quad\hbox{for each fixed }r.                         \tag{15}
\]

All coefficients are independent of the collapsing angular variable;
the orthonormal connection coefficients remain bounded. The estimate
therefore contains no inverse injectivity radius. Distinct active base
collars are disjoint, so the same argument works for the noncommuting
twists in `E_full`.

Consequently

\[
                 C_L:=B_L-\beta_L,\qquad F_{C_L}=i\omega_L\tag{16}
\]

is a globally defined unitary connection on the same determinant line
with exactly harmonic curvature. This is an allowed fixed **source**
connection. It is explicitly `O(L^{-1})` from the target determinant
connection `B_L`; no inverse Hodge-Laplacian estimate has been used.

## 5. Quantifying the round-9 seeds and ruling out small closure

Let `A_{0,L}=d plus B_L` on the canonical splitting
`W=C plus K_{J_L}^{-1}`. The source spin connection induced by the
Levi--Civita connection and `C_L` differs from `A_{0,L}` by
`O(L^{-1})` with all fixed-order derivatives. To see this, first lift
the Hermitian connection `nabla^J` to the canonical spin-c bundle.
It fixes its unit canonical spinor and is exactly `d plus B_L` on
positive spinors. Its difference from the Levi--Civita spin-c connection
with determinant `B_L` is linear in `nabla J=O(L^{-1})`.
Replacing `B_L` by `C_L` adds only the scalar term `-beta_L/2`.

Let `T_L` be the trace isomorphism used in round 9,
`tr tau(phi)=T_L((phi*phi)_0)`, and fix a constant `t>q_0` from (9).
Set

\[
 H_L=\left(tI+\mathcal T_L^{-1}(F_{B_L}^+)\right)^{1/2}.\tag{17}
\]

For large `L`, both eigenvalues stay uniformly positive and distinct.
Their squares tend uniformly to `t+q_0,t-q_0`. The tensor `T_L` is
parallel for the source spin connection. From (13)--(16) and
`nabla omega_L=O(L^{-1})`, it follows that

\[
 \|D_{A_{0,L}}H_L\|_{C^1}=O(L^{-1}).                   \tag{18}
\]

Here and below `C1` means uniform intrinsic zeroth and first covariant
derivative bounds; it does not refer to coordinates with a collapsing
angular scale.

For the traceless connection map
`L_H(b)=sum b_j H c_j`, round 9 computed a nonzero minor
`-(x-y)^4(x+y)^4`. On the present compact range of positive distinct
eigenvalues, its smooth right inverse and its first derivatives are
uniformly bounded. Therefore the exact correction

\[
 b_L=-\mathcal L_{H_L}^*
       (\mathcal L_{H_L}\mathcal L_{H_L}^*)^{-1}
          D_{A_{0,L}}H_L,\qquad A_L=A_{0,L}+b_L         \tag{19}
\]

satisfies

\[
 D_{A_L}H_L=0,\quad\det A_L=B_L,\quad
 \operatorname{tr}(F_{A_L}^+-\tau(H_L))=0,\qquad
 \|b_L\|_{C^1}=O(L^{-1}),\quad
 \|(F_{A_L}^-)_0\|_\infty=O(L^{-1}).                   \tag{20}
\]

The last estimate follows from `F_{A_{0,L}}=diag(0,F_{B_L})`, (13),
and `F_{A_L}-F_{A_{0,L}}=d_{A_{0,L}}b_L+b_L wedge b_L`.

Use normalized norms `||u||_{p,av}=(Vol^{-1} integral |u|^p)^{1/p}`.
The actual metric volume is fixed. Since the spinor bundles are
canonical, `c_2(E)=0`. Furthermore

\[
 \fint\det(H_L^2)\longrightarrow t^2-q_0^2>0,\qquad
 \|\tau(H_L)\|_{2,av}^2\longrightarrow6\kappa^2t^2-1.   \tag{21}
\]

Apply (6) and (20). For `R_L=F_{A_L}^+-tau(H_L)`, this gives

\[
 \boxed{\quad
 \liminf_{L\to\infty}\|R_L\|_{2,av}
 \ge\sqrt{12\kappa^2t^2-4}-\sqrt{6\kappa^2t^2-1}>0.
 \quad}                                                    \tag{22}
\]

Thus the final equation in round 9 is not a small residual on these
uniformly full-rank seeds. Equation (10) independently displays its
nonzero product-limit origin without using the Chern--Weil identity.

**Theorem 3 (no small critical-curvature closure).** There are no
connections `A'_L=A_L+u_L` and spinors `phi'_L` satisfying

\[
 \|d_{A_L}u_L\|_{2,av}+\|u_L\|_{4,av}^2\to0,
 \qquad\|\phi'_L-H_L\|_{4,av}\to0,                     \tag{23}
\]

for which `||F_{A'_L}^+-tau(phi'_L)||_{2,av}->0`.
In particular they cannot be exact coupled solutions, regardless of
whether their Dirac equation is imposed.

**Proof.** Curvature expansion and (23) imply
`||(F_{A'_L}^-)_0||_{2,av}->0`. Polynomial continuity in `L4` gives
bounded `||tau(phi'_L)||_{2,av}` and
`fint det(phi'_L*phi'_L)->t²-q_0²>0`. These facts contradict (6).
The statement is unchanged by simultaneous unitary gauge transformations
of the seed and perturbed pair. QED.

## 6. Rank-one partial seeds do not require a singular right inverse

The rank-loss alternative in (7) is not an obstruction to solving the
two partial equations. In fact the same balanced metrics admit exact
Dirac-and-trace seeds of rank one with a uniformly small connection
correction.

Put

\[
 Q_L=\mathcal T_L^{-1}(F_{B_L}^+),\qquad
 q_L=|Q_L|_{\mathrm{op}},\qquad
 P_L={1\over2}(I+Q_L/q_L),\qquad
 H_L^{(1)}=\sqrt{2q_L}\,P_L.                         \tag{24}
\]

Here `q_L->q_0>0` uniformly, `Q_L` is traceless Hermitian, and `P_L`
is its positive-eigenvalue spectral projector. Thus (24) is globally
smooth, has rank one everywhere, and
`(H_L^{(1)})²=q_L I+Q_L`. It solves the target trace equation exactly.
The formula in terms of `P_L`, rather than differentiating the square
root on all semidefinite matrices, proves the uniform derivative
estimates needed here: the nonzero spectral gap stays bounded away
from zero, and `nabla Q_L=O(L^{-1})` with the requisite further
derivatives. Consequently
`||D_{A_{0,L}}H_L^{(1)}||_{C1}=O(L^{-1})`.

For `H=diag(x,0)`, `x>0`, the eight-column real minor of the traceless
connection map from Section 5 is

\[
             -(x-y)^4(x+y)^4\big|_{y=0}=-x^8\ne0.     \tag{25}
\]

The analogous conclusion holds after interchanging the two eigenspaces.
Hence the intrinsic pseudoinverse in (19) stays smooth and uniformly
bounded on this compact rank-one spectral range. Applying it gives a
connection `A_L^{(1)}=A_{0,L}+b_L^{(1)}` such that

\[
 \begin{gathered}
 D_{A_L^{(1)}}H_L^{(1)}=0,\qquad \det A_L^{(1)}=B_L,\\
 \operatorname{tr}\big(F_{A_L^{(1)}}^+-\tau(H_L^{(1)})\big)=0,\qquad
 \|b_L^{(1)}\|_{C^1}=O(L^{-1}),\qquad
 \|(F_{A_L^{(1)}}^-)_0\|_\infty=O(L^{-1}).            \tag{26}
 \end{gathered}
\]

These are genuine rank-one **partial** seeds for the actual trace map;
the construction makes no favorable choice of its relative sign. At the
exact product the two convention-labeled computations in (10) give
residual squared `4` and `0` at `m=1`. Assigning either value to the
published system requires the additional source-dual and curvature-sign
identification withheld in Section 3. The checker verifies both values,
not the choice between them. The determinant term in (5) is identically
zero for (24), so the present energy obstruction by itself supplies no
positive lower bound at this endpoint. Rank loss therefore remains an
actual available partial-seed direction, not a blow-up of the Dirac
right inverse and not a proved solution of the last equation.

## 7. Scope

The obstruction treats small repairs of a concrete full-rank bridge on
the actual smooth input bundles. It does not exclude a solution with
substantial anti-self-dual connection curvature, an `L4`-distant spinor,
or determinant mass tending to zero. In particular it does not extend
the parallel-field discussion in round 9 to all coupled solutions.

The scalar offset `t` was fixed strictly above the rank-loss threshold.
Letting it approach `q_0` is a materially different limiting problem:
the determinant term in (5) then degenerates. Section 6 shows that
exact Dirac-and-trace seeds persist at rank one, but does not settle
their last equation or the published rank-one convention bridge.
The sign-independent energy obstruction and the explicit harmonic-source
construction already suffice for (22)--(23).

The balanced-profile condition in Section 4 is essential to the uniform
source-connection argument supplied here. The round-9 existence of
partial seeds did not require that condition, but gave no such smallness
estimate. This note does not silently promote a collapsing Hodge estimate
for unbalanced profiles.

[round10_nonabelian_check.py](round10_nonabelian_check.py) checks the
quadratic norm identity, the exact product residual in both sign
labelings, the canonical determinant connection and its primitive,
the residual lower-bound algebra, and the nonsingular fixed-determinant
Dirac correction at rank one. It does not solve the remaining PDE or
verify the external uniformization theorem.
