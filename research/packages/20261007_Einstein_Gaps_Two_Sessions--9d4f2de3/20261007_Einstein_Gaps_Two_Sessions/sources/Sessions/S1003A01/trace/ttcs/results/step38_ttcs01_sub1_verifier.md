# TTCS Independent Branch Record

```json
{
  "step_id": 38,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/scripts/step38_expmap_gn_response.py",
    "Sessions/S1003A01/workspace/notes/step38_curvature_conditioned_cap_response.md",
    "Sessions/S1003A01/workspace/notes/step37_cap_congruence_transport.md",
    "Sessions/S1003A01/workspace/data/step38/ch_band_gn1_fit32.json",
    "Sessions/S1003A01/workspace/data/step38/cap_band_gn1_cv.json",
    "Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md",
    "Sessions/S1003A02/workspace/notes/step43_w0_cotton_quadratic_law_and_debts.md"
  ]
}
```

## Task

Read the Step-37 exponential-chart construction, the new Step-38 curvature-conditioned response method and records, and the peer Step-42/43 mathematical notes. Check the scientific and numerical substance: (i) whether the residual weighting and SVD whitening really implement the Gauss–Newton norm for D(Ric+g); (ii) whether the positive congruence response has first variation h; (iii) whether the paired control-variate comparisons support the stated narrow conclusions, including the CH control and coarse-fit overfitting; (iv) whether any interpretation improperly promotes the fixed-bolt cap experiment into a cap infimum or lower theorem; and (v) how the Taubes period obstruction and Cotton/quadratic law should alter the global research direction. Give precise corrections and the strongest supportable mathematical interpretation, not procedural advice.

## Output

# 科学核验备忘录

## 1. 残差、积分权重与 SVD 白化

在拟合节点 \(x_q\) 上，脚本实际构造的是
\[
r_q(c)=
\left(\frac{w_q\sqrt{\det g_c(x_q)}}{8\pi^2}\right)^{1/2}
\operatorname{vec}_{\mathrm{sym}}
\!\left(L_c^{-1}E_cL_c^{-T}\right),
\qquad
E_c=\operatorname{Ric}(g_c)+g_c,
\]
其中 \(g_c=L_cL_c^T\)，而 `vec_sym` 对非对角分量乘 \(\sqrt2\)。因此
\[
\left|\operatorname{vec}_{\mathrm{sym}}
(L^{-1}EL^{-T})\right|^2
=
|E|_g^2
\]
且
\[
\sum_q |r_q(c)|^2
=
\sum_q\frac{w_q}{8\pi^2}
|E_c(x_q)|_{g_c}^2\sqrt{\det g_c(x_q)}.
\]
只要 `qmc_annulus` 按其设计对欧氏环带均匀取样，这正是
\[
\frac1{8\pi^2}\int |\operatorname{Ric}(g_c)+g_c|^2\,d\mu_{g_c}
\]
的离散求积。体积因子也正确：残差乘子是 \((\sqrt{\det g})^{1/2}=(\det g)^{1/4}\)，平方后恢复 \(d\mu_g\)。

令 \(J=Dr(0)\)，薄 SVD 为
\[
J=U\Sigma V^T,\qquad T=V_{\rm keep}\Sigma_{\rm keep}^{-1}.
\]
于是
\[
JT=U_{\rm keep},\qquad
T^TJ^TJT=I.
\]
所以 \(y\mapsto c=Ty\) 确实把**选定节点、选定残差表示、基点 \(c=0\)**处的 Gauss–Newton 二次型白化。线性最小二乘步
\[
y_{\rm GN}=-U_{\rm keep}^Tr(0)
\]
也与代码中的 `pred` 完全一致。

这里有三点需要精确改写。

1. \(J\) 不只是
   \[
   D_g(\operatorname{Ric}+g)[h].
   \]
   因为 \(E_0\neq0\)，它还包含正交标架和体积权重的变化：
   \[
   D(L^{-1}EL^{-T})[h]
   =
   L^{-1}D E[h]L^{-T}
   +\text{含 }E_0\,D L[h]\text{ 的项},
   \]
   残差体积乘子还贡献
   \[
   \frac14\operatorname{tr}_{g_0}(h)\,r_0.
   \]
   只有在 \(E_0=0\) 时，才退化为纯粹的
   \(\int|D(\operatorname{Ric}+g)[h]|^2d\mu_g\)。

