# O11：极值方程的 Codazzi 分解及一个不能使用的非线性正性步骤

2026-09-29，续研 C。

本记继续检验 O11 的全局变分路线。结论是：可以把常负标量曲率下的第一变分写成一个具有明确正主部的双线性式，并准确识别其唯一零阶负势；但把这一算子代替此前的 rough-Laplacian resolvent 时，所需的有界性与非线性单调性并不自动保留。下文给出一个明确代数反例，排除后一种直接替换。

这不是 O11 最佳系数定理。对角 Cotton 估计已在整合稿中证明；此处不把它重新登记为新突破。新增记录是适用于任意无迹测试的完整双线性式、算子符号，以及非线性正性替换失效的具体计算。

## 1. 范数、符号和现有输入

设闭四维流形上 \(s=-4\)，令
\[
 Z=\operatorname{Ric}^{\circ}=\operatorname{Ric}+g,
 \qquad P=\int|Z|^2,\qquad S=\int s^2.
\]
采用正 rough Laplacian \(L=\nabla^*\nabla\)。对称二张量曲率作用记作
\[
 \operatorname{Rm}(H,K)=R_{ikjl}H^{ij}K^{kl},
 \qquad W(H,K)=W_{ikjl}H^{ij}K^{kl}.
\]
定义
\[
 C(H)_{ijk}=\nabla_kH_{ij}-\nabla_jH_{ik},
\]
其范数包含全部有序指标。常标量曲率给 \(\operatorname{div}Z=0\)。

标准第一变分为
\[
 \operatorname{grad}P=LZ-2\operatorname{Rm}(Z)+\tfrac12|Z|^2g,
 \qquad \operatorname{grad}S=8Z. \tag{1}
\]
来源核验：Gursky–Viaclovsky，*Rigidity and stability of Einstein metrics for quadratic curvature functionals*，arXiv:1105.4648，§2.1，式 (2.5)、(2.9)；将其非正 Laplacian 改为本文正号，取 \(P=\int|\operatorname{Ric}|^2-S/4\)，即得 (1)。

整合稿第 9440–9500、31173–31230 行已给相应对角 Cotton 恒等式与实际 Weyl 预算。本记沿用同一规范，不另加局部几何假设。

## 2. 对所有无迹测试成立的精确分解

**命题。** 任意光滑无迹对称二张量 \(H\)，不要求 \(\operatorname{div}H=0\)，均满足
\[
 \boxed{DP[H]
 =\frac12\int\langle C(Z),C(H)\rangle
   +\int\left\langle\left(\frac23I-W\right)Z,H\right\rangle.} \tag{2}
\]
因此，若 \(F_\gamma=P-\gamma S\)，并在变分时固定 \(\gamma\)，则
\[
 \boxed{DF_\gamma[H]
 =\frac12\int\langle C(Z),C(H)\rangle
   +\int\left\langle\left(\left(\frac23-8\gamma\right)I-W\right)Z,H\right\rangle.} \tag{3}
\]

**证明。** 极化 Cotton 分部积分式给
\[
 \frac12\int\langle C(Z),C(H)\rangle
 =\int\langle\nabla Z,\nabla H\rangle
   -\int\operatorname{Rm}(Z,H)
   +\int\operatorname{Ric}:ZH. \tag{4}
\]
其中散度双线性项为零，因为 \(\operatorname{div}Z=0\)；并不需要 \(\operatorname{div}H=0\)。由于 \(\operatorname{Ric}=-g+Z\)，
\[
 \operatorname{Ric}:ZH=-\langle Z,H\rangle+\operatorname{tr}(Z^2H).
\]
另一方面，在无迹张量上四维曲率分解给
\[
 \operatorname{Rm}(Z,H)
 =W(Z,H)+\frac13\langle Z,H\rangle-\operatorname{tr}(Z^2H). \tag{5}
\]
把 (4) 解出 \(\int\langle\nabla Z,\nabla H\rangle\)，代入 (1) 的无迹测试式
\[
 DP[H]=\int\langle\nabla Z,\nabla H\rangle
             -2\int\operatorname{Rm}(Z,H),
\]
再用 (5)，全部 \(\operatorname{tr}(Z^2H)\) 项精确相消，得到 (2)。式 (3) 由 \(DS[H]=8\int\langle Z,H\rangle\) 得到。证毕。

