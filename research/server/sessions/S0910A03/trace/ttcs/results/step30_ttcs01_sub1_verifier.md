# TTCS Independent Branch Record

```json
{
  "step_id": 30,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/Pseudolocality-of-Ricci-Flow-under-Integral-Bound-of-Curvature--ca47a7c773f9--79daf5157f68/object.md",
    "Sessions/S0910A03/workspace/codex_loop/work/shifted_curvature_continuation.md",
    "Sessions/S0910A03/workspace/notes/step27_normalized_local_flow_extension_theorem.md"
  ]
}
```

## Task

Adversarially verify the claimed smooth-extension proof for the normalized fixed-cutoff flow ∂_t g=-2χ²(Ric+g), focusing only on the high-order Wang induction. Read Wang's actual Section 4 source and the Codex/A03 shifted-curvature derivations. Determine whether the grouped Γ1–Γ4 integrations really bound ∇^m U using cutoff derivatives only through order m (not m+1 or m+2), without dividing by χ or assuming hidden pointwise bounds. Expand the dangerous terms sufficiently to expose any unmatched factor, state a valid finite Hölder-exponent schedule if it closes, and classify the new G-linear terms exactly. If the source itself has a gap, identify it precisely rather than inheriting it. The scientific output should be a rigorous lemma/proof or a concrete obstruction.

## Output

# Scientific memo: high-order induction for the shifted normalized local flow

## 1. Main result

Let
\[
a=\chi^2,\qquad T=\operatorname{Rm}+G,\qquad U=aT,
\]
with \(\operatorname{Ric}(G)=g\). The differentiated \(U\)-equation contains
\[
\Gamma_1=\chi\nabla^{m+2}\chi*U,\quad
\Gamma_2=\nabla\chi*\nabla^{m+1}\chi*U,
\]
\[
\Gamma_3=\chi\nabla^{m+1}\chi*\nabla U,\quad
\Gamma_4=\chi\nabla\chi*\nabla^{m+1}U.
\]

The integration described in Wang Proposition 4.14 and in §7.3 of `shifted_curvature_continuation.md` does **not** estimate \(\nabla^mU\) from cutoff derivatives only through order \(m\). An unmatched term containing \(\nabla^{m+1}\chi\) remains.

A valid replacement is a coupled induction:
\[
\boxed{\quad
(\nabla^mU,\ \nabla^{m+1}\chi)
\ \text{are estimated together, followed by }\nabla^mT.
\quad}
\]
This needs no \(\nabla^{m+2}\chi\) input, no division by \(\chi\), and no pointwise estimate for cutoff derivatives of order at least two. It supplies the high-order part needed for smooth continuation.

---

## 2. The unmatched term in the \(\Gamma_1\) integration

Put
\[
W=\nabla^mU,\qquad
H=\nabla^{m+1}\chi,\qquad
Q=\nabla^m\chi,
\]
and
\[
\Phi_p(W)=|W|^{p-2}W.
\]
A representative contraction from \(\Gamma_1\) contributes
\[
I_1=\int_M \Phi_p(W)*
       \chi\nabla H*U\,d\mu .
\]
One covariant integration by parts gives
\[
\begin{aligned}
I_1={}&-\int_M \nabla\Phi_p(W)*\chi H*U\,d\mu\\
&-\int_M\Phi_p(W)*\nabla\chi*H*U\,d\mu\\
&-\int_M\Phi_p(W)*\chi H*\nabla U\,d\mu
+\text{commutator terms}.                                    \tag{2.1}
\end{aligned}
\]

