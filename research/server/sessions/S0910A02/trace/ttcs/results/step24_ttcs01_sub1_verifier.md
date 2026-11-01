# TTCS Independent Branch Record

```json
{
  "step_id": 24,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A02/workspace/notes/step24_all_dim_positive_collapse_architecture.md",
    "Sessions/S0910A02/workspace/data/step24_kk_circle_product_family_audit.json",
    "Sessions/S0910A02/workspace/notes/step6_positive_collapse_regularity_probes.md"
  ]
}
```

## Task

Verify the Step 24 Kaluza--Klein circle-collapse correction for the Yau-26 positive branch. Read the supplied note, Step-6 source calculation, and the JSON audit. Check whether the O'Neill/Kaluza--Klein equations stated there are internally consistent; whether the product base B=S^2_{Ric=2} x N^d_{Ric=1}, phi=sqrt(2) area_{S^2}, satisfies the exact Ric_M=g connection-metric equations for d>=2; whether the total space is correctly described as L(q,1) x N^d with q-dependent fiber scale and exact positive Einstein collapse; and whether the conclusion that the Step-6 Bochner obstruction is special to total dimension 4 (not all odd base dimensions) is mathematically justified. Identify any convention caveats, missing hypotheses, or stronger statements that should or should not be recorded. Do not decide the whole Yau-26 problem; focus on this KK correction and its implications for the positive-collapse route.

## Output

# 科学核验备忘录：Step 24 的圆纤维 Kaluza–Klein 修正

## 1. O’Neill/Kaluza–Klein 方程彼此一致

设主 \(S^1\)-丛的生成向量场 \(\xi\) 具有参数周期 \(2\pi\)，连接形式满足
\[
\alpha(\xi)=1,\qquad d\alpha=\pi^*F,
\]
且
\[
g_M=\pi^*g_B+t^2\alpha^2,\qquad t>0
\]
为常数。令 \(U=t^{-1}\xi\) 为单位竖直向量，并令
\[
\phi=tF,\qquad
(\phi\circ\phi)(X,Y)=\langle \iota_X\phi,\iota_Y\phi\rangle .
\]
采用
\[
|\phi|^2=\sum_{i<j}\phi_{ij}^2
\]
这一二形式范数后，所给公式为
\[
\begin{aligned}
\operatorname{Ric}_M(X,Y)
 &=\operatorname{Ric}_B(X,Y)-\frac12(\phi\circ\phi)(X,Y),\\
\operatorname{Ric}_M(U,U)&=\frac12|\phi|^2,\\
\operatorname{Ric}_M(X,U)&=\pm\frac12(d_B^*\phi)(X).
\end{aligned}
\]
这些系数与标准 O’Neill 张量
\[
A_XY=-\frac t2F(X,Y)U
\]
一致。特别地，
\[
\operatorname{Ric}_M=g_M
\]
等价于
\[
|\phi|^2=2,\qquad d_B^*\phi=0,\qquad
\operatorname{Ric}_B=g_B+\frac12\phi\circ\phi. \tag{1}
\]
另外 \(d\phi=0\) 来自 \(t\) 为常数以及 \(dF=0\)，并非 Einstein 方程额外产生的条件；把它与 (1) 合并书写没有数学问题，但其逻辑来源应予区分。

取迹也给出一致性验证：
\[
R_M=R_B-\frac12|\phi|^2.
\]
后面的乘积模型中 \(R_B=d+4\)、\(|\phi|^2=2\)，故 \(R_M=d+3=\dim M\)，正好对应 \(\operatorname{Ric}_M=g_M\)。

这些公式对应恒定纤维长度、主圆作用不变且纤维全测地的连接度量。若 \(t\) 随基点变化，竖直、水平和混合 Ricci 分量中会出现 \(\nabla t\)、\(\nabla^2t\) 等项，当前公式不能直接套用。

## 2. \(S^2\times N^d\) 乘积基底确实逐分量满足方程

