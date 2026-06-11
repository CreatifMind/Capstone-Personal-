# PurityLoop AI — Framework Diagrams
**Version 1.0** | Capstone AY2025/26 | Sunway Business School — Business Analytics

---

## Fig 1 — PurityLoop Conceptual Framework
*Modelled after Narishah et al. (2022) SVRA-ERP framework structure*

```mermaid
flowchart TD
    A["🏭 Problem Context\nManual sorting → 6.96% recyclable loss\nMalaysia 2024 recycling rate: 37.9%\nTarget: 40% by 2025 (12th Malaysia Plan)"] --> B

    B["📋 Literature Gap\nNo integrated system combining:\n① CV contamination detection\n② Real-time process audit trail\n③ Gamified behavioral intervention"] --> C

    C["🔷 PROPOSED FRAMEWORK\nPurityLoop AI"] --> D & E & F

    D["Layer 1: Input\nPython RPA Hot Folder\n• Monitors /watch_folder/\n• Validates: image format, file inteoperational auditty\n• Error handling: non-image → quarantine log\n• Triggers inference on new file"]

    E["Layer 2: Detection\nYOLOv8m-seg Engine\n• 9-class multi-label detection\n• Instance segmentation mask\n• 3-tier confidence system\n  Green ≥ 0.70 | Yellow 0.45–0.69 | Red < 0.45\n• Contamination class → immediate alert"]

    F["Layer 3: Decision Logic\n• Purity Rate = (pure items / total) × 100\n• Net Weight Saved = Σ(Wt × ΔEmissions) × PurityFactor\n• Contamination Event → alert + audio"]

    D --> G
    E --> G
    F --> G

    G["Layer 4: Data\nSQLite Database\n• session_id, timestamp, class, confidence\n• purity_rate, material_yield, weight_saved\n• user_id (phone number hash)"]

    G --> H & I

    H["Layer 5: Analytics\nPower BI / Tableau Dashboard\n• Real-time Purity % gauge\n• Revenue from material yield\n• Weight offset trend\n• Contamination event log"]

    I["Layer 6: User\nStreamlit Recycling Coach\n• Phone number login\n• Personal weight sorted\n• Eco-Credit score\n• Educational feedback"]

    J["📊 Evaluation Plan\n• mAP@0.5 ≥ 0.85\n• mAP@0.5:0.95 ≥ 0.70\n• Detection latency ≤ 500ms\n• Purity rate accuracy ±2%\n• Carbon formula: Yield-peer-reviewed source"]

    H --> J
    I --> J
```

---

## Fig 2 — DMAIC Quality Framework Mapping

```mermaid
flowchart LR
    subgraph D["DEFINE"]
        D1["Problem:\nRecycling contamination\ncauses 6.96% material loss\nin Malaysia annually"]
        D2["Scope:\n9 waste classes\nSimulated conveyor belt\n6-person team\nWW12 showcase target"]
    end

    subgraph M["MEASURE"]
        M1["Baseline:\nManual sorting error rate\n30–40% (literature)"]
        M2["Dataset KPIs:\n• Total images post-clean\n• Class distribution balance\n• Human annotation error rate"]
    end

    subgraph A["ANALYZE"]
        A1["Why YOLOv8m-seg?\n• vs EfficientDet: slower inference\n• vs ResNet: no segmentation mask\n• vs YOLOv8n: higher recall on small items\n• Anchor-free: adapts to irregular waste shape"]
        A2["Why multi-dataset fusion?\n• No single dataset covers Battery class\n  + recyclables + organic contaminants\n• TACO: real-world diversity\n• GC-V2: hazardous class coverage"]
    end

    subgraph I["IMPROVE"]
        I1["PurityLoop System\n(see Fig 1 framework)"]
        I2["10-Phase Training Pipeline\n(see Fig 5)"]
        I3["MLOps Quality Gates\n(see Fig 5)"]
    end

    subgraph C["CONTROL"]
        C1["KPI Dashboard\n• mAP tracked per epoch\n• Purity rate logged per session\n• Weight formula audited vs Yield source"]
        C2["Active Learning Loop\n• Low-confidence predictions → human review\n• Quarterly model retraining\n• Version control via Git tags"]
    end

    D --> M --> A --> I --> C
```

