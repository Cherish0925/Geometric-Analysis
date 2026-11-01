# TTCS Independent Branch Record

```json
{
  "step_id": 51,
  "type": "Verifier",
  "task_field": "verifier",
  "task_index": 1,
  "status": "complete",
  "context_files": [
    "Sessions/S0910A01/workspace/notes/step51_reflexive_bridge_einstein_existence_proof.md",
    "Sessions/S0910A01/workspace/scripts/step51_reflexive_bridge_verify.py",
    "Sessions/S0910A01/workspace/notes/step50_global_smoothing_evidence_campedelli_front.md"
  ]
}
```

## Task

Verify the complete mathematical chain in the proof note for Einstein existence on the BCGP Z₄² K²=2 product-quotient resolution. The chain is: (1) T_X⁰ ≅ (π_*T_Y)^G by reflexive extension, where π: Y=C₁×C₂ → X=Y/G and X has six isolated A₁ singularities. The argument is: both sheaves are reflexive, they agree on the étale locus U = X\Sing(X) (codim-2 complement), and reflexive extension is unique on a normal surface. (2) H²(X, T_X⁰) = H²(Y, T_Y)^G via Reynolds splitting + Leray (finite pushforward). (3) H²(Y, T_Y)^G = 0 via equivariant Serre duality giving H⁰(Y, Ω¹_Y ⊗ K_Y)^G, then Künneth decomposition, then character computation (already verified by script: both invariant dimensions are zero). (4) Lee-Park Proposition 2.4(2): H²(T_X⁰)=0 implies global QG smoothing of all 6 A₁ nodes. (5) Ampleness persistence + Aubin-Yau on smooth fibers. (6) Milnor fiber bridge: S ≅_diff X_t. Check each step for hidden hypotheses, incorrect categorical claims, missing conditions, or logical gaps. In particular: (a) Is T_X⁰ = Hom(Ω¹_X, O_X) indeed reflexive on a normal surface with A₁ singularities? (b) Is (π_*T_Y)^G reflexive? (c) Does the Reynolds splitting work at the sheaf level (not just cohomology)? (d) Is the Serre duality trace map G-equivariant? (e) Does Lee-Park's proposition apply to RDP (du Val) singularities specifically, or only to T-singularities more generally? (f) Is the Milnor fiber for A₁ really diffeomorphic to the resolution neighborhood?

## Output

# 数学核验备忘录

## 总结

最终结论可以成立：BCGP 的 \(G=\mathbb Z_4^2,\ K^2=2\) 六节点商曲面的最小解消 \(S\) 与一个 \(K\) ample 的光滑纤维微分同胚，因此 \(S\) 承载满足 \(\operatorname{Ric}_h=-h\) 的光滑 Einstein 度量。

不过，当前证明文字有五处需要实质修正：

1. “无挠且在有限点外局部自由，所以 reflexive”是错误的一般命题；
2. 脚本中关于非超椭圆性的固定点论证少了一种可能；
3. \(A_1\) 的局部平滑方程写错；
4. 一阶局部到整体满射与实际平滑族之间需要使用 Lee–Park 的完整变形定理，而不能只引用切空间满射；
5. “两个局部填充微分同胚，所以整体微分同胚”还需要粘合标记相容性；ADE simultaneous resolution 提供了严格闭合。

以下逐段给出可直接替代的证明材料。

---

## 1. Reflexive extension bridge

### 1.1 \(T_X^0\) 确实是 reflexive

令
\[
T_X^0=\mathcal Hom_{\mathcal O_X}(\Omega_X^1,\mathcal O_X).
\]
在正规 Noetherian 空间上，任意 coherent sheaf 的对偶都是 reflexive。对二维局部环 \(A=\mathcal O_{X,x}\)，可直接证明如下。取有限表示
\[
A^m\longrightarrow A^r\longrightarrow \Omega_A^1\longrightarrow0.
\]
对偶后得到
\[
0\longrightarrow \operatorname{Hom}_A(\Omega_A^1,A)
 \longrightarrow A^r\longrightarrow A^m.
\]
右侧映像是自由模的子模，因而无挠，在二维正规局部环上深度至少为 \(1\)。正规二维局部环满足 \(\operatorname{depth}A=2\)，由深度引理，
\[
\operatorname{depth}_A\operatorname{Hom}_A(\Omega_A^1,A)=2.
\]
在余维一处，\(A\) 是 DVR，对偶模无挠，因而自由。因此 \(T_X^0\) 满足 \(S_2\) 且无挠，也就是 reflexive。

