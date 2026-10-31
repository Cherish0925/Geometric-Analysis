# 第一主线几何构造、变分与数值知识表（内部合并稿）

阅读依据：02卷 I52/X09/I53，03卷 I54/I55/X10，06卷四份继承原稿，11卷全部数值模型说明与六组回执；并参照10卷节点目录，以及本轮 `audit_cap.md`、`audit_radial.md`、`audit_global.md`。下表区分“原稿已有定理”“本轮已核验推论”“条件性接口”“真实反例”“数值未发现”；不把所有节点压缩成O11。

**完整资料范围说明。** 当前集中资料还已纳入早期八卷中的04—08卷，位于 `/workspace/scratch/e82e2d951212/review/earlier_eight_volumes/`：04《允许Weyl结构与核心控制》、05《紧致范围精确实现》、06《覆盖塌缩与轨形实现》、07《全局转移慢模态与填充》、08《跨线依赖反例与证据》。它们涉及此前的实现性、修复、holonomy／monodromy、慢模态及真实跨线反例；并未因本表聚焦续研几何结果而从研究体系删除。逐项实现性结论另由实现性附录说明；本表不把早期卷标题当成定理量词的替代，也不宣称在本次快速复查中重新验证了其中所有证明。

**本地定位约定。** 下列“02卷”等指 `/workspace/scratch/e82e2d951212/review/continuation_0b14907/` 下的相应文件；每个Source内部节号独立。准确文件与Source对应如下：

| 简称 | 本地文件 | Source及原稿名 |
|---|---|---|
| 02卷 | `02_first_order_stability_and_moving_centers.md` | Source1 `20260927_endpoint_covariance_and_surgery_limits.md`；Source2 `20260928_marked_centers_and_harmonic_slices.md`；Source3 `20260928_intrinsic_caps_and_stability.md` |
| 03卷 | `03_complete_cells_localization_and_selection.md` | Source1 `20260928_relative_cell_cost.md`；Source2 `20260928_localization_and_coupled_filling.md`；Source3 `20260928_signed_characteristic_selection.md` |
| 05卷 | `05_inherited_linear_coercivity.md` | Source1 `20260927_mixed_current_and_signed_cores.md`；Source2 `20260927_conformal_separation_and_zero_end.md` |
| 06卷 | `06_inherited_geometry_cores_and_variation.md` | Source1 `20260927_covering_geometry_and_sharp_subfamilies.md`；Source2 `20260927_local_geometry_and_variational_extrema.md`；Source3 `20260927_full_core_cost_and_extremal_metrics.md`；Source4 `20260927_signed_balance_and_conformal_flow.md` |
| 10卷 | `10_source_map_and_history.md` | 按节点I42—I55、X06、X09、X10定位目录与范围核对；它是索引，不替代前四行证明 |
| 11卷 | `11_numerical_constructions.md` | “参数如何定义实际度量”及六个`verification/computations/...`回执标题；各组另有Record编号 |
| 本轮报告 | `/workspace/scratch/e82e2d951212/audit_cap.md`、`audit_radial.md`、`audit_global.md` | 以下各行引用各报告内部节号；这些是本轮推导和核验，不混作冻结原稿Source |

本表没有工具内引用编号。若涉及本轮单解改进，准确称“**已证较弱输入**”，不据此断言分析假设已最优。

统一记号：`E=infλ∫|Ric−λg|²/(λ²V)`；`P=∫|Ric°|²`；`R=∫|Ric|²`；`A=c1²(X)`；手术量`Q=k+4ℓ=Ah`。曲率平方采用原稿曲率算子范数。完整单元的 `J=∫cell|Ric+g|²` 不等于闭流形无量纲 E；I47 的 `𝒬=|Ric°|²+4|W+|²+s²/12` 也不是全曲率能量。

## A. 几何零端与实际场的局部—整体接口

