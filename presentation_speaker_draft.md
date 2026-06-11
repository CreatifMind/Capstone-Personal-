# PurityLoop AI — Capstone Presentation Speaker Script

**Capstone Project AY2025/26 | Sunway University | Department of Business Analytics**  
**Presenter:** Chris Wong Lihong (Project Manager)  
**Supervisor:** Dr. Narishah Mohamed Salleh  

---

## ⏱️ Presentation Timing & Strategy

* **Total Target Duration:** ~8–10 minutes (approx. 1.5 to 2 minutes per slide).
* **Aesthetic & Tone:** Confident, data-driven, bridging advanced machine learning with tangible business and operational metrics.

---

## 🗂️ Slide-by-Slide Speaker Script

### 📋 Slide 1: Cover & Team Task Delegation

**Slide Title:** PurityLoop AI: Automated Waste Sorting & Contamination Detection  
**Visuals:** Title on the left; "Team Task Delegation" matrix on the right showing 6 members across Backend and Frontend squads.  

#### 🗣️ Speaker Script
>
> "Good morning, Dr. Narishah and members of the panel. Today, we are excited to present our Capstone project: **PurityLoop AI — an Automated Waste Sorting and Contamination Detection platform** designed under the motto 'Smart Waste, Clean Future.'
>
> My name is **Chris Wong Lihong**, and I serve as the Project Manager and Model Evaluator for this project. Over our 14-week delivery timeline, our team of six has been structured into two dedicated squads to ensure a cohesive end-to-end integration:
>
> * The **Backend Squad** focuses on the data-to-model pipeline: **Naomi** manages our multi-dataset preparation and CVAT annotation; **Talvin** and **Gen Wei** oversee the core YOLOv8m-seg model training and optimization; and **Kong** leads the backend API integration.
> * The **Frontend Squad** translates our data layer into enterprise value: **Feng** is responsible for our Business Intelligence dashboard and operational reporting, and **Georgene** designs our Streamlit web application.
>
> Together, we have built an integrated system that replaces traditional manual sorting with real-time computer vision. I will now walk you through the core business problem we are addressing."

---

### ⚠️ Slide 2: Recyclable Loss & Contamination Challenges (Business Problem)

**Slide Title:** Business Problem: Recyclable Loss at Recycling Facilities  
**Visuals:** The Sorting Bottleneck on the left (conveyor belt with contaminant warnings and 30–40% manual error rate badge); The Contamination Crisis on the right (rejected waste bales and the 1 Million Tonnes Rejected Annually metric).  

#### 🗣️ Speaker Script
>
> "To understand why PurityLoop AI is necessary, we must examine the severe contamination crisis currently facing Malaysian recycling facilities.
>
> According to data from **Greenpeace Malaysia (2024)**, recycling plants reject a staggering **1 million tonnes of potentially recyclable materials annually** purely due to late contamination detection. As visualized on the right side of the slide, this results in a massive pile-up of rejected bales diverted directly to landfills.
>
> The root of this crisis is the manual sorting line shown on the left. In practice, operators face three systemic challenges:
>
> 1. **The Sorting Bottleneck:** Manual classification is slow and error-prone, yielding a high error rate of **30% to 40%** under peak volumes.
> 2. **Hazardous Contaminants:** Missed items like **lithium-ion batteries** slip into the compactors, presenting severe workplace safety and fire risks.
> 3. **Financial Penalties:** When a single organic or hazardous contaminant is pressed into a recyclable bale, the entire batch is rejected by buyers, leading to lost resale revenue and tipping fee penalties of up to **RM 250 per tonne**.
>
> PurityLoop AI was developed specifically to solve this quality gate bottleneck."

---

### 💡 Slide 3: Business Solution (4W1H Framework)

**Slide Title:** Business Solution  
**Visuals:** 4W1H (What, When, Where, Who, How) boxes wrapped around a mockup tablet displaying YOLOv8m-seg active segmentation.  

#### 🗣️ Speaker Script
>
> "Our solution is built on a clear, automated workflow outlined by the 4W1H framework:
>
> * **What is it?** PurityLoop AI is an automated waste classification, recyclable recovery, and contamination detection platform.
> * **Who uses it?** It is designed for MRF managers who require high-level yield analytics, and sorting operators who need immediate sorting guidance.
> * **Where is it deployed?** Materials Recovery Facilities (MRFs) and automated waste sorting lines.
> * **How does it work?** High-speed conveyor cameras capture the live sorting stream. Our custom YOLOv8m-seg model processes these frames to identify items, draw precise segmentations, and instantaneously push telemetry to update the Web Dashboard.
> * **When does it operate?** Continually and in real-time, as waste frames pass along the conveyor sorting lines.
>
> As displayed in the tablet mockup, the system doesn't just draw boxes; it uses instance segmentation to isolate irregular shapes like crumpled plastic bottles and soda cans, measuring their exact pixel area to estimate weight and purity."

---

### 🔄 Slide 4: AI Parallel Project Lifecycle

