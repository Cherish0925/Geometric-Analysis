# TTCS Independent Branch Record

```json
{
  "step_id": 78,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A03/workspace/scripts/step78_bianchi_vii0_verify.py",
    "Sessions/S0910A03/workspace/data/step78_bianchi_vii0_symbolic.json",
    "Sessions/S0910A03/workspace/notes/step75_reflection_core_flux_and_center_theorem.md",
    "Sessions/S0910A03/workspace/notes/step77_pe_scattering_correction.md"
  ]
}
```

## Task

Independently verify the rotating-eigenframe Bianchi VII_0 benchmark for the negative graph-connector route. Read the Step 78 symbolic script/output and the inherited Step 75/77 notes. For g=dr^2+a(r)^2 dz^2+b(r)^2 omega_1^2+c(r)^2 omega_2^2 with omega_1=cos(kz)dx+sin(kz)dy, omega_2=-sin(kz)dx+cos(kz)dy, d=log(b/c), u=a'/a, H=a'/a+b'/b+c'/c, and K=2k^2 a^{-2}sinh^2 d, check from first principles: intrinsic Ricci/scalar formulas; exact Ric=-3g ODEs u'+Hu=3-K, d''+Hd'=2K coth d, (log K)'=-2u+2 coth(d)d'; reflected center implications; and the proposed invariant-region proof u<0, d'>0, K>=6 for r>0. Then derive the sharpest elementary small-defect persistence statement under ||Ric+3g||_op<=delta, including whether delta<3/5 is correct, what interval it covers, and what role H plays. Identify any omitted momentum/off-diagonal equation or global-periodicity issue. Explain precisely what this rules out and what it leaves open for a finite vanishing-defect connector.

## Output

# Verification memo: rotating-eigenframe Bianchi VII₀ benchmark (Step 78) and the reflected-center invariant region

I recomputed everything from first principles with an orthonormal moving frame, independent of the SymPy coordinate route, and I reconstructed the small-defect persistence argument in full. The symbolic identities in `step78_bianchi_vii0_verify.py` are correct, and the invariant-region argument is sound. Below I give the independent derivation, the exact constants, the one structural equation the record does not display, the cross-check against the Step 75/77 center results, and a precise statement of what is excluded versus open.

## 1. Independent Ricci computation confirms all four formulas

