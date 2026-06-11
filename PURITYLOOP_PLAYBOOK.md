# PurityLoop AI — Success Metrics Playbook

## Strategy, Rationale, and Academic Citations

**Project:** PurityLoop AI | Sunway University Capstone AY2025/26
**Supervisor:** Dr. Narishah Mohamed Salleh | **ML R&D:** Talvin
**Written:** 2026-06-11 | **Scope:** Image classification for waste sorting (CV model only)

---

## WHAT THIS DOCUMENT IS

This playbook answers one question: **how, exactly, do we build an AI that correctly identifies waste on a conveyor belt — and how do we prove it works?**

Every section explains the strategy in plain English first, then the technical method, then the academic evidence behind the decision. Nothing is assumed. If a term needs explaining, it is explained.

This is not a list of steps to follow blindly. It is a reasoning document — every decision has a "why" and every target has evidence behind it.

---

## PART 1 — THE PROBLEM WE ARE SOLVING

### What PurityLoop AI actually does

Imagine a recycling facility with a conveyor belt moving hundreds of items per minute — plastic bottles, aluminium cans, cardboard boxes, batteries, food waste, glass jars. A worker standing at the belt must decide what each item is and where it should go. That worker gets tired, misses things, and cannot process items fast enough when the belt speeds up.

PurityLoop AI replaces that decision with a camera and an algorithm. A camera mounted above the conveyor takes a photo. The AI looks at the photo and answers: *what is this object, and where should it go?*

The AI must do this correctly, quickly, and for 9 different types of waste: plastic, paper, cardboard, metal, glass, textile, food/organic waste, battery, and general trash.

### Why this is harder than it sounds

Three specific problems make this genuinely difficult:

**Problem 1 — Things look the same.** A 9-volt battery and an aluminium drink can look almost identical to a camera: same metallic silver colour, similar cylindrical shape, similar size. The difference is what is inside — and a camera cannot see inside. Getting this wrong has serious consequences: a battery mixed into a metal recycling bale can cause a fire at the smelting facility.

**Problem 2 — Items pile on top of each other.** On a real conveyor belt, items are not neatly separated. A plastic bag might be sitting on top of a cardboard box. A broken glass bottle might overlap with a food container. The AI must identify multiple overlapping items in a single photo, not just one item per photo.

**Problem 3 — The data is uneven.** Our training dataset contains 139,909 food/organic waste photos but only 12,814 battery photos. If we train the AI on this raw imbalance, it learns a shortcut: "when in doubt, guess food waste." That produces a high accuracy score on paper — because most items really are food waste — but the AI is essentially useless for everything else. We have to correct for this deliberately.

### What success looks like

Success is not "the AI works." Success is a set of specific, measurable targets that must all be achieved at the same time:

| What we measure | Target | Why this number |
|-----------------|--------|----------------|
| Overall detection accuracy (mAP@0.5) | ≥ 85% | Peer-reviewed benchmark for YOLOv8 on waste classification (Ding et al., 2024; Midigudla et al., 2025) |
| Precise boundary accuracy (mAP@0.5:0.95) | ≥ 70% | Validates the AI can locate items precisely, not just name them |
| Precision — when AI says "recyclable", how often is it right? | ≥ 85% | Prevents hazardous items from entering the recycling stream |
| Recall — of all recyclable items, how many did AI catch? | ≥ 80% | Prevents too many good items being wasted |
| Battery accuracy (tracked separately) | ≥ 80% | Cannot be hidden in an average — this is a safety-critical class |
| Processing speed | ≥ 25 frames per second | Must keep up with a moving conveyor belt in real time |
| Performance on photos AI has never seen | Drop ≤ 10% | Proves the AI learned, not just memorised |
| Human labellers agreeing on the same photo | ≥ 85% | Ensures training data is internally consistent |

> **All of these must be achieved simultaneously.** A model that scores 95% overall but only 40% on batteries has failed — the average hides the most dangerous failure mode.

---

## PART 2 — THE OVERALL STRATEGY

### The three-layer strategy

Achieving these targets requires three things working together, not just training a model:

**Layer 1 — Clean, accurate training data.** The AI can only learn from what it is shown. If the training photos are mislabelled, blurry, duplicated, or dominated by one category, the AI learns the wrong things. The first five phases of this project exist purely to ensure the training data is trustworthy before any learning begins.

**Layer 2 — A model built to handle this specific problem.** Not every AI model is suitable for every problem. We chose a specific model (YOLOv8s-seg) for specific reasons: it can identify multiple objects in one photo simultaneously, it trains and iterates faster than larger variants, and published research on the same architecture achieves the accuracy targets we need on waste classification problems. If the small variant cannot reach our target after full tuning, we upgrade to the medium variant (YOLOv8m-seg).

**Layer 3 — A human safety net that never disappears.** No AI model is 100% accurate. The strategy for handling the remaining uncertainty is not to pretend it does not exist — it is to build a system where uncertain decisions are automatically routed to a human operator for review. Those human decisions are then used to make the AI smarter over time.

These three layers are not sequential. They interact. Better training data raises the accuracy ceiling. Better accuracy means fewer uncertain decisions that need human review. Fewer human reviews means faster throughput. The system is designed to improve continuously, not to reach a fixed level and stop.

### Why we use a pre-trained model instead of building from scratch

Training a visual recognition AI from scratch requires millions of photos and months of computing time. We do not have either. Instead, we start from a model that has already been trained to recognise 80 common objects — cars, chairs, people, animals — using 330,000 images (the COCO dataset). This model has already learned how to see: how to detect edges, textures, shapes, and spatial relationships.

We then take this general-purpose vision model and specialise it on our 9 waste categories. The model's visual foundation remains intact; we only adjust the final decision-making layers to produce waste-specific outputs. This approach — called transfer learning — requires far fewer training images and far less computing time, while producing accuracy levels that are consistent with purpose-built waste classification systems in peer-reviewed literature (Jaikumar et al., 2020; White et al., 2020).

---

## PART 3 — THE TEAM WORKFLOW: HOW 3 PEOPLE BUILD 1 MODEL

### One model. Three class groups. Three team members

The end product is a single YOLOv8s-seg model that recognises all 9 waste classes. It is trained once on the full 9-class merged dataset and deployed as one file (`best.pt`).

The reason the dataset was split into three class groups is not about the final model architecture — it is about how three team members divide the work of labelling, quality checking, and diagnostic training before everything is merged. Think of it like three people each writing three chapters of the same book. The chapters exist separately during the writing process. The final published book is one document.

**The three class groups and who owns them:**

| Group | Classes | Zip file | Owned by |
|-------|---------|----------|----------|
| Group 1 | Plastic · Paper · Cardboard | `group1_plastic_paper_cardboard.zip` | Naomi |
| Group 2 | Food/Organic · Battery · General Trash | `group2_food_battery_trash.zip` | Chris |
| Group 3 | Metal · Glass · Textile | `group3_metal_glass_textile.zip` | Talvin |

**Why split the work this way:**

**Reason 1 — Manageable labelling load.**
Labelling 227,490 images as one person is impossible within the project timeline. Splitting by class group gives each person a focused set of categories to annotate with deep familiarity. Naomi knows plastic, paper, and cardboard thoroughly. Chris knows batteries. Talvin knows metal and glass. Each person becomes an expert on their classes, which produces higher labelling accuracy than if everyone tried to label all 9 classes simultaneously.

**Reason 2 — Parallel diagnostic training (Phase 3).**
Each person trains a short diagnostic model on their own labelled slice only. This is a quality control step — not the final model. The diagnostic run reveals labelling mistakes through the confusion matrix before those mistakes contaminate the full merged dataset. Three people training three smaller models simultaneously is also faster than one person waiting for a single large diagnostic run.

**Reason 3 — Battery/metal boundary ownership.**
Battery (Chris, Group 2) and metal (Talvin, Group 3) are visually similar and represent the most dangerous confusion in the project. By giving battery and metal to separate people with separate labelling guides for their respective classes, the boundary decision is explicit and owned. Chris decides what counts as a battery. Talvin decides what counts as metal. Any dispute at the Phase 4 cross-audit is resolved together. This is cleaner than both working on both classes simultaneously.

**How the workflow converges into one model:**

```text
Naomi labels Group 1             Chris labels Group 2             Talvin labels Group 3
(plastic / paper / cardboard)    (food / battery / trash)         (metal / glass / textile)
         │                                │                                │
Phase 3: each person trains a SHORT diagnostic model on their own slice only
         │                                │                                │
Phase 4: cross-team audit — all three sets of labels reviewed together
         │                                │                                │
Phase 5: automated label error scan across all three sets
         │                                │                                │
         └────────────── Phase 6: ALL THREE SETS MERGED ──────────────────┘
                                          │
                    One combined 9-class dataset — Phase 6 applies a
                    5,000/class hard cap → ~45,000 images, 80/20 split
                    (raw dataset: 227,426 images, unbalanced — cap not yet applied)
                                          │
                        Phase 7: ONE model trained on all 9 classes
                                          │
                        Phase 8: ONE model tuned on all 9 classes
                                          │
                      Phase 9: ONE model tested on quarantine set
                                          │
                              Single deployed model — best.pt
                         Detects all 9 classes in every camera frame
```

**What this means for the total number of training runs:**

| Training event | Number of runs | Notes |
|---------------|---------------|-------|
| Phase 3 diagnostic runs | 3 | One per person, on their own slice only. Temporary — for label quality checking |
| Phase 7 baseline (full 9-class) | 1 | First real training run on the merged dataset |
| Phase 8 tuning experiments | 4 | One parameter changed per run; all 4 applied to the same 9-class model |
| Phase 9 quarantine test | 1 | Final validation before deployment |
| **Total training runs** | **9 minimum** | Phase 10 adds more if Phase 9 fails |

The 3 group zips serve Phase 3 only. From Phase 6 onward, there is one dataset and one model.

---

## PART 4 — THE 10-PHASE PIPELINE

### Why the pipeline has exactly 10 phases

The structure is not arbitrary. It is derived from two established frameworks that define what a rigorous, defensible model-building process looks like.

#### Framework 1 — CRISP-DM (Cross-Industry Standard Process for Data Mining)

CRISP-DM is the industry standard for building data-driven systems. It defines six stages: Business Understanding, Data Understanding, Data Preparation, Modelling, Evaluation, and Deployment (Shearer, 2000). Every one of our 10 phases belongs to one of these six stages. No stage is skipped.

