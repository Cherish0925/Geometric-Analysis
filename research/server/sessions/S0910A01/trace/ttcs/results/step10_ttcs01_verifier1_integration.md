# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 10,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step10_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step10_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the corrected Step 10 reassessment and route plan for the Yau 26 Ricci-pinching project. Check the mathematical scope and consistency of the fixed-scale accessible-cover theorem, the use of the normal-cover mean lemma, Naber--Zhang Proposition 6.4, Lott's orbit-volume formula, Cheeger--Naber positive-branch statements, and the four-dimensional energy bookkeeping. Identify any remaining overstatement, missing hypothesis, coefficient/sign issue, or stronger next mathematical target. Treat the goal as rigorous progress toward proving or refuting the full proposition, not final exposition.

## Integrated Scientific Memo

# Step 10 核验结论

Step 10 的主干是成立的：它正确收缩了 Lott 轨道体积公式的适用范围，正确区分了 Naber–Zhang 的 harmonic-radius 结论与需要 \(|\nabla\mathrm{Ric}|\) 的曲率结论，正确限定了 Cheeger–Naber 的四维有限微分同胚型定理，并修正了四维 signature 系数。然而，**当前写出的 fixed-scale accessible-cover theorem 还不是完整严谨的定理**；主要缺口在 cover buffer、可测性、尺度安排和能量范数约定。

## 1. Normal-cover mean lemma：核心正确，但 buffer 必须重写

乘重数消去论证是正确的。对 regular/normal cover，

\[
m_r(x)\le N(2r),\qquad
N(2r)\operatorname{Vol}B_r(p)\le \operatorname{Vol}B_{3r}(\hat p),
\]

从而

\[
\fint_{B_r(\hat p)}\pi^*\phi
\le
\frac{V_{-K}^{(n)}(3r)}{V_{-K}^{(n)}(r)}
\fint_{B_r(p)}\phi .
\]

但原假设

\[
B_{3r}(\hat p)\subset \widehat U
\]

若球按 \(\widehat U\) 的内在距离定义，就是同义反复，不能保证 deck 轨道在有界集内有限，也不能排除球碰到不完备域的边缘。应改为例如

\[
\overline{B_{3r}^{\,\widehat U}(\hat p)}\Subset \widehat U,
\]

并要求 Ricci 下界在该闭球邻域成立；或者更干净地假设 cover 定义在 \(B_{4r}(p)\) 上，而论证只使用其上方的 \(3r\)-核心。

“closest-lift ties 是余维一光滑子流形”的说法不可靠，cut locus 会造成问题，也完全没有必要。枚举可数 deck 群，在所有最近 lift 中按枚举选第一个，即得可测截面；再用局部等距的面积公式即可。

此外，Step 9 中给出的双曲 Bishop–Gromov 数值似不准确，但这些数值不参与证明，建议删除而不是保留未经核验的小数。

## 2. Accessible-cover 排除定理：可成立，但需精确化

适当的版本如下。令 \(E_i\subset M_i\) 为可测集。假设每个 \(p\in E_i\) 满足：

1. \(|\operatorname{Ric}_{g_i}|\le3\)，并有 Naber–Zhang 所需的局部完备性
   \[
   \overline{B_2(p)}\Subset B_4(p);
   \]
2. 对某些 \(0\le\ell\le k\le4\)、\(\ell\le3\)，
   \[
   d_{GH}\!\left(B_2(p),B_2(0^{k-\ell},z^\ell)\right)
   <\delta_*(4,r_*);
   \]
3. \(Z^\ell\) 是相应的 Ricci-limit space，且模型非塌缩半径
   \[
   r_c(z^\ell)\ge r_*>0;
   \]
4. 对 Naber–Zhang 定义的同一个尺度 \(\delta_*\)，
   \[
   \operatorname{rank}\Gamma_{\delta_*}(p)=4-k,
   \qquad
   \Gamma_{\delta_*}(p)
   =\operatorname{Image}\bigl[\pi_1(B_{\delta_*}(p))
      \to\pi_1(B_2(p))\bigr].
   \]

则 Naber–Zhang Proposition 6.4 给出统一的

\[
r_h(\tilde q)\ge h_*(4,r_*)>0
\]

于 \(B_1(p)\) 中各点的适当局部 universal cover 上。取固定

\[
0<a<\min\{1/4,h_*/4\},
\]

便可在 \(\widetilde{B_1(p)}\) 中使用 precompact 的 \(3a\)-核心，因此无需额外把“存在 genuine normal cover”列为独立几何假设：universal cover 本身就是 normal cover，真正要核验的是半径和域的兼容性。

若 \(\operatorname{Vol}E_i\ge\eta\operatorname{Vol}M_i\)，固定半径平均选择给出 \(p_i\in E_i\) 使

\[
\fint_{B_a(p_i)}F_i\to0.
\]

cover-mean lemma 于是给出

\[
\fint_{B_a(\tilde p_i)}\pi_i^*F_i\to0.
\]

在固定 harmonic chart 上，bounded Ricci 给出有限 \(W^{2,p}\) 控制；应明确选 \(p>4\)，从而获得 \(C^{1,\alpha}\) 紧性。利用

