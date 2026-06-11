# PurityLoop AI — Project Proposal
### Automated Waste Sorting & Contamination Detection System
**Sunway University · Department of Business Analytics**
**Supervisor: Dr. Narishah Mohamed Salleh**
**Date: May 2026 | Team Size: 6**

---

## EXECUTIVE SUMMARY

PurityLoop AI proposes a dual-layer computer vision system for automated waste sorting and contamination detection in recycling facilities. The system applies YOLOv8s object detection (Layer A) with conditional YOLOv8s-seg instance segmentation (Layer B) to classify waste items in real time, calculate material yield savings, and deliver actionable ESG data via a live business intelligence dashboard and user-facing behavioural change application.

The project addresses a measurable operational gap: manual sorting in Malaysian recycling facilities produces approximately 30% contamination rates (Moh & Abd Manaf, 2017), resulting in unsaleable material bales, missed material recovery opportunities, and unreliable operational reporting. PurityLoop AI targets ≥90% purity rate, ≥25 FPS processing speed, and mAP@0.5 ≥ 0.85 on the validation dataset.

The framework is structured under the DMAIC Lean Six Sigma methodology as applicable to Industry 4.0 digital transformation (Pongboonchai-Empl et al., 2023), and the conceptual framework is modelled after Tang et al. (2022).

---

## 1. PROBLEM STATEMENT

**Domain:** Industrial Operations & Quality Assurance | Waste Management & Circular Economy

**Problem:** Manual waste sorting is the dominant method at Malaysian recycling facilities. It produces inconsistent material purity, misses hazardous items (batteries, e-waste), and generates no traceable data for operational performance auditing or operational reporting. As operational reporting requirements tighten under Malaysian and global sustainability frameworks, the lack of verified, item-level recycling data is a material business risk.

**Gap identified in literature:** Existing CV-based waste sorting solutions apply single-stage detection without uncertainty handling (no MAYBE tier), resulting in either high false acceptance or high false rejection rates on real-world damaged waste. No existing solution integrates a continuous active learning loop with a operational performance auditing module and a user behavioural change layer in a unified pipeline.

**DMAIC Define statement:** Develop an automated waste sorting system that reduces contamination rate from ~30% to ≤10%, processes items at ≥25 FPS, and generates real-time, per-item material yield data suitable for ESG audit reporting.

---

## 2. OBJECTIVES

| # | Objective | KPI | Target |
|---|-----------|-----|--------|
| O1 | Automate multi-class waste sorting | mAP@0.5 | ≥ 0.85 |
| O2 | Detect hazardous items (battery) with priority accuracy | Battery class AP | Report separately; ≥ 0.80 |
| O3 | Enable real-time processing | Inference speed | ≥ 25 FPS |
| O4 | Increase material purity | Purity Rate | ≥ 90% per session |
| O5 | Quantify environmental impact | weight processed | Calculated per kg processed |
| O6 | Reduce contamination at source | User app engagement | Behavioural feedback delivery |

---

## 3. VARIABLE MATRIX

| Variable Type | Variable Name | Definition & Metric |
|---------------|--------------|---------------------|
| Independent (Input) | Raw Image Frames | RGB pixel arrays from simulated conveyor belt camera |
| Independent (Input) | User Identifier | Phone number linking waste sessions to user accounts |
| Predicted (ML) | Object Class | Categorical label: PET Plastic, Aluminum, Contaminant, Battery, etc. |
| Predicted (ML) | Confidence Score | Continuous 0.0–1.0; gates YES/MAYBE/NO decision logic |
| Output (Business) | Purity Rate | Ratio of accepted recyclables to total items detected per session/bale |
| Output (Business) | Material Yield | Volume/weight of verified pure recyclables available for resale |
| Output (Business) | Carbon Offset (weight) | Avoided emissions calculated via material-specific Yield emission factors (JEM, 2024) |

---

## 4. METHODOLOGY

### 4.1 Research Design

This project adopts a **design science research** approach: constructing an artefact (the PurityLoop AI system) and evaluating it against defined performance metrics. The evaluation framework follows DMAIC (Pongboonchai-Empl et al., 2023). The conceptual framework structure follows Tang et al. (2022).

### 4.2 Literature Selection Criteria

