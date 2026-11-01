# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 36,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step36_ttcs02_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step36_ttcs02_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Review A03 Step 37's three analytic-interface notes as possible proofs for the restricted four-dimensional negative cutoff-flow route, using A01's Step 36 platform note and verifier as comparison. Focus especially on the shifted-U base-pair continuation note. Check: (1) transported-DeTurck existence: does the note correctly adapt Yang's Theorem 8.2 to the normalized term, and is any claimed chi^2 weight for delta(hat a) too strong or harmless? (2) global Q persistence: are the weights, buffered K2 use, Gronwall coefficient, and independence from J6 correct? (3) base-pair continuation: does the written proof actually implement the second integration by parts for I_{1c}/I_3 that the script/message claim, or does it still rely on an invalid direct Holder bound such as ∫ chi |Theta| |W|^p <= ||Theta||_p ||W||_p^p? Are unweighted L^p(T), Sobolev upgrades, and G terms sufficiently justified, or still hidden hypotheses? Give a direct mathematical memo identifying what can be accepted now and what exact calculation remains.

## Integrated Scientific Memo

# 数学核验备忘录

## 结论概览

三项接口的当前状态是：

1. **transported-DeTurck 短时存在性：可接受，但须更正 \(\delta\widehat a\) 的权重表述。**
2. **全局 \(Q\) 延续：机制正确；须补上遗漏的 \(\nabla a\) 项、明确 buffered \(K_2\) 的使用，并默认采用 \(C(1+r^{-2})\) 的 Grönwall 系数。**
3. **shifted-\(U\) base pair：当前正文确实实施了所需的第二次分部积分，不再依赖错误的直接 Hölder；但它仅给出有条件的有限 \(L^p\) 基础估计，尚不是 continuation theorem。**

---

## 1. Transported-DeTurck 存在性

### 可接受部分

A03 的系统
\[
\partial_t\widehat g
=-2\Big[\widehat a(\operatorname{Ric}_{\widehat g}+\widehat g)
-\widehat\delta^*(\widehat a\,S^{-1}\delta G(S))\Big],
\qquad
\widehat a=a\circ\varphi_t^{-1},
\]
连同 Yang 的同一微分同胚方程，是其 Theorem 8.2 的正确 normalized 改写。

这里 gauge 系数必须置于 \(\widehat\delta^*\) 内；等价地，它产生
\[
\mathcal L_{\widehat aW}\widehat g
=\widehat a\mathcal L_W\widehat g
+d\widehat a\otimes W^\flat+W^\flat\otimes d\widehat a.
\]
故旧的 fixed-coefficient \(\widehat a\mathcal L_W\widehat g\) 确实不够。

令 \(g=\varphi_t^*\widehat g\)，则 Yang 的 Lie derivative cancellation 原样成立，并且
\[
\varphi_t^*\widehat a=a,\qquad
\varphi_t^*\operatorname{Ric}_{\widehat g}=\operatorname{Ric}_g.
\]
因此
\[
\partial_tg=-2a(\operatorname{Ric}_g+g).
\]

### 必须修正的 \(\delta\widehat a\)

A03 所称
\[
\delta\widehat a=\chi^2(\text{一阶作用于 }\psi)
\]
一般不成立。若
\[
Y=\delta\varphi\circ\varphi^{-1},
\]
则精确公式是
\[
\boxed{\delta\widehat a=-d\widehat a(Y)
=-2\widehat\chi\,d\widehat\chi(Y).}
\]
通常只有一个 \(\widehat\chi\) 因子，不能写成 \(\widehat a\) 乘有界光滑系数。

但这个过强权重主张是**无害的**：新增 normalization 的线性化为
\[
\delta(-2\widehat a\,\widehat g)
=-2\widehat a\,h+2d\widehat a(Y)\widehat g.
\]
它对 \(h,Y\) 都是零阶项，满足逐阶 Sobolev 估计
\[
\|\delta(-2\widehat a\widehat g)\|_{H^m}
\le C_m\big(\|h\|_{H^m}+\|Y\|_{H^m}\big),
\]
故分别进入 Yang 线性系统的 \(Dh\) 与 \(E\psi\) 槽，不改变
\(2\chi^2\Delta h\) 的主符号或三角 transport 结构。

