# LAB2_project - von Heijne Method 

This repository contains an implementation of the **Von Heijne statistical method (1986)** for signal peptide cleavage site prediction.  
It provides an interpretable, frequency-based baseline to compare against machine learning classifiers.

---

## **Method Overview**

The method builds a **Position-Specific Weight Matrix (PSWM)** from experimentally validated signal peptide sequences and compares them to background amino acid frequencies (SwissProt).  
Pseudocounts (+1) are added to avoid zero probabilities.  

- **Window size**: 16 amino acids (–13 upstream, +2 downstream of cleavage site)  
- **Background distribution**: SwissProt amino acid frequencies  
- **PSWM**: constructed from positive examples  
- **Scoring**: candidate windows are scored with the PSWM; the maximum score in the N-terminal region is used as prediction  

The log-odds formula for PSWM is:

```math
W_{k,j} = \log \left( \frac{M_{k,j}}{b_k} \right)
```
```math
M_{k,j}: \text{ probability of amino acid } k \text{ at position } j 
```
```math
b_k: \text{ background frequency of amino acid } k
```
```math
W_{k,j}: \text{ log-odds weight}
```

---

## **Implementation**

All steps are contained in a single notebook: [vonHeijne.ipynb](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/von_Heijne/vonHeijne.ipynb)

Pipeline:  
1. **Window extraction** from annotated cleavage sites  
2. **Count → PSPM → PSWM** (with pseudocount normalization)  
3. **Sliding window scoring** (scan N-terminal region, keep max score)  
4. **Threshold optimization** on validation set (F1 maximization)  
5. **Testing and cross-validation** with evaluation metrics  

---
## **Evaluation**

Binary classification task:  
- Class 1 = protein with signal peptide  
- Class 0 = protein without signal peptide  

Metrics reported:  
- **Accuracy (ACC):** proportion of correctly classified samples  
- **Precision (PPV):** fraction of predicted positives that are true positives  
- **Recall / Sensitivity:** fraction of actual positives correctly identified  
- **F1-score:** harmonic mean of precision and recall  
- **Matthews Correlation Coefficient (MCC):** balanced measure of binary classification quality (–1 to +1)  

Results are averaged over **5-fold cross-validation**, reported as **mean ± standard error**.  

### Final Metrics

Reported in the file: [vonHeijne_res.txt](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/von_Heijne/vonHeijne_res.txt)

| **Metric**   | **Value**            |
|--------------|----------------------|
| Accuracy     | 0.939 ± 0.002        |
| PPV          | 0.708 ± 0.017        |
| Sensitivity  | 0.756 ± 0.032        |
| F1 Score     | 0.728 ± 0.011        |
| MCC          | 0.697 ± 0.013        |
| Threshold    | 9.123                |

### Per-Fold Results

Detailed results of each fold are provided in [results_cv_set.txt](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/von_Heijne/results_cv_set.txt):  

| Fold | Accuracy | Sensitivity | PPV | F1 Score | MCC  | Confusion Matrix          |
|------|----------|-------------|-----|----------|------|---------------------------|
| 1    | 0.946    | 0.760       | 0.751 | 0.756  | 0.726 | [[1386, 44], [42, 133]]  |
| 2    | 0.941    | 0.686       | 0.755 | 0.719  | 0.687 | [[1391, 39], [55, 120]]  |
| 3    | 0.932    | 0.703       | 0.683 | 0.693  | 0.655 | [[1372, 57], [52, 123]]  |
| 4    | 0.936    | 0.743       | 0.695 | 0.718  | 0.683 | [[1372, 57], [45, 130]]  |
| 5    | 0.938    | 0.891       | 0.657 | 0.756  | 0.732 | [[1348, 81], [19, 155]]  |

**Observation:**  
- Performance is consistent across folds.  
- MCC remains stable (0.65–0.73), robust against class imbalance.  
- Fold 5 shows higher sensitivity but slightly lower precision.
---

## **Benchmarking**

After model optimization through cross-validation, the final evaluation was performed on an **independent test set** to assess the generalization ability of the Von Heijne statistical model.
Each sequence was scanned using the PSWM across the N-terminal region, and the **maximum score** was compared to the optimized threshold (**1.82**) to determine the presence of a signal peptide.

### Final Test Metrics

Reported in the file: [vonHeijne_bench_res.txt](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/von_Heijne/vonHeijne_bench_res.txt)

| **Metric**  | **Value** |
| ----------- | --------- |
| Accuracy    | 0.930     |
| PPV         | 0.665     |
| Sensitivity | 0.726     |
| F1 Score    | 0.694     |
| MCC         | 0.656     |
| Threshold   | 1.824     |

**Confusion Matrix:**
<p align="center">

| | Predicted Negative | Predicted Positive |
|---|---|---|
| **Actual Negative** | 1707 | 80 |
| **Actual Positive** | 60 | 159 |

</p>

**Observation:**
The model shows **consistent behavior** with the cross-validation phase, maintaining a good balance between **precision** and **sensitivity**.
This confirms the **robustness and interpretability** of the Von Heijne approach as a strong **baseline model** for signal peptide prediction.

The test sequences used for this benchmarking are provided in `vonHeijne_pos_test.tsv` and `vonHeijne_neg_test.tsv`, while `vonHeijne_final.tsv`
 contains all predicted scores and final classifications.

---

## **Visualization**

All plots are generated by the notebook and saved in: Plots/

| **Plot** | **Description** |
|----------|-----------------|
| [PR CURVE CONF MATRIX 1](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/von_Heijne/Plots/pr-rec-conf-mat-test1-val2.png) | Precision–Recall curve with optimal threshold and Confusion matrix (fold 1) |
| [PR CURVE CONF MATRIX 2](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/von_Heijne/Plots/pr-rec-conf-mat-test2-val3.png) | Precision–Recall curve with optimal threshold and Confusion matrix (fold 2) |
| [PR CURVE CONF MATRIX 3](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/von_Heijne/Plots/pr-rec-conf-mat-test3-val4.png) | Precision–Recall curve with optimal threshold and Confusion matrix (fold 3) |
| [PR CURVE CONF MATRIX 4](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/von_Heijne/Plots/pr-rec-conf-mat-test4-val5.png) | Precision–Recall curve with optimal threshold and Confusion matrix (fold 4) |
| [PR CURVE CONF MATRIX 5](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/von_Heijne/Plots/pr-rec-conf-mat-test5-val1.png) | Precision–Recall curve with optimal threshold and Confusion matrix (fold 5) |
| [PR CURVE ALL FOLDS](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/von_Heijne/Plots/precision_recall-curves-all-folds.png) | Combined Precision–Recall curves (all folds, with thresholds) |
| [HEATMAP PSWM](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/von_Heijne/Plots/heatmapPSWM.png) | Heatmap visualization of the Position-Specific Weight Matrix |

---

## **About NumPy**

**NumPy** was used for efficient array manipulation, linear algebra routines, and mathematical functions such as logarithms and means, which are essential in scientific computing.



