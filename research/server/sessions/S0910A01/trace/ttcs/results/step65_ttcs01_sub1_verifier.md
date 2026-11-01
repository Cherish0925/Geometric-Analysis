# TTCS Independent Branch Record

```json
{
  "step_id": 65,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step65_per_datum_existence_theorem.md",
    "Sessions/S0910A03/workspace/notes/step56_tame_direct_flow_repair.md"
  ]
}
```

## Task

Verify the mathematical correctness of the per-datum existence theorem for the degenerate cutoff flow in the given note. Focus on these specific claims:

1. PRINCIPAL SYMBOL: Is the principal symbol truly diagonal? Specifically, verify that the DeTurck Lie derivative term 2sym(d(β²)⊗W^♭) contributes no second-order β derivatives to the G-equation, and that β²W·Dβ contributes no second-order G derivatives to the β-equation. The DeTurck vector field W^k = G^{ab}(Γ^k_{ab}(G) - Γ^k_{ab}(ḡ)) involves first derivatives of G; check that ∂_i(β²W^k) does not introduce ∂²G into the scalar equation.

2. (ε,ν)-INDEPENDENCE: Verify that the ratio β^{2k}/(β²+ε)^j ≤ 1 for k≥j truly controls all ε-appearances in the tame hierarchy. In particular, check the Lie cross term (A03 Step 56 eq 3.9): when ∫D^mG · βD^{m+1}β · W is integrated by parts to produce ∫βD^{m+1}G · D^mβ · W, the absorption into D_m^G uses β⁴/(β²+ε) ≤ 1. Is this the correct power? Count the β-powers precisely.

3. CONTINUATION CRITERION: The argument claims that if T_max(ε,ν) < T₀, then the H^{s₀} bound survives, so all continuation hypotheses are met. Is this logically correct? Does the H^{s₀} bound, together with Sobolev embedding, truly prevent the solution from leaving the admissible domain (G positive definite) and prevent C^k blow-up?

4. SIGN-GENERAL EXTENSION: For general σ, the only change is the zero-order term +2σβ²G. Verify that this contributes C|σ|(1+E_m) to the m-th energy estimate, as claimed. Check that no hidden σ-dependence appears in the principal or Lie terms.

5. SMOOTH LIMIT: The claim is that C^∞ convergence of (G^ε,β^ε) to (G_∞,β_∞) plus ε(R+Q)→0 gives a solution of the exact system. Is there any subtlety about convergence of the nonlinear terms (e.g. Q quadratic in DG)?

## Output

# 数学核验备忘录

## 总结

给定的正则化方案能够支持逐数据短时存在性。五个核心环节中：

1. 对基本未知量 \((G,\beta)\)，二阶主符号确实为对角形式。
2. \(\varepsilon\)-一致估计的机制成立，但式 (3.9) 积分分部后的正确比值是
   \(\beta^2/(\beta^2+\varepsilon)\)，不是
   \(\beta^4/(\beta^2+\varepsilon)\)；后者属于标量输运项 (3.12)。
3. 延拓论证需要补上一段：低阶 \(H^{s_0}\) 控制正定性和 \(C^4\)，而任意 \(C^k\) 控制应由同一低阶区间上的高阶能量估计推出。
4. 任意 \(\sigma\in\mathbb R\) 只增加零阶项，能量贡献确为
   \(C_{m,R}|\sigma|(1+\mathcal E_m)\)。
5. 在统一正定性和所有空间阶数一致估计下，所有非线性项均可通过 \(C^\infty\) 极限；这里没有额外的非线性收敛障碍。

---

## 1. 二阶主符号

令
\[
C^k_{ab}=\Gamma(G)^k_{ab}-\Gamma(\bar g)^k_{ab}.
\]
用背景联络 \(D\) 表示，
\[
C^k_{ab}
=\frac12G^{k\ell}
 \bigl(D_aG_{b\ell}+D_bG_{a\ell}-D_\ell G_{ab}\bigr),
\]
所以
\[
W^k=G^{ab}C^k_{ab}
\]
只含 \(G\) 的一阶导数，而
\[
W_i^\flat=G_{ik}W^k
\]
同样只含 \(G,DG\)。

### 度量方程中的额外 Lie 项

