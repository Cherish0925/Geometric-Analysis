# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 16,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step16_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step16_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the Step-16 joint dual-calibration note and its core scripts. Check the mathematical normalization of z versus diagonal Ricci, the dual/Gram coefficient 1/4, signs and boundary offset for the spin field, interpretation of the numerical shares, and what the E=0 reconstruction does or does not establish. Identify any substantive error and propose the strongest corrected mathematical formulation toward a diagonal lower theorem. Also check the exact bolt Weyl calculation from the validated 2-jet, including likely factor/chirality convention issues. Do not turn this into a generic issue list; provide a direct scientific memo.

## Integrated Scientific Memo

# 核验备忘录：Step‑16 联合对偶校准与 bolt Weyl 手性

## 1. \(z\) 的归一化及 Gram 系数正确

设正交标架中
\[
\Ric^\circ=\operatorname{diag}(e_0,e_1,e_2,e_3),\qquad
e_0+e_1+e_2+e_3=0,
\]
并定义
\[
z_i=-(e_0+e_i),\qquad i=1,2,3.
\]
则
\[
\sum_{i=1}^3z_i^2
=3e_0^2+2e_0\sum_{i=1}^3e_i+\sum_{i=1}^3e_i^2
=\sum_{\alpha=0}^3e_\alpha^2.
\]
因此
\[
|z|^2=|\Ric^\circ|^2.
\]
所以 \(z\) 确实是完整的三维对角无迹 Ricci 变量，不存在遗漏的“第四 Ricci 通道”。

在笔记采用的轨道体积规范下，
\[
\frac{P}{8\pi^2}=\frac14\int W|z|^2\,dt.
\]
逐点配方
\[
\frac14|z|^2-\frac12z\!\cdot\!\beta+\frac14|\beta|^2
=\frac14|z-\beta|^2
\]
给出
\[
\frac{P}{8\pi^2}\ge
\frac12\langle z,\beta\rangle_W-\frac14\|\beta\|_W^2.
\]
若 \(\beta=\sum_Ac_AB_A\)，定义
\[
m_A=\langle z,B_A\rangle_W,\qquad
G_{AB}=\langle B_A,B_B\rangle_W,
\]
则最优值为
\[
\boxed{\frac14\,m^TG^\dagger m}.
\]
这里 \(G^\dagger\) 为 Moore–Penrose 逆；精确积分时 \(m\in\operatorname{Im}G\)。等价地，
\[
m^TG^\dagger m=\|\Pi_{\operatorname{span}\{B_A\}}z\|_W^2.
\]
因此系数 \(1/4\) 及“把所有方向放进同一个 Gram 矩阵、只优化一次”的做法均正确。

---

## 2. 自旋方向存在两个实质错误：测试场权重错，且边界常数被错误移除

令
\[
p_i=\partial_{u_i}\Phi,\qquad \Phi=C-u_2^2.
\]
源脚本给出的
\[
p=(2H_1,u_1u_3,2H_3)
\]
满足
\[
\dot\Phi=\sum_i p_i\dot u_i.
\]
又由
\[
z_i=\frac{\dot u_i}{a_i}-\frac{2H_i}{a_ja_k},
\qquad
\lambda_i=\frac{a_ja_k}{a_i},
\]
可得
\[
a_i z_i=\dot u_i-\frac{2H_i}{\lambda_i},
\]
故真正的自旋 transport 恒等式是
\[
\sum_i p_i a_i z_i
=\dot\Phi-2\sum_i\frac{p_iH_i}{\lambda_i}. \tag{2.1}
\]

### 2.1 正确的 \(L^2(Wdt)\) 测试场不是 \(p_i/a_i\)

要把 (2.1) 左端写成 \(\int Wz\cdot B^\Phi dt\)，必须取
\[
\boxed{
B_i^\Phi=\frac{a_i}{W}p_i=\frac{p_i}{a_ja_k}.
}
\]
此时
\[
Wz_iB_i^\Phi=p_i a_i z_i.
\]

