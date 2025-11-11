# LAB2 Project – Evaluation and Comparison of Methods

This section presents the **final benchmarking and comparative evaluation** of two predictive strategies for **signal peptide (SP) prediction**:

| Method | Type | Implementation |
|---------|------|----------------|
| **Von Heijne** | Rule-based | Position-Specific Weight Matrix (PSWM) |
| **SVM** | Machine Learning | Support Vector Machine (RBF kernel, optimized) |

 **Notebook:** `Evaluation_and_comparison.ipynb`  


## Objective

The aim of this analysis is to quantitatively and qualitatively assess the predictive behavior of the **Von Heijne** model and the **SVM classifier** on an independent benchmark dataset, focusing on:

- **Classification metrics** and confusion matrices  
- **False positive (FP)** and **false negative (FN)** trends  
- **Cleavage-site motif conservation**  
- **Amino acid composition** and **signal peptide length**  
- **Feature-level deviations** (hydrophobicity, charge, TM propensity)

---

## Workflow Summary

| Step | Description | 
|------|--------------|
| **1. Benchmark dataset** | Curated subset of SP⁺ and SP⁻ proteins `benchmark_set.tsv` |
| **2. Model training** | PSWM built on canonical motifs; SVM retrained on extracted physicochemical features |
| **3. Prediction** | Classification of unseen benchmark proteins | 
| **4. Evaluation** | Metric computation and confusion matrices | 
| **5. Biological analysis** | Cleavage motif, AA composition, length, TM bias | 

---

## Quantitative Evaluation

| Metric | Von Heijne | SVM |
|:-------|:-----------:|:---:|
| **Accuracy** | 0.930 | **0.953** |
| **Precision** | 0.665 | **0.796** |
| **Recall (TPR)** | 0.726 | **0.767** |
| **F1-score** | 0.694 | **0.781** |
| **MCC** | 0.656 | **0.755** |

**Interpretation:**  
The **Von Heijne** model exhibits higher recall, identifying most true SPs but with slightly more false positives.  
Conversely, the **SVM** classifier adopts a stricter decision boundary, reducing false positives at the cost of marginally lower sensitivity.  
This trade-off reflects their distinct nature: heuristic motif scoring versus learned feature boundaries.

---

## Confusion Matrices

| Model | True Negatives | False Positives | False Negatives | True Positives |
|--------|----------------|-----------------|-----------------|----------------|
| **Von Heijne** | 1707 | 80 | 60 | 159 |
| **SVM** | 1594 | 193 | 201 | 18 |

**Interpretation:**  
- Von Heijne achieves higher recall but is more prone to FP misclassifications caused by transmembrane helices.  
- SVM minimizes FP but occasionally fails on marginal or short SPs, leading to slightly higher FN.

---

## False Positive Analysis

### (a) By Transmembrane Content
| Method | FP Transmembrane (%) | FP Non-Transmembrane (%) |
|---------|----------------------|---------------------------|
| **Von Heijne** | 53.8 | 46.2 |
| **SVM** | 15.0 | 85.0 |

The rule-based PSWM often confuses hydrophobic transmembrane helices with SPs due to similar N-terminal composition.  
The SVM integrates additional descriptors (charge, TM propensity, size) that reduce this bias.

### (b) By Taxonomic Kingdom
| Kingdom | Von Heijne FP (%) | SVM FP (%) |
|----------|-------------------|-------------|
| **Metazoa** | 66.2 | 52.8 |
| **Viridiplantae** | 20.0 | 19.7 |
| **Fungi** | 10.0 | 25.9 |
| **Other** | 3.8 | 1.6 |

Von Heijne is tuned toward **Metazoan** sequences, while the SVM distributes errors more evenly.  
Fungal sequences remain a weak point for both methods due to taxon-specific motif deviations.

---

## Motif Consistency and Length Distribution

Figures show the cleavage-site sequence logos and SP length profiles.

**Cleavage Motif:**  
- **False Negatives (FN)** display weakened `[A,V]XA` motifs and reduced upstream hydrophobicity.  
- **True Positives (TP)** retain canonical hydrophobic H-regions with the sharp H→C transition expected by Von Heijne’s rule.


**Signal Peptide Length Profile:**  
SPs cluster around **22 amino acids**, typical for eukaryotic signals.  
Misclassified SPs are often **shorter (<18 aa)** or **longer (25–30 aa)**, the latter primarily in fungal and plant proteins.

---

## Amino Acid Frequency and Composition

True positives display higher frequencies of **L, A, V**, defining the hydrophobic core critical for translocation.  
False negatives are enriched in **S, T, D, E**, polar residues that weaken hydrophobic signal and cleavage recognition.  
These patterns confirm that misclassifications originate from compositional shifts, not annotation bias.

---

## Feature-Level Comparison

Feature distributions (hydrophobicity, charge, TM propensity, etc.) reveal distinct profiles between FN and TP:

- **Charge (mean/max):** reduced in FN sequences  
- **TM Propensity:** elevated in FP regions  
- **Hydrophobicity:** remains the main discriminant feature

---

## Discussion

Overall, both models capture biologically meaningful trends:
- **Von Heijne** provides an interpretable and sensitive heuristic that effectively identifies canonical motifs but tends to overpredict hydrophobic TM helices.  
- **SVM** leverages nonlinear boundaries in physicochemical space, achieving higher precision and lower FP.  
- Errors in both models largely arise from **local deviations in hydrophobicity** and **motif strength**, not from dataset bias.

> In conclusion, SPs generally show enrichment in **L, A, V, M**, a conserved `[A,V]XA` motif, and average lengths around 22 residues.  
> FNs exhibit polar enrichment (S, T, D, E) and shortened hydrophobic cores (<18 aa), confirming that **compositional variability** is the main cause of reduced recognition.


---

## Output Files

| File | Description |
|------|--------------|
| [metrics_comparison] | Quantitative performance summary |
| [FP_comparisons](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Evaluation_and_Comparison/Plots/FP_comparisons.png) | FP composition and TM bias |
| [FP_kingdom_comparisons](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Evaluation_and_Comparison/Plots/FP_kingdom_comparisons.png) | FP distribution by kingdom |
| [residues_composition](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Evaluation_and_Comparison/Plots/residues_composition.png) | Amino acid frequency plot |
| [SP_lengths.png](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Evaluation_and_Comparison/Plots/SP_lenghts.png) | Signal peptide length distribution |
| [FN_features_distribution](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Evaluation_and_Comparison/Plots/FN_features_distribution.png), [TP_features_distribution](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Evaluation_and_Comparison/Plots/TP_features_distribution.png) | Density plots for main features |
| [boxplots_features_distribution_comparison](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Evaluation_and_Comparison/Plots/boxplots_features_distribution_comparison.png) | Feature-level TP vs. FN comparison |
| [logo_vonheijne_FN.png](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Evaluation_and_Comparison/Plots/logo_vonheijne_FN.png), [logo_vonheijne_TP.png](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Evaluation_and_Comparison/Plots/logo_vonheijne_TP.png) | Sequence logos around cleavage sites |

---

**Next step →** Integration of a **Multi-Layer Perceptron (MLP)** [Deep_Learning](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Deep_Learning).

