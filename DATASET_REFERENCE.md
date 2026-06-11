# PurityLoop AI — Dataset Master Reference
**Updated:** 2026-05-17 v2 | **Path:** `e:/Capstone/dataset_master/`  
**Model:** YOLOv8m-seg | **Classes:** 9 | **Format:** YOLO seg

---

## Dataset Sources

| Dataset | Source | Images | Format | Status | Notes |
|---------|--------|--------|--------|--------|-------|
| TrashNet | kaggle/feyzazkefe/trashnet | 2,527 | Classif → pseudo-seg | ✅ | 6 classes baseline |
| TACO | github/pedropro/TACO | 1,500 | COCO polygon → YOLO seg | ✅ | Real polygon annotations |
| Garbage Classification v2 | kaggle/sumn2u/garbage-classification-v2 | 19,762 | Classif → pseudo-seg | ✅ | Has Battery class |
| Waste Classification 25k | kaggle/techsash/waste-classification-data | 25,077 | Classif → pseudo-seg | ✅ | Organic + Recyclable |
| RealWaste | kaggle/joebeachcapital/realwaste | 4,752 | Classif → pseudo-seg | ✅ | Real landfill env |
| Garbage Classification 12 | kaggle/mostafaabla/garbage-classification | ~15,000 | Classif → pseudo-seg | ✅ | 12 classes |
| Recyclable & Household Waste | kaggle/alistairking/... | 14,500 | Classif → pseudo-seg | ✅ | Fixed nested folders |
| Waste Classification v2 | kaggle/sapal6/waste-classification-data-v2 | 3,242 | Classif → pseudo-seg | ✅ | Non-recyclable → general_trash |
| Garbage Classification 6 | kaggle/asdasdasasdas/garbage-classification | 2,467 | Classif → pseudo-seg | ✅ | 6 classes backup |
| Chinese Trash Detection ⭐ | kaggle/cubeai/trash-detection-for-yolov8 | 6,004 | YOLO det bbox | ✅ | 18 Chinese classes → index map |
| WasteSense | kaggle/sumn2u/wastesense | 625 | Classif → pseudo-seg | ✅ | CC BY-NC 4.0 |
| Garbage Detection ⭐ NEW | kaggle/viswaprakash1990/garbage-detection | 10,464 | YOLO det bbox | ✅ | BIODEG/CARDBOARD/GLASS/METAL/PAPER/PLASTIC |
| E-Waste Classification NEW | kaggle/akshat103/e-waste-image-classification-dataset | 3,000 | Classif → pseudo-seg | ✅ | Battery→7, others→trash |
| E-Waste 18-class NEW | kaggle/harshadsgore/e-waste-image-classification-18-classes | 27,560 | Classif → pseudo-seg | ✅ | Battery=1,360 imgs |
| Waste Classification (kaanerkez) NEW | kaggle/kaanerkez/waste-classfication-dataset | 6,782 | Classif → pseudo-seg | ✅ | Battery=398 imgs |
| Unified Waste ⭐⭐ NEW | kaggle/siddhantmaji/unified-waste-classification-dataset | 64,000 | Classif → pseudo-seg | ✅ | 8,000/class × 8 — key battery source |
| Trash Detection (Roboflow) | roboflow/trash-detection-1fjjc | 0 | — | ❌ FAILED | GCS export cleared |
| YOLO Waste Detection (Roboflow) | roboflow/yolo-waste-detection | 0 | — | ❌ FAILED | 13,104 imgs — most valuable missing |
| Waste Detection vqkjo (Roboflow) | roboflow/waste-detection-vqkjo | 0 | — | ❌ FAILED | 58 imgs — low priority |

---

## Class Distribution — Final (2026-05-17, add-only)

**Balance strategy:** ADD data to underrepresented classes only. No removals.

**Total images:** 227,490

| Class | ID | Annotations | Notes |
|-------|----|-------------|-------|
| plastic | 0 | 46,588 | |
| paper | 1 | 23,915 | |
| cardboard | 2 | 17,754 | |
| metal | 3 | 24,220 | |
| glass | 4 | 30,030 | |
| textile | 5 | 17,734 | lowest class |
| food_organic | 6 | 139,909 | dominant — no removal per policy |
| battery | 7 | 12,814 | was 2,458 → boosted +421% ✓ |
| general_trash | 8 | 67,367 | |

**Imbalance ratio:** ~7.9:1 (food_organic / textile)  
**Battery improvement:** 2,458 → 12,814 (+421%)

---

## Roboflow Failure

All 3 Roboflow datasets fail — GCS export storage cleared on Free plan.  
Fix: app.roboflow.com → each project → Versions → regenerate export.  
Most valuable missing: `yolo-waste-detection` (13,104 images).

---

## Training

| Run | Script | Device | Params |
|-----|--------|--------|--------|
| Windows (active) | `train_seg_dml.py` | AMD RX 7800 XT DirectML | batch=4, epochs=100, patience=12 |
| Ubuntu Ferrari (pending) | `train_ferrari.py` | ROCm CUDA | batch=32, epochs=1000, patience=50 |

`data.yaml` path: `e:/Capstone/dataset_master/data.yaml`

> **Note:** food_organic dominant (139K vs textile 17K) — apply cls_weights or focal loss on Ferrari run.  
> Windows batch=4/accumulate=4 — DO NOT CHANGE.
