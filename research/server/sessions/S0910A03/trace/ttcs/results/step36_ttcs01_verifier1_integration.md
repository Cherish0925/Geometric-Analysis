# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 36,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step36_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step36_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Review the Step 35 analytic handoff for the normalized fixed-cutoff Ricci flow in the four-dimensional negative Ishida--LeBrun route. Focus on four interfaces: (i) whether the unregularized fixed J6 persistence lemma is a genuine valid advance and exactly what assumptions it still needs; (ii) whether the Step 35 DeTurck/existence note uses the correct gauge and transported coefficient, and whether its epsilon/Schauder argument actually gives epsilon-independent smooth existence; (iii) whether the cutoff-jet continuation note proves an extension criterion on [0,Tmax) or instead assumes smoothness/uses uncontrolled quantities such as unweighted T or a∇Rm; and (iv) whether terminal calibration still needs a separate global Q=∫|E|^2 estimate rather than J6 or |aE|. Give a direct scientific memo with corrected mathematical status and the next proof targets, not publication advice.

## Integrated Scientific Memo

# Scientific memo: corrected status of the Step 35 analytic handoff

This memo verifies the Step 35 handoff for the normalized fixed-cutoff flow
\[
\partial_t g=-2aE,\qquad a=\chi^2,\qquad E=\operatorname{Ric}_g+g
\]
in the four-dimensional negative Ishida–LeBrun route, at the four requested interfaces.

## 1. Unregularized fixed \(J_6\) persistence

The unregularized \(J_6\) lemma is a genuine analytic advance, but only as a conditional persistence estimate on a provisional first-exit interval.

The valid core is this. Set
\[
s=|E|^2,\qquad J_6=\int \eta^2 a^4s^3\,d\mu,\qquad
X_6=\int \eta^2a^5s^2|\nabla E|^2\,d\mu .
\]
Because \(s^3=|E|^6\) and the test function
\[
q=3\eta^2a^4s^2
\]
are smooth tensor-polynomial quantities, no Kato regularization near \(E=0\) is needed. The chain rule gives
\[
(\partial_t-a\Delta)s^3
=3s^2(\partial_t-a\Delta)s-6as|\nabla s|^2,
\]
and the principal defect dissipation contributes
\[
-6\int \eta^2a^5s^2|\nabla E|^2=-6X_6,
\]
with the extra \(-6\int\eta^2a^5s|\nabla s|^2\le0\) discarded.

The cutoff-Hessian terms can be controlled provided one integrates by parts the actual tensor \(\nabla_i\nabla_j a\), not \(|\nabla^2a|\). The load-bearing structure is
\[
T_H=\int a_{ij}\,q\,B_0^{ij}(E),
\]
where
\[
B_0^{ij}=2g^{ij}|E|^2+2\tau E^{ij}-4E^{ik}E_k{}^j,
\qquad \tau=\operatorname{tr}E,
\]
so \(B_0=O(s)\) and \(\nabla B_0=O(s^{1/2}|\nabla E|)\). After one integration by parts, every top cutoff term reduces to either
\[
a^3|da|^2s^3
\]
or
\[
a^4|da|s^{5/2}|\nabla E|,
\]
and hence
\[
|T_H|\le \varepsilon X_6+C_\varepsilon r^{-2}J_6
\]
using \(a=\chi^2\), \(|d\chi|\lesssim r^{-1}\), and
\[
a^3|da|^2=4a^4|d\chi|^2\lesssim r^{-2}a^4 .
\]

One displayed term in the Step 35 note should be corrected: the first-derivative cutoff contribution in §3.6 should have the same power as \(I_1\),
\[
C\int \eta^2a^4|da|\,s^{5/2}|\nabla E|,
\]
not \(s^{3/2}\). With \(s^{5/2}\), Young’s inequality gives exactly the required
\[
\varepsilon X_6+C_\varepsilon r^{-2}J_6 .
\]

The reaction and measure terms reduce to
\[
CJ_6+CP_6,
\qquad
P_6=\int \eta^2a^5F s^3\,d\mu .
\]
The important improvement is the two-factor absorption
\[
P_6=\int Fw_6^2
\le \|F\|_{2,U}\|w_6\|_4^2,
\qquad
w_6=\eta a^{5/2}s^{3/2}=\eta\chi^5|E|^3 .
\]
Here \(w_6\in W^{1,2}\), indeed \(C^1\) for smooth \(E,\chi,\eta\), and
\[
\|\nabla w_6\|_2^2
\le C(X_6+r^{-2}J_6),
\]
because the \(d\eta\) term vanishes on \(\operatorname{supp}d\eta\), where \(a=da=0\), the \(d\chi\) term gives \(r^{-2}J_6\), and
\[
|\nabla s|^2\le 4s|\nabla E|^2
\]
gives the \(X_6\) term. The local Sobolev inequality yields
\[
P_6\le C\mathcal S K_2^{1/2}(X_6+r^{-2}J_6)
= C\gamma(X_6+r^{-2}J_6),
\]
where
\[
K_2\simeq \int_U F^2\,d\mu,\qquad \gamma=\mathcal S K_2^{1/2}.
\]

