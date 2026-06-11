# 2. Literature Review

## 2.1 Literature Search Protocol

This review was conducted in accordance with systematic search principles to ensure transparency and reproducibility. The primary databases searched were Scopus, Web of Science, and Google Scholar. Inclusion criteria were: (1) peer-reviewed journal articles or conference papers; (2) publication between 2021 and 2026; (3) subject matter directly relevant to one of five defined thematic areas; and (4) Scopus indexing at Q1 or Q2 level where applicable. Exclusion criteria were: (1) publications before 2021; (2) studies lacking empirical or quantitative evaluation; (3) grey literature without peer review. Boolean search strings combined primary terms (e.g., "waste detection," "computer vision," "YOLOv8") with secondary terms (e.g., "recycling," "contamination," "ESG," "gamification," "DMAIC"). A total of 47 papers were retrieved and reviewed; 18 are directly cited in this proposal.

---

## 2.2 Theme 1: Deep Learning for Automated Waste Classification and Contamination Detection

### 2.2.1 Evolution of Object Detection Architectures in Waste Management

The application of deep learning to waste classification has progressed through three generations of architectural approach. Early work employed image-level classification models (AlexNet, VGG, ResNet) to assign waste images to broad categories, achieving high accuracy on curated benchmark datasets but producing no spatial localisation information—a critical limitation for deployment on physical sorting lines where position and extent of a contaminant must be known to trigger isolation (Nahiduzzaman et al., 2025).

The second generation introduced bounding-box object detection frameworks, most notably the YOLO family and Single Shot Detectors (SSDs), which provided fast, spatially-resolved predictions suitable for real-time deployment. These models demonstrated strong performance for recyclable waste categories but were limited to rectangular bounding boxes, which are inadequate for capturing the irregular, heterogeneous morphology of contaminating materials such as shredded food waste overlapping recyclable items (Islam & Chowdhury, 2024). Furthermore, early YOLO variants used anchor-based prediction schemes that required manual tuning for domain-specific object scales.

The third and current generation is represented by anchor-free, single-stage segmentation models, of which YOLOv8-seg (Jocher et al., 2023) is the most widely adopted in industrial applications. YOLOv8-seg combines bounding box detection with instance segmentation mask prediction in a single inference pass, using an anchor-free head that adapts to objects of arbitrary scale and irregular shape. This architectural property is directly relevant to contamination detection, where contaminants may partially occlude recyclables and require pixel-level boundary delineation to calculate material purity accurately.

### 2.2.2 YOLOv8 Performance in Waste Detection Tasks

Multiple recent studies confirm the superiority of YOLOv8 over predecessor architectures for waste detection tasks. Ahmad et al. (2025) trained a ResNet-based classification model on a 12-class urban waste dataset and reported 98.16% accuracy, while noting that classification-only models cannot support contamination localisation on sorting lines. Arishi (2025) deployed YOLOv8 for real-time household waste detection and demonstrated competitive precision and recall metrics across organic, recyclable, and non-recyclable categories. Islam and Chowdhury (2024) proposed a robust deep learning approach for simultaneous waste classification and detection using CNN ensembles and reported significant accuracy gains over single-model baselines, emphasising the value of multi-model diversity for class imbalance mitigation.

Nahiduzzaman et al. (2025) introduced a three-stage hierarchical classification system achieving 96% accuracy at the two-class level and 85.25% at 36-class granularity. This paper is particularly relevant to PurityLoop AI as it demonstrates that lightweight architectures (1.09M parameters) can perform competitive multi-class waste classification when combined with structured preprocessing and ensemble classification heads—a data-centric insight consistent with the present study's emphasis on pipeline-level optimisation.

### 2.2.3 Model Selection Justification: YOLOv8m-seg

The selection of YOLOv8m-seg over lighter (YOLOv8n-seg) and heavier (YOLOv8l-seg, YOLOv8x-seg) variants is justified on three grounds. First, the medium variant provides a superior accuracy-efficiency trade-off for multi-class detection tasks involving small objects (e.g., battery cells obscured by paper waste) compared to the nano variant, which demonstrated lower recall on small contaminant objects in preliminary ablation studies. Second, YOLOv8m-seg's segmentation head enables pixel-level purity rate calculation, which is required by the operational reporting module. Third, inference latency benchmarks for YOLOv8m on standard GPU hardware remain within the 500ms per frame target required for real-time dashboard updates. EfficientDet and ResNet-based alternatives were evaluated and excluded due to the absence of native single-stage segmentation capability and slower inference on equivalent hardware (Islam & Chowdhury, 2024).

---

## 2.3 Theme 2: Dataset Landscape and Multi-Dataset Fusion Strategies

### 2.3.1 Benchmark Datasets for Waste Detection

