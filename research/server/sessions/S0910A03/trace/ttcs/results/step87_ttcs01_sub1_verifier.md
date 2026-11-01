# TTCS Independent Branch Record

```json
{
  "step_id": 87,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step85_bochner_comparison_theorem.md",
    "Sessions/S0910A03/workspace/notes/step86_forced_bochner_superlevel_and_localization.md",
    "Sessions/S0910A03/workspace/data/step87_resolvent_comparison.json"
  ]
}
```

## Task

Verify the following forced reflected OT connector obstruction theorem. The setting: a complete 2D smooth weighted base (B², γ_B, dμ = e^σ dA) with σ-harmonic map U: B → H² (hyperbolic plane), orbit energy e = |dU|²_{H²}, weighted tension F = τ_σ(U), and the Einstein base equation gives Ric_f^4 = Ric_B - Hess σ - ½dσ⊗dσ ≥ -(3+δ)γ_B (finite-dimensional CD condition with N=4).

The argument chain:

1. FORCED BOCHNER (from Steps 85-86): ½Le ≥ |DdU|² + div_σ V - |F|² + ½e² - (3+δ)e, where V(X) = ⟨dU(X), F⟩, |V| ≤ |F|√e ≤ 2δ√e. Drop |DdU|² ≥ 0.

2. MASSIVE COMPARISON: With κ = 6+2δ = 2(3+δ), rearrange to get (-L+κ)e ≤ κ² + 2(2δ)² - 2div_σ V. Key step: 2κe - e² ≤ κ² (completing the square).

3. LI-YAU FISHER INFORMATION: On a complete smooth weighted manifold with CD(-K,N) [Ric_f^N ≥ -K], the heat kernel p_t of L satisfies the Li-Yau gradient estimate, hence I(t) := ∫ p_t |∇_y log p_t|² dμ ≤ N/(2t) + NK/2. By Cauchy-Schwarz and heat conservation ∫p_t dμ = 1: ∫|∇_y p_t(x,y)| dμ(y) ≤ √I(t) ≤ √(N/(2t) + NK/2).

4. RESOLVENT ESTIMATE: C_κ = sup_x ∫|∇_y G_κ(x,y)| dμ(y) ≤ ∫_0^∞ e^{-κt} √(N/(2t)+NK/2) dt = √(2πN/(2κ)) + √(NK/2)/κ. With N=4, K=3+δ: C_κ ≤ √(2π/κ) + √(2(3+δ))/κ.

5. COMPARISON PRINCIPLE: Since -L+κ has strictly positive potential (κ>0) on a complete manifold, if (-L+κ)(ψ-e) ≥ 0 and ψ-e is bounded below, then ψ-e ≥ 0 (Omori-Yau). Define ψ by (-L+κ)ψ = κ²+8δ²-2div_σ V. Then ψ = (κ²+8δ²)/κ + ψ_2 where |ψ_2| ≤ 2C_κ·2δ·√B (B=sup e). So B ≤ κ+8δ²/κ + 4δC_κ√B.

6. QUADRATIC CLOSURE: B ≤ α + β√B with α = κ+8δ²/κ, β = 4δC_κ. Solution: B ≤ (β/2+√(β²/4+α))². CENTER FLOOR: ⟨e(0,·)⟩_μ ≥ 12-8δ (from reflected center Gauss equation with defect). For δ < δ₀ ≈ 0.249, the ceiling B(δ) < 12-8δ = floor. Contradiction.

Verify each step. Particular attention to: (a) Is the Li-Yau Fisher information bound I(t) ≤ N/(2t)+NK/2 correct under CD(-K,N) with N > dim M? What is the standard reference? (b) Is stochastic completeness (∫p_t dμ = 1) guaranteed under CD(-(3+δ),4) on our complete weighted manifold? (c) Is the integration by parts for R_κ[div_σ V] justified when V vanishes at infinity? (d) Does the Omori-Yau maximum principle apply to -L+κ on this specific complete manifold (exponential weighted volume growth)? (e) Is the center floor 12-8δ correctly derived from the Gauss equation? Check all sign conventions.

## Output

# Scientific verification memo

## Overall result

Steps 1, 2, 5, and 6 are mathematically consistent once boundedness of \(e\), geodesic completeness, and the full four-dimensional defect estimate \(\|E\|_{\mathrm{op}}\le \delta\) are included.

