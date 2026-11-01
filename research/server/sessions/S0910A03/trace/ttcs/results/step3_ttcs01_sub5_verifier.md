# TTCS Independent Branch Record

```json
{
  "step_id": 3,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Knowledge/objects/papers/Spin-Manifolds-Einstein-Metrics-and-Differential-Topology--c5d29fae197e--75ec82ead070/object.md",
    "Knowledge/objects/papers/Weyl-Curvature-Einstein-Metrics-and-Seiberg-Witten-Theory--010d90d7328e--6fed64eff4e5/object.md",
    "Knowledge/objects/papers/Curvature-Connected-Sums-and-Seiberg-Witten-Theory--7e92a6723434--2ac6d11897c5/object.md",
    "Sessions/S0910A03/workspace/notes/step2_corrected_prop4_analysis.tex",
    "Sessions/S0910A03/workspace/scripts/corrected_prop4_analysis.py"
  ]
}
```

## Task

Check the mathematical correction and boundary analysis: (1) explain precisely why Step 2's independent derivation of ∫|W+|²≥(4π²/3)(a+)² is invalid, while published Ishida–LeBrun Proposition 4 remains usable; (2) recompute from scratch, with exact constants, what ||Ric+g||_op≤δ implies on an Ishida–LeBrun Theorem 7 boundary family where T=(2χ+3τ)(M)=2A/3; (3) determine whether any known exact L2 Ricci-infimum result in the supplied connected-sum paper already yields a uniform pointwise pinching gap or instead shows a degenerating sharp sequence. Explicitly catch normalization/volume mistakes and state what remains open.

## Output

# 数学核验备忘录

## 1. Step 2 中纯 \(W_+\) 下界的推导无效；已发表的混合曲率估计仍成立

令 \(\varphi\) 为自对偶二形式。正确的 Weitzenböck 恒等式积分形式是
\[
\int_M\bigl(|d\varphi|^2+|d^*\varphi|^2\bigr)
=
\int_M\left(
|\nabla\varphi|^2-2W_+(\varphi,\varphi)+\frac{s}{3}|\varphi|^2
\right).
\]
由于左端非负，只能推出
\[
\int_M(-W_+)(\varphi,\varphi)
\ge
-\frac16\int_Ms|\varphi|^2
-\frac12\int_M|\nabla\varphi|^2.
\]
当 \(s<0\) 为常数时，这成为
\[
\int_M(-W_+)(\varphi,\varphi)
\ge
\frac{|s|}{6}\int_M|\varphi|^2
-\frac12\int_M|\nabla\varphi|^2.
\]
Step 2 丢掉了最后一项，但它带的是负号。因而
\[
\int(-W_+)(F_A^+,F_A^+)
\ge \frac{|s|}{6}\int|F_A^+|^2
\]
并不能由该公式得到。事实上 \(F_A^+\) 一般也不是调和形式；即使它恰好调和，\(-\frac12\int|\nabla F_A^+|^2\) 仍然存在。

另外，
\[
|F_A^+|^2=\frac18|\Phi|^4\le \frac{s^2}{8}
\]
只是在换到常负标量曲率的 Yamabe 代表并使用极大值原理后成立。对一般变标量曲率度量，通常得到的是
\[
\|\Phi\|_\infty^2\le \max(0,-\min_M s),
\]
而不是逐点的 \(|\Phi(x)|^2\le |s(x)|\)。

这也说明为什么 LeBrun 1998 的证明必须估计 \(\nabla F_A^+\)，并由此引入
\[
\beta=\frac{\int s^2}{32\pi^2(a^+)^2};
\]
纯粹的
\[
\int|W_+|^2\ge \frac{4\pi^2}{3}(a^+)^2
\]
并不存在。供应的 1998 文献还讨论了 \(W_+\equiv0\) 且具有非平凡 Seiberg–Witten 数据的反自对偶度量；若 \(a^+\ne0\)，上述纯 \(W_+\) 下界会立即与这些例子矛盾。

### 已发表估计的正确来源与推导

