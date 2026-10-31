# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 11,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step11_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step11_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently verify the geometric and global deduction from the frozen C² cell to a smooth exact-CH-collar blow-up cell and then to a balanced sequence with coefficient below four. Check bolt smoothness with dσ_i=2σ_j∧σ_k and ∫σ123=2π², topology/orientation of collapsing σ1 versus the aligned blow-up, the O(δ³) exact-collar smoothing, constant rescaling Ric=-6g to Ric=-g, I54 transfer arithmetic, and residual-finite fixed-ball supply. Also analyze the consequence of the inherited exact handle-only formula α=4h/(1+h): prove or refute that every pure-handle exact-CH cell must have J≥32π²ℓ, and formulate the distinct mixed-cell interaction question without conflating it with isolated handle improvement.

## Integrated Scientific Memo

# 核验结论

冻结的垂直 \(C^2\) 剖面确实可转化为光滑、具有精确复双曲外 collar 的单 blow-up cell；常数缩放、I54 转移及有限覆盖中的固定大球供给均成立。因而存在平衡序列满足
\[
\limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}<4.
\]
另外，由纯 handle 家族的精确全度量公式可严格推出：任何纯 handle、exact-CH cell 都满足
\[
\boxed{J\ge 32\pi^2\ell}.
\]
因此“孤立 handle cell 能否低于 \(32\pi^2\)”并非开放问题；真正独立的开放问题是 blow-up 与 handle 在同一混合 cell 内是否产生严格非加性降价。

---

## 1. Bolt 光滑性、周期与体积归一化

令 \(y=x-x_0\)。由于
\[
u=\frac{\log(1+y/x_0)}{\ell}
=\frac{y}{x_0\ell}+O(y^2),\qquad S(u)=O(y^3),
\]
且修正后的系数满足
\[
q_F(0)+q_G(0)=0,
\]
故
\[
F=f_1y+O(y^2),\qquad G=g_1y+O(y^2),\qquad
f_1g_1=1,\qquad w=O(y^2).
\]

取测地径向坐标
\[
dt=\frac{dx}{2\sqrt G}.
\]
则
\[
y=g_1t^2+O(t^4),
\]
从而
\[
F=t^2+O(t^4),\qquad
x=x_0+g_1t^2+O(t^4),\qquad
xe^w=x_0+g_1t^2+O(t^4),
\]
并且
\[
x-xe^w=O(t^4).
\]

在归一化
\[
d\sigma_i=2\sigma_j\wedge\sigma_k,\qquad
\int_{S^3}\sigma_1\wedge\sigma_2\wedge\sigma_3=2\pi^2
\]
下，\(\sum_i\sigma_i^2\) 是单位圆三球度量，\(\sigma_1\)-对偶 Hopf 圆的周期为 \(2\pi\)。因此：

* 折叠方向的 \(F=t^2+O(t^4)\) 正是无锥角条件；
* \(\operatorname{span}\{\sigma_2,\sigma_3\}\) 是 isotropy 的权 \(2\) 实表示，其无迹对称张量具有权 \(4\)，所以平滑性要求
  \[
  h_2-h_3=O(t^4),
  \]
  而 \(w=O(y^2)=O(t^4)\) 恰好满足该条件；
* 各系数均为 \(t^2\) 的解析函数，故 bolt 是光滑二维球，而非 orbifold bolt。

体积形式为
\[
dV_g
=\frac{x e^{w/2}}2\sqrt{\frac FG}\,
dx\wedge\sigma_1\wedge\sigma_2\wedge\sigma_3,
\]
轨道积分后
\[
\boxed{dV_g=\pi^2x e^{w/2}\sqrt{\frac FG}\,dx.}
\]
这与 Step 10 的积分密度及 \(8\pi^2\) 归一化一致。

---

## 2. 折叠 \(\sigma_1\) 的拓扑与定向

\(\sigma_1\) 与通常 aligned 模型中的 \(\sigma_3\) Hopf 圆通过 \(SU(2)\) 的共轭相互转换。相应的三轴循环置换属于 \(SO(3)\)，保持
\[
\sigma_1\wedge\sigma_2\wedge\sigma_3
\]
及四维定向，并同伦于恒等映射。