Take the coframe $e^0=dr,\ e^1=a\,dz,\ e^2=b\,\omega_1,\ e^3=c\,\omega_2$. Using $d\omega_1=k\,dz\wedge\omega_2$, $d\omega_2=-k\,dz\wedge\omega_1$ (which I verified from the definitions of $\omega_1,\omega_2$), the exterior derivatives are
$$de^1=u\,e^0\wedge e^1,\quad de^2=v\,e^0\wedge e^2+P\,e^1\wedge e^3,\quad de^3=w\,e^0\wedge e^3-Q\,e^1\wedge e^2,$$
with $u=a'/a,\ v=b'/b,\ w=c'/c$, $P=\tfrac{bk}{ac}$, $Q=\tfrac{ck}{ab}$. Solving Cartan's first equation gives the connection
$$\omega_{0i}=-(u,v,w)_i e^i,\quad \omega_{12}=A e^3,\ \omega_{13}=A e^2,\ \omega_{23}=B e^1,\quad A=\tfrac{Q-P}{2},\ B=-\tfrac{P+Q}{2}.$$
Computing the curvature 2-forms yields the diagonal frame-Ricci
$$
\begin{aligned}
R_{00}&=-(u'{+}u^2)-(v'{+}v^2)-(w'{+}w^2)=-(a''/a+b''/b+c''/c),\\
R_{11}&=-(u'{+}u^2)-u(v{+}w)-K,\\
R_{22}&=-(v'{+}v^2)-v(u{+}w)+L,\\
R_{33}&=-(w'{+}w^2)-w(u{+}v)-L,
\end{aligned}
$$
with $A(P-Q)=-\tfrac{(P-Q)^2}{2}=-K$ and $-A(P+Q)=\tfrac{P^2-Q^2}{2}=L$. Since $P-Q=\tfrac{k}{a}\tfrac{b^2-c^2}{bc}$ one gets exactly
$$K=\frac{k^2(b^2-c^2)^2}{2a^2b^2c^2}=2k^2a^{-2}\sinh^2 d,\qquad L=\frac{k^2(b^4-c^4)}{2a^2b^2c^2}=k^2a^{-2}\sinh(2d)=K\coth d,$$
$d=\log(b/c)$. These match the script's `Rrr, Rz_unit, Rb_unit, Rc_unit` and its `K_algebraic`, `L_algebraic`, and the identity $L=K\coth d$. The intrinsic 3-metric Ricci obtained by suppressing all radial derivatives ($-K,\,+L,\,-L$ in the $z,\omega_1,\omega_2$ directions) I also reproduced by a direct 3-dimensional frame computation on the slice; the intrinsic scalar is $-K$. All confirmed.

**Off-diagonal / momentum question.** I evaluated every mixed frame component. In this rotating eigenframe the curvature 2-forms $\Omega_{0i}$ contain only $e^0\wedge e^i$ and one $e^j\wedge e^k$ term, and the contractions give $R_{0i}=0$ and $R_{ij}=0$ ($i\ne j$) **identically for all $a,b,c$** — not merely at $z=0$. The rotating frame simultaneously diagonalizes the metric and the Ricci tensor, so there is no separate momentum equation to satisfy: the diagonal system is self-contained. This is exactly why the SymPy off-diagonal entries vanish at $z=0$ (where $\omega_1=dx,\omega_2=dy$ align the coordinate and invariant frames), and the homogeneity that makes normalized diagonal entries $z$-independent justifies the $z=0$ evaluation. No equation is omitted on this account.

## 2. Exact Einstein ODEs — confirmed, plus the first integral not written down

Setting each diagonal frame-Ricci to $-3$ and using $u'+u^2+u(v+w)=u'+uH$ gives directly
$$u'+Hu=3-K,\qquad v'+Hv=3+L,\qquad w'+Hw=3-L.$$
Subtracting the last two and using $d'=v-w$, $d''=v'-w'$, $L=K\coth d$ gives $d''+Hd'=2K\coth d$. The equation $(\log K)'=-2u+2\coth(d)\,d'$ is a purely kinematic identity from $K=2k^2a^{-2}\sinh^2d$ and holds independently of the Einstein condition. All three quoted ODEs are correct.

One equation belongs in the record and is not displayed: the $R_{00}=-3$ relation is the **Hamiltonian first integral**
$$H^2-(u^2+v^2+w^2)=6-K,\qquad H=u+v+w,$$
together with its evolution $H'=9-H^2-K$. Because the momentum components vanish identically, this is the only constraint present, and it is preserved by the diagonal evolution. It is what pins the center data (Section 3) and it should sit alongside the three ODEs in `resulting_exact_odes`; the sign bootstrap does not use it, but the geometry does.

## 3. Reflected center: forced value $K(0)=6$ and forced anisotropy

At a totally geodesic center ($u=v=w=0$, hence $H=0$, $d'=0$) the first integral forces $K(0)=6$. Equivalently the intrinsic scalar $-K=-6$, matching the Step 77 center condition $R(q_0)=-6$. Since $K(0)=6$ needs $\sinh^2d(0)=3a(0)^2/k^2>0$, the center **cannot** be isotropic in the two orbit directions: $b(0)\ne c(0)$ is forced (and $k\ne0$ is required for a center at all).

The center jet is $S'(0)=\operatorname{diag}(u',v',w')(0)=\operatorname{diag}(-3,\,3+L(0),\,3-L(0))$, trace $3$ (i.e. $R(q_0)+9=3$). The $z$-direction gives $u'(0)=-3$, and $L(0)=6\coth d(0)$ has $|L(0)|>6$, so $\lambda_{\min}(S'(0))\le -3$ with the extra contraction living in an orbit direction. This is the same order-one center contraction as Step 75 Theorem 3.1, now realized inside a genuinely 3-dimensional VII₀ slice rather than the flat-$T^2$-orbit class of Step 75. Note the two symmetry classes differ: Step 75/77 used flat $T^2$ orbits; the Step 78 slice is a non-flat left-invariant VII₀ metric on $T^3$. The rotating eigenframe is therefore a genuinely new ansatz, not a special case of the earlier ones.

## 4. The invariant-region argument is rigorous

Take $d(0)>0$ (relabel $b\leftrightarrow c$ otherwise; $d(0)=0$ is impossible at a center). On any interval where $u<0$, $d>0$, $d'>0$, $K\ge6$, the three ODEs close as a bootstrap through positive integrating factors $\mu=e^{\int_0^r H}$:

- $u$: $(\mu u)'=\mu(3-K)\le-3\mu<0$ with $\mu u|_0=0\Rightarrow u<0$.
- $d'$: $(\mu d')'=\mu\,2K\coth d>0$ with $\mu d'|_0=0\Rightarrow d'>0$ (and then $d>0$).
- $K$: $K'=K(-2u+2\coth d\,d')>0\Rightarrow K\ge K(0)=6$.

The initial pushes ($u'(0)=-3<0$, $d''(0)=12\coth d(0)>0$, $K'$ positive for small $r>0$) seed the strict interior, and the three bounds thereafter reinforce one another. The region is invariant on the entire forward smooth-existence interval $r\in(0,R_{\max})$. Geometrically: $K$ (the anisotropy source) never decreases below $6$, $|d|=|\log(b/c)|$ grows monotonically, and $a'/a<0$ so the $z$-circle contracts, with $K=2k^2a^{-2}\sinh^2d\to\infty$ as $a\to0$ — an $r$-finite pinch, not a smooth expanding end.

**Role of $H$.** $H$ enters only as the coefficient in two first-order linear equations, absorbed into the positive factor $\mu$; its sign and size do not affect the signs of $u$ and $d'$. The argument needs neither $H'=9-H^2-K$ nor any bound on $H$. (The bound $0\le H<\sqrt3$ that follows from $H'\le3-H^2$ under $K\ge6$ is real but not used.) This is precisely why the argument is elementary and clean.

## 5. Small-defect persistence: $\delta<3/5$ is correct, and it covers the whole existence interval

With $E=\operatorname{Ric}+3g$, $\|E\|_{\rm op}\le\delta$, the perturbed equations are $u'+Hu=3-K-E_z$ and $d''+Hd'=2K\coth d-(E_{\omega_1}-E_{\omega_2})$, $|E_z|\le\delta$, $|E_{\omega_1}-E_{\omega_2}|\le2\delta$; the $(\log K)'$ identity is unchanged (kinematic). The first integral becomes $H^2-(u^2+v^2+w^2)=6-K+E_{00}-\operatorname{tr}_T E$, so at the center
$$K(0)=6-e,\qquad e=\operatorname{tr}_T E(0)-E_{00}(0),\quad |e|\le4\delta\ \Rightarrow\ K(0)\ge6-4\delta.$$
The binding requirement is keeping the $u$-source $3-K-E_z$ negative, i.e. $K>3+\delta$ (worst case $E_z=-\delta$). Since $u<0$ keeps $K$ increasing, the minimum of $K$ is $K(0)\ge6-4\delta$, so it suffices that
$$6-4\delta>3+\delta\ \Longleftrightarrow\ \boxed{\delta<3/5.}$$
Then the same integrating-factor bootstrap gives, for **all** $r>0$ on the smooth-existence interval, $u<0$, $d>0$, $d'>0$, and $K\ge6-4\delta>3+\delta$. The $d'$-condition needs only $K\coth d>\delta$, guaranteed by $K\ge6-4\delta$ and $\coth d>1$ whenever $\delta<6/5$; it is not binding. So $3/5$ is set entirely by the $z$-direction/anisotropy-source equation.

Two consistency notes. The threshold uses $K(0)\ge6-4\delta$ (worst case $e=4\delta$), whereas the center jet obeys the sharper $u'(0)=3-K(0)-E_z(0)=-3+E_{22}+E_{33}-E_{00}\le-3+3\delta$ — the $E_{11}$ terms cancel — which reproduces Step 75 eq. (3.12) $\lambda_{\min}(S'(0))\le-3+3\delta$ exactly. The $4\delta$ and $3\delta$ live in different places and both are correct. The constant $3/5$ is the sharp value for this uniform elementary argument; it combines the worst sign of $E_{11}$ at the center (small $K(0)$) with the worst sign of $E_z$ later, so a pointwise-correlated analysis could conceivably relax it, but $3/5$ is the natural threshold to state.

## 6. Global periodicity

For $z$-period $2\pi$ the metric coefficients ($b^2\cos^2kz+c^2\sin^2kz$, etc.) are single-valued iff $k\in\mathbb Z$; the $2\pi k$ frame rotation is then the identity on the $x,y$ lattice, so the metric descends to $[0,R]\times T^3$ with a non-flat left-invariant VII₀ fiber. This is what the script flags, and it is right. $k\ne0$ is additionally required for the twist, hence for a center at all ($k=0$ gives $K\equiv0$, flat orbits, no center theorem). No periodicity error is present.

## 7. What this rules out and what remains open

**Excluded.** For $\delta<3/5$, any rotating-eigenframe Bianchi VII₀ metric on $[0,R]\times T^3$ with a reflection center and $\|\operatorname{Ric}+3g\|_{\rm op}\le\delta$ has, on the whole forward smooth interval, monotonically growing anisotropy $|d|$ and $K\ge6-4\delta$ with $a'/a<0$. It cannot flatten toward the small-$|S-I|$, small scaled intrinsic curvature slice that the Step 73 adiabatic tail needs, and the $z$-circle pinches ($K\to\infty$). This makes the exact ($\delta=0$) obstruction robust in a full neighborhood and removes the reflected-center rotating-eigenframe VII₀ ansatz as a finite vanishing-defect connector for the route named in the title, quantitatively for $\delta<3/5$.

**Open.**
1. The ansatz is diagonal in the rotating eigenframe. A general orbit metric $G(r)$ with $r$-dependent eigenframe rotation, off-diagonal evolution, or the twist/Toda structures of Step 76/77 is not covered by this bootstrap.
2. Connectors with no reflection center (asymmetric, or $S(0)\ne0$): the entire argument seeds from $K(0)=6-e$; without a center $K(0)$ is not pinned near $6$ and the invariant region need not start.
3. $\delta\ge3/5$: the elementary argument is silent; whether the same geometry still obstructs is not decided here.
4. The precise fate of the exact/near-exact solution — finite-$r$ curvature singularity versus incompleteness — is not analyzed; the monotone growth of $K$ and $|d|$ indicates no PE end forms, but a completeness statement would need more than the sign bootstrap.
5. Higher dimensions, other Bianchi types, and the positive branch of Yau 26 are entirely outside this benchmark.
6. The Step 75 §6 bulk-redistribution mechanism for a forced core is only excluded here inside this class for $\delta<3/5$; for larger defect or other classes it is untouched.

Nothing in the script or the derivation needs correction; the two items worth adding to the record are the Hamiltonian first integral $H^2-(u^2+v^2+w^2)=6-K$ (with its defect form $+E_{00}-\operatorname{tr}_TE$) that pins $K(0)$, and an explicit statement that the frame-off-diagonal Ricci vanishes identically so no momentum equation is dropped.