The academic literature on waste detection has coalesced around several benchmark datasets. TrashNet (Thung & Yang, 2016, as cited in Nahiduzzaman et al., 2025) provides 2,527 images across six broad categories and serves as a widely-used clean baseline, though its studio-captured images do not reflect real-world sorting line conditions. The Trash Annotations in Context (TACO) dataset (Proença & Simões, 2020, as cited in Islam & Chowdhury, 2024) offers approximately 1,500 annotated images across 60 fine-grained waste categories in real-world litter environments, with annotations in COCO format, making it directly compatible with YOLOv8 training pipelines. TACO's real-world environmental diversity is its primary strength; its relatively small size and class imbalance are acknowledged limitations.

### 2.3.2 Critical Gap: Hazardous Waste Class Coverage

A critical gap exists across all established benchmark datasets: the near-universal absence of hazardous waste categories, specifically lithium-ion batteries and electronic waste components. This gap is directly consequential for PurityLoop AI, which identifies battery detection as a primary contamination alert trigger due to the fire risk and chemical hazard posed by batteries in standard recyclable bales. The Garbage Classification v2 dataset (Sumn2u, as cited in Dataset.txt internal reference, 2024) addresses this gap by including Battery as an explicit class across 19,762 images, making it the only publicly available large-scale dataset with confirmed hazardous class coverage.

### 2.3.3 Multi-Dataset Fusion Rationale

No single public dataset simultaneously provides: (a) battery/hazardous class coverage, (b) real-world visual diversity, (c) YOLO-compatible annotation format, and (d) sufficient volume for training a medium-scale segmentation model to convergence. This motivates the multi-dataset fusion approach adopted in this study. The fusion corpus draws from four primary sources—TrashNet, TACO, Garbage Classification v2, and Trash Detection (Roboflow, 64-class pre-annotated)—yielding a combined training corpus of over 70,000 images post-augmentation. This approach is consistent with best practice in medical imaging data-centric learning (Ahmad et al., 2025) and directly addresses the dataset limitations identified in the literature.

---

## 2.4 Theme 3: Operational Reporting and AI-Driven Carbon Accountability

### 2.4.1 AI Integration with Sustainability Reporting

Environmental, Social, and Governance (ESG) reporting has rapidly transitioned from voluntary narrative disclosure to a quantitative, regulatory-driven accountability requirement. Mustafa et al. (2025) conducted a systematic review of 304 Scopus-indexed documents examining AI's role in sustainability reporting and found that 76% of all publications in this area emerged between 2023 and 2025, signalling an accelerating convergence of AI capability and ESG measurement demand. The authors identify real-time monitoring, predictive analytics, and automated data inteoperational auditty as the three primary value vectors of AI in ESG contexts—all three of which are directly instantiated in PurityLoop AI's architecture.

AI significantly enhances ESG performance by alleviating financing constraints, promoting green innovation, and strengthening information disclosure, with effects particularly pronounced in the Environmental dimension (Mustafa et al., 2025). This finding directly motivates the inclusion of a real-time material yield dashboard in PurityLoop AI as a tangible, machine-verifiable Environmental pillar output.

### 2.4.2 Carbon Offset Calculation Methodology

The material yield quantification module in PurityLoop AI employs a Material Yield Assessment (Yield)-derived formula:

> **Net Weight Saved = Σ (Weight_material × (Emissions_virgin − Emissions_recycled)) × Purity_Factor**

Where emission coefficients (kg Weight per kg material) are sourced from the UK Government Greenhouse Gas Conversion Factors (BEIS/DESNZ, 2023)—a peer-reviewed, annually updated government publication widely used as the authoritative reference for material-specific recovered weight calculations. The Purity Factor (ranging 0.0 to 1.0) scales the theoretical offset by the actual purity rate detected by the CV system, ensuring that only verified, uncontaminated material yield contributes to the reported yield improvements figure. This methodology ensures the carbon figure is not merely an estimate but is computationally tied to the CV system's actual detection output.

---

## 2.5 Theme 4: Gamification for Behavioural Change in Recycling

### 2.5.1 Gamification as a Recycling Intervention

The source-level contamination problem—where end-users introduce non-recyclable materials into recycling streams before facility-level sorting occurs—cannot be fully addressed by industrial automation alone. Behavioural intervention at the household or user level is required to complement facility-level detection. Gamification—the application of game design elements (points, badges, leaderboards, challenges, rewards) to non-game contexts—has demonstrated evidence-based effectiveness in promoting pro-environmental behaviour.

Venturi et al. (2024) conducted a mixed-methods study involving 26 interviews and an 18-participant app usage experiment, evaluating gamified versus non-gamified recycling apps. The study found that gamified applications significantly enhanced users' comprehension of correct waste separation practices and increased declared intention to maintain correct sorting behaviour. Critically, the study identified that the combination of information provision and reward mechanisms—rather than either element in isolation—drove the most durable behavioural engagement. This finding directly informs PurityLoop AI's Recycling Coach design, which combines real-time educational feedback (contamination reason notification) with a reward mechanism (Eco-Credit points for high purity sessions).

