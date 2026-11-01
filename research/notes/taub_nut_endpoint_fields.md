# Taub–NUT 度量上的三次扭率、线丛截面与拼接条件

Shuxing Yang, Junyao Wu, Rui Zhao, Hongsheng Chen, Yihao Yang  
Qiushi Engine Team, Zhejiang University · [作者与通讯信息](../../AUTHORS.md)

有限 Euler 密度端点证明使用负旋量的四次梯度与二阶导数控制。Taub–NUT 模型将这一要求的尺度含义具体化：某些二次场能量随核尺度平方衰减，四次和二阶能量却保持非零。下面的局部公式解释这种差别，并给出在闭流形上拼接单极子解所需的匹配条件。

## 1. 度量、旋量与三次扭率

取 Gibbons–Hawking 度量

```math
g_\ell=H(dx_1^2+dx_2^2+dx_3^2)+H^{-1}\eta^2,
\quad H=1+\ell/r,\quad
\eta=d\psi+\ell\cos\theta\,d\varphi,
```

其中 $`r=|x|`$、$`\ell>0`$，$`\psi`$ 的周期为 $`4\pi\ell`$。补入 nut 后度量光滑、完备且 Ricci-flat。取超 Kähler 形式自对偶的取向，则 $`W^+=0`$。下列积分采用未归一化体积；对只依赖底空间的函数，

```math
dV=H\,dx_1dx_2dx_3d\psi,\qquad
\Delta_g=H^{-1}\Delta_{\mathbb R^3},
```

这里 $`\Delta=\operatorname{div}\nabla`$。选择平行正旋量 $`e_1,e_2`$，使 $`e_2`$ 对应所选复结构 $`I_3`$ 的 $`(0,2)`$ 方向，$`f=x_1+ix_2`$ 为全纯函数。置

```math
\rho_*=\frac43,\qquad m_* =\frac{128}{81},\qquad a=\frac{\sqrt2}{3},
\qquad \Phi_\ell=\sqrt{\rho_*}\,e_1+a\bar f e_2.
```

由于 $`c(d\bar f)e_2=0`$，有 $`D\Phi_\ell=0`$。设

```math
t(\Phi)=\sum_i c(e^i)\Phi\otimes(\Phi\wedge\nabla_i\Phi).
```

在平行行列式平凡化中，$`\Phi_\ell\wedge\nabla_i\Phi_\ell=\sqrt{\rho_*}a\,\partial_i\bar f\,e_1\wedge e_2`$；又因
$`\langle d\bar f,d\bar f\rangle_{\mathbb C}=0`$，二次项消失，得到

```math
v:=t(\Phi_\ell)=\sqrt2\rho_*a\,d\bar f
=\sqrt{m_*/2}\,d\bar f,
\qquad D^-v=0,\qquad |v|^2=\frac{m_*r}{r+\ell}.
\tag{1}
```

这是 Ricci-flat 切模型中的 Dirac 旋量及其三次扭率；它尚未给出标量曲率 $`-4`$ 的完整单极子解。

## 2. 精确能量及尺度

在正交标架 $`e^i=H^{1/2}dx_i`$、$`e^4=H^{-1/2}\eta`$ 中，直接计算联络得

```math
|\operatorname{Hess}\bar f|^2=\frac{2\ell^2}{(r+\ell)^4},\qquad
|\nabla\operatorname{Hess}\bar f|^2
=\frac{12\ell^2r}{(r+\ell)^7}.
```

因此 $`m=|v|^2`$、$`q=|\nabla v|^2`$ 满足

```math
q=\frac{m_*\ell^2}{(r+\ell)^4}
=\frac12\Delta_g m,
\qquad
\int_{r\le R}q=8\pi^2m_*\ell^2\left(\frac{R}{R+\ell}\right)^2.
\tag{2}
```

径向积分进一步给出

