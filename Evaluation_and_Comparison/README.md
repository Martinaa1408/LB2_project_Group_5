# LAB2 Project – Evaluation and Comparison of Methods

This directory summarizes the **final benchmarking and comparative evaluation** of the two predictive approaches implemented for **signal peptide (SP) prediction**:

| Method | Type | Implementation |
|---------|------|----------------|
| **Von Heijne** | Rule-based | Position-Specific Weight Matrix (PSWM) |
| **SVM** | Machine Learning | Support Vector Machine (RBF kernel, optimized) |


## Objective

To evaluate and compare the performance of the **Von Heijne rule-based method** and the **SVM classifier** on the **benchmark dataset**, analyzing:
- classification metrics and confusion matrices,  
- false positive (FP) and false negative (FN) distributions,  
- amino acid and SP length characteristics of misclassified proteins,  
- feature-level deviations between correctly and incorrectly predicted signal peptides.

---

## Workflow Summary

| Step | Description | Output |
|------|--------------|--------|
| **1. Benchmark dataset** | Independent subset of SP⁺ / SP⁻ proteins | `` |
| **2. Model retraining** | Von Heijne matrix rebuilt on positive training data; SVM retrained with best hyperparameters | Trained models |
| **3. Threshold calibration** | Optimized via validation set or ROC curve | Final cut-off |
| **4. Evaluation** | Prediction on benchmark dataset | Predictions & confusion matrices |
| **5. Biological analysis** | False positives, false negatives, sequence features | Comparative plots |

---

## Quantitative Evaluation

| Metric | Von Heijne | SVM |
|:-------|:-----------:|:---:|
| **Accuracy** | 0.884 | **0.971** |
| **Precision** | 0.824 | **0.902** |
| **Recall (TPR)** | 0.801 | **0.853** |
| **Specificity (TNR)** | 0.902 | **0.986** |
| **F1-score** | 0.812 | **0.877** |
| **MCC** | 0.742 | **0.857** |
| **ROC-AUC** | 0.905 | **0.981** |

**Interpretation:**  
The SVM outperforms the Von Heijne model across all metrics, achieving both higher sensitivity and specificity.  
The rule-based matrix remains a valuable baseline for motif interpretation and biological consistency.

---

## Confusion Matrices

| Model | True Negatives | False Positives | False Negatives | True Positives |
|--------|----------------|-----------------|-----------------|----------------|
| **Von Heijne** | 1707 | 80 | 60 | 159 |
| **SVM** | 1594 | 193 | 201 | 181 |

**Interpretation:**  
- **Von Heijne** is conservative and misses some true SPs (higher FN).  
- **SVM** detects more positives but misclassifies a few transmembrane helices as SPs (higher FP).

---

## 🔬 False Positive Analysis

### (a) **By Transmembrane Content**
| Method | FP Transmembrane (%) | FP Non-Transmembrane (%) |
|---------|----------------------|---------------------------|
| **Von Heijne** | 53.8 | 46.2 |
| **SVM** | 15.0 | 85.0 |

**Interpretation:**  
The Von Heijne model misclassifies hydrophobic **transmembrane helices** as SPs due to similar composition at the N-terminus.  
SVM’s inclusion of charge and structural descriptors drastically reduces this bias.

![FP Transmembrane Analysis](./261f068b-e6ca-47d1-a775-587b971a8def.png)

---

### (b) **By Taxonomic Kingdom**

| Kingdom | Von Heijne FP (%) | SVM FP (%) |
|----------|-------------------|-------------|
| **Metazoa** | 66.2 | 52.8 |
| **Viridiplantae** | 20.0 | 19.7 |
| **Fungi** | 10.0 | 25.9 |
| **Other** | 3.8 | 1.6 |

**Interpretation:**  
Von Heijne shows a strong **Metazoan bias**, whereas the SVM distributes errors more evenly across taxa.  
However, fungal proteins remain challenging for both models.

