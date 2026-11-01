# TTCS Independent Branch Record

```json
{
  "step_id": 52,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step52_kernel_insertion_theorem.md",
    "Sessions/S1003A01/workspace/scripts/step52_exact_su2minus_fast.py",
    "Sessions/S1003A01/workspace/scripts/step52_analyze_Q.py",
    "Sessions/S1003A01/workspace/data/step52a/exact_su2minus_analysis.json",
    "Sessions/S1003A01/workspace/notes/step50_wminus_completed_square_and_general_KE_construction.md"
  ]
}
```

## Task

Verify the mathematics of Theorem 52.A (kernel-direction Burns insertion on an arbitrary Einstein four-manifold) and Lemma 52.C in workspace/notes/step52_kernel_insertion_theorem.md. Check specifically: (1) the SU(2)_- reduction in Section 2 (is the a^2 eps^2 CGB density really constant on S^3 for SU(2)_- -invariant data, and do the 10 tensors sym(v_i v_j)/u span all SU(2)_- -invariant degree-0 symmetric 2-tensors?), and whether the exact results in data/step52a/exact_su2minus_analysis.json (F_opt = -mu(mu - s/8) - |T|^2; family F = -|T|^2 with zero gradient; mixed-block linear term) are consistent with the script step52_exact_su2minus_fast.py and the convexity/averaging argument; (2) the W^- cross-term vanishing by SU(2)_- irreducibility; (3) the two-scale remainder argument of Section 3.2: Hadamard factorization R = r^4 z^2 rho, evenness in r via the antipodal map, the claim that only h2 and k0 enter rho(0,0), and the O(eps^2) control of core and outer transition; (4) Section 3.3: that the order-eps contribution equals minus an inner-boundary flux of a transgression form, that its leading constant is a U(2)_zeta-invariant linear function of Rm_p (so alpha s + beta W+(zeta,zeta)), that the r^1 term vanishes by parity, and that the Ch.5 CH construction legitimately calibrates beta = 12 alpha (does Ch.5's Bianchi-IX neck have the same leading flux as the additive normal-coordinate neck?); (5) Lemma 52.C: delta W+ = 0 with constant eigenvalues (a,-a/2,-a/2) forcing grad u = 0, and the Kahler eigenvalue contradiction; (6) the sign correction in Section 5 and Corollary 52.B. Report errors, missing steps, and any correction that changes the theorem statement, with precise repairs.

## Output

# 数学验证备忘录

## 总结

Theorem 52.A 的局部系数、两尺度积分以及 Lemma 52.C 的主要数学内容成立。精确二次型与脚本、JSON 数据相符；核方向上确有
\[
F=-|T|^2,
\qquad
P(g_\varepsilon)
=
P(g)+8\pi^2-4\pi^2|T|^2\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2).
\]

有三处需要明确修正或补证：

1. “任意 \(SU(2)_-\)-stable corrector class”必须改成对 Haar 平均封闭的线性或凸类；对全部光滑齐次零次 corrector 空间当然成立。
2. §3.3 仅从 Ch.5 的“无 \(\varepsilon\) 项”进行标定时，需要写出 Bianchi–IX neck 与法坐标加法 neck 的渐近等价。所给 Step 50 通量公式
   \[
   \ell=-R^+_p(\zeta,\zeta)
   \]
   可以直接替代这一步，并完整给出零点与符号。
3. Corollary 52.B 对“没有一阶或 \(\varepsilon^2\log\) 降低”的分类漏掉
   \[
   R^+_p=0\quad (s=0,\ W^+_p=0).
   \]
   Section 5 中“\(R^+<0\) off \(Z\)”也应显式置于 \(s<0\) 的情形；\(s=0\) 时还存在 \(R^+\equiv0\) 分支。

Theorem 52.A 本身不需要改变结论，只需把 §3.3 的通量论证写实或直接引用 Step 50 的通量计算。

---

## 1. \(SU(2)_-\) 约化与十维 invariant corrector 空间

### 1.1 球面密度确为常数

令 \(H=SU(2)_-\) 为与 \(J_1,J_2,J_3\) 对易的四维实表示。它在 \(S^3\) 上单传递：对任意 \(x\neq0\)，
\[
e_0(x)=\frac{x}{|x|},\qquad e_m(x)=\frac{J_mx}{|x|},\quad m=1,2,3
\]
构成一个随 \(H\) 等变移动的正交标架，且固定一个球面点的稳定子是平凡的。

