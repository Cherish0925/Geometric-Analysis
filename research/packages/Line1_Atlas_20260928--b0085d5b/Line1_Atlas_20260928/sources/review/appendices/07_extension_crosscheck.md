# audit_zero.md 独立交叉核验

核验对象：`review/continuation_0b14907/audit_zero.md` 的 (A)–(H)。同时回查第四卷最终稿第7节、第一卷 I50/I51 的实际核心构造、第五卷 I41 §15.1 的固定双曲背景方程。

## 判断

在其明示的**固定外半径、受控光滑背景、同一实际解、spinor 幅度有界**条件下，正则性推导成立，数值指数可保留：

- `sup |nabla_{3A} tau| <= C(1+||F_A||_2)^4`；
- 实际简单核的固定半径延拓必须满足 `integral |F_A|² >= c ell^{-1/2}`；
- 对有界重叠延拓球的数量密度结论 (H) 及其 calibrated-fit 加强随之成立。

不是一般 O10；本结论中几何控制在整个固定外球上，不只在微观核上。

## 逐项检查

1. **阿贝尔 Coulomb 规范。** 球可缩，H1=0。对闭2形式 F 求绝对边界 Coulomb 原函数 a：da=F、delta a=0、a(normal)=0。线性 Hodge 估计给 `||a||_{W1p} <= C_p ||F||_p`，无需小曲率条件。若写相对一个非平坦固定背景联络，应写 `C(1+K)`，不必坚持 CK；后续本来用 L=1+K，不影响结论。gauge 在球上可取平方根，故 determinant gauge 与 spinor 的半权变换没有拓扑障碍。

2. **临界 Sobolev 没有错用。** 先由 aW12 得 aL4，利用幅度界和 D0Phi=−(1/2)c(a)Phi 得 PhiW14=O(L)。这里没有声称 W14 控制 C0。接着 Maxwell 源 `delta F=4i delta sigma(Phi)` 属 L4 且为 O(L)。先 p=2 Hodge，再 p=4 Hodge，获得 FW14=O(L)，最后只使用其向固定有限 p=8 的连续嵌入。这一步合法，常数仅依赖固定球、固定 p 与受控背景。

3. **第二次规范与多项式次数。** 在较小球重新取 Coulomb 规范，aW18=O(L)，因此 aL∞=O(L)。依次得到 PhiW18=O(L)、FW18=O(L)、aW28=O(L)。Dirac 的两次微分给 PhiW28=O(L²)、PhiW38=O(L³)。最高乘积 aD²Phi 为 O(L³)；DaDPhi 是 O(L²)，D²aPhi 是 O(L)。最后原始 amplitude 界用于最后一项。规范协变导数增加 aDPhi、DaPhi、a²Phi 等项，均不超过 O(L³)。

4. **torsion 次数。** 第四卷第二稿 (1.1) 给出 cubic torsion 在适配架下为 rho 乘 spinor 一阶导数的线性组合，故其规范不变导数满足 `|nabla tau| <= C(M² |nabla²Phi| + M |nabla Phi|²)`。因此安全次数为 L4，原稿 (A) 正确。既不需要 Phi 远离0，也不需要除以 rho。

5. **核心导数下界建议改成规范不变的一行证明。** 第四卷最终稿 (7.1) 的 C1 重标度展开意味着在固定 y-shell 上 `|tau_ell|(ell y)=|y|+o_C1(1)`。固定双曲背景缩放后趋欧氏，因此其物理径向导数满足 `|d|tau_ell|| >= c/ell`。Kato 点态不等式 `|d|tau||| <= |nabla_{3A}tau|` 立即给 (E)。无需单独依赖局部联络修正的规范大小。壳层远离零点，不存在绝对值函数不光滑问题。也可由原稿 (7.4) 的梯度 L2 能量 ~ell² 与壳层体积 ~ell4 直接推出同一 sup 下界。

6. **能量指数。** `c/ell <= C(1+K)^4` 给 K>=c'ell^{-1/4}−1，故 K²>=c''ell^{-1/2}（ell足够小）。指数转换无误。把 K 误认为曲率能量而非其平方根才会导致错误，此稿没有这种混淆。

7. **模型拟合误差。** `|F_A^+|<=C` 来自幅度界及同一常权重方程，`|K_-|<=C` 是 I51 的有界模型。因此 `||F^-−K_-||_2² >= (1/2)||F||_2²−C Vol` 正确。固定背景球体积一致受控，ell->0 时可吸收常数。对重叠数<=Lambda 的球求和，(H) 以及 epsilon_* 加强没有漏加 N 个常数，因为这些常数先逐球被发散主项吸收。

## 应保留的表述细节

- 正则性常数必须允许依赖足够阶的背景导数、统一椭圆性、固定内外半径与固定 amplitude 上界。材料的“smoothly bounded family”足以表达；不能仅写 C0 bounded geometry。
- 结论针对实际核心连同其原有 amplitude 和 derivative 标度的延拓，不能只从相同 torsion index 推出同一下界。高指数核的常数可以依赖固定 seed；未得到按 index 的统一收费。
- 一个 fixed-ball extension 的否定/发散不能直接应用到半径随 ell 缩小的 extension，也不能免费下推覆盖空间估计。
- 该推导是经典阿贝尔椭圆 bootstrapping 对已给核心的新的条件性应用；无需把局部正则性机制本身宣称原创。
