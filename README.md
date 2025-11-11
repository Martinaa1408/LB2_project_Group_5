# LAB2 Project Group 5 – Prediction of Secretory Signal Peptides

[![Introduction – Signal Peptide Prediction](https://img.shields.io/badge/Introduction-Signal%20Peptide%20Prediction-blue)](https://virtuale.unibo.it/pluginfile.php/2682963/mod_resource/content/2/01c-IntroSP.pdf)
[![Data Collection](https://img.shields.io/badge/Data%20Collection-PDF-green)](https://virtuale.unibo.it/pluginfile.php/2682966/mod_resource/content/3/02a-Data%20collection.pdf)
[![Data Preparation](https://img.shields.io/badge/Data%20Preparation-PDF-orange)](https://virtuale.unibo.it/pluginfile.php/2682969/mod_resource/content/2/02b-Data%20preparation.pdf)
[![Data Analysis](https://img.shields.io/badge/Data%20Analysis-PDF-red)](https://virtuale.unibo.it/pluginfile.php/2682971/mod_resource/content/3/02c-Data%20analysis.pdf)
[![Von Heijne Method](https://img.shields.io/badge/Von%20Heijne-Method-purple)](https://virtuale.unibo.it/pluginfile.php/2682972/mod_resource/content/2/03-Methods-vonHeijne.pdf)
[![Evaluation of Classifiers](https://img.shields.io/badge/Evaluation-Classifiers-lightgrey)](https://virtuale.unibo.it/pluginfile.php/2682972/mod_resource/content/2/03-Methods-vonHeijne.pdf)
[![Feature extraction](https://img.shields.io/badge/Feature%20Extraction-PDF-yellowgreen)](https://virtuale.unibo.it/pluginfile.php/2814411/mod_resource/content/1/04-Methods-FeatureExtractionSelection.pdf)
[![SVM for SP detection](https://img.shields.io/badge/SVM%20for%20SP%20Detection-PDF-lightgrey)](https://virtuale.unibo.it/pluginfile.php/2682973/mod_resource/content/2/04-Methods-SVM.pdf)
[![Training Final Models and Analysis of Benchmarking Results](https://img.shields.io/badge/Benchmarking%20and%20Analysis-PDF-blue)](https://virtuale.unibo.it/pluginfile.php/2682977/mod_resource/content/2/06-Benchmarking%20and%20analysis%20of%20results.pdf)


## Table of Contents
- [About](#about)
- [Abstract](#abstract)
- [Project Work Plan](#project-work-plan)
- [Installation Guide](#installation-guide)
- [Repository Structure](#repository-structure)
- [Results Summary](#results-summary)
- [Authors](#authors)
- [License](#license)
- [Acknowledgements](#acknowledgements)
- [References & Tools](#references--tools)

---

## About
This repository contains the scripts, notebooks, and documentation for the **Laboratory of Bioinformatics II** project.  
The project addresses the **prediction of secretory signal peptides in eukaryotic proteins**, a crucial step for **protein function prediction** and **subcellular localization**.

---

## Abstract
Predicting secretory signal peptides (SPs) is fundamental for understanding protein localization and function.  
Traditional experimental methods are accurate but time-consuming, motivating the adoption of **computational approaches**.  

This project compares two main strategies for SP prediction:
1. **Motif-based statistical approach** (von Heijne, 1986)  
2. **Support Vector Machine (SVM)**-based classification (scikit-learn)  

The aim is to evaluate their performance using curated datasets from **UniProtKB**, applying cross-validation and benchmarking on a blind test set.  
In later stages, the pipeline may be extended to **neural networks** and **deep learning architectures** for advanced prediction.

---

## Project Work Plan

| Task | Description |
|------|-------------|
| Retrieve datasets | Collect relevant protein datasets from UniProtKB |
| Preprocess datasets | Prepare data for cross-validation and benchmarking |
| Analyze statistics | Compute and visualize dataset statistics |
| Feature extraction | Extract relevant features for classification |
| von Heijne’s algorithm | Implement cleavage site prediction method |
| SVM classifier | Train and test Support Vector Machine model |
| Evaluation | Assess methods with cross-validation and blind test set |
| Reporting | Discuss and interpret results |
| Manuscript | Prepare manuscript in scientific article format |

---

# Installation Guide

Python 3.8+ is required, along with the following main libraries:
`numpy`, `pandas`, `scikit-learn`, `matplotlib`, `seaborn`.

To set up the environment and run the project, follow these steps:

1. **Clone the repository**
  ```bash
  git clone https://github.com/Martinaa1408/LB2_project_Group_5.git
  cd LB2_project_Group_5
  ```

2. **Create and activate a virtual environment**
  ```bash
  python -m venv env
  source env/bin/activate        # On Windows use: env\Scripts\activate
  ```

3. **Install the required libraries**
  ```bash
  pip install numpy pandas scikit-learn matplotlib seaborn
  ```

4. **Run the Main Scripts**
   
---

## Repository Structure

- [**Data_Collection/**](./Data_Collection)  
  Retrieval of raw datasets from UniProtKB.  
  → Main notebook: `Data_Collection.ipynb`

- [**Data_Preparation/**](./Data_Preparation)  
  Redundancy reduction with MMseqs2 and generation of train/benchmark sets with CV folds.  
  → Key scripts: `clustering.sh`, `get_tsv.py`, `get_sets.py`

- [**Data_Analysis/**](./Data_Analysis)  
  Exploratory analysis of datasets (length distributions, amino acid composition, taxonomy, cleavage motifs).  
  → Main notebook: `DataAnalysis.ipynb`

- [**von_Heijne/**](./von_Heijne)  
  Implementation of the von Heijne (1986) statistical method for SP cleavage site prediction.  
  → Main notebook: `vonHeijne.ipynb`
  
- [**Features_extraction/**](./Features_extraction)
  Feature extraction from N-terminal regions (AA composition + physicochemical scales) and export of the feature matrix.  
  → Main notebook: `Features_extraction_SVM.ipynb`

- [**SVM_method/**](./SVM_method)
  Implementation of the Support Vector Machine (SVM) classifier with feature selection and hyperparameter optimization.  
  → Main notebook: `SVM_Method.ipynb`

- [**Evaluation_and_Comparison/**](./Evaluation_and_Comparison)
  Comparative analysis of SVM and von Heijne models using independent test sets and performance metrics visualization.  
  → Main notebook: `Evaluation_Comparison.ipynb`

- [**Supplementary_materials/**](./Supplementary_materials)
  Additional resources, figures, and intermediate files supporting the main notebooks and report.  
  → PDF document: `Support_materials_LB2_Group5.pdf`.

- [**Report/**](./Report)
  PDF version of the final report related to the project.
  →PDF document: `Report_LB2_Group5.pdf`
  
- [**README.md**](./README.md)  
  General project overview and workflow description.

- [**LICENSE**](./LICENSE)  
  Open-source license (GPL-3.0).

---

## Results Summary

This section summarizes the core data, feature extraction, and predictive performance achieved by the two implemented models — **Von Heijne (rule-based)** and **SVM (RBF kernel)**.

### Data Collection & Curation

| Phase | Description | SP⁺ | SP⁻ | Total | Notes |
|:------|--------------|----:|----:|------:|:------|
| **Raw UniProtKB** | Manually reviewed *S. cerevisiae* proteins with signal peptide annotation | 2,932 | 20,615 | 23,547 | Experimental annotations only |
| **After MMseqs2 clustering (30% ID)** | Non-redundant representative sequences | 1,093 | 8,934 | 10,027 | Removes homolog redundancy |
| **Final dataset split** | 80% training + 20% independent benchmark | 874 | 7,147 | 8,021 (train) <br> 219 / 1,787 (bench) | Balanced and taxonomically representative |

### Feature Extraction Summary

| Feature Category | Description | Example Features | Count |
|:------------------|-------------|------------------|------:|
| **Amino acid composition** | Residue frequencies in N-terminal region (–30 to +2 aa) | comp_L, comp_A, comp_V | 20 |
| **Hydrophobicity** | Kyte–Doolittle mean & max | hydro_mean, hydro_max | 2 |
| **Charge distribution** | Mean charge, max charge | charge_mean, charge_max | 2 |
| **Secondary structure** | α-helix propensity (Chou–Fasman scale) | alpha_mean, alpha_max | 2 |
| **Transmembrane propensity** | Mean & max TM index | trans_mean, trans_max | 2 |
| **Residue size/volume** | Mean and maximum residue volume | size_mean, size_max | 2 |

| Total features extracted | 29 |
| Features selected for SVM (RF importance) | **15** |

### Model Training and Optimization

| Step | Method | Details / Parameters | Output |
|:------|:--------|:--------------------|:---------|
| **Model 1** | **Von Heijne (rule-based)** | Position-Specific Weight Matrix (PSWM), optimized threshold by MCC | Cleavage-site scoring function |
| **Model 2** | **SVM (RBF kernel)** | `C = 10`, `γ = 'scale'`, kernel = RBF; Stratified 5-fold CV | Trained classifier on 15 features |

### Quantitative Performance

#### Internal Evaluation (Training / Validation Set)

| Metric | Von Heijne | SVM (RBF) |
|:--------|------------:|----------:|
| **Accuracy** | 0.930 | **0.972** |
| **Precision** | 0.665 | **0.896** |
| **Recall (TPR)** | 0.726 | **0.846** |
| **F1-score** | 0.694 | **0.870** |
| **MCC** | 0.656 | **0.855** |
| **ROC–AUC** | 0.905 | **0.980** |

#### External Evaluation (Independent Benchmark)

| Metric | Von Heijne | SVM (RBF) |
|:--------|------------:|----------:|
| **Accuracy** | 0.930 | **0.953** |
| **Precision** | 0.665 | **0.796** |
| **Recall (TPR)** | 0.726 | **0.767** |
| **F1-score** | 0.694 | **0.781** |
| **MCC** | 0.656 | **0.755** |

### Comparative Summary

| Model | Type | Accuracy | Precision | Recall | F1 | MCC | Strength |
|:-------|:------|----------:|-----------:|--------:|----:|----:|:----------|
| **Von Heijne** | Rule-based (PSWM) | 0.930 | 0.665 | 0.726 | 0.694 | 0.656 | Interpretable, motif-driven |
| **SVM (RBF)** | Machine Learning | **0.953** | **0.796** | **0.767** | **0.781** | **0.755** | Best overall performance |

### Key Observations

| Aspect | Von Heijne | SVM |
|:--------|:-------------|:----|
| **False Positives (FP)** | Hydrophobic TM helices (Metazoa bias) | Strongly reduced; fewer TM-related misclassifications |
| **False Negatives (FN)** | Short or polar SPs (<18 aa) | Borderline SPs with weak α-helix signals |
| **Motif capture** | Conserved `[A,V]XA` cleavage motif | Broader tolerance to sequence variability |
| **SP mean length** | 22.4 aa | 21.9 aa |
| **Interpretability** | High (biological motifs visible) | Moderate (feature-dependent) |

### Final Summary Table

| Dataset | Model | Accuracy | F1-score | MCC | Best For |
|:--------|:-------|----------:|----------:|----------:|:----------|
| **Training / Validation** | Von Heijne | 0.930 | 0.694 | 0.656 | Baseline biological interpretability |
| | SVM (RBF) | **0.972** | **0.870** | **0.855** | Pattern learning and discrimination |
| **Benchmark (Independent)** | Von Heijne | 0.930 | 0.694 | 0.656 | Motif-based baseline |
| | SVM (RBF) | **0.953** | **0.781** | **0.755** | Robust generalization |
 
The **SVM (RBF kernel)** outperforms the rule-based model on all quantitative metrics, maintaining excellent generalization to independent data while minimizing false positives.  
The **Von Heijne PSWM** remains biologically interpretable and complements the SVM by providing motif-level insight into cleavage-site conservation.

---

## Authors
This project has been developed by the following group members:

- **Martina Castellucci** – [@Martinaa1408](https://github.com/Martinaa1408)  
- **Alessia Corica** – [@alessia-corica](https://github.com/alessia-corica)  
- **Anna Rossi** – [@AnnaRossi01](https://github.com/AnnaRossi01)  
- **Sofia Natale** – [@sofianatale](https://github.com/sofianatale)  

---

## License
This project is released under the **[GPL-3.0 License](https://github.com/Martinaa1408/LB2_project_Group_5/tree/main?tab=License-1-ov-file)**.

---

## Acknowledgements
This project is part of the **[Laboratory of Bioinformatics II](https://www.unibo.it/en/study/course-units-transferable-skills-moocs/course-unit-catalogue/course-unit/2025/504345)** course (University of Bologna, 2025). 
We would like to thank Professors **Castrense Savojardo** and **Matteo Manfredi** for their guidance, feedback and continuous support throughout the project.

---

## References & Tools

### Software stack
- **[MMseqs2](https://github.com/soedinglab/MMseqs2)** — clustering and redundancy reduction  
- **Python 3** — data preprocessing and analysis  
- **[Biopython](https://biopython.org/wiki/Documentation)** — sequence handling, FASTA/TSV parsing, and biological data processing  
- **[scikit-learn (sklearn)](https://scikit-learn.org/stable/)** — machine learning framework (SVM, evaluation metrics, preprocessing)  
- **[NumPy](https://numpy.org/doc/stable/)** — numerical computation and matrix operations  
- **[Seaborn](https://seaborn.pydata.org/)** — statistical data visualization
- **[ProtScale (ExPASy)](https://web.expasy.org/protscale/)** — computation of physicochemical property scales (e.g. hydrophobicity)
- **[AAindex](https://www.genome.jp/aaindex/)** - is a curated database of numerical indices describing the physicochemical and biochemical properties of amino acids.
- **[SwissProt statistics](https://web.expasy.org/docs/relnotes/relstat.html)** — summary of protein counts, taxonomy coverage, and annotation status in                        UniProtKB/SwissProt releases.
- **[WebLogo generator](https://weblogo.berkeley.edu/logo.cgi)** — tool for visualizing sequence motifs and residue conservation (used for cleavage site motif analysis).
- **[PyTorch](https://www.geeksforgeeks.org/deep-learning/getting-started-with-pytorch/)** — deep learning framework for neural network modeling.
- **Bash utils** — quick FASTA/TSV operations  
- **Jupyter / Google Colab** — environment for interactive workflows  
- **conda environment tools** — package and environment management  

---

### Key references
- UniProt Consortium (2023). *UniProt: the Universal Protein Knowledgebase.* **Nucleic Acids Research**.  
- von Heijne G. (1986). *A new method for predicting signal sequence cleavage sites.* **Nucleic Acids Research**.
- Cortes C. & Vapnik V. (1995). *Support-Vector Networks.* **Machine Learning**, 20(3): 273–297.  
- Kyte J. & Doolittle R.F. (1982). *A simple method for displaying the hydropathic character of a protein.* **J. Mol.        Biol.**  
- Chou P.Y. & Fasman G.D. (1978). *Prediction of protein conformation.* **Biochemistry**.
- Grantham, R. (1974). *Amino acid difference formula to help explain protein evolution.* **Science**.  
- [scikit-learn SVM documentation](https://scikit-learn.org/stable/modules/svm.html)
