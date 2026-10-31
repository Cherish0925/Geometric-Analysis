## 共同解析核心：从实际场到曲率相容性，而不只是线性下界

本节按原稿正文提炼。`F07.Sk` 是本图谱的来源定位号（第07卷 Source k），不是为旧成果臆造 I 编号；有明确历史编号的节点沿用 I38/I39/I40/I41/I51。这里“已证”指包内有命题及证明的研究稿状态，并不另行宣称所有前置来源、外部首创性已经重新认证。

最贯通的机制可写成：**实际场供给 → 保留所有非负余项 → 有界场与光滑曲率模型 → 无 Sobolev 的二阶估计 → 弱 Bianchi 自测 → 代数曲率模型与实际微分几何的相容性选择 → 全局拓扑与变分结论。**

这条链条的关键并不是把几个经典曲率下界相加。经典积分不等式只规定允许的数值；本链保留产生这些数值的同一个实际场，追踪它的方向、振幅、导数与联络曲率，进而证明某些数值上合法的近饱和状态无法满足实际微分方程。

### 基础节点与思想演化

| 节点与来源 | 已建立的命题/机制 | 真实输入及范围 | 继承、加强或尚未涵盖 |
|---|---|---|---|
| F07.S1，`line1_integral_rigidity_paper.md`，§§1–9 | 原积分刚性：`E(g)+(T/A−2/3)_+ ≥ ε₀`。分析层是指定 Weyl 轨道附近的校准缺陷满足 `(1+B_a)κ≥c`。先保留 SW 不等式的非负误差，截断权重得到有界旋量，再制作全局光滑的多项式 Weyl 模型，避免在特征值重合处微分不光滑特征投影。 | 闭定向四流形；逐度量选择实际 Spin-c 类，`p=(a⁺)²≥A>0`、`a²≥T=2χ+3τ`；原证明要求同一结构在该共形类全部正权重下有解。类可随初始度量改变，无需连续选类。 | 无直径、体积、非塌缩、Sobolev、点态曲率或曲率导数前提。原结果已超越精确 Einstein 非存在，给出积分距离。零 Ricci 常数另由非零实际投影的标量预算排除，不能仅凭 `E` 处理。最新 N1 回接并加强这一原临界障碍。 |
| F07.S2，`round21_analytic.md`，§§1–7 | 提炼独立的有界自对偶二形式准则。令 `B=avg|Δ_Hψ|²`、`d_t=avg(|Ric+g|²+|W⁺−A_{ψ,t}|²+(|ψ|²−2)²)`；有 `|t||1−2t|≤C√[d_t(1+B+d_t)]`。 | 只需有界自对偶形式及 Hodge-Laplacian 预算；不预设 Spin 或 monopole，不预设小一阶导数。模型 `A_{ψ,t}=t(|ψ|²I/3−ψ⊗ψ)`。 | 将“如何供给场”与“场如何强迫几何”分开。非零精确分支选择负 KE 值 `t=1/2`；另一分支 `t=0` 是 Weyl 振幅消失。正负 Einstein 统一形式为 `|t||σ+2t|≤C√[d_{σ,t}(1+B+d_{σ,t})]`，非零精确分支 `t=−σ/2` 给 KE。仅是解析准则推广，未自动提供正侧规范供给。 |
| F07.S3，I07，`line1_functional_pencil.md` | 从一个禁配 Weyl 轨道推广到标量–Weyl 泛函族。`Dβ=(1+1/β)∫s²+6(β+1)∫|W⁺|²−72π²p`；有限 `2≤β≤L` 有 `(1+b_a)(r+Dβ/V)≥c_L(β−2)²`。 | 原实际共形供给；平方负部成本 `b_a=(-a²)_+/V`。`a²≥T` 时成本因子可由 Chern–Weil 去除。不需要标量曲率点态带。 | 原 β=8 临界障碍成为这一族的一个截面；β=2 必须允许真实负 KE 饱和，不能误称所有参数有统一正隙。精确误差分解也产生 Weyl 方向信息，而非只有其范数。 |
| F07.S4，`line1_compactified_pencil.md` | 控制所有有限 β 的常数并紧化 `t=1/β∈[0,1/2]`，令 `P_t=tD_{1/t}`、`P_0=6∫|W⁺|²`。旧紧化界为 `(1+b_a)(r+P_t/V)≥ct³(1−2t)²`；得到能量上、下包络的定量内缩。 | 同一实际供给；常数跟踪独立于参数截断，不能仅把有限 L 定理形式取极限。 | t=0 的延拓是真实定义，但右端仍为0，未证 O10。后由 I51 将三次衰减改善为二次。经典可行能量区间本身不计新结论；新增的是严格分离。 |
| F07.S5，`line1_energy_envelope_gap.md` | 在 `T=A(1−h)`、`0<h<1/3` 下，`E+(e−F(h))_+≥εh²`，`F(h)=(4−√(1−3h))²/9`。 | 每度量实际 `p≥A,a²≥T`；包含原一般型吹起及添柄族，需保留小扰动 chamber 与 loop insertions。 | 将局部参数不饱和转成候选 Einstein 的能量下墙。它没有把 Ricci 能量下确界误当所有候选的上界。后来 I40/I41 在小 h 窗口形成更强线性墙。 |
| F07.S6，`line1_two_chirality_topology.md` | 对立手性的非负 Weyl 能量给 `e(1−E)≤U`，`U=3min(T₊,T₋)/A`；与前述下墙结合得 `E+(U−F(h))_+≥ch²`。 | 不要求相反取向也有 monopole，只用另一 Chern–Weil 恒等式。给实际混合球商手术族的全度量障碍。 | “双手性”是增加独立几何预算，不是引入第二个任意规范类。所得点态 pinching 下界排除这些流形成为任意近 Einstein 输入，故不构成 Yau26 反例。 |
| F07.S7，`line1_bauer_furuta_geography.md` | 用 BF 非消失供给实际场，构造 ordinary SW 不足以检测的连通和应用，包含两取向均无 almost-complex 结构的真实族。 | 原稿规定的2或3个单连通辛块、`b₊≡3 mod4`、适用 BF 连接和非消失、负定附块和符号选择；预算 `A=Σc₁²(X_i)`，手术量含 `4(r−1)`。 | 分析常数不依赖 ordinary basic classes 数目、同调秩或虚维数。这里拓扑应用范围确有增加，但分析引擎继承。不能将 arbitrary connected sum 视为自动有供给。 |
| F07.S8，`round14_twisted_rigidity.md` | Pin-minus 输入经双覆盖提升为普通实际 SW，再将覆盖不变权重版本的积分障碍下降。 | 只需覆盖上证明实际用到的 deck-invariant 权重有解；解本身不要求 invariant，更不要求覆盖上一切非不变度量有解。扭曲类及能量在双覆盖同乘2。 | 真正拓展供给范畴，保持归一化常数；不可偷换为覆盖全部度量的 ordinary monopole 类。最新单解版也能在相应不变 Yamabe 代表上继承。 |
| F07.S9，`lebrun_stability_closure.md` | 将原临界积分障碍严格接回 classical polarized class：一般 `E+((T_X−D)/A−2/3)_+≥ε`，一般型 `A=T_X` 时为 `E+(1/3−D/A)_+≥ε`。 | 不变量非消失、正虚维时保留插入、`b₊=1` 时固定正确 small-perturbation chamber；在一个共形类中同一选定结构供给所有权重。 | 解决原解析结论到真实拓扑的量词、正负/零 Einstein 常数与预算角点，不是重新证明 Hessian/Bianchi。`T_X=D=0` 等零角不能乱写成一般 Einstein 非存在。 |
| F07.S10，`20260926_boundary_compatibility.md` | 同一实际形式的一致近闭性；零 Weyl 假设下 `avg|∇ω|²→8/3`；实际 h→0 平衡族及恢复上界；联合类证书的经典预算支配。 | 沿用同一实际解的误差与Hodge预算。h→0 构造与旧供给一致，不能只凭数值 Chern 数据。 | “零端不是近平行端”是关键认知修正。精确 ASD negative almost-Kähler 禁止不自动推出退化族统一间隙。纯 cup/Gram/PSD 符号证书未增加所需信息。该时 h² 下界后来被 I40 线性下界取代。 |
| F07.S11，I38/I39，`20260926_actual_topological_cost.md` | 同解精确式 `Σ+∫(f−c)²ρ²=||s+cρ||²+8cK+8J₊`；低幅区局部方程与 signed Chern transgression；另构造光滑 cubic torsion 的 opposite-spinor Dirac 方程。 | 实际正权重 SW，同一解；不能把 weighted 与 ordinary 不同解的误差互换。权重变化新增左侧非负项，不能删去，也不需微分 f 来获得该式。 | I38 当时证明 sublinear h 序列必有临界集中，后来 I40 在其条件下排除此分支。I39 给零端弱残差和扭率预算，仍有独立用途：q<2 小残差不等于 critical L² 小，局部实际核心不是闭流形反例。 |