\[
\operatorname{Ric}_{g_i}=-g_i+e_i,
\qquad \|e_i\|_{L^\infty}\to0,
\]

harmonic-coordinate 方程进一步给出缩小图上的 strong \(W^{2,p}\) 收敛。极限光滑且满足 \(\operatorname{Ric}=-g\)。曲率及 \(W^+\) 在 \(L^p\) 中强收敛，特征值对对称矩阵是 Lipschitz 的，因此 \(\mathcal G_i\) 可在 \(L^1\) 中传递，得到

\[
s=-4,\qquad |W^+|^2=\frac1{24},\qquad
\operatorname{Spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).
\]

Derdziński 因子为 \(1\)，故极限局部 Kähler；但 Kähler 曲面满足

\[
|W^+|^2=\frac{s^2}{24}=\frac23,
\]

与 \(1/24\) 冲突。因此

\[
\frac{\operatorname{Vol}E_i}{\operatorname{Vol}M_i}\to0.
\]

这里仍需两项正式修补：

- \(S_i(r_*)\) 由“存在某模型”定义时未证明 Borel；最好对任意满足条件的**可测子集**陈述结论，或另证 analytic/Borel 可测性。
- 必须写出 \(\delta_*,h_*,a\) 的选取顺序，不能笼统地说“固定尺度”。

这一定理排除的是 fixed-scale NZ-modeled maximal-rank 部分，而不是所有 regular collapse。

## 3. Lott 公式：范围和符号均已正确收缩

Lott (2.9) 确为

\[
\Delta_Bv=
\left(\frac14|F|^2-\lambda N\right)v,
\qquad v=\sqrt{\det G}.
\]

除 exact adapted metric 和 free local abelian action 外，还需要 determinant holonomy 落在 \(\det^{-1}(\{\pm1\})\)，否则 \(v\) 未必在基底上全局定义。Proposition 2.10 还要求：

\[
B\ \text{parabolic},\qquad \lambda\le0,\qquad v\ \text{bounded above}.
\]

因此 Step 10 对该公式的限制是正确的。对 \(\lambda=-1\)，

\[
\Delta_Bv=\left(\frac14|F|^2+N\right)v>0,
\]

但局部区间并不矛盾。实双曲 cusp

\[
dt^2+e^{2t/\sqrt3}g_{T^3}
\]

满足 \(\operatorname{Ric}=-g\)，且 \(v=e^{\sqrt3t}\)、\(v''=3v\)，正好校准该事实。

## 4. \(\mathrm{Nil}^3\) 方程：\(3-\mu\) 正确，但不能单独排除圆基底

设

