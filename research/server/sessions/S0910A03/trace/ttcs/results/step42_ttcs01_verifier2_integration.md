# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 42,
  "task_field": "verifier",
  "task_index": 2,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step42_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step42_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Independently examine the terminal contradiction and the claimed full spectral calibration. There are two possible routes in the files: the explicit nonnegative LeBrun spectral density G=f²-(b_-)², and the positive-part rescaled-monopole harmonic form/eigenline density. Determine which route is actually sufficient once a smooth Einstein chart with s=-4 and |W+|²=1/24 is obtained. Verify algebraically that G=0 forces the calibrated spectrum under the stated eigenvalue ordering, and identify the regularity/convergence needed to pass ∫G→0 to the limit. In parallel, assess whether the positive-part monopole construction is proven in the session files or only generator/Codex-level material, and whether it should be removed from the load-bearing proof. Finally check the local Derdziński/projector contradiction constants and orientation. Ground the answer in the supplied files and do not assume weak W2p convergence passes curvature nonlinearities.

## Integrated Scientific Memo

# 终端谱校准核验结论

## 1. 应采用显式 LeBrun 密度 \(G\)；它已足以确定完整谱

设 \(W^+\colon\Lambda^+\to\Lambda^+\) 的有序特征值为
\[
\lambda_1\ge \lambda_2\ge w,\qquad
\lambda_1+\lambda_2+w=0,
\]
并记
\[
u=|W^+|,\qquad
\alpha=\sqrt{\frac23},
\]
\[
f=\frac23s-2\alpha u,\qquad
b=\frac23s+2w,\qquad
G=f^2-(b_-)^2,
\]
其中文件采用
\[
b_-=\min\{b,0\}.
\]

对任意迹零对称 \(3\times3\) 算子，
\[
u^2=w^2+\lambda_1^2+\lambda_2^2
\ge w^2+\frac{(\lambda_1+\lambda_2)^2}{2}
=\frac32w^2.
\]
最低特征值满足 \(w\le0\)，故
\[
-\sqrt{\frac23}u\le w\le0.
\]
令
\[
\xi=w+\alpha u,
\]
则 \(\xi\ge0\)，且
\[
b=f+2\xi.
\]

在极限图表上已有
\[
s=-4,\qquad u^2=\frac1{24},\qquad u=\frac1{2\sqrt6},
\]
因此
\[
\alpha u=\frac16,\qquad 0\le\xi\le\frac16,
\]
以及
\[
f=-3,\qquad b=-3+2\xi<0.
\]
于是
\[
G=9-(-3+2\xi)^2=4\xi(3-\xi).
\]
在 \([0,1/6]\) 上 \(3-\xi>0\)，所以
\[
G=0\iff \xi=0\iff w=-\frac16.
\]

其余两个特征值满足
\[
\lambda_1+\lambda_2=\frac16,
\qquad
\lambda_1^2+\lambda_2^2
=\frac1{24}-\frac1{36}=\frac1{72}.
\]
因而
\[
\lambda_1\lambda_2
=\frac{(1/6)^2-1/72}{2}
=\frac1{144},
\]
判别式为零，故
\[
\lambda_1=\lambda_2=\frac1{12}.
\]
最终
\[
\boxed{\operatorname{spec}(W^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right).}
\]

因此正确的逻辑次序是：

1. \((s+4)^2\to0\) 给出 \(s=-4\)；
2. \((s+8\sqrt6|W^+|)^2\to0\) 给出 \(|W^+|^2=1/24\)；
3. \(G\to0\) 再确定特征值分裂。

A01 Step 8、Step 28 和 Step 39 中的 \(G\)-路线已经包含终端谱校准所需的全部信息。无需在极限图表中重构单极子或谐和二形式。这里应区分：全局 LeBrun/Seiberg–Witten 不等式仍是校准估计的必要来源；冗余的是终端图表上的正部加权单极子/特征线构造。

## 2. \(\int G_i\to0\) 的极限传递必须使用强曲率收敛

弱 \(W^{2,p}\) 收敛本身不能传递 \(G\)。曲率含有二阶导数，而 \(G\) 对曲率是二次非线性的。Step 39 §7.2 中“曲率特征值对度量系数 Lipschitz，故弱极限满足校准”等表述不成立；特征值只是在固定识别后对曲率端omorphism Lipschitz，并不能把弱二阶导数收敛升级为非线性收敛。

在缩小后的公共坐标图上，以下任一条件足够：

