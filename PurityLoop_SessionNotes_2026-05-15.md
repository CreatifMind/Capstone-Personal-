# PurityLoop AI — Session Notes
**Date:** 2026-05-15
**Context:** Playbook v3 breakdown + Dr. Narishah feedback debrief

---

## 1. Model Development Process (7 Phases)

1. **Align** → agree 9 classes, write label guide, edge case rules
2. **Parallel dataset work** → each person labels own slice
3. **Individual diagnostic training** → 50 epochs, find label bugs per person
4. **Quality gate** → fix bugs, re-run if fail (class AP < 0.60 = re-label)
5. **Merge** → cross-audit → Cleanlab algorithmic check → one 80/20 split on combined pool
6. **Final training** → baseline → tune one param at a time
7. **Deploy** → Streamlit + SQLite

3 people → 1 model. Individual runs = QC gate only, not final output.

---

## 2. DL Framework

- **Library:** Ultralytics YOLOv8
- **Model:** `yolov8m-seg.pt`
- **Single inference pass** → bounding box + class label + confidence + pixel mask
- No ensemble. One model.

---

## 3. Model Configuration

| Param | Value |
|---|---|
| `epochs` | 100 |
| `patience` | 20 |
| `batch` | 16 |
| `imgsz` | 640 |
| `lr0` | 0.01 |
| `momentum` | 0.937 |
| `weight_decay` | 0.0005 |
| `overlap_mask` | True |
| `mask_ratio` | 4 |

---

## 4. Hyperparameter Tuning — Terms Explained

**Protocol: 1 change per run. Record baseline first. Never change 2 params simultaneously.**

| Param | Default → Try | Plain meaning | Analogy |
|---|---|---|---|
| `imgsz` | 640 → 800 | Input resolution | More pixels = model sees battery more clearly |
| `cls` | 0.5 → 0.75 | Classification loss weight | Raise = model penalised harder for wrong class label |
| `copy_paste` | 0 → 0.1 | Synthetic minority class boost | Cut battery from one photo, paste onto another = fake-but-valid training data |
| `weight_decay` | 0.0005 → 0.001 | Overfitting brake | Penalises memorising. Raise if train-val gap > 10% |
| `degrees` | 0 → 10 | Random rotation ±10° during training | Teach model to recognise rotated waste on conveyor |
| `flipud` | 0 → 0.3 | Vertical flip 30% probability | Bottle is still bottle upside down |
| `lr0` | 0.01 | Learning rate | Step size toward lowest loss. Don't touch for baseline. |
| `patience` | 20 | Early stopping | Stop if no val mAP improvement after 20 epochs |
| `mosaic` | 1.0 | 4 images combined per step | Forces model to detect in cluttered multi-item scenes |

---

## 5. Evaluation Metrics — Terms Explained

### mAP50
- Mean Average Precision at IoU threshold 0.50
- IoU = overlap area ÷ total combined area between predicted box and ground truth box
- Detection counts correct if IoU ≥ 0.50 AND class matches
- Averaged across all 9 classes
- **Target: ≥ 0.82**

### mAP50-95
- Same but averaged across IoU 0.50 to 0.95 (stricter)
- Always lower than mAP50
- **Target: ≥ 0.60**

### Precision
- TP ÷ (TP + FP) — of all detections made, how many were correct?
- **Battery precision must be ≥ 0.85** — battery misclassified as plastic = contamination event
- Analogy: doctor diagnoses 100 patients with cancer. 90 actually have it. Precision = 90%.

### Recall
- TP ÷ (TP + FN) — of all real objects, how many did model find?
- **Target: ≥ 0.75 overall**
- Missed battery → amber queue → human review → still caught. Acceptable.
- Battery classified as plastic → passes green zone → contaminates batch. NOT acceptable.
- **Precision > Recall** for this project.

### F1 Score
- 2 × (Precision × Recall) ÷ (Precision + Recall)
- Peak F1 on F1_curve.png = best balanced confidence threshold

### Mask mAP50-M
- Same as mAP50 but checks pixel mask overlap, not box overlap
- Measures segmentation boundary quality
- **Target: ≥ 0.70**

---

## 6. Baselines — What They Are and Why Both Matter

### Baseline 1 — Majority Class (Dumb Baseline)
- No model. Pure statistics. Count most common class → guess it forever.
- Formula: most common class count ÷ total images
- Analogy: student writes "C" for every answer because most answers historically were C. Zero understanding.
- Beats this → model learned something real, not just class frequency

### Baseline 2 — Off-the-Shelf YOLOv8 (No Fine-Tuning)
- Real model, real inference, zero domain knowledge
- COCO-trained weights only. Thinks in "person, car, dog" not "battery, plastic, cardboard"
- Analogy: student studied wrong textbook. Applies real knowledge, wrong domain.
- Beats this → proves fine-tuning on waste data added value beyond COCO pretraining