| 节点／定位 | 结果与适用范围 | 主结论依赖及逻辑作用 | 必须保留的限制／已失效路线 |
|---|---|---|---|
| I42（05卷Source2§8–12，06卷后续继承） | 对有界自对偶近闭形式及 `t∈[0,1/4]`，局部有界Ricci且非塌缩时存在模型缺陷正下界；有界截面曲率情形不需injectivity下界；精确负Einstein+有界χ/V给零端非退化间隙。 | 正则图中的极限是局部不存在的负Einstein ASD almost-Kähler系统；`t>0`用Bianchi迫平行再与参数冲突。指数映射与Liouville平均处理多层覆盖；精确Einstein时CT小能量正则性+Fubini提取正体积好点。 | 非塌缩只在所述局部入口；不能把极限论证搬到纯积分Ricci输入。坏序列是曲率尺度在测度中消失，不是处处曲率值发散。 |
| I43（06卷Source1§1–4） | 用局部普遍覆盖体积代替基底体积：好覆盖区域体积分数受缺陷控制。CFG比较、Li II平滑、最大纤维秩提供可检查供给。 | 真实形式及误差始终留在原度量；平滑只供给比较几何；路径提升与Liouville平均避免覆盖层数上界。给无直径的零端和上能量壁分离。 | 一致小局部完整曲率L²／局部L^(2+η)等是额外条件；不是平均能量自动推出。覆盖上的成本不能不计体积／重数地下推。 |
| I45（06卷Source2§3） | `|Ric|≤K`、有界形式、Euler密度预算下，所有 `t∈[0,1/4]` 有非退化几何间隙；不需直径、基底非塌缩、全局Sobolev或精确Einstein。 | CT有界Ricci覆盖正则性+Euler/Fubini选点；原拓扑比χ/T+或χ/A可供给预算。一般型手术族通过Noether等继承统一密度界。 | 删除的是逐球小能量条件，未删除点态Ricci条件。小L² Ricci误差不能代替它。 |
| I48（06卷Source3§3、Source4§5） | 两种独立椭圆入口：①`|ΔRic|≤C|Rm||Ric|`且固定尺度归一化负Ricci Lp量足够小、p>2；②精确csc二次曲率临界点、指定全局Sobolev和绝对拓扑上界。两者均给零端间隙。 | 局部Sobolev吸收、曲率bootstrap、Euler选点；或Anderson紧致性产生不可能的正则极限。 | “小”不能改为“有限”；“驻点”不能从Yamabe归一化／近极小自动获得；第二条是绝对T+、χ界而非仅比值界。 |
| I46（06卷Source2§4） | 实际带标记平坦商环带的正spinor与反向扭率平行极限，仅允许奇数循环 `1/n(1,−2)` 及两个指定determinant类；其它实际lift支付校准／曲率／Dirac代价。允许类有真正局部方程解。 | 自旋holonomy分类；固定有限商群族的临界紧致性；有界重叠的物理尺度计数。 | 常数未对任意商阶统一；实际局部解含未填充orbifold顶点，不能当闭流形或光滑核心；弱全局输入尚未自动供给环带和marking。 |
| 全局一阶ALE匹配（06卷Source1§7） | 完整一端hyper-Kähler ALE、非平凡SU(2)−端群、H¹=0，全正spin-c联络有全球平行架，实际场有明示一阶展开且联络曲率一阶项L²，则有界一阶协变导数／物理扭率必为0。 | 保留一阶联络源；全球exact L²单手性2形式为0；ALE上次线性harmonic函数Liouville。 | 不能省略determinant twist、全球识别、一阶展开或有限能量；bare signed degree不够；此结果未自动适用于任意bubble。 |
| 曲率最大点提取（06卷Source4§6） | 精确csc二次曲率临界序列，尺度一致非塌缩、完整曲率总能量界、绝对Ricci/W+拟合误差→0，能提取非平坦Ricci-flat ASD ALE并把其大截断嵌入原流形。I47排除其共振奇循环端群。 | 真实椭圆方程+非塌缩bootstrap；BKN用于极限；不预设bubble-tree能量等式。 | 只抽取终端几何核心，未抽出同尺度非零反向spinor；原绝对场误差经r^-4放大可能不小，不能免费接I46的双场holonomy。 |

