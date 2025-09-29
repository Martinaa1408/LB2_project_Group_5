# LAB2 Project Group 5 – Prediction of Secretory Signal Peptides

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

**Tasks:**
-  Retrieve relevant datasets from UniProtKB  
-  Preprocess datasets for cross-validation and benchmarking  
-  Analyze and visualize dataset statistics  
-  Extract relevant features for classification  
-  Implement von Heijne’s algorithm  
-  Implement the SVM classifier  
-  Evaluate methods with cross-validation and blind test set  
-  Discuss and report results  
-  Prepare manuscript in scientific article format  
---

## Repository Structure

## Repository Structure

- [**Data_Collection/**](./Data_Collection)  
  Retrieval of raw datasets from UniProtKB.  
  → Main notebook: [`Data_Collection.ipynb`](./Data_Collection/Data_Collection.ipynb)

- [**Data_Preparation/**](./Data_Preparation)  
  Redundancy reduction with MMseqs2 and generation of train/benchmark sets with CV folds.  
  → Key scripts: [`clustering.sh`](./Data_Preparation/clustering.sh), [`get_tsv.py`](./Data_Preparation/get_tsv.py), [`get_sets.py`](./Data_Preparation/get_sets.py)

- [**Data_Analysis/**](./Data_Analysis)  
  Exploratory analysis of datasets (length distributions, amino acid composition, taxonomy, cleavage motifs).  
  → Main notebook: [`DataAnalysis.ipynb`](./Data_Analysis/DataAnalysis.ipynb)

- [**von Heijne/**](./vonHeijne)  
  Implementation of the von Heijne (1986) statistical method for SP cleavage site prediction.  
  → Main notebook: 

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
- **MMseqs2**: clustering and redundancy reduction  
- **Python 3**: data preprocessing and analysis (`pandas`, `scikit-learn`, `seaborn`)  
- **Bash utils**: `grep`, `wc`, `tr` for quick FASTA/TSV operations  
- **Jupyter/Colab**: environment for interactive workflows  
- **conda environment tools**: package and environment management  

### Key references 
- UniProt Consortium (2023). UniProt: the Universal Protein Knowledgebase. *NAR*.  
- MMseqs2 repository: [https://github.com/soedinglab/MMseqs2](https://github.com/soedinglab/MMseqs2)  
- Seaborn documentation: [https://seaborn.pydata.org/](https://seaborn.pydata.org/)  
- WebLogo: [https://weblogo.berkeley.edu/logo.cgi](https://weblogo.berkeley.edu/logo.cgi)
- SwissProt statistics: [https://web.expasy.org/docs/relnotes/relstat.html](https://web.expasy.org/docs/relnotes/relstat.html)
- von Heijne G. (1986). A new method for predicting signal sequence cleavage sites. *Nucleic Acids Res*.  
  
---

