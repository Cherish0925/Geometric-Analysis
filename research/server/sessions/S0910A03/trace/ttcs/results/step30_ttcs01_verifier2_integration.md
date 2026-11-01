# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 30,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step30_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step30_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Adversarially verify and strengthen the proposed common-union first-exit route for varying Ishida–LeBrun manifolds. Use the Step 23/26/A01 Moser files and the Step 29 terminal lemma. Focus on: (i) a quantitatively correct disjoint macro-support selection in collapsed Ricci-lower-bound geometry retaining a fixed total volume fraction; (ii) one common cutoff flow a=Σχ_j² with componentwise H2/H3/J6 and global Q closing noncircularly; (iii) strict center set P versus a larger bounded-curvature plateau containing every chart geodesic; (iv) terminal errors normalized by A or volume for σ/A→0, with positive-weight regularization ε chosen correctly when Q itself need not tend to zero; and (v) eigenline density restricted to the bounded-curvature region and extended by zero. Identify any remaining mathematical obstruction, especially any false use of maximal-function constants, Sobolev domains, or flow existence.

## Integrated Scientific Memo

# 核验结论：common-union first-exit 路线的可成立部分与剩余障碍

该路线目前可以严格保留的是：

1. 在仅有 Ricci 下界、允许塌缩的情形下，确实可选出**彼此不交的宏支撑**，且严格中心集保留固定总体积比例；
2. 对同一个
   \[
   a=\sum_j\chi_j^2
   \]
   的流，固定指数 \(H_2,H_3,J_6\) 与全局 \(Q\) 可以无支撑数目损失地同时闭合；
3. 终端平均必须使用严格中心集 \(P\)，其所有短测地线位于更大的 \(a=1\) 有界曲率平台；
4. 对变化的流形，终端误差必须按 \(A_i\) 或体积归一化，并取强度型正则参数
   \(\varepsilon_i=Q_i/V_i\)，不能取 \(\varepsilon_i=Q_i\)；
5. 最低特征线密度只在有界曲率平台上有估计，必须在平台外延拓为零。

但是，临界 \(\sigma/A\to0\) 路线仍未闭合。两个主要缺口是：

- 已写出的加权 Moser 迭代存在半次幂权重错配，不能推出所声称的
  \(\|a\operatorname{Rm}\|_\infty\) 和 \(\|aE\|_\infty\)；
- 退化规范化截断流的光滑存在与延拓定理尚无完整证明。

此外，在变化的 Ishida–LeBrun 家族上获得固定物理半径，还需要 \(\chi(M_i)/A_i\) 等拓扑比值的统一控制，或其他统一控制平均曲率能量的机制。

---

## 1. 正确的宏支撑选择

Step 29 中以阈值 \(4K_0\) 并假设 doubling 常数 \(C_D\le2\) 的论证错误。在四维小尺度，半径加倍体积比趋近 \(2^4=16\)，故不能如此估计好集比例。

令
\[
F=(1+|\operatorname{Rm}|^2)^{1/2},\qquad
\bar K=\fint_MF^2,
\]
并假设 \(\operatorname{Ric}\ge-\kappa g\)。固定尺度 \(r\)，使所有至 \(30r\) 的球具有只依赖 \(4,\kappa r^2\) 的 doubling 常数。定义截断中心极大函数好集
\[
G=\left\{x:\sup_{0<s\le6r}\fint_{B_s(x)}F^2
             \le\Lambda\bar K\right\},
\qquad \Lambda=2C_{\mathrm M}.
\]
弱 \((1,1)\) 估计给出
\[
\operatorname{Vol}(G)\ge\frac12\operatorname{Vol}(M).
\]

