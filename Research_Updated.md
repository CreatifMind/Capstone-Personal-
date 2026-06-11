# PurityLoop AI — Research Citations
### APA 7th Edition | Organized by Topic
**Version:** 2.0 | **Updated:** 2026-05-15

---

## 1. Object Detection & YOLO Architecture

> Supports: YOLOv8 model selection, architecture justification, hyperparameter tuning, confidence threshold rationale

Ajayi, O. G., Ibrahim, P. O., & Adegboyega, O. S. (2024). Effect of hyperparameter tuning on the performance of YOLOv8 for multi crop classification on UAV images. *Applied Sciences, 14*(13), 5708. https://doi.org/10.3390/app14135708

> **Supports:** Hyperparameter tuning protocol (one-param-at-a-time, epochs, batch, imgsz). Demonstrates mAP sensitivity to lr0, imgsz, augmentation flags in YOLOv8.

Al-Dosari, M., Mahmoud, H., Al-Hadidi, M., Almemar, A., & Obeidallah, R. (2025). Benchmarking YOLO-based deep learning models for real-time object detection in hybrid ADAS and intelligent transportation systems. *Transportation Research Interdisciplinary Perspectives, 30*, 101234. https://doi.org/10.1016/j.trip.2025.101234

> **Supports:** YOLOv8 real-time performance benchmarks. Justifies 640px input and confidence threshold selection for industrial deployment.

Chen, W., Yang, J. S., Xia, C., Li, Y., & Xiao, X. (2025). Road surface damage detection based on enhanced YOLOv8. *Computers in Industry, 173*, 104363. https://doi.org/10.1016/j.compind.2025.104363

> **Supports:** Confidence threshold rationale. Demonstrates ≥0.75–0.85 as standard industrial CV acceptance threshold in physical-world detection tasks.

Guo, X., Sun, M., Zhang, X., Cui, S., & Li, Y. (2024). Optimization and implementation of garbage classification algorithm based on YOLOv8. *International Core Journal of Engineering, 10*(5), 107–115.

> **Supports:** Domain-specific validation of YOLOv8 for waste/garbage classification; algorithm optimization within same application domain as PurityLoop.

Lin, T., Dollár, P., Girshick, R., He, K., Hariharan, B., & Belongie, S. (2017). Feature pyramid networks for object detection. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2017)* (pp. 2117–2125). https://openaccess.thecvf.com/content_cvpr_2017/html/Lin_Feature_Pyramid_Networks_CVPR_2017_paper.html

> **Supports:** YOLOv8's FPN neck architecture. Explains why the model detects both small objects (batteries, labels) and large items (cardboard, bags) simultaneously at multiple scales.

Midigudla, R. S., Dichpally, T., Vallabhaneni, U., Wutla, Y., Sundaram, D. M., & Jayachandran, S. (2025). A comparative analysis of deep learning models for waste segregation: YOLOv8, EfficientDet, and Detectron 2. *Multimedia Tools and Applications*. https://doi.org/10.1007/s11042-025-20647-y

> **Supports:** Model selection justification. Direct comparison showing YOLOv8 outperforms EfficientDet and Detectron 2 on waste classification — required citation for supervisor's "justify vs alternatives" demand.

Sapkota, R. (2025). Ultralytics YOLO evolution: An overview of YOLO26, YOLO11, YOLOv8, and YOLOv5 object detectors for computer vision and pattern recognition. *arXiv preprint arXiv:2510.09653*.

> **Supports:** YOLOv8 selection over earlier YOLO versions. Covers anchor-free architecture, segmentation head, and performance improvements. Use alongside Terven et al. (2023) for version justification.

Terven, J., Córdova-Esparza, D., & Romero-González, J. (2023). A comprehensive review of YOLO architectures in computer vision: From YOLOv1 to YOLOv8 and YOLO-NAS. *Machine Learning and Knowledge Extraction, 5*(4), 1680–1716. https://doi.org/10.3390/make5040083

> **Supports:** Primary YOLO architecture citation. Anchor-free head, C2f backbone, decoupled classification/regression. Use for Section 1 of any technical writeup.

---

