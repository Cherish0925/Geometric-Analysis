# TTCS Independent Branch Record

```json
{
  "step_id": 28,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step23_single_support_wang_bridge.md",
    "Sessions/S0910A03/workspace/notes/step25_whole_support_moser_and_normalization_repair.md",
    "Sessions/S0910A03/workspace/notes/step26_general_p_and_sobolev_resolution.md",
    "Sessions/S0910A01/workspace/notes/step27_unified_weak_moser_iteration.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md"
  ]
}
```

## Task

Independently check the complete analytic chain for the normalized cutoff flow on the selected disjoint supports. Read the actual derivations, not their status labels. Determine whether the q=2 and q=3 estimates, global Q and J6 propagation, general-p tensor inequality, three-factor/time-slab Moser iteration, first-exit closure, and shifted-curvature continuation form a logically closed proof with volume-independent constants for a fixed critical four-manifold. Attack the most consequential non-routine transitions: active-region versus collar energy, use of the unweighted F factor, relative Sobolev domains, polynomial p dependence, terminal H3 propagation, the t=0 splice, and the current-order Wang derivative induction. State any precise missing lemma or false inference, with equations and a concrete repair if available. Do not infer validity from scripts or prior summaries.

## Output

# Scientific verification memo

## Overall assessment

The \(q=2\), \(q=3\), \(Q\), \(J_6\), and Moser portions contain a coherent volume-independent mechanism once three details are formulated precisely:

1. the \(q=2\) energy must be derived directly on the active part before any coarse \(Cr^{-2}H_2\) estimate that includes the stationary collar;
2. the general-\(p\) calculation must retain the \(p(p-2)|\nabla\Phi|^2\) dissipation, or else record a polynomially small coefficient in front of \(\|\nabla Z_p\|_2^2\);
3. all Sobolev and volume factors must refer to one enlarged ambient ball containing the buffered support.

The fixed-weight Moser iteration is valid. Its essential step is not merely the Sobolev estimate for \(Z_p\), but the interpolation
\[
K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2},
\qquad K_{2p}=\|Z_p\|_4^4.
\]
That identity exactly recovers the half-power of \(a\) which would otherwise be lost near \(\{a=0\}\).

The shifted-curvature continuation argument has the correct algebraic mechanism. The supplied text, however, still imports the hardest current-order integration-by-parts estimate from Wang’s Proposition 4.14 through schematic \(*\)-notation. Thus the whole module is not yet an independently self-contained proof from the displayed derivations alone. A precise normalized Wang derivative lemma, stated below, is the remaining substantial source-dependent step.

---

## 1. Active energy versus stationary collar

Let
\[
\widehat H_2(t)=\int_{\operatorname{supp}\chi}F^2\,d\mu_t,
\qquad
C_{\rm col}=
\int_{\operatorname{supp}\eta\setminus\operatorname{supp}\chi}
\eta^2F_0^2\,d\mu_0.
\]
Because \(\eta=1\) near \(\operatorname{supp}\chi\) and
\(\operatorname{supp}d\eta\subset\{a=0\}^{\circ}\),
\[
H_2(t)=\int\eta^2F^2\,d\mu_t=\widehat H_2(t)+C_{\rm col}.
\]
On the open collar, \(a=da=\nabla^2a=0\), hence \(g_t=0\) there and \(C_{\rm col}\) is constant.

The important logical point is that one cannot first replace every lower-order term by \(Cr^{-2}H_2\) and then simply subtract \(C_{\rm col}\). The termwise curvature calculation must retain the fact that every evolving contribution is supported where at least one of
\[
a,\qquad da,\qquad \frac{|da|^2}{a}
\]
is nonzero. Since
\[
\frac{|da|^2}{a}=4|d\chi|^2,
\]
these contributions lie in the active part and are bounded by \(\widehat H_2\), not by the collar energy. The correct active equation is therefore
\[
\boxed{
\widehat H_2'+cD_2
\le Cr^{-2}\widehat H_2+C H_3,
\qquad
H_3=\int aF^3.}
\]
This justifies the collar-free equation asserted in Step 26, but the justification is the termwise support argument, not algebraic subtraction from a previously coarsened inequality.

---

## 2. The \(q=2\) and \(q=3\) estimates

