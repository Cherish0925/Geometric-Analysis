# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 87,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step87_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step87_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 87 correction to the Step 86 product-orbifold Green-response claim. Read the Step 87 note, scripts/data, and the Step 86 note/TTCS memo. Check whether the missed mode h=(*du_A)⊗(*du_B)+(*du_B)⊗(*du_A) is a legitimate mixed one-form product eigentensor (P eigenvalue 1 in the stated product-sector convention), whether its quadratic jet near NN contains the fully mixed channels h_{03}=-x_1x_2 and h_{12}=-x_0x_3, whether the boundary source projection B_+-B_- is genuinely nonzero in the C_ab convention, and whether the receiver linearized curvature calculation supports a nonzero local radial response. Also identify any normalization/gauge/receiver caveats that prevent promoting this single-mode calculation to the full Ozuch coefficient c_opp-c_same.

## Integrated Scientific Memo

# Step 87 核验结论

Step 87 的核心修正成立。该模式是合法的 \(P\)-本征张量，其二次 jet 确实进入 Step 86 漏掉的四指标全混合通道；源端手征差和局部接收端径向曲率均严格非零。因此 Step 86 的“所有乘积本征模逐模消失”论证被反例推翻。

但这只证明一个局部、未归一化、同节点同标架的活跃通道；尚不能推出完整 Ozuch 系数 \(c_{\rm opp}-c_{\rm same}\neq0\)，更不能给出其数值或符号。

## 1. 模式合法性与 \(P\)-本征值

令单位二球面上的 \(u=\cos\theta\)，并置
\[
\alpha=*du_A,\qquad \beta=*du_B,\qquad
h=\alpha\otimes\beta+\beta\otimes\alpha .
\]

在 \(S^2(1)\) 上，
\[
\Delta_H\alpha=2\alpha,\qquad
\Delta_H=\nabla^*\nabla+\operatorname{Ric},
\qquad \operatorname{Ric}=g,
\]
故
\[
\nabla^*\nabla\alpha=\alpha,
\qquad
\nabla^*\nabla\beta=\beta.
\]
乘积联络给出
\[
\nabla^*\nabla h=2h.
\]
乘积曲率没有混合 \(AB\) 曲率分量，因此
\[
\mathring Rh=0.
\]
在 Step 85–87 的约定
\[
P=\frac12\nabla^*\nabla-\mathring R
\]
下，
\[
\boxed{Ph=h.}
\]
这等价于 sector ledger 的
\[
\lambda_P=\frac12(2+2-2)=1.
\]

此外，\(\alpha,\beta\) 余闭且分别只依赖一个因子，故
\[
\operatorname{tr}h=0,\qquad \delta h=0.
\]
因此它是 TT/Bianchi 模式，不是未约化微分同胚方向造成的伪通道。

该张量也下降到四节点商空间。不过 Step 87 中“两个 odd one-form factors”措辞应修正：局部系数在 \(x\mapsto-x\) 下为奇，但 \(dx\) 也变号，完整一形式的拉回是不变的。这里的商生成元是每个球面绕极轴旋转 \(\pi\)，其固定点为 \(N,S\)；不应称为标准球面 antipodal map，因为后者没有固定点。

## 2. 二次 jet 确实含全混合通道

在 NN 节点的定向正规坐标中，
\[
\alpha=x_1dx_0-x_0dx_1+O(r_A^3),\qquad
\beta=x_3dx_2-x_2dx_3+O(r_B^3).
\]
于是 \(h\) 的非零独立二次分量为
\[
\begin{aligned}
h_{02}&=x_1x_3,&
h_{03}&=-x_1x_2,\\
h_{12}&=-x_0x_3,&
h_{13}&=x_0x_2,
\end{aligned}
\]
及其对称分量。因此特别有
\[
\boxed{M_{03,12}=-1,\qquad M_{12,03}=-1.}
\]

