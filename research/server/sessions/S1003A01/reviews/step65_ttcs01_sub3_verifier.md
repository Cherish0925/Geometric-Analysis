# TTCS Independent Branch Record

```json
{
  "step_id": 65,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 2,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step63_SU2_nut_and_clean_zero_surface.md",
    "Sessions/S1003A01/workspace/notes/step64_exceptional_points_second_order_zero.md",
    "Sessions/S1003A01/workspace/notes/spirit_step64_homogeneous_zero_identity.md",
    "Sessions/S1003A01/workspace/notes/step55_darboux_ricci_compatibility.md",
    "Knowledge/objects/papers/Local-models-and-integrability-of-certain-almost-Kahler-4-manifolds--89a416df784a--79aaa9509e7d/object.md"
  ]
}
```

## Task

Analyze the compact torsion-zero surface problem using the established Step-62 cone, Step-63 degree formula, and the proposed higher-order leading normal form. The goal is to derive, if possible, an intrinsic normal-expansion equation along a smooth J-complex surface C contained in {T=0}: identify the rank-two normal coefficient corresponding to W_3^+|_C, how the exact AAD/soldered equations constrain its tangential covariant derivative including normal connection and second fundamental form, and whether they imply a similarity-principle relation or allow negative winding. Do not assume holomorphicity. Distinguish what follows from the supplied equations from a proposed route; correct the false inference that zero linear term controls winding.

## Output

# 科学核验备忘录：沿 \(J\)-复零曲面 \(C\) 的法向展开与 \(W_3^+\) 绕数

## 1. 秩二点的内禀法向系数

采用 AAD 标架
\[
\nabla\Omega=a\otimes\phi-Ja\otimes J\phi,\qquad
\nabla\phi=-a\otimes\Omega+b\otimes J\phi .
\]
因此 \(T=\nabla\Omega=0\) 等价于 \(a=0\)。若 \(C\subset\{T=0\}\) 是光滑 \(J\)-复曲面，则
\[
\nabla_Xa=0,\qquad X\in TC.
\]
记
\[
B_p(v):=(\nabla_va)^\sharp,\qquad v\in T_pM .
\]

在 \(p\in C\) 的秩二点，Step-62 首射流
\[
f(z)=cz+(S+A)\bar z
\]
满足 \(TC\subset\ker Df\)。实行列式公式迫使 \(c=0\) 与 \(\det(S+A)=0\)。把反复线性部分写成秩一分解 \(B=u\otimes v^T\)，Step-62 圆锥关系
\[
\|A\|^2=\|S\|^2
\]
等价于 \(u\perp_{\mathbb C}v\)。反复线性映射 \(z\mapsto B\bar z\) 的核是 \(v^\perp\)，故
\[
\boxed{\ker B=\operatorname{im}B=TC.}
\]
于是，在单位复切向量 \(E\) 和单位复法向量 \(N\) 下，
\[
B(\zeta N)=\bar\zeta\,\beta E,\qquad \beta\neq0.
\tag{1.1}
\]
这就是秩二的法向首系数。其 AAD 规范依赖与 \(\phi\) 的规范依赖结合后，给出规范无关的 \(W_3^+|_C\)。

更直接地，AAD Ricci 恒等式
\[
da-Ja\wedge b=-R(J\phi),\qquad
d(Ja)+a\wedge b=-R(\phi)
\]
在 \(C\) 上化为
\[
da=-R(J\phi),\qquad d(Ja)=-R(\phi).
\]
此时 \(q=0,\eta=0\)，且 Einstein 曲率在
\(\langle\phi,J\phi\rangle\) 上的标量部分恰与 \(s/12\) 抵消，所以
\[
\boxed{
da=-W_3^+(J\phi),\qquad d(Ja)=-W_3^+(\phi).
}
\tag{1.2}
\]
因此 (1.1) 与 \(W_3^+|_C\) 之间是一个固定的复线性同构。

例如取实正交标架
\[
e_2=Je_1\in TC,\qquad e_4=Je_3\in NC,
\]
以及
\[
\phi=e^{13}-e^{24},\qquad J\phi=e^{14}+e^{23}.
\]
若
\[
B(e_3)=\rho e^1,\qquad B(e_4)=-\rho e^2,
\]
则
\[
da=-\rho\phi,\qquad d(Ja)=-\rho J\phi,
\]
故 \(W_3^+(\phi)=\rho J\phi,\ W_3^+(J\phi)=\rho\phi\)。这具体展示了法向首系数与 \(W_3^+\) 系数只差固定单位复数。

---

## 2. 法向展开、法丛联络与第二基本形式

