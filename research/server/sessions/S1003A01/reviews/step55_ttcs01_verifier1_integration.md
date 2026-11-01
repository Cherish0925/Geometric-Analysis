# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 55,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step55_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step55_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the Step-55 Goldberg note as a differential geometer. Check the tensor algebra and conventions in the Darboux Ricci-symbol relation, its divergence expansion, the Einstein specialization of AAD equation (33), and the Einstein specialization of AAD equation (47). In particular decide whether eta may be identified with rho_*'', whether coefficients 3/8, 1/4, 3s/4, 1/2, and the term 2 nabla_{J eta(X)} Omega are correct, and whether the conclusion that the bare scalar compatibility is a differential consequence rather than a negative-lambda obstruction is justified. Report corrections and any sharper global identity suggested by the checked equations. Ground the review in the supplied primary-source text; do not invent literature.

## Integrated Scientific Memo

## Verification memo

**The questioned tensor coefficients in Step 55 are correct.** With \(\eta\) understood as the **2-form**
\[
\eta=\bigl(W^+(\Omega)\bigr)_{\Omega^\perp},
\]
one has exactly \(\eta=\rho_*''\). The Einstein specializations of AAD (33) and (47) give the displayed \(3/8,\ 1/4,\ 3s/4,\ 1/2\), and \(2\nabla_{J\eta(X)}\Omega\).

There are three important corrections:

1. The Laplacian in the Darboux contraction must be specified: its displayed sign matches \(\Delta=\operatorname{tr}\nabla^2\), **not** AAD’s nonnegative Laplacian.
2. In the Einstein setting, the third Gray condition is **\(\eta=0\) alone**; \(W_3^+=0\) is unnecessary.
3. The bare Ricci contraction is a differential consequence of Einstein, but this does **not** establish that its resolved, lower-order compatibility condition is redundant in a truncated jet system. No negative-\(\lambda\) obstruction follows from the supplied calculation or numerical data.

The checked equations also yield an exact global Hessian-energy identity and a useful divergence identity for \(W_3^+\).

### 1. Darboux symbol and divergence expansion

Write a compatible metric variation as \(h(X,Y)=g(HX,Y)\). Fixing \(\Omega\) gives
\[
HJ+JH=0,\qquad h(JX,JY)=-h(X,Y),\qquad \operatorname{tr}h=0.
\]
The unrestricted Ricci symbol, up to an overall symbol-sign convention, is
\[
\sigma_{\mathrm{Ric}}(\xi)h
=\frac12\left(\xi\otimes h\xi+h\xi\otimes\xi
-|\xi|^2h-\xi\otimes\xi\,\operatorname{tr}h\right).
\]
Thus Step 55 correctly uses its restriction to compatible variations.

For \(A=\sigma_{\mathrm{Ric}}(\xi)h\), identifying covectors and vectors by \(g\),
\[
A(J\xi,J\xi)=\frac12|\xi|^2h(\xi,\xi),
\qquad \operatorname{tr}A=h(\xi,\xi).
\]
Consequently
\[
\boxed{A(J\xi,J\xi)-\frac12|\xi|^2\operatorname{tr}A=0.}
\]
This is independent of the contracted-Bianchi symbol. With \(\xi=e_1\), \(J\xi=e_2\), Bianchi fixes \(A_{11}=\tfrac12\operatorname{tr}A\) and \(A_{1j}=0\), whereas this relation fixes \(A_{22}=\tfrac12\operatorname{tr}A\).

The composite relation is fourth order in the metric. Its stated contribution \(n_{N-4}\) has the correct order, and the corrected counting arithmetic is
\[
12n_N-4n_{N+1}-4n_{N-1}-9n_{N-2}+4n_{N-3}+n_{N-4}
=N^2+8N-5.
\]
This is a corrected **symbol count**, not a proof of formal integrability.

