# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 76,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step76_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A02/trace/ttcs/results/step76_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the Step-76 Preceptor audit before the next mixed-row Green computation is built. Focus on the scientific correctness of four gates: (1) Ozuch's \bar h^4 singular asymptotic is a source/self-node issue and inter-node expansions at other A1 points are regular second-jet extractions; (2) on a product background the P-Green/resolvent separates with additive spectral denominators (or heat-kernel integral) and is not a literal product of two static S^2 Green functions, so adjacent coincident-in-one-factor pairs must be treated in the full product resolvent or a justified massive one-factor reduction; (3) the T^2 pole selection rule restricts characters but does not truncate spherical degree l; (4) the D8 reduction, working diagonal=spin identification caveat, scalar full-gauged kernel slice requirement, and Yau-26 scope statements are faithful. Identify any overclaims, missing tensor/operator convention issues, or a better completion criterion for the next diagonal r=2 calibration computation.

## Integrated Scientific Memo

# Step‑76 核验结论

四个 gate 的核心方向均成立，但审计稿还不能原样作为下一次计算的规范：必须修正热核表示、明确 full-\(P\) 伪逆及零模投影，并重新命名所计算的 inter-node 系数。特别是，正则 inter-node 二阶 jet 一般不是 Ozuch 记号中的局部 \(\mu\)。

## 1. 源点奇异性与异节点正则性

Ozuch Proposition 2.10 对指定源点 \(p_i\) 构造
\[
P_o\bar h_i^4
 =\sum_l\nu_{i,l}v_l+\sum_k\lambda_{i,k}\bar o_{i,k}^4,
\qquad
\bar h_i^4
 =H^4(\zeta_i)+H_{i,2}^4+O(r_i^{-\varepsilon}),
\]
并要求 \(\bar h_i^4\perp\mathbf O(g_o)\)。因此 \(r^{-4}\) 奇异渐近确实只属于 source/self node。

若 \(j\ne i\)，则 \(\bar h_i^4\) 在 \(p_j\) 的局部统一化覆盖上光滑；由于 \(A_1\) 作用为 \(x\mapsto-x\)，奇数 Taylor 项消失：
\[
\bar h_i^4
 =H_{ji,0}+H_{ji,2}+O(r_j^4).
\]
Ozuch 在 torus 模型中的
\[
\sum_{i'\ne i}\bar h_{i'}^4
 =H_0(i)+H_2(i)+O(d(i,\cdot)^4)
\]
正是这一结构的实例。故：

- self term 需要奇异渐近、通量归一化和 renormalization；
- \(i\ne j\) 的 receiver 不减任何 \(r^{-4}\) 项；
- 同时存在所有 sources 时，必须先将 receiver 自己的 self term 与其他节点的 regular terms 分开。

不过 \(H_{ji,0}\) 不能简单“归零后遗忘”。应取线性映射
\[
\psi_{ji}^{*}e=e+H_{ji,0},
\]
再在相应标架中读取 \(\psi_{ji*}(H_{j,2}^{\rm base}+H_{ji,2})\) 所诱导的曲率变化。产品背景曲率非零，所以常数项引起的标架变化可能与二阶 jet 对 obstruction 的贡献同阶。

另外，Ozuch 的显式格点 periodization 是平坦 torus 特有的；在 \(S^2\times S^2\) 商空间上应使用紧致 orbifold Fredholm/Green 构造，不能照搬格点公式。

## 2. 产品算子与 Green/resolvent

固定 Ozuch 约定
\[
P=\frac12\nabla^*\nabla-\mathring R,\qquad \Delta_E=2P.
\]
Kröncke 的产品谱分解表明，不同张量块的本征值均为因子谱之和。例如
\[
P(h_1f_2)
 =(P_1h_1)f_2+\frac12h_1\Delta_0^{(2)}f_2,
\]
混合块则涉及两个 connection Laplacian 的和。有限维张量分量对角化后，分母具有
\[
\frac1{\alpha_{a,l_1}+\beta_{b,l_2}},
\]
或等价的“两个谱值之和加代数曲率位移”形式，而非
\[
\frac{C}{(\lambda_{l_1}+a)(\lambda_{l_2}+b)}.
\]
因此 Step‑76 对静态一因子 Green 核乘积的否定是正确的。

### 必须修正的热核公式

审计稿所写
\[
P^{-1}=\int_0^\infty e^{-tP}\,dt
\]
不能直接用于当前 \(P\)，因为它既有零模，也有负模；例如
\[
P(g_1-g_2)=-\Lambda(g_1-g_2).
\]
对 self-adjoint \(P\)，正确伪逆可写为
\[
G^\perp
 =\sum_{\sigma<0}\sigma^{-1}\Pi_\sigma
 +\int_0^\infty
 \left(
 e^{-tP}-\Pi_0-\sum_{\sigma<0}e^{-t\sigma}\Pi_\sigma
 \right)\,dt,
\]
其中积分只保留正谱部分。产品热核只是在每个分离张量块及投影修正之前因子化；最终 resolvent 仍不是两个静态 Green 核的乘积。

