# Personal Draft: Chris (Group Leader)
**PurityLoop AI Capstone Project**

*This document contains the exact drafted text for all sections assigned to Chris, updated and renumbered in accordance with the latest Table of Contents and Capstone Proposal Instructions, and aligned with the technical decisions and quality protocols established in the team session notes. The content is written in a formal, academic tone suitable for the final thesis submission.*

---

## 1.3 Research Objectives

This study aims to design, develop, and evaluate PurityLoop AI, an integrated waste contamination detection and analytics system, in pursuit of the following three core research objectives (consolidated in compliance with the capstone proposal instructions limit of maximum four objectives):

1. **Automate Multi-Class Waste Sorting & Enhance Safety (Computer Vision Module):** To design, fine-tune, and evaluate a single-stage instance segmentation model (YOLOv8m-seg) capable of classifying heterogeneous waste streams into nine distinct categories and prioritizing the real-time detection of hazardous contaminants (specifically lithium-ion batteries) to prevent operational facility fires, targeting a model performance of mAP@0.5 ≥ 0.82.
2. **Quantify Environmental Accountability & Establish Live Analytics (Data & BI Module):** To implement a robust, watchdog-monitored Python RPA data ingestion pipeline and SQLite database schema that seamlessly captures sorting events and feeds a real-time business intelligence dashboard (Power BI) to calculate and visualize Yield-derived material yield metrics (Weight saved) as a verifiable process audit trail.
3. **Drive Behavioral Intervention & Source-Level Contamination Reduction (User App Module):** To construct a user-facing, gamified Streamlit application that links with the operational database to display personal ecological impact, deliver real-time educational contamination feedback, and manage an Eco-Credit token reward economy to incentivize sorting correctness at the household level.

---

## 2.6 Theme 5: DMAIC and Industry 4.0 Integration for Machine Learning Quality

The application of machine learning in industrial environments requires rigorous quality governance, bridging the gap between probabilistic model outputs and deterministic business requirements.

### 2.6.1 DMAIC as a Framework for ML Quality Governance

The DMAIC (Define-Measure-Analyse-Improve-Control) framework, originating from Lean Six Sigma quality engineering, provides a structured, evidence-based methodology for process improvement that translates effectively to Industry 4.0 deployments. Pongboonchai-Empl et al. (2023) demonstrated that DMAIC provides robust structural support for machine learning integration, showing that digital transformation projects benefit from mapping data mining and algorithmic training specifically to the *Improve* phase, while assigning automated dashboard monitoring to the *Control* phase. For the PurityLoop AI system, this framework ensures that the machine learning lifecycle is not treated merely as an isolated coding task, but as an industrial quality control initiative where every pipeline adjustment is directly traceable to the reduction of the baseline contamination defect rate.

### 2.6.2 Multi-Stage Quality Gate Protocol for MLOps **[UPDATED]**

In the context of deep learning development, relying solely on final validation metrics often masks underlying pipeline errors. To operationalize the DMAIC *Analyse* and *Control* phases at the code level, this project integrates a multi-stage Quality Gate and Algorithmic Audit protocol. Rather than proceeding directly to master training on unverified data, the process mandates individual diagnostic training runs on independent dataset slices to surface label noise, followed by an algorithmic label-error audit using Cleanlab. By nesting these structured quality checkpoints within the broader DMAIC quality framework, PurityLoop AI establishes a verified mathematical and spatial foundation. This ensures that when the project proceeds to the two-phase training protocol, Phase 1 (Head Adaptation) begins with a structurally sound data-loading and backpropagation architecture, and subsequent joint fine-tuning in Phase 2 is built on genuine, clean feature representation rather than dataset leakage or corrupted annotations.

---

## 2.8 Critical Synthesis and Research Gap **[SHIFTED / RENUMBERED]**

