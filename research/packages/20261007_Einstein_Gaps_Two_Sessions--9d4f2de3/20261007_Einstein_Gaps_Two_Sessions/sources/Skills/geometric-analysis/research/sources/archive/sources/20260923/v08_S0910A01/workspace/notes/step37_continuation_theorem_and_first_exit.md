# Step 38 superseding correction

Step 37's conclusion that the shifted continuation theorem and the flow platform were closed is withdrawn.  The argument inserted as Lemma 1.2a is false in the cutoff-degenerate region: from \(|U|=|\chi^2(\operatorname{Rm}+G)|\le K\) one obtains \(|aE|=|\operatorname{Ric}(U)|\le C K\), not an extra \(\chi^2K\) factor, and small metric drift would not control higher curvature derivatives.  The continuation theorem below is therefore retained only as a record of a failed attempt and of useful zero-order estimates.  Use `workspace/notes/step38_continuation_repair_and_support_normalization.md` for the current repair route.

---

# Step 37: Continuation theorem and first-exit closure

Session: S0910A01. Agent2 / Constructor. Phase: Execute.

## 0. Purpose

This note constructs the two remaining analytical pieces that close the
degenerate cutoff-flow platform:

1. **Shifted continuation theorem**: if \(\sup|U|<\infty\) on a positive-time
   slab, the solution extends.
2. **First-exit closure**: the continuation theorem combines with the conditional
   Moser endpoints and first-exit self-improvement to prove that the flow exists
   on \([0,\theta r^2]\), completing the smoothing principle.

Throughout, \(\dim M=4\),
\[
  \partial_tg=-2aE,\qquad a=\chi^2,\qquad E=\operatorname{Ric}+g,
\tag{0.1}
\]
\[
  G=\frac{g\owedge g}{6},\qquad T=\operatorname{Rm}+G,
  \qquad U=aT=\chi^2(\operatorname{Rm}+G),
\tag{0.2}
\]
so \(\operatorname{Ric}(U)=aE\) and \(\partial_tg=-2\operatorname{Ric}(U)\).

The signed Hessian-cutoff lemma (A03 Step 38, §1) is used throughout:
for any signed integral of the form
\[
  J=\int_M\chi\,\nabla_i\nabla_j\chi\,B^{ij}(V),
  \qquad |B|\le C_p|V|^p,\quad |\nabla B|\le C_p|V|^{p-1}|\nabla V|,
\tag{0.3}
\]
one integration by parts gives
\[
  |J|\le\varepsilon\int a|\nabla V|^2|V|^{p-2}
       +C_{p,\varepsilon}\|d\chi\|_\infty^2\int|V|^p.
\tag{0.4}
\]

**Source model**: Wang, *Pseudolocality of Ricci Flow under Integral Bound of
Curvature*, Theorem 4.1, Lemmas 4.4–4.6, 4.10 (Knowledge object
`Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9`).

---

## 1. Shifted continuation theorem

**Theorem 1.1 (continuation).**
Let \((M^4,g(t))\), \(t\in[0,T_{\max})\), be a smooth solution of (0.1) on a
closed Riemannian four-manifold, with \(\chi\in C_0^\infty(M)\) fixed and
\(T_{\max}<\infty\).  If
\[
  K(\tau)\;:=\;\sup_{M\times[\tau,T_{\max})}|U|<\infty
\tag{1.1}
\]
for some \(\tau\in(0,T_{\max})\), then the solution extends smoothly past
\(T_{\max}\).

### 1.1 Step A: metric equivalence

For any tangent vector \(v\ne0\) and \(t\in[\tau,T_{\max})\):
\[
  \left|{d\over dt}\log g_t(v,v)\right|
  ={2|aE(v,v)|\over g_t(v,v)}
  \le CK(\tau).
\tag{1.2}
\]
Therefore
\[
  e^{-CK(T_{\max}-\tau)}g(\tau)\le g(t)\le e^{CK(T_{\max}-\tau)}g(\tau).
\tag{1.2a}
\]
Thus \(g(t)\) and \(g(\tau)\) are uniformly bilipschitz on \([\tau,T_{\max})\).
In particular, \(|d\chi|_{g(t)}\), Sobolev constants, and volumes are uniformly
controlled.