其坐标形式为
\[
2\operatorname{sym}\bigl(d(\beta^2)\otimes W^\flat\bigr)_{ij}
=(D_i\beta^2)W_j+(D_j\beta^2)W_i.
\]
因此该项是
\[
(D\beta)*(DG)
\]
型的一阶乘积。对扰动 \((h,b)\) 线性化时，只产生
\[
(Db)*(DG)+(D\beta)*(Dh)
\]
以及零阶项，不产生 \(D^2b\) 或 \(D^2h\)。

### 标量方程

\[
F(G,\beta)=\beta^2W(G)^kD_k\beta.
\]
其线性化为
\[
\delta F
=2\beta b\,W^kD_k\beta
 +\beta^2\,\delta W^k\,D_k\beta
 +\beta^2W^kD_kb,
\]
而
\[
\delta W=A(G)*Dh+B(G,DG)*h.
\]
故该方程对 \(h,b\) 也只含一阶导数。

因此，固定 \(\varepsilon,\nu>0\) 时，二阶主符号作用于 \((h,b)\) 为
\[
(h,b)\longmapsto
\left(
(\beta^2+\varepsilon)G^{ab}\xi_a\xi_b\,h,\;
\nu\bar g^{ab}\xi_a\xi_b\,b
\right),
\]
没有二阶交叉块。式 (3.2) 正确。

### 关于 \(D_i(\beta^2W^k)\)

这里需要区分基本方程与空间微分后的方程。事实上
\[
D_i(\beta^2W^k)
=2\beta(D_i\beta)W^k+\beta^2D_iW^k,
\]
并且
\[
D_iW^k=A(G)*D^2G+B(G,DG)*DG.
\]
所以，**对标量方程再作空间微分以后，确实会出现 \(D^2G\)**。这不改变基本 \((G,\beta)\) 系统的主符号，因为原标量方程中并没有 \(D_i(\beta^2W^k)\)。它在 \(H^m\) 能量中表现为
\[
\beta^2D^{m+1}G*D\beta*D^m\beta,
\]
正是 A03 式 (3.12) 处理的最高阶耦合。

---

## 2. \((\varepsilon,\nu)\)-一致性与精确的 \(\beta\) 次数

记
\[
a_\varepsilon=\beta^2+\varepsilon.
\]
当 \(0\le\beta\le1\)、\(k\ge j\) 时，
\[
\frac{\beta^{2k}}{a_\varepsilon^j}
=\left(\frac{\beta^2}{a_\varepsilon}\right)^j
 \beta^{2(k-j)}
\le1.
\]
这个恒等式正确。不过完整论证还同时使用了
\[
a_\varepsilon\le2,\qquad D\varepsilon=0.
\]
前者处理未进入加权 Young 不等式的项，后者说明系数微分不会产生新的 \(\varepsilon\)-项。

### Lie 项 (3.9) 的精确计算

最高阶部分为
\[
I=\int_M D^mG*\beta D^{m+1}\beta*W\,d\mu_{\bar g},
\]
忽略固定数值系数和张量缩并。将一个导数从 \(\beta\) 移出：
\[
\begin{aligned}
I={}&-\int_M
 \beta D^{m+1}G*D^m\beta*W\\
&-\int_M
 D^mG*D\beta*D^m\beta*W\\
&-\int_M
 D^mG*\beta D^m\beta*DW .
\end{aligned}
\]
第一项满足
\[
\begin{aligned}
\left|
\int \beta D^{m+1}G*D^m\beta*W
\right|
\le{}&
\zeta\int a_\varepsilon|D^{m+1}G|^2\\
&+C_\zeta\int
\frac{\beta^2}{a_\varepsilon}|D^m\beta|^2|W|^2.
\end{aligned}
\]
所以这里使用的是
\[
\boxed{\frac{\beta^2}{\beta^2+\varepsilon}\le1.}
\]
原文把它写成 \(\beta^4/(\beta^2+\varepsilon)\) 是一次幂数错置，但正确的 \(\beta^2/a_\varepsilon\) 同样给出所需的一致估计。

### \(\beta^4/a_\varepsilon\) 真正出现的位置

在标量输运项中，
\[
D^m(\beta^2W\cdot D\beta)
\]
含有
\[
\beta^2A(G)D^{m+1}G*D\beta.
\]
与 \(D^m\beta\) 配对后得到
\[
J=\int D^m\beta*
 \beta^2 A(G)D^{m+1}G*D\beta .
\]
此时加权 Young 不等式给出
\[
|J|
\le\zeta\int a_\varepsilon|D^{m+1}G|^2
+C_{\zeta,R}\int
 \frac{\beta^4}{a_\varepsilon}|D^m\beta|^2.
\]
故
\[
\boxed{\beta^4/(\beta^2+\varepsilon)}
\]
属于 A03 式 (3.12)，而不是式 (3.9)。

