# PurityLoop AI — CVAT Annotation Guide & Success Metrics

This document outlines the dataset annotation requirements using CVAT and the success metrics established for the three AI engineers and the overall model.

![Team Success Metrics Dashboard](/Users/chris/Documents/Capstone/success_metrics_dashboard.png)

---

## 1. Determining Which Datasets Require Annotations using CVAT

Since PurityLoop AI is trained on a **YOLOv8m-seg (instance segmentation)** architecture, every training image must have a precise polygon boundary (mask) rather than just a bounding box or classification tag.

Based on the [DATASET_REFERENCE.md](file:///Users/chris/Documents/Capstone/DATASET_REFERENCE.md#L7-L30) master list, you can identify which datasets need attention in CVAT:

1. **`Classif → pseudo-seg` (High Priority for CVAT Review & Refinement)**
   * **Datasets:** *TrashNet*, *Garbage Classification v2*, *Waste Classification 25k*, *RealWaste*, *Unified Waste*, etc.
   * **Status:** These datasets only contain image-level categories. They were converted to segmentations using automated scripts that generated rough "pseudo-segmentation" boxes.
   * **Action:** Import these into **CVAT** and use AI annotation tools (such as **Segment Anything Model - SAM**) to refine the masks. Focus heavily on the **Battery** class (Chris) and **Textiles** (Talvin) to clean up boundary lines.
2. **`YOLO det bbox` (Requires CVAT Annotation)**
   * **Datasets:** *Chinese Trash Detection*, *Garbage Detection*.
   * **Status:** These contain bounding box coordinates (rectangles) but no polygon shapes.
   * **Action:** Load these into CVAT to convert bounding boxes into precise polygon masks.
3. **Active Learning Failure Cases (Phase 10)**
   * **Status:** Edge cases, false positives, or operator-corrected samples collected during system runtime.
   * **Action:** These must be imported into CVAT for manual review and annotation before model fine-tuning.

---

## 2. Success Metrics

### 2.1 Individual & Team Success Metrics (Phase 3 & Phase 4)

Refer to [PURITYLOOP_PLAYBOOK.md:L253-311](file:///Users/chris/Documents/Capstone/PURITYLOOP_PLAYBOOK.md#L253-L311) and [03_METHODOLOGY.md:L146-155](file:///Users/chris/Documents/Capstone/03_METHODOLOGY.md#L146-L155) for the diagnostic and audit rules:

* **Diagnostic Pass Gate (Phase 3):**
  Each engineer trains a short individual diagnostic model on their assigned categories/datasets. **Every class must reach an Average Precision (AP) ≥ 0.60** on their localized validation photos. Any class below 0.60 triggers a targeted re-annotation sprint.
* **Expected Diagnostic Performance Ranges:**
  * **Naomi** (Group 1: plastic, paper, cardboard): **60–72% mAP@0.5**
  * **Chris (You)** (Group 2: food, battery, trash): **64–76% mAP@0.5**
  * **Talvin** (Group 3: metal, glass, textile): **48–62% mAP@0.5** *(lower range expected due to odd angles and piled landfill environments)*
* **Cross-Team Audit Gate (Phase 4):**
  To verify consistency among annotators:
  * **Category Agreement:** Must reach **≥ 85%** across a shared audited sample.
  * **Outline Overlap (Mask IoU):** Must exceed **0.75** (segmentation masks must cover at least 75% of the same pixels).

---

## 2.2 Overall Model Success Metrics (Phase 8 & Phase 9)

Refer to [03_METHODOLOGY.md:L174-185](file:///Users/chris/Documents/Capstone/03_METHODOLOGY.md#L174-L185) and [PURITYLOOP_PLAYBOOK.md:L645-675](file:///Users/chris/Documents/Capstone/PURITYLOOP_PLAYBOOK.md#L645-L675):

| Metric | Target Value | Verification Source |
|---|---|---|
| **mAP@0.5** (Primary Accuracy) | **≥ 0.85 (85%)** | Computed via `ultralytics val()` on Test Set |
| **mAP@0.5:0.95** (Boundary Precision) | **≥ 0.70 (70%)** | Computed via `ultralytics val()` on Test Set |
| **F1-Score** (Precision/Recall Balance) | **≥ 0.82** | Harmonic mean on Test Set |
| **Generalisation Gap** | **≤ 10%** | Difference between Phase 8 Validation and Phase 9 Quarantine Test accuracy |
| **Battery Class Recall** | **≥ 0.90 (90%)** | Safety Quality Gate during model validation |
| **Battery Quarantine Error Rate** | **Zero-Tolerance** | Zero false negatives allowed for the Battery class on the held-out quarantine test |
| **Inference Speed** | **≥ 25 FPS** | Latency ≤ 500ms on demo hardware |
| **Purity Rate Accuracy** | **±2%** | Comparison of system-reported vs. ground-truth purity |