## B. I44、I47：可精确计算的全局子族与完整核心

| 节点／定位 | 结果与范围 | 主结论依赖及用途 | 限制／失败箭头 |
|---|---|---|---|
| I44：只添柄精确值（06卷Source1§5） | `M=X#ℓ(S¹×S³)`，`0≤h=4ℓ/A≤1/3`，**全度量**`inf E=4h/(1+h)`；`0<h<1/3`不取到。更一般k=o(Q)有渐近系数4。 | scalar monopole budget+两手性Chern–Weil精确式；经典实际收缩手术给上界。等号spinor平行与c₂(S+)正矛盾给不取到。 | 不是只在恢复族里最优；但不能转写为平衡族k/Q→2/9的全度量结论。h=1/3的取到问题未在此判定。 |
| I44：带标记吹降帽（06卷Source1§6） | 对匹配完整领口的真实吹降帽，`E≥4h/(1+h)−2C+/[π²A(1+h)²]`，`C+=∫caps|W+|²`。只需正手性帽成本，不需帽scalar/Ricci/W−界。 | 相减signature精确保留`B_M=12π²k+B_N+K+−C+`，k项抵消；`C+=o(Q)`即可系数4。 | 光滑可封帽≠低能帽；内禀圆边界≠完整领口便宜。原稿给圆边界但强制帽成本任意大的真实球。 |
| I44：Hermitian／方向扭率（06卷Source2§2） | 兼容全局almost-complex形式的方向能ν、Lee能Θ给`P≥8π²Ah−2ν+2Θ+3(ν−Θ)²/(8V)`；ν=o(Q)足够首项4。任意Hermitian度量在实际scalar输入下 `E≥J≥4h/(1+h)`。 | 自对偶Weitzenböck、Weyl方向谱估计、Yamabe保持Hermitian。可延至原稿所列可控制孤立projective奇点／弱形式接口。 | 未证明平衡流形本身Hermitian或全局almost-complex；不能删spinor零点后遗漏边界项。 |
| I47：整个光滑核心锐利成本（06卷Source3§1） | 物理取向固定的`1/n(1,−2)`，n奇≥3，整个任意内部拓扑光滑填充、外向精确锥领口，`inf∫𝒬=4π²(n−1)/n≥8π²/3`。lifted C²近锥时误差`Cδ²/n`，商阶一致。 | APS型signature/Euler边界公式、η明确符号、相对整数距离；Calderbank–Singer scalar-flat Kähler ALE截断与领口平坦化给上界。 | 这不是全曲率能量；χ与W−能可随n无限增长而该成本有界。不能反转取向，不能用内禀lens-space边界或未填顶点替代完整光滑填充。 |
| I47：真实缺陷原子（06卷Source3§1.3、1.6） | 小体积、近锥误差小的完整核心对原缺陷`Z_t`有正原子，统一极限下界π²；有界重叠得数量密度≤C缺陷密度。相对整数分支j≤0更直接强迫纯Ricci成本，无需体积或规范场。 | 将𝒬拆为有界模型与实际误差；保留相对整数分支收费。额外内部吹起降低j，费用累加。 | 原子sharpness未在实际SW场类证明；不自动计量全部Euler复杂度；原输入尚未提供这些核心、重叠和体积条件。 |
| I47：忠实determinant阻碍（06卷Source3§2） | 完整光滑Ric≥0 ALE、非平凡端群上忠实平坦线丛，不能延拓为全局平坦线丛。因此给定非零平行正实际spinor就排除共振Ricci-flat ALE光滑填充。 | 覆盖／体积刚性与平坦holonomy；平行spinor的几何限制。 | 需要忠实character与实际延拓，不是任何ALE纯拓扑禁定理。 |
| 跨尺度边界（06卷Source3§1.4） | 中间有孔核心的所有内外边界贡献需保留，嵌套区域可望远镜抵消。 | 正确的完整区域相对特征公式。 | 不得在每个嵌套尺度重复收费；“每个终端bubble有成本”不等于整个手术区或所有拓扑都已计数。 |

