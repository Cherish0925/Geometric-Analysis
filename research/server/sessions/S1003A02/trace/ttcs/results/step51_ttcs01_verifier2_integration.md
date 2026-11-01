# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 51,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step51_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A02/trace/ttcs/results/step51_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Read the Step-50 note, Anderson orbifold compactness source, GV critical-metric source, and the existing link-charge note. Verify Theorems 50.B–C under a legitimate scale-compatible residual hypothesis and uniform noncollapse/Sobolev input. Check: point-picking and passage to exact P-critical limits; scalar-flatness of ALE bubbles; lower semicontinuity/energy identity; exact APS charge formula and Burns/Eguchi-Hanson/Kronheimer tests; topology of multiple-end/reducible bubbles; Seiberg-Witten connected-sum split; b1 sign in the pure Γ=1 negative-definite charge; claims of sharp equality/attainment of the bulk infimum; and the certified-cell alternatives. Produce a corrected conditional structure theorem that uses Theorem G/link charges without asserting more topology or equality than follows.

## Integrated Scientific Memo

# 核验结论：Theorems 50.B–C 的正确条件形式

Step 50 的基本机制成立，但原 50.B–C 不能按现有文字直接视为已证。主要修正是：

1. 将尚未证明的 Theorem 50.A/Lemma W 输出，暂时替换为明确的尺度相容 Palais–Smale 残差与 own-scale 正则性假设；
2. 加入统一局部 Sobolev 输入，而不只是假设体积非塌缩；
3. 对近临界序列只能先证明模量型 \(\varepsilon\)-正则性，不能直接声称 Anderson 的精确线性估计 (1.5)；
4. 一般能量结论是下半连续性，颈能量消失需另证；
5. 泡的 APS 收费必须允许多端和内部轨形链环；
6. \(\Gamma=1\)、负定紧化泡的正确收费是 \(b_2+4b_1\)，不是 \(b_2-2b_1\)；
7. 一般拓扑重构是沿 \(S^3/\Gamma\) 链环拼合，不自动是普通连通和；
8. bulk attainment 和精确等式只在额外标准性及 Burns 插入假设下成立；
9. certified-cell 情形中，\(b_1>0\) 的 \(\Gamma=1\) 负定泡是被排除的通道，不是逃逸通道。

---

## 1. 合法的解析假设

设 \(g_i\) 是 \(M^4\) 上的单位体积最小化序列，
\[
P(g_i)\to\alpha(M),\qquad P(g)=\int_M|\Ric^\circ_g|^2\,d\mu_g.
\]

记 \(\mathcal E_P(g)=\nabla^{L^2}P(g)\)，并令 \(\rho_i\) 为光滑曲率尺度函数，与截断曲率半径 \(r_i\) 一致到固定常数：
\[
c\,r_i\le \rho_i\le C\,r_i.
\]

一个足够且尺度正确的条件组是：

### (PS) 尺度相容残差
\[
\varepsilon_i^2
:=
\int_M \rho_i^4|\mathcal E_P(g_i)|^2\,d\mu_{g_i}
\longrightarrow0.
\tag{1.1}
\]

### (NC) 非塌缩
\[
\vol_{g_i}B(x,r)\ge \nu_0 r^4,\qquad 0<r\le1.
\tag{1.2}
\]

### (S) 统一局部 Sobolev 不等式
\[
\left(\int_{B(x,r)}|u|^4\right)^{1/2}
\le C_S\left(
\int_{B(x,r)}|\nabla u|^2+r^{-2}\int_{B(x,r)}u^2
\right).
\tag{1.3}
\]

### (R) own-scale 紧致性
例如对所有 \(m\ge1\)，
\[
\rho_i(x)^{m+2}
\sup_{B(x,c\rho_i(x))}
|\nabla^m\Rm_{g_i}|
\le C_m.
\tag{1.4}
\]
等价地，也可假设足以通过规范化四阶椭圆方程的统一调和坐标控制。

Anderson Proposition 3.5 的常数依赖 Sobolev 常数；源文献 Remark 3.10 只说体积下界仍须假设，并未给出仅依赖 \(\nu_0\) 的临界度量 \(\varepsilon\)-正则性。因此原 50.B 中“常数只依赖 \(\nu_0\)”缺乏来源支持。若以后证明了从 (NC) 导出所需局部 Sobolev 常数的版本，才可删除 (S)。

