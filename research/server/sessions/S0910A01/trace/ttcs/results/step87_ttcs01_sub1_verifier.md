# TTCS Independent Branch Record

```json
{
  "step_id": 87,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step87_missed_mode_green_correction.md",
    "Sessions/S0910A01/workspace/scripts/step87_missed_killing_mode_boundary.py",
    "Sessions/S0910A01/workspace/data/step87_missed_killing_mode_boundary.json",
    "Sessions/S0910A01/workspace/scripts/step87_missed_killing_mode_receiver.py",
    "Sessions/S0910A01/workspace/data/step87_missed_killing_mode_receiver.json",
    "Sessions/S0910A01/workspace/notes/step86_kernel_projection_vanishing_and_green_formula.md",
    "Sessions/S0910A01/trace/ttcs/results/step86_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Verify the Step 87 correction to the Step 86 product-orbifold Green-response claim. Read the Step 87 note, scripts/data, and the Step 86 note/TTCS memo. Check whether the missed mode h=(*du_A)⊗(*du_B)+(*du_B)⊗(*du_A) is a legitimate mixed one-form product eigentensor (P eigenvalue 1 in the stated product-sector convention), whether its quadratic jet near NN contains the fully mixed channels h_{03}=-x_1x_2 and h_{12}=-x_0x_3, whether the boundary source projection B_+-B_- is genuinely nonzero in the C_ab convention, and whether the receiver linearized curvature calculation supports a nonzero local radial response. Also identify any normalization/gauge/receiver caveats that prevent promoting this single-mode calculation to the full Ozuch coefficient c_opp-c_same.

## Output

# Step 87 科学核验备忘录

## 总体结论

Step 87 的核心修正成立：

1. 
   \[
   h=\alpha\otimes\beta+\beta\otimes\alpha,\qquad
   \alpha=*du_A,\quad \beta=*du_B
   \]
   是合法的混合 \(AB\) 对称二阶张量；在文中
   \[
   P=\tfrac12\nabla^*\nabla-\mathring R
   \]
   的约定下满足 \(Ph=h\)。

2. 它在 NN 节点的二次 jet 确实含有
   \[
   h_{03}=-x_1x_2,\qquad h_{12}=-x_0x_3,
   \]
   因而进入 Step 86 忽略的四指标全混合通道。

3. Step 87 第一个 Python 计算中的链球面配对是精确非零的：
   \[
   B_+=\frac{\pi^2}{2},\qquad
   B_-=-\frac{\pi^2}{2},\qquad
   B_+-B_-=\pi^2.
   \]

4. `step87_missed_killing_mode_receiver.py` 给出的曲率块也正确：
   \[
   \delta R^+=\operatorname{diag}(-2,1,1),\qquad
   \delta R^-=\operatorname{diag}(2,-1,-1),
   \]
   所以对 \(\zeta=\omega_2\)，径向分量分别为 \(+1\) 与 \(-1\)。

因此，Step 86 中“所有乘积本征张量都因张量指标与导数指标匹配而落在 \(\ker D\)”这一推理不成立。这个模式已经足以推翻逐模式消失结论。它仍未确定完整的 \(c_{\rm opp}-c_{\rm same}\)，因为该量需要全本征空间投影、四节点传输及 Ozuch 接收泛函的统一识别。

---

## 1. 模式的本征值与 gauge 性质

在单位二球面上，若 \(u\) 是 \(\ell=1\) 高度函数，则
\[
\Delta_H(*du)=2(*du).
\]
由 Weitzenböck 公式
\[
\Delta_H\alpha=\nabla^*\nabla\alpha+\operatorname{Ric}(\alpha),
\qquad \operatorname{Ric}=g,
\]
得到
\[
\nabla^*\nabla\alpha=\alpha,\qquad
\nabla^*\nabla\beta=\beta.
\]
乘积联络因而给出
\[
\nabla^*\nabla h=2h.
\]
对混合 \(AB\) 分量，乘积曲率没有交叉项，所以
\[
\mathring Rh=0.
\]
于是
\[
\boxed{Ph=\tfrac12(2h)-0=h.}
\]

这也直接复核了 sector ledger 中
\[
\lambda_P
=\frac12\bigl(2+2-2\bigr)=1.
\]

此外，\(\alpha,\beta\) 都余闭，且分别只依赖一个因子，因此
\[
\operatorname{tr}h=0,\qquad \delta h=0.
\]
故该模式位于 Bianchi/TT 子空间，不是因未约化微分同胚方向而产生的伪通道。

### 商空间与附加对称性

对产生四个 \(A_1\) 节点的轴向半转，\(u\) 与 \(*du\) 都在拉回下不变，所以 \(h\) 确实下降到商空间。对同时共轭 \(J\)，每个 \(*du\) 改变符号，而二者乘积不变。

JSON 中“two odd one-form factors”的措辞不够精确：在局部 \(x\mapsto-x\) 下，一形式的系数是奇函数，但 \(dx\) 也改变符号；作为完整一形式，\(\alpha\) 在轴向半转下是拉回不变的。脚本记录的二次 jet 拉回误差为零，与正确的张量变换一致。

“antipodal”一词也应明确指轴向半转；标准球面 antipodal 映射没有固定点，不能产生这里的四个 orbifold 节点。

---

## 2. 二次 jet 的全混合分量

在北极测地正规坐标中
\[
u=\cos r=1-\frac12r^2+O(r^4),
\]
并取 \(dx_0\wedge dx_1\) 的局部定向，则
\[
*du=x_1dx_0-x_0dx_1+O(r^3).
\]
同理，
\[
\beta=x_3dx_2-x_2dx_3+O(r^3).
\]

因此 \(h\) 的全部非零二次混合分量为
\[
\begin{aligned}
h_{02}&=x_1x_3, &
h_{03}&=-x_1x_2,\\
h_{12}&=-x_0x_3, &
h_{13}&=x_0x_2,
\end{aligned}
\]
以及由 \(h_{ij}=h_{ji}\) 得到的对称项。余项为 \(O(r^4)\)。

特别地，
\[
M_{03,12}=-1,\qquad M_{12,03}=-1.
\]
它们与数据中的
\[
D_{03,12}=D_{12,03}=2
\]
直接配对。乘积结构只规定前两个指标一个来自 \(A\)、一个来自 \(B\)，并不规定导数指标必须重复前两个指标；Step 86 正是在这里遗漏了真实的乘积模式。

---

## 3. 链球面配对的独立复算

令
\[
A_k^+=C_{2k},\qquad A_k^-=C_{k2},
\]
并写
\[
h_{ij}=M_{ijpq}x_px_q.
\]
在 \(S^3\) 上，
\[
H_\epsilon^4
=-\frac12\sum_k(x^TA_k^\epsilon x)A_k^\epsilon.
\]
结合 \(S^3/\mathbb Z_2\) 的体积因子 \(1/2\)，可写成
\[
B_\epsilon
=-\frac34\sum_k\int_{S^3}
(x^TA_k^\epsilon x)
(A_{k,ij}^\epsilon M_{ijpq}x_px_q)\,d\sigma.
\]

由于每个 \(C_{ab}\) 对称且无迹，四次矩公式给出
\[
\int_{S^3}
(x^TAx)(A_{ij}M_{ijpq}x_px_q)\,d\sigma
=
\frac{\pi^2}{6}A_{ij}A_{pq}M_{ijpq}.
\]
这里 \(\delta_{ap}\delta_{bq}\) 与
\(\delta_{aq}\delta_{bp}\) 两项都贡献。

所以
\[
B_+-B_-
=-\frac{\pi^2}{8}D_{ijpq}M_{ijpq}.
\]
数据中的精确整数收缩为
\[
D:M=-8,
\]
从而
\[
\boxed{B_+-B_-=\pi^2.}
\]
第一份 JSON 的分项结果
\[
B_+=\frac{\pi^2}{2},\qquad B_-=-\frac{\pi^2}{2}
\]
与此完全一致。

第一份脚本在 `mode_report` 附近的注释曾试写
\[
(-3/4)(\pi^2/12)\,D:M.
\]
该注释少了第二个 Wick 收缩；正确系数是
\[
(-3/4)(\pi^2/6)=-\pi^2/8.
\]
实际循环调用 `moment_coeff` 时包含了两个收缩，所以 JSON 数值没有受这条注释影响。

---

## 4. 接收端曲率的手算复核

对于 Killing–Killing 模式，
\[
h_{02}=x_1x_3,\quad
h_{03}=-x_1x_2,\quad
h_{12}=-x_0x_3,\quad
h_{13}=x_0x_2.
\]
采用脚本明示的约定
\[
\delta R_{ijkl}
=\frac12(h_{il,jk}+h_{jk,il}-h_{ik,jl}-h_{jl,ik}),
\]
有
\[
\delta R_{02\,13}
=\frac12(h_{03,21}+h_{21,03})
=-1.
\]
同时
\[
\delta R_{02\,02}=\delta R_{13\,13}=0.
\]

对
\[
\omega_2^+=\frac{e_{02}-e_{13}}{\sqrt2},
\qquad
\omega_2^-=\frac{e_{02}+e_{13}}{\sqrt2},
\]
于是
\[
\begin{aligned}
\langle\omega_2^+,\delta R\,\omega_2^+\rangle
&=2\left(\frac1{\sqrt2}\right)
\left(-\frac1{\sqrt2}\right)(-1)=1,\\
\langle\omega_2^-,\delta R\,\omega_2^-\rangle
&=2\left(\frac1{\sqrt2}\right)
\left(\frac1{\sqrt2}\right)(-1)=-1.
\end{aligned}
\]
同样计算其余对角元便得到
\[
\boxed{
\delta R^+=\operatorname{diag}(-2,1,1),\qquad
\delta R^-=\operatorname{diag}(2,-1,-1).
}
\]

该模式在节点满足
\[
h(0)=0,\qquad \nabla h(0)=0.
\]
因此此处没有由常数 jet 引起的正交标架、Hodge 星算子或背景曲率修正。整体 Riemann 符号约定可能同时翻转两个矩阵，但不能使径向响应变成零。

---

## 5. 该单模的 \(L^2\) 归一化可以显式补出

若高度函数取 \(u=\cos\theta\)，则
\[
\|\alpha\|_{L^2(S^2)}^2
=\int_{S^2}\sin^2\theta\,dA
=\frac{8\pi}{3},
\]
\(\beta\) 同样如此。覆盖空间上
\[
\|h\|^2
=2\|\alpha\|^2\|\beta\|^2
=\frac{128\pi^2}{9}.
\]
商空间积分为覆盖空间的一半，故
\[
\|h\|^2_{(S^2\times S^2)/\mathbb Z_2}
=\frac{64\pi^2}{9},
\qquad
\widehat h=\frac{3}{8\pi}h.
\]

若暂时只采用脚本中的源配对和局部曲率接收映射，则归一化后的 plus-minus 单模差为
\[
\frac{B_+(\widehat h)-B_-(\widehat h)}{\lambda_P}
\,L^+(\widehat h)
=
\left(\frac{3}{8\pi}\right)^2\pi^2
=\frac9{64}.
\]
该数值只属于这套局部约定；EH 参数尺度、Ozuch 障碍量的常数以及节点标架传输尚未并入。

---

## 6. 与完整 \(c_{\rm opp}-c_{\rm same}\) 之间仍缺少的数学识别

### 6.1 单个简并本征向量不是完整本征空间贡献

\(\lambda_P=1\) 的 Killing–Killing 空间具有简并性。一个归一化本征向量的乘积
\[
L(\widehat h)\,S(\widehat h)\neq0
\]
依赖所选正交基；真正不依赖基的量是整个 \(\lambda=1\) 本征空间投影
\[
L\,\Pi_{\lambda=1}\,S.
\]
其他同特征值模式仍可能产生抵消。因此现有计算证明“逐模式全零”错误，但尚未证明整个 \(\lambda=1\) 投影非零。

### 6.2 当前计算是同节点、同标架测试

真正的节点间项要求在源节点 \(j\) 和接收节点 \(i\) 分别展开同一个全局本征张量。N/S 节点的定向标架、\(\Lambda^\pm\) 基、\(\zeta\) 方向以及 \(A,J,L\) 的传输都可能引入符号或 \(\omega_2,\omega_3\) 混合。第一份脚本只处理 NN，接收脚本也使用同一局部标架。

### 6.3 Ozuch Proposition 2.10 直接表述的是核投影

该命题直接给出的
\[
3\int\langle H^4,V_{l,2}\rangle
\]
针对 \(v_l\in\ker P\)。把同一局部 Green 配对用于 \(\lambda=1\) 模式，需要把奇异源 \(S_j\) 与全局 gauge 明确定义。

对当前模式，这一延拓相当有力：它从二次阶开始，
\[
V_0=V_1=0,
\]
所以 \(r^{-2}\) 奇异修正、常数 jet 和标架修正都不能贡献有限配对；主导的 \(H_{-4}\)-\(V_2\) Wronskian 正是上面的系数 \(3\)。但完整文献识别仍需把此局部 Green 恒等式写入所采用的 Ozuch 全局奇异解。

### 6.4 接收泛函的整体常数

脚本计算的是
\[
h\longmapsto \delta R^\pm(h)(p_i).
\]
Ozuch 的径向障碍变量还可能包含：

- EH 核张量的归一化；
- \(\zeta\) 参数与泡尺度的换算；
- 曲率算子与第一障碍系数之间的通用常数；
- 投影到指定径向核方向的符号约定。

这些因素可改变数值和符号，但不会消除当前模式的局部曲率通道。

### 6.5 全 Green 算子与求和方式

完整结果还需包括所有允许的乘积 sectors、\(\lambda<0\) 模式以及核正交投影。Step 86 中简单写出的 \(\ell^{-3}\) 收敛说明没有计入本征空间维数及二阶 jet 的增长，不能据此推出逐项绝对收敛。不同节点之间可用离对角 Green 核或热核投影定义；同节点项需要先减去局部奇异部分再取正则值。

---

## 7. 对 Step 86 其余结论的影响

当前模式的特征值是 \(1\)，不是零模，所以它不改变此前对候选核模所得的
\[
\nu_l=0.
\]
正确解释仍是：奇异源与 \(\ker P\) 正交，因此核正交补上的 Green 解可以定义。它不意味着
\[
P\bar h=0
\]
在全局分布意义下成立；奇异 \(r^{-4}\) 多极场必然保留节点处的分布源。若全局分布意义下真有 \(P\bar h=0\)，椭圆正则性会使其成为光滑 orbifold 张量，与该奇异渐近矛盾。

综上，Step 87 对 Step 86 的修正是数学上实质性的：手征差确实能被真实、TT、低特征值的乘积本征张量看见。当前材料尚未给出完整 \(c_{\rm opp}-c_{\rm same}\) 的值或非零性，但“乘积因子化迫使所有手征 Green 响应逐模式消失”已经被这个明确模式排除。