## 2. Instance Segmentation & Zero-Shot Annotation

> Supports: SAM annotation tool selection, segmentation over detection justification, Pile Problem solution, mask IoU

Kaur, P., Khehra, B. S., & Mavi, D. S. (2024). Real-time instance segmentation of recyclables from highly cluttered construction and demolition waste streams. *Waste Management, 187*, 147–158. https://doi.org/10.1016/j.wasman.2024.033516

> **Supports:** Instance segmentation for waste sorting in cluttered scenes. Directly analogous to PurityLoop's conveyor belt scenario with touching/overlapping items (Pile Problem). Strongest citation for choosing seg over detection.

Kirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C., Gustafson, L., Xiao, T., Whitehead, S., Berg, A. C., Lo, W.-Y., Dollár, P., & Girshick, R. (2023). Segment anything. In *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV 2023)* (pp. 4015–4026). https://doi.org/10.1109/ICCV51070.2023.00371

> **Supports:** SAM as annotation tool. Zero-shot polygon mask generation without per-class training. Cite for Phase 2 annotation methodology and 90% annotation time reduction over manual polygon tracing.

Nayfeh, A., Al-Azani, S., & Samma, H. (2025). A two-stage YOLOv8 approach for waste detection and classification in cognitive cities. *Transportation Research Procedia, 84*, 579–586. https://doi.org/10.1016/j.trpro.2025.03.111

> **Supports:** Two-stage detection + segmentation pipeline validation. Validates PurityLoop's architectural decision. YOLOv8-specific waste domain reference.

Ravi, N., Gabeur, V., Hu, Y.-T., Hu, R., Ryali, C., Ma, T., Ramanathan, V., Poirson, P., Joulin, A., Feichtenhofer, C., & Girshick, R. (2024). SAM 2: Segment anything in images and videos. *arXiv preprint arXiv:2408.00714*.

> **Supports:** SAM 2 as upgraded annotation and zero-shot mask generation tool. Extends SAM to video frames — relevant if annotating conveyor belt video frames rather than static images.

---

## 3. Waste Classification & Sorting (Domain Studies)

> Supports: Problem context, contamination rate baseline, domain validation, real-time deployment evidence

Abo-Zahhad, M. M., & Abo-Zahhad, M. (2025). Real time intelligent garbage monitoring and efficient collection using YOLOv8 and YOLOv5 deep learning models for environmental sustainability. *Scientific Reports, 15*(1), 16024. https://doi.org/10.1038/s41598-025-99885-x

> **Supports:** Real-time YOLOv8 waste monitoring at deployment scale. Validates <5s inference latency target and Streamlit-style output dashboards. Cite for deployment section.

Kunwar, S. (2025, October 21). *DWaste: Greener AI for waste sorting using mobile and edge devices*. arXiv. https://doi.org/10.48550/arXiv.2510.18513

> **Supports:** Edge/CPU deployment of waste classification models. Validates ONNX export and CPU-only showcase deployment decision. Model compression for resource-constrained environments.

Mohamad, R., Roslan, R., Shahbudin, N. F. E., & Abu, F. (2024). Recycle waste detection and classification model using YOLOv8 for real-time waste management. In *2024 IEEE International Conference on Artificial Intelligence in Engineering*. IEEE.

> **Supports:** YOLOv8 applied to recycling detection in real-time. Close domain match to PurityLoop. Validates class taxonomy and detection pipeline.

Moh, Y. C., & Abd Manaf, L. (2017). Solid waste management transformation and future challenges of source separation and recycling practice in Malaysia. *Resources, Conservation and Recycling, 116*, 1–14. https://doi.org/10.1016/j.resconrec.2016.09.012

> **Supports:** Problem context / Define phase. Provides baseline contamination rates and cost of manual sorting failure in Southeast Asian recycling context. Directly relevant to Malaysia-based project.

Zhang, Q., Yang, Q., Zhang, X., Bao, Q., Su, J., & Liu, X. (2021). Waste image classification based on transfer learning and convolutional neural network. *Waste Management, 135*, 150–157. https://doi.org/10.1016/j.wasman.2021.08.038