可在 bolt 邻域使用该共轭，在自由轨道区沿 \(SU(2)\) 中的一条路径逐渐退回恒等，从而得到外 collar 上逐点为恒等的定向微分同胚。故垂直 cell 与 aligned ordinary blow-up cell 定向微分同胚：
\[
\boxed{C\cong D\#\overline{\mathbb{CP}}^{\,2}},
\qquad (k,\ell,q)=(1,0,1).
\]

这只是拓扑等价，不是 collar 几何的等距变换：CH collar 只保留特定 Hopf 方向的额外对称。因此垂直 cell 可以逃离材料中针对 aligned/biaxial 或相应 conformally almost-Kähler bolt 的排除结论，并不与那些结论矛盾。

---

## 3. 从 \(C^2\) 拼接到光滑 exact-CH collar

令
\[
d_F=F-x,\qquad
d_G=G-(x+x^2),\qquad
d_w=w-\log(1+x).
\]
由
\[
1-S=(1-u)^3(1+3u+6u^2),\qquad
q_F,q_G=O((1-u)^3),
\]
可得在 \(x=X\)：
\[
d_\bullet^{(k)}(x)=O((X-x)^{3-k}),\qquad k=0,1,2.
\]
所以直接接 CH 剖面得到 \(C^2\) 度量，且二阶 jet 完全匹配。

取
\[
\chi_\delta(x)=\chi\!\left(\frac{X-x}{\delta}\right),
\qquad
d_{\bullet,\delta}=\chi_\delta d_\bullet.
\]
Leibniz 公式给出
\[
\left|\partial_x^k(\chi_\delta d_\bullet)\right|
\le C\delta^{3-k},\qquad k\le2.
\]
因此在 \(B_\delta=[X-\delta,X]\) 上
\[
\|g_\delta-g_{\rm CH}\|_{C^2}
+\|g-g_{\rm CH}\|_{C^2}\le C\delta.
\]
该区域远离 bolt，故充分小的 \(\delta\) 保持正定性。Ricci 缺陷是度量二阶 jet 的光滑函数，在 CH jet 上为零，因而
\[
|\operatorname{Ric}(g_\delta)+6g_\delta|
+|\operatorname{Ric}(g)+6g|
\le C\delta.
\]
又因 \(\operatorname{Vol}(B_\delta)=O(\delta)\)，
\[
\boxed{|J_6(g_\delta)-J_6(g)|=O(\delta^3).}
\]

\(g_\delta\) 在 \(x\ge X-\delta/2\) 精确等于 CH，bolt 完全未改动，并且全局光滑。

### 严格数值余量

按显示的 \(X=8\) enclosure，安全取
\[
\eta_8^*
=1-\bigl(0.99911624314+7.0\times10^{-12}\bigr)
=8.83756853\times10^{-4}.
\]
原笔记中的末位
\(\eta=8.8375686\times10^{-4}\) 略超过显示 enclosure 直接支持的保守值；应改用 \(\eta_8^*\)。于是可选固定 \(\delta\) 使
\[
J_6(g_\delta)\le8\pi^2(1-\eta_8^*/2).
\]
若让 \(\delta\to0\)，则对任意 \(\rho>0\) 可做到
\[
J_6(g_\delta)\le8\pi^2(1-\eta_8^*+\rho).
\]

类似地，\(X=16\) 可安全取
\[
\eta_{16}^*
=1-(0.99890294372+2.4\times10^{-12})
=1.0970562776\times10^{-3}.
\]

---

## 4. 从 \(\operatorname{Ric}=-6g\) 到 \(\operatorname{Ric}=-g\)

令
\[
\widetilde g=6g.
\]
常数缩放不改变协变 Ricci 张量，因此 CH 区上
\[
\operatorname{Ric}_{\widetilde g}
=\operatorname{Ric}_g=-6g=-\widetilde g.
\]
同时
\[
\operatorname{Ric}_{\widetilde g}+\widetilde g
=\operatorname{Ric}_g+6g.
\]
四维中，协变二张量的范数平方乘 \(6^{-2}\)，体积乘 \(6^2\)，所以
\[
\boxed{
\int|\operatorname{Ric}_{\widetilde g}+\widetilde g|_{\widetilde g}^2
\,dV_{\widetilde g}
=
J_6(g).
}
\]
故冻结积分正是 I54 的 cell cost \(J_1\)，没有遗漏任何 \(6\) 因子。

CH 径向距离为
\[
r_{-6}=\operatorname{arsinh}\sqrt X,\qquad
r_{-1}=\sqrt6\,\operatorname{arsinh}\sqrt X.
\]
在 \(X=8\) 时，
\[
r_{-1}\approx4.32.
\]

---

## 5. I54 转移算术

设
\[
Q_j=k_j+4\ell_j,\qquad h_j=\frac{Q_j}{A_j},
\]
且
\[
\frac{k_j}{Q_j}\to\frac29,\qquad
\frac{\ell_j}{Q_j}\to\frac7{36}.
\]
每个 blow-up cell 的代价为 \(J_1\)，每个标准 handle surgery 的一阶代价为 \(32\pi^2\)。由 I54 的精确 cell 公式及 \(Q_j=o(A_j)\)，体积和总标量交叉项仅贡献 \(o(Q_j)\)，故
\[
\begin{aligned}
\limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}
&\le
\frac29\frac{J_1}{2\pi^2}
+\frac7{36}\frac{32\pi^2}{2\pi^2}\\
&=\boxed{\frac{28}{9}+\frac{J_1}{9\pi^2}}.
\end{aligned}
\]
若
\[
J_1=8\pi^2(1-\varepsilon_0),
\]
则
\[
\limsup\frac{\alpha}{h}
\le4-\frac{8\varepsilon_0}{9}.
\]

