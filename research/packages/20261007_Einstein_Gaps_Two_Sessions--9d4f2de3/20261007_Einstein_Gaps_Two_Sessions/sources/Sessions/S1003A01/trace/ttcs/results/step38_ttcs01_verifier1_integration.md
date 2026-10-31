# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 38,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "usable": true,
  "partial": false,
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step38_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S1003A01/trace/ttcs/results/step38_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Read the Step-37 exponential-chart construction, the new Step-38 curvature-conditioned response method and records, and the peer Step-42/43 mathematical notes. Check the scientific and numerical substance: (i) whether the residual weighting and SVD whitening really implement the Gauss–Newton norm for D(Ric+g); (ii) whether the positive congruence response has first variation h; (iii) whether the paired control-variate comparisons support the stated narrow conclusions, including the CH control and coarse-fit overfitting; (iv) whether any interpretation improperly promotes the fixed-bolt cap experiment into a cap infimum or lower theorem; and (v) how the Taubes period obstruction and Cotton/quadratic law should alter the global research direction. Give precise corrections and the strongest supportable mathematical interpretation, not procedural advice.

## Integrated Scientific Memo

# 核验结论

## 1. 残差加权正确，但“实现了 \(D(\mathrm{Ric}+g)[h]\) 的内禀 Gauss–Newton 范数”表述过强

令
\[
E(g)=\operatorname{Ric}(g)+g,\qquad g=LL^T.
\]
代码在每个求积点构造
\[
r_q(g)=
\left(\frac{w_q\sqrt{\det g}}{8\pi^2}\right)^{1/2}
\operatorname{vec}_{\rm sym}\!\left(L^{-1}EL^{-T}\right),
\]
其中非对角分量乘 \(\sqrt2\)。因此
\[
\left|\operatorname{vec}_{\rm sym}(L^{-1}EL^{-T})\right|^2
=|E|_g^2
\]
且
\[
\sum_q|r_q|^2
=\sum_q\frac{w_q}{8\pi^2}|E|_g^2\sqrt{\det g},
\]
确为 \(D(g)/(8\pi^2)\) 的离散求积。这里体积权重也是正确的：残差乘 \((\det g)^{1/4}\)，平方后得到 \(d\mu_g\)。

若
\[
J=Dr(0)=U\Sigma V^T,\qquad
T=V_{\rm keep}\Sigma_{\rm keep}^{-1},
\]
则
\[
JT=U_{\rm keep},\qquad T^TJ^TJT=I.
\]
所以代码确实白化了**所选节点上、以 Cholesky 残差表示的离散 Gauss–Newton 矩阵**，且
\[
y_{\rm GN}=-U_{\rm keep}^Tr_0,\qquad c_{\rm GN}=Ty_{\rm GN}
\]
是保留子空间中的线性最小二乘步。

但 \(J\) 并非只有 \(D E[h]\)。在非 Einstein 基点 \(E_0\neq0\) 时，
\[
Dr[h]
=
W_0^{1/2}\Phi_0(DE[h])
+W_0^{1/2}(D\Phi[h])E_0
+\frac14\operatorname{tr}_{g_0}h\,r_0,
\]
其中 \(\Phi_g(E)=L_g^{-1}EL_g^{-T}\)。后两项分别来自移动 Cholesky 标架和移动体积因子。因此：

* 当前 \(J^TJ\) 是完整加权残差映射的 GN 形式；
* 它一般不等于
  \[
  \int |D(\operatorname{Ric}+g)[h]|^2\,d\mu_{g_0};
  \]
* Cholesky 标架改成依赖 \(g\) 的另一正交标架时，目标值及梯度不变，但在 \(E_0\neq0\) 时 \(J^TJ\) 可因标架导数项而改变。

若要精确实现纯 Einstein 算子线性化的 Gram 形式，应冻结基点的标架和权重，只微分 \(E\)。Step-38 文本应改为：

> “白化所选离散加权残差映射在基点处的 Gauss–Newton 形式。”