### 1.2 Step B: unweighted \(L^p\) curvature propagation

**Lemma 1.2** (adapted from Wang Lemma 4.10).  Under the hypotheses of
Theorem 1.1, for every \(p\ge 2\):
\[
  \|\operatorname{Rm}(t)\|_{L^p}\le C(p,K,\chi,\tau,g(\tau))
  \qquad\forall\,t\in[\tau,T_{\max}).
\tag{1.3}
\]

*Proof.*
The evolution of the all-lower Riemann tensor under \(h=-2aE\) was derived in
Step 35.  Schematically:
\[
  (\partial_t-a\Delta)\operatorname{Rm}
  =a(\operatorname{Rm}*\operatorname{Rm}+\operatorname{Rm})
   +\nabla a*\nabla\operatorname{Rm}
   +\nabla^2a*\operatorname{Rm}*E
   +a\operatorname{Rm}.
\tag{1.4}
\]
The last term comes from the normalization \(-2ag\); the next-to-last from the
Hessian-\(a\) contraction.  Testing against
\(|\operatorname{Rm}|^{p-2}\operatorname{Rm}\):

**Diffusion.**
\[
  \int\operatorname{Rm}*a\Delta\operatorname{Rm}\cdot|\operatorname{Rm}|^{p-2}
  \le -cp\int a|\nabla\operatorname{Rm}|^2|\operatorname{Rm}|^{p-2}.
\tag{1.5}
\]
This is the degenerate diffusion; it vanishes where \(a=0\).

**Reaction.**
\[
  \left|\int a|\operatorname{Rm}|^{p+1}\right|
  =\left|\int(a|\operatorname{Rm}|)|\operatorname{Rm}|^p\right|
  \le(K+C)\int|\operatorname{Rm}|^p,
\tag{1.6}
\]
using \(|a\operatorname{Rm}|\le|U|+|aG|\le K+C\).

**Gradient of \(a\).**
\[
  \left|\int|da||\nabla\operatorname{Rm}||\operatorname{Rm}|^{p-1}\right|
  \le\varepsilon\int a|\nabla\operatorname{Rm}|^2|\operatorname{Rm}|^{p-2}
     +C_\varepsilon r^{-2}\int|\operatorname{Rm}|^p,
\tag{1.7}
\]
by Young, using \(|da|^2/a=4|d\chi|^2\le Cr^{-2}\).

**Hessian of \(a\).**
Split \(E=\operatorname{Ric}+g\).  The Step 35 variation formula gives
Hessian-\(a\) contributions of the schematic form
\(\nabla^2a*\operatorname{Ric}*|\operatorname{Rm}|^{p-2}\operatorname{Rm}\)
and \(\nabla^2a*g*|\operatorname{Rm}|^{p-2}\operatorname{Rm}\).  For the Ricci
part, the signed contraction tensor is
\[
  B_{\mathrm{Ric}}^{ij}=\text{(metric contraction of }
    |\operatorname{Rm}|^{p-2}\operatorname{Rm}\otimes\operatorname{Ric}),
\]
with \(|B_{\mathrm{Ric}}|\le C|\operatorname{Rm}|^p\),
\(|\nabla B_{\mathrm{Ric}}|\le C|\operatorname{Rm}|^{p-1}|\nabla\operatorname{Rm}|\).
For the \(g\)-part,
\[
  B_g^{ij}=\text{(metric contraction of }
    |\operatorname{Rm}|^{p-2}\operatorname{Rm}\otimes g),
\]
with \(|B_g|\le C|\operatorname{Rm}|^{p-1}\),
\(|\nabla B_g|\le C|\operatorname{Rm}|^{p-2}|\nabla\operatorname{Rm}|\).
Both are of the signed form (0.3) with \(V=\operatorname{Rm}\), and by (0.4)
each gives
\[
  \varepsilon\int a|\nabla\operatorname{Rm}|^2|\operatorname{Rm}|^{p-2}
  +C_{p,\varepsilon}r^{-2}\int(1+|\operatorname{Rm}|^p).
\tag{1.8}
\]
The \(|\operatorname{Rm}|^{p-1}\) factors from \(B_g\) produce
\(|\operatorname{Rm}|^{p-1}\) under IBP, which by Young is
\(\le\varepsilon|\operatorname{Rm}|^p+C_\varepsilon\).  Near
\(\operatorname{Rm}=0\), the Kato regularization
\((|\operatorname{Rm}|^2+\epsilon)^{1/2}\) can be used; the limit
\(\epsilon\to0\) is standard.

