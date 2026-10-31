# Step 64: Consistent shifted-curvature convention after the KN sign repair

Session: S0910A01. Agent1 / Orchestrator. Phase: Explore.

This note replaces the first draft of the Step 64 sweep. TTCS
(`trace/ttcs/results/step64_ttcs01_verifier1_integration.md`) found two real
repairs beyond the original sign relabeling: (i) the two auxiliary properties
`Ric(T)=E` and `nabla T=nabla Rm` alone do not characterize the auxiliary
constant-curvature tensor unless one also specifies that it is the universal
multiple of `g owedge g`; (ii) Step 63's pure-scaling line for `G` missed a
factor two, and the curvature norm convention had to be stated explicitly. The
repairs below are now the convention record for the restricted IL theorem.

---

## 1. Canonical convention for the IL bridge

Use Hamilton's curvature/Ricci contraction convention from Step 63:
\[
R_{jk}=g^{il}R_{ijkl}.
\]
Use the standard Kulkarni--Nomizu product
\[
(\varphi\owedge\psi)_{ijkl}=\varphi_{ik}\psi_{jl}+\varphi_{jl}\psi_{ik}
-\varphi_{il}\psi_{jk}-\varphi_{jk}\psi_{il}.
\tag{1.1}
\]
Define
\[
G_{ijkl}=\frac{1}{2(n-1)}(g\owedge g)_{ijkl}
=\frac{1}{n-1}(g_{ik}g_{jl}-g_{il}g_{jk}),
\qquad
T=\operatorname{Rm}-G.
\tag{1.2}
\]
Then
\[
g^{il}G_{ijkl}=-g_{jk},
\qquad
\operatorname{Ric}(T)=\operatorname{Ric}+g=E,
\qquad
\nabla T=\nabla\operatorname{Rm}.
\tag{1.3}
\]
The IL bridge uses the operator-normalized curvature norm, one quarter of the
full four-index contraction. With this norm
\[
|G|^2=\frac{n}{2(n-1)}=\frac23\quad (n=4).
\tag{1.4}
\]
If one instead uses the raw four-index contraction, the corresponding value is
`2n/(n-1)`; the theorem writeup must not mix these two norm conventions.

---

## 2. How to read the older `T=Rm+G` notes

Steps 34, 36, 43, 54, 55, 58, 59, and 60 wrote
\[
T_{old}=\operatorname{Rm}+G_{old}
\]
while simultaneously using the specific constant-curvature shift whose Ricci
contraction makes `Ric(T_old)=E`. Because the old `G` was meant to be the
universal `g owedge g` multiple, comparison with (1.2) gives
\[
G_{old}=-G,
\qquad
T_{old}=\operatorname{Rm}+G_{old}=\operatorname{Rm}-G=T.
\tag{2.1}
\]
This conclusion uses the *specific universal-shift definition* of `G_old`. It
would not follow from the two properties `Ric(T)=E` and `nabla T=nabla Rm`
alone: one could add a parallel Ricci-free algebraic Weyl tensor to the
auxiliary shift. That possibility is irrelevant for the old notes because they
were not introducing an arbitrary parallel Ricci-free summand; they were using
the constant-curvature reference tensor.

Thus the old estimates are read by synchronous reflection `G_old=-G`, not by
keeping the old plus sign with the canonical positive `G`.

---

## 3. Exact identities affected by the sign and norm repair

### 3.1 Norm and comparability

Under the canonical convention,
\[
|T|^2=|\operatorname{Rm}-G|^2
=|\operatorname{Rm}|^2-2\langle\operatorname{Rm},G\rangle+|G|^2.
\tag{3.1}
\]
Under the old symbol this same identity reads
\[
|T|^2=|\operatorname{Rm}+G_{old}|^2
=|\operatorname{Rm}|^2+2\langle\operatorname{Rm},G_{old}\rangle+|G_{old}|^2.
\tag{3.2}
\]
Both are the same pointwise number. In either notation,
\[
F_T=(1+|T|^2)^{1/2}\asymp_n (1+|\operatorname{Rm}|^2)^{1/2}.
\tag{3.3}
\]
The sign of the cross term is not used in the Moser or bootstrap estimates;
only (3.3) and `nabla T=nabla Rm` are used.

### 3.2 Evolution of `G`

