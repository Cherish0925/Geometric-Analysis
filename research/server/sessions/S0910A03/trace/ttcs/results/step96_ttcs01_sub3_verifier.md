# TTCS Independent Branch Record

```json
{
  "step_id": 96,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step96_koiso_einstein_cauchy_evolution.py",
    "Sessions/S0910A03/workspace/scripts/step96_initial_taylor_invariants.py",
    "Sessions/S0910A03/workspace/scripts/step96_relative_KX_diagnostic.py",
    "Sessions/S0910A03/workspace/data/step96_initial_taylor_invariants.json",
    "Sessions/S0910A03/workspace/data/step96_koiso_einstein_cauchy_evolution_N96_short.json",
    "Sessions/S0910A03/workspace/data/step96_relative_KX_diagnostic.json",
    "Sessions/S0910A03/workspace/notes/step94_charge_sign_correction_and_global_flux.md",
    "Sessions/S0910A03/workspace/notes/step95_KX_and_bochner_cancellation.md"
  ]
}
```

## Task

Read the Step 96 charged-Koiso Einstein Cauchy evolution and relative K_X experiment as a differential geometer/numerical analyst. Check (i) the Gaussian evolution equations and sign conventions; (ii) whether the extraction of quotient variables a, rho, connection, charge, Q and K_X is invariantly correct; (iii) whether the initial Taylor conclusions H_n=2, sigma_nn=6+Q, a_nn=-(4+Q) (as the data suggest), and coordinate-charge conservation follow analytically; (iv) whether the short-resolution results at n=0.02 genuinely support a local exact continuation or are numerical artifacts; (v) whether the R_X numerator cancellation is an independent validation of the Noether pairing or merely an integration identity; and (vi) what exact finite-dimensional/joint-matching object should be constructed next from this center, without reverting to radial flat-slice models or assuming a bounded transition. Identify any errors precisely and derive corrected formulas where possible.

## Output

# Scientific verification memo

## 1. Gaussian evolution and signs

With
\[
g=dn^2+q_{ij}(n,s)\,dy^i dy^j,\qquad K=\frac12\partial_nq,\qquad
W=q^{-1}K,\qquad H=\operatorname{tr}W,
\]
the normal Christoffel symbols are
\[
\Gamma^n_{ij}=-K_{ij},\qquad \Gamma^i_{nj}=W^i{}_j.
\]
Consequently,
\[
\operatorname{Ric}_{nn}=-\partial_nH-|W|^2,
\]
\[
\operatorname{Ric}_{ni}=(\operatorname{div}_qK-dH)_i,
\]
and
\[
\operatorname{Ric}_{ij}(g)
=\operatorname{Ric}_{ij}(q)-\partial_nK_{ij}-HK_{ij}
+2(Kq^{-1}K)_{ij}.
\]
Thus \(\operatorname{Ric}_g=-3g\) gives exactly
\[
\partial_nq=2K,\qquad
\partial_nK=\operatorname{Ric}(q)+3q-HK+2Kq^{-1}K.
\]
The Gauss equation gives
\[
R(q)-H^2+|W|^2=-6,
\]
and the mixed equation gives
\[
\operatorname{div}_qK-dH=0.
\]
The signs used in `step96_koiso_einstein_cauchy_evolution.py` are therefore correct.

Equivalently,
\[
q_{nn}=2\operatorname{Ric}(q)+6q-Hq_n+q_nq^{-1}q_n.
\]
This is an analytic system solved explicitly for the second \(n\)-derivative. Since the continuum Step 94 data are periodic analytic functions of \(s\) and satisfy the two constraints, Cauchy–Kowalevski produces a periodic analytic local solution. The contracted Bianchi identity propagates the normal and mixed equations from the center. Hence the exact local Einstein germ follows analytically; the numerical evolution is evidence about its short normal development, not the source of local existence.

