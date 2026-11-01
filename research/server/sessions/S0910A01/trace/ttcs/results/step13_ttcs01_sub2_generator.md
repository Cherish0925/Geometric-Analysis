# TTCS Independent Branch Record

```json
{
  "step_id": 13,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step13_normalized_accessibility_theorem.md",
    "Sessions/S0910A03/workspace/notes/step12_reduced_equations_accessibility.md",
    "Sessions/S0910A01/workspace/plans/route_assessment_step13.md"
  ]
}
```

## Task

For the four-dimensional negative-branch near-Einstein circle collapse problem, consider a rank-one Kaluza-Klein metric g = g_B + ℓ²(dψ+A)² with Ric ≈ -g on a closed 4-manifold. The normalized cover g = g_B + v²(dz+B)² with v(p)=1 removes the fiber period from local coefficients. The reduced Einstein equations are: (V) Δv/v = 1 + v²|F_B|²/2, (M) div(v²F_B) ≈ 0, (H) Ric_B = -I + Hess(v)/v + (v²/2)F_B⊗F_B. The chiral variables a± = u ∓ z/2 (where u=d log v, z=*(vF_B)) satisfy W± = -[sym∇a± + a±⊗a±]₀ and da+ = a+∧a-. The calibrated W+ spectrum is (-1/6, 1/12, 1/12). The key analytical question: on the calibrated bulk where the W+ defect vanishes, does the chiral constraint force the Hessian tensor H = Hess(v)/v to have nonnegative eigenvalues? If H ≥ 0, then Ric_B ≥ -I (since the twist contribution is nonneg), giving a 3D Bishop-Gromov volume lower bound and 4D cover noncollapse. Investigate: (1) Can the calibrated W+ = E + B with E = 1/3·I - H + (|z|²I - z⊗z)/4 and B involving ∇z force H ≥ 0? (2) What is the relationship between the calibrated eigenvalues of E+B and the sign of H eigenvalues? (3) Can a counterexample with calibrated W+ but H having a negative eigenvalue exist? Consider the constraints from the trace mode tr(H) = 1 + |z|²/2 ≥ 1 and the chiral Riccati. Provide a rigorous mathematical assessment of whether H ≥ 0 is forced or can be violated on the calibrated bulk.

## Output

## Central result: an exact identity that removes "sign of the Hessian" as the real unknown

The cleanest way to answer all three questions is to solve the algebra of the reduced curvature for $H$ itself, rather than trying to read its sign off the calibrated block. From the definitions $W^\pm = E \pm B$ we have $E = \tfrac12(W^+ + W^-)$, and substituting into $E = \tfrac13 I - H + \tfrac14(|z|^2 I - z\otimes z)$ gives the exact pointwise identity

$$
\boxed{\,H \;=\; \tfrac13 I \;+\; \underbrace{\tfrac14\big(|z|^2 I - z\otimes z\big)}_{\text{twist, }\ge 0}\;-\;\tfrac12\big(W^+ + W^-\big)\,}
$$

valid at every point of the regular circle region. This is the whole story. The self-dual block $W^+$ (which calibration pins down) and the anti-self-dual block $W^-$ (which calibration leaves completely free) enter $H$ **symmetrically and additively**. There is no algebraic mechanism by which fixing $W^+$ alone can control the sign of $H$, because $H$ depends equally on $W^-$.

Evaluating on a unit direction $\xi$ and using the positive twist term:

$$
H(\xi,\xi)\;=\;\tfrac13+\tfrac14\big(|z|^2-\langle z,\xi\rangle^2\big)-\tfrac12 W^+(\xi,\xi)-\tfrac12 W^-(\xi,\xi)\;\ge\;\tfrac13-\tfrac12\lambda_{\max}(W^+)-\tfrac12\|W^-\|_{\mathrm{op}}.
$$

On the calibrated bulk (task normalization $W^+$ spectrum $(-\tfrac16,\tfrac1{12},\tfrac1{12})$, so $\lambda_{\max}(W^+)=\tfrac1{12}$):

$$
\boxed{\,H\;\ge\;\Big(\tfrac{7}{24}-\tfrac12\|W^-\|_{\mathrm{op}}\Big)I\quad\Longrightarrow\quad H\ge 0\ \text{ whenever }\ \|W^-\|_{\mathrm{op}}\le \tfrac{7}{12}.\,}
$$