#### Framework 2 — DMAIC (Lean Six Sigma)

DMAIC is a quality management framework: Define, Measure, Analyse, Improve, Control. It is designed to ensure that improvements are measured against baselines, not just claimed. Dr. Narishah's research context directly references this framework. Our pipeline maps to it explicitly.

**Why 10 phases and not 6 (CRISP-DM) or 5 (DMAIC):**

CRISP-DM was designed for tabular data — spreadsheets and databases — where labels come from systems that already recorded the truth. When someone's bank transaction says "£45.00 at a supermarket," the label is exact. No human had to draw an outline around the supermarket receipt and decide whether it was a food purchase or a household item.

In computer vision with human annotation, labels do not come from systems — they come from people. Three people drawing outlines around the same photo of a crushed battery will produce three slightly different outlines and may disagree on whether it is a battery or a metal can. CRISP-DM has no phase for "check that three human annotators agree before training." We added phases 3, 4, and 5 specifically to address this gap.

Similarly, Phase 10 (active learning retrain) is a continuous improvement loop that extends past CRISP-DM's "Deployment" endpoint. In CRISP-DM, deployment is the final stage. In a real recycling facility, deployment is the beginning of an ongoing feedback process — the AI must keep improving from real operator corrections after it is running. Phase 10 is the engineering mechanism that makes this possible.

**How the 10 phases map to both frameworks:**

| Phase | Our name | CRISP-DM stage | DMAIC stage |
|-------|----------|---------------|-------------|
| 1 | Data Cleaning | Data Preparation | Measure |
| 2 | Labelling | Data Preparation | Measure |
| 3 | Individual Diagnostic Training | Data Understanding | Measure |
| 4 | Cross-Team Human Audit | Data Preparation (validation) | Measure |
| 5 | Automated Label Error Scan | Data Preparation (validation) | Measure |
| 6 | Data Merge, Balancing, Split | Data Preparation (final) | Analyse |
| 7 | First Full Training Run | Modelling — baseline | Measure (baseline) |
| 8 | Hyperparameter Tuning | Modelling — optimise | Improve |
| 9 | Generalisation Test | Evaluation | Control |
| 10 | Active Learning Retrain | Deployment — continuous | Control (ongoing) |

The 5 data preparation phases (1–5) are not redundant — they address different layers of the same problem. Phase 1 addresses photo quality. Phase 2 addresses label creation. Phase 3 addresses per-person label consistency. Phase 4 addresses cross-person label consistency. Phase 5 addresses systematic errors that survived human review. Each catches a class of problem the previous phase cannot. Removing any one of them leaves a known gap in the quality chain.

**Citations:**

- Shearer, C. (2000). The CRISP-DM model: The new blueprint for data mining. *Journal of Data Warehousing*, *5*(4), 13–22. *(Standard CRISP-DM reference)*
- Wirth, R., & Hipp, J. (2000). CRISP-DM: Towards a standard process model for data mining. *Proceedings of the 4th International Conference on the Practical Applications of Knowledge Discovery and Data Mining*, 29–39. *(Full CRISP-DM framework paper)*
- Mosqueira-Rey, E., et al. (2023). Human-in-the-loop machine learning: A state of the art. *Artificial Intelligence Review*, *56*(4), 3005–3054. <https://doi.org/10.1007/s10462-022-10246-w> *(HITL justification for phases 3–5)*

---

The pipeline has three stages:

- **Phases 1–5:** Prepare clean, trustworthy training data
- **Phases 6–8:** Train and systematically improve the model
- **Phases 9–10:** Test on genuinely unseen photos before deployment

Each phase has a defined pass/fail gate. Failing a gate means going back to fix the problem — not proceeding with known errors.

---

### PHASE 1 — Data Cleaning: Making Sure the Training Photos Are Trustworthy

**The plain English version:**

Before the AI sees a single photo, we need to make sure the photos themselves are good. This means three things: no duplicates, no blurry images, and no corrupted files.

**Why duplicates are a problem:**

Imagine teaching a student to identify animals by showing them 1,000 flashcards. If the same photo of a cat appears 50 times in the deck and only once in the test, the student learns to recognise that specific photo of that specific cat — not cats in general. The same thing happens with AI. A duplicate image appearing many times in training inflates the score on validation without improving real-world performance. The AI has memorised a photo, not learned a concept.

We remove duplicates using a technique called perceptual hashing. It works like a fingerprint for photos: instead of comparing every pixel, it creates a short numerical code that captures the visual essence of the image. Two photos with nearly identical codes are near-duplicates and one is discarded. This handles both exact copies and slightly edited versions of the same photo (Assoesoedarso et al., 2024).

**Why blurry images are a problem:**

A blurry photo of a battery and a blurry photo of a metal can look identical. Training the AI on blurry photos teaches it to make decisions based on noise rather than real visual information. We discard any image where a sharpness score falls below the minimum threshold — these photos would mislead the AI rather than teach it.

**Why this serves the generalisation target:**

The generalisation gap (≤ 10%) is the most important proof that the AI actually learned something. Removing duplicates ensures the validation test is genuinely testing new knowledge, not memory. If duplicates were present, the gap would artificially appear small — masking overfitting.

**Citation:** Assoesoedarso, G., Widjaja, D., & Iskandar, A. A. (2024). Comparative evaluation of perceptual hashing and deep embedding methods for robust and efficient image deduplication. *Electronics*, *15*(7), 1493. <https://doi.org/10.3390/electronics15071493>

---

### PHASE 2 — Labelling: Teaching the AI What to Call Each Item

**The plain English version:**

An AI cannot learn from a pile of photos. It needs to be told what is in each photo. This process is called labelling or annotation: a human draws an outline around each object in the photo and assigns it a category name. The AI learns by studying thousands of these labelled examples.

**How we label efficiently:**

Drawing precise outlines around 227,000 photos by hand would take months. We use a tool called SAM (Segment Anything Model) to speed this up. SAM is itself an AI — but trained for a different task. When a human clicks on an object in a photo, SAM automatically draws the outline. The human then verifies the outline is correct and assigns the category. What would take hours is reduced to minutes per image.

**The most important labelling rule:**

A dirty, contaminated item is still labelled by what it is made of — not by how clean it is. A plastic bottle covered in food residue is still labelled "plastic," not "general trash." This is critical because the AI's job is to identify material type. Whether the item is clean enough to recycle is a separate decision made at the system level, not at the labelling level. If we labelled by cleanliness, the AI would learn to sort by condition, not by material — the opposite of what the facility needs.

**The battery boundary:**

The single hardest labelling decision in the entire project is distinguishing a 9-volt battery from a small aluminium container. Both are metallic, cylindrical, and approximately the same size. The labelling guide defines this boundary explicitly so every team member draws the same distinction. Inconsistency at this step propagates into a model that cannot reliably tell them apart — which is a safety risk.

**Citation:** Sakr, G. E., Mokbel, M. F., & Darwish, A. I. (2022). Computer vision for solid waste sorting: A critical review of academic research. *Waste Management*, *142*, 29–43. <https://doi.org/10.1016/j.wasman.2022.02.009>

---

### PHASE 3 — Individual Diagnostic Training: Using the AI to Find Labelling Mistakes

**The plain English version:**

After each team member labels their own set of photos, we run a short training session on each person's labels separately. We are not trying to build the final model here. We are using the AI as a quality control instrument to find labelling mistakes before they contaminate the merged dataset.

> ⚠️ **Critical distinction — Phase 3 metrics are NOT the same as production metrics.**
>
> The individual diagnostic models are 3-class models. The production model is a 9-class model. These two problems are fundamentally different in difficulty and the same success metric numbers mean different things in each context. Do not use Phase 3 results to predict or validate production performance.
>
> | | Individual diagnostic model (Phase 3) | Production model (Phases 7–9) |
> |-|--------------------------------------|-------------------------------|
> | Classes | 3 | 9 |
> | Random guess floor | 33.3% | 11.1% |
> | Purpose | Detect label errors in one person's slice | Deploy on a real conveyor belt |
> | Pass gate | AP ≥ 0.60 per class | mAP@0.5 ≥ 0.85 across all 9 classes |
> | Battery AP meaning | Battery vs food/trash only — **metal is absent** | Battery vs all 8 other classes including metal |
> | Valid for production claim? | ❌ No | ✅ Yes |
>
> **The most important consequence:** Chris's battery model will appear to classify batteries well — because it has never seen a metal can. The hardest battery/metal confusion does not exist in the diagnostic model. A battery AP of 0.85 in Phase 3 does **not** mean battery AP will be 0.85 in the production model. The production model must be evaluated on all 9 classes together before any claim about battery accuracy can be made.

**How Phase 3 works:**

When a person has consistently mislabelled a category — say, they labelled 40 out of 200 batteries as "food waste" — the AI trained on their data will reflect that confusion. The confusion matrix will show a bright cell at the battery-vs-food row. That cell is not an AI failure; it is pointing directly to a labelling problem in that person's slice that must be fixed before the merge.

**What Phase 3 CAN detect (within-group confusions):**

- Chris: battery mislabelled as general_trash or food_organic
- Chris: food_organic mislabelled as general_trash (and vice versa)
- Naomi: cardboard mislabelled as paper
- Talvin: metal mislabelled as glass or textile

**What Phase 3 CANNOT detect (cross-group confusions — only visible after the merge):**

- Battery (Group 2) confused with metal (Group 3) — the most dangerous confusion in the project
- Cardboard (Group 1) confused with general_trash (Group 2)
- Glass (Group 3) confused with plastic (Group 1)

These cross-group confusions are invisible to each individual model because the classes from other groups simply do not exist in that model's universe. They will only surface in Phase 7, when all 9 classes are trained together. This is why Phase 7 (the first 9-class training run) is essential — it is the first point in the pipeline where cross-group confusions can be detected and addressed.

**Pass gate:** Every category must reach at least 60% accuracy (AP ≥ 0.60) on each person's own validation photos. Any category below this threshold indicates a within-group labelling problem. The fix is always in the labels at this stage — not in the model.

**Why 100 training cycles (epochs), not the full 300:**

This phase is a diagnostic tool, not the final training run. 100 cycles gives enough signal for labelling errors to appear in the confusion matrix without spending computing time on full convergence. If the model stops improving early (patience = 10–15 cycles), it stops automatically, saving time for the re-labelling work that follows.

