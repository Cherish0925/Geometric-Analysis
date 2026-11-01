# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 66,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step66_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step66_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step-66 mathematical/computational conclusions about the Eguchi-Hanson correction export for the Yau-26 positive-branch experiment. Read the supplied note/data. Check specifically: (1) whether the Kähler-potential identity and its limitation by the EH bolt cohomology/obstruction term are stated correctly in the session conventions; (2) whether the solver-agnostic operator-norm audit results justify decoupling the refined small-defect certificate from BVP convergence and from the naive-start flow experiment; (3) whether the ODE compatibility extraction (rank-two highest-derivative system plus lower-order constraint) is a legitimate correction to the Step-65 handoff; (4) whether the LS-profile and nonlinear audit should be interpreted only as diagnostic, not as a near-pinched metric certificate; and (5) what concrete mathematical/computational next step would most reduce uncertainty without overclaiming. Please identify any sign/factor/cohomology/gauge caveats that could materially change the next work.

## Integrated Scientific Memo

# Step-66 核验结论

## 总结

Step-66 的主要计算结论成立：

1. 径向 Kähler 势恒等式在本会话归一化下正确，但只能局部化简，不能跨越 bolt 的全局上同调障碍。
2. 直接 Ricci 端态算子范数审计确实应与 BVP 收敛、以及朴素初值流实验分离。
3. 最高阶系统确为秩二并带一条低阶相容约束；但“通过选择 \(f_1'\) 传播约束”不正确，剩余自由度必须用规范条件固定。
4. 标量截断与 LS profile 只能作为诊断，均未给出近夹逼度量。
5. 当前最能降低不确定性的工作不是继续调 LS/BVP，而是先求真实 ambient 二次 jet \(H\)，完成 EH 复方向下的曲率、规范和角模态分解。

另有两项必须修正文案：

- Biquard 的 \(o_j\) 是 EH 上全局光滑、\(L^2\)、按 \(r^{-4}\) 衰减的核张量；紧支撑的是拼接后的 \(\chi_t o_j\)，不是 \(o_j\) 本身。
- 原文方程是
  \[
  d_{eh}\operatorname{Ric}(h)=\Lambda eh+\sum_{j=1}^3\lambda_j o_j,
  \]
  不是 \(\frac13\sum_j\lambda_j o_j\)。PDF 提取把求和下标 \(1\) 与上标 \(3\) 排成了类似分数。虽然常数可吸收入 \(\lambda_j\)，但归一化必须统一。

---

## 1. Kähler 势恒等式及其全局限制

在 Step-65/66 约定中
\[
g_{EH}=W^{-1}dr^2+\frac{r^2}{4}
 (\sigma_1^2+\sigma_2^2+W\sigma_3^2),\qquad W=1-r^{-4},
\]
且径向 \(\phi\)、\(q=\phi'\) 给出
\[
h_\phi=A_\phi(e_0^2+e_3^2)+B_\phi(e_1^2+e_2^2),
\]
其中
\[
A_\phi=\frac{r(r^4-1)q'+(r^4+3)q}{r^5},\qquad
B_\phi=\frac{2(r^4-1)q}{r^5}.
\]

精确符号代入对任意函数 \(q(r)\) 验证了
\[
d\operatorname{Ric}_{EH}(h_\phi)
=-\frac12\,i\partial\bar\partial(A_\phi+B_\phi).
\]
JSON 中只有因子 \(-1/2\) 使三个独立框架分量恒等为零，因此这不是数值拟合。注意 \(A+B\) 是复迹；实迹为 \(2(A+B)\)。从其他文献导入公式时，必须统一 \(i\partial\bar\partial\)、Ricci 符号和实/复迹的二倍归一化。

对 \(\phi=r^2\)，
\[
A_\phi=4+4r^{-4},\qquad B_\phi=4-4r^{-4},
\]
故本会话中
\[
i\partial\bar\partial(r^2)
=4\omega+4r^{-4}(e_0\wedge e_3-e_1\wedge e_2),
\]
而不是 \(2\omega\)；甚至在无穷远其主项也是 \(4\omega\)。

在去掉 bolt 的端部，
\[
q=\frac{2r^5}{r^4-1},\qquad
\phi=r^2+\frac12\log\frac{r^2-1}{r^2+1}
\]
满足 \(A_\phi=B_\phi=4\)，即
\[
i\partial\bar\partial\phi=4\omega.
\]
但 \(\phi\) 在 \(r=1\) 对数奇异。由于
\[
\int_{S^2_{\rm bolt}}\omega\neq0,
\]
而光滑全局标量的 \(i\partial\bar\partial\) 在 bolt 上积分为零，\(\omega\) 不可能有光滑全局标量势。因此纯 Kähler 势 ansatz 不能全局光滑地求解
\[
-\tfrac12 i\partial\bar\partial S=\Lambda\omega,\qquad \Lambda\ne0.
\]

应避免把这一事实与 Biquard 的整个三维 Fredholm 障碍空间逐字等同。标量论证直接看到的是固定复结构下的 Kähler 类；Biquard 的
\[
o_j(x,y)=\Omega(I_jx,y)
\]
由一个反自对偶 \(L^2\) 谐和二形式 \(\Omega\) 和三个超 Kähler 复结构生成，是对称张量算子的三维核/余核。二者都源于 EH 核心拓扑，但标量通道只解释其中一个受限机制，不能覆盖非 Kähler、复结构变化或一般角向模态。

---

## 2. 算子范数审计与流实验可以且必须解耦

对任意已组装候选 \(h\)，直接计算
\[
d\operatorname{Ric}_{EH}(h)-\Lambda g_{EH}
\]
不依赖产生 \(h\) 的 BVP 求解器是否报告收敛。对于物理缩放
\[
g_\varepsilon=\varepsilon\widehat g_\varepsilon,\qquad
\widehat g_\varepsilon=eh+\varepsilon h,
\]
相应端态残差为
\[
E_\varepsilon
=g_\varepsilon^{-1}
(\operatorname{Ric}_{g_\varepsilon}-\Lambda g_\varepsilon)
=\varepsilon^{-1}\widehat g_\varepsilon^{-1}
 \operatorname{Ric}_{\widehat g_\varepsilon}-\Lambda I,
\]
固定 \(r\) 展开为
\[
E_\varepsilon
=eh^{-1}\!\left(d\operatorname{Ric}_{EH}(h)-\Lambda eh\right)
+O(\varepsilon).
\]
所以候选生成、线性残差审计和非线性物理缩放审计是三个逻辑上不同的步骤。

数据一致地显示：

- raw EH：缺陷恒为 \(1\)，因为 \(\operatorname{Ric}_{EH}=0\)；
- \(h=4eh\)：线性化 Ricci 为零，缺陷仍为 \(1\)；
- \(h=r^2eh\)：线性最大缺陷约 \(8.92\)，确认不能用 Lichnerowicz 项替代完整 \(d\operatorname{Ric}\)；
- 标量截断：远离截断处中位残差约 \(3\times10^{-6}\)，但全区最大值为 \(5\)–\(12\)，故只消除了端部源项，没有得到全局小算子范数。

非线性径向审计也显示 raw 缺陷随 \(\varepsilon\to0\) 仍为 \(1\)，而标量截断的核心最大值保持 \(O(1)\)–\(O(10)\)。因此当前没有 refined small-defect certificate，更没有多 bubble 的全局近夹逼证书。

另一方面，Biquard 的朴素拼接在小 \(t\) 时是光滑正定度量，可以独立作为 Einstein–DeTurck 或变分搜索初值；初值不必近 Einstein。其失败不能证明流形不承载其他 Einstein 度量。若流达到定态，还须分别审计 DeTurck 向量和
\(\operatorname{Ric}-\lambda g\)，以排除非 Einstein soliton。已知正 KE 的控制行仍是解释算法行为所必需的对照，但与近夹逼认证无逻辑依赖。

---

## 3. ODE 提取是对 Step-65 的合法修正，但传播解释需更正

以最高阶未知量
\[
(f_1',f_2'',f_3'')
\]
组成的系数矩阵在 \(r>1\) 确实满足
\[
\operatorname{rank}M=2,\qquad (-1,2,1)M=0.
\]
于是源项与低阶数据必须满足
\[
\begin{aligned}
C={}&\Lambda r^6-(3r^4+1)f_1
 +2(r^4+1)f_2+2r^5f_2'\\
& +(r^4-1)f_3+r(r^4-1)f_3'=0.
\end{aligned}
\]
这比“任意两条二阶方程加一条独立一阶演化方程”更准确：它是未固定规范的线性化 Ricci 系统中的相容关系。

但 Step-66 文案所说“选择 \(f_1'\) 以保持约束传播”不成立。把数据中的 \(f_2'',f_3''\) 代入 \(C'\) 可化简为
\[
C'=-\frac{4}{r(r^4-1)}C.
\]
因此若某一截面上 \(C=0\)，两条二阶方程自动保持它；\(f_1'\) 完全消去。剩余自由度是径向微分同胚规范，应通过 Bianchi 规范或等价规范方程固定，而不是由相容式确定。

按
\[
Bh=\delta h+\frac12d\,\operatorname{tr}h,\qquad
\delta=-\operatorname{tr}\nabla
\]
的约定，径向对角 ansatz 的 Bianchi 条件可写为
\[
-\frac12 f_1'+f_2'+\frac12f_3'
-\frac{2}{r}(f_1-f_2)
-\frac{r^4+1}{r(r^4-1)}(f_1-f_3)=0.
\]
这才关闭 \(f_1'\) 自由度。若改用不同的 divergence 符号，该式整体符号或部分项会变化，必须用纯规范制造解
\[
h=\mathcal L_Xeh,\qquad d\operatorname{Ric}(h)=0
\]
校准。

在 \(r=1\) 处矩阵秩进一步下降，裸 \(r\) 坐标奇异。令 proper distance 为 \(s\)，则
\[
r-1\sim s^2.
\]
光滑性要求系数为 \(s^2\) 的光滑函数，并至少有
\[
f_1(1)=f_3(1),\qquad f_1-f_3=O(r-1),
\]
而不是简单对三个 \(f_i\) 施加任意 Neumann 条件。应在 \(s\) 坐标中做 Frobenius 展开。

还需警惕：三函数 \(U(2)\)-不变 ansatz 未必能匹配真实 ambient \(H\)。即使选择 EH Kähler 方向落入 \(\ker R^\pm\) 消去首阶 obstruction，ambient 曲率的另一半自对偶/反自对偶块仍可能含非 \(U(2)\)-不变角模态。若有这些模态，正确问题是有限张量球谐模态的耦合径向系统，而不是当前三函数 BVP。

---

## 4. LS profile 只能作诊断

LSQR 数据具有以下决定性问题：

- 达到 \(20000\) 次迭代上限；
- 估计条件数约 \(1.0\times10^7\)；
- 虽然内部线性残差中位数约 \(5\times10^{-4}\)，全区最大值约 \(4.7\times10^3\)；
- bolt 条件只是启发式边界惩罚，不是 Frobenius 光滑条件；
- 外端未匹配真实 ambient \(H\)。

非线性审计中，在 \(r>1.2\) 后最大残差仍约
\[
0.688,\ 0.667,\ 0.652,\ 0.646
\]
而没有随 \(\varepsilon\to0\) 消失；全区最大值约 \(19\)–\(20\)。\(\varepsilon=10^{-4}\) 时自然截断半径超过 profile 数据上限，外插又产生约 \(10^4\) 的伪峰。小中位数和采样正定性均不能替代上确界算子范数控制。

故 LS profile、标量 cutoff 及现有非线性审计只能验证软件接口能发现局部成功和边界失败，不能作为近夹逼度量、Biquard \(h\)、多 bubble 证书或 Yau-26 证据。

---

## 5. 最能减少不确定性的下一数学对象

应先精确求实际 orbifold 奇点处的二次 jet：
\[
H_{ij}(x)=-\frac13R_{ikjl}(p_0)x^kx^l
\]
（该式依赖 Riemann 符号约定，必须与 Biquard 的曲率约定核对），然后依次完成：

1. 将 EH Kähler 方向旋转到候选 \(\ker R^+\) 或 \(\ker R^-\)；
2. 用齐次三次向量场把 \(H\) 放入欧氏 Bianchi 规范；
3. 计算 Biquard 条件
   \[
   R^\pm(H)(I_1)=0
   \]
   及对应 \(\lambda_j\)；
4. 将 \(H\) 分解成 \(U(2)\)-径向与非径向张量谐波，判断三函数系统是否覆盖真实边界数据；
5. 仅对实际出现的模态，在 proper-distance/Frobenius 坐标和 Bianchi 规范中建立 BVP。

实现时应加入三项精确回归测试：

\[
d\operatorname{Ric}(\mathcal L_Xeh)=0,
\]
\[
d\operatorname{Ric}(k_i)=o_i
\quad\text{（Biquard Proposition 1.1 的显式 }k_i\text{）},
\]
以及
\[
C'=-\frac{4}{r(r^4-1)}C.
\]
它们能同时核对 Ricci 符号、\(-\tfrac12\) 因子、Bianchi 规范、obstruction 归一化和约束传播。

最后，Biquard 的实际 Einstein 存在定理依赖非紧 AH 情形中改变 conformal infinity 来消除剩余障碍；闭流形只有近似拼接及部分必要性结论直接保留。即使最终获得小残差闭度量，也不能据此自动推出闭 Einstein 度量存在。反向上，小残差或某次流失败同样不能证明闭流形不存在任何 Einstein 度量。