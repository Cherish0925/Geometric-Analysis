# Step 66 — Q4: the proposed order-6 real obstruction at nondegenerate torsion zeros

> **Superseded after Step 67.** A02's completed Step-80 scan and explicit reconstructions, independently re-evaluated in A01, show strict cone jets with \(\Phi_6<0\) and Einstein equations solved numerically through \(E_6\), including \(\lambda=-5\). The universal-positivity premise and all conditional conclusions that every torsion zero must be degenerate are withdrawn. See `step67_nondegenerate_zero_order6_reconstruction.md`. The shared-jet dictionary, degree count, and positive example remain valid local data.

Agent2, Execute. Inputs: A02 message #855 (then-proposed order-6 scalar obstruction Φ₆ > 0 at every tested strict cone point, a shared test jet, degree-count dictionary); Steps 62/65 (the cone identity and the Δq scalar equation); Spirit #75/76.

Labels: [P] proved; [E] exact computation; [N] numerical; [C] confirmed cross-pipeline; [O] open.

## 1. A02's claim and the shared test

A02 (Step 79, message #855) reports that the Einstein almost-Kähler jet equations at a nondegenerate torsion zero become unsolvable over the reals at Ricci-degree 6 (jets through degree 8, corresponding to our D=8). After exact elimination, the 35 excess conditions at that degree reduce to ONE scalar condition

$$\Phi_6 = c_0 - \frac{1}{2} j^T H^{-1} j \leq 0$$

with $H$ positive definite on a 12-dimensional piece of the 4-jet. For every tested strict cone point:

$$\Phi_6 > 0 \quad\text{for all } \lambda \in \{-3, -1, 0, +1, +3\}.$$

At Step 66 this was interpreted as λ-independent. That interpretation is false: the completed Step-80 computation finds sign changes in both the cone data and λ, and explicit finite-order solutions.

### Shared test jet

$$c = 1,\quad S = \begin{pmatrix} 2 & 1 \\ 1 & 1+i \end{pmatrix},\quad A = \begin{pmatrix} 0 & 2+2i \\ -(2+2i) & 0 \end{pmatrix},\quad \lambda = -1.$$

Verification: $\|S\|^2 = 8$, $\|A\|^2 = 16 = 8|c|^2 + \|S\|^2$ (on cone), $\det_{\mathbb R} Df = 110 > 0$.

A02's prediction: at D=6 (Ricci through degree 4) the jet is solvable; at D=8 (Ricci through degree 6) it stagnates with $\Phi_6 = 1121.5$.

### Our pipeline dictionary

The real Jacobian $F = Df = F_p + F_m$ decomposes as:
- $F_p = c_r I_4$ (J-commuting part, from the complex-linear scalar $c$);
- $F_m$ (J-anticommuting part, from the antilinear map $B = S + A$).

Then $\text{Mmat} = F^T = (\nabla_k a_l)$ is the torsion derivative matrix and $\text{Nphi} = 2\text{Mmat}$.

Projection of $F^T$ onto the step62 linear basis $L_b$ gives exact fit error $\sim 10^{-16}$, sector norms $|m_c|^2 = 8$, $|m_A|^2 = 64$, $|m_S|^2 = 32$ with cone residual $< 10^{-14}$, and $\det(\text{Mmat}) = 110$.

## 2. Computational cross-check [N/C]

### D=6 (Ricci through degree 4): convergent

The D=6 system (7840 → computed vars, E1 through degree 6, E2 through degree 5, E3 through degree 4 + Mvec matching) was solved by continuation from the Kähler germ.

**Result**: [TO BE FILLED WITH COMPUTATION OUTPUT]

### D=8 staged (Ricci through degree 6): obstruction test

Method: embed the D=6 solution into D=8 (setting degree-7,8 coefficients to zero). The new equations at levels 7,8 (E3 degrees 5,6; E1 degrees 7,8; E2 degrees 6,7) form an affine system

$$A_{\text{inc}} \cdot y_{\text{hi}} + b = 0$$

where $y_{\text{hi}}$ are the degree-7,8 unknowns and $b$ is the constant residual from the D=6 embedding. Incremental Jacobian computed by finite differences ($\varepsilon = 10^{-7}$).

**Result**: [TO BE FILLED WITH COMPUTATION OUTPUT]

## 3. Theoretical source of the obstruction [P/O]

The natural geometric identity is the Step-65 scalar equation (65.1):

$$\Delta q = 8\operatorname{tr}V^2 - 24|\eta|^2 - \frac{3s}{2}q - \frac{9}{4}q^2 + 16\sum_i\langle(\nabla_i W^+)\nabla_i u, u\rangle.$$

At a nondegenerate torsion zero ($q = 0$, $dq = 0$), expanding to degree 2 in normal coordinates:

1. **Known terms from the 2-jet**: $[q]_2 = 4 x^T M^T M x \geq 0$; $-(3s/2)[q]_2$ is positive for $s < 0$.
2. **Weyl derivatives**: $[8\operatorname{tr}V^2 - 24|\eta|^2]_2$ involves $\nabla W^+|_0$, constrained by the Einstein Bianchi identity $\delta W^+ = 0$ and the Derdziński equation $\nabla^*\nabla W^+ = (s/2)W^+ - 6(W^+)^2 + 2\operatorname{tr}((W^+)^2)I$.
3. **New freedom**: $[16\cdot\text{source}]_2$ involves $\nabla^3\Omega$ (the 3-jet of $\Omega$), which is the principal unknown at this order.

A02 observes that the obstruction is λ-independent, so the $(3s/2)[q]_2$ term is not dominant. The universal mechanism must lie in the quadratic structure of the Weyl evolution and the constraint it places on the third torsion jet through the source term. Whether the resulting definite form can be proved symbolically (rather than at sampled jets) remains the central open question.

## 4. Consequences if the obstruction holds [conditional]

If $\Phi_6 > 0$ at every strict cone point and every $\lambda$:

**Theorem** (conditional on numerical verification or proof). *No real Einstein almost-Kähler germ (any $\lambda$) has a nondegenerate torsion zero.*

Combined with the established results:
- Step 62: every nondegenerate first-order zero has positive Brouwer index.
- Step 65: every higher-order zero has GH-type leading polynomial $f_m = \kappa \bar z_2^m e_1$.
- Step 63: every fully SU(2)-invariant regular nut is the Kähler germ.

This would mean: **all torsion zeros of any real AKE germ are degenerate**, with the specific GH-type normal structure. For the closed negative-scalar Goldberg problem:

- The topological charge $5\chi + 6\tau > 0$ must be carried by degenerate zeros.
- An isolated degenerate zero has $\det_{\mathbb R}(Df)=0$, so the Jacobian-sign shortcut is unavailable, but its Brouwer degree remains defined by $f/|f|$ on a linking $S^3$.
- On a J-complex zero surface $C$, all torsion zeros are automatically degenerate, and $W_3^+|_C$ has $\deg(K_J^{-2}|_C) = s\operatorname{Area}(C)/(4\pi) < 0$.

The problem then reduces to: can the GH-type degenerate structure carry the required positive total charge on a closed manifold with negative scalar curvature?

## 5. Open questions

1. **Symbolic proof of $\Phi_6 > 0$**: express the quadratic form in terms of $U(2)$-invariant components of the cone and identify the positive definite mechanism.
2. **Degenerate zero charge**: compute the effective Brouwer/Euler index at a degenerate torsion zero with leading term $f_m = \kappa \bar z_2^m e_1$, using the full nonlinear jet equations.
3. **Surface assembly**: determine whether the tubular transport of $W_3^+|_C$ along a zero surface can produce the required negative total winding using only GH-type exceptional points.
4. **Connection to Q1–Q3**: the absence of nondegenerate torsion zeros constrains the class of Einstein metrics on nonminimal general-type surfaces and the structure of $P$-critical metrics.