### I40—I41：线性跃迁与全度量无迹 Ricci 化

**I40，第05卷 Source1 §§4–5。** 真正新增之处是删除旧二阶估计中的背景体积 `O(V)`：β=2 的 KE 代数曲率模型在校准幅度上湮灭所选旋量。因而

`H=∫(|∇²_AΦ|²+|∇_AΦ|⁴) ≤ C(K+Θ+B)`，

其中 `B=∫|F_A⁻|²`、`Θ=rV+D₂+εV`。类平方条件把 B 控制为 K 与Θ；弱Bianchi自测和多项式散度强制再吸收K，得到

`Σ,(p−T₊)_+ ≤ C(rV+D₂)`。

由此在双手性窗得到 `E+(U−1−h)_+≥ch`；原真实平衡族有 `c₁h≤inf E≤4h/(1+h)`，首次决定线性阶。允许平方亏损 `y=(T₊−a²)_+/A` 时保留 `ch²/(h+y)`，所以 `y≤Lh` 仍保留线性阶。此结果不是最佳首项4的证明；β=2 的模型消去机制不能原样移植到 t=0。

**I41，第05卷 Source2 PartI §§1–5。** 在每个负 Yamabe 类归一化到 `s=-4`，利用精确共形能量关系，把 I40 的 `rV` 中标量波动删除，得到无小误差前提的