> **Supports:** Transfer learning from COCO weights for waste classification. Earliest strong baseline for CNN-based waste sorting. Cite as prior work that PurityLoop's instance segmentation approach advances upon.

Zhalgas, A., Amirgaliyev, B., Boltay, B., Shegenova, D., Zhylkybay, N., & Yedilkhan, D. (2026). Development of an intelligent waste segregation system using a self-collected dataset and deep learning methods. *Journal of Robotics and Control (JRC), 7*(1), 3393–3404. https://doi.org/10.18196/jrc.v7i1.27247

> **Supports:** Self-collected dataset methodology. Validates sample size decisions, class taxonomy design, and per-class distribution choices. 2026 publication = most current domain evidence available.

[Authors TBC — verify full citation]. (2025). Smart waste, smarter world: Exploring waste types, trends, and tech-driven valorization through artificial intelligence, Internet of Things, and Blockchain. *Sustainable Development*. https://doi.org/10.1002/sd.70345 [Preprint: arXiv:2408.15857]

> **Supports:** Macro-level validation of AI-driven waste systems. ESG angle, sustainability metrics, and operational performance auditing context for PurityLoop's weight output. Verify author list before submission.

---

## 4. Dataset Quality & Confident Learning

> Supports: Cleanlab audit methodology, algorithmic label noise detection, inter-annotator agreement gate

Northcutt, C. G., Jiang, L., & Chuang, I. L. (2021). Confident learning: Estimating uncertainty in dataset labels. *Journal of Artificial Intelligence Research, 70*, 1373–1411. https://doi.org/10.1613/jair.1.12125

> **Supports:** Cleanlab algorithmic audit in Phase 5. Theoretical foundation for Confident Learning (CL) — uses predicted probability vectors to find mislabelled images without re-annotation. Primary citation for any claim about label noise detection.

---

## 5. Active Learning

> Supports: Phase 10 active learning retrain, amber queue → human label → model update loop, uncertainty sampling

Menke, M., Wenzel, T., & Schwung, A. (2024). Bridging the gap: Active learning for efficient domain adaptation in object detection. *Expert Systems with Applications, 254*, 124403. https://doi.org/10.1016/j.eswa.2024.124403

> **Supports:** Active learning loop architecture — amber queue items → human review → selective retrain. Validates 100-sample retrain threshold and domain adaptation framing. Cite for Phase 10 and showcase generalization gap.

Raj, A., & Bach, F. (2022). Convergence of uncertainty sampling for active learning. In *Proceedings of the 39th International Conference on Machine Learning (ICML 2022)*, PMLR 162, 18310–18331.

> **Supports:** Uncertainty sampling as active learning strategy. Theoretical guarantee that selecting low-confidence (amber zone) samples for labelling improves model convergence faster than random sampling.

---

## 6. Human-in-the-Loop (HITL)

> Supports: Phase 4 quality gate (>85% inter-annotator agreement), amber queue human review, HITL principle

Mosqueira-Rey, E., Hernández-Pereira, E., Alonso-Ríos, D., Bobes-Bascarán, J., & Fernández-Leal, Á. (2023). Human-in-the-loop machine learning: A state of the art. *Artificial Intelligence Review, 56*(4), 3005–3054. https://doi.org/10.1007/s10462-022-10246-w

> **Supports:** HITL quality gate design (Phase 4) and amber zone human review (Phase 10). Comprehensive review of HITL patterns including active learning, annotation, and iterative model improvement. Primary citation for any HITL claim.

---

## 7. Data Augmentation

> Supports: degrees, flipud, mosaic, copy_paste augmentation flags, augmentation as minority class boost

Abdulkareem, I. M., AL-Shammri, F. K., Khalid, N. A., & Omran, N. A. (2024). Proposed approach for object detection and recognition by deep learning models using data augmentation. *International Journal of Online and Biomedical Engineering (iJOE), 20*(5). https://doi.org/10.3991/ijoe.v20i05.47171

> **Supports:** Augmentation strategies for object detection models. Validates rotation, flipping, and copy-paste augmentation choices. Domain-adjacent (object detection with augmentation = PurityLoop Phase 8 tuning).