法向指数坐标中的内禀展开是
\[
a(\exp_x\nu)=B_x(\nu)+O(|\nu|^2),\qquad x\in C,\ \nu\in N_xC.
\tag{2.1}
\]
在复记号下可写成
\[
a^{\mathbb C}(z,\zeta)
   =\beta(z)\,\bar\zeta\,E^\flat+O(|\zeta|^2),
\tag{2.2}
\]
但普通导数必须换成切丛、法丛及 AAD 规范联络所诱导的协变导数。

设 \(\mathrm{II}\) 是 \(C\subset M\) 的第二基本形式。由 \(a|_C=0\) 可直接得到两条焊接公式：
\[
\boxed{
(\nabla^2a)(X,Y)=-B(\mathrm{II}(X,Y)),
\qquad X,Y\in TC,
}
\tag{2.3}
\]
以及
\[
\boxed{
(\nabla^2a)(X,\nu)
   =D_XB(\nu)+\mathrm{II}\bigl(X,B(\nu)\bigr),
\qquad X\in TC,\ \nu\in NC .
}
\tag{2.4}
\]
这里 \(D\) 是 \(\operatorname{Hom}_{\bar{\mathbb C}}(NC,TC)\) 的诱导联络。公式 (2.3) 描述核随 \(C\) 弯曲时产生的切—切二阶分量；公式 (2.4) 中第二项描述像空间 \(TC\) 随 \(C\) 弯曲时产生的法向分量。因而在秩二点使用平直坐标写二阶射流时，所有与 \(\mathrm{II}\beta\) 有关的项都必须保留。

另一方面，\(W_3^+|_C\) 是复线丛
\[
L:=K_J^{-2}|_C
   \cong\bigl(T^{1,0}C\otimes N^{1,0}C\bigr)^{\otimes2}
\tag{2.5}
\]
的截面。若
\[
\nabla_XE=i\alpha_T(X)E+h(X)N,\qquad
\nabla_XN=-\overline{h(X)}E+i\alpha_N(X)N,
\]
则 \(h\) 正是第二基本形式的复表示，而
\[
\nabla_X(E\wedge N)
   =i\bigl(\alpha_T(X)+\alpha_N(X)\bigr)(E\wedge N).
\tag{2.6}
\]
可见第二基本形式作为酉联络矩阵的非对角项，在行列式联络中相消；\(L\) 的联络只看见切向与法向 \(U(1)\) 联络之和。

把
\[
W_3^+
 =\frac{\lambda}{2}(\phi\otimes\phi-J\phi\otimes J\phi)
 +\frac{\mu}{2}(\phi\otimes J\phi+J\phi\otimes\phi),
\qquad w:=\lambda+i\mu ,
\tag{2.7}
\]
则在规范旋转
\[
\phi'=\cos\theta\,\phi+\sin\theta\,J\phi
\]
下，
\[
w'=e^{-2i\theta}w,\qquad b'=b+d\theta .
\]
所以 \(L\) 上的协变导数为
\[
\boxed{
D^L_Xw=X(w)+2i\,b(X)w .
}
\tag{2.8}
\]
按上述适配标架的符号约定，\(b|_C=\alpha_T+\alpha_N\)。这正是法丛联络进入 \(W_3^+|_C\) 切向导数的方式；\(\mathrm{II}\) 则通过 (2.3)–(2.4) 进入完整二阶扭率射流。

微分 (1.2) 还给出精确的焊接等式
\[
\operatorname{Alt}(\nabla_X\nabla a)
 =-(\nabla_XW_3^+)(J\phi)+b(X)W_3^+(\phi),
\tag{2.9}
\]
\[
\operatorname{Alt}(\nabla_X\nabla(Ja))
 =-(\nabla_XW_3^+)(\phi)-b(X)W_3^+(J\phi).
\tag{2.10}
\]
它们把 \(D^L_Xw\)、法向首系数的协变导数以及 (2.3)–(2.4) 中的外在几何项直接连接起来。

---

## 3. AAD Bianchi 方程给出的切向一阶方程

AAD 方程 (33)，即 Step-55 的 (3.6)，在 \(C\) 上满足
\[
q=0,\quad dq=0,\quad \eta=0,\quad \nabla\Omega=0,\quad \kappa=s.
\]
取其 \(\llbracket\Lambda^{0,2}\rrbracket\) 分量，得到
\[
\boxed{
2(\delta W_3^+)_Z''+(\nabla_{JZ}\eta)''=0.
}
\tag{3.1}
\]

令 \(Z=e_3\) 或 \(e_4=Je_3\)。在一点处选取 \(b=0\) 的 AAD 规范，由 (2.7) 直接计算散度：
\[
2(\delta W_3^+)_{e_3}''
 =-\bigl(\lambda_1+\mu_2\bigr)\phi
  -\bigl(\mu_1-\lambda_2\bigr)J\phi,
\tag{3.2}
\]
\[
2(\delta W_3^+)_{e_4}''
 =-\bigl(\mu_1-\lambda_2\bigr)\phi
  +\bigl(\lambda_1+\mu_2\bigr)J\phi,
\tag{3.3}
\]
其中下标 \(1,2\) 表示沿 \(e_1,e_2\) 的导数。法向导数 \(e_3,e_4\) 不出现在这些式子中，因为 \(\phi,J\phi\) 都是切—法混合二形式，在法—法二向量上取值为零。