2. 基点不是 Einstein 时，Gauss–Newton 矩阵依赖残差的平方根分解。Cholesky 标架换成另一个随 \(g\) 变化的正交标架，标量目标不变，但 \(J^TJ\) 一般会变，因为标架导数乘上了非零的 \(E_0\)。因此最准确的表述是：

   > 代码白化了所选 Cholesky 标架残差的离散 Gauss–Newton 矩阵。

   “内禀的 \(D(\operatorname{Ric}+g)[h]\) Gram 范数”则过强。

3. 两个给出的记录均保留了全部十个方向。CH 的最小奇异值为 \(0.07344\)，阈值约 \(1.37\times10^{-3}\)；粗 cap 的最小奇异值为 \(0.1071\)，阈值约 \(1.49\times10^{-3}\)。所以这些运行中 SVD 实施了白化，但没有实际删去方向。

这些修正不削弱其数值预条件作用：它确实把原坐标中约 \(10^2\) 的奇异值比消除了，并给出合法的一步离散 Gauss–Newton 搜索。

---

## 2. 正定同余响应及其一阶变分

对一参数 \(h_t=t h\)，
\[
B_t=I+\frac t2g_0^{-1}h,
\qquad
g_t=B_t^Tg_0B_t.
\]
直接展开得
\[
g_t
=
g_0+t h+\frac{t^2}{4}h\,g_0^{-1}h,
\]
因此
\[
\left.\frac{d}{dt}\right|_{t=0}g_t=h.
\]
这一部分完全正确。

有限振幅时应加上
\[
\det B_t\neq0.
\]
同余给出半正定张量，而严格正定等价于 \(B_t\) 可逆；写成同余本身并不自动排除 \(B_t\) 奇异。一个充分条件是
\[
\left\|\frac12g_0^{-1}h\right\|_{\mathrm{op}}<1.
\]
代码没有给出全环带上的解析估计。记录中的采样 `min_eig` 均为正：CH 各重复约 \(0.1115\)–\(0.1159\)，粗 cap 约 \(0.1136\)–\(0.1142\)。这说明采样点没有出现退化，但不是连续区域上的证明。

由于响应在 \(r\le0.45\) 恒为零，它确实保持整个 bolt 邻域及其中所有度量射流不变；这也正是它无法探测 bolt 面积和 bolt-compatible 核心射流的原因。

---

## 3. 配对控制变量与数值记录

### 3.1 CH 控制

在 `environment="ch"` 时，零系数度量就是 `gstar`，所以代码中的 \(C\) 与 \(B\) 逐点相同。JSON 中每个壳层的 `base` 与 `ch` 也完全一致。此时
`partial_cap_minus_ch` 这个字段名并不贴切；它实际就是
\[
\Delta_{\rm resp}
=
\frac{D(g_{\rm resp})-D(g_*)}{8\pi^2}
\]
在响应带中的值。

`ch_band_gn1_fit32.json` 给出：

- 投影 Gauss–Newton 步长
  \[
  \|y_{\rm GN}\|\simeq6.60\times10^{-4};
  \]
- 拟合节点上的变化
  \[
  0.6805704457734092-0.6805708719900065
  =-4.26217\times10^{-7};
  \]
- 四个独立随机扰动 Sobol 重复上的平均变化
  \[
  \Delta_{\rm resp}
  =(-5.8916\pm9.0960)\times10^{-7}.
  \]

四个重复分别约为
\[
4.85\times10^{-7},\quad
3.73\times10^{-7},\quad
-3.31\times10^{-6},\quad
9.24\times10^{-8}.
\]
因此没有解析出非零下降。最强可用解释是：

> 对一个固定径向 bump、十个对称张量分量以及当前求积精度，CH 认证单元的残差与这些线性化方向几乎正交。

