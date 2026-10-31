# TTCS Independent Branch Record

```json
{
  "step_id": 4,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/cell_qsearch.py",
    "Sessions/S1003A01/workspace/scripts/cell_compensation.py",
    "Sessions/S1003A01/workspace/data/cell_qsearch/main_mu01.jsonl",
    "Sessions/S1003A01/workspace/data/cell_qsearch_small/musmall.jsonl",
    "Sessions/S1003A01/workspace/notes/step3_coupled_compensation_and_route_reassessment.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_localization_and_coupled_filling.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md"
  ]
}
```

## Task

Read the current O11 triaxial-cell theory and the new direct positive-q computational instrument/results. Check whether the numerical experiment genuinely enters the necessary I55 dangerous sector and whether its conclusions about inner-scale versus fixed-physical-scale compensation follow from the data. Inspect for normalization, optimization, smoothness/collar, positivity, or interpretation errors. Most importantly, identify the strongest mathematically extractable scaling conjecture/weighted ODE inequality suggested by the q>0 results, without treating finite-dimensional optimization as proof.

## Output

# 科学核验备忘录：正 \(q\) 搜索、尺度分支与候选加权 ODE 不等式

## 一、核心结论

1. **这些计算确实进入了 I55 的危险正 \(q\) 区间。**  
   对 C1 而言，形式收益出现于 \(0<q<2M_0\)；全部目标 \(q=fM_0\) 满足 \(0<f\le1\)。更强地，对可能达到 \(j<4\) 的必要条件
   \[
   q>\delta_{\mu,R}
   =1+\frac2\mu\left(1-\sqrt{1-\mu^2/R^4}\right),
   \]
   所有数据也都满足。因而这不是此前停留在 \(q\le0\) 的搜索。

2. **但低代价结果几乎全在 \(w=0\) 或 \(w\) 极小的分支。**  
   最佳数据中 \(P_w=N=R_V=0\)，带 \(w\)-种子的解也通常回到 \(w_{\max}\sim10^{-4}\!-\!10^{-3}\)。因此它们主要探测的是**共形双轴、从而共形 Kähler** 的子类；这个子类已经由 I54 定理严格满足 \(j\ge K\)。计算清楚展示了正 \(q\) 如何由 \(R_X,R_Z\) 等项补偿，却尚未实质探测未解决的有限振幅三轴机制。

3. **数据中确有两个不同的数值尺度分支：**
   - 低代价分支：\(j=O(1)\)、\(\|\phi\|_\infty=O(1)\)，与 \(r=\sqrt\mu\,x\) 的内尺度一致；
   - `fixed` 延拓分支：\(j\sim C(f)/\mu\)、\(\|\phi\|_\infty\sim A(f)/\sqrt\mu\)，与固定物理环带上的梯度预算一致。

   这两种标度很清楚，但“所有固定物理尺度补偿都必须支付 \(1/\mu\)”并不由当前优化给出。各 family 只规定初值；随后 \(F,w,\phi\) 在同一个有限维空间内全部变化。不同结果主要说明不同吸引盆，而不是两个彼此隔离的度量类。

4. **最强且数学上自然的提炼，是一个明确的内尺度极限泛函及其加权 ODE 不等式**
   \[
   \widehat{\mathscr R}\ge \vartheta(4-\vartheta),
   \qquad \vartheta=\lim_{\mu\to0}\mu q\in(0,4),
   \]
   等价于内尺度极限能量 \(\mathcal J_\infty\ge4\)。现有计算只支持其中
   \(\vartheta\in[0.2,2]\) 左右，而且主要沿 \(W=0\) 分支；后半段 \(2<\vartheta<4\) 和真正的 \(W\ne0\) 情形尚未被数值材料覆盖。

---

## 二、归一化与危险区间

代码中的
\[
I_R=\frac14(\mu^{-2}-R^{-4}),\qquad M_0=1+\frac2\mu,
\qquad M=M_0-q
\]
满足
\[
\frac{M_0^2}{4I_R}
=\frac{(2+\mu)^2R^4}{R^4-\mu^2}=K,
\]
与 I54/I55 的共形 Kähler常数完全一致。若 \(q=fM_0\)，则在约束精确时
\[
\operatorname{proj}=\frac{M^2}{4I_R}=K(1-f)^2,\qquad
\operatorname{gain}_q=Kf(2-f).
\]