置
\[
A=\lambda_1+\mu_2,\qquad B_0=\mu_1-\lambda_2.
\]
方程 (3.1) 等价于
\[
(\nabla_{e_4}\eta)''
   =A\phi+B_0J\phi,
\tag{3.4}
\]
\[
(\nabla_{e_3}\eta)''
   =-B_0\phi+A J\phi.
\tag{3.5}
\]
协变化后，这一对公式可压缩为
\[
\boxed{
\bigl(D^L_{e_1}-iD^L_{e_2}\bigr)w=\Xi,
}
\tag{3.6}
\]
其中 \(\Xi\) 是由 \((\nabla_{Je_3}\eta)''\) 对应得到的 \(L\)-值复系数。法向标架旋转与 \(\eta\) 的规范旋转恰好使 \(\Xi\) 也按 \(L\) 的过渡函数变换。

这是由现有 AAD 方程得到的内禀法向展开方程。它有三个重要特征：

1. 左端确实是 \(C\) 上的 Cauchy–Riemann 型切向算子；
2. 法丛联络已经包含在 \(D^L\) 中；
3. 右端是 \(\eta\) 的法向一阶射流，而不是 \(w\) 的零阶表达式。

因此现有方程给出的是一个带法向源项的一阶方程，并未给出
\[
\Xi=A_0w+B_0\bar w
\tag{3.7}
\]
这类系数可连续穿过 \(w=0\) 的关系。仅在 \(w\neq0\) 处写 \(\Xi/w\) 没有几何内容，因为该比值可在异常点发散。

---

## 4. 与二阶射流计算的吻合

在忽略一点处联络系数的局部模型中，取 \(z_1\) 为切向复坐标、\(z_2\) 为法向复坐标。秩二首项为
\[
f_1=b_0\bar z_2e_1.
\]
Step-64 的一般二次主符号解为
\[
f_2=z\,\delta(\bar z)+Q(\bar z,\bar z).
\]
扣除 (2.3)–(2.4) 所给出的 \(\mathrm{II}\,b_0\) 焊接项后，沿 \(C\) 的法向系数具有形式
\[
w(z_1)
 =w_0+\delta_2z_1+2Q^1_{12}\bar z_1+O(|z_1|^2).
\tag{4.1}
\]
这里：

- \(\delta_2\) 同时控制 \(w\) 的一个 Cauchy–Riemann 导数和 \(\eta\) 的法向导数；
- \(Q^1_{12}\) 控制另一个切向复导数；
- \(C\) 上持续满足秩一圆锥会消去法向像分量，对应 Step-64 中的 \(Q^2_{12}=0\)。

这正与 (3.6) 相符：一个切向复导数等于 \(\nabla_N\eta\) 的相应分量，但另一个切向复导数没有被化成 \(w\) 的零阶倍数。

在异常点 \(DT(p)=0\) 时，\(\mathrm{II}\) 不影响最低二阶条件，因为所有一阶扭率项已消失。Step-64 二阶恒等式与曲面条件给出
\[
|Q^1_{12}|^2+|Q^2_{22}|^2+\frac{15}{4}|\delta_2|^2=0,
\]
从而
\[
\boxed{D^Lw(p)=0.}
\tag{4.2}
\]
这是“切向一阶协变导数为零”，而不是绕数信息。

---

## 5. 高阶首项正规形能推出什么

若接受 `spirit_step64_homogeneous_zero_identity.md` 中由 \((H_m)\) 推出的高阶正规形，则在扭率总消失阶为 \(m\ge2\) 的异常点，
\[
f_m(z)=\kappa\,\bar z_2^{\,m}e_1.
\tag{5.1}
\]
因为 \(W_3^+\) 是扭率法向一阶导数的曲率像，(5.1) 对 \(W_3^+|_C\) 没有非零贡献。更精确地，任意不超过 \(m-1\) 阶的切向导数都会把至少一个切向变量代入纯法向 \(m\)-线性张量，故
\[
\boxed{
j^{m-1}_p\bigl(W_3^+|_C\bigr)=0.
}
\tag{5.2}
\]
所以 \(W_3^+|_C\) 的 Taylor 消失阶至少为 \(m\)。

但 (5.1) 只描述扭率在该点的最低总次数项。以后次数中的
\[
\bar z_2\,P(z_1,\bar z_1)e_1
\tag{5.3}
\]
才决定 \(W_3^+|_C\) 的首个非零切向项，而 (5.1) 本身没有规定 \(P\) 的绕数。