## C. 变分、动力学与真实反例

| 节点／定位 | 结果与范围 | 依赖／影响 | 限制／排除的错误路线 |
|---|---|---|---|
| I41共形归约（05卷Source2§3–3.1，06卷Source2§1继承） | 负共形类中J(g)是J(Yamabe)与1的加权平均；`inf E<1`时`inf E=inf J`。精确excess分解控制近极小的scalar variance与共形scalar能损失。 | Weyl共形不变、Chern–Weil、负Yamabe代表。 | 是全局泛函关系，不给pointwise Ricci保持、共形因子C⁰紧致或极小值取到。 |
| 二次曲率零层变分（06卷Source2§1） | α=inf E<1与`Qθ=R+θS₂≥0`的最佳参数`θ*=−1/(4−α)`等价。光滑取到时csc负、Qθ*=0且驻点；若0<α<1，不能Bach-flat、Kähler或Ricci平行。 | 精确一阶变分；全局nonnegativity。 | 拓扑上非Einstein不等于不取到；一般二次曲率驻点不等于E极小；θ*在(−1/3,−1/4)不能误用θ≥−1/4的既有定理。 |
| Cotton／低级驻点集中（06卷Source3§4.2–4.4） | 实际SW余项与全Euler–Lagrange方程相接，低能平衡驻点必须保留pointwise Ricci误差；原目录记录`liminf δ−≥1/(4√2)`；pointwise近Einstein csc竞争者的相对二次梯度有正下界。 | 实际同解缺陷、Cotton恒等式及二次临界方程。 | 不是对任意近极小序列可假定驻点；没有给出平衡极小值系数。 |
| I49：有限conformal Ricci flow时间（06卷Source4§1–2） | s=−4流`∂tg=−2Ric°−2ϖg`、`(3Δ+4)ϖ=|Ric°|²`，精确`V′=−P`。三墙控制−y′；原平衡近极小初始窗给`limsup Tmax≤1+log(4/c₁)`，即使ch间隙趋0。 | 已有所有度量scalar下界、Ricci下界、线性E下界；无需连续选择monopole类。另在明确pointwise管状条件内有实际E下降率。 | 是conformal Ricci flow，不是normalized Ricci flow；有限的是最大经典光滑存在时间，未描述奇性、未证明全局延拓或最优寿命；不能用“流会坏”独立证明新非存在。 |
| X06（06卷Source4§3） | 真正闭双曲曲面乘积，anti-Hermitian TT扰动+Yamabe+实际普通SW解，得到`S/F→2`、`P/F→0`。 | 当第二因子首特征值→0，实际变形量满足P/K→λ、S/K→1、F/K→(λ+2)/4；逐固定参数取IFT再对角。 | 否定普适`S≤cF+CP`中c<2；不能丢Weyl payment。该族h=0,U=3，并非平衡族，未反驳系数4。 |
| 纯共形方向正定（06卷Source4§4） | 对真实负csc E驻点0<α<1，非恒定纯共形Hessian严格正；TT+conformal完成平方，最优conformal correction恰令一阶scalar空间常数。 | 精确非Einstein驻点Hessian，`(3Δ+4)((4−α)Δ+4)`正定。 | 不能用纯共形负模破局；余下TT Schur补不是已知负，未证明所有驻点不稳定。 |
| 本轮全曲率归约（audit_global.md§1–3） | `ρ=inf P/(8π²A)`，`4ρ/(U+4ρ)≤α≤4ρ/(1+ρ)`。平衡族α=4ρ+O(h²)，O11等价`inf∫|Rm_op|²=8π²χ+8π²Q+o(Q)`。s=−4竞争代表上的真近极小序列等价到o(Q)。 | scalar下界、反手性Chern–Weil上墙、Yamabe降P。无core或自动选择。 | 不把LeBrun精确Ricci最小值当全曲率最小值；两个下界不能相减。此等价约化未关闭下界。 |

