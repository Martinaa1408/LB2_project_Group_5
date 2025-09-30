# LAB2_project - von Heijne Method 

This module implements the **von Heijne (1986) statistical method** for detecting signal peptide (SP) cleavage sites.  
It provides an interpretable, frequency-based baseline that complements machine learning classifiers.

---

## Data

We use two datasets:

- **Positive set**: `von_pos.tsv`  
  Proteins with experimentally validated signal peptides.  
  Columns:  
  1. UniProt ID  
  2. Signal peptide sequence  
  3. Cleavage annotation  
  4. Additional info  
  5. Full protein sequence  

- **Negative set**: `von_neg.tsv`  
  Proteins without signal peptides, used as background.

From each entry, we extract a **16-residue window** around the cleavage site:
- 13 residues upstream (–13..–1)  
- 2 residues downstream (+1..+2)  

Only complete windows are retained.  
Typical results:  
- Positive windows (N_pos) = XXX  
- Negative windows (N_neg) = YYY  

---

## Methodology

1. **Window extraction**  
   Cleavage site is set at the **end of the annotated signal peptide** (length of column 2).  

2. **Count matrix**  
- Initialize with pseudocount = 1.  
- Matrix dimensions: 16 × 20 (positions × amino acids).  
- Rows = positions (–13..+2).  
- Columns = amino acids (`GAVPLIMFWYSTCNQHDEKR`).  
- Each window contributes +1 to the corresponding cell.

3. **PSPM (Position Specific Probability Matrix)**  
Normalize counts by *(N + 20)*, where *N* = number of sequences.  
Gives observed amino acid probabilities at each position.

4. **PSWM (Position Specific Weight Matrix)**  
Transform PSPM into log-odds ratios vs **SwissProt background frequencies**:  
```math
W_{a,j} = \log_2 \frac{P(a,j)}{b_a}
```
where:  
- (P(a,j)) = probability of amino acid *a* at position *j*  
- (b_a) = SwissProt frequency of *a*  

5. **Scoring**  
For a candidate 16-aa window:
```math
S = \sum_{j=-13}^{+2} W_{a_j,j}
```
- Compute **S_pos** using PSWM from positives.  
- Compute **S_neg** using PSWM from negatives.  
- Final discriminant:
  ```math
  \Delta S = S_{pos} - S_{neg}
  ```
If 
```math
\(\Delta S \geq \theta\)
```
classify as **signal peptide**.

6. **Sliding window**  
To scan a full protein, apply the PSWM in a sliding window (first 90 aa).  
The **maximum positional score** is taken as the global score for that sequence.

---

## Evaluation

Prediction is a **binary classification problem**:  
- Class 1 = protein with signal peptide  
- Class 0 = protein without signal peptide  

We report:  
- Accuracy  
- Precision  
- Recall / Sensitivity  
- Specificity  
- F1-score  
- MCC (Matthews correlation coefficient)  

All results are averaged over **k-fold cross-validation**, reported as mean ± standard error.  
**Threshold optimization is performed only on validation sets, never on the test set**.

---