### 2.5.2 Eco-Credit Incentive Architecture

The Eco-Credit system in PurityLoop AI implements a token economy aligned with principles from cognitive evaluation theory. Users earn credits for high-purity disposal sessions; credits are redeemable for rewards or neighbourhood status visibility on a leaderboard. This architecture mirrors the gamification elements identified by Venturi et al. (2024) as most effective: positive reinforcement, peer comparison, and tangible value exchange. The system is designed to create a closed feedback loop between the industrial sorting system and the end-user behavioural layer—a novel integration not identified in any reviewed prior work.

---

## 2.6 Theme 5: DMAIC and Industry 4.0 Integration for Machine Learning Quality

### 2.6.1 DMAIC as a Framework for ML Quality Governance

The DMAIC (Define-Measure-Analyse-Improve-Control) framework, originating in Six Sigma quality engineering, provides a structured, evidence-based methodology for process improvement that is directly applicable to machine learning model development. Pongboonchai-Empl et al. (2023) conducted a systematic review of 692 papers examining the integration of Industry 4.0 technologies into Lean Six Sigma DMAIC and found that the Analyse phase is the most extensively supported DMAIC phase through machine learning, big data analytics, and IoT techniques. The authors propose a DMAIC 4.0 framework that explicitly maps data mining and ML model training to the Improve phase and automated monitoring to the Control phase—a structure directly adopted in PurityLoop AI's methodology.

The relevance of DMAIC to this study extends beyond process framework selection. Dr. Narishah Mohamed Salleh's published research (Narishah et al., 2019a, 2019b) demonstrates the application of hybrid DMAIC methodologies to software engineering requirement elicitation, establishing a conceptual precedent for applying quality engineering frameworks to technology system development at the requirements and design level. The present study applies this precedent to the domain of machine learning pipeline quality governance.

### 2.6.2 Multi-Stage Quality Gate Protocol for MLOps

In the context of deep learning development, relying solely on final validation metrics often masks underlying pipeline errors. To operationalize the DMAIC *Analyse* and *Control* phases at the code level, this project integrates a multi-stage Quality Gate and Algorithmic Audit protocol. Rather than proceeding directly to master training on unverified data, the process mandates individual diagnostic training runs on independent dataset slices to surface label noise, followed by an algorithmic label-error audit using Cleanlab. By nesting these structured quality checkpoints within the broader DMAIC quality framework, PurityLoop AI establishes a verified mathematical and spatial foundation. This ensures that when the project proceeds to the two-phase training protocol, Phase 1 (Head Adaptation) begins with a structurally sound data-loading and backpropagation architecture, and subsequent joint fine-tuning in Phase 2 is built on genuine, clean feature representation rather than dataset leakage or corrupted annotations.


---

## 2.7 Critical Synthesis and Research Gap

The five literature themes reviewed above converge on a unified research gap. The literature on deep learning for waste detection has produced increasingly capable single-model architectures but has not demonstrated integrated, end-to-end deployment pipelines that connect CV inference to business intelligence outputs. The operational reporting literature has documented AI's value for sustainability disclosure but lacks industrial demonstrations of real-time, CV-fed carbon audit systems. The gamification literature has validated behavioural intervention app designs but has not linked these applications to facility-level sorting data. The DMAIC literature has mapped Industry 4.0 tools to quality framework phases but lacks case implementations in the recycling domain.

**PurityLoop AI addresses this convergent gap** by proposing and implementing an integrated system in which all five themes are operationalised simultaneously: YOLOv8m-seg detection (Theme 1) trained on fused multi-dataset corpus (Theme 2) feeding a real-time ESG carbon dashboard (Theme 3) linked to a gamified user app (Theme 4) governed by DMAIC quality engineering (Theme 5). This integration constitutes the primary originality claim of the study.

---

## 2.8 Requirement Elicitation Approach

Following the hybrid requirement elicitation methodology advocated by Narishah et al. (2019b), system requirements for PurityLoop AI were elicited through three complementary channels:

1. **Literature Review Elicitation:** Performance benchmarks, class requirements, and evaluation metrics derived from the reviewed literature (Sections 2.2–2.6).
2. **Stakeholder Analysis:** Functional requirements derived from analysis of recycling facility operator needs (throughput, purity rate, safety alerts) and corporate operational reporting needs (carbon audit, material yield tracking).
3. **Benchmark Analysis:** Non-functional requirements derived from RadioLens (2025) and comparable YOLOv8-seg deployment studies, establishing achievable performance targets.

The resulting functional and non-functional requirements are formally specified in Section 3.4.
