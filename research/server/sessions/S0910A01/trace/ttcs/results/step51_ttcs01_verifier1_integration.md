# TTCS Task-Scoped Scientific Integration

```json
{
  "step_id": 51,
  "task_field": "verifier",
  "task_index": 1,
  "type": "Verifier",
  "branches": [
    {
      "branch": 1,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step51_ttcs01_sub1_verifier.md"
    },
    {
      "branch": 2,
      "status": "complete",
      "result_path": "Sessions/S0910A01/trace/ttcs/results/step51_ttcs01_sub2_verifier.md"
    }
  ]
}
```

## Exact Task

Verify the complete mathematical chain in the proof note for Einstein existence on the BCGP Z₄² K²=2 product-quotient resolution. The chain is: (1) T_X⁰ ≅ (π_*T_Y)^G by reflexive extension, where π: Y=C₁×C₂ → X=Y/G and X has six isolated A₁ singularities. The argument is: both sheaves are reflexive, they agree on the étale locus U = X\Sing(X) (codim-2 complement), and reflexive extension is unique on a normal surface. (2) H²(X, T_X⁰) = H²(Y, T_Y)^G via Reynolds splitting + Leray (finite pushforward). (3) H²(Y, T_Y)^G = 0 via equivariant Serre duality giving H⁰(Y, Ω¹_Y ⊗ K_Y)^G, then Künneth decomposition, then character computation (already verified by script: both invariant dimensions are zero). (4) Lee-Park Proposition 2.4(2): H²(T_X⁰)=0 implies global QG smoothing of all 6 A₁ nodes. (5) Ampleness persistence + Aubin-Yau on smooth fibers. (6) Milnor fiber bridge: S ≅_diff X_t. Check each step for hidden hypotheses, incorrect categorical claims, missing conditions, or logical gaps. In particular: (a) Is T_X⁰ = Hom(Ω¹_X, O_X) indeed reflexive on a normal surface with A₁ singularities? (b) Is (π_*T_Y)^G reflexive? (c) Does the Reynolds splitting work at the sheaf level (not just cohomology)? (d) Is the Serre duality trace map G-equivariant? (e) Does Lee-Park's proposition apply to RDP (du Val) singularities specifically, or only to T-singularities more generally? (f) Is the Milnor fiber for A₁ really diffeomorphic to the resolution neighborhood?

## Integrated Scientific Memo

# 核验结论

在修正若干实质性论证后，这条证明链可以闭合：

\[
T_X^0\cong (\pi_*T_Y)^G,\qquad
H^2(X,T_X^0)\cong H^2(Y,T_Y)^G=0,
\]

从而六个 \(A_1\) 点可同时作全局 \(\mathbb Q\)-Gorenstein 平滑；附近光滑纤维的典范束仍 ample，故由 Aubin–Yau 承载负 Kähler–Einstein 度量；再由 ADE simultaneous resolution 与 Ehresmann 定理，光滑纤维与最小解消 \(S\) 微分同胚。因此 \(S\) 承载满足

\[
\operatorname{Ric}_h=-h
\]

的光滑 Einstein 度量。

原证明稿的结论是可修复的，但当前文字中至少有四个必须改正的缺口：

1. 两个 reflexive 性的原论证使用了错误的一般命题；
2. 非超椭圆性的固定点论证不完整；
3. \(A_1\) 的局部平滑方程写错；
4. 局部填充微分同胚不足以自动保证全局粘合；应改用 simultaneous resolution。

另有一处理由需要替换：不能仅从“最小一般型且 \(K^2>0\)”推出 \(K_X\) ample；本例应使用有限拉回 \(\pi^*K_X=K_Y\)。

---

## 1. Reflexive extension

令

\[
T_X^0:=\mathcal Hom_{\mathcal O_X}(\Omega_X^1,\mathcal O_X).
\]

### 1.1 \(T_X^0\) 是 reflexive

结论正确，但原稿所说

> 正规曲面上，无挠且在有限点外局部自由就 reflexive

是错误的。例如光滑曲面上一点 \(p\) 的理想层 \(\mathcal I_p\) 满足这些条件，却有

\[
\mathcal I_p^{\vee\vee}\cong\mathcal O_X\neq\mathcal I_p.
\]

正确理由是：正规 Noetherian 空间上 coherent sheaf 的对偶是 reflexive。这里 \(T_X^0=(\Omega_X^1)^\vee\)，故为 reflexive。

在二维局部环上也可直接证明。若 \(A=\mathcal O_{X,x}\)，取有限表示

\[
A^m\longrightarrow A^r\longrightarrow\Omega_A^1\longrightarrow0.
\]