因此一次固定平滑、取 \(\varepsilon_0=\eta_8^*/2\)，给出
\[
\limsup\frac{\alpha}{h}
\le4-\frac{4\eta_8^*}{9}
\approx3.999607219.
\]
对任意给定 \(\epsilon>0\)，取足够小但固定的平滑宽度，则
\[
\limsup\frac{\alpha}{h}
\le4-\frac{8\eta_8^*}{9}+\epsilon
\approx3.999214438+\epsilon.
\]
使用 \(X=16\)：
\[
4-\frac{8\eta_{16}^*}{9}
\approx3.999024839.
\]

还可令第 \(j\) 个 cell 的平滑宽度 \(\delta_j\to0\)。由于相应的 \(J_j\to J_{\rm frozen}\)，而 cell 的体积及
\[
t_j=\int_C(s+4)
\]
保持有界，I54 的精确公式仍允许对角化，直接得到
\[
\limsup\frac{\alpha}{h}
\le4-\frac{8\eta_8^*}{9}
\]
或 \(X=16\) 的相应值。固定宽度版本已经足以证明严格低于四；对角版本只是去掉任意小的平滑损失。

---

## 6. residual finiteness 与固定大球供给

令 \(\Gamma\) 是紧 CH 曲面的格，\(p\in\mathbb{CH}^2\)，固定半径 \(r\) 包含 cell 和缓冲 collar。由 proper discontinuity，
\[
\mathcal F_r
=\{\gamma\in\Gamma\setminus\{1\}:
d(p,\gamma p)\le2r\}
\]
是有限集。

\(\Gamma\) 是有限生成线性群，故 residually finite。分别排除 \(\mathcal F_r\) 中各元素并取有限交，可得有限指数子群 \(\Gamma_*\) 满足
\[
\Gamma_*\cap\mathcal F_r=\varnothing.
\]
于是 \(B_r(p)\) 在
\[
X_*=\mathbb{CH}^2/\Gamma_*
\]
中嵌入。

对任一进一步有限覆盖 \(X_j\to X_*\)，该球的原像由
\[
[X_j:X_*]
\]
个互不相交的等距复制组成，而
\[
A_j=c_1^2(X_j)
=[X_j:X_*]\,c_1^2(X_*).
\]
故可用固定大球数与 \(A_j\) 成正比。平衡构造只需
\[
k_j+\ell_j=O(Q_j)=o(A_j)
\]
个 surgery 区域，因此供给充足。