Thus the corrected differential inequality is
\[
J_6'+cX_6
\le C(1+r^{-2})J_6+CP_6.
\]
If
\[
C\gamma\le c/2,
\]
then
\[
J_6'+\frac c2X_6
\le C(1+r^{-2})J_6,
\]
and therefore
\[
J_6(t)\le e^{C(1+r^{-2})t}J_6(0).
\]

This is independent of the \(q=3\) curvature seed \(Y=\int aF^3\). That is the real advance: the defect reaction is linear in \(F\), so \(P_6\) needs only \(L^2\) curvature control. But the lemma still assumes:

1. smooth existence of the fixed-cutoff flow on the interval;
2. moving metric/support/Sobolev comparability;
3. a local Sobolev inequality
   \[
   \|u\|_4^2\le \mathcal S(t)(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2);
   \]
4. \(K_2(t)\) persistence strong enough that \(\gamma(t)=\mathcal S(t)K_2(t)^{1/2}\) remains below the absorption threshold;
5. the cutoff geometry
   \[
   a=\chi^2,\quad 0\le a\le1,\quad |d\chi|\lesssim r^{-1},\quad
   \eta=1\text{ near }\operatorname{supp}\chi,\quad a=da=0\text{ on }\operatorname{supp}d\eta .
   \]

So \(J_6\) persistence is not unconditional. It is a valid component of the first-exit bootstrap once \(K_2\) persistence and moving geometry are available.

One algebraic item still deserves independent hand verification: the printed Step 35 expression for a “metric variation” source contains a malformed index pattern involving \(E^{jkl}{}^p\). The estimate only needs the schematic bound \(a\,\mathrm{Rm}*E*E\), but a final proof should recompute \((\partial_t-a\Delta)s\) and the Hessian contraction \(B_0^{ij}\) cleanly.

---

## 2. DeTurck/existence note

The Step 35 degenerate-flow existence note is not a correct proof as written.

There are two separate problems.

### 2.1 Gauge and transported coefficient

The note writes a DeTurck-modified equation schematically as
\[
\partial_t g
=
-2a(\operatorname{Ric}+g)
+a(\nabla W+\nabla W)
=a\mathcal F(g),
\]
with fixed coefficient \(a=\chi^2\). This is not the correct geometric DeTurck construction for the fixed-cutoff equation.

For a local flow, the coefficient must be transported in the gauged equation. Yang’s local Ricci-flow construction uses a hatted coefficient of the form
\[
\widehat a=(\chi\circ\varphi_t^{-1})^2 .
\]
For the normalized equation, the corresponding hatted system should be of the form
\[
\partial_t\widehat g
=
-2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
+\mathcal L_{\widehat a W(\widehat g)}\widehat g
\]
or Yang’s equivalent \(\widehat\delta^*(\widehat a\,\omega)\) formulation. The important point is that the coefficient is part of the gauged vector-field mechanism. Then
\[
\varphi_t^*\widehat a=\chi^2
\]
and the Lie derivative cancels under pullback, giving the original fixed-cutoff equation
\[
\partial_t g=-2\chi^2(\operatorname{Ric}_g+g).
\]

If instead one solves a modified equation with fixed \(a\) and then pulls back, the coefficient generally becomes transported incorrectly. If one tries to cancel \(a\mathcal L_Wg\) by using vector field \(aW\), extra \(da*W\) terms appear unless the gauged equation is formulated with the coefficient correctly included. Thus the Step 35 note does not recover the target equation.

### 2.2 The \(\varepsilon\)/Schauder argument does not give \(\varepsilon\)-independent smooth existence

The regularization
\[
a_\varepsilon=\chi^2+\varepsilon
\]
does produce a strictly parabolic gauged system for each fixed \(\varepsilon>0\). But the Step 35 claim that standard Schauder estimates give \(\varepsilon\)-independent \(C^{k,\alpha}\) bounds is unsupported. Standard parabolic Schauder constants depend on the ellipticity constant, hence typically on \(\varepsilon^{-1}\).