A03 写出的 transport equation 也应改为
\[
\partial_t\widehat a+\mathcal L_{V_t}\widehat a=0,
\qquad
V_t=\partial_t\varphi_t\circ\varphi_t^{-1}.
\]

### 核验结论

依赖 Yang 已陈述的 tame energy estimates，并使用上述标准零阶扰动估计，**每个固定光滑 datum 的 normalized fixed-cutoff 短时光滑存在性可以接受**。普通退化 Schauder 理论不能替代 Yang 的一致 tame estimates。

Approach 2 的附注不宜作为证明依据：空间变化的 \(-2(\varepsilon^2+a)g\) 在曲率方程中还会产生 \(\nabla^2a\) 型项，不只是代数反应项；但这些仍是 datum-dependent 的低阶项，且主证明使用的是 Approach 1，故不影响结论。

---

## 2. 全局无权 defect 能量 \(Q\)

设
\[
Q=\int_M|E|^2\,d\mu,\qquad
X=\int_Ma|\nabla E|^2\,d\mu.
\]

### 演化结构

“方程对 \(E\) 齐次、无 curvature-only source”是正确的。不过 A03 的 (2.1) 不是完整的 schematic identity；还应包含梯度 cutoff 项：
\[
\begin{aligned}
(\partial_t-a\Delta)|E|^2
={}&-2a|\nabla E|^2
+\nabla a*E*\nabla E
+\nabla^2a*E*E\\
&+a\,\operatorname{Rm}*E*E
+a\,E*E*E+a\,E*E .
\end{aligned}
\]
遗漏项可由
\[
\int|\nabla a||E||\nabla E|
\le \varepsilon X+
C_\varepsilon\int\frac{|\nabla a|^2}{a}|E|^2
\]
处理。对于 \(a=\chi^2\)，在 \(\{\chi\neq0\}\)
\[
\frac{|\nabla a|^2}{a}=4|\nabla\chi|^2,
\]
并以零连续延拓至零集。Hessian-\(a\) 项使用已核验的
\[
|B_{\rm def}|\le C|E|^2,\qquad
|\nabla B_{\rm def}|\le C|E||\nabla E|
\]
做一次 signed integration by parts，得到相同的
\[
\varepsilon X+Cr^{-2}Q.
\]

### Buffered \(K_2\) 的正确用法

A03 写成
\[
\|F\|_{L^2(U_j)}\le K_{2,j}^{1/2}
\]
仅在 \(\eta_j\equiv1\) 于整个 \(U_j\) 时成立。正确写法是
\[
\begin{aligned}
\int F(\chi_jE)^2
&=\int_{\operatorname{supp}\chi_j}F(\chi_jE)^2\\
&\le
\left(\int_{U_j}\eta_j^2F^2\right)^{1/2}
\|\chi_jE\|_4^2,
\end{aligned}
\]
其中
\[
\eta_j\equiv1\quad\text{于 }\operatorname{supp}\chi_j.
\]
随后四维局部 Sobolev 给出
\[
\|\chi_jE\|_4^2
\le C\mathcal S_j
\left(
\int_{U_j}a|\nabla E|^2+
r^{-2}\int_{U_j}|E|^2
\right),
\]
从而
\[
I_{1,j}\le C\gamma_j(X_j+r^{-2}Q_j),
\qquad
\gamma_j=\mathcal S_jK_{2,j}^{1/2}.
\]
支集互不相交时可直接求和，并在 \(\gamma_*=\max_j\gamma_j\) 足够小时吸收 \(X\)。

### Grönwall 系数