### adjacent pair

对 \((N,N)\to(N,S)\)，完整四维点不同，故 full product Green kernel 及其 jets 光滑。短时热核中 antipodal 因子提供指数衰减，压制 coincident 因子的局部奇性。

“massive one-factor reduction”必须证明：

1. 一个因子确实被投影到固定本征空间；
2. 余下因子的 shifted operator 可逆，或其核被投影掉；
3. 求和、取 pole jet 与正则化可以交换。

尤其不能把 coincident 因子的二维静态 Green 核逐模取值后乘以另一个因子的 antipodal Green 核；这会制造虚假的二维对数奇性。adjacent 情形最稳妥的表达仍是 full product heat kernel/resolvent。

## 3. \(T^2\) 选择规则

“筛 character，不截断 \(l\)”完全正确。标量模型中二阶 pole jet 的 \(|m|=2\) 通道满足
\[
P_l''(1)=\frac{(l+2)(l+1)l(l-1)}8\ne0,\qquad l\ge2,
\]
故所有 \(l\ge2\) 均保留；antipodal 端点给出
\[
P_l''(-1)=(-1)^lP_l''(1).
\]

但正式张量计算不能机械使用标量条件 \(|m|\le2\)。张量局部标架本身带 isotropy/spin weight \(q\)，pole vanishing order 实际依赖 \(m\pm q\)。最安全的做法是按完整张量的总 \(T^2\)-character 分块。EH kernel-product 的
\[
(\pm2,0),\qquad(0,\pm2)
\]
以及 quotient 条件 \(m_1+m_2\) 偶，只将问题压缩到少数无限谱通道。

## 4. \(D_8\)、spin、kernel 与范围

### \(D_8\)

四节点方格的轨道分类正确：

- \(r=1\) 与 \(r=3\) 经 orientation reversal/complement 对应；
- \(r=2\) 分 adjacent 和 diagonal；
- stabilizer 大小分别为 \(2\) 与 \(4\)。

不过稳定子给出的首先是等变关系
\[
F(\gamma\!\cdot\!t,\gamma\!\cdot\!\zeta)
 =\rho_{\rm out}(\gamma)F(t,\zeta)\rho_{\rm in}(\gamma)^{-1},
\]
而非在任意 EH 参数下同一数值数组直接相等。只有参数也被 \(\gamma\) 固定时，才得到数值自约束。\(r=1\leftrightarrow r=3\) 的检查必须同时运输 chirality、kernel basis 和 EH 参数。

此外，\(\rho(z,w)=(-z,-w)\) 是各 \(S^2\) 上有固定极点的半转，不应称作 antipodal map；“antipodal”只应用于节点之间的 \(N\to S\) 位置关系。

### diagonal \(=\) spin

乘积 spin lift 在四固定点的符号
\[
(+,-,-,+)
\]
至整体号，确实将 distinguished pair 放在 diagonal orbit。它足以作为工作识别和内部校验；但从 fixed-point lift 到 punctured quotient 的 \(RP^3\) seam spin structure 仍依赖边界取向和填充约定。没有独立 Kirby/boundary-spin 推导前，不能把 diagonal \(=\) spin 当作最终拓扑定理。

### full-\(P\) kernel

TT kernel 为零的直接 \(S^2\times S^2\) 计算是可信的；但不能未经修正地套用 Kröncke Proposition 4.8 到球面因子，因为 \(l=1\) 时
\[
\nabla^2f=-\Lambda fg
\]
使球面分解中的 \(fg\) 与 Hessian 项重合。

商空间上的 full-\(P\) kernel 有四个 invariant scalar modes：
\[
u_1g_1,\quad u_1g_2,\quad u_2g_1,\quad u_2g_2,
\qquad \Delta u_a=2\Lambda u_a.
\]
这里必须区分：

- \(\bar h\perp\ker P\)：固定伪逆解的唯一性；
- source 对 kernel 的配对：决定
  \[
  P\bar h=S-\Pi_{\ker P}S
  \]
  中的 \(\nu_l\)。

因此，“取 \(L^2\)-正交 slice”本身不能替代 \(\nu_l\) 的计算。必须证明所有相关配对为零，或显式保留四个投影系数及其有限维方程。若改用 reduced Bianchi slice，还须给出 slice 上的算子、domain/cokernel 与 source compatibility。

所谓这四个模式的“integrability”也不应未经证明地宣称；若 Ozuch 的 integrable-deformation 假设在此处确实需要，应先判断它们是纯 gauge/automorphism directions、真正 Einstein deformations，还是仅 full-gauged kernel。