---

## Fig 3 — System Architecture (Technical)

```mermaid
flowchart TD
    subgraph INPUT["INPUT LAYER"]
        CAM["Simulated Camera\n(Hot Folder Drop)"]
        RPA["Python RPA Script\nwatchdog library\nError: quarantine log"]
    end

    subgraph ML["ML INFERENCE LAYER"]
        PRE["Preprocessing\n640×640 resize\nRGB normalize"]
        YOLO["YOLOv8m-seg\nbest.pt weights\nGPU inference"]
        POST["Post-processing\nNMS | Confidence filter\nSegmentation mask decode"]
    end

    subgraph LOGIC["DECISION LAYER"]
        CONT["Contamination Check\nClass ∈ {Battery, FoodWaste, Contaminant}\n→ Alert trigger"]
        PURITY["Purity Calculator\nPurity% = pure_count/total × 100"]
        CARBON["Carbon Calculator\nΣ(Wt × ΔEmission) × PurityFactor\nCoefficients: ecoinvent Yield"]
    end

    subgraph DATA["DATA LAYER"]
        DB["SQLite Database\ndetections | sessions | users"]
    end

    subgraph OUTPUT["OUTPUT LAYER"]
        DASH["Power BI Dashboard\nSupervisor UI\nCommand Center Display"]
        APP["Streamlit App\nUser Portal\nMobile-Responsive"]
        ALERT["Alert System\nRed bounding box\nAudio notification"]
    end

    CAM --> RPA --> PRE --> YOLO --> POST
    POST --> CONT & PURITY & CARBON
    CONT --> ALERT
    PURITY & CARBON --> DB
    DB --> DASH & APP
```

---

## Fig 4 — Integrated Methodology Framework

```mermaid
flowchart TD
    subgraph GOVERNANCE["MACRO GOVERNANCE\n(Iterative Waterfall)"]
        G1["Phase 1: Proposal"] --> G2["Phase 2: Interim"] --> G3["Phase 3: Final Submission"]
    end

    subgraph QUALITY["QUALITY FRAMEWORK\n(Lean Six Sigma / DMAIC)"]
        Q1["Define → Measure → Analyze → Improve → Control\nApplied across BOTH web dev and model dev"]
    end

    subgraph STRATEGY["ANALYTICS STRATEGY\n(BALC + CRISP-DM)"]
        S1["Business Analytics Life Cycle\nBusiness Understanding → Data Understanding\n→ Modelling → Evaluation → Deployment"]
        S2["CRISP-DM Loop\nData prep → Model → Evaluate → Loop if mAP < 0.85"]
    end

    subgraph WEB["WEB DEVELOPMENT\n(Iterative Prototyping)"]
        W1["Sprint 1: Wireframe"] --> W2["Sprint 2: Mock data UI"]
        W2 --> W3["Sprint 3: API integration"]
        W3 --> W4["Sprint 4: Live data + polish"]
    end

    subgraph MODEL["MODEL DEVELOPMENT\n(OSEMN + Quality Gates)"]
        O1["Obtain"] --> O2["Scrub"] --> O3["Explore"]
        O3 --> O4["Model"] --> O5["iNterpret"]
        O5 -->|"mAP < 0.85"| O2
    end

    GOVERNANCE --> QUALITY
    QUALITY --> STRATEGY
    STRATEGY --> WEB & MODEL
```

---

## Fig 5 — Model Development Pipeline (10 Phases)

