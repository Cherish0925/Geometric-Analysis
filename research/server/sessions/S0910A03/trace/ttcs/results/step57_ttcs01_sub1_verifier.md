# TTCS Independent Branch Record

```json
{
  "step_id": 57,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step57_H2_evolution_and_continuation_bridge.md",
    "Sessions/S0910A01/workspace/notes/step25_tensor_energy_derivation.md",
    "Sessions/S0910A03/workspace/notes/step56_positive_time_base_pair.md",
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md"
  ]
}
```

## Task

Verify the H₂ evolution derivation in §§2-7 of this note for the exact normalized cutoff flow ∂_tg = -2χ²(Ric+g) using the shifted curvature T = Rm + g∧g/(2(n-1)). The main claims to check:

1. The identity |∇T|² = |∇Rm|² because ∇G = 0 (G is built from the metric). Does this hold exactly, including under the evolving metric g(t)? The covariant derivative ∇ = ∇_{g(t)} is time-dependent; is ∇_{g(t)}G(g(t)) still zero?

2. The Bochner pair integration §3: the cross term 2ηa(∇η)·∇|T|² vanishes because a = 0 on supp(∇η). The extra shifted-curvature term ∫η²a⟨ΔRm, G⟩ reduces by IBP to εD₂ + C/(εr²)·Vol using ∇G = 0 and the buffer collar. Check the IBP steps explicitly.

3. The Type (C) Hessian-of-a term §5: after one IBP, ∫η²(∇²a)·𝒯 = -∫η²(∇a)·∇𝒯 with the cross term killed by a∇η = 0. Then Young gives ε''D₂ + C/(ε''r²)H₂. Is this correct for 𝒯 involving E·T (a product of two curvature-type tensors)?

4. The normalization cancellation §6: under pure conformal h = -2ag in n = 4, ∫|Rm|²dμ is exactly constant (the 4D conformal invariance). For T = Rm + G, the extra G-dependent terms are bounded by CaF_T. Verify this dimension-specific cancellation.

5. The W^{1,p} → L^∞ bridge (Proposition 9.1): the base pair gives T ∈ L^q and ∇T ∈ L^q for all q on [τ,T*]. For p > 4, Kato + Sobolev gives ‖T‖_∞ < ∞. Is the Sobolev embedding valid on a closed manifold with bilipschitz-controlled geometry? Does the per-datum Sobolev constant depend on collapse? Check whether this really eliminates the need for the infinite staggered hierarchy.

## Output

## Verification memo: shifted \(H_2\) evolution and \(W^{1,p}\) bridge

### 1. Parallelness of \(G(g(t))\) and \(|\nabla T|^2=|\nabla \operatorname{Rm}|^2\)

At each fixed time \(t\), the Levi-Civita connection \(\nabla=\nabla_{g(t)}\) is metric-compatible:

\[
\nabla_{g(t)} g(t)=0.
\]

Since

\[
G(g)=\frac{g\owedge g}{2(n-1)}
\]

is obtained by tensor algebra from \(g\), it follows exactly that

\[
\nabla_{g(t)}G(g(t))=0
\]

for every \(t\). The fact that \(\nabla_{g(t)}\) varies with time is irrelevant for this spatial identity at a fixed time. Therefore

\[
\nabla T=\nabla(\operatorname{Rm}+G)=\nabla\operatorname{Rm},
\]

and hence, using the current metric \(g(t)\) to measure both sides,

\[
|\nabla T|_{g(t)}^2=|\nabla\operatorname{Rm}|_{g(t)}^2
\]

pointwise and exactly. Thus the equality of the dissipation terms

\[
D_2=\int \eta^2 a|\nabla T|^2\,d\mu
=\int \eta^2 a|\nabla\operatorname{Rm}|^2\,d\mu
\]

is correct.

One notation issue: the component normalization of \(G\) must be kept consistent. With the standard Kulkarni–Nomizu convention,

\[
(g\owedge g)_{ijkl}
=2(g_{ik}g_{jl}-g_{il}g_{jk}),
\]

the definition \(G=(g\owedge g)/(2(n-1))\) gives \(\operatorname{Ric}(G)=g\). The line in §2.8 writing

