# Step 21 Corrections: TTCS, A01, A02 repairs

Appended to `step21_derivative_free_first_exit_and_plateau_regularity.md`.

## 9. Corrections from TTCS verification and peer review

### 9.1 Volume form during the flow (TTCS §1.1)

The bound $|s+4|\le4\delta$ holds only at $t=0$. During the flow, the volume rate is
$$
\partial_t(d\mu)=-a\operatorname{tr}(E)d\mu,
\qquad |\operatorname{tr}(E)|\le CF,\quad F=(1+|\operatorname{Rm}|^2)^{1/2}.
$$
Before the defect Moser estimate is available, the volume-form reaction
$|a\operatorname{tr}(E)|\le CaF$ must be absorbed into the curvature reaction
$\int a^{q-1}F^{q+1}$ (which it is, at exponent $q-1$ instead of $q+1$, hence lower order).
After the defect estimate is obtained, one can tighten to
$|a\operatorname{tr}(E)|\le C|aE|\le C\delta(r^2/t)^{1/3}$. The correct Grönwall
factor is $e^{C_q(\theta+\theta r^2)}$, not merely $e^{CT_0}$.

### 9.2 Exit conditions: separate H₂ and Q (TTCS §4, item 2)

Step 21 Section 4 mixed curvature energy (F3) with defect energy (Step V).
The correct exit framework has four independent conditions plus two
derived outputs:

- **(F1)** Metric comparability  
- **(F2)** Relative Sobolev persistence  
- **(F3a)** Curvature energy: $H_{2,\alpha}(t)\le 2H_{2,\alpha}(0)$ for covering centers  
- **(F3b)** Defect energy: $Q_\alpha(t)\le 2Q_\alpha(0)$ for covering centers  
- **(F4)** [Derived] Weighted curvature: $|\chi^2\operatorname{Rm}|\le C\gamma/t$  
- **(F5)** [Derived] Weighted defect: $|\chi^2E|\le C\delta(r^2/t)^{1/3}$

(F3a) is propagated by the curvature energy inequality from the $H_q$ hierarchy.
(F3b) is propagated by the triangular $Q$ system (Step 20, eq. 4.1), using the
curvature absorption $\int a|\operatorname{Rm}||E|^2\le\beta\int a|\nabla E|^2+\cdots$,
where $\beta=A_0^2\|\operatorname{Rm}\|_2$ is small.

### 9.3 Uniform work scale (TTCS §2.2, A02 #298)

The TTCS verifier correctly warns that if $r_i\to0$, Shi estimates blow up. This does not occur on the critical family:

For fixed topology $M$ (critical Ishida–LeBrun), near-Einstein $|E|\le\delta$ gives:
$$
\int_M|\operatorname{Rm}|^2
\le 8\pi^2(2\chi+3|\tau|)+O(\delta^2\operatorname{Vol})
\le C(M).
$$
$$
\operatorname{Vol}(M,g_i)\to\frac{32\pi^2A}{9}.
$$
Hence $K_0=\operatorname{Vol}^{-1}\int|\operatorname{Rm}|^2\le C(M)$, and
$$
r_*=\left(\frac{\varepsilon_{\rm Li}}{K_0}\right)^{1/4}
\ge\left(\frac{\varepsilon_{\rm Li}}{C(M)}\right)^{1/4}>0,
\qquad\text{uniformly in }i.
$$
Therefore $T_0=\theta r_*^2>0$ and $\gamma=Cr_*^2\sqrt{K_0}$ are all uniform.
The Shi constants depend only on $(n,k,C\gamma/T_0,d)$ where $d\ge\rho/16$ is the
plateau buffer width (determined by $r_*$). All are uniform.

For the standard subclass (Noether bound $\chi/A\le65/6$), the constants
are also uniform across varying topology with bounded $\chi/A$.

### 9.4 Collapse-Sobolev degeneration (A02 #298)

A02 correctly observes that for a collapsed $S^1_\ell\times B^3$ ($\ell\to0$):
$$
A_\ell^2\ge c\ell^{-1/2},\qquad
\|\operatorname{Rm}\|_2\sim\sqrt{\ell},\qquad
\beta=A_\ell^2\|\operatorname{Rm}\|_2=O(1)\text{ (not small)}.
$$