这不是任意紧支撑变分下的驻定性，也不是十维族中精确极小性的证明。

### 3.2 粗 cap 拟合的样本外符号反转

`cap_band_gn1_cv.json` 每个拟合壳层只有四个空间节点。离散拟合值从
\[
0.6866829990
\quad\hbox{降到}\quad
0.6767593469,
\]
即拟合节点上的变化为
\[
-0.0099236521.
\]
但独立随机扰动验证给出
\[
\Delta_{\rm resp}
=
+0.00870249\pm0.00109277,
\]
三个重复分别为
\[
+0.00810176,\qquad
+0.01082269,\qquad
+0.00718301.
\]
因此样本外符号一致地反转。这个记录充分支持“每壳四点不足以确定该高杠杆方向”；曲率白化修复了系数尺度，却不能替代空间分辨率。

验证后的优化 cap 相对 CH 的带内差为
\[
0.0591498\pm0.007089.
\]
从每个重复中减去响应变化，可恢复未响应 cap 基底的带内差：
\[
0.0433490,\quad0.0418662,\quad0.0661267,
\]
平均约
\[
0.0504473\pm0.00785.
\]
所以粗响应把该带内差从约 \(0.0504\) 推到了约 \(0.0591\)，而不是消除了它。

字段 `response_improvement` 的符号命名容易误读：代码定义的是
\[
D_{\rm opt}-D_{\rm base}.
\]
正值表示作用量增加，负值才表示下降。

### 3.3 统计解释

每个壳层内部的
```python
diff.std(ddof=1)/sqrt(n)
```
把 Sobol 点按独立同分布样本处理；随机化 Sobol 点之间并非独立，因此这些壳层内数值不能直接当作普通 Monte Carlo 标准误差。独立 scramble 之间的经验离散更适合描述 RQMC 不确定度，但这里分别只有三次和四次重复，正态区间解释没有充分支持。Step-38 笔记把所报“\(\pm\)”明确解释为重复间标准误差，这一点是合适的。

### 3.4 控制变量只积分了响应带

