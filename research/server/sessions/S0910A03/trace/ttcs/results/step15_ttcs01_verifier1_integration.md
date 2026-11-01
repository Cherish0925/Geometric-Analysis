# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 15,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step15_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step15_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following proposed L² completion-square chain for the Yau Problem 26 negative-branch program on a fixed critical Ishida-LeBrun 4-manifold M.

CHAIN CLAIM: For ANY Riemannian metric g on M (not just the original near-Einstein sequence), the following hold:
(a) Chern-Gauss-Bonnet: I - R = 2A/3 where I = (4pi²)⁻¹∫(s²/24 + 2|W⁺|²), R = (8pi²)⁻¹∫|Ric₀|².
(b) Seiberg-Witten monopole: K ≥ A where K = (72pi²)⁻¹∫(s - √6|W⁺|)².
(c) Completion square: ∫(s + 8√6|W⁺|)² ≤ 864pi²R ≤ 108∫|E|² where E = Ric + g.
(d) Consequence: ∫(|W⁺| - 1/(2√6))² ≤ C∫|E|² with C ≈ 0.41.

VERIFY EACH STEP. In particular:
1. Is (b) really metric-independent? The SW inequality involves metric data; check that the final bound K ≥ A uses only topological invariants after minimizing over metrics.
2. Does the chain from R → calibrated Weyl profile require volume control as an additional input? Or is the bound (d) truly volume-independent?
3. The CRITICAL QUESTION: After applying a normalized cutoff flow ∂_t g = -2χ²(Ric+g), the evolved metric g(t) is still on M. Does the chain apply to g(t) without additional hypotheses? What if the flow develops singularities or degeneracies?
4. For the forbidden-germ contradiction (Step 6), we need not just |W⁺| ≈ 1/(2√6) but the specific eigenvalue structure (-1/6, 1/12, 1/12). Does the L² Weyl modulus convergence suffice to extract eigenvalue information, or is additional compactness needed? What is the MINIMAL additional input beyond ∫|E|² → 0 to reach the contradiction?

## Integrated Scientific Memo

# L² 配方链核验结论

固定定向的临界 Ishida–LeBrun 四流形 \(M\)，满足
\[
2\chi(M)+3\tau(M)=\frac{2A}{3},
\]
并假设所用全部 Bauer–Furuta 符号类确为 monopole classes。对 \(M\) 上任意光滑 Riemann 度量 \(g\)，令
\[
I=\frac1{4\pi^2}\int_M\left(\frac{s^2}{24}+2|W^+|^2\right)d\mu,\quad
R=\frac1{8\pi^2}\int_M|\Ric^\circ|^2d\mu,
\]
\[
K=\frac1{72\pi^2}\int_M(s-\sqrt6|W^+|)^2d\mu,\qquad
E=\Ric+g.
\]

结论是：

- (a)、(b)、(c) 均正确；
- (d) 正确且无需体积控制，常数还可从约 \(0.4123\) 改进为 \(7/24\)；
- 该静态链适用于截断流产生的每个光滑正定时刻，但完全不保证流存在或 \(L^2\) 缺陷沿流保持小；
- \(|W^+|\) 的 \(L^2\) 收敛不能确定 Weyl 特征值结构；Step 6 还需要局部非消失的 monopole/harmonic 自对偶形式所携带的最低特征线饱和，以及局部光滑紧性。

## 1. Chern–Gauss–Bonnet：正确且逐度量成立

四维公式为
\[
2\chi+3\tau
=\frac1{4\pi^2}\int_M
\left(\frac{s^2}{24}+2|W^+|^2-\frac12|\Ric^\circ|^2\right)d\mu.
\]
因此
\[
I-R=2\chi+3\tau=\frac{2A}{3}.
\]
这是纯拓扑恒等式，对每个光滑 \(g\) 成立。

## 2. \(K_g\ge A\)：逐度量成立，不是先对度量取极小值

令
\[
a_{\varepsilon,\eta}
=\sum_j\varepsilon_jc_j+\sum_\ell\eta_\ell e_\ell
\]
为全部 Bauer–Furuta 符号类。对任意固定度量 \(g\)，在其 Hodge 正负分解下对符号平均：
\[
\operatorname{Av}_{\varepsilon,\eta}
\|(a_{\varepsilon,\eta})^+\|_2^2
=
A+\sum_j\|c_j^-\|_2^2+\sum_\ell\|e_\ell^+\|_2^2
\ge A.
\]
故对该度量至少存在一个符号类满足
\[
\|(a_{\varepsilon,\eta})^+\|_2^2\ge A.
\]
对这个类应用 scalar–Weyl monopole 不等式：
\[
K_g\ge \|(a_{\varepsilon,\eta})^+\|_2^2\ge A.
\]