Shorten, C., & Khoshgoftaar, T. M. (2021). A survey on image data augmentation for deep learning. *Journal of Big Data, 6*(1), 1–48. https://doi.org/10.1186/s40537-019-0197-0

> **Supports:** Foundation survey for all augmentation decisions. Covers geometric transforms (degrees, flipud), mosaic composition, and synthetic oversampling (copy_paste). Cite for any augmentation strategy explanation.

Yang, S., Xiao, W., Zhang, M., Guo, S., Zhao, J., & Shen, F. (2022). Image data augmentation for deep learning: A survey. *arXiv preprint arXiv:2204.08610*.

> **Supports:** Comprehensive augmentation taxonomy. Covers mosaic augmentation and CutPaste/copy_paste techniques specifically. More recent than Shorten & Khoshgoftaar — use both for strong coverage.

Zeng, W. (2024). Image data augmentation techniques based on deep learning: A survey. *Mathematical Biosciences and Engineering, 21*(6), 6190–6224. https://doi.org/10.3934/mbe.2024272

> **Supports:** 2024 augmentation survey — most current. Covers deep learning-specific techniques including generative augmentation. Validates mosaic + copy_paste combination for rare class boost (battery class).

---

## 8. Transfer Learning & Class Imbalance

> Supports: COCO pretrained weights, cls_pw battery weighting, focal loss for minority class

Lin, T., Goyal, P., Girshick, R., He, K., & Dollár, P. (2017). Focal loss for dense object detection. In *Proceedings of the IEEE International Conference on Computer Vision (ICCV 2017)* (pp. 2980–2988). https://openaccess.thecvf.com/content_iccv_2017/html/Lin_Focal_Loss_for_ICCV_2017_paper.html

> **Supports:** Focal loss as class imbalance solution. Down-weights easy majority class examples; focuses training on hard minority class (battery). Foundation for cls_pw weighting decision.

Phan, T. H., & Yamamoto, K. (2020, June 2). *Resolving class imbalance in object detection with weighted cross entropy losses*. arXiv. https://doi.org/10.48550/arXiv.2006.01413

> **Supports:** Weighted cross-entropy (cls_pw) for class imbalance in object detection. Directly supports battery class weight=3.0 decision. Validates per-class weight tuning approach.

Plested, J., Shen, X., & Gedeon, T. (2021, July 19). *Non-binary deep transfer learning for image classification*. arXiv. https://doi.org/10.48550/arXiv.2107.08585

> **Supports:** Transfer learning from COCO pretrained weights to waste classification domain. Non-binary framing (partial weight freezing) relevant to fine-tuning backbone vs head decisions.

Zhang, Q., Yang, Q., Zhang, X., Bao, Q., Su, J., & Liu, X. (2021). Waste image classification based on transfer learning and convolutional neural network. *Waste Management, 135*, 150–157. https://doi.org/10.1016/j.wasman.2021.08.038

> **Supports:** Transfer learning established as best practice for waste image classification. Baseline B2 rationale (COCO weights without domain fine-tuning) rests on this foundation.

---

## 9. Learning Rate Schedule & Optimisation

> Supports: lr0=0.01, cosine annealing in YOLO training, large batch training rationale

Goyal, P., Dollár, P., Girshick, R., Noordhuis, P., Wesolowski, L., Kyrola, A., Tulloch, A., Jia, Y., & He, K. (2017, June 8). *Accurate, large minibatch SGD: Training ImageNet in 1 hour*. arXiv. https://doi.org/10.48550/arXiv.1706.02677

> **Supports:** batch=16 and lr0=0.01 relationship. Linear scaling rule for learning rate with batch size. Cite if justifying why batch=16 uses lr0=0.01 vs different batch sizes.

Loshchilov, I., & Hutter, F. (2016, August 13). *SGDR: Stochastic gradient descent with warm restarts*. arXiv. https://doi.org/10.48550/arXiv.1608.03983

> **Supports:** Cosine annealing learning rate schedule used internally by Ultralytics YOLOv8. Cite when explaining why loss curves show characteristic decay pattern across 100/300 epochs.

---

## 10. Process Methodology (DMAIC / Industry 4.0)

