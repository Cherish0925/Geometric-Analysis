# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 4,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step4_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step4_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the current O11 triaxial-cell theory and the new direct positive-q computational instrument/results. Check whether the numerical experiment genuinely enters the necessary I55 dangerous sector and whether its conclusions about inner-scale versus fixed-physical-scale compensation follow from the data. Inspect for normalization, optimization, smoothness/collar, positivity, or interpretation errors. Most importantly, identify the strongest mathematically extractable scaling conjecture/weighted ODE inequality suggested by the q>0 results, without treating finite-dimensional optimization as proof.

## Integrated Scientific Memo

# 核验结论：正 \(q\) 搜索进入了危险区，但尚未检验真正的三轴逃逸

## 1. 归一化与危险区间是正确的

代码采用
\[
I_R=\frac14(\mu^{-2}-R^{-4}),\qquad M_0=1+\frac2\mu,\qquad
q=T_\phi-P_w,\qquad M=M_0-q,
\]
并满足
\[
\frac{M_0^2}{4I_R}
=\frac{(2+\mu)^2R^4}{R^4-\mu^2}=K.
\]
因此 I55 分解确为
\[
j=\frac{(M_0-q)^2}{4I_R}+\mathscr R_{\rm rad},
\]
且相对 Kähler 基准的形式投影收益为
\[
K-\frac{(M_0-q)^2}{4I_R}
=\frac{q(2M_0-q)}{4I_R}.
\]

脚本约束 \(q=fM_0\)，其中 \(0<f\le1\)，故所有运行均在
\[
0<q\le M_0\subset(0,2M_0)
\]
这个 I55 危险区间内。进一步，可能达到 \(j<4\) 的必要下端
\[
\delta_{\mu,R}
=1+\frac2\mu\!\left(1-\sqrt{1-\frac{\mu^2}{R^4}}\right)
\]
在 \(R=2\) 时分别约为

\[
\delta_{0.1,2}=1.00625,\qquad
\delta_{0.03,2}=1.00188,\qquad
\delta_{0.01,2}=1.00063.
\]

数据的最小目标分别为 \(1.05,6.7667,20.1\)，全部越过该下端。因此“搜索从未进入必要的正 \(q\) 部门”已不再成立。

但搜索只覆盖 \(q\le M_0\)，尚未覆盖完整危险区间的另一半
\[
M_0<q<2M_0\qquad(M<0).
\]
投影项虽关于 \(q=M_0\) 对称，其余 \(X,Y,Z,V_w\) 非线性余项并无已知对称性，故不能由当前数据外推。

---

## 2. 数据没有实质进入未解决的三轴机制

低代价记录几乎都位于 \(w=0\) 或 \(w\) 极小的分支：

- `wseed=-1` 时初始化 \(w=0\)。由于目标泛函和 \(q\) 约束均对 \(w\mapsto-w\) 偶对称，自动微分在精确算术下将该子空间保持不变；这些运行根本没有离开双轴子类。
- 加入 \(w\)-seed 后，很多最终解仍只有
  \[
  w_{\max}\sim10^{-4}\!-\!10^{-3},
  \]
  且 \(P_w,n,R_V\) 极小，往往回到近双轴盆地。
- 最好的 `broad` 解均可取 \(w=0\)，于是是共形于 Kähler 填充的指标；I54 已严格证明该类 \(j\ge K\)。

所以，计算确实进入了**正 \(q\) 危险矩区间**，却主要通过 \(T_\phi>0,\ P_w=0\) 进入，而没有显著激活真正开放的有限振幅三轴竞争。它可靠地显示共形梯度的形式投影收益如何由 \(R_X,R_Z\)（以及靠近 \(M=0\) 时的 \(R_Y\)）偿还，但并未排除某个 \(W\neq0\) 的无限维逃逸分支。

例如 \(\mu=0.01\) 的最佳 `broad`, \(w=0\), 负号分支为：

\[
\begin{array}{c|ccccc}
f&q/M_0&\mathrm{proj}&R_X&R_Y&R_Z&j\\ \hline
0.10&0.10&3.2725&1.9414&0.6719&2.5226&8.4084\\
0.35&0.35&1.7070&9.5245&0.7138&4.1534&16.0987\\
0.60&0.60&0.6464&15.8595&1.2056&3.8833&21.5948\\
1.00&1.00&\approx0&19.9530&7.8423&7.6592&35.4545
\end{array}
\]
而 \(R_V=0\)。这直接确认：消掉径向矩 \(M\) 并不能消掉总成本。

