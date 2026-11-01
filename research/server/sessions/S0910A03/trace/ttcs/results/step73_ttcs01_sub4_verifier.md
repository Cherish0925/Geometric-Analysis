# TTCS Independent Branch Record

```json
{
  "step_id": 73,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step73_tail_completion_and_core_entry.md",
    "Sessions/S0910A03/workspace/scripts/step73_expanding_tail_verify.py",
    "Sessions/S0910A03/workspace/data/step73_expanding_tail.json",
    "Sessions/S0910A03/workspace/data/step72_conformal_gauge_system.json",
    "Sessions/S0910A03/trace/ttcs/results/step72_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Independently verify the mathematical content of the Step 73 note and computation. Check (i) all five Ricci-defect formulas for the explicit expanding tail, including which mixed components vanish; (ii) the exact operator-norm formula, N-independence, endpoint matching, shape operator, and normal balance; (iii) the general adiabatic tail formulas for h=e^{2a}q_{(r-r0)/K}, including the rr, tangential, and mixed components and the stated C(epsilon+K^-1+K^-2+e^-2a0) estimate; (iv) the exact core decomposition equations in a volume-preserving gauge; and (v) the warning that the 3-equation conformal-gauge elliptic subsystem does not automatically solve the remaining constraints. Identify and repair any wrong sign, coefficient, norm factor, unstated regularity/geometric assumption, or conclusion whose scope is too broad. Return a direct mathematical memo with corrected formulas and what the tail result genuinely establishes for the graph-neck route.

## Output

# Independent verification — Step 73 adiabatic tails and core-entry system

Session S0910A03. I re-derived every formula from the multiply-warped-product Ricci identities rather than re-running the supplied script, then cross-checked against the script and JSON. The mathematical content of Step 73 holds. Below are the confirmations, three refinements, and a precise statement of what the tail genuinely delivers.

## 0. Master Ricci formulas (foundation for everything)

I re-derived the five Step-72 components for
$$g=e^{2\phi}(dt^2+dz^2)+e^{2b}dx^2+e^{2c}dy^2,\quad \phi,b,c=\phi,b,c(t,z),$$
treating it as a multiply-warped product over the $2$D conformal base $g_B=e^{2\phi}\delta$ with two flat $1$D fibers. Using the standard fiber formula $\operatorname{Ric}(\hat e_x,\hat e_x)=-\big(\tfrac{\Delta_{g_B}e^b}{e^b}+\tfrac{\langle\nabla e^b,\nabla e^c\rangle}{e^be^c}\big)$ and the base formula $\operatorname{Ric}(X,Y)=\operatorname{Ric}_{g_B}(X,Y)-e^{-b}H^{e^b}(X,Y)-e^{-c}H^{e^c}(X,Y)$, with $\Delta_{g_B}=e^{-2\phi}\Delta_{\rm flat}$ and the conformal Christoffel symbols, I obtain term-by-term agreement with the `tt`, `zz`, `tz`, `xx`, `yy` strings in `step72_conformal_gauge_system.json`. This confirms the entire downstream computation rests on correct curvature identities. The elliptic determinant `det_ttzz_xx_yy = 2*(tau^2+xi^2)^3` also checks: $(2\tau^2+2\xi^2)(\tau^2+\xi^2)^2$.

## (i)–(ii) Explicit expanding tail — confirmed exactly

For $g=dr^2+e^{2r}[dz^2+N^{-2}e^{v}dx^2+N^{-2}e^{-v}dy^2]$ I recomputed via the multiply-warped structure over the hyperbolic base $dr^2+e^{2r}dz^2$ ($K_{\rm Gauss}=-1$), with $b=r-\log N+v/2$, $c=r-\log N-v/2$, $\sigma=b+c=2r-2\log N$, $d=b-c=v$:

- **Fiber components.** $\operatorname{Ric}(\hat e_x,\hat e_x)=-3-\tfrac12(v_{rr}+3v_r+e^{-2r}v_{zz})$, hence
$$E_x=-\tfrac12 L,\quad E_y=+\tfrac12 L,\quad L:=v_{rr}+3v_r+e^{-2r}v_{zz}.\ \checkmark$$
- **Base block.** Since $\nabla^2\sigma=2\nabla^2 r=\operatorname{diag}(0,2)$ (orthonormal) and $db\otimes db+dc\otimes dc$ contributes $\operatorname{diag}(2+\tfrac12 v_r^2,\ 2+\tfrac12 e^{-2r}v_z^2)$ with off-diagonal $\tfrac12 e^{-r}v_rv_z$, all constant "$2$" and "$-1$" pieces cancel the $3g$ shift, leaving exactly
$$E|_B=-\tfrac12\,dv\otimes dv.\ \checkmark$$
This gives $E_{rr}=-\tfrac12 v_r^2$, $E_{zz}=-\tfrac12 e^{-2r}v_z^2$, $E_{rz}=-\tfrac12 e^{-r}v_rv_z$.
- **Which mixed components vanish.** Base–fiber ($rx,ry,zx,zy$) and fiber–fiber ($xy$) all vanish by the multiply-warped identities; the base $rz$ term does not. The note's inline phrase "base $rz$ component is $-v_rv_z/2$" quotes the $(dr,dz)$-coordinate component of $-\tfrac12dv\otimes dv$; the **orthonormal** value carries $e^{-r}$: $E(\hat e_r,\hat e_z)=-\tfrac12 e^{-r}v_rv_z$. No result depends on this distinction because the operator norm uses eigenvalues.
- **Operator norm.** $E$ is block diagonal ($2\times2$ base $\oplus\,E_x\oplus E_y$). The base block is rank one with eigenvalues $\{-\tfrac12|dv|_{g_B}^2,0\}$, $|dv|_{g_B}^2=v_r^2+e^{-2r}v_z^2$. Hence
$$\|E\|_{\rm op}=\max\{\tfrac12(v_r^2+e^{-2r}v_z^2),\ \tfrac12|L|\}.\ \checkmark$$
The script's `defect = max(0.5*grad2, 0.5*|Lv|)` is exactly this.
- **$N$-independence.** $N$ enters $b,c$ only as the additive constant $-\log N$; all derivatives, hence all $E$-components, are $N$-free. $\checkmark$
- **Shape/normal balance.** $S=\operatorname{diag}(1,1+\tfrac12 v_r,1-\tfrac12 v_r)$, $H=3$, $|S-I|^2=\tfrac12 v_r^2$. The radial identity $\operatorname{Ric}(\nu,\nu)=-H'-|S|^2$ with $|S|^2=3+\tfrac12 v_r^2$ gives $E_{rr}=3+\operatorname{Ric}(\nu,\nu)=-\tfrac12 v_r^2=-|S-I|^2$. $\checkmark$
- **Estimate and numerics.** With $v=\chi(\tfrac{r-r_0}{K})v_0(z)$, $v_r=\tfrac1K\chi'v_0$, $v_{rr}=\tfrac1{K^2}\chi''v_0$: the leading term is $\tfrac12|L|\approx\tfrac{3}{2K}|\chi'|\,|v_0|$, giving $\|E\|_{\rm op}\le C(K^{-1}+K^{-2}+e^{-2r_0})$. $\checkmark$ For the quintic $\chi$, $\chi'=-30s^2(1-s)^2$, $\max|\chi'|=15/8$, so $K\sup\to\tfrac32\cdot\tfrac{15}{8}=2.8125$; the reported $K\!\cdot\!\sup\to2.813$ matches. I also reproduced the $r_0$-dependent left-edge values by hand: at $s=0$, $\|E\|_{\rm op}=\tfrac12 e^{-2r_0}\max_z|\!\sin z|$; $r_0=6\Rightarrow 3.07\times10^{-6}$, $r_0=2\Rightarrow 9.16\times10^{-3}$, matching the JSON. $\checkmark$

The symbolic residual `all_zero: true` is therefore corroborated by an independent derivation, not just by the same substitution.

## (iii) General adiabatic tail — confirmed, with two testable checks

For $g=dr^2+e^{2a(r)}q_s$, $s=(r-r_0)/K$, $Q=q_s^{-1}\dot q_s$:

- $S=a'I+\tfrac1{2K}Q$, $H=3a'+\tfrac1{2K}\operatorname{tr}Q$. $\checkmark$
- $E_{rr}=3-3a''-3(a')^2-\tfrac{a'}{K}\operatorname{tr}Q-\tfrac1{2K^2}\partial_s\operatorname{tr}Q-\tfrac1{4K^2}\operatorname{tr}(Q^2)$: re-derived from $E_{rr}=3-H'-|S|^2$ with $H'=3a''+\tfrac1{2K^2}\partial_s\operatorname{tr}Q$ and $|S|^2=3a'^2+\tfrac{a'}{K}\operatorname{tr}Q+\tfrac1{4K^2}\operatorname{tr}(Q^2)$. $\checkmark$
- $E_{r\cdot}=\tfrac1{2K}(\operatorname{div}_{q_s}Q-d\operatorname{tr}Q)$: this is the contracted Codazzi/momentum equation with $S=a'I+\tfrac1{2K}Q$ ($\operatorname{div}(a'I)=0$, $dH=\tfrac1{2K}d\operatorname{tr}Q$). Sign convention immaterial for the norm; the extra $e^{-a}$ factor when measuring the covector in $g$ is correct. $\checkmark$
- $E_T$: I verified the full tensor on **two independent inputs** that exercise all term types:
  - Traceless test = the explicit tail ($a'=1$, $Q=\operatorname{diag}(0,v_s,-v_s)$, $\operatorname{tr}Q=0$). The formula returns $E_{zz}=-\tfrac12 e^{-2r}v_z^2$, $E_{xx}=-\tfrac12 L$, $E_{yy}=+\tfrac12 L$, matching Section 2 exactly. This uses $\operatorname{Ric}(q_s)=\operatorname{diag}(-\tfrac12 v_z^2,-\tfrac12 v_{zz},+\tfrac12 v_{zz})$ for the flat-coordinate $T^3$ metric, which I computed separately.
  - Pure-trace test = conformal path $q_s=\psi(s)^2q_0$, $Q=2\tfrac{\psi'}{\psi}I$. Then $g$ collapses to the single warped product $dr^2+e^{2\tilde a}q_0$, $\tilde a=a+\log\psi$, whose tangential $E_T=e^{-2\tilde a}\operatorname{Ric}(q_0)^\sharp+(3-\tilde a''-3\tilde a'^2)I$. Expanding $\tilde a',\tilde a''$ and comparing coefficient-by-coefficient reproduces the note's $\operatorname{tr}Q$- and $(\operatorname{tr}Q)Q$-terms exactly.

  Both tests pass, so the $E_T$ formula is correct including the trace-dependent terms not exercised by the explicit tail.
- **Estimate.** With $a'=1-\varepsilon\eta$: $3(1-a'^2)=O(\varepsilon)$, $a''=O(\varepsilon/K)$, the $\tfrac1K Q$-terms $=O(1/K)$, the $\tfrac1{K^2}$-terms $=O(1/K^2)$, and $e^{-2a}\operatorname{Ric}(q_s)=O(e^{-2a_0})$ using $a\ge a_0$ (which holds since $a'\ge1-\varepsilon>0$). Hence $\|\operatorname{Ric}_g+3g\|_{\rm op,\infty}\le C(\varepsilon+K^{-1}+K^{-2}+e^{-2a_0})$. $\checkmark$

**Refinement A (the $\operatorname{tr}Q=0$ remark).** The note says a volume-form-preserving path improves the "$K^{-1}$" term to "$K^{-2}$." That is correct *only for the normal component* $E_{rr}$, whose sole $O(1/K)$ piece is $\tfrac{a'}{K}\operatorname{tr}Q$. The **total** operator norm keeps an $O(1/K)$ contribution from the tangential block $-\tfrac{3a'}{2K}Q$, which does not vanish when $\operatorname{tr}Q=0$. The explicit tail is precisely a $\operatorname{tr}Q=0$ path and has $\|E\|_{\rm op}\sim 2.8125/K\neq o(1/K)$, confirming the leading $K^{-1}$ is genuine and tangential in origin. The phrasing "normal path term" is defensible but should be read as I state, not as an improvement of the overall bound.

**Refinement B (path regularity actually needed).** The stated hypotheses ("$q_s$, its inverse, its first two $s$-derivatives, and spatial curvature and first spatial derivatives uniformly bounded") should explicitly include: (a) a uniform positive lower ellipticity bound on $q_s$ (needed to form $q_s^{-1}\dot q_s$ and to convert $q_s$-norms of $E_T$, $Q$, $\operatorname{div}_qQ$ into $g$-norms with controlled constants), and (b) one spatial derivative of $\dot q_s$, since $\operatorname{div}_{q_s}Q=\operatorname{div}_{q_s}(q_s^{-1}\dot q_s)$ enters $E_{r\cdot}$ and requires a mixed $s$-and-space derivative of $q_s$. With these included, $C$ depends only on the $C^1_{\rm space}\!\cap C^2_s$ norms and the ellipticity floor of $q_s$; the estimate stands.

## (iv) Exact core decomposition — confirmed and mutually consistent

With $h_r=e^{2a}q_r$, $S=a'I+P$, $\operatorname{tr}_{q_r}P=0$, $q_r'=2q_rP$:

- Normal: $E_{rr}=0$ gives $a''=1-(a')^2-\tfrac13|P|^2$. $\checkmark$
- Traceless tangential: taking the trace-free part of $E_T=0$ (with $Q=2P$, $\operatorname{tr}Q=0$) gives $P'+3a'P=e^{-2a}\operatorname{Ric}(q_r)^\circ$. $\checkmark$
- Hamiltonian: I checked internal consistency by equating $a''$ from the normal equation with $a''$ from the trace part of $E_T=0$ (the latter gives $a''=3-3a'^2+\tfrac13 e^{-2a}R(q)$). Equating yields exactly $e^{-2a}R(q_r)+6(1-a'^2)+|P|^2=0$. $\checkmark$ This is a nontrivial confirmation: the Hamiltonian constraint is not an extra postulate but the compatibility of the two second-order equations.
- Momentum: $\operatorname{div}_{q_r}P=0$ from $E_{r\cdot}=0$. $\checkmark$
- Reflection center: $S=0\Rightarrow a'(0)=0,\ P(0)=0$, and the Hamiltonian then forces $R(q_0)=-6e^{2a(0)}$. $\checkmark$

The note's structural reading is correct: the traceless equation carries damping $3a'P$ and an $e^{-2a}$-suppressed source, so anisotropy is naturally erased under expansion — but this is an evolution in $r$ whose tangential part is elliptic with growing branches, so global continuation from center data is not established by these equations. The statement that a complete $\lambda<0$, $Y<0$ Poincaré–Einstein $\mathbb R\times T^3$ reflection core "would suffice" but is neither supplied nor excluded by the cited Witten–Yau / Cai–Galloway results is accurate: those results exclude disconnected conformal infinity of nonnegative Yamabe type (the flat class included) but say nothing about the $Y<0$ class, and Fuchsian warped products need a $\lambda<0$ Einstein cross-section, unavailable on $T^3$.

## (v) The three-equation warning — correct

Solving $(E_{tt}+E_{zz},E_x,E_y)=0$ leaves $E_{tt}-E_{zz}$ and $E_{tz}$ undetermined; the reduced system is elliptic (determinant $2(\tau^2+\xi^2)^3$) but omits two components that play the role of Hamiltonian/momentum constraints. A value problem on the finite cylinder that drives the three chosen components to zero can leave the other two large, exactly as noted. The correct route is either full Einstein–DeTurck with subsequent removal of the DeTurck field, or an argument propagating the remaining components from compatible data at the faces. This warning is well-founded and is the single most important guard on the next computation.

## What the tail genuinely establishes for the graph route

1. **A rigorous attachment lemma.** Given any core reaching a large, almost-umbilic expanding slice with the interface data of §4 ($S_j\to I$, $e^{-2a_j}\|\operatorname{Ric}(q_j)\|\to0$), and given a controlled path from $q_j$ to a flat cusp metric, the adiabatic tail extends it to an exact flat-cusp germ with $\|\operatorname{Ric}_g+3g\|_{\rm op,\infty}\to0$, uniformly in the lattice parameter $N$. The estimates and the two mechanism formulas are correct. This removes order-one orbit-anisotropy and torus-flattening as obstructions in the outgoing region — a real advance over the withdrawn finite-cylinder $T^2$ route.

2. **It does not construct the core or the interface.** The lemma is an extension result; it presupposes the interface data. The exact core system of §4 is an unsolved Cauchy-type problem from center data, and the source search found no theorem supplying or excluding the required $\mathbb R\times T^3$ reflection core.

3. **The family is approximately, not exactly, Einstein.** Every metric produced has $\|\operatorname{Ric}+3g\|_{\rm op}\le\eta\to0$, i.e. $(-3-\eta)g\le\operatorname{Ric}\le(-3+\eta)g$ — genuine two-sided Ricci pinching around $-3$. It is not a metric with $\operatorname{Ric}=\lambda g$. For the Yau-26 statement this is the right target on the refuting side *only if* the metric lives on a **closed** manifold that carries no Einstein metric: then it would exhibit the pinching hypothesis without an Einstein conclusion. Two things this program still requires and which the present material does not supply: (a) closing the graph manifold into a smooth closed 4-manifold (a cusp germ is a complete non-compact end and must instead be capped or glued to a mirror core), and (b) a closed topology in dimension four known to admit no Einstein metric to attach the construction to. Section 6 states the surrounding coverage correctly: even full success settles only the $\lambda<0$ normalization in dimension four; the $\lambda>0$ side and the higher-dimensional quantifiers remain untouched, and the product construction is a family extension, not $P_4^+\Rightarrow P_n^+$.

## Net

No wrong sign, coefficient, or norm factor was found in the Step-73 formulas; I confirmed each by independent derivation and by two structurally distinct test inputs for the general $E_T$. The three refinements are: the $\operatorname{tr}Q=0$ improvement is confined to the normal component (total bound stays $O(K^{-1})$, as the explicit example proves); the adiabatic hypotheses should list a uniform ellipticity floor for $q_s$ and one mixed space-derivative of $\dot q_s$; and the produced objects are Ricci-pinched near $-3$, whose use for the original proposition depends on an as-yet-unbuilt closed no-Einstein 4-manifold. The unresolved scientific object remains the $z$-inhomogeneous core/interface: a solution or controlled near-solution of the §4 system carrying a totally geodesic $R(q_0)=-6e^{2a(0)}$ center out to a large almost-umbilic slice with $\|\operatorname{Ric}+3g\|_{\rm op}\to0$, together with the full five-component constraint propagation flagged in §5.