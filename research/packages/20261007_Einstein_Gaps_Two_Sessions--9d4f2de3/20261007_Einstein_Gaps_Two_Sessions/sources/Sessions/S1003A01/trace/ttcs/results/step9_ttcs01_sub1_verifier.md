# TTCS Independent Branch Record

```json
{
  "step_id": 9,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step9_subthreshold_cell_verification.md",
    "Sessions/S1003A01/workspace/notes/step7_perpendicular_verification_and_endpoint_map.md",
    "Sessions/S1003A01/workspace/notes/step8_kahler_period_law_and_Rplus_response.md",
    "Skills/geometric-analysis/research/sources/continuation/20260928_relative_cell_cost.md",
    "Skills/geometric-analysis/research/sources/continuation/20260926_boundary_compatibility.md",
    "Sessions/S1003A01/workspace/scripts/perp_dual_cost.py",
    "Sessions/S1003A02/workspace/scripts/o11_perp_cell.py",
    "Sessions/S1003A01/workspace/data/perp_collar/verify_x0.01_X8_J_d8.json"
  ]
}
```

## Task

Read the Step-9 construction note as a differential geometer and verify the logical chain for the proposed finite-scale perpendicular complex-hyperbolic blow-up cell: normalization/rescaling from J6 to the Ric=-g cell cost, smooth bolt conditions, C2-to-smooth exact-collar perturbation, residual-finiteness supply of a fixed large embedded ball, and the I54 single-blowup transfer to a balanced-family coefficient below four. Identify any mathematical flaw that would invalidate the route, and separate it from the single remaining computational enclosure. Use the actual inherited I54 source and the Step-7/8 derivations. Do not treat floating-point evidence as proof.

## Output

# 科学核验备忘录

## 总结

在冻结系数所定义的精确剖面确实满足
\[
J_6<8\pi^2
\]
这一严格积分不等式的前提下，Step-9 的几何与拓扑传递链是成立的：

1. \(g\mapsto \widetilde g=6g\) 将 \(\operatorname{Ric}=-6g\) 归一化为 \(\operatorname{Ric}_{\widetilde g}=-\widetilde g\)，并且四维积分恰好保持；
2. 螺栓处的无锥关系与 weight-four 各向异性条件给出光滑普通 blow-up；
3. 三阶消失的外端偏差可改成光滑、完全等于 CH 的外环带，代价变化为 \(O(\delta^3)\)；
4. 剩余有限性确实能先构造一个含固定大嵌入球的有限覆盖，再从其进一步覆盖中得到与覆盖次数成比例的互不相交球；
5. I54 §2 的单 blow-up 公式由此给出严格小于 \(4\) 的 balanced-family 上系数。

没有发现另一处会使这条路线失效的数学错误。当前真正未证明的是冻结剖面的严格能量符号。两套浮点实现高度一致，但它们仍不构成
\[
J_6/(8\pi^2)<1
\]
的证明。另有两个需要措辞精确之处：存档剖面直接拼接时只有 \(C^2\)，不是 I54 定义中的光滑 cell；以及文中 \(3.9992144389\) 是未平滑极限剖面的数值，固定平滑 cell 的实际数值会有 \(O(\delta^3)\) 改动。

---

## 1. \(J_6\) 与 I54 中 \(\operatorname{Ric}=-g\) cell cost 的归一化

令
\[
\widetilde g=6g.
\]
常数缩放不改变 Levi–Civita 联络，故把 Ricci 张量看成 \((0,2)\)-张量时
\[
\operatorname{Ric}_{\widetilde g}=\operatorname{Ric}_g.
\]
于是
\[
\operatorname{Ric}_{\widetilde g}+\widetilde g
=\operatorname{Ric}_g+6g.
\]
在四维中，对任意固定 \((0,2)\)-张量 \(T\)，
\[
|T|_{\widetilde g}^2=6^{-2}|T|_g^2,
\qquad
dV_{\widetilde g}=6^2dV_g.
\]
因此
\[
\int_C|\operatorname{Ric}_{\widetilde g}+\widetilde g|_{\widetilde g}^2\,dV_{\widetilde g}
=
\int_C|\operatorname{Ric}_g+6g|_g^2\,dV_g.
\]
这正是 I54 中
\[
J(C)=\int_C|\operatorname{Ric}+G|^2
\]
的归一化。