This does NOT defeat the argument because we use $\beta$ on
**maximal-function good balls of the Li radius $r_*$**, not on
arbitrary balls:
$$
\beta=A_0^2(B_{r_*})\cdot\|\operatorname{Rm}\|_{L^2(B_{r_*})}
=Cr_*^2\operatorname{Vol}(B_{r_*})^{-1/2}\cdot(\textstyle\int_{B_{r_*}}|\operatorname{Rm}|^2)^{1/2}
=Cr_*^2\sqrt{K_0}.
$$
The volume cancels. This is volume-independent (Step 19) and equals
$C\sqrt{\varepsilon_{\rm Li}}$, which is small.

The relative Sobolev constant $A_0^2$ on a collapsed ball IS large;
the total $L^2$ curvature IS small; their PRODUCT is fixed and small.
Any argument using one without the other is incorrect (A02's warning).

### 9.5 Spectrum determination needs monopole data (TTCS §3.3)

The modulus $|W^+|=1/(2\sqrt6)$ alone does not determine the spectrum.
For example, $(-1/(4\sqrt3),0,1/(4\sqrt3))$ also has the same
trace-zero norm $1/24$.

The correct chain requires the full joint density from Step 16:
1. At terminal time $T_0$, reapply Ishida–LeBrun monopole inequality
   to $g_i(T_0)$ (valid for any smooth metric on $M$).
2. The positive-part quantity $q^+=\max(\sqrt6|W^+|-|s|,0)$ and the
   eigenline saturation $\mathscr A H=0$ where
   $\mathscr A=W^++(1/6)I\ge0$ provide the additional constraint.
3. Good-center selection uses the **full joint density**
   $\mathcal D_i=\mathcal D_i^{\rm Weyl}+\mathcal D_i^{\rm amp}+\mathcal D_i^{\rm line}$,
   not just the Weyl modulus calibration.
4. On the smooth limit $h_\infty$, the harmonic SD form $H_\infty\ne0$
   and $\mathscr A H_\infty=0$ force the simple eigenvalue $-1/6$,
   hence $\operatorname{Spec}(W^+)=(-1/6,1/12,1/12)$.

This requires the platform volume denominator $\operatorname{Vol}(P_i)\ge c\operatorname{Vol}(M,g_i)$
for the averaging to produce good centers with vanishing density. Since
the metric drift is $O(\delta_i)$ and the cutoff $\chi$ is determined by
the fixed Li radius, this is satisfied.

### 9.6 Nash/semigroup alternative (TTCS generator)

The generator identifies a potentially simpler route: compress the
nested Moser iteration into a single abstract Nash ultracontractivity
estimate on the conformal measure $d\nu=a^{-2}d\mu$ on $\{a>0\}$.
The weighted moments become $H_q=\int\mathcal K^q\,d\nu$ with
$\mathcal K=aF$. A single $L^2\to L^\infty$ Nash bound replaces
infinitely many Moser exponents:
$$
\|\mathcal K(t)\|_\infty\lesssim A^2t^{-1}\|\mathcal K(0)\|_{L^2(\nu_0)}.
$$
This requires verifying: (i) the non-autonomous form $\mathfrak e_t$
is uniformly closed and satisfies the 4D Nash inequality on
$(M\setminus\{\chi=0\},\nu_t)$; (ii) first-order $da$-terms are
sector-bounded; (iii) the curvature potential is a small form
perturbation ($\gamma<1$). The softer defect rate
$|aE|\lesssim\delta(r^2/t)^{1/2}$ (not $t^{-1/3}$) suffices for
metric drift integrability. This is a promising simplification
but not yet established.

### 9.7 A01 Stampacchia correction (#297)

A01's Stampacchia step had a scaling error: under $\tilde g=\ell^{-2}g$,
curvature transforms as $|\operatorname{Rm}(\tilde g)|=\ell^2|\operatorname{Rm}(g)|$,
so $F$ is not invariant. The corrected route uses A03's $q\to3q/2$
weighted-moment Moser iteration, which avoids metric rescaling entirely.
This is consistent with our Step 20 framework.