对偶得到

\[
0\longrightarrow\operatorname{Hom}_A(\Omega_A^1,A)
\longrightarrow A^r\longrightarrow A^m.
\]

二维正规局部环满足 \(S_2\)，故 \(\operatorname{depth}A=2\)；结合深度引理可得该对偶模深度为 \(2\)，并且在余维一处为自由模。因此它无挠且满足 \(S_2\)，即 reflexive。

### 1.2 \((\pi_*T_Y)^G\) 是 reflexive

原稿同样不能仅凭“无挠且在有限点外局部自由”得出结论。应使用 maximal Cohen–Macaulay 性。

在 \(x\in X\) 处令 \(A=\mathcal O_{X,x}\)，而 \(B\) 为 \(\pi^{-1}(x)\) 上方局部环组成的有限半局部 \(A\)-代数。每个 \(B_y\) 都是二维光滑局部环，故 Cohen–Macaulay。由于 \(\pi\) 有限，\(A\) 的参数系在每个 \(B_y\) 上仍为参数系，并在局部自由模 \(T_{Y,y}\) 上构成正则序列。因此

\[
(\pi_*T_Y)_x
\]

作为 \(A\)-模深度为 \(2\)，即 maximal Cohen–Macaulay。

群作用是 \(\mathcal O_X\)-线性的，因为 \(\pi\circ g=\pi\)。特征零下 Reynolds 算子

\[
R=\frac1{|G|}\sum_{g\in G}g
\]

是 \(\mathcal O_X\)-线性幂等元，给出

\[
\pi_*T_Y=(\pi_*T_Y)^G\oplus\ker R.
\]

直和因子仍具有深度 \(2\)。因此 \((\pi_*T_Y)^G\) 无挠并满足 \(S_2\)，故在正规曲面 \(X\) 上 reflexive。

### 1.3 Étale locus 与余维二延拓

这里有一个必须显式记录的假设：对角 \(G\)-作用在余维一处自由。由给定 branch triples 生成 \(G\)，各曲线作用忠实；非平凡有限阶曲线自同构的固定集是离散的，故对角作用不存在固定曲线。结合 BCGP 的固定点分类——非自由轨道恰好产生六个 \(A_1\) 点——得到

\[
\pi^{-1}(U)\to U,\qquad U=X\setminus\operatorname{Sing}(X),
\]

是有限 étale \(G\)-覆盖。

Étale descent 给出

\[
T_U\cong
\left(\pi_*T_{\pi^{-1}(U)}\right)^G.
\]

两端在 \(X\) 上的延拓均为 reflexive，而 \(X\setminus U\) 余维为 \(2\)，故唯一 reflexive extension 给出

\[
\boxed{T_X^0\cong(\pi_*T_Y)^G}.
\]

所以问题 (a)、(b) 的答案均为“是”，但原稿证明必须替换。

---

## 2. Reynolds splitting 与 Leray

这一部分正确。

令 \(F=\pi_*T_Y\)。Reynolds 算子在 sheaf 层面就是 \(\mathcal O_X\)-线性幂等态射，因此

\[
F=F^G\oplus\ker R.
\]

取上同调后，

\[
H^i(X,F)=H^i(X,F^G)\oplus H^i(X,\ker R),
\]

而 \(H^i(R)\) 正是 \(H^i(X,F)\) 上的群平均投影，所以

\[
H^i(X,F^G)\cong H^i(X,F)^G.
\]

由于有限态射是 affine，

\[
R^j\pi_*T_Y=0\qquad(j>0),
\]

故 Leray 给出自然且 \(G\)-等变的同构

\[
H^i(X,\pi_*T_Y)\cong H^i(Y,T_Y).
\]

于是

\[
\boxed{
H^2(X,T_X^0)\cong H^2(Y,T_Y)^G}.
\]

问题 (c) 的答案是肯定的：Reynolds splitting 确实发生在 sheaf 层面，而非仅在上同调层面。

---

## 3. Equivariant Serre duality 与 character vanishing

### 3.1 Trace map 的 \(G\)-不变性

Serre duality 给出

\[
H^2(Y,T_Y)^\vee
\cong H^0(Y,\Omega_Y^1\otimes K_Y).
\]

其配对通过

\[
H^2(Y,K_Y)\xrightarrow{\operatorname{Tr}}\mathbb C.
\]

对任意 \(g\in G\)，

\[
\operatorname{Tr}(g^*\alpha)=\operatorname{Tr}(\alpha).
\]

等价地，由

\[
H^2(Y,K_Y)^\vee\cong H^0(Y,\mathcal O_Y)=\mathbb C
\]