Step-9 使用的分解也正确：
\[
\operatorname{Ric}+6g
=\operatorname{Ric}^{\circ}+\frac{s+24}{4}g,
\]
而四维中 \(|g|^2=4\)，所以
\[
J_6
=P+\frac14\int_C(s+24)^2\,dV,
\qquad
P=\int_C|\operatorname{Ric}^{\circ}|^2\,dV.
\]
故记录中的无量纲数值确实是
\[
\frac{J_1}{8\pi^2}
\]
的候选值。这里的“确实”只涉及缩放恒等式；存档剖面成为 I54 的光滑 cell 还需后述外环带改造。

---

## 2. 螺栓光滑性与普通 blow-up 拓扑

对脚本中的 perpendicular 参数化，令 \(y=x-x_0\)，并记
\[
S(u)=10u^3-15u^4+6u^5,\qquad
u=\frac{\log(x/x_0)}{\log(X/x_0)}.
\]
其局部形式为
\[
F=y\,e^{q_F}+x_0S(u),
\]
\[
G=\bigl[y+(x^2+x_0)S(u)\bigr]e^{q_G},
\]
\[
w=\log(1+x)S(u)+u^2(1-u)^3p_w(u),
\]
其中 \(q_F,q_G\) 在 \(u=0\) 光滑。由于 \(u=O(y)\) 且 \(S(u)=O(u^3)\)，
\[
F=f_1y+O(y^2),\qquad G=g_1y+O(y^2),\qquad w=O(y^2).
\]
系数平移在代数上给出
\[
q_G(0)=-q_F(0),
\]
因此
\[
f_1=e^{q_F(0)},\qquad g_1=e^{q_G(0)},\qquad f_1g_1=1.
\]
这不是由打印出的 \(0.968860\) 与 \(1.032140\) 推断，而是参数化本身的恒等式。

令 \(t\) 为螺栓的测地径向坐标。由
\[
dt=\frac{dy}{2\sqrt{G}}
\]
得到
\[
y=g_1t^2+O(t^4).
\]
于是
\[
F=t^2+O(t^4),
\]
并且
\[
x=x_0+g_1t^2+O(t^4),
\qquad
xe^w-x=O(t^4).
\]
所以局部度量具有形式
\[
dt^2+\bigl(t^2+O(t^4)\bigr)\sigma_1^2
+\bigl(x_0+O(t^2)\bigr)(\sigma_2^2+\sigma_3^2)
+O(t^4)(\sigma_3^2-\sigma_2^2).
\]
其中：

- \(f_1g_1=1\) 给出周期 \(2\pi\) 的无锥关系；
- 非塌缩二维切向度量在 \(t=0\) 为圆形；
- \(\sigma_2,\sigma_3\) 的无迹各向异性为 \(O(t^4)\)，正是该奇异轨道的 weight-four 光滑条件；
- 所有径向系数由 \(t^2\) 的光滑函数组成。

因此螺栓不是仅有形式上的一阶正则，而是光滑的 SU(2)-不变奇异轨道。

塌缩方向由常规 \(\sigma_3\) 改为 \(\sigma_1\) 不改变底层 blow-up 拓扑：循环置换
\[
(\sigma_1,\sigma_2,\sigma_3)\mapsto(\sigma_2,\sigma_3,\sigma_1)
\]
保持结构方程及三维取向，把该模型变为常规 Hopf 螺栓模型。所得 cell 仍是球的一点 blow-up，即 I54 中的 \(k=1,\ell=0,q=1\) cell。

### 正定性实际上由参数化直接保证

网格上的正定性数据并非这里的核心证明。因为
\[
S'(u)=30u^2(1-u)^2\ge0,\qquad S(0)=0,\quad S(1)=1,
\]
故 \(0\le S(u)\le1\)。对 \(x_0<x\le X\)，
\[
F=(x-x_0)e^{q_F}+x_0S(u)>0,
\]
\[
G=\bigl[(x-x_0)+(x^2+x_0)S(u)\bigr]e^{q_G}>0.
\]
同时
\[
x>0,\qquad xe^w>0.
\]
所以原始剖面在整个开区间上的正定性是解析事实，不依赖 20,001 点网格或 Arb 下端点。