**Laplacian correction.** Define \(L=\nabla^i\nabla_i\). The contraction whose frozen symbol is the boxed relation is
\[
\mathcal C_J(S)
=J_i{}^aJ_j{}^b\nabla^i\nabla^jS_{ab}
-\frac12L(\operatorname{tr}S).
\]
AAD uses \(\Delta=\delta d=-L\), as follows from its equation (14),
\(\Delta f=-\langle dd^Jf,\Omega\rangle\). In that convention the formula must instead read
\[
\boxed{\mathcal C_J(S)
=J_i{}^aJ_j{}^b\nabla^i\nabla^jS_{ab}
+\frac12\Delta(\operatorname{tr}S).}
\]
The operator is second order in \(S\), fourth order after substituting \(S=\operatorname{Ric}(g)\).

The divergence expansion itself is correct. Since \(d\Omega=0\) and \(\Omega\) is self-dual, \(\delta\Omega=0\), hence \(\nabla^iJ_i{}^a=0\). The product rule gives
\[
\boxed{
J_i{}^aJ_j{}^b\nabla^i\nabla^jS_{ab}
=\nabla^i\!\left(J_i{}^aJ_j{}^b\nabla^jS_{ab}\right)
-J_i{}^a(\nabla^iJ_j{}^b)\nabla^jS_{ab}.}
\]
On a closed manifold this gives Step 55 (2.4). For \(S=\lambda g\), constant \(\lambda\), both sides vanish pointwise.

### 2. Identification of \(\eta\) and specialization of AAD (33)

AAD §2.2, equation (8), gives
\[
W_2^+=\frac12(\rho_*''\otimes\Omega+\Omega\otimes\rho_*'').
\]
Because \(|\Omega|^2=2\) and \(\rho_*''\perp\Omega\),
\[
W_2^+(\Omega)=\rho_*''.
\]
Together with \(W_1^+(\Omega)=\frac{\kappa}{6}\Omega\) and \(W_3^+(\Omega)=0\), this proves
\[
\boxed{W^+(\Omega)=\frac{\kappa}{6}\Omega+\eta,\qquad \eta=\rho_*''.}
\]
This identification does not require Einstein.

There is a normalization distinction between the notes: in Step 48’s orthonormal matrix entries,
\[
\eta=\eta_1\phi+\eta_2J\phi,\qquad
|\eta|_{\mathrm{form}}^2=2(\eta_1^2+\eta_2^2).
\]
Step 53’s off-diagonal block \(\eta/\sqrt2\) uses the 2-form convention and is consistent with AAD.

For Einstein,
\[
\operatorname{Ric}=\frac{s}{4}g,\quad ds=0,\quad
\rho=\frac{s}{4}\Omega,\quad \rho_0=0,\quad \operatorname{Ric}''=0.
\]
AAD defines
\[
A_Z=(d^\nabla\operatorname{Ric}'')_Z+\iota_{JZ}d\rho,
\]
so \(A=0\). Its equation (20) gives
\[
q=|\nabla\Omega|^2=s^*-s,\qquad
s^*=\frac{2\kappa+s}{3},
\]
and therefore
\[
\boxed{\kappa-s=\frac32q.}
\]

Direct substitution in AAD (33) yields
\[
\boxed{
\begin{aligned}
0={}&-\frac38(d^Jq)_Z\Omega
+\frac14(dq\wedge Z^\flat)^+
+(\delta\eta)_Z\Omega\\
&+\frac{\kappa}{4}\nabla_{JZ}\Omega
+\nabla_{\eta(Z)}\Omega+\nabla_{JZ}\eta
+2(\delta W_3^+)_Z .
\end{aligned}}
\]
Thus Step 55 (3.6), including both questioned coefficients, is correct.