当 \(W^-_p=\Ric^\circ_p=0\) 时，代数曲率张量只有 \(s\) 与 \(W^+\) 部分；\(SU(2)_-\) 在 \(\Lambda^+\) 上作用平凡，因此法坐标二阶项
\[
h_2=-\frac13R_{ikjl}x^kx^l
\]
是 \(H\)-等变的。\(k_B\) 以及十个 corrector 基元也同样等变。由曲率构造出的 \(a^2\varepsilon^2\) 标量密度于是满足
\[
q(hx)=q(x),\qquad h\in H.
\]
由于 \(H\) 在 \(S^3\) 上传递，\(q\) 为常数。

脚本取
\[
F=\frac1{8\pi^2}\int_{S^3}q\,d\Omega.
\]
因 \(\operatorname{Area}(S^3)=2\pi^2\)，确有
\[
F=\frac14q(x_0).
\]
因此 `step52_exact_su2minus_fast.py` 在单点 \(x_0\) 计算并除以 \(4\) 的做法正确。

### 1.2 十个张量确实张成全部 invariant 齐次零次对称张量

任一 \(H\)-invariant 齐次零次对称二阶张量 \(K\) 完全由 \(K(x_0)\in\operatorname{Sym}^2(\mathbb R^4)^*\) 决定。由于稳定子平凡，\(K(x_0)\) 不受额外代数条件约束。因此 invariant 空间维数就是
\[
\dim \operatorname{Sym}^2(\mathbb R^4)^*=10.
\]
在移动标架 \(v_0=x,\ v_m=J_mx\) 中，其基可取
\[
\frac{\operatorname{sym}(v_i\otimes v_j)}{|x|^2},
\qquad 0\le i\le j\le3.
\]
这正是脚本中的 `COR`。

这个结论依赖于“齐次零次”。若允许任意径向系数，还会出现径向函数；当前 neck ansatz 中没有这种自由度。

### 1.3 平均与凸性

corrector 的二次部分来自平坦度量处的线性化 chiral curvature：
\[
Q(k_0)
=
\frac1{8\pi^2}\int_{S^3}
\left(
4|D_\delta W^+[k_0]|^2
+\frac1{12}|D_\delta s[k_0]|^2
\right)d\Omega,
\]
因此为半正定二次型。全 \(F\) 是该二次型加上线性项与常数项，所以是凸函数。

对 Haar 平均
\[
\bar k_0=\int_H h\cdot k_0\,dh
\]
有
\[
F(\bar k_0)
\le \int_H F(h\cdot k_0)\,dh
=F(k_0).
\]
因此在全部光滑齐次零次 corrector 空间，或任何对 Haar 平均封闭的线性/凸子空间中，最优值可在十维 invariant 子空间中求得。

原文“any \(SU(2)_-\)-stable class”过宽：仅有群不变性而不对积分平均封闭的集合，不保证 \(\bar k_0\) 仍属于该集合。这里应改为：

> any \(SU(2)_-\)-invariant linear or convex corrector space closed under Haar averaging.

---

## 2. JSON 二次型与定理中的不变量公式

令
\[
w_{33}=-w_{11}-w_{22},\qquad
\mu_i=w_{ii}+\frac{s}{12},
\]
并令 \(\zeta=J_3\)。在 \(\zeta\) 为特征向量时，\(w_{13}=w_{23}=0\)。脚本使用剩余 \(U(1)_+\) 自由将一般情形的 \(w_{23}\) 置零。

`exact_su2minus_analysis.json` 给出
\[
F_{\rm opt}
=
\frac{
s^2+12s(w_{11}+w_{22})
-432w_{11}^2-288w_{11}w_{22}
-576w_{12}^2-432w_{22}^2
}{288}.
\]
直接整理得到
\[
F_{\rm opt}
=
-\mu_3\left(\mu_3-\frac{s}{8}\right)
-\left[
\frac{(w_{11}-w_{22})^2}{2}+2w_{12}^2
\right].
\]
方括号正是 \(\zeta^\perp\) 上二阶对称矩阵无迹部分的 Frobenius 范数：
\[
|T|^2=\frac{(\mu_1-\mu_2)^2}{2}+2(R^+_{12})^2.
\]
因此
\[
F_{\rm opt}
=
-\mu_\zeta\left(\mu_\zeta-\frac{s}{8}\right)-|T|^2.
\]