一个独立的系数检验：在两个曲率分别为 \(-1+a\)、\(-1-a\) 的曲面乘积上，\(Z=a(g_1-g_2)\) 平行，且 \(W(Z,Z)=-(4/3)|Z|^2\)。式 (2) 给 \(DP[Z]=2P\)。直接沿 \(g+tZ\) 计算两因子的面积和曲率，也给 \(DP[Z]=2P\)。

## 3. 算子主部确实椭圆，但不等于可直接使用的有界 resolvent

在无迹张量丛上，式 (3) 的分布算子是
\[
 K_\gamma Z:=\frac12C^*C Z+
       \left(\left(\frac23-8\gamma\right)I-W\right)Z.
\]
若 \(|\xi|=1\)，其二阶主符号的二次型为
\[
 \frac12|\sigma_C(\xi)H|^2=|H|^2-|H\xi|^2.
\]
对四维无迹对称 \(H\)，有
\[
 |H\xi|^2\le\frac34|H|^2,
\]
所以
\[
 \frac14|H|^2\le\frac12|\sigma_C(\xi)H|^2\le|H|^2. \tag{6}
\]
证明可取 \(\xi=e_1\)，将 \(H\) 写成首行列 \((a,b)\) 和剩余三阶块 \(B\)，用 \(\operatorname{tr}B=-a\) 与 \(|B|^2\ge a^2/3\)。

因此这是真正的强椭圆二阶系统。原族上令
\[
 \xi_W=(w_3^++w_3^--1/3)_+,
\]
实际场给 \(\int\xi_W^2=O(Q)\)，且零阶二次型满足
\[
 \left\langle\left(\left(\frac23-8\gamma\right)I-W\right)H,H\right\rangle
 \ge\left(\frac13-8\gamma-\xi_W\right)|H|^2. \tag{7}
\]

但 (6) 只是系统椭圆性；它没有给 Kato 支配或标量最大值原理。此前 \((L+\sqrt{1+|Z|^2})H=Z\) 的 \(L^\infty\) 控制，不能因此原样转移到 \(C^*C\) 系统。

## 4. 一个明确反例：径向单调映射不保持 Codazzi 配对正性

此前 rough-Laplacian resolvent 的正量证明使用
\[
 \mathcal F(U)=\frac{U}{\sqrt{1-|U|^2}},\qquad
 \langle D\mathcal F(U)V,V\rangle\ge|V|^2.
\]
这保证 \(\langle\nabla\mathcal F(H),\nabla H\rangle\ge0\)。若把 \(\nabla\) 换成 \(C\)，相应正性是假的。

下面是一个纯代数反例。取欧氏四维空间、\(\xi=e_1\)，并在无迹对称张量丛中令
\[
 U=\frac r{\sqrt2}\operatorname{diag}(1,-1,0,0),
 \qquad V=\operatorname{diag}(2,1,-3,0),\qquad 0<r<1.
\]
在某点指定 \(H=U\)、\(\partial_1H=V\)、其余方向导数为零。此一阶 jet 可由光滑无迹张量局部实现，并在充分小邻域保持 \(|H|<1\)。

置 \(f=(1-r^2)^{-1/2}\)，则
\[
 D\mathcal F(U)V=fV+f^3\langle U,V\rangle U.
\]
对 \(\xi=e_1\) 定义符号双线性式
\[
 B(A,B)=\langle A,B\rangle-\langle A\xi,B\xi\rangle.
\]
直接计算给
\[
 B(V,V)=10,\qquad
 \langle U,V\rangle=\frac r{\sqrt2},\qquad
 B(U,V)=-\frac r{\sqrt2}.
\]
因此
\[
 \boxed{\frac12\langle C(\mathcal F(H)),C(H)\rangle
   =10f-\frac{r^2}{2}f^3<0
   \quad\text{当}\quad r^2>\frac{20}{21}.} \tag{8}
\]
例如 \(r^2=99/100\) 时，右边为 \(-395\)。