---

## 3. 从二阶匹配到光滑 exact-CH 外环带

设
\[
q=(F-F_{\rm CH},\,G-G_{\rm CH},\,w-w_{\rm CH}),
\]
其中
\[
F_{\rm CH}=x,\qquad G_{\rm CH}=x(1+x),\qquad
w_{\rm CH}=\log(1+x).
\]
脚本中的 \(S(u)\) 在 \(u=1\) 满足一、二阶导数为零，而所有自由偏差含有 \((1-u)^3\)。因此在 \(\rho=X-x\downarrow0\) 时
\[
q=O(\rho^3),\qquad q'=O(\rho^2),\qquad q''=O(\rho).
\]

取光滑函数 \(\chi_\delta\)，在 \(x\le X-2\delta\) 等于 \(1\)，在 \(x\ge X-\delta\) 等于 \(0\)，且
\[
|\partial_x^j\chi_\delta|\le C_j\delta^{-j}.
\]
令
\[
q_\delta=\chi_\delta q.
\]
在过渡带上，
\[
q_\delta=O(\delta^3),\qquad
q_\delta'=O(\delta^2),\qquad
q_\delta''=O(\delta).
\]
由于 \(x=X>0\) 处没有坐标退化，Ricci 张量与标量曲率是度量二阶 jet 的光滑函数。因而
\[
|\operatorname{Ric}^{\circ}(g_\delta)|+
|s(g_\delta)+24|=O(\delta)
\]
于宽度 \(O(\delta)\) 的过渡带上成立。CH 背景的这两个缺陷都为零，于是
\[
P(g_\delta;\text{过渡带})+
J_6(g_\delta;\text{过渡带})=O(\delta^3).
\]
原始剖面在同一带上的曲率缺陷同样是 \(O(\delta)\)，故
\[
|P(g_\delta)-P(g)|+
|J_6(g_\delta)-J_6(g)|\le C\delta^3. \tag{3.1}
\]

正定性在改造中也没有新问题。若直接设置
\[
F_\delta=F_{\rm CH}+\chi_\delta(F-F_{\rm CH}),
\qquad
G_\delta=G_{\rm CH}+\chi_\delta(G-G_{\rm CH}),
\]
则它们是两个正函数的凸组合；而 \(xe^{w_\delta}\) 对任意实 \(w_\delta\) 都为正。

因此，一旦精确证明
\[
J_6(g)=8\pi^2(1-\varepsilon_0),\qquad \varepsilon_0>0,
\]
式 (3.1) 立即给出某个固定 \(\delta>0\)，使
\[
J_6(g_\delta)<8\pi^2.
\]
对存在性定理而言，不需要先打印出常数 \(C\) 或具体 \(\delta\)。若要给出一个完全数值化的光滑剖面，则还要指定 cutoff 与 \(\delta\)，并给出对应的显式上界。

这也澄清了存档对象的身份：原始记录是光滑 cell 的 \(C^2\) 极限剖面，而不是直接可代入 I54 的光滑 cell。

---

## 4. 尚缺的计算事实

Step-7 的 Cartan 推导给出精确恒等式
\[
|\operatorname{Ric}^{\circ}|^2=\sum_i(r_i-v_i)^2,
\qquad
s=-2\sum_i(r_i+v_i),
\]
以及相对公式
\[
\frac{P}{8\pi^2}-1=S_1+S_2+S_3+C_3,
\]
其中三个 \(S_i\) 是平方积分，\(C_3\) 是带符号的三次项。对 \(X=8\) 存档，浮点输出为
\[
S_1+S_2+S_3
=0.003210025221687777,
\]
\[
C_3=-0.004101322488094909,
\]
故
\[
\frac{P}{8\pi^2}-1
\approx-0.000891297266407132.
\]
再加入
\[
\frac{J_6-P}{8\pi^2}
\approx 7.5404017317\times10^{-6},
\]
得到
\[
\frac{J_6}{8\pi^2}-1
\approx-8.83756864675\times10^{-4}. \tag{4.1}
\]

这些数值与两个独立实现的一致性说明：

- Cartan 公式、坐标曲率公式和相对公式很可能实现一致；
- 所见符号不是普通 Gauss 阶数变化造成的数值翻转；
- 带符号三次项确实足以超过三个平方项与标量平方项。