## 5. 最大的概念性过称：inter-node jet 不等于局部 \(\mu\)

EH 渐近随 gluing 参数缩放为
\[
H^4(t_i\phi_i)=t_i^2H^4(\phi_i).
\]
Ozuch 的局部 obstruction 展开为
\[
t_j\lambda_{j,k}+t_j^2\mu_{j,k}
 =O(t_{\max}^{5/2}).
\]
源点 \(i\) 在 receiver \(j\) 产生的 regular second jet 是 \(O(t_i^2)\)，因而首先改变 receiver 的第一 obstruction：
\[
\delta\lambda_{j,k}
 =t_i^2\mathcal I_{ji,k}+o(t_i^2).
\]
代入后得到
\[
t_j\,\delta\lambda_{j,k}
 =t_jt_i^2\mathcal I_{ji,k}+\cdots.
\]
等尺度 \(t_i=t_j=t\) 时这是 \(t^3\) 相互作用，不是 Ozuch 方程中的 \(t^2\mu\)。

下一次 Green 计算所得对象应称为 multipole-to-curvature interaction map：
\[
\mathcal I_{ji,k}
 =c\Big\langle
 \delta R_j^{\epsilon_j}(H_{ji,0},H_{ji,2})\phi_j,
 e_{j,k}
 \Big\rangle.
\]
只有在另行证明的部分解消或重新参数化框架中，它才可能表现为某个新背景上的第一 obstruction；不能直接标记为 Proposition 2.10/方程 (23) 的局部 \(\mu\)。

同时，产品背景
\[
R^\pm=\operatorname{diag}(\Lambda,0,0)
\]
确使 \(\phi_j\in\ker R^\pm\) 时 \(\lambda^{(0)}=0\)，且 Ozuch 的 determinant 公式给出径向
\[
\mu^{(0)}_{j,1}
 =C\det(R^\pm|_{\phi_j^\perp})=0.
\]
所给来源并未据此计算所有横向 \(\mu_{j,2},\mu_{j,3}\)，故不能笼统说“整个第一和第二 obstruction 都因二维 kernel 消失”。

## 6. diagonal \(r=2\) 校准的更强完成标准

一次可独立复验的 diagonal calibration 至少应产出：

1. **完整约定**：\(\Lambda\)、orientation、orbifold charts、\(\Lambda^\pm\) 基、EH kernel 基、\(P=\frac12\nabla^*\nabla-\mathring R\)、D8/factor-swap/\(c\) 的运输矩阵。

2. **精确 source normalization**：以小球面通量定义分布源 \(S_{i,\zeta}\)，固定
   \[
   \bar h_i^4=G^\perp S_{i,\zeta}
   \sim H^4(\zeta)
   \]
   的符号与常数。

3. **全谱伪逆**：逐张量块给出加法型分母，单独处理负谱和四个零模；若用 heat kernel，采用上述 projected formula。

4. **全部 kernel projections**：
   \[
   \nu_{i,l}=\langle S_{i,\zeta},v_l\rangle
   \]
   或等价通量式，并证明其在 diagonal 总配置中的消失/相消，或保留进有限维系统。

5. **有序 inter-node 数据**：
   \[
   (H_{ji,0},H_{ji,2}),\qquad
   \delta R_j^\pm,\qquad
   \mathcal I_{ji,k},
   \]
   覆盖 receiver kernel plane 的固定实基，而非只算一个高对称方向。

6. **实际阶数展开**：
   \[
   F_{j,k}
   =t_j\lambda^{(0)}_{j,k}
    +t_j^2\mu^{(0)}_{j,k}
    +\sum_{i\ne j}t_jt_i^2\mathcal I_{ji,k}
    +\cdots,
   \]
   明确程序究竟计算哪一项。

7. **\(\Lambda>0\) 项与张量块追踪**：不能仿照平坦 torus 把 \(\Lambda\,\mathrm{eh}\) 源项删除；需记录 symmetric-tensor lifts、mixed one-form blocks 和 scalar/gauge blocks各自的贡献。

8. **强校验**：D8 等变性、chirality/complement 运输、Green 自伴性导致的 source–jet reciprocity，以及已知 all-compatible/all-reversed 行中的总投影或 interaction consistency。

9. **严格误差控制**：heat kernel 短时/长时分裂，或双球谐级数的 Abel/Ewald 求和及 certified tail bounds；未经证明的截断和交错抵消不足以判定零或非零。

## 范围结论

该计算无论得到零或非零，都只控制指定 orbifold 极限、参数、尺度和 slice 下的局部解消路线。非零固定参数系数不排除其他参数零点，更不排除远离退化区的 Einstein 度量；有限阶消失也不蕴含非线性可解性或横截性。因此 Step‑76 的 Yau‑26 scope guardrail 是忠实的：这里既未证明也未否定 Yau 第26题。