Theorem 50.A 的加权流可能产生 (1.1)–(1.4)，但当前 Lemma W 只是提纲。四阶流没有最大值原理；仅由零阶曲率界和形式上的强抛物性，尚不足以证明统一 own-scale 生存时间和尺度保持。因此 50.B–C 应先以这些性质作为条件。

---

## 2. 点选与精确 \(P\)-临界极限

若在
\[
B_{g_i}(y_i,A_i\lambda_i),\qquad A_i\to\infty,
\]
上点选使
\[
r_i\ge c\lambda_i,\qquad
|\Rm_{g_i}|\le C\lambda_i^{-2},
\]
并令
\[
\widetilde g_i=\lambda_i^{-2}g_i,
\]
则四维缩放给出
\[
\int_{B_{\widetilde g_i}(y_i,A)}
|\mathcal E_P(\widetilde g_i)|^2\,d\mu_{\widetilde g_i}
=
\lambda_i^4
\int_{B_{g_i}(y_i,A\lambda_i)}
|\mathcal E_P(g_i)|^2\,d\mu_{g_i}.
\]
由 \(\rho_i\ge c\lambda_i\)，
\[
\int_{B_{\widetilde g_i}(y_i,A)}
|\mathcal E_P(\widetilde g_i)|^2
\le c^{-4}\varepsilon_i^2\to0.
\tag{2.1}
\]

结合 (NC)、(S)、(R)，固定球上可取光滑 Cheeger–Gromov 极限
\[
(N,g_N,y_\infty),
\]
且
\[
\mathcal E_P(g_N)=0
\]
弱意义成立；规范化椭圆性继而给出光滑性。

由 GV 的参数关系
\[
P=\frac12\mathcal B_{1/6}-16\pi^2\chi,
\]
故
\[
P\text{-critical}
\iff B^{1/6}=0.
\]
其取迹方程为
\[
\Delta s=0,
\]
闭情形下 \(s\) 为常数，并且
\[
B=\frac13s\,\Ric^\circ.
\tag{2.2}
\]

---

## 3. 近临界序列的 \(\varepsilon\)-正则性范围

原 50.B 的点选反证足以证明：

### 曲率尺度不塌缩
存在 \(\delta_0,K\)，使充分大的 \(i\) 满足
\[
\int_{B(x,r)}|\Rm|^2\le\delta_0
\quad\Longrightarrow\quad
r^2\sup_{B(x,r/2)}|\Rm|\le K.
\tag{3.1}
\]

还可得到模量形式：

### 模量型小能量正则性
对每个 \(\eta>0\)，存在 \(\delta(\eta)>0\) 与 \(i_0(\eta)\)，使
\[
\int_{B(x,r)}|\Rm|^2\le\delta(\eta)
\quad\Longrightarrow\quad
r^2\sup_{B(x,r/2)}|\Rm|\le\eta
\tag{3.2}
\]
对 \(i\ge i_0(\eta)\) 成立。

证明是点选、重标度及 (2.1)：若 (3.2) 失败，得到非平坦精确 \(P\)-临界极限，但其局部总曲率趋零，矛盾。

然而，这并不直接证明 Anderson 的定量线性形式
\[
\sup_{B(x,r/2)}|\Rm|
\le
\left(
\frac{C_0}{\vol B(x,r)}
\int_{B(x,r)}|\Rm|^2
\right)^{1/2}.
\tag{3.3}
\]
对近临界度量，Euler–Lagrange 残差作为椭圆方程的非齐次项出现；点选极限为平坦并不能控制曲率与能量平方根之比。

修正方式是：用 (3.1)–(3.2) 重跑 Anderson 的 good/bad-ball 论证；所有吹起极限本身是精确临界度量，因此在极限上可由 Anderson Remark 3.10、Lemma 3.3、Proposition 3.5 使用真正的 (3.3)。这足以得到轨形紧致性和 ALE 泡树，但不应声称原序列已直接满足同一线性估计。

---

## 4. ALE 泡必为标量平坦

在完整有限能量 ALE 泡上，\(s\) 调和且
\[
s\in L^2(N).
\]
取截断函数 \(\eta_R\)，有
\[
0=\int \eta_R^2s\,\Delta s
\]
从而
\[
\int_{B_R}|\nabla s|^2
\le
CR^{-2}\int_{B_{2R}\setminus B_R}s^2\to0.
\]
故 \(s\) 为常数。ALE 空间体积无限而 \(s\in L^2\)，所以
\[
s\equiv0.
\tag{4.1}
\]
由 (2.2)，每个泡满足
\[
B=0.
\tag{4.2}
\]
因此泡是标量平坦 Bach-flat ALE 轨形。若其 \(P\)-能量为零，则
\[
\Ric^\circ=0,\qquad s=0,
\]
故为 Ricci-flat。

