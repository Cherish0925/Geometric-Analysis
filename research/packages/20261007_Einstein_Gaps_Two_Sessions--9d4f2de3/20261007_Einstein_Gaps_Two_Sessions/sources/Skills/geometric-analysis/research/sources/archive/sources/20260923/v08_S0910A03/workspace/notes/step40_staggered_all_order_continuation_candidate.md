# Step 40: staggered all-order continuation after the m=2 repair

Session: S0910A03. Agent3 / Actuator. Phase: Execute.

## 0. Purpose and status

The companion note `step40_m2_coupled_continuation_mechanism.md` proves two
low-order facts for the shifted normalized cutoff flow:

1. the independent whole-manifold estimate for \(\nabla T\), where
   \(T=\operatorname{Rm}+G\);
2. the coupled estimate for \((\nabla^2U,\nabla^3\chi)\), where \(U=aT\) and
   \(a=\chi^2\).

The essential repair is to integrate the current-cutoff-jet product
\(\chi\nabla^{m+1}\chi*\nabla U*P(\nabla^mU)\) once more, instead of asking for
the current cutoff jet at exponent \(2p\).  This note formulates the resulting
staggered induction at arbitrary order and displays why every use of a larger
finite exponent falls on a previously established spatial level.

The derivative-energy argument applies to a smooth solution on a positive-time
slab under \(\sup|U|<\infty\). It is per datum. A full continuation theorem
still needs the transported-coefficient short-time restart. The note does not
establish that restart, the sequence-uniform smoothing estimates, terminal
calibration, or Yau Problem 26.

## 1. Equations and induction families

On a closed manifold consider

\[
 \partial_tg=-2aE,
 \qquad a=\chi^2,
 \qquad E=\operatorname{Ric}+g,
 \qquad T=\operatorname{Rm}+G,
 \qquad U=aT,
\]

where \(G=(g\owedge g)/(2(n-1))\).  Then

\[
 \operatorname{Ric}(T)=E,
 \qquad \operatorname{Ric}(U)=aE,
 \qquad \partial_tg=-2\operatorname{Ric}(U).                       \tag{1.1}
\]

Work on \([\tau,T_*)\), \(\tau>0\), and assume

\[
 \sup_{M\times[\tau,T_*)}|U|\le K.                                \tag{1.2}
\]

Metric bilipschitz equivalence, volume equivalence, scalar Sobolev inequalities,
and \(|d\chi|\) then have finite per-datum constants on this slab.

Write

\[
 U_m=\nabla^mU,
 \qquad C_j=\nabla^j\chi,
 \qquad T_m=\nabla^mT.                                             \tag{1.3}
\]

The two structural evolution families are

\[
\begin{split}
 \partial_tU_m={}&a\Delta U_m
 +\sum_{\alpha+\beta+\gamma=m+2,\ \gamma\le m+1}
       C_\alpha*C_\beta*U_\gamma\\
 &+\sum_{i+j+k=m,\ k\le m-1}\nabla^ia*U_j*T_k
 +U*U_m+\mathcal G_m,                                             \tag{1.4}
\end{split}
\]

and

\[
\begin{split}
 \partial_tT_m={}&a\Delta T_m
 +\sum_{r+k=m+2,\ 1\le r\le m+2,\ k\le m+1}
       \nabla^ra*T_k\\
 &+\sum_{i+j+k=m}\nabla^ia*T_j*T_k
 +\mathcal N_m .                                                   \tag{1.5}
\end{split}
\]

Here \(C_0=\chi\).  The terms \(\mathcal G_m,\mathcal N_m\) contain the
normalization, the parallel tensor \(G\), Laplacian commutators, and connection
variation.  Their highest derivatives have the same ordering as the displayed
terms: in particular, connection variation contributes products
\(U_j*T_k\) with no derivative of \(U\) above the current order.  Since
\(\nabla G=0\), no new derivative branch is introduced.

For each \(m\ge1\), the staggered stage is

\[
 (U_m,C_{m+1})\quad\hbox{first},
 \qquad T_m\quad\hbox{second}.                                    \tag{1.6}
\]

At the beginning of stage \(m\), assume for every finite exponent \(q\):

\[
 U_j,C_{j+1},T_j\in L^q\quad(0\le j<m),                            \tag{1.7}
\]

