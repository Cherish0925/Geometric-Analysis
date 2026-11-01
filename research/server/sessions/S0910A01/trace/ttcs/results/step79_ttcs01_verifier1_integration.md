# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 79,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step79_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step79_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 79 mathematical repair of the positive mixed-row product-orbifold obstruction problem. Read the repair note plus the two data files and the relevant Ozuch source excerpts. Check: (1) whether Ozuch's rho_x dependence invalidates the Step 78 fixed-rho rank-one/block-diagonal conclusions; (2) whether the factor-traceless bare scalar-decoupling theorem survives for zeta in span{omega2,omega3}; (3) whether the tilt linearization D_phi lambda=(0,c Lambda a,0) at phi0=omega2 is correctly interpreted as making mu2 adjustable and leaving the cokernel component as the actual second-order local condition; (4) whether the response to A02's r=0 KE-control argument is mathematically sound or too strong. Give a direct scientific memo with corrections and next computation priorities.

## Integrated Scientific Memo

## Step 79 核验备忘录

### 结论

Step 79 的核心修复成立：

1. Ozuch 的 \(\rho_x\) 是随边界角变量 \(x\) 变化的旋转，故 Step 78 的固定-\(\rho\) 核归属、秩一/固定块对角结论无效。
2. 对
   \[
   \zeta^+\in\operatorname{span}\{\omega_2^+,\omega_3^+\},
   \]
   裸 \(H^4\) 的逐因子无迹性严格保留。
3. 在 \(\phi_0=\omega_2\) 处，
   \[
   D_\phi\lambda(a,b)=(0,c\Lambda a,0)
   \]
   的解释正确：\(\mu_2\) 可由 \(O(t)\) 的出核倾斜吸收；完整余核是 \(k=1,3\)，而此秩一乘积块上 \(\mu_1=0\)，所以仅剩 \(k=3\) 的局部二阶兼容条件。
4. 对 A02 的 \(r=0\) Kähler–Einstein 控制论证的反驳方向正确：精确 KE 族一般只迫使 \(\mu\) 在所有一阶可调参数导数像空间的商中消失，不能直接推出各 \(\mu_k\) 分量都为零。

但应加入两项关键修正：

- 商空间应使用所有 \(O(t)\) 可动参数的全导数
  \[
  D_{(\phi,v,\ldots)}\lambda,
  \]
  不仅是 \(D_\phi\lambda\)。
- 吸收 \(\mu_2\) 所需的出核倾斜会重新引入裸张量对 \(g_1-g_2\) 形状标量模的耦合；因此“裸标量解耦”和“倾斜消障”不能分开处理。

---

### 1. \(\rho_x\) 确实推翻 Step 78 的固定块结论

Ozuch Definition 1.14 给出
\[
\rho_x(\zeta)_j
=\frac{x^T(\zeta^+\circ\omega_j^-)x}{|x|^2},
\]
Remark 1.15 将其识别为单位四元数共轭。因此固定 \(\zeta\neq0\) 时，
\[
x\longmapsto \rho_x(\zeta)
\]
扫过半径 \(|\zeta|\) 的整个 \(S^2\)，而不是固定向量或固定在 \(\ker R^-\) 中。

当
\[
R^-=\operatorname{diag}(\Lambda,0,0)
\]
时，
\[
R^-\rho_x(\zeta)=\Lambda\rho_1(x,\zeta)e_1,
\]
一般非零。又由 Proposition 1.16，
\[
d_eR^-(H^4)
=\frac{12}{r^6}
\left(\rho_x\rho_x^T-\frac{|\zeta|^2}{3}I\right),
\]
故
\[
(d_eR^-)_{12}=\frac{12\rho_1\rho_2}{r^6},\qquad
(d_eR^-)_{13}=\frac{12\rho_1\rho_3}{r^6},
\]
一般亦非零。

数据中的显式点
\[
x=(0.4,0.8,-0.4,0.2),\qquad
\rho_x(\omega_2)=(0.48,0.36,0.8)
\]
直接给出
\[
R^-\rho_x=(0.48\Lambda,0,0),
\]
以及 \(r=1\) 时
\[
(d_eR^-)_{12}=2.0736,\qquad
(d_eR^-)_{13}=4.608.
\]

因此 Step 78 的以下推论均须撤回：

- 在固定乘积标架中令 \(\rho=(0,\cos\alpha,\sin\alpha)\)；
- 由 \(\zeta\in\ker R^-\) 推出 \(R^-\rho_x(\zeta)=0\)；
- 推出 \(d_eR^-(H^4)\) 固定块对角；
- 进而断言完整二阶障碍消失。

