# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 3,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step3_ttcs01_sub5_verifier.md"
    },
    {
      "branch": 2,
      "status": "unavailable",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step3_ttcs01_sub6_verifier.md"
    }
  ]
}
```

## Exact Task

Check the mathematical correction and boundary analysis: (1) explain precisely why Step 2's independent derivation of ∫|W+|²≥(4π²/3)(a+)² is invalid, while published Ishida–LeBrun Proposition 4 remains usable; (2) recompute from scratch, with exact constants, what ||Ric+g||_op≤δ implies on an Ishida–LeBrun Theorem 7 boundary family where T=(2χ+3τ)(M)=2A/3; (3) determine whether any known exact L2 Ricci-infimum result in the supplied connected-sum paper already yields a uniform pointwise pinching gap or instead shows a degenerating sharp sequence. Explicitly catch normalization/volume mistakes and state what remains open.

## Integrated Scientific Memo

# 核验结论

## 1. Step 2 的纯 \(W_+\) 下界推导错误，但已发表的 Proposition 4 可继续使用

对自对偶二形式 \(\varphi\)，Weitzenböck 公式积分后为
\[
\int_M\bigl(|d\varphi|^2+|d^*\varphi|^2\bigr)
=
\int_M\left(
|\nabla\varphi|^2-2W_+(\varphi,\varphi)+\frac{s}{3}|\varphi|^2
\right).
\]
故只能推出
\[
\int_M(-W_+)(\varphi,\varphi)
\ge
-\frac16\int_M s|\varphi|^2
-\frac12\int_M|\nabla\varphi|^2.
\]
在 \(s<0\) 为常数时，
\[
\int_M(-W_+)(\varphi,\varphi)
\ge
\frac{|s|}{6}\int_M|\varphi|^2
-\frac12\int_M|\nabla\varphi|^2.
\]
Step 2 删除了最后一项，但该项符号是负的，不能删除以增强下界。因此不能得到
\[
\int(-W_+)(F_A^+,F_A^+)
\ge \frac{|s|}{6}\int|F_A^+|^2,
\]
也不能据此推出
\[
\boxed{\int|W_+|^2\ge \frac{4\pi^2}{3}(a^+)^2}.
\]
一般而言 \(F_A^+\) 并不调和；即使调和，上式中的
\(-\frac12\int|\nabla F_A^+|^2\) 仍不会消失。LeBrun 1998 正是通过估计该梯度项而引入
\[
\beta=\frac{\int s^2}{32\pi^2(a^+)^2}.
\]

还有一个适用范围错误：
\[
|F_A^+|^2=\frac18|\Phi|^4\le \frac{s^2}{8}
\]
是在换到常负标量曲率的 Yamabe 代表后由极大值原理得到的；它不是任意变标量曲率度量上的逐点结论。1998 论文中存在具有非平凡 SW 数据的反自对偶度量；当 \(a^+\neq0\) 时，任何上述正的纯 \(W_+\) 下界都将与 \(W_+\equiv0\) 直接矛盾。

### Proposition 4 的正确依据

Ishida–LeBrun 已发表的混合估计仍然成立：
\[
\frac1{4\pi^2}\int_M
\left(\frac{s^2}{24}+2|W_+|^2\right)d\mu
\ge \frac23(a^+)^2.
\]
其引用的 [17] 是 LeBrun 2001 的工作，不是供应材料中的 1998 年 \(32/57\) 估计。

供应的 2003 connected-sum 论文给出了可直接验证它的更原始估计
\[
K:=\int_M(s-\sqrt6\,|W_+|)^2d\mu
\ge72\pi^2(a^+)^2.
\]
令
\[
L:=\int_M\left(\frac{s^2}{24}+2|W_+|^2\right)d\mu.
\]
逐点展开得到
\[
27L-K
=\frac18\int_M(s+8\sqrt6\,|W_+|)^2d\mu\ge0.
\]
于是
\[
L\ge\frac{K}{27}
\ge\frac{8\pi^2}{3}(a^+)^2,
\]
恰好等价于 Proposition 4。它是混合曲率估计，不蕴含独立的纯 \(W_+\) 下界。

---

## 2. Theorem 7 临界族上的精确重新计算

统一记
\[
A=\sum_{j=1}^m c_1^2(X_j),\qquad
\Delta=k+4(m-1),\qquad m=2,3.
\]
即
\[
\Delta=
\begin{cases}
k+4,&m=2,\\
k+8,&m=3,
\end{cases}
\qquad
T:=(2\chi+3\tau)(M)=A-\Delta.
\]
Theorem 7 的边界等号是
\[
\Delta=\frac A3,\qquad T=\frac{2A}{3}.
\]
因此此处正确的无量纲参数是 \(\Delta/A\)，不是 \(k/A\)。先前针对单个 blow-up 族 \(k/A=25/57\) 得到的
\(1/(1+\sqrt{19})\) 不能移植到该边界族。

设
\[
E=\operatorname{Ric}_g+g,\qquad \|E\|_{\mathrm{op}}\le\delta<1.
\]
在一点把 \(E\) 对角化，特征值 \(e_i\in[-\delta,\delta]\)。则
\[
s=-4+\sum_{i=1}^4e_i,
\qquad
-4(1+\delta)\le s\le-4(1-\delta),
\]
且
\[
\mathring{\operatorname{Ric}}=E^\circ,\qquad
|E^\circ|^2
=\sum_{i=1}^4(e_i-\bar e)^2\le4\delta^2.
\]
这个 \(4\delta^2\) 是精确的盒约束上界。

记
\[
S=\int_M\frac{s^2}{24}\,d\mu,\qquad
R=\frac12\int_M|\mathring{\operatorname{Ric}}|^2\,d\mu,\qquad
W=\int_M|W_+|^2\,d\mu.
\]
逐点有
\[
\frac{|\mathring{\operatorname{Ric}}|^2/2}{s^2/24}
\le q_\delta,\qquad
q_\delta:=\frac{3\delta^2}{(1-\delta)^2},
\]
所以
\[
R\le q_\delta S.
\]
Chern–Gauss–Bonnet–signature 公式为
\[
4\pi^2T=2W+S-R.
\]

LeBrun 符号选择给出某个 monopole class 满足
\[
(a^+)^2\ge A.
\]
Proposition 4 因而给出
\[
2W+S\ge\frac{8\pi^2}{3}A.
\]
由此，对一般 \(\Delta\)，
\[
R=(2W+S)-4\pi^2(A-\Delta)
\ge4\pi^2\left(\Delta-\frac A3\right).
\]
若
\[
q_\delta<1
\iff
\delta<\frac1{1+\sqrt3},
\]
则由 \(W\ge0\) 及 \(R\le q_\delta S\) 得
\[
S\le\frac{4\pi^2(A-\Delta)}{1-q_\delta}.
\]
合并可得精确条件
\[
\boxed{
\frac{\Delta}{A}
\le
\frac13+\frac{2\delta^2}{(1-\delta)^2}
}.
\]

### 临界边界 \(\Delta=A/3\)

代入后，上式仅成为恒真式；它不给出任何正的、与 \(A\) 无关的 \(\delta\) 下界。此时
\[
4\pi^2T=\frac{8\pi^2A}{3},
\]
而混合估计仅给出 \(R\ge0\)。

由于 Theorem 7 选取的 monopole class 满足
\[
a^2=
\begin{cases}
T+4,&m=2,\\
T+8,&m=3,
\end{cases}
\]
它不可能是辛结构的第一 Chern 类；Proposition 4 的严格性因此给出
\[
R>0.
\]
但这是无定量的严格性，不能推出统一 pinching gap。

令
\[
\eta_\delta=(1-\delta)^2-3\delta^2
=1-2\delta-2\delta^2>0.
\]
边界族上可得
\[
0<R\le\frac{8\pi^2A\,\delta^2}{\eta_\delta},
\]
以及必须保留体积因子的估计
\[
\frac{2\pi^2A}{(1+\delta)^2}
\le \operatorname{Vol}(M,g)
\le \frac{4\pi^2A}{\eta_\delta}.
\]
左界来自
\(\int s^2\ge32\pi^2A\) 与 \(s^2\le16(1+\delta)^2\)；右界来自上述 CGB 和点态估计。故体积自然是 \(A\) 的量级，绝不能未经论证设为 \(1\)。

### 若存在 \(\delta_j\to0\) 的序列

由
\[
27L-K=\frac18\int(s+8\sqrt6|W_+|)^2,\qquad
K\ge72\pi^2A,
\]
以及 \(L=8\pi^2A/3+R\)，有
\[
\int_M(s+8\sqrt6|W_+|)^2d\mu
\le216R
\le\frac{1728\pi^2A\,\delta^2}{\eta_\delta}.
\]
因此任何这样的序列都必须满足
\[
\frac{\operatorname{Vol}(M,g_j)}{\pi^2A}\to\frac{32}{9},
\qquad
\frac1{\pi^2A}\int s^2d\mu\to\frac{512}{9},
\]
\[
\frac1{\pi^2A}\int|W_+|^2d\mu\to\frac4{27},
\qquad
\frac1{\pi^2A}\int|\mathring{\operatorname{Ric}}|^2d\mu\to0,
\]
以及
\[
\frac1{\pi^2A}\int|\operatorname{Ric}|^2d\mu\to\frac{128}{9}.
\]
这些是必要渐近条件，不是存在性结论。

---

## 3. 精确 \(L^2\) Ricci 下确界不产生点态 pinching gap

在 2003 connected-sum 论文 Theorem C 的额外假设成立且
\(N=k\overline{\mathbb{CP}}^{\,2}\) 时，Corollary 16 给出
\[
\mathcal I_r(M)
=\inf_g\int_M|\operatorname{Ric}_g|^2d\mu_g
=8\pi^2(A+\Delta).
\]
同时 Theorem B 给出
\[
\mathcal I_s(M)
=\inf_g\int_Ms_g^2d\mu_g
=32\pi^2A.
\]
在临界值 \(\Delta=A/3\)：
\[
\boxed{\mathcal I_r(M)=\frac{32\pi^2A}{3}},
\qquad
\boxed{\mathcal I_s(M)=32\pi^2A}.
\]
这些等式只覆盖满足论文中复曲面、同余条件及 \(N\) 几何条件的子族；不能自动推广到 Theorem 7 的任意辛成分。

它们不蕴含统一点态间隙，原因有二：

1. 不能写
   \[
   \inf_g\int|\mathring{\operatorname{Ric}}|^2
   =
   \mathcal I_r-\frac14\mathcal I_s.
   \]
   两个下确界一般可能由不同度量序列实现。

2. 四维中 \(\int|\operatorname{Ric}|^2\) 对整体缩放不变，而
   \(\|\operatorname{Ric}+g\|_{\mathrm{op}}\) 固定了尺度 \(\operatorname{Ric}\approx-g\)，并不缩放不变。把体积擅自归一化为 \(1\)，或从
   \[
   |\operatorname{Ric}+g|^2\le4\delta^2
   \]
   积分后省略 \(\operatorname{Vol}(g)\)，都会制造假的 \(\delta\) 下界。

论文证明 sharpness 所用的序列是退化粘合序列。沿该序列，
\[
\int s^2d\mu\to32\pi^2A,\qquad
\int|\operatorname{Ric}|^2d\mu\to8\pi^2(A+\Delta),
\]
从而在同一序列上
\[
\int|\mathring{\operatorname{Ric}}|^2d\mu
\to8\pi^2\Delta.
\]
边界时该极限为
\[
\frac{8\pi^2A}{3}.
\]
固定的无迹 Ricci 能量集中到体积收缩的颈区，因此该 sharp 序列不是
\(\|\operatorname{Ric}+g\|_{\mathrm{op}}\to0\) 的序列；相反，它表现出曲率集中和几何退化。

这也不排除另一类点态近 Einstein 序列：若后者存在，其 Ricci 能量趋于
\[
\frac{128\pi^2A}{9},
\]
而非下确界
\[
\frac{32\pi^2A}{3}=\frac{96\pi^2A}{9}.
\]

## 尚未解决的问题

对每个 Theorem 7 临界流形，
\[
\varepsilon(M):=
\inf_g\|\operatorname{Ric}_g+g\|_{\mathrm{op},\infty}
\]
是否严格为正，供应文献没有决定。它们排除了实际 Einstein 度量，却既没有证明统一或逐流形的正 gap，也没有构造 \(\varepsilon(M)=0\) 的点态近 Einstein 序列。

缺失的核心结果是 Proposition 4 近等号情形的定量稳定性/紧致性定理，或某种能把拓扑和 \(L^2\) 信息提升为
\(\|\mathring{\operatorname{Ric}}\|_\infty\) 控制的估计。