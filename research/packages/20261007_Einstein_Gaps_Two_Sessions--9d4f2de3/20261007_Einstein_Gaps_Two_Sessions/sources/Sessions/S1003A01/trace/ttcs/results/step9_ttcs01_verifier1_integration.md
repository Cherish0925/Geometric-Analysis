# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 9,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step9_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step9_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the Step-9 construction note as a differential geometer and verify the logical chain for the proposed finite-scale perpendicular complex-hyperbolic blow-up cell: normalization/rescaling from J6 to the Ric=-g cell cost, smooth bolt conditions, C2-to-smooth exact-collar perturbation, residual-finiteness supply of a fixed large embedded ball, and the I54 single-blowup transfer to a balanced-family coefficient below four. Identify any mathematical flaw that would invalidate the route, and separate it from the single remaining computational enclosure. Use the actual inherited I54 source and the Step-7/8 derivations. Do not treat floating-point evidence as proof.

## Integrated Scientific Memo

# 核验结论

在冻结剖面满足严格不等式
\[
J_6(g)<8\pi^2
\]
得到可靠区间证明的前提下，Step-9 的几何—拓扑传递链成立：

\[
\text{冻结的 perpendicular 剖面}
\longrightarrow
\text{光滑 exact-CH 单 blow-up cell}
\longrightarrow
\text{固定大球有限覆盖}
\longrightarrow
\limsup_j\frac{\alpha(M_j)}{h_j}<4.
\]

未发现另一处会使路线失效的数学错误。当前唯一实质性未闭合命题是冻结 \(X=8\) 剖面的严格能量符号：
\[
\boxed{\quad J_6/(8\pi^2)<1.\quad}
\]
现有浮点重构是很强的证据，但不是证明。

需要同时修正三点措辞：

1. 存档剖面直接接到 CH 外部时仅为 \(C^2\)，不是 I54 定义中的光滑 cell；必须先作 Step-7 的平坦 cutoff。
2. 数值 \(3.99921444\) 对应未平滑极限剖面；固定光滑 cell 的系数有 \(O(\delta^3)\) 改动，但仍可严格小于 \(4\)。
3. 剩余有限性论证给出的是适当重新选择的 existential balanced cover sequence，并不自动适用于任意预先指定的 tower。

---

## 1. 缩放与 I54 cell cost

令
\[
\widetilde g=6g.
\]
常数缩放不改变 Levi–Civita 联络，故作为 \((0,2)\)-张量，
\[
\operatorname{Ric}_{\widetilde g}=\operatorname{Ric}_g.
\]
若背景满足 \(\operatorname{Ric}_g=-6g\)，则
\[
\operatorname{Ric}_{\widetilde g}=-\widetilde g,\qquad
\operatorname{Ric}_{\widetilde g}+\widetilde g
=\operatorname{Ric}_g+6g.
\]
四维中
\[
|T|_{\widetilde g}^2=6^{-2}|T|_g^2,\qquad
dV_{\widetilde g}=6^2dV_g,
\]
所以
\[
\int|\operatorname{Ric}_{\widetilde g}+\widetilde g|_{\widetilde g}^2\,dV_{\widetilde g}
=
\int|\operatorname{Ric}_g+6g|_g^2\,dV_g.
\]
这正是 I54 §1–2 中 \(\operatorname{Ric}=-g\) 归一化的 cell cost \(J_1\)。

同时
\[
\operatorname{Ric}+6g
=\operatorname{Ric}^{\circ}+\frac{s+24}{4}g,
\qquad |g|^2=4,
\]
故
\[
J_6=P+\frac14\int(s+24)^2,\qquad
P=\int|\operatorname{Ric}^{\circ}|^2.
\]
因此记录中的 `J` 确实是 \(J_1/(8\pi^2)\) 的候选值。

---

## 2. 螺栓光滑性、拓扑和正定性

令 \(y=x-x_0\)。脚本剖面在 bolt 附近满足
\[
F=f_1y+O(y^2),\qquad
G=g_1y+O(y^2),\qquad
w=O(y^2).
\]
其中 coefficient shift 代数上强制
\[
q_F(x_0)+q_G(x_0)=0,
\]
因而
\[
f_1g_1=1
\]
是精确恒等式，不依赖打印出的近似小数。