对 \(R=2\)，可能达到 \(j<4\) 的投影必要区间下端为

| \(\mu\) | \(\delta_{\mu,2}\) | 最小目标 \(q\) |
|---:|---:|---:|
| \(0.1\) | \(1.006251\) | \(1.05\) |
| \(0.03\) | \(1.001875\) | \(6.7667\) |
| \(0.01\) | \(1.000625\) | \(20.1\) |

所以即使 \(\mu=0.1,f=0.05\) 的最浅搜索也已经越过该下端；其投影约为 \(3.9825<4\)。小 \(\mu\) 数据则深入其中。

另一方面，程序只取 \(f\le1\)，即 \(q\le M_0\) 和 \(M\ge0\) 的一半。完整 C1 危险区间是 \(0<q<2M_0\)；投影关于 \(q=M_0\) 对称，但其余非线性项并无对应对称性，因此 \(M<0\) 的一半不能由当前数据代替。

---

## 三、数据真正显示的尺度行为

### 3.1 低代价与固定环带分支

取共同拥有的 \(f\in\{0.1,0.35,0.6,1\}\)，并比较 \(w=0,\phi\) 初始取减号的延拓：

| \(f\) | broad \(j\), \(\mu=.03\to.01\) | fixed \(\mu j\), \(\mu=.03\to.01\) | fixed \(\sqrt\mu\,\phi_{\max}\), \(\mu=.03\to.01\) |
|---:|---:|---:|---:|
| 0.10 | \(8.660\to8.408\) | \(10.842\to10.419\) | \(1.437\to1.487\) |
| 0.35 | \(16.555\to16.099\) | \(34.409\to35.131\) | \(2.689\to2.782\) |
| 0.60 | \(22.158\to21.595\) | \(57.132\to60.802\) | \(3.536\to3.665\) |
| 1.00 | \(36.888\to35.455\) | \(95.883\to105.189\) | \(4.268\to4.751\) |

这很好地支持两个数值标度：
\[
j_{\rm low}=O(1),\qquad
j_{\rm fixed}\asymp\mu^{-1},\qquad
\phi_{\max,\rm fixed}\asymp\mu^{-1/2}.
\]

不过 family 名称不能直接解释为最终支撑集：

- 初值投影后已经不是严格紧支撑 bump；
- 优化阶段所有系数都可变；
- 输出文件没有保存
  \[
  \frac{T_{\phi,\{r\le L\sqrt\mu\}}}{T_\phi},
  \qquad
  \frac{T_{\phi,\{r\ge\rho\}}}{T_\phi}
  \]
  这样的尺度分布；
- `broad` 是最低 collar 基模，不是预先定义的内尺度初值，却给出了最低代价。

因此可从数据中提取的是“存在两个延拓分支，其能量和振幅具有上述标度”，而不是固定环带类的普遍极值规律。

另一个重要细节是：当 \(\mu=0.1\) 时
\[
[2r_0,3r_0]=[0.632,0.949],
\]
与固定环带 \([0.55,1.05]\) 基本重叠。`main_mu01.jsonl` 本身不能区分两种尺度；真正有区分力的是 \(\mu=.03,.01\) 的数据。

### 3.2 低代价分支由哪些余项支付

在 \(\mu=.01\) 的最佳 broad、\(w=0\) 数据中：

| \(f\) | \(\operatorname{proj}\) | \(R_X\) | \(R_Y\) | \(R_Z\) | \(j\) | \(\operatorname{gain}_q\) |
|---:|---:|---:|---:|---:|---:|---:|
| 0.10 | 3.2725 | 1.9414 | 0.6719 | 2.5226 | 8.4084 | 0.7676 |
| 0.35 | 1.7070 | 9.5245 | 0.7138 | 4.1534 | 16.0987 | 2.3332 |
| 0.60 | 0.6464 | 15.8595 | 1.2056 | 3.8833 | 21.5948 | 3.3937 |
| 1.00 | \(\approx0\) | 19.9530 | 7.8423 | 7.6592 | 35.4545 | 4.0401 |

