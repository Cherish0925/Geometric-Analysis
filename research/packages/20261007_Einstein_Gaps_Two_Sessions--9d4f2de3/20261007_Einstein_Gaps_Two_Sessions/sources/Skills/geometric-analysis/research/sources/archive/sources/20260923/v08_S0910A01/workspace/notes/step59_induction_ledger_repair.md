# Step 59: Current-pair induction ledger repair and background triangular conversion

Session: S0910A01. Agent1 / Orchestrator. Phase: Explore.

## 0. Mathematical purpose

This note refines the Step 58 all-order continuation component rather than
using its module count as a route decision.  The important point is not whether
one can name many established pieces, but whether the differentiated tensor
hierarchy actually closes with every current-order term extracted and treated.
The Strategist note identified two exact places where the previous wording was
still too compressed:

1. In Step 58 §4.5, the alleged strict lower family still included expressions
   of the form `B_{m+2}*U_0` and `B_2*U_m`.  These are not harmless lower
   products.  `B_{m+2}*U_0` contains the top cutoff term
   `chi*C_{m+2}*U_0`; `B_2*U_m` contains the signed-Hessian term
   `chi*C_2*U_m`.  Both may be controllable, but only after being separated
   and estimated by their own mechanisms.
2. In Step 58 §7.2 the fixed-background conversion introduced a current
   `A_m` coefficient.  With the ordered identity
   `partial_t A = g^{-1}*U_1`, the top fixed-background derivative is
   `g^{-1}*U_{m+1}` and the remaining products involve background derivatives
   of `A` only through order `m-1`.  The conversion is strictly triangular.

The result below keeps the useful Step 58 mechanisms but replaces the loose
classification by an explicit source-by-source ledger.  It also preserves the
correct source order for the base layer:

\[
\bigl(U_0\in L^\infty,\ T_0\in L^q\text{ for all finite }q\bigr)
\quad\longrightarrow\quad (U_1,C_2)
\quad\longrightarrow\quad T_1
\quad\longrightarrow\quad T_0\in L^\infty,
\tag{0.1}
\]

so the `W^{1,p}\to L^\infty` step is an output of the base derivative estimates,
not a proof of those estimates.  The first occurrence of `T_0` in this order is
finite-exponent unweighted curvature, whereas pointwise `T_0` enters only after
`T_1` has been obtained.

## 1. Notation and exact structural inputs

Work at a fixed positive time slab `[tau,T*)` of a smooth solution of

\[
\partial_t g=-2aE,\qquad E=\operatorname{Ric}_g+g,
\qquad a=\chi^2.
\tag{1.1}
\]

Let

\[
T=\operatorname{Rm}+G,
\qquad G={g\owedge g\over 2(n-1)},
\qquad U=aT,
\tag{1.2}
\]

so `Ric(T)=E` and `Ric(U)=aE`.  Write

\[
U_j=\nabla^jU,
\quad T_j=\nabla^jT,
\quad C_j=\nabla^j\chi,
\quad B_j=\nabla^ja.
\tag{1.3}
\]

The algebraic cutoff identities are

\[
B_k=\nabla^k(\chi^2)
=2\chi C_k+
\sum_{i=1}^{k-1} c_{i,k}\, C_i*C_{k-i},
\qquad k\ge2,
\tag{1.4}
\]

and

\[
B_1=2\chi C_1,
\qquad { |B_1|^2\over a}=4|C_1|^2
\quad\text{on }\{a>0\},
\tag{1.5}
\]

with the last identity used only in no-division Young estimates.

The corrected zero-order equations from Step 58 are retained only in the
following normal form: the level-`m` principal second-order piece is
`div(a nabla U_m)` or `a Delta T_m+B_1*nabla T_m`, and every other term is a
Leibniz product coming from derivatives of `a`, curvature commutators, time
commutators, or algebraic reactions.  This avoids double-counting the displayed
`B_1*nabla U` drift.

The key ordered connection-velocity identity is exact:

\[
\partial_t\Gamma = g^{-1}*\nabla(aE)=g^{-1}*U_1.
\tag{1.6}
\]

The equality uses `Ric(U)=aE`, so the derivative lands on the tensor `U`; no
separate derivative of `a` is created in (1.6).

## 2. Source-by-source classification for the `U_m` equation, `m>=2`

After applying `nabla^m` to the `U` equation and commuting derivatives to put
the second-order term into divergence form, the equation has the form

\[
\partial_t U_m=\operatorname{div}(a\nabla U_m)+\mathcal C_m^U+
\mathcal L_m^U+
\mathcal N_m^U+\mathcal Q_m^U,
\tag{2.1}
\]

