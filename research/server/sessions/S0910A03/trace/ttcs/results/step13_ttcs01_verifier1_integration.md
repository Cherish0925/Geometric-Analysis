# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 13,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step13_ttcs01_sub3_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A03/trace/ttcs/results/step13_ttcs01_sub4_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the following claim about the Einstein defect evolution under normalized Ricci flow. For the flow d/dt g = -2(Ric + g), define E = Ric(g) + g. The claim is: d/dt E = Delta_L E - 2E, where Delta_L is the Lichnerowicz Laplacian. Furthermore, the squared norm satisfies (d/dt - Delta)|E|^2 = -2|nabla E|^2 + 4 R_{ikjl} E_{ij} E_{kl}. The derivation uses: (1) contracted Bianchi identity div(E) = (1/2) d(tr E) to cancel the Hessian-of-trace terms in the variation formula; (2) substitution R_{ik} = E_{ik} - g_{ik} to cancel tr(E^3) and |E|^2 terms in the |E|^2 evolution. Check each step for correctness. Then assess the consequence: under Ye Li's smoothing (which gives |Rm(g(t))| <= C/t for t in (0, T)), the Gronwall estimate for sup|E(t)|^2 gives a growth factor exp(int_0^{t_0} 4C/t dt) = exp(4C log(t_0/0)) = infinity, so the Einstein defect is NOT controlled pointwise through the flow. Is this analysis correct? Are there alternative estimates (using integral norms, parabolic regularity, or the -2E damping term) that could circumvent this gap?

## Integrated Scientific Memo

## 核验结论

采用约定
\[
\Delta=\nabla^k\nabla_k,\qquad
(\Delta_Lh)_{ij}
=\Delta h_{ij}+2R_{ikjl}h_{kl}
-R_i{}^kh_{kj}-R_j{}^kh_{ki},
\]
两个目标演化公式均正确。不过，脚本 Part 3/6 所说的“\(-2E\) 阻尼”不能用于 \(|E|^2\) 的最大值估计：该线性阻尼在精确标量演化中完全抵消。

### 1. \(E\) 的张量演化

对 \(v=\partial_tg\)，
\[
2\partial_tR_{ij}
=-(\Delta_Lv)_{ij}
-\nabla_i\nabla_j\tr v
+\nabla_i(\div v)_j+\nabla_j(\div v)_i.
\]
这里 \(v=-2E\)，且
\[
\tr E=R+n,\qquad
\div E=\frac12\,dR=\frac12\,d(\tr E).
\]
于是
\[
\tr v=-2\tr E,\qquad \div v=-d(\tr E).
\]
因此 Hessian 项分别为
\[
2\nabla_i\nabla_j\tr E,\qquad
-2\nabla_i\nabla_j\tr E,
\]
恰好抵消，得到
\[
\partial_t\Ric=\Delta_LE.
\]
再加上 \(\partial_tg=-2E\)，即
\[
\boxed{\partial_tE=\Delta_LE-2E.}
\]

所以 contracted Bianchi 的使用及 Hessian-of-trace 抵消均正确。

### 2. \(|E|^2\) 的演化

因为
\[
\partial_tg^{ij}=2E^{ij},
\]
两个逆度量的变化贡献
\[
4\tr(E^3).
\]
同时
\[
\begin{aligned}
2\langle\Delta_LE,E\rangle
={}&\Delta|E|^2-2|\nabla E|^2
+4R_{ikjl}E_{ij}E_{kl}\\
&-4R_{ik}E_{ij}E_{kj}.
\end{aligned}
\]
由 \(\Ric=E-g\)，
\[
R_{ik}E_{ij}E_{kj}=\tr(E^3)-|E|^2.
\]
所有纯代数项为
\[
[-4\tr(E^3)+4|E|^2]
+4\tr(E^3)-4|E|^2=0,
\]
其中最后一项来自张量方程中的 \(-2E\)。故
\[
\boxed{
(\partial_t-\Delta)|E|^2
=-2|\nabla E|^2
+4R_{ikjl}E_{ij}E_{kl}.
}
\]
因此脚本关于 \(\tr(E^3)\) 与 \(|E|^2\) 的抵消是正确的。

也可以将张量方程重写为
\[
\partial_tE
=\Delta E+2R_{ikjl}E_{kl}-2(E^2)_{ij}.
\]
这再次表明显式的线性 \(-2E\) 已与 \(\Delta_L\) 中由背景 \(\Ric=E-g\) 产生的线性项抵消；剩余的 \(-2E^2\) 并非定号线性阻尼。

## \(C/t\) 最大值估计确实失效

