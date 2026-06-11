# PurityLoop AI — HITL & Deep Learning Frameworks
## Capstone Project AY2025/26 | Sunway University | Department of Business Analytics
**Supervisor: Dr. Narishah Mohamed Salleh**
**Written: 2026-06-04 | Talvin (ML R&D)**

> This document covers two frameworks:
> - **HITL Framework** — how human review is built into the system so that the AI never operates without a safety net
> - **Deep Learning Framework** — how the AI model is built, trained, evaluated, and improved
>
> Each section contains: the conceptual framework, component breakdown, plain English explanation, slide-ready summary, and a Gemini image prompt.
> All technical terms are translated into plain English. Original terms appear in parentheses for reference.

---

---

# PART 1 — HITL FRAMEWORK
## Human-in-the-Loop: How Human Judgement Is Built Into the System

---

## 1.1 What HITL Means and Why We Need It

**In plain English:**

HITL stands for Human-in-the-Loop. It means the system is designed so that a human is always involved at the right moment — not for every decision (that would be no different from manual sorting), but specifically for the decisions the AI is not confident about.

The core idea is this: the AI handles what it is sure about automatically. When it is not sure, it pauses and asks a human. The human's answer is recorded. The AI learns from that answer. Over time, the AI becomes more confident in more situations — but the human safety net never disappears.

**Why this is not optional:**

An AI system that operates with no human oversight is a liability, not an asset. In a recycling facility, a missed battery is a fire risk. A wrongly rejected aluminium bale is revenue lost. The HITL framework is the engineering solution to the fact that no AI model achieves 100% accuracy — it channels uncertainty into a structured human review process instead of letting it become an error.

**The principle behind it:**

> The AI owns the easy decisions. The human owns the hard ones. The system is designed so neither side is overwhelmed.

---

## 1.2 The HITL Framework — Full Structure

The HITL framework operates at two distinct levels in PurityLoop AI:

```
LEVEL 1 — BUILD-TIME HITL (Before deployment)
  Phase 2: Each team member labels their own image slice
  Phase 3: Solo training run surfaces label mistakes via confusion matrix
  Phase 4: Cross-team label audit — human agreement must reach ≥85%
  Phase 5: Automated label error scan flags remaining mistakes
  → Purpose: ensure the AI is taught from correct human labels

LEVEL 2 — RUNTIME HITL (After deployment)
  Yellow Zone: AI certainty falls below threshold → item held for human review
  Operator confirms or corrects the AI's guess on the dashboard screen
  Correction is saved to the digital logbook
  When 100 corrections accumulate → AI retrains on those exact failure cases
  → Purpose: ensure the AI keeps improving from real-world mistakes
```

---

## 1.3 Level 1 — Build-Time HITL: Teaching the AI With Clean Labels

**Purpose:** Before the AI learns anything, the information it learns from (the labels) must be verified by humans. Garbage in, garbage out — if the labels are wrong, the AI learns the wrong things.

### Phase 2 — Individual Labelling

Each team member labels their own slice of images using a consistent smart labelling tool. Every item in every image is outlined and assigned one of the 9 categories. The labelling guide is locked before anyone starts — this prevents each person from making up their own interpretation of where, for example, to draw the boundary on a flattened plastic bottle.

**Key labelling rule:** a dirty recyclable is still labelled by material type, not by cleanliness. A greasy plastic bottle is still "plastic," not "general trash." This is critical — the AI must learn to classify by material, not by condition. The contamination check is a system-level decision, not a label-level one.

### Phase 4 — Cross-Team Human Audit

After each person finishes labelling their own slice, the team cross-checks each other's labels. This is the first formal HITL gate:

| Check | Threshold | If failed |
|-------|-----------|-----------|
| Label agreement between two reviewers on the same item | ≥85% agreement | Re-label disputed samples. Update the labelling guide to clarify the edge case. |
| Outline overlap between two reviewers on the same item | Mask IoU > 0.75 | Re-draw outlines on flagged items. |

**What "agreement" means in practice:** Person A labels an item as "cardboard." Person B, reviewing the same item independently, also labels it "cardboard." That is an agreement. If Person B says "general trash," that is a disagreement. Disagreements are resolved by discussion, then the labelling guide is updated to prevent the same disagreement from occurring again.

**Why ≥85% specifically:** 100% agreement is unachievable and undesirable — it would require every edge case to have an obvious answer. 85% agreement means the team has resolved the clear-cut cases and is flagging only genuinely ambiguous items. Items below 85% agreement are either re-labelled after discussion or removed from the dataset.

