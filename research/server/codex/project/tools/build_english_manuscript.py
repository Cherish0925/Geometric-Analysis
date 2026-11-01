#!/usr/bin/env python3
"""Assemble a standalone English manuscript from maintained proof sections.

The original research files are read only.  The selection below is explicit:
replaced proofs, management records and finite-check logs are not manuscript
sections.  Mathematical supplements retain the arguments behind the geometric
and variational results rather than replacing them by a status catalogue.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
sys.path.insert(0, str(ROOT / "tools"))
from build_recent_review import compile_math_layout, compile_table_layout

READER = "markdown+tex_math_single_backslash-raw_tex-raw_html-superscript-subscript"

# (section label, English title, relative source, inclusive line selections)
def current(slug, title, name, ranges):
    return dict(label="sec:" + slug, title=title,
                path="mathematics/current/" + name + ".md", ranges=ranges)

def later(slug, title, name, ranges):
    return dict(label="sec:" + slug, title=title,
                path="continuation/" + name + ".md", ranges=ranges)

def original(slug,title,name,ranges):
    return dict(label="sec:"+slug,title=title,
                path="mathematics/current/skill/research/"+name+".tex",ranges=ranges,raw=True)

WEB_ROOT = "archive/sources/20261001-web-increment/Line1_Web_Increment_20260929_30/"

def web(slug, title, name, ranges):
    return dict(label="sec:web-" + slug, title=title,
                path=WEB_ROOT + "research/" + name + ".md", ranges=ranges)

PLAN = [
 {"part": "Integral calibration and the parameter theorem"},
 current("intrinsic-calibration", "Intrinsic integral calibration", "line1_integral_rigidity_paper", [(31,1344)]),
 current("bounded-forms", "A differential criterion for bounded self-dual forms", "round21_analytic", [(16,326),(343,10000)]),
 current("weighted-pencil", "The weighted scalar--Weyl pencil", "line1_functional_pencil", [(5,483)]),
 later("single-parameter", "Constant-weight calibration and finite-parameter separation", "20260927_constant_weight_and_global_fit", [(22,624)]),
 {"tex": "sections/tracefree_gap.tex"},
 {"part": "Linear coercivity, actual suppliers, and sharp variational scale"},
 {"tex": "sections/linear_coercivity.tex"},
 {"tex": "sections/single_solution_coercivity.tex"},
 current("energy-envelopes", "The classical envelope and its differential separation", "line1_energy_envelope_gap", [(9,258)]),
 current("two-chiral", "Two-chirality budgets and realized mixed surgery", "line1_two_chirality_topology", [(13,288)]),
 current("cover-obstructions", "Finite-cover obstructions and ordinary-SW-invisible quotients", "round14_rigidity", [(25,340)]),
 current("twisted-supply", "Twisted monopoles and invariant double-cover supply", "round14_twisted_rigidity", [(3,268)]),
 current("bf-geography", "Stable-cohomotopy supply and realized geography", "line1_bauer_furuta_geography", [(10,329)]),
 later("bf-linear", "A stable-cohomotopy family in the linear exclusion window", "20260927_conformal_separation_and_zero_end", [(381,524)]),
 {"tex": "sections/bf_budget_comparison.tex"},
 {"tex": "sections/variational_geometry.tex"},
 later("directional-variations", "Quadratic curvature variation and directional lower bounds", "20260927_local_geometry_and_variational_extrema", [(15,460)]),
 {"tex": "sections/quadratic_and_matter.tex"},
 {"part": "The finite-density endpoint and global variational selection"},
 {"tex": "sections/finite_density_endpoint.tex"},
 {"tex": "sections/variational_selection_and_global_cost.tex"},
 {"part": "First-order geometry and the full variational problem"},
 later("surgery-stability", "Surgery limits and transverse first-order stability", "20260927_endpoint_covariance_and_surgery_limits", [(338,1645)]),
 later("moving-centers", "Moving centers and marked harmonic slices", "20260928_marked_centers_and_harmonic_slices", [(28,590),(610,10000)]),
 later("caps", "Intrinsic caps and global curvature reduction", "20260928_intrinsic_caps_and_stability", [(13,538)]),
 later("relative-cells", "Relative cell costs and non-Kähler variations", "20260928_relative_cell_cost", [(11,815)]),
 later("coupled-filling", "Localization, coupled fillings, and finite-amplitude competitors", "20260928_localization_and_coupled_filling", [(10,10000)]),
 later("signed-selection", "Signed characteristic mass and genuine near-minimizers", "20260928_signed_characteristic_selection", [(11,535)]),
 later("conformal-flow", "Conformal flow, transverse variations, and stationary equations", "20260927_signed_balance_and_conformal_flow", [(18,847)]),
 {"tex": "sections/field_interfaces_and_curvature_interactions.tex"},
 {"tex": "open_problems.tex"},
 {"appendix": True, "part": "Local rigidity and weighted geometric analysis"},
 {"tex": "sections/normalized_existence.tex"},
 {"tex": "sections/early_pointwise_rigidity.tex"},
 original("early-local-rigidity", "Local developments, exact topological separation, and necessary collapse", "20260916_uniform_gap", [(64,492)]),
 original("early-joint-density", "Joint scalar and spectral density with explicit constants", "20260916_rigidity", [(80,102),(266,283),(311,403)]),
 original("supercritical-bound", "The explicit supercritical Ricci-eigenvalue bound", "20260916_rigidity", [(483,520)]),
 {"tex": "sections/ricci_box_optimization.tex"},
 original("early-walsh", "Retained monopole defects and Walsh polarization", "20260916_rigidity", [(630,640),(647,968)]),
 original("early-local-flow", "Weighted local flow and conditional terminal rigidity", "20260916_rigidity", [(595,629),(970,1880)]),
 {"tex": "sections/analytic_limitations.tex"},
 {"tex": "sections/early_equality_geometry.tex"},
 original("symmetric-reductions", "Nil and circle reductions of the Einstein equation", "20260916_rigidity", [(1881,1960)]),
 original("quotient-smoothing", "Actual product-quotient smoothings", "20260916_rigidity", [(1961,2072)]),
 original("curvature-spikes", "Pointwise small Ricci defect with full-curvature spikes", "20260916_construction", [(2158,2203)]),
 {"part": "Actual forms, periods, and compatible Weyl structure"},
 current("product-calibration", "The realizable product calibration", "round15_rigidity", [(1,10000)]),
 current("product-endpoint", "Curvature control at the product volume endpoint", "round16_rigidity", [(1,10000)]),
 current("product-propagation", "Integral product calibration and quantitative propagation", "round17_integral", [(1,10000)]),
 current("actual-forms", "Harmonic Chern alignment from actual monopoles", "line1_composed_application", [(10,332)]),
 current("scalar-band", "The scalar-band remainder without an Einstein hypothesis", "line1_scalar_band_remainder", [(16,626)]),
 current("nonkahler-transfer", "Scalar coherence and the non-Kähler transfer", "line1_non_kahler_bridge", [(10,164)]),
 current("symplectic-chamber", "The actual symplectic chamber when the canonical square is positive", "round21_chambers", [(116,173)]),
 current("period-inertia", "Simultaneous saturation and the positive inertia of periods", "line1_period_inertia", [(9,332)]),
 current("periods", "Intersection covariance and scalar slow modes", "round18_periods", [(1,10000)]),
 current("positive-planes", "Properness of period budgets on positive planes", "round20_rigidity", [(1,10000)]),
 later("joint-matrix", "A joint sign-correlation criterion without a spectral gap", "20260926_boundary_compatibility", [(128,284)]),
 current("variable-calibration", "Variable-amplitude calibration and exact differential identities", "line1_variable_calibration", [(9,362)]),
 current("negative-selection", "Selection of a variable negative Weyl amplitude", "line1_variable_negative_selection", [(1,10000)]),
 current("half-weyl", "Derivative budgets from the half-Weyl equation", "line1_half_weyl_regularity", [(6,324)]),
 current("signed-weyl", "The signed harmonic-Weyl balance", "line1_signed_harmonic_weyl", [(5,252)]),
 current("spectral-einstein", "Spectral restrictions for exact Einstein metrics", "line1_einstein_spectral_application", [(1,10000)]),
 current("spectral-escape", "Spectral separation on non-virtually-Kähler smooth types", "line1_allowed_branch_escape", [(17,134)]),
 current("energy-selection", "Ricci-energy selection and scalar coherence", "line1_energy_selection", [(32,371)]),
 current("kahler-energy", "Kähler curvature energy and primitive periods", "line1_kahler_energy", [(1,10000)]),
 current("all-class-ceiling", "The all-class ceiling on shear topology", "round19_global_gap", [(1,10000)]),
 current("entropy-comparison", "Rank-one degree entropy and monopole budgets", "line1_rank_one_entropy_scope", [(1,10000)]),
 current("clifford-block", "An auxiliary Clifford-block system and its supply obstruction", "round12_uniformization", [(5,451)]),
 {"part": "Compactness, topology, and exact geometric realization"},
 current("aspherical-cores", "Half-flat ALE cores and aspherical topology", "line1_aspherical_no_bubbles", [(1,10000)]),
 later("compact-realization", "Einstein realization in a compact geometric regime", "20260923_compact_realization", [(8,393)]),
 later("topological-cores", "Topological exclusion beyond asphericity", "20260923_topological_core_scope", [(9,221)]),
 later("critical-chiral", "Critical chiral thresholds and paired concentration", "20260923_critical_chiral_threshold", [(9,239)]),
 later("ale-boundary", "ALE boundary compatibility and Weyl-free compactness", "20260924_ale_boundary_compatibility", [(15,213)]),
 later("gauge-ke", "From actual saturation to a Kähler--Einstein metric", "20260923_gauge_saturation_ke", [(9,452)]),
 later("allowed-rigidity", "Exact rigidity on the allowed Weyl branch", "20260923_allowed_mode_rigidity", [(9,383)]),
 later("bilateral", "Bilateral saturation and bidisk realization", "20260924_bilateral_realization", [(11,10000)]),
 later("chern-boundary", "Complex-hyperbolic realization on the Chern boundary", "20260924_chern_boundary_realization", [(7,10000)]),
 later("virtual-realization", "Finite-cover supply and realization on the base", "20260924_virtual_gauge_realization", [(9,10000)]),
 later("local-repair", "Uniformly local nonlinear Einstein repair", "20260924_uniformly_local_repair", [(10,259)]),
 later("higher-local-repair", "Uniformly local repair in higher dimensions", "20260924_higher_dimensional_local_repair", [(9,10000)]),
 later("local-to-global", "Local harmonic radius and full-tensor repair", "20260924_local_to_global_scope", [(1,10000)]),
 later("collapsed-bilateral", "Bilateral geometry on rewound collapsed balls", "20260924_collapsed_bilateral_bulk", [(1,10000)]),
 later("orbifold", "Orbifold compactification and marked smoothing", "20260924_orbifold_smoothing_bridge", [(17,330)]),
 {"part": "Global transfer, integrable kernels, and slow geometry"},
 later("cycle-holonomy", "Cycle deformation and finite monodromy", "20260924_cycle_holonomy_realization", [(20,485)]),
 later("ricci-monodromy", "Pointwise Ricci control and monodromy displacement", "20260924_ricci_monodromy_realization", [(13,254)]),
 later("cyclic-kernel", "Repair with the full integrable kernel on cyclic covers", "20260924_integrable_kernel_cyclic_repair", [(12,408)]),
 later("thin-monodromy", "Thin-fiber monodromy and global reduction", "20260924_thin_monodromy_alternative", [(20,541)]),
 later("slow-moduli", "Nonlinear slow-moduli equations and fixed-amplitude metrics", "20260924_nonlinear_slow_moduli", [(26,385)]),
 later("moduli-gauge", "Actual monopole deficits as moduli energy", "20260924_moduli_energy_gauge", [(11,324)]),
 later("milnor-matching", "Harmonic forms and whole-filling Milnor matching", "20260924_harmonic_contact_milnor_matching", [(16,399)]),
 later("harmonic-zeros", "Harmonic zeros, scale costs, and complete marked fillings", "20260924_harmonic_zero_scale", [(19,410)]),
 {"part": "Closed degenerating constructions and their global topology"},
 {"tex": "sections/fixed_bundle_geometry.tex"},
 current("multitwist", "Fixed multitwist bundles and exact representation-volume loss", "round8_multitwist", [(5,10000)]),
 current("closed-shear", "Closed sheared gluing with pointwise Ricci control", "round11_closed_gluing", [(1,10000)]),
 current("shear-topology", "Graph topology and the sheared fundamental group", "round11_graph_topology", [(1,10000)]),
 current("virtual-nonkahler", "The virtual non-Kähler obstruction", "round11_kahler", [(1,10000)]),
 current("shear-variational", "Variational invariants of the fixed closed shear", "round11_variational", [(1,10000)]),
 current("shear-global", "Canonical classes and all Einstein candidates on a fixed shear", "round12_global", [(1,10000)]),
 current("shear-symmetry", "Universal-cover rigidity and complete local symmetry breaking", "round12_symmetry", [(5,142)]),
 current("hilbert-modular", "The obstruction to Hilbert-modular compact cores", "round16_global", [(5,413)]),
 current("canonical-shear", "Canonical harmonic forms on the fixed shear", "line1_canonical_shear", [(1,10000)]),
 current("shear-capacity", "Connection capacity, waist force, and Teichmüller response", "round14_shear", [(3,280)]),
 current("full-collar", "Full-collar shear and exact scalar calibration", "round14_global", [(3,514)]),
 current("shear-repair-radius", "An all-tensor lower bound on the Einstein repair radius", "round14_repair_radius", [(3,244)]),
 current("harmonic-projection", "Intrinsic harmonic projection energy and its exact remainder", "round9_bundle", [(5,395)]),
 current("kodaira-controls", "Exact Einstein control families with fixed monodromy image", "round10_bundle", [(5,312)]),
 current("integral-limits", "Integral approximation without an Einstein output", "round18_integral_limits", [(1,10000)]),
 current("yamabe-endpoint", "The negative Yamabe endpoint and scalar coherence", "line1_yamabe_endpoint", [(1,10000)]),
 current("conformal-neck", "Conformal collars and exact curvature bookkeeping", "line1_conformal_neck", [(1,10000)]),
 current("product-operator", "The complete product operator and its low modes", "round17_product_operator", [(1,10000)]),
 current("twisted-operator", "Finite-monodromy operator channels", "round18_twisted_operator", [(1,10000)]),
 current("slow-construction", "Actual slow fields and complete operator response", "round20_construction", [(1,10000)]),
 {"part": "Signed topology, actual cores, and the weak endpoint"},
 later("actual-topological", "Actual field identities and topological cost", "20260926_actual_topological_cost", [(22,212),(276,376),(410,651)]),
 later("mixed-current", "Mixed transgression and the actual opposite-spinor equation", "20260927_mixed_current_and_signed_cores", [(38,249),(664,10000)]),
 later("zero-end-geometry", "Weak endpoint forms and conditional curvature rigidity", "20260927_conformal_separation_and_zero_end", [(525,10000)]),
 later("bounded-ricci-endpoint", "The endpoint with bounded Ricci curvature and Euler density", "20260927_local_geometry_and_variational_extrema", [(462,1268)]),
 later("covering-endpoint", "Covering geometry, chiral caps, and first-order ALE matching", "20260927_covering_geometry_and_sharp_subfamilies", [(22,419),(539,981)]),
 later("whole-core", "The sharp cost of complete smooth cores", "20260927_full_core_cost_and_extremal_metrics", [(17,1013)]),
 later("marked-charge", "Marked determinant charge and high-index actual cores", "20260927_marked_charge_and_first_order_flux", [(14,1038)]),
 later("actual-core-fit", "Constant-weight actual cores and their global extension cost", "20260927_constant_weight_and_global_fit", [(625,1010)]),
 later("endpoint-covariance", "Endpoint covariance and current--Hessian interaction", "20260927_endpoint_covariance_and_surgery_limits", [(25,337)]),
 later("phase-curvature", "Polynomial phase curvature through torsion zeros", "20260928_zero_endpoint_phase_curvature", [(15,361)]),
 later("torsion-prolongation", "Actual torsion prolongation and the Ricci forcing block", "20260928_actual_torsion_prolongation", [(9,265)]),
 later("quartic-flux", "Signed quartic flux and the remaining curvature interaction", "20260928_signed_quartic_flux", [(1,10000)]),
 {"part": "Strong actual currents and endpoint prolongation"},
 web("strong-current", "Strong current convergence from the actual positive spinor", "C/O10_Strong_Current_Prerequisite", [(13,10000)]),
 web("direct-resolvent", "A bounded resolvent on the actual opposite-spinor bundle", "C/O10_Direct_Resolvent_Prerequisite", [(5,10000)]),
 web("first-prolongation", "The full first prolongation and its adjoint test", "B/O10_Resolvent_Prolongation", [(5,216)]),
 web("weak-bianchi", "Derivative covariance and the fifth-line coefficient", "C/O10_Weak_Bianchi", [(5,213),(230,10000)]),
 {"tex": "sections/web_density_and_geometric_supplements.tex"},
 web("density-rate", "Fifth-line exclusion with growing opposite-Weyl energy", "D/O10_Alternative_Global", [(5,10000)]),
 {"tex": "sections/web_primitive_rate.tex"},
 {"part": "Unbounded-density identities and the remaining radial interaction"},
 web("unbounded-reductions", "Capacity reduction and exact weighted cancellations", "D/O10_Unbounded_Density", [(5,233)]),
 web("double-weighted", "Double weighted tests and bilinear Hessian cancellation", "E/O10_Double_Weighted_Test", [(7,10000)]),
 web("radial-measure", "Amplitude defect measures and weak radial tests", "E/O10_Global_Closure_Attempt", [(22,258)]),
 web("mass-transfer", "Strong radial transfer to the original actual field", "F/O10_Actual_Mass_Transfer", [(5,10000)]),
 web("radial-matrix", "The full polynomial radial one-form", "F/O10_Radial_Matrix_Identity", [(5,184)]),
 web("exact-hessian", "The exact positive-spinor Hessian limit", "F/O10_Exact_Hessian_Budget_Check", [(5,10000)]),
 web("line-limitation", "Why the rank-one lemma retains a Ricci budget", "C/O10_LineBundle_Limitation", [(7,10000)]),
 web("vector-scope", "Orthogonal obstruction estimates and their scale", "C/O10_Vector_Obstruction", [(17,230)]),
 web("local-system", "Exact local compatibility and the role of prolongation", "E/O10_Local_Model_And_Prolongation_Audit", [(5,61)]),
 {"part": "Critical variations, complete costs, and competing global geometry"},
 {"tex": "sections/web_variational_supplements.tex"},
 web("ordinary-competitors", "Exceptional topology and complete competitor tests", "C/O11_Geometry_Competitor", [(5,126)]),
 web("bulk-invariance", "Alternative complex bulks and invariant recovery cost", "D/O11_Competitors", [(21,101)]),
 web("ideal-minimizers", "Ideal minimizers and complete AE and ALE costs", "E/O11_Ideal_Minimizer", [(5,10000)]),
 web("full-collar-cost", "Complete Euclidean collars and finite complex-hyperbolic collars", "F/O11_Constructive_Audit", [(5,57),(83,10000)]),
 web("critical-stability", "Direct variations at an exact critical metric", "F/O11_Critical_Stability_Attempt", [(5,127)]),
 web("entropy-scope", "Entropy invariance under ordinary surgeries", "E/O11_BCG_Test", [(5,89)]),
 web("cover-topology", "Compactly supported intersection forms in the universal cover", "E/O11_Global_Alternative", [(5,69)]),
 web("field-selection", "Actual field selection and metric variation", "E/O11_Closure_Attempt", [(5,72)]),
]

PATH_LABELS = {}
for spec in PLAN:
    if "path" in spec:
        PATH_LABELS.setdefault(spec["path"], spec["label"])
ALIASES = {
 "mathematics/current/round4_rigidity.md": "sec:intrinsic-calibration",
 "mathematics/current/round4_all_sign_gap.md": "sec:intrinsic-calibration",
 "mathematics/current/round5_rigidity.md": "sec:intrinsic-calibration",
 "mathematics/current/lebrun_stability_closure.md": "sec:intrinsic-calibration",
 "mathematics/current/round21_chambers.md": "sec:intrinsic-calibration",
 "mathematics/current/round13_chamber.md": "sec:intrinsic-calibration",
 "mathematics/current/round2_rigidity.md": "sec:analytic-limitations",
 "mathematics/current/round3_monopole_input.md": "sec:intrinsic-calibration",
 "mathematics/current/line1_compactified_pencil.md": "sec:single-parameter",
 "mathematics/current/round21_comparison.md": "sec:kahler-energy",
}
PATH_LABELS.update(ALIASES)
BASENAME_LABELS = {Path(path).name: label for path, label in PATH_LABELS.items()}
BASENAME_LABELS.update({
 "01_O10_Strong_Current.md": "sec:web-strong-current",
 "O10_Strong_Current.md": "sec:web-strong-current",
 "O10_Resolvent_Audit.md": "sec:web-direct-resolvent",
 "O10_All_Finite_Density.md": "sec:finite-density-endpoint",
 "O10_Finite_Density_Complete_Proof.tex": "sec:finite-density-endpoint",
 "O10_Topological_Escape.md": "sec:finite-density-endpoint",
 "O10_LineBundle_Resolvent_Audit.md": "sec:finite-density-endpoint",
 "O10_Abelian_Spectral_Independent_Audit.md": "sec:finite-density-endpoint",
 "O10_Fifth_Line_Audit.md": "sec:web-positive-potential",
 "03_Finite_Density_Fifth_Line.md": "sec:web-positive-potential",
 "User_Fifth_Line.md": "sec:web-positive-potential",
 "O10_Primitive_Rate_Audit.md": "sec:web-primitive-rate",
 "04_Quantitative_Escape.md": "sec:web-growing-energy-chern",
 "05_Low_Amplitude_and_O11_Scope.md": "sec:web-inverse-amplitude",
 "02_O11_Variational_Selection.md": "sec:variational-selection-global-cost",
 "03_O11_Classical_Budget.md": "sec:variational-selection-global-cost",
 "O11_Global_Sharp.md": "sec:variational-selection-global-cost",
 "O11_Threshold_Variation.md": "sec:web-threshold-variation",
 "O11_Descent_or_Recovery.md": "sec:web-curvature-compensation",
 "O11_Positive_Curvature_Compensation.md": "sec:web-curvature-compensation",
 "O11_Global_Variation.md": "sec:web-codazzi-scope",
})
ID_LABELS = {
 "I01":"early-local-rigidity", "I02":"intrinsic-calibration", "I03":"intrinsic-calibration", "I04":"twisted-supply",
 "I05":"bounded-forms", "I06":"actual-forms", "I07":"weighted-pencil",
 "I08":"two-chiral", "I09":"single-parameter", "I10":"bf-geography",
 "I11":"product-calibration", "I12":"period-inertia", "I13":"variable-calibration", "I14":"spectral-einstein",
 "I15":"aspherical-cores", "I16":"aspherical-cores", "I17":"kahler-energy", "I18":"all-class-ceiling",
 "I19":"compact-realization", "I20":"topological-cores",
 "I21":"critical-chiral", "I22":"gauge-ke", "I23":"allowed-rigidity",
 "I24":"ale-boundary", "I25":"bilateral", "I26":"chern-boundary",
 "I27":"local-to-global", "I28":"virtual-realization", "I29":"local-repair", "I30":"collapsed-bilateral", "I31":"orbifold",
 "I32":"cycle-holonomy", "I33":"cyclic-kernel", "I34":"milnor-matching",
 "I35":"thin-monodromy", "I36":"moduli-gauge", "I37":"harmonic-zeros",
 "I38":"actual-topological", "I39":"mixed-current", "I40":"linear-coercivity",
 "I41":"linear-coercivity", "I42":"zero-end-geometry", "I43":"covering-endpoint",
 "I44":"variational-geometry", "I45":"bounded-ricci-endpoint", "I46":"bounded-ricci-endpoint",
 "I47":"whole-core", "I48":"whole-core", "I49":"conformal-flow",
 "I50":"marked-charge", "I51":"single-parameter", "I52":"surgery-stability",
 "I53":"caps", "I54":"relative-cells", "I55":"coupled-filling",
 "N1":"tracefree-gap",
}

def plain(node):
    if isinstance(node, dict):
        t, c = node.get("t"), node.get("c")
        if t == "Str": return c
        if t in ("Space", "SoftBreak", "LineBreak"): return " "
        if t in ("Math", "Code"): return c[1]
        if t == "Link": return plain(c[1])
        return plain(c)
    if isinstance(node, list): return "".join(map(plain,node))
    return ""

def raw(text):
    return {"t":"RawInline", "c":["latex",text]}

def safe(s):
    return re.sub(r"[^a-zA-Z0-9:.-]", "-", s)

def latex_text(s):
    return s.replace("&",r"\&").replace("_",r"\_").replace("%",r"\%")

OMIT_HEAD = re.compile(r"verification|reproducib|dependency (?:trace|record)|"
    r"research status|status and|continuation point|continuing research|"
    r"sources and|primary.source|logical summary|what has changed|"
    r"what is resolved|remaining tasks|finite checks|coordinate checks|proof inputs and checks", re.I)
OMIT_PARA = re.compile(r"^(?:\d{1,2} September 2026|Baseline:|Source commit:|"
    r"The new project conclusion|"
    r"Global priority|Verification:|Independent verification|The script |"
    r"The companion script|The numerical script|Reproduction:)", re.I)

def selected_body(spec):
    lines=(ROOT/spec["path"]).read_text().splitlines(keepends=True)
    result=[]
    for a,b in spec["ranges"]:
        if not 1<=a<=len(lines): raise ValueError(spec)
        result.extend(lines[a-1:min(b,len(lines))])
    body="".join(result)
    if spec["label"] == "sec:web-entropy-scope":
        # The preserved source omitted the closing display delimiter after
        # its equation (4). Repair the presentation, not the source record.
        body = body.replace("\\tag{4}\non every", "\\tag{4}\n\\]\non every")
        body = body.replace("Besson–Courtois–Gallot's main theorem, printed p.734,",
                            "Besson--Courtois--Gallot's main theorem [BCG],")
        body = body.replace("arXiv:0807.1187v2, Theorem 1.1,",
                            "[BIS], Theorem 1.1,")
        body = body.replace("Aubry, arXiv:0810.0149, §1.4,",
                            "Aubry [Aubry], Section 1.4,")
        body = body.replace("Theorem 1.4, explicitly assumes",
                            "[CW], Theorem 1.4, explicitly assumes")
    if spec["label"] == "sec:web-density-rate":
        body = body.replace(
            "No rate formula expressing \\(\\eta_j\\) in terms of the original scalar defect \\(\\kappa_j\\) is established in this note.",
            "The rate in terms of the original defect is proved in [the primitive-error transfer](#sec:web-primitive-rate).")
        body = body.replace(
            "No explicit modulus \\(\\eta\\le\\omega(\\kappa,\\beta^{-1})\\) with a power rate is claimed here. The inherited strong-current argument supplies smallness; extracting a modulus requires tracing its truncation and resolvent choices. Even an explicit modulus alone would not bound \\(b\\) or force (2).",
            "[The primitive-error transfer](#sec:web-primitive-rate) gives an explicit power rate by tracing the truncation and resolvent estimates, including the $H^1$ and $L^4$ transfers. The resulting polynomial density bound still does not force (2) at arbitrary unbounded density.")
        body = body.replace("the supplied proof", "[the fifth-line proof](#sec:web-positive-potential)")
        body = body.replace("This finite algebra was independently checked using the Clifford-to-Cartan script; it prevents mistaking a missing negative-curvature estimate for an immediately available positive-curvature one.",
                            "Thus the positive-curvature block alone does not supply this negative-curvature estimate.")
    if spec["label"].startswith("sec:web-"):
        body = re.sub(r"\bContinuation D\b", "The simultaneous-field decomposition", body)
        body = body.replace("D/O11_Global_Sharp.md", "[the simultaneous-field proof](#sec:variational-selection-global-cost)")
        body = body.replace("The primary source checked this turn is", "The relevant classical source is")
        body = body.replace("The project already established this geometric identification. It is not new research credit for this turn. The fresh source check only prevents the erroneous assumption that an exact Ricci infimum already supplies the exact trace-free Ricci infimum.",
                            "The exact Ricci infimum therefore does not by itself determine the trace-free Ricci infimum.")
        body = body.replace("Inputs already proved in continuation B", "Actual-field and resolvent inputs")
        body = body.replace("Integration with the new rank-one lemma", "The rank-one Chern consequence")
        body = body.replace("What this does and does not close", "The remaining radial interaction")
        body = body.replace("Current boundary of the combined-equation attempt", "The remaining combined equation")
        body = body.replace("What the full actual equations would have to add", "Information not supplied by the scalar model")
        body = body.replace("What the degree theorem actually gives", "The degree-entropy inequality")
        body = body.replace("Exact consequence for the research decision", "Consequences for complete competitors")
    # A source can contribute separate sections to this manuscript. Resolve
    # these proof dependencies before path/ID fallback loses the cited claim.
    fragment_references = {
        "sec:marked-charge": [
            ("[I41, Sections 6--7](20260927_conformal_separation_and_zero_end.md)",
             "[determinant saturation](#subsec:proof:zero-end-geometry:s6) and [signed transition flux](#subsec:proof:zero-end-geometry:s7)"),
            ("[I41, Section 15.1](20260927_conformal_separation_and_zero_end.md)",
             "[the hyperbolic actual core](#subsec:proof:zero-end-geometry:s15.1)"),
            ("I41 Section 15.1.",
             "[the hyperbolic actual-core construction](#subsec:proof:zero-end-geometry:s15.1)."),
        ],
        "sec:actual-core-fit": [
            ("[I41, Section 6](20260927_conformal_separation_and_zero_end.md)",
             "[the determinant saturation](#subsec:proof:zero-end-geometry:s6)"),
        ],
        "sec:phase-curvature": [
            ("and notation of I51/I52:",
             "and notation of [the constant-weight solution](#sec:single-parameter) and [the endpoint covariance](#sec:endpoint-covariance):"),
            ("These are the same smooth bounded rational weights as in I52.\nThe actual quadratic Dirac identity there is",
             "These are the smooth bounded rational weights of [the endpoint covariance estimate](#subsec:proof:endpoint-covariance:s1). The [quadratic Dirac identity](#subsec:proof:endpoint-covariance:s2.1) gives"),
            ("With the curvature-operator convention used in I41,",
             "With the curvature-operator convention of [the actual torsion calculation](#subsec:proof:zero-end-geometry:s14),"),
            ("[I41, Sections 15--15.1](20260927_conformal_separation_and_zero_end.md)",
             "[the local right inverses](#subsec:proof:zero-end-geometry:s15) and [their hyperbolic implementation](#subsec:proof:zero-end-geometry:s15.1)"),
        ],
        "sec:quartic-flux": [
            ("[I41, Section 15.1](20260927_conformal_separation_and_zero_end.md)",
             "[the hyperbolic actual-core construction](#subsec:proof:zero-end-geometry:s15.1)"),
        ],
        "sec:bounded-ricci-endpoint": [
            ("right inverses from Section 15\nof the conformal continuation",
             "right inverses from [the local actual-core construction](#subsec:proof:zero-end-geometry:s15)"),
        ],
        "sec:zero-end-geometry": [
            ("the BF family in Section 4",
             "the BF family in [the linear exclusion window](#sec:bf-linear)"),
        ],
        "sec:surgery-stability": [
            ("Here \\(Q\\) is the surgery number, unrelated to the ASD form in Section 1.",
             "Here \\(Q\\) is the surgery number."),
        ],
        "sec:endpoint-covariance": [
            ("The local actual cores in I50/I51",
             "The local actual cores in [the marked-charge construction](#sec:marked-charge) and [the split-core construction](#subsec:proof:actual-core-fit:s4)"),
            ("For the last estimate insert I51's actual torsion Dirac equation,",
             "For the last estimate insert [the actual torsion Dirac equation](#eq:proof:mixed-current:e2.2),"),
            ("as in I51's scale calculation.",
             "as in [the split-core scale calculation](#subsec:proof:actual-core-fit:s4)."),
        ],
    }
    for old,new in fragment_references.get(spec["label"], []):
        count=body.count(old)
        if count != 1:
            raise ValueError(f"Expected one dependency reference in {spec['label']}: {old!r}; found {count}")
        body=body.replace(old,new)
    body=body.replace("This note uses", "We use").replace("This note proves", "We prove")
    body=body.replace("This note supplies exact tests for the corrected first scientific line.", "We give exact equality and strictness examples.")
    body=body.replace("For the actual variational target, I41 permits replacing near-minimizers\nby their negative Yamabe representatives.",
        r"For the variational target, Proposition~\ref{prop:vg-conformal-infimum} permits replacing near-minimizers by their negative Yamabe representatives.")
    body=body.replace("I41's negative\nYamabe reduction",r"the negative Yamabe reduction of Proposition~\ref{prop:vg-conformal-infimum}")
    body=body.replace("The conformal reduction in I41, Section 3,\ngives inf_g J=alpha.",r"Proposition~\ref{prop:vg-conformal-infimum} gives \(\inf_g\mathcal J=\alpha\).")
    body=body.replace("The passage from the project infimum to the zero level in (1.4) uses I41.",r"The passage from the infimum to the zero level in (1.4) uses Proposition~\ref{prop:vg-conformal-infimum}.")
    body=body.replace("The exact conformal formula in I41 says\nJ(g) is a weighted average of J_hat and 1.",r"Proposition~\ref{prop:vg-conformal-infimum} expresses \(\mathcal J(g)\) as a weighted average of \(\mathcal J(\widehat g)\) and \(1\).")
    prose_math={
      "For (14.4) the real Jacobian is epsilon^{-4} and m=|x|^2/epsilon^2.\nIf chi equals one near zero and vanishes before m=R_0^2, polar integration\ngives int dchi wedge T_t=-int_0^{R_0^2}chi'(m)dm=1.":r"For (14.4) the real Jacobian is \(\epsilon^{-4}\) and \(m=|x|^2/\epsilon^2\). If \(\chi\) equals one near zero and vanishes before \(m=R_0^2\), polar integration gives \[\int d\chi\wedge T_t=-\int_0^{R_0^2}\chi'(m)\,dm=1.\]",
      "Fix f_*>0 and a>0. For every sufficiently\nsmall epsilon>0 there is a smooth unitary determinant connection A_epsilon\nand positive spinor Phi_epsilon on the Euclidean ball B_{2epsilon}":r"Fix \(f_*>0\) and \(a>0\). For every sufficiently small \(\epsilon>0\) there is a smooth unitary determinant connection \(A_\epsilon\) and positive spinor \(\Phi_\epsilon\) on the Euclidean ball \(B_{2\epsilon}\)",
      "Indeed the limiting y-field has m=a^4|y|^2, |dt|^2=4a^4,\n|<t,dt>|^2=2a^8|y|^2 and |dm|^2=4a^8|y|^2; integrate with\nthe four-dimensional polar factor 2pi^2 r^3 dr.":r"Indeed the limiting \(y\)-field satisfies \[m=a^4|y|^2,\quad |dt|^2=4a^4,\quad |\langle t,dt\rangle|^2=2a^8|y|^2,\quad |dm|^2=4a^8|y|^2.\] Integrate with the four-dimensional polar factor \(2\pi^2r^3\,dr\).",
      "Indeed c_2(S^-)=(a^2+2chi-3tau)/4; tensoring by L adds\nc_1(S^-)c_1(L)+c_1(L)^2=2a^2.":r"Indeed \(c_2(S^-)=(a^2+2\chi-3\tau)/4\); tensoring by \(L\) adds \[c_1(S^-)c_1(L)+c_1(L)^2=2a^2.\]",
      "For the flat metric the inherited majorant weight is exactly sqrt(3), so\nf_*=sqrt(3) is an allowed concrete choice; there is no zero-weight limit.\nChoosing a^2=4/3 and radius R_0 epsilon with R_0=2sqrt(2)/3 makes the\nleading boundary torsion mass a^4 R_0^2=128/81 equal to the zero-end\nmass.":r"For the flat metric the majorant weight is \(\sqrt3\), so \(f_*=\sqrt3\) is an allowed choice. Taking \(a^2=4/3\) and radius \(R_0\epsilon\), where \(R_0=2\sqrt2/3\), makes the leading boundary torsion mass \(a^4R_0^2=128/81\) equal to the zero-end mass.",
      "is 2a^4 R_0/epsilon+O(1)":r"is \(2a^4R_0/\epsilon+O(1)\)",
      "Determinant saturation gives C_+/V=O(beta^{-1}+sqrt eta)->0, while\n4pi^2T_+/V=2/3+16/(3beta^2)+O(sqrt eta).":r"Determinant saturation gives \[\frac{C_+}{V}=O(\beta^{-1}+\sqrt\eta)\longrightarrow0,\qquad \frac{4\pi^2T_+}{V}=\frac23+\frac{16}{3\beta^2}+O(\sqrt\eta).\]",
      "Work first on the fixed Euclidean ball B_2 in y-coordinates.\nLet lambda=epsilon^2 and Phi_0=a e_1+epsilon g_0(y)e_2, with g_0 from\n(14.4). Thus D^+Phi_0=0. On imaginary-valued forms put\nT=(d^*,sqrt(2)d^+). In flat space TT^*=Delta on Omega^0 direct-sum\nOmega^2_+, with Delta nonnegative.":r"Work on the fixed Euclidean ball \(B_2\) in \(y\)-coordinates. Let \(\lambda=\epsilon^2\) and \(\Phi_0=ae_1+\epsilon g_0(y)e_2\), with \(g_0\) from (14.4); thus \(D^+\Phi_0=0\). On imaginary-valued forms put \(T=(d^*,\sqrt2d^+)\). In flat space \[TT^*=\Delta\quad\text{on }\Omega^0\oplus\Omega^2_+,\] where \(\Delta\) is nonnegative.",
      "Then TR_A=Id and D^+R_D=Id. On C^{k,alpha} for fixed k>=3,\n0<alpha<1, both are bounded operators gaining one derivative":r"Then \(TR_A=\mathrm{Id}\) and \(D^+R_D=\mathrm{Id}\). On \(C^{k,\alpha}\), for fixed \(k\ge3\) and \(0<\alpha<1\), both are bounded operators gaining one derivative",
      "q_beta=4(1+1/beta), rho_beta=2sqrt(q_beta)/3 and\nU_beta=(4/3)(2/beta-1)":r"\(q_\beta=4(1+1/\beta)\), \(\rho_\beta=2\sqrt{q_\beta}/3\), and \(U_\beta=(4/3)(2/\beta-1)\)",
      "avg[(S-2m_beta)^2/S]=avg S-4m_beta+4m_beta^2 avg(1/S)":r"\[\fint\frac{(S-2m_\beta)^2}{S}=\fint S-4m_\beta+4m_\beta^2\fint\frac1S\]",
      "|t||dW|+|P||t||dW|<=C(|d rho|+|H|)":r"\(|t||dW|+|P||t||dW|\le C(|d\rho|+|H|)\)",
      "S=m_beta+m+d, avg d=O(eta)":r"\(S=m_\beta+m+d\), \(\fint d=O(\eta)\)",
      "avg[(S-2m_beta)^2/S]=O(sqrt eta)":r"\(\fint (S-2m_\beta)^2/S=O(\sqrt\eta)\)",
      "Moreover |chi'|<=C theta. The curvature of E_- is bounded algebraically\nby C(|W^-|+|s|+|Ric^circ|+|F_A|).":r"Moreover \(|\chi'|\le C\theta\). The curvature of \(E_-\) is bounded algebraically by \(C(|W^-|+|s|+|\Ric^\circ|+|F_A|)\).",
      "Given Lambda_0,L>0, every closed Ric=-g four-manifold with\nLambda<=Lambda_0":r"Given \(\Lambda_0,L>0\), every closed four-manifold with \(\Ric=-g\) and \(\Lambda\le\Lambda_0\)",
      "Take a^2=4/3. The physical determinant curvature has F_A^-=O(epsilon)\nand |F_A^+|^2=8/9+O(epsilon^2).":r"Take \(a^2=4/3\). The physical determinant curvature has \(F_A^-=O(\varepsilon)\) and \(|F_A^+|^2=8/9+O(\varepsilon^2)\).",
      "H^1(Q_Gamma;R)=H^2(Q_Gamma;R)=0":r"\(H^1(Q_\Gamma;\mathbb R)=H^2(Q_\Gamma;\mathbb R)=0\)",
      "||A-A_0||_{W^{1,2}}<=C||F_A||_2->0":r"\(\|A-A_0\|_{W^{1,2}}\le C\|F_A\|_2\to0\)",
      "V>=2pi^2/(1+delta)^2":r"\(V\ge2\pi^2/(1+\delta)^2\)",
      "Vol B_1(x)>=v(D)>0":r"\(\Vol B_1(x)\ge v(D)>0\)",
      "T_+>0 and 3pi^2T_+<=V<=12pi^2T_+":r"\(T_+>0\) and \(3\pi^2T_+\le V\le12\pi^2T_+\)",
      "int(sqrt(Q)-c_beta)^2<=6kappa V and\nint(u-sqrt(Q))^2<=39kappa V":r"\(\int(\sqrt Q-c_\beta)^2\le6\kappa V\) and \(\int(u-\sqrt Q)^2\le39\kappa V\)",
      "alpha=*(a wedge omega_2), beta=*(b wedge omega_3)":r"\(\alpha=*(a\wedge\omega_2)\), \(\beta=*(b\wedge\omega_3)\)",
      "Q_tau*=(1/2+tau_*)S_2-8pi^2(2chi+3tau)":r"\(\mathcal Q_{\tau_*}=(\tfrac12+\tau_*)S_2-8\pi^2(2\chi+3\tau)\)",
      "S_2=s^2V and\n   Q_tau*=0 imply q+tau_*s^2=0":r"\(S_2=s^2V\) and \(\mathcal Q_{\tau_*}=0\) imply \(q+\tau_*s^2=0\)",
      "D=(3/2)S_2+18W_+-72pi^2p and T=A(1-h)":r"\(D=\tfrac32S_2+18W_+-72\pi^2p\) and \(T=A(1-h)\)",
      "|omega|^2=2":r"\(|\omega|^2=2\)",
      "d omega=theta wedge omega":r"\(d\omega=\theta\wedge\omega\)",
      "nabla omega=a tensor omega_2+b tensor omega_3":r"\(\nabla\omega=a\otimes\omega_2+b\otimes\omega_3\)",
      "Q=<W^+ omega,omega>":r"\(Q=\langle W^+\omega,\omega\rangle\)",
      "|d omega|^2=|theta|^2":r"\(|d\omega|^2=|\theta|^2\)",
      "|W^+|^2>=(3/8)Q^2":r"\(|W^+|^2\ge\tfrac38Q^2\)",
      "P=S_2/12+4int|W^+|^2-8pi^2T":r"\(P=S_2/12+4\int|W^+|^2-8\pi^2T\)",
      "int<W^+omega,omega>=T_omega/2-4a/3":r"\(\int\langle W^+\omega,\omega\rangle=T_\omega/2-4a/3\)",
      "|(omega tensor omega)_0|^2=(2/3)|omega|^4":r"\(|(\omega\otimes\omega)_0|^2=\tfrac23|\omega|^4\)",
      "omega=iF_A^+":r"\(\omega=iF_A^+\)",
      "rho=|Phi|^2<=4":r"\(\rho=|\Phi|^2\le4\)",
      "E-4h/(1+h)=4(P-4hV)/[(1+h)R]":r"\(\mathcal E-\frac{4h}{1+h}=\frac{4(P-4hV)}{(1+h)R}\)",
      "Let s_0=(G(h)-e)_+. If delta_->1/8 or s_0>1/16":r"Let \(s_0=(G(h)-e)_+\). If \(\delta_->1/8\) or \(s_0>1/16\)",
      "Also vF_0=[4sqrt(v)+sqrt(2(B-v))]^2-36. Its upper zero is G(h), F_0<=0 for v>=G(h), and elementary square-root comparison gives F_0(h,v)<=30sqrt((G(h)-v)_+) on the displayed compact v-range. Since (G-e_0)_+<=s_0+(49/20)J, ell<=81/64, ell/e>=5/16, and J<=256delta_-^2/49":r"Also \[vF_0=[4\sqrt v+\sqrt{2(B-v)}]^2-36.\] Its upper zero is \(G(h)\), and \(F_0\le0\) for \(v\ge G(h)\). Elementary square-root comparison gives \(F_0(h,v)\le30\sqrt{(G(h)-v)_+}\) on the stated compact range. Since \((G-e_0)_+\le s_0+\tfrac{49}{20}J\), \(\ell\le81/64\), \(\ell/e\ge5/16\), and \(J\le256\delta_-^2/49\)",
      "is: D+_epsilon Phi_hat_0=0, and Phi_hat_0-Phi_0=O(epsilon^2).":r"satisfies \(D_\epsilon^+\widehat\Phi_0=0\) and \(\widehat\Phi_0-\Phi_0=O(\epsilon^2)\).",
      "c_1(L)|_{S^3/Gamma}=+1 or -1 in Z/n":r"\(c_1(L)|_{S^3/\Gamma}=\pm1\) in \(\mathbb Z/n\)",
      "||Phi-Phi_r^0||_{C^k}+||alpha||_{C^k}<=C_k r^2":r"\(\|\Phi-\Phi_r^0\|_{C^k}+\|\alpha\|_{C^k}\le C_kr^2\)",
      "For a spinor Phi in a fixed bounded C^{k,alpha} neighborhood of Phi_0 set":r"For a spinor \(\Phi\) in a fixed bounded \(C^{k,\alpha}\) neighborhood of \(\Phi_0\), set",
      "A(Phi)=O(lambda) and the Lipschitz constant of T is O(lambda), uniformly for small epsilon. A ball of radius C lambda about Phi_0 is mapped to itself for fixed sufficiently large C; for sufficiently small epsilon, T is a contraction.":r"One has \(A(\Phi)=O(\lambda)\), and the Lipschitz constant of \(\mathcal T\) is \(O(\lambda)\), uniformly for small \(\epsilon\). A ball of radius \(C\lambda\) about \(\Phi_0\) is mapped to itself for fixed sufficiently large \(C\); for sufficiently small \(\epsilon\), \(\mathcal T\) is a contraction.",
    }
    supplements={
        "joint_current_prose_math.json": {"sec:joint-matrix", "sec:mixed-current"},
        "endpoint_prose_math.json": {"sec:actual-topological", "sec:endpoint-covariance"},
    }
    for supplement,sections in supplements.items():
        if spec["label"] in sections and (PAPER / supplement).exists():
            prose_math.update(json.loads((PAPER / supplement).read_text()))
    for old,new in prose_math.items():
        pattern=r"\s+".join(re.escape(part) for part in re.split(r"\s+",old))
        body=re.sub(pattern,lambda _:new,body)
    body=body.replace(r"Proposition~\ref{prop:vg-conformal-infimum}","[the conformal infimum](#prop:vg-conformal-infimum)")
    body=body.replace("in the functional-pencil note, Section 5, and Round 21, Section 2", "in [the weighted Hessian estimate](#subsec:proof:weighted-pencil:s5) and [the intrinsic Hessian identity](#subsec:proof:bounded-forms:s2)")
    body=body.replace("`round4_rigidity.md`, Section 2, and rederived in `round21_analytic.md`,\nSection 2", "[the intrinsic Hessian estimate](#subsec:proof:bounded-forms:s2)")
    body=body.replace("`round11_variational.md`,\nSection 2", "[the scalar monopole calculation](#subsec:proof:shear-variational:s2)")
    body=body.replace("[Round 17](round17_product_operator.md), §§2–6", "[the product-operator calculation](#sec:product-operator), in its spectral and perturbation subsections")
    body=body.replace("Crisp--Wiest's explicit genus-two dissection in §4, Figure 2", "Crisp--Wiest's explicit genus-two dissection in their fourth section, Figure 2")
    body=body.replace("0<h->0",r"\(0<h\to0\)")
    if spec["label"]=="sec:endpoint-covariance":
        body=body.replace("[I41, Section 14](20260927_conformal_separation_and_zero_end.md)", "[the torsion projection](#subsec:proof:zero-end-geometry:s14)")
        body=body.replace("In the Clifford conventions of I41", "In the Clifford conventions of [the torsion projection](#subsec:proof:zero-end-geometry:s14)")
    # Plain-text adjoints and Hodge stars must not become Markdown emphasis.
    spans=re.split(r"(\\\[.*?\\\]|\\\(.*?\\\)|\$\$.*?\$\$|(?<!\$)\$(?!\$).*?\$|`[^`]*`)",body,flags=re.S) if not spec.get("raw") else []
    for i in range(0,len(spans),2):
        keep=[]
        def emphasis(m):
            keep.append(m[0]);return "KEEPEMPHASIS"+str(len(keep)-1)+"TOKEN"
        value=re.sub(r"(?<!\*)\*([A-Za-z][A-Za-z ,:;.'’–—-]{0,180})\*(?!\*)",emphasis,spans[i])
        value=re.sub(r"(?<![\\*])\*(?!\*)",r"\\*",value)
        for j,term in enumerate(keep): value=value.replace("KEEPEMPHASIS"+str(j)+"TOKEN",term)
        spans[i]=value
    if spans: body="".join(spans)
    # Resolve multipart predecessor references before local subsection numbering.
    def predecessor(m):
        code,n=m[1],int(m[2])
        if code=="I41": target="linear-coercivity" if n<=5 else "zero-end-geometry"
        elif code=="I40": target="linear-coercivity" if n in (4,5) else "mixed-current"
        else: target="single-parameter" if n<=2 else "actual-core-fit"
        return "[the relevant identity](#sec:"+target+")"
    body=re.sub(r"\b(I40|I41|I51),?\s+[Ss]ection\s+(\d+)(?:\.\d+)*",predecessor,body)
    body=body.replace("The zero-end weak\ngap and the linear small-h lower bound therefore remain open.",
        "The weak zero-end gap remains open. The linear small-h lower bound follows instead from the calibrated-background argument proved above.")
    body=body.replace("as an explanation for Theorem 4's leading term", "as a carrier of a leading topological cost")
    body=body.replace("An averaged bound chi/V controls total L2 energy per volume, not the\nsupremum over centers in (4.5). Without an elliptic metric equation,\nextending Section 4's Euler-density conclusion requires a verified\nbuffered LOCAL smoothing and covering argument. The abstract of Li I\nalone is not used to declare that stronger extension proved.",
        "An averaged Euler-density bound controls total curvature energy per volume, not the supremum over centers in (4.5). This local smoothing argument therefore does not itself establish the Euler-density extension. That extension follows from the separate bounded-Ricci argument in [the endpoint theorem](#sec:bounded-ricci-endpoint).")
    if spec["label"]=="sec:symplectic-chamber":
        body=body.replace("in Section 2", "in [the connected-sum application](#sec:intrinsic-calibration)")
        body=body.replace("satisfies\n(5)", "satisfies the integral gap")
        body=body.replace("and (3)--(5) apply", "and the connected-sum integral-gap theorem applies")
    if spec["label"]=="sec:twisted-supply":
        body=body.replace(r"\(f_0=\max\{\sqrt{\max(-s+\sqrt6|W^+|,3)},(-s)_+/4\}\)",r"\[f_0=\max\{\sqrt{\max(-s+\sqrt6|W^+|,3)},(-s)_+/4\}.\]")
        body=body.replace("Take the smallest closed shear example from round 12:",
            "Take the even-first-Betti example of [the closed shear construction](#sec:shear-global), with base-block genus one, fibre genus two, and \\(f_*=\\operatorname{diag}(H,H)\\), where \\(H=\\left(\\begin{smallmatrix}2&1\\\\1&1\\end{smallmatrix}\\right)\\):")
    if spec["label"]=="sec:cover-obstructions":
        body=body.replace("round 13, equation (2)", "the actual conformal input of [the integral calibration](#sec:intrinsic-calibration)")
        body=body.replace("[round 5](skill/references/rounds/round5_rigidity.md), Section 3", "[the all-class budget comparison](#sec:all-class-ceiling)")
    if spec["label"]=="sec:slow-construction":
        body=re.sub(r"The proposed extension.*?No new smooth near-Einstein family is obtained by repeating that argument\.",
            "[The closed gluing construction](#sec:closed-shear), with zero circle shear, permits arbitrary representations of its geometric free quotient, including noncommuting and pseudo-Anosov monodromy.",body,flags=re.S)
    if spec["label"]=="sec:shear-repair-radius":
        body=body.replace("The accompanying\nprogram also derives all ten first-variation blocks directly from\ncoordinate Christoffel symbols, without importing the variation formula.", "")
        body=body.replace("from `round14_shear.md`", "from [the shear capacity identity](#sec:shear-capacity)")
        body=body.replace("in\n`round14_global.md`", "in [the full-collar construction](#sec:full-collar)")
    if spec["label"]=="sec:integral-limits":
        body=re.sub(r"The same comparison already underlies.*?No new entropy inequality is claimed here\.",
            "We use this classical entropy comparison only in its stated degree and Ricci-volume form.",body,flags=re.S)
    if spec["label"]=="sec:harmonic-projection":
        body=re.sub(r"The metric construction, existence of optimal targets,.*?No global priority claim is made\.","",body,flags=re.S)
        body=body.replace("in\n`round8_multitwist.md`", "in [the multitwist construction](#sec:multitwist)")
    if spec["label"]=="sec:multitwist":
        body=re.sub(r"The metric mechanism is.*?It does not establish Einstein nonexistence\.",
            "The metric mechanism is the slow interpolation of [the fixed-bundle construction](#sec:fixed-bundle-geometry). We compute representation volumes for these same smooth bundles and retain the full Ricci estimate.",body,flags=re.S)
        body=body.replace("the curve-killing proof from `round8_construction.md`", "the curve-killing argument")
    if spec["label"]=="sec:kodaira-controls":
        body=body.replace("The round-9 Bochner/Hodge decomposition", "The Bochner--Hodge decomposition of [the harmonic projection](#sec:harmonic-projection)")
        body=body.replace("the round-9 Hodge/Bochner identities", "the Hodge--Bochner identities of [the harmonic projection](#sec:harmonic-projection)")
        body=body.replace("with notation from `round9_bundle.md`", "with the notation of [the harmonic projection](#sec:harmonic-projection)")
    if spec["label"]=="sec:variable-calibration":
        body=body.replace("in `round21_analytic.md`, Section 2", "in [the bounded-section identity](#subsec:proof:bounded-forms:s2)")
    if spec["label"]=="sec:covering-endpoint":
        body=re.sub(r"the preceding\s+manuscript,\s+Theorem 6", "[the local endpoint estimate](#subsec:proof:zero-end-geometry:s8)",body)
        body=re.sub(r"the preceding\s+manuscript,\s+Section 8", "[the local endpoint estimate](#subsec:proof:zero-end-geometry:s8)",body)
        body=body.replace("Section 13 of the preceding manuscript", "[the scalar-variance argument](#subsec:proof:zero-end-geometry:s13)")
        body=body.replace("the preceding manuscript, Section 11", "[the development averaging argument](#subsec:proof:zero-end-geometry:s11)")
        body=body.replace("in Section 12 there", "in [the regular-fraction argument](#subsec:proof:zero-end-geometry:s12)")
    if spec["label"]=="sec:conformal-flow":
        body=body.replace("preceding proof's quantities", "quantities of [the full curvature variation](#sec:whole-core)")
        body=body.replace("the preceding proof, Section 4.1", "[the retained ordinary-SW identity](#subsec:proof:whole-core:s4.1)")
    if spec["label"]=="sec:harmonic-projection":
        body=body.replace("in the previous round", "in [the multitwist Ricci calculation](#sec:multitwist)")
    if spec["label"]=="sec:twisted-operator":
        body=body.replace(r"\(\ker\nabla^*\nabla=\{\text{parallel sections}\}\)",r"\[\ker\nabla^*\nabla=\{\text{parallel sections}\}.\]")
    if spec["label"]=="sec:early-local-flow":
        body=body.replace(r"$Q_{\rm global}(T)\le e^{C(1+r^{-2})T}Q_{\rm global}(0)$",r"\[Q_{\rm global}(T)\le e^{C(1+r^{-2})T}Q_{\rm global}(0).\]")
    if spec["label"]=="sec:supercritical-bound":
        body=body.replace("the estimate in \\path{20260912.tex}, Proposition~\\texttt{FND:SWgap}, is", "one has")
        body=body.replace("Set $\\mathcal E=\\int|E|^2$", "Here $E=\\Ric^\\circ$. Set $\\mathcal P=\\int|E|^2$")
        body=body.replace(r"\mathcal E",r"\mathcal P")
    if spec["label"]=="sec:early-local-rigidity":
        body=body.replace("the blowup family of Section 1", "the blowup family specified above")
    if spec["label"]=="sec:early-joint-density":
        body=body.replace("The remaining issue is to obtain", "For this local-development approach, the remaining issue is to obtain")
    if spec["label"]=="sec:zero-end-geometry":
        body=body.replace("in Section 8 of the preceding proof", "in [the weighted torsion identities](#subsec:proof:mixed-current:s8)")
        body=body.replace("the preceding proof, Section 8", "[the weighted torsion identities](#subsec:proof:mixed-current:s8)")
        body=body.replace("Section 1 of the preceding proof", "[the rank-two transgression](#subsec:proof:mixed-current:s1)")
        body=body.replace("(8.10) of the preceding proof", "[the weighted derivative identity](#eq:proof:mixed-current:e8.10)")
        body=body.replace("Further results are recorded below as their proofs\nclose, without turning them into an export or a completion claim.", "The following arguments describe the determinant and torsion constraints.")
    if spec["label"]=="sec:covering-endpoint":
        body=body.replace("Theorem 1.1 and\nSection 3, provides", "Theorem 1.1 and its third section, provides")
    if spec["label"]=="sec:bounded-ricci-endpoint":
        body=re.sub(r"\\\[\s*S=m_\\beta(.*?)\\tag\{4\.1\}\s*\\\]",lambda _:r"\[\begin{gathered} S=m_\beta+2\rho^2|P_{\rm spin}|^2,\qquad d=2\rho^2|P_{\rm spin}|^2-|t_\Phi|^2\ge0,\\ \mathcal J=\frac{(S-2m_\beta)^2}{S},\qquad \mathcal A=(\rho-\rho_\beta)^2+\mathcal J+d,\qquad \mathcal R=D^-_{3A}t_\Phi.\end{gathered}\tag{4.1}\]",body,flags=re.S)
    if spec["label"]=="sec:product-operator":
        body=body.replace(r"\text{ below }\sigma}",r"\text{ below }\sigma\}")
    return body

EXTRA_BIB = {}

def markdown_bibliography(spec):
    """Retain named primary references even when editorial lists are omitted."""
    full=(ROOT/spec["path"]).read_text()
    entries={}
    lines=full.splitlines()
    i=0
    while i<len(lines):
        match=re.match(r"^- \[([A-Za-z][A-Za-z0-9-]*)\]\s+(.*)",lines[i])
        if not match:
            i+=1; continue
        name,first=match.groups(); block=[first]; i+=1
        while i<len(lines) and lines[i].startswith("  "):
            block.append(lines[i].strip()); i+=1
        value=subprocess.check_output(["pandoc","--from="+READER,"--to=latex","--wrap=none"],input=" ".join(block),text=True).strip()
        key="source:"+Path(spec["path"]).stem+":"+name
        EXTRA_BIB[key]=value; entries[name]=key
    return entries

def raw_transform(spec):
    full=(ROOT/spec["path"]).read_text()
    prefix="legacy:"+Path(spec["path"]).stem+":"
    for m in re.finditer(r"\\bibitem\{([^{}]+)\}(.*?)(?=\\bibitem|\\end\{thebibliography\})",full,re.S):
        EXTRA_BIB[prefix+m[1]]=m[2].strip()
    body=selected_body(spec)
    body=body.replace(r"\appendix","")
    body=re.sub(r"\\label\{([^{}]+)\}",lambda m:r"\label{"+prefix+m[1]+"}",body)
    body=re.sub(r"\\(ref|eqref|pageref)\{([^{}]+)\}",lambda m:"\\"+m[1]+"{"+prefix+m[2]+"}",body)
    body=re.sub(r"\\cite(\[[^\]]*\])?\{([^{}]+)\}",lambda m:r"\cite"+(m[1] or "")+"{"+",".join(prefix+k.strip() for k in m[2].split(","))+"}",body)
    body=body.replace(r"\subsubsection",r"\paragraph").replace(r"\subsection",r"\subsubsection").replace(r"\section",r"\subsection")
    body=body.replace("The remaining common-time problem", "The conditional common-time extension")
    if re.search(r"[\u4e00-\u9fff]",body): raise ValueError("Untranslated raw source: "+spec["path"])
    return r"\section{"+spec["title"]+"}\n"+r"\label{"+spec["label"]+"}\n"+body,dict(spec)

def transform(spec):
    if spec.get("raw"): return raw_transform(spec)
    body=selected_body(spec)
    bib=markdown_bibliography(spec)
    if spec["label"] == "sec:web-entropy-scope":
        bib.update(BCG="BessonCourtoisGallot1995",
                   BIS="BrunnbauerIshidaSuarezSerrato",
                   Aubry="AubryEntropy", CW="ChenWei")
    tree=json.loads(subprocess.check_output(["pandoc","--from="+READER,"--to=json"],input=body,text=True))
    prefix=spec["label"].replace("sec:", "proof:")
    hnums={}
    # Discover original local section numbers before changing heading levels.
    for block in tree["blocks"]:
        if block["t"]=="Header":
            m=re.match(r"(\d+(?:\.\d+)*)\.?\s",plain(block["c"][2]))
            if m: hnums[m[1]]=prefix+":s"+m[1]
    tags=set(re.findall(r"\\tag\{([^{}]+)\}",body))
    dropped=[]; links=[]
    def walk(node):
        if isinstance(node,list):
            out=[]
            for item in node:
                new=walk(item)
                if isinstance(item,dict) and isinstance(new,list):
                    out.extend(new)
                else:
                    out.append(new)
            return out
        if not isinstance(node,dict): return node
        t,c=node.get("t"),node.get("c")
        if t=="Math":
            value=compile_math_layout(c[1])
            def outer_tag(m):
                tags=re.findall(r"\\tag\{[^{}]*\}",m[1])
                inside=re.sub(r"\\tag\{[^{}]*\}","",m[1])
                return r"\begin{aligned}"+inside+r"\end{aligned}"+"".join(tags)
            value=re.sub(r"\\begin\{aligned\}(.*?)\\end\{aligned\}",outer_tag,value,flags=re.S)
            value=re.sub(r"\\tag\{([^{}]+)\}",lambda m:
                r"\tag{\thesection."+m[1]+r"}\label{"+prefix+":e"+safe(m[1])+"}",value)
            return {"t":t,"c":[c[0],value]}
        if t=="Link":
            label,target=c[1],c[2][0]
            if target.startswith("#sec:"):
                return raw(r"Section~\ref{"+target[1:]+"}")
            if target.startswith("#prop:"):
                return raw(r"Proposition~\ref{"+target[1:]+"}")
            if target.startswith("#subsec:"):
                return raw(r"subsection~\ref{"+target[8:]+"}")
            if target.startswith("#eq:"):
                return raw(r"\eqref{"+target[4:]+"}")
            if target.startswith(("http://","https://")):
                return node
            p=(ROOT/spec["path"]).parent/target.split("#")[0]
            try: rel=str(p.resolve().relative_to(ROOT))
            except ValueError: rel=target
            destination=PATH_LABELS.get(rel)
            links.append({"target":rel,"section":destination})
            if destination:
                return raw(r"Section~\ref{"+destination+"}")
            txt=plain(label)
            if re.search(r"\.md|\.tex|\.py|directive|guidance|research|round\s*\d",txt,re.I):
                return {"t":"Str","c":"the corresponding geometric construction"}
            return walk(label)
        if t=="Str":
            value=c
            m=re.fullmatch(r"\[([A-Za-z][A-Za-z0-9-]*)\]([,.;:]?)",value)
            if m and m[1] in bib:
                return raw(r"\cite{"+bib[m[1]]+"}"+m[2])
            if value in ID_LABELS: return raw(r"Section~\ref{sec:"+ID_LABELS[value]+"}")
            if re.fullmatch(r"O\d+",value): return {"t":"Str","c":{
                "O10":"the weak endpoint problem", "O11":"the balanced extremal problem",
                "O12":"diameter-free realization", "O02":"the fixed-bundle existence problem"}.get(value,"the corresponding existence problem")}
            m=re.fullmatch(r"\(([^()]+)\)([,.;:]?)",value)
            if m and m[1] in tags:
                return raw(r"\eqref{"+prefix+":e"+safe(m[1])+"}"+m[2])
            if re.search(r"\((\d+(?:\.\d+)*)\)",value):
                converted=re.sub(r"\((\d+(?:\.\d+)*)\)",
                    lambda m:r"\eqref{"+prefix+":e"+safe(m[1])+"}" if m[1] in tags else m[0],
                    latex_text(value))
                if r"\eqref{" in converted: return raw(converted)
            return node
        if t=="Code":
            txt=c[1]
            if r"\(" in txt and r"\)" in txt:
                return raw(txt)
            if Path(txt).name in BASENAME_LABELS:
                return raw(r"Section~\ref{"+BASENAME_LABELS[Path(txt).name]+"}")
            if re.search(r"\.md|\.tex|\.py|^[0-9a-f]{7,40}$",txt):
                return {"t":"Str","c":"the corresponding construction"}
            return node
        return {k:walk(v) for k,v in node.items()}
    output=[]; skip_level=None
    for block in tree["blocks"]:
        if block["t"]=="Header":
            level,attr,inlines=block["c"]
            text=plain(inlines)
            if skip_level is not None and level<=skip_level: skip_level=None
            if OMIT_HEAD.search(text):
                skip_level=level; dropped.append(text); continue
            if skip_level is not None: continue
            # A full-source title is replaced by the common section title.
            if level==1 and not re.match(r"\d+[.]?\s",text) and len(output)==0:
                continue
            m=re.match(r"(\d+(?:\.\d+)*)\.?\s+",text)
            number=m[1] if m else None
            clean=re.sub(r"^\d+(?:\.\d+)*\.?\s+", "",text)
            clean=clean.replace("mathematical increment","statement").replace("The question this note resolves","The variational problem")
            depth=2+(number.count(".") if number else max(0,level-2))
            clean_inlines=list(inlines)
            if number and clean_inlines and clean_inlines[0].get("t")=="Str":
                clean_inlines=clean_inlines[1:]
                while clean_inlines and clean_inlines[0].get("t")=="Space": clean_inlines.pop(0)
            block={"t":"Header","c":[min(depth,4),[hnums.get(number,prefix+":"+safe(clean)),[],[]],clean_inlines]}
        if skip_level is not None: continue
        if block["t"] in ("CodeBlock","HorizontalRule"):
            dropped.append(plain(block)[:100]);continue
        if block["t"] in ("Para","Plain") and OMIT_PARA.search(plain(block)):
            dropped.append(plain(block)[:160]);continue
        if block["t"] in ("Para","Plain") and re.search(r"\b\S+\.py\b.*\bchecks?\b",plain(block)):
            dropped.append(plain(block)[:160]);continue
        if block["t"] in ("Para","Plain") and re.match(r"(?:The (?:independent|exact|accompanying) (?:script|checker)|\S+\.py independently)",plain(block)):
            dropped.append(plain(block)[:160]);continue
        if re.search(r"[\u4e00-\u9fff]",plain(block)):
            raise ValueError("Non-English source paragraph: "+spec["path"]+" "+plain(block)[:100])
        output.append(walk(block))
    tree["blocks"]=output;tree["meta"]={}
    tex=subprocess.check_output(["pandoc","--from=json","--to=latex","--wrap=none"],input=json.dumps(tree),text=True)
    tex=compile_table_layout(tex)
    # Protect complete external links while renumbering local references.
    protected=[]
    def shield(m):
        protected.append(m[0]);return "PROTECTEDLINKTOKEN"+str(len(protected)-1)+"END"
    tex=re.sub(r"\\href\{[^{}]*\}\{(?:[^{}]|\{[^{}]*\})*\}",shield,tex)
    # Make local section references unambiguous in the assembled paper.
    for num,destination in sorted(hnums.items(),key=lambda x:-len(x[0])):
        tex=re.sub(r"(?<![A-Za-z])(?:Section|section|§)\s*"+re.escape(num)+r"(?!\d|\.\d)",
                   lambda _:r"subsection~\ref{"+destination+"}",tex)
    def section_range(m):
        left,right=m[1],m[2]
        if left not in hnums or right not in hnums: return m[0]
        return r"subsections~\ref{"+hnums[left]+r"}--\ref{"+hnums[right]+"}"
    tex=re.sub(r"Sections\s+(\d+(?:\.\d+)*)(?:--|–)(\d+(?:\.\d+)*)",section_range,tex)
    for code,dest in ID_LABELS.items():
        tex=re.sub(r"\b"+code+r"\b",lambda _:r"Section~\ref{sec:"+dest+"}",tex)
    tex=re.sub(r"\bO10\b", "the weak endpoint problem",tex)
    tex=re.sub(r"\bO11\b", "the balanced extremal problem",tex)
    tex=re.sub(r"\bX0?6\b", "the transverse Weyl-payment example",tex)
    tex=re.sub(r"\bX10\b", "the competitive signed-mass example",tex)
    tex=tex.replace("in this project", "here")
    tex=re.sub(r"\bthe project\b","the present setting",tex)
    tex=tex.replace("in this note", "here").replace("in this research package", "in this paper")
    tex=tex.replace("not a new theorem of this round", "a classical input")
    tex=tex.replace("a classical input, a classical input", "a classical input")
    tex=tex.replace("LeBrun's paper verified here", "LeBrun's preprint")
    tex=tex.replace("The full contraction in the checker gives", "Direct contraction gives")
    tex=tex.replace("; the pointwise contraction is independently checked in the accompanying program", "")
    tex=tex.replace(", not a new Round21 extension", "")
    tex=tex.replace("The exact sign check is in the accompanying program. ", "")
    tex=tex.replace("the supplied web certificate", "joint sign-correlation bound")
    tex=tex.replace("web mixed-current refinement", "mixed-current estimate")
    tex=tex.replace("The web note's exact expansion is", "The exact expansion is")
    tex=tex.replace("the web note observes", "one has")
    tex=tex.replace("The web note supplies a further equation, not an ordinary new monopole.", "The same fields satisfy an additional curvature equation, distinct from the ordinary monopole equation.")
    tex=tex.replace("in the supplied brief", "for the scalar monopole identity")
    tex=tex.replace("not the form rescaling constant denoted similarly in some earlier manuscripts", "distinct from the constant used to rescale two-forms")
    tex=tex.replace("; no literature-priority claim is made for this assembly", "")
    tex=re.sub(r"The moduli-energy obstruction itself was already proved in.*?They are retained below as inputs, with their conventions made explicit\.", "The moduli-energy and submersion identities are derived below in a fixed normalization.", tex, flags=re.S)
    tex=tex.replace(r"This is the \texttt{BUN:WP-signature} calculation in an explicit real-tensor normalization, not a new signature or energy formula.", "We use the following real-tensor normalization for the moduli-energy calculation.")
    tex=tex.replace(r"These specialize the earlier \texttt{SUB:blocks} and \texttt{SUB:vv-integrable} formulas.", "These are the vertical and mixed submersion identities in the present normalization.")
    tex=tex.replace(r"The earlier \texttt{SUB:basic} theorem already treats every negative Einstein surface submersion with basic fibre mean curvature, including minimal fibres, without imposing intrinsic fibre curvature. The following is its narrower corollary, not a new classification. Its direct proof illustrates the role of the same vertical and mixed blocks.", "The following exact rigidity consequence for minimal hyperbolic-fibre submersions follows directly from the same vertical and mixed blocks.")
    tex=tex.replace("rather than a construction or a literature-priority claim", "within the stated geometric class")
    tex=tex.replace("in the supplied report", "below")
    tex=tex.replace("Round18", r"Section~\ref{sec:periods}")
    tex=re.sub(r"(?:No (?:worldwide-|exhaustive |literature-)?priority claim is made|no priority claim is made)\.", "", tex)
    tex=re.sub(r"The accompanying checker verifies.*?not claims certified by finite computation\.", "", tex, flags=re.S)
    tex=re.sub(r"The contribution here is a completed consequence.*?The classical ingredients and the gap have been kept separate\.", "", tex, flags=re.S)
    tex=tex.replace("The calculation below supplies a checkable control family for the present harmonic/Hodge functional; ", "The following calculation gives an exact control family for the harmonic/Hodge functional.")
    tex=re.sub(r"The finite checker validates.*?worldwide originality\.", "", tex, flags=re.S)
    tex=re.sub(r"The checker independently recomputes all sixteen entries directly from.*?retaining the moving-frame quadratic terms\.", "The curvature calculation retains the moving-frame quadratic terms.", tex, flags=re.S)
    tex=tex.replace("The contribution here is a completed consequence and a decisive test of the proposed extension, not a new general Einstein obstruction. The classical ingredients and the gap have been kept separate. ", "")
    tex=tex.replace("The unqualified statement of Theorem 3.3 in the verified preprint includes this corner, but its appeal to the Hitchin--Thorpe inequality does not exclude these equality cases. We therefore do \\textbf{not} claim an unqualified subsumption of that literal zero-corner wording, nor infer an exception-free statement for a separately unverified published version. The conclusions established here are: the positive-budget integral strengthening with the stated gauge input; the classical negative-\\(T_M\\) exclusion; and an explicit reservation of the Ricci-flat zero corner.", "Thus the positive-budget integral strengthening and the negative-\\(T_M\\) exclusion must be distinguished from the Ricci-flat zero corner.")
    tex=tex.replace("Rounds 15--16",r"Sections~\ref{sec:product-calibration}--\ref{sec:product-endpoint}")
    tex=tex.replace("Rounds 11--12",r"Sections~\ref{sec:closed-shear}--\ref{sec:shear-global}")
    tex=tex.replace("Rounds 11--15",r"Sections~\ref{sec:closed-shear}, \ref{sec:virtual-nonkahler}, and \ref{sec:product-calibration}")
    tex=tex.replace("; exhaustive publication-priority verification is not asserted", "")
    tex=tex.replace("The report's higher slow-spectrum estimate", "The higher slow-spectrum estimate")
    tex=tex.replace("Relation to the research program and classical theory", "Relation to classical Weyl structure")
    tex=tex.replace("Relation to the research programme and sources", "Geometric implications")
    tex=tex.replace("Relation to the first scientific line", "Relation to integral rigidity")
    tex=tex.replace("Consequence for the research program", "The pointwise and integral distinction")
    tex=tex.replace("Consequence for the first research line", "Scalar coherence and integral rigidity")
    tex=tex.replace("What this changes in the research problem", "Spectral and nonlinear consequences")
    tex=tex.replace("What the monopole proof actually requires", "Conformal solvability and the connection-energy budget")
    tex=tex.replace("What this settles, and what it does not", "Consequences for period compactness")
    tex=tex.replace("Why all free-quotient examples were already included", "Free-quotient monodromy and closed gluing")
    tex=re.sub(r"The accompanying symbolic checker verifies[^.]*\.","",tex)
    tex=tex.replace("Scope and research consequence", "Geometric scope")
    tex=re.sub(r"\bround 21\b","the bounded-form argument",tex,flags=re.I)
    round_targets={2:"analytic-limitations",3:"intrinsic-calibration",4:"intrinsic-calibration",5:"intrinsic-calibration",9:"harmonic-projection",10:"kodaira-controls",11:"closed-shear",12:"shear-global",13:"intrinsic-calibration",14:"full-collar",15:"product-calibration",16:"product-endpoint",17:"product-propagation",18:"periods",19:"all-class-ceiling",20:"positive-planes",21:"bounded-forms"}
    if spec["label"]=="sec:shear-capacity": round_targets[13]="shear-capacity"
    if spec["label"] in {"sec:twisted-operator","sec:slow-construction"}: round_targets[17]="product-operator"
    tex=re.sub(r"\b[Rr]ound[- ](\d+)\b",lambda m:r"Section~\ref{sec:"+round_targets.get(int(m[1]),"intrinsic-calibration")+"}",tex)
    tex=re.sub(r"\bthe inherited\b","the",tex)
    tex=tex.replace("QED.",r"\hfill\(\square\)")
    if spec["label"] in ("sec:relative-cells","sec:coupled-filling","sec:signed-selection","sec:caps","sec:surgery-stability"):
        tex=re.sub(r"(Yamabe (?:replacement|reduction)[^.]{0,150})Section~\\ref\{sec:linear-coercivity\}",
                   lambda m:m[1]+r"Proposition~\ref{prop:vg-conformal-infimum}",tex)
    for i,link in enumerate(protected):
        tex=tex.replace("PROTECTEDLINKTOKEN"+str(i)+"END",link)
    tex=tex.replace("LeBrun's paper verified here", "LeBrun's preprint")
    if spec["label"]=="sec:signed-selection":
        for number in ("1.1","2.1"):
            tex=tex.replace(r"Section~\ref{sec:relative-cells} \eqref{proof:signed-selection:e"+number+"}",
                r"Section~\ref{sec:relative-cells} \eqref{proof:relative-cells:e"+number+"}")
    if spec["label"]=="sec:shear-variational":
        tex=tex.replace(r"constructed in subsection~\ref{proof:shear-variational:s6}",r"constructed in subsection~\ref{proof:closed-shear:s6}")
    if spec["label"]=="sec:bounded-ricci-endpoint":
        tex=tex.replace(r"Section 6 of the Section~\ref{sec:bf-linear}",r"subsection~\ref{proof:zero-end-geometry:s6}")
    if spec["label"]=="sec:whole-core":
        tex=tex.replace(r"exactly as verified in Section~\ref{sec:directional-variations}",r"as in subsection~\ref{proof:bounded-ricci-endpoint:s3.1}")
    if spec["label"]=="sec:periods":
        tex=tex.replace(r"\eqref{proof:periods:e8} of Section~\ref{sec:product-propagation}",r"\eqref{proof:product-propagation:e8}")
    if spec["label"]=="sec:single-parameter":
        tex=tex.replace(r"Section~\ref{sec:linear-coercivity} (8.10)",r"\eqref{proof:mixed-current:e8.10}")
        tex=tex.replace(r"Section~\ref{sec:whole-core} Section 4.1",r"subsection~\ref{proof:whole-core:s4.1}")
        tex=tex.replace(r"Section~\ref{sec:weighted-pencil} Section 5",r"subsection~\ref{proof:weighted-pencil:s5}")
        tex=tex.replace("that representative in Section 1",r"that representative in subsection~\ref{proof:single-parameter:s1}")
    if spec["label"]=="sec:intrinsic-calibration":
        tex=tex.replace("proved in §2",r"proved in subsection~\ref{proof:intrinsic-calibration:s2}")
    if spec["label"]=="sec:endpoint-covariance":
        tex=tex.replace(r"the Section~\ref{sec:bf-linear}",r"subsection~\ref{proof:zero-end-geometry:s14}")
    if spec["label"]=="sec:torsion-prolongation":
        tex=tex.replace(r"Section~\ref{sec:linear-coercivity} (14.2)",r"\eqref{proof:zero-end-geometry:e14.2}")
    if spec["label"]=="sec:quartic-flux":
        tex=tex.replace(r"proved in Section~\ref{sec:linear-coercivity}",r"proved in \eqref{proof:zero-end-geometry:e7.3}")
    if spec["label"]=="sec:covering-endpoint":
        tex=tex.replace("(5.4)",r"\eqref{eq:vg-P-theta}")
    if spec["label"]=="sec:chern-boundary":
        # These are subsections of other source files, not local subsection 4.
        for old, new in (
            (r"subsection~\ref{proof:chern-boundary:s4} of the Section~\ref{sec:gauge-ke}",
             r"subsection~\ref{proof:gauge-ke:s4}"),
            (r"subsection~\ref{proof:chern-boundary:s4} of Section~\ref{sec:compact-realization}",
             r"subsection~\ref{proof:compact-realization:s4}"),
        ):
            if tex.count(old) != 1:
                raise ValueError("Chern-boundary external subsection reference changed")
            tex=tex.replace(old,new)
    head=r"\section{"+latex_text(spec["title"])+"}\n"+r"\label{"+spec["label"]+"}\n"
    if spec["label"]=="sec:single-parameter":
        head+=(PAPER/"sections/single_parameter_statement.tex").read_text()+"\n"
    return head+tex, {**spec,"removed_editorial_blocks":dropped,"links":links}

def main():
    parts=[(PAPER/"frontmatter.tex").read_text()]
    records=[]
    for spec in PLAN:
        if spec.get("appendix"):
            parts.append(r"\appendix\renewcommand{\thesection}{\AlphAlph{\value{section}}}"+"\n")
        if "part" in spec:
            parts.append(r"\clearpage\part{"+spec["part"]+"}\n")
        elif "tex" in spec:
            path=PAPER/spec["tex"]
            if not path.exists(): raise FileNotFoundError(path)
            parts.append(path.read_text()+"\n")
        else:
            tex,record=transform(spec);parts.append(tex);records.append(record)
    references=(PAPER/"references.tex").read_text()
    used=set(k.strip() for m in re.finditer(r"\\cite(?:\[[^\]]*\])?\{([^{}]+)\}","\n".join(parts)) for k in m[1].split(","))
    additions="\n".join(r"\bibitem{"+key+"} "+value for key,value in EXTRA_BIB.items() if key in used)
    references=references.replace(r"\end{thebibliography}",additions+"\n"+r"\end{thebibliography}")
    parts.append(references)
    manuscript="\n\n".join(parts)
    # A reference to a subsection of a named preceding section is external
    # to the imported fragment. Resolve it in that section, not locally.
    labels=set(re.findall(r"\\label\{([^{}]+)\}",manuscript))
    def external_subsection(m):
        section,number=m[1],m[2]
        target="proof:"+section+":s"+number
        return r"subsection~\ref{"+target+"}" if target in labels else m[0]
    manuscript=re.sub(
        r"Section~\\ref\{sec:([^{}]+)\},?\s+(?:subsection~\\ref\{proof:[^{}]+:s(\d+(?:\.\d+)*)\})",
        external_subsection,manuscript)
    manuscript=re.sub(
        r"Section~\\ref\{sec:([^{}]+)\},?\s+Section\s+(\d+(?:\.\d+)*)(?!\d|\.\d)",
        external_subsection,manuscript)
    def external_range(m):
        section,left,right=m[1],m[2],m[3]
        a,b="proof:"+section+":s"+left,"proof:"+section+":s"+right
        if a not in labels or b not in labels: return m[0]
        return r"subsections~\ref{"+a+r"}--\ref{"+b+"}"
    manuscript=re.sub(
        r"Section~\\ref\{sec:([^{}]+)\},?\s+subsections~\\ref\{proof:[^{}]+:s(\d+(?:\.\d+)*)\}--\\ref\{proof:[^{}]+:s(\d+(?:\.\d+)*)\}",
        external_range,manuscript)
    manuscript=re.sub(
        r"Section~\\ref\{sec:([^{}]+)\},?\s+Sections\s+(\d+(?:\.\d+)*)--(\d+(?:\.\d+)*)(?!\d|\.\d)",
        external_range,manuscript)
    def external_equation(m):
        target="proof:"+m[1]+":e"+m[2]
        return r"\eqref{"+target+"}" if target in labels else m[0]
    manuscript=re.sub(
        r"Section~\\ref\{sec:([^{}]+)\},?\s+(?:formula|equation)\s+\\eqref\{proof:[^{}]+:e([^{}]+)\}",
        external_equation,manuscript)
    if re.search(r"[\u4e00-\u9fff]",manuscript): raise ValueError("Chinese in English manuscript")
    manuscript="\n".join(line.rstrip() for line in manuscript.splitlines())+"\n"
    (PAPER/"Integral_Einstein_Rigidity.tex").write_text(manuscript)
    (PAPER/"source_selection.json").write_text(json.dumps({"sources":records},indent=2)+"\n")
    print(f"Standalone manuscript: {len(manuscript):,} characters; {len(records)} proof selections")

if __name__=="__main__": main()