当前稿件中的理由不能使用：光滑曲面上一点 \(p\) 的理想层 \(\mathcal I_p\) 无挠、在 \(p\) 外局部自由，但
\[
\mathcal I_p^{\vee\vee}\cong\mathcal O_X\ne\mathcal I_p.
\]

### 1.2 \((\pi_*T_Y)^G\) 也确实是 reflexive

结论正确，但也不能仅由“无挠并在有限点外局部自由”推出。

在闭点 \(x\in X\) 处，记 \(A=\mathcal O_{X,x}\)。有限映射上方的局部环组成有限半局部 \(A\)-代数 \(B\)，每个 \(B_y\) 都是二维正规光滑局部环。若 \(a,b\) 是 \(A\) 的参数系，则因 \(B\) 在 \(A\) 上有限，\(a,b\) 在每个 \(B_y\) 中也是参数系。每个 \(B_y\) 都是 Cohen–Macaulay，故 \(a,b\) 在 \(T_{Y,y}\) 上构成正则序列。因此
\[
(\pi_*T_Y)_x
\]
作为 \(A\)-模深度为 \(2\)，即为 maximal Cohen–Macaulay 模。

群作用在 \(\pi_*T_Y\) 上是 \(\mathcal O_X\)-线性的，因为每个 \(g\in G\) 都位于 \(X\) 上方。Reynolds 幂等元
\[
R=\frac1{|G|}\sum_{g\in G}g
\]
给出
\[
\pi_*T_Y=(\pi_*T_Y)^G\oplus\ker R.
\]
直和因子的深度仍为 \(2\)，所以 \((\pi_*T_Y)^G\) 是无挠 \(S_2\) 模，因而 reflexive。

### 1.3 余维二延拓

由于两个 branch triple 都生成 \(G\)，两条曲线上的 \(G\)-作用忠实。非平凡有限阶曲线自同构在固定点处的导数不可能为 \(1\)，所以对角作用没有余维一固定集。由题设，全部非自由轨道正好给出六个 \(A_1\) 点。因此
\[
\pi^{-1}(U)\longrightarrow U,\qquad U=X\setminus\operatorname{Sing}(X),
\]
是有限 étale \(G\)-覆盖。

Étale descent 给出
\[
T_U\cong\bigl(\pi_*T_{\pi^{-1}(U)}\bigr)^G.
\]
两端在 \(X\) 上都是 reflexive，而 \(X\setminus U\) 余维为二，因此唯一延拓给出
\[
\boxed{\,T_X^0\cong(\pi_*T_Y)^G\,}.
\]

所以问题 (a)、(b) 的答案都是肯定的，但证明必须使用对偶模的 \(S_2\) 性质和 maximal Cohen–Macaulay 性质。

---

## 2. Reynolds splitting 与有限推前

这一段成立。

令 \(F=\pi_*T_Y\)。Reynolds 算子是 coherent \(\mathcal O_X\)-模上的幂等态射，且
\[
F=F^G\oplus\ker R.
\]
取上同调后仍为直和。\(H^i(R)\) 正是 \(H^i(X,F)\) 上的群平均算子，因此
\[
H^i(X,F^G)=H^i(X,F)^G.
\]

由于有限映射是 affine，
\[
R^j\pi_*T_Y=0\qquad(j>0),
\]
故 Leray 给出自然且 \(G\)-等变的同构
\[
H^i(X,\pi_*T_Y)\cong H^i(Y,T_Y).
\]
结合第一步，
\[
\boxed{\,H^2(X,T_X^0)\cong H^2(Y,T_Y)^G\,}.
\]

问题 (c) 的答案是肯定的；这里的 splitting 确实发生在 sheaf 层面。

---

## 3. Equivariant Serre duality 与 character 计算

### 3.1 Trace 的 \(G\)-等变性