JSON 中
\[
F_{\rm opt}-\Phi=-2w_{12}^2
\]
不是矛盾；脚本里的 \(\Phi\) 只包含对角形式
\[
\frac{(\mu_1-\mu_2)^2}{2},
\]
而完整的 \(|T|^2\) 还包含 \(2w_{12}^2\)。Section 1 中
\[
|T|^2=(\mu_1-\mu_2)^2/2
\]
应注明“在将 \(\zeta^\perp\) 上的限制对角化后”。

### 2.1 kernel family

在
\[
\mu_3=0,\qquad w_{22}=\frac{s}{12}-w_{11},
\]
脚本代入
\[
A=-\frac{s}{12},
\]
以及
\[
c_4=\frac{7A}{4}+\frac{T_{11}}3,\quad
c_7=\frac{7A}{4}-\frac{T_{11}}3,\quad
c_9=\frac A2,\quad
c_5=\frac{2T_{12}}3
\]
后得到
\[
F=-|T|^2
\]
并且十个 \(c_i\) 导数全部为零。corrector Hessian 的谱为
\[
0^{\times4},\quad 2,\quad4^{\times3},\quad8^{\times2},
\]
故半正定。零梯度因此给出全局最小值，而不是仅给出一个驻点。

这与张量公式
\[
k_0^{\ker}
=
\frac{7A}{4}(P_1+P_2)+\frac A2P_3
+\frac13\sum_{i,j\le2}T_{ij}
\frac{(J_ix)\otimes(J_jx)}{|x|^2}
\]
完全一致；交叉项的脚本基元是
\[
\operatorname{sym}(v_1v_2^T)/u
=\frac{v_1v_2^T+v_2v_1^T}{2u},
\]
故系数必须是 \(2T_{12}/3\)。

在 CH 数值 \(s=-24,\ w_{11}=2,\ w_{22}=-4\) 下得到
\[
(c_4,c_7,c_9)=\left(\frac92,\frac52,1\right).
\]
JSON 的 `"CH_family_coeffs"` 第一项仍含 \(s,w_{11}\)，原因是 `subs(chs).subs(ker)` 的第二次代入重新引入了这两个符号，却没有再次执行 `subs(chs)`。这只是输出脚本的小错误；直接代入原公式确为 \(9/2\)。

另有一个复现细节：`step52_exact_su2minus_fast.py` 默认写入 `data/step52`，而 `step52_analyze_Q.py` 固定读取 `data/step52a`。生成现有 JSON 时必须设置 `OUTDIR=step52a`。

### 2.2 mixed block

数据中的精确项为
\[
\frac{2w_{13}}9(-9c_2+15c_6+7w_{13}).
\]
其中 \(c_2\) 没有二次项；它对应
\[
\frac{\operatorname{sym}(x\otimes J_2x)}{|x|^2}
\]
并与
\[
\mathcal L_{(\log r)J_2x}\delta
\]
仅差固定倍数。因此 \(w_{13}\ne0\) 时，沿 \(c_2\) 方向 \(F\) 无下端。

若同时 \(\langle R^+\zeta,\zeta\rangle=0\) 但 \(R^+\zeta\ne0\)，则在
\(\operatorname{span}\{\zeta,R^+\zeta\}\) 上的矩阵行列式小于零，所以 \(R^+\) 同时有正、负特征值。原文对此的几何解释正确。

---

## 3. \(W^-\) 部分

\((s,W^+)\)-jet、\(k_B\) 与 \(k_0^{\ker}\) 都属于 \(SU(2)_-\) 的平凡表示。\(W^-_p\) 是五维不可约 spin-2 表示，\(h_W\) 与自然构造出的 \(k_0^W\) 等变地依赖于 \(W^-_p\)。

任何 invariant 部分与 \(W^-\) 部分的积分交叉项，都会定义一个 \(SU(2)_-\)-不变线性泛函
\[
W^-_p\longmapsto \mathbb R.
\]
spin-2 的对偶中没有平凡子表示，所以这些交叉项为零。