其余最高阶项的权重如下：

| 项 | \(D^{m+1}G\) 前的 \(\beta\) 因子 | Young 后比值 |
|---|---:|---:|
| \(D a_\varepsilon*D^{m+1}G\) | \(\beta\) | \(\beta^2/a_\varepsilon\) |
| \(D(\beta^2)*D^mW\) | \(\beta\) | \(\beta^2/a_\varepsilon\) |
| 式 (3.9) 积分分部后 | \(\beta\) | \(\beta^2/a_\varepsilon\) |
| 标量输运式 (3.12) | \(\beta^2\) | \(\beta^4/a_\varepsilon\) |

对于 \((\beta^2+\varepsilon)Q(G,DG)\)，最高阶 \(D^{m+1}G\) 自带
\(a_\varepsilon\)，可直接由度量耗散吸收。其余系数微分项全部由 tame 乘积估计处理，不需要除以 \(\varepsilon\)。

黏性项则给出
\[
-\nu\|D^{m+1}\beta\|_2^2
+C_m\nu\|\beta\|_{H^m}^2,
\]
并用 \(0<\nu\le1\) 控制第二项，不出现 \(1/\nu\)。

---

## 3. 正定性与延拓

设初始度量满足
\[
g_0\ge \lambda_0\bar g
\]
且 \(\lambda_0>0\)。低阶方程估计给出
\[
\|\partial_tG\|_{H^{s_0-2}}\le K_R
\]
直至低阶 bootstrap 区间结束。由于
\[
s_0-2>\frac n2,
\]
有 \(H^{s_0-2}\hookrightarrow C^0\)，故
\[
\|G(t)-g_0\|_{C^0}
\le C K_Rt.
\]
取时间足够小，使 \(CK_RT_0\le\lambda_0/2\)，便得到
\[
G(t)\ge \frac{\lambda_0}{2}\bar g.
\]
所以正定性不是单由 \(H^{s_0}\) 有界推出的，而是由低阶能量与时间导数控制共同推出的。上特征值则由 \(H^{s_0}\hookrightarrow C^0\) 控制。

现稿延拓段落还需要明确处理任意阶导数。其 Theorem A 写成“某个有限 \(k\) 的 \(C^k\) 范数发散”，仅有一个 \(H^{s_0}\) 界并不能按字面排除任意大的 \(k\)。但同一份 tame 层级已经提供所需桥梁：

假定固定 \((\varepsilon,\nu)\) 的最大时间满足
\[
T_{\max}<T_0.
\]
在 \([0,T_{\max})\) 上，低阶界和统一正定性已经成立。因此对每个 \(m>s_0\)，可直接应用 (4.3)：
\[
\frac d{dt}\mathcal E_m
\le C_{m,R,|\sigma|}(1+\mathcal E_m).
\]
于是
\[
\sup_{t<T_{\max}}\mathcal E_m(t)
\le
\bigl(\mathcal E_m(0)+1\bigr)
e^{C_{m,R,|\sigma|}T_0}-1.
\]
该推导只用到当前已存在的区间，并不预先使用向右延拓。由于初始数据光滑，对每个 \(m\) 都得到有限上界，继而所有 \(C^k\) 范数均有上界。再结合
\[
\|\partial_tG\|_{H^{m-2}}
+\|\partial_t\beta\|_{H^{m-2}}\le C_m,
\]
可在 \(t\uparrow T_{\max}\) 时取得光滑端点，并从该端点重新应用固定参数的强抛物理论。

因此延拓结论成立，但正文宜明确引用“所有 \(m\) 的 (4.3)”，或者将所用抛物定理直接表述为 \(H^{s_0}\) 型延拓定理。

另有一个端点细节：由“排除 \(T_{\max}<T_0\)”只能先得到
\(T_{\max}\ge T_0\)。若恰有 \(T_{\max}=T_0\)，仍需用上述端点估计把解延伸到 \(T_0\) 之后；也可以从一开始把最终闭区间取为初步时间的一半。

---

## 4. 任意 \(\sigma\) 的零阶项