---

## 1.4 Level 2 — Runtime HITL: The Yellow Zone Review Queue

**Purpose:** After the AI is deployed, every detection that falls below the confidence threshold is routed to a human reviewer instead of being auto-decided. The reviewer's decision is recorded and eventually used to retrain the AI.

### The 3-Zone Routing System

```
Every detected item gets a certainty score from 0% to 100%

   ┌─────────────────────────────────────────────────────┐
   │  Certainty ≥85% + recyclable class                  │
   │  → GREEN: Auto-accepted to recycling stream         │
   └─────────────────────────────────────────────────────┘
   
   ┌─────────────────────────────────────────────────────┐
   │  Certainty ≥85% + hazardous or non-recyclable class │
   │  → RED: Auto-rejected. Alert sounds.                │
   └─────────────────────────────────────────────────────┘
   
   ┌─────────────────────────────────────────────────────┐
   │  Certainty below threshold (any class)              │
   │  → YELLOW: Held. Shown to operator. Human decides.  │
   └─────────────────────────────────────────────────────┘

   Battery exception: threshold is ≥90%, not ≥85%.
   Any battery below 90% certainty → YELLOW regardless.
```

### What the Operator Sees in the Yellow Zone

When an item enters the Yellow zone, the operator's screen displays:
- A photo of the item with the AI's outline drawn around it
- The AI's best guess for the category
- The AI's certainty score
- Two buttons: **Confirm** (AI was right) or **Correct** (AI was wrong, select correct category)

The operator makes a decision. The decision is saved immediately to the digital logbook with a timestamp and the operator's confirmation.

### Why the Battery Threshold Is Stricter

A standard 9-volt battery and a 330 mL aluminium drink can share almost identical visual characteristics at the camera resolution used: metallic surface, cylindrical shape, similar aspect ratio, similar size. The AI at default settings will confuse these regularly.

Rather than accepting a 85% confident "battery" call as correct, the system requires 90% certainty before auto-routing any battery to the reject stream. Below 90%, even a probable battery goes to the Yellow zone for human confirmation. This engineering choice reflects the asymmetric cost of errors:

- Cost of auto-rejecting a can that is actually a battery: nothing (it gets quarantined safely)
- Cost of auto-accepting a battery that is actually a can: fire risk in the plastic bale

One direction of error is acceptable. The other is not. The threshold reflects this.

---

## 1.5 The Active Learning Loop — How the AI Learns From Human Corrections

**Purpose:** Every human correction in the Yellow zone is potential training data. The active learning loop converts operator feedback into model improvement without requiring the team to manually collect new data.

```
ACTIVE LEARNING CYCLE

Step 1: AI makes a detection with low certainty → routed to Yellow zone
Step 2: Operator reviews the item → confirms or corrects the AI's guess
Step 3: Correction saved to amber_queue table with:
         - original image path
         - AI's predicted category
         - operator's confirmed category
         - timestamp
         - reviewed flag = 1
Step 4: When amber_queue reaches 100 reviewed corrections:
         → Active learning retrain triggered
Step 5: Retrain starts from the current best model (not from scratch)
         → Backbone layers frozen (preserve general visual features)
         → Only the final classification and segmentation layers retrain
         → Learning rate very low (lr0 = 0.0005)
         → New training set = original training data + 100 operator corrections
Step 6: Retrained model evaluated against Phase 9 pass gates
Step 7: If passes → new model replaces old model in deployment
         If fails → investigate failure, adjust, retrain again
Step 8: Cycle repeats at every 100 new corrections
```

**Why retrain from the current model instead of from scratch:**

Starting from scratch each time would require thousands of hours of computing time and would discard all the learning the model has already accumulated. Starting from the current model and making small targeted updates (called fine-tuning) is faster, cheaper, and safer. The risk of fine-tuning is "catastrophic forgetting" — the model unlearns old knowledge while learning new. Freezing the backbone layers and using a very low learning rate prevents this.

**Why 100 corrections as the threshold:**

100 corrections provides a statistically meaningful batch of new data without waiting too long between improvement cycles. With fewer samples, the retrain would be noisy — the model would overfit to a tiny number of examples. With more samples, the team would wait too long before the system improves. 100 is the practical balance point supported by active learning literature (Menke et al., 2024).

---

## 1.6 HITL Team Responsibility Matrix