这里要区分两件事：

- 不可约性消去的是线性于 \(W^-\) 的交叉项；
- 它不会自动消去允许出现的 \(|W^-|^2\)。

\(|W^-|^2\) 项为零还需要 Step 50 的两项输入：

1. 在 \(a^2\varepsilon^2\) 次数上，\(W^-\) 自项只有平坦线性化 source 的平方；
2. 精确恒等式
   \[
   D_\delta W^+[k_0^W]+D_\delta^2W^+[h_W,k_B]=0,
   \qquad
   D_\delta s[k_0^W]+D_\delta^2s[h_W,k_B]=0.
   \]

由此该平方逐点为零。于是
\[
F(k_0^{\ker}+k_0^W)=-|T|^2
\]
成立。Section 2 的文字最好明确引用“Step 50 的次数分解加精确 source 恒等式”，因为仅写“by irreducibility”不足以处理 \(|W^-|^2\)。

---

## 4. 两尺度余项

令
\[
\widehat g_{r,z}
=
\delta+G(r,x)+zk_B+zr^2k_0,
\qquad
G(r,x)=r^2h_2+r^3h_3+\cdots .
\]

### 4.1 偶性

反点映射 \(A(x)=-x\) 在四维的行列式为 \(+1\)，其在 \(S^3\) 上的度也是 \(+1\)。同时：

- \(k_B(-x)=k_B(x)\)；
- 所有 invariant 齐次零次 corrector 都是偶张量；
- \(k_0^W\) 也是偶张量；
- \(h_m(-x)=(-1)^mh_m(x)\)。

因此
\[
A^*\widehat g_{r,z}=\widehat g_{-r,z}
\]
并且球面积分满足
\[
\Psi(-r,z)=\Psi(r,z).
\]
所以 \(r\) 的奇次系数全部消失。

### 4.2 Hadamard 分解

在 \(r=0\) 时
\[
\widehat g_{0,z}=\delta+zk_B
\]
是平坦尺度的 Burns 度量，满足
\[
W^+=0,\qquad s=0.
\]
扰动从 \(r^2\) 开始，因此
\[
\mathcal C(\widehat g_{r,z})
=
r^2\mathcal C_2(z)+r^3\mathcal C_3(z)+\cdots ,
\]
从而
\[
\Psi(r,z)=O(r^4)
\]
且该估计对 \(z\in[0,1/4]\) 一致。

定义
\[
R(r,z)=\Psi(r,z)-\Psi(r,0)-z\,\partial_z\Psi(r,0).
\]
则
\[
R(r,0)=0,\qquad \partial_zR(r,0)=0,
\]
故可先写成 \(R=z^2R_2\)。另一方面前三个 \(r\)-导数均在 \(r=0\) 消失，所以再作 Hadamard 分解得到
\[
R=r^4z^2\rho(r,z),
\]
其中 \(\rho\) 光滑。由偶性，\(\rho\) 对 \(r\) 也是偶函数，因而
\[
|\rho(r,z)-\rho(0,0)|\le C(r^2+z).
\]

### 4.3 为什么 \(\rho(0,0)\) 只含 \(h_2,k_0\)

\(r^4\) 首项来自
\[
|\mathcal C_2(z)|^2.
\]
\(\mathcal C_2\) 只由度量中的 \(r^2\) 系数
\[
h_2+zk_0
\]
以及 Burns 参数 \(zk_B\) 决定。\(h_3\) 首次进入 \(r^3\mathcal C_3\)，\(h_4\) 首次进入更高次；它们都不能进入 \(r^4z^2\) 系数。因此
\[
\rho(0,0)=F(h_2,k_B,k_0).
\]

积分给出
\[
\int_{2\sqrt\varepsilon}^{T}R\frac{dr}{r}
=
\varepsilon^2
\int_{2\sqrt\varepsilon}^{T}
\rho\left(r,\frac{\varepsilon}{r^2}\right)\frac{dr}{r}.
\]
主项为
\[
\frac F2\varepsilon^2\log(1/\varepsilon)+O_T(\varepsilon^2),
\]
而误差满足
\[
\varepsilon^2\int_{2\sqrt\varepsilon}^{T}
\left(r^2+\frac{\varepsilon}{r^2}\right)\frac{dr}{r}
=O_T(\varepsilon^2).
\]
这部分推导正确。

