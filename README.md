# LAB2 Project Group 5 – Prediction of Secretory Signal Peptides

## Table of Contents
- [About](#about)
- [Abstract](#abstract)
- [Project Work Plan](#project-work-plan)
- [Current Progress](#current-progress)
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

**Tasks:**
-  Retrieve relevant datasets from UniProtKB  
-  Preprocess datasets for cross-validation and benchmarking  
-  Analyze and visualize dataset statistics  
-  Extract relevant features for classification  
-  Implement von Heijne’s algorithm  
-  Implement the SVM classifier  
-  Evaluate methods with cross-validation and blind test set  
-  Discuss and report results  
-  *(Optional)* Extend with advanced methods (NNs, DL)  
-  Prepare manuscript in scientific article format  
---

## Repository Structure
```bash
LB2_project_Group_5/
│
├── Data Collection/
│   ├── Positive Set/
│   │   ├── positive.fasta
│   │   └── positive.tsv
│   │
│   ├── Negative Set/
│   │   ├── negative.fasta
│   │   └── negative.tsv.
│   │
│   ├── Data_Collection.ipynb           # Jupyter/Colab for dataset retrieval
│   └── README.md                       # specific README for data collection
│
├── README.md         # main project README (global overview)
└── LICENSE
```
