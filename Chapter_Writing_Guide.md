# PurityLoop AI: Chapter Writing Guide & Rubric

This document provides a breakdown of what needs to be written for every section in the Table of Contents, including ideas for elaboration and key references to include. Use this as a starting point to draft your assigned sections.

---

## Chapter 1: Introduction

**1.1 Background and Context [Naomi]**
*   **What to write:** Introduce the global and Malaysian solid waste management challenge. Discuss recycling targets (e.g., 40% by 2025) and how contamination derails these goals.
*   **References:** SWCorp Malaysia (2024), Pertanika Journal (2024).

**1.2 Problem Statement [Talvin]**
*   **What to write:** Describe the failures of manual sorting (30-40% error rate). Detail the lack of machine-readable output for operational reporting and the safety hazards (like lithium batteries).
*   **References:** Islam & Chowdhury (2024).

**1.3 Research Objectives [Chris]**
*   **What to write:** Use bullet points. 1) Operational efficiency (YOLOv8 pipeline). 2) Quality Assurance. 3) Safety Enhancement (detecting batteries). 4) Environmental Accountability (Operational dashboard). 5) Behavioural Change (Gamification app).

**1.4 Research Questions [Kong]**
*   **What to write:** Map to the objectives. E.g., "Can YOLOv8m-seg achieve mAP@0.5 ≥ 0.85?", "How can an RPA pipeline bridge CV inference to a Power BI dashboard?"

**1.5 Scope and Delimitations [Georgene]**
*   **What to write:** Define the 9 target classes. State that the project uses simulated conveyor belt imagery (not physical hardware integration) and a web dashboard for the WW12 showcase.

**1.6 Significance of the Study [Feng]**
*   **What to write:** Explain how this benefits three fields: 1) Computer Vision/ML, 2) Business Analytics (DMAIC integration), 3) Operational Reporting (verifiable material yield data). 
*   **References:** Pongboonchai-Empl et al. (2023), Mustafa et al. (2025).

**1.7 Structure of the Proposal [Naomi]**
*   **What to write:** A brief 1-paragraph roadmap stating what Chapters 2, 3, 4, and 5 will cover.

---

## Chapter 2: Literature Review

**2.1 Literature Search Protocol [Talvin]**
*   **What to write:** Briefly explain how you found your papers (Scopus, Google Scholar, years 2021-2026, Q1/Q2 indexing). 

**2.2 Theme 1: Deep Learning for Waste Classification [Talvin & Chris]**
*   **What to write:** Discuss the evolution from simple image classification (ResNet) to object detection (YOLO), and why single-stage segmentation (YOLOv8-seg) is best for irregular waste shapes. 
*   **References:** Jocher et al. (2023), Ahmad et al. (2025), Nahiduzzaman et al. (2025).

**2.3 Theme 2: Dataset Landscape & Fusion Strategies [Naomi]**
*   **What to write:** Review benchmark datasets like TrashNet and TACO. Highlight the critical gap: none have a "hazardous/battery" class. Explain why fusing multiple datasets (like Garbage Classification v2) solves this.
*   **References:** Proença & Simões (2020).

**2.4 Theme 3: Operational Reporting & Carbon Accountability [Feng]**
*   **What to write:** Discuss the shift from voluntary ESG to regulatory requirements. Explain the material yield Yield calculation formula.
*   **References:** Mustafa et al. (2025), BEIS/DESNZ (2023).

**2.5 Theme 4: Gamification for Behavioural Change [Georgene]**
*   **What to write:** Explain that facility sorting isn't enough; source-level behaviour must change. Discuss how token economies (Eco-Credits) promote pro-environmental behaviour.
*   **References:** Venturi et al. (2024).

**2.6 Theme 5: DMAIC & ML Quality [Chris]**
*   **What to write:** Map machine learning development to Lean Six Sigma (DMAIC). Discuss Andrej Karpathy's defensive ML protocols to prevent silent model failures.
*   **References:** Pongboonchai-Empl et al. (2023), Karpathy (2019).

**2.7 & 2.8 Critical Synthesis & Requirements [Chris & Kong]**
*   **What to write:** Summarize the literature gap (no end-to-end CV + ESG pipeline exists) and how requirements were gathered from these studies.

---

## Chapter 3: Methodology

**3.1 Integrated Multi-Framework Approach [Chris, Kong, Talvin, Georgene]**
*   **What to write:** Explain how different frameworks govern different parts of the project: Iterative Waterfall (Macro), DMAIC (Quality), BALC (Strategy), Iterative Prototyping (Web), and OSEMN (ML). Add Georgene's section on UI design (Wireframes).

**3.2 System Requirements Specification [Kong]**
*   **What to write:** Create two tables: Functional Requirements (Must have, Should have) and Non-Functional Requirements (mAP > 0.85, Latency < 500ms).

**3.3 Dataset Preparation [Naomi]**
*   **What to write:** Detail the cleaning process (removing duplicates), the 640x640 resize standard, color normalization, and your specific data augmentations (flips, rotations, brightness). Explain the 70/20/10 split.

**3.4 Model Architecture and Training [Talvin & Chris]**
*   **What to write:** 
    *   **Talvin:** Describe the YOLOv8m-seg backbone and the hyperparameter config (300 epochs, batch 16, SGD). Detail the two-phase training protocol. 
    *   **Chris:** Write about the Karpathy Checkpoints (Overfit-one-batch, visualize before net).

**3.5 Python RPA Ingestion Pipeline [Kong]**
*   **What to write:** Explain the 'watchdog' script. How does it monitor a folder for new camera images, run the YOLO inference, and save to SQLite?

**3.6 Evaluation Protocol [Chris]**
*   **What to write:** Define the metrics you will use to grade the model (mAP@0.5, mAP@0.5:0.95, Precision, Recall, F1-Score, Inference FPS).

**3.7 Ethical and Data Governance [Naomi]**
*   **What to write:** Briefly mention that user phone numbers are hashed (SHA-256) and no personally identifiable info is stored in plaintext.

---

## Chapter 4: Value Evaluation & Industry Impacts

**4.1 & 4.2 Industry Impact [Georgene & Feng]**
*   **What to write:** Discuss how Material Recovery Facilities (MRFs) will actually use this. How does it improve their bale purity rates and operational organization?

**4.3 Impact to the Model as New Knowledge [Chris]**
*   **What to write:** Explain that your approach (Data-centric tracking and fusion) is a novel contribution, proving that data quality is just as important as the model architecture.

**4.4 Summary of Expected ESG Benefits [Feng]**
*   **What to write:** Conclude how the real-time Power BI dashboard provides verifiable sustainability data for corporate auditing.

---

## Chapter 5: Project Management

**5.1 to 5.4 Overview, Gantt Chart, Delegation, Conclusion [Kong, Talvin, Georgene, Feng]**
*   **What to write:** Insert your Gantt chart images. Insert the Delegation of Work matrix. Write a strong concluding paragraph summarizing the vision of PurityLoop AI.
