# LAB2_project - von Heijne Method 

This module implements the **von Heijne method (1986)**, a motif–based statistical approach for predicting signal peptide (SP) cleavage sites.  
It is part of the practical session and complements machine learning classifiers by providing an interpretable, rule–based baseline.

## Method Overview
- **Cleavage site context**: 15 amino acids window (positions –13 to +1 relative to the cleavage site).  
- **Training data**: positive proteins with experimentally validated cleavage sites.  
- **Background model**: SwissProt amino acid frequencies.  
- **Pseudocounts**: smoothing value (=1) to avoid zero probabilities.  
- **PSWM construction**: log–odds ratios between observed frequencies and background.  
- **Scanning**: slide the 15-aa window across the first 90 residues of a candidate sequence; assign the maximum score.  
- **Thresholding**: classify as positive if score ≥ threshold (fixed or optimized).
