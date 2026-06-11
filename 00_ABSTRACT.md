# PurityLoop AI: An Integrated Computer Vision and Business Analytics Framework for Automated Waste Contamination Detection and Operational Reporting

**Capstone Project Proposal** | Sunway Business School | Department of Business Analytics
**Academic Year:** 2025/2026 | **Supervisor:** Dr. Narishah Mohamed Salleh

---

## Abstract

### Purpose
Malaysia's recycling sector faces a persistent quality crisis: an estimated 6.96% of potentially recyclable material—nearly one million tonnes annually—fails to enter the recycling stream due to contamination by hazardous and non-recyclable waste (SWCorp, 2024). Manual sorting, the current industry-standard method, is characterised by inconsistent accuracy, operator safety risks, and the absence of data-driven audit trails required for Environmental, Social, and Governance (ESG) compliance reporting. This study proposes PurityLoop AI, an end-to-end automated waste contamination detection and reporting system designed to address these limitations.

### Design/Methodology/Approach
PurityLoop AI adopts an Integrated Multi-Framework Methodology, combining the Define-Measure-Analyse-Improve-Control (DMAIC) quality engineering framework with the Cross-Industry Standard Process for Data Mining (CRISP-DM) and the Obtain-Scrub-Explore-Model-iNterpret (OSEMN) tactical pipeline. The system's machine learning core employs YOLOv8m-seg, a medium-scale, anchor-free, single-stage instance segmentation architecture, trained on a fused multi-dataset corpus of over 70,000 images spanning nine waste categories including recyclables, organic contaminants, and hazardous materials (e.g., lithium batteries). A Python Robotic Process Automation (RPA) hot-folder ingestion script automates data flow from simulated conveyor-belt camera input through inference, to a SQLite database and real-time Power BI analytics dashboard. A supplementary Streamlit-based Recycling Coach application operationalises a gamified behavioural intervention layer for source-level contamination reduction.

### Expected Outcomes
The system targets a minimum mAP@0.5 of 0.85 on a held-out test set, with real-time inference latency not exceeding 500 milliseconds per frame. The purity rate dashboard is expected to demonstrate a 30–40% improvement in sortable material throughput relative to manual baseline, with material yield recovery calculations traceable to peer-reviewed Material Yield Assessment (Yield) emission coefficients.

### Practical Implications
PurityLoop AI provides recycling facility operators with a deployable, cost-effective industrial automation tool that simultaneously generates verifiable ESG audit data and engages end-users through personalised environmental feedback. The system is designed for progressive scalability from simulated single-bin environments to multi-camera industrial conveyor belt configurations.

### Originality/Value
To the best of the authors' knowledge, this is among the first studies to integrate real-time computer vision contamination detection with a structured process audit trail and a gamified user behavioural intervention in a unified, end-to-end pipeline within the Malaysian recycling context. The proposed framework draws on the Lean Six Sigma DMAIC structure as its quality governance backbone, ensuring that all technical decisions are grounded in measurable, industry-standard process improvement principles.

---

**Keywords:** Computer Vision; YOLOv8; Waste Contamination Detection; Operational Reporting; DMAIC; Recycling Automation; Gamification; Instance Segmentation; Malaysia Solid Waste Management