数据中的
\[
D_{03,12}=D_{12,03}=2
\]
与这些项直接配对。乘积结构只要求张量指标分别来自 \(A,B\) 两因子，并不要求导数指标等于张量指标。对 Killing 一形式，导数方向恰被二维 Hodge 星旋转；Step 86 §8.2 的“指标匹配”假设只适用于其测试过的特殊梯度型模式，不适用于一般混合一形式积。

## 3. 源端边界投影严格非零

写
\[
h_{ij}=M_{ijpq}x_px_q,\qquad
D_{ijpq}=\sum_k\bigl(C_{2k,ij}C_{2k,pq}
-C_{k2,ij}C_{k2,pq}\bigr).
\]
在所给 \(C_{ab}\) 约定下，
\[
H_\pm^4=-\frac12\sum_k(x^TA_k^\pm x)A_k^\pm,
\quad
A_k^+=C_{2k},\quad A_k^-=C_{k2},
\]
且
\[
B_\pm=3\int_{S^3/\mathbb Z_2}\langle H_\pm^4,h_2\rangle\,d\sigma.
\]

利用
\[
\int_{S^3}x_ax_bx_px_q\,d\sigma
=\frac{\pi^2}{12}
(\delta_{ab}\delta_{pq}+\delta_{ap}\delta_{bq}
+\delta_{aq}\delta_{bp})
\]
以及 \(C_{ab}\) 对称无迹，可化为
\[
\boxed{B_+-B_-=-\frac{\pi^2}{8}\,D_{ijpq}M_{ijpq}.}
\]
脚本给出的精确收缩
\[
D:M=-8
\]
因此产生
\[
\boxed{B_+-B_-=\pi^2.}
\]
分项值也一致：
\[
\boxed{B_+=\frac{\pi^2}{2},\qquad
B_-=-\frac{\pi^2}{2}.}
\]

边界脚本中 `mode_report` 附近的注释曾暗示系数
\((-3/4)(\pi^2/12)\)；该注释漏掉了两个对称 Wick 收缩中的一个。正确系数是
\[
(-3/4)(\pi^2/6)=-\pi^2/8.
\]
实际循环包含两个收缩，故 JSON 数值正确。

这验证的是非零本征模源系数的自然局部 Green/Wronskian 配对，而不是 Proposition 2.10 中仅针对 \(v_l\in\ker P\) 的 \(\nu_l\)。把该配对放入完整 \(G_P^\perp\) 构造仍需明确全局奇异源和 gauge。

## 4. 接收端局部曲率计算正确

采用脚本约定
\[
\delta R_{ijkl}
=\frac12(h_{il,jk}+h_{jk,il}-h_{ik,jl}-h_{jl,ik}),
\]
有
\[
\delta R_{0213}
=\frac12(h_{03,21}+h_{12,03})=-1,
\qquad
\delta R_{0202}=\delta R_{1313}=0.
\]
对
\[
\omega_2^+=\frac{e_{02}-e_{13}}{\sqrt2},
\qquad
\omega_2^-=\frac{e_{02}+e_{13}}{\sqrt2},
\]
故
\[
\langle\omega_2^+,\delta R\,\omega_2^+\rangle=1,
\qquad
\langle\omega_2^-,\delta R\,\omega_2^-\rangle=-1.
\]
完整块为
\[
\boxed{\delta R^+=\operatorname{diag}(-2,1,1),\qquad
\delta R^-=\operatorname{diag}(2,-1,-1)}
\]
（若采用相反 Riemann 符号约定，两块整体反号）。

因此对脚本选择的 \(\zeta=\omega_2\)，局部径向响应分别为
\[
\boxed{L^+(h)=1,\qquad L^-(h)=-1.}
\]
由于此模式在节点满足
\[
h(0)=0,\qquad dh(0)=0,
\]
本项没有由常数 jet 引起的标架、Hodge 星或背景曲率修正；但 Ozuch 接收泛函的整体归一化常数仍未识别。

## 5. 对 Step 86 的精确修正

该模式的 \(\lambda_P=1\)，不是核模，因而不影响先前候选零模的
\[
\nu_l=0
\]
结论。它推翻的是进一步的错误推论：
\[
\text{“所有物理乘积本征模均落在 }\ker D\text{”。}
\]