`Σ ≤ C{P+D₂+√[(P+D₂)Y]}`，`Y=(T−a²)_+`。

这不仅简化记号：下界的支付对象变成真正的无迹 Ricci。令 `J=4P/R`、`e=R/(8π²A)`、`z=p/A−1`，`Y=0` 时

`e(1+J/18) ≥ 1+(1+c₀)h+(2+c₀)z`，

另一手性给 `e(1−J)≤U`，因此全度量线性障碍直接成立于J。`Y>0` 时附加项为 `c_s(h+z)²/(h+z+y)`。这使类平方亏损可量化，而非一刀切删除所有该类输入。

同一工作给出了真实 BF geography 新线性窗及**次单位极值的准确共形归约**。若 `δ=∫s_g²−∫s_ĝ²≥0`，则 `P_g−P_ĝ=δ/12`、`R_g−R_ĝ=δ/3`，故 `J(g)` 是 `J(ĝ)` 与1的能量加权平均。原范畴次单位区间内 `inf E=inf J`；正确处理相应近极小序列与标量损失。不能继续把“去标量方差”列为开放，也不能说Yamabe替换保持点态Ricci误差。

### I51：同一普通解覆盖全部有限参数，保留不同误差尺度

第01卷 Source2。先在负 Yamabe 代表使用固定实际方程 `D_AΦ=0,F_A⁺=2iσ(Φ)`；β只出现在代数拟合，而不要求每个β另换场。完整平方分解同时控制：场幅度/一阶误差为 `Dβ` 阶，Weyl模型拟合为 `Dβ/(β+1)` 阶。后者多出的 `1/β` 不能被粗化丢掉。

