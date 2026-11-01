# TTCS Independent Branch Record

```json
{
  "step_id": 14,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/originals/0911_3104__Smoothing_Riemannian_Metrics_with_Bounded_Ricci_Curvatures_in_Dimens.pdf",
    "Knowledge/objects/papers/0911.3104-Smoothing-Riemannian-Metrics-with-Bounded-Ricci-Curvatures-in--fc5404da6e14--415cdf5be1eb/object.md",
    "Sessions/S0910A03/workspace/notes/step13_smoothing_bridge_and_L2_propagation.md",
    "Sessions/S0910A03/trace/ttcs/results/step13_ttcs01_verifier1_integration.md"
  ]
}
```

## Task

Read Ye Li's actual paper and the Step 13 smoothing note in light of the Strategist correction. Reconstruct rigorously the source-based estimate for the normalized Einstein defect E=Ric+g under normalized Ricci flow, focusing on Corollary 3.5. Determine the correct scaling, Sobolev constant A and volume cancellation, the subsolution inequality for u=(|E|^2+eta)^{1/2}, normalized-vs-unnormalized flow conversion, and exactly which global/local all-centers, evolving curvature-energy, cutoff, metric-equivalence, and boundary hypotheses are needed. Explicitly identify any source typographical ambiguity such as the cutoff phi^2 in Cor. 3.5. Assess whether one can obtain |E(x,t)| <= C delta (r^2/t)^(2/3) uniformly on an interior ball and metric drift O(delta r^(4/3)t^(1/3)); do not assume the flawed Step 13 inner/outer Gronwall. Give a direct mathematical memo with derivations and a precise conditional lemma.

## Output

# 科学核验备忘录：Ye Li Corollary 3.5 与归一化 Einstein 缺陷

## 1. Corollary 3.5 真正提供的估计

Ye Li 使用四维 Dirichlet–Sobolev 系数 \(A\)：

\[
\left(\int_{B_r(y)}v^4\,d\mu_s\right)^{1/2}
\le A_y\int_{B_r(y)}|\nabla v|^2\,d\mu_s,
\qquad v\in C^\infty_0(B_r(y)).
\tag{1.1}
\]

这里的 \(A_y\) 在四维无量纲。论文第 4 页给出

\[
A_y\le C
\left(\frac{r^4}{V_0(B_r(y))}\right)^{1/2}
=
C\frac{r^2}{V_0(B_r(y))^{1/2}}.
\tag{1.2}
\]

若 \(\frac12g_0\le g(s)\le2g_0\)，固定初始球上的测度、梯度与 \(L^4\) 范数彼此可比，所以 (1.1) 在演化中仍成立，只改变一个维数常数。

令 \(f\ge0\) 满足 Theorem 3.4 的方程与体积形式条件：

\[
(\partial_s-\Delta)f\le C_0f^2,
\qquad
\partial_s d\mu_s\le c f\,d\mu_s.
\tag{1.3}
\]

其关键动态小量不是单独的初始 \(L^2\) 能量，而是

\[
A_y\|f(s)\|_{L^2(B_r(y),g(s))}\le \theta_0
\tag{1.4}
\]

在所有相关中心与所有相关时刻成立，其中 \(\theta_0\) 足够小。Theorem 3.4 的覆盖论证正是用初始全中心小能量来维持 (1.4)。同一论证给出论文第 12 页的估计

\[
\int_{B_r(y)}f^3(s)\,d\mu_s
\le C N A_y e_y^3\,s^{-1},
\qquad
e_y=\sup_{\sigma\le s}
\|f(\sigma)\|_{L^2(B_r(y),g(\sigma))}.
\tag{1.5}
\]

若写成 Theorem 2.5 的记号，

\[
\mu_y^3=CNA_y e_y^3,
\qquad
A_y^2\mu_y^3=CN(A_y e_y)^3,
\tag{1.6}
\]

所以 Moser 常数由 (1.4) 一致控制，与球体积无关。

现在令 \(u\ge0\) 满足

\[
(\partial_s-\Delta)u\le c_0fu.
\tag{1.7}
\]

取固定于 \(g_0\) 的截断函数 \(\chi\)，则对 \(z=\chi u^{3/2}\)，标准计算给出

\[
\begin{aligned}
\frac d{ds}\int\chi^2u^3\,d\mu_s
+c\int|\nabla z|^2\,d\mu_s
\le {}&
C r^{-2}\int_{\operatorname{supp}\chi}u^3\,d\mu_s\\
&+C\int f z^2\,d\mu_s .
\end{aligned}
\tag{1.8}
\]