而不应称为“内禀的 \(D(\operatorname{Ric}+g)[h]\) Gram 范数”。

两个现有记录均保留全部十个方向：CH 阈值约 \(1.37\times10^{-3}\)，最小奇异值 \(0.07344\)；粗 cap 阈值约 \(1.49\times10^{-3}\)，最小奇异值 \(0.1071\)。所以这些运行中 SVD 没有删除任何方向。由于 `ybound` 也未激活，一步结果实际上就是
\[
c=-J^+r_0.
\]
白化仍提供有用坐标和诊断，但本次结果的实质改进来自使用线性最小二乘/GN 步，而非截断或约束意义上的白化。

另有一个未决点：最弱奇异方向在两个记录中都强烈集中于 \((0,1)\) 非对角模态，并被 \(\Sigma^{-1}\) 放大；粗 cap 的最大系数 \(0.131\) 也来自该方向。它是否近似微分同胚方向，现有材料没有解决。故不能把最小奇异值直接解释为几何软模。

---

## 2. 正同余响应的一阶变分严格等于 \(h\)，但全域正定尚未证明

对于 \(h_t=t h\)，
\[
B_t=I+\frac t2g_0^{-1}h,
\]
有
\[
B_t^Tg_0B_t
=g_0+t h+\frac{t^2}{4}h\,g_0^{-1}h.
\]
故
\[
\left.\frac d{dt}\right|_{0}B_t^Tg_0B_t=h.
\]
这部分完全正确；二次项也为半正定。

严格正定的准确条件是 \(B_t\) 可逆，即
\[
-2/t\notin\operatorname{spec}(g_0^{-1}h),
\]
例如
\[
\left\|\frac t2g_0^{-1}h\right\|_{\rm op}<1
\]
是充分条件。“同余自动保持正定”应理解为“在 \(B\) 非奇异时”。JSON 中 `min_eig` 在所有验证点约为 \(0.11\)，支持采样点上的非退化，但不是整个连续环带上的证明。

响应在 \(r\le0.45\) 恒为零，因此确实保持一个完整 bolt 邻域及其中全部度量射流；同一事实也说明它完全不能检验 bolt 面积或 bolt-compatible 核心射流的调整。

---

## 3. 配对比较支持的结论很窄，但数值上是清楚的

### 3.1 CH 控制

在 `environment="ch"` 时，零响应基底就是 `gstar`，故代码中的 base 与 CH 逐点一致；JSON 也逐壳层验证了这一点。此时 `partial_cap_minus_ch` 实际应读作带内响应差
\[
\Delta_{\rm resp}
=\frac{D(g_{\rm resp})-D(g_*)}{8\pi^2}.
\]

记录给出：

\[
\|y_{\rm GN}\|\simeq6.60\times10^{-4},
\]
拟合节点上的变化为
\[
0.6805704457734092-0.6805708719900065
=-4.26217\times10^{-7},
\]
四个独立 scramble 的平均带内变化为
\[
\Delta_{\rm resp}
=(-5.8916\pm9.0960)\times10^{-7},
\]
其中“\(\pm\)”是重复间标准误，不是严格区间。

因此最强可支持结论是：

> 对一个固定径向 bump 乘十个对称张量分量，在当前离散化和精度下，未解析出 CH 认证单元的实质下降；投影梯度的尺度约为 \(10^{-4}\)–\(10^{-3}\)，作用量变化约为 \(10^{-6}\)。

这不是无限维驻定性、十维族中的严格极小性或真正 Hessian 非负性的证明。GN 二次型 \(J^TJ\) 必为半正定，不能检测真实 Hessian
\[
J^TJ+\sum_\nu r_\nu\nabla^2r_\nu
\]
中由非零基底残差产生的负方向。

### 3.2 粗 cap 拟合确实过拟合，而且失败局限在外壳层

