# Step 93: Signed Maxwell transport — corrected direction, Koiso OT theorem, and the remaining gap

Session `S0910A03`, Agent2 / Execute.

> **This step corrects the original claim that backward Maxwell propagation
> from the cusp end bounds separator charge.** The backward direction gives
> exponentially growing bounds, not convergent ones. TTCS verification
> independently derived the 1D counterexample: forcing at distance R from
> the separator amplifies by \(e^{3R}\). The numerical thresholds
> \(\delta^{**}=0.186\) and \(0.210\) are withdrawn.
>
> The Koiso OT theorem, forward cusp transport, and Ricci-component
> distinction are correct and survive.
>
> **Step 94 correction of Sections 6--8.** The diagonal identity in (6.1)--(6.2)
> is algebraically correct, but the maximum-principle corollary is false. At an
> interior maximum the inequality `LQ <= 0` is compatible with
> `LQ=-18Q-4Q^2<0`; `L log Q<0` is superharmonicity and does not exclude a
> maximum. The claims that `Q -> 0` at both ends forces `Q=0`, that the identity
> reproves the OT obstruction, and that source-derivative control would yield
> `Q=O(delta^2)` are withdrawn. For fixed general charge the corrected invariant
> identity is
> `L log Q=-18-4Q+e-|d(beta o U)|^2`.
> See `workspace/notes/step94_charge_sign_correction_and_global_flux.md`.

## 1. Koiso germ OT theorem (valid)

**Theorem.** The constrained Koiso germs of Step 92 preserve orthogonal
transitivity under exact Einstein continuation.

**Proof.** The Step 92 Cauchy data have
\[
g_\Sigma=ds^2+M(U(s))_{ab}\,dx^adx^b,
\]
with Weingarten block \(B\) purely in the target-normal direction and no
mixed base-orbit component. In the Gaussian normal gauge \(A_\nu=0\),
this gives initial connection curvature
\[
F_{\nu s}^a=0,\qquad q_a=\rho G_{ab}(*_\gamma F^b)=0.
\]
Under exact \(\operatorname{Ric}=-3g\), the Maxwell conservation
\(\mathrm{d}q_a=0\) preserves \(q_a\equiv0\) in the connected quotient domain.
Thus \(F^a\equiv0\) and the germ is OT. \(\square\)

**Consequence.** In any completed two-ended cylinder with free \(T^2\)
action and two outward-expanding cusp ends, the exact OT obstruction
(Steps 85–88) blocks the completion for \(\delta<\delta_*\approx0.246\).
The concentrated \(e_\nu\) germs of Step 92 do not escape the OT
obstruction because their exact Einstein continuation has \(q\equiv0\).

**Scope.** This applies only to extensions preserving the free \(T^2\)
symmetry within an exact Einstein region. A forced interior
(\(\|\operatorname{Ric}+3g\|_{\rm op}\le\delta>0\)) sources \(dq=O(\delta)\),
and the resulting twist is the substantive remaining unknown.

## 2. Signed Maxwell transport: correct forward direction

The invariant transport (Step 90, eq.\ (5.1)) is
\[
\left|\mathrm{d}w+\frac32w\,\mathrm{d}\sigma\right|
\le\frac12w|dU|+|b|,
\qquad w=\sqrt{2Q},\quad |b|\le2\sqrt2\,\delta.
\tag{2.1}
\]

### Forward propagation: separator toward cusp

Along the outward normal from the separator (\(n=0\)) toward one cusp
end (\(n\to+\infty\)):
\[
w'+(p-c)w\le\beta,
\tag{2.2}
\]
with \(p=(3/2)\sigma_\nu\), \(c=\sqrt{e_\nu}/2\), \(\beta=2\sqrt2\delta\).
On the exact cusp: \(p=3\), \(c=0\), \(\beta=2\sqrt2\delta\), so
\(p-c=3>0\). The Gronwall bound gives
\[
w(n)\le e^{-3n}w(0)+\frac{2\sqrt2\delta}3\bigl(1-e^{-3n}\bigr).
\tag{2.3}
\]
This says: **any twist at the separator is exponentially damped toward
the cusp**. On the cusp, \(w\) converges to at most
\(2\sqrt2\delta/3\), independently of \(w(0)\) and the connector length.
This is valid and useful, but it bounds cusp-side \(w\) given
separator-side \(w\), not the reverse.

### Backward propagation: cusp end toward separator

