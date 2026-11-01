# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 94,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step94_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step94_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 94 correction to the Step 93 AA/BB tensor-sector calculation for the product-orbifold chirality-odd Green response. Check specifically: (1) if electric TF tensor E=(Hess f)^TF has pole amplitude 2b and norm mu(mu-2)/2, then magnetic tensor M=L_{(*df)^#}g has pole amplitude 4b and norm four times the electric norm; equivalently using (1/2)M restores amplitude 2b and the electric norm. (2) With this corrected normalization, separated-pole tensor electric and magnetic contributions cancel exactly under the Step-93 transported pole signs, so the claimed BB_NS/AA_SN coincident divergence is not intrinsic. (3) Same-pole tensor electric and magnetic contributions reinforce equally, leaving a finite AA_NS/BB_SN principal response. (4) The heat-kernel representation K_AA_NS = -1/1024 int_0^infty e^s A0(s) B2(s) ds with B2=32*pi d_x^2 p_{s/2}^{S2}(-1) is consistent with the script and gives a negative finite value in the stated Step89/91 principal normalization. Identify any remaining source/gauge/Ozuch normalizations not settled by this correction.

## Integrated Scientific Memo

# Step 94 verification memo

## Verdict

The Step 94 correction is valid **for the Step 89/91 principal product-background pairing implemented by the script**:

