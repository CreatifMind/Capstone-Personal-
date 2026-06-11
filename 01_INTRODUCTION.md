# 1. Introduction

## 1.1 Background and Context

Solid waste management represents one of the defining infrastructure challenges of the twenty-first century. In Malaysia, total solid waste generation reached 15.2 million tonnes in 2024 and is projected to rise to 17.03 million tonnes by 2035 (SWCorp, 2024). Despite government-led initiatives under the 12th Malaysia Plan, which targets a national recycling rate of 40% by 2025, Malaysia achieved only 37.9% in 2024—a figure that, while representing significant progress from 21% in 2017, continues to mask a critical underlying problem: contamination. An estimated 6.96% of all waste that could have been recycled, representing nearly one million tonnes of material, is rejected from the recycling stream annually due to the presence of contaminants introduced during collection and sorting (SWCorp, 2024; Pertanika Journal, 2024).

This contamination problem carries cascading economic and environmental consequences. Contaminated material bales must be rejected at the materials recovery facility (MRF) level, diverting otherwise recoverable resources to landfill. Operators face increased operational cost, reduced material yield revenue, and mounting difficulty in meeting operational compliance targets increasingly demanded by corporate supply chains and international trade partners. The manual sorting approach—the predominant method in Malaysian MRFs—is fundamentally inadequate for addressing this challenge at scale.

## 1.2 Problem Statement

Manual waste sorting is characterised by three systemic failures. First, human visual classification of mixed waste is inconsistent, with error rates reported in the range of 30–40% across studies examining operator performance under realistic throughput conditions (Islam & Chowdhury, 2024). Second, manual sorting provides no machine-readable output, precluding data-driven quality tracking and process audit trail generation. Third, it creates occupational hazard exposure for workers who handle potentially toxic materials, including lithium batteries, electronic waste, and biological contaminants, without automated identification and isolation.

Advances in deep learning and computer vision have produced architectures capable of addressing these limitations. The YOLO (You Only Look Once) family of object detection models, and specifically the YOLOv8 generation with integrated instance segmentation capability, has demonstrated strong performance on heterogeneous waste classification tasks under real-world conditions (Ahmad et al., 2025; Arishi, 2025; Nahiduzzaman et al., 2025). However, a critical deployment gap persists in the literature: existing CV-based waste detection systems are evaluated in isolation from the industrial operational context in which they must function. Specifically, no integrated system has been demonstrated that combines (1) real-time contamination detection with pixel-level segmentation, (2) automated data pipeline ingestion and storage, (3) a live business intelligence dashboard for operational reporting, and (4) a gamified user-facing application for behavioural intervention at the source.

## 1.3 Research Objectives

This study aims to design, develop, and evaluate PurityLoop AI, an integrated waste contamination detection and analytics system, in pursuit of the following objectives:

1. **Operational Efficiency:** To replace manual waste sorting with a high-speed computer vision pipeline targeting a 30–40% increase in materials recovery facility throughput.
2. **Quality Assurance:** To ensure the purity of recycled material bales by identifying and flagging contaminants in real time using YOLOv8m-seg instance segmentation.
3. **Safety Enhancement:** To minimise workplace hazard exposure by automating the detection and isolation of hazardous waste categories, including lithium batteries and biological contaminants.
4. **Environmental Accountability:** To provide a data-driven, verifiable audit trail for corporate operational reporting, including Yield-sourced material yield recovery calculations.
5. **Behavioural Change:** To reduce contamination at the source through a personalised gamified Recycling Coach application.

## 1.4 Research Questions

The study addresses the following primary research questions:

**RQ1:** Can a YOLOv8m-seg model trained on a fused multi-dataset corpus achieve mAP@0.5 ≥ 0.85 on a held-out test set spanning nine waste categories including hazardous materials?

**RQ2:** How can a Python RPA automation pipeline effectively bridge real-time CV inference output to a business intelligence dashboard for operational reporting purposes?

**RQ3:** To what extent does a gamified recycling feedback application, integrated with facility-level purity data, influence user perception and declared intention to reduce contamination behaviour?

## 1.5 Scope and Delimitations

The scope of this study is defined as follows:

- **Detection domain:** Nine waste classes derived from the fused dataset corpus: PET Plastic, Aluminium, Glass, Paper, Cardboard, Organic/Food Waste, Battery (Hazardous), General Contaminant, and Other/Mixed.
- **Input modality:** Still images ingested via a Python watchdog-monitored hot folder, simulating industrial camera output during a conveyor-belt sorting operation.
- **Platform:** Streamlit-based web application with mobile-responsive user portal; Power BI analytics dashboard; SQLite database.
- **Evaluation environment:** Simulated conveyor belt demonstration during the WW12 Showcase using a dual-display configuration (Supervisor UI + Command Centre).
- **Exclusion:** This study does not include physical hardware integration with real conveyor belt systems, cloud deployment, or longitudinal behavioural tracking beyond the WW12 showcase period.

## 1.6 Significance of the Study

This study contributes to three intersecting fields. In the domain of **computer vision and machine learning**, it demonstrates a data-centric optimisation approach for multi-class instance segmentation on heterogeneous, real-world waste imagery, consistent with recent findings that pipeline-level decisions—data quality, augmentation strategy, and evaluation rigour—are as consequential as architectural choice (Ahmad et al., 2025). In the domain of **business analytics and operations management**, it operationalises DMAIC quality engineering within an AI model development workflow, bridging a gap identified by Pongboonchai-Empl et al. (2023) between Lean Six Sigma methodology and Industry 4.0 data-driven tools. In the domain of **sustainability and operational reporting**, it provides a practical implementation model for real-time AI-driven operational process accountability, responding to the growing regulatory and corporate demand for verifiable sustainability data documented by Mustafa et al. (2025).

## 1.7 Structure of the Proposal

The remainder of this proposal is organised as follows. Section 2 reviews the relevant literature across five thematic areas. Section 3 presents the integrated methodology framework, including DMAIC alignment, system requirements, architecture, and evaluation protocol. Section 4 presents the framework diagrams and system specification. Section 5 lists all references in APA 7th edition format.