* 正时间内部曲率导数估计所给出的光滑收敛；
* 强 \(C^1\) 加强 \(W^{2,2}_{\mathrm{loc}}\) 收敛；更方便地取强 \(W^{2,p}_{\mathrm{loc}}\), \(p>2\)。

事实上，
\[
\operatorname{Rm}(g_i)
=g_i^{-1}*\partial^2g_i
 +g_i^{-2}*\partial g_i*\partial g_i.
\]
强 \(C^1\) 和强 \(W^{2,2}\) 收敛蕴含
\[
\operatorname{Rm}(g_i)\to\operatorname{Rm}(g_\infty)
\quad\text{强收敛于 }L^2_{\mathrm{loc}}.
\]
固定图表方向后，\(\Lambda^+\) 的 Hodge 投影一致收敛，因此
\[
s_i\to s_\infty,\qquad
W_i^+\to W_\infty^+
\quad\text{强收敛于 }L^2.
\]
矩阵范数、最低特征值和 \(x\mapsto\min(x,0)\) 都是 Lipschitz 的，故
\[
f_i\to f_\infty,\qquad (b_i)_-\to(b_\infty)_-
\quad\text{强收敛于 }L^2,
\]
从而
\[
G_i\to G_\infty\quad\text{强收敛于 }L^1.
\]
于是局部 \(\int G_i\to0\) 给出 \(\int G_\infty=0\)。因 \(G_\infty\ge0\)，且 Einstein 极限经椭圆正则性为光滑度量，遂有
\[
G_\infty\equiv0.
\]

A01 Step 8 §5 所述谐和坐标机制可以提供所需的强收敛：若
\[
g_i\to g_\infty\quad\text{于 }C^{1,\beta},
\qquad
\operatorname{Ric}_{g_i}+g_i\to0
\quad\text{强于 }L^2\text{ 或 }L^\infty,
\]
则谐和坐标方程
\[
g_i^{ab}\partial_a\partial_b(g_i)_{jk}
=-2(\operatorname{Ric}_{g_i})_{jk}
 +Q_{jk}(g_i^{-1},\partial g_i)
\]
的右端强收敛。对差方程应用内部 \(W^{2,2}\) 估计并缩小图表，即得强 \(W^{2,2}\)；有一致曲率界时还可通过插值提高到有限 \(W^{2,p}\)。

在正时间流的拉回图表中，若较大 plateau buffer 上已有一致曲率导数界，则直接使用光滑收敛最简洁。无论采用哪种机制，都不能写成“弱 \(W^{2,p}\) 自动传递曲率非线性”。

另有一个几何细节：指数拉回平均要求从每个被平均中心发出的长度 \(\rho\) 径向测地线都留在有曲率控制的 buffer 中。若曲率界仅写在 \(B_{2r}(x_\alpha)\)，就不应在整个 \(B_{2r}(x_\alpha)\) 上选中心。可改在 \(B_r(x_\alpha)\) 上平均并取 \(\rho<r\)；Bishop–Gromov 比较仍保留统一比例的 plateau 体积。

## 3. 正部加权单极子路线不应作为承重步骤

其有限维终点代数是正确的。令
\[
\mathscr A=W^++\sqrt{\frac23}|W^+|I_{\Lambda^+}\ge0.
\]
若已有光滑极限二形式满足
\[
H_\infty\ne0,\qquad
\langle\mathscr A_\infty H_\infty,H_\infty\rangle=0,
\]
则正半定性给出
\[
\mathscr A_\infty H_\infty=0,
\]
故 \(H_\infty\) 位于最低特征线，最低特征值为
\[
-\sqrt{\frac23}|W^+|=-\frac16.
\]
再由迹与范数即得其余两个特征值均为 \(1/12\)。

但在所给会话文件中，这条路线尚未形成完整、自包含的分析定理：

* `quantitative_deficit_analysis.md` 给出了细致的形式恒等式和缺陷分解，但若干关键恒等式是从“保留单极子证明中所有被丢弃项”得到的陈述，并未从源定理逐行重建。
* Step 16 明确说明相关脚本只核验有限维代数，不核验正权重重标度单极子解的存在性，也不核验图表极限。
* \(f^2\approx q^++\varepsilon\) 的光滑正则化、每个权重对应解的存在、一致估计及对角选择，未在所给材料中组装为完整证明。
* 把谐和形式传到图表极限还需要局部强收敛和 Hodge 椭圆估计。
* 特征线密度的积分控制必须覆盖从 \(P_i\) 发出的全部半径 \(\rho\) buffer，而不能只写在中心集合 \(P_i\) 上。
* Step 29 真正使用的是
  \[
  A_\rho\mathfrak D(p_i)\lesssim Q_i/A_i,
  \]
  而不是仅由 \(Q_i/(8\pi^2)\le\varepsilon\) 得到一个与 \(A_i\) 无关的 \(C\varepsilon\)。