但它们仍没有证明 (4.1)。严格版本需要把 JSON 中的十进制系数定义为确定的实数，最直接的做法是解释为相应有理数，并给出一个外包区间
\[
S_1+S_2+S_3+C_3+
\frac{1}{32\pi^2}\int(s+24)^2\,dV
\subset(-\infty,0).
\]
螺栓附近原始 spin 表达式包含可消去的相消项，因此可靠证明对象通常是：

- 在短初始区间上使用 \(t\) 或 \(y=x-x_0\) 的解析 Taylor 展开；
- 在其余紧区间上对 Step-7 已简化的相对密度和标量平方密度作 Arb/MPFI 外包积分。

由前述参数化可知，正定性无需并入这项机器证明；定性的光滑外环带改造也无需数值常数。因而当前材料中真正未闭合的计算命题可以压缩为冻结剖面的严格能量上界。

`verify_x0.01_X8_J_d8.json`、两套高阶积分和同行重构是很强的数值佐证，但不能替代这个外包区间。

---

## 5. 固定大球的剩余有限性论证

设原紧致 CH 曲面为
\[
X=\Gamma\backslash\mathbb{CH}^2,
\]
取 \(p\in\mathbb{CH}^2\)，并固定半径 \(R\)，使其包含 \(X=8\) cell 及外环带改造区域。集合
\[
S_R=\{\gamma\in\Gamma\setminus\{1\}:d(p,\gamma p)\le2R\}
\]
由作用的适当不连续性而为有限集。

对每个 \(\gamma\in S_R\)，剩余有限性给出一个有限商，使 \(\gamma\) 的像不为单位元。取这些核的有限交 \(H\)，则 \(H<\Gamma\) 有限指标，并且
\[
H\cap S_R=\varnothing.
\]
所以对任意 \(h\in H\setminus\{1\}\)，
\[
d(p,hp)>2R.
\]
由此 \(B_R(p)\) 在
\[
X_*=H\backslash\mathbb{CH}^2
\]
中嵌入。

若 \(H_j<H\) 是进一步的有限指标子群，则这个嵌入球在
\[
X_j=H_j\backslash\mathbb{CH}^2
\]
中的逆像分解为 \([H:H_j]\) 个互不相交的等距副本。同时
\[
A_j=c_1^2(X_j)=[H:H_j]\,c_1^2(X_*).
\]
故大球数量与 \(A_j\) 成正比。

balanced 构造中
\[
k_j\sim\frac29Q_j,\qquad
Q_j=A_jh_j,\qquad h_j\to0,
\]
因而
\[
\frac{k_j}{A_j}\to0.
\]
所以这些大球最终远多于所需的 perpendicular cells。其余 handle surgery 数量同样是 \(o(A_j)\)，可放入另外的球中。

进一步选择 \(A_j\ge j^4\) 也成立：无限、有限生成且剩余有限的 \(H\) 有无界的有限指数子群。该论证得到的是一个重新选择的 balanced 序列；它并不自动为任意预先固定的覆盖序列提供同样的大嵌入球。

半径换算也正确：
\[
r_{-6}=\operatorname{arsinh}\sqrt X,
\qquad
r_{-1}=\sqrt6\,r_{-6}.
\]
在 \(X=8\) 时
\[
r_{-1}\approx4.32.
\]

---

## 6. I54 单 blow-up 传递系数

I54 `20260928_relative_cell_cost.md` §2 首先给出固定 cell 的精确公式
\[
\mathcal E
=\frac{4nJ-n^2t^2/v_j}{4v_j+n(J-2t)}, \tag{I54-2.1}
\]
从而当 \(n/A_j\to0\) 时，
\[
\frac{\mathcal E}{h_j}\longrightarrow
\frac{J}{2\pi^2q}. \tag{I54-2.2}
\]
这里 cell 的体积变化和总标量变化已包含在 \(t\) 与 \(v_j\) 中；二次项在除以 \(h_j\) 后趋于零。

