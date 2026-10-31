# 第一主线总图谱：物理与文献审计备忘

审计对象：`review/Qiushi_Line1_Research_20260928/03_物理迁移_场方程与重大问题.md`、`04_来源与继承核对.md`、`references.bib`，并核对卷02的M7–M9。本文供总图谱整合，不新增研究方向。

## 1. 中心与依赖链

物理支线的发动机仍是**实际规范供给下、对全度量成立的四维积分相容性强制估计，以及真实平衡族的线性积分gap**。物理名称不能倒过来替代这条主线。合理图谱顺序是：I40/I41 → 全尺度积分预算 → 指定拓扑/真实族的线性gap → 作用量、应力、手性及流残差的演绎接口 → 需要完整方程或边界理论的后续连接。

记P=∫|Ric°|²，R=∫|Ric|²，S₂=∫s²，S₁=∫s，V=Vol；p=(a⁺)²，T₊=2χ+3τ；D₂=(3/2)S₂+18∫|W⁺|²−72π²p。保留实际供给、p≥A、a²≥T₊、T₊=A(1−h)等原输入。

必须区分两级：M7给P+D₂≥cAh；只给P收费的M9还使用双手性窗口( U−1−h )₊≤(c/2)h。物理应力推论依赖M9，不能只由M7宣称无条件P gap。

## 2. 五组已经写清的直接演绎

| 接口与公式 | 现有科学内容 | 尚未由公式完成的部分 |
|---|---|---|
| 正耦合二次曲率作用量，P7：Iᵤᵥ=uP+v[(3/2)S₂+18∫|W⁺|²]；Iᵤᵥ−72π²vA≥min(u,v)36π²Ah/K_C，u,v>0，K_C=9/2+9C/8 | 从I41与精确恒等式直接推出；是明确、非空的全度量变分问题的下界。签名公式把它改写成uP+(3/2)vS₂+9v∫|W|²+108π²vτ，故除固定拓扑项外属于标准二次曲率项组合 | 不是任意二次引力耦合；下界锐利性、极小值是否达到、Euler–Lagrange鞍点、退化极小序列结构和相对既有文献的新窗口尚需独立证明。加入EH/宇宙学/物质项后须处理整个作用量 |
| Einstein–matter无迹应力，P10–P12：Ric°=κT°，故∫|T°|²≥C₀Ah/κ²；迹零时s=4Λ，若J=4P/R≥c_Jh，则P/(Λ²V)≥4c_Jh/(4−c_Jh) | 在同一适用几何范畴内，任一真实耦合解必须满足的代数推论；控制各向异性反作用 | 尚不保证该模型/磁通扇区存在解；不是质量、总能量或宇宙学常数下界。迹零归一化式要求Λ≠0、0<c_Jh<4 |
| 实欧氏Maxwell，P14–P15：|T|²=4|F⁺|²|F⁻|²，故∫|F⁺|²|F⁻|²≥C₀Ah/(4κ²) | 单位二形式范数|F|²=(1/2)FᵢⱼFⁱʲ下的精确恒等式；接原P gap得到手性重叠下界。在相同正Lie代数范数约定的Yang–Mills情形，|T|≤2|F⁺||F⁻|仍给相应下界 | 非阿贝尔颜色项可抵消，不能保留Maxwell等号。重叠积分不分别控制两手性L²能量；需完整Maxwell/YM方程、固定通量与能量控制来判断新非存在区或饱和态 |
| Levi-Civita手性块，P1–P2：Riemann曲率算子对Λ²₊⊕Λ²₋的非对角块B满足|B|²_HS=|Ric°|²/4，D_LC=4∫|B|²=P | 经典AHS结构的明确归一化；原gap可解释为两套必须来自同一度量的手性联络的相容性缺陷 | AHS等价关系本身非新成果；不是对任意独立规范联络的gap。换规范曲率迹范数需说明表示常数 |
| 一圈RG去尺度残差，P23：β⁽¹⁾=α′Ric，inf_λ∫|β⁽¹⁾−λg|²=α′²[P+(S₂−S₁²/V)/4] | 固定度量、无额外背景场、固定一圈约定时的正交投影恒等式；原积分gap约束此残差 | 尚未除去L_Xg等物理冗余；负Einstein通常仍沿整体尺度流动；B场、dilaton、高圈项及α′|Rm|控制未处理。不能据此排除一般CFT或弦真空 |

上述身份是“由新几何定理获得的物理量直接推论”，不是五项已经完成查新和完整模型闭合的独立物理突破。无需贬低其准确价值，也无需提升为未证结论。

特别纠正一个常见过度防御说法：只要当前拓扑/真实度量类别已保证原几何估计，对这个类别中的Einstein–Maxwell解应用P下界时，**并不需要把SW旋量当成电磁场、再从Maxwell方程重新证明SW供给**。SW仍可作为独立的辅助几何探针。真正未完成的是指定物理扇区的解存在性、最优性及新非存在判定；若越出原几何范畴，才需另证供给或替代机制。

