# PurityLoop AI — Project Framework
### Automated Waste Sorting & Contamination Detection
**Sunway University · Department of Business Analytics · Capstone Project**
**Supervisor: Dr. Narishah Mohamed Salleh**

> Framework structure modelled after Tang et al. (2022) conceptual framework methodology.
> All decisions cited by peer-reviewed journals. Scopus Q1/Q2, published 2020+.

---

## 1. PROBLEM CONTEXT (DMAIC: DEFINE)

Manual waste sorting in recycling facilities is error-prone, slow, and produces inconsistent purity levels in recyclable material bales. Contaminated bales reduce resale value, increase landfill diversion failure, and prevent accurate operational performance auditing for operational reporting.

**Baseline (DMAIC Measure):** Malaysian recycling facilities operating under manual sorting show contamination rates of approximately 30% of processed waste (Moh & Abd Manaf, 2017). This baseline constitutes the pre-system state against which PurityLoop AI improvement is measured.

**Target:** 30–40% increase in sorting throughput. Purity rate improvement from ~70% to ≥90% post-deployment.

**Business impact:** Contaminated bales = unsaleable material = lost revenue + missed material recovery value + failed process audit trail.

---

## 2. LITERATURE GAP

| Existing approach | Limitation | How PurityLoop addresses it |
|------------------|-----------|----------------------------|
| Manual sorting | Human error, slow, hazardous for battery/e-waste | Automated CV pipeline removes human from sorting loop |
| Single-stage detection only | No recovery mechanism for low-confidence / occluded items | Two-stage: detect → segment-on-MAYBE (Nayfeh et al., 2025) |
| Static model deployment | Model degrades as waste categories evolve | Active learning loop retrains at 100-sample threshold (Menke et al., 2024) |
| operations reported qualitatively | No traceable per-item material yield data | Material-level weight from Yield emission factors (JEM, 2024) |
| Binary recyclable/non-recyclable only | Misses hazardous class (battery) — safety risk | 8-class taxonomy with Battery as dedicated hazard class |

---

## 3. DMAIC ALIGNMENT
*Methodology grounded in Pongboonchai-Empl et al. (2023): integration of Industry 4.0 technologies into Lean Six Sigma DMAIC.*

| Phase | PurityLoop Content | Evidence / KPI |
|-------|-------------------|----------------|
| **Define** | Problem: 30% contamination under manual sorting. Scope: PurityLoop AI for recycling facility automation. | Moh & Abd Manaf (2017) |
| **Measure** | Baseline: contamination rate ~30% manual. Target: purity rate ≥90%. Speed: ≥25 FPS real-time. Accuracy: mAP@0.5 ≥ 0.85. | Midigudla et al. (2025); Abo-Zahhad et al. (2025) |
| **Analyze** | Why CV over manual sensors: real-time multi-class, scalable, traceable. Why YOLOv8 over EfficientDet/Detectron2: higher mAP, faster inference, anchor-free. | Midigudla et al. (2025); Terven et al. (2023) |
| **Improve** | PurityLoop AI system: dual CV pipeline + decision logic + SQLite + dashboard + user app. | See Section 4 framework diagram |
| **Control** | Live purity rate dashboard. Active learning quarterly retrain. Alert system for hazardous items. | Menke et al. (2024); Pongboonchai-Empl et al. (2023) |

---

## 4. PROPOSED FRAMEWORK

*See PurityLoop_Diagram.md for full Mermaid system architecture diagram.*

The PurityLoop AI framework operates across five integrated layers:

```
LAYER 0 — PROBLEM CONTEXT
        ↓
LAYER 1 — DATA ACQUISITION (RPA Hot Folder)
        ↓
LAYER 2 — CV PIPELINE (Detection → Segmentation → Decision)
        ↓
LAYER 3 — CLASSIFICATION & CALCULATION
        ↓
LAYER 4 — BUSINESS OUTPUT (Dashboard + App + ESG Report)
        ↑
LAYER 5 — ACTIVE LEARNING LOOP (MAYBE → Retrain → Layer 2)
```

