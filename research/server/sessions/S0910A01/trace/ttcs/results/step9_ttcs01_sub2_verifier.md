# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/scripts/step9_nil3_orbit_volume.py",
    "Sessions/S0910A01/workspace/notes/step9_regular_collapse_exclusion.md",
    "Sessions/S0910A03/workspace/notes/step7_orbit_volume_negative_einstein_collapse.tex"
  ]
}
```

## Task

Verify the following derivation for the nil³ orbit-volume equation. For a 4D Bianchi-II warped product g = dt² + a₁²σ₁² + a₂²σ₂² + a₃²σ₃² with [σ₁,σ₂] = σ₃ (Nil³ frame) and Ric = -g:

1. Define fᵢ = aᵢ'/aᵢ and μ = a₃²/(2a₁²a₂²).
2. The Einstein equations are:
   E0: (f₁'+f₁²)+(f₂'+f₂²)+(f₃'+f₃²) = 1
   E1: (f₁'+f₁²)+f₁f₂+f₁f₃-μ = 1
   E2: (f₂'+f₂²)+f₁f₂+f₂f₃-μ = 1
   E3: (f₃'+f₃²)+f₁f₃+f₂f₃+μ = 1
3. The orbit volume v = a₁a₂a₃ satisfies v''/v = 1 + 2(f₁f₂+f₁f₃+f₂f₃).
4. Summing E1+E2+E3: 1 + 2(f₁f₂+f₁f₃+f₂f₃) - μ = 3.
5. Therefore v'' = (3+μ)v ≥ 3v.

Check each step: (a) Are the Ricci tensor components correct for Bianchi II? (b) Is the cross-term sum correctly extracted from E1+E2+E3? (c) Does E0 play the right role? (d) Does the result v'' ≥ 3v exclude periodic and vanishing-boundary solutions? (e) For the near-Einstein case Ric = -g+E with |E| ≤ δ, does v'' ≥ 3(1-δ)v hold? (f) Is there any sign convention issue with the Nil³ structure constants that could affect the result?

## Output

# Verification Memo: Nil³ orbit-volume equation for the λ = −1 branch

## Summary of the finding

The algebra in steps 3–5 is internally valid, but the input Einstein equations E1, E2, E3 carry the wrong sign on the structure term μ. Directions 1 and 2 (the pair whose bracket generates the center) should carry **+μ**, and direction 3 (the center) should carry **−μ**. The note has these reversed. Propagating the corrected signs gives

$$
\boxed{v'' = (3-\mu)\,v},\qquad \mu=\frac{a_3^2}{2a_1^2a_2^2}\ge 0,
$$

not $v''=(3+\mu)v$. Because $3-\mu$ is not bounded below by $3$ — and can be $\le 0$ once $\mu\ge3$ — the strict convexity $v''\ge 3v$ and every consequence drawn from it in §2 (Corollaries 1–3), in §3 (the "Nil³ excluded" row), and in §4 (Step 6) does not follow. The intrinsic Heisenberg curvature **reduces** $v''$; it does not add to it. This restores exactly the compensation that S0910A03 anticipated (the note's Remark reversing that expectation is the erroneous step).

A decisive independent check below (the explicit Heisenberg Einstein solvmanifold) confirms $v''=(3-\mu)v$ and refutes the exclusion.

## (a) Ricci components of the diagonal Bianchi II metric

I recomputed the Ricci tensor of $g=dt^2+a_1^2\sigma_1^2+a_2^2\sigma_2^2+a_3^2\sigma_3^2$ with $d\sigma^3=-\sigma^1\wedge\sigma^2$ (equivalently $[e_1,e_2]=e_3$) three independent ways: Cartan structure equations, the Milnor formula for left-invariant Heisenberg metrics, and the ADM/warped-product decomposition. All three agree.

Set $b=a_3/(a_1a_2)$, so $\mu=b^2/2$. In the orthonormal frame $E_i=e_i/a_i$ one has $[E_1,E_2]=bE_3$, and the intrinsic spatial Ricci (Milnor) is

$$
{}^{3}\mathrm{Ric}(E_1)={}^{3}\mathrm{Ric}(E_2)=-\tfrac{b^2}{2}=-\mu,\qquad
{}^{3}\mathrm{Ric}(E_3)=+\tfrac{b^2}{2}=+\mu .
$$

The center direction $E_3$ has positive intrinsic Ricci; the two generating directions $E_1,E_2$ have it negative. My Cartan computation reproduces exactly this ($b^2$-part of $R_{11},R_{22}$ is $-b^2/2$; of $R_{33}$ is $+b^2/2$), and the extrinsic ($f$-dependent) parts match $R_{ii}={}^{3}\mathrm{Ric}_{ii}-(f_i'+f_i^2)-f_i(F-f_i)$, $F=\sum f_j$.

Imposing $\mathrm{Ric}=-g$ ($R_{aa}=-1$) then gives:

- **E0** (from $R_{00}$, no $\mu$): $\ (f_1'+f_1^2)+(f_2'+f_2^2)+(f_3'+f_3^2)=1$. **Correct as stated.**
- **E1**: $(f_1'+f_1^2)+f_1f_2+f_1f_3+\mu=1$ — the note has $-\mu$.
- **E2**: $(f_2'+f_2^2)+f_1f_2+f_2f_3+\mu=1$ — the note has $-\mu$.
- **E3**: $(f_3'+f_3^2)+f_1f_3+f_2f_3-\mu=1$ — the note has $+\mu$.

The reason: rearranging $R_{11}={}^{3}\mathrm{Ric}_{11}+(\text{warping})=-1$ with ${}^{3}\mathrm{Ric}_{11}=-\mu$ moves $+\mu$ to the warping side; the center equation moves $-\mu$. The note assigned positive intrinsic Ricci to the generating directions and negative to the center, i.e. it swapped the two roles.

## (b) Cross-term extraction

The identity $v''/v=1+2(f_1f_2+f_1f_3+f_2f_3)$ (step 3) is correct and $\mu$-independent. Summing the **corrected** E1+E2+E3:

$$
\underbrace{\sum(f_i'+f_i^2)}_{=1\text{ by E0}}+2(f_1f_2+f_1f_3+f_2f_3)+\mu=3
\ \Rightarrow\ 2(f_1f_2+f_1f_3+f_2f_3)=2-\mu .
$$

Hence $v''/v=1+(2-\mu)=3-\mu$. The note's $2\Sigma f_if_j=2+\mu$ is a direct consequence of the flipped E1–E3.

## (c) Role of E0

E0 is used correctly and is unaffected: $R_{00}$ contains no $b^2$ term, so $\sum(f_i'+f_i^2)=1$ holds exactly. This part is sound.

## (d) Consequences $v''\ge 3v$ — do not hold

With $v''=(3-\mu)v$:

- **Circle base (Cor. 1).** $\int_0^L v''=0$ becomes $\int_0^L(3-\mu)v=0$, i.e. $\int \mu v=3\int v$. This is not contradictory, so periodicity is not obstructed by the equation.
- **Endpoint-vanishing base (Cor. 2).** At an interior maximum $v''\le0$ forces only $\mu\ge3$ there — a constraint, not a contradiction.
- The strict subharmonicity/convexity used throughout §3 requires $\mu<3$; it is not automatic. In a Nil³ collapse where $a_3$ is comparatively long relative to $a_1a_2$, $\mu$ is large and $v''$ can be $\le0$.

## (e) Near-Einstein version

For $\mathrm{Ric}=-g+E$, $|E|\le\delta$, the vertical traces shift each spatial equation by $O(\delta)$, and E0 by $O(\delta)$. The corrected sum gives

$$
v''=\bigl(3-\mu+O(\delta)\bigr)v .
$$

The stated bound $v''\ge3(1-\delta)v$ does not hold; there is no $\mu$-independent positive lower coefficient.

## (f) Sign convention of the structure constants

Choosing $d\sigma^3=+\sigma^1\wedge\sigma^2$ versus $-\sigma^1\wedge\sigma^2$ only flips the sign of $b$; every curvature term depends on $b^2$, so $\mu$ and the result are unchanged. The error is therefore not a convention ambiguity. It is the assignment of the intrinsic Heisenberg Ricci to the correct frame directions, which is fixed unambiguously by which direction is the center.

## Decisive independent check: the Heisenberg Einstein solvmanifold

The Heisenberg algebra is the nilradical of a rank-one homogeneous Einstein solvmanifold with $\lambda<0$ — a complete Nil³ warped product with $\mathrm{Ric}=-g$. Take $a_i=c_i e^{\lambda_i t}$, $\lambda_1=\lambda_2=\alpha$, $\lambda_3=2\alpha$ (grading $\lambda_3=\lambda_1+\lambda_2$, so $b$ is constant), and let $\mu$ be set by the fiber/base scale.

Substituting into the **corrected** equations:
- E0: $6\alpha^2=1\Rightarrow\alpha^2=1/6$.
- E1: $4\alpha^2+\mu=1\Rightarrow\mu=1/3$.
- E3: $8\alpha^2-\mu=1\Rightarrow\mu=1/3$. ✓ (E2 = E1.)

All four are satisfied simultaneously with $\mu=1/3$, $b^2=2/3$. This is a genuine $\mathrm{Ric}=-g$ Nil³ warped product. Its orbit volume $v=Ce^{(\lambda_1+\lambda_2+\lambda_3)t}=Ce^{4\alpha t}$ gives

$$
v''=16\alpha^2 v=\tfrac{16}{6}v=\tfrac{8}{3}v,\qquad 3-\mu=3-\tfrac13=\tfrac83 .\ \checkmark
$$

The note's equation would predict $(3+\mu)v=\tfrac{10}{3}v\ne\tfrac83 v$. Moreover the note's flipped equations, applied to this same solution, force $\mu=4\alpha^2-1=-1/3<0$, impossible for $\mu=b^2/2\ge0$ — so the note's system has no solution consistent with an object that demonstrably exists. This both confirms $v''=(3-\mu)v$ and exhibits a concrete Nil³ warped $\mathrm{Ric}=-g$ metric of exactly the type §2 asserts cannot occur.

This is also what one expects from Cheeger–Fukaya–Gromov theory, where Nil-geometry collapse with bounded curvature is the prototypical example rather than an excluded one.

## Status of the numerics in `step9_nil3_orbit_volume.py`

The ODE right-hand sides (`dda1=a1*(1-f1*(f2+f3)+mu)`, `dda3=a3*(1-f3*(f1+f2)-mu)`) encode the note's flipped E1/E3, so the integration re-uses the same equations and cannot independently test the $\mu$ sign. The observed exponential growth of $v$ in the trial runs is compatible with $v''=(3-\mu)v$ whenever $\mu<3$ (which holds for the small-$\mu$ initial data used) and therefore does not discriminate between the two equations. The pointwise "$1+2\Sigma f_if_j$ vs $3+\mu$" comparison in the script also does not test the sign, since it only observes that the identity holds solely on solutions. An independent check would integrate the **corrected** system, target large $\mu$ (small $a_1,a_2$, large $a_3$), and confirm the sign against the explicit solvmanifold value $v''=\tfrac83 v$ at $\mu=1/3$.

## What this leaves for the downstream program

- The §2 Proposition should read $v''=(3-\mu)v$; the Remark's assertion that $\mu$ makes Nil³ "even harder" is reversed — $\mu$ reduces $v''$.
- The §3 table entry "Nil³ … Excluded by $v''\ge3(1-\delta)v$" and the §4 Step 6 use of it are not supported; a Nil³ negative-Einstein warped product exists.
- The abelian rows use Lott's $\Delta v=(|F|^2/4+N)v$, where $|F|^2$ is the O'Neill/connection curvature of a torus bundle — a different quantity from the intrinsic Heisenberg term, and correctly positive. The note's analogy "nil adds like abelian $F^2$" conflates the connection curvature of a fibration with the intrinsic bracket curvature of the fiber; only the former enters with $+$. A correct combined Nil³ statement would need both the fibration term ($+|F|^2/4$, if the base is twisted) and the intrinsic center term ($-\mu$).
- What remains genuinely open is whether Nil³ collapse under $\mathrm{Ric}\approx-g$ can be obstructed at all by an orbit-volume argument; the corrected equation permits it precisely in the large-$\mu$ regime, which is where Nil collapse actually lives.