**Expected results before training (based on literature):**

| Person | Data slice | Classes trained | Expected mAP@0.5 range | Why |
|--------|-----------|----------------|----------------------|-----|
| Naomi | TrashNet, RealWaste | plastic, paper, cardboard | 60–72% | Clean studio images; 3-class problem is relatively distinct |
| Chris | Mixed classification datasets | food_organic, battery, general_trash | 64–76% | Larger slice; but food/trash boundary is genuinely ambiguous |
| Talvin | TACO, edge cases | metal, glass, textile | 48–62% | Deliberately hard images (piled, occluded, odd angles) |

Talvin's lower expected score does not mean worse labelling — it means Talvin deliberately annotated the hardest images. A lower score on hard images is expected and informative.

**These ranges are higher than the production model target (≥ 85%) for one reason only:** 3-class problems are easier. Do not interpret Phase 3 results as evidence that the production model will meet its targets. They are not comparable.

---

### Phase 3 — Individual Model Success Metrics

These are the complete, standalone success metrics for each person's diagnostic model. They are separate from and cannot be compared with the production model metrics in Part 1.

**Primary metric — Confusion matrix (not a number, a pattern):**

The confusion matrix is a grid showing, for each class, how often the model correctly identified it versus what it confused it with. It is the most important Phase 3 output. A number like "mAP = 0.67" tells you something is wrong. The confusion matrix tells you exactly *what* is wrong and *which labels to fix*.

Reading rule:

- **Diagonal cell ≥ 0.60** for every class → labelling is clean, proceed to Phase 4
- **Off-diagonal cell > 0.30 in any row** → investigate that confusion pair; likely a labelling boundary problem
- **Diagonal cell < 0.50 and off-diagonal > 0.40** → clear labelling error; re-annotate before proceeding

---

**Per-group pass gates:**

#### Group 1 — Naomi (plastic, paper, cardboard)

| Metric | Pass gate | Action if failed |
|--------|----------|-----------------|
| mAP@0.5 overall | ≥ 0.60 | Check confusion matrix for which class is dragging the score down |
| AP — plastic | ≥ 0.60 | Review plastic labels; check for plastic bags mislabelled as textile or trash |
| AP — paper | ≥ 0.60 | Review paper labels; check for paper confused with cardboard |
| AP — cardboard | ≥ 0.60 | Review cardboard labels; check for flat cardboard mislabelled as paper |
| Confusion matrix: paper ↔ cardboard off-diagonal | < 0.30 | The paper/cardboard boundary is the highest-risk confusion in this group; update labelling guide if exceeded |

Key watch point: paper and cardboard are the most visually similar pair in Group 1. A flat unfolded cardboard sheet and a thick sheet of paper are genuinely hard to distinguish. Any confusion in this pair needs a clear labelling guide update before Phase 4.

---

#### Group 2 — Chris (food_organic, battery, general_trash)

| Metric | Pass gate | Action if failed |
|--------|----------|-----------------|
| mAP@0.5 overall | ≥ 0.60 | Check confusion matrix |
| AP — food_organic | ≥ 0.60 | Review food labels; check for food residue on containers being labelled as food rather than the container material |
| AP — battery | ≥ 0.65 | Battery gets a stricter diagnostic threshold — see note below |
| AP — general_trash | ≥ 0.60 | Review trash labels; check for food waste mislabelled as general trash |
| Confusion matrix: battery ↔ general_trash off-diagonal | < 0.25 | Very strict — a battery entering the trash stream is still a safety risk |
| Confusion matrix: food_organic ↔ general_trash off-diagonal | < 0.35 | Acceptable boundary confusion — resolve with labelling guide |

> **Why battery AP pass gate is 0.65 here, not 0.60:**
> Battery is safety-critical. Even within Group 2, the labelling must be cleaner than average. Note that this 0.65 threshold is a *diagnostic* gate only — it does not mean battery is safe in production. In production, battery competes with metal (which is absent in Group 2). The 0.65 at Phase 3 only confirms Chris labelled batteries consistently within their own class group.
>
> **What Phase 3 cannot tell you about battery:** If Chris's battery AP is 0.78 at Phase 3, that does not mean battery AP will be 0.78 in the production model. In production, battery will also need to be separated from metal, glass containers, and other metallic objects from Group 3 — none of which exist in Chris's diagnostic model. Battery's true production performance only becomes measurable at Phase 7.

---

#### Group 3 — Talvin (metal, glass, textile)

| Metric | Pass gate | Action if failed |
|--------|----------|-----------------|
| mAP@0.5 overall | ≥ 0.48 | Lower threshold reflects deliberately hard edge-case images |
| AP — metal | ≥ 0.55 | Review metal labels; crushed cans and flat metal sheets may be labelled inconsistently |
| AP — glass | ≥ 0.55 | Review glass labels; broken glass fragments vs intact bottles may differ |
| AP — textile | ≥ 0.50 | Lowest gate — highest variation class (torn shirts, plastic bags, fabric scraps all map to textile) |
| Confusion matrix: metal ↔ glass off-diagonal | < 0.35 | Both are often cylindrical containers; boundary must be in the labelling guide |

> **Why Group 3 has lower gates than Groups 1 and 2:**
> Talvin deliberately annotated edge cases — items at odd angles, piled up, partially obscured. A lower AP on these images does not mean the labels are wrong. It means the problem is genuinely harder. The confusion matrix diagnosis is more important than the mAP number for Group 3. If the confusion matrix shows no clear pattern of systematic errors, Group 3 passes even at the lower thresholds.

---

**What Phase 3 does NOT measure (and why):**

| Metric | Why not measured at Phase 3 |
|--------|-----------------------------|
| mAP@0.5:0.95 | Too strict for diagnostic purposes; segmentation mask precision is not the focus here — label category errors are |
| Inference speed (FPS) | Hardware varies per person; speed is not a Phase 3 concern |
| Generalisation gap | No quarantine set at Phase 3; the diagnostic model is not evaluated for production readiness |
| Battery AP as a production safety gate | Battery here only competes with food/trash — the metal confusion is invisible. Production battery AP is only measurable at Phase 7 |

**Full Phase 3 vs Production metrics comparison:**

| Metric | Phase 3 individual model | Production model (Phase 7–9) |
|--------|--------------------------|------------------------------|
| mAP@0.5 target | ≥ 0.48–0.60 (per group) | ≥ 0.85 |
| Per-class AP target | ≥ 0.50–0.65 (per class, per group) | ≥ 0.80 for battery; ≥ 0.85 overall |
| Primary output | Confusion matrix — find label errors | mAP, precision, recall — validate production readiness |
| Battery gate | ≥ 0.65 (within Group 2 only) | ≥ 0.80 (competing with all 9 classes including metal) |
| Cross-group confusions visible? | ❌ No | ✅ Yes |
| Comparable to each other? | ❌ No | ✅ Yes |

---

### PHASE 4 — Cross-Team Human Audit: Making Sure Three People Teach the AI the Same Things

**The plain English version:**

Three people have now labelled three separate sets of photos. Before we combine them, we need to verify that all three people mean the same thing when they write "plastic" or "battery." If Naomi and Chris would label the same photo differently, the merged dataset contains contradictory lessons — and the AI cannot converge on a consistent answer when the training data disagrees with itself.

**The agreement test:**

Team members compare each other's labels on a shared set of photos that everyone labelled independently. For each photo, we check: did everyone agree on the category? Did everyone draw the outline in roughly the same place?

- Category agreement must reach **≥ 85%** across the audited sample
- Outline overlap (Mask IoU) must exceed **0.75** — meaning the two outlines must cover at least 75% of the same pixels

**Why 85% and not 100%:**

100% agreement is not achievable and not the goal. Some items are genuinely ambiguous — a heavily crushed aluminium can looks different from a clean one, and two people might reasonably classify it differently. Requiring 100% would mean either removing all hard items from the dataset (bad — these are exactly the items the AI needs to learn) or creating endless disagreements that never resolve (bad — the project never moves forward).

85% agreement means the obvious cases are resolved and only genuinely ambiguous items remain. Those genuinely ambiguous items are resolved through team discussion, and the labelling guide is updated so the same question never causes disagreement again. This is the continuous improvement loop applied to the training data itself.

**Why this matters for the final model:**

An AI trained on contradictory labels will appear confused not because it is too simple, but because it was taught conflicting information. A battery labelled as battery in 80 photos and as metal in 20 photos produces a model that is 80% confident about batteries at best — the 20 contradictory examples act as persistent noise that caps accuracy. Phase 4 removes that noise before it enters training.

**Citation:** Mosqueira-Rey, E., Hernández-Pereira, E., Alonso-Ríos, D., Bobes-Bascarán, J., & Fernández-Leal, Á. (2023). Human-in-the-loop machine learning: A state of the art. *Artificial Intelligence Review*, *56*(4), 3005–3054. <https://doi.org/10.1007/s10462-022-10246-w>

---

### PHASE 5 — Automated Label Error Scan: Finding the Mistakes Humans Cannot See

**The plain English version:**

Human reviewers are good at catching individual errors — "this one photo is labelled wrong." They are not good at catching *systematic* errors — "the same mistake was made across 200 photos in a consistent pattern." Phase 5 uses an automated tool (Cleanlab) to find the patterns.

**How confident learning works:**

The Phase 3 diagnostic model assigned a confidence score to every photo: "I think this is a battery with 82% confidence, metal with 11%, plastic with 7%." When the model's confidence strongly disagrees with the human label — for example, the model says "95% confident this is metal" but the human labelled it "battery" — that disagreement is flagged as a potential labelling error.

The key insight from Northcutt et al. (2021) is this: *a correct label will never consistently disagree with a well-trained model's high-confidence predictions*. When disagreements cluster — when 30 photos all have the same pattern of "human says X, model strongly says Y" — that cluster is almost certainly a systematic labelling mistake, not a model failure.

**What happens to flagged photos:**

Flagged photos are reviewed by the team. They are either:

- Corrected and re-labelled (the model was right, the human was wrong)
- Kept as-is with a note (the model was wrong; the human label was correct; this photo is kept but monitored)
- Removed entirely (the photo is genuinely too ambiguous to label with confidence)

**Why this matters:**

Systematic label noise is the most common reason a model plateaus below its accuracy target. A model trained on 5% mislabelled data can rarely exceed 95% accuracy — the noise creates a ceiling. By removing systematic errors before Phase 7 training begins, we raise the achievable ceiling for all subsequent tuning.

