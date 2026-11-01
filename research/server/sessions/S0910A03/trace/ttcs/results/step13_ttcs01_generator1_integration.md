# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 13,
  "task_field": "generator",
  "task_index": 1,
  "type": "Generator",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step13_ttcs01_sub1_generator.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step13_ttcs01_sub2_generator.md"
    }
  ]
}
```

## Exact Task

For a four-dimensional negative Einstein metric Ric = -g with a local free circle action g = q + ell^2 theta^2, define H = Hess_q(ell)/ell. In the chiral variables a_+ = u - z/2 and a_- = u + z/2 where u = d log(ell) and z = *_q(ell F), we have W+ = -[sym nabla a_+ + a_+ otimes a_+]_0 and the electric Weyl E = (1/3)I - H + (|z|^2 I - z otimes z)/4, magnetic Weyl B = (1/2)(sym nabla z + u otimes z + z otimes u - <u,z>I). The trace constraint is tr(H) = 1 + |z|^2/2. The question: if the calibrated W+ spectrum is (-1/6, 1/12, 1/12), and the full curvature average is bounded (fint |Rm|^2 <= K_0), investigate whether H has nonnegative eigenvalues. In the static case (B=0, z=0), calibrated E has eigenvalues (-1/6, 1/12, 1/12), giving H = (1/2, 1/4, 1/4) > 0. For the general twisted case, express H = (1/3)I + Q - E where Q = (|z|^2 I - z otimes z)/4, and E = W+ - B. Determine: (A) Can large B (twist gradient) push an eigenvalue of H below zero while maintaining |W+|^2 = 1/24? (B) Does the L^2 smallness of |B| (from integral calibrated deficit) suffice to control H in L^p for p > 3/2? (C) Explore whether the chiral Riccati structure W+ = -[sym nabla a_+ + a_+ otimes a_+]_0 with |W+|^2 = 1/24 provides a direct estimate relating |B|^2 to |nabla z|^2 + |u|^2|z|^2 that would bound H from below. Seek a precise inequality or a counterexample (an explicit 1-jet model).

## Integrated Scientific Memo

## 结论

采用题中约定
\[
W^+=E+B,\qquad
E=\frac13I-H+Q,\qquad
Q=\frac14\bigl(|z|^2I-z\otimes z\bigr)\succeq0,
\]
因此
\[
\boxed{H=\frac13I-W^++Q+B.}
\]
若
\[
\operatorname{Spec}(W^+)=\left(-\frac16,\frac1{12},\frac1{12}\right),
\]
则
\[
G:=\frac13I-W^+,\qquad
\operatorname{Spec}(G)=\left(\frac12,\frac14,\frac14\right),
\]
从而得到核心算子不等式
\[
\boxed{H=G+Q+B\succeq \frac14I+B.}
\]

所以：

1. **\(Q\) 只会把 \(H\) 向上推；使 \(H\) 出现负特征值的唯一代数机制是 \(B\)。**
2. 校准的 \(W^+\) 谱与有限的平均曲率能量不推出 \(H\succeq0\)。
3. \(B\) 的 \(L^2\)-小性控制 \(H\) 的负谱部分，但不控制整个 \(H\)，因为 \(Q\sim z^2\) 可以任意大并与 \(H\) 在 \(E\) 中抵消。
4. chiral Riccati 方程只控制一个无迹对称组合；在 1-jet 层面不存在由 \(|W^+|\) 或 \(|B|\) 控制
   \(|\nabla z|^2+|u|^2|z|^2\) 的 coercive 不等式。

---

## (A) 显式校准 1-jet：\(B\) 可使 \(H\) 不定

在一点 \(p\) 取 \(q\)-正交标架，并令
\[
u(p)=z(p)=0,\qquad
W^+=\operatorname{diag}\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
对任意 \(L>0\)，取
\[
B_L=\operatorname{diag}\left(\frac L2,-L,\frac L2\right).
\]
由于 \(Q=0\)，
\[
H=\frac13I-W^++B_L
 =\operatorname{diag}\left(
 \frac12+\frac L2,\,
 \frac14-L,\,
 \frac14+\frac L2
 \right).
\]
故只要
\[
\boxed{L>\frac14,}
\]
\(H\) 的第二个特征值即为负，而 \(W^+\) 的校准谱完全不变。

该数据满足一点处的全部约化一阶约束：令
\[
\nabla z=2B_L,\qquad \nabla u=H.
\]
则
\[
dz=0=-2u\wedge z,\qquad
\operatorname{div}z=0=\langle u,z\rangle,
\]
以及
\[
\operatorname{tr}H=1=1+\frac{|z|^2}{2}.
\]
又有
\[
E=\frac13I-H=W^+-B_L,
\]
故 \(E+B_L=W^+\)。

这个模型同时说明代价进入另一手征块：
\[
W^-=E-B_L=W^+-2B_L.
\]
直接计算
\[
|W^-|^2
=6L^2+\frac12L+\frac1{24}.
\]
因此大 \(B\) 必然增加完整曲率能量，但一个仅有上界的平均条件
\(\fint|{\rm Rm}|^2\le K_0\) 并不能排除它；只有足够小的局部 \(W^-\) 或 \(B\) 能量才可能排除。

更一般地，
\[
\lambda_{\min}(H)
\ge\frac14+\lambda_{\min}(B)
\ge \frac14-\sqrt{\frac23}\,|B|_{\mathrm{HS}},
\]
因为三维无迹对称矩阵满足
\(\lambda_{\min}(B)\ge-\sqrt{2/3}|B|_{\mathrm{HS}}\)。所以
\[
|B|_{\mathrm{HS}}\le\frac{\sqrt6}{8}
\quad\Longrightarrow\quad H\succeq0.
\]
这是一个充分条件，而非校准条件本身的推论。

上述构造是**约化方程的 1-jet 反例**，不是一个开集上的精确校准 Einstein 度量；后者还受更高阶 Bianchi/Derdziński 相容条件约束。

---

## (B) \(B\) 的 \(L^2\)-小性只控制 \(H\) 的负谱尾

定义
\[
H_-:=\bigl(-\lambda_{\min}(H)\bigr)_+.
\]
由 \(H\succeq\frac14I+B\)，
\[
H_-\le
\left(|B|_{\rm op}-\frac14\right)_+
\le |B|_{\rm op}
\le \sqrt{\frac23}\,|B|_{\mathrm{HS}}.
\]
因此在归一化有限测度区域上，对所有 \(1\le p\le2\)，
\[
\boxed{
\|H_-\|_{L^p_{\rm av}}
\le \sqrt{\frac23}\,\|B\|_{L^p_{\rm av}}
\le \sqrt{\frac23}\,\|B\|_{L^2_{\rm av}}.
}
\]
特别地，这包括所问的任意
\[
\frac32<p\le2.
\]
并且由较粗但方便的阈值估计
\[
\{H_- >0\}\subseteq
\{|B|_{\rm op}>1/4\},
\]
可得
\[
\mu_{\rm av}\{H\not\succeq0\}
\le16\,\|B\|_{L^2_{\rm av}}^2.
\]

但必须区分：

- 若只知道 \(\|B\|_{L^2}\) **有界**，则只得到 \(H_-\) 有界；
- 若 \(\|B\|_{L^2}\to0\)，才得到负谱尾在 \(L^p\)、测度意义下趋零；
- 这些都不推出整个 \(H\) 的 \(L^p\) 控制。

完整曲率平均给出的也是有界性而非小性。由于
\[
B=\frac12(W^+-W^-),
\]
有
\[
|B|^2\le\frac12\bigl(|W^+|^2+|W^-|^2\bigr).
\]
在采用
\[
|{\rm Rm}|^2=|W^+|^2+|W^-|^2+\frac83
\]
的范数约定时，校准区域上
\[
\fint |B|^2
\le \frac12\left(K_0-\frac83\right).
\]
该常数依赖曲率张量范数约定；不依赖约定的内容是：完整曲率 \(L^2\) 上界给出 \(B\) 的 \(L^2\) 上界，但并不自动给出小性或非集中性。

### 为什么不能控制整个 \(H\)

取
\[
B=0,\qquad
u=Ne^1,\qquad z=Ne^1,
\]
并保持同一个校准 \(W^+\)。此时
\[
Q=\operatorname{diag}
\left(0,\frac{N^2}{4},\frac{N^2}{4}\right),
\]
且令
\[
H=\frac13I-W^++Q
=\operatorname{diag}\left(
\frac12,\frac14+\frac{N^2}{4},
\frac14+\frac{N^2}{4}
\right).
\]
于是
\[
|H|\asymp N^2,
\qquad
E=\frac13I-H+Q=W^+,
\qquad
W^-=W^+.
\]
取
\[
\nabla z
=\langle u,z\rangle I-2u\otimes z
=\operatorname{diag}(-N^2,N^2,N^2),
\]
和
\[
\nabla u=H-u\otimes u,
\]
则
\[
dz=-2u\wedge z=0,\qquad
\operatorname{div}z=\langle u,z\rangle=N^2,
\qquad B=0.
\]
所以即使 \(B\equiv0\)，\(H\)、\(|z|^2\) 和 \(|\nabla z|\) 仍可在 1-jet 层面任意大。

故问题 (B) 的精确答案是：

\[
\boxed{\text{\(L^2\)-小的 \(B\) 控制 \(H\) 的负部于所有 \(3/2<p\le2\)，但不控制整个 \(H\)。}}
\]

---

## (C) chiral Riccati 结构产生的是抵消恒等式，而非 coercivity

为避免“\(\operatorname{sym}\)”是否含 \(1/2\) 的歧义，直接写分量：
\[
B_{ij}
=\frac14(\nabla_i z_j+\nabla_j z_i)
+\frac12(u_i z_j+u_j z_i-\langle u,z\rangle\delta_{ij}).
\]
结合
\[
dz=-2u\wedge z,\qquad
\operatorname{div}z=\langle u,z\rangle,
\]
可恢复完整导数：
\[
\boxed{
\nabla_i z_j
=2B_{ij}
+\langle u,z\rangle\delta_{ij}
-2u_i z_j.
}
\]
即
\[
\boxed{
4|B|^2=
\left|\nabla z+2u\otimes z-\langle u,z\rangle I\right|^2.
}
\]
展开得
\[
\boxed{
|\nabla z|^2
=
4|B|^2+4|u|^2|z|^2-\langle u,z\rangle^2
-8B(u,z).
}
\]

这不是
\[
|\nabla z|^2+|u|^2|z|^2\lesssim1+|B|^2
\]
型估计，因为右侧组合允许精确抵消。上面的
\(B=0,\ u=z=Ne^1\) 模型给出
\[
|\nabla z|^2=3N^4,\qquad
|u|^2|z|^2=N^4,
\]
所以
\[
|\nabla z|^2+|u|^2|z|^2=4N^4,
\qquad B=0,\qquad |W^+|^2=\frac1{24}.
\]
因此不存在仅由校准 \(W^+\) 与 \(B\) 控制这些量的普适点态不等式。

其结构原因是
\[
W^+=-\bigl[\operatorname{sym}\nabla a_+
+a_+\otimes a_+\bigr]_0,\qquad
a_+=u-\frac z2,
\]
只控制一个**无迹对称 Riccati 张量**。它不控制 trace mode
\[
\operatorname{tr}
\bigl(\operatorname{sym}\nabla a_+
+a_+\otimes a_+\bigr)
=
1+\frac34|z|^2-\frac32\langle u,z\rangle,
\]
也不分别控制 \(u,z\)。大 \(u\) 与 \(z\) 可以在 \(a_+\) 或 \(B\) 中抵消，同时保留于另一手征变量 \(a_-=u+z/2\)。

---

## 可严格保留的最终判断

\[
\boxed{
H\succeq\frac14I+B
}
\]
是校准条件下最有用的点态结论。

- **(A)** 是：显式 1-jet 表明大负向 \(B\) 可使 \(H\) 出现负特征值，同时 \(W^+\) 完全校准。
- **(B)** 若 \(B\) 在 \(L^2\) 中真正小，则 \(H\) 的负谱尾在所有 \(3/2<p\le2\) 中小；但仅有 \(\fint|{\rm Rm}|^2\le K_0\) 通常只给有界性，而且不控制整个 \(H\)。
- **(C)** chiral Riccati 公式不提供所寻求的点态 coercivity；显式 \(B=0\) 1-jet 已否定它。

一个可能的更高阶方向是利用 Einstein 条件的
\(\delta W^\pm=0\) 推导加权 quotient 上的完整 div–curl/Bochner 系统。但不能未经计算便断言分别有简单的
\(\delta_qE=\delta_qB=0\)：垂直场 \(V\) 非平行，四维散度分解会产生 \(u,z,E,B\) 的代数耦合项。真正尚未解决的对象是：这些耦合的 Bianchi 方程能否给出加权 Caccioppoli 或逆 Hölder 估计，从而阻止 \(B\)-能量集中；现有材料尚未建立这一点。