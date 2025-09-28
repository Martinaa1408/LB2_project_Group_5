# LAB2_project – Data Analysis

This stage explores the **statistical and biological properties** of the curated datasets using the Colab notebook `DataAnalysis.ipynb`.  
Training and benchmarking datasets are analysed **independently**, following the Practical Session guidelines.

Main goals:
- Verify the **quality and balance** of the datasets (handled per set),
- Detect potential **biases** (SP length, AA composition, taxonomy),
- Produce **reference statistics** and **sequence logos** around SP cleavage sites,
- Compare SP amino-acid composition against **SwissProt statistics** (see: https://web.expasy.org/docs/relnotes/relstat.html).

---

## Repository contents (this folder)

**Data / intermediates**
- `train_SP.seq` → SP sequences (training set), one sequence per line (plain text).
- `bench_SP.seq` → SP sequences (benchmark set), one per line.
- `train_logo.seq` → windows **[-13, +2]** around the annotated cleavage site (training), one per line.
- `bench_logo.seq` → windows **[-13, +2]** (benchmark), one per line.

> These `.seq` files are the **intermediate inputs** used to compute SP length stats and to generate the **WebLogo** figures.

---

## Workflow (per dataset: *training* and *benchmarking*)

> The **protein length distribution of full sequences** is **not included** in this repo.  
> The workflow below focuses on the analyses supported by the files actually present.

### 1) Signal Peptide (SP) Length Distribution
- **Objective:** analyse the distribution of SP lengths in the **positive** set.
- **Input:** `train_SP.seq`, `bench_SP.seq`
- **Rationale:** SPs typically fall in the **15–30 aa** range; outliers may indicate annotation issues.
- **Visualization:** histogram / density / boxplot (done in `DataAnalysis.ipynb`).
- **Expected output names:** `SP_lengths.png`

---

### 2) Amino Acid Composition (SP vs SwissProt)
- **Objective:** compare AA frequencies in SP sequences against the **SwissProt background**.
- **Input:** `train_SP.seq`, `bench_SP.seq` + SwissProt AA frequencies (see relnotes: https://web.expasy.org/docs/relnotes/relstat.html).
- **Rationale:** SPs show hydrophobic enrichment (H-region) and small residues near the cleavage site.
- **Visualization:** combined barplot (SP vs SwissProt).
- **Expected output names:** `residues_composition_.png`

---

### 3) Taxonomic Classification (optional, when metadata available)
- **Objective:** distribution by **kingdom** and **species** to check dataset bias.
- **Input:** metadata table (not committed in this folder).
- **Visualization:** pie chart / barplot.
- **Expected output names:** `kingdom_pie.png`, `taxonomy_distribution.png`

---

### 4) Cleavage-Site Motif Logos (WebLogo)
- **Objective:** visualize conserved motifs around SP cleavage sites using the **[-13, +2] window**.
- **Inputs (intermediate):**  
  - `train_logo.seq` (training windows)  
  - `bench_logo.seq` (benchmark windows)
- **Visualization:** sequence logos (AA) with WebLogo / Logomaker.
- **Output names:** `seq_logo_train.png`, `seq_logo_bench.png`

---

## Seaborn / Logomaker Notes

- **Seaborn** (Matplotlib-based) is used for quick statistical plotting directly from Pandas dataframes:
  - `displot` → distributions (histogram / kde),
  - `boxplot` / `violinplot` → group comparisons,
  - `barplot` / `countplot` → categorical data.
- **Logomaker** (Python) or **WebLogo** (CLI) are used to generate amino-acid logos from aligned or fixed-window sequences (provided in `*_logo.seq`).

---

## Current Results

| Step                        | Inputs                        | Output type            | Files now in repo / generated |
|-----------------------------|-------------------------------|------------------------|-------------------------------|
| SP sequences (intermediate) | curated positives             | `.seq` (plain text)    | `train_SP.seq`, `bench_SP.seq` |
| Cleavage windows (intermed.)| SP cleavage windows [-13,+2]  | `.seq` for logos       | `train_logo.seq`, `bench_logo.seq` |
| SP length distribution      | `train_SP.seq`, `bench_SP.seq`| Histogram / Boxplot    | `SP_lengths.png` |
| AA composition vs SwissProt | `*_SP.seq` + SwissProt stats  | Combined barplot       | `residues_composition_.png` |
| Motif logos                 | `*_logo.seq`                  | WebLogo / Logomaker    | `seq_logo_train.png`, `seq_logo_bench.png` |

---