**Citations:**

- Northcutt, C. G., Jiang, L., & Chuang, I. L. (2021). Confident learning: Estimating uncertainty in dataset labels. *Journal of Artificial Intelligence Research*, *70*, 1055–1093. <https://doi.org/10.1613/jair.1.12125>
- Kertész, C. (2021). Automated cleanup of the ImageNet dataset by model consensus, explainability and confident learning. *arXiv*, 2103.16324. <https://doi.org/10.48550/arXiv.2103.16324> ⚠️ *arXiv preprint — verify peer-reviewed version before final submission*

---

### PHASE 6 — Data Merge, Balancing, and Split: Preparing the Final Training Set

**The plain English version:**

We now have three clean, audited sets of labelled photos. Phase 6 combines them into one final dataset and applies two rules that are critical for fair, unbiased training.

**Rule 1 — Balance the dataset (hard cap at 5,000 photos per category):**

Our dataset has 139,909 food/organic waste photos and only 12,814 battery photos. If we train on this raw imbalance, the AI learns a shortcut: food waste is the most common answer, so default to food waste when uncertain. This produces deceptively high accuracy scores — because the AI is right whenever the item really is food waste — while being nearly useless for rare categories.

To fix this, we apply a hard cap of 5,000 photos per category. Every category contributes exactly 5,000 training photos. The AI has no reason to favour one category over another because all categories appear with equal frequency.

**What this does to the baseline:**

Before balancing: if the AI always guessed "food waste," it would be right 61.5% of the time — appearing to perform well without learning anything.
After balancing: if the AI always guessed "food waste," it would be right 11.1% (1 in 9 categories). Any model that scores above 11.1% has learned something real. This 11.1% is our Baseline 1 — the floor that any model must beat to justify its existence.

**Rule 2 — Stratified 80/20 split with zero data leakage:**

The dataset is divided into two groups that never overlap:

- **Training set (80%)** — what the AI learns from. It sees these photos thousands of times.
- **Validation set (20%)** — what we use to measure performance. The AI never trains on these photos.

"Stratified" means each category maintains the same 80/20 ratio. We do not accidentally put all of one category's rare photos into training and have nothing to measure validation against.

"Zero data leakage" means the same photo never appears in both sets. A photo that is in both training and validation would mean the AI is being tested on photos it already memorised — falsely inflating the score.

**Citation:** Northcutt, C. G., et al. (2021). Confident learning. *JAIR*, *70*, 1055–1093. <https://doi.org/10.1613/jair.1.12125>

---

### PHASE 7 — First Full Training Run: Measuring the Untuned Baseline

**The plain English version:**

We now train the AI on the full clean merged dataset for the first time, using completely default settings with no optimisation. The purpose is not to get the best possible result — it is to establish an honest starting point that all subsequent improvements must beat.

**Why we deliberately record an untuned result:**

This is the Lean Six Sigma Measure phase. Before improving anything, measure the current state. Without a documented starting point, there is no way to prove that any later optimisation added real value. If we skip straight to tuning, we can never answer the question: "did the tuning actually help, or did the model improve on its own?"

Baseline 2 is that starting point.

---

### Phase 7 — Complete Initial Parameter Table (Benchmark Configuration)

Every parameter below is the YOLOv8s-seg default as published by Jocher, Chaurasia, & Qiu (2023). No parameter is changed from default in Phase 7. This is the benchmark configuration — the exact settings that produce Baseline 2. The primary reference for this initial configuration is Wang et al. (2026), who applied YOLOv8-seg to garbage segmentation on the TACO dataset using the same architecture and achieved a mask mAP@50 of 82.6% — establishing the upper bound we expect before domain-specific tuning.

**Core training parameters:**

| Parameter | Value used | Plain English meaning | Why this value | Citation |
|-----------|------------|----------------------|---------------|----------|
| `model` | YOLOv8s-seg | Which AI architecture we use | Small variant: faster training, lower memory requirement, allows rapid iteration. Wang et al. (2026) applied YOLOv8-seg to garbage segmentation on TACO and achieved mask mAP@50 of 82.6%. If Phase 8 tuning cannot close the gap to ≥ 0.85, upgrade path is YOLOv8m-seg | Wang et al. (2026); Ding et al. (2024) |
| `pretrained` | True (COCO weights) | Start from a model that already knows how to see general objects | Transfer learning requires fewer images and less compute than training from scratch | Jaikumar et al. (2020) |
| `epochs` | 100 | How many times the AI studies the full training dataset from start to finish | 100 gives a clear convergence signal for baseline measurement; Phase 8 extends to 300 | Ajayi et al. (2024); Midigudla et al. (2025) |
| `imgsz` | 640 | The resolution each photo is resized to before the AI sees it (640 × 640 pixels) | YOLOv8 standard resolution; Phase 8 Run 1 tests 1280 to evaluate the trade-off | Jocher et al. (2023); Ren et al. (2024); Steindl et al. (2025) |
| `batch` | Set per machine | How many photos the AI studies simultaneously before updating its knowledge | Start at 16 and halve if out-of-memory errors occur. Larger batch = more stable gradient updates; smaller batch = less memory required. Results must be reported with the batch size used | Jocher et al. (2023); Ren et al. (2024); Steindl et al. (2025); Abo-Zahhad & Abo-Zahhad (2025) |
| `patience` | 50 | How many consecutive epochs with no improvement before training stops early | Prevents wasted compute if the model has already converged. 50 is the researcher's choice based on dataset size and training budget — no citation required for the value itself. Early stopping concept: Prechelt (1998) | Prechelt (1998) |
| `workers` | Set per machine | Background processes loading images while the AI is training | Match to the number of CPU cores available; 8 is a reasonable default | Jocher et al. (2023) |

**Optimiser parameters:**

| Parameter | Value | Plain English meaning | Why this value | Citation |
|-----------|-------|----------------------|---------------|----------|
| `optimizer` | SGD | The algorithm that adjusts the AI's internal weights after studying each batch of photos | SGD with momentum is the standard choice for YOLO-family models; produces stable convergence on large datasets | Redmon & Farhadi (2018); Jocher et al. (2023); Abo-Zahhad & Abo-Zahhad (2025) |
| `lr0` | 0.01 | Initial learning rate — how large each knowledge update is at the start of training | 0.01 is the standard starting rate for fine-tuning from COCO pretrained weights; too high causes divergence, too low causes stagnation | Jocher et al. (2023); Abo-Zahhad & Abo-Zahhad (2025) |
| `lrf` | 0.01 | Final learning rate as a fraction of lr0 — how large updates are at the end | Training uses cosine annealing: the learning rate gradually decreases from lr0 to lr0 × lrf over training. Smaller updates near convergence prevent overshooting the optimal weights | Jocher et al. (2023) |
| `momentum` | 0.937 | SGD momentum — carries forward the direction of previous updates to smooth out noisy batches | High momentum (close to 1.0) is standard for large-batch image training; 0.937 is the empirically validated value for YOLO models | Sutskever, Martens, Dahl, & Hinton (2013); Jocher et al. (2023); Abo-Zahhad & Abo-Zahhad (2025) |
| `weight_decay` | 0.0005 | Penalty added to training for having very large internal weights | Acts as a regulariser — prevents the model from becoming overspecialised to training photos. Equivalent to penalising a student for memorising one specific example instead of understanding the concept | Jocher et al. (2023) |
| `warmup_epochs` | 3.0 | Number of epochs at the start where the learning rate ramps up gradually instead of starting at full lr0 | Prevents unstable weight updates in the first few epochs when the model is adjusting from COCO weights to the waste dataset | Jocher et al. (2023) |
| `warmup_momentum` | 0.8 | Momentum used during the warmup period | Lower momentum during warmup reduces oscillation while the model is adjusting to the new task | Jocher et al. (2023) |
| `warmup_bias_lr` | 0.1 | Learning rate for bias parameters during warmup | Bias terms need a different warmup rate than weight terms; standard YOLO practice | Jocher et al. (2023) |

**Loss function parameters (what the AI is penalised for getting wrong):**

| Parameter | Value | Plain English meaning | Why this value | Citation |
|-----------|-------|----------------------|---------------|----------|
| `box` | 7.5 | How much weight the AI gives to getting the location of each object right | The bounding box (approximate rectangle around an object) feeds the segmentation mask. Getting location right is penalised 7.5× harder than classification by default | Jocher et al. (2023) |
| `cls` | 0.5 | How much weight the AI gives to getting the category right | Classification loss weight. **This is the parameter changed in Phase 8 Run 2** — we upweight it for battery and textile specifically | Jocher et al. (2023) |
| `dfl` | 1.5 | Distribution focal loss — penalises imprecise boundary prediction at the sub-pixel level | Controls how precisely the segmentation mask hugs the true edge of each object | Jocher et al. (2023) |

**Data augmentation parameters (what the AI sees during training to improve robustness):**

| Parameter | Value | Plain English meaning | Why enabled/disabled for Phase 7 | Citation |
|-----------|-------|----------------------|----------------------------------|----------|
| `mosaic` | 1.0 (enabled) | Combines 4 training photos into a single image during training. The AI sees 4 items simultaneously, learning to handle multi-item scenes | Enabled at default strength. Teaches multi-item awareness without custom setup | Bochkovskiy, Wang, & Liao (2020) |
| `hsv_h` / `hsv_s` / `hsv_v` | 0.015 / 0.7 / 0.4 | Randomly shifts the hue (colour tone), saturation (colour intensity), and brightness of each training photo | Teaches the AI that a green plastic bottle and a clear plastic bottle are both "plastic"; makes the model robust to different lighting conditions on the conveyor | Standard augmentation; Jocher et al. (2023) |
| `fliplr` | 0.5 | Randomly mirrors 50% of training photos left-to-right | An aluminium can photographed from the left and from the right should both be "metal." This teaches left-right invariance | Standard augmentation |
| `translate` | 0.1 | Randomly shifts each photo slightly in position | Prevents the model from relying on where in the photo an item appears rather than what it looks like | Jocher et al. (2023) |
| `scale` | 0.5 | Randomly resizes objects to simulate different distances from the camera | Items on a conveyor belt are not always the same distance from the camera | Jocher et al. (2023) |
| `copy_paste` | 0.0 (disabled) | Overlapping item augmentation | **Off for Phase 7 baseline.** Enabled in Phase 8 Run 3 to measure its isolated contribution | Ghiasi et al. (2021) |
| `degrees` | 0.0 (disabled) | Rotation augmentation | **Off for Phase 7 baseline.** Enabled in Phase 8 Run 4 to measure its isolated contribution | Standard augmentation |
| `mixup` | 0.0 (disabled) | Blends two photos together at partial opacity | Off by default; causes confusion in segmentation tasks where each pixel must belong to a single object | Jocher et al. (2023) |
| `flipud` | 0.0 (disabled) | Upside-down flip | Off — items do not appear upside down on a conveyor belt under normal conditions | Task-specific decision |

