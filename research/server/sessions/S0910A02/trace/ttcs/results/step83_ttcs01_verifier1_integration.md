# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 83,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step83_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step83_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Check the Step 83 theorem-grade audit of the fixed-A1 log-Weyl near-pinched construction for Yau--26. The central question is whether the claimed metrics on fixed A1 resolutions really satisfy ||Ric-sigma g||_op <= C/|log a| after raising an index in all three zones: EH core, log annulus, and ambient patching. Pay special attention to the sharp concern that the interpolated ambient quadratic jet may not be pure Weyl in all angular sectors at product nodes, that the Step 83 full Weyl-sector symbolic audit may or may not cover all relevant H_2 components and both chiralities, and that four-node patching/uniform constants must not hide an O(1) defect. Also check whether the note states the exact scope correctly: fixed representation/marking near-pinched input metrics only, not exact Einstein existence or nonexistence. Give a mathematical verification memo with any defects, missing hypotheses, or corrected theorem statement needed.

## Integrated Scientific Memo

# Step 83 数学核验备忘录

## 结论

Step 83 的三分区尺度账本基本正确；在补充若干关键假设并修正一处论证表述后，可支持如下结论：
\[
\left\|\Ric_{g_a}-\sigma g_a\right\|_{\mathrm{op},\infty;g_a}
\le \frac{C}{|\log a|}
\]
其中 \(M\) 是由**固定局部表示、固定端部标记和固定 EH 填充方向**得到的固定 \(A_1\) 光滑分辨，\(C\) 可依赖这些固定数据，但不依赖 \(a\)。

未发现 EH 核、对数环带、外部回接或四节点拼接中隐藏的 \(O(1)\) 算子缺陷。不过，现有定理表述应明确加入：

1. \(H_0\) 与 EH 远场二次项 \(H_1\) 必须写在**同一个径向正规规范**中；  
2. EH 线性修正需要有至二阶、实际最好逐阶的加权尾估计；  
3. 外部 \(O(r^4)\) 余项需要至二阶可微控制；  
4. 对数环带的任意截断公式应以解析推导证明，不能只靠三个单项式测试。

这些不是纯修辞条件：第一条正是保证 \(H_0-H_1\) 真为 Weyl 正规二次项的要点。

---

## 1. EH 核区：升指标后的尺度正确

令
\[
k=g_{\rm EH},\qquad
\widehat g_a=k+a^2\sigma\widetilde h,\qquad
G_a=a^2\widehat g_a,
\]
其中
\[
D\Ric_k(\widetilde h)=k,\qquad
|\nabla^j\widetilde h|_k\le C_j(1+\rho)^{2-j},\quad 0\le j\le2.
\]
在 \(\rho\le b/a=a^{-1/2}\) 上，
\[
a^2|\widetilde h|_k\le Ca,
\]
故 \(\widehat g_a\) 与 \(k\) 一致等价。Ricci 的二阶 Taylor 余项给
\[
|\Ric(G_a)-\sigma G_a|_k
\le Ca^4(1+\rho)^2.
\]
常数缩放不改变 \((0,2)\)-Ricci，但
\[
G_a^{-1}\simeq a^{-2}k^{-1},
\]
所以
\[
\left|G_a^{-1}\bigl(\Ric(G_a)-\sigma G_a\bigr)\right|
\le Ca^2(1+\rho)^2
=C(a^2+r^2),\qquad r=a\rho.
\]
在 \(r=b=a^{1/2}\) 处为 \(O(a)\)。

EH 尾部截断到 \(e+H_1\) 的二阶导数账本为
\[
O\!\left(b^2+a^4b^{-6}+a^4b^{-4}\right)
=O(a)+O(a)+O(a^2)=O(a).
\]
因此早期“缩放 Ricci-flat 核留下单位缺陷”的问题确由
\(D\Ric_k\widetilde h=k\) 消除。

`step68_qLambda_core_verify.json` 核对了 \(\widetilde h\) 的显式系数；完整逻辑仍依赖精确族
\(\Ric(q_\Lambda)=\Lambda q_\Lambda\)、规范自然性和上述尾估计。数据文件本身不是这些分析估计的替代。

---

## 2. 环带前提：相同 Ricci 收缩尚不足够

正规坐标中的二次度量项对应代数曲率张量：
\[
H_{ij}=-\frac13R_{ikjl}x^kx^l,
\qquad H(x,\cdot)=0.
\]
若 \(H_0,H_1\) 都处于这一共同径向正规规范，并满足
\[
D\Ric_eH_0=D\Ric_eH_1=\sigma e,
\]
则
\[
K=H_0-H_1
\]
对应一个 Ricci 收缩为零的代数曲率张量，因而是 Weyl 张量：
\[
K_{ij}=-\frac13C_{ikjl}x^kx^l.
\]
于是
\[
\tr K=0,\qquad \div K=0,\qquad
\Delta K=0,\qquad K(x,\cdot)=0.
\]