## D. I52—I55、X09/X10：从指定扰动到任意内部

| 节点／定位 | 结果与范围 | 依赖／主作用 | 限制／失效路线 |
|---|---|---|---|
| I52（02卷Source1） | 精细挑选的真实CH吹起/添柄恢复基底；任意a→0的C⁰扰动，在TT后Yamabe、精确csc Bianchi或明示小残差规范中，有`P_final≥P₀+DP₀[k]+c||A₀k||²−Ca²Q`，首项≥4−Ca²−o(1)；等号刻画图范数o(√Q)。 | 完整tensor CH谱隙、Q尺度局域化、真实Taylor、共形比较；没有输入导数界或能量前提。 | 规范需供给，不是自动；近似规范有显式误差；不是固定幅度分类、一般TT全局参数化或任意竞争度量。 |
| X09（02卷Source2） | 同一原平衡拓扑中有真实s=−4恢复对，C⁰距离→0、gauge residual=o(√Q)、各自系数4，但所有固定基底精确Diff₀ Bianchi gauge的bilipschitz常数发散。 | 移动exceptional标记中心与负曲率harmonic唯一性冲突；柄两口聚到同一极限点，避免错误的“不同点合并仍是原光滑极限”。 | 否定统一固定基底精确规范；不否定I52，例子满足近似规范且移动中心可吸收；不产生sub-four。 |
| I53帽定理（02卷Source3§1） | 小C⁰、小完整曲率L²的标记欧氏环带，无输入导数界，可造精确匹配原外领口的光滑球帽，帽完整曲率能≤C(E_annulus+a²)。 | 局域DeTurck完整Lie项；q=χ²+η²平滑；固定输入后η→0冻结领口；临界能量保持；最后回接原germ。 | 每个输入可单独选η，未构造统一连续帽算子；不能只做正时间平滑就声称匹配原领口。帽不需要解场方程。 |
| I53首项稳定（02卷Source3§2–3） | 标记长环带供给，允许o(Q)坏核、均方C⁰误差o(Q)、Lh→∞，得系数4；特别所选恢复轨道的每个收缩C⁰邻域内inf E/h→4，允许orientation-preserving diffeo饱和。 | 竞争能量给全曲率O(A)；长环带平均；部分吹降、signature收费坏核；I44帽公式。 | 尚未从任意真正近极小输入提取环带；未主张新任意C⁰邻域的自动conformal饱和；I52在其规范内的正二次余项仍更细。 |
| 本轮截断帽评分（audit_cap.md§4） | 每个候选标记环带组取`c_i=inf(E_i+a_i²)`；r为未供给者。严格得`E≥4h/(1+h)−C[r+Σmin(1,c_i)]/A`。总评分o(Q)足够。 | 好帽收费、坏帽截断计数、部分signature相减；无需先有竞争能量。 | 是对已给候选环带的更弱有限接口，不提供自动候选选择。 |
| I54完整单元与实际稀疏植入（03卷Source1§1–2） | 完整CH领口、全部过渡计入，q=k+4ℓ；`R=8π²q+S/3+4W+−4d`，`J−8π²q=∫[(s+3)²/3+1+4W+²]−4d`。固定单元稀疏复制给E/h→J/(2π²q)。8吹起7柄q36保留原平衡族；一吹起J<8π²即可反驳系数4。 | 精确闭流形相减、实际覆盖植入、剩余o(Q)手术经典恢复。 | 正密度不意味积分≥4d；没有构造低成本单元；不能忽略scalar/volume/过渡项。 |
| I54 conformal Kähler/biaxial排除（03卷Source1§3–5） | 正exceptional periods与所述相对Chern类下，任何幅度正共形改变仍`J>8π²k`；所有光滑普通bolt biaxial单元归入该类。 | relative Ricci form、Cauchy和共形能量恒等式；整个领口匹配。 | 不覆盖任意non-Kähler填充；普通bolt与相对Chern标记不能删除。 |
| I54完整单元无光滑驻点（03卷Source1§8） | q>0的固定完整CH领口单元，对所有compactly-supported度量变分不存在光滑J驻点。 | conformal trace方程强迫s=−4；tensor方程unique continuation强迫Einstein；接回CH后解析性和拓扑矛盾。 | 不取到／无驻点不等于全体J≥阈值；退化的subthreshold序列未排除。有限维优化器驻点不是无限维驻点。 |
| I55任意内部及等号（03卷Source2§1–4） | CH外部丢失背景体积D=o(Q)时，补集幅度、塌缩、集中、拓扑均可任意，仍liminf E/h≥4；等号等价补集`v+S+W+=o(Q)`，全补集P=8π²Q+o(Q)、W−能=12π²k+o(Q)。 | 精确relative integral身份+两次Cauchy，保留非负余项。一般非Einstein外部有明确积分预算与加法首项`E_out+4h+v/(a+v)+o(h)`。 | 内部可以任意≠外部自动存在；可测区域版本不需逐核识别，但仍需其外部实际预算；不是Γ极限。 |
| I55全nonconformal三轴径向排除（03卷Source2§8） | 普通单bolt、任意正F、任意光滑三轴w、φ=0，全类`J/(2π²)≥(μ+2+μP_w)²/(1−μ²/R⁴)>4`。允许φ时有完整四个非负平方，关键moment M=1+2/μ+P_w−Tφ。 | 完整残差在L²(r³dr)投影到r^-4；bolt与CH端值精确给moment。 | φ≠0的Tφ负窗口未吸收；不能把M任意指定后丢掉其它平方；高成本下降与全类下界相容。 |
| I55两尺度必要性（03卷Source2§9） | μ→0、固定R、若J/(2π²)≤4−ε，则微观区μ加权Tφ保留正量，任何r≥μ^a(a<1/4)部分贡献→0；同时全部背景改动不能限于体积→0。 | moment窗口+scalar/Weyl真实能量下界给宏观梯度界；完整单元J≥8π²−4d/3。 | 只说明微观梯度与宏观改动必须共存，未证明它们不能共存。 |
| X10选择反例（03卷Source3§1–4） | `f=(s²/12+4W+²−Ric°²)/(8π²)`、N=∫f−。竞争序列中I55可测bulk选择等价N≥Q−o(Q)。实际s=−4例子有limsup N/Q≤1−2δ/9但E=O(h)。 | radial负质量原函数；局部scalar gluing；固定参数后再稀释；固定j的Yamabe极限与柄缩小；不交换极限。 | 其系数`28/9+Jcell/(9π²)>4`，是高于最优上界的竞争例，不是否定O11；真正Kähler吹起由全纯Morse可供给N≥k，但不能任意度量化。 |
| X10真正近极小退化（03卷Source3§5.1） | s=−4，E−inf E=o(h)时，任何固定光滑C⁴紧致族的完整CH领口非平凡单元只能出现o(Q)个。 | 每个单元无驻点→实际有限下降；紧致性给统一下降；复制正密度下降与近极小矛盾。 | 未给退化块统一下降率，也未供给分解；不能擅自把近极小替换为Euler–Lagrange解。剩余补偿`P=8π²N+Z`中的Z不能丢。 |