但是笔记式 (2) 和 `joint_dual_calibration.py` 实际使用
\[
B_i^{\rm code}=\frac{p_i}{a_i}.
\]
对此
\[
Wz_iB_i^{\rm code}
=p_i\left(\frac{a_ja_k}{a_i}\dot u_i-2H_i\right),
\]
一般不等于 (2.1) 的左端。因此笔记所写
\[
\int Wz\cdot\frac{\nabla_u\Phi}{a}\,dt
=\Phi(T)-\Phi(0)-2\int\sum_i\frac{p_iH_i}{\lambda_i}\,dt
\]
按通常逐分量 \(p_i/a_i\) 的含义是错误的。

`check_joint_dual_identities.py` 并未检查这个关键权重等式；它只检查了
\[
\sum_i p_i\left(\dot u_i-\frac{2H_i}{\lambda_i}\right)
=\dot\Phi-2\sum_i\frac{p_iH_i}{\lambda_i},
\]
所以脚本返回零不能验证数值代码中的 `bspin/a`。

这个错误还会导致 bolt 端的可积性问题。若第 \(k\) 轴塌缩，则 \(a_k\sim t\)、\(W\sim ct\)，而相应 \(p_k\) 通常有非零极限，于是
\[
W\left|\frac{p_k}{a_k}\right|^2\sim \frac Ct,
\]
呈对数发散。数值程序把首点替换为 `ve[0]=1e-7`，会把这一发散隐藏为依赖截断的有限数。正确场 \(p_i/(a_ja_k)\) 在塌缩分量的分母由两个非塌缩半径组成，具有正确的加权可积性。

代码应改为
```python
Bspin0 = a*bspin/W[:, None]       # = p_i/(a_j a_k)
Bspin  = Bspin0[:, None, :]
```
并直接检查
```python
integrate(mu*np.sum(z*Bspin0, axis=1), v)
```
与 transport 右端相等。

### 2.2 边界差 \(-1\) 的符号正确，但不能从 Gram moment 中扣除

对 \(O(-1)\) bolt 和标准 CH collar，
\[
\Phi(0)=1,\qquad \Phi(T)=0,
\]
所以
\[
\Phi(T)-\Phi(0)=-1.
\]
因此正确的自旋 moment 是
\[
\boxed{
M_\Phi
=\langle z,B^\Phi\rangle_W
=-1-2\int_0^T\sum_i\frac{p_iH_i}{\lambda_i}\,dt.
} \tag{2.2}
\]

源代码设置
```python
spin_boundary = -1.0
m = raw_integral - offset
```
故实际使用
\[
m_{\rm code}=M_\Phi-(-1)=M_\Phi+1,
\]
即只留下势积分。该仿射平移不是 \(\langle z,B^\Phi\rangle_W\)，不能代入
\(\frac14m^TG^\dagger m\)。边界项可以为解释目的单独列出，但进入 Gram 对偶式时必须恢复完整 moment (2.2)。

因此当前表格中的：

- `spin`；
- `joint`；
- `joint_gain_over_max`；
- “自旋增益在 \(x_0\to0\) 变大、体现 AE charge”的解释；

都不是已建立的对偶下界或投影份额。这里不能只“去掉 offset 后重算”：还必须先把测试场从 \(p_i/a_i\) 改成 \(a_ip_i/W\)。独立分支中关于“去掉 offset 后可能达到 75–85%”的估计没有来源支持，而且忽略了更根本的场权重错误。

---

## 3. 数值 shares 中哪些仍然有效

Green 四场没有仿射偏移；对其统一改号不会改变投影能量。因此在数值积分准确的前提下，
\[
\frac{\texttt{green}}P
=
\frac{\|\Pi_{\mathcal B_{\rm green}}z\|_W^2}
{\|z\|_W^2}.
\]
例如 \(x_0=.03\) 时
\[
0.643402897/0.995848408=0.646085\ldots,
\]
确实表示所选 witness 的约 \(64.6\%\) 对角 Ricci 能量被四维 Green 子空间捕获。它不是四个独立能量账单的相加，而是一次完整 Gram 投影。

因此目前可保留的定量结论是：

- 各 witness 的 Green 子空间捕获约 \(50.7\%-66.1\%\)；
- \(x_0=.03\) witness 对该四维 Green 空间仍有约 \(35.4\%\) 的正交余量。

不能据现有表格声称正确的五场空间只捕获 \(64.9\%\)，因为第五个场及其 moment 都实现错误。也不能由错误的 joint 数据判断正确自旋场究竟增加多少。