**Design rationale:** Hybrid two-stage CV architecture (Layer A detection + Layer B conditional segmentation) mirrors the hybrid methodology approach validated by Nayfeh et al. (2025). Combining two complementary techniques with explicit trigger conditions produces a more robust pipeline than single-stage detection alone, particularly for real-world waste which is frequently damaged, occluded, or overlapping.

---

## 5. COMPONENT BREAKDOWN

### 5.1 Layer 1 — Data Acquisition

| Component | Specification | Justification |
|-----------|--------------|---------------|
| Input source | Simulated conveyor belt camera / hot folder | Demo environment proxy for industrial camera |
| Python RPA script | File watcher (watchdog library) + format validator | Automation pipeline robustness; Tang et al. (2022) |
| Error handling | Non-image files → log + skip. Corrupt files → quarantine folder. Empty folder → idle state. | RPA robustness standard; Tang et al. (2022) |
| Supported formats | .jpg, .jpeg, .png, .bmp | Standard camera output formats |

**Functional requirements:**
- FR1: System shall detect new files in hot folder within 500ms.
- FR2: System shall reject non-image files and log rejection with timestamp.
- FR3: System shall pass valid images to CV pipeline within 1 second.

**Non-functional requirements:**
- NFR1: System shall process ≥25 frames per second on T4 GPU hardware.
- NFR2: System shall maintain uptime ≥99% during showcase demo window.

---

### 5.2 Layer 2 — CV Pipeline (Hybrid Two-Stage)

#### Stage A: Object Detection (YOLOv8s)

**Model selection:** YOLOv8s over alternatives justified by Midigudla et al. (2025) — comparative analysis shows YOLOv8 achieves mAP >85% on waste classification, outperforming EfficientDet and Detectron2 in both accuracy and inference speed. YOLOv8 anchor-free head reduces false positives on irregular shapes (Terven et al., 2023). YOLOv8s selected over larger variants (m/l/x) due to Google Colab free tier constraint (T4 16GB VRAM; batch 16 maximum).

**Architecture components:**
- Backbone: CSP-DarkNet — hierarchical feature extraction (Terven et al., 2023)
- Neck: FPN + PAN — multi-scale feature aggregation for small object detection (Lu et al., 2023)
- Head: Decoupled anchor-free — separate classification and localisation branches

**Training parameters (Ajayi et al., 2024):**

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Image size | 640×640 px | YOLOv8 native resolution; smaller = miss small objects (battery); larger = OOM on Colab |
| Batch size | 16 | Maximum for T4 16GB VRAM with YOLOv8s |
| Epochs | 100 | Standard for fine-tuning pretrained weights; early stop patience=20 |
| Learning rate | 0.01 initial, cosine decay | Validated for YOLOv8 convergence by Ajayi et al. (2024) |
| Optimizer | AdamW | Decoupled weight decay; standard for fine-tuning (Ajayi et al., 2024) |
| Weight decay | 0.0005 | L2 regularisation; prevents overfitting on ~44k image dataset |
| Pretrained weights | COCO | Transfer learning from COCO backbone; Zhang et al. (2021) |

**Class imbalance handling:**
Battery class has significantly fewer samples than plastic. Automatically weighted focal loss (Mahmoodi et al., 2025) dynamically up-weights underrepresented classes per epoch, preventing model from ignoring rare hazard classes.

#### Stage B: Instance Segmentation (YOLOv8s-seg) — Conditional

Triggered only for MAYBE detections (confidence 0.40–0.74). Pixel-level masks recover shape information from damaged or overlapping waste items. Justified by Nayfeh et al. (2025) two-stage architecture validation. Running segmentation on all frames incurs ~33% speed penalty; conditional triggering maintains overall pipeline at ≥25 FPS.

**Decision routing (Chen et al., 2025):**

| Score | Decision | Action |
|-------|----------|--------|
| ≥ 0.75 | YES | Accept, classify, calculate, log |
| 0.40–0.74 | MAYBE | Trigger Stage B segmentation |
| < 0.40 | NO | Discard as background, no log |

---

### 5.3 Layer 3 — Classification & Calculation

**Unified 8-class taxonomy:**

