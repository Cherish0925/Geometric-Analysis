# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 26,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step26_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step26_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step-26 nilpotent abelian-forcing audit for the Yau-26 positive branch. Focus on mathematical correctness and theorem-shaping consequences: (i) the Heisenberg intrinsic Ricci/anistropy pattern; (ii) the twist-only rank/center bound and whether it is narrow; (iii) the cohomogeneity-one diagonal H3 moving-frame Ricci formulas and the claim that T-active local exact Ric=+1 data with large bracket are algebraically possible; (iv) whether this really defeats a pointwise Milnor-only abelian-forcing theorem and supports a graded/relative-rate theorem instead; (v) source-scope claims about Kapovitch--Wilking/Naber--Zhang/Rong. Do not invent external facts; if exact O'Neill formulas are needed but not in the files, state the missing source need precisely. Please give a direct scientific memo: corrections, confirmed parts, and what theorem statement remains viable.

## Integrated Scientific Memo

# Step-26 核验备忘录

## 结论

Step-26 的核心局部计算成立，但其一般性结论必须收窄：

- \(H_3\) 的内禀 Ricci 与各向异性公式正确。
- \(T=0\) 时的中心方向上界和 twist 秩阻碍正确，但只是垂直方程给出的必要条件，不能代表一般坍缩。
- 对角余维一 \(H_3\) 模型的移动标架 Ricci 公式正确；任意大的正交 bracket \(b\) 都能出现在局部光滑的精确 \(\operatorname{Ric}=g\) 解中。
- 因而，“总 Ricci 夹逼 + Milnor 纤维 Ricci”在一点上直接迫使非交换纤维阿贝尔化，是错误的。
- 现有材料支持的是**相对速率/分级型条件定理**：大 bracket 若持续，必须由同阶的第二基本形式及更快的横向变化补偿。它尚未证明一般闭流形上的非交换坍缩必然分解成迭代阿贝尔阶段。

---

## 1. Heisenberg 内禀 Ricci：确认

设正交标架满足
\[
[e_1,e_2]=b e_3.
\]
其截面曲率为
\[
K_{12}=-\frac34b^2,\qquad K_{13}=K_{23}=\frac14b^2,
\]
故
\[
\operatorname{Ric}^F
=\operatorname{diag}\!\left(-\frac12b^2,-\frac12b^2,\frac12b^2\right),
\qquad
\operatorname{scal}_F=-\frac12b^2.
\]
中心方向与任一生成元方向的 Ricci 差恰为
\[
\operatorname{Ric}^F(e_3,e_3)-\operatorname{Ric}^F(e_1,e_1)=b^2.
\]

因此 Step-26 所称的内禀“相反符号 + 大小 \(b^2\) 的各向异性”完全正确。

---

## 2. \(T=0\) twist-only 检验：正确但很窄

在纤维全测地的 Riemannian submersion 中，垂直 Ricci 满足
\[
\operatorname{Ric}_M(U,U)
=
\operatorname{Ric}_F(U,U)+Q(U,U),
\qquad
Q(U,U)=\sum_i|A_{X_i}U|^2\ge0.
\]
若记
\[
\omega_{ij}=A_{X_i}X_j,
\]
则在标准约定下
\[
Q(U,U)=2\sum_{i<j}\langle\omega_{ij},U\rangle^2.
\]
系数可能随 \(A\)-张量约定改变，但以下两点不变：
\[
Q\ge0,\qquad \operatorname{rank}Q\le \binom d2,
\]
其中 \(d\) 是底空间维数。

若要求 \(H_3\) 的垂直 Ricci 精确等于单位阵，则必须有
\[
Q=I-\operatorname{Ric}^F
=
\operatorname{diag}\!\left(
1+\frac12b^2,\,
1+\frac12b^2,\,
1-\frac12b^2
\right).
\]

由此严格得到：

1. 若
   \[
   \operatorname{Ric}_M\le (1+\delta)g,
   \]
   则中心方向给出
   \[
   \frac12b^2\le1+\delta.
   \]

2. 当 \(0<b<\sqrt2\) 时，所需 \(Q\) 正定，秩为 \(3\)，故秩条件要求
   \[
   \binom d2\ge3,
   \]
   即 \(d\ge3\)。

3. 当 \(b=\sqrt2\) 时，所需 \(Q\) 的秩为 \(2\)；二维底空间仍只有
   \[
   \binom22=1
   \]
   个独立 twist 方向，不能实现。

4. \(d\ge3\) 仅通过秩检验；它不保证水平、混合 Ricci 方程、曲率形式闭合性或整体拓扑条件可同时满足。

因此 \(H_3\) over a \(2\)-base 的阻碍是可靠的，但只是 \(T=0\) 的局部代数必要条件。Burdick Lemma 2.5 已能确认全测地情形中 twist 项的正号结构；真正缺失的是一般 \(T\neq0\) 的完整 O’Neill 系统。

---

## 3. 对角余维一 \(H_3\) 模型：公式确认

