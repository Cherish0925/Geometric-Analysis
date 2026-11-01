# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 65,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step65_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step65_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the mathematical correctness of the per-datum existence theorem for the degenerate cutoff flow in the given note. Focus on these specific claims:

1. PRINCIPAL SYMBOL: Is the principal symbol truly diagonal? Specifically, verify that the DeTurck Lie derivative term 2sym(d(β²)⊗W^♭) contributes no second-order β derivatives to the G-equation, and that β²W·Dβ contributes no second-order G derivatives to the β-equation. The DeTurck vector field W^k = G^{ab}(Γ^k_{ab}(G) - Γ^k_{ab}(ḡ)) involves first derivatives of G; check that ∂_i(β²W^k) does not introduce ∂²G into the scalar equation.

2. (ε,ν)-INDEPENDENCE: Verify that the ratio β^{2k}/(β²+ε)^j ≤ 1 for k≥j truly controls all ε-appearances in the tame hierarchy. In particular, check the Lie cross term (A03 Step 56 eq 3.9): when ∫D^mG · βD^{m+1}β · W is integrated by parts to produce ∫βD^{m+1}G · D^mβ · W, the absorption into D_m^G uses β⁴/(β²+ε) ≤ 1. Is this the correct power? Count the β-powers precisely.

3. CONTINUATION CRITERION: The argument claims that if T_max(ε,ν) < T₀, then the H^{s₀} bound survives, so all continuation hypotheses are met. Is this logically correct? Does the H^{s₀} bound, together with Sobolev embedding, truly prevent the solution from leaving the admissible domain (G positive definite) and prevent C^k blow-up?

4. SIGN-GENERAL EXTENSION: For general σ, the only change is the zero-order term +2σβ²G. Verify that this contributes C|σ|(1+E_m) to the m-th energy estimate, as claimed. Check that no hidden σ-dependence appears in the principal or Lie terms.

5. SMOOTH LIMIT: The claim is that C^∞ convergence of (G^ε,β^ε) to (G_∞,β_∞) plus ε(R+Q)→0 gives a solution of the exact system. Is there any subtlety about convergence of the nonlinear terms (e.g. Q quadratic in DG)?

## Integrated Scientific Memo

# 核验结论：现稿尚未完整证明逐数据存在定理

五项核验结果如下：

- **主符号对角性：正确。**
- **\((\varepsilon,\nu)\)-一致性：核心机制正确，但 Lie 项的 \(\beta\) 次数写错。**
- **延拓论证：结论可修复，但现有表述有逻辑缺口，不能仅凭 \(H^{s_0}\) 界按所述 Theorem A 直接延拓。**
- **任意符号 \(\sigma\)：正确，只增加零阶能量贡献。**
- **光滑极限：在所声称的全阶一致估计成立后正确。**

因此，逐数据短时存在结论具有可行的证明框架，但正文至少必须修正 \(\beta\)-权重记账，并补全延拓步骤。

## 1. 主符号确实是对角的

背景联络下
\[
W^k(G)=\frac12G^{ab}G^{k\ell}
 \bigl(D_aG_{b\ell}+D_bG_{a\ell}-D_\ell G_{ab}\bigr),
\]
所以 \(W\) 只依赖 \(G,DG\)。

度量方程中的额外项为
\[
2\operatorname{sym}(d(\beta^2)\otimes W^\flat)_{ij}
=(D_i\beta^2)W_j+(D_j\beta^2)W_i,
\]
其结构只是
\[
\beta\,D\beta * A(G)*DG.
\]
对扰动 \((h,b)\) 线性化只产生 \(Db*DG\)、\(D\beta*Dh\) 及零阶项，不产生 \(D^2b\) 或 \(D^2h\)。因此它不贡献二阶交叉主符号。

标量输运项
\[
F(G,\beta)=\beta^2W(G)^kD_k\beta
\]
的线性化为
\[
\delta F
=2\beta b\,W\cdot D\beta
+\beta^2\delta W\cdot D\beta
+\beta^2W\cdot Db,
\qquad
\delta W=A(G)*Dh+B(G,DG)*h.
\]
它也只含一阶扰动导数。因此固定 \(\varepsilon,\nu>0\) 时，二阶主符号是
\[
\sigma_2(\xi)(h,b)
=
\left(
(\beta^2+\varepsilon)G^{ab}\xi_a\xi_b\,h,\,
\nu\bar g^{ab}\xi_a\xi_b\,b
\right).
\]