| Class | Category | Alert |
|-------|----------|-------|
| PET Plastic | Recyclable | None |
| HDPE Plastic | Recyclable | None |
| Aluminum | Recyclable | None |
| Paper | Recyclable | None |
| Cardboard | Recyclable | None |
| Glass | Recyclable | None |
| Battery | Hazardous | RED — immediate quarantine |
| Food Waste / General Trash | Non-Recyclable | Contamination penalty |

**Purity Rate:**
```
Purity Rate (%) = (Recyclable_items / Total_items_detected) × 100
```

**Recovered Weight formula:**
```
Recovered_Weight (kg) = Σ [item_count_i × average_weight_i] × Purity_Factor
```
Where:
- item_count_i = count of items in category i
- average_weight_i = average class weight constant (kg) — fixed per class (e.g., PET bottle avg = 0.025 kg)
- Purity_Factor = Purity Rate (decimal) — penalises contaminated batches

**Weight estimation method:** Camera cannot measure mass directly. Class-average weight constants used as proxy. This is acknowledged as a limitation in Section 8.

---

### 5.4 Layer 4 — Business Output

| Output | Tool | KPI tracked |
|--------|------|-------------|
| Live dashboard | Power BI / Tableau | Purity Rate %, weight processed, Material Yield kg, Revenue estimate |
| Audit trail | SQLite | All detections timestamped with class, confidence, decision |
| User app | Mobile web (responsive) | Personal purity score, Eco-Credits, contamination feedback |
| operational report | Power BI export | Corporate carbon audit documentation |

Dashboard KPI targets (DMAIC Control):

| KPI | Baseline | Target | Measurement |
|-----|----------|--------|-------------|
| Purity Rate | ~70% (manual) | ≥90% | Per session, per bale |
| Detection Speed | N/A | ≥25 FPS | Frames per second |
| mAP@0.5 | N/A | ≥0.85 | Validation set |
| weight processed | 0 (no tracking) | Calculated per session | kg weight per kg processed |

---

### 5.5 Layer 5 — Active Learning Loop

MAYBE detections accumulate in a review pool. At 100-sample threshold, DataOps team member reviews and confirms or corrects labels. Confirmed labels added to training dataset. Model retrained on updated dataset. Scheduled quarterly model review regardless of sample count (Pongboonchai-Empl et al., 2023).

**Justification:** Active learning reduces annotation cost while continuously improving model performance on domain-specific edge cases (Menke et al., 2024). Eliminates model freeze-frame problem where accuracy degrades as real-world waste categories evolve.

---

## 6. DATASET STRATEGY

*Reference: PurityLoop_Diagram.md — Unified 8-Class Taxonomy*

| Priority | Dataset | Images | Classes | Format | Why |
|----------|---------|--------|---------|--------|-----|
| P1 | Garbage Classification v2 (Kaggle) | 19,762 | 10 | Standard | Only public dataset with Battery class — critical for hazard detection |
| P1 | Trash Detection (Roboflow) | 2,800 | 64 | YOLOv8 ready | Pre-labelled in YOLOv8 txt format — zero annotation conversion |
| P2 | TrashNet (Kaggle) | 2,527 | 6 | Standard | Established academic baseline; widely cited |
| P2 | RealWaste (Kaggle) | 4,752 | 9 | Standard | Real-world landfill images — increases domain realism |

**Total P1+P2: ~29,841 images**

**Data preparation pipeline:**
1. Standardise all annotations to YOLOv8 txt format (class_id cx cy w h normalised)
2. Map all dataset classes → unified 8-class taxonomy (class harmonisation)
3. Train/Val/Test split: 70% / 15% / 15% stratified by class
4. Augmentation: Mosaic (4-image tile), horizontal flip, scale jitter ±50%, HSV colour shift (Ajayi et al., 2024)
5. Checkpoint to Google Drive every 5 epochs (Colab runtime protection)

**Transfer learning justification:** ~30k images insufficient for scratch training of a deep CNN. COCO-pretrained YOLOv8s backbone already encodes general visual features (edges, textures, shapes). Fine-tuning converges in ~100 epochs vs ~300+ for scratch training (Zhang et al., 2021).

---

## 7. MODEL EVALUATION

**Primary metrics (Midigudla et al., 2025; Abo-Zahhad et al., 2025):**

