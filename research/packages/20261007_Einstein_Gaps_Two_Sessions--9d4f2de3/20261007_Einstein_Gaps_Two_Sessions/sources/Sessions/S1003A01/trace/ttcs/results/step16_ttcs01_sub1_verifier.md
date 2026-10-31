# TTCS Independent Branch Record

```json
{
  "step_id": 16,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step16_joint_dual_calibration_and_exact_bolt_chirality.md",
    "Sessions/S1003A01/workspace/scripts/joint_dual_calibration.py",
    "Sessions/S1003A01/workspace/scripts/check_joint_dual_identities.py",
    "Sessions/S1003A01/workspace/scripts/test_Ezero_reconstruction.py",
    "Sessions/S1003A01/workspace/scripts/ach_bolt_weyl_exact.py",
    "Sessions/S1003A01/workspace/scripts/ach_bolt_weyl_coordinate_check.py",
    "Sessions/S1003A01/workspace/data/joint_dual/summary.csv",
    "Sessions/S1003A02/workspace/notes/step15_ach_projected_theory.md",
    "Sessions/S1003A02/workspace/data/ach_capd/fuchs_boxes_N6_complex.json"
  ]
}
```

## Task

Read the Step-16 joint dual-calibration note and its core scripts. Check the mathematical normalization of z versus diagonal Ricci, the dual/Gram coefficient 1/4, signs and boundary offset for the spin field, interpretation of the numerical shares, and what the E=0 reconstruction does or does not establish. Identify any substantive error and propose the strongest corrected mathematical formulation toward a diagonal lower theorem. Also check the exact bolt Weyl calculation from the validated 2-jet, including likely factor/chirality convention issues. Do not turn this into a generic issue list; provide a direct scientific memo.

## Output

# 科学核验备忘录

## 1. \(z\) 与对角无迹 Ricci 的归一化是正确的

设正交标架下
\[
\operatorname{Ric}^{\circ}=\operatorname{diag}(e_0,e_1,e_2,e_3),
\qquad \sum_{\alpha=0}^3e_\alpha=0,
\]
且
\[
z_i=-(e_0+e_i),\qquad i=1,2,3.
\]
则
\[
\sum_{i=1}^3z_i^2
=\sum_{i=1}^3(e_0+e_i)^2
=3e_0^2+2e_0\sum_{i=1}^3e_i+\sum_{i=1}^3e_i^2
=\sum_{\alpha=0}^3e_\alpha^2.
\]
所以
\[
|z|^2=|\operatorname{Ric}^{\circ}|^2.
\]
这也说明对角无迹 Ricci 确实只有三个独立分量，不存在遗漏的“第四通道”。

在笔记采用的主轨道体积归一化
\[
\int_{S^3}\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2
\]
下，
\[
\frac{P}{8\pi^2}
=\frac14\int W|z|^2\,dt
\]
与四维体积积分一致。

对任意 \(\beta\in L^2(Wdt;\mathbb R^3)\)，逐点恒等式
\[
\frac14|z|^2-
\left(\frac12z\cdot\beta-\frac14|\beta|^2\right)
=\frac14|z-\beta|^2
\]
给出
\[
\frac{P}{8\pi^2}
\geq \frac12\langle z,\beta\rangle_W-\frac14\|\beta\|_W^2.
\]
若 \(\beta=\sum_Ac_AB_A\)，
\[
m_A=\langle z,B_A\rangle_W,\qquad
G_{AB}=\langle B_A,B_B\rangle_W,
\]
则最大值确为
\[
\boxed{\frac14\,m^TG^\dagger m}.
\]
当积分精确时，\(m\in\operatorname{Im}G\)，所以允许使用 Moore–Penrose 逆。该量还有明确几何意义：
\[
m^TG^\dagger m=\|\Pi_{\operatorname{span}\{B_A\}}z\|_W^2.
\]
因此 \(1/4\) 系数和“只优化一次完整 Gram 矩阵”的原则都是正确的。

---

## 2. 自旋场有两个实质性错误：权重错误与端点常数被错误移除

记
\[
p_i=\partial_{u_i}\Phi,\qquad
\Phi=C-u_2^2,
\]
则脚本中的
\[
p=(2H_1,u_1u_3,2H_3)
\]
与
\[
\frac{d\Phi}{dt}=\sum_ip_i\dot u_i
\]
相符。又因
\[
z_i=\frac{\dot u_i}{a_i}-\frac{2H_i}{a_ja_k},
\qquad
\lambda_i=\frac{a_ja_k}{a_i},
\]
有
\[
a_iz_i=\dot u_i-\frac{2H_i}{\lambda_i}.
\]
从而真正的自旋通量恒等式是
\[
\sum_i p_i a_i z_i
=\frac{d\Phi}{dt}
-2\sum_i\frac{p_iH_i}{\lambda_i}.
\]