全部式子使用正定欧氏四维。Lorentz签名下二形式*²=−1，现有实手性与正定估计不能直接挪用。

## 3. 只能作为条件扩展的现有支线

| 支线 | 目前已具备 | 总图谱应标出的桥梁 |
|---|---|---|
| 完整核心与曲率平方作用量 | I47的指定取向、指定锥领口、完整光滑填充锐利下确界；四维曲率平方缩放不变 | 实际作用量耦合、边界项、参考态；下确界不等于有极小元或物理鞍点。EH项缩放为r²，不能把I47代价原封解释成EH作用量 |
| 微观核心到宏观有效理论 | 宏观inf E≍h与个别核心代价 | 从原序列提取带实际规范/取向/边界标记的核心，跨尺度传递，处理neck和signed抵消，给出下极限及恢复序列。P18只是目标，不是已证Γ极限 |
| 欧氏引力鞍点与拓扑扇区 | 对适用闭流形的Einstein存在/逼近限制；明确二次泛函下界 | 选定边界/积分轮廓/完整作用量；鞍点、负模、规范固定、测度和涨落。几何残差gap既不是EH作用量gap也不是配分函数结论 |
| AdS/AHE填充 | 负Einstein方程的形式联系 | 当前主体闭紧四维；需非紧端、共形无穷远、边界项与重整化作用量理论。不可归入已完成推论 |
| BPS/超引力 | I40的校准背景消去可作为方法参照；经典模型有完整超协变方程 | 固定真实模型、实结构/轮廓、非零旋量归一化、完整费米变分及物质方程；P21尚未证明。SW旋量非自动Killing spinor，非Einstein非自动SUSY破缺 |
| 单值变换/KK紧化 | 固定E_D、Dehn twist及慢模态工作 | 区分四维总空间→二维基底有效理论与四维内部紧化空间；计算全模态作用量与误差，防止截断遗漏轻模/连接/混合张量。未证全系统真空不存在 |

## 4. 引力瞬子猜想：定义与关联强度

### 4.1 名称先固定

Li–Sun 2026采用：完整、非紧、定向、四维、Ricci-flat，且|Rm|=O(r⁻²)。该衰减与有限∫|Rm|²等价；此定义不假设hyper-Kähler。不同物理文献有更宽的instanton用法，因此不能把任意Einstein–Maxwell或负Einstein解无说明地纳入同一个分类猜想。

I47研究的指定取向1/n(1,−2)、n奇且≥3的完整核心填充，不是“任意Ricci-flat ALE空间”。其上界借用Calderbank–Singer经典scalar-flat Kähler ALE模型；scalar-flat不等于Ricci-flat。

### 4.2 Bando–Kasue–Nakajima/Gibbons问题

准确陈述为：任意完整、光滑、单连通、Ricci-flat ALE四维instantons是否hyper-Kähler。Araneda–Lucietti的Thm1.2只证明具有相容toric **Hermitian non-Kähler结构**、所述torus作用条件的情形为Eguchi–Hanson（相对于hyper-Kähler取向反向）。不能省略non-Kähler而宣称所有toric Hermitian ALE只有EH；一般hyper-Kähler A_k已提供更多模型。

与I47关系是局部端/取向/填充技术相邻，但未建立该猜想的直接部分解决。Ricci-flat时I47泛函变为4∫|W⁺|²，正下界不排除Ricci-flat，更不自动迫使一种Weyl手性消失。

### 4.3 Energy Finiteness Conjecture

Sun–Zhang Conj7.7：完整Ricci-flat四维，∫|Rm|²有限当且仅当有限拓扑型。Li–Sun Conj30以其instanton定义重述；Conj9另列“instanton有有限拓扑型”。这里的有限拓扑型是可光滑紧化为带边界紧流形，即其内部；不是仅有有限Betti数、有限Euler数或与R⁴同胚。

因此有限能量⇒有限拓扑型在一般塌缩、非特殊结构情形仍是待证方向，其逆否命题“无限拓扑型⇒无限能量”也是待证。Cheeger–Tian正则性、chopping及Gauss–Bonnet给衰减/能量关系和某种耗尽域Euler数稳定，不能将其直接升级为光滑端稳定。已知ALE和hyper-Kähler等子类并不覆盖一般问题。

**I47既不证明该猜想，也不否定它。**