\[
H_j=\frac{a_j'}{a_j},\quad
H=H_1+H_2+H_3,\quad
v'=Hv,\quad
\mu=\frac{a_3^2}{2a_1^2a_2^2}.
\]

\(\mathrm{Nil}^3\) 轨道的内在 Ricci 特征值为

\[
(-\mu,-\mu,\mu).
\]

对 \(\operatorname{Ric}=-g\)，三条切向 Einstein 方程求和得

\[
H'+H^2=3-\mu,
\]

所以

\[
v''=(3-\mu)v.
\]

该修正符号正确。不过 \(3-\mu\) 不定号，**此式本身不能用最大值原理排除周期基底**。还需第二个恒等式。令

\[
q=H_1+H_2-H_3,
\]

则个别切向方程给出

\[
q'+Hq=1-3\mu,
\qquad
(vq)'=(1-3\mu)v.
\]

若基底为圆，周期积分同时产生

\[
\int (3-\mu)v=0,\qquad
\int(1-3\mu)v=0.
\]

令 \(I_0=\int v>0\)、\(I_\mu=\int\mu v\)，则前者给 \(I_\mu=3I_0\)，后者给 \(I_\mu=I_0/3\)，矛盾。Step 10 所说“circle-base exclusion survives”可以保留，但必须附上此第二恒等式，不能归因于 \(v''=(3-\mu)v\) 单独作用。

复杂双曲 nil cusp 的归一化在现有材料中没有完整 coframe 计算；若继续把它作为校准例，应补出明确尺度和 \(\operatorname{Ric}=-g\) 的直接验证。

## 5. Cheeger–Naber 正分支：结论准确但只能到有限型/塌缩二分

在四维，

\[
\|g^{-1}(\operatorname{Ric}-g)\|_{\mathrm{op}}\le\delta<1
\]

给出 \(\operatorname{Ric}\ge(1-\delta)g\)，故 Myers 提供统一直径界。若总面积有统一正下界，Bishop–Gromov 给出单位球体积下界；而从 op norm 估计也可得到 eventually \(|\operatorname{Ric}|_{\mathrm{HS}}\le3\)。因此 Cheeger–Naber Theorem 1.12 可用，并推出：

- 对两两非微分同胚的 \(\#_k(S^2\times S^2)\)，若 \(\delta_i\to0\)，则总面积必须趋零；
- 或者在大 \(k\) 尾部，正 Einstein 缺陷有正下界。

这不推出任一固定流形存在 Einstein 度量。非塌缩极限若为 orbifold，也仍需 obstruction projection/desingularization。Theorem 1.12 明确是四维；Theorem 1.4 的全维 codimension-four 正则性不能替代全维有限微分同胚型定理。

## 6. 四维能量：signature 修正正确，但必须声明曲率范数

正确的 signature 公式是

\[
12\pi^2\tau(M)
=\int(|W^+|^2-|W^-|^2),
\]

且 \(M=X\#k\overline{\mathbb{CP}}^{\,2}\) 时

\[
\int|W^-|^2
=
\int|W^+|^2-12\pi^2\tau(X)+12\pi^2k.
\]

因此此前 \(32\pi^2k\) 的系数确实错误。

Step 10 的

\[
\int|\operatorname{Rm}|^2
=8\pi^2\chi(M)+\int|E|^2
\]

只在 \(\operatorname{Rm}\) 指曲率算子
\(\mathcal R:\Lambda^2\to\Lambda^2\) 的 Hilbert–Schmidt 范数时成立：

\[
|\mathcal R|^2
=|W^+|^2+|W^-|^2+\frac12|E|^2+\frac{s^2}{24}.
\]

若使用通常的 \((0,4)\)-曲率张量范数，则

\[
|\mathrm{Rm}|_{(0,4)}^2=4|\mathcal R|^2,
\]

所有相应系数乘 \(4\)。脚本和正文必须统一注明约定。

定义

\[
J=\frac1{8\pi^2}\int|E|^2
\]

时才有

\[
\int|\mathcal R|^2
=8\pi^2\bigl(\chi(X)+k+J\bigr).
\]

在 \(\operatorname{Ric}+g=o_{L^\infty}(1)\) 且 \(\operatorname{Vol}/A=O(1)\) 下，

\[
E=\operatorname{Ric}-\frac{s}{4}g=O(\delta_i),
\qquad
J_i/A_i\to0.
\]

因而真正额外需要的是选定代数曲面族的 \(\chi(X_i)/A_i\) geography bound，以及已校准的 \(k_i/A_i\) 界；这些不由 Ricci pinching 单独推出。

校准值相互一致：

\[
\operatorname{Vol}\sim\frac{32}{9}\pi^2A,\quad
\int\frac{s^2}{24}\sim\frac{64}{27}\pi^2A,\quad
\int|W^+|^2\sim\frac4{27}\pi^2A.
\]

局部尺度不变量

\[
r^4\fint_{B_r}|\mathcal R|^2
\]

也是正确对象。但“均值有界”只给出受控能量，不给出小于 \(\varepsilon\)-regularity 阈值，也不会在塌缩基底上自动产生 harmonic radius。

## 7. 仍然存在的最大范围问题

这一整条负分支分析研究的是

\[
\|\operatorname{Ric}_{g_i}+g_i\|_{L^\infty,\mathrm{op}}\to0
\]

的近 Einstein、近 LeBrun 临界序列。Yau 26 的假设则只是存在固定常数

\[
c_4g\le\operatorname{Ric}_g\le C_4g,
\]

并不意味着该 metric 接近任何 Einstein metric，也不自动产生上述 near-critical 序列。因此目前成果严格支持的是：

> 对特定四维 LeBrun 家族，某些趋近负 Einstein 边界的序列若存在，则其大部分体积必须逃离所有固定尺度 accessible-cover 区域。

它尚不是对 \(P_4^{-}\) 的证明或反证，更不是对 Yau 26 的直接归约。即使构造出一个 \(\operatorname{Ric}\approx-g\) 的非 Einstein 家族，要反驳原命题仍须击败所有候选区间 \([c_4,C_4]\)，包括正、负和跨零区间。

## 8. 更强而精确的下一数学目标

最直接的桥梁是证明存在固定 \(a,v,\eta>0\)，使每个假想 near-critical LeBrun 序列都满足

\[
\operatorname{Vol}\mathcal A_i(a,v)
\ge\eta\,\operatorname{Vol}M_i,
\]

其中

\[
\mathcal A_i(a,v)=
\left\{p:
\begin{array}{l}
\widetilde{B_{4a}(p)}\text{ 上有 precompact }3a\text{-核心},\\
\operatorname{Vol}B_a(\tilde p)\ge va^4
\end{array}
\right\}.
\]

现有 transport lemma 与 forbidden-germ 论证会立即排除这种序列。Naber–Zhang 给出了进入 \(\mathcal A_i(a,v)\) 的充分条件，所以剩余的具体对象是定量控制以下坏集的体积：

\[
\operatorname{rank}\Gamma_{\delta_*}(p)<4-k,
\qquad
r_c(z)\to0,
\]

以及 residual four-dimensional cores、singular fibers 和仅 shrinking-scale 可解卷区域。理想的桥梁应把这些失败模式中的至少一个与曲率算子能量或 Euler/Chern–Weil 密度集中联系起来。仅有全局 \(O(A)\) 能量预算不足；需要一个“不可访问体积 \(\Rightarrow\) 定量拓扑/能量代价”的新局部定理。