由 A03 当前直接写出的估计，稳妥结论是 A01 的
\[
\boxed{Q'\le C(1+r^{-2})Q,}
\]
故
\[
\boxed{
Q(t)\le e^{C(1+r^{-2})t}Q(0)
\le e^{C\theta(1+r^2)}Q(0),
\qquad t\le\theta r^2.
}
\]

较短的 \(Cr^{-2}\) 系数在以下任一补充下成立：

- 明确假设 \(r\le1\)；或
- 利用 \(|E|\le CF\)，把 measure cubic 与所有 \(O(1)\) 活跃区反应项都并入
  \(\int aF|E|^2\)，再由小 \(\gamma_*\) 处理。

A03 没有明确执行这一步，因此不应无条件直接写成 \(Cr^{-2}\)。

### 与 \(J_6\) 的独立性

这一点完全正确。靠近 \(a=0\)，加权量
\[
J_6=\int\eta^2a^4|E|^6,\qquad \|aE\|_\infty
\]
不能控制 \(\int|E|^2\)。故供终端 calibration 使用的 \(Q\) 必须独立传播，其证明不依赖 \(J_6\)。

### 核验结论

在 first-exit 的 moving Sobolev、buffered \(K_2\)、metric comparability 和小 \(\gamma_*\) 假设下，**全局 \(Q\) persistence 可接受**，但正文应作上述三项修正。

---

## 3. Shifted-\(U\) base pair

令
\[
U=aT,\qquad W=\nabla U,\qquad \Theta=\nabla^2\chi.
\]

### 第二次分部积分确实已写入正文

当前正文的 \(I_{1c}\) 与 \(I_3\) 均保留了 signed contraction：
\[
J=\int_M\chi\,\nabla_i\nabla_j\chi\,B^{ij}(W)\,d\mu,
\]
其中
\[
|B(W)|\le C_p|W|^p,\qquad
|\nabla B(W)|\le C_p|W|^{p-1}|\nabla W|.
\]
在闭流形上精确地有
\[
\boxed{
J=-\int\nabla_i\chi\,\nabla_j\chi\,B^{ij}(W)
-\int\chi\,\nabla_j\chi\,\nabla_iB^{ij}(W).
}
\]
因此
\[
\begin{aligned}
|J|
&\le C_p\|d\chi\|_\infty^2\int|W|^p\\
&\quad+C_p\int\chi|d\chi||W|^{p-1}|\nabla W|\\
&\le
\varepsilon\int a|\nabla W|^2|W|^{p-2}
+C_{p,\varepsilon}\|d\chi\|_\infty^2\int|W|^p.
\end{aligned}
\]
这正是 (3.9)、(3.11) 所需的计算。

所以当前正文**不再依赖**错误不等式
\[
\int\chi|\Theta||W|^p
\lesssim\|\Theta\|_p\|W\|_p^p.
\]
该直接 Hölder 实际需要
\[
W\in L^{p^2/(p-1)},
\]
而不仅是 \(L^p\)。

脚本注释中“total power \(p+1\)”是错误的；实际 \(B(W)\) 的总次数是 \(p\)。文件开头称 (3.9)、(3.11) 仍有旧错误的 supersession banner 也已与当前正文不一致，应删除或改写。

### 其余 base-level 估计

以下配重是正确的：

- \(I_{1a}\) 利用 \(\chi=\sqrt a\)：
  \[
  |I_{1a}|
  \le\varepsilon\int a|\nabla W|^2|W|^{p-2}
  +CK^2\|\Theta\|_p^2\|W\|_p^{p-2}.
  \]
- \(I_{1b}\)、\(I_2\) 合法使用
  \[
  \int|\Theta||W|^{p-1}
  \le\|\Theta\|_p\|W\|_p^{p-1}.
  \]
- \(I_4=\chi\,d\chi*\nabla W\) 可吸收到加权 diffusion。
- 由
  \[
  \partial_t\nabla^2\chi
  =g^{-1}*\nabla\operatorname{Ric}(U)*d\chi
  \]
  可得
  \[
  \partial_t|\Theta|
  \le CK|\Theta|+C|W||d\chi|.
  \]

因此，**若**精确的 \(W\)-方程确实只有文中列出的项，且已有一致的 unweighted \(\|T\|_p\)，则
\[
Y_1=\|W\|_p^p+\|\Theta\|_p^p
\]
满足
\[
Y_1'\le C_p(1+Y_1+\|T\|_p^p),
\]
从而得到每个有限 \(p\) 的一致 base-pair \(L^p\) 界。

### 仍是隐藏输入的对象

#### 1. Unweighted \(L^p(T)\)

\[
\sup|U|=\sup|aT|\le K
\]
本身不能控制 \(a\ll1\) 区域的 unweighted \(T\)。固定 \(t<T_{\max}\) 的光滑性只给每个时刻有限，不给 \(t\uparrow T_{\max}\) 的一致界。

因此需要独立证明 normalized shifted 版本的
\[
\boxed{
\frac d{dt}\int_M|T|^p
\le C_{p,K,\chi}\left(1+\int_M|T|^p\right),
}
\]
其中 Hessian-cutoff 项必须做 signed IBP。Wang 的 Lemma 4.10 给出 unnormalized \(\mathrm{Rm}\) 的类似机制，但 A03 Step 37 未写出 \(T=\mathrm{Rm}+G\) 的 normalized 推导。

#### 2. 精确的 \(U/W\) 方程及 \(G\) 项

仍须从 tensor-level normalized shifted equation 导出
\[
\begin{aligned}
(\partial_t-a\Delta)W
={}&\chi\nabla^3\chi*U
+d\chi*\Theta*U+\chi\Theta*W\\
&+\chi d\chi*\nabla W
+U*W+G*W+\mathcal R,
\end{aligned}
\]
并验证
\[
|\mathcal R|\le C_K(1+|T|+|W|),
\]
尤其不能残留 unweighted \(T*W\) 作为 Grönwall 系数，也不能残留 unweighted \(\nabla T\)。

\(G=(g\owedge g)/(2(n-1))\) 本身满足 \(\nabla G=0\)、\(|G|\le C_n\)，其纯代数项无问题；未核验的是完整演化展开后所有 normalized/G 交叉项确实落入上述可控类别。

#### 3. Sobolev 升级与 continuation

有限
\[
\|\nabla U\|_{L^p},\qquad \|\nabla^2\chi\|_{L^p}
\]
不推出 \(L^\infty\)。当前 diffusion 只控制
\[
\int a|\nabla W|^2|W|^{p-2},
\]
不是 unweighted \(W^{1,p}\) 范数。必须完成更高阶 staggered induction，获得下一层无权空间导数，之后才能用 Sobolev embedding 得到点态导数界和光滑终端极限。

---

## 最终可采纳范围

### 现在可采纳

- normalized transported-DeTurck 的正确系统、pullback identity，以及依赖 Yang tame estimates 的 per-datum 短时存在性；
- 在 first-exit 几何假设下独立于 \(J_6\) 的全局 \(Q\) 传播，建议采用
  \[
  Q'\le C(1+r^{-2})Q;
  \]
- \(I_{1c}/I_3\) 的第二次 signed IBP，以及由此得到的**有条件有限-\(L^p\) base-pair lemma**。

### 尚未完成的精确计算

1. normalized shifted \(T=\mathrm{Rm}+G\) 的 unweighted \(L^p\) 能量不等式；
2. 完整 index-level \(U\) 与 \(W=\nabla U\) 演化，核清所有 \(G\)、connection 和 normalization 项；
3. \(m\ge2\) 的 shifted-curvature/cutoff-jet 联立归纳；
4. 获得下一层无权导数后实施 \(W^{1,p}\to L^\infty\)；
5. 由全部点态导数界构造 \(t\uparrow T_{\max}\) 的光滑极限，再用已核验的短时存在性重启。

因此，**Step 37 已修复 base-pair 中最关键的错误 Hölder，但 restricted negative cutoff-flow route 的 continuation interface 仍未闭合。**