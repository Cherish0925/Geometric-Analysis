# TTCS Independent Branch Record

```json
{
  "step_id": 70,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step69_anisotropic_cusp_compensation.md",
    "Sessions/S0910A03/workspace/notes/step70_mixed_boundary_formulation.md"
  ]
}
```

## Task

Verify the peripheral algebraic reduction for the anisotropic quotient construction. The claim: for a one-cusped orientable hyperbolic 4-manifold piece P with cusp lattice Λ≅Z³ and a primitive character φ:π₁(P)→Z with φ|Λ=dℓ (ℓ primitive, d≥1), the cyclic mod-N cover (N coprime to d) has one cusp with peripheral lattice ker(dℓ mod N) = {v∈Λ: d ℓ(v)≡0 mod N}, which has type (N,1,1) in the basis {ℓ,e₂,e₃}. VERIFY: (1) Is this algebraic claim correct? (2) Does the resulting cover remain a single-cusped manifold (i.e., does the peripheral inclusion being surjective mod N guarantee one cusp)? (3) For the long exact sequence H₁(T³)→H₁(M̄)→H₁(M̄,T³)→0 with Poincaré-Lefschetz H₁(M̄,T³)≅H³(M̄), derive necessary and sufficient conditions on M̄ for the peripheral image in H₁(M̄;Q) to be nonzero. (4) For the Slavich orientable one-cusped 24-cell manifold with H₁≅Z⊕Z₃, determine whether the peripheral image is nonzero.

## Output

## Verification memo — peripheral algebra for the anisotropic $(N,1,1)$ quotient

Notation: $P$ is a one‑cusped orientable complete hyperbolic $4$‑manifold with torus cusp; $\Lambda\cong\mathbb Z^3$ its cusp lattice; $\bar M$ the compact core with $\partial\bar M=T^3$ (I use the symbol $\partial$, not the word). $\varphi:\pi_1(P)\to\mathbb Z$ is primitive (surjective) with $\varphi|_\Lambda=d\ell$, $\ell$ a primitive functional on $\Lambda$, $d\ge1$, $\gcd(N,d)=1$. Overall: parts (1) and (2) are correct, with one notational repair and one geometric point that is not the same as the algebraic statement. Part (3) has a clean exact answer. Part (4) reduces to a single integer invariant that the material does not yet supply, but the reduction produces a nontrivial structural fact that constrains the answer.

### (1) The algebraic statement is correct; two points to record

Let $\bar\varphi=\varphi\bmod N:\pi_1(P)\to\mathbb Z/N$. Since $\varphi$ is surjective onto $\mathbb Z$, $\bar\varphi$ is surjective onto $\mathbb Z/N$, so the associated cover $\tilde P\to P$ is connected of degree $N$. It is regular with deck group $\mathbb Z/N$.

The cusp subgroup upstairs is $\Lambda'=\ker(\bar\varphi|_\Lambda)=\{v\in\Lambda:\ d\ell(v)\equiv0\ (\mathrm{mod}\ N)\}$, exactly as written. Choose a basis $\{f_1,e_2,e_3\}$ of $\Lambda$ with $\ell(f_1)=1$, $\ell(e_2)=\ell(e_3)=0$ (possible because $\ell$ is primitive; $e_2,e_3$ span $\ker\ell$). For $v=af_1+be_2+ce_3$ the condition is $da\equiv0\ (\mathrm{mod}\ N)$, and because $\gcd(d,N)=1$ this is $a\equiv0\ (\mathrm{mod}\ N)$. Hence
$$
\Lambda'=N\mathbb Z\,f_1\oplus\mathbb Z\,e_2\oplus\mathbb Z\,e_3,\qquad [\Lambda:\Lambda']=N,
$$
which is Smith‑normal‑form type $(N,1,1)$. So the elementary‑divisor statement is right, and $\gcd(d,N)=1$ is doing exactly the work stated.

Two things to keep separate:

- **Notational repair.** The note writes the basis as $\{\ell,e_2,e_3\}$; $\ell$ is a functional, and the correct third generator is the dual lattice vector $f_1$ with $\ell(f_1)=1$. This is cosmetic but should be fixed so the index computation reads correctly.
- **Algebraic type $\neq$ metric type.** Type $(N,1,1)$ here is the abstract sublattice type. The construction in step69 §4 and step70 §8 needs a *metric* rectangular lattice so that a horospherical truncation at depth $\log N$ scales all three lengths uniformly and yields shape $(1,N^{-1},N^{-1})$. That requires $f_1\perp\ker\ell$ in the flat cusp metric, i.e. the covered direction is metrically orthogonal to the fixed $2$‑plane. Smith normal form does not give this; the flat cusp of $P$ is a general marked $3$‑torus, and $f_1$ need not be orthogonal to $\mathrm{span}(e_2,e_3)$. The notes already hedge this with "up to the bounded nonflat deformation carried by the core," but the elongation direction being non‑orthogonal changes the induced shape by a fixed shear that must be absorbed; it does not vanish as $N\to\infty$. This is a genuine geometric point to carry, distinct from the (correct) algebra.