保持模型导数中的 `t=1/β` 后得到

`(1+b_a)(r+Dβ/(βV)) ≥ c₀(β−2)²/β⁴`，

即紧化后 `r+P_t/V ≳ t²(1−2t)²`，把原三次端点衰减严格加强为二次，并改善原实际族的 upper energy wall。因而这是全度量积分理论的改善，不仅是某种点态曲率受控版本。证明无需导数曲率上界，Maxwell控制是Hodge graph范数，不能读成联络协变W¹,²估计。

I51另检验高指数与分裂核心：单项式模型的昂贵临界成本不是所有高指数结构的普遍下界；多个简单零可分裂，使核心局部成本降阶。此修正保留了完整外部延拓这一缺口。

### 最新单解加强与 N1：缩短输入后回接原临界障碍

来源：同日续研报告附录06；`Qiushi_Line1_Unified_Gap_20260928.md`。

**单解解析节点。** 在 `s=-4` 的代表，只需一个普通实际解，`ρ=|Φ|²≤2`，有精确动力恒等式

`Σ=16K+4∫(ρ−2)²+8J₊`。

它与 I51 β=2 分解、低幅区真正的局部方程测试、背景模型湮灭及弱 Bianchi 吸收结合，重新得到 I41 的线性平方亏损式。此证明不比较两解、不取辅助权重解的导数、不依赖整族可解性。因此当前最小充分输入为：**逐共形类，在其负 Yamabe 代表上存在一个实际普通解，并满足指定投影及类平方预算。** 全度量应用是 `∀[g]∃(a,A_conn,Φ)`，统一下限A；不是“一处存在一个解便控制所有度量”。不同共形类允许选不同a，无连续性要求。

这一加强压缩了分析供给；既有SW/BF/Pin实例全部保留，但目前尚无由此新增、严格超出旧供给的拓扑族。抽象二形式准则也仍保留独立价值：它容许完全不同的实际形式构造，并不因单解证明更短而被废弃。

**N1，原临界障碍的无迹 Ricci版。** 在上述单解输入且 `p≥A>0,a²≥T` 下，存在绝对ε使

`J(g)+(T/A−2/3)_+ ≥ ε`。

证明取单解I51的 β=8，使用精确式 `D₈=108π²(T−2p/3)+(27/2)P`、标量预算 `16V≥32π²p`，先在Yamabe代表得 `43r/16+27d/4≥c₈`；再由 `J(g)≥min{J(ĝ),1}` 转移。它将原积分障碍的E加强成J，并减少实际输入。这个回接很重要：统一主线不应只剩小h端与系数4，而应同时包括**原 T/A=2/3 临界禁区、完整参数曲率相容性与 KE端线性代价**。N1属于明确推论链，不另称全新独立PDE机制。

### 主干关系与必须保留的边界

1. F07.S1 的固定校准禁配，经F07.S2提炼为独立形式准则，再经I07/F07.S4扩为整个参数族；F07.S5–S9把它落实到真实拓扑、两手性与不同实际供给。
2. F07.S10–S11暴露两个端点的不同机制：KE端候选浓缩由I40背景消去关闭；零Weyl端仍有非零导数/扭率，不能套近平行证明。
3. I41把I40归约为全度量无迹Ricci结论；I51从同一实际普通解提取更精确的参数误差尺度；最新单解证明再削弱I40/I41供给；N1使这一新输入完整回接最早的临界拓扑障碍。
4. 上述主干允许独立形式、普通SW、BF、twisted/cover几条供给入口，但每条必须实际提供所需的场与微分预算。cohomology数字、有限覆盖拉回、对多个basic类纯Gram/符号凸组合，均不自动带来新微分信息。
5. O10仍缺零端不退化的实际微分约束：现有全部有限参数预算兼容形式端点数据；这仅说明该层数值信息不足，不是闭流形实际反例。O11仍缺全部竞争共形类的最佳首阶代价；普适强制常数优化不能单独闭合4。两者是主干的加强目标，不是已有I40/I41所欠缺的证明。
6. 精确零端禁配、定量统一间隙、真实局部核心、闭流形匹配、精确Einstein实现，量词和尺度不同。任何知识图谱必须把这些作为不同节点，避免用一处局部存在或精确不可能代替全局变分结论。