with \(U_0\in L^\infty\).  The zero-order unweighted curvature energy supplies
\(T_0\in L^q\) for all finite \(q\).  Stage \(m=1\) is the repaired base pair
followed by the order-one unweighted lemma in the companion note.

All derivatives of \(a\) are always expanded honestly:

\[
 \nabla^ra=\sum_{s=0}^r {r\choose s}C_s*C_{r-s}.                   \tag{1.8}
\]

Only the two summands \(\chi C_r\) carry a factor \(\chi\); the other products
do not and are never treated as if they did.

## 2. Weighted current pair

Fix \(p\ge2\), set

\[
 V=U_m,
 \qquad Z=C_{m+1},
 \qquad
 D^U_{m,p}=\int\chi^2|\nabla V|^2|V|^{p-2},
 \qquad P(V)=|V|^{p-2}V.                                          \tag{2.1}
\]

### 2.1 Terms containing a derivative of the current variable

The only first-sum allocation with \(U_{m+1}\) is

\[
 \chi d\chi*U_{m+1}.
\]
After testing, Young's inequality gives

\[
 \left|\int P(V)*\chi d\chi*\nabla V\right|
 \le\varepsilon D^U_{m,p}+C_{p,\varepsilon}\|d\chi\|_\infty^2
      \|V\|_p^p.                                                   \tag{2.2}
\]

The current \(U_m\) allocations have total cutoff order two:
\(\chi C_2*V\) and \(C_1*C_1*V\).  The first is kept as a signed Hessian
contraction and obeys

\[
 \left|\int\chi\nabla_i\nabla_j\chi\,B^{ij}(V)\right|
 \le\varepsilon D^U_{m,p}+C_{p,\varepsilon}\|d\chi\|_\infty^2
      \|V\|_p^p,                                                   \tag{2.3}
\]

while the second is zeroth order.

### 2.2 The only cutoff jet above the current pair

The sole \(C_{m+2}\) allocation is

\[
 \Gamma_1=\chi C_{m+2}*U.
\]
Integrating once gives

\[
\begin{split}
 \int P(V)*\Gamma_1={}&
 -\int\nabla P(V)*\chi Z*U
 -\int P(V)*d\chi*Z*U\\
 &-\int P(V)*\chi Z*U_1.                                          \tag{2.4}
\end{split}
\]

The first term is bounded by

\[
 \varepsilon D^U_{m,p}
 +C_{p,\varepsilon}K^2\int|Z|^2|V|^{p-2}
 \le\varepsilon D^U_{m,p}+C_{p,K}(\|Z\|_p^p+\|V\|_p^p),           \tag{2.5}
\]

and the second by the same-exponent product
\(C_{p,K}(\|Z\|_p^p+\|V\|_p^p)\).

The third term is the one that invalidated Step 39. It also occurs directly as
the original allocation \(\chi C_{m+1}*U_1\); every occurrence of this tensor
type is treated together. Do not estimate it with \(Z\in L^{2p}\). For
\(m\ge2\), write \(Z=\nabla C_m\) in the actual ordered
covariant derivative and integrate once more:

\[
\begin{split}
 \int\chi Z*U_1*P(V)={}&
 -\int d\chi*C_m*U_1*P(V)
 -\int\chi C_m*U_2*P(V)\\
 &-\int\chi C_m*U_1*\nabla P(V)+\mathcal R_{\rm com}.             \tag{2.6}
\end{split}
\]

Any reordering remainder \(\mathcal R_{\rm com}\) contains curvature times
lower cutoff and U derivatives and is covered by (1.7) together with the already
available \(T_j\), \(j<m\).

The first term in (2.6) uses \(C_m,U_1\in L^{2p}\).  For the second:

- if \(m=2\), \(C_m=C_2\) and \(U_2=V\), so it is the signed Hessian term
  (2.3);
- if \(m\ge3\), both \(C_m\) and \(U_2\) are previous-level quantities and
  Holder with exponents \((2p,2p,p/(p-1))\) closes it.

For the third term,

\[
\begin{split}
 \int\chi|C_m||U_1||V|^{p-2}|\nabla V|
 &\le\varepsilon D^U_{m,p}
 +C_{p,\varepsilon}\int|C_m|^2|U_1|^2|V|^{p-2}\\
 &\le\varepsilon D^U_{m,p}+C_{m,p}(1+\|V\|_p^p),                 \tag{2.7}
\end{split}
\]

