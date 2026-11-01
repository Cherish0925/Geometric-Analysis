# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 93,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step93_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step93_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 93 finding that the AA/BB trace-free tensor sectors of the product-orbifold chirality-odd Green coefficient have a coincident-point divergence that prevents independent sector-by-sector computation, while the AB sector remains finite and has a strict negative sign.

The specific claims to check:
1. For an AA mode h = phi_B(x_B) T_A(x_A) where T is a TF symmetric 2-tensor on S^2_A, the sparse odd receiver R_odd(H) = (1/2)(H_{01,23} - H_{03,12} - H_{12,03} + H_{23,01}) reduces to a single term R_odd = (1/2)(d_2 d_3 phi_B)(0) * T_{01}(0), because h has no components with tensor indices crossing factors.
2. Electric TF tensor (from scalar TF Hessian) has T_{01}(pole) != 0 only for m=2 sin modes; magnetic TF tensor (from Lie derivative of coexact 1-form) has T_{01}(pole) != 0 only for m=2 cos modes.
3. For the NS adjacent pair (receiver NN, source NS), the BB sector has the scalar factor on A evaluated at the SAME pole (N) in both source and receiver, creating a coincident-point spectral sum that diverges.
4. The divergence is characterized by the dimension-raising identity: d_x^2 p_t^{S^2}(x)|_{x=1} = 4*pi^2 * e^{-6t} * p_t^{S^6}(1), giving short-time behavior ~ 1/(16*pi*t^3).
5. By contrast, the AB sector uses d_x p_t^{S^2}(-1) = 2*pi*e^{-2t}*p_t^{S^4}(-1) which is finite for t>0, so the AB adjacent sector K_adj^AB converges and is strictly negative.
6. The implication that the full inter-node coefficient requires the ALE source normalization from Ozuch's framework and cannot be extracted from a naive sector-by-sector mode sum.

Check whether the receiver reduction for AA/BB is correct, whether the divergence diagnosis is real (not a normalization error), and whether the dimension-raising identities are applied correctly.

## Integrated Scientific Memo

# Step 93 verification memo

## Verdict

The following are verified:

1. The AA/BB sparse-receiver reductions are correct.
2. The electric/magnetic \(m=2\) pole-selection rules are correct, modulo the conventional choice of pole frame and sine/cosine phase.
3. The Step 93 **implemented** NS–BB expression genuinely contains a coincident-point \(t^{-3}\) heat-kernel singularity and grows as \(\tau^{-2}\); this is not removable by an overall normalization change.
4. Both dimension-raising identities and the coefficient \(1/(16\pi t^3)\) are correct.
5. The Step 92 AB subseries converges and is strictly negative in its stated principal normalization.

A qualification is essential for claims 3 and 6: the supplied material does **not** prove that a correctly localized AA or BB inter-node Green sector is intrinsically divergent. Since \(NN\) and \(NS\) are distinct points, a complete localized BB source-to-receiver pairing should also retain off-diagonal propagation in the \(B\)-tensor factor, which may supply exponential short-time suppression. Thus Step 93 proves that the naive/incomplete AA/BB sector formula is divergent and cannot be identified with the physical coefficient. Determining whether the properly defined AA/BB pieces are separately finite, or only their ALE-prescribed combination is meaningful, requires Ozuch’s actual \(H^4\) source and gauge projection.

## 1. AA/BB receiver reduction

Use product normal coordinates, with \(0,1\) tangent to \(S_A^2\) and \(2,3\) tangent to \(S_B^2\). For
\[
h=\phi_B\,T_A,
\]
all components except those with both tensor indices in \(A\) vanish. Therefore
\[
h_{03}=h_{12}=h_{23}=0,\qquad h_{01}=\phi_B T_{01}.
\]
The product connection preserves the factor splitting, so at the node
\[
H_{01,23}
 =\nabla_2\nabla_3h_{01}
 =(\nabla_2\nabla_3\phi_B)\,T_{01}.
\]
Consequently,
\[
R_{\rm odd}(h)
 =\frac12(\nabla_2\nabla_3\phi_B)(0)\,T_{01}(0).
\]
The other three sparse-receiver terms vanish because they require \(h_{03}\), \(h_{12}\), or \(h_{23}\).

