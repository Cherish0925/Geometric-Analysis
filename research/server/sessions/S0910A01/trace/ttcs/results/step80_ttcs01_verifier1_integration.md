# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 80,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step80_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step80_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the J-symmetry all-order obstruction elimination theorem for the product orbifold (S²×S²)/⟨(r_π,r_π)⟩ with EH insertion direction ω₂. The claim is: simultaneous complex conjugation J(z,w)=(z̄,w̄) acts on the SD/ASD basis at each node as diag(-1,+1,-1), fixes ω₂ (the insertion direction), and therefore a J-equivariant Eguchi-Hanson construction has zero obstruction projections onto the J-odd directions (ω₁ and ω₃) at EVERY order of the Ozuch expansion. Combined with A-symmetry (killing scalar kernel ν_l) and the rank-one determinant (μ₁=0), this eliminates all finite-dimensional Ozuch obstructions. Check: (1) Is the J-parity argument mathematically rigorous? (2) Does J genuinely extend as an isometry of the EH metric when the insertion direction is ω₂? (3) Is the 'every order' claim correct, or could higher-order gauge/normalization issues break J-invariance? (4) Is the surviving system really balanced (2 equations in 2 unknowns)? (5) What is the strongest statement about existence that this structural result supports, and what analytical gaps remain?

## Integrated Scientific Memo

# 核验结论

该 \(J\)-对称性论证的核心是正确的，但 Step 80 的总括结论过强。准确结论是：

> 在严格 \(J\)-等变的 Eguchi–Hanson 拼接中，插入方向取 \(J\)-不变的 \(\omega _2\) 时，所有对应于 \(\omega _1,\omega _3\) 的 \(J\)-奇障碍投影恒等为零；因此，只要相应渐近展开被构造出来，其每一阶系数都为零。  
> \(A\)-对称性同时消去四个 \(A\)-奇的全局标量核投影，而秩一曲率的行列式公式仅消去当前已知二阶径向系数 \(\mu _1\)。它并不消去更高阶的 \(J\)-偶径向障碍。

所以，“横向障碍全阶消失”成立；“全部有限维障碍全阶消失”不成立。

---

## 1. \(J\) 在 \(\Lambda^\pm\) 上的作用

在每个节点取相容的定向正交积框架
\[
(e^1,e^2,e^3,e^4),\qquad
dJ=\operatorname{diag}(1,-1,1,-1).
\]
于是 \(\det dJ=1\)，故 \(J\) 分别保持 \(\Lambda^+\) 和 \(\Lambda^-\)。采用标准基
\[
\begin{aligned}
\omega_1^\pm&=\frac1{\sqrt2}(e^{12}\pm e^{34}),\\
\omega_2^\pm&=\frac1{\sqrt2}(e^{13}\mp e^{24}),\\
\omega_3^\pm&=\frac1{\sqrt2}(e^{14}\pm e^{23}),
\end{aligned}
\]
直接得到
\[
J^*|_{\Lambda^+}=J^*|_{\Lambda^-}
=\operatorname{diag}(-1,+1,-1).
\]
因此 \(\omega _2\) 为偶，\(\omega _1,\omega _3\) 为奇。这个结论是精确线性代数，不依赖数值采样。

节点间的基必须用全局相容方式运输；内禀地说，每个 \(\Lambda^\pm\) 中 \(J\) 的 \(+1\) 特征空间是一维，所谓 \(\omega _2\) 应定义为该直线。又因 \(J\) 与局部群 \(\{\pm I\}\) 及全局商作用 \(\sigma\) 对易，它确实下降为商 orbifold 的等距变换。

Step 79 所强调的角变量 \(\rho_x\) 不会破坏该结论。对 \(\zeta=\omega _2\)，
\[
\rho_{Jx}(\omega _2)_j=\varepsilon_j\rho_x(\omega _2)_j,
\qquad \varepsilon=(-1,+1,-1),
\]
而
\[
H^4(\omega _2)
=-\frac1{2r^4}\sum_j \rho_x(\omega _2)_j\,
(\omega_j^-\circ\omega_2^+)
\]
的每项获得两次同样的符号，故 \(J^*H^4=H^4\)。这与 Step 79 对“冻结 \(\rho\)”的纠正完全相容：这里使用的是完整的 \(x\)-依赖协变性，而不是错误的固定向量代换。

---

## 2. \(J\) 是否真能延拓为 EH 等距变换

可以，但必须相对于由插入方向 \(\omega _2\) 选出的 EH 复结构陈述，而不是相对于原来的乘积复结构。