\[
G_{ijkl}=\frac{g_{ik}g_{jl}-g_{il}g_{jk}}{2(n-1)}
\]

would instead give a factor \(1/2\) under the usual convention. This does not affect the energy estimates, which only use \(\nabla G=0\) and \(|G|\le C_n\), but it matters for the exact identity \(\operatorname{Ric}(T)=E\) and for the coefficient in \(\partial_tG\).

---

### 2. Bochner pair and the shifted term \(\int \eta^2 a\langle \Delta\operatorname{Rm},G\rangle\)

The buffer cancellation used in §3 is correct. Since \(\operatorname{supp} d\eta\) lies where \(\chi=0\), one has

\[
a=\chi^2=0,\qquad da=0
\quad\text{on }\operatorname{supp} d\eta.
\]

Thus

\[
\int 2\eta a\,\nabla\eta\cdot \nabla |T|^2\,d\mu=0.
\]

For the extra shifted integral, the integration by parts is:

\[
I_G=\int \eta^2 a\langle \Delta\operatorname{Rm},G\rangle\,d\mu.
\]

On the closed manifold,

\[
I_G
=
-\int \left\langle \nabla\operatorname{Rm},
\nabla(\eta^2 aG)\right\rangle\,d\mu.
\]

Expanding,

\[
\nabla(\eta^2 aG)
=
2\eta a\,d\eta\otimes G
+\eta^2 da\otimes G
+\eta^2 a\,\nabla G.
\]

The first term vanishes because \(a\,d\eta=0\). The last term vanishes because \(\nabla G=0\). Hence

\[
I_G
=
-\int \eta^2\, da\cdot \langle \nabla\operatorname{Rm},G\rangle\,d\mu.
\]

Using \(|G|\le C_n\), \(\nabla T=\nabla\operatorname{Rm}\), and

\[
\frac{|da|^2}{a}=4|d\chi|^2\le \frac{C}{r^2},
\]

Young’s inequality gives

\[
|I_G|
\le
\varepsilon \int \eta^2 a|\nabla T|^2\,d\mu
+
\frac{C_n}{\varepsilon r^2}\int_{\operatorname{supp}\eta}1\,d\mu.
\]

So the stated estimate

\[
|I_G|\le \varepsilon D_2+\frac{C_n}{\varepsilon r^2}\operatorname{Vol}
\]

is correct.

There is one bookkeeping issue in §3: if one applies the Bochner identity directly to \(T\), then since \(\Delta T=\Delta\operatorname{Rm}\),

\[
2\langle T,a\Delta\operatorname{Rm}\rangle
=
2\langle T,a\Delta T\rangle
=
a\Delta |T|^2-2a|\nabla T|^2.
\]

In that formulation there is no additional separate \(I_G\). The \(I_G\) term appears only if one first writes the Bochner identity for \(\operatorname{Rm}\) and then expands \(T=\operatorname{Rm}+G\). The final inequality remains valid with the added \(C r^{-2}\operatorname{Vol}\) source, but the derivation should use one of these two decompositions consistently to avoid counting the same shifted piece twice.

---

### 3. Type (C) Hessian-of-\(a\) term

The schematic term

\[
I_C=\int \eta^2(\nabla^2 a)_{ij}\mathcal T^{ij}\,d\mu,
\qquad
|\mathcal T|\le C|E||T|\le C F_T^2,
\]

is handled correctly, provided the buffer assumption \(da=0\) on \(\operatorname{supp}d\eta\) is used.

The precise integration by parts is

\[
I_C
=
-\int (\nabla_i a)\,\nabla_j(\eta^2\mathcal T^{ij})\,d\mu.
\]

Expanding,

\[
I_C
=
-\int \eta^2(\nabla_i a)\nabla_j\mathcal T^{ij}\,d\mu
-2\int \eta(\nabla_i a)(\nabla_j\eta)\mathcal T^{ij}\,d\mu.
\]

The second term is zero because \(da=0\) where \(d\eta\ne0\). It is not merely \(a\,d\eta=0\) that is needed here; the factor is \(da\), not \(a\).

