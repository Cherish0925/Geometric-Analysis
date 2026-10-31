# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 26,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step26_ttcs02_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step26_ttcs02_sub2_generator.md"
    }
  ]
}
```

## Exact Task

Develop a mathematically serious next result for the diagonal scalar-normalized Bianchi-IX cell problem from the exact identities in the supplied notes. Focus on the non-round late-opening branch: combine the Hamiltonian constraint residual C, the anisotropy equation (W q')'=W(P_g-P_h-D), the chiral charge variation, and the expanding-block hypotheses to derive either (i) a reusable quantitative lower bound for a transition from a collapsed state to a CH-like state with b_+ below -1, or (ii) a precise counter-mechanism showing why such a bound cannot hold without extra hypotheses. Track all weights, endpoint terms, and drift terms. The result must distinguish exact Einstein trajectories, scalar-normalized competitors with nonzero trace-free Ricci, and raw high-shear paths; do not assume an unproved compactness theorem or invent numerical evidence.

## Integrated Scientific Memo

## Quantitative late-opening alternative with momentum production priced

Work throughout in the scalar-normalized diagonal class \(s\equiv-24\). On an interval \(I\),
\[
\widehat P_I
=\int_I W\left(\frac{\mathcal C^2}{3}+\frac{E^2}{6}+\frac{D^2}{8}\right)dt,
\]
where
\[
\mathcal C=\Ric^\circ_{00},\qquad
D=\Ric_{gg}-\Ric_{hh},\qquad
q=\log\frac{a_g}{a_h},\qquad J=Wq'.
\]
The exact anisotropy equation is
\[
J'=W(\Pi-D),\qquad
\Pi=P_g-P_h
=-8\zeta\sinh q+\frac{8\zeta^2}{\kappa^2}\sinh(2q).
\tag{1}
\]

The main obstruction in the one-interval Green estimate is the incoming momentum \(J(T_0)\). It cannot be dropped: it is a genuine zero-\(D\)-cost mode. The following two-stage identity prices the part of that momentum produced after an earlier controlled section.

### 1. Exact two-stage Green identity

Let
\[
T_-<T_0<T_1,\qquad I_-=[T_-,T_0],\quad I_+=[T_0,T_1],
\]
and on \(I_+\) set
\[
K(t)=\int_t^{T_1}\frac{du}{W(u)},\qquad K_0=K(T_0).
\]
Define
\[
J_-=W(T_-)q'(T_-),\qquad
\mathcal R_-=\int_{I_-}W\Pi\,dt,\qquad
\mathcal R_+=\int_{I_+}W\Pi K\,dt.
\]
Integrating (1) first on \(I_-\), then using Fubini on \(I_+\), gives
\[
\boxed{
\mathcal M:=
q(T_1)-q(T_0)-(J_-+\mathcal R_-)K_0-\mathcal R_+
=
-K_0\int_{I_-}WD\,dt-\int_{I_+}WDK\,dt.
}
\tag{2}
\]
Hence
\[
|\mathcal M|^2
\le
\left(\int_{I_-\cup I_+}WD^2dt\right)
\left(K_0^2\int_{I_-}Wdt+\int_{I_+}WK^2dt\right),
\]
and therefore
\[
\boxed{
\widehat P_{I_-\cup I_+}
\ge
\frac{\mathcal M^2}
{8\left(K_0^2\int_{I_-}Wdt+\int_{I_+}WK^2dt\right)}.
}
\tag{3}
\]
Unlike the one-stage estimate, (3) does not regard \(J(T_0)\) as free: momentum created on \(I_-\) is charged through the first \(D\)-integral. Only the flux inherited at \(T_-\) remains an endpoint datum.

### 2. Hamiltonian alternative and control of the Green kernel

Assume on \(I_+\)
\[
R^{(3)}\ge-\rho,\qquad A^2:=18-\rho>0,
\]
and choose
\[
0<\sigma<m:=\min\{S(T_0),A\}.
\]
Since
\[
S'=18-S^2+R^{(3)}+\mathcal C,
\tag{4}
\]
the corrected first-barrier argument yields the dichotomy
\[
\boxed{
S\ge\sigma\ \text{on }I_+,
\qquad\text{or}\qquad
\widehat P_{I_+}\ge
L_{\mathcal C}:=\frac{\sigma W_0}{3}(m-\sigma)^2,
}
\tag{5}
\]
where \(W_0=W(T_0)\).

Indeed, before the first point at which \(S=\sigma\),
\[
W(t)\ge W_0e^{\sigma(t-T_0)},\qquad
\int_{T_0}^t\frac{du}{W(u)}\le\frac1{\sigma W_0},
\]
while the first-barrier estimate gives
\[
m-\sigma\le\int_{T_0}^t|\mathcal C|\,du.
\]
Cauchy–Schwarz and the \(\mathcal C^2/3\) action term imply (5).

On the expanding alternative \(S\ge\sigma\),
\[
K(t)\le\frac1{\sigma W(t)},\qquad
K_0\le\frac1{\sigma W_0},\qquad
\int_{I_+}WK^2dt\le\frac1{\sigma^3W_0}.
\tag{6}
\]

Suppose additionally that on \(I_+\)
\[
B:=y_g+y_h\ge\mu>0,\qquad |q|\le Q,\qquad \kappa\ge\kappa_0>0.
\tag{7}
\]
Since \(\zeta'=-B\zeta\),
\[
\zeta(t)\le \zeta_0e^{-\mu(t-T_0)},\qquad \zeta_0=\zeta(T_0).
\]
Using (1) and (6),
\[
\boxed{
|\mathcal R_+|
\le
\Lambda_+
:=
\frac{8\zeta_0\sinh Q}{\sigma\mu}
+
\frac{4\zeta_0^2\sinh(2Q)}
{\sigma\mu\kappa_0^2}.
}
\tag{8}
\]
This is the correct two-rate version of the drift estimate: \(\sigma\) controls volume and the Green kernel, while \(\mu\) controls \(\zeta\)-decay. Setting \(\mu=\sigma\) recovers the estimate in the notes.

Let
\[
\mathcal W_-:=\int_{I_-}Wdt,\qquad
\Xi_-:=\int_{I_-}W|\Pi|dt.
\]
Then
\[
|\mathcal M|
\ge
\left(
|q(T_1)-q(T_0)|
-\frac{|J_-|+\Xi_-}{\sigma W_0}
-\Lambda_+
\right)_+
=:\Delta_q
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
Combining the two alternatives gives the reusable estimate
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

For a CH-like terminal section with
\[
|q(T_1)|\le\varepsilon,\qquad |q(T_0)|\ge Q_*,
\]
one may use
\[
\Delta_q\ge
\left(
Q_*-\varepsilon
-\frac{|J_-|+\Xi_-}{\sigma W_0}
-\Lambda_+
\right)_+.
\tag{12}
\]
Thus a positive late-opening gap follows once the incoming flux and pre-block drift are quantitatively smaller than the required anisotropy change.

If no production interval is used, the exact endpoint term remains:
\[
\widehat P_{I_+}\ge
\min\left\{
\frac{\sigma W_0}{3}(m-\sigma)^2,\,
\frac{\sigma^3W_0}{8}
\left(
|q_1-q_0|-\frac{|q'_0|}{\sigma}-\Lambda_+
\right)_+^2
\right\}.
\tag{13}
\]
The term \(q'_0/\sigma\) is indispensable.

### 3. Addition of chiral variation and the bolt-prefix budget

For any interval \(I\), define
\[
\mathcal V_\chi(I)
=\int_I\max\{0,\mathfrak b_+',\mathfrak b_-'\}\,dt.
\]
The pointwise chiral identities imply
\[
\widehat P_I\ge\mathcal V_\chi(I).
\tag{14}
\]
Because (11) and (14) use the same action on \(I_-\cup I_+\), they combine by a maximum, not by addition:
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

For an \(O(-1)\) bolt at \(t_b\), the disjoint prefix \([t_b,T_-]\) may be added:
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
\tag{16}
\]

At a controlled collapsed section,
\[
x=Xz^3+o(z^3),\qquad \chi=\Gamma z+o(z),
\]
the exact charge limits are
\[
\mathfrak b_+=-2-(\Gamma+4X)^2,\qquad
\mathfrak b_-=2+(\Gamma-4X)^2.
\]
Consequently the bolt prefix costs at least
\[
\mathcal V_\chi([t_b,T_-])
\ge \big((\Gamma-4X)^2-5\big)_++o(1).
\tag{17}
\]

If \(T_1\) is exactly the CH orbit of radius \(\tau\), then
\[
\mathfrak b_+(T_1)=2-9\sinh^4\tau,
\]
and
\[
\mathcal V_\chi([T_-,T_1])
\ge
\left(4+(\Gamma+4X)^2-9\sinh^4\tau\right)_++o(1).
\tag{18}
\]
Therefore
\[
\boxed{
\begin{aligned}
\widehat P_{[t_b,T_1]}
\ge\;&
\big((\Gamma-4X)^2-5\big)_+\\
&+\max\Bigg\{
\left(4+(\Gamma+4X)^2-9\sinh^4\tau\right)_+,\\
&\hspace{27mm}
\min\left(
\frac{\sigma W_0}{3}(m-\sigma)^2,\,
\frac{\Delta_q^2}{8\mathcal H}
\right)
\Bigg\}
+o(1).
\end{aligned}
}
\tag{19}
\]

The cap \(\mathfrak b_+\le-1\) forces an exact CH endpoint to obey
\[
2-9\sinh^4\tau\le-1
\quad\Longleftrightarrow\quad
\tau\ge \operatorname{arsinh}(3^{-1/4}),
\tag{20}
\]
but does not by itself make the charge term (18) positive for large \(\tau\). The Hamiltonian/\(D\)-channel term is precisely what remains effective there.

### 4. Precise obstruction to any stronger hypothesis-free bound

The exact one-stage identity is
\[
q_1-q_0-J_0K_0-\int_{I_+}W\Pi K\,dt
=-\int_{I_+}WDK\,dt.
\tag{21}
\]
Thus both incoming momentum and Einstein drift are genuine zero-\(D\)-cost mechanisms. A lower bound depending only on \(|q_1-q_0|\), expansion, and the cap \(\mathfrak b_+\le-1\) cannot be valid.

This is visible directly in exact Einstein initial data. At a principal orbit prescribe
\[
B=y_g+y_h=b>0,\qquad q'=d,
\]
so
\[
y_g=\frac{b+d}{2},\qquad y_h=\frac{b-d}{2},
\]
and choose
\[
y_f=
\frac{6+\frac12R^{(3)}-\frac14(b^2-d^2)}{b}.
\tag{22}
\]
Then
\[
y_fy_g+y_gy_h+y_hy_f=6+\frac12R^{(3)},
\]
hence \(\mathcal C=0\) at that orbit. For \(|d|\to\infty\),
\[
S=y_f+b\sim\frac{d^2}{4b}>0,
\]
while \(B=b>0\) remains fixed. The Einstein ODE with these constrained initial data has locally
\[
\mathcal C=D=E=0,\qquad \widehat P=0.
\]
For \(\kappa>b\), direct large-\(|d|\) expansion of the chiral charge gives
\[
\mathfrak b_+
=
\frac{a_f^2}{16b^2}
\left(\frac{b}{\kappa}-1\right)d^4+O(|d|^3)
\longrightarrow-\infty.
\tag{23}
\]
Hence local exact-Einstein arcs can simultaneously have
\[
B>0,\qquad S>0,\qquad \mathfrak b_+<-1,
\]
and arbitrarily large \(q'\), while paying zero defect action. Along such an arc the chiral identities imply \(\mathfrak b_\pm'\le0\), so upward charge variation also vanishes.

This local construction is not a complete regular bolt-to-CH Einstein cell. Its role is sharper: it proves that the expanding-block assumptions and one-sided chiral cap do not alone imply a positive late-opening cost. Any global theorem must additionally constrain the inherited momentum, price where it was produced, or impose global bolt/end information that rules out the local Einstein mode.

### 5. Separation of the three branches

1. **Exact Einstein trajectories.**  
   Here \(\mathcal C=D=E=0\), so \(\mathcal M=0\). Anisotropy change is supplied exactly by inherited momentum plus \(\Pi\)-drift. No valid defect bound may be positive on such compatible data.

2. **Scalar-normalized non-Einstein competitors.**  
   If \(S\) loses the required expansion, the Hamiltonian residual costs \(L_{\mathcal C}\). If expansion persists, every momentum- and drift-corrected mismatch costs at least \(\Delta_q^2/(8\mathcal H)\) through \(D\). The unused \(E\)-term is nonnegative and may strengthen the estimate through the separate fibre/base pinning identity.

3. **Raw high-shear paths.**  
   Charge variation excludes those that raise either \(\mathfrak b_+\) or \(\mathfrak b_-\); for example the recorded raw \(\Delta\eta=-8\) state already costs at least \(8.54957-7=1.54957\) on the bolt prefix. If both charges remain low or decrease, raw shear can still enter through \(J_-\). Formula (2) identifies the exact unresolved quantity: inherited flux \(J_-\), together with the production volume \(\mathcal W_-\) and drift budget \(\Xi_-\).

The resulting sharp conclusion is therefore an alternative rather than an unconditional universal constant: a non-round late opening pays through upward chiral variation, Hamiltonian loss of expansion, or the momentum-renormalized \(D\)-mismatch. Without quantitative control of the incoming anisotropy flux and geometric drift, exact Einstein high-momentum arcs provide the precise counter-mechanism.