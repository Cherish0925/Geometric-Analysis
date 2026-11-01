# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 65,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step65_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step65_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Analyze the compact torsion-zero surface problem using the established Step-62 cone, Step-63 degree formula, and the proposed higher-order leading normal form. The goal is to derive, if possible, an intrinsic normal-expansion equation along a smooth J-complex surface C contained in {T=0}: identify the rank-two normal coefficient corresponding to W_3^+|_C, how the exact AAD/soldered equations constrain its tangential covariant derivative including normal connection and second fundamental form, and whether they imply a similarity-principle relation or allow negative winding. Do not assume holomorphicity. Distinguish what follows from the supplied equations from a proposed route; correct the false inference that zero linear term controls winding.

## Integrated Scientific Memo

## 科学核验备忘录

### 1. 秩二点的法向首项及其与 \(W_3^+\) 的关系

在 AAD 局部规范中写
\[
\nabla\Omega=a\otimes\phi-Ja\otimes J\phi,\qquad
\nabla\phi=-a\otimes\Omega+b\otimes J\phi .
\]
于是 \(\{T=0\}=\{a=0\}\)。设 \(C\subset\{a=0\}\) 是光滑 \(J\)-复曲面。沿 \(C\) 对任意 \(X\in TC\) 有
\[
\nabla_Xa=0.
\]

在 \(p\in C\) 的秩二点，Step-62 的锥关系和 \(\ker DT(p)=T_pC\) 给出：在适配的复单位标架
\[
E,JE\in TC,\qquad N,JN\in NC,
\]
存在 \(\beta(p)\neq0\)，使得
\[
(\nabla_{\zeta N}a)^\sharp
 =\bar\zeta\,\beta\,E,\qquad \zeta\in\mathbb C .
\tag{1}
\]
换言之，\(DT\) 的唯一非零复块是一个反复线性秩一映射
\[
\bar N\longrightarrow TC.
\]
其核和像均为 \(TC\)。

AAD 的 Ricci 恒等式为
\[
da-Ja\wedge b=-R(J\phi),\qquad
d(Ja)+a\wedge b=-R(\phi).
\tag{2}
\]
在 \(C\) 上 \(a=0\)，而且 Step-62 的曲率字典给出
\[
\eta=W_2^+=0,\qquad \kappa=s.
\]
因此标量曲率项在 (2) 中抵消，留下
\[
da|_C=-W_3^+(J\phi),\qquad
d(Ja)|_C=-W_3^+(\phi),
\tag{3}
\]
这里的精确符号取决于 \(\phi,J\phi\) 的定向约定，但其内容不变：\(\beta\) 与 \(W_3^+|_C\) 之间是一个固定的、复线性的点态同构。故
\[
\beta\in\Gamma(L),\qquad
L=K_J^{-2}|_C
\cong \bigl(T^{1,0}C\otimes N^{1,0}C\bigr)^{\otimes2}.
\tag{4}
\]
这也解释了 Step-63 中 \(W_3^+|_C\) 的线丛和次数公式。

特别要注意：\(W_3^+\) 是 \(L\) 的截面，而不是一个普通复函数。若
\[
W_3^+=\frac{\lambda}{2}(\phi\otimes\phi-J\phi\otimes J\phi)
+\frac{\mu}{2}(\phi\otimes J\phi+J\phi\otimes\phi),
\]
则 \(w=\lambda+i\mu\) 在规范旋转 \(\phi\mapsto e^{i\theta}\phi\) 下变为
\[
w\mapsto e^{-2i\theta}w.
\]
相应的 \(L\)-联络为
\[
D^L_Xw=X(w)+2i\,b(X)w
\tag{5}
\]
（整体符号随联络约定改变）。法丛联络通过 \(b|_C\) 进入；第二基本形式不改变行列式联络中的 \(U(1)\) 部分，因为适配的切—法非对角联络项在行列式中相互抵消。但它仍会出现在把环境中的二阶、三阶导数限制到 \(C\) 时的 Gauss–Weingarten 修正中。

更稳妥地说，若 \(B:NC\to TC\) 表示 (1) 的法向首系数，则沿 \(C\) 的导数应使用
\[
D_XB
\]
这个 \(\operatorname{Hom}_{\mathbb C}(NC,TC)\)-诱导联络，而不是普通坐标导数。环境二阶导数转换为 \(D_XB\) 时，会出现第二基本形式作用于输入和输出的项。不能在平直坐标中简单把这些项删去；但也不能把它们误认为新的零阶曲率项。