| Responsibility | Who owns it | When |
|---------------|------------|------|
| Individual image labelling | All three annotators | Phase 2 |
| Cross-label audit (≥85% agreement check) | All three — Person C leads | Phase 4 |
| Automated label error review | Person C owns merge pipeline | Phase 5 |
| Runtime Yellow zone review | Facility operator (end user) | Live deployment |
| Active learning retrain trigger | Naomi (DataOps) | Every 100 corrections |
| Retrain quality evaluation | Talvin (ML) | After every retrain |
| Escalation if battery false positive occurs | All team + supervisor | Immediate |

---

## 1.7 HITL Slide-Ready Summary

**Slide Title:** Human-in-the-Loop — Where Humans and AI Work Together

**On the slide:**

The AI handles what it is sure about. A human handles what it is not.

| Stage | What triggers human involvement | What the human does |
|-------|--------------------------------|---------------------|
| **Build-time** (Phase 2) | Labelling every training image | Draw outlines, assign categories |
| **Build-time** (Phase 4) | Cross-checking each other's labels | Resolve disagreements, update labelling guide |
| **Runtime** (Yellow Zone) | AI certainty falls below 85% | Confirm or correct the AI's guess on-screen |
| **Runtime** (Active Learning) | 100 corrections accumulate | Corrections automatically trigger AI retrain |

**The feedback loop that never stops:**

```
AI detects item → uncertain → human reviews → human corrects
→ correction saved → 100 corrections → AI retrains
→ AI improves → fewer uncertain detections → human reviews less
→ cycle continues
```

**Speaker notes:**

Dr. Narishah will recognise this as HITL methodology — she cited Mosqueira-Rey et al. (2023) in her research framework. The key point to make: the Yellow zone is not a failure state. It is a designed feature. An AI system that has no uncertainty output is overconfident — it is not safer, it is just hiding its failures. The Yellow zone makes uncertainty explicit and actionable.

The active learning loop connects directly to DMAIC Control — it is the mechanism that sustains improvement after initial deployment. The system does not reach a fixed performance level and stop. It continues improving as long as operators are reviewing Yellow zone items.

---

**[GEMINI PROMPT — HITL Framework Visual]**