| Criterion | Specification |
|-----------|--------------|
| Publication year | 2020 onwards |
| Indexing | Scopus Q1 or Q2 |
| Document type | Peer-reviewed journal article |
| Search databases | Google Scholar, Scopus, ScienceDirect |
| Keywords used | "YOLOv8 waste detection", "transfer learning waste classification", "active learning object detection", "material yield recycling Yield", "DMAIC Industry 4.0" |
| Exclusion | arXiv preprints without journal publication, conference proceedings pre-2020, government/industry reports (used only for background statistics) |

### 4.3 AI Model Development

**Model:** YOLOv8s (Ultralytics) — anchor-free single-stage object detector with CSP-DarkNet backbone, FPN+PAN neck, and decoupled detection head (Terven et al., 2023).

**Version justification:** YOLOv8s selected over n (insufficient accuracy for hazard detection) and m/l/x (exceed Colab free tier T4 16GB VRAM constraint). YOLOv8 selected over YOLOv5 based on +7.5 mAP improvement (Abo-Zahhad et al., 2025) and anchor-free architecture advantage for irregular waste shapes (Midigudla et al., 2025).

**Detection method:** Bounding box detection (Layer A) + conditional instance segmentation (Layer B) for MAYBE-confidence items. Hybrid two-stage approach validated by Nayfeh et al. (2025).

**Training environment:** Google Colab free tier (T4 GPU, 16GB VRAM). Checkpoints saved to Google Drive every 5 epochs.

**Transfer learning:** COCO-pretrained weights provide pre-learned edge, texture, and shape features. Fine-tuning on waste dataset requires ~100 epochs vs ~300+ for scratch training (Zhang et al., 2021).

### 4.4 Dataset Strategy

| Priority | Dataset | Images | Classes | Scopus-citable |
|----------|---------|--------|---------|----------------|
| P1 | Garbage Classification v2 (Kaggle) | 19,762 | 10 (incl. Battery) | Yes — Zhalgas et al. (2026) |
| P1 | Trash Detection (Roboflow) | 2,800 | 64 (incl. Battery, Food Waste) | Yes — Midigudla et al. (2025) |
| P2 | TrashNet (Kaggle) | 2,527 | 6 | Yes — Zhang et al. (2021) |
| P2 | RealWaste (Kaggle) | 4,752 | 9 | Yes — Abo-Zahhad et al. (2025) |

All datasets harmonised to unified 8-class taxonomy. All annotations converted to YOLOv8 txt format. Train/Val/Test: 70/15/15 stratified split.

### 4.5 Model Evaluation

Primary benchmark: Midigudla et al. (2025) establishes YOLOv8 mAP >85% on waste classification as achievable baseline. Evaluation metrics: mAP@0.5, mAP@0.5:0.95, Precision, Recall, F1, FPS, and per-class AP for Battery.

### 4.6 Carbon Offset Calculation

```
weight_processed (kg) = Σ [mass_i × (EF_virgin_i − EF_recycled_i)] × Purity_Factor
```

Emission factors (EF) sourced from Yield peer-reviewed literature (JEM, 2024). Mass estimated via class-average weight constants (acknowledged limitation — see Section 7).

---

## 5. TECHNICAL ARCHITECTURE OVERVIEW

*Full architecture: PurityLoop_Diagram.md*

```
Camera / Hot Folder
      ↓
Python RPA (Tang et al., 2022)
      ↓
YOLOv8s Detection — Layer A (Terven 2023, Ajayi 2024)
      ↓
Confidence Decision Gate (Chen 2025)
   YES ≥0.75 → Classify → Calculate → SQLite
   MAYBE 0.40-0.74 → YOLOv8s-seg Layer B (Nayfeh 2025)
   NO <0.40 → Discard
      ↓
Classification: 8-class taxonomy (Mahmoodi 2025, Midigudla 2025)
      ↓
Carbon Offset + Purity Rate (JEM 2024)
      ↓
Power BI Dashboard + User App + ESG Report
      ↑
Active Learning Loop (Menke 2024, Pongboonchai-Empl 2023)
```

---

## 6. TEAM STRUCTURE & ROLES

| Member | Role | Layer Ownership |
|--------|------|----------------|
| Member 1 | Project Management & ESG | Carbon formula, operational report, DMAIC documentation |
| Member 2 | DataOps | Dataset harmonisation, annotation format conversion, class mapping |
| Member 3 | ML R&D | Model training, evaluation, hyperparameter tuning, active learning |
| Member 4 | Backend / Integration | Python RPA script, SQLite schema, data pipeline |
| Member 5 | Full-Stack UI | User app (mobile-responsive), Eco-Credits, feedback display |
| Member 6 | BI Analytics | Power BI / Tableau dashboard, KPI visualisation, operational report export |

