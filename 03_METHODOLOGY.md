# 3. Methodology

## 3.1 Integrated Multi-Framework Approach

The development of PurityLoop AI presents a dual engineering challenge that no single methodology adequately addresses. The system comprises two fundamentally different subsystems: a probabilistic machine learning component (the YOLOv8m-seg detection pipeline) and a deterministic software component (the Streamlit web application, RPA ingestion script, and database layer). Machine learning systems are characterised by non-deterministic outcomes, iterative data-dependency, and probabilistic performance guarantees. Traditional Software Development Life Cycle (SDLC) frameworks are designed for deterministic systems with fixed specifications. Applying a single framework to both domains introduces systematic risk: either the ML pipeline is over-constrained by milestone-driven phase gating, or the web application lacks the governance structure required for a multi-developer parallel workflow (Amershi et al., 2019, as cited in Overview_Draft.txt internal reference, 2025).

The Integrated Multi-Framework Methodology adopted by this study resolves this tension by assigning distinct frameworks to distinct problem layers, governed by a unifying quality engineering backbone. The framework architecture is visualised in Figure 4 of the Framework Diagrams document.

### 3.1.1 Framework Layer 1: Macro Governance — Iterative Waterfall

The Iterative Waterfall model governs the overall project lifecycle across three academic milestone phases: Proposal (Week 1–4), Interim Submission (Week 5–9), and Final Submission and WW12 Showcase (Week 10–14). Within each milestone phase, iterative sprints are permitted; however, phase gates require supervisor sign-off before progression. This structure satisfies the academic requirement for sequential milestone accountability while accommodating the inherent iteration of ML training.

### 3.1.2 Framework Layer 2: Quality Engineering Backbone — Lean Six Sigma / DMAIC

DMAIC (Define-Measure-Analyse-Improve-Control) serves as the overarching quality governance framework across both web development and ML model development subsystems. This selection is grounded in Pongboonchai-Empl et al. (2023), who demonstrate that DMAIC provides the strongest structural support for Industry 4.0 ML integration at the Analyse and Improve phases. The full DMAIC mapping for PurityLoop AI is presented in Table 3.1 below and visualised in Figure 2 of the Framework Diagrams document.

**Table 3.1 — DMAIC Phase Mapping for PurityLoop AI**

| DMAIC Phase | PurityLoop Content | Measurable Criterion |
|---|---|---|
| **Define** | Problem: 6.96% recyclable loss due to contamination; Malaysia 2024 recycling rate 37.9%; Manual sorting 30–40% error rate | Problem statement approved; Scope document signed |
| **Measure** | Baseline dataset statistics; class distribution analysis; human annotation inter-rater reliability | Dataset audit report complete; class imbalance ratio documented |
| **Analyse** | Model variant comparison (n/s/m/l/x); dataset selection rationale; augmentation FID validation | Decision matrix documented with citations |
| **Improve** | YOLOv8m-seg 10-phase training pipeline; Python RPA ingestion; Streamlit app; Power BI dashboard | mAP@0.5 ≥ 0.85; system end-to-end integration test pass |
| **Control** | Active learning loop; versioned model weights; KPI dashboard monitoring | Purity rate tracking live; monthly model health check defined |

### 3.1.3 Framework Layer 3: Analytics Strategy — BALC + CRISP-DM

The Business Analytics Life Cycle (BALC) serves as the macro-level analytics strategy wrapper, ensuring that all technical development outputs are traceable to business value extraction. Each sprint deliverable is mapped to a BALC stage: Business Understanding (problem definition) → Data Understanding (dataset audit) → Data Preparation (cleaning + augmentation) → Modelling (YOLOv8m-seg training) → Evaluation (mAP, FPS, purity rate) → Deployment (WW12 showcase).

The Cross-Industry Standard Process for Data Mining (CRISP-DM) operationalises the machine learning workflow within the BALC Modelling stage. CRISP-DM's defining feature—the mandatory loop-back from Evaluation to Data Preparation if performance targets are not met—is directly instantiated as the conditional re-training trigger: if mAP@0.5 < 0.85 on the held-out test set, the pipeline returns to data preparation and augmentation before retraining (Martinez-Plumed et al., 2019, as cited in Overview_Draft.txt internal reference, 2025).

### 3.1.4 Framework Layer 4: Web Development — Iterative Prototyping

