# TTCS Independent Branch Record

```json
{
  "step_id": 51,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step50_minimizer_entry_PS_noncollapsed_alternative.md",
    "Sessions/S1003A02/workspace/notes/step33_link_charges_global_decomposition_static_channel.md",
    "Knowledge/objects/papers/Orbifold-compactness-for-spaces-of-Riemannian-metrics-and-applications--30aa929b9159--a0e9497fbde6/object.md",
    "Knowledge/objects/papers/Critical-metrics-on-connected-sums-of-Einstein-four-manifolds--e569e9d1f954--5258e72d2de1/object.md"
  ]
}
```

## Task

Read the Step-50 note, Anderson orbifold compactness source, GV critical-metric source, and the existing link-charge note. Verify Theorems 50.B–C under a legitimate scale-compatible residual hypothesis and uniform noncollapse/Sobolev input. Check: point-picking and passage to exact P-critical limits; scalar-flatness of ALE bubbles; lower semicontinuity/energy identity; exact APS charge formula and Burns/Eguchi-Hanson/Kronheimer tests; topology of multiple-end/reducible bubbles; Seiberg-Witten connected-sum split; b1 sign in the pure Γ=1 negative-definite charge; claims of sharp equality/attainment of the bulk infimum; and the certified-cell alternatives. Produce a corrected conditional structure theorem that uses Theorem G/link charges without asserting more topology or equality than follows.

## Output

# 科学核验备忘录：非塌缩 Palais–Smale 序列的轨形紧致性、ALE 树与链环收费

## 1. 总结

Step 50 的核心思路可以成立，但 Theorems 50.B–C 需要把 Theorem 50.A 的加权流输出替换为一个明确的、尺度相容的 Palais–Smale 假设，并加入统一局部 Sobolev 不等式或等价的调和坐标控制。仅有
\[
\operatorname{vol}B(x,r)\ge \nu_0r^4
\]
不足以直接调用 Anderson §3 的临界度量小能量估计；Anderson Proposition 3.5 的证明实际使用了 Sobolev 常数。

在这些输入下，可以严格得到：

1. 点选重标度极限是精确 \(P\)-临界度量。
2. 非紧泡是有限能量 ALE 轨形，并且标量曲率为零，故 Bach-flat。
3. 极限能量只自动给出下半连续不等式；一般形式应写成
   \[
   \alpha(M)=P(g_\infty)+\sum_bP(N_b)+E_{\mathrm{neck}},
   \qquad E_{\mathrm{neck}}\ge0,
   \]
   其中等式把未由已抽取泡吸收的颈区能量定义为 \(E_{\mathrm{neck}}\)。要证明 \(E_{\mathrm{neck}}=0\)，还需独立的无颈能量论证。
4. 对光滑、多端 ALE 空间，APS 公式必须对所有端求和。对带内部轨形点的泡，应在截断正则部分使用 Theorem G；树中成对链环的电荷随后相消。
5. 一端、\(\Gamma=1\)、紧化后 \(b^+=0\) 的泡满足
   \[
   \widehat P(N)\ge b_2(\widehat N)+4b_1(\widehat N),
   \]
   不是 \(b_2-2b_1\)。\(b_1\) 增加而不是减少收费。