The proposed split into \(U_+=\{a>a_0\}\) and \(U_0=\{a<2a_0\}\) does not close the gap. On \(U_0\), the displayed estimate has a top derivative term of the form
\[
C(2a_0+\varepsilon)\|h\|_{H^{k+1}}^2
\]
on the wrong side for a closed \(H^k\) estimate, and the interface terms between \(U_+\) and \(U_0\) are not controlled. More basically, Yang’s \(\varepsilon\)-regularized route obtains uniformity from weighted curvature energy estimates, not from generic metric Schauder theory.

For the present first-exit argument, one only needs per-datum short-time smooth existence, not sequence-uniform \(\varepsilon\)-independent Schauder bounds. The reliable route is Yang’s transported-coefficient DeTurck construction, with the normalized lower-order term \(-2\widehat a\,\widehat g\) added. Since this term is zeroth order, it should not affect the principal parabolic/tame estimate mechanism. But the Step 35 existence note should be replaced by that transported-coefficient construction, not treated as a proof.

---

## 3. Cutoff-jet continuation note

The Step 35 cutoff-jet continuation note does not prove an extension criterion on \([0,T_{\max})\). It proves, at most, qualitative higher regularity for an already smooth solution on compact subintervals away from a terminal time.

The plateau part is essentially fine after shrinking to a smaller interior plateau where \(a=1\) on a full neighborhood. There the flow is ordinary normalized Ricci flow,
\[
\partial_t g=-2(\operatorname{Ric}+g),
\]
and a curvature bound of the form
\[
\|aF(t)\|_\infty\le C\gamma/t
\]
gives an ordinary curvature bound on the plateau. Shi-type estimates then give positive-time derivative bounds on a smaller plateau.

The transition-region argument is not an extension proof. It introduces coefficients such as
\[
\Lambda(t)
=
1+r^{-2}+\|T(t)\|_\infty
+\|a\nabla\operatorname{Rm}(t)\|_\infty^{2/(p-1)},
\qquad T=\operatorname{Rm}+G,
\]
and then declares them finite because the solution is smooth. This is circular for continuation. The zero-order bootstrap controls \(\|aF\|_\infty\), not unweighted \(\|T\|_\infty\), and it does not control \(a\nabla\operatorname{Rm}\). Near \(\chi=0\), \(U=aT\) can be bounded while \(T\) is not controlled pointwise by the bootstrap. Likewise, \(a\nabla\operatorname{Rm}\) is a first-derivative quantity whose control is part of the desired conclusion.

The correct extension mechanism is the shifted-curvature Wang induction from Step 27. One sets
\[
G=\frac{g\owedge g}{2(n-1)},\qquad
T=\operatorname{Rm}+G,\qquad
U=aT.
\]
Then
\[
\operatorname{Ric}(T)=\operatorname{Ric}+g=E,\qquad
\operatorname{Ric}(U)=aE,
\]
and \(\nabla^rT=\nabla^r\operatorname{Rm}\) for \(r\ge1\). The shifted evolution has the schematic form
\[
(\partial_t-a\Delta)T
=
da*\nabla T+\nabla^2a*T+a(T*T+G*T),
\]
and the \(U\)-equation contains no division by \(a\):
\[
(\partial_t-a\Delta)U
=
da*\nabla U+\nabla^2a*U+d\chi*d\chi*U+U*U+aG*U .
\]

After differentiating, the dangerous top cutoff term is
\[
\chi\,\nabla^{m+2}\chi*U.
\]
It must be integrated by parts once in the \(L^p\)-energy for
\[
W=\nabla^mU,
\]
so that the derivative falls on \(W\) and is absorbed by the weighted diffusion
\[
\int a|\nabla W|^2|W|^{p-2}.
\]
The factor \(\chi\) is exactly what matches \(a=\chi^2\). The remaining terms involve \(\nabla^{m+1}\chi\), which is coupled to \(\nabla^mU\) through the cutoff-jet evolution
\[
\partial_t\nabla^r\chi
=
\sum_{q=0}^{r-2}\nabla^q(\partial_t\Gamma)*\nabla^{r-1-q}\chi,
\qquad
\partial_t\Gamma=g^{-1}*\nabla(aE)
=g^{-1}*\nabla\operatorname{Ric}(U).
\]
This gives the triangular dependency
\[
\nabla^mU \longleftrightarrow \nabla^{m+1}\chi,
\]
with unweighted \(\nabla^mT\) controlled separately after the weighted step.