The Fisher-information estimate in Step 3 is incorrect. Consequently, the numerical universal threshold \(0.24885\) in the supplied JSON does not follow from this argument. Replacing Steps 3–4 by the standard \(CD(-K,N)\) entropy estimate preserves the obstruction and gives the rigorous threshold

\[
\boxed{\delta<\delta_* \simeq 0.246250.}
\]

The listed value \(0.214212\), computed using a larger resolvent coefficient, is also supported.

---

## 1. Forced Bochner formula and massive comparison

Put \(f=-\sigma\). Then

\[
L=\Delta-\langle\nabla f,\nabla\cdot\rangle
=\Delta+\langle\nabla\sigma,\nabla\cdot\rangle .
\]

The finite-dimensional tensor is

\[
\operatorname{Ric}^{4}_{f}
=\operatorname{Ric}_B-\operatorname{Hess}\sigma
-\frac12d\sigma\otimes d\sigma.
\]

Using the base equation,

\[
\operatorname{Ric}^{4}_{f}
=-3\gamma_B+\frac12U^*h_{\mathbb H^2}+E_B
\ge -(3+\delta)\gamma_B.
\]

For \(V(X)=\langle dU(X),F\rangle\),

\[
\operatorname{div}_{\sigma}V
=|F|^2+\langle dU,DF\rangle,
\]

so the sign in

\[
\langle dU,DF\rangle
=\operatorname{div}_{\sigma}V-|F|^2
\]

is correct. The curvature of \(\mathbb H^2\), with the normalization used in Steps 85–86, gives

\[
Q(A)=\frac12e^2+\det A\ge \frac12e^2.
\]

Thus

\[
\frac12Le\ge
|DdU|^2+\operatorname{div}_{\sigma}V-|F|^2
+\frac12e^2-(3+\delta)e.
\]

The vertical defect equation gives \(|F|\le2\delta\), while

\[
|V|\le |F|\sqrt e\le2\delta\sqrt e.
\]

Dropping \(|DdU|^2\) and setting

\[
K=3+\delta,\qquad \kappa=2K=6+2\delta,\qquad f_0=2\delta,
\]

gives

\[
(-L+\kappa)e
\le \kappa^2+2f_0^2-2\operatorname{div}_{\sigma}V,
\]

because

\[
2\kappa e-e^2=\kappa^2-(e-\kappa)^2\le\kappa^2.
\]

These two steps are correct.

---

## 2. The proposed Fisher estimate is incorrect

The asserted estimate

\[
I(t)\le \frac{N}{2t}+\frac{NK}{2}
\tag{A}
\]

does not hold for general \(CD(-K,N)\) spaces.

### Explicit counterexample from the round cusp

For the supplied benchmark

\[
\gamma_B=dr^2+e^{2r}dz^2,\qquad \sigma=2r,
\]

one has

\[
d\mu=e^{3r}dr\,dz,\qquad
L=\partial_{rr}+3\partial_r+e^{-2r}\partial_{zz}.
\]

The tensor identities are

\[
\operatorname{Ric}_B-\operatorname{Hess}\sigma
=\operatorname{diag}(-1,-3),
\]

but after the finite-\(N\) correction,

\[
\boxed{\operatorname{Ric}^{4}_{f}=-3\gamma_B.}
\]

Thus the JSON entry identifying \(\operatorname{Ric}^{4}_{f}\) with
\(\operatorname{diag}(-1,-3)\) omits the term
\(-\tfrac12d\sigma^2\).

For radial functions, \(L=\partial_{rr}+3\partial_r\). Starting at \(r_0\), the radial Lebesgue density is Gaussian with mean \(r_0+3t\) and variance \(2t\). Its density relative to \(e^{3r}dr\) has Fisher information

\[
9+\frac1{2t}.
\]

Marginalization cannot increase Fisher information, so the full heat kernel satisfies

\[
I(t)\ge 9+\frac1{2t}.
\]

For \(N=4\), \(K=3\), formula (A) would give

\[
I(t)\le \frac2t+6,
\]

which is incompatible with the preceding lower estimate whenever \(t>1/2\).

---

## 3. Correct \(CD(-K,N)\) Fisher estimate

Let \(p_t(x,\cdot)\) be the heat kernel and

\[
I(t)=\int p_t\,|\nabla\log p_t|^2\,d\mu.
\]

Entropy dissipation and the \(\Gamma_2\) identity give

\[
I'(t)=-2\int p_t\,\Gamma_2(\log p_t)\,d\mu.
\]