---

### 2. AAD/Bianchi 方程在 \(C\) 上的精确约束

Step-55 中 Einstein 情形的 AAD 微分 Bianchi 方程是
\[
0=-\frac38(d^Jq)_Z\Omega
+\frac14(dq\wedge Z^\flat)^+
+(\delta\eta)_Z\Omega
+\frac{\kappa}{4}\nabla_{JZ}\Omega
+\nabla_{\eta(Z)}\Omega
+\nabla_{JZ}\eta
+2(\delta W_3^+)_Z .
\tag{6}
\]

由于 \(q=|T|^2\) 在 \(C\) 上恒为零，且 \(q\ge0\)，故不仅其切向导数为零，而且
\[
dq|_C=0.
\]
再由 \(a=0\)、\(\eta=0\)、\(\kappa=s\) 以及 \(\nabla\Omega=0\) 在 \(C\) 上成立，(6) 的 \(\llbracket\Lambda^{0,2}\rrbracket\)-分量化为
\[
\boxed{
2(\delta W_3^+)_Z^{\prime\prime}
+\bigl(\nabla_{JZ}\eta\bigr)^{\prime\prime}=0
\qquad\text{on }C .
}
\tag{7}
\]
这里 \(Z\) 可取法向方向。其 \(\Omega\)-分量则给出 \(\delta\eta\) 与标量分量的关系，但不产生 \(W_3^+|_C\) 的封闭输运方程。

在 \(b(p)=0\) 的规范和
\[
e_2=Je_1\in TC,\qquad e_4=Je_3\in NC
\]
下，若 \(w=\lambda+i\mu\) 表示 \(W_3^+|_C\)，则法向 \(Z=e_3,e_4\) 时的散度只含 \(e_1,e_2\) 方向的切向导数。等价地，(7) 可压缩成一个形式为
\[
\boxed{
\bigl(D^L_{e_1}-iD^L_{e_2}\bigr)w
=\Xi,
}
\tag{8}
\]
的内禀方程，其中
\[
\Xi
\quad\text{是}\quad
(\nabla^\perp\eta)|_C
\]
的相应复分量。具体的 \(i\) 号和 \(e_1\mp ie_2\) 取决于复坐标与 \(J\) 的约定，但以下事实不依赖约定：

1. 左端是 \(L=K_J^{-2}|_C\) 上的 Cauchy–Riemann 型协变导数；
2. 法丛联络已经包含在 \(D^L\) 中；
3. 右端是 \(\eta\) 的法向一阶导数，而不是 \(w\) 的零阶倍数。

因此，目前的精确方程不是
\[
D^L_{\bar z}w=A\,w+B\,\bar w
\tag{9}
\]
这种可直接应用相似性原理的方程。除非进一步证明
\[
\Xi=A\,w+B\,\bar w
\]
且 \(A,B\) 在 \(w=0\) 处连续有界，否则不能把 \(\Xi/w\) 当作一个合法的系数。仅在 \(w\neq0\) 处将方程除以 \(w\)，无法控制异常零点的绕数。

---

### 3. Step-64 二阶恒等式的正确含义

Step-64 的二阶零点恒等式及其曲面限制给出，在 \(DT(p)=0\) 的异常点
\[
\delta=0,\qquad
Q^1_{12}=0,\qquad
Q^2_{22}=0,
\]
因而
\[
D^Lw(p)=0
\tag{10}
\]
（在适配标架中即 \(dw(p)=0\)，联络项因 \(w(p)=0\) 消失）。

这说明异常零点的 \(W_3^+|_C\) 的一阶 Taylor 项消失，但**不说明其局部绕数不能为 \(\pm1\)**。例如
\[
w_+(z)=z|z|^2,\qquad
w_-(z)=\bar z|z|^2
\]
都满足 \(dw(0)=0\)，但其绕数分别为 \(+1\) 和 \(-1\)。所以“线性项为零 \(\Rightarrow\) 绕数不能是 \(\pm1\)”是错误推理。

同样，若 (8) 的右端暂时为零，则在平直标架中可能得到
\[
(\partial_x-i\partial_y)w=0,
\]
其解依赖于 \(\bar z\)，非零退化零点自然带有负绕数。究竟应称其为“全纯型”还是“反全纯型”，必须连同 \(L\) 的复结构和曲面定向一起判断；不能仅凭算子符号断言正绕数。

---

### 4. 拟议高阶正规形的地位