粗记录每个拟合壳层只有 \(2^2=4\) 个点，共 12 点。拟合值从
\[
0.6866829990
\quad\hbox{降至}\quad
0.6767593469,
\]
即样本内变化
\[
-0.0099236521.
\]
独立配对验证却给出
\[
D(g_{\rm opt})-D(g_{\rm base})
=+0.00870249\pm0.00109277,
\]
三个重复均为正：
\[
0.00810,\quad0.01082,\quad0.00718.
\]
所以样本内下降、样本外上升的符号反转是明确的。它直接说明：曲率残差白化不能补偿空间欠采样。

更细地看，这并非方向处处错误。内两壳层合计变化稳定在约
\[
-0.0115,
\]
而最外层 \(0.597<r<0.78\) 增加约
\[
+0.019\text{--}0.022.
\]
因此该方向在 switching band 内部有真实局部下降，但外壳层未被四点拟合充分解析，导致净增加。这比笼统称作“完全虚假的下降”更准确。

代码字段 `response_improvement` 定义为
\[
D_{\rm opt}-D_{\rm base},
\]
所以正值表示变差，字段名容易造成相反理解。

验证后优化 cap 相对 CH 的带内差为
\[
0.05915\pm0.00709.
\]
减去响应增量，可还原未响应 cap 基底的平均带内差约
\[
0.05045,
\]
与 Step-37 的 \(0.047\)–\(0.057\) 一致。粗响应将其增大到约 \(0.059\)，并未消除。

这里有两个控制变量：

* 对响应差 \(D(g_{\rm opt})-D(g_{\rm base})\)，未修改 cap 基底是有效控制；
* 对 cap–CH 差，CH 对 switching anisotropy 的相关性较弱，方差消减有限。

壳层内部使用 `std/sqrt(n)` 把 Sobol 点当作独立样本，并不具有普通 Monte Carlo 标准误的严格解释。独立 scramble 间离散更合适，但只有三或四次重复，仍只是经验不确定度。

### 3.3 验证只覆盖响应带，不给出完整 cap 作用量

`cv_validate` 只积分
\[
0.45<r<0.78.
\]
因为响应在带外为零，它确实完整计算了
\[
D(g_{\rm opt})-D(g_{\rm base}).
\]
但 `partial_cap_minus_ch` 只是带内 cap–CH 差，不能把
\[
D_{\rm cert}+\texttt{partial\_cap\_minus\_ch}
\]
当作完整 cap 单元作用量。完整值还需加入 Step-37 全单元的带外 cap–CH 差。

脚本文档中的
\[
D_{\rm cap}(c)=D_{\rm cert}+\int(F_{\rm cap}-F_{\rm CH})
\]
只有积分覆盖整个单元时才成立。当前实现应明确写成 partial-band identity。

`CERT_D` 使用认证区间中点可用于浮点控制变量，但不能替代原认证区间
\[
[0.995670030344086,\ 0.995670030355131]
\]
参与严格组合。

### 3.4 精细 cap 运行不可核验

Step-38 笔记提到 `cap_band_gn1_fit32.json`，但该文件不在给定材料中。因此目前无法核验精细 cap 计算的步长、样本外变化、剩余 cap–CH 差、scramble 稳定性或正定性。现有 cap 结论只能基于粗记录，不能以文字中的“authoritative terminal record”替代数据。

---

## 4. Step-37/38 没有产生 cap 下确界或任何 lower theorem

Step-37 最可靠的构造结论是：将同一认证剖面通过不同的移植标记嵌入 cap，会产生非常不同的试验度量。Fermi 型标记给出约 \(1.916\)，中心指数型标记给出约 \(1.057\)。这说明先前约 \(0.9\) 的大代价主要是劣质移植标记造成的构造代价。

但这不是同一度量的被动坐标变换；\(L\) 在两个标记下进入移植公式，所得度量不同。因此“representation loss”或“纯坐标伪影”应改写为：

> Fermi 标记产生了远劣于中心法向标记的试验度量；该构造对标记高度敏感。

同样，Step-37 的 \(+0.010\) tail 只能称为：