The Streamlit web application and Power BI dashboard are developed using the Iterative Prototyping model. The UI team operates on mock data contracts defined by the Backend Integration developer during Sprint 1, enabling parallel development of the frontend and backend layers without dependency blocking. Prototype iterations progress from wireframe (Sprint 1) to mock-data interface (Sprint 2) to live API integration (Sprint 3) to final polish (Sprint 4).

### 3.1.5 Framework Layer 5: ML Tactical Execution — OSEMN + Quality Gates

The OSEMN (Obtain-Scrub-Explore-Model-iNterpret) framework provides the daily tactical execution protocol for the DataOps and ML R&D roles. OSEMN's five stages map directly to the 7-phase model development pipeline (Align → Label → Diagnostic → Quality Gate → Merge → Final Training → Deploy) established in the team session notes. The MLOps quality protocol—comprising individual diagnostic training, class-specific AP thresholds, Cleanlab audits, and strict data leakage validation—is integrated as the primary quality gate within the Model stage. Additionally, the Model stage incorporates the two-phase training protocol (Phase 1: Head Adaptation with Backbone Frozen to prevent catastrophic forgetting; Phase 2: Full Fine-Tuning with Cosine Annealing decay to adapt mid-level visual representations) and enforces a safety-critical Battery Class Recall Gate (recall ≥ 0.90) during validation to ensure that aggregate mAP optimization is subordinate to battery-hazard detection safety.

---

## 3.2 System Requirements Specification

Requirements were elicited through the hybrid methodology described in Section 2.8. Requirements are classified as Functional (FR) and Non-Functional (NFR) following established software engineering practice (Narishah et al., 2019b).

### 3.2.1 Functional Requirements

| ID | Requirement | Priority |
|---|---|---|
| FR1 | System monitors designated hot folder for new image files using watchdog library | Must Have |
| FR2 | System validates input files (image format, file inteoperational auditty) before inference; non-image files quarantined to error log | Must Have |
| FR3 | System processes valid images through YOLOv8m-seg inference pipeline | Must Have |
| FR4 | System classifies detected objects into nine defined waste categories | Must Have |
| FR5 | System applies 3-tier confidence scoring: Green ≥ 0.70 (Auto-accept), Yellow 0.45–0.69 (Flag for review), Red < 0.45 (Reject/query) | Must Have |
| FR6 | System triggers contamination alert (visual + audio) when contaminant class detected with confidence ≥ 0.45 | Must Have |
| FR7 | System calculates purity rate per session: Purity% = (pure_items / total_items) × 100 | Must Have |
| FR8 | System calculates Weight offset using Yield formula; coefficients traceable to BEIS/DESNZ (2023) | Must Have |
| FR9 | System writes all detection events to SQLite database within 100ms of inference completion | Must Have |
| FR10 | Power BI dashboard displays real-time purity rate, material yield, Weight saved, and contamination event log | Must Have |
| FR11 | Streamlit portal accepts phone number input; displays personal session impact and educational feedback | Should Have |
| FR12 | System awards Eco-Credits when session purity rate ≥ 85% | Should Have |
| FR13 | System generates end-of-session PDF ESG summary report | Could Have |

### 3.2.2 Non-Functional Requirements

| ID | Requirement | Metric |
|---|---|---|
| NFR1 | Detection latency per image ≤ 500ms on demonstration hardware | Benchmarked via Python time() |
| NFR2 | mAP@0.5 on held-out test set ≥ 0.85 | Computed via Ultralytics val() |
| NFR3 | mAP@0.5:0.95 on held-out test set ≥ 0.70 | Computed via Ultralytics val() |
| NFR4 | System uptime during WW12 Showcase ≥ 99% | No unrecoverable crash during demo |
| NFR5 | Streamlit web UI loads in < 3 seconds on 100Mbps network | Browser DevTools measurement |
| NFR6 | Carbon emission coefficient source must be peer-reviewed or government-published Yield reference | Verifiable citation in code comment |
| NFR7 | All team branches must pass CI pre-merge check (unit tests + lint) | GitHub Actions automation |

---

## 3.3 Dataset Preparation

### 3.3.1 Dataset Selection

Eleven candidate datasets were evaluated against four selection criteria: (1) battery/hazardous class coverage, (2) visual diversity (real-world vs. studio), (3) annotation format compatibility with YOLOv8, and (4) total volume ≥ 2,000 images per class after fusion. Four primary datasets were selected for the training corpus. Two supplementary Roboflow datasets pre-annotated in YOLOv8 format are incorporated to reduce annotation effort during initial model seeding.