### 4.4 core 与 outer transition

在 core 过渡环上用 \(x=\sqrt\varepsilon\,\hat x\) 缩放，
\[
\varepsilon^{-1}\Phi_{\sqrt\varepsilon}^*g_\varepsilon
=
g_{\rm Burns,1}+\varepsilon m_\varepsilon,
\]
且 \(m_\varepsilon\) 在固定环 \(1\le|\hat x|\le2\) 上一致有界。由于 Burns 的 \(\mathcal C\) 为零，
\[
f(g_{\rm Burns,1}+\varepsilon m_\varepsilon)=O(\varepsilon^2),
\]
故 core 为 \(O(\varepsilon^2)\)。被删去的背景小球体积为 \(O(\varepsilon^2)\)，背景曲率有界，因此其 \(f\)-积分同样为 \(O(\varepsilon^2)\)。

在 \(T\le r\le2T\) 上，
\[
f(g+\varepsilon\chi k)
=
f(g)+\varepsilon Df_g[\chi k]+O_T(\varepsilon^2).
\]
这里仅二阶 Taylor 余项是 \(O_T(\varepsilon^2)\)；线性项本身通常不是。它必须与 neck 的 \(z\)-线性项一起转化为通量。原文后续正是这样处理的，但 §3.2 单独阅读时应避免把整个 outer contribution 称为 \(O(\varepsilon^2)\)。

---

## 5. 一阶项与 transgression

Einstein 背景满足 \(\Ric^\circ=0\)，所以
\[
D\bigl(|\Ric^\circ|^2dV\bigr)_g[h]=0.
\]
由点态 CGB 恒等式，
\[
Df_g[h]
=
16\pi^2\,De_g[h]+24\pi^2\,Dl_g[h]
=
d\Theta_g(h),
\]
其中 \(\Theta_g(h)\) 对 \(h\) 线性且局部依赖于 \(g,h\) 及其导数。

neck 的 \(z\)-线性项与 outer transition 的线性项合起来正是
\[
\varepsilon\int_{r\ge2\sqrt\varepsilon}
Df_g[\chi_{\rm out}k].
\]
由于 \(\chi_{\rm out}k\) 在 \(r\ge2T\) 为零，Stokes 公式只留下内球面，且补域诱导的定向给出
\[
-\varepsilon\int_{S_{2\sqrt\varepsilon}}\Theta_g(k).
\]
原文的负号正确。

### 5.1 小球面展开

标准 Chern–Weil transgression 形如“背景曲率乘以连接变分”。在平坦背景处曲率为零，所以
\[
\Theta_\delta(k)=0.
\]
对 \(k_B=O(r^{-2})\)，有 \(\nabla k_B=O(r^{-3})\)，乘以球面体积 \(O(r^3)\) 后得到常数阶。对齐次零次 \(k_0\)，
\[
\nabla k_0=O(r^{-1}),
\]
故球面积分从 \(r^2\) 开始。因此
\[
\Lambda(r)
=
\varepsilon\left(\theta_2+\theta_3r+O(r^2)\right)
+\varepsilon O(r^2)_{k_0}.
\]

反点映射保持 \(k_B\)，而背景曲率的一阶 Taylor 项改变符号；相应球面积分保持不变，所以
\[
\theta_3=0.
\]
在 \(r=2\sqrt\varepsilon\) 且 \(\theta_2=0\) 时，
\[
\Lambda(2\sqrt\varepsilon)=O(\varepsilon^2).
\]

### 5.2 invariant 线性泛函

Burns tail 的稳定群是
\[
U(2)_\zeta\simeq U(1)_+\times SU(2)_-.
\]
代数曲率上的 \(U(2)_\zeta\)-不变线性泛函只有：

- 标量曲率 \(s\)；
- \(W^+(\zeta,\zeta)\)。

\(W^-\) 在 \(SU(2)_-\) 下为 spin-2，\(\Ric^\circ\in\Lambda^+\otimes\Lambda^-\) 也没有 \(SU(2)_-\) 不变线性分量。因此
\[
\theta_2=\alpha s+\beta W^+(\zeta,\zeta).
\]