这里 \(R_V=0\)。在 \(f\le0.6\) 时，主要支付来自投影后的 \(X\) 模式与 \(Z\) 方程，而不是 scalar square；到 \(M=0\) 时 \(Y\) 也明显增长。这与 I55 的“零矩并不降低总成本”完全一致。

但这仍是 \(w=0\) 数据。它支持的是共形梯度的 \(X\)–\(Z\) 补偿机制，而不是三轴 \(V_w\) 机制。

---

## 四、优化与数值解释中的实质问题

### 4.1 \(w=0\) 是精确对称驻点

当 `wseed=-1` 时，初始化 \(w=0\)，而泛函和 \(q\) 约束都对 \(w\mapsto-w\) 偶对称，因此梯度会把该分支精确保持在 \(w=0\)。这部分搜索从未离开共形双轴子空间。

带 `wseed=0` 的运行确实打破了该对称性，但最终通常有极小的 \(w_{\max},P_w,n\)。例如最佳 broad 解的有种子版本仅比 \(w=0\) 解略高。由此只能看出当前离散化和初值没有找到显著三轴补偿；不能把它解释成 \(w=0\) 在无限维固定-\(q\) 问题中的全局极小性。

### 4.2 停止条件只监测 \(q\)

增强拉格朗日循环在 \(q\) 误差足够小时停止，没有保存：

- 拉格朗日驻点残量；
- 各系数梯度范数；
- Hessian 的下降方向；
- 不同次数、不同延拓方向的复现值。

若达到 outer 次数上限，结果仍照常写出。部分 history 中 \(j\) 在最后几轮仍持续下降。因此这些数值是可采样本的上界，而不是受控精度的约束极小值。

两种初始化并没有出现脚本文档所说的“agreement”：在小 \(\mu\) 时 `fixed` 与 `broad` 相差两个数量级。这恰好说明吸引盆依赖很强。

### 4.3 正性只在离散点并以软罚项处理

输出的 `F_min_scaled` 在所有所示数据中仍大于零，所以求积节点上的 \(F\) 没有改变符号。但：

- 罚项只要求它接近 \(2\times10^{-3}\)，不是硬约束；
- 若低于该值，优化仍可接受；
- 该最小值只在 Cell 的离散节点上计算。

高 \(q\) 和固定环带分支常靠近这一层，例如 broad、\(f=1\) 时约 \(1.98\times10^{-3}\)，fixed 分支甚至降到 \(3\times10^{-4}\) 左右。连续区间上的 \(F>0\) 以及更高次数重采样尚未由 JSON 给出。对最低 broad 分支，罚项的数值贡献很小；对极高代价 fixed 分支，它会影响优化路径，但不足以解释 \(j\sim1/\mu\) 的主要量级。

### 4.4 collar 与光滑性依赖 `Cell.fields`

`cell_qsearch.py` 没有绕开原来的 Cell 基函数，因此若 `Cell.fields` 正确实施 bolt 条件和完整 CH collar，所有优化解都继承它们。另一方面，当前提供材料不含 `cell_opt.py` 的具体基函数定义，也没有输出端点 jet 残量。`smooth_bump` 的 C∞ 性只属于投影目标；有限次 Chebyshev 投影本身不会保留精确支撑。

### 4.5 两个“恒等误差”的独立性不同

`radial_identity_error` 比较直接 Ricci 残量积分与 \(X,Y,Z,V\) 投影分解，达到 \(10^{-12}\) 左右，确实说明同一离散求积上的代数实现一致。

但 `i54_identity_error` 不是独立曲率核验，因为
```python
B0_norm = (j_direct-4-base-A0_norm/12-ry)/4
```
把 \(B_0\) 定义为恰好补足 I54 恒等式的剩余量。随后再代回，误差接近机器精度是代数必然。因而：