令
\[
B=S^2\times N^d,\qquad
\operatorname{Ric}_{S^2}=2g_{S^2},\qquad
\operatorname{Ric}_N=g_N,
\]
并取 \(S^2\) 的面积形式 \(\omega\)。在二维正交标架下，
\[
|\omega|^2=1,\qquad
\omega\circ\omega=g_{S^2}.
\]
因此
\[
\phi=\sqrt2\,\omega
\]
满足
\[
|\phi|^2=2,\qquad
\frac12\phi\circ\phi=g_{S^2}\oplus0.
\]
而且 \(\omega\) 在乘积度量下平行，故
\[
d\phi=d_B^*\phi=0.
\]
最后，
\[
g_B+\frac12\phi\circ\phi
=(2g_{S^2})\oplus g_N
=\operatorname{Ric}_B.
\]
所以 (1) 全部成立。等价地，Ricci 特征值逐块为：

- \(S^2\) 水平方向：\(2-1=1\)；
- \(N\) 水平方向：\(1\)；
- 圆纤维方向：\(\frac12|\phi|^2=1\)；
- 混合分量：\(0\)。

因此对每个实际存在的闭 Einstein 流形 \(N^d\) 满足 \(\operatorname{Ric}_N=g_N\)，构造出的总空间度量严格满足
\[
\operatorname{Ric}_M=g_M.
\]

对于 \(d\ge2\)，至少可取适当缩放的圆球 \(N=S^d\)。Step-24 JSON 中 \(d=1\) 行的残差 \(-1\) 也正确：一维流形恒有 \(\operatorname{Ric}=0\)，而 \(\phi\) 在该方向上为零，所以这一方向的总空间 Ricci 仍为零。该行只验证了这个乘积选择在 \(d=1\) 时不成立；任意三维基底上的一般性排除来自 Step-6 的 Bochner 推导。

## 3. Chern 数、纤维尺度和总空间拓扑均正确

由 \(\operatorname{Ric}_{S^2}=2g_{S^2}\) 可知其 Gauss 曲率为 \(2\)，从而
\[
\operatorname{Area}(S^2)=2\pi,\qquad
\int_{S^2}\omega=2\pi.
\]
在周期 \(2\pi\) 的圆群约定下，
\[
c_1(P)=\left[\frac{F}{2\pi}\right].
\]
取
\[
F_q=q\omega,\qquad q\in\mathbb Z_{>0},
\]
便有
\[
\int_{S^2}F_q=2\pi q.
\]
为了得到 \(\phi=tF_q=\sqrt2\,\omega\)，必须且只需取
\[
t_q=\frac{\sqrt2}{q}.
\]
因此 JSON 中的 \(q\)-依赖尺度和 \(tF\) 的固定范数均正确。若 \(q<0\)，可取
\[
t_q=\frac{\sqrt2}{|q|},\qquad
\phi=\operatorname{sgn}(q)\sqrt2\,\omega;
\]
Ricci 方程不受符号影响。

若 Chern 类仅来自 \(S^2\) 因子，即
\[
c_1=q\,\operatorname{pr}_1^*[S^2],
\]
该主圆丛是 \(S^2\) 上 Euler 数为 \(q\) 的圆丛沿投影的拉回，因此
\[
P_q\cong L(q,1)\times N
\]
至多相差常用的定向约定；某些 lens-space 记号会写成 \(L(q,-1)\)，底层无定向光滑流形相同。

更直接地，度量写成
\[
g_{M,q}
=g_N+\pi^*g_{S^2}+\frac{2}{q^2}\alpha_q^2.
\]
其 \(L(q,1)\) 因子是半径 \(\sqrt2\) 的圆三维球面沿 Hopf 纤维作 \(\mathbb Z_q\) 商所得的圆度量，具有
\[
\sec=\frac12,\qquad \operatorname{Ric}=g.
\]
因而
\[
(L(q,1)\times N,\;g_{L(q,1)}+g_N)
\]
本身就是 Einstein 乘积，而不仅是由代数方程形式上得到的候选。

### 体积归一化的一处数据标注

纤维圆周长为
\[
2\pi t_q=\frac{2\pi\sqrt2}{q}.
\]
因此在上述周期约定下，
\[
\frac{\operatorname{Vol}(M_q)}{\operatorname{Vol}(B)}
=2\pi t_q,
\]
而不是字面上的 \(t_q\)。Step-24 JSON 的 `volume_factor_relative_to_base` 字段记录的是省略固定因子 \(2\pi\) 后的 \(q\)-依赖比例。由于同一 JSON 又记录了
\(\int F=2\pi q\)，若该字段意在表示实际几何体积比，应改为 \(2\pi t_q\)。