### 正确的 Hilbert 空间测试场

为了把左端写成 \(\int Wz\cdot B^\Phi dt\)，必须取
\[
\boxed{
B^\Phi_i=\frac{a_i}{W}p_i
=\frac{p_i}{a_ja_k}.
}
\]
因为
\[
Wz_iB^\Phi_i=p_i a_i z_i.
\]

笔记和 `joint_dual_calibration.py` 使用的是
\[
B_i^{\rm code}=\frac{p_i}{a_i},
\]
但此时
\[
Wz_iB_i^{\rm code}
=p_i\left(\frac{a_ja_k}{a_i}\dot u_i-2H_i\right),
\]
并不等于
\[
p_i\left(\dot u_i-\frac{2H_i}{\lambda_i}\right).
\]
因此式 (2) 与数值脚本实际使用的测试场并不对应。

`check_joint_dual_identities.py` 只验证了
\[
\sum_i p_i\left(\dot u_i-\frac{2H_i}{\lambda_i}\right)
=\dot\Phi-2\sum_i\frac{p_iH_i}{\lambda_i},
\]
没有验证其与 \(Wz\cdot(p/a)\) 相等。这正是符号程序仍然输出零、而数值场却不正确的原因。

### 错误场在光滑 bolt 处通常不属于加权 \(L^2\)

由 \(\Phi(0)=1\) 可知塌缩轴不是第 \(2\) 轴。在塌缩轴 \(k=1\) 或 \(3\) 上，
\[
a_k\sim t,\qquad u_k(0)=-1,\qquad p_k(0)=2H_k(0)=-2,
\qquad W\sim c\,t.
\]
于是
\[
W\left|\frac{p_k}{a_k}\right|^2\sim \frac{C}{t},
\]
其积分呈对数发散。脚本用 `ve[0]=1e-7` 避开了端点，因而得到的是依赖人工截断和网格的有限数值。

正确场 \(p_i/(a_ja_k)\) 在同一轴上的分母是两个非塌缩半径之积，光滑 bolt 展开使其加权平方积分有限。

### 端点常数 \(-1\) 必须保留在 moment 中

对标准 CH collar，
\[
\Phi(0)=1,\qquad \Phi(T)=0,
\]
故正确 moment 为
\[
\boxed{
m_\Phi
=\langle z,B^\Phi\rangle_W
=-1-2\int_0^T\sum_i\frac{p_iH_i}{\lambda_i}\,dt.
}
\]
脚本设置 `spin_boundary=-1`，随后计算
\[
m_{\rm code}=\langle z,B\rangle_W-(-1)
=\langle z,B\rangle_W+1.
\]
这把固定端点贡献移除了。Gram 对偶式要求使用真实内积 \(\langle z,B\rangle_W\)，不能用加上常数后的仿射量替代。若把
\[
m_{\rm pot}:=m_\Phi+1
\]
单独存为势项信息，则进入 Gram 公式时必须恢复
\[
m_\Phi=m_{\rm pot}-1.
\]

因此：

* 端点差 \(\Phi(T)-\Phi(0)=-1\) 的符号正确；
* 将它从 Gram moment 中减去是不正确的；
* `spin` 与 `joint` 两列目前不是式 (1) 的数值下界；
* \(x_0\to0\) 时报告的自旋增益及其 AE 电荷解释，不能由现有表格推出。

核心代码中的对应修正应是
```python
Bspin0 = a*bspin/W[:, None]
Bspin = Bspin0[:, None, :]
```
并以零仿射偏移形成 Gram moment。恒等式可独立比较
\[
\int Wz\cdot B^\Phi dt
\quad\text{与}\quad
-1-2\int\sum_i p_iH_i/\lambda_i\,dt.
\]

---

## 3. 数值“份额”的准确解释

四个 Green 形状场没有使用仿射偏移，其符号整体翻转也不会改变投影能量。因此在积分误差可忽略时，
\[
\frac{\texttt{green}}{P}
=
\frac{\|\Pi_{\mathcal B_{\rm green}}z\|_W^2}{\|z\|_W^2}.
\]
例如 \(x_0=.03\) 时
\[
\frac{0.6434029}{0.9958484}=0.646085\ldots
\]
确实表示四维 Green 子空间捕获了该样本约 \(64.6\%\) 的对角 Ricci 能量。它不是若干独立“付费通道”的相加，而是一次正交投影；完整 Gram 矩阵在这里发挥了正确作用。