取 \(G\) 中一个极大 \(r\)-分离族 \(\{p_\alpha\}\)。则 \(B_r(p_\alpha)\) 覆盖 \(G\)。以顶点 \(p_\alpha\) 构图，距离不超过 \(12r\) 时连边。doubling/packing 给出统一最大度
\[
N=N(4,\kappa r^2).
\]
选取总权重最大的颜色类，其中权重为
\[
w_\alpha=\operatorname{Vol}(B_r(p_\alpha)).
\]
所得子族 \(\{p_j\}\) 满足
\[
\sum_j\operatorname{Vol}(B_r(p_j))
\ge\frac{\operatorname{Vol}(G)}{N+1}
\ge\frac{\operatorname{Vol}(M)}{2(N+1)},
\tag{1}
\]
且 \(B_{6r}(p_j)\) 两两不交。

可以安排
\[
P_j=B_r(p_j),\qquad
\chi_j=1\ \text{于 }B_{4r}(p_j),\qquad
\operatorname{supp}\chi_j\Subset B_{5r}(p_j),
\]
以及
\[
\eta_j=1\ \text{于 }\operatorname{supp}\chi_j\text{ 的邻域},\qquad
\operatorname{supp}\eta_j\Subset B_{6r}(p_j).
\tag{2}
\]
这里必须把 Sobolev 区域取为实际球 \(B_{6r}(p_j)\)，不能声称好中心自动控制任意
\(U_j\subset B_{6r}(p_j)\) 的平均值：若 \(U_j\) 很小，该结论不成立。

在球上，相对 Sobolev 不等式为
\[
\|u\|_4^2\le S_j\left(\|\nabla u\|_2^2+r^{-2}\|u\|_2^2\right),
\qquad
S_j\le C r^2\operatorname{Vol}(B_{6r}(p_j))^{-1/2}.
\tag{3}
\]
好点条件给出
\[
S_j\|F\|_{L^2(B_{6r}(p_j))}
\le C\sqrt{\Lambda}\,r^2\sqrt{\bar K}.
\tag{4}
\]
因此可取
\[
r=c\,\bar K^{-1/4}
\tag{5}
\]
并令无量纲常数 \(c\) 足够小，使临界吸收系数统一小。

这比 Step 29 原来的 \(r/5\)-分离构造更可靠：原构造只保证小球不交，却允许 \(B_{2r/3}\) 型支撑大量重叠，因而不能推出 \(a\le1\)。

---

## 2. 一个公共流上的固定指数层可以非循环闭合

由于 \(B_{6r}(p_j)\) 不交，
\[
a=\sum_j\chi_j^2
\]
在第 \(j\) 个分量上就是 \(\chi_j^2\)，并且全局 \(0\le a\le1\)。流
\[
\partial_tg=-2aE,\qquad E=\operatorname{Ric}+g
\tag{6}
\]
是一个公共流，但在各宏支撑上完全分量化。特别地，
\[
\frac{|da|^2}{a}=4|d\chi_j|^2\le Cr^{-2}
\tag{7}
\]
在零集上取连续延拓值 \(0\)。

在暂定双 Lipschitz 与 Sobolev 区间内，Step 23 的固定指数估计可逐分量使用：
\[
H_{2,j}'+cD_{2,j}
 \le Cr^{-2}H_{2,j}+CH_{3,j},
\tag{8}
\]
\[
H_{3,j}'+cD_{3,j}
 \le Cr^{-2}H_{3,j}
 +C\int \eta_j^2a^2F^4.
\tag{9}
\]
由 (4) 的小临界乘积吸收反应项，可得
\[
H_{2,j}(t)\le e^{Ct/r^2}H_{2,j}(0),
\tag{10}
\]
以及先由时空三次估计选取好时间片，再用固定 \(q=3\) 方程排除终端尖峰：
\[
S_j^2H_{3,j}(t)
\le \frac{C\gamma_{j,*}^3}{t}.
\tag{11}
\]

这里 active \(H_2\) 必须直接在活动区域重做测试。不能仅从包含静止 collar 的 \(H_2\) 中减去常数后引用原不等式，否则可能残留虚假的 collar 加性项。正确计算中所有截断余项都含 \(a,da\) 或 \(|da|^2/a\)，故仅支撑在活动区。