反应项满足

\[
\int fz^2
\le \|f\|_2\|z\|_4^2
\le A_y\|f\|_2\int|\nabla z|^2.
\tag{1.9}
\]

由 (1.4) 可吸收最后一项。配合有限重数覆盖与嵌套截断，可得

\[
\sup_{0\le \sigma\le s}
\int_{B_r(x)}u^3(\sigma)\,d\mu_\sigma
\le
C\int_{B_{3r}(x)}u^3(0)\,d\mu_0,
\qquad s\le c r^2.
\tag{1.10}
\]

将 Theorem 2.5 取 \(p_0=3\)，再用 (1.5)、(1.6) 和 (1.10)，得到

\[
\begin{aligned}
u(x,s)
&\le
C A_x^{2/3}
\left(s^{-1}+r^{-2}\right)
\left(
\int_0^s\int_{B_r(x)}u^3
\right)^{1/3} \\
&\le
C A_x^{2/3}s^{-2/3}
\left(
\int_{B_{3r}(x)}u^3(0)\,d\mu_0
\right)^{1/3},
\qquad 0<s\le c r^2.
\end{aligned}
\tag{1.11}
\]

这就是 Corollary 3.5 的来源。论文第 13 页第一行中的 \(C_3\int u^3\) 隐含了截断梯度；恢复尺度后应读作 \(Cr^{-2}\int u^3\)。

---

## 2. 两次精确的体积消去

设初始归一化曲率能量为

\[
\varepsilon_y(r)
=
\frac{r^4}{V_0(B_r(y))}
\int_{B_r(y)}|\Rm(g_0)|^2\,d\mu_0.
\tag{2.1}
\]

由 (1.2)，

\[
\begin{aligned}
A_y\|\Rm(g_0)\|_{L^2(B_r(y))}
&\le
C\frac{r^2}{V_y^{1/2}}
\left(\frac{\varepsilon_yV_y}{r^4}\right)^{1/2}\\
&=C\varepsilon_y^{1/2}.
\end{aligned}
\tag{2.2}
\]

这是使曲率项可吸收的第一次体积消去。

若初始 Einstein 缺陷满足

\[
|E(0)|_{g_0}\le\delta
\quad\text{于 }B_{3r}(x),
\tag{2.3}
\]

则 Corollary 3.5 右端满足

\[
\begin{aligned}
A_x^{2/3}
\left(\int_{B_{3r}(x)}|E(0)|^3\,d\mu_0\right)^{1/3}
&\le
C\left(\frac{r^2}{V_0(B_r(x))^{1/2}}\right)^{2/3}
\delta V_0(B_{3r}(x))^{1/3}\\
&=
C\delta r^{4/3}
\left(
\frac{V_0(B_{3r}(x))}
{V_0(B_r(x))}
\right)^{1/3}.
\end{aligned}
\tag{2.4}
\]

Ricci 下界和 \(r\le1\) 给出

\[
\frac{V_0(B_{3r}(x))}{V_0(B_r(x))}
\le D(n,Kr^2),
\tag{2.5}
\]

即使球严重塌缩，这个比值仍一致有界。因此

\[
u(x,s)\le
C\delta r^{4/3}s^{-2/3}
=
C\delta\left(\frac{r^2}{s}\right)^{2/3}.
\tag{2.6}
\]

这是第二次体积消去。它依赖的正是 \(A^{2/3}\) 与初始 \(L^3\) 范数，而不是 Step 13 中另行写出的内球/外球 \(L^2\) Gronwall。

---

## 3. \(E\) 的标量次解：正则化计算

对于归一化流

\[
\partial_tg=-2(\Ric+g),\qquad E=\Ric+g,
\tag{3.1}
\]

已有精确公式

\[
(\partial_t-\Delta)|E|^2
=
-2|\nabla E|^2+
4R_{ikjl}E_{ij}E_{kl}.
\tag{3.2}
\]

取

\[
u_\eta=(|E|^2+\eta)^{1/2}.
\tag{3.3}
\]

若 \(F=|E|^2\)，则

\[
(\partial_t-\Delta)u_\eta
=
\frac{(\partial_t-\Delta)F}{2u_\eta}
+
\frac{|\nabla F|^2}{4u_\eta^3}.
\tag{3.4}
\]

利用

\[
|\nabla F|^2\le4F|\nabla E|^2
\tag{3.5}
\]

可得梯度部分

\[
-\frac{|\nabla E|^2}{u_\eta}
+\frac{F|\nabla E|^2}{u_\eta^3}
=
-\frac{\eta|\nabla E|^2}{u_\eta^3}\le0.
\tag{3.6}
\]