现有 `joint` 数字混入了错误自旋场、非零仿射偏移以及 bolt 截断，因此不能解释为更大子空间的投影份额。当前可保留的数值信息是 Green 四场的约 \(50.7\%\)–\(66.1\%\) 投影结果，以及在 \(x_0=.03\) 样本上仍有约 \(35.4\%\) 位于该四维子空间的正交补中。

此外，该脚本使用浮点中值、`numpy.gradient` 和 Simpson 积分，没有给出积分误差包围。故表中数值应称为投影能量估计；输入 metric record 的认证并不会自动认证这些二次积分。

---

## 4. \(E=0\) 重构实验实际说明了什么

设
\[
E=\operatorname{Ric}_{22}-\operatorname{Ric}_{11}.
\]
对角无迹张量中，与单位方向
\[
T=\frac1{\sqrt2}\operatorname{diag}(0,-1,1,0)
\]
对应的系数是 \(E/\sqrt2\)。因此该方向对 \(P/(8\pi^2)\) 的正交能量贡献为
\[
\frac14\int W\frac{E^2}{2}\,dt
=\frac18\int WE^2\,dt.
\]
所以脚本所针对的标量通道及其 \(1/8\) 系数在数学上是正确的。

实验冻结 \(F,G\)，只在有限阶 \(w\) 系数中变化。其结果说明：

* 在这个有限维切片内，所选 Ricci 差能量可以从 \(0.13210\) 降到 \(0.00632\)；
* 同一生成 metric 的完整 \(P/(8\pi^2)\) 同时升至 \(2.46\times10^5\)；
* 因而单独控制 \(E\) 不能代替控制完整三向量 \(z\)。

它没有给出以下数学结论：

* 没有构造精确满足 \(E\equiv0\) 的 metric；
* 没有求出约束 \(E=0\) 下完整 \(P\) 的下确界；
* 没有证明任意消去该通道的路径都必须产生巨大完整代价；
* 没有排除同时改变 \(F,G,w\) 的低能序列。

带 \(\mu\) 的系数惩罚依赖所选多项式参数化和基底，因此“系数位移大小”不是几何不变量；相应输出适合作为该有限维参数化中的权衡数据。完整 \(P\) 的剧增则是所生成 metric 的几何量。

---

## 5. 通向对角下界的修正数学表述

令 \(\mathcal C\) 为正则 \(O(-1)\) bolt、标准 CH collar 的某类对角 cells。对每个 \(g\in\mathcal C\)，取四个形状场和正确的自旋场
\[
B^\Phi_i=\frac{a_i}{W}\partial_{u_i}\Phi.
\]
定义
\[
M_A(g)=\int Wz\cdot B_A\,dt,\qquad
G_{AB}(g)=\int WB_A\cdot B_B\,dt.
\]
则对每一个 cell 都有精确命题
\[
\boxed{
\frac{P(g)}{8\pi^2}
\geq \frac14M(g)^TG(g)^\dagger M(g).
}
\]
自旋分量必须写成
\[
M_\Phi(g)
=-1-2\int\sum_i
\frac{(\partial_{u_i}\Phi)H_i}{\lambda_i}\,dt.
\]

一个直接的统一正下界充分条件是存在 \(\delta,\Lambda>0\)，使所有 \(g\in\mathcal C\) 满足
\[
|M(g)|\geq\delta,
\qquad
\lambda_{\max}(G(g))\leq\Lambda.
\]
由于 \(M(g)\in\operatorname{Im}G(g)\)，随即得到
\[
\boxed{
\frac{P(g)}{8\pi^2}\geq\frac{\delta^2}{4\Lambda}.
}
\]
这里不需要 Gram 矩阵的最小特征值下界；相关或线性依赖的测试场由 \(G^\dagger\) 自动处理。真正需要的内容是：端点通量与势积分组成的完整 \(M\) 不能同时接近零，同时测试场的加权平方范数保持统一可控。