Reversing the normal sends \(K\mapsto-K\). At a minimal center \(H=0\), \(\partial_nH\) is unchanged when expressed in the outward coordinate on each side.

---

## 2. Quotient variables and invariance

Writing the full metric as
\[
g=dn^2+a^2ds^2+
G_{ab}\bigl(dx^a+\mathcal A^a_sds\bigr)
\bigl(dx^b+\mathcal A^b_sds\bigr),
\]
the code uses
\[
G=q_{ab},\qquad v_a=q_{as},\qquad
\mathcal A_s=G^{-1}v,\qquad
a^2=q_{ss}-v^TG^{-1}v.
\]
These are the correct Schur-complement formulas. In the Gaussian/temporal gauge \(g_{na}=0\), the other connection component is zero and
\[
F^a_{ns}=\partial_n\mathcal A_s^a,\qquad
f^a=F^a(e_n,e_s)=\frac{\partial_n\mathcal A_s^a}{a}.
\]
The implemented derivative
\[
\partial_n\mathcal A_s
=G^{-1}\bigl(v_n-G_n\mathcal A_s\bigr)
\]
is correct.

For
\[
\rho=\sqrt{\det G},\qquad \sigma=\log\rho,\qquad M=\rho^{-1}G,
\]
one has \(\det M=1\), and
\[
c=\rho Gf,\qquad
Q=\frac12f^TGf
=\frac12c^T\bigl(e^{-3\sigma}M^{-1}\bigr)c.
\]
Since
\[
e^{-3\sigma}M^{-1}=\rho^{-2}G^{-1},
\]
both `charge`, `Q`, and `Amat` are implemented correctly. The weighted measure is
\[
d\mu_\sigma=e^\sigma d\operatorname{vol}_{\gamma_B}
=\rho a\,dn\,ds,
\]
also matching the code.

Important distinctions:

* \(a,\rho,F,c,Q\) are geometric once the torus lattice basis and orientation are fixed.
* \(\mathcal A_s\) itself is gauge-dependent. Thus `connection_abs_max` is not an invariant observable. Its normal derivative represents curvature only in the temporal gauge used here.
* The sign of \(c\) depends on the orientation of \(dn\wedge ds\). The code obtains \(c=-\mathfrak q\) at the center, whereas the metadata records the positive amplitude of \(\mathfrak q\). This is consistent but should be stated explicitly.
* Componentwise means and standard deviations of \(c\) depend on the fixed torus basis, although the statement \(dc=0\) does not.
* The clipping in `sqrt(max(a2,0))` and `sqrt(max(detG,0))` would mask a sign change in longer integrations. It is inactive here because the reported \(q\)-eigenvalue minimum remains \(0.127>0\).

### One concrete denominator error

The shape derivative is
\[
C_n=M^{-1}M_n=G^{-1}G_n-\sigma_nI,
\qquad
|U_n|_h^2=\frac12\operatorname{tr}(C_n^2).
\]
Because \(n\) is already unit speed in the quotient metric, there is no factor \(a^{-2}\). The line
```python
Un2=.5*np.einsum(...)/(a*a)
```
should be
```python
Un2=.5*np.einsum("nij,nji->n", Cn, Cn)
```
and then
```python
dUX=np.abs(ch)*np.sqrt(np.maximum(Un2,0))
```
is the correct \(|dU(X)|\). Division by \(a^2\) belongs to an \(s\)-derivative, not an \(n\)-derivative. Since \(a\) differs from one by less than \(10^{-3}\) at \(n=0.02\), this has a tiny effect on the displayed denominator.

If the denominator is intended as the dual coefficient controlling the Noether right side under
\(|H|,|T|,|Z|\le\varepsilon\), the natural pointwise weights are
\[
2|\operatorname{sym}\nabla X|
+\sqrt2\,|\operatorname{div}_\sigma X|
+|\operatorname{div}X|
+|dU(X)|,
\]
using \(|\operatorname{tr}H|\le\sqrt2|H|\) in two dimensions. The present denominator omits the factors \(2\) and \(\sqrt2\); it is a normalized heuristic ratio rather than the exact dual norm of the displayed Noether expression.