且 \(G\) 在常数函数上作用平凡，可知 \(G\) 在 \(H^2(Y,K_Y)\) 上也作用平凡。因此 Serre pairing 是 \(G\)-不变的。特征零下取不变部分是 exact，故

\[
\bigl(H^2(Y,T_Y)^G\bigr)^\vee
\cong H^0(Y,\Omega_Y^1\otimes K_Y)^G.
\]

问题 (d) 的答案是肯定的。

### 3.2 Künneth 分解

有 \(G\)-等变分解

\[
\Omega_Y^1\otimes K_Y
=
(2K_{C_1}\boxtimes K_{C_2})
\oplus
(K_{C_1}\boxtimes2K_{C_2}),
\]

因此

\[
H^0(Y,\Omega_Y^1\otimes K_Y)
=
H^0(2K_{C_1})\otimes H^0(K_{C_2})
\oplus
H^0(K_{C_1})\otimes H^0(2K_{C_2}).
\]

该部分正确。

### 3.3 非超椭圆性：原证明不完整

脚本只证明了 \(G\) 内每个二阶元最多有四个固定点，因此 \(G\) 中没有元素能成为具有八个固定点的 genus-\(3\) hyperelliptic involution。但这没有排除 hyperelliptic involution \(\iota\notin G\)。

补充证明如下。若 \(C_i\) 超椭圆，则其 hyperelliptic involution \(\iota\) 在 \(\operatorname{Aut}(C_i)\) 中是中心元。若 \(\iota\in G\)，则前述固定点数已经矛盾。因此 \(\iota\notin G\)。于是 \(G\) 在商

\[
C_i/\langle\iota\rangle\cong\mathbb P^1
\]

上忠实作用，从而给出嵌入

\[
\mathbb Z_4^2\hookrightarrow\operatorname{PGL}_2(\mathbb C).
\]

但 \(\operatorname{PGL}_2(\mathbb C)\) 的有限 abelian 子群只能是 cyclic 或 \((\mathbb Z_2)^2\)，不可能包含 \(\mathbb Z_4^2\)。矛盾。因此两条 \(C_i\) 均非超椭圆。

所以 canonical multiplication 是 \(G\)-等变同构

\[
\operatorname{Sym}^2 H^0(K_{C_i})
\xrightarrow{\sim}
H^0(2K_{C_i}).
\]

给定脚本验证的 character decompositions 随即成立，并且两个 Künneth summand 的 invariant dimensions 都是零。由此

\[
H^0(Y,\Omega_Y^1\otimes K_Y)^G=0
\]

以及

\[
\boxed{H^2(X,T_X^0)=0}.
\]

若 Chevalley–Weil 使用相反 character convention，所有 character 同时取逆，不影响 invariant dimension 为零的结论。

---

## 4. Lee–Park globalization

问题 (e) 的答案是肯定的：\(A_1\) 是 rational double point，也是 index-one class \(T\) singularity，包含在 Lee–Park 所用的 \(\mathbb Q\)-Gorenstein smoothing 理论中。

但原稿的局部方程

\[
\{uv=t\}\subset\mathbb C^3/(\pm1)
\]

不正确。标准 \(A_1\) 模型及其平滑为

\[
A_1=\{xy-z^2=0\}\subset\mathbb C^3,
\qquad
\{xy-z^2=\tau\},
\]

等价地写为

\[
u^2+v^2+w^2=\tau.
\]

每个节点有一个局部平滑参数，所以

\[
H^0(\mathcal T_X^1)\cong
\bigoplus_{i=1}^6\mathbb C_{p_i}
\cong\mathbb C^6.
\]

这里不能只说“一阶 local-to-global map 满射，所以有实际族”。必须使用 Lee–Park Proposition 2.4(2) 的完整变形函子结论：在

\[
H^2(T_X^0)=0
\]

时局部 \(\mathbb Q\)-Gorenstein deformation 的整体 obstruction 消失，所选局部 deformation 可以提升并积分为实际全局 \(\mathbb Q\)-Gorenstein family。

选择六个坐标均非零的局部方向。得到的一参数族可写为

\[
\tau_i(t)=a_i t+O(t^2),\qquad a_i\neq0.
\]

因此对充分小的 \(t\neq0\)，所有六个节点同时被平滑，\(X_t\) 光滑。

---

## 5. Ampleness persistence 与 Aubin–Yau

原稿中“minimal surface of general type 且 \(K^2>0\)，故 \(K\) ample”的一般推理不成立，因为最小一般型曲面可能含有 \(K\cdot C=0\) 的 \((-2)\)-曲线。

本模型有直接证明。由于 \(\pi\) 在余维一处 étale，