这否定的是“直接照搬此前径向单调性积分证明”的局部被积式正性。它不排除某个另有全局补偿的积分定理，也不证明所有 Codazzi resolvent 方法无效；但若采用这种方法，必须另行证明所需有界性与补偿，不能从 \(D\mathcal F\ge I\) 推出。

## 5. 在精确临界点可得什么，以及为何尚不能用于一般近极小序列

若 \(g\) 是 \(F_\gamma\) 的光滑临界点，取 \(H=Z\) 得
\[
 \frac12\|C(Z)\|_2^2+
       \left(\frac13-8\gamma\right)P
       \le\int\xi_W|Z|^2. \tag{9}
\]
这就是整合稿已有对角 Cotton 信息；不是本轮新增下界。

在原平衡族上，\(\gamma=O(h)\)，已有更精确预算
\[
 \|\xi_W\|_2^2\le\frac89\{P+O(Ah^2)\}.
\]
当 \(P\asymp Q\) 时，(9) 的直接后果是
\[
 \int|Z|^4\ge\left(\frac18-o(1)\right)P. \tag{10}
\]
这说明一个光滑非 Einstein 临界点不可能让全部缺陷以幅度 \(O(\sqrt h)\) 均匀分布于 \(A\) 尺度主体。它必须保留较大的四阶矩。

然而本项目选定的一般近极小序列只在规定的有界临界测试类上近驻点。未经控制，\(H=Z\) 不属于该类，故不能把 (9)–(10) 宣布为这些序列已获得的结论。

对合法的自适应粗糙 resolvent 测试，(3) 当然成立，但
\[
 \frac12\int\langle C(Z),C(H)\rangle
\]
没有已证非负号。此前的正补偿 \(\mathfrak D(Z)\) 仍然有效；(8) 表明不能用一个形式替换把它升级为全局 Codazzi 强制。

## 6. 直接检验“驻点强迫标量松弛消失”的尝试

### 6.1 Yamabe 约束修正没有改变所需的一阶信息

令 \(H\) 无迹，先取 \(g_t=g+tH\)，再取其唯一标量 \(-4\) 的共形代表 \(\widehat g_t=u_t^2g_t\)，\(u_0=1\)。微分标量变换公式得到
\[
 (6\Delta+8)\dot u=-Ds[H],
 \qquad Ds[H]=\operatorname{div}\operatorname{div}H-\langle Z,H\rangle. \tag{11}
\]
闭流形上积分后，
\[
 \dot V=4\int\dot u=\frac12\int\langle Z,H\rangle,
 \qquad \dot S=16\dot V=8\int\langle Z,H\rangle. \tag{12}
\]
\(P\) 在常标量度量上的纯共形一阶变分为零，因此
\[
 \frac d{dt}P(\widehat g_t)\big|_0=DP[H]. \tag{13}
\]
所以转到 Yamabe 切片，不会把 \(DP\) 近零变成 \(DS\) 近零。对此前的自适应 \(H\)，
\[
 \int\langle Z,H\rangle=
 \int\bigl(|\nabla H|^2+\sqrt{1+|Z|^2}|H|^2\bigr)\ge0,
\]
且只能由当前预算控制为 \(O(Q)\)。

### 6.2 实际类预算的微分是另一项应力，不由驻点自动消掉