The two component equations, from AAD (37)–(38), are particularly useful:
\[
\boxed{
0=-\frac12(d^Jq)_Z
+2\langle(\delta W_3^+)_Z,\Omega\rangle
+2(\delta\eta)_Z-\langle\eta,\nabla_{JZ}\Omega\rangle,}
\tag{B\(_\Omega\)}
\]
\[
\boxed{
0=\frac14(dq\wedge Z^\flat)''
+\frac{\kappa}{4}\nabla_{JZ}\Omega
+2(\delta W_3^+)_Z''
+\nabla_{\eta(Z)}\Omega+(\nabla_{JZ}\eta)''.}
\tag{B\(_\perp\)}
\]

### 3. Specialization and reduction of AAD (47)

AAD (47) specializes exactly to
\[
\boxed{
\begin{aligned}
(\nabla^*\nabla(\nabla\Omega))_X+\frac{3s}{4}\nabla_X\Omega
={}&\left[\frac12dq_X
-2\langle(\delta W_3^+)_{JX},\Omega\rangle\right]\Omega\\
&+2(\nabla_X\eta)''
+2\nabla_{J\eta(X)}\Omega .
\end{aligned}}
\tag{H}
\]
All questioned coefficients and signs are correct. In the last term, the direction is \(J(\eta(X))\); since \(\eta\) anticommutes with \(J\),
\[
\eta(JX)=-J\eta(X).
\]
Interchanging these expressions would reverse the sign.

The source’s computation immediately before (47) independently confirms this term:
\[
(W_2^+\cdot\nabla\Omega)_X
=-\nabla_{J\rho_*''(X)}\Omega
-\frac12\langle\rho_*'',\nabla_X\Omega\rangle\Omega.
\]
The coefficient \(-2\) on the curvature action produces \(+2\nabla_{J\eta(X)}\Omega\).

**A source-text correction:** the displayed AAD (46) has
\[
\frac{\kappa-s}{2}\nabla\Omega,
\]
but its preceding equations (40), (43)–(45) give
\[
\frac{\kappa-s}{3}\nabla\Omega.
\]
The latter produces the coefficient in (47):
\[
-\frac{s}{4}-\frac{s}{6}-\frac{\kappa}{3}
+\frac{\kappa-s}{3}=-\frac{3s}{4}.
\]
Thus (46), as supplied, contains a coefficient error; (47) is consistent with the derivation and Proposition 1.

Equation (H) admits a sharper reduction. Set \(Z=JX\) in \((B_\Omega)\), using AAD’s convention \((d^Jq)_{JX}=dq_X\):
\[
\frac12dq_X-2\langle(\delta W_3^+)_{JX},\Omega\rangle
=2(\delta\eta)_{JX}+\langle\eta,\nabla_X\Omega\rangle.
\]
Hence
\[
\boxed{
\begin{aligned}
(\nabla^*\nabla(\nabla\Omega))_X+\frac{3s}{4}\nabla_X\Omega
={}&[2(\delta\eta)_{JX}+\langle\eta,\nabla_X\Omega\rangle]\Omega\\
&+2(\nabla_X\eta)''
+2\nabla_{J\eta(X)}\Omega .
\end{aligned}}
\tag{H\(_\eta\)}
\]
Thus \(\eta,\nabla\eta\) are the only explicit sources in this Helmholtz system; \((B_\perp)\) retains the transverse divergence constraint on \(W_3^+\).

AAD Lemma 1 identifies the third Gray condition with
\[
\operatorname{Ric}''=0,\qquad \rho_*''=0.
\]
For Einstein this is precisely **\(\eta=0\)**. Equation \((H_\eta)\) then becomes
\[
\boxed{\nabla^*\nabla(\nabla\Omega)+\frac{3s}{4}\nabla\Omega=0}
\]
without assuming \(W_3^+=0\). The supplied AAD local classification—not this equation alone—shows that strictly almost-Kähler Einstein metrics in this Gray class are the Ricci-flat local models.

### 4. What the scalar compatibility does and does not establish

The two interpretations should be separated.

