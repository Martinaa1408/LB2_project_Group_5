# LAB2_project - Features Selection

This module implements the **feature extraction and selection stage** of the LB2 Signal Peptide Prediction project.  
The aim is to represent each protein sequence as a **numerical feature vector**, capturing both **compositional** and **physicochemical** information from its **N-terminal region** — the portion most relevant to signal peptide (SP) identification.

---

## Concept
Machine learning models require numeric input.  
To predict biological properties from sequences, each protein is **encoded** through a set of **biochemical descriptors** that summarize:
- Amino acid composition (first 22 residues)
- Local physicochemical trends (hydrophobicity, charge, α-helix, transmembrane, size)

These features can later be used as input for **SVM-based classification** (see the `SVM_Method` module).

---

## Workflow Summary
| Step | Description | Output |
|------|--------------|---------|
| **1. Data preparation** | Merge FASTA sequences with TSV annotations for positive and negative datasets. | Combined DataFrame with `seq_id`, `sequence`, `Class`. |
| **2. Scale definition** | Define residue property scales from ProtScale / AAindex (Kyte–Doolittle, Chou–Fasman, etc.). | Property dictionaries. |
| **3. Feature computation** | Calculate mean and max values of physicochemical scales using sliding windows. | Numerical descriptors. |
| **4. Amino acid composition** | Compute frequency of 20 amino acids in the first 22 residues. | 20D composition vector. |
| **5. Feature aggregation** | Concatenate all computed descriptors into a single feature matrix. | `ML_features.tsv`. |
| **6. Feature selection (optional)** | Identify the most informative features (RandomForest, RFE). | Reduced matrix. |

---

---

## Feature Overview

### **Compositional Features**
- Frequencies of the 20 standard amino acids in the **first 22 residues**.  
- Captures the distinctive residue distribution of signal peptides (non-polar enrichment).

### **Physicochemical Features**
Computed using **Biopython’s ProteinAnalysis** and numeric scales from ProtScale/AAindex:
| Property | Description | Features |
|-----------|-------------|-----------|
| Hydrophobicity | Kyte–Doolittle scale | max, mean |
| Charge | positive residue index | max, mean |
| α-helix propensity | Chou–Fasman scale | max, mean |
| Transmembrane propensity | TM helix scale | max, mean |
| Size | residue volume | max, mean |

Total of **10 physicochemical + 20 compositional = ~30 features per sequence**.

