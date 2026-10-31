# 经典输入、实际供给与统一积分障碍的继承子图

内部合并片段；2026-09-28。核对依据是快照 `0b1490791be560203b86a7d9834dcdc3cbc83b41` 第01、05、07、09、10卷、续研报告附录06，以及 `outputs/Qiushi_Line1_Unified_Gap_20260928.md`。这里的“已证”指原稿已有对应证明及本次所核继承关系，不代表本轮重新认证全部外部文献。

## A. 统一记号与边类型

`input`：外部已有定理提供实际解、拓扑或恒等式；没有重新证明外部定理。
`implication`：前一节点在逐项满足假设后严格推出后一节点。
`extension`：保持原适用范围，同时加强结论或削弱输入；不是声称包含源论文所有结果。
`comparison`：比较同一对象上的不同判据，不能自动画成包含关系。

\[
T=T_+=2\chi+3\tau,\quad T_-=2\chi-3\tau,\quad
p=(a_g^+)^2,\quad P=\int|\mathrm{Ric}^{\circ}|^2,\quad R=\int|\mathrm{Ric}|^2,
\]
\[
\mathcal E=\inf_{\lambda\ne0}\frac{\int|\mathrm{Ric}-\lambda g|^2}{\lambda^2V},
\qquad \mathcal J=4P/R\le\mathcal E.
\]
旧全权重输入的量词是：对每个待测度量可选一个实际 Spin\(^c\) 结构；它在该共形类中固定，并对证明使用的每个正权重可解。类可跨共形类改变，无连续选类要求。新单解输入是：每个待测共形类为负，其标量曲率归一化为 \(-4\) 的 Yamabe 代表上有一个实际解；同一类有 \(p\ge A>0\) 和所需类平方预算。

## B. 四条经典供应链：准确输入及现有输出