例如形式表达式
\[
f(z_1,z_2)
 =\kappa\bar z_2^{\,m}e_1
  +\bar z_2\,\bar z_1^{\,r}e_1+\cdots,
\qquad r\ge m,
\tag{5.4}
\]
保持 \(C=\{z_2=0\}\) 上扭率为零，最低项仍是 (5.1)，并且第二项属于主半旋量方程允许的反全纯多项式部分 \(g(\bar z)\)。它给出
\[
W_3^+|_C\sim\bar z_1^{\,r},
\]
其绕数为 \(-r\)。式 (5.4) 尚不是完整 Einstein germ；它说明 Step-62 圆锥、二阶恒等式、高阶最低项正规形和主符号方程这几层信息都没有排除负绕数。

---

## 6. “零线性项控制绕数”这一推理不成立

光滑甚至实解析复值截面可同时满足 \(dw(0)=0\) 和绕数 \(\pm1\)。最简单的例子是
\[
w_+(z)=z|z|^2=z^2\bar z,\qquad
w_-(z)=\bar z|z|^2=z\bar z^2.
\]
二者都在原点消失到三阶，但局部绕数分别为 \(+1\) 与 \(-1\)。因此 Step-64 中“线性项消失，所以绕数不能为 \(\pm1\)”这一句不成立。现有结果只说明异常零点是退化零点；Taylor 消失阶与拓扑绕数是两个不同量。

此外，按 \(Je_1=e_2\) 和 \(w=\lambda+i\mu\) 的上述规范，若 (3.6) 的源项恰好为零，则
\[
(D^L_{e_1}-iD^L_{e_2})w=0.
\]
在平直标架中这是
\[
(\partial_x-i\partial_y)w=0,
\]
其解局部依赖于 \(\bar z\)，非零阶零点具有负的 \(J\)-定向绕数。因而即使以后得到相似性原理型方程，也必须先确认它作用于 \(L=K_J^{-2}|_C\) 的哪一个复结构。把系数取共轭会把算子写成通常的 \(\bar\partial\)，但同时也把线丛换成共轭线丛，绕数符号随之反转。

---

## 7. 与 Step-63 全局次数公式的关系

由 AAD canonical Chern form
\[
\gamma_J=R(\Omega)-a\wedge Ja
\]
以及 \(a|_C=0,\eta|_C=0\)，
\[
\gamma_J|_C=\frac{s}{4}\Omega|_C.
\]
由于 \(L=K_J^{-2}|_C\)，
\[
\boxed{
\deg L
 =2c_1(M,J)[C]
 =\frac{s\,\operatorname{Area}(C)}{4\pi}
 =2\bigl(\chi(C)+C\!\cdot\!C\bigr).
}
\tag{7.1}
\]

因此：

- 若 \(DT\) 在整个闭曲面上秩二，则 \(W_3^+|_C\) 无零点，平凡化 \(L\)，与 \(s\neq0\) 时的 (7.1) 冲突。这就是 Step-63 的 clean-surface 定理。
- 若秩二点稠密且异常点孤立，则所有局部绕数之和等于 (7.1)。
- 当 \(s<0\) 时，总绕数必须为负。方程 (3.6) 并未排除这一情形；在源项消失的模型中，它甚至自然产生反全纯型、负绕数零点。
- 若异常点非孤立，则应使用 \(W_3^+\) 的局部化第一 Chern 类，不能用孤立零点求和。
- 若 \(DT=0\) 沿整个 \(C\)，则 \(W_3^+|_C\equiv0\)。此时次数仍由 (7.1) 给出，但不存在由该零截面直接定义的孤立绕数分解。

## 核心结论

现有材料给出了一个明确的内禀法向方程：
\[
\boxed{
(D^L_{e_1}-iD^L_{e_2})\,W_3^+|_C
   =\mathcal N\bigl((\nabla^\perp\eta)|_C\bigr),
}
\]
其中 \(D^L\) 含切丛与法丛联络，第二基本形式通过扭率二阶焊接公式 (2.3)–(2.4) 进入；在 \(K_J^{-2}\) 的行列式联络中，其非对角贡献相消。

AAD 方程尚未把右端写成 \(W_3^+|_C\) 的有界零阶表达式，所以目前没有得到穿过异常点的相似性原理。Step-64 恒等式以及拟议的高阶正规形只提高异常点的 Taylor 消失阶，不决定绕数符号。负绕数与 Step-63 的 \(s<0\) 次数公式相容，并且在现有首项与主符号方程中仍可出现。真正决定绕数的缺失关系，是 \((\nabla^\perp\eta)|_C\) 对 \(W_3^+|_C\) 的可除性或一个在零点处仍有连续系数的闭合输运系统。