由
\[
dt=\frac{dy}{2\sqrt G}
\]
得
\[
y=g_1t^2+O(t^4),
\qquad
F=t^2+O(t^4).
\]
又因为 \(w=O(y^2)=O(t^4)\)，
\[
xe^w-x=O(t^4).
\]
所以局部度量为
\[
dt^2+\bigl(t^2+O(t^4)\bigr)\sigma_1^2
+\bigl(x_0+O(t^2)\bigr)(\sigma_2^2+\sigma_3^2)
+O(t^4)(\sigma_3^2-\sigma_2^2).
\]
这里：

- \(F'G'=1\) 是无锥关系；
- 非塌缩二维切向度量在 bolt 上为圆形；
- 无迹各向异性为 \(O(t^4)\)，满足 weight-four 光滑条件。

因此这是光滑普通 blow-up bolt。`wpow=2` 是关键；`wpow=1` 一般不光滑。验证产物最好显式记录 `wpow=2` 和 \(w'(x_0)=0\)，而不只记录 \(w(x_0)=0\)。

塌缩槽从 \(\sigma_3\) 换成 \(\sigma_1\) 只是保持结构方程与取向的循环置换；底层相对拓扑仍是
\[
D\#\overline{\mathbb{CP}}^{\,2},
\qquad k=q=1.
\]
没有证据表明发生取向翻转或变成 \(+1\) sphere。

### 正定性无需区间计算

令
\[
S(u)=10u^3-15u^4+6u^5.
\]
因
\[
S'(u)=30u^2(1-u)^2\ge0,\qquad 0\le S(u)\le1,
\]
脚本公式直接给出，在 \(x_0<x\le X\) 上
\[
F=(x-x_0)e^{q_F}+x_0S(u)>0,
\]
\[
G=\bigl[(x-x_0)+(x^2+x_0)S(u)\bigr]e^{q_G}>0,
\]
以及
\[
x>0,\qquad xe^w>0.
\]
所以原始剖面的全区间正定性是解析事实，不是仍待验证的网格命题。20,001 点检查和 Arb 正下界仅是佐证。

---

## 3. \(C^2\) 拼接到 smooth exact collar

设相对于 CH 剖面的偏差为
\[
q=(F-x,\;G-x(1+x),\;w-\log(1+x)).
\]
由于 smoothstep 在 \(u=1\) 与常数 \(1\) 匹配到二阶，且自由项含 \((1-u)^3\)，在 \(\rho=X-x\to0\) 时
\[
q=O(\rho^3),\qquad q'=O(\rho^2),\qquad q''=O(\rho).
\]
因此直接拼接得到的是 \(C^2\) 度量，而非 \(C^\infty\) 度量。

取标准 cutoff \(\chi_\delta\)，在 \(x\le X-2\delta\) 为 \(1\)，在 \(x\ge X-\delta\) 为 \(0\)，并令
\[
q_\delta=\chi_\delta q.
\]
在过渡带中
\[
q_\delta=O(\delta^3),\qquad
q_\delta'=O(\delta^2),\qquad
q_\delta''=O(\delta).
\]
外端几何非退化，而 Ricci 与标量曲率平滑依赖于二阶 jet。由于 CH 上
\[
\operatorname{Ric}^{\circ}=0,\qquad s+24=0,
\]
过渡带上的 defect 为 \(O(\delta)\)，带宽为 \(O(\delta)\)，所以
\[
|P(g_\delta)-P(g)|+
|J_6(g_\delta)-J_6(g)|
\le C\delta^3.
\]
这正是 Step-7 (5.2) 的机制。

正定性在 cutoff 后仍保持：\(F_\delta,G_\delta\) 可取原剖面与 CH 正函数的凸组合，而 \(xe^{w_\delta}>0\) 自动成立。

因此，只要严格证明
\[
J_6(g)=8\pi^2(1-\varepsilon_0),\qquad\varepsilon_0>0,
\]
就存在固定且充分小的 \(\delta>0\)，使光滑 exact-collar cell 满足
\[
J_6(g_\delta)<8\pi^2.
\]
存在性证明不需要显式计算 cutoff 常数；若要声称某个具名光滑剖面的具体数值，则需要给出该常数及选定的 \(\delta\)。

---

## 4. 唯一剩余的计算封闭

Step-7 的精确相对恒等式给出
\[
\frac{P}{8\pi^2}-1=S_1+S_2+S_3+C_3,
\]
其中 \(S_i\) 为平方积分，而 \(C_3\) 是带符号三次项。对冻结的 \(X=8\) 剖面，浮点结果为
\[
S_1+S_2+S_3
=0.0032100252216878,
\]
\[
C_3=-0.0041013224880949,
\]
所以
\[
\frac{P}{8\pi^2}-1
\approx-8.91297266407\times10^{-4}.
\]
标量平方贡献为
\[
\frac{J_6-P}{8\pi^2}
\approx7.5404017317\times10^{-6},
\]
从而
\[
\frac{J_6}{8\pi^2}
\approx0.99911624313525,
\]
即
\[
\varepsilon_0\approx8.8375686475\times10^{-4}.
\]

两个实现及多个求积阶数之间的一致性表明公式实现很可能正确，也排除了普通浮点漂移导致符号翻转的解释；但这仍不是严格证明。

需要认证的精确命题可以压缩为
\[
\boxed{
\Delta:=
S_1+S_2+S_3+C_3+
\frac1{32\pi^2}\int(s+24)^2\,dV<0.
}
\]
可将 JSON 十进制系数解释为精确有理数或 dyadic 数，再对 \(\Delta\) 给出外包区间。

最自然的验证方式是：

1. 在 bolt 的短区间写
   \[
   F=y\widehat F,\qquad G=y\widehat G,\qquad w=y^2\widehat w,
   \]
   先符号消去 \(\sqrt y\) 和所有可消去的 \(0/0\)；
2. 用解析 Taylor model 处理该初始区间；
3. 在其余紧区间对 Step-7 已简化的相对密度和标量平方密度作 Arb/MPFI 外包积分。

由于正定性已经解析证明，且 cutoff 只需定性 \(O(\delta^3)\) 连续性，这个能量外包就是当前路线唯一实质性缺口。

---

## 5. 剩余有限性提供固定大嵌入球

设原紧致 CH 曲面为
\[
X=\Gamma\backslash\mathbb{CH}^2.
\]
固定包含 cell 和 smoothing buffer 的半径 \(R\)，并取 \(p\in\mathbb{CH}^2\)。集合
\[
S_R=\{\gamma\in\Gamma\setminus\{1\}:d(p,\gamma p)\le2R\}
\]
因 proper discontinuity 为有限集。

对每个 \(\gamma\in S_R\)，剩余有限性给出有限指数子群排除 \(\gamma\)。取有限交得 \(H<\Gamma\)，满足
\[
H\cap S_R=\varnothing.
\]
于是 \(B_R(p)\) 在
\[
X_*=H\backslash\mathbb{CH}^2
\]
中嵌入。

任意进一步有限覆盖 \(X_j\to X_*\) 中，该球有与覆盖次数相同数量的互不相交 lift，故球数与
\[
A_j=c_1^2(X_j)
\]
成正比。balanced family 中
\[
Q_j=A_jh_j=o(A_j),\qquad
k_j\sim\frac29Q_j,
\]
所以需要的 large-cell balls 只有 \(o(A_j)\) 个，供应充分；其余 handle surgeries 同样只需 \(o(A_j)\) 个位置。

半径换算正确：
\[
r_{-6}=\operatorname{arsinh}\sqrt X,\qquad
r_{-1}=\sqrt6\,r_{-6}.
\]
在 \(X=8\) 时
\[
r_{-1}\approx4.32,
\]
再加固定 smoothing buffer。

这证明存在适当选择的 balanced sequence。不能把它表述为任意预先固定的 cover tower 都含有所需大球。

---

## 6. I54 的 single-blowup transfer

I54 §2 对固定 cell 给出
\[
\mathcal E
=
\frac{4n_jJ-n_j^2t^2/v_j}
     {4v_j+n_j(J-2t)}.
\]
当 \(n_j/A_j\to0\) 时，二次项相对于 \(h_j\) 消失，得到 cell 的一阶贡献
\[
\frac{J}{2\pi^2q}.
\]

balanced family 满足
\[
\frac{k_j}{Q_j}\to\frac29,\qquad
\frac{\ell_j}{Q_j}\to\frac7{36}.
\]
单 blow-up 使用成本 \(J_1\)，handle 使用继承的 shrinking construction，每个 handle 的权重 \(q=4\)，成本为 \(32\pi^2\)。因此
\[
\limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}
\le
\frac1{2\pi^2}
\left(
\frac29J_1+\frac7{36}\,32\pi^2
\right)
=
\frac{28}{9}+\frac{J_1}{9\pi^2}.
\]
若
\[
J_1=8\pi^2(1-\varepsilon),
\]
则
\[
\limsup_j\frac{\alpha(M_j)}{h_j}
\le4-\frac{8\varepsilon}{9}<4.
\]