令
\[
F(t)=\sup_M|E(t)|^2.
\]
在闭流形上，最大值原理给出
\[
D^+F(t)\le 4\|\Rm(t)\|_\infty F(t).
\]
若只有
\[
\|\Rm(t)\|_\infty\le \frac Ct,
\]
则对 \(0<s<t_0\),
\[
F(t_0)\le F(s)\left(\frac{t_0}{s}\right)^{4C}.
\]
当 \(s\downarrow0\) 时，该上界发散。因此：

* \(C/t\) 点态曲率估计本身不能将 \(t=0\) 的一致点态小缺陷传播到固定正时间；
* 这只证明该最大值/Gronwall 论证失效，并不证明实际的 \(E(t_0)\) 必然变大；
* 对每个固定的光滑初始度量，实际曲率在 \(t=0\) 有限，故其解当然仍有有限的 \(E(t_0)\)；缺失的是对初始全曲率可能发散的一族度量的一致估计；
* 若 \(E(0)=0\)，则唯一性仍给出 \(E\equiv0\)。

脚本中的辅助 ODE
\[
f'=(-2+4C/t)f
\]
不由精确的 \(|E|^2\) 方程推出。若把 \(f\) 理解为 \(|E|^2\)，显式 \(-2\) 应删除；即使人为保留一个常数阻尼，有限因子 \(e^{-a(t_0-s)}\) 也无法消除 \((t_0/s)^{4C}\) 的发散。

同样，“曲率有界便使 Einstein 固定点稳定”也过强。有限时间连续依赖可由曲率界得到，但衰减需要背景线性化算子的有利谱性质，而不是仅靠公式中的 \(-2E\)。

## 可行替代：临界积分能量，而非点态 Gronwall

全局 \(L^2\) 恒等式还要包括
\[
\partial_td\mu=-\tr E\,d\mu:
\]
\[
\boxed{
\frac d{dt}\int_M|E|^2\,d\mu
=-2\int_M|\nabla E|^2\,d\mu
+4\int_M\Rm(E,E)\,d\mu
-\int_M(\tr E)|E|^2\,d\mu.
}
\]
此外
\[
\boxed{
(\partial_t-\Delta)\tr E=2|E|^2-2\tr E,
}
\]
可用最大值原理控制 \(\tr E\) 的负部。真正困难的项是
\[
\int |\Rm|\,|E|^2.
\]

在四维局部球上，
\[
\int |\Rm|\,|\phi E|^2
\le \|\Rm\|_{L^2}\|\phi E\|_{L^4}^2.
\]
若具有一致的相对 Sobolev 不等式，并且归一化临界曲率能量
\[
\varepsilon_r
=\frac{r^4}{\Vol(B_r)}
\int_{B_r}|\Rm|^2
\]
足够小，则可得示意估计
\[
\int |\Rm|\,|\phi E|^2
\lesssim
\varepsilon_r^{1/2}\int|\nabla(\phi E)|^2
+\varepsilon_r^{1/2}r^{-2}\int|\phi E|^2.
\]
第一项可被 \(-2\int|\nabla E|^2\) 吸收，从而在长度 \(O(r^2)\) 的时间区间内得到尺度一致的局部 \(L^2\) 传播。之后在 \(t\ge\theta r^2\) 时，
\[
|\Rm(t)|\le C_\theta r^{-2},
\]
再结合局部均值不等式或 Moser 迭代，有希望把时空 \(L^2\) 控制升级为内部点态控制。

但根据现有材料，这条路线尚缺关键输入，不能直接宣称闭合：

1. 初始归一化小 \(L^2\) 曲率能量在早期 Ricci 流中的持续性或相应时空估计；
2. 随时间一致的局部 Sobolev、倍增和 cutoff 控制；
3. 缓冲球边界误差的控制；
4. 若现有 good-point 信息只有“有界”而非低于吸收阈值的“小能量”，还需额外的小能量分解或重整化机制。

仅有 Ye Li 输出的 \(|\Rm|\le C/t\) 并不提供这些条件。普通抛物正则性从任意固定 \(s>0\) 开始有效，却仍需先控制 \(E(s)\)，所以不能单独跨越 \(t=0\) 的临界层。

更一般地，以下任一增强条件都可避开该发散：
\[
\int_0^{t_0}\|\Rm(t)\|_\infty dt<\infty,
\]
或次临界混合范数
\[
\Rm\in L_t^qL_x^p,\qquad
\frac n{2p}+\frac1q<1,
\]
以及临界端点的小 Kato/热核控制，或对 \(\Rm(E,E)\) 正部的可积上界。

**最终判断：**两个演化恒等式和 \(C/t\) 导致点态 Gronwall 上界失效的结论正确；“因此实际 Einstein 缺陷必然不受控”应改为“该点态方法不能提供一致控制”。脚本所称普适 \(-2E\) 阻尼在 \(|E|^2\) 方程中不存在。四维临界 \(L^2\)+Sobolev/Moser 是最具体的绕行方案，但尚需证明 smoothing 期间的归一化曲率能量与局部几何不等式持续成立。