结论是存在一个适当选择的覆盖塔；这并不自动适用于任意预先指定、可能保留短闭路的非正规覆盖塔。若塔由 cofinal normal 子群组成，则每个固定有限位移集合最终都会被排除，因而固定半径条件在充分深层自动成立。

---

## 7. 纯 handle exact-CH cell 的强制下界

设
\[
C=D\#\ell(S^1\times S^3),\qquad \ell\ge1,
\]
其度量在完整外 collar 上精确等于 \(\operatorname{Ric}=-g\) 的 CH 度量，并令
\[
J(C)=\int_C|\operatorname{Ric}+g|^2.
\]

### 7.1 由继承的精确闭流形公式直接推出

将该固定 cell 插入 \(c_1^2=A\) 的 CH 有限覆盖。所得闭流形为
\[
M_A=X_A\#\ell(S^1\times S^3),\qquad
h_A=\frac{4\ell}{A}.
\]
I54 的单 cell 精确公式给出
\[
\frac{\mathcal E(g_A)}{h_A}
\longrightarrow
\frac{J(C)}{8\pi^2\ell}
\qquad(A\to\infty).
\]
另一方面，纯 handle 家族的全度量精确下确界是
\[
\alpha(M_A)=\frac{4h_A}{1+h_A}
\qquad(h_A\le1/3).
\]
由于
\[
\alpha(M_A)\le \mathcal E(g_A),
\]
故
\[
\frac{\mathcal E(g_A)}{h_A}
\ge\frac4{1+h_A}.
\]
令 \(A\to\infty\)，得到
\[
\boxed{J(C)\ge32\pi^2\ell.}
\]

这一步仅依赖已经继承的 exact handle-only formula，完全回答 TTCS 所要求的“证明或反驳”。

### 7.2 更强的严格性

材料中的相对恒等式还给出
\[
\boxed{
J(C)-32\pi^2\ell
=
\frac{S_C-16d}{12}
+4B_C
+\frac14\int_C(s+4)^2,
}
\]
其中
\[
S_C=\int_Cs^2,\qquad B_C=\int_C|W^-|^2,
\qquad d=\operatorname{Vol}(D).
\]
把 cell 嵌入闭 CH 覆盖后，继承的 metricwise scalar estimate 给出
\[
S_C\ge16d.
\]
故每项非负，再次推出 \(J\ge32\pi^2\ell\)。

若 equality 成立，则必须
\[
S_C=16d,\qquad B_C=0,\qquad s\equiv-4.
\]
粘回 CH 外部后，闭流形达到纯 handle 标量不等式的 equality；继承的 equality 论证产生非零平行正旋量，但
\[
c_2(S^+)[M]=\ell>0
\]
排除处处非零平行截面。因此在接受该继承 equality 理论时，
\[
\boxed{J(C)>32\pi^2\ell\quad\text{对每个固定光滑 cell}.}
\]
然而 shrinking-handle 构造使代价趋于 \(32\pi^2\ell\)，所以
\[
\boxed{\inf J=32\pi^2\ell}
\]
且对 \(\ell>0\) 不达到。

因此 Step 10 中“handle cells 是否也能低于 \(32\pi^2\)”若指孤立纯 handle exact-CH cells，应删除或改写：答案是否定的。

---

## 8. 一般 cell 的共同相对恒等式

对
\[
C=D\#k\overline{\mathbb{CP}}^{\,2}
\#\ell(S^1\times S^3),\qquad q=k+4\ell,
\]
相对 Chern–Weil 恒等式可整理为
\[
\boxed{
J-8\pi^2q
=
\frac{S_C-16d}{12}
+\frac14\int_C(s+4)^2
-4\left(\frac{2d}{3}-W_C\right),
}
\]
其中 \(W_C=\int_C|W^+|^2\)。签名恒等式又给出
\[
\frac{2d}{3}-W_C=12\pi^2k-B_C\le12\pi^2k.
\]

