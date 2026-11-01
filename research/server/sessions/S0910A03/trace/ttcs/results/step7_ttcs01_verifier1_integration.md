# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 7,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step7_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step7_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the orbit-volume obstruction argument for negative Einstein regular collapse:

1. Check that Lott's equation (2.9) Δv = (|F|²/4 - λN)v correctly specializes to Δv = (|F|²/4 + N)v for λ = -1, and that this makes v strictly subharmonic.

2. Verify the parabolicity argument: complement of finitely many points in a compact space of dim ≥ 2 is parabolic (Grigoryan), bounded-above subharmonic → constant → contradiction with positive RHS.

3. Check the circle base case: ∫v'' = 0 vs ∫Nv > 0.

4. Verify the near-Einstein error term: for Ric = -g + E with ||E||∞ ≤ δ, the coefficient becomes N(1-δ) > 0 for δ < 1.

5. Check the capacity estimate: from Δv ≥ cv with test function η²/v, one gets c∫η² ≤ ∫|∇η|².

6. Verify that the conclusion is correctly scoped: excludes free abelian collapse only (not nil³), and only on parabolic bases with bounded orbit volume. Identify any gaps or additional hypotheses needed.

7. Check whether the Cheeger-Tian framework legitimately applies to near-Einstein (not exactly Einstein) 4-manifolds to produce a groupoid limit with Ric = -g.

## Integrated Scientific Memo

# 核验结论：负 Einstein 正则阿贝尔塌缩的轨道体积障碍

核心局部结论成立，但其在近 Einstein 塌缩序列上的全局应用目前不成立。主要问题有三项：

1. “有限总体积 \(\Rightarrow v\) 有界”错误；
2. 所声称的容量估计符号错误，事实上为假；
3. 仅由 \(\|\operatorname{Ric}+g\|_{L^\infty}\to0\) 不能直接调用 Einstein 情形的 Cheeger–Tian 曲率分解。

以下逐项核验。

## 1. Lott 方程及 \(\lambda=-1\) 特化

在具有自由等距 \(\mathbb R^N\)-作用的正则区域，令
\[
v=\sqrt{\det G}>0.
\]
Lott 的轨道体积方程为
\[
\Delta_Bv
 =\left(\frac14|F|^2-\lambda N\right)v.
\]
因此当 \(\lambda=-1\) 时，
\[
\boxed{\Delta_Bv
 =\left(\frac14|F|^2+N\right)v\ge Nv>0.}
\]
在约定 \(\Delta=\operatorname{tr}\nabla^2\) 下，\(v\) 确为严格次调和函数。该结论仅适用于自由作用和适配分解存在的正则阿贝尔支层，不能直接跨越秩降、奇异纤维或非阿贝尔轨道。

## 2. 抛物性论证：条件成立时正确，但应用中缺少两个条件

若 \(B\) 连通且具有相应 Liouville 抛物性，并且
\[
0<v\le C,\qquad \Delta v\ge cv,\quad c>0,
\]
则有界上方的次调和函数 \(v\) 必为常数，而后
\[
0=\Delta v\ge cv>0
\]
矛盾。因此，作为一个带假设的命题，这一障碍正确。

### 有限点补空间的精确条件

若 \(K\) 是紧致光滑 Riemann 流形或 orbifold，\(\dim K=m\ge2\)，且
\[
B=K\setminus\{p_1,\dots,p_q\},
\]
在穿孔附近度量具有通常的光滑、orbifold 或受控锥形结构，则单点具有零 \(W^{1,2}\)-容量：

- \(m>2\) 时，环形截断能量为 \(O(\varepsilon^{m-2})\)；
- \(m=2\) 时，对数截断能量为 \(O(1/\log(1/\varepsilon))\)。

因此有界次调和函数可跨穿孔延拓，进而由紧致空间上的最大值原理成为常数。

但“有限点补的任意紧致度量空间，维数至少二”过强。仅有拓扑维数和完备化添加有限点，并不能保证这些点是 polar，也不能排除 cusp、退化 warped end 或真实边界。必须证明每个端点在极限基底度量下：

- 位于有限距离；
- 具有零容量；
- 或直接证明整个基底抛物。