同时必须修正 Step 86 的分布表述。核投影消失仅表示奇异源满足 Fredholm 相容条件，可在 \((\ker P)^\perp\) 上反演；并不意味着
\[
P\bar h=0
\]
在整个 orbifold 上分布成立。节点处仍存在多极分布源。否则椭圆正则性会迫使 \(\bar h\) 光滑，与 \(r^{-4}\) 奇异渐近矛盾。

## 6. 不能据此推出完整 \(c_{\rm opp}-c_{\rm same}\) 的原因

剩余障碍是实质性的，而不仅是一个总常数：

1. **同节点测试，不是节点间项。**  
   两个脚本都在 NN、同一局部标架计算。真正系数为
   \[
   L_iG_P^\perp S_j,\qquad i\ne j,
   \]
   要求同一全局本征张量在源节点 \(j\) 和接收节点 \(i\) 的 jets，以及 N/S 节点间的定向、\(\Lambda^\pm\) 基和 gluing frame 传输。

2. **必须投影整个简并本征空间。**  
   一个本征向量的非零乘积依赖基的选择；基无关对象是
   \[
   L_i\Pi_{\lambda=1}S_j.
   \]
   同一 \(\lambda=1\) 本征空间的其他模式可能加强或抵消该模式。因此当前结果反驳“逐模全零”，但尚未证明整个 \(\lambda=1\) 投影非零。

3. **全局 \(L^2\) 归一化。**  
   当前 \(h\) 未归一化，且对称积未除以 \(2\)。若商是二重覆盖商且 \(u=\cos\theta\)，则
   \[
   \|h\|_{L^2(\mathrm{orb})}^2=\frac{64\pi^2}{9},
   \qquad \widehat h=\frac{3}{8\pi}h.
   \]
   但即使据此得到脚本约定下的形式数 \(9/64\)，它仍不是 Ozuch 系数，因为接收端、EH 参数和节点传输尚未归一化。

4. **EH 方向依赖。**  
   计算固定了 \(\zeta^\pm=\omega_2^\pm\)。一般
   \[
   \zeta^\pm\in\operatorname{span}\{\omega_2^\pm,\omega_3^\pm\}
   \]
   时源投影和接收响应会随方向及 gluing frame 改变；\(\pi^2\) 不是方向无关的规范常数。

5. **接收泛函尚未与 Ozuch 障碍变量完全等同。**  
   脚本计算的是局部
   \[
   h\mapsto\delta R^\pm(h)(p_i).
   \]
   还需证明它与所用 Ozuch/Biquard chart 中的径向障碍泛函完全一致，包括 EH 核张量归一化、泡尺度与 \(\zeta\) 参数换算以及通用符号/常数。对当前 \(V_0=0\) 模式，常数-jet 修正消失，这是有利条件，但不是完整识别。

6. **完整 resolvent 与正则化。**  
   必须纳入所有允许 sectors、负特征值（特别是 \(P=-1\) shape mode）并排除核；同节点项还需减去局部奇异部分。Step 86 的简单 \(\ell^{-3}\) 收敛估计忽略了本征空间维数和 jet 增长，不能作为绝对收敛证明。

## 最终判定

\[
\boxed{\text{Step 87 的反例及其源端、接收端局部计算均成立。}}
\]

它严格建立了：

- 合法的 TT 混合本征张量 \(Ph=h\)；
- 漏掉的全混合 jet 通道；
- 精确非零源差 \(B_+-B_-=\pi^2\)；
- 精确非零局部径向响应 \(+1/-1\)。

因此 Step 86 的结构性逐模消失定理无效。尚未决定的精确数学对象是基无关、节点间、规范化且正则化的
\[
\boxed{L_iG_P^\perp(S_j^+-S_j^-)}
\]
及其所有节点和 eigenspaces 的组合；现有单模计算本身不能确定 \(c_{\rm opp}-c_{\rm same}\) 的非零性、数值或符号。