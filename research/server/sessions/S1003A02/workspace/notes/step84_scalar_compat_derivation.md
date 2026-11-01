# Step 84: Independent derivation of the scalar compatibility operator

## Statement

**Proposition 84.P.** Let $L_d : H_{d+2} \to E_d$ be the flat top map of the anti-$J$ truncated power-series tower (symmetric 2-tensors of degree $d$, with $H_{d+2}$ a tracefree anti-$J$ polynomial metric perturbation of degree $d+2$ and $E_d$ the degree-$d$ part of $\operatorname{Ric}(e^H)-\lambda e^H$). Define the scalar operator
$$
\mathcal P(E) \;=\; J^i{}_a\, J^j{}_b\,\partial_a\partial_b E_{ij}\;-\;\tfrac12\,\Delta\operatorname{tr}E.
$$
Then for $d = 4, 6, 8$:

1. $\mathcal P$ annihilates the image of $L_d$: $\mathcal P(L_d\, h) = 0$ for every anti-$J$ tracefree $h$.
2. The cokernel of $L_d$ is spanned exactly by the linearized Bianchi rows $B_d$ and the degree-$(d-2)$ coefficients of $\mathcal P(E_d)$:
$$
\operatorname{coker}(L_d) = B_d \oplus \mathcal P_d, \qquad
\dim = 4\binom{d+2}{3} + \binom{d+1}{3}.
$$
3. The radial class $\Delta^{(d-2)/2}\mathcal P(E_d)(0)$ is independent of $B_d$.
4. At $d=6$, the radial class equals the universal multiplier $\ell$ of §23.5 (modulo Bianchi, $|\cos|=1$ to $2\times10^{-16}$ across all four saved jets).

## Proof ingredients

**(a) Fourier identity.** In Fourier space, the linearized Ricci symbol maps a symmetric 2-tensor $h$ with momentum $k$ to
$$
\widehat{(\delta\operatorname{Ric})}_{ij}(k) = -\tfrac12|k|^2 h_{ij} + \tfrac12(k_i k_m h_{jm} + k_j k_m h_{im}) - \tfrac12 k_i k_j \operatorname{tr}h.
$$
For anti-$J$ $h$ (i.e. $J^ThJ=-h$; such $h$ is automatically tracefree, since $\operatorname{tr}h=\operatorname{tr}(J^ThJ)=-\operatorname{tr}h$) the proof is two lines. Write $R=\widehat{dRic}(h)$ and use $Jk\perp k$:
$$
(Jk)^TR(Jk)=-\tfrac12|k|^2(Jk)^Th(Jk)=\tfrac12|k|^2\,k^Thk,\qquad \operatorname{tr}R=k^Thk,
$$
so $\widehat{\mathcal P}(R)=(Jk)^TR(Jk)-\tfrac12|k|^2\operatorname{tr}R=0$. (The overall sign of $J$ and of the symbol is irrelevant; $\mathcal P$ is quadratic in $J$.) The script confirms this at 500 random momenta on the 6-dimensional anti-$J$ space (value $0.0$ in floating point) and gives values of size $\sim10^2$ for generic $h$.

**Not a Bianchi consequence.** Every Bianchi-generated functional vanishes on $dRic(h)$ for *all* $h$. For the conformal direction $h=f\,\delta$ one finds $R=-\tfrac12|k|^2f\,\delta-f\,k\otimes k$, $(Jk)^TR(Jk)=-\tfrac12|k|^4f$, $\operatorname{tr}R=-3|k|^2f$, hence $\widehat{\mathcal P}(R)=|k|^4f$, i.e. $\mathcal P(dRic(f\delta))=\Delta^2f$ (up to the symbol sign). Since $\Delta^2$ maps degree-$(d+2)$ polynomials onto degree-$(d-2)$ polynomials, the $\binom{d+1}3$ coefficients of $\mathcal P$ are independent modulo Bianchi. So $\mathcal P$ is exactly the compatibility created by restricting to anti-$J$ (fixed-$\omega$, Darboux) perturbations: the conformal and $J$-invariant directions that would fill it are absent.

**Symbol count.** At fixed $k\ne0$, anti-$J$ $h$ is 6-dimensional and the Hamiltonian gauge $h=\mathcal L_{X_\phi}\delta$ contributes a 1-dimensional symbol kernel, so the symbol image is 5-dimensional in the 10-dimensional space of symmetric tensors. Its annihilator is 5-dimensional, which is exactly Bianchi (4) plus $\mathcal P$ (1). The degree-by-degree statement below is the polynomial version, checked by exact rank counts.

**Uniqueness of the radial class.** $\mathcal P$ is $U(2)$-equivariant. $U(2)$ acts transitively on $S^3\subset\mathbb C^2$, so the only $U(2)$-invariant polynomials are polynomials in $|z|^2$. Consequently the invariant linear functionals on degree-$m$ polynomials are spanned by $f\mapsto\Delta^{m/2}f(0)$ when $m$ is even, and there are none when $m$ is odd. The radial class $\Delta^{(d-2)/2}\mathcal P(E_d)(0)$ is therefore the unique $U(2)$-invariant compatibility at even $d$, and none exists at odd $d$.

**(b) Rank computation.** The script `step84_scalar_compat.py` builds the $B_d$ and $\mathcal P_d$ row matrices and $L_d$ in the TowerAll tower (which uses anti-$J$ Darboux coordinates, matching all previous computations). It verifies:

| $d$ | rows $E_d$ | rank $L_d$ | coker | rank $B$ | rank $\mathcal P$ | $B+\mathcal P$ | $|BL|$ | $|PL|$ |
|---|---|---|---|---|---|---|---|---|
| 4 | 350 | 260 | 90 | 80 | 10 | 90 | 0 | 0 |
| 6 | 840 | 581 | 259 | 224 | 35 | 259 | 0 | 0 |
| 8 | 1650 | 1086 | 564 | 480 | 84 | 564 | 0 | 0 |

In every case $\operatorname{rank}(B)+\operatorname{rank}(\mathcal P)=\operatorname{coker}$, with the joint rows independent and both annihilating $\operatorname{im}(L_d)$ exactly. The excess count $\binom{d+1}{3}=10,35,84$ matches $\operatorname{rank}(\mathcal P)$.

**(c) Radial identification.** For $d=6$, the radial functional $e\mapsto\Delta^2\mathcal P(e)(0)$ is independent of the Bianchi span. The saved universal multiplier $\ell$ (from `data/step80/universal_pi.npz`, four jets) has $|\cos(\ell\bmod B,\text{radial}\bmod B)|=1$ to machine precision. The fraction of $\ell$ outside the Bianchi span is $>0.9999$, confirming that $\ell$ is essentially the $\mathcal P$-radial row.

## Consequence for Q4

$\Phi_6 \le 0$ is the semialgebraic condition imposed by the scalar compatibility $\mathcal P$: it is the minimal radial fourth moment $\Delta^2\mathcal P(E_6)(0) \le 0$ in the parameterisation of §23.5. This is an algebraic relation between the first jet $(c,S,A)$, the Einstein constant $\lambda$, and the background curvature at a torsion zero, not an obstruction. The order-8 cokernel consists of $\binom93=84$ $\mathcal P$-rows and $4\binom{10}3=480$ Bianchi rows, all of which annihilate $\operatorname{im}(L_8)$.

## Order-8 arbitration at gen5, $\lambda=-5$ (task s83_t7_tool1)

Our order-8 run at exactly A01's point, `data/step81/order8_F012gen5_lam-5.json`, starts on the order-6 solution ($r_6=1.4\times10^{-8}$, total residual $4.3\times10^3$, all of it in $r_8$). After 150 LM iterations the residual is $0.317$ and still decreasing, $r_6$ has degraded to $0.22$, and the projected Jacobian has rank 91, the same as at gen2. The same file records `M_rank_w_to_r8 = 28`.

This settles the rank question. The variable projection in `step81_order8.py` removes the range of the constant matrix $M_w$ (the $H_8$-kernel directions $w\in\ker L_6$) from the $r_8$ rows. Since $M_w$ has rank 28, the projected system has $259+564-28=795$ rows, which is exactly the recorded `n_rows`. Its nontrivial rows number $35+(84-28)=91$. **Rank 91 is therefore full rank**, not a deficiency. The earlier comparison 91/119 counted the 28 rows that $w$ already absorbs. The number 28 is independently A01's rank of the newest jet on the radial/$\mathcal P$ rows at $d=8$ (§23.6(iii)), so the two pipelines agree structurally. At gen2 and gen5 alike, the order-8 Jacobian of our reduced system is surjective onto its nontrivial rows. This agrees with A01's rank-84 submersion, which is the same statement before $w$ is eliminated ($84=28+56$).

The LM stagnation is therefore a global-path effect. LM started from the order-6 root is far from an order-8 root ($\|r_8\|\sim10^3$), and the order-6 surface is curved: LM leaves it, and $r_6$ grows. A homotopy along $\{r_6=0\}$ (A01's method) is the appropriate instrument. Neither pipeline has yet produced a completed order-8 jet in this Session, so order-8 solvability remains [N, undecided] here. No rank obstruction exists at order 8 at either jet tested.

## Files

- Script: `workspace/scripts/step84_scalar_compat.py`
- Data: `workspace/data/step84/scalar_compat.json`
- Dependencies: step79_general_order6 (tower), step80_universal_pi (ell reference)

## Order-8 witness (A01 polished jet, evaluated here)

A01's order-8 continuation at gen5, $\lambda=-5$ (message #862) was evaluated in our unreduced tower by `scripts/step84_eval_a01_order8.py`, with output in `data/step84/eval_a01_order8_gen5_lam-5.json`.

| Residual | Value | Comparison scale |
|---|---|---|
| $E_0$ | $2.7\times10^{-15}$ | |
| $E_2$ | $3.5\times10^{-12}$ | |
| $E_4$ | $2.6\times10^{-10}$ | |
| $E_6$ | $4.5\times10^{-9}$ | $5.3\times10^6$ with $H_8=0$ |
| $E_8$ | $9.8\times10^{-7}$ | $1.5\times10^8$ with $H_{10}=0$ |

Relative to these scales, both top-order residuals are about $10^{-15}$.

The torsion jet is unchanged from the order-6 point: it lies on the cone and has $\det Df=0.0234>0$, so the zero has index $+1$. The order-8 point lies elsewhere on the order-$\le6$ solution variety; its distances from our Step-80 values are $2.5$ for $H_4$ and $12.9$ for $H_6$. The coefficients grow quickly with degree, from $\|H_4\|\approx1.6\times10^3$ to $\|H_{10}\|\approx8.6\times10^6$ at unit torsion norm. Convergence of the formal germ is therefore not addressed by this evidence.

Conclusion [N]: there is no local formal obstruction through order 8 at a nondegenerate AKE torsion zero. Two independent equation systems agree on this. Our own homotopy (`scripts/step84_order8_homotopy.py`) stalled at $t\approx0.035$ because its corrector tolerance of $10^{-8}$ sits at the residual floor for this coefficient scale. A rerun (s84_t30) was cancelled as redundant once the cross-evaluation succeeded.