Under \(CD(-K,N)\),

\[
\Gamma_2(\phi)\ge -K\Gamma(\phi)+\frac1N(L\phi)^2.
\]

Also,

\[
\int p_tL\log p_t\,d\mu=-I(t),
\]

and hence Jensen’s inequality gives

\[
\int p_t(L\log p_t)^2\,d\mu\ge I(t)^2.
\]

Therefore

\[
I'(t)\le 2KI(t)-\frac2N I(t)^2.
\]

Comparison with the singular Riccati solution yields

\[
\boxed{
I(t)\le \frac{NK}{1-e^{-2Kt}}
=\frac{NK}{2}\bigl(\coth(Kt)+1\bigr).
}
\tag{B}
\]

The expression in Step 3 is only the first two terms of the small-\(t\) expansion of (B):

\[
\frac{NK}{1-e^{-2Kt}}
=\frac{N}{2t}+\frac{NK}{2}+O(t).
\]

Standard references for this finite-dimensional Bakry–Émery heat-semigroup theory include:

- Bakry–Qian, *Revista Matemática Iberoamericana* **15** (1999), 143–179.
- Bakry–Gentil–Ledoux, *Analysis and Geometry of Markov Diffusion Operators*, Springer, 2014.

---

## 4. Stochastic completeness

For a geodesically complete smooth weighted manifold with finite \(N>n\) and

\[
\operatorname{Ric}^{N}_{f}\ge-Kg,
\]

weighted Bishop comparison gives at most exponential weighted-volume growth,

\[
\mu(B_R(x))\le C_x e^{\sqrt{(N-1)K}\,R}
\]

for large \(R\). Consequently,

\[
\int^\infty \frac{R}{\log\mu(B_R(x))}\,dR=\infty,
\]

which implies nonexplosion of the weighted diffusion. Thus the minimal heat kernel is conservative:

\[
\boxed{\int_B p_t(x,y)\,d\mu(y)=1.}
\]

This applies to the complete doubled connector and to the round-cusp benchmark. Qian’s weighted-volume comparison results, together with the standard Grigor’yan volume test, provide the usual reference route.

---

## 5. Correct resolvent gradient estimate

From conservation and Cauchy–Schwarz,

\[
\int |\nabla_y p_t(x,y)|\,d\mu(y)
\le \sqrt{I(t)}.
\]

Combining this with (B),

\[
C_\kappa
:=\sup_x\int|\nabla_yG_\kappa(x,y)|\,d\mu(y)
\le
\int_0^\infty
e^{-\kappa t}
\sqrt{\frac{NK}{1-e^{-2Kt}}}\,dt.
\]

The integral is explicit:

\[
\boxed{
C_\kappa
\le
\frac{\sqrt{NK}}{2K}
\operatorname B\!\left(\frac{\kappa}{2K},\frac12\right).
}
\]

Here \(\kappa=2K\), so \(\operatorname B(1,\tfrac12)=2\), and therefore

\[
\boxed{
C_\kappa\le\sqrt{\frac NK}
=\frac{2}{\sqrt{3+\delta}}.
}
\tag{C}
\]

Two additional arithmetic points about the original Step 4:

1. Even if its Fisher estimate were available, one would use
   \(\sqrt{a+b}\le\sqrt a+\sqrt b\), not equality.
2. The first separated integral is
   \[
   \int_0^\infty e^{-\kappa t}\sqrt{\frac{N}{2t}}\,dt
   =\sqrt{\frac{\pi N}{2\kappa}}.
   \]

The numerical value \(1.13518\) in the JSON comes from integrating the incorrect Fisher expression. At \(\delta=0\), the valid universal value from (C) is \(2/\sqrt3\simeq1.15470\).

---

## 6. Resolvent integration by parts and comparison

Let \(G_\kappa\) be the massive Green kernel. For smooth bounded \(V\), compactly supported cutoffs \(\chi_R\) give

\[
\int \chi_RG_\kappa\,\operatorname{div}_\sigma V\,d\mu
=
-\int\chi_R\langle\nabla G_\kappa,V\rangle\,d\mu
-\int G_\kappa\langle\nabla\chi_R,V\rangle\,d\mu.
\]

Since

\[
\int G_\kappa\,d\mu=\frac1\kappa,\qquad
|\nabla\chi_R|\le \frac{C}{R},
\]

the last term tends to zero. Moreover,