自旋结构还给出一个更灵活的非线性校准公式。对任意光滑 \(F(u)\)，令
\[
B_i^F=\frac{a_i}{W}\frac{\partial F}{\partial u_i}.
\]
则
\[
\langle z,B^F\rangle_W
=F(u(T))-F(u(0))
-2\int\sum_i\frac{F_{u_i}H_i}{\lambda_i}\,dt,
\]
并且
\[
\frac{P}{8\pi^2}\geq
\frac12\bigl(F(u(T))-F(u(0))\bigr)
-\int\sum_i\frac{F_{u_i}H_i}{\lambda_i}\,dt
-\frac14\int\sum_i\frac{a_i^2F_{u_i}^2}{W}\,dt.
\]
允许径向乘子 \(\eta(t)\) 时，
\[
B_i^{\eta,F}=\eta(t)\frac{a_i}{W}F_{u_i}
\]
满足
\[
\langle z,B^{\eta,F}\rangle_W
=[\eta F]_0^T-\int\eta'F\,dt
-2\int\eta\sum_i\frac{F_{u_i}H_i}{\lambda_i}\,dt.
\]
这提供了局域化自旋场的精确 transport 恒等式，同时保留固定端点信息。它比把多项式乘子仅作为数值投影基底更接近可证明的中尺度下界结构。

---

## 6. bolt Weyl 精确值：原脚本矩阵不正确，但“双手性均非零”仍成立

取
\[
A(t)=B(t)=r+\frac{49}{20}t^2+O(t^4),
\qquad
C(t)=t-\frac{25}{24}t^3+O(t^5),
\qquad r=\frac45.
\]
在定向二形式基底
\[
(01,02,03\,|\,23,31,12),
\qquad *01=23,\quad *02=31,\quad *03=12,
\]
且采用给出 \(s=-24\) 的曲率号约定时，bolt 处曲率算子的结构为
\[
\mathcal R_0=
\begin{pmatrix}
D&Q\\
Q&D
\end{pmatrix},
\]
其中
\[
D=\operatorname{diag}\left(-\frac{49}{8},-\frac{49}{8},\frac{25}{4}\right),
\qquad
Q=\operatorname{diag}\left(\frac{25}{16},\frac{25}{16},-\frac{25}{8}\right).
\]
这里径向截面曲率为
\[
K_{01}=K_{02}=-\frac{2(49/20)}{4/5}=-\frac{49}{8},
\qquad
K_{03}=-6\left(-\frac{25}{24}\right)=\frac{25}{4},
\]
Einstein 方程给出互补截面相同；Cartan 连接计算给出
\[
Q=\left(r^{-2},r^{-2},-2r^{-2}\right).
\]

因此两个手性曲率块为 \(D\pm Q\)。由于 \(s/12=-2\)，Weyl 算子块是
\[
\mathcal W_\pm=D\pm Q+2I.
\]
在上述定向下可取
\[
\boxed{
\mathcal W_+
=\operatorname{diag}\left(
-\frac{41}{16},-\frac{41}{16},\frac{41}{8}
\right),
}
\]
\[
\boxed{
\mathcal W_-
=\operatorname{diag}\left(
-\frac{91}{16},-\frac{91}{16},\frac{91}{8}
\right).
}
\]
反转定向只会交换这两个块。

对应的曲率算子 Hilbert–Schmidt 平方范数是
\[
\boxed{
\operatorname{tr}(\mathcal W_+^2)=\frac{5043}{128}
=39.3984375,
}
\]
\[
\boxed{
\operatorname{tr}(\mathcal W_-^2)=\frac{24843}{128}
=194.0859375.
}
\]
这正好解释 `ach_bolt_weyl_coordinate_check.py` 趋近的 \(39.3985\) 和 \(194.083\)。它们并不支持原脚本给出的
\[
\frac{14647}{128},\qquad \frac{111279}{128}.
\]
两组数之间不存在统一倍率；交换手性标签也不能使其一致。

原脚本最可能的代数来源是符号捕获：

```python
t,b = sp.symbols('t b', positive=True)
AA = b + A2*t**2
...
subs = {pc.a: AA, pc.b: BB, ...}
expr.subs(subs)
```

若局部 `b` 与 `pc.b` 是同一个 SymPy symbol，默认顺序替换会继续替换先前插入到 `AA` 中的 `b`，而 `a1,a2` 的 jet 替换不会同步改变。这会人为制造 \(A-B=O(t^2)\)，破坏真实的 \(A-B=O(t^4)\) bolt 结构。使用新的 `Dummy` 半径符号和 simultaneous substitution 可消除此问题。二形式对 \((3,1)\) 的定向符号也应在 `R` 接口中显式固定。

若 \(|W^\pm|^2\) 表示标准 \((0,4)\) 张量范数，则与曲率算子范数相差因子 \(4\)：
\[
|W^+|_{(0,4)}^2=\frac{5043}{32},
\qquad
|W^-|_{(0,4)}^2=\frac{24843}{32}.
\]
Chern–Weil 公式通常使用这一张量范数。无论采用哪一种统一规范，两个块都精确非零，所以该 ACH Einstein metric 既非自对偶也非反自对偶；这一手性结论保留，但原笔记中的具体矩阵和平方范数需要替换。