新增项为
\[
2\sigma\beta^2G.
\]
Moser 乘积估计给出
\[
\|\beta^2G\|_{H^m}
\le C_{m,R}
\bigl(1+\|G\|_{H^m}+\|\beta\|_{H^m}\bigr),
\]
其中低阶 \(L^\infty\) 因子由固定的 \(H^{s_0}\) 界控制。于是
\[
\begin{aligned}
2|\sigma|
\left|\left\langle
D^mG,D^m(\beta^2G)
\right\rangle\right|
&\le
C_{m,R}|\sigma|
\left(1+\|G\|_{H^m}^2+\|\beta\|_{H^m}^2\right)\\
&\le C_{m,R}|\sigma|(1+\mathcal E_m).
\end{aligned}
\]
较低阶的 \(D^kG\) 项同理。

\(\sigma\) 不进入：

- \(W(G)\) 的定义；
- 度量方程的二阶系数；
- Lie 交叉项；
- 标量输运方程；
- \(\varepsilon,\nu\) 权重。

所以主符号和所有最高阶吸收均与 \(\sigma\) 无关。时间 \(T_0\) 和能量常数可以依赖 \(|\sigma|\)。

---

## 5. 光滑极限与非线性项

统一正定性给出
\[
\lambda\bar g\le G_\ell\le\lambda^{-1}\bar g.
\]
若
\[
G_\ell\to G_\infty,\qquad
\beta_\ell\to\beta_\infty
\]
在 \(C^\infty\) 中成立，则光滑矩阵求逆定理给出
\[
G_\ell^{-1}\to G_\infty^{-1}
\quad\text{于 }C^\infty.
\]

二次项可写成有限和
\[
Q(G,DG)=A(G,G^{-1})*DG*DG.
\]
因此
\[
Q(G_\ell,DG_\ell)\to
Q(G_\infty,DG_\infty)
\]
于每个 \(C^k\) 中。代数曲率项 \(R(G,\bar g)\)、DeTurck 向量场、Lie 项和输运项也具有相同连续性。二阶主项需要 \(G_\ell\to G_\infty\) 的 \(C^{k+2}\) 收敛，而现有任意阶一致估计足以提供它。

对于正则化余项，
\[
\left\|
\varepsilon_\ell
\bigl(G_\ell^{-1}D^2G_\ell+R(G_\ell)+Q(G_\ell,DG_\ell)\bigr)
\right\|_{C^k}
\le \varepsilon_\ell C_k\to0,
\]
以及
\[
\|\nu_\ell\bar\Delta\beta_\ell\|_{C^k}
\le\nu_\ell C_k\to0.
\]
故可逐项通过极限，得到精确的退化输运系统。

混合时间导数的一致性也可由方程递归获得：一次时间微分损失至多两个空间导数，而所有空间阶数均已有统一上界，且递归过程中只乘以
\(\varepsilon,\nu\)，从不除以它们。

最后，
\[
\frac d{dt}\beta(t,\varphi_t(x))
=\beta_t+d\beta(-\beta^2W)=0,
\]
所以
\[
\beta(t,\varphi_t(x))=\chi(x).
\]
度量拉回中的
\(\mathcal L_{\beta^2W}G\) 与 \(\varphi_t\) 生成的
\(\mathcal L_{-\beta^2W}G\) 抵消，从而恢复
\[
\partial_tg=-2\chi^2(\operatorname{Ric}_g-\sigma g).
\]

---

## 与主定理相邻的两处文字问题

1. §9.2 中“正则化系统唯一，因此精确退化系统也由同一极限论证唯一”的句子没有由紧致性推出。唯一的正则化解仍可能存在不同子列极限；精确系统的唯一性需要直接的差分能量估计。该句不参与存在性证明。

2. Restart 段落混合了两个坐标框架。若直接从几何数据 \((g(T),\chi)\) 重新应用定理，新输运变量初值是 \(\tilde\beta(0)=\chi\)。若沿用旧的 DeTurck 坐标，则初值应是
   \[
   (G(T),\beta(T)),\qquad
   \beta(T)=\chi\circ\varphi_T^{-1}.
   \]
   在约定 \(g=\varphi^*G\) 下，若新 gauge 映射为 \(\psi_s\)，旧坐标中的组合为
   \[
   \varphi_{T+s}=\psi_s\circ\varphi_T,
   \]
   因为
   \[
   \varphi_T^*\psi_s^*=(\psi_s\circ\varphi_T)^*.
   \]
   这不影响逐数据短时存在性，但 restart 的书写需要统一采用其中一个坐标框架。