### 5.3 CH 标定中缺少的显式比较

在 CH 点，
\[
s=-24,\qquad W^+(\zeta,\zeta)=2
\]
对垂直 kernel 方向成立。若 Ch.5 的 Bianchi–IX neck 在法坐标与 Burns 参数下满足
\[
g_{\varepsilon}^{\rm Ch5}-g_{\rm CH}
=
c\,\varepsilon k_B+\varepsilon q_0+o(\varepsilon r^0),
\qquad c\ne0,
\]
其中 \(q_0\) 为齐次零次项，且可能出现的坐标变换项具有零常数通量，那么 Ch.5 无 \(\varepsilon\) 项确实推出
\[
-24\alpha+2\beta=0,
\qquad \beta=12\alpha.
\]
齐次零次项只产生 \(O(\varepsilon r^2)\)，不会改变 \(\theta_2\)。

Step 52 只用一句“same two-scale form”代替了这个渐近比较；单独作为证明时少了上述展开。所给 Step 50 材料提供了更直接的替代：
\[
\mathcal B_\infty(h_2)
=
-8\pi^2\left(W^+(\zeta,\zeta)+\frac{s}{12}\right),
\]
即在 \(P/8\pi^2\) 归一化下
\[
\ell=-R^+_p(\zeta,\zeta).
\]
这个公式同时给出：

- kernel 方向的一阶项严格为零；
- \(\beta=12\alpha\)；
- 正特征值方向给出一阶降低；
- \(R^+(\zeta,\zeta)<0\) 给出一阶增加。

因此，把 Step 50 通量公式作为引理引用后，Theorem 52.A 的一阶部分完整闭合；不再需要依赖 Bianchi–IX 坐标比较。

---

## 6. Theorem 52.A 的系数

在
\[
R^+_p\zeta=0
\]
时，一阶项为零，且
\[
F=-|T|^2.
\]
归一化 neck 积分给出
\[
\frac1{8\pi^2}\Delta\!\int f
=
\frac F2\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2).
\]
又因 blow-up 使 \(2\chi+3\tau\) 减少 \(1\)，拓扑项增加 \(8\pi^2\)。所以
\[
P(g_\varepsilon)
=
P(g)+8\pi^2
+4\pi^2F\varepsilon^2\log(1/\varepsilon)
+O(\varepsilon^2),
\]
即
\[
\boxed{
P(g_\varepsilon)
=
P(g)+8\pi^2
-4\pi^2|T|^2\varepsilon^2\log(1/\varepsilon)
+O(\varepsilon^2).
}
\]
对于闭 Einstein 流形，\(P(g)=\int|\Ric^\circ|^2=0\)。若 \(T\ne0\)，则小 \(\varepsilon\) 时严格小于 \(8\pi^2\)。

KE 垂直方向的数值也一致：
\[
|T|^2=\frac{s^2}{32}.
\]
取 \(s=-24\) 得 \(|T|^2=18\)，于是
\[
-4\pi^2|T|^2=-72\pi^2,
\]
等价于
\[
\frac{P}{8\pi^2}
=
1-9\varepsilon^2\log(1/\varepsilon)+O(\varepsilon^2).
\]

---

## 7. Lemma 52.C

设
\[
W^+
=
\frac{3a}{2}\,u\otimes u-\frac a2 I_{\Lambda^+},
\qquad a=-\frac{s}{12},
\]
其中 \(u\) 是局部单位自对偶二形式。Einstein 条件给出
\[
\delta W^+=0.
\]
因 \(a\) 常数且 \(I_{\Lambda^+}\) 平行，
\[
\nabla^i(u_{ij}u_{kl})=0.
\]
展开：
\[
(\nabla^iu_{ij})u_{kl}+u_{ij}\nabla^iu_{kl}=0.
\]
与 \(u^{kl}\) 收缩。由于 \(|u|\) 常数，
\[
u^{kl}\nabla^iu_{kl}
=
\frac12\nabla^i|u|^2=0,
\]
所以
\[
\nabla^iu_{ij}=0.
\]
代回得到
\[
u_{ij}\nabla^iu_{kl}=0.
\]
任意非零自对偶二形式在四维都是非退化的；对单位归一化存在常数 \(c>0\) 使
\[
u_i{}^ku_k{}^j=-c\,\delta_i{}^j.
\]
故上式可逆地推出
\[
\nabla_m u_{kl}=0.
\]