这只是消除了一个错误简化；局部障碍是积分投影量，点态非零本身还不计算 \(\mu_k\)。

另有一处来源转录警告：文档中
\[
\rho_{-x}=\rho_x^T=\rho_x^{-1}=\rho_x
\]
不可能对一般旋转逐字成立。正确的四元数关系应是
\[
\rho_{-x}=\rho_x,\qquad
\rho_{\bar x}=\rho_x^{-1}=\rho_x^T
\]
（单位四元数）。后续交换节点或相互作用点时不能使用错误转录式。

---

### 2. 裸 \(H^4\) 的逐因子无迹定理成立

令两个乘积因子的切平面为
\[
E=\operatorname{span}\{e_1,e_2\},\qquad
F=\operatorname{span}\{e_3,e_4\}.
\]
JSON 中六个基乘积严格验证
\[
\operatorname{tr}_{E}(\eta^-\circ\zeta^+)
=
\operatorname{tr}_{F}(\eta^-\circ\zeta^+)=0
\]
对任意
\[
\eta^-\in\Lambda^-,
\qquad
\zeta^+\in\operatorname{span}\{\omega_2^+,\omega_3^+\}
\]
成立。由双线性，这不是数值现象而是精确代数恒等式。

取 \(\eta^-=\rho_x(\zeta)^-\)，得到
\[
H^4(\zeta^+)
=-\frac{\rho_x(\zeta)^-\circ\zeta^+}{2r^4}
\]
满足
\[
\operatorname{tr}_{g_1}H^4
=\operatorname{tr}_{g_2}H^4=0
\]
逐点成立，故对任意函数 \(f\),
\[
\langle H^4,fg_1\rangle
=\langle H^4,fg_2\rangle=0.
\]

但结论仅限于未倾斜、未修正的裸 \(H^4\)。它不推出下列对象无标量分量：

- 截断及 Bianchi 修正项；
- \(Q^{(2)}\) 等非线性源；
- 全局 Green 响应；
- \(P\)-伪逆经过偶标量模或 \(g_1-g_2\) 负模后的响应。

尤其，若为吸收 \(\mu_2\) 而令
\[
\phi(t)=\omega_2+t\,a\omega_1+\cdots,
\]
则 \(H^4\) 获得 \(O(t)\) 的 \(\omega_1^+\) 分量；而例如
\[
\omega_1^+\circ\omega_1^-
=\operatorname{diag}(-1,-1,1,1)
\]
具有非零逐因子迹。因此必需的倾斜会在下一阶重新耦合 \(g_1-g_2\) 形状模。

---

### 3. 倾斜线性化及余核解释正确

在
\[
R=\operatorname{diag}(\Lambda,0,0),\qquad
\phi_0=\omega_2
\]
处，采用适配标架
\[
(\phi_{(1)},\phi_{(2)},\phi_{(3)})
=(\omega_2,\omega_1,\omega_3)
\]
并令
\[
\phi(\varepsilon)
=\frac{\omega_2+\varepsilon(a\omega_1+b\omega_3)}
{\sqrt{1+\varepsilon^2(a^2+b^2)}}.
\]
由 Ozuch
\[
\lambda_k=c\langle R\phi,\phi_{(k)}\rangle
\]
得到
\[
\lambda_1=c\Lambda a^2\varepsilon^2+O(\varepsilon^4),
\]
\[
\lambda_2
=c\Lambda a\varepsilon
-c\Lambda\left(a^3+\frac12ab^2\right)\varepsilon^3
+O(\varepsilon^4),
\]
\[
\lambda_3=0
\]
（在所选平滑适配标架下）。因此
\[
D_\phi\lambda_{\phi_0}(a,b)
=(0,c\Lambda a,0).
\]

若
\[
\phi(t)=\phi_0+t(a\omega_1+b\omega_3)+o(t),
\]
则
\[
t\lambda(\phi(t))+t^2\mu(\phi(t))
=t^2\bigl(D_\phi\lambda(a,b)+\mu(\phi_0)\bigr)+o(t^2).
\]
所以
\[
a=-\frac{\mu_2}{c\Lambda}
\]
可消去 \(k=2\) 分量，而 \(b\) 是核圆内转动，对一阶 \(\lambda\) 不可见。

严格说，
\[
\operatorname{coker}D_\phi\lambda
=\operatorname{span}\{e_{(1)},e_{(3)}\}.
\]
在当前秩一块上，\(\phi_0^\perp\) 中的曲率块为
\[
\begin{pmatrix}\Lambda&0\\0&0\end{pmatrix},
\]
Ozuch 的行列式公式给出
\[
\mu_1
=C\det
\begin{pmatrix}\Lambda&0\\0&0\end{pmatrix}=0.
\]
故利用这一独立结构恒等式后，实际剩余的局部二阶条件是
\[
\mu_3=0,
\]
而不是同时要求 \(\mu_2=\mu_3=0\)。