固定 \(J_6\) 也可逐分量保持：
\[
J_{6,j}(t)
=\int\eta_j^2a^4|E|^6
\le e^{Ct/r^2}J_{6,j}(0)
\le C\delta^6\operatorname{Vol}(B_{6r}(p_j)).
\tag{12}
\]
这一步从 \(t=0\) 以固定指数临界吸收完成，不能把 \(H_3(t)\sim t^{-1}\) 从零积分。

对全局
\[
Q(t)=\int_M|E|^2\,d\mu_t,
\]
有
\[
Q'+c\int a|\nabla E|^2
\le C\int\left(\frac{|da|^2}{a}+a\right)|E|^2
 +C\int a|\operatorname{Rm}|\,|E|^2.
\tag{13}
\]
逐分量估计
\[
\int\chi_j^2|\operatorname{Rm}|\,|E|^2
\le \|\operatorname{Rm}\|_{2,B_{6r}(p_j)}
   \|\chi_jE\|_4^2
\]
并利用同一小临界乘积吸收梯度项，求和时由于支撑不交而无分量数损失，得到
\[
Q'(t)\le Cr^{-2}Q(t),\qquad
Q(t)\le e^{Ct/r^2}Q(0).
\tag{14}
\]
流外静止区的缺陷能量保持不变，并不会产生额外源项。

因此 \(H_2/H_3/J_6/Q\) 的同时第一退出层本身是相容且非循环的。

---

## 3. 当前 Moser 迭代确实错误；必须改用未加权变量

Step 26/29 使用
\[
K_p=\int\eta^2a^{p-2}\Phi^p,\qquad
Z_p=\eta a^{(p-1)/2}\Phi^{p/2}.
\]
四维抛物 Sobolev 步控制
\[
\int Z_p^3
=\int\eta^3a^{3(p-1)/2}\Phi^{3p/2}.
\tag{15}
\]
而下一能量是
\[
K_{3p/2}
=\int\eta^2a^{3p/2-2}\Phi^{3p/2}.
\tag{16}
\]
两者的 \(a\)-指数相差 \(1/2\)：
\[
\frac{3(p-1)}2-\left(\frac{3p}{2}-2\right)=\frac12.
\]
由于 \(0\le a\le1\)，得到的是
\[
\int Z_p^3\le K_{3p/2},
\tag{17}
\]
方向与迭代所需相反。因此 Step 26 的递推式及其结果
\[
\|aF(t)\|_\infty\le C\beta/t,\qquad
\|aE(t)\|_\infty\le C\delta(r^2/t)^{1/3}
\tag{18}
\]
并未由所写加权层推出。Step 27 文件首部的纠正是正确的，Step 29 继续沿用旧递推则不正确。

正确候选是直接迭代
\[
U=a(\operatorname{Rm}+G),\qquad V=aE,
\tag{19}
\]
或对应的范数，其中 \(G\) 是为规范化项选取的固定移位张量。对 \(U=aF\) 的标量模型，
\[
w_p=U^{p/2}
\]
满足
\[
\int w_p^3=\int U^{3p/2},
\tag{20}
\]
与下一指数能量精确匹配，不再出现半次幂缺口。

但供应材料中尚未给出以下完整内容：

- \(U,V\) 的弱能量不等式；
- 所有 \(da,\nabla^2a\) 项的一次分部积分和可吸收结构；
- \(V=0\) 处的统一正则化；
- 从 \(H_3\) 与 \(J_6\) 种子到未加权 \(U,V\) 种子的正确转换；
- 新递推中的 Sobolev 与体积因子消去。

故 (18) 目前仍是未证结论。这不仅影响度量漂移，也同时阻断平台曲率界和 Wang 延拓。

另一个应在正式张量公式中修正的记号是：Step 23 的反应项写成
\[
a(\operatorname{Rm}*\operatorname{Rm}+\operatorname{Rm})
\]
会掩盖 \(E=0\) 时的完全静止性。应显式组织为 \(a\,\operatorname{Rm}*E\) 加导数截断项，或展示归一化 Ricci 与 \(-2ag\) 反应项的精确抵消。

