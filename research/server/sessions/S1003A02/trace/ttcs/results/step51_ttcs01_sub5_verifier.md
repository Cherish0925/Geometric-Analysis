# TTCS Independent Branch Record

```json
{
  "step_id": 51,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 3,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A02/workspace/notes/step50_minimizer_entry_PS_noncollapsed_alternative.md",
    "Knowledge/objects/papers/Blowing-up-and-desingularizing-constant-scalar-curvature--7e9bd4072728--db5d10d44a5c/object.md"
  ]
}
```

## Task

Verify Theorem K-infinity in the Step-50 note: for the blow-up (including infinitely-near points) of any minimal compact complex surface of general type, is inf over Kähler metrics of P exactly 8π²k and not attained? Check the lower formula and Hodge-index argument for nef non-ample K_X; the Arezzo-Pacard hypotheses on the canonical orbifold and subsequent smooth blow-ups; the Kähler class signs and epsilon expansion; whether negative cscK metrics are Yamabe representatives; and the statement D_W=0, DeltaV→0. Return a precise theorem, scope, and any needed repair.

## Output

# 科学核验备忘录：Theorem \(K_\infty\)

## 1. 精确定理

设 \((X,J_X)\) 是极小紧致一般型复曲面，
\[
A:=K_X^2=c_1^2(X)>0.
\]
令
\[
M=X_k\xrightarrow{\pi_k}X_{k-1}\to\cdots\to X_1\to X_0=X
\]
由 \(k\) 次复吹起得到；每次中心可以是当前曲面的任意光滑点，因而允许位于先前例外曲线上，即允许 infinitely-near points。记 \(J\) 为由此得到的复结构。则对所有与 \(J\) 相容的 Kähler 度量，
\[
\boxed{\inf_{g\ {\rm K\ddot ahler\ on}\ (M,J)}
       \int_M|\operatorname{Ric}^{\circ}_g|^2\,d\mu_g
       =8\pi^2k.}
\]
若 \(k\ge1\)，此下确界不由任何 Kähler 度量实现。

这里必须把度量类别写成“与给定吹起复结构 \(J\) 相容的 Kähler 度量”。现有证明不覆盖同一光滑四流形上与其他复结构相容的全部 Kähler 度量，也不涉及全部 Riemannian 度量。

补充地，当 \(k=0\) 时，
\[
\inf_{g\ {\rm K\ddot ahler\ on}\ X}P(g)=0.
\]
若 \(K_X\) ample，则由负 Kähler–Einstein 度量实现；若 \(K_X\) nef、big 但不 ample，则不实现。

---

## 2. Kähler 公式及常数

令 \(\Omega=[\omega]\)，采用
\[
d\mu=\frac{\omega^2}{2},\qquad [\rho]=2\pi c_1(M),\qquad c_1(M)=-K_M.
\]
对 Kähler 曲面，
\[
\int_M s\,d\mu
 =2\int_M\rho\wedge\omega
 =4\pi c_1(M)\cdot\Omega
 =-4\pi K_M\cdot\Omega,
\]
故
\[
\bar s=-\,\frac{8\pi K_M\cdot\Omega}{\Omega^2}.
\]
Kähler 曲面的 Chern–Weil 恒等式给出
\[
P(g)=\int_M|\operatorname{Ric}^{\circ}|^2d\mu
     =\frac14\int_Ms^2d\mu-8\pi^2c_1^2(M).
\]
由于每次吹起使 \(c_1^2\) 减少 \(1\)，
\[
c_1^2(M)=K_M^2=A-k.
\]
分解 \(s=\bar s+(s-\bar s)\)，并用
\[
\operatorname{Vol}(g)=\frac{\Omega^2}{2},
\]
得到精确公式
\[
\boxed{
\widehat P(g):=\frac{P(g)}{8\pi^2}
 =
 \frac{(K_M\cdot\Omega)^2}{\Omega^2}
 +\frac1{32\pi^2}\int_M(s-\bar s)^2\,d\mu
 -A+k.}
\tag{2.1}
\]
Step-50 中的系数是正确的。

---

## 3. nef 但不 ample 时的 Hodge 指数论证

对 infinitely-near 吹起，必须谨慎定义例外类。令 \(e_i\in H^2(M;\mathbb Z)\) 是第 \(i\) 次产生的例外除子在最终曲面上的**全变换类**。则
\[
e_i\cdot e_j=-\delta_{ij},\qquad
\pi^*K_X\cdot e_i=0,\qquad
K_M=\pi^*K_X+\sum_{i=1}^ke_i.
\tag{3.1}
\]
每个全变换是非零有效除子，虽未必不可约，故对任意 Kähler 类 \(\Omega\)，
\[
e_i\cdot\Omega>0.
\tag{3.2}
\]