这揭示了纯 handle 与混合 cell 的本质差异：

* 当 \(k=0\) 时，
  \[
  \frac{2d}{3}-W_C=-B_C\le0,
  \]
  所以 handle 没有任何正的自对偶 Weyl deficit 预算，不能低于 \(32\pi^2\ell\)。
* 当 \(k>0\) 时，blow-up 通过签名提供最多 \(12\pi^2k\) 的正 deficit 预算；冻结垂直 cell 正是利用这一通道使 \(J<8\pi^2k\)。

因此低于标准拓扑成本的资源来自 blow-up，而不是 handle 本身。

---

## 9. 正确的混合-cell 问题

定义
\[
\mathfrak J_{k,\ell}
=
\inf\left\{
\int_C|\operatorname{Ric}+g|^2:
C=D\#k\overline{\mathbb{CP}}^{\,2}
\#\ell(S^1\times S^3),\
g\text{ 有 exact-CH outer collar}
\right\},
\]
允许外球半径变化。已知
\[
\mathfrak J_{0,\ell}=32\pi^2\ell,\qquad
\mathfrak J_{1,0}<8\pi^2.
\]

但纯 handle 定理并不推出
\[
\mathfrak J_{k,\ell}
\ge \mathfrak J_{k,0}+32\pi^2\ell.
\]
相对曲率恒等式是全 cell 的积分关系，不会按 connected-sum 拓扑块自动相加。blow-up 与 handle 若置于同一不可分解 cell 中，可能共同重排 \(W^+\)、标量平方和 Ricci 缺陷。

平衡比例的最小整数块是
\[
(k,\ell,q)=(8,7,36).
\]
一个这样的混合 cell 会给出一阶系数
\[
\boxed{c_{\rm mix}=\frac{\mathfrak J_{8,7}}{72\pi^2}.}
\]
低于四等价于
\[
\mathfrak J_{8,7}<288\pi^2.
\]

分离式构造的成本是
\[
\mathfrak J_{\rm sep}
=8\mathfrak J_{1,0}+7(32\pi^2)
=8\mathfrak J_{1,0}+224\pi^2,
\]
对应
\[
c_{\rm sep}
=\frac{28}{9}
+\frac{\mathfrak J_{1,0}}{9\pi^2}.
\]

所以真正的 blow-up–handle 相互作用问题是
\[
\boxed{
\mathfrak J_{8,7}
<
8\mathfrak J_{1,0}+224\pi^2\;?
}
\]
更一般地，可问多块极限是否出现严格次可加性。若要把系数压到 \(28/9\) 以下，则必须达到更强条件
\[
\mathfrak J_{8,7}<224\pi^2,
\]
因为所有分离纯 handle 的贡献本身已经是 \(224\pi^2\)。

这与“孤立 handle cell 是否能低于 \(32\pi^2\)”严格不同：后者已被否定；前者仍未由现有材料解决。

---

## 最终判断

1. 冻结 \(C^2\) 垂直 cell 的 bolt、定向拓扑、正定性和 exact-collar 三阶接触均成立。
2. 平滑误差确为 \(O(\delta^3)\)，足以保持严格 subthreshold。
3. \(g\mapsto6g\) 后，冻结能量原封不动成为 \(\operatorname{Ric}=-g\) 归一化的 \(J_1\)。
4. I54 算术给出
   \[
   \limsup\alpha/h
   \le 28/9+J_1/(9\pi^2)<4.
   \]
5. residual finiteness 足以构造拥有线性数量固定大球的适当覆盖塔。
6. 应使用 enclosure 支持的保守余量 \(\eta_8^*,\eta_{16}^*\)，而非略向上舍入的最后一位。
7. 每个纯 handle exact-CH cell 均满足
   \[
   J\ge32\pi^2\ell,
   \]
   固定光滑 cell 实际严格大于该值，而下确界由退化 shrinking-handle 序列逼近。
8. 剩余的相关开放对象是混合 cell 的非加性相互作用，尤其是 \(\mathfrak J_{8,7}\)，不是孤立 handle 改进。