令 \(I_2\) 由
\[
g_{\mathrm e}(I_2X,Y)=\omega_2(X,Y)
\]
定义。由于 \(dJ\) 正交且 \(J^*\omega _2=\omega _2\)，有
\[
dJ\,I_2=I_2\,dJ.
\]
所以 \(J\) 对 \(I_2\) 是复线性的。可取 \(I_2\)-复坐标
\[
\xi_1=x_1+i x_3,\qquad \xi_2=x_2-i x_4,
\]
其中
\[
J(\xi_1,\xi_2)=(\xi_1,-\xi_2).
\]
因此 \(J\in U(2,I_2)\)，与中心 \(\{\pm1\}\) 对易，并作用于
\(\mathbb C^2/\{\pm1\}\)。标准 EH 度量在固定尺度下具有这一酉对称性；该作用提升到最小解消，保持例外球及其 Kähler 类，故给出精确 EH 等距变换。对使用 \(\Lambda^-\) 的节点同理，只需采用相反环境定向的对应解释。

因此 EH 延拓没有几何缺陷。需要注意：

* 相对于原乘积复结构，同时复共轭是反全纯的；这不是这里使用的复结构。
* \(J\)-等变性把核平面
  \(\operatorname{span}\{\omega _2,\omega _3\}\)
  中的连续角度固定到 \(J\)-偶直线 \(\mathbb R\omega _2\)；一般的 \(\omega _2+\alpha\omega _3\) 插入不保持 \(J\)。

---

## 3. 全阶奇投影消失是否严格

设 \(\mathcal E(g)\) 是 Einstein–DeTurck 残差，参考度量也取 \(J\)-不变。由自然性，
\[
J^*\mathcal E(g)=\mathcal E(J^*g).
\]
若拼接度量 \(g_t\) 精确 \(J\)-不变，则
\[
J^*\mathcal E(g_t)=\mathcal E(g_t).
\]

尚需补上 Step 80 简略证明中隐含的核张量协变性。若
\(\mathbf o_v\) 是由插入数据方向 \(v\) 产生的 EH 核/余核张量，则
\[
J^*\mathbf o_v=\mathbf o_{J^*v}.
\]
这可由
\[
J^*g_{\rm EH}(\phi)=g_{\rm EH}(J^*\phi)
\]
在 \(\phi=\omega _2\) 处微分得到。于是适应基
\[
(\phi_{(1)},\phi_{(2)},\phi_{(3)})
=(\omega _2,\omega _1,\omega _3)
\]
的奇偶性为
\[
(+1,-1,-1).
\]

因此完整投影
\[
C_v(t)=\int \langle\mathcal E(g_t),\mathbf o_v\rangle\,dV
\]
满足
\[
C_v(t)=C_{J^*v}(t).
\]
若 \(J^*v=-v\)，则
\[
C_v(t)=-C_v(t)=0.
\]
故
\[
C_{\omega _1}(t)\equiv C_{\omega _3}(t)\equiv0.
\]

这是完整非线性投影的恒等消失，而不只是 \(\mu _2,\mu _3\) 的二阶消失。因此，在任何已经建立的幂级数或多齐次展开中，这两个投影的每一阶系数都为零。

### 规范和归一化不会产生真实破坏

只要以下数据均等变：

* orbifold/EH 坐标图；
* 径向截断函数；
* DeTurck 参考度量；
* 线性修正及核—余核分解；
* 模态归一化，

则规范固定与 Lyapunov–Schmidt 修正均保持 \(J\)-不变。有限群平均
\[
u\longmapsto \tfrac12(u+J^*u)
\]
可将线性选择强制置于不变子空间，且奇偶子空间正交。非等变坐标或规范可能产生表面上的奇系数，但那不是不变量意义下的障碍投影。

准确措辞应是：

> 对每个实际构造出的 Ozuch 阶数，奇投影为零。

对称性本身不构造尚未证明存在的无限渐近展开，因此不应把它描述成一个独立的“无限阶 Ozuch 展开存在定理”。

---

## 4. \(A+J+\det\) 到底消去了什么

在
\[
R^\pm=\operatorname{diag}(1,0,0),\qquad \phi_0=\omega _2
\]
时：

1. \(\phi_0\in\ker R^\pm\)，故一阶局部障碍
   \(\lambda(\phi_0)=0\)；
2. \(J\)-对称性给出所有阶的
   \[
   C_{\omega_1}=C_{\omega_3}=0,
   \]
   特别是 \(\mu _2=\mu _3=0\)；
3. 秩一曲率的行列式公式给出当前二阶径向系数
   \[
   \mu _1=0;
   \]
4. \(A\)-奇偶性消去四个
   \[
   u_i g_j
   \]
   对应的 \(\nu_l\) 投影。

所以 Ozuch 当前给出的
\[
t_j\lambda_k^j+t_j^2\mu_k^j
=O(t_{\max}^{5/2}),\qquad
\nu_l=O(t_{\max}^{5/2})
\]
中显式出现的系数均被消去。