| 积分 | 全 Taub–NUT 空间上的值 |
| --- | --- |
| $`\int\lvert\nabla^2\Phi_\ell\rvert^2`$ | $`(32\pi^2/9)\ell^2`$ |
| $`\int\lvert dm\rvert^2`$ | $`(16\pi^2/3)m_*^2\ell^2`$ |
| $`\int\lvert\nabla v\rvert^4`$ | $`(8\pi^2/15)m_*^2`$ |
| $`\int\lvert\nabla^2v\rvert^2`$ | $`(16\pi^2/5)m_*`$ |
| $`\int\lvert W^-\rvert^2`$ | $`8\pi^2`$ |

例如，利用纤维周期与球面积，

```math
\int|\nabla v|^4
=16\pi^2m_*^2\ell^5\int_0^\infty\frac{r}{(r+\ell)^7}\,dr
=\frac{8\pi^2}{15}m_*^2.
```

所以小核的正旋量 Hessian 能量趋于零，负旋量的四次梯度和二阶能量却不趋于零。若取截断半径 $`R_\ell\sim(3\ell/4)^{1/3}`$，则

```math
\operatorname{Vol}(r\le R_\ell)
=16\pi^2\ell\left(\frac{R_\ell^3}{3}+\frac{\ell R_\ell^2}{2}\right)
\sim4\pi^2\ell^2.
```

此时核的 $`\int q`$ 与块体积之比趋于 $`2m_*`$，正好等于闭端点序列中由
$`(\nabla^*\nabla-2)u\to0`$、$`|u|^2\to m_*`$ 推出的平均值
$`\fint|\nabla u|^2\to2m_*`$。另一方面，负 Weyl 平均能量为 $`2\ell^{-2}+o(\ell^{-2})`$。这说明上述平均值不排除这种集中尺度；它没有构造满足全部方程的闭序列。

## 3. 第五张量幂线丛截面的偶极表达式

对 (1) 的 $`v`$ 再施行三次运算并与原正旋量楔积，令

```math
\sigma_\ell=\Phi_\ell\wedge t(v),\qquad
C_\sigma=\frac{2^{11}\sqrt6}{3^7}.
```

在同一平行行列式平凡化中，Clifford 收缩给

```math
\boxed{\sigma_\ell=C_\sigma\frac{\ell\bar f}{(r+\ell)^3}.}
\tag{3}
```

它不恒等于零，但在 nut 与 $`f=0`$ 的两条轴向曲面上消失，并在外端按 $`\ell r^{-2}`$ 衰减。零集到达每个截断边界；不能将这个截面用作处处非零的边界相位。

式 (3) 的标量微分、模长微分和质量可以精确积分：

```math
\int|d\sigma_\ell|^2=\frac{32\pi^2}{35}C_\sigma^2,
\qquad
\int|d|\sigma_\ell||^2=\frac{8\pi^2}{21}C_\sigma^2,
\qquad
\int|\sigma_\ell|^2=\frac{8\pi^2}{3}C_\sigma^2\ell^2.
\tag{4}
```

证明可分离径向与角向变量。写
$`\sigma_\ell=C_\sigma\ell r(r+\ell)^{-3}\sin\theta e^{-i\varphi}`$，
底空间函数的 Dirichlet 积分中 $`H`$ 恰好消去，纤维积分只贡献 $`4\pi\ell`$。径向积分化为

```math
\int_0^\infty\left[\frac{t^2(1-2t)^2}{(1+t)^8}
+\frac{2t^2}{(1+t)^6}\right]dt=\frac3{35}.
```

对模长，角向系数 $`2`$ 换成 $`1/2`$，相应积分为 $`1/28`$，得到第二式；质量积分用
$`\int_0^\infty t^3(1+t)^{-5}dt=1/4`$。
式 (4) 的首项是平凡化中的普通微分，不包含行列式联络。第二式则给任意酉联络的 Kato 下界

```math
\int|\nabla^{5\mathcal A}\sigma_\ell|^2
\ge\frac{8\pi^2}{21}C_\sigma^2>0.
```

在 $`R_\ell\asymp\ell^{1/3}`$ 的块上，对每个固定 $`b>0`$ 有
$`\operatorname{Vol}\{|\sigma_\ell|>b\}/\operatorname{Vol}(B_{R_\ell})=O_b(\ell^{1/2})`$。
因而此模型的第五张量幂线丛截面依测度趋零，且每个核上模长导数的能量保持尺度不变；它不提供有限密度证明要求的正常数模长。