The academic literature on automated waste management reveals a convergent gap across multiple disciplines. While computer vision research has produced highly capable single-model architectures for waste classification (Ahmad et al., 2025; Jocher et al., 2023), these models are frequently evaluated in isolation from the industrial operational contexts in which they must function. Conversely, literature on operational reporting (Mustafa et al., 2025) highlights the growing demand for verifiable sustainability data but lacks industrial demonstrations of real-time, computer-vision-fed carbon audit systems. Furthermore, gamification research (Venturi et al., 2024) validates behavioural intervention applications but fails to link user applications to live, facility-level sorting data.

**The primary research gap is the absence of an end-to-end, integrated deployment pipeline.** Existing solutions either optimize the machine learning architecture without addressing downstream business intelligence, or they focus on web applications without a robust, real-time computer vision backend. PurityLoop AI directly addresses this gap by simultaneously operationalizing YOLOv8m-seg detection trained on a fused multi-dataset corpus, feeding a real-time ESG carbon dashboard, linked to a gamified user app, all governed by Lean Six Sigma DMAIC quality engineering. This holistic integration constitutes the primary originality and contribution of the study.

---

## 3.1 Integrated Multi-Framework Approach

The development of PurityLoop AI presents a dual engineering challenge: integrating a probabilistic machine learning component (the YOLOv8m-seg pipeline) with a deterministic software component (the web application and ingestion scripts). Traditional Software Development Life Cycle (SDLC) frameworks are designed for deterministic systems and are inadequate for the non-deterministic, highly iterative nature of model training. Conversely, using a purely agile approach risks losing the strict quality controls required for industrial operational compliance. To resolve this, the project adopts an **Integrated Multi-Framework Methodology** that assigns distinct frameworks to specific problem layers:

### 3.1.1 Framework Layer 1: Macro Governance — Iterative Waterfall
The Iterative Waterfall model governs the overall project lifecycle across three academic milestone phases: Proposal (Weeks 1–4), Interim Submission (Weeks 5–9), and Final Submission and WW12 Showcase (Weeks 10–14). Within each milestone phase, iterative sprints are permitted; however, phase gates require supervisor sign-off before progression. This structure satisfies the academic requirement for sequential milestone accountability while accommodating the inherent iteration of ML training.

### 3.1.2 Framework Layer 2: Quality Engineering Backbone — Lean Six Sigma / DMAIC
DMAIC (Define-Measure-Analyse-Improve-Control) serves as the overarching quality governance framework across both web development and ML model development subsystems. This selection is grounded in Pongboonchai-Empl et al. (2023), who demonstrate that DMAIC provides the strongest structural support for Industry 4.0 ML integration at the Analyse and Improve phases. The full DMAIC mapping for PurityLoop AI is presented in Table 3.1 below:

**Table 3.1 — DMAIC Phase Mapping for PurityLoop AI**

| DMAIC Phase | PurityLoop Content | Measurable Criterion |
|---|---|---|
| **Define** | Problem: 6.96% recyclable loss due to contamination; Malaysia 2024 recycling rate 37.9%; Manual sorting 30–40% error rate | Problem statement approved; Scope document signed |
| **Measure** | Baseline dataset statistics; class distribution analysis; human annotation inter-rater reliability | Dataset audit report complete; class imbalance ratio documented |
| **Analyse** | Model variant comparison (n/s/m/l/x); dataset selection rationale; augmentation FID validation | Decision matrix documented with citations |
| **Improve** | YOLOv8m-seg 10-phase training pipeline; Python RPA ingestion; Streamlit app; Power BI dashboard | mAP@0.5 ≥ 0.82; system end-to-end integration test pass |
| **Control** | Active learning loop; versioned model weights; KPI dashboard monitoring | Purity rate tracking live; monthly model health check defined |

### 3.1.3 Framework Layer 3: Analytics Strategy — BALC + CRISP-DM
The Business Analytics Life Cycle (BALC) serves as the macro-level analytics strategy wrapper, ensuring that all technical development outputs are traceable to business value extraction. Each sprint deliverable is mapped to a BALC stage: Business Understanding (problem definition) → Data Understanding (dataset audit) → Data Preparation (cleaning + augmentation) → Modelling (YOLOv8m-seg training) → Evaluation (mAP, FPS, purity rate) → Deployment (WW12 showcase).