Serre duality 给出
\[
H^2(Y,T_Y)^\vee
 \cong H^0(Y,T_Y^\vee\otimes K_Y)
 =H^0(Y,\Omega_Y^1\otimes K_Y).
\]
对任意 \(g\in G\)，Serre trace 满足
\[
\operatorname{Tr}_Y(g^*\alpha)=\operatorname{Tr}_Y(\alpha).
\]
也可以从
\[
H^2(Y,K_Y)^\vee\cong H^0(Y,\mathcal O_Y)=\mathbb C
\]
看出：\(G\) 在常数函数上作用平凡，因此也在 \(H^2(K_Y)\) 上作用平凡。故 Serre pairing 是 \(G\)-不变的。特征零下取不变部分是 exact 的，于是
\[
\bigl(H^2(Y,T_Y)^G\bigr)^\vee
 \cong H^0(Y,\Omega_Y^1\otimes K_Y)^G.
\]

问题 (d) 的答案是肯定的。

### 3.2 Künneth 分解正确

有
\[
\Omega_Y^1\otimes K_Y
 =
(2K_{C_1}\boxtimes K_{C_2})
\oplus
(K_{C_1}\boxtimes2K_{C_2}),
\]
从而
\[
H^0(Y,\Omega_Y^1\otimes K_Y)
=
H^0(2K_{C_1})\otimes H^0(K_{C_2})
\oplus
H^0(K_{C_1})\otimes H^0(2K_{C_2}).
\]
这是 \(G\)-等变分解。

### 3.3 非超椭圆性需要补充一步

脚本证明了：每个 \(G\) 中的二阶元在每条 \(C_i\) 上最多固定四点。原因是三个 branch monodromy 的二倍彼此不同，每个相应 branch fiber 含四个固定点。

这只排除了超椭圆 involution \(\iota\) 属于 \(G\) 的情形。若 \(\iota\notin G\)，由于 \(\iota\) 在 \(\operatorname{Aut}(C_i)\) 中中心化所有自同构，\(G\) 将忠实作用于
\[
C_i/\langle\iota\rangle\cong\mathbb P^1.
\]
这会给出嵌入
\[
\mathbb Z_4^2\hookrightarrow\operatorname{PGL}_2(\mathbb C),
\]
但有限 abelian 子群 of \(\operatorname{PGL}_2(\mathbb C)\) 只能是 cyclic 或 \((\mathbb Z_2)^2\)。矛盾。因此两条曲线确实非超椭圆。

于是 canonical multiplication 是 \(G\)-等变同构
\[
\operatorname{Sym}^2H^0(K_{C_i})\xrightarrow{\sim}H^0(2K_{C_i}).
\]
脚本给出的两个 invariant dimension 均为零，故
\[
H^0(Y,\Omega_Y^1\otimes K_Y)^G=0
\]
以及
\[
\boxed{\,H^2(X,T_X^0)=0\,}.
\]

Chevalley–Weil 中若采用相反的 character convention，全部 character 同时取逆；这里的 invariant dimension 仍然为零，因此最终消失结论不受该 convention 影响。

---

## 4. Lee–Park 与六节点同步平滑

\(A_1\) 是 rational double point，也是 class \(T\) singularity，因此 Lee–Park 所引用的 Q-Gorenstein globalization 定理适用。

正确的局部模型是
\[
A_1=\{xy-z^2=0\}\subset\mathbb C^3,
\]
其一维 miniversal deformation 为
\[
\{xy-z^2=\tau\}.
\]
也可写成
\[
u^2+v^2+w^2=\tau.
\]
稿件中的 \(\{uv=t\}\subset\mathbb C^3/(\pm1)\) 不是正确的 \(A_1\) 平滑表达式。

每个节点贡献一个局部参数，因此
\[
H^0(\mathcal T_X^1)
 \cong\bigoplus_{i=1}^6\mathbb C_{p_i}\cong\mathbb C^6.
\]
选取六个坐标都非零的局部 deformation direction。Lee–Park Prop. 2.4(2) 在这里应按变形函子的完整陈述使用：\(H^2(T_X^0)=0\) 消除局部 deformation globalization 的整体 obstruction，从而该局部方向提升为实际 Q-Gorenstein family。仅有切空间映射的满射还不足以单独推出一个收敛的解析族。

