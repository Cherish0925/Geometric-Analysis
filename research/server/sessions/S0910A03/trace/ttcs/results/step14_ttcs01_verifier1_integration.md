# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 14,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step14_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step14_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Read Ye Li's actual paper and the Step 13 smoothing note in light of the Strategist correction. Reconstruct rigorously the source-based estimate for the normalized Einstein defect E=Ric+g under normalized Ricci flow, focusing on Corollary 3.5. Determine the correct scaling, Sobolev constant A and volume cancellation, the subsolution inequality for u=(|E|^2+eta)^{1/2}, normalized-vs-unnormalized flow conversion, and exactly which global/local all-centers, evolving curvature-energy, cutoff, metric-equivalence, and boundary hypotheses are needed. Explicitly identify any source typographical ambiguity such as the cutoff phi^2 in Cor. 3.5. Assess whether one can obtain |E(x,t)| <= C delta (r^2/t)^(2/3) uniformly on an interior ball and metric drift O(delta r^(4/3)t^(1/3)); do not assume the flawed Step 13 inner/outer Gronwall. Give a direct mathematical memo with derivations and a precise conditional lemma.

## Integrated Scientific Memo

# 科学核验备忘录：由 Ye Li Corollary 3.5 传播归一化 Einstein 缺陷

## 1. 结论

在 Ye Li 论文的**全局、全中心**假设下，或在一个带缓冲的局部流上另行假设 Li 证明所需的全部动态分析输入时，可以严格推出四维归一化 Ricci 流
\[
\partial_tg=-2(\Ric_g+g)
\]
的 Einstein 缺陷
\[
E=\Ric_g+g
\]
满足内部估计
\[
\boxed{\;
|E(x,t)|_{g(t)}
\le C\delta \left(\frac{r^2}{t}\right)^{2/3},
\qquad 0<t\le a r^2,
\;}
\]
前提是初始缓冲球上 \(|E(0)|\le\delta\)。相应地，
\[
\boxed{\;
\left|\log\frac{g(t)(v,v)}{g_0(v,v)}\right|
\le C\delta r^{4/3}t^{1/3}.
\;}
\]
当右端不超过常数时，这给出
\[
|g(t)-g_0|_{g_0}\le C\delta r^{4/3}t^{1/3}.
\]

正确证明是直接使用 Corollary 3.5，而不是 Step 13 中有缺口的“内球/外球 \(L^2\)-Gronwall”。但 Ye Li 的定理本身是完整流形上的全局定理；单个好点虽能产生一个缓冲区域内的**初始全中心小能量**，却不能仅凭论文现成结论产生塌缩情形下的局部 Ricci 流。局部流构造及其动态能量控制是准确的剩余缺口。

---

## 2. Corollary 3.5 的正确内容及排印问题

Li 在固定的 \(g(0)\)-球上使用四维 Dirichlet–Sobolev 不等式
\[
\left(\int_{B_r(y)}v^4\,d\mu_s\right)^{1/2}
\le A_y\int_{B_r(y)}|\nabla v|^2\,d\mu_s,
\qquad v\in C^\infty_0(B_r(y)).
\tag{2.1}
\]
这里 \(A_y\) 在四维无量纲，并且在有 Ricci 下界、\(r\le1\) 时
\[
A_y\le C_S\left(\frac{r^4}{V_0(B_r(y))}\right)^{1/2}
=C_S\frac{r^2}{V_0(B_r(y))^{1/2}}.
\tag{2.2}
\]

论文 Corollary 3.5 写成
\[
\partial_tu\le \phi^2(\Delta u+c_0fu).
\tag{2.3}
\]
这应视为排印或从局部 Ricci 流论证遗留的符号，而不是可按字面使用的命题：

1. 推论陈述中没有定义该 \(\phi\)；
2. Theorem 2.5 要求的是普通次解不等式；
3. Li 随后把推论用于普通 Ricci 流的 \(\Ric\)，其方程没有 \(\phi^2\Delta\)；
4. 第 13 页同样错误地出现
   \[
   \partial_t|\Rm|^2=\phi^2\Delta|\Rm|^2-\cdots,
   \]
   而普通 Ricci 流中 Laplacian 前没有 \(\phi^2\)。