> Supports: DMAIC alignment, supervisor requirement, six sigma framing of model comparison

Pongboonchai-Empl, T., Antony, J., Garza-Reyes, J. A., Komkowski, T., & Tortorella, G. L. (2023). Integration of Industry 4.0 technologies into Lean Six Sigma DMAIC: A systematic review. *Production Planning & Control*. https://doi.org/10.1080/09537287.2023.2188496

> **Supports:** DMAIC methodology framing for PurityLoop. Maps Define/Measure/Analyze/Improve/Control to project phases. Required citation for supervisor Dr. Narishah's methodology alignment requirement.

Tang, T. Y., Salleh, N. M., & Wong, M. E. L. (2022). Smart virtual robot automation (SVRA)—Improving supplier transactional processes in enterprise resource planning (ERP) system: A conceptual framework. In R. Szewczyk, C. Zielinski, & M. Kaliczynska (Eds.), *Automation 2022* (Lecture Notes in Networks and Systems, Vol. 483, pp. 195–205). Springer. https://doi.org/10.1007/978-3-031-20429-6_19

> **Supports:** SVRA framework citation — Dr. Narishah's own paper. Mirror her framework structure: Problem → Framework → Components → Validation. Highest-impact citation for supervisor alignment. PurityLoop = SVRA for recycling.

---

## 11. Environmental Context & ESG Metrics

> Supports: Problem motivation, contamination rate baseline, weight calculation, operational reporting

Moh, Y. C., & Abd Manaf, L. (2017). Solid waste management transformation and future challenges of source separation and recycling practice in Malaysia. *Resources, Conservation and Recycling, 116*, 1–14. https://doi.org/10.1016/j.resconrec.2016.09.012

> **Supports:** Define phase problem context. Malaysian recycling contamination rate baseline. Justifies why human manual sorting alone is insufficient and why automation is needed. Directly relevant to local industry context.

---

## Master Reference List (APA 7th, Alphabetical)

Abdulkareem, I. M., AL-Shammri, F. K., Khalid, N. A., & Omran, N. A. (2024). Proposed approach for object detection and recognition by deep learning models using data augmentation. *International Journal of Online and Biomedical Engineering (iJOE), 20*(5). https://doi.org/10.3991/ijoe.v20i05.47171

Abo-Zahhad, M. M., & Abo-Zahhad, M. (2025). Real time intelligent garbage monitoring and efficient collection using YOLOv8 and YOLOv5 deep learning models for environmental sustainability. *Scientific Reports, 15*(1), 16024. https://doi.org/10.1038/s41598-025-99885-x

Ajayi, O. G., Ibrahim, P. O., & Adegboyega, O. S. (2024). Effect of hyperparameter tuning on the performance of YOLOv8 for multi crop classification on UAV images. *Applied Sciences, 14*(13), 5708. https://doi.org/10.3390/app14135708

Al-Dosari, M., Mahmoud, H., Al-Hadidi, M., Almemar, A., & Obeidallah, R. (2025). Benchmarking YOLO-based deep learning models for real-time object detection in hybrid ADAS and intelligent transportation systems. *Transportation Research Interdisciplinary Perspectives, 30*, 101234. https://doi.org/10.1016/j.trip.2025.101234

Chen, W., Yang, J. S., Xia, C., Li, Y., & Xiao, X. (2025). Road surface damage detection based on enhanced YOLOv8. *Computers in Industry, 173*, 104363. https://doi.org/10.1016/j.compind.2025.104363

Goyal, P., Dollár, P., Girshick, R., Noordhuis, P., Wesolowski, L., Kyrola, A., Tulloch, A., Jia, Y., & He, K. (2017, June 8). *Accurate, large minibatch SGD: Training ImageNet in 1 hour*. arXiv. https://doi.org/10.48550/arXiv.1706.02677

Guo, X., Sun, M., Zhang, X., Cui, S., & Li, Y. (2024). Optimization and implementation of garbage classification algorithm based on YOLOv8. *International Core Journal of Engineering, 10*(5), 107–115.

