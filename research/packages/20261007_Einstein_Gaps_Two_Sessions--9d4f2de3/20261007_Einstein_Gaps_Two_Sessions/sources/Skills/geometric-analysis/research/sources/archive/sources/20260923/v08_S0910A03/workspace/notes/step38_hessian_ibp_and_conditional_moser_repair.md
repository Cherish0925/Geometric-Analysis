# Step 38: signed Hessian-cutoff repair and conditional K2--Y--Moser chain

Session: S0910A03. Agent3 / Actuator. Phase: Execute.

## 0. Purpose and current status

This note repairs the Step 37 continuation handoff without treating the downstream
interfaces as closed.  The Step 37 base-pair note still contains three erroneous
claims:

1. equations (3.9) and (3.11) estimate the terms
   \(I_{1c}\) and \(I_3\) as if their total power were \(p\), but in the raw
   absolute-value form they have total power \(p+1\):
   \[
   |I_{1c}|,|I_3|\lesssim\int \chi |\nabla^2\chi|\,|W|^p,
   \qquad W=\nabla U;
   \]
2. the displayed quotient \(\chi^2/a\) is not a pointwise expression on
   \(\{a=0\}\); the correct estimate uses \(|\chi|=\sqrt a\) and Young's
   inequality without division;
3. the asserted finite-
   \(L^p\)-to-\(L^\infty\) conclusion in §6 does not follow from finite
   \(L^p\) norms alone; pointwise continuation still needs a higher derivative
   induction.

TTCS Step 37 supplied a key repair: every single-\(\chi\) Hessian term with the
actual signed tensor structure
\[
   J=\int_M \chi\,\nabla_i\nabla_j\chi\,B^{ij}(V)\,d\mu
\tag{0.1}
\]
can be integrated once off the Hessian.  The strategist note correctly stresses
that this is stronger than the previous workaround using an evolving
\(\|\nabla^2\chi\|_4\) coefficient.  The point of this step is to apply that
repair to the real \(m=2\) shifted-curvature contractions and to keep the
K2--Y--Moser smoothing estimates conditional on a smooth first-exit interval.

Throughout
\[
   \partial_t g=-2aE,\qquad a=\chi^2,\qquad E=\operatorname{Ric}+g,
\]
\[
   G={g\owedge g\over2(n-1)},\qquad T=\operatorname{Rm}+G,
   \qquad U=aT,
\]
so \(\operatorname{Ric}(U)=aE\) and
\(\partial_tg=-2\operatorname{Ric}(U)\).  All continuation constants in this note
are per-datum unless explicitly labelled sequence-uniform.

## 1. The signed Hessian-cutoff lemma

Let \(V\) be a tensor and suppose a tested energy term has the signed form
\[
   J=\int_M \chi\,\nabla_i\nabla_j\chi\,B^{ij}(V)\,d\mu,
\tag{1.1}
\]
where, after the standard tensor-norm regularization if necessary,
\[
   |B(V)|\le C_p|V|^p,
   \qquad
   |\nabla B(V)|\le C_p|V|^{p-1}|\nabla V|.
\tag{1.2}
\]
Then on the closed manifold (or with the buffered stationary collar killing
boundary terms), integrating one derivative from \(\nabla^2\chi\) gives
\[
\begin{aligned}
J
&=-\int_M \nabla_i\chi\,\nabla_j\chi\,B^{ij}(V)\,d\mu
  -\int_M \chi\,\nabla_j\chi\,\nabla_iB^{ij}(V)\,d\mu .
\end{aligned}
\tag{1.3}
\]
Therefore
\[
\begin{aligned}
|J|
&\le C_p\|d\chi\|_\infty^2\int |V|^p
  +C_p\int |\chi|\,|d\chi|\,|V|^{p-1}|\nabla V|  \\
&\le \varepsilon\int \chi^2|\nabla V|^2|V|^{p-2}
  +C_{p,\varepsilon}\|d\chi\|_\infty^2\int |V|^p .
\end{aligned}
\tag{1.4}
\]
The last step uses
\[
 |\chi|\,|d\chi|\,|V|^{p-1}|\nabla V|
 = (|\chi||\nabla V||V|^{(p-2)/2})(|d\chi||V|^{p/2})
\tag{1.5}
\]
and Young.  No quotient by \(a\), no pointwise bound for \(\nabla^2\chi\), and
no \(\|\nabla^2\chi\|_4\) input is used.  The lemma applies only to the signed
contractions (1.1); it cannot be invoked after replacing the integrand by
\(\chi|\nabla^2\chi||V|^p\) and forgetting tensor placement.