The binding direction is $\xi=\hat z$ (along the twist covector), where the twist buffer $\tfrac14(|z|^2-\langle z,\xi\rangle^2)$ vanishes; there $H(\hat z,\hat z)\ge 0 \iff W^+(\hat z,\hat z)+W^-(\hat z,\hat z)\le \tfrac23$. Since $\mathrm{Ric}_B = -I + H + \tfrac12(|z|^2I - z\otimes z)$ and the twist matrix has its zero eigenvalue exactly along $\hat z$, the condition $\mathrm{Ric}_B\ge -I$ reduces to the **same** condition $H(\hat z,\hat z)\ge0$. In perpendicular directions the twist supplies an extra margin $\tfrac12|z|^2$, so those directions are never binding.

Consistency check with the static calibrated profile: $z=0$ forces $B=0$, hence $W^-=E=W^+$, giving $H=\tfrac13 I - W^+ = \mathrm{diag}(\tfrac12,\tfrac14,\tfrac14)\ge 0$ with $\|W^-\|_{\mathrm{op}}=\tfrac16<\tfrac7{12}$ — inside the guaranteed region, matching $H_{\mathrm{cal}}=(\tfrac12,\tfrac14,\tfrac14)$.

## (1) Calibrated $W^+=E+B$ does not force $H\ge 0$

At the level of point values plus the first jet of $z$, any $H$ with $\operatorname{tr}H = 1+|z|^2/2$ is compatible with an exactly calibrated $W^+$. Counting: $W^+$ trace-free symmetric is 5-dimensional; the symmetric part of $\nabla z$ contributes 5 free components with its trace pinned to $\langle u,z\rangle$ by the mixed equation $\operatorname{div}z=\langle u,z\rangle$, and this trace pinning is exactly what makes $B$ trace-free. Given any $H,u,z$, the tensor $E$ is determined, and one solves $B = W^+_{\mathrm{cal}}-E$ for $\operatorname{sym}\nabla z$; the trace condition is automatically satisfied. So $B$ ranges over **all** symmetric trace-free tensors as $\operatorname{sym}\nabla z$ varies, and calibration of $W^+$ imposes no condition on $H$.

Explicit realization (align $z,u$ along $e_1$, all diagonal). Put $H=\mathrm{diag}(-a,h_2,h_3)$ with $a>0$ (an eigenvalue below zero) and $h_2+h_3=1+|z|^2/2+a$. Requiring $W^+=\mathrm{diag}(-\tfrac16,\tfrac1{12},\tfrac1{12})$ (calibrated, $e=e_1$) forces
$$
B=W^+-E=\mathrm{diag}\big(-\tfrac12-a,\;h_2-\tfrac{|z|^2}{4},\;h_3-\tfrac{|z|^2}{4}\big),
$$
which is trace-free by the trace mode, and is achieved by a definite $\operatorname{sym}\nabla z$. The cost is read off from $W^-=E-B$: its $e_1$–entry is $\big(\tfrac16-(-\tfrac12-a)-2(-a)\big)$-type and grows linearly with $a$, so $\|W^-\|_{\mathrm{op}}\gtrsim \tfrac{7}{12}+2a$. This is the quantitative version of the boxed identity: an eigenvalue of $H$ below zero of size $a$ is paid for **entirely** by anti-self-dual curvature of size $\gtrsim a$. In A03's chiral language this is precisely "derivative twisting": $-W^- = [\operatorname{sym}\nabla a_- + a_-\otimes a_-]_0$ with $a_-=u+z/2$, and $\operatorname{sym}\nabla a_-$ (hence $\operatorname{sym}\nabla z$) is the free channel that calibration never touches.

## (2) The exact relation between $E+B$ and the sign of $H$

The relation is not a spectral coincidence between $H$-eigenvalues and $W^+$-eigenvalues (that holds only in the static, twist-free case, where $W^+=E=\tfrac13 I - H$ and the two spectra are affinely related). With twist present, the correct statement is the boxed identity: the eigenvalues of $H$ are those of $\tfrac13 I + \text{(twist)} - \tfrac12(W^++W^-)$. Fixing $W^+$ therefore fixes only the "half-sum" $E=\tfrac12(W^++W^-)$-input from the self-dual side; the sign of $H$ is decided by $W^-$. Equivalently:

$$
H\ge 0 \iff \tfrac12 W^-(\xi,\xi)\le \tfrac13+\tfrac14\big(|z|^2-\langle z,\xi\rangle^2\big)-\tfrac12 W^+(\xi,\xi)\quad\forall\xi,
$$

and on the calibrated bulk the right side is $\ge \tfrac13-\tfrac12\lambda_{\max}(W^+)>0$, so a **definite** amount of anti-self-dual curvature is tolerated before any eigenvalue of $H$ can reach zero. The trace mode $\operatorname{tr}H=1+|z|^2/2\ge 1$ does not by itself constrain the sign: it only says that if one eigenvalue is below zero the other two are correspondingly larger; combined with the identity it is automatically consistent because a below-zero eigenvalue is accompanied by a large positive $W^-$-eigenvalue, which raises the other two $H$-eigenvalues through the same identity.

## (3) Existence of a configuration with calibrated $W^+$ and a sign-indefinite $H$

Two regimes must be separated, and they give opposite answers.

**Exact calibration on an open set: no such configuration.** If $W^+$ equals the calibrated form $\tfrac13 I - e\otimes e$ (two-repeated-eigenvalue structure) on an open set of a genuine Einstein 4-manifold, Derdziński's theorem forces the metric to be Kähler with respect to the corresponding orientation and hence Kähler–Einstein locally. In that rigid class $H$ is the static (or complex-hyperbolic) profile with all eigenvalues $\ge 0$. So exactly on the true calibrated locus the sign question never even arises — which is exactly why the forbidden-germ mechanism works.

**Approximate calibration, the actual near-critical regime: such configurations exist.** The near-critical sequence has the calibrated defect small only in $L^2$-average, not pointwise, and the metrics are only approximately Einstein. In this regime the 1-jet construction of part (1) is realizable and, by prolongation/Cartan–Kähler type freedom in $\operatorname{sym}\nabla z$, extends to genuine local solutions of the reduced system that keep $\|W^+ - W^+_{\mathrm{cal}}\|$ small while carrying $\|W^-\|_{\mathrm{op}}>\tfrac7{12}$ and an eigenvalue of $H$ below zero on a set. The obstruction to such a set having positive measure in the true sequence is **not** the sign of $H$; it is whether $\|W^-\|$ can be that large on a definite fraction of the calibrated bulk.

## The decisive redirection: the sign of $H$ is a proxy for pointwise control of $W^-$

The boxed identity converts the noncollapse question into an exact and clean statement:

> On the calibrated bulk, $\mathrm{Ric}_B\ge -I$ (equivalently $H\ge 0$ in the twist direction) holds precisely on the set where $\|W^-\|_{\mathrm{op}}$ lies below an explicit constant of order $\tfrac7{12}$.

This removes the "Hessian sign" from the list of independent unknowns and localizes the entire difficulty to a pointwise (or $\varepsilon$-regularity) estimate for the **anti-self-dual** Weyl block on the bulk. That is a much more tractable and well-studied object than a Hessian sign, and it comes with three concrete avenues:

**(a) The signature/Euler integral pins $\int|W^-|^2$.** From $\tau(M)=\tfrac1{12\pi^2}\int(|W^+|^2-|W^-|^2)$ and the calibrated density $|W^+|^2\to \tfrac1{24}$ on the bulk, $\int_{\mathrm{bulk}}|W^-|^2$ is determined by the calibrated self-dual energy and the topology of the LeBrun-laboratory manifold. The worthwhile computation: evaluate $\int|W^-|^2 = \int|W^+|^2 - 12\pi^2\tau$ for the specific $(\chi,\tau)$ of the manifolds in the fixed critical family, and see whether the near-critical limit drives $\int_{\mathrm{bulk}}|W^-|^2\to$ small (in which case an $\varepsilon$-regularity argument for $W^-$ gives pointwise smallness a.e. on the bulk, hence $H\ge0$ and cover noncollapse), or whether it stays bounded away from zero (in which case the derivative-twist configuration of part (3) is genuinely available and the route must be reformulated). This single topological computation should be decisive for the whole branch and is inexpensive.