## E. 本轮任意振幅共形公式与数值事实

本轮 `audit_radial.md` 的严格结果：固定完整领口，`G=e^{2φ}K`、φ在领口为0；`δ=s_K+4`、`H=Δφ+|dφ|²`（Δ=div∇）、`a=e^{2φ}`，精确有

`J(G)−J(K)=∫[12(H−δ/6)²+4(a−1+δ/4)²+(16+12a)|dφ|²−7δ²/12]`。

不需振幅／导数小；下降只能由与共形支撑相交的基底scalar误差支付。特别支撑处δ=0时非平凡共形变化严格增加J。接I55径向square后，若j≤4−ε，归一化支撑内scalar误差必须至少`3ε+12μ+3μ²`，且另有支撑外误差与正梯度附加收费。任意φ不能在scalar误差总量o(1)的μ→0基底上获得固定sub-four改进。尚未控制非消失δ²与其它平方的联合优化。

| 数值／模型 | 实际做了什么 | 结果 | 不能推出什么 |
|---|---|---|---|
| 原11卷四组28起点（small/wide/smallbolt/large四组标题） | 光滑普通bolt、完整CH外领口、F=e^v乘正基底，w/φ有限Legendre平坦截断；完整残差、体积及过渡全部算入；粗细Gauss与scalar identity检查。 | 没有j=J/(2π²)<4返回。六份回执保留全部系数、失败状态。 | 有限维局部搜索未发现≠全径向类或全度量下界；没有区间证书。 |
| 原真实高成本负方向（11卷negative_mode及negative_mode_joint两组） | biaxial基底寻找负triaxial Hessian再有限幅度下降，完整参数保留。 | 12.3549246969→12.3355352746；联合优化回到4.1627155918。指定约束容差失败的阶段明确记录失败。 | 对称化不全局单调；但并未接近sub-four，也不是精确负模认证替代解析推导。 |
| 本轮两尺度27参数（audit_radial.md§4，无约束局部搜索） | μ=.001,R=3；micro、macro、log三组相交支撑；非零w起点避免被对称性困在biaxial；完整实际残差。 | 无约束三起点最低4.0040015146；两随机起点700次未收敛。 | 不能称全局最优／驻点证书。 |
| 本轮进入Tφ窗口（audit_radial.md§4，进入有符号窗口后再搜索） | 约束真实`μ(Tφ−P_w)=a₀`，正负φ种子、非零三轴起点；a₀=.1,.5,1,2.001。 | 最低j分别6.75309、16.76881、30.30753、54.55585；约束误差约5e−12以下，粗细积分差<4e−11。 | M=0不代表总cost小；实际剩余平方支付很大，但有限搜索仍不证明普适排除。 |
| 本轮共形恒等式数值复核（audit_radial.md§4，精确恒等式的独立数值复核） | 三组实际随机profiles，直接残差算jG−jK与新平方公式独立积分。 | 两边差约1e−13。 | 仅核对实现与代数；定理依据精确积分证明，不靠浮点。 |