所以
\[
\boxed{K_g\ge A\quad\text{对每个光滑 }g.}
\]

其中所选符号类可以随 \(g\) 改变；不需要沿度量路径连续选择。这里的实质外部输入是：所有这些符号类确实都是 monopole classes。单凭临界拓扑等式 \(D=A/3\) 并不能推出 \(K\ge A\)。

## 3. 配方步骤及常数：全部正确

逐点恒等式
\[
27\left(\frac{s^2}{24}+2w^2\right)
-(s-\sqrt6w)^2
=\frac18(s+8\sqrt6w)^2,\qquad w=|W^+|
\]
积分后给出
\[
L:=\int_M(s+8\sqrt6|W^+|)^2d\mu
=288\pi^2(3I-2K).
\]
利用
\[
I=\frac{2A}{3}+R,\qquad K\ge A,
\]
得到
\[
3I-2K\le 3R,
\]
因而
\[
L\le864\pi^2R.
\]
又因为
\[
R=\frac1{8\pi^2}\int|\Ric^\circ|^2d\mu,\qquad
E^\circ=\Ric^\circ,
\]
所以
\[
\boxed{
\int_M(s+8\sqrt6|W^+|)^2d\mu
\le864\pi^2R
=108\int_M|\Ric^\circ|^2d\mu
\le108\int_M|E|^2d\mu.}
\]

同时有精确关系
\[
K=A+\frac32R-\frac{L}{576\pi^2},
\]
故
\[
0\le K-A\le\frac32R.
\]

## 4. Weyl 模长估计确实不需要体积控制

置
\[
q=s+4=\tr_g E,\qquad
v=|W^+|-\frac1{2\sqrt6}.
\]
则
\[
s+8\sqrt6|W^+|=q+8\sqrt6v.
\]
记
\[
P=\int|\Ric^\circ|^2,\qquad X=\int q^2,\qquad Q=\int|E|^2.
\]
迹—无迹正交分解给出
\[
Q=P+\frac14X.
\]
由上一步
\[
\|q+8\sqrt6v\|_2\le\sqrt{108P},
\]
于是
\[
\begin{aligned}
8\sqrt6\|v\|_2
&\le \|q+8\sqrt6v\|_2+\|q\|_2\\
&\le \sqrt{108}\,P^{1/2}+2\left(\frac X4\right)^{1/2}\\
&\le \sqrt{112}\left(P+\frac X4\right)^{1/2}.
\end{aligned}
\]
平方即得
\[
\boxed{
\int_M\left(|W^+|-\frac1{2\sqrt6}\right)^2d\mu
\le\frac7{24}\int_M|E|^2d\mu.}
\]

因此 (d) 是完全体积无关的。脚本约 \(0.4123\) 的常数也有效，但较松，因为它分别使用了 \(P\le Q\) 与 \(X\le4Q\)，重复消耗同一 \(Q\)。

脚本注释中的判别式有笔误：
\[
32^2\cdot6+4\cdot384\cdot108=172032,
\]
不是 \(172416\)。代码实际使用 \(172032\)，故数值结果未受影响。

### 体积轮廓

若在固定 \(M\) 上
\[
Q_i=\int|E_i|^2\to0,
\]
则体积不是额外假设，而是可以推出。先由 \(I_i=2A/3+R_i\) 及 scalar 项非负得到 \(\|s_i\|_2\) 有界；又有
\[
\|s_i+4\|_2\le2Q_i^{1/2}.
\]
由
\[
4\Vol(g_i)^{1/2}\le\|s_i\|_2+\|s_i+4\|_2
\]
先得体积有界。随后
\[
\int s_i^2=16\Vol(g_i)+o(1),\qquad
\int|W_i^+|^2=\frac1{24}\Vol(g_i)+o(1).
\]
结合 \(I_i\to2A/3\)，可得
\[
\Vol(g_i)\to\frac{32\pi^2A}{9},
\quad
S_i\to\frac{16A}{27},
\quad
W_i\to\frac{2A}{27}.
\]

若拓扑变化、\(A_i\to\infty\)，相应结论需要 \(Q_i=o(A_i)\)，并应作 \(A_i\)-归一化。

## 5. 截断流后的适用范围

若
\[
\partial_tg=-2\chi^2(\Ric+g)
\]
在某时刻 \(t\) 给出了原闭流形 \(M\) 上的光滑正定度量 \(g(t)\)，则 (a)–(d) 对 \(g(t)\) 原样成立：

- 拓扑量不变；
- monopole classes 不变；
- Hodge 正投影虽随 \(t\) 变化，但符号平均论证可逐时重新应用。

因此，链条适用于最大光滑存在区间内每个 \(t<T\)。但若在 \(T\) 发生曲率爆破、失去正定性或只剩奇异极限，则经典 Chern–Weil、Hodge 与 SW 论证不能未经扩展直接使用。