曲率部分给出

\[
\frac{2\,\Rm(E,E)}{u_\eta}
\le 2|\Rm|\frac{|E|^2}{u_\eta}
\le2|\Rm|u_\eta.
\tag{3.7}
\]

所以

\[
\boxed{
(\partial_t-\Delta)u_\eta
\le2|\Rm|u_\eta.
}
\tag{3.8}
\]

令 \(\eta\downarrow0\) 后，\(|E|\) 在 barrier 或分布意义下满足同一不等式。

不过，Ye Li 的 Corollary 3.5 写于非归一化 Ricci 流中。最干净的使用方式是先作精确流转换，而不是直接把论文结论套到 (3.1)。

---

## 4. 归一化流与非归一化流的精确转换

设

\[
\partial_s\bar g=-2\Ric_{\bar g},\qquad \bar g(0)=g_0,
\tag{4.1}
\]

并定义

\[
s=\frac{e^{2t}-1}{2},
\qquad
g(t)=e^{-2t}\bar g(s)
=\frac1{1+2s}\bar g(s).
\tag{4.2}
\]

则 \(g\) 满足 (3.1)。

令

\[
q(s)=\frac1{1+2s},\qquad
H(s)=\Ric_{\bar g}+q(s)\bar g.
\tag{4.3}
\]

作为协变二阶张量，

\[
H(s)=E(t).
\tag{4.4}
\]

但范数按

\[
|E(t)|_{g(t)}
=(1+2s)|H(s)|_{\bar g(s)}
=e^{2t}|H(s)|_{\bar g(s)}
\tag{4.5}
\]

转换。