- `B_pay` 可作为接受 I54 推导后的精确记账量；
- 它不能独立核验自对偶 Weyl 算子的数值实现；
- 接近零的 `i54_identity_error` 不能与 radial identity 视为两份独立证据。

此外，次数固定为 22、求积点固定为 700，而 \(\phi_{\max}\) 在部分分支达到 \(30\!-\!50\)。同一离散网格上的恒等闭合不能替代次数与求积加密后的积分收敛。

---

## 五、最自然的内尺度极限与加权 ODE 不等式

令
\[
r=\sqrt\mu\,x,\qquad
F_\mu(\sqrt\mu x)\to\mathcal F(x),\quad
w_\mu(\sqrt\mu x)\to W(x),\quad
\phi_\mu(\sqrt\mu x)\to\Phi(x),
\]
并假定这是有界振幅的内尺度分支，使
\(\mu e^{2\phi_\mu}\to0\)。定义
\[
\widehat T
 =2\int_1^\infty\frac{\mathcal F\dot\Phi^2}{x}\,dx,
\]
\[
\widehat P
 =\int_1^\infty\left[
 \frac{2\mathcal F\dot W^2}{x}
 +\frac{8(\cosh2W-1)}{x^3}
 +\frac{8\sinh^2(2W)}{x^3\mathcal F}
 \right]dx,
\qquad
\vartheta=\widehat T-\widehat P.
\]
则
\[
\mu q\to\vartheta,\qquad
q=fM_0\Longrightarrow \vartheta=2f.
\]

乘原残量以 \(\mu\) 后得到极限表达式
\[
\widehat E_V=-\frac12\ddot{\mathcal F}
             -\frac{5}{2x}\dot{\mathcal F},
\qquad
\widehat E_H=-\frac{\dot{\mathcal F}}x
             +\frac{4(1-\mathcal F)}{x^2},
\]
\[
\widehat D_0=\widehat E_V
 -3\mathcal F\ddot\Phi
 -(2\dot{\mathcal F}+3\mathcal F/x)\dot\Phi,
\]
\[
\widehat D_3=\widehat E_V
 -\mathcal F\ddot\Phi
 -(2\dot{\mathcal F}+5\mathcal F/x)\dot\Phi
 -2\mathcal F\dot\Phi^2,
\]
\[
\widehat D_H=\widehat E_H
 -\mathcal F\ddot\Phi
 -(\dot{\mathcal F}+5\mathcal F/x)\dot\Phi
 -2\mathcal F\dot\Phi^2,
\]
以及
\[
\widehat U=-\mathcal F\ddot W
-(\dot{\mathcal F}+3\mathcal F/x)\dot W
+\frac{4\sinh4W}{x^2\mathcal F}
-\frac{4\sinh2W}{x^2}.
\]
按 I55 相同方式定义
\(\widehat a_0,\widehat a_3,\widehat a_H,
\widehat X,\widehat Y,\widehat Z,\widehat V\)。bolt 条件变成
\[
\mathcal F(1)=0,\qquad \dot{\mathcal F}(1)=2,\qquad
W(1)=\dot W(1)=0,
\]
而内尺度局域分支在 \(x\to\infty\) 时趋于
\((\mathcal F,W,\Phi)=(1,0,0)\)。

原径向矩恒等式极限为
\[
\int_1^\infty\frac{\widehat X}{x}\,dx=2-\vartheta.
\]
因此极限泛函具有精确投影分解
\[
\mathcal J_\infty
=(2-\vartheta)^2+\widehat{\mathscr R},
\]
其中
\[
\begin{aligned}
\widehat{\mathscr R}={}&
\frac14\int_1^\infty x^3
 \left(\widehat X-\frac{4(2-\vartheta)}{x^4}\right)^2dx\\
&+\frac14\int_1^\infty x^3\widehat Y^2dx
+\frac12\int_1^\infty x^3\widehat Z^2dx
+2\int_1^\infty x^3\widehat V^2dx.
\end{aligned}
\]

于是完整、尺度正确而且常数尖锐的候选不等式是
\[
\boxed{
\widehat{\mathscr R}\ge
4-(2-\vartheta)^2
=\vartheta(4-\vartheta),
\qquad 0<\vartheta<4.
}
\]
它等价于
\[
\boxed{\mathcal J_\infty\ge4.}
\]

