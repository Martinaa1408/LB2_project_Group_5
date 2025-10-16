# LAB2_project – Features extraction

This folder contains the notebook dedicated to the **Feature extraction** phase of the project: `Features_extraction_SVM.ipynb`.  
The main goal is to translate biological sequences into **numerical representations** that describe the biochemical characteristics of their **N-terminal region** — the part where signal peptides (SPs) are located.

---

## Objective
To extract a consistent set of **sequence-derived descriptors** that capture the compositional and physicochemical differences between proteins containing a signal peptide (SP+) and those without (SP–).

This step produces a feature matrix that will serve as input for the next step.

---

## Feature Overview

| Category | Description | Purpose |
|-----------|--------------|----------|
| **Amino Acid Composition** | Frequency of the 20 amino acids in the **first 22 residues**. | Captures overall residue bias of SPs (hydrophobic enrichment). |
| **Hydrophobicity** | Mean and maximum Kyte–Doolittle hydropathy values within the first 40 residues. | Quantifies the hydrophobic core typical of SPs. |
| **Charge** | Average and net positive charge (K/R vs D/E). | Detects positively charged N-regions. |
| **α-Helix Propensity** | Based on Chou–Fasman scale. | Reflects structural tendencies of the signal sequence. |
| **Size / Volume** | Mean and max residue volume. | Represents steric effects in the N-terminal. |

Each sequence is represented by approximately **30 numeric features**.

---

## ProtScale and AAindex
Some residue property scales used in this step were derived from:
- **ProtScale (ExPASy)** – a collection of amino acid property scales (e.g., hydrophobicity, flexibility, charge, polarity).  
- **AAindex** – a curated database of numerical indices representing physical and chemical properties of amino acids.

These resources were used to define custom **property dictionaries**, ensuring that the computed features reflect biologically validated residue properties.

---

## Workflow Summary
1. **Data loading:** import curated positive and negative sets (FASTA + TSV).  
2. **Truncation:** select N-terminal subsequences (first 22–40 residues).  
3. **Compositional features:** calculate relative frequency of amino acids.  
4. **Physicochemical features:** compute mean and max values from ProtScale and AAindex scales.  
5. **Aggregation:** combine all descriptors into a single table.  
6. **Export:** save the final feature matrix as `ML_features.tsv`.

---

## Output File

| File | Description |
|------|--------------|
| **`ML_features.tsv`** | Final feature matrix (rows = proteins, columns = extracted features). |

This file will be used as input for the next stage: **SVM model implementation and feature selection**.

---

**Next step →** proceed to [SVM_method](https://github.com/Martinaa1408/LB2_project_Group_5/tree/main/SVM_method)  
where the extracted features are normalized, selected (RandomForest/RFE), and used to train the Support Vector Machine classifier.
