# TTCS Independent Branch Record

```json
{
  "step_id": 18,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step3_boundary_near_saturation.tex",
    "Sessions/S0910A03/workspace/notes/step17_normalized_cutoff_flow_theorem.md",
    "Sessions/S0910A03/workspace/scripts/verify_step18_noether_topology_bound.py",
    "Knowledge/objects/papers/Curvature-Connected-Sums-and-Seiberg-Witten-Theory--7e92a6723434--2ac6d11897c5/object.md"
  ]
}
```

## Task

Check the topological-uniformity correction for the critical Ishida–LeBrun family. Derive c2≤5c1²+36 for each minimal complex surface of general type from Noether's formula and Noether's inequality, then compute χ(M)/A for M=(#_{j=1}^m X_j)#N, m=2 or 3, using exact connected-sum formulas and D=4m-(2χ+3τ)(N)=A/3. Determine under the actual standard hypotheses on N in the Ishida–LeBrun construction whether χ(N)/A is automatically bounded above; distinguish what follows from D alone, from negative-definiteness/b1 assumptions, and from the common choices of N. Correct any convention mismatch. The aim is an exact, reusable bound or a precise statement of the missing N input.

## Output

# Verification Memo: Topological Uniformity of the Critical Ishida–LeBrun Family

## Summary of findings

The arithmetic chain "Noether formula + Noether inequality ⟹ $c_2\le 5c_1^2+36$ ⟹ $\chi(M)/A$ bounded" is correct in every step I checked, **but two things in the surrounding notes need correcting**:

1. $\chi(N)$ **is** bounded above under the actual standing hypothesis $b_+(N)=0$. The Step 18 script's conclusion that "the critical $D$ relation alone does not bound $\chi(N)$" is arithmetically true for two *free* variables $(\chi_N,\tau_N)$, but it omits the second relation $\chi(N)+\tau(N)=2-2b_1(N)$ supplied by $b_+(N)=0$, which is a hypothesis of Ishida–LeBrun Theorems A–D. With it, $\chi(N)$ is pinned exactly.

2. The genuine additional input is **not** on $N$ but on the surfaces: the bound $c_2\le 5c_1^2+36$ (hence bounded $\chi(M)/A$) requires each $X_j$ to be **of general type** ($c_1^2(X_j)>0$). Ishida–LeBrun's Theorem D admits minimal complex/almost-complex summands that are *not* general type (e.g. properly elliptic $E(n)$ with $c_1^2=0$, $c_2=12n$), and for those the ratio is unbounded. Step 17's phrase attributing the bound to BMY is the wrong direction; BMY gives a lower bound on $c_2$, whereas the needed upper bound comes from Noether.

Details below.

## 1. The surface bound $c_2\le 5c_1^2+36$ (verified, general type required)

For $X$ minimal of general type, write $a=c_1^2(X)=K_X^2$, $c_2(X)=\chi_{\mathrm{top}}(X)$, $\chi_h=\chi(\mathcal O_X)=1-q+p_g$.

- Noether formula: $a+c_2=12\chi_h$.
- $q\ge0$ gives $\chi_h\le 1+p_g$.
- Noether inequality (valid for minimal general type): $a\ge 2p_g-4$, i.e. $p_g\le a/2+2$.

Hence $\chi_h\le 1+p_g\le a/2+3$, and
$$c_2=12\chi_h-a\le 12(a/2+3)-a=5a+36.$$
This reproduces the script's `c2 ≤ 5*c1^2 + 36` exactly, and the script's intermediate $\chi_h\le(a+6)/2$ is correct.

**Domain of validity.** Noether's inequality holds only for surfaces of general type. For $X=E(n)$ (minimal properly elliptic, $c_1^2=0$, $c_2=12n$, $b_1=0$, $b_+=2n-1$) it does not hold once $n\ge4$: there $2p_g-4=2n-6>0=c_1^2$. Correspondingly $c_2=12n>36=5c_1^2+36$. So the bound is specifically a general-type statement; for minimal surfaces this is equivalent to $c_1^2>0$.

## 2. Connected-sum Euler characteristic (verified)

For $M=(\#_{j=1}^m X_j)\#N$ ($m+1$ summands, $\chi(S^4)=2$):
$$\chi(M)=\sum_{j=1}^m c_2(X_j)+\chi(N)-2m,$$
matching the script's `chiM = sumc2 + chiN - 2m`. With $\sum c_2(X_j)\le 5A+36m$ this gives $\chi(M)\le 5A+34m+\chi(N)$, also matching the script.

## 3. $\chi(N)$ is pinned by $b_+(N)=0$ plus the critical relation

This is the crux. Using $b_+(N)=0$:
$$\tau(N)=-b_-(N),\quad \chi(N)=2-2b_1(N)+b_-(N),\quad \chi(N)+\tau(N)=2-2b_1(N).$$
Then $(2\chi+3\tau)(N)=4-4b_1(N)-b_-(N)$, so the Ishida–LeBrun invariant is
$$D=4m-(2\chi+3\tau)(N)=4(m-1)+4b_1(N)+b_-(N).$$
(This equals the $\tfrac13\{12(m-1)+(12b_1+3b_-)(N)\}$ form of Theorem D — consistent with the paper.)

Impose the critical relation $D=A/3$. Solving,
$$b_-(N)=\tfrac{A}{3}-4(m-1)-4b_1(N),$$
$$\boxed{\chi(N)=\tfrac{A}{3}-4m+6-6\,b_1(N)}.$$
Since $b_1(N)\ge0$,
$$\chi(N)\le \tfrac{A}{3}-4m+6,\qquad \frac{\chi(N)}{A}\le \tfrac13-\frac{4m-6}{A}<\tfrac13\quad(m\ge2).$$

So $\chi(N)/A$ is automatically bounded above — indeed by less than $1/3$. The script's `assert chiN in critical_sub.free_symbols` correctly detects that one linear relation among two symbols leaves one free, but the physical constraint $b_+(N)=0$ supplies exactly the missing second relation $\chi_N+\tau_N=2-2b_1$. The "missing $N$ input" the script asks for is therefore already present in every relevant Ishida–LeBrun theorem (Theorem A/B/C/D all impose $b_+(N)=0$; Theorem C's ASD-positive-scalar hypothesis forces it). No further hypothesis on $N$ is needed for the $\chi(N)$ half.

**Cross-checks against the paper's examples.**
- $N=k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)$ (Corollary 16): $b_1=\ell$, $b_-=k$, $b_+=0$. Then $\chi(N)=2-2\ell+k$, and the critical relation gives $k=A/3-4(m-1)-4\ell$, yielding $\chi(N)=A/3-4m+6-6\ell$. Consistent.
- Definite $N$ with $b_+=0$, $b_1=0$, $b_2=k$ (the script's `_nd` case): $\chi(N)=2+k$, $\tau(N)=-k$, $(2\chi+3\tau)(N)=4-k$, and $D=4m-(4-k)=4(m-1)+k$. The script's code computes `D_nd = 4m-4+k` correctly; only the inline prose "$D=k$" is loose (true only for $m=1$). The script's own caution against identifying $D=k$ is well placed, but the resolution is simply $D=4(m-1)+k$, not an unresolved convention.

## 4. The exact $\chi(M)/A$ bound

Combine §1–§3:
$$\chi(M)=\sum c_2(X_j)+\chi(N)-2m\le (5A+36m)+\big(\tfrac{A}{3}-4m+6\big)-2m=\tfrac{16A}{3}+30m+6.$$
$$\boxed{\dfrac{\chi(M)}{A}\le \dfrac{16}{3}+\dfrac{30m+6}{A}}.$$

A lower bound on $A$ is also automatic on the critical family: $b_-(N)\ge0$ forces $A\ge 12(m-1)+12b_1(N)\ge 12(m-1)$. Hence
- $m=2$: $A\ge12$, $\chi(M)/A\le 16/3+66/12=65/6\approx10.83$;
- $m=3$: $A\ge24$, $\chi(M)/A\le 16/3+96/24=28/3\approx9.33$;

and $\chi(M)/A\to 16/3$ as $A\to\infty$. So $\Lambda:=65/6$ works uniformly for $m=2,3$.

Feeding this into Step 17's estimate $\bar K\le \tfrac94\,\chi(M)/A+C$ (whose $9/4$ I confirm from $\mathrm{Vol}\to32\pi^2A/9$ and $\int|Rm|^2\approx8\pi^2\chi(M)+O(\mathrm{Vol})$) gives $\bar K\le \tfrac94\cdot\tfrac{65}{6}+C$, i.e. a volume-independent bound. The uniformity Step 17 wants is therefore genuinely available — provided §5.

## 5. The real additional input, and the BMY misattribution

Step 17 writes that "the Bogomolov–Miyaoka–Yau inequality ensures $\chi/A\ge1/3$, so the bound $\Lambda$ is automatic." This is the wrong direction for what is needed. BMY reads $c_1^2\le 3c_2$, i.e. $c_2\ge c_1^2/3$ — a **lower** bound on $c_2$ (and hence on $\chi$). The quantity that must be controlled for bounded $\bar K$ is an **upper** bound on $\chi(M)/A$, which BMY does not give. The upper bound comes from **Noether's inequality** (§1), together with $b_+(N)=0$ (§3). The two inequalities delimit the surface geography from opposite sides; only the Noether side is load-bearing here.

The one genuinely necessary extra hypothesis is that **every $X_j$ is of general type** ($c_1^2(X_j)>0$). Concretely, take $m=2$, $X_1$ general type with $c_1^2=a_1$, and $X_2=E(n)$ ($n$ even $\ge4$: minimal properly elliptic, $b_1=0$, $b_+=2n-1\equiv3\bmod4$, nonzero mod-2 SW, so admissible for Theorem D). Then $A=a_1$ is fixed while $\chi(M)\ge c_2(E(n))=12n\to\infty$, so $\chi(M)/A\to\infty$ and $\bar K$ is unbounded. Ishida–LeBrun Theorem D (which defines the critical obstruction at $D=A/3$) does **not** exclude such summands; only the sharp $\mathcal I_r$ Theorem C, whose gluing uses Kähler–Einstein orbifold canonical models, effectively needs general type. So the general-type restriction must be stated explicitly for the uniform-$\Lambda$ result; it is the true "missing input," and it is on the $X_j$, not on $N$.

## 6. Net corrected statement (reusable)

For $M=(\#_{j=1}^m X_j)\#N$, $m\in\{2,3\}$, with

- each $X_j$ minimal complex **of general type** ($c_1^2(X_j)>0$), satisfying the Ishida–LeBrun conditions (1–3);
- $b_+(N)=0$;
- critical relation $D=4m-(2\chi+3\tau)(N)=A/3$, $A=\sum c_1^2(X_j)$,

one has, unconditionally,
$$\chi(N)=\tfrac{A}{3}-4m+6-6b_1(N)\le\tfrac{A}{3}-4m+6,\qquad
\frac{\chi(M)}{A}\le \frac{16}{3}+\frac{30m+6}{A}\le \frac{65}{6},$$
with $A\ge12(m-1)$. Hence $\chi(M)/A$ and $\bar K$ are bounded by dimension-only constants, uniformly across such critical families. The bound rests on Noether's formula and Noether's inequality (surfaces) and on $b_+(N)=0$ (the $N$ summand); it does **not** rest on BMY, and it **breaks** if non-general-type summands ($c_1^2=0$, e.g. high-$n$ elliptic surfaces) are admitted.

## What remains open in this arithmetic layer

Nothing in the topological accounting is unresolved once general-type $X_j$ is stated: the two-sided control of $\chi(M)/A$ is exact. The one item worth a line in any write-up is a consistency note that the Bauer–Furuta monopole bound $(a^+)^2\ge A$ is only nontrivial when $A>0$, which again is exactly the general-type condition — so the general-type restriction is natural rather than ad hoc, but it is a real hypothesis distinct from the $b_+(N)=0$ hypothesis and should be carried explicitly through Steps 17–18 wherever "bounded $\chi/A$" is invoked.