# LAB2_project – Data Analysis

This stage of the pipeline explores the **statistical and biological properties** of the curated datasets using the Colab notebook `DataAnalysis.ipynb`.  
The main goals are to:
- Verify the **quality and balance** of the datasets,  
- Detect potential **biases** that may affect model training,  
- Generate **reference statistics** to benchmark predictive models.  

---

## Workflow

### 1. Protein Length Distribution
- **Objective:** Compare protein sequence lengths in the **positive** (SP-containing) and **negative** (non-SP) datasets.  
- **Rationale:** Major differences in sequence size could bias classifiers or indicate systematic errors in dataset construction.    

**Outputs:**  
- `length_distribution.png` → Histogram, density plot, and boxplot of protein lengths.  

---

### 2. Signal Peptide (SP) Length Distribution
- **Objective:** Analyze the distribution of SP lengths within the **positive dataset**.  
- **Rationale:** Signal peptides typically fall within a **15–30 amino acid range**; values outside this interval may indicate annotation errors.  

**Outputs:**  
- `sp_length_stats.png` → Histogram and table of descriptive statistics (mean, median, range).  

---

### 3. Amino Acid Composition
- **Objective:** Compare the amino acid frequencies of SP sequences against a **background distribution** (SwissProt).  
- **Rationale:** Signal peptides have well-known compositional biases (e.g., hydrophobic residues in the H-region, small residues near cleavage sites).  

**Outputs:**  
- `aa_composition.png` → Combined barplot of SP vs SwissProt amino acid composition.  

---

### 4. Taxonomic Classification
- **Objective:** Annotate sequences by **kingdom** (Eukaryotes, Bacteria, Archaea, etc.) and **species**.  
- **Rationale:** Datasets heavily skewed towards certain taxa may reduce model generalization.  

**Outputs:**  
- `taxonomy_distribution.png` → Pie charts and barplots of taxonomic representation.  

---

### 5. Cleavage-Site Motif Analysis
- **Objective:** Visualize conserved motifs around annotated cleavage sites.  
- **Rationale:** The **(-13 to +2) window** captures the N-region, H-region end, and cleavage position, which contain conserved residues essential for recognition.  

**Outputs:**  
- `cleavage_logo.png` → Sequence logo highlighting conserved residues near cleavage sites.  

---

## Seaborn Notes

Seaborn (built on Matplotlib) provides high-level functions for statistical plotting directly from Pandas dataframes.  
In this project it is applied to:  
- **displot** for distributions (hist/kde),  
- **boxplot/violinplot** for group comparisons,  
- **barplot/countplot** for categorical data.  

---

## Current Results

| Step                        | Dataset(s)         | Output type             | Content of `Plots/` |
|-----------------------------|--------------------|-------------------------|---------------------------|
| Protein length distribution | Positive / Negative| Histogram, Boxplot      | [length_distribution.png]() |
| SP length distribution      | Positive only      | Histogram, Stats table  | [sp_length_stats.png]()    |
| Amino acid composition      | SP vs SwissProt    | Barplot                 | [aa_composition.png]()      |
| Taxonomic classification    | Positive / Negative| Pie chart, Barplot      | [taxonomy_distribution.png]() |
| Cleavage-site motifs        | SP sequences       | WebLogo sequence logo   | [cleavage_logo.png]()       |

---