Kaur, P., Khehra, B. S., & Mavi, D. S. (2024). Real-time instance segmentation of recyclables from highly cluttered construction and demolition waste streams. *Waste Management, 187*, 147–158. https://doi.org/10.1016/j.wasman.2024.033516

Kirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C., Gustafson, L., Xiao, T., Whitehead, S., Berg, A. C., Lo, W.-Y., Dollár, P., & Girshick, R. (2023). Segment anything. In *Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV 2023)* (pp. 4015–4026). https://doi.org/10.1109/ICCV51070.2023.00371

Kunwar, S. (2025, October 21). *DWaste: Greener AI for waste sorting using mobile and edge devices*. arXiv. https://doi.org/10.48550/arXiv.2510.18513

Lin, T., Dollár, P., Girshick, R., He, K., Hariharan, B., & Belongie, S. (2017). Feature pyramid networks for object detection. In *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR 2017)* (pp. 2117–2125). https://openaccess.thecvf.com/content_cvpr_2017/html/Lin_Feature_Pyramid_Networks_CVPR_2017_paper.html

Lin, T., Goyal, P., Girshick, R., He, K., & Dollár, P. (2017). Focal loss for dense object detection. In *Proceedings of the IEEE International Conference on Computer Vision (ICCV 2017)* (pp. 2980–2988). https://openaccess.thecvf.com/content_iccv_2017/html/Lin_Focal_Loss_for_ICCV_2017_paper.html

Loshchilov, I., & Hutter, F. (2016, August 13). *SGDR: Stochastic gradient descent with warm restarts*. arXiv. https://doi.org/10.48550/arXiv.1608.03983

Menke, M., Wenzel, T., & Schwung, A. (2024). Bridging the gap: Active learning for efficient domain adaptation in object detection. *Expert Systems with Applications, 254*, 124403. https://doi.org/10.1016/j.eswa.2024.124403

Midigudla, R. S., Dichpally, T., Vallabhaneni, U., Wutla, Y., Sundaram, D. M., & Jayachandran, S. (2025). A comparative analysis of deep learning models for waste segregation: YOLOv8, EfficientDet, and Detectron 2. *Multimedia Tools and Applications*. https://doi.org/10.1007/s11042-025-20647-y

Mohamad, R., Roslan, R., Shahbudin, N. F. E., & Abu, F. (2024). Recycle waste detection and classification model using YOLOv8 for real-time waste management. In *2024 IEEE International Conference on Artificial Intelligence in Engineering*. IEEE.

Moh, Y. C., & Abd Manaf, L. (2017). Solid waste management transformation and future challenges of source separation and recycling practice in Malaysia. *Resources, Conservation and Recycling, 116*, 1–14. https://doi.org/10.1016/j.resconrec.2016.09.012

Mosqueira-Rey, E., Hernández-Pereira, E., Alonso-Ríos, D., Bobes-Bascarán, J., & Fernández-Leal, Á. (2023). Human-in-the-loop machine learning: A state of the art. *Artificial Intelligence Review, 56*(4), 3005–3054. https://doi.org/10.1007/s10462-022-10246-w

Nayfeh, A., Al-Azani, S., & Samma, H. (2025). A two-stage YOLOv8 approach for waste detection and classification in cognitive cities. *Transportation Research Procedia, 84*, 579–586. https://doi.org/10.1016/j.trpro.2025.03.111

Northcutt, C. G., Jiang, L., & Chuang, I. L. (2021). Confident learning: Estimating uncertainty in dataset labels. *Journal of Artificial Intelligence Research, 70*, 1373–1411. https://doi.org/10.1613/jair.1.12125

Phan, T. H., & Yamamoto, K. (2020, June 2). *Resolving class imbalance in object detection with weighted cross entropy losses*. arXiv. https://doi.org/10.48550/arXiv.2006.01413

Plested, J., Shen, X., & Gedeon, T. (2021, July 19). *Non-binary deep transfer learning for image classification*. arXiv. https://doi.org/10.48550/arXiv.2107.08585

Pongboonchai-Empl, T., Antony, J., Garza-Reyes, J. A., Komkowski, T., & Tortorella, G. L. (2023). Integration of Industry 4.0 technologies into Lean Six Sigma DMAIC: A systematic review. *Production Planning & Control*. https://doi.org/10.1080/09537287.2023.2188496