## 2. Application to the actual \(m=2\) shifted-curvature contractions

Let
\[
   V=\nabla^2U,
   \qquad
   D_{2,p}=\int\chi^2|\nabla V|^2|V|^{p-2}.
\tag{2.1}
\]
In the differentiated \(U\)-equation, the high-cutoff line of Step 27/Codex has
schematic allocations
\[
 \sum_{\alpha+\beta+\gamma=4,\;\gamma\le3}
   \nabla^\alpha\chi*\nabla^\beta\chi*\nabla^\gamma U .
\tag{2.2}
\]
For \(m=2\), the terms containing \(V=\nabla^2U\) are, up to finite universal
contractions,
\[
   \chi\nabla^2\chi*V,
   \qquad
   \nabla\chi*\nabla\chi*V,
   \qquad
   \chi\nabla\chi*\nabla V .
\tag{2.3}
\]
Testing against \(|V|^{p-2}V\):

* The last term is directly absorbed:
  \[
  \left|\int |V|^{p-2}V*(\chi\nabla\chi*\nabla V)\right|
   \le \varepsilon D_{2,p}+C_{p,\varepsilon}\|d\chi\|_\infty^2\|V\|_p^p.
  \tag{2.4}
  \]
* The middle term contributes only
  \(C\|d\chi\|_\infty^2\|V\|_p^p\).
* The first term is exactly of the signed form (1.1): after expanding the
  universal contraction, each summand is
  \[
  \int\chi\,\nabla_i\nabla_j\chi\,B^{ij}(V)
  \tag{2.5}
  \]
  with \(B\) a metric contraction of \(|V|^{p-2}V\otimes V\). Hence
  \[
  \left|\int |V|^{p-2}V*(\chi\nabla^2\chi*V)\right|
   \le \varepsilon D_{2,p}+C_{p,\varepsilon}\|d\chi\|_\infty^2\|V\|_p^p.
  \tag{2.6}
  \]

Thus the previously isolated term
\(\int\chi|\nabla^2\chi||\nabla^2U|^p\) is not intrinsically an obstruction at
\(m=2\).  It was created by taking absolute values before using the available
signed Hessian contraction.  The earlier Step 32/A01 estimate through
\(\|\nabla^2\chi\|_4\) remains a fallback for unsigned remnants, but it is not
needed for the genuine \(\chi\nabla^2\chi*V\) line.

## 3. What remains hard in the higher-order continuation induction

The same lemma treats any term that can be written as
\(\int\chi\nabla^2\chi\,B(\nabla^mU)\).  It does **not** finish the shifted
extension theorem.

For general \(m\), the top line contains
\[
   \Gamma_1=\chi\nabla^{m+2}\chi*U,
   \quad
   \Gamma_2=\nabla\chi*\nabla^{m+1}\chi*U,
   \quad
   \Gamma_3=\chi\nabla^{m+1}\chi*\nabla U,
   \quad
   \Gamma_4=\chi\nabla\chi*\nabla^{m+1}U.
\tag{3.1}
\]
\(\Gamma_4\) is paid by diffusion as in (2.4).  Integrating \(\Gamma_1\) once
leaves current cutoff jet \(\nabla^{m+1}\chi\) coupled to the current energy
\(\nabla^mU\); that is a same-level pair with the cutoff equation, not an
absolute Hessian obstruction.  The truly delicate terms are those in which the
highest cutoff jet is coupled to differentiated lower-order curvature factors,
for example descendants of
\[
   \chi\nabla^{m+1}\chi*\nabla U*|\nabla^mU|^{p-2}\nabla^mU
\tag{3.2}
\]
after integration by parts.  If the derivative falls on \(\nabla U\), one obtains
\(\nabla^m\chi*\nabla^2U\) multiplying the current power; if it falls on metric
contractions or commutators, unweighted lower \(T\)-derivatives may appear.  These
terms require a finite-exponent induction schedule for previous \(U\), \(T\), and
cutoff-jet levels.  They should not be merged with the single-Hessian term
\(\chi\nabla^2\chi*\nabla^mU\), which is already controlled by (1.4).