*Each member is the designated Q&A owner for their layer during the WW12 presentation.*

---

## 7. LIMITATIONS & RISK MITIGATION

| Limitation | Risk | Mitigation |
|------------|------|-----------|
| Weight estimation via constants | ±15–30% weight error | Acknowledge in report; future work = load cell |
| Colab free tier GPU availability | Training interrupted | Checkpoint every 5 epochs to Drive; use YOLOv8s not m/l |
| Studio-biased training data | Lower accuracy on soiled waste | RealWaste (4,752 images) added for domain realism |
| Styrofoam not in dataset | Misclassified as General Trash | Acknowledged limitation; flag in report |
| Malaysia-specific EF gap | weight calculated on global factors | Acknowledged; future work = MyHIJAU/MGTC validation |
| Hot folder ≠ real industrial camera | Demo not production-equivalent | Explicitly scoped as proof-of-concept; future work = edge deployment |

---

## 8. EXPECTED OUTCOMES

| Outcome | Metric | Evidence |
|---------|--------|----------|
| Trained YOLOv8s model | mAP@0.5 ≥ 0.85 | Midigudla et al. (2025) benchmark |
| Real-time inference | ≥ 25 FPS on T4 | Abo-Zahhad et al. (2025) |
| Purity rate improvement | ≥ 90% vs ~70% manual baseline | Moh & Abd Manaf (2017) baseline |
| Carbon tracking | weight per kg per session | JEM (2024) emission factors |
| Active learning loop | Retrains at 100-sample threshold | Menke et al. (2024) |
| Operational dashboard | Live Power BI KPIs | Tang et al. (2022) output layer |

---

## 9. TIMELINE

| Week | Milestone |
|------|-----------|
| 1–2 | Dataset download, class harmonisation, annotation conversion |
| 3–4 | Training pipeline setup on Colab; baseline training run |
| 5–6 | Hyperparameter tuning; evaluation against benchmark |
| 7–8 | RPA script development; SQLite schema; pipeline integration |
| 9–10 | Dashboard development; user app; material yield module |
| 11 | End-to-end demo test; active learning loop validation |
| 12 | WW12 Showcase — live dual-screen demo |

---

## 10. GENERALISATION — COMMERCIAL VIABILITY

PurityLoop AI framework is not limited to recycling. The backbone feature representations, once trained on waste domain, transfer to analogous detection problems in other industries with minimal retraining (Zhang et al., 2021). Demonstrated use cases:

- **F&B manufacturing:** Foreign object detection on conveyor (same hardware setup, different classes)
- **Hospital waste:** Sharps/biohazard separation (hazard class logic directly analogous to Battery detection)
- **Construction:** Debris classification on site (outdoor detection; RealWaste training improves robustness)

This generalisation capability supports commercial scaling arguments in the ESG and Industry 4.0 market, where automated quality assurance and environmental accountability are increasingly mandated (Pongboonchai-Empl et al., 2023).

---

## REFERENCES

Abo-Zahhad, M. M., & Abo-Zahhad, M. (2025). Real time intelligent garbage monitoring and efficient collection using YOLOv8 and YOLOv5 deep learning models for environmental sustainability. *Scientific Reports*, *15*(1), 16024. https://doi.org/10.1038/s41598-025-99885-x

Ajayi, O. G., Ibrahim, P. O., & Adegboyega, O. S. (2024). Effect of hyperparameter tuning on the performance of YOLOv8 for multi crop classification on UAV images. *Applied Sciences*, *14*(13), 5708. https://doi.org/10.3390/app14135708

Author(s) TBC. (2024). Recycling packaging waste from residual waste reduces operational waste inefficiencies. *Journal of Environmental Management*. https://doi.org/10.1016/j.jenvman.2024 [VERIFY: ScienceDirect pii/S0301479724030147]

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

Zhalgas, A., Amirgaliyev, B., Boltay, B., Shegenova, D., Zhylkybay, N., & Yedilkhan, D. (2026). Development of an intelligent waste segregation system using a self-collected dataset and deep learning methods. *Journal of Robotics and Control*, *7*(1), 3393–3404. https://doi.org/10.18196/jrc.v7i1.27247 [VERIFY Scopus Q rating]