---

## 3. Exact center Taylor coefficients

Let the center data be
\[
q_\Sigma=ds^2+M(s)_{ab}dx^adx^b,\qquad \det M=1,
\]
and
\[
W=
\begin{pmatrix}
0&m_b\\
m^a&B^a{}_b
\end{pmatrix},
\qquad
m=-\frac12\mathfrak q.
\]
Write
\[
Q=\frac12\mathfrak q^TM^{-1}\mathfrak q,\qquad
\operatorname{tr}(B^2)=P,\qquad P+Q=S.
\]
Then
\[
|W|^2=S,\qquad H=0.
\]

### Mean curvature

The normal Einstein equation gives
\[
-H_n-|W|^2=-3,
\]
hence
\[
\boxed{H_n=3-S.}
\]
For the numerical choice \(S=1\),
\[
\boxed{H_n=2.}
\]
This is also the constant term in the full Jacobi operator at the minimal center.

### Base scale

For the intrinsic center metric,
\[
\operatorname{Ric}_{ss}(q_\Sigma)
=-\frac12|U_s|^2
=-6-S,
\]
because \(|U_s|^2=12+2S\). Moreover,
\[
(Kq^{-1}K)_{ss}=m^TM^{-1}m=\frac Q2.
\]
The tangential evolution therefore gives
\[
(K_n)_{ss}=-6-S+3+Q=-3-S+Q,
\]
so
\[
(q_{ss})_{nn}=-6-2S+2Q.
\]
At the center,
\[
v_n=2m=-\mathfrak q,\qquad
v_n^TM^{-1}v_n=2Q.
\]
Since \(a^2=q_{ss}-v^TG^{-1}v\),
\[
(a^2)_{nn}
=(q_{ss})_{nn}-2v_n^TM^{-1}v_n
=-6-2S-2Q.
\]
As \(a=1\) and \(a_n=0\),
\[
\boxed{a_{nn}=-3-S-Q.}
\]
For \(S=1\),
\[
\boxed{a_{nn}=-(4+Q).}
\]

### Orbit area

The spatial slice volume density is
\[
\sqrt{\det q}=a\rho,
\]
so
\[
H=\partial_n\log(a\rho)=\frac{a_n}{a}+\sigma_n.
\]
At the center \(a_n=\sigma_n=0\), hence
\[
H_n=a_{nn}+\sigma_{nn}.
\]
Combining the preceding formulas gives
\[
\boxed{\sigma_{nn}=6+Q.}
\]

Thus the exact second-order expansions for \(S=1\) are
\[
H=2n+O(n^2),
\]
\[
a=1-\frac12(4+Q)n^2+O(n^3),
\]
\[
\sigma=\frac12(6+Q)n^2+O(n^3),
\qquad
\rho=1+\frac12(6+Q)n^2+O(n^3).
\]
The base circle contracts while the torus-orbit area expands. Their sum gives the positive second variation of the full slice volume.

### Coordinate charge

At the center,
\[
\partial_n\mathcal A_s
=G^{-1}v_n=-M^{-1}\mathfrak q,
\]
and therefore
\[
c=\rho Gf=-\mathfrak q
\]
for the orientation used by the code. The mixed Einstein equations give
\[
dc=0
\]
throughout the connected analytic germ. Hence both \(c_s=0\) and \(c_n=0\) hold exactly. The reported
\[
\max|c_n|\simeq9.8\times10^{-14}
\]
is the expected floating-point residual.

---

## 4. Interpretation of the \(n=0.02\) computation

The short run is quantitatively consistent with the exact Taylor coefficients:

* From \(Q\in[0.00862,0.5]\),
  \[
  \sigma(0.02)\approx \tfrac12(6+Q)(0.02)^2
  \in[0.0012017,0.0013000].
  \]
  The computed
  \[
  \rho\in[1.0012022,1.0013013]
  \]
  agrees at the expected order.

* The quadratic prediction
  \[
  a(0.02)\approx1-\tfrac12(4+Q)(0.02)^2
  \in[0.9991,0.999198]
  \]
  agrees with
  \[
  a\in[0.9990785,0.9991693].
  \]

* The initial \(\max|\partial_n\mathcal A_s|=2.75946\) predicts
  \[
  \max|\mathcal A_s(0.02)|\approx0.05519,
  \]
  compared with \(0.05573\).

* \(H\sim0.04\) at first order; the computed mean \(0.03604\) shows visible higher normal derivatives but remains consistent with the Taylor direction.

The resolution data also show strong spatial convergence:

\[
\begin{array}{c|ccc}
N&48&64&96\\ \hline
\max|\mathcal H|&8.32\!\times10^{-2}&9.96\!\times10^{-3}&1.32\!\times10^{-4}\\
\max|\mathcal M|&5.79\!\times10^{-2}&1.01\!\times10^{-2}&2.29\!\times10^{-4}\\
\max_s\operatorname{std}(c)&2.41\!\times10^{-4}&3.75\!\times10^{-5}&7.98\!\times10^{-7}\\
Q_{\max}(0.02)&0.5095501&0.5095584&0.5095580
\end{array}
\]

At \(N=96\), however, the initial momentum residual is already
\(2.09\times10^{-4}\), versus \(2.29\times10^{-4}\) at the final sample. Much of the terminal mixed residual therefore comes from spectral construction of the initial \(K\), rather than growth during the \(0.02\) interval. The Hamiltonian residual starts near \(10^{-11}\) and grows to \(1.3\times10^{-4}\), reflecting the filtered semidiscrete evolution.

Because the retained modes satisfy roughly \(|k|\le32\) at \(N=96\), elliptic amplification over \(n=0.02\) is only of order \(e^{32(0.02)}\simeq1.9\). The interval is short enough that the ill-posed high-mode mechanism has not become dominant. The supplied numbers therefore support convergence of the short semidiscrete evolution to the analytic germ. They do not reveal its behavior at normal distances comparable with one.

A stronger numerical record would include inter-resolution norms of the fields after Fourier restriction to common modes, runs at \(N=128,160\), and comparisons among filtered and unfiltered systems. The exact analytic germ itself is already supplied by the analytic evolution argument.

---

## 5. What the relative \(K_X\) cancellation measures

Let
\[
A_{\rm ch}=e^{-3\sigma}M^{-1}=\rho^{-2}G^{-1},
\qquad
Q=\frac12c^TA_{\rm ch}c,
\qquad
m_c=c^TA_{\rm ch}dc.
\]
For any vector field \(X\),
\[
X(Q)=m_c(X)+\frac12c^TX(A_{\rm ch})c.
\]
Using
\[
K_X=X(A_{\rm ch})+(\operatorname{div}_\sigma X)A_{\rm ch},
\]
one obtains pointwise
\[
\frac12c^TK_Xc
=\operatorname{div}_\sigma(QX)-m_c(X).
\]
If \(X\) vanishes at the two strip ends,
\[
\frac12\int c^TK_Xc\,d\mu_\sigma
=-\int m_c(X)\,d\mu_\sigma.
\]

For an exactly fixed charge \(dc=0\),
\[
\frac12c^TK_Xc=\operatorname{div}_\sigma(QX),
\]
so its integral vanishes for every metric, independently of the Einstein equations and independently of the horizontal Noether identity. This explains the large opposite slice values
\[
252.75\quad\text{and}\quad -254.55
\]
and their tiny integrated remainder.