**Inference and evaluation parameters:**

| Parameter | Value | Plain English meaning | Why this value |
|-----------|-------|----------------------|---------------|
| `conf` | 0.25 | Minimum confidence score for a detection to be reported during evaluation | YOLOv8 default evaluation threshold; Phase 9 deployment uses class-specific thresholds (0.85 general / 0.90 battery) |
| `iou` | 0.7 | When the AI detects the same object twice (duplicate detection), the one with lower confidence is removed if the two outlines overlap more than 70% | Standard NMS (non-maximum suppression) threshold for segmentation models |
| `val` | True | Run validation at the end of each epoch | Produces the learning curve — shows whether training accuracy and validation accuracy are tracking together or diverging |

**Summary — what Phase 7 deliberately omits (and why):**

| What is missing | Effect | Fixed in |
|----------------|--------|----------|
| Battery class upweighting | Model treats all 9 classes equally; battery/metal confusion goes unmitigated | Phase 8 Run 2 |
| Higher resolution (1280px) | Small objects like batteries appear at lower pixel density | Phase 8 Run 1 |
| Copy-paste augmentation | No synthetic overlapping-item scenarios | Phase 8 Run 3 |
| Rotation augmentation | No odd-angle generalisation | Phase 8 Run 4 |
| Focal loss | Model treats easy and hard examples equally | Evaluated in Phase 8 if needed |

Everything absent from Phase 7 is absent deliberately. Phase 7 is the honest zero — the score we earn before any optimisation. Phase 8 adds each item one at a time and measures whether it helped.

**Citations for this parameter table:**

- Jocher, G., Chaurasia, A., & Qiu, J. (2023). *Ultralytics YOLO* (Version 8.0.0) [Software]. GitHub. <https://github.com/ultralytics/ultralytics> *(Primary source for all default parameter values)*
- Bochkovskiy, A., Wang, C.-Y., & Liao, H.-Y. M. (2020). YOLOv4: Optimal speed and accuracy of object detection. *arXiv*, 2004.10934. <https://doi.org/10.48550/arXiv.2004.10934> *(Mosaic augmentation — introduced in YOLOv4, carried into v8)*
- Sutskever, I., Martens, J., Dahl, G., & Hinton, G. (2013). On the importance of initialization and momentum in deep learning. *Proceedings of the 30th International Conference on Machine Learning (ICML)*, *28*(3), 1139–1147. *(SGD momentum rationale)*
- Ghiasi, G., et al. (2021). Simple copy-paste. *CVPR 2021*. <https://doi.org/10.1109/CVPR46437.2021.00294> *(Copy-paste — disabled in Phase 7, measured in Phase 8)*
- Ajayi, O. G., Ibrahim, P. O., & Adegboyega, O. S. (2024). Effect of hyperparameter tuning on the performance of YOLOv8 for multi crop classification on UAV images. *Applied Sciences*, *14*(13), 5708. <https://doi.org/10.3390/app14135708> *(Empirical YOLOv8 hyperparameter tuning study — epochs, lr0, batch)*
- Ren, Y., Li, Y., & Gao, X. (2024). An MRS-YOLO model for high-precision waste detection and classification. *Sensors*, *24*(13), 4339. <https://doi.org/10.3390/s24134339> *(Waste classification — batch=16, imgsz=640, epochs=300)*
- Steindl, G., Baca, A., & Kornfeind, P. (2025). Influences and training strategies for effective object detection in challenging environments using YOLO NAS-L. *Sensors*, *26*(1), 190. <https://doi.org/10.3390/s26010190> *(Batch size, imgsz=640, pretrained COCO weights analysis)*
- Abo-Zahhad, M. M., & Abo-Zahhad, M. (2025). Real-time intelligent garbage monitoring and efficient collection using YOLOv8 and YOLOv5 deep learning models for environmental sustainability. *Scientific Reports*, *15*, 16024. <https://doi.org/10.1038/s41598-025-99885-x> *(Waste — SGD, lr=0.01, momentum=0.95, batch=16)*
- Prechelt, L. (1998). Early stopping — but when? In G. Orr & K.-R. Müller (Eds.), *Neural Networks: Tricks of the Trade* (Lecture Notes in Computer Science, vol. 1524, pp. 55–69). Springer. <https://doi.org/10.1007/3-540-49430-8_3> *(Early stopping concept — patience parameter rationale)*
- Wang, Z., Zhang, Z., Wang, T., Zhang, X., Ren, Z., & Zhang, Y. (2026). Garbage recognition based on YOLOv8-seg: An instance segmentation approach for automated waste sorting. *International Core Journal of Engineering*, *12*(4), 267–278. <https://doi.org/10.6919/ICJE.202604_12(4).0029> *(Primary reference for Phase 7 initial model configuration — YOLOv8-seg on TACO, mask mAP@50 = 82.6%)*

---

**What we expect before training (based on literature):**

| Metric | Expected range | Reason it is below target |
|--------|---------------|--------------------------|
| Overall accuracy (mAP@0.5) | 58–70% | No class weighting, no advanced augmentation |
| Battery accuracy | 48–65% | No battery-specific settings; battery/metal confusion unmitigated |
| Processing speed | 28–35 FPS | Within target range at default settings |

These numbers are low compared to our targets — deliberately so. The gap between Baseline 2 and the target defines exactly how much work Phase 8 needs to do.

**Citations:**

- Ding, R., Jiang, K., Cheng, G., Liu, Z., Yang, Q., Zhou, Z., Bi, S., & Xiao, N. (2024). Performance comparison of YOLOv5, YOLOv8, and RCNN for waste detection and classification. *2024 IEEE IICAIET*, 1–7. <https://doi.org/10.1109/iicaiet62352.2024.10730703>
- Midigudla, S. R. K., Suresh, A., Smolarski, J., & Elamer, A. A. (2025). AI-driven waste classification system using YOLOv8 for sustainable waste management. *(Verify full journal citation before submission)*

---

### PHASE 8 — Hyperparameter Tuning: Closing the Gap to Target

**The plain English version:**

Phase 8 is where we deliberately close the gap between the Baseline 2 score and the ≥ 85% target. We do this by making one specific change at a time, retraining, and measuring whether the change improved things. Only changes that demonstrably improve the score are kept.

**Why one change at a time:**

If we change five settings simultaneously and the score improves, we have no idea which of the five changes caused the improvement. The next time we train, we would have to keep all five together — we cannot know which ones are actually helping. Worse, if a future researcher wants to verify our work, they cannot isolate the contribution of any single decision.

One change at a time is slower, but every improvement is traceable, citable, and reproducible.

**The four tuning decisions, explained in plain English:**

---

#### Tuning Run 1 — Higher resolution images (imgsz: 640 → 1280 pixels)

Think of the difference between reading a document on a small phone screen versus a large monitor. At 640 pixels, small objects like batteries appear very small in the image — the AI has fewer pixels of information to work with when making its decision. At 1280 pixels, the same battery appears twice as large in each dimension (four times the pixel area). The AI has significantly more detail to detect the difference between a battery and a small aluminium can.

The trade-off: larger images require more computing memory and are slower to process. We verify that the speed stays above 25 FPS after this change before keeping it.

Expected effect: +3–8% improvement in battery accuracy specifically.

---

#### Tuning Run 2 — Class loss weighting (upweight battery and textile)

During training, the AI optimises a score that summarises how wrong its predictions are. By default, being wrong about a battery counts the same as being wrong about any other category. We change this by making errors on battery and textile count more — specifically 2× more for battery and 1.5× more for textile.

The practical effect: the AI is penalised more heavily for getting batteries wrong, so it devotes more of its learning capacity to understanding what makes a battery a battery. This is the equivalent of a student knowing that one topic is worth double the marks on the exam — they study it harder.

Battery and textile are chosen because they are the two categories most likely to fall below their individual accuracy targets. Battery because of visual similarity to metal. Textile because of visual variety — a torn cotton shirt and a polyester shopping bag are both "textile" but look very different.

Expected effect: improved precision and recall on the two hardest minority categories.

**Citation:** Menke, J., Reischl, M., & Mikut, R. (2024). Active learning strategies for robust industrial machine vision. *(Cite per project reference — 100-correction batch threshold)*

---

#### Tuning Run 3 — Copy-Paste Augmentation

Copy-paste augmentation creates synthetic training scenarios by taking an object from one image and pasting it on top of another image. The result is a new training photo showing two overlapping items.

Why this matters: on a real conveyor belt, items are almost never neatly separated. A plastic bottle sitting on top of a cardboard box is a routine scenario. But in our training photos, each image typically shows one or two items. If the AI has never trained on overlapping items, it has no strategy for them — it will either ignore the item underneath or misclassify the combined shape as something else.

Copy-paste augmentation solves this without requiring thousands of new photos. We synthetically create the overlapping scenarios that the AI needs to learn from.

Expected effect: improved mAP@0.5:0.95 — the strict accuracy metric that measures how precisely the AI locates item boundaries, which is hardest when items overlap.

**Citation:** Ghiasi, G., Cui, Y., Srinivas, A., Qian, R., Lin, T.-Y., Cubuk, E. D., Le, Q. V., & Zoph, B. (2021). Simple copy-paste is a strong data augmentation method for instance segmentation. *CVPR 2021*, 2918–2928. <https://doi.org/10.1109/CVPR46437.2021.00294>

---

#### Tuning Run 4 — Rotation Augmentation (degrees: 0 → ±30°)

Items on a conveyor belt do not arrive perfectly upright. A plastic bottle might be lying on its side, tilted 45 degrees, or tumbling as the belt moves. If the AI has only seen upright items during training, it will struggle to classify the same item at an unusual angle.

Rotation augmentation solves this by randomly rotating each training photo by up to 30 degrees in either direction during training. The AI sees the same battery at many different orientations and learns that the orientation does not change what the object is.