随着 \(q\to\infty\)，纤维直径为 \(O(q^{-1})\)，
\[
\operatorname{Vol}(M_q)\to0,
\]
且 Riemannian submersion
\[
M_q\longrightarrow S^2\times N
\]
给出 Gromov–Hausdorff 收敛。事实上这些度量局部等距于固定的
\[
S^3_{\sec=1/2}\times N,
\]
所以这是具有一致局部曲率控制的严格 Einstein 圆纤维塌缩。序列中的光滑流形随 \(q\) 改变；其基本群至少含有阶数 \(q\) 的 lens-space 因子。

## 4. Step-6 的三维基底 Bochner 机制确实不能推广到所有奇数维基底

在三维定向基底上，每个二形式都可写成
\[
\phi=*b
\]
其中 \(b\) 是一形式，并有
\[
\phi\circ\phi=|b|^2g_B-b\otimes b.
\]
由 \(d\phi=0\) 和 \(d_B^*\phi=0\) 得
\[
d_B^*b=0,\qquad db=0,
\]
故 \(b\) 是调和一形式。竖直方程给出 \(|b|^2=2\)，水平方程则给出
\[
\operatorname{Ric}_B
=2g_B-\frac12b\otimes b,
\qquad
\operatorname{Ric}_B(b,b)=|b|^2>0.
\]
这与闭基底上的一形式 Bochner 恒等式矛盾。若基底不可定向，可拉回到定向双覆盖后进行同一计算。

该推导真正使用了
\[
\Lambda^2T^*B\cong T^*B
\]
这一三维特性。较高奇数维中，一个二形式虽必有非平凡核，但核分布不会自动产生全局调和一形式。给出的乘积模型对此提供了严格反例：当基底维数
\[
m=d+2
\]
为任意奇数 \(m\ge5\) 时，可取奇数 \(d\ge3\) 及
\[
N=S^d_{\operatorname{Ric}=1}.
\]
此时 \(\phi=\sqrt2\omega_{S^2}\) 的核为 \(TN\)，但全部 KK 方程仍然成立。尤其在 \(m\ge5\) 时，试图用 \(*\phi^{(m-1)/2}\) 制造一形式也不起作用，因为这个秩二形式满足 \(\phi^2=0\)。

因此，数学上准确的表述是：

- Step-6 的 Hodge–Bochner 排除适用于三维基底，即四维总空间的恒长自由圆连接模型；
- 它不能推广成“所有奇数维基底均排除严格正 Einstein 圆塌缩”；
- 当前乘积族在总维数 \(n=3\)（取 \(N\) 为一点）以及每个 \(n\ge5\) 都给出严格 Einstein 圆塌缩；
- 总维数 \(n=2\) 也不能用该机制实现，因为一维基底上 \(F=0\)，竖直 Ricci 为零。因而若把所有 \(n\ge2\) 都纳入叙述，“四维是唯一没有该乘积族的维数”并不准确；更精确的是在 \(n\ge3\) 中，该族恰好跳过 \(n=4\)。

## 5. 对正号塌缩研究的严格含义

这组度量直接表明，在 \(n=3\) 及每个 \(n\ge5\) 中，即使
\[
\operatorname{Ric}=g
\]
完全成立，也不存在仅由这一归一化推出的维数统一体积下界或注入半径下界。因而任何以“紧 Ricci 夹逼自动排除塌缩”为前提的紧性论证都会被该族否定。

另一方面，这个族本身只说明一种非常清楚的 Einstein 商机制：
\[
M_q=(S^3_{\sec=1/2}\times N)/\mathbb Z_q.
\]
它没有给出所有正 Ricci 夹逼塌缩的分类，也没有推出任意塌缩拓扑必定承载 Einstein 度量。对于四维，它只排除了 Step-6 所处理的恒长自由主圆模型；变纤维长度、固定点轨道、奇异轨道以及曲率集中构型均不由这项计算处理。

总体而言，Step 24 的核心修正成立：乘积基底计算、Chern 数尺度、lens-space 总空间以及严格 Einstein 塌缩均正确；需要补上的主要文字细节是 \(2\pi\) 体积因子、\(q\) 的符号约定、\(d=0\) 给出的三维加强，以及“四维特殊性”应明确指向三维基底上的这一个 Bochner 机制。