### (2) Single cusp: the coprimality condition is not merely sufficient — it is equivalent

For a regular cover with deck group $G=\mathbb Z/N$ and covering homomorphism $\bar\varphi$, the number of cusps over the single cusp of $P$ equals the number of double cosets $\ker\bar\varphi\backslash\pi_1(P)/\Lambda$, which for a normal subgroup is $[\,G:\bar\varphi(\Lambda)\,]$. Here
$$
\bar\varphi(\Lambda)=d\ell(\Lambda)\bmod N=d\mathbb Z\bmod N=\gcd(d,N)\,\mathbb Z/N .
$$
So the count is $\gcd(d,N)$, and it equals $1$ precisely when $\gcd(d,N)=1$. Thus "one cusp upstairs $\iff$ $\bar\varphi|_\Lambda$ surjective onto $\mathbb Z/N$ $\iff$ $\gcd(d,N)=1$." The single‑cusp property is therefore an equivalence, not a one‑way implication; the wording "peripheral inclusion surjective mod $N$ guarantees one cusp" is correct and is sharp. The one cusp cross‑section is $\mathbb R^3/\Lambda'\cong T^3$, so it stays a genuine $3$‑torus, and its lattice covers the base lattice with degree $[\Lambda:\Lambda']=N$, consistent with the total covering degree. (This all assumes the cusp is a torus, $\Lambda\cong\mathbb Z^3$; for the other orientable flat $3$‑manifold cross‑sections the peripheral group is a Bieberbach group and the count uses its image, so the same computation must be redone through the crystallographic quotient.)

### (3) Necessary and sufficient condition for nonzero peripheral image, over $\mathbb Q$

Work with $\mathbb Q$ coefficients; $\bar M$ compact oriented, $\partial\bar M=T^3$, both connected. The long exact sequence of $(\bar M,\partial\bar M)$ gives at the low end
$$
H_1(T^3)\xrightarrow{\,i_*\,}H_1(\bar M)\xrightarrow{\,j\,}H_1(\bar M,\partial\bar M)\xrightarrow{\ \partial_*\ }H_0(T^3)\xrightarrow{\sim}H_0(\bar M).
$$
Because both are connected, the last map is an isomorphism, so $\partial_*=0$ and $j$ is surjective. Poincaré–Lefschetz duality gives $H_1(\bar M,\partial\bar M)\cong H^3(\bar M)$, whence $\dim H_1(\bar M,\partial\bar M)=b_3(\bar M)$. Therefore
$$
\boxed{\ \operatorname{rank}\bigl(i_*:H_1(T^3;\mathbb Q)\to H_1(\bar M;\mathbb Q)\bigr)=\dim\ker j=b_1(\bar M)-b_3(\bar M).\ }
$$
So **the peripheral image is nonzero over $\mathbb Q$ if and only if $b_1(\bar M)>b_3(\bar M)$**, equivalently $b_1(\bar M)>\dim H_1(\bar M,\partial\bar M;\mathbb Q)$. Since $H^1(\bar M;\mathbb Q)$ is dual to $H_1(\bar M;\mathbb Q)$, this is also equivalent to $i^*:H^1(\bar M;\mathbb Q)\to H^1(T^3;\mathbb Q)$ being nonzero, i.e. to the existence of an integral $\varphi$ with $\varphi|_\Lambda\neq0$ — precisely the hypothesis the construction needs before any character can be chosen. This ties part (3) directly to the premise of (1): no such $\varphi$ exists unless $b_1>b_3$.

A structural consequence worth recording. Running the full rank bookkeeping of the same sequence (using $b_4=0$, $r_0=1$, and $H_k(\bar M,\partial)\cong H^{4-k}(\bar M)$) gives, for the torus cusp,
$$
r_3=0,\qquad r_1=b_1-b_3,\qquad r_2=\operatorname{rank}\bigl(H_2(T^3)\to H_2(\bar M)\bigr)=3-b_1+b_3 .
$$
Because $r_2\le b_2(\bar M)$, one obtains $b_2\ge 3-b_1+b_3$ and hence
$$
\chi(\bar M)=1-b_1+b_2-b_3\ \ge\ 4-2b_1,\qquad\text{i.e. } b_1(\bar M)\ge 2-\tfrac{\chi}{2}.
$$
For $\chi=1$ this forces $b_1\ge2$. This is a genuine constraint on which pieces can be used and is a useful cross‑check on the retrieval program in step70 §1/step69 §4.