与证明和应用一致的版本是
\[
\boxed{\;\partial_tu\le\Delta u+c_0fu.\;}
\tag{2.4}
\]
若真要处理 \(\phi^2\Delta u\)，主部会退化且分部积分产生额外 \(\nabla\phi\) 项，论文的证明并未提供这种版本。

另一个明显排印问题是 (3.9) 中类似
\[
\left(\int |\Rm|\right)^{1/2};
\]
结合 Theorem 3.1 及后文 \(\|\Rm\|_2\) 的使用，应为
\[
\left(\int |\Rm|^2\right)^{1/2}.
\]

---

## 3. Corollary 3.5 的源内机制与尺度

令 \(f\ge0\) 满足 Theorem 3.4 的条件
\[
(\partial_s-\Delta)f\le C_0f^2,\qquad
\partial_s d\mu_s\le cf\,d\mu_s.
\tag{3.1}
\]
真正需要维持的动态小量是
\[
A_y\|f(s)\|_{L^2(B_r(y),g(s))}\le\theta_0
\tag{3.2}
\]
对所有相关中心和时间成立。Li 由初始全中心小能量、覆盖及 bootstrap 得到它，并推出
\[
\int_{B_r(y)}f^3(s)\,d\mu_s
\le C N A_y e_y^3\,s^{-1},
\quad
e_y=\sup_{\sigma\le s}\|f(\sigma)\|_{L^2(B_r(y),g(\sigma))}.
\tag{3.3}
\]
在 Theorem 2.5 的记号中
\[
\mu_y^3=CNA_ye_y^3,\qquad
A_y^2\mu_y^3=CN(A_ye_y)^3,
\tag{3.4}
\]
故 Moser 常数由 (3.2) 控制，不依赖塌缩体积。

若 \(u\) 满足 (2.4)，取固定于 \(g_0\) 的截断 \(\chi\)，则
\[
\begin{aligned}
\frac d{ds}\int\chi^2u^3\,d\mu_s
+c\int|\nabla(\chi u^{3/2})|^2\,d\mu_s
\le{}&
Cr^{-2}\int_{\supp\chi}u^3\,d\mu_s\\
&+C\int f\,\chi^2u^3\,d\mu_s .
\end{aligned}
\tag{3.5}
\]
反应项由
\[
\int f(\chi u^{3/2})^2
\le \|f\|_2\|\chi u^{3/2}\|_4^2
\le A_y\|f\|_2
\int|\nabla(\chi u^{3/2})|^2
\tag{3.6}
\]
吸收。论文第 13 页的 \(C_3\int u^3\) 在恢复尺度后正是 \(Cr^{-2}\int u^3\)。

覆盖和嵌套截断于是给出
\[
\sup_{0\le \sigma\le s}\int_{B_r(x)}u^3(\sigma)\,d\mu_\sigma
\le C\int_{B_{3r}(x)}u_0^3\,d\mu_0,
\qquad s\le cr^2.
\tag{3.7}
\]
将 Theorem 2.5 取 \(p_0=3\)，令其中终止时间趋于当前时间，得到
\[
\boxed{\;
u(x,s)\le
C A_x^{2/3}s^{-2/3}
\left(\int_{B_{3r}(x)}u_0^3\,d\mu_0\right)^{1/3},
\quad 0<s\le cr^2.
\;}
\tag{3.8}
\]
其中 \(s^{-2/3}\) 来自 Moser 中 \(s^{-1}\) 与时空积分长度 \(s\) 的组合，而不是点态 \(C/s\) Gronwall。

---

## 4. Einstein 缺陷的次解不等式

对归一化流
\[
\partial_tg=-2E,\qquad E=\Ric+g,
\]
精确演化为
\[
\partial_tE=\Delta_LE-2E
\]
以及
\[
(\partial_t-\Delta)|E|^2
=-2|\nabla E|^2+4R_{ikjl}E_{ij}E_{kl}.
\tag{4.1}
\]
张量方程中的显式 \(-2E\) 不会在标量方程中留下线性阻尼；它与逆度量变化及 \(\Delta_L\) 中的 Ricci 收缩项抵消。