### Baseline 3 — Individual Person Diagnostic Models
- mAP from each person's Phase 3 run (own slice only)
- Merged model must beat all 3. If not → merge introduced poison.

| Baseline | Beats it → proves |
|---|---|
| B1 | Model learned something real, not just class frequency |
| B2 | Fine-tuning added domain-specific value |
| B3 | Merging all slices improved over any individual slice |

---

## 7. Model Generalization

- Val mAP = performance on dataset (optimistic)
- Deployment mAP = performance on real showcase environment (always lower)
- Collect 50–100 showcase-environment images → label → run `model.val()` → report both
- Gap 5–10% = normal. Gap >20% = training data doesn't match real world.
- Report both numbers to supervisor. Hiding the gap = academic dishonesty.

---

## 8. Dr. Narishah Feedback — 2026-05-15

### What She Said
- Web requirements: upload image → link to `best.pt` → output visualization
- Point of Integration (POI) = most difficult part
- Requirement gathering = WHAT. Requirement analysis = HOW.
- Split into: Web dev | DL model | Visualization → POI → Deployment
- DL methodology must map to waterfall / six sigma / DMAIC
- Justify YOLOv8 vs alternatives
- "Annotated means no value, nothing new" — need model comparison, not just annotation
- Model 1 (detection) + Model 2 (segmentation) → integrate
- Segmentation lives inside bounding box — annotation inside box is the difficult part
- Baseline = benchmark. Model comparison = tuning. Show which config is best.
- Sample size justification
- Generalization testing required
- Object identification = classification task

### What She Actually Wants

**Her DMAIC lens on your project:**

| DMAIC | Mapping |
|---|---|
| Define | Contamination problem in recycling |
| Measure | Baseline mAP (off-shelf + majority class) |
| Analyze | Model comparison table — which config wins, why |
| Improve | Best confirmed config with evidence |
| Control | Deployment + generalization test + active learning loop |

### Architecture She Wants Documented

```
Frontend:  Streamlit UI (upload, display, ESG panel)
Backend:   Python inference pipeline (YOLOv8 → routing logic)
Model:     best.pt (trained weights)
DB:        SQLite (detections table, amber_queue table)
```

### Point of Integration Diagram

```
[Image Upload] → [Streamlit Frontend]
                       ↓
              [YOLO Inference Engine]  ← best.pt loaded here
                       ↓
              [3-Zone Routing Logic]
                       ↓
         [SQLite Logger] + [Visualization Output]
```

### Deliverables — Priority Order

| Priority | Deliverable |
|---|---|
| 🔴 1 | System framework diagram (SVRA-style: problem → framework → components → validation) |
| 🔴 2 | Functional + non-functional requirements list |
| 🔴 3 | Model comparison table (baseline vs tuned variants, mAP side by side) |
| 🔴 4 | POI diagram (upload → inference → DB → output, labelled handoffs) |
| 🔴 5 | DB schema diagram (detections table + amber_queue) |
| 🟡 6 | Sample size justification per class with citation |
| 🟡 7 | Generalization gap report (val mAP vs showcase mAP) |
| 🟡 8 | YOLOv8 justification vs alternatives (cite Midigudla 2025 + Sapkota 2025) |
| 🟡 9 | DL methodology mapped to DMAIC or waterfall |
| 🟢 10 | RPA/hot folder script with error handling |

### What Will Fail You (Per Her Research DNA)

| Hard fail | Why |
|---|---|
| Technical decision with no citation | She cites everything — expects same |
| "Our model is accurate" without numbers | LSS = measure or it doesn't count |
| Framework diagram missing | She always draws framework first (SVRA paper) |
| Annotation work with no model comparison | "Nothing new" — contribution must be in the comparison |
| Team can't answer questions on each other's layers | 6 people = 6 knowledge owners |

### Strongest Move Against Her

Her SVRA paper (2022) = automation framework improving ERP processes.
Your project = automation framework improving recycling processes.
Same structure, different domain. Mirror her paper structure:

1. Problem context → why manual sorting fails
2. PurityLoop framework diagram → CV layer + app layer + dashboard layer
3. Phase breakdown → detection → decision logic → output
4. Evaluation plan → mAP + purity rate improvement

---

## 9. Key Decisions / Principles

- **Precision > Recall** — battery false positive ruins entire batch
- **3-zone system** — Green (≥0.85 confident recyclable) / Red (≥0.85 hazardous) / Amber (uncertain → human review)
- **Amber zone** = contamination firewall — requires model failure AND human failure simultaneously
- **One 80/20 split on combined pool** — not per-person. Prevents artificially inflated val mAP.
- **Data leakage check** must show 0 duplicates between train and val sets
- **Cleanlab audit before any paid cloud training** — catching systematic label error algorithmically = free

---

*Session: 2026-05-15 | Model: claude-sonnet-4-6 | Project: PurityLoop AI Capstone*