### (4) Slavich orientable one‑cusped $24$‑cell manifold, $H_1\cong\mathbb Z\oplus\mathbb Z_3$

Here $b_1(\bar M)=1$. Part (3) gives $b_3\le b_1=1$ (from $r_1\ge0$), so $b_3\in\{0,1\}$ and
$$
\text{peripheral image nonzero over }\mathbb Q\iff b_3(\bar M)=0\iff r_1=1 .
$$
Equivalently, at the integral level: with $H_1(\bar M;\mathbb Z)=\mathbb Z\oplus\mathbb Z/3$, the image of $i_*:H_1(T^3;\mathbb Z)\to\mathbb Z\oplus\mathbb Z/3$ is rationally nonzero iff the composite $H_1(T^3;\mathbb Z)\to\mathbb Z\oplus\mathbb Z/3\to\mathbb Z$ (projection to the free part) is nonzero, i.e. iff the single free generator of $H_1(\bar M)$ is peripheral rather than an internal cycle.

Two derived facts, and one datum that is missing:

- **Not a single $24$‑cell.** The regular ideal $24$‑cell has volume $4\pi^2/3$, so a manifold assembled from one $24$‑cell has $\chi=1$. By the inequality above, $\chi=1$ forces $b_1\ge2$. Since the stated $H_1$ gives $b_1=1$, this manifold must have $\chi\ge2$, i.e. it is not a single $24$‑cell. This is consistent with an orientable piece built from at least two copies (e.g. an orientable double of a non‑orientable single‑$24$‑cell manifold), which is the natural way to get orientability, and it agrees with $\chi=b_2-b_3\ge2$.

- **Both alternatives survive $H_1$ alone.** With $b_1=1$: either $(b_3,r_1)=(0,1)$, peripheral image rank one, $b_2=\chi\ge2$; or $(b_3,r_1)=(1,0)$, peripheral image rationally zero, $b_2=\chi+1\ge3$. Knowing $H_1$ (hence $b_1$ and the torsion $\mathbb Z_3$) does not by itself separate these; one additional Betti number ($b_2$ or $b_3$) or the explicit integer peripheral matrix is required.

- **The decisive datum is $b_3(\bar M)$ (equivalently $r_1$).** The retrieved material in step69/step70 does not contain it. To settle part (4) definitively one needs, from Slavich's explicit cell structure or a computed homology of $\bar M$, either $b_3(\bar M)$, or $b_2(\bar M)$ together with $\chi$, or directly the rank of the peripheral inclusion $H_1(T^3;\mathbb Z)\to\mathbb Z\oplus\mathbb Z_3$. I did not reconstruct these from the given files and do not have a reliable value to assert; presenting a definite yes/no here without that computation would be unsupported.

Why this matters for the construction, not just for bookkeeping: $r_1=1$ is exactly the value the $(N,1,1)$ program wants. If $r_1=1$, then $\ker(i_*)\cap\Lambda$ is rationally a rank‑$2$ sublattice — the fixed flat $2$‑plane $\mathrm{span}(e_2,e_3)$ — and every integral $\varphi$ restricts on $\Lambda$ to a multiple of one primitive functional $\ell$, so the elongation direction and the fixed $2$‑plane are canonically determined; this is the geometry step69 §4 assumes. If instead $b_3=1$ (so $r_1=0$), then $i^*=0$, no integral $\varphi$ has $\varphi|_\Lambda\neq0$, and this piece produces no anisotropic character cover at all — the premise of parts (1)–(2) is empty for it. So determining $b_3$ for the Slavich piece decides whether it is usable, not merely which subtype it is.

### Net

Parts (1) and (2) are mathematically sound; fix the $\ell$‑vs‑$f_1$ notation, and separate the correct algebraic type $(N,1,1)$ from the stronger metric‑rectangular property the truncation needs (a fixed shear from non‑orthogonality of the elongation direction does not decay with $N$). Part (3) has the exact answer $r_1=b_1-b_3$, nonzero over $\mathbb Q$ iff $b_1>b_3$, together with the free constraint $b_1\ge 2-\chi/2$. Part (4) reduces cleanly to $b_3(\bar M)=0$; the given $H_1$ forces $\chi\ge2$ (so the piece is not a single $24$‑cell), but the yes/no on the peripheral image requires the explicit $b_3$ / peripheral matrix from Slavich's data, which is what remains to be retrieved before this piece can be relied upon.