- **Established:** \(\mathcal C_J(\operatorname{Ric})=0\) on Einstein metrics is a differential consequence of \(\nabla\operatorname{Ric}=0\). Its bare expression and its principal symbol give no negative-\(\lambda\)-specific obstruction.
- **Not established:** after eliminating fourth derivatives using compatibility, the resulting lower-order equation is redundant among already imposed lower Taylor equations. Differential consequences can be genuine integrability conditions at a lower jet order and can contain sign-sensitive terms.
- **Unsupported:** interpreting the reported full ranks or failed prolongations as evidence for a negative-scalar obstruction. The same extension failures occur for the nonexact “controls”; no explicit lower-order remainder or row dependence was evaluated on exact extendible controls.

AAD’s introduction expressly reports nontrivial higher-jet relations for \(\operatorname{Ric}''=0\). A source-grounded intrinsic scalar consequence illustrates the distinction. Put
\[
\theta=\rho_0-\frac{s}{4}\Omega=-*\rho.
\]
AAD (26), \(-\delta\theta=J\delta\operatorname{Ric}''\), implies
\[
\delta\operatorname{Ric}''=J*d\rho.
\]
Using \(\delta(J\alpha)=\langle d\alpha,\Omega\rangle\), valid because \(\delta\Omega=0\),
\[
\boxed{\delta\delta\operatorname{Ric}''
=\langle d*d\rho,\Omega\rangle.}
\tag{C}
\]
Modulo contracted Bianchi, its leading symbol is the additional Darboux scalar relation.

AAD’s closed canonical Chern form
\[
\gamma_J=\rho_*-a\wedge Ja
\]
and \(\rho_*-\rho=\eta+\frac q4\Omega\) further give
\[
d\rho=-d\eta+d(a\wedge Ja)-\frac14dq\wedge\Omega.
\]
Thus (C) can be written
\[
\delta\delta\operatorname{Ric}''
=\left\langle d*d\left(a\wedge Ja-\frac q4\Omega-\eta\right),\Omega\right\rangle.
\]
The highest symbol of the \(\eta\)-term vanishes because
\(\eta(\xi,J\xi)=0\); this exposes the derivative cancellation intrinsically. For Einstein, \(d\rho=0\) is equivalently closure of
\[
\beta=\gamma_J-\frac{s}{4}\Omega
=\eta+\frac q4\Omega-a\wedge Ja.
\]

This does not identify every component of Step 55’s particular coordinate remainder. The unresolved object is its **explicit lower-jet expression and its dependence on the lower equations**, not whether the unreduced Ricci expression vanishes on Einstein solutions.

### 5. Exact global identities

Assume henceforth that \(M\) is closed and Einstein. All \(\eta\)-norms below are **form norms**. Let
\[
T=\nabla\Omega,\qquad q=|T|^2,\qquad \nabla T=\nabla^2\Omega
\]
with the full ordered-two-index tensor norm.

#### Hessian energy

Pair (H) with \(T\) and integrate. The \(\Omega\)-valued term vanishes since \(T_X\perp\Omega\). The directional term also vanishes pointwise:
\[
\sum_i\langle T_{J\eta(e_i)},T_{e_i}\rangle=0,
\]
because \(J\eta\) is skew and \(\langle T_X,T_Y\rangle\) is symmetric.

AAD (41) gives
\[
\nabla^*\nabla\Omega=2\eta+\frac q2\Omega,
\]
so integration by parts yields
\[
2\int\langle\nabla\eta,T\rangle=4\int|\eta|^2.
\]
Therefore
\[
\boxed{
\int_M|\nabla^2\Omega|^2+\frac{3s}{4}\int_Mq
=4\int_M|\eta|^2.}
\tag{G1}
\]
For \(s<0\),
\[
\int|\nabla^2\Omega|^2
=\frac{3|s|}{4}\int q+4\int|\eta|^2.
\]
This explains precisely why this integration is not coercive toward \(q=0\).

