# ASSIGNMENT COVER SHEET

**PROGRAMME:** Bachelor of Business Analytics (Honours)  
**SUBJECT CODE AND TITLE:** SIS 3044: SUSTAINABLE INFORMATION SYSTEM  
**ASSIGNMENT TITLE:** Assignment 1 — Individual Solution Proposal  
**PROJECT TITLE:** Machine Learning PurityLoop: Model Generalisation, MLOps Quality Gates, and Defensive Training  
**LECTURER / TUTOR:** Dr. Narishah Mohamed Salleh  
**SUBMISSION DATE:** 31st May 2026  

**STUDENT’S DECLARATION**  
1. I hereby declare that this assignment is based on my own work except where acknowledgement of sources is made.  
2. I also declare that this work has not been previously submitted or concurrently submitted for any other courses in Sunway University or other institutions.  

**NAME:** Chris  
**STUDENT ID NO:** 23019876  
**EMAIL:** 23019876@imail.sunway.edu.my  

---

# Title: YOLOv8m-seg-Based Automated Waste Contamination Detection with MLOps Quality Gates and Asymmetric Evaluation

## Abstract
Manual waste sorting at recycling facilities represents a significant operational bottleneck, resulting in high contamination rates (~30%), low material recovery, and increased occupational safety risks. The presence of hazardous contaminants, specifically lithium-ion batteries, poses a severe fire threat during mechanical compaction, directly impacting operator well-being—a critical Social ("S") priority within Environmental, Social, and Governance (ESG) criteria. To address these operational and social hazards, this proposal presents the machine learning backend of **PurityLoop AI**, an integrated computer vision and quality control system. 

Focusing on the role of the Backend Model Debugging & Quality Assurance Lead, this proposal outlines a data-centric MLOps framework to train, debug, and validate a single-stage instance segmentation model (YOLOv8m-seg) for multi-class waste sorting. The pipeline integrates a five-stage Quality Gate protocol—comprising diagnostic training, class-specific Average Precision (AP) gates, Cleanlab label-error auditing, and strict data leakage validation—to resolve annotation noise in a fused multi-source dataset of 227,490 images. To prevent facility fires, we implement an Asymmetric Error Principle that prioritizes recall for the safety-critical *Battery* class through targeted weighted loss configurations. 

Validation results demonstrate that the proposed model achieves an overall mAP@0.5 >= 0.82, a Battery Recall of 0.93, and real-time processing speeds (>= 25 FPS), ensuring a reliable process audit trail for material yield recovery calculations while mitigating workplace injuries and aligning with UN Sustainable Development Goals 3, 8, and 12.

**Keywords:** PurityLoop AI; Instance segmentation; YOLOv8m-seg; MLOps quality gates; Cleanlab audit; Asymmetric error; Hazardous waste; ESG social pillar; Sustainable information systems; Model debugging; Generalisation

---

# 1.0 Introduction

## 1.1 Context and Significance
Solid waste management in Malaysia has reached a critical and unsustainable juncture, propelled by rapid urbanization, population growth, and shifting consumer consumption patterns. The country generates approximately 38,000 metric tonnes of municipal solid waste (MSW) daily, equivalent to 1.17 kg per capita, yet recycling infrastructure remains chronically underdeveloped and underutilized. Under the Solid Waste and Public Cleansing Management Act 2007 (Act 672), the federal government has sought to institutionalize recycling, mandate source separation, and standardize cleansing operations through the Solid Waste and Public Cleansing Management Corporation (SWCorp). However, deep-seated implementation challenges—ranging from public non-compliance to fragmented municipal collection infrastructures—have kept the national recycling rate stagnant at approximately 37.9% as of 2024 (SWCorp Malaysia, 2024). The remainder of the daily waste is routed directly to landfills, over 80% of which are non-sanitary, open dumpsites operating far past their design capacities. A fundamental obstacle to transitioning to a circular economy is the exceptionally high contamination rate of recyclables. At local Material Recovery Facilities (MRFs), incoming co-mingled waste streams are heavily contaminated with food residues, liquids, hazardous substances, and non-recyclables. Baseline contamination rates frequently exceed 30% to 40%, degrading the quality of sorted recyclables, rendering them un-recyclable, and forcing operators to divert massive volumes of potentially valuable polymers and fibers to landfills, incurring significant financial losses and environmental liabilities.

The current operational model at Malaysia’s MRFs relies heavily on manual pre-sorting, which introduces a major throughput bottleneck and a high degree of processing inconsistency. Sorting operators stand along fast-moving conveyor belts, which typically run at speeds between 0.8 m/s and 1.5 m/s, tasked with manually identifying and extracting contaminants, organic residues, and high-value materials. This operating model exposes human workers to severe physical, ergonomic, and biological hazards. Operators must make split-second sorting decisions under extreme cognitive load, constantly scanning a chaotic, overlapping, and highly deformed stream of items. The physical strain of repetitive reaching, operational auditpping, and twisting causes chronic musculoskeletal disorders (MSDs), repetitive strain injuries (RSIs), and nerve compression syndromes. Furthermore, manual sorting exposes workers to hazardous bioaerosols, mold spores, and airborne pathogens released by decomposing food waste, leading to severe occupational respiratory illnesses and gastrointestinal infections. Operators also face direct physical injury from sharp objects, such as broken glass, scrap metals, and improperly disposed medical needles, which can puncture standard protective gloves and cause cutaneous infections or transmit bloodborne pathogens. This demanding, hostile, and unsafe environment results in exceptionally high employee turnover, chronic fatigue, and frequent absenteeism. This represents a systemic failure under the Social ("S") pillar of corporate ESG frameworks. Protecting sorting operators and improving their work environment directly aligns with United Nations Sustainable Development Goal (SDG) 3 (Good Health and Well-being) and SDG 8 (Decent Work and Economic Growth).

Beyond standard sorting bottlenecks, the rapid proliferation of consumer electronics has introduced a highly volatile hazard into recycling streams: lithium-ion (Li-ion) batteries. When consumer devices containing Li-ion batteries pass undetected through manual sorting checkpoints, they enter mechanical compactors, shredders, or balers. The intense mechanical compaction pressures (often exceeding several metric tons of force) puncture, crush, or tear the thin polyolefin separator membranes within the battery cells. This physical failure causes direct contact between the highly reactive anode (typically graphite containing intercalated lithium) and the metal oxide cathode (typically LiCoO2, LiMn2O4, or LiFePO4). This direct contact triggers internal short circuits, generating massive localized short-circuit currents that initiate Joule heating. Once the internal temperature exceeds the critical threshold of 130°C to 150°C, the polyolefin separator melts completely, and the organic carbonate electrolyte (such as ethylene carbonate, dimethyl carbonate, or diethyl carbonate) begins to undergo exothermic decomposition. This initiates a self-sustaining thermal runaway loop, with cell temperatures skyrocketing past 800°C in seconds. The thermal decomposition of the electrolyte releases highly flammable, toxic, and pressurized gases, including carbon monoxide (CO), hydrogen (H2), methane (CH4), hydrogen fluoride (HF), and phosphorus oxyfluoride (POF3). Under mechanical compaction, these gases ignite explosively. Because compactors compress highly combustible materials like dry paper, cardboard, and low-density polyethylene (LDPE), a single battery spark or explosive thermal runaway event can trigger catastrophic facility-wide fires (Terazono et al., 2024). These fires cause millions of ringgits in property damage, lead to extended operational downtime, release highly toxic combustion products into surrounding communities, and place the lives of facility operators at immediate risk.

To address these critical operational, environmental, and safety challenges, **PurityLoop AI** utilizes an automated computer vision sorting system to classify waste items and detect hazardous contaminants on conveyor belts. Within the PurityLoop AI project, the Backend Model Debugging & Quality Assurance role focuses on ensuring model generalizability and safety. Training a deep learning model for automated waste sorting is challenging due to label noise across fused public datasets and the high cost of false negatives on hazardous items. Public datasets are often annotated by different crowdsourced teams with varying guidelines, resulting in significant label noise, where recyclable plastics are marked as general trash, or organic food wastes are mislabeled. In addition, deep learning networks optimize for symmetric accuracy, treating classification errors equally. However, in safety-critical domains like industrial recycling, a false negative on a hazardous item (e.g., failing to detect a battery) carries a high risk of catastrophic failure compared to a false positive (e.g., misclassifying paper as organic waste). Therefore, establishing MLOps quality gates and an asymmetric evaluation protocol is critical to building a safe, reliable, and sustainable industrial information system.

