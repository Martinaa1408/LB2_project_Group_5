# LAB2 Project Group 5 – Prediction of Secretory Signal Peptides

[![Introduction – Signal Peptide Prediction](https://img.shields.io/badge/Introduction-Signal%20Peptide%20Prediction-blue)](https://virtuale.unibo.it/pluginfile.php/2682963/mod_resource/content/2/01c-IntroSP.pdf)
[![Data Collection](https://img.shields.io/badge/Data%20Collection-PDF-green)](https://virtuale.unibo.it/pluginfile.php/2682966/mod_resource/content/3/02a-Data%20collection.pdf)
[![Data Preparation](https://img.shields.io/badge/Data%20Preparation-PDF-orange)](https://virtuale.unibo.it/pluginfile.php/2682969/mod_resource/content/2/02b-Data%20preparation.pdf)
[![Data Analysis](https://img.shields.io/badge/Data%20Analysis-PDF-red)](https://virtuale.unibo.it/pluginfile.php/2682971/mod_resource/content/3/02c-Data%20analysis.pdf)
[![Von Heijne Method](https://img.shields.io/badge/Von%20Heijne-Method-purple)](https://virtuale.unibo.it/pluginfile.php/2682972/mod_resource/content/2/03-Methods-vonHeijne.pdf)
[![Evaluation of Classifiers](https://img.shields.io/badge/Evaluation-Classifiers-lightgrey)](https://virtuale.unibo.it/pluginfile.php/2682972/mod_resource/content/2/03-Methods-vonHeijne.pdf)
[![Feature extraction](https://img.shields.io/badge/Feature%20Extraction-PDF-yellowgreen)](https://virtuale.unibo.it/pluginfile.php/2814411/mod_resource/content/1/04-Methods-FeatureExtractionSelection.pdf)
[![SVM for SP detection](https://img.shields.io/badge/SVM%20for%20SP%20Detection-PDF-lightgrey)](https://virtuale.unibo.it/pluginfile.php/2682973/mod_resource/content/2/04-Methods-SVM.pdf)



## Table of Contents
- [About](#about)
- [Abstract](#abstract)
- [Project Work Plan](#project-work-plan)
- [Repository Structure](#repository-structure)
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

- [**README.md**](./README.md)  
  General project overview and workflow description.

- [**LICENSE**](./LICENSE)  
  Open-source license (GPL-3.0).

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
- **Bash utils** — quick FASTA/TSV operations  
- **Jupyter / Google Colab** — environment for interactive workflows  
- **conda environment tools** — package and environment management  

---

### Key references
- UniProt Consortium (2023). *UniProt: the Universal Protein Knowledgebase.* **Nucleic Acids Research**.  
- von Heijne G. (1986). *A new method for predicting signal sequence cleavage sites.* **Nucleic Acids Research**.  
- [SwissProt statistics](https://web.expasy.org/docs/relnotes/relstat.html)  
- [WebLogo generator](https://weblogo.berkeley.edu/logo.cgi)