---

## 3. 内尺度与固定物理尺度：数据支持“两个延拓盆地”，不是普遍定理

### 3.1 可可靠提取的标度

小 \(\mu\) 数据显示两个清楚的数值分支。

低代价 `broad` 分支：
\[
j=O(1),\qquad \|\phi\|_\infty=O(1).
\]

`fixed` 初始化所得高代价分支：
\[
j\asymp\mu^{-1},\qquad
\|\phi\|_\infty\asymp\mu^{-1/2}.
\]

例如 \(w=0\)、负号分支：

\[
\begin{array}{c|cc|cc}
f&
j_{\rm broad}(\mu=.03)&j_{\rm broad}(\mu=.01)&
\mu j_{\rm fixed}(\mu=.03)&\mu j_{\rm fixed}(\mu=.01)\\ \hline
0.10&8.660&8.408&10.842&10.419\\
0.35&16.555&16.099&34.409&35.131\\
0.60&22.158&21.595&57.132&60.802\\
1.00&36.888&35.455&95.883&105.189
\end{array}
\]

并且 fixed 分支上的 \(\sqrt\mu\,\phi_{\max}\) 大致保持 \(O(1)\)。这与简单尺度分析一致：若固定物理环带上 \(F\asymp1\)，要产生
\[
T_\phi=2\int\frac{F\phi'^2}{r}\,dr\asymp\mu^{-1},
\]
则典型振幅应为 \(\mu^{-1/2}\)，而二阶残量平方积分自然产生约 \(\mu^{-1}\) 的代价。

### 3.2 不能从数据推出的结论

不能据此声称“固定物理尺度补偿必然支付 \(1/\mu\)，而内尺度补偿必然是 \(O(1)\)”：

1. `family` 只决定初值；之后 \(F,w,\phi\) 的全部系数共同优化，没有最终支撑约束。
2. 有限 Chebyshev 投影不保留 bump 的严格紧支撑。
3. JSON 没有保存诸如
   \[
   \frac{T_{\phi,\{r\le L\sqrt\mu\}}}{T_\phi},
   \qquad
   \frac{T_{\phi,\{r\ge\rho\}}}{T_\phi}
   \]
   的尺度分布，无法确认最终解仍在哪个尺度。
4. 最低代价解来自 `broad` 基模，而非命名为 `inner` 的初值；这表明名称不能当作最终几何分类。
5. \(\mu=0.1\) 时所谓 inner 支撑
   \[
   [2\sqrt\mu,3\sqrt\mu]=[0.632,0.949]
   \]
   与 fixed 支撑 \([0.55,1.05]\) 几乎重叠；只有 \(\mu=.03,.01\) 才真正区分尺度。
6. fixed 与 broad 结果并不“agreement”；小 \(\mu\) 时相差数个数量级，显示的是强盆地依赖。

因此，数据支持的是：

> 固定次数离散化中存在一个 \(O(1)\) 低代价盆地和一个近似 \(1/\mu\) 的高代价盆地；它们与内尺度和固定物理尺度的启发式相符。

它不证明任一受支撑约束的无限维极小值标度。

---

## 4. 数值和实现层面的核验

### 4.1 径向恒等式核验有效，I54 “误差”不是独立核验

`radial_identity_error` 比较直接 Ricci 残量积分与 I55 的 \(X,Y,Z,V_w\) 平方分解，误差约 \(10^{-12}\) 或更小。这是同一离散网格上的有意义代数一致性检查，并支持 q、投影和各余项的归一化。

但
```python
B0_norm = (j_direct-4-base-A0_norm/12-ry)/4
```
是用 I54 恒等式反解 \(B_0\)。随后再计算 `i54_identity_error`，其近机器零基本是代数必然。因此：

- `B_pay` 在接受 I54 推导后可作为记账量；
- 它不是独立计算的 \(W^+\) 余项；
- `i54_identity_error` 不能被描述成第二个独立曲率实现核验。

### 4.2 约束优化没有给出受控极小值

增强拉格朗日循环的停止条件只检查 \(q\)-误差，不检查：

- 完整 KKT/拉格朗日梯度范数；
- Hessian 负方向；
- 系数空间驻点误差；
- 从大 \(q\) 反向延拓的一致性。

部分运行达到 outer 上限时仍在下降，随后仍被写入数据。因此每个记录只是一个可行或近可行竞争者，给出有限维约束下确界的**上界**，不是其数值证明，更不是无限维下界。

### 4.3 正性是软的、离散的

所有展示记录在求积节点上有 \(F>0\)，但惩罚为
\[
10^7\bigl(2\times10^{-3}-F_{\min}^{\rm scaled}\bigr)_+^2
\]
而不是硬约束。高 \(q\) 分支常贴近或越过该层：

- 若 `F_min_scaled < 2\times10^{-3}`，结果实际上包含非零人工罚项，但输出的 `j` 不包含该罚项；
- 最小值只在离散节点上检查，不能保证节点间 \(F>0\)；
- fixed 小 \(\mu\) 分支可降至 \(3\times10^{-4}\) 量级，已明显受近退化几何和罚项路径影响。

低代价 broad 分支在 \(f\le0.35\) 时远离该层；在 \(f=.6,1\) 时则也接近它。任何有关高 \(q\) 极限的结论都需要连续区间正性验证及次数/求积加密。

### 4.4 collar 和 bolt 光滑性不能由本输入完全独立核验

脚本使用 `Cell.fields` 的同一基底，因而没有显式破坏原有 bolt/collar 条件；但当前材料未提供 `cell_opt.py`。故无法从本输入独立检查：

\[
F(r_0)=0,\quad F'(r_0)=2/r_0,\quad
w(r_0)=w'(r_0)=0,
\]
以及 collar 上 \(F=1+r^2/6,\ w=\phi=0\) 的精确实施方式。`smooth_bump` 的 \(C^\infty\) 性只属于初始化目标，不足以证明投影后紧支撑。应把“精确 collar/bolt 类”视为依赖 `Cell` 实现的条件，而不是由这些 JSON 自证。

---

## 5. 最强可提炼的标度猜想：内尺度极限 coercivity

令
\[
r=\sqrt\mu\,x,\qquad
F_\mu(\sqrt\mu x)\to\mathcal F(x),\quad
w_\mu(\sqrt\mu x)\to W(x),\quad
\phi_\mu(\sqrt\mu x)\to\Phi(x),
\]
考虑有界振幅、局域于内尺度的分支，并设
\[
\vartheta=\lim_{\mu\to0}\mu q.
\]
当 \(q=fM_0\) 时，
\[
\vartheta=2f.
\]

定义
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

在 \(\mu e^{2\phi_\mu}\to0\) 的内尺度极限下，缩放后的基本残量为
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
-\left(2\dot{\mathcal F}+\frac{3\mathcal F}{x}\right)\dot\Phi,
\]
\[
\widehat D_3=\widehat E_V
-\mathcal F\ddot\Phi
-\left(2\dot{\mathcal F}+\frac{5\mathcal F}{x}\right)\dot\Phi
-2\mathcal F\dot\Phi^2,
\]
\[
\widehat D_H=\widehat E_H
-\mathcal F\ddot\Phi
-\left(\dot{\mathcal F}+\frac{5\mathcal F}{x}\right)\dot\Phi
-2\mathcal F\dot\Phi^2,
\]
\[
\widehat U=-\mathcal F\ddot W
-\left(\dot{\mathcal F}+\frac{3\mathcal F}{x}\right)\dot W
+\frac{4\sinh4W}{x^2\mathcal F}
-\frac{4\sinh2W}{x^2}.
\]
由这些按 I55 定义
\(\widehat a_0,\widehat a_3,\widehat a_H,\widehat X,
\widehat Y,\widehat Z,\widehat V\)。