需要澄清任务中提到的
\[
D_i(\beta^2W^k)
=2\beta D_i\beta\,W^k+\beta^2D_iW^k.
\]
这里 \(D_iW^k\) 的确含 \(D^2G\)，但该导数只在对标量方程做空间微分、建立高阶能量估计时出现；它不在原始标量方程中，故不改变基本系统的主符号。它对应 A03 的最高阶输运耦合 (3.12)。

## 2. \((\varepsilon,\nu)\)-一致性成立，但 Lie 项使用的是 \(\beta^2/(\beta^2+\varepsilon)\)

令
\[
a_\varepsilon=\beta^2+\varepsilon.
\]
对 \(0\le\beta\le1\) 和 \(k\ge j\)，
\[
\frac{\beta^{2k}}{a_\varepsilon^j}
=
\left(\frac{\beta^2}{a_\varepsilon}\right)^j
\beta^{2(k-j)}
\le1.
\]
还隐含使用了 \(a_\varepsilon\le2\) 和 \(D\varepsilon=0\)。

### Lie 项的正确次数

A03 (3.9) 为
\[
I=\int D^mG*\beta D^{m+1}\beta*W.
\]
积分分部后第一项为
\[
-\int \beta D^{m+1}G*D^m\beta*W.
\]
加权 Young 不等式给出
\[
|I_{\rm top}|
\le
\zeta\int a_\varepsilon|D^{m+1}G|^2
+C_\zeta\int
\frac{\beta^2}{a_\varepsilon}|D^m\beta|^2|W|^2.
\]
所以这里正确的权重是
\[
\boxed{\frac{\beta^2}{\beta^2+\varepsilon}\le1},
\]
不是 \(\beta^4/(\beta^2+\varepsilon)\)。

### \(\beta^4/a_\varepsilon\) 出现在输运耦合

标量方程微分后的最高阶度量耦合为
\[
\int D^m\beta*
 \beta^2 A(G)D^{m+1}G*D\beta.
\]
此处才有
\[
|J|
\le
\zeta\int a_\varepsilon|D^{m+1}G|^2
+C_{\zeta,R}\int
\frac{\beta^4}{a_\varepsilon}|D^m\beta|^2,
\]
故
\[
\frac{\beta^4}{\beta^2+\varepsilon}\le\beta^2\le1.
\]

精确记账是：

| 最高阶项 | \(D^{m+1}G\) 前因子 | Young 后权重 |
|---|---:|---:|
| \(DA*D^{m+1}G\) | \(\beta\) | \(\beta^2/a_\varepsilon\) |
| \(D(\beta^2)*D^mW\) | \(\beta\) | \(\beta^2/a_\varepsilon\) |
| Lie 项 (3.9) 分部后 | \(\beta\) | \(\beta^2/a_\varepsilon\) |
| 输运项 (3.12) | \(\beta^2\) | \(\beta^4/a_\varepsilon\) |

因此 A01 §4.3 的 Lie 项说明必须更正，但一致估计的结论不受影响。黏性项
\[
-\nu\|D^{m+1}\beta\|_2^2+C_m\nu\|\beta\|_{H^m}^2
\]
利用 \(\nu\le1\)，也不产生 \(1/\nu\)。

## 3. 延拓：现稿必须补用高阶层级，或改引明确的低阶延拓定理

首先，正定性并非仅由“\(H^{s_0}\) 有界”自动得到。若
\[
g_0\ge\lambda_0\bar g
\]
且低阶 bootstrap 区间上
\[
\|\partial_tG\|_{H^{s_0-2}}\le K_R,
\]
由于 \(s_0-2>n/2\)，
\[
\|G(t)-g_0\|_{C^0}\le CK_Rt.
\]
选取 \(T_0\) 使 \(CK_RT_0\le\lambda_0/2\)，即可保证
\[
G(t)\ge \frac{\lambda_0}{2}\bar g.
\]
上特征值则由 \(H^{s_0}\hookrightarrow C^0\) 控制。这是维持 admissible domain 的正确机制。

但现稿 Theorem A 将障碍表述为“某个有限 \(k\) 的 \(C^k\) 范数爆炸”。按此字面表述，仅有 \(H^{s_0}\hookrightarrow C^4\) 并不能排除任意更高 \(k\) 的爆炸。证明可按以下方式补全。