---

## 4. 严格中心集必须严格位于更大的 \(a=1\) 平台内

由 \(\|a\operatorname{Rm}\|_\infty\) 只能在 \(a=1\) 区域推出普通曲率界；在 \(0<a<1\) 的过渡 collar 上，
\[
|\operatorname{Rm}|\le \frac{C}{a\,t}
\]
会在 \(a\to0\) 时退化。因此所有用于 Rauch 比较的测地线都必须完全位于 \(a=1\) 平台，而不仅仅位于 \(\operatorname{supp}\chi_j\)。

采用 (2) 的尺度，可设
\[
P=\bigcup_jB_r^{g(0)}(p_j),\qquad
L=\bigcup_jB_{4r}^{g(0)}(p_j)\subset\{a=1\}.
\tag{21}
\]
若
\[
e^{-2I}g(0)\le g(T)\le e^{2I}g(0),
\]
则从 \(p\in P\) 出发的 \(g(T)\)-测地线长度 \(\rho=c_0r\) 留在 \(L\) 的充分条件是
\[
r+e^I\rho<4r.
\tag{22}
\]
在 \(L\) 上，若未加权 Moser 最终成立，则
\[
|\sec_{g(T)}|
\le K\le \frac{C\beta}{\theta r^2}+C,\qquad T=\theta r^2.
\tag{23}
\]
还需选择 \(c_0\) 使
\[
K\rho^2<\frac{\pi^2}{4}.
\tag{24}
\]
等价地，主导尺度上要求
\[
c_0^2\lesssim\frac{\theta}{\beta}.
\tag{25}
\]
所以 \(\rho\) 可以是固定比例的 \(r\)，但该比例通常必须远小于 \(1/4\)，并依赖第一退出参数 \(\theta,\beta\)。

由 (1) 和度量比较，
\[
\operatorname{Vol}_{g(T)}(P)
\ge e^{-4I}\frac{\operatorname{Vol}_{g(0)}(M)}{2(N+1)}.
\tag{26}
\]
若 \(\operatorname{Vol}(M_i)/A_i\ge v_0>0\)，则得到终端桥所需
\[
\operatorname{Vol}_{g(T)}(P_i)\ge\alpha A_i.
\]

对变化族，还需 \(r_i\ge r_{\min}>0\) 才有固定物理半径 \(\rho\)。正确四维恒等式为
\[
\int|\operatorname{Rm}|^2
=32\pi^2\chi(M)+4\int|\operatorname{Ric}_0|^2,
\tag{27}
\]
不是系数 \(6\)。因此平均曲率能量的统一上界一般需要
\(\chi(M_i)/A_i\) 和 \(\operatorname{Vol}(M_i)/A_i\) 的统一控制。
仅有 \(\sigma_i/A_i\to0\) 并不提供这一点。

---

## 5. 终端误差应按 \(A_i\) 归一化；正则参数取 \(Q_i/V_i\)

变化族中所需的是
\[
\frac{Q_i}{A_i}\to0,
\tag{28}
\]
而不是 \(Q_i\to0\)。通常 \(Q_i\sim\delta_i^2A_i\)，所以 \(Q_i\) 本身可不趋零。

令
\[
q_i=\sqrt6|W_i^+|-s_i,\qquad r_i=q_i^+,\qquad
V_i=\operatorname{Vol}(g_i(T)).
\]
应取
\[
\boxed{\varepsilon_i=\frac{Q_i}{V_i}}
\tag{29}
\]
并平滑逼近 \(f_i^2=r_i+\varepsilon_i\)。这样
\[
0\le L_i^+(f_i)-\int r_i^2
\le \varepsilon_i^2V_i
=\frac{Q_i^2}{V_i}.
\tag{30}
\]
若 \(Q_i/V_i\to0\)，则右端为 \(o(Q_i)\)。又因
\[
\int r_i\le C V_i
\]
（由校准及 Cauchy–Schwarz），有
\[
\varepsilon_i\int r_i+\varepsilon_i^2V_i
\le C Q_i.
\tag{31}
\]
因此所有正权重、谐和振幅及投影误差都是 \(O(Q_i)\)，归一化后为
\(o(A_i)\)。