所得一参数族的六个局部平滑参数满足
\[
\tau_i(t)=a_it+O(t^2),\qquad a_i\ne0,
\]
故充分小的 \(t\ne0\) 时六个节点全部消失。问题 (e) 的答案是肯定的：RDP 包含在该定理处理的 class \(T\) 情形中。

---

## 5. \(K\) 的 ample 性与 Aubin–Yau

当前稿件中“minimal general-type、\(K^2>0\) 所以 \(K\) ample”的一般性理由不成立；最小一般型曲面可能含有 \(K\cdot C=0\) 的 \((-2)\)-曲线。

本模型有一个更直接的证明。由于 \(\pi\) 在余维一处 étale，
\[
\pi^*K_X=K_Y.
\]
而
\[
K_Y=p_1^*K_{C_1}\otimes p_2^*K_{C_2}
\]
是 ample，因为 \(g(C_1)=g(C_2)=3\)。有限满射下，divisor ample 当且仅当其有限拉回 ample，因此 \(K_X\) ample。

在 Q-Gorenstein family
\[
f:\mathcal X\to\Delta
\]
中，取公共整数 \(m>0\)，使
\[
L=\omega_{\mathcal X/\Delta}^{[m]}
\]
为 line bundle 并与 base change 相容。中央纤维上
\[
L|_X=mK_X
\]
ample。Proper family 中 line bundle 在纤维上 ample 是开性质；缩小 \(\Delta\) 后，\(L|_{X_t}=mK_{X_t}\) ample。因此光滑纤维的 \(K_{X_t}\) ample。

Aubin–Yau 随即给出
\[
\operatorname{Ric}(\omega_t)=-\omega_t.
\]

---

## 6. \(A_1\) Milnor fiber 与最小解消

问题 (f) 的答案是肯定的，但需要区分非紧 affine quadric 与紧 Milnor fiber：

* affine smoothing \(u^2+v^2+w^2=1\) 微分同胚于 \(T^*S^2\)；
* 与充分小 Milnor ball 相交所得紧 fiber 微分同胚于 cotangent disk bundle \(D(T^*S^2)\)；
* 在复定向下，vanishing sphere 的自交数为 \(-2\)，故该 disk bundle 的 Euler number 是 \(-2\)；
* \(A_1\) 最小解消的 exceptional curve 邻域是
  \[
  D(\mathcal O_{\mathbb P^1}(-2)),
  \]
  也是 Euler number \(-2\) 的 oriented disk bundle；
* 两者的共同三维端面为 \(L(2,1)=\mathbb{RP}^3\)。

因此两个局部四维填充确实微分同胚。不过，“局部填充微分同胚并拥有同一外部补集”一般还需要核对端面上的粘合标记。这里最严密的处理是 ADE simultaneous resolution：

对一参数 \(A_1\) 平滑作有限 base change（局部可取 \(\tau=s^2\)），存在 simultaneous resolution
\[
\widetilde{\mathcal X}\longrightarrow\Delta_s
\]
使中央纤维是 \(S\)，而 \(s\ne0\) 的纤维仍是原来的光滑 \(X_{\tau(s)}\)。六个节点彼此分离，可在同一个有限 base change 后同时处理。该 family 是 proper smooth submersion，Ehresmann 定理给出
\[
\boxed{\,S\cong_{\mathrm{diff}}X_t\,}.
\]

最后将 \(X_t\) 上的 Kähler–Einstein metric 经该微分同胚拉回，即得 \(S\) 上满足
\[
\operatorname{Ric}_h=-h
\]
的光滑 Einstein metric。这里无需 \(S\) 原有复结构的 canonical class ample；所用 metric 来自微分同胚的光滑纤维。

---

## 最终评定

六段推理在上述修订后闭合。核心等式为
\[
T_X^0\cong(\pi_*T_Y)^G,\qquad
H^2(X,T_X^0)\cong H^2(Y,T_Y)^G=0,
\]
随后由 Lee–Park 得到六节点同步 Q-Gorenstein 平滑，由 canonical ample 的开性质与 Aubin–Yau 得到精确 Einstein metric，再由 ADE simultaneous resolution 与 Ehresmann 将该 metric 转移到最小解消 \(S\)。当前脚本正确验证了 character algebra；几何证明中必须加入 maximal Cohen–Macaulay、完整非超椭圆论证、正确 \(A_1\) 方程及 simultaneous resolution 这几项。