对可能可约的 bulk 轨形，\(s\) 只能断言在每个正则连通分支上为常数；不同锥支汇聚于一点时，不应未经可移奇点论证就断言这些常数相同。

---

## 5. 能量：已证的是下半连续性

对 bulk 正则部分和每个尺度分离的泡核心，光滑局部收敛及 \(P\) 的尺度不变性给出
\[
\alpha(M)
\ge
P(g_\infty)+\sum_bP(N_b).
\tag{5.1}
\]

更完整地可定义
\[
\alpha(M)
=
P(g_\infty)+\sum_bP(N_b)+E_{\rm neck},
\qquad E_{\rm neck}\ge0,
\tag{5.2}
\]
其中 \(E_{\rm neck}\) 是未被已抽取核心吸收的颈区极限能量。

现有来源没有证明
\[
E_{\rm neck}=0.
\tag{5.3}
\]
这需要独立的无颈估计，例如
\[
\lim_{R\to\infty}\lim_{\rho\to0}\lim_i
\int_{\mathrm{neck}_i(R,\rho)}
|\Ric^\circ|^2\,d\mu=0.
\]
Anderson 的轨形紧致性本身只支持 (5.1)。

若没有曲率集中，则全局光滑收敛，因而
\[
P(g_\infty)=\alpha(M);
\]
这时确实得到 \(M\) 上的光滑 \(P\)-临界极小度量。

---

## 6. 正确的 APS/链环收费

### 6.1 光滑多端标量平坦 ALE 空间

设 \(N\) 有端 \(S^3/\Gamma_e\)，并采用
\[
\frac1{12\pi^2}\int_N(|W^+|^2-|W^-|^2)
=
\tau(N)+\sum_e\eta_{\Gamma_e}
\tag{6.1}
\]
的约定。则 Theorem G 给出，对 \(\sigma=\pm1\)，
\[
\boxed{
\widehat P(N)
=
\frac1{2\pi^2}\int_N|W^\sigma|^2
-\bigl(2\chi(N)+3\sigma\tau(N)\bigr)
+\sum_e\left(\frac2{|\Gamma_e|}-3\sigma\eta_{\Gamma_e}\right).
}
\tag{6.2}
\]
从而
\[
\boxed{
\widehat P(N)\ge
\left[
2\sum_e\frac1{|\Gamma_e|}
-2\chi(N)
+3\left|\tau(N)+\sum_e\eta_{\Gamma_e}\right|
\right]_+.
}
\tag{6.3}
\]

原 50.C 的公式只适用于光滑单端泡。

### 6.2 带内部轨形点的泡块

若从泡中挖去内部轨形奇点邻域，并截断所有外端，得到光滑紧致块 \(\Omega\)，则
\[
\widehat P(\Omega)
=
\frac1{2\pi^2}\int_\Omega|W^\sigma|^2
+\frac1{96\pi^2}\int_\Omega s^2
-\bigl(2\chi(\Omega)+3\sigma\tau(\Omega)\bigr)
+\sum_{\rm out}q_\sigma
-\sum_{\rm in}q_\sigma,
\tag{6.4}
\]
其中
\[
q_\sigma(\Gamma)=\frac2{|\Gamma|}-3\sigma\eta_\Gamma.
\]
完整泡树中，每个内部链环同时作为父块的 in-link 和子块的 out-link，因而电荷成对相消。这是比“逐泡赋一个不含内部链环的电荷”更可靠的表述。

### 6.3 模型检验

- 平坦 \(\mathbb R^4\)：
  \[
  \chi=1,\quad\tau=0,\quad\Gamma=1
  \quad\Longrightarrow\quad \widehat P=0.
  \]

- Burns：
  \[
  \chi=2,\quad\tau=-1,\quad\Gamma=1,\quad W^+=0,
  \]
  故
  \[
  \widehat P=-(4-3)+2=1.
  \]

- Eguchi–Hanson：
  \[
  \chi=2,\quad\tau=-1,\quad|\Gamma|=2,\quad W^+=0,\quad P=0,
  \]
  得本约定下
  \[
  \eta_{\mathbb Z_2}=0.
  \]