The first term,
\[
J=-\int_M \nabla\Phi_p(W)*\chi H*U\,d\mu,                     \tag{2.2}
\]
is the missing term. Since
\[
|\nabla\Phi_p(W)|
 \le C_p|W|^{p-2}|\nabla W|,
\]
and \(|U|\le K\),
\[
\begin{aligned}
|J|
&\le C_pK\int_M
       \chi|\nabla W|\,|H|\,|W|^{p-2}\,d\mu\\
&\le \varepsilon
 \int_M\chi^2|\nabla W|^2|W|^{p-2}\,d\mu
 +C_{\varepsilon,p}K^2
 \int_M|H|^2|W|^{p-2}\,d\mu.                                 \tag{2.3}
\end{aligned}
\]
Thus
\[
|J|
\le \varepsilon D_{m,p}
 +C_{\varepsilon,p}K^2
 \|H\|_{L^p}^2\|W\|_{L^p}^{p-2},                             \tag{2.4}
\]
where
\[
D_{m,p}=\int_M\chi^2|\nabla W|^2|W|^{p-2}\,d\mu.
\]

Consequently \(J\) requires \(\nabla^{m+1}\chi\) in \(L^p\). It is not controlled by \(\nabla^r\chi\), \(r\le m\).

The other three displayed terms cannot cancel \(J\):

* \(\Gamma_2\) and \(\Gamma_3\) initially contain \(\Phi_p(W)*H\), not
  \(\nabla\Phi_p(W)*H\).
* Integrating \(\Gamma_2\) or \(\Gamma_3\) moves the derivative from \(H\) to \(Q\), producing \(\nabla\Phi_p(W)*Q\), not the expression in (2.2).
* \(\Gamma_4\) contains \(\chi\nabla\chi*\nabla W\), whose coefficient only uses \(\nabla\chi\).

Integrating (2.2) once more produces \(\nabla^2\Phi_p(W)\), hence \(\nabla^2W\), while diffusion controls only the weighted first derivative \(\chi\nabla W\). Reversing that integration returns (2.2).

This is the precise missing step in Wang Proposition 4.14. The sentence asserting that integration by parts in \(\Gamma_1,\Gamma_2,\Gamma_3\) leaves only
\[
\nabla^2\chi*\nabla^m\chi*U*W|W|^{p-2}
\]
omits (2.2). The same omission occurs in equation (7.12) of the Codex derivation.

---

## 3. Principal-term test

The absence of an estimate using only cutoff derivatives through order \(m\) can also be seen from a local scalar principal-term test. On a flat coordinate interval, take
\[
\chi_N=1+\delta N^{-m}\sin(Nx+\theta_1),\qquad
u_N=1+\varepsilon N^{-m}\sin(Nx+\theta_2),
\]
with phases chosen so that
\[
\partial^m u_N
\quad\text{and}\quad
\partial^{m+2}\chi_N
\]
have the same sign profile.

Then all derivatives \(\partial^r\chi_N\), \(r\le m\), remain uniformly bounded, while
\[
|\partial^{m+1}\chi_N|\asymp \delta N,\qquad
|\partial^{m+2}\chi_N|\asymp \delta N^2.
\]
Writing \(W_N=\partial^m u_N\), the \(\Gamma_1\) energy contribution has size
\[
\int |W_N|^{p-2}W_N\,
      \chi_N\partial^{m+2}\chi_N\,u_N
 \asymp \delta\varepsilon^{p-1}N^2.                           \tag{3.1}
\]
The diffusion has size
\[
\int\chi_N^2|\partial W_N|^2|W_N|^{p-2}
 \asymp \varepsilon^pN^2.                                    \tag{3.2}
\]
Taking \(\varepsilon\ll\delta\), the source in (3.1) cannot be bounded by a fixed portion of (3.2) plus quantities depending only on derivatives of \(\chi_N\) through order \(m\) and \(\|W_N\|_p\). The other \(\Gamma_2,\Gamma_3,\Gamma_4\) terms have lower powers of \(N\) in this test, so they cannot cancel (3.1).

This scalar term is the principal part of the genuine tensor expression obtained by differentiating
\[
(\nabla^2a)*T=2\chi\nabla^2\chi*T+2\nabla\chi*\nabla\chi*T.
\]

---

## 4. Correct coupled high-order lemma

### Lemma

Assume:

1. \(g(t)\) is uniformly equivalent to \(g(0)\);
2. \(\sup|U|<\infty\) and \(\sup|\nabla\chi|<\infty\);
3. the unweighted curvature derivatives through order \(m-1\), the weighted derivatives through order \(m-1\), and cutoff derivatives through order \(m\) are uniformly bounded in every required finite \(L^q\) space;
4. the differentiated equations have the forms displayed as (3.1)–(3.2) in `step27_normalized_local_flow_extension_theorem.md`.

For every fixed \(p>\max\{n,2\}\), define
\[
X_p=\|\nabla^mU\|_{L^p}^p,\qquad
Z_p=\|\nabla^{m+1}\chi\|_{L^p}^p.
\]
Then
\[
\frac d{dt}(X_p+Z_p)+c_{m,p}D_{m,p}
 \le C_{m,p}(1+X_p+Z_p).                                     \tag{4.1}
\]
The constant uses only finite \(L^q\) norms from earlier derivative levels and the smooth initial value of \(\nabla^{m+1}\chi\).

### Proof: the four top terms

Equation (2.3) gives
\[
|J|\le\varepsilon D_{m,p}
 +C\|H\|_p^2\|W\|_p^{p-2}
\le\varepsilon D_{m,p}+C(X_p+Z_p).                            \tag{4.2}
\]

The \(\Gamma_2\) term satisfies
\[
\left|\int\Phi_p(W)*\nabla\chi*H*U\right|
\le C Z_p^{1/p}X_p^{(p-1)/p}
\le C(X_p+Z_p).                                               \tag{4.3}
\]

For every \(\Gamma_3\)-type term, integrate the derivative from
\(H=\nabla Q\):
\[
\begin{aligned}
\int\Phi_p(W)*\chi\nabla Q*\nabla U
={}&-\int\nabla\Phi_p(W)*\chi Q*\nabla U\\
&-\int\Phi_p(W)*\nabla\chi*Q*\nabla U\\
&-\int\Phi_p(W)*\chi Q*\nabla^2U
+\text{lower commutators}.                                   \tag{4.4}
\end{aligned}
\]
The first term is bounded by
\[
\varepsilon D_{m,p}
 +C\int |Q|^2|\nabla U|^2|W|^{p-2}
\le \varepsilon D_{m,p}+C(1+X_p),                             \tag{4.5}
\]
using \(Q,\nabla U\in L^{2p}\). The second term is treated by Hölder and Young.

When \(m\ge3\), \(\nabla^2U\) is an earlier derivative and the third term in (4.4) is also bounded by \(C(1+X_p)\). When \(m=1\), it contains \(\chi\nabla W\) and is absorbed by \(D_{m,p}\). For \(m=2\), it has the form
\[
\int |\chi\nabla^2\chi|\,|W|^p.
\]
No pointwise estimate for \(\nabla^2\chi\) is needed. Put
\[
f=|W|^{p/2},\qquad y=\chi f.
\]
Uniform Sobolev and
\[
|\nabla y|^2
 \le C_p\bigl(\chi^2|\nabla W|^2|W|^{p-2}
             +|\nabla\chi|^2|W|^p\bigr)
\]
give, for \(n>2\),
\[
\begin{aligned}
\int|\nabla^2\chi|\,|y|\,|f|
&\le \|\nabla^2\chi\|_{L^n}
    \|y\|_{L^{2n/(n-2)}}\|f\|_{L^2}\\
&\le \varepsilon D_{m,p}+C_{\varepsilon,p}X_p.                \tag{4.6}
\end{aligned}
\]
In dimension two one uses any fixed \(L^q\), \(q>2\), and the corresponding finite Sobolev exponent.

Finally,
\[
\left|\int\Phi_p(W)*
 \chi\nabla\chi*\nabla W\right|
\le\varepsilon D_{m,p}+C X_p.                                 \tag{4.7}
\]

### Cutoff equation

From
\[
\partial_t\Gamma=\nabla U
\]
schematically, the top part of the cutoff evolution is
\[
\partial_tH=U*H+W*\nabla\chi+L_m,                             \tag{4.8}
\]
where \(L_m\) contains only earlier derivative levels. Therefore
\[
\frac d{dt}Z_p
\le C(1+Z_p+X_p).                                             \tag{4.9}
\]
Combining (4.2)–(4.9) with the remaining lower products yields (4.1).