For \(\mathcal T\) built from \(E\), \(T\), and \(g\),

\[
\nabla \mathcal T
=
(\nabla E)*T+E*\nabla T,
\]

with metric factors contributing nothing because \(\nabla g=0\). Also

\[
|\nabla E|=|\nabla\operatorname{Ric}|
\le C_n|\nabla\operatorname{Rm}|
=
C_n|\nabla T|,
\]

and

\[
|E|\le C_nF_T,\qquad |T|\le F_T.
\]

Hence

\[
|\nabla\mathcal T|
\le C_n F_T|\nabla T|.
\]

Therefore

\[
|I_C|
\le
C\int \eta^2 |da|\,F_T|\nabla T|\,d\mu.
\]

Young’s inequality with the weight \(a\) gives

\[
|da|\,F_T|\nabla T|
\le
\varepsilon a|\nabla T|^2
+
\frac{C}{\varepsilon}\frac{|da|^2}{a}F_T^2,
\]

so

\[
|I_C|
\le
\varepsilon D_2
+
\frac{C}{\varepsilon r^2}H_2.
\]

Thus the Type (C) estimate in §5 is mathematically sound for \(E*T\)-type tensors. No \(\|\nabla^2\chi\|_\infty\) enters after this integration by parts.

---

### 4. Normalization cancellation in dimension four

The dimension-four cancellation is correct for the zero-order conformal part of the variation. For the piece

\[
h_{\mathrm{conf}}=-2a\,g,
\]

ignoring the Hessian-\(a\) terms, the algebraic variation of the lowered curvature tensor is

\[
(\partial_t\operatorname{Rm})_{\mathrm{alg}}=-2a\,\operatorname{Rm}.
\]

Thus

\[
2\langle \operatorname{Rm},-2a\operatorname{Rm}\rangle
=
-4a|\operatorname{Rm}|^2.
\]

The four inverse metrics in \(|\operatorname{Rm}|^2\) contribute

\[
+8a|\operatorname{Rm}|^2.
\]

So

\[
(\partial_t|\operatorname{Rm}|^2)_{\mathrm{alg}}
=
4a|\operatorname{Rm}|^2.
\]

The volume variation from \(h_{\mathrm{conf}}\) is

\[
\partial_t d\mu
=
\frac12\operatorname{tr}(-2ag)\,d\mu
=
-na\,d\mu.
\]

In \(n=4\),

\[
-na|\operatorname{Rm}|^2=-4a|\operatorname{Rm}|^2,
\]

so the algebraic density variation of \(|\operatorname{Rm}|^2d\mu\) cancels exactly.

For nonconstant \(a\), the full conformal variation also contains \(\nabla^2 a\) terms. Those are not part of this algebraic cancellation; they are precisely Type (C) terms and are controlled by the signed Hessian integration above. Thus the statement should be read as a zero-order dimension-four cancellation, not as invariance of \(\int|\operatorname{Rm}|^2\) under arbitrary spatially varying conformal changes. The conformally invariant four-dimensional curvature energy is \(\int |W|^2\), not \(\int|\operatorname{Rm}|^2\).

For \(T=\operatorname{Rm}+G\), the remaining \(G\)-dependent zero-order pieces are lower order in \(F_T\). Under the conformal algebraic part,

\[
\partial_tG=-4aG
\]

with the standard \(G=(g\owedge g)/(2(n-1))\) convention. Combining tensor variation, inverse-metric variation, and volume variation leaves terms involving

\[
a\langle \operatorname{Rm},G\rangle,\qquad a|G|^2,\qquad a,
\]

all bounded by

\[
C_n aF_T.
\]

The Ricci part of \(\partial_tG\) contributes

\[
|2\langle T,\partial_tG\rangle|
\le C_n a|T||E|
\le C_n aF_T^2
\le C_n aF_T^3,
\]

because \(F_T\ge1\). Therefore the §6 conclusion

\[
\int \eta^2 |(\text{algebraic terms})|
\le
C\int\eta^2 aF_T^3\,d\mu+C_0
\]

has the right analytic size.