若固定 \((\varepsilon,\nu)\) 且假设
\[
T_{\max}<T_0,
\]
那么在整个 \([0,T_{\max})\) 上低阶界和统一正定性均成立。于是对每个 \(m>s_0\)，直接在现有区间应用 tame 估计：
\[
\frac d{dt}\mathcal E_m
\le C_{m,R,|\sigma|}(1+\mathcal E_m),
\]
从而
\[
\sup_{t<T_{\max}}\mathcal E_m(t)
\le
(\mathcal E_m(0)+1)e^{C_{m,R,|\sigma|}T_0}-1.
\]
初始数据光滑，故所有 \(m\) 均有界，进而所有 \(C^k\) 范数有界。结合
\[
\|\partial_tG\|_{H^{m-2}}
+\|\partial_t\beta\|_{H^{m-2}}\le C_m,
\]
可在 \(t\uparrow T_{\max}\) 取得光滑、仍正定的端点，并由固定参数强抛物理论重启，矛盾。

另一种修法是把 Theorem A 精确表述为：固定参数下，只要状态远离正定锥边界且某个指定的基准 \(H^s\) 或 \(C^{2,\alpha}\) 范数有界，即可延拓。现稿引用的抽象版本没有如此精确，因此补入上述全阶论证最稳妥。

还应处理闭区间端点：证明 \(T_{\max}\ge T_0\) 只保证解存在于 \([0,T_0)\)。要声称在 \(M\times[0,T_0]\) 光滑，需用相同端点界延伸超过 \(T_0\)，或将最终时间改取为预先构造时间的严格较小值。

## 4. 一般 \(\sigma\) 的扩展正确

新增项只有
\[
2\sigma\beta^2G.
\]
Moser tame 估计给出
\[
\|\beta^2G\|_{H^m}
\le C_{m,R}
\bigl(1+\|G\|_{H^m}+\|\beta\|_{H^m}\bigr),
\]
故
\[
\left|
\langle D^mG,D^m(2\sigma\beta^2G)\rangle
\right|
\le
C_{m,R}|\sigma|(1+\mathcal E_m).
\]
较低阶能量项同理。

\(\sigma\) 不进入 \(W\)、主系数、Lie 项、标量输运项或正则化权重。因此没有隐藏的主部或交叉项依赖；只有 Grönwall 常数和所选时间 \(T_0\) 可依赖 \(|\sigma|\)。

## 5. 光滑极限不存在额外非线性障碍

在统一正定壳层
\[
\lambda\bar g\le G_\ell\le\lambda^{-1}\bar g
\]
内，若
\[
(G_\ell,\beta_\ell)\to(G_\infty,\beta_\infty)
\quad\text{于 }C^\infty,
\]
则矩阵求逆的光滑性给出
\[
G_\ell^{-1}\to G_\infty^{-1}
\quad\text{于 }C^\infty.
\]
二次项可写为
\[
Q(G,DG)=A(G,G^{-1})*DG*DG,
\]
所以它在每个 \(C^k\) 中收敛；\(R\)、\(W\)、Lie 项和输运项同理。主项在 \(C^k\) 中通过极限只需 \(C^{k+2}\) 收敛，包含于所声称的 \(C^\infty\) 收敛。

若相应全阶一致界已经建立，则
\[
\left\|
\varepsilon_\ell
\bigl(G_\ell^{-1}D^2G_\ell+R(G_\ell)+Q(G_\ell,DG_\ell)\bigr)
\right\|_{C^k}
\le\varepsilon_\ell C_k\to0,
\]
且
\[
\|\nu_\ell\bar\Delta\beta_\ell\|_{C^k}
\le\nu_\ell C_k\to0.
\]
因此可逐项通过极限，得到精确系统。混合时间导数可由方程递归控制：每次时间微分至多要求更高空间阶数，且不需要除以 \(\varepsilon\) 或 \(\nu\)。

## 最终判定

该证明应判为“**可修复但现稿未完全闭合**”，而不是完全无误：

1. A01 §4.3 必须把 Lie 项的权重改为
   \[
   \beta^2/(\beta^2+\varepsilon),
   \]
   并把 \(\beta^4/(\beta^2+\varepsilon)\) 留给输运耦合。
2. §4.4 必须明确利用所有高阶 tame 估计排除任意 \(C^k\) 爆炸，或引用一个精确匹配 \(H^{s_0}\) 控制的延拓定理。
3. 必须补上 \(t=T_0\) 的端点延伸，或把最终闭区间缩短。

修正这三点后，五项受核验内容支持逐数据短时存在性。另需删除或另证 §9.2 关于精确退化系统唯一性的表述：正则化解唯一与子列紧致性并不能推出退化极限唯一；不过该问题不影响本次存在性结论。