Expected effect: more consistent accuracy across real-world conveyor conditions where items arrive at unpredictable angles.

---

**Extended training duration for Phase 8:**

Phase 7 trained for 100 cycles. Phase 8 trains for 300 cycles with a patience of 50 — meaning training continues until the model has gone 50 consecutive cycles without improving. This longer run gives the optimised model enough time to fully converge on the benefits of the tuning changes.

---

### Phase 8 Extended — What to Do If the 4 Runs Do Not Reach the Target

**The plain English version:**

The 4 tuning runs described above are the first layer of Phase 8. If any success metric is still not met after all 4 runs, Phase 8 does not end — it continues with a second layer of more targeted interventions. Every additional run follows the same rule: one change at a time, measured against the best result so far.

**Step 1 — Diagnose before tuning.**

Before adding more tuning runs, read the results table and identify exactly which metric is still failing. The fix depends entirely on which number is below target:

| Metric still failing | Root cause | Next intervention |
|---------------------|-----------|------------------|
| Overall mAP@0.5 below 85% | Model not converging fully | Run 5: switch optimizer to AdamW (see below) |
| Battery AP below 80% | Battery/metal confusion persists | Run 6: focal loss (fl_gamma = 1.5–2.0) |
| Precision below 85% | Too many false positives | Run 7: raise confidence threshold at evaluation; review class weight balance |
| Recall below 80% | Too many missed detections | Run 8: lower detection threshold; increase mosaic probability |
| Generalisation gap above 10% | Overfitting to training photos | Run 9: increase weight_decay (0.0005 → 0.001); add mixup augmentation |
| mAP@0.5:0.95 below 70% | Weak boundary precision | Run 10: increase dfl loss weight; refine segmentation masks in training data |

**Step 2 — The extended tuning sequence (if needed):**

---

#### Extended Run 5 — Switch optimizer from SGD to AdamW

SGD with momentum is the standard YOLO optimizer and is the correct starting point. However, for datasets with high class imbalance or noisy labels — both of which apply to this project — AdamW sometimes produces better convergence. AdamW handles irregular gradient surfaces more gracefully than SGD because it adapts the learning rate per parameter rather than using one global rate.

When to try: if mAP has plateaued in the 0.78–0.84 range across multiple runs and no single augmentation or weight change is moving the needle.

Setting: `optimizer=AdamW`, `lr0=0.001` (lower than SGD default — AdamW is sensitive to high learning rates).

**Citation:** Loshchilov, I., & Hutter, F. (2019). Decoupled weight decay regularization. *Proceedings of the International Conference on Learning Representations (ICLR 2019)*. <https://doi.org/10.48550/arXiv.1711.05101>

---

#### Extended Run 6 — Focal Loss (fl_gamma > 0)

Focal loss is a modification to the standard cross-entropy loss that reduces the weight given to easy, already-correctly-classified examples. The effect: the model stops spending training capacity on items it already recognises well (clear plastic bottles, obvious cardboard boxes) and redirects that capacity to the hard examples it keeps getting wrong (batteries that look like metal cans, textiles that look like general trash).

Setting: `fl_gamma=1.5`. Start here before increasing further — values above 2.0 can destabilise training.

When to try: if battery AP remains below 0.80 after Run 2's class weight upweighting. Focal loss attacks the hard-example problem from a different angle than class weighting — they are complementary interventions.

**Citation:** Lin, T.-Y., Goyal, P., Girshick, R., He, K., & Dollár, P. (2017). Focal loss for dense object detection. *Proceedings of the IEEE International Conference on Computer Vision (ICCV)*, 2980–2988. <https://doi.org/10.1109/ICCV.2017.324>

---

#### Extended Run 7 — Mixup Augmentation

Mixup creates training images by blending two photos together at partial transparency — for example, a plastic bottle image blended 40% with a cardboard image. The label is a weighted combination: 40% plastic, 60% cardboard.

This forces the model to build smoother, more generalised decision boundaries rather than hard cutoffs. The practical effect: better precision on ambiguous items because the model has been trained on blended in-between cases.

Setting: `mixup=0.1` (10% of training batches use mixup). Do not exceed 0.2 for segmentation tasks — heavy mixup disrupts pixel-level mask learning.

When to try: if generalisation gap exceeds 10% or precision is below 0.85 after the initial 4 runs.

**Citation:** Zhang, H., Cissé, M., Dauphin, Y. N., & Lopez-Paz, D. (2018). mixup: Beyond empirical risk minimization. *Proceedings of the International Conference on Learning Representations (ICLR 2018)*. <https://doi.org/10.48550/arXiv.1710.09412>

---

#### Extended Run 8 — Label Smoothing

Label smoothing prevents the model from becoming overconfident. In standard training, the correct label is 100% ("this is definitely a battery"). Label smoothing changes it to, say, 95% ("this is very likely a battery but there is 5% uncertainty"). This sounds counter-intuitive — why introduce fake uncertainty? — but overconfident models generalise poorly. A model trained to be 100% certain tends to fail badly on items that are slightly different from its training examples.

Setting: `label_smoothing=0.1`.

When to try: if the generalisation gap is above 10% and the model shows very high training accuracy (>95%) but lower validation accuracy — a classic sign of overconfidence.

**Citation:** Szegedy, C., Vanhoucke, V., Ioffe, S., Shlens, J., & Wojna, Z. (2016). Rethinking the Inception architecture for computer vision. *Proceedings of CVPR*, 2818–2826. <https://doi.org/10.1109/CVPR.2016.308>

---

**When to stop Phase 8 and accept the result:**

Phase 8 extended tuning has a stopping rule. If all of the following are true, Phase 8 is complete regardless of whether targets are fully met:

1. At least 8 tuning runs have been completed
2. The last 3 runs produced no improvement greater than 1% on any metric
3. The confusion matrix no longer shows a clear, fixable pattern

At this point, the model has reached its practical ceiling given the current training data. The correct next action is to investigate data quality — not add more tuning runs. Common causes of a hard ceiling: systematic label noise that Phase 5 did not catch; insufficient training examples for the failing class; class boundary ambiguity that requires more labelling guide clarity and re-annotation.

Proceeding to Phase 9 with the best available model and documenting the gap honestly is the correct academic approach. Dr. Narishah will accept a documented and explained limitation far more readily than a claim that targets were met when they were not.

---

### PHASE 9 — Generalisation Test: The Only Honest Measure of Real-World Performance

**The plain English version:**

This is the most important test in the entire pipeline. 100 photos have been locked away since Phase 1 — the AI has never seen them in any form. Not during training, not during validation, not during any diagnostic run. These photos are the quarantine set.

We now run the Phase 8 best model against these 100 photos and compare the score to the validation score from Phase 8. The difference is the generalisation gap.

**Why this matters more than any other score:**

Every other metric we have measured so far has been on photos the AI has in some way influenced — either directly trained on them, or had its performance shaped by the validation set through the tuning process. Those scores tell us how well the AI performs on photos it has been repeatedly exposed to.

The quarantine set tells us how well the AI performs on genuinely new photos. This is the only honest approximation of what will happen when the AI is deployed in a real facility and sees items it has never encountered before.

A model that scores 88% on its training/validation photos but 75% on the quarantine set has memorised rather than learned. It has found shortcuts specific to the training photos that do not generalise to new photos.

**The pass/fail rules:**

| What the gap shows | Interpretation | Action |
|-------------------|---------------|--------|
| Gap less than 5% | Suspiciously small — possible data contamination | Verify the quarantine photos were never exposed to the model before accepting |
| Gap between 5% and 10% | Normal — model has genuinely learned and generalises well | Authorise deployment |
| Gap greater than 10% | Model has memorised, not learned (overfitting) | Proceed to Phase 10 to fix |
| Any battery misclassified as a safe category | Zero-tolerance failure | Retrain regardless of all other scores |
| More than 20% of items missed entirely | Too many misses | Retrain |

**The battery zero-tolerance rule:**

A battery entering the recycling stream is a fire hazard. There is no acceptable rate of battery false positives — every single battery must be caught. If even one battery passes through Phase 9 as a false positive, the model fails regardless of its overall score. This is the asymmetric cost principle: one direction of error (battery missed) is catastrophic; the other direction (safe item routed for human review) is a minor operational inconvenience.

---

### PHASE 10 — Active Learning Retrain: Fixing What Phase 9 Reveals

**The plain English version:**

If Phase 9 fails, we retrain. But the way we retrain matters significantly.

**Why we do not start over:**

Starting from scratch every time would mean throwing away everything the model has learned and rebuilding from the beginning. This wastes weeks of computing time and discards valid knowledge. The model has already learned how to identify plastic, glass, paper, and most other categories reliably. The Phase 9 failure is usually specific to one or two categories or one type of scenario.

**What we do instead — fine-tuning:**

We keep the current best model as a starting point and make targeted, small updates. Specifically:

- The first two-thirds of the model (the visual processing layers) are frozen — they are not updated. This preserves everything the model has already learned about general visual patterns.
- Only the final decision-making layers are updated, using the photos that caused Phase 9 failures as new training examples.
- The learning rate (how large each update is) is set very low — 0.0005 instead of a typical 0.01. Small updates prevent the model from overwriting its existing knowledge when learning from the small number of failure cases.

**The active learning loop that continues after deployment:**

This fine-tuning approach does not only apply when Phase 9 fails. After the model is deployed in a facility, every time a human operator reviews an uncertain item and corrects the AI's guess, that correction is saved. When 100 corrections accumulate, the same frozen-backbone, low-learning-rate fine-tuning cycle is automatically triggered.

This means the AI continuously improves from real-world operator feedback — not just from the original training data. A battery that was consistently confused with metal cans in the first month of deployment becomes correctly classified by the second month, because the operator's corrections have trained the model on the exact real-world cases where it was failing.

100 corrections as the retraining threshold is supported by active learning research showing that smaller batches produce noisy, inconsistent updates while larger batches introduce too long a delay between improvement cycles (Mosqueira-Rey et al., 2023).

**Citations:**

- Mosqueira-Rey, E., Hernández-Pereira, E., Alonso-Ríos, D., Bobes-Bascarán, J., & Fernández-Leal, Á. (2023). Human-in-the-loop machine learning: A state of the art. *Artificial Intelligence Review*, *56*(4), 3005–3054. <https://doi.org/10.1007/s10462-022-10246-w>
- Menke, J., et al. (2024). Active learning strategies for robust industrial machine vision. *(Cite per project reference)*