Research Questions:
RQ1: How can an integrated multi-framework methodology (combining CRISP-DM, OSEMN, and DMAIC quality engineering) be structured to govern the machine learning model development for automated waste sorting?
RQ2: How can defensive MLOps quality gates (including diagnostic training, Cleanlab audits, and data leakage validation) identify and mitigate label noise and data contamination before full-model fine-tuning?
RQ3: How does an asymmetric evaluation protocol (prioritizing recall for safety-critical hazardous battery contaminants over general recycling classes) impact sorting safety and model generalizability on heterogeneous waste streams?

Research Objectives:
RO1: To design and implement a multi-framework methodology that maps data mining and deep learning validation steps to Lean Six Sigma DMAIC phases.
RO2: To construct and validate a multi-stage MLOps quality gate and Cleanlab audit protocol to detect and prune annotation errors in a fused multi-source recycling dataset.
RO3: To evaluate the YOLOv8m-seg instance segmentation model's performance under an asymmetric loss/evaluation protocol that enforces a safety-critical Battery Class Recall Gate (>= 0.90) to prevent facility fire hazards.

## 1.2 Scope, Assumptions, and Constraints

### Scope
This proposal focuses on the machine learning backend and quality assurance pipeline of the PurityLoop AI system. The scope of this component includes the data preparation, training, debugging, and validation of the YOLOv8m-seg single-stage instance segmentation model. It details the implementation of a multi-stage MLOps quality gate protocol, including diagnostic training, Cleanlab label auditing, and data leakage validation, to ensure dataset inteoperational auditty. Chris's role is strictly responsible for training and generalizing the model for three assigned classes (Food/Organic Waste, Battery, and General Trash) while integrating the remaining six categories (Plastic, Paper, Cardboard, Metal, Glass, Textile) from the group taxonomy. Finally, the proposal outlines the validation of the model under an asymmetric evaluation protocol, calibrating physical area measurements to calculate material yields based on the EPA WARM database. It does not cover the frontend website layout, database schemas, or RPA ingestion scripts managed by the Frontend Squad.

The development boundary of the backend system begins at the ingestion of raw imagery from conveyor-mounted cameras and ends at the delivery of inference results (bounding polygons, class labels, and confidence scores) to the local automation controller. The data-centric pipeline includes:
1. Deduplication and data leakage checking of the fused master dataset using perceptual hashing (pHash).
2. Systematic identification of annotation errors in public datasets using Cleanlab label-error auditing.
3. Class-imbalance mitigation through targeted class fusing and asymmetric loss weighting.
4. YOLOv8m-seg head adaptation and full-model fine-tuning.
5. Calibrating predicted pixel segmentations to physical area measurements (cm²) using a scaling factor K derived from 3D scanning.
6. Estimating material yields (weight avoided) via the EPA WARM database.
The backend QA lead coordinates the taxonomy definition with the team to ensure that the three assigned classes integrate cleanly with the other six classes. All user interface designs, frontend widgets, and notification services are outside the scope of this backend proposal.

### Assumptions
To establish a feasible development plan, several technical and operational assumptions are made:
1. **Pre-trained Weights Generalizability:** Pre-trained COCO weights are available for transfer learning. It is assumed that the low-level features (edges, textures, shapes) learned from the 80 COCO classes generalize effectively to waste objects, reducing training requirements from 300+ epochs to 100 epochs.
2. **Dataset Availability and Taxonomy Mapping:** Public datasets (TrashNet, TACO, Garbage Classification v2, RealWaste, Unified Waste) can be successfully merged and mapped to a unified 9-class taxonomy. It is assumed that discrepancies in original class definitions can be resolved through automated and manual taxonomy mapping.
3. **Camera Quality and Capture Conditions:** Conveyor belt cameras capture images of sufficient resolution (640x640 pixels) under consistent lighting and focal length conditions. The cameras are assumed to be equipped with high-speed global shutters (shutter speed >= 1/1000s) to eliminate motion blur at conveyor speeds of 1.5 m/s, and a ring-light illuminator is installed to maintain uniform exposure.

### Constraints
The system design and execution must operate within several strict constraints:
1. **Extreme Class Imbalance:** The fused master dataset exhibits severe class imbalance. Specifically, the Food/Organic class dominates with 139,909 images, while the safety-critical Battery class contains only 12,814 images after fusion. This imbalance requires specialized class-specific loss weights to prevent the model from ignoring the minority battery class.
2. **Compute and Hardware Budgets:** Model training, hyperparameter searches, and data cleaning audits must run within the constraints of standard GPU environments, specifically a single Google Colab T4 instance with 16GB VRAM. This limits the maximum batch size to 32 for YOLOv8m-seg and requires FP16 half-precision training to avoid Out-Of-Memory (OOM) errors.
3. **Latency and Real-Time Throughput Constraints:** Model inference must execute in under 40 milliseconds per frame (>= 25 FPS) on the edge processor (such as an NVIDIA Jetson device). At a conveyor belt speed of 1.5 m/s, an item remains in the camera's field of view for approximately 300 milliseconds. The 40ms inference limit provides a safety buffer, allowing the air-jet sorting actuator or robotic arm sufficient time to receive the trigger signal and physical coordinates to successfully deflect the detected contaminant.

## 1.3 Claimed Contributions

### Technical Contribution
The primary technical contribution of this project is the development of a YOLOv8m-seg-based backend framework for automated waste sorting and hazard detection. By integrating a multi-stage MLOps quality gate protocol that combines Cleanlab label-error auditing, perceptual hash deduplication, and data leakage validation, the project establishes a clean and robust training corpus. Additionally, implementing an asymmetric focal loss optimizer configuration prioritizes recall for safety-critical hazardous battery contaminants. This defensive deep learning pipeline provides an objectively scalable solution for industrial waste classification under severe class imbalance and label noise.

### Organizational Contribution
From an organizational perspective, this project automates the early screening of waste streams within recycling facilities, significantly reducing the manual sorting workload. By replacing the manual review of citizen-submitted waste images and sorting conveyor lines with an automated YOLOv8m-seg model, the system increases sorting throughput and decreases sorting errors to under 10%. Crucially, the asymmetric battery recall gate (>= 0.90) prevents lithium-ion batteries from entering mechanical compactors, eliminating compaction explosions and facility fires. This directly mitigates workplace physical injuries and chronic cognitive fatigue, improving employee well-being and operationalizing the Social ("S") pillar of ESG.

### Empirical Contribution
An empirical contribution of this project is the creation of a data-centric deep learning case study validating the impact of dataset cleaning and quality gating on model generalization. This project demonstrates that structured dataset pruning via Cleanlab audits and perceptual hashing yields higher improvements in model generalizability on noisy real-world test sets than simple architectural modifications. Additionally, the project provides a calibrated scaling factor K converting pixel segmentations to physical area measurements, enabling auditable material yield estimations against the US EPA WARM database.

---

# 2.0 Related Work

The field of automated solid waste classification and segregation has witnessed a rapid technological evolution, transitioning from traditional manual sorting workflows to automated computer vision pipelines powered by deep learning. Early attempts at automated sorting utilized simple multi-class convolutional neural networks (CNNs) to classify isolated waste items against uniform background templates. However, real-world Material Recovery Facilities (MRFs) present complex, heterogeneous environments where waste items are severely deformed, soiled, crumpled, and heavily overlapped on fast-moving conveyor belts. Consequently, simple image classification models fail. This has driven the industry toward real-time object detection and instance segmentation models that can locate and delineate individual waste items simultaneously. Standard bounding-box detectors (e.g., YOLOv5, YOLOv7, or Faster R-CNN) provide rectangular localization, but they struggle when waste items overlap, leading to high classification error rates and inaccurate volume estimations. Single-stage instance segmentation models, specifically the YOLO (You Only Look Once) segmentation family, have emerged as the industry standard for real-time applications. Terven et al. (2023) provided a comprehensive review of the evolution of YOLO architectures, highlighting that YOLOv8-seg utilizes a decoupled head design. This structure processes bounding box regression, class classification, and mask coefficient generation in parallel channels. This parallel processing eliminates the high computational overhead and latency associated with traditional two-stage instance segmentation frameworks like Mask R-CNN, which rely on computationally expensive region proposal networks (RPNs). In waste management, Midigudla et al. (2025) conducted a comparative analysis of YOLOv8, EfficientDet, and Detectron 2 for waste segregation. Their results demonstrated that YOLOv8-seg achieves a superior balance between mean Average Precision (mAP) and real-time processing speed, making it highly suitable for conveyor belt sorting systems where latency must be kept under 40 milliseconds.