`cv_validate` 只计算 \(0.45<r<0.78\)。因为响应在该带外恒为零，
\[
D(g_{\rm opt})-D(g_{\rm base})
\]
确实可由这段积分完整得到。但
\[
D(g_{\rm opt})-D(g_{\rm CH})
\]
还包含该带外未修改 cap 基底与 CH 单元之间的差。因此不能把
\[
D_{\rm cert}+\text{`partial_cap_minus_ch'}
\]
当成完整 cap 总作用量。完整重建需要 Step-37 的全单元 cap–CH 差，再加带内响应变化。

`cert_reference` 使用认证区间中点。浮点比较中这无实际影响，但若与认证结果组合，仍应保留原区间
\[
[0.995670030344086,\ 0.995670030355131]
\]
而不是把中点写成精确值。

### 3.5 尚未提供的精细 cap 记录

Step-38 笔记提到 `cap_band_gn1_fit32.json`，但给出的材料中没有该 JSON。因此无法核对精细 cap 拟合的：

- 白化步长；
- 样本外响应变化；
- 剩余带内 cap–CH 差；
- scramble 间稳定性；
- 采样正定性。

现有 cap 数值结论只能来自粗记录，不能由文字说明替代。

---

## 4. Step-37 指数标记的科学含义

Step-37 的核心进展是真实的：用中心点的法向坐标识别代替 divisor 的 Fermi 型识别后，同一个 CH 单元剖面所生成的 cap 移植度量从约 \(1.916\) 降至约 \(1.057\)。这说明先前约 \(0.9\) 的大额外作用量主要来自移植识别，而不是 cap 曲率本身。

但 \(D\) 对固定度量在坐标变换下不变，因此 \(1.916\to1.057\) 不是对同一度量做被动换坐标。Fermi 与指数识别进入了同余移植公式，生成的是两个不同度量。更准确的解释是：

> 该构造对移植标记高度敏感；中心法向标记产生了远低于 Fermi 标记的试验度量。

“内禀尾部作用 \(+0.010\)”也应理解为：

> 未改变的认证剖面，在这一指数型标记和这一固定核心数据下，与 cap 环境相互作用所得的数值。

它不是 cap 环境对所有单元的固有收费。

有限步 RK4 产生的是一个平滑的离散流映射；只要其微分可逆，拉回精确 Einstein cap 仍是 Einstein 度量，只是标记并非精确指数映射。Step-37 的 \(64\) 步 Gauss 引理和 CH 对照支持其接近指数标记，但采样到的正 Jacobian 只能说明采样点没有发现共轭现象或退化，不能建立整个半径 \(7.645\) 球上的全局单射性。Step-38 的 cap 粗记录使用 `nstep=16`，而材料中没有 \(16,32,64,128\) 步的作用量收敛比较；因此它目前是离散 RK4 标记下的响应实验。

另外，Step-37 在 Fermi 构造上使用的 350 模态不能与 Step-38 指数构造的十模态合并解释，因为基底度量和移植识别均已改变。指数标记下目前实际验证的只有一个径向 bump 乘十个张量分量。

---

## 5. 固定 bolt 实验没有给出 cap 下确界或全局下界

现有实验固定了：

- 认证单元的 \(x_0=0.03,\ X=128\) 剖面；
- bolt 面积和 bolt 邻域射流；
- 指数标记；
- 一个固定径向 bump；
- `nang=1`，即没有角向响应；
- 一次基点 Gauss–Newton 步及有限线搜索。

所以即使精细十模态响应仍显示作用量增加，也只能描述这个有限维固定-bolt 族。它没有计算 cap-cell 下确界，也没有排除：

- bolt 面积变化；
- bolt-compatible 核心射流；
- 多径向尺度；
- 真正角向模态；
- 核心与长 collar 的联合调整；
- 不同的拓扑或闭流形实现。

Step-37/38 笔记总体上已经明确区分了这些层次。需要收紧的只是“几何上正确标记”“内禀 tail”等措辞；“中心法向标记下的固定剖面数值”更准确。常数 \(W^-(p)\) 的一阶 \(SU(2)\) 配对消失有表示论依据，但“首个线性项必在 \(\nabla^4W^-\)”需要完整的 jet 分解才能成为定理；现有代码与数据只支持常数 spin-2 分量的平均消失。

---

## 6. Taubes 周期阻碍对全局解释的改变

在 Step-42 明列的前提下——\(b^+\ge2\)，且基本类恰为
\[
\pm K_X+\sum_i\pm E_i
\]
（模挠）——Taubes 论证是成立的。若自对偶调和二形式 \(\omega\) 处处非零，则它是辛形式，并且每个例外类满足
\[
|E_i\cdot[\omega]|>0.
\]
因而零例外周期迫使 \(\omega\) 有零点。若 \(E_i\) 的调和代表是反自对偶的，则任一自对偶调和形式与 \(E_i\) 的周期为零，所以不存在处处非零的自对偶调和形式。

这与局部单元并不矛盾：局部对称模型中的闭自对偶形式在 bolt 上退化。它不是闭流形上处处非零、零例外周期的 almost-Kähler 公共模态。

Taubes 结果是拓扑上的严格非实现性，却没有给出统一正数代价。例外面积可以趋于零，或者调和形式可以通过细小零集实现拓扑要求。因此它排除了 Step-40 的精确公共模态，却仍允许逼近序列靠近该形式。

Step-42 的 AK\(\Gamma\) 公式本身
\[
C_+\ge
\frac{\ell^2}{128\pi^2V}\Gamma(\theta),
\qquad
\Gamma(\theta)=3\theta^2-2\theta+1,
\]
以及
\[
\frac{\ell^2}{128\pi^2V}
=A(\eta+\alpha)^2
\]
是正确的。需要保持文本一致的是：在 \(b^+>1\) 时不能一般推出 \(\eta\ge1\)。无附加 Hodge/Lorentz 型假设时，证明应在 \(\ell\)-形式或 \((\eta+\alpha)\)-形式停止；逆 Cauchy–Schwarz 只属于附加假设下的推论。Taubes 只给出 \(\alpha>0\)，不提供与 \(k\) 成比例的统一下界。

---

## 7. Cotton 符号与二次尺度

Step-43 的符号公式
\[
W_0=a\left(\frac13I-n\otimes n\right),
\qquad a=\frac{\rho^2}{4},
\]
以及闭 almost-Kähler 一阶 jet 上
\[
|\delta W_0|^2
=
\frac{a^2}{2}|\nabla n|^2
+\frac13|\nabla a|^2
=
\frac{\rho^4}{32}|\nabla n|^2
+\frac13|d(\rho^2/4)|^2
\]
与 Step-38 摘要一致。它说明 \(\delta W_0\) 对 almost-Kähler 旋转方向具有非退化符号。

但
\[
\delta W^+=C^+\sim\nabla\operatorname{Ric}^{\circ}
\]
含有 Ricci 的导数，而
\[
P=\int|\operatorname{Ric}^{\circ}|^2
\]
不控制该导数。积分分部后只能得到形如
\[
R\lesssim
\bigl(\sqrt P+\|E\|_2\bigr)\|\operatorname{Rm}\|_2
\]
的关系，还需二阶 \(n\) 估计、振幅项、零集截断项以及
\(E=W^+-W_0\) 的非循环控制。因此 Cotton 路线本身自然产生
\[
P\gtrsim \frac{R^2}{A},
\]
而不是
\[
P\gtrsim R.
\]

若独立得到
\[
P\ge \frac{R^2}{\Lambda A},
\qquad
P\ge8\pi^2k-2R,
\]
则精确消元给出
\[
P\ge
\left(\sqrt{\Lambda A+8\pi^2k}
-\sqrt{\Lambda A}\right)^2
=
\frac{16\pi^4k^2}{\Lambda A}
+O(k^3/A^2).
\]
这是一条条件二次尺度。线性 \(P\ge\kappa R\) 则属于定量 Armstrong/Goldberg 型结果，不能从当前 Bianchi–Cotton 计算直接推出；在 Kähler–Einstein 主体附近的谱理论中它可能成立，但有限覆盖上一致常数仍是额外数学内容。

还应注意，局部数值泛函与全局场论中的 \(P\) 满足
\[
|\operatorname{Ric}+g|^2
=
|\operatorname{Ric}^{\circ}|^2+\frac{(s+4)^2}{4},
\]
故
\[
D=P+\frac14\int(s+4)^2d\mu.
\]
只有在 \(s\equiv-4\) 时二者相同。将局部 cell 的 \(D\) 系数转成闭流形的 \(P\) 结论，还需要同时控制标量曲率项。

---

## 最强可支持的综合解释

1. Step-38 正确实现了一个离散非线性最小二乘问题及其 Cholesky 残差的 Gauss–Newton 白化；它不是纯线性化 Einstein 算子的内禀 \(L^2\) Gram 形式。
2. 同余响应的一阶变分严格等于 \(h\)；有限振幅正定还需 \(B\) 可逆，当前只有采样证据。
3. CH 记录支持十个固定径向张量方向上的投影梯度约为零，精度约 \(10^{-6}\)；不推出无限维驻定性。
4. 粗 cap 记录明确显示空间欠采样造成样本内下降、样本外上升。所述精细 cap 结果尚无数据可核对。
5. Step-37 说明指数型移植识别比 Fermi 型识别优越得多；约 \(+0.010\) 的 tail 值只属于未改变剖面和该标记。
6. 固定 bolt 十模态实验没有给出 cap 下确界、环境普适符号或 Einstein gap 下界。
7. Taubes 排除了零例外周期、处处非零的闭公共模态，却没有提供定量代价；逼近序列仍可通过小例外面积或零集接近形式极值。
8. Cotton 机制支持条件二次尺度 \(P\sim R^2/A\)。线性 per-class 代价需要额外的定量 Armstrong/Goldberg 或覆盖一致谱结构，而不是当前局部符号计算的推论。