### 最有价值的后续解析问题（按增加的信息，而非按方法名）

- **通用输入的实质扩大：** 找到一个旧供给未覆盖、却满足单解Yamabe输入或独立有界形式预算的自然真实范畴，实际产生新的全度量结论。只去掉“all weights”措辞而没有新对象，不应重复算应用突破。
- **零端新信息：** 构造一个在t=0仍有内容的、同一实际场的全局相容性量，控制外部同时退化时的扭率/曲率付费；或构造完整闭实际逃逸序列。不能继续只扫描β和已有线性组合。
- **最优代价新信息：** 全曲率归约允许从真正近极小序列取得变分信息，尝试与同解场估计耦合；首先须构造具有适合Q尺度的一阶变分残差的序列，不能把近极小自动当驻点。也保留同原族真实低成本构造，任何能改变全局首项的构造都属于主线。

## 早期八卷中不可遗漏的核心分支（01—03卷增补）

以下 `Evv.Okk` 仅为早期卷号/原稿序号定位。早期02卷的五篇分别与上述 F07.S2/S3/S5/S6/S4 对应，已完整登记，不将重复收录再算成果。早期01卷中的核心论文、polarized closure、twisted、BF也已对应；其余如下。

### 早期入口与规范供给的额外节点

| 节点 | 原稿标题与内容 | 必须保留的逻辑关系 |
|---|---|---|
| E01.O1–O3 | `COMPACT_READING.md`、`LINE1_CURRENT.md`、`LATEST_DISCUSSION_STATUS.md`：区分已证障碍主干、独立实现延伸、当前供给与sharpness问题。 | 这是阅读与研究范围约定，不是新增数学定理。早期主线明确要求保留不同范围；不能以最新系数4题抹掉原临界障碍、实际供给与实现分支。 |
| E01.O6 | `round21_chambers.md`，*Polarized scope of the integral gap and the symplectic chamber*：解析输入只需指定共形类；若辛四流形 `b₊=1,K²>0,K·[ω]>0`，Lorentzian 正锥保证 canonical 类的 small-perturbation chamber 对全部度量一致，得到实际供给与原积分障碍。 | 无需可积复结构；`K·[ω]>0`不能删除，否则会误排除CP²正Einstein度量。它是实际供给条件的几何验证，不是Bianchi证明自动提供的事实。 |
| E01.O7 | `round14_rigidity.md`，*Finite-cover integral rigidity beyond ordinary Seiberg–Witten detection*：有限覆盖精确下降，积分缺陷及pointwise defect不变，常数不随度数损失；自由对角orientation-reversing双曲曲面乘积商的吹起给ordinary SW全消失但覆盖障碍仍适用的实际族。 | 所需只是对所有拉回度量存在相应upstairs供给，不能擅自要求/推得cover上全部度量的monopole。任意cover度量可能不下降，故两个全度量inf不能直接等同。既有shear族的归一化预算在覆盖保持为1，不能由覆盖把它推到2/3禁区。 |
| E01.O10 | `20260916_uniform_gap.tex`，*Uniform gaps at the Einstein topological boundary and necessary collapse of near-Einstein metrics*：早期用校准密度与Einstein四维正则性取得经典blow-up边界附近的统一精确Einstein禁区；有界Ricci下near-boundary近Einstein输入迫使固定尺度非塌缩中心体积分数消失、直径发散；另有条件SC的近Einstein间隙。 | 属于思想演化的重要起点：最初通过“若输入存在则必须退化”识别紧性障碍，后来无几何紧性积分障碍在相应实际范围直接排除该逼近。旧必要退化结论与条件SC不得恢复成新主定理仍必需的假设。其历史Yau26工作表述也须与另行核定的原题量词分开。 |