* \(\mathscr A\) 严格说是正半定端omorphism，并非先验“projector”；只有在校准谱已知后，它才是相应正交投影的常数倍。

故终端承重证明应删除谐和形式振幅和特征线密度，只保留
\[
|E|^2+(s+4)^2+(s+8\sqrt6|W^+|)^2+G.
\]
正部单极子构造可保留为辅助性或探索性替代路线，但不应作为当前证明依赖。

## 4. Derdziński 与直接 projector 矛盾的常数和方向均正确

Einstein 性给出
\[
\delta W^+=0.
\]
对已校准谱，Derdziński 因子为
\[
(24|W^+|^2)^{1/3}
=(24\cdot\tfrac1{24})^{1/3}=1.
\]
所引 Proposition 5 给出的 Kähler 方向正是预先选定、定义 \(W^+\) 的方向，因此原极限度量本身局部 Kähler。对复方向下的 Kähler 四维度量，
\[
\operatorname{spec}(W^+)
=\left(\frac{s}{6},-\frac{s}{12},-\frac{s}{12}\right),
\qquad
|W^+|^2=\frac{s^2}{24}.
\]
当 \(s=-4\) 时，
\[
\operatorname{spec}(W^+)
=\left(-\frac23,\frac13,\frac13\right),
\qquad
|W^+|^2=\frac23,
\]
与校准值 \(1/24\) 矛盾。该 Kähler 范数闭合不依赖 Weyl 三次项常数，宜作为主矛盾。

直接 projector 证明也一致。若
\[
W^+=\mu I+(\lambda-\mu)P_\omega
\]
且两个不同特征值均为常数，则 \(\delta W^+=0\) 给出
\[
(\nabla^a\omega_{ab})\omega_{cd}
+\omega_{ab}\nabla^a\omega_{cd}=0.
\]
与 \(\omega^{cd}\) 收缩并使用 \(|\omega|\) 常数，得到
\[
\nabla^a\omega_{ab}=0.
\]
代回后
\[
\omega_{ab}\nabla^a\omega_{cd}=0.
\]
非零自对偶二形式在四维非退化，因此
\[
\nabla\omega=0,\qquad \nabla W^+=0.
\]

另一方面，
\[
\det W^+
=\left(-\frac16\right)\left(\frac1{12}\right)^2
=-\frac1{864}.
\]
采用文件中的 Einstein–Weyl 标量恒等式
\[
\Delta|W^+|^2
=2|\nabla W^+|^2+s|W^+|^2-36\det W^+,
\]
以及 \(|W^+|^2\equiv1/24\)，有
\[
0
=2|\nabla W^+|^2-\frac16+\frac1{24}
=2|\nabla W^+|^2-\frac18,
\]
故
\[
|\nabla W^+|^2=\frac1{16},
\]
与 \(\nabla W^+=0\) 矛盾。所有数值均相容。

## 5. 经核验的最小终端链

承重终端论证应写为
\[
\int\!\left[
|E_i|^2+(s_i+4)^2+
(s_i+8\sqrt6|W_i^+|)^2+G_i
\right]\to0
\]
\[
\Downarrow\quad
\text{指数拉回选择和强曲率收敛}
\]
\[
\operatorname{Ric}_{g_\infty}=-g_\infty,\quad
s_\infty=-4,\quad
|W_\infty^+|^2=\frac1{24},\quad
G_\infty=0
\]
\[
\Downarrow\quad
\operatorname{spec}(W_\infty^+)
=\left(-\frac16,\frac1{12},\frac1{12}\right)
\]
\[
\Downarrow\quad
\text{Derdziński 因子为 \(1\)，故局部 Kähler}
\]
\[
\Downarrow\quad
|W_\infty^+|^2=\frac{s_\infty^2}{24}=\frac23,
\]
与 \(1/24\) 矛盾。

这个终端模块在其明确假设下成立。它仍依赖上游尚属条件性的输出：统一正体积 plateau、完整 buffer 上的统一曲率控制、\(Q_i(T)/A_i\to0\)，以及足以产生强 \(W^{2,2}\) 或光滑图表收敛的正则性。