| Metric | Target | What it measures |
|--------|--------|-----------------|
| mAP@0.5 | ≥ 0.85 | Detection accuracy at IoU threshold 0.5 |
| mAP@0.5:0.95 | ≥ 0.60 | Stricter benchmark — localisation quality |
| Precision | ≥ 0.85 | Of predicted positives: how many correct |
| Recall | ≥ 0.80 | Of actual positives: how many caught |
| F1-Score | ≥ 0.82 | Harmonic mean of Precision and Recall |
| FPS | ≥ 25 | Real-time viability on demo hardware |
| Battery class AP | Report separately | Safety-critical class — cannot be aggregated into mAP only |

**Benchmark baseline:** Midigudla et al. (2025) reports YOLOv8 achieves mAP >85% on waste classification. Abo-Zahhad et al. (2025) shows YOLOv8s achieves 44.9 mAP vs YOLOv5s 37.4 mAP on COCO benchmark (+7.5 mAP improvement).

**Overfitting detection:**
- Overfitting: Training mAP − Validation mAP > 15% → increase weight decay, add augmentation
- Underfitting: Both train + val mAP < 0.60 → increase epochs, lower LR, unfreeze more layers

**Addressing false signals:**
- False positives (non-recyclable flagged as recyclable): raise YES threshold (0.75 → 0.80)
- False negatives (contaminant missed): lower MAYBE floor (0.40 → 0.35); add class weight for contaminant
- Duplicate detections: tune NMS IoU threshold (default 0.45 → 0.35 for dense waste)

---

## 8. MODEL GENERALISATION

The PurityLoop AI backbone, once trained on waste domain, encodes feature representations for irregular-shaped, variable-material objects under varied lighting conditions. These features transfer to analogous industrial applications with minimal retraining:

| Industry | Application | Feature transfer | Retraining needed |
|----------|-------------|-----------------|-------------------|
| F&B manufacturing | Foreign object detection on conveyor | Shape + texture detection of irregular items | Head layer only; ~500 labelled images |
| Hospital waste management | Sharps / biohazard separation | Hazard class detection logic (Battery → Sharps) | Head layer + new classes |
| Construction site | Debris classification | Large irregular object detection | Head + domain-specific augmentation |
| Retail quality control | Damaged SKU detection | Defect boundary detection from segmentation layer | Head layer only |

**Justification:** Transfer learning approach (Zhang et al., 2021) preserves backbone feature weights. New domain requires only head retraining — reduces new deployment from 30k labelled images to ~500–1,000.

---

## 9. LIMITATIONS

1. **Weight estimation:** Formula requires kg mass per item. Camera cannot measure weight. Class-average weight constants used as proxy. Introduces ±15–30% error in weight calculation. Future work: integrate load cell sensor on conveyor.
2. **Indoor dataset bias:** Training data (TrashNet, Garbage Classification v2) composed primarily of studio/clean images. RealWaste dataset partially addresses this. Model may underperform on heavily soiled or unusual waste configurations.
3. **Styrofoam gap:** No current dataset source includes Styrofoam as a dedicated class. Classified under General Trash. Future work: collect and annotate Styrofoam samples.
4. **Malaysia-specific emission factors:** Yield emission factors sourced from European/US-origin datasets (JEM, 2024). Malaysian energy mix and recycling infrastructure may differ. Future work: validate against MyHIJAU or mgmt Malaysia-specific data.
5. **Demo vs production:** Hot folder ingestion simulates industrial camera. Production deployment requires edge GPU hardware (NVIDIA Jetson or equivalent) and camera integration.
6. **Google Colab free tier:** Training constrained by T4 availability and 12-hour runtime. Checkpointing to Drive required. YOLOv8l/x not feasible — YOLOv8s selected as practical compromise.

---

## 10. FUTURE WORK

1. Upgrade to YOLOv8m or YOLOv8l post-Colab Pro / cloud GPU access for mAP improvement
2. Add conveyor belt load cell for real-time weight measurement → eliminate weight constant approximation
3. Collect Malaysia-specific waste images → domain adaptation fine-tuning
4. ERP integration: push audit trail directly to SAGE X3 or SAP for automated operational reporting (Tang et al., 2022)
5. Edge deployment: export model to ONNX → TensorRT for Jetson Nano deployment at production facility