One textual correction: §6 says the conformal inverse-metric variation gives something like \(+8a|E||\operatorname{Rm}|^2\). For the pure conformal subpart it is \(+8a|\operatorname{Rm}|^2\). The \(|E|\)-weighted cubic term belongs to the full \(-2aE\) metric variation, not to the exact conformal cancellation.

---

### 5. Resulting \(H_2\) inequality

After correcting the bookkeeping point in the Bochner decomposition, the estimate

\[
\frac d{dt}H_2+(2-\delta_0)D_2
\le
C_1\int\eta^2aF_T^3\,d\mu
+\frac{C_2}{r^2}H_2
+C_0
\]

is supported by the computations in §§2–7.

The constants depend on dimension, the first cutoff derivative bound \(|d\chi|\lesssim r^{-1}\), the buffer geometry, and \(\delta_0\). The derivation does not need a direct \(\|\nabla^2\chi\|_\infty\) term.

A small notation correction in §2.2: since \(E=\operatorname{Ric}+g\),

\[
\operatorname{tr}E=\operatorname{scal}+n.
\]

Thus if \(s=\operatorname{scal}\), then \(\operatorname{tr}E=s+n\). The displayed phrase “\(s=\operatorname{tr}(E)-n=\operatorname{scal}+n\)” has a shifted \(+n\). The estimate itself uses the correct quantity \(\operatorname{tr}E\).

---

### 6. \(W^{1,p}\to L^\infty\) bridge

Assume the Step 56 differential inequalities are available on \([\tau,T^*)\), and assume

\[
\|aF_T(t)\|_\infty\le \frac{C\gamma}{t}.
\]

Then on \([\tau,T^*)\),

\[
|\partial_tg|
=
2a|E|
\le C aF_T
\le \frac{C\gamma}{\tau},
\]

so \(g(t)\) is bilipschitz equivalent to \(g(\tau)\) with a finite per-datum constant.

The Step 56 chain gives, for every finite \(q\),

\[
T\in L^\infty([\tau,T^*];L^q),
\]

then

\[
V=\nabla U,\quad Z=\nabla^2\chi
\in L^\infty([\tau,T^*];L^q),
\]

and finally

\[
\nabla T\in L^\infty([\tau,T^*];L^q).
\]

Choose \(p>4\). At each fixed time,

\[
|d|T||\le |\nabla T|
\]

by Kato’s inequality, so \(|T|\in W^{1,p}\). The Sobolev embedding

\[
W^{1,p}(M,g(\tau))\hookrightarrow L^\infty(M),
\qquad p>4,
\]

has a finite constant because \(M\) is closed and \(g(\tau)\) is smooth. Bilipschitz equivalence converts the \(g(t)\)-norms to \(g(\tau)\)-norms with a finite factor. Therefore

\[
\|T(t)\|_\infty
\le
C_{S,\tau,p}
\bigl(
\|T(t)\|_{L^p(g(t))}
+
\|\nabla T(t)\|_{L^p(g(t))}
\bigr),
\]

uniformly for \(t\in[\tau,T^*)\). This proves pointwise curvature boundedness on the terminal slab.

The Sobolev constant here is per datum. It may depend strongly on the geometry of \((M,g(\tau))\), including collapse. That dependence is harmless for continuing a single smooth branch; it is not a sequence-uniform input.

The bridge genuinely replaces the infinite derivative ladder for the specific purpose of obtaining \(\|T\|_\infty\): only \(T\), \(\nabla U\), \(\nabla^2\chi\), and \(\nabla T\) at sufficiently large finite \(p\) are needed.

For smooth restart past \(T^*\), however, one still needs smooth convergence of the metric at \(T^*\). The supplied text sketches this by saying that once \(|T|\) is bounded, the higher derivative hierarchy closes by standard Grönwall estimates. That is plausible, but it is a separate higher-regularity argument: bounded curvature plus the first \(W^{1,p}\) bridge gives the pointwise curvature bound, while smooth extension requires either a proved degenerate-Shi-type hierarchy or an explicit continuation theorem for this cutoff flow. Thus the finite-order bridge removes the infinite hierarchy from the curvature-boundedness step, but not from the full smooth-endpoint justification unless that higher-regularity propagation is supplied elsewhere.