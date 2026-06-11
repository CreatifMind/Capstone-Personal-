import subprocess
import os

html_content = """<html>
<head>
<meta charset="utf-8">
<style>
body {
    font-family: Arial, sans-serif;
    font-size: 11pt;
    line-height: 1.5;
    margin-left: 1.0in;
    margin-right: 1.0in;
    margin-top: 1.0in;
    margin-bottom: 1.0in;
}
h1 {
    text-align: center;
    font-size: 18pt;
    font-weight: bold;
    color: #0F5132;
    margin-bottom: 6pt;
}
h2 {
    font-size: 14pt;
    font-weight: bold;
    color: #212529;
    margin-top: 18pt;
    margin-bottom: 6pt;
    border-bottom: 1px solid #0F5132;
    padding-bottom: 3pt;
}
h3 {
    font-size: 12pt;
    font-weight: bold;
    color: #0F5132;
    margin-top: 12pt;
    margin-bottom: 4pt;
}
p {
    margin-top: 0pt;
    margin-bottom: 6pt;
}
ul {
    margin-top: 0pt;
    margin-bottom: 6pt;
    margin-left: 20px;
}
li {
    margin-bottom: 3pt;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin-top: 12pt;
    margin-bottom: 12pt;
}
th {
    border: 1px solid #dddddd;
    background-color: #0F5132;
    color: white;
    font-weight: bold;
    text-align: left;
    padding: 8px;
    font-size: 10pt;
}
td {
    border: 1px solid #dddddd;
    text-align: left;
    padding: 8px;
    vertical-align: top;
    font-size: 9.5pt;
}
tr:nth-child(even) {
    background-color: #f9f9f9;
}
.note {
    background-color: #f2f7f4;
    border-left: 4px solid #0F5132;
    padding: 10px;
    margin-bottom: 12pt;
}
</style>
</head>
<body>

<h1>PurityLoop AI</h1>
<p style="text-align: center; font-style: italic; color: #555;">Capstone Project Proposal Presentation Outline</p>

<div class="note">
    <strong>Slide Design Theme Recommendation:</strong><br>
    <ul>
        <li><strong>Primary Color:</strong> Deep Emerald Green (#0F5132) representing sustainability and waste stream purity.</li>
        <li><strong>Secondary Color:</strong> Sleek Charcoal/Dark Gray (#212529) for professional, high-contrast text and tables.</li>
        <li><strong>Accent Color:</strong> Vivid Amber/Gold (#FFC107) representing caution/validation (quarantine and the Amber Review Queue).</li>
        <li><strong>Typography:</strong> Montserrat or Outfit for headers, Inter or Roboto for body text (clean, modern sans-serif).</li>
    </ul>
</div>

<h2>Speaker Time Distribution</h2>
<ul>
    <li><strong>Chris</strong> (Project Manager & Quality): Slides 1, 10, 11, 15, 19, 21 (~5 minutes total)</li>
    <li><strong>Naomi</strong> (Data & Ethics Lead): Slides 2, 8, 13, 22 (~3 minutes total)</li>
    <li><strong>Talvin</strong> (ML R&D Lead): Slides 3, 7, 14 (~2.5 minutes total)</li>
    <li><strong>Kong</strong> (RPA & Requirements Lead): Slides 4, 12, 16 (~2.5 minutes total)</li>
    <li><strong>Georgene</strong> (Full-Stack & Gamification Lead): Slides 5, 9, 17, 20 (~3.5 minutes total)</li>
    <li><strong>Feng</strong> (BI & ESG Lead): Slides 6, 18, 22 (~2.5 minutes total)</li>
</ul>

<h2>Slide-by-Slide Contents Outline</h2>

<table>
  <thead>
    <tr>
      <th style="width: 8%;">Slide #</th>
      <th style="width: 22%;">Slide Title</th>
      <th style="width: 15%;">Presenter</th>
      <th style="width: 33%;">Slide Content & Key Bullet Points</th>
      <th style="width: 22%;">Visual/Diagram Recommendation</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1</td>
      <td>Title Slide: PurityLoop AI</td>
      <td>Chris</td>
      <td>
        <ul>
          <li>Project Name: PurityLoop AI</li>
          <li>Subtitle: AI-Driven Waste Contamination Detection, ESG Auditing & Gamified Recycling Platform</li>
          <li>Group Name & Member Names with Roles</li>
        </ul>
      </td>
      <td>Premium title slide with group logo and high-quality sustainability imagery.</td>
    </tr>
    <tr>
      <td>2</td>
      <td>Project Background & Context</td>
      <td>Naomi</td>
      <td>
        <ul>
          <li>The global solid waste crisis (15.2M tonnes in Malaysia)</li>
          <li>12th Malaysia Plan target (40% recycling rate by 2025)</li>
          <li>The core issue: Contamination (6.96% recyclable loss annually)</li>
        </ul>
      </td>
      <td>SWCorp Malaysia recycling target progress bar (37.9% in 2024 vs 40% target).</td>
    </tr>
    <tr>
      <td>3</td>
      <td>The Three Failure Modes</td>
      <td>Talvin</td>
      <td>
        <ul>
          <li>Failure 1: Perceptual ambiguity at material boundaries (human RGB limitations)</li>
          <li>Failure 2: Structural incapacity for machine-read ESG data</li>
          <li>Failure 3: Undetected lithium-ion battery fire hazards</li>
        </ul>
      </td>
      <td>A side-by-side comparison table showing the 3 Failure Modes vs. PurityLoop solutions.</td>
    </tr>
    <tr>
      <td>4</td>
      <td>Research Objectives & Questions</td>
      <td>Kong</td>
      <td>
        <ul>
          <li>The 3 consolidated Research Objectives (automation, hazard gate, ESG auditing)</li>
          <li>Parallel Research Questions (RQ1: mAP, RQ2: Safety Gate cost, RQ3: Latency, RQ4: ESG completeness)</li>
        </ul>
      </td>
      <td>Split-layout slide showing Objectives on the left and matching RQs on the right.</td>
    </tr>
    <tr>
      <td>5</td>
      <td>Project Scope & Delimitations</td>
      <td>Georgene</td>
      <td>
        <ul>
          <li>Scope: 9-class waste detection system, Python RPA watchdog, Streamlit app, custom BI</li>
          <li>Delimitations: Simulated conveyor belt (hot folder drop), estimated carbon mass (no physical scale)</li>
        </ul>
      </td>
      <td>Visual "In Scope" vs "Out of Scope" boundary diagram.</td>
    </tr>
    <tr>
      <td>6</td>
      <td>Significance of the Study</td>
      <td>Feng</td>
      <td>
        <ul>
          <li>CV Innovation: Automated instance segmentation for irregular waste shapes</li>
          <li>Business Impact: Continuous LSS/DMAIC process control</li>
          <li>Environmental Impact: Verifiable, item-level carbon auditing</li>
        </ul>
      </td>
      <td>A 3-column benefit card layout (Computer Vision | Business Analytics | ESG Auditing).</td>
    </tr>
    <tr>
      <td>7</td>
      <td>Lit Review: Waste Classification Evolution</td>
      <td>Talvin</td>
      <td>
        <ul>
          <li>1st Gen: Image Classifiers (no spatial localization)</li>
          <li>2nd Gen: Two-Stage Region-Proposal Detectors (too slow for real-time edge)</li>
          <li>3rd Gen: Single-stage YOLOv8m-seg (selected for speed + contour masking)</li>
        </ul>
      </td>
      <td>Timeline/evolution diagram of computer vision architectures.</td>
    </tr>
    <tr>
      <td>8</td>
      <td>Lit Review: Dataset & Hazard Gaps</td>
      <td>Naomi</td>
      <td>
        <ul>
          <li>Evaluation of public datasets (TrashNet, RealWaste, TACO, GC-V2)</li>
          <li>The critical gap: The omission of safety-critical hazardous classes (batteries)</li>
          <li>Rationale for multi-source dataset fusion</li>
        </ul>
      </td>
      <td>A radar chart or table showing dataset features (GC-V2 is the only one with batteries).</td>
    </tr>
    <tr>
      <td>9</td>
      <td>Lit Review: ESG & Gamification</td>
      <td>Georgene</td>
      <td>
        <ul>
          <li>ESG: AI integration with GRI/ISSB reporting standards (Mustafa et al., 2025)</li>
          <li>Gamification: Eco-credit reward loops for changing user behavior (Venturi et al., 2024)</li>
        </ul>
      </td>
      <td>A dual-loop flow diagram: Upstream Behavior Loop <-> Downstream Facility Ingestion Loop.</td>
    </tr>
    <tr>
      <td>10</td>
      <td>Lit Review: DMAIC & Synthesis Gap</td>
      <td>Chris</td>
      <td>
        <ul>
          <li>DMAIC as a governance framework for MLOps and software quality</li>
          <li>The Synthesis Gap: Lack of academic literature connecting edge model output to corporate databases</li>
        </ul>
      </td>
      <td>The PurityLoop Synthesis Gap graphic showing the disconnected ML and ESG domains.</td>
    </tr>
    <tr>
      <td>11</td>
      <td>Integrated Multi-Framework Approach</td>
      <td>Chris</td>
      <td>
        <ul>
          <li>Macro Governance: Iterative Waterfall</li>
          <li>Quality Backbone: Lean Six Sigma / DMAIC</li>
          <li>Analytics Strategy: BALC + CRISP-DM</li>
          <li>Web Dev & ML Execution: Iterative Prototyping & OSEMN</li>
        </ul>
      </td>
      <td>The PurityLoop AI Conceptual Framework Diagram (Define-Measure-Analyze-Improve-Control).</td>
    </tr>
    <tr>
      <td>12</td>
      <td>System Requirements Specification</td>
      <td>Kong</td>
      <td>
        <ul>
          <li>Key Functional Requirements (watchdog directory, 3-tier confidence, database write)</li>
          <li>Critical Non-Functional Requirements (Latency <= 500ms, mAP >= 0.85)</li>
        </ul>
      </td>
      <td>A structured table displaying high-priority FRs and metrics-bound NFRs.</td>
    </tr>
    <tr>
      <td>13</td>
      <td>Dataset Ingestion & Preprocessing</td>
      <td>Naomi</td>
      <td>
        <ul>
          <li>Dataset acquisition and cleaning (pHash deduplication, annotation remapping)</li>
          <li>Preprocessing pipeline (color normalization, 640x640 resizing, Tenengrad quality filter)</li>
        </ul>
      </td>
      <td>A flow diagram of the Data Prep Pipeline (resize -> normalise -> filter -> remap).</td>
    </tr>
    <tr>
      <td>14</td>
      <td>Model Architecture & Training</td>
      <td>Talvin</td>
      <td>
        <ul>
          <li>YOLOv8m-seg backbone, PANet neck, and mask prototype head</li>
          <li>2-Phase training protocol (Phase A: Reference, Phase B: Frozen backbone + fine-tuning)</li>
        </ul>
      </td>
      <td>Model architecture schematic showing backbone, neck, and dual prediction heads.</td>
    </tr>
    <tr>
      <td>15</td>
      <td>MLOps Quality Gates & Auditing</td>
      <td>Chris</td>
      <td>
        <ul>
          <li>Overfit-one-batch check (sanity check)</li>
          <li>Individual diagnostic training runs (AP >= 0.60 quality gate)</li>
          <li>Cleanlab confident learning algorithmic label-error audit</li>
          <li>Cross-partition duplicate check (zero data leakage check)</li>
        </ul>
      </td>
      <td>A workflow showing the Quality Gate sequence from raw slices to audited master corpus.</td>
    </tr>
    <tr>
      <td>16</td>
      <td>RPA Development: Python Watchdog</td>
      <td>Kong</td>
      <td>
        <ul>
          <li>Folder watchdog library monitoring new frame events</li>
          <li>File validation (mime check, integrity) and quarantine handling</li>
          <li>Relational SQLite database schema (detections, sessions, users)</li>
        </ul>
      </td>
      <td>An Entity-Relationship (ER) diagram representing the database schema.</td>
    </tr>
    <tr>
      <td>17</td>
      <td>Web Application: Streamlit Interface</td>
      <td>Georgene</td>
      <td>
        <ul>
          <li>Operator Inference & Visual Testing Portal (OpenCV overlays, threshold sliders)</li>
          <li>The Amber Review Queue: Human-in-the-loop validation for low-confidence & hazard alerts</li>
        </ul>
      </td>
      <td>Streamlit application wireframe/mockup showing the operator dashboard and threshold sliders.</td>
    </tr>
    <tr>
      <td>18</td>
      <td>Business Intelligence Development</td>
      <td>Feng</td>
      <td>
        <ul>
          <li>Custom HTML/JS/Python dashboard stack</li>
          <li>Real-time KPI cards (Purity %, Material Yield, carbon offset calculations mapped to EPA WARM)</li>
        </ul>
      </td>
      <td>Dashboard mockup displaying the gauge, trend line, and active alert warnings.</td>
    </tr>
    <tr>
      <td>19</td>
      <td>System Evaluation Protocol</td>
      <td>Chris</td>
      <td>
        <ul>
          <li>Performance metrics: mAP@0.5, mAP@0.5:0.95, Recall, and F1</li>
          <li>The Battery Class Recall Gate (recall >= 0.90) priority</li>
          <li>Throughput and end-to-end processing latency benchmarks</li>
        </ul>
      </td>
      <td>A scorecard showing target validation values vs. test metrics.</td>
    </tr>
    <tr>
      <td>20</td>
      <td>Expected Contributions & Value</td>
      <td>Georgene</td>
      <td>
        <ul>
          <li>Operational impact: Contamination deflections upstream, equipment protection, facility safety</li>
          <li>Research contributions: Data-centric MLOps generalizability over architectural changes</li>
        </ul>
      </td>
      <td>A "Before vs. After" comparison grid for MRF sorting lines.</td>
    </tr>
    <tr>
      <td>21</td>
      <td>Project Schedule & Task Delegation</td>
      <td>Chris</td>
      <td>
        <ul>
          <li>14-week Iterative Waterfall Gantt Chart</li>
          <li>Critical path management (diagnostic checks, system integration testing)</li>
          <li>Group delegation of work matrix</li>
        </ul>
      </td>
      <td>Gantt chart timeline split into proposal, core dev, integration, and showcase phases.</td>
    </tr>
    <tr>
      <td>22</td>
      <td>Conclusion & Ethical Considerations</td>
      <td>Feng</td>
      <td>
        <ul>
          <li>Summary of the PurityLoop AI smart recycling ecosystem</li>
          <li>Ethical data governance (phone number hashing via SHA-256, local demonstration containment)</li>
        </ul>
      </td>
      <td>Summary slide with closing remarks.</td>
    </tr>
  </tbody>
</table>

</body>
</html>
"""

temp_html = "temp_outline.html"
output_docx = "PurityLoop_Presentation_Outline.docx"

with open(temp_html, "w", encoding="utf-8") as f:
    f.write(html_content)

# Convert to DOCX using textutil
subprocess.run(["textutil", "-convert", "docx", "-output", output_docx, temp_html], check=True)
os.remove(temp_html)
print(f"Successfully generated {output_docx}")