由于 \(\Delta_L\bar g=0\)、\(q'=-2q^2\)，有

\[
\partial_sH=\Delta_LH-2qH.
\tag{4.6}
\]

在非归一化流下，逆度量变化产生的 Ricci 收缩项与 \(\Delta_L\) 中的 Ricci 收缩项相消，故

\[
(\partial_s-\Delta_{\bar g})|H|^2
=
-2|\nabla H|^2
+4\bar R_{ikjl}H_{ij}H_{kl}
-4q|H|^2.
\tag{4.7}
\]

因此

\[
\bar u_\eta=(|H|_{\bar g}^2+\eta)^{1/2}
\]

满足

\[
(\partial_s-\Delta_{\bar g})\bar u_\eta
\le2|\Rm(\bar g)|\,\bar u_\eta.
\tag{4.8}
\]

附加的 \(-4q|H|^2\) 对上界有利，可以舍去。于是 Corollary 3.5 可取

\[
f=|\Rm(\bar g)|,\qquad u=|H|.
\tag{4.9}
\]

若 \(0<t\le c r^2\le c\)，则 \(s\ge t\) 且 \(e^{2t}\le C\)。由 (2.6) 和 (4.5)，

\[
\boxed{
|E(x,t)|_{g(t)}
\le
C\delta
\left(\frac{r^2}{t}\right)^{2/3}.
}
\tag{4.10}
\]

四维中，Dirichlet–Sobolev 系数 \(A\) 以及
\(\int|\Rm|^2d\mu\) 都在常数倍缩放下不变，所以转换 (4.2) 不破坏临界能量结构。

---

## 5. 由缺陷估计得到归一化度量漂移

对固定非零切向量 \(v\)，

\[
\partial_t\log g(t)(v,v)
=
-2\frac{E(v,v)}{g(v,v)}.
\tag{5.1}
\]

于是由 (4.10)，

\[
\begin{aligned}
\left|
\log\frac{g(t)(v,v)}{g_0(v,v)}
\right|
&\le
2\int_0^t|E(x,\tau)|_{g(\tau)}\,d\tau\\
&\le
C\delta r^{4/3}
\int_0^t\tau^{-2/3}\,d\tau\\
&=
C\delta r^{4/3}t^{1/3}.
\end{aligned}
\tag{5.2}
\]

所以

\[
e^{-D(t)}g_0\le g(t)\le e^{D(t)}g_0,
\qquad
D(t)=C\delta r^{4/3}t^{1/3}.
\tag{5.3}
\]

当 \(D(t)\le1\) 时，

\[
\|g(t)-g_0\|_{g_0}
\le C\delta r^{4/3}t^{1/3}.
\tag{5.4}
\]

因此题目中提出的漂移阶数正确；它是归一化流的漂移。非归一化流本身还含有 Einstein 背景的整体缩放，必须先按 (4.2) 消去。

---

## 6. Corollary 3.5 中的 \(\phi^2\) 排印歧义

论文第 12 页写道

\[
\partial_tu\le \phi^2(\Delta u+c_0fu).
\tag{6.1}
\]

这里存在三个文本事实：

1. Corollary 3.5 的陈述没有定义这个 \(\phi\)；
2. Theorem 2.5 假设的是
   \[
   \partial_tu\le\Delta u+c_0fu,
   \]
   不能直接从 (6.1) 推出，因为 \(\Delta u\) 没有固定符号；
3. 论文随后把 Corollary 3.5 用于普通 Ricci 流的 Ricci 张量，而方程 (3.3) 没有 \(\phi^2\)。

同样，Theorem 3.1 的证明中还出现

\[
\partial_t|\Rm|^2
=
\phi^2\Delta|\Rm|^2-2|\nabla\Rm|^2+\Rm*\Rm*\Rm,
\]

而全局 Ricci 流应为没有该 \(\phi^2\) 的公式。这些痕迹与从局部 Ricci 流论证复制文本相符。

因此，与论文前后推导一致并且可直接证明的版本是

\[
\boxed{
\partial_tu\le\Delta u+c_0fu.
}
\tag{6.2}
\]

若确实研究 \(\partial_tu\le\phi^2\Delta u+\cdots\)，则分部积分会出现 \(\nabla\phi\) 项，还需重新处理退化主部；论文显示的单行证明没有给出这套推导。

另一个相关排印问题是第 13 页的 (3.9)：正文写成类似
\((\int|\Rm|)^{1/2}\)，但上下文、Theorem 3.1 和随后使用的
\(\|\Rm\|_2\) 表明应为

\[
\left(\int|\Rm|^2\right)^{1/2}.
\]

---

## 7. 全局与局地使用所需的几何输入

### 7.1 论文实际陈述的全局情形

Theorem 3.6 假设对同一个 \(r\)，每个 \(y\in M\) 都满足

\[
\frac{r^4}{V_0(B_r(y))}
\int_{B_r(y)}|\Rm(g_0)|^2\,d\mu_0
\le\varepsilon,
\qquad
|\Ric(g_0)|\le K.
\tag{7.1}
\]

论文的覆盖、曲率 \(L^2\) 延续、Sobolev 比较和度量等价均在“所有中心”条件下进行。其证明中真正供 Corollary 3.5 使用的动态信息为：

\[
\sup_{y,\;0\le s\le S}
A_y\|\Rm(\bar g(s))\|_{L^2(B_r(y),\bar g(s))}
\le\theta_0,
\tag{7.2}
\]

以及

\[
\frac12g_0\le\bar g(s)\le2g_0,
\tag{7.3}
\]

固定初始球上的 Sobolev 不等式、有限重数覆盖和截断梯度控制。论文第 13–15 页的 bootstrap 正是在构造这些信息。

第 14–15 页度量比较中写出的
\(\|\Ric\|_\infty T\) 应理解为时间积分。由
\(|\Ric(s)|\le Cs^{-2/3}\) 得到的是

\[
\int_0^S|\Ric(s)|\,ds\le 3CS^{1/3},
\]

而不是在含 \(s=0\) 的区间取 \(\|\Ric\|_\infty\)。

### 7.2 局地情形

若只在某个好点附近知道初始能量，则论文并未陈述“仅在一个球内产生 Ricci 流”的定理。对一个已经存在的光滑局地流，Corollary 3.5 的能量论证可用紧支撑截断完成；但统一存在时间、动态能量 (7.2) 和度量等价 (7.3) 仍需由额外的局地流构造提供。

一个充分的局地几何配置是：

- 开集 \(\Omega\) 包含 \(\overline{B_{10r}^{g_0}(p)}\)；
- \(\bar g(s)\) 在 \(\Omega\times[0,S]\) 光滑满足非归一化 Ricci 流；
- 对 \(y\in B_{6r}(p)\)，所有使用的 \(B_{2r}(y)\) 紧含于 \(\Omega\)；
- 每个固定初始球都有时间一致的 (1.1)，并有
  \[
  A_y\le C_Sr^2V_0(B_r(y))^{-1/2};
  \]
- \(B_{2r}(y)\) 可由至多 \(N\) 个 \(r\)-球覆盖，附近球的体积彼此可比；
- (7.2) 对所有这些中心成立；
- 截断函数固定于 \(g_0\)，支撑紧含于 \(\Omega\)，并满足
  \[
  |\nabla\chi|_{\bar g(s)}\le Cr^{-1};
  \]
- 初始 \(|E(0)|\le\delta\) 至少在所有 \(B_{3r}(x)\)、\(x\in B_r(p)\) 上成立。

紧支撑条件保证分部积分不会从区域外缘产生通量项。只知道中心 \(p\) 的初始能量，而没有上述动态信息，尚不能直接引用论文的全局 Corollary 3.5。

---

## 8. 好点确实给出局地“所有中心”初始小能量

设

\[
\mathcal M_1(|\Rm|^2)(p)\le K_0,
\]

即对 \(0<R\le1\)，

\[
\int_{B_R(p)}|\Rm|^2
\le K_0V(B_R(p)).
\tag{8.1}
\]

若 \(q\in B_{R/2}(p)\)、\(0<\rho\le R/2\)，则

\[
B_\rho(q)\subset B_R(p)
\subset B_{3R/2}(q).
\]

由 Bishop–Gromov 比较，

\[
\frac{V(B_R(p))}{V(B_\rho(q))}
\le
\frac{V(B_{3R/2}(q))}{V(B_\rho(q))}
\le C\left(\frac R\rho\right)^4.
\]

所以

\[
\frac{\rho^4}{V(B_\rho(q))}
\int_{B_\rho(q)}|\Rm|^2
\le CK_0R^4.
\tag{8.2}
\]

选择 \(R\) 使 \(CK_0R^4\le\varepsilon\)，便在 \(B_{R/2}(p)\) 内得到所有中心、所有较小尺度的初始小能量。Strategist 对这一初始尺度问题的修正是正确的。它仍需与上一节的局地流及动态能量结构配合。

---

## 9. 精确的条件性引理

**引理（局地 Corollary 3.5 版本）。**  
设 \(n=4\)、\(0<r\le1\)，且 \(\bar g(s)\) 是
\(\Omega\times[0,S]\) 上的光滑非归一化 Ricci 流。设
\(\overline{B_{10r}^{g_0}(p)}\subset\Omega\)，并假设第 7.2 节列出的度量等价、Sobolev、覆盖、紧支撑截断和动态曲率能量条件成立，且

\[
\sup_{B_{4r}(p)}|\Ric(g_0)+g_0|_{g_0}\le\delta.
\]

定义

\[
t=\frac12\log(1+2s),\qquad
g(t)=(1+2s)^{-1}\bar g(s).
\]

则存在 \(a,C>0\)，仅依赖于 Sobolev、覆盖、体积比较、度量等价常数及维数，使得对

\[
x\in B_r^{g_0}(p),\qquad
0<t\le a r^2
\]

有

\[
\boxed{
|\Ric(g(t))+g(t)|_{g(t)}
\le
C\delta\left(\frac{r^2}{t}\right)^{2/3}.
}
\tag{9.1}
\]

并且

\[
\boxed{
\left|
\log\frac{g(t)(v,v)}{g_0(v,v)}
\right|
\le
C\delta r^{4/3}t^{1/3}
}
\tag{9.2}
\]

对所有 \(x\in B_r(p)\) 与 \(v\in T_xM\setminus\{0\}\) 成立。

---

## 10. 对 Step 13 内球/外球 Gronwall 的评估

Step 13 写出的形式

\[
\frac d{dt}
\int_{B_{r/4}}|E|^2
\le
Cr^{-2}
\int_{B_{r/2}}|E|^2
\tag{10.1}
\]

不能直接推出

\[
\int_{B_{r/4}}|E(t)|^2
\le
e^{Ct/r^2}
\int_{B_{r/2}}|E(0)|^2,
\]

因为右端是另一个空间区域上的未知演化量。此外，归一化流下对
\(\int|E|^2d\mu\) 求导还会出现体积形式项。要闭合这类论证，需要嵌套截断、覆盖求和及所有相关中心的动态能量控制。

Corollary 3.5 已经完成了所需结构：先传播局地 \(L^3\) 范数，再用曲率的临界 \(L^3\) 时空估计作 Moser 迭代。由此得到的 (9.1) 和 (9.2) 不依赖 Step 13 的内球/外球 Gronwall。

**最终数学结论：**在 Ye Li 全局全中心假设下，或在局地流具备同样的动态 Sobolev、覆盖、度量等价与曲率能量结构时，

\[
|E(x,t)|\le C\delta(r^2/t)^{2/3},
\qquad
\text{metric drift}\le C\delta r^{4/3}t^{1/3}
\]

均可严格推出，常数与塌缩体积无关。单个好点足以产生局地所有中心的初始小能量，但从该初始信息构造具有统一时间和上述动态结构的局地 Ricci 流，未由所给 Ye Li 定理直接提供。