The Cross-Industry Standard Process for Data Mining (CRISP-DM) operationalises the machine learning workflow within the BALC Modelling stage. CRISP-DM's defining feature—the mandatory loop-back from Evaluation to Data Preparation if performance targets are not met—is directly instantiated as the conditional re-training trigger: if mAP@0.5 < 0.82 on the held-out test set, the pipeline returns to data preparation and augmentation before retraining (Martinez-Plumed et al., 2019).

### 3.1.4 Framework Layer 4: Web Development — Iterative Prototyping
The Streamlit web application and Power BI dashboard are developed using the Iterative Prototyping model. The UI team operates on mock data contracts defined by the Backend Integration developer during Sprint 1, enabling parallel development of the frontend and backend layers without dependency blocking. Prototype iterations progress from wireframe (Sprint 1) to mock-data interface (Sprint 2) to live API integration (Sprint 3) to final polish (Sprint 4).

### 3.1.5 Framework Layer 5: ML Tactical Execution — OSEMN + Quality Gates **[UPDATED]**
The OSEMN (Obtain-Scrub-Explore-Model-iNterpret) framework provides the daily tactical execution protocol for the DataOps and ML R&D roles. OSEMN's five stages map directly to the 7-phase model development pipeline (Align → Label → Diagnostic → Quality Gate → Merge → Final Training → Deploy) established in the team session notes. The MLOps quality protocol—comprising individual diagnostic training, class-specific AP thresholds, Cleanlab audits, and strict data leakage validation—is integrated as the primary quality gate within the Model stage. Additionally, the Model stage incorporates the two-phase training protocol (Phase 1: Head Adaptation with Backbone Frozen to prevent catastrophic forgetting; Phase 2: Full Fine-Tuning with Cosine Annealing decay to adapt mid-level visual representations) and enforces a safety-critical Battery Class Recall Gate (recall ≥ 0.90) during validation to ensure that aggregate mAP optimization is subordinate to battery-hazard detection safety.

### 3.1.6 User Interface Design — Wireframes & User Journey
The user interface design layer focuses on behavioral engineering, translating industrial data into intuitive visuals. Wireframes map out the user journey from authentication via a SHA-256 hashed phone number to the visualization of personal material yields (Weight saved) and Eco-Credit points. The user journey includes micro-animations and positive reinforcement feedback (such as specific explanations for sorting contamination) to drive behavioral change.

---

## 3.4.3 Model Development Quality Gates and Algorithmic Audits **[UPDATED]**

To ensure model inteoperational auditty, resolve label noise, and prevent silent failures during the YOLOv8m-seg training process, five mandatory defensive quality checks and algorithmic audits were embedded into the pipeline before master training was authorized:

1. **Class-Specific Labeling & Guide Alignment (Align Phase):** A unified taxonomy and edge-case label guide were established for the nine waste classes. A manual cross-audit of 100 random images per class was conducted to verify annotation consistency and define clear bounding criteria.
2. **Individual Diagnostic Training (Diagnostic Phase):** To surface labeling errors or systematic annotator bias, each team member trained an individual diagnostic model (50 epochs, batch size 16) solely on their assigned dataset slice. This isolated diagnostic stage serves as a localized quality control step before merging data.
3. **Class-Specific AP Quality Gate (QC Gate Phase):** Every class within the individual diagnostic runs was required to pass an Average Precision (AP) threshold of ≥ 0.60. Any class failing to meet this threshold triggered a targeted re-labeling cycle on that specific slice.
4. **Cleanlab Algorithmic Audit (Merge Phase):** Upon merging the individual data slices, the label-error detection library Cleanlab was executed on the combined pool. Cleanlab algorithmically flagged and pruned corrupted labels, systematic mislabeling, and ambiguous features to produce a high-fidelity master corpus.
5. **Strict Data Leakage Validation (Control Phase):** A perceptual hash comparison and duplicate check were executed across the combined training and validation sets. Checkpoints were rejected if any duplicate or near-duplicate images were found across partitions, ensuring exactly zero data leakage and preventing artificially inflated performance metrics.