## F. 依赖关系与研究边界（供主图合并）

1. **几何零端链**：局部模型不相容 → 有界Ricci／覆盖正则性下正体积好区域 → I42/I43/I45间隙；I48以明确椭圆条件给另一入口。I46环带与I47整个核心是另外的带标记障碍，尚未从纯积分输入自动接通。
2. **精确最优值链**：经典scalar预算+signature+经典恢复 → I44只添柄精确inf；它已经是全度量结果。平衡族的线性阶来自I40/I41，精确系数尚不由该链给出。
3. **首项稳定链**：I44纯W+帽支付 → I52受控规范二次稳定 → X09否定固定基底自动规范 → I53直接精确帽绕过该障碍；I55则以真实外部积分预算允许任意内部。X10证明外部预算不能由“竞争”自动供给。
4. **实际构造链**：I54完整单元稀疏植入把局部完整cost变成原族首项；Kähler/biaxial、nonconformal diagonal整类已排除；I55及新共形平方把剩余coupled窗口压到微观梯度＋宏观改动＋相交scalar误差。它仍是开放窗口。
5. **变分动力链**：I41负Yamabe／J归约 → 最佳二次功能量参数与光滑驻点限制 → I49有限流时间及条件下降；X06要求保留Weyl支付。不能把变分必要条件当极小存在／紧致性。
6. **本轮增量**：帽评分弱化可检查接口；一般任意振幅共形平方严格排除新范围；O11与Berger全曲率的一阶严格等价。三者都加强可用结构，但没有补齐一般弱积分O10、全度量O11或固定E_D全部Einstein判定。

记录原则：11卷保存的六份数值回执、28起点、未达容差与未收敛应完整保留；它们解释路线变化，不计为证明。I47 Calderbank–Singer、I44 LeBrun等为经典构造输入，新结果的来源关系应明确；“manuscript-theorem”不等于外部同行认证或优先权认证。