此外，原笔记中的
\[
\text{有限四维总体积}\Longrightarrow \sup_B v<\infty
\]
是错误的。总体积推送至多给出
\[
\int_B v\,(\text{lattice factor})\,d\mu_B<\infty,
\]
即某种 \(L^1\) 控制，而非 \(L^\infty\) 控制。正解 Green 核可在穿孔处无界且可积，并在穿孔外满足 \(\Delta v=cv\)，所以可积性不能替代有界性。必须另行证明轨道体积在奇异端附近一致有界，例如由受控正则塌缩、小纤维尺度或延拓定理推出；“正在塌缩”本身若无统一几何控制，也不能自动提供这一点。

还需注意：Step 6 得到直径趋于无穷，因此 pointed groupoid 极限的基底完备化未必紧致，更未必只是紧致 orbifold 删除有限点。该几何描述本身需要证明。

## 3. 圆周基底

若基底为长度 \(L\) 的圆周，取弧长参数 \(s\)。二维曲率形式在一维基底上为零，所以精确方程甚至是
\[
v''=Nv.
\]
周期性给出
\[
\int_0^L v''\,ds=0,
\]
而 \(v>0\) 意味着
\[
N\int_0^L v\,ds>0,
\]
矛盾。近 Einstein 不等式
\[
v''\ge N(1-\delta)v,\qquad \delta<1,
\]
也给出同一矛盾。

若基底是区间，则需要端点条件。若两个有限端点均有 \(v\to0\)，严格凸性排除正解；若 \(v\) 不趋零、发散或端点位于无限距离，则目前没有闭合的结论。

## 4. 近 Einstein 误差项

在原度量本身具有精确自由等距阿贝尔作用和精确适配分解时，若
\[
\operatorname{Ric}_{\bar g}=-\bar g+E,
\qquad
\|g^{-1}E\|_{\mathrm{op}}\le\delta,
\]
则一般的竖直迹公式给出
\[
\Delta_Bv
 =\left(\frac14|F|^2-\operatorname{tr}_V\operatorname{Ric}\right)v
 =\left(\frac14|F|^2+N-\operatorname{tr}_VE\right)v.
\]
因为
\[
|\operatorname{tr}_VE|\le N\delta,
\]
故
\[
\boxed{\Delta_Bv
 \ge\left(\frac14|F|^2+N(1-\delta)\right)v
 \ge N(1-\delta)v.}
\]
所以 \(\delta<1\) 时系数确为正。

然而这不能未经补充直接用于 CFG 的近似 \(N\)-结构。若作用只对某个平滑后的不变度量等距，而不是对原 \(g_i\) 精确等距，则轨道体积方程会出现作用非等距及二阶度量比较误差；仅有 Ricci 缺陷 \(E_i\) 的 \(L^\infty\) 控制无法吸收这些项。最干净的用法是在已经获得的光滑极限 groupoid 上应用精确方程，但这依赖第 7 项尚未建立的正则紧性。

## 5. 所声称的容量估计为假

从
\[
\Delta v\ge cv,\qquad v>0
\]
以 \(\psi=\eta^2/v\) 测试，得到
\[
\begin{aligned}
c\int\eta^2
&\le \int\frac{\eta^2}{v}\Delta v\\
&=-\int\left\langle\nabla\!\left(\frac{\eta^2}{v}\right),\nabla v\right\rangle\\
&=\int\eta^2|\nabla\log v|^2
 -2\int\eta\langle\nabla\eta,\nabla\log v\rangle\\
&=\int|\eta\nabla\log v-\nabla\eta|^2
 -\int|\nabla\eta|^2.
\end{aligned}
\]
这里不存在将右侧从上方控制为 \(\int|\nabla\eta|^2\) 的 AM–GM 步骤；平方项符号正好阻止这种推导。

反例可取
\[
v(x)=e^{\sqrt c\,x}\quad\text{于 }\mathbb R,
\qquad v''=cv.
\]
令 \(\eta_R=1\) 于 \([-R,R]\)，并在两个固定宽度过渡区截断，则
\[
c\int\eta_R^2\asymp R,\qquad
\int|\eta_R'|^2=O(1),
\]
直接否定
\[
c\int\eta^2\le\int|\nabla\eta|^2.
\]

因此，下列推论均应删除，除非另有独立证明：

- “正则区域体积由边界容量控制”；
- “\(\operatorname{Vol}(\Omega)\le L^2/c\)”；
- “有限容量迫使向奇异支层支付确定过渡代价”；
- 由该容量估计建立的定量 deficit-transport 桥梁。