Likewise, for \(h=\phi_A T_B\),
\[
R_{\rm odd}(h)
 =\frac12(\nabla_0\nabla_1\phi_A)(0)\,T_{23}(0).
\]
This uses the Step 91 result that frame, Hodge-splitting, normalization, and background-curvature variations contribute no additional term to this odd linear receiver.

## 2. Electric and magnetic pole selection

In oriented geodesic coordinates \((u,v)\) at a pole, real \(m=2\) scalar harmonics have leading jets
\[
Y_{\ell2}^{c}=a_\ell(u^2-v^2)+O(r^3),\qquad
Y_{\ell2}^{s}=2a_\ell uv+O(r^3).
\]
Their Hessians are proportional respectively to
\[
C=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
S=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

For the electric tensor
\[
E(f)=(\nabla^2f)^{\rm TF},
\]
trace removal changes only diagonal entries, hence \(E(f)_{01}\neq0\) precisely for the sine \(m=2\) polarization.

For the magnetic tensor constructed from \(\alpha=*df\),
\[
M(f)=\operatorname{sym}\nabla\alpha,
\]
the relevant derivative matrix is obtained by applying the complex structure \(J\):
\[
JC=S,\qquad JS=-C.
\]
Thus the cosine \(m=2\) mode gives the off-diagonal component, while the sine mode gives a diagonal tensor:
\[
E(Y_{\ell m})_{01}\neq0
 \iff m=2\text{ sine},\qquad
M(Y_{\ell m})_{01}\neq0
 \iff m=2\text{ cosine}.
\]
A rotation of the pole frame can interchange the labels “sine” and “cosine”; the invariant statement is that the electric and magnetic tensors select complementary \(m=2\) polarizations.

## 3. What the NS–BB divergence proves

For receiver \(NN=(N_A,N_B)\) and source \(NS=(N_A,S_B)\), the BB receiver differentiates the scalar \(A\)-factor. The Step 93 expression evaluates that scalar factor at \(N_A\) at both ends, producing the diagonal shell sum
\[
\left.\partial_x^2p_t^{S^2}(x)\right|_{x=1}.
\]
Its \(t^{-3}\) short-time growth yields \(\tau^{-2}\) growth after the Green-time integration. The numerical ladder confirms this:
\[
K_{BB}(0.01)=46.5503,\qquad
K_{BB}(0.005)=188.0833,
\]
approximately quadrupling when \(\tau\) is halved. More directly,
\[
\tau^2K_{BB}(\tau)
\]
approaches a nonzero constant over the displayed range. Under \(A\leftrightarrow B\), the divergence moves from BB in the NS pair to AA in the SN pair, while both displayed sectors are finite for SS. This geometric pattern rules out a uniform overall-normalization explanation.

Nevertheless, it is too strong to conclude from this alone that the **correct localized BB inter-node sector** diverges. A complete BB pairing between \(NN\) and \(NS\) should schematically involve
\[
\int_0^\infty
\mathcal H_A(N_A,N_A;t)\,
\mathcal T_B(N_B,S_B;t)\,dt,
\]
where \(\mathcal H_A\) is the diagonal differentiated scalar kernel but \(\mathcal T_B\) is an off-diagonal tensor kernel. For a Laplace-type operator at separated points,
\[
\mathcal T_B(N_B,S_B;t)
 =O(t^{-N}e^{-c/t}),
\]
which defeats every polynomial diagonal singularity. The alternating tensor-harmonic parity at antipodal points is the spectral manifestation of this suppression.

Therefore, Step 93 establishes precisely:

- the naive NS–BB formula contains a genuine coincident-factor divergence;
- it cannot be assigned an independent physical value by the displayed sector-by-sector summation;
- the supplied formulas do not decide whether a correctly sourced BB sector is finite by itself or only after combining ALE-prescribed components.

## 4. Dimension raising and asymptotics

With mass-one spherical heat kernels and Laplacian eigenvalues
\[
-\ell(\ell+d-1),
\]
the dimension-raising identity is
\[
\partial_xp_t^{S^d}(x)
 =2\pi e^{-dt}p_t^{S^{d+2}}(x).
\]
Applying it twice gives
\[
\partial_x^2p_t^{S^2}(x)
 =4\pi^2e^{-6t}p_t^{S^6}(x).
\]
At \(x=1\),
\[
p_t^{S^6}(1)\sim(4\pi t)^{-3},
\]
hence
\[
\left.\partial_x^2p_t^{S^2}(x)\right|_{x=1}
 \sim4\pi^2(4\pi t)^{-3}
 =\frac1{16\pi t^3}.
\]
The numerical values in the source agree with the identity to machine precision and approach this asymptotic coefficient. Thus the power and coefficient are correct and cannot be altered away by a constant harmonic normalization.

The first-derivative identity used for AB is likewise
\[
\partial_xp_t^{S^2}(x)
 =2\pi e^{-2t}p_t^{S^4}(x).
\]

## 5. AB convergence and strict negative sign

After the exact \(m=2\) polarization cancellation, the residual AB expression is
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
\[
B(s)=-4\pi\,
\partial_t p_t^{S^2}(-1)\big|_{t=s/2}.
\]
For a zonal function on \(S^2\),
\[
\Delta=(1-x^2)\partial_x^2-2x\partial_x,
\]
so at \(x=-1\),
\[
\partial_t p_t^{S^2}(-1)
 =2\partial_xp_t^{S^2}(-1)
 =4\pi e^{-2t}p_t^{S^4}(-1)>0.
\]
Therefore
\[
B(s)=-16\pi^2e^{-s}p_{s/2}^{S^4}(-1)<0,
\]
and
\[
K_\tau^{AB}
 =-\frac{\pi^2}{32}
 \int_\tau^\infty A(s)p_{s/2}^{S^4}(-1)\,ds<0.
\]

At \(s\downarrow0\), the antipodal heat kernel is exponentially small and dominates the polynomial growth \(A(s)=O(s^{-2})\). At infinity,
\[
A(s)=6e^{-s}+O(e^{-3s}),
\]
while the \(S^4\) kernel tends to its constant mode. Hence
\[
K_{\rm adj}^{AB}=\lim_{\tau\downarrow0}K_\tau^{AB}
\]
exists and is strictly negative in the stated principal normalization.

This proves the sign of that AB subseries, not automatically the sign of the Ozuch-normalized total coefficient: source contraction could change the overall convention and the regulated AA/BB pieces have unknown relative weights.

## 6. Required ALE input

The receiver alone does not determine a Green coefficient. One also needs the source-mode contractions
\[
\langle S_{\rm ALE},e_{\ell m}\rangle,
\]
including:

- the actual \(H^4\) singular tensor;
- Bianchi/gauge projection;
- quotient and isotropy normalization;
- the symmetric-product convention;
- and any prescribed finite-part combination of individually nonintegrable terms.

None of these source formulas is supplied here. Accordingly, the strongest justified implication is:

> The naive AA/BB mode sums cannot be used as independent physical inter-node coefficients. Ozuch’s localized ALE source structure is required to determine whether the missing off-diagonal tensor propagation renders each sector finite, or whether only a prescribed combined/renormalized AA/BB expression is defined.

The unresolved scientific object is the Ozuch-normalized AA/BB source-to-receiver pairing. Its computation is necessary to determine the full adjacent coefficient and its sign.