Ishida–LeBrun 的《Spin Manifolds, Einstein Metrics, and Differential Topology》命题 4 给出
\[
\frac1{4\pi^2}\int_M\left(\frac{s^2}{24}+2|W_+|^2\right)d\mu
\ge \frac23(a^+)^2.
\]
该文献中的参考文献 [17] 是 LeBrun 2001 年的 *Ricci curvature, minimal volumes, and Seiberg–Witten theory*，不是 1998 年系数 \(32/57\) 的论文。

供应的 2003 年 connected-sum 论文还给出更原始的形式
\[
K(g):=\int_M\left(s-\sqrt6\,|W_+|\right)^2d\mu
\ge72\pi^2(a^+)^2.
\]
令
\[
L(g):=\int_M\left(\frac{s^2}{24}+2|W_+|^2\right)d\mu.
\]
逐点代数恒等式为
\[
27L-K
=
\frac18\int_M\left(s+8\sqrt6\,|W_+|\right)^2d\mu\ge0.
\]
因此
\[
L\ge\frac{K}{27}
\ge\frac{8\pi^2}{3}(a^+)^2,
\]
恰好等价于系数 \(2/3\) 的命题。这个推导不产生任何纯 \(W_+\) 下界。

---

## 2. Ishida–LeBrun Theorem 7 临界等号族的精确计算

统一写成
\[
A=\sum_{j=1}^m c_1^2(X_j),\qquad
\Delta=k+4(m-1),\qquad m=2\ \text{或}\ 3.
\]
于是

- \(m=2\) 时，\(\Delta=k+4\)；
- \(m=3\) 时，\(\Delta=k+8\)；

并且
\[
T:=(2\chi+3\tau)(M)=A-\Delta.
\]
Theorem 7 的等号情形是
\[
\Delta=\frac A3,\qquad T=\frac{2A}{3}.
\]

这说明 Step 2 中的 \(k/A\) 不能直接用于该族。正确变量是
\[
\frac{\Delta}{A}
=
\frac{k+4}{A}
\quad\text{或}\quad
\frac{k+8}{A}.
\]
系数 \(1/(1+\sqrt{19})\) 属于 \(m=1\)、\(T=A-k\)、\(k/A=25/57\) 的另一族，不能移植到这里。

### 2.1 点态 Ricci 夹逼的精确 \(L^2\) 后果

设
\[
E=\operatorname{Ric}_g+g,\qquad \|E\|_{\mathrm{op}}\le\delta<1.
\]
在每一点将 \(E\) 对角化，特征值记作 \(e_i\in[-\delta,\delta]\)。则
\[
s=-4+\sum_{i=1}^4e_i,
\qquad
-4(1+\delta)\le s\le-4(1-\delta).
\]
而
\[
\mathring{\operatorname{Ric}}=E^\circ,
\qquad
|E^\circ|^2
=\sum_{i=1}^4(e_i-\bar e)^2
\le4\delta^2.
\]
定义
\[
\mathsf S=\int_M\frac{s^2}{24}\,d\mu,\qquad
\mathsf R=\frac12\int_M|\mathring{\operatorname{Ric}}|^2\,d\mu,\qquad
\mathsf W=\int_M|W_+|^2\,d\mu.
\]
于是逐点得到
\[
\frac{|\mathring{\operatorname{Ric}}|^2/2}{s^2/24}
\le
q_\delta,
\qquad
q_\delta:=\frac{3\delta^2}{(1-\delta)^2},
\]
从而
\[
\mathsf R\le q_\delta\mathsf S.
\]
Gauss–Bonnet–signature 恒等式为
\[
4\pi^2T=2\mathsf W+\mathsf S-\mathsf R.
\]