### 早期03卷：实际形式、允许分支、多类周期与能量选择

| 节点/原稿 | 核心已证结论和机制 | 范围与保留边界 |
|---|---|---|
| E03.O1 `round3_monopole_input.md`，*Quantified monopole inequalities and a bounded Weyl model* | 重做项目曲率/旋量规范下的weighted供给，保留四类微分缺陷、两次Hölder的准确总余项；控制振幅及实际Hodge投影，在受控谱区取得方向对齐，制作全局有界光滑Weyl模型，并核定Hodge与divergence-energy归一化。 | 为后续几乎全部解析分支提供同解误差和规范基础。Hodge类来自实际联络曲率，不来自“微分小所以谐投影接近”的无谱隙论证。 |
| E03.O2 `line1_scalar_band_remainder.md`，*A scalar-band remainder for LeBrun's Ricci-energy inequality* | 在负标量双侧带、实际共形供给下，由LeBrun余项构造有界旋量/自对偶形式、Weyl多项式拟合、近闭与协变导数估计、实际谐投影；标量方差估计显式支付 `1/λ₁`。 | 等号给**负cscK**而不是必为KE。`dψ`与`∇ψ`必须区分；小外微分不自动小协变导数。原度量方差估计的谱支付不能删除。 |
| E03.O3 `line1_composed_application.md`，*Harmonic Chern representatives at the realizable Einstein calibration* | 在β=2的实际供给、Ricci残差与D₂小的输入下，不假设标量带、谱隙或预先形式，直接产生有界almost-parallel形式，接近指定实际harmonic Chern代表；同时给Hodge-Laplacian预算及连接Laplacian低频投影。 | 这是允许KE分支的**结构供给**，不是另一个禁止定理。负平方成本只进入二阶预算，一阶谐对齐不支付它。不能由low mode推出精确平行或Einstein修复。 |
| E03.O4 `round15_rigidity.md`，*Quantitative product-boundary calibration and its surviving source* | 常负标量、实际单解 `a²=A=T` 时有准确标量损失式 `4D=K+κ∫(4κ−ρ)+2||F⁻||²`，控制真实可实现Weyl模型；两取向供给给全乘积曲率模型。保留weak Bianchi实际源，并用真shear计算源的三次阶。 | 允许的模型是双曲曲面乘积，不能套早期禁配模型制造矛盾。constant scalar是该时真实假设。精确Einstein接近sharp volume时排除曲率泡，仍可留下长薄退化。 |
| E03.O5 `round16_rigidity.md`，*Product-profile propagation into collapsing Einstein regions* | 精确 `Ric=-3g`、双取向实际供给、绝对体积excess D小，取得相对局部 `sup_{B1/4}(dist(Rm,product)+|∇Rm|)≤C√(D/Vol B1)`；从一个厚点对数距离传播，半径 `θlog(1/D)` 区域逼近product。 | 不要求统一ball volume下界，但必须 D比局部体积更小；远端极薄区域仍未覆盖。真实Einstein方程是正则性输入，不能推广到任意小积分残差。 |
| E03.O6 `round17_integral.md`，*Scalar-energy stability on the original metric* | 用smooth radial truncation去掉Round15常标量前提，在**原度量**上从一个实际ordinary解构造有界形式，控制 `∫|∇φ|²≤4κB`、振幅及实际闭determinant curvature距离；Weyl轨道误差由P、scalar energy slack B、目标标量误差L和 `(T−A)_+` 控制。 | 无scalar band、Sobolev、紧性或共形更换；两取向扩为完整product曲率。形式可能有零、可能不闭，积分轨道控制不等于pointwise曲率控制。 |
| E03.O7 `round18_periods.md`，*Actual monopole intersections and global phase mixing* | 多个**实际等正平方**类同时近饱和，共同Weyl强迫形式接近同一无向线；全局L² wedge得到归一化交叉矩阵接近sign-correlation polytope `conv{zzᵀ}`。非极端交叉数迫使scalar Laplacian小特征值，协方差秩控制多个慢模态。 | 不假设类和/差也是monopole，不在塌缩cycle上做无保证trace。相位允许切换，结论是切换造成慢模态，绝非全局sign不变。实际连通和族及其饱和度量实现了相关现象。 |
| E03.O8 `round20_rigidity.md`，*What an integral monopole gap can control in the period domain* | 无scalar saturation时也可给每个实际类的投影半径上界。有限类span W所定义的period-height proper，当且仅当W含maximal positive或maximal negative子空间；此时才有整个period plane紧约束。 | 半径改进继承积分障碍，properness是明确线性代数条件。实际exact Einstein双曲曲面乘积可退化，说明special类数目多或每类有界不自动给period compactness；未证一般monopole集合秩定理。 |
| E03.O9 I12 `line1_period_inertia.md`，*Simultaneous endpoint saturation and the positive inertia of Chern periods* | 去掉等平方、正平方/类平方预算：多个实际共形类在β=2同时近饱和，给带明确scalar谱支付的常sign投影对齐；positive-period矩阵 `P=q₁ααᵀ+R`，cup矩阵 `Q=q₁ααᵀ+R−N`，R,N半正定，`trR≤(m−1)J`，因而第二正特征值 `ν₂(Q)≤(m−1)J`。 | J含 `G(κ)/λ₁`；只需 `λ₁≫√κ` 而非固定谱隙。若第二正惯性定量不消失则逼出小λ₁。必须保留volume归一化；单有positive inertia符号不够。F07.S10后来检验标准signed suppliers的纯matrix证书不超过经典预算，并未否定实际period定理。 |
| E03.O10 `line1_kahler_energy.md`，*Kähler controls for LeBrun equality, Ricci energy, and Einstein defect* | 关键等号校正及真实测试：Kähler时 `D=L/(64π²)`、`P=8π²(p−A)+L/4`、`R=8π²(2p−A)+L/2`。因此LeBrun D=0只是cscK，primitive period `p−A`另行支付Ricci各向异性。unequal negative products是实际反例；blow-up最小序列有正极限缺陷。 | 这些是经典Kähler/Hodge/Chern–Weil推导，非宣称首创。它们纠正了“Ricci余项小或D=0便Einstein”的错误，并持续约束后来的I41通用常数与Weyl支付。 |
| E03.O11 `line1_energy_selection.md`，*Ricci-energy selection, scalar coherence, and Einstein defect* | 从经典SW/Chern–Weil得到对**所有**Ricci-energy近极小序列的有限估计：C=8π²A,H=8π²d,J_R=R−C−H≥0，有 `H−√[J_R(C+J_R)]≤P≤H+J_R`；准确 `E=(4P+L)/R`。 | 不依赖项目Bianchi引理；原度量scalar variance不能删（有实际conformal反例）。负Yamabe代表可删除该方差而不需scalar谱隙。Ricci能量最小不等于E或全曲率最小，后来的全曲率归约必须单独证明。 |
| E03.O12 `line1_non_kahler_bridge.md`，*Einstein-defect bridges without a Kähler assumption* | 原度量：scalar band+明确谱支付，将period/topology与LeBrun余项转成Ricci残差上界并供给allowed-form；共形代表：无需scalar band/谱隙，`θ=(p−T+4D)/p≥0`给 `E(ĝ)≤4θ/(1+θ)`。 | 这是从实际拓扑/period与饱和度推导近Einstein的**正向构造接口**，与禁止型不等式不同；原度量和改变共形代表的结论不能混同。仍不升级成pointwise pinching或精确Einstein输出。 |

以上分支必须出现在整个知识图谱中：第一主线从来同时研究**禁止的校准与允许的校准**，并且已有实际谐Chern对齐、多类周期/慢模态、Kähler等号修正与非Kähler逼近接口。把它只画成“I40线性h → 最佳4”会丢掉主要认识与已有独立结果。
