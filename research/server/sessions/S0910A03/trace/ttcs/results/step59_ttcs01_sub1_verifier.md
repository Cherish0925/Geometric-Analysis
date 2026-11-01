# TTCS Independent Branch Record

```json
{
  "step_id": 59,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step59_finite_regularity_continuation_and_common_time.md",
    "Sessions/S0910A03/workspace/notes/step40_staggered_all_order_continuation_candidate.md",
    "Sessions/S0910A01/workspace/notes/step55_finite_restart_threshold_and_C3_exchange.md",
    "Sessions/S0910A03/workspace/notes/step56_positive_time_base_pair.md",
    "Sessions/S0910A03/workspace/notes/step58_critical_to_subcritical_bridge.md"
  ]
}
```

## Task

Verify the finite-regularity continuation bridge in step59_finite_regularity_continuation_and_common_time.md. The theorem claims: on the exact normalized cutoff flow ∂_tg = -2χ²(Ric+g) on a closed 4-manifold, if the first-exit curvature estimate ||aF_T(t)||_∞ ≤ CΓ/t holds on (0,T*) with T* < ∞, then the flow extends smoothly past T*.

The argument chain is:
(A) W^{1,p} bridge (Kato + Sobolev for p>4) gives |T|_∞ bounded on [τ,T*].
(B) Staggered induction through (U_m, C_{m+1}) for m=2,...,7 and T_m for m=2,...,6, using: (i) IBP of χC_{m+2}*U to lower cutoff jet; (ii) Hölder-Sobolev for the residual χC_{m+1}*U_1 using U_1 ∈ L^4 and current degenerate diffusion; (iii) signed-Hessian for χC_2*U_m; (iv) honest expansion of ∇^r a without false χ factors.
(C) Fixed-background conversion: A = ∇^{g(t)} - ∇^{g(τ)} satisfies a triangular ODE requiring U_1,...,U_7, giving g(t) ∈ H^7.
(D) Restart via Step 56 Theorem 4.3.

Verify specifically:
1. Is the general m induction pattern (Step 40 / A01 Step 55) structurally sound? Does the residual at every level m ≥ 2 genuinely use only U_1 (not U_j with j > 1) in the Hölder-Sobolev step?
2. Is the fixed-background conversion from current-pair L^p bounds to H^{s_0} correct? Does ∂_t(bar-nabla^m A) = g^{-1}*U_{m+1} + lower really hold?
3. Does the common observation time argument correctly separate sequence-uniform first-exit inputs from per-datum continuation inputs?
4. Are there any hidden terms at general level m that would defeat the pattern?

## Output

## Scientific memo: verification of Step 59 continuation bridge

I read Step 59 together with Step 40, A01 Step 55, Step 56 positive-time base pair, and Step 58. The finite-regularity bridge is structurally coherent at the schematic tensor level supplied in those notes. The mechanism is the coupled collar induction for \((U_m,C_{m+1})\), not ordinary Shi estimates. The main remaining mathematical load is the proof-level expansion of the general \(m\) evolution equations and the exact restart theorem used at the terminal time.

### 1. General \(m\) staggered induction

The Step 59 pattern for
\[
U_m=\nabla^mU,\qquad C_j=\nabla^j\chi,\qquad U=aT,\quad a=\chi^2
\]
is consistent with Step 40 and A01 Step 55.

The key derivative-counting fact is:

\[
\partial_tU_m
=\operatorname{div}(a\nabla U_m)
+\chi C_{m+2}*U
+\chi C_{m+1}*U_1
+\chi C_2*U_m
+C_1*C_1*U_m
+\mathcal P_m .
\]

The top cutoff jet \(C_{m+2}\) can only occur with \(U_0=U\). After one integration by parts,

\[
\int P(U_m)*\chi C_{m+2}*U
\]
produces three relevant terms:

\[
-\int \nabla P(U_m)*\chi C_{m+1}*U,
\]
\[
-\int P(U_m)*C_1*C_{m+1}*U,
\]
\[
-\int P(U_m)*\chi C_{m+1}*U_1.
\]

Thus the residual current-cutoff term genuinely contains \(U_1\), not \(U_j\) with \(j>1\). Terms with \(U_j\), \(j\ge2\), necessarily have cutoff jet order at most \(m\), hence use already available cutoff levels, except for the current \(U_m\) terms with total cutoff order two:
\[
\chi C_2*U_m,\qquad C_1*C_1*U_m.
\]

The residual estimate in Step 59 is valid in dimension four. With
\[
f=\chi |U_m|^{p/2},
\]
one has
\[
\int \chi |C_{m+1}|\,|U_1|\,|U_m|^{p-1}
\le
\|f\|_4\,\|C_{m+1}\|_p\,\|U_1\|_4\,\|U_m\|_p^{p/2-1},
\]
using Hölder exponents
\[
4,\quad p,\quad 4,\quad \frac{2p}{p-2}.
\]
The weighted Sobolev estimate
\[
\|f\|_4^2
\le C\bigl(p^2D_{m,p}^U+C_{p,r}\|U_m\|_p^p\bigr)
\]
then gives
\[
I_{\rm res}
\le \varepsilon D_{m,p}^U
+C_{m,p,\tau}\bigl(1+\|C_{m+1}\|_p^p+\|U_m\|_p^p\bigr).
\]
This avoids any need for \(C_{m+1}\in L^{2p}\). The same calculation applies to the direct \(\chi C_{m+1}*U_1\) term.