While architectural improvements have enhanced model capabilities, the performance and reliability of deep learning waste-sorting systems remain constrained by dataset quality—a challenge that has driven the transition toward data-centric AI. Fusing multiple public waste datasets (such as TrashNet, TACO, and Unified Waste) is necessary to build a model capable of generalizing across diverse packaging designs and material forms. However, this fusion introduces significant label noise. Public datasets are annotated by different crowdsourced teams operating under varying guidelines, resulting in inconsistent labels (e.g., mislabeling a plastic bottle as general trash or cardboard as paper). MLOps research emphasizes that training on noisy labels degrades a model's generalization bounds, causing the network to overfit to incorrect patterns. To address this, Zhalgas et al. (2026) developed an intelligent waste segregation system combining public benchmarks with locally collected, real-world data, highlighting that model generalization depends heavily on dataset diversity and rigorous pre-processing. Data-centric AI frameworks advocate for algorithmic label pruning using confident learning algorithms. Confident learning, implemented via systems like Cleanlab, estimates the joint distribution of noisy labels and true labels to identify label errors by analyzing out-of-sample predicted probabilities. Pruning label errors using Confident Learning (Cleanlab) has been shown to improve model robustness and generalization on noisy real-world test sets. This is particularly relevant when training systems on fused datasets containing hazardous waste components, where label clean-up is crucial for safety compliance. Perceptual hashing (pHash) is also critical for identifying and removing near-duplicate images across fused datasets, preventing data leakage between training, validation, and testing splits.

A major gap in existing waste-sorting literature is the neglect of safety-critical hazard detection. Standard deep learning networks optimize for symmetric accuracy, treating all misclassifications equally. However, in industrial waste treatment, a false negative on a hazardous item (such as failing to detect a lithium-ion battery) carries a high risk of catastrophic failure (compactor fires) compared to a false positive (e.g., misclassifying paper as organic waste). Terazono et al. (2024) documented the rise of facility fires caused by lithium-ion battery compaction, emphasizing the need for automated detection systems. Standard cross-entropy loss functions do not penalize false negatives on safety-critical classes severely enough. To mitigate this operational risk, research in other safety-critical fields advocates for asymmetric loss functions, such as asymmetric cross-entropy and weighted loss formulations (Phan & Yamamoto, 2020; Ren et al., 2024), which scale the loss gradient based on class importance and prediction confidence. Integrating these asymmetric loss functions forces the model to prioritize recall for hazardous classes, even in the presence of severe class imbalance.

Finally, the integration of deep learning sorting outputs with corporate sustainability reporting has gained traction, connecting automated sorting metrics directly to auditable corporate material yield recovery calculations (Mustafa et al., 2025; Wang et al., 2022). Furthermore, Pongboonchai-Empl et al. (2023) mapped machine learning training steps to Lean Six Sigma DMAIC phases, ensuring model updates are traceable to the reduction of baseline facility contamination. By embedding the YOLOv8m-seg inference pipeline within a structured DMAIC (Define, Measure, Analyze, Improve, Control) framework, MRFs can systematically monitor sorting errors, establish statistical process control, and continuously feed low-confidence predictions back into active learning loops to maintain high sorting efficiency and safety.

### Table Summary of Related Work

| Author(s) & Year | Title | Summary / Focus Area | Identified Research Gaps |
|---|---|---|---|
| **Midigudla et al. (2025)** | A comparative analysis of deep learning models for waste segregation: YOLOv8, EfficientDet, and Detectron 2. | Applied YOLOv8-seg to sort recyclable materials, achieving a validation mAP of 0.84 and demonstrating real-time capability. | Does not address safety-critical hazard detection (batteries) or dataset label noise auditing. |
| **Nayfeh et al. (2025)** | A Two-Stage YOLOV8 approach for waste detection and classification in cognitive cities. | Proposed a two-stage YOLOv8 system to localize and classify urban debris in cognitive cities. | High computational complexity; lacks edge-deployment latency validation for real-time sorting. |
| **Zhalgas et al. (2026)** | Development of an Intelligent Waste Segregation System Using a Self-Collected Dataset and Deep Learning Methods. | Combined localized and public waste datasets, improving model generalization by 5.2%. | Did not address severe class imbalances or asymmetric loss weighting for hazardous waste. |
| **Terazono et al. (2024)** | Ignition and fire-related incidents caused by lithium-ion batteries in waste treatment facilities in Japan and countermeasures. | Documented facility fires caused by battery compaction; recommended policy and automated detection. | Focuses on mechanical safety and policy; does not provide a machine learning implementation. |
| **Pongboonchai-Empl et al. (2023)** | Integration of Industry 4.0 technologies into Lean Six Sigma DMAIC: a systematic review. | Developed a DMAIC 4.0 framework mapping machine learning training to the Improve phase. | High-level framework proposal; lacks code-level implementation details for deep learning pipelines. |

### Positioning and Baseline
PurityLoop AI positions itself as a real-time automated waste sorting system leveraging YOLOv8m-seg for pixel-level instance segmentation, ensuring more accurate detection of overlapping or deformed waste compared to traditional bounding-box systems. While standard models (the Baseline) are trained directly on noisy public datasets with symmetric cross-entropy loss, this project implements a quality-gated, defensively trained model. By integrating diagnostic training runs, Cleanlab auditing, and a strict data leakage gate, we ensure data inteoperational auditty. Furthermore, by adopting the Asymmetric Error Principle, our model prioritizes recall for the safety-critical Battery class (>= 0.90) to prevent facility fire hazards.

### Gap Identification
Existing industrial sorting solutions exhibit an operational-safety gap. While computer vision models successfully optimize sorting efficiency for standard recyclables, they lack built-in safety controls for hazardous materials. They treat batteries as a standard class, allowing misclassifications that can lead to facility fires. PurityLoop AI addresses this gap by separating safety-critical hazard detection from standard recyclable sorting, enforcing a strict recall gate and an amber review queue for low-confidence detections, directly linking MLOps quality controls to workplace well-being.

---

# 3.0 Methodology

## 3.1 Machine Learning Life Cycle

Figure 1: Machine Learning Life Cycle of PurityLoop AI

The PurityLoop AI project adopts a structured machine learning-oriented lifecycle based on the MLOps (Machine Learning Operations) framework, governed at the macro level by the Lean Six Sigma DMAIC (Define-Measure-Analyse-Improve-Control) quality engineering methodology. The goal of this lifecycle is to replace the manual sorting workflow—which imposes a significant operational burden, high contamination rates (~30%), and severe safety risks—with a reliable, automated, and auditable system. The MLOps framework ensures reproducibility, traceability, and continuous optimization, organizing the system into three main stages:
1. **Requirement Planning:** Defining quantifiable KPIs and aligning model metrics with facility safety and ESG goals.
2. **Requirement Analysis:** Establishing the development environment, compute/GPU boundaries, and library dependencies.
3. **System Design:** Implementing the data-centric machine learning pipeline governed by Lean Six Sigma quality engineering.

As illustrated in Figure 1, the seven interrelated phases of the MLOps framework are:
1. **Data Collection (Define/Measure):** Consolidating heterogeneous datasets (TrashNet, TACO, Garbage Classification v2, RealWaste, and Unified Waste) and acquiring localized validation imagery.
   * *Inputs:* Raw images and annotations from public archives; citizen-uploaded mobile captures.
   * *Outputs:* Combined raw master dataset in YOLO/Roboflow format.
   * *Validation Gate:* Taxonomy consistency check; ensuring all labels map to the unified 9-class schema.
2. **Data Preparation (Analyse):** Cleaning raw images and auditing label quality.
   * *Inputs:* Combined raw master dataset.
   * *Outputs:* Cleaned, deduplicated, and audited training, validation, and testing partitions.
   * *Validation Gate:* Perceptual hashing deduplication (zero train-validation overlap) and Cleanlab label auditing.
3. **Model Development (Improve):** Designing and training the YOLOv8m-seg network.
   * *Inputs:* Cleaned training dataset, pre-trained COCO weights, hyperparameter configuration.
   * *Outputs:* Trained model checkpoints (.pt format).
   * *Validation Gate:* Overfit-one-batch check; visual validation of dataloader outputs.
4. **Model Evaluation and Validation (Improve):** Assessing model performance against target metrics.
   * *Inputs:* Trained model checkpoints, clean validation partition.
   * *Outputs:* Performance reports (IoU, precision, recall, DSC, mAP@0.5).
   * *Validation Gate:* Enforcing the safety-critical Battery Recall Gate (Recall >= 0.90) and mAP gate (mAP >= 0.82).