No quotient involving \(\chi\) appears.

---

## 5. Finite Hölder-exponent schedule

For a target exponent \(p>\max\{n,2\}\), the finite list
\[
p,\qquad 2p,\qquad 4p
\]
is sufficient:

* The current pair \(W=\nabla^mU\) and \(H=\nabla^{m+1}\chi\) is used only in \(L^p\).
* Products such as
  \[
  |Q|^2|\nabla U|^2|W|^{p-2}
  \]
  use \(Q,\nabla U\in L^{2p}\).
* Expanding
  \[
  \nabla^ia
  =\sum_{r=0}^i\nabla^r\chi*\nabla^{i-r}\chi
  \]
  creates at most two cutoff factors. Together with one lower \(U\)-factor and one lower \(T\)-factor, there are at most four earlier-level factors; assigning each \(L^{4p}\) places their product in \(L^p\).
* The weighted multiplier estimate (4.6) uses only
  \(\nabla^2\chi\in L^n\), already included because \(p>n\).

The induction is quantified over every finite \(p\). Thus, when proving the level-\(m\) estimate at exponent \(p\), the earlier levels are invoked at \(2p\) and \(4p\). No infinite exponent ladder occurs.

The valid ordering is
\[
(\nabla^mU,\nabla^{m+1}\chi)
\longrightarrow \nabla^mT
\longrightarrow
(\nabla^{m+1}U,\nabla^{m+2}\chi).
\]
This agrees with “Move A/Move B” in §6 of the Step 27 note, rather than the order asserted in §7.3 of the Codex document.

---

## 6. Exact derivative class of the new \(G\)-terms

Since \(\nabla G=0\), the normalization contribution to the undifferentiated \(U\)-equation is a universal contraction of
\[
aG*U.
\]
After \(m\) spatial derivatives, every new term is of the form
\[
\boxed{\quad
\mathcal G_m
 =\sum_{i+j=m}\nabla^ia*G*\nabla^jU.
\quad}                                                        \tag{6.1}
\]

There are two cases:

* \(i=0,j=m\):
  \[
  aG*\nabla^mU,
  \]
  a bounded zeroth-order coefficient multiplying the current derivative.

* \(j<m\):
  \[
  \nabla^ia*G*\nabla^jU,
  \]
  involving only earlier \(U\)-derivatives and cutoff derivatives through order \(i\le m\).

Hence
\[
\left|\int\Phi_p(W)*\mathcal G_m\right|
\le C(1+X_p).                                                 \tag{6.2}
\]
These terms contain neither \(\nabla^{m+1}\chi\) nor \(\nabla^{m+1}U\).

For the unweighted shifted curvature equation, the corresponding class is
\[
\boxed{\quad
\widetilde{\mathcal G}_m
 =\sum_{i+j=m}\nabla^ia*G*\nabla^jT.
\quad}                                                        \tag{6.3}
\]
Again, \(i=0,j=m\) is a bounded linear coefficient, and all other terms use earlier \(T\)-derivatives.

---

## 7. Scientific conclusion

Wang’s Proposition 4.14 contains an omitted high-order term, namely (2.2). The Codex statement that the \(\Gamma_1\)–\(\Gamma_4\) integrations use cutoff derivatives only through order \(m\) is therefore unsupported.

The smooth-continuation induction can nevertheless be completed by coupling
\[
\nabla^mU\quad\text{with}\quad\nabla^{m+1}\chi.
\]
One integration removes every occurrence of \(\nabla^{m+2}\chi\); the remaining \(\nabla^{m+1}\chi\) term is controlled by the cutoff evolution at the same derivative level. The finite exponent schedule \(p,2p,4p\) closes all products, and the new \(G\)-terms are strictly zeroth-order or earlier-level terms as classified in (6.1)–(6.3).