\[
\|M\|^2=4\|E\|^2,\qquad M=L_{(*df)^\#}g,\quad
E=(\nabla^2f)^{\mathrm{TF}}.
\]

After this relative normalization is repaired:

- separated-pole electric and magnetic tensor contributions cancel mode-by-mode;
- same-pole contributions reinforce with equal normalized weight;
- hence \(BB_{NS}=AA_{SN}=0\) in this principal sector;
- \(AA_{NS}=BB_{SN}\) remains finite and negative,
  \[
  K_{AA,NS}\approx-0.00400249866.
  \]

Thus the Step 93 coincident divergence is not intrinsic to the corrected principal AA/BB pairing. It arose because the full-Lie magnetic pole amplitude \(4b\) was divided by the electric norm instead of its four-times-larger norm.

## 1. Tensor normalization

Let \(f\) be \(L^2\)-normalized with
\[
-\Delta f=\mu f,\qquad \mu=\ell(\ell+1).
\]
On the unit \(S^2\), Bochner gives
\[
\int|\nabla^2f|^2=\mu(\mu-1).
\]
Removing the trace yields
\[
\|E\|^2
=\mu(\mu-1)-\frac{\mu^2}{2}
=\frac12\mu(\mu-2).
\]

At a point write
\[
E=\begin{pmatrix}a&c\\c&-a\end{pmatrix}.
\]
For \(X=J\nabla f\), direct differentiation gives, up to the irrelevant convention-dependent overall sign,
\[
M=L_Xg
=2\begin{pmatrix}-c&a\\a&c\end{pmatrix}.
\]
Therefore, pointwise and hence in \(L^2\),
\[
|M|^2=4|E|^2,\qquad
\|M\|^2=2\mu(\mu-2).
\]

For the normalized real \(m=2\) pole jets,
\[
\nabla^2Y_{\ell2}^{c}
=2b_\ell\begin{pmatrix}1&0\\0&-1\end{pmatrix},
\qquad
\nabla^2Y_{\ell2}^{s}
=2b_\ell\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]
so
\[
E(Y_{\ell2}^{s})_{01}=2b_\ell,\qquad
M(Y_{\ell2}^{c})_{01}=4b_\ell.
\]
Equivalently, using \(\frac12M\) gives amplitude \(2b_\ell\) and norm
\[
\left\|\frac12M\right\|^2=\frac12\mu(\mu-2),
\]
identical to the electric convention.

## 2. Separated-pole cancellation

With the transported pole signs used by Steps 93–94,
\[
\begin{array}{c|cc}
 &N&S\\ \hline
E_{01}&2b_\ell&-(-1)^\ell\,2b_\ell\\
M_{01}&4b_\ell&(+1)(-1)^\ell\,4b_\ell .
\end{array}
\]
Put
\[
N_E=\frac12\mu(\mu-2),\qquad N_M=4N_E.
\]
Then
\[
\frac{E_{01}(N)E_{01}(S)}{N_E}
=-(-1)^\ell\frac{4b_\ell^2}{N_E},
\]
whereas
\[
\frac{M_{01}(N)M_{01}(S)}{N_M}
=(+1)(-1)^\ell\frac{16b_\ell^2}{4N_E}
=(+1)(-1)^\ell\frac{4b_\ell^2}{N_E}.
\]
Their sum vanishes for every \(\ell\), before any spectral summation.

Consequently:

- \(BB_{NS}=0\), because its tensor factor is evaluated at \(N_B,S_B\);
- \(AA_{SN}=0\), because its tensor factor is evaluated at \(N_A,S_A\);
- the displayed \(SS\) principal contributions also vanish.

In Step 93 the magnetic numerator \(16b_\ell^2\) was divided by \(N_E\), leaving a nonzero residual multiplying the coincident scalar heat sum. That residual generated the apparent \(t^{-3}\), or heat-cutoff \(\tau^{-2}\), divergence. This was a **relative electric/magnetic normalization error**, not an overall normalization error.

The cancellation is invariant under rescaling \(M\), including replacing it by \(M/2\). It does, however, rely on the transported relative electric/magnetic pole sign; the supplied explicit jets support precisely the sign table above.

## 3. Same-pole reinforcement

At the same pole,
\[
\frac{E_{01}(N)^2}{N_E}
=\frac{4b_\ell^2}{N_E},
\qquad
\frac{M_{01}(N)^2}{N_M}
=\frac{16b_\ell^2}{4N_E}
=\frac{4b_\ell^2}{N_E}.
\]
Thus the two polarizations reinforce equally.

For \(NS\), the AA tensor factor is same-pole while its scalar factor is antipodally separated, leaving a finite \(AA_{NS}\). By factor exchange, the corresponding surviving term for \(SN\) is \(BB_{SN}\). The supplied heat ladder confirms
\[
K_{AA,NS}=K_{BB,SN}\approx-0.00400249866,
\]
while the separated-tensor terms are numerically exactly zero.

## 4. Heat-kernel representation and sign

Let
\[
P_{rq}=\frac{\mu_r+\mu_q}{2}-1,\qquad
b_\ell^2=\frac{(2\ell+1)\mu_\ell(\mu_\ell-2)}{128\pi}.
\]
Reduction of the corrected electric-plus-magnetic sum gives
\[
K_{AA,NS}(\tau)
=-\frac1{1024}\sum_{r,q\ge2}
\frac{(2r+1)(-1)^q(2q+1)\mu_q(\mu_q-2)}
{P_{rq}}e^{-\tau P_{rq}}.
\]
Using
\[
\frac{e^{-\tau P}}P=\int_\tau^\infty e^{-sP}\,ds
\]
yields
\[
K_{AA,NS}
=-\frac1{1024}\int_0^\infty e^sA_0(s)B_2(s)\,ds,
\]
where
\[
A_0(s)=\sum_{\ell\ge2}(2\ell+1)e^{-s\mu_\ell/2},
\]
and
\[
B_2(s)=\sum_{\ell\ge2}(-1)^\ell(2\ell+1)
\mu_\ell(\mu_\ell-2)e^{-s\mu_\ell/2}.
\]

For the mass-one zonal heat kernel,
\[
P_\ell''(-1)=(-1)^\ell\frac{\mu_\ell(\mu_\ell-2)}8,
\]
so, since the \(\ell=0,1\) terms vanish,
\[
B_2(s)=32\pi\,\partial_x^2p_{s/2}^{S^2}(-1).
\]
Dimension raising gives
\[
\partial_x^2p_t^{S^2}(x)
=4\pi^2e^{-6t}p_t^{S^6}(x),
\]
hence
\[
B_2(s)=128\pi^3e^{-3s}p_{s/2}^{S^6}(-1)>0.
\]
Since \(A_0(s)>0\),
\[
K_{AA,NS}<0.
\]

The integral is finite: as \(s\downarrow0\), \(A_0(s)=O(s^{-1})\), while the antipodal \(S^6\) kernel is exponentially suppressed; as \(s\to\infty\), the integrand decays exponentially. The spectral ladder and quadrature agree at approximately
\[
K_{AA,NS}=-0.00400249866.
\]
Near \(s=0\), the script’s direct alternating evaluation of \(B_2\) suffers cancellation; the dimension-raised \(S^6\) expression or multiprecision summation is preferable for numerical verification.

## 5. Scope and unresolved normalizations

This correction establishes the finite principal pairing
\[
\frac{\pi^2}{2}\sum_e
\frac{R_i(e)R_j(e)}{P_e\|e\|^2},
\]
not the physical Ozuch source-to-receiver coefficient
\[
\sum_e
\frac{R_i(e)\langle S_j^{\mathrm{ALE}},e\rangle}
{P_e\|e\|^2}.
\]

Still unsettled are:

1. the exact Eguchi–Hanson \(H^4\) source tensor, scale and chirality normalization;
2. its electric/magnetic and AA/BB/AB mode contractions;
3. Bianchi projection and gauge correction;
4. the Green-operator sign and derivation of the principal \(\pi^2/2\) prefactor;
5. quotient/isotropy and symmetric-product normalization;
6. ordered north/south frame transport between orbifold charts;
7. ALE-to-orbifold radial matching and the nonlinear gluing normalization.

There is also a wording ambiguity in the script: “simultaneous antipodal” should not be used unless that is literally the quotient action. The Step 93 descent rule \(m_A+m_B\) even and the four fixed pole-products instead indicate a simultaneous axial half-turn. These actions have different orientation and descent rules, so the quotient generator should be stated explicitly.

Therefore the rigorous conclusion is:

\[
\boxed{
BB_{NS}=AA_{SN}=0,\qquad
AA_{NS}=BB_{SN}\approx-0.00400249866
}
\]

in the corrected Step 89/91 principal normalization. Whether the full Ozuch coefficient has this sign remains undetermined until the ALE source and gauge contractions are fixed.