由 Spirit 材料中的齐次主部恒等式 \((H_m)\)，可以提出如下很有力但仍需谨慎标记的结论：若 \(a\) 在 \(p\) 的最低非零总阶为 \(m\ge2\)，则其主部被迫具有
\[
f_m(z)=\kappa\,\bar z_2^{\,m}e_1.
\tag{11}
\]
这与 Step-64 的 \(m=2\) 结果一致，并说明最低阶扭率主部纯粹沿法向退化。它支持的可靠后果是：

- 最低阶主部本身不产生 \(W_3^+|_C\) 的切向系数；
- 低于相应阶数的 \(W_3^+|_C\) 切向 Taylor 系数会消失；
- 需要更高阶中含有一个法向因子、同时带有切向变量的项，才可能产生 \(W_3^+|_C\) 的首个非零切向项。

但 (11) 不是完整 Einstein 解析芽的分类，也没有规定该首个切向项的复型。形式上完全可能出现
\[
a(z_1,z_2)
=\kappa\,\bar z_2^{\,m}e_1
+\bar z_2\,P(z_1,\bar z_1)e_1+\cdots,
\tag{12}
\]
其中 \(P\) 的 \(z_1,\bar z_1\) 组成决定 \(W_3^+|_C\) 的局部绕数。是否所有此类项都能延拓为完整 Einstein–almost-Kähler 解，尚未由所给材料证明；但现有主部恒等式本身没有排除负绕数。

尤其不能把 Branch 2 中关于某个 \(|z_2|^2\)-系数的“严格正性平均”直接升级为
\[
W_3^+|_C\text{ 在每个分支上处处非零或恒等为零}.
\]
该论证明确依赖尚未完成的曲率修正计算、第二基本形式项的消去以及高阶系数的符号控制。所给源材料并未证明这些“curved terms”具有所需阶数和正性。因此它目前只能作为待验证路线，不能作为已得定理，更不能据此消除异常点或负绕数。

---

### 5. 与 Step-63 次数公式的关系

AAD 的规范曲率形式为
\[
\gamma_J=R(\Omega)-a\wedge Ja.
\]
在 \(C\) 上 \(a=0\)，并且 Einstein、\(\eta=0\) 给出
\[
R(\Omega)|_C=\frac{s}{4}\Omega|_C.
\]
因此
\[
\deg(K_J^{-2}|_C)
=2c_1(M,J)[C]
=\frac{s\,\operatorname{Area}(C)}{4\pi}
=2\bigl(\chi(C)+C\cdot C\bigr).
\tag{13}
\]

所以：

- 若 \(DT\) 在 \(C\) 上处处秩二，则 \(W_3^+|_C\) 无零点，平凡化 \(K_J^{-2}|_C\)，与 \(s\neq0\) 的 (13) 矛盾；
- 若秩二点稠密且异常点孤立，则局部绕数总和等于 (13)；
- 当 \(s<0\) 时，总绕数为负，因此至少需要负的局部贡献，除非零集非离散并采用局部化第一 Chern 类；
- 现有 AAD 方程 (8) 含有独立的法向源项 \(\Xi\)，尚未给出排除负绕数的相似性原理；
- 若 \(DT=0\) 沿整个 \(C\)，则 \(W_3^+|_C\equiv0\)，此时不能把次数写成孤立零点绕数之和，必须使用零截面的局部化 Chern 类。

## 结论

从 supplied equations 真正得到的是
\[
\boxed{
(D^L_{e_1}-iD^L_{e_2})\,
\bigl(W_3^+|_C\bigr)
=
\text{the corresponding normal derivative of }\eta ,
}
\]
其中 \(D^L\) 同时包含切丛和法丛联络；第二基本形式通过将环境高阶导数限制到 \(C\) 的 Gauss–Weingarten 修正进入，但在 \(L=K_J^{-2}|_C\) 的行列式联络中不产生额外的非对角 \(U(1)\) 项。

这不是闭合的相似性原理方程，因为右端尚未被证明可除以 \(W_3^+|_C\)，也未被证明由其零阶项有界控制。Step-64 恒等式和拟议的高阶纯法向正规形只说明异常点高度退化；它们不决定局部绕数。因而，依据现有材料，负绕数仍被允许，并且在 \(s<0\) 时与全局次数公式相容。真正未解决的科学对象是：是否存在一个包含 \(\eta\) 法向导数的完整输运系统，使其右端在 \(W_3^+=0\) 处仍具有可除性或有界零阶控制。