必须避免写成“两个任意二次张量的线性 Ricci 相同，所以差自动纯 Weyl”。若规范不同，差中可有纯微分同胚二次项。EH 侧减去
\[
V=\frac5{72}(r^3-r^{-1})\partial_r
\]
的 Lie 导数是负载步骤：它既不改变
\(D\Ric_{\rm EH}\widetilde h=g_{\rm EH}\)，又把远场项放进所需径向规范。

因此 Step 83 定理中的“same Ricci contraction”应改为“在固定端部标记下，二者已置于同一正规径向规范，并具有相同 Ricci 收缩”。对所给显式 \(H_*\)，条件确实成立；它并非仅由 Ricci 收缩等式自动推出。

---

## 3. 全 Weyl 扇区审计：十维覆盖成立，但脚本的作用应准确表述

四维 Weyl 空间为
\[
\mathcal W
=\Sym^2_0(\Lambda^+)\oplus\Sym^2_0(\Lambda^-),
\qquad \dim\mathcal W=5+5.
\]
脚本分别在 \(W^+\)、\(W^-\) 中使用两个对角和三个非对角无迹对称 \(3\times3\) 矩阵，确实给出每个手性块的五维基。它逐基元精确核验：
\[
\tr K=\div K=\Delta K=0,\quad K(x,\cdot)=0,\quad
D\Ric_eK=0,
\]
并核验 \(p=1,2,-1\) 时
\[
D\Ric_e(r^pK)
=-\frac{p^2+6p}{2r^2}r^pK.
\]
故审计不限于 \(U(2)\)-不变模式，也覆盖：

- 任意 \(W^+\) 分量；
- 任意 \(W^-\) 分量；
- 两种 EH 手性；
- 任意固定正交标记；若标记反转定向，只会交换两手性块；
- 产品节点处同时含两手性成分的任意线性组合。

脚本没有显式输出“十个张量线性无关”或代数 Bianchi 恒等式，但这些来自其
\(\Sym^2_0(\Lambda^\pm)\) 曲率算子构造。可将此作为短引理写入正式证明。

一处应修正的论证是：三个 \(p\) 值的单项式测试本身并不足以严谨推出任意光滑径向截断公式，除非先证明径向算子必具有预设的二阶 Euler 形式。直接解析推导如下。对任意径向 \(\eta(r)\)，由径向规范得
\[
\tr(\eta K)=0,\qquad \div(\eta K)=0,
\]
故
\[
D\Ric_e(\eta K)=-\frac12\Delta(\eta K).
\]
又因 \(K\) 调和且二次齐次，
\[
\Delta(\eta K)
=\left(\eta_{rr}+\frac7r\eta_r\right)K
=\frac{\eta_{tt}+6\eta_t}{r^2}K,\qquad t=\log r.
\]
所以
\[
D\Ric_e(\eta K)
=-\frac{\eta_{tt}+6\eta_t}{2r^2}K.
\]
取
\[
\eta(r)=\psi\!\left(\frac{\log(r/(4b))}{L}\right)
\]
即得 Step 83 所用公式。

---

## 4. 对数环带：算子误差为 \(O(L^{-1}+R^2)\)

在
\[
4b<r<R/2,\qquad g=e+q,\qquad q=H_1+\chi K
\]
上，有
\[
q=O(r^2),\quad
Dq=O\!\bigl(r(1+L^{-1})\bigr),\quad
D^2q=O(1+L^{-1}+L^{-2}).
\]
线性截断项满足
\[
D\Ric_e(\chi K)=O(L^{-1}),
\]
因为 \(K/r^2=O(1)\)。Ricci 非线性余项满足
\[
N_e(q)
=O\!\left(|q||D^2q|+|Dq|^2\right)
=O\!\left(r^2(1+L^{-1}+L^{-2})\right).
\]
另外目标项 \(-\sigma q\) 也是 \(O(r^2)\)。因 \(R\) 小时
\(g\simeq e\)，升指标不会引入退化因子，故
\[
\|\Ric_g-\sigma g\|_{\op,g}
\le C(L^{-1}+R^2).
\]
所有角向模式共享该估计，不存在某个未审计的 \(H_2\) 分量产生较大项。

---

## 5. 外部回接：\(A_1\) 偶性给 \(O(R^2)\)