| 节点 | 经典对象、实际输入与预算 | 本项目已建立的边与结果 | 证明定位及不能越过的边界 |
|---|---|---|---|
| C-LB：LeBrun 极化手术供给 | 基底 \(X\) 有非零普通 SW 不变量，保留正维插入；\(T_X>0\)，\(A=c^2\ge T_X\)。在 \(M=X\#k\overline{\mathbb{CP}}^2\#\ell(S^1\times S^3)\) 上，极化选符号取得 \(p\ge A\)、\(a^2=A-k\ge T_M=T_X-k-4\ell\)。一般型最小复曲面有 \(A=T_X=c_1^2(X)\)。 | `input` 进入原实际场校准；`implication` 得旧 \(\mathcal E+(T_M/A-2/3)_+\ge\varepsilon\)；`extension` N1 将其加强为 \(\mathcal J+(T_M/A-2/3)_+\ge\varepsilon'\)。从而恢复所列精确 Einstein 非存在范围并得到统一近似障碍及临界下方扩张。 | 07/Source1 §§9–10；07/Source9 `lebrun_stability_closure.md` §§1–2、Theorem3.3边界；LeBrun math/0003068 Prop3.2、Thm3.3、Cor3.4。\(b_+=1\) 必须保留 small-perturbation chamber 与 canonical chamber 核对，不能任取 chamber。 |
| C-K：Kotschick special monopole 框架 | 真正 monopole class 对所有度量有实际解；special 条件 \(a^2\ge T\)，虚维 \(\nu=(a^2-T)/4\ge0\)。在 \(a^2>0\) 时可取 \(A=a^2\)，因为 \(p=a^2+\|a^-\|^2\ge a^2\)。 | `input` 给旧与新定理所需类平方及实际供给；`extension` N1 给该正预算范畴的定量障碍。与 Theorem12 的 \(T\ge8\nu\) 作 `comparison`：若取 \(A=a^2\)，Einstein 输入要求更强的 \(T/a^2\ge2/3+\varepsilon'\)。 | 09/原审读§五及§九；Kotschick math/0306022 定义与Thm12。不可把任意 monopole class 自动当 special；不可把全部 special 类假定为正平方。Kotschick entropy paper math/0410215 是另一独立比较节点，不是这里的输入身份。 |
| C-BF：Ishida–LeBrun / Bauer–Furuta 供给 | \(r=2,3\) 个 simply connected symplectic \(X_i\)，\(b_+(X_i)\equiv3\pmod4\)，\(A=\sum c_1^2(X_i)>0\)。加 \(k\) 吹起和 \(m\) 柄，\(D=4(r-1)+k+4m\)，\(T=A-D\)。实际符号类有 \(p\ge A\)、\(a^2=A-k\)，故 \(a^2-T=4(r-1+m)\ge0\)。 | `input` stable cohomotopy 非消失产生实际普通 Spin\(^c\) 解，即使整流形 ordinary SW invariants 为零；`implication` 原二次双手性带；`extension` I41 新线性窗口有真实 geography 家族；N1 亦由同一输入成立。 | 07/Source7 `line1_bauer_furuta_geography.md` §§1–4；05/Source2 Part I §4。外部 Ishida–LeBrun math/0111228 Cor8、Thm9、Prop10、Cor11、ThmD；Bauer 非消失及 Braungardt–Kotschick geography 都仍是外部输入。四个正 \(b_+\) 连通和不能不加额外同余条件就沿用本表的 \(r=2,3\) 结论。 |
| C-Pin：Ishida–Matsuo–Nakamura 扭曲供给 | 固定非平凡双覆盖与 sign local system \(\ell\)，真实 Spin\(^c_-\) 结构，扭曲Euler类 \(a\in H^2(M;\ell)\)；每个 base 共形类上实际 Pin 解，投影 \(p\ge A>0\)、\(a^2\ge T\)。提升到 ordinary Spin\(^c\) 后 \(\tilde p=2p,\tilde a^2=2a^2,\tilde T=2T\)。 | `input` 只提供所需 deck-invariant 权重，不宣称 cover 任意非不变度量可解；`implication` 原统一积分 gap；`extension` I41 全部 Part I 及新单解 N1 均提升后应用再除2，常数无度数损失。 | 07/Source8 §§1–2；05/Source2 Part I §5；续研附录06 §4；IMN arXiv:1505.05948 §2、Prop8–9。不得把扭曲类直接视为 downstairs ordinary Chern类；不得从任意Pin模空间虚维公式推断 \(a^2\ge T\)。 |

### C-LB 的辅助外部输入

- Ozsváth–Szabó，math/0005268，Prop2.2、Remark2.3、Thm3.2：插入、吹起与添柄手术；非零插入须带入，新添每个 \(S^1\times S^3\) 带一个 loop insertion。
- Li–Liu，math/0012048，§2.1、Thm2.2：\(b_+=1\) 的 canonical chamber 与非消失；只有拓扑正平方不足以替代这一步。
- LeBrun，math/0611450，Lemma3.7：共形变换对应正权重方程；Hodge star 在四维二形式上不变，故同一结构与 \(p\) 保持。
- 这些边已在07/Source1 §§2、9及参考文献完整列出。

### C-Pin 的真实新对象及预算

07/Source8 §3：起始 \(M\) 有 \(b_+\ge2\) 及 odd ordinary SW class，\(c^2=A=T_M>0\)；\(N\) 有 \(b_+(N)=0\)，置 \(k=b_2(N),l=b_1(N)\)。
\[
Z=\#_{j=1}^{n}(S^2\times\Sigma_{r_j})\#\#_{i=1}^{m}(S^1\times Y_i),
\quad D=k+4l+\sum_j(8r_j-4)+4m.
\]
对 \(X=M\#N\#Z\)，真实Pin供给给 \(p\ge A,a^2=A-k,T_X=A-D\)，所以
\[
a^2-T_X=D-k\ge0,\qquad
\mathcal E_X+(1/3-D/A)_+\ge c_*.
\]
N1进一步把 \(\mathcal E_X\) 换成 \(\mathcal J_X\)。明确例子
\(M_j=\Sigma_2\times\Sigma_{3j+1}\)、\(Z_j=\#^{2j}(S^2\times T^2)\)，有 \(A_j=24j,D_j=8j,T_j/A_j=2/3\)，因此获得所有 \(j\)、所有度量统一正 gap。原稿明确 ordinary SW 与 ordinary BF invariants 在此为零，Pin供应链是真实新增适用范围，不可删去。

## C. 已完成继承链：旧输入如何进入新单解 N1

| 起点 → 终点 | 边型 | 严格步骤、状态 | 来源 |
|---|---|---|---|
| 旧共形供给 + \(p>0\) → 负 Yamabe 类 | implication | 若该类有非负常标量代表，其普通实际解满足 Weitzenböck，迫使spinor与 \(F^+\) 为零，与 \(p>0\) 矛盾。因此每个原适用类均为负。 | 05/Source2 Part I §1证明；07/Source1 §§2、8 |
| 负 Yamabe类 + 旧共形供给 → 单个 \(s=-4\) 实际解 | implication | 取唯一归一化负Yamabe代表；同一实际结构仍可解，将spinor常数缩放为项目权重2规范。\(p,a^2,T\) 不变。 | 同上；续研附录06 §§1、4 |
| 单个实际解 → 所有有限 \(\beta\ge2\) 的I51界 | extension | 同一个实际解的Weitzenböck、Hodge、曲率模型、Hessian及弱Bianchi估计；不比较不同权重解。 | 01/Source2 §2；续研附录06 §§1–4 |
| \(\beta=8\) 参数界 → N1 | implication | \(D_8=108\pi^2(T-2p/3)+(27/2)P\)，加单解标量预算与精确共形比较，得 \(\mathcal J+(T/A-2/3)_+\ge\varepsilon\)。 | 07/Source3 §8；`Qiushi_Line1_Unified_Gap_20260928.md` §§1–3 |
| N1 → 原积分母gap | extension | \(\mathcal E\ge\mathcal J\)。支付从“无迹Ricci+标量波动”加强为无迹Ricci本身。旧常数数值不声明保持，最佳常数未确定。 | 新统一稿§3；07/Source1 Thm1.2 |
| 单解 \(\beta=2\) → I40/I41线性强制 | extension | 保留 \(\Sigma\le C(\Pi+\sqrt{\Pi Y})\) 与 \((p-T)_+\) 控制；结合相反手性预算得线性窗口。 | 05/Source1 §§4–5；Source2 Part I §§1–3；续研附录06 §§2–4 |
| Pin base实际输入 → 单解N1及I41 | implication | 负Yamabe代表提升后为deck-invariant常标量代表；提升的普通实际解可直接应用分析，所有积分及拓扑同乘覆盖次数，归一化结论不变。 | 07/Source8 §§1–2；05/Source2 Part I §5；新统一稿§3 |

必须同时保留有限参数族和 \(\beta=2\) 的精细线性估计。仅 \(\mathcal J+(U-1-h)_+\ge ch\) 并不逻辑包含原近 \(1/3\) gap；原近 \(1/3\) gap 的严格回接由 \(\beta=8\) 提供。

## D. 正预算、零预算、Ricci-flat与类平方短缺

1. **正预算主范围。** 原母定理要求实际 \(p\ge A>0\)。一般型手术及BF/Pin实例明确给出。\(T_X>0\) 的LeBrun应用恢复其所列正预算障碍。以 \(\mathcal E=0\) 解释时只涵盖非零Einstein常数。

2. **Ricci-flat须独立排除。** 定义在Ricci-flat上给 \(\mathcal E=4\)，且 \(\mathcal J=4P/R\) 此时为 \(0/0\)，不得照代。旧实际正投影供应链给 \(\int s_-^2\ge32\pi^2A>0\)，故独立排除Ricci-flat；新单解输入要求所有相关类负Yamabe，也排除包含Ricci-flat的零Yamabe类。来源07/Source1 §8，Source7 §2末段。

3. **负拓扑预算。** 若 \(T_M<0\)，Chern–Weil独立排除Einstein，不需规范输入。对 \(R>0\)，\(\mathcal E=1+(12W_2-24\pi^2T_M+L_s)/R\)，所以 \(T_M\le0\Rightarrow\mathcal E\ge1\)；\(R=0\) 按定义 \(\mathcal E=4\)。来源07/Source9 “Theorem3.3: the positive budget and the zero corner”。

4. **零预算零手术例外。** \(T_X=D=0\) 不是非存在性结论；Einstein可为Ricci-flat且半平坦，K3是原稿明确的例子。原检查使用LeBrun March2000预印本，不能把其未限定表述跨该角点机械搬用，也不能声称期刊最终措辞已逐字核验。此限定不影响 \(c_1^2(X)>0\) 的一般型Cor3.4。来源同上。

5. **类平方短缺已经部分量化，但不是删除条件。** I40/I41保留
\[
Y=(T-a^2)_+,\quad \Pi=P+D_2,\quad
\Sigma,(p-T)_+\le C\{\Pi+\sqrt{\Pi Y}\}.
\]
在 \(T=A(1-h)\)、\(y=Y/A\) 下，已有窗口代价为 \(c h^2/(h+y)\)；当 \(y\le Lh\) 时仍为 \(ch/(1+L)\)。这是已证加强，来源05/Source1 §5.1、Source2 Part I §§1–3。

6. **N1类平方短缺形式已闭合，常数随短缺退化。** 本片段§H从保留成本的I51直接证明 \(\mathcal J+(T/A-2/3)_+\ge c/(1+y)\)，\(y=(T-a^2)_+/A\)。因此 \(y\le L\) 给统一 \(c/(1+L)\) gap；当 \(y=0\) 恢复N1的绝对常数范围。任意无界短缺下的无损统一常数及最佳短缺依赖未证明。旧07/Source1 §7(7.11)中依赖 \(C_A\) 的原 \(\mathcal E\)-gap是保留的历史分支，不再把“有界短缺的无迹Ricci版尚待推出”列为开放问题。

## E. 经典优化与BF完整类预算：已证和未证分开

| 节点或比较 | 已证内容 | 未证内容及其影响 | 来源 |
|---|---|---|---|
| 明确供给的BF符号集合 \(\mathcal C_0\) | 两种经典优化预算 \(\beta^2(\mathcal C_0)=\alpha^2(\mathcal C_0)=A\)。凸包正块系数≤1，exceptional负块只减平方；选包含两个canonical正方向且正交exceptional的最大正子空间实现上界。 | 未要求该抽象正子空间由实际度量实现；该代数优化不等于全部未知monopole类优化。 | 09/原审读§五（约行235–290） |
| 新BF线性家族 | \(h\to0\)，\(U=1+(1+\theta)h+O(h^2)\)，\(0<\theta<c_0\)。原二次带不迫使正gap，新I41线性壁给 \(\inf\mathcal J\ge c_2h\)。 | 没有该BF家族近Einstein恢复上界的声明；不能把CH平衡族的恢复序列转贴到BF geography家族。 | 05/Source2 Part I §4；09/§五 |
| 与Ishida–LeBrun ThmD、Kotschick Thm12、LeBrun双手性/Ricci预算比较 | 在这组已知供给预算A下：\(h<1/3\)；\(T\ge8\nu\)有余量；\(T_+\ge2A/3,T_-\ge A/3\)有余量；\(1+h\le e\le U\)有余量；优化包络 \(F(h)\le e\le U\)亦有余量。I41新增线性余量消除该区间。 | 不等于遍历世界上全部Einstein障碍，也不等于已排除未知其他实际类。 | 09/§五表格 |
| 完整monopole集合预算 | 已清楚识别精度需求：若完整预算 \(B=A(1+\delta)\)，经典Einstein必要条件改成 \(1+h+2\delta\le U\)。 | 若未知类使预算增加 \(O(Ah)\)，旧经典障碍可能也排除同一BF家族。尚需上控如 \(\alpha^2(M)=A+o(Ah)\)，或提供适用的真实标量能量上界。原稿未供给此类上界，不能套用复杂曲面KE拼接。 | 09/§五，原文明确开放 |

该缺口限制“这些具体光滑类型首次被任何方法排除Einstein”的历史优先性主张；**不影响**新分析定理、实际BF应用及相对已知符号集合的严格加强。

## F. 其他必须保留的经典节点

- **Chern–Weil / Hitchin–Thorpe**：恒等式与两手性非负能量是input；本项目加实际规范条件后的更强范围不覆盖所有四流形上经典定理的全部一般性。
- **LeBrun scalar–Weyl、Ricci能量、凸几何**：既是input又是comparison。经典作品已有实际方程、等号几何、锐能量与最小体积，不能描述成“只有拓扑代数”或“只给0/1”。07/Source9明确不从本gap推出LeBrun整篇的绝对Ricci能量下确界与最小体积结论。
- **Bauer非消失、Braungardt–Kotschick geography**：外部input，用以产生合法的BF光滑类型、同余与不变量；I41的新增量是其上的统一线性排斥。
- **Kotschick entropy / Besson–Courtois–Gallot关联输入**：07/Source6 §4单独比较degree-to-CH entropy限制，实际家族严格满足该限制，不能把它列为被新定理整体恢复的“四类供应链”之一。
- **经典sharp恢复／LeBrun Thm4.3**：提供原CH吹起添柄族的 \(4h/(1+h)\) 上界所用构造，是input；与新的线性下界合起来证明阶数，不自动给所有度量的首项4。

## G. 继承节点上的具体剩余任务

| 缺口 | 已有基础 | 严格完成条件 | 不应误记为未完成 |
|---|---|---|---|
| 新单解输入的严格新拓扑适用范围 | 普通/BF/Pin旧供给全部已兼容；N1和I41分析输入确实减少 | 供给一个旧定理范围未覆盖的自然实例，逐类验证负Yamabe、实际解、p与square预算，并推出新结论 | Pin提升和旧范畴覆盖已做完，不应反复列为桥梁 |
| 类平方短缺下N1最佳依赖 | 已证明 \(\mathcal J+(T/A-2/3)_+\ge c/(1+y)\)，故 \(y\le L\) 时有统一 \(c/(1+L)\) gap；同时保留I41的Y误差插值 | 确定最优短缺依赖，或以真实实例判定何种损失不可避免；新实例仍须有实际单解及 \(p\ge A>0\) | 有界短缺形式已经闭合，不再列为开放；任意无界y不能宣称无损常数 |
| BF完整monopole预算／更强优先性 | 已知 \(\mathcal C_0\) 精确优化A及新实际线性窗口 | 精确到 \(o(Ah)\) 的完整预算上控，或足以比较的实际曲率上界 | 新定理和实际应用的证明不等待此历史比较完成 |
| 最佳常数与线性首项 | N1绝对正常数；I40/I41阶数；原族恢复上界 | 对明确族确定最佳值与匹配构造（O11），不能用通用常数调优代替 | 统一正gap、全度量无迹Ricci支付、线性阶已是已证成果 |

## H. 本轮直接补出的短缺版N1：有界短缺不再列作开放问题

**带 \(1/(1+y)\) 损失的N1已经由保留类平方成本的I51直接推出；其最佳短缺依赖仍未确定。** D.6与G表已同步这一完成状态。不声称任意短缺下都保持无损绝对gap。

沿用N1的负Yamabe单解输入与 \(p\ge A>0\)，但不要求 \(a^2\ge T\)。在标量 \(-4\) 的代表上置
\[
Y=(T-a^2)_+,\quad y=Y/A,\quad b=(-a^2)_+/V,\quad
r=P/V,\quad d=(T/A-2/3)_+.
\]
第01卷Source2§2.3式(2.15)的保留成本版本及单解附录06给
\[
(1+b)\left(r+\frac{D_8}{8V}\right)\ge c_{8,\mathrm{raw}}>0.
\]
Chern–Weil与单解标量预算分别给
\[
\frac{(-T)_+}{V}\le\frac{r}{8\pi^2},\qquad
\frac AV\le\frac1{2\pi^2}.
\]
故
\[
b\le\frac{(-T)_++Y}{V}
\le\frac r{8\pi^2}+\frac y{2\pi^2}.
\]
若原度量 \(\mathcal J(g)<1\)，精确共形比较使
\(r\le4\mathcal J(g)/3<4/3\)，从而
\[
1+b\le1+\frac1{6\pi^2}+\frac y{2\pi^2}.
\]
N1中不依赖类平方条件的 \(D_8\) 上界仍为
\[
r+\frac{D_8}{8V}
\le\frac{43}{16}r+\frac{27}{4}d
\le\frac{27}{4}(\mathcal J(g)+d).
\]
因此
\[
\boxed{
\left(1+\frac1{6\pi^2}+\frac y{2\pi^2}\right)
(\mathcal J(g)+d)\ge\frac{4c_{8,\mathrm{raw}}}{27}.}
\]
对 \(\mathcal J(g)\ge1\) 分支直接取较小常数。置
\[
c=\min\left\{1,
\frac{4c_{8,\mathrm{raw}}}{27(1+1/(6\pi^2))}\right\},
\]
即在所有上述输入下得到
\[
\boxed{
\mathcal J(g)+\left(\frac TA-\frac23\right)_+
\ge\frac{c}{1+y},\qquad y=\frac{(T-a^2)_+}{A}.}
\]
若逐共形类供给可统一保证 \(y\le L\)，便有统一下界 \(c/(1+L)\)。\(\mathcal E\ge\mathcal J\) 给对应积分障碍；Pin提升使 \(Y,A\) 同倍缩放，\(y\) 不变，故同式下降。该推论只使用已写出的I51成本式、单解输入、Chern–Weil及共形恒等式；不使用新的供给定理，不宣称短缺依赖最优。