where the four groups below are separated by principal source.  Some displayed
current structures are contributed by more than one source—for instance,
`nabla^m((C_1*C_1)*U)` also produces `C_1*C_{m+1}*U_0` and
`C_1*C_1*U_m`.  The point of the ledger is structural exhaustion of all
current-order terms, not a one-to-one source label.

### 2.1 Coefficient derivatives of the second-order and drift part

All terms created by differentiating the cutoff coefficients have schematic
form

\[
\sum_{k=2}^{m+2} B_k*U_{m+2-k}.
\tag{2.2}
\]

The cases `k=m+2`, `k=m+1`, and `k=2` must be extracted before any remainder is
called previous-level:

\[
\boxed{
\begin{aligned}
B_{m+2}*U_0
&=2\chi C_{m+2}*U_0
 +\sum_{i=1}^{m+1}C_i*C_{m+2-i}*U_0,\tag{2.3a}\\
B_{m+1}*U_1
&=2\chi C_{m+1}*U_1
 +\sum_{i=1}^{m}C_i*C_{m+1-i}*U_1,\tag{2.3b}\\
B_2*U_m
&=2\chi C_2*U_m+2C_1*C_1*U_m.\tag{2.3c}
\end{aligned}}
\]

The extracted current-order structures are therefore

\[
\boxed{
\chi C_{m+2}*U_0,
\qquad
\chi C_{m+1}*U_1,
\qquad
C_1*C_{m+1}*U_0,
\qquad
\chi C_2*U_m,
\qquad
C_1*C_1*U_m.}
\tag{2.4}
\]

Here `C_1*C_{m+1}*U_0` is not difficult, but it is still a current-pair term
because `C_{m+1}` is part of the level-`m` unknown.  It is controlled by Young,
not by induction.  The term `chi*C_2*U_m` is the signed-Hessian term; it is not
an `L^\infty` coefficient.  The term `C_1*C_1*U_m` is a bounded-coefficient
current term.

Every remaining case in (2.2) is previous-level in the actual sense:

\[
3\le k\le m,
\qquad U_{m+2-k}\le U_{m-1},
\qquad B_k\text{ contains only }C_j\text{ with }j\le m.
\tag{2.5}
\]

For `m=2` this interval is empty, which is exactly why the extracted
`B_2*U_2`, `B_3*U_1`, and `B_4*U_0` terms are the whole difficulty at the first
general level.

### 2.2 Algebraic reactions

The nonlinear term `U*U` gives

\[
\nabla^m(U*U)=U_m*U_0+U_0*U_m+
\sum_{1\le i\le m-1} U_i*U_{m-i}.
\tag{2.6}
\]

The two endpoint terms are current but have bounded zero-order coefficient
`U_0`, already controlled by the weighted curvature endpoint.  The middle terms
are previous-level products for `m>=2`.

The linear normalization term `aU` gives

\[
\nabla^m(aU)=aU_m+B_1*U_{m-1}+
\sum_{k=2}^{m}B_k*U_{m-k}.
\tag{2.7}
\]

Only `aU_m` is current, and it has bounded coefficient.  No `C_{m+1}` or
`C_{m+2}` occurs here.

### 2.3 Spatial curvature commutators

Commuting `nabla^m` with the rough Laplacian produces

\[
a\sum_{r+s=m}T_r*U_s
\quad\text{plus terms already included in (2.2) when derivatives hit }a.
\tag{2.8}
\]

The current endpoints are

\[
aT_m*U_0,
\qquad aT_0*U_m.
\tag{2.9}
\]

The second is a bounded-coefficient current term after the base pointwise
curvature step `T_0 in L^infty`.  The first is converted without division by
`a`:

\[
aT_m=U_m-
\sum_{q=1}^{m}\binom mq B_q*T_{m-q}.
\tag{2.10}
\]

The right side is `U_m` plus previous unweighted curvature levels.  Thus no
bare `T_m` remains.  Interior commutator products involve only `T_i,U_j` with
indices `<m` after (2.10) and the base pointwise `T_0` bound are used.

### 2.4 Time commutators

Using (1.6),

\[
[\partial_t,\nabla^m]U
=\sum_{r+s=m-1}\nabla^r(g^{-1}*U_1)*U_s.
\tag{2.11}
\]

The endpoint `r=m-1,s=0` gives

\[
U_m*U_0
\tag{2.12}
\]