\[
\pi^*K_X=K_Y.
\]

而

\[
K_Y=p_1^*K_{C_1}\otimes p_2^*K_{C_2}
\]

在 \(g(C_1)=g(C_2)=3\) 时是 ample。有限满射下，线束 ample 当且仅当其有限拉回 ample，因此 \(K_X\) ample。

对 \(\mathbb Q\)-Gorenstein family

\[
f:\mathcal X\to\Delta,
\]

取公共指数 \(m>0\)，使

\[
L=\omega_{\mathcal X/\Delta}^{[m]}
\]

为 line bundle，并与纤维限制相容。中央纤维上

\[
L|_X=mK_X
\]

ample。Proper family 中“line bundle 在纤维上 ample”是开条件；缩小底空间后，

\[
L|_{X_t}=mK_{X_t}
\]

对小 \(t\) 均 ample。因此光滑纤维 \(X_t\) 的 \(K_{X_t}\) ample。

Aubin–Yau 给出唯一负 Kähler–Einstein 度量

\[
\operatorname{Ric}(\omega_t)=-\omega_t.
\]

---

## 6. Milnor fiber bridge

问题 (f) 的局部答案是肯定的，但原稿的直接粘合论证不够严格。

对于 \(A_1\)：

* affine smoothing \(u^2+v^2+w^2=1\) 微分同胚于 \(T^*S^2\)；
* 紧 Milnor fiber 是 cotangent disk bundle \(D(T^*S^2)\)；
* 其零截面自交数为 \(-2\)，故 Euler number 为 \(-2\)；
* 最小解消的 exceptional curve 邻域是
  \[
  D(\mathcal O_{\mathbb P^1}(-2)),
  \]
  同样是 Euler number \(-2\) 的 oriented disk bundle；
* 两者边界均为
  \[
  L(2,1)=\mathbb{RP}^3.
  \]

因此两个局部填充作为 manifolds-with-boundary 确实微分同胚。然而，仅凭局部填充同胚与共同外部补集，仍需核对边界 gluing map 的标记相容性。

最稳妥的全局闭合方式是 ADE simultaneous resolution。对一参数 \(A_1\) 平滑作有限 base change，局部可取

\[
\tau=s^2.
\]

随后存在 simultaneous resolution

\[
\widetilde{\mathcal X}\longrightarrow\Delta_s
\]

使中央纤维是六节点的最小解消 \(S\)，而 \(s\neq0\) 的纤维仍是原光滑纤维 \(X_{\tau(s)}\)。六个节点彼此分离，可用一个共同有限 base change 同时处理。该族是 proper smooth submersion，故 Ehresmann 定理给出

\[
\boxed{S\cong_{\mathrm{diff}}X_t}.
\]

这也说明该桥梁依赖于 du Val/ADE 性质。对一般 \(T\)-singularity，Milnor fiber 通常不同于 resolution neighborhood，产生的是 rational blowdown，而非这里的微分同胚。

---

# 最终核验结论

修订后的完整链为

\[
T_X^0\cong(\pi_*T_Y)^G,
\]

\[
H^2(X,T_X^0)
\cong H^2(Y,T_Y)^G
\cong
\left(H^0(Y,\Omega_Y^1\otimes K_Y)^G\right)^\vee
=0.
\]

Lee–Park 的 \(\mathbb Q\)-Gorenstein globalization 定理随后给出同时平滑六个 \(A_1\) 点的实际族。由

\[
\pi^*K_X=K_Y
\]

知 \(K_X\) ample，且 ampleness 在该 \(\mathbb Q\)-Gorenstein proper family 中对附近纤维保持。故 \(X_t\) 承载负 Kähler–Einstein 度量。ADE simultaneous resolution 加 Ehresmann 给出

\[
S\cong_{\mathrm{diff}}X_t,
\]

因此该度量可拉回为 \(S\) 上满足

\[
\operatorname{Ric}_h=-h
\]

的光滑 Einstein 度量。

所以结论成立，但 proof note 应明确替换以下内容：

- 删除“无挠且在有限点外局部自由 \(\Rightarrow\) reflexive”；
- 补充 diagonal action 在余维一处自由及六个 \(A_1\) 的固定点输入；
- 补全排除 \(\iota\notin G\) 的 hyperelliptic 情形；
- 将 \(A_1\) 平滑方程改为 \(xy-z^2=\tau\)；
- 使用 Lee–Park 的完整 obstruction/globalization 结论，而非仅切空间满射；
- 用 \(\pi^*K_X=K_Y\) 证明 ampleness；
- 用 simultaneous resolution 与 Ehresmann 取代未经标记核对的局部粘合。