**Table 3.2 — Selected Training Datasets**

| Dataset | Images | Classes | Reason for Selection |
|---|---|---|---|
| TrashNet | 2,527 | 6 (Cardboard, Glass, Metal, Paper, Plastic, Trash) | Established benchmark; clean studio baseline |
| TACO | ~1,500 | 60 → mapped to 9 super-categories | Academic citation; real-world diversity; COCO format |
| Garbage Classification v2 | 19,762 | 10 (incl. **Battery**, Biological) | Only large public dataset with Battery class |
| Trash Detection (Roboflow) | 2,800 | 64 → mapped to 9 (incl. Battery, Food Waste) | Pre-annotated YOLOv8 format; plug-and-train |

### 3.3.2 Data Cleaning Protocol

Following the Obtain stage of OSEMN and the Measure phase of DMAIC, the raw corpus undergoes systematic cleaning: (1) duplicate image removal via perceptual hash comparison; (2) corrupted file identification and exclusion; (3) image-to-label pairing verification—images without corresponding annotation files are excluded from training splits. All cleaning steps are logged with row-level audit records maintained in a cleaning_log.csv file.

### 3.3.3 Preprocessing Pipeline

All images undergo the following standardised preprocessing sequence:

1. **Colour Normalisation:** Convert all images to RGB three-channel format; normalise pixel intensities to [0, 255] range using Min-Max scaling.
2. **Resize:** Standardise all images to 640×640 pixels (YOLOv8m-seg input requirement).
3. **Quality Filtering:** Apply Tenengrad sharpness filter; images with Tenengrad score < 100 (threshold calibrated empirically for 640×640 at 8-bit depth) are excluded.
4. **Class Remapping:** Map all source dataset labels to the nine PurityLoop target classes using a master label mapping table; unlabelled or ambiguous classes are assigned to "Other/Mixed."

### 3.3.4 Data Augmentation

Four augmentation techniques are applied to the training split following sharpness filtering, at a 4× multiplier:

- 90° clockwise rotation (structural variation)
- Horizontal flip (orientation diversity)
- Brightness enhancement ×1.2 (illumination variation)
- Gaussian blur 2.5px (sensor noise simulation)

The Fréchet Inception Distance (FID) metric is used to validate augmentation fidelity; the 4× multiplier target is based on evidence from comparable studies (Ahmad et al., 2025) showing optimal FID at this level. Augmentation is applied to training images only; validation, testing, and held-out sets are not augmented.

### 3.3.5 Data Splitting Protocol

The cleaned and augmented corpus is split as follows: Training (70%), Validation (20%), Testing (10%). A separate held-out generalization set of 10% of the original (pre-augmentation) corpus is reserved for cross-distribution robustness evaluation. The held-out set is isolated before any model training, hyperparameter tuning, or augmentation selection decisions are made.

---

## 3.4 Model Architecture and Training

### 3.4.1 YOLOv8m-seg Architecture

YOLOv8m-seg (Jocher et al., 2023) is an anchor-free, single-stage object detection and instance segmentation model. The architecture comprises three components: (1) a CSP (Cross-Stage Partial) backbone for hierarchical feature extraction, (2) a PANet (Path Aggregation Network) neck for multi-scale feature fusion, and (3) dual detection and segmentation heads that simultaneously output bounding box predictions and binary instance segmentation masks. The anchor-free design eliminates the need for domain-specific anchor tuning, making the model well-suited to the highly heterogeneous scale and aspect ratio distribution of waste objects.

The medium variant (YOLOv8m-seg) is selected over the nano and small variants on the basis of superior recall on small object classes (battery cells, cigarette stubs) at the cost of approximately 2× inference time—a trade-off that remains within the 500ms latency budget on the demonstration hardware (NVIDIA GPU-enabled laptop).

### 3.4.2 Training Configuration

| Parameter | Value | Justification |
|---|---|---|
| Model | YOLOv8m-seg | Superior small-object recall vs. nano; within latency budget |
| Epochs | 300 | Sufficient for convergence on 70k+ image corpus |
| Batch size | 16 | Balances GPU memory and gradient stability |
| Image size | 640×640 | YOLOv8m default; preserves spatial detail |
| Optimiser | SGD with momentum | Default; stable convergence for segmentation tasks |
| Learning rate | 0.01 (cosine decay) | Standard warmup + cosine schedule |
| Early stopping | patience=50 epochs | Prevents overfitting on validation loss plateau |
| Random seed | 42 (fixed) | Ensures reproducibility across training runs |
| Data augmentation | YOLOv8 built-in (mosaic, mixup) + offline 4× | Combined strategy for maximum diversity |

