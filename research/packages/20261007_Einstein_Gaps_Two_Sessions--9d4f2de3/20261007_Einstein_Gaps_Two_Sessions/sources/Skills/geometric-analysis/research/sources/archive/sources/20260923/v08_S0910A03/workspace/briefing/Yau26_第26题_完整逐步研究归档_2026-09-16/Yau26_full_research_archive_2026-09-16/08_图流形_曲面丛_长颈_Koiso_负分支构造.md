# 08 图流形、曲面丛、长颈与 Koiso 路线

## 1. 两个“半个反例”

### surface-bundle
已有 maximum-norm near-negative-Einstein input family，但同一 smooth type 的 unrestricted Einstein nonexistence 未闭合。

### extended graph-manifold
有强 Einstein nonexistence 机制，但缺 \(\delta_-\to0\) operator-norm construction。

不能把不同流形的两半直接拼成反例。

## 2. long-collar inverse 警告

长 neck 说明：
> \(L^2\) spectral control 不自动给 maximum-norm inverse control。

近零 mode / Green kernel 可随 collar length 放大。这使很多“global inverse uniform bounded” shortcut 失效。

## 3. T²-invariant graph neck

项目建立 conformal-gauge / Frobenius modes / weighted shear reduced equations。一个高度对称 graph core 路线被阻碍，但后续明确：只排除该 ansatz，不排除一般 non-symmetric graph metric。

## 4. anisotropic quotient 构造

Step69 rank-two collapsed Koiso center \(q_N\)：
- periodic Yamabe residual \(<1.2\times10^{-16}\)；
- scalar error \(<4.5\times10^{-15}\)；
- family volume \(\sim N^{-2}\)。

peripheral cover lattice
\[
(N,1,1)
\]
经 cusp depth \(\log N\) 变成
\[
(1,N^{-1},N^{-1}),
\]
与 collapsed center 匹配。

**意义**：collapse 由 quotient/cusp depth 产生，无需 homothetic rescaling curvature。

## 5. Einstein Cauchy 数值演化

6/8/10/12 Fourier modes：
- constraints 在 \(t\lesssim0.4\) 越来越一致；
- \(H\) 初期变正后反转；
- \(t=0.4\) 约落在 \(-3.848,-0.873\)；
- \(t\gtrsim0.45\) stiff/resolution-dependent，不作为 geometric blow-up 证据。

不同 amplitude sweep 也有 reversal。

## 6. reversal 的结构解释

\[
P=\mathrm{Ric}_q^\sharp+3I=S'(0)
\]
与 complementary sectional curvature 存在关系；\(T^3\) 不能处处严格负 sectional curvature，因此简单 reflection center 必有 initially nonexpanding direction。

这排除一个自然的 symmetric core，不排除 inhomogeneous compensation。

## 7. 仍可能逃逸

Li–Liu 类 exact PE/AH-cusp Einstein metrics 表明 nonlinear tangential-normal compensation 可以发生。因此 graph route 被拆成：

1. 构造 global inhomogeneous expanding/compensating core；
2. 实现 anisotropic peripheral lattice；
3. finite transition + graph gluing 保持 \(C^0\) Ricci defect 小。

Step69 对第2项有实质推进；第1项最难。

## 8. charged Koiso / flux 后期

Steps94–99 继续发展：
- invariant charge；
- horizontal Noether/flux；
- redshift taper；
- relative \(K_X\)；
- cusp indicial roots；
- full matrix matching；
- Raychaudhuri/CGB Ricci floor；
- transition optimization。

多次出现 cancellation，迫使撤回 scalar-charge ceiling，说明最终 obstruction 必须是 full matrix/global matching 型。

## 9. 当前判别条件

graph route 要成功，必须在**同一 smooth manifold**同时证明：
\[
\delta_-(g_i)\to0
\]
且
\[
\text{没有任意符号 Einstein metric}.
\]

当前两者仍没有在同一 family 上闭合。