平行自对偶二形式定义一个与给定定向相容的平行复结构，所以度量局部 Kähler。Kähler 四维度量满足
\[
W^+(u)=\frac{s}{6}u
\]
对 Kähler 形式方向成立；但当前谱给出
\[
W^+(u)=a\,u=-\frac{s}{12}u.
\]
因此
\[
\frac{s}{6}=-\frac{s}{12},
\]
从而 \(s=0\)，与 \(s<0\) 矛盾。Lemma 52.C 正确。

特征线可能整体不可定向并无影响：上述推导只需在每个小坐标邻域选择 \(u\)。

---

## 8. Section 5 与 Corollary 52.B 的精确修正

对特征方向 \(\zeta\)，局部展开的前两项为
\[
\frac{P(g_\varepsilon)-P(g)-8\pi^2}{8\pi^2}
=
-\mu_\zeta\varepsilon
+\frac12\left[
-\mu_\zeta\left(\mu_\zeta-\frac{s}{8}\right)-|T|^2
\right]
\varepsilon^2\log(1/\varepsilon)
+O(\varepsilon^2),
\]
其中第一项采用 Step 50 的 Burns 参数归一化。

因此：

- 若 \(R^+\) 有正特征值，取相应特征方向，一阶项降低；
- 若 \(R^+\le0\) 且有 kernel 方向，只有在该方向 \(T\ne0\) 时出现 \(\varepsilon^2\log\) 降低；
- 若 \(R^+<0\)，所有方向的一阶项均增加，log 项无论何符号都处于次阶。

原文关于 strictly \(R^+<0\) 时
\[
W^+=0
\quad\Longrightarrow\quad
F=\frac{s^2}{288}>0
\]
的符号修正完全正确。\(F\le0\) 只是在 kernel 上成立。

### Corollary 52.B 漏掉的情形

当 \(R^+\le0\) 且没有正特征值时，没有上述两种降低的情形应精确分为：

1. \(R^+<0\)；
2. \(s<0\)，且
   \[
   \operatorname{spec}(R^+)=\left(0,\frac{s}{8},\frac{s}{8}\right),
   \]
   即 simple kernel 且 \(T=0\)，等价于
   \[
   \operatorname{spec}(W^+)
   =
   \left(-\frac{s}{12},\frac{s}{24},\frac{s}{24}\right);
   \]
3. \(R^+=0\)，等价于
   \[
   s=0,\qquad W^+=0.
   \]

第三项在原来的 “iff” 中缺失。Ricci-flat 情形下若 \(W^+\ne0\)，因 \(W^+\) 无迹，必有正特征值；但 \(W^+=0\) 时确实没有一阶或当前 log 阶降低。

### Section 5 的 \(Z\) 叙述

在 \(s<0\) 且 surviving pointwise condition 为 \(R^+\le0\) 时，排除 \(T\ne0\) kernel 点后，非严格点只能具有 simple-kernel 谱
\[
\left(0,\frac{s}{8},\frac{s}{8}\right).
\]
对应的 \(W^+\) 谱正是 Lemma 52.C 中
\[
\left(-\frac{s}{12},\frac{s}{24},\frac{s}{24}\right).
\]
故接触集 \(Z\) 闭且内点为空，进而 \(R^+<0\) 在 \(X\setminus Z\) 上成立。

若不先写 \(s<0\)，则 \(s=0,\ R^+\equiv0\) 会使 \(Z\) 可能等于整个开集，而 Lemma 52.C 不适用。因此 Section 5 的相应句子应显式加入 \(s<0\)。

在 \(s<0\) 下，
\[
R^+\le0
\quad\Longrightarrow\quad
|W^+|^2\le\frac{s^2}{24}.
\]
等号对应
\[
\operatorname{spec}(R^+)=\left(\frac{s}{4},0,0\right),
\]
即二维 kernel；任取 kernel 方向都有 \(T\ne0\)，已由 Theorem 52.A 排除。因此 surviving configuration 中等号确实处处不出现。