A clean two-level framework diagram on white background. Top half labelled "Build-Time HITL" with three boxes connected left to right: "Phase 2: Team Labels Images" → "Phase 4: Cross-Check Labels (≥85% agreement)" → "Phase 5: Remove Bad Labels". Bottom half labelled "Runtime HITL" with a circular loop: "AI detects item" → "Below 85% certainty" → "Yellow Zone — human reviews" → "Correction saved" → "100 corrections" → "AI retrains" → back to "AI detects item". A dividing line between top and bottom sections. Emerald green (#0F5132) boxes, white background, flat corporate design, clean arrows.

---

---

# PART 2 — DEEP LEARNING FRAMEWORK
## How the AI Model Is Built, Trained, Evaluated, and Improved

---

## 2.1 What Deep Learning Means in This Project

**In plain English:**

Deep learning is a method of teaching a computer to recognise things in photos by showing it thousands of examples. The computer does not follow written rules ("a battery is cylindrical and metallic"). Instead, it looks at enough labelled photos until it builds its own internal understanding of what each category looks like.

The "deep" part refers to the structure of the system — it has many layers of processing, each layer learning a different level of detail. The first layers learn basic edges and colours. The middle layers learn shapes and textures. The final layers learn "this combination of shapes, textures, and edges is a battery."

**What makes this harder than a standard photo classifier:**

A standard classifier answers one question: "what is the main object in this photo?" The PurityLoop AI system answers multiple questions simultaneously for every photo:

1. How many separate items are in this photo?
2. What is the exact outline of each item?
3. What category does each item belong to?
4. How certain are we about each decision?

This is called instance segmentation — identifying each item as an individual object with its own precise boundary. It is harder than classification, requires more training data, and is more computationally demanding. It is necessary because conveyor belt waste is never neatly separated — items overlap, stack, and obscure each other.

---

## 2.2 Model Selection — Why YOLOv8m-seg

**The shortlist considered:**

| Model | Why considered | Why not chosen |
|-------|---------------|----------------|
| YOLOv8m-seg | Proven waste classification performance, single-pass inference, anchor-free | — (chosen) |
| EfficientDet | High accuracy on standard benchmarks | Slower inference, harder to fine-tune for segmentation |
| Detectron2 | Strong research pedigree | Too slow for real-time conveyor belt (>500ms per image) |
| YOLOv8l-seg (larger version) | Higher accuracy ceiling | Requires more GPU memory than available on free training tier |
| YOLOv8n-seg (smaller version) | Very fast inference | Insufficient accuracy for 9-class problem |

**Why YOLOv8m-seg specifically:**

Midigudla et al. (2025) conducted a direct comparison of YOLOv8, EfficientDet, and Detectron2 on waste classification. YOLOv8 achieved greater than 85% accuracy while maintaining real-time processing speeds. The medium-size variant (m) provides the best balance between accuracy and computing resource requirements within the project's training constraints.

YOLOv8m-seg starts with weights pre-trained on 80 common object categories (the COCO dataset). This means the model already knows how to recognise general visual patterns — edges, textures, shapes — before any waste-specific training begins. Fine-tuning from this starting point requires far fewer examples and far less training time than starting from scratch.

---

## 2.3 Model Architecture — 3 Layers Explained

The YOLOv8m-seg model processes every image through three sequential layers:

### Layer 1 — The Visual Processing Engine (CSP-DarkNet Backbone)

**What it does:** reads the raw photo and extracts visual features — edges, gradients, textures, colour patterns, shapes at multiple scales.

**In plain English:** this is the part of the model that "sees." It does not yet know what it is looking at — it just converts the photo into a rich mathematical description of what visual patterns are present and where.

**Why it matters for waste:** waste items come in many sizes. A battery is small. A flattened cardboard box is large. The backbone processes the image at multiple resolutions simultaneously, which means it can detect both small and large objects in the same photo without losing detail on either.

### Layer 2 — The Scale Combiner (PANet Neck)

**What it does:** takes the visual features from Layer 1 (which exist at multiple resolution levels) and combines them into a unified representation.

**In plain English:** imagine looking at a photo from far away, from normal distance, and from very close, then merging all three views into one coherent understanding. The Scale Combiner does this mathematically. A battery hidden behind a plastic bag might only be visible at the close-up resolution level — the Scale Combiner ensures that detail is not lost when merging with the wider view.

**Why it matters for waste:** overlapping items on a conveyor belt require the model to simultaneously understand the big picture (what is the general scene?) and the fine detail (is that a metallic edge peeking out from under the cardboard?). The Scale Combiner enables both at once.

### Layer 3 — The Decision Head (Decoupled Classification + Segmentation)

**What it does:** takes the combined visual representation from Layer 2 and produces two outputs for every detected object:
1. A category label with a certainty score
2. A pixel-level outline (segmentation mask) of the object's exact boundary

**In plain English:** this is where the model makes its actual decisions. "This object is plastic, I am 91% certain, and its exact shape covers these pixels in the image." The two outputs are computed by two separate sub-components — one specialised for classification, one for outlining — which improves accuracy on both tasks compared to a shared output head.

**Why decoupled outputs matter:** earlier detection models used a single output head for both classification and outlining. This created a trade-off — improving classification often hurt outlining accuracy and vice versa. The decoupled design removes that trade-off by letting each sub-component specialise.

---

## 2.4 The Training Pipeline — 10 Phases

The deep learning framework follows a 10-phase quality-gated pipeline. Each phase has a defined input, a defined output, and a pass/fail gate. Failing a gate means going back to fix the problem — not proceeding with known errors.

### Phase 1 — Data Cleaning

**Input:** raw images from 6 merged public datasets (227,490 images total)

**What happens:**
- Duplicate images are removed using a photo fingerprint comparison (perceptual hashing with threshold=5). Near-identical images — such as consecutive frames of the same item — are identified and only one copy is kept.
- Blurry images are removed using a sharpness scoring method (Tenengrad filter). Images scoring below the minimum threshold are discarded.
- All images are confirmed to be valid format (.jpg, .jpeg, .png, .bmp).

**Output:** a clean, unique set of images with no duplicates and no blurry frames.

**Why this matters:** duplicate images in the training set cause the model to memorise specific examples rather than learn general patterns. If the same image of a battery appears 50 times in training and once in testing, the model effectively "recognises" that specific photo — it does not learn what batteries look like in general.

### Phase 2 — Labelling (Annotation)

**Input:** clean images from Phase 1

**What happens:**
- Each image is labelled by a team member using a smart polygon tool (SAM — Segment Anything Model). The tool draws an initial outline automatically; the labeller refines it.
- Each item in each image receives a category label from the 9-class taxonomy.
- Labels are stored in YOLO format: one text file per image, one line per object, containing category index and normalised outline coordinates.

**Output:** labelled dataset — every image has a corresponding label file.

**Gate:** outline overlap between two reviewers on matched samples must exceed 75% (Mask IoU > 0.75).

**Why SAM for initial outlines:** drawing precise polygon outlines around 45,000 images manually would take hundreds of hours. SAM generates an initial outline automatically from a single click. The labeller only needs to verify and refine, not draw from scratch. This reduces labelling time significantly while maintaining consistency.

### Phase 3 — Individual Diagnostic Training

**Input:** each team member's own labelled image slice

**What happens:**
- Each person trains a separate test model on their own images only.
- Training runs for 100 epochs with early stopping (patience = 10–15).
- The confusion matrix is examined after training — it shows which categories the model confuses with each other.

**Output:** three separate test models (one per person), three confusion matrices, three sets of per-category accuracy scores.

**Gate:** every category must reach ≥60% accuracy (AP ≥ 0.60) on each person's own validation slice. Any category below this threshold indicates a labelling error, not a model capacity problem.

**The diagnostic logic:** if a category fails the gate, the confusion matrix reveals what it is being confused with. Battery confused with metal → review battery labels for metal items that were mislabelled as batteries. Paper confused with cardboard → review the labelling guide boundary between flat paper and corrugated cardboard. The fix is always in the labels, not in the model.

### Phase 4 — Cross-Team Human Audit

**Input:** labels from all three team members

**What happens:**
- Team members compare each other's labels on a shared subset of images.
- Disagreements are identified and resolved through discussion.
- The labelling guide is updated to clarify any edge cases that caused disagreement.

**Gate:** human label agreement must exceed 85% across the audited sample.

**Output:** refined labels, updated labelling guide, resolved edge cases.

### Phase 5 — Automated Label Error Scan (Cleanlab)

**Input:** prediction probability scores exported from Phase 3 models + original labels

**What happens:**
- An automated tool (Cleanlab confident learning algorithm) cross-references each model's probability outputs with the human-assigned labels.
- Images where the model's probability strongly disagrees with the human label are flagged as potential mislabels.
- Flagged images are reviewed by the team and either corrected or removed.

**Output:** a dataset with systematic label noise removed before merging.

**Why automated scanning after human audit:** human reviewers catch obvious disagreements but may share the same blind spots — three people who all made the same labelling mistake will not catch each other's error. The automated scan compares the labels against model behaviour, which is independent of human interpretation. It catches systematic errors that human review misses.

### Phase 6 — Data Merge and Exploratory Analysis

**Input:** all three cleaned, audited, labelled slices

**What happens:**
- All three slices are merged into one combined pool.
- A second duplicate check is run across the combined pool to catch any duplicates that exist across person slices (not within a slice).
- The combined pool is split into training (80%) and validation (20%) sets using stratified random sampling. Stratified means each category is split in the same proportion — not all of one category ends up in training while another ends up mostly in validation.
- A hard cap of 5,000 images per category is applied during splitting. This balances the dataset: food_organic (originally 139,909 images) is capped at 5,000, the same as battery (originally 12,814 images).
- The data leakage check confirms zero images appear in both training and validation sets.

**Output:** clean, split, balanced training and validation sets. Baseline 1 (majority class accuracy = 11.1%) is computed and locked.

**Why the cap at 5,000:** without the cap, food_organic would dominate training. The model would learn to guess "food waste" for uncertain cases because that was the most common answer in training. After capping, all categories have equal weight in training. The model has no reason to favour one category over another.

### Phase 7 — First Full Training Run (Baseline 2)

**Input:** merged, balanced training and validation sets from Phase 6

**What happens:**
- YOLOv8m-seg is trained on the full dataset for 100 epochs using completely default settings — no hyperparameter adjustments of any kind.
- All metrics are recorded: mAP@0.5, mAP@0.5:0.95, precision, recall, F1-score, per-category accuracy, inference speed.

**Output:** Baseline 2 — the untuned benchmark score that all Phase 8 tuning must beat.

**Expected result [SUGGESTED]:** mAP@0.5 in the range 0.58–0.70. Battery category accuracy expected in the range 0.48–0.65.

**Why record a deliberately untuned result:** Baseline 2 provides the measuring stick for Phase 8. Without it, there is no way to prove that tuning improved anything. Every tuning decision in Phase 8 is justified by the improvement it produces over Baseline 2. This is the Lean Six Sigma Measure phase — measure before improving.

### Phase 8 — Hyperparameter Tuning (Master Model Training)

**Input:** Baseline 2 model and metrics, training and validation sets from Phase 6

**What happens:**
- One hyperparameter is changed at a time. The model is retrained and evaluated. If the metric improves over Baseline 2, the change is kept. If it does not, it is reverted.
- Training runs for 300 epochs with early stopping patience = 50.
- A comparison table records every run: which parameter changed, what the new mAP was, whether it beat Baseline 2.

**Tuning sequence:**

| Run | What changes | Why | Expected effect |
|-----|-------------|-----|----------------|
| 1 | Input image size: 640 → 1280 pixels | Larger input = more detail for small objects like batteries | Improve battery and small item accuracy |
| 2 | Category loss weight (`cls`) | Upweight battery and textile — harder, rarer categories | Improve minority category accuracy |
| 3 | Copy-paste augmentation | Synthetically creates overlapping item scenarios during training | Improve performance on piled/overlapping items |
| 4 | Rotation angle (`degrees`) | Trains the model on items at unusual angles | Generalise to odd-angle waste on moving belt |

**Output:** the tuned master model with the highest validation mAP across all runs. The best model file is saved as `best.pt`.

**Target [from literature]:** mAP@0.5 ≥ 0.85 (Midigudla et al., 2025). Battery category accuracy ≥ 0.80 tracked separately.

**Why one parameter at a time:** changing multiple parameters simultaneously makes it impossible to know which change caused the improvement (or degradation). The single-parameter approach produces a traceable, citable record of which engineering decisions contributed to the final model's performance.

### Phase 9 — Generalisation Test on Quarantined Photos

**Input:** 100 real-world photos that have been locked away since Phase 1, never seen by the model during training

**What happens:**
- The Phase 8 best model runs inference on all 100 quarantined photos.
- Accuracy on quarantined photos is compared to accuracy on the validation set used during training.
- The difference is the "generalisation gap."

**Pass/fail criteria:**

| Result | Interpretation | Action |
|--------|---------------|--------|
| Gap < 5% | Suspicious — possible data leakage | Verify quarantine was not contaminated before accepting |
| Gap 5–10% | Normal distribution shift — model generalises well | Deploy |
| Gap > 10% | Model overfitted to training data — does not generalise | Proceed to Phase 10 |
| Any battery false positive | Zero tolerance | Immediate retrain regardless of other metrics |
| False negative rate > 20% | Too many missed items | Retrain |

**Why the quarantine set matters:** a model that scores 90% on its own training and validation data but only 70% on genuinely new photos has memorised, not learned. The quarantine set is the only honest test of real-world performance because it contains photos the model has never influenced — no augmentation, no balancing, no label review based on model feedback.

### Phase 10 — Active Learning Retrain (If Phase 9 Fails)

**Input:** 100 quarantined photos that caused Phase 9 failures, current best model

**What happens:**
- Failed photos are labelled (if not already labelled) and added to the training set.
- Training resumes from the current best model with the backbone layers frozen.
- Learning rate is set very low (lr0 = 0.0005) to make small, targeted updates without disrupting existing knowledge.
- After retraining, the model is re-evaluated on the quarantine set (Phase 9 repeated).

**This cycle repeats until the Phase 9 pass criteria are met.**

**Output:** a model that generalises to real-world photos. Deployment is authorised.

---

## 2.5 Evaluation Framework — What Good Performance Looks Like

### Primary Metrics

| Metric | Target | What it measures |
|--------|--------|-----------------|
| mAP@0.5 | ≥ 0.85 | Detection accuracy — is the AI identifying items correctly and locating them? (at 50% overlap threshold) |
| mAP@0.5:0.95 | ≥ 0.70 | Strict detection accuracy — how precisely does the outline match the actual item boundary? |
| Precision | ≥ 0.85 | Of all items the AI called "recyclable," how many actually were recyclable? |
| Recall | ≥ 0.80 | Of all actual recyclable items, how many did the AI successfully identify? |
| Battery category accuracy | ≥ 0.80 | Tracked separately — cannot be hidden in overall average |
| Inference speed | ≥ 25 FPS | Can the system keep up with the conveyor belt speed? |
| Generalisation gap | ≤ 10% | How much does accuracy drop on photos the model has never seen? |

### The Precision-Recall Trade-off

Precision and recall pull in opposite directions. Increasing one tends to decrease the other.

- **Higher precision** means fewer false alarms — the AI only flags something as recyclable when it is very sure. But this increases the chance of missing real recyclable items (lower recall).
- **Higher recall** means fewer missed items — the AI catches more real recyclable items. But this increases the chance of false alarms (lower precision).

For PurityLoop AI, the priority is **precision over recall**. The reason is the asymmetric error principle: allowing a hazardous item through as recyclable (false positive) has a higher cost than flagging a recyclable item for human review (false negative that becomes a Yellow zone item). The Yellow zone catches false negatives safely. There is no safe catch for false positives on hazardous classes.

### Why Battery Is Tracked Separately

mAP averages accuracy across all categories. If the model scores 0.95 on the 8 non-battery categories but 0.30 on battery, the overall mAP reads approximately 0.87 — which appears to pass the ≥0.85 gate. But a battery accuracy of 0.30 means the model misclassifies 70% of batteries.

This is why battery accuracy is always reported as a separate number alongside overall mAP. The overall number cannot substitute for the safety-critical class metric.

### Overfitting vs Underfitting

| Condition | Sign | Fix |
|-----------|------|-----|
| Overfitting | Training accuracy much higher than validation accuracy (gap > 15%) | Increase regularisation (weight decay), add augmentation, reduce model size |
| Underfitting | Both training and validation accuracy below target | Increase training duration, lower learning rate, unfreeze more model layers |
| Good fit | Training and validation accuracy close, both near target | Proceed to Phase 9 |

---

## 2.6 The Three Baselines — Proving Every Step Adds Value

| Baseline | What it is | What beating it proves |
|----------|-----------|----------------------|
| **Baseline 1 — Blind Guess** | Always predict the most common category. With balanced data: 11.1% accuracy (1 in 9). | Any model trained on this data learned something real — not just class frequency. |
| **Baseline 3 — Solo Diagnostic Runs** | Each person's individual Phase 3 model mAP (0.52–0.76 expected). | Merging all three slices into one dataset improves over any single person's data alone. |
| **Baseline 2 — Untuned Full Run** | Phase 7 model mAP with zero tuning (0.58–0.70 expected). | Phase 8 hyperparameter tuning added measurable, documented value. |

**Reading rule:** the final tuned model must beat all three baselines. If Baseline 2 does not beat Baseline 3, the data merge failed. If the final model does not beat Baseline 2, Phase 8 tuning failed.

---

## 2.7 Deployment Configuration

When the Phase 9 pass criteria are met, the model is deployed as follows:

| Setting | Value | Reason |
|---------|-------|--------|
| Model file | `best.pt` (PyTorch format) | Native format — lowest latency |
| Backup format | ONNX export | CPU-only machines that cannot run PyTorch GPU inference |
| Battery confidence gate | 0.90 (hardcoded, not adjustable) | Safety-critical threshold — operator cannot accidentally lower it |
| Recyclable confidence gate | 0.85 (default, operator-adjustable via slider) | Adjustable for facility-specific operational requirements |
| Input image size | 640×640 pixels (default) or 1280×1280 (if Phase 8 tuning selected this) | Determined by Phase 8 best result |
| Inference device | GPU (primary), CPU (fallback) | Automatic device selection at startup |

**What "hardcoded battery threshold" means in practice:** the operator dashboard has a confidence threshold slider. Moving it changes how strictly the system handles recyclable categories. However, the slider has no effect on the battery threshold — that is set in the code and cannot be changed from the dashboard. This prevents accidental lowering of the safety threshold during normal operation.

---

## 2.8 Deep Learning Framework Slide-Ready Summary

**Slide Title:** Deep Learning Pipeline — How the AI Is Built and Verified

**On the slide:**

**The model:** YOLOv8m-seg — a pre-trained visual recognition model fine-tuned on 45,000 waste images across 9 categories.

**3 internal layers:**

| Layer | Role |
|-------|------|
| Visual Processing | Reads the photo — detects edges, textures, shapes at multiple scales |
| Scale Combiner | Merges detail from multiple zoom levels — catches both tiny batteries and large boxes |
| Decision Head | Outputs: category + certainty score + precise item outline |

**10-phase build pipeline:**

| Phases | Stage | Key gate |
|--------|-------|----------|
| 1–5 | Prepare clean labelled data | ≥85% team label agreement, ≥60% per-category accuracy in solo runs |
| 6–8 | Train and tune the model | Each tuning run must beat Baseline 2 |
| 9–10 | Test on unseen real-world photos | Accuracy drop ≤10%, zero battery false positives |

**3 baselines that must all be beaten:**

```
Blind guess (11.1%) → Solo runs (0.52–0.76) → Untuned full run (0.58–0.70) → Final target (≥0.85)
```

**Speaker notes:**

The key framing for Dr. Narishah: this is not "we trained a model and hoped for the best." Every decision has a rationale, every result is compared to a documented benchmark, every tuning change is recorded and justified. This maps exactly to DMAIC: Define (problem + 9 classes), Measure (3 baselines), Analyze (model selection + architecture choice), Improve (Phase 8 tuning), Control (Phase 9 generalisation gate + active learning loop).

She will likely ask why YOLOv8 over alternatives — cite Midigudla et al. (2025) directly: "YOLOv8 achieved greater than 85% mAP on waste classification, outperforming EfficientDet and Detectron2 in both accuracy and inference speed."

She may ask what the model backbone does — say: "The backbone is the part that reads the image and identifies visual patterns. We use a pre-trained backbone so the model already knows how to see general objects. We only train the final layers to specialise in waste categories. This is why we need 45,000 images instead of millions."

---

**[GEMINI PROMPT — Deep Learning Framework Visual]**

A clean three-layer model architecture diagram on white background. Three horizontal blocks stacked vertically with downward arrows. Top block (lightest green): "Layer 1 — Visual Processing: reads photo, finds edges, textures, shapes at multiple zoom levels". Middle block (medium green): "Layer 2 — Scale Combiner: merges close-up and wide-view features into one understanding". Bottom block (darkest green): "Layer 3 — Decision Head: outputs category + certainty score + item outline". To the right of the diagram: a small input photo (conveyor belt items) on the top, and at the bottom: three output bubbles — "Category: plastic", "Certainty: 91%", "Outline: [mask]". Flat design, emerald green (#0F5132) colour scheme, white background, corporate presentation style.

---

**[GEMINI PROMPT — 10-Phase Pipeline Visual]**

A clean horizontal three-stage pipeline diagram on white background. Stage 1 (light green, phases 1-5): "Prepare Clean Data — label, audit, remove errors". Stage 2 (medium green, phases 6-8): "Train and Tune — merge, benchmark, optimise". Stage 3 (dark green, phases 9-10): "Test and Deploy — real-world photos, active learning". Each stage has a pass gate diamond between stages labelled "Gate: pass or go back". Below each stage: key gate condition in small text. A final lock icon at the end labelled "Deploy". Emerald green gradient across stages, white background, flat corporate design.

---

---

# APPENDIX — FRAMEWORK COMPARISON: HITL vs DL

| Dimension | HITL Framework | Deep Learning Framework |
|-----------|---------------|------------------------|
| **Primary purpose** | Keep humans in control of uncertain decisions | Build and validate the AI model itself |
| **Operates at** | Two levels: build-time (labelling) and runtime (Yellow zone) | 10 sequential phases from data to deployment |
| **Key quality gate** | ≥85% human label agreement (Phase 4); 100-correction retrain trigger (runtime) | Phase 9: ≤10% generalisation gap; zero battery false positives |
| **What it produces** | Clean labelled data (build-time); corrected detections + training data (runtime) | `best.pt` — the trained model file deployed in the web application |
| **Failure action** | Re-label, re-audit, re-run the affected phase | Go back to the failed phase gate, fix, re-run |
| **DMAIC phase** | Measure (Phase 4 audit) + Control (active learning loop) | Measure (baselines) + Analyze (model choice) + Improve (tuning) + Control (Phase 9) |
| **Responsible team member** | Person C owns Phase 4 merge pipeline; facility operator owns runtime review | Talvin owns training pipeline; Naomi owns data splits |
| **Self-improving?** | Yes — runtime corrections accumulate and trigger retrains | Yes — Phase 10 active learning retrains from failure cases |

---

## Key Question Dr. Narishah Is Likely to Ask About Both Frameworks

**On HITL:**
> "What happens if the operator always clicks Confirm without really checking?"

Answer: operator fatigue is a known HITL risk. Two mitigations in the design: (1) the system logs the time between Yellow zone display and operator decision — very fast confirmations flag possible rubber-stamping; (2) active learning retrains include the operator-confirmed labels, so consistently wrong confirmations will degrade model performance and become visible in the next Phase 9 evaluation. The retrain outcome is the audit mechanism.

**On Deep Learning:**
> "How do you know the model is not just memorising the training photos?"

Answer: three mechanisms prevent memorisation. First, the data is deduplicated so no photo appears twice. Second, the training and validation sets have zero overlap — validation accuracy measures performance on photos the model never trained on. Third, Phase 9 releases 100 completely unseen real-world photos. If the model was memorising, its accuracy would collapse on these photos. The ≤10% generalisation gap requirement is the formal test of this.

---

*PurityLoop AI Capstone AY2025/26*
*HITL & Deep Learning Framework Document*
*Written: 2026-06-04 | Talvin (ML R&D)*
*Citations: Midigudla et al. (2025) · Menke et al. (2024) · Mosqueira-Rey et al. (2023) · Moh & Abd Manaf (2017)*