**(b) Decoupled $\varepsilon$-regularity for the $a_-$ Riccati.** Because $-W^- = [\operatorname{sym}\nabla a_- + a_-\otimes a_-]_0$ with $da_- = -a_+\wedge a_-$, and because the calibrated $a_+$ satisfies a determined first-order system (its symmetric derivative fixed by calibrated $W^+$, its curl fixed by Maurer–Cartan), the anti-self-dual block is governed by a first-order equation for $a_-$ coupled to a controlled $a_+$. Standard Weyl $\varepsilon$-regularity for near-Einstein 4-manifolds needs small **total** energy; here the obstruction has always been the definite background from $W^+$. The identity shows one only needs $\varepsilon$-regularity for the $W^-$-carrying tensor $\operatorname{sym}\nabla a_-$, with $W^+$ treated as a fixed calibrated coefficient. This is exactly the "gauge-covariant smoothing of the calibrated residual" A03 flagged, now with a precise target tensor: subtract the calibrated $W^+$ and prove $\varepsilon$-regularity for the residual chiral Riccati of $a_-$ alone.

**(c) A coercive weighted Bochner should be aimed at $W^-$, not at $H$.** The right coercive identity is not for $H$ (which is a derived, sign-indefinite combination) but for $a_-$ under the $\ell\,dvol_q$-weighted Laplacian, controlling $|\nabla a_-|^2 + |a_+\wedge a_-|^2$ by the two chiral Weyl energies plus divergence terms. The uncontrolled trace mode that A03 identified is exactly $\operatorname{tr}(\operatorname{sym}\nabla a_- + a_-\otimes a_-)= \kappa + \tfrac34|z|^2 + \tfrac32\langle u,z\rangle$; the boxed identity suggests normalizing by the calibrated $W^+$ energy, since that is the only place the trace mode couples back to a quantity already fixed on the bulk.

## Summary judgment

Calibration of $W^+$ neither forces nor forbids $H\ge 0$: the exact identity $H = \tfrac13 I + (\text{twist}) - \tfrac12(W^+ + W^-)$ shows the sign of $H$ is set by the anti-self-dual block $W^-$, which calibration does not see. There is a sharp, always-valid inequality $H \ge (\tfrac7{24}-\tfrac12\|W^-\|_{\mathrm{op}})I$ on the calibrated bulk, so $H\ge0$ (hence $\mathrm{Ric}_B\ge -I$, in fact $\ge -\tfrac{17}{24}I$) holds automatically wherever $\|W^-\|_{\mathrm{op}}$ is below an explicit order-one constant, and a sign-indefinite $H$ requires $\|W^-\|$ several times the calibrated $|W^+|$. Exact calibration excludes the sign-indefinite case entirely (Derdziński rigidity to Kähler–Einstein); the approximate near-critical regime admits it, but only through large $W^-$. The cover-noncollapse question on the bulk is therefore mathematically identical to a pointwise / $\varepsilon$-regularity bound on the anti-self-dual Weyl curvature, with the signature integral of the LeBrun family providing the fastest test of which way it resolves.

One reconciliation is needed before locking numbers: the stated $E=\tfrac13 I - H+\cdots$ with $\mathrm{Ric}\approx -g$ makes the Kähler–Einstein self-dual energy $|W^+|^2 = s^2/24 = 2/3$ with spectrum $(-\tfrac23,\tfrac13,\tfrac13)$, whereas the calibrated value used here is $(-\tfrac16,\tfrac1{12},\tfrac1{12})$ with $|W^+|^2=1/24$ (a factor $16$ apart). Both are internally consistent as static reduced profiles under $\mathrm{tr}H=1$, but they are distinct tensors, and the forbidden-germ contradiction relies on the calibrated $1/24$ being incompatible with the Kähler–Einstein $2/3$. The qualitative conclusions above are normalization-robust; the explicit constants $\tfrac7{12}$, $\tfrac{17}{24}$ shift under the alternative calibration to $\tfrac13$, $\tfrac56$ respectively, and the identity itself is unchanged.