令 \(L=\pi^*K_X\)。极小一般型曲面的 \(K_X\) nef 且 big，所以
\[
L^2=A>0.
\]
Hodge 指数定理对位于正锥闭包中的 \(L\) 与 Kähler 类 \(\Omega\) 给出
\[
(L\cdot\Omega)^2\ge L^2\Omega^2=A\Omega^2,
\qquad L\cdot\Omega>0.
\tag{3.3}
\]
不需要 \(K_X\) ample。由 (3.1)–(3.3)，当 \(k\ge1\) 时，
\[
K_M\cdot\Omega
 =L\cdot\Omega+\sum_i e_i\cdot\Omega
 >L\cdot\Omega>0,
\]
从而
\[
\frac{(K_M\cdot\Omega)^2}{\Omega^2}>A.
\]
代入 (2.1)，
\[
\widehat P(g)>k,\qquad P(g)>8\pi^2k
\tag{3.4}
\]
对每个实际 Kähler 度量均成立。因此一旦构造出趋近 \(8\pi^2k\) 的序列，不实现性立即成立。

Step-50 应把 \(E_i\) 明确写成“全变换类”；若把它们理解成最终曲面上的不可约真变换，则 \(K_M=\pi^*K_X+\sum E_i\) 在 infinitely-near 情形通常不对，系数也会改变。

---

## 4. Arezzo–Pacard 输入确实适用

令
\[
q:X\longrightarrow\bar X
\]
为极小曲面的 canonical model 映射。供应的 Arezzo–Pacard 文本给出以下所需事实：

1. \(\bar X\) 的奇点是 isolated quotient singularities
   \[
   \mathbb C^2/\Gamma,\qquad \Gamma\subset SU(2).
   \]
2. \(\bar X\) 有负标量曲率 Kähler–Einstein orbifold 度量 \(\omega_{\rm KE}\)。
3. 其自同构群离散，所以没有非零全纯向量场；这正是 Theorem 1.3 的非退化情形。
4. \(SU(2)\) 奇点有 Kronheimer crepant Ricci-flat ALE resolution，并具有 Theorem 1.3 所需的渐近衰减；这在 Corollary 8.2–8.3 的证明中被直接使用。
5. Theorem 1.3 于是给出 \(X\) 上的负 cscK 度量，并在奇点之外收敛到 \(\omega_{\rm KE}\)。
6. 一般型曲面没有非零全纯向量场；吹起后仍是一般型。因此 Theorem 1.1 可以在每一步任意指定的光滑点继续使用。若下一中心位于先前例外曲线上，它仍是当前光滑曲面上的普通光滑点。

因此：

- canonical model 的所有奇点可同时解消；
- 任意给定的后续光滑吹起可以逐步完成；
- infinitely-near 配置由迭代 Theorem 1.1 得到；
- 每一步所得 cscK 度量仍有负标量曲率。

这里不需要各次 gluing parameter 有共同速率。选择 canonical desingularization 参数趋零，再依次选择每个吹起参数充分小，最后取对角序列即可。

---

## 5. Kähler 类符号与上界

Kähler–Einstein orbifold 类可写成
\[
[\omega_{\rm KE}]=\lambda\,c_1(K_{\bar X}),\qquad \lambda>0.
\]
由于 \(q\) crepant，
\[
q^*K_{\bar X}=K_X.
\]
Arezzo–Pacard 解消后，在 \(X\) 上的类可写成
\[
\Omega_\delta=\lambda K_X+\xi_\delta,
\tag{5.1}
\]
其中 \(\xi_\delta\) 位于 canonical 例外曲线张成的负定子空间，并满足
\[
K_X\cdot\xi_\delta=0,\qquad
\xi_\delta^2\le0,\qquad
\xi_\delta\longrightarrow0.
\tag{5.2}
\]
符号是加号：\(\xi_\delta\) 对解消曲线有正面积，但其平方为负。

在后续第 \(i\) 次光滑吹起中，Burns 类满足
\[
[\eta_{\rm Burns}]=-\operatorname{PD}[E_i],
\]
所以最终类为
\[
\Omega_{\delta,\mathbf t}
 =\pi^*\Omega_\delta-\sum_{i=1}^kt_ie_i,
 \qquad t_i>0.
\tag{5.3}
\]
此符号也正确，因为
\[
\Omega_{\delta,\mathbf t}\cdot e_i=t_i>0.
\]

记
\[
T=\sum_it_i,\qquad Q=\sum_it_i^2.
\]
由正交分解，
\[
K_M\cdot\Omega_{\delta,\mathbf t}
 =\lambda A+T,
\qquad
\Omega_{\delta,\mathbf t}^2
 =\lambda^2A+\xi_\delta^2-Q.
\tag{5.4}
\]
这些度量是 cscK，故 (2.1) 中的标量曲率方差项为零。因此
\[
\boxed{
\widehat P(\Omega_{\delta,\mathbf t})
 =
 k+
 \frac{(\lambda A+T)^2}
      {\lambda^2A+\xi_\delta^2-Q}
 -A.}
\tag{5.5}
\]
令 \(\delta\to0\) 且所有 \(t_i\to0\)，便有
\[
\widehat P(\Omega_{\delta,\mathbf t})\longrightarrow k.
\tag{5.6}
\]
结合 (3.4)，得到精确下确界及 \(k\ge1\) 时的不实现性。