The reported numerators
\[
7.93\times10^{-9},\quad2.34\times10^{-9},\quad2.66\times10^{-9}
\]
do not decrease monotonically from \(N=64\) to \(N=96\). They are most naturally read as temporal quadrature and ODE-tolerance remnants in an integral that is already a total weighted divergence. The ratio \(R_X\sim10^{-10}\) is therefore not an independent numerical validation of the horizontal Bianchi/Noether formula.

An independent computational comparison would evaluate three separately coded quantities:

\[
-\frac12\int c^TK_Xc\,d\mu_\sigma,
\qquad
\int m_c(X)\,d\mu_\sigma,
\]
and
\[
\int\!\left[
2H:\operatorname{sym}\nabla X
-(\operatorname{tr}H)\operatorname{div}_\sigma X
+T\operatorname{div}X
-\langle Z,dU(X)\rangle
\right]d\mu_\sigma.
\]
Agreement for several \(s\)-dependent vector fields with both normal and tangential components would test the quotient reduction and Noether coefficients. The present computation evaluates only the first expression.

---

## 6. The appropriate joint matching object

A pure Einstein continuation from this center cannot meet an OT collar: \(dc=0\) and \(c_\Sigma=-\mathfrak q\ne0\). The useful continuum object is therefore a **two-sided Lyapunov–Schmidt matching map for the full \(s\)-dependent \(T^2\)-invariant quotient system with metric-generated Ricci defect**.

Take a small exact Koiso collar \(|n|\le\varepsilon\). On each side use a strip
\[
B_{\pm,L_\pm}=[\varepsilon,L_\pm]\times S^1,
\]
with \(L_\pm\) free, full fields
\[
Y=(a,\sigma,M,\mathcal A_s),
\]
and outer data in a finite-dimensional family of exact OT collars. Solving the infinite-dimensional complementary equations leaves a finite matching map whose components are:

1. **Two coordinate-charge balances on each side**
   \[
   c_{\rm OT}-c_\Sigma
   =\int_{\gamma_\pm}dc
   =2\int_{\gamma_\pm}\rho\,
   E(J\dot\gamma_\pm,V)\,dr
   \in\mathbb R^2,
   \]
   with the orientation sign fixed consistently.

2. **Horizontal Noether moments** against a basis \(X_j^\pm\) of the relevant adjoint cokernel:
   \[
   \int_{B_{\pm,L_\pm}}\!\left[
   2H:\operatorname{sym}\nabla X_j
   -(\operatorname{tr}H)\operatorname{div}_\sigma X_j
   +T\operatorname{div}X_j
   -\langle Z,dU(X_j)\rangle
   \right]d\mu_\sigma
   +\frac12\int c^TK_{X_j}c\,d\mu_\sigma=0.
   \]

3. **Flat-connection holonomy matching**
   \[
   \oint_{S^1}\mathcal A_s\,ds
   \quad \bmod \text{the torus lattice},
   \]
   since \(\mathcal A_s\) itself is gauge-dependent while its holonomy remains relevant when \(F\) reaches zero.

4. **Outer Jacobi-mode matching** between the strip Cauchy data and the chosen OT collar family, projected onto the finite kernel and cokernel left after solving the complementary elliptic equations.

The two sides share the same central parameters \((S,\mathfrak q,U\text{-phase},M\text{-frame})\), so their maps must be solved jointly. Keeping \(L_\pm\) as variables incorporates arbitrarily long redshift regions rather than fixing a transition length. The interior equations retain all \(s\)-dependence, the curved base factor \(a(n,s)\), orbit map \(M(n,s)\), and connection curvature.

The missing mathematical substance is the Fredholm analysis that identifies the exact kernel and cokernel dimensions for this strip problem, together with an OT collar family and a metric transition family whose generated tensor \(E=\operatorname{Ric}+3g\) becomes uniformly small while the charge, horizontal moments, holonomy, and end Jacobi data all match. Arbitrarily prescribing \(dc,H,T,Z\) separately would not represent a metric, because the Bianchi/Noether identity couples them.