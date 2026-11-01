# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 74,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step74_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step74_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step 74 route correction for the Yau--26 research. Read the Step74 note and supporting data, together with A02's positive-branch allocation and the 20260912 manuscript source. Check two load-bearing mathematical points: (1) the graph-neck repair: does the construction h0=dtheta^2+e^{2f}dx^2+e^{-2f}dy^2 with negative Yamabe normalization really give analytic T^2-invariant scalar -6 torus metrics suitable as Koiso center data S(0)=0, S'(0)=Ric_h^#+3I, and what assumptions or caveats remain? (2) the positive flux scale critique: does FND:flux / constant-scalar refinement only give a c/L lower bound, so that nonzero obstruction coefficient is compatible with delta->0 along L->infty unless an additional sequence-scale mechanism is proved? Compare with the manuscript's |log a| delta_+ -> 1/6 construction. Please identify any mathematical errors, missing hypotheses, or sharper next theorem statement that would materially improve the research direction.

## Integrated Scientific Memo

# Step 74 核验结论

两个承重点均成立：

1. **Yamabe 修正确实构造出解析、对角、\(T^2\)-不变、标量曲率 \(-6\) 的 \(T^3\) 度量，并给出合法的 Koiso 全测地中心数据。**
2. **二次 TT 模的环带通量只产生 \(c/L\) 级下界；因此当 \(L\to\infty\) 时，非零障碍系数与 \(\delta\to0\) 完全相容。手稿中的常标量模型以 \(L\delta_+\to1/6\) 实现了这一尺度，说明该损失不是证明技术上的松弛。**

但两点都只解决局部接口，尚未给出图颈全局构造或正分支证明。

---

## 一、Yamabe–Koiso 中心构造

