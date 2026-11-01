# TTCS Independent Branch Record

```json
{
  "step_id": 6,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step5_regular_patch_and_derdzinski_boundary.tex",
    "Sessions/S0910A03/workspace/codex_loop/work/quantitative_deficit_analysis.md",
    "Sessions/S0910A03/trace/ttcs/results/step5_ttcs01_verifier2_integration.md",
    "Knowledge/objects/papers/1406.6534-Regularity-of-Einstein-Manifolds-and-the-Codimension-4-Conject--487f466da601--0ffa6f2917a4/object.md"
  ]
}
```

## Task

Review the regular-patch and spectral-transfer chain needed to exploit any local algebraic contradiction. For a fixed critical Ishida–LeBrun manifold with ||Ric+g||∞→0 and absolute scalar–Weyl/SW deficits O(Aδ²), determine rigorously whether the existence of one unit ball with Vol B1≥v yields a fixed harmonic chart on which a smooth Einstein limit exists and the full spectrum (−1/6,1/12,1/12) holds. Check the use of Cheeger–Naber Theorem 1.13, the definition/propagation of harmonic radius, strong W^{2,p} convergence under only L∞ Ricci defect, and transfer of the selected regularized SW forms/eigenvalue defect. Pay special attention to whether a monopole solution can be chosen coherently across i and regularization, and whether local elliptic estimates give a nonzero limiting eigenform. State the strongest theorem actually justified, and exactly what conclusion about sup_p Vol B1 can follow if the local projector obstruction is valid.

## Output

## Scientific memo: regular patch and spectral transfer

### 1. What one noncollapsed unit ball gives

Assume
\[
\delta_i=\|g_i^{-1}(\Ric_{g_i}+g_i)\|_{L^\infty}\to0
\]
on the fixed critical Ishida–LeBrun four-manifold, and suppose for some \(p_i\)
\[
\Vol_{g_i}B_1(p_i)\ge v>0 .
\]
For large \(i\), \(|\Ric_{g_i}|\le 3\), so Cheeger–Naber Theorem 1.13 in the supplied arXiv:1406.6534 object applies. It gives the weak \(L^2\) harmonic-radius estimate
\[
\Vol\!\left(T_r\{x\in B_1(p_i):r_h(x)\le r\}\right)\le C(v)r^4 .
\]
This is a harmonic-radius statement; it is not a curvature-scale statement, since the sequence is only almost Einstein and there is no \(\nabla\Ric\) control.

By Bishop–Gromov, \(\Vol B_{1/2}(p_i)\ge b(v)>0\). Choose \(\rho=\rho(v)>0\) so that
\[
C(v)(2\rho)^4<\frac12 b(v).
\]
Then
\[
G_i:=B_{1/2}(p_i)\setminus T_{2\rho}\{r_h\le 2\rho\}
\]
has uniformly positive volume. For any \(x_i\in G_i\),
\[
y\in B_\rho(x_i)\quad\Longrightarrow\quad r_h(y)>2\rho .
\]
Thus one noncollapsed ball gives a positive-measure family of regular patches and, after choosing \(x_i\), a harmonic chart
\[
\Phi_i:B_{2\rho}(0)\to M,\qquad \Phi_i(0)=x_i .
\]
It does not give a uniform harmonic-radius lower bound on all of \(B_1(p_i)\), and it gives no information on curvature concentration or collapse outside the selected regular region.

### 2. Local Einstein limit under only \(L^\infty\) Ricci defect

In the harmonic charts, \(\tilde g_i=\Phi_i^*g_i\) have uniform
\[
C^{1,\alpha}\cap W^{2,p}
\]
bounds for every finite \(p\), as stated after Definition 2.9 in Cheeger–Naber. Hence, after passing to a subsequence,
\[
\tilde g_i\to g_\infty \quad\text{strongly in }C^{1,\beta}_{\rm loc},
\qquad
\tilde g_i\rightharpoonup g_\infty\quad\text{weakly in }W^{2,p}_{\rm loc}.
\]