Set
\[
\beta(t)=S(t)\|F(t)\|_{L^2(\operatorname{supp}\chi)}.
\]
The unweighted factor in Hölder is legitimate because the remaining factors vanish off the active support:
\[
H_3
=\int_{\operatorname{supp}\chi}F(\chi F)^2
\le \|F\|_{2,\operatorname{supp}\chi}\|\chi F\|_4^2.
\]
The relative Sobolev estimate gives
\[
\|\chi F\|_4^2
\le S\left(D_2+Cr^{-2}\widehat H_2\right),
\]
using \(|\nabla F|\le|\nabla\operatorname{Rm}|\). Hence
\[
H_3\le C\beta(t)\left(D_2+r^{-2}\widehat H_2\right).
\]
For uniformly small \(\beta\),
\[
\widehat H_2'+\frac c2D_2\le Cr^{-2}\widehat H_2,
\]
so
\[
\widehat H_2(t)\le e^{Ct/r^2}\widehat H_2(0),\qquad
\int_0^tD_2\le C\widehat H_2(0),
\]
and consequently
\[
\int_0^tH_3(s)\,ds
\le C\beta_*\widehat H_2(0).
\]

For \(q=3\),
\[
R_3=\int a^2F^4=\int F(aF^{3/2})^2.
\]
Since
\[
|\nabla(aF^{3/2})|^2
\le C a^2F|\nabla\operatorname{Rm}|^2
   +C|da|^2F^3,
\]
and
\[
|da|^2F^3=4a|d\chi|^2F^3\le Cr^{-2}H_3,
\]
one obtains
\[
R_3\le C\beta(t)(D_3+r^{-2}H_3).
\]
After absorption,
\[
H_3'\le Cr^{-2}H_3.
\]

The terminal estimate is then rigorous. Choose
\(s\in[t/4,t/2]\) such that
\[
H_3(s)\le \frac4t\int_0^{t/2}H_3(\tau)\,d\tau.
\]
Forward propagation from \(s\) to \(t\) gives
\[
H_3(t)\le
\frac{C\beta_*\widehat H_2(0)}{t}.
\]
With \(\widehat H_2(0)=\beta(0)^2/S^2\) and persistence of \(\beta\),
\[
\boxed{S^2H_3(t)\le \frac{C\beta_*^3}{t}.}
\]
Thus the terminal estimate does not arise from a spacetime average alone; the separate \(q=3\) differential inequality is essential and is used correctly.

---

## 3. Global \(Q\) and fixed \(J_6\)

For
\[
Q=\int_M|E|^2,
\]
the homogeneous \(E\)-equation gives
\[
Q'+c\int a|\nabla E|^2
\le
C\int\left(\frac{|da|^2}{a}+a\right)|E|^2
+C\int aF|E|^2.
\]
On each disjoint component,
\[
\int aF|E|^2
=\int F|\chi E|^2
\le
\|F\|_{2,\operatorname{supp}\chi}\|\chi E\|_4^2.
\]
The \(F\)-norm should be written over \(\operatorname{supp}\chi\), rather than the whole auxiliary \(U_j\); this aligns the estimate exactly with the active \(\beta_j\). Sobolev absorption then yields
\[
Q'\le Cr^{-2}Q.
\]
Disjointness prevents any factor proportional to the number of supports.

For
\[
J_6=\int a^4|E|^6,
\qquad
Z_6=a^{5/2}|E|^3,
\]
the potential term is
\[
\int a^5F|E|^6
=\int F|Z_6|^2
\le
\|F\|_{2,\operatorname{supp}\chi}\|Z_6\|_4^2.
\]
Hence
\[
J_6'+c\|\nabla Z_6\|_2^2
\le Cr^{-2}J_6+C\beta
  \bigl(\|\nabla Z_6\|_2^2+r^{-2}J_6\bigr),
\]
and small \(\beta\) gives
\[
\boxed{J_6(t)\le e^{Ct/r^2}J_6(0).}
\]
The pointwise initial estimate \(|E(0)|\le\delta\) then preserves the factor
\(\delta^6\).

---

## 4. General-\(p\) coercivity needs one correction

The displayed inference in Step 26 from
\[
K_p'+cD_p\le Cp^2r^{-2}K_p+CpR_p
\]
to an inequality with a uniform coefficient multiplying
\(\|\nabla Z_p\|_2^2\) is not justified from \(D_p\) alone. Indeed,
\[
\|\nabla Z_p\|_2^2
\lesssim
p^2D_p+p^2r^{-2}K_p,
\]
so a coefficient \(cD_p\) would produce only \(c p^{-2}\|\nabla Z_p\|_2^2\).

The curvature calculation itself contains the repair. The Laplacian term supplies both
\[
p\int a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2
\]
and
\[
p(p-2)\int a^{p-1}F^{p-2}|\nabla F|^2.
\]
Since the \(\Phi\)-derivative part of
\[
Z_p=a^{(p-1)/2}\Phi^{p/2}
\]
has coefficient \(p^2\), the second integral controls it uniformly for \(p\ge3\). The correct retained form is
\[
\begin{aligned}
K_p'
&+c_1p\int a^{p-1}F^{p-2}|\nabla\operatorname{Rm}|^2\\
&+c_2p(p-2)\int a^{p-1}F^{p-2}|\nabla F|^2
\le Cp^2r^{-2}K_p+CpR_p.
\end{aligned}
\]
This implies
\[
\boxed{
K_p'+c\|\nabla Z_p\|_2^2
\le Cp^2r^{-2}K_p+CpR_p.}
\]
The regularized defect calculation has the same structure: the tensor term controls \(\nabla E\), while the chain rule supplies
\[
p(p-2)a\Phi_\varepsilon^{p-2}|\nabla\Phi_\varepsilon|^2.
\]

