# TTCS Independent Branch Record

```json
{
  "step_id": 39,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "usable": true,
  "partial": false,
  "context_files": [
    "Sessions/S1003A01/workspace/notes/step39_actual_harmonic_zero_test_and_route_comparison.md",
    "Sessions/S1003A01/workspace/scripts/step39_harmonic_zero_profile.py",
    "Sessions/S1003A01/workspace/data/step39/harmonic_zero_certifiedprofile_x003_X128.json",
    "Sessions/S1003A01/workspace/data/step39/harmonic_zero_x0038_X128.json",
    "Sessions/S1003A01/workspace/notes/step28_AK_gap_identity_nijenhuis_transport.md",
    "Sessions/S1003A01/workspace/notes/step29_boundary_corrected_AK_exterior_and_contact_capacity.md",
    "Sessions/S1003A02/workspace/notes/step42_ak_torsion_profile_taubes_goldberg.md",
    "Sessions/S1003A02/workspace/notes/step44_perturbative_ke_coercivity_and_pocket_price.md"
  ]
}
```

## Task

Independently check the Step-39 actual harmonic-zero test object and its computed/scaled quantities. Verify the differential-geometric assertions: collar gluing gives a smooth closed self-dual harmonic form on the closed replicated metric; zero exceptional period and bolt vanishing are consistent; the sixfold scaling of q, amplitude defect, one-derivative form energy, Weyl-model error, and Ricci cost is correct; the negative-Kähler target used in the script has the stated original-scale eigenvalues; eta=1 is justified for the fixed pullback Kähler cohomology class but not arbitrary directions; and the singular hatted AK s* calculation cannot directly invoke closed AKGamma. Read the script and JSONs rather than trusting the note. Identify any normalization or logical error and give corrected formulas/numbers. Then assess only what the evidence establishes about localized O(k) form cost versus a diffuse construction.

## Output

# Step 39 科学核验备忘

## 1. 闭合调和形式的几何构造

