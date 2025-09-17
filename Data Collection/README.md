# LAB2_project – Data Collection

This folder contains the data, scripts and documentation for the Laboratory of Bioinformatics II project.  
The first step of the pipeline is the construction of two datasets of eukaryotic proteins from **UniProtKB**:

- **Positive set** → proteins with experimentally validated signal peptides.  
- **Negative set** → proteins without signal peptides, but experimentally localized in non-secretory compartments.  

---

## Positive Set (Signal Peptide proteins)

**Selection criteria:**
- No fragments (`fragment:false`)  
- Only eukaryotic proteins (`taxonomy_id:2759`)  
- Minimum sequence length ≥ 40 aa (`length:[40 TO *]`)  
- Only reviewed entries (`reviewed:true`)  
- Signal peptide with **experimental evidence** (`ft_signal_exp:`)  
- (Additional filtering: SP length > 14 aa, and cleaved)  

**Query used in UniProt graphical interface:**
(fragment:false) AND (taxonomy_id:2759) AND (length:[40 TO ]) AND (reviewed:true) AND (existence:1) AND (ft_signal_exp:)


**API URL (paginated, 500 entries per batch):**
https://rest.uniprot.org/uniprotkb/search?format=fasta&query=%28%28fragment%3Afalse%29+AND+%28taxonomy_id%3A2759%29+AND+%28length%3A%5B40+TO+*%5D%29+AND+%28reviewed%3Atrue%29+AND+%28existence%3A1%29+AND+%28ft_signal_exp%3A*%29%29&size=500

This query retrieves all **positive proteins** to build the dataset. Results are exported in both TSV (metadata) and FASTA (sequences).  

---

## Negative Set (Non-SP proteins)

**Selection criteria:**
- No fragments (`fragment:false`)  
- Only eukaryotic proteins (`taxonomy_id:2759`)  
- Minimum sequence length ≥ 40 aa (`length:[40 TO *]`)  
- Only reviewed entries (`reviewed:true`)  
- **No signal peptide** annotation (`NOT ft_signal`)  
- Experimentally localized to one of the following compartments:  
  - Cytosol (SL-0091)  
  - Nucleus (SL-0191)  
  - Mitochondrion (SL-0173)  
  - Plastid (SL-0209)  
  - Peroxisome (SL-0204)  
  - Cell membrane (SL-0039)  

**Query used in UniProt graphical interface:**
(reviewed:true) AND (fragment:false) AND (taxonomy_id:2759) AND (length:[40 TO *]) AND (existence:1) NOT (ft_signal:*) OR (cc_scl_term_exp:SL-0191) OR (cc_scl_term_exp:SL-0204) OR (cc_scl_term_exp:SL-0039) OR (cc_scl_term_exp:SL-0091) OR (cc_scl_term_exp:SL-0209) OR (cc_scl_term_exp:SL-0173)


**API URL (paginated, 500 entries per batch):**
https://rest.uniprot.org/uniprotkb/search?format=fasta&query=%28%28reviewed%3Atrue%29+AND+%28fragment%3Afalse%29+AND+%28taxonomy_id%3A2759%29+AND+%28length%3A%5B40+TO+*%5D%29+AND+%28existence%3A1%29+NOT+%28ft_signal%3A*%29+OR+%28cc_scl_term_exp%3ASL-0191%29+OR+%28cc_scl_term_exp%3ASL-0204%29+OR+%28cc_scl_term_exp%3ASL-0039%29+OR+%28cc_scl_term_exp%3ASL-0091%29+OR+%28cc_scl_term_exp%3ASL-0209%29+OR+%28cc_scl_term_exp%3ASL-0173%29%29&size=500

This query retrieves all **negative proteins**. For each entry, the TSV includes accession, organism, protein length, kingdom (derived from lineage), and a flag indicating whether a transmembrane helix is present in the first 90 residues.  

---

## Dataset Summary

| Dataset       | Proteins | Files |
|---------------|----------|-------|
| Positive Set  | 2,949    | [FASTA](Data_Collection/Positive_Set/uniprotkb_fragment_false_AND_taxonomy_i_2025_09_17(2).fasta.gz), [TSV](Data_Collection/Positive_Set/uniprotkb_fragment_false_AND_taxonomy_i_2025_09_17(2).tsv.gz) |
| Negative Set  | 20,615   | [FASTA](Data_Collection/Negative_Set/uniprotkb_fragment_false_AND_taxonomy_i_2025_09_17(1).fasta.gz), [TSV](Data_Collection/Negative_Set/uniprotkb_fragment_false_AND_taxonomy_i_2025_09_17(1).tsv.gz) |
