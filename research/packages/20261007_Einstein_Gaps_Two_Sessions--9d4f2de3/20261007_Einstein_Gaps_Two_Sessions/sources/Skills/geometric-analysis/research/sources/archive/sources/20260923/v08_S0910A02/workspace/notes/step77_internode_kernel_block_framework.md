# Step 77: mixed-chirality inter-node kernel block — faithful obstruction framework

Session `S0910A02`. Agent2 / Constructor. Phase Execute.

## 0. Scope

The active target remains the full Yau Problem 26 for every closed connected smooth
manifold in every dimension.  The computation described here is a **local
nearby-orbifold diagnostic** on the product quotient $(S^2\times S^2)/\mathbb Z_2$,
$\operatorname{Ric}(g_o)=\Lambda g_o>0$.  Its outcome chooses which continuation
is live (tower rigidity vs. global existence), it does not prove or refute $P_4^+$
or Yau–26.

## 1. Pattern-blind vanishing (local order $t$ and $t^2$)

On the product orbifold $O=(S^2\times S^2)/\mathbb Z_2$:

- $\nabla\operatorname{Rm}\equiv0$ (product of round spheres, parallel curvature).
- The reflection $c(z,w)=(\bar z,w)$ is an isometry that fixes every $A_1$ node
  and exchanges $\Lambda^+\leftrightarrow\Lambda^-$.
- $R^+=R^-=\operatorname{diag}(\Lambda,0,0)$ at each node, with
  $\ker R^\pm=\operatorname{span}\{\omega_2^\pm,\omega_3^\pm\}$ (2-dimensional).

Because $\nabla\operatorname{Rm}=0$, the local 2-jet $H_2$ is the same algebraic
object at all four nodes.  Because $c$ fixes nodes and exchanges chiralities, the
local Ozuch coefficients $\lambda_k$, $\mu_k$ (equations (28)/(40), (21)/(23),
Lemma 2.14 in the Ozuch source) are **identical for compatible and reversed**
EH insertions.  Thus the order-$t$ and order-$t^2$ obstruction equations are
**pattern-blind**: they cannot distinguish any $r\in\{0,1,2,3,4\}$.

On the $r=0$ (all-compatible) control, the Kähler–Einstein desingularization (degree-4
del Pezzo) exists as an open family in the gluing parameters, giving $4$ complex
smoothing parameters modulo $(\mathbb C^*)^2$ (gauge), a 4-real-dimensional
desingularization family.  Its existence forces all local necessary conditions (Ozuch
equations (22), (23), and all $\nu_l$-projections) to be identically satisfied.
Therefore:

$$
\lambda_k^j(\phi_j,0)=0,\qquad \mu_1^j=0,
\qquad\text{for all $j$, all $k$, every pattern.}
$$

The compatible-$\mu_1$ vanishing also follows directly from Lemma 2.14:
$\mu_1=C\det\bigl(\begin{smallmatrix}R_{22}&R_{23}\\R_{32}&R_{33}\end{smallmatrix}\bigr)
=C\det(0)=0$.

**Zero-checks verified** (Step 77 script `step77_internode_kernel_block.py`):

| Check | Status |
|-------|--------|
| SD/ASD form algebra | ✓ |
| Same-chirality commutator zero on kernel: $\langle[A,R^+]\zeta,\zeta'\rangle=0$ for all $A\in\mathfrak{so}(3)$ and $\zeta,\zeta'\in\ker R^+$ | ✓ |
| Compatible bare $\mu_1=0$ (rank-one kernel block det) | ✓ |

## 2. Where chirality enters: inter-node mixed-chirality kernel block

### 2.1 Chirality split (Ozuch §1.2, eq. (9))

The EH multipole tensor $H^4(\zeta^+)$ has linearized curvature response
$$
d_e R^-(H^4(\zeta^+))=\frac{12\pi_{\mathrm{tr}}(\rho(\zeta)^-\otimes\rho(\zeta)^-)}{r^6}
$$
which lives **purely in $\operatorname{End}(\Omega^-)$** — the ASD curvature sector.
A self-dual multipole $\zeta^+$ shifts $R^-$, not $R^+$.  Symmetric statement for
$\zeta^-$ shifting $R^+$.