Even without retaining this term, a coefficient \(cp^{-2}\) could be carried through; it would only increase the polynomial power of \(p\). The present uniform-\(c\) formula nevertheless requires the scalar dissipation to remain visible.

---

## 5. Three-factor absorption and Moser recurrence

The exact factorization is
\[
\eta^2a^{p-1}F\Phi^p
=(aF^3)^{1/3}
 (\eta^2a^{p-2}\Phi^p)^{1/3}
 |Z_p|^{4/3}.
\]
Therefore
\[
R_p\le Y^{1/3}K_p^{1/3}\|Z_p\|_4^{4/3},
\qquad
Y=\int aF^3.
\]
After Sobolev and Young,
\[
CpR_p
\le \frac c2\|\nabla Z_p\|_2^2
+Cp^3S^2Y\,K_p
+Cp^3r^{-2}K_p.
\]
The \(p^3\) power is consistent with choosing the Young parameter of order \(p^{-1}\).

The nontrivial weight transition is
\[
\boxed{
K_{3p/2}\le K_p^{1/2}K_{2p}^{1/2}.}
\]
Moreover, because \(\eta=1\) wherever \(a>0\),
\[
K_{2p}
=\int a^{2p-2}\Phi^{2p}
=\|Z_p\|_4^4.
\]
Without the strict \(\eta=1\) plateau this equality would be unavailable in the required direction.

On \([t/2,t]\),
\[
S^2Y(s)\le C\beta^3/t,
\]
so the time-cutoff energy estimate and the interpolation above give
\[
\mathcal M_{3p/2,j+1}
\le CS\bigl(L_j\mathcal M_{p,j}\bigr)^{3/2},
\qquad
L_j=Cp^3 4^j(t^{-1}+r^{-2}).
\]
The infinite product converges since
\[
\sum_jp_j^{-1}<\infty,
\qquad
\sum_j\frac{j+\log p_j}{p_j}<\infty.
\]

For a clean terminal estimate, the times may be chosen with
\[
\tau_j\uparrow 3t/4,
\]
leaving the final slab \([3t/4,t]\). Step 26 instead writes
\(\tau_j\uparrow t\); that still yields the value at \(t\) using smoothness, but the \(3t/4\) version is the standard stronger formulation.

The resulting estimates are
\[
\boxed{\|aF(t)\|_\infty\le C\beta/t}
\]
and
\[
\boxed{
\|aE(t)\|_\infty
\le C\delta(r^2/t)^{1/3}.}
\]

---

## 6. Relative Sobolev volume and collapse cancellation

One ambient ball must be used consistently. Let
\[
\operatorname{supp}\eta\Subset B_R(x),
\qquad V_R=\operatorname{Vol}(B_R(x)),
\]
with \(R\) comparable to \(r\). The relative Sobolev estimate is
\[
S\le C(4,KR^2)R^2V_R^{-1/2}.
\]
The maximal-function estimate must apply at radius \(R\):
\[
\int_{\operatorname{supp}\chi}F^2
\le CK_0V_R.
\]
Then
\[
\beta(0)\le CR^2\sqrt{K_0},
\]
independently of \(V_R\).

Likewise,
\[
J_6(0)\le\delta^6V_R,
\]
and the defect output contains
\[
S^{1/3}V_R^{1/6}
\le CR^{2/3}.
\]
Thus the volume cancels exactly. The notes alternate between \(U_j\), \(B_r\), and \(B_{6r}\); the proof needs the single enlarged ball formulation above. If the cited local Poincaré theorem uses a dilated ball for the gradient integral, the existing buffer accommodates it by replacing \(R\) with a fixed multiple.

---

## 7. First-exit and the \(t=0\) splice

There is no singular-time obstruction at \(t=0\):

* short-time smooth existence supplies an initial interval for each fixed metric and cutoff;
* the defect estimate is integrable:
  \[
  \int_0^{\theta r^2}\|aE(s)\|_\infty ds
  \le C\delta\theta^{2/3}r^2;
  \]
* hence
  \[
  e^{-2I(t)}g_0\le g(t)\le e^{2I(t)}g_0,
  \qquad
  I(t)=\int_0^t\|aE(s)\|_\infty ds;
  \]
