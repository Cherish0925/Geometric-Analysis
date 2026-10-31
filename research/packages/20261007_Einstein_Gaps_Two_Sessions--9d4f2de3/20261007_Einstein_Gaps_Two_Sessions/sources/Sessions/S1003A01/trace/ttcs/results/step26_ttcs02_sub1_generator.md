# TTCS Independent Branch Record

```json
{
  "step_id": 26,
  "type": "Generator",
  "task_field": "generator",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step26_action_budget_matching.md",
    "Sessions/S1003A02/workspace/notes/step31_charge_variation_constraint_pinning_nonround_opening.md",
    "Sessions/S1003A02/workspace/notes/step30_Qdoubleprime_beta_pinning_and_anisotropic_collapse.md",
    "Sessions/S1003A02/workspace/scripts/saturation_optimal_control.py"
  ]
}
```

## Task

Develop a mathematically serious next result for the diagonal scalar-normalized Bianchi-IX cell problem from the exact identities in the supplied notes. Focus on the non-round late-opening branch: combine the Hamiltonian constraint residual C, the anisotropy equation (W q')'=W(P_g-P_h-D), the chiral charge variation, and the expanding-block hypotheses to derive either (i) a reusable quantitative lower bound for a transition from a collapsed state to a CH-like state with b_+ below -1, or (ii) a precise counter-mechanism showing why such a bound cannot hold without extra hypotheses. Track all weights, endpoint terms, and drift terms. The result must distinguish exact Einstein trajectories, scalar-normalized competitors with nonzero trace-free Ricci, and raw high-shear paths; do not assume an unproved compactness theorem or invent numerical evidence.

## Output

## Momentum-renormalized late-opening estimate

Write the scalar-normalized action on an interval \(I\) as
\[
\widehat P_I
=\int_I W\left(\frac{\mathcal C^2}{3}+\frac{E^2}{6}+\frac{D^2}{8}\right)dt,
\qquad s\equiv-24,
\]
where
\[
\mathcal C=\operatorname{Ric}^{\circ}_{00},\qquad
D=\operatorname{Ric}_{gg}-\operatorname{Ric}_{hh}.
\]
For the contact-slot anisotropy
\[
q=\log\frac{a_g}{a_h},\qquad J=Wq',
\]
the exact equation is
\[
J'=W(\Pi-D),
\qquad
\Pi:=P_g-P_h
=-8\zeta\sinh q+\frac{8\zeta^2}{\kappa^2}\sinh(2q),
\tag{1}
\]
with
\[
\zeta'=-(y_g+y_h)\zeta.
\]

The useful refinement is to remove the initial momentum \(Wq'\) by accounting for the interval on which that momentum was produced.

### 1. Exact two-stage Green identity

Let
\[
T_-<T_0<T_1,\qquad I_-=[T_-,T_0],\qquad I_+=[T_0,T_1].
\]
On \(I_+\), put
\[
K(t)=\int_t^{T_1}\frac{du}{W(u)},\qquad K_0=K(T_0).
\]
Introduce
\[
J_-=W(T_-)q'(T_-),\qquad
\mathcal R_-=\int_{I_-}W\Pi\,dt,
\qquad
\mathcal R_+=\int_{I_+}W\Pi K\,dt.
\]
Then
\[
\boxed{
\mathcal M:=
q(T_1)-q(T_0)-(J_-+\mathcal R_-)K_0-\mathcal R_+
=
-K_0\int_{I_-}WD\,dt-\int_{I_+}WDK\,dt.
}
\tag{2}
\]

Indeed, integrating (1) on \(I_-\) gives
\[
J(T_0)=J_-+\mathcal R_--\int_{I_-}WD\,dt,
\]
while Fubini on \(I_+\) gives
\[
q(T_1)-q(T_0)
=J(T_0)K_0+\mathcal R_+-\int_{I_+}WDK\,dt.
\]
Substitution yields (2).

Cauchy–Schwarz across the two disjoint intervals now gives
\[
|\mathcal M|^2
\le
\left(\int_{I_-\cup I_+}WD^2dt\right)
\left(
K_0^2\int_{I_-}Wdt+\int_{I_+}WK^2dt
\right).
\]
Consequently,
\[
\boxed{
\widehat P_{I_-\cup I_+}
\ge
\frac{\mathcal M^2}
{8\left(
K_0^2\displaystyle\int_{I_-}Wdt+
\displaystyle\int_{I_+}WK^2dt
\right)}.
}
\tag{3}
\]

Formula (3) is the momentum-renormalized \(D\)-channel estimate. Unlike the one-interval formula, it does not treat \(W(T_0)q'(T_0)\) as free: the part of that momentum created after \(T_-\) is represented by \(D\) on \(I_-\). The remaining data are the earlier flux \(J_-\) and the exact Einstein drift \(\mathcal R_-\).

### 2. Hamiltonian control of the Green weights

Assume on \(I_+\) that
\[
R^{(3)}\ge-\rho,\qquad A^2:=18-\rho>0,
\]
and choose
\[
0<\sigma<m:=\min\{S(T_0),A\}.
\]
Set
\[
W_0=W(T_0),\qquad
L_{\mathcal C}:=\frac{\sigma W_0}{3}(m-\sigma)^2.
\tag{4}
\]

The identity
\[
S'=18-S^2+R^{(3)}+\mathcal C
\]
has the following direct consequence:

* either \(S\ge\sigma\) throughout \(I_+\);
* or
  \[
  \widehat P_{I_+}\ge L_{\mathcal C}.
  \tag{5}
  \]

To see this, suppose \(S\) first reaches \(\sigma\). Up to that point,
\[
W(t)\ge W_0e^{\sigma(t-T_0)},\qquad
\int_{T_0}^{t}\frac{du}{W(u)}\le\frac1{\sigma W_0}.
\]
The first-barrier argument for \(S+\int|\mathcal C|\) gives
\[
m-\sigma\le\int_{T_0}^{t}|\mathcal C|du.
\]
Hence
\[
(m-\sigma)^2
\le
\left(\int W\mathcal C^2dt\right)
\left(\int\frac{dt}{W}\right)
\le
\frac{3\widehat P_{I_+}}{\sigma W_0},
\]
which is (5).

If \(S\ge\sigma\), then for every \(t\in I_+\),
\[
K(t)\le\frac1{\sigma W(t)},\qquad
K_0\le\frac1{\sigma W_0},
\qquad
\int_{I_+}WK^2dt\le\frac1{\sigma^3W_0}.
\tag{6}
\]

Now also assume on \(I_+\) that
\[
B:=y_g+y_h\ge\mu>0,\qquad
|q|\le Q,\qquad
\kappa\ge\kappa_0>0.
\tag{7}
\]
Writing \(\zeta_0=\zeta(T_0)\), equation \(\zeta'=-B\zeta\) yields
\[
\zeta(t)\le\zeta_0e^{-\mu(t-T_0)}.
\]
Using (6) and the explicit formula for \(\Pi\),
\[
|\mathcal R_+|
\le
\frac{8\zeta_0\sinh Q}{\sigma\mu}
+
\frac{4\zeta_0^2\sinh(2Q)}{\sigma\mu\kappa_0^2}
=:\Lambda_+.
\tag{8}
\]

For the production interval define
\[
\mathcal W_-:=\int_{I_-}Wdt,\qquad
\Xi_-:=\int_{I_-}W|\Pi|dt.
\]
Under \(S\ge\sigma\), equations (2), (6), and (8) imply
\[
|\mathcal M|
\ge
\left(
|q(T_1)-q(T_0)|
-\frac{|J_-|+\Xi_-}{\sigma W_0}
-\Lambda_+
\right)_+
=:\Delta_q,
\tag{9}
\]
and
\[
K_0^2\mathcal W_-+\int_{I_+}WK^2dt
\le
\frac{\mathcal W_-}{\sigma^2W_0^2}
+\frac1{\sigma^3W_0}
=:\mathcal H.
\tag{10}
\]

Combining the Hamiltonian and anisotropy channels therefore gives the quantitative estimate
\[
\boxed{
\widehat P_{I_-\cup I_+}
\ge
\min\left\{
\frac{\sigma W_0}{3}(m-\sigma)^2,\,
\frac{\Delta_q^2}{8\mathcal H}
\right\}.
}
\tag{11}
\]

For a CH-like terminal section satisfying
\[
|q(T_1)|\le\varepsilon,\qquad |q(T_0)|\ge Q_*,
\]
one may replace the first term inside (9) by \(Q_*-\varepsilon\):
\[
\Delta_q\ge
\left(
Q_*-\varepsilon
-\frac{|J_-|+\Xi_-}{\sigma W_0}
-\frac{8\zeta_0\sinh Q}{\sigma\mu}
-\frac{4\zeta_0^2\sinh(2Q)}
{\sigma\mu\kappa_0^2}
\right)_+.
\tag{12}
\]

When \(I_-\) is empty, \(J_-=W_0q'(T_0)\) and (11) reduces to
\[
\widehat P_{I_+}
\ge
\min\left\{
\frac{\sigma W_0}{3}(m-\sigma)^2,\,
\frac{\sigma^3W_0}{8}
\left(
|q_1-q_0|-\frac{|q'(T_0)|}{\sigma}-\Lambda_+
\right)_+^2
\right\}.
\tag{13}
\]
Thus the initial anisotropy velocity is an essential endpoint term, not an error that can be discarded.

### 3. Chiral variation and the full bolt-to-opening decomposition

For any interval \(I\), define the upward chiral variation
\[
\mathcal V_\chi(I)
=
\int_I\max\{0,\mathfrak b_+',\mathfrak b_-'\}\,dt.
\]
The chiral identities give
\[
\widehat P_I\ge\mathcal V_\chi(I).
\tag{14}
\]
Since (11) and (14) both draw on the same action on \(I_-\cup I_+\), their valid combination is
\[
\boxed{
\widehat P_{I_-\cup I_+}
\ge
\max\left\{
\mathcal V_\chi(I_-\cup I_+),\,
\min\left(L_{\mathcal C},\frac{\Delta_q^2}{8\mathcal H}\right)
\right\}.
}
\tag{15}
\]

If \(t_b\) is an \(O(-1)\) bolt and \(T_-\) is an earlier collapsed section, the disjoint bolt prefix supplies
\[
\widehat P_{[t_b,T_-]}
\ge
\mathcal V_\chi([t_b,T_-])
\ge
\max\{0,\mathfrak b_+(T_-)-1,\mathfrak b_-(T_-)-7\}.
\tag{16}
\]
Therefore
\[
\boxed{
\widehat P_{[t_b,T_1]}
\ge
\mathcal V_\chi([t_b,T_-])
+
\max\left\{
\mathcal V_\chi([T_-,T_1]),\,
\min\left(L_{\mathcal C},\frac{\Delta_q^2}{8\mathcal H}\right)
\right\}.
}
\tag{17}
\]

This is additive only because the bolt prefix and late-opening region are disjoint.

For a controlled collapsed first jet
\[
x=X\epsilon^3+o(\epsilon^3),\qquad
\chi=\Gamma\epsilon+o(\epsilon),
\]
the limiting charges are
\[
\mathfrak b_+=-2-(\Gamma+4X)^2,\qquad
\mathfrak b_-=2+(\Gamma-4X)^2.
\]
Hence the bolt prefix contributes
\[
\mathcal V_\chi([t_b,T_-])
\ge
\big((\Gamma-4X)^2-5\big)_++o(1).
\tag{18}
\]

If \(T_1\) is an exact CH orbit of radius \(\tau\), then
\[
\mathfrak b_+(T_1)=2-9\sinh^4\tau,
\]
so the late interval also has
\[
\mathcal V_\chi([T_-,T_1])
\ge
\left(
4+(\Gamma+4X)^2-9\sinh^4\tau
\right)_++o(1).
\tag{19}
\]
Combining (17)–(19),
\[
\boxed{
\begin{aligned}
\widehat P_{[t_b,T_1]}
\ge\;&
\big((\Gamma-4X)^2-5\big)_+\\
&+
\max\Bigg\{
\left(4+(\Gamma+4X)^2-9\sinh^4\tau\right)_+,\\
&\hspace{38mm}
\min\left(
\frac{\sigma W_0}{3}(m-\sigma)^2,\,
\frac{\Delta_q^2}{8\mathcal H}
\right)
\Bigg\}
+o(1).
\end{aligned}
}
\tag{20}
\]

The cap \(\mathfrak b_+\le-1\) forces an exact CH endpoint to satisfy
\[
\tau\ge \operatorname{arsinh}(3^{-1/4}),
\]
but it does not itself make (19) positive when \(\tau\) is large. In that regime the quantitative content comes from the Hamiltonian/\(D\) term in (20).

## 4. Why the endpoint momentum and drift cannot be omitted

The exact one-stage identity is
\[
q_1-q_0-J_0K_0-\int_{I_+}W\Pi K\,dt
=
-\int_{I_+}WDK\,dt.
\tag{21}
\]
Thus the homogeneous anisotropy momentum \(J_0=W_0q'(T_0)\) and the Einstein drift \(\Pi\) are genuine zero-\(D\)-cost mechanisms. An estimate depending only on \(|q_1-q_0|\), the expanding constants, and the cap \(\mathfrak b_+\le-1\) cannot suppress them.

There is also a local exact-Einstein realization of this mechanism. At a fixed principal orbit let
\[
B=y_g+y_h=b>0,\qquad q'=d,
\]
and set
\[
y_g=\frac{b+d}{2},\qquad
y_h=\frac{b-d}{2},
\]
\[
y_f=
\frac{6+\tfrac12R^{(3)}-\tfrac14(b^2-d^2)}{b}.
\tag{22}
\]
Then
\[
y_fy_g+y_gy_h+y_hy_f
=6+\frac12R^{(3)},
\]
so \(\mathcal C=0\) at that section. For \(|d|\) large,
\[
S=y_f+b\sim\frac{d^2}{4b}>0,
\]
while \(B=b\) remains fixed. The Einstein evolution equations with these initial data give a local solution with
\[
\mathcal C=D=E=0,\qquad \widehat P=0.
\]

Moreover, if
\[
\kappa=\frac{a_f}{a_ga_h}>b,
\]
then the chiral coefficient has the large-\(|d|\) behavior
\[
\mathfrak b_+
=
\frac{a_f^2}{16b^2}
\left(\frac{b}{\kappa}-1\right)d^4+O(|d|^3)
\longrightarrow-\infty.
\tag{23}
\]
Hence these local exact-Einstein arcs can satisfy
\[
\mathfrak b_+<-1,\qquad B>0,\qquad S>0,
\]
while carrying arbitrarily large \(q'\). Since \(\widehat P=0\), the chiral identities give
\[
\mathfrak b_\pm'\le0
\]
along the arc, so the upward chiral variation also vanishes. The change of \(q\) is supplied exactly by the initial momentum and the Einstein drift, and the left side of (21) is zero.

This local construction does not produce a complete regular bolt-to-standard-CH Einstein metric. It does show that the expanding hypotheses and the one-sided chiral cap alone cannot yield a positive function of \(|q_1-q_0|\). Global information fixing the incoming momentum or pricing its production is mathematically indispensable.

## 5. Separation of the three geometric mechanisms

* **Exact Einstein trajectories.** Here
  \[
  \mathcal C=D=E=0.
  \]
  Equation (2) forces \(\mathcal M=0\), and both chiral charges move only downward. Any anisotropy change must be exactly the sum of inherited momentum and Einstein drift. A proposed lower estimate that is positive on such data is incompatible with the exact equations.

* **Scalar-normalized competitors with \(\operatorname{Ric}^{\circ}\ne0\).** If the competitor lowers \(S\) enough to enlarge \(K\), the \(\mathcal C\)-channel pays at least \(L_{\mathcal C}\). If \(S\ge\sigma\), the Green denominator is bounded by (10), and every drift- and momentum-corrected anisotropy mismatch pays the \(D\)-cost in (11). The \(E\)-term remains unused and can only increase the action.

* **Raw high-shear paths.** An arbitrary incoming \(J_-\) can erase the numerator in (12). The two-stage identity moves any momentum produced after \(T_-\) into
  \[
  K_0\int_{I_-}WD,
  \]
  but a uniform value still requires control of the earlier flux \(J_-\), the production volume \(\mathcal W_-\), and the drift integral \(\Xi_-\). Chiral variation catches raw shear whenever either charge rises. If both charges stay level or move downward, the exact quantity that remains is the momentum-renormalized mismatch \(\mathcal M\).

Thus a uniform late-opening constant follows once a controlled collapsed section supplies bounded \(J_-\), \(\mathcal W_-\), and \(\Xi_-\), while a later expanding block supplies fixed \(W_0,\sigma,\mu,Q,\kappa_0\) and a CH-like endpoint with \(|q(T_1)|\ll |q(T_0)|\). Without those incoming-flux and drift data, the exact Einstein mode (22)–(23) gives the precise counter-mechanism.