Starting from a finite distance \(R\) with \(w(R)=0\)
(exact OT open set), the reverse direction uses the lower-bound ODE:
\[
w'+\bigl(p+c\bigr)w\ge-\beta.
\tag{2.4}
\]
The comparison function \(U'\!+(p+c)U=-\beta\), \(U(R)=0\), gives
\[
U(r)=\int_r^R e^{(p+c)(s-r)}\beta\,ds.
\tag{2.5}
\]
On the exact cusp (\(p+c=3\)):
\[
U(0)=\beta\frac{e^{3R}-1}3\sim\beta\frac{e^{3R}}3.
\tag{2.6}
\]
This **grows exponentially with the collar length** \(R\). The cusp
damps twist in the forward direction but amplifies backward inversion.

### 1D counterexample (TTCS verified)

Even with \(e_\nu=0\) and \(\sigma_\nu=2\) everywhere, choose a smooth
source \(b=-\beta_0\phi(t)\) supported near \(t=R\). The exact solution
with \(w(R)=0\) is
\[
w(0)=e^{-3\cdot0}\int_0^R e^{3s}\beta_0\phi(s)\,ds
\asymp\beta_0 e^{3R}.
\tag{2.7}
\]
Hence no length-independent bound on separator twist follows from the
cusp-end boundary condition alone, even for zero orbit energy.

## 3. Why the self-consistent loop fails

The original script computed
\(w_{\rm sep}\le 2\sqrt2\delta/(3-\sqrt{B}/2)\), which is equation (2.3)
evaluated at \(n=\infty\) and incorrectly read as a bound on \(w(0)\).
The comparison kernel \(\exp(-(p-c)(t-r))\) is the *forward damping*
kernel, not the *backward propagation* kernel.

For the exact ODE \(w'+3w=b\), both \(w=Ce^{-3t}+\textrm{particular}\)
satisfy \(w(t)\to\textrm{particular}(\infty)\) for any finite \(C\), so
\(w(\infty)=0\) does not determine \(C=0\). One must use either a finite
boundary \(w(R)=0\) (yielding the exponential backward kernel) or an
independent regularity argument. Neither was supplied.

The numerical thresholds \(\delta^{**}=0.185928\ldots\) (worst case)
and \(\delta^{**}=0.210028\ldots\) (decaying \(e_\nu\)) are
**withdrawn**. They correspond to a specific radial model with an
invalid comparison direction.

## 4. Ricci component distinction (valid)

For the 4D free-\(T^2\) metric, the Ricci defect \(E=\operatorname{Ric}+3g\)
has distinct component blocks sharing the operator-norm budget
\(\|E\|_{\rm op}\le\delta\):

| Component | Type | Role |
|-----------|------|------|
| \(E_{nn},E_{ns},E_{ss}\) | base–base | horizontal Einstein, Codazzi |
| \(E_{na},E_{sa}\) | base–orbit | Maxwell source: \(\partial_n q_a\propto\rho E_{sa}\), \(\partial_s q_a\propto\rho E_{na}\) |
| \(E_{ab}\) | orbit–orbit | orbit-map tension |

The collar seed of Step 92 conflated \(E_{ns}\) (Codazzi) with
\(E_{na},E_{sa}\) (Maxwell). Normal twist transport is sourced by
\(E_{sa}\), not by \(E_{ns}\).

## 5. What controls remain for Q

The following separator-side controls survive:

1. **Stability average** (Step 91):
   \(\langle Q\rangle_C\le3+\delta\).

2. **Jacobi capacity** (Step 92):
   for any width-\(\ell\) spike of height \(A\) in
   \(\mathcal W=\frac34V+\frac18(h^2+e_s)\):
   \(A\ell\lesssim2\sqrt{a_\delta}\tanh(\sqrt{a_\delta}L/2)\).

3. **Forward cusp damping** (this step):
   \(w(n)\le e^{-3n}w(0)+O(\delta)\) on the cusp.

4. **Bochner subsolution** (Step 85):
   \(\frac12Le\ge\frac12e(e-6)\) for exact OT, with variable-twist corrections
   (Step 90).

5. **Resolvent ceiling** (Step 87): \(\sup e\le B(\delta)\) for
   exact-end, twist-free complete extensions.

Missing: a bound on \(Q_+=\sup_BQ\). The forward transport bounds cusp
\(w\) in terms of separator \(w\), but the separator \(w\) itself is
not bounded by the cusp-end condition. The global maximum of \(Q\) could
be anywhere in the finite connector region.

## 6. Supersolution identity for Q (exact case)

**Theorem.** For the free-\(T^2\) reduction with exact Einstein
equations (\(\operatorname{Ric}=-3g\)), constant charge \(q\), and
diagonal orbit shape, the physical twist energy \(Q\) satisfies
\[
\boxed{LQ=\frac{|\nabla Q|^2}Q-18Q-4Q^2,}
\tag{6.1}
\]
or equivalently
\[
\boxed{L(\log Q)=-18-4Q.}
\tag{6.2}
\]
The \(-18\) arises from the area equation (\(L\sigma=6+Q\),
contributing \(-3(6+Q)=-18-3Q\)) and the orbit traceless equation
(\(L\alpha=Q\), contributing \(-Q\)); total \(-18-4Q\).

**Proof.** Direct computation (verified symbolically in
`workspace/scripts/step93_Q_supersolution_verify.py`):
\[
LQ = Q\bigl[|3\nabla\sigma+\nabla\alpha|^2
-3\Delta\sigma-\Delta\alpha\bigr].
\]
Substitute \(\Delta\sigma=6+Q-|\nabla\sigma|^2\) (from
\(L\sigma=6+Q\)) and \(\Delta\alpha=Q-\langle\nabla\sigma,\nabla\alpha\rangle\)
(from \(L\alpha=Q\)):
\[
LQ=Q\bigl[|3\nabla\sigma+\nabla\alpha|^2-18-4Q\bigr]
=\frac{|\nabla Q|^2}Q-18Q-4Q^2.\quad\square
\]

**Withdrawn maximum-principle inference (Step 94).** On a compact domain, an
interior maximum satisfies \(LQ\le0\). The value
\(-18Q-4Q^2<0\) is fully compatible with this condition and gives no
contradiction. Likewise \(L\log Q<0\) is superharmonicity. A scalar even
solution of \(y''=-18-4e^y\) has \(Q=e^y>0\) maximized at the center and
\(Q\to0\) at both infinities. Thus (6.1)--(6.2) do not reprove either the
Koiso charge-conservation statement or the OT connector obstruction.

## 7. Forced case: structure and remaining gap

For \(\|\operatorname{Ric}+3g\|_{\rm op}\le\delta\), the modified
identity is
\[
L(\log Q)=-18-4Q+2L(\log q_0)-3D_\sigma-D_\alpha,
\tag{7.1}
\]
where \(|D_\sigma|,|D_\alpha|\le C\delta\) (from the perturbed area and
orbit equations). The term \(2L(\log q_0)\) involves
\[
L(\log q_0)=\frac{Lq_0}{q_0}-|\nabla\log q_0|^2
=\frac{d^*S+\nabla\sigma\cdot S}{q_0}-|\xi|^2,
\]
with \(S=dq_0\) the Maxwell source, \(|S|\le2\sqrt2\delta\rho\).
The divergence \(d^*S\) contains first derivatives of the Ricci defect,
which are not controlled by the \(C^0\) hypothesis
\(\|E\|_{\rm op}\le\delta\) alone.

At the maximum of \(Q\): \(\nabla Q=0\) constrains
\(\xi=\nabla\log q_0=(3\nabla\sigma+\nabla\alpha)/2\), and the
\(-|\xi|^2/2\) term is favorable. The gap is the
\(d^*S/q_0\) term.

A weak integrated formulation can avoid differentiating the mixed Ricci source,
but it does not turn the negative reaction into an upper bound. Smoothness of
each metric likewise gives no sequence-uniform derivative estimate under a
\(C^0\) Ricci pinching hypothesis. The substantive unresolved problem is a
two-ended weighted vector-charge flux estimate coupled to separator stability
and the quotient equations; see Step 94.

## 8. Corrected frontier

The free-\(T^2\) symmetry class has:
- Exact OT obstruction for \(\delta<0.246\) (Steps 85–88)
- Koiso germs preserving OT under exact Einstein continuation (this step)
- Forward cusp damping but no backward separator bound
- Separator \(\langle Q\rangle\le3+\delta\) from stability
- No global \(Q_+\) bound

The decisive missing object is one of:
1. A two-ended weighted source-to-charge flux/coercivity estimate coupling the
   stable separator, both exact end collars, and the quotient area/orbit
   equations; a scalar maximum principle for \(Q\) is not available
2. A collar transport theorem using Codazzi/Bianchi structure to propagate
   separator data into the interior
3. An explicit two-ended connector construction with \(\delta\to0\) and
   nonvanishing twist
4. A different route entirely (non-\(T^2\) graph metrics, \(N\#N\),
   positive branch)

## Provenance

- Koiso OT theorem: structural; verified by TTCS.
- Forward/backward transport: corrected per TTCS. The backward
  exponential growth counterexample is the decisive correction.
- Self-consistent thresholds: **withdrawn**.
- Script: `workspace/scripts/step93_signed_maxwell_self_consistent.py`
  (records the model and its failure).
- Data: `workspace/data/step93_signed_maxwell_self_consistent.json`
  (numbers are valid for the model but not applicable to the general
  problem).
- TTCS: `trace/ttcs/results/step93_ttcs01_verifier1_integration.md`.