---

## PART 5 — THE AI MODEL: WHY WE CHOSE YOLOV8M-SEG

### What the model is doing

YOLOv8s-seg (You Only Look Once, version 8, small-size, segmentation variant) is the specific AI architecture we use. It does two things simultaneously for every photo it processes: it identifies each object (classification) and it draws a precise pixel-level outline around each object (segmentation).

The segmentation capability matters for two reasons. First, on a conveyor belt with overlapping items, knowing which pixels belong to which object is necessary for accurate counting and routing. Second, the precise outline feeds back into the confidence score — if the model cannot draw a clean outline around a battery, it should not be highly confident about its battery classification.

### The three internal layers

Every photo passes through three sequential layers inside the model:

#### Layer 1 — The Visual Reading Engine (CSP-DarkNet Backbone)

This layer reads the raw photo and extracts visual patterns: edges (where does one surface end and another begin?), textures (is this surface smooth, ridged, or rough?), shapes (is this object cylindrical, flat, or irregular?), and colours at multiple levels of detail.

The model processes the same photo at multiple zoom levels simultaneously — a wide view to understand the overall scene, a medium view to understand individual objects, and a close view to detect fine details like a battery's label or a glass bottle's rim. This multi-scale processing is what allows the model to detect both a large cardboard box and a small battery in the same photo without losing detail on either.

This layer was pre-trained on 330,000 photos of 80 everyday objects. It already knows how to see. We do not retrain it — we reuse it.

#### Layer 2 — The Scale Merger (PANet Neck)

The reading engine produces separate outputs for each zoom level. The scale merger combines these into a single unified understanding of the photo — ensuring that a small battery partially hidden under a plastic bag is still detected, because the close-up view caught the metallic edge even though the wide view showed only plastic.

#### Layer 3 — The Decision Head (Decoupled Classification + Segmentation)

This is where the model makes its final outputs. Critically, the decision head has two separate sub-components: one for classification (what is this object?) and one for segmentation (what is its exact outline?). These two sub-components do not share parameters.

Earlier models combined classification and segmentation into a single component. This created a fundamental trade-off: improving one tended to degrade the other. Decoupling them allows each to specialise — classification accuracy and segmentation precision can both be optimised independently.

### Why not a different model?

| Alternative | Reason not chosen |
|-------------|------------------|
| YOLOv8m-seg (medium version) | Upgrade path if YOLOv8s-seg cannot reach ≥ 0.85 after Phase 8 tuning — higher parameter count, higher compute cost |
| YOLOv8l-seg (large version) | Higher compute cost with diminishing accuracy returns for a 9-class problem; reserved if both s and m variants fail to meet targets |
| YOLOv8n-seg (smaller version) | Tested on waste classification — accuracy insufficient for a 9-class problem |
| EfficientDet | Slower inference; benchmarked at >500ms per image on standard GPU — fails the 25 FPS gate |
| Detectron2 | Strong research pedigree but designed for research, not real-time deployment; also exceeds 500ms per image |

The small variant (s) is the starting point: faster training cycles allow rapid iteration through Phases 7 and 8. If Phase 8 tuning exhausts all 8 runs and still cannot reach mAP@0.5 ≥ 0.85, the upgrade path is YOLOv8m-seg — the medium variant adds ~15M parameters and typically gains 3–5% mAP on the same dataset (Ding et al., 2024).

**Citations:**

- Ding, R., et al. (2024). *IICAIET 2024*. <https://doi.org/10.1109/iicaiet62352.2024.10730703>
- Jaikumar, P., Vandaele, R., & Ojha, V. (2020). Transfer learning for instance segmentation of waste bottles using Mask R-CNN. *ISDA 2020*, vol. 1351, 140–149. <https://doi.org/10.1007/978-3-030-71187-0_13>
- White, G., Cabrera, C., Palade, A., & Li, F. (2020). WasteNet: Waste classification at the edge for smart bins. *arXiv*, 2006.05873. <https://doi.org/10.48550/arXiv.2006.05873>

---

## PART 6 — THE HUMAN-IN-THE-LOOP SYSTEM

### Why the AI alone is not enough

No AI model achieves 100% accuracy on real-world, uncontrolled data. The question is not whether the AI will sometimes be wrong — it will be. The question is what the system does when the AI is uncertain.

A system that pretends the AI is never uncertain will sometimes route a battery into the recycling stream or reject an aluminium can it misidentified as a battery. Neither outcome is acceptable.

The Human-in-the-Loop (HITL) system is the engineering solution to AI uncertainty. It makes uncertainty explicit and actionable instead of hiding it.

### The three-zone routing system

Every object detected by the AI receives a confidence score — a percentage expressing how certain the model is about its classification. Based on that score, every item is routed into one of three zones:

**Green Zone — Auto-accepted**
Confidence ≥ 85% AND the item is a recyclable category (plastic, paper, cardboard, metal, glass, or textile). The item moves automatically to the recycling stream. No human involvement required. This is the majority of items on a well-functioning belt.

**Red Zone — Auto-rejected**
Confidence ≥ 85% AND the item is a non-recyclable or hazardous category (food/organic waste, battery, general trash). The item is automatically diverted to the reject stream. An alert sounds for battery detections so an operator is aware.

**Yellow Zone — Human review required**
Confidence falls below 85% for any category. The item is held and displayed on the operator's screen with the AI's best guess and confidence score. The operator confirms or corrects. The Yellow Zone is not a failure state — it is a designed feature that ensures uncertain decisions are never made automatically.

**Battery exception:** For battery specifically, the threshold is raised to 90%, not 85%. Any battery detection with confidence below 90% goes to the Yellow Zone even if the model seems fairly certain. The reason: the visual difference between a battery and a small aluminium container is subtle enough at camera resolution that 85% confidence on battery is not confident enough. One missed battery in a metal recycling bale is a fire risk. The stricter threshold directly addresses this asymmetric cost.

### The correction-to-improvement loop

Every time an operator reviews a Yellow Zone item and corrects the AI's guess, that correction is saved in a log. The log records the original photo, what the AI guessed, and what the operator said the correct answer was.

When 100 corrections accumulate, a fine-tuning retrain is automatically triggered (Phase 10 protocol). The AI improves specifically on the cases where it was getting wrong. The Yellow Zone shrinks over time as the AI becomes more confident on previously uncertain items.

This feedback loop means the system deployed in month 1 and the system running in month 6 are not the same model. Month 6 has learned from thousands of real-world corrections that the original training data could never have anticipated.

**Citations:**

- Mosqueira-Rey, E., et al. (2023). Human-in-the-loop machine learning: A state of the art. *Artificial Intelligence Review*, *56*(4), 3005–3054. <https://doi.org/10.1007/s10462-022-10246-w>
- Sakr, G. E., et al. (2022). Computer vision for solid waste sorting. *Waste Management*, *142*, 29–43. <https://doi.org/10.1016/j.wasman.2022.02.009>

---

## PART 7 — PROVING EVERY STEP ADDED VALUE

### The baseline progression chain

We measure at four points across the project. Each point must be a measurable improvement over the previous one. If any step fails to improve on the previous benchmark, that step failed — regardless of how good the final number looks.

```text
BENCHMARK 1          BENCHMARK 3          BENCHMARK 2          FINAL TARGET
─────────────        ─────────────        ─────────────        ─────────────
Blind majority       Per-person           Full merged          Tuned master
class guess          training runs        dataset,             model
                                          no tuning
11.1% accuracy  →    52–76% mAP    →    58–70% mAP    →     ≥ 85% mAP
(always guess        (Phase 3)            (Phase 7)           (Phase 8)
food waste                                
after balancing)
```

**Reading rule:**

- If Benchmark 2 ≤ Benchmark 3: the data merge made things worse. Go back to Phase 6.
- If Final Target ≤ Benchmark 2: tuning added no value. Review Phase 8 decisions.
- If Final Target > all benchmarks: every stage contributed measurable improvement.

**Why Benchmark 3 comes before Benchmark 2 in the numbering:**

Benchmark 3 (per-person runs) happens at Phase 3, which is before Phase 7 (Benchmark 2). The numbering follows significance rather than chronology: Benchmark 2 is the main reference line for Phase 8 tuning.

---

## PART 8 — RISK REGISTER

Every target has at least one realistic failure mode. Knowing these in advance means the mitigation is already built into the pipeline.

---

### Risk: Battery cannot be distinguished from metal cans

What it threatens: Battery accuracy (≥ 80%) and the zero-tolerance Phase 9 gate

Why it happens: At 640-pixel camera resolution, a 9-volt battery and an aluminium drink can share nearly identical visual features — metallic surface, cylindrical shape, similar size. The model at default settings will confuse them regularly.

How we mitigate it:

1. Phase 8 Run 1 increases image resolution to 1280 pixels — giving the model four times more pixel information per object
2. Phase 8 Run 2 upweights battery in the loss function — the model is penalised more for battery mistakes
3. At deployment, battery confidence threshold is set to 90%, not 85% — uncertain battery detections always go to human review
4. Battery accuracy is tracked as a separate metric throughout — it cannot be masked by the overall average

---

### Risk: The model always guesses food/organic waste

What it threatens: Precision and recall on minority classes (battery, cardboard, textile)

Why it happens: Food/organic waste accounts for 139,909 photos in the raw dataset — 61.5% of all images. Without intervention, the model learns the statistical shortcut: "when unsure, guess food waste."

How we mitigate it:

- Phase 6 hard cap at 5,000 images per category makes all 9 classes equally represented in training
- The 11.1% baseline makes this problem visible: if the model scores near 61.5%, it has not learned the balance; if it scores near 11.1%, it has also not learned; the target ≥ 85% requires genuinely distinguishing all 9 classes

---

### Risk: The model performs well on training photos but fails on new photos

What it threatens: Generalisation gap (≤ 10%)

Why it happens: AI models can memorise training photos — learning to recognise specific images rather than general patterns. This happens when training photos appear multiple times (duplicates) or when the model is over-trained on the same limited set.

How we mitigate it:

- Phase 1 perceptual hash deduplication removes near-identical images before training
- Phase 9 uses 100 photos locked away since Phase 1 — no part of the pipeline has ever seen them — as the honest performance test
- The stratified 80/20 split with verified zero overlap ensures validation is genuinely separate from training