- Kronheimer ADE，设 \(b_2=r\)：
  \[
  \chi=1+r,\qquad\tau=-r,\qquad W^+=0,\qquad P=0,
  \]
  因而
  \[
  3\eta_\Gamma=r-2+\frac2{|\Gamma|}.
  \tag{6.5}
  \]
  代入 (6.3) 恰得零收费。

因此“scalar-flat bubbles never save”是错误的：Kronheimer Ricci-flat ALE 泡可以携带二阶拓扑而 \(P=0\)。正确结论仅是：\(\Gamma=1\)、负定、单端泡没有次单位收费。

---

## 7. \(\Gamma=1\) 负定泡的 \(b_1\) 符号

设 \(N\) 光滑、单端、\(\Gamma=1\)，以四球封端得到闭流形 \(\widehat N\)。若
\[
b^+(\widehat N)=0,\qquad
m=b_2(\widehat N),\qquad
q=b_1(\widehat N),
\]
则
\[
\chi(N)=\chi(\widehat N)-1=1-2q+m,\qquad
\tau(N)=-m.
\]
由 (6.3)，
\[
\boxed{\widehat P(N)\ge m+4q.}
\tag{7.1}
\]

所以原文的 \(m-2q\) 符号和系数都错误。\(b_1\) 增加收费。

特别地，
\[
N\simeq\mathbb R^4\#k\,\overline{\mathbb{CP}}^{\,2},
\qquad b_1=0
\]
给出
\[
\widehat P(N)\ge k,
\tag{7.2}
\]
Burns 达到 \(k=1\) 的等号。

若有 \(\kappa\) 个 \(\Gamma=1\) 端且可同时光滑封端，负定情形给出
\[
\widehat P(N)\ge b_2+4b_1+4\kappa-4.
\tag{7.3}
\]
因此额外端和 \(S^1\times S^3\) 型拓扑的收费至少为 \(4\)。