此外，这些计算使用浮点中值、`numpy.gradient`、伪逆和 Simpson 积分，没有误差包围。即使底层 metric record 已认证，也不能自动把这些 shares 称为认证下界；它们是具体 witness 上的数值投影估计。

---

## 4. \(E=0\) 重构实验的严格含义

若
\[
E=\Ric_{22}-\Ric_{11},
\]
则它对应对角无迹空间中的单位方向系数 \(E/\sqrt2\)，所以该方向对
\(P/(8\pi^2)\) 的贡献为
\[
\frac14\int W\frac{E^2}{2}\,dt
=\frac18\int WE^2\,dt.
\]
`test_Ezero_reconstruction.py` 的通道归一化因而正确。

实验冻结 \(F,G\)，只改变有限阶参数化中的 \(w\)。它表明：

1. 在该有限维切片内，一个 Ricci 差通道可从 \(0.13210\) 降到 \(0.00632\)；
2. 同时所生成 metric 的完整 \(P/(8\pi^2)\) 上升到约 \(2.46\times10^5\)；
3. 因而“小的单一形状通道”不蕴含“小的完整 \(z\)”。

但它不建立：

- 精确解 \(E\equiv0\)；
- 约束 \(E=0\) 下完整 \(P\) 的下确界；
- 任意消去 \(E\) 的路径都必有巨大代价；
- 同时改变 \(F,G,w\) 时不存在低能路径；
- 任何 competitor-independent 下界。

带 \(\mu\) 的系数惩罚及“系数位移”依赖所选多项式基底，不是几何不变量。这个实验只能作为有限维诊断，不能作为刚性或全局障碍。

---

## 5. 修正后的对角下界框架

对一类正则 \(O(-1)\) bolt、标准 CH collar 的对角 cells，取 Green transport 场以及正确自旋场
\[
B_i^\Phi=\frac{a_i}{W}\partial_{u_i}\Phi.
\]
定义真实 moments 和 Gram 矩阵
\[
M_A(g)=\int Wz\cdot B_A\,dt,\qquad
G_{AB}(g)=\int WB_A\cdot B_B\,dt.
\]
则每个 cell 都满足精确有限维下界
\[
\boxed{
\frac{P(g)}{8\pi^2}
\ge \frac14 M(g)^TG(g)^\dagger M(g).
} \tag{5.1}
\]
其中自旋分量必须是
\[
M_\Phi(g)
=-1-2\int\sum_i
\frac{(\partial_{u_i}\Phi)H_i}{\lambda_i}\,dt. \tag{5.2}
\]

一个直接、足够且不要求 Gram 可逆的统一正间隙准则是：存在
\(\delta,\Lambda>0\)，使所有允许的 \(g\) 都满足
\[
|M(g)|\ge\delta,\qquad
\lambda_{\max}(G(g))\le\Lambda.
\]
因为 \(M\in\operatorname{Im}G\)，由 (5.1)
\[
\boxed{
\frac{P(g)}{8\pi^2}\ge \frac{\delta^2}{4\Lambda}.
} \tag{5.3}
\]
这里需要的是 \(G\) 的统一上谱界，而不是最小特征值下界；线性相关由 \(G^\dagger\) 自动处理。真正困难是证明完整 moment 向量不能被势积分同时抵消，并控制测试场的加权范数。