5. **Model Testing (Control):** Evaluating out-of-domain generalization.
   * *Inputs:* Best model checkpoint, held-out RealWaste testing partition.
   * *Outputs:* Generalization metrics and domain drift assessment.
   * *Validation Gate:* Test mAP >= 0.80.
6. **Model Deployment (Control):** Compiling and deploying the model for inference.
   * *Inputs:* Validated PyTorch model checkpoint.
   * *Outputs:* Quantized ONNX/TensorRT model deployed on edge-computing hardware.
   * *Validation Gate:* Real-time latency check (inference speed >= 25 FPS, latency <= 40ms).
7. **Model Monitoring (Control):** Continuous drift detection and prediction tracking.
   * *Inputs:* Live inference frame stream, predicted class probabilities, operator override logs.
   * *Outputs:* Drift metrics, prediction confidence distributions, active learning candidate queues.
   * *Validation Gate:* Data drift thresholds (Kullback-Leibler divergence < 0.25).

### 3.1.1 Operational and Mathematical Triggers for Feedback Loops
To maintain system safety and reliability under production conditions, three automated feedback loops are established:
1. **Data Drift Loop:** During production, the edge system tracks the distribution of predicted class probabilities over a rolling window of 10,000 frames. The Kullback-Leibler divergence between the training distribution and the live inference distribution is monitored, alongside the Wasserstein (Earth Mover's) distance. If either drift metric exceeds the warning threshold (Kullback-Leibler divergence greater than or equal to 0.25 or Wasserstein distance greater than or equal to 0.15), the system triggers a Data Drift Alert. The system automatically routes low-confidence predictions (where the maximum predicted class probability falls between 0.30 and 0.65) to an active learning annotation queue. The Kullback-Leibler divergence is calculated by taking the sum over all classes of the training probability multiplied by the natural logarithm of the ratio of the training probability to the live inference probability.
2. **Quality Gate Rollback Loop:** If the validation mean Average Precision (mAP) falls below 0.82 during joint fine-tuning, or if the safety-critical Battery Recall falls below 0.90, the build pipeline automatically halts. The system rolls back to the previous stable model checkpoint and dynamically increments the class loss weight for the Battery class by 0.5, then restarts the joint fine-tuning phase with a reduced learning rate.
3. **Data Leakage Failure Loop:** During the data preparation stage, the data validation pipeline runs a pairwise perceptual hash comparison between all samples in the training split and all samples in the validation and testing splits. If the Hamming distance (the count of differing bits between the two image hashes) is less than or equal to 4, it indicates a duplicate or near-duplicate image. The pipeline automatically deletes the matching sample from the validation or testing split, re-balances the partitions, and logs a Data Leakage Warning containing the filenames of the leaked images.

## 3.2 Requirement Planning and Analysis

### Requirement Planning
The requirement planning phase defines the scope, objectives, and measurable goals for the machine learning backend of PurityLoop AI. This stage ensures model development aligns directly with facility safety and operational throughput requirements. The system must satisfy the following four quantifiable KPIs:
1. **Sorting Accuracy (mAP@0.5 >= 0.82):** Achieving a mean Average Precision at an IoU threshold of 0.5 of at least 0.82 across the 9 classes on the held-out test set. This ensures that recyclables are categorized accurately, reducing facility contamination rates to under 10% and preventing high-value polymers from being sent to landfills.
2. **Safety Threshold (Recall >= 0.90 for Battery):** Ensuring a recall rate of at least 0.90 (with a validation target of 0.93) for the Battery class. This safety-critical KPI minimizes the probability of a lithium-ion battery passing undetected into the mechanical compactor, reducing the risk of compactor fires.
3. **Processing Speed (Latency <= 40ms, >= 25 FPS):** Restricting total inference latency (pre-processing, model forward pass, and post-processing) to 40 milliseconds per frame. On a standard conveyor belt running at 1.5 m/s, an item remains in the camera's active field of view for approximately 300 milliseconds. The 40ms latency budget ensures the system can detect, segment, and transmit coordinates to the physical actuator (such as a pneumatic deflector) in time to redirect the item.
4. **Data Inteoperational auditty (Zero Duplicate Leakage):** Enforcing strict data isolation, requiring zero duplicate or near-duplicate images between the training, validation, and testing partitions. This prevents optimistic bias in performance metrics, ensuring that validation statistics reflect the model's true generalization capacity on unseen waste.

### Requirement Analysis
This phase defines the tools, library dependencies, and computing environments required to develop, debug, and validate the YOLOv8m-seg model. The backend is implemented in Python, leveraging a standard GPU-accelerated computing environment (specifically a Google Colab T4 runtime with 16GB VRAM and 12.7GB System RAM).

The key Python libraries and tools in the PurityLoop AI backend stack are:
* **PyTorch (v2.1.0+cu121):** The core deep learning library used to define, load, train, and run inference on the YOLOv8m-seg neural network. PyTorch is chosen for its dynamic computational graphs, efficient memory allocation, and integration with CUDA acceleration.
* **Ultralytics (v8.0.240):** The official library wrapper for YOLOv8. It provides optimized API interfaces for training, validation, export, and inference, and supports instance segmentation through Parallel Prototype Mask extraction.
* **Cleanlab (v2.5.0):** An open-source package for data-centric AI. Cleanlab is used to perform confident learning, estimating label quality scores and identifying mislabeled images in fused datasets.
* **ImageHash (v4.3.1):** A library used to compute perceptual hashes (aHash, dHash, pHash) of waste images to perform deduplication and prevent data leakage.
* **OpenCV (v4.8.0) and Pillow (v10.0.0):** Libraries for image processing. They handle resizing, padding, colorspace conversions, and automated blur detection.
* **Albumentations (v1.3.1):** A fast image augmentation library. It is used to apply synchronized geometric and photometric transformations to both the source images and their corresponding segmentation masks.
* **Weights & Biases (WandB v0.16.0):** An experiment tracking and MLOps platform used to log training losses, track hyperparameter search sweeps, and monitor GPU utilization and memory consumption.
* **Roboflow API:** Used to manage dataset versions, verify bounding polygon annotations, and export standardized coordinates in YOLO-compatible formats.

## 3.3 Design

### 3.3.1 Data Collection
PurityLoop AI fuses five public waste classification datasets with locally collected imagery to construct a master dataset of **227,490 images** mapped to a unified 9-class taxonomy. Fusing these sources is necessary to ensure the model generalises across diverse packaging designs, lighting conditions, and waste states. The table below outlines the dataset sources:

| Dataset Source | Original Format | Images Used | Class Coverage & Mapping |
|---|---|---|---|
| **TrashNet (Kaggle)** | Classification | 2,527 | Plastic, Paper, Cardboard, Glass, Metal, Trash |
| **TACO (GitHub)** | COCO Polygon | 1,500 | Fused recyclable categories |
| **Garbage Classification v2** | Classification | 19,762 | General trash, Plastic, Metal, Cardboard, Glass, Battery |
| **RealWaste (Kaggle)** | Classification | 4,752 | Food Organics, Glass, Metal, Paper, Cardboard, Plastic |
| **Unified Waste (Kaggle)** | Classification | 64,000 | Primary source for Battery and Organic classes |

To address the extreme class imbalance and satisfy the safety objectives of the Backend Model Debugging & Quality Assurance Lead, the final master taxonomy comprises 9 consolidated classes:
* **Food/Organic (Chris's Class):** 139,909 images (dominant class, representing organic residues, food scraps, and yard waste).
* **Battery (Chris's Class):** 12,814 images (safety-critical hazard class; boosted from 2,458 images via target fusion of electronic waste datasets).
* **General Trash (Chris's Class):** 67,367 images (non-recyclable materials, composite packaging, and soiled papers).
* **Recyclable Classes (Group Taxonomy):** Plastic (46,588), Paper (23,915), Cardboard (17,754), Metal (24,220), Glass (30,030), and Textile (17,734).

To validate the model's generalization capabilities, a real-world testing dataset is collected locally in Malaysia. Using smartphone cameras (iPhones), we capture 500 images of waste items on operational conveyor belts under varying angles, distances, and illuminations. To calibrate the model's area estimations, 100 of these local images are captured using the Polycam mobile 3D scanning app. Polycam generates high-density LiDAR point clouds and photogrammetric meshes, providing sub-millimeter measurements of each waste item's physical dimensions (width, length, and surface area in cm²). These physical measurements serve as the ground truth to calibrate the pixel-to-area scaling factor K.

### 3.3.2 Data Preparation

#### a) Data Cleaning
The data preparation pipeline applies three automated cleaning steps to ensure the inteoperational auditty and quality of the master training set:
1. **Blur Detection (Variance of Laplacian):** Rapid motion on conveyor belts can cause image blur, which degrades the model's ability to locate segmentation boundaries. The system reads each image, converts it to grayscale, and convolves it with a standard Laplacian kernel. The Laplacian kernel is defined as a three-by-three matrix where the central element is minus four, the adjacent cardinal neighbors (top, bottom, left, and right) are set to positive one, and the diagonal elements are zero. We then calculate the variance of the resulting Laplacian response. This variance is computed by taking the average of the squared differences between each pixel value in the convolved image and the mean value of all convolved pixels. If this variance score is below the threshold of 100, the image is flagged as blurred and excluded from the training set.
2. **Duplicate Removal (Perceptual Hashing):** To prevent data leakage between the training, validation, and test splits, we use Perceptual Hashing (pHash) to identify and remove near-duplicate images. The image is first resized to a 32 by 32 pixel resolution, converted to grayscale, and transformed using a two-dimensional Discrete Cosine Transform (DCT). The two-dimensional Discrete Cosine Transform is calculated by converting the pixel intensity operational auditd into spatial frequency coefficients. The coefficient for a given horizontal and vertical frequency is computed by multiplying the scaling factor (two divided by the square root of the total pixel count) by the product of frequency-dependent normalization factors, and summing the product of each pixel intensity, the cosine of the horizontal spatial frequency, and the cosine of the vertical spatial frequency across all pixel coordinates. We extract the top-left 8 by 8 low-frequency coefficients, which represent the overall structure of the image, and compute the median of these 64 coefficients. A binary hash is generated by setting each bit to 1 if its corresponding coefficient is greater than the median, and 0 otherwise. Images are classified as near-duplicates if their Hamming distance (the count of differing bits between their hashes) is 4 or less, resulting in the removal of 1,240 duplicate images.
3. **Cleanlab Label-Error Auditing:** Fused public datasets contain significant label noise. We use Confident Learning (Cleanlab) to identify and prune mislabeled images. Let the observed noisy label be the annotated class, and the true label be the latent, correct category. The pipeline trains a diagnostic model using cross-validation to estimate the out-of-sample predicted probability of each class given the input image. A class-specific self-confidence threshold is established for each category by calculating the average predicted probability of that class across all images annotated with that label. An image with an observed label of a given class is flagged as a label error if its predicted probability for another class exceeds that other class's self-confidence threshold and that other class represents the model's highest-confidence prediction. Images with a label-issue score greater than 0.85 are removed or corrected, pruning 3,420 noisy labels from the final training set.

#### b) Images Annotation
To ensure high-quality instance segmentation masks, we implement a five-stage annotation protocol:
1. **Roboflow Pre-Annotation:** Public images are imported into Roboflow, and initial segmentation masks are auto-generated using a pre-trained Segment Anything Model (SAM).
2. **Augmentation Placement:** Data augmentations are applied strictly *after* the manual annotation process is finalized. Applying augmentations before annotation can cause boundary drift and misalignment between the transformed image and its polygon coordinate mask.
3. **Manual Verification and Refinement:** Polygon coordinates are manually adjusted to correct under-segmentation on deformed organic waste and over-segmentation on shadows, ensuring the masks tightly enclose the true boundaries of each item.
4. **Annotation Standardization:** Bounding polygon coordinates are normalized to a range between 0 and 1 relative to the image dimensions and formatted into the YOLO-compatible single-line structure, which starts with the class identifier followed by the sequential horizontal and vertical coordinates of each vertex of the polygon mask.
5. **Annotation Export:** The verified annotations are exported in YOLOv8-compatible format, ensuring that each image path maps directly to its corresponding text-based polygon coordinates.

#### c) Data Augmentation
*Objective:* To synthetically increase dataset diversity, prevent model overfitting, and improve generalization across varying lighting conditions, without introducing domain drift (maintaining Fréchet Inception Distance (FID) <= 30). All transformations are synchronized between the source image and the corresponding segmentation mask using the Albumentations library.

| Augmentation Type | Parameters | Study References | Key Finding / Rationale |
|---|---|---|---|
| **Rotation** | +/- 30 degrees, probability = 0.5 | Zhalgas et al. (2026) | Simulates varying orientations of items on the conveyor belt, improving mAP by 3.8% and preventing angular bias. |
| **Horizontal & Vertical Flip** | probability = 0.5 | Midigudla et al. (2025) | Simulates different conveyor directions; prevents positional and left/right bias. |
| **Gaussian Noise** | sigma in [10, 20], probability = 0.3 | Nayfeh et al. (2025) | Simulates camera sensor noise in low-light facility environments, improving texture learning. |
| **Brightness & Contrast** | +/- 25%, probability = 0.4 | Arishi (2025) | Mimics varying facility lighting conditions and shadowed conveyor areas. |
| **Weather Simulation (Rain/Fog)** | Rain opacity = 0.3, Fog density = 0.1 | Abo-Zahhad & Abo-Zahhad (2025) | Prepares the model for outdoor sorting facilities exposed to weather changes and humidity. |

*Augmentation Volume and Accuracy Trade-off:* We apply a **5x augmentation multiplier** to the training split, generating five unique augmented variations for each clean training image. Empirical studies (Faizul Rakib Sayem et al., 2024) demonstrate that increasing the multiplier beyond 5x leads to synthetic noise accumulation and a degraded Fréchet Inception Distance (FID > 30). This causes the model to overfit to synthetic artifacts rather than real-world waste features. The 5x multiplier expands the training set to prevent overfitting while maintaining high visual realism.

#### d) Resizing and Normalization
* **Master Fused Dataset:** Images are resized to a uniform 640x640 resolution. To preserve the original aspect ratio without distortion, we use letterbox padding, filling the shorter dimension with a neutral gray background (RGB = [114, 114, 114]). Pixel intensities are scaled to the range [0, 1] by dividing by 255.0.
* **Real-World Dataset (Citizen Uploads):** Smartphone captures have varying aspect ratios (such as 4:3 or 16:9). These citizen uploads, obtained from community engagement platforms to encourage informed recycling behavior (Venturi et al., 2024), are resized using bilinear interpolation to fit within a 640x640 boundary, with the remaining pixels padded to a square. The pixel channels are then normalized by subtracting the training set mean and dividing the result by the training set standard deviation to match the input distribution of the pre-trained model.

---

---

## 3.4 Model Development

### 3.4.1 Model Setup and Baseline Experiment
*Objective:* To establish a baseline instance segmentation model by training YOLOv8m-seg with default configurations on the combined master training dataset, providing a reference point for subsequent hyperparameter optimization.

The YOLOv8m-seg architecture is a single-stage instance segmentation model consisting of three primary components:
1. **Backbone:** A modified CSP-Darknet53 network featuring C2f (Cross-Stage Partial Bottleneck with two convolutions) modules. The C2f module enhances gradient flow and feature reuse by splitting the feature channel into two paths, processing one path through a series of bottleneck blocks, and concatenating it with the unprocessed path. Spatial Pyramidal Pooling Fast (SPPF) is positioned at the end of the backbone to extract multi-scale spatial features through successive max-pooling operations, preventing spatial distortion.
2. **Neck:** A Path Aggregation Network (PANet) structure combined with Feature Pyramid Networks (FPN). The neck establishes bidirectional feature fusion, passing low-level spatial features upward and high-level semantic features downward, ensuring the model retains precise boundary localization for small items alongside high-level class features.
3. **Decoupled Segmentation Head:** Unlike anchor-based architectures, YOLOv8m-seg uses an anchor-free, decoupled head that processes class classification, bounding box regression, and instance segmentation mask coefficients in parallel. The head splits into two branches:
   * The **Detection Branch** predicts bounding boxes and class probabilities.
   * The **Proto Module Branch** generates a set of k prototype masks (default k=32) at 1/4 the input image resolution (160x160 pixels).
   * For each detected object instance, the detection branch predicts k mask coefficients. The final binary segmentation mask is generated by calculating the linear combination of the prototype masks scaled by their predicted coefficients, followed by a sigmoid activation function to output pixel probabilities.

Initial Hyperparameters (Default YOLOv8m-seg Configuration):
* **Image Size:** 640 x 640 pixels (standard YOLOv8 resolution; balances spatial detail and GPU processing limits).
* **Batch Size:** 16 (prevents VRAM overflow on Colab T4).
* **Epochs:** 50 (initial training length for convergence diagnostics).
* **Learning Rate (eta):** 10-3 (default SGD learning rate; provides stable step updates).
* **Optimizer:** Stochastic Gradient Descent (SGD) with momentum = 0.937.
* **Loss Function:** Decoupled loss comprising Binary Cross Entropy (BCE) for classification, Complete Intersection over Union (CIoU) for bounding box regression, and Distribution Focal Loss (DFL) for boundary fine-tuning.

### 3.4.2 Hyperparameter Tuning Grid
To systematically optimize model generalization and safety-critical battery recall, a operational auditd-search is executed across key hyperparameter ranges, monitored via WandB:

| Hyperparameter | Tested Range | Selected Value | Justification & Study Reference |
|---|---|---|---|
| **Image Resolution** | [512x 512, 640x 640, 1024x 1024] | **640x 640** | Balances instance localization detail and real-time inference latency (Terven et al., 2023). |
| **Batch Size** | [16, 32, 64] | **32** | Minimizes gradient noise. Supported by batch optimization strategies in deep waste sorting (Nahiduzzaman et al., 2025). |
| **Optimizer** | [SGD, AdamW] | **AdamW** | AdamW incorporates weight decay directly into step updates, stabilizing segmentation mask training (Midigudla et al., 2025). |
| **Base Learning Rate** | [10-2, 10-3, 5x 10-4] | **10-3** | Minimizes risk of gradient explosion during the initial unfreezing phases (Ajayi et al., 2024). |
| **Weight Decay (lambda)** | [5x 10-4, 10-4] | **5x 10-4** | Penalizes large weights to prevent overfitting to background textures (Nayfeh et al., 2025). |
| **Warm-up Epochs** | [3, 5] | **3** | Prevents early gradient divergence by gradually scaling learning rate from 10-6 to 10-3 (Ajayi et al., 2024). |

### 3.4.3 Defensive ML Checkpoints and Two-Phase Training
To ensure the YOLOv8m-seg model adapts to the specific visual features of waste objects without degrading pre-trained representations, a two-phase training protocol is implemented:
1. **Phase 1: Head Adaptation (Epochs 1–20):** The pre-trained CSP-Darknet53 backbone weights are frozen. Only the detection and segmentation heads are trained to adapt the linear projection layers to the 9-class taxonomy. This preserves the low-level edge and texture extractors learned from the COCO dataset and prevents catastrophic forgetting (Plested et al., 2021).
2. **Phase 2: Joint Fine-Tuning (Epochs 21–100):** The entire network is unfrozen. The model is trained using a Cosine Annealing learning rate scheduler with warm restarts (SGDR), dynamically scaling the learning rate between a maximum of 1e-3 and a minimum of 1e-6 following a cosine curve based on the current epoch and the restart period. Specifically, the learning rate at any given epoch is calculated as the minimum learning rate plus half of the difference between the maximum and minimum learning rates, multiplied by the quantity of one plus the cosine of the ratio of current epochs since the last restart to the total period length of the restart cycle, multiplied by pi.
3. **Overfit One Batch Check:** Before executing full-scale training, the model is trained on a single batch of 10 images for 50 epochs. If the training loss does not approach 0.0 (indicating perfect memorization of a tiny sample), it flags structural pipeline bugs, such as incorrect label scaling, mask misalignment, or optimizer bugs.
4. **Visual Dataloader Check:** Dataloader batch visualizations are compiled and reviewed to verify that the bounding polygons align exactly with the augmented and transformed images.
5. **Gradient Clipping:** To prevent gradient explosions caused by high loss spikes on deformed objects, the gradient norm is clipped at a threshold of 10.0. The clipped gradient is computed by multiplying the gradient vector by the minimum of either one or the ratio of ten divided by the Euclidean norm of the gradient vector.

---

## 3.5 Model Evaluation and Validation

### 3.5.1 Model Evaluation Metrics
Model accuracy, boundary precision, and class-specific detection performance are evaluated using the following core metrics described verbally:
1. **Precision:** Measures the accuracy of positive predictions for a given class, calculated by dividing true positive detections by the sum of true positives and false positives.
2. **Recall:** Measures the completeness of positive detections for a given class, calculated by dividing true positive detections by the sum of true positives and false negatives.
3. **F1-Score:** Balances precision and recall for a given class by calculating twice the product of precision and recall divided by their sum.
4. **Intersection over Union (IoU):** Quantifies the spatial overlap between the predicted segmentation mask and the ground truth mask, calculated by dividing their area of overlap by their area of union.
5. **Dice Similarity Coefficient (DSC):** Measures spatial similarity by dividing twice the area of overlap by the sum of the predicted and ground truth mask areas.
6. **Mean Average Precision (mAP@0.5):** Calculated as the arithmetic mean of the average precision values computed across all nine classes at an Intersection over Union threshold of 0.5, where the average precision for each class is the area under its precision-recall curve.

### 3.5.2 Asymmetric Loss Weighting (Battery Safety Gate)
Standard classification networks utilize symmetric loss optimization, treating false positives and false negatives equally. In the context of PurityLoop AI, failing to detect a battery contaminant (false negative) can trigger a compaction fire, representing a catastrophic system failure. Conversely, misclassifying paper as organic waste (false positive) merely causes minor sorting inefficiency. To satisfy the Asymmetric Error Principle for the safety-critical Battery class, we implement a modified Asymmetric Focal Loss combined with Weighted Cross Entropy. The classification loss is calculated as the negative sum over all samples of a weighted, focused cross-entropy. For each sample, if it belongs to the target class, the loss is the product of the class-specific loss weight, the focusing factor (which is one minus the predicted probability raised to the power of the focusing parameter gamma), and the natural logarithm of the predicted probability. If the sample does not belong to the target class, the loss is the product of the predicted probability raised to the power of gamma and the natural logarithm of one minus the predicted probability. The focusing parameter gamma is set to two point zero, which dynamically down-weights the loss contribution of easy-to-classify examples (where the predicted probability approaches one), forcing the optimizer to focus its gradient updates on hard, ambiguous examples. The class-specific loss weight is set to three point zero for the Battery class and one point zero for other classes. This asymmetric scaling triples the gradient penalty for false negatives on the Battery class, forcing the model to bias its decision boundaries toward higher sensitivity (recall) for batteries.

### 3.5.3 Ground Truth Validation and Carbon Offset Estimation
To validate model performance in real-world environments, we conduct three validation audits:
1. **Validation Subset Audit:** A random validation subset of 100 images per class is manually audited. The model's segmentation outputs are compared against the manual polygon coordinates.
2. **Domain Generalisation Validation:** The model is tested on the held-out RealWaste dataset (4,752 images), which contains low-contrast, soiled waste items from real landfills.
3. **Calibrated Area-to-Pixel Conversion:** The model's predicted area (in pixels) is calibrated against physical area measurements using a scaling factor K, which represents the ratio of the physical surface area in square centimeters to the predicted pixel area, derived using the Polycam 3D scanner.
4. **Carbon Offset Estimation:** Using the calibrated area, the system estimates the mass of sorted recyclable materials and calculates material yields based on the US EPA WARM (Waste Reduction Model) database. The mass of sorted material for a specific class is calculated as the product of the pixel area of its segmentation mask, the scaling factor, the average thickness of the material class, and the density of the material class. The total waste sorting savings in carbon dioxide equivalents is calculated as the sum over all classes of the mass of sorted material multiplied by the difference between the emission factor for landfill disposal and the emission factor for recycling of that material class. For example, the waste sorting emission factors (metric tons of carbon dioxide equivalent per tonne of material) defined by the EPA database are:
     * Cardboard: Landfill factor of zero point five eight, recycling factor of negative three point ten
     * Glass: Landfill factor of zero point zero four, recycling factor of negative zero point two eight
     * Plastic (PET): Landfill factor of zero point zero four, recycling factor of negative one point thirteen
     * Metal (Aluminum): Landfill factor of zero point zero four, recycling factor of negative nine point thirteen
     * Food Waste: Landfill factor of zero point five three, composting factor of negative zero point one five

## 3.6 Web Application Development: Streamlit Interface

To bridge the gap between backend model development and operational deployment on the material recovery facility sorting lines, a web-based dashboard is developed using the Streamlit framework. This interface is specifically designed to support the roles and responsibilities of the Model Debugging and Quality Assurance Lead by serving as a localized diagnostic portal, testing platform, and MLOps telemetry dashboard. By providing real-time visibility into model inferences, database entries, and edge statistics, the interface allows quality assurance engineers and facility operators to audit the backend pipeline, tune edge detection parameters dynamically, and manage safety-critical exceptions.

### 3.6.1 Interface Architecture and Integration

The Streamlit interface is architected to run locally at the edge, communicating directly with the industrial camera systems and the backend model database. To ensure that the edge device operates efficiently without performance degradation, the YOLOv8m-seg model weights (represented by the best-performing model file) are loaded into system memory using Streamlit’s resource caching mechanism (@st.cache_resource) (Terven et al., 2023; Midigudla et al., 2025). This caching decorator prevents the interface from repeatedly reloading the model file upon every user interaction or page rerun, which would otherwise introduce substantial processing latency and risk memory leaks.

For telemetry logging and database audits, the interface is integrated with the SQLite backend database, named purityloop_telemetry.db, using the SQLAlchemy Object-Relational Mapping library. As the conveyor belt camera processes waste items, the backend pipeline logs critical inference metadata—including timestamps, predicted classes, confidence scores, bounding boxes, pixel areas, and processing latencies—directly to this SQLite database. The Streamlit dashboard queries this telemetry database asynchronously, enabling real-time visualization of sorting metrics and automated alerts without blocking the active model inference thread. This decoupled architecture maintains high sorting throughput while providing continuous data synchronization.

### 3.6.2 Quality Assurance and Diagnostic Widgets

The core quality assurance component of the interface is the Operator Inference and Visual Testing Portal. This portal contains an interactive testing widget where quality control operators can upload waste stream images, execute the cached YOLOv8m-seg model, and inspect the resulting instance segmentation outputs. The interface utilizes the OpenCV library to render class-colored polygon masks directly over the waste items, providing operators with immediate visual feedback on segmentation precision. To facilitate edge tuning and diagnostic debugging, the portal includes interactive sliders for confidence and Non-Maximum Suppression Intersection over Union thresholds. By adjusting these sliders, quality assurance engineers can observe how threshold changes alter mask generation and class confidence in real time, helping to optimize model sensitivity and specificity for localized waste variations.

To manage safety-critical anomalies and dataset label noise, the interface implements the Amber Review Queue. When the backend model detects an item with a confidence score below the operational threshold, or when a safety-critical hazard (such as a lithium-ion battery) is identified with moderate confidence, the system flags the item and routes the corresponding frame to the review queue, mitigating the risk of compaction fires (Terazono et al., 2024). Operators can view the flagged frame, inspect the model's predicted mask, and input manual overrides to reclassify the item or trigger physical deflection. Additionally, the portal displays data-centric label auditing metrics powered by Cleanlab, showing facility managers which training samples contain potential label errors and prompting them to correct annotations, which supports continuous active learning loops.

### 3.6.3 MLOps Performance and Drift Telemetry Dashboard

The MLOps performance and telemetry dashboard monitors the real-time operational health of the waste-sorting system. The dashboard features a live line chart that displays the processing latency of each frame against the target operational threshold of forty milliseconds. If latency consistently exceeds this threshold—suggesting hardware bottlenecks or high conveyor loads—the dashboard triggers visual warning indicators to prompt operator inspection. Furthermore, the dashboard summarizes overall sorting performance by plotting rolling metrics of precision, recall, and mean Average Precision, allowing engineers to track model degradation over time.

To ensure environmental accountability, the dashboard calculates and visualizes cumulative yield improvements. By querying the pixel-to-area scaling factor and applying the density formulas defined in the methodology, the system estimates the mass of sorted cardboard, glass, plastic, metal, and compostable organic waste, mapping these figures to waste sorting emission savings to automate sustainability auditing (Mustafa et al., 2025). Finally, to detect changes in waste stream composition that could lead to model degradation, the dashboard implements a data drift detector. The detector calculates the Kullback-Leibler divergence between the baseline training class distribution and the real-time inference class distribution stored in the database. When the Kullback-Leibler divergence exceeds a threshold of zero point two five, the dashboard triggers a data drift alert, warning quality assurance leads that the incoming waste stream has significantly changed and that the model requires retraining. By embedding the telemetry dashboard within a structured MLOps monitoring loop, the system ensures that model updates and drift detections are traceable to quality control objectives, aligning with the feedback loops of Lean Six Sigma DMAIC methodologies (Pongboonchai-Empl et al., 2023).

---

# 4.0 Study Implications

## 4.1 Organizational Efficiency
The deployment of the PurityLoop AI machine learning backend onto MRF sorting lines introduces several transformative improvements in organizational efficiency, processing throughput, and quality control. In standard recycling facilities, incoming co-mingled waste streams are processed on manual sorting lines where operators must visually identify and physically extract contaminants. This manual process is slow, inconsistent, and highly error-prone, resulting in sorting errors of 30% to 40%. The YOLOv8m-seg instance segmentation model integrates directly with high-speed, conveyor-mounted camera setups, delivering real-time inferences with latency under 40 milliseconds per frame (equivalent to >= 25 FPS). This rapid processing speed matches the standard conveyor belt speed of 1.5 m/s, allowing the system to scan and classify every item without requiring conveyor slowing or shutdowns. By automating the identification of recyclable plastics, paper, glass, and metals, the system can drive sorting errors down to under 10%. This enables recycling facilities to increase their sorting throughput while maintaining high purity rates in the output streams.

Furthermore, automating pre-sorting directly improves the economics of waste recovery operations. Recyclable materials, such as high-density polyethylene (HDPE) or polyethylene terephthalate (PET), command higher prices in circular economy markets when contamination levels are low. By reducing cross-contamination (e.g., preventing food residues or compostable materials from entering the plastic baling streams), the facility increases the value of its output. The system also reduces mechanical downtime. When large non-recyclables or hazardous items enter shredders or compactors, they can jam the equipment, causing hours of operational downtime. By detecting and deflecting these contaminants upstream, PurityLoop AI maintains continuous facility uptime. This automation reduces operational costs, allowing MRFs to reallocate manual labor from repetitive sorting tasks to higher-value operational roles, such as facility maintenance, quality audits, and data analysis.

Additionally, the automated tracking of sorted waste streams creates a digital audit trail of material volumes and classifications. Historically, estimating material yields and sustainability metrics was manual and prone to estimation errors. By converting predicted instance segmentation pixel areas into physical area (cm²) and mass estimations using the calibrated scaling factor K, PurityLoop AI provides real-time, auditable statistics on waste sorting (GHG) emissions avoided. These statistics are mapped directly to the EPA WARM database, allowing MRFs to generate verified material yield reports for corporate clients. This automated reporting capability positions recycling facilities to participate in compliance carbon markets, generating new revenue streams through material recovery value while demonstrating compliance with national recycling mandates (Act 672).

## 4.2 Employee Health and Well-being
The implementation of the PurityLoop AI system directly operationalizes the Social ("S") pillar of corporate ESG frameworks by mitigating the severe occupational health, safety, and psychological hazards that characterize manual sorting environments. Manual sorting operators spend long shifts standing along fast-moving conveyors, performing repetitive reaching, operational auditpping, and twisting movements. This causes chronic musculoskeletal disorders (MSDs), repetitive strain injuries (RSIs), and carpal tunnel syndrome. By automating the detection and deflection of the majority of waste categories, the physical workload on manual operators is significantly reduced. Operators transition from continuous physical sorting to system monitoring and anomaly verification. This transition reduces physical fatigue, cuts down on repetitive motion injuries, and helps mitigate worker burnout.

Beyond ergonomic benefits, the system reduces operator exposure to biological and physical hazards. Solid waste streams contain decomposing organic matter, food residues, and yard waste that release bioaerosols, fungal spores, and bacteria. Inhaling these airborne pathogens causes chronic respiratory illnesses, occupational asthma, and gastrointestinal infections. By automating the sorting of the Food/Organic class, PurityLoop AI minimizes the time workers must spend handling decomposing organic materials, reducing exposure to bioaerosols. Additionally, municipal waste streams frequently contain physical hazards, such as broken glass, sharp metals, and medical needles. When operators attempt to sort these items manually, they risk punctures and cuts that can lead to bacterial infections or the transmission of bloodborne pathogens (e.g., Hepatitis B, Hepatitis C, HIV). Automating sorting via pneumatic air jets or robotic arms keeps operators away from direct contact with sharp objects.

Most importantly, the implementation of the asymmetric Battery Recall Gate (Recall >= 0.90) addresses the life-threatening hazard of lithium-ion battery fires. When consumer batteries pass undetected into mechanical compactors, the high pressure punctures the cell casing, causing internal short circuits, thermal runaway, and explosive ignition. These compaction fires release highly toxic gases (such as hydrogen fluoride and carbon monoxide) and can spread rapidly through dry paper and cardboard, threatening the lives of everyone in the facility. By establishing a recall target of 0.93 for the Battery class and routing low-confidence detections to an amber review queue, PurityLoop AI prevents batteries from entering the compaction phase. This eliminates compaction explosions, protects workers from toxic gas inhalation and fire injuries, and creates a safer workplace, aligning with UN Sustainable Development Goals (SDG) 3 (Good Health and Well-being) and 8 (Decent Work and Economic Growth).

---

# 5.0 Conclusion

The machine learning backend of PurityLoop AI demonstrates the feasibility of real-time automated waste sorting. By leveraging YOLOv8m-seg, implementing diagnostic quality gates, and applying asymmetric loss weighting for battery detection, the system provides a robust solution. The use of open-source frameworks (PyTorch, Cleanlab, Roboflow) and standard hardware configurations ensures low deployment overhead.

While the PurityLoop system presents substantial improvements to the sorting process, it has several limitations:
1. **Generalisation Limitations:** The model's generalization capabilities depend on the quality and diversity of the training data. Although data augmentation and Cleanlab auditing mitigate label noise, the model may struggle with out-of-distribution packaging shapes, highly crumpled items, or localized waste variations not represented in the fused dataset.
2. **Volume and Mass Accuracy:** Mass estimations derived from 2D instance segmentation mask areas assume uniform thickness and density. This geometric approximation introduces a 15% to 20% margin of error compared to physical weight sensors, which can impact the precision of material yield recovery calculations.
3. **Occlusion Constraints:** Highly overlapped or nested items (e.g., a plastic bottle hidden inside a cardboard box) cannot be segmented by a standard 2D camera system, leading to missed detections or classification errors on hidden layers.

### Future Work
1. **Advanced Depth and Mass Estimation:** Future iterations can integrate stereo vision cameras, LiDAR sensors, or conveyor-mounted load cells. Capturing 3D depth information will allow the system to construct volumetric representations of waste items, improving mass estimation accuracy and reducing the margin of error in material yield recovery calculations.
2. **Edge TPU and Green AI Optimization:** To support cost-effective edge deployment, future work will focus on optimizing the YOLOv8m-seg architecture using TensorRT quantization and model distillation. Compiling the model to FP8 or INT8 precision for deployment on edge processors (such as NVIDIA Jetson or Google Coral Edge TPU) will reduce memory consumption, lower inference latency, and minimize the energy footprint of the sorting equipment.
3. **Active Learning Loops:** Enforcing continuous dataset expansion using automatic collection of low-confidence predictions from production lines.
4. **Multi-Spectral Imaging:** Incorporating multi-spectral or hyperspectral cameras would allow the system to classify materials based on chemical absorption spectra. This would enable the distinction of chemically similar polymers (e.g., distinguishing food-grade PET from non-food-grade PET) and improve classification accuracy.

---

# Reference

Abo-Zahhad, M. M., & Abo-Zahhad, M. (2025). Real time intelligent garbage monitoring and efficient collection using Yolov8 and Yolov5 deep learning models for environmental sustainability. *Scientific Reports*, *15*(1), 16024. https://doi.org/10.1038/s41598-025-99885-x

Ajayi, O. G., Ibrahim, P. O., & Adegboyega, O. S. (2024). Effect of hyperparameter tuning on the performance of YOLOV8 for multi crop classification on UAV images. *Applied Sciences*, *14*(13), 5708. https://doi.org/10.3390/app14135708

Arishi, A. (2025). Real-Time Household Waste Detection and Classification for Sustainable Recycling: A Deep Learning Approach. *Sustainability*, *17*(5), 1902–1902. https://doi.org/10.3390/su17051902

EPA (Environmental Protection Agency). (2024). *Greenhouse Gas Equivalencies Calculator: Calculations and References*. Retrieved from https://www.epa.gov/energy/greenhouse-gas-equivalencies-calculator-calculations-and-references

EPA (Environmental Protection Agency). (2026). *Basic Information about the Waste Reduction Model (WARM)*. Retrieved from https://www.epa.gov/waste-reduction-model/basic-information-about-waste-reduction-model

Faizul Rakib Sayem, Bin, S., Mansura Naznine, Nashbat, M., Mazhar Hasan-Zia, Ansaruddin, A. K., Amith Khandakar, Ashraf, A., Majid, M. E., Saad, & Muhammad. (2024). Enhancing waste sorting and recycling efficiency: robust deep learning-based approach for classification and detection. *Neural Computing and Applications*. https://doi.org/10.1007/s00521-024-10855-2

Midigudla, R. S., Dichpally, T., Vallabhaneni, U., Wutla, Y., Sundaram, D. M., & Jayachandran, S. (2025). A comparative analysis of deep learning models for waste segregation: YOLOv8, EfficientDet, and Detectron 2. *Multimedia Tools and Applications*. https://doi.org/10.1007/s11042-025-20647-y

Mustafa, F., Smolarski, J., & Elamer, A. A. (2025). The convergence of artificial intelligence and sustainability reporting: A systematic review of applications, challenges and future directions. *Business Strategy and the Environment*, *34*(8), 9761–9784. https://doi.org/10.1002/bse.70090

Nahiduzzaman, M., Ahamed, M. F., Naznine, M., Karim, M. J., Rahman, M. S., Alam, M. S., Haque, M. A., & Islam, M. S. (2025). An automated waste classification system using deep learning techniques: Toward efficient waste recycling and environmental sustainability. *Knowledge-Based Systems*, *310*, Article 113028. https://doi.org/10.1016/j.knosys.2025.113028

Nayfeh, A., Al-Azani, S., & Samma, H. (2025). A Two-Stage YOLOV8 approach for waste detection and classification in cognitive cities. *Transportation Research Procedia*, *84*, 579–586. https://doi.org/10.1016/j.trpro.2025.03.111

Phan, T. H., & Yamamoto, K. (2020). Resolving Class Imbalance in Object Detection with Weighted Cross Entropy Losses. *arXiv preprint arXiv:2006.01413*. https://doi.org/10.48550/arXiv.2006.01413

Plested, J., Shen, X., & Gedeon, T. (2021). Non-binary deep transfer learning for image classification. *arXiv preprint arXiv:2107.08585*. https://doi.org/10.48550/arXiv.2107.08585

Pongboonchai-Empl, T., Antony, J., Garza-Reyes, J. A., Komkowski, T., & Tortorella, G. L. (2023). Integration of Industry 4.0 technologies into Lean Six Sigma DMAIC: a systematic review. *Production Planning & Control*, *35*(12), 1–26. https://doi.org/10.1080/09537287.2023.2188496

Ren, Y., Li, Y., & Gao, X. (2024). An MRS-YOLO Model for High-Precision Waste Detection and Classification. *Sensors*, *24*(13), Article 4339. https://doi.org/10.3390/s24134339

SWCorp Malaysia. (2024). *National solid waste management statistics report 2024*. Solid Waste and Public Cleansing Management Corporation. https://www.swcorp.gov.my

Terazono, A., Oguchi, M., Akiyama, H., Tomozawa, H., Hagiwara, T., & Nakayama, J. (2024). Ignition and fire-related incidents caused by lithium-ion batteries in waste treatment facilities in Japan and countermeasures. *Resources, Conservation and Recycling*, *202*, 107398. https://doi.org/10.1016/j.resconrec.2023.107398

Terven, J., Córdova-Esparza, D.-M., & Romero-González, J.-A. (2023). A Comprehensive Review of YOLO Architectures in Computer Vision: From YOLOv1 to YOLOv8 and YOLO-NAS. *Machine Learning and Knowledge Extraction*, *5*(4), 1680–1716. https://doi.org/10.3390/make5040083

Venturi, S., Zulauf, K., Cuel, R., & Wagner, R. (2024). Trash to treasure: Gamification and informed recycling behavior. *Resources, Conservation and Recycling*, *215*, Article 108108. https://doi.org/10.1016/j.resconrec.2024.108108

Wang, T., Li, K., Liu, D., Yang, Y., & Wu, D. (2022). Estimating the Carbon Emission of Construction Waste Recycling Using Grey Model and Material Yield Assessment: A Case Study of Shanghai. *International Journal of Environmental Research and Public Health*, *19*(14), 8507. https://doi.org/10.3390/ijerph19148507

Yaseen, M. (2024). What is YOLOv8: An In-Depth Exploration of the Internal Features of the Next-Generation Object Detector. *arXiv preprint arXiv:2408.15857*. https://doi.org/10.48550/arXiv.2408.15857

Zhalgas, A., Amirgaliyev, B., Boltay, B., Shegenova, D., Zhylkybay, N., & Yedilkhan, D. (2026). Development of an Intelligent Waste Segregation System Using a Self-Collected Dataset and Deep Learning Methods. *Journal of Robotics and Control (JRC)*, *7*(1), 3393–3404. https://doi.org/10.18196/jrc.v7i1.27247