using \(C_m,U_1\in L^{4p}\) and a finite-volume Holder factor.  Thus the
current jet \(Z\) occurs only at exponent \(p\), never at an enlarged exponent.

For \(m=1\), the corresponding \(\chi C_2*U_1\) term is directly of the signed
Hessian form (2.3), which is the base-pair mechanism.

### 2.3 All other weighted products

The remaining first-sum allocations have cutoff derivatives at most \(m\) and
U derivatives at most \(m-1\), except the already treated current Hessian and
diffusion terms.  They are products of finitely many previous-level factors
against \(|V|^{p-1}\).  A product of \(N\) such factors is bounded by assigning
each factor exponent \(Np\):

\[
 \int |A_1\cdots A_N|\,|V|^{p-1}
 \le\prod_{j=1}^N\|A_j\|_{Np}\,\|V\|_p^{p-1}.                    \tag{2.8}
\]

In the second sum of (1.4), if the current derivative \(U_m=V\) occurs then
\(i=k=0\), and its coefficient is \(aT=U\), which is bounded by K.  Otherwise
all \(U_j,T_k\) are previous levels.  Expansion (1.8) handles every cutoff
factor without inserting a false \(\chi\).

Consequently

\[
 {d\over dt}\|V\|_p^p+cD^U_{m,p}
 \le C_{m,p}\bigl(1+\|V\|_p^p+\|Z\|_p^p\bigr).                  \tag{2.9}
\]

### 2.4 Evolution of the current cutoff jet

Because \(\chi\) is fixed as a scalar and
\(\partial_t\Gamma=g^{-1}*\nabla\operatorname{Ric}(U)\), variation of
\(C_{m+1}\) has the structure

\[
 \partial_tC_{m+1}
 =U_m*C_1+U_0*C_{m+1}
  +\sum_{1\le j<m}U_j*C_{m+1-j}
  +\text{previous-level curvature commutators}.                   \tag{2.10}
\]

The first term is the current V times bounded \(d\chi\). The explicit
covariant-derivative evolution itself has only the sum with \(j\ge1\); the
schematic \(U_0*C_{m+1}\) term records inverse-metric, norm, and volume-form
variation in the \(L^p\) energy, not a leading term of the fixed scalar's raw
jet evolution. Every other product contains two previous-level factors. Testing
against \(|Z|^{p-2}Z\), using enlarged exponents only for those previous levels,
yields

\[
 {d\over dt}\|Z\|_p^p
 \le C_{m,p}(1+\|V\|_p^p+\|Z\|_p^p).                            \tag{2.11}
\]

Adding (2.9) and (2.11) closes \((U_m,C_{m+1})\) by Gronwall for every finite
p.

## 3. The subsequent unweighted T derivative

After the current pair is known in every finite exponent, set

\[
 X=T_m,
 \qquad D^T_{m,p}=\int\chi^2|\nabla X|^2|X|^{p-2}.                 \tag{3.1}
\]

In (1.5), the only cutoff derivative above the available \(C_{m+1}\) is the
term coming from

\[
 \nabla^{m+2}a*T=2\chi C_{m+2}*T
 +\sum_{s=1}^{m+1}C_s*C_{m+2-s}*T.                               \tag{3.2}
\]

All terms in the sum use cutoff jets of order at most \(m+1\), already known.
For the first term, integrate only the derivative in \(C_{m+2}=\nabla C_{m+1}\):

\[
\begin{split}
 \int\chi C_{m+2}*T*P(X)={}&
 -\int d\chi*C_{m+1}*T*P(X)\\
 &-\int\chi C_{m+1}*T_1*P(X)
 -\int\chi C_{m+1}*T*\nabla P(X).                                \tag{3.3}
\end{split}
\]

The last term is

\[
 \le\varepsilon D^T_{m,p}
 +C_{p,\varepsilon}\int|C_{m+1}|^2|T|^2|X|^{p-2}
 \le\varepsilon D^T_{m,p}+C_{m,p}(1+\|X\|_p^p).                  \tag{3.4}
\]

The first term is an ordinary finite-exponent product.  In the second term:

- for \(m=1\), \(T_1=X\) and \(C_{m+1}=C_2\), so it is another signed Hessian
  contraction;
- for \(m\ge2\), \(T_1\) is a previous level and direct Holder applies.

The allocation \(\nabla a*T_{m+1}\) is absorbed by \(D^T_{m,p}\), and
\(\nabla^2a*T_m\) is expanded as