---

### Risk: Items overlap on the conveyor and confuse the AI

What it threatens: mAP@0.5:0.95 (≥ 70%) — the strict boundary accuracy metric

Why it happens: Training photos typically show one or two items per image. Real conveyor belt photos show items piled, overlapping, and partially obscured.

How we mitigate it:

- Phase 8 Run 3 (copy-paste augmentation) synthetically creates overlapping item scenarios during training, teaching the model strategies for handling partial occlusion before it encounters these scenarios in the real world

---

### Risk: The operator always clicks "confirm" without really checking

What it threatens: Active learning loop quality — if all corrections are wrong, the retrain degrades performance

Why it happens: Operators under time pressure may rubber-stamp Yellow Zone items without careful review. This is a known failure mode in HITL systems (Mosqueira-Rey et al., 2023).

How we mitigate it:

- The system logs the time between when a Yellow Zone item appears and when the operator makes a decision. Suspiciously fast decisions (sub-second confirmations) are flagged for audit
- The Phase 9 generalisation test is repeated after every fine-tuning cycle — if a retrain degraded performance, the anomaly is detected immediately and investigated

---

## PART 9 — FULL CITATION LIST

> ⚠️ Citations marked with ⚠️ require DOI verification on doi.org before final submission per citation integrity protocol.

### Peer-Reviewed Journals and Conference Proceedings

Abo-Zahhad, M. M., & Abo-Zahhad, M. (2025). Real-time intelligent garbage monitoring and efficient collection using YOLOv8 and YOLOv5 deep learning models for environmental sustainability. *Scientific Reports*, *15*, 16024. <https://doi.org/10.1038/s41598-025-99885-x> *(SGD, lr=0.01, momentum=0.95, batch=16 — Phase 7 optimizer and lr0 support)* ⚠️

Ajayi, O. G., Ibrahim, P. O., & Adegboyega, O. S. (2024). Effect of hyperparameter tuning on the performance of YOLOv8 for multi crop classification on UAV images. *Applied Sciences*, *14*(13), 5708. <https://doi.org/10.3390/app14135708> *(Empirical YOLOv8 hyperparameter tuning study — epochs, lr0, batch size)* ⚠️

Assoesoedarso, G., Widjaja, D., & Iskandar, A. A. (2024). Comparative evaluation of perceptual hashing and deep embedding methods for robust and efficient image deduplication. *Electronics*, *15*(7), 1493. <https://doi.org/10.3390/electronics15071493>

Ding, R., Jiang, K., Cheng, G., Liu, Z., Yang, Q., Zhou, Z., Bi, S., & Xiao, N. (2024). Performance comparison of YOLOv5, YOLOv8, and RCNN for waste detection and classification. *2024 IEEE International Conference on Artificial Intelligence in Engineering and Technology (IICAIET)*, 1–7. <https://doi.org/10.1109/iicaiet62352.2024.10730703>

Ghiasi, G., Cui, Y., Srinivas, A., Qian, R., Lin, T.-Y., Cubuk, E. D., Le, Q. V., & Zoph, B. (2021). Simple copy-paste is a strong data augmentation method for instance segmentation. *Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR)*, 2918–2928. <https://doi.org/10.1109/CVPR46437.2021.00294>

Jaikumar, P., Vandaele, R., & Ojha, V. (2020). Transfer learning for instance segmentation of waste bottles using Mask R-CNN algorithm. In *Intelligent Systems Design and Applications* (Vol. 1351, pp. 140–149). Springer. <https://doi.org/10.1007/978-3-030-71187-0_13>

Bochkovskiy, A., Wang, C.-Y., & Liao, H.-Y. M. (2020). YOLOv4: Optimal speed and accuracy of object detection. *arXiv*, 2004.10934. <https://doi.org/10.48550/arXiv.2004.10934> *(Mosaic augmentation — introduced here, carried into YOLOv8)*

Jocher, G., Chaurasia, A., & Qiu, J. (2023). *Ultralytics YOLO* (Version 8.0.0) [Software]. GitHub. <https://github.com/ultralytics/ultralytics> *(Primary reference for all Phase 7 default parameter values)*

Lin, T.-Y., Goyal, P., Girshick, R., He, K., & Dollár, P. (2017). Focal loss for dense object detection. *Proceedings of the IEEE International Conference on Computer Vision (ICCV)*, 2980–2988. <https://doi.org/10.1109/ICCV.2017.324> *(Phase 8 Extended Run 6 — focal loss for hard minority classes)*

Loshchilov, I., & Hutter, F. (2019). Decoupled weight decay regularization. *Proceedings of ICLR 2019*. <https://doi.org/10.48550/arXiv.1711.05101> *(Phase 8 Extended Run 5 — AdamW optimizer)*

Szegedy, C., Vanhoucke, V., Ioffe, S., Shlens, J., & Wojna, Z. (2016). Rethinking the Inception architecture for computer vision. *Proceedings of CVPR*, 2818–2826. <https://doi.org/10.1109/CVPR.2016.308> *(Phase 8 Extended Run 8 — label smoothing)*

Zhang, H., Cissé, M., Dauphin, Y. N., & Lopez-Paz, D. (2018). mixup: Beyond empirical risk minimization. *Proceedings of ICLR 2018*. <https://doi.org/10.48550/arXiv.1710.09412> *(Phase 8 Extended Run 7 — mixup augmentation)*

Menke, J., Reischl, M., & Mikut, R. (2024). Active learning strategies for robust industrial machine vision applications. *(Verify full journal citation and DOI before submission)*

Shearer, C. (2000). The CRISP-DM model: The new blueprint for data mining. *Journal of Data Warehousing*, *5*(4), 13–22. *(10-phase structure justification — CRISP-DM framework)*

Sutskever, I., Martens, J., Dahl, G., & Hinton, G. (2013). On the importance of initialization and momentum in deep learning. *Proceedings of the 30th International Conference on Machine Learning (ICML)*, *28*(3), 1139–1147. *(SGD momentum 0.937 rationale)*

Wirth, R., & Hipp, J. (2000). CRISP-DM: Towards a standard process model for data mining. *Proceedings of the 4th International Conference on the Practical Applications of Knowledge Discovery and Data Mining*, 29–39. *(Full CRISP-DM framework paper)*

Midigudla, S. R. K., Suresh, A., Smolarski, J., & Elamer, A. A. (2025). AI-driven waste classification system using YOLOv8 for sustainable waste management. *(Verify full journal citation and DOI before submission)*

Mosqueira-Rey, E., Hernández-Pereira, E., Alonso-Ríos, D., Bobes-Bascarán, J., & Fernández-Leal, Á. (2023). Human-in-the-loop machine learning: A state of the art. *Artificial Intelligence Review*, *56*(4), 3005–3054. <https://doi.org/10.1007/s10462-022-10246-w>

Northcutt, C. G., Jiang, L., & Chuang, I. L. (2021). Confident learning: Estimating uncertainty in dataset labels. *Journal of Artificial Intelligence Research*, *70*, 1055–1093. <https://doi.org/10.1613/jair.1.12125>

Prechelt, L. (1998). Early stopping — but when? In G. Orr & K.-R. Müller (Eds.), *Neural Networks: Tricks of the Trade* (Lecture Notes in Computer Science, vol. 1524, pp. 55–69). Springer. <https://doi.org/10.1007/3-540-49430-8_3> *(Early stopping concept — patience parameter rationale)*

Ren, Y., Li, Y., & Gao, X. (2024). An MRS-YOLO model for high-precision waste detection and classification. *Sensors*, *24*(13), 4339. <https://doi.org/10.3390/s24134339> *(Waste classification — Adam, lr=1×10⁻⁴, batch=16, epochs=300, imgsz=640)* ⚠️

Sakr, G. E., Mokbel, M. F., & Darwish, A. I. (2022). Computer vision for solid waste sorting: A critical review of academic research. *Waste Management*, *142*, 29–43. <https://doi.org/10.1016/j.wasman.2022.02.009>

Steindl, G., Baca, A., & Kornfeind, P. (2025). Influences and training strategies for effective object detection in challenging environments using YOLO NAS-L. *Sensors*, *26*(1), 190. <https://doi.org/10.3390/s26010190> *(Batch size, imgsz=640, pretrained COCO weights analysis)* ⚠️

Wang, Z., Zhang, Z., Wang, T., Zhang, X., Ren, Z., & Zhang, Y. (2026). Garbage recognition based on YOLOv8-seg: An instance segmentation approach for automated waste sorting. *International Core Journal of Engineering*, *12*(4), 267–278. <https://doi.org/10.6919/ICJE.202604_12(4).0029> *(Primary reference — YOLOv8-seg applied to garbage segmentation on TACO; mask mAP@50 = 82.6%; direct precedent for Phase 7 initial model configuration)*

### arXiv Preprints

Kertész, C. (2021). Automated cleanup of the ImageNet dataset by model consensus, explainability and confident learning. *arXiv*, 2103.16324. <https://doi.org/10.48550/arXiv.2103.16324> ⚠️

White, G., Cabrera, C., Palade, A., & Li, F. (2020). WasteNet: Waste classification at the edge for smart bins. *arXiv*, 2006.05873. <https://doi.org/10.48550/arXiv.2006.05873> ⚠️

---

## PART 10 — PRE-TRAINING CHECKLIST

```text
Before Phase 7:
[ ] All [SUGGESTED] ranges replaced with actual training results after runs complete
[ ] Battery AP confirmed as a SEPARATE column in the training results CSV
[ ] Quarantine set (100 images) verified — never seen by any model in Phases 3–8
[ ] Midigudla et al. (2025) full journal details verified before citing in presentation
[ ] Menke et al. (2024) full citation details verified

Before Phase 9:
[ ] Phase 8 tuning table complete — one row per run, what changed, what the new mAP was
[ ] Confusion matrix screenshots saved for all 9 classes — Dr. Narishah will ask for the battery row

Before deployment:
[ ] Battery confidence threshold hardcoded to 0.90 in deployment config (not operator-adjustable)
[ ] Recyclable confidence threshold set to 0.85 (operator-adjustable via slider)
[ ] Yellow Zone decision latency logging confirmed active
```

---

*PurityLoop AI Capstone AY2025/26 · Success Metrics Playbook*
*Written: 2026-06-11 | Talvin (ML R&D)*
*All expected ranges are pre-training projections grounded in cited literature. Replace with actual results after training.*