更关键的是，静态链不证明
\[
Q(t)=\int_M|\Ric_{g(t)}+g(t)|^2d\mu_{g(t)}
\]
保持小。截断缺陷演化虽对 \(E\) 齐次，排除了与 \(E\) 无关的加性源，但仍含
\[
\int\chi^2|\Rm|\,|E|^2
\]
及过渡带梯度项。齐次性本身不能推出 \(Q(t)\le C Q(0)\)。Step 14 所要求的 collapse-uniform 局部曲率能量 bootstrap、Sobolev 吸收和过渡带控制仍未完成；脚本末尾的 “ALL DONE” 不成立。

还应注意：原度量若已有 \(Q_i(0)\to0\)，则上述 \(L^2\) Weyl 模长轮廓在 \(t=0\) 已经成立。截断流的用途只能是提供局部正则性或紧性，而不是产生该轮廓。

## 6. Weyl 模长不蕴含目标特征值

\(W^+\) 是 \(\Lambda^+\) 上迹零对称 \(3\times3\) 算子。相同模长
\[
|W^+|^2=\frac1{24}
\]
可对应不同谱，例如
\[
\left(-\frac16,\frac1{12},\frac1{12}\right)
\]
和
\[
\left(\frac1{4\sqrt3},-\frac1{4\sqrt3},0\right).
\]
所以即使 \(|W_i^+|\to1/(2\sqrt6)\) 点态成立，也不能确定 Step 6 所需谱。

设特征值
\[
\lambda_1\le\lambda_2\le\lambda_3,\qquad
\lambda_1+\lambda_2+\lambda_3=0.
\]
则
\[
|W|^2\ge\frac32\lambda_1^2,\qquad
\lambda_1\ge-\sqrt{\frac23}|W|.
\]
等号恰当且仅当
\[
\lambda_2=\lambda_3=-\frac{\lambda_1}{2}.
\]
在 \(|W|=1/(2\sqrt6)\) 时，这才给出
\[
\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
等价地，还需
\[
\det W^+=-\frac{|W^+|^3}{3\sqrt6}.
\]

## 7. 到达 forbidden-germ 矛盾所需的最小附加输入

除 \(\int|E_i|^2\to0\) 外，至少需要以下两个不同层面的输入。

### (i) 局部 Weyl 代数饱和的载体

需要某个选定 monopole 类的自对偶 harmonic/SW 形式 \(H_i\)，在相关开集上具有非零极限，并满足最低特征值缺陷趋零，例如
\[
\frac{\langle W_i^+H_i,H_i\rangle}{|H_i|^2}
+\sqrt{\frac23}|W_i^+|\longrightarrow0.
\]
该非负缺陷趋零会同时迫使：

- \(H_i\) 落入最低特征线；
- 最低特征值达到代数极值；
- 另外两个特征值相等。

仅有数值饱和 \(K_i\to A\) 并不自动保留 \(H_i\) 的局部质量；它可能消失、集中或相分离。

### (ii) 一个可传递曲率和形式的局部正则极限

需要存在正体积开集（或适当局部覆盖）使拉回后
\[
g_i\to g_\infty
\]
至少强到能传递 Ricci、Weyl 和上述非负缺陷，并有
\[
H_i\to H_\infty,\qquad |H_\infty|>0.
\]
光滑局部收敛是清楚的充分条件。此时得到
\[
\Ric_{g_\infty}=-g_\infty,\quad s_\infty=-4,\quad
|W_\infty^+|=\frac1{2\sqrt6},
\]
以及
\[
\Spec(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]
Einstein 条件给出 \(\delta W_\infty^+=0\)。常谱投影引理于是推出
\[
\nabla W_\infty^+=0.
\]
但 Einstein–Weyl 标量恒等式
\[
\Delta|W^+|^2
=2|\nabla W^+|^2+s|W^+|^2-36\det W^+
\]
在
\[
s=-4,\quad |W^+|^2=\frac1{24},\quad
\det W^+=-\frac1{864}
\]
下要求
\[
|\nabla W^+|^2=\frac1{16},
\]
矛盾。

因此，逻辑上最小的附加内容不是单一“紧性”假设，而是：

\[
\boxed{\text{局部正则极限}
+\text{非消失的 monopole/harmonic 形式}
+\text{最低特征值饱和。}}
\]

在固定临界流形上，Step 6 的非塌缩球论证若成立，会立即产生该矛盾，并因此反推出单位尺度处处塌缩。剩余关键对象遂是：在塌缩区域的局部覆盖上实现非塌缩正则化，同时保持拉回后的 LeBrun 非负缺陷和 monopole 形式非消失。当前材料尚未给出这一 collapse-unwrapping/curvature-bootstrap 定理。