## 4. 原度量的曲率项与全局拼接条件

在标量曲率 $`-4`$ 的原度量上，负旋量丛 $`S^-\otimes L`$ 的行列式联络为 $`3\mathcal A`$。Weitzenböck 公式是

```math
(\mathcal L_{3\mathcal A}-2)t
=D_{3\mathcal A}^{-*}D_{3\mathcal A}^-t
-\left(1+\tfrac12c(F^-_{3\mathcal A})\right)t.
\tag{5}
```

在 Ricci-flat 且行列式曲率为零的切模型上得到的 $`-2v`$，还须与原尺度上的标量曲率及行列式曲率作用合并，才能计算局部解的残差。求解原尺度上的场方程要求同时满足式（5）及非线性曲率方程。

模型的反自对偶方向已有一个闭延拓。令

```math
\beta_h^- =\eta\wedge dh+H*_3dh.
```

由 $`d\eta=*_3dH`$ 可知 $`d\beta_h^-=0`$ 等价于
$`\operatorname{div}(H^2\nabla h)=0`$。取 $`h=x_3/H`$，则
$`\operatorname{div}(H^2\nabla(x_3/H))=H\Delta x_3-x_3\Delta H=0`$。
故 $`i(\tfrac23\omega_3+\tfrac13\beta^-_{x_3/H})`$ 给闭曲率模型，其正手性部分匹配极限常旋量。它尚不等于非恒定 $`\Phi_\ell`$ 的完整非线性曲率方程。

场的共同一阶数据又限制块之间的拼接。对向量值函数 $`u`$，固定端值和一阶导数，三次 Hermite 插值精确给出

```math
\inf\int_0^L|u''|^2
=\frac{12}{L^3}\left|u_1-u_0-\frac L2(p_0+p_1)\right|^2
+\frac1L|p_1-p_0|^2.
\tag{6}
```

Euler 方程为 $`u^{(4)}=0`$；任意同边界余项与该三次式的二阶导数正交，故它是全局最小值。在宽度 $`L`$、面体积量级 $`L^5`$、块体积量级 $`L^6`$ 的受控塌缩领口中，独立重置固定非零一阶旋量数据会产生量级 $`L^{-2}`$ 的平均 Hessian 平方积分。已有正旋量 Hessian 界因此要求相邻块在实际自旋及行列式转移下保留同一个宏观一阶场。式 (6) 不能将彼此独立的局部解自动拼成全局实际解。

此外，保持全局定向自由圆纤维结构的单 nut 块，向外传递一个单位的几何圆丛次数；仅将相对面周期识别会消去外边界通量，与该次数矛盾。这个几何次数、标量质量通量及实际行列式相对陈数是三个不同的量。若破坏圆纤维结构或加入补偿固定分量，须计算相应的场与度量过渡。

## 5. 对无密度端点的含义

上述公式解释一个有限密度估计无法控制的具体尺度：核的数目若为 $`N\asymp V/\ell^2`$，二次场能量仍与体积同阶，但四次梯度、负旋量 Hessian 和第五张量幂线丛截面的导数能量可比体积大 $`\ell^{-2}`$ 倍。

行列式陈数却不能任意集中在这些小核。实际端点的曲率拟合
$`F_{\mathcal A}=F_0+e`$、$`|F_0|\le C`$、$`\|e\|_{2,\mathrm{av}}\to0`$ 给

```math
\left|V^{-1}\int_U F_{\mathcal A}\wedge F_{\mathcal A}\right|
\le2C^2\frac{\operatorname{Vol}(U)}V+2\|e\|_{2,\mathrm{av}}^2\to0
```

对归一化体积趋零的 $`U`$ 成立。反自对偶 Weyl 能量的集中区域与第五张量幂线丛陈数的分布因而受到不同的限制。

这组模型与若干平均恒等式相容，但没有实现完整闭流形的单极子、相位、联络与边界转移。无密度端点问题要求由这些拼接条件导出额外的积分下界，或构造满足全部条件的闭流形序列。两者均须同时处理式（5）、单极子方程及全局联络数据。