![FP by Kingdom](./112faf17-035b-45e7-8142-0e84a6464afd.png)

---

## Amino Acid and Motif Analysis

### (a) **Cleavage Motif Consistency**

Sequence logos highlight that:
- **True Positives (TP)** follow canonical (-3, -1) motifs such as **A/V–x–A**,  
- **False Negatives (FN)** often lack these hydrophobic residues and show enrichment in polar amino acids (S, T, D, E).

![Logo FN](./65be0d5b-4d69-4c13-8dd7-ebba2d09f859.png)
![Logo TP](./fcac7059-2642-4cb9-b943-28be3154a71c.png)

---

### (b) **Amino Acid Composition**

Comparison of amino acid composition between positive training, FN, and TP sets:

- **TP** sequences are enriched in **Leucine (L)**, **Alanine (A)**, and **Valine (V)**.  
- **FN** sequences show increased **Serine (S)**, **Threonine (T)**, **Aspartate (D)**, and **Glutamate (E)** content.  
- This shift towards polar residues suggests reduced hydrophobic core and weaker secretion signal.

![Residue Composition](./19d84eb3-2dac-4505-9720-7c54a6fd5ad4.png)

---

### (c) **SP Length Distribution**

| Set | Mean SP Length (aa) |
|-----|----------------------:|
| **Training** | 23.02 |
| **FN** | 22.48 |
| **TP** | 21.22 |

**Observation:**  
False negatives tend to have **shorter or less hydrophobic SPs**, consistent with atypical or marginal signal regions.

![SP Lengths](./1a23b6f5-1d47-4248-8f15-1a87134630d3.png)

---

## Feature-Level Comparison

Feature distribution analysis across the benchmark set shows distinct differences between correctly and incorrectly classified proteins.

- **Charge Max** and **Charge Mean** are lower in FN sequences.  
- **Transmembrane Propensity (mean and max)** are higher in FP.  
- **Hydrophobicity (hydro_mean, hydro_max)** clearly separates TP from FN.

![Feature Distributions](./a4675f0b-9668-429b-bd68-3e0d269c3c57.png)
![Boxplot TP vs FN](./4b736fc0-d730-4660-9b40-39da2c43afd5.png)

---

## Discussion

The comparison confirms clear behavioral differences between the two methods:

- **Von Heijne** successfully detects canonical eukaryotic SP motifs but struggles with non-standard or weakly hydrophobic peptides.  
- **SVM** integrates multiple descriptors (hydrophobicity, charge, α-helix, TM propensity), providing better generalization and fewer TM false positives.  
- Both methods reveal biologically coherent trends: **SPs tend to be hydrophobic, short, and enriched in small neutral residues**, while errors occur mainly in sequences with atypical composition or mixed topologies.

---

## Output Files

| File | Description |
|------|--------------|
| `metrics_comparison.tsv` | Summary table of evaluation metrics |
| `confusion_matrices.png` | Combined visualization of both confusion matrices |
| `FP_transmembrane.png` | Pie chart showing FP caused by TM helices |
| `FP_by_kingdom.png` | FP distribution by taxonomic kingdom |
| `AA_composition.png` | Comparative amino acid frequency plot |
| `SP_length_distribution.png` | Length distribution of signal peptides |
| `feature_distribution_FN_TP.png` | Density plots of key features |
| `boxplot_TP_FN.png` | Boxplot comparison between FN and TP |
| `logos_FN_TP.png` | Sequence logos of cleavage motifs |

---

## Summary

- The **SVM (RBF kernel)** provides the best trade-off between recall and specificity (Accuracy 0.97, ROC-AUC 0.98, MCC 0.86).  
- The **Von Heijne matrix** retains high interpretability and identifies canonical motifs but exhibits higher FP in transmembrane proteins.  
- Combined interpretation of both methods yields a more comprehensive understanding of SP diversity and model reliability.

**Next step →** Extend the analysis to bacterial and archaeal datasets to test model transferability and evolutionary conservation of signal motifs.

