# TTCS Independent Branch Record

```json
{
  "step_id": 82,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/notes/step81_collapse_and_contraction.md",
    "Sessions/S0910A03/workspace/notes/step79_ot_reduction_and_mechanism.md",
    "Sessions/S0910A03/workspace/notes/step80_joint_base_response_and_inner_layer.md",
    "Sessions/S0910A03/workspace/data/step82_geometric_balance.json",
    "Sessions/S0910A03/workspace/data/step82_turning_covariance_model.json"
  ]
}
```

## Task

Develop the strongest mathematically plausible next step from the slice balances for the finite small-defect graph connector. Focus on the actual reversal problem: starting at a reflected scalar-minus-six center with I(0)=J(0)=0 and I'(0)=-3V, J'(0)=6V, can the coupled OT Einstein or small-defect equations dynamically create the covariance/orbit-expansion term needed for I to return to zero before singularity? Seek either (a) a coercive evolution identity controlling the turning expression 2Cov(u,v)+<v^2>/2-<|B0|^2> using the orbit H^2 energy, Codazzi/base constraints, and J' balance, or (b) a constraint-compatible perturbative center family whose exact early radial jets make the expression grow toward 3. Work in physical measures and retain all Einstein components. Do not return to constant-exit maximum principles or Noether current alone. Provide explicit equations/calculations and a decisive low-cost computation or theorem target, while clearly separating a mechanism from an established connector.

## Output

## Reframing the reversal as a planar system closed by z‑fluctuations

Work in physical Gaussian radial gauge with the orthogonally transitive metric

$$
g=dr^2+e^{2a(r,z)}dz^2+e^{\sigma(r,z)}M_{ab}(r,z)\,d\xi^a d\xi^b,\qquad \det M=1,\ \ U=[M]\in\mathbb H^2 .
$$

Let $s$ be arclength along $z$ ($ds=e^a\,dz$), $\rho=e^{\sigma}$, so the slice volume measure is $\rho\,ds=e^{a+\sigma}\,dz$. The shape operator splits as $u=a_r$ (the $z$ direction), $v=\sigma_r$ (orbit trace), $B_0=\tfrac12 M^{-1}M_r$ (orbit trace‑free), with $H=u+v$ and $|S|^2=u^2+\tfrac12v^2+|B_0|^2$.

The exact Einstein system ($E=0$) is
$$
u'+Hu=R^z{}_z(q)+3,\quad v'+Hv=\tau+6,\quad B_0'+HB_0=R^0_{\rm orb},\quad H'=3-|S|^2,
$$
with the pointwise Hamiltonian identity $R(q)=-6+H^2-|S|^2$ and the intrinsic slice curvatures, written geometrically in $s$,
$$
R^z{}_z(q)=-\sigma_{ss}-\tfrac12\sigma_s^2-e,\qquad
\tau:=\operatorname{tr}_{\rm orb}R(q)=-\sigma_{ss}-\sigma_s^2,\qquad
e:=\operatorname{tr}(\mathcal A^2)=\tfrac12|U_s|^2_{\mathbb H^2},
$$
$\mathcal A=\tfrac12M^{-1}M_s$. Since $\tau=-(e^{\sigma}\sigma_s)_s/e^{\sigma}$ is a weighted total derivative, $\int\tau\,\rho\,ds=0$.