This is the algebraic engine: at a **compatible** receiver (kernel in $R^+$, say), a
compatible (SD) source's response shifts $R^-$, which is **orthogonal** to the
receiver's obstruction block.  A **reversed** (ASD) source shifts $R^+$, which is
exactly the receiver's block.

### 2.2 Same-chirality zero-check

A compatible source's response, being tangent to the Kähler family, perturbs
$R^{\epsilon_j}$ by an infinitesimal frame rotation $\delta R^{\epsilon_j}=[A,R^{\epsilon_j}]$
with $A\in\mathfrak{so}(3)$.  Since $R^+=\operatorname{diag}(\Lambda,0,0)$,

$$
[A,R^+] = \Lambda\begin{pmatrix}0&-A_{12}&-A_{13}\\A_{12}&0&0\\A_{13}&0&0\end{pmatrix}.
$$

The kernel 2×2 block (rows 2–3, cols 2–3) is identically **zero** for all $A$.  Hence
same-chirality interactions produce no obstruction on $\ker R^+$.

### 2.3 The decisive object

A **reversed** source at node $i$ with chirality $\epsilon_i\ne\epsilon_j$ produces,
at receiver $j$, a regular second jet $H_{ij,2}$ of the orbifold Green response
$\bar h_i^4$.  This shifts the effective $H_{j,2}$ entering Ozuch's first obstruction:
$$
\delta\lambda_{j,k} = c\langle R^{\epsilon_j}(H_{ij,2}[\phi_i^{\epsilon_i}])\,\zeta_j,\,\zeta_{j,(k)}\rangle,
$$
entering at scale order $t_jt_i^2$ (order $t^3$ at equal scales).

The **mixed-chirality inter-node kernel block** is the symmetric 2×2 matrix
$$
\boxed{M_{ji}^{\epsilon_j}[\phi_i]
=\Pi_{\ker R^{\epsilon_j}}\;R^{\epsilon_j}(H_{ij,2}[\phi_i^{\epsilon_i}])\;
\Pi_{\ker R^{\epsilon_j}}}
$$

where $H_{ij,2}$ is the second jet at node $j$ of the solution $\bar h_i^4$ to
Ozuch's equation (35), evaluated from the projected product-$P$ pseudo-inverse
with additive spectral denominators.

### 2.4 Two geometry types

There are only two inter-node geometries (by node-pair structure):

- **M_adj** (adjacent pair): nodes differ in one $S^2$ factor (coincident in the
  other, e.g. $(N,N)\to(N,S)$).  Distance $\pi/\sqrt\Lambda$ in the diagonal product
  metric.

- **M_diag** (diagonal pair): nodes differ in both factors (antipodal in both,
  e.g. $(N,N)\to(S,S)$).  Distance $\pi\sqrt2/\sqrt\Lambda$.  Regular in both
  one-factor perspectives.

Both are regular at the receiver in the full four-dimensional product resolvent
(only the source/self node requires singular subtraction).  But M_diag is cleanest
to compute first because it is regular in each one-factor projection separately.

## 3. Pattern algebra (verified by executable)

From `workspace/data/step77_internode_kernel_block.json`:

### 3.1 Controls

$r=0$ (all compatible) and $r=4$ (all reversed): **zero mixed pairs**.  The
obstruction system is vacuous at this order; both endpoints have KE
desingularizations.

### 3.2 Patterns

| Pattern | Independent class | Reversed nodes | Mixed coupling per compatible receiver | Coupling types |
|---------|-------------------|----------------|---------------------------------------|----------------|
| $r=1\sim r=3$ | Yes | 1 (or 3) | single reversed source | **M_adj** or **M_diag** depending on geometry |
| Diagonal spin $r=2$ | Yes | 2 (antipodal) | two reversed sources | **M_adj** + **M_adj** (all adjacent couplings!) |
| Adjacent nonspin $r=2$ | Yes | 2 (share pole) | two reversed sources | **M_adj** + **M_diag** |

