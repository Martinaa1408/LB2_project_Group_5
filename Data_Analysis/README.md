# LAB2_project - Data Analysis

This stage focuses on exploring the **statistical and biological properties** of the curated datasets.  
The goal is to verify dataset quality, uncover potential biases, and generate reference statistics for benchmarking predictive models.

---

## Workflow Details

### 1. Protein length distribution
Analysis of the overall protein length across positive and negative datasets.  
- Detects potential differences in sequence size.  
- Identifies outliers and ensures data consistency.  

**Outputs:**  
- Histograms, density plots, and boxplots of sequence lengths.

---

### 2. Signal peptide (SP) length distribution
Calculation of the distribution of SP lengths in the positive dataset.  
- Confirms expected biological ranges (typically 15–30 aa).  
- Useful for benchmarking cleavage-site predictions.  

**Outputs:**  
- Histogram and descriptive statistics of SP lengths.  

---

### 3. Amino acid composition
Comparison of amino acid frequencies in SP sequences against a background (e.g., SwissProt).  
- Highlights enrichment/depletion of specific residues.  
- Provides evidence for known SP features (hydrophobic core, polar N-region, small residues near cleavage site).  

**Outputs:**  
- Barplots of amino acid composition (SP vs background).  

---

### 4. Taxonomic classification
Annotation of sequences by **kingdom** and **species**.  
- Detects overrepresentation of specific organisms.  
- Helps assess generalization of the dataset.  

**Outputs:**  
- Pie charts and barplots of taxonomic distribution.  

---

### 5. Cleavage-site motif analysis
Extraction of sequence windows around annotated SP cleavage sites (typically -13 to +2).  
- Conserved motifs are visualized as **sequence logos**.  
- Provides benchmark motifs for predictive modeling.  

**Outputs:**  
- WebLogo plots showing conserved positions around cleavage sites.  

---

## Seaborn Notes

Seaborn (built on Matplotlib) provides high-level functions for statistical plotting directly from Pandas dataframes.  
In this project it is applied to:  
- **displot** for distributions (hist/kde),  
- **boxplot/violinplot** for group comparisons,  
- **barplot/countplot** for categorical data.  

---

## Current Results

| Step                        | Dataset(s)         | Output type             | Example file(s) / plot(s) |
|-----------------------------|--------------------|-------------------------|---------------------------|
| Protein length distribution | Positive / Negative| Histogram, Boxplot      | `length_distribution.png` |
| SP length distribution      | Positive only      | Histogram, Stats table  | `sp_length_stats.png`     |
| Amino acid composition      | SP vs SwissProt    | Barplot                 | `aa_composition.png`      |
| Taxonomic classification    | Positive / Negative| Pie chart, Barplot      | `taxonomy_distribution.png` |
| Cleavage-site motifs        | SP sequences       | WebLogo sequence logo   | `cleavage_logo.png`       |

---