up to bounded metric factors and lower connection reorderings.  This is a
bounded-coefficient current term.  All other terms have `U_{r+1}` with
`r+1<=m-1` and are previous-level.  Most importantly, no `U_{m+1}` occurs in
the time commutator.

### 2.5 Corrected `U_m` equation

Combining the four sources, the level equation can be written as

\[
\boxed{
\begin{aligned}
\partial_tU_m
=&\operatorname{div}(a\nabla U_m)
 +\chi C_{m+2}*U_0
 +\chi C_{m+1}*U_1
 +C_1*C_{m+1}*U_0 \\
&+\chi C_2*U_m
 +C_1*C_1*U_m
 +\mathcal B_m^U*U_m
 +\mathcal P_m^U.
\end{aligned}}
\tag{2.13}
\]

Here `mathcal B_m^U` is a bounded zero-order coefficient depending on
`g^{-1},U_0,T_0,a,C_1`, and `mathcal P_m^U` is genuinely previous-level: every
factor belongs to the already constructed list

\[
\{U_j:j<m\}\cup\{T_j:j<m\}\cup\{C_j:j\le m\}\cup\{T_0,U_0,g^{-1}\}.
\tag{2.14}
\]

The terms `B_{m+2}*U_0`, `B_{m+1}*U_1`, and `B_2*U_m` are not allowed to remain
inside `mathcal P_m^U`; their current pieces are exactly the five displayed
terms in (2.13).  One also needs the derivative-reordering lemma: when
`nabla^m nabla^2 a` is rewritten as `nabla C_{m+1}` for the integration by
parts, every curvature commutator produced by changing derivative order has the
form `T_i*C_j*U_0` with `i<=m-1` and `j<=m`, hence belongs to previous levels.
Equivalently, the highest cutoff jet `C_{m+2}` occurs only paired with the
zero-order curvature variable (`U_0` here, `T_0` in the unweighted equation),
never with `U_j` for `j>=1`.  This is a genuine tensor lemma still to be written
with indices.

## 3. Pair energy inequality from (2.13)

Let

\[
V=U_m,
\qquad Z=C_{m+1},
\qquad D_{m,p}^U=\int a|\nabla V|^2|V|^{p-2}.
\tag{3.1}
\]

Testing (2.13) against `|V|^{p-2}V` gives the following estimates.

### 3.1 Principal operator and first-order drift

The divergence term gives

\[
\int |V|^{p-2}V*\operatorname{div}(a\nabla V)
=-c_pD_{m,p}^U.
\tag{3.2}
\]

If one keeps a separate `B_1*nabla V` drift from a chosen normal form, it is
estimated by

\[
\int |B_1|\,|\nabla V|\,|V|^{p-1}
\le \varepsilon D_{m,p}^U
 +C_{\varepsilon,p}\|C_1\|_\infty^2\|V\|_p^p,
\tag{3.3}
\]

using `|B_1|^2/a=4|C_1|^2` as a no-division identity under Young.

### 3.2 Top cutoff term `chi*C_{m+2}*U_0`

Since `C_{m+2}=nabla C_{m+1}`, integrate once by parts:

\[
\begin{aligned}
&\int |V|^{p-2}V*\chi C_{m+2}*U_0 \\
=&-\int \nabla(|V|^{p-2}V)*\chi Z*U_0
  -\int |V|^{p-2}V*C_1*Z*U_0 \\
&-\int |V|^{p-2}V*\chi Z*U_1.
\end{aligned}
\tag{3.4}
\]

The first term is absorbed into `D_{m,p}^U` because `U_0` is bounded:

\[
\le \varepsilon D_{m,p}^U+C\bigl(\|Z\|_p^p+\|V\|_p^p\bigr).
\tag{3.5}
\]

The second term is bounded by Young with bounded `C_1,U_0`.  The third term is
the critical residual

\[
I_m=\int \chi |Z|\,|U_1|\,|V|^{p-1}.
\tag{3.6}
\]

The directly occurring next-cutoff term `chi*C_{m+1}*U_1` contributes the same
residual.  Thus both top and next cutoff terms are covered by one estimate.

### 3.3 Critical residual for `m>=2`

Set `f=chi |V|^{p/2}`.  In dimension four,

\[
\|f\|_4^2\le C_S\bigl(p^2D_{m,p}^U+C_{p,r}\|V\|_p^p\bigr).
\tag{3.7}
\]

For `p>2`, Hölder with exponents `(4,p,4,2p/(p-2))` gives

\[
I_m\le \|f\|_4\,\|Z\|_p\,\|U_1\|_4\,\|V\|_p^{p/2-1}.
\tag{3.8}
\]