* this preserves the relative Sobolev inequality, cutoff-gradient estimate, fixed-domain volumes, and active \(\beta\);
* the \(q=2\), \(Q\), and \(J_6\) Grönwall estimates then strictly improve their bootstrap constants for sufficiently small \(\theta\) and \(\delta\).

If a maximal smooth time \(T\in(0,\theta r^2)\) occurred, the estimate
\[
|a\operatorname{Rm}(t)|\le C\beta/t
\]
is uniformly bounded on \([T/2,T)\), while ordinary smoothness supplies a finite bound on \([0,T/2]\). Thus the continuation theorem applies at every positive terminal time; the \(t^{-1}\) behavior near zero is irrelevant there.

---

## 8. Shifted-curvature continuation

The shift
\[
G=\frac{g\owedge g}{2(n-1)},\qquad
T=\operatorname{Rm}+G,\qquad
U=aT
\]
is correct:
\[
\operatorname{Ric}(G)=g,\qquad
aE=\operatorname{Ric}(U),\qquad
g_t=-2\operatorname{Ric}(U).
\]
It removes an independent \(ag\) branch from the connection evolution. The shifted tensor equation
\[
(\partial_t-a\Delta)T
=da*\nabla T+\nabla^2a*T+a(T*T+G*T)
\]
is consistent with the stationary state \(T=0\). In particular, there is no \(\nabla^2a*G\) source.

The base unweighted estimate is also sound:
\[
\frac d{dt}\int|T|^p
+c_p\int a|\nabla T|^2|T|^{p-2}
\le C_p\int|T|^p.
\]
The Hessian-\(a\) term is integrated once and controlled through
\[
|da|^2/a=4|d\chi|^2.
\]

The unresolved self-contained step is the current-order weighted derivative estimate. The raw differentiated \(U\)-equation contains
\[
\Gamma_1=\chi\nabla^{m+2}\chi*U,\quad
\Gamma_2=\nabla\chi*\nabla^{m+1}\chi*U,
\]
\[
\Gamma_3=\chi\nabla^{m+1}\chi*\nabla U,\quad
\Gamma_4=\chi\nabla\chi*\nabla^{m+1}U.
\]
The supplied Codex report states that Wang’s contraction-preserving integrations give
\[
\left|
\int |\nabla^mU|^{p-2}\nabla^mU*
       \sum_{\nu=1}^4\Gamma_\nu
\right|
\le
\varepsilon D_m+C(1+\|\nabla^mU\|_p^p),
\]
with only the residual product
\[
\nabla^2\chi*\nabla^m\chi*U*
\nabla^mU|\nabla^mU|^{p-2}.
\]
This is precisely the needed lemma, but its proof is imported through “verbatim Wang” rather than displayed. The shorter Step 27 argument instead couples
\(\nabla^mU\) with \(\nabla^{m+1}\chi\), again referring to Wang’s finite staggered-exponent system.

A complete source-level formulation would state:

> For each \(m\) there is a finite family of exponents \(p_\nu>n+2\) such that the energies of \(\nabla^mU\) and \(\nabla^{m+1}\chi\), together with already established lower derivatives, satisfy
> \[
> Y_m'(t)+cD_m(t)
> \le C_m\left(1+Y_m(t)+\int_0^tY_m(s)\,ds\right),
> \]
> and every added \(G\)-monomial is bounded by \(C(1+Y_m)\).

The displayed \(G\)-terms
\[
\sum_{i+j=m}\nabla^ia*G*\nabla^jU
\]
do satisfy this estimate and introduce no new top derivative. Thus the normalization does not create a new analytic obstruction. What remains is the exact Wang Proposition 4.14 transfer, including the finite exponent assignments and the grouped integrations of \(\Gamma_1,\Gamma_2,\Gamma_3\).

The normalized DeTurck restart is structurally correct: the added term
\(-2\widehat a\,\widehat g\) is zeroth order, and transporting the same
\(\widehat a\) in both normalized terms recovers the fixed coefficient after pullback. A fully independent presentation would package this with the derivative lemma as a normalized local-flow extension theorem.

---

## Conclusion

The active energy estimates, terminal \(H_3\) propagation, global \(Q\), \(J_6\), three-factor absorption, time-slab Moser iteration, volume cancellation, and \(t=0\) splice fit together mathematically. The displayed general-\(p\) proof needs the retained \(p(p-2)\) scalar dissipation, and the Sobolev notation needs one consistent enlarged ball.

The only substantial non-self-contained transition is the current-order Wang derivative induction and its degenerate DeTurck restart. The shifted tensor identities show that the normalized term is compatible with Wang’s triangular structure, but the supplied material still cites the central grouped integration and exponent hierarchy rather than deriving them in full. Once that normalized Wang lemma is admitted from the cited source transfer, the cutoff-flow analytic chain closes with constants independent of collapsed support volume for the fixed four-dimensional construction.