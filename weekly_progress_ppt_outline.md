# PurityLoop AI — Weekly Progress Update: Master Slide Document
**Capstone Project AY2025/26 | Sunway University | Department of Business Analytics**
**Supervisor: Dr. Narishah Mohamed Salleh**
**Prepared by: Chris (PM), Talvin (ML), Naomi (Data), Kong (Backend), Georgene (UI), Feng (Analytics)**

---

> **How to use this file**
> - **Slide content** = what goes on the physical slide. Keep it short — Dr. Narishah does not like too many words on one slide.
> - **Speaker notes** = what you say aloud. These answer questions she is likely to ask.
> - **[GEMINI PROMPT]** = copy this text directly into Gemini Image Generation to create the visual for that slide.
> - Numbers marked `[SUGGESTED]` = pre-training estimates based on published research. Replace with real results after training completes.
> - All technical words have been translated into plain English throughout. Where the original term appears, it is in brackets for reference only.

---

---

# SECTION 1 — PROJECT OVERVIEW & MANAGEMENT

---


# SECTION 1 — PROJECT MANAGEMENT

---



## SLIDE 1: Cover Slide

**Slide Title:** PurityLoop AI: Automated Waste Sorting & Contamination Detection

**On the slide:**

| | |
|--|--|
| Project | PurityLoop AI |
| Subtitle | Weekly Progress Update — Capstone AY2025/26 |
| University | Sunway University · Department of Business Analytics |
| Supervisor | Dr. Narishah Mohamed Salleh |
| Domain | Industrial Operations · Quality Assurance · Circular Economy |

**Visual theme:** Emerald Green `#0F5132` and Charcoal Slate. Clean, minimal.

---