\[
 (2\chi C_2+2C_1*C_1)*X,                                         \tag{3.5}
\]

with its first part treated by the signed Hessian lemma and its second part
zeroth order.  A quadratic term containing current \(T_m=X\) carries a factor
a and another T factor, hence has bounded coefficient \(aT=U\).  All other
quadratic, commutator, and connection-variation products contain only current
pair \(U_m,C_{m+1}\) and previous T levels; use (2.8) with a finite number of
factors.

Therefore

\[
 {d\over dt}\|T_m\|_p^p+cD^T_{m,p}
 \le C_{m,p}(1+\|T_m\|_p^p),                                    \tag{3.6}
\]

and Gronwall completes stage m.

## 4. Finite exponent closure

At a fixed stage m and target p, equations (2.8) and (3.4) call on only finitely
many previous-level norms.  If a term has N previous factors against a current
power \(|V|^{p-1}\), choose exponent Np for each previous factor.  If Young's
inequality leaves two copies of previous factors against \(|V|^{p-2}\), choose
exponents large enough that their reciprocal sum is at most \(2/p\), and use the
remaining finite-volume exponent.  Hypothesis (1.7) already supplies every
finite exponent at each previous spatial level.

Crucially, the only two appearances of a current unknown cutoff jet are

\[
 |Z|^2|V|^{p-2}
 \quad\text{and}\quad |Z||V|^{p-1},                               \tag{4.1}
\]

which use \(Z,V\in L^p\).  The apparent third appearance
\(\chi Z*U_1*P(V)\) is removed by (2.6).  No current quantity is passed from p
to 2p, so the construction is a finite triangular induction rather than an
infinite exponent ascent.

Starting with \(T_0\), then

\[
 (U_1,C_2)\to T_1\to(U_2,C_3)\to T_2\to\cdots,                  \tag{4.2}
\]

proves all three families in every finite \(L^p\) norm on the positive-time
slab.

## 5. Pointwise derivatives and terminal extension

Choose \(p>n\).  Applying the uniform scalar Sobolev inequality to
\(|U_m|\), with Kato's inequality
\(|\nabla|U_m||\le|U_{m+1}|\), gives

\[
 \|U_m\|_\infty
 \le C\bigl(\|U_m\|_p+\|U_{m+1}\|_p\bigr)<\infty.               \tag{5.1}
\]

Thus every covariant derivative of the compactly supported velocity

\[
 \partial_tg=-2\operatorname{Ric}(U)                             \tag{5.2}
\]

is uniformly bounded.  In particular, \(\partial_tg\),
\(\partial_t\Gamma\), and all spatial derivatives of these tensors are
integrable over the finite time interval.  The standard connection-difference
induction then gives a positive definite smooth limit \(g(T_*)\) in fixed
coordinates.  A short-time theorem for the same normalized fixed-cutoff equation
starting from this terminal metric would restart the solution and yield the
continuation implication

\[
 \sup_{M\times[\tau,T_*)}|U|<\infty
 \quad\Longrightarrow\quad
 \text{smooth extension past }T_* .                              \tag{5.3}
\]

The energy induction above supplies the substantive derivative part of (5.3).
The final restart still relies on a valid transported-coefficient degenerate
short-time construction; it is not proved in this note.

## 6. Independent verification and consequence for the smoothing route

Two independent TTCS branches, integrated in
`trace/ttcs/results/step40_ttcs02_verifier1_integration.md`, checked the
arbitrary-order classification, the extra integration by parts, honest
expansion of \(\nabla^{m+2}a\), the cutoff-jet evolution, and the finite exponent
schedule. They found no term defeating (2.9), (2.11), or (3.6), while making the
two bookkeeping corrections incorporated above. This verification concerns the
derivative-energy induction only; it does not prove the terminal restart.



This staggered ordering removes the two errors in Step 39:

- no derivative of \(a=\chi^2\) is assigned a nonexistent \(\chi\) factor;
- no current \(C_{m+1}\) norm at exponent \(2p\) is replaced by its \(L^p\)
  norm.

Together with the independently supported general-p defect power inequality,
it advances the desired defect-preserving smoothing mechanism.  The result is
still not the full flow theorem until the transported-coefficient start/restart
is established, and even that restricted four-dimensional negative-family
mechanism would not settle the positive branch, arbitrary topology, dimensions
n>=5, dimension-only constants, or Lean formalization required by Yau Problem
26.