以未平滑冻结剖面的浮点值计算，
\[
4-\frac89\varepsilon_0
\approx3.9992144383.
\]
对固定 smooth cutoff，应写成
\[
\frac{28}{9}+\frac{J_{1,\delta}}{9\pi^2},
\qquad
J_{1,\delta}=J_{1,0}+O(\delta^3),
\]
并选足够小的 \(\delta\) 保持严格小于四。

---

## 7. 与 I54、Step-7/8 的一致性

该候选不与已证明的下界冲突：

- Step-8 的 Kähler period law 和 I54 §3–5 排除的是 Kähler、conformally Kähler 或 biaxial 路线；当前 perpendicular 剖面是三轴且不属于这些类别。
- I54 §6.1 的 conformal almost-Kähler reduction 留有明确的中间补偿窗口，并未证明所有 triaxial cell 都满足 \(J\ge8\pi^2\)。
- I54 §7 的一般下界只限制 subthreshold cell 的体积窗口，不排除该候选。
- I54 §8 的“无 smooth interior critical point”不相关：此剖面不要求是 unrestricted fixed-collar 泛函的临界点。
- Step-8 的
  \[
  R^+|_{\omega^\perp}=0
  \]
  说明 perpendicular 方向没有一阶响应；观察到的 \(O(x_0^2)\) deficit 与此相容，但并不自行证明二阶符号。

