# LAB2_project - Data Preparation

This stage of the project focuses on generating **non-redundant and unbiased datasets** that can be used for training and benchmarking machine learning models. The process involves clustering, representative selection, TSV filtering, and final dataset splitting.

---

## Workflow Details

### 1. Clustering of protein sequences
Positive and negative datasets were clustered independently using **MMseqs2** in order to reduce redundancy and ensure that no highly similar proteins appear in both training and benchmarking sets.

**Main outputs:**
- `pos_cluster-results_cluster.tsv` / `neg_cluster-results_cluster.tsv`  
  Tables mapping each input sequence to its cluster representative.  
- `pos-cluster-results_rep_seq.fasta` / `neg-cluster-results_rep_seq.fasta`  
  FASTA files containing only the representative sequences (one per cluster).  

---

### 2. Extraction of representative IDs
Representative identifiers were retrieved directly from the FASTA headers of the MMseqs2 output.  

**Generated files:**
- `rep_positive.ids` → list of representative IDs for the positive dataset  
- `rep_negative.ids` → list of representative IDs for the negative dataset  

---

### 3. Filtering of original TSV files
The script **`get_tsv.py`** takes the representative ID lists (`.ids`) and the cluster mapping tables (`*_cluster.tsv`) as input. It produces reduced TSV files that contain only the representative entries.  

**Outputs:**
- `pos_cluster_results.tsv` → positive dataset, reduced to representatives  
- `neg_cluster_results.tsv` → negative dataset, reduced to representatives  

These files serve as the **non-redundant reference datasets** for downstream analysis.

---

### 4. Splitting into training and benchmarking sets
The script **`get_sets.py`** takes the representative ID lists (`.ids`) as input and generates:  

- **Training set (80%)**  
  Used for model training and hyperparameter tuning.  
  Within this set, each sequence is also assigned to one of **five cross-validation folds**, preserving the positive/negative ratio.  

- **Benchmarking set (20%)**  
  Held out and never used during model training, providing an unbiased evaluation of generalization performance.  

**Outputs in Cross_Validation/:**
- `pos_train.tsv` and `neg_train.tsv` → training data for positive and negative classes, including fold assignments  
- `pos_bench.tsv` and `neg_bench.tsv` → benchmarking data for positive and negative classes  

---

## Reproducibility

All data preparation steps (clustering, representative selection, TSV filtering, and train/benchmark splitting)  
are automated in the script [clustering.sh](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Preparation/clustering.sh):

```bash
bash clustering.sh
```

---
## About MMseqs2

**MMseqs2 (Many-against-Many sequence searching)** was used in this project to:  
- Cluster sequences based on **≥30% identity** and **≥40% alignment coverage**  
- Select a single representative per cluster  
- Prevent redundancy and overlap between subsets  

These thresholds are specifically chosen to minimize the risk of **data leakage**, which occurs if similar sequences are present in both training and benchmarking datasets.  

Official repository: [soedinglab/MMseqs2](https://github.com/soedinglab/MMseqs2)  

---

## Current Results

After clustering and representative selection:  

| Dataset   | Total sequences | Representative sequences | File containing representatives |
|-----------|----------------:|-------------------------:|---------------------------------|
| Positive  |     2,949       |      1093                | [POS CLUSTER TSV](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Preparation/Positive_Cluster/pos_cluster_results.tsv)      |
| Negative  |     20,615      |      8934                | [NEG CLUSTER TSV](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Preparation/Negative_Cluster/neg_cluster_results.tsv)        |

After splitting with `get_sets.py`:  

| Subset        | Positive | Negative | Files generated                  |
|---------------|---------:|---------:|----------------------------------|
| Training (80%)|   874   | 7147    | [POS TRAIN TSV](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Preparation/Cross_Validation/pos_train.tsv), [NEG TRAIN TSV](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Preparation/Cross_Validation/neg_train.tsv) |
| Benchmarking (20%) | 219 | 1787  | [POS BENCH TSV](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Preparation/Cross_Validation/pos_bench.tsv), [NEG BENCH TSV](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Preparation/Cross_Validation/neg_bench.tsv) |

Each sequence in the training set is also annotated with a **cross-validation fold index** (1–5).  

---