---

## 3.8 Evaluation Protocol **[SHIFTED / RENUMBERED / UPDATED]**

The evaluation of the PurityLoop AI model is strictly governed by the **Asymmetric Error Principle**, which dictates that false positives on hazardous materials (e.g., classifying a battery as recyclable plastic) carry a significantly higher operational risk and cost (facility fire hazard) than false negatives. Therefore, the evaluation protocol heavily prioritizes precision and explicit uncertainty handling over pure recall. This is empirically motivated by Terazono et al. (2024), who document that 80–90% of municipal waste treatment facility fires are caused by undetected lithium-ion battery ignition during the mechanical crushing stage.

The system is evaluated against the following primary metrics on the held-out test generalization set:
* **mAP@0.5 (mAP50):** The primary detection accuracy metric, with a strict minimum target of ≥ 0.82 across all classes, benchmarked against waste detection accuracy levels reported in the literature (Arishi, 2025; Sayem et al., 2024).
* **mAP@0.5:0.95 (mAP50-95):** Evaluates the strictness of the boundary regression, with a target of ≥ 0.60.
* **Mask mAP@0.5 (Mask mAP50-M):** Evaluates the strictness of the segmentation boundary masks, with a target of ≥ 0.70.
* **Battery Precision:** Specifically monitored for the *Battery* class, with a target of ≥ 0.85. A single false positive for this class on the generalization set (i.e., failing to flag a battery) triggers a mandatory retraining cycle because of the high ignition risk documented by Terazono et al. (2024).
* **Inference FPS:** Latency must remain below 500ms per frame (≥ 25 FPS on demonstration hardware) to ensure viability for live conveyor belt deployment, satisfying the real-time operational thresholds validated by Terven et al. (2023) and Sayem et al. (2024).

Predictions falling below the confidence threshold (0.85 for general classes, 0.90 for batteries) are deliberately routed to a "Yellow/Amber" zone. This explicitly engineers uncertainty into the pipeline, requiring human review and establishing a robust contamination firewall.

---

## 4.3 Impact to the Model as New Knowledge

A prevailing assumption in applied computer vision is that performance gains are primarily achieved through architectural modifications (e.g., upgrading from YOLOv5 to YOLOv8). However, the development of PurityLoop AI contributes new knowledge to the field by demonstrating the overwhelming efficacy of a **data-centric MLOps methodology** applied to heterogeneous waste streams.

By maintaining a static model architecture (YOLOv8m-seg) and iteratively refining the dataset—through multi-dataset fusion to inject missing hazardous classes, targeted augmentation (rotation, Gaussian blur), and rigorous perceptual hash deduplication—the system proves that pipeline-level data governance is as consequential as algorithmic selection. Furthermore, by explicitly modelling uncertainty through a 3-tier confidence gating system (Auto-Accept, Flag for Review, Reject), this project proves that computer vision systems in waste management do not need to be perfectly accurate to be operationally viable; they simply need to be perfectly transparent about their uncertainty. Additionally, by using instance segmentation masks rather than standard bounding boxes, the system introduces a scalable method to estimate waste volume and mass dynamically. This resolves a critical limitation in the literature regarding material yield tracking, where bounding boxes provide poor approximations for non-convex waste contours, and maps directly to Material Yield Assessment (Yield) substitution calculations (Wang et al., 2022).

---

## 5.1 Overview **[NEW]**

Project management for PurityLoop AI adopts a hybrid approach that bridges academic sequential milestones with agile software development practices. The six-member team is divided into two specialized development units: the Backend Squad (focusing on DataOps, ML modeling, and pipeline integration) and the Frontend Squad (focusing on UI/UX, Streamlit development, and Power BI dashboards). Sprint planning occurs bi-weekly, where technical backlog items are assigned and tracked. Team synchronization is maintained via git branching rules and a collaborative task board. A strict version control protocol governs the main branch: developers work on independent feature branches, push changes through pull requests, and require a minimum of one peer review and a clean automated pre-merge test suite run (linting and basic unit tests) before integration.