For `m>=2`, `U_1` is base data.  Young therefore yields

\[
I_m\le \varepsilon D_{m,p}^U
 +C_{m,p,\tau}\bigl(1+\|Z\|_p^p+\|V\|_p^p\bigr).
\tag{3.9}
\]

For `m=1`, the same line would read
`int chi |C_2| |U_1|^p`; the factor `U_1` is then current, not base.  This is
why the general induction begins only at `m=2`.

### 3.4 Signed-Hessian current term

The term `chi*C_2*V` has the tensor form

\[
J_m=\int \chi (\nabla_i\nabla_j\chi)\,\mathcal B^{ij}(V),
\qquad |\mathcal B|\le C|V|^p,
\quad |\nabla\mathcal B|\le Cp|V|^{p-1}|\nabla V|.
\tag{3.10}
\]

Integrating off one derivative of `C_2` gives

\[
|J_m|\le C\int |C_1|^2|V|^p
 +Cp\int \chi |C_1| |V|^{p-1}|\nabla V|.
\tag{3.11}
\]

Weighted Young gives

\[
|J_m|\le \varepsilon D_{m,p}^U
 +C_{p,\varepsilon}\|C_1\|_\infty^2\|V\|_p^p.
\tag{3.12}
\]

Thus this current term uses only the first cutoff derivative in `L^\infty`, not
an evolving `L^\infty` norm of `C_2`.

### 3.5 Cutoff-jet equation and coupled inequality

Since `C_{m+1}=\nabla^mC_1` and `C_1=d\chi` is connection-independent at order
zero,

\[
\partial_t C_{m+1}
=C_1*U_m+
\sum_{1\le j<m}C_{m+1-j}*U_j+
\mathcal R_m,
\tag{3.13}
\]

where `mathcal R_m` contains only previous curvature/cutoff levels after the
same connection reorderings.  There is no `U_{m+1}` and no `C_{m+2}`.
Testing (3.13) against `|Z|^{p-2}Z` gives

\[
{d\over dt}\|Z\|_p^p
\le C_{m,p,\tau}\bigl(1+\|Z\|_p^p+\|V\|_p^p\bigr).
\tag{3.14}
\]

Combining (3.2)--(3.14), with all previous-level products absorbed by
Hölder/Young using finite exponents, gives

\[
\boxed{
{d\over dt}\bigl(\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr)
+cD_{m,p}^U
\le C_{m,p,\tau}\bigl(1+\|U_m\|_p^p+\|C_{m+1}\|_p^p\bigr).}
\tag{3.15}
\]

This is the usable current-pair estimate for `m>=2`.

## 4. Unweighted `T_m` equation and energy inequality

The unweighted curvature equation has the same coefficient-derivative sources,
with `T` in place of `U`:

\[
\partial_tT_m
=a\Delta T_m+B_1*\nabla T_m
+\chi C_{m+2}*T_0
+\chi C_{m+1}*T_1
+C_1*C_{m+1}*T_0
+\chi C_2*T_m
+C_1*C_1*T_m
+\mathcal B_m^T*T_m+
\mathcal P_m^T.
\tag{4.1}
\]

Again `mathcal P_m^T` is allowed to contain only genuinely previous levels.
The current terms in (4.1) are treated as follows.

1. The principal `a Delta T_m+B_1*nabla T_m` gives the dissipation

   \[
   D_{m,p}^T=\int a|\nabla T_m|^2|T_m|^{p-2}.
   \tag{4.2}
   \]

2. The top cutoff term is integrated by parts:

   \[
   \int |T_m|^{p-2}T_m*\chi C_{m+2}*T_0
   \tag{4.3}
   \]

   produces a diffusion-absorbed term with coefficient `T_0 in L^infty`, a
   bounded `C_1*C_{m+1}*T_0` term, and the residual

   \[
   \widetilde I_m=\int \chi |C_{m+1}|\,|T_1|\,|T_m|^{p-1}.
   \tag{4.4}
   \]

   Since `T_1 in L^4` is part of the base derivative package, the same
   `(4,p,4,2p/(p-2))` argument gives

   \[
   \widetilde I_m\le \varepsilon D_{m,p}^T
    +C_{m,p,\tau}(1+\|C_{m+1}\|_p^p+\|T_m\|_p^p).
   \tag{4.5}
   \]

3. The signed-Hessian term `chi*C_2*T_m` is estimated by the same integration
   by parts as (3.10)--(3.12), with `T_m` replacing `U_m`.