The current signed-Hessian term
\[
\chi C_2*U_m
\]
is also correctly separated from bounded-coefficient terms. Since \(C_2\) is only known in finite \(L^q\) spaces, treating it as \(L^\infty\) would be invalid. The integration-by-parts lemma gives
\[
\left|\int \chi(C_2)_{ij}B^{ij}(U_m)\right|
\le
\varepsilon D_{m,p}^U
+C_{p,\varepsilon}\|C_1\|_\infty^2\|U_m\|_p^p,
\]
provided
\[
|B(U_m)|\lesssim |U_m|^p,\qquad
|\nabla B(U_m)|\lesssim |U_m|^{p-1}|\nabla U_m|.
\]
This is the right structural use of \(a=\chi^2\).

For the unweighted curvature stage \(T_m\), the same derivative count works after \(|T|_\infty\) has been obtained. The top cutoff term
\[
\nabla^{m+2}a*T
=
2\chi C_{m+2}*T
+\sum_{s=1}^{m+1}C_s*C_{m+2-s}*T
\]
has only one term above the available cutoff level. Integrating
\[
\int |T_m|^{p-2}T_m*\chi C_{m+2}*T
\]
once leaves the residual
\[
\int \chi |C_{m+1}|\,|T_1|\,|T_m|^{p-1},
\]
which is controlled exactly as above, with \(T_1\in L^4\).

So, for the supplied schematic equations, the triangular induction
\[
T_0\to(U_1,C_2)\to T_1
\to(U_2,C_3)\to T_2
\to\cdots
\to(U_7,C_8)\to T_6
\]
is mathematically consistent.

The one item not supplied in full proof form is the complete tensor expansion of the general \(m\) equations. The decisive hidden-term test is whether every occurrence of \(U_{m+1}\) or \(T_{m+1}\) is contained in \(\operatorname{div}(a\nabla U_m)\) or \(\operatorname{div}(a\nabla T_m)\), and whether every occurrence of \(C_{m+2}\) is exactly of the form \(\chi C_{m+2}*U\) or \(\chi C_{m+2}*T\). Step 40 states this structure; Step 59 relies on it.

### 2. \(W^{1,p}\to L^\infty\) curvature bridge

Step 59’s part (A) is sound.

On any positive slab \([\tau,T^*)\), the curvature endpoint gives
\[
\|U(t)\|_\infty=\|aT(t)\|_\infty\le \frac{C\Gamma}{\tau}=K_\tau.
\]
This yields uniform bilipschitz comparison of \(g(t)\) with \(g(\tau)\) on that slab.

The Step 56 base block supplies
\[
T,\quad \nabla T,\quad \nabla U,\quad \nabla^2\chi
\in L_t^\infty L_x^q
\qquad\forall q<\infty.
\]
For \(p>4\), Kato plus the scalar Sobolev inequality gives
\[
\|T(t)\|_\infty
\le C\bigl(\|T(t)\|_p+\|\nabla T(t)\|_p\bigr).
\]
The Sobolev constant here is per datum and per positive slab, coming from the metric \(g(\tau)\) and bilipschitz comparison. It is not used in the sequence-uniform first-exit estimates. Therefore
\[
|\operatorname{Rm}(t)|\le |T(t)|+|G(t)|\le C_\tau
\]
on \([\tau,T^*)\).

This is enough to make all zero-order curvature coefficients harmless in the later finite induction.

### 3. Fixed-background conversion

The fixed-background conversion is essentially correct.

Let
\[
\bar\nabla=\nabla^{g(\tau)},\qquad A=\nabla^{g(t)}-\bar\nabla.
\]
The connection variation formula gives
\[
\partial_t A=\partial_t\Gamma(g)
=
g^{-1}*\nabla^g(aE)
=
g^{-1}*U_1.
\]
If one first writes \(\bar\nabla(aE)\), then extra \(A*U\) terms appear; these are lower in the triangular system and have bounded \(U\)-coefficient.

Applying \(\bar\nabla^m\) gives
\[
\bar\nabla^m\partial_t A
=
g^{-1}*U_{m+1}
+
P_m(A,\ldots,\bar\nabla^{m-1}A;\,U_0,\ldots,U_m;\,g^{-1}).
\]
The top derivative \(A_m=\bar\nabla^mA\) does not appear if the formula is written using the \(g(t)\)-covariant derivative before converting to \(\bar\nabla\). The reason is:

\[
\bar\nabla^m U_1
=
\nabla^m U_1
+
\text{terms involving }A_0,\ldots,A_{m-1}
\text{ and }U_1,\ldots,U_m,
\]
and
\[
\nabla^mU_1=U_{m+1}.
\]
Also, \(\bar\nabla^m g^{-1}\) involves only \(A_0,\ldots,A_{m-1}\).