**Volume.**
\[
  \left|\int|\operatorname{Rm}|^p\operatorname{tr}(aE)\right|
  \le CK\int|\operatorname{Rm}|^p.
\tag{1.9}
\]

Combining (1.5)–(1.9) with \(\varepsilon\) chosen to absorb diffusion:
\[
  \boxed{
  {d\over dt}\int|\operatorname{Rm}|^p
  \le C_p(K+1+r^{-2})\int|\operatorname{Rm}|^p+C_p.}
\tag{1.10}
\]
Gronwall on \([\tau,T_{\max})\) gives (1.3).  Since \(|G|\le C\) and
\(\nabla G=0\), \(\|T(t)\|_p\) is also bounded. \(\square\)

### 1.2a Step B′: unweighted derivative recovery (Wang Prop 4.13 analog)

The staggered induction requires unweighted \(\|\nabla^k\operatorname{Rm}\|_p\)
at each level.  Once \(\|\nabla^k U\|_p\) is bounded (from the induction),
unweighted control follows by a splitting argument.

**Lemma 1.2a.**  If \(\|\nabla^kU(t)\|_p\), all cutoff jets
\(\|\nabla^j\chi\|_\infty\) for \(j\le k+2\), and metric comparison are bounded
on \([\tau,T_{\max})\), then \(\|\nabla^k\operatorname{Rm}(t)\|_p\) is bounded
on the same interval (with per-datum constants).

*Proof.*
Split \(M=\{\chi\ge\delta\}\cup\{\chi<\delta\}\) for a small fixed \(\delta>0\).

*On \(\{\chi\ge\delta\}\)*:
the Leibniz formula gives
\[
  \chi^2\nabla^k\operatorname{Rm}
  =\nabla^k(\chi^2\operatorname{Rm})
   -\sum_{j=1}^k\binom{k}{j}\nabla^j(\chi^2)*\nabla^{k-j}\operatorname{Rm} .
\]
Since \(U=\chi^2(\operatorname{Rm}+G)\) and \(\nabla^j G=0\) for \(j\ge1\),
\(\nabla^k(\chi^2\operatorname{Rm})=\nabla^kU-\nabla^k(\chi^2G)\).  All
\(\nabla^j(\chi^2)\) are bounded cutoff jets.  Therefore
\[
  |\nabla^k\operatorname{Rm}|
  \le{1\over\delta^2}\bigl(|\nabla^kU|+C\sum_{j=0}^{k-1}|\nabla^j\operatorname{Rm}|+C\bigr)
  \qquad\text{on }\{\chi\ge\delta\},
\]
and by the induction hypothesis \(\|\nabla^kU\|_p\) and lower
\(\|\nabla^j\operatorname{Rm}\|_p\) are bounded.

*On \(\{\chi<\delta\}\)*:
the metric drift from \(g(\tau)\) is bounded by
\[
  |g(t)-g(\tau)|
  \le 2\int_\tau^t|aE|\,ds
  \le 2\chi^2 K(T_{\max}-\tau)
  \le 2\delta^2 K(T_{\max}-\tau).
\]
For \(\delta\) small enough, the metric on \(\{\chi<\delta\}\) is
\(C^k\)-close to \(g(\tau)\), so
\[
  \int_{\chi<\delta}|\nabla^k\operatorname{Rm}(t)|^p
  \le C(k,p,\delta,g(\tau)).
\]

Combining gives
\(\|\nabla^k\operatorname{Rm}(t)\|_{L^p(M)}\le C(k,p,K,\delta,\chi,g(\tau))\)
on \([\tau,T_{\max})\). \(\square\)


### 1.3 Step C: staggered derivative induction

Wang's staggered triple (Remark 4.2) in our variables is:

