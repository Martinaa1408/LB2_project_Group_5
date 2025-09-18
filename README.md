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
│   │   └── negative.tsv
│   │
│   ├── Data_Collection.ipynb           # Jupyter/Colab for dataset retrieval
│   └── README.md                       # specific README for data collection
│
├── README.md         # main project README (global overview)
└── LICENSE
```
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
This project is part of the **Laboratory of Bioinformatics II** course (University of Bologna, 2025).  
We thank the course instructors and teaching assistants for their guidance, feedback, and support.  

---

## References & Tools
- **UniProtKB**: [https://www.uniprot.org/](https://www.uniprot.org/)  
- **scikit-learn**: [https://scikit-learn.org/](https://scikit-learn.org/)  
- **Jupyter/Colab** for analysis and dataset retrieval  
- von Heijne G. (1986) “A new method for predicting signal sequence cleavage sites.” *Nucleic Acids Res.*  
- State-of-the-art methods for signal peptide prediction (e.g. SignalP, Phobius) as references for benchmarking.