该常数在 \(\vartheta=0\) 处尖锐：取
\[
\mathcal F=1-x^{-2},\qquad W=\Phi=0,
\]
则 \(\widehat X=8x^{-4}\)、其余残量为零，故
\(\mathcal J_\infty=4\)。

用 \(s=\log x\)、\(A=x\dot\Phi\)、\(B=x\dot W\)，\(\widehat Z\) 与
\(\widehat V\) 还给出明确的一阶系统
\[
\partial_sA-2A-A^2
=-B^2+\frac{4\sinh^2(2W)}{\mathcal F^2}
-\frac{x^2\widehat Z}{2\mathcal F},
\]
\[
x^2\widehat V
=-\mathcal F\,\partial_sB
-(\partial_s\mathcal F)B
-2\mathcal F B-2\mathcal F AB
+\frac{4\sinh4W}{\mathcal F}-4\sinh2W.
\]
而危险矩为
\[
\vartheta=\int_0^\infty e^{-2s}
\left[
2\mathcal F(A^2-B^2)
-8(\cosh2W-1)
-\frac{8\sinh^2(2W)}{\mathcal F}
\right]ds.
\]
这正是所需加权 ODE 问题：由终端衰减、bolt 数据及
\(\widehat Z,\widehat V,\widehat X,\widehat Y\) 的平方，控制带
\(e^{-2s}\) 权的 Riccati 矩。

对于 \(W=0\)，该不等式是有限 \(\mu\) 共形 Kähler 下界的内尺度影像。真正新的数学内容是允许 \(W\ne0\) 后仍成立。当前数值中 \(W\) 基本消失，因而没有为这一部分提供强独立支持。

---

## 六、固定物理尺度对应的 ODE 形式

数据中的 \(j_{\rm fixed}\sim1/\mu\) 与下述类型的固定环带估计相符。若在 \([\rho,R]\) 上 \(\rho>0\) 固定、\(\mathcal F\) 保持一致椭圆，并有完整 collar 终端数据，则自然的估计形式是
\[
\boxed{
\left(
2\int_\rho^R\frac{F\phi'^2}{r}\,dr
-P_{w,[\rho,R]}
\right)_+
\le C
\int_\rho^Rr^3\bigl(X^2+Y^2+Z^2+V_w^2\bigr)\,dr .
}
\]
一旦固定环带承担 \(q\sim1/\mu\) 的非零比例，它立即给出
\(j\gtrsim1/\mu\)。

该形式与上面的 Riccati 系统一致，但当前 fixed 数据的
\(\phi_{\max}\sim\mu^{-1/2}\)，且 \(F\) 会接近退化层，所以常数是否保持一致尚无数值或解析材料。它适合描述“固定尺度正 \(q\) 必须由 ODE 残量支付”的机制，但目前的 \(1/\mu\) 表格只是这一机制的有限维表现。

---

## 七、最终科学判断

- 正 \(q\) 部门确实被进入，而且连 \(j<4\) 所需的更窄投影区间也被进入。
- 所有低代价结果仍远高于 \(K\)，径向分解显示主要由 \(X\) 与 \(Z\) 支付。
- 最佳结果属于 \(w=0\) 的已知共形 Kähler子类；三轴补偿没有被实质激活。
- `broad`/inner 的 \(O(1)\) 与 fixed 的 \(1/\mu\) 标度很鲜明，但它们是延拓分支的性质，尚不是按最终支撑尺度划分的变分定理。
- 最有价值的数学产物是上述内尺度极限：
  \[
  \mathcal J_\infty=(2-\vartheta)^2+\widehat{\mathscr R},
  \qquad
  \widehat{\mathscr R}\ge\vartheta(4-\vartheta).
  \]
  它保留了正确尺度、最佳阈值、bolt 数据、终端衰减以及
  \(X,Y,Z,V\) 的全部耦合，并明确指出未解决部分只在
  \(W\ne0\) 的加权 ODE coercivity。