这一阶数抽取要求相关尺度可比，使 Ozuch 的
\[
O(t_{\max}^{5/2})=o(t_j^2).
\]
若尺度严重分离，现有误差估计不足以逐节点提取 \(t_j^2\) 系数。

---

### 4. A02 的 KE 控制结论过强；Step 79 的回应基本正确

设某精确 KE 族在 Ozuch 坐标中具有
\[
\phi(t)=\phi_0+t\psi+o(t),\qquad
v(t)=t\,w+o(t).
\]
那么二阶约化方程应为
\[
D_\phi\lambda(\psi)
+D_v\lambda(w)
+\mu(\phi_0)=0,
\]
并可能还包含其他以 \(O(t)\) 运动的允许参数。因此精确族只推出
\[
[\mu]=0
\quad\text{于}\quad
\mathbb R^3/
\operatorname{im}D_{(\phi,v,\ldots)}\lambda,
\]
而不推出 \(\mu_k=0\) 逐分量成立。

所以 Step 79 以 Ozuch 证明中允许 \(\phi_n\) 发生 \(O(t)\) 移动来反驳“所有 \(\mu_k\) 自动为零”，是数学上正确的。需要收紧的表述是：

- 若尚未证明 \(v'(0)=0\)，则不能只对 \(D_\phi\lambda\) 取余核；
- 若 \(D_v\lambda(w)\) 有 \(k=3\) 分量，则连“KE 族迫使 \(\mu_3=0\)”也不能单独推出；
- 只有证明该 KE 族在 Ozuch 规范下满足
  \[
  \phi(t)=\phi_0+o(t),\qquad v(t)=o(t),
  \]
  或有额外 Kähler 对称性强制这些一阶运动消失，才可据其推断裸 \(\mu_k\) 分量分别消失。

因此 A02 的 \(r=0\) KE 控制最多提供约化商中的消失，不能替代实际系数计算。

---

### 下一步最关键计算

1. **计算完整一阶参数像空间。**  
   求
   \[
   D_{(\phi,v,\text{其他允许变量})}\lambda
   \]
   在乘积秩一点的秩与像，尤其检查 \(D_v\lambda\) 是否含 \(k=3\) 分量。

2. **提取 KE 控制族的 Ozuch 坐标一阶 jet。**  
   明确
   \[
   \bigl(\phi'(0),v'(0)\bigr),
   \]
   以区分“\(\mu\) 本身为零”和“由参数运动抵消”。

3. **用完整 \(\rho_x\) 计算投影后的 \(\mu_2,\mu_3\)。**  
   应计算定义 \(\mu_k\) 的完整 \(\mathbf o_k\)-投影，包括 \(\underline h_2\) 与
   \(Q^{(2)}(\underline h_2,\underline h_2)\)，而非只检查点态曲率。角积分可用精确 Haar 矩：
   \[
   \int\rho_i\rho_j\,d\sigma
   =\frac{|\zeta|^2}{3}\delta_{ij},
   \]
   \[
   \int\rho_i\rho_j\rho_k\rho_l\,d\sigma
   =\frac{|\zeta|^4}{15}
   (\delta_{ij}\delta_{kl}+\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}).
   \]

4. **量化 \(\mu_2\)-吸收倾斜引起的标量再耦合。**  
   代入
   \[
   a=-\frac{\mu_2}{c\Lambda}
   \]
   后，计算 \(O(t)\) 的逐因子迹源及其通过投影 \(P\)-伪逆对偶标量模和 \(g_1-g_2\) 模的响应。

5. **随后计算完整 \(t^3\) 切片约化映射。**  
   该阶至少包括
   \[
   D\lambda(\psi^{(2)})
   +\frac12D^2\lambda(\psi^{(1)},\psi^{(1)})
   +D\mu(\psi^{(1)})
   +\sum_i\mathcal I_{ji}
   +\text{局部三阶响应}.
   \]
   已有展开显示 \(k=1\) 分量含二次倾斜项 \(c\Lambda a^2\)。此阶不能由当前 \(O(t^{5/2})\) 误差估计直接恢复，需要更精细的约化展开。

总之，Step 79 正确修复了角变量和二阶商空间的两个核心错误；当前真正未决对象不是裸 \((\mu_2,\mu_3)\) 两个数，而是包含全部一阶可调参数、倾斜诱导标量源及配对节点相互作用后的切片余核分量。