The current safe continuation statement is therefore:

> On a smooth interval where \(\sup |U|\), metric comparison, Sobolev constants,
> and finite unweighted \(T\)-moments are available, the Step 37 finite-
> \(L^p\) base estimate for \((\nabla U,\nabla^2\chi)\) is repaired by the signed
> Hessian lemma.  At \(m=2\), the apparent single-\(\chi\) Hessian term is also
> repaired by the same lemma.  A full extension theorem still requires a
> written induction controlling top cutoff jets coupled to differentiated
> lower-order curvature factors, and Step 27 cannot be cited as already proving
> that induction.

## 4. Conditional K2--Y fixed-exponent layer

Now return to the smoothing estimates.  Everything below is conditional on a
smooth first-exit interval with fixed macro-disjoint buffered supports,
\(a=\sum_j\chi_j^2\), moving Sobolev comparison, and
\[\gamma_j(t)=\mathcal S_j(t)K_{2,j}(t)^{1/2}\le\gamma_0\ll1.\]
Here \(K_{2,j}=\int_{U_j}\eta_j^2F^2\),
\(F=(1+|\operatorname{Rm}|^2)^{1/2}\), and
\(Y_j=\int_{U_j}\eta_j^2aF^3\).

A01 Step 35 supplies the index-level Hessian-a tensor for the curvature power
inequality:
\[
 B_{\rm curv}^{pq}=R^p{}_j{}^q{}_l E^{jl},
 \qquad |B_{\rm curv}|\le CF^2,
 \qquad |\nabla B_{\rm curv}|\le CF|\nabla\operatorname{Rm}|.
\tag{4.1}
\]
Signed integration by parts gives, for \(p\ge3\),
\[
K_p'+c\{pD_p^{\operatorname{Rm}}+p(p-2)D_p^F\}
\le Cp^N(r^{-2}+1+\mathcal S^2Y)K_p .
\tag{4.2}
\]
At \(p=2\) the same tensor mechanism yields
\[
K_2'+cD_2\le CY+Cr^{-2}K_2.
\tag{4.3}
\]
The matched Sobolev estimate for \(v=\chi F\) is
\[
Y=\int Fv^2
\le \|F\|_2\|v\|_4^2
\le C\gamma(D_2+r^{-2}K_2).
\tag{4.4}
\]
For \(C\gamma<c/2\), (4.3) gives
\[
\sup_{s\le t}K_2(s)+\int_0^tD_2(s)\,ds\le CK_2(0),
\qquad
\int_0^tY(s)\,ds\le C\gamma K_2(0).
\tag{4.5}
\]

The fixed \(q=3\) equation is
\[
Y'+cD_3\le Cr^{-2}Y+C\int a^2F^4,
\tag{4.6}
\]
and with \(u=aF^{3/2}\),
\[
\int a^2F^4=\int Fu^2
\le C\gamma(D_3+r^{-2}Y).
\tag{4.7}
\]
After absorption,
\[
Y'\le Cr^{-2}Y.
\tag{4.8}
\]
Combining (4.5) with a good slice in \([t/4,t/2]\) and propagating by (4.8),
\[
Y(t)\le {C\gamma K_2(0)\over t},
\qquad
\mathcal S^2Y(t)\le {C\gamma^3\over t}.
\tag{4.9}
\]
This is the dyadic coefficient input for the high-exponent Moser iteration.  It
is not a time-zero pointwise curvature bound.

## 5. Conditional high-exponent Moser outputs