**Key finding:**  The diagonal spin pattern ($\#_3(S^2\times S^2)$) is governed
purely by $M_\mathrm{adj}$.  The adjacent nonspin pattern
($3\mathbb{CP}^2\#3\overline{\mathbb{CP}}{}^2$) needs both $M_\mathrm{adj}$ and
$M_\mathrm{diag}$.  And $r=1$ also needs both.

### 3.3 Decision table

| Outcome | $r=1/r=3$ | Diagonal spin | Adjacent nonspin |
|---------|-----------|---------------|-----------------|
| $M_\mathrm{adj}=0,M_\mathrm{diag}=0$ | unobstructed | unobstructed | unobstructed |
| $M_\mathrm{adj}\ne0,M_\mathrm{diag}=0$ | obstructed (by adj receivers) | obstructed | may have solutions |
| $M_\mathrm{adj}=0,M_\mathrm{diag}\ne0$ | obstructed (by diag receiver) | unobstructed | may have solutions |
| Both $\ne0$ | obstructed | obstructed | may have solutions if cancellation works |

If either $M_\mathrm{adj}$ or $M_\mathrm{diag}$ is invertible, $r=1/r=3$ has no
Einstein desingularization of this degeneration (because each compatible receiver
sees a **single** reversed source with no tunable in-kernel freedom).

## 4. Source-pinning

**Ozuch formulas used:**

1. First obstruction (eq. (28)/(40), lines 512–514, 653):
   $\lambda_k(\zeta^\pm) = c\langle R^\pm(H_2)\zeta^\pm,\zeta_{(k)}^\pm\rangle$.

2. Chirality split (eq. (9), lines 332–341):
   $d_e R^-(H^4(\zeta^+)) = 12\pi_{\mathrm{tr}}(\rho(\zeta)^-\otimes\rho(\zeta)^-)/r^6$.

3. Multi-singularity extension (eq. (39)/(42), lines 640–647):
   $\bar h^4 = \sum_j \bar h_j^4$ with $P_o\bar h^4\in\mathbf{O}(g_o)+\sum\lambda_k\bar{\mathbf o}^4_k$.

4. Local second obstruction (Lemma 2.14/Biq16 Lemme 9, lines 673–704):
   $\mu_1 = C\det R_{\ker}$ — vanishes for rank-one $R^\pm$.

5. Inter-node regularity (lines 640–646, 903–905):
   at node $j\ne i$, $\bar h_i^4 = H_{ij,0}+H_{ij,2}+O(r_j^4)$ — no singular part.

**Product-orbifold-specific:**

6. $\nabla\operatorname{Rm}=0$: H₂ is a global parallel curvature form.
7. Reflection $c$: fixes nodes, exchanges chiralities, makes all local coefficients
   pattern-blind.
8. $r=0$ KE control: open del Pezzo family forces all local necessary conditions
   to vanish.

## 5. What M_adj and M_diag require to compute

The Green response $H_{ij,2}$ is the second jet at node $j$ of the projected
pseudo-inverse solution to Ozuch (35), sourced by $H^4(\zeta_i^{\epsilon_i})$ at
node $i$.  The computation needs:

1. **Projected product-$P$ Green/resolvent** with additive spectral denominators
   $1/(\lambda_1+\lambda_2+\kappa_{\mathrm{tensor}})$.  Not a product of static $S^2$
   Green functions (Step 76 audit, additive obstruction $xy\ne0$).

2. **Negative-mode treatment**: $g_1-g_2$ has $P(g_1-g_2)=-\Lambda(g_1-g_2)$; the
   negative eigenspace is one-dimensional and contributes $(-1/\Lambda)\Pi_{g_1-g_2}$.

3. **Zero-mode (scalar kernel) treatment**: four modes
   $\{u_1g_1,u_1g_2,u_2g_1,u_2g_2\}$ in $\ker P$.  Their $\nu_l$-projections have
   Bianchi-corrected local quadratic pairing equal to zero (A01 Step 77 audit).
   Either include them as Ozuch $\nu_l$ equations or remove by a derived
   Bianchi/diffeomorphism slice.

4. **Spectral sum convergence**: pole second-jet coefficients $P_l''(1)\ne0$ for all
   $l\ge2$, so infinitely many harmonics contribute in each allowed character channel.
   Need closed-form summation, heat-kernel integral, or certified alternating-series
   tail bounds.

5. **T² selection rule**: pole jets restricted to $|m_a|\le2$, quotient parity
   $m_1+m_2\equiv0\pmod2$, EH kernel-product block characters $(±2,0),(0,±2)$.

The **diagonal pair** is the cleanest first target: antipodal in both factors,
regular in each one-factor projection, larger $D_8$ stabilizer (order 4), and
the working $\#_3(S^2\times S^2)$ topology link.  M_diag alone decides the $r=1$
diagonal receiver, and if M_adj is also needed, the adjacent pair has one coincident
factor requiring more careful resolvent treatment.

## 6. Pattern-blind vanishing of local μ_k: structural evidence and remaining gap

### 6.1 Unconditionally proved

| Coefficient | Status | Method |
|---|---|---|
| $\mu_1=0$ | **Proved** | Rank-one determinant: $\mu_1=C\det(R_{\ker})=0$ (Ozuch Lemma 2.14) |
| $\nu_l=0$ for in-kernel $\zeta$ | **Proved** | A01's scalar decoupling: $H^4(\zeta)$ factor-traceless for $\zeta\in\ker R$ |
| $\nu_l=0$ by symmetry | **Proved** | A01's $A$-symmetry: scalar kernel modes are $A$-odd |

### 6.2 μ₂=μ₃=0: strong structural support with a parameter-matching gap

**Conditional theorem.** If there exists a comparable-scale KE desingularization sequence
approaching the product orbifold with Ozuch parameters satisfying
$\lambda_k(\phi_j(t),v(t))=o(t_j)$, then $\mu_2=\mu_3=0$.

*Proof sketch.* With the stated condition, $t_j^2\mu_k=O(t_{\max}^{5/2})$ at comparable
scales forces $\mu_k=0$ (since $\mu_k$ is $t$-independent). Pattern-blindness via
$c$-symmetry and $D_8$ extends to all chiralities and nodes.

**The gap** (identified by TTCS verification): the Ozuch equation is
$$
t_j\lambda_k^j(\phi_j(t),v(t))+t_j^2\mu_k^j(\phi_j(t),v(t))=O(t_{\max}^{5/2}).
$$
If $\phi_j(t)=\phi_{j,0}+t_j\dot\phi_j+o(t_j)$ and $v(t)=t_jv_1+o(t_j)$, then
even with $\lambda_k(\phi_{j,0},0)=0$, the variation gives
$$
D_\phi\lambda\cdot\dot\phi_j+D_v\lambda\cdot v_1+\mu_k(\phi_{j,0},0)=0,
$$
which does not force $\mu_k=0$ unless $D_\phi\lambda\cdot\dot\phi_j+D_v\lambda\cdot v_1=0$.

**Partial closure via scalar decoupling.** Ozuch's Corollary 2.12 (lines 655–666) gives
$$
\sum_j|\zeta_j|\lambda_1^j(\zeta,v)=C\sum_l\langle v,\mathbf v_l\rangle\nu_l(\zeta,0)+O(\|v\|^2|\zeta|^2).
$$
Since $\nu_l(\zeta,0)=0$ for in-kernel $\zeta$ (scalar decoupling), the $D_v\lambda$
term vanishes at leading order for $k=1$. The extension to $k=2,3$ requires the analogous
transverse Corollary, which is not stated in the available source.

**Degree correction (TTCS).** The all-compatible resolution $r=0$ gives
$\mathbb{CP}^2\#5\overline{\mathbb{CP}}{}^2=\mathrm{Bl}_5\mathbb{CP}^2$ (degree-4 del Pezzo),
not $\mathrm{Bl}_4\mathbb{CP}^2$ as incorrectly written earlier.

**Assessment.** The algebraic evidence strongly supports $\mu_2=\mu_3=0$:
rank-one orthogonality ($R^-\cdot\rho(\zeta)^-=0$), scalar decoupling ($\nu_l=0$),
pattern-blind structure ($\nabla\operatorname{Rm}=0$, $c$-symmetry).
The clean unconditional closure is the direct Biq16 formula computation at one convenient
angle (e.g. $\zeta=\omega_2^+$, $\alpha=0$), as A01 identified. SO(2) covariance,
reflection, and node symmetry then cover all directions, chiralities, and nodes.

## 7. Combined structural conclusion

Combining the results of this note with A01's Step-78 equivariant diagonal reduction:

| Obstruction | Status | Method |
|---|---|---|
| First: $\lambda_k$ | $=0$ for in-kernel $\zeta$ | Rank-one $R^\pm$ has 2D kernel |
| Second: $\mu_1$ | $=0$ | Rank-one determinant (Lemma 2.14) |
| Second: $\mu_2,\mu_3$ | Strongly supported $=0$, gap remains | r=0 KE control + scalar decoupling; Biq16 check needed |
| Scalar $\nu_l$ | $=0$ | Scalar decoupling (A01 Thm 3.1) and $A$-symmetry (A01 Thm 2.1) |
| Inter-node coupling | $O(t^3) \ll O(t^{5/2})$ | Below Ozuch remainder |

**The product quotient passes all unconditionally checked Ozuch obstructions for every
chirality pattern.  The remaining check is $\mu_2=\mu_3=0$, strongly supported but
requiring the Biq16 formula computation or a precise KE parameter-matching theorem.**

If $\mu_2=\mu_3=0$ is confirmed: with the scalar kernel eliminated (A01 Thm 2.1) and
the non-scalar operator positive definite (spectral gap $\ge\Lambda$, A01 §7), the
remaining problem becomes **purely analytical**: a weighted inverse estimate on the
non-scalar sector plus nonlinear contraction.  If this succeeds, it would produce exact
positive Einstein metrics on every mixed-chirality resolution of the product orbifold,
including $\#_3(S^2\times S^2)$ and $3\mathbb{CP}^2\#3\overline{\mathbb{CP}}{}^2$.

**This does NOT prove $P_4^+$ or Yau-26.** It establishes that the product quotient
is an unobstructed candidate for Einstein desingularization in every chirality
pattern.  Whether the analytical estimates close is a separate PDE problem, and
global Einstein existence far from this orbifold degeneration remains unaddressed.

## 8. Order bookkeeping

Following Step 76 Preceptor correction and A01 Step 77 repair:

$$
F_{j,k}=\underbrace{t_j\lambda^{(0)}_{j,k}}_{\text{pattern-blind}=0}
+\underbrace{t_j^2\mu^{(0)}_{j,k}}_{\text{pattern-blind}=0}
+\underbrace{\sum_{i\ne j,\;\epsilon_i\ne\epsilon_j}
t_jt_i^2\langle M_{ji}\phi_j,\phi_{j,(k)}\rangle}_{\text{mixed chirality: decisive}}
+\underbrace{\text{same chirality}}_{\text{zero on kernel}}
+O(t_{\max}^{5/2}).
$$

At equal scales $t_j\sim t_i\sim t$, the pattern-dependent term is order $t^3$,
which is below Ozuch's resolution of $O(t^{5/2})$ in Theorem 0.2.  Thus the
computation explores **beyond** the current Ozuch estimates and tests whether a
higher-precision construction can succeed.

## Files

- Script: `workspace/scripts/step77_internode_kernel_block.py`
- Data: `workspace/data/step77_internode_kernel_block.json`
- Source: Ozuch `Knowledge/objects/papers/Higher-order-obstructions-to-the-desingularization-of-Einstein-metrics--94f76f3b5378--19c12fb27fae/object.md`
- Step 76 audit: `workspace/notes/step76_preceptor_audit_mixed_green_factorization.md`
- A01 repair: `Sessions/S0910A01/workspace/notes/step77_mixed_row_obstruction_repair.md`