Let
\[
E_i:=\Ric_{g_i}+g_i,\qquad \|E_i\|_{L^\infty}=O(\delta_i).
\]
In harmonic coordinates,
\[
(\Ric \tilde g_i)_{ab}
=-\frac12 \tilde g_i^{kl}\partial_k\partial_l(\tilde g_i)_{ab}
+Q_{ab}(\tilde g_i,\partial\tilde g_i).
\]
Since \(E_i\to0\) in \(L^\infty\), the equation passes to the distributional limit:
\[
\Ric(g_\infty)=-g_\infty .
\]
Elliptic regularity then makes \(g_\infty\) smooth. After this, interior elliptic estimates for the difference equation give
\[
\tilde g_i\to g_\infty
\quad\text{strongly in }W^{2,p}_{\rm loc}\quad(\forall p<\infty).
\]
This is enough to pass algebraic curvature expressions. It still does not give \(C^{2,\alpha}\) convergence of the sequence, because no derivative of \(E_i\) is controlled.

### 3. Transfer of scalar–Weyl data

The quantitative note `quantitative_deficit_analysis.md`, especially equations (30), (32), and (37), gives absolute global deficits of size \(O(A\delta_i^2)\) for a selected sign monopole class after taking a subsequence. Since \(A\) is fixed, these absolute integrals restrict to every chosen patch.

The scalar part is immediate:
\[
s_i=-4+\operatorname{tr}_{g_i}E_i\to -4
\]
uniformly. The scalar–Weyl completion gives
\[
q_i=-s_i+\sqrt6\,|W_i^+|\to \frac92
\]
in \(L^2\), hence on the harmonic chart. Strong \(W^{2,p}\) convergence gives \(W_i^+\to W_\infty^+\) in \(L^p_{\rm loc}\). Therefore
\[
s_\infty=-4,
\qquad
|W_\infty^+|=\frac{1}{2\sqrt6}.
\]

### 4. Regularized monopoles and the limiting harmonic form

For the nonsmooth optimal weight \(f=\sqrt q\), the quantitative note correctly uses smooth positive approximations. For the sequence, one may choose a diagonal family \(f_i\) with
\[
\|f_i-\sqrt{q_i}\|_{L^\infty}\to0,
\]
and choose one rescaled Seiberg–Witten solution for each \(i\). No continuous choice of solutions in \(i\) or in the regularization parameter is needed for the spectral transfer.

The fixed sign class is obtained by passing to a subsequence among finitely many sign choices. Let \(H_i\) be the harmonic self-dual representative of its \(a^+\). The estimates in `quantitative_deficit_analysis.md`, equations (16)–(17), give
\[
\|f_i\varphi_i+6\sqrt2\pi H_i\|_2\to0,
\qquad
\left\||2\pi H_i|-\frac{q_i}{3\sqrt2}\right\|_2\to0 .
\]
Since \(q_i\to9/2\),
\[
|H_i|\to \frac{3}{4\sqrt2\pi}
\]
in \(L^2\) on every selected patch.

Local elliptic estimates for the first-order Hodge system
\[
dH_i=0,\qquad d^*_{g_i}H_i=0,\qquad H_i=*_{g_i}H_i
\]
apply in the harmonic charts. The \(L^2\) norms of \(H_i\) are bounded because the selected period satisfies \(p_i=(a_i^+)^2\le A+o(1)\). Hence, after a subsequence,
\[
\Phi_i^*H_i\to H_\infty
\]
strongly in local \(L^r\) for finite \(r\), and \(H_\infty\) is smooth, harmonic, and self-dual for \(g_\infty\). The norm transfer gives
\[
|H_\infty|=\frac{3}{4\sqrt2\pi}>0 .
\]