LeBrun 符号选择给出某个 monopole class 满足
\[
(a^+)^2\ge A.
\]
所以
\[
2\mathsf W+\mathsf S\ge\frac{8\pi^2}{3}A.
\]
一般 \(\Delta\) 下，
\[
\mathsf R
=(2\mathsf W+\mathsf S)-4\pi^2(A-\Delta)
\ge4\pi^2\left(\Delta-\frac A3\right).
\]
若 \(q_\delta<1\)，即
\[
\delta<\frac1{1+\sqrt3},
\]
还可由 \(\mathsf W\ge0\) 得到
\[
\mathsf S\le \frac{4\pi^2(A-\Delta)}{1-q_\delta}.
\]
合并后得到
\[
\boxed{\frac{\Delta}{A}
\le
\frac13+\frac{2\delta^2}{(1-\delta)^2}}.
\]
代入临界值 \(\Delta/A=1/3\) 后，这个不等式只变成恒真式，不能给出与 \(A\) 无关的正数下界。

### 2.2 临界等号族上真正得到的估计

在 \(\Delta=A/3\) 时，
\[
\frac{8\pi^2}{3}A=4\pi^2T.
\]
因此混合曲率估计与 Chern–Gauss–Bonnet 只给出
\[
\mathsf R\ge0.
\]
这里实际上有严格性：Theorem 7 中所选 monopole class 满足

- \(m=2\) 时 \(a^2=T+4\)；
- \(m=3\) 时 \(a^2=T+8\)。

辛结构的第一 Chern 类平方必须等于 \(T\)，所以这个 \(a\) 不能是相应的辛第一 Chern 类。已发表命题因而给出
\[
\mathsf R>0.
\]
但严格性没有给出数值大小。

若
\[
\eta_\delta:=(1-\delta)^2-3\delta^2
=1-2\delta-2\delta^2>0,
\]
则
\[
0<\mathsf R
\le
\frac{8\pi^2A\,\delta^2}{\eta_\delta},
\]
以及
\[
\operatorname{Vol}(M,g)
\le
\frac{4\pi^2A}{\eta_\delta}.
\]
标量曲率的 Seiberg–Witten 估计
\[
\int s^2d\mu\ge32\pi^2A
\]
与 \(s^2\le16(1+\delta)^2\) 还给出
\[
\operatorname{Vol}(M,g)
\ge
\frac{2\pi^2A}{(1+\delta)^2}.
\]
所以小 \(\delta\) 度量若存在，其体积自然是 \(A\) 的量级，不能任意设成 1。

### 2.3 假设存在 \(\delta_j\to0\) 序列时的强制渐近量

平方形式估计还给出更精确的信息。由
\[
K\ge72\pi^2A=27\cdot\frac{8\pi^2A}{3},
\qquad
L=\frac{8\pi^2A}{3}+\mathsf R,
\]
以及 \(27L-K=\frac18\int(s+8\sqrt6|W_+|)^2\)，可得
\[
\int_M\left(s+8\sqrt6|W_+|\right)^2d\mu
\le216\mathsf R
\le
\frac{1728\pi^2A\,\delta^2}{\eta_\delta}.
\]
因此若临界等号族中存在 \(\delta_j\to0\) 的度量序列，则必有
\[
\frac1{\pi^2A}\int s^2d\mu\longrightarrow\frac{512}{9},
\]
\[
\frac1{\pi^2A}\int|W_+|^2d\mu\longrightarrow\frac4{27},
\]
\[
\frac{\operatorname{Vol}(M,g_j)}{\pi^2A}
\longrightarrow\frac{32}{9},
\]
\[
\frac1{\pi^2A}\int|\mathring{\operatorname{Ric}}|^2d\mu\longrightarrow0,
\]
以及
\[
\frac1{\pi^2A}\int|\operatorname{Ric}|^2d\mu
\longrightarrow\frac{128}{9}.
\]
这些是潜在点态近 Einstein 序列必须满足的归一化数据；现有严格曲率估计并未排除它们。

---

## 3. connected-sum 论文中的精确 \(\mathcal I_r\) 结果