\[
\int|\nabla G_\kappa|\,|V|\,d\mu
\le C_\kappa\|V\|_\infty.
\]

Thus, distributionally and then by local elliptic regularity,

\[
R_\kappa[\operatorname{div}_\sigma V](x)
=
-\int\langle\nabla_yG_\kappa(x,y),V(y)\rangle\,d\mu(y).
\]

The assumption \(e\to0\) at every end implies \(e\in L^\infty\) and
\(V\to0\), although boundedness of \(V\) already suffices for the cutoff argument.

The comparison principle is also available. Finite-dimensional \(CD(-K,N)\) gives weighted Laplacian comparison and the weighted Omori–Yau principle. Exponential weighted-volume growth causes no problem.

A direct semigroup proof avoids any regularity concern. If

\[
(-L+\kappa)e\le S
\]

and \(e\) is bounded, then

\[
e\le e^{-\kappa T}P_Te+\int_0^T e^{-\kappa t}P_tS\,dt.
\]

Letting \(T\to\infty\) yields \(e\le R_\kappa S\). Therefore

\[
B:=\sup e
\le
\kappa+\frac{8\delta^2}{\kappa}
+4\delta C_\kappa\sqrt B.
\]

So Step 5 is valid after replacing \(C_\kappa\) by a justified estimate.

---

## 7. Center floor and signs

Let \(\Sigma\) be the totally geodesic reflected center and

\[
E=\operatorname{Ric}_g+3g,\qquad \|E\|_{\mathrm{op}}\le\delta.
\]

For its unit normal \(\nu\), the Gauss equation gives

\[
R_\Sigma=R_g-2\operatorname{Ric}_g(\nu,\nu)
=-6+\operatorname{tr}E-2E(\nu,\nu).
\]

Writing

\[
D=\operatorname{tr}E-2E(\nu,\nu)
=\sum_{a=1}^{3}E(e_a,e_a)-E(\nu,\nu),
\]

one has

\[
|D|\le4\delta.
\]

On the center,

\[
q=ds^2+G_{ab}(s)d\xi^ad\xi^b,\qquad
G=e^\sigma M,\qquad \rho=e^\sigma.
\]

With \(h=\sigma_s=(\log\rho)_s\) and the stated target normalization,

\[
R_\Sigma=-2h_s-\frac32h^2-\frac12e.
\]

Weighted integration around the center circle uses
\(\rho_s=\rho h\), hence

\[
\langle R_\Sigma\rangle_\mu
=\frac12\langle h^2-e\rangle_\mu.
\]

It follows that

\[
\langle e\rangle_\mu
=
12-2\langle D\rangle_\mu+\langle h^2\rangle_\mu
\ge 12-8\delta.
\]

Thus

\[
\boxed{\langle e(0,\cdot)\rangle_\mu\ge12-8\delta}
\]

has the correct sign and coefficient. With \(\rho=e^\sigma\), the center variable is \(h=\sigma_s\); the phrase \(h=\sigma_s/2\) appearing once in Step 85 is a notation typo.

The floor uses the four-dimensional Gauss equation and the full estimate on \(E\); it is not implied by the abstract \(CD(-K,4)\) condition alone.

---

## 8. Corrected numerical threshold

Using (C), with \(K=3+\delta\),

\[
\alpha=2K+\frac{4\delta^2}{K},
\qquad
\beta=\frac{8\delta}{\sqrt K}.
\]

Hence

\[
B\le
\mathcal B(\delta):=
\left(
\frac{4\delta}{\sqrt{3+\delta}}
+
\sqrt{
2(3+\delta)+\frac{20\delta^2}{3+\delta}
}
\right)^2.
\]

The equation

\[
\mathcal B(\delta)=12-8\delta
\]

is equivalently

\[
9-12\delta-7\delta^2
=
8\delta\sqrt{(3+\delta)(3-2\delta)}.
\]

Its first positive root is

\[
\boxed{\delta_*\simeq0.246250.}
\]

Therefore a complete reflected free-OT connector satisfying the stated coupled equations, \(\|E\|_{\mathrm{op}}\le\delta\), and bounded orbit energy cannot exist for

\[
\boxed{0\le\delta<0.246250.}
\]

The value \(0.24885\) is not obtained from a valid universal Fisher estimate. The JSON value \(0.214212\), computed with the larger coefficient
\((\sqrt\pi+1/\sqrt2)/\sqrt K\), remains supported because that coefficient exceeds the valid estimate \(2/\sqrt K\).