考虑
\[
g=dt^2+a(t)^2(\theta_1^2+\theta_2^2)+c(t)^2\theta_3^2,
\qquad [E_1,E_2]=E_3,
\]
并令
\[
k_1=\frac{a'}a,\qquad
k_3=\frac{c'}c,\qquad
H=2k_1+k_3,\qquad
b=\frac{c}{a^2}.
\]
正交标架满足
\[
[e_0,e_1]=-k_1e_1,\quad
[e_0,e_2]=-k_1e_2,\quad
[e_0,e_3]=-k_3e_3,\quad
[e_1,e_2]=be_3.
\]

Koszul/移动标架计算给出
\[
\begin{aligned}
\operatorname{Ric}_{00}
&=-2(k_1'+k_1^2)-(k_3'+k_3^2),\\
\operatorname{Ric}_{11}
=\operatorname{Ric}_{22}
&=-\frac{b^2}{2}-k_1'-Hk_1,\\
\operatorname{Ric}_{33}
&=\frac{b^2}{2}-k_3'-Hk_3.
\end{aligned}
\]
这些公式与 `step26_heisenberg_moving_frame_ricci.json` 的符号输出完全一致。

令三个切片方向满足 \(\operatorname{Ric}_{ii}=1\)，则
\[
k_1'=-1-\frac12b^2-Hk_1,
\qquad
k_3'=-1+\frac12b^2-Hk_3,
\]
同时
\[
\frac{b'}b=k_3-2k_1.
\]
剩余的 \(\operatorname{Ric}_{00}=1\) 等价于约束
\[
C:=4k_1^2+8k_1k_3+b^2+4=0.
\]

还可直接验证
\[
C'=-2HC.
\]
因此满足 \(C=0\) 的初值会由 ODE 精确保持；局部大-\(b\) Einstein 数据不只是数值现象。

事实上，对任意 \(B>0\)，取
\[
b(0)=B,\qquad
k_1(0)=\frac B2,\qquad
k_3(0)=-\frac B2-\frac1B
\]
即满足约束。取正的 \(a(0),c(0)\)，再解
\[
a'=k_1a,\qquad c'=k_3c,
\]
便得到真正的局部光滑 \(\operatorname{Ric}=g\) 度量。文件中的 \(B=20\) 样本正是
\[
k_1=10,\qquad k_3=-10.05,
\]
且
\[
b'=b(k_3-2k_1)=-601.
\]

数值残差只验证 ODE 积分和约束保持；独立的曲率依据是移动标架符号计算。

---

## 4. 可强化为严格的相对速率估计

令切片第二基本形式的平方范数为
\[
|T|^2=2k_1^2+k_3^2.
\]
由约束及恒等式
\[
4k_1^2+8k_1k_3+2|T|^2
=2(2k_1+k_3)^2\ge0
\]
得到
\[
|T|^2\ge\frac{b^2+4}{2}.
\]
故在这个精确 Einstein 模型中，大 bracket 必然要求
\[
|T|\gtrsim |b|.
\]

同样，
\[
4k_1^2+8k_1k_3+\frac45(k_3-2k_1)^2
=\frac45(3k_1+k_3)^2\ge0
\]
给出
\[
\left|\frac{b'}b\right|^2
\ge\frac54(b^2+4),
\]
从而
\[
|b'|\gtrsim b^2.
\]

这两条比单个数值样本更有价值：在该模型中，Milnor 各向异性可以被抵消，但代价必然是同阶的第二基本形式和更快的 bracket 相对变化。

对
\[
1-\delta\le \operatorname{Ric}_{\mu\mu}\le1+\delta
\]
的同一对角模型，消去导数可得
\[
4k_1^2+8k_1k_3
=
2\rho_0-4\rho_1-2\rho_3-b^2.
\]
因此
\[
|T|^2\ge\frac{b^2+4-8\delta}{2},
\qquad
\left|\frac{b'}b\right|^2
\ge\frac54\bigl(b^2+4-8\delta\bigr).
\]
这给出了可直接使用的 pinched 模型定理。

---

## 5. 它究竟否定了什么

该局部模型严格否定如下点态论证：

> nilpotent 纤维的 Milnor Ricci 含 \(\pm b^2/2\)，而总 Ricci 有界，所以 \(b\) 必须小。

错误在于忽略了第二基本形式、平均曲率及横向导数项；这些项可以精确抵消内禀 Milnor 各向异性。

甚至可在一点取
\[
a(0)=c(0)=B^{-1},
\]
使三个纤维方向同尺度、纤维直径约 \(B^{-1}\)，同时
\[
b(0)=B.
\]
所以现有计算也不能推出“同尺度非交换局部切片不可能”。它只能推出：这种配置若存在，必须有
\[
|T|\asymp B,\qquad |b'|\asymp B^2.
\]

因此不能把 Step-26 写成“同尺度非交换坍缩已经被排除”。严格结论应是：

> 在原度量下若 \(T\)、平均曲率及进入垂直 Ricci 的横向导数项在相应尺度上统一受控，则大 bracket 无法被这些项补偿；在该附加控制下，第一可见坍缩尺度才可望阿贝尔化。

分级尺度
\[
a=\varepsilon^\alpha,\qquad
c=\varepsilon^\gamma,\qquad
b=\varepsilon^{\gamma-2\alpha}
\]
与此相容：

- \(\gamma=\alpha\)：同尺度坍缩，\(b\to\infty\)，需要 \(|T|\to\infty\)；
- \(\gamma=2\alpha\)：\(b=O(1)\)，但在直径尺度重标后 bracket 为
  \[
  \varepsilon^\alpha b\to0;
  \]
- \(\gamma>2\alpha\)：\(b\to0\)。

这支持“交换子方向可能落入更小尺度”的机制，但没有证明一般非交换坍缩必然如此分级。

---

## 6. 全局标量积分不能单独完成证明

该模型的标量曲率可重写为
\[
\operatorname{scal}_M
=
-\frac12b^2-2H'-H^2-|T|^2.
\]
若
\[
w=a^2c,\qquad \frac{w'}w=H,
\]
且数据周期，则
\[
\int \operatorname{scal}_M\,w\,dt
=
\int\left(-\frac12b^2+H^2-|T|^2\right)w\,dt.
\]
其中 \(+H^2\) 仍可承担补偿，所以一般标量积分并不自动控制 \(b\)。

对精确 \(\operatorname{Ric}=g\) 模型，约束进一步给出
\[
-\frac12b^2+H^2-|T|^2=-b^2-2,
\]
与周期闭合不相容。因此这些局部解不能直接拼成周期型闭模型；若通过奇异轨道闭合，必须显式计算端点/固定层通量。

---

## 7. 文献范围：可确认与不可外推之处

### Kapovitch–Wilking / Naber–Zhang

供应材料支持：

- 在
  \[
  \operatorname{Ric}\ge-(n-1)
  \]
  下，短环像群为 \((w(n),n)\)-nilpotent。
- 若球 GH 接近 \(k\)-维 Ricci 极限球，则精细 fibered group 为
  \[
  (w_0,n-k)\text{-nilpotent},\qquad
  \operatorname{rank}\le n-k.
  \]
- 在 GH 模型及最大秩假设下，局部普遍覆盖非坍缩并有调和半径下界。
- 若进一步是 Einstein，或有 \(|\nabla\operatorname{Ric}|\) 上界，则可得曲率上界。

因此这些结果给出群论 nilpotency、秩界及特定区域的覆盖正则性；它们不由两侧 \(C^0\) Ricci 夹逼自动产生一个对原度量具有统一 \(A,T,N\) 控制的 Riemannian submersion。

最大秩、\(\dim Z^\ell\le3\) 的区域确实是最有希望建立阿贝尔 forcing 的区域，因为 Naber–Zhang 在那里提供覆盖正则性。维数限制是实质性的；供应材料明确指出 \(\ell=4\) 时存在 Eguchi–Hanson 型反例。

### Rong

Rong 的 Theorem B 需要：

- Ricci 下界；
- local rewinding volume 下界；
- GH 接近较低维、非坍缩的光滑流形；
- 底空间的截面曲率和 injectivity radius 控制。

结论是光滑 fiber bundle、infra-nil 纤维、仿射结构群和 GHA。其定理陈述没有给出原度量下统一的 \(\varepsilon\)-Riemannian submersion、纤维第二基本形式或完整 O’Neill 张量估计。因此它解决了拓扑纤维识别，却没有自动补上 Step-26 所需的定量曲率方程。

---

## 8. 仍然可行的定理形态

当前已严格成立的模型定理是：

> 对角余维一 \(H_3\) 度量若满足 \(\operatorname{Ric}=g\)，则
> \[
> |T|^2\ge\frac{b^2+4}{2},
> \qquad
> |\partial_t\log b|^2\ge\frac54(b^2+4).
> \]
> 对 \([1-\delta,1+\delta]\)-夹逼有上述 \(8\delta\) 修正。

一般 regular infranil-submersion 的合理条件式定理应表述为：

> 在一个与原度量定量相容的 regular infranil fibration 上，若 \(A,T,N\) 及进入垂直 Ricci 的横向导数项在 collapse scale 上统一受控，则非交换 bracket 不能以主阶出现在第一可见坍缩尺度；该阶段因而虚拟阿贝尔。更深层的非交换结构只能通过尺度分离进入后续层。

这仍需：

1. 完整且固定约定的 \(T\neq0\) O’Neill Ricci 公式；
2. 混合与水平方程；
3. 标量迹中的 mean-curvature divergence 项及正确积分测度；
4. 奇异/固定层的边界通量；
5. 从 \(C^0\) Ricci 夹逼导出上述 fibration 与张量控制的正则性桥梁。

Burdick Lemma 2.5 只足以确认全测地或特殊 doubly-warped 情形，不能替代一般公式。所需直接来源必须明确给出一般垂直 Ricci、混合 Ricci、水平 Ricci、\(T\)、\(A\)、mean curvature 以及散度项的符号和系数。

**最终判定：**Step-26 成功推翻了过强的点态 Milnor-only 阿贝尔 forcing，并建立了严格的 \(H_3\) 相对速率模型；它支持但尚未证明一般 graded/iterated-abelian collapse 定理。