```mermaid
flowchart TD
    P0["Phase 0: Become One with Data\nManual data inspection\nManual inspect 100 images per class\nFind biases, corrupted labels, annotation errors\nRecord human error rate baseline"]

    P1["Phase 1: Dataset Acquisition\n11 datasets evaluated\n4 primary selected for fusion\nCriteria: battery class coverage + diversity"]

    P2["Phase 2: Data Cleaning\nRemove duplicates, corrupted files\nImage-to-label verification\nAnnotation inteoperational auditty check"]

    P3["Phase 3: Preprocessing\nResize → 640×640\nRGB normalization\nClass rebalancing via weighting"]

    P4["Phase 4: Annotation\nRoboflow Label Assist\n100% manual verification for seed set\nAuto-labelling for scale (10–20% spot check)"]

    P5["Phase 5: Augmentation\nRotation 90°, Horizontal flip\nBrightness ×1.2, Gaussian blur 2.5px\n4× multiplier (FID-validated)"]

    P6["Phase 6: Overfit-One-Batch Test\nData/Code Sanity Check\n2 images, near-zero loss required\nFail → debug coordinates/loading code\nDo NOT proceed to full training if fail"]

    P7["Phase 7: Diagnostic Training\n50 epochs, small batch\nVerify loss @ init: expected -ln(1/9) ≈ 2.20\nMonitor train_batch0.jpg\nInput-independent baseline test"]

    P8["Phase 8: Master Training\nYOLOv8m-seg, 300 epochs\nBatch=16, imgsz=640\nSeed=42 fixed\nEarly stopping on val/seg loss"]

    P9["Phase 9: Evaluation\nmAP@0.5 | mAP@0.5:0.95 | F1\nGeneralization held-out set\nConfusion matrix per class\nLatency benchmark (FPS)"]

    P10["Phase 10: Control\nActive learning: low-confidence → review queue\nVersioned weights via Git tags\nRetrain trigger: mAP drift > 3% from baseline"]

    P0 --> P1 --> P2 --> P3 --> P4 --> P5 --> P6 --> P7 --> P8 --> P9 --> P10
    P9 -->|"mAP@0.5 < 0.85"| P2
```

---

## Fig 6 — Team Structure & Git Protocol

```mermaid
flowchart TD
    MAIN["🔒 main branch\n(Protected — Repository Owner only merges)"]

    subgraph BACKEND_SQUAD["⚙️ Backend Squad"]
        PM["Project Manager / ESG\nBranch: feat/esg-*\nDeliverables: PRD, progress_plan, ESG KPIs"]
        DO["DataOps Developer\nBranch: feat/data-*\nDeliverables: clean dataset, annotation labels"]
        ML["ML R&D (Trainer + Evaluator)\nBranch: feat/model-*\nDeliverables: best.pt, eval report, confusion matrix"]
    end

    subgraph FRONTEND_SQUAD["💻 Frontend Squad"]
        BE["Backend / Integration\nBranch: feat/api-*\nDeliverables: RPA script, SQLite schema, API routes"]
        UI["Full-Stack UI\nBranch: feat/ui-*\nDeliverables: Streamlit app, mobile-responsive portal"]
        BI["BI Analytics\nBranch: feat/bi-*\nDeliverables: Power BI dashboard, purity rate formula, DB schema"]
    end

    PM & DO & ML & BE & UI & BI -->|"git push → PR → human review"| MAIN

    RULE1["Rule 1: Pull before push\ngit pull origin main"]
    RULE2["Rule 2: Never push to main directly"]
    RULE3["Rule 3: Human-only merge review"]
    RULE4["Rule 4: Delete branch after merge"]
```

---

## Fig 7 — Variable Matrix (Formal Specification)

```mermaid
erDiagram
    DETECTION_SESSION {
        string session_id PK
        datetime timestamp
        string user_id FK
        float purity_rate
        float material_yield_kg
        float weight_saved_kg
        int total_items_detected
        int contaminant_count
    }

    DETECTION_EVENT {
        string event_id PK
        string session_id FK
        string object_class
        float confidence_score
        string confidence_tier
        string bbox_coordinates
        string segmentation_mask_path
        string alert_triggered
    }

    USER {
        string user_id PK
        string phone_number_hash
        int eco_credits
        int total_sessions
        float total_weight_saved
    }

    DETECTION_SESSION ||--o{ DETECTION_EVENT : "contains"
    USER ||--o{ DETECTION_SESSION : "owns"
```