bolt/终端条件应为
\[
\mathcal F(1)=0,\quad \dot{\mathcal F}(1)=2,\quad
W(1)=\dot W(1)=0,
\]
以及局域分支的
\[
(\mathcal F,W,\Phi)\to(1,0,0)\qquad(x\to\infty).
\]

径向矩恒等式缩放为
\[
\int_1^\infty\frac{\widehat X}{x}\,dx=2-\vartheta.
\]
于是极限能量具有精确分解
\[
\mathcal J_\infty=(2-\vartheta)^2+\widehat{\mathscr R},
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

因此最强、尺度正确且阈值常数精确的猜想是
\[
\boxed{\widehat{\mathscr R}\ge
4-(2-\vartheta)^2=\vartheta(4-\vartheta),
\qquad 0<\vartheta<4,}
\]
等价于
\[
\boxed{\mathcal J_\infty\ge4.}
\]

其常数在 \(\vartheta=0\) 处确实尖锐：取
\[
\mathcal F=1-x^{-2},\qquad W=\Phi=0,
\]
则 \(\widehat X=8x^{-4}\)，其余残量为零，故
\(\mathcal J_\infty=4\)。

当前数据只覆盖 \(f\le1\)，即
\[
0<\vartheta\le2,
\]
并且低代价数据主要在 \(W=0\)。所以数值只支持这一猜想的前半区及其已知共形 Kähler 截面；真正新的对象是 \(W\neq0\) 时的全区间 \(0<\vartheta<4\)。

---

## 6. 更具体的加权 ODE 形式

令
\[
s=\log x,\qquad A=x\dot\Phi,\qquad B=x\dot W.
\]
由 \(\widehat Z\) 和 \(\widehat V\) 可写出耦合的一阶/Riccati 系统
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
危险矩则是
\[
\vartheta=\int_0^\infty e^{-2s}\!
\left[
2\mathcal F(A^2-B^2)
-8(\cosh2W-1)
-\frac{8\sinh^2(2W)}{\mathcal F}
\right]ds.
\]

这给出最精确的证明目标：

> 用 bolt 数据、无穷远终端条件以及
> \(\widehat X,\widehat Y,\widehat Z,\widehat V\) 的加权平方，
> 控制上述 \(e^{-2s}\)-加权 Riccati 矩，并推出
> \(\widehat{\mathscr R}\ge\vartheta(4-\vartheta)\)。

它比单独估计 \(T_\phi\)、\(P_w\)、\(M\) 或 scalar mean 更符合 I55 的零矩反例和现有数据中的支付结构。

---

## 7. 固定尺度分支所提示的较弱估计

若在固定环带 \([\rho,R]\)、\(\rho>0\) 上保持一致椭圆性
\[
0<c\le F\le C
\]
及适当系数控制，并使用 collar 终端数据，则数值标度提示
\[
\boxed{
\left(
2\int_\rho^R\frac{F\phi'^2}{r}\,dr
-P_{w,[\rho,R]}
\right)_+
\le C_{\rho,R}
\int_\rho^R r^3
\bigl(X^2+Y^2+Z^2+V_w^2\bigr)\,dr .
}
\]
若固定环带承担 \(q\sim\mu^{-1}\) 的非零比例，该估计立即给出
\[
j\gtrsim\mu^{-1}.
\]

但当前 fixed 分支恰会使 \(F\) 接近退化层，且 \(\phi_{\max}\sim\mu^{-1/2}\)，所以不能从现有数据断言常数 \(C_{\rho,R}\) 对这些解保持一致。该式应被视为固定尺度机制的候选 ODE 估计，而非已验证结论。

---

## 总判断

1. **是：**实验确实进入 I55 必要的正 \(q\) 危险区，且越过了 \(j<4\) 的投影必要下端。  
2. **否：**它尚未覆盖完整 \(0<q<2M_0\)，也没有实质探索有限振幅 \(w\neq0\) 的三轴逃逸。  
3. **数据支持但不证明：**存在 \(O(1)\) 的内尺度型低代价盆地和 \(j\sim1/\mu\)、\(\phi_{\max}\sim\mu^{-1/2}\) 的固定尺度型高代价盆地。由于优化不保持最终支撑，这不能升级为尺度分类定理。  
4. **主要解释错误风险：**把 family 名称当最终支撑、把 \(q\)-可行性当优化收敛、把 inferred \(B_0\) 的 I54 闭合当独立验证、以及忽略软正性和近退化 \(F\)。  
5. **最强可提炼数学对象：**
   \[
   \mathcal J_\infty=(2-\vartheta)^2+\widehat{\mathscr R},
   \qquad
   \widehat{\mathscr R}\ge\vartheta(4-\vartheta),
   \quad 0<\vartheta<4.
   \]
   它保留正确尺度、最佳阈值、bolt/collar 极限数据和全部 \(X,Y,Z,V\) 耦合；真正未解决的核心是 \(W\neq0\) 的加权 ODE coercivity。