在 Theorem C 的附加假设成立、且
\[
N=k\overline{\mathbb{CP}}^{\,2}
\]
时，Corollary 16 给出
\[
\mathcal I_r(M)
=
\inf_g\int_M|\operatorname{Ric}_g|^2d\mu_g
=
8\pi^2(A+\Delta).
\]
Theorem B 同时给出
\[
\mathcal I_s(M)
=
\inf_g\int_Ms_g^2d\mu_g
=
32\pi^2A.
\]
临界值 \(\Delta=A/3\) 下，
\[
\boxed{\mathcal I_r(M)=\frac{32\pi^2A}{3}},
\qquad
\boxed{\mathcal I_s(M)=32\pi^2A}.
\]

这些公式只适用于满足该论文中复曲面、\(b_1\)、\(b_+\) 同余和 \(N\) 几何假设的子族，并非 Theorem 7 的任意辛成分都自动满足。

### 3.1 它没有产生点态夹逼间隙

\(\mathcal I_r\) 是完整 Ricci 张量的 \(L^2\) 下确界，不是
\[
\inf_g\int|\mathring{\operatorname{Ric}}|^2.
\]
不能写成
\[
\inf\int|\mathring{\operatorname{Ric}}|^2
=
\mathcal I_r-\frac14\mathcal I_s;
\]
两个下确界一般由不同序列逼近。

此外，\(\int|\operatorname{Ric}|^2\) 在四维中具有尺度不变性，而
\[
\|\operatorname{Ric}+g\|_{\mathrm{op}}
\]
固定了 Einstein 常数为 \(-1\)，不具有这种尺度不变性。把度量改成 \(cg\) 会改变 Ricci 相对于新度量的特征值，因此不能先将体积设为 1 再使用点态估计。若错误地省略体积因子，就会虚构出一个正的 \(\delta\) 下界。

### 3.2 论文实际构造的是退化的下确界逼近序列

Theorem C 的证明把各个复曲面的 Kähler–Einstein orbifold 部分与缩放后的标量平坦反自对偶部分粘合。对该序列，
\[
\int s^2d\mu\longrightarrow32\pi^2A,
\]
\[
\int|\operatorname{Ric}|^2d\mu
\longrightarrow8\pi^2(A+\Delta),
\]
所以同一序列上
\[
\int|\mathring{\operatorname{Ric}}|^2d\mu
\longrightarrow8\pi^2\Delta.
\]
临界值下即
\[
\int|\mathring{\operatorname{Ric}}|^2d\mu
\longrightarrow\frac{8\pi^2A}{3}.
\]
若把 Kähler–Einstein 主体归一化为 \(\operatorname{Ric}=-g\)，主体体积趋于 \(2\pi^2A\)，而固定的无迹 Ricci 能量聚集在体积收缩的颈部。因此该序列没有给出
\[
\|\operatorname{Ric}+g\|_{\mathrm{op}}\to0;
\]
相反，颈部的点态曲率会集中。

值得注意的是，潜在点态近 Einstein 序列若存在，其完整 Ricci 能量必须趋于
\[
\frac{128\pi^2A}{9},
\]
而 \(\mathcal I_r\) 的下确界是
\[
\frac{32\pi^2A}{3}
=\frac{96\pi^2A}{9}.
\]
所以这种序列不会逼近 \(\mathcal I_r\) 的下确界，两者并不矛盾。

---

## 4. 尚未解决的数学内容

对临界等号族定义
\[
\varepsilon(M)
=
\inf_g\|\operatorname{Ric}_g+g\|_{\mathrm{op},\infty}.
\]
供应文献证明不存在 \(\varepsilon=0\) 的单个 Einstein 度量，但没有证明
\[
\varepsilon(M)>0,
\]
也没有构造使该量趋于零的度量序列。精确 \(L^2\) 下确界结果同样没有决定这个问题。

现有公式允许 Ricci 两侧有界、体积在 \(A\) 的量级内，同时直径或注入半径仍可退化。真正缺少的数学内容是 LeBrun 平方估计近等号时的几何紧致性或稳定性定理，或者一个直接控制
\(\|\mathring{\operatorname{Ric}}\|_\infty\) 的拓扑—几何估计。