---

## REFERENCES

Abo-Zahhad, M. M., & Abo-Zahhad, M. (2025). Real time intelligent garbage monitoring and efficient collection using YOLOv8 and YOLOv5 deep learning models for environmental sustainability. *Scientific Reports*, *15*(1), 16024. https://doi.org/10.1038/s41598-025-99885-x

Ajayi, O. G., Ibrahim, P. O., & Adegboyega, O. S. (2024). Effect of hyperparameter tuning on the performance of YOLOv8 for multi crop classification on UAV images. *Applied Sciences*, *14*(13), 5708. https://doi.org/10.3390/app14135708

Author(s) TBC. (2024). Recycling packaging waste from residual waste reduces operational waste inefficiencies. *Journal of Environmental Management*. https://doi.org/10.1016/j.jenvman.2024 [VERIFY full citation at ScienceDirect pii/S0301479724030147]

Chen, W., Yang, J. S., Xia, C., Li, Y., & Xiao, X. (2025). Road surface damage detection based on enhanced YOLOv8. *Computers in Industry*, *173*, 104363. https://doi.org/10.1016/j.compind.2025.104363

Lu, Y., Su, M., Wang, Y., Lu, X., & Jia, F. (2023). Learning discriminated features based on feature pyramid networks and attention for multi-scale object detection. *Cognitive Computation*, *15*, 505–517. https://doi.org/10.1007/s12559-022-10052-0

Mahmoodi, N., Shirazi, H., & Fakhredanesh, M. (2025). Automatically weighted focal loss for imbalance learning. *Neural Computing and Applications*, *37*, 4035–4052. https://doi.org/10.1007/s00521-024-10323-x

Menke, M., Wenzel, T., & Schwung, A. (2024). Bridging the gap: Active learning for efficient domain adaptation in object detection. *Expert Systems with Applications*, *254*, 124403. https://doi.org/10.1016/j.eswa.2024.124403

Midigudla, R. S., Dichpally, T., Vallabhaneni, U., Wutla, Y., Sundaram, D. M., & Jayachandran, S. (2025). A comparative analysis of deep learning models for waste segregation: YOLOv8, EfficientDet, and Detectron 2. *Multimedia Tools and Applications*. https://doi.org/10.1007/s11042-025-20647-y

Moh, Y. C., & Abd Manaf, L. (2017). Solid waste management transformation and future challenges of source separation and recycling practice in Malaysia. *Resources, Conservation and Recycling*, *116*, 1–14. https://doi.org/10.1016/j.resconrec.2016.09.012

Nayfeh, A., Al-Azani, S., & Samma, H. (2025). A two-stage YOLOv8 approach for waste detection and classification in cognitive cities. *Transportation Research Procedia*, *84*, 579–586. https://doi.org/10.1016/j.trpro.2025.03.111

Pongboonchai-Empl, T., Antony, J., Garza-Reyes, J. A., Komkowski, T., & Tortorella, G. L. (2023). Integration of Industry 4.0 technologies into Lean Six Sigma DMAIC: A systematic review. *Production Planning & Control*. https://doi.org/10.1080/09537287.2023.2188496

Tang, T. Y., Salleh, N. M., & Wong, M. E. L. (2022). Smart virtual robot automation (SVRA)—Improving supplier transactional processes in enterprise resource planning (ERP) system: A conceptual framework. In R. Szewczyk, C. Zielinski, & M. Kaliczynska (Eds.), *Automation 2022* (Lecture Notes in Networks and Systems, Vol. 483, pp. 195–205). Springer. https://doi.org/10.1007/978-3-031-20429-6_19

Terven, J., Córdova-Esparza, D., & Romero-González, J. (2023). A comprehensive review of YOLO architectures in computer vision: From YOLOv1 to YOLOv8 and YOLO-NAS. *Machine Learning and Knowledge Extraction*, *5*(4), 1680–1716. https://doi.org/10.3390/make5040083

Zhang, Q., Yang, Q., Zhang, X., Bao, Q., Su, J., & Liu, X. (2021). Waste image classification based on transfer learning and convolutional neural network. *Waste Management*, *135*, 150–157. https://doi.org/10.1016/j.wasman.2021.08.038