The spinor quadratic form also has a determined limit. Since \(\varphi_i=\frac32\psi_i\) and \(f_i\to 3/\sqrt2\) locally,
\[
\psi_i\to -\frac{8\pi}{3}H_\infty
\]
in local \(L^2\). The product passage in the eigenvalue defect uses the standard pointwise spinor amplitude estimate from the rescaled Seiberg–Witten equation; \(L^2\)-closeness alone would not control \(\langle W_i^+\psi_i,\psi_i\rangle\).

### 5. Transfer of the eigenvalue defect and spectrum

Define
\[
\mathcal W_i:=W_i^+ +\sqrt{\frac23}\,|W_i^+|\,\mathrm{Id}_{\Lambda_i^+}.
\]
This endomorphism is positive semidefinite pointwise. The quantitative eigenvalue defect is
\[
D_{{\rm eig},i}
=
2\int \langle \mathcal W_i\psi_i,\psi_i\rangle\,d\mu_{g_i}
\to0 .
\]
On the harmonic chart,
\[
\mathcal W_i\to \mathcal W_\infty
\]
in \(L^p_{\rm loc}\), and \(\psi_i\to\psi_\infty:=-(8\pi/3)H_\infty\) strongly enough to pass the integral:
\[
\int \langle \mathcal W_\infty\psi_\infty,\psi_\infty\rangle\,d\mu_{g_\infty}=0 .
\]
Since the integrand is \(\ge0\), smooth, and \(\psi_\infty\neq0\), one obtains
\[
\mathcal W_\infty\psi_\infty=0 .
\]
Thus \(H_\infty\) spans the lowest eigenspace of \(W_\infty^+\), and
\[
\lambda_{\min}(W_\infty^+)
=
-\sqrt{\frac23}\,|W_\infty^+|
=
-\frac16 .
\]
Because \(W_\infty^+\) is trace-free and \(|W_\infty^+|=1/(2\sqrt6)\), the full spectrum is
\[
\operatorname{Spec}(W_\infty^+)
=
\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

So the regular-patch and spectral-transfer chain is rigorous, provided the diagonal regularized monopoles and the standard spinor \(L^\infty\) amplitude bound are included explicitly.

### Strongest justified theorem

For any sequence satisfying the fixed critical Ishida–LeBrun hypotheses, the absolute \(O(A\delta_i^2)\) scalar–Weyl/SW deficits, and
\[
\Vol_{g_i}B_1(p_i)\ge v>0,
\]
there exist \(\rho(v)>0\), points \(x_i\in B_{1/2}(p_i)\), harmonic charts
\[
\Phi_i:B_{2\rho}(0)\to M,
\]
a smooth Einstein metric \(g_\infty\) on \(B_\rho(0)\), and a smooth self-dual harmonic two-form \(H_\infty\) such that
\[
\Ric(g_\infty)=-g_\infty,
\qquad
|H_\infty|=\frac{3}{4\sqrt2\pi},
\]
and
\[
\operatorname{Spec}(W_\infty^+)
=
\left(-\frac16,\frac1{12},\frac1{12}\right),
\]
with \(H_\infty\) lying in the lowest eigenspace of \(W_\infty^+\).

The spectrum alone is not a local impossibility in the supplied Step 5 note; Derdziński’s two-eigenvalue mechanism is locally compatible. Any local projector obstruction must rule out precisely the Einstein patch plus the nonzero harmonic eigenform described above.

### Conditional consequence for \(\sup_p\Vol B_1(p)\)

If a valid local projector obstruction excludes the above local object on every nonempty smooth Einstein patch, then any hypothetical pinched sequence on the fixed critical manifold must satisfy
\[
\boxed{
\sup_{p\in M}\Vol_{g_i}B_1(p)\longrightarrow0 .
}
\]
Indeed, if a subsequence had \(\sup_p\Vol B_1(p)\ge v>0\), choosing such \(p_i\) would produce the forbidden regular patch. This conclusion is exactly a unit-scale collapse conclusion; by itself it does not recover the global topology or produce a global Einstein metric.