### 3.4.3 Model Development Quality Gates and Algorithmic Audits

To ensure model inteoperational auditty, resolve label noise, and prevent silent failures during the YOLOv8m-seg training process, five mandatory defensive quality checks and algorithmic audits were embedded into the pipeline before master training was authorized:

1. **Class-Specific Labeling & Guide Alignment (Align Phase):** A unified taxonomy and edge-case label guide were established for the nine waste classes. A manual cross-audit of 100 random images per class was conducted to verify annotation consistency and define clear bounding criteria.
2. **Individual Diagnostic Training (Diagnostic Phase):** To surface labeling errors or systematic annotator bias, each team member trained an individual diagnostic model (50 epochs, batch size 16) solely on their assigned dataset slice. This isolated diagnostic stage serves as a localized quality control step before merging data.
3. **Class-Specific AP Quality Gate (QC Gate Phase):** Every class within the individual diagnostic runs was required to pass an Average Precision (AP) threshold of ≥ 0.60. Any class failing to meet this threshold triggered a targeted re-labeling cycle on that specific slice.
4. **Cleanlab Algorithmic Audit (Merge Phase):** Upon merging the individual data slices, the label-error detection library Cleanlab was executed on the combined pool. Cleanlab algorithmically flagged and pruned corrupted labels, systematic mislabeling, and ambiguous features to produce a high-fidelity master corpus.
5. **Strict Data Leakage Validation (Control Phase):** A perceptual hash comparison and duplicate check were executed across the combined training and validation sets. Checkpoints were rejected if any duplicate or near-duplicate images were found across partitions, ensuring exactly zero data leakage and preventing artificially inflated performance metrics.

### 3.4.4 Two-Phase Training Protocol

Following the RadioLens (2025) benchmark framework, training proceeds in two phases:

**Phase A — Reference Training (Base Model):** Default YOLOv8m-seg hyperparameters, no preprocessing standardisation beyond basic resize. Used to establish a baseline and diagnose generalisation gaps.

**Phase B — Adjusted Training (Optimised Model):** Full preprocessing pipeline + 4× validated augmentation + controlled hyperparameter tuning applied. Improvements are attributed to specific pipeline decisions through controlled ablation.

---

## 3.5 Python RPA Ingestion Pipeline

The Python RPA hot-folder script performs four functions: (1) monitors the designated watch folder using the watchdog library for new file creation events; (2) validates each new file (checks MIME type, file size, inteoperational auditty); (3) on validation pass, invokes the inference function with the image path and appends results to the detection queue; (4) on validation fail, moves the file to a quarantine subfolder and logs the error type, filename, and timestamp to error_log.csv.

This design addresses the robustness requirements identified in Dr. Narishah's SVRA paper (2022), which explicitly evaluates RPA script robustness against edge cases including malformed inputs, empty folders, and process race conditions.

---

## 3.6 Evaluation Protocol

Model performance is assessed across four dataset partitions: Training (monitoring only), Validation (model selection), Test (internal evaluation), and Held-Out Generalization (cross-distribution robustness). Performance metrics are:

- **mAP@0.5:** Primary detection accuracy metric; target ≥ 0.85
- **mAP@0.5:0.95:** Strict boundary precision metric; target ≥ 0.70
- **Precision and Recall:** Per-class; particular emphasis on Battery and Food Waste classes
- **F1-Score:** Harmonic mean of Precision and Recall; target ≥ 0.82
- **Inference FPS:** Target ≥ 2 FPS sustained on demonstration hardware (500ms/frame)
- **Purity Rate Accuracy:** Ground-truth purity rate vs. system-reported purity rate; target ±2%

---

## 3.7 Ethical and Data Governance Considerations

All datasets used in this study are publicly available and do not contain personally identifiable information. User phone numbers collected by the Streamlit app are hashed (SHA-256) before storage; plaintext phone numbers are never persisted. The system does not transmit data to external servers during the WW12 showcase. A data handling statement is appended to the demonstration consent form provided to showcase participants.