但 \(\omega _2\) 径向模态是 \(J\)-偶的；行列式公式只证明其二阶系数 \(\mu _1\) 为零，并不约束三阶及以后自响应、节点间 Green 相互作用、规范响应或非线性响应。因此以下说法必须撤回：

* “所有有限维 Ozuch 障碍全阶消失”；
* “不存在剩余有限维方程”。

Step 80 §7 所保留的径向系统才是与对称性相容的结论。

此外，
\[
g_1-g_2
\]
同时为 \(A\)-偶和 \(J\)-偶，且线性算子特征值为 \(-\Lambda\)。它不是核，因而通常不增加障碍方程，但使不变补空间上的算子成为不定算子；不能再声称该补空间上的二次型正定。需要的是一致可逆性，而非正性。

---

## 5. 剩余系统是否真是 \(2\times2\)

在固定 Einstein 归一化、没有遗漏额外可积 orbifold 变形参数的前提下，维数计数是合理的：

* 四个节点各剩一个 \(J\)-偶径向投影；
* \(A\) 将
  \[
  (N,N)\leftrightarrow(S,S),\qquad
  (N,S)\leftrightarrow(S,N),
  \]
  因而只剩两个独立方程；
* \(A\)-等变尺度也只剩每个节点轨道一个，即
  \[
  (t_1,t_2).
  \]

因此预期完整约化映射为
\[
(F_1,F_2):(t_1,t_2)\longmapsto\mathbb R^2.
\]

但这个结论仍是有条件的 Lyapunov–Schmidt 计数，尚需核实：

1. 是否存在未枚举的 \(A,J\)-不变全局可积变形 \(v\)；
2. Einstein 常数或整体尺度是否已通过归一化正确剔除；
3. 线性补空间是否一致可逆，从而确实只留下这两个余核坐标。

Step 80 关于单方程约化的理由错误：\(A\) 只在两个轨道内部交换节点，并不交换两个轨道。因此它既不推出 \(F_1=F_2\)，也不推出 \(t_1=t_2\)。

单因子反足或类似的定向反转等距变换可能交换两个轨道并同时交换 \(\Lambda^+\) 与 \(\Lambda^-\)，这与两轨道的相反手征性有潜在相容性；但其 EH 提升及与 \(J,\sigma\) 的相容性尚未验证。没有该额外对称性时，应保留完整 \(2\times2\) 系统。

而“方程数等于未知数数”本身没有存在性意义。若首个非零项为
\[
F_i(t)=t_i\sum_j B_{ij}t_j^2+\cdots,
\]
则对 \(t_i>0\)，首阶条件是
\[
B
\begin{pmatrix}t_1^2\\t_2^2\end{pmatrix}=0.
\]
若 \(B\) 可逆，唯一小解仍是退化点 \(t_1=t_2=0\)；只有适当的退化性和符号结构才可能产生正尺度分支。现有 \(O(t^{5/2})\) 余项也不足以证明首个非零径向项严格为纯三次项；还需精细展开以排除其他幂次或对数项。

---

## 6. 最强存在性结论与缺口

目前最强且严格支持的陈述是：

> 对该乘积 orbifold，取 \(\omega _2\) 插入并实施精确 \(A,J\)-等变 EH 拼接后，所有 \(J\)-奇横向泡障碍和所有 \(A\)-奇全局标量核障碍恒等消失；秩一行列式公式又使已知二阶径向障碍消失。因此当前已解析到的 Ozuch 局部必要条件不排除该正 Einstein 解消。

这只是一个强的表示论约化，不是 Einstein 度量存在定理。仍需完成：

1. **全局等变拼接：** 在四个 EH 片上构造彼此兼容的 \(A,J\) 提升及精确等变近似度量。
2. **完整不变切片与参数审计：** 枚举所有 \(A,J\)-不变核、余核、可积变形、尺度和 Einstein 归一化参数。
3. **一致线性逆估计：** 控制颈部小特征值、微分同胚模态以及 \(-\Lambda\) 的 shape 模态；这里不能依赖正定性。
4. **计算剩余径向约化映射：** 包括局部自响应、节点间乘积 Green 相互作用、偶标量 shape 响应、规范修正和非线性项。
5. **求得正尺度零点：** 证明 \(F_1=F_2=0\) 有 \(t_1,t_2>0\) 的小解，并给出足够的非退化性或其他分支机制。
6. **加权椭圆与非线性闭合：** 建立 Schauder/Hölder 估计及压缩映射或隐函数定理。

因此该结构结果至多表明：该 orbifold 解消通过了目前可见的二阶障碍检验，并把未知内容压缩到两个 \(J\)-偶径向方程及相应分析问题。它尚不能推出 \(\#_3(S^2\times S^2)\) 上存在正 Einstein 度量，更不能对完整的 Yau 第 26 题作出结论。