For either \(f=F\) or \(f=|E|\), define
\[
H_p(f)=\int\eta^2a^{p-2}f^p,
\qquad
z_p=\eta a^{(p-1)/2}f^{p/2}.
\tag{5.1}
\]
Assume the corresponding tensor power inequality
\[
H_p'(f)+c\|\nabla z_p\|_2^2
\le Cp^N(r^{-2}+1+\mathcal S^2Y)H_p(f)
\tag{5.2}
\]
(with no curvature-only source in the defect case).  On a dyadic slab
\([t/2,t]\), (4.9) bounds the coefficient by
\(Cp^N4^k(t^{-1}+r^{-2})\) at the \(k\)-th time cutoff.  The exact mixed
interpolation is
\[
H_{3p/2}\le H_p^{1/2}\|z_p\|_4^2,
\tag{5.3}
\]
with weight identity
\((p-2)/2+(p-1)=3p/2-2\).  The standard time-cutoff recurrence gives
\[
\boxed{
\|af(t)\|_\infty
\le C\mathcal S^{2/p_0}t^{-3/p_0}
      \left(\int_{t/2}^{t}H_{p_0}(f,s)\,ds\right)^{1/p_0}.}
\tag{5.4}
\]
The product converges because \(p_k=p_0(3/2)^k\) grows geometrically while all
losses are polynomial in \(p_k\) and dyadic in \(4^k\).

For curvature, \(p_0=3\) and (4.5) gives
\[
\int_{t/2}^tY(s)\,ds\le C\gamma K_2(0).
\]
Using \(\gamma=\mathcal S K_2(0)^{1/2}\),
\[
\boxed{\|aF(t)\|_\infty\le C\gamma/t.}
\tag{5.5}
\]

For the defect, Step 35 gives the unregularized fixed seed
\[
J_6(t)=\int\eta^2a^4|E|^6\le C\delta^6V,
\tag{5.6}
\]
under the same smooth first-exit and \(\gamma\)-small hypotheses.  Then (5.4)
with \(p_0=6\) and \(\mathcal S\simeq r^2V^{-1/2}\) yields
\[
\boxed{\|aE(t)\|_\infty
\le C\delta(r^2/t)^{1/3}.}
\tag{5.7}
\]
Consequently
\[
\int_0^{\theta r^2}\|aE(t)\|_\infty\,dt
\le C\delta\theta^{2/3}r^2,
\tag{5.8}
\]
which is the support-wide metric-drift estimate needed to keep the moving
Sobolev and support geometry within the first-exit assumptions.

## 6. Scientific meaning for the Yau 26 route

The useful research asset is not a completed Ishida--LeBrun gap proof.  The
asset is a conditional collapse-uniform smoothing mechanism:

\[
K_2 \Rightarrow Y \Rightarrow \|aF\|_\infty,
\qquad
K_2 \Rightarrow J_6,Q \Rightarrow \|aE\|_\infty
\Rightarrow \text{metric/Sobolev persistence},
\]
with all Sobolev-volume factors canceling on matched supports.  This mechanism
preserves the global defect \(Q\) for terminal calibration while producing
bounded-curvature positive-volume plateaux, if the smooth first-exit flow exists
and extends to the selected time.

The remaining mathematical work is now better separated:

1. prove the higher shifted-curvature continuation induction, not merely the
   finite-\(L^p\) base estimate; use the signed Hessian lemma for the
   single-Hessian current terms and isolate the top-jet/lower-curvature couplings;
2. keep the K2--Y--Moser estimates conditional on a smooth first-exit interval
   until (1) and the transported-coefficient existence theorem are fully secured;
3. consolidate the terminal geometric passage only after the smoothing principle
   is a theorem.

Even completion of this smoothing principle would still address only the
restricted four-dimensional negative Ishida--LeBrun laboratory.  The full Yau
Problem 26 statement still requires a proof or counterexample for arbitrary
closed smooth manifolds in every dimension, including the positive branch,
\(n\ge5\), dimension-only constants, and ultimately Lean formalization.