Thus \(A_m\) satisfies an ODE-type estimate driven by \(U_{m+1}\) and already controlled lower quantities. Running the estimate for every finite \(p\) gives
\[
A_m\in L_t^\infty L_x^p,
\qquad 0\le m\le 6,\quad p<\infty,
\]
provided
\[
U_1,\ldots,U_7
\]
are controlled in all finite \(L^p\) spaces.

Then
\[
\bar\nabla g=A*g,
\]
and recursively
\[
\bar\nabla^{m+1}g
=
(\bar\nabla^mA)*g+\text{products of lower }A_j.
\]
Because the \(A_j\) are available in all finite \(L^p\) spaces and \(g(t)\) is bilipschitz to \(g(\tau)\), the product terms lie in \(L^2\). Hence
\[
g(t)\in H^7(M,g(\tau))
\]
uniformly on \([\tau,T^*)\).

One technical point in Step 59’s restart paragraph should be stated more sharply. From the displayed estimates one obtains an \(H^7\) terminal metric and \(H^5\)-Lipschitz time convergence:
\[
\|\partial_tg\|_{H^5}\lesssim 1.
\]
If Step 56 Theorem 4.3 is a strong \(H^7\) local well-posedness theorem with uniqueness and smoothing for positive time, then restarting from \(g(T^*)\in H^7\) is valid in the strong class. If the desired extension is required to be smooth at \(t=T^*\) itself, the cleaner formulation is to restart at times \(t_j<T^*\) using the uniform \(H^7\) radius; the initial data \(g(t_j)\) are smooth, and the Step 56 lifespan depends only on the \(H^7\) control and ellipticity, so for \(j\) large the new interval crosses \(T^*\). That gives a classical smooth continuation past \(T^*\).

### 4. Sequence-uniform inputs versus per-datum continuation inputs

Step 59 separates these correctly.

The sequence-uniform first-exit chain uses only quantities such as
\[
n=4,\quad r,\quad \|d\chi\|_\infty,\quad H_i(0),\quad \mathcal S_i(0),
\quad \gamma_i(0)=\mathcal S_i(0)H_i(0)^{1/2},
\quad \delta_i,
\quad Q_i(0),\quad J_{6,i}(0).
\]
It does not use:

\[
Y_i(0),\qquad
\text{high Sobolev norms of }g_i,\qquad
\|\nabla^k\chi\|,\ k\ge2,
\]
nor the Sobolev constant of \(g_i(\tau)\) on a positive slab.

The continuation bridge uses per-datum quantities after choosing
\[
\tau\in(0,T_i^*),
\]
for instance \(K_\tau=C\Gamma/\tau\), the Sobolev constant of \(g_i(\tau)\), and finite positive-time \(L^p\) norms. These constants may blow up along the sequence or as \(\tau\downarrow0\); that does not affect the common observation time, because they are only used to rule out a finite maximal time before \(\theta r^2\) for each fixed datum.

So the logic

\[
T_i^*<\theta r^2
\quad\Rightarrow\quad
\text{positive-slab continuation applies}
\quad\Rightarrow\quad
\text{extension past }T_i^*
\]
does not feed per-datum constants back into the first-exit estimates determining \(\theta r^2\).

### 5. Hidden-term assessment

No hidden term is visible in the supplied schematic structure that defeats the pattern. The relevant classes behave as follows.

- Terms with \(U_{m+1}\) or \(T_{m+1}\) are part of the divergence operator \(\operatorname{div}(a\nabla U_m)\) or \(\operatorname{div}(a\nabla T_m)\), not separate drift terms.

- Terms with \(C_{m+2}\) occur only as \(\chi C_{m+2}*U\) or \(\chi C_{m+2}*T\). One integration by parts lowers them to \(C_{m+1}\) and produces only \(U_1\) or \(T_1\) in the Sobolev residual.

- Current \(U_m\) or \(T_m\) terms with two cutoff derivatives are exactly of signed-Hessian type \(\chi C_2*\text{current}\) plus bounded \(C_1*C_1*\text{current}\).

- Quadratic curvature terms with a current derivative carry a bounded coefficient:
\[
aT=U.
\]

- Connection-variation terms in the \(U_m\) and \(C_{m+1}\) equations contain either current \(U_m\) with bounded \(C_1\) or previously controlled levels.

- Full expansion of
\[
\nabla^ra=\sum_{s=0}^r C_s*C_{r-s}
\]
is essential. The non-\(\chi\) terms have split cutoff derivatives and are controlled by already available finite-exponent cutoff levels; inserting an artificial \(\chi\) would change the analytic content.

The supplied Step 40 and A01 Step 55 notes give the correct derivative-counting architecture. A fully independent proof would still need the explicit term-by-term tensor expansion for general \(m\), especially for the commutators
\[
[\nabla^m,\operatorname{div}(a\nabla)]U,\qquad
[\nabla^m,\operatorname{div}(a\nabla)]T,\qquad
[\partial_t,\nabla^m],
\]
and for all terms generated by differentiating \(G\) and the normalization. Based on the displayed structures, these terms fall into the controlled classes above.