更一般地，对任意状态函数 \(F(u)\)，定义
\[
B_i^F=\frac{a_i}{W}F_{u_i}.
\]
则有精确恒等式
\[
\langle z,B^F\rangle_W
=F(u(T))-F(u(0))
-2\int\sum_i\frac{F_{u_i}H_i}{\lambda_i}\,dt. \tag{5.4}
\]
若引入局域化乘子 \(\eta(t)\)，
\[
B_i^{\eta,F}=\eta(t)\frac{a_i}{W}F_{u_i},
\]
则
\[
\langle z,B^{\eta,F}\rangle_W
=[\eta F]_0^T-\int\eta'F\,dt
-2\int\eta\sum_i\frac{F_{u_i}H_i}{\lambda_i}\,dt. \tag{5.5}
\]
这给出了把数值上有效的径向局域化方向转化为真正 transport identities 的自然机制。相应 HJ 型下界为
\[
\frac{P}{8\pi^2}\ge
\frac12\langle z,B^{\eta,F}\rangle_W
-\frac14\int \eta^2
\sum_i\frac{a_i^2F_{u_i}^2}{W}\,dt.
\]
由此可见，通向下界定理的核心不是简单增加多项式基，而是选择 \(F,\eta\)，使固定边界通量、\(-\eta'F\) 和非线性势项形成可控正余项。

---

## 6. bolt Weyl 精确计算：原脚本数值错误，手性结论仍成立

给定经过验证的二阶 jet
\[
A(t)=B(t)=\frac45+\frac{49}{20}t^2+O(t^4),\qquad
C(t)=t-\frac{25}{24}t^3+O(t^5),
\]
并采用给出 \(s=-24\) 的曲率号约定，在二形式基
\[
(01,02,03\,|\,23,31,12),\qquad
*01=23,\ *02=31,\ *03=12
\]
中，bolt 曲率算子应具有 Einstein 块形
\[
\mathcal R_0=
\begin{pmatrix}D&Q\\Q&D\end{pmatrix},
\]
其中
\[
D=\operatorname{diag}\!\left(-\frac{49}{8},-\frac{49}{8},\frac{25}{4}\right),
\qquad
Q=\operatorname{diag}\!\left(\frac{25}{16},\frac{25}{16},-\frac{25}{8}\right).
\]
于是手性曲率块为 \(D\pm Q\)，且 \(s/12=-2\)，故
\[
W_\pm=D\pm Q+2I.
\]
按上述定向可取
\[
\boxed{
W^+=\operatorname{diag}\!\left(
-\frac{41}{16},-\frac{41}{16},\frac{41}{8}
\right),
}
\]
\[
\boxed{
W^-=\operatorname{diag}\!\left(
-\frac{91}{16},-\frac{91}{16},\frac{91}{8}
\right).
}
\]
反转定向只交换二者。曲率算子 Hilbert–Schmidt 范数为
\[
\boxed{
\operatorname{tr}(W_+^2)=\frac{5043}{128}=39.3984375,
\qquad
\operatorname{tr}(W_-^2)=\frac{24843}{128}=194.0859375.
}
\]
这与 coordinate check 趋向的 \(39.3985\) 和 \(194.083\) 一致，只差输出顺序和数值极限误差。

因此原笔记列出的
\[
W_A=\diag(-139/16,57/16,41/8),\qquad
W_B=\diag(-385/16,203/16,91/8)
\]
及
\[
14647/128,\qquad111279/128
\]
不是简单的二形式范数倍数或手性互换；它们与 coordinate check 不相容，应删除。

最可能的实现错误是 `ach_bolt_weyl_exact.py` 中的符号捕获和顺序替换：

```python
t,b = sp.symbols('t b', positive=True)
AA = b + A2*t**2
...
subs = {pc.a: AA, pc.b: BB, ...}
expr.subs(subs)
```

若局部 `b` 与 `pc.b` 被 SymPy 视为同一 symbol，顺序 substitution 会继续替换先前插入 `AA` 的 bolt 半径符号，却不会同步修正独立指定的一、二阶 jets，从而人为破坏 \(A-B=O(t^4)\)。应使用全新的 `Dummy` 参数，例如
```python
r = sp.Dummy('r', positive=True)
AA = r + A2*t**2
BB = r + B2*t**2
```
并用 simultaneous substitution；同时明确固定 \((31)\) 而非 \((13)\) 的二形式符号。

若 \(|W^\pm|^2\) 指标准 \((0,4)\)-张量范数，则相对曲率算子范数多因子 \(4\)：
\[
|W^+|_{(0,4)}^2=\frac{5043}{32},\qquad
|W^-|_{(0,4)}^2=\frac{24843}{32}.
\]
Chern–Weil 公式通常使用这一张量规范，必须在后续公式中明确区分。

无论采用哪一统一范数规范，两个块均严格非零。因此可靠的最终结论是：

\[
\boxed{\text{该经验证的 ACH Einstein filling 既非自对偶，也非反自对偶。}}
\]

具体 \(W^\pm\) 标签取决于整体定向，但非半共形平坦结论不受影响。