对 balanced family，
\[
\frac{k_j}{Q_j}\to\frac29,\qquad
\frac{\ell_j}{Q_j}\to\frac7{36}.
\]
每个 blow-up 使用成本 \(J_1\) 的 smooth cell；每个 handle 使用继承的 shrinking construction，其一阶成本为
\[
8\pi^2\cdot4=32\pi^2.
\]
于是
\[
\limsup_{j\to\infty}\frac{\alpha(M_j)}{h_j}
\le
\frac1{2\pi^2}
\left(
\frac29J_1+\frac7{36}\,32\pi^2
\right)
=
\frac{28}{9}+\frac{J_1}{9\pi^2}. \tag{6.1}
\]
这正是 I54 §2 明文记录的 single-blowup 公式。

若
\[
J_1=8\pi^2(1-\varepsilon),
\qquad \varepsilon>0,
\]
则
\[
\limsup\frac{\alpha(M_j)}{h_j}
\le4-\frac{8\varepsilon}{9}<4. \tag{6.2}
\]

从存档浮点值计算，
\[
\varepsilon_0
=1-0.9991162431352536
\approx8.837568647464\times10^{-4},
\]
因此未平滑极限剖面对应
\[
4-\frac89\varepsilon_0
\approx3.99921443834245.
\]
这与 Step-9 的 \(3.9992144389\) 只有约 \(6\times10^{-10}\) 的抄录或舍入差异，不影响严格小于四的结构。

对于一个固定的平滑 cutoff，实际系数应写成
\[
\frac{28}{9}+\frac{J_{1,\delta}}{9\pi^2},
\qquad
J_{1,\delta}=J_{1,0}+O(\delta^3).
\]
严格小于四由足够小的固定 \(\delta\) 保持。若令 \(\delta_j\to0\)，I54-2.1 的代数仍适用，因为 cell 的体积、标量矩和能量保持一致有界，此时 limsup 可达到未平滑极限剖面给出的数值上界。

---

## 7. 与 Step-7、Step-8 及 I54 其他结论的一致性

### 7.1 不与 Kähler period law 冲突

Step-8 Theorem 1 对 Kähler cell 给出
\[
P=2(2\pi-\lambda t)^2+\frac14L.
\]
在 \(\lambda=-1\) 归一化下，它强制 Kähler blow-up cell 的成本超过 \(8\pi^2\)。当前 perpendicular 剖面在过渡区是三轴的，并非原 CH 复结构下的 Kähler metric，所以该公式不适用于它。

I54 §4–5 对 biaxial、conformally Kähler cells 的估计也不覆盖这个三轴剖面。I54 §6.1 虽把所有此类对角三轴 cell 化为 conformal almost-Kähler 问题，但式 (6.6) 保留了一个可出现补偿的中间区间，并没有推出普遍的 \(J\ge8\pi^2\)。因此 Step-9 的数值现象与 I54 的既有定理没有矛盾。

### 7.2 与 \(R^+\) 一阶响应一致

Step-8 的响应公式为
\[
\frac{P_{\rm cell}}{8\pi^2}
=
1-\frac{t}{\pi}R^+(\hat\zeta,\hat\zeta)+o(t).
\]
在 CH 的 Kähler 取向中，
\[
\operatorname{spec}R^+=\{s/4,0,0\}.
\]
perpendicular 方向位于零特征空间，所以一阶 \(t\)-项消失。当前
\[
1-\frac{J_6}{8\pi^2}\approx8.84\times10^{-4}
\]
而 \(x_0^2=10^{-4}\)，其量级与二阶响应相容。这个结构解释不决定二阶项符号；真正决定符号的仍是 Step-7 相对公式中的三次补偿积分。

---

## 最终判断

- 缩放、螺栓正则性、普通 blow-up 拓扑、光滑 exact-CH 外环带改造、剩余有限性大球供应以及 I54 系数换算均成立。
- 存档剖面本身只有二阶外端匹配，不能直接作为 I54 的 smooth cell；Step-7 的 \(O(\delta^3)\) 改造严格补上这一点。
- 正定性由剖面公式直接得到，不需要依赖网格。
- 浮点重构没有证明 \(J_6<8\pi^2\)。当前材料尚缺一个对冻结系数精确积分的经验证外包区间。
- 一旦该区间给出严格上端点 \(<1\)，便立即存在 smooth exact-collar one-blowup cell，其 I54 balanced-family 系数严格小于四。没有另一项几何或拓扑障碍需要同时补充。