---

## 5.2 Gantt Chart Project Schedule **[NEW]**

The PurityLoop AI timeline is structured across the 14-week semester, with major deliverables mapped to academic milestone gates. The schedule is divided into: Phase 1: Requirements and Proposal (Weeks 1–4), Phase 2: Core Development and Interim Submission (Weeks 5–9), and Phase 3: System Integration, Testing, and Final WW12 Showcase (Weeks 10–14). The schedule incorporates parallel development tracks for the ML and Web systems, converging during the integration sprints.

### 5.2.1 Critical Path Part 1: Diagnostic Training Timelines
The first critical path of the project governs the ML R&D lifecycle (Weeks 1–6). It outlines the sequential steps of dataset collection, de-duplication, resizing, and individual diagnostic runs. Before master model training can proceed, the diagnostic training protocol—incorporating the individual 50-epoch runs, class-specific AP gates (AP ≥ 0.60), and the Cleanlab algorithmic audit—must be successfully completed. Any failure at these checkpoints acts as a quality gate, halting progression and requiring the team to cycle back to the data preparation phase. This ensures that the 100-epoch master training run (with early stopping patience of 20 epochs) is executed on verified, high-fidelity data.

### 5.2.2 Critical Path Part 2: Integrated Testing Timelines
The second critical path governs the system integration phase (Weeks 10–12). This track manages the dependencies between the backend RPA scripts and the frontend presentation layers. Specifically, the database schema (SQLite) must be finalized and frozen before Streamlit API routing and Power BI dashboard queries can be bound. Integrated testing timelines detail the end-to-end processing path: simulated image ingestion, file watchdog triggers, YOLOv8m-seg inference, confidence threshold evaluation, database logging, and live dashboard updating. This path concludes with a formal User Acceptance Testing (UAT) phase to verify that system processing latency remains ≤ 500ms.

---

## 5.3 Delegation of Work Matrix **[NEW]**

To ensure equitable distribution of effort and clear task boundaries, the project deliverables are partitioned across the six team members. Each member serves as the designated owner and Q&A lead for their respective components during milestone presentations. The delegation matrix is formally specified in Table 5.1:

**Table 5.1 — Team Delegation of Work Matrix**

| Member | Role | Core Technical Focus Areas | Key Proposal Deliverables |
|---|---|---|---|
| **Naomi** | DataOps & Governance | Dataset acquisition, cleaning, remapping, annotation tools (CVAT) | Lit Search Protocol (Theme 2), Dataset Prep, Ethical & Data Governance |
| **Talvin** | ML Lead (Training) | YOLOv8m-seg training, hyperparameter tuning, training environment setup | Lit Search Protocol (Theme 1), YOLO Architecture, Training Config, Two-Phase Protocol |
| **Chris** | ML Debug & QA | Model generalisation validation, MLOps quality gates, overall methodology frameworks | Research Objectives, Lit Search Protocol (Theme 5), Critical Synthesis, Multi-Framework Approach, Evaluation Protocol, New Knowledge Impact |
| **Kong** | Backend Integration | Python RPA ingestion script, SQLite schema, watchdog setup, database triggers | Research Questions, Requirement Elicitation, Web Dev Framework, System Requirements, RPA Ingestion Pipeline, PM Overview |
| **Georgene** | UI/UX & Gamification | Streamlit frontend, Eco-Credit logic, wireframes, user journey design | Scope & Delimitations, Lit Search Protocol (Theme 4), UI Design Wireframes, Web Application Dev (Streamlit), Value Evaluation Overview |
| **Feng** | BI & ESG Analytics | Power BI / Tableau dashboard, Yield material yield recovery calculations, operational reporting | Significance of Study, Lit Search Protocol (Theme 3), BI Dashboard Dev (Power BI), Industry Impact, Expected ESG Benefits |