| Level \(m\) | Variable | Highest-order input |
|:-:|:-:|:-:|
| \(\nabla^m U\) | — | \(\nabla^{m-1}\operatorname{Rm}\) |
| \(\nabla^{m-1}\operatorname{Rm}\) | — | \(\nabla^m\chi\) |
| \(\nabla^m\chi\) | — | \(\nabla^{m-1}U\) |

That is:
1. \(\|\nabla^mU\|_p\) depends on \(\|\nabla^{m-1}\operatorname{Rm}\|_{p'}\) as
   highest order.
2. \(\|\nabla^{m-1}\operatorname{Rm}\|_{p'}\) depends on
   \(\|\nabla^m\chi\|_{p''}\) as highest order.
3. \(\|\nabla^m\chi\|_{p''}\) depends on \(\|\nabla^{m-1}U\|_{p'''}\) as
   highest order.

**Level \(m=0\)**: Step B gives \(\|\operatorname{Rm}\|_p\) bounded.
Since \(U=a\operatorname{Rm}+aG\) and \(a,G\) are bounded,
\(\|U\|_p\) is bounded.  And \(\chi\) is fixed, so
\(\|\chi\|_{W^{k,p}}\) is bounded for all \(k\).

**Level \(m=1\) (base pair).**

(a) **Cutoff jet \(\nabla^2\chi\).**  The Levi-Civita connection \(\Gamma\)
    evolves as
    \[
      \partial_t\Gamma=-g^{-1}*\nabla(aE)
      =-g^{-1}*\nabla\operatorname{Ric}(U)
      =-g^{-1}*(\text{contraction of }\nabla U).
    \tag{1.11}
    \]
    Therefore
    \[
      \partial_t(\nabla^2\chi)
      =-(\partial_t\Gamma)*\nabla\chi
      =g^{-1}*\nabla U*\nabla\chi.
    \tag{1.12}
    \]
    Testing against \(|\nabla^2\chi|^{p-2}(\nabla^2\chi)\):
    \[
      {d\over dt}\|\nabla^2\chi\|_p^p
      \le C(K)\bigl(\|\nabla U\|_p^p+\|\nabla^2\chi\|_p^p\bigr)+C .
    \tag{1.13}
    \]

(b) **Derivative \(\nabla U\).**
    Following Wang Lemma 4.4, the differentiated U-equation gives
    \[
      \partial_t(\nabla U)
      =a\Delta(\nabla U)
       +\sum_{i+j+k=3,\,k\le2}\nabla^i\chi*\nabla^j\chi*\nabla^k\operatorname{Rm}
       +a*\operatorname{Rm}*\nabla U
       +\text{lower}.
    \tag{1.14}
    \]
    The highest cutoff allocation \(i+j=3,\,k=0\) is \(\chi\nabla^3\chi*\operatorname{Rm}\);
    after one integration by parts this yields \(\nabla^2\chi\) coupled to
    \(\nabla\operatorname{Rm}\).  All \(\chi\nabla^2\chi*\nabla U\) terms are
    handled by (0.4).

    Testing against \(|\nabla U|^{p-2}(\nabla U)\) and collecting:
    \[
      {d\over dt}\|\nabla U\|_p^p
      \le C_p(K+1+r^{-2})
          \bigl(\|\nabla U\|_p^p
                +\|\operatorname{Rm}\|_{p'}^{p'}
                +\|\nabla^2\chi\|_{p''}^{p''}\bigr)+C_p .
    \tag{1.15}
    \]

Combining (1.13) and (1.15) into
\(Y_1=\|\nabla U\|_p^p+\|\nabla^2\chi\|_p^p\):
\[
  Y_1'\le C_p(K+1+r^{-2})(Y_1+\|\operatorname{Rm}\|_{p'}^{p'})+C_p.
\tag{1.16}
\]
The \(\operatorname{Rm}\) term is bounded from Step B.  Gronwall gives
\(Y_1(t)\le C\) on \([\tau,T_{\max})\).

**Level \(m\ge2\) (induction step).**

Wang's Lemma 4.5 generalizes.  The differentiated \(U\)-equation at level \(m\)
contains:
\[
  \partial_t(\nabla^mU)
  =a\Delta(\nabla^mU)
   +\sum_{i+j+k=m+2,\,k\le m+1}
      \nabla^i\chi*\nabla^j\chi*\nabla^k\operatorname{Rm}
   +\sum_{i+j+k=m}
      \nabla^i(a)*\nabla^j\operatorname{Rm}*\nabla^k\operatorname{Rm}
   +\text{lower}.
\tag{1.17}
\]

The top cutoff allocations are of the types in A03 Step 38, (3.1):
\[
  \Gamma_1=\chi\nabla^{m+2}\chi*\text{lower},
  \quad
  \Gamma_2=\nabla\chi*\nabla^{m+1}\chi*\text{lower},
  \quad
  \Gamma_3=\chi\nabla^{m+1}\chi*\nabla U,
  \quad
  \Gamma_4=\chi\nabla\chi*\nabla^{m+1}U.
\tag{1.18}
\]
\(\Gamma_4\) is absorbed by diffusion.  \(\Gamma_1\) integrates once to produce
\(\nabla^{m+1}\chi\) coupled to the current level.
\(\Gamma_2\) and \(\Gamma_3\) are paid by the coupled cutoff-jet equation.
All single-Hessian terms \(\chi\nabla^2\chi*\nabla^mU\) are paid by (0.4).

The cutoff-jet equation at level \(m+1\) is (Wang Lemma 4.6):
\[
  \partial_t|\nabla^{m+1}\chi|
  \le C(K)\sum_{k\le m}|\nabla^k U|\cdot|\nabla^{m+1-k}\chi|.
\tag{1.19}
\]

Define
\[
  Y_m=\|\nabla^mU\|_p^p+\|\nabla^{m+1}\chi\|_p^p.
\tag{1.20}
\]
At level \(m\), the Gronwall inhomogeneity comes from lower levels
\(Y_0,\ldots,Y_{m-1}\), which are bounded by the induction hypothesis.  Therefore
\[
  Y_m'\le C_{p,m,K,\chi}(Y_m+C_{m-1})+C,
\tag{1.21}
\]
giving \(Y_m(t)\le C(p,m,K,\chi,g(\tau))\) on \([\tau,T_{\max})\).

### 1.4 Step D: pointwise bounds and extension

For \(p>4=\dim M\), Sobolev embedding gives
\[
  \sup|\nabla^mU|
  \le C\bigl(\|\nabla^{m+1}U\|_p+\|\nabla^mU\|_p\bigr)
  \le C(m,K,\chi,g(\tau))
\tag{1.22}
\]
on \([\tau,T_{\max})\).  Since \(\nabla^mU=\sum_{j\le m}\binom{m}{j}\nabla^ja*\nabla^{m-j}T\), controlling \(\nabla^mU\) and the cutoff jets
controls \(\nabla^mT=\nabla^m\operatorname{Rm}\) on any open set where \(a\ge a_0>0\).

By Hamilton's extension principle (Wang Proposition 4.3), the smooth solution
extends past \(T_{\max}\). \(\square\)

**Remark 1.3.** All constants in Theorem 1.1 are per-datum: they depend on
\(K(\tau)\), \(\chi\), \(\tau\), \(T_{\max}\), and \(g(\tau)\), not on the
topology or collapse parameters of the sequence.  This is correct and expected:
continuation is about each individual smooth flow, not about the sequence.

---

## 2. Quantifier separation and the first-exit argument

The smoothing principle requires three layers with distinct uniformity:

| Layer | Quantities | Uniformity |
|:---:|:---|:---|
| A. Existence | short-time smooth start | per-datum (Yang) |
| B. Continuation | \(\nabla^mU\), cutoff jets | per-datum (Theorem 1.1) |
| C. Terminal geometry | \(K_2\), \(Y\), \(J_6\), \(Q\), \(\|aF\|\), \(\|aE\|\) | **sequence-uniform** |

Layers A and B use individual-metric constants and are not required to be
uniform across the topology parameter \(A\).  Layer C uses the selected-support
hypotheses (small \(\gamma\), macro-disjoint buffers, volume control) and must
produce sequence-uniform bounds for the terminal Derdziński contradiction.

The continuation theorem closes layer B as soon as the weighted curvature
endpoint from layer C provides a finite \(\sup|U|\) on any positive-time slab.

---

## 3. First-exit closure

### 3.1 First-exit set

Following A03 Step 35, define the first-exit set on each macro-disjoint support
\(j\).  Given constants \(K_*,\gamma_*,\Lambda_*,\theta\) and an input datum
\((M_i,g_i,\chi_j)\):

- **(F1)** \(K_{2,j}^\eta(t)\le 2K_{2,j}^\eta(0)\),
- **(F2)** \(\gamma_j(t)=\mathcal S_j(t)K_{2,j}^\eta(t)^{1/2}\le 2\gamma_j(0)\le\gamma_*\),
- **(F3)** \(\|g(t)/g(0)-I\|_\infty\le\Lambda_*\) on \(\operatorname{supp}\eta_j\),

and let
\[
  T^*=\sup\{t\in(0,\theta r^2]:(F1)\text{--}(F3)\text{ hold on }[0,t)\text{ and the flow is smooth}\}.
\tag{3.1}
\]

### 3.2 Self-improvement at \(T^*\)

Suppose \(T^*<\theta r^2\).

**Smooth existence on \([0,T^*)\).**
By (F1)–(F3), the Moser endpoints (A03 Step 38, (5.5)–(5.7)) give:
\[
  \|aF(t)\|_\infty\le C\gamma/t,
  \qquad
  \|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}
\tag{3.2}
\]
for \(t\in(0,T^*)\).  In particular, since \(|U|\le a|\operatorname{Rm}|+a|G|\le
aF+C\le\|aF\|_\infty+C\):
\[
  K(\tau):=\sup_{M\times[\tau,T^*)}|U|
  \le{C\gamma\over\tau}+C
  <\infty
\tag{3.3}
\]
for every \(\tau>0\) (without using unweighted \(\sup|T|\)).  By Theorem 1.1, the smooth solution extends past \(T^*\):
the flow exists on \([0,T^*+\varepsilon)\) for some \(\varepsilon>0\).

**Energy self-improvement.**
The K₂ energy persistence (Step 34, (4.5)) gives, for small \(\gamma\):
\[
  K_{2,j}^\eta(t)\le e^{Cr^{-2}t}K_{2,j}^\eta(0)
  \le e^{C\theta}K_{2,j}^\eta(0)
  <2K_{2,j}^\eta(0)
\tag{3.4}
\]
for \(\theta\le\theta_0(C)\).  So (F1) is strictly satisfied at \(T^*\).

**Sobolev self-improvement.**
Metric drift on \([0,T^*]\) is bounded:
\[
  \|g(T^*)/g(0)-I\|_\infty
  \le C\int_0^{T^*}\|aE\|_\infty\,dt
  \le C\delta\theta^{2/3}r^2
  <\Lambda_*/2
\tag{3.5}
\]
for \(\delta\theta^{2/3}\) small.  Thus \(\mathcal S_j(T^*)\le(1+o(1))\mathcal S_j(0)\),
and \(\gamma_j(T^*)=\mathcal S_j(T^*)K_{2,j}^\eta(T^*)^{1/2}\) strictly satisfies (F2).

(F3) is strictly satisfied by (3.5).

**Conclusion.** (F1)–(F3) hold on \([0,T^*+\varepsilon']\) for some
\(\varepsilon'>0\), contradicting the definition of \(T^*\).  Therefore
\(T^*=\theta r^2\).

### 3.3 Assembled smoothing principle

**Theorem 3.1 (conditional smoothing principle).**
Under the following conditions on a closed smooth four-manifold
\((M^4,g_0)\) with a fixed cutoff \(\chi\in C_0^\infty(M)\):

1. \(a=\chi^2\), \(\|d\chi\|_\infty\le C/r\), support radius \(\sim r\);
2. \(\gamma_0=\mathcal S_0 K_{2,0}^{1/2}\ll1\);
3. \(\delta=\|g_0^{-1}E_0\|_\infty\ll1\) on \(\operatorname{supp}\chi\);
4. short-time smooth existence (transported DeTurck);

the normalized cutoff Ricci flow (0.1) has a smooth solution on \([0,\theta r^2]\)
with:
\[
  K_2^\eta(t)\le CK_2^\eta(0),
  \qquad
  \|aF(t)\|_\infty\le C\gamma/t,
  \qquad
  \|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3},
\]
\[
  J_6(t)\le C\delta^6V,
  \qquad
  Q(t)\le e^{C\theta}Q(0).
\]

The proof combines:
- per-datum short-time existence (§1, layer A);
- Theorem 1.1 continuation (§1, layer B);
- first-exit self-improvement (§3.2, layer C).

The conditional inputs are: transported-coefficient DeTurck existence (A03 Step 37),
the fixed-exponent curvature/defect estimates (Steps 34–35, A03 Step 38), and the
global Q persistence (Step 36).  The assembled smoothing principle is *not* a
conditional theorem with unverified external hypotheses: layers A and B are
per-datum consequences of the flow equation itself, while layer C is a
self-contained first-exit argument that only requires the input parameters
\(\gamma_0,\delta,r\) to be appropriately chosen.

---

## 4. Downstream implications for the restricted negative route

If Theorem 3.1 is applied on macro-disjoint selected supports for a
near-critical Ishida--LeBrun sequence with \(\delta_i\to0\), \(A_i\to\infty\),
\(\sigma_i/A_i\to0\), the downstream chain is:

1. **Flow to \(T=\theta r^2\)**: Theorem 3.1 gives smooth metrics \(g_i(T)\) with
   \(Q_i(T)\le e^{C\theta}Q_i(0)\to0\) (since \(Q_i(0)=O(\delta_i^2\operatorname{Vol}_i)\to0/A_i\)).
2. **Terminal recalibration** (Step 28): reapply the Seiberg--Witten/Chern--Gauss--Bonnet
   identities on \(g_i(T)\), giving terminal deficits bounded by \(O(Q_i(T))\).
3. **Plateau selection**: macro-disjoint bounded-curvature regions with
   \(\operatorname{Vol}(P_i)\ge\alpha A_i\) and radius-\(\rho\) buffers.
4. **Exponential pullback**: Rauch comparison on tangent-space balls selects a
   center with vanishing mean terminal deficit.
5. **Forbidden germ**: harmonic-coordinate compactness and Derdziński's
   conformally Kähler theorem give a smooth Einstein four-manifold realizing the
   calibrated spectrum, which is locally Kähler with \(|W^+|^2=1/24\) but
   a negative Kähler--Einstein metric requires \(|W^+|^2=2/3\).
   Contradiction.

This would rule out the near-critical Ishida--LeBrun family as a source of
negative counterexamples.

---

## 5. What this step does NOT establish

The continuation theorem and first-exit closure complete the *flow platform*.
The following items remain:

1. **Macro-disjoint support construction**: maximal-function good centers,
   volume-proportional assignment, coloring, plateau containment.
2. **Plateau volume bound**: \(\operatorname{Vol}(P_i)\ge\alpha A_i\) requires a
   uniform \(\operatorname{Vol}(M_i)/A_i\) lower bound and good-center density.
3. **Positive-branch counterpart**: entirely separate mechanism (A02 period
   transport).
4. **Arbitrary four-manifold topology**: current route uses Ishida--LeBrun
   inputs only.
5. **Dimensions \(n\ge5\)**: no Seiberg--Witten, calibrated Weyl, or Derdziński
   analogue.
6. **Lean formalization**: premature.
7. **Full Yau Problem 26 decision**: unresolved.

---

## 6. File dependencies

- Signed Hessian-cutoff lemma: A03 Step 38, §1 (read and used in §1.2–1.3).
- Wang source: `Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md`,
  lines 396–512.
- Index-level Hessian-a tensors: `workspace/notes/step35_tensor_variation_and_hessian_a.md`.
- K₂/Y/J₆ fixed-exponent chain: `workspace/notes/step34_integrated_potential_q3_and_defect.md`,
  A03 Step 38 §4.
- Global Q persistence: `workspace/notes/step36_analytic_platform_and_global_Q.md` §3.
- Terminal recalibration: `workspace/notes/step28_terminal_recalibration_pullback.md`.
- Conditional Moser endpoints: A03 Step 38 §5.
- Verification script: `workspace/scripts/step37_continuation_verify.py`.