The two Step 27 notes differ in maturity: one presents this as a credible transfer mechanism still needing term-by-term completion; the other states it as a theorem. The safe corrected status is intermediate: the correct structural induction is identified, but a final proof still needs the detailed Wang-style staggered-exponent Hölder bookkeeping, including all \(G\)-terms \(\mathcal L_{G,m}\), without suppressing \(\chi\nabla^{m+2}\chi*U\) before the integration by parts.

Thus Step 35’s cutoff-jet note should not be used as the continuation theorem. The real continuation proof target is:

\[
\sup_{M\times[0,T)}|a\operatorname{Rm}|<\infty
\quad\Longrightarrow\quad
\sup_{M\times[0,T)}|\nabla^mU|<\infty\ \forall m,
\]
then smooth convergence of \(g(t)\) as \(t\uparrow T\), followed by restarted transported-coefficient DeTurck existence.

---

## 4. Terminal calibration and global \(Q=\int |E|^2\)

Terminal calibration still needs a separate global unweighted estimate for
\[
Q(t)=\int_M |E|^2\,d\mu_t.
\]
Neither \(J_6\) nor \(\|aE\|_\infty\) replaces it.

The calibration inequality used downstream has a global unweighted right-hand side:
\[
\int\left(|W^+|-\frac1{2\sqrt6}\right)^2
\le
\frac7{24}\int |E|^2 .
\]
But
\[
J_6=\int \eta^2a^4|E|^6
\]
is weighted by \(a^4\) and localized. It controls defect only where \(a\) is not small, and even there only after Hölder. It is blind to the transition/frozen exterior in the unweighted global sense.

Similarly,
\[
\|aE\|_\infty
\]
controls the velocity
\[
\partial_tg=-2aE
\]
and hence metric drift, but it gives no bound for \(|E|\) where \(a\) is small or zero.

The correct independent estimate is the global homogeneous \(Q\)-energy from Step 23:
\[
Q'(t)+c\int_M a|\nabla E|^2
\le
Cr^{-2}Q(t)
+
C\int_M aF|E|^2 .
\]
On each disjoint good support,
\[
\int_{U_j}\chi_j^2F|E|^2
=
\int_{U_j}F(\chi_jE)^2
\le
\|F\|_{2,U_j}\|\chi_jE\|_4^2
\]
and Sobolev gives
\[
\|\chi_jE\|_4^2
\le
C\mathcal S_j\left(
\int_{U_j}a|\nabla E|^2+r^{-2}\int_{U_j}|E|^2
\right).
\]
Thus, if the same small parameter
\[
\gamma_j=\mathcal S_j\|F\|_{2,U_j}
\]
is below threshold, the gradient term is absorbed and
\[
Q'(t)\le Cr^{-2}Q(t),
\qquad
Q(t)\le e^{Cr^{-2}t}Q(0).
\]
For \(t\le\theta r^2\),
\[
Q(t)\le e^{C\theta}Q(0).
\]
This estimate is logically separate from \(J_6\). The three defect controls have distinct roles:

\[
Q(t)\lesssim Q(0)
\quad\text{feeds terminal calibration;}
\]
\[
J_6(t)\lesssim J_6(0)
\quad\text{seeds defect Moser;}
\]
\[
\|aE(t)\|_\infty
\quad\text{controls metric drift and moving Sobolev constants.}
\]

The Step 35 assembly should keep these separate.

---

## Corrected proof targets

The handoff’s corrected analytic status is:

1. **\(J_6\) persistence:** valid and useful under explicit first-exit hypotheses, especially \(K_2\)-small \(\gamma\), moving Sobolev comparability, cutoff geometry, and smooth existence. It removes the need for a \(Y=K_3\) input in this one estimate.

2. **Existence:** Step 35’s fixed-coefficient DeTurck/\(\varepsilon\)-Schauder note is not a proof. Replace it with the transported-coefficient DeTurck construction:
   \[
   \widehat a=(\chi\circ\varphi_t^{-1})^2,
   \qquad
   \partial_t\widehat g
   =
   -2\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
   +\mathcal L_{\widehat aW}\widehat g,
   \]
   plus pullback to recover the fixed-cutoff equation.

3. **Continuation:** Step 35’s cutoff-jet note assumes smoothness and uses uncontrolled quantities \(\|T\|_\infty\), \(a\nabla\operatorname{Rm}\). The needed theorem is the Step 27 shifted-curvature Wang induction from \(\sup|a\operatorname{Rm}|<\infty\), with full treatment of the \(\chi\nabla^{m+2}\chi*U\) term and the \(G\)-monomials.

4. **Calibration:** retain and prove the separate global \(Q\)-estimate. Weighted \(J_6\) and weighted pointwise \(aE\) are insufficient for the unweighted global calibration inequality.