令
\[
u_\eta=(|E|^2+\eta)^{1/2}.
\]
写 \(F=|E|^2\)，则
\[
(\partial_t-\Delta)u_\eta
=\frac{(\partial_t-\Delta)F}{2u_\eta}
+\frac{|\nabla F|^2}{4u_\eta^3}.
\]
由
\[
|\nabla F|^2\le4F|\nabla E|^2
\]
可得梯度部分
\[
-\frac{|\nabla E|^2}{u_\eta}
+\frac{F|\nabla E|^2}{u_\eta^3}
=-\frac{\eta|\nabla E|^2}{u_\eta^3}\le0.
\]
因此
\[
\boxed{\;
(\partial_t-\Delta)u_\eta
\le2|\Rm|u_\eta.
\;}
\tag{4.2}
\]
令 \(\eta\downarrow0\)，\(|E|\) 在 barrier/弱意义下满足同一不等式。

为了严格对接 Li 的非归一化流，最好作下面的精确转换，而不是直接宣称归一化流满足其全部 bootstrap 假设。

---

## 5. 归一化与非归一化流转换

设
\[
\partial_s\bar g=-2\Ric_{\bar g},\qquad \bar g(0)=g_0,
\]
并定义
\[
s=\frac{e^{2t}-1}{2},\qquad
g(t)=e^{-2t}\bar g(s)=\frac{\bar g(s)}{1+2s}.
\tag{5.1}
\]
则 \(g(t)\) 满足归一化流。