1. I47被积量Q=|Ric°|²+4|W⁺|²+s²/12省略W⁻，不是全曲率能量。hyper-Kähler的复取向下Q≡0，但全曲率可非零；它不可能普遍检测该类拓扑复杂性。
2. 4π²(1−1/n)随n有统一上界，因而不能把n增长或相应填充拓扑复杂性增长直接计为线性Q费用。它按指定完整填充收费，不按每个拓扑生成元收费。
3. 另一方面，若已独立提取无限多个**互不相交、各自满足I47全套取向及领口合同**的核心，n≥3确实提供每核心至少8π²/3的Q费用，非负积分可相加，推出无限Q与无限全曲率能量。这是条件推论；决定性的未证桥梁是一般无限拓扑迫使这种核心提取。I47本身不提供该桥梁，no-loss仅针对已识别核心也不提供。
4. exotic R⁴与标准R⁴同胚，不能据此自动满足上述光滑有限型条件；是否存在完整Ricci-flat度量仍是文献明确问题。不要以这个名字制造已得到的反例或推论。

### 4.4 Einstein消奇与紧化：更近的比较对象

Biquard针对特定A₁/Eguchi–Hanson消奇有det R⁺(p)=0的曲率障碍，并在其非退化AHE框架构造解。Ozuch研究非塌缩Einstein四维退化与反向gluing、bubble树及具体消奇障碍。这些是I47/标记跨尺度工作更近的文献比较对象：它们约束“该极限能否由Einstein度量解析”，I47约束“指定完整填充最低积分费用”。两者输入和输出不同，不能互称自动推论。当前总图谱只保留比较与待桥接关系。

## 5. 交接稿R1–R18各自角色

| 文献 | 在总图谱中的角色 | 不应让它承担的证据任务 |
|---|---|---|
| R1 LeBrun 2001；R2 Kotschick 2004；R3 Ishida–LeBrun；R4 LeBrun convex geometry | 核心最近邻：SW/BF实际供给、曲率/体积/Yamabe变分、Einstein障碍、凸包与等号/拼接比较 | 不可概括成仅有“数值拓扑预算”，再由此放大当前创新；需逐项比较完整定理 |
| R5 Calderbank–Singer | I47锐利上界所用经典scalar-flat Kähler ALE构造 | 不是本项目新构造，也不是Ricci-flat分类结论 |
| R6 Atiyah–Hitchin–Singer | 手性曲率块和诱导联络的经典几何身份 | 非新量子规范理论结论 |
| R7 Witten | SW与超对称规范理论的历史/方程来源 | 不给一般BPS残差gap |
| R8 LeBrun Einstein–Maxwell | 物理直接最近邻：紧四维EM作为黎曼变分问题与SW/极值Kähler关系 | 不能跳过它而声称“SW首次联系EM” |
| R9 Stelle；R10 Salvio | 二次引力作用量、耦合与模型语境；R9原始工作，R10综述 | 不证明本gap的新颖性、量子一致性或ghost问题已解决 |
| R11 Festuccia–Seiberg | 曲空间刚性SUSY包含辅助场的模型依据 | 不能由非Einstein直接推SUSY破缺 |
| R12 Braides | Γ收敛的定义与方法要求 | 不是本项目Γ极限已经成立的证据 |
| R13 Ishida–Matsuo–Nakamura | Pin⁻(2)供给、Yamabe及Einstein障碍比较 | 扭曲/覆盖供给条件不可省略 |
| R14 PRL、R15 PRX官方标准 | 编辑标准的独立附录资料 | 不属于数学/物理结论的文献证据；总科学图谱宜降为附录 |
| R16 Dunajski–Gutowski–Sabra–Tod | 真实欧氏EM/SUSY anti-self-dual模型与分类 | 本项目BPS普遍gap仍待建立 |
| R17 Caldarelli–Klemm | Lorentzian N=2 D=4 gauged超引力完整解分类比较 | 不作欧氏定理直接引用 |
| R18 Carfora–Dappiaggi–Drago–Rinaldi | 一圈sigma RG与Ricci flow的模型联系 | P23以外的完整RG商空间或高圈结论尚未建立 |

## 6. 核对的一手文献入口

- Li–Sun, Geometry of Gravitational instantons (2026)：https://arxiv.org/html/2606.10443v1 ，Definition 1.1、Lemma 2.2 / Remark 2.3、Conjectures 9、30。
- Sun–Zhang, Collapsing geometry of hyperkähler 4-manifolds：https://arxiv.org/pdf/2108.12991 ，Conjecture 7.7。
- Araneda–Lucietti, All toric Hermitian ALE gravitational instantons：https://arxiv.org/html/2510.09291v1 ，Conjecture 1.1、Theorem 1.2。须区分2025初稿与2026修订日期。
- LeBrun, The Einstein–Maxwell Equations, Extremal Kähler Metrics, and Seiberg–Witten Theory：https://arxiv.org/abs/0803.3734 。
- Biquard, Désingularisation de métriques d'Einstein：https://arxiv.org/abs/1105.4904 。
- Ozuch, Noncollapsed degeneration of Einstein 4-manifolds II：https://arxiv.org/abs/1909.12960 。
- Carfora等一圈RG：https://arxiv.org/abs/1809.07652 。

它们用于定位外部问题及最近邻，不认证项目内部的解析证明。有限代数核验也不替代几何证明或物理模型查新。