**Slide Title:** AI Parallel Project Lifecycle  
**Visuals:** Software/System Development Lifecycle (SDLC) diagram showing three parallel development tracks (AI Model Development, Web Application Development, Analytics Dashboard) flanked by Requirements/Design on the left and Integration/Testing/Deployment on the right.  

#### 🗣️ Speaker Script
>
> "To execute this project successfully within our timeline, we structured our engineering workflow under a unified Software Development Lifecycle framework, as detailed in this parallel lifecycle diagram based on **Monson (2021)**.
>
> Our workflow begins with collaborative requirements planning and design on the left, which splits into three parallel engineering tracks:
>
> * **Track 1 (AI Model Development):** Follows the **CRISP-DM** and **BALC** methodologies to guide Naomi and Talvin through business understanding, data cleaning, and YOLOv8 model training and evaluation (grounded in **Terven et al., 2023**).
> * **Track 2 (Web Application Development):** Utilizes an iterative prototyping method (caged by **Pongboonchai-Empl et al., 2023**) allowing Georgene to build, user-test, and refine the Streamlit app interface.
> * **Track 3 (Analytics Dashboard):** Employs the **Business Analytics Life Cycle** framework (following **Mustafa et al., 2025**) for Feng to ingest SQLite telemetry data and translate it into Power BI visualizations.
>
> These tracks converge on the right during the Integration and Testing phases, validating our SQLite schemas and API calls, before entering the continuous maintenance loop where operator feedback drives retraining and system improvements."

---

### ⚙️ Slide 5: BPMN Diagram (Waste Classification Business Process)

**Slide Title:** PurityLoop AI — Waste Classification Business Process  
**Visuals:** Swimlanes mapping the Operator, AI Detection Engine, SQLite Data Layer, and Web App & BI Dashboard.  

#### 🗣️ Speaker Script
>
> "This BPMN diagram illustrates the cross-functional logic of our waste classification process, spanning four distinct layers: the Operator, the AI Detection Engine, the SQLite Data Layer, and the Web/BI Dashboard.
>
> 1. The process begins when a frame is captured and received by our **AI Engine running YOLOv8m-seg**.
> 2. The engine runs inference to generate class labels, confidence scores, and segmentation masks.
> 3. We apply an **Asymmetric Safety Gate** at this point:
>     * If the model's confidence is **below 85%**, it is routed to the **Amber Queue**. This triggers an Amber Alert for the operator to manually review and approve or reject the item, keeping a Human-in-the-Loop.
>     * If the confidence is **85% or higher**, it is automatically processed.
> 4. The system then runs a safety-critical check: **Is it a battery?** If a battery is detected, the system immediately fires an operator alert to quarantine the hazard, eliminating fire risks in mechanical compactors.
> 5. For normal recyclables, the record is immediately committed to our SQLite database (`purityloop_telemetry.db`), calculating the purity rate in under 100 milliseconds.
> 6. This database write triggers a synchronous update on the Streamlit Web UI and the dashboard, keeping facility KPIs constantly updated."

---

### 🔄 Slide 6: As-Is vs To-Be Business Process

**Slide Title:** As-Is vs To-Be  
**Visuals:** Flowchart comparing the 7-step manual process (As-Is) against the streamlined 5-step automated process (To-Be).  

#### 🗣️ Speaker Script
>
> "Finally, let’s look at the operational transformation from the **As-Is** manual workflow to our **To-Be** automated workflow.
>
> In the traditional **As-Is process**, sorting is a highly serial, seven-step manual flow. Operators physically sort items, manually assess cleanliness, write logs in paper logbooks, and compile reports by hand. By the time a facility manager decides on process adjustments, days or weeks have passed, and contaminated bales have already been rejected.
>
> With **PurityLoop AI**, we streamline this into a data-driven, five-step **To-Be process**. Material conveying and frame capture are automated. Real-time detection results are written directly to our Web UI and BI dashboards, allowing managers to adjust sorting thresholds instantly.
>
> Importantly, we maintain a **Human-in-the-Loop (HITL)** review process at step 6 for flagged Amber items. This ensures that the system remains highly accurate, protects downstream operations, and logs corrected annotations to retrain and continuously improve our AI model over time.
>
> Thank you, and we would now love to open the floor to any questions from Dr. Narishah and the panel."

---

## 💡 Q&A Cheat Sheet (Anticipating Panel Questions)

### Q1: Why did you choose SQLite over other databases like PostgreSQL?

* **Answer:** *"Since the conveyor runs at high speed, database write latency must be minimal. SQLite operates as a local, serverless database file, allowing us to commit transaction records (`purityloop_telemetry.db`) in under 10 milliseconds, which completely avoids buffering bottlenecks on the edge machine."*

### Q2: Why choose YOLOv8m-seg (medium) instead of a larger model?

* **Answer:** *"We chose the medium variant because it offers the optimal trade-off for edge computing. Larger models (YOLOv8l/x) would drop our inference rate below the required real-time speed of the conveyor belt, while smaller models (nano/small) lacked the recall required to isolate small, deformed contaminants like batteries."*