---

## 8. 代码层面的验证陷阱

这些不否定 Step-9 的专用验证结果，但会破坏直接复现：

1. `perp_dual_cost.py` 的 `make_cell` 硬编码 `X=1.0`。因此用其 `eval` 读取 \(X=8\) 或 \(X=16\) 记录会静默评估错误的剖面。Step-9 数值来自另一个 verifier，且 collar 数据明确为 \(X=8\)，所以当前报告值不受此 bug 影响。
2. `eval` 对缺失 `wpow` 的记录默认使用 `wpow=1`，会把光滑 bolt 重新解释为一般不光滑的剖面。
3. `o11_perp_cell.py` 中 “\(G\to x+x^2\) (C1)” 的注释已过时；实际构造在外端匹配到二阶。
4. \(X=16\) witness 的文件名在 Step-9 中疑有 `x00.01`/`x0.01` 拼写不一致。

---

# 最终判定

缩放归一化、bolt 光滑性、普通 \((-1)\)-blow-up 拓扑、\(C^2\)-到 smooth exact-collar 改造、固定大球的剩余有限性供应，以及 I54 的 single-blowup 系数传递均成立。正定性也可由剖面公式直接证明，不属于剩余数值任务。

唯一尚未证明的是冻结剖面的严格能量外包：
\[
J_6/(8\pi^2)<1.
\]
一旦给出该区间证书，就严格得到一个 smooth exact-CH 单 blow-up cell，并由 I54 推出某个 balanced family 满足
\[
\limsup_j\frac{\alpha(M_j)}{h_j}<4.
\]
现有浮点证据不能替代这一最后的 enclosure。