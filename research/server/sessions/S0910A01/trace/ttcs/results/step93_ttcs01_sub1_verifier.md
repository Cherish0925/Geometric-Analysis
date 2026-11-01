# TTCS Independent Branch Record

```json
{
  "step_id": 93,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/data/step93_aabb_tensor_sector_analysis.json",
    "Sessions/S0910A01/workspace/data/step93_aabb_analytic_divergence.json",
    "Sessions/S0910A01/workspace/notes/step92_route_comparison_and_ab_heat_sign.md",
    "Sessions/S0910A01/workspace/data/step91_receiver_simplification.json",
    "Sessions/S0910A01/workspace/data/step91_corrected_spectral_ledger.json"
  ]
}
```

## Task

Verify the Step 93 finding that the AA/BB trace-free tensor sectors of the product-orbifold chirality-odd Green coefficient have a coincident-point divergence that prevents independent sector-by-sector computation, while the AB sector remains finite and has a strict negative sign.

The specific claims to check:
1. For an AA mode h = phi_B(x_B) T_A(x_A) where T is a TF symmetric 2-tensor on S^2_A, the sparse odd receiver R_odd(H) = (1/2)(H_{01,23} - H_{03,12} - H_{12,03} + H_{23,01}) reduces to a single term R_odd = (1/2)(d_2 d_3 phi_B)(0) * T_{01}(0), because h has no components with tensor indices crossing factors.
2. Electric TF tensor (from scalar TF Hessian) has T_{01}(pole) != 0 only for m=2 sin modes; magnetic TF tensor (from Lie derivative of coexact 1-form) has T_{01}(pole) != 0 only for m=2 cos modes.
3. For the NS adjacent pair (receiver NN, source NS), the BB sector has the scalar factor on A evaluated at the SAME pole (N) in both source and receiver, creating a coincident-point spectral sum that diverges.
4. The divergence is characterized by the dimension-raising identity: d_x^2 p_t^{S^2}(x)|_{x=1} = 4*pi^2 * e^{-6t} * p_t^{S^6}(1), giving short-time behavior ~ 1/(16*pi*t^3).
5. By contrast, the AB sector uses d_x p_t^{S^2}(-1) = 2*pi*e^{-2t}*p_t^{S^4}(-1) which is finite for t>0, so the AB adjacent sector K_adj^AB converges and is strictly negative.
6. The implication that the full inter-node coefficient requires the ALE source normalization from Ozuch's framework and cannot be extracted from a naive sector-by-sector mode sum.

Check whether the receiver reduction for AA/BB is correct, whether the divergence diagnosis is real (not a normalization error), and whether the dimension-raising identities are applied correctly.

## Output

# Scientific verification memo

## Main finding

Items 1, 2, 4, and the analytic AB sign computation in item 5 are mathematically correct under the conventions recorded in Steps 91–93.

The Step 93 data also contain a genuine \(t^{-3}\) diagonal heat-kernel singularity and a corresponding \(\tau^{-2}\) growth in the implemented NS–BB sum. This growth cannot be removed by changing an overall harmonic normalization.

However, the supplied material does not establish that a correctly projected, localized BB source has an intrinsically divergent Green response between the distinct nodes \(NN\) and \(NS\). A proper BB source-to-receiver pairing must also contain the tensor heat kernel between \(N_B\) and \(S_B\), which is off diagonal and exponentially small as \(t\downarrow0\). The \(\tau^{-2}\) ladder therefore demonstrates that the Step 93 BB expression is not yet the complete localized ALE source pairing. It may represent an unrenormalized piece of \(H^4\), or it may omit the antipodal tensor factor.

## 1. AA/BB receiver reduction

Use product normal coordinates with indices \(0,1\) on \(S_A^2\) and \(2,3\) on \(S_B^2\). For

\[
h=\phi_B\,T_A,
\]

the only nonzero components of \(h\) have both tensor indices in \(A\). Hence

\[
h_{03}=h_{12}=h_{23}=0,
\qquad
h_{01}=\phi_B T_{01}.
\]

The product connection preserves the \(A/B\) splitting, so at the node

\[
H_{01,23}
 =\nabla_2\nabla_3 h_{01}
 =(\nabla_2\nabla_3\phi_B)\,T_{01}.
\]

The other three entries in the sparse receiver vanish identically. Therefore

\[
R_{\mathrm{odd}}(h)
 =\frac12(\nabla_2\nabla_3\phi_B)(0)\,T_{01}(0).
\]