The closed form \(\beta\) above satisfies \(\beta\wedge\beta=|\eta|^2d\mu\): \(\beta-\eta\) is decomposable and of type \((1,1)\), hence has square zero and wedges trivially with \(\eta\). Consequently
\[
\boxed{
\int|\nabla^2\Omega|^2+\frac{3s}{4}\int q
=4[\beta]^2,\qquad
[\beta]=2\pi c_1-\frac{s}{4}[\Omega].}
\]

#### Antisymmetric Hessian and the curvature balance

Let \(A_{XY}=\frac12(T_{X;Y}-T_{Y;X})\), with either consistent index ordering. AAD’s Ricci identities (23) give
\[
|A|^2=|R(\phi)|^2+|R(J\phi)|^2
=|\eta|^2+2|W_3^+|^2+\frac{q^2}{16}.
\]
Here \(|W_3^+|\) is its Hilbert–Schmidt norm on \(\Lambda^+\).

The Step-48 balance, with these normalizations, is
\[
\boxed{
\int\left(|\eta|^2+2|W_3^+|^2+\frac{3q^2}{16}\right)
=-\frac{s}{8}\int q.}
\tag{Balance}
\]
It can be checked directly by equating the canonical Chern-form square with the Einstein Chern–Weil expression:
\[
\gamma_J^2
=\left(|\eta|^2+\frac{s^2}{8}+\frac{sq}{8}\right)d\mu,
\]
\[
4\pi^2c_1^2
=\int\left(\frac{s^2}{24}+2|W^+|^2\right),\qquad
|W^+|^2=\frac{\kappa^2}{24}+|\eta|^2+|W_3^+|^2.
\]
Thus, for \(s<0\),
\[
\boxed{\int|A|^2=\frac{|s|}{8}\int q-\frac18\int q^2,}
\]
\[
\boxed{
\int|\operatorname{Sym}\nabla^2\Omega|^2
=\frac{5|s|}{8}\int q+4\int|\eta|^2+\frac18\int q^2.}
\tag{G2}
\]

#### Transverse divergence of \(W_3^+\)

Define the anti-invariant-form-valued 1-form
\[
B_Z=\frac14(dq\wedge Z^\flat)''
+\nabla_{\eta(Z)}\Omega+(\nabla_{JZ}\eta)''.
\]
Equation \((B_\perp)\) says
\[
2(\delta W_3^+)_Z''=-\frac{\kappa}{4}T_{JZ}-B_Z.
\]
The \(dq\)- and \(\eta(Z)\)-cross terms with \(T_{JZ}\) vanish pointwise; the remaining cross term is \(\langle\nabla\eta,T\rangle\). Squaring and integrating gives the exact identity
\[
\boxed{
4\int|(\delta W_3^+)''|^2
=\frac1{16}\int\kappa^2q
+\frac12\int\kappa\langle\nabla\eta,T\rangle
+\int|B|^2.}
\tag{G3}
\]
Equivalently, using \(d\kappa=\frac32dq\),
\[
\boxed{
4\int|(\delta W_3^+)''|^2
=\frac1{16}\int\kappa^2q+\int\kappa|\eta|^2
-\frac34\int\langle\eta,T_{\operatorname{grad}q}\rangle
+\int|B|^2.}
\]
Its nominal \(s^2q/16\) term is **not an unconditional lower bound**: the remaining terms require control.

A complementary pairing, followed by (Balance), yields
\[
\boxed{
\int\sum_i\langle(\delta W_3^+)_{e_i},T_{Je_i}\rangle
=-\frac18\int\kappa q-\int|\eta|^2
=2\int|W_3^+|^2.}
\]
These identities supply the concrete divergence information sought in Step 48. Turning it into a new rigidity estimate still requires the precise comparison with the **canonical-connection** derivative of \(W_3^+\), including its torsion corrections; the verified equations alone do not provide that coercive inequality.