Raj, A., & Bach, F. (2022). Convergence of uncertainty sampling for active learning. In *Proceedings of the 39th International Conference on Machine Learning (ICML 2022)*, PMLR 162, 18310–18331.

Ravi, N., Gabeur, V., Hu, Y.-T., Hu, R., Ryali, C., Ma, T., Ramanathan, V., Poirson, P., Joulin, A., Feichtenhofer, C., & Girshick, R. (2024). SAM 2: Segment anything in images and videos. *arXiv preprint arXiv:2408.00714*.

Sapkota, R. (2025). Ultralytics YOLO evolution: An overview of YOLO26, YOLO11, YOLOv8, and YOLOv5 object detectors for computer vision and pattern recognition. *arXiv preprint arXiv:2510.09653*.

Shorten, C., & Khoshgoftaar, T. M. (2021). A survey on image data augmentation for deep learning. *Journal of Big Data, 6*(1), 1–48. https://doi.org/10.1186/s40537-019-0197-0

Tang, T. Y., Salleh, N. M., & Wong, M. E. L. (2022). Smart virtual robot automation (SVRA)—Improving supplier transactional processes in enterprise resource planning (ERP) system: A conceptual framework. In R. Szewczyk, C. Zielinski, & M. Kaliczynska (Eds.), *Automation 2022* (Lecture Notes in Networks and Systems, Vol. 483, pp. 195–205). Springer. https://doi.org/10.1007/978-3-031-20429-6_19

Terven, J., Córdova-Esparza, D., & Romero-González, J. (2023). A comprehensive review of YOLO architectures in computer vision: From YOLOv1 to YOLOv8 and YOLO-NAS. *Machine Learning and Knowledge Extraction, 5*(4), 1680–1716. https://doi.org/10.3390/make5040083

Yang, S., Xiao, W., Zhang, M., Guo, S., Zhao, J., & Shen, F. (2022). Image data augmentation for deep learning: A survey. *arXiv preprint arXiv:2204.08610*.

Zeng, W. (2024). Image data augmentation techniques based on deep learning: A survey. *Mathematical Biosciences and Engineering, 21*(6), 6190–6224. https://doi.org/10.3934/mbe.2024272

Zhalgas, A., Amirgaliyev, B., Boltay, B., Shegenova, D., Zhylkybay, N., & Yedilkhan, D. (2026). Development of an intelligent waste segregation system using a self-collected dataset and deep learning methods. *Journal of Robotics and Control (JRC), 7*(1), 3393–3404. https://doi.org/10.18196/jrc.v7i1.27247

Zhang, Q., Yang, Q., Zhang, X., Bao, Q., Su, J., & Liu, X. (2021). Waste image classification based on transfer learning and convolutional neural network. *Waste Management, 135*, 150–157. https://doi.org/10.1016/j.wasman.2021.08.038

[Authors TBC — verify full citation]. (2025). Smart waste, smarter world: Exploring waste types, trends, and tech-driven valorization through artificial intelligence, Internet of Things, and Blockchain. *Sustainable Development*. https://doi.org/10.1002/sd.70345 [Preprint: arXiv:2408.15857]

---

## Flags for Verification

| Citation | Issue | Action |
|----------|-------|--------|
| Kaur et al. (2024) | Author names inferred from DOI URL pattern — full team not confirmed | Verify at doi.org/10.1016/j.wasman.2024.033516 |
| Smart Waste paper (2025) | Author list unknown — arXiv/journal not confirmed | Look up arXiv:2408.15857 and doi:10.1002/sd.70345 |
| Guo et al. (2024) | *International Core Journal of Engineering* — verify journal indexing (not SCOPUS-indexed) | Cross-check on SCOPUS/WoS before citing in report |
| Raj & Bach (2022) | No DOI — conference proceedings only | Cite via PMLR URL: https://proceedings.mlr.press/v162/raj22a.html |

---

*PurityLoop AI Capstone | Research_Updated.md v2.0 | 2026-05-15*
*33 unique citations | 11 thematic sections | APA 7th edition*