取 \(\varepsilon_i=Q_i\) 在 \(A_i\to\infty\) 时错误：它会产生
\(\varepsilon_i\int r_i\sim Q_iA_i\) 和
\(\varepsilon_i^2V_i\) 的广延误差，远大于 \(Q_i\)。

终端桥的正确选点结论是
\[
A_\rho\mathfrak D_i(p_i)
\le C(K,\rho,\alpha)\frac{Q_i}{A_i}\to0.
\tag{32}
\]
若 \(\sigma_i/A_i\to0\)，则拓扑余量也必须按 \(A_i\) 归一化；由
\(\sigma_i\lesssim Q_i\) 可同样消失。

---

## 6. 最低特征线密度只能局部定义后零延拓

正权重论证给出的
\[
\int_{L_i}\langle\mathscr A_iH_i,H_i\rangle
\le C(K)Q_i,\qquad
\mathscr A_i=W_i^++\sqrt{\frac23}|W_i^+|I,
\tag{33}
\]
依赖 \(L_i\) 上的曲率界和 \(f_i^2\) 上界；它不是全局估计。

因此终端非负密度应定义为
\[
\begin{aligned}
\mathfrak D_i={}&|E_i|^2+(s_i+4)^2
 +(s_i+8\sqrt6|W_i^+|)^2+\mathcal G_i\\
&+\left(|2\pi H_i|-\frac{r_i}{3\sqrt2}\right)^2
 +2\mathbf1_{L_i}\langle\mathscr A_iH_i,H_i\rangle .
\end{aligned}
\tag{34}
\]
即把特征线项在 \(L_i\) 外延拓为零。则
\[
\int_M\mathfrak D_i\le C(K)Q_i.
\tag{35}
\]
由于从 \(P_i\) 出发的所有长度 \(\rho\) 测地线都位于 \(L_i\)，拉回图内
\(\mathbf1_{L_i}=1\)，不会丢失极限所需的特征线信息。结合
\(\operatorname{Vol}(P_i)\ge\alpha A_i\)，有
\[
A_\rho\mathfrak D_i(p_i)
\le C(K,\rho,\alpha)\frac{Q_i}{A_i}\to0.
\tag{36}
\]

---

## 7. 精确剩余数学障碍

当前 common-union 路线尚缺三个实质对象：

1. **未加权移位变量的完整 Moser 定理。**  
   必须从 \(U=a(\operatorname{Rm}+G)\)、\(V=aE\) 推导正确方向的抛物递推，并重新验证体积消去与
   \[
   \|U(t)\|_\infty\lesssim \beta/t,\qquad
   \|V(t)\|_\infty\lesssim\delta(r^2/t)^{1/3}.
   \]
   旧的 \(K_p\)-加权递推不能修补为现有形式。

2. **退化规范化截断流的存在与延拓。**  
   方程在 \(a=0\) 处不是通常严格抛物。必须完整证明固定空间截断的 DeTurck 构造，以及在
   \(\sup|a(\operatorname{Rm}+G)|<\infty\) 下的 Wang 型高阶归纳和延拓。仅称 \(-2ag\) 为“低阶项”不足以处理 collar 上未加权曲率可能无界的问题。

3. **变化族中的统一物理尺度。**  
   若目标超出 \(\chi(M_i)/A_i\) 受控的子族，则需要新的机制确保
   \(\bar K_i\) 统一有界，从而 \(r_i,\rho_i\ge c>0\)。否则即使每个流都局部成立，终端 Einstein germ 的定义域也可能缩为零。

因此，宏支撑选择、固定指数能量层及终端桥已经可以形成一致框架；真正阻断临界路线的是未加权 Moser/度量漂移与规范化退化流延拓，而不是终端校准或塌缩本身。