这些结论直接来自 Theorem G，不需要 Donaldson 对角化。Donaldson 只能给交形式信息，不能把流形微分同胚识别为
\(\#_m\overline{\mathbb{CP}}^{\,2}\)。

---

## 8. 多端、可约轨形点及拓扑重构

Anderson 支持的拓扑结论是：

1. 截去 bulk 中各锥邻域；
2. 截去泡块的外端和内部轨形点邻域；
3. 沿成对的 \(S^3/\Gamma\) 链环拼回 \(M\)。

若出现多端泡、一个轨形点的多个锥支，或拼合图有回路，则可能产生 \(S^1\times S^3\) 型拓扑，不能一般写成
\[
M\cong V\#\widehat N_1\#\cdots\#\widehat N_m.
\tag{8.1}
\]
“\(M\) 是 \(V\) 的轨形解消”也只适用于单锥、单端、无回路的树状情形。

在一个分离的 \(\Gamma=1\) 单链环上，正确的普通连通和因子是整个被链环包围区域 \(D\) 的封端 \(\widehat D\)，不一定是某一层单独泡的紧化，因为该区域内部仍可能含 \(\Gamma'\ne1\) 的更深泡。

统一 Sobolev 常数结合 Anderson Proposition 3.6 可排除某些可约锥点，但仍需链环确实分离。若 \(b_1(M)=0\)，任意定向三维链环分离，因此这一条件特别有用。

---

## 9. Seiberg–Witten 分裂的精确范围

只有在已经得到真实的光滑普通连通和
\[
M\cong V\#Y_1\#\cdots\#Y_m
\tag{9.1}
\]
时，才能直接调用通常的 SW 连通和消失定理。

若
\[
M=X\#k\overline{\mathbb{CP}}^{\,2},\qquad
b^+(X)\ge2,\qquad SW(M)\ne0,
\]
则 (9.1) 中至多一个因子具有正 \(b^+\)。由于
\[
b^+(M)=b^+(X)\ge2,
\]
恰有一个因子携带所有正方向：

- 若每个 \(Y_b\) 都有 \(b^+(Y_b)=0\)，则
  \[
  b^+(V)=b^+(M).
  \]
- 若某个 \(Y_b\) 有 \(b^+>0\)，则它是唯一这样的泡因子，并且
  \[
  b^+(V)=0.
  \]

这不推出：

- \(V\cong X\#k'\overline{\mathbb{CP}}^{\,2}\)；
- \(Y_b\cong\#_{m_b}\overline{\mathbb{CP}}^{\,2}\)；
- 多端或轨形泡可进入普通连通和式 (9.1)。

对一般球面空间形式链环，如需使用规范场分裂，必须另行证明相应 neck-stretching 版本；不能把普通 \(S^3\) 连通和定理无条件外推。

---

## 10. bulk attainment 与精确等式

一般有泡时，\(g_\infty\) 只是 \(P\)-临界，并不自动极小。若 bulk 可光滑封端为 \(\widehat V\)，至多有
\[
P(g_\infty)\ge\alpha(\widehat V),
\tag{10.1}
\]
而且若 \(g_\infty\) 在封端点仅为轨形或 \(C^0\)，还需平滑化或可移奇点论证。

精确等式可在如下额外假设下恢复：

1. bulk 封端为光滑 \(\widehat V\)；
2. 有真实微分同胚
   \[
   M\cong\widehat V\#r\,\overline{\mathbb{CP}}^{\,2};
   \]
3. 集中区域的总链环收费至少为 \(r\)；
4. Burns 插入给出
   \[
   \alpha(M)\le\alpha(\widehat V)+8\pi^2r.
   \]

此时
\[
\alpha(M)
\ge P(g_\infty)+8\pi^2r
\ge \alpha(\widehat V)+8\pi^2r,
\]
与上界合并得
\[
\boxed{
\alpha(M)=\alpha(\widehat V)+8\pi^2r,
\qquad
P(g_\infty)=\alpha(\widehat V).
}
\tag{10.2}
\]
并且所有中间不等式成为等号，故相应情形下可反推出
\[
E_{\rm neck}=0.
\]

没有真实连通和、标准泡拓扑和匹配 Burns 上界时，原 50.C(3) 的 sharp equality 与 bulk attainment 均不能断言。

---

## 11. 修正后的条件结构定理

### 定理（非塌缩尺度相容 \(P\)-Palais–Smale 泡树）

设 \(g_i\) 满足 (1.1)–(1.4)。则存在子列，使：

1. **小能量控制。**  
   (3.1) 和 (3.2) 成立。精确线性 Anderson 估计仅对所得精确临界极限使用。

2. **轨形极限。**  
   \((M,g_i)\) 收敛到紧致四维轨形 \((V,g_\infty)\)，在正则部分光滑收敛。每个正则连通分支上
   \[
   \mathcal E_P(g_\infty)=0,\qquad s_{g_\infty}=\mathrm{const}.
   \]

3. **ALE 泡树。**  
   每个非平坦吹起极限是完整、非塌缩、有限能量 ALE 轨形；其正则部分满足
   \[
   \mathcal E_P=0,\qquad s=0,\qquad B=0.
   \]

4. **能量下界。**
   \[
   \alpha(M)
   =
   P(g_\infty)+\sum_bP(N_b)+E_{\rm neck},
   \qquad E_{\rm neck}\ge0,
   \]
   因而
   \[
   \alpha(M)\ge P(g_\infty)+\sum_bP(N_b).
   \]

5. **链环收费。**  
   对每个截断光滑泡块 \(D\)，
   \[
   \mathfrak c(D)=
   \left[
   \max_{\sigma=\pm1}
   \left\{
   \sum_{\rm out}q_\sigma(\Gamma)
   -\sum_{\rm in}q_\sigma(\Gamma)
   -(2\chi(D)+3\sigma\tau(D))
   \right\}
   \right]_+,
   \tag{11.1}
   \]
   且
   \[
   \widehat P(D)\ge\mathfrak c(D).
   \]
   树中内部链环电荷相消。对光滑多端泡，(11.1) 化为 (6.3)。

6. **拓扑。**  
   \(M\) 由 bulk 截断块和泡截断块沿 \(S^3/\Gamma\) 拼合恢复。只有在所有链环分离、单锥、泡单端且拼合图为普通树时，才化为普通连通和。

7. **无集中。**  
   若无曲率集中，则
   \[
   P(g_\infty)=\alpha(M),
   \]
   且 \(g_\infty\) 是 \(M\) 上光滑 \(P\)-临界极小度量。

8. **零缺口。**  
   若 \(\alpha(M)=0\)，则
   \[
   P(g_\infty)=0,\qquad P(N_b)=0,\qquad E_{\rm neck}=0.
   \]
   因而 bulk 每个正则分支是 Einstein，所有泡均 Ricci-flat ALE。非平凡 \(\Gamma=1\) Ricci-flat ALE 泡还可由 Bishop–Gromov 刚性排除；非平凡零收费集中必须经过 \(\Gamma\ne1\) 链环。

9. **SW 结论。**  
   仅在所得链环分解确实化为普通连通和时，SW 非消失才推出恰有一个封端因子携带全部 \(b^+\)。

---

## 12. certified cell 的正确备选结构

令
\[
M=X\#\overline{\mathbb{CP}}^{\,2},
\]
其中 \(X\) 为满足嵌入条件且 \(b^+(X)\ge2\) 的球商。采用 Step 50 给出的认证值
\[
\widehat\alpha(M)
\le 0.995662732771115<1.
\tag{12.1}
\]

对满足上述条件定理的最小化序列：

### 可直接排除

若一个集中区域具有单个 \(\Gamma=1\) 外链环，且其封端满足
\[
b^+=0,
\]
则
\[
\widehat P(D)\ge b_2(\widehat D)+4b_1(\widehat D).
\tag{12.2}
\]
因此只要
\[
b_1(\widehat D)+b_2(\widehat D)>0,
\]
收费至少为 \(1\)，与总能量 \(<1\) 矛盾。

特别排除：

- Burns 泡；
- 任意携带负定二阶同调的一端 \(\Gamma=1\) 泡；
- \(b_1>0\) 的一端 \(\Gamma=1\)、\(b^+=0\) 泡；
- 纯 \(\Gamma=1\) 多端或 handle 型结构，其附加收费至少为 \(4\)。

所以原 certified-cell alternatives 中的“\(b_1>0\) bubble”应删除。

### 仍可能发生

1. **无集中：**
   \[
   \alpha(M)
   \]
   由 \(M\) 上光滑、常标量、\(B^{1/6}\)-flat 度量实现。

2. **\(\Gamma\ne1\) 集中：**  
   例如 Kronheimer Ricci-flat ALE 可有零 \(P\)-收费；一般 lens-link 块也可能有次单位收费。

3. **正 \(b^+\) 转移：**  
   在确有普通连通和分解时，一个封端集中区域携带全部 \(b^+(M)\)，而 bulk 为 \(b^+=0\)。现有纯拓扑收费不足以排除此支。

4. **\(\Gamma=1\) 同调平凡区域：**
   \[
   b_1(\widehat D)=b_2(\widehat D)=0.
   \]
   Theorem G 对其只给零拓扑收费；若其实际 \(P\)-能量小于 \(1\)，不能仅由电荷排除。

5. **Sobolev 退化或塌缩：**  
   若统一 (S) 或 (NC) 失败，上述轨形–ALE 结构不适用。Taub–NUT/ALF 的 \((-2,2)\) 链环收费属于这一退化通道。

若在无集中支中 \(\alpha(M)=0\)，所得光滑临界度量就是 Einstein。

---

## 13. 应对 Step 50 作出的直接文字修订

- 以明确的 (PS)+(NC)+(S)+(R) 替代尚未完成的 Theorem-50.A replacement。
- 不声称近临界序列满足 Anderson 的精确线性 (1.5)；改用尺度界加模量型 \(\varepsilon\)-正则性，并只对精确临界极限调用 Anderson。
- 能量结论写成
  \[
  \alpha=P(g_\infty)+\sum P(N_b)+E_{\rm neck},
  \qquad E_{\rm neck}\ge0.
  \]
- 一般泡收费改用带内外链环的 Theorem G 公式。
- “orbifold resolution”改为沿 \(S^3/\Gamma\) 的链环拼合重构。
- 将负定 \(\Gamma=1\) 收费修正为
  \[
  b_2+4b_1.
  \]
- 删除由 Donaldson 对角化直接识别微分同胚类型的推断。
- 删除一般有泡情形下
  \[
  P(g_\infty)=\alpha(V),\qquad
  \alpha(M)=P(g_\infty)+8\pi^2r
  \]
  的无条件表述；仅在第 10 节额外假设下恢复。
- 将“scalar-flat bubbles never save”改为“单端 \(\Gamma=1\)、负定泡无次单位收费”；\(\Gamma\ne1\) 的 scalar-flat/Ricci-flat 泡可以零收费或次单位收费。
- certified-cell 备选项中，\(b_1>0\) 的 \(\Gamma=1\) 负定泡属于被排除通道，而不是剩余通道。