定性抛物 Liouville 障碍不依赖这一错误估计，因而仍然成立。

## 6. 正确的作用范围

可严格保留的命题是：

> 设 \(B\) 连通且抛物，某 Riemann 度量在 \(B\) 上具有精确自由等距 \(\mathbb R^N\)-作用的适配结构，\(N\ge1\)。若
> \[
> \operatorname{Ric}=-g
> \]
> 或更一般地
> \[
> \operatorname{Ric}=-g+E,\qquad
> \|g^{-1}E\|_{\mathrm{op}}<1,
> \]
> 并且 \(v=\sqrt{\det G}\) 在整个 \(B\) 上有界，则该结构不可能存在。闭圆周基底无需 \(v\) 有界假设。

它不排除：

- \(\mathrm{nil}^3\) 或其他非阿贝尔塌缩；
- 秩降和奇异纤维；
- 无端点渐近信息的区间基底；
- 非抛物基底；
- \(v\) 在穿孔处无界的情形；
- 仅近似等距的 \(N\)-结构。

对于 \(N=4\)、基底为一点的阿贝尔情形，正确理由是：自由传递的阿贝尔 \(\mathbb R^4\)-作用使度量为阿贝尔群上的左不变度量，故平坦，不能满足 \(\operatorname{Ric}=-g\)。不能以“一切四维局部齐性负 Einstein 度量不存在”为理由，因为负 Einstein 齐性空间确实可能存在；关键是作用群为阿贝尔。

## 7. Cheeger–Tian 对近 Einstein 序列的适用性

现有材料不足以证明所写的分解：

\[
\text{删去至多 } \mathcal N(\chi)
\text{ 个曲率爆破球后得到有界曲率塌缩和 Einstein groupoid 极限。}
\]

Cheeger–Tian 的相关四维曲率正则性依赖精确 Einstein 方程给出的椭圆曲率方程，示意为
\[
\nabla^*\nabla\operatorname{Rm}
 =\operatorname{Rm}*\operatorname{Rm}
  +\lambda\operatorname{Rm}.
\]
对于
\[
\operatorname{Ric}_{g_i}=-g_i+E_i
\]
则曲率方程还含有 \(\nabla^2E_i\) 等源项。假设
\[
\|E_i\|_{L^\infty}\to0
\]
并不控制这些导数，因此不能自动从小曲率能量推出点态曲率半径，亦不能直接获得 CFG 所需的有界截面曲率区域。

固定拓扑、Ricci 有界和 Chern–Gauss–Bonnet 可提供总 \(L^2\) 曲率预算，但这本身不足以推出：

- 只有有限个点态曲率集中球；
- 其余区域有统一曲率半径；
- 有界曲率塌缩结构；
- 光滑 Riemannian groupoid 收敛。

条件性地，若已独立得到局部 cover 上统一 harmonic radius 及强 \(W^{2,p}\) 紧性，则 harmonic-coordinate Ricci 方程确可将
\[
\operatorname{Ric}_{g_i}+g_i\to0
\]
传至极限，得到光滑
\[
\operatorname{Ric}_{g_\infty}=-g_\infty.
\]
但真正未解决的是如何由当前近 Einstein 假设产生这些正则 cover/groupoid 区域。

足以修补的额外输入可包括：

- 适用于 \(L^\infty\)-近 Einstein 四流形的 \(\varepsilon\)-正则性定理；
- 对 \(E_i\) 的尺度相容 \(W^{2,p}\)、\(C^{1,\alpha}\) 或导数控制；
- 独立证明正则区域的曲率半径下界；
- 或直接构造带统一 harmonic-radius 控制的局部非塌缩 covers。

## 最终判定

精确负 Einstein、自由阿贝尔、抛物且轨道体积有界时的局部 PDE 障碍是正确的；圆周基底结论也完全正确。近 Einstein 系数 \(N(1-\delta)\) 在“精确等距适配作用”条件下正确。

但当前 Step 7 尚不能推出所述 collapsed sequence 的整个正则区域不存在阿贝尔塌缩，因为仍缺：

1. 极限基底确为具有 polar 穿孔的抛物空间；
2. \(v\) 的全局上界；
3. 从近 Einstein 序列产生正则 Einstein groupoid 的合法紧性/正则性定理。

容量估计及依赖它的全部定量结论应视为已证伪。