Set $I=\int u\,\rho\,ds$, $J=\int v\,\rho\,ds$, $V=\int\rho\,ds$, and $x=I/V,\ y=J/V$. Because $2uv+\tfrac12v^2-|B_0|^2=H^2-|S|^2$ and $\int\tau\,\rho\,ds=0$,
$$
I'=-3V+\int\!\big(H^2-|S|^2\big)\rho\,ds,\qquad J'=6V .
$$
Writing the second moments through $x=\langle u\rangle,\ y=\langle v\rangle$, $\mathrm{Cov}=\mathrm{Cov}_\rho(u,v)$, $\mathrm{Var}=\mathrm{Var}_\rho(v)$, the system **closes exactly into a planar flow driven by a single moment functional**:
$$
\boxed{\;x'=\widetilde T-3+xy+\tfrac12y^2-x^2,\qquad y'=6-xy-y^2\;}
$$
$$
\widetilde T:=2\,\mathrm{Cov}_\rho(u,v)+\tfrac12\mathrm{Var}_\rho(v)-\langle|B_0|^2\rangle_\rho .
$$
At the center $x=y=0$, $\widetilde T=0$, giving $x'(0)=-3$, $y'(0)=6$, matching $I'(0)=-3V,\ J'(0)=6V$. The turning condition ($x$ back to $0$ with $x'\ge0$) is $\widetilde T\ge 3$ at that instant, i.e. exactly the step‑82 term evaluated at $\langle u\rangle=0$.

**The deterministic core collapses.** Set $\widetilde T\equiv 0$ (any $z$‑independent, VII$_0$‑type slice): $x'=xy+\tfrac12y^2-x^2-3$, $y'=6-xy-y^2$. Starting at the origin, $x$ runs to $-\infty$ in finite $r$; even letting $y$ reach its $x=0$ nullcline $y=\sqrt6$ gives $x'=x(y-x)<0$ for $x<0,y>0$. So reversal is **entirely a $z$‑fluctuation phenomenon**: it lives in $\widetilde T$ and cannot be produced by any homogeneous state. This is a clean restatement of why the VII$_0$ collapse is unavoidable in the homogeneous class, and it isolates the whole problem into the production law for $\widetilde T$.

## The exact constraint‑reduced germ makes $\widetilde T$ start with the opposing sign

For an exact reflected center the Hamiltonian constraint holds pointwise, $R(q_0)=-6$, i.e.
$$
-2\sigma_{ss}-\tfrac32\sigma_s^2-e=-6\ \Longrightarrow\ e=6-2\sigma_{ss}-\tfrac32\sigma_s^2 .
$$
Substituting into the first radial jet and defining $\varphi:=\sigma_{ss}+\sigma_s^2=(e^{\sigma})_{ss}/e^{\sigma}$,
$$
\boxed{\,u'(0,z)=-3+\varphi(z),\qquad v'(0,z)=6-\varphi(z)\,},\qquad B_0'(0)=R^0_{\rm orb}=:R^0 .
$$
Since $\int\varphi\,e^{\sigma}\,ds=\int(e^{\sigma})_{ss}\,ds=0$, one recovers the volume‑weighted universals $\langle u'(0)\rangle_\rho=-3$, $\langle v'(0)\rangle_\rho=6$. But the *only* $z$‑structure a scalar‑minus‑six reflected center can carry, the area‑bending field $\varphi$, enters $u$ and $v$ with **opposite signs**. Hence at leading order
$$
\mathrm{Cov}_\rho(u,v)\approx -r^2\,\mathrm{Var}_\rho(\varphi),\quad
\mathrm{Var}_\rho(v)\approx r^2\,\mathrm{Var}_\rho(\varphi),\quad
\langle|B_0|^2\rangle\approx r^2\langle (R^0)^2\rangle,
$$
$$
\boxed{\;\widetilde T(r)=-r^2\Big[\tfrac32\mathrm{Var}_\rho(\varphi)+\langle (R^0)^2\rangle_\rho\Big]+O(r^3)\le 0.\;}
$$
So a modulated exact center **deepens** the collapse at second order; the literal version of option (b) — early jets that push $\widetilde T$ toward $3$ — does not exist. Turning, if it happens, is a strictly *intermediate‑$r$, nonlinear, non‑germ* event in which the sign of $\mathrm{Cov}(u,v)$ reverses after the fields have developed. This is the single most decisive analytic fact for the connector question and it should redirect effort away from germ engineering.

## Why the sign is structurally adverse, and the one mechanism that can flip it

Rewrite the pointwise equations using the Hamiltonian identity:
$$
u'=-Hu-3+H^2-|S|^2-\tau,\qquad v'=-Hv+\tau+6 .
$$
Two independent structural terms bias $\mathrm{Cov}(u,v)$ toward the opposing sign:

1. **The area‑bending scalar $\tau$** appears as $-\tau$ in $u'$ and $+\tau$ in $v'$. Any region where $\tau$ grows sends $v$ up and $u$ down — anti‑correlated production, identical in origin to the germ result.
2. **The $-|S|^2=-(u^2+\tfrac12v^2+|B_0|^2)$ term** in $u'$ means that wherever $v$ is large the $z$ direction is driven down: again $u\downarrow$ where $v\uparrow$.

Positive covariance therefore cannot be borrowed from these; it must be manufactured against them. The only channel is **differential relaxation of the shear energy $e(r,z)$**. Where $e$ is small, $R^z{}_z=-6+H^2-|S|^2-\tau$ is least deep, so $u$ recovers upward, while $\Lambda=-3$ drives $v$ upward through the area equation $\Delta\rho=6e^{2\lambda}\rho$. In those low‑$e$ patches $u$ and $v$ **co‑expand**, producing $\mathrm{Cov}(u,v)>0$. The competition is quantitative: the co‑expanding patches must dominate the $\rho$‑weighted covariance before the high‑$e$ patches (still contracting, still deepening $-|S|^2$) drive a local $|S|^2$ blow‑up. This is a genuine race of two rates, not settled by any algebraic compatibility count.

## A coercive route: Codazzi controls $\mathrm{Var}(v)$ by the very anisotropy that must vanish at the exit

The momentum constraint (Codazzi, exact $E_{rj}=0$) in this adapted frame reduces to
$$
\boxed{\;\partial_s v=\sigma_s\,u-\tfrac12\sigma_s\,v-\operatorname{tr}(\mathcal A B_0)\;}
$$
(the orbit component is vacuous by $T^2$ invariance). This is the coercive tool option (a) needs: the $z$‑variation of the orbit expansion is *sourced only* by the area gradient $\sigma_s$ coupled to $(u-\tfrac12v)$ and by the shear coupling $\operatorname{tr}(\mathcal A B_0)$. A weighted Poincaré inequality on the $z$‑circle then gives
$$
\mathrm{Var}_\rho(v)\ \le\ C_P\,\big\langle(\partial_s v)^2\big\rangle_\rho
= C_P\,\big\langle(\sigma_s u-\tfrac12\sigma_s v-\operatorname{tr}(\mathcal A B_0))^2\big\rangle_\rho ,
$$
with $C_P$ of order $(L/2\pi)^2$, $L$ the slice $z$‑length. Combined with $|\mathrm{Cov}(u,v)|\le\sqrt{\mathrm{Var}(u)\mathrm{Var}(v)}$, this bounds the entire turning functional:
$$
\widetilde T\le 2\sqrt{\mathrm{Var}_\rho(u)\,\mathrm{Var}_\rho(v)}+\tfrac12\mathrm{Var}_\rho(v).
$$
The right side is controlled by the area gradient $\sigma_s$ and the shear pair $(\mathcal A,B_0)$ — precisely the anisotropy fields that must tend to $0$ to match the smooth expanding Step‑73 tail (where $U$ has relaxed, $\sigma_s\to0$, $B_0\to0$). Near both ends of the connector $\widetilde T$ is therefore squeezed: it starts $\le0$ (germ), and it tends to $-\langle|B_0|^2\rangle\le0$ at the exit. Any reversal is confined to a bounded middle band, and its attainable height is set by how large $\mathrm{Var}(v)$ and $\mathrm{Cov}(u,v)$ can be while $|S|^2$ (which contains $\tfrac12v^2$) stays below the $H'=3-|S|^2$ blow‑up rate. This is the exact tension to quantify, and it is the shape of a real theorem.

## Decisive low‑cost computations and theorem targets (mechanism vs. established connector)

**Computation 1 — direct reachability march (cheapest, most informative).** Initialize the coupled OT system (area eq. 4.1, orbit map eq. 4.3, conformal eq. 4.8, constraint 4.10 of the Step‑79 reduction) at $r=0$ with a reflected center: pick $\sigma(0,z)$ and $U(0,z)=(d(z),\psi(z))$ satisfying $R(q_0)=-6$ pointwise via $e=6-2\sigma_{ss}-\tfrac32\sigma_s^2$, all $\partial_r$ data zero. Use one‑dimensional spectral resolution in $z$ (few dozen modes) and a stiff $r$‑march. Record $x(r),y(r),\widetilde T(r),\mathrm{Cov},\mathrm{Var}(v),\langle|B_0|^2\rangle,\ \max_z|S|^2$. The single question: does $x$ return to $0$ (equivalently $\widetilde T$ reaches $3$) before $\max|S|^2$ diverges? Sweep the seed spectrum of $\varphi$ and of the shear phase to search for the co‑expansion window. This resolves reachability, which the 140 algebraically compatible profiles of step 82 cannot. Cost: minutes.

**Computation 2 — moment‑closure surrogate.** Reduce to a low‑dimensional ODE for $(x,y,\mathrm{Var}\,v,\mathrm{Cov},\langle e\rangle)$ by inserting the Codazzi source into $\partial_r\mathrm{Var}(v)$ and $\partial_r\mathrm{Cov}$, modeling the shear‑energy decay $\langle e\rangle$ on the expanding weight from eq. 4.4–4.5. Test whether *any* closure with the correct signs (Codazzi source, $\tau$ anti‑coupling, $-|S|^2$ anti‑coupling) admits $\widetilde T\!\to\!3$. If every sign‑faithful closure keeps $\widetilde T<3$, that is strong evidence of an intrinsic block; if some do, it pinpoints the required $\langle e\rangle$ decay profile to target in Computation 1.

**Theorem target A (block).** Prove a differential inequality of the form
$$
\widetilde T(r)\le F\big(y,\ \mathcal E(r)\big),\qquad \mathcal E:=\big\langle \sigma_s^2+e\big\rangle_\rho,
$$
using Codazzi + Poincaré + the Hamiltonian identity, together with a supersolution/decay statement for $\mathcal E(r)$ driven by the expanding weight (an energy inequality for the weighted $\mathbb H^2$ map on a growing $\rho$). If $F$ stays below $3$ along every trajectory from the reflected center that also reaches $\mathcal E\to0$ at the exit, the graph‑connector route in this ansatz is closed unconditionally. The needed input is a monotone control of $\mathcal E(r)$ under eqs. 4.1/4.4/4.5; this is the honest missing analytic piece.

**Theorem target B (mechanism realized).** Exhibit an explicit intermediate profile with $\mathrm{Cov}(u,v)>0$ and $\mathrm{Var}(v)$ large enough that $\widetilde T\ge3$, *and* verify via Codazzi that it is a constraint‑compatible slice reachable by the $r$‑flow (not merely algebraically admissible). Success here is a mechanism, not a connector: it must still be threaded continuously from $r=0$ to the tail with all Einstein components small, which is exactly what Computation 1 tests.

A clear separation to keep: the planar system, the germ sign, the $\tau$/$-|S|^2$ anti‑coupling, and the Codazzi–Poincaré bound are established identities; the reachability of a $\widetilde T\ge3$ turning and the decay control of $\mathcal E(r)$ are open and are what the two computations and two theorem targets are meant to decide. And even a fully realized $\lambda<0$ graph connector would leave the $\lambda>0$ branch and the all‑dimension quantifiers of the original problem untouched.