> 未改变的认证剖面在该指数型标记、固定核心数据和固定环境中的正数值交互项。

它不是 cap 的“内禀 tariff”。对常数 \(W^-(p)\) 的一阶 \(SU(2)\) 配对消失有对称性依据，但“首个线性项必来自 \(\nabla^4W^-\)”尚需完整 jet 表示分解；当前数据更不确定其符号。响应松弛后的二阶环境系数可能包含 Schur-complement 型负修正，现有 `nang=1` 家族不足以决定它。

此外，Step-38 cap 记录使用 `nstep=16`，而 Step-37 的主要指数图检查用 64 步。JAX 精确微分离散 RK4 映射，因此拉回 Einstein cap 在局部微分同胚处仍然精确 Einstein；步数误差改变的是移植标记，而不是凭空产生背景 Einstein 残差。然而缺少 \(16,32,64,128\) 步的响应量收敛检查，故当前 cap 结果应称为“离散 RK4 标记下的实验”。

现有固定-bolt 家族固定了：

* \(x_0=0.03,\ X=128\) 剖面；
* bolt 面积和 bolt 邻域全部射流；
* 指数型移植标记；
* 一个径向 bump；
* `nang=1`，无真正角向响应；
* 一次基点 GN 方向及有限线搜索。

它没有检验 bolt 面积、核心射流、多径向尺度、角向 spin 模式、核心—collar 联合重优化、其他标记或其他拓扑实现。因此无论响应最终为正还是负，都不能推出 cap-cell infimum、环境普适符号或 Einstein-gap 下界。

还应保持局部泛函与全局场论量的区别：
\[
D=\int|\operatorname{Ric}+g|^2
=P+\frac14\int(s+4)^2\,d\mu,
\qquad
P=\int|\operatorname{Ric}^{\circ}|^2.
\]
只有 \(s\equiv-4\) 时 \(D=P\)。局部 cell 的 \(D\) 系数不能未经标量曲率控制直接转成闭流形的 \(P\) 定理。

---

## 5. Taubes 周期阻碍排除精确公共模态，但不产生定量 gap

在 Step-42 明列的假设下——\(b^+\ge2\)，且基本类为
\[
\pm K_X+\sum_i\pm E_i
\]
（模挠）——Taubes 论证成立。处处非零的自对偶调和二形式给出辛形式，且每个例外类满足
\[
|E_i\cdot[\omega]|>0.
\]
因此零例外周期迫使该自对偶调和形式出现零点；若某 \(E_i\) 的调和代表为反自对偶，则不存在处处非零的自对偶调和形式。

这排除了 Step-40 所设想的“闭、处处非零、对所有 \(E_i\) 零周期、且与符号无关”的精确 common mode。局部 perpendicular cell 与此不矛盾，因为其规范闭自对偶形式在 bolt 上退化；它属于零集分支，而不是闭流形上的 almost-Kähler 公共模态。

关键限制是：Taubes 只给出严格不实现性，不给出统一正代价。逼近序列仍可通过

1. 很小但正的例外面积 \(a_i\)，或
2. 自对偶调和形式的细零集/近零区

接近形式极值。因此它不能单独证明每次 blow-up 的统一 tariff。

Step-42 的
\[
C_+\ge\frac{\ell^2}{128\pi^2V}\Gamma(\theta),
\qquad
\Gamma(\theta)=3\theta^2-2\theta+1,
\]
应保留为 \(\ell\) 或 \((\eta+\alpha)\) 形式。一般 \(b^+>1\) 时不能推出 \(\eta\ge1\)；该结论只在额外 Lorentz/Hodge-index 假设 \(H_L\) 下成立。Taubes 给出 \(\alpha>0\)，却不给 \(\alpha\) 与 \(k\) 成比例的下界。

---

## 6. Cotton 计算支持的是条件二次尺度，而不是线性 Goldberg/Armstrong 定理