在等变指数坐标中，局部群元精确为 \(x\mapsto-x\)，且
\[
(-I)^*g_0=g_0.
\]
因此度量分量为偶函数：
\[
g_0=e+H_0+E_4,\qquad
|\partial^jE_4|\le C_jr^{4-j},\quad 0\le j\le2.
\]
在 \(r\asymp R\) 上截断 \(E_4\) 时，最坏二阶项为
\[
R^{-2}O(R^4)=O(R^2).
\]
背景度量一致等价于 \(e\)，所以这也是升指标后的算子误差。

这里需要的是固定等变正规图及 \(C^2\) Taylor 余项，而不只是形式记号 \(O(r^4)\)。

---

## 6. 四节点拼接：没有相互作用型 \(O(1)\) 项

对固定有限节点集，先选固定等变正规图半径，小于节点最小距离的一半。因 \(R=a^{1/4}\to0\)，所有替换球最终两两不交。Ricci 是度量二阶局部算子，因此不同球中的修改没有交叉项；球外度量精确等于原 Einstein 轨形度量。

全局常数可取有限个局部常数的最大值，并允许依赖：

- 固定轨形及其有限阶曲率 jet；
- 各节点固定标记和 EH 手性；
- 固定截断函数；
- 固定节点数。

不得把该常数宣称为仅依赖维数，也不得让标记或截断族随 \(a\) 无控制变化。

取
\[
b=a^{1/2},\qquad R=a^{1/4},\qquad
L=\log \frac{R}{8b}
=\frac14|\log a|-\log 8,
\]
得到
\[
\delta_\sigma(g_a)
\le C\left(
a^2+b^2+a^4b^{-6}+a^4b^{-4}
+L^{-1}+R^2
\right)
\le C'\left(a+a^{1/2}+|\log a|^{-1}\right),
\]
从而
\[
\delta_\sigma(g_a)\le \frac{C''}{|\log a|}
\]
对充分小 \(a\) 成立。

---

## 7. 建议采用的修正版定理

> **固定标记 \(A_1\) 分辨的近 Einstein 定理。**  
> 设 \((\mathcal O^4,g_0)\) 是闭、定向 Einstein 轨形，
> \(\Ric(g_0)=\sigma g_0\)，仅有有限个孤立 \(A_1\) 点。每个节点固定一个等变正交正规图、一个 EH 填充手性及端部标记。假设相应 EH 线性修正 \(\widetilde h_i\) 光滑并满足
> \[
> D\Ric_{g_{\rm EH}}\widetilde h_i=g_{\rm EH},\qquad
> \widetilde h_i=H_{*,i}+O_2(\rho^{-2}),
> \]
> 且在该固定标记下 \(H_{*,i}\) 与环境正规二次项处于同一径向正规规范，
> \[
> H_{*,i}(x,\cdot)=0,\qquad D\Ric_eH_{*,i}=e.
> \]
> 令 \(M\) 为这些固定标记填充得到的固定光滑分辨。则存在
> \(a_0,C>0\) 及 \(M\) 上光滑度量 \(g_a\)，\(0<a<a_0\)，使
> \[
> \|\Ric_{g_a}-\sigma g_a\|_{\op,\infty;g_a}
> \le C|\log a|^{-1}.
> \]
> \(C\) 可依赖固定轨形、有限节点集、所有固定标记和截断轮廓，但不依赖 \(a\)。

对 \((S^2\times S^2)/\mathbb Z_2\)，\(\sigma=1\)。四个节点可独立选择固定手性；由独立的环面拓扑识别，这涵盖文稿列出的各固定光滑行。

---

## 8. 对 Yau–26 的准确范围

该结果只证明固定分辨上存在输入度量
\[
\|\Ric_{g_a}-g_a\|_{\op}\to0.
\]
它既不构造同一流形上的 Einstein 度量，也不排除任意
\(\lambda>0,\lambda=0,\lambda<0\) 的 Einstein 度量。因此目前不是 Yau–26 的反例。

还应避免更强的量词误读：即使日后证明某一产品分辨不承载任何 Einstein 度量，这个**正**近夹逼族只直接处理含正数的候选 Ricci 区间；它本身不能处理完全位于 \((-\infty,0]\) 的区间。完整否定原始“存在某一维数常数区间”的命题需要与该全称/存在量词相匹配的额外输入构造。

**最终审计意见：** Step 83 的核心数学结论可保留，但应把“共同径向正规规范”、加权尾估计和任意截断的解析公式写入正式证明；“同 Ricci 收缩自动纯 Weyl”以及“由三个单项式测试自动推出任意截断公式”的简写均应删除。