For a metric variation `h=partial_t g`,
\[
\partial_t(g\owedge g)=2(h\owedge g),
\qquad
\partial_tG=\frac{1}{n-1}(h\owedge g).
\tag{3.4}
\]
For the cutoff flow `h=-2aE`,
\[
\partial_tG=-\frac{2a}{n-1}(E\owedge g).
\tag{3.5}
\]
Therefore
\[
\partial_tT=\partial_t\operatorname{Rm}-\partial_tG
=\partial_t\operatorname{Rm}+\frac{2a}{n-1}(E\owedge g).
\tag{3.6}
\]
The added term is algebraic in `E=Ric(T)`, hence linear in `T`; it is not an
independent constant forcing.

For pure scaling (`a=1`, `E=g`, `h=-2g`),
\[
\partial_tG=-4G,
\qquad
\partial_tT=-2\operatorname{Rm}+4G=-2T+2G.
\tag{3.7}
\]
Thus Step 63's old homogeneous line `partial_t T=-2T` was false and has been
patched. This does **not** damage the energy inequality, because the repaired
zero-order term in (3.6) is bounded by `C a F_T^2` and hence by `C a F_T^3`
since `F_T>=1`.

### 3.3 Energies and dissipations

The quantities consumed by the bridge are
\[
H_2=\int\eta^2F_T^2,
\qquad
K_p^\eta=\int\eta^2a^{p-2}F_T^p,
\qquad
Y=\int\eta^2aF_T^3,
\qquad
\Gamma=\max_\alpha\sup\mathcal S_\alpha H_{2,\alpha}^{1/2},
\tag{3.8}
\]
and dissipations built from `nabla Rm`, `nabla F_T`, or `nabla T`. Since
`T_old=T` after synchronous reflection and `nabla T=nabla Rm`, these are
unchanged as pointwise quantities. The defect Moser endpoint from Step 62 is
`G`-free.

---

## 4. Consequences for the IL proof stack

1. **Step 63 anchor.** Patched in this step: the header now states the canonical
   convention, the curvature norm normalization is explicit, the stale
   `T=Rm+G` sentence in §4.2 is corrected, and the pure-scaling table is
   replaced by the correct non-homogeneous `T` computation.
2. **Step 54 / Step 55 first-exit and `(Gamma,V)` bootstrap.** These notes use
   only `F_T`, `F_T asymp F`, `Ric(T)=E`, `nabla T=nabla Rm`, and the resulting
   energy inequalities. All survive unchanged after (2.1) and (3.3)--(3.8).
3. **Step 58 / Step 59 / Step 60 continuation.** The displayed structural
   equations should be read schematically, with all universal zero-order
   algebraic terms absorbed into `a(T+T*T)` or the corresponding `F_T` reaction.
   The equality `partial_t U=a partial_t T` is exact because `a=chi^2` is time
   independent. Step 58's old stationarity line has been annotated; the
   substantive stationarity fact remains `T=0 => E=0 => partial_t g=0`, using
   the canonical `Ric(T)=E`.
4. **Theorem assembly.** The final restricted IL theorem must be written under
   one convention, preferably (1.1)--(1.2). It should not quote exact legacy
   signs involving `G_old`; it should quote only the convention-invariant
   estimates or re-express the exact equations using `Rm=T+G`.

---

## 5. What remains after the convention repair

The convention sweep changes no curvature or defect Moser endpoint, no
signed-Hessian absorption, no `(Gamma,V)` bootstrap, and no base-pair or
all-order continuation estimate. It does, however, remove the overstrong Step 63
statement that the exact shifted curvature has a homogeneous pure-scaling
law. The current restricted IL analytic bridge therefore stands as follows:

* curvature endpoint: still at proof level as an inequality, with the corrected
  Step 63 zero-order algebra;
* defect endpoint: proof note Step 62, unaffected;
* `(Gamma,V)` first-exit bootstrap: Step 55, unaffected;
* continuation/base-pair stack: Steps 58--60, unaffected as schematic estimates
  but final text must rewrite the zero-order `G` terms under (1.2);
* sole substantive unresolved input for the conditional IL theorem: per-datum
  existence of the degenerate cutoff flow, i.e. passage from the doubly
  regularized transported-DeTurck system to the exact degenerate flow using
  regularization-uniform estimates.

A03 message #469 clarifies that the named parabolic theorem is needed only for
the strictly parabolic `(epsilon,nu)` regularized system; the real work is the
uniform estimate package allowing `epsilon,nu -> 0`. This should guide the next
Step if the session continues this IL line rather than returning to broader
Yau-26 route comparison.