4. Whenever any source presents a current weighted unweighted-curvature factor
   `aT_m`—spatial commutator, reaction, or reordered coefficient term—it is
   reduced using

   \[
   aT_m=U_m-
   \sum_{q=1}^{m}\binom mq B_q*T_{m-q},
   \tag{4.6}
   \]

   after the current-pair estimate (3.15) has supplied `U_m`.  All remaining
   unweighted curvature factors have lower index.

Therefore, after the pair `(U_m,C_{m+1})` has been controlled,

\[
\boxed{
{d\over dt}\|T_m\|_p^p+cD_{m,p}^T
\le C_{m,p,\tau}\bigl(1+\|T_m\|_p^p\bigr).}
\tag{4.7}
\]

The level order is consequently

\[
(U_0\in L^\infty,\ T_0\in L^q_{\rm fin})
\to (U_1,C_2)\to T_1\to T_0\in L^\infty
\to (U_2,C_3)\to T_2\to (U_3,C_4)\to T_3\to\cdots.
\tag{4.8}
\]

The pointwise curvature bound `T_0 in L^infty` enters before the general
`m>=2` unweighted estimates; it does not replace the base-pair or `T_1`
derivation.

## 5. Strict triangular fixed-background conversion

Fix `bar g=g(tau)` and `bar nabla=nabla^{bar g}`.  Let

\[
A=\nabla^{g(t)}-\bar\nabla.
\tag{5.1}
\]

The exact ordered identity is

\[
\partial_tA=\partial_t\Gamma(g)=g^{-1}*U_1.
\tag{5.2}
\]

For `m>=0`, apply `bar nabla^m` to (5.2).  Two conversion facts are used.
First,

\[
\bar\nabla^k g^{-1}=P_k(g^{-1},A_{\le k-1}),
\qquad k\ge1,
\tag{5.3}
\]

because `bar nabla g=A*g`.  Second,

\[
\bar\nabla^mU_1
=U_{m+1}+P_m(A_{\le m-1},U_{\le m}),
\tag{5.4}
\]

which follows by repeatedly replacing one `bar nabla` with `nabla-A`.  The
highest background derivative of `A` that appears in this conversion is
`A_{m-1}`, never `A_m`.

Thus

\[
\boxed{
\partial_t A_m
=g^{-1}*U_{m+1}+P_m(A_{\le m-1},U_{\le m},g^{-1}),
\qquad A_m=\bar\nabla^mA.}
\tag{5.5}
\]

This is stronger than the Step 58 §7.2 wording with a current `B_0^A*A_m`
coefficient.  No such current `A_m` term is needed.  On a positive slab, the
already obtained evolving tower gives finite `L^p` bounds for `U_{m+1}`; by
induction on `m`, (5.5) gives

\[
\sup_{t\in[\tau,T_*)}\|A_m(t)\|_{L^p(\bar g)}<\infty
\quad\text{for every finite }m,p.
\tag{5.6}
\]

The metric derivatives follow from

\[
\bar\nabla^{m+1}g=A_m*g+P_m(A_{<m},g),
\tag{5.7}
\]

so `g(t)` has fixed-background `H^s` bounds of all finite orders.  Moreover

\[
\partial_tg=-2aE=-2\operatorname{Ric}(U),
\tag{5.8}
\]

so `partial_t g` in fixed-background `H^s` is controlled by the same `U` and
`A` towers.  Uniform bounds on a finite interval imply Cauchy convergence in
each `H^s` as `t` approaches a finite terminal time.  Sobolev embedding then
gives a smooth terminal metric, and the autonomous time-jet splice from Step 58
can be used without any overlap uniqueness argument.

## 6. What this repairs and what remains outside the induction ledger

The repaired current-pair hierarchy is now sharper in three ways.

- `B_{m+2}*U_0`, `B_{m+1}*U_1`, and `B_2*U_m` are not placed in a generic lower
  family.  Their current components are extracted as the top-cutoff,
  next-cutoff, bounded-current, and signed-Hessian terms.
- The unweighted equation uses the same extraction before invoking
  weighted-to-unweighted conversion for `aT_m`.
- The background conversion is strictly triangular in `A`: `partial_t A_m`
  is forced by `U_{m+1}` plus `A_{<m}` products, not by a current `A_m`
  coefficient.

This does not by itself supply new geometric input for the full Yau 26 problem.
Outside the IL negative branch, one still needs both (i) a topology/geometry
mechanism producing a curvature budget analogous to the Seiberg--Witten/Chern--Weil
calibration and (ii) a terminal density whose zero set is locally impossible for
Einstein metrics.  The analytic continuation machinery is reusable only after
those ingredients are independently supplied.