令
\[
h_0=d\theta^2+e^{2f(\theta)}dx^2+e^{-2f(\theta)}dy^2 ,
\]
其中 \(f\) 是非恒定实解析周期函数。一般地，
\[
ds^2+e^{2b(s)}dx^2+e^{2c(s)}dy^2
\]
的标量曲率为
\[
R=-2(b''+c'')-2\bigl((b')^2+(c')^2+b'c'\bigr).
\]
取 \(b=f,c=-f\)，得到
\[
R(h_0)=-2(f')^2.
\]
又因 \(d\mu_{h_0}=d\theta\,dx\,dy\)，
\[
\int_{T^3}R(h_0)\,d\mu_{h_0}<0.
\]
以常数函数测试 Yamabe 泛函即得 \(Y([h_0])<0\)。

### Yamabe 因子与对称性

负 Yamabe 类中，将常标量固定为 \(-6\) 后，共形代表唯一。\(x,y\) 平移保持 \(h_0\)，故也必须保持唯一解，因而共形因子只依赖 \(\theta\)：
\[
h=\psi^4h_0,\qquad \psi=\psi(\theta)>0.
\]
三维共形标量公式给
\[
R_h=\psi^{-5}\left(-8\Delta_{h_0}\psi+R(h_0)\psi\right),
\]
而 \(\Delta_{h_0}\psi=\psi''\)，所以
\[
-8\psi''-2(f')^2\psi=-6\psi^5.
\]
当 \(f\) 解析时，这是解析 ODE，故正解 \(\psi\) 解析。因此 \(h\) 是解析、对角、\(T^2\)-不变的标量 \(-6\) 度量。

作弧长变换
\[
ds=\psi^2d\theta,\qquad
b=2\log\psi+f,\qquad c=2\log\psi-f,
\]
则
\[
h=ds^2+e^{2b(s)}dx^2+e^{2c(s)}dy^2,
\]
且 \(b,c\) 在长度
\[
\ell=\int\psi^2\,d\theta
\]
的圆上周期。因此这确实修复了 Step 73 固定 Riccati 参数族的“非零均值”问题；那个失败只属于受限参数族，并非对角 \(T^2\)-不变中心数据的障碍。

### Koiso 中心条件

采用
\[
S=\frac12h_t^{-1}\partial_th_t,\qquad H=\operatorname{tr}S.
\]
对 Gaussian 度量 \(g=dt^2+h_t\)，在 \(S(0)=0\) 时，
\[
\operatorname{Ric}_{00}=-\operatorname{tr}S'(0),
\]
\[
(\operatorname{Ric}_{\tan})^\sharp
=\operatorname{Ric}_h^\sharp-S'(0).
\]
若 \(\operatorname{Ric}_g=-3g\)，则
\[
\operatorname{tr}S'(0)=3,\qquad
S'(0)=\operatorname{Ric}_h^\sharp+3I.
\]
取迹得到
\[
3=R_h+9,
\]
即约束恰为
\[
R_h=-6.
\]
动量约束
\[
\operatorname{div}S-dH=0
\]
在 \(S=0\) 时自动成立。

所以 \((h,S=0)\) 是合法解析 Einstein Cauchy 数据；\(S'(0)\) 不是额外自由指定的数据，而是 Einstein 方程决定的二阶量。手稿所引解析 Cauchy/Koiso 定理因而给出某个 \(|t|<\varepsilon\) 上的局部偶对称精确 \(\operatorname{Ric}=-3g\) collar。

### 尚需保留的关键限制

该结论没有给出：

- 向任意长区间的延拓；
- \(S(t)\to I\)、\(H(t)\to3\)；
- \(e^{-2t}h_t\) 收敛到某个带标记的平坦环面；
- 实际纤维 Ricci 各向异性按 \(e^{-2t}\) 衰减；
- 与另一半核或图流形块的全局匹配；
- 全部 normal、tangential、mixed Ricci 分量的统一最大范数控制。

弧长周期 \(\ell\) 还是实际 cusp 晶格模数；把坐标周期重写为 \(2\pi\) 并不会消除相对晶格尺度。

若采用 Einstein–DeTurck 方程
\[
\operatorname{Ric}+3g+\mathcal L_Wg=0,
\]
还必须用边界条件或 \(W\) 的方程证明 \(W=0\)，或者直接估计真实残差 \(\operatorname{Ric}+3g\)。仅求得 DeTurck 解不等于 Einstein 解。

### 数值文件的两个问题

数值结果与解析构造相容，但有两处报告应修正。

1. 脚本先由 ODE 右端定义
   \[
   \psi''=\frac34\psi^5-\frac14(f')^2\psi,
   \]
   再代回同一等式计算 residual，因此记录的 \(1.1\times10^{-16}\) 是代数自消，不是独立数值验证。真正有意义的是 FFT 二阶导数残差约 \(1.5\times10^{-5}\) 及标量曲率接近 \(-6\) 的范围。

2. `np.trapezoid` 用在不含末端点的周期网格上，漏掉最后一个周期小区间。应使用
   \[
   \ell\approx \frac{2\pi}{N}\sum_j\psi_j^2.
   \]
   因此记录的 \(2.577531\) 略低，修正量约 \(1.2\!-\!1.3\times10^{-3}\)。这不影响任何存在性或 Koiso 结论。

---

## 二、正分支通量的真实尺度

对二次齐次 TT 张量 \(K\)，手稿取
\[
o=r^{-d-2}K.
\]
由于 \(K=O(r^2)\)，
\[
\int_A\|o\|_*\,dV
=J_K\int_b^R\frac{dr}{r}
=J_KL,\qquad L=\log(R/b).
\]
而边界 Wronskian 给固定通量
\[
\int_A\langle D\operatorname{Ric}_e u,o\rangle
=-\frac{d+2}{2}I_K.
\]
故只能推出
\[
\|D\operatorname{Ric}_eu\|_{\mathrm{op},\infty}
\ge
\frac{(d+2)I_K}{2J_KL}.
\]
若端点跳跃为 \(\kappa K\)，右侧相应乘 \(|\kappa|\)。

非线性与加权能量版本只在分子、分母加入端点误差和能量余项，主尺度仍是 \(1/L\)。因此
\[
\kappa\ne0,\qquad L_i\to\infty,\qquad \delta_i\asymp L_i^{-1}\to0
\]
没有矛盾。

### 与手稿 \(1/6\) 模型的精确比较

常标量球面 \(A_1\) 模型满足更强下界
\[
\liminf L\,\delta_+\ge\frac16.
\]
显式构造取
\[
T=|\log a|,\qquad b=aT,\qquad R=T^{-1},
\]
故
\[
L=\log\frac{R}{b}=T-2\log T,\qquad \frac LT\to1.
\]
而
\[
s_{\widehat g_a}=4,\qquad
T\,\delta_+(\widehat g_a)\to\frac16,
\]
所以实际上
\[
L\,\delta_+(\widehat g_a)\to\frac16.
\]
这同时给出下界与实现：常数 \(1/6\) 在该退化方案中是锐的，而误差本身仍趋零。故通量不能单独产生维数统一的正间隙。

这些模型未必位于无 Einstein 的底层流形上，因此不是 \(P_n^+\) 的反例；但它们已经严格否定了“非零局部障碍系数自动给出固定正误差”的推理。

---

## 三、固定重标环带提取仍需 tightness

仅仅“先固定重标环带、令 \(\delta_i\to0\)，再令环带半径增大”不足以消去系数。模型
\[
\eta_i(t)=\frac{t}{L_i},\qquad 0\le t\le L_i,
\]
具有总跳跃 \(1\) 和残差 \(O(L_i^{-1})\)，但在每个固定长度的 \(t\)-区间上变化都趋零。先取 \(i\to\infty\) 会把整个过渡丢到无穷远尺度。

固定环带论证只有在同时满足以下某种紧性时才有效：

- 固定比例的系数跳跃集中在统一有界的对数长度内；
- 整条颈上的加权残差质量趋零；
- \(\delta_iL_i\to0\)；
- 存在阻止对数尺度慢漂移的全局传输、单调性或 coercive 恒等式。

最自然的序列量不是单独的 \(\delta_i\)，而是
\[
\mathfrak R_i
=\int_{A_i}
\|\operatorname{Ric}_{g_i}-\sigma g_i\|_{\mathrm{op}}
\,\|o_i\|_*\,dV.
\]
在适当 harmonic/Bianchi gauge、端点模型和非线性误差控制下，应证明
\[
\frac{d+2}{2}I_K|\kappa_i|
\le
\mathfrak R_i+
C_K\bigl(\epsilon_i+\mathcal E_i+
R_i\sqrt{\mathcal E_i}+R_i^2\bigr).
\]
而最大范数只给
\[
\mathfrak R_i\le J_K\,\delta_iL_i+o(1).
\]
因此真正可推出的是
\[
|\kappa_i|\lesssim\delta_iL_i+o(1),
\]
常标量 \(A_1\) 归一化下相应为
\[
|\kappa_i|\le6\,\delta_iL_i+o(1).
\]
手稿模型以 \(\kappa_i=1\)、\(\delta_iL_i\to1/6\) 饱和这一关系。

---

## 四、A02 高阶 mode 计划需要的修正

若 \(K_\ell\) 是次数 \(\ell\) 的齐次模式，候选对偶张量
\[
o_\ell=r^{-(d-2)-2\ell}K_\ell
\]
及预期 Wronskian 系数
\[
-\frac{d+2\ell-2}{2}I_{K_\ell}
\]
与 \(\ell=2\) 的手稿公式相容，但必须另行证明规范项消失和边界系数。

更重要的是，其核范数质量为
\[
\int_A\|o_\ell\|_*\,dV
=J_{K_\ell}\int_b^R r^{1-\ell}\,dr.
\]
所以：

- \(\ell=2\)：唯一的对数临界模，质量为 \(LJ_K\)；
- \(\ell\ge3\)：质量主要由内端控制，约为 \(b^{2-\ell}\)，所得最大范数下界反而只有 \(O(b^{\ell-2})\)。

因此高阶逐模 flux 不会比二次模更强。正分支的核心应聚焦于二次 Weyl/TT 模如何在对数尺度上传输；高阶模更可能需要由椭圆方程从属于二次模，而不是分别靠通量强迫消失。

---

## 五、更准确的下一定理对象

正分支真正缺少的不是另一条静态 \(c/L\) 不等式，而是一个排除慢漂移的序列定理。可表述为二次 TT 模的三环带估计：

> 在紧正 Ricci 夹逼反例序列产生的规范化 maximal neck 上，存在只依赖局部模型的 \(\lambda>1\)、\(\vartheta<1\)，使二次 TT 系数 \(K_i\) 满足
> \[
> \|K_i\|_{[\lambda r,\lambda^2r]}
> \le
> \vartheta\max\!\left\{
> \|K_i\|_{[r,\lambda r]},
> \|K_i\|_{[\lambda^2r,\lambda^3r]}
> \right\}
> +C\delta_i,
> \]
> 或者给出等价的全颈加权残差 tightness。

若 \(\vartheta<1\)，系数不能以 \(1/L\) 斜率横跨无限多个对数尺度，因而可在有限长度环带捕获固定跳跃，再由 flux 迫使二次障碍消失。手稿的 \(A_1\) 常标量填充正是 \(\vartheta=1\) 的临界压力测试：其系数近似线性地铺展在整个 \(\log r\) 区间。

该定理若不能在纯 Ricci 夹逼下成立，则必须明确增加何种结构——例如标量规范化、非塌缩、bubble-tree 端点控制、weighted harmonic gauge 或全局拓扑/能量账本——并检验这些假设是否排除手稿的 \(L\delta\to1/6\) 模型。

---

## 总结判断

- **图颈修复成立，但范围仅为局部解析中心数据。** 它消除了 Step 73 受限 Riccati 参数族的伪障碍；没有解决长时间延拓、平坦 cusp 匹配或闭图流形上的最大 Ricci 误差构造。
- **正通量尺度批评成立且为锐的。** 非零二次障碍系数与 \(\delta\to0\) 不矛盾，只与 \(\delta L\to0\) 矛盾。
- **固定重标环带提取本身不够。** 必须额外证明过渡不能逃逸到无限对数尺度。
- **最有实质的下一对象是二次 TT 模的 sequence-level tightness/three-annulus theorem，而非无尺度的“非零通量即正间隙”命题。**