> **GEMINI PROMPT — Slide 1 Cover Image**
> A professional presentation cover background. Dark emerald green (#0F5132) gradient from top-left to bottom-right. In the centre: a top-down photograph of a recycling conveyor belt with mixed items — plastic bottles, aluminium cans, cardboard boxes. Overlaid digitally: glowing green bounding boxes around recyclable items, a red bounding box with alarm icon around a battery. Semi-transparent white card in bottom-right corner showing "Purity Rate: 89%". No text in the image. Cinematic, corporate, high quality. Suitable for an academic capstone presentation cover.

---

---


---

---

---


## SLIDE 2: Problem Statement & Contamination Crisis

**Slide Title:** Problem Statement: The Contamination Crisis

**On the slide:**

**The Contamination Crisis in Malaysia:**
- **National Waste Growth:** 15.2M tonnes in 2024; rising to 17M tonnes by 2035 (SWCorp, 2024).
- **Recycling Gap:** Only 37.9% recycling rate achieved in 2024 vs. 12th Malaysia Plan target of 40%.
- **The Contamination Loss:** 6.96% of recyclable waste (~1M tonnes) rejected annually due to contaminants.

**Three Failures of Manual Sorting:**
- **1. Error-Prone:** 30–40% error rate under realistic throughput (Islam & Chowdhury, 2024).
- **2. No Audit Trail:** Manual sorting provides no digital, machine-readable record for operational reporting.
- **3. Occupational Hazard:** Exposure to toxic batteries, e-waste, and sharp biohazards.

**Operational Baseline:**
- ~30% contamination rate in Malaysian facilities operating under manual sorting (Moh & Abd Manaf, 2017).

**Speaker notes:**
This slide establishes the problem statement and the academic background. In Malaysia, total solid waste generation reached 15.2 million tonnes in 2024 and is projected to rise to 17.03 million tonnes by 2035. SWCorp (2024) statistics show we missed the 12th Malaysia Plan target of 40% recycling rate, landing at 37.9% due to contamination. An estimated 6.96% of all waste that could have been recycled is rejected from the recycling stream annually.
Dr. Narishah will ask about the 30% baseline. Ground it in Moh & Abd Manaf (2017), a peer-reviewed study of source separation and recycling practices in Malaysia. Be ready to quote the three failures of manual sorting (Islam & Chowdhury, 2024): error rate, lack of audit trail, and worker safety.

---

> **GEMINI PROMPT — Slide 2 Visual**
> A clean infographic layout on white background showing waste statistics. On the left: a large graphic of Malaysia with a recycling bin icon and the text "37.9% Recycling Rate". On the right: a red warning icon with the text "6.96% Recyclable Loss (~1M Tonnes Rejected)". Below: a comparison showing a hand-sorting icon with "30-40% Error Rate" and a safety hazard warning triangle for lithium batteries. Flat corporate design, emerald green (#0F5132) and charcoal accents, white background.

---

---

---


## SLIDE 3: Project Solution: PurityLoop AI

**Slide Title:** Project Solution: PurityLoop AI

**On the slide:**

**The PurityLoop AI System:**
- An integrated automation system that replaces manual sorting with a high-speed computer vision pipeline.

**Core Solution Components:**
- **Real-Time CV Pipeline:** YOLOv8m-seg instance segmentation identifies and segments waste classes.
- **RPA Data Pipeline:** Automates image monitoring, format checks, database logging, and routing.
- **Live Dashboard:** Translates database events into live KPIs (Purity Rate, Weight saved, Yield).
- **Active Learning Queue:** Feed low-confidence data back for model calibration and improvement.

**Operational Target:**
- Post-deployment purity rate increase from ~70% to ≥90%.
- 30–40% increase in materials recovery facility throughput.

**Speaker notes:**
This slide presents the project solution. Ground this in the Pongboonchai-Empl (2023) framework, which integrates Industry 4.0 technologies into Lean Six Sigma DMAIC. PurityLoop AI is not just a computer vision model — it is a complete integration of CV, RPA, BI, and active learning loops. It has five layers: Data Acquisition, CV Inference, Routing Logic, Business Output, and the Active Learning Loop. Dr. Narishah will look for the connection between the technical layers and the target KPI. The target is a purity rate of ≥90% post-deployment, compared to the ~70% baseline under manual sorting.

---

> **GEMINI PROMPT — Slide 3 Visual**
> A system integration diagram showing four key parts of the PurityLoop solution on a clean white background. Top-left: "Computer Vision Camera". Top-right: "Python RPA Pipeline". Bottom-left: "Manager Calibration Dashboard". Bottom-right: "Operator Active Learning Queue". All four icons connected by emerald green (#0F5132) arrows to a central logo "PurityLoop AI". Clean, flat vector design, corporate color palette, white background.

---

---

---


## SLIDE 4: Business Pitching: The Value Proposition



**Slide Title:** Business Pitching: The Value Proposition

**On the slide:**

**The Business Pitch:**
- An automated waste sorting and purity monitoring system targeting materials recovery facilities (MRFs) to address landfill costs and operational compliance.

**Key Commercial Value Drivers:**
- **Landfill Cost Savings:** Diverting contaminants saves up to **RM 250/tonne** in tipping fees.
- **Resale Value Maximisation:** Pure recyclable bales (plastic/metal) command **20–35% higher prices** from buyers.
- **Process Audit Trail:** Translates raw sorted weights directly into verifiable material yield figures.

**The Market Gap:**
- Existing solutions are either manual (unsafe, slow) or binary (no hazard detection, no material yield auditing).

**Speaker notes:**
This slide presents the commercial pitch for PurityLoop AI. In the waste management sector, MRFs operate on tight margins where bale rejection due to contamination represents a massive financial loss. By automating the quality gate and calculating material-level material yield data, we address both operational revenue and corporate sustainability demand. Dr. Narishah will ask about local tipping fees — in Malaysia, these range from RM 40 to RM 250 per tonne depending on the state and landfill class, making diversion highly profitable.

---

> **GEMINI PROMPT — Slide 4 Visual**
> A clean two-column infographic layout on white background showing commercial value. Left column: a factory icon with a green checkmark showing "20-35% Bale Price Increase". Right column: a landfill truck icon with a red cross showing "Tipping Fee Cost Diverted (RM 250/Tonne)". Below: a digital document icon showing "Verifiable ESG Carbon Audit Trail". Flat corporate style, emerald green (#0F5132) and charcoal colors, white background.

---

---


## SLIDE 5: Project Management & Role Framework

**Slide Title:** Who Does What — Team & Project Goal

**On the slide:**

**Project Goal:**
> Reduce recycling contamination in Malaysian facilities from ~30% (manual sorting) to ≤10% using an AI camera system — while generating verifiable yield improvements data for sustainability reporting.
>
> *(Baseline source: Moh & Abd Manaf, 2017)*

**Team Roles:**

| Name | Role |
|------|------|
| Chris | Project Management & Sustainability Reporting |
| Talvin | AI Model Development |
| Naomi | Data Collection & Preparation |
| Kong | Data Pipeline & Automation |
| Georgene | Application & User Interface |
| Feng | Analytics Dashboard & Carbon Reports |

**Speaker notes:**
The project goal contains two parts — an operational target (contamination rate) and a business reporting target (material yield data). Dr. Narishah will ask about the 30% baseline. The source is Moh & Abd Manaf (2017), a peer-reviewed paper on Malaysian solid waste management. Be ready to quote it.

---

> **GEMINI PROMPT — Slide 4 Visual**
> A clean team structure diagram on white background. Six boxes arranged in two rows, each with a person icon and a role label. Row 1: "Chris — Project Management", "Talvin — AI Model", "Naomi — Data Collection". Row 2: "Kong — Data Pipeline", "Georgene — App & Interface", "Feng — Analytics Dashboard". All boxes connected by thin lines to a central circle labelled "PurityLoop AI". Emerald green (#0F5132) central circle, grey boxes, flat corporate design, white background.

---

---


---

---

---


## SLIDE 6: Current Project Status

**Slide Title:** Where We Are Now — Progress Tracker

**On the slide:**

| Phase | Scope | Status |
|-------|-------|--------|
| **Phase 1** — Requirements & Proposal (Weeks 1–4) | Problem defined, literature reviewed, proposal approved | ✅ Done |
| **Phase 2** — Design & Data Preparation (Weeks 3–5) | 9-category system locked, 227,490 images collected, duplicates removed, data split | ✅ Done |
| **Phase 3** — Development & Integration (Weeks 4–5) | AI model training running, individual quality checks in progress, data pipeline being built | 🔄 In Progress |
| **Phase 4** — Testing & Control (Weeks 6–10) | Full system speed test, 100 real-world photo test, AI self-improvement loop | ⏳ Pending |

**Speaker notes:**
Phase 2 completion means the dataset is clean and ready. 227,490 images were collected, duplicate photos were removed using a similarity check, and a sharpness filter removed blurry images. The data has been split into training (80%) and testing (20%) sets with a hard cap of 5,000 images per category to prevent any one category from dominating.

Phase 3 is currently active — each team member is running their own training test on their own image slice to catch labelling errors before everything is merged.

---

> **GEMINI PROMPT — Slide 5 Visual**
> A clean project timeline Gantt-style progress tracker on white background. Four horizontal rows, each a phase. Row 1 (solid green fill, full width): "Phase 1 — Done ✓". Row 2 (solid green fill, full width): "Phase 2 — Done ✓". Row 3 (half-filled green, animated progress bar look): "Phase 3 — In Progress". Row 4 (empty/grey outline): "Phase 4 — Pending". Weeks 1–10 shown on the x-axis. Phase labels on the left. Small tick icons beside done phases, spinning circle beside in-progress, clock icon beside pending. Emerald green (#0F5132), flat corporate design, white background.

---

---


---

---

---


## SLIDE 7: Project Schedule: Actual vs. Planned Timeline



**Slide Title:** Project Schedule: Actual vs. Planned Timeline

**On the slide:**

**Schedule Comparison (Weeks 1–10):**

| Phase | Activity | Planned Timeline | Actual Timeline | Status |
|-------|----------|------------------|-----------------|--------|
| **Phase 1** | Requirements & Proposal | Weeks 1–4 | Weeks 1–4 | ✅ Done |
| **Phase 2** | Design & Data Preparation | Weeks 3–5 | Weeks 3–5 | ✅ Done |
| **Phase 3** | Development & Diagnostic Run | Weeks 4–5 | Weeks 4–5 | 🔄 Active |
| **Phase 4** | Integration & Control Testing | Weeks 6–10 | Week 6 Started | ⏳ Pending |

**Schedule Compliance:**
- Parallel task execution has eliminated bottlenecks.
- Zero schedule slippage. Critical milestones (proposal approval, dataset locked) met on time.

**Speaker notes:**
This slide shows our actual schedule vs. planned timeline, demonstrating strict adherence to milestones. Dr. Narishah will look for resource scheduling and task dependencies. Chris coordinated the parallel workflow so that Talvin's model training, Kong's RPA pipeline, and Georgene's Streamlit frontend could proceed simultaneously in Sprints. Phase 3 diagnostic training has been launched in parallel with database integration, maintaining zero schedule slippage.

---

> **GEMINI PROMPT — Slide 7 Visual**
> A clean project schedule Gantt chart on white background. Shows four horizontal bars representing Phase 1, Phase 2, Phase 3, and Phase 4. Weeks 1 to 10 are marked along the top. Bars for Phase 1 and 2 are solid green with checkmarks. The bar for Phase 3 is green with diagonal stripes (active). The bar for Phase 4 is light grey. A vertical red dotted line marks the current date at Week 5. Flat design, emerald green (#0F5132) accent, white background.

---

---


## SLIDE 8: Key Project Challenges & How We Solved Them

**Slide Title:** Challenges Faced & Mitigations Applied

**On the slide:**

| Challenge | What happened | How we fixed it |
|-----------|---------------|----------------|
| **Limited computing power** | Free cloud GPU limits training time to 12 hours per session | Saved progress every 5 training rounds; chose a model size balanced for accuracy vs. computing cost |
| **Inconsistent item labelling** | 3 people drawing outlines around the same item may draw them differently | Used the same smart labelling tool for everyone; locked a written rule guide (e.g., a dirty plastic bottle is still labelled "plastic", not "trash") |
| **Too few battery images** | Battery is rare in public datasets — the AI may never learn to recognise it | Merged 6 separate datasets to reach 12,814 battery images; battery still uses a stricter accuracy gate than all other categories |

**Speaker notes:**
The battery challenge is the most important one to articulate. Dr. Narishah may probe this because battery misclassification is the only error type with zero tolerance in the system. One battery allowed into a plastic bale creates a fire risk. The mitigation is not just more data — it is a system-level design choice: the battery confidence gate is set at 90% certainty (vs 85% for all other categories). Any battery detection below 90% certainty is held for human review, not auto-passed.

---

> **GEMINI PROMPT — Slide 6 Visual**
> Three side-by-side problem-solution card pairs on white background. Card pair 1: left card (grey, problem icon ⚠️) "Limited GPU Time", right card (green, solution icon ✓) "Checkpoints every 5 rounds". Card pair 2: left card (grey) "Inconsistent Labelling", right card (green) "Shared labelling guide + same tool". Card pair 3: left card (grey) "Too few battery images", right card (green) "12,814 battery images + stricter 90% gate". Flat corporate design, emerald green solution cards, white background, arrows pointing from problem to solution.

---

---

# SECTION 2 — AI MODEL & DATA PREPARATION

---


---

---

---


## SLIDE 9: How the Whole System Works — The Big Picture

**Slide Title:** PurityLoop AI in 5 Steps

**On the slide:**

```
[Rubbish on belt] → [Camera captures photo] → [AI identifies each item]
                                                        ↓
                    [Dashboard + Carbon Report] ← [System sorts & alerts]
```

| Step | What happens |
|------|-------------|
| 1 | Camera takes a photo of items on the conveyor belt |
| 2 | The photo is automatically picked up by the system |
| 3 | The AI looks at the photo and identifies every item — what it is and how certain it is |
| 4 | The system routes each item: accept, reject, or flag for human check |
| 5 | All results are saved. A live screen shows operators. A carbon report is generated. |

**Before PurityLoop AI:** 1 worker, manual inspection, ~30% error rate.
**After PurityLoop AI:** 1 camera, automatic, target ≤10% error rate.

**Speaker notes:**
This slide establishes the business case. Lead with the numbers: 30% contamination before, target 10% after. Dr. Narishah will want to see this connected to the DMAIC framework — this slide is the **Define** phase. The problem is defined, the baseline is stated, the target is stated.

---

> **GEMINI PROMPT — Slide 7 Visual**
> A clean flat infographic showing 5 steps in a horizontal flow from left to right. Step 1: conveyor belt icon with mixed items. Step 2: camera icon pointing at items. Step 3: AI chip/brain icon with floating category labels (plastic, metal, battery). Step 4: three coloured bins (green/yellow/red). Step 5: laptop dashboard icon with percentage gauge and document icon. Large arrows between steps. Below: two-line comparison — "Before: 1 worker · 30% error" (grey, crossed out) vs "After: 1 camera · target ≤10% error" (green, highlighted). Emerald green (#0F5132), white background, flat corporate style.

---

---


---

# SECTION 2 — BUSINESS INTELLIGENCE (BI) & OPERATIONAL REPORTING

---

---

---


## SLIDE 10: How the Analytics Wrap Around Everything

**Slide Title:** Business Analytics as the Enterprise Layer

**On the slide:**

Every technical output from the system — the AI results, the sorting decisions, the purity calculations — feeds into business analytics tools that turn raw data into management decisions.

**The feedback loop:**

```
[Conveyor belt detections]
         ↓
[Digital logbook accumulates records]
         ↓
[Analytics dashboard reads records → KPIs]
         ↓
[Management reviews KPIs → adjusts operations]
         ↓
[Better operations → cleaner sorting → better KPIs]
```

**What the analytics layer produces:**

| Output | Tool | Who uses it |
|--------|------|------------|
| Live cleanliness rate | Web application dashboard | Sorting supervisor |
| Material recovered by category (kg) | Power BI | Operations manager |
| Carbon saved per session | Power BI | Sustainability team |
| ESG audit report (PDF) | Automated export | Corporate reporting / external auditors |

**Speaker notes:**
This slide connects the engineering outputs to business value — Dr. Narishah will look for this bridge. The phrase to use: "Every detection the AI makes is a data point. Individually, they mean one item sorted. In aggregate, they become a facility's recycling performance, revenue recovery rate, and operational process accountability record." That is the Business Analytics life cycle applied to physical operations.

---

> **GEMINI PROMPT — Slide 8 Visual**
> A clean circular feedback loop diagram on white background. Five boxes connected in a clockwise circle. Box 1: conveyor belt icon, "AI Detections". Box 2: database icon, "Digital Logbook". Box 3: chart/BI icon, "Analytics Dashboard". Box 4: management person icon, "Operations Decisions". Box 5: upward trend arrow icon, "Improved Sorting". Centre of circle: a shield icon with "Business Value". Below: four output cards in a row — "Live Dashboard", "Power BI Charts", "Carbon Report", "Operational Report PDF". Emerald green (#0F5132) circle arrows, white boxes, flat corporate design.

---

---


---

---

---


## SLIDE 11: How We Calculate Recovered Yield — The Formula

**Slide Title:** The Yield Formula — Item by Item

**On the slide:**

$$\text{Recovered Yield (kg)} = \sum_{i=1}^{n} \Bigl[ \text{Count}_i \times w_i \Bigr] \times P$$

**What each part means:**

| Symbol | Plain English |
|--------|---------------|
| $\text{Count}_i$ | The count of items detected in category $i$ in this session |
| $w_i$ | Average weight constant of category $i$ (kg) |
| $P$ | Purity factor — the cleanliness score (penalises contaminated batches) |

**Average weight constants by material**

| Material | Average weight per item (kg) |
|----------|--------------------------|
| Glass | **0.250 kg** (highest — solid glass container) |
| Textile | 0.200 kg |
| Cardboard | 0.150 kg |
| Paper | 0.050 kg |
| PET Plastic | 0.025 kg |
| Aluminium / Metal | **0.015 kg** (lowest — lightweight soda can) |

**Why the purity factor is multiplied at the end:**
> A contaminated batch cannot be fully sorted or reclaimed. If 13% of a batch is food waste or non-recyclable residue, only 87% is clean recyclable yield. The purity factor scales the total yield to match what was actually sorted cleanly.

**Example — one session:**
- 80 plastic bottles (80 × 0.025 = 2.00 kg) + 45 aluminium cans (45 × 0.015 = 0.68 kg) + 20 cardboard boxes (20 × 0.150 = 3.00 kg)
- Cleanliness score: 87% → P = 0.87

$$= (2.00 + 0.68 + 3.00) \times 0.87 = 5.68 \times 0.87 = \mathbf{4.94 \text{ kg cleanly recovered yield}}$$

**Note:** camera cannot measure weight directly — weight is estimated using class-average constants per item (e.g., 1 PET bottle ≈ 0.025 kg). This introduces ±15–30% weight estimation error, disclosed as a known limitation.

**Speaker notes:**

**Q: Where do the average weight constants come from?**
> "From standard industrial packaging benchmarks. These represent the average weight of post-consumer containers under typical sorting configurations. The exact values are finalized against local facility averages before deployment."

**Q: Why multiply by purity at the end?**
> "The purity rate applies to the entire batch, not to individual material types. We calculate maximum possible yield first, then scale down by the actual proportion that is clean enough to be accepted. This matches how standard waste management auditing treats batch contamination."

**Q: Is this traceable for a real process audit?**
> "Yes. Every detection is recorded in the digital logbook with its timestamp, category, certainty score, and zone. The formula inputs — item count per category, purity rate per session — come directly from those records. Any auditor can recalculate any session's yield figure from the raw database entries."

**Q: What about battery — is it included in the yield calculation?**
> "No. Battery is routed to hazardous quarantine, not recyclable bins. Hazardous battery handling requires specialized e-waste tracking, which is processed under a separate operational stream."

---

> **GEMINI PROMPT — Slide 9 Visual**
> A clean two-panel slide visual on white background. Left panel: a vertical bar chart showing average weight per item by material — glass tallest (0.25), then textile (0.20), cardboard (0.15), paper (0.05), plastic (0.025), metal (0.015). Bars coloured dark-to-light green. Right panel: a worked example box showing 3 items → calculation → result "4.94 kg cleanly recovered yield". A small legend note: "Purity factor scales final result — contaminated batch claims less yield". Emerald green accents, white background, flat corporate design.

---

---


---

---

---


## SLIDE 12: Business Analytics Life Cycle



**Slide Title:** Business Analytics Life Cycle

**On the slide:**

**The 4 Stages of Waste Analytics:**
- **1. Descriptive (What happened?):** Live charts showing material yield (kg) and purity percentage per sorting session.
- **2. Diagnostic (Why did it happen?):** Bounding box audit trails showing which contaminant caused a purity drop.
- **3. Predictive (What will happen?):** Trend forecasts estimating monthly material yields and tipping fee savings.
- **4. Prescriptive (How can we improve?):** Automated zone routing alerts and active learning retrain triggers.

**The Integration Layer:**
- Analytics serves as the bridge between deep learning outputs (pixel segmentations) and business reports.

**Speaker notes:**
This slide defines the Business Analytics life cycle applied to PurityLoop AI. Dr. Narishah will ask how our analytics goes beyond simple descriptive charts. The system moves from descriptive reporting to prescriptive action. When an operator reviews low-confidence items in the Amber zone, those prescriptive corrections are captured by SQLite, which automatically triggers model updates. This represents a mature prescriptive loop where analytics directly drives AI improvement.

---

> **GEMINI PROMPT — Slide 12 Visual**
> A clean four-step staircase infographic on white background showing the stages of Business Analytics. Step 1: Descriptive (bar chart icon). Step 2: Diagnostic (magnifying glass icon). Step 3: Predictive (trend line with forecast icon). Step 4: Prescriptive (gear and circular arrows icon). Emerald green (#0F5132) gradient steps from light to dark, white background, flat corporate design.

---

---


## SLIDE 13: Bidirectional Loop: Power BI & Web App



**Slide Title:** Bidirectional Loop: Power BI & Web App

**On the slide:**

**The Traditional One-Way Flow:**
- Database → Power BI Dashboard (Passive visual reporting).

**The PurityLoop Bidirectional Loop:**
- **1. Ingest:** Web App writes raw detection coordinates and confidence scores to SQLite.
- **2. Analyze:** Power BI audits logs, identifying specific category contamination trends.
- **3. Define:** Analytical findings define new operational thresholds and gamified points weights.
- **4. Enforce:** Web App dynamically reads new rules from database and adjusts operator alerts.

**Example Feedback Loop:**
- **BI Finding:** Battery contamination increased by 15% in zone B.
- **Web App Action:** App raises battery threshold to 92% and triggers targeted UI alerts.

**Speaker notes:**
This slide illustrates that Power BI is not just a passive dashboard. It is a decision-support component that feeds requirements back into the Web Application. In the PurityLoop framework, data flows bidirectionally. When Power BI analysis identifies a spike in contamination, it adjusts the active rules (such as confidence gates or gamified points payouts) stored in the database, which the Web Application reads dynamically at startup.

---

> **GEMINI PROMPT — Slide 13 Visual**
> A clean circular bidirectional data flow diagram on white background. Shows two main components: a web app mockup icon on the left and a Power BI chart dashboard icon on the right. Two thick emerald green (#0F5132) arrows form a circle connecting them: top arrow points from Web App to BI (labelled "Detections logged"), bottom arrow points from BI to Web App (labelled "Business rules updated"). Flat vector design, white background.

---

---


## SLIDE 14: How Data Drives Operations — 3 Business Rules

**Slide Title:** From Dashboard Number to Operational Action

**On the slide:**

The analytics dashboard does not just display numbers — it triggers specific actions:

| Dashboard reading | What the system does | Business outcome |
|------------------|---------------------|-----------------|
| Cleanliness score drops below 85% | Warning appears on operator screen. Alert to check incoming batch. | Contaminated bale caught before it reaches the buyer |
| Battery detected in sorting stream | Alarm sounds on operator screen. Item routed to hazardous quarantine immediately. | Worker safety protected. Liability risk eliminated. |
| Operator completes audit on Amber item | Corrected labels written to database. RETRAIN trigger queues next training sweep. | Continuous active learning loop adapts to new packaging variants |
| Carbon savings pass the monthly reporting threshold | System automatically generates a PDF carbon report ready for submission | operational reporting completed without manual data compilation |

**Before PurityLoop AI:** contamination found at buyer facility → bale rejected → revenue lost → no data on why.

**After PurityLoop AI:** contamination flagged at sorting stage → batch corrected before dispatch → revenue protected → full audit trail available.

**Speaker notes:**
Dr. Narishah's research connects analytics to business outcomes — she will appreciate that each dashboard reading maps to a specific, named operational response. This is the **Control** phase of DMAIC. The system is not just measuring performance — it is triggering corrective action. The feedback loop from detection → alert → action → cleaner batch is the sustained improvement mechanism that DMAIC requires.

---

> **GEMINI PROMPT — Slide 10 Visual**
> A clean three-column trigger-action table infographic on white background. Column 1 (grey): "Dashboard Reading" — three icons: warning triangle, battery with alarm, star/trophy. Column 2 (emerald green arrows pointing right). Column 3 (green): "Action Taken" — three icons: operator checking belt, hazard quarantine box, coin/reward. Below: a before/after comparison bar. Left (grey, strikethrough): "Before: contamination found at buyer — revenue lost". Right (green): "After: caught at belt — revenue protected". Flat corporate design, white background.

---

---


---

# SECTION 3 — WEB APPLICATION DEVELOPMENT

---

---

---


## SLIDE 15: The Application — What It Does and Who Uses It

**Slide Title:** Two Roles, One Portal

**On the slide:**

The system has one web application that opens in any browser — no installation needed. It shows two different views depending on the user's role:

| | Operator View | Manager View |
|--|----------------|------------|
| **Who uses it** | Sorting line operator / QA staff | Operations manager / operational compliance auditor |
| **What they see** | Real-time conveyor alerts, battery warning panels, Amber review queue | Tonnage throughput charts, material yield metrics, PDF ESG exporter |
| **Main function** | Auditing low-confidence items and priority hazard flags | Adjusting YOLOv8 threshold sliders and exporting operational reports |

**How the AI connects to the screen:**
> The screen loads the AI model directly. When a photo is uploaded or detected from the camera, the AI analyses it and the results appear on screen in under 0.5 seconds.

**Development progress:**
- Sprint 1: Layout designs on paper (wireframes)
- Sprint 2: Screens built with sample data — in progress

**Speaker notes:**
Dr. Narishah may ask about the technical connection between the screen and the AI. The web application loads the trained AI model file (`best.pt`) at startup. Every photo that arrives goes through the AI and results are displayed immediately. This is the point of integration — described in detail in Slide 12.

---

> **GEMINI PROMPT — Slide 11 Visual**
> Two side-by-side screens on white background. Left: a desktop mockup showing the Streamlit "Operator view" with a list of cropped items in the Amber Review queue and confirmed button. Right: a desktop mockup showing the Streamlit "Manager view" with a line chart of conveyor throughput, sliders for accept/reject thresholds, and an export CSV button. Centre label: "One web application · Dedicated Operator & Manager Roles". Emerald green (#0F5132) interface color, flat UI design, corporate style.

---

---


---

---

---


## SLIDE 16: Web Application: Development Life Cycle & Gaps



**Slide Title:** Web Application: Development Life Cycle & Gaps

**On the slide:**

**Software Development Life Cycle (SDLC):**
- **Agile Scrum Methodology:** Two-week sprint iterations.
  - **Sprint 1 (Weeks 3–4):** GUI wireframing, SQL schema design, role definitions.
  - **Sprint 2 (Weeks 5–6):** Streamlit prototype building, mock data rendering, and logic routing.
  - **Sprint 3 (Weeks 7–8):** Integration of YOLO inference model and active learning review screens.

**What-IS vs. To-Be Analysis:**

| Feature | What-IS (Standard Dashboard) | To-Be (PurityLoop App) |
|---------|-----------------------------|------------------------|
| Camera Integration | Static images only | Live camera feed with bounding box overlay |
| Data Processing | Batch processing | Real-time SQLite logging (<100ms) |
| Feedback Loop | Read-only graphs | Active learning Amber Review queue |

**Speaker notes:**
This slide details the software development lifecycle for the application layer. We follow an Agile Scrum model. Georgene focuses on bridging the gap between a standard static analytics screen ("What-IS") and the real-time PurityLoop app ("To-Be"). The primary gap we are addressing is live integration: standard business dashboards are read-only, whereas the PurityLoop interface acts as a control center that passes user inputs back to the AI model database.

---

> **GEMINI PROMPT — Slide 16 Visual**
> A comparison table graphic on a clean white background. Shows two vertical columns. Left column (grey, "What-IS"): icons representing static, disconnected, manual systems. Right column (emerald green, "To-Be"): icons representing real-time conveyor feeds, automated database logs, and a user review interface. Clean flat design, white background, corporate style.

---

---


## SLIDE 17: Point of Integration — How All Parts Connect

**Slide Title:** The Junction — How Screen, AI, and Records Connect

**On the slide:**

The point of integration is where three separate parts of the system exchange information. Nothing is hardcoded or manual — every connection is automated.

**The full data journey in under 0.5 seconds:**

| Step | What happens | Time |
|------|-------------|------|
| 1 | Camera drops photo into the monitored folder | Instant |
| 2 | File monitor picks up the photo | < 0.5 sec |
| 3 | Photo is resized to the standard input size | < 0.1 sec |
| 4 | AI reads the photo and outputs labels + certainty scores + outlines | 0.1–0.3 sec |
| 5 | Decision gate assigns Green / Yellow / Red zone | Instant |
| 6 | Record is written to the digital logbook | Instant |
| 7 | Screen refreshes with new detection and updated scores | < 0.1 sec |
| **Total** | | **< 0.5 seconds** |

**Who connects where:**

| Team member | What they built | Where it connects |
|------------|----------------|------------------|
| Naomi | Training data | Feeds into Talvin's AI model |
| Talvin | AI model | Feeds results into Kong's pipeline |
| Kong | File monitor + pipeline | Feeds results into the digital logbook |
| Georgene | Screens | Reads from the digital logbook |
| Feng | Analytics dashboard | Reads from the digital logbook |
| Chris | operational report | Pulls from Feng's dashboard |

**Speaker notes:**
The critical integration point is between the AI model and the web application — the application loads the trained model file at startup and calls it for every photo received. The output (label, certainty, outline coordinates) is passed to the routing logic, then written to the database. Dr. Narishah may ask how the screen stays live — the web application polls the database every few seconds for new entries and updates the display without the user refreshing.

---

> **GEMINI PROMPT — Slide 12 Visual**
> A clean hub-and-spoke diagram on white background. Central hub circle (emerald green): "Web Application — Integration Point". Six spoke boxes around it: "Camera Feed" (top), "AI Model" (top-right), "Digital Logbook" (right), "Analytics Dashboard" (bottom-right), "ESG Report" (bottom), "Operator & Manager Views" (left). Arrows from camera to hub (labelled "photo in"), hub to AI (labelled "send for analysis"), AI back to hub (labelled "result returned"), hub to logbook (labelled "saved"), logbook to dashboard (labelled "read"). Below: a timing bar "End-to-end: under 0.5 seconds". Emerald green hub, grey spokes, white background, flat corporate design.

---

---


---

# SECTION 4 — DEEP LEARNING (DL) & DATA PREPARATION

---

---

---


## SLIDE 18: Deep Learning Framework: YOLOv8m-seg

**Slide Title:** Deep Learning Framework: YOLOv8m-seg

**On the slide:**

**YOLOv8m-seg Architecture:**
- **Backbone (CSP-DarkNet):** Hierarchical feature extraction of irregular shapes (Terven et al., 2023).
- **Neck (FPN + PAN):** Multi-scale feature aggregation for small object detection (Lu et al., 2023).
- **Head (Decoupled Anchor-Free):** Separate classification and localisation branches.
- **Segmentation Layer:** Bounding box + class label + confidence score + pixel-level mask.

**Training Specifications & Hyperparameters:**

| Parameter | Value | Justification |
|-----------|-------|---------------|
| Image Size | 640×640 px | Native resolution; prevents out-of-memory on T4 GPU |
| Batch Size | 16 | Hardware limit for T4 16GB VRAM |
| Optimizer | AdamW | Decoupled weight decay; optimized convergence (Ajayi et al., 2024) |
| Focal Loss | Weighted | Dynamically weights rare class (Battery) (Mahmoodi et al., 2025) |

**Transfer Learning:**
- Fine-tuned on ~30k images using COCO-pretrained weights (Zhang et al., 2021).

**Speaker notes:**
Dr. Narishah will ask why we selected YOLOv8s/m over other architectures. Midigudla et al. (2025) comparative analysis shows YOLOv8 outperforming EfficientDet and Detectron2 in accuracy and inference speed on waste classification, achieving mAP >85%. The decoupled anchor-free head reduces false positives on irregular shapes (Terven et al., 2023). Because battery images are rare, we use automatically weighted focal loss (Mahmoodi et al., 2025) to prevent the model from ignoring the safety-critical hazard class.

---

> **GEMINI PROMPT — Slide 13 Visual**
> A technical diagram of the YOLOv8m-seg neural network architecture on a clean white background. Shows three main blocks connected by arrows: "Backbone (CSP-DarkNet)", "Neck (FPN + PAN)", and "Head (Decoupled Anchor-Free)". The Head splits into two output branches: "Bounding Box Detection" and "Instance Segmentation Mask". Clean technical drawing, flat design, emerald green (#0F5132) and charcoal colors, white background.

---

---

---


## SLIDE 19: Enhanced Machine Learning Framework



**Slide Title:** Enhanced Machine Learning Framework

**On the slide:**

**The Enhancement Pipeline:**
- **Baseline Model:** YOLOv8m-seg pre-trained on COCO dataset (no waste-specific labels).
- **Enhanced PurityLoop Model:** Tuned specifically for heterogeneous industrial waste sorting.

**Key Technical Enhancements:**
- **Focal Loss Adjustment:** Dynamically weights class loss to prioritize the rare Battery class.
- **Anchor-Free Decoupled Head:** Optimises object bounding boxes and masks independently.
- **Conveyor Augmentations:** Mosaic augmentation and Copy-Paste overlays model overlapping waste.
- **Stricter Bounding Box NMS:** Non-Maximum Suppression tuned to 0.35 to prevent duplicate detections.

**Speaker notes:**
This slide shows how we enhance the baseline deep learning model for our specific domain. Pre-trained weights on the COCO dataset are insufficient because waste items are frequently crushed, overlapping, or dirty. We enhance the model's loss function using focal loss to prevent class overlap, and we use domain-specific data augmentations (like Mosaic and Copy-Paste) to train the model to handle heavily occluded and piled waste on the moving conveyor.

---

> **GEMINI PROMPT — Slide 19 Visual**
> A technical diagram showing the model enhancement process on white background. On the left: a box "Baseline YOLOv8m-seg (Pre-trained COCO)". An arrow pointing right passes through three gear icons: "Focal Loss", "Mosaic Augmentation", and "Anchor-Free Tuning". On the right: a larger green box "Enhanced PurityLoop Model (Waste Domain)". Flat corporate illustration, emerald green (#0F5132) accent, white background.

---

---


## SLIDE 20: Methodology: Extended CRISP-DM Framework



**Slide Title:** Methodology: Extended CRISP-DM Framework

**On the slide:**

**CRISP-DM Phases for PurityLoop:**
- **1. Business Understanding:** Problem defined (30% contamination, RM loss).
- **2. Data Understanding:** Ingesting ~227k images from 6 datasets.
- **3. Data Preparation:** Perceptual hash deduplication, blur filtering, 5,000 per class balancing.
- **4. Modelling:** Fine-tuning YOLOv8m-seg for instance segmentation.
- **5. Evaluation:** Generalisation test on 100 quarantine images; checkpoints verification.
- **6. Deployment:** Integration with SQLite, Streamlit frontend, and watchdog pipeline.

**The PurityLoop Extension:**
- **Active Learning Feedback Loop:** Deployed model logs low-confidence items to SQLite, which are reviewed and re-fed into Data Preparation.

**Speaker notes:**
This slide connects our methodology to the industry-standard CRISP-DM framework. We explicitly extend CRISP-DM by introducing a bidirectional active learning feedback loop from deployment back to data preparation. Rather than being a static, one-way pipeline, PurityLoop AI continuously improves by capturing operator corrections in the SQLite database and using them to retrain the model.

---

> **GEMINI PROMPT — Slide 20 Visual**
> A clean circular flowchart of the CRISP-DM lifecycle on white background. Six boxes arranged in a circle: Business Understanding, Data Understanding, Data Preparation, Modeling, Evaluation, Deployment. Standard loop arrows connect them. An extra thick emerald green (#0F5132) arrow loops from Deployment back to Data Preparation, labelled "Active Learning Feedback Loop". Flat design, white background.

---

---


## SLIDE 21: The Project Life Cycle — How We Built the AI

**Slide Title:** 10-Step AI Build Process — Quality Gate at Every Step

**On the slide:**

**3 Stages, 10 Steps:**

**Stage 1 — Prepare the Teaching Materials (Steps 1–5)**

| Step | What we do |
|------|-----------|
| 1. Clean Photos | Remove blurry and duplicate images |
| 2. Label Items | Draw outlines around every item and name the category |
| 3. Solo Training Test | Each person trains a mini-AI on their own photos to find labelling mistakes |
| 4. Cross-Check Labels | Team compares labels — must agree ≥85% of the time |
| 5. Remove Bad Labels | Automated tool flags and removes incorrect labels |

**Stage 2 — Train & Improve (Steps 6–8)**

| Step | What we do |
|------|-----------|
| 6. Merge & Count | Combine all cleaned photos into one pool |
| 7. First Training Run | Train AI with zero settings changed — record accuracy as the benchmark |
| 8. Fine-Tune Settings | Change one setting at a time; keep only changes that improve accuracy |

**Stage 3 — Test & Protect (Steps 9–10)**

| Step | What we do |
|------|-----------|
| 9. Blind Test | Run AI on 100 photos it has never seen before — test if it can generalise |
| 10. Learn from Failures | If blind test fails, AI retrains on the photos it got wrong, then re-tested |

**The key rule:** every step has a pass/fail gate. Fail = go back and fix. Do not move forward with bad data.

**Speaker notes:**
Dr. Narishah will recognise this as a DMAIC process discipline — she will ask: "What happens if a step fails?" The answer is explicit: the system has defined fail actions for every gate. Phase 3 gate: per-category accuracy must reach ≥60%. Phase 9 gate: accuracy drop on unseen photos must be ≤10%. This is the **Measure** and **Analyze** phases of DMAIC.

---

> **GEMINI PROMPT — Slide 14 Visual**
> A clean three-stage vertical flowchart with 10 numbered steps. Stage 1 (steps 1-5): light green background, icons — camera, pen, brain, handshake, trash. Stage 2 (steps 6-8): medium green, icons — merge arrows, training chart, tuning sliders. Stage 3 (steps 9-10): dark green, icons — test beaker, circular arrows. Red "back" arrows between key steps showing quality gates. Small lock icon at the bottom "Deploy Only After Step 9 Passes". Flat design, emerald green colour scheme, white background, corporate style.

---

---


---

---

---


## SLIDE 22: What the AI Needs to Solve — The Problem & Gap

**Slide Title:** Why Simple Photo Recognition Is Not Enough

**On the slide:**

**The problem on a conveyor belt:**
- Items are squashed, torn, and piled on top of each other
- Simple photo classification (what is in this photo?) fails when multiple items overlap
- One battery hidden under cardboard = entire bale rejected = revenue lost

**What we use instead:** the AI draws a precise outline around each individual item — even when they overlap. This lets it count, classify, and calculate separately for each object.

**The gap in existing systems:**
| What existing systems do | What PurityLoop adds |
|--------------------------|---------------------|
| Detect items — yes or no | Detect + outline each item precisely |
| No "uncertain" category | A holding zone for items the AI is unsure about |
| Binary: recyclable or trash | 9 categories including hazardous (battery) |
| No material yield data | Item-level carbon calculation per session |

**Speaker notes:**
Dr. Narishah will probe the "why not simpler?" question. The answer is the piled/overlapping problem — when a battery sits on top of a plastic bag, a simple classifier sees one blurry blob and guesses wrong. Precise outlining (instance segmentation) treats each object as separate regardless of overlap. This is not a feature added for complexity — it is required by the physical reality of a conveyor belt.

---

> **GEMINI PROMPT — Slide 15 Visual**
> Two side-by-side comparison images on white background. Left image (grey, labelled "Simple Recognition — Fails"): a photo of overlapping rubbish items with one large bounding box around the whole pile and a "?" label — shows the system cannot tell items apart. Right image (green, labelled "PurityLoop — Separate Outlines"): same photo but each item has its own precise coloured outline — green outline around a plastic bottle, blue outline around a can, red outline around a partially hidden battery. A caption below reads "Each item identified separately, even when overlapping." Flat illustration style, emerald green accent, white background.

---

---


---

---

---


## SLIDE 23: Cleaning the Data Before Training

**Slide Title:** How We Prepared 227,490 Images

**On the slide:**

**Raw data → clean training data in 4 steps:**

| Step | What we did | Why |
|------|------------|-----|
| **1. Collect** | Merged 6 public datasets across 9 categories | No single dataset had all 9 categories including battery |
| **2. Remove duplicates** | Used a photo similarity check (comparing compressed image fingerprints) | Duplicate photos in training inflate accuracy scores — the model looks good because it memorised, not learned |
| **3. Remove blurry images** | Applied a sharpness score filter; images scoring below the threshold were removed | Blurry training images teach the AI to be uncertain on clear images |
| **4. Balance categories** | Hard cap: 5,000 images per category maximum | Prevents the AI from becoming biased toward the most common category (food waste, which had 139,909 images) |

**Final dataset:** ~45,000 images · 9 categories · 5,000 per category · 80% training / 20% testing

**Speaker notes:**
The balancing step is critical to explain. Before capping, food waste (food_organic) made up 61.5% of all images. Without balancing, the AI would learn to guess "food waste" for everything and still appear 61.5% accurate. After capping at 5,000 per category, all 9 categories are equally represented. This is honest evaluation.

---

> **GEMINI PROMPT — Slide 16 Visual**
> A clean four-step funnel infographic on white background. Wide top: "Raw Data — 227,490 images from 6 datasets". Arrow down to: "Step 1: Remove Duplicates — fingerprint comparison". Arrow down to: "Step 2: Remove Blurry Images — sharpness filter". Arrow down to: "Step 3: Balance Categories — 5,000 per category max". Narrow bottom: "Clean Dataset — ~45,000 images · 9 categories · ready for training". Numbers shown at each step showing count reducing. Emerald green funnel, white background, flat design, corporate style.

---

---


---

---

---


## SLIDE 24: How We Split the Data & The Accuracy Floor

**Slide Title:** Data Split & Baseline 1 — Setting the Accuracy Floor

**On the slide:**

**How the data is split:**

| Set | Purpose | Size |
|-----|---------|------|
| **Training set** (80%) | AI learns from these photos | ~36,000 images (4,000 per category) |
| **Testing set** (20%) | AI is tested on photos it has never seen | ~9,000 images (1,000 per category) |
| **Quarantine set** (100 photos) | Locked away until the very end — final real-world test | 100 real-world photos, never touched during training |

**Baseline 1 — The Accuracy Floor:**

> If the AI ignores every photo and always guesses the most common category, how often would it be right?

| | Value |
|--|--|
| Categories | 9 (all equally balanced) |
| Blind guess accuracy | **11.1%** (1 in 9) |
| What this means | Our AI must score **above 11.1%** to prove it learned anything at all |

> **11.1% is the floor. Any model below this has not learned — it is worse than a coin flip across 9 options.**

**Speaker notes:**
This number is often misunderstood. Before data balancing, the majority category (food waste) was 61.5% of all images. An AI that always says "food waste" would score 61.5% — impressive looking but useless. After balancing (5,000 per category cap), the honest floor is 1/9 = 11.1%. This is the correct Baseline 1. Dr. Narishah will recognise this as rigorous measurement — it connects directly to the DMAIC Measure phase.

The quarantine set is important: 100 real-world photos were locked away before any training began. No team member sees them until Phase 9. This is the "hold-out" that tests whether the AI generalises to the real world, not just the training photos.

---

> **GEMINI PROMPT — Slide 17 Visual**
> A clean two-panel infographic on white background. Left panel: a data split pie chart showing 80% (dark green, "Training"), 20% (medium green, "Testing"), with a separate small circle labelled "100 photos — locked quarantine". Right panel: a simple comparison table — a balance scale icon where one side shows "AI always guesses food waste → 61.5% (dishonest)" and the other side shows "After balancing → 11.1% floor (honest)". Below: bold text "Our AI must beat 11.1% to prove it learned something real." Emerald green accent, white background, flat design.

---

---


---

---

---


## SLIDE 25: AI Model Structure & The 3 Accuracy Checkpoints

**Slide Title:** How We Know the AI Is Actually Learning — 3 Checkpoints

**On the slide:**

**The AI model we use:** YOLOv8m-seg *(a pre-taught visual recognition model, fine-tuned on our waste data)*

**It works in 3 layers:**

| Layer | What it does in plain English |
|-------|------------------------------|
| **Visual Processing** (CSP-DarkNet) | Reads the photo and identifies edges, textures, shapes |
| **Scale Combiner** (PANet) | Combines details seen at different zoom levels — catches both tiny batteries and large cardboard boxes |
| **Decision Head** | Two outputs: what is this item (classification) + draw its outline (segmentation) |

**3 Accuracy Checkpoints — Each Must Beat the One Before:**

| Checkpoint | What it is | Expected score `[SUGGESTED]` |
|-----------|-----------|-------------------------------|
| **Checkpoint 1 — Blind Guess** | Always predict the most common category | 11.1% accuracy |
| **Checkpoint 3 — Solo Runs** (Phase 3) | Each person's mini-AI trained on their own photos | mAP: 0.52–0.76 |
| **Checkpoint 2 — First Full Run** (Phase 7) | Full merged dataset, no settings changed | mAP: 0.58–0.70 `[SUGGESTED]` |
| **Final Target** (Phase 8) | Tuned master model | mAP: **≥0.85** |

**Quality gate sequence:**
1. Solo training test → any category below 60% accuracy → fix labels, re-run
2. Label cross-check → team agreement must reach ≥85%
3. Automated label error scan → remove flagged mistakes before merging
4. Duplicate check across training/testing → must find zero shared photos

**Speaker notes:**
The three checkpoints follow a strict logic: every subsequent model must beat everything before it. If Checkpoint 2 (full merged run) does not beat the solo runs (Checkpoint 3), the merge made things worse — go back to Phase 6 and investigate the merge quality.

The battery category has its own separate tracking. Overall accuracy averages across all 9 categories. If the model scores 95% on the 8 non-battery categories but 30% on battery, the overall score reads ~87% — passing the gate but hiding a safety-critical failure. Battery is always reported separately.

For the final target: Midigudla et al. (2025) published a direct comparison of AI models on waste classification. YOLOv8 achieved >85% accuracy. That is the published benchmark for this exact model type and problem — matching it means our results are consistent with peer-reviewed findings.

---

> **GEMINI PROMPT — Slide 18 Visual**
> A clean upward staircase infographic on white background. Four steps from left (low) to right (high). Step 1 (grey, lowest): "Blind Guess — 11.1%". Step 2 (light green): "Solo Runs — 0.52–0.76". Step 3 (medium green): "First Full Run — 0.58–0.70". Step 4 (dark green, highest, gold star): "Final Target — ≥0.85". A bold upward arrow running along the steps labelled "Each step must beat the step before." Below step 4: a small battery icon with a separate label "Battery tracked separately — target ≥0.80". Emerald green gradient, white background, flat corporate design.

---

---

# SECTION 3 — WEB APPLICATION & DATA PIPELINE

---


---

# SECTION 5 — HUMAN-IN-THE-LOOP (HITL) & RPA PIPELINE

---

---

---


## SLIDE 26: Human-in-the-Loop (HITL) & Quality Framework

**Slide Title:** Human-in-the-Loop (HITL) & Quality Framework

**On the slide:**

**The HITL Quality Framework (Mosqueira-Rey et al., 2023):**
- **Phase 4 Quality Gate:** Cross-team label review targeting >85% inter-annotator agreement.
- **Phase 10 Active Learning:** Ambiguous detections feed human review queue → retrain loop.

**Algorithmic Quality Check:**
- **Cleanlab (Confident Learning):** Automatically identifies systematic annotation errors.

**Inference Routing & Confidence Gates:**

| Zone | Confidence | Action |
|------|------------|--------|
| **Green** (Recyclable) | ≥ 0.85 | Auto-pass to recycling stream |
| **Red** (Hazard/Contaminant) | ≥ 0.90 (Battery) / ≥ 0.85 (Trash) | Auto-reject — quarantine alert |
| **Amber** (Uncertain) | < 0.85 (Recyclable) / < 0.90 (Battery) | Route to Amber Queue for human check |

**Speaker notes:**
This slide presents our Human-in-the-Loop (HITL) quality framework. We integrate two layers of quality check: human-in-the-loop and algorithmic confident learning (Cleanlab). HITL checks catch judgment calls, whereas Cleanlab catches systematic label errors. This follows Mosqueira-Rey et al. (2023) research showing that human-first review gates yield higher dataset purity. Explain the three confidence zones: green (auto-pass), red (auto-reject), and amber (human review). The battery class has a stricter threshold of 90% due to zero fire risk tolerance. Low-confidence detections are written to the database, where they accumulate until a 100-sample threshold triggers active learning (Menke et al., 2024).

---

> **GEMINI PROMPT — Slide 19 Visual**
> A flowchart showing the 3-Zone Routing Logic and human-in-the-loop validation on a clean white background. Shows a detection event passing to a decision diamond. The diamond splits into three colored paths: Green Path (≥0.85) pointing to "Auto-Sort", Red Path (≥0.90 / ≥0.85) pointing to "Auto-Reject", and Amber Path (<0.85 / <0.90) pointing to a user icon "Human Review Queue". The Human Review Queue loop points back to "Active Learning Retrain". Flat, clean vector art, white background.

---

---

---


## SLIDE 27: HITL Framework: Theoretical Taxonomy



**Slide Title:** HITL Framework: Theoretical Taxonomy

**On the slide:**

**Four Types of Human-AI Integration (Mosqueira-Rey et al., 2023):**

| HITL Type | Description | PurityLoop Implementation |
|-----------|-------------|---------------------------|
| **Human-in-the-Loop (HITL)** | Human approves or corrects AI decision before execution. | **Amber Queue:** Operator labels uncertain items before database logging. |
| **Human-on-the-Loop (HOTL)** | AI processes autonomously; Human monitors and overrides exceptions. | **Operator Screen:** Factory manager overrides belt speed or alerts. |
| **Human-over-the-Loop (HOOTL)** | AI executes decisions; Human audits outcomes retrospectively. | **Operational Dashboard:** Sustainability auditors review monthly carbon records. |
| **Human-as-the-Loop (HATL)** | Human makes all decisions; AI serves only as passive advice. | N/A (Manual sorting - baseline pre-system state). |

**Speaker notes:**
This slide presents the theoretical taxonomy of Human-AI integration based on Mosqueira-Rey et al. (2023). Dr. Narishah will expect you to understand these definitions. PurityLoop AI does not use a single integration style; it is a hybrid. We use Human-in-the-Loop (HITL) for the active learning review process (where the operator labels uncertain items), and we use Human-on-the-Loop (HOTL) for the operator dashboard, allowing the supervisor to override alerts or stop the belt.

---

> **GEMINI PROMPT — Slide 27 Visual**
> A clean three-column comparison table infographic on white background showing the types of Human-AI integration. Three rows with distinct colored icons: Human-in-the-Loop (cog icon with human silhouette), Human-on-the-Loop (monitor screen icon with human eye), and Human-over-the-Loop (checklist document icon with magnifying glass). Emerald green (#0F5132) and charcoal colors, flat corporate design, white background.

---

---


## SLIDE 28: The Data Pipeline — What Happens Behind the Scenes

**Slide Title:** The Automated Pipeline — No Manual Button Pressing

**On the slide:**

**4 parts that work together automatically:**

```
[Camera drops photo into folder]
            ↓
[File Monitor detects new photo] ← checks if valid, rejects corrupt files
            ↓
[AI identifies every item] ← draws outlines, assigns labels and certainty scores
            ↓
[Decision Gate] → Green (accept) / Yellow (hold) / Red (reject)
            ↓
[Digital Logbook records everything] ← timestamp, label, certainty, zone
```

**File Monitor detail:**

| Situation | What happens |
|-----------|-------------|
| Valid photo arrives | Passed to AI within 0.5 seconds |
| Corrupted or non-image file arrives | Moved to a separate error folder, logged — pipeline never crashes |
| Folder is empty | System waits silently — no error, no crash |

**Digital logbook saves within 100ms of each detection.**

**Speaker notes:**
Dr. Narishah published on automation pipelines (SVRA paper, 2022) — she will probe the robustness question: "What if the folder receives a bad file?" The explicit answer is here: MIME type validation, file inteoperational auditty check, quarantine folder for malformed files, logged to error_log.csv. The pipeline is designed to never crash from bad input. This is what separates a production-ready automation from a fragile demo.

---

> **GEMINI PROMPT — Slide 20 Visual**
> A clean vertical pipeline flowchart on white background with 5 stages. Stage 1 (top): folder icon + camera, "Camera drops photo". Stage 2: shield/filter icon, "File Monitor — checks photo is valid". Two branches: green arrow "Valid → continue" and red arrow "Invalid → error folder". Stage 3: AI brain icon, "AI identifies items — labels + certainty scores". Stage 4: three-colour traffic light, "Decision Gate — Green / Yellow / Red". Stage 5 (bottom): database cylinder, "Digital Logbook — saved within 100ms". Emerald green arrows, white background, flat design.

---

---


---

---

---


## SLIDE 29: The Digital Record Book — What Gets Saved

**Slide Title:** What the System Saves — The Digital Audit Trail

**On the slide:**

Every item that passes through the system is recorded in a digital database — like a structured spreadsheet that never gets deleted.

**3 tables:**

**Table 1 — People (User)**

| What is saved | Example |
|--------------|---------|
| Scrambled phone number (privacy protected) | Not stored as readable text |
| Eco-credit points total | 247 pts |
| Session history | 12 sessions, avg. 89% clean |

**Table 2 — Each Sorting Session (Detection_Session)**

| What is saved | Example |
|--------------|---------|
| Cleanliness score for this session | 87% |
| Total weight of recyclable material | 12.4 kg |
| Carbon saved this session | 9.39 kg Weight |
| Total items detected | 342 |

**Table 3 — Each Item Detected (Detection_Event)**

| What is saved | Example |
|--------------|---------|
| Category | plastic |
| Certainty score | 91% |
| Zone assigned | Green |
| Position outline coordinates | [saved automatically] |
| Alarm triggered | No |

**Privacy:** phone numbers are scrambled (SHA-256) before storage. The original number is never saved anywhere in the system.

**Speaker notes:**
Dr. Narishah's SVRA paper emphasises audit trail inteoperational auditty. The three-table structure is the technical implementation of that — every detection is traceable back to the session, the user, and the specific photo. This makes the Weight calculation reproducible: any auditor can recalculate any session's carbon figure from the raw Detection_Event records.

---

> **GEMINI PROMPT — Slide 21 Visual**
> A clean entity-relationship diagram on white background. Three rectangular table boxes. Top-centre box: "USER — scrambled ID, eco-credits, session history". Bottom-left box: "DETECTION SESSION — cleanliness score, weight, weight sorted, item count". Bottom-right box: "DETECTION EVENT — category, certainty %, zone, outline coords, alarm". Lines connecting User to Session (one user has many sessions), Session to Event (one session has many events). Lock icon beside USER box labelled "Privacy protected". Emerald green table headers, white table body, grey borders, flat corporate design.

---

---


---

---

---


## SLIDE 30: The Human Review Step — When the AI Is Unsure

**Slide Title:** The Yellow Zone — Human Review Protects Against AI Mistakes

**On the slide:**

The system never forces a wrong decision. When the AI is not certain enough, it holds the item and asks a human.

**3-Zone System:**

| Zone | Condition | What happens |
|------|-----------|-------------|
| 🟢 **Green** | AI is ≥85% certain + item is recyclable | Auto-accepted to recycling stream |
| 🔴 **Red** | AI is ≥85% certain + item is hazardous or non-recyclable | Auto-rejected, alert sounds |
| 🟡 **Yellow** | AI certainty falls below 85% for any category | Item held — shown to operator on screen for manual confirmation |

**Battery exception:** battery must reach ≥90% certainty before auto-rejecting. Below 90%, even a likely battery goes to Yellow for human check.

**What human confirmations do:**
> Every time an operator confirms or corrects an item in the Yellow zone, that correction is saved. When 100 corrections accumulate, the AI re-trains on those corrections — it learns from the exact cases it was uncertain about.

**This is why the system improves over time without team intervention.**

**Speaker notes:**
Dr. Narishah will ask why the threshold is 85% and not 100%. At 100% certainty requirement, almost every item would be flagged for human review — the automation provides no value. At 85%, the vast majority of clear-cut items are handled automatically, while genuinely ambiguous items reach the human. The 85% threshold is consistent with the confidence levels reported in Midigudla et al. (2025) for production waste sorting systems.

The active learning loop is the key system design feature — the Yellow zone is not just a safety net, it is a data collection mechanism. Operator corrections become new training data. The AI gets better at exactly the cases it struggles with.

---

> **GEMINI PROMPT — Slide 22 Visual**
> A clean three-path decision diagram on white background. Top: one item (bottle) on conveyor belt. Three arrows branching downward. Left path (green background): "GREEN ≥85% certain, recyclable → Auto-accept ✓". Centre path (yellow/amber background): "YELLOW below threshold → Human review on screen ⚠️". Right path (red background): "RED ≥85% certain, hazardous → Auto-reject + alert 🔴". Below the Yellow path: a circular arrow labelled "Human corrections → AI learns → system improves". Battery icon with note "Battery: stricter ≥90% gate". Flat design, emerald green and grey, white background.

---

---

# SECTION 4 — BUSINESS ANALYTICS & OPERATIONAL REPORTING

---


---

# APPENDIX A — ALL GEMINI IMAGE PROMPTS (CONSOLIDATED)

Copy each prompt directly into Gemini Image Generation. No modification needed.

---

# APPENDIX B — BASELINES & PURITY RATE FORMULA (DETAILED REFERENCE)

*For speaker use. Not for the slide — these are the full explanations behind the numbers shown on Slides 10, 23, and 24.*

---

## B1 — Baseline 1: The 11.1% Floor

**What it is:** If the system ignores every photo and always guesses the most common category, it is correct 11.1% of the time — because after balancing, all 9 categories are equally represented (1/9 = 11.1%).

**Why not 61.5%:** Before balancing, food_organic made up 61.5% of all images. Always guessing "food waste" scores 61.5% accuracy — but that is a dishonest baseline. After capping at 5,000 images per category, every category has equal representation. The honest floor is 11.1%.

**Key rule:** every model trained — solo runs, first full run, final tuned model — must beat 11.1% on the balanced validation set. Anything below is worse than a random guess.

---

## B2 — Baseline 3: Individual Diagnostic Runs (Phase 3)

**What it is:** Each person trains a test model on their own photos only. Not the final model — a diagnostic tool to catch labelling mistakes before everything is merged.

**Expected ranges `[SUGGESTED]`:**

| Person | Dataset | Training size | Expected mAP@0.5 |
|--------|---------|--------------|-----------------|
| Person A | TrashNet + RealWaste + YOLO Waste | ~10,000 | 0.60 – 0.72 |
| Person B | Garbage Classification v2 + Roboflow | ~22,000 | 0.64 – 0.76 |
| Person C | TACO + edge cases | ~3,000–6,000 | 0.48 – 0.62 |

**Gate:** every category must reach accuracy ≥0.60. Fail = fix labels and re-run.

**Battery watch (Person B):**
- ≥0.70 → proceed
- 0.60–0.69 → review confusion matrix for battery→metal confusion
- <0.60 → re-annotate battery images before proceeding

**Why Person C's range is lower:** Person C deliberately labelled hard images — overlapping items, unusual angles. A lower score is expected. Person C's confusion matrix is the most valuable diagnostic output.

---

## B3 — Baseline 2: First Full Training Run (Phase 7)

**What it is:** After merging all clean photo sets (Phases 4–6), the model is trained once on the full 36,000-image set with zero settings changed from default. This score is the benchmark all Phase 8 tuning must beat.

**Expected results `[SUGGESTED]`:**

| Metric | Expected range | Reason |
|--------|---------------|--------|
| mAP@0.5 | 0.58 – 0.70 | Default settings, 9 categories, no focal loss or class weight tuning |
| mAP@0.5:0.95 | 0.38 – 0.52 | Stricter accuracy threshold — reveals mask boundary weaknesses |
| Precision | 0.62 – 0.74 | Default confidence threshold not optimised |
| Recall | 0.55 – 0.68 | Battery and textile recall expected lowest |
| Battery category accuracy | 0.48 – 0.65 | Visually similar to metal cans at default settings |
| Speed (frames per second) | 28 – 35 FPS | YOLOv8m-seg on T4 GPU at standard resolution, batch=1 |

**Why lower than the 0.85 target:** Baseline 2 is intentionally untuned. No focal loss, no class weight adjustment, no copy-paste augmentation. Each of these is added in Phase 8 — one at a time — and each improvement over Baseline 2 is documented evidence that the tuning worked.

---

## B4 — Final Target: Phase 8 Tuned Model

| Metric | Target | Source |
|--------|--------|--------|
| mAP@0.5 | ≥0.85 | Midigudla et al. (2025) — YOLOv8 >85% on waste classification |
| mAP@0.5:0.95 | ≥0.70 | Validates mask outline quality, not just detection |
| Precision | ≥0.85 | Asymmetric error principle — false positives on battery = zero tolerance |
| Recall | ≥0.80 | False negatives routed to Yellow zone — acceptable if caught |
| Battery accuracy | ≥0.80 | Tracked separately — cannot be hidden in overall average |
| Speed | ≥25 FPS | Conveyor belt real-time requirement |
| Accuracy drop on unseen photos | ≤10% | Phase 9 pass gate |

**Phase 8 tuning sequence (one parameter per run):**

| Run | What changes | Expected effect |
|-----|-------------|----------------|
| 1 | Input resolution: 640 → 1280 pixels | Finer detail for small items like batteries |
| 2 | Category loss weighting (cls) | Upweights battery and textile — hardest categories |
| 3 | Copy-paste augmentation | Teaches model to handle overlapping items on belt |
| 4 | Rotation angle (degrees) | Generalises to odd-angle waste on moving conveyor |

**If target is not met:** document the actual result honestly. Deploy with a wider Yellow zone (lower the auto-pass threshold) so more items go to human review. Acknowledge the gap as a limitation with a Phase 10 improvement plan. Dr. Narishah will respect a transparent gap over an uncited claim.

---

## B5 — Master Comparison Table

| | Baseline 1 | Baseline 3 | Baseline 2 | Final Target |
|--|--|--|--|--|
| **Description** | Blind majority guess | Per-person solo run | Full merge, no tuning | Tuned master model |
| **Phase** | Pre-training | Phase 3 | Phase 7 | Phase 8 |
| **mAP@0.5** | — | 0.52–0.76 `[SUGGESTED]` | 0.58–0.70 `[SUGGESTED]` | **≥0.85** |
| **Classification accuracy** | 11.1% | — | — | — |
| **Battery accuracy** | — | 0.48–0.65 `[SUGGESTED]` | 0.48–0.65 `[SUGGESTED]` | **≥0.80** |
| **What it proves** | Any model must beat this | Label quality per person | Merging data works | Tuning adds value |

> **Reading rule:** every column must beat the column to its left. If it does not, that stage failed — go back.

---

## B6 — Carbon Formula Full Reference

**The formula:**

$$\text{CO}_2\text{e Saved (kg)} = \sum_{i=1}^{n} \Bigl[ m_i \times \bigl( \text{EF}^{\text{virgin}}_i - \text{EF}^{\text{recycled}}_i \bigr) \Bigr] \times P$$

**Variable breakdown:**

| Symbol | Full name | Plain English |
|--------|----------|---------------|
| $n$ | Number of recyclable categories | 6: plastic, paper, cardboard, metal, glass, textile |
| $m_i$ | Mass of category $i$ (kg) | Estimated: item count × class-average weight constant |
| $\text{EF}^{\text{virgin}}_i$ | Virgin emission factor (kg Weight/kg) | Weight to make 1 kg from raw resources |
| $\text{EF}^{\text{recycled}}_i$ | Recycled emission factor (kg Weight/kg) | Weight to process 1 kg through recycling |
| $P$ | Purity factor (decimal) | Cleanliness score — penalises contaminated batches |

**Mass estimation — weight constants per item:**

| Category | Weight per item | Assumption |
|----------|----------------|-----------|
| Plastic bottle (PET) | 0.025 kg | Standard 500 mL bottle |
| Aluminium can | 0.015 kg | Standard 330 mL can |
| Glass bottle | 0.300 kg | Standard 750 mL bottle |
| Cardboard box | 0.150 kg | Small corrugated box |
| Paper item | 0.005 kg | Single sheet |
| Textile item | 0.200 kg | Lightweight garment |

**Known limitation:** weight constants introduce ±15–30% error. The dashboard labels all Weight figures as "estimated". Future fix: load cell sensor on conveyor for real weight measurement.

**Emission factor table** *(source: JEM, 2024 — verify values before final submission)*

| Material | EF_virgin (kg Weight/kg) | EF_recycled (kg Weight/kg) | Net saving (kg Weight/kg) |
|----------|------------------------|--------------------------|------------------------|
| Aluminium / Metal | 8.24 | 0.60 | **7.64** |
| Textile | 4.00 | 1.20 | **2.80** |
| PET Plastic | 2.15 | 0.45 | **1.70** |
| Paper | 1.10 | 0.25 | **0.85** |
| Cardboard | 0.94 | 0.21 | **0.73** |
| Glass | 0.86 | 0.30 | **0.56** |

**Why aluminium saves the most:** raw aluminium smelting from bauxite ore uses ~8.24 kg Weight per kg. Recycling requires only ~7% of that energy (0.60 kg Weight/kg). One 330 mL aluminium can ≈ 0.11 kg Weight avoided when recycled.

**Why the purity factor multiplies at the end:** the purity rate applies to the whole batch. A 13% contamination rate means 13% of material may not be accepted by the recycler. Multiplying at the end scales the total saving by actual accepted yield — consistent with operational audit operational performance auditing standards.

**Worked example — one session:**
- 80 PET bottles → 80 × 0.025 = 2.00 kg
- 45 aluminium cans → 45 × 0.015 = 0.68 kg
- 20 cardboard boxes → 20 × 0.150 = 3.00 kg
- Purity Rate = 87% → P = 0.87

$$= [(2.00 \times 1.70) + (0.68 \times 7.64) + (3.00 \times 0.73)] \times 0.87$$
$$= [3.40 + 5.20 + 2.19] \times 0.87 = 10.79 \times 0.87 = \mathbf{9.39 \text{ kg CO}_2\text{e saved}}$$

---

---

# APPENDIX C — PRE-PRESENTATION CHECKLIST

**For Talvin (ML):**
- [ ] Replace all `[SUGGESTED]` mAP values with actual training results
- [ ] Confirm battery accuracy is tracked as a separate column in training results — not averaged into overall mAP
- [ ] Have confusion matrix screenshots ready (especially battery row vs metal column)
- [ ] Know the exact training setup: epochs, patience, batch size, image resolution

**For Chris (PM):**
- [ ] Verify JEM (2024) emission factor values against the actual paper before presenting Slide 10
- [ ] Moh & Abd Manaf (2017) — know the 30% contamination figure and be ready to quote the paper title

**For Naomi (Data):**
- [ ] Know the final dataset count after deduplication (how many photos were removed)
- [ ] Know the class distribution after balancing (should be ~5,000 per category)

**For Kong (Backend):**
- [ ] Know what happens when the folder receives a non-image file (MIME check → quarantine folder → error_log.csv)
- [ ] Know the database table structure — be ready to walk through it

**For Georgene (UI):**
- [ ] Have wireframe or mock screenshots ready for Slides 14 and 17
- [ ] Know the connection between the screen and the AI model file

**For Feng (Analytics):**
- [ ] Know the three KPIs: cleanliness score formula, material yield calculation, purity rate formula
- [ ] Power BI mock dashboard ready if possible

**For everyone:**
- [ ] Dr. Narishah will ask each person about their own layer — know your section deeply
- [ ] DMAIC alignment: be able to name which DMAIC phase your work belongs to
- [ ] Do not claim exact accuracy numbers unless training is complete — say "expected range based on published benchmarks" and cite Midigudla et al. (2025)

---

*PurityLoop AI Capstone AY2025/26*
*Master Slide Document — Frameworks + Baselines + Carbon Formula + Gemini Prompts*
*Written: 2026-06-03 | All `[SUGGESTED]` values = pre-training estimates from literature. Replace after training completes.*
*Sources: Midigudla et al. (2025) · JEM (2024) · Moh & Abd Manaf (2017) · ecoinvent 3.x (EF values pending JEM verification)*
