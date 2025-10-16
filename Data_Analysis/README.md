# LAB2_project – Data Analysis

In this stage we explored the **statistical and biological properties** of our curated datasets using the notebook [DataAnalysis.ipynb](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Analysis/DataAnalysis.ipynb).  
Both the **training** and **benchmarking** sets were analysed independently.
The idea was to check that the data are well balanced, to spot possible biases, and to generate reference plots that can also provide biological insight into signal peptide (SP) features.

---

## Analyses performed

### Protein length distribution  
We compared the lengths of proteins in the positive (SP-containing) and negative datasets.  
This check is important because large systematic differences in sequence size could bias the classifiers.  
The results are shown both as a **density plot** and as a **boxplot**, saved as:  
- `density_protein_lengths.png`  
- `boxplot_protein_length.png`

---

### Signal peptide (SP) length distribution  
We then focused only on the signal peptides themselves, measuring their lengths in both training and benchmarking sets.  
As expected, most SPs fall within the 15–30 amino acid window, but a few outliers were also observed.  
The combined plot is available in:  
- `SP_lengths.png`

---

### Amino acid composition  
Amino acid frequencies of SPs were compared against the **SwissProt background distribution**  
(see [SwissProt statistics](https://web.expasy.org/docs/relnotes/relstat.html)).  
This highlights the well-known compositional biases of SPs: enrichment in hydrophobic residues in the H-region and preference for small residues close to the cleavage site.  
The comparison is shown in a **barplot**:  
- `residues_composition.png`

---

### Taxonomic classification  
We looked at how the sequences are distributed across taxa, both at the kingdom and species levels.  
This is a useful control to ensure that our datasets are not overly dominated by a single lineage, which would reduce model generalization.  
The outputs are:  
- `kingdom_pie.png`  
- `barplot_species_train.png`  
- `barplot_species_bench.png`

---

### Cleavage-site motifs  
Finally, we visualized the conserved motifs around annotated cleavage sites by extracting the **[-13, +2] window** from each SP.  
These sequences were stored in [train_logo.seq](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Analysis/train_logo.seq) and [bench_logo.seq](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Analysis/bench_logo.seq) and then visualized using WebLogo/Logomaker.  
The resulting logos clearly show conserved small residues at the -1 and -3 positions.  
Plots:  
- `seq_logo_train.png`  
- `seq_logo_bench.png`

---

## Tools and libraries

Plots were generated mainly with **Seaborn** (on top of Matplotlib), using `displot` for distributions, `boxplot` for group comparisons and `barplot` for categorical frequencies.  
For the cleavage-site motifs we used **Logomaker** inside the notebook and **WebLogo** for the final sequence logos.  

---

## Summary of results

| Analysis                    | What we checked                                   | Output files |
|-----------------------------|--------------------------------------------------|--------------|
| Protein lengths             | Differences between positive and negative sets   | [Density protein lengths](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Analysis/Plots/density_protein_lengths.png), [Boxplot protein length](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Analysis/Plots/boxplot_protein_length.png) |
| SP lengths                  | Typical SP range (15–30 aa) and outliers         | [SP lengths](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Analysis/Plots/SP_lengths.png) |
| Amino acid composition      | Biases in SPs compared to SwissProt              | [Residues compositions](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Analysis/Plots/residues_compositions.png) |
| Taxonomy                    | Balance across kingdoms and species              | [Kingdom pie](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Analysis/Plots/kingdom_pie.png), [Barplot species train](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Analysis/Plots/barplot_species_train.png), [Barplot species bench](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Analysis/Plots/barplot_species_bench.png) |
| Cleavage-site motifs        | Conserved residues around cleavage site          | [Seq Logo train](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Analysis/Plots/seq_logo_train.png), [Seq Logo bench](https://github.com/Martinaa1408/LB2_project_Group_5/blob/main/Data_Analysis/Plots/seq_logo_bench.png) |

---

This set of analyses ensures that our datasets are well characterized and provides biological validation of known SP features, while also highlighting potential biases that could influence downstream machine learning models.

---

**Next step →**  
The exploratory analyses performed in this stage support two downstream modules:

- [von_Heijne](https://github.com/Martinaa1408/LB2_project_Group_5/edit/main/von_Heijne): implementation of a rule-based PSWM method to identify conserved cleavage-site motifs and provide a biological baseline.  
- [Feature_Extraction](https://github.com/Martinaa1408/LB2_project_Group_5/edit/main/Feature_Extraction): generation of numerical feature matrices (composition and physicochemical properties) for SVM-based classification.

Together, these two branches connect statistical motif discovery and machine learning–based modeling within a unified predictive framework.