固定一个实际类 \(a\)，令 \(\alpha\) 为其调和二形式代表，按 de Rham 规范取 \([\alpha]=a\)。记 \(p=(a_g^+)^2\)，
\[
 T(\alpha)_{ij}=\alpha_{ik}\alpha_j{}^k-	frac14\alpha_{ab}\alpha^{ab}g_{ij}.
\]
调和性消去代表本身的一阶变化，给
\[
 p'[H]=-rac12\int\langle H,T(\alpha)\rangle
       =-\int H^{ij}\alpha^+_{ik}(\alpha^-)_j{}^k. \tag{14}
\]
因中维 Hodge 星共形不变，Yamabe 修正不改变此式。于是对于标准标量松弛量 \(\Sigma_a=S-32\pi^2p\)，
\[
 \Sigma_a'[H]=8\int\langle Z,H\rangle
                  +16\pi^2\int\langle H,T(\alpha)\rangle. \tag{15}
\]
不同实际符号类产生不同调和应力。已有单解相容性估计不使这些应力之和或所选项自动等于 \(-Z/(2\pi^2)\)。若要利用所有符号类，必须证明新的联合微分关系；只增加符号类的数目，不能从 (15) 得到所需符号。

此外，I41 对 \(\Sigma_a\) 给的是通常仍有 \(O(Q)\) 松弛的上界。一个具有 \(O(Q)\) 非零余量的不等式，不能直接微分成极小点处的符号约束。这里没有找到使这一步合法的新饱和估计。

### 6.3 一个严格的数值模型说明现有标量预算为何不够

本段只构造形式能量数据，不构造度量。用前轮规范
\[
 t=\frac P{8\pi^2Q},\qquad
 x=\frac{S-32\pi^2A}{32\pi^2Q},\qquad
 b=\frac{W_-}{2\pi^2Q}.
\]
在平衡比例的首阶，取任意固定 \(0<\eta<1/2\)，令
\[
 t(x)=1-2\eta x+\eta x^2,
 \qquad b(x)=t(x)+\frac13-\frac x3,
 \qquad 0\le x\le1+\delta
\]
其中 \(\delta>0\) 充分小。则
\[
 t+x-1=(1-2\eta)x+\eta x^2\ge0,
 \qquad b>0.
\]
因此 sharp Ricci 预算与负手性非负性均被满足。取形式投影预算 \(p=A\)，则直接由特征数恒等式得到
\[
 D_2=36\pi^2Q(x+t-1)\ge0,
 \qquad \frac{D_2}{18}+3W_-=P. \tag{16}
\]
这同时保留原平衡族最重要的首阶双手性预算。

在恢复端 \(x=0\)，有 \(t=1\)。然而在内点 \(x=1\)，
\[
 t'=0,\qquad t''=2\eta>0,
 \qquad t=1-\eta<1,
 \qquad S-32\pi^2A=32\pi^2Q.
\]
所以这些标量预算与严格二阶稳定，在逻辑上允许一个具有 \(Q\) 级标量松弛的较低极小值。它不是实际几何反例，也不声称满足全部实际场微分方程；它准确说明：**要排除这种图景，证明必须使用当前标量预算与驻点符号之外的实际几何信息。**

## 7. 对 O11 的实际状态更新

本记排除了一个具体的短证明漏洞：**不能因为 Codazzi 主部椭圆且径向纤维映射单调，就认为其 resolvent 自动具有此前 rough-Laplacian resolvent 的有界性与单调补偿。**

目前没有从这些变分关系推出 \(P\ge8\pi^2Q-o(Q)\)，也没有构造低于该阈值的原流形度量。缺失的内容仍是带有 \(Q\) 拓扑计数的全局补偿，而不是变分选择、测试合法性或正主部的形式识别。

本记应进入证明设计和失效路线记录，不应列为 O11 最优系数的完成报告。

## 8. 引用定位

- 主底本：`upload/27b3cef6-aeed-442c-9e66-fef1a757828e.tex`，常标量变分、实际 Cotton/Weyl 预算及原平衡族。
- 前轮：`O11_Positive_Curvature_Compensation.md`，径向单调映射在 rough-Laplacian resolvent 中的合法使用。
- 前轮：`O11_TT_Independent_Check.md`，一般无迹张量的 Cotton 积分恒等式。
- Gursky–Viaclovsky，arXiv:1105.4648，https://arxiv.org/pdf/1105.4648 ，§2.1，式 (2.5)、(2.9)。本记只借用经典第一变分公式，不将其局部 Einstein 稳定性定理套用于任意退化近极小序列。