令
\[
q(s)=\frac1{1+2s},\qquad
H(s)=\Ric_{\bar g}+q(s)\bar g.
\tag{5.2}
\]
作为协变二阶张量，
\[
H(s)=E(t),
\]
但范数满足
\[
|E(t)|_{g(t)}
=(1+2s)|H(s)|_{\bar g(s)}=e^{2t}|H(s)|_{\bar g(s)}.
\tag{5.3}
\]
由于 \(q'=-2q^2\) 且 \(\Delta_L\bar g=0\)，
\[
\partial_sH=\Delta_LH-2qH.
\]
相应地
\[
(\partial_s-\Delta_{\bar g})|H|^2
=-2|\nabla H|^2
+4\bar R_{ikjl}H_{ij}H_{kl}
-4q|H|^2.
\tag{5.4}
\]
最后一项有利，故
\[
(\partial_s-\Delta_{\bar g})(|H|^2+\eta)^{1/2}
\le2|\Rm(\bar g)|(|H|^2+\eta)^{1/2}.
\tag{5.5}
\]
这允许将 Corollary 3.5 严格应用于
\[
f=|\Rm(\bar g)|,\qquad u=|H|.
\]

对 \(t\le ar^2\le a\)，有 \(s\asymp t\)、\(e^{2t}\le C\)。四维 Dirichlet–Sobolev 系数和 \(\int|\Rm|^2d\mu\) 在常数缩放下均不变，所以转换不破坏临界结构。

---

## 6. 两次体积消去

定义
\[
\varepsilon_y(r)
=\frac{r^4}{V_0(B_r(y))}
\int_{B_r(y)}|\Rm(g_0)|^2\,d\mu_0.
\]
由 (2.2)，
\[
A_y\|\Rm(g_0)\|_{L^2(B_r(y))}
\le
C\frac{r^2}{V_y^{1/2}}
\left(\frac{\varepsilon_yV_y}{r^4}\right)^{1/2}
=C\varepsilon_y^{1/2}.
\tag{6.1}
\]
这是 Li 小能量吸收中的第一次体积消去。

若
\[
|E(0)|\le\delta\quad\text{于 }B_{3r}(x),
\]
则
\[
\begin{aligned}
A_x^{2/3}
\left(\int_{B_{3r}(x)}|E(0)|^3\,d\mu_0\right)^{1/3}
&\le
C\frac{r^{4/3}}{V_0(B_r(x))^{1/3}}
\delta V_0(B_{3r}(x))^{1/3}\\
&\le C\delta r^{4/3}.
\end{aligned}
\tag{6.2}
\]
最后一步使用 Ricci 下界给出的相邻尺度体积比
\[
\frac{V_0(B_{3r}(x))}{V_0(B_r(x))}\le D(n,Kr^2).
\]
这不要求非塌缩。代入 (3.8)，并使用 \(s\asymp t\)、(5.3)，得到
\[
\boxed{\;
|E(x,t)|_{g(t)}
\le C\delta r^{4/3}t^{-2/3}
=C\delta\left(\frac{r^2}{t}\right)^{2/3}.
\;}
\tag{6.3}
\]

---

## 7. 度量漂移

对固定非零切向量 \(v\)，
\[
\left|\partial_t\log g(t)(v,v)\right|
=2\left|\frac{E(v,v)}{g(v,v)}\right|
\le2|E|_{g(t)}.
\]
因此
\[
\begin{aligned}
\left|\log\frac{g(t)(v,v)}{g_0(v,v)}\right|
&\le2\int_0^t|E(x,\tau)|\,d\tau\\
&\le C\delta r^{4/3}\int_0^t\tau^{-2/3}\,d\tau\\
&=C\delta r^{4/3}t^{1/3}.
\end{aligned}
\tag{7.1}
\]
无须另假设初始短时间内 \(|E|\le2\delta\)；(6.3) 的奇性可积。于是
\[
e^{-D(t)}g_0\le g(t)\le e^{D(t)}g_0,\qquad
D(t)=C\delta r^{4/3}t^{1/3}.
\tag{7.2}
\]
这是归一化流的漂移。非归一化流还含 Einstein 背景的整体缩放，不能直接称为 \(O(\delta)\) 漂移。

---

## 8. 精确条件性引理

**条件性局部缺陷传播引理。**  
设 \(n=4\)、\(0<r\le1\)，\(\bar g(s)\) 是开集 \(\Omega\) 上的光滑非归一化 Ricci 流，且
\[
\overline{B^{g_0}_{10r}(p)}\subset\Omega.
\]
假设在 \(0\le s\le ar^2\)：

1. **动态度量等价**
   \[
   \Lambda^{-1}g_0\le\bar g(s)\le\Lambda g_0.
   \]

2. **所有相关中心的 Sobolev 控制**：对 \(y\in B_{6r}^{g_0}(p)\)，所有所用固定初始球及 \(v\in C^\infty_0(B_r(y))\)，
   \[
   \|v\|_4^2\le A_y\|\nabla v\|_2^2,\qquad
   A_y\le C_S\frac{r^2}{V_0(B_r(y))^{1/2}}.
   \]

3. **覆盖和体积控制**：相关 \(2r\)-球可由至多 \(N\) 个 \(r\)-球覆盖，相邻球体积可比，且
   \[
   V_0(B_{3r}(x))/V_0(B_r(x))\le D.
   \]

4. **动态临界曲率小量**
   \[
   \sup_{\substack{y\in B_{6r}(p)\\0\le s\le ar^2}}
   A_y\|\Rm(\bar g(s))\|_{L^2(B_r(y),\bar g(s))}
   \le\theta_0,
   \]
   其中 \(\theta_0\) 小到足以完成 (3.6) 的吸收；并且 Li 的覆盖论证所给
   \[
   \int_{B_r(y)}|\Rm|^3\,d\mu_s\le \mu_y^3s^{-1},
   \qquad A_y^2\mu_y^3\le C.
   \]

5. **截断和边界条件**：所有截断固定于 \(g_0\)，紧支撑于 \(\Omega\)，等于 \(1\) 于目标内球，并满足
   \[
   |\nabla\chi|_{\bar g(s)}\le Cr^{-1}.
   \]
   因紧支撑，分部积分无外边界通量。

6. **初始缺陷**
   \[
   \sup_{B_{4r}(p)}|\Ric(g_0)+g_0|_{g_0}\le\delta.
   \]

定义
\[
t=\frac12\log(1+2s),\qquad g(t)=(1+2s)^{-1}\bar g(s).
\]
则存在 \(a,C>0\)，仅依赖于维数及 \(\Lambda,C_S,N,D,\theta_0\) 等上述结构常数，使得
\[
|\,\Ric(g(t))+g(t)\,|_{g(t)}
\le C\delta\left(\frac{r^2}{t}\right)^{2/3}
\]
对 \(x\in B_r^{g_0}(p)\)、\(0<t\le ar^2\) 成立，并且
\[
\left|\log\frac{g(t)(v,v)}{g_0(v,v)}\right|
\le C\delta r^{4/3}t^{1/3}.
\]

在 Li 的完整全局情形中，这些动态条件由 Theorem 3.1/3.4 的 maximal bootstrap 提供；它们不能由单独的点态 \(|\Rm|\le C/t\) 推出。

---

## 9. 全局、局部与好点的准确区分

Li 的 Theorem 3.1/3.6 假设对完整流形上的**每个中心** \(y\)
\[
\frac{r^4}{V_0(B_r(y))}
\int_{B_r(y)}|\Rm(g_0)|^2\le\varepsilon_{\rm Li},
\qquad |\Ric(g_0)|\le K.
\tag{9.1}
\]
其短时存在、曲率能量持续性、Sobolev 持续性和度量等价均依赖这一全中心 bootstrap。

Strategist 的尺度修正本身是正确的。若
\[
\mathcal M_1(|\Rm|^2)(p)\le K_0,
\]
则对 \(q\in B_{R/2}(p)\)、\(0<\rho\le R/2\)，
\[
B_\rho(q)\subset B_R(p)\subset B_{3R/2}(q).
\]
Bishop–Gromov 给出
\[
\begin{aligned}
\frac{\rho^4}{V(B_\rho(q))}
\int_{B_\rho(q)}|\Rm|^2
&\le
K_0\rho^4\frac{V(B_R(p))}{V(B_\rho(q))}\\
&\le CK_0R^4.
\end{aligned}
\tag{9.2}
\]
选 \(R\) 使 \(CK_0R^4\le\varepsilon_{\rm Li}\)，便在 \(B_{R/2}(p)\) 内获得所有中心、所有较小尺度的**初始**小能量。背景曲率非零并不妨碍这一缩尺。

但论文没有由此推出“只在该球内存在”的局部 smoothing 定理。要局部化，必须另行构造带缓冲区域的流，并证明：

- 边界不会污染目标内球；
- 所有相关中心的动态 \(L^2\) 曲率小量持续；
- Sobolev、覆盖、cutoff 和度量等价持续；
- Li 所用的 \(L^3\) 曲率估计仍成立。

在塌缩情形下，这不是论文已经证明的形式结果。仅说“覆盖只涉及附近球，因此局部化应当成立”还不足以解决流的边界存在性。

---

## 10. Step 13 内球/外球 Gronwall 为何不能使用

Step 13 的示意不等式
\[
\frac d{dt}\int_{B_{r/4}}|E|^2
\le Cr^{-2}\int_{B_{r/2}}|E|^2
\tag{10.1}
\]
不能直接推出
\[
\int_{B_{r/4}}|E(t)|^2
\le e^{Ct/r^2}\int_{B_{r/2}}|E(0)|^2.
\]
原因是右端含另一个、更大区域上的未知演化量，并不是待估函数自身；此外归一化流下对 \(\int|E|^2d\mu\) 求导还有体积项
\[
\partial_td\mu=-\tr E\,d\mu.
\]
要闭合必须进行嵌套截断、覆盖求和和所有中心的动态能量控制。Corollary 3.5 正是通过传播局部 \(L^3\) 范数并作 Moser 迭代完成这些步骤，因此应直接采用它。

同样，点态
\[
|\Rm(t)|\le C/t
\]
只给
\[
D^+\sup|E|^2\le\frac{C}{t}\sup|E|^2,
\]
其 Gronwall 因子从 \(0\) 积分发散。标量演化中不存在可挽救这一发散的普适 \(-2E\) 阻尼。

---

## 11. 最终核验判断

1. **估计本身成立**：在 Li 的全局全中心框架下，或满足上述完整局部动态条件时，
   \[
   |E(x,t)|\le C\delta(r^2/t)^{2/3}
   \]
   与
   \[
   \operatorname{drift}(g(t),g_0)
   \le C\delta r^{4/3}t^{1/3}
   \]
   均由 Corollary 3.5 严格推出，且常数与塌缩体积无关。

2. **正确的 Sobolev 系数为**
   \[
   A\lesssim r^2V(B_r)^{-1/2},
   \]
   因而 \(A^{2/3}\) 恰与初始 \(L^3\) 数据中的 \(V^{1/3}\) 消去。

3. **\(\phi^2\) 是源文歧义/排印错误**；可核验的推论要求普通次解
   \[
   (\partial_t-\Delta)u\le c_0fu.
   \]

4. **单个好点足以给出缓冲区域内的初始全中心小能量**，但不足以直接调用 Li 的完整流形定理来构造局部流。

5. **准确未决对象**是塌缩情形下的局部 smoothing：在带边界缓冲域上建立统一 \(O(r^2)\) 存在时间、内部 \(C/t\) 曲率界以及 Li 所需动态能量/Sobolev/cutoff 结构。缺少该构造时，不能把上述条件性局部引理宣称为 Ye Li 论文已证明的局部定理。