### Step-50 中 \(\varepsilon\)-展开的修订

若确有共同速率
\[
\xi_\varepsilon=\varepsilon^2c,\qquad
t_i=\varepsilon^2a_i,
\]
则 (5.5) 成为
\[
\widehat P
 =
 k+
 \frac{(\lambda A+\varepsilon^2\sum_i a_i)^2}
 {\lambda^2A+\varepsilon^4(c^2-\sum_i a_i^2)}
 -A
 =
 k+\frac{2\varepsilon^2}{\lambda}\sum_i a_i+O(\varepsilon^4).
\tag{5.7}
\]
所以该展开及其正号正确。

但 Theorem 1.1 的逐次使用本身只直接产生多参数族；对任意 infinitely-near 配置，不应未经额外一致估计便写成同一个 \(\varepsilon\) 的 (5.7)。一般情形应使用 (5.5) 和极限 (5.6)。这不影响下确界定理。

---

## 6. 负 cscK 度量是 Yamabe 代表

是。设 \(g\) 是紧流形上的常负标量曲率度量。常数试探函数表明其共形类的 Yamabe 常数为负。该共形类中的 Yamabe 极小度量也有常负标量曲率。

将两个常标量曲率度量作常数伸缩，使其标量曲率相同。若
\[
\widetilde g=u^{4/(n-2)}g,
\]
则 \(u>0\) 满足相应 Yamabe 方程。因两端标量曲率相同且为负，最大值原理在 \(u\) 的最大点给出 \(u\le1\)，在最小点给出 \(u\ge1\)，故 \(u\equiv1\)。因此常负标量曲率度量在其共形类中是 Yamabe 极小度量，且仅差常数伸缩。

Arezzo–Pacard 度量在每一步均有负标量曲率，所以可作常数伸缩使
\[
s_{\widehat g}\equiv-4.
\]
该 \(\widehat g\) 仍是 Kähler 度量，并是其共形类的 Yamabe 代表。

---

## 7. \(D_W=0\) 与 \(\Delta V\to0\)

取复定向。任意 Kähler 曲面都有逐点恒等式
\[
|W^+|^2=\frac{s^2}{24}.
\]
在 \(s\equiv-4\) 归一化下，
\[
|W^+|^2=\frac{16}{24}=\frac23.
\]
因此若 Step-50 中
\[
D_W(\widehat g)
 =\int_M\left(\frac23-|W^+|^2\right)d\mu_{\widehat g},
\]
则
\[
\boxed{D_W(\widehat g)=0}
\]
是逐点恒等式，不只是渐近结论。

另一方面，\(s=-4\) 与平均标量曲率公式给出
\[
K_M\cdot\Omega=\frac{\Omega^2}{2\pi}.
\]
于是
\[
\frac{(K_M\cdot\Omega)^2}{\Omega^2}
 =\frac{\Omega^2}{4\pi^2}
 =\frac{\operatorname{Vol}_{\widehat g}(M)}{2\pi^2}.
\]
定义 Step-50 的体积超额
\[
\Delta V(\widehat g)
 :=\operatorname{Vol}_{\widehat g}(M)-2\pi^2A.
\]
由 (2.1)，对这些 cscK Yamabe 度量有精确关系
\[
\boxed{
\widehat P(\widehat g)-k
 =\frac{\Delta V(\widehat g)}{2\pi^2},
\qquad
P(\widehat g)-8\pi^2k=4\Delta V(\widehat g).}
\tag{7.1}
\]
因此每个实际度量满足 \(\Delta V>0\)，而 Arezzo–Pacard 恢复序列满足
\[
\boxed{\Delta V\longrightarrow0.}
\]

---

## 8. Step-50 所需的文字修订

Theorem \(K_\infty\) 的核心结论成立。建议将证明改成以下精确版本：

1. 明确下确界取遍固定吹起复结构 \(J\) 的 Kähler 度量。
2. infinitely-near 情形中的 \(E_i\) 改为每次例外除子的全变换类。
3. canonical model 解消与任意后续吹起分成两步：先用 Theorem 1.3 得到 \(\Omega_\delta\to\lambda K_X\)，再逐次使用 Theorem 1.1。
4. 任意 infinitely-near 配置使用多参数公式 (5.5)；共同 \(\varepsilon\) 展开 (5.7) 只用于确有共同速率的族。
5. 明确写出负 cscK 度量经常数伸缩后是 Yamabe 代表。
6. 将
   \[
   D_W=0,\qquad
   \Delta V=2\pi^2(\widehat P-k)\to0
   \]
   写成由 Kähler Weyl 恒等式和 \(s=-4\) 归一化直接推出的精确等式。