修正后的模型张量是
\[
W_0=a\left(\frac13I-n\otimes n\right),
\qquad a=\frac{\rho^2}{4}.
\]
在闭 almost-Kähler 一阶 jet 上，
\[
|\delta W_0|^2
=\frac{a^2}{2}|\nabla n|^2+\frac13|\nabla a|^2
=\frac{\rho^4}{32}|\nabla n|^2
+\frac13\left|d\!\left(\frac{\rho^2}{4}\right)\right|^2.
\]
这证明 \(\delta W_0\) 对允许的旋转一阶 jet 有非退化符号。但
\[
\delta W^+=C^+\sim\nabla\operatorname{Ric}^{\circ},
\]
而
\[
P=\int|\operatorname{Ric}^{\circ}|^2
\]
不控制该导数。积分分部后，还必须控制 \(\nabla^2n\)、\((\nabla n)^2\)、零集截断、Lee 分量、振幅梯度以及
\[
E=W^+-W_0.
\]
这些正是当前未闭合、并可能循环依赖于 saving 的逃逸项。

所以直接 Cotton–Cauchy–Schwarz 路线自然至多给出条件型
\[
R\lesssim(\sqrt P+\|E\|_2)\|\operatorname{Rm}\|_2,
\]
并在非循环控制 \(E\) 等项后导向
\[
P\gtrsim \frac{R^2}{A},
\]
而不是 \(P\gtrsim R\)。

若独立证明
\[
P\ge\frac{R^2}{\Lambda A},
\qquad
P\ge8\pi^2k-2R,
\]
则精确消元为
\[
P\ge
\left(\sqrt{\Lambda A+8\pi^2k}-\sqrt{\Lambda A}\right)^2
=
\frac{16\pi^4k^2}{\Lambda A}
+O\!\left(\frac{k^3}{A^2}\right).
\]
这是条件二次尺度，不是当前定理。

若 \(\Lambda\) 在有限覆盖下统一，且 \(k/A\) 固定，则该公式的每类系数也固定；它不会仅因取覆盖塔而趋零。沿覆盖塔出现每类系数消失，必须来自：

* \(k/A\to0\)，或
* \(\Lambda\) 因 \(E,\nabla a\)、零集项或谱常数而失去覆盖一致性。

线性估计
\[
P\ge\kappa R
\]
属于定量负标量 Goldberg/Armstrong 理论。当前 Cotton 符号计算不能推出它；较可信的线性机制仅是负 Kähler–Einstein 主体附近、去除规范和 Kähler 模空间后的扰动谱理论，而覆盖一致性仍是额外难点。

---

## 最强支持的整体解释

1. Step-38 正确离散了 \(D/(8\pi^2)\)，并白化了完整加权 Cholesky 残差映射的 GN 形式；它不是纯 \(D(\operatorname{Ric}+g)\) 的内禀 \(L^2\) Gram 范数。
2. 同余响应的一阶变分严格为 \(h\)；有限振幅严格正定还要求 \(B\) 全域可逆，目前仅有采样支持。
3. CH 控制只支持十个固定径向张量方向上未解析出下降，尺度约 \(10^{-6}\)；不支持无限维驻定性或 Hessian 稳定性。
4. 粗 cap 运行明确证明了空间欠采样：内带有约 \(-0.0115\) 的真实下降，外带出现约 \(+0.02\) 的漏拟合代价，净结果为 \(+0.0087\pm0.0011\)。
5. 指数型移植远优于 Fermi 型移植，但比较的是不同试验度量；固定剖面的 \(+0.010\) tail 不是 cap 的内禀收费。
6. 所给材料缺少精细 cap JSON，且所有响应都固定 bolt；不存在可核验的 cap infimum 或 lower theorem。
7. Taubes 阻碍排除了零例外周期的处处非零闭公共模态，却允许小例外面积或零集逼近，故没有定量 per-class gap。
8. Cotton 机制目前支持条件二次尺度 \(P\sim k^2/A\)。线性 tariff 需要额外的定量 Armstrong/Goldberg 或覆盖一致谱结构；不能从现有符号恒等式中宣称。