Likewise, for \(h=\phi_A T_B\),

\[
R_{\mathrm{odd}}(h)
 =\frac12(\nabla_0\nabla_1\phi_A)(0)\,T_{23}(0).
\]

This uses the Step 91 result that the chirality-odd linear response is exactly the displayed second-jet functional and that frame or background-curvature variations add nothing in this component.

## 2. Pole selection for electric and magnetic TF tensors

Let \(u,v\) be oriented geodesic coordinates at a pole. An \(m=2\) scalar harmonic has leading terms

\[
Y_{\ell 2}^{c}=a_\ell(u^2-v^2)+O(r^3),
\qquad
Y_{\ell 2}^{s}=2a_\ell uv+O(r^3).
\]

Writing

\[
C=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
S=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

their Hessians are proportional to \(C\) and \(S\), respectively.

For the electric tensor

\[
E(f)=(\nabla^2f)^{\mathrm{TF}},
\]

the \(01\) component is therefore zero for the cosine mode and nonzero for the sine mode. Modes with \(m=0\) have isotropic pole Hessian, while \(m=1\) and \(m>2\) have zero second jet of the required type. Thus

\[
E(Y_{\ell m})_{01}(N)\ne0
\quad\Longleftrightarrow\quad
m=2\text{ sine},
\]

up to the chosen azimuthal phase.

For the magnetic tensor obtained from \(\alpha=*df\),

\[
M(f)=\operatorname{sym}\nabla\alpha,
\]

the derivative matrix is obtained by applying the complex structure \(J\) to the scalar Hessian. Since

\[
JC=S,\qquad JS=-C,
\]

the \(m=2\) cosine mode gives an off-diagonal tensor, while the sine mode gives a diagonal tensor. Hence

\[
M(Y_{\ell m})_{01}(N)\ne0
\quad\Longleftrightarrow\quad
m=2\text{ cosine}.
\]

The cosine/sine names may exchange under a rotated pole frame, but the complementary electric/magnetic selection is invariant.

## 3. What the NS–BB divergence establishes

For receiver \(q=(N_A,N_B)\) and source \(p=(N_A,S_B)\), the BB scalar factor is indeed evaluated at the same \(A\)-pole at both ends. Its mixed-Hessian shell sum is proportional to

\[
\left.\partial_x^2p_t^{S^2}(x)\right|_{x=1}.
\]

At each \(t>0\) this is finite, but it grows as \(t^{-3}\) as \(t\downarrow0\). Integrating such a factor from \(\tau\) produces \(\tau^{-2}\) growth. The Step 93 ladder displays exactly this behavior:

\[
\begin{aligned}
0.02^2 K_{BB}(0.02)&\simeq0.004562,\\
0.01^2 K_{BB}(0.01)&\simeq0.004655,\\
0.005^2 K_{BB}(0.005)&\simeq0.004702.
\end{aligned}
\]

Thus the divergence in the implemented expression is numerically and analytically real.

There is, however, an important distinction. The nodes \(NN\) and \(NS\) are separated in the \(B\)-factor. A complete localized BB pairing should schematically contain

\[
\int_0^\infty
\mathcal H_A(N_A,N_A;t)\,
\mathcal T_B(N_B,S_B;t)\,dt,
\]

where \(\mathcal H_A\) carries the diagonal mixed-Hessian singularity and \(\mathcal T_B\) is a tensor heat kernel evaluated at antipodal points. For a Laplace-type tensor operator,

\[
\mathcal T_B(N_B,S_B;t)
 =O\!\left(t^{-N}e^{-c/t}\right)
\]

for some \(c>0\). This exponential factor makes the product integrable despite any polynomial diagonal factor.

The expected antipodal parity supports this point. If \(a:S^2\to S^2\) is the antipodal map, then

\[
a^*E(Y_{\ell m})=(-1)^\ell E(Y_{\ell m}),
\]

while orientation reversal introduces one additional fixed sign for the magnetic construction:

\[
a^*M(Y_{\ell m})=(-1)^{\ell+1}M(Y_{\ell m}).
\]

Both families still alternate with \(\ell\), producing the off-diagonal heat-kernel suppression. The different fixed signs also explain why electric and magnetic entries can differ at an antipodal source.

Consequently, the Step 93 result should be read pairwise and formula-specifically:

- NS: the displayed AA sum is finite and the displayed BB sum grows like \(\tau^{-2}\);
- SN: the roles reverse;
- SS: both displayed sums are finite.

The broad statement that AA/BB Green sectors themselves diverge is not established by the supplied formulas. What is established is that the present AA/BB source normalization yields a diagonal subfactor without the complete antipodal tensor pairing.

## 4. Dimension-raising identities

With heat kernels normalized to have total mass one and with \(\Delta\) having eigenvalues \(-\ell(\ell+d-1)\), the standard identity is

\[
\partial_xp_t^{S^d}(x)
 =2\pi e^{-dt}p_t^{S^{d+2}}(x).
\]

Applying it twice from \(d=2\) gives

\[
\partial_x^2p_t^{S^2}(x)
 =4\pi^2e^{-6t}p_t^{S^6}(x).
\]

At the diagonal,

\[
p_t^{S^6}(1)\sim(4\pi t)^{-3},
\]

and hence

\[
\left.\partial_x^2p_t^{S^2}(x)\right|_{x=1}
\sim
4\pi^2(4\pi t)^{-3}
=
\frac{1}{16\pi t^3}.
\]

The Step 93 numerical values reproduce the exact identity to roughly \(10^{-15}\). Their ratios to \(1/(16\pi t^3)\) approach one as \(t\downarrow0\), with the recorded sequence \(0.90008,0.95001,0.98000,0.99000,\ldots\). The power \(t^{-3}\) is therefore not an artifact of an overall mode normalization.

## 5. AB convergence and strict sign

The displayed AB representation is

\[
K_\tau^{AB}
 =\frac1{512}\int_\tau^\infty e^sA(s)B(s)\,ds,
\]

where

\[
A(s)=\sum_{\ell\ge1}(2\ell+1)\mu_\ell e^{-s\mu_\ell/2}>0
\]

and

\[
B(s)=\sum_{\ell\ge1}(-1)^\ell(2\ell+1)\mu_\ell
e^{-s\mu_\ell/2}.
\]

Since

\[
p_t^{S^2}(-1)
 =\frac1{4\pi}\sum_{\ell\ge0}(2\ell+1)(-1)^\ell e^{-t\mu_\ell},
\]

one has

\[
B(s)
 =-4\pi\,\partial_t p_t^{S^2}(-1)\big|_{t=s/2}.
\]

For a zonal function,

\[
\Delta=(1-x^2)\partial_x^2-2x\partial_x.
\]

At \(x=-1\),

\[
\partial_t p_t^{S^2}(-1)
 =2\partial_xp_t^{S^2}(-1)
 =4\pi e^{-2t}p_t^{S^4}(-1)>0.
\]

Therefore

\[
B(s)=-16\pi^2e^{-s}p_{s/2}^{S^4}(-1)<0
\]

and

\[
K_\tau^{AB}
 =-\frac{\pi^2}{32}
 \int_\tau^\infty A(s)p_{s/2}^{S^4}(-1)\,ds<0.
\]

As \(s\downarrow0\), the antipodal \(S^4\) heat kernel has exponential off-diagonal decay, which dominates the polynomial growth \(A(s)=O(s^{-2})\). As \(s\to\infty\),

\[
A(s)=6e^{-s}+O(e^{-3s}),
\]

while \(p_{s/2}^{S^4}(-1)\) tends to its constant mode. The improper integral is therefore finite and strictly below zero.

This verifies the Step 92/93 AB subseries, including its sign. It does not by itself fix the sign of an Ozuch-normalized full coefficient, since an unprovided ALE source pairing could introduce an overall factor or mix further tensor components.

## 6. Role of the ALE source

The receiver functional determines only how a global tensor perturbation is read at a node. A Green coefficient additionally requires the source-mode pairings

\[
\langle S_{\mathrm{ALE}},e_{\ell m}\rangle,
\]

together with the \(H^4\) singular tensor, Bianchi/gauge projection, quotient measure, symmetric-product convention, and any finite-part extension of nonintegrable local terms.

None of those source formulas is present in the supplied Step 93 artifacts. The generating script for the AA/BB ladder is also absent, so its asymptotic scaling can be assessed, but its source contraction cannot be inspected line by line.

Two mathematically different situations remain compatible with the data:

1. the complete localized source supplies the missing antipodal tensor factor, making each properly defined inter-node sector finite; or  
2. isolated AA/BB pieces of \(H^4\) do not define distributions separately, and only their prescribed combination has a finite Green response.

Both situations require the actual ALE source structure. Thus the naive AA/BB mode sum cannot be identified with the physical inter-node coefficient, while the diagonal \(t^{-3}\) calculation remains a correct and useful description of the incomplete expression.