令
\[
g=dt^2+a_f^2\sigma_f^2+a_g^2\sigma_g^2+a_h^2\sigma_h^2,
\qquad d\sigma_f=2\sigma_g\wedge\sigma_h,
\]
并取定向使得 \(*e^{0f}=e^{gh}\)。则
\[
\Omega=\frac12d(\phi\sigma_f)
=\frac{\phi'}{2a_f}e^{0f}+\frac{\phi}{a_ga_h}e^{gh}.
\]
由
\[
\frac{\phi'}{\phi}=\frac{2a_f}{a_ga_h}
\]
可得
\[
\Omega=u^2(e^{0f}+e^{gh}),\qquad
u^2=\frac{\phi}{a_ga_h},\qquad
|\Omega|_g^2=2u^4.
\]
因此在 \(u>0\) 处它确为闭、自对偶二形式。四维中
\[
d\Omega=0,\qquad *\Omega=\Omega
\quad\Longrightarrow\quad
d^*\Omega=-*d*\Omega=0,
\]
所以它是调和形式。

### 螺栓处

Step 28 给出的光滑 \(O(-1)\) 螺栓展开为
\[
a_f=b+O(t^2),\qquad a_g=b+O(t^2),\qquad
a_h=t+O(t^3),
\]
相应 ODE 给出
\[
\phi=Ct^2(1+O(t^2)),\qquad
u^2=\frac{C}{b}t+O(t^3).
\]
势 \(\phi\sigma_f\) 是光滑、二阶消失的不变一形式，故其外微分光滑；同时
\[
\Omega|_{E}=0.
\]
因而螺栓球 \(E\) 上的周期为零：
\[
\int_E\Omega=0.
\]
这里“周期为零”和“整张螺栓球上消失”是此对称模型的具体性质；一般二形式的零周期并不推出逐点消失。

### CH 领圈及闭流形粘接

在精确 CH 领圈上，Kähler 恒等式为
\[
(a_ga_h)'=2a_f.
\]
因此 \(\phi=a_ga_h\) 满足同一 ODE。脚本在外端取 \(\phi(X)=X=a_ga_h(X)\)，故在整个精确领圈上
\[
\phi=a_ga_h,\qquad
\Omega=\frac12d(a_ga_h\sigma_f)=\omega_{\rm CH}.
\]
它与未改动宿主上的 Kähler 形式逐点相同，不需要截断函数。多个互不相交胞元复制后，得到闭流形上的光滑闭自对偶形式；它在每张螺栓球上消失。JSON 中的 `closed_self_dual_harmonic: true` 本身只是写入的元数据，真正依据是上述 ODE、螺栓展开和精确领圈相等关系。

这也与 Taubes 的周期论述相容：该形式具有零点，并非处处非退化的辛形式。

---

## 2. 六倍缩放核验

置
\[
\bar g=6g,\qquad \psi=6\Omega.
\]
若 \(\operatorname{Ric}_g=-6g\) 在 CH 区域成立，则
\[
\operatorname{Ric}_{\bar g}=\operatorname{Ric}_g=-6g=-\bar g.
\]
四维常数缩放满足
\[
dV_{\bar g}=36\,dV_g,\qquad
*_{\bar g}|_{\Lambda^2}=*_g|_{\Lambda^2}.
\]

### 2.1 振幅

二形式范数满足
\[
|\psi|_{\bar g}^2
=|6\Omega|_{6g}^2
=36\cdot6^{-2}|\Omega|_g^2
=|\Omega|_g^2=q.
\]
故
\[
q=2u^4
\]
在缩放前后不变，而
\[
\int(q-2)^2\,dV_{\bar g}
=36\int(q-2)^2\,dV_g.
\]
脚本中的因子 \(36\) 正确。

### 2.2 一阶二形式能量

联络在常数缩放下不变，\(\nabla\psi=6\nabla\Omega\)。三协变指标张量范数给出
\[
|\nabla\psi|_{\bar g}^2
=6^2\,6^{-3}|\nabla\Omega|_g^2
=\frac16|\nabla\Omega|_g^2.
\]
乘以体积后
\[
\int|\nabla\psi|_{\bar g}^2dV_{\bar g}
=6\int|\nabla\Omega|_g^2dV_g.
\]
脚本中的因子 \(6\) 正确。

脚本使用调和二形式 Weitzenböck 恒等式
\[
\int|\nabla\Omega|^2
=\int \left(2W^+(\Omega,\Omega)-\frac{s}{3}|\Omega|^2\right)dV.
\]
由于 \(\Omega\) 沿第一个自对偶本征方向，
\[
2W^+(\Omega,\Omega)-\frac{s}{3}|\Omega|^2
=q\left(2W_{ff}^+-\frac{s}{3}\right),
\]
正是
```python
grad_density = W * qform * (2 * Wff - scal / 3)
```
所用表达式。外端位于平行 Kähler 领圈，端面分部积分项为零；螺栓是光滑内部子流形。该密度可以局部取负值，因此 JSON 中约 \(-1.87\)、\(-2.89\) 的最小值不与总能量非负冲突。

### 2.3 Weyl 模型

若
\[
A_{\psi,1/2}=-\frac12(\psi\otimes\psi)_0
\]
作为 \(\Lambda^+\) 上的迹零算子，沿 \(\psi\) 及其正交补的本征值为
\[
\left(-\frac q3,\frac q6,\frac q6\right).
\]
在原始 \(\operatorname{Ric}=-6g\) 曲率单位中，应比较
\[
6A_{\psi,1/2}
=\operatorname{diag}(-2q,q,q),
\]
这正是脚本的
```python
kahler_target_original_scale = [-2*q, q, q].
```
在 CH 领圈 \(q=2\)，目标为
\[
(-4,2,2),
\]
恰等于标量曲率 \(-24\) 的 Kähler–Einstein \(W^+\) 本征值。

因 \(W_{\bar g}^+=W_g^+/6\)，
\[
\int_{\bar g}|W_{\bar g}^+-A_{\psi,1/2}|^2dV_{\bar g}
=
\int_g|W_g^+-6A_{\psi,1/2}|^2dV_g.
\]
所以脚本所算 Weyl 模型误差确实在这组配对缩放下不变。

### 2.4 Ricci 项

迹零 Ricci 作用量满足
\[
\int|\operatorname{Ric}_{\bar g}^{\circ}|_{\bar g}^2dV_{\bar g}
=
\int|\operatorname{Ric}_g^{\circ}|_g^2dV_g.
\]
脚本没有乘六；它把记录中的
\[
J=\frac{P}{8\pi^2},\qquad P=\int|\operatorname{Ric}^{\circ}|^2,
\]
转为以 \(2\pi^2\) 为单位：
\[
\frac{P}{2\pi^2}=4J.
\]
这里的因子 \(4\) 是归一化单位转换，不是度量缩放因子。

---

## 3. 一个实质性的 Ricci 公式不一致

Step 39 文本将分支分子写成
\[
\int\Bigl(|\operatorname{Ric}_{\bar g}+\bar g|^2
+|W^+-A_{\psi,1/2}|^2+(q-2)^2\Bigr)dV_{\bar g},
\]
但脚本实际加入的是
\[
P=\int|\operatorname{Ric}_{\bar g}^{\circ}|^2dV_{\bar g}.
\]
两者只有在 \(s_{\bar g}\equiv-4\) 时相同，而 JSON 显示原始标量曲率并不恒为 \(-24\)：

- certified profile：约 \([-24.45771,-23.99968]\)；
- floating profile：约 \([-24.02673,-23.95444]\)。

精确分解为
\[
|\operatorname{Ric}_{\bar g}+\bar g|^2
=
|\operatorname{Ric}_{\bar g}^{\circ}|^2
+\frac14(s_{\bar g}+4)^2.
\]
换回原始尺度，
\[
\int_{\bar g}\frac14(s_{\bar g}+4)^2dV_{\bar g}
=
\int_g\frac14(s_g+24)^2dV_g.
\]
因此：

- 若分支泛函采用 \(|\operatorname{Ric}^{\circ}|^2\)，JSON 数字正确，Step 39 的显示公式应将 \(|\operatorname{Ric}+\bar g|^2\) 改为 \(|\operatorname{Ric}^{\circ}|^2\)。
- 若确实采用 \(|\operatorname{Ric}+\bar g|^2\)，则当前数字缺少
  \[
  I_s:=\frac1{2\pi^2}\int_g\frac{(s_g+24)^2}{4}\,dV_g>0.
  \]

脚本中相应的修正量就是
```python
scalar_Einstein_over_2pi2 = integ_dt(W * (scal + 24.0)**2 / 4.0)
```
完整分子应为
\[
4J+I_s+\text{Weyl error}+36\,\text{amplitude error}.
\]
现有 JSON 没有储存 \(I_s\)，所以不能从这两个 JSON 单独恢复其数值。

---

## 4. 数值重算

所有下列数值仍以实际积分除以 \(2\pi^2\) 表示。

### Certified coefficient profile

\[
36(0.0021273360285258345)
=0.07658409702693005,
\]
\[
6(0.0754119998065093)
=0.4524719988390558.
\]
Weyl 模型误差为
\[
0.02240536774440919.
\]
故纯形式项为
\[
0.07658409702693005+0.02240536774440919
=0.09898946477133924,
\]
若再加入一阶能量，则为
\[
0.5514614636103950.
\]
迹零 Ricci 数值为
\[
4J=3.9826806443720573.
\]
因此脚本中的两个和数完全一致：
\[
3.9826806443720573+0.09898946477133924
=4.0816701091433965,
\]
\[
4.0816701091433965+0.4524719988390558
=4.534142107982452.
\]

### Floating profile

\[
36(0.0030491974221540353)
=0.10977110719754526,
\]
\[
6(0.09818744461847811)
=0.5891246677108687.
\]
Weyl 模型误差为
\[
0.03361064226893610.
\]
故纯形式项为
\[
0.14338174946648136,
\]
连同一阶能量为
\[
0.7325064171773501.
\]
再加入迹零 Ricci：
\[
3.9811508676845797+0.14338174946648136
=4.124532617151061,
\]
\[
4.124532617151061+0.5891246677108687
=4.713657284861930.
\]

这些形式积分是普通双精度/JAX–SciPy 数值；Arb 包围只覆盖记录中的 Ricci 作用量，并未覆盖振幅、梯度或 Weyl 模型积分。

### 体积钉扎

由 ODE 可直接推出
\[
(\phi^2)'=4Wu^4,
\qquad
\int Wu^4dt=\frac{\phi(X)^2-\phi(0)^2}{4}=\frac{X^2}{4}.
\]
因此 \(X=128\) 时精确目标为 \(4096\)。脚本得到：

- certified：\(4096.000000007811\)，相对偏差约 \(1.91\times10^{-12}\)；
- floating：\(4095.999999998188\)，相对偏差约 \(4.42\times10^{-13}\)。

同时
\[
\int q\,dV_g=2\int u^4dV_g=\frac{X^2}{2},
\]
也与 JSON 一致。该测试主要确认数值积分与势函数归一化保持了 ODE 的精确积分关系。

---

## 5. 上同调类与 \(\eta\)

这里有一个符号归一化需要澄清。用
\[
[\beta]_{2\pi}:=\frac{[\beta]}{2\pi}
\]
表示积分上同调归一化。

在原始 \(\operatorname{Ric}=-6g\) 的宿主上，Ricci 形式满足
\[
\rho=-6\Omega,\qquad \frac{[\rho]}{2\pi}=-K_X,
\]
故
\[
[\Omega]_{2\pi}=\frac16K_X.
\]
闭流形粘接后，零 exceptional 周期排除了所有 \(E_i\) 分量，因此
\[
[\Omega]_{2\pi}=\frac16\pi^*K_X,
\]
从而
\[
[\Omega]_{2\pi}^2=\frac{A}{36},
\qquad
K_X\cdot[\Omega]_{2\pi}=\frac A6.
\]

六倍缩放后 \(\psi=6\Omega\)，于是
\[
[\psi]_{2\pi}=\pi^*K_X,\qquad
[\psi]_{2\pi}^2=A,\qquad
K_X\cdot[\psi]_{2\pi}=A.
\]
所以 Step 39 的
\[
[\Omega]^2=A,\qquad K_X\cdot[\Omega]=A
\]
只有在 \(\Omega\) 被重新用于表示缩放后的 \(\psi\)，或已隐含六倍归一化时才正确。对脚本开头的原始 \(\Omega\)，应使用 \(A/36\) 和 \(A/6\)。

不过角量是齐次零次的：
\[
\eta(\Omega)
=\frac{|K_X\cdot[\Omega]_{2\pi}|}
{\sqrt{A[\Omega]_{2\pi}^2}}
=\frac{A/6}{\sqrt{A(A/36)}}=1,
\]
且
\[
\eta(\psi)=1.
\]
因此 \(\eta=1\) 的结论正确，错误只在未说明六倍归一化时把原始 \(\Omega\) 的平方写成了 \(A\)。

对任意调和自对偶方向则不能推出 \(\eta\ge1\)。当 \(b^+>1\) 时，正平方锥不是一维 Lorentz 平面；方向可以含有与 \(K_X\) 正交的正平方分量，故 \(|K_X\cdot[\omega]|\) 可以相对于 \([\omega]^2\) 很小。这里的 \(\eta=1\) 来自固定 pullback Kähler 类，而非任意自对偶调和方向的普遍性质。

---

## 6. 奇异 almost-Kähler 量

在 \(u>0\) 的补集上，
\[
\widehat g=u^2g,\qquad
|\Omega|_{\widehat g}^2=u^{-4}|\Omega|_g^2=2,
\]
所以 \((\widehat g,\Omega)\) 是 almost-Kähler。脚本的
\[
\widehat s=u^{-3}(-6\Delta_g u+s_gu)
\]
以及
\[
\nu=-\frac1{2u}\left(q_t+\frac{4\sinh q}{a_f}\right),
\qquad
s^*=\widehat s+4\nu^2
\]
与 Step 28 的通常 star-scalar 约定一致。

螺栓附近
\[
u^2\sim ct,\qquad
T=\int u\,dt\sim t^{3/2},
\]
并有
\[
A_f,A_g\asymp T^{1/3},\qquad A_h\asymp T.
\]
因此 \(\widehat g\) 不是闭流形上的光滑 Riemann 度量。尽管相关积分有限，闭光滑 AKΓ 推导中的分部积分必须改写为去掉小管后的公式，并保留极限界面通量。直接把脚本输出代入闭 AKΓ 公式没有数学依据。

数值上，两个 profile 的所有 quadrature 节点均满足 \(s^*<0\)，最大值分别为

\[
-23.5046830,\qquad -23.4268853
\]
（原始 \(\operatorname{Ric}=-6g\) 单位）。这说明脚本没有检测到 \(s^*>0\) pocket；它不是连续变量的区间算术包围。由于距离零约为 \(23\)，数值图景很清楚，但仍应称作这两个离散 profile 的数值结果。

### \(s^*\) 积分的一致性

Step 28 的 Chern–Stokes 关系给出
\[
\int(\widehat s+2\nu^2)dV_{\widehat g}=-6X^2=-98304.
\]
令
\[
N=\int4\nu^2dV_{\widehat g}.
\]
则
\[
\int s^*dV_{\widehat g}
=-98304+\frac N2.
\]
Certified 数据给出
\[
-98304+\frac{0.04885886548959678}{2}
=-98303.9755705673,
\]
与 JSON 的 \(-98303.9755707679\) 相差约 \(2.0\times10^{-7}\)。Floating 数据相差约 \(1.1\times10^{-7}\)。这独立确认了脚本所用 \(s^*=\widehat s+4\nu^2\) 的约定。

### 六倍单位下的 hatted torsion

JSON 中 singular-hatted 部分仍使用原始尺度。若转到 \(\operatorname{Ric}=-\bar g\) 单位，则
\[
\bar{\widehat g}=6\widehat g,
\qquad
\int4\bar\nu^2dV_{\bar{\widehat g}}
=6\int4\nu^2dV_{\widehat g}.
\]
因此相应数值是

\[
0.2931531929375807
\quad\text{和}\quad
0.3906258716342408,
\]
而不是 \(0.0488589\) 和 \(0.0651043\)。后两个数适用于原始 \(\operatorname{Ric}=-6g\) 单位。点值则除以六：
\[
\max \bar s^*=-3.91744717,\qquad -3.90448088.
\]
符号不变，所以 pocket 结论不受此单位转换影响。

---

## 7. 这些数据对局域 \(O(k)\) 与 diffuse 构造所说明的内容

对固定胞元 profile，宿主区域上
\[
q=2,\qquad \nabla\psi=0,\qquad
W^+=A_{\psi,1/2},\qquad \operatorname{Ric}^{\circ}=0.
\]
因此所有列出的分子项都局域在互不相交的胞元内，复制 \(k\) 次后严格按 \(k\) 相加。Certified profile 每胞元的形式代价为

\[
\frac1{2\pi^2}\int
\bigl(|W^+-A_{\psi,1/2}|^2+(q-2)^2\bigr)
=0.0989894648,
\]
若计入一阶形式能量，则为
\[
0.5514614636.
\]
加入迹零 Ricci 后分别为
\[
4.0816701091,\qquad 4.5341421080.
\]
所以这个显式 harmonic-zero 构造确实提供了一个 \(O(k)\) 分子和宿主体积尺度上的 \(O(k/A)\) 示例。

若平均值使用最终粘接度量的实际体积，而 Step 28 的原始尺度每胞元体积增量记为 \(V_{\rm exc}\)，则
\[
\frac{V_{\rm final}}{2\pi^2}
=A+36kV_{\rm exc},
\]
相应平均值是
\[
\frac{4.0816701091\,k}{A+36kV_{\rm exc}}
\]
而不是严格等于 \(4.0816701091\,k/A\)。后者是相对于原宿主体积的表达，并在稀疏 \(k/A\) 情形给出相同首阶尺度。

这些计算没有给出所有度量或所有调和方向的线性下估计。它们也没有构造出 \(o(k)\) 的 diffuse 序列。它们建立的是：

1. 固定 harmonic-zero 胞元具有有限、非零、逐胞元可加的形式与 Ricci 作用量；
2. 该 profile 的 \(s^*\) 数值为负，没有呈现 aligned \(s^*>0\) pocket；
3. pullback Kähler 类把 \(\eta\) 固定为 \(1\)；
4. 将零点或旋转扩散到宿主尺度若要降低逐胞元代价，必须同时改变实际闭度量、其调和代表以及上述振幅、Weyl、一阶和 Ricci 项；单独在固定宿主上移动一个形式方向并不提供这样的构造；
5. 当前 evaluator 不排除另一族闭度量/调和形式把总作用量降到次线性，也没有提供这种族存在的数值证据。

最主要的文本修正是：区分 \(|\operatorname{Ric}^{\circ}|^2\) 与 \(|\operatorname{Ric}+\bar g|^2\)，并区分原始 \(\Omega\) 的类 \(K_X/6\) 与缩放后 \(\psi\) 的类 \(K_X\)。其余核心缩放、Kähler Weyl 目标、调和性、零周期和 \(\eta=1\) 均与脚本及几何公式一致。