6. Anderson 的拓扑结论是沿球面空间形式链环拼合；若出现多端泡或一个轨形点连接多个锥支，不能一般地改写成普通连通和，也不能直接称为一个轨形分解。
7. Seiberg–Witten 连通和消失只能用于已经得到的光滑普通连通和分解。它表明至多一个闭合因子携带正的 \(b^+\)，但不把其余因子识别为若干个 \(\overline{\mathbb{CP}}^{\,2}\)。
8. 一般有泡情形下，\(g_\infty\) 只是 \(P\)-临界度量；它未必实现其所在光滑流形的下确界。精确等式和 bulk attainment 需要一个真实的普通连通和分解以及匹配的 Burns 上界。
9. 对认证 cell 给出的
   \[
   \widehat\alpha\bigl(X\#\overline{\mathbb{CP}}^{\,2}\bigr)
   <0.995663<1,
   \]
   所有一端、光滑、\(\Gamma=1\)、\(b^+=0\) 且 \(b_1+b_2>0\) 的泡都被排除。此前把 \(b_1>0\) 列为逃逸类型的表述方向相反。

---

## 2. 合法的尺度相容 Palais–Smale 输入

记
\[
\mathcal E_P(g)=\nabla^{L^2}P(g)
\]
为 \(P\) 的 Euler–Lagrange 张量。由 GV (1.5)–(1.10)，
\[
2P=\mathcal B_{1/6}-32\pi^2\chi,
\]
所以
\[
\mathcal E_P(g)=0
\quad\Longleftrightarrow\quad
B^{1/6}(g)=0.
\]
在闭流形上取迹得到 \(s\) 为常数，并且
\[
B=\frac13s\,\operatorname{Ric}^{\circ}.
\]
GV Proposition 3.3 给出 \(t=1/6\neq0\) 时的规范化椭圆性。

### 2.1 建议采用的假设

设 \(r_i(x)\) 为截断到 \(1\) 的曲率半径，并取光滑尺度函数 \(\rho_i\) 满足
\[
c\,r_i\le \rho_i\le C\,r_i.
\]
对最小化序列 \(g_i\)，假设：

\[
\operatorname{Vol}(g_i)=1,\qquad P(g_i)\to\alpha(M),
\tag{2.1}
\]

\[
\operatorname{vol}_{g_i}B(x,r)\ge\nu_0r^4,\qquad 0<r\le1,
\tag{2.2}
\]

以及局部尺度不变 Sobolev 不等式
\[
\left(\int_{B(x,r)}|u|^4\right)^{1/2}
\le C_S\left[
\int_{B(x,r)}|\nabla u|^2+r^{-2}\int_{B(x,r)}u^2
\right].
\tag{2.3}
\]

尺度相容残差取为
\[
\varepsilon_i^2
:=
\int_M\rho_i^4|\mathcal E_P(g_i)|^2\,d\mu_{g_i}
\longrightarrow0.
\tag{2.4}
\]

还需要 own-scale 椭圆紧致性。一个足够强而清楚的版本是：在每个
\(B(x,c\rho_i(x))\) 上，
\[
\rho_i(x)^{m+2}
\sup_{B(x,c\rho_i(x))}
|\nabla^m\operatorname{Rm}_{g_i}|
\le C_m,\qquad m\ge1.
\tag{2.5}
\]
也可以把 (2.5) 换成统一调和坐标 \(W^{4,2}\) 估计以及相应的椭圆自举定理。

### 2.2 为什么 (2.4) 正好适配吹起尺度

若 \(\lambda_i\) 是点选得到的长度尺度，且在
\(B(y_i,A\lambda_i)\) 上有 \(\rho_i\ge c\lambda_i\)，令
\[
\widetilde g_i=\lambda_i^{-2}g_i.
\]
四维尺度变换给出
\[
\int_{B_{\widetilde g_i}(y_i,A)}
|\mathcal E_P(\widetilde g_i)|^2\,d\mu_{\widetilde g_i}
=
\lambda_i^4
\int_{B_{g_i}(y_i,A\lambda_i)}
|\mathcal E_P(g_i)|^2\,d\mu_{g_i}.
\]
因此
\[
\int_{B_{\widetilde g_i}(y_i,A)}
|\mathcal E_P(\widetilde g_i)|^2\,d\mu_{\widetilde g_i}
\le c^{-4}\varepsilon_i^2\to0.
\tag{2.6}
\]
这正是点选极限成为精确临界度量所需的尺度关系。

### 2.3 Step 50 的加权流目前尚未给出上述全部输入

Lemma W 的提纲尚未建立以下解析事实：

* 任意塌缩背景中的指数映射拉回并不自动产生统一局部有限的抛物坐标系统；
* 四阶拟线性流的统一初始生存时间不能仅由零阶曲率界和形式上的主符号直接推出；
* Bour 的 Bando–Bernstein–Shi 型估计是在解已经存在并且曲率受控时使用的，不能独自提供统一初始生存时间；
* \(\rho\) 的高阶导数及变系数 DeTurck 项需要统一调和半径或等价几何输入。

在 (2.2)–(2.3) 下，曲率尺度上的注入半径和调和坐标控制使这条流路线更可行；但在完整写出这些局部存在估计以前，Theorems 50.B–C 应直接以 (2.4)–(2.5) 为条件。

---

## 3. 点选、精确临界极限与 Anderson 小能量估计

### 3.1 点选极限

若统一小能量估计不存在，可选取球
\[
B_{g_i}(x_i,r_i),\qquad
\int_{B(x_i,r_i)}|\operatorname{Rm}|^2\le\delta_*,
\]
而内部曲率相对 \(r_i^{-2}\) 任意大。标准点选给出 \(y_i\) 和
\[
\lambda_i=|\operatorname{Rm}(y_i)|^{-1/2}
\]
使得
\[
\lambda_i/r_i\to0,
\]
并且对某个 \(A_i\to\infty\)，
\[
|\operatorname{Rm}_{g_i}|
\le4\lambda_i^{-2}
\quad\text{于 }B(y_i,A_i\lambda_i),
\qquad
|\operatorname{Rm}_{\lambda_i^{-2}g_i}(y_i)|=1.
\tag{3.1}
\]

非塌缩、Sobolev 不等式和 own-scale 正则性在重标度后保持。由 (2.6)，残差在每个固定球上趋于零。因此子列收敛到完整非塌缩极限
\[
(N,g_N,y_\infty),
\]
并且
\[
\mathcal E_P(g_N)=0
\]
以弱意义成立；GV 的规范化椭圆方程随后给出光滑性。极限满足
\[
\int_N|\operatorname{Rm}|^2\le\delta_*,
\qquad
|\operatorname{Rm}(y_\infty)|=1.
\tag{3.2}
\]

### 3.2 与 Anderson 源文献的连接

Anderson Remark 3.10 明确指出，\(\int|z|^2=P\) 的临界度量具有常标量曲率，并满足
\[
D^*D\operatorname{Ric}+\operatorname{Rm}*\operatorname{Ric}=0.
\tag{3.3}
\]
Proposition 3.5 的小能量正则性证明使用 Sobolev 输入。由 (2.3)，其常数在极限及所有重标度上统一。

把 Anderson 的估计用于 \(B(y_\infty,R)\)：
\[
\sup_{B(y_\infty,R/2)}|\operatorname{Rm}|
\le
\left(
\frac{C}{\operatorname{vol}B(y_\infty,R)}
\int_{B(y_\infty,R)}|\operatorname{Rm}|^2
\right)^{1/2}.
\]
由
\[
\operatorname{vol}B(y_\infty,R)\ge\nu_0R^4,
\qquad
\int_N|\operatorname{Rm}|^2\le\delta_*,
\]
得到
\[
|\operatorname{Rm}(y_\infty)|
\le C(\delta_*/\nu_0)^{1/2}R^{-2}.
\]
令 \(R\to\infty\) 得到基点曲率为零，与 (3.2) 冲突。

所以存在统一 \(\delta_0,C_0\)，使 Anderson (1.5) 对充分大的 \(i\) 成立。随后 Theorem 1.1、Theorem 1.2 和 Remark 2.10 给出轨形极限及有限 ALE 泡树。

---

## 4. ALE 泡的标量平坦性

在闭 bulk 上，临界方程取迹给出
\[
\Delta s=0,
\]
所以每个正则连通分支上的 \(s\) 为常数。

对完整有限能量 ALE 泡，同一方程给出 \(s\) 为调和函数。全曲率有限能量蕴含
\[
s\in L^2(N).
\]
取标准截断函数 \(\eta_R\)，由
\[
0=\int \eta_R^2s\,\Delta s
\]
得到
\[
\int_{B_R}|\nabla s|^2
\le
CR^{-2}\int_{B_{2R}\setminus B_R}s^2\to0.
\]
故 \(s\) 为常数；ALE 空间体积无限且 \(s\in L^2\)，于是
\[
s\equiv0.
\tag{4.1}
\]
临界方程因而化为
\[
B=0.
\tag{4.2}
\]
所以每个泡都是标量平坦、Bach-flat 的 ALE 度量。若其 \(P\)-能量为零，则
\[
\operatorname{Ric}^{\circ}=0,\qquad s=0,
\]
故该泡 Ricci-flat。

---

## 5. 能量下半连续性与无颈问题

由 Anderson Lemma 3.2 的四维恒等式，固定 \(M\) 且 \(P(g_i)\) 有界时，
\[
\int_M|\operatorname{Rm}_{g_i}|^2
\]
统一有界。对 bulk 正则部分和每个已抽取泡，光滑局部收敛及 \(P\) 的尺度不变性给出
\[
\alpha(M)
\ge
P(g_\infty)+\sum_bP(N_b).
\tag{5.1}
\]

更完整地，应写为
\[
\alpha(M)
=
P(g_\infty)+\sum_bP(N_b)+E_{\mathrm{neck}},
\qquad E_{\mathrm{neck}}\ge0,
\tag{5.2}
\]
其中 \(E_{\mathrm{neck}}\) 是在依次截去 bulk、泡核心后剩余颈区的
\(|\operatorname{Ric}^{\circ}|^2\)-能量。

当前材料没有证明
\[
E_{\mathrm{neck}}=0.
\tag{5.3}
\]
(5.3) 需要形如
\[
\lim_{R\to\infty}\lim_{\rho\to0}\lim_i
\int_{\text{neck}_i(R,\rho)}
|\operatorname{Ric}^{\circ}_{g_i}|^2\,d\mu_{g_i}=0
\]
的独立估计。Anderson 的轨形紧致性本身只提供 (5.1)。

若没有曲率集中，则不存在颈区和泡，收敛在整个 \(M\) 上光滑，因而
\[
P(g_\infty)=\alpha(M).
\]
这时 \(\alpha(M)\) 确由一个光滑 \(P\)-临界度量实现。

---

## 6. 精确 APS 电荷公式

### 6.1 光滑多端 ALE 空间

设 \(N\) 是光滑、标量平坦、有限能量 ALE 四维流形，端为
\(S^3/\Gamma_e\)。固定约定
\[
\frac1{12\pi^2}\int_N(|W^+|^2-|W^-|^2)
=
\tau(N)+\sum_e\eta_{\Gamma_e}.
\tag{6.1}
\]
令 \(\sigma=\pm1\)，其中 \(W^\sigma=W^+\) 或 \(W^-\)，定义
\[
q_\sigma(\Gamma)
=
\frac2{|\Gamma|}-3\sigma\eta_\Gamma.
\tag{6.2}
\]
Theorem G 在截断域上取极限给出
\[
\boxed{
\widehat P(N)
=
\frac1{2\pi^2}\int_N|W^\sigma|^2
-\bigl(2\chi(N)+3\sigma\tau(N)\bigr)
+\sum_e q_\sigma(\Gamma_e).
}
\tag{6.3}
\]
因此
\[
\boxed{
\widehat P(N)
\ge
\left[
2\sum_e\frac1{|\Gamma_e|}
-2\chi(N)
+3\left|\tau(N)+\sum_e\eta_{\Gamma_e}\right|
\right]_+.
}
\tag{6.4}
\]

Step 50 中的一端公式是 (6.3) 的特例，但“orbifold bubble”不能直接使用同一拓扑表达式而忽略内部轨形点。

### 6.2 带内部轨形点的泡

从轨形泡中挖去内部奇点的小锥邻域，并截断所有 ALE 端，得到光滑紧致块 \(\Omega\)。若“out”表示 ALE 端链环，“in”表示内部奇点链环，则
\[
\widehat P(\Omega)
=
\frac1{2\pi^2}\int_\Omega|W^\sigma|^2
-\bigl(2\chi(\Omega)+3\sigma\tau(\Omega)\bigr)
+\sum_{\rm out}q_\sigma
-\sum_{\rm in}q_\sigma.
\tag{6.5}
\]
在完整泡树中，每个内部链环同时是父块的 in-link 和子块的 out-link，所以这些项成对相消。这是处理多层轨形泡最稳健的形式。

### 6.3 模型核验

**平坦 \(\mathbb R^4\).**
\[
\chi=1,\quad \tau=0,\quad \Gamma=1,\quad \eta=0,
\]
于是 (6.3) 给出 \(\widehat P=0\)。

**Burns 空间.**
\[
\chi=2,\quad \tau=-1,\quad \Gamma=1,\quad \eta=0.
\]
在复定向下 \(W^+=0\)，故
\[
\widehat P=-(4-3)+2=1.
\]
所以
\[
P(\mathrm{Burns})=8\pi^2.
\]

**Eguchi–Hanson.**
\[
\chi=2,\quad \tau=-1,\quad |\Gamma|=2.
\]
在使 \(W^+=0\) 的定向下，(6.3) 与 \(P=0\) 给出
\[
-1+1-3\eta_{\mathbb Z_2}=0,
\]
即本约定下
\[
\eta_{\mathbb Z_2}=0.
\]

**Kronheimer ADE 空间.**
设 \(b_2=r\)，则
\[
\chi=1+r,\qquad \tau=-r,\qquad W^+=0,\qquad P=0.
\]
于是
\[
3\eta_\Gamma=r-2+\frac2{|\Gamma|}.
\tag{6.6}
\]
代回 (6.4) 恰得零。这说明 Ricci-flat ALE 分解泡具有零 \(P\)-收费，与零缺口情形一致。

---

## 7. \(\Gamma=1\) 负定泡中的 \(b_1\) 符号

设 \(N\) 光滑、一端、\(\Gamma=1\)，并以一个四球封闭该端得到 \(\widehat N\)。若
\[
b^+(\widehat N)=0,\qquad
m=b_2(\widehat N),\qquad q=b_1(\widehat N),
\]
则
\[
\chi(N)=\chi(\widehat N)-1
=1-2q+m,
\qquad
\tau(N)=-m.
\]
由 (6.4)：
\[
\boxed{
\widehat P(N)\ge m+4q.
}
\tag{7.1}
\]
在对应定向下，等号要求 \(W^+\equiv0\)。

特别地，
\[
N\simeq\mathbb R^4\#k\,\overline{\mathbb{CP}}^{\,2},
\qquad b_1=0,
\]
给出
\[
\widehat P(N)\ge k,
\]
Burns 型泡达到等号。

因此 Step 50 中的
\[
k_b-2b_1(N_b)
\]
符号错误；正确项为
\[
k_b+4b_1.
\]

若 \(N\) 有 \(\kappa\) 个 \(\Gamma=1\) 端，并可同时以点光滑紧化，则
\[
\chi(N)=2-2b_1+b_2-\kappa,
\]
从而
\[
\widehat P(N)
\ge
\left[
4\kappa-4+4b_1-2b_2+3|\tau|
\right]_+.
\tag{7.2}
\]
若紧化后的交形式负定，则
\[
\widehat P(N)\ge b_2+4b_1+4\kappa-4.
\tag{7.3}
\]

这些公式完全来自 Theorem G，不需要 Donaldson 对角化。即使交形式已知对角，也不能由此把 \(\widehat N\) 识别为
\(\#_m\overline{\mathbb{CP}}^{\,2}\) 的光滑类型。

---

## 8. 多端泡、可约轨形点与拓扑重构

Anderson Remark 2.10 支持的拓扑描述是：

* 截去 bulk 中小锥邻域；
* 截去各 ALE 块的远端及内部轨形点邻域；
* 沿成对的 \(S^3/\Gamma\) 链环重新拼合。

若一个轨形点含多个锥支，或一个 ALE 块有多个端，所得拼合图可以有分叉或回路。此时：

* 一个泡可能同时连接多个 bulk 分支；
* 可能产生 \(S^1\times S^3\) 型拓扑；
* 不能把每个泡独立紧化后写成
  \[
  M\cong V\#\widehat N_1\#\cdots\#\widehat N_m;
  \]
* “\(M\) 是 \(V\) 的轨形解消”只适合每个奇点单锥、每个对应泡单端并且拼合树没有额外回路的情形。

因此修正后的结构定理应以链环拼合为基本拓扑对象，而不是普通连通和。

---

## 9. Seiberg–Witten 分裂实际给出的信息

只有在已经得到光滑普通连通和
\[
M\cong V\#Y_1\#\cdots\#Y_m
\tag{9.1}
\]
时，才能直接使用 Seiberg–Witten 连通和消失定理。

若 \(M=X\#k\overline{\mathbb{CP}}^{\,2}\)，\(b^+(X)\ge2\)，且 \(M\) 具有非零 Seiberg–Witten 不变量，则 (9.1) 中至多一个因子具有正的 \(b^+\)。由于
\[
b^+(M)=b^+(X)\ge2,
\]
恰有一个因子携带全部正方向。因此：

* 若所有 \(Y_b\) 都满足 \(b^+(Y_b)=0\)，则
  \[
  b^+(V)=b^+(M).
  \]
* 若某个 \(Y_b\) 有 \(b^+>0\)，则
  \[
  b^+(V)=0,
  \]
  且其他闭合泡因子均有 \(b^+=0\)。

这不推出：

* \(V\) 与 \(X\#k'\overline{\mathbb{CP}}^{\,2}\) 微分同胚；
* \(Y_b\) 与若干个 \(\overline{\mathbb{CP}}^{\,2}\) 的连通和微分同胚；
* 多端或轨形泡可以进入 (9.1)。

交形式层面的加法只给出 Betti 数和签名关系。

---

## 10. bulk 下确界与精确等式

一般有泡时，只能写
\[
P(g_\infty)\ge\alpha(V)
\tag{10.1}
\]
——这里还要求 \(V\) 是光滑闭流形，且 \(\alpha(V)\) 已按同一度量类定义。临界性本身不蕴含
\[
P(g_\infty)=\alpha(V).
\]

下面这组额外假设足以恢复 Step 50 所希望的精确等式：

1. \(V\) 光滑；
2. 有真实微分同胚
   \[
   M\cong V\#r\,\overline{\mathbb{CP}}^{\,2};
   \]
3. 泡树的 \(\Gamma=1\) 收费总和至少为 \(r\)；
4. Burns 插入在这个真实连通和上给出
   \[
   \alpha(M)\le\alpha(V)+8\pi^2r.
   \]

这时紧致性下界给出
\[
\alpha(M)
\ge P(g_\infty)+8\pi^2r
\ge \alpha(V)+8\pi^2r,
\]
与 Burns 上界合并得到
\[
\boxed{
\alpha(M)=\alpha(V)+8\pi^2r,
\qquad
P(g_\infty)=\alpha(V).
}
\tag{10.2}
\]
同时所有中间不等式均为等号，故 \(E_{\mathrm{neck}}=0\)，相应泡达到链环收费。

没有上述真实连通和时，交形式相同不能替代第 2 项，因而不能推出 (10.2)。

---

## 11. 修正后的条件结构定理

### 定理：非塌缩、尺度相容 \(P\)-Palais–Smale 泡树

设 \(M^4\) 为闭定向光滑四维流形，\(g_i\) 满足 (2.1)–(2.5)。则存在子列，使：

1. **统一小能量估计。**  
   存在 \(\delta_0,C_0\)，对所有充分大的 \(i\)，若
   \[
   \int_{B(x,r)}|\operatorname{Rm}|^2\le\delta_0,
   \]
   则
   \[
   \sup_{B(x,r/2)}|\operatorname{Rm}|
   \le
   \left(
   \frac{C_0}{\operatorname{vol}B(x,r)}
   \int_{B(x,r)}|\operatorname{Rm}|^2
   \right)^{1/2}.
   \]

2. **轨形收敛。**  
   \((M,g_i)\) 收敛到紧致四维轨形 \((V,g_\infty)\)，在正则部分光滑收敛。每个正则连通分支上
   \[
   \mathcal E_P(g_\infty)=0,\qquad
   s_{g_\infty}=\mathrm{const}.
   \]

3. **泡树。**  
   每个非平坦吹起极限是完整、非塌缩、有限能量 ALE 轨形；其正则部分满足
   \[
   \mathcal E_P=0,\qquad s=0,\qquad B=0.
   \]

4. **能量分解。**
   \[
   \alpha(M)
   =
   P(g_\infty)+\sum_bP(N_b)+E_{\mathrm{neck}},
   \qquad E_{\mathrm{neck}}\ge0.
   \]
   因而
   \[
   \alpha(M)\ge P(g_\infty)+\sum_bP(N_b).
   \]

5. **链环收费。**  
   每个光滑多端泡满足 (6.3)–(6.4)。带内部轨形点的泡使用 (6.5)，树中成对链环项相消。

6. **拓扑。**  
   \(M\) 由 bulk 截断块和各泡截断块沿 \(S^3/\Gamma\) 链环拼合恢复。只有在所有相关链环均为单支、各泡单端且拼合图为普通树时，才进一步化为普通连通和。

7. **无集中情形。**  
   若无曲率集中，则
   \[
   P(g_\infty)=\alpha(M),
   \]
   且 \(g_\infty\) 是 \(M\) 上的光滑 \(P\)-临界度量。

8. **零缺口情形。**  
   若 \(\alpha(M)=0\)，则 bulk 是 Einstein 轨形，所有泡均 Ricci-flat ALE，且
   \[
   E_{\mathrm{neck}}=0.
   \]
   这给出“Einstein 轨形加 Ricci-flat ALE 树”的结构，但不赋予该树唯一性或某个预定的解消类型。

---

## 12. 认证 cell 的修正推论

令
\[
M=X\#\overline{\mathbb{CP}}^{\,2},
\]
其中 \(X\) 是满足嵌入条件且 \(b^+(X)\ge2\) 的球商。认证 cell 给出
\[
\widehat\alpha(M)
\le0.995662732771115<1.
\tag{12.1}
\]

对满足第 11 节条件的最小化序列：

### 12.1 可直接排除的泡

若 \(N\) 是光滑、一端、\(\Gamma=1\)，且其紧化 \(\widehat N\) 满足
\[
b^+(\widehat N)=0,
\]
则
\[
\widehat P(N)
\ge b_2(\widehat N)+4b_1(\widehat N).
\]
只要
\[
b_1(\widehat N)+b_2(\widehat N)>0,
\]
右侧至少为 \(1\)，与 (12.1) 及总能量下界冲突。

所以认证 cell 排除所有：

* 携带任意负定二阶同调的一端 \(\Gamma=1\) 泡；
* \(b_1>0\) 的一端 \(\Gamma=1\)、\(b^+=0\) 泡；
* 特别是 Burns 泡及任意 \(k\ge1\) 的纯 blow-up 泡。

### 12.2 非塌缩集中仍可能采用的几何形式

若仍有集中，则至少出现以下结构之一：

1. 某个链环具有 \(\Gamma\neq1\)，例如 Ricci-flat Kronheimer 型零 \(P\)-收费；
2. 泡树具有多端、多个锥支或不能化成一端光滑因子的拼合图；
3. 在可写成普通连通和的情形，有一个紧化泡携带 \(b^+>0\)；Seiberg–Witten 分裂随后迫使 bulk 的 \(b^+=0\)；
4. 出现一端、\(\Gamma=1\)、紧化后
   \[
   b_1=b_2=0
   \]
   的同调平凡泡。链环公式对这种泡只给出零拓扑收费，因此不能仅凭 (12.1) 排除其正的 \(P\)-能量。

若没有集中，则
\[
\alpha(M)
\]
由 \(M\) 上一个光滑、常标量、\(B^{1/6}\)-flat 度量实现。若该值为零，该度量就是 Einstein。

对任意最小化序列而言，若统一非塌缩或统一 Sobolev 输入不存在，则上述轨形—ALE 结构不适用；这正对应仍需研究的塌缩或 Sobolev 退化通道。

---

## 13. 对 Step 50.B–C 的具体修订

建议把原文中的以下几处替换：

* “Theorem 50.A replacement”改为明确的 (2.2)–(2.5) 假设，直到 Lemma W 的统一四阶抛物理论完成。
* “energy decomposition”改为 (5.2)，保留 \(E_{\mathrm{neck}}\ge0\)。
* 一般轨形泡的单端公式改为截断块公式 (6.5)。
* “\(M\) is diffeomorphic to the orbifold resolution”改为沿 \(S^3/\Gamma\) 链环的拼合重构。
* \(\Gamma=1\)、\(b^+=0\) 的收费改为
  \[
  b_2+4b_1.
  \]
* 删除由交形式直接识别光滑类型的推断。
* 删除一般情形下
  \[
  \alpha(M)=P(g_\infty)+8\pi^2(k-k')
  \quad\text{和}\quad
  P(g_\infty)=\alpha(V)
  \]
  的表述；仅在第 10 节的真实连通和及 Burns 上界同时成立时使用。
* 认证 cell 的备选项中，\(b_1>0\) 的